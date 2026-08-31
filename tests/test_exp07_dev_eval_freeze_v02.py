import csv
import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "audits" / "exp07_dev_eval_freeze_v0.2"
MANIFEST = OUT / "gate_exp07_dev_eval_freeze_manifest_v0.2.json"
DEV_SHA = "434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00"
EVAL_SHA = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class TestExp07DevEvalFreezeV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.usage = {row["phase"]: row for row in rows(OUT / "exp07_dev_eval_usage_inventory_v0.2.csv")}
        cls.changes = rows(OUT / "exp07_post_freeze_change_audit_v0.2.csv")

    def test_01_frozen_hashes_and_counts(self):
        self.assertEqual(sha256(DATA / "data_aduanas_devset_clase87_v0.2.csv"), DEV_SHA)
        self.assertEqual(sha256(DATA / "data_aduanas_evalset_clase87_v0.2.csv"), EVAL_SHA)
        self.assertEqual(self.manifest["dev_cases"], 100)
        self.assertEqual(self.manifest["eval_cases"], 1056)

    def test_02_split_dam_overlap_is_zero(self):
        self.assertEqual(self.manifest["dam_overlap"], {"historical_dev": 0, "historical_eval": 0, "dev_eval": 0})
        self.assertTrue(self.manifest["dev_frozen"])
        self.assertTrue(self.manifest["eval_frozen"])

    def test_03_labels_are_for_evaluation_not_generation(self):
        self.assertTrue(self.manifest["eval_ground_truth_used_for_evaluation"])
        self.assertFalse(self.manifest["eval_ground_truth_exposed_to_generation"])
        self.assertEqual(self.usage["Phase I HE4 generation"]["generation_exposure"], "False")
        self.assertEqual(self.usage["Phase H HE4 sample"]["generation_exposure"], "False")

    def test_04_no_eval_informed_tuning(self):
        self.assertFalse(self.manifest["eval_informed_tuning_detected"])
        self.assertFalse(any(row["classification"] == "EVAL_INFORMED_TUNING" for row in self.changes))
        split = next(row for row in self.changes if row["component"] == "split")
        self.assertEqual(split["change_type"], "EXPERIMENTAL_DESIGN_CORRECTION")
        self.assertEqual(split["eval_information_used_for_change"], "False")
        self.assertTrue(self.manifest["experimental_design_correction_v01_to_v02"])
        self.assertFalse(self.manifest["v01_to_v02_is_eval_tuning"])

    def test_05_phase_specific_limitations_are_preserved(self):
        self.assertFalse(self.manifest["d1a_eval_training_or_selection"])
        self.assertEqual(self.manifest["phase_e_70_30_status"], "DIAGNOSTIC_ONLY_NOT_FINAL_ARCHITECTURE")
        self.assertIn("0_WIN_19_TIE_0_LOSS_1_REFERENCE_ABSENT", self.manifest["phase_g_status"])
        self.assertEqual(self.manifest["phase_j_limitation"], "PROMPT_SCHEMA_SPECIFICATION_MISMATCH")
        self.assertEqual(self.manifest["phase_k_limitation"], "EVALUATOR_MODALITY_DEVIATION")

    def test_06_gate_and_hashes(self):
        self.assertEqual(self.manifest["gate_exp07"], "APPROVED")
        self.assertTrue(self.manifest["ready_for_exp04_consolidated_close"])
        for name, expected in self.manifest["output_sha256"].items():
            self.assertEqual(sha256(OUT / name), expected, name)


if __name__ == "__main__":
    unittest.main()
