from __future__ import annotations

import argparse
import csv
import json
import statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..evaluation.metrics import acc_at_k, mrr_from_rank
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_HYBRID_POOL = Path("outputs/evaluation/hybrid_historical_normative_pool_v0.1/hybrid_pool.csv")
DEFAULT_SAMPLE_CASES = Path("outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1/sample_cases.csv")
DEFAULT_NORMALIZED = Path("outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1/llm_rerank_normalized.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1")

POOL_STRATEGY = "historical_first_80_normative_20"
CANDIDATE_LIMIT = 10
K_VALUES = [1, 3, 5, 10]


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


def _rel(path: Path) -> str:
    root = project_root()
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _median(values: Sequence[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def _bool(value: object) -> bool:
    return _clean(value).lower() in {"true", "1", "yes"}


def _load_pool(path: Path, sample_ids: set[str]) -> tuple[dict[str, list[dict[str, Any]]], int]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    oracle_rows = 0
    for row in _read_csv(path):
        strategy = _clean(row.get("pool_strategy"))
        if "oracle" in strategy:
            oracle_rows += 1
            continue
        if strategy != POOL_STRATEGY:
            continue
        case_id = _clean(row.get("case_id"))
        if case_id not in sample_ids:
            continue
        grouped[case_id].append(
            {
                "rank": int(_clean(row.get("final_rank")) or "0"),
                "nandina": _clean(row.get("candidate_nandina")),
                "source_membership": _clean(row.get("source_membership")),
                "source_rank_history": _clean(row.get("source_rank_history")),
            }
        )
    for rows in grouped.values():
        rows.sort(key=lambda item: int(item["rank"]))
    return grouped, oracle_rows


def _load_llm_rankings(path: Path) -> tuple[dict[str, list[dict[str, Any]]], dict[str, dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    status: dict[str, dict[str, Any]] = {}
    for row in _read_csv(path):
        case_id = _clean(row.get("case_id"))
        if not case_id:
            continue
        status[case_id] = {
            "json_valid": _bool(row.get("json_valid")),
            "codes_outside_pool": int(_clean(row.get("codes_outside_pool")) or "0"),
            "ranking_incomplete": _bool(row.get("ranking_incomplete")),
            "duplicates": int(_clean(row.get("duplicates")) or "0"),
            "selected_rank1_outside_pool": _bool(row.get("selected_rank1_outside_pool")),
            "parse_error": _clean(row.get("parse_error")),
        }
        rank = _clean(row.get("normalized_rank"))
        code = _clean(row.get("nandina"))
        if rank and code and _bool(row.get("in_pool")) and not _bool(row.get("duplicate_code")):
            grouped[case_id].append({"rank": int(rank), "nandina": code})
    for rows in grouped.values():
        rows.sort(key=lambda item: int(item["rank"]))
    return grouped, status


def _rank_of_expected(ranking: Sequence[Mapping[str, Any]], expected: str) -> int:
    for idx, row in enumerate(ranking[:CANDIDATE_LIMIT], start=1):
        if _clean(row.get("nandina")) == expected:
            return idx
    return 0


def _metrics(rows: Sequence[Mapping[str, Any]], prefix: str) -> dict[str, Any]:
    metrics: dict[str, Any] = {
        f"{prefix}_mrr": _mean([float(row[f"{prefix}_reciprocal_rank"]) for row in rows]),
        f"{prefix}_median_rank_nonzero": _median([float(row[f"{prefix}_rank"]) for row in rows if int(row[f"{prefix}_rank"]) > 0]),
    }
    for k in K_VALUES:
        metrics[f"{prefix}_top_{k}"] = _mean([float(row[f"{prefix}_at_{k}"]) for row in rows])
    return metrics


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    metrics = payload["metrics"]
    lines = [
        "# LLM re-rank hybrid pool sample v0.1",
        "",
        "## Resultado",
        "",
        f"- Modelo: `{payload['model']}`.",
        f"- Pool: `{payload['pool_strategy']}`.",
        f"- Casos evaluados: {metrics['cases_evaluated']}.",
        f"- JSON valido: {metrics['json_valid_rate']:.4f}.",
        f"- Casos con violacion de pool: {metrics['pool_violation_cases']}.",
        "",
        "| Ranking | Top-1 | Top-3 | Top-5 | Top-10 | MRR |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        f"| Original enviado | {metrics['original_top_1']:.4f} | {metrics['original_top_3']:.4f} | {metrics['original_top_5']:.4f} | {metrics['original_top_10']:.4f} | {metrics['original_mrr']:.4f} |",
        f"| LLM | {metrics['llm_top_1']:.4f} | {metrics['llm_top_3']:.4f} | {metrics['llm_top_5']:.4f} | {metrics['llm_top_10']:.4f} | {metrics['llm_mrr']:.4f} |",
        "",
        "## Cambios",
        "",
        f"- Ganados: {metrics['won_cases']}.",
        f"- Perdidos: {metrics['lost_cases']}.",
        f"- Sin cambio: {metrics['unchanged_cases']}.",
        f"- Top-1 correctos degradados: {metrics['top1_correct_degraded_cases']}.",
        f"- Casos donde el LLM sube la NANDINA correcta: {metrics['llm_raises_correct_cases']}.",
        "",
        "## Decision",
        "",
        payload["decision"],
        "",
    ]
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    sample_path = resolve_project_path(args.sample_cases)
    normalized_path = resolve_project_path(args.normalized)
    output_dir = resolve_project_path(args.output_dir)
    sample_rows = _read_csv(sample_path)
    if len(sample_rows) != 20:
        raise ValueError(f"Expected 20 sample cases, found {len(sample_rows)}")
    sample_by_case = {_clean(row.get("case_id")): row for row in sample_rows}
    pool_by_case, oracle_rows_skipped = _load_pool(resolve_project_path(args.hybrid_pool), set(sample_by_case))
    llm_by_case, status_by_case = _load_llm_rankings(normalized_path)

    comparison_rows: list[dict[str, Any]] = []
    for case_id, sample in sample_by_case.items():
        expected = _clean(sample.get("expected_nandina"))
        original_ranking = pool_by_case.get(case_id, [])[:CANDIDATE_LIMIT]
        llm_ranking = llm_by_case.get(case_id, [])[:CANDIDATE_LIMIT]
        original_rank = _rank_of_expected(original_ranking, expected)
        llm_rank = _rank_of_expected(llm_ranking, expected)
        status = status_by_case.get(case_id, {})
        if llm_rank and (not original_rank or llm_rank < original_rank):
            outcome = "won"
        elif original_rank and (not llm_rank or llm_rank > original_rank):
            outcome = "lost"
        else:
            outcome = "unchanged"
        row: dict[str, Any] = {
            "case_id": case_id,
            "expected_nandina": expected,
            "sample_target_category": sample["sample_target_category"],
            "selection_source_category": sample["selection_source_category"],
            "support_bucket": sample["support_bucket"],
            "historical_support_count": sample["historical_support_count"],
            "original_rank": original_rank,
            "llm_rank": llm_rank,
            "rank_delta": "" if not original_rank or not llm_rank else original_rank - llm_rank,
            "outcome": outcome,
            "json_valid": int(bool(status.get("json_valid"))),
            "codes_outside_pool": int(status.get("codes_outside_pool", 0)),
            "ranking_incomplete": int(bool(status.get("ranking_incomplete"))),
            "duplicates": int(status.get("duplicates", 0)),
            "selected_rank1_outside_pool": int(bool(status.get("selected_rank1_outside_pool"))),
            "parse_error": _clean(status.get("parse_error")),
            "top1_correct_degraded": int(original_rank == 1 and llm_rank != 1),
            "llm_raises_correct": int(llm_rank and (not original_rank or llm_rank < original_rank)),
            "original_reciprocal_rank": mrr_from_rank(original_rank),
            "llm_reciprocal_rank": mrr_from_rank(llm_rank),
        }
        for k in K_VALUES:
            row[f"original_at_{k}"] = int(acc_at_k(original_rank, k))
            row[f"llm_at_{k}"] = int(acc_at_k(llm_rank, k))
        comparison_rows.append(row)

    metrics: dict[str, Any] = {
        "cases_evaluated": len(comparison_rows),
        **_metrics(comparison_rows, "original"),
        **_metrics(comparison_rows, "llm"),
        "won_cases": sum(1 for row in comparison_rows if row["outcome"] == "won"),
        "lost_cases": sum(1 for row in comparison_rows if row["outcome"] == "lost"),
        "unchanged_cases": sum(1 for row in comparison_rows if row["outcome"] == "unchanged"),
        "top1_correct_degraded_cases": sum(int(row["top1_correct_degraded"]) for row in comparison_rows),
        "llm_raises_correct_cases": sum(int(row["llm_raises_correct"]) for row in comparison_rows),
        "json_valid_cases": sum(int(row["json_valid"]) for row in comparison_rows),
        "json_valid_rate": _mean([float(row["json_valid"]) for row in comparison_rows]),
        "pool_violation_cases": sum(1 for row in comparison_rows if int(row["codes_outside_pool"]) or int(row["selected_rank1_outside_pool"])),
        "codes_outside_pool_total": sum(int(row["codes_outside_pool"]) for row in comparison_rows),
        "duplicate_cases": sum(1 for row in comparison_rows if int(row["duplicates"])),
        "ranking_incomplete_cases": sum(1 for row in comparison_rows if int(row["ranking_incomplete"])),
    }
    sample_composition: dict[str, int] = {}
    for row in comparison_rows:
        sample_composition[row["sample_target_category"]] = sample_composition.get(row["sample_target_category"], 0) + 1
    metrics["sample_composition"] = sample_composition

    decision = (
        "No escalar a 9C-B: el re-ranking LLM degrada Top-1 o MRR frente al ranking original enviado."
        if metrics["llm_top_1"] < metrics["original_top_1"] or metrics["llm_mrr"] < metrics["original_mrr"]
        else "Pasar a 9C-B: no degrada Top-1/MRR y no presenta violaciones de pool."
    )
    if metrics["pool_violation_cases"]:
        decision = "No escalar a 9C-B: existen violaciones de pool o seleccion rank 1 fuera del pool."

    payload: dict[str, Any] = {
        "version": "v0.1",
        "phase": "9C-A",
        "model": args.model,
        "pool_strategy": POOL_STRATEGY,
        "candidate_limit": CANDIDATE_LIMIT,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "hybrid_pool": _rel(resolve_project_path(args.hybrid_pool)),
            "sample_cases": _rel(sample_path),
            "normalized": _rel(normalized_path),
        },
        "metrics": metrics,
        "decision": decision,
        "policy": {
            "openai_used": False,
            "remote_api_used": False,
            "ollama_local_only": True,
            "pool_strategy_used": POOL_STRATEGY,
            "oracle_used": False,
            "oracle_rows_skipped": oracle_rows_skipped,
        },
        "outputs": {
            "llm_rerank_metrics_json": _rel(output_dir / "llm_rerank_metrics.json"),
            "llm_rerank_summary_md": _rel(output_dir / "llm_rerank_summary.md"),
            "llm_rerank_case_comparison_csv": _rel(output_dir / "llm_rerank_case_comparison.csv"),
        },
    }

    fieldnames = [
        "case_id",
        "expected_nandina",
        "sample_target_category",
        "selection_source_category",
        "support_bucket",
        "historical_support_count",
        "original_rank",
        "llm_rank",
        "rank_delta",
        "outcome",
        "json_valid",
        "codes_outside_pool",
        "ranking_incomplete",
        "duplicates",
        "selected_rank1_outside_pool",
        "parse_error",
        "top1_correct_degraded",
        "llm_raises_correct",
        "original_reciprocal_rank",
        "llm_reciprocal_rank",
        *[f"original_at_{k}" for k in K_VALUES],
        *[f"llm_at_{k}" for k in K_VALUES],
    ]
    _write_csv(output_dir / "llm_rerank_case_comparison.csv", comparison_rows, fieldnames)
    _write_json(output_dir / "llm_rerank_metrics.json", payload)
    ensure_parent(output_dir / "llm_rerank_summary.md").write_text(_summary_markdown(payload), encoding="utf-8")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate local LLM re-ranking over the hybrid pool sample.")
    parser.add_argument("--hybrid-pool", default=str(DEFAULT_HYBRID_POOL))
    parser.add_argument("--sample-cases", default=str(DEFAULT_SAMPLE_CASES))
    parser.add_argument("--normalized", default=str(DEFAULT_NORMALIZED))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--model", default="qwen2.5:7b-instruct")
    return parser


def main() -> int:
    payload = evaluate(build_parser().parse_args())
    metrics = payload["metrics"]
    print("OK: evaluacion LLM rerank hibrido completada")
    print(
        f"Original @1={metrics['original_top_1']:.4f} @10={metrics['original_top_10']:.4f} MRR={metrics['original_mrr']:.4f}"
    )
    print(f"LLM @1={metrics['llm_top_1']:.4f} @10={metrics['llm_top_10']:.4f} MRR={metrics['llm_mrr']:.4f}")
    print(f"Ganados={metrics['won_cases']} Perdidos={metrics['lost_cases']} Sin cambio={metrics['unchanged_cases']}")
    print(payload["decision"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
