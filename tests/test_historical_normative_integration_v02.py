import csv
import hashlib
import json
import unittest
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2"
CONFIG_PATH = ROOT / "src/configs/historical_normative_integration_v0.2.json"
EVAL_HASH = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_jsonl(path: Path):
    with path.open(encoding="utf-8-sig") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


class TestHistoricalNormativeIntegrationV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        cls.metadata = json.loads((OUT / "integration_run_metadata.json").read_text(encoding="utf-8"))
        cls.metrics = json.loads((OUT / "integration_metrics.json").read_text(encoding="utf-8"))
        cls.coverage = json.loads((OUT / "integration_evidence_coverage.json").read_text(encoding="utf-8"))
        cls.ranking_invariance = json.loads((OUT / "integration_ranking_invariance.json").read_text(encoding="utf-8"))
        cls.top3_invariance = json.loads((OUT / "integration_top3_invariance.json").read_text(encoding="utf-8"))
        cls.traceability = json.loads((OUT / "integration_traceability.json").read_text(encoding="utf-8"))
        cls.compatibility = json.loads((OUT / "integration_compatibility.json").read_text(encoding="utf-8"))
        cls.label_audit = json.loads((OUT / "integration_label_leakage_audit.json").read_text(encoding="utf-8"))
        cls.eval_rows = read_csv(ROOT / cls.config["eval"]["path"])
        cls.historical_rows = read_csv(ROOT / cls.config["historical_ranking"]["path"])
        cls.history_rows = read_csv(ROOT / cls.config["historical_dataset"]["path"])
        cls.slots = read_csv(OUT / "integration_candidate_slots.csv")
        cls.case_summary = read_csv(OUT / "integration_case_summary.csv")

    def test_01_eval_hash_and_case_count_are_frozen(self) -> None:
        self.assertEqual(sha256(ROOT / self.config["eval"]["path"]), EVAL_HASH)
        self.assertEqual(len(self.eval_rows), 1056)
        self.assertEqual(len({row["case_id"] for row in self.eval_rows}), 1056)
        self.assertTrue(all(row["case_id"].startswith("DA-EVAL-V02-") for row in self.eval_rows))

    def test_02_exactly_three_historical_candidates_per_case(self) -> None:
        grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in self.slots:
            grouped[row["case_id"]].append(row)
        self.assertEqual(len(grouped), 1056)
        self.assertEqual(len(self.slots), 3168)
        for case_id, rows in grouped.items():
            self.assertEqual([int(row["historical_rank"]) for row in rows], [1, 2, 3], case_id)
        self.assertEqual(self.compatibility["candidate_slots"], 3168)

    def test_03_top3_codes_scores_and_order_equal_phase_a(self) -> None:
        before: dict[tuple[str, str], tuple[str, str]] = {}
        for row in self.historical_rows:
            if row["method"] == self.config["historical_ranking"]["method"] and int(row["candidate_rank"]) <= 3:
                before[(row["case_id"], row["candidate_rank"])] = (row["candidate_nandina"], row["score"])
        after = {(row["case_id"], row["historical_rank"]): (row["historical_candidate_code"], row["historical_score"]) for row in self.slots}
        self.assertEqual(before, after)
        self.assertEqual(len(before), 3168)
        self.assertTrue(self.ranking_invariance["pass"])
        self.assertTrue(self.top3_invariance["pass"])

    def test_04_no_normative_candidate_or_score_affects_order(self) -> None:
        self.assertFalse(self.ranking_invariance["normative_score_affects_order"])
        self.assertTrue(self.ranking_invariance["no_new_candidate_inserted"])
        self.assertTrue(self.ranking_invariance["no_candidate_removed"])
        self.assertEqual(self.ranking_invariance["historical_results_sha256_before"], self.ranking_invariance["historical_results_sha256_after"])
        self.assertEqual(self.ranking_invariance["historical_results_sha256_before"], self.config["historical_ranking"]["sha256"])

    def test_05_precedents_are_only_frozen_historical_v02_rows(self) -> None:
        history = {row["case_id"]: row for row in self.history_rows}
        self.assertEqual(len(history), len(self.history_rows))
        for slot in self.slots:
            precedent = history[slot["historical_precedent_case_id"]]
            self.assertEqual(precedent["split"], "historico")
            self.assertEqual(precedent["NANDINA"], slot["historical_candidate_code"])
            self.assertEqual(precedent["id_unico"], slot["historical_precedent_id_unico"])
            self.assertEqual(precedent["DECLARACION"], slot["historical_precedent_dam"])
            self.assertEqual(int(slot["historical_precedent_count"]), 1)

    def test_06_evidence_mapping_is_direct_and_recalculable(self) -> None:
        corpus = {}
        for row in read_jsonl(ROOT / self.config["normative_corpus"]["path"]):
            code = str(row.get("nandina_8d") or row.get("codigo") or "").strip()
            if len(code) == 8 and code.isdigit() and code not in corpus:
                corpus[code] = row
        for slot in self.slots:
            document = corpus[slot["historical_candidate_code"]]
            self.assertEqual(slot["normative_doc_ids"], document["doc_id"])
            self.assertEqual(slot["normative_document_code"], slot["historical_candidate_code"])
            self.assertEqual(slot["has_exact_nandina8_evidence"], "1")
            self.assertEqual(int(slot["has_hs6_evidence"]), int(document.get("hs_6d", "") == slot["historical_candidate_code"][:6]))
            self.assertEqual(int(slot["has_hs4_evidence"]), int(document.get("partida_4d", "") == slot["historical_candidate_code"][:4]))
            self.assertEqual(int(slot["has_chapter_evidence"]), int(document.get("chapter", "") == slot["historical_candidate_code"][:2]))

    def test_07_coverage_and_case_distribution_recompute(self) -> None:
        for field, key in (("has_exact_nandina8_evidence", "exact_nandina8"), ("has_hs6_evidence", "hs6"), ("has_hs4_evidence", "hs4"), ("has_chapter_evidence", "chapter")):
            numerator = sum(int(row[field]) for row in self.slots)
            self.assertEqual(numerator, self.coverage[key]["numerator"])
            self.assertAlmostEqual(numerator / len(self.slots), self.coverage[key]["rate"])
        counts = Counter(row["exact_evidence_candidates"] for row in self.case_summary)
        self.assertEqual({key: value for key, value in counts.items()}, {key: value for key, value in self.coverage["cases_exact_evidence_count"].items() if value})
        self.assertEqual(len(self.case_summary), 1056)

    def test_08_traceability_and_missing_exact_evidence_recompute(self) -> None:
        complete = sum(int(row["traceability_complete"]) for row in self.slots)
        self.assertEqual(complete, self.traceability["complete"]["numerator"])
        self.assertEqual(complete, self.metrics["candidate_slots"])
        missing = read_csv(OUT / "integration_missing_exact_evidence.csv")
        self.assertEqual(len(missing), sum(not int(row["has_exact_nandina8_evidence"]) for row in self.slots))

    def test_09_label_leakage_and_forbidden_components_are_excluded(self) -> None:
        self.assertTrue(self.label_audit["pass"])
        self.assertTrue(self.label_audit["labels_only_used_after_construction_for_metrics"])
        for key in ("label_used_for_candidate_selection", "label_used_for_precedent_selection", "label_used_for_evidence_selection", "label_used_for_order_or_fallback"):
            self.assertFalse(self.label_audit[key])
        self.assertFalse(self.metrics["llm_used"])
        self.assertFalse(self.metrics["reranker_used"])
        self.assertFalse(self.metrics["candidate_pool_used"])
        self.assertFalse(self.metrics["d1a_used"])

    def test_10_compatibility_and_frozen_phase_artifacts_hold(self) -> None:
        self.assertTrue(self.compatibility["compatible"])
        self.assertTrue(self.compatibility["ranking_unchanged"])
        self.assertTrue(self.compatibility["exactly_three_historical_candidates_per_case"])
        for name, entry in self.config["frozen_phase_artifacts"].items():
            self.assertEqual(sha256(ROOT / entry["path"]), entry["sha256"], name)
        self.assertNotIn("v0.1", self.config["eval"]["path"])
        self.assertNotIn("v0.1", self.config["historical_ranking"]["path"])

    def test_11_output_hashes_match_metadata(self) -> None:
        self.assertTrue(self.metadata["output_sha256_excludes_self_referential_metadata"])
        for name, digest in self.metadata["output_sha256"].items():
            self.assertEqual(sha256(ROOT / self.metadata["outputs"][name]), digest, name)


if __name__ == "__main__":
    unittest.main()
