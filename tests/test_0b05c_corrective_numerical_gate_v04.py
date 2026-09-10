from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.experiments import prepare_0b05c_corrective_numerical_gate_v04 as gate
from src.experiments import run_0b05c_corrective_numerical_v04 as runner


ROOT = Path(__file__).resolve().parents[1]
SHADOW = ROOT / "outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json"


class CorrectiveNumericalGateV04Tests(unittest.TestCase):
    def test_exactly_six_gate_artifacts_exist(self) -> None:
        root = ROOT / gate.AUDIT_ROOT
        self.assertEqual(sorted(path.name for path in root.glob("*.json")), sorted(gate.ARTIFACT_NAMES))

    def test_gate_and_specs_are_unauthorized(self) -> None:
        bundle = gate.build_bundle(ROOT, "INDEX")
        self.assertEqual(bundle["gate"]["gate_status"], "CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED")
        self.assertEqual(bundle["gate"]["authorization_readiness"], "NOT_AUTHORIZED")
        self.assertEqual(bundle["gate"]["authorization"], gate.AUTHORIZATION)
        for name, key in (("ev03", "EV03_NUMERICAL_EXECUTION"), ("ev04", "EV04_NUMERICAL_EXECUTION"), ("d1a", "D1A_NUMERICAL_EXECUTION")):
            self.assertEqual(bundle[name]["authorization"][key], "NOT_AUTHORIZED")
            self.assertEqual(bundle[name]["attempt05"], "NOT_AUTHORIZED / NOT_EXECUTED")

    def test_authorization_record_is_absent(self) -> None:
        self.assertFalse((ROOT / gate.AUTHORIZATION_RECORD).exists())

    def test_all_future_roots_are_new_and_absent(self) -> None:
        self.assertEqual(len(gate.FUTURE_ROOTS), 16)
        self.assertTrue(all("v0.4" in path for path in gate.FUTURE_ROOTS))
        self.assertTrue(all(not (ROOT / path).exists() for path in gate.FUTURE_ROOTS))

    def test_pipeline_preserves_exact_19_step_order(self) -> None:
        self.assertEqual(len(gate.PIPELINE_STEPS), 19)
        self.assertEqual(len(runner.OPERATION_KEYS), 19)

    def test_reuses_v03_builder_and_d1a_runner(self) -> None:
        source = (ROOT / "src/experiments/run_0b05c_corrective_numerical_v04.py").read_text(encoding="utf-8")
        self.assertIn("build_bm25_corrective_0b05c_v03", source)
        self.assertIn("run_d1a_corrective_0b05c_v03", source)
        self.assertFalse((ROOT / "src/experiments/build_bm25_corrective_0b05c_v04.py").exists())
        self.assertFalse((ROOT / "src/experiments/run_d1a_corrective_0b05c_v04.py").exists())

    def test_preflight_passes_read_only(self) -> None:
        result = gate.preflight(ROOT, revision="INDEX", require_clean=False)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["mode"], "PREEXECUTION_CLOSED_READONLY")
        self.assertFalse(result["numerical_execution_occurred"])

    def test_authorized_preflight_rejects_before_side_effects(self) -> None:
        before = {path: (ROOT / path).exists() for path in gate.FUTURE_ROOTS}
        with self.assertRaises(gate.ContractViolation):
            runner.preflight_authorized(ROOT)
        after = {path: (ROOT / path).exists() for path in gate.FUTURE_ROOTS}
        self.assertEqual(before, after)
        self.assertFalse(any(after.values()))

    def test_shadow_contains_twenty_passing_invariants(self) -> None:
        payload = json.loads(SHADOW.read_text(encoding="utf-8"))
        self.assertEqual(len(payload["pre_mortem_invariants"]), 20)
        self.assertTrue(all(item["status"] == "PASS" for item in payload["pre_mortem_invariants"]))

    def test_shadow_covers_a_through_f(self) -> None:
        payload = json.loads(SHADOW.read_text(encoding="utf-8"))
        self.assertEqual(list(payload["shadow_controls"]), ["A", "B", "C", "D", "E", "F"])
        self.assertTrue(all(item["status"] == "PASS" for item in payload["shadow_controls"].values()))

    def test_scientific_state_remains_open(self) -> None:
        self.assertEqual(gate.SCIENTIFIC_STATE["0B05C_METRIC_IMPACT"], "NOT_DETERMINED")
        self.assertEqual(gate.SCIENTIFIC_STATE["0B05C_CLOSURE"], "NOT_AUTHORIZED")


if __name__ == "__main__":
    unittest.main()
