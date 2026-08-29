import csv
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "evaluation" / "normative_bm25_hierarchical_data_aduanas_clase87_v0.2"
HIST_OUT = ROOT / "outputs" / "evaluation" / "historical_retrieval_data_aduanas_clase87_v0.2"
FLAT_OUT = ROOT / "outputs" / "evaluation" / "normative_bm25_flat_data_aduanas_clase87_v0.2"

EXPECTED_EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
EXPECTED_CORPUS_SHA256 = "f389ae6c303279cfea23697cbedb3315a5254254c2efc2450cf28f81243df175"
EXPECTED_INDEX_SHA256 = "f828736ea700471c95d2b985bdd969d751cd36c3ca01c407049209010bdbe60b"
EXPECTED_FLAT_HASHES = {
    "normative_results.csv": "d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015",
    "normative_case_summary.csv": "f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0",
    "normative_metrics.json": "56a702398d3b9d1483ecd1be3ca79587682ad8fd3afd84858917f248b5ae0460",
    "run_metadata.json": "e57d1ebd360790c64b485f5fb4d7aa34be500e48f4ebf48ab7c0437874caba44",
}
EXPECTED_HIST_HASHES = {
    "historical_results.csv": "c350b63e0180a4c28573d2626c76d030308913b690c524d2d62ea439cf34a6c8",
    "historical_case_summary.csv": "f8f4ac6d585194aace74c50f495720cc87b0c09a28438d888b0030dfaddd0d56",
    "historical_metrics.json": "5334e64ab2b3f812f939b652fe1ee8ad8db24b673ebb48fd4d7b1ddb0dd444fa",
    "run_metadata.json": "edb8bd3343418714fb6736f896c8831aeebe8ecec2f31599bb84ad32722a3a32",
}
K_VALUES = [1, 3, 5, 10, 50]
RECALL_VALUES = [50, 100, 200]
HIER_VALUES = [10, 50, 100, 200]


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


class TestNormativeBm25HierarchicalV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metadata = load_json(OUT / "run_metadata.json")
        cls.metrics_payload = load_json(OUT / "normative_hierarchical_metrics.json")
        cls.coverage = load_json(OUT / "hierarchical_coverage_summary.json")
        cls.corpus_audit = load_json(OUT / "corpus_hierarchical_audit.json")
        cls.compatibility = load_json(OUT / "historical_flat_vs_normative_hierarchical_compatibility_v0.2.json")
        cls.case_rows = rows(OUT / "normative_hierarchical_case_summary.csv")
        cls.result_rows = rows(OUT / "normative_hierarchical_results.csv")
        cls.position_rows = rows(OUT / "position_distribution.csv")
        cls.coverage_rows = rows(OUT / "hierarchical_coverage_summary.csv")
        cls.comparison_rows = rows(OUT / "flat_vs_hierarchical_comparison_v0.2.csv")
        cls.coverage_comparison_rows = rows(OUT / "hierarchical_coverage_comparison_v0.2.csv")
        cls.stratified_rows = rows(OUT / "limitation_stratified_metrics_v0.2.csv")

    def test_01_expected_outputs_exist(self):
        for rel in self.metadata["outputs"].values():
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_02_input_hashes_are_locked(self):
        inputs = self.metadata["inputs"]
        self.assertEqual(inputs["evalset_sha256"], EXPECTED_EVAL_SHA256)
        self.assertEqual(inputs["hierarchical_corpus_sha256"], EXPECTED_CORPUS_SHA256)
        self.assertEqual(inputs["hierarchical_index_sha256"], EXPECTED_INDEX_SHA256)
        self.assertNotIn("v0.1", inputs["evalset"])
        self.assertTrue(self.metadata["validation"]["hierarchical_methodology_uses_existing_v01_corpus_artifact"])

    def test_03_eval_scope_and_cases_are_v02(self):
        case_ids = [row["case_id"] for row in self.case_rows]
        self.assertEqual(len(case_ids), 1056)
        self.assertEqual(len(set(case_ids)), 1056)
        self.assertTrue(all(case_id.startswith("DA-EVAL-V02-") for case_id in case_ids))
        self.assertEqual(len({row["nandina_ref"] for row in self.case_rows}), 42)
        self.assertTrue(all(row["clase_ref"] == "87" for row in self.case_rows))

    def test_04_compatibility_with_phase_a_and_b(self):
        self.assertTrue(self.compatibility["compatible"])
        self.assertTrue(self.compatibility["identical_case_id_set"])
        self.assertTrue(self.compatibility["identical_labels"])
        self.assertEqual(self.compatibility["eval_hash_historical"], EXPECTED_EVAL_SHA256)
        self.assertEqual(self.compatibility["eval_hash_flat"], EXPECTED_EVAL_SHA256)
        self.assertEqual(self.compatibility["eval_hash_hierarchical"], EXPECTED_EVAL_SHA256)

    def test_05_corpus_hierarchical_audit_is_frozen(self):
        audit = self.corpus_audit
        self.assertEqual(audit["records_total"], 7648)
        self.assertEqual(audit["nandina_8_rows"], 7648)
        self.assertEqual(audit["nandina_8_unique_codes"], 7644)
        self.assertEqual(audit["nandina_8_codes_with_multiple_documents"], 2)
        self.assertEqual(audit["total_extra_documents_from_duplicate_codes"], 4)
        self.assertEqual(audit["metadata_counts"]["cantidad_sin_padre_4d"], 407)
        self.assertEqual(audit["metadata_counts"]["cantidad_sin_padre_hs6"], 4504)
        self.assertEqual(audit["metadata_counts"]["cantidad_sin_padres"], 185)
        self.assertEqual(audit["versioned_audit_counts"]["source_conflicting_parent_duplicates"], 56)
        self.assertTrue(audit["methodology_linkage"]["linked_to_approved_methodology"])

    def test_06_ranking_effective_codes_are_unique(self):
        by_case: dict[str, list[str]] = {}
        for row in self.result_rows:
            by_case.setdefault(row["case_id"], []).append(row["candidate_code"])
        self.assertEqual(set(by_case), {row["case_id"] for row in self.case_rows})
        for case_id, codes in by_case.items():
            self.assertEqual(len(codes), len(set(codes)), case_id)
            self.assertLessEqual(len(codes), 200)
        self.assertTrue(self.metadata["validation"]["final_ranking_effective_codes_unique"])
        self.assertEqual(self.metadata["validation"]["cases_with_repeated_codes_in_effective_ranking"], 0)
        self.assertEqual(self.metadata["validation"]["cases_with_repeated_codes_in_raw_ranking"], 303)

    def test_07_topk_recall_and_mrr_recompute(self):
        metrics = self.metadata["metrics"]
        denominator = len(self.case_rows)
        self.assertEqual(denominator, metrics["cases_evaluated"])
        reciprocal_sum = sum(float(row["reciprocal_rank"]) for row in self.case_rows)
        self.assertAlmostEqual(reciprocal_sum, metrics["mrr_numerator"])
        self.assertAlmostEqual(reciprocal_sum / denominator, metrics["mrr"])
        for k in K_VALUES:
            numerator = sum(int(row[f"hit_top_{k}"]) for row in self.case_rows)
            self.assertEqual(numerator, metrics[f"top_{k}_numerator"])
            self.assertAlmostEqual(numerator / denominator, metrics[f"top_{k}"])
        for k in RECALL_VALUES:
            numerator = sum(int(row[f"hit_recall_{k}"]) for row in self.case_rows)
            self.assertEqual(numerator, metrics[f"recall_at_{k}_numerator"])
            self.assertAlmostEqual(numerator / denominator, metrics[f"recall_at_{k}"])
        self.assertEqual(metrics["pool_recall_at_200"], metrics["recall_at_200"])

    def test_08_hierarchical_coverage_recomputes(self):
        metrics = self.metadata["metrics"]
        denominator = len(self.case_rows)
        for k in HIER_VALUES:
            for name in ["exact", "hs6", "hs4", "chapter"]:
                numerator = sum(int(row[f"{name}_at_{k}"]) for row in self.case_rows)
                self.assertEqual(numerator, metrics[f"{name}_at_{k}_numerator"])
                self.assertAlmostEqual(numerator / denominator, metrics[f"{name}_at_{k}"])
        self.assertEqual(metrics["exact_at_100_numerator"], 107)
        self.assertEqual(metrics["hs6_at_100_numerator"], 118)
        self.assertEqual(metrics["hs4_at_100_numerator"], 264)
        self.assertEqual(metrics["chapter_at_100_numerator"], 538)
        self.assertEqual(metrics["exact_at_200_numerator"], 321)
        self.assertEqual(metrics["hs6_at_200_numerator"], 363)
        self.assertEqual(metrics["hs4_at_200_numerator"], 529)
        self.assertEqual(metrics["chapter_at_200_numerator"], 810)

    def test_09_position_and_coverage_distributions_match(self):
        positions = {row["position_bucket"]: int(row["cases"]) for row in self.position_rows}
        self.assertEqual(sum(positions.values()), 1056)
        self.assertEqual(positions["1"], 28)
        self.assertEqual(positions["2-3"], 27)
        self.assertEqual(positions["4-5"], 11)
        self.assertEqual(positions["6-10"], 3)
        self.assertEqual(positions["11-50"], 27)
        self.assertEqual(positions["51-100"], 11)
        self.assertEqual(positions["101-200"], 214)
        self.assertEqual(positions[">200_or_not_retrieved"], 735)
        by_k: dict[str, int] = {}
        for row in self.coverage_rows:
            by_k[row["k"]] = by_k.get(row["k"], 0) + int(row["cases"])
        self.assertEqual(by_k, {"100": 1056, "200": 1056})

    def test_10_no_leakage_or_forbidden_components(self):
        validation = self.metadata["validation"]
        self.assertEqual(validation["label_string_found_inside_query_count"], 0)
        self.assertFalse(validation["llm_used"])
        self.assertFalse(validation["text2trade_used"])
        self.assertFalse(validation["dual_protected_used"])
        self.assertFalse(validation["candidate_pool_used"])
        self.assertFalse(validation["dense_retrieval_used"])
        self.assertFalse(validation["rag_used"])
        self.assertFalse(validation["historical_results_used_as_retrieval_features"])
        self.assertFalse(validation["flat_results_used_as_retrieval_features"])
        self.assertFalse(validation["dam_used_as_query_feature"])
        self.assertFalse(validation["serie_used_as_query_feature"])

    def test_11_flat_vs_hierarchical_comparison_values(self):
        rows_by_metric = {row["metric"]: row for row in self.comparison_rows}
        self.assertAlmostEqual(float(rows_by_metric["Top-1"]["flat_v0_2"]), 0.027462121212121212)
        self.assertAlmostEqual(float(rows_by_metric["Top-1"]["hierarchical_v0_2"]), 0.026515151515151516)
        self.assertAlmostEqual(float(rows_by_metric["Recall@100"]["hierarchical_v0_2"]), 0.10132575757575757)
        self.assertAlmostEqual(float(rows_by_metric["MRR"]["hierarchical_v0_2"]), 0.04334161160288281)

    def test_12_corpus_coverage_classes_are_separated(self):
        self.assertEqual(self.coverage["eval_codes_covered_by_corpus"], 42)
        self.assertEqual(self.coverage["eval_cases_covered_by_corpus"], 1056)
        self.assertEqual(self.coverage["eval_cases_absent_from_corpus"], 0)
        self.assertEqual(self.coverage["reference_present_but_not_exact_at_100"], 949)
        self.assertEqual(self.coverage["hs6_recovered_without_exact_at_100"], 11)
        self.assertEqual(self.coverage["hs4_recovered_without_hs6_or_exact_at_100"], 146)
        self.assertEqual(self.coverage["chapter_only_at_100"], 274)
        self.assertEqual(self.coverage["no_hierarchical_evidence_at_100"], 518)

    def test_13_stratified_limitations_are_present(self):
        groups = {row["group"]: row for row in self.stratified_rows}
        self.assertEqual(set(groups), {"all_cases", "missing_parent_4d", "missing_parent_hs6", "missing_both_parents", "duplicate_code_documents", "generic_or_short_leaf_description"})
        self.assertEqual(int(groups["all_cases"]["n"]), 1056)
        self.assertEqual(int(groups["missing_parent_hs6"]["n"]), 381)
        self.assertEqual(int(groups["generic_or_short_leaf_description"]["n"]), 369)

    def test_14_output_hashes_and_lf_serialization(self):
        for name, expected in self.metadata["output_sha256"].items():
            path = ROOT / self.metadata["outputs"][name]
            self.assertEqual(sha256(path), expected, name)
        for rel in self.metadata["outputs"].values():
            path = ROOT / rel
            if path.suffix in {".csv", ".json", ".md"}:
                data = path.read_bytes()
                self.assertNotIn(b"\r\n", data, path)
                self.assertTrue(data.endswith(b"\n"), path)

    def test_15_previous_phase_outputs_preserved(self):
        for name, expected in EXPECTED_FLAT_HASHES.items():
            self.assertEqual(sha256(FLAT_OUT / name), expected, name)
        for name, expected in EXPECTED_HIST_HASHES.items():
            self.assertEqual(sha256(HIST_OUT / name), expected, name)
        self.assertTrue(self.metadata["previous_phase_artifact_hashes"]["all_match_expected"])

    def test_16_gate_c_is_approved(self):
        self.assertEqual(self.metadata["gate_c_status"], "APPROVED")
        self.assertEqual(self.metrics_payload["gate_c_status"], "APPROVED")


if __name__ == "__main__":
    unittest.main()
