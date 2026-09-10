"""v0.4 corrective evaluator with explicit MRR@100 and legacy MRR@200."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from . import evaluate_normative_bm25_corrective_0b05c_v01 as legacy
from . import evaluate_normative_bm25_hierarchical_data_aduanas_v02 as hierarchical
from .prepare_0b05c_corrective_numerical_gate_v04 import ContractViolation, ROOT, require


EVALSET = legacy.EVALSET
CONFIG = legacy.CONFIG
EV03_CANDIDATE_FIELDS = legacy.EV03_CANDIDATE_FIELDS
EV03_CASE_FIELDS = legacy.EV03_CASE_FIELDS
EV04_CANDIDATE_FIELDS = legacy.EV04_CANDIDATE_FIELDS
EV04_CASE_FIELDS = legacy.EV04_CASE_FIELDS
materialize_corrective_corpus = legacy.materialize_corrective_corpus
compare_control_reproduction = legacy.compare_control_reproduction
produce_case_level_comparison = legacy.produce_case_level_comparison
produce_aggregate_comparison = legacy.produce_aggregate_comparison

MRR_DEFINITION = (
    "MRR@100 is the arithmetic mean of 1/rank_ref for ranks 1..100 and zero "
    "otherwise; MRR@200 preserves the legacy hierarchical evaluator exactly: "
    "sum(float(reciprocal_rank)) in frozen CSV row order divided by case count."
)
LEGACY_METRIC_ORDER = (
    "mrr",
    *(f"top_{k}" for k in hierarchical.K_VALUES),
    *(f"recall_at_{k}" for k in hierarchical.RECALL_K_VALUES),
    "pool_recall_at_200",
    *(f"{name}_at_{k}" for k in hierarchical.HIERARCHICAL_K_VALUES for name in ("exact", "hs6", "hs4", "chapter")),
)
EV04_METRIC_ORDER = ("mrr_at_100", "mrr_at_200", *LEGACY_METRIC_ORDER[1:])
EV04_AGGREGATE_METRIC_ORDER = (
    "mrr_at_100",
    "mrr_at_200",
    "mrr_101_200_contribution",
    *EV04_METRIC_ORDER[2:],
)
METRIC_ROW_FIELDS = ("metric", "numerator", "denominator", "value")


def _rank(row: Mapping[str, Any]) -> int:
    try:
        return int(row.get("rank_ref", 0))
    except (TypeError, ValueError) as exc:
        raise ContractViolation("EV04 rank_ref is not an integer") from exc


def _exact_rank_sum(case_rows: Sequence[Mapping[str, Any]], depth: int) -> Fraction:
    total = Fraction(0, 1)
    for row in case_rows:
        rank = _rank(row)
        if 1 <= rank <= depth:
            total += Fraction(1, rank)
    return total


def _metric_row_exact(name: str, numerator: Fraction, denominator: int) -> dict[str, Any]:
    return {
        "metric": name,
        "numerator": float(numerator),
        "denominator": denominator,
        "value": float(numerator / denominator),
    }


def build_ev04_enriched_metrics(
    case_rows: Sequence[Mapping[str, Any]],
    base_metrics: Mapping[str, Any] | None = None,
    *,
    require_real_case_count: bool = False,
) -> dict[str, Any]:
    """Build the canonical v0.4 schema strictly from case-level rows."""

    denominator = len(case_rows)
    require(denominator > 0, "EV04 metrics require at least one case row")
    if require_real_case_count:
        require(denominator == 1056, "EV04 real execution requires exactly 1056 cases")
    base = dict(base_metrics or hierarchical.metrics_from_cases(case_rows))
    table = base.get("metric_table")
    require(isinstance(table, list) and table, "EV04 base metric_table is missing")
    require(table[0].get("metric") == "mrr", "EV04 legacy metric_table prefix changed")

    exact_100 = _exact_rank_sum(case_rows, 100)
    exact_200 = _exact_rank_sum(case_rows, 200)
    numerator_100 = float(exact_100)
    mrr_100 = float(exact_100 / denominator)
    # Frozen legacy behavior: preserve float parsing and CSV row order exactly.
    numerator_200 = sum(float(row["reciprocal_rank"]) for row in case_rows)
    mrr_200 = numerator_200 / denominator
    contribution = exact_200 - exact_100

    out = dict(base)
    out.update({
        "mrr": mrr_200,
        "mrr_numerator": numerator_200,
        "mrr_denominator": denominator,
        "mrr_at_100": mrr_100,
        "mrr_at_200": mrr_200,
        "mrr_at_100_numerator": numerator_100,
        "mrr_at_200_numerator": numerator_200,
        "mrr_at_100_denominator": denominator,
        "mrr_at_200_denominator": denominator,
        "mrr_definition": MRR_DEFINITION,
        "mrr_101_200_contribution_numerator": float(contribution),
        "mrr_101_200_contribution": float(contribution / denominator),
        "metric_table": [
            _metric_row_exact("mrr_at_100", exact_100, denominator),
            hierarchical.metric_row("mrr_at_200", numerator_200, denominator),
            *[dict(row) for row in table[1:]],
        ],
    })
    validate_enriched_ev04_metrics(out)
    return out


def validate_enriched_ev04_metrics(metrics: Mapping[str, Any]) -> None:
    table = metrics.get("metric_table")
    require(isinstance(table, list), "EV04 enriched metric_table is missing")
    require([row.get("metric") for row in table] == list(EV04_METRIC_ORDER), "EV04 metric names or order changed")
    for row in table:
        require(tuple(row) == METRIC_ROW_FIELDS, f"EV04 metric row schema changed: {row.get('metric')}")
    denominator = metrics.get("cases_evaluated")
    require(metrics.get("mrr_at_100_denominator") == denominator, "EV04 MRR@100 denominator drift")
    require(metrics.get("mrr_at_200_denominator") == denominator, "EV04 MRR@200 denominator drift")
    require(metrics.get("mrr_denominator") == denominator, "EV04 legacy MRR denominator drift")
    require(metrics.get("mrr") == metrics.get("mrr_at_200"), "EV04 legacy mrr must alias MRR@200")
    require(metrics.get("mrr_numerator") == metrics.get("mrr_at_200_numerator"), "EV04 legacy numerator must alias MRR@200")
    require(metrics.get("mrr_definition") == MRR_DEFINITION, "EV04 MRR definition drift")
    require(isinstance(metrics.get("mrr_101_200_contribution_numerator"), float), "EV04 contribution numerator type drift")
    require(isinstance(metrics.get("mrr_101_200_contribution"), float), "EV04 contribution type drift")


def _finite_numeric(metrics: Mapping[str, Any], key: str, label: str) -> int | float:
    value = metrics.get(key)
    require(
        isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value)),
        f"{label} {key} must be finite numeric",
    )
    return value


def produce_ev04_aggregate_comparison_v04(
    original_metrics: Mapping[str, Any],
    corrective_metrics: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Compare the canonical 27-row table plus the v0.4 MRR 101-200 contribution."""

    validate_enriched_ev04_metrics(original_metrics)
    validate_enriched_ev04_metrics(corrective_metrics)
    canonical_rows = legacy.produce_aggregate_comparison(original_metrics, corrective_metrics)
    require(
        [row.get("metric") for row in canonical_rows] == list(EV04_METRIC_ORDER),
        "EV04 canonical aggregate metric order changed",
    )
    original_denominator = _finite_numeric(original_metrics, "cases_evaluated", "Original EV04")
    corrective_denominator = _finite_numeric(corrective_metrics, "cases_evaluated", "Corrective EV04")
    require(
        isinstance(original_denominator, int) and isinstance(corrective_denominator, int),
        "EV04 contribution denominators must be integer case counts",
    )
    require(original_denominator == corrective_denominator, "EV04 contribution denominator mismatch")
    original_numerator = _finite_numeric(
        original_metrics, "mrr_101_200_contribution_numerator", "Original EV04",
    )
    corrective_numerator = _finite_numeric(
        corrective_metrics, "mrr_101_200_contribution_numerator", "Corrective EV04",
    )
    original_value = _finite_numeric(original_metrics, "mrr_101_200_contribution", "Original EV04")
    corrective_value = _finite_numeric(corrective_metrics, "mrr_101_200_contribution", "Corrective EV04")
    contribution_row = {
        "metric": "mrr_101_200_contribution",
        "original_numerator": original_numerator,
        "corrected_numerator": corrective_numerator,
        "denominator": original_denominator,
        "original_value": original_value,
        "corrected_value": corrective_value,
        "absolute_delta": float(corrective_value) - float(original_value),
    }
    rows = [*canonical_rows[:2], contribution_row, *canonical_rows[2:]]
    require(len(rows) == 28, "EV04 aggregate comparison must contain exactly 28 rows")
    require(
        [row.get("metric") for row in rows] == list(EV04_AGGREGATE_METRIC_ORDER),
        "EV04 aggregate comparison omitted or reordered a reportable metric",
    )
    return rows


def compare_canonical_metrics_v04(expected: Mapping[str, Any], actual: Mapping[str, Any]) -> None:
    """Fail closed on any key, type, order, or value difference."""

    validate_enriched_ev04_metrics(expected)
    validate_enriched_ev04_metrics(actual)
    require(list(expected) == list(actual), "EV04 canonical metric key order changed")
    for key in expected:
        require(type(actual[key]) is type(expected[key]), f"EV04 metric type changed: {key}")
        require(actual[key] == expected[key], f"EV04 metric value changed: {key}")


def compare_ev04_control_v04(
    expected_case_rows: Sequence[Mapping[str, Any]],
    actual_case_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Construct both metric dictionaries independently before comparison."""

    expected = build_ev04_enriched_metrics(expected_case_rows)
    actual = build_ev04_enriched_metrics(actual_case_rows)
    compare_canonical_metrics_v04(expected, actual)
    return {"status": "PASS", "expected_metrics": expected, "actual_metrics": actual}


def compare_complete_ev04_control_v04(
    expected_ranking: Path,
    actual_ranking: Path,
    expected_summary: Path,
    actual_summary: Path,
) -> dict[str, Any]:
    """Apply exact file controls plus independent canonical metric derivation."""

    expected_rows = legacy.flat._read_csv(expected_summary)
    actual_rows = legacy.flat._read_csv(actual_summary)
    canonical = compare_ev04_control_v04(expected_rows, actual_rows)
    files = legacy.compare_control_reproduction(
        expected_ranking,
        actual_ranking,
        expected_summary,
        actual_summary,
        canonical["expected_metrics"],
        canonical["actual_metrics"],
        expected_candidate_schema=EV04_CANDIDATE_FIELDS,
        expected_case_schema=EV04_CASE_FIELDS,
    )
    return {**files, **canonical, "status": "PASS_EXACT"}


def evaluate_arm(
    arm: str,
    corpus_path: Path,
    index_path: Path,
    metadata_path: Path,
    output_dir: Path,
    *,
    evalset: Path = EVALSET,
    config_path: Path = CONFIG,
    root: Path = ROOT,
) -> dict[str, Any]:
    require(not output_dir.exists(), f"Corrective evaluator refuses overwrite or resume: {legacy._relative(output_dir, root)}")
    inputs = legacy.validate_dynamic_inputs(arm, corpus_path, index_path, metadata_path, config_path=config_path)
    evalset = (root / evalset).resolve() if not evalset.is_absolute() else evalset.resolve()
    require(evalset.is_file(), f"Frozen EVAL is missing: {legacy._relative(evalset, root)}")
    depth = 100 if arm == "EV03" else 200
    if arm == "EV03":
        cases, candidates, metrics = legacy._flat_rows(evalset, corpus_path, inputs["index"], depth)
        prefix, case_fields, candidate_fields = "normative_flat", EV03_CASE_FIELDS, EV03_CANDIDATE_FIELDS
    else:
        cases, candidates, base_metrics = legacy._hierarchical_rows(evalset, corpus_path, inputs["index"], depth)
        metrics = build_ev04_enriched_metrics(cases, base_metrics, require_real_case_count=True)
        prefix, case_fields, candidate_fields = "normative_hierarchical", EV04_CASE_FIELDS, EV04_CANDIDATE_FIELDS
    output_dir.mkdir(parents=True, exist_ok=False)
    ranking = output_dir / f"{prefix}_results.csv"
    summary = output_dir / f"{prefix}_case_summary.csv"
    metric_file = output_dir / f"{prefix}_metrics.json"
    legacy._write_csv_new(ranking, legacy._normalize_rows(candidates), candidate_fields)
    legacy._write_csv_new(summary, legacy._normalize_rows(cases), case_fields)
    payload = {
        "arm": arm,
        "dynamic_inputs": {key: value for key, value in inputs.items() if key not in {"metadata", "index"}},
        "evalset": legacy._relative(evalset, root),
        "evalset_sha256": sha256_file(evalset),
        "retrieval_depth": depth,
        "metric_contract": "EV04_CANONICAL_MRR_V0.4" if arm == "EV04" else "EV03_FROZEN_V0.2",
        "metrics": metrics,
        "outputs": {"ranking": legacy._relative(ranking, root), "case_summary": legacy._relative(summary, root)},
    }
    legacy._write_json_new(metric_file, payload, root=root)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arm", choices=("EV03", "EV04"), required=True)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--index-metadata", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    print(json.dumps(evaluate_arm(args.arm, args.corpus, args.index, args.index_metadata, args.output_dir), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
