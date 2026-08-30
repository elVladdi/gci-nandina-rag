from __future__ import annotations

import csv
import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2"
CONFIG = json.loads((ROOT / "src/configs/diagnostic_llm_reranker_v0.2.json").read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class DiagnosticRerankerPostLlmTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.inputs = [json.loads(line) for line in (OUT / "reranker_inputs_v0.2.jsonl").read_text(encoding="utf-8").splitlines() if line]
        cls.outputs = [json.loads(line) for line in (OUT / "reranker_outputs_v0.2.jsonl").read_text(encoding="utf-8").splitlines() if line]
        cls.rows = csv_rows(OUT / "reranker_case_results_v0.2.csv")
        cls.metrics = json.loads((OUT / "reranker_metrics_v0.2.json").read_text(encoding="utf-8"))
        cls.closure = json.loads((OUT / "reranker_candidate_closure_audit_v0.2.json").read_text(encoding="utf-8"))
        cls.compatibility = json.loads((OUT / "reranker_compatibility_v0.2.json").read_text(encoding="utf-8"))
        cls.metadata = json.loads((OUT / "reranker_run_metadata_v0.2.json").read_text(encoding="utf-8"))

    def test_01_every_output_is_traced_to_one_frozen_input(self) -> None:
        self.assertEqual({row["case_id"] for row in self.inputs}, {row["case_id"] for row in self.outputs})
        self.assertEqual(len(self.outputs), 20)
        self.assertTrue(all(row["attempt_count"] == 1 for row in self.outputs))
        self.assertTrue(all(not row["retry_reason"] for row in self.outputs))

    def test_02_candidate_closure_is_exact_and_recalculable(self) -> None:
        input_by_case = {row["case_id"]: [candidate["nandina"] for candidate in row["candidates"]] for row in self.inputs}
        for output in self.outputs:
            validation = output["validation"]
            self.assertEqual(validation["validation_status"], "valid")
            self.assertTrue(validation["candidate_closure_pass"])
            self.assertEqual(set(validation["ordered_candidate_codes"]), set(input_by_case[output["case_id"]]))
            self.assertEqual(len(validation["ordered_candidate_codes"]), len(input_by_case[output["case_id"]]))
        self.assertTrue(self.closure["pass"])
        self.assertEqual(self.closure["candidate_closure_pass_cases"], 20)

    def test_03_no_invalid_or_external_outputs_exist(self) -> None:
        self.assertEqual(self.closure["invalid_final"], 0)
        self.assertEqual(self.closure["parse_errors"], 0)
        self.assertEqual(self.closure["external_code_attempts"], 0)
        self.assertEqual(self.closure["duplicate_code_attempts"], 0)
        self.assertEqual(self.closure["missing_code_outputs"], 0)

    def test_04_win_tie_loss_and_metrics_recompute(self) -> None:
        self.assertEqual(len(self.rows), 20)
        self.assertEqual(sum(row["outcome"] == "TIE" for row in self.rows), 19)
        self.assertEqual(sum(row["outcome"] == "NOT_EVALUABLE_REFERENCE_ABSENT" for row in self.rows), 1)
        self.assertEqual(sum(row["outcome"] == "WIN" for row in self.rows), 0)
        self.assertEqual(sum(row["outcome"] == "LOSS" for row in self.rows), 0)
        self.assertEqual(self.metrics["mrr_before"], self.metrics["mrr_after"])
        self.assertEqual(self.metrics["delta_mrr"], 0.0)
        for k in (1, 3, 5):
            self.assertEqual(self.metrics[f"delta_top_{k}"], 0.0)

    def test_05_compatibility_metadata_and_frozen_phases_hold(self) -> None:
        self.assertTrue(self.compatibility["compatible"])
        self.assertTrue(self.compatibility["phase_a_to_f_intact"])
        self.assertTrue(self.compatibility["labels_used_only_in_evaluation"])
        self.assertEqual(self.metadata["model_status"]["digest"], CONFIG["model"]["expected_digest"])
        self.assertEqual(self.metadata["calls"], 20)
        files = {
            "pool": "reranker_candidate_pool_v0.2.csv", "sample": "reranker_diagnostic_sample_v0.2.csv",
            "inputs": "reranker_inputs_v0.2.jsonl", "outputs": "reranker_outputs_v0.2.jsonl",
            "case_results": "reranker_case_results_v0.2.csv", "position_changes": "reranker_position_changes_v0.2.csv",
            "metrics": "reranker_metrics_v0.2.json", "win_tie_loss": "reranker_win_tie_loss_v0.2.json",
            "closure": "reranker_candidate_closure_audit_v0.2.json", "label_audit": "reranker_label_leakage_audit_v0.2.json",
            "compatibility": "reranker_compatibility_v0.2.json", "summary": "summary.md",
        }
        for name, digest in self.metadata["output_sha256"].items():
            self.assertEqual(sha256(OUT / files[name]), digest, name)

    def test_06_required_post_outputs_exist(self) -> None:
        for name in [
            "reranker_case_results_v0.2.csv", "reranker_position_changes_v0.2.csv", "reranker_metrics_v0.2.json",
            "reranker_win_tie_loss_v0.2.json", "reranker_candidate_closure_audit_v0.2.json",
            "reranker_compatibility_v0.2.json", "reranker_run_metadata_v0.2.json", "summary.md",
        ]:
            self.assertTrue((OUT / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
