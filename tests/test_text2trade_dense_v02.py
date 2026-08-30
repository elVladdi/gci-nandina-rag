import csv
import hashlib
import json
import unittest
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2"
EXPECTED_EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
EXPECTED_CORPUS_SHA256 = "83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0"
EXPECTED_DOCSTORE_SHA256 = "acff90a10c3a0e52e8a8a6adbaf98fd747b76af01218acffcff00956952a5721"
EXPECTED_VECTORS_SHA256 = "67cd07f96fe98712940db467ea2510018698e40e3b3a24e8478256e62e0f3773"
K_VALUES = [1, 3, 5, 10, 50]
RECALL_VALUES = [100, 200]
HIER_VALUES = [100, 200]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def mrr_at(rank: int, k: int) -> float:
    return 1.0 / rank if 1 <= rank <= k else 0.0


class TestText2TradeDenseV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metadata = load_json(OUT / "run_metadata.json")
        cls.metrics_payload = load_json(OUT / "text2trade_metrics.json")
        cls.coverage = load_json(OUT / "text2trade_coverage_summary.json")
        cls.hierarchical_coverage = load_json(OUT / "text2trade_hierarchical_coverage.json")
        cls.compatibility = load_json(OUT / "historical_flat_hierarchical_text2trade_compatibility_v0.2.json")
        cls.model_manifest = load_json(OUT / "model_manifest.json")
        cls.case_rows = rows(OUT / "text2trade_case_summary.csv")
        cls.result_rows = rows(OUT / "text2trade_results.csv")
        cls.position_rows = rows(OUT / "position_distribution.csv")
        cls.comparison_rows = rows(OUT / "strategy_comparison_v0.2.csv")

    def test_01_expected_outputs_exist(self):
        for rel in self.metadata["outputs"].values():
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_02_eval_and_corpus_hashes_are_locked(self):
        inputs = self.metadata["inputs"]
        self.assertEqual(inputs["evalset_sha256"], EXPECTED_EVAL_SHA256)
        self.assertEqual(inputs["source_corpus_sha256"], EXPECTED_CORPUS_SHA256)
        self.assertEqual(inputs["docstore_sha256"], EXPECTED_DOCSTORE_SHA256)
        self.assertEqual(inputs["vectors_sha256"], EXPECTED_VECTORS_SHA256)
        self.assertNotIn("v0.1", inputs["evalset"])
        self.assertTrue(self.metadata["validation"]["evalset_hash_matches_official_v02"])

    def test_03_scope_cases_and_labels_are_v02(self):
        self.assertEqual(len(self.case_rows), 1056)
        self.assertEqual(len({row["case_id"] for row in self.case_rows}), 1056)
        self.assertTrue(all(row["case_id"].startswith("DA-EVAL-V02-") for row in self.case_rows))
        self.assertTrue(all(row["clase_ref"] == "87" for row in self.case_rows))
        self.assertEqual(len({row["nandina_ref"] for row in self.case_rows}), 42)

    def test_04_model_identity_is_recorded(self):
        manifest = self.model_manifest
        self.assertEqual(manifest["model_id"], "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        self.assertEqual(manifest["embedding_dim"], 384)
        self.assertEqual(manifest["device"], "cpu")
        self.assertTrue(manifest["normalize_embeddings"])
        self.assertEqual(manifest["similarity_metric"], "cosine via dot product over normalized vectors")
        self.assertEqual(manifest["pooling"]["pooling_mode_mean_tokens"], True)
        self.assertEqual(manifest["tokenizer_max_length"], 128)
        self.assertEqual(manifest["revision_status"], "not recorded in local Text2Trade artifact metadata")
        self.assertTrue(any(file["path"].endswith("model.safetensors") for file in manifest["files"]))

    def test_05_compatibility_with_phase_a_b_c(self):
        self.assertTrue(self.compatibility["compatible"])
        self.assertTrue(self.compatibility["identical_case_id_sets"])
        self.assertTrue(self.compatibility["identical_historical_case_id_set"])
        self.assertTrue(self.compatibility["identical_flat_case_id_set"])
        self.assertTrue(self.compatibility["identical_hierarchical_case_id_set"])
        self.assertTrue(self.compatibility["identical_labels"])
        self.assertEqual(self.compatibility["eval_hash_text2trade"], EXPECTED_EVAL_SHA256)

    def test_06_effective_ranking_has_unique_codes(self):
        by_case = defaultdict(list)
        for row in self.result_rows:
            by_case[row["case_id"]].append(row["candidate_code"])
        self.assertEqual(set(by_case), {row["case_id"] for row in self.case_rows})
        for case_id, codes in by_case.items():
            self.assertEqual(len(codes), 200, case_id)
            self.assertEqual(len(codes), len(set(codes)), case_id)
        self.assertTrue(self.metadata["validation"]["ranking_effective_codes_unique"])

    def test_07_topk_recall_and_mrr_recompute(self):
        metrics = self.metadata["metrics"]
        denominator = len(self.case_rows)
        self.assertEqual(denominator, metrics["cases_evaluated"])
        for k in K_VALUES:
            numerator = sum(int(row[f"hit_top_{k}"]) for row in self.case_rows)
            self.assertEqual(numerator, metrics[f"top_{k}_numerator"])
            self.assertAlmostEqual(numerator / denominator, metrics[f"top_{k}"])
        for k in RECALL_VALUES:
            numerator = sum(int(row[f"hit_recall_{k}"]) for row in self.case_rows)
            self.assertEqual(numerator, metrics[f"recall_at_{k}_numerator"])
            self.assertAlmostEqual(numerator / denominator, metrics[f"recall_at_{k}"])
        for k in RECALL_VALUES:
            numerator = sum(mrr_at(int(row["rank_ref"]), k) for row in self.case_rows)
            self.assertAlmostEqual(numerator, metrics[f"mrr_at_{k}_numerator"])
            self.assertAlmostEqual(numerator / denominator, metrics[f"mrr_at_{k}"])

    def test_08_hierarchical_metrics_recompute_from_rankings(self):
        by_case = defaultdict(list)
        for row in self.result_rows:
            by_case[row["case_id"]].append(row)
        counts = {k: {"exact": 0, "hs6": 0, "hs4": 0, "chapter": 0} for k in HIER_VALUES}
        for case in self.case_rows:
            ref = case["nandina_ref"]
            candidates = sorted(by_case[case["case_id"]], key=lambda row: int(row["candidate_rank"]))
            for k in HIER_VALUES:
                top = [row["candidate_code"] for row in candidates if int(row["candidate_rank"]) <= k]
                counts[k]["exact"] += int(any(code == ref for code in top))
                counts[k]["hs6"] += int(any(code[:6] == ref[:6] for code in top))
                counts[k]["hs4"] += int(any(code[:4] == ref[:4] for code in top))
                counts[k]["chapter"] += int(any(code[:2] == ref[:2] for code in top))
        metrics = self.metadata["metrics"]
        for k in HIER_VALUES:
            for name in ["exact", "hs6", "hs4", "chapter"]:
                self.assertEqual(counts[k][name], metrics[f"{name}_at_{k}_numerator"])

    def test_09_corpus_coverage_recomputes(self):
        eval_codes = {row["nandina_ref"] for row in self.case_rows}
        docstore = []
        with (ROOT / self.metadata["inputs"]["docstore"]).open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    docstore.append(json.loads(line))
        corpus_codes = {str(row["codigo"]).strip() for row in docstore}
        self.assertEqual(len(eval_codes), 42)
        self.assertEqual(len(eval_codes & corpus_codes), 42)
        self.assertEqual(sum(1 for row in self.case_rows if row["reference_code_in_corpus"] == "True"), 1056)
        self.assertEqual(self.coverage["eval_cases_absent_from_corpus"], 0)
        self.assertFalse(self.coverage["parent_codes_counted_as_exact_coverage"])

    def test_10_position_distribution_sums(self):
        total = sum(int(row["cases"]) for row in self.position_rows)
        self.assertEqual(total, 1056)
        self.assertEqual(int({row["position_bucket"]: row for row in self.position_rows}["101-200"]["cases"]), 7)
        self.assertEqual(int({row["position_bucket"]: row for row in self.position_rows}[">200_or_not_retrieved"]["cases"]), 1045)

    def test_11_strategy_comparison_uses_approved_values(self):
        by_metric = {row["metric"]: row for row in self.comparison_rows}
        self.assertEqual(by_metric["Recall@100"]["historical"], "")
        self.assertAlmostEqual(float(by_metric["MRR@100"]["flat"]), 0.04229731726741296)
        self.assertAlmostEqual(float(by_metric["MRR@100"]["hierarchical"]), 0.04198129438896377)
        self.assertAlmostEqual(float(by_metric["MRR@100"]["text2trade"]), 6.046196473541642e-05)

    def test_12_no_forbidden_components_or_leakage(self):
        validation = self.metadata["validation"]
        self.assertEqual(validation["label_string_found_inside_query_count"], 0)
        self.assertFalse(validation["dam_used_as_query_feature"])
        self.assertFalse(validation["serie_used_as_query_feature"])
        self.assertFalse(validation["historical_results_used_as_retrieval_features"])
        self.assertFalse(validation["flat_results_used_as_retrieval_features"])
        self.assertFalse(validation["hierarchical_results_used_as_retrieval_features"])
        self.assertFalse(validation["candidate_pool_used"])
        self.assertFalse(validation["dual_protected_used"])
        self.assertFalse(validation["mixed_70_30_used"])
        self.assertFalse(validation["rag_used"])
        self.assertFalse(validation["llm_used"])
        self.assertFalse(validation["phase_e_started"])

    def test_13_output_hashes_match_run_metadata(self):
        for name, expected in self.metadata["output_sha256"].items():
            path = ROOT / self.metadata["outputs"][name]
            self.assertEqual(sha256(path), expected, name)

    def test_14_previous_phase_outputs_preserved(self):
        status = self.metadata["previous_phase_artifact_hashes"]
        self.assertTrue(status["all_match_expected"])
        for entry in status["entries"].values():
            self.assertEqual(sha256(ROOT / entry["path"]), entry["expected_sha256"])
            self.assertEqual(entry["actual_sha256"], entry["expected_sha256"])

    def test_15_large_outputs_policy(self):
        versioned_outputs = [ROOT / rel for rel in self.metadata["outputs"].values()]
        over_50mb = [path for path in versioned_outputs if path.exists() and path.stat().st_size > 50 * 1024 * 1024]
        self.assertEqual(over_50mb, [])
        over_25mb = [path.name for path in versioned_outputs if path.exists() and path.stat().st_size > 25 * 1024 * 1024]
        self.assertEqual(over_25mb, ["text2trade_results.csv"])
        self.assertFalse(self.metadata["validation"]["large_outputs_over_50mb_versioned"])

    def test_16_metadata_reproducibility(self):
        self.assertEqual(self.metadata["experiment_id"], "exp04_phase_d_text2trade_dense_v0.2")
        self.assertEqual(self.metadata["strategy"], "text2trade_dense")
        self.assertEqual(self.metadata["dataset_version"], "v0.2")
        self.assertEqual(self.metadata["parameters"]["retrieval_depth"], 200)
        self.assertEqual(self.metadata["parameters"]["batch_size"], 32)
        self.assertTrue(self.metadata["parameters"]["brute_force_used"])
        self.assertFalse(self.metadata["parameters"]["hnsw_index_exists"])
        self.assertFalse(self.metadata["parameters"]["mcd_used_in_run"])
        self.assertEqual(self.metadata["columns"]["query"], "DESCRIPCION DE MERCANCIAS CONCATENADA")

    def test_17_gate_d_is_approved(self):
        self.assertEqual(self.metadata["gate_d_status"], "GATE D APROBADO")
        self.assertTrue(self.metadata["validation"]["compatibility_true"])
        self.assertTrue(self.metadata["validation"]["previous_phase_artifacts_preserved"])


if __name__ == "__main__":
    unittest.main()
