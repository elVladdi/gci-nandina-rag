import csv
import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "data" / "processed" / "data_aduanas_evalset_clase87_v0.2.csv"
OUT = ROOT / "outputs" / "audits" / "exp05_unified_eval_hash_v0.2"
MANIFEST = OUT / "gate_exp05_unified_eval_hash_manifest_v0.2.json"
EXPECTED_SHA = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class TestExp05UnifiedEvalHashV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = rows(OUT / "exp05_eval_consumer_inventory_v0.2.csv")
        cls.by_phase = {row["phase"]: row for row in cls.inventory}
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_01_official_eval_hash(self):
        self.assertEqual(sha256(EVAL), EXPECTED_SHA)
        self.assertEqual(self.manifest["official_eval_sha256"], EXPECTED_SHA)

    def test_02_official_eval_has_1056_unique_cases(self):
        eval_rows = rows(EVAL)
        self.assertEqual(len(eval_rows), 1056)
        self.assertEqual(len({row["case_id"] for row in eval_rows}), 1056)

    def test_03_direct_consumers_are_reconciled(self):
        direct = [row for row in self.inventory if row["consumer_type"] == "DIRECT_EVALSET_CONSUMER"]
        self.assertEqual(len(direct), 6)
        self.assertEqual({row["phase"] for row in direct}, {
            "Phase A historical BM25", "Phase B normative flat", "Phase C normative hierarchical",
            "Phase D1a dense comparator", "Phase E candidate pools", "Phase F historical-normative integration",
        })
        self.assertTrue(all(row["eval_sha256_if_direct"] == EXPECTED_SHA for row in direct))
        self.assertTrue(all(row["status"] == "RECONCILED" for row in direct))

    def test_04_subsets_and_derived_consumers_are_reconciled(self):
        self.assertEqual(self.by_phase["Phase G diagnostic reranker"]["case_count"], "20")
        self.assertEqual(self.by_phase["Phase H HE4 sample selection"]["case_count"], "50")
        self.assertEqual(self.by_phase["Phase G diagnostic reranker"]["case_set_relation"], "SUBSET_OF_1056")
        self.assertEqual(self.by_phase["Phase H HE4 sample selection"]["case_set_relation"], "SUBSET_OF_1056")
        self.assertEqual(self.by_phase["Phase L / EXP-10 HE5 matrix"]["case_count"], "1056")
        self.assertEqual(self.by_phase["EXP-08 v0.1-v0.2 sensitivity"]["case_count"], "1056")
        self.assertTrue(all(row["status"] == "RECONCILED" for row in self.inventory))

    def test_05_no_undeclared_eval_drift(self):
        self.assertFalse(self.manifest["eval_drift_detected"])
        self.assertFalse(self.manifest["undeclared_eval_drift_detected"])
        self.assertTrue(self.manifest["all_final_v02_consumers_reconciled"])
        self.assertTrue(self.manifest["subset_consumers_validated"])
        self.assertEqual(self.manifest["gate_exp05"], "APPROVED")

    def test_06_manifest_hashes_match_outputs(self):
        for name, expected in self.manifest["output_sha256"].items():
            self.assertEqual(sha256(OUT / name), expected, name)


if __name__ == "__main__":
    unittest.main()
