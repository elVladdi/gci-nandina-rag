from __future__ import annotations

import csv
import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2"
RAW_SHA = "8a34a4c46f11ca9d54bf558eb81ce2428e3e12f03e6ff7f02e46757b4e5134b4"
PARSED_SHA = "daf7ab5c475764e281866e5faf7929314811ce2ff002c529f94366d7fca7b0b6"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class He4PhaseJAutomaticValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.case_rows = csv_rows(OUT / "he4_automatic_validation_case_results_v0.2.csv")
        cls.slot_rows = csv_rows(OUT / "he4_automatic_validation_slot_results_v0.2.csv")
        cls.metrics = json.loads((OUT / "he4_automatic_validation_metrics_v0.2.json").read_text(encoding="utf-8"))
        cls.manifest = json.loads((OUT / "gate_j_automatic_validation_manifest_v0.2.json").read_text(encoding="utf-8"))

    def test_01_all_frozen_inputs_have_expected_hashes(self) -> None:
        self.assertEqual(sha256(OUT / "he4_responses_raw_v0.2.jsonl"), RAW_SHA)
        self.assertEqual(sha256(OUT / "he4_responses_parsed_v0.2.jsonl"), PARSED_SHA)
        for name, item in self.manifest["input_hashes"].items():
            self.assertTrue(item["pass"], name)

    def test_02_exactly_fifty_cases_and_one_hundred_fifty_slots(self) -> None:
        self.assertEqual(len(self.case_rows), 50)
        self.assertEqual(len(self.slot_rows), 150)
        self.assertEqual(len({row["case_id"] for row in self.case_rows}), 50)

    def test_03_raw_parse_and_parsed_identity_are_recalculable(self) -> None:
        values = self.metrics["case_metrics"]
        self.assertEqual(values["raw_json_parse_rate"]["numerator"], sum(row["raw_parseable"] == "1" for row in self.case_rows))
        self.assertEqual(values["parsed_raw_identity_rate"]["numerator"], sum(row["parsed_matches_raw"] == "1" for row in self.case_rows))

    def test_04_candidate_and_order_metrics_are_recalculable(self) -> None:
        values = self.metrics["case_metrics"]
        self.assertEqual(values["candidate_set_closure_rate"]["numerator"], sum(row["candidate_set_exact"] == "1" for row in self.case_rows))
        self.assertEqual(values["top3_order_preservation_rate"]["numerator"], sum(row["top3_order_preserved"] == "1" for row in self.case_rows))
        self.assertEqual(values["external_code_free_rate"]["numerator"], sum(row["external_code_count"] == "0" for row in self.case_rows))

    def test_05_slot_metrics_are_recalculable(self) -> None:
        values = self.metrics["slot_metrics"]
        self.assertEqual(values["candidate_code_valid_rate"]["numerator"], sum(row["code_valid"] == "1" for row in self.slot_rows))
        self.assertEqual(values["rank_consistent_rate"]["numerator"], sum(row["rank_consistent"] == "1" for row in self.slot_rows))
        self.assertEqual(values["historical_reference_valid_rate"]["numerator"], sum(row["historical_reference_valid"] == "1" for row in self.slot_rows))
        self.assertEqual(values["normative_reference_valid_rate"]["numerator"], sum(row["normative_reference_valid"] == "1" for row in self.slot_rows))

    def test_06_no_per_case_pass_rule_was_invented(self) -> None:
        self.assertFalse(self.metrics["automatic_validation_pass"]["applicable"])
        self.assertEqual({row["automatic_validation_pass"] for row in self.case_rows}, {"NOT_DEFINED_PRE_GENERATION"})

    def test_07_validator_has_no_model_or_retrieval_dependency(self) -> None:
        source = (ROOT / "src/experiments/evaluate_he4_automatic_validation_v02.py").read_text(encoding="utf-8").lower()
        for forbidden in ("import urllib", "import requests", "http://", "https://", "ollama", "bm25", "embedding"):
            self.assertNotIn(forbidden, source)
        self.assertTrue(self.manifest["no_model_calls"])
        self.assertTrue(self.manifest["no_retrieval"])

    def test_08_phase_k_and_exp10_remain_unexecuted(self) -> None:
        self.assertFalse(self.manifest["phase_k_executed"])
        self.assertFalse(self.manifest["exp10_executed"])
        self.assertEqual(self.manifest["he4_global_status"], "PENDING QUALITATIVE EVALUATION - FASE K")

    def test_09_outputs_are_hashed_and_under_size_limit(self) -> None:
        for name, expected in self.manifest["output_sha256"].items():
            self.assertEqual(sha256(OUT / name), expected, name)
        self.assertEqual(self.manifest["outputs_over_50_mib"], [])

    def test_10_traceability_and_bucket_outputs_are_complete(self) -> None:
        trace = json.loads((OUT / "he4_traceability_validation_v0.2.json").read_text(encoding="utf-8"))
        buckets = csv_rows(OUT / "he4_automatic_validation_by_bucket_v0.2.csv")
        self.assertEqual(len(trace["cases"]), 50)
        self.assertTrue(all(row["traceability_complete"] for row in trace["cases"]))
        self.assertEqual({row["selection_target"] for row in buckets}, {"rank_1", "rank_2_3", "rank_4_10", "difficult_low_support"})


if __name__ == "__main__":
    unittest.main()
