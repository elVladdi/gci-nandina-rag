from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import unittest
from collections import defaultdict
from pathlib import Path

from tests.sha_contracts_v02 import assert_frozen_sha, git_content_sha256


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2"
CONFIG = json.loads((ROOT / "src/configs/he4_pre_explainer_v0.2.json").read_text(encoding="utf-8"))
BASE_HEAD = "12acbee8d796a28df8f7b6b7a04370f65b3b8fdd"


def sha256(path: Path) -> str:
    return git_content_sha256(path)


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def jsonl_rows(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


class He4PhaseIPreGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.inputs_path = OUT / "he4_generation_inputs_v0.2.jsonl"
        cls.inputs = jsonl_rows(cls.inputs_path)
        cls.contexts_path = OUT / "he4_contexts_v0.2.jsonl"
        cls.sample_path = OUT / "he4_explainer_sample_v0.2.csv"
        cls.gate_h = json.loads((OUT / "gate_h_pre_explainer_freeze_v0.2.json").read_text(encoding="utf-8"))

    def test_01_initial_head_is_ancestor_and_branch_is_authorized(self) -> None:
        branch = subprocess.run(
            ["git", "branch", "--show-current"], cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE
        ).stdout.strip()
        self.assertIn(branch, {"", "codex/exp04-rerun-v02"})
        self.assertEqual(subprocess.run(["git", "merge-base", "--is-ancestor", BASE_HEAD, "HEAD"], cwd=ROOT).returncode, 0)

    def test_02_freeze_hashes_match_gate_h(self) -> None:
        expected = self.gate_h["hashes"]
        paths = {
            "sample": self.sample_path,
            "contexts": self.contexts_path,
            "generation_inputs": self.inputs_path,
            "prompt": ROOT / CONFIG["prompt"]["path"],
            "schema": ROOT / CONFIG["schema"]["path"],
            "rubric": ROOT / CONFIG["rubric"]["path"],
        }
        for name, path in paths.items():
            assert_frozen_sha(self, path, expected[name])

    def test_03_sample_and_generation_input_counts_are_frozen(self) -> None:
        self.assertEqual(len(csv_rows(self.sample_path)), 50)
        self.assertEqual(len(self.inputs), 50)
        self.assertEqual(len({str(row["case_id"]) for row in self.inputs}), 50)

    def test_04_inputs_are_exactly_the_frozen_contexts(self) -> None:
        self.assertEqual(self.contexts_path.read_bytes(), self.inputs_path.read_bytes())
        self.assertEqual(sha256(self.contexts_path), sha256(self.inputs_path))

    def test_05_each_input_has_three_closed_candidates_and_evidence(self) -> None:
        slots = 0
        for payload in self.inputs:
            top3 = payload["top3_original"]
            self.assertEqual([candidate["rank_original"] for candidate in top3], [1, 2, 3])
            self.assertEqual(len({candidate["nandina"] for candidate in top3}), 3)
            self.assertTrue(all(candidate["evidencia_historica"]["candidate_id_unico"] for candidate in top3))
            self.assertTrue(all(candidate["evidencia_normativa"]["doc_id"] for candidate in top3))
            slots += len(top3)
        self.assertEqual(slots, 150)

    def test_06_top3_is_invariant_with_phase_a_and_phase_f(self) -> None:
        results = {
            (row["case_id"], int(row["candidate_rank"])): (row["candidate_nandina"], row["score"])
            for row in csv_rows(ROOT / CONFIG["historical_results"]["path"])
            if row["method"] == CONFIG["historical_results"]["method"] and int(row["candidate_rank"]) <= 3
        }
        phase_f = defaultdict(list)
        case_ids = {str(row["case_id"]) for row in self.inputs}
        for row in csv_rows(ROOT / CONFIG["phase_f_slots"]["path"]):
            if row["case_id"] in case_ids:
                phase_f[row["case_id"]].append(row)
        for payload in self.inputs:
            case_id = str(payload["case_id"])
            slots = sorted(phase_f[case_id], key=lambda row: int(row["historical_rank"]))
            self.assertEqual(len(slots), 3)
            for candidate, slot in zip(payload["top3_original"], slots, strict=True):
                rank = int(candidate["rank_original"])
                self.assertEqual((candidate["nandina"], candidate["score_historico"]), results[(case_id, rank)])
                self.assertEqual((candidate["nandina"], candidate["score_historico"]), (slot["historical_candidate_code"], slot["historical_score"]))

    def test_07_payloads_have_no_label_or_reference_keys(self) -> None:
        forbidden = {"expected_nandina", "reference_code", "reference_rank", "exact_rank", "selection_target", "selection_bucket", "ground_truth", "correct_candidate", "correctness", "target"}

        def keys(value: object) -> set[str]:
            if isinstance(value, dict):
                return {str(key).lower() for key in value} | set().union(*(keys(child) for child in value.values()))
            if isinstance(value, list):
                return set().union(*(keys(child) for child in value)) if value else set()
            return set()

        self.assertFalse(forbidden & set().union(*(keys(payload) for payload in self.inputs)))

    def test_08_generation_runner_does_not_load_evaluation_or_diagnostic_artifacts(self) -> None:
        source = (ROOT / "src/experiments/run_he4_explanation_generation_v02.py").read_text(encoding="utf-8")
        self.assertNotIn("he4_sample_evaluation_only_v0.2.csv", source)
        self.assertNotIn("diagnostic_llm", source)
        self.assertNotIn("evaluate_llm_explanation", source)

    def test_09_generation_runner_has_no_retrieval_dependency(self) -> None:
        source = (ROOT / "src/experiments/run_he4_explanation_generation_v02.py").read_text(encoding="utf-8")
        self.assertNotIn("bm25", source.lower())
        self.assertNotIn("candidate_pool", source.lower())
        self.assertNotIn("dense", source.lower())
        self.assertIn("_assert_no_phase_i_overwrite", source)

    def test_10_model_manifest_and_parameters_are_frozen(self) -> None:
        manifest = json.loads((OUT / "he4_model_manifest_v0.2.json").read_text(encoding="utf-8"))
        model = manifest["model"]
        self.assertEqual(model["name"], "qwen2.5:7b-instruct")
        self.assertEqual(model["digest"], "845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e")
        self.assertEqual(model["quantization"], "Q4_K_M")
        self.assertEqual(model["parameters"]["temperature"], 0)
        self.assertEqual(model["parameters"]["num_ctx"], 8192)
        self.assertEqual(model["parameters"]["format"], "json")
        self.assertFalse(model["parameters"]["stream"])

    def test_11_phase_i_manifest_records_no_phase_j_or_k_at_generation(self) -> None:
        manifest = json.loads((OUT / "gate_i_generation_manifest_v0.2.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["phase_j_or_k_executed"])


@unittest.skipUnless((OUT / "gate_i_generation_manifest_v0.2.json").is_file(), "Phase I outputs not generated yet")
class He4PhaseIPostGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.status = json.loads((OUT / "he4_generation_status_v0.2.json").read_text(encoding="utf-8"))
        cls.metadata = json.loads((OUT / "he4_generation_metadata_v0.2.json").read_text(encoding="utf-8"))
        cls.manifest = json.loads((OUT / "gate_i_generation_manifest_v0.2.json").read_text(encoding="utf-8"))
        cls.execution = csv_rows(OUT / "he4_generation_execution_v0.2.csv")
        cls.raw = jsonl_rows(OUT / "he4_responses_raw_v0.2.jsonl")
        cls.parsed = jsonl_rows(OUT / "he4_responses_parsed_v0.2.jsonl")

    def test_20_one_primary_execution_and_raw_record_per_frozen_case(self) -> None:
        self.assertEqual(self.status["calls_attempted"], 50)
        self.assertEqual(self.status["calls_completed"], 50)
        self.assertEqual(len(self.execution), 50)
        self.assertEqual(len(self.raw), 50)
        self.assertEqual(len(self.parsed), 50)
        self.assertEqual([int(row["generation_sequence"]) for row in self.execution], list(range(1, 51)))
        self.assertTrue(all(row["attempt_count"] == "1" and not row["retry_reason"] for row in self.execution))
        self.assertEqual([str(row["case_id"]) for row in self.raw], [row["case_id"] for row in self.execution])
        self.assertTrue(all(isinstance(row["raw_response"], str) and row["raw_response"] for row in self.raw))

    def test_21_outputs_are_linked_to_frozen_inputs_and_model(self) -> None:
        input_hashes = {hashlib.sha256(line.encode("utf-8")).hexdigest() for line in (OUT / "he4_generation_inputs_v0.2.jsonl").read_text(encoding="utf-8").splitlines() if line}
        self.assertEqual({str(row["input_hash"]) for row in self.execution}, input_hashes)
        self.assertTrue(all(row["prompt_hash"] == CONFIG["prompt"]["sha256"] for row in self.execution))
        self.assertTrue(all(row["model_digest"] == CONFIG["model"]["digest"] for row in self.execution))

    def test_22_generation_remained_blind_and_without_retrieval(self) -> None:
        self.assertTrue(self.metadata["no_label_or_evaluation_only_loaded"])
        self.assertTrue(self.metadata["no_phase_g_loaded"])
        self.assertTrue(self.metadata["no_retrieval_performed"])
        self.assertFalse(self.manifest["phase_j_or_k_executed"])

    def test_23_manifest_hashes_and_operational_status_are_complete(self) -> None:
        self.assertEqual(self.manifest["gate_i"], "APPROVED")
        self.assertEqual(self.manifest["he4_status"], "PENDING AUTOMATIC VALIDATION / QUALITATIVE EVALUATION")
        self.assertEqual(self.status["technical_failures"], 0)
        self.assertEqual(self.status["raw_responses_stored"], 50)
        for name, expected in self.manifest["output_sha256"].items():
            assert_frozen_sha(self, OUT / name, expected)


if __name__ == "__main__":
    unittest.main()
