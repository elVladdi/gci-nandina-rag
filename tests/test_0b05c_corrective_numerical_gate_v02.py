"""Contract tests for the closed 0B-05C numerical gate v0.2."""

from __future__ import annotations

import copy
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src.experiments import build_bm25_corrective_0b05c_v02 as builder
from src.experiments import prepare_0b05c_corrective_numerical_gate_v02 as gate
from src.experiments import run_0b05c_corrective_numerical_v02 as runner
from src.experiments.run_d1a_corrective_0b05c_v02 import preflight as d1a_preflight


ROOT = Path(__file__).resolve().parents[1]


def load_bundle() -> dict:
    return {
        key: gate.read_json(ROOT, gate.AUDIT_ROOT / name)
        for key, name in zip(("ev03", "ev04", "d1a", "gate", "manifest", "ledger"), gate.ARTIFACT_NAMES, strict=True)
    }


def candidate_revision() -> tuple[str, bool]:
    status = subprocess.run(
        ["git", "status", "--short", "--untracked-files=no"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    return ("HEAD", True) if not status else ("INDEX", False)


class CorrectiveNumericalGateV02Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = load_bundle()

    def test_01_closed_preflight_passes_read_only(self) -> None:
        before = {path: path.stat().st_mtime_ns for path in (ROOT / gate.AUDIT_ROOT).iterdir()}
        revision, require_clean = candidate_revision()
        result = gate.preflight(ROOT, revision=revision, require_clean=require_clean)
        after = {path: path.stat().st_mtime_ns for path in (ROOT / gate.AUDIT_ROOT).iterdir()}
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["mode"], "PREEXECUTION_CLOSED_READONLY")
        self.assertEqual(result["authorization_readiness"], "NOT_AUTHORIZATION_READY")
        self.assertEqual(before, after)

    def test_02_all_four_authorizations_are_closed(self) -> None:
        authorization = self.bundle["gate"]["authorization"]
        for name in ("EV03", "EV04", "D1A", "UNIFIED_0B05C"):
            self.assertEqual(authorization[f"{name}_NUMERICAL_EXECUTION"], "NOT_AUTHORIZED")

    def test_03_execute_authorized_stops_before_side_effects(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with mock.patch.object(runner, "read_json", return_value=self.bundle["gate"]):
                with self.assertRaisesRegex(gate.ContractViolation, "four.*AUTHORIZED"):
                    runner.execute_authorized(root)
            self.assertEqual(list(root.iterdir()), [])

    def test_04_every_future_root_is_absent(self) -> None:
        self.assertTrue(all(not (ROOT / relative).exists() for relative in gate.FUTURE_ROOTS))

    def test_05_no_overwrite_or_resume(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output = root / "index" / "index.pkl"
            output.parent.mkdir()
            output.write_bytes(b"partial")
            corpus = root / "corpus.jsonl"
            corpus.write_text("{}\n", encoding="utf-8")
            with self.assertRaisesRegex(gate.ContractViolation, "overwrite or resume"):
                builder.build("EV03", corpus, output, root / "index" / "metadata.json", root=root)

    def test_06_fake_operations_follow_exact_19_step_order(self) -> None:
        calls: list[str] = []
        operations = {}
        for key in runner.OPERATION_KEYS:
            status = "PASS_EXACT" if key in {"verify_ev03", "verify_ev04"} else "PASS"
            operations[key] = lambda key=key, status=status: calls.append(key) or {"status": status}
        result = runner.run_authorized_pipeline(operations)
        self.assertEqual(calls, list(runner.OPERATION_KEYS))
        self.assertEqual(result["execution_order"], list(gate.PIPELINE_STEPS))

    def test_07_failure_short_circuits_without_retry(self) -> None:
        calls: list[str] = []
        operations = {}
        for key in runner.OPERATION_KEYS:
            status = "FAIL" if key == "ev03_build" else ("PASS_EXACT" if key in {"verify_ev03", "verify_ev04"} else "PASS")
            operations[key] = lambda key=key, status=status: calls.append(key) or {"status": status}
        with self.assertRaisesRegex(gate.ContractViolation, "stopped"):
            runner.run_authorized_pipeline(operations)
        self.assertEqual(calls[-1], "ev03_build")
        self.assertEqual(calls.count("ev03_build"), 1)

    def test_08_ev03_corrected_is_blocked_without_exact_control(self) -> None:
        operations = {key: (lambda: {"status": "PASS"}) for key in runner.OPERATION_KEYS}
        with self.assertRaisesRegex(gate.ContractViolation, "verify_ev03 must be PASS_EXACT"):
            runner.run_authorized_pipeline(operations)

    def test_09_ev04_corrected_is_blocked_without_exact_control(self) -> None:
        operations = {}
        for key in runner.OPERATION_KEYS:
            status = "PASS" if key == "verify_ev04" else ("PASS_EXACT" if key == "verify_ev03" else "PASS")
            operations[key] = lambda status=status: {"status": status}
        with self.assertRaisesRegex(gate.ContractViolation, "verify_ev04 must be PASS_EXACT"):
            runner.run_authorized_pipeline(operations)

    def test_10_ev03_uses_recovered_len1_policy(self) -> None:
        semantics = builder.ARM_SEMANTICS["EV03"]
        self.assertEqual(semantics["token_policy"], "DROP_SINGLE_CHARACTER_TOKENS")
        self.assertEqual(semantics["builder"], "build_ev03_recovered_historical_from_corpus")
        self.assertFalse(semantics["global_builder_direct_use"])

    def test_11_ev04_does_not_inherit_ev03_policy(self) -> None:
        semantics = builder.ARM_SEMANTICS["EV04"]
        self.assertEqual(semantics["token_policy"], "ORIGINAL_HIERARCHICAL_V0.1")
        self.assertFalse(semantics["inherits_ev03_policy"])
        self.assertEqual(semantics["kwargs"]["text_field"], "texto_index_jerarquico")

    def test_12_decision906_patch_is_exactly_two_codes(self) -> None:
        for arm in ("ev03", "ev04"):
            patches = self.bundle[arm]["corrective_corpus"]["patches"]
            self.assertEqual([item["code"] for item in patches], ["87044110", "87045110"])
            self.assertTrue(all(item["replacement"]["titulo"] == "Inferior a 4,537 t" for item in patches))

    def test_13_d1a_freezes_model_and_forbids_retraining(self) -> None:
        spec = self.bundle["d1a"]
        self.assertEqual(spec["model_policy"]["MODEL_POLICY"], "FREEZE_ORIGINAL_D1A_WEIGHTS")
        self.assertTrue(spec["model_policy"]["must_not_retrain"])
        self.assertEqual(spec["model_policy"]["weights"]["sha256"], gate.MODEL_IDENTITY["sha256"])
        self.assertEqual(spec["index_builder"]["policy"], "FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD")
        self.assertEqual(spec["evaluation"]["ranking_depth"], 200)

    def test_14_v02_roots_are_disjoint_from_v01(self) -> None:
        self.assertTrue(set(gate.FUTURE_ROOTS).isdisjoint(gate.V01_ROOTS))
        self.assertTrue(all("v0.2" in path for path in gate.FUTURE_ROOTS))

    def test_15_canonical_binding_mutation_fails_closed(self) -> None:
        current = gate.git_binding(ROOT, "src/bm25_index.py", "HEAD")
        changed = copy.deepcopy(current)
        changed["canonical_git_blob_sha256"] = "0" * 64
        self.assertNotEqual(current, changed)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
            (root / "bound.txt").write_text("one\n", encoding="utf-8")
            subprocess.run(["git", "add", "bound.txt"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "-c", "user.name=Codex", "-c", "user.email=codex@example.invalid", "commit", "-m", "fixture"], cwd=root, check=True, capture_output=True)
            frozen = gate.git_binding(root, "bound.txt", "HEAD")
            (root / "bound.txt").write_text("two\n", encoding="utf-8")
            subprocess.run(["git", "add", "bound.txt"], cwd=root, check=True, capture_output=True)
            self.assertNotEqual(frozen, gate.git_binding(root, "bound.txt", "INDEX"))

    def test_16_contracts_have_no_operational_authorized_state(self) -> None:
        for key in ("ev03", "ev04", "d1a", "gate", "manifest", "ledger"):
            serialized = gate.canonical_json_bytes(self.bundle[key]).decode("utf-8")
            self.assertNotIn('"AUTHORIZED"', serialized)
        self.assertFalse((ROOT / gate.AUTHORIZATION_RECORD).exists())

    def test_17_tests_leave_no_persistent_outputs(self) -> None:
        self.assertTrue(all(not (ROOT / relative).exists() for relative in gate.FUTURE_ROOTS))

    def test_18_ev03_control_contract_is_byte_and_metric_exact(self) -> None:
        control = self.bundle["ev03"]["required_control"]
        self.assertEqual(control["status"], "PASS_EXACT")
        self.assertEqual(control["logical_index_identity"], "EXACT")
        self.assertEqual(control["ranking_rows"], 50327)
        self.assertEqual(control["cases"], 1056)
        self.assertTrue(control["ranking_bytes_exact"] and control["case_summary_bytes_exact"])
        self.assertTrue(control["metric_table_exact"] and control["full_metrics_exact"])

    def test_19_gate_and_ledger_are_complete(self) -> None:
        payload = self.bundle["gate"]
        self.assertEqual(payload["gate_scope"], "UNIFIED_0B05C_NUMERICAL_PREEXECUTION")
        self.assertEqual(payload["gate_status"], "CANDIDATE_PENDING_EXTERNAL_AUDIT")
        self.assertEqual(self.bundle["ledger"]["mismatch_count"], 0)
        categories = {item["classification"] for item in self.bundle["ledger"]["entries"]}
        self.assertTrue({"VERSIONED_GIT_BLOB", "FROZEN_BINARY_GIT_BLOB", "FROZEN_FILE_IDENTITY", "FUTURE_GENERATED_OUTPUT_NOT_PRESENT"} <= categories)

    def test_20_d1a_closed_preflight_is_read_only(self) -> None:
        revision, _ = candidate_revision()
        self.assertEqual(d1a_preflight(ROOT, revision=revision)["mode"], "PREEXECUTION_CLOSED_READONLY")


if __name__ == "__main__":
    unittest.main()
