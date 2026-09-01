"""Contract tests for prospective EXP-11B H150/H200 planning."""

from __future__ import annotations

import hashlib
import importlib.util
import inspect
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src/experiments/prepare_exp11b_historical_size_extension_v0.1.py"
CONFIG_PATH = ROOT / "src/configs/exp11b_historical_size_extension_v0.1.json"
EXP11A_CONFIG_PATH = ROOT / "src/configs/exp11_historical_size_sensitivity_v0.3.json"
FEASIBILITY_PATH = ROOT / "outputs/audits/new_historical_gate_v0.1/exp11b_h150_h200_feasibility_v0.1.json"
MASK_PATH = ROOT / "outputs/audits/new_historical_gate_v0.1/eval_common_clean_masks_v0.1.csv"
SPEC = importlib.util.spec_from_file_location("exp11b_planner_v01", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
PLANNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PLANNER)


class Exp11bHistoricalSizeExtensionV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

    def test_01_contract_is_prospective(self) -> None:
        self.assertEqual(self.config["contract_status"], "NEW_HISTORICAL_GATE_03_PROSPECTIVE_DESIGN_ONLY")

    def test_02_execution_is_not_authorized(self) -> None:
        self.assertFalse(self.config["execution_authorized"])
        self.assertFalse(self.config["retrieval_executed"])

    def test_03_h150_and_h200_are_not_materialized(self) -> None:
        self.assertFalse(self.config["conditions"]["H150"]["materialized"])
        self.assertFalse(self.config["conditions"]["H200"]["materialized"])

    def test_04_h100_reference_is_fixed(self) -> None:
        self.assertEqual(self.config["conditions"]["H100"]["frozen_rows"], 2950)
        self.assertEqual(self.config["frozen_datasets"]["H100"]["rows"], 2950)

    def test_05_targets_are_new_row_increments(self) -> None:
        self.assertEqual(self.config["conditions"]["H150"]["target_new_rows"], 1475)
        self.assertEqual(self.config["conditions"]["H200"]["target_new_rows"], 2950)

    def test_06_tolerance_is_contractual(self) -> None:
        self.assertEqual(self.config["feasibility_contract"]["max_abs_new_row_deviation"], 148)

    def test_07_seed_schedule_is_frozen(self) -> None:
        policy = self.config["replicate_policy"]
        self.assertEqual(policy["seed_stream_start"], 20261001)
        self.assertEqual(policy["max_seed_candidates"], 100000)
        self.assertEqual(policy["accepted_replicates"], 10)

    def test_08_selection_input_contract_excludes_descriptions_and_codes(self) -> None:
        self.assertEqual(
            self.config["selection"]["allowed_selection_inputs"],
            ["DAM identifier", "row count per DAM", "seed", "namespace"],
        )
        self.assertFalse(self.config["selection"]["uses_nandina_for_selection"])
        self.assertFalse(self.config["selection"]["uses_description_for_selection"])

    def test_09_selection_excludes_eval_and_duplicate_information(self) -> None:
        selection = self.config["selection"]
        self.assertFalse(selection["uses_eval_labels_for_selection"])
        self.assertFalse(selection["uses_eval_performance_for_selection"])
        self.assertFalse(selection["uses_duplicates_for_selection"])

    def test_10_seeded_order_is_deterministic(self) -> None:
        counts = {"DAM-A": 20, "DAM-B": 30, "DAM-C": 40}
        self.assertEqual(
            PLANNER.seeded_dam_order(counts, 20261001, "EXP11B"),
            PLANNER.seeded_dam_order(counts, 20261001, "EXP11B"),
        )

    def test_11_seeded_order_matches_sha256_contract(self) -> None:
        counts = {"DAM-A": 1, "DAM-B": 1}
        expected = sorted(
            counts,
            key=lambda dam: (hashlib.sha256(f"7:EXP11B:{dam}".encode("utf-8")).hexdigest(), dam),
        )
        self.assertEqual(PLANNER.seeded_dam_order(counts, 7, "EXP11B"), expected)

    def test_12_prefix_uses_complete_dams(self) -> None:
        counts = {"DAM-A": 700, "DAM-B": 800, "DAM-C": 1000}
        selected = PLANNER.choose_complete_dam_prefix(["DAM-A", "DAM-B", "DAM-C"], counts, 1475)
        self.assertEqual(selected["realized_new_rows"], sum(counts[dam] for dam in selected["dams"]))

    def test_13_prefix_tie_breaks_on_fewer_dams(self) -> None:
        counts = {"DAM-A": 100, "DAM-B": 50, "DAM-C": 50}
        selected = PLANNER.choose_complete_dam_prefix(["DAM-A", "DAM-B", "DAM-C"], counts, 150)
        self.assertEqual(selected["dams"], ["DAM-A", "DAM-B"])

    def test_14_h150_is_strict_subset_of_h200_for_prefixes(self) -> None:
        counts = {f"DAM-{index:02d}": 100 for index in range(40)}
        selected = PLANNER.select_nested_prefixes(counts, 20261001, "EXP11B", 1000, 2000)
        self.assertTrue(selected["h150_is_strict_subset_h200"])

    def test_15_composition_hash_is_order_independent(self) -> None:
        self.assertEqual(
            PLANNER.composition_sha256(["DAM-C", "DAM-A", "DAM-B"]),
            PLANNER.composition_sha256(["DAM-A", "DAM-B", "DAM-C"]),
        )

    def test_16_selector_signature_is_dam_count_only(self) -> None:
        source = inspect.getsource(PLANNER.select_nested_prefixes)
        self.assertNotIn("NANDINA", source)
        self.assertNotIn("evaluation", source.lower())
        self.assertNotIn("description", source.lower())

    def test_17_common_clean_masks_are_sensitivity_only(self) -> None:
        mask_contract = self.config["common_clean_mask"]
        self.assertFalse(mask_contract["affects_selection"])
        self.assertFalse(mask_contract["affects_primary_denominator"])
        self.assertEqual(mask_contract["primary_eval_denominator"], 1056)

    def test_18_exp11a_contract_remains_separate(self) -> None:
        exp11a = json.loads(EXP11A_CONFIG_PATH.read_text(encoding="utf-8"))
        self.assertFalse(exp11a["target_conditions"]["H150"]["enabled"])
        self.assertFalse(exp11a["target_conditions"]["H200"]["enabled"])

    def test_19_gate03_artifacts_are_lf_portable(self) -> None:
        attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
        self.assertIn("data/interim/new_historical_gate_v0.1/** text eol=lf", attributes)
        self.assertIn("outputs/audits/new_historical_gate_v0.1/** text eol=lf", attributes)

    def test_20_increment_descriptor_differs_from_total_bank_descriptor(self) -> None:
        h100 = [
            {"DECLARACION": "H100-DAM", "NANDINA": f"{index:08d}"}
            for index in range(66)
        ]
        new_rows = [{"DECLARACION": "NEW-DAM", "NANDINA": "22222222"}]
        h100_codes = {row["NANDINA"] for row in h100}
        increment = PLANNER.increment_descriptor(new_rows, ["NEW-DAM"], h100_codes)
        total = PLANNER.total_bank_descriptor(h100, new_rows, ["NEW-DAM"], h100_codes)
        self.assertEqual(increment["rows"], 1)
        self.assertEqual(total["rows"], 67)
        self.assertNotEqual(increment, total)

    def test_21_total_rows_equal_h100_plus_increment(self) -> None:
        feasibility = json.loads(FEASIBILITY_PATH.read_text(encoding="utf-8"))
        for replicate in feasibility["accepted_replicates"]:
            for condition in ("H150", "H200"):
                bank = replicate[condition]
                self.assertEqual(
                    bank["total_bank_descriptor"]["rows"],
                    2950 + bank["realized_new_rows"],
                )

    def test_22_total_dam_count_uses_disjoint_h100_core(self) -> None:
        feasibility = json.loads(FEASIBILITY_PATH.read_text(encoding="utf-8"))
        self.assertEqual(feasibility["pool"]["direct_h100_new_dam_overlap_count"], 0)
        for replicate in feasibility["accepted_replicates"]:
            for condition in ("H150", "H200"):
                bank = replicate[condition]
                self.assertEqual(
                    bank["total_bank_descriptor"]["dam_count"],
                    28 + bank["increment_descriptor"]["dam_count"],
                )

    def test_23_total_bank_retains_all_h100_codes(self) -> None:
        feasibility = json.loads(FEASIBILITY_PATH.read_text(encoding="utf-8"))
        for replicate in feasibility["accepted_replicates"]:
            for condition in ("H150", "H200"):
                descriptor = replicate[condition]["total_bank_descriptor"]
                self.assertEqual(descriptor["H100_nandina_coverage_n"], 66)
                self.assertEqual(descriptor["H100_nandina_coverage_denominator"], 66)
                self.assertEqual(descriptor["H100_nandina_coverage_pct"], 100.0)

    def test_24_total_bank_hhi_is_calculated_over_h100_plus_increment(self) -> None:
        feasibility = json.loads(FEASIBILITY_PATH.read_text(encoding="utf-8"))
        replicate = feasibility["accepted_replicates"][0]
        descriptor = replicate["H150"]["total_bank_descriptor"]
        h100_rows = PLANNER.read_csv_rows(ROOT / PLANNER.H100_PATH)
        new_rows = PLANNER.read_csv_rows(ROOT / PLANNER.NEW_ELIGIBLE_PATH)
        total_rows = [*h100_rows, *PLANNER.rows_for_dams(new_rows, replicate["H150"]["dams"])]
        counts = {}
        for row in total_rows:
            counts[row["DECLARACION"]] = counts.get(row["DECLARACION"], 0) + 1
        expected_hhi = sum((count / len(total_rows)) ** 2 for count in counts.values())
        self.assertEqual(descriptor["dam_hhi"], expected_hhi)
        self.assertNotEqual(descriptor["dam_hhi"], replicate["H150"]["increment_descriptor"]["dam_hhi"])

    def test_25_total_largest_dam_share_is_recalculable(self) -> None:
        feasibility = json.loads(FEASIBILITY_PATH.read_text(encoding="utf-8"))
        replicate = feasibility["accepted_replicates"][0]
        descriptor = replicate["H200"]["total_bank_descriptor"]
        h100_rows = PLANNER.read_csv_rows(ROOT / PLANNER.H100_PATH)
        new_rows = PLANNER.read_csv_rows(ROOT / PLANNER.NEW_ELIGIBLE_PATH)
        total_rows = [*h100_rows, *PLANNER.rows_for_dams(new_rows, replicate["H200"]["dams"])]
        counts = {}
        for row in total_rows:
            counts[row["DECLARACION"]] = counts.get(row["DECLARACION"], 0) + 1
        self.assertEqual(descriptor["largest_dam_rows"], max(counts.values()))
        self.assertEqual(descriptor["largest_dam_share"], max(counts.values()) / len(total_rows))

    def test_26_all_selection_identities_match_the_baseline(self) -> None:
        current = json.loads(FEASIBILITY_PATH.read_text(encoding="utf-8"))
        baseline_bytes = subprocess.check_output(
            ["git", "show", f"b3806190cb645d35c2a121c0f1d0c07fbfe21605:{FEASIBILITY_PATH.relative_to(ROOT).as_posix()}"],
            cwd=ROOT,
        )
        baseline = json.loads(baseline_bytes.decode("utf-8"))
        self.assertEqual(PLANNER.selection_identity(current), PLANNER.selection_identity(baseline))
        self.assertTrue(current["selection_identity_comparison"]["accepted_seed_schedule_identical"])

    def test_27_common_clean_denominators_are_explicit_and_fixed(self) -> None:
        summary = json.loads(FEASIBILITY_PATH.read_text(encoding="utf-8"))["common_clean_mask_summary"]
        self.assertEqual(summary["primary_eval_denominator"], 1056)
        self.assertEqual(summary["masked_case_counts"], {"exact": 36, "near090": 75, "near095": 54, "near098": 46})
        self.assertEqual(summary["clean_denominators"], {"exact": 1020, "near090": 981, "near095": 1002, "near098": 1010})
        self.assertFalse(summary["primary_denominator_affected"])
        self.assertFalse(summary["selection_affected"])

    def test_28_common_clean_mask_sha_is_unchanged_from_baseline(self) -> None:
        baseline_bytes = subprocess.check_output(
            ["git", "show", f"b3806190cb645d35c2a121c0f1d0c07fbfe21605:{MASK_PATH.relative_to(ROOT).as_posix()}"],
            cwd=ROOT,
        )
        self.assertEqual(hashlib.sha256(MASK_PATH.read_bytes()).hexdigest(), hashlib.sha256(baseline_bytes).hexdigest())

    def test_29_selector_remains_independent_of_descriptors_and_evaluation(self) -> None:
        source = inspect.getsource(PLANNER.select_nested_prefixes).lower()
        for forbidden in ("nandina", "evaluation", "performance", "hhi", "coverage", "description"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
