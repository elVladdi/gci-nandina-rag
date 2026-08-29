import csv
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "evaluation" / "historical_retrieval_data_aduanas_clase87_v0.2"

EXPECTED_HASHES = {
    "historical": "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff",
    "evalset": "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941",
    "support": "4fed0fe48a8d36718bb65e1adbb5eecce2ca671fbb5aa846bd22a2dc2762f385",
    "exact_duplicates": "691b094fbd4e6a142b235226abea27ba20897418b5929fa7dedcee48bc295525",
    "near_duplicates": "0f1f0283c993dd57ab3e02ba064b8c964fd688777726f7ae80c04c47e9c9b955",
}
K_VALUES = [1, 3, 5, 10, 50]
HIERARCHICAL_K = [10, 50]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class TestHistoricalBm25V02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metrics = load_json(OUT / "historical_metrics.json")
        cls.run_metadata = load_json(OUT / "run_metadata.json")
        cls.case_rows = rows(OUT / "historical_case_summary.csv")
        cls.results_rows = rows(OUT / "historical_results.csv")
        cls.failures = rows(OUT / "historical_failure_cases.csv")
        cls.position_rows = rows(OUT / "position_distribution.csv")
        cls.exact_sensitivity = rows(OUT / "sensitivity_exact_duplicates.csv")
        cls.near_sensitivity = rows(OUT / "sensitivity_near_duplicates_095.csv")

    def test_01_expected_outputs_exist(self):
        for rel in self.metrics["outputs"].values():
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_02_inputs_are_locked_v02_hashes(self):
        inputs = self.run_metadata["inputs"]
        self.assertEqual(inputs["historical_sha256"], EXPECTED_HASHES["historical"])
        self.assertEqual(inputs["evalset_sha256"], EXPECTED_HASHES["evalset"])
        self.assertEqual(inputs["support_by_eval_row_sha256"], EXPECTED_HASHES["support"])
        self.assertEqual(inputs["exact_duplicates_sha256"], EXPECTED_HASHES["exact_duplicates"])
        self.assertEqual(inputs["near_duplicates_sha256"], EXPECTED_HASHES["near_duplicates"])
        self.assertNotIn("v0.1", inputs["historical"])
        self.assertNotIn("v0.1", inputs["evalset"])

    def test_03_scope_and_case_ids_are_v02_eval_only(self):
        case_ids = [row["case_id"] for row in self.case_rows]
        self.assertEqual(len(case_ids), 1056)
        self.assertEqual(len(set(case_ids)), 1056)
        self.assertTrue(all(case_id.startswith("DA-EVAL-V02-") for case_id in case_ids))
        self.assertFalse(any("V01" in case_id.upper() for case_id in case_ids))
        self.assertEqual(len({row["expected_nandina"] for row in self.case_rows}), 42)

    def test_04_support_and_duplicate_counts_match_audits(self):
        self.assertTrue(all(row["nandina_present_in_history"] == "1" for row in self.case_rows))
        self.assertEqual(sum(row["exact_duplicate_cross_split"] == "True" for row in self.case_rows), 35)
        self.assertEqual(sum(row["near_duplicate_095"] == "True" for row in self.case_rows), 44)
        validation = self.run_metadata["validation"]
        self.assertEqual(validation["eval_cases_with_historical_support"], 1056)
        self.assertEqual(validation["eval_cases_with_exact_duplicate"], 35)
        self.assertEqual(validation["eval_cases_with_near_duplicate_095"], 44)

    def test_05_metrics_recompute_from_case_summary(self):
        metrics = self.metrics["metrics"]
        denominator = len(self.case_rows)
        self.assertEqual(denominator, metrics["cases_evaluated"])
        reciprocal_sum = sum(float(row["reciprocal_rank"]) for row in self.case_rows)
        self.assertAlmostEqual(reciprocal_sum / denominator, metrics["mrr"])
        self.assertAlmostEqual(reciprocal_sum, metrics["mrr_numerator"])
        for k in K_VALUES:
            numerator = sum(int(row[f"exact_at_{k}"]) for row in self.case_rows)
            self.assertEqual(numerator, metrics[f"exact_at_{k}_numerator"])
            self.assertEqual(denominator, metrics[f"exact_at_{k}_denominator"])
            self.assertAlmostEqual(numerator / denominator, metrics[f"exact_at_{k}"])
        for k in HIERARCHICAL_K:
            for metric in ["partida", "sub_partida", "clase"]:
                key = f"{metric}_at_{k}"
                numerator = sum(int(row[key]) for row in self.case_rows)
                self.assertEqual(numerator, metrics[f"{key}_numerator"])
                self.assertAlmostEqual(numerator / denominator, metrics[key])

    def test_06_top50_failures_and_position_distribution_are_consistent(self):
        self.assertEqual(len(self.failures), 9)
        self.assertEqual(sum(row["exact_at_50"] == "0" for row in self.case_rows), 9)
        self.assertEqual(sum(int(row["cases"]) for row in self.position_rows), 1056)
        by_bucket = {row["position_bucket"]: int(row["cases"]) for row in self.position_rows}
        self.assertEqual(by_bucket[">50_or_not_retrieved"], 9)

    def test_07_sensitivity_files_cover_present_absent_groups(self):
        exact = {row["value"]: int(row["cases"]) for row in self.exact_sensitivity}
        near = {row["value"]: int(row["cases"]) for row in self.near_sensitivity}
        self.assertEqual(exact["exact_duplicate_present"], 35)
        self.assertEqual(exact["exact_duplicate_absent"], 1021)
        self.assertEqual(near["near_duplicate_095_present"], 44)
        self.assertEqual(near["near_duplicate_095_absent"], 1012)

    def test_08_output_hashes_match_run_metadata(self):
        for name, expected in self.run_metadata["output_sha256"].items():
            path = ROOT / self.run_metadata["outputs"][name]
            self.assertEqual(sha256(path), expected, name)

    def test_09_csv_outputs_use_lf_serialization(self):
        for rel in self.metrics["outputs"].values():
            path = ROOT / rel
            if path.suffix != ".csv":
                continue
            data = path.read_bytes()
            self.assertNotIn(b"\r\n", data, path)
            self.assertTrue(data.endswith(b"\n"), path)

    def test_10_candidate_ranking_is_bm25_historical_only(self):
        self.assertTrue(self.results_rows)
        self.assertTrue(all(row["method"] == "historical_bm25_data_aduanas_clase87_v0.2" for row in self.results_rows))
        validation = self.run_metadata["validation"]
        self.assertFalse(validation["llm_used"])
        self.assertFalse(validation["text2trade_used"])
        self.assertFalse(validation["remote_api_used"])
        self.assertFalse(validation["normative_bm25_used_as_candidate_source"])
        self.assertFalse(validation["hierarchical_bm25_used_as_candidate_source"])


if __name__ == "__main__":
    unittest.main()