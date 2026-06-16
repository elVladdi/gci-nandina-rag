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

DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_FLAT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_ABLATION_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_dual_backfill_evalset_v0.1")

EXPECTED_EVALSET_ROWS = 600
PRECISION_VARIANT = "C_hs6_leaf"
RECALL_VARIANT = "D_4d_hs6_leaf"
DUAL_METHOD = "BM25_dual_protected_top_5_backfill"
METHOD_ORDER = [
    "BM25_flat_current",
    PRECISION_VARIANT,
    "BM25_hierarchical_v0.1",
    DUAL_METHOD,
]
BASELINE_ORDER = [
    "BM25_flat_current",
    PRECISION_VARIANT,
    "BM25_hierarchical_v0.1",
]
K_LIST = [1, 3, 5, 10]
CRITICAL_CODES_FROM_DEVSET = ["39012000", "85414100", "28151100", "02013000", "95030010"]


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


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _rank_metric(rank: int, depth: int) -> int:
    return rank if rank > 0 else depth + 1


def _top10_hit(rank: int) -> bool:
    return 0 < rank <= 10


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _dedupe_append(target: list[dict[str, Any]], seen: set[str], hits: Sequence[Mapping[str, Any]], limit: int | None = None) -> None:
    for hit in hits if limit is None else hits[:limit]:
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


def _same_prefix_in_top(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int = 10) -> int:
    prefix = true_code[:prefix_len]
    return int(any(_clean(hit.get("code")).startswith(prefix) for hit in hits[:k]))


def _top_codes(hits: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_clean(hit.get("code")) for hit in hits[:limit])


def _method_metrics(rows: Sequence[Mapping[str, Any]], method: str) -> dict[str, Any]:
    ranks = [int(row[f"{method}_rank"]) for row in rows]
    retrieved = [int(row[f"{method}_retrieved_count"]) for row in rows]
    metrics: dict[str, Any] = {
        "cases_total": len(rows),
        "cases_with_results": sum(1 for count in retrieved if count > 0),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "recall_at_50": _mean([acc_at_k(rank, 50) for rank in ranks]),
        "recall_at_100": _mean([acc_at_k(rank, 100) for rank in ranks]),
        "top_10_hs4": _mean([float(row[f"{method}_top10_hs4"]) for row in rows]),
        "top_10_hs2": _mean([float(row[f"{method}_top10_hs2"]) for row in rows]),
        "not_found": sum(1 for rank in ranks if rank <= 0),
        "sin_match_top_10": sum(1 for rank in ranks if not _top10_hit(rank)),
    }
    for k in K_LIST:
        metrics[f"top_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
    return metrics


def _comparison_rows(rows: Sequence[Mapping[str, Any]], baseline: str, depth: int) -> list[dict[str, Any]]:
    comparison: list[dict[str, Any]] = []
    for row in rows:
        dual_rank = int(row[f"{DUAL_METHOD}_rank"])
        baseline_rank = int(row[f"{baseline}_rank"])
        dual_value = _rank_metric(dual_rank, depth)
        baseline_value = _rank_metric(baseline_rank, depth)
        if dual_value < baseline_value:
            outcome = "ganado"
            gain = baseline_value - dual_value
            loss = 0
        elif dual_value > baseline_value:
            outcome = "perdido"
            gain = 0
            loss = dual_value - baseline_value
        else:
            outcome = "sin_cambio"
            gain = 0
            loss = 0
        dual_top10 = _top10_hit(dual_rank)
        baseline_top10 = _top10_hit(baseline_rank)
        comparison.append(
            {
                "case_id": row["case_id"],
                "descripcion": row["descripcion"],
                "nandina_ref": row["nandina_ref"],
                "hs2_ref": row["hs2_ref"],
                "hs4_ref": row["hs4_ref"],
                "regimen": row["regimen"],
                "baseline_method": baseline,
                "baseline_rank": baseline_rank,
                "dual_rank": dual_rank,
                "outcome": outcome,
                "rank_gain_if_improved": gain,
                "rank_loss_if_worse": loss,
                "both_fail_top_10": int(not dual_top10 and not baseline_top10),
                "dual_rescues_top_10_baseline_not": int(dual_top10 and not baseline_top10),
                "baseline_hits_top_10_dual_not": int(baseline_top10 and not dual_top10),
                "baseline_top10_codes": row[f"{baseline}_top10_codes"],
                "dual_top10_codes": row[f"{DUAL_METHOD}_top10_codes"],
            }
        )
    return comparison


def _comparison_summary(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    gains = [float(row["rank_gain_if_improved"]) for row in rows if row["outcome"] == "ganado"]
    losses = [float(row["rank_loss_if_worse"]) for row in rows if row["outcome"] == "perdido"]
    return {
        "ganados": sum(1 for row in rows if row["outcome"] == "ganado"),
        "perdidos": sum(1 for row in rows if row["outcome"] == "perdido"),
        "sin_cambio": sum(1 for row in rows if row["outcome"] == "sin_cambio"),
        "ganancia_media_rank_cuando_mejora": _mean(gains),
        "perdida_media_rank_cuando_empeora": _mean(losses),
        "casos_ambos_fallan_top_10": sum(int(row["both_fail_top_10"]) for row in rows),
        "casos_dual_rescata_top_10_y_baseline_no": sum(int(row["dual_rescues_top_10_baseline_not"]) for row in rows),
        "casos_baseline_acierta_top_10_y_dual_no": sum(int(row["baseline_hits_top_10_dual_not"]) for row in rows),
    }


def _family_analysis(rows: Sequence[Mapping[str, Any]], group_field: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[Mapping[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(_clean(row.get(group_field)) or "NA", []).append(row)

    analysis: list[dict[str, Any]] = []
    for group_value, group_rows in sorted(grouped.items()):
        if len(group_rows) < 5:
            continue
        flat_top10 = _mean([acc_at_k(int(row["BM25_flat_current_rank"]), 10) for row in group_rows])
        dual_top10 = _mean([acc_at_k(int(row[f"{DUAL_METHOD}_rank"]), 10) for row in group_rows])
        flat_mrr = _mean([mrr_from_rank(int(row["BM25_flat_current_rank"])) for row in group_rows])
        dual_mrr = _mean([mrr_from_rank(int(row[f"{DUAL_METHOD}_rank"])) for row in group_rows])
        analysis.append(
            {
                group_field: group_value,
                "cases_total": len(group_rows),
                "BM25_flat_current_top_10": flat_top10,
                f"{DUAL_METHOD}_top_10": dual_top10,
                "top_10_diff_dual_minus_flat": dual_top10 - flat_top10,
                "BM25_flat_current_mrr": flat_mrr,
                f"{DUAL_METHOD}_mrr": dual_mrr,
                "mrr_diff_dual_minus_flat": dual_mrr - flat_mrr,
            }
        )
    return analysis


def _summary_markdown(metrics: Mapping[str, Any]) -> str:
    lines = [
        "# Evaluacion BM25 dual backfill evalset v0.1",
        "",
        "## Alcance",
        "",
        "`protected_top_5_backfill` fue seleccionado previamente usando solo el devset de 13 casos. Esta corrida usa el evalset final v0.1 una sola vez como validacion controlada; no ejecuta LLM, Text2Trade ni ajuste posterior de reglas.",
        "",
        "## Arquitectura congelada",
        "",
        "- Indice de precision: `C_hs6_leaf`.",
        "- Indice de recall: `D_4d_hs6_leaf`.",
        "- Fusion: proteger Top-5 de precision y completar con candidatos nuevos del indice jerarquico.",
        "",
        "## Metricas globales",
        "",
        "| Metodo | Casos | Con resultados | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4@10 | HS2@10 | not_found | sin match Top-10 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in METHOD_ORDER:
        m = metrics["metrics_by_method"][method]
        lines.append(
            f"| {method} | {m['cases_total']} | {m['cases_with_results']} | {m['top_1']:.4f} | {m['top_3']:.4f} | {m['top_5']:.4f} | {m['top_10']:.4f} | {m['mrr']:.4f} | {m['recall_at_50']:.4f} | {m['recall_at_100']:.4f} | {m['top_10_hs4']:.4f} | {m['top_10_hs2']:.4f} | {m['not_found']} | {m['sin_match_top_10']} |"
        )

    lines.extend(
        [
            "",
            "## Comparacion contra baselines",
            "",
            "| Baseline | Ganados | Perdidos | Sin cambio | Ganancia media rank | Perdida media rank | Ambos fallan Top-10 | Dual rescata Top-10 | Baseline acierta Top-10 y dual no |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for baseline in BASELINE_ORDER:
        c = metrics["comparisons_vs_dual"][baseline]
        lines.append(
            f"| {baseline} | {c['ganados']} | {c['perdidos']} | {c['sin_cambio']} | {c['ganancia_media_rank_cuando_mejora']:.2f} | {c['perdida_media_rank_cuando_empeora']:.2f} | {c['casos_ambos_fallan_top_10']} | {c['casos_dual_rescata_top_10_y_baseline_no']} | {c['casos_baseline_acierta_top_10_y_dual_no']} |"
        )

    lines.extend(
        [
            "",
            "## Analisis por familias",
            "",
            "Los CSV por HS2, HS4 y regimen incluyen grupos con al menos 5 casos. El resumen agregado muestra la diferencia del dual protegido contra BM25 plano en Top-10 y MRR.",
            "",
            "## Casos criticos",
            "",
            f"Codigos criticos del devset encontrados en evalset: {metrics['critical_codes_from_devset']['matched_cases_total']}.",
            "",
            "## Decision metodologica",
            "",
            metrics["methodological_decision"],
            "",
            "## Limitaciones",
            "",
            "- El evalset esta concentrado casi totalmente en regimen 10.",
            "- La evaluacion aun no incorpora LLM de re-ranking ni justificacion.",
            "- BM25 dual solo evalua el ranking inicial documental.",
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
    depth = args.retrieval_depth

    eval_rows = _read_csv(evalset_path)
    if len(eval_rows) != EXPECTED_EVALSET_ROWS:
        raise ValueError(f"Evalset row count is {len(eval_rows)}, expected {EXPECTED_EVALSET_ROWS}.")

    start = time.time()
    flat_index = load_bm25_index(flat_index_path)
    hierarchical_index = load_bm25_index(hierarchical_index_path)
    precision_index = load_bm25_index(precision_index_path)
    recall_index = load_bm25_index(recall_index_path)

    rows: list[dict[str, Any]] = []
    for position, eval_row in enumerate(eval_rows, start=1):
        descripcion = _clean(eval_row.get("descripcion"))
        true_code = _clean(eval_row.get("nandina_ref") or eval_row.get("nandina"))
        flat_hits = retrieve(flat_index, descripcion, top_n=depth)
        precision_hits = retrieve(precision_index, descripcion, top_n=depth)
        hierarchical_hits = retrieve(hierarchical_index, descripcion, top_n=depth)
        recall_hits = retrieve(recall_index, descripcion, top_n=depth)
        dual_hits = _protected_top_5_backfill(precision_hits, recall_hits, depth=depth)
        method_hits = {
            "BM25_flat_current": flat_hits,
            PRECISION_VARIANT: precision_hits,
            "BM25_hierarchical_v0.1": hierarchical_hits,
            DUAL_METHOD: dual_hits,
        }
        row: dict[str, Any] = {
            "case_id": _clean(eval_row.get("case_id")) or f"eval-{position:04d}",
            "descripcion": descripcion,
            "nandina_ref": true_code,
            "hs2_ref": _clean(eval_row.get("capitulo")) or true_code[:2],
            "hs4_ref": _clean(eval_row.get("partida")) or true_code[:4],
            "regimen": _clean(eval_row.get("regimen")),
        }
        for method, hits in method_hits.items():
            rank = rank_of_true(hits, true_code)
            row[f"{method}_rank"] = rank
            row[f"{method}_retrieved_count"] = len(hits)
            row[f"{method}_top10_hs4"] = _same_prefix_in_top(hits, true_code, 4)
            row[f"{method}_top10_hs2"] = _same_prefix_in_top(hits, true_code, 2)
            row[f"{method}_top10_codes"] = _top_codes(hits)
        rows.append(row)

    metrics_by_method = {method: _method_metrics(rows, method) for method in METHOD_ORDER}

    comparison_outputs: dict[str, list[dict[str, Any]]] = {
        baseline: _comparison_rows(rows, baseline, depth) for baseline in BASELINE_ORDER
    }
    comparisons_vs_dual = {baseline: _comparison_summary(items) for baseline, items in comparison_outputs.items()}

    family_hs2 = _family_analysis(rows, "hs2_ref")
    family_hs4 = _family_analysis(rows, "hs4_ref")
    family_regimen = _family_analysis(rows, "regimen")

    vs_flat = comparison_outputs["BM25_flat_current"]
    top_rescues = sorted(
        [row for row in vs_flat if row["outcome"] == "ganado"],
        key=lambda item: (-int(item["rank_gain_if_improved"]), int(item["dual_rank"]) if int(item["dual_rank"]) > 0 else depth + 1),
    )
    top_deteriorations = sorted(
        [row for row in vs_flat if row["outcome"] == "perdido"],
        key=lambda item: (-int(item["rank_loss_if_worse"]), int(item["baseline_rank"]) if int(item["baseline_rank"]) > 0 else depth + 1),
    )
    all_methods_fail = [
        row for row in rows if all(not _top10_hit(int(row[f"{method}_rank"])) for method in METHOD_ORDER)
    ]
    dual_failures = [
        row for row in rows if not _top10_hit(int(row[f"{DUAL_METHOD}_rank"]))
    ]
    failure_sample = sorted(dual_failures, key=lambda item: (item["hs2_ref"], item["hs4_ref"], item["case_id"]))[:50]
    critical_rows = [
        row for row in rows if row["nandina_ref"] in set(CRITICAL_CODES_FROM_DEVSET)
    ]

    dual = metrics_by_method[DUAL_METHOD]
    flat = metrics_by_method["BM25_flat_current"]
    precision = metrics_by_method[PRECISION_VARIANT]
    hierarchical = metrics_by_method["BM25_hierarchical_v0.1"]
    if (
        dual["top_10"] >= flat["top_10"]
        and dual["mrr"] >= flat["mrr"]
        and dual["top_10"] >= precision["top_10"]
        and dual["top_10"] >= hierarchical["top_10"]
        and dual["mrr"] >= hierarchical["mrr"]
    ):
        methodological_decision = (
            "`BM25_dual_protected_top_5_backfill` se acepta como ranking inicial principal del pipeline, "
            "congelado como recuperador documental inicial. La decision no incorpora ajustes post-evalset."
        )
    elif dual["recall_at_100"] > flat["recall_at_100"] and dual["mrr"] >= hierarchical["mrr"]:
        methodological_decision = (
            "`BM25_dual_protected_top_5_backfill` queda como candidato condicionado: mejora cobertura profunda, "
            "pero debe volver a fase exploratoria antes de promoverse como ranking inicial principal."
        )
    else:
        methodological_decision = (
            "`BM25_dual_protected_top_5_backfill` debe volver a fase exploratoria; el evalset no sostiene su adopcion "
            "como ranking inicial principal sin nuevas pruebas en devset."
        )

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_dual_backfill_evalset",
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
        "architecture": {
            "precision_index": PRECISION_VARIANT,
            "recall_index": RECALL_VARIANT,
            "fusion": "protected_top_5_backfill",
            "rule": "Protect precision Top-5, then append new hierarchical recall candidates, then remaining precision candidates.",
            "selected_on": "devset_validacion_intermedia.csv",
            "evalset_usage": "single controlled validation run",
        },
        "bm25_config": {
            "retrieval_depth": depth,
            "protected_top_n": 5,
        },
        "method_order": METHOD_ORDER,
        "metrics_by_method": metrics_by_method,
        "comparisons_vs_dual": comparisons_vs_dual,
        "family_analysis": {
            "hs2_groups": len(family_hs2),
            "hs4_groups": len(family_hs4),
            "regimen_groups": len(family_regimen),
        },
        "critical_codes_from_devset": {
            "codes_checked": CRITICAL_CODES_FROM_DEVSET,
            "matched_cases_total": len(critical_rows),
            "matched_codes": sorted({row["nandina_ref"] for row in critical_rows}),
        },
        "samples": {
            "top_rescues_vs_flat_total": len(top_rescues),
            "top_deteriorations_vs_flat_total": len(top_deteriorations),
            "all_methods_fail_top_10_total": len(all_methods_fail),
            "dual_failure_sample_size": len(failure_sample),
        },
        "methodological_decision": methodological_decision,
        "controls": {
            "llm_executed": False,
            "text2trade_executed": False,
            "rules_adjusted_after_evalset": False,
            "evalset_modified": False,
            "devset_modified": False,
            "source_excel_modified": False,
        },
        "outputs": {
            "output_dir": _rel(output_dir, root),
            "results_csv": _rel(output_dir / "dual_evalset_results.csv", root),
            "metrics_json": _rel(output_dir / "dual_evalset_metrics.json", root),
            "summary_md": _rel(output_dir / "dual_evalset_summary.md", root),
        },
    }

    result_fields = ["case_id", "descripcion", "nandina_ref", "hs2_ref", "hs4_ref", "regimen"]
    for method in METHOD_ORDER:
        result_fields.extend(
            [
                f"{method}_rank",
                f"{method}_retrieved_count",
                f"{method}_top10_hs4",
                f"{method}_top10_hs2",
                f"{method}_top10_codes",
            ]
        )
    _write_csv(output_dir / "dual_evalset_results.csv", rows, result_fields)
    _write_json(output_dir / "dual_evalset_metrics.json", metrics)
    (output_dir / "dual_evalset_summary.md").parent.mkdir(parents=True, exist_ok=True)
    (output_dir / "dual_evalset_summary.md").write_text(_summary_markdown(metrics), encoding="utf-8")

    comparison_fields = [
        "case_id",
        "descripcion",
        "nandina_ref",
        "hs2_ref",
        "hs4_ref",
        "regimen",
        "baseline_method",
        "baseline_rank",
        "dual_rank",
        "outcome",
        "rank_gain_if_improved",
        "rank_loss_if_worse",
        "both_fail_top_10",
        "dual_rescues_top_10_baseline_not",
        "baseline_hits_top_10_dual_not",
        "baseline_top10_codes",
        "dual_top10_codes",
    ]
    _write_csv(output_dir / "dual_evalset_comparison_vs_flat.csv", comparison_outputs["BM25_flat_current"], comparison_fields)
    _write_csv(output_dir / "dual_evalset_comparison_vs_c_hs6.csv", comparison_outputs[PRECISION_VARIANT], comparison_fields)
    _write_csv(output_dir / "dual_evalset_comparison_vs_hierarchical.csv", comparison_outputs["BM25_hierarchical_v0.1"], comparison_fields)

    family_fields = [
        "cases_total",
        "BM25_flat_current_top_10",
        f"{DUAL_METHOD}_top_10",
        "top_10_diff_dual_minus_flat",
        "BM25_flat_current_mrr",
        f"{DUAL_METHOD}_mrr",
        "mrr_diff_dual_minus_flat",
    ]
    _write_csv(output_dir / "dual_evalset_family_analysis_hs2.csv", family_hs2, ["hs2_ref", *family_fields])
    _write_csv(output_dir / "dual_evalset_family_analysis_hs4.csv", family_hs4, ["hs4_ref", *family_fields])
    _write_csv(output_dir / "dual_evalset_family_analysis_regimen.csv", family_regimen, ["regimen", *family_fields])
    _write_csv(output_dir / "dual_evalset_top_rescues.csv", top_rescues[:100], comparison_fields)
    _write_csv(output_dir / "dual_evalset_top_deteriorations.csv", top_deteriorations[:100], comparison_fields)
    _write_csv(output_dir / "dual_evalset_all_methods_fail.csv", all_methods_fail, result_fields)
    _write_csv(output_dir / "dual_evalset_failure_sample.csv", failure_sample, result_fields)
    _write_csv(output_dir / "dual_evalset_devset_critical_codes.csv", critical_rows, result_fields)
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate frozen BM25 dual protected Top-5 backfill on evalset v0.1.")
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--flat-index", type=Path, default=DEFAULT_FLAT_INDEX)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--ablation-index-dir", type=Path, default=DEFAULT_ABLATION_INDEX_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion BM25 dual protected_top_5_backfill evalset completada")
    for method in metrics["method_order"]:
        item = metrics["metrics_by_method"][method]
        print(
            f"{method}: top1={item['top_1']:.4f} top10={item['top_10']:.4f} "
            f"mrr={item['mrr']:.4f} r100={item['recall_at_100']:.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
