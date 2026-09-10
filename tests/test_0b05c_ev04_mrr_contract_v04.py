from __future__ import annotations

import copy
import csv
import json
import math
import unittest
from pathlib import Path

from src.experiments import evaluate_normative_bm25_corrective_0b05c_v04 as subject


def case(rank: int) -> dict[str, object]:
    row: dict[str, object] = {
        "rank_ref": rank,
        "reciprocal_rank": (1.0 / rank) if 1 <= rank <= 200 else 0.0,
        "retrieved_count": 200,
    }
    for k in subject.hierarchical.K_VALUES:
        row[f"hit_top_{k}"] = int(1 <= rank <= k)
    for k in subject.hierarchical.RECALL_K_VALUES:
        row[f"hit_recall_{k}"] = int(1 <= rank <= k)
    for k in subject.hierarchical.HIERARCHICAL_K_VALUES:
        for name in ("exact", "hs6", "hs4", "chapter"):
            row[f"{name}_at_{k}"] = int(1 <= rank <= k)
    return row


class EV04MRRContractV04Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = [case(1), case(2), case(77), case(101), case(200), case(0)]
        self.metrics = subject.build_ev04_enriched_metrics(self.rows)

    def test_mrr100_uses_rank_ref_and_exact_final_conversion(self) -> None:
        expected_numerator = float(subject.Fraction(1, 1) + subject.Fraction(1, 2) + subject.Fraction(1, 77))
        self.assertEqual(self.metrics["mrr_at_100_numerator"], expected_numerator)
        self.assertEqual(self.metrics["mrr_at_100"], expected_numerator / len(self.rows))

    def test_mrr200_preserves_legacy_sum_and_aliases(self) -> None:
        expected = sum(float(row["reciprocal_rank"]) for row in self.rows)
        self.assertEqual(self.metrics["mrr_at_200_numerator"], expected)
        self.assertEqual(self.metrics["mrr_numerator"], expected)
        self.assertEqual(self.metrics["mrr"], self.metrics["mrr_at_200"])

    def test_contribution_is_exact_rational_difference(self) -> None:
        exact = subject.Fraction(1, 101) + subject.Fraction(1, 200)
        self.assertEqual(self.metrics["mrr_101_200_contribution_numerator"], float(exact))
        self.assertEqual(self.metrics["mrr_101_200_contribution"], float(exact / len(self.rows)))

    def test_metric_table_schema_and_order_are_frozen(self) -> None:
        table = self.metrics["metric_table"]
        self.assertEqual([row["metric"] for row in table], list(subject.EV04_METRIC_ORDER))
        self.assertTrue(all(tuple(row) == subject.METRIC_ROW_FIELDS for row in table))

    def test_expected_and_actual_are_built_independently(self) -> None:
        result = subject.compare_ev04_control_v04(copy.deepcopy(self.rows), copy.deepcopy(self.rows))
        self.assertEqual(result["status"], "PASS")
        self.assertIsNot(result["expected_metrics"], result["actual_metrics"])

    def assert_rejected(self, mutate) -> None:
        actual = copy.deepcopy(self.metrics)
        mutate(actual)
        with self.assertRaises(subject.ContractViolation):
            subject.compare_canonical_metrics_v04(self.metrics, actual)

    def test_rejects_mrr100_one_ulp_drift(self) -> None:
        self.assert_rejected(lambda m: m.__setitem__("mrr_at_100", math.nextafter(m["mrr_at_100"], math.inf)))

    def test_rejects_mrr200_alias_drift(self) -> None:
        self.assert_rejected(lambda m: m.__setitem__("mrr", math.nextafter(m["mrr"], math.inf)))

    def test_rejects_contribution_one_ulp_drift(self) -> None:
        self.assert_rejected(lambda m: m.__setitem__("mrr_101_200_contribution", math.nextafter(m["mrr_101_200_contribution"], math.inf)))

    def test_rejects_missing_key(self) -> None:
        self.assert_rejected(lambda m: m.pop("mrr_definition"))

    def test_rejects_extra_key(self) -> None:
        self.assert_rejected(lambda m: m.__setitem__("unexpected", 0))

    def test_rejects_type_change(self) -> None:
        self.assert_rejected(lambda m: m.__setitem__("mrr_at_100_denominator", float(m["mrr_at_100_denominator"])))

    def test_rejects_metric_table_order_change(self) -> None:
        def mutate(metrics):
            metrics["metric_table"][0], metrics["metric_table"][1] = metrics["metric_table"][1], metrics["metric_table"][0]
        self.assert_rejected(mutate)

    def test_rejects_changed_ranking(self) -> None:
        actual = copy.deepcopy(self.rows)
        actual[0]["rank_ref"] = 2
        with self.assertRaises(subject.ContractViolation):
            subject.compare_ev04_control_v04(self.rows, actual)

    def test_rejects_changed_case_summary(self) -> None:
        actual = copy.deepcopy(self.rows)
        actual[0]["hit_top_1"] = 0
        with self.assertRaises(subject.ContractViolation):
            subject.compare_ev04_control_v04(self.rows, actual)

    def test_frozen_shadow_values_and_legacy_fields(self) -> None:
        root = Path(__file__).resolve().parents[1]
        directory = root / "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2"
        with (directory / "normative_hierarchical_case_summary.csv").open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        actual = subject.build_ev04_enriched_metrics(rows, require_real_case_count=True)
        frozen = json.loads((directory / "normative_hierarchical_metrics.json").read_text(encoding="utf-8"))["metrics"]
        self.assertEqual(actual["mrr_at_100"], 0.04198129438896378)
        self.assertEqual(actual["mrr_at_100"].hex(), "0x1.57e927ce3818cp-5")
        self.assertEqual(actual["mrr_at_200"], 0.04334161160288281)
        self.assertEqual(actual["mrr_at_200"].hex(), "0x1.630df28c7d779p-5")
        self.assertEqual(actual["mrr_101_200_contribution"], 0.0013603172139190346)
        self.assertEqual(actual["mrr_101_200_contribution"].hex(), "0x1.649957c8abdbep-10")
        prospective = {
            "mrr_at_100", "mrr_at_100_numerator", "mrr_at_100_denominator",
            "mrr_at_200", "mrr_at_200_numerator", "mrr_at_200_denominator",
            "mrr_definition", "mrr_101_200_contribution_numerator",
            "mrr_101_200_contribution", "metric_table",
        }
        for key, value in frozen.items():
            if key not in prospective:
                self.assertEqual(actual[key], value, key)

    def test_rational_fields_are_row_order_invariant(self) -> None:
        forward = subject.build_ev04_enriched_metrics(self.rows)
        reverse = subject.build_ev04_enriched_metrics(list(reversed(self.rows)))
        for key in ("mrr_at_100", "mrr_at_100_numerator", "mrr_101_200_contribution", "mrr_101_200_contribution_numerator"):
            self.assertEqual(forward[key], reverse[key])

    def test_producer_has_no_known_output_literals_or_tolerance(self) -> None:
        source = Path(subject.__file__).read_text(encoding="utf-8")
        for forbidden in ("0.04198129438896377", "0.04198129438896378", "0.04334161160288281", "0.0013603172139190346", "isclose", "nextafter"):
            self.assertNotIn(forbidden, source)

    def test_frozen_complete_shadow_control_passes_exact(self) -> None:
        root = Path(__file__).resolve().parents[1]
        directory = root / "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2"
        result = subject.compare_complete_ev04_control_v04(
            directory / "normative_hierarchical_results.csv",
            directory / "normative_hierarchical_results.csv",
            directory / "normative_hierarchical_case_summary.csv",
            directory / "normative_hierarchical_case_summary.csv",
        )
        self.assertEqual(result["status"], "PASS_EXACT")


if __name__ == "__main__":
    unittest.main()
