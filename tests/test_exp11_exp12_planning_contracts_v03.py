"""Synthetic tests for the frozen pre-retrieval EXP-11/EXP-12 contracts."""

from __future__ import annotations

import inspect
import json
from pathlib import Path
import unittest

from src.experiments.plan_historical_bank_conditions_v03 import (
    EXP11_MAX_ABS_ROW_DEVIATION,
    EXP11_REQUIRED_DOMINANT_COUNTS,
    EXP11_TARGET_ROWS,
    EXP12_CANDIDATE_COUNT,
    EXP12_MAX_ROWS,
    EXP12_MINIMUM_UNIQUE_FEASIBLE,
    EXP12_MIN_ROWS,
    Exp12Candidate,
    accepted_exp11_h50_paired_seeds,
    accepted_exp11_independent_schedules,
    assert_expanded_historical_gate,
    dam_concentration_metrics,
    generate_exp12_candidates,
    select_exp12_conditions,
    select_exp11_independent_condition,
    total_variation_distance,
    validate_exp11_contract,
    validate_exp12_contract,
    validate_manifest_fields,
)


ROOT = Path(__file__).resolve().parents[1]


def load_config(name: str) -> dict[str, object]:
    return json.loads((ROOT / "src" / "configs" / name).read_text(encoding="utf-8"))


def exp11_fixture() -> dict[str, int]:
    rows = {f"DAM-{index:02d}": 35 for index in range(25)}
    rows["DAM-25"] = 90
    rows["DOM-1"] = 1045
    rows["DOM-2"] = 940
    return rows


def exp12_fixture() -> tuple[dict[str, int], dict[str, dict[str, int]], dict[str, int]]:
    rows = {
        "DAM-A": 600, "DAM-B": 600, "DAM-C": 600, "DAM-D": 600,
        "DAM-E": 500, "DAM-F": 500, "DAM-G": 500, "DAM-H": 500,
        "DAM-I": 400, "DAM-J": 400,
    }
    labels = {dam: {"87010000": count // 2, "87020000": count - count // 2} for dam, count in rows.items()}
    return rows, labels, {"87010000": 1475, "87020000": 1475}


class TestExp11Exp12PlanningContractsV03(unittest.TestCase):
    def setUp(self) -> None:
        self.exp11 = load_config("exp11_historical_size_sensitivity_v0.3.json")
        self.exp12 = load_config("exp12_historical_diversity_control_v0.3.json")

    def test_configs_parse_and_validate(self) -> None:
        validate_exp11_contract(self.exp11)
        validate_exp12_contract(self.exp12)

    def test_exp11_targets_and_integer_tolerance_are_frozen(self) -> None:
        self.assertEqual(EXP11_TARGET_ROWS, {"H25": 738, "H50": 1475, "H75": 2213, "H100": 2950})
        self.assertEqual(EXP11_MAX_ABS_ROW_DEVIATION, 148)
        self.assertEqual(self.exp11["feasibility_contract"]["nominal_target_formula"], "floor(fraction * 2950 + 0.5)")

    def test_exp11_independent_selection_is_complete_dam_and_deterministic(self) -> None:
        rows = exp11_fixture()
        first = select_exp11_independent_condition(rows, "H50", 20261001, ("DOM-1", "DOM-2"))
        second = select_exp11_independent_condition(rows, "H50", 20261001, ("DOM-1", "DOM-2"))
        self.assertEqual(first, second)
        self.assertTrue(first["complete_dams_valid"])
        self.assertTrue(first["valid_seed"])
        self.assertEqual(first["dominant_count"], 1)
        self.assertLessEqual(first["absolute_row_deviation"], EXP11_MAX_ABS_ROW_DEVIATION)

    def test_exp11_acceptance_uses_independent_unique_compositions(self) -> None:
        accepted = accepted_exp11_independent_schedules(exp11_fixture(), required_seeds=10, max_seed_candidates=1000)
        self.assertEqual(accepted["status"], "ACCEPTED")
        for condition, required_dominants in EXP11_REQUIRED_DOMINANT_COUNTS.items():
            records = accepted["by_condition"][condition]["accepted"]
            self.assertEqual(len(records), 10)
            self.assertEqual(len({record["composition_sha256"] for record in records}), 10)
            self.assertTrue(all(record["valid_seed"] for record in records))
            self.assertTrue(all(record["dominant_count"] == required_dominants for record in records))

    def test_exp11_h50_is_deterministic_paired_and_balanced_by_dominant_stratum(self) -> None:
        rows = exp11_fixture()
        first = accepted_exp11_h50_paired_seeds(rows, ("DOM-1", "DOM-2"), required_pairs=5, max_seed_candidates=1000)
        second = accepted_exp11_h50_paired_seeds(rows, ("DOM-1", "DOM-2"), required_pairs=5, max_seed_candidates=1000)
        self.assertEqual(first, second)
        self.assertEqual(first["status"], "ACCEPTED")
        self.assertEqual(len(first["accepted_pairs"]), 5)
        self.assertEqual(len(first["paired_seeds"]), 5)
        by_stratum = {"D1": [], "D2": []}
        for pair in first["accepted_pairs"]:
            self.assertEqual(pair["seed"], pair["D1"]["seed"])
            self.assertEqual(pair["seed"], pair["D2"]["seed"])
            self.assertEqual(pair["D1"]["pair_id"], pair["D2"]["pair_id"])
            for stratum, forced, excluded in (("D1", "DOM-1", "DOM-2"), ("D2", "DOM-2", "DOM-1")):
                record = pair[stratum]
                by_stratum[stratum].append(record)
                self.assertTrue(record["complete_dams_valid"])
                self.assertTrue(record["valid_seed"])
                self.assertEqual(record["dominant_stratum"], stratum)
                self.assertEqual(record["dominant_count"], 1)
                self.assertTrue(record["dominant_1_present"] if stratum == "D1" else record["dominant_2_present"])
                self.assertFalse(record["dominant_2_present"] if stratum == "D1" else record["dominant_1_present"])
                self.assertLessEqual(record["absolute_row_deviation"], EXP11_MAX_ABS_ROW_DEVIATION)
                self.assertIn(forced, record["dam_ids"])
                self.assertNotIn(excluded, record["dam_ids"])
        for records in by_stratum.values():
            self.assertEqual(len({record["composition_sha256"] for record in records}), 5)

    def test_exp11_f008_proof_and_non_nested_design_are_frozen(self) -> None:
        selection = self.exp11["selection"]
        structural = self.exp11["structural_volume_consequences"]
        self.assertEqual(selection["nested_policy"], "NOT_REQUIRED_STRUCTURALLY_INFEASIBLE")
        self.assertEqual(selection["sampling_design"], "INDEPENDENT_COMPLETE_DAM_SUBSETS_BY_CONDITION")
        self.assertEqual(structural["minimum_h75_rows_if_nested_with_h25"], 2575)
        self.assertEqual(structural["h75_maximum_rows"], 2361)
        self.assertGreater(structural["minimum_h75_rows_if_nested_with_h25"], structural["h75_maximum_rows"])

    def test_exp11_h100_is_single_reference_without_label_balancing(self) -> None:
        policy = self.exp11["replicate_policy"]
        self.assertEqual(policy["h100_replicates"], 1)
        self.assertEqual(policy["planning_feasibility"]["nested_design_status"], "STRUCTURALLY_INFEASIBLE_UNDER_FROZEN_GROUP_AND_VOLUME_CONSTRAINTS")
        self.assertEqual(policy["planning_feasibility"]["status"], "FROZEN_APPROVED_FOR_EXP11A")
        self.assertEqual(policy["seed_schedule"], [])
        for condition in ("H25", "H75"):
            schedule = policy[f"accepted_seed_schedule_{condition}"]
            self.assertEqual(len(schedule), 10)
            self.assertEqual(len(set(schedule)), 10)
        self.assertEqual(policy["accepted_paired_seed_schedule_H50"], policy["accepted_seed_schedule_H50_D1"])
        self.assertEqual(policy["accepted_paired_seed_schedule_H50"], policy["accepted_seed_schedule_H50_D2"])
        self.assertEqual(len(policy["accepted_paired_seed_schedule_H50"]), 5)
        self.assertEqual(self.exp11["h50_stratification"]["primary_analysis"], "POOLED_EQUAL_WEIGHT_5_D1_5_D2")
        self.assertEqual(self.exp11["h50_stratification"]["secondary_diagnostic"], "DOMINANT_STRATUM_COMPARISON")
        feasibility = self.exp11["feasibility_contract"]
        self.assertTrue(feasibility["no_label_balancing"])
        self.assertTrue(feasibility["no_nandina_distribution_selection"])
        self.assertTrue(feasibility["no_eval_performance_selection"])

    def test_exp11_g2_findings_record_the_verified_h50_correction(self) -> None:
        findings = self.exp11["g2a_findings"]
        self.assertEqual(findings["F008"]["status"], "VERIFIED_IN_G2")
        self.assertEqual(findings["F009"]["status"], "VERIFIED_IN_G2")
        self.assertEqual(findings["F010"]["status"], "VERIFIED_IN_G2")
        self.assertEqual(findings["F010"]["resolution"], "RESOLVED_PRE_EXECUTION_BY_H50_STRATIFICATION")
        self.assertEqual(findings["F010"]["previous_v0_1_dominant_counts"], {"D1": 2, "D2": 8})
        self.assertEqual(findings["F010"]["final_dominant_counts"], {"D1": 5, "D2": 5})

    def test_exp11_selector_uses_no_eval_or_nandina_fields(self) -> None:
        source = inspect.getsource(select_exp11_independent_condition).lower()
        self.assertNotIn("nandina", source)
        self.assertNotIn("eval", source)
        self.assertNotIn("top_k", source)
        self.assertNotIn("mrr", source)

    def test_exp11_h150_and_h200_remain_fail_closed(self) -> None:
        self.assertEqual(self.exp11["contract_status"], "FROZEN_APPROVED_FOR_EXP11A")
        self.assertTrue(self.exp11["execution_authorized"])
        self.assertEqual(self.exp11["execution_authorized_scope"], "EXP11A_H25_H50_H75_H100_ONLY")
        self.assertTrue(self.exp11["exp11a_execution_authorized"])
        self.assertEqual(self.exp11["authorized_conditions"], ["H25", "H50", "H75", "H100"])
        self.assertFalse(self.exp11["exp11b_execution_authorized"])
        self.assertFalse(self.exp11["expanded_historical_conditions_authorized"])
        for condition in ("H150", "H200"):
            pending = self.exp11["target_conditions"][condition]
            self.assertFalse(pending["enabled"])
            self.assertTrue(pending["fail_closed"])
            self.assertEqual(pending["source"], "PENDING_NEW_HISTORICAL_GATE")
            self.assertIsNone(pending["path"])
            self.assertIsNone(pending["sha256"])

    def test_exp12_hhi_and_derived_metrics_follow_the_frozen_formula(self) -> None:
        metrics = dam_concentration_metrics({"A": 70, "B": 20, "C": 10}, ("A", "B", "C"))
        self.assertEqual(metrics["rows"], 100)
        self.assertAlmostEqual(metrics["hhi"], 0.54)
        self.assertAlmostEqual(metrics["effective_dam"], 1 / 0.54)
        self.assertAlmostEqual(metrics["dominant_dam_share"], 0.7)
        self.assertAlmostEqual(metrics["top2_dam_share"], 0.9)
        self.assertEqual(metrics["dam_count"], 3)

    def test_exp12_tvd_and_h100_label_reference_are_frozen(self) -> None:
        self.assertAlmostEqual(total_variation_distance({"A": 60, "B": 40}, 100, {"A": 50, "B": 50}), 0.1)
        reference = self.exp12["reference_h100"]
        self.assertEqual(reference["rows"], 2950)
        self.assertEqual(reference["sha256"], "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff")
        self.assertEqual(self.exp12["label_control"]["required_label_coverage_fraction"], 1.0)
        self.assertEqual(self.exp12["label_control"]["maximum_tvd"], 0.05)

    def test_exp12_candidate_generation_uses_only_dam_profiles_and_overlap_set(self) -> None:
        rows, labels, reference = exp12_fixture()
        candidates = generate_exp12_candidates(rows, labels, reference, set(), 20262001, candidate_count=300)
        self.assertGreaterEqual(len(candidates), EXP12_MINIMUM_UNIQUE_FEASIBLE)
        self.assertTrue(all(EXP12_MIN_ROWS <= candidate.rows <= EXP12_MAX_ROWS for candidate in candidates))
        self.assertTrue(all(candidate.label_coverage_fraction == 1.0 for candidate in candidates))
        self.assertTrue(all(candidate.tvd <= 0.05 for candidate in candidates))
        source = inspect.getsource(generate_exp12_candidates).lower()
        self.assertNotIn("expected_nandina", source)
        self.assertNotIn("eval_description", source)
        self.assertNotIn("reference_rank", source)
        self.assertNotIn("top_k", source)
        self.assertNotIn("mrr", source)

    def test_exp12_quantiles_are_distinct_and_strictly_ordered(self) -> None:
        candidates = tuple(
            Exp12Candidate(
                candidate_index=index,
                dam_ids=(f"DAM-{index:02d}",),
                rows=2950,
                hhi=0.10 + index * 0.01,
                effective_dam=1 / (0.10 + index * 0.01),
                dominant_dam_share=0.5,
                top2_dam_share=0.75,
                label_coverage_fraction=1.0,
                tvd=0.0,
            )
            for index in range(EXP12_MINIMUM_UNIQUE_FEASIBLE)
        )
        selected = select_exp12_conditions(candidates, 20262001)
        self.assertEqual(set(selected), {"D-LOW", "D-MID", "D-HIGH"})
        self.assertEqual(len({candidate.dam_ids for candidate in selected.values()}), 3)
        self.assertGreater(selected["D-LOW"].hhi, selected["D-MID"].hhi)
        self.assertGreater(selected["D-MID"].hhi, selected["D-HIGH"].hhi)
        self.assertEqual(self.exp12["candidate_generation"]["candidate_count"], EXP12_CANDIDATE_COUNT)

    def test_exp12_fails_closed_for_missing_gate_and_insufficient_candidates(self) -> None:
        with self.assertRaises(ValueError):
            assert_expanded_historical_gate(None)
        with self.assertRaises(ValueError):
            select_exp12_conditions((), 20262001)
        self.assertTrue(self.exp12["sampling_universe"]["fail_closed"])
        self.assertTrue(self.exp12["sampling_universe"]["must_not_fallback_to_h100"])

    def test_exp12_freezes_quantiles_duplicate_method_and_no_weighted_objective(self) -> None:
        self.assertEqual(self.exp12["contract_status"], "CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE")
        self.assertEqual(self.exp12["method_contract"], "CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE")
        self.assertEqual(self.exp12["condition_selection"]["quantiles"], {"D-HIGH": 0.1, "D-MID": 0.5, "D-LOW": 0.9})
        self.assertTrue(self.exp12["selection"]["no_weighted_multiobjective"])
        duplicate = self.exp12["duplicate_measurement"]
        self.assertEqual(duplicate["near_duplicate_method"], "token_jaccard_rare_block")
        self.assertEqual(duplicate["thresholds"], [0.9, 0.95, 0.98])

    def test_exp12_future_manipulation_check_is_fail_closed_without_a_new_threshold(self) -> None:
        check = self.exp12["future_manipulation_check"]
        self.assertEqual(
            set(check["required_reports"]),
            {"HHI_q10", "HHI_q50", "HHI_q90", "HHI_span_q90_q10", "effective_DAM_q10", "effective_DAM_q50", "effective_DAM_q90", "effective_DAM_ratio_high_low"},
        )
        self.assertEqual(check["strict_hhi_order_fail_closed"], "HHI_DLOW > HHI_DMID > HHI_DHIGH")
        self.assertTrue(check["manipulation_strength_review_required"])
        self.assertFalse(check["new_threshold_introduced"])

    def test_manifest_contract_requires_identity_and_selection_fields(self) -> None:
        fields = self.exp11["output_contract"]["manifest_required_fields"]
        valid = {field: "present" for field in fields}
        validate_manifest_fields(valid, fields)
        valid.pop("selection_seed")
        with self.assertRaises(ValueError):
            validate_manifest_fields(valid, fields)


if __name__ == "__main__":
    unittest.main()
