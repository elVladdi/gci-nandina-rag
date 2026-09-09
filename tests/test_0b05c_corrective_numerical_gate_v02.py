"""Contract tests for the closed 0B-05C numerical gate v0.2."""

from __future__ import annotations

import copy
import hashlib
import json
import shlex
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
            with mock.patch.object(runner, "read_json", return_value=self.bundle["gate"]), \
                 mock.patch.object(runner.subprocess, "run", return_value=mock.Mock(stdout="")):
                with self.assertRaises(gate.ContractViolation):
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

    def _authorized_snapshot(self) -> tuple[dict, dict]:
        baseline = gate.authorization_snapshot(self.bundle["gate"], self.bundle["ev03"], self.bundle["ev04"], self.bundle["d1a"])
        candidate = copy.deepcopy(baseline)
        candidate["gate"]["gate_status"] = gate.AUTHORIZED_GATE_STATUS
        candidate["gate"]["authorization_readiness"] = gate.AUTHORIZED_READINESS
        for name in ("EV03", "EV04", "D1A", "UNIFIED_0B05C"):
            candidate["gate"]["authorization"][f"{name}_NUMERICAL_EXECUTION"] = "AUTHORIZED"
        candidate["gate"]["authorization"]["authorization_record_present"] = True
        candidate["EV03"]["authorization"]["EV03_NUMERICAL_EXECUTION"] = "AUTHORIZED"
        candidate["EV04"]["authorization"]["EV04_NUMERICAL_EXECUTION"] = "AUTHORIZED"
        candidate["D1a"]["authorization"]["D1A_NUMERICAL_EXECUTION"] = "AUTHORIZED"
        return baseline, candidate

    def test_21_gate_strings_alone_cannot_authorize(self) -> None:
        baseline, candidate = self._authorized_snapshot()
        candidate["gate"]["gate_status"] = baseline["gate"]["gate_status"]
        candidate["gate"]["authorization_readiness"] = baseline["gate"]["authorization_readiness"]
        candidate["gate"]["authorization"]["authorization_record_present"] = False
        candidate["EV03"] = baseline["EV03"]
        candidate["EV04"] = baseline["EV04"]
        candidate["D1a"] = baseline["D1a"]
        with self.assertRaises(gate.ContractViolation):
            gate.validate_authorization_transition(baseline, candidate)

    def test_22_complete_authorization_transition_is_accepted(self) -> None:
        baseline, candidate = self._authorized_snapshot()
        gate.validate_authorization_transition(baseline, candidate)

    def test_23_unauthorized_baseline_mutation_is_rejected(self) -> None:
        baseline, candidate = self._authorized_snapshot()
        candidate["EV03"]["methodology"]["k1"] = 1.6
        with self.assertRaisesRegex(gate.ContractViolation, "immutable"):
            gate.validate_authorization_transition(baseline, candidate)

    def test_24_authorization_record_schema_binds_four_git_artifacts(self) -> None:
        contract = gate.authorization_record_contract()
        self.assertEqual(contract["schema_version"], 2)
        self.assertEqual(contract["baseline_artifact_paths"], gate.AUTHORIZATION_BASELINE_ARTIFACTS)
        self.assertEqual(set(contract["baseline_identity_fields"]), {"path", "git_blob_sha1", "canonical_git_blob_sha256", "canonical_size_bytes"})

    def test_25_frozen_file_identity_is_checked_before_execution(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            model = root / "models/model.bin"
            model.parent.mkdir()
            model.write_bytes(b"frozen")
            binding = {"path": "models/model.bin", "classification": "FROZEN_FILE_IDENTITY", "size_bytes": 6, "sha256": hashlib.sha256(b"frozen").hexdigest()}
            runner.validate_dependency_bindings(root, [binding])
            model.write_bytes(b"changed")
            with self.assertRaisesRegex(gate.ContractViolation, "size mismatch|SHA mismatch"):
                runner.validate_dependency_bindings(root, [binding])

    @staticmethod
    def _control_fixture(root: Path, *, crlf_ranking: bool = False) -> tuple[dict, dict, Path, Path, dict, dict]:
        ranking = root / "ranking.csv"
        summary = root / "summary.csv"
        ranking_bytes = b"case_id,rank\n1,1\n2,2\n"
        ranking.write_bytes(ranking_bytes.replace(b"\n", b"\r\n") if crlf_ranking else ranking_bytes)
        summary.write_bytes(b"case_id,rank\n1,1\n2,2\n")
        required = {"ranking_rows": 2, "cases": 2, "ranking_sha256": hashlib.sha256(ranking_bytes).hexdigest(), "case_summary_sha256": hashlib.sha256(summary.read_bytes()).hexdigest()}
        comparison = {"status": "PASS", "ranking_schema_exact": True, "case_summary_schema_exact": True, "ranking_exact": True, "case_summary_exact": True, "metrics_exact": True}
        return required, comparison, ranking, summary, {"m": 1}, {"m": 1}

    def test_26_ev03_full_pass_exact(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            args = self._control_fixture(Path(temporary))
            result = runner.validate_control_exact("EV03", *args, logical_index_identity="EXACT")
            self.assertEqual(result["status"], "PASS_EXACT")
            self.assertTrue(all(result["checks"].values()))

    def test_27_ev03_ranking_byte_mismatch_fails_with_logical_rows_equal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            args = self._control_fixture(Path(temporary), crlf_ranking=True)
            with self.assertRaisesRegex(gate.ContractViolation, "PASS_EXACT"):
                runner.validate_control_exact("EV03", *args, logical_index_identity="EXACT")

    def test_28_ev03_case_summary_byte_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            args = list(self._control_fixture(Path(temporary)))
            args[0]["case_summary_sha256"] = "0" * 64
            with self.assertRaises(gate.ContractViolation):
                runner.validate_control_exact("EV03", *args, logical_index_identity="EXACT")

    def test_29_ev03_row_count_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            args = list(self._control_fixture(Path(temporary)))
            args[0]["ranking_rows"] = 3
            with self.assertRaises(gate.ContractViolation):
                runner.validate_control_exact("EV03", *args, logical_index_identity="EXACT")

    def test_30_ev03_logical_index_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(gate.ContractViolation):
                runner.validate_control_exact("EV03", *self._control_fixture(Path(temporary)), logical_index_identity="FAIL")

    def test_31_ev03_metrics_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            args = list(self._control_fixture(Path(temporary)))
            args[-1] = {"m": 2}
            with self.assertRaises(gate.ContractViolation):
                runner.validate_control_exact("EV03", *args, logical_index_identity="EXACT")

    def test_32_ev04_requires_both_frozen_shas(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            required, comparison, ranking, summary, expected, actual = self._control_fixture(Path(temporary))
            required.pop("ranking_rows")
            required.pop("cases")
            self.assertEqual(runner.validate_control_exact("EV04", required, comparison, ranking, summary, expected, actual)["status"], "PASS_EXACT")
            required["ranking_sha256"] = "0" * 64
            with self.assertRaises(gate.ContractViolation):
                runner.validate_control_exact("EV04", required, comparison, ranking, summary, expected, actual)

    def test_33_commands_use_only_canonical_v02_roots(self) -> None:
        for arm, roots in (("ev03", gate.EV03_ROOTS), ("ev04", gate.EV04_ROOTS)):
            commands = self.bundle[arm]["prospective_execution"]["commands"]
            tokens = [token for command in commands.values() for token in shlex.split(command)]
            for root in roots:
                self.assertTrue(any(token == root or token.startswith(root + "/") for token in tokens), root)
            self.assertFalse(any("bm25_nandina8_hierarchical_ev04_decision885_control_v0.2" in token for token in tokens))
            self.assertFalse(any("corpus_nandina_hierarchical_ev04_corrective" in token for token in tokens))

    def test_34_exact_ledger_includes_three_file_roots(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            corpora = [gate.EV03_ROOTS[2], gate.EV04_ROOTS[2], gate.D1A_ROOTS[0]]
            for relative in corpora:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("{}\n", encoding="utf-8")
            contract = {"expected_paths": corpora, "discovery_roots": corpora, "excluded_self_path": "ledger.json"}
            entries = runner.validate_runtime_ledger_contract(root, contract)
            self.assertEqual({item["path"] for item in entries}, set(corpora))

    def test_35_exact_ledger_missing_output_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            contract = {"expected_paths": ["missing.jsonl"], "discovery_roots": ["missing.jsonl"], "excluded_self_path": "ledger.json"}
            with self.assertRaisesRegex(gate.ContractViolation, "missing"):
                runner.validate_runtime_ledger_contract(Path(temporary), contract)

    def test_36_exact_ledger_unexpected_output_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / "output"
            directory.mkdir()
            (directory / "expected.json").write_text("{}", encoding="utf-8")
            (directory / "extra.json").write_text("{}", encoding="utf-8")
            contract = {"expected_paths": ["output/expected.json"], "discovery_roots": ["output"], "excluded_self_path": "ledger.json"}
            with self.assertRaisesRegex(gate.ContractViolation, "unexpected"):
                runner.validate_runtime_ledger_contract(root, contract)

    def test_37_d1a_summary_requires_aggregate_and_integrity_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            outputs = {"aggregate_comparison": "d1a/aggregate.json", "case_level_comparison": "d1a/cases.jsonl", "execution_manifest": "d1a/manifest.json", "hash_ledger": "d1a/ledger.csv"}
            for relative in outputs.values():
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
            (root / outputs["aggregate_comparison"]).write_text(json.dumps({"metrics": []}), encoding="utf-8")
            (root / outputs["case_level_comparison"]).write_text("{}\n", encoding="utf-8")
            (root / outputs["execution_manifest"]).write_text(json.dumps({"status": "PASS"}), encoding="utf-8")
            (root / outputs["hash_ledger"]).write_text("path,sha256,size_bytes\n", encoding="utf-8")
            result = runner._d1a_summary_reference(root, {"orchestration": {"runner_outputs": outputs}}, {"status": "PASS"})
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(set(result) - {"status"}, set(outputs))

    def test_38_d1a_summary_missing_aggregate_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            outputs = {"aggregate_comparison": "missing.json", "case_level_comparison": "missing2", "execution_manifest": "missing3", "hash_ledger": "missing4"}
            with self.assertRaisesRegex(gate.ContractViolation, "missing"):
                runner._d1a_summary_reference(Path(temporary), {"orchestration": {"runner_outputs": outputs}}, {"status": "PASS"})

    def test_39_frozen_runtime_ledger_contract_is_explicit(self) -> None:
        contract = self.bundle["gate"]["runtime_hash_ledger_contract"]
        self.assertEqual(contract["missing_or_unexpected_policy"], "FAIL_CLOSED")
        for corpus in (gate.EV03_ROOTS[2], gate.EV04_ROOTS[2], gate.D1A_ROOTS[0]):
            self.assertIn(corpus, contract["expected_paths"])

    def test_40_candidate_remains_closed_and_without_real_roots(self) -> None:
        self.assertEqual(self.bundle["gate"]["authorization_readiness"], "NOT_AUTHORIZATION_READY")
        self.assertFalse(self.bundle["gate"]["authorization"]["authorization_record_present"])
        self.assertFalse((ROOT / gate.AUTHORIZATION_RECORD).exists())
        self.assertTrue(all(not (ROOT / relative).exists() for relative in gate.FUTURE_ROOTS))

    def test_41_authorization_record_is_mandatory_before_static_inputs(self) -> None:
        _, candidate = self._authorized_snapshot()
        with tempfile.TemporaryDirectory() as temporary, \
             mock.patch.object(runner, "read_json", return_value=candidate["gate"]), \
             mock.patch.object(runner.subprocess, "run", return_value=mock.Mock(stdout="")):
            with self.assertRaisesRegex(gate.ContractViolation, "record v0.2 is required"):
                runner.preflight_authorized(Path(temporary))

    def test_42_ev04_case_summary_sha_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            required, comparison, ranking, summary, expected, actual = self._control_fixture(Path(temporary))
            required.pop("ranking_rows")
            required.pop("cases")
            required["case_summary_sha256"] = "0" * 64
            with self.assertRaises(gate.ContractViolation):
                runner.validate_control_exact("EV04", required, comparison, ranking, summary, expected, actual)

    def test_43_unified_summary_requires_d1a_aggregate_reference(self) -> None:
        with self.assertRaisesRegex(gate.ContractViolation, "aggregate comparison"):
            runner.build_unified_summary({}, {}, {"status": "PASS"})
        d1a = {"status": "PASS", "aggregate_comparison": {"path": "aggregate.json", "sha256": "a" * 64}}
        self.assertEqual(runner.build_unified_summary({}, {}, d1a)["D1a"], d1a)


if __name__ == "__main__":
    unittest.main()
