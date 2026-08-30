from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class He4PhaseJPromptSchemaMicroauditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads((OUT / "gate_j_prompt_schema_microaudit_v0.2.json").read_text(encoding="utf-8"))

    def test_01_frozen_hashes_are_intact(self) -> None:
        self.assertTrue(all(item["pass"] for item in self.audit["hashes"].values()))

    def test_02_prompt_schema_mismatch_is_textually_reproducible(self) -> None:
        self.assertFalse(self.audit["prompt_audit"]["advertencias_globales_explicitly_required"])
        self.assertTrue(self.audit["schema_audit"]["advertencias_globales_required_root_field"])
        self.assertEqual(self.audit["classification"], "B. PROMPT-SCHEMA SPECIFICATION MISMATCH")

    def test_03_schema_impact_is_exact(self) -> None:
        impact = self.audit["schema_impact"]
        self.assertEqual(impact["cases_failing_only_advertencias_globales"], 50)
        self.assertEqual(impact["cases_with_other_schema_errors"], 0)
        self.assertEqual(impact["cases_complete_if_field_is_not_evaluable"], 50)

    def test_04_warning_controls_are_separated(self) -> None:
        controls = self.audit["warning_control_decomposition"]
        self.assertEqual(controls["warnings_field_valid"], "50/50")
        self.assertEqual(controls["generic_normative_warning_when_required"], "41/50")
        self.assertEqual(len(controls["cases_failing_warnings_field"]), 0)
        self.assertEqual(len(controls["cases_failing_generic_control"]), 9)
        self.assertEqual(controls["overlap"], [])

    def test_05_generic_rule_and_rubric_interpretation_are_frozen(self) -> None:
        self.assertTrue(self.audit["warning_control_decomposition"]["generic_rule_pre_specified"])
        self.assertFalse(self.audit["rubric_audit"]["advertencias_globales_present"])
        self.assertFalse(self.audit["rubric_audit"]["missing_advertencias_globales_is_hard_violation"])

    def test_06_original_j_outputs_and_phase_k_remain_unchanged(self) -> None:
        self.assertTrue(self.audit["original_j_metrics_preserved"])
        self.assertTrue(self.audit["gate_j"]["preserved"])
        self.assertFalse(self.audit["phase_k_executed"])
        self.assertFalse(self.audit["rubric_applied"])

    def test_07_microaudit_has_no_model_or_retrieval_dependency(self) -> None:
        source = (ROOT / "src/experiments/audit_he4_phase_j_prompt_schema_v02.py").read_text(encoding="utf-8").lower()
        for forbidden in ("import urllib", "import requests", "http://", "https://", "ollama", "bm25", "embedding"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
