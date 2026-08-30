from __future__ import annotations

import csv
import hashlib
import json
import unittest
from collections import Counter, defaultdict
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


def selection_bucket(exact_rank: int, support_count_dams: int) -> str:
    """Mirror the frozen selector's ordered conditions for audit only."""
    if exact_rank == 1:
        return "rank_1"
    if 2 <= exact_rank <= 3:
        return "rank_2_3"
    if 4 <= exact_rank <= 10:
        return "rank_4_10"
    if exact_rank == 0 or exact_rank > 10 or support_count_dams <= 9:
        return "difficult_low_support"
    return "other"


def full_rank_group(rank: int) -> str:
    if rank == 1:
        return "rank_1"
    if 2 <= rank <= 3:
        return "rank_2_3"
    if 4 <= rank <= 10:
        return "rank_4_10"
    if 11 <= rank <= 50:
        return "rank_11_50"
    return "rank_gt_50_or_not_recovered"


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
        cls.eval_rows = {row["case_id"]: row for row in csv_rows(ROOT / CONFIG["eval"]["path"])}
        cls.summary = {row["case_id"]: row for row in csv_rows(ROOT / CONFIG["historical_case_summary"]["path"])}
        cls.historical_rows = csv_rows(ROOT / CONFIG["historical_results"]["path"])
        cls.historical_full_rank = {
            (row["case_id"], row["candidate_nandina"]): int(row["candidate_rank"])
            for row in cls.historical_rows
        }
        cls.historical_top3 = {
            key: rank for key, rank in cls.historical_full_rank.items() if rank <= 3
        }

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

    def test_09_microaudit_reproduces_selector_buckets_quotas_and_no_fallback(self) -> None:
        targets = {"rank_1": 15, "rank_2_3": 15, "rank_4_10": 10, "difficult_low_support": 10}
        availability = Counter(
            selection_bucket(int(row["exact_rank"]), int(row["support_count_dams"]))
            for row in self.summary.values()
        )
        self.assertEqual(dict(availability), {"rank_4_10": 232, "rank_1": 538, "rank_2_3": 171, "difficult_low_support": 115})
        selected = Counter(row["selection_target"] for row in self.sample)
        self.assertEqual(dict(selected), targets)
        for row in self.sample:
            source = self.summary[row["case_id"]]
            self.assertEqual(row["selection_source"], row["selection_target"])
            self.assertEqual(row["selection_note"], "exact_category")
            self.assertEqual(
                selection_bucket(int(source["exact_rank"]), int(source["support_count_dams"])),
                row["selection_target"],
            )

    def test_10_microaudit_recomputes_full_reference_ranks_and_evaluation_only_projection(self) -> None:
        complete = Counter()
        projected = Counter()
        for sample in self.sample:
            case_id = sample["case_id"]
            eval_row = self.eval_rows[case_id]
            summary = self.summary[case_id]
            expected = eval_row["NANDINA"]
            self.assertEqual(expected, summary["expected_nandina"])
            self.assertEqual(expected, sample["reference_nandina_evaluation_only"])
            rank = int(summary["exact_rank"])
            self.assertEqual(self.historical_full_rank.get((case_id, expected), 0), rank)
            complete[full_rank_group(rank)] += 1
            projected_rank = self.historical_top3.get((case_id, expected), 0)
            projected[projected_rank] += 1
            evaluation_only = next(row for row in self.eval_only if row["case_id"] == case_id)
            self.assertEqual(evaluation_only["reference_nandina_evaluation_only"], expected)
            self.assertEqual(int(evaluation_only["reference_rank_evaluation_only"]), projected_rank)
        self.assertEqual(
            dict(complete),
            {"rank_1": 15, "rank_2_3": 15, "rank_4_10": 10, "rank_11_50": 10},
        )
        self.assertEqual(dict(projected), {1: 15, 2: 10, 3: 5, 0: 20})

    def test_11_microaudit_preserves_full_topk_and_phase_a_f_top3_invariance(self) -> None:
        ranks = [int(self.summary[row["case_id"]]["exact_rank"]) for row in self.sample]
        self.assertEqual(sum(rank == 1 for rank in ranks), 15)
        self.assertEqual(sum(0 < rank <= 3 for rank in ranks), 30)
        self.assertEqual(sum(0 < rank <= 10 for rank in ranks), 40)
        self.assertEqual(sum(0 < rank <= 50 for rank in ranks), 50)
        phase_f_rows = csv_rows(ROOT / CONFIG["phase_f_slots"]["path"])
        phase_f_top3 = defaultdict(list)
        for row in phase_f_rows:
            if row["case_id"] in {item["case_id"] for item in self.sample}:
                phase_f_top3[row["case_id"]].append(row)
        self.assertEqual(sum(len(rows) for rows in phase_f_top3.values()), 150)
        for case_id, rows in phase_f_top3.items():
            rows.sort(key=lambda row: int(row["historical_rank"]))
            self.assertEqual([int(row["historical_rank"]) for row in rows], [1, 2, 3])
            for row in rows:
                self.assertEqual(
                    self.historical_full_rank[(case_id, row["historical_candidate_code"])],
                    int(row["historical_rank"]),
                )

    def test_12_microaudit_artifacts_record_the_frozen_audit_result(self) -> None:
        audit = json.loads((OUT / "gate_h_sample_composition_microaudit_v0.2.json").read_text(encoding="utf-8"))
        audit_rows = csv_rows(OUT / "gate_h_bucket_vs_rank_v0.2.csv")
        self.assertEqual(audit["decision"]["gate_h"], "APPROVED")
        self.assertTrue(audit["decision"]["ready_for_phase_i"])
        self.assertEqual(audit["full_reference_rank_composition"], {"rank_1": 15, "rank_2_3": 15, "rank_4_10": 10, "rank_11_50": 10, "rank_gt_50_or_not_recovered": 0})
        self.assertEqual(audit["full_reference_rank_top_k"], {"top_1": "15/50", "top_3": "30/50", "top_10": "40/50", "top_50": "50/50"})
        self.assertEqual(audit["evaluation_only_audit"]["status"], "CORRECT_AS_TOP3_PROJECTION")
        self.assertEqual(
            {name: item["eligible_initial"] for name, item in audit["quota_audit"].items()},
            {"rank_1": 538, "rank_2_3": 171, "rank_4_10": 232, "difficult_low_support": 115},
        )
        self.assertEqual(len(audit_rows), 50)
        self.assertTrue(all(row["selected_directly"] == "true" for row in audit_rows))
        self.assertTrue(all(row["fallback_used"] == "false" for row in audit_rows))


if __name__ == "__main__":
    unittest.main()
