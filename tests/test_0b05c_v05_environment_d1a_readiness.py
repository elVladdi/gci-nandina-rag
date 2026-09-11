from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src.experiments import prepare_0b05c_corrective_numerical_gate_v05 as gate
from src.experiments import run_d1a_corrective_0b05c_v05 as d1a


ROOT = Path(__file__).resolve().parents[1]


class EnvironmentReadinessV05Tests(unittest.TestCase):
    def test_candidate_is_closed_and_all_v05_roots_are_absent(self) -> None:
        result = gate.preflight(ROOT)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["attempt06"], "NOT_AUTHORIZED / NOT_EXECUTED")
        self.assertFalse(any((ROOT / path).exists() for path in gate.FUTURE_ROOTS))

    def test_v05_roots_are_disjoint_and_never_reference_v04_as_input(self) -> None:
        self.assertEqual(len(gate.FUTURE_ROOTS), 16)
        self.assertTrue(set(gate.FUTURE_ROOTS).isdisjoint(gate.V04_ROOTS))
        bundle = gate.build_bundle(ROOT)
        self.assertEqual(bundle["gate"]["v04_partial_roots"]["policy"], "NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05")

    def test_authorization_record_is_absent(self) -> None:
        self.assertFalse((ROOT / gate.AUTHORIZATION_RECORD).exists())

    def test_complete_model_manifest_requires_all_nine_files(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            files = []
            for index in range(9):
                path = root / "models/m" / f"f{index}"
                path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(str(index).encode())
                files.append({"path": path.relative_to(root).as_posix(), "size_bytes": 1, "sha256": gate._sha256(path)})
            metadata = {"inputs": {"model": {"path": "models/m", "files": files}}}
            (root / gate.MODEL_METADATA).parent.mkdir(parents=True)
            (root / gate.MODEL_METADATA).write_text(json.dumps(metadata), encoding="utf-8")
            self.assertEqual(gate.validate_complete_model_directory(root)["governed_file_count"], 9)
            (root / files[-1]["path"]).unlink()
            with self.assertRaises(gate.ContractViolation):
                gate.validate_complete_model_directory(root)

    def test_complete_model_manifest_rejects_hash_and_extra_file(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); model = root / "models/m"; model.mkdir(parents=True)
            files = []
            for index in range(9):
                path = model / f"f{index}"; path.write_bytes(b"x")
                files.append({"path": path.relative_to(root).as_posix(), "size_bytes": 1, "sha256": gate._sha256(path)})
            metadata = {"inputs": {"model": {"path": "models/m", "files": files}}}
            (root / gate.MODEL_METADATA).parent.mkdir(parents=True)
            (root / gate.MODEL_METADATA).write_text(json.dumps(metadata), encoding="utf-8")
            (model / "f0").write_bytes(b"y")
            with self.assertRaises(gate.ContractViolation):
                gate.validate_complete_model_directory(root)
            (model / "f0").write_bytes(b"x"); (model / "extra").write_bytes(b"x")
            with self.assertRaises(gate.ContractViolation):
                gate.validate_complete_model_directory(root)

    def test_environment_preflight_binds_interpreter_packages_smoke_and_capacity(self) -> None:
        interpreter = Path(__file__).resolve()
        probe = {
            "python": "3.10.11",
            "packages": {**gate.TESTED_ENVIRONMENT["required_packages"], "transformers": "x", "tokenizers": "x", "safetensors": "x", "huggingface_hub": "x"},
            "builder_import": "PASS", "evaluator_import": "PASS",
            "smoke": {"shape": [32, 384], "dtype": "float32", "all_finite": True, "norms_within_tolerance": True, "norm_min": 1.0, "norm_max": 1.0, "tolerance": 1e-6},
        }
        usage = type("Usage", (), {"free": gate.DISK_MARGIN_BYTES + 1})()
        with mock.patch.object(gate, "_sha256", return_value=gate.TESTED_ENVIRONMENT["executable_sha256"]), \
             mock.patch.object(gate, "validate_complete_model_directory", return_value={"status": "PASS_EXACT"}), \
             mock.patch.object(gate, "_interpreter_probe", return_value=probe), \
             mock.patch.object(gate, "optional_historical_vector_replay", return_value={"status": "PASS"}), \
             mock.patch.object(gate.shutil, "disk_usage", return_value=usage), \
             mock.patch.object(gate, "_available_memory", return_value=(10_000_000_000, gate.MEMORY_MARGIN_BYTES + 1)):
            result = gate.preauthorization_environment_preflight(ROOT, interpreter)
        self.assertEqual(result["status"], "PASS")
        self.assertFalse(result["numerical_execution_occurred"])

    def test_environment_preflight_rejects_wrong_interpreter_or_package(self) -> None:
        interpreter = Path(__file__).resolve()
        with mock.patch.object(gate, "_sha256", return_value="0" * 64):
            with self.assertRaises(gate.ContractViolation):
                gate.preauthorization_environment_preflight(ROOT, interpreter)
        probe = {"python": "3.10.11", "packages": {**gate.TESTED_ENVIRONMENT["required_packages"], "numpy": "0"}, "smoke": {}}
        with mock.patch.object(gate, "_sha256", return_value=gate.TESTED_ENVIRONMENT["executable_sha256"]), \
             mock.patch.object(gate, "validate_complete_model_directory", return_value={"status": "PASS_EXACT"}), \
             mock.patch.object(gate, "_interpreter_probe", return_value=probe):
            with self.assertRaises(gate.ContractViolation):
                gate.preauthorization_environment_preflight(ROOT, interpreter)

    def test_d1a_closed_preflight_has_no_side_effect(self) -> None:
        before = {path: (ROOT / path).exists() for path in d1a.D1A_ROOTS}
        result = d1a.preflight(ROOT)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(before, {path: (ROOT / path).exists() for path in d1a.D1A_ROOTS})

    def test_d1a_real_execute_is_rejected_while_unauthorized(self) -> None:
        with self.assertRaises(gate.ContractViolation):
            d1a.execute_authorized(ROOT, authorization_proof={})
        self.assertFalse(any((ROOT / path).exists() for path in d1a.D1A_ROOTS))


if __name__ == "__main__":
    unittest.main()
