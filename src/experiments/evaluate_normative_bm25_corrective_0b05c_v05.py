"""v0.5 comparison and aggregate contracts for the 0B-05C recovery gate.

This module changes validation boundaries only. Retrieval, tokenization, ranking,
and the prospective MRR definitions remain delegated to the audited v0.4 code.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any, Mapping, Sequence

from . import evaluate_normative_bm25_corrective_0b05c_v01 as legacy
from . import evaluate_normative_bm25_corrective_0b05c_v04 as v04
from .prepare_0b05c_corrective_numerical_gate_v05 import ContractViolation, require


EVALSET = v04.EVALSET
CONFIG = v04.CONFIG
EV03_CANDIDATE_FIELDS = v04.EV03_CANDIDATE_FIELDS
EV03_CASE_FIELDS = v04.EV03_CASE_FIELDS
EV04_CANDIDATE_FIELDS = v04.EV04_CANDIDATE_FIELDS
EV04_CASE_FIELDS = v04.EV04_CASE_FIELDS
EV04_METRIC_ORDER = v04.EV04_METRIC_ORDER
EV04_AGGREGATE_METRIC_ORDER = v04.EV04_AGGREGATE_METRIC_ORDER
MRR_DEFINITION = v04.MRR_DEFINITION
build_ev04_enriched_metrics = v04.build_ev04_enriched_metrics
materialize_corrective_corpus = v04.materialize_corrective_corpus
evaluate_arm = v04.evaluate_arm

METRIC_FIELDS = {"metric", "numerator", "denominator", "value"}
AGGREGATE_FIELDS = {
    "metric", "original_numerator", "corrected_numerator", "denominator",
    "original_value", "corrected_value", "absolute_delta",
}


def _integer(value: Any, label: str, *, minimum: int = 0) -> int:
    text = str(value).strip()
    require(text.isdigit(), f"{label} is not a non-negative integer")
    number = int(text)
    require(number >= minimum, f"{label} is below {minimum}")
    return number


def _case_summary_by_id(rows: Sequence[Mapping[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for raw in rows:
        require(isinstance(raw, Mapping), f"{label} case summary row is malformed")
        row = dict(raw)
        case_id = str(row.get("case_id", "")).strip()
        require(case_id and case_id not in out, f"{label} duplicate or empty case_id: {case_id!r}")
        require(str(row.get("nandina_ref", "")).strip(), f"{label} missing nandina_ref: {case_id}")
        _integer(row.get("retrieved_count"), f"{label} retrieved_count {case_id}")
        _integer(row.get("rank_ref"), f"{label} rank_ref {case_id}")
        out[case_id] = row
    require(out, f"{label} case summary is empty")
    return out


def effective_rankings_v05(
    candidates: Sequence[Mapping[str, Any]],
    summaries: Mapping[str, Mapping[str, Any]],
    label: str,
    *,
    require_unique_codes: bool,
) -> dict[str, tuple[str, ...]]:
    """Validate candidate groups while allowing only contractually empty cases."""

    grouped: dict[str, list[tuple[int, str]]] = {case_id: [] for case_id in summaries}
    for row in candidates:
        require(isinstance(row, Mapping), f"{label} candidate row is malformed")
        case_id = str(row.get("case_id", "")).strip()
        require(case_id in grouped, f"{label} candidate references unknown case_id: {case_id!r}")
        code = str(row.get("candidate_code", "")).strip()
        require(code, f"{label} candidate code is empty: {case_id}")
        require(str(row.get("nandina_ref", "")).strip() == str(summaries[case_id].get("nandina_ref", "")).strip(), f"{label} candidate nandina_ref mismatch: {case_id}")
        grouped[case_id].append((_integer(row.get("candidate_rank"), f"{label} rank {case_id}", minimum=1), code))

    rankings: dict[str, tuple[str, ...]] = {}
    for case_id, ranked in grouped.items():
        summary = summaries[case_id]
        retrieved = _integer(summary.get("retrieved_count"), f"{label} retrieved_count {case_id}")
        rank_ref = _integer(summary.get("rank_ref"), f"{label} rank_ref {case_id}")
        if not ranked:
            require(retrieved == 0, f"{label} candidate group missing for nonempty case: {case_id}")
            require(rank_ref == 0, f"{label} empty ranking must have rank_ref=0: {case_id}")
            for field in ("top1_code", "top1_doc_id", "top1_score"):
                require(str(summary.get(field, "")).strip() == "", f"{label} empty ranking has nonempty {field}: {case_id}")
            rankings[case_id] = ()
            continue
        require(retrieved > 0, f"{label} candidates present for retrieved_count=0: {case_id}")
        require(len(ranked) == retrieved, f"{label} candidate count differs from retrieved_count: {case_id}")
        ranked.sort(key=lambda item: item[0])
        require([rank for rank, _ in ranked] == list(range(1, len(ranked) + 1)), f"{label} ranks are not contiguous: {case_id}")
        codes = tuple(code for _, code in ranked)
        if require_unique_codes:
            require(len(codes) == len(set(codes)), f"{label} effective ranking has duplicate codes: {case_id}")
        require(str(summary.get("top1_code", "")).strip() == codes[0], f"{label} top1_code mismatch: {case_id}")
        reference = str(summary.get("nandina_ref", "")).strip()
        require(rank_ref == _rank_of(codes, reference), f"{label} summary rank_ref differs from effective ranking: {case_id}")
        rankings[case_id] = codes
    return rankings


def _rank_of(codes: Sequence[str], code: str) -> int:
    try:
        return list(codes).index(code) + 1
    except ValueError:
        return 0


def produce_case_level_comparison(
    arm_name: str,
    original_cases: Sequence[Mapping[str, Any]],
    corrective_cases: Sequence[Mapping[str, Any]],
    original_candidates: Sequence[Mapping[str, Any]],
    corrective_candidates: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    contract = legacy.case_level_comparison_contract(arm_name)
    original = _case_summary_by_id(original_cases, f"{arm_name} original")
    corrected = _case_summary_by_id(corrective_cases, f"{arm_name} corrective")
    require(set(original) == set(corrected), "Case-level comparison requires identical case IDs")
    unique = arm_name == "EV04"
    original_rankings = effective_rankings_v05(original_candidates, original, f"{arm_name} original", require_unique_codes=unique)
    corrected_rankings = effective_rankings_v05(corrective_candidates, corrected, f"{arm_name} corrective", require_unique_codes=unique)
    rows: list[dict[str, Any]] = []
    for case_id in sorted(original):
        left, right = original[case_id], corrected[case_id]
        reference = str(left["nandina_ref"]).strip()
        require(reference == str(right["nandina_ref"]).strip(), f"Case reference changed: {case_id}")
        left_codes, right_codes = original_rankings[case_id], corrected_rankings[case_id]
        left_rank, right_rank = _rank_of(left_codes, reference), _rank_of(right_codes, reference)
        row: dict[str, Any] = {
            "case_id": case_id, "nandina_ref": reference,
            "original_rank_ref": left_rank, "corrected_rank_ref": right_rank,
            "ranking_changed": left_codes != right_codes,
            "rank_convention": "0=NOT_FOUND/EMPTY",
        }
        for k in contract["k_values"]:
            row[f"original_hit_{k}"] = int(1 <= left_rank <= k)
            row[f"corrected_hit_{k}"] = int(1 <= right_rank <= k)
        for code in ("87044110", "87045110"):
            old, new = _rank_of(left_codes, code), _rank_of(right_codes, code)
            row[f"original_rank_{code}"] = old
            row[f"corrected_rank_{code}"] = new
            row[f"original_contains_{code}"] = old > 0
            row[f"corrected_contains_{code}"] = new > 0
        expected_fields = list(contract["field_order"])
        require(set(row) == set(expected_fields), f"{arm_name} comparison schema drift")
        rows.append({field: row[field] for field in expected_fields})
    return rows


def _finite(value: Any, label: str) -> float:
    require(isinstance(value, (int, float)) and not isinstance(value, bool), f"{label} is not numeric")
    number = float(value)
    require(math.isfinite(number), f"{label} is not finite")
    return number


def validate_metric_table(metrics: Mapping[str, Any], label: str, expected_names: Sequence[str] | None = None) -> list[dict[str, Any]]:
    table = metrics.get("metric_table")
    require(isinstance(table, list) and table, f"{label} metric_table is missing")
    rows: list[dict[str, Any]] = []
    for raw in table:
        require(isinstance(raw, Mapping) and set(raw) == METRIC_FIELDS, f"{label} metric row field set changed")
        row = dict(raw)
        metric = row.get("metric")
        require(isinstance(metric, str) and metric, f"{label} metric name is malformed")
        _finite(row["numerator"], f"{label} {metric} numerator")
        denominator = row["denominator"]
        require(isinstance(denominator, int) and not isinstance(denominator, bool) and denominator > 0, f"{label} {metric} denominator must be a positive integer")
        _finite(row["value"], f"{label} {metric} value")
        rows.append(row)
    names = [row["metric"] for row in rows]
    require(len(names) == len(set(names)), f"{label} metric names are duplicated")
    if expected_names is not None:
        require(names == list(expected_names), f"{label} metric row order changed")
    return rows


def _compare_complete(expected: Any, actual: Any, label: str) -> None:
    require(type(actual) is type(expected), f"{label} type changed")
    if isinstance(expected, Mapping):
        require(set(actual) == set(expected), f"{label} key set changed")
        for key in expected:
            _compare_complete(expected[key], actual[key], f"{label}.{key}")
    elif isinstance(expected, list):
        require(len(actual) == len(expected), f"{label} list length changed")
        for index, (left, right) in enumerate(zip(expected, actual, strict=True)):
            _compare_complete(left, right, f"{label}[{index}]")
    elif isinstance(expected, (int, float)) and not isinstance(expected, bool):
        require(math.isfinite(float(actual)), f"{label} is nonfinite")
        require(actual == expected, f"{label} value changed")
    else:
        require(actual == expected, f"{label} value changed")


def validate_complete_metrics_v05(arm: str, case_rows: Sequence[Mapping[str, Any]], metrics: Mapping[str, Any], *, require_real_case_count: bool = True) -> dict[str, Any]:
    """Validate the complete persisted metric object against case-summary derivation."""

    require(isinstance(metrics, Mapping), f"{arm} metrics object is malformed")
    if require_real_case_count:
        require(len(case_rows) == 1056, f"{arm} metrics require 1056 case rows")
    if arm == "EV04":
        expected = v04.build_ev04_enriched_metrics(case_rows, require_real_case_count=require_real_case_count)
        require(len(expected) == 92 and len(expected["metric_table"]) == 27, "EV04 canonical metric cardinality drift")
        validate_metric_table(metrics, arm, EV04_METRIC_ORDER)
    else:
        expected = legacy.flat._metrics(case_rows)
        validate_metric_table(metrics, arm, [row["metric"] for row in expected["metric_table"]])
    _compare_complete(expected, dict(metrics), f"{arm} complete metrics")
    return {"status": "PASS_EXACT", "key_count": len(expected), "metric_row_count": len(expected["metric_table"])}


def validate_aggregate_rows(rows: Sequence[Mapping[str, Any]], expected_names: Sequence[str], label: str) -> list[dict[str, Any]]:
    require(isinstance(rows, Sequence) and not isinstance(rows, (str, bytes)), f"{label} aggregate is malformed")
    normalized: list[dict[str, Any]] = []
    for raw in rows:
        require(isinstance(raw, Mapping) and set(raw) == AGGREGATE_FIELDS, f"{label} aggregate row field set changed")
        row = dict(raw)
        require(isinstance(row["metric"], str) and row["metric"], f"{label} metric is malformed")
        require(isinstance(row["denominator"], int) and not isinstance(row["denominator"], bool) and row["denominator"] > 0, f"{label} denominator must be positive integer")
        for field in AGGREGATE_FIELDS - {"metric", "denominator"}:
            _finite(row[field], f"{label} {row['metric']} {field}")
        normalized.append(row)
    require([row["metric"] for row in normalized] == list(expected_names), f"{label} aggregate metric order changed")
    return normalized


def produce_aggregate_comparison_v05(
    original_metrics: Mapping[str, Any],
    corrective_metrics: Mapping[str, Any],
    *,
    arm: str,
) -> list[dict[str, Any]]:
    expected = list(EV04_METRIC_ORDER) if arm == "EV04" else None
    left = validate_metric_table(original_metrics, f"{arm} original", expected)
    names = [row["metric"] for row in left]
    right = validate_metric_table(corrective_metrics, f"{arm} corrective", names)
    rows: list[dict[str, Any]] = []
    for old, new in zip(left, right, strict=True):
        require(old["denominator"] == new["denominator"], f"{arm} denominator mismatch: {old['metric']}")
        rows.append({
            "metric": old["metric"], "original_numerator": old["numerator"],
            "corrected_numerator": new["numerator"], "denominator": old["denominator"],
            "original_value": old["value"], "corrected_value": new["value"],
            "absolute_delta": float(new["value"]) - float(old["value"]),
        })
    if arm == "EV04":
        denominator = original_metrics.get("cases_evaluated")
        require(isinstance(denominator, int) and denominator > 0 and corrective_metrics.get("cases_evaluated") == denominator, "EV04 contribution denominator mismatch")
        contribution = {
            "metric": "mrr_101_200_contribution",
            "original_numerator": _finite(original_metrics.get("mrr_101_200_contribution_numerator"), "EV04 original contribution numerator"),
            "corrected_numerator": _finite(corrective_metrics.get("mrr_101_200_contribution_numerator"), "EV04 corrected contribution numerator"),
            "denominator": denominator,
            "original_value": _finite(original_metrics.get("mrr_101_200_contribution"), "EV04 original contribution"),
            "corrected_value": _finite(corrective_metrics.get("mrr_101_200_contribution"), "EV04 corrected contribution"),
            "absolute_delta": float(corrective_metrics["mrr_101_200_contribution"]) - float(original_metrics["mrr_101_200_contribution"]),
        }
        rows = [*rows[:2], contribution, *rows[2:]]
        expected_order = EV04_AGGREGATE_METRIC_ORDER
    else:
        expected_order = tuple(names)
    return validate_aggregate_rows(rows, expected_order, f"{arm} comparison")


def compare_complete_ev03_control_v05(ranking: Path, summary: Path) -> dict[str, Any]:
    cases = legacy.flat._read_csv(summary)
    candidates = legacy.flat._read_csv(ranking)
    rows = produce_case_level_comparison("EV03", cases, cases, candidates, candidates)
    empty = sum(1 for row in cases if int(row["retrieved_count"]) == 0)
    require(len(rows) == 1056 and empty == 10, "Frozen EV03 empty-ranking contract changed")
    return {"status": "PASS_EXACT", "case_count": len(rows), "valid_empty_ranking_count": empty, "rank_convention": "0=NOT_FOUND/EMPTY"}
