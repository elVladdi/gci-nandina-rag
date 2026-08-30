from __future__ import annotations

import csv
import hashlib
import json
import unittest
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2"
CONFIG = json.loads((ROOT / "src/configs/he4_pre_explainer_v0.2.json").read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class He4PreExplainerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sample = csv_rows(OUT / "he4_explainer_sample_v0.2.csv")
        cls.eval_only = csv_rows(OUT / "he4_sample_evaluation_only_v0.2.csv")
        cls.contexts = [json.loads(line) for line in (OUT / "he4_contexts_v0.2.jsonl").read_text(encoding="utf-8").splitlines() if line]
        cls.inputs = [json.loads(line) for line in (OUT / "he4_generation_inputs_v0.2.jsonl").read_text(encoding="utf-8").splitlines() if line]
        cls.invariance = json.loads((OUT / "he4_top3_invariance_v0.2.json").read_text(encoding="utf-8"))
        cls.compatibility = json.loads((OUT / "he4_sample_compatibility_v0.2.json").read_text(encoding="utf-8"))
        cls.gate = json.loads((OUT / "gate_h_pre_explainer_freeze_v0.2.json").read_text(encoding="utf-8"))

    def test_01_frozen_source_hashes_and_eval_scope(self) -> None:
        for name in ("eval", "historical_results", "historical_case_summary", "phase_f_slots", "corpus"):
            entry = CONFIG[name]
            self.assertEqual(sha256(ROOT / entry["path"]), entry["sha256"], name)
        self.assertEqual(len(csv_rows(ROOT / CONFIG["eval"]["path"])), 1056)

    def test_02_sample_is_exactly_fifty_unique_eval_cases(self) -> None:
        ids = {row["case_id"] for row in self.sample}
        eval_ids = {row["case_id"] for row in csv_rows(ROOT / CONFIG["eval"]["path"])}
        self.assertEqual(len(self.sample), 50)
        self.assertEqual(len(ids), 50)
        self.assertTrue(ids <= eval_ids)
        self.assertEqual({row["selection_target"] for row in self.sample}, {"rank_1", "rank_2_3", "rank_4_10", "difficult_low_support"})

    def test_03_rule_seed_and_sample_hash_are_frozen(self) -> None:
        self.assertEqual(CONFIG["sample"]["seed"], 2026)
        self.assertEqual(self.gate["hashes"]["sample"], sha256(OUT / "he4_explainer_sample_v0.2.csv"))
        self.assertEqual(self.gate["hashes"]["eval"], CONFIG["eval"]["sha256"])

    def test_04_contexts_and_generation_inputs_are_closed_top3(self) -> None:
        self.assertEqual(self.contexts, self.inputs)
        self.assertEqual(len(self.contexts), 50)
        for row in self.contexts:
            top3 = row["top3_original"]
            self.assertEqual([candidate["rank_original"] for candidate in top3], [1, 2, 3])
            self.assertEqual(len({candidate["nandina"] for candidate in top3}), 3)
            self.assertTrue(all(candidate["evidencia_historica"]["candidate_id_unico"] for candidate in top3))
            self.assertTrue(all(candidate["evidencia_normativa"]["doc_id"] for candidate in top3))

    def test_05_top3_and_evidence_invariants_hold(self) -> None:
        self.assertTrue(self.invariance["pass"])
        self.assertEqual(self.invariance["slots"], 150)
        self.assertEqual(self.invariance["exact_normative_evidence"], 150)
        self.assertTrue(self.invariance["codes_positions_scores_identical"])

    def test_06_labels_and_phase_g_are_absent_from_llm_inputs(self) -> None:
        forbidden = ("expected_nandina", "reference_nandina", "reference_rank", "correctness", "reranker", "diagnostic_reranked")
        for context in self.contexts:
            serialized = json.dumps(context, ensure_ascii=False).lower()
            self.assertFalse(any(value in serialized for value in forbidden))
        audit = json.loads((OUT / "he4_label_leakage_audit_v0.2.json").read_text(encoding="utf-8"))
        self.assertTrue(audit["pass"])
        self.assertTrue(audit["label_used_for_sample_design"])
        self.assertFalse(audit["label_exposed_to_llm"])

    def test_07_generation_is_not_executed(self) -> None:
        self.assertTrue(self.gate["ready_for_phase_i"])
        self.assertFalse(self.gate["llm_called"])
        self.assertFalse(self.gate["generation_outputs_exist"])
        self.assertFalse((OUT / "he4_responses_v0.2.jsonl").exists())

    def test_08_prompt_model_schema_rubric_and_compatibility_are_frozen(self) -> None:
        self.assertEqual(sha256(ROOT / CONFIG["prompt"]["path"]), CONFIG["prompt"]["sha256"])
        self.assertTrue((ROOT / CONFIG["schema"]["path"]).is_file())
        self.assertTrue((ROOT / CONFIG["rubric"]["path"]).is_file())
        self.assertTrue((OUT / "he4_model_manifest_v0.2.json").is_file())
        self.assertTrue(self.compatibility["compatible"])
        self.assertTrue(self.compatibility["phase_a_to_g_intact"])


if __name__ == "__main__":
    unittest.main()
