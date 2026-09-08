"""Contract tests for the prospective EV03 historical-builder recovery v0.2."""

from __future__ import annotations

import json
import pickle
import subprocess
import unittest
from pathlib import Path

from src.bm25_index import DEFAULT_STOPWORDS_ES, build_bm25_from_corpus, read_jsonl, tokenize_es
from src.experiments.build_bm25_corrective_0b05c_v01 import ARM_SEMANTICS
from src.experiments.build_bm25_ev03_historical_recovered_v02 import (
    TOKEN_POLICY,
    build_ev03_recovered_historical_from_corpus,
    tokenize_ev03_recovered_historical,
)
from src.experiments.verify_ev03_historical_builder_recovery_v02 import (
    AUDIT_ROOT,
    CORPUS,
    EVALSET,
    FUTURE_EXECUTION_ROOTS,
    HISTORICAL_INDEX,
    FROZEN_OUTPUT_ROOT,
    V01_EVIDENCE_ROOTS,
    logical_identity,
)
from src.experiments.evaluate_normative_bm25_corrective_0b05c_v01 import _flat_rows, _normalize_rows
from src.experiments import evaluate_normative_bm25_flat_data_aduanas_v02 as flat


ROOT = Path(__file__).resolve().parents[1]
GLOBAL_BM25_BLOB = "718895e0658a55cc1590c84ef807f901b75e7c7f"


def load_json(path: Path) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class HistoricalBuilderRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.gate = load_json(AUDIT_ROOT / "0b05c_corrective_numerical_gate_v0.2.json")
        cls.spec = load_json(AUDIT_ROOT / "ev03_corrective_execution_spec_v0.2.json")
        cls.logical = load_json(AUDIT_ROOT / "ev03_logical_index_identity_v0.2.json")
        cls.reproduction = load_json(AUDIT_ROOT / "ev03_decision885_control_reproduction_v0.2.json")
        cls.provenance = load_json(AUDIT_ROOT / "ev03_historical_builder_provenance_v0.2.json")
        cls.rows = read_jsonl(ROOT / CORPUS)
        with (ROOT / HISTORICAL_INDEX).open("rb") as handle:
            cls.historical = pickle.load(handle)
        cls.recovered, cls.recovered_stats = build_ev03_recovered_historical_from_corpus(cls.rows)

    def test_01_recovered_tokenizer_drops_single_character_tokens(self) -> None:
        self.assertEqual(tokenize_ev03_recovered_historical("A x 1 22 motor"), ["22", "motor"])

    def test_02_multi_character_normalization_and_stopwords_are_preserved(self) -> None:
        text = "Árboles MOTORES de 12"
        expected = [token for token in tokenize_es(text, stopwords=None) if len(token) > 1 and token not in DEFAULT_STOPWORDS_ES]
        self.assertEqual(tokenize_ev03_recovered_historical(text), expected)
        self.assertEqual(expected, ["arboles", "motores", "12"])

    def test_03_global_bm25_source_is_unchanged(self) -> None:
        blob = subprocess.run(
            ["git", "rev-parse", "HEAD:src/bm25_index.py"], cwd=ROOT, check=True, capture_output=True, text=True
        ).stdout.strip()
        self.assertEqual(blob, GLOBAL_BM25_BLOB)
        self.assertEqual(subprocess.run(["git", "diff", "--quiet", "--", "src/bm25_index.py"], cwd=ROOT).returncode, 0)

    def test_04_frozen_parameters_and_document_order_are_exact(self) -> None:
        self.assertEqual((self.recovered.k1, self.recovered.b), (1.5, 0.75))
        self.assertEqual(self.recovered_stats["docs_indexed"], 7644)
        self.assertEqual(self.recovered_stats["avg_doc_len"], 5.793302059173584)
        self.assertEqual(self.recovered_stats["vocab_size"], 5646)

    def test_05_ev04_does_not_consume_recovered_policy(self) -> None:
        self.assertNotIn("token_policy", ARM_SEMANTICS["EV04"])
        self.assertEqual(self.gate["ev04_policy"], "UNCHANGED_AND_NOT_ASSUMED_TO_USE_EV03_RECOVERED_TOKEN_POLICY")
        self.assertEqual(TOKEN_POLICY, "DROP_SINGLE_CHARACTER_TOKENS")

    def test_06_current_builder_fails_historical_logical_identity(self) -> None:
        current, _ = build_bm25_from_corpus(self.rows, stopwords=DEFAULT_STOPWORDS_ES)
        self.assertEqual(logical_identity(self.historical, current)["LOGICAL_INDEX_IDENTITY"], "FAIL")

    def test_07_recovered_builder_is_logically_exact(self) -> None:
        self.assertEqual(logical_identity(self.historical, self.recovered)["LOGICAL_INDEX_IDENTITY"], "EXACT")
        self.assertTrue(all(self.logical["checks"].values()))

    def test_08_full_control_reproduction_is_exact(self) -> None:
        cases, candidates, metrics = _flat_rows(ROOT / EVALSET, ROOT / CORPUS, self.recovered, 100)
        frozen_candidates = flat._read_csv(ROOT / FROZEN_OUTPUT_ROOT / "normative_results.csv")
        frozen_cases = flat._read_csv(ROOT / FROZEN_OUTPUT_ROOT / "normative_case_summary.csv")
        frozen_metadata = load_json(FROZEN_OUTPUT_ROOT / "run_metadata.json")
        self.assertEqual(_normalize_rows(candidates), frozen_candidates)
        self.assertEqual(_normalize_rows(cases), frozen_cases)
        self.assertEqual(metrics, frozen_metadata["metrics"])
        self.assertEqual(self.reproduction["EV03_DECISION885_CONTROL_REPRODUCTION"], "PASS_EXACT")
        self.assertTrue(self.reproduction["ranking"]["bytes_exact"])
        self.assertTrue(self.reproduction["case_summary"]["bytes_exact"])
        self.assertTrue(self.reproduction["metrics"]["full_metrics_exact"])
        self.assertEqual(self.reproduction["case_summary"]["rows"], 1056)

    def test_09_exact_reproduction_is_an_independent_precondition(self) -> None:
        self.assertEqual(self.spec["precondition"]["LOGICAL_INDEX_IDENTITY"], "EXACT")
        self.assertEqual(self.spec["precondition"]["EV03_DECISION885_CONTROL_REPRODUCTION"], "PASS_EXACT")
        self.assertFalse(self.spec["corrected_arm_executed"])

    def test_10_v02_bundle_is_closed_and_has_no_future_roots(self) -> None:
        authorization = self.gate["authorization"]
        for field in (
            "EV03_NUMERICAL_EXECUTION",
            "EV04_NUMERICAL_EXECUTION",
            "D1A_NUMERICAL_EXECUTION",
            "UNIFIED_0B05C_NUMERICAL_EXECUTION",
        ):
            self.assertEqual(authorization[field], "NOT_AUTHORIZED")
        self.assertFalse(authorization["corrective_retrieval_executed"])
        self.assertFalse(authorization["corrective_metrics_computed"])
        self.assertFalse(authorization["runtime_authorization_record_present"])
        for relative in FUTURE_EXECUTION_ROOTS:
            self.assertFalse((ROOT / relative).exists(), relative)

    def test_11_v01_attempt_roots_are_excluded_from_v02(self) -> None:
        self.assertEqual(tuple(self.spec["v01_evidence_roots_excluded"]), V01_EVIDENCE_ROOTS)
        self.assertTrue(set(V01_EVIDENCE_ROOTS).isdisjoint(self.gate["future_roots"]))

    def test_12_provenance_limits_are_explicit(self) -> None:
        self.assertEqual(self.provenance["AUTHENTIC_HISTORICAL_SOURCE_PY"], "NOT_VERSIONED_AT_INDEX_CREATION")
        self.assertEqual(self.provenance["versioned_bytecode"]["classification"], "DERIVED_BYTECODE_EVIDENCE_NOT_AUTHENTIC_SOURCE_PY")
        self.assertEqual(self.provenance["conclusion"], "HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED")


if __name__ == "__main__":
    unittest.main()
