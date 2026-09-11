from __future__ import annotations

import copy
import csv
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src.experiments import evaluate_normative_bm25_corrective_0b05c_v05 as evaluator
from src.experiments import prepare_0b05c_corrective_numerical_gate_v05 as gate
from src.experiments import run_d1a_corrective_0b05c_v05 as d1a
from src.experiments import run_0b05c_corrective_numerical_v05 as runner


ROOT = Path(__file__).resolve().parents[1]


def authorized_artifacts(baseline: dict[str, dict]) -> dict[str, dict]:
    authorized = copy.deepcopy(baseline)
    unified = authorized["unified_gate"]
    unified["gate_status"] = gate.AUTHORIZED_GATE_STATUS
    unified["authorization_readiness"] = gate.AUTHORIZED_READINESS
    unified["attempt06"] = gate.AUTHORIZED_ATTEMPT06
    for key in unified["authorization"]:
        if key.endswith("NUMERICAL_EXECUTION"):
            unified["authorization"][key] = "AUTHORIZED"
    unified["authorization"]["authorization_record_present"] = True
    for artifact, key in gate.AUTHORIZATION_SPEC_KEYS.items():
        authorized[artifact]["authorization"][key] = "AUTHORIZED"
        authorized[artifact]["attempt06"] = gate.AUTHORIZED_ATTEMPT06
    return authorized


class D1aLedgerAuthorizationContractsV05Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = gate.build_bundle(ROOT)
        cls.baseline = {
            "unified_gate": cls.bundle["gate"], "ev03_spec": cls.bundle["ev03"],
            "ev04_spec": cls.bundle["ev04"], "d1a_spec": cls.bundle["d1a"],
        }

    def test_d1a_three_way_runner_path_identity(self) -> None:
        sets = d1a.d1a_path_contract_sets(ROOT, self.bundle["d1a"])
        unified = {path for path in self.bundle["ledger"]["expected_set"] if Path(path).name in set(gate.D1A_RUNNER_OUTPUTS.values())}
        self.assertEqual(sets["D1A_SPEC_RUNNER_SET"], sets["D1A_ACTUAL_PRODUCER_SET"])
        self.assertEqual(sets["D1A_SPEC_RUNNER_SET"], unified)
        for side in ("spec", "producer", "unified"):
            mutated = {key: set(value) for key, value in sets.items()}
            target = unified.copy()
            if side == "spec": mutated["D1A_SPEC_RUNNER_SET"].remove(next(iter(mutated["D1A_SPEC_RUNNER_SET"])))
            elif side == "producer": mutated["D1A_ACTUAL_PRODUCER_SET"].add("wrong-v0.1.json")
            else: target.add("wrong-v0.4.json")
            with self.subTest(side=side), self.assertRaises(gate.ContractViolation):
                gate.require(mutated["D1A_SPEC_RUNNER_SET"] == mutated["D1A_ACTUAL_PRODUCER_SET"] == target, "D1a three-way path mismatch")

    def test_d1a_hash_ledger_contract_matches_actual_adapter_producers(self) -> None:
        spec = self.bundle["d1a"]
        declared = {path.relative_to(ROOT).as_posix() for path in d1a.contractual_ledger_paths(ROOT, spec)}
        actual = d1a.actual_producer_set(ROOT, spec)
        ledger = spec["orchestration"]["runner_outputs"]["hash_ledger"]
        self.assertEqual(declared, actual - {ledger})
        self.assertEqual(spec["orchestration"]["hash_ledger_contract"]["excluded_self_path"], ledger)

    def test_expected_and_producer_sets_are_independently_equal(self) -> None:
        expected = set(gate.expected_runtime_paths_from_specs(self.bundle["ev03"], self.bundle["ev04"], self.bundle["d1a"]))
        produced = set(gate.producer_runtime_paths())
        self.assertEqual(expected, produced)
        self.assertEqual(len(expected), 47)
        changed = copy.deepcopy(self.bundle)
        changed["gate"]["runtime_hash_ledger_contract"]["expected_paths"] = ["poisoned"]
        self.assertEqual(set(gate.producer_runtime_paths(changed)), produced)

    def test_observed_filesystem_exact_missing_extra_failure_and_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); output = root / "runtime"; output.mkdir()
            first, second = output / "a.json", output / "b.csv"
            first.write_text("{}\n", encoding="utf-8"); second.write_text("x\n", encoding="utf-8")
            expected = {"runtime/a.json", "runtime/b.csv"}
            entries = gate.validate_runtime_ledger(root, expected, expected, discovery_roots=("runtime",), excluded_self_path="runtime/ledger.json")
            self.assertEqual({row["path"] for row in entries}, expected)
            first.unlink()
            with self.assertRaises(gate.ContractViolation):
                gate.validate_runtime_ledger(root, expected, expected, discovery_roots=("runtime",))
            first.write_text("{}\n", encoding="utf-8"); extra = output / "extra.txt"; extra.write_text("x", encoding="utf-8")
            with self.assertRaises(gate.ContractViolation):
                gate.validate_runtime_ledger(root, expected, expected, discovery_roots=("runtime",))
            extra.unlink(); failed = output / "execution_failed.json"; failed.write_text("{}", encoding="utf-8")
            with self.assertRaises(gate.ContractViolation):
                gate.validate_runtime_ledger(root, expected, expected, discovery_roots=("runtime",))
            failed.unlink(); snapshot = {"runtime/a.json": gate._sha256(first)}; first.write_text('{"changed":true}\n', encoding="utf-8")
            with self.assertRaises(gate.ContractViolation):
                gate.validate_runtime_ledger(root, expected, expected, snapshot=snapshot, discovery_roots=("runtime",))

    def test_positive_authorization_transition_shadow(self) -> None:
        result = gate.validate_authorization_transition(self.baseline, authorized_artifacts(self.baseline))
        self.assertEqual(result["status"], "PASS")
        self.assertTrue(result["allowed_fields_only"])

    def test_positive_authorized_preflight_shadow_has_no_side_effects(self) -> None:
        authorized = authorized_artifacts(self.baseline)
        transition = {
            "authorization_record_binding": {"path": gate.AUTHORIZATION_RECORD.as_posix(), "git_blob_sha1": "a" * 40, "canonical_git_blob_sha256": "b" * 64, "canonical_size_bytes": 1},
            "authorization_baseline_commit": "c" * 40, "execution_authorization_commit": "d" * 40,
            "transition": {"status": "PASS"},
            "authorization_commit_shape": {"status": "PASS", "mode": "DIRECT_PARENT_EXACT_FIVE_PATH_AUTHORIZATION_DIFF"},
            "current_dependency_bindings_equal_baseline": True,
            "authorized_artifact_bindings": {key: {} for key in gate.AUTHORIZATION_BASELINE_ARTIFACTS},
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for key, path in gate.AUTHORIZATION_BASELINE_ARTIFACTS.items():
                target = root / path; target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(authorized[key]), encoding="utf-8")
            auth = root / gate.AUTHORIZATION_RECORD; auth.write_text("{}", encoding="utf-8")
            completed = subprocess.CompletedProcess([], 0, stdout="", stderr="")
            environment = {"status": "PASS", "interpreter": {"python_version": gate.TESTED_ENVIRONMENT["python_version"], "executable_sha256": gate.TESTED_ENVIRONMENT["executable_sha256"]}}
            with mock.patch.object(runner.subprocess, "run", return_value=completed), \
                 mock.patch.object(runner, "load_authorization_transition_from_git", return_value=transition), \
                 mock.patch.object(runner, "preauthorization_environment_preflight", return_value=environment), \
                 mock.patch.object(runner, "build_bundle", return_value=self.bundle):
                proof = runner.preflight_authorized(root)
            self.assertEqual(proof["mode"], "AUTHORIZED_PREFLIGHT_ONLY")
            self.assertFalse(proof["numerical_execution_occurred"])
            self.assertFalse(any((root / path).exists() for path in gate.FUTURE_ROOTS))

    def test_authorization_transition_rejects_scientific_root_environment_and_code_drift(self) -> None:
        for label, mutate in (
            ("scientific", lambda a: a["unified_gate"]["methodological_invariants"].update({"mrr_at_100": "changed"})),
            ("root", lambda a: a["unified_gate"]["future_roots"].append("unexpected")),
            ("environment", lambda a: a["unified_gate"]["environment_contract"].update({"python_version": "0"})),
            ("code", lambda a: a["unified_gate"]["candidate_source_bindings"][0].update({"git_blob_sha1": "0" * 40})),
        ):
            value = authorized_artifacts(self.baseline); mutate(value)
            with self.subTest(label=label), self.assertRaises(gate.ContractViolation):
                gate.validate_authorization_transition(self.baseline, value)

    def test_authorization_record_exact_schema_and_binding_sha(self) -> None:
        contract = gate.authorization_record_contract()
        binding = {"path": "x", "git_blob_sha1": "a" * 40, "canonical_git_blob_sha256": "b" * 64, "canonical_size_bytes": 1}
        record = {
            "artifact_id": gate.AUTHORIZATION_RECORD_ID, "schema_version": gate.AUTHORIZATION_RECORD_SCHEMA_VERSION,
            "authorization_baseline_commit": "a" * 40, "baseline_external_audit": contract["baseline_external_audit"],
            "baseline_artifacts": {key: {**binding, "path": path} for key, path in gate.AUTHORIZATION_BASELINE_ARTIFACTS.items()},
        }
        gate.validate_authorization_record_schema(record)
        for mutation in (lambda x: x.pop("schema_version"), lambda x: x.update({"extra": 1})):
            changed = copy.deepcopy(record); mutation(changed)
            with self.assertRaises(gate.ContractViolation): gate.validate_authorization_record_schema(changed)
        wrong = copy.deepcopy(record); wrong["baseline_artifacts"]["unified_gate"]["git_blob_sha1"] = "0" * 40
        with mock.patch.object(gate, "authorization_artifact_binding", side_effect=lambda root, path, revision: record["baseline_artifacts"][next(key for key, value in gate.AUTHORIZATION_BASELINE_ARTIFACTS.items() if value == path)]):
            with self.assertRaises(gate.ContractViolation): gate.validate_authorization_record_bindings(ROOT, wrong)

    def test_baseline_must_be_proper_ancestor(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "test"], cwd=root, check=True)
            (root / "x").write_text("1", encoding="utf-8"); subprocess.run(["git", "add", "x"], cwd=root, check=True); subprocess.run(["git", "commit", "-qm", "one"], cwd=root, check=True)
            baseline = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            with self.assertRaises(gate.ContractViolation): gate.validate_authorization_baseline_ancestry(root, baseline)
            (root / "x").write_text("2", encoding="utf-8"); subprocess.run(["git", "commit", "-qam", "two"], cwd=root, check=True)
            self.assertEqual(len(gate.validate_authorization_baseline_ancestry(root, baseline)), 40)

    def test_filesystem_artifacts_must_match_authorized_commit(self) -> None:
        authorized = authorized_artifacts(self.baseline)
        gate.validate_filesystem_authorization_artifacts(authorized, copy.deepcopy(authorized))
        changed = copy.deepcopy(authorized); changed["ev03_spec"]["attempt06"] = "different"
        with self.assertRaises(gate.ContractViolation): gate.validate_filesystem_authorization_artifacts(authorized, changed)

    def test_complete_metric_objects_round_trip_and_derived_values(self) -> None:
        ev03_dir = ROOT / "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2"
        with (ev03_dir / "normative_case_summary.csv").open(encoding="utf-8-sig", newline="") as handle:
            ev03_cases = list(csv.DictReader(handle))
        ev03_metrics = json.loads((ev03_dir / "run_metadata.json").read_text(encoding="utf-8"))["metrics"]
        self.assertEqual(evaluator.validate_complete_metrics_v05("EV03", ev03_cases, ev03_metrics)["key_count"], 56)
        ev04_dir = ROOT / "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2"
        with (ev04_dir / "normative_hierarchical_case_summary.csv").open(encoding="utf-8-sig", newline="") as handle:
            ev04_cases = list(csv.DictReader(handle))
        ev04_metrics = evaluator.build_ev04_enriched_metrics(ev04_cases, require_real_case_count=True)
        reloaded = json.loads(json.dumps(ev04_metrics, sort_keys=True))
        result = evaluator.validate_complete_metrics_v05("EV04", ev04_cases, reloaded)
        self.assertEqual((result["key_count"], result["metric_row_count"]), (92, 27))
        reloaded["mrr_at_100"] += 0.1
        with self.assertRaises(gate.ContractViolation): evaluator.validate_complete_metrics_v05("EV04", ev04_cases, reloaded)

    def test_stale_current_identity_audit_and_negatives(self) -> None:
        self.assertEqual(gate.audit_stale_current_identities(self.bundle)["stale_current_identity_count"], 0)
        self.assertEqual(gate.audit_stale_source_tokens(ROOT)["stale_current_identity_count"], 0)
        for mutate in (
            lambda value: value["d1a"].update({"specification_id": "d1a_numerical_execution_spec_v0.4"}),
            lambda value: value["d1a"]["orchestration"]["runner_outputs"].update({"hash_ledger": "wrong_v0.1.csv"}),
        ):
            changed = copy.deepcopy(self.bundle); mutate(changed)
            with self.assertRaises(gate.ContractViolation): gate.audit_stale_current_identities(changed)


if __name__ == "__main__":
    unittest.main()
