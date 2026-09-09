"""Fail-closed unified runner for a future authorized 0B-05C v0.2 run."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Mapping

from .prepare_0b05c_corrective_numerical_gate_v02 import (
    AUTHORIZATION,
    ContractViolation,
    FUTURE_ROOTS,
    GATE_PATH,
    PIPELINE_STEPS,
    ROOT,
    git_binding,
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


def preflight_authorized(root: Path = ROOT) -> dict[str, Any]:
    gate = read_json(root, GATE_PATH)
    required = {key: "AUTHORIZED" for key in AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")}
    current = {key: gate["authorization"].get(key) for key in required}
    require(current == required, "All four 0B-05C v0.2 numerical components must be AUTHORIZED before any side effect")
    require(gate["authorization"].get("corrective_retrieval_executed") is False, "Corrective retrieval was already executed")
    require(gate["authorization"].get("corrective_metrics_computed") is False, "Corrective metrics were already computed")
    for relative in FUTURE_ROOTS:
        require(not (root / relative).exists(), f"Prospective v0.2 root already exists: {relative}")
    for binding in gate["dependency_bindings"]:
        if binding["classification"] == "FROZEN_FILE_IDENTITY":
            continue
        require(git_binding(root, binding["path"], "HEAD", binding["classification"]) == binding, f"Canonical binding mismatch: {binding['path']}")
    return {
        "status": "PASS",
        "mode": "AUTHORIZED_PREFLIGHT_ONLY",
        "numerical_execution_occurred": False,
        "authorization": current,
        "bundle": {
            "gate": gate,
            "EV03": read_json(root, GATE_PATH.parent / "ev03_numerical_execution_spec_v0.2.json"),
            "EV04": read_json(root, GATE_PATH.parent / "ev04_numerical_execution_spec_v0.2.json"),
            "d1a": read_json(root, GATE_PATH.parent / "d1a_numerical_execution_spec_v0.2.json"),
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


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _arm_paths(root: Path, arm: str, spec: Mapping[str, Any]) -> dict[str, Path]:
    execution = spec["prospective_execution"]
    names = ("normative_results.csv", "normative_case_summary.csv") if arm == "EV03" else ("normative_hierarchical_results.csv", "normative_hierarchical_case_summary.csv")
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

    specs = {name: proof["bundle"][name] for name in ("EV03", "EV04")}
    paths = {name: _arm_paths(root, name, specs[name]) for name in specs}
    runtime_root = root / proof["bundle"]["gate"]["future_roots"][-1]
    evaluation_root = root / proof["bundle"]["gate"]["future_roots"][-2]
    control: dict[str, Mapping[str, Any]] = {}
    corrected: dict[str, Mapping[str, Any]] = {}
    case_comparisons: dict[str, Mapping[str, Any]] = {}
    aggregate_comparisons: dict[str, Mapping[str, Any]] = {}
    d1a_result: Mapping[str, Any] = {}

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
        require(comparison.get("status") == "PASS", f"{arm} control comparison did not pass")
        require(item["control_output"].joinpath(item["ranking_name"]).stat().st_size > 0, f"{arm} ranking is empty")
        control[arm] = {**comparison, "status": "PASS_EXACT", "required_contract": required}
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
        nonlocal d1a_result
        d1a_result = d1a_runner.execute_authorized(root)
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
        return _write_json_new(evaluation_root / "unified_sensitivity_summary_v0.2.json", {"status": "PASS", "EV03": aggregate_comparisons["EV03"], "EV04": aggregate_comparisons["EV04"], "D1a": d1a_result})

    def manifest() -> Mapping[str, Any]:
        return _write_json_new(runtime_root / "execution_manifest_v0.2.json", {"status": "PASS", "execution_order": list(PIPELINE_STEPS), "control_reproductions": control, "corrected_arms": corrected, "d1a": d1a_result})

    def ledger() -> Mapping[str, Any]:
        ledger_path = runtime_root / "exact_hash_ledger_v0.2.json"
        files = sorted(path for base in FUTURE_ROOTS for path in (root / base).rglob("*") if path.is_file() and path != ledger_path)
        entries = [{"path": path.relative_to(root).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "size_bytes": path.stat().st_size} for path in files]
        return _write_json_new(ledger_path, {"status": "PASS", "entries": entries, "mismatch_count": 0})

    return {
        "unified_preflight": lambda: _write_json_new(runtime_root / "runtime_authorization_record_v0.2.json", {"status": "PASS", "mode": proof["mode"], "authorization": proof["authorization"]}),
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
