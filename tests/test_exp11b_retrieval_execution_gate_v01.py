"""Prospective contract tests for the EXP-11B retrieval execution gate."""

from __future__ import annotations

import copy
import inspect
import json
import tempfile
import unittest
from pathlib import Path

from src.experiments.freeze_exp11b_retrieval_execution_gate_v01 import (
    ContractViolation,
    freeze_gate,
    load_json,
    preflight,
    read_csv,
    validate_bank_identity_contract,
    validate_inputs,
    validate_static_contract,
)


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "src/configs/exp11b_retrieval_execution_gate_v0.1.json"
AUDIT_DIR = ROOT / "outputs/audits/exp11b_retrieval_execution_gate_v0.1"


class Exp11bRetrievalExecutionGateV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = load_json(CONFIG_PATH)
        cls.materialization = cls.config["materialization_contract"]
        cls.manifest = load_json(ROOT / cls.materialization["manifest"]["path"])
        cls.ledger_rows = read_csv(ROOT / cls.materialization["ledger"]["path"])

    def test_01_base_commit_and_pending_status_are_frozen(self) -> None:
        self.assertEqual(self.config["integrated_base_commit"], "95ffec45ae5a734545ae7bb2d8d530f42f8f056c")
        self.assertEqual(self.config["gate_status"], "CANDIDATE_PENDING_EXTERNAL_AUDIT")

    def test_02_evalset_sha_and_primary_n_are_frozen(self) -> None:
        evalset = self.config["frozen_inputs"]["evalset"]
        self.assertEqual(evalset["sha256"], "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941")
        self.assertEqual(evalset["rows"], 1056)

    def test_03_h100_sha_and_reference_metrics_are_frozen(self) -> None:
        h100 = self.config["frozen_inputs"]["h100"]
        metrics = self.config["frozen_inputs"]["h100_reference_metrics"]
        self.assertEqual(h100["sha256"], "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff")
        self.assertEqual(metrics["top_1"]["numerator"], 538)
        self.assertEqual(metrics["top_50"]["numerator"], 1047)
        self.assertEqual(metrics["mrr"], 0.6297077493524843)

    def test_04_materialization_manifest_and_ledger_contracts_validate(self) -> None:
        checks, identities, _common = validate_inputs(ROOT, self.config)
        self.assertGreaterEqual(len(checks), 15)
        self.assertEqual(len(identities), 20)

    def test_05_ledger_defines_twenty_banks(self) -> None:
        self.assertEqual(len(self.ledger_rows), 20)
        self.assertEqual(sum(row["condition"] == "H150" for row in self.ledger_rows), 10)
        self.assertEqual(sum(row["condition"] == "H200" for row in self.ledger_rows), 10)

    def test_06_complete_bank_identities_validate(self) -> None:
        identities = validate_bank_identity_contract(self.config, self.ledger_rows, self.manifest["banks"])
        self.assertEqual([row["bank_id"] for row in identities], self.materialization["expected_bank_ids"])
        self.assertTrue(all(len(row["bank_csv_sha256"]) == 64 for row in identities))

    def test_07_altered_bank_hash_is_rejected(self) -> None:
        altered = copy.deepcopy(self.ledger_rows)
        altered[0]["bank_csv_sha256"] = "0" * 64
        with self.assertRaisesRegex(ContractViolation, "Bank hash mismatch"):
            validate_bank_identity_contract(self.config, altered, self.manifest["banks"])

    def test_08_altered_evalset_hash_is_rejected(self) -> None:
        altered = copy.deepcopy(self.config)
        altered["frozen_inputs"]["evalset"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ContractViolation, "SHA256 mismatch for evalset"):
            validate_inputs(ROOT, altered)

    def test_09_altered_bm25_configuration_is_rejected(self) -> None:
        altered = copy.deepcopy(self.config)
        altered["canonical_retrieval_semantics"]["k1"] = 1.7
        with self.assertRaisesRegex(ContractViolation, "BM25 k1/b"):
            validate_static_contract(altered)

    def test_10_case_level_schema_is_auditable(self) -> None:
        columns = self.config["future_output_contract"]["files"]["case_level_csv"]["columns"]
        required = {"run_id", "bank_id", "condition", "seed", "case_id", "id_unico", "reference_nandina", "reference_rank", "reciprocal_rank", "hit_at_1", "hit_at_3", "hit_at_5", "hit_at_10", "hit_at_50"}
        self.assertTrue(required.issubset(columns))

    def test_11_k_values_and_tie_handling_are_frozen(self) -> None:
        semantics = self.config["canonical_retrieval_semantics"]
        self.assertEqual(semantics["k_values"], [1, 3, 5, 10, 50])
        self.assertEqual(semantics["ranking_order"], "descending_score_then_ascending_historical_case_id")

    def test_12_common_clean_denominators_are_exact_and_complementary(self) -> None:
        common = self.config["common_clean"]
        self.assertEqual(common["primary_denominator"], 1056)
        self.assertEqual({name: item["clean_denominator"] for name, item in common["sets"].items()}, {"exact": 1020, "near090": 981, "near095": 1002, "near098": 1010})
        self.assertTrue(common["complementary_only"])

    def test_13_primary_denominator_is_immutable(self) -> None:
        altered = copy.deepcopy(self.config)
        altered["common_clean"]["primary_denominator"] = 1020
        with self.assertRaisesRegex(ContractViolation, "Primary denominator"):
            validate_static_contract(altered)

    def test_14_freeze_rejects_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory) / "gate"
            freeze_gate(ROOT, target, CONFIG_PATH)
            with self.assertRaisesRegex(ContractViolation, "not empty"):
                freeze_gate(ROOT, target, CONFIG_PATH)

    def test_15_freeze_rejects_silent_resume(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory) / "partial"
            target.mkdir()
            (target / "partial.json").write_text("{}\n", encoding="utf-8")
            with self.assertRaisesRegex(ContractViolation, "not empty"):
                freeze_gate(ROOT, target, CONFIG_PATH)

    def test_16_missing_bank_is_rejected(self) -> None:
        with self.assertRaisesRegex(ContractViolation, "Expected 20 ledger rows"):
            validate_bank_identity_contract(self.config, self.ledger_rows[:-1], self.manifest["banks"])

    def test_17_future_result_directory_is_absent(self) -> None:
        future = ROOT / self.config["future_output_contract"]["official_output_root"]
        self.assertFalse(future.exists())

    def test_18_preflight_does_not_import_or_call_retrieval(self) -> None:
        source = inspect.getsource(__import__("src.experiments.freeze_exp11b_retrieval_execution_gate_v01", fromlist=["*"]))
        self.assertNotIn("evaluate_historical_retrieval_data_aduanas_v02", source)
        self.assertNotIn("_build_bm25_index(", source)
        report = preflight(ROOT, CONFIG_PATH)
        self.assertEqual(report["status"], "PREFLIGHT_PASS_CANDIDATE_PENDING_EXTERNAL_AUDIT")

    def test_19_retrieval_and_metric_flags_remain_false(self) -> None:
        report = preflight(ROOT, CONFIG_PATH)
        self.assertEqual(report["flags"], {
            "retrieval_executed": False,
            "evaluation_metrics_computed": False,
            "h150_h200_results_observed": False,
            "exp11b_retrieval_authorized": False,
        })

    def test_20_frozen_gate_artifacts_are_candidate_only(self) -> None:
        manifest = load_json(AUDIT_DIR / "exp11b_retrieval_execution_gate_manifest_v0.1.json")
        inventory = load_json(AUDIT_DIR / "exp11b_retrieval_execution_input_inventory_v0.1.json")
        self.assertEqual(manifest["gate_status"], "CANDIDATE_PENDING_EXTERNAL_AUDIT")
        self.assertEqual(manifest["bank_count"], 20)
        self.assertEqual(len(inventory["bank_identities"]), 20)
        self.assertFalse(manifest["retrieval_executed"])


if __name__ == "__main__":
    unittest.main()
