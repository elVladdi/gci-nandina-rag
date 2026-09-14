from __future__ import annotations

import unittest
from unittest.mock import patch

from src.experiments.diagnose_exp12_feasibility_failure_v01 import (
    FORENSIC_CANDIDATE_COUNT,
    FORENSIC_SEED,
    _classify_candidate,
    _diagnose_profiles,
    main,
    validate_forensic_request,
)
from src.experiments.plan_exp12_historical_diversity_v01 import (
    ContractViolation,
    generate_exp12_candidates,
)


def balanced_labels(rows: dict[str, int]) -> dict[str, dict[str, int]]:
    return {
        dam: {"A": count // 2, "B": count - count // 2}
        for dam, count in rows.items()
    }


class TestExp12FeasibilityFailureDiagnosticV01(unittest.TestCase):
    def test_exact_accounting_for_10000_synthetic_indices(self) -> None:
        rows = {"DAM-A": 1500, "DAM-B": 1450}
        result = _diagnose_profiles(
            rows,
            balanced_labels(rows),
            {"A": 50, "B": 50},
            set(),
            seed=FORENSIC_SEED,
            candidate_count=10000,
        )
        self.assertEqual(result["candidate_indices_attempted"], 10000)
        self.assertEqual(result["duplicate_dam_set_rejections"], 9999)
        self.assertEqual(result["unique_nonoverlap_candidates"], 1)
        self.assertEqual(result["final_unique_feasible_count"], 1)

    def test_eval_overlap_precedes_seen_registration(self) -> None:
        rows = {"DAM-A": 1500, "DAM-B": 1450}
        result = _diagnose_profiles(
            rows,
            balanced_labels(rows),
            {"A": 50, "B": 50},
            {"DAM-A"},
            seed=FORENSIC_SEED,
            candidate_count=20,
        )
        self.assertEqual(result["eval_overlap_rejections"], 20)
        self.assertEqual(result["duplicate_dam_set_rejections"], 0)
        self.assertEqual(result["unique_nonoverlap_candidates"], 0)

    def test_volume_below_within_and_above_cases(self) -> None:
        reference = {"A": 50, "B": 50}
        for rows, expected in ((2801, "below"), (2900, "within"), (3099, "above")):
            with self.subTest(rows=rows):
                observed, _, _ = _classify_candidate(
                    ("DAM-X",),
                    {"DAM-X": rows},
                    {"DAM-X": {"A": rows // 2, "B": rows - rows // 2}},
                    reference,
                )
                self.assertEqual(observed, expected)

    def test_coverage_pass_tvd_pass(self) -> None:
        self.assertEqual(
            _classify_candidate(
                ("DAM-X",),
                {"DAM-X": 2900},
                {"DAM-X": {"A": 1450, "B": 1450}},
                {"A": 50, "B": 50},
            ),
            ("within", True, True),
        )

    def test_coverage_pass_tvd_fail(self) -> None:
        self.assertEqual(
            _classify_candidate(
                ("DAM-X",),
                {"DAM-X": 2900},
                {"DAM-X": {"A": 2899, "B": 1}},
                {"A": 50, "B": 50},
            ),
            ("within", True, False),
        )

    def test_coverage_fail_tvd_pass(self) -> None:
        self.assertEqual(
            _classify_candidate(
                ("DAM-X",),
                {"DAM-X": 2900},
                {"DAM-X": {"A": 2900}},
                {"A": 99, "B": 1},
            ),
            ("within", False, True),
        )

    def test_coverage_fail_tvd_fail(self) -> None:
        self.assertEqual(
            _classify_candidate(
                ("DAM-X",),
                {"DAM-X": 2900},
                {"DAM-X": {"A": 2900}},
                {"A": 50, "B": 50},
            ),
            ("within", False, False),
        )

    def test_final_feasible_count_equals_joint_pass_cell(self) -> None:
        rows = {"DAM-A": 1400, "DAM-B": 1500, "DAM-C": 1600}
        result = _diagnose_profiles(
            rows,
            balanced_labels(rows),
            {"A": 50, "B": 50},
            set(),
            seed=FORENSIC_SEED,
            candidate_count=50,
        )
        self.assertEqual(
            result["final_unique_feasible_count"],
            result["coverage_and_tvd_pass_count"],
        )

    def test_four_joint_cells_sum_to_volume_within(self) -> None:
        rows = {"DAM-A": 1400, "DAM-B": 1500, "DAM-C": 1600}
        result = _diagnose_profiles(
            rows,
            balanced_labels(rows),
            {"A": 50, "B": 50},
            set(),
            seed=FORENSIC_SEED,
            candidate_count=50,
        )
        cell_sum = sum(
            result[key]
            for key in (
                "coverage_and_tvd_pass_count",
                "coverage_pass_tvd_fail_count",
                "coverage_fail_tvd_pass_count",
                "coverage_and_tvd_fail_count",
            )
        )
        self.assertEqual(cell_sum, result["volume_within_range_count"])

    def test_final_count_matches_frozen_generator_on_synthetic_profiles(self) -> None:
        rows = {"DAM-A": 1400, "DAM-B": 1500, "DAM-C": 1600}
        labels = balanced_labels(rows)
        diagnostic = _diagnose_profiles(
            rows,
            labels,
            {"A": 50, "B": 50},
            set(),
            seed=FORENSIC_SEED,
            candidate_count=50,
        )
        generated = generate_exp12_candidates(
            rows,
            labels,
            {"A": 50, "B": 50},
            set(),
            seed=FORENSIC_SEED,
            candidate_count=50,
        )
        self.assertEqual(diagnostic["final_unique_feasible_count"], len(generated))

    def test_productive_interface_rejects_other_seed(self) -> None:
        with self.assertRaisesRegex(ContractViolation, "seed"):
            validate_forensic_request(seed=20262002)

    def test_productive_interface_rejects_candidate_count_change(self) -> None:
        with self.assertRaisesRegex(ContractViolation, "candidate_count"):
            validate_forensic_request(candidate_count=FORENSIC_CANDIDATE_COUNT - 1)

    def test_productive_interface_rejects_frozen_constraint_changes(self) -> None:
        changes = (
            {"target_rows": 2949},
            {"minimum_rows": 2801},
            {"maximum_rows": 3099},
            {"required_label_coverage_fraction": 0.99},
            {"maximum_tvd": 0.06},
        )
        for change in changes:
            with self.subTest(change=change), self.assertRaises(ContractViolation):
                validate_forensic_request(**change)

    def test_cli_without_flag_is_fail_closed_and_does_not_run(self) -> None:
        with patch(
            "src.experiments.diagnose_exp12_feasibility_failure_v01.run_forensic_diagnostic"
        ) as diagnostic:
            self.assertEqual(main([]), 2)
            diagnostic.assert_not_called()


if __name__ == "__main__":
    unittest.main()
