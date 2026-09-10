"""Contract tests for the isolated 0B-05C D1a v0.4 adapter."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.experiments import prepare_0b05c_corrective_numerical_gate_v04 as gate
from src.experiments import run_d1a_corrective_0b05c_v04 as d1a


ROOT = Path(__file__).resolve().parents[1]


class D1aCorrective0B05cRunnerV04Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec = json.loads((ROOT / d1a.SPEC_PATH).read_text(encoding="utf-8"))

    def test_v04_adapter_and_spec_bind_only_v04_or_original_components(self) -> None:
        self.assertEqual(d1a.SPEC_PATH, gate.AUDIT_ROOT / "d1a_numerical_execution_spec_v0.4.json")
        self.assertEqual(self.spec["orchestration"]["runner"]["path"], "src/experiments/run_d1a_corrective_0b05c_v04.py")
        self.assertEqual(self.spec["index_builder"]["code_identity"]["path"], "src/experiments/build_text2trade_mnrl_index_v02.py")
        self.assertEqual(self.spec["evaluation"]["code_identity"]["path"], "src/experiments/evaluate_text2trade_mnrl_data_aduanas_v02.py")
        self.assertTrue(all("v0.4" in path for path in self.spec["orchestration"]["future_roots"]))

    def test_v04_proof_is_accepted_and_v03_record_path_is_rejected(self) -> None:
        proof = {
            "status": "PASS",
            "mode": "AUTHORIZED_PREFLIGHT_ONLY",
            "authorization": dict(d1a.REQUIRED_UNIFIED_AUTHORIZATIONS),
            "authorization_baseline_commit": "a" * 40,
            "authorization_record_binding": {
                "path": gate.AUTHORIZATION_RECORD.as_posix(),
                "git_blob_sha1": "1" * 40,
                "canonical_git_blob_sha256": "2" * 64,
                "canonical_size_bytes": 1,
            },
        }
        d1a.validate_unified_authorization_proof(proof)
        invalid = copy.deepcopy(proof)
        invalid["authorization_record_binding"]["path"] = (
            "outputs/audits/0b05c_corrective_numerical_gate_v0.3/"
            "0b05c_numerical_authorization_record_v0.3.json"
        )
        with self.assertRaises(gate.ContractViolation):
            d1a.validate_unified_authorization_proof(invalid)

    def test_closed_preflight_passes_without_creating_v04_roots(self) -> None:
        before = {path: (ROOT / path).exists() for path in gate.D1A_ROOTS}
        proof = d1a.preflight(ROOT, revision="INDEX")
        after = {path: (ROOT / path).exists() for path in gate.D1A_ROOTS}
        self.assertEqual(proof["status"], "PASS")
        self.assertEqual(proof["mode"], "PREEXECUTION_CLOSED_READONLY")
        self.assertEqual(before, after)
        self.assertFalse(any(after.values()))

    def test_adapter_source_has_no_v03_gate_or_root_binding(self) -> None:
        source = Path(d1a.__file__).read_text(encoding="utf-8")
        self.assertNotIn("prepare_0b05c_corrective_numerical_gate_v03", source)
        self.assertNotIn("corrective_0b05c_v0.3", source)
        self.assertNotIn("run_0b05c_corrective_numerical_v03", source)


if __name__ == "__main__":
    unittest.main()
