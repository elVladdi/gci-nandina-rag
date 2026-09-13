from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from src.experiments.plan_exp12_historical_diversity_v01 import (
    CANDIDATE_COUNT,
    EXPECTED_SEEDS,
    MAXIMUM_TVD,
    ContractViolation,
    Exp12Candidate,
    generate_exp12_candidates,
    main,
    select_exp12_conditions,
    total_variation_distance_full_support,
    validate_exp12_v05_contract,
)


ROOT = Path(__file__).resolve().parents[1]


def load_config(version: str) -> dict[str, object]:
    path = ROOT / "src" / "configs" / f"exp12_historical_diversity_control_{version}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def synthetic_profiles() -> tuple[dict[str, int], dict[str, dict[str, int]], dict[str, int]]:
    rows = {
        "DAM-A": 600,
        "DAM-B": 600,
        "DAM-C": 600,
        "DAM-D": 600,
        "DAM-E": 500,
        "DAM-F": 500,
        "DAM-G": 500,
        "DAM-H": 500,
        "DAM-I": 400,
        "DAM-J": 400,
    }
    labels = {
        dam: {"A": count // 2, "B": count - count // 2}
        for dam, count in rows.items()
    }
    return rows, labels, {"A": 50, "B": 50}


class TestExp12PreplanningCompatibilityV01(unittest.TestCase):
    def setUp(self) -> None:
        self.v04 = load_config("v0.4")
        self.v05 = load_config("v0.5")

    def test_tvd_is_zero_for_identical_distribution(self) -> None:
        self.assertEqual(
            total_variation_distance_full_support({"A": 50, "B": 50}, 100, {"A": 50, "B": 50}),
            0.0,
        )

    def test_tvd_explicitly_counts_other_mass(self) -> None:
        observed = total_variation_distance_full_support(
            {"A": 45, "B": 45, "X": 10}, 100, {"A": 50, "B": 50}
        )
        self.assertAlmostEqual(observed, 0.10)
        self.assertNotAlmostEqual(observed, 0.05)

    def test_tvd_rejects_inconsistent_candidate_denominator(self) -> None:
        with self.assertRaisesRegex(ContractViolation, "sum of all candidate label counts"):
            total_variation_distance_full_support({"A": 45, "B": 45, "X": 10}, 99, {"A": 50, "B": 50})

    def test_v05_contract_passes(self) -> None:
        validate_exp12_v05_contract(self.v05)
        self.assertEqual(self.v05["label_control"]["maximum_tvd"], MAXIMUM_TVD)
        self.assertEqual(tuple(self.v05["replicate_policy"]["seed_schedule"]), EXPECTED_SEEDS)

    def test_v05_validator_rejects_changed_maximum_tvd(self) -> None:
        changed = copy.deepcopy(self.v05)
        changed["label_control"]["maximum_tvd"] = 0.06
        with self.assertRaisesRegex(ContractViolation, "label_control.maximum_tvd"):
            validate_exp12_v05_contract(changed)

    def test_v05_validator_rejects_changed_candidate_count(self) -> None:
        changed = copy.deepcopy(self.v05)
        changed["candidate_generation"]["candidate_count"] = CANDIDATE_COUNT - 1
        with self.assertRaisesRegex(ContractViolation, "candidate_generation.candidate_count"):
            validate_exp12_v05_contract(changed)

    def test_v05_validator_rejects_execution_authorization(self) -> None:
        changed = copy.deepcopy(self.v05)
        changed["execution_authorized"] = True
        with self.assertRaisesRegex(ContractViolation, "execution_authorized"):
            validate_exp12_v05_contract(changed)

    def test_v05_validator_rejects_v04(self) -> None:
        with self.assertRaisesRegex(ContractViolation, "experiment_id"):
            validate_exp12_v05_contract(self.v04)

    def test_v05_preserves_all_non_tvd_frozen_fields(self) -> None:
        v04 = copy.deepcopy(self.v04)
        v05 = copy.deepcopy(self.v05)
        for payload in (v04, v05):
            for key in ("experiment_id", "version", "contract_status", "method_contract"):
                payload.pop(key)
            payload["future_manipulation_check"].pop("execution_gate")
        v04_labels = v04["label_control"]
        v05_labels = v05["label_control"]
        v04_labels.pop("distribution_distance")
        for key in (
            "distribution_distance",
            "distribution_distance_formula",
            "nonreference_support_policy",
            "candidate_probability_denominator",
            "reference_probability_denominator",
            "conditional_renormalization_over_h100_only",
            "historical_v04_formula",
        ):
            v05_labels.pop(key)
        self.assertEqual(v05, v04)

    def test_synthetic_candidate_generation_uses_full_support_tvd(self) -> None:
        rows, labels, reference = synthetic_profiles()
        candidates = generate_exp12_candidates(
            rows, labels, reference, set(), seed=20262001, candidate_count=300
        )
        self.assertGreaterEqual(len(candidates), 30)
        self.assertTrue(all(candidate.tvd == 0.0 for candidate in candidates))
        self.assertTrue(all(candidate.label_coverage_fraction == 1.0 for candidate in candidates))

    def test_synthetic_condition_selection_uses_frozen_quantiles(self) -> None:
        candidates = tuple(
            Exp12Candidate(
                candidate_index=index,
                dam_ids=(f"DAM-{index:02d}",),
                rows=2950,
                hhi=0.10 + index * 0.01,
                effective_dam=1 / (0.10 + index * 0.01),
                dominant_dam_share=0.5,
                top2_dam_share=0.75,
                label_coverage_fraction=1.0,
                tvd=0.0,
            )
            for index in range(30)
        )
        selected = select_exp12_conditions(candidates, 20262001)
        self.assertEqual(set(selected), {"D-HIGH", "D-MID", "D-LOW"})
        self.assertGreater(selected["D-LOW"].hhi, selected["D-MID"].hhi)
        self.assertGreater(selected["D-MID"].hhi, selected["D-HIGH"].hhi)

    def test_cli_without_execute_planning_is_fail_closed(self) -> None:
        with patch(
            "src.experiments.plan_exp12_historical_diversity_v01.execute_planning"
        ) as execute:
            self.assertEqual(main([]), 2)
            execute.assert_not_called()


if __name__ == "__main__":
    unittest.main()
