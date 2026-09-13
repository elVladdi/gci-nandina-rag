"""Source-bound, fail-closed planning primitives for EXP-12 v0.5.

This module plans complete-DAM historical banks only. It contains no retrieval,
ranking, evaluation-label, Top-k, or MRR logic, and its CLI does nothing unless
``--execute-planning`` is supplied explicitly.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = Path("src/configs/exp12_historical_diversity_control_v0.5.json")
DEFAULT_SAMPLING_UNIVERSE = Path("data/interim/new_historical_gate_v0.2/new_historical_eligible.csv")
DEFAULT_H100 = Path("data/processed/data_aduanas_historico_clase87_v0.2.csv")
DEFAULT_EVAL = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")

EXPECTED_CONTRACT_STATUS = "PREPLANNING_COMPATIBILITY_CORRECTED_PENDING_EXTERNAL_AUDIT"
EXPECTED_METHOD_CONTRACT = "FROZEN_METHOD_SOURCE_BOUND_TVD_FULL_SUPPORT_PENDING_EXTERNAL_AUDIT"
EXPECTED_POOL_SHA256 = "f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457"
EXPECTED_H100_SHA256 = "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff"
EXPECTED_EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
EXPECTED_SEEDS = tuple(range(20262001, 20262011))
EXPECTED_QUANTILES = {"D-HIGH": 0.1, "D-MID": 0.5, "D-LOW": 0.9}
EXPECTED_REPORTS = {
    "HHI_q10",
    "HHI_q50",
    "HHI_q90",
    "HHI_span_q90_q10",
    "effective_DAM_q10",
    "effective_DAM_q50",
    "effective_DAM_q90",
    "effective_DAM_ratio_high_low",
}
TARGET_ROWS = 2950
MIN_ROWS = 2802
MAX_ROWS = 3098
CANDIDATE_COUNT = 10000
MINIMUM_UNIQUE_FEASIBLE = 30
MAXIMUM_TVD = 0.05


class ContractViolation(ValueError):
    """Raised when the frozen EXP-12 planning contract is not satisfied."""


@dataclass(frozen=True)
class Exp12Candidate:
    candidate_index: int
    dam_ids: tuple[str, ...]
    rows: int
    hhi: float
    effective_dam: float
    dominant_dam_share: float
    top2_dam_share: float
    label_coverage_fraction: float
    tvd: float


def _require(mapping: Mapping[str, Any], key: str) -> Any:
    if key not in mapping:
        raise ContractViolation(f"Missing required contract field: {key}")
    return mapping[key]


def _expect(actual: Any, expected: Any, field: str) -> None:
    if actual != expected:
        raise ContractViolation(f"{field} must equal {expected!r}; observed {actual!r}")


def validate_exp12_v05_contract(config: Mapping[str, Any]) -> None:
    """Validate the source-bound v0.5 contract without reading data or planning."""
    _expect(_require(config, "experiment_id"), "exp12_historical_diversity_control_v0.5", "experiment_id")
    _expect(_require(config, "version"), "v0.5", "version")
    _expect(_require(config, "contract_status"), EXPECTED_CONTRACT_STATUS, "contract_status")
    _expect(_require(config, "method_contract"), EXPECTED_METHOD_CONTRACT, "method_contract")
    _expect(_require(config, "execution_authorized"), False, "execution_authorized")

    fixed_eval = _require(config, "fixed_eval")
    _expect(fixed_eval.get("path"), DEFAULT_EVAL.as_posix(), "fixed_eval.path")
    _expect(fixed_eval.get("sha256"), EXPECTED_EVAL_SHA256, "fixed_eval.sha256")
    _expect(fixed_eval.get("rows"), 1056, "fixed_eval.rows")

    universe = _require(config, "sampling_universe")
    expected_universe = {
        "source": "NEW_HISTORICAL_GATE_EXTENSION_V02_APPROVED",
        "path": DEFAULT_SAMPLING_UNIVERSE.as_posix(),
        "sha256": EXPECTED_POOL_SHA256,
        "rows": 7190,
        "dam_count": 101,
        "nandina_count": 84,
        "fail_closed": True,
        "must_not_fallback_to_h100": True,
    }
    for field, expected in expected_universe.items():
        _expect(universe.get(field), expected, f"sampling_universe.{field}")

    reference = _require(config, "reference_h100")
    _expect(reference.get("path"), DEFAULT_H100.as_posix(), "reference_h100.path")
    _expect(reference.get("sha256"), EXPECTED_H100_SHA256, "reference_h100.sha256")
    _expect(reference.get("rows"), 2950, "reference_h100.rows")

    volume = _require(config, "volume_control")
    _expect(volume.get("target_rows"), TARGET_ROWS, "volume_control.target_rows")
    _expect(volume.get("max_abs_row_deviation"), 148, "volume_control.max_abs_row_deviation")
    _expect(volume.get("minimum_rows"), MIN_ROWS, "volume_control.minimum_rows")
    _expect(volume.get("maximum_rows"), MAX_ROWS, "volume_control.maximum_rows")
    _expect(volume.get("preserve_complete_dams"), True, "volume_control.preserve_complete_dams")

    replicate = _require(config, "replicate_policy")
    _expect(replicate.get("number_of_replicates_per_condition"), 10, "replicate_policy.number_of_replicates_per_condition")
    _expect(tuple(replicate.get("seed_schedule", ())), EXPECTED_SEEDS, "replicate_policy.seed_schedule")

    labels = _require(config, "label_control")
    expected_labels = {
        "reference": "H100_FROZEN_REFERENCE",
        "reference_label_set": "all NANDINA present in reference_h100",
        "reference_label_distribution": "series proportion by NANDINA in reference_h100",
        "required_label_coverage_fraction": 1.0,
        "distribution_distance": "TVD_FULL_SUPPORT_H100_PLUS_OTHER",
        "distribution_distance_formula": "0.5 * (sum_{c in H100} abs(p_c - q_c) + abs(p_OTHER - 0))",
        "nonreference_support_policy": "AGGREGATE_ALL_NON_H100_CODES_AS_OTHER_WITH_REFERENCE_MASS_ZERO",
        "candidate_probability_denominator": "ALL_CANDIDATE_ROWS",
        "reference_probability_denominator": "ALL_H100_ROWS",
        "conditional_renormalization_over_h100_only": False,
        "maximum_tvd": MAXIMUM_TVD,
    }
    for field, expected in expected_labels.items():
        _expect(labels.get(field), expected, f"label_control.{field}")

    selection = _require(config, "selection")
    _expect(selection.get("uses_eval_performance"), False, "selection.uses_eval_performance")
    _expect(selection.get("uses_eval_labels_for_selection"), False, "selection.uses_eval_labels_for_selection")
    _expect(selection.get("requires_zero_eval_dam_overlap"), True, "selection.requires_zero_eval_dam_overlap")
    _expect(selection.get("no_weighted_multiobjective"), True, "selection.no_weighted_multiobjective")

    generation = _require(config, "candidate_generation")
    _expect(generation.get("candidate_count"), CANDIDATE_COUNT, "candidate_generation.candidate_count")
    _expect(generation.get("deduplicate_by"), "sorted DAM tuple", "candidate_generation.deduplicate_by")

    feasibility = _require(config, "feasibility_filter")
    _expect(feasibility.get("minimum_unique_feasible_candidates"), MINIMUM_UNIQUE_FEASIBLE, "feasibility_filter.minimum_unique_feasible_candidates")
    _expect(feasibility.get("requires_volume_range"), [MIN_ROWS, MAX_ROWS], "feasibility_filter.requires_volume_range")
    _expect(feasibility.get("requires_label_coverage_fraction"), 1.0, "feasibility_filter.requires_label_coverage_fraction")
    _expect(feasibility.get("requires_tvd_at_most"), MAXIMUM_TVD, "feasibility_filter.requires_tvd_at_most")
    _expect(feasibility.get("requires_zero_eval_dam_overlap"), True, "feasibility_filter.requires_zero_eval_dam_overlap")
    _expect(feasibility.get("requires_complete_dams"), True, "feasibility_filter.requires_complete_dams")

    condition_selection = _require(config, "condition_selection")
    _expect(condition_selection.get("quantiles"), EXPECTED_QUANTILES, "condition_selection.quantiles")
    _expect(condition_selection.get("requires_distinct_dam_sets"), True, "condition_selection.requires_distinct_dam_sets")
    _expect(condition_selection.get("requires_strict_hhi_order"), "HHI_DLOW > HHI_DMID > HHI_DHIGH", "condition_selection.requires_strict_hhi_order")

    manipulation = _require(config, "future_manipulation_check")
    _expect(set(manipulation.get("required_reports", ())), EXPECTED_REPORTS, "future_manipulation_check.required_reports")
    _expect(manipulation.get("strict_hhi_order_fail_closed"), "HHI_DLOW > HHI_DMID > HHI_DHIGH", "future_manipulation_check.strict_hhi_order_fail_closed")
    _expect(manipulation.get("manipulation_strength_review_required"), True, "future_manipulation_check.manipulation_strength_review_required")
    _expect(manipulation.get("new_threshold_introduced"), False, "future_manipulation_check.new_threshold_introduced")
    _expect(manipulation.get("execution_gate"), "PREPLANNING_COMPATIBILITY_PACKAGE_PENDING_EXTERNAL_AUDIT", "future_manipulation_check.execution_gate")


def total_variation_distance_full_support(
    candidate_label_counts: Mapping[str, int],
    candidate_rows: int,
    reference_label_counts: Mapping[str, int],
) -> float:
    """Compute TVD over H100 reference codes plus aggregated non-H100 mass."""
    if candidate_rows <= 0:
        raise ContractViolation("candidate_rows must be positive")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in candidate_label_counts.values()):
        raise ContractViolation("Candidate label counts must be non-negative integers")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in reference_label_counts.values()):
        raise ContractViolation("Reference label counts must be non-negative integers")
    if sum(candidate_label_counts.values()) != candidate_rows:
        raise ContractViolation("candidate_rows must equal the sum of all candidate label counts")
    reference_rows = sum(reference_label_counts.values())
    if reference_rows <= 0:
        raise ContractViolation("Reference label counts must sum to a positive row count")

    reference_codes = set(reference_label_counts)
    reference_distance = sum(
        abs(candidate_label_counts.get(code, 0) / candidate_rows - count / reference_rows)
        for code, count in reference_label_counts.items()
    )
    other_count = sum(count for code, count in candidate_label_counts.items() if code not in reference_codes)
    return 0.5 * (reference_distance + abs(other_count / candidate_rows - 0.0))


def dam_concentration_metrics(dam_rows: Mapping[str, int], dam_ids: Iterable[str]) -> dict[str, float | int]:
    selected = tuple(dam_ids)
    rows = sum(dam_rows[dam] for dam in selected)
    if not selected or rows <= 0:
        raise ContractViolation("A diversity candidate needs at least one positive-row DAM")
    shares = sorted((dam_rows[dam] / rows for dam in selected), reverse=True)
    hhi = sum(share**2 for share in shares)
    return {
        "rows": rows,
        "hhi": hhi,
        "effective_dam": 1 / hhi,
        "dominant_dam_share": shares[0],
        "top2_dam_share": sum(shares[:2]),
        "dam_count": len(selected),
    }


def _dam_set_hash(dam_ids: Iterable[str]) -> str:
    return sha256("|".join(sorted(dam_ids)).encode("utf-8")).hexdigest()


def _prefixes(order: Iterable[str], dam_rows: Mapping[str, int]) -> list[tuple[int, tuple[str, ...]]]:
    rows = 0
    selected: tuple[str, ...] = tuple()
    prefixes = [(0, selected)]
    for dam in order:
        rows += dam_rows[dam]
        selected += (dam,)
        prefixes.append((rows, selected))
    return prefixes


def _nearest_prefix(prefixes: Iterable[tuple[int, tuple[str, ...]]]) -> tuple[str, ...]:
    _, selected = min(
        prefixes,
        key=lambda item: (abs(item[0] - TARGET_ROWS), len(item[1]), _dam_set_hash(item[1])),
    )
    return selected


def _candidate_label_counts(
    dam_label_counts: Mapping[str, Mapping[str, int]],
    dam_ids: Iterable[str],
) -> dict[str, int]:
    counts: dict[str, int] = {}
    for dam in dam_ids:
        for code, value in dam_label_counts[dam].items():
            counts[code] = counts.get(code, 0) + value
    return counts


def generate_exp12_candidates(
    dam_rows: Mapping[str, int],
    dam_label_counts: Mapping[str, Mapping[str, int]],
    reference_label_counts: Mapping[str, int],
    eval_dams: set[str],
    seed: int,
    candidate_count: int = CANDIDATE_COUNT,
) -> tuple[Exp12Candidate, ...]:
    """Generate complete-DAM candidates using the frozen deterministic algorithm."""
    if candidate_count <= 0:
        raise ContractViolation("candidate_count must be positive")
    if set(dam_rows) != set(dam_label_counts):
        raise ContractViolation("Each DAM needs exactly one row and label-count profile")
    if any(not dam or rows <= 0 for dam, rows in dam_rows.items()):
        raise ContractViolation("DAM identifiers and row counts must be positive")

    candidates: list[Exp12Candidate] = []
    seen: set[tuple[str, ...]] = set()
    for candidate_index in range(candidate_count):
        order = tuple(
            sorted(
                dam_rows,
                key=lambda dam: (sha256(f"{seed}:{candidate_index}:{dam}".encode("utf-8")).hexdigest(), dam),
            )
        )
        selected = _nearest_prefix(_prefixes(order, dam_rows))
        canonical_ids = tuple(sorted(selected))
        if canonical_ids in seen or set(canonical_ids) & eval_dams:
            continue
        seen.add(canonical_ids)
        concentration = dam_concentration_metrics(dam_rows, canonical_ids)
        rows = int(concentration["rows"])
        if not MIN_ROWS <= rows <= MAX_ROWS:
            continue
        label_counts = _candidate_label_counts(dam_label_counts, canonical_ids)
        coverage = sum(label_counts.get(code, 0) > 0 for code in reference_label_counts) / len(reference_label_counts)
        tvd = total_variation_distance_full_support(label_counts, rows, reference_label_counts)
        if coverage != 1.0 or tvd > MAXIMUM_TVD:
            continue
        candidates.append(
            Exp12Candidate(
                candidate_index=candidate_index,
                dam_ids=canonical_ids,
                rows=rows,
                hhi=float(concentration["hhi"]),
                effective_dam=float(concentration["effective_dam"]),
                dominant_dam_share=float(concentration["dominant_dam_share"]),
                top2_dam_share=float(concentration["top2_dam_share"]),
                label_coverage_fraction=coverage,
                tvd=tvd,
            )
        )
    return tuple(candidates)


def select_exp12_conditions(candidates: Iterable[Exp12Candidate], seed: int) -> dict[str, Exp12Candidate]:
    """Select the frozen HHI quantiles from a feasible candidate collection."""
    pool = tuple(candidates)
    if len(pool) < MINIMUM_UNIQUE_FEASIBLE:
        raise ContractViolation("EXP-12 requires at least 30 unique feasible candidates")
    selected: dict[str, Exp12Candidate] = {}
    for condition, quantile in EXPECTED_QUANTILES.items():
        ordered = sorted(
            pool,
            key=lambda candidate: (
                candidate.hhi,
                sha256(f"{seed}:{condition}:{'|'.join(candidate.dam_ids)}".encode("utf-8")).hexdigest(),
            ),
        )
        selected[condition] = ordered[int(quantile * (len(ordered) - 1))]
    if len({candidate.dam_ids for candidate in selected.values()}) != 3:
        raise ContractViolation("EXP-12 conditions must use distinct DAM sets")
    if not selected["D-LOW"].hhi > selected["D-MID"].hhi > selected["D-HIGH"].hhi:
        raise ContractViolation("EXP-12 requires strict HHI_DLOW > HHI_DMID > HHI_DHIGH")
    return selected


def _portable_text_sha256(path: Path) -> str:
    content = path.read_bytes()
    raw = sha256(content).hexdigest()
    normalized = sha256(content.replace(b"\r\n", b"\n")).hexdigest()
    return raw if raw == normalized else normalized


def _load_profiles(path: Path) -> tuple[dict[str, int], dict[str, dict[str, int]], dict[str, int]]:
    dam_rows: dict[str, int] = {}
    dam_labels: dict[str, dict[str, int]] = {}
    label_counts: dict[str, int] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            dam = row["DECLARACION"].strip()
            code = row["NANDINA"].strip()
            if not dam or not code:
                raise ContractViolation(f"{path} contains an empty DAM or NANDINA")
            dam_rows[dam] = dam_rows.get(dam, 0) + 1
            per_dam = dam_labels.setdefault(dam, {})
            per_dam[code] = per_dam.get(code, 0) + 1
            label_counts[code] = label_counts.get(code, 0) + 1
    return dam_rows, dam_labels, label_counts


def _load_eval_dams_only(path: Path) -> tuple[set[str], int]:
    dams: set[str] = set()
    rows = 0
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        dam_index = header.index("DECLARACION")
        for row in reader:
            rows += 1
            dams.add(row[dam_index].strip())
    return dams, rows


def _assert_path(provided: Path, expected_relative: str, field: str) -> Path:
    resolved = provided.resolve()
    expected = (ROOT / expected_relative).resolve()
    if resolved != expected:
        raise ContractViolation(f"{field} must resolve to {expected}")
    return resolved


def validate_source_identities(
    config: Mapping[str, Any],
    sampling_universe: Path,
    h100: Path,
    eval_path: Path,
) -> tuple[dict[str, int], dict[str, dict[str, int]], dict[str, int], set[str]]:
    """Validate frozen source identities and read EVAL only for DAM overlap."""
    universe = _require(config, "sampling_universe")
    reference = _require(config, "reference_h100")
    fixed_eval = _require(config, "fixed_eval")
    pool_path = _assert_path(sampling_universe, universe["path"], "sampling_universe")
    h100_path = _assert_path(h100, reference["path"], "h100")
    eval_resolved = _assert_path(eval_path, fixed_eval["path"], "eval")
    for path, expected, label in (
        (pool_path, universe["sha256"], "sampling_universe"),
        (h100_path, reference["sha256"], "h100"),
        (eval_resolved, fixed_eval["sha256"], "eval"),
    ):
        if _portable_text_sha256(path) != expected:
            raise ContractViolation(f"{label} SHA-256 does not match the frozen contract")

    dam_rows, dam_labels, pool_labels = _load_profiles(pool_path)
    h100_rows, _, reference_labels = _load_profiles(h100_path)
    eval_dams, eval_rows = _load_eval_dams_only(eval_resolved)
    _expect(sum(dam_rows.values()), universe["rows"], "sampling_universe.rows")
    _expect(len(dam_rows), universe["dam_count"], "sampling_universe.dam_count")
    _expect(len(pool_labels), universe["nandina_count"], "sampling_universe.nandina_count")
    _expect(sum(h100_rows.values()), reference["rows"], "reference_h100.rows")
    _expect(eval_rows, fixed_eval["rows"], "fixed_eval.rows")
    if set(dam_rows) & eval_dams:
        raise ContractViolation("Sampling universe and EVAL DAM identifiers must not overlap")
    return dam_rows, dam_labels, reference_labels, eval_dams


def _quantile_candidate(candidates: Sequence[Exp12Candidate], quantile: float) -> Exp12Candidate:
    ordered = sorted(candidates, key=lambda candidate: (candidate.hhi, candidate.dam_ids))
    return ordered[int(quantile * (len(ordered) - 1))]


def manipulation_descriptors(candidates: Sequence[Exp12Candidate]) -> dict[str, float]:
    if len(candidates) < MINIMUM_UNIQUE_FEASIBLE:
        raise ContractViolation("Manipulation descriptors require at least 30 feasible candidates")
    q10 = _quantile_candidate(candidates, 0.1)
    q50 = _quantile_candidate(candidates, 0.5)
    q90 = _quantile_candidate(candidates, 0.9)
    return {
        "HHI_q10": q10.hhi,
        "HHI_q50": q50.hhi,
        "HHI_q90": q90.hhi,
        "HHI_span_q90_q10": q90.hhi - q10.hhi,
        "effective_DAM_q10": q10.effective_dam,
        "effective_DAM_q50": q50.effective_dam,
        "effective_DAM_q90": q90.effective_dam,
        "effective_DAM_ratio_high_low": q90.effective_dam / q10.effective_dam,
    }


def execute_planning(
    config_path: Path,
    sampling_universe: Path,
    h100: Path,
    eval_path: Path,
    output_dir: Path,
) -> dict[str, Any]:
    """Run the explicitly requested planning-only workflow and write one summary."""
    config_resolved = _assert_path(config_path, DEFAULT_CONFIG.as_posix(), "config")
    config = json.loads(config_resolved.read_text(encoding="utf-8"))
    validate_exp12_v05_contract(config)
    dam_rows, dam_labels, reference_labels, eval_dams = validate_source_identities(
        config, sampling_universe, h100, eval_path
    )
    if output_dir.exists():
        raise ContractViolation("output_dir must not already exist")

    runs: list[dict[str, Any]] = []
    for seed in EXPECTED_SEEDS:
        candidates = generate_exp12_candidates(
            dam_rows, dam_labels, reference_labels, eval_dams, seed, CANDIDATE_COUNT
        )
        if len(candidates) < MINIMUM_UNIQUE_FEASIBLE:
            raise ContractViolation(f"Seed {seed} produced fewer than 30 unique feasible candidates")
        selected = select_exp12_conditions(candidates, seed)
        runs.append(
            {
                "seed": seed,
                "candidate_count_attempted": CANDIDATE_COUNT,
                "unique_feasible_candidate_count": len(candidates),
                "selected": {condition: asdict(candidate) for condition, candidate in selected.items()},
                "manipulation_descriptors": manipulation_descriptors(candidates),
            }
        )

    triplets = [tuple(tuple(run["selected"][condition]["dam_ids"]) for condition in EXPECTED_QUANTILES) for run in runs]
    summary = {
        "artifact": "EXP12_PLANNING_ONLY",
        "config": DEFAULT_CONFIG.as_posix(),
        "sampling_universe": DEFAULT_SAMPLING_UNIVERSE.as_posix(),
        "h100_reference": DEFAULT_H100.as_posix(),
        "eval_usage": "DECLARACION_OVERLAP_ONLY",
        "tvd_semantics": "FULL_REFERENCE_SUPPORT_PLUS_OTHER",
        "runs": runs,
        "duplicate_triplet_structure": len(triplets) != len(set(triplets)),
        "retrieval_executed": False,
        "bm25_executed": False,
        "top_k_computed": False,
        "mrr_computed": False,
    }
    output_dir.mkdir(parents=True)
    (output_dir / "exp12_planning_summary_v0.1.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--sampling-universe", type=Path, default=DEFAULT_SAMPLING_UNIVERSE)
    parser.add_argument("--h100", type=Path, default=DEFAULT_H100)
    parser.add_argument("--eval", dest="eval_path", type=Path, default=DEFAULT_EVAL)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--execute-planning", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.execute_planning:
        print(json.dumps({"status": "NOT_EXECUTED", "reason": "--execute-planning is required"}))
        return 2
    if args.output_dir is None:
        raise ContractViolation("--output-dir is required with --execute-planning")
    execute_planning(args.config, args.sampling_universe, args.h100, args.eval_path, args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
