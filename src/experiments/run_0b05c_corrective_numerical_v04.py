"""Fail-closed unified runner for a future authorized 0B-05C v0.4 run."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Callable, Mapping

from . import run_0b05c_corrective_numerical_v02 as common
from .prepare_0b05c_corrective_numerical_gate_v04 import (
    ARTIFACT_NAMES,
    AUDIT_ROOT,
    AUTHORIZATION,
    AUTHORIZATION_BASELINE_ARTIFACTS,
    AUTHORIZATION_RECORD,
    AUTHORIZED_ATTEMPT05,
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
SPEC_PATHS = {
    "EV03": AUDIT_ROOT / ARTIFACT_NAMES[0],
    "EV04": AUDIT_ROOT / ARTIFACT_NAMES[1],
    "d1a": AUDIT_ROOT / ARTIFACT_NAMES[2],
}
def preflight(root: Path = ROOT) -> dict[str, Any]:
    return gate_preflight(root)


def preflight_authorized(root: Path = ROOT) -> dict[str, Any]:
    gate = read_json(root, GATE_PATH)
    clean = subprocess.run(["git", "status", "--short", "--untracked-files=no"], cwd=root, check=True, capture_output=True, text=True).stdout.strip()
    require(clean == "", "Tracked working tree is not clean")
    require(gate.get("gate_status") == AUTHORIZED_GATE_STATUS, "Authorized v0.4 gate is not approved and integrated")
    require(gate.get("authorization_readiness") == AUTHORIZED_READINESS, "Authorized v0.4 gate readiness is invalid")
    required = {key: "AUTHORIZED" for key in AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")}
    current = {key: gate["authorization"].get(key) for key in required}
    require(current == required, "All four 0B-05C v0.4 numerical components must be AUTHORIZED before any side effect")
    specs = {name: read_json(root, path) for name, path in SPEC_PATHS.items()}
    for name, authorization_key in (("EV03", "EV03_NUMERICAL_EXECUTION"), ("EV04", "EV04_NUMERICAL_EXECUTION"), ("d1a", "D1A_NUMERICAL_EXECUTION")):
        require(specs[name].get("authorization", {}).get(authorization_key) == "AUTHORIZED", f"{name} v0.4 spec is not AUTHORIZED")
    attempt_states = {gate.get("attempt05"), *(spec.get("attempt05") for spec in specs.values())}
    require(attempt_states == {AUTHORIZED_ATTEMPT05}, "Attempt05 authorization state is not coherent across gate and specs")
    require(gate["authorization"].get("authorization_record_present") is True, "Authorization record v0.4 state is not present")
    require((root / AUTHORIZATION_RECORD).is_file(), "Authorization record v0.4 is required")
    transition = load_authorization_transition_from_git(root, gate)
    committed_specs = transition["artifacts"]
    require(committed_specs["ev03_spec"] == specs["EV03"], "Filesystem EV03 spec differs from committed authorization spec")
    require(committed_specs["ev04_spec"] == specs["EV04"], "Filesystem EV04 spec differs from committed authorization spec")
    require(committed_specs["d1a_spec"] == specs["d1a"], "Filesystem D1a spec differs from committed authorization spec")
    for relative in FUTURE_ROOTS:
        require(not (root / relative).exists(), f"Prospective v0.4 root already exists: {relative}")
    for binding in gate["dependency_bindings"]:
        if binding["classification"] == "FROZEN_FILE_IDENTITY":
            path = root / binding["path"]
            require(path.is_file(), f"Frozen file is missing: {binding['path']}")
            require(path.stat().st_size == binding["size_bytes"], f"Frozen file size mismatch: {binding['path']}")
            require(hashlib.sha256(path.read_bytes()).hexdigest() == binding["sha256"], f"Frozen file SHA mismatch: {binding['path']}")
        else:
            require(git_binding(root, binding["path"], "HEAD", binding["classification"]) == binding, f"Canonical binding mismatch: {binding['path']}")
    record_binding = git_binding(root, AUTHORIZATION_RECORD.as_posix(), "HEAD")
    return {
        "status": "PASS",
        "mode": "AUTHORIZED_PREFLIGHT_ONLY",
        "numerical_execution_occurred": False,
        "authorization": current,
        "authorization_baseline_commit": transition["authorization_baseline_commit"],
        "authorization_record": transition["record"],
        "authorization_record_binding": record_binding,
        "baseline_external_audit": transition["baseline_external_audit"],
        "baseline_artifact_bindings": transition["baseline_artifact_bindings"],
        "authorized_artifact_bindings": transition["authorized_artifact_bindings"],
        "authorization_transition_proof": transition["transition"],
        "execution_authorization_commit": transition["execution_authorization_commit"],
        "bundle": {"gate": gate, **specs},
    }


def run_authorized_pipeline(operations: Mapping[str, Callable[[], Mapping[str, Any]]]) -> dict[str, Any]:
    require(tuple(operations) == OPERATION_KEYS, "Operation contract does not match the frozen 19-step order")
    state: dict[str, Mapping[str, Any]] = {}
    for step, key in zip(PIPELINE_STEPS, OPERATION_KEYS, strict=True):
        result = operations[key]()
        if key in {"verify_ev03", "verify_ev04"}:
            require(result.get("status") == "PASS_EXACT", f"Pipeline control verification requires PASS_EXACT: {step}")
        elif key == "final_state":
            require(len(state) == 18, "Final state cannot pass before the preceding 18 steps")
            require(result.get("status") == "PASS", f"Final completion state must be PASS: {step}")
        else:
            require(result.get("status") in {"PASS", "PASS_EXACT"}, f"Pipeline step failed closed: {step}")
        state[step] = dict(result)
    return {"status": "PASS", "mode": "AUTHORIZED_EXECUTION", "steps": state}


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_json_new(path: Path, payload: Mapping[str, Any]) -> dict[str, Any]:
    require(not path.exists(), f"Runner refuses overwrite or resume: {path.as_posix()}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return dict(payload)


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


def build_runtime_authorization_provenance(proof: Mapping[str, Any]) -> dict[str, Any]:
    required = {key: "AUTHORIZED" for key in AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")}
    require(proof.get("status") == "PASS" and proof.get("mode") == "AUTHORIZED_PREFLIGHT_ONLY", "Runtime authorization proof is invalid")
    require(proof.get("authorization") == required, "Runtime authorization proof lacks four authorized states")
    return {
        "status": "PASS",
        "mode": "AUTHORIZED_PREFLIGHT_ONLY",
        "execution_authorization_commit": proof["execution_authorization_commit"],
        "authorization_baseline_commit": proof["authorization_baseline_commit"],
        "authorization": dict(required),
        "authorization_record": dict(proof["authorization_record_binding"]),
        "baseline_external_audit": proof["baseline_external_audit"],
        "authorized_artifacts": {key: dict(value) for key, value in proof["authorized_artifact_bindings"].items()},
    }


def _default_operations(root: Path, proof: Mapping[str, Any]) -> dict[str, Callable[[], Mapping[str, Any]]]:
    from ..retrieval.bm25 import load_bm25_index
    from . import build_bm25_corrective_0b05c_v03 as builder
    from . import evaluate_normative_bm25_corrective_0b05c_v04 as evaluator
    from . import prepare_0b05c_corrective_numerical_gate_v01 as v01_gate
    from . import run_d1a_corrective_0b05c_v03 as d1a_runner
    from . import verify_ev03_historical_builder_recovery_v02 as ev03_recovery

    specs = {name: proof["bundle"][name] for name in ("EV03", "EV04")}
    paths = {name: _arm_paths(root, name, specs[name]) for name in specs}
    runtime_root = root / proof["bundle"]["gate"]["future_roots"][-1]
    evaluation_root = root / proof["bundle"]["gate"]["future_roots"][-2]
    runtime_record = runtime_root / "runtime_authorization_record_v0.4.json"
    control: dict[str, Mapping[str, Any]] = {}
    corrected: dict[str, Mapping[str, Any]] = {}
    case_comparisons: dict[str, Mapping[str, Any]] = {}
    aggregate_comparisons: dict[str, Mapping[str, Any]] = {}
    d1a_result: Mapping[str, Any] = {}
    d1a_summary: Mapping[str, Any] = {}

    def unified_preflight() -> Mapping[str, Any]:
        return _write_json_new(runtime_record, build_runtime_authorization_provenance(proof))

    def reproduce(arm: str) -> Mapping[str, Any]:
        spec, item = specs[arm], paths[arm]
        corpus = root / spec["frozen_inputs"]["corpus"]["path"]
        builder.build(arm, corpus, item["control_index"], item["control_metadata"], root=root)
        observed = evaluator.evaluate_arm(arm, corpus, item["control_index"], item["control_metadata"], item["control_output"], root=root)
        outputs = spec["primary_original_control"]["outputs"]
        if arm == "EV03":
            original_ranking = root / outputs["normative_results_csv"]["path"]
            original_summary = root / outputs["normative_case_summary_csv"]["path"]
            schemas = evaluator.EV03_CANDIDATE_FIELDS, evaluator.EV03_CASE_FIELDS
        else:
            original_ranking = root / outputs["normative_hierarchical_results_csv"]["path"]
            original_summary = root / outputs["normative_hierarchical_case_summary_csv"]["path"]
            schemas = evaluator.EV04_CANDIDATE_FIELDS, evaluator.EV04_CASE_FIELDS
        original_metrics = json.loads((root / spec["primary_original_control"]["run_metadata"]["path"]).read_text(encoding="utf-8"))["metrics"]
        if arm == "EV04":
            comparison = evaluator.compare_complete_ev04_control_v04(
                original_ranking,
                item["control_output"] / item["ranking_name"],
                original_summary,
                item["control_output"] / item["summary_name"],
            )
            original_metrics = comparison["expected_metrics"]
            observed = {**observed, "metrics": comparison["actual_metrics"]}
        else:
            comparison = evaluator.compare_control_reproduction(
                original_ranking,
                item["control_output"] / item["ranking_name"],
                original_summary,
                item["control_output"] / item["summary_name"],
                original_metrics,
                observed["metrics"],
                expected_candidate_schema=schemas[0],
                expected_case_schema=schemas[1],
            )
        logical = None
        if arm == "EV03":
            historical_index = load_bm25_index(root / spec["frozen_inputs"]["index_identity_from_frozen_run_metadata"]["path"])
            recovered_index = load_bm25_index(item["control_index"])
            logical = ev03_recovery.logical_identity(historical_index, recovered_index)["LOGICAL_INDEX_IDENTITY"]
        control[arm] = common.validate_control_exact(
            arm,
            spec["required_control"],
            comparison,
            item["control_output"] / item["ranking_name"],
            item["control_output"] / item["summary_name"],
            original_metrics,
            observed["metrics"],
            logical_index_identity=logical,
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
        d1a_summary = common._d1a_summary_reference(root, proof["bundle"]["d1a"], d1a_result)
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
                arm,
                _read_csv(root / outputs[summary_key]["path"]),
                _read_csv(paths[arm]["corrected_output"] / paths[arm]["summary_name"]),
                _read_csv(root / outputs[ranking_key]["path"]),
                _read_csv(paths[arm]["corrected_output"] / paths[arm]["ranking_name"]),
            )
            case_comparisons[arm] = _write_json_new(evaluation_root / f"{arm.lower()}_case_level_comparison_v0.4.json", {"status": "PASS", "rows": rows})
        return {"status": "PASS"}

    def compare_aggregates() -> Mapping[str, Any]:
        for arm, spec in specs.items():
            original = json.loads((root / spec["primary_original_control"]["run_metadata"]["path"]).read_text(encoding="utf-8"))["metrics"]
            aggregate_comparisons[arm] = _write_json_new(evaluation_root / f"{arm.lower()}_aggregate_comparison_v0.4.json", {"status": "PASS", "metrics": evaluator.produce_aggregate_comparison(original, corrected[arm]["metrics"])})
        return {"status": "PASS"}

    def summary() -> Mapping[str, Any]:
        payload = common.build_unified_summary(aggregate_comparisons["EV03"], aggregate_comparisons["EV04"], d1a_summary)
        return _write_json_new(evaluation_root / "unified_sensitivity_summary_v0.4.json", payload)

    def manifest() -> Mapping[str, Any]:
        payload = {
            "status": "PASS",
            "execution_order": list(PIPELINE_STEPS),
            "authorization": build_runtime_authorization_provenance(proof),
            "control_reproductions": dict(control),
            "corrected_arms": dict(corrected),
            "d1a": dict(d1a_result),
        }
        return _write_json_new(runtime_root / "execution_manifest_v0.4.json", payload)

    def ledger() -> Mapping[str, Any]:
        entries = common.validate_runtime_ledger_contract(root, proof["bundle"]["gate"]["runtime_hash_ledger_contract"])
        return _write_json_new(runtime_root / "exact_hash_ledger_v0.4.json", {"status": "PASS", "entries": entries, "mismatch_count": 0})

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
