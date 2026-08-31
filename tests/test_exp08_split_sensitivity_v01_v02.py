import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "evaluation" / "exp08_split_sensitivity_v01_vs_v02"
MANIFEST = OUTPUT / "gate_exp08_split_sensitivity_manifest_v0.2.json"


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class TestExp08SplitSensitivityV01V02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.metrics = {row["metric"]: row for row in rows(OUTPUT / "exp08_global_sensitivity_v01_vs_v02.csv")}
        cls.independence = {row["version"]: row for row in rows(OUTPUT / "exp08_split_independence_comparison_v01_vs_v02.csv")}

    def test_01_required_artifacts_exist(self):
        required = {
            "exp08_comparability_audit_v01_vs_v02.json",
            "exp08_global_sensitivity_v01_vs_v02.csv",
            "exp08_split_independence_comparison_v01_vs_v02.csv",
            "exp08_duplicate_sensitivity_comparison_v01_vs_v02.csv",
            "exp08_code_coverage_v01_vs_v02.csv",
            "exp08_code_sensitivity_v01_vs_v02.csv",
            "exp08_he2_sensitivity_assessment_v0.2.json",
            "exp08_he5_component_assessment_v0.2.csv",
            "exp08_final_he5_assessment_v0.2.json",
            "exp08_integrated_findings_v0.2.md",
            MANIFEST.name,
        }
        self.assertTrue(all((OUTPUT / name).exists() for name in required))

    def test_02_gate_and_scope_are_frozen(self):
        self.assertEqual(self.manifest["gate_exp08"], "APPROVED")
        self.assertTrue(self.manifest["ready_for_exp05_exp07_formal_close"])
        self.assertFalse(self.manifest["algorithm_reexecuted"])
        self.assertFalse(self.manifest["model_called"])
        self.assertFalse(self.manifest["new_retrieval"])
        self.assertFalse(self.manifest["causal_claim"])

    def test_03_comparison_is_unpaired_and_v02_is_final(self):
        self.assertFalse(self.manifest["evalsets_equivalent"])
        self.assertFalse(self.manifest["global_comparison_paired"])
        self.assertEqual(self.manifest["common_case_ids"], 0)
        self.assertTrue(self.manifest["v02_final_benchmark"])

    def test_04_global_metrics_match_frozen_case_summaries(self):
        self.assertEqual(int(float(self.metrics["Top1"]["v01_numerator"])), 868)
        self.assertEqual(int(float(self.metrics["Top1"]["v02_numerator"])), 538)
        self.assertEqual(int(float(self.metrics["Top3"]["v01_numerator"])), 943)
        self.assertEqual(int(float(self.metrics["Top3"]["v02_numerator"])), 709)
        self.assertAlmostEqual(float(self.metrics["MRR"]["v01_value"]), 0.9062394558614818)
        self.assertAlmostEqual(float(self.metrics["MRR"]["v02_value"]), 0.6297077493524843)

    def test_05_dam_independence_contrast_is_preserved(self):
        self.assertEqual(int(self.independence["v0.1"]["historical_eval_dam_overlap"]), 995)
        self.assertEqual(int(self.independence["v0.2"]["historical_eval_dam_overlap"]), 0)
        self.assertEqual(self.independence["v0.2"]["independence_status"], "DAM_GROUPED_INDEPENDENT")

    def test_06_limitations_are_explicit(self):
        self.assertFalse(self.manifest["v01_run_metadata_available"])
        self.assertTrue(self.manifest["v01_metadata_provenance_limitation"])
        self.assertEqual(self.manifest["implementation_difference_recorded"], "ranking_depth_v01_200_v02_100")
        self.assertFalse(self.manifest["description_quality_evaluated"])

    def test_07_he2_and_he5_statuses(self):
        he2 = json.loads((OUTPUT / "exp08_he2_sensitivity_assessment_v0.2.json").read_text(encoding="utf-8"))
        he5 = json.loads((OUTPUT / "exp08_final_he5_assessment_v0.2.json").read_text(encoding="utf-8"))
        self.assertEqual(he2["status"], "NOT_REOPENED")
        self.assertEqual(he5["status"], "PARTIALLY_SUPPORTED")
        self.assertEqual(he5["evaluated_components"], 3)


if __name__ == "__main__":
    unittest.main()
