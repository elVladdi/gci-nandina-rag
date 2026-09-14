"""Non-governing forensic accounting for the EXP12 planning failure.

The production interface is locked to the historical seed and frozen v0.5
parameters. The module performs no work unless its explicit diagnostic flag is
provided. It never selects EXP12 conditions or runs retrieval/evaluation.
"""

from __future__ import annotations

import argparse
import json
import sys
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping, Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.experiments.plan_exp12_historical_diversity_v01 import (
    CANDIDATE_COUNT,
    DEFAULT_CONFIG,
    DEFAULT_EVAL,
    DEFAULT_H100,
    DEFAULT_SAMPLING_UNIVERSE,
    EXPECTED_EVAL_SHA256,
    EXPECTED_H100_SHA256,
    EXPECTED_POOL_SHA256,
    MAXIMUM_TVD,
    MAX_ROWS,
    MINIMUM_UNIQUE_FEASIBLE,
    MIN_ROWS,
    ROOT,
    TARGET_ROWS,
    ContractViolation,
    _assert_path,
    _candidate_label_counts,
    _nearest_prefix,
    _portable_text_sha256,
    _prefixes,
    dam_concentration_metrics,
    total_variation_distance_full_support,
    validate_exp12_v05_contract,
    validate_source_identities,
)


FORENSIC_SEED = 20262001
FORENSIC_CANDIDATE_COUNT = CANDIDATE_COUNT
FORENSIC_OUTPUT = Path(
    "outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/"
    "exp12_feasibility_failure_diagnostic_v0.1.json"
)
EXPECTED_CONFIG_SHA256 = "1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264"
EXPECTED_RUNNER_PATH = Path("src/experiments/plan_exp12_historical_diversity_v01.py")
EXPECTED_RUNNER_SHA256 = "cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac"


def validate_forensic_request(
    *,
    seed: int = FORENSIC_SEED,
    candidate_count: int = FORENSIC_CANDIDATE_COUNT,
    target_rows: int = TARGET_ROWS,
    minimum_rows: int = MIN_ROWS,
    maximum_rows: int = MAX_ROWS,
    required_label_coverage_fraction: float = 1.0,
    maximum_tvd: float = MAXIMUM_TVD,
) -> None:
    """Reject any production request that departs from the frozen scope."""
    expected = {
        "seed": (seed, FORENSIC_SEED),
        "candidate_count": (candidate_count, FORENSIC_CANDIDATE_COUNT),
        "target_rows": (target_rows, TARGET_ROWS),
        "minimum_rows": (minimum_rows, MIN_ROWS),
        "maximum_rows": (maximum_rows, MAX_ROWS),
        "required_label_coverage_fraction": (required_label_coverage_fraction, 1.0),
        "maximum_tvd": (maximum_tvd, MAXIMUM_TVD),
    }
    for field, (observed, frozen) in expected.items():
        if observed != frozen:
            raise ContractViolation(f"Forensic {field} must equal {frozen!r}; observed {observed!r}")


def _classify_candidate(
    dam_ids: tuple[str, ...],
    dam_rows: Mapping[str, int],
    dam_label_counts: Mapping[str, Mapping[str, int]],
    reference_label_counts: Mapping[str, int],
) -> tuple[str, bool | None, bool | None]:
    """Classify one unique non-overlap candidate under frozen constraints."""
    rows = int(dam_concentration_metrics(dam_rows, dam_ids)["rows"])
    if rows < MIN_ROWS:
        return "below", None, None
    if rows > MAX_ROWS:
        return "above", None, None
    label_counts = _candidate_label_counts(dam_label_counts, dam_ids)
    coverage = sum(label_counts.get(code, 0) > 0 for code in reference_label_counts) / len(
        reference_label_counts
    )
    tvd = total_variation_distance_full_support(label_counts, rows, reference_label_counts)
    return "within", coverage == 1.0, tvd <= MAXIMUM_TVD


def _assert_accounting(result: Mapping[str, Any]) -> None:
    if result["candidate_indices_attempted"] != (
        result["duplicate_dam_set_rejections"]
        + result["eval_overlap_rejections"]
        + result["unique_nonoverlap_candidates"]
    ):
        raise ContractViolation("Candidate-index accounting invariant failed")
    if result["unique_nonoverlap_candidates"] != (
        result["volume_below_min_count"]
        + result["volume_within_range_count"]
        + result["volume_above_max_count"]
    ):
        raise ContractViolation("Volume accounting invariant failed")
    if result["volume_within_range_count"] != (
        result["coverage_and_tvd_pass_count"]
        + result["coverage_pass_tvd_fail_count"]
        + result["coverage_fail_tvd_pass_count"]
        + result["coverage_and_tvd_fail_count"]
    ):
        raise ContractViolation("Coverage-by-TVD accounting invariant failed")
    if result["volume_within_range_count"] != (
        result["coverage_pass_count_among_volume_pass"]
        + result["coverage_fail_count_among_volume_pass"]
    ):
        raise ContractViolation("Coverage marginal accounting invariant failed")
    if result["volume_within_range_count"] != (
        result["tvd_pass_count_among_volume_pass"]
        + result["tvd_fail_count_among_volume_pass"]
    ):
        raise ContractViolation("TVD marginal accounting invariant failed")
    if result["final_unique_feasible_count"] != result["coverage_and_tvd_pass_count"]:
        raise ContractViolation("Final feasible-count accounting invariant failed")


def _diagnose_profiles(
    dam_rows: Mapping[str, int],
    dam_label_counts: Mapping[str, Mapping[str, int]],
    reference_label_counts: Mapping[str, int],
    eval_dams: set[str],
    *,
    seed: int,
    candidate_count: int,
) -> dict[str, Any]:
    """Instrument frozen generation using in-memory profiles.

    ``candidate_count`` is injectable only so synthetic tests can stay small;
    the production entry point validates and supplies exactly 10,000.
    """
    if candidate_count <= 0:
        raise ContractViolation("candidate_count must be positive")
    if set(dam_rows) != set(dam_label_counts):
        raise ContractViolation("Each DAM needs exactly one row and label-count profile")
    if any(not dam or rows <= 0 for dam, rows in dam_rows.items()):
        raise ContractViolation("DAM identifiers and row counts must be positive")
    if not reference_label_counts:
        raise ContractViolation("Reference label counts must not be empty")

    result: dict[str, Any] = {
        "candidate_indices_attempted": candidate_count,
        "duplicate_dam_set_rejections": 0,
        "eval_overlap_rejections": 0,
        "unique_nonoverlap_candidates": 0,
        "volume_below_min_count": 0,
        "volume_within_range_count": 0,
        "volume_above_max_count": 0,
        "coverage_pass_count_among_volume_pass": 0,
        "coverage_fail_count_among_volume_pass": 0,
        "tvd_pass_count_among_volume_pass": 0,
        "tvd_fail_count_among_volume_pass": 0,
        "coverage_and_tvd_pass_count": 0,
        "coverage_pass_tvd_fail_count": 0,
        "coverage_fail_tvd_pass_count": 0,
        "coverage_and_tvd_fail_count": 0,
        "final_unique_feasible_count": 0,
        "minimum_required_unique_feasible": MINIMUM_UNIQUE_FEASIBLE,
    }
    seen: set[tuple[str, ...]] = set()
    for candidate_index in range(candidate_count):
        order = tuple(
            sorted(
                dam_rows,
                key=lambda dam: (
                    sha256(f"{seed}:{candidate_index}:{dam}".encode("utf-8")).hexdigest(),
                    dam,
                ),
            )
        )
        selected = _nearest_prefix(_prefixes(order, dam_rows))
        canonical_ids = tuple(sorted(selected))
        if canonical_ids in seen:
            result["duplicate_dam_set_rejections"] += 1
            continue
        if set(canonical_ids) & eval_dams:
            result["eval_overlap_rejections"] += 1
            continue
        seen.add(canonical_ids)
        result["unique_nonoverlap_candidates"] += 1

        volume, coverage_pass, tvd_pass = _classify_candidate(
            canonical_ids, dam_rows, dam_label_counts, reference_label_counts
        )
        if volume == "below":
            result["volume_below_min_count"] += 1
            continue
        if volume == "above":
            result["volume_above_max_count"] += 1
            continue
        result["volume_within_range_count"] += 1
        result[
            "coverage_pass_count_among_volume_pass"
            if coverage_pass
            else "coverage_fail_count_among_volume_pass"
        ] += 1
        result[
            "tvd_pass_count_among_volume_pass"
            if tvd_pass
            else "tvd_fail_count_among_volume_pass"
        ] += 1
        if coverage_pass and tvd_pass:
            result["coverage_and_tvd_pass_count"] += 1
        elif coverage_pass:
            result["coverage_pass_tvd_fail_count"] += 1
        elif tvd_pass:
            result["coverage_fail_tvd_pass_count"] += 1
        else:
            result["coverage_and_tvd_fail_count"] += 1

    result["final_unique_feasible_count"] = result["coverage_and_tvd_pass_count"]
    result["historical_failure_condition_reproduced"] = (
        result["final_unique_feasible_count"] < MINIMUM_UNIQUE_FEASIBLE
    )
    _assert_accounting(result)
    return result


def run_forensic_diagnostic(
    config_path: Path,
    sampling_universe: Path,
    h100: Path,
    eval_path: Path,
    output_path: Path,
    *,
    seed: int = FORENSIC_SEED,
    candidate_count: int = FORENSIC_CANDIDATE_COUNT,
    target_rows: int = TARGET_ROWS,
    minimum_rows: int = MIN_ROWS,
    maximum_rows: int = MAX_ROWS,
    required_label_coverage_fraction: float = 1.0,
    maximum_tvd: float = MAXIMUM_TVD,
) -> dict[str, Any]:
    """Run the separately authorized aggregate-only forensic diagnostic."""
    validate_forensic_request(
        seed=seed,
        candidate_count=candidate_count,
        target_rows=target_rows,
        minimum_rows=minimum_rows,
        maximum_rows=maximum_rows,
        required_label_coverage_fraction=required_label_coverage_fraction,
        maximum_tvd=maximum_tvd,
    )
    config_resolved = _assert_path(config_path, DEFAULT_CONFIG.as_posix(), "config")
    if _portable_text_sha256(config_resolved) != EXPECTED_CONFIG_SHA256:
        raise ContractViolation("config SHA-256 does not match the frozen forensic binding")
    runner_path = ROOT / EXPECTED_RUNNER_PATH
    if _portable_text_sha256(runner_path) != EXPECTED_RUNNER_SHA256:
        raise ContractViolation("runner SHA-256 does not match the frozen forensic binding")
    config = json.loads(config_resolved.read_text(encoding="utf-8"))
    validate_exp12_v05_contract(config)
    dam_rows, dam_labels, reference_labels, eval_dams = validate_source_identities(
        config, sampling_universe, h100, eval_path
    )
    expected_output = (ROOT / FORENSIC_OUTPUT).resolve()
    if output_path.resolve() != expected_output:
        raise ContractViolation(f"output must resolve to {expected_output}")
    if output_path.exists():
        raise ContractViolation("forensic output must not already exist")

    accounting = _diagnose_profiles(
        dam_rows,
        dam_labels,
        reference_labels,
        eval_dams,
        seed=seed,
        candidate_count=candidate_count,
    )
    payload = {
        "artifact": "EXP12_FEASIBILITY_FAILURE_DIAGNOSTIC",
        "version": "v0.1",
        "status": "NON_GOVERNING_FORENSIC_RESULT",
        "scientific_base_commit": "428dfecca5cff313f910032a28a8a3c7ae13c2ef",
        "historical_attempt": "EXP12_PLANNING_ATTEMPT_001",
        "forensic_non_governing": True,
        "seed": seed,
        "candidate_count": candidate_count,
        "bindings": {
            "config": DEFAULT_CONFIG.as_posix(),
            "config_sha256": EXPECTED_CONFIG_SHA256,
            "runner": EXPECTED_RUNNER_PATH.as_posix(),
            "runner_sha256": EXPECTED_RUNNER_SHA256,
            "sampling_universe": DEFAULT_SAMPLING_UNIVERSE.as_posix(),
            "sampling_universe_sha256": EXPECTED_POOL_SHA256,
            "h100": DEFAULT_H100.as_posix(),
            "h100_sha256": EXPECTED_H100_SHA256,
            "eval": DEFAULT_EVAL.as_posix(),
            "eval_sha256": EXPECTED_EVAL_SHA256,
            "eval_usage": "DECLARACION_OVERLAP_ONLY",
        },
        "accounting": accounting,
        "condition_selection_performed": False,
        "retrieval_executed": False,
        "bm25_executed": False,
        "top_k_computed": False,
        "mrr_computed": False,
    }
    output_path.parent.mkdir(parents=True, exist_ok=False)
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--sampling-universe", type=Path, default=DEFAULT_SAMPLING_UNIVERSE)
    parser.add_argument("--h100", type=Path, default=DEFAULT_H100)
    parser.add_argument("--eval", dest="eval_path", type=Path, default=DEFAULT_EVAL)
    parser.add_argument("--output", type=Path, default=FORENSIC_OUTPUT)
    parser.add_argument("--seed", type=int, default=FORENSIC_SEED)
    parser.add_argument("--candidate-count", type=int, default=FORENSIC_CANDIDATE_COUNT)
    parser.add_argument("--target-rows", type=int, default=TARGET_ROWS)
    parser.add_argument("--minimum-rows", type=int, default=MIN_ROWS)
    parser.add_argument("--maximum-rows", type=int, default=MAX_ROWS)
    parser.add_argument("--required-label-coverage-fraction", type=float, default=1.0)
    parser.add_argument("--maximum-tvd", type=float, default=MAXIMUM_TVD)
    parser.add_argument("--execute-forensic-diagnostic", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.execute_forensic_diagnostic:
        print(json.dumps({"status": "NOT_EXECUTED", "reason": "--execute-forensic-diagnostic is required"}))
        return 2
    run_forensic_diagnostic(
        args.config,
        args.sampling_universe,
        args.h100,
        args.eval_path,
        args.output,
        seed=args.seed,
        candidate_count=args.candidate_count,
        target_rows=args.target_rows,
        minimum_rows=args.minimum_rows,
        maximum_rows=args.maximum_rows,
        required_label_coverage_fraction=args.required_label_coverage_fraction,
        maximum_tvd=args.maximum_tvd,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
