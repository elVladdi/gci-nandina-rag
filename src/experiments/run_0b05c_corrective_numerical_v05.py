"""Fail-closed 19-step runner for a future, separately authorized Attempt06."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import subprocess
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from . import run_0b05c_corrective_numerical_v02 as common
from .prepare_0b05c_corrective_numerical_gate_v05 import (
    ARTIFACT_NAMES, AUDIT_ROOT, AUTHORIZATION_RECORD, FUTURE_ROOTS, PIPELINE_STEPS,
    AUTHORIZATION_BASELINE_ARTIFACTS, ROOT, ContractViolation, build_bundle,
    load_authorization_transition_from_git, preauthorization_environment_preflight,
    preflight as gate_preflight, require, validate_manifest_payload,
    validate_runtime_ledger, write_manifest_new,
)


OPERATION_KEYS = (
    "unified_preflight", "ev03_control", "verify_ev03", "ev03_materialize", "ev03_build", "ev03_evaluate",
    "ev04_control", "verify_ev04", "ev04_materialize", "ev04_build", "ev04_evaluate", "d1a_execute",
    "integrity", "case_comparisons", "aggregate_comparisons", "summary", "manifest", "ledger", "final_state",
)
SPEC_PATHS = {
    "EV03": AUDIT_ROOT / ARTIFACT_NAMES[0],
    "EV04": AUDIT_ROOT / ARTIFACT_NAMES[1],
    "d1a": AUDIT_ROOT / ARTIFACT_NAMES[2],
}
EV03_AGGREGATE_ORDER = (
    "mrr", "top_1", "top_3", "top_5", "top_10", "top_50", "recall_at_50", "recall_at_100",
    "partida_at_10", "sub_partida_at_10", "clase_at_10", "partida_at_50", "sub_partida_at_50",
    "clase_at_50", "partida_at_100", "sub_partida_at_100", "clase_at_100",
)
D1A_REFERENCE_KEYS = ("aggregate_comparison", "case_level_comparison", "execution_manifest", "hash_ledger")


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(payload, dict), f"JSON object required: {path.as_posix()}")
    return payload


def _read_csv(path: Path) -> list[dict[str, str]]:
    require(path.is_file() and path.stat().st_size > 0, f"CSV missing or empty: {path.as_posix()}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_json_new(path: Path, payload: Mapping[str, Any]) -> dict[str, Any]:
    require(not path.exists(), f"Runner refuses overwrite or resume: {path.as_posix()}")
    encoded = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(encoded, encoding="utf-8", newline="\n")
    require(_read_json(path) == dict(payload), f"JSON round-trip changed content: {path.as_posix()}")
    return dict(payload)


def preflight(root: Path = ROOT) -> dict[str, Any]:
    return gate_preflight(root)


def preflight_authorized(root: Path = ROOT, *, interpreter: Path | str | None = None) -> dict[str, Any]:
    """Future authorization gate. Environment readiness runs before any write."""

    clean = subprocess.run(["git", "status", "--short", "--untracked-files=no"], cwd=root, check=True, capture_output=True, text=True).stdout.strip()
    require(clean == "", "Tracked working tree is not clean")
    require((root / AUTHORIZATION_RECORD).is_file(), "v0.5 authorization record is absent")
    gate = _read_json(root / AUDIT_ROOT / ARTIFACT_NAMES[3])
    require(gate.get("gate_status") == "APPROVED / INTEGRATED", "v0.5 gate is not approved/integrated")
    require(gate.get("authorization_readiness") == "AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION", "v0.5 gate is not authorization-ready")
    required = {key: "AUTHORIZED" for key in ("EV03_NUMERICAL_EXECUTION", "EV04_NUMERICAL_EXECUTION", "D1A_NUMERICAL_EXECUTION", "UNIFIED_0B05C_NUMERICAL_EXECUTION")}
    require({key: gate.get("authorization", {}).get(key) for key in required} == required, "v0.5 four-arm authorization is incomplete")
    require(gate.get("attempt06") == "AUTHORIZED / NOT_EXECUTED", "Attempt06 is not authorized")
    require(all(not (root / path).exists() for path in FUTURE_ROOTS), "A v0.5 prospective root exists")
    specs = {name: _read_json(root / path) for name, path in SPEC_PATHS.items()}
    for name, key in (("EV03", "EV03_NUMERICAL_EXECUTION"), ("EV04", "EV04_NUMERICAL_EXECUTION"), ("d1a", "D1A_NUMERICAL_EXECUTION")):
        require(specs[name].get("authorization", {}).get(key) == "AUTHORIZED", f"{name} v0.5 spec is not authorized")
        require(specs[name].get("attempt06") == "AUTHORIZED / NOT_EXECUTED", f"{name} Attempt06 state is invalid")
    transition = load_authorization_transition_from_git(root, gate)
    environment = preauthorization_environment_preflight(root, interpreter)
    return {
        "status": "PASS", "mode": "AUTHORIZED_PREFLIGHT_ONLY", "authorization": required,
        "authorization_record_binding": transition["authorization_record_binding"],
        "authorization_baseline_commit": transition["authorization_baseline_commit"],
        "execution_authorization_commit": transition["execution_authorization_commit"],
        "authorization_transition_proof": transition["transition"],
        "authorization_commit_shape": transition["authorization_commit_shape"],
        "current_dependency_bindings_equal_baseline": transition["current_dependency_bindings_equal_baseline"],
        "authorized_artifact_bindings": transition["authorized_artifact_bindings"],
        "environment": environment, "bundle": {**build_bundle(root), **specs},
        "numerical_execution_occurred": False, "prospective_roots_present": False,
    }


def run_authorized_pipeline(operations: Mapping[str, Callable[[], Mapping[str, Any]]]) -> dict[str, Any]:
    require(tuple(operations) == OPERATION_KEYS, "Operation contract does not match the frozen 19-step order")
    states: dict[str, dict[str, Any]] = {}
    for step, key in zip(PIPELINE_STEPS, OPERATION_KEYS, strict=True):
        result = operations[key]()
        require(isinstance(result, Mapping), f"Pipeline operation returned malformed result: {key}")
        if key == "final_state":
            require(len(states) == 18, "Final state cannot pass before 18 prior steps")
            require(result.get("status") == "PASS", "Final state did not PASS")
        elif key in {"verify_ev03", "verify_ev04"}:
            require(result.get("status") == "PASS_EXACT", f"Control verification did not PASS_EXACT: {key}")
        else:
            require(result.get("status") in {"PASS", "PASS_EXACT"}, f"Pipeline failed closed: {key}")
        states[step] = dict(result)
    return {"status": "PASS", "mode": "AUTHORIZED_EXECUTION", "steps": states}


def validate_arm_runtime_integrity(
    arm: str, ranking: Path, summary: Path, metrics_path: Path,
) -> dict[str, Any]:
    from . import evaluate_normative_bm25_corrective_0b05c_v05 as evaluator
    candidates, cases = _read_csv(ranking), _read_csv(summary)
    expected_candidate = evaluator.EV03_CANDIDATE_FIELDS if arm == "EV03" else evaluator.EV04_CANDIDATE_FIELDS
    expected_case = evaluator.EV03_CASE_FIELDS if arm == "EV03" else evaluator.EV04_CASE_FIELDS
    require(candidates and set(candidates[0]) == set(expected_candidate), f"{arm} candidate schema changed")
    require(cases and set(cases[0]) == set(expected_case), f"{arm} case schema changed")
    summaries = evaluator._case_summary_by_id(cases, arm)
    require(len(summaries) == 1056, f"{arm} must contain 1056 unique cases")
    rankings = evaluator.effective_rankings_v05(candidates, summaries, arm, require_unique_codes=arm == "EV04")
    metrics = _read_json(metrics_path).get("metrics")
    evaluator.validate_complete_metrics_v05(arm, cases, metrics, require_real_case_count=True)
    snapshot = {path.as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in (ranking, summary, metrics_path)}
    return {"status": "PASS", "case_count": len(summaries), "empty_ranking_count": sum(not value for value in rankings.values()), "snapshot": snapshot}


def validate_d1a_runtime_integrity(required_paths: Sequence[Path]) -> dict[str, Any]:
    require(required_paths, "D1a integrity path set is empty")
    snapshot: dict[str, str] = {}
    for path in required_paths:
        require(path.is_file() and path.stat().st_size > 0, f"D1a output missing or truncated: {path.as_posix()}")
        if path.suffix == ".json":
            _read_json(path)
        snapshot[path.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {"status": "PASS", "snapshot": snapshot}


def strict_unified_summary(ev03: Mapping[str, Any], ev04: Mapping[str, Any], d1a: Mapping[str, Any]) -> dict[str, Any]:
    from . import evaluate_normative_bm25_corrective_0b05c_v05 as evaluator
    require(isinstance(ev03, Mapping) and ev03.get("status") == "PASS", "EV03 aggregate payload is missing or failed")
    require(isinstance(ev04, Mapping) and ev04.get("status") == "PASS", "EV04 aggregate payload is missing or failed")
    evaluator.validate_aggregate_rows(ev03.get("metrics"), EV03_AGGREGATE_ORDER, "EV03 unified")
    evaluator.validate_aggregate_rows(ev04.get("metrics"), evaluator.EV04_AGGREGATE_METRIC_ORDER, "EV04 unified")
    require(isinstance(d1a, Mapping) and d1a.get("status") == "PASS", "D1a validated summary is missing or failed")
    require(set(d1a) == {"status", *D1A_REFERENCE_KEYS}, "D1a validated summary schema is not exact")
    for key in D1A_REFERENCE_KEYS:
        reference = d1a.get(key)
        require(isinstance(reference, Mapping) and set(reference) == {"path", "sha256", "size_bytes"}, f"D1a reference is incomplete: {key}")
        require(isinstance(reference["path"], str) and reference["path"] and isinstance(reference["sha256"], str) and len(reference["sha256"]) == 64 and isinstance(reference["size_bytes"], int) and reference["size_bytes"] > 0, f"D1a reference is malformed: {key}")
    return {"status": "PASS", "EV03": dict(ev03), "EV04": dict(ev04), "D1a": dict(d1a)}


def _arm_paths(root: Path, arm: str, spec: Mapping[str, Any]) -> dict[str, Path]:
    execution = spec["prospective_execution"]
    names = ("normative_flat_results.csv", "normative_flat_case_summary.csv", "normative_flat_metrics.json") if arm == "EV03" else ("normative_hierarchical_results.csv", "normative_hierarchical_case_summary.csv", "normative_hierarchical_metrics.json")
    return {
        "control_index": root / execution["control_reproduction_index_root"] / "index.pkl",
        "control_metadata": root / execution["control_reproduction_index_root"] / "index_metadata.json",
        "control_output": root / execution["control_reproduction_output_root"],
        "corrected_corpus": root / spec["corrective_corpus"]["prospective_path"],
        "corrected_index": root / execution["corrected_index_root"] / "index.pkl",
        "corrected_metadata": root / execution["corrected_index_root"] / "index_metadata.json",
        "corrected_output": root / execution["corrected_output_root"],
        "ranking_name": Path(names[0]), "summary_name": Path(names[1]), "metrics_name": Path(names[2]),
    }


def _default_operations(root: Path, proof: Mapping[str, Any], *, interpreter: Path | str | None = None) -> dict[str, Callable[[], Mapping[str, Any]]]:
    from ..retrieval.bm25 import load_bm25_index
    from . import build_bm25_corrective_0b05c_v03 as builder
    from . import evaluate_normative_bm25_corrective_0b05c_v05 as evaluator
    from . import prepare_0b05c_corrective_numerical_gate_v01 as v01_gate
    from . import run_d1a_corrective_0b05c_v05 as d1a_runner
    from . import verify_ev03_historical_builder_recovery_v02 as ev03_recovery

    specs = {arm: _read_json(root / SPEC_PATHS[arm]) for arm in ("EV03", "EV04")}
    paths = {arm: _arm_paths(root, arm, specs[arm]) for arm in specs}
    runtime_root = root / FUTURE_ROOTS[-1]; evaluation_root = root / FUTURE_ROOTS[-2]
    runtime_record = runtime_root / "runtime_authorization_record_v0.5.json"
    control: dict[str, Mapping[str, Any]] = {}; baseline_metrics: dict[str, Mapping[str, Any]] = {}
    corrected: dict[str, Mapping[str, Any]] = {}
    comparisons: dict[str, Mapping[str, Any]] = {}; aggregates: dict[str, Mapping[str, Any]] = {}
    d1a_result: Mapping[str, Any] = {}; d1a_summary: Mapping[str, Any] = {}; integrity_snapshot: dict[str, str] = {}

    def unified_preflight() -> Mapping[str, Any]:
        return _write_json_new(runtime_record, {"status": "PASS", "mode": "AUTHORIZED_PREFLIGHT_ONLY", "authorization": proof["authorization"], "environment": proof["environment"]["interpreter"]})

    def reproduce(arm: str) -> Mapping[str, Any]:
        spec, item = specs[arm], paths[arm]; corpus = root / spec["frozen_inputs"]["corpus"]["path"]
        builder.build(arm, corpus, item["control_index"], item["control_metadata"], root=root)
        observed = evaluator.evaluate_arm(arm, corpus, item["control_index"], item["control_metadata"], item["control_output"], root=root)
        outputs = spec["primary_original_control"]["outputs"]
        ranking_key = "normative_results_csv" if arm == "EV03" else "normative_hierarchical_results_csv"
        summary_key = "normative_case_summary_csv" if arm == "EV03" else "normative_hierarchical_case_summary_csv"
        original_ranking, original_summary = root / outputs[ranking_key]["path"], root / outputs[summary_key]["path"]
        if arm == "EV04":
            comparison = evaluator.v04.compare_complete_ev04_control_v04(original_ranking, item["control_output"] / item["ranking_name"], original_summary, item["control_output"] / item["summary_name"])
            expected_metrics = comparison["expected_metrics"]; observed = {**observed, "metrics": comparison["actual_metrics"]}
        else:
            expected_metrics = _read_json(root / spec["primary_original_control"]["run_metadata"]["path"])["metrics"]
            comparison = evaluator.legacy.compare_control_reproduction(original_ranking, item["control_output"] / item["ranking_name"], original_summary, item["control_output"] / item["summary_name"], expected_metrics, observed["metrics"], expected_candidate_schema=evaluator.EV03_CANDIDATE_FIELDS, expected_case_schema=evaluator.EV03_CASE_FIELDS)
        logical = None
        if arm == "EV03":
            historical = load_bm25_index(root / spec["frozen_inputs"]["index_identity_from_frozen_run_metadata"]["path"])
            recovered = load_bm25_index(item["control_index"])
            logical = ev03_recovery.logical_identity(historical, recovered)["LOGICAL_INDEX_IDENTITY"]
        baseline_metrics[arm] = expected_metrics
        control[arm] = common.validate_control_exact(arm, spec["required_control"], comparison, item["control_output"] / item["ranking_name"], item["control_output"] / item["summary_name"], expected_metrics, observed["metrics"], logical_index_identity=logical)
        return control[arm]

    def materialize(arm: str) -> Mapping[str, Any]:
        spec = specs[arm]; source = v01_gate.validate_current_text_identity(root, spec["frozen_inputs"]["corpus"], f"{arm} corpus")
        return {"status": "PASS", "corrected_corpus_sha256": evaluator.materialize_corrective_corpus(source, paths[arm]["corrected_corpus"], spec["corrective_corpus"]["patches"], root=root)}

    def build(arm: str) -> Mapping[str, Any]:
        item = paths[arm]; return {"status": "PASS", "metadata": builder.build(arm, item["corrected_corpus"], item["corrected_index"], item["corrected_metadata"], root=root)}

    def evaluate(arm: str) -> Mapping[str, Any]:
        item = paths[arm]; corrected[arm] = evaluator.evaluate_arm(arm, item["corrected_corpus"], item["corrected_index"], item["corrected_metadata"], item["corrected_output"], root=root)
        return {"status": "PASS", **corrected[arm]}

    def execute_d1a() -> Mapping[str, Any]:
        nonlocal d1a_result, d1a_summary
        d1a_result = d1a_runner.execute_authorized(root, authorization_proof=proof, interpreter=interpreter)
        d1a_summary = d1a_runner.d1a_summary_reference(root, _read_json(root / SPEC_PATHS["d1a"]), d1a_result)
        return {"status": "PASS", "result": d1a_result}

    def integrity() -> Mapping[str, Any]:
        nonlocal integrity_snapshot
        results = {}
        for arm, item in paths.items():
            results[arm] = validate_arm_runtime_integrity(arm, item["corrected_output"] / item["ranking_name"], item["corrected_output"] / item["summary_name"], item["corrected_output"] / item["metrics_name"])
            integrity_snapshot.update(results[arm]["snapshot"])
        d1a_paths = [root / d1a_summary[key]["path"] for key in D1A_REFERENCE_KEYS]
        d1a_integrity = validate_d1a_runtime_integrity(d1a_paths); integrity_snapshot.update(d1a_integrity["snapshot"])
        return {"status": "PASS", "arms": results, "d1a": d1a_integrity}

    def compare_cases() -> Mapping[str, Any]:
        for arm, spec in specs.items():
            outputs = spec["primary_original_control"]["outputs"]; rk = "normative_results_csv" if arm == "EV03" else "normative_hierarchical_results_csv"; sk = "normative_case_summary_csv" if arm == "EV03" else "normative_hierarchical_case_summary_csv"
            rows = evaluator.produce_case_level_comparison(arm, _read_csv(root / outputs[sk]["path"]), _read_csv(paths[arm]["corrected_output"] / paths[arm]["summary_name"]), _read_csv(root / outputs[rk]["path"]), _read_csv(paths[arm]["corrected_output"] / paths[arm]["ranking_name"]))
            comparisons[arm] = _write_json_new(evaluation_root / f"{arm.lower()}_case_level_comparison_v0.5.json", {"status": "PASS", "rows": rows})
        return {"status": "PASS"}

    def compare_aggregates() -> Mapping[str, Any]:
        for arm, spec in specs.items():
            original = baseline_metrics[arm]
            aggregates[arm] = _write_json_new(evaluation_root / f"{arm.lower()}_aggregate_comparison_v0.5.json", {"status": "PASS", "metrics": evaluator.produce_aggregate_comparison_v05(original, corrected[arm]["metrics"], arm=arm)})
        return {"status": "PASS"}

    def summary() -> Mapping[str, Any]:
        return _write_json_new(evaluation_root / "unified_sensitivity_summary_v0.5.json", strict_unified_summary(aggregates["EV03"], aggregates["EV04"], d1a_summary))

    def manifest() -> Mapping[str, Any]:
        provenance = {
            "status": "PASS", "execution_authorization_commit": proof["execution_authorization_commit"],
            "authorization_baseline_commit": proof["authorization_baseline_commit"],
            "authorization_transition_proof": proof["authorization_transition_proof"],
            "authorization_commit_shape": proof["authorization_commit_shape"],
            "current_dependency_bindings_equal_baseline": proof["current_dependency_bindings_equal_baseline"],
            "authorization_flags": proof["authorization"],
            "authorization_record_binding": proof["authorization_record_binding"],
            "authorized_artifact_bindings": proof["authorized_artifact_bindings"],
        }
        environment = proof["environment"]["interpreter"]
        payload = {"artifact_id": "0b05c_corrective_execution_manifest_v0.5", "status": "PASS", "authorization_provenance": provenance, "environment_fingerprint": environment, "pipeline_steps": list(PIPELINE_STEPS), "future_roots": list(FUTURE_ROOTS), "results": {"control": control, "corrected": corrected, "d1a": d1a_result}}
        path = runtime_root / "execution_manifest_v0.5.json"; write_manifest_new(path, payload); return payload

    def ledger() -> Mapping[str, Any]:
        bundle = build_bundle(root); expected = set(bundle["ledger"]["expected_set"]); produced = set(bundle["ledger"]["producer_set"])
        relative_snapshot = {Path(path).relative_to(root).as_posix(): digest for path, digest in integrity_snapshot.items() if Path(path).is_relative_to(root)}
        entries = validate_runtime_ledger(root, expected, produced, snapshot=relative_snapshot, discovery_roots=tuple(FUTURE_ROOTS), excluded_self_path=bundle["ledger"]["excluded_self_path"])
        return _write_json_new(runtime_root / "exact_hash_ledger_v0.5.json", {"status": "PASS", "entries": entries, "mismatch_count": 0})

    return {
        "unified_preflight": unified_preflight, "ev03_control": lambda: reproduce("EV03"), "verify_ev03": lambda: control["EV03"],
        "ev03_materialize": lambda: materialize("EV03"), "ev03_build": lambda: build("EV03"), "ev03_evaluate": lambda: evaluate("EV03"),
        "ev04_control": lambda: reproduce("EV04"), "verify_ev04": lambda: control["EV04"], "ev04_materialize": lambda: materialize("EV04"),
        "ev04_build": lambda: build("EV04"), "ev04_evaluate": lambda: evaluate("EV04"), "d1a_execute": execute_d1a,
        "integrity": integrity, "case_comparisons": compare_cases, "aggregate_comparisons": compare_aggregates,
        "summary": summary, "manifest": manifest, "ledger": ledger, "final_state": lambda: {"status": "PASS", "state": "COMPLETED"},
    }


def execute_authorized(root: Path = ROOT, *, interpreter: Path | str | None = None) -> dict[str, Any]:
    proof = preflight_authorized(root, interpreter=interpreter)
    return run_authorized_pipeline(_default_operations(root, proof, interpreter=interpreter))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true"); group.add_argument("--execute-authorized", action="store_true")
    args = parser.parse_args(argv); result = execute_authorized(ROOT) if args.execute_authorized else preflight(ROOT)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
