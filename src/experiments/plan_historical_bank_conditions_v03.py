"""Deterministic, pre-retrieval planning contracts for EXP-11 and EXP-12.

The module intentionally contains no retrieval, ranking, Top-k, MRR, or eval-label
logic. EXP-11 planning operates on complete DAM row counts. EXP-12 planning is
limited to synthetic or separately approved expanded-bank catalogues.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable, Mapping


EXPANDED_HISTORICAL_GATE = "PENDING_NEW_HISTORICAL_GATE"
H100_ROWS = 2950
EXP11_TARGET_ROWS = {"H25": 738, "H50": 1475, "H75": 2213, "H100": 2950}
EXP11_MAX_ABS_ROW_DEVIATION = 148
EXP11_SUBSAMPLE_CONDITIONS = ("H25", "H50", "H75")
EXP11_REQUIRED_DOMINANT_COUNTS = {"H25": 0, "H50": 1, "H75": 2}
EXP11_H50_STRATA = ("D1", "D2")
EXP12_TARGET_ROWS = 2950
EXP12_MAX_ABS_ROW_DEVIATION = 148
EXP12_MIN_ROWS = 2802
EXP12_MAX_ROWS = 3098
EXP12_CANDIDATE_COUNT = 10000
EXP12_MINIMUM_UNIQUE_FEASIBLE = 30
EXP12_MAX_TVD = 0.05
FORBIDDEN_SELECTION_TERMS = ("top-k", "top_k", "top1", "top_1", "top3", "top_3", "mrr")


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
        raise ValueError(f"Missing required contract field: {key}")
    return mapping[key]


def _selection_is_eval_independent(selection: Mapping[str, Any]) -> bool:
    text = " ".join(str(value).lower() for value in selection.values())
    return not any(term in text for term in FORBIDDEN_SELECTION_TERMS)


def _dam_set_hash(dam_ids: Iterable[str]) -> str:
    return sha256("|".join(sorted(dam_ids)).encode("utf-8")).hexdigest()


def _chain_key(plan: Mapping[str, tuple[str, ...]]) -> str:
    payload = {condition: sorted(plan[condition]) for condition in ("H25", "H50", "H75")}
    return sha256(json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stable_dam_order(dam_rows: Mapping[str, int], seed: int) -> tuple[str, ...]:
    """Return a deterministic DAM-only order without consulting evaluation data."""
    if not dam_rows:
        raise ValueError("DAM catalogue cannot be empty")
    if any(not dam or rows <= 0 for dam, rows in dam_rows.items()):
        raise ValueError("DAM identifiers must be non-empty and row counts positive")
    return tuple(sorted(dam_rows, key=lambda dam: (sha256(f"{seed}:{dam}".encode("utf-8")).hexdigest(), dam)))


def _prefixes(order: Iterable[str], dam_rows: Mapping[str, int]) -> list[tuple[int, tuple[str, ...]]]:
    rows = 0
    selected: tuple[str, ...] = tuple()
    prefixes = [(0, selected)]
    for dam in order:
        rows += dam_rows[dam]
        selected += (dam,)
        prefixes.append((rows, selected))
    return prefixes


def _nearest_prefix(prefixes: Iterable[tuple[int, tuple[str, ...]]], target_rows: int) -> tuple[str, ...]:
    """Choose closest volume, then fewer DAMs, then canonical DAM-set SHA."""
    _, selected = min(
        prefixes,
        key=lambda item: (abs(item[0] - target_rows), len(item[1]), _dam_set_hash(item[1])),
    )
    return selected


def select_nested_dam_prefixes(
    dam_rows: Mapping[str, int],
    target_fractions: Mapping[str, float],
    seed: int,
) -> dict[str, tuple[str, ...]]:
    """Backward-compatible generic complete-DAM nested prefix planner for fixtures."""
    if not target_fractions:
        raise ValueError("At least one target condition is required")
    if any(fraction <= 0 or fraction > 1 for fraction in target_fractions.values()):
        raise ValueError("Target fractions must be in (0, 1]")
    order = stable_dam_order(dam_rows, seed)
    prefixes = _prefixes(order, dam_rows)
    total = sum(dam_rows.values())
    return {
        condition: _nearest_prefix(prefixes, int(total * fraction + 0.5))
        for condition, fraction in sorted(target_fractions.items(), key=lambda item: item[1])
    }


def select_exp11_dam_prefixes(dam_rows: Mapping[str, int], seed: int) -> dict[str, tuple[str, ...]]:
    """Select H25/H50/H75 prefixes and the immutable H100 complete-DAM reference."""
    if sum(dam_rows.values()) != H100_ROWS:
        raise ValueError(f"EXP-11 H100 requires exactly {H100_ROWS} rows")
    order = stable_dam_order(dam_rows, seed)
    prefixes = _prefixes(order, dam_rows)
    plan = {condition: _nearest_prefix(prefixes, target) for condition, target in EXP11_TARGET_ROWS.items() if condition != "H100"}
    plan["H100"] = order
    return plan


def _nested(plan: Mapping[str, tuple[str, ...]]) -> bool:
    return (
        set(plan["H25"]).issubset(plan["H50"])
        and set(plan["H50"]).issubset(plan["H75"])
        and set(plan["H75"]).issubset(plan["H100"])
    )


def assess_exp11_seed(
    dam_rows: Mapping[str, int],
    seed: int,
    dominant_dams: Iterable[str],
) -> dict[str, Any]:
    """Assess size-only H100 feasibility for one candidate seed."""
    plan = select_exp11_dam_prefixes(dam_rows, seed)
    dominant = tuple(dominant_dams)
    conditions: dict[str, dict[str, Any]] = {}
    for condition, selected in plan.items():
        rows = sum(dam_rows[dam] for dam in selected)
        conditions[condition] = {
            "dam_ids": list(selected),
            "rows": rows,
            "fraction_of_h100": rows / H100_ROWS,
            "abs_deviation": abs(rows - EXP11_TARGET_ROWS[condition]),
            "dam_count": len(selected),
            "dominant_dams_present": {dam: dam in selected for dam in dominant},
        }
    nesting_valid = _nested(plan)
    valid = all(conditions[condition]["abs_deviation"] <= EXP11_MAX_ABS_ROW_DEVIATION for condition in ("H25", "H50", "H75"))
    valid = valid and nesting_valid and set(plan["H100"]) == set(dam_rows)
    return {
        "seed": seed,
        "conditions": conditions,
        "nesting_valid": nesting_valid,
        "complete_dams_valid": True,
        "chain_key": _chain_key(plan),
        "valid_seed": valid,
    }


def accepted_exp11_seeds(
    dam_rows: Mapping[str, int],
    dominant_dams: Iterable[str],
    seed_stream_start: int = 20261001,
    seed_increment: int = 1,
    required_seeds: int = 10,
    max_seed_candidates: int = 100000,
) -> dict[str, Any]:
    """Return the first unique, feasible seeds or a deterministic fail-closed result."""
    accepted: list[dict[str, Any]] = []
    used_chain_keys: set[str] = set()
    for offset in range(max_seed_candidates):
        seed = seed_stream_start + offset * seed_increment
        evidence = assess_exp11_seed(dam_rows, seed, dominant_dams)
        if evidence["valid_seed"] and evidence["chain_key"] not in used_chain_keys:
            accepted.append(evidence)
            used_chain_keys.add(evidence["chain_key"])
            if len(accepted) == required_seeds:
                return {"status": "ACCEPTED", "candidates_evaluated": offset + 1, "accepted": accepted}
    return {"status": "DESIGN_INFEASIBLE", "candidates_evaluated": max_seed_candidates, "accepted": accepted}


def load_h100_dam_rows(path: Path, dam_column: str = "DECLARACION") -> dict[str, int]:
    """Read only the DAM column needed by the authorized EXP-11 planner."""
    counts: dict[str, int] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            dam = row[dam_column].strip()
            if not dam:
                raise ValueError("H100 contains an empty DAM identifier")
            counts[dam] = counts.get(dam, 0) + 1
    return counts


def h100_feasibility_evidence(historical_path: Path, seed_schedule: Iterable[int]) -> dict[str, Any]:
    """Produce non-scientific G2A planning evidence from H100 DAM counts only."""
    dam_rows = load_h100_dam_rows(historical_path)
    dominant = tuple(dam for dam, _ in sorted(dam_rows.items(), key=lambda item: (-item[1], item[0]))[:2])
    original = [assess_exp11_seed(dam_rows, seed, dominant) for seed in seed_schedule]
    accepted = accepted_exp11_seeds(dam_rows, dominant)
    return {
        "artifact_type": "G2A_EXP11_H100_PLANNING_FEASIBILITY_ONLY",
        "retrieval_executed": False,
        "eval_descriptions_read": False,
        "eval_labels_read": False,
        "input": {"path": str(historical_path).replace("\\", "/"), "sha256": sha256_file(historical_path), "rows": sum(dam_rows.values()), "dams": len(dam_rows)},
        "dominant_dams": [{"dam_id": dam, "rows": dam_rows[dam]} for dam in dominant],
        "target_rows": EXP11_TARGET_ROWS,
        "max_abs_row_deviation": EXP11_MAX_ABS_ROW_DEVIATION,
        "original_seed_schedule": list(seed_schedule),
        "original_seed_evidence": original,
        "seed_acceptance": accepted,
    }


def _exp11_dominant_dams(dam_rows: Mapping[str, int]) -> tuple[str, str]:
    dominant = tuple(dam for dam, _ in sorted(dam_rows.items(), key=lambda item: (-item[1], item[0]))[:2])
    if len(dominant) != 2:
        raise ValueError("EXP-11 requires at least two DAM units")
    return dominant[0], dominant[1]


def _exp11_forced_dams(
    condition: str,
    seed: int,
    dominant_dams: tuple[str, str],
    h50_stratum: str | None = None,
) -> tuple[str, ...]:
    if condition == "H25":
        return tuple()
    if condition == "H50":
        if h50_stratum == "D1":
            return (dominant_dams[0],)
        if h50_stratum == "D2":
            return (dominant_dams[1],)
        if h50_stratum is not None:
            raise ValueError(f"Unsupported H50 dominant stratum: {h50_stratum}")
        return (
            min(
                dominant_dams,
                key=lambda dam: (sha256(f"{seed}:H50:DOMINANT:{dam}".encode("utf-8")).hexdigest(), dam),
            ),
        )
    if condition == "H75":
        return dominant_dams
    raise ValueError(f"Unsupported EXP-11 condition: {condition}")


def select_exp11_independent_condition(
    dam_rows: Mapping[str, int],
    condition: str,
    seed: int,
    dominant_dams: tuple[str, str] | None = None,
    h50_stratum: str | None = None,
) -> dict[str, Any]:
    """Select one complete-DAM EXP-11 subset without inter-condition nesting."""
    if condition not in EXP11_SUBSAMPLE_CONDITIONS:
        raise ValueError(f"Unsupported independent EXP-11 condition: {condition}")
    if sum(dam_rows.values()) != H100_ROWS:
        raise ValueError(f"EXP-11 H100 requires exactly {H100_ROWS} rows")
    dominant = dominant_dams or _exp11_dominant_dams(dam_rows)
    if condition != "H50" and h50_stratum is not None:
        raise ValueError("Only H50 may select a dominant stratum")
    forced = _exp11_forced_dams(condition, seed, dominant, h50_stratum)
    forced_rows = sum(dam_rows[dam] for dam in forced)
    eligible = tuple(dam for dam in dam_rows if dam not in dominant)
    condition_key = f"H50:{h50_stratum}" if h50_stratum is not None else condition
    ordered_eligible = tuple(
        sorted(
            eligible,
            key=lambda dam: (sha256(f"{seed}:{condition_key}:{dam}".encode("utf-8")).hexdigest(), dam),
        )
    )
    prefixes = _prefixes(ordered_eligible, dam_rows)
    _, prefix = min(
        prefixes,
        key=lambda item: (
            abs(forced_rows + item[0] - EXP11_TARGET_ROWS[condition]),
            len(item[1]),
            _dam_set_hash((*forced, *item[1])),
        ),
    )
    selected = (*forced, *prefix)
    rows = sum(dam_rows[dam] for dam in selected)
    dominant_count = sum(dam in selected for dam in dominant)
    valid = (
        abs(rows - EXP11_TARGET_ROWS[condition]) <= EXP11_MAX_ABS_ROW_DEVIATION
        and dominant_count == EXP11_REQUIRED_DOMINANT_COUNTS[condition]
        and len(selected) == len(set(selected))
    )
    result = {
        "condition": condition,
        "seed": seed,
        "dam_ids": list(selected),
        "rows": rows,
        "fraction_of_h100": rows / H100_ROWS,
        "absolute_row_deviation": abs(rows - EXP11_TARGET_ROWS[condition]),
        "dam_count": len(selected),
        "dominant_1_present": dominant[0] in selected,
        "dominant_2_present": dominant[1] in selected,
        "dominant_count": dominant_count,
        "complete_dams_valid": True,
        "composition_sha256": _dam_set_hash(selected),
        "valid_seed": valid,
    }
    if h50_stratum is not None:
        result["dominant_stratum"] = h50_stratum
    return result


def accepted_exp11_independent_condition_seeds(
    dam_rows: Mapping[str, int],
    condition: str,
    dominant_dams: tuple[str, str] | None = None,
    seed_stream_start: int = 20261001,
    seed_increment: int = 1,
    required_seeds: int = 10,
    max_seed_candidates: int = 100000,
) -> dict[str, Any]:
    """Accept the first unique complete-DAM subsets for one independent condition."""
    accepted: list[dict[str, Any]] = []
    used_compositions: set[str] = set()
    dominant = dominant_dams or _exp11_dominant_dams(dam_rows)
    for offset in range(max_seed_candidates):
        seed = seed_stream_start + offset * seed_increment
        candidate = select_exp11_independent_condition(dam_rows, condition, seed, dominant)
        if candidate["valid_seed"] and candidate["composition_sha256"] not in used_compositions:
            candidate["replicate_id"] = f"{condition}-R{len(accepted) + 1:02d}"
            accepted.append(candidate)
            used_compositions.add(candidate["composition_sha256"])
            if len(accepted) == required_seeds:
                return {
                    "condition": condition,
                    "status": "ACCEPTED",
                    "candidates_evaluated": offset + 1,
                    "accepted": accepted,
                }
    return {
        "condition": condition,
        "status": "INDEPENDENT_DESIGN_INFEASIBLE",
        "candidates_evaluated": max_seed_candidates,
        "accepted": accepted,
    }


def accepted_exp11_h50_paired_seeds(
    dam_rows: Mapping[str, int],
    dominant_dams: tuple[str, str] | None = None,
    seed_stream_start: int = 20261001,
    seed_increment: int = 1,
    required_pairs: int = 5,
    max_seed_candidates: int = 100000,
) -> dict[str, Any]:
    """Accept paired H50-D1/H50-D2 complete-DAM candidates from the same seed."""
    accepted_pairs: list[dict[str, Any]] = []
    used_by_stratum = {stratum: set() for stratum in EXP11_H50_STRATA}
    dominant = dominant_dams or _exp11_dominant_dams(dam_rows)
    for offset in range(max_seed_candidates):
        seed = seed_stream_start + offset * seed_increment
        candidates = {
            stratum: select_exp11_independent_condition(dam_rows, "H50", seed, dominant, stratum)
            for stratum in EXP11_H50_STRATA
        }
        if not all(candidate["valid_seed"] for candidate in candidates.values()):
            continue
        if any(candidates[stratum]["composition_sha256"] in used_by_stratum[stratum] for stratum in EXP11_H50_STRATA):
            continue
        pair_id = f"H50-P{len(accepted_pairs) + 1:02d}"
        for stratum, candidate in candidates.items():
            candidate["pair_id"] = pair_id
            candidate["replicate_id"] = f"H50-{stratum}-R{len(accepted_pairs) + 1:02d}"
            used_by_stratum[stratum].add(candidate["composition_sha256"])
        accepted_pairs.append({"pair_id": pair_id, "seed": seed, "D1": candidates["D1"], "D2": candidates["D2"]})
        if len(accepted_pairs) == required_pairs:
            return {
                "condition": "H50",
                "status": "ACCEPTED",
                "candidates_evaluated": offset + 1,
                "paired_seeds": [pair["seed"] for pair in accepted_pairs],
                "accepted_pairs": accepted_pairs,
            }
    return {
        "condition": "H50",
        "status": "H50_STRATIFIED_DESIGN_INFEASIBLE",
        "candidates_evaluated": max_seed_candidates,
        "paired_seeds": [pair["seed"] for pair in accepted_pairs],
        "accepted_pairs": accepted_pairs,
    }


def accepted_exp11_independent_schedules(
    dam_rows: Mapping[str, int],
    seed_stream_start: int = 20261001,
    seed_increment: int = 1,
    required_seeds: int = 10,
    max_seed_candidates: int = 100000,
) -> dict[str, Any]:
    """Build H25/H75 schedules and a paired, stratified H50 schedule."""
    if required_seeds != 10:
        raise ValueError("EXP-11 requires ten H25, H50 and H75 replicates")
    dominant = _exp11_dominant_dams(dam_rows)
    by_condition = {
        condition: accepted_exp11_independent_condition_seeds(
            dam_rows,
            condition,
            dominant,
            seed_stream_start,
            seed_increment,
            required_seeds,
            max_seed_candidates,
        )
        for condition in ("H25", "H75")
    }
    h50_pairs = accepted_exp11_h50_paired_seeds(
        dam_rows,
        dominant,
        seed_stream_start,
        seed_increment,
        required_pairs=5,
        max_seed_candidates=max_seed_candidates,
    )
    h50_records = [
        pair[stratum]
        for pair in h50_pairs["accepted_pairs"]
        for stratum in EXP11_H50_STRATA
    ]
    by_condition["H50"] = {
        "condition": "H50",
        "status": h50_pairs["status"],
        "candidates_evaluated": h50_pairs["candidates_evaluated"],
        "paired_seeds": h50_pairs["paired_seeds"],
        "accepted": h50_records,
        "accepted_pairs": h50_pairs["accepted_pairs"],
    }
    return {
        "status": "ACCEPTED" if all(item["status"] == "ACCEPTED" for item in by_condition.values()) else "INDEPENDENT_DESIGN_INFEASIBLE",
        "dominant_dams": dominant,
        "by_condition": by_condition,
    }


def load_h100_dam_profiles(path: Path, dam_column: str = "DECLARACION", label_column: str = "NANDINA") -> tuple[dict[str, int], dict[str, dict[str, int]], dict[str, int]]:
    """Read H100 DAM and NANDINA counts; labels are descriptors, never selector inputs."""
    dam_rows: dict[str, int] = {}
    dam_label_counts: dict[str, dict[str, int]] = {}
    reference_label_counts: dict[str, int] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            dam = row[dam_column].strip()
            label = row[label_column].strip()
            if not dam or not label:
                raise ValueError("H100 requires non-empty DAM and NANDINA fields")
            dam_rows[dam] = dam_rows.get(dam, 0) + 1
            per_dam = dam_label_counts.setdefault(dam, {})
            per_dam[label] = per_dam.get(label, 0) + 1
            reference_label_counts[label] = reference_label_counts.get(label, 0) + 1
    return dam_rows, dam_label_counts, reference_label_counts


def _exp11_descriptors(
    dam_rows: Mapping[str, int],
    dam_label_counts: Mapping[str, Mapping[str, int]],
    reference_label_counts: Mapping[str, int],
    dam_ids: Iterable[str],
) -> dict[str, Any]:
    selected = tuple(dam_ids)
    concentration = dam_concentration_metrics(dam_rows, selected)
    selected_labels = _candidate_label_counts(dam_label_counts, selected)
    independent_support: dict[str, set[str]] = {}
    for dam in selected:
        for label in dam_label_counts[dam]:
            independent_support.setdefault(label, set()).add(dam)
    support_counts = [len(dams) for dams in independent_support.values()]
    histogram = Counter(support_counts)
    return {
        "dam_hhi": concentration["hhi"],
        "effective_dam": concentration["effective_dam"],
        "nandina_coverage": {
            "covered_codes": len(selected_labels),
            "reference_codes": len(reference_label_counts),
            "fraction": len(selected_labels) / len(reference_label_counts),
        },
        "independent_dam_support_summary": {
            "supported_codes": len(support_counts),
            "minimum_dams_per_nandina": min(support_counts),
            "maximum_dams_per_nandina": max(support_counts),
            "mean_dams_per_nandina": sum(support_counts) / len(support_counts),
            "code_count_by_independent_dam_support": {str(key): histogram[key] for key in sorted(histogram)},
        },
    }


def _exp11_composition_record(
    selection: Mapping[str, Any],
    dam_rows: Mapping[str, int],
    dam_label_counts: Mapping[str, Mapping[str, int]],
    reference_label_counts: Mapping[str, int],
) -> dict[str, Any]:
    record = dict(selection)
    record.update(_exp11_descriptors(dam_rows, dam_label_counts, reference_label_counts, record["dam_ids"]))
    return record


def _exp11_condition_summary(records: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    items = tuple(records)
    rows = [int(item["rows"]) for item in items]
    fractions = [float(item["fraction_of_h100"]) for item in items]
    hhis = [float(item["dam_hhi"]) for item in items]
    return {
        "replicate_count": len(items),
        "rows": {"min": min(rows), "max": max(rows), "mean": sum(rows) / len(rows)},
        "fractions": {"min": min(fractions), "max": max(fractions), "mean": sum(fractions) / len(fractions)},
        "dam_hhi": {"min": min(hhis), "max": max(hhis), "mean": sum(hhis) / len(hhis)},
    }


def exp11_independent_condition_feasibility_evidence(
    historical_path: Path,
    seed_stream_start: int = 20261001,
    seed_increment: int = 1,
    required_seeds: int = 10,
    max_seed_candidates: int = 100000,
) -> dict[str, Any]:
    """Generate the authorized pre-retrieval EXP-11 independent-condition evidence."""
    dam_rows, dam_label_counts, reference_label_counts = load_h100_dam_profiles(historical_path)
    if sum(dam_rows.values()) != H100_ROWS:
        raise ValueError(f"EXP-11 H100 requires exactly {H100_ROWS} rows")
    schedules = accepted_exp11_independent_schedules(
        dam_rows,
        seed_stream_start,
        seed_increment,
        required_seeds,
        max_seed_candidates,
    )
    dominant_1, dominant_2 = schedules["dominant_dams"]
    records_by_condition = {
        condition: [
            _exp11_composition_record(item, dam_rows, dam_label_counts, reference_label_counts)
            for item in schedules["by_condition"][condition]["accepted"]
        ]
        for condition in EXP11_SUBSAMPLE_CONDITIONS
    }
    h100_selection = {
        "condition": "H100",
        "replicate_id": "H100_REFERENCE",
        "seed": None,
        "dam_ids": sorted(dam_rows),
        "rows": H100_ROWS,
        "fraction_of_h100": 1.0,
        "absolute_row_deviation": 0,
        "dam_count": len(dam_rows),
        "dominant_1_present": True,
        "dominant_2_present": True,
        "dominant_count": 2,
        "complete_dams_valid": True,
        "composition_sha256": _dam_set_hash(dam_rows),
        "valid_seed": True,
    }
    h100_reference = _exp11_composition_record(h100_selection, dam_rows, dam_label_counts, reference_label_counts)
    lower_h25, upper_h25 = EXP11_TARGET_ROWS["H25"] - EXP11_MAX_ABS_ROW_DEVIATION, EXP11_TARGET_ROWS["H25"] + EXP11_MAX_ABS_ROW_DEVIATION
    lower_h50, upper_h50 = EXP11_TARGET_ROWS["H50"] - EXP11_MAX_ABS_ROW_DEVIATION, EXP11_TARGET_ROWS["H50"] + EXP11_MAX_ABS_ROW_DEVIATION
    lower_h75, upper_h75 = EXP11_TARGET_ROWS["H75"] - EXP11_MAX_ABS_ROW_DEVIATION, EXP11_TARGET_ROWS["H75"] + EXP11_MAX_ABS_ROW_DEVIATION
    dominant_rows = dam_rows[dominant_1] + dam_rows[dominant_2]
    return {
        "artifact_type": "G2A_EXP11_INDEPENDENT_CONDITION_FEASIBILITY_V0_2_ONLY",
        "supersedes_planning_evidence": "exp11_independent_condition_feasibility_v0.1.json",
        "retrieval_executed": False,
        "eval_descriptions_read": False,
        "eval_labels_read": False,
        "selection_uses_nandina": False,
        "selection_uses_eval": False,
        "input": {
            "path": str(historical_path).replace("\\", "/"),
            "sha256": sha256_file(historical_path),
            "rows": H100_ROWS,
            "dams": len(dam_rows),
            "reference_nandina_codes": len(reference_label_counts),
        },
        "dominant_dams": [
            {"dam_id": dominant_1, "rows": dam_rows[dominant_1]},
            {"dam_id": dominant_2, "rows": dam_rows[dominant_2]},
        ],
        "f008_structural_infeasibility": {
            "classification": "PRE_EXECUTION_DESIGN_INFEASIBILITY",
            "status": "STRUCTURALLY_INFEASIBLE_UNDER_FROZEN_GROUP_AND_VOLUME_CONSTRAINTS",
            "bands": {"H25": [lower_h25, upper_h25], "H50": [lower_h50, upper_h50], "H75": [lower_h75, upper_h75]},
            "rest_of_dams_rows": H100_ROWS - dominant_rows,
            "minimum_h75_rows_if_h25_were_nested": lower_h25 + dominant_rows,
            "h75_upper_band": upper_h75,
        },
        "f010_h50_dominant_stratum_imbalance": {
            "classification": "H50_DOMINANT_STRATUM_IMBALANCE",
            "status": "OPEN_CORRECTABLE_PRE_EXECUTION",
            "previous_v0_1_counts": {dominant_1: 2, dominant_2: 8},
            "previous_v0_1_mean_hhi": {dominant_1: 0.5197288651, dominant_2: 0.4232268197},
            "correction": "PAIRED_EQUAL_WEIGHT_5_D1_5_D2",
        },
        "selection": {
            "sampling_design": "INDEPENDENT_COMPLETE_DAM_SUBSETS_BY_CONDITION",
            "candidate_seed_stream": {"start": seed_stream_start, "increment": seed_increment, "max_candidates": max_seed_candidates},
            "required_dominant_counts": EXP11_REQUIRED_DOMINANT_COUNTS,
            "h50_strata": {"D1": dominant_1, "D2": dominant_2},
            "h50_pair_acceptance": "same seed; both strata valid; unique composition within stratum",
            "selection_inputs": ["dam_id", "row_count", "seed", "condition_id"],
        },
        "seed_acceptance": schedules,
        "replicate_schedules": {
            "H25": [item["seed"] for item in records_by_condition["H25"]],
            "H50": {
                "paired_seeds": schedules["by_condition"]["H50"]["paired_seeds"],
                "D1": [item["seed"] for item in records_by_condition["H50"] if item["dominant_stratum"] == "D1"],
                "D2": [item["seed"] for item in records_by_condition["H50"] if item["dominant_stratum"] == "D2"],
            },
            "H75": [item["seed"] for item in records_by_condition["H75"]],
        },
        "conditions": records_by_condition,
        "h100_reference": h100_reference,
        "descriptive_summaries": {
            condition: _exp11_condition_summary(records)
            for condition, records in records_by_condition.items()
            if records
        },
        "h50_dominant_counts": {
            dominant_1: sum(record["dominant_1_present"] for record in records_by_condition["H50"]),
            dominant_2: sum(record["dominant_2_present"] for record in records_by_condition["H50"]),
        },
        "h50_stratum_summaries": {
            stratum: _exp11_condition_summary(
                record for record in records_by_condition["H50"] if record["dominant_stratum"] == stratum
            )
            for stratum in EXP11_H50_STRATA
        },
        "h50_interpretation": {
            "primary_analysis": "POOLED_EQUAL_WEIGHT_5_D1_5_D2",
            "secondary_diagnostic": "DOMINANT_STRATUM_COMPARISON",
            "causal_dominant_identity_claim_allowed": False,
        },
    }


def dam_concentration_metrics(dam_rows: Mapping[str, int], dam_ids: Iterable[str]) -> dict[str, float | int]:
    selected = tuple(dam_ids)
    rows = sum(dam_rows[dam] for dam in selected)
    if not selected or rows <= 0:
        raise ValueError("A diversity candidate needs at least one positive-row DAM")
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


def total_variation_distance(
    candidate_label_counts: Mapping[str, int],
    candidate_rows: int,
    reference_label_counts: Mapping[str, int],
) -> float:
    """TVD over the H100 reference-code universe, using each bank's row proportions."""
    reference_rows = sum(reference_label_counts.values())
    if candidate_rows <= 0 or reference_rows <= 0:
        raise ValueError("TVD requires positive candidate and reference row counts")
    return 0.5 * sum(
        abs(candidate_label_counts.get(code, 0) / candidate_rows - reference_label_counts[code] / reference_rows)
        for code in reference_label_counts
    )


def _candidate_label_counts(dam_label_counts: Mapping[str, Mapping[str, int]], dam_ids: Iterable[str]) -> dict[str, int]:
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
    candidate_count: int = EXP12_CANDIDATE_COUNT,
) -> tuple[Exp12Candidate, ...]:
    """Generate feasible synthetic-or-approved-pool candidates without retrieval inputs."""
    if candidate_count <= 0:
        raise ValueError("candidate_count must be positive")
    if set(dam_rows) != set(dam_label_counts):
        raise ValueError("Each DAM needs exactly one row and label-count profile")
    candidates: list[Exp12Candidate] = []
    seen: set[tuple[str, ...]] = set()
    for candidate_index in range(candidate_count):
        order = tuple(sorted(dam_rows, key=lambda dam: (sha256(f"{seed}:{candidate_index}:{dam}".encode("utf-8")).hexdigest(), dam)))
        selected = _nearest_prefix(_prefixes(order, dam_rows), EXP12_TARGET_ROWS)
        canonical_ids = tuple(sorted(selected))
        if canonical_ids in seen or set(canonical_ids) & eval_dams:
            continue
        seen.add(canonical_ids)
        concentration = dam_concentration_metrics(dam_rows, canonical_ids)
        rows = int(concentration["rows"])
        if not EXP12_MIN_ROWS <= rows <= EXP12_MAX_ROWS:
            continue
        label_counts = _candidate_label_counts(dam_label_counts, canonical_ids)
        coverage = sum(label_counts.get(code, 0) > 0 for code in reference_label_counts) / len(reference_label_counts)
        tvd = total_variation_distance(label_counts, rows, reference_label_counts)
        if coverage != 1.0 or tvd > EXP12_MAX_TVD:
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
    """Select D-HIGH/D-MID/D-LOW from feasible candidates by predeclared HHI quantiles."""
    pool = tuple(candidates)
    if len(pool) < EXP12_MINIMUM_UNIQUE_FEASIBLE:
        raise ValueError("EXP-12 requires at least 30 unique feasible candidates")
    selected: dict[str, Exp12Candidate] = {}
    for condition, quantile in (("D-HIGH", 0.1), ("D-MID", 0.5), ("D-LOW", 0.9)):
        ordered = sorted(
            pool,
            key=lambda candidate: (
                candidate.hhi,
                sha256(f"{seed}:{condition}:{'|'.join(candidate.dam_ids)}".encode("utf-8")).hexdigest(),
            ),
        )
        selected[condition] = ordered[int(quantile * (len(ordered) - 1))]
    if len({candidate.dam_ids for candidate in selected.values()}) != 3:
        raise ValueError("EXP-12 conditions must use distinct DAM sets")
    if not selected["D-LOW"].hhi > selected["D-MID"].hhi > selected["D-HIGH"].hhi:
        raise ValueError("EXP-12 requires strict HHI_DLOW > HHI_DMID > HHI_DHIGH")
    return selected


def assert_expanded_historical_gate(gate_status: str | None) -> None:
    """Fail closed until a separately approved expanded historical gate is supplied."""
    if gate_status != "APPROVED_NEW_HISTORICAL_GATE":
        raise ValueError("Expanded historical data are unavailable: execution is blocked fail-closed")


def validate_exp11_contract(config: Mapping[str, Any]) -> None:
    """Validate EXP-11 freeze fields without accessing experiment inputs."""
    if _require(config, "contract_status") != "FROZEN_APPROVED_FOR_EXP11A":
        raise ValueError("EXP-11 must remain frozen and approved only for EXP-11A")
    if _require(config, "execution_authorized") is not True:
        raise ValueError("EXP-11A authorization must be explicit")
    if _require(config, "execution_authorized_scope") != "EXP11A_H25_H50_H75_H100_ONLY":
        raise ValueError("EXP-11 authorization scope must exclude H150 and H200")
    if _require(config, "exp11a_execution_authorized") is not True:
        raise ValueError("EXP-11A must be explicitly authorized")
    if _require(config, "authorized_conditions") != ["H25", "H50", "H75", "H100"]:
        raise ValueError("EXP-11A authorized conditions must be the frozen H25/H50/H75/H100 set")
    if _require(config, "exp11b_execution_authorized") is not False:
        raise ValueError("EXP-11B must remain unauthorized")
    if _require(config, "expanded_historical_conditions_authorized") is not False:
        raise ValueError("Expanded historical conditions must remain unauthorized")
    fixed_eval = _require(config, "fixed_eval")
    h100 = _require(config, "h100_frozen_reference")
    selection = _require(config, "selection")
    feasibility = _require(config, "feasibility_contract")
    if fixed_eval.get("sha256") != "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941":
        raise ValueError("EXP-11 fixed eval SHA is not the frozen v0.2 contract")
    if h100.get("sha256") != "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff" or h100.get("rows") != H100_ROWS:
        raise ValueError("EXP-11 H100 must remain the frozen 2,950-row reference")
    if feasibility.get("target_rows") != EXP11_TARGET_ROWS or feasibility.get("max_abs_row_deviation") != EXP11_MAX_ABS_ROW_DEVIATION:
        raise ValueError("EXP-11 size feasibility contract is not frozen")
    if selection.get("selection_unit") != "DAM" or not selection.get("preserve_complete_dams"):
        raise ValueError("EXP-11 must select complete DAM units")
    if selection.get("nested_policy") != "NOT_REQUIRED_STRUCTURALLY_INFEASIBLE":
        raise ValueError("EXP-11 cannot retain the structurally infeasible nesting requirement")
    if selection.get("sampling_design") != "INDEPENDENT_COMPLETE_DAM_SUBSETS_BY_CONDITION":
        raise ValueError("EXP-11 must use independent complete-DAM subsets by condition")
    if selection.get("uses_eval_performance") or not _selection_is_eval_independent(selection):
        raise ValueError("EXP-11 selection cannot use evaluation performance")
    if selection.get("uses_nandina_for_selection") or not feasibility.get("no_label_balancing") or not feasibility.get("no_nandina_distribution_selection"):
        raise ValueError("EXP-11 cannot balance NANDINA during size selection")
    structural = _require(config, "structural_volume_consequences")
    if structural.get("required_dominant_count") != EXP11_REQUIRED_DOMINANT_COUNTS:
        raise ValueError("EXP-11 dominant-DAM structural consequences are not frozen")
    if structural.get("nested_design_status") != "STRUCTURALLY_INFEASIBLE_UNDER_FROZEN_GROUP_AND_VOLUME_CONSTRAINTS":
        raise ValueError("EXP-11 must preserve the F008 structural finding")
    policy = _require(config, "replicate_policy")
    if policy.get("h100_replicates") != 1:
        raise ValueError("H100 must remain a single frozen reference")
    if policy.get("seed_schedule") != []:
        raise ValueError("EXP-11 independent conditions cannot use one shared nested seed schedule")
    for condition in ("H25", "H75"):
        schedule = policy.get(f"accepted_seed_schedule_{condition}")
        if not isinstance(schedule, list) or len(schedule) != 10 or len(set(schedule)) != 10:
            raise ValueError(f"EXP-11 {condition} needs ten frozen unique candidate seeds")
    h50_paired = policy.get("accepted_paired_seed_schedule_H50")
    h50_d1 = policy.get("accepted_seed_schedule_H50_D1")
    h50_d2 = policy.get("accepted_seed_schedule_H50_D2")
    if not all(isinstance(schedule, list) and len(schedule) == 5 and len(set(schedule)) == 5 for schedule in (h50_paired, h50_d1, h50_d2)):
        raise ValueError("EXP-11 H50 requires five unique paired seeds in each dominant stratum")
    if h50_paired != h50_d1 or h50_paired != h50_d2:
        raise ValueError("Every H50 D1/D2 replicate must retain its paired seed")
    planning = _require(policy, "planning_feasibility")
    if planning.get("status") != "FROZEN_APPROVED_FOR_EXP11A":
        raise ValueError("EXP-11 independent schedules must retain the approved EXP-11A freeze")
    if planning.get("accepted_seed_count_per_condition") != {"H25": 10, "H50_D1": 5, "H50_D2": 5, "H75": 10}:
        raise ValueError("EXP-11 H50 stratum replicate counts are not frozen")
    h50 = _require(config, "h50_stratification")
    if h50.get("status") != "FROZEN_APPROVED_FOR_EXP11A":
        raise ValueError("EXP-11 H50 stratification must retain the approved EXP-11A freeze")
    if h50.get("primary_analysis") != "POOLED_EQUAL_WEIGHT_5_D1_5_D2" or h50.get("secondary_diagnostic") != "DOMINANT_STRATUM_COMPARISON":
        raise ValueError("EXP-11 H50 analysis and diagnostic contract are not frozen")
    strata = _require(h50, "strata")
    if strata.get("D1", {}).get("forced_included") != "118-2026-10-128583-00" or strata.get("D1", {}).get("forced_excluded") != "118-2026-10-146957-00":
        raise ValueError("EXP-11 H50 D1 forced dominant contract is not frozen")
    if strata.get("D2", {}).get("forced_included") != "118-2026-10-146957-00" or strata.get("D2", {}).get("forced_excluded") != "118-2026-10-128583-00":
        raise ValueError("EXP-11 H50 D2 forced dominant contract is not frozen")
    findings = _require(config, "g2a_findings")
    expected_findings = {
        "F008": ("PRE_EXECUTION_DESIGN_INFEASIBILITY", "VERIFIED_IN_G2", "FROZEN_PRE_EXECUTION_CORRECTION"),
        "F009": ("STRUCTURAL_SIZE_COMPOSITION_COUPLING", "VERIFIED_IN_G2", "DECLARED_LIMITATION"),
        "F010": ("H50_DOMINANT_STRATUM_IMBALANCE", "VERIFIED_IN_G2", "RESOLVED_PRE_EXECUTION_BY_H50_STRATIFICATION"),
    }
    for finding_id, (classification, status, resolution) in expected_findings.items():
        finding = _require(findings, finding_id)
        if (
            finding.get("classification") != classification
            or finding.get("status") != status
            or finding.get("resolution") != resolution
        ):
            raise ValueError(f"EXP-11 {finding_id} is not frozen in the candidate contract")
    if findings["F010"].get("previous_v0_1_dominant_counts") != {"D1": 2, "D2": 8}:
        raise ValueError("EXP-11 F010 must retain the v0.1 H50 imbalance history")
    if findings["F010"].get("final_dominant_counts") != {"D1": 5, "D2": 5}:
        raise ValueError("EXP-11 F010 must retain the final balanced H50 counts")
    interpretation = _require(config, "interpretation")
    if interpretation.get("isolated_size_causal_effect_claim_allowed") or interpretation.get("h50_dominant_identity_causal_claim_allowed"):
        raise ValueError("EXP-11 cannot claim isolated causal size or dominant-DAM effects")
    output_contract = _require(config, "output_contract")
    required_manifest_descriptors = {
        "nominal_condition", "realized_rows", "realized_fraction", "dam_count", "dam_hhi",
        "effective_dam", "nandina_coverage", "dominant_structure", "historical_support_summary",
    }
    if not required_manifest_descriptors.issubset(set(output_contract.get("manifest_required_fields", []))):
        raise ValueError("EXP-11 future manifests must retain the descriptive composition fields")
    required_case_fields = {"case_id", "reference_nandina_supported_in_bank", "reference_independent_dam_support_count"}
    if not required_case_fields.issubset(set(output_contract.get("case_level_required_fields", []))):
        raise ValueError("EXP-11 future case output must retain historical support fields")
    for condition in ("H150", "H200"):
        pending = _require(_require(config, "target_conditions"), condition)
        if pending.get("source") != EXPANDED_HISTORICAL_GATE or not pending.get("fail_closed"):
            raise ValueError(f"{condition} must remain gated by new historical evidence")
        if pending.get("path") is not None or pending.get("sha256") is not None:
            raise ValueError(f"{condition} cannot invent an unavailable source path or SHA")


def validate_exp12_contract(config: Mapping[str, Any]) -> None:
    """Validate EXP-12's fail-closed methodological freeze without executing it."""
    if _require(config, "contract_status") != "CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE":
        raise ValueError("EXP-12 must remain a frozen pending candidate")
    if _require(config, "method_contract") != "CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE":
        raise ValueError("EXP-12 must remain conditional on a new historical gate")
    if _require(_require(config, "fixed_eval"), "sha256") != "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941":
        raise ValueError("EXP-12 fixed eval SHA is not the frozen v0.2 contract")
    universe = _require(config, "sampling_universe")
    if universe.get("source") != EXPANDED_HISTORICAL_GATE or not universe.get("fail_closed"):
        raise ValueError("EXP-12 must fail closed without the expanded historical gate")
    if universe.get("path") is not None or universe.get("sha256") is not None or not universe.get("must_not_fallback_to_h100"):
        raise ValueError("EXP-12 cannot silently replace the expanded universe with H100")
    reference = _require(config, "reference_h100")
    if reference.get("sha256") != "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff":
        raise ValueError("EXP-12 reference labels must come from frozen H100")
    volume = _require(config, "volume_control")
    if (volume.get("target_rows"), volume.get("max_abs_row_deviation"), volume.get("minimum_rows"), volume.get("maximum_rows")) != (2950, 148, 2802, 3098):
        raise ValueError("EXP-12 integer volume contract is not frozen")
    labels = _require(config, "label_control")
    if labels.get("required_label_coverage_fraction") != 1.0 or labels.get("maximum_tvd") != EXP12_MAX_TVD:
        raise ValueError("EXP-12 label matching contract is not frozen")
    generation = _require(config, "candidate_generation")
    if generation.get("candidate_count") != EXP12_CANDIDATE_COUNT:
        raise ValueError("EXP-12 candidate count is not frozen")
    feasibility = _require(config, "feasibility_filter")
    if feasibility.get("minimum_unique_feasible_candidates") != EXP12_MINIMUM_UNIQUE_FEASIBLE:
        raise ValueError("EXP-12 minimum feasible candidates is not frozen")
    conditions = _require(config, "condition_selection")
    if conditions.get("quantiles") != {"D-HIGH": 0.1, "D-MID": 0.5, "D-LOW": 0.9}:
        raise ValueError("EXP-12 quantiles are not frozen")
    selection = _require(config, "selection")
    if selection.get("uses_eval_performance") or not _selection_is_eval_independent(selection):
        raise ValueError("EXP-12 selection cannot use evaluation performance")
    if not selection.get("no_weighted_multiobjective"):
        raise ValueError("EXP-12 must use HHI as its single primary diversity variable")
    manipulation = _require(config, "future_manipulation_check")
    required_reports = {
        "HHI_q10", "HHI_q50", "HHI_q90", "HHI_span_q90_q10",
        "effective_DAM_q10", "effective_DAM_q50", "effective_DAM_q90", "effective_DAM_ratio_high_low",
    }
    if set(manipulation.get("required_reports", [])) != required_reports:
        raise ValueError("EXP-12 future historical gate must report all diversity manipulation descriptors")
    if manipulation.get("strict_hhi_order_fail_closed") != "HHI_DLOW > HHI_DMID > HHI_DHIGH":
        raise ValueError("EXP-12 must fail closed when strict HHI ordering is absent")
    if not manipulation.get("manipulation_strength_review_required") or manipulation.get("new_threshold_introduced"):
        raise ValueError("EXP-12 manipulation review must remain required without a new threshold")


def validate_manifest_fields(manifest: Mapping[str, Any], required_fields: Iterable[str]) -> None:
    """Check an execution manifest only for the predeclared identity fields."""
    missing = [field for field in required_fields if field not in manifest]
    if missing:
        raise ValueError(f"Manifest misses required fields: {', '.join(missing)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--historical", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed-start", type=int, default=20261001)
    parser.add_argument("--seed-count", type=int, default=10)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    evidence = exp11_independent_condition_feasibility_evidence(
        args.historical,
        seed_stream_start=args.seed_start,
        required_seeds=args.seed_count,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if evidence["seed_acceptance"]["status"] == "ACCEPTED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
