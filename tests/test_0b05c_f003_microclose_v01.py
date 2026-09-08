"""Focused fail-closed coverage for 0B-05C Gate F003."""

from __future__ import annotations

import copy
import csv
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable

from src.experiments.evaluate_normative_bm25_corrective_0b05c_v01 import (
    EV03_CANDIDATE_FIELDS,
    EV03_CASE_FIELDS,
    actual_ledger_paths,
    compare_control_reproduction,
    produce_aggregate_comparison,
    write_hash_ledger,
)
from src.experiments.prepare_0b05c_corrective_numerical_gate_v01 import (
    AUTHORIZATION_BASELINE_ARTIFACTS,
    ContractViolation,
    authorization_record_contract,
    load_authorization_transition_from_git,
    validate_authorization_transition,
)


ROOT = Path(__file__).resolve().parents[1]
TRANSITION_CONTRACT = {
    "allowed_transition": "NOT_AUTHORIZED -> AUTHORIZED",
    "allowed_authorization_fields": {
        "gate": [
            "EV03_NUMERICAL_EXECUTION",
            "EV04_NUMERICAL_EXECUTION",
            "D1A_NUMERICAL_EXECUTION",
            "UNIFIED_0B05C_NUMERICAL_EXECUTION",
        ],
        "arm_specs": ["EV03_NUMERICAL_EXECUTION", "EV04_NUMERICAL_EXECUTION"],
        "d1a_spec": ["D1A_NUMERICAL_EXECUTION"],
    },
}


def _snapshot() -> dict[str, Any]:
    return {
        "gate": {
            "authorization": {name: "NOT_AUTHORIZED" for name in TRANSITION_CONTRACT["allowed_authorization_fields"]["gate"]},
            "arms": {"EV03": {"specification_sha256": "ev03-closed"}, "EV04": {"specification_sha256": "ev04-closed"}},
            "corrective_execution_binding": {
                "orchestration_runner": {"path": "runner.py", "identity": "runner-frozen"},
                "corrective_builder": {"path": "builder.py", "identity": "builder-frozen"},
                "corrective_evaluator": {"path": "evaluator.py", "identity": "evaluator-frozen"},
            },
        },
        "specifications": {
            "EV03": {"authorization": {"EV03_NUMERICAL_EXECUTION": "NOT_AUTHORIZED"}, "schema": ["fixed"], "metric_contract": ["mrr"]},
            "EV04": {"authorization": {"EV04_NUMERICAL_EXECUTION": "NOT_AUTHORIZED"}, "schema": ["fixed"], "metric_contract": ["mrr_at_200"]},
        },
        "d1a_spec": {
            "authorization": {"D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED"},
            "model_policy": {"weights": {"path": "models/frozen.safetensors", "sha256": "frozen-model"}},
            "evaluation": {"metrics_to_compare": ["MRR@200"], "prospective_output_root": "outputs/d1a"},
        },
    }


def _authorized(snapshot: dict[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(snapshot)
    for name in TRANSITION_CONTRACT["allowed_authorization_fields"]["gate"]:
        candidate["gate"]["authorization"][name] = "AUTHORIZED"
    for arm in ("EV03", "EV04"):
        candidate["specifications"][arm]["authorization"][f"{arm}_NUMERICAL_EXECUTION"] = "AUTHORIZED"
        candidate["gate"]["arms"][arm]["specification_sha256"] = f"{arm.lower()}-authorized-derived"
    candidate["d1a_spec"]["authorization"]["D1A_NUMERICAL_EXECUTION"] = "AUTHORIZED"
    return candidate


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def _write_snapshot(root: Path, snapshot: dict[str, Any]) -> None:
    payloads = {
        AUTHORIZATION_BASELINE_ARTIFACTS["unified_gate"]: snapshot["gate"],
        AUTHORIZATION_BASELINE_ARTIFACTS["ev03_spec"]: snapshot["specifications"]["EV03"],
        AUTHORIZATION_BASELINE_ARTIFACTS["ev04_spec"]: snapshot["specifications"]["EV04"],
        AUTHORIZATION_BASELINE_ARTIFACTS["d1a_spec"]: snapshot["d1a_spec"],
    }
    for relative, payload in payloads.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _authorization_repo(mutate: Callable[[dict[str, Any]], None] | None = None, *, baseline_override: str | None = None) -> tempfile.TemporaryDirectory[str]:
    temporary = tempfile.TemporaryDirectory()
    root = Path(temporary.name)
    _git(root, "init")
    _git(root, "config", "user.name", "Codex")
    _git(root, "config", "user.email", "codex@example.invalid")
    _write_snapshot(root, _snapshot())
    _git(root, "add", ".")
    _git(root, "commit", "-m", "closed baseline")
    baseline_commit = _git(root, "rev-parse", "HEAD")
    candidate = _authorized(_snapshot())
    if mutate is not None:
        mutate(candidate)
    _write_snapshot(root, candidate)
    record_contract = authorization_record_contract()
    record = {
        "artifact_id": record_contract["artifact_id"],
        "schema_version": record_contract["schema_version"],
        "authorization_baseline_commit": baseline_override or baseline_commit,
        "baseline_artifacts": record_contract["baseline_artifacts"],
    }
    record_path = root / record_contract["record_path"]
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "authorized candidate")
    return temporary


def _write_csv(path: Path, fields: list[str], row: dict[str, str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerow(row)


class AuthorizationBaselineTests(unittest.TestCase):
    def test_authorization_transition_uses_proper_ancestor_git_baseline(self) -> None:
        with _authorization_repo() as directory:
            loaded = load_authorization_transition_from_git(Path(directory), authorization_record_contract())
            validate_authorization_transition(loaded["baseline"], loaded["candidate"], TRANSITION_CONTRACT, require_authorized=True)
            self.assertNotEqual(loaded["baseline_commit"], _git(Path(directory), "rev-parse", "HEAD"))

    def test_authorization_transition_rejects_runner_builder_and_evaluator_delta(self) -> None:
        mutations = {
            "runner": lambda candidate: candidate["gate"]["corrective_execution_binding"]["orchestration_runner"].update({"identity": "changed"}),
            "builder": lambda candidate: candidate["gate"]["corrective_execution_binding"]["corrective_builder"].update({"identity": "changed"}),
            "evaluator": lambda candidate: candidate["gate"]["corrective_execution_binding"]["corrective_evaluator"].update({"identity": "changed"}),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label), _authorization_repo(mutate) as directory:
                loaded = load_authorization_transition_from_git(Path(directory), authorization_record_contract())
                with self.assertRaisesRegex(ContractViolation, "immutable"):
                    validate_authorization_transition(loaded["baseline"], loaded["candidate"], TRANSITION_CONTRACT, require_authorized=True)

    def test_authorization_transition_rejects_d1a_model_path_and_metric_delta(self) -> None:
        mutations = {
            "model": lambda candidate: candidate["d1a_spec"]["model_policy"]["weights"].update({"sha256": "changed-model"}),
            "path": lambda candidate: candidate["d1a_spec"]["evaluation"].update({"prospective_output_root": "outputs/changed"}),
            "metric": lambda candidate: candidate["d1a_spec"]["evaluation"].update({"metrics_to_compare": ["Top@1"]}),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label), _authorization_repo(mutate) as directory:
                loaded = load_authorization_transition_from_git(Path(directory), authorization_record_contract())
                with self.assertRaisesRegex(ContractViolation, "immutable"):
                    validate_authorization_transition(loaded["baseline"], loaded["candidate"], TRANSITION_CONTRACT, require_authorized=True)

    def test_authorization_transition_rejects_nonexistent_baseline(self) -> None:
        with _authorization_repo(baseline_override="0" * 40) as directory:
            with self.assertRaisesRegex(ContractViolation, "proper ancestor"):
                load_authorization_transition_from_git(Path(directory), authorization_record_contract())


class Ev03SchemaTests(unittest.TestCase):
    def test_ev03_historical_headers_are_exact_and_reproduction_fixture_is_independent(self) -> None:
        frozen_ranking = ROOT / "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv"
        frozen_summary = ROOT / "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv"
        with frozen_ranking.open("r", encoding="utf-8-sig", newline="") as handle:
            self.assertEqual(next(csv.reader(handle)), EV03_CANDIDATE_FIELDS)
        with frozen_summary.open("r", encoding="utf-8-sig", newline="") as handle:
            self.assertEqual(next(csv.reader(handle)), EV03_CASE_FIELDS)
        expected_candidate = {field: f"candidate-{index}" for index, field in enumerate(EV03_CANDIDATE_FIELDS)}
        actual_candidate = {field: f"candidate-{index}" for index, field in enumerate(EV03_CANDIDATE_FIELDS)}
        expected_case = {field: f"case-{index}" for index, field in enumerate(EV03_CASE_FIELDS)}
        actual_case = {field: f"case-{index}" for index, field in enumerate(EV03_CASE_FIELDS)}
        metrics = {"metric_table": [{"metric": "mrr", "numerator": 1.0, "denominator": 1, "value": 1.0}]}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected_ranking, actual_ranking = root / "expected_ranking.csv", root / "actual_ranking.csv"
            expected_summary, actual_summary = root / "expected_summary.csv", root / "actual_summary.csv"
            _write_csv(expected_ranking, EV03_CANDIDATE_FIELDS, expected_candidate)
            _write_csv(actual_ranking, EV03_CANDIDATE_FIELDS, actual_candidate)
            _write_csv(expected_summary, EV03_CASE_FIELDS, expected_case)
            _write_csv(actual_summary, EV03_CASE_FIELDS, actual_case)
            result = compare_control_reproduction(
                expected_ranking, actual_ranking, expected_summary, actual_summary, metrics, dict(metrics),
                expected_candidate_schema=EV03_CANDIDATE_FIELDS, expected_case_schema=EV03_CASE_FIELDS,
            )
            self.assertEqual(
                {key: result[key] for key in ("ranking_schema_exact", "case_summary_schema_exact", "ranking_exact", "case_summary_exact", "metrics_exact")},
                {"ranking_schema_exact": True, "case_summary_schema_exact": True, "ranking_exact": True, "case_summary_exact": True, "metrics_exact": True},
            )
            for path, fields, row in (
                (expected_ranking, EV03_CANDIDATE_FIELDS[1:] + EV03_CANDIDATE_FIELDS[:1], expected_candidate),
                (actual_ranking, EV03_CANDIDATE_FIELDS[1:] + EV03_CANDIDATE_FIELDS[:1], actual_candidate),
                (expected_summary, EV03_CASE_FIELDS[1:] + EV03_CASE_FIELDS[:1], expected_case),
                (actual_summary, EV03_CASE_FIELDS[1:] + EV03_CASE_FIELDS[:1], actual_case),
            ):
                _write_csv(path, fields, row)
                with self.assertRaises(ContractViolation):
                    compare_control_reproduction(
                        expected_ranking, actual_ranking, expected_summary, actual_summary, metrics, dict(metrics),
                        expected_candidate_schema=EV03_CANDIDATE_FIELDS, expected_case_schema=EV03_CASE_FIELDS,
                    )
                _write_csv(expected_ranking, EV03_CANDIDATE_FIELDS, expected_candidate)
                _write_csv(actual_ranking, EV03_CANDIDATE_FIELDS, actual_candidate)
                _write_csv(expected_summary, EV03_CASE_FIELDS, expected_case)
                _write_csv(actual_summary, EV03_CASE_FIELDS, actual_case)


class LedgerAndAggregateTests(unittest.TestCase):
    def test_filesystem_discovered_ledger_rejects_missing_unexpected_self_and_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runtime = root / "runtime"
            runtime.mkdir()
            (runtime / "a.json").write_text("a\n", encoding="utf-8", newline="\n")
            contract = {
                "expected_paths": ["runtime/a.json", "runtime/b.json"],
                "discovery_roots": [{"path": "runtime", "kind": "DIRECTORY"}],
                "excluded_self_path": "runtime/ledger.json",
            }
            with self.assertRaisesRegex(ContractViolation, "exact contract"):
                write_hash_ledger(runtime / "ledger.json", contract, root=root)
            (runtime / "b.json").write_text("b\n", encoding="utf-8", newline="\n")
            self.assertEqual(actual_ledger_paths(contract, root=root), ["runtime/a.json", "runtime/b.json"])
            (runtime / "unexpected.json").write_text("x\n", encoding="utf-8", newline="\n")
            with self.assertRaisesRegex(ContractViolation, "exact contract"):
                write_hash_ledger(runtime / "ledger.json", contract, root=root)
            (runtime / "unexpected.json").unlink()
            (runtime / "nested").mkdir()
            (runtime / "nested/unexpected.json").write_text("x\n", encoding="utf-8", newline="\n")
            with self.assertRaisesRegex(ContractViolation, "exact contract"):
                write_hash_ledger(runtime / "ledger.json", contract, root=root)
            (runtime / "nested/unexpected.json").unlink()
            (runtime / "nested").rmdir()
            (runtime / "ledger.json").write_text("old\n", encoding="utf-8", newline="\n")
            with self.assertRaisesRegex(ContractViolation, "Only the ledger"):
                write_hash_ledger(runtime / "ledger.json", contract, root=root)
            duplicate = {**contract, "expected_paths": ["runtime/a.json", "runtime/a.json"]}
            with self.assertRaisesRegex(ContractViolation, "duplicate"):
                write_hash_ledger(runtime / "ledger.json", duplicate, root=root)

    def test_aggregate_comparison_uses_metric_table_numerators_denominators_and_values(self) -> None:
        original = {"metric_table": [{"metric": "top_1", "numerator": 2, "denominator": 10, "value": 0.2}]}
        corrective = {"metric_table": [{"metric": "top_1", "numerator": 3, "denominator": 10, "value": 0.3}]}
        comparison = produce_aggregate_comparison(original, corrective)
        self.assertEqual(
            comparison,
            [{"metric": "top_1", "original_numerator": 2, "corrected_numerator": 3, "denominator": 10, "original_value": 0.2, "corrected_value": 0.3, "absolute_delta": 0.09999999999999998}],
        )
        mismatch = {"metric_table": [{"metric": "top_1", "numerator": 3, "denominator": 11, "value": 3 / 11}]}
        with self.assertRaisesRegex(ContractViolation, "denominator mismatch"):
            produce_aggregate_comparison(original, mismatch)


if __name__ == "__main__":
    unittest.main()
