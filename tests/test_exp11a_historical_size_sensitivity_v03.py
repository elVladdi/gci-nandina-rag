"""Pre-execution contract tests for the frozen EXP-11A runner."""

from __future__ import annotations

import json
from pathlib import Path
import unittest
from unittest.mock import patch

from src.experiments.run_exp11a_historical_size_sensitivity_v03 import (
    ALLOWED_CONDITIONS,
    H100_SHA256,
    EVAL_SHA256,
    _canonical_status_lines,
    _source_by_dam,
    _subset_rows,
    _validate_execution_contract,
    load_frozen_run_specs,
)
from src.experiments import evaluate_historical_retrieval_data_aduanas_v02 as historical


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "outputs" / "audits" / "g2a_reproducibility_v0.1"


class TestExp11aHistoricalSizeSensitivityV03(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads((ROOT / "src/configs/exp11_historical_size_sensitivity_v0.3.json").read_text(encoding="utf-8"))
        cls.gate = json.loads((AUDIT / "gate_g2a_reproducibility_manifest_v0.1.json").read_text(encoding="utf-8"))
        cls.exp12 = json.loads((ROOT / "src/configs/exp12_historical_diversity_control_v0.3.json").read_text(encoding="utf-8"))
        cls.evidence = json.loads((AUDIT / "exp11_independent_condition_feasibility_v0.2.json").read_text(encoding="utf-8"))
        cls.historical_path = ROOT / "data/processed/data_aduanas_historico_clase87_v0.2.csv"
        cls.eval_path = ROOT / "data/processed/data_aduanas_evalset_clase87_v0.2.csv"
        cls.historical_rows = historical._read_csv(cls.historical_path)

    def test_gate_and_config_authorize_only_exp11a(self) -> None:
        _validate_execution_contract(self.config, self.gate, self.exp12)
        self.assertTrue(self.config["exp11a_execution_authorized"])
        self.assertEqual(self.config["authorized_conditions"], list(ALLOWED_CONDITIONS))
        self.assertFalse(self.config["exp11b_execution_authorized"])
        self.assertFalse(self.exp12["execution_authorized"])

    def test_frozen_evidence_defines_exactly_thirty_variable_runs(self) -> None:
        specs = load_frozen_run_specs(self.evidence, _source_by_dam(self.historical_rows))
        self.assertEqual(specs[0]["run_id"], "H100_REEXECUTED_CHECK")
        self.assertEqual({spec["condition_id"]: sum(item["condition_id"] == spec["condition_id"] for item in specs) for spec in specs}, {"H25": 10, "H50": 10, "H75": 10, "H100": 1})
        h50 = [spec for spec in specs if spec["condition_id"] == "H50"]
        self.assertEqual(sum(spec["dominant_stratum"] == "D1" for spec in h50), 5)
        self.assertEqual(sum(spec["dominant_stratum"] == "D2" for spec in h50), 5)
        self.assertEqual([spec["seed"] for spec in h50 if spec["dominant_stratum"] == "D1"], [20261001, 20261002, 20261003, 20261004, 20261005])

    def test_frozen_subsets_match_evidence_without_reselection(self) -> None:
        specs = load_frozen_run_specs(self.evidence, _source_by_dam(self.historical_rows))
        for spec in specs:
            subset = _subset_rows(self.historical_rows, spec)
            self.assertEqual(len(subset), spec["expected_rows"])
            self.assertEqual({row["DECLARACION"] for row in subset}, set(spec["dam_ids"]))
            self.assertEqual(len({row["DECLARACION"] for row in subset}), spec["expected_dam_count"])

    def test_inputs_and_bm25_contract_are_frozen(self) -> None:
        self.assertEqual(historical.sha256_file(self.historical_path), H100_SHA256)
        self.assertEqual(historical.sha256_file(self.eval_path), EVAL_SHA256)
        self.assertEqual(historical.K_VALUES, [1, 3, 5, 10, 50])
        self.assertEqual(self.config["target_conditions"]["H150"]["enabled"], False)
        self.assertEqual(self.config["target_conditions"]["H200"]["enabled"], False)

    def test_git_status_parser_preserves_permitted_path_with_spaces(self) -> None:
        status = "?? data/Series - Descripciones.xlsx\0?? Referencias/Antecedentes/\0"
        with patch("src.experiments.run_exp11a_historical_size_sensitivity_v03._git", return_value=status):
            self.assertEqual(
                _canonical_status_lines(ROOT),
                ["?? data/Series - Descripciones.xlsx", "?? Referencias/Antecedentes/"],
            )


if __name__ == "__main__":
    unittest.main()
