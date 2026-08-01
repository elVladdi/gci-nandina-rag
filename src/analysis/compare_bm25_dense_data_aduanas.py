from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_BM25_METRICS = Path("outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/metrics.json")
DEFAULT_BM25_RESULTS = Path("outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/results.csv")
DEFAULT_DENSE_METRICS = Path("outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/metrics.json")
DEFAULT_DENSE_RESULTS = Path("outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/results.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1")
K_LIST = [1, 3, 5, 10]
RECALL_K_LIST = [50, 100]
FAMILY_K_LIST = [10, 50, 100]
FAMILY_LEVELS = {
    "partida": "Partida HS4",
    "sub_partida": "Sub Partida HS6",
    "clase": "Clase HS2",
}


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _rate(numerator: int, denominator: int) -> float:
    return float(numerator / denominator) if denominator else 0.0


def _as_int(value: object, default: int = 0) -> int:
    try:
        return int(_clean(value))
    except ValueError:
        return default


def _hit(row: Mapping[str, str], column: str) -> bool:
    return _as_int(row.get(column)) == 1


def _case_maps(rows: Sequence[Mapping[str, str]]) -> dict[str, Mapping[str, str]]:
    return {_clean(row.get("case_id")): row for row in rows if _clean(row.get("case_id"))}


def _global_metric(metrics: Mapping[str, Any], key: str) -> float:
    value = metrics.get("global_metrics", {}).get(key, 0.0)
    return float(value or 0.0)


def _hierarchical_metric(metrics: Mapping[str, Any], key: str) -> float:
    value = metrics.get("hierarchical_metrics", {}).get(key, 0.0)
    return float(value or 0.0)


def _metric_pair(bm25_value: float, dense_value: float) -> dict[str, float]:
    return {
        "bm25": bm25_value,
        "dense": dense_value,
        "delta_dense_minus_bm25": dense_value - bm25_value,
    }


def _outcome(bm25_hit: bool, dense_hit: bool) -> str:
    if dense_hit and not bm25_hit:
        return "won_by_dense"
    if bm25_hit and not dense_hit:
        return "lost_by_dense"
    if dense_hit and bm25_hit:
        return "both_retrieve"
    return "both_fail"


def _build_case_comparison(
    bm25_by_id: Mapping[str, Mapping[str, str]],
    dense_by_id: Mapping[str, Mapping[str, str]],
    shared_ids: Sequence[str],
    top_k: int,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for case_id in shared_ids:
        bm25_row = bm25_by_id[case_id]
        dense_row = dense_by_id[case_id]
        bm25_hit = _hit(bm25_row, f"hit_top_{top_k}")
        dense_hit = _hit(dense_row, f"hit_top_{top_k}")
        row: dict[str, Any] = {
            "case_id": case_id,
            "nandina_ref": _clean(dense_row.get("nandina_ref")) or _clean(bm25_row.get("nandina_ref")),
            "query": _clean(dense_row.get("query")) or _clean(bm25_row.get("query")),
            "bm25_rank_ref": _as_int(bm25_row.get("rank_ref")),
            "dense_rank_ref": _as_int(dense_row.get("rank_ref")),
            f"bm25_hit_top_{top_k}": int(bm25_hit),
            f"dense_hit_top_{top_k}": int(dense_hit),
            f"outcome_top_{top_k}": _outcome(bm25_hit, dense_hit),
            "bm25_top_codes": _clean(bm25_row.get("top_codes")),
            "dense_top_codes": _clean(dense_row.get("top_codes")),
        }
        for family in FAMILY_LEVELS:
            for k in FAMILY_K_LIST:
                row[f"bm25_{family}_at_{k}"] = _as_int(bm25_row.get(f"{family}_at_{k}"))
                row[f"dense_{family}_at_{k}"] = _as_int(dense_row.get(f"{family}_at_{k}"))
        rows.append(row)
    return rows


def _summary_markdown(comparison: Mapping[str, Any]) -> str:
    metrics = comparison["metrics"]
    outcome = comparison["case_outcomes_top_10"]
    lines = [
        "# Comparacion BM25 vs Text2Trade dense data_aduanas clase 87 v0.1",
        "",
        "## Alcance",
        "",
        "Comparacion pareada sobre el evalset `data_aduanas` Clase = 87. Dense usa fuerza bruta sobre artefactos Text2Trade locales; BM25 usa el baseline normativo plano de Fase 4 actualizada.",
        "",
        "## Metricas exactas",
        "",
        "| Metrica | BM25 | Dense | Delta dense-BM25 |",
        "| --- | ---: | ---: | ---: |",
    ]
    for key, label in [
        ("top_1_accuracy", "Top-1 NANDINA8"),
        ("top_3_accuracy", "Top-3 NANDINA8"),
        ("top_5_accuracy", "Top-5 NANDINA8"),
        ("top_10_accuracy", "Top-10 NANDINA8"),
        ("mrr", "MRR"),
        ("recall_at_50", "Recall@50"),
        ("recall_at_100", "Recall@100"),
    ]:
        row = metrics["exact"][key]
        lines.append(f"| {label} | {row['bm25']:.4f} | {row['dense']:.4f} | {row['delta_dense_minus_bm25']:+.4f} |")

    lines.extend(
        [
            "",
            "## Metricas jerarquicas",
            "",
            "| Metrica | BM25 | Dense | Delta dense-BM25 |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for family, label in FAMILY_LEVELS.items():
        for k in FAMILY_K_LIST:
            key = f"{family}_at_{k}"
            row = metrics["hierarchical"][key]
            lines.append(f"| {label}@{k} | {row['bm25']:.4f} | {row['dense']:.4f} | {row['delta_dense_minus_bm25']:+.4f} |")

    lines.extend(
        [
            "",
            "## Casos Top-10",
            "",
            f"- Ganados por dense: {outcome['won_by_dense_count']}.",
            f"- Perdidos por dense: {outcome['lost_by_dense_count']}.",
            f"- Ambos recuperan: {outcome['both_retrieve_count']}.",
            f"- Ambos fallan: {outcome['both_fail_count']}.",
            "",
            "## Lectura metodologica",
            "",
            "La comparacion mide recuperacion documental, no clasificacion oficial. La Fase 5 historica de 600 casos se conserva como artefacto previo y no es comparable de forma directa con esta corrida clase 87 porque cambian fuente, alcance y tamano del evalset.",
            "",
        ]
    )
    return "\n".join(lines)


def compare(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    bm25_metrics_path = resolve_project_path(args.bm25_metrics)
    bm25_results_path = resolve_project_path(args.bm25_results)
    dense_metrics_path = resolve_project_path(args.dense_metrics)
    dense_results_path = resolve_project_path(args.dense_results)
    output_dir = resolve_project_path(args.output_dir)

    bm25_metrics = _read_json(bm25_metrics_path)
    dense_metrics = _read_json(dense_metrics_path)
    bm25_rows = _read_csv(bm25_results_path)
    dense_rows = _read_csv(dense_results_path)
    bm25_by_id = _case_maps(bm25_rows)
    dense_by_id = _case_maps(dense_rows)
    shared_ids = sorted(set(bm25_by_id) & set(dense_by_id))
    if not shared_ids:
        raise ValueError("BM25 and dense results have no shared case_id values.")

    case_rows = _build_case_comparison(bm25_by_id, dense_by_id, shared_ids, args.top_k)
    won = [row for row in case_rows if row[f"outcome_top_{args.top_k}"] == "won_by_dense"]
    lost = [row for row in case_rows if row[f"outcome_top_{args.top_k}"] == "lost_by_dense"]
    both_retrieve = [row for row in case_rows if row[f"outcome_top_{args.top_k}"] == "both_retrieve"]
    both_fail = [row for row in case_rows if row[f"outcome_top_{args.top_k}"] == "both_fail"]

    exact_metrics: dict[str, Any] = {}
    for key in ["top_1_accuracy", "top_3_accuracy", "top_5_accuracy", "top_10_accuracy", "mrr", "recall_at_50", "recall_at_100"]:
        exact_metrics[key] = _metric_pair(_global_metric(bm25_metrics, key), _global_metric(dense_metrics, key))

    hierarchical_metrics: dict[str, Any] = {}
    for family in FAMILY_LEVELS:
        for k in FAMILY_K_LIST:
            key = f"{family}_at_{k}"
            hierarchical_metrics[key] = _metric_pair(_hierarchical_metric(bm25_metrics, key), _hierarchical_metric(dense_metrics, key))

    comparison: dict[str, Any] = {
        "script": "src.analysis.compare_bm25_dense_data_aduanas",
        "input": {
            "bm25_metrics": _rel(bm25_metrics_path, root),
            "bm25_results": _rel(bm25_results_path, root),
            "dense_metrics": _rel(dense_metrics_path, root),
            "dense_results": _rel(dense_results_path, root),
        },
        "scope": {
            "source": "data_aduanas",
            "class": "87",
            "top_k_case_outcomes": args.top_k,
        },
        "cases": {
            "bm25_rows": len(bm25_rows),
            "dense_rows": len(dense_rows),
            "shared_cases": len(shared_ids),
            "bm25_only_cases": len(set(bm25_by_id) - set(dense_by_id)),
            "dense_only_cases": len(set(dense_by_id) - set(bm25_by_id)),
        },
        "metrics": {
            "exact": exact_metrics,
            "hierarchical": hierarchical_metrics,
        },
        "case_outcomes_top_10": {
            "won_by_dense_count": len(won),
            "lost_by_dense_count": len(lost),
            "both_retrieve_count": len(both_retrieve),
            "both_fail_count": len(both_fail),
            "won_by_dense_rate": _rate(len(won), len(shared_ids)),
            "lost_by_dense_rate": _rate(len(lost), len(shared_ids)),
            "both_retrieve_rate": _rate(len(both_retrieve), len(shared_ids)),
            "both_fail_rate": _rate(len(both_fail), len(shared_ids)),
            "won_by_dense_case_ids": [row["case_id"] for row in won[:100]],
            "lost_by_dense_case_ids": [row["case_id"] for row in lost[:100]],
        },
        "decision": {
            "dense_adds_over_bm25": exact_metrics["top_10_accuracy"]["delta_dense_minus_bm25"] > 0
            or exact_metrics["recall_at_100"]["delta_dense_minus_bm25"] > 0,
            "methodological_reading": (
                "Dense Text2Trade should only be considered additive if it improves exact Top-10 or Recall@100 "
                "without unacceptable hierarchical loss on this same data_aduanas Clase 87 evalset."
            ),
        },
        "warnings": [
            "Dense run uses brute-force vector search, not HNSW.",
            "Historical Phase 5 over 600 cases is preserved and not directly comparable with this data_aduanas run.",
            "Comparison uses local outputs under outputs/; no LLM, Ollama or remote API is executed by this script.",
        ],
        "output": {
            "comparison_json": _rel(output_dir / "comparison_bm25_dense_data_aduanas.json", root),
            "comparison_md": _rel(output_dir / "comparison_bm25_dense_data_aduanas.md", root),
            "case_comparison_csv": _rel(output_dir / "case_comparison.csv", root),
        },
    }

    _write_json(output_dir / "comparison_bm25_dense_data_aduanas.json", comparison)
    ensure_parent(output_dir / "comparison_bm25_dense_data_aduanas.md")
    (output_dir / "comparison_bm25_dense_data_aduanas.md").write_text(_summary_markdown(comparison), encoding="utf-8")
    case_fields = list(case_rows[0].keys())
    _write_csv(output_dir / "case_comparison.csv", case_rows, case_fields)
    return comparison


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare BM25 against dense Text2Trade on data_aduanas Clase 87.")
    parser.add_argument("--bm25-metrics", type=Path, default=DEFAULT_BM25_METRICS)
    parser.add_argument("--bm25-results", type=Path, default=DEFAULT_BM25_RESULTS)
    parser.add_argument("--dense-metrics", type=Path, default=DEFAULT_DENSE_METRICS)
    parser.add_argument("--dense-results", type=Path, default=DEFAULT_DENSE_RESULTS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--top-k", type=int, default=10)
    return parser


def main() -> int:
    comparison = compare(build_parser().parse_args())
    exact = comparison["metrics"]["exact"]
    outcome = comparison["case_outcomes_top_10"]
    print("OK: comparacion BM25 vs dense data_aduanas clase 87 completada")
    print(f"Top-1 BM25: {exact['top_1_accuracy']['bm25']:.4f}")
    print(f"Top-1 dense: {exact['top_1_accuracy']['dense']:.4f}")
    print(f"Top-10 BM25: {exact['top_10_accuracy']['bm25']:.4f}")
    print(f"Top-10 dense: {exact['top_10_accuracy']['dense']:.4f}")
    print(f"MRR BM25: {exact['mrr']['bm25']:.4f}")
    print(f"MRR dense: {exact['mrr']['dense']:.4f}")
    print(f"Recall@100 BM25: {exact['recall_at_100']['bm25']:.4f}")
    print(f"Recall@100 dense: {exact['recall_at_100']['dense']:.4f}")
    print(f"Ganados por dense Top-10: {outcome['won_by_dense_count']}")
    print(f"Perdidos por dense Top-10: {outcome['lost_by_dense_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
