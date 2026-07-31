from __future__ import annotations

import argparse
import csv
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_FIELDED_INDEX = Path("data/processed/indexes/bm25_nandina8_fielded_v0.1.pkl")
DEFAULT_EXPANDED_INDEX = Path("data/processed/indexes/bm25_nandina8_fielded_expanded_v0.1.pkl")
DEFAULT_ABLATION_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_FIELDED_CORPUS_METADATA = Path("data/processed/corpus_nandina_fielded_v0.1_metadata.json")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_fielded_devset_v0.1")
DEFAULT_REPORT = Path("docs/evaluacion_bm25_fielded_devset_v0.1.md")

EXPECTED_DEVSET_ROWS = 13
K_LIST = [1, 3, 5, 10]
METHODS = (
    "BM25_hierarchical_Q0",
    "BM25_fielded_weighted_v0.1",
    "BM25_fielded_weighted_expanded_v0.1",
    "phase7a_pool_hierarchical_80_dual_backfill_20",
)
CRITICAL_CODES = {"28151100", "84713000", "84717000", "39012000", "85414100", "83022000", "63064000", "95030010"}
PRECISION_VARIANT = "C_hs6_leaf"
RECALL_VARIANT = "D_4d_hs6_leaf"
DUAL_PROTECTED_TOP_N = 5
PHASE7A_BASE = 80


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return payload


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


def _rank_metric(rank: int, depth: int) -> int:
    return rank if rank > 0 else depth + 1


def _case_outcome(q0_rank: int, method_rank: int, depth: int) -> str:
    q0_metric = _rank_metric(q0_rank, depth)
    method_metric = _rank_metric(method_rank, depth)
    if method_metric < q0_metric:
        return "ganado"
    if method_metric > q0_metric:
        return "perdido"
    return "sin_cambio"


def _code_from_hit(hit: Mapping[str, Any]) -> str:
    return _clean(hit.get("code"))


def _renumber(hits: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    ranked: list[dict[str, Any]] = []
    for rank, hit in enumerate(hits[:depth], start=1):
        item = dict(hit)
        item["rank"] = rank
        ranked.append(item)
    return ranked


def _dedupe_append(
    target: list[dict[str, Any]],
    seen: set[str],
    hits: Sequence[Mapping[str, Any]],
    limit: int | None = None,
) -> None:
    iterable = hits if limit is None else hits[:limit]
    for hit in iterable:
        code = _code_from_hit(hit)
        if code and code not in seen:
            seen.add(code)
            target.append(dict(hit))


def _protected_top_5_backfill(
    precision_hits: Sequence[Mapping[str, Any]],
    recall_hits: Sequence[Mapping[str, Any]],
    depth: int,
) -> list[dict[str, Any]]:
    fused: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(fused, seen, precision_hits, limit=DUAL_PROTECTED_TOP_N)
    _dedupe_append(fused, seen, recall_hits)
    _dedupe_append(fused, seen, precision_hits[DUAL_PROTECTED_TOP_N:])
    return _renumber(fused, depth)


def _phase7a_pool(
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    depth: int,
) -> list[dict[str, Any]]:
    pool: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(pool, seen, hierarchical_hits, limit=min(PHASE7A_BASE, depth))
    _dedupe_append(pool, seen, dual_hits, limit=depth)
    if len(pool) < depth:
        _dedupe_append(pool, seen, hierarchical_hits[PHASE7A_BASE:])
    return _renumber(pool, depth)


def _family_hit(candidates: Sequence[Mapping[str, Any]], true_code: str, family_len: int, k: int) -> int:
    prefix = _clean(true_code)[:family_len]
    if not prefix:
        return 0
    return int(any(_code_from_hit(hit).startswith(prefix) for hit in candidates[:k]))


def _top_codes(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_code_from_hit(hit) for hit in candidates[:limit])


def _compact_top(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for hit in candidates[:limit]:
        rows.append(
            {
                "rank": int(hit.get("rank", len(rows) + 1)),
                "code": _code_from_hit(hit),
                "score": float(hit.get("score", 0.0)),
                "text": _clean(hit.get("text")),
            }
        )
    return rows


def _metrics_for_method(
    rows: Sequence[Mapping[str, Any]],
    method: str,
    *,
    depth: int,
) -> dict[str, Any]:
    ranks = [int(row[f"rank_{method}"]) for row in rows]
    metrics: dict[str, Any] = {
        "cases_total": len(rows),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "recall_at_50": _mean([acc_at_k(rank, 50) for rank in ranks]),
        "recall_at_100": _mean([acc_at_k(rank, 100) for rank in ranks]),
        "top_10_hs4": _mean([int(row[f"{method}_top10_hs4"]) for row in rows]),
        "top_10_hs2": _mean([int(row[f"{method}_top10_hs2"]) for row in rows]),
        "not_found_at_depth": sum(1 for rank in ranks if rank <= 0),
        "depth": depth,
    }
    for k in K_LIST:
        metrics[f"top_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
    return metrics


def _comparison_vs_q0(rows: Sequence[Mapping[str, Any]], method: str, depth: int) -> dict[str, int]:
    return {
        "ganados": sum(
            1
            for row in rows
            if _case_outcome(int(row["rank_BM25_hierarchical_Q0"]), int(row[f"rank_{method}"]), depth) == "ganado"
        ),
        "perdidos": sum(
            1
            for row in rows
            if _case_outcome(int(row["rank_BM25_hierarchical_Q0"]), int(row[f"rank_{method}"]), depth) == "perdido"
        ),
        "sin_cambio": sum(
            1
            for row in rows
            if _case_outcome(int(row["rank_BM25_hierarchical_Q0"]), int(row[f"rank_{method}"]), depth)
            == "sin_cambio"
        ),
        "new_cases_q0_not_found_method_found": sum(
            1
            for row in rows
            if int(row["rank_BM25_hierarchical_Q0"]) <= 0 and int(row[f"rank_{method}"]) > 0
        ),
        "degraded_cases": sum(
            1
            for row in rows
            if _rank_metric(int(row[f"rank_{method}"]), depth) > _rank_metric(int(row["rank_BM25_hierarchical_Q0"]), depth)
        ),
    }


def _short(text: object, limit: int = 95) -> str:
    value = _clean(text).replace("|", "/")
    return value if len(value) <= limit else value[: limit - 3].rstrip() + "..."


def _row(cells: Sequence[Any]) -> str:
    return "| " + " | ".join(_short(cell, 120) for cell in cells) + " |"


def _expansion_table(corpus_summary: Mapping[str, Any]) -> list[str]:
    lines = ["| ID | Codigos objetivo | Terminos |", "|---|---|---|"]
    for entry in corpus_summary.get("expansions", {}).get("entries", []):
        lines.append(
            _row(
                [
                    entry.get("id", ""),
                    ", ".join(str(code) for code in entry.get("target_codes", [])),
                    ", ".join(str(term) for term in entry.get("terms", [])),
                ]
            )
        )
    return lines


def _summary_markdown(
    metrics: Mapping[str, Any],
    case_rows: Sequence[Mapping[str, Any]],
    critical_rows: Sequence[Mapping[str, Any]],
    corpus_summary: Mapping[str, Any],
) -> str:
    methods = metrics["methods"]
    comparison = metrics["comparison_vs_q0"]
    decision = metrics["decision"]
    lines = [
        "# Evaluacion BM25 fielded devset v0.1",
        "",
        "## Objetivo",
        "",
        "Evaluar una variante BM25 por campos para NANDINA8 con ponderacion explicita de descripcion 8D, HS6, 4D y expansion lexica controlada del corpus. La evaluacion usa solo el devset de 13 casos.",
        "",
        "## Razon metodologica",
        "",
        "La Fase 7A-2 con extraccion LLM pre-retrieval no mejoro Recall@50 ni Recall@100 frente a Q0 BM25 jerarquico. Por eso esta fase vuelve al problema base: calidad del corpus y recuperacion documental, sin LLM en tiempo de consulta.",
        "",
        "## Construccion del corpus por campos",
        "",
        "Se parte de `data/processed/corpus_nandina_hierarchical_v0.1.jsonl` y se generan dos JSONL regenerables: fielded y fielded-expanded. Los codigos NANDINA se conservan como identificadores/metadata, no como terminos en `texto_index_fielded`.",
        "",
        "## Ponderacion",
        "",
        "| Campo | Peso |",
        "|---|---:|",
    ]
    for field, weight in corpus_summary.get("field_weights", {}).items():
        lines.append(f"| {field} | {weight} |")
    lines.extend(
        [
            "",
            "La ponderacion se simula repitiendo campos en el texto indexable porque el BM25 actual no implementa campos reales.",
            "",
            "## Expansiones controladas usadas",
            "",
        ]
    )
    lines.extend(_expansion_table(corpus_summary))
    lines.extend(
        [
            "",
            "## Metricas comparativas",
            "",
            "| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4@10 | HS2@10 |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for method in METHODS:
        data = methods[method]
        lines.append(
            f"| {method} | {data['top_1']:.4f} | {data['top_3']:.4f} | {data['top_5']:.4f} | "
            f"{data['top_10']:.4f} | {data['mrr']:.4f} | {data['recall_at_50']:.4f} | "
            f"{data['recall_at_100']:.4f} | {data['top_10_hs4']:.4f} | {data['top_10_hs2']:.4f} |"
        )
    lines.extend(["", "## Comparacion contra BM25_hierarchical_Q0", "", "| Metodo | Ganados | Perdidos | Sin cambio | Nuevos Q0 no recuperaba | Degradados |", "|---|---:|---:|---:|---:|---:|"])
    for method, data in comparison.items():
        lines.append(
            f"| {method} | {data['ganados']} | {data['perdidos']} | {data['sin_cambio']} | "
            f"{data['new_cases_q0_not_found_method_found']} | {data['degraded_cases']} |"
        )
    lines.extend(["", "## Tabla de 13 casos", "", "| Caso | Descripcion | NANDINA | Rank Q0 | Rank fielded | Rank expanded | Resultado expanded |", "|---|---|---|---:|---:|---:|---|"])
    for item in case_rows:
        lines.append(
            _row(
                [
                    item["case_id"],
                    item["descripcion"],
                    item["nandina_ref"],
                    item["rank_BM25_hierarchical_Q0"],
                    item["rank_BM25_fielded_weighted_v0.1"],
                    item["rank_BM25_fielded_weighted_expanded_v0.1"],
                    item["outcome_BM25_fielded_weighted_expanded_v0.1"],
                ]
            )
        )
    lines.extend(["", "## Casos criticos", "", "| Caso | NANDINA | Rank Q0 | Rank fielded | Rank expanded | Top10 expanded |", "|---|---|---:|---:|---:|---|"])
    for item in critical_rows:
        lines.append(
            _row(
                [
                    item["case_id"],
                    item["nandina_ref"],
                    item["rank_BM25_hierarchical_Q0"],
                    item["rank_BM25_fielded_weighted_v0.1"],
                    item["rank_BM25_fielded_weighted_expanded_v0.1"],
                    item["top10_codes_BM25_fielded_weighted_expanded_v0.1"],
                ]
            )
        )
    lines.extend(
        [
            "",
            "## Decision metodologica",
            "",
            decision["recommendation"],
            "",
            f"- Delta Recall@50 expanded vs Q0: {decision['expanded_recall50_delta']:+.4f}.",
            f"- Delta Recall@100 expanded vs Q0: {decision['expanded_recall100_delta']:+.4f}.",
            f"- Delta Top-10 expanded vs Q0: {decision['expanded_top10_delta']:+.4f}.",
            f"- Delta MRR expanded vs Q0: {decision['expanded_mrr_delta']:+.4f}.",
            "",
            "## Limitaciones",
            "",
            "- El devset tiene solo 13 casos y sirve como senal exploratoria.",
            "- La expansion es manual y conservadora; puede mejorar casos lexicales concretos sin generalizar.",
            "- El corpus jerarquico fuente tiene ruido en algunos padres 4D/capitulos; el fielded reduce peso 4D, pero no repara la extraccion fuente.",
            "- No se evalua fundamento legal ni clasificacion oficial, solo recuperacion documental.",
            "",
            "## Validaciones declaradas",
            "",
            "- No se ejecuto evalset.",
            "- No se uso LLM.",
            "- No se uso Text2Trade.",
            "- Devset/evalset/Excel fuente no se modifican por estos scripts.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    devset_path = resolve_project_path(args.devset)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    fielded_index_path = resolve_project_path(args.fielded_index)
    expanded_index_path = resolve_project_path(args.expanded_index)
    ablation_index_dir = resolve_project_path(args.ablation_index_dir)
    corpus_metadata_path = resolve_project_path(args.fielded_corpus_metadata)
    output_dir = resolve_project_path(args.output_dir)
    report_path = resolve_project_path(args.report)
    depth = args.retrieval_depth

    dev_rows = _read_csv(devset_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")

    hierarchical_index = load_bm25_index(hierarchical_index_path)
    fielded_index = load_bm25_index(fielded_index_path)
    expanded_index = load_bm25_index(expanded_index_path)
    precision_index = load_bm25_index(ablation_index_dir / f"{PRECISION_VARIANT}.pkl")
    recall_index = load_bm25_index(ablation_index_dir / f"{RECALL_VARIANT}.pkl")
    corpus_summary = _read_json(corpus_metadata_path)

    start = time.time()
    case_rows: list[dict[str, Any]] = []
    retrieval_rows: list[dict[str, Any]] = []

    for position, dev_row in enumerate(dev_rows, start=1):
        descripcion = _clean(dev_row.get("descripcion"))
        true_code = _clean(dev_row.get("nandina") or dev_row.get("nandina_ref"))
        case_id = f"dev-{position:02d}"
        hierarchical_hits = retrieve(hierarchical_index, descripcion, top_n=depth)
        fielded_hits = retrieve(fielded_index, descripcion, top_n=depth)
        expanded_hits = retrieve(expanded_index, descripcion, top_n=depth)
        precision_hits = retrieve(precision_index, descripcion, top_n=depth)
        recall_hits = retrieve(recall_index, descripcion, top_n=depth)
        dual_hits = _protected_top_5_backfill(precision_hits, recall_hits, depth)
        phase7a_hits = _phase7a_pool(hierarchical_hits, dual_hits, depth)
        method_candidates = {
            "BM25_hierarchical_Q0": hierarchical_hits,
            "BM25_fielded_weighted_v0.1": fielded_hits,
            "BM25_fielded_weighted_expanded_v0.1": expanded_hits,
            "phase7a_pool_hierarchical_80_dual_backfill_20": phase7a_hits,
        }
        ranks = {method: rank_of_true(candidates, true_code) for method, candidates in method_candidates.items()}
        row: dict[str, Any] = {
            "case_id": case_id,
            "descripcion": descripcion,
            "nandina_ref": true_code,
            "hs4_ref": true_code[:4],
            "hs2_ref": true_code[:2],
            "is_critical_case": int(true_code in CRITICAL_CODES),
        }
        for method, candidates in method_candidates.items():
            rank = ranks[method]
            row[f"rank_{method}"] = rank
            row[f"{method}_top10_hs4"] = _family_hit(candidates, true_code, 4, 10)
            row[f"{method}_top10_hs2"] = _family_hit(candidates, true_code, 2, 10)
            row[f"top10_codes_{method}"] = _top_codes(candidates)
            row[f"top10_json_{method}"] = json.dumps(_compact_top(candidates), ensure_ascii=False)
            retrieval_rows.append(
                {
                    "case_id": case_id,
                    "method": method,
                    "descripcion": descripcion,
                    "nandina_ref": true_code,
                    "rank": rank,
                    "hit_top_1": int(acc_at_k(rank, 1)),
                    "hit_top_3": int(acc_at_k(rank, 3)),
                    "hit_top_5": int(acc_at_k(rank, 5)),
                    "hit_top_10": int(acc_at_k(rank, 10)),
                    "recall_at_50": int(acc_at_k(rank, 50)),
                    "recall_at_100": int(acc_at_k(rank, 100)),
                    "top10_hs4": _family_hit(candidates, true_code, 4, 10),
                    "top10_hs2": _family_hit(candidates, true_code, 2, 10),
                    "top10_codes": _top_codes(candidates),
                    "top10_json": json.dumps(_compact_top(candidates), ensure_ascii=False),
                }
            )
        for method in METHODS:
            if method != "BM25_hierarchical_Q0":
                row[f"outcome_{method}"] = _case_outcome(ranks["BM25_hierarchical_Q0"], ranks[method], depth)
        case_rows.append(row)

    critical_rows = [row for row in case_rows if int(row["is_critical_case"])]
    methods = {method: _metrics_for_method(case_rows, method, depth=depth) for method in METHODS}
    comparison = {
        method: _comparison_vs_q0(case_rows, method, depth)
        for method in METHODS
        if method != "BM25_hierarchical_Q0"
    }
    q0 = methods["BM25_hierarchical_Q0"]
    expanded = methods["BM25_fielded_weighted_expanded_v0.1"]
    recall50_delta = expanded["recall_at_50"] - q0["recall_at_50"]
    recall100_delta = expanded["recall_at_100"] - q0["recall_at_100"]
    top10_delta = expanded["top_10"] - q0["top_10"]
    mrr_delta = expanded["mrr"] - q0["mrr"]
    should_scale = (recall50_delta > 0 or recall100_delta > 0) and top10_delta >= -0.0001 and mrr_delta >= -0.0001
    recommendation = (
        "Escalar al evalset en una subfase separada con la variante congelada `BM25_fielded_weighted_expanded_v0.1`, porque mejora recall amplio sin degradar materialmente Top-10/MRR."
        if should_scale
        else "No escalar al evalset: `BM25_fielded_weighted_expanded_v0.1` no cumple el criterio de mejorar Recall@50 o Recall@100 sin deteriorar materialmente Top-10/MRR. Mantener como variante exploratoria y priorizar curacion del corpus fuente."
    )

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_fielded_devset",
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
            "devset_path": _rel(devset_path, root),
            "devset_sha256": sha256_file(devset_path),
            "hierarchical_index_path": _rel(hierarchical_index_path, root),
            "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
            "fielded_index_path": _rel(fielded_index_path, root),
            "fielded_index_sha256": sha256_file(fielded_index_path),
            "fielded_expanded_index_path": _rel(expanded_index_path, root),
            "fielded_expanded_index_sha256": sha256_file(expanded_index_path),
            "fielded_corpus_metadata_path": _rel(corpus_metadata_path, root),
            "fielded_corpus_metadata_sha256": sha256_file(corpus_metadata_path),
        },
        "retrieval": {"retrieval_depth": depth, "k_list": K_LIST},
        "methods": methods,
        "comparison_vs_q0": comparison,
        "decision": {
            "should_scale_to_evalset": should_scale,
            "frozen_variant_if_scaled": "BM25_fielded_weighted_expanded_v0.1" if should_scale else "",
            "recommendation": recommendation,
            "expanded_recall50_delta": recall50_delta,
            "expanded_recall100_delta": recall100_delta,
            "expanded_top10_delta": top10_delta,
            "expanded_mrr_delta": mrr_delta,
        },
        "validations": {
            "devset_only": True,
            "evalset_executed": False,
            "llm_used": False,
            "text2trade_used": False,
            "expected_devset_rows": EXPECTED_DEVSET_ROWS,
            "case_comparison_rows": len(case_rows),
            "critical_case_rows": len(critical_rows),
        },
        "outputs": {
            "fielded_corpus_summary_json": _rel(output_dir / "fielded_corpus_summary.json", root),
            "fielded_retrieval_results_csv": _rel(output_dir / "fielded_retrieval_results.csv", root),
            "fielded_retrieval_metrics_json": _rel(output_dir / "fielded_retrieval_metrics.json", root),
            "fielded_case_comparison_13_cases_csv": _rel(output_dir / "fielded_case_comparison_13_cases.csv", root),
            "fielded_critical_cases_csv": _rel(output_dir / "fielded_critical_cases.csv", root),
            "fielded_summary_md": _rel(output_dir / "fielded_summary.md", root),
            "report_md": _rel(report_path, root),
        },
    }

    base_fields = ["case_id", "descripcion", "nandina_ref", "hs4_ref", "hs2_ref", "is_critical_case"]
    case_fields = list(base_fields)
    for method in METHODS:
        case_fields.extend(
            [
                f"rank_{method}",
                f"{method}_top10_hs4",
                f"{method}_top10_hs2",
                f"top10_codes_{method}",
                f"top10_json_{method}",
            ]
        )
    for method in METHODS:
        if method != "BM25_hierarchical_Q0":
            case_fields.append(f"outcome_{method}")
    retrieval_fields = [
        "case_id",
        "method",
        "descripcion",
        "nandina_ref",
        "rank",
        "hit_top_1",
        "hit_top_3",
        "hit_top_5",
        "hit_top_10",
        "recall_at_50",
        "recall_at_100",
        "top10_hs4",
        "top10_hs2",
        "top10_codes",
        "top10_json",
    ]
    corpus_summary_out = {
        "corpus_summary": corpus_summary,
        "evaluation_inputs": metrics["input"],
        "validations": metrics["validations"],
    }
    _write_json(output_dir / "fielded_corpus_summary.json", corpus_summary_out)
    _write_csv(output_dir / "fielded_retrieval_results.csv", retrieval_rows, retrieval_fields)
    _write_csv(output_dir / "fielded_case_comparison_13_cases.csv", case_rows, case_fields)
    _write_csv(output_dir / "fielded_critical_cases.csv", critical_rows, case_fields)
    _write_json(output_dir / "fielded_retrieval_metrics.json", metrics)
    summary = _summary_markdown(metrics, case_rows, critical_rows, corpus_summary)
    ensure_parent(output_dir / "fielded_summary.md")
    (output_dir / "fielded_summary.md").write_text(summary, encoding="utf-8")
    ensure_parent(report_path)
    report_path.write_text(summary, encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate fielded BM25 variants on devset only.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--fielded-index", type=Path, default=DEFAULT_FIELDED_INDEX)
    parser.add_argument("--expanded-index", type=Path, default=DEFAULT_EXPANDED_INDEX)
    parser.add_argument("--ablation-index-dir", type=Path, default=DEFAULT_ABLATION_INDEX_DIR)
    parser.add_argument("--fielded-corpus-metadata", type=Path, default=DEFAULT_FIELDED_CORPUS_METADATA)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion BM25 fielded devset completada")
    print(f"Casos evaluados: {metrics['validations']['case_comparison_rows']}")
    for method in METHODS:
        data = metrics["methods"][method]
        print(
            f"{method}: top10={data['top_10']:.4f} mrr={data['mrr']:.4f} "
            f"recall50={data['recall_at_50']:.4f} recall100={data['recall_at_100']:.4f}"
        )
    print(metrics["decision"]["recommendation"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
