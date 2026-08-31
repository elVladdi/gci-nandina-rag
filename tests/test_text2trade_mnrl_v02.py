import csv
import json
import unittest
from pathlib import Path

from src.retrieval.text2trade_mnrl_v02 import choose_hard_negative, historical_code_pools, normalize_code, read_csv
from tests.sha_contracts_v02 import assert_frozen_sha, git_content_sha256


ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "src/configs/text2trade_mnrl_v0.2.json"
HIST = ROOT / "data/processed/data_aduanas_historico_clase87_v0.2.csv"
EVAL = ROOT / "data/processed/data_aduanas_evalset_clase87_v0.2.csv"
MODEL = ROOT / "models/text2trade_mnrl_v0.2"
INDEX = ROOT / "data/processed/indexes/text2trade_mnrl_nandina8_v0.2"
TRAINING = ROOT / "outputs/training/text2trade_mnrl_v0.2/training_metadata.json"
OUT = ROOT / "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2"


def sha256(path: Path) -> str:
    return git_content_sha256(path)


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


class TestText2TradeMNRLV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(CFG.read_text(encoding="utf-8"))
        cls.training = json.loads(TRAINING.read_text(encoding="utf-8"))
        cls.index_metadata = json.loads((INDEX / "text2trade_mnrl_nandina8_v02_run_metadata.json").read_text(encoding="utf-8"))
        cls.integrity = json.loads((INDEX / "vector_integrity_gate_v0.2.json").read_text(encoding="utf-8"))
        cls.metrics = json.loads((OUT / "d1a_metrics.json").read_text(encoding="utf-8"))
        cls.historical = read_csv(HIST)
        cls.eval_rows = read_csv(EVAL)

    def test_01_frozen_inputs_and_config(self):
        frozen = self.config["frozen_inputs"]
        self.assertEqual(sha256(HIST), frozen["historical_sha256"])
        self.assertEqual(sha256(EVAL), frozen["eval_sha256"])
        self.assertEqual(self.config["training"]["loss"], "MultipleNegativesRankingLoss")
        self.assertEqual(self.config["training"]["epochs"], 1)
        self.assertEqual(self.config["training"]["seed"], 2026)
        self.assertFalse(self.config["training"]["devset_used_for_training_or_selection"])
        self.assertFalse(self.config["training"]["evalset_used_for_training_or_selection"])
        self.assertFalse(self.config["mcd"]["implemented_in_d1a"])

    def test_02_no_train_eval_leakage(self):
        self.assertSetEqual({row["DECLARACION"] for row in self.historical} & {row["DECLARACION"] for row in self.eval_rows}, set())
        self.assertSetEqual({row["id_unico"] for row in self.historical} & {row["id_unico"] for row in self.eval_rows}, set())
        self.assertSetEqual({row["case_id"] for row in self.historical} & {row["case_id"] for row in self.eval_rows}, set())
        audit = self.training["leakage_audit"]
        self.assertEqual(audit["dam_overlap_historical_eval"], 0)
        self.assertEqual(audit["id_overlap_historical_eval"], 0)
        self.assertEqual(audit["case_overlap_historical_eval"], 0)
        self.assertFalse(audit["eval_labels_used_for_training"])
        self.assertFalse(audit["eval_metric_used_for_selection"])

    def test_03_positive_pairs_and_hard_negative_rules(self):
        pairs = self.training["pairs"]
        self.assertEqual(pairs["historical_rows"], 2950)
        self.assertEqual(pairs["historical_unique_codes"], 66)
        self.assertEqual(pairs["normative_positive_rows"], 2950)
        self.assertEqual(pairs["missing_normative_positive_rows"], 0)
        self.assertTrue(pairs["positive_codes_unique_within_every_batch"])
        codes = historical_code_pools(self.historical, "NANDINA")
        for row in self.historical:
            positive = normalize_code(row["NANDINA"])
            negative, level = choose_hard_negative(row["case_id"], positive, codes)
            self.assertNotEqual(positive, negative)
            same_hs4 = any(code != positive and code[:4] == positive[:4] for code in codes)
            same_chapter = any(code != positive and code[:2] == positive[:2] for code in codes)
            self.assertEqual(level, "same_hs4_different_code" if same_hs4 else "same_chapter_different_code" if same_chapter else "other_historical_code")

    def test_04_new_index_mapping_and_hashes(self):
        artifacts = self.index_metadata["artifacts"]
        self.assertEqual(artifacts["vectors"]["shape"], [7644, 384])
        self.assertEqual(artifacts["vectors"]["dtype"], "float32")
        self.assertEqual(artifacts["docstore"]["records"], 7644)
        self.assertEqual(artifacts["id_map"]["records"], 7644)
        self.assertEqual(self.index_metadata["mapping"]["vectors_documents_codes"], [7644, 7644, 7644])
        self.assertRegex(artifacts["vectors"]["sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(artifacts["docstore"]["sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(artifacts["id_map"]["sha256"], r"^[0-9a-f]{64}$")
        self.assertTrue(self.index_metadata["mapping"]["id_map_matches_docstore"])

    def test_05_vector_integrity_gate_and_frozen_sample(self):
        self.assertEqual(self.integrity["status"], "PASS")
        self.assertEqual(self.integrity["sample_count"], 21)
        self.assertLessEqual(self.integrity["max_absolute_difference"], self.integrity["tolerance"])
        sample = ROOT / self.integrity["sample_csv"]
        assert_frozen_sha(self, sample, self.integrity["sample_csv_sha256"])
        self.assertEqual(len(read_csv_rows(sample)), self.integrity["sample_count"])
        self.assertEqual(self.integrity["byte_exact_count"], 9)

    def test_06_metrics_recompute_from_ranking_trace(self):
        cases = read_csv_rows(OUT / "d1a_case_summary.csv")
        trace = [json.loads(line) for line in (OUT / "d1a_ranked_codes_top200.jsonl").read_text(encoding="utf-8").splitlines() if line]
        by_case = {row["case_id"]: row for row in trace}
        self.assertEqual(len(cases), len(by_case), 1056)
        metrics = self.metrics["metrics"]
        for case in cases:
            candidates = by_case[case["case_id"]]["candidate_codes"]
            reference = case["nandina_ref"]
            rank = next((index for index, code in enumerate(candidates, 1) if code == reference), 0)
            self.assertEqual(rank, int(case["rank_ref"]))
        for k in (1, 3, 5, 10, 50):
            numerator = sum(int(case[f"hit_top_{k}"]) for case in cases)
            self.assertEqual(numerator, metrics[f"top_{k}_numerator"])
        for k in (100, 200):
            self.assertEqual(sum(int(case[f"hit_recall_{k}"]) for case in cases), metrics[f"recall_at_{k}_numerator"])
            expected_mrr = sum(float(case[f"mrr_at_{k}_contribution"]) for case in cases)
            self.assertAlmostEqual(expected_mrr, metrics[f"mrr_at_{k}_numerator"])
            for name in ("exact", "hs6", "hs4", "chapter"):
                self.assertEqual(sum(int(case[f"{name}_at_{k}"]) for case in cases), metrics[f"{name}_at_{k}_numerator"])
        self.assertEqual(metrics["top_1"], 0.0)
        self.assertAlmostEqual(metrics["recall_at_100"], 0.3456439393939394)
        self.assertAlmostEqual(metrics["mrr_at_100"], 0.03242432639034634)

    def test_07_eval_compatibility_and_no_forbidden_components(self):
        d0_cases = read_csv_rows(ROOT / "outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/text2trade_case_summary.csv")
        d1_cases = read_csv_rows(OUT / "d1a_case_summary.csv")
        self.assertSetEqual({row["case_id"] for row in d0_cases}, {row["case_id"] for row in d1_cases})
        validation = self.metrics["validation"]
        self.assertTrue(validation["vector_integrity_passed_before_eval"])
        self.assertFalse(validation["evalset_used_for_training_or_selection"])
        self.assertFalse(validation["mcd_used"])
        self.assertFalse(validation["candidate_pool_used"])
        self.assertFalse(validation["phase_e_started"])
        self.assertTrue(validation["ranking_codes_unique"])

    def test_08_comparison_names_d0_and_d1a_explicitly(self):
        rows = read_csv_rows(OUT / "strategy_comparison_a_b_c_d0_d1a_v0.2.csv")
        names = {row["strategy"] for row in rows}
        self.assertSetEqual(names, {"Historical BM25", "Normative BM25 flat", "Normative BM25 hierarchical", "D0 pretrained dense SBERT baseline", "D1a Text2Trade-inspired MNRL"})
        d1 = {row["metric"]: row["value"] for row in rows if row["strategy"] == "D1a Text2Trade-inspired MNRL"}
        self.assertAlmostEqual(float(d1["Recall@100"]), 0.3456439393939394)
        self.assertAlmostEqual(float(d1["MRR@200"]), 0.03254853477630825)


if __name__ == "__main__":
    unittest.main()
