"""Contract tests for prospective EXP-11B H150/H200 planning."""

from __future__ import annotations

import hashlib
import importlib.util
import inspect
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src/experiments/prepare_exp11b_historical_size_extension_v0.1.py"
CONFIG_PATH = ROOT / "src/configs/exp11b_historical_size_extension_v0.1.json"
EXP11A_CONFIG_PATH = ROOT / "src/configs/exp11_historical_size_sensitivity_v0.3.json"
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


if __name__ == "__main__":
    unittest.main()
