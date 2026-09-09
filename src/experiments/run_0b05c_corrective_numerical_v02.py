"""Fail-closed unified runner for a future authorized 0B-05C v0.2 run."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import subprocess
from pathlib import Path
from typing import Any, Callable, Mapping

from .prepare_0b05c_corrective_numerical_gate_v02 import (
    AUTHORIZATION,
    AUTHORIZATION_BASELINE_ARTIFACTS,
    AUTHORIZATION_RECORD,
    AUTHORIZED_GATE_STATUS,
    AUTHORIZED_READINESS,
    ContractViolation,
    FUTURE_ROOTS,
    GATE_PATH,
    PIPELINE_STEPS,
    ROOT,
    git_binding,
    load_authorization_transition_from_git,
    preflight as gate_preflight,
    read_json,
    require,
)


OPERATION_KEYS = (
    "unified_preflight", "ev03_control", "verify_ev03", "ev03_materialize", "ev03_build", "ev03_evaluate",
    "ev04_control", "verify_ev04", "ev04_materialize", "ev04_build", "ev04_evaluate", "d1a_execute",
    "integrity", "case_comparisons", "aggregate_comparisons", "summary", "manifest", "ledger", "final_state",
)


def preflight(root: Path = ROOT) -> dict[str, Any]:
    return gate_preflight(root)


def validate_dependency_bindings(root: Path, bindings: list[Mapping[str, Any]], *, revision: str = "HEAD") -> None:
    for binding in bindings:
        if binding["classification"] == "FROZEN_FILE_IDENTITY":
            path = root / str(binding["path"])
            require(path.is_file(), f"Frozen file is missing: {binding['path']}")
            require(path.stat().st_size == binding["size_bytes"], f"Frozen file size mismatch: {binding['path']}")
            require(hashlib.sha256(path.read_bytes()).hexdigest() == binding["sha256"], f"Frozen file SHA mismatch: {binding['path']}")
        else:
            require(git_binding(root, str(binding["path"]), revision, str(binding["classification"])) == binding, f"Canonical binding mismatch: {binding['path']}")


def preflight_authorized(root: Path = ROOT) -> dict[str, Any]:
    gate = read_json(root, GATE_PATH)
    require(subprocess.run(["git", "status", "--short", "--untracked-files=no"], cwd=root, check=True, capture_output=True, text=True).stdout.strip() == "", "Tracked working tree is not clean")
    require(gate.get("gate_status") == AUTHORIZED_GATE_STATUS, "Authorized gate is not approved and integrated")
    require(gate.get("authorization_readiness") == AUTHORIZED_READINESS, "Authorized gate readiness is invalid")
    required = {key: "AUTHORIZED" for key in AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")}
    current = {key: gate["authorization"].get(key) for key in required}
    require(current == required, "All four 0B-05C v0.2 numerical components must be AUTHORIZED before any side effect")
    require(gate["authorization"].get("authorization_record_present") is True, "Authorization record state is not present")
    require((root / AUTHORIZATION_RECORD).is_file(), "Authorization record v0.2 is required")
    transition = load_authorization_transition_from_git(root, gate)
    require(gate["authorization"].get("corrective_retrieval_executed") is False, "Corrective retrieval was already executed")
    require(gate["authorization"].get("corrective_metrics_computed") is False, "Corrective metrics were already computed")
    for relative in FUTURE_ROOTS:
        require(not (root / relative).exists(), f"Prospective v0.2 root already exists: {relative}")
    validate_dependency_bindings(root, gate["dependency_bindings"])
    candidate = transition["candidate"]
    authorization_commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True).stdout.strip()
    authorization_record_binding = git_binding(root, AUTHORIZATION_RECORD.as_posix(), "HEAD")
    authorized_artifact_bindings = {
        key: git_binding(root, path, "HEAD")
        for key, path in AUTHORIZATION_BASELINE_ARTIFACTS.items()
    }
    return {
        "status": "PASS",
        "mode": "AUTHORIZED_PREFLIGHT_ONLY",
        "numerical_execution_occurred": False,
        "authorization": current,
        "authorization_baseline_commit": transition["baseline_commit"],
        "authorization_record": transition["record"],
        "authorization_record_binding": authorization_record_binding,
        "execution_authorization_commit": authorization_commit,
        "baseline_external_audit": transition["record"]["baseline_external_audit"],
        "authorized_artifact_bindings": authorized_artifact_bindings,
        "bundle": {
            "gate": gate,
            "EV03": candidate["EV03"],
            "EV04": candidate["EV04"],
            "d1a": candidate["D1a"],
        },
    }


def _require_exact(result: Mapping[str, Any], label: str) -> Mapping[str, Any]:
    require(result.get("status") == "PASS_EXACT", f"{label} must be PASS_EXACT")
    return result


def run_authorized_pipeline(operations: Mapping[str, Callable[[], Mapping[str, Any]]]) -> dict[str, Any]:
    require(tuple(operations) == OPERATION_KEYS, "Operation contract does not match the frozen 19-step order")
    state: dict[str, Mapping[str, Any]] = {}
    for index, (step, key) in enumerate(zip(PIPELINE_STEPS, OPERATION_KEYS, strict=True)):
        result = operations[key]()
        if key in {"verify_ev03", "verify_ev04"}:
            result = _require_exact(result, key)
        elif key == "final_state":
            require(len(state) == 18, "Final state cannot pass before the first 18 steps")
            require(result.get("status") == "PASS", "Final completion state did not PASS")
        else:
            require(result.get("status") in {"PASS", "PASS_EXACT"}, f"Pipeline stopped at {step}")
        state[step] = result
        require(len(state) == index + 1, "Pipeline order drift")
    return {"status": "PASS", "execution_order": list(PIPELINE_STEPS), "steps": state}


def _write_json_new(path: Path, payload: Mapping[str, Any]) -> dict[str, Any]:
    require(not path.exists(), f"Runner refuses overwrite or resume: {path.as_posix()}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return dict(payload)


def build_runtime_authorization_provenance(proof: Mapping[str, Any]) -> dict[str, Any]:
    required_authorization = {key: "AUTHORIZED" for key in AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")}
    require(proof.get("status") == "PASS" and proof.get("mode") == "AUTHORIZED_PREFLIGHT_ONLY", "Runtime authorization proof is invalid")
    require(proof.get("authorization") == required_authorization, "Runtime authorization proof lacks four authorized states")
    authorization_commit = proof.get("execution_authorization_commit")
    baseline_commit = proof.get("authorization_baseline_commit")
    require(isinstance(authorization_commit, str) and len(authorization_commit) == 40, "Execution authorization commit is missing")
    require(isinstance(baseline_commit, str) and len(baseline_commit) == 40, "Authorization baseline commit is missing")
    record = proof.get("authorization_record")
    binding = proof.get("authorization_record_binding")
    require(isinstance(record, Mapping), "Authorization record proof is missing")
    require(record.get("authorization_baseline_commit") == baseline_commit, "Authorization record baseline mismatch")
    require(isinstance(binding, Mapping) and binding.get("path") == AUTHORIZATION_RECORD.as_posix(), "Authorization record binding is missing")
    require(all(binding.get(key) is not None for key in ("git_blob_sha1", "canonical_git_blob_sha256", "canonical_size_bytes")), "Authorization record binding is incomplete")
    authorized_artifacts = proof.get("authorized_artifact_bindings")
    require(isinstance(authorized_artifacts, Mapping) and set(authorized_artifacts) == set(AUTHORIZATION_BASELINE_ARTIFACTS), "Authorized artifact bindings are incomplete")
    require(proof.get("baseline_external_audit") == "PASS / APPROVED_FOR_INTEGRATION", "Authorization baseline external audit is invalid")
    return {
        "status": "PASS",
        "mode": "AUTHORIZED_PREFLIGHT_ONLY",
        "execution_authorization_commit": authorization_commit,
        "authorization_baseline_commit": baseline_commit,
        "authorization": dict(required_authorization),
        "authorization_record": {
            "path": binding["path"],
            "git_blob_sha1": binding["git_blob_sha1"],
            "canonical_git_blob_sha256": binding["canonical_git_blob_sha256"],
            "canonical_size_bytes": binding["canonical_size_bytes"],
        },
        "baseline_external_audit": proof["baseline_external_audit"],
        "authorized_artifacts": {key: dict(value) for key, value in authorized_artifacts.items()},
    }


def file_reference(root: Path, path: Path) -> dict[str, Any]:
    require(path.is_file(), f"Runtime provenance file is missing: {path}")
    return {"path": path.relative_to(root).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "size_bytes": path.stat().st_size}


def build_execution_manifest_payload(
    root: Path,
    runtime_authorization_record: Path,
    proof: Mapping[str, Any],
    control: Mapping[str, Any],
    corrected: Mapping[str, Any],
    d1a_result: Mapping[str, Any],
) -> dict[str, Any]:
    provenance = build_runtime_authorization_provenance(proof)
    return {
        "status": "PASS",
        "execution_order": list(PIPELINE_STEPS),
        "execution_authorization_commit": provenance["execution_authorization_commit"],
        "authorization_baseline_commit": provenance["authorization_baseline_commit"],
        "runtime_authorization_record": file_reference(root, runtime_authorization_record),
        "control_reproductions": dict(control),
        "corrected_arms": dict(corrected),
        "d1a": dict(d1a_result),
    }


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_control_exact(
    arm: str,
    required: Mapping[str, Any],
    comparison: Mapping[str, Any],
    ranking_path: Path,
    summary_path: Path,
    expected_metrics: Mapping[str, Any],
    actual_metrics: Mapping[str, Any],
    *,
    logical_index_identity: str | None = None,
) -> dict[str, Any]:
    checks = {
        "ranking_schema_exact": comparison.get("ranking_schema_exact") is True,
        "case_summary_schema_exact": comparison.get("case_summary_schema_exact") is True,
        "ranking_rows_content_exact": comparison.get("ranking_exact") is True,
        "case_summary_rows_content_exact": comparison.get("case_summary_exact") is True,
        "metric_table_exact": comparison.get("metrics_exact") is True,
        "full_metrics_exact": expected_metrics == actual_metrics,
        "ranking_sha256_exact": hashlib.sha256(ranking_path.read_bytes()).hexdigest() == required.get("ranking_sha256"),
        "case_summary_sha256_exact": hashlib.sha256(summary_path.read_bytes()).hexdigest() == required.get("case_summary_sha256"),
    }
    if "ranking_rows" in required:
        checks["ranking_row_count_exact"] = len(_read_csv(ranking_path)) == int(required["ranking_rows"])
    if "cases" in required:
        checks["case_summary_row_count_exact"] = len(_read_csv(summary_path)) == int(required["cases"])
    if arm == "EV03":
        checks["logical_index_identity_exact"] = logical_index_identity == "EXACT"
    require(all(checks.values()), f"{arm} full PASS_EXACT contract failed")
    return {**dict(comparison), "status": "PASS_EXACT", "checks": checks, "required_contract": dict(required)}


def _contractual_runtime_files(root: Path, contract: Mapping[str, Any]) -> list[Path]:
    excluded = root / str(contract["excluded_self_path"])
    files: set[Path] = set()
    for relative in contract["discovery_roots"]:
        path = root / str(relative)
        if path.is_file():
            files.add(path)
        elif path.is_dir():
            files.update(item for item in path.rglob("*") if item.is_file())
    files.discard(excluded)
    return sorted(files)


def validate_runtime_ledger_contract(root: Path, contract: Mapping[str, Any]) -> list[dict[str, Any]]:
    expected = {str(item) for item in contract["expected_paths"]}
    observed_files = _contractual_runtime_files(root, contract)
    observed = {path.relative_to(root).as_posix() for path in observed_files}
    missing = sorted(expected - observed)
    unexpected = sorted(observed - expected)
    require(not missing, f"Runtime ledger is missing contractual outputs: {missing}")
    require(not unexpected, f"Runtime ledger found unexpected contractual outputs: {unexpected}")
    return [
        {"path": path.relative_to(root).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "size_bytes": path.stat().st_size}
        for path in observed_files
    ]


def _d1a_summary_reference(root: Path, spec: Mapping[str, Any], result: Mapping[str, Any]) -> dict[str, Any]:
    require(result.get("status") == "PASS", "D1a execution did not PASS")
    outputs = spec.get("orchestration", {}).get("runner_outputs")
    require(isinstance(outputs, Mapping), "D1a runner output contract is malformed")
    required = ("aggregate_comparison", "case_level_comparison", "execution_manifest", "hash_ledger")
    references: dict[str, dict[str, Any]] = {}
    for key in required:
        relative = outputs.get(key)
        require(isinstance(relative, str) and relative, f"D1a runner output contract is missing: {key}")
        path = root / relative
        require(path.is_file(), f"D1a contractual output is missing: {relative}")
        references[key] = {"path": relative, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "size_bytes": path.stat().st_size}
    aggregate = json.loads((root / references["aggregate_comparison"]["path"]).read_text(encoding="utf-8"))
    metrics = aggregate.get("metrics")
    expected_metrics = spec.get("orchestration", {}).get("comparison_contract", {}).get("aggregate_metrics")
    require(isinstance(expected_metrics, list) and len(expected_metrics) == 17, "D1a aggregate metric contract is malformed")
    require(isinstance(metrics, list) and len(metrics) == len(expected_metrics), "D1a aggregate comparison metric count is invalid")
    names = [row.get("metric") if isinstance(row, Mapping) else None for row in metrics]
    require(names == expected_metrics and len(set(names)) == len(names), "D1a aggregate metric names or order changed")
    row_fields = {"metric", "original_numerator", "corrected_numerator", "denominator", "original_value", "corrected_value", "absolute_delta"}
    numeric_fields = row_fields - {"metric"}
    for row in metrics:
        require(isinstance(row, Mapping) and row_fields <= set(row), "D1a aggregate metric row schema is incomplete")
        require(
            all(isinstance(row[field], (int, float)) and not isinstance(row[field], bool) and math.isfinite(float(row[field])) for field in numeric_fields),
            "D1a aggregate metric row contains a non-numeric value",
        )
    manifest = json.loads((root / references["execution_manifest"]["path"]).read_text(encoding="utf-8"))
    require(manifest.get("status") == "PASS", "D1a execution manifest did not PASS")
    require(references["case_level_comparison"]["size_bytes"] > 0, "D1a case-level comparison is empty")
    require(references["hash_ledger"]["size_bytes"] > 0, "D1a hash ledger is empty")
    return {"status": "PASS", "aggregate_comparison": references["aggregate_comparison"], "case_level_comparison": references["case_level_comparison"], "execution_manifest": references["execution_manifest"], "hash_ledger": references["hash_ledger"]}


def build_unified_summary(ev03: Mapping[str, Any], ev04: Mapping[str, Any], d1a: Mapping[str, Any]) -> dict[str, Any]:
    require(d1a.get("status") == "PASS", "D1a aggregate evidence is missing before unified summary")
    require(isinstance(d1a.get("aggregate_comparison"), Mapping), "D1a aggregate comparison is not incorporated")
    return {"status": "PASS", "EV03": dict(ev03), "EV04": dict(ev04), "D1a": dict(d1a)}


def _arm_paths(root: Path, arm: str, spec: Mapping[str, Any]) -> dict[str, Path]:
    execution = spec["prospective_execution"]
    names = ("normative_flat_results.csv", "normative_flat_case_summary.csv") if arm == "EV03" else ("normative_hierarchical_results.csv", "normative_hierarchical_case_summary.csv")
    return {
        "control_index": root / execution["control_reproduction_index_root"] / "index.pkl",
        "control_metadata": root / execution["control_reproduction_index_root"] / "index_metadata.json",
        "control_output": root / execution["control_reproduction_output_root"],
        "corrected_corpus": root / spec["corrective_corpus"]["prospective_path"],
        "corrected_index": root / execution["corrected_index_root"] / "index.pkl",
        "corrected_metadata": root / execution["corrected_index_root"] / "index_metadata.json",
        "corrected_output": root / execution["corrected_output_root"],
        "ranking_name": Path(names[0]),
        "summary_name": Path(names[1]),
    }


def _default_operations(root: Path, proof: Mapping[str, Any]) -> dict[str, Callable[[], Mapping[str, Any]]]:
    from . import build_bm25_corrective_0b05c_v02 as builder
    from . import evaluate_normative_bm25_corrective_0b05c_v01 as evaluator
    from . import prepare_0b05c_corrective_numerical_gate_v01 as v01_gate
    from . import run_d1a_corrective_0b05c_v02 as d1a_runner
    from . import verify_ev03_historical_builder_recovery_v02 as ev03_recovery
    from ..retrieval.bm25 import load_bm25_index

    specs = {name: proof["bundle"][name] for name in ("EV03", "EV04")}
    paths = {name: _arm_paths(root, name, specs[name]) for name in specs}
    runtime_root = root / proof["bundle"]["gate"]["future_roots"][-1]
    evaluation_root = root / proof["bundle"]["gate"]["future_roots"][-2]
    runtime_authorization_record = runtime_root / "runtime_authorization_record_v0.2.json"
    control: dict[str, Mapping[str, Any]] = {}
    corrected: dict[str, Mapping[str, Any]] = {}
    case_comparisons: dict[str, Mapping[str, Any]] = {}
    aggregate_comparisons: dict[str, Mapping[str, Any]] = {}
    d1a_result: Mapping[str, Any] = {}
    d1a_summary: Mapping[str, Any] = {}

    def unified_preflight() -> Mapping[str, Any]:
        return _write_json_new(runtime_authorization_record, build_runtime_authorization_provenance(proof))

    def reproduce(arm: str) -> Mapping[str, Any]:
        spec, item = specs[arm], paths[arm]
        corpus = root / spec["frozen_inputs"]["corpus"]["path"]
        builder.build(arm, corpus, item["control_index"], item["control_metadata"], root=root)
        evaluated = evaluator.evaluate_arm(arm, corpus, item["control_index"], item["control_metadata"], item["control_output"], root=root)
        outputs = spec["primary_original_control"]["outputs"]
        if arm == "EV03":
            original_ranking = root / outputs["normative_results_csv"]["path"]
            original_summary = root / outputs["normative_case_summary_csv"]["path"]
            schemas = (evaluator.EV03_CANDIDATE_FIELDS, evaluator.EV03_CASE_FIELDS)
        else:
            original_ranking = root / outputs["normative_hierarchical_results_csv"]["path"]
            original_summary = root / outputs["normative_hierarchical_case_summary_csv"]["path"]
            schemas = (evaluator.EV04_CANDIDATE_FIELDS, evaluator.EV04_CASE_FIELDS)
        original_metrics = json.loads((root / spec["primary_original_control"]["run_metadata"]["path"]).read_text(encoding="utf-8"))["metrics"]
        comparison = evaluator.compare_control_reproduction(
            original_ranking, item["control_output"] / item["ranking_name"],
            original_summary, item["control_output"] / item["summary_name"],
            original_metrics, evaluated["metrics"],
            expected_candidate_schema=schemas[0], expected_case_schema=schemas[1],
        )
        required = spec["required_control"]
        logical_status = None
        if arm == "EV03":
            historical_index = load_bm25_index(root / spec["frozen_inputs"]["index_identity_from_frozen_run_metadata"]["path"])
            recovered_index = load_bm25_index(item["control_index"])
            logical_status = ev03_recovery.logical_identity(historical_index, recovered_index)["LOGICAL_INDEX_IDENTITY"]
        control[arm] = validate_control_exact(
            arm,
            required,
            comparison,
            item["control_output"] / item["ranking_name"],
            item["control_output"] / item["summary_name"],
            original_metrics,
            evaluated["metrics"],
            logical_index_identity=logical_status,
        )
        return control[arm]

    def materialize(arm: str) -> Mapping[str, Any]:
        spec = specs[arm]
        source = v01_gate.validate_current_text_identity(root, spec["frozen_inputs"]["corpus"], f"{arm} corpus")
        digest = evaluator.materialize_corrective_corpus(source, paths[arm]["corrected_corpus"], spec["corrective_corpus"]["patches"], root=root)
        return {"status": "PASS", "corrected_corpus_sha256": digest}

    def build(arm: str) -> Mapping[str, Any]:
        item = paths[arm]
        return {"status": "PASS", "metadata": builder.build(arm, item["corrected_corpus"], item["corrected_index"], item["corrected_metadata"], root=root)}

    def evaluate(arm: str) -> Mapping[str, Any]:
        item = paths[arm]
        corrected[arm] = evaluator.evaluate_arm(arm, item["corrected_corpus"], item["corrected_index"], item["corrected_metadata"], item["corrected_output"], root=root)
        return {"status": "PASS", **corrected[arm]}

    def execute_d1a() -> Mapping[str, Any]:
        nonlocal d1a_result, d1a_summary
        d1a_result = d1a_runner.execute_authorized(root, authorization_proof=proof)
        d1a_summary = _d1a_summary_reference(root, proof["bundle"]["d1a"], d1a_result)
        return {"status": "PASS", "result": d1a_result}

    def integrity() -> Mapping[str, Any]:
        for arm, item in paths.items():
            required = (item["control_index"], item["control_metadata"], item["corrected_corpus"], item["corrected_index"], item["corrected_metadata"], item["corrected_output"] / item["ranking_name"], item["corrected_output"] / item["summary_name"])
            require(all(path.is_file() for path in required), f"Missing runtime output for {arm}")
        return {"status": "PASS"}

    def compare_cases() -> Mapping[str, Any]:
        for arm, spec in specs.items():
            outputs = spec["primary_original_control"]["outputs"]
            ranking_key = "normative_results_csv" if arm == "EV03" else "normative_hierarchical_results_csv"
            summary_key = "normative_case_summary_csv" if arm == "EV03" else "normative_hierarchical_case_summary_csv"
            rows = evaluator.produce_case_level_comparison(
                arm, _read_csv(root / outputs[summary_key]["path"]), _read_csv(paths[arm]["corrected_output"] / paths[arm]["summary_name"]),
                _read_csv(root / outputs[ranking_key]["path"]), _read_csv(paths[arm]["corrected_output"] / paths[arm]["ranking_name"]),
            )
            case_comparisons[arm] = _write_json_new(evaluation_root / f"{arm.lower()}_case_level_comparison_v0.2.json", {"status": "PASS", "rows": rows})
        return {"status": "PASS"}

    def compare_aggregates() -> Mapping[str, Any]:
        for arm, spec in specs.items():
            original = json.loads((root / spec["primary_original_control"]["run_metadata"]["path"]).read_text(encoding="utf-8"))["metrics"]
            aggregate_comparisons[arm] = _write_json_new(evaluation_root / f"{arm.lower()}_aggregate_comparison_v0.2.json", {"status": "PASS", "metrics": evaluator.produce_aggregate_comparison(original, corrected[arm]["metrics"])})
        return {"status": "PASS"}

    def summary() -> Mapping[str, Any]:
        return _write_json_new(evaluation_root / "unified_sensitivity_summary_v0.2.json", build_unified_summary(aggregate_comparisons["EV03"], aggregate_comparisons["EV04"], d1a_summary))

    def manifest() -> Mapping[str, Any]:
        payload = build_execution_manifest_payload(root, runtime_authorization_record, proof, control, corrected, d1a_result)
        return _write_json_new(runtime_root / "execution_manifest_v0.2.json", payload)

    def ledger() -> Mapping[str, Any]:
        ledger_path = runtime_root / "exact_hash_ledger_v0.2.json"
        entries = validate_runtime_ledger_contract(root, proof["bundle"]["gate"]["runtime_hash_ledger_contract"])
        return _write_json_new(ledger_path, {"status": "PASS", "entries": entries, "mismatch_count": 0})

    return {
        "unified_preflight": unified_preflight,
        "ev03_control": lambda: reproduce("EV03"),
        "verify_ev03": lambda: control["EV03"],
        "ev03_materialize": lambda: materialize("EV03"),
        "ev03_build": lambda: build("EV03"),
        "ev03_evaluate": lambda: evaluate("EV03"),
        "ev04_control": lambda: reproduce("EV04"),
        "verify_ev04": lambda: control["EV04"],
        "ev04_materialize": lambda: materialize("EV04"),
        "ev04_build": lambda: build("EV04"),
        "ev04_evaluate": lambda: evaluate("EV04"),
        "d1a_execute": execute_d1a,
        "integrity": integrity,
        "case_comparisons": compare_cases,
        "aggregate_comparisons": compare_aggregates,
        "summary": summary,
        "manifest": manifest,
        "ledger": ledger,
        "final_state": lambda: {"status": "PASS", "state": "COMPLETED"},
    }


def execute_authorized(root: Path = ROOT) -> dict[str, Any]:
    proof = preflight_authorized(root)
    return run_authorized_pipeline(_default_operations(root, proof))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--execute-authorized", action="store_true")
    args = parser.parse_args(argv)
    result = execute_authorized(ROOT) if args.execute_authorized else preflight(ROOT)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
