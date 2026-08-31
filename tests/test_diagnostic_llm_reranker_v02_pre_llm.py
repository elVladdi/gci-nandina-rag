from __future__ import annotations

import csv
import hashlib
import json
import unittest
from collections import defaultdict
from pathlib import Path

from tests.sha_contracts_v02 import assert_frozen_sha, git_content_sha256


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "src/configs/diagnostic_llm_reranker_v0.2.json"
OUT = ROOT / "outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2"


def sha256(path: Path) -> str:
    return git_content_sha256(path)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class DiagnosticRerankerPreLlmTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        cls.gate = json.loads((OUT / "gate_g_pre_llm_freeze_v0.2.json").read_text(encoding="utf-8"))
        cls.pool = read_csv(OUT / "reranker_candidate_pool_v0.2.csv")
        cls.sample = read_csv(OUT / "reranker_diagnostic_sample_v0.2.csv")
        cls.inputs = [json.loads(line) for line in (OUT / "reranker_inputs_v0.2.jsonl").read_text(encoding="utf-8").splitlines() if line]

    def test_01_eval_and_frozen_phase_hashes_match(self) -> None:
        assert_frozen_sha(self, ROOT / self.config["eval"]["path"], self.config["eval"]["sha256"])
        for name, item in self.config["frozen_phase_artifacts"].items():
            assert_frozen_sha(self, ROOT / item["path"], item["sha256"])

    def test_02_pool_is_closed_unique_and_v02_only(self) -> None:
        grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in self.pool:
            grouped[row["case_id"]].append(row)
            self.assertTrue(row["candidate_code"].isdigit() and len(row["candidate_code"]) == 8)
        self.assertEqual(len(grouped), 1056)
        for case_id, rows in grouped.items():
            self.assertEqual([int(row["candidate_position_before"]) for row in rows], list(range(1, len(rows) + 1)), case_id)
            self.assertEqual(len({row["candidate_code"] for row in rows}), len(rows), case_id)
            self.assertGreaterEqual(len(rows), 10)
        self.assertNotIn("v0.1", self.config["pool"]["historical_results"]["path"])

    def test_03_sample_is_deterministic_and_pre_label(self) -> None:
        self.assertEqual(len(self.sample), 20)
        self.assertEqual(len({row["case_id"] for row in self.sample}), 20)
        self.assertTrue(all(row["seed"] == "0" for row in self.sample))
        self.assertTrue(all(row["candidate_pool_sha256"] == self.gate["hashes"]["pool"] for row in self.sample))
        header = set(self.sample[0])
        self.assertFalse({"NANDINA", "nandina_ref", "expected_nandina", "reference_nandina"} & header)

    def test_04_inputs_are_exactly_ten_closed_candidates(self) -> None:
        pool_by_case: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in self.pool:
            pool_by_case[row["case_id"]].append(row)
        self.assertEqual({row["case_id"] for row in self.sample}, {row["case_id"] for row in self.inputs})
        for item in self.inputs:
            candidates = item["candidates"]
            self.assertEqual(len(candidates), 10)
            codes = [candidate["nandina"] for candidate in candidates]
            self.assertEqual(len(codes), len(set(codes)))
            self.assertEqual(codes, [row["candidate_code"] for row in pool_by_case[item["case_id"]][:10]])
            self.assertNotIn("NANDINA", item)

    def test_05_prompt_and_inputs_have_no_label_tokens(self) -> None:
        audit = json.loads((OUT / "reranker_label_leakage_audit_v0.2.json").read_text(encoding="utf-8"))
        self.assertTrue(audit["pass"])
        self.assertTrue(audit["source_reader_excludes_label_columns"])
        self.assertFalse(any(audit["observed_forbidden_tokens"].values()))

    def test_06_hashes_and_pre_llm_gate_are_frozen(self) -> None:
        self.assertEqual(self.gate["status"], "PRE_LLM_FREEZE_PASS")
        assert_frozen_sha(self, OUT / "reranker_candidate_pool_v0.2.csv", self.gate["hashes"]["pool"])
        assert_frozen_sha(self, OUT / "reranker_diagnostic_sample_v0.2.csv", self.gate["hashes"]["sample"])
        assert_frozen_sha(self, OUT / "reranker_inputs_v0.2.jsonl", self.gate["hashes"]["inputs"])
        assert_frozen_sha(self, ROOT / "src/prompts/reranker_diagnostic_v0.2.txt", self.gate["hashes"]["prompt"])

    def test_07_gate_contains_only_pre_llm_freeze_state(self) -> None:
        serialized = json.dumps(self.gate, ensure_ascii=False).lower()
        self.assertNotIn("reranker_outputs_v0.2.jsonl", serialized)
        self.assertNotIn("execution_commit", serialized)
        self.assertEqual(self.gate["status"], "PRE_LLM_FREEZE_PASS")


if __name__ == "__main__":
    unittest.main()
