import csv
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "evaluation" / "normative_bm25_flat_data_aduanas_clase87_v0.2"

EXPECTED_EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
EXPECTED_CORPUS_SHA256 = "83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0"
EXPECTED_INDEX_SHA256 = "fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b"
K_VALUES = [1, 3, 5, 10, 50]


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


class TestNormativeBm25FlatV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metrics = load_json(OUT / "normative_metrics.json")
        cls.run_metadata = load_json(OUT / "run_metadata.json")
        cls.coverage = load_json(OUT / "normative_coverage_summary.json")
        cls.compatibility = load_json(OUT / "historical_vs_normative_flat_compatibility_v0.2.json")
        cls.case_rows = rows(OUT / "normative_case_summary.csv")
        cls.result_rows = rows(OUT / "normative_results.csv")
        cls.position_rows = rows(OUT / "position_distribution.csv")
        cls.coverage_rows = rows(OUT / "normative_coverage_summary.csv")

    def test_01_expected_outputs_exist(self):
        for rel in self.metrics["outputs"].values():
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_02_input_hashes_are_locked(self):
        inputs = self.run_metadata["inputs"]
        self.assertEqual(inputs["evalset_sha256"], EXPECTED_EVAL_SHA256)
        self.assertEqual(inputs["corpus_sha256"], EXPECTED_CORPUS_SHA256)
        self.assertEqual(inputs["index_sha256"], EXPECTED_INDEX_SHA256)
        self.assertNotIn("v0.1", inputs["evalset"])
        self.assertNotIn("v0.1", inputs["corpus"])
        self.assertNotIn("v0.1", inputs["index"])

    def test_03_eval_scope_is_v02(self):
        case_ids = [row["case_id"] for row in self.case_rows]
        self.assertEqual(len(case_ids), 1056)
        self.assertEqual(len(set(case_ids)), 1056)
        self.assertTrue(all(case_id.startswith("DA-EVAL-V02-") for case_id in case_ids))
        self.assertFalse(any("V01" in case_id.upper() for case_id in case_ids))
        self.assertEqual(len({row["nandina_ref"] for row in self.case_rows}), 42)

    def test_04_corpus_coverage_is_explicit(self):
        self.assertEqual(self.coverage["eval_unique_codes"], 42)
        self.assertEqual(self.coverage["eval_codes_covered_by_corpus"], 42)
        self.assertEqual(self.coverage["eval_cases"], 1056)
        self.assertEqual(self.coverage["eval_cases_covered_by_corpus"], 1056)
        self.assertEqual(self.coverage["eval_cases_absent_from_corpus"], 0)
        self.assertEqual(self.coverage["eval_cases_covered_but_not_recovered_top_50"], 982)

    def test_05_topk_and_mrr_recompute_from_case_summary(self):
        metrics = self.metrics["metrics"]
        denominator = len(self.case_rows)
        self.assertEqual(denominator, metrics["cases_evaluated"])
        reciprocal_sum = sum(float(row["reciprocal_rank"]) for row in self.case_rows)
        self.assertAlmostEqual(reciprocal_sum / denominator, metrics["mrr"])
        self.assertAlmostEqual(reciprocal_sum, metrics["mrr_numerator"])
        for k in K_VALUES:
            numerator = sum(int(row[f"hit_top_{k}"]) for row in self.case_rows)
            self.assertEqual(numerator, metrics[f"top_{k}_numerator"])
            self.assertEqual(denominator, metrics[f"top_{k}_denominator"])
            self.assertAlmostEqual(numerator / denominator, metrics[f"top_{k}"])

    def test_06_summary_matches_ranking_reference_positions(self):
        by_case = {}
        for row in self.result_rows:
            if row["is_reference_code"] == "1":
                by_case[row["case_id"]] = int(row["candidate_rank"])
        for row in self.case_rows:
            rank = int(row["rank_ref"])
            if rank > 0:
                self.assertEqual(by_case[row["case_id"]], rank)
            else:
                self.assertNotIn(row["case_id"], by_case)

    def test_07_position_and_coverage_distributions_match(self):
        self.assertEqual(sum(int(row["cases"]) for row in self.position_rows), 1056)
        self.assertEqual(sum(int(row["cases"]) for row in self.coverage_rows), 1056)
        position = {row["position_bucket"]: int(row["cases"]) for row in self.position_rows}
        coverage = {row["coverage_class"]: int(row["cases"]) for row in self.coverage_rows}
        self.assertEqual(position["1"], 29)
        self.assertEqual(position["2-3"], 25)
        self.assertEqual(position["4-5"], 11)
        self.assertEqual(position["6-10"], 4)
        self.assertEqual(position["11-50"], 5)
        self.assertEqual(position[">50_or_not_retrieved"], 982)
        self.assertEqual(coverage["reference_code_absent_from_corpus"], 0)
        self.assertEqual(coverage["present_not_recovered_top_50"], 982)

    def test_08_compatibility_with_historical_is_true(self):
        self.assertTrue(self.compatibility["compatible"])
        self.assertTrue(self.compatibility["identical_case_id_set"])
        self.assertTrue(self.compatibility["identical_labels"])
        self.assertEqual(self.compatibility["eval_hash_historical"], EXPECTED_EVAL_SHA256)
        self.assertEqual(self.compatibility["eval_hash_normative"], EXPECTED_EVAL_SHA256)

    def test_09_output_hashes_match_run_metadata(self):
        for name, expected in self.run_metadata["output_sha256"].items():
            path = ROOT / self.run_metadata["outputs"][name]
            self.assertEqual(sha256(path), expected, name)

    def test_10_csv_outputs_use_lf_serialization_and_no_forbidden_components(self):
        for rel in self.metrics["outputs"].values():
            path = ROOT / rel
            if path.suffix == ".csv":
                data = path.read_bytes()
                self.assertNotIn(b"\r\n", data, path)
                self.assertTrue(data.endswith(b"\n"), path)
        validation = self.run_metadata["validation"]
        self.assertFalse(validation["llm_used"])
        self.assertFalse(validation["text2trade_used"])
        self.assertFalse(validation["hierarchical_bm25_used"])
        self.assertFalse(validation["candidate_pool_used"])
        self.assertFalse(validation["rag_used"])


if __name__ == "__main__":
    unittest.main()