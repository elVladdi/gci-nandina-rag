"""v0.3 corrective evaluator with case-derived enriched EV04 MRR metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from . import evaluate_normative_bm25_corrective_0b05c_v01 as legacy
from . import evaluate_normative_bm25_hierarchical_data_aduanas_v02 as hierarchical
from .prepare_0b05c_corrective_numerical_gate_v03 import MRR_DEFINITION, ROOT, require


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
ContractViolation = legacy.ContractViolation

EV04_METRIC_ORDER = (
    "mrr_at_100",
    "mrr_at_200",
    *(f"top_{k}" for k in hierarchical.K_VALUES),
    *(f"recall_at_{k}" for k in hierarchical.RECALL_K_VALUES),
    "pool_recall_at_200",
    *(f"{name}_at_{k}" for k in hierarchical.HIERARCHICAL_K_VALUES for name in ("exact", "hs6", "hs4", "chapter")),
)
METRIC_ROW_FIELDS = ("metric", "numerator", "denominator", "value")


def _rank(row: Mapping[str, Any]) -> int:
    try:
        return int(row.get("rank_ref", 0))
    except (TypeError, ValueError) as exc:
        raise ContractViolation("EV04 rank_ref is not an integer") from exc


def build_ev04_enriched_metrics(
    case_rows: Sequence[Mapping[str, Any]],
    base_metrics: Mapping[str, Any] | None = None,
    *,
    require_real_case_count: bool = False,
) -> dict[str, Any]:
    """Build the frozen enriched MRR schema strictly from reproduced cases."""

    denominator = len(case_rows)
    require(denominator > 0, "EV04 metrics require at least one case row")
    if require_real_case_count:
        require(denominator == 1056, "EV04 real execution requires exactly 1056 cases")
    base = dict(base_metrics or hierarchical.metrics_from_cases(case_rows))
    table = base.get("metric_table")
    require(isinstance(table, list) and table, "EV04 base metric_table is missing")
    require(table[0].get("metric") == "mrr", "EV04 legacy metric_table prefix changed")
    ranks = [_rank(row) for row in case_rows]
    numerator_100 = sum(1.0 / rank for rank in ranks if 1 <= rank <= 100)
    numerator_200 = sum(1.0 / rank for rank in ranks if 1 <= rank <= 200)
    mrr_100 = numerator_100 / denominator
    mrr_200 = numerator_200 / denominator
    contribution_numerator = numerator_200 - numerator_100
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
        "mrr_101_200_contribution_numerator": contribution_numerator,
        "mrr_101_200_contribution": contribution_numerator / denominator,
        "metric_table": [
            hierarchical.metric_row("mrr_at_100", numerator_100, denominator),
            hierarchical.metric_row("mrr_at_200", numerator_200, denominator),
            *[dict(row) for row in table[1:]],
        ],
    })
    validate_enriched_ev04_metrics(out)
    return out


def validate_enriched_ev04_metrics(metrics: Mapping[str, Any]) -> None:
    table = metrics.get("metric_table")
    require(isinstance(table, list), "EV04 enriched metric_table is missing")
    require([row.get("metric") for row in table] == list(EV04_METRIC_ORDER), "EV04 enriched metric_table names or order changed")
    for row in table:
        require(tuple(row) == METRIC_ROW_FIELDS, f"EV04 enriched metric row schema changed: {row.get('metric')}")
    denominator = metrics.get("cases_evaluated")
    require(metrics.get("mrr_at_100_denominator") == denominator, "EV04 MRR@100 denominator drift")
    require(metrics.get("mrr_at_200_denominator") == denominator, "EV04 MRR@200 denominator drift")
    require(metrics.get("mrr_denominator") == denominator, "EV04 legacy MRR denominator drift")
    require(metrics.get("mrr") == metrics.get("mrr_at_200"), "EV04 legacy mrr must equal MRR@200")
    require(metrics.get("mrr_numerator") == metrics.get("mrr_at_200_numerator"), "EV04 legacy MRR numerator drift")
    require(metrics.get("mrr_definition") == MRR_DEFINITION, "EV04 MRR definition drift")
    expected_contribution = metrics.get("mrr_at_200_numerator") - metrics.get("mrr_at_100_numerator")
    require(metrics.get("mrr_101_200_contribution_numerator") == expected_contribution, "EV04 MRR 101-200 contribution numerator drift")
    require(metrics.get("mrr_101_200_contribution") == expected_contribution / denominator, "EV04 MRR 101-200 contribution drift")


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
        "metric_contract": "EV04_ENRICHED_MRR_V0.3" if arm == "EV04" else "EV03_FROZEN_V0.2",
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
