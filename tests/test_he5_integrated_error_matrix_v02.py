from __future__ import annotations

import csv
import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/he5_integrated_error_analysis_v0.2"


class He5IntegratedErrorMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with (OUT / "he5_integrated_error_matrix_v0.2.csv").open(encoding="utf-8", newline="") as handle:
            cls.matrix = list(csv.DictReader(handle))
        cls.manifest = json.loads((OUT / "gate_l_integrated_error_analysis_manifest_v0.2.json").read_text(encoding="utf-8"))
        cls.hypothesis = json.loads((OUT / "he5_hypothesis_assessment_v0.2.json").read_text(encoding="utf-8"))

    def test_01_frozen_evalset_and_matrix_are_exact(self) -> None:
        self.assertEqual(hashlib.sha256((ROOT / "data/processed/data_aduanas_evalset_clase87_v0.2.csv").read_bytes()).hexdigest(), "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941")
        self.assertEqual(len(self.matrix), 1056)
        self.assertEqual(len({row["case_id"] for row in self.matrix}), 1056)

    def test_02_historical_metrics_and_hierarchy_reconcile(self) -> None:
        self.assertEqual(sum(int(row["historical_top1_correct"]) for row in self.matrix), 538)
        self.assertEqual(sum(int(row["historical_top3_correct"]) for row in self.matrix), 709)
        self.assertEqual(sum(int(row["historical_top5_correct"]) for row in self.matrix), 806)
        self.assertEqual(sum(int(row["historical_top10_correct"]) for row in self.matrix), 941)
        self.assertEqual(sum(int(row["historical_top50_recovered"]) for row in self.matrix), 1047)
        counts = {key: sum(row["historical_error_hierarchy"] == key for row in self.matrix) for key in ("SAME_HS6", "SAME_HS4", "SAME_CHAPTER", "DIFFERENT_CHAPTER")}
        self.assertEqual(counts, {"SAME_HS6": 87, "SAME_HS4": 284, "SAME_CHAPTER": 147, "DIFFERENT_CHAPTER": 0})

    def test_03_coverage_is_explicit_and_not_imputed(self) -> None:
        self.assertEqual(sum(int(row["reranker_evaluated"]) for row in self.matrix), 20)
        self.assertEqual(sum(int(row["he4_evaluated"]) for row in self.matrix), 50)
        self.assertTrue(all(row["reranker_outcome"] == "NOT_EVALUATED" for row in self.matrix if not int(row["reranker_evaluated"])))
        self.assertTrue(all(not row["he4_total_score"] for row in self.matrix if not int(row["he4_evaluated"])))

    def test_04_gate_and_protocol_limits_are_preserved(self) -> None:
        self.assertEqual(self.manifest["gate_l"], "APPROVED")
        self.assertTrue(self.manifest["ready_for_exp08"])
        self.assertTrue(self.manifest["no_model_call"])
        self.assertTrue(self.manifest["no_new_retrieval"])
        self.assertTrue(self.manifest["no_web"])
        self.assertEqual(self.hypothesis["he5_status"], "PENDING_FINAL_ASSESSMENT_AFTER_EXP08")
        self.assertEqual(self.hypothesis["preserved"], {"HE2": "PARTIALLY SUPPORTED", "HE3": "SUPPORTED", "HE4": "PARTIALLY SUPPORTED"})

    def test_05_corrective_description_and_near_duplicate_contract(self) -> None:
        self.assertTrue(all(row["commercial_description"] for row in self.matrix))
        self.assertEqual(sum(int(row["near_ge_090"]) for row in self.matrix), 55)
        self.assertEqual(sum(int(row["near_ge_095"]) for row in self.matrix), 44)
        self.assertEqual(sum(int(row["near_ge_098"]) for row in self.matrix), 37)
        self.assertTrue(all(row["description_quality_operationalized"] == "0" for row in self.matrix))


if __name__ == "__main__":
    unittest.main()
