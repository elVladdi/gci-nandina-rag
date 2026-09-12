from __future__ import annotations

import copy
import csv
import json
import math
import tempfile
import unittest
from pathlib import Path

from src.experiments import evaluate_normative_bm25_corrective_0b05c_v05 as evaluator
from src.experiments import prepare_0b05c_corrective_numerical_gate_v05 as gate
from src.experiments import run_0b05c_corrective_numerical_v05 as runner


ROOT = Path(__file__).resolve().parents[1]


def metric_payload(names: list[str]) -> dict[str, object]:
    return {"metric_table": [{"metric": name, "numerator": 1.0, "denominator": 2, "value": 0.5} for name in names]}


class ComparatorAggregateIntegrityV05Tests(unittest.TestCase):
    def test_frozen_ev03_original_vs_original_accepts_ten_empty_rankings(self) -> None:
        directory = ROOT / "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2"
        result = evaluator.compare_complete_ev03_control_v05(directory / "normative_results.csv", directory / "normative_case_summary.csv")
        self.assertEqual(result["case_count"], 1056)
        self.assertEqual(result["valid_empty_ranking_count"], 10)
        self.assertEqual(result["rank_convention"], "0=NOT_FOUND/EMPTY")

    def test_empty_ranking_contract_rejects_false_empty_and_false_nonempty(self) -> None:
        summary = {"c": {"case_id": "c", "nandina_ref": "1", "retrieved_count": "1", "rank_ref": "0", "top1_code": "", "top1_doc_id": "", "top1_score": ""}}
        with self.assertRaises(gate.ContractViolation):
            evaluator.effective_rankings_v05([], summary, "x", require_unique_codes=False)
        summary["c"]["retrieved_count"] = "0"
        with self.assertRaises(gate.ContractViolation):
            evaluator.effective_rankings_v05([{"case_id": "c", "nandina_ref": "1", "candidate_rank": "1", "candidate_code": "1"}], summary, "x", require_unique_codes=False)

    def test_empty_ranking_rejects_nonempty_top1_and_nonzero_rank_ref(self) -> None:
        for field, value in (("top1_code", "1"), ("top1_doc_id", "d"), ("top1_score", "0"), ("rank_ref", "1")):
            row = {"case_id": "c", "nandina_ref": "1", "retrieved_count": "0", "rank_ref": "0", "top1_code": "", "top1_doc_id": "", "top1_score": ""}
            row[field] = value
            with self.subTest(field=field), self.assertRaises(gate.ContractViolation):
                evaluator.effective_rankings_v05([], {"c": row}, "x", require_unique_codes=False)

    def test_candidate_count_contiguity_and_ev04_uniqueness_are_closed(self) -> None:
        summary = {"c": {"case_id": "c", "nandina_ref": "1", "retrieved_count": "2", "rank_ref": "1", "top1_code": "1", "top1_doc_id": "d", "top1_score": "1"}}
        with self.assertRaises(gate.ContractViolation):
            evaluator.effective_rankings_v05([{"case_id": "c", "candidate_rank": "1", "candidate_code": "1"}], summary, "x", require_unique_codes=False)
        rows = [{"case_id": "c", "nandina_ref": "1", "candidate_rank": str(rank), "candidate_code": "1"} for rank in (1, 2)]
        with self.assertRaises(gate.ContractViolation):
            evaluator.effective_rankings_v05(rows, summary, "x", require_unique_codes=True)

    def test_nonempty_ranking_rejects_wrong_rank_ref_and_candidate_reference(self) -> None:
        summary = {"c": {"case_id": "c", "nandina_ref": "2", "retrieved_count": "2", "rank_ref": "2", "top1_code": "1", "top1_doc_id": "d", "top1_score": "1"}}
        rows = [
            {"case_id": "c", "nandina_ref": "2", "candidate_rank": "1", "candidate_code": "1"},
            {"case_id": "c", "nandina_ref": "2", "candidate_rank": "2", "candidate_code": "2"},
        ]
        self.assertEqual(evaluator.effective_rankings_v05(rows, summary, "x", require_unique_codes=False)["c"], ("1", "2"))
        wrong_rank = copy.deepcopy(summary); wrong_rank["c"]["rank_ref"] = "1"
        with self.assertRaises(gate.ContractViolation):
            evaluator.effective_rankings_v05(rows, wrong_rank, "x", require_unique_codes=False)
        wrong_ref = copy.deepcopy(rows); wrong_ref[0]["nandina_ref"] = "9"
        with self.assertRaises(gate.ContractViolation):
            evaluator.effective_rankings_v05(wrong_ref, summary, "x", require_unique_codes=False)

    def test_metric_validation_is_key_order_independent_after_json_reload(self) -> None:
        metrics = metric_payload(["a", "b"])
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "m.json"
            path.write_text(json.dumps(metrics, sort_keys=True), encoding="utf-8")
            loaded = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual([row["metric"] for row in evaluator.validate_metric_table(loaded, "x", ["a", "b"])], ["a", "b"])

    def test_metric_validation_rejects_nan_inf_any_field_and_bad_denominator(self) -> None:
        for field, value in (("numerator", math.nan), ("value", math.inf), ("denominator", 0), ("denominator", 2.0)):
            payload = metric_payload(["a"]); payload["metric_table"][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(gate.ContractViolation):
                evaluator.validate_metric_table(payload, "x", ["a"])

    def test_metric_validation_rejects_missing_extra_and_reordered_rows(self) -> None:
        payload = metric_payload(["a", "b"])
        for mutate in (
            lambda p: p["metric_table"][0].pop("value"),
            lambda p: p["metric_table"][0].update({"extra": 1}),
            lambda p: p["metric_table"].reverse(),
        ):
            changed = copy.deepcopy(payload); mutate(changed)
            with self.assertRaises(gate.ContractViolation):
                evaluator.validate_metric_table(changed, "x", ["a", "b"])

    def test_ev04_aggregate_retains_28_rows_and_contribution_third(self) -> None:
        directory = ROOT / "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2"
        with (directory / "normative_hierarchical_case_summary.csv").open(encoding="utf-8-sig", newline="") as handle:
            cases = list(csv.DictReader(handle))
        metrics = evaluator.build_ev04_enriched_metrics(cases, require_real_case_count=True)
        rows = evaluator.produce_aggregate_comparison_v05(metrics, metrics, arm="EV04")
        self.assertEqual((len(metrics), len(metrics["metric_table"]), len(rows)), (92, 27, 28))
        self.assertEqual(rows[2]["metric"], "mrr_101_200_contribution")

    def test_aggregate_rejects_nonfinite_and_denominator_mismatch(self) -> None:
        left = metric_payload(["a"]); right = copy.deepcopy(left)
        right["metric_table"][0]["value"] = math.nan
        with self.assertRaises(gate.ContractViolation):
            evaluator.produce_aggregate_comparison_v05(left, right, arm="EV03")
        right = copy.deepcopy(left); right["metric_table"][0]["denominator"] = 3
        with self.assertRaises(gate.ContractViolation):
            evaluator.produce_aggregate_comparison_v05(left, right, arm="EV03")

    def test_runtime_integrity_rejects_truncated_missing_and_malformed_files(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); ranking = root / "r.csv"; summary = root / "s.csv"; metrics = root / "m.json"
            ranking.write_text("", encoding="utf-8")
            summary.write_text("x\n", encoding="utf-8")
            metrics.write_text("{}", encoding="utf-8")
            with self.assertRaises(gate.ContractViolation):
                runner.validate_arm_runtime_integrity("EV03", ranking, summary, metrics)
            with self.assertRaises(gate.ContractViolation):
                runner.validate_d1a_runtime_integrity([root / "missing"])


if __name__ == "__main__":
    unittest.main()
