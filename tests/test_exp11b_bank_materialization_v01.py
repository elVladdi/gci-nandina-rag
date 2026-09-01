"""Fail-closed tests for deterministic EXP-11B bank materialization."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src/experiments/materialize_exp11b_banks_v01.py"
CONFIG_PATH = ROOT / "src/configs/exp11b_bank_materialization_v0.1.json"
SPEC = importlib.util.spec_from_file_location("exp11b_bank_materializer_v01", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MATERIALIZER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MATERIALIZER
SPEC.loader.exec_module(MATERIALIZER)


class Exp11bBankMaterializationV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        cls.inputs, cls.plans = MATERIALIZER.preflight(ROOT)
        cls.by_id = {plan.bank_id: plan for plan in cls.plans}

    def test_01_contract_is_materialization_only(self) -> None:
        self.assertEqual(self.config["contract_status"], "EXP11B_BANK_MATERIALIZATION_ONLY")
        self.assertTrue(self.config["bank_materialization_authorized"])

    def test_02_retrieval_and_metrics_remain_disabled(self) -> None:
        self.assertFalse(self.config["retrieval_authorized"])
        self.assertFalse(self.config["retrieval_executed"])
        self.assertFalse(self.config["evaluation_metrics_allowed"])
        self.assertFalse(self.config["evaluation_metrics_computed"])

    def test_03_h100_sha_mismatch_fails_closed(self) -> None:
        spec = self.config["inputs"]["H100"]
        with self.assertRaises(MATERIALIZER.ContractViolation):
            MATERIALIZER.validate_file_contract(ROOT / spec["path"], "0" * 64, spec["rows"], "H100")

    def test_04_new_eligible_sha_mismatch_fails_closed(self) -> None:
        spec = self.config["inputs"]["NEW_ELIGIBLE"]
        with self.assertRaises(MATERIALIZER.ContractViolation):
            MATERIALIZER.validate_file_contract(ROOT / spec["path"], "0" * 64, spec["rows"], "NEW_ELIGIBLE")

    def test_05_feasibility_sha_mismatch_is_detectable(self) -> None:
        path = ROOT / self.config["feasibility"]["path"]
        self.assertNotEqual(MATERIALIZER.sha256_file(path), "0" * 64)
        self.assertEqual(MATERIALIZER.sha256_file(path), self.config["feasibility"]["sha256"])

    def test_06_exactly_ten_frozen_replicates(self) -> None:
        replicates = self.inputs.feasibility["accepted_replicates"]
        self.assertEqual(len(replicates), 10)
        self.assertEqual([item["replicate_id"] for item in replicates], [f"R{number:02d}" for number in range(1, 11)])

    def test_07_exactly_twenty_bank_plans(self) -> None:
        self.assertEqual(len(self.plans), 20)
        self.assertEqual({plan.condition for plan in self.plans}, {"H150", "H200"})

    def test_08_h100_is_the_first_2950_rows_of_every_plan(self) -> None:
        self.assertEqual(len(self.inputs.h100.rows), 2950)
        for plan in self.plans:
            bank_rows = (*self.inputs.h100.rows, *plan.projected_new_rows)
            self.assertEqual(bank_rows[:2950], self.inputs.h100.rows, plan.bank_id)

    def test_09_h100_order_is_frozen(self) -> None:
        core_ids = [row["id_unico"] for row in self.inputs.h100.rows]
        self.assertEqual(core_ids, [row["id_unico"] for row in self.inputs.h100.rows])
        self.assertEqual(len(core_ids), len(set(core_ids)))

    def test_10_new_rows_keep_eligible_source_order(self) -> None:
        for plan in self.plans:
            expected = [
                row["id_unico"]
                for row in self.inputs.new_eligible.rows
                if row["DECLARACION"] in set(plan.selected_dams)
            ]
            self.assertEqual([row["id_unico"] for row in plan.selected_new_rows], expected, plan.bank_id)

    def test_11_selected_dams_equal_the_gate03_lists(self) -> None:
        for plan in self.plans:
            self.assertEqual(
                {row["DECLARACION"] for row in plan.selected_new_rows},
                set(plan.selected_dams),
                plan.bank_id,
            )

    def test_12_missing_dam_fails_closed(self) -> None:
        feasibility = copy.deepcopy(self.inputs.feasibility)
        feasibility["accepted_replicates"][0]["H150"]["dams"] = feasibility["accepted_replicates"][0]["H150"]["dams"][1:]
        with self.assertRaises(MATERIALIZER.ContractViolation):
            MATERIALIZER.validate_replicates(replace(self.inputs, feasibility=feasibility))

    def test_13_extra_dam_fails_closed(self) -> None:
        feasibility = copy.deepcopy(self.inputs.feasibility)
        h150 = feasibility["accepted_replicates"][0]["H150"]
        extra = next(dam for dam in MATERIALIZER.dam_set(self.inputs.new_eligible.rows, "NEW") if dam not in h150["dams"])
        h150["dams"].append(extra)
        with self.assertRaises(MATERIALIZER.ContractViolation):
            MATERIALIZER.validate_replicates(replace(self.inputs, feasibility=feasibility))

    def test_14_composition_sha_matches_gate03(self) -> None:
        for plan in self.plans:
            self.assertEqual(MATERIALIZER.composition_sha256(plan.selected_dams), plan.feasibility_entry["composition_sha256"])

    def test_15_realized_new_row_counts_match_gate03(self) -> None:
        for plan in self.plans:
            self.assertEqual(len(plan.selected_new_rows), plan.feasibility_entry["realized_new_rows"])

    def test_16_realized_total_row_counts_match_gate03(self) -> None:
        for plan in self.plans:
            self.assertEqual(2950 + len(plan.projected_new_rows), plan.feasibility_entry["realized_total_rows"])

    def test_17_h150_total_ids_are_strict_subset_of_h200(self) -> None:
        h100_ids = {row["id_unico"] for row in self.inputs.h100.rows}
        for number in range(1, 11):
            h150 = self.by_id[f"EXP11B_R{number:02d}_H150"]
            h200 = self.by_id[f"EXP11B_R{number:02d}_H200"]
            h150_ids = h100_ids | {row["id_unico"] for row in h150.projected_new_rows}
            h200_ids = h100_ids | {row["id_unico"] for row in h200.projected_new_rows}
            self.assertTrue(h150_ids < h200_ids)

    def test_18_duplicate_id_unico_fails_closed(self) -> None:
        row = {"id_unico": "duplicate"}
        with self.assertRaises(MATERIALIZER.ContractViolation):
            MATERIALIZER.require_unique_nonempty_ids((row, dict(row)), "synthetic")

    def test_19_dev_or_eval_dam_overlap_fails_closed(self) -> None:
        overlap_row = dict(self.inputs.h100.rows[0])
        overlapping_dev = MATERIALIZER.Dataset(Path("synthetic-dev.csv"), self.inputs.dev.headers, (overlap_row,))
        with self.assertRaises(MATERIALIZER.ContractViolation):
            MATERIALIZER.validate_replicates(replace(self.inputs, dev=overlapping_dev))

    def test_20_increment_descriptors_match_gate03(self) -> None:
        h100_codes = {row["NANDINA"] for row in self.inputs.h100.rows if row["NANDINA"]}
        for plan in self.plans:
            MATERIALIZER.assert_descriptor_matches(
                MATERIALIZER.increment_descriptor(plan.projected_new_rows, h100_codes),
                plan.feasibility_entry["increment_descriptor"],
                plan.bank_id,
            )

    def test_21_total_descriptors_match_gate03(self) -> None:
        h100_codes = {row["NANDINA"] for row in self.inputs.h100.rows if row["NANDINA"]}
        for plan in self.plans:
            MATERIALIZER.assert_descriptor_matches(
                MATERIALIZER.total_bank_descriptor(self.inputs.h100.rows, plan.projected_new_rows, h100_codes),
                plan.feasibility_entry["total_bank_descriptor"],
                plan.bank_id,
            )

    def test_22_h100_coverage_is_66_of_66(self) -> None:
        h100_codes = {row["NANDINA"] for row in self.inputs.h100.rows if row["NANDINA"]}
        descriptor = MATERIALIZER.total_bank_descriptor(self.inputs.h100.rows, self.plans[0].projected_new_rows, h100_codes)
        self.assertEqual(descriptor["H100_nandina_coverage_n"], 66)
        self.assertEqual(descriptor["H100_nandina_coverage_denominator"], 66)

    def test_23_materializer_has_no_retrieval_or_bm25_dependency(self) -> None:
        source = MODULE_PATH.read_text(encoding="utf-8").lower()
        self.assertNotIn("bm25", source)
        self.assertNotIn("import numpy", source)
        self.assertNotIn("import pandas", source)

    def test_24_preexisting_output_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "banks"
            path.mkdir()
            (path / "old.csv").write_text("old\n", encoding="utf-8")
            with self.assertRaises(MATERIALIZER.ContractViolation):
                MATERIALIZER.assert_empty_target(path, "synthetic")

    def test_25_csv_serialization_is_utf8_lf_and_deterministic(self) -> None:
        headers = ("id_unico", "DECLARACION")
        rows = ({"id_unico": "one", "DECLARACION": "DAM,1"},)
        first = MATERIALIZER.serialize_csv(headers, rows)
        second = MATERIALIZER.serialize_csv(headers, rows)
        self.assertEqual(first, second)
        self.assertNotIn(b"\r\n", first)
        self.assertEqual(hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest())

    def test_26_projection_preserves_h100_header_and_excludes_admin_columns(self) -> None:
        source = self.inputs.new_eligible.rows[0]
        projected = MATERIALIZER.project_new_row(source, self.inputs.h100.headers)
        self.assertEqual(tuple(projected), self.inputs.h100.headers)
        self.assertNotIn("protected_dev_eval_dam", projected)
        self.assertEqual(projected["id_unico"], source["id_unico"])

    def test_27_h100_core_id_hash_is_constant_for_all_banks(self) -> None:
        expected = MATERIALIZER.sha256_json_list(row["id_unico"] for row in self.inputs.h100.rows)
        self.assertEqual(expected, MATERIALIZER.sha256_json_list(row["id_unico"] for row in self.inputs.h100.rows))

    def test_28_feasibility_flags_remain_gate03_safe(self) -> None:
        self.assertIs(self.inputs.feasibility["execution_authorized"], False)
        self.assertIs(self.inputs.feasibility["retrieval_executed"], False)


if __name__ == "__main__":
    unittest.main()
