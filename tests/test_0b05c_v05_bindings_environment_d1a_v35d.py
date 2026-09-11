from __future__ import annotations

import copy
import csv
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from src.experiments import prepare_0b05c_corrective_numerical_gate_v05 as gate
from src.experiments import run_d1a_corrective_0b05c_v05 as d1a


ROOT = Path(__file__).resolve().parents[1]
MINIMUM_CLOSURE = {
    "src/experiments/prepare_0b05c_corrective_numerical_gate_v01.py",
    "src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py",
    "src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py",
    "src/experiments/evaluate_normative_bm25_flat_data_aduanas_v02.py",
    "src/evaluation/metrics.py",
    "src/utils/paths.py",
}
BASELINE_METRICS = {
    "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json",
    "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json",
    "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json",
    "outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/run_metadata.json",
}


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def commit(root: Path, message: str) -> str:
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)
    subprocess.run(["git", "commit", "-qm", message], cwd=root, check=True)
    return git(root, "rev-parse", "HEAD")


def authorization_repo(extra_source_drift: bool = False) -> tuple[tempfile.TemporaryDirectory[str], Path, str, str]:
    folder = tempfile.TemporaryDirectory()
    root = Path(folder.name)
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.name", "test"], cwd=root, check=True)
    for path in gate.AUTHORIZATION_BASELINE_ARTIFACTS.values():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text('{"state":"closed"}\n', encoding="utf-8")
    source = root / "src/runtime.py"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text("VALUE = 1\n", encoding="utf-8")
    baseline = commit(root, "baseline")
    for path in gate.AUTHORIZATION_BASELINE_ARTIFACTS.values():
        (root / path).write_text('{"state":"authorized"}\n', encoding="utf-8")
    record = root / gate.AUTHORIZATION_RECORD
    record.write_text("{}\n", encoding="utf-8")
    if extra_source_drift:
        source.write_text("VALUE = 2\n", encoding="utf-8")
    authorization = commit(root, "authorization")
    return folder, root, baseline, authorization


def case_row(index: int) -> dict[str, object]:
    row: dict[str, object] = {
        "case_id": f"CASE-{index:04d}", "nandina_ref": "87044110",
        "original_rank_ref": 0, "corrected_rank_ref": 0,
        "ranking_changed": False, "rank_convention": "0=NOT_FOUND_AT_200",
    }
    for field in d1a.CASE_HIT_FIELDS:
        row[field] = 0
    for field in d1a.CASE_PATCH_FIELDS:
        row[field] = False if field.startswith("corrected_contains") else 0
    return row


def materialize_d1a(root: Path, spec: dict[str, object]) -> dict[str, Path]:
    paths = d1a.runner_output_paths(root, spec)
    for relative in spec["orchestration"]["hash_ledger_contract"]["included_paths"]:  # type: ignore[index]
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"x\n")
    aggregate = {
        "comparison_id": "d1a_corrective_vs_original_v0.5",
        "metrics": [
            {
                "metric": label, "original_numerator": index + 1,
                "corrected_numerator": index + 2, "denominator": 1056,
                "original_value": (index + 1) / 1056,
                "corrected_value": (index + 2) / 1056,
                "absolute_delta": 1 / 1056,
            }
            for index, (label, _) in enumerate(d1a.legacy.METRIC_SPECS)
        ],
    }
    paths["aggregate_comparison"].write_text(json.dumps(aggregate, allow_nan=True), encoding="utf-8")
    paths["case_level_comparison"].write_text(
        "".join(json.dumps(case_row(index), sort_keys=True) + "\n" for index in range(1056)), encoding="utf-8"
    )
    paths["execution_manifest"].write_text(json.dumps({
        "status": "PASS", "runner_version": "v0.5",
        "runner_outputs": spec["orchestration"]["runner_outputs"],  # type: ignore[index]
    }), encoding="utf-8")
    ledger_path = paths["hash_ledger"]
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    included = spec["orchestration"]["hash_ledger_contract"]["included_paths"]  # type: ignore[index]
    with ledger_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "sha256", "size_bytes"], lineterminator="\n")
        writer.writeheader()
        for relative in included:
            target = root / relative
            writer.writerow({"path": relative, "sha256": d1a.legacy.sha256_file(target), "size_bytes": target.stat().st_size})
    return paths


class BindingsEnvironmentD1aV35DTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = gate.build_bundle(ROOT)

    def test_authorization_commit_is_direct_child_with_exact_five_path_diff(self) -> None:
        folder, root, baseline, authorization = authorization_repo()
        with folder:
            result = gate.validate_authorization_commit_shape(root, baseline, authorization)
            self.assertEqual(result["mode"], "DIRECT_PARENT_EXACT_FIVE_PATH_AUTHORIZATION_DIFF")
            self.assertEqual(result["path_status"], gate.AUTHORIZATION_COMMIT_PATH_STATUS)
            bindings = [gate.git_binding(root, "src/runtime.py", baseline, "PROJECT_LOCAL_IMPORT_CLOSURE")]
            gate.validate_project_import_bindings(root, bindings, baseline, ("src/runtime.py",))
            gate.validate_project_import_bindings(root, bindings, authorization, ("src/runtime.py",))

    def test_actual_source_drift_in_authorization_commit_fails_closed(self) -> None:
        folder, root, baseline, authorization = authorization_repo(extra_source_drift=True)
        with folder:
            bindings = [gate.git_binding(root, "src/runtime.py", baseline, "PROJECT_LOCAL_IMPORT_CLOSURE")]
            with self.assertRaises(gate.ContractViolation):
                gate.validate_authorization_commit_shape(root, baseline, authorization)
            with self.assertRaises(gate.ContractViolation):
                gate.validate_project_import_bindings(root, bindings, authorization, ("src/runtime.py",))

    def test_non_direct_parent_authorization_fails_closed(self) -> None:
        folder, root, baseline, authorization = authorization_repo()
        with folder:
            extra = root / "unrelated"
            extra.write_text("x", encoding="utf-8")
            descendant = commit(root, "descendant")
            with self.assertRaises(gate.ContractViolation):
                gate.validate_authorization_commit_shape(root, baseline, descendant)

    def test_project_import_closure_is_exact_and_contains_audited_minimum(self) -> None:
        closure = set(gate.project_local_import_closure(ROOT))
        self.assertTrue(MINIMUM_CLOSURE <= closure)
        self.assertEqual(closure, set(self.bundle["gate"]["project_local_import_closure"]))
        bindings = [item for item in self.bundle["gate"]["candidate_source_bindings"] if item["classification"] == "PROJECT_LOCAL_IMPORT_CLOSURE"]
        gate.validate_project_import_bindings(ROOT, bindings, "INDEX")
        for missing in MINIMUM_CLOSURE:
            with self.subTest(missing=missing), self.assertRaises(gate.ContractViolation):
                gate.validate_project_import_bindings(ROOT, [item for item in bindings if item["path"] != missing], "INDEX")

    def test_new_project_import_not_bound_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "test"], cwd=root, check=True)
            (root / "src").mkdir()
            (root / "src/__init__.py").write_text("", encoding="utf-8")
            (root / "src/entry.py").write_text("import src.new_dependency\n", encoding="utf-8")
            (root / "src/new_dependency.py").write_text("VALUE = 1\n", encoding="utf-8")
            commit(root, "closure")
            paths = gate.project_local_import_closure(root, "HEAD", ("src/entry.py",))
            bindings = [gate.git_binding(root, path, "HEAD", "PROJECT_LOCAL_IMPORT_CLOSURE") for path in paths]
            incomplete = [item for item in bindings if item["path"] != "src/new_dependency.py"]
            with self.assertRaises(gate.ContractViolation):
                gate.validate_project_import_bindings(root, incomplete, "HEAD", ("src/entry.py",))

    def test_runtime_data_dependencies_include_all_baseline_metric_reads(self) -> None:
        self.assertTrue(BASELINE_METRICS <= set(gate.RUNTIME_DATA_DEPENDENCY_PATHS))
        bindings = self.bundle["gate"]["candidate_source_bindings"]
        self.assertEqual({item["path"] for item in bindings if item["classification"] == "VERSIONED_RUNTIME_DATA_DEPENDENCY"}, set(gate.RUNTIME_DATA_DEPENDENCY_PATHS))

    def test_d1a_strong_validation_positive(self) -> None:
        spec = copy.deepcopy(self.bundle["d1a"])
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            materialize_d1a(root, spec)
            result = d1a.d1a_summary_reference(root, spec, {"status": "PASS", "mode": "AUTHORIZED_EXECUTION"})
            self.assertEqual(set(result), {"status", "aggregate_comparison", "case_level_comparison", "execution_manifest", "hash_ledger"})

    def test_d1a_aggregate_missing_and_nan_fail_closed(self) -> None:
        for mutation in ("missing", "nan"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as folder:
                root = Path(folder); spec = copy.deepcopy(self.bundle["d1a"]); paths = materialize_d1a(root, spec)
                payload = json.loads(paths["aggregate_comparison"].read_text(encoding="utf-8"))
                if mutation == "missing": payload["metrics"].pop()
                else: payload["metrics"][0]["original_value"] = float("nan")
                paths["aggregate_comparison"].write_text(json.dumps(payload, allow_nan=True), encoding="utf-8")
                with self.assertRaises(gate.ContractViolation):
                    d1a.d1a_summary_reference(root, spec, {"status": "PASS", "mode": "AUTHORIZED_EXECUTION"})

    def test_d1a_case_duplicate_and_1055_fail_closed(self) -> None:
        for mutation in ("duplicate", "short"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as folder:
                root = Path(folder); spec = copy.deepcopy(self.bundle["d1a"]); paths = materialize_d1a(root, spec)
                rows = paths["case_level_comparison"].read_text(encoding="utf-8").splitlines()
                if mutation == "duplicate": rows[-1] = rows[0]
                else: rows.pop()
                paths["case_level_comparison"].write_text("\n".join(rows) + "\n", encoding="utf-8")
                with self.assertRaises(gate.ContractViolation):
                    d1a.d1a_summary_reference(root, spec, {"status": "PASS", "mode": "AUTHORIZED_EXECUTION"})

    def test_d1a_manifest_stale_output_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); spec = copy.deepcopy(self.bundle["d1a"]); paths = materialize_d1a(root, spec)
            payload = json.loads(paths["execution_manifest"].read_text(encoding="utf-8"))
            payload["runner_outputs"]["aggregate_comparison"] = "stale_v0.4.json"
            paths["execution_manifest"].write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaises(gate.ContractViolation):
                d1a.d1a_summary_reference(root, spec, {"status": "PASS", "mode": "AUTHORIZED_EXECUTION"})

    def test_d1a_ledger_missing_extra_and_bad_hash_fail_closed(self) -> None:
        for mutation in ("missing", "extra", "hash"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as folder:
                root = Path(folder); spec = copy.deepcopy(self.bundle["d1a"]); paths = materialize_d1a(root, spec)
                with paths["hash_ledger"].open(encoding="utf-8", newline="") as handle:
                    rows = list(csv.DictReader(handle))
                if mutation == "missing": rows.pop()
                elif mutation == "extra": rows.append({"path": "extra", "sha256": "0" * 64, "size_bytes": "1"})
                else: rows[0]["sha256"] = "0" * 64
                with paths["hash_ledger"].open("w", encoding="utf-8", newline="") as handle:
                    writer = csv.DictWriter(handle, fieldnames=["path", "sha256", "size_bytes"], lineterminator="\n")
                    writer.writeheader(); writer.writerows(rows)
                with self.assertRaises(gate.ContractViolation):
                    d1a.d1a_summary_reference(root, spec, {"status": "PASS", "mode": "AUTHORIZED_EXECUTION"})


if __name__ == "__main__":
    unittest.main()
