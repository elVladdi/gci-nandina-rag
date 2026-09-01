"""Execute the frozen EXP-11A historical-bank size sensitivity design.

This module intentionally imports the EXP-04 v0.2 BM25 helpers.  It never
reselects DAMs: all variable-bank compositions come from the versioned G2A
v0.2 evidence, while H100 is re-executed only as a deterministic check.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
import platform
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import pandas as pd

from ..bm25_index import sha256_file
from ..evaluation.group_split_by_dam import exact_duplicate_audit, near_duplicate_audit, normalize_text
from ..utils.paths import ensure_parent, project_root, resolve_project_path
from . import evaluate_historical_retrieval_data_aduanas_v02 as historical
from .plan_historical_bank_conditions_v03 import _dam_set_hash, validate_exp11_contract


EXPERIMENT_ID = "EXP-11A"
EXPERIMENT_VERSION = "historical_size_sensitivity_v0.3"
BASE_MAIN_COMMIT = "a6140b66cf2975313be327d6d3d4e18e38f1fdf5"
H100_SHA256 = "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff"
EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
H100_MRR_ABS_TOLERANCE = 1e-12
H100_COMPARISON_FIELDS = (
    ("Top1_count", "Top1_correct_count", "exact_at_1_numerator"),
    ("Top3_count", "Top3_correct_count", "exact_at_3_numerator"),
    ("Top5_count", "Top5_correct_count", "exact_at_5_numerator"),
    ("Top10_count", "Top10_correct_count", "exact_at_10_numerator"),
    ("Top50_count", "Top50_correct_count", "exact_at_50_numerator"),
    ("MRR", "MRR", "mrr"),
)
K_VALUES = (1, 3, 5, 10, 50)
ALLOWED_CONDITIONS = ("H25", "H50", "H75", "H100")
ALLOWED_UNTRACKED = {
    "Referencias/Antecedentes/",
    "Referencias/Glosario/",
    "data/Series - Descripciones.xlsx",
}
DEFAULT_CONFIG = Path("src/configs/exp11_historical_size_sensitivity_v0.3.json")
DEFAULT_EVIDENCE = Path("outputs/audits/g2a_reproducibility_v0.1/exp11_independent_condition_feasibility_v0.2.json")
DEFAULT_GATE = Path("outputs/audits/g2a_reproducibility_v0.1/gate_g2a_reproducibility_manifest_v0.1.json")
DEFAULT_HISTORICAL = Path("data/processed/data_aduanas_historico_clase87_v0.2.csv")
DEFAULT_EVAL = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")
DEFAULT_OUTPUT = Path("outputs/experiments/exp11a_historical_size_sensitivity_v0.3")
DEFAULT_H100_REFERENCE = Path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json")
QUERY_COLUMN = historical.QUERY_COLUMN
LABEL_COLUMN = historical.LABEL_COLUMN
DAM_COLUMN = "DECLARACION"


def _read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, check=True, text=True, capture_output=True)
    return result.stdout.strip()


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fields: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def _write_text(path: Path, text: str) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text if text.endswith("\n") else f"{text}\n")


def _rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _canonical_status_lines(root: Path) -> list[str]:
    return [
        line.replace("\\", "/")
        for line in _git(root, "status", "--short", "-z").split("\0")
        if line
    ]


def _validate_git_state(root: Path) -> dict[str, Any]:
    branch = _git(root, "branch", "--show-current")
    commit = _git(root, "rev-parse", "HEAD")
    _require(branch == "codex/exp11a-size-sensitivity-v01", f"EXP-11A must run on its experimental branch, found {branch}")
    _require(commit != BASE_MAIN_COMMIT, "EXP-11A execution requires the frozen pre-execution commit, not main base")
    lines = _canonical_status_lines(root)
    unexpected = []
    for line in lines:
        if not line.startswith("?? ") or line[3:] not in ALLOWED_UNTRACKED:
            unexpected.append(line)
    _require(not unexpected, f"Unexpected Git state before retrieval: {unexpected}")
    return {"branch": branch, "commit": commit, "dirty_status_short": lines}


def _validate_execution_contract(config: Mapping[str, Any], gate: Mapping[str, Any], exp12: Mapping[str, Any]) -> None:
    validate_exp11_contract(config)
    _require(gate.get("status") == "APPROVED_WITH_NONBLOCKING_LIMITATIONS", "G2A final gate is not approved")
    _require(gate.get("G2A_CLOSED") is True, "G2A must be closed before EXP-11A")
    authorization = gate.get("execution_authorization", {})
    _require(authorization.get("exp11a") is True, "Gate does not authorize EXP-11A")
    _require(authorization.get("exp11a_execution_scope") == "EXP11A_H25_H50_H75_H100_ONLY", "EXP-11A scope is not frozen")
    _require(authorization.get("authorized_conditions") == list(ALLOWED_CONDITIONS), "Gate authorized conditions differ from frozen EXP-11A")
    _require(authorization.get("exp11b") is False and authorization.get("expanded_historical_conditions") is False, "EXP-11B must remain fail-closed")
    _require(authorization.get("exp12") is False, "EXP-12 must remain unauthorized")
    for condition in ("H150", "H200"):
        pending = config["target_conditions"][condition]
        _require(pending.get("enabled") is False, f"{condition} must remain disabled")
        _require(pending.get("source") == "PENDING_NEW_HISTORICAL_GATE" and pending.get("fail_closed") is True, f"{condition} gate must remain fail-closed")
    _require(exp12.get("contract_status") == "CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE", "EXP-12 contract changed")
    _require(exp12.get("execution_authorized") is False, "EXP-12 must remain unauthorized")
    _require(exp12.get("sampling_universe", {}).get("source") == "PENDING_NEW_HISTORICAL_GATE", "EXP-12 cannot use an existing historical bank")
    _require(exp12.get("sampling_universe", {}).get("must_not_fallback_to_h100") is True, "EXP-12 H100 fallback must remain forbidden")


def _source_by_dam(rows: Sequence[Mapping[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        dam = historical._clean(row.get(DAM_COLUMN))
        _require(bool(dam), "H100 row has no DECLARACION DAM")
        grouped[dam].append(dict(row))
    return dict(grouped)


def _spec_sort_key(spec: Mapping[str, Any]) -> tuple[int, int, int]:
    condition_order = {"H100": 0, "H25": 1, "H50": 2, "H75": 3}
    if spec["condition_id"] == "H100":
        return condition_order["H100"], 0, 0
    replicate = str(spec["replicate_id"])
    if spec["condition_id"] == "H50":
        pair = int(str(spec["pair_id"]).rsplit("P", 1)[1])
        stratum = 0 if spec.get("dominant_stratum") == "D1" else 1
        return condition_order["H50"], pair, stratum
    return condition_order[str(spec["condition_id"])], int(replicate.rsplit("R", 1)[1]) if "R" in replicate else 0, 0


def load_frozen_run_specs(evidence: Mapping[str, Any], h100_dams: Iterable[str]) -> list[dict[str, Any]]:
    """Return the fixed run order directly from G2A evidence; never select DAMs."""
    _require(evidence.get("artifact_type") == "G2A_EXP11_INDEPENDENT_CONDITION_FEASIBILITY_V0_2_ONLY", "Unexpected EXP-11 evidence artifact")
    _require(evidence.get("retrieval_executed") is False, "Planning evidence must be pre-retrieval")
    conditions = evidence.get("conditions", {})
    expected_counts = {"H25": 10, "H50": 10, "H75": 10}
    specs: list[dict[str, Any]] = []
    for condition, count in expected_counts.items():
        records = conditions.get(condition)
        _require(isinstance(records, list) and len(records) == count, f"Frozen evidence requires {count} {condition} replicates")
        for record in records:
            dam_ids = list(record.get("dam_ids", []))
            _require(record.get("condition") == condition and record.get("complete_dams_valid") is True, f"Invalid frozen {condition} record")
            _require(len(dam_ids) == len(set(dam_ids)) and bool(dam_ids), f"Frozen {condition} DAM list is invalid")
            _require(_dam_set_hash(dam_ids) == record.get("composition_sha256"), f"Frozen {condition} composition_sha256 mismatch")
            specs.append(
                {
                    "run_id": str(record["replicate_id"]),
                    "condition_id": condition,
                    "nominal_condition": condition,
                    "replicate_id": str(record["replicate_id"]),
                    "seed": record.get("seed"),
                    "pair_id": record.get("pair_id", ""),
                    "dominant_stratum": record.get("dominant_stratum", ""),
                    "dam_ids": dam_ids,
                    "composition_sha256": str(record["composition_sha256"]),
                    "expected_rows": int(record["rows"]),
                    "expected_dam_count": int(record["dam_count"]),
                    "frozen_descriptors": {
                        "dam_hhi": record["dam_hhi"],
                        "effective_dam": record["effective_dam"],
                        "nandina_coverage": record["nandina_coverage"],
                        "historical_support_summary": record["independent_dam_support_summary"],
                    },
                }
            )
    h100_ids = sorted(h100_dams)
    specs.append(
        {
            "run_id": "H100_REEXECUTED_CHECK",
            "condition_id": "H100",
            "nominal_condition": "H100",
            "replicate_id": "H100_REFERENCE",
            "seed": None,
            "pair_id": "",
            "dominant_stratum": "",
            "dam_ids": h100_ids,
            "composition_sha256": _dam_set_hash(h100_ids),
            "expected_rows": 2950,
            "expected_dam_count": len(h100_ids),
            "frozen_descriptors": {},
        }
    )
    specs.sort(key=_spec_sort_key)
    h50 = [spec for spec in specs if spec["condition_id"] == "H50"]
    _require(len(h50) == 10 and sum(spec["dominant_stratum"] == "D1" for spec in h50) == 5 and sum(spec["dominant_stratum"] == "D2" for spec in h50) == 5, "H50 must retain five D1 and five D2 runs")
    pairs = defaultdict(list)
    for spec in h50:
        pairs[str(spec["pair_id"])].append(spec)
    _require(len(pairs) == 5 and all({item["dominant_stratum"] for item in pair} == {"D1", "D2"} and len({item["seed"] for item in pair}) == 1 for pair in pairs.values()), "H50 paired seeds are not frozen correctly")
    d1_seeds = [
        next(item["seed"] for item in pair if item["dominant_stratum"] == "D1")
        for pair in sorted(pairs.values(), key=lambda pair: pair[0]["pair_id"])
    ]
    _require(d1_seeds == [20261001, 20261002, 20261003, 20261004, 20261005], "H50 paired seed schedule differs from frozen evidence")
    return specs


def _subset_rows(source_rows: Sequence[Mapping[str, str]], spec: Mapping[str, Any]) -> list[dict[str, str]]:
    selected = set(spec["dam_ids"])
    rows = [dict(row) for row in source_rows if historical._clean(row.get(DAM_COLUMN)) in selected]
    actual_dams = {historical._clean(row.get(DAM_COLUMN)) for row in rows}
    _require(actual_dams == selected, f"{spec['run_id']} missing or extra DAM rows")
    _require(len(rows) == int(spec["expected_rows"]), f"{spec['run_id']} row count differs from frozen evidence")
    _require(len(actual_dams) == int(spec["expected_dam_count"]), f"{spec['run_id']} DAM count differs from frozen evidence")
    _require(_dam_set_hash(actual_dams) == spec["composition_sha256"], f"{spec['run_id']} composition SHA differs from frozen evidence")
    return rows


def _support_by_code(rows: Sequence[Mapping[str, str]]) -> tuple[Counter[str], dict[str, set[str]]]:
    counts: Counter[str] = Counter()
    dams: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        code = historical._clean(row.get(LABEL_COLUMN))
        dam = historical._clean(row.get(DAM_COLUMN))
        counts[code] += 1
        dams[code].add(dam)
    return counts, dams


def _bank_descriptors(rows: Sequence[Mapping[str, str]], reference_codes: set[str]) -> dict[str, Any]:
    dam_counts = Counter(historical._clean(row.get(DAM_COLUMN)) for row in rows)
    code_counts, code_dams = _support_by_code(rows)
    total = len(rows)
    hhi = sum((count / total) ** 2 for count in dam_counts.values()) if total else 0.0
    support_counts = [len(dams) for dams in code_dams.values()]
    histogram = Counter(support_counts)
    return {
        "dam_hhi": hhi,
        "effective_dam": 1 / hhi if hhi else 0.0,
        "nandina_coverage": {
            "covered_codes": len(code_counts),
            "reference_codes": len(reference_codes),
            "fraction": len(code_counts) / len(reference_codes) if reference_codes else 0.0,
        },
        "historical_support_summary": {
            "supported_codes": len(support_counts),
            "minimum_dams_per_nandina": min(support_counts) if support_counts else 0,
            "maximum_dams_per_nandina": max(support_counts) if support_counts else 0,
            "mean_dams_per_nandina": statistics.fmean(support_counts) if support_counts else 0.0,
            "code_count_by_independent_dam_support": {str(key): histogram[key] for key in sorted(histogram)},
        },
    }


def _ordered_fields(rows: Sequence[Mapping[str, Any]]) -> list[str]:
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    return fields


def _duplicate_audit(subset_rows: Sequence[Mapping[str, str]], eval_rows: Sequence[Mapping[str, str]], run_id: str) -> dict[str, Any]:
    historical_frame = pd.DataFrame(subset_rows)
    eval_frame = pd.DataFrame(eval_rows)
    exact, _ = exact_duplicate_audit(historical_frame, eval_frame, "historico-evaluacion")
    near, _ = near_duplicate_audit(historical_frame, eval_frame, "historico-evaluacion")
    normalized = [normalize_text(row.get(QUERY_COLUMN, "")) for row in subset_rows]
    counts = Counter(value for value in normalized if value)
    internal_rows = sum(value for value in counts.values() if value > 1)
    internal_pairs = sum(value * (value - 1) // 2 for value in counts.values() if value > 1)
    by_threshold = {float(row["threshold"]): row for row in near}
    output = {
        "run_id": run_id,
        "internal_exact_duplicates": internal_rows,
        "internal_exact_duplicate_pairs": internal_pairs,
        "hist_eval_exact_matches": int(exact["affected_rows"]),
        "hist_eval_exact_match_rate": float(exact["affected_rows"] / len(eval_rows)) if eval_rows else 0.0,
    }
    for threshold, name in ((0.90, "090"), (0.95, "095"), (0.98, "098")):
        row = by_threshold[threshold]
        output[f"hist_eval_near_{name}"] = int(row["affected_rows"])
        output[f"hist_eval_near_{name}_rate"] = float(row["affected_rows"] / len(eval_rows)) if eval_rows else 0.0
        output[f"hist_eval_near_{name}_pairs"] = int(row["pairs"])
    return output


def _hierarchy_category(reference: str, top1: str) -> str:
    family = historical._top1_error_family(reference, top1)
    return {
        "same_sub_partida_6d": "same_HS6",
        "same_partida_4d": "same_HS4",
        "same_chapter_2d": "same_chapter",
        "different_chapter": "different_chapter",
        "no_candidate": "no_candidate",
    }[family]


def _run_bm25(spec: Mapping[str, Any], subset: Sequence[Mapping[str, str]], eval_rows: Sequence[Mapping[str, str]]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    index = historical._build_bm25_index(subset)
    support_counts, support_dams = _support_by_code(subset)
    historical_by_case = {historical._clean(row.get("case_id")): row for row in subset}
    case_rows: list[dict[str, Any]] = []
    metric_counts = {f"Top{k}_correct_count": 0 for k in K_VALUES}
    error_counts: Counter[str] = Counter()
    mrr_total = 0.0
    for eval_row in eval_rows:
        query = historical._clean(eval_row.get(QUERY_COLUMN))
        reference = historical._clean(eval_row.get(LABEL_COLUMN))
        scores = historical._bm25_scores(query, index, k1=1.5, b=0.75)
        candidates = historical._dedup_candidates(scores, subset, len(subset), 100)
        rank = historical._rank_of(candidates, reference)
        top_codes = [historical._clean(item.get("candidate_nandina")) for item in candidates]
        top1 = top_codes[0] if top_codes else ""
        for k in K_VALUES:
            metric_counts[f"Top{k}_correct_count"] += int(0 < rank <= k)
        mrr_total += historical.mrr_from_rank(rank)
        category = "correct" if rank == 1 else _hierarchy_category(reference, top1)
        if category != "correct":
            error_counts[category] += 1
        best = candidates[0] if candidates else {}
        best_case = historical._clean(best.get("candidate_case_id"))
        best_dam = historical._clean(historical_by_case.get(best_case, {}).get(DAM_COLUMN))
        case_rows.append(
            {
                "run_id": spec["run_id"],
                "condition_id": spec["condition_id"],
                "nominal_condition": spec["nominal_condition"],
                "replicate_id": spec["replicate_id"],
                "seed": spec["seed"] if spec["seed"] is not None else "",
                "dominant_stratum": spec["dominant_stratum"],
                "case_id": historical._clean(eval_row.get("case_id")),
                "reference_nandina": reference,
                "reference_rank": rank,
                "top1_candidate": top1,
                "top3_candidates": json.dumps(top_codes[:3]),
                "top5_candidates": json.dumps(top_codes[:5]),
                "top10_candidates": json.dumps(top_codes[:10]),
                "top50_contains_reference": int(0 < rank <= 50),
                "top1_correct": int(rank == 1),
                "top3_correct": int(0 < rank <= 3),
                "top5_correct": int(0 < rank <= 5),
                "top10_correct": int(0 < rank <= 10),
                "top50_correct": int(0 < rank <= 50),
                "best_historical_precedent": best_case,
                "best_precedent_DAM": best_dam,
                "reference_nandina_supported_in_bank": int(reference in support_counts),
                "reference_independent_dam_support_count": len(support_dams.get(reference, set())),
                "hierarchical_error_category": category,
            }
        )
    n_eval = len(eval_rows)
    metrics: dict[str, Any] = {
        "run_id": spec["run_id"],
        "condition_id": spec["condition_id"],
        "replicate_id": spec["replicate_id"],
        "seed": spec["seed"] if spec["seed"] is not None else "",
        "dominant_stratum": spec["dominant_stratum"],
        "n_eval": n_eval,
        "ranking_depth": 100,
        "bm25_k1": 1.5,
        "bm25_b": 0.75,
        **metric_counts,
        "MRR": mrr_total / n_eval if n_eval else 0.0,
        "same_HS6_errors": error_counts["same_HS6"],
        "same_HS4_errors": error_counts["same_HS4"],
        "same_chapter_errors": error_counts["same_chapter"],
        "different_chapter_errors": error_counts["different_chapter"],
        "no_candidate_errors": error_counts["no_candidate"],
        "reference_supported_cases": sum(int(row["reference_nandina_supported_in_bank"]) for row in case_rows),
        "reference_independent_dam_support_mean": statistics.fmean(int(row["reference_independent_dam_support_count"]) for row in case_rows),
    }
    for k in K_VALUES:
        metrics[f"Top{k}"] = metrics[f"Top{k}_correct_count"] / n_eval if n_eval else 0.0
    return metrics, case_rows


def _condition_summary(rows: Sequence[Mapping[str, Any]], condition: str, scope: str = "PRIMARY") -> dict[str, Any]:
    _require(bool(rows), f"No runs available for {condition}")
    output: dict[str, Any] = {"condition": condition, "aggregation_scope": scope, "replicate_count": len(rows)}
    for metric in ("Top1", "Top3", "Top5", "Top10", "Top50", "MRR"):
        values = [float(row[metric]) for row in rows]
        output.update(
            {
                f"{metric}_mean": statistics.fmean(values),
                f"{metric}_sd": statistics.stdev(values) if len(values) > 1 else "NOT_APPLICABLE",
                f"{metric}_median": statistics.median(values),
                f"{metric}_min": min(values),
                f"{metric}_max": max(values),
            }
        )
    output["mean_rows"] = statistics.fmean(float(row["realized_rows"]) for row in rows)
    output["mean_dam_hhi"] = statistics.fmean(float(row["DAM_HHI"]) for row in rows)
    output["mean_effective_dam"] = statistics.fmean(float(row["effective_DAM"]) for row in rows)
    output["mean_nandina_coverage"] = statistics.fmean(float(row["NANDINA_coverage"]) for row in rows)
    return output


def _learning_row(summary: Mapping[str, Any], nominal_fraction: float) -> dict[str, Any]:
    row = {
        "condition": summary["condition"],
        "nominal_fraction": nominal_fraction,
        "mean_realized_rows": summary["mean_rows"],
        "mean_realized_fraction": float(summary["mean_rows"]) / 2950,
        "replicate_count": summary["replicate_count"],
        "mean_DAM_HHI": summary["mean_dam_hhi"],
        "mean_effective_DAM": summary["mean_effective_dam"],
        "mean_NANDINA_coverage": summary["mean_nandina_coverage"],
    }
    for metric in ("Top1", "Top3", "Top5", "Top10", "Top50", "MRR"):
        row[f"{metric}_mean"] = summary[f"{metric}_mean"]
        row[f"{metric}_sd"] = summary[f"{metric}_sd"]
    return row


def _load_frozen_h100_reference(root: Path) -> dict[str, Any]:
    reference_path = root / DEFAULT_H100_REFERENCE
    reference_relative = _rel(reference_path, root)
    _require(_git(root, "ls-files", "--error-unmatch", "--", reference_relative) == reference_relative, "Frozen H100 metrics reference is not tracked")
    _require(not _git(root, "diff", "--name-only", BASE_MAIN_COMMIT, "--", reference_relative), "Frozen H100 metrics reference differs from the scientific base")
    payload = _read_json(reference_path)
    inputs = payload.get("inputs", {})
    parameters = payload.get("parameters", {})
    _require(payload.get("version") == "v0.2", "Frozen H100 metrics reference version differs")
    _require(payload.get("experiment_id") == "exp04_phase_a_historical_bm25_v0.2", "Frozen H100 metrics reference experiment differs")
    _require(inputs.get("historical_sha256") == H100_SHA256, "Frozen H100 metrics reference historical SHA differs")
    _require(inputs.get("evalset_sha256") == EVAL_SHA256, "Frozen H100 metrics reference eval SHA differs")
    _require(parameters.get("history_depth") == 2950 and parameters.get("candidate_depth") == 100, "Frozen H100 depth parameters differ")
    _require(parameters.get("k1") == 1.5 and parameters.get("b") == 0.75, "Frozen H100 BM25 parameters differ")
    frozen_metrics = payload.get("metrics", {})
    return {
        "path": reference_relative,
        "git_base": BASE_MAIN_COMMIT,
        "metrics": {
            output_name: frozen_metrics[source_name]
            for output_name, _actual_name, source_name in H100_COMPARISON_FIELDS
        },
    }


def _actual_h100_metrics(metrics: Mapping[str, Any]) -> dict[str, Any]:
    return {
        output_name: metrics[actual_name]
        for output_name, actual_name, _source_name in H100_COMPARISON_FIELDS
    }


def _frozen_h100_pass(metrics: Mapping[str, Any], frozen_metrics: Mapping[str, Any]) -> dict[str, Any]:
    comparisons: dict[str, Any] = {}
    passed = True
    for output_name, actual_name, _source_name in H100_COMPARISON_FIELDS:
        expected = frozen_metrics[output_name]
        actual = metrics[actual_name]
        tolerance = H100_MRR_ABS_TOLERANCE if output_name == "MRR" else 0
        absolute_delta = abs(float(actual) - float(expected))
        match = actual == expected if output_name != "MRR" else math.isclose(float(actual), float(expected), rel_tol=0.0, abs_tol=H100_MRR_ABS_TOLERANCE)
        comparisons[output_name] = {"expected": expected, "actual": actual, "absolute_delta": absolute_delta, "tolerance": tolerance, "match": match}
        passed = passed and match
    return {"status": "PASS" if passed else "FAILED", "comparisons": comparisons}


def build_preflight(root: Path, config_path: Path, evidence_path: Path, gate_path: Path, historical_path: Path, eval_path: Path, output_dir: Path) -> dict[str, Any]:
    config = _read_json(config_path)
    evidence = _read_json(evidence_path)
    gate = _read_json(gate_path)
    exp12 = _read_json(root / "src/configs/exp12_historical_diversity_control_v0.3.json")
    _validate_execution_contract(config, gate, exp12)
    _require(sha256_file(historical_path) == H100_SHA256, "H100 SHA256 mismatch")
    _require(sha256_file(eval_path) == EVAL_SHA256, "Eval SHA256 mismatch")
    frozen_h100_reference = _load_frozen_h100_reference(root)
    historical_rows = historical._read_csv(historical_path)
    eval_rows = historical._read_csv(eval_path)
    _require(len(historical_rows) == 2950 and len(eval_rows) == 1056, "Frozen input row count mismatch")
    grouped = _source_by_dam(historical_rows)
    specs = load_frozen_run_specs(evidence, grouped)
    eval_dams = {historical._clean(row.get(DAM_COLUMN)) for row in eval_rows}
    _require(not (set(grouped) & eval_dams), "H100/eval DAM overlap detected")
    for spec in specs:
        subset = _subset_rows(historical_rows, spec)
        _require(not ({historical._clean(row.get(DAM_COLUMN)) for row in subset} & eval_dams), f"{spec['run_id']} has eval DAM overlap")
    expected_output = (root / DEFAULT_OUTPUT).resolve()
    _require(output_dir.resolve() == expected_output, "EXP-11A outputs must use the authorized experiment directory")
    if output_dir.exists():
        _require(not any(output_dir.iterdir()), "EXP-11A output directory must be empty before execution")
    return {
        "experiment_id": EXPERIMENT_ID,
        "status": "PASS",
        "git": _validate_git_state(root),
        "input_sha256": {"h100": H100_SHA256, "eval": EVAL_SHA256},
        "input_rows": {"h100": len(historical_rows), "eval": len(eval_rows), "h100_dams": len(grouped)},
        "run_counts": {"H25": 10, "H50": 10, "H75": 10, "H100": 1, "variable_runs": 30},
        "h50": {"D1": 5, "D2": 5, "paired_seeds": [20261001, 20261002, 20261003, 20261004, 20261005]},
        "outputs": _rel(output_dir, root),
        "frozen_h100_reference": frozen_h100_reference,
        "frozen_execution_order": [spec["run_id"] for spec in specs],
    }


def _artifact_hash_rows(output_dir: Path, root: Path) -> list[dict[str, Any]]:
    inventory = output_dir / "exp11_artifact_hashes.csv"
    rows = []
    for path in sorted(item for item in output_dir.rglob("*") if item.is_file() and item != inventory):
        rows.append({"artifact": _rel(path, root), "sha256": sha256_file(path), "size_bytes": path.stat().st_size, "role": "EXP11A_SCIENTIFIC_OUTPUT"})
    rows.append({"artifact": _rel(inventory, root), "sha256": "SELF_EXCLUDED_TO_AVOID_RECURSIVE_DIGEST", "size_bytes": "NOT_APPLICABLE", "role": "HASH_INVENTORY"})
    return rows


def _findings_text(condition_rows: Sequence[Mapping[str, Any]], h50_rows: Sequence[Mapping[str, Any]], metrics: Sequence[Mapping[str, Any]]) -> str:
    by_condition: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in metrics:
        by_condition[str(row["condition_id"])].append(row)
    lines = [
        "# EXP-11A Findings",
        "",
        "Status: DESCRIPTIVE_PRE_EXTERNAL_AUDIT.",
        "",
        "Scientific interpretation: Sensitivity of historical retrieval performance to nominal historical bank size under complete-DAM sampling and the composition constraints of the frozen H100 bank.",
        "",
        "No causal claim about bank size or H50 dominant stratum is made here.",
        "",
        "## Condition Descriptions",
        "",
    ]
    for condition in ("H25", "H50", "H75", "H100"):
        rows = by_condition[condition]
        top3 = [float(row["Top3"]) for row in rows]
        mrr = [float(row["MRR"]) for row in rows]
        lines.append(f"- {condition}: Top-3 range {min(top3):.6f}-{max(top3):.6f}; MRR range {min(mrr):.6f}-{max(mrr):.6f}.")
    lines.extend(["", "## H50 Diagnostic", ""])
    for stratum in ("D1", "D2"):
        rows = [row for row in h50_rows if row["dominant_stratum"] == stratum]
        lines.append(f"- H50-{stratum}: {len(rows)} runs; Top-3 mean {statistics.fmean(float(row['Top3']) for row in rows):.6f}; MRR mean {statistics.fmean(float(row['MRR']) for row in rows):.6f}.")
    lines.extend(["", "The H50 stratum comparison is descriptive only. No hypothesis decision, inference, causal attribution, or thesis conclusion is declared."])
    return "\n".join(lines)


def run_h100_check_only(preflight: Mapping[str, Any], root: Path, historical_path: Path, eval_path: Path, evidence_path: Path, output_dir: Path) -> dict[str, Any]:
    """Revalidate H100 only and persist the audit before a fail-closed raise."""
    _require(preflight.get("status") == "PASS", "EXP-11A preflight did not pass")
    output_dir.mkdir(parents=True, exist_ok=False)
    for name in ("conditions", "runs", "logs", "audit"):
        (output_dir / name).mkdir()
    started = datetime.now(timezone.utc)
    _write_json(
        output_dir / "audit" / "attempt02_start.json",
        {
            "attempt_id": "H100_ATTEMPT_02",
            "execution_commit": preflight["git"]["commit"],
            "EXP11A_H100_ATTEMPT_02_STARTED_AT": started.isoformat(),
            "EXP11_RETRIEVAL_STARTED": True,
            "variable_runs_executed": 0,
        },
    )
    frozen_reference = _load_frozen_h100_reference(root)
    historical_rows = historical._read_csv(historical_path)
    eval_rows = historical._read_csv(eval_path)
    specs = load_frozen_run_specs(_read_json(evidence_path), _source_by_dam(historical_rows))
    h100_spec = specs[0]
    _require(h100_spec["run_id"] == "H100_REEXECUTED_CHECK", "H100 must be the only first attempt-02 spec")
    subset = _subset_rows(historical_rows, h100_spec)
    _write_csv(output_dir / "conditions" / "H100_REEXECUTED_CHECK.csv", subset, list(historical_rows[0]))
    actual_metrics, _case_rows = _run_bm25(h100_spec, subset, eval_rows)
    comparison = _frozen_h100_pass(actual_metrics, frozen_reference["metrics"])
    ended = datetime.now(timezone.utc)
    audit = {
        "attempt_id": "H100_ATTEMPT_02",
        "execution_commit": preflight["git"]["commit"],
        "timestamp_start_utc": started.isoformat(),
        "timestamp_end_utc": ended.isoformat(),
        "frozen_reference_path": frozen_reference["path"],
        "frozen_reference_git_base": frozen_reference["git_base"],
        "frozen": frozen_reference["metrics"],
        "actual": _actual_h100_metrics(actual_metrics),
        "comparison": comparison["comparisons"],
        "status": comparison["status"],
        "H25_runs_executed": 0,
        "H50_runs_executed": 0,
        "H75_runs_executed": 0,
        "EXP11A_VARIABLE_RUNS_EXECUTED": 0,
    }
    _write_json(output_dir / "audit" / "h100_validity_check.json", audit)
    _write_text(
        output_dir / "logs" / "exp11_execution_log.txt",
        "\n".join((
            f"EXP11A_H100_ATTEMPT_02_STARTED_AT={started.isoformat()}",
            f"EXP11A_H100_ATTEMPT_02_ENDED_AT={ended.isoformat()}",
            f"git_commit={preflight['git']['commit']}",
            f"H100_REVALIDATION={comparison['status']}",
            "EXP11A_VARIABLE_RUNS_EXECUTED=0",
        )),
    )
    _require(comparison["status"] == "PASS", "EXP11A_VALIDITY_GATE = FAILED: H100 re-executed check differs from frozen baseline")
    return audit


def execute(preflight: Mapping[str, Any], root: Path, historical_path: Path, eval_path: Path, evidence_path: Path, output_dir: Path) -> dict[str, Any]:
    _require(preflight.get("status") == "PASS", "EXP-11A preflight did not pass")
    output_dir.mkdir(parents=True, exist_ok=False)
    for name in ("conditions", "runs", "logs", "audit"):
        (output_dir / name).mkdir()
    started = datetime.now(timezone.utc)
    historical_rows = historical._read_csv(historical_path)
    eval_rows = historical._read_csv(eval_path)
    evidence = _read_json(evidence_path)
    frozen_h100_reference = _load_frozen_h100_reference(root)
    specs = load_frozen_run_specs(evidence, _source_by_dam(historical_rows))
    reference_codes = {historical._clean(row.get(LABEL_COLUMN)) for row in historical_rows}
    fields = list(historical_rows[0])
    condition_records: list[dict[str, Any]] = []
    metrics_rows: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []
    duplicate_rows: list[dict[str, Any]] = []
    run_entries: list[dict[str, Any]] = []
    execution_log = [f"EXP11_RETRIEVAL_STARTED_AT={started.isoformat()}", f"git_commit={preflight['git']['commit']}", "execution_order=" + ",".join(preflight["frozen_execution_order"])]
    for index, spec in enumerate(specs, start=1):
        subset = _subset_rows(historical_rows, spec)
        subset_path = output_dir / "conditions" / f"{spec['run_id']}.csv"
        _write_csv(subset_path, subset, fields)
        subset_sha = sha256_file(subset_path)
        descriptors = _bank_descriptors(subset, reference_codes)
        frozen = spec.get("frozen_descriptors") or {}
        if frozen:
            _require(math.isclose(descriptors["dam_hhi"], float(frozen["dam_hhi"]), rel_tol=0.0, abs_tol=1e-12), f"{spec['run_id']} DAM HHI differs from frozen evidence")
            _require(math.isclose(descriptors["effective_dam"], float(frozen["effective_dam"]), rel_tol=0.0, abs_tol=1e-12), f"{spec['run_id']} effective DAM differs from frozen evidence")
            _require(descriptors["nandina_coverage"] == frozen["nandina_coverage"], f"{spec['run_id']} NANDINA coverage differs from frozen evidence")
        result_metrics, result_cases = _run_bm25(spec, subset, eval_rows)
        if spec["condition_id"] == "H100":
            h100_check = _frozen_h100_pass(result_metrics, frozen_h100_reference["metrics"])
            _require(h100_check["status"] == "PASS", "EXP11A_VALIDITY_GATE = FAILED: H100 re-executed check differs from frozen baseline")
            result_metrics["h100_reexecuted_check"] = "PASS"
        else:
            result_metrics["h100_reexecuted_check"] = "NOT_APPLICABLE"
        duplicate = _duplicate_audit(subset, eval_rows, str(spec["run_id"]))
        result_metrics.update(
            {
                "realized_rows": len(subset),
                "realized_fraction": len(subset) / 2950,
                "DAM_count": len(spec["dam_ids"]),
                "DAM_HHI": descriptors["dam_hhi"],
                "effective_DAM": descriptors["effective_dam"],
                "NANDINA_coverage": descriptors["nandina_coverage"]["fraction"],
                "composition_sha256": spec["composition_sha256"],
                "historical_subset_sha256": subset_sha,
                "eval_sha256": EVAL_SHA256,
                "dam_overlap_count": 0,
            }
        )
        duplicate_rows.append({**duplicate, "condition_id": spec["condition_id"], "replicate_id": spec["replicate_id"]})
        metrics_rows.append(result_metrics)
        case_rows.extend(result_cases)
        condition_records.append(
            {
                "run_id": spec["run_id"], "condition_id": spec["condition_id"], "replicate_id": spec["replicate_id"], "seed": spec["seed"] or "", "dominant_stratum": spec["dominant_stratum"],
                "rows": len(subset), "DAM_count": len(spec["dam_ids"]), "DAM_list": json.dumps(spec["dam_ids"]), "composition_sha256": spec["composition_sha256"], "historical_subset_sha256": subset_sha,
                "DAM_HHI": descriptors["dam_hhi"], "effective_DAM": descriptors["effective_dam"], "NANDINA_coverage": descriptors["nandina_coverage"]["fraction"],
                "dominant_structure": spec["dominant_stratum"] or "H100_ALL_DAMS", "historical_support_summary": json.dumps(descriptors["historical_support_summary"], sort_keys=True),
            }
        )
        run_path = output_dir / "runs" / f"{spec['run_id']}.json"
        run_payload = {"run": condition_records[-1], "metrics": result_metrics, "duplicate_nearduplicate_audit": duplicate, "execution_commit": preflight["git"]["commit"]}
        _write_json(run_path, run_payload)
        run_entries.append({**condition_records[-1], "output_path": _rel(run_path, root), "output_sha256": sha256_file(run_path), "selection_algorithm": "FROZEN_EVIDENCE_V0_2_NO_RESELECTION", "selection_used_eval_performance": False, "bm25": {"k1": 1.5, "b": 0.75, "ranking_depth": 100}})
        execution_log.append(f"{index:02d}/{len(specs)} {spec['run_id']} completed")
    ended = datetime.now(timezone.utc)
    by_condition = {condition: [row for row in metrics_rows if row["condition_id"] == condition] for condition in ALLOWED_CONDITIONS}
    condition_summaries = [_condition_summary(by_condition[condition], condition) for condition in ("H25", "H50", "H75")]
    h100 = by_condition["H100"][0]
    h100_summary = {"condition": "H100", "aggregation_scope": "FROZEN_REFERENCE", "replicate_count": 1, "mean_rows": h100["realized_rows"], "mean_dam_hhi": h100["DAM_HHI"], "mean_effective_dam": h100["effective_DAM"], "mean_nandina_coverage": h100["NANDINA_coverage"]}
    for metric in ("Top1", "Top3", "Top5", "Top10", "Top50", "MRR"):
        h100_summary.update({f"{metric}_mean": h100[metric], f"{metric}_sd": "NOT_APPLICABLE", f"{metric}_median": h100[metric], f"{metric}_min": h100[metric], f"{metric}_max": h100[metric]})
    condition_summaries.append(h100_summary)
    h50_rows = by_condition["H50"]
    condition_summaries.extend(_condition_summary([row for row in h50_rows if row["dominant_stratum"] == stratum], "H50", f"H50_{stratum}_DIAGNOSTIC") for stratum in ("D1", "D2"))
    learning = [_learning_row(next(row for row in condition_summaries if row["condition"] == condition and row["aggregation_scope"] in {"PRIMARY", "FROZEN_REFERENCE"}), fraction) for condition, fraction in (("H25", 0.25), ("H50", 0.5), ("H75", 0.75), ("H100", 1.0))]
    outputs = {
        "conditions": output_dir / "exp11_conditions.csv",
        "metrics_by_run": output_dir / "exp11_metrics_by_run.csv",
        "metrics_by_condition": output_dir / "exp11_metrics_by_condition.csv",
        "case_level": output_dir / "exp11_case_level_ranks.csv",
        "bank_composition": output_dir / "exp11_bank_composition_by_run.csv",
        "duplicates": output_dir / "exp11_duplicate_nearduplicate_audit.csv",
        "learning_curve": output_dir / "exp11_learning_curve.csv",
        "findings": output_dir / "exp11_findings.md",
        "execution_log": output_dir / "exp11_execution_log.txt",
        "manifest": output_dir / "exp11_run_manifest.json",
        "hashes": output_dir / "exp11_artifact_hashes.csv",
    }
    _write_csv(outputs["conditions"], condition_records, list(condition_records[0]))
    _write_csv(outputs["metrics_by_run"], metrics_rows, list(metrics_rows[0]))
    _write_csv(outputs["metrics_by_condition"], condition_summaries, _ordered_fields(condition_summaries))
    _write_csv(outputs["case_level"], case_rows, list(case_rows[0]))
    _write_csv(outputs["bank_composition"], condition_records, list(condition_records[0]))
    _write_csv(outputs["duplicates"], duplicate_rows, list(duplicate_rows[0]))
    _write_csv(outputs["learning_curve"], learning, list(learning[0]))
    _write_text(outputs["findings"], _findings_text(condition_summaries, h50_rows, metrics_rows))
    execution_log.append(f"timestamp_utc_end={ended.isoformat()}")
    _write_text(outputs["execution_log"], "\n".join(execution_log))
    manifest = {
        "experiment_id": EXPERIMENT_ID,
        "experiment_version": EXPERIMENT_VERSION,
        "EXP11A_EXECUTION_COMMIT_SHA": preflight["git"]["commit"],
        "main_base_commit": BASE_MAIN_COMMIT,
        "timestamp_start": started.isoformat(),
        "timestamp_end": ended.isoformat(),
        "runtime": {"python": platform.python_version(), "os": platform.platform(), "architecture": platform.machine(), "packages": {package: importlib.metadata.version(package) for package in ("numpy", "pandas")}},
        "inputs": {"h100_path": _rel(historical_path, root), "h100_sha256": H100_SHA256, "eval_path": _rel(eval_path, root), "eval_sha256": EVAL_SHA256},
        "preflight": preflight,
        "h100_reexecuted_check": _frozen_h100_pass(h100, frozen_h100_reference["metrics"]),
        "runs": run_entries,
        "outputs": {name: _rel(path, root) for name, path in outputs.items()},
        "EXP11_RETRIEVAL_STARTED": True,
        "EXP11A_EXECUTION_COMPLETED": True,
        "SCIENTIFIC_INTERPRETATION": "SENSITIVITY_TO_HISTORICAL_BANK_SIZE_UNDER_NATURAL_COMPOSITION_CONSTRAINTS",
    }
    _write_json(outputs["manifest"], manifest)
    _write_csv(outputs["hashes"], _artifact_hash_rows(output_dir, root), ["artifact", "sha256", "size_bytes", "role"])
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the frozen EXP-11A historical BM25 size-sensitivity protocol.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true", help="Validate only; do not run retrieval or create outputs.")
    mode.add_argument("--h100-check-only", action="store_true", help="Run and persist only the H100 revalidation; never start variable runs.")
    mode.add_argument("--execute", action="store_true", help="Run H100 check followed by the 30 frozen variable compositions.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--evidence", default=str(DEFAULT_EVIDENCE))
    parser.add_argument("--gate", default=str(DEFAULT_GATE))
    parser.add_argument("--historical", default=str(DEFAULT_HISTORICAL))
    parser.add_argument("--eval", default=str(DEFAULT_EVAL))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = project_root()
    preflight = build_preflight(
        root,
        resolve_project_path(args.config),
        resolve_project_path(args.evidence),
        resolve_project_path(args.gate),
        resolve_project_path(args.historical),
        resolve_project_path(args.eval),
        resolve_project_path(args.output_dir),
    )
    if args.preflight:
        print(json.dumps(preflight, ensure_ascii=False, indent=2))
        return 0
    if args.h100_check_only:
        audit = run_h100_check_only(preflight, root, resolve_project_path(args.historical), resolve_project_path(args.eval), resolve_project_path(args.evidence), resolve_project_path(args.output_dir))
        print(f"OK: H100 revalidation {audit['status']} at {audit['timestamp_end_utc']}")
        return 0
    manifest = execute(preflight, root, resolve_project_path(args.historical), resolve_project_path(args.eval), resolve_project_path(args.evidence), resolve_project_path(args.output_dir))
    print(f"OK: EXP-11A completed at {manifest['timestamp_end']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
