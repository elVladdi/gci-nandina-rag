from __future__ import annotations

import copy
import json
import math
import tempfile
import unittest
from pathlib import Path

from src.experiments import prepare_0b05c_corrective_numerical_gate_v05 as gate
from src.experiments import run_0b05c_corrective_numerical_v05 as runner


ROOT = Path(__file__).resolve().parents[1]


def aggregate(names):
    return {"status": "PASS", "metrics": [{"metric": name, "original_numerator": 1.0, "corrected_numerator": 1.0, "denominator": 2, "original_value": 0.5, "corrected_value": 0.5, "absolute_delta": 0.0} for name in names]}


def d1a():
    reference = {"path": "x", "sha256": "a" * 64, "size_bytes": 1}
    return {"status": "PASS", **{key: dict(reference) for key in runner.D1A_REFERENCE_KEYS}}


class SummaryManifestLedgerOrchestrationV05Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.ev03 = aggregate(runner.EV03_AGGREGATE_ORDER)
        from src.experiments.evaluate_normative_bm25_corrective_0b05c_v05 import EV04_AGGREGATE_METRIC_ORDER
        self.ev04 = aggregate(EV04_AGGREGATE_METRIC_ORDER)
        self.d1a = d1a()

    def test_strict_summary_positive(self) -> None:
        result = runner.strict_unified_summary(self.ev03, self.ev04, self.d1a)
        self.assertEqual(result["status"], "PASS")

    def test_strict_summary_rejects_missing_wrong_empty_or_failed_d1a(self) -> None:
        for payload in (None, [], {}, {"status": "FAIL"}, {"status": "PASS"}):
            with self.subTest(payload=payload), self.assertRaises(gate.ContractViolation):
                runner.strict_unified_summary(self.ev03, self.ev04, payload)

    def test_strict_summary_rejects_incomplete_d1a_reference(self) -> None:
        payload = d1a(); payload["aggregate_comparison"].pop("sha256")
        with self.assertRaises(gate.ContractViolation):
            runner.strict_unified_summary(self.ev03, self.ev04, payload)

    def test_strict_summary_rejects_malformed_ev_arms(self) -> None:
        for which in ("missing", "failed", "wrong_count", "reordered"):
            ev03 = copy.deepcopy(self.ev03)
            if which == "missing": ev03 = None
            elif which == "failed": ev03["status"] = "FAIL"
            elif which == "wrong_count": ev03["metrics"].pop()
            else: ev03["metrics"].reverse()
            with self.subTest(which=which), self.assertRaises(gate.ContractViolation):
                runner.strict_unified_summary(ev03, self.ev04, self.d1a)

    def manifest(self):
        binding = {"path": "x", "git_blob_sha1": "a" * 40, "canonical_git_blob_sha256": "b" * 64, "canonical_size_bytes": 1}
        provenance = {
            "status": "PASS", "execution_authorization_commit": "c" * 40,
            "authorization_baseline_commit": "d" * 40,
            "authorization_transition_proof": {"status": "PASS"},
            "authorization_commit_shape": {"status": "PASS", "mode": "DIRECT_PARENT_EXACT_FIVE_PATH_AUTHORIZATION_DIFF"},
            "current_dependency_bindings_equal_baseline": True,
            "authorization_flags": {key: "AUTHORIZED" for key in gate.AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")},
            "authorization_record_binding": binding,
            "authorized_artifact_bindings": {key: dict(binding) for key in gate.AUTHORIZATION_BASELINE_ARTIFACTS},
        }
        environment = {
            **{key: gate.TESTED_ENVIRONMENT[key] for key in ("python_version", "python_implementation", "architecture", "platform_system", "machine", "executable_sha256")},
            "packages": dict(gate.TESTED_ENVIRONMENT["required_packages"]),
            "distributions": dict(gate.TESTED_ENVIRONMENT["required_distributions"]),
            "project_imports": {"status": "PASS", "count": len(gate.project_local_import_closure(ROOT)), "modules": []},
        }
        return {"artifact_id": "m", "status": "PASS", "authorization_provenance": provenance, "environment_fingerprint": environment, "pipeline_steps": list(gate.PIPELINE_STEPS), "future_roots": list(gate.FUTURE_ROOTS), "results": {}}

    def test_manifest_round_trip_and_overwrite_guard(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "manifest.json"; payload = self.manifest()
            gate.write_manifest_new(path, payload)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), payload)
            with self.assertRaises(gate.ContractViolation): gate.write_manifest_new(path, payload)

    def test_manifest_rejects_nan_missing_key_order_and_v04_root(self) -> None:
        variants = []
        missing = self.manifest(); missing.pop("results"); variants.append(missing)
        reordered = self.manifest(); reordered["pipeline_steps"].reverse(); variants.append(reordered)
        old = self.manifest(); old["results"] = {"path": gate.V04_ROOTS[0]}; variants.append(old)
        nonfinite = self.manifest(); nonfinite["results"] = {"x": math.nan}; variants.append(nonfinite)
        incomplete = self.manifest(); incomplete["authorization_provenance"].pop("authorization_record_binding"); variants.append(incomplete)
        inconsistent = self.manifest(); inconsistent["authorization_provenance"]["authorization_flags"]["EV03_NUMERICAL_EXECUTION"] = "NOT_AUTHORIZED"; variants.append(inconsistent)
        for payload in variants:
            with self.assertRaises((gate.ContractViolation, ValueError)):
                gate.validate_manifest_payload(payload)

    def test_ledger_expected_and_producer_sets_are_independent_and_exact(self) -> None:
        bundle = gate.build_bundle(ROOT)
        expected, produced = set(bundle["ledger"]["expected_set"]), set(bundle["ledger"]["producer_set"])
        self.assertEqual(expected, produced)
        self.assertEqual(len(expected), 47)
        gate.validate_ledger_sets(expected, produced)

    def test_ledger_rejects_remove_add_failure_record_and_missing_bytes(self) -> None:
        expected = {"a"}; produced = {"a"}
        for changed in (set(), {"a", "b"}, {"execution_failed.json"}):
            with self.assertRaises(gate.ContractViolation): gate.validate_ledger_sets(expected, changed)
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(gate.ContractViolation): gate.validate_runtime_ledger(Path(folder), expected, produced)

    def test_ledger_detects_snapshot_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); path = root / "a"; path.write_text("x", encoding="utf-8")
            with self.assertRaises(gate.ContractViolation):
                gate.validate_runtime_ledger(root, {"a"}, {"a"}, snapshot={"a": "0" * 64})

    def operations(self):
        return {key: (lambda key=key: {"status": "PASS_EXACT" if key in {"verify_ev03", "verify_ev04"} else "PASS"}) for key in runner.OPERATION_KEYS}

    def test_nineteen_step_positive(self) -> None:
        result = runner.run_authorized_pipeline(self.operations())
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(len(result["steps"]), 19)

    def test_nineteen_step_rejects_missing_reordered_failed_and_early_final(self) -> None:
        missing = self.operations(); missing.pop("summary")
        reordered = self.operations(); value = reordered.pop("summary"); reordered = {"summary": value, **reordered}
        failed = self.operations(); failed["ev03_build"] = lambda: {"status": "FAIL"}
        early = self.operations(); early["ledger"] = lambda: {"status": "PASS"}; early["final_state"] = lambda: {"status": "FAIL"}
        for operations in (missing, reordered, failed, early):
            with self.assertRaises(gate.ContractViolation): runner.run_authorized_pipeline(operations)

    def test_current_authorized_preflight_fails_before_environment_or_side_effect(self) -> None:
        with self.assertRaises(gate.ContractViolation): runner.preflight_authorized(ROOT)
        self.assertFalse(any((ROOT / path).exists() for path in gate.FUTURE_ROOTS))


if __name__ == "__main__":
    unittest.main()
