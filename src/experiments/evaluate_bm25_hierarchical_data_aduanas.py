from __future__ import annotations

import argparse
import csv
import json
import platform
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.1.csv")
DEFAULT_FLAT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_ABLATION_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_hierarchical_data_aduanas_clase87_v0.1")
DEFAULT_REPORT = Path("docs/evaluacion_bm25_jerarquico_dual_data_aduanas_clase87_v0.1.md")

QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
EXPECTED_EVALSET_ROWS = 1006
EXPECTED_SCOPE_CLASS = "87"
PRECISION_VARIANT = "C_hs6_leaf"
RECALL_VARIANT = "D_4d_hs6_leaf"
DUAL_METHOD = "BM25_dual_protected_top_5_backfill"
METHOD_ORDER = [
    "BM25_flat_current",
    "BM25_hierarchical_v0.1",
    DUAL_METHOD,
]
K_LIST = [1, 3, 5, 10]
RECALL_K_LIST = [50, 100]
FAMILY_K_LIST = [10, 50, 100]
RESULT_CANDIDATES = 10
FAILURE_SAMPLE_SIZE = 50


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _normalize_code(value: object) -> str:
    return re.sub(r"\D", "", _clean(value))


def _family_hit(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int) -> int:
    prefix = true_code[:prefix_len]
    if not prefix:
        return 0
    return int(any(_clean(hit.get("code")).startswith(prefix) for hit in hits[:k]))


def _top_codes(hits: Sequence[Mapping[str, Any]], limit: int = RESULT_CANDIDATES) -> str:
    return " ".join(_clean(hit.get("code")) for hit in hits[:limit])


def _dedupe_append(target: list[dict[str, Any]], seen: set[str], hits: Sequence[Mapping[str, Any]], limit: int | None = None) -> None:
    selected_hits = hits if limit is None else hits[:limit]
    for hit in selected_hits:
        code = _clean(hit.get("code"))
        if code and code not in seen:
            seen.add(code)
            target.append(dict(hit))


def _renumber(hits: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    ranked: list[dict[str, Any]] = []
    for rank, hit in enumerate(hits[:depth], start=1):
        item = dict(hit)
        item["rank"] = rank
        ranked.append(item)
    return ranked


def _protected_top_5_backfill(
    precision_hits: Sequence[Mapping[str, Any]],
    recall_hits: Sequence[Mapping[str, Any]],
    depth: int,
) -> list[dict[str, Any]]:
    fused: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(fused, seen, precision_hits, limit=5)
    _dedupe_append(fused, seen, recall_hits)
    _dedupe_append(fused, seen, precision_hits[5:])
    return _renumber(fused, depth)


def _validate_evalset(rows: Sequence[Mapping[str, str]], query_column: str, label_column: str) -> list[str]:
    warnings: list[str] = []
    if not rows:
        raise ValueError("Evalset is empty.")
    if len(rows) != EXPECTED_EVALSET_ROWS:
        raise ValueError(f"Evalset row count is {len(rows)}, expected {EXPECTED_EVALSET_ROWS}.")
    missing = [column for column in [query_column, label_column] if column not in rows[0]]
    if missing:
        raise ValueError(f"Missing required columns in evalset: {missing}")
    empty_queries = sum(1 for row in rows if not _clean(row.get(query_column)))
    invalid_labels = sum(1 for row in rows if not re.fullmatch(r"\d{8}", _normalize_code(row.get(label_column))))
    if empty_queries:
        raise ValueError(f"Found empty queries in {query_column}: {empty_queries}")
    if invalid_labels:
        raise ValueError(f"Found non-NANDINA8 expected labels in {label_column}: {invalid_labels}")
    non_scope = sum(1 for row in rows if _normalize_code(row.get(label_column))[:2] != EXPECTED_SCOPE_CLASS)
    if non_scope:
        warnings.append(f"{non_scope} rows have expected code outside Clase {EXPECTED_SCOPE_CLASS}.")
    return warnings


def _ensure_artifact(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Required artifact for {label} is missing: {path}")


def _method_metrics(rows: Sequence[Mapping[str, Any]], method: str) -> dict[str, Any]:
    ranks = [int(row["rank_ref"]) for row in rows if row["method"] == method]
    retrieved_counts = [int(row["retrieved_count"]) for row in rows if row["method"] == method]
    metrics: dict[str, Any] = {
        "cases_total": len(ranks),
        "cases_with_retrieval": sum(1 for count in retrieved_counts if count > 0),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "not_found_at_depth": sum(1 for rank in ranks if rank <= 0),
    }
    for k in K_LIST:
        metrics[f"top_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
    for k in RECALL_K_LIST:
        metrics[f"recall_at_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
    for k in FAMILY_K_LIST:
        metrics[f"partida_at_{k}"] = _mean([float(row[f"partida_at_{k}"]) for row in rows if row["method"] == method])
        metrics[f"sub_partida_at_{k}"] = _mean([float(row[f"sub_partida_at_{k}"]) for row in rows if row["method"] == method])
        metrics[f"clase_at_{k}"] = _mean([float(row[f"clase_at_{k}"]) for row in rows if row["method"] == method])
    return metrics


def _comparison_summary(case_rows: Sequence[Mapping[str, Any]], candidate: str, baseline: str, depth: int) -> dict[str, Any]:
    won = lost = unchanged = rescues_top10 = loses_top10 = 0
    rank_gains: list[float] = []
    rank_losses: list[float] = []
    for row in case_rows:
        candidate_rank = int(row[f"{candidate}_rank"])
        baseline_rank = int(row[f"{baseline}_rank"])
        candidate_value = candidate_rank if candidate_rank > 0 else depth + 1
        baseline_value = baseline_rank if baseline_rank > 0 else depth + 1
        if candidate_value < baseline_value:
            won += 1
            rank_gains.append(float(baseline_value - candidate_value))
        elif candidate_value > baseline_value:
            lost += 1
            rank_losses.append(float(candidate_value - baseline_value))
        else:
            unchanged += 1
        candidate_top10 = 0 < candidate_rank <= 10
        baseline_top10 = 0 < baseline_rank <= 10
        rescues_top10 += int(candidate_top10 and not baseline_top10)
        loses_top10 += int(baseline_top10 and not candidate_top10)
    return {
        "baseline": baseline,
        "candidate": candidate,
        "ganados": won,
        "perdidos": lost,
        "sin_cambio": unchanged,
        "ganancia_media_rank_cuando_mejora": _mean(rank_gains),
        "perdida_media_rank_cuando_empeora": _mean(rank_losses),
        "candidate_rescues_top10_baseline_not": rescues_top10,
        "baseline_hits_top10_candidate_not": loses_top10,
    }


def _format_metric(value: object) -> str:
    return f"{float(value):.4f}"


def _summary_markdown(metrics: Mapping[str, Any]) -> str:
    lines = [
        "# Evaluacion BM25 jerarquico/dual data_aduanas clase 87 v0.1",
        "",
        "## Objetivo",
        "",
        "Reevaluar, de forma acotada, las variantes normativas previamente definidas en Fase 6B/6C sobre el nuevo evalset `data_aduanas` Clase = 87. Esta corrida no rehace la busqueda de variantes ni ajusta reglas mirando el evalset.",
        "",
        "## Por que no se rehace toda Fase 6B/6C",
        "",
        "Fase 6B/6C historica conserva su rol exploratorio sobre devset/evalset anterior. En esta actualizacion solo se valida si los recuperadores normativos ya congelados siguen aportando como trazabilidad o respaldo sobre descripciones comerciales clase 87.",
        "",
        "## Variantes evaluadas",
        "",
    ]
    for method, artifact in metrics["artifacts_used"].items():
        lines.append(f"- `{method}`: {artifact}.")
    if metrics["variants_not_evaluated"]:
        lines.append("- Variantes no evaluadas: " + "; ".join(metrics["variants_not_evaluated"]))
    lines.extend(
        [
            "",
            "## Evalset",
            "",
            f"- Archivo: `{metrics['input']['evalset_path']}`.",
            f"- Filas evaluadas por metodo: {metrics['validations']['rows_per_method_expected']}.",
            f"- Columna de consulta: `{metrics['columns']['query_column']}`.",
            f"- Etiqueta esperada: `{metrics['columns']['label_column']}`.",
            "",
            "## Metricas",
            "",
            "| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | Partida@10 | Partida@50 | Partida@100 | Sub Partida@10 | Sub Partida@50 | Sub Partida@100 | Clase@10 | Clase@50 | Clase@100 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for method in metrics["method_order"]:
        m = metrics["metrics_by_method"][method]
        lines.append(
            f"| {method} | {_format_metric(m['top_1'])} | {_format_metric(m['top_3'])} | {_format_metric(m['top_5'])} | {_format_metric(m['top_10'])} | {_format_metric(m['mrr'])} | {_format_metric(m['recall_at_50'])} | {_format_metric(m['recall_at_100'])} | {_format_metric(m['partida_at_10'])} | {_format_metric(m['partida_at_50'])} | {_format_metric(m['partida_at_100'])} | {_format_metric(m['sub_partida_at_10'])} | {_format_metric(m['sub_partida_at_50'])} | {_format_metric(m['sub_partida_at_100'])} | {_format_metric(m['clase_at_10'])} | {_format_metric(m['clase_at_50'])} | {_format_metric(m['clase_at_100'])} |"
        )
    flat = metrics["phase4_reference"]
    lines.extend(
        [
            "",
            "## Comparacion con BM25 plano Fase 4 actualizada",
            "",
            f"La referencia Fase 4 clase 87 reporto Top-10 = {flat['top_10']:.4f}, MRR = {flat['mrr']:.4f}, Recall@100 = {flat['recall_at_100']:.4f}, Partida@100 = {flat['partida_at_100']:.4f}, Sub Partida@100 = {flat['sub_partida_at_100']:.4f} y Clase@100 = {flat['clase_at_100']:.4f}. La corrida actual recalcula `BM25_flat_current` con el mismo evalset e indice plano para dejar una comparacion por metodo en el mismo archivo.",
            "",
            "## Lectura metodologica",
            "",
            metrics["methodological_reading"],
            "",
            "## Decision",
            "",
            metrics["methodological_decision"],
            "",
            "## Advertencia de comparabilidad",
            "",
            "Estas metricas no sustituyen ni corrigen las cifras historicas de Fase 6B/6C: cambian fuente, distribucion y alcance del evalset. La comparacion valida solo el uso auxiliar de variantes normativas sobre `data_aduanas` clase 87.",
            "",
            "## Controles",
            "",
            "- No se ejecuto LLM.",
            "- No se ejecuto Ollama.",
            "- No se ejecuto Text2Trade.",
            "- No se usaron APIs remotas.",
            "- No se modificaron evalset historico, devset historico ni splits clase 87.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    evalset_path = resolve_project_path(args.evalset)
    flat_index_path = resolve_project_path(args.flat_index)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    ablation_index_dir = resolve_project_path(args.ablation_index_dir)
    precision_index_path = ablation_index_dir / f"{PRECISION_VARIANT}.pkl"
    recall_index_path = ablation_index_dir / f"{RECALL_VARIANT}.pkl"
    output_dir = resolve_project_path(args.output_dir)
    report_path = resolve_project_path(args.report)
    depth = max(args.retrieval_depth, max(RECALL_K_LIST), max(FAMILY_K_LIST), max(K_LIST))

    _ensure_artifact(evalset_path, "data_aduanas evalset clase 87")
    _ensure_artifact(flat_index_path, "BM25_flat_current")
    _ensure_artifact(hierarchical_index_path, "BM25_hierarchical_v0.1")
    _ensure_artifact(precision_index_path, PRECISION_VARIANT)
    _ensure_artifact(recall_index_path, RECALL_VARIANT)

    eval_rows = _read_csv(evalset_path)
    warnings = _validate_evalset(eval_rows, args.query_column, args.label_column)

    start = time.time()
    flat_index = load_bm25_index(flat_index_path)
    hierarchical_index = load_bm25_index(hierarchical_index_path)
    precision_index = load_bm25_index(precision_index_path)
    recall_index = load_bm25_index(recall_index_path)

    results_by_method: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []
    for position, eval_row in enumerate(eval_rows, start=1):
        query = _clean(eval_row.get(args.query_column))
        expected = _normalize_code(eval_row.get(args.label_column))
        flat_hits = retrieve(flat_index, query, top_n=depth)
        hierarchical_hits = retrieve(hierarchical_index, query, top_n=depth)
        precision_hits = retrieve(precision_index, query, top_n=depth)
        recall_hits = retrieve(recall_index, query, top_n=depth)
        dual_hits = _protected_top_5_backfill(precision_hits, recall_hits, depth=depth)
        method_hits = {
            "BM25_flat_current": flat_hits,
            "BM25_hierarchical_v0.1": hierarchical_hits,
            DUAL_METHOD: dual_hits,
        }
        case_id = _clean(eval_row.get("case_id")) or f"data-aduanas-eval-{position:05d}"
        case_row: dict[str, Any] = {
            "case_id": case_id,
            "query": query,
            "nandina_ref": expected,
            "partida_ref": expected[:4],
            "sub_partida_ref": expected[:6],
            "clase_ref": expected[:2],
        }
        for method, hits in method_hits.items():
            rank = rank_of_true(hits, expected)
            result: dict[str, Any] = {
                "method": method,
                "case_id": case_id,
                "query": query,
                "nandina_ref": expected,
                "partida_ref": expected[:4],
                "sub_partida_ref": expected[:6],
                "clase_ref": expected[:2],
                "rank_ref": rank,
                "retrieved_count": len(hits),
                "top_codes": _top_codes(hits),
            }
            for k in K_LIST:
                result[f"hit_top_{k}"] = int(acc_at_k(rank, k))
            for k in RECALL_K_LIST:
                result[f"hit_recall_{k}"] = int(acc_at_k(rank, k))
            for k in FAMILY_K_LIST:
                result[f"partida_at_{k}"] = _family_hit(hits, expected, 4, k)
                result[f"sub_partida_at_{k}"] = _family_hit(hits, expected, 6, k)
                result[f"clase_at_{k}"] = _family_hit(hits, expected, 2, k)
            for candidate_rank in range(1, RESULT_CANDIDATES + 1):
                hit = hits[candidate_rank - 1] if candidate_rank <= len(hits) else None
                result[f"candidate_{candidate_rank}_code"] = _clean(hit.get("code")) if hit else ""
                result[f"candidate_{candidate_rank}_score"] = hit.get("score", "") if hit else ""
                result[f"candidate_{candidate_rank}_text"] = _clean(hit.get("text")) if hit else ""
            results_by_method.append(result)

            case_row[f"{method}_rank"] = rank
            case_row[f"{method}_top10_codes"] = _top_codes(hits)
            case_row[f"{method}_partida_at_100"] = result["partida_at_100"]
            case_row[f"{method}_sub_partida_at_100"] = result["sub_partida_at_100"]
            case_row[f"{method}_clase_at_100"] = result["clase_at_100"]
        case_rows.append(case_row)

    metrics_by_method = {method: _method_metrics(results_by_method, method) for method in METHOD_ORDER}
    comparisons = {
        "hierarchical_vs_flat": _comparison_summary(case_rows, "BM25_hierarchical_v0.1", "BM25_flat_current", depth),
        "dual_vs_flat": _comparison_summary(case_rows, DUAL_METHOD, "BM25_flat_current", depth),
        "dual_vs_hierarchical": _comparison_summary(case_rows, DUAL_METHOD, "BM25_hierarchical_v0.1", depth),
    }

    hierarchical = metrics_by_method["BM25_hierarchical_v0.1"]
    dual = metrics_by_method[DUAL_METHOD]
    flat_current = metrics_by_method["BM25_flat_current"]
    if hierarchical["top_10"] >= flat_current["top_10"] or hierarchical["recall_at_100"] >= flat_current["recall_at_100"]:
        hierarchical_role = "`BM25_hierarchical_v0.1` se conserva como recuperador normativo auxiliar de trazabilidad."
    else:
        hierarchical_role = "`BM25_hierarchical_v0.1` no aporta frente al plano en este evalset y queda como evidencia historica."
    if dual["recall_at_100"] > flat_current["recall_at_100"] or dual["recall_at_100"] > hierarchical["recall_at_100"]:
        dual_role = "`BM25_dual_protected_top_5_backfill` se conserva solo como fuente auxiliar de cobertura profunda."
    else:
        dual_role = "`BM25_dual_protected_top_5_backfill` no aporta cobertura adicional suficiente y queda como evidencia historica."
    methodological_reading = (
        "La familia normativa mantiene alta senal de Clase@100, pero sigue lejos de resolver exactitud NANDINA8 "
        "sobre descripciones comerciales clase 87. La comparacion confirma que estas variantes son utiles como "
        "trazabilidad y respaldo, no como recuperador principal cuando exista evidencia historica."
    )
    methodological_decision = f"{hierarchical_role} {dual_role} No se promueven como ranking principal para clase 87."

    rows_per_method = {
        method: sum(1 for row in results_by_method if row["method"] == method)
        for method in METHOD_ORDER
    }
    if any(count != EXPECTED_EVALSET_ROWS for count in rows_per_method.values()):
        raise ValueError(f"Unexpected rows per method: {rows_per_method}")

    phase4_reference = {
        "top_10": 0.0467,
        "mrr": 0.0312,
        "recall_at_100": 0.0626,
        "partida_at_100": 0.1252,
        "sub_partida_at_100": 0.0755,
        "clase_at_100": 0.8887,
    }
    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_hierarchical_data_aduanas",
        "execution": {
            "datetime_utc": datetime.now(timezone.utc).isoformat(),
            "timestamp_unix": int(time.time()),
            "elapsed_seconds": time.time() - start,
            "environment": {
                "python_version": platform.python_version(),
                "system": platform.system(),
                "release": platform.release(),
                "machine": platform.machine(),
            },
        },
        "input": {
            "evalset_path": _rel(evalset_path, root),
            "evalset_sha256": sha256_file(evalset_path),
            "flat_index_path": _rel(flat_index_path, root),
            "flat_index_sha256": sha256_file(flat_index_path),
            "hierarchical_index_path": _rel(hierarchical_index_path, root),
            "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
            "precision_variant": PRECISION_VARIANT,
            "precision_index_path": _rel(precision_index_path, root),
            "precision_index_sha256": sha256_file(precision_index_path),
            "recall_variant": RECALL_VARIANT,
            "recall_index_path": _rel(recall_index_path, root),
            "recall_index_sha256": sha256_file(recall_index_path),
        },
        "columns": {
            "query_column": args.query_column,
            "label_column": args.label_column,
        },
        "scope": {
            "source": "data_aduanas",
            "class": EXPECTED_SCOPE_CLASS,
            "evalset_role": "updated Phase 3 class 87 evaluation split",
        },
        "method_order": METHOD_ORDER,
        "artifacts_used": {
            "BM25_flat_current": _rel(flat_index_path, root),
            "BM25_hierarchical_v0.1": _rel(hierarchical_index_path, root),
            DUAL_METHOD: f"{_rel(precision_index_path, root)} + {_rel(recall_index_path, root)}",
        },
        "variants_not_evaluated": [
            "A/B/E/F/G no se reejecutan porque esta actualizacion solo valida variantes normativas previamente utiles.",
        ],
        "bm25_config": {
            "retrieval_depth": depth,
            "protected_top_n": 5,
            "k_list": K_LIST,
            "recall_k_list": RECALL_K_LIST,
            "family_k_list": FAMILY_K_LIST,
            "flat_docs": len(flat_index.doc_ids),
            "hierarchical_docs": len(hierarchical_index.doc_ids),
            "precision_docs": len(precision_index.doc_ids),
            "recall_docs": len(recall_index.doc_ids),
        },
        "metrics_by_method": metrics_by_method,
        "comparisons": comparisons,
        "phase4_reference": phase4_reference,
        "methodological_reading": methodological_reading,
        "methodological_decision": methodological_decision,
        "validations": {
            "evalset_rows": len(eval_rows),
            "results_rows": len(results_by_method),
            "rows_per_method": rows_per_method,
            "rows_per_method_expected": EXPECTED_EVALSET_ROWS,
            "empty_queries": 0,
            "invalid_expected_labels": 0,
            "expected_labels_nandina8": True,
            "metrics_recomputed_from_results": True,
            "llm_executed": False,
            "ollama_executed": False,
            "text2trade_executed": False,
            "remote_apis_used": False,
        },
        "warnings": warnings,
        "outputs": {
            "output_dir": _rel(output_dir, root),
            "results_by_method_csv": _rel(output_dir / "results_by_method.csv", root),
            "metrics_json": _rel(output_dir / "metrics.json", root),
            "summary_md": _rel(output_dir / "summary.md", root),
            "case_comparison_csv": _rel(output_dir / "case_comparison.csv", root),
            "failure_sample_csv": _rel(output_dir / "failure_sample.csv", root),
            "report_md": _rel(report_path, root),
        },
        "comparability_note": (
            "Historical Phase 6B/6C used prior devset/evalset artifacts. This class 87 run is not a paired comparison "
            "and must not be used to redesign variants after seeing evalset results."
        ),
    }

    base_fields = [
        "method",
        "case_id",
        "query",
        "nandina_ref",
        "partida_ref",
        "sub_partida_ref",
        "clase_ref",
        "rank_ref",
        "retrieved_count",
        "top_codes",
    ]
    hit_fields = [f"hit_top_{k}" for k in K_LIST] + [f"hit_recall_{k}" for k in RECALL_K_LIST]
    family_fields: list[str] = []
    for k in FAMILY_K_LIST:
        family_fields.extend([f"partida_at_{k}", f"sub_partida_at_{k}", f"clase_at_{k}"])
    candidate_fields: list[str] = []
    for rank in range(1, RESULT_CANDIDATES + 1):
        candidate_fields.extend([f"candidate_{rank}_code", f"candidate_{rank}_score", f"candidate_{rank}_text"])

    comparison_fields = [
        "case_id",
        "query",
        "nandina_ref",
        "partida_ref",
        "sub_partida_ref",
        "clase_ref",
    ]
    for method in METHOD_ORDER:
        comparison_fields.extend(
            [
                f"{method}_rank",
                f"{method}_partida_at_100",
                f"{method}_sub_partida_at_100",
                f"{method}_clase_at_100",
                f"{method}_top10_codes",
            ]
        )
    failure_rows = [
        row
        for row in case_rows
        if any(int(row[f"{method}_rank"]) <= 0 or int(row[f"{method}_rank"]) > 10 for method in METHOD_ORDER)
    ][: args.failure_sample_size]

    _write_csv(output_dir / "results_by_method.csv", results_by_method, base_fields + hit_fields + family_fields + candidate_fields)
    _write_csv(output_dir / "case_comparison.csv", case_rows, comparison_fields)
    _write_csv(output_dir / "failure_sample.csv", failure_rows, comparison_fields)
    _write_json(output_dir / "metrics.json", metrics)
    summary = _summary_markdown(metrics)
    ensure_parent(output_dir / "summary.md")
    (output_dir / "summary.md").write_text(summary, encoding="utf-8")
    ensure_parent(report_path)
    report_path.write_text(summary, encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate frozen normative BM25 hierarchy/dual variants on data_aduanas Clase 87.")
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--flat-index", type=Path, default=DEFAULT_FLAT_INDEX)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--ablation-index-dir", type=Path, default=DEFAULT_ABLATION_INDEX_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--query-column", default=QUERY_COLUMN)
    parser.add_argument("--label-column", default=LABEL_COLUMN)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    parser.add_argument("--failure-sample-size", type=int, default=FAILURE_SAMPLE_SIZE)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion BM25 jerarquico/dual data_aduanas clase 87 completada")
    for method in metrics["method_order"]:
        item = metrics["metrics_by_method"][method]
        print(
            f"{method}: top1={item['top_1']:.4f} top10={item['top_10']:.4f} "
            f"mrr={item['mrr']:.4f} r50={item['recall_at_50']:.4f} r100={item['recall_at_100']:.4f} "
            f"partida100={item['partida_at_100']:.4f} subpartida100={item['sub_partida_at_100']:.4f} "
            f"clase100={item['clase_at_100']:.4f}"
        )
    print(f"Outputs: {metrics['outputs']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
