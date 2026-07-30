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
from ..evaluation.metrics import acc_at_k, mrr_from_rank
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_RESPONSES = Path("outputs/evaluation/llm_rerank_pool_devset_v0.1/rerank_responses.jsonl")
DEFAULT_CANDIDATE_POOL = Path("outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool.csv")
DEFAULT_POOL_METRICS = Path("outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool_metrics.json")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_rerank_pool_devset_v0.1")
DEFAULT_POOL_STRATEGY = "hierarchical_80_dual_backfill_20"
K_LIST = [1, 3, 5, 10]


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc.msg}") from exc
            if not isinstance(item, dict):
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: root is not an object")
            rows.append(item)
    return rows


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


def _rank_metric(rank: int, missing_value: int) -> int:
    return rank if rank > 0 else missing_value


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _rank_of_code(codes: Sequence[str], expected: str) -> int:
    for rank, code in enumerate(codes, start=1):
        if code == expected:
            return rank
    return 0


def _ranked_codes(record: Mapping[str, Any]) -> list[str]:
    parsed = record.get("parsed_response")
    if not isinstance(parsed, Mapping):
        return []
    ranked = parsed.get("ranked_candidates")
    if not isinstance(ranked, list):
        return []
    codes: list[str] = []
    seen: set[str] = set()
    for item in ranked:
        if not isinstance(item, Mapping):
            continue
        code = _clean(item.get("nandina"))
        if code and code not in seen:
            seen.add(code)
            codes.append(code)
    return codes


def _pool_lookup(rows: Sequence[Mapping[str, str]], strategy: str) -> dict[tuple[str, str], Mapping[str, str]]:
    lookup: dict[tuple[str, str], Mapping[str, str]] = {}
    for row in rows:
        if row.get("pool_strategy") != strategy:
            continue
        lookup[(row["case_id"], row["candidate_code"])] = row
    return lookup


def _load_pool_metrics(path: Path | None, strategy: str) -> dict[str, Any]:
    if path is None or not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("metrics_by_strategy", {}).get(strategy, {})


def _metrics_from_ranks(rows: Sequence[Mapping[str, Any]], rank_field: str, candidate_limit: int) -> dict[str, Any]:
    ranks = [int(row[rank_field]) for row in rows]
    metrics = {
        "cases": len(rows),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "not_found": sum(1 for rank in ranks if rank <= 0),
    }
    for k in K_LIST:
        capped_k = min(k, candidate_limit)
        metrics[f"top_{k}"] = _mean([acc_at_k(rank, capped_k) for rank in ranks])
    return metrics


def _summary_markdown(metrics: Mapping[str, Any]) -> str:
    lines = [
        "# Evaluacion LLM rerank pool v0.1",
        "",
        "## Alcance",
        "",
        "Evaluacion cerrada del re-ranking LLM sobre candidatos efectivamente enviados. No compara el LLM contra `final_pool@100` cuando `candidate_limit` es menor que 100.",
        "",
        "## Metricas principales",
        "",
        f"- Casos totales: {metrics['cases_total']}.",
        f"- Candidate limit: {metrics['candidate_limit']}.",
        f"- `sent_pool_at_candidate_limit`: {metrics['sent_pool_at_candidate_limit']:.4f}.",
        f"- JSON valido: {metrics['valid_json_rate']:.4f}.",
        f"- Adherencia cruda al esquema: {metrics['raw_schema_adherence_rate']:.4f}.",
        f"- Casos normalizados: {metrics['normalization_cases']}.",
        f"- Violaciones de pool: {metrics['pool_violation_rate']:.4f}.",
        f"- Top-1 global: {metrics['llm_global']['top_1']:.4f}.",
        f"- Top-1 condicionado: {metrics['llm_conditioned_on_sent_pool']['top_1']:.4f}.",
        f"- MRR global: {metrics['llm_global']['mrr']:.4f}.",
        f"- MRR condicionado: {metrics['llm_conditioned_on_sent_pool']['mrr']:.4f}.",
        "",
        "## Comparacion contra ranking original enviado",
        "",
        f"- Ganados: {metrics['comparison_vs_original_sent_pool']['ganados']}.",
        f"- Perdidos: {metrics['comparison_vs_original_sent_pool']['perdidos']}.",
        f"- Sin cambio: {metrics['comparison_vs_original_sent_pool']['sin_cambio']}.",
        "",
    ]
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    responses_path = resolve_project_path(args.responses_jsonl)
    candidate_pool_path = resolve_project_path(args.candidate_pool)
    pool_metrics_path = resolve_project_path(args.pool_metrics) if args.pool_metrics else None
    output_dir = resolve_project_path(args.output_dir)
    start = time.time()

    records = _read_jsonl(responses_path)
    pool_rows = _read_csv(candidate_pool_path)
    lookup = _pool_lookup(pool_rows, args.pool_strategy)
    pool_metrics = _load_pool_metrics(pool_metrics_path, args.pool_strategy)

    eval_rows: list[dict[str, Any]] = []
    for record in records:
        case_id = _clean(record.get("case_id"))
        expected = _clean(record.get("nandina_ref"))
        sent_codes = [_clean(code) for code in record.get("sent_pool_codes", []) if _clean(code)]
        candidate_limit = int(record.get("candidate_limit") or args.candidate_limit)
        ranked_codes = _ranked_codes(record)
        json_valid = bool(record.get("json_valid"))
        pool_violation = bool(record.get("pool_violation"))
        normalization_actions = [str(item) for item in record.get("normalization_actions", [])]
        sent_pool_contains_expected = expected in set(sent_codes)
        llm_rank = _rank_of_code(ranked_codes, expected) if json_valid and not pool_violation else 0
        original_sent_rank = _rank_of_code(sent_codes, expected)

        expected_pool_row = lookup.get((case_id, expected))
        original_pool_rank_100 = int(expected_pool_row["candidate_rank_pool"]) if expected_pool_row else 0
        hierarchical_rank = int(expected_pool_row["candidate_rank_hierarchical"]) if expected_pool_row and expected_pool_row["candidate_rank_hierarchical"] else 0

        missing_value = candidate_limit + 1
        llm_value = _rank_metric(llm_rank, missing_value)
        original_value = _rank_metric(original_sent_rank, missing_value)
        if llm_value < original_value:
            outcome = "ganado"
        elif llm_value > original_value:
            outcome = "perdido"
        else:
            outcome = "sin_cambio"

        eval_rows.append(
            {
                "case_id": case_id,
                "descripcion": _clean(record.get("descripcion")),
                "nandina_ref": expected,
                "pool_strategy": _clean(record.get("pool_strategy")),
                "candidate_limit": candidate_limit,
                "sent_pool_contains_expected": int(sent_pool_contains_expected),
                "json_valid": int(json_valid),
                "pool_violation": int(pool_violation),
                "normalization_actions": " | ".join(normalization_actions),
                "codes_outside_pool": " ".join(record.get("codes_outside_pool", [])),
                "selected_nandina": _clean(record.get("selected_nandina")),
                "ranked_candidates": " ".join(ranked_codes),
                "llm_rank": llm_rank,
                "original_sent_rank": original_sent_rank,
                "original_pool_rank_100": original_pool_rank_100,
                "hierarchical_rank": hierarchical_rank,
                "outcome_vs_original_sent_pool": outcome,
                "llm_raises_expected": int(outcome == "ganado"),
                "llm_lowers_expected": int(outcome == "perdido"),
                "error": _clean(record.get("error")),
            }
        )

    candidate_limit = int(eval_rows[0]["candidate_limit"]) if eval_rows else args.candidate_limit
    conditioned_rows = [row for row in eval_rows if int(row["sent_pool_contains_expected"]) == 1]
    valid_rows = [row for row in eval_rows if int(row["json_valid"]) == 1 and int(row["pool_violation"]) == 0]
    raw_schema_valid_rows = [
        row for row in eval_rows if int(row["json_valid"]) == 1 and not _clean(row["normalization_actions"])
    ]
    comparison_rows = conditioned_rows
    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_llm_rerank_pool",
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
            "responses_jsonl": _rel(responses_path, root),
            "responses_sha256": sha256_file(responses_path),
            "candidate_pool": _rel(candidate_pool_path, root),
            "candidate_pool_sha256": sha256_file(candidate_pool_path),
            "pool_metrics": _rel(pool_metrics_path, root) if pool_metrics_path else "",
        },
        "pool_strategy": args.pool_strategy,
        "candidate_limit": candidate_limit,
        "cases_total": len(eval_rows),
        "valid_json_cases": sum(int(row["json_valid"]) for row in eval_rows),
        "valid_json_rate": _mean([float(row["json_valid"]) for row in eval_rows]),
        "raw_schema_valid_cases": len(raw_schema_valid_rows),
        "raw_schema_adherence_rate": len(raw_schema_valid_rows) / len(eval_rows) if eval_rows else 0.0,
        "normalization_cases": sum(1 for row in eval_rows if _clean(row["normalization_actions"])),
        "pool_violation_cases": sum(int(row["pool_violation"]) for row in eval_rows),
        "pool_violation_rate": _mean([float(row["pool_violation"]) for row in eval_rows]),
        "invalid_or_rule_break_cases": len(eval_rows) - len(valid_rows),
        "cases_without_valid_response": sum(1 for row in eval_rows if int(row["json_valid"]) == 0),
        "cases_expected_not_in_sent_pool": sum(1 for row in eval_rows if int(row["sent_pool_contains_expected"]) == 0),
        "cases_expected_in_sent_pool": len(conditioned_rows),
        "sent_pool_at_candidate_limit": len(conditioned_rows) / len(eval_rows) if eval_rows else 0.0,
        "llm_global": _metrics_from_ranks(eval_rows, "llm_rank", candidate_limit),
        "llm_conditioned_on_sent_pool": _metrics_from_ranks(conditioned_rows, "llm_rank", candidate_limit),
        "original_sent_pool_global": _metrics_from_ranks(eval_rows, "original_sent_rank", candidate_limit),
        "original_sent_pool_conditioned": _metrics_from_ranks(conditioned_rows, "original_sent_rank", candidate_limit),
        "bm25_hierarchical_available_global": _metrics_from_ranks(eval_rows, "hierarchical_rank", max(candidate_limit, 100)),
        "final_pool_at_100_reference": pool_metrics.get("final_pool_at_100"),
        "union_oracle_at_100_reference": pool_metrics.get("union_oracle_at_100"),
        "comparison_vs_original_sent_pool": {
            "ganados": sum(1 for row in comparison_rows if row["outcome_vs_original_sent_pool"] == "ganado"),
            "perdidos": sum(1 for row in comparison_rows if row["outcome_vs_original_sent_pool"] == "perdido"),
            "sin_cambio": sum(1 for row in comparison_rows if row["outcome_vs_original_sent_pool"] == "sin_cambio"),
            "llm_raises_expected": sum(int(row["llm_raises_expected"]) for row in comparison_rows),
            "llm_lowers_expected": sum(int(row["llm_lowers_expected"]) for row in comparison_rows),
        },
        "controls": {
            "text2trade_executed": False,
            "paid_or_remote_api_used": False,
            "conditioned_metrics_denominator": "cases where expected NANDINA is within sent_pool_codes",
            "do_not_compare_llm_directly_to_final_pool_at_100_when_candidate_limit_lt_100": True,
        },
        "outputs": {
            "rerank_evaluation_csv": _rel(output_dir / "rerank_evaluation.csv", root),
            "rerank_metrics_json": _rel(output_dir / "rerank_metrics.json", root),
            "rerank_evaluation_summary_md": _rel(output_dir / "rerank_evaluation_summary.md", root),
        },
    }

    fields = [
        "case_id",
        "descripcion",
        "nandina_ref",
        "pool_strategy",
        "candidate_limit",
        "sent_pool_contains_expected",
        "json_valid",
        "pool_violation",
        "normalization_actions",
        "codes_outside_pool",
        "selected_nandina",
        "ranked_candidates",
        "llm_rank",
        "original_sent_rank",
        "original_pool_rank_100",
        "hierarchical_rank",
        "outcome_vs_original_sent_pool",
        "llm_raises_expected",
        "llm_lowers_expected",
        "error",
    ]
    _write_csv(output_dir / "rerank_evaluation.csv", eval_rows, fields)
    _write_json(output_dir / "rerank_metrics.json", metrics)
    ensure_parent(output_dir / "rerank_evaluation_summary.md")
    (output_dir / "rerank_evaluation_summary.md").write_text(_summary_markdown(metrics), encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate closed-pool LLM reranking outputs.")
    parser.add_argument("--responses-jsonl", type=Path, default=DEFAULT_RESPONSES)
    parser.add_argument("--candidate-pool", type=Path, default=DEFAULT_CANDIDATE_POOL)
    parser.add_argument("--pool-metrics", type=Path, default=DEFAULT_POOL_METRICS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--pool-strategy", default=DEFAULT_POOL_STRATEGY)
    parser.add_argument("--candidate-limit", type=int, default=20)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion rerank LLM completada")
    print(f"Casos: {metrics['cases_total']}")
    print(f"sent_pool_at_candidate_limit: {metrics['sent_pool_at_candidate_limit']:.4f}")
    print(f"Top-1 global: {metrics['llm_global']['top_1']:.4f}")
    print(f"Top-1 condicionado: {metrics['llm_conditioned_on_sent_pool']['top_1']:.4f}")
    print(f"Violaciones de pool: {metrics['pool_violation_cases']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
