import csv
import json
import unittest
from pathlib import Path

from tests.sha_contracts_v02 import assert_frozen_sha, git_content_sha256


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "evaluation" / "exp08_split_sensitivity_v01_vs_v02"
MANIFEST = OUTPUT / "gate_exp08_split_sensitivity_manifest_v0.2.json"
CORRECTIVE = OUTPUT / "gate_exp08_corrective_microclose_manifest_v0.2.json"


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    return git_content_sha256(path)


class TestExp08SplitSensitivityV01V02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.corrective = json.loads(CORRECTIVE.read_text(encoding="utf-8"))
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
            "exp08_stratified_performance_v01_vs_v02.csv",
            "exp08_he2_sensitivity_assessment_v0.2.json",
            "exp08_he5_component_assessment_v0.2.csv",
            "exp08_final_he5_assessment_v0.2.json",
            "exp08_integrated_findings_v0.2.md",
            "summary_exp08.md",
            MANIFEST.name,
            CORRECTIVE.name,
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

    def test_06_near_duplicate_threshold_semantics_are_unambiguous(self):
        duplicates = {row["signal"]: row for row in rows(OUTPUT / "exp08_duplicate_sensitivity_comparison_v01_vs_v02.csv") if row["version"] == "v0.2"}
        self.assertEqual(int(duplicates["near_duplicate_ge_090"]["count"]), 55)
        self.assertEqual(int(duplicates["near_duplicate_ge_095"]["count"]), 44)
        self.assertEqual(int(duplicates["near_duplicate_ge_098"]["count"]), 37)
        self.assertNotIn("near_duplicate_095_same_nandina", duplicates)
        self.assertNotIn("near_duplicate_095_different_nandina", duplicates)

    def test_07_code_sensitivity_is_one_row_per_union_code(self):
        code_rows = rows(OUTPUT / "exp08_code_sensitivity_v01_vs_v02.csv")
        required = {
            "reference_nandina", "presence_status", "n_v01", "top1_n_v01", "top1_v01", "top3_n_v01", "top3_v01", "mrr_v01",
            "n_v02", "top1_n_v02", "top1_v02", "top3_n_v02", "top3_v02", "mrr_v02",
            "delta_top1_v02_minus_v01", "delta_top3_v02_minus_v01", "delta_mrr_v02_minus_v01",
        }
        self.assertEqual(len(code_rows), len({row["reference_nandina"] for row in code_rows}))
        self.assertTrue(required.issubset(code_rows[0]))
        self.assertTrue({row["presence_status"] for row in code_rows}.issubset({"CODE_IN_BOTH_EVALSETS", "ONLY_V01", "ONLY_V02"}))

    def test_08_code_sensitivity_reconciles_denominators_and_deltas(self):
        code_rows = rows(OUTPUT / "exp08_code_sensitivity_v01_vs_v02.csv")
        self.assertEqual(sum(int(row["n_v01"]) for row in code_rows), 1006)
        self.assertEqual(sum(int(row["n_v02"]) for row in code_rows), 1056)
        for row in code_rows:
            both = row["presence_status"] == "CODE_IN_BOTH_EVALSETS"
            self.assertEqual(bool(row["delta_top1_v02_minus_v01"]), both)
            self.assertEqual(bool(row["delta_top3_v02_minus_v01"]), both)
            self.assertEqual(bool(row["delta_mrr_v02_minus_v01"]), both)

    def test_09_nominal_code_coverage_reconciles_to_frozen_splits(self):
        coverage = {row["version"]: row for row in rows(OUTPUT / "exp08_code_coverage_v01_vs_v02.csv")}
        self.assertEqual(int(coverage["v0.1"]["eval_cases"]), 1006)
        self.assertEqual(int(coverage["v0.2"]["eval_cases"]), 1056)
        for row in coverage.values():
            self.assertEqual(int(row["cases_with_historical_nominal_support"]), int(row["eval_cases"]))
            self.assertEqual(float(row["historical_nominal_support_rate"]), 1.0)
            self.assertEqual(int(row["supported_codes"]), int(row["total_eval_codes"]))

    def test_10_stratified_v02_counts_and_metrics_are_frozen(self):
        strata = {(row["signal"], row["stratum"]): row for row in rows(OUTPUT / "exp08_stratified_performance_v01_vs_v02.csv") if row["version"] == "v0.2"}
        exact = strata[("EXACT_DUPLICATE", "EXACT")]
        non_exact = strata[("EXACT_DUPLICATE", "NON_EXACT")]
        near = strata[("NEAR_GE_095", "NEAR_GE_095")]
        rest = strata[("NEAR_GE_095", "REST_NEAR_GE_095")]
        self.assertEqual(int(exact["n"]), 35)
        self.assertEqual(int(non_exact["n"]), 1021)
        self.assertEqual(int(near["n"]), 44)
        self.assertEqual(int(rest["n"]), 1012)
        self.assertEqual(int(exact["top1_n"]), 34)
        self.assertAlmostEqual(float(exact["mrr"]), 0.9857142857142858)
        self.assertAlmostEqual(float(non_exact["top1_rate"]), 0.49363369245837413)
        self.assertAlmostEqual(float(non_exact["mrr"]), 0.6175038034439012)
        self.assertAlmostEqual(float(near["top1_rate"]), 0.9545454545454546)
        self.assertAlmostEqual(float(near["mrr"]), 0.9772727272727273)
        self.assertAlmostEqual(float(rest["top1_rate"]), 0.4901185770750988)
        self.assertAlmostEqual(float(rest["mrr"]), 0.6145962285733431)

    def test_11_stratified_v01_unpreserved_flags_are_not_invented(self):
        rows_v01 = [row for row in rows(OUTPUT / "exp08_stratified_performance_v01_vs_v02.csv") if row["version"] == "v0.1" and row["signal"] != "DAM_MEMBERSHIP"]
        self.assertTrue(rows_v01)
        self.assertTrue(all(row["availability"] == "NOT_AVAILABLE_NO_FROZEN_CASE_LEVEL_DUPLICATE_FLAGS" for row in rows_v01))
        self.assertTrue(all(row["n"] == "NOT_AVAILABLE" for row in rows_v01))

    def test_12_he5_component_schema_and_assessment(self):
        components = rows(OUTPUT / "exp08_he5_component_assessment_v0.2.csv")
        required = {"component", "source", "evaluated", "evidence", "assessment", "limitation"}
        self.assertEqual(len(components), 4)
        self.assertEqual({row["component"] for row in components}, {"DESCRIPTION_QUALITY", "HIERARCHICAL_PROXIMITY", "HISTORICAL_PRECEDENT_AVAILABILITY", "INTERNAL_EVALUATION_SCOPE"})
        self.assertTrue(required.issubset(components[0]))
        description = next(row for row in components if row["component"] == "DESCRIPTION_QUALITY")
        internal = next(row for row in components if row["component"] == "INTERNAL_EVALUATION_SCOPE")
        self.assertEqual(description["evaluated"], "False")
        self.assertEqual(description["assessment"], "NOT_EVALUATED_NO_FROZEN_CASE_RULE")
        self.assertEqual(internal["assessment"], "SENSITIVITY_TO_EXPERIMENTAL_CONFIGURATION")

    def test_13_summary_and_he_statuses_exist(self):
        summary = (OUTPUT / "summary_exp08.md").read_text(encoding="utf-8")
        he2 = json.loads((OUTPUT / "exp08_he2_sensitivity_assessment_v0.2.json").read_text(encoding="utf-8"))
        he5 = json.loads((OUTPUT / "exp08_final_he5_assessment_v0.2.json").read_text(encoding="utf-8"))
        self.assertIn("-35.335 pp", summary)
        self.assertIn("Near-duplicates", summary)
        self.assertEqual(he2["status"], "NOT_REOPENED")
        self.assertEqual(he5["status"], "PARTIALLY_SUPPORTED")

    def test_14_corrective_manifest_and_output_hashes_are_complete(self):
        self.assertEqual(self.corrective["phase"], "EXP-08 CORRECTIVE MICROCLOSE")
        self.assertEqual(self.corrective["original_gate_commit"], "f0a369a7552cf3af7a950b2e7cdef4c286b94a9e")
        self.assertEqual(self.corrective["gate_exp08_corrective_microclose"], "APPROVED")
        self.assertTrue(self.corrective["ready_for_exp05_exp07_formal_close"])
        self.assertTrue(self.corrective["near_duplicate_semantics_corrected"])
        self.assertTrue(self.corrective["code_sensitivity_corrected"])
        for name, expected in self.corrective["new_output_sha256"].items():
            assert_frozen_sha(self, OUTPUT / name, expected)
        self.assertEqual(self.manifest["output_sha256"], self.corrective["new_output_sha256"])


if __name__ == "__main__":
    unittest.main()
