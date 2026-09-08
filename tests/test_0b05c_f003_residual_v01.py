"""Focused fail-closed coverage for residual 0B-05C Gate F003 findings."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src.experiments import prepare_0b05c_corrective_numerical_gate_v01 as gate
from src.experiments.evaluate_normative_bm25_corrective_0b05c_v01 import (
    produce_case_level_comparison,
    produce_unified_sensitivity_summary,
)
from src.experiments.run_0b05c_corrective_numerical_v01 import (
    _d1a_summary_reference,
    run_authorized_pipeline,
)


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _candidate(case_id: str, rank: int, code: str) -> dict[str, str]:
    return {"case_id": case_id, "candidate_rank": str(rank), "candidate_code": code}


def _summary(case_id: str = "case-1", nandina_ref: str = "11111111") -> dict[str, str]:
    return {"case_id": case_id, "nandina_ref": nandina_ref, "rank_ref": "1"}


class AuthorizedStaticBindingTests(unittest.TestCase):
    def _fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path, dict, dict, dict]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        _git(root, "init")
        _git(root, "config", "user.name", "Codex")
        _git(root, "config", "user.email", "codex@example.invalid")
        files = {
            "historical_runner.py": "historical runner\n",
            "config.json": "{\"version\": 1}\n",
            "corpus.jsonl": "{\"codigo\": \"11111111\"}\n",
            "eval.csv": "case_id,nandina_ref\ncase-1,11111111\n",
            "runner.py": "runner\n",
            "builder.py": "builder\n",
            "evaluator.py": "evaluator\n",
            "src/retrieval/bm25.py": "bm25\n",
            "src/evaluation/metrics.py": "metrics\n",
            "outputs/original_results.csv": "case_id,candidate_rank,candidate_code\ncase-1,1,11111111\n",
            "outputs/original_summary.csv": "case_id,nandina_ref,rank_ref\ncase-1,11111111,1\n",
        }
        for relative, contents in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(contents, encoding="utf-8", newline="\n")
        metadata = {
            "outputs": {"results": "outputs/original_results.csv", "summary": "outputs/original_summary.csv"},
            "output_sha256": {
                "results": _sha(root / "outputs/original_results.csv"),
                "summary": _sha(root / "outputs/original_summary.csv"),
            },
        }
        for arm_name in ("EV03", "EV04"):
            path = root / f"metadata_{arm_name.lower()}.json"
            path.write_text(json.dumps(metadata, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
        _git(root, "add", ".")
        _git(root, "commit", "-m", "baseline")
        identities = {relative: gate.head_text_identity(root, relative) for relative in files}
        arms = {
            name: {
                "runner": "historical_runner.py", "corpus": "corpus.jsonl", "metadata": f"metadata_{name.lower()}.json",
                "results_key": "results", "summary_key": "summary", "config_path": "config.json", "eval_path": "eval.csv",
            }
            for name in ("EV03", "EV04")
        }
        specs = {}
        for name, arm in arms.items():
            metadata_path = root / arm["metadata"]
            specs[name] = {
                "frozen_inputs": {key: identities[path] for key, path in {
                    "runner": "historical_runner.py", "config": "config.json", "corpus": "corpus.jsonl", "eval": "eval.csv",
                }.items()},
                "primary_original_control": {
                    "run_metadata": {**gate.head_text_identity(root, arm["metadata"]), "artifact_sha256": _sha(metadata_path)},
                    "outputs": {key: {"path": relative, "sha256": digest} for key, relative, digest in (
                        ("results", metadata["outputs"]["results"], metadata["output_sha256"]["results"]),
                        ("summary", metadata["outputs"]["summary"], metadata["output_sha256"]["summary"]),
                    )},
                },
            }
        dependency_paths = ("runner.py", "builder.py", "evaluator.py", "historical_runner.py", "src/retrieval/bm25.py", "src/evaluation/metrics.py")
        frozen_dependencies = {path: identities[path] for path in dependency_paths}
        payload = {"corrective_execution_binding": {
            "frozen_dependencies": frozen_dependencies,
            "orchestration_runner": frozen_dependencies["runner.py"],
            "corrective_builder": frozen_dependencies["builder.py"],
            "corrective_evaluator": frozen_dependencies["evaluator.py"],
        }}
        (root / "authorization_artifacts.json").write_text("{\"intact\": true}\n", encoding="utf-8", newline="\n")
        _git(root, "add", ".")
        _git(root, "commit", "-m", "authorization artifacts")
        return temporary, root, payload, specs, {"arms": arms, "paths": dependency_paths}

    def test_each_persisted_static_referent_rejects_a_later_git_change(self) -> None:
        mutations = {
            "corpus": "corpus.jsonl",
            "config": "config.json",
            "eval": "eval.csv",
            "bm25": "src/retrieval/bm25.py",
            "metrics": "src/evaluation/metrics.py",
            "historical_helper": "historical_runner.py",
        }
        for label, relative in mutations.items():
            with self.subTest(label=label):
                temporary, root, payload, specs, fixture = self._fixture()
                with temporary:
                    path = root / relative
                    path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8", newline="\n")
                    _git(root, "add", relative)
                    _git(root, "commit", "-m", f"mutate {label}")
                    with self.assertRaises(gate.ContractViolation):
                        gate.validate_authorized_static_bindings(
                            root, payload, specs, arms=fixture["arms"], frozen_dependency_paths=fixture["paths"],
                            execution_roles={"orchestration_runner": "runner.py", "corrective_builder": "builder.py", "corrective_evaluator": "evaluator.py"},
                            run_metadata_validator=lambda _root, _arm: json.loads((root / _arm["metadata"]).read_text(encoding="utf-8")),
                            overlap_validator=lambda *_args: None,
                        )

    def test_static_binding_passes_when_authorization_artifacts_are_unchanged(self) -> None:
        temporary, root, payload, specs, fixture = self._fixture()
        with temporary:
            result = gate.validate_authorized_static_bindings(
                root, payload, specs, arms=fixture["arms"], frozen_dependency_paths=fixture["paths"],
                execution_roles={"orchestration_runner": "runner.py", "corrective_builder": "builder.py", "corrective_evaluator": "evaluator.py"},
                run_metadata_validator=lambda _root, _arm: json.loads((root / _arm["metadata"]).read_text(encoding="utf-8")),
                overlap_validator=lambda *_args: None,
            )
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["frozen_dependency_count"], len(fixture["paths"]))


class D1aPreflightOrderingTests(unittest.TestCase):
    def test_read_only_d1a_preflight_passes_without_execution(self) -> None:
        calls: list[str] = []

        def read_only(_root: Path) -> dict[str, object]:
            calls.append("d1a")
            return {
                "status": "PASS", "mode": "PREFLIGHT_ONLY", "numerical_execution_occurred": False,
                "retrieval_executed": False, "corrected_corpus_created": False,
                "corrected_index_created": False, "new_metrics_computed": False,
            }

        self.assertEqual(gate.validate_d1a_read_only_preflight(Path("."), preflight_callable=read_only)["status"], "PASS")
        self.assertEqual(calls, ["d1a"])

    def test_failed_d1a_preflight_prevents_all_later_pipeline_operations(self) -> None:
        calls: list[str] = []

        def failed_preflight() -> dict[str, str]:
            calls.append("authorized_preflight")
            raise gate.ContractViolation("D1a preflight FAIL")

        names = (
            "ev03_control", "verify_ev03", "ev03_materialize", "ev03_build", "ev03_evaluate", "ev04_control", "verify_ev04",
            "ev04_materialize", "ev04_build", "ev04_evaluate", "d1a_execute", "integrity", "case_comparisons", "aggregate_comparisons",
            "summary", "manifest", "ledger", "final_state",
        )
        operations = {"authorized_preflight": failed_preflight}
        operations.update({name: (lambda name=name: calls.append(name) or {"status": "PASS"}) for name in names})
        with self.assertRaisesRegex(gate.ContractViolation, "D1a preflight FAIL"):
            run_authorized_pipeline(operations)
        self.assertEqual(calls, ["authorized_preflight"])

    def test_gate_authorized_preflight_calls_d1a_before_root_check(self) -> None:
        actual_gate = {"authorization_transition_contract": {"authorization_record": {}}, "authorization": {"corrective_retrieval_executed": False, "corrective_metrics_computed": False}}
        transition = {"baseline": {}, "candidate": {"gate": actual_gate, "specifications": {}, "d1a_spec": {}}, "baseline_commit": "a" * 40, "record": {"baseline_artifacts": gate.AUTHORIZATION_BASELINE_ARTIFACTS}}
        calls: list[str] = []
        with mock.patch.object(gate, "git_revision_blob", return_value="blob"), \
             mock.patch.object(gate, "integrated_base_is_ancestor", return_value=True), \
             mock.patch.object(gate, "_read_head_json", return_value=actual_gate), \
             mock.patch.object(gate, "load_authorization_transition_from_git", return_value=transition), \
             mock.patch.object(gate, "validate_authorization_transition"), \
             mock.patch.object(gate, "validate_authorized_static_bindings", return_value={"status": "PASS"}), \
             mock.patch.object(gate, "validate_d1a_reference", return_value={"spec": {}, "D1A_NUMERICAL_EXECUTION": "AUTHORIZED"}), \
             mock.patch.object(gate, "validate_d1a_read_only_preflight", side_effect=gate.ContractViolation("D1a missing")) as d1a, \
             mock.patch.object(gate, "require_absent") as roots:
            with self.assertRaisesRegex(gate.ContractViolation, "D1a missing"):
                gate.preflight_authorized(Path("."))
        self.assertTrue(d1a.called)
        roots.assert_not_called()


class CaseLevelComparisonTests(unittest.TestCase):
    def test_full_effective_sequence_and_affected_code_ranks_are_frozen(self) -> None:
        original_cases, corrected_cases = [_summary()], [_summary()]
        original = [_candidate("case-1", 1, "11111111"), _candidate("case-1", 2, "87044110"), _candidate("case-1", 3, "87045110")]
        rows = produce_case_level_comparison("EV03", original_cases, corrected_cases, original, list(original))
        row = rows[0]
        self.assertFalse(row["ranking_changed"])
        self.assertEqual((row["original_rank_87044110"], row["original_rank_87045110"]), (2, 3))
        self.assertTrue(row["original_contains_87044110"])
        self.assertTrue(row["original_contains_87045110"])
        self.assertEqual(len(row), len(gate.case_level_comparison_contract("EV03")["field_order"]))

    def test_irrelevant_rank_change_and_missing_affected_code_are_observable(self) -> None:
        original = [_candidate("case-1", 1, "11111111"), _candidate("case-1", 2, "87044110"), _candidate("case-1", 3, "99999999")]
        corrected = [_candidate("case-1", 1, "11111111"), _candidate("case-1", 2, "99999999"), _candidate("case-1", 3, "87044110")]
        row = produce_case_level_comparison("EV04", [_summary()], [_summary()], original, corrected)[0]
        self.assertTrue(row["ranking_changed"])
        self.assertEqual(row["original_rank_ref"], row["corrected_rank_ref"])
        self.assertEqual(row["original_rank_87045110"], 0)
        self.assertFalse(row["original_contains_87045110"])

    def test_case_id_mismatch_duplicate_and_missing_ranking_are_fail_closed(self) -> None:
        candidates = [_candidate("case-1", 1, "11111111")]
        with self.assertRaises(gate.ContractViolation):
            produce_case_level_comparison("EV03", [_summary()], [_summary("case-2")], candidates, candidates)
        with self.assertRaises(gate.ContractViolation):
            produce_case_level_comparison("EV03", [_summary(), _summary()], [_summary()], candidates, candidates)
        with self.assertRaises(gate.ContractViolation):
            produce_case_level_comparison("EV03", [_summary()], [_summary()], [], candidates)


class UnifiedSummaryTests(unittest.TestCase):
    def test_unified_summary_requires_and_records_d1a(self) -> None:
        summary = produce_unified_sensitivity_summary({"status": "PASS"}, {"status": "PASS"}, {"status": "PASS"})
        self.assertEqual(list(summary["arms"]), ["EV03", "EV04", "D1a"])
        self.assertEqual(summary["interpretation_status"], "AUTHORIZED_EXECUTION_COMPLETED_PENDING_INTERPRETATION")
        with self.assertRaises(gate.ContractViolation):
            produce_unified_sensitivity_summary({"status": "PASS"}, {"status": "PASS"}, {})

    def test_d1a_summary_is_referenced_from_existing_contractual_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            outputs = {
                "aggregate_comparison": "out/aggregate.json", "case_level_comparison": "out/cases.jsonl", "execution_manifest": "out/manifest.json",
            }
            for key, relative in outputs.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('{"status": "PASS"}\n' if key == "execution_manifest" else "contractual\n", encoding="utf-8", newline="\n")
            reference = _d1a_summary_reference(root, {"orchestration": {"runner_outputs": outputs}}, {"status": "PASS"})
            self.assertEqual(reference["status"], "PASS")
            self.assertEqual(reference["integrity_status"], "PASS")


if __name__ == "__main__":
    unittest.main()
