from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_BM25_METRICS = Path("outputs/evaluation/bm25_eval_v0.1/metrics.json")
DEFAULT_BM25_RESULTS = Path("outputs/evaluation/bm25_eval_v0.1/results.csv")
DEFAULT_DENSE_METRICS = Path("outputs/evaluation/text2trade_dense_eval_v0.1/metrics.json")
DEFAULT_DENSE_RESULTS = Path("outputs/evaluation/text2trade_dense_eval_v0.1/results.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/text2trade_dense_eval_v0.1")


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


def _report_path(path: Path, root: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return str(resolved)


def _rate(numerator: int, denominator: int) -> float:
    return float(numerator / denominator) if denominator else 0.0


def _topk_hit(row: Mapping[str, str], k: int) -> bool:
    try:
        return int(_clean(row.get(f"hit_top_{k}")) or "0") == 1
    except ValueError:
        return False


def _family_hit(row: Mapping[str, str], family_len: int, k: int) -> bool:
    ref = _clean(row.get("nandina_ref"))[:family_len]
    if not ref:
        return False
    for rank in range(1, k + 1):
        if _clean(row.get(f"candidate_{rank}_code"))[:family_len] == ref:
            return True
    return False


def _case_maps(rows: Sequence[Mapping[str, str]]) -> dict[str, Mapping[str, str]]:
    return {_clean(row.get("case_id")): row for row in rows}


def _family_deltas(
    bm25_rows: Sequence[Mapping[str, str]],
    dense_rows: Sequence[Mapping[str, str]],
    k: int,
    group_field: str,
    min_group_size: int,
) -> list[dict[str, Any]]:
    bm25_by_id = _case_maps(bm25_rows)
    grouped: dict[str, list[Mapping[str, str]]] = defaultdict(list)
    for row in dense_rows:
        group_value = _clean(row.get(group_field))
        if group_value:
            grouped[group_value].append(row)

    payload: list[dict[str, Any]] = []
    for group, rows in grouped.items():
        if len(rows) < min_group_size:
            continue
        dense_hits = sum(1 for row in rows if _topk_hit(row, k))
        bm25_hits = sum(1 for row in rows if _topk_hit(bm25_by_id.get(_clean(row.get("case_id")), {}), k))
        payload.append(
            {
                "group": group,
                "cases": len(rows),
                "bm25_top_k": _rate(bm25_hits, len(rows)),
                "dense_top_k": _rate(dense_hits, len(rows)),
                "delta": _rate(dense_hits, len(rows)) - _rate(bm25_hits, len(rows)),
            }
        )
    return sorted(payload, key=lambda item: item["delta"], reverse=True)


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
    k = args.top_k

    won_by_dense: list[str] = []
    lost_by_dense: list[str] = []
    both_fail: list[str] = []
    both_hit: list[str] = []
    hs4_counter: Counter[str] = Counter()
    hs4_fail_counter: Counter[str] = Counter()

    for case_id in shared_ids:
        bm25_row = bm25_by_id[case_id]
        dense_row = dense_by_id[case_id]
        bm25_hit = _topk_hit(bm25_row, k)
        dense_hit = _topk_hit(dense_row, k)
        if dense_hit and not bm25_hit:
            won_by_dense.append(case_id)
            hs4_counter[_clean(dense_row.get("partida_ref"))] += 1
        elif bm25_hit and not dense_hit:
            lost_by_dense.append(case_id)
        elif not bm25_hit and not dense_hit:
            both_fail.append(case_id)
            hs4_fail_counter[_clean(dense_row.get("partida_ref"))] += 1
        else:
            both_hit.append(case_id)

    bm25_global = bm25_metrics["global_metrics"]
    dense_global = dense_metrics["global_metrics"]
    compared_metrics: dict[str, Any] = {
        "top_k": k,
        "nandina8_exact": {},
        "hs4": {},
        "hs2": {},
        "mrr": {
            "bm25": bm25_global.get("mrr"),
            "dense": dense_global.get("mrr"),
            "delta": dense_global.get("mrr", 0.0) - bm25_global.get("mrr", 0.0),
        },
    }
    for cutoff in [1, 3, 5, 10]:
        key = f"top_{cutoff}_accuracy"
        compared_metrics["nandina8_exact"][f"top_{cutoff}"] = {
            "bm25": bm25_global.get(key),
            "dense": dense_global.get(key),
            "delta": dense_global.get(key, 0.0) - bm25_global.get(key, 0.0),
        }
        compared_metrics["hs4"][f"top_{cutoff}"] = {
            "bm25": _rate(sum(1 for row in bm25_rows if _family_hit(row, 4, cutoff)), len(bm25_rows)),
            "dense": dense_global.get(f"top_{cutoff}_hs4_accuracy"),
        }
        compared_metrics["hs4"][f"top_{cutoff}"]["delta"] = (
            compared_metrics["hs4"][f"top_{cutoff}"]["dense"] - compared_metrics["hs4"][f"top_{cutoff}"]["bm25"]
        )
        compared_metrics["hs2"][f"top_{cutoff}"] = {
            "bm25": _rate(sum(1 for row in bm25_rows if _family_hit(row, 2, cutoff)), len(bm25_rows)),
            "dense": dense_global.get(f"top_{cutoff}_hs2_accuracy"),
        }
        compared_metrics["hs2"][f"top_{cutoff}"]["delta"] = (
            compared_metrics["hs2"][f"top_{cutoff}"]["dense"] - compared_metrics["hs2"][f"top_{cutoff}"]["bm25"]
        )

    comparison: dict[str, Any] = {
        "script": "src.analysis.compare_bm25_dense",
        "input": {
            "bm25_metrics": _report_path(bm25_metrics_path, root),
            "bm25_results": _report_path(bm25_results_path, root),
            "dense_metrics": _report_path(dense_metrics_path, root),
            "dense_results": _report_path(dense_results_path, root),
        },
        "cases": {
            "bm25_rows": len(bm25_rows),
            "dense_rows": len(dense_rows),
            "shared_cases": len(shared_ids),
        },
        "metrics": compared_metrics,
        "case_outcomes_top_10": {
            "won_by_dense_count": len(won_by_dense),
            "lost_by_dense_count": len(lost_by_dense),
            "both_fail_count": len(both_fail),
            "both_hit_count": len(both_hit),
            "won_by_dense_case_ids": won_by_dense[:100],
            "lost_by_dense_case_ids": lost_by_dense[:100],
        },
        "families": {
            "dense_improves_more_by_partida_top_10": _family_deltas(bm25_rows, dense_rows, 10, "partida_ref", args.min_group_size)[:10],
            "dense_worst_by_partida_top_10": list(reversed(_family_deltas(bm25_rows, dense_rows, 10, "partida_ref", args.min_group_size)[-10:])),
            "both_fail_partida_counts_top_10": [
                {"partida_ref": group, "cases": count} for group, count in hs4_fail_counter.most_common(20)
            ],
            "dense_win_partida_counts_top_10": [
                {"partida_ref": group, "cases": count} for group, count in hs4_counter.most_common(20)
            ],
        },
        "warnings": [
            "Dense run uses brute-force vector search, not HNSW.",
            "Comparison uses BM25 and dense result files already present under outputs/.",
        ],
    }

    json_path = output_dir / "comparison_bm25_dense.json"
    md_path = output_dir / "comparison_bm25_dense.md"
    _write_json(json_path, comparison)
    ensure_parent(md_path)
    md_path.write_text(_summary_markdown(comparison), encoding="utf-8")
    return comparison


def _summary_markdown(comparison: Mapping[str, Any]) -> str:
    metrics = comparison["metrics"]
    outcome = comparison["case_outcomes_top_10"]
    lines = [
        "# Comparacion BM25 vs Text2Trade dense v0.1",
        "",
        "## Resultados globales",
        "",
    ]
    for cutoff in [1, 3, 5, 10]:
        row = metrics["nandina8_exact"][f"top_{cutoff}"]
        lines.append(
            f"- Top-{cutoff} NANDINA8: BM25={row['bm25']:.4f}, dense={row['dense']:.4f}, delta={row['delta']:+.4f}."
        )
    lines.extend(
        [
            f"- MRR: BM25={metrics['mrr']['bm25']:.4f}, dense={metrics['mrr']['dense']:.4f}, delta={metrics['mrr']['delta']:+.4f}.",
            f"- Top-10 HS4: BM25={metrics['hs4']['top_10']['bm25']:.4f}, dense={metrics['hs4']['top_10']['dense']:.4f}, delta={metrics['hs4']['top_10']['delta']:+.4f}.",
            f"- Top-10 HS2: BM25={metrics['hs2']['top_10']['bm25']:.4f}, dense={metrics['hs2']['top_10']['dense']:.4f}, delta={metrics['hs2']['top_10']['delta']:+.4f}.",
            "",
            "## Casos",
            "",
            f"- Ganados por dense en Top-10: {outcome['won_by_dense_count']}.",
            f"- Perdidos por dense en Top-10: {outcome['lost_by_dense_count']}.",
            f"- Ambos fallan en Top-10: {outcome['both_fail_count']}.",
            f"- Ambos aciertan en Top-10: {outcome['both_hit_count']}.",
            "",
            "## Lectura metodologica",
            "",
            "La comparacion es de recuperacion documental. Dense usa fuerza bruta sobre vectores congelados; no usa HNSW ni LLM.",
            "",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare BM25 baseline against dense Text2Trade outputs.")
    parser.add_argument("--bm25-metrics", type=Path, default=DEFAULT_BM25_METRICS)
    parser.add_argument("--bm25-results", type=Path, default=DEFAULT_BM25_RESULTS)
    parser.add_argument("--dense-metrics", type=Path, default=DEFAULT_DENSE_METRICS)
    parser.add_argument("--dense-results", type=Path, default=DEFAULT_DENSE_RESULTS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--min-group-size", type=int, default=5)
    return parser


def main() -> int:
    comparison = compare(build_parser().parse_args())
    exact = comparison["metrics"]["nandina8_exact"]["top_10"]
    print("OK: comparacion BM25 vs dense completada")
    print(f"Top-10 BM25: {exact['bm25']:.4f}")
    print(f"Top-10 dense: {exact['dense']:.4f}")
    print(f"Delta Top-10: {exact['delta']:+.4f}")
    print(f"Ganados por dense Top-10: {comparison['case_outcomes_top_10']['won_by_dense_count']}")
    print(f"Perdidos por dense Top-10: {comparison['case_outcomes_top_10']['lost_by_dense_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
