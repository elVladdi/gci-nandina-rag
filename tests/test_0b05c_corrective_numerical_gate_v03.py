from __future__ import annotations

import copy
import csv
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src.experiments import evaluate_normative_bm25_corrective_0b05c_v03 as evaluator
from src.experiments import prepare_0b05c_corrective_numerical_gate_v03 as gate
from src.experiments import run_0b05c_corrective_numerical_v03 as runner


ROOT = Path(__file__).resolve().parents[1]


def synthetic_case(rank: int) -> dict[str, object]:
    row: dict[str, object] = {
        "rank_ref": rank,
        "reciprocal_rank": 1.0 / rank if rank > 0 else 0.0,
        "retrieved_count": 200,
    }
    for k in (1, 3, 5, 10, 50):
        row[f"hit_top_{k}"] = int(1 <= rank <= k)
    for k in (50, 100, 200):
        row[f"hit_recall_{k}"] = int(1 <= rank <= k)
    for k in (10, 50, 100, 200):
        for name in ("exact", "hs6", "hs4", "chapter"):
            row[f"{name}_at_{k}"] = int(1 <= rank <= k)
    return row


class TestCorrectiveNumericalGateV03(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = {
            key: gate.read_json(ROOT, gate.AUDIT_ROOT / name)
            for key, name in zip(("ev03", "ev04", "d1a", "gate", "manifest", "ledger"), gate.ARTIFACT_NAMES, strict=True)
        }

    def test_01_enriched_mrr_is_derived_from_case_ranks(self) -> None:
        rows = [synthetic_case(rank) for rank in (1, 50, 150, 201, 0)]
        metrics = evaluator.build_ev04_enriched_metrics(rows)
        expected_100 = 1.0 + 1.0 / 50
        expected_200 = expected_100 + 1.0 / 150
        self.assertAlmostEqual(metrics["mrr_at_100_numerator"], expected_100)
        self.assertAlmostEqual(metrics["mrr_at_200_numerator"], expected_200)
        self.assertAlmostEqual(metrics["mrr_at_100"], expected_100 / 5)
        self.assertAlmostEqual(metrics["mrr_at_200"], expected_200 / 5)
        self.assertEqual(metrics["mrr"], metrics["mrr_at_200"])
        self.assertEqual(metrics["mrr_numerator"], metrics["mrr_at_200_numerator"])
        self.assertAlmostEqual(metrics["mrr_101_200_contribution_numerator"], 1.0 / 150)
        self.assertAlmostEqual(metrics["mrr_101_200_contribution"], (1.0 / 150) / 5)

    def test_02_metric_table_names_order_and_schema_are_exact(self) -> None:
        metrics = evaluator.build_ev04_enriched_metrics([synthetic_case(1), synthetic_case(150)])
        self.assertEqual([row["metric"] for row in metrics["metric_table"]], list(evaluator.EV04_METRIC_ORDER))
        for row in metrics["metric_table"]:
            self.assertEqual(tuple(row), evaluator.METRIC_ROW_FIELDS)

    def test_03_legacy_mrr_and_definition_match_frozen_contract(self) -> None:
        metrics = evaluator.build_ev04_enriched_metrics([synthetic_case(101), synthetic_case(0)])
        self.assertEqual(metrics["mrr"], metrics["mrr_at_200"])
        self.assertEqual(metrics["mrr_denominator"], 2)
        self.assertEqual(metrics["mrr_definition"], gate.MRR_DEFINITION)

    def test_04_synthetic_enriched_control_can_pass_exactly(self) -> None:
        metrics = evaluator.build_ev04_enriched_metrics([synthetic_case(1), synthetic_case(150)])
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths = [root / name for name in ("expected_rank.csv", "actual_rank.csv", "expected_case.csv", "actual_case.csv")]
            for path in paths:
                with path.open("w", encoding="utf-8", newline="") as handle:
                    writer = csv.DictWriter(handle, fieldnames=["case_id", "value"], lineterminator="\n")
                    writer.writeheader()
                    writer.writerow({"case_id": "A", "value": "1"})
            result = evaluator.compare_control_reproduction(
                paths[0], paths[1], paths[2], paths[3], metrics, copy.deepcopy(metrics),
                expected_candidate_schema=["case_id", "value"], expected_case_schema=["case_id", "value"],
            )
            self.assertTrue(result["metrics_exact"])
            self.assertEqual(result["status"], "PASS")

    def test_05_missing_mrr_field_fails_closed(self) -> None:
        metrics = evaluator.build_ev04_enriched_metrics([synthetic_case(1)])
        metrics.pop("mrr_definition")
        with self.assertRaises(gate.ContractViolation):
            evaluator.validate_enriched_ev04_metrics(metrics)

    def test_06_reordered_mrr_metric_fails_closed(self) -> None:
        metrics = evaluator.build_ev04_enriched_metrics([synthetic_case(1)])
        metrics["metric_table"][0], metrics["metric_table"][1] = metrics["metric_table"][1], metrics["metric_table"][0]
        with self.assertRaisesRegex(gate.ContractViolation, "names or order"):
            evaluator.validate_enriched_ev04_metrics(metrics)

    def test_07_renamed_mrr_metric_fails_closed(self) -> None:
        metrics = evaluator.build_ev04_enriched_metrics([synthetic_case(1)])
        metrics["metric_table"][0]["metric"] = "mrr100"
        with self.assertRaisesRegex(gate.ContractViolation, "names or order"):
            evaluator.validate_enriched_ev04_metrics(metrics)

    def test_08_ranking_mismatch_fails_even_when_metrics_match(self) -> None:
        metrics = evaluator.build_ev04_enriched_metrics([synthetic_case(1)])
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            expected_rank, actual_rank = root / "expected_rank.csv", root / "actual_rank.csv"
            expected_case, actual_case = root / "expected_case.csv", root / "actual_case.csv"
            expected_rank.write_text("case_id,value\nA,1\n", encoding="utf-8")
            actual_rank.write_text("case_id,value\nA,2\n", encoding="utf-8")
            expected_case.write_text("case_id,value\nA,1\n", encoding="utf-8")
            actual_case.write_text("case_id,value\nA,1\n", encoding="utf-8")
            with self.assertRaisesRegex(evaluator.ContractViolation, "not exact"):
                evaluator.compare_control_reproduction(
                    expected_rank, actual_rank, expected_case, actual_case, metrics, copy.deepcopy(metrics),
                    expected_candidate_schema=["case_id", "value"], expected_case_schema=["case_id", "value"],
                )

    def test_09_ev03_recovered_semantics_are_unchanged(self) -> None:
        invariants = self.bundle["gate"]["ev03_invariants"]
        self.assertEqual(invariants, {"token_policy": "DROP_SINGLE_CHARACTER_TOKENS", "k1": 1.5, "b": 0.75, "depth": 100, "eval_n": 1056})

    def test_10_ev04_scientific_invariants_are_unchanged(self) -> None:
        invariants = self.bundle["gate"]["ev04_invariants"]
        self.assertEqual((invariants["k1"], invariants["b"], invariants["effective_depth"], invariants["eval_n"]), (1.5, 0.75, 200, 1056))
        self.assertEqual(invariants["only_change"], "ENRICHED_MRR_METRIC_PRODUCER_CONTRACT")

    def test_11_d906_patch_scope_remains_exactly_two_codes(self) -> None:
        self.assertEqual(self.bundle["gate"]["patch_codes"], ["87044110", "87045110"])
        for arm in ("ev03", "ev04"):
            self.assertEqual(sorted(item["code"] for item in self.bundle[arm]["corrective_corpus"]["patches"]), ["87044110", "87045110"])

    def test_12_v03_roots_are_disjoint_from_v02(self) -> None:
        self.assertTrue(set(gate.FUTURE_ROOTS).isdisjoint(gate.V02_ROOTS))
        self.assertTrue(all("v0.3" in path for path in gate.FUTURE_ROOTS))

    def test_13_v02_partial_roots_are_not_v03_inputs(self) -> None:
        specs = json.dumps([self.bundle["ev03"], self.bundle["ev04"], self.bundle["d1a"]], sort_keys=True)
        self.assertTrue(all(path not in specs for path in gate.V02_ROOTS))
        self.assertEqual(self.bundle["gate"]["v02_attempt03"]["partial_roots_policy"], "MAY_EXIST_AS_LOCAL_EVIDENCE / NEVER_ERROR / NEVER_INPUT / NEVER_REUSED")

    def test_14_candidate_preflight_authorized_fails_before_side_effects(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(runner, "read_json", return_value=self.bundle["gate"]), mock.patch.object(runner.subprocess, "run", return_value=mock.Mock(stdout="")):
            with self.assertRaisesRegex(gate.ContractViolation, "not approved"):
                runner.preflight_authorized(Path(temporary))
            self.assertEqual(list(Path(temporary).iterdir()), [])

    def test_15_attempt04_cannot_start_from_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(runner, "preflight_authorized", side_effect=gate.ContractViolation("candidate closed")):
            with self.assertRaisesRegex(gate.ContractViolation, "candidate closed"):
                runner.execute_authorized(Path(temporary))
            self.assertEqual(list(Path(temporary).iterdir()), [])
        self.assertEqual(self.bundle["gate"]["attempt04"], "NOT_AUTHORIZED / NOT_EXECUTED")

    def test_16_d1a_contract_remains_exactly_17_metrics(self) -> None:
        metrics = self.bundle["d1a"]["orchestration"]["comparison_contract"]["aggregate_metrics"]
        self.assertEqual(len(metrics), 17)
        self.assertEqual(len(set(metrics)), 17)
        model = self.bundle["gate"]["d1a_invariants"]
        self.assertEqual(model["model_size_bytes"], 470637416)
        self.assertEqual(model["model_sha256"], "ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87")

    def test_17_gate_dependencies_are_not_circular(self) -> None:
        bound = {item["path"] for item in self.bundle["gate"]["dependency_bindings"]}
        artifacts = {(gate.AUDIT_ROOT / name).as_posix() for name in gate.ARTIFACT_NAMES}
        self.assertTrue(bound.isdisjoint(artifacts))
        self.assertTrue(self.bundle["manifest"]["no_circular_dependency"])

    def test_18_candidate_is_closed_and_v03_roots_are_absent(self) -> None:
        candidate = self.bundle["gate"]
        self.assertEqual(candidate["gate_status"], "CANDIDATE_PENDING_EXTERNAL_AUDIT")
        self.assertEqual(candidate["authorization_readiness"], "NOT_AUTHORIZATION_READY")
        self.assertEqual(candidate["authorization"], gate.AUTHORIZATION)
        self.assertFalse((ROOT / gate.AUTHORIZATION_RECORD).exists())
        self.assertTrue(all(not (ROOT / path).exists() for path in gate.FUTURE_ROOTS))


if __name__ == "__main__":
    unittest.main()
