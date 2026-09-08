"""Bound runner for a future, separately authorized 0B-05C execution.

The current candidate is deliberately closed. The implementation below is
nevertheless complete and deterministic so a later audited authorization can
not silently replace the sequence it authorizes.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Callable, Mapping

from . import prepare_0b05c_corrective_numerical_gate_v01 as gate
from .run_d1a_corrective_0b05c_v01 import ContractViolation, require


ROOT = Path(__file__).resolve().parents[2]
GATE_PATH = gate.AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.1.json"

PIPELINE_STEPS = (
    "01_unified_preflight",
    "02_EV03_control_reproduction",
    "03_EV03_control_reproduction_verification",
    "04_EV03_corrected_corpus_materialization",
    "05_EV03_corrected_index_build",
    "06_EV03_corrected_evaluation",
    "07_EV04_Decision885_control_reproduction",
    "08_EV04_control_reproduction_verification",
    "09_EV04_corrected_corpus_materialization",
    "10_EV04_corrected_index_build",
    "11_EV04_corrected_evaluation",
    "12_D1a_corrected_execution_under_its_own_authorization",
    "13_integrity_validation",
    "14_case_level_comparisons",
    "15_aggregate_comparisons",
    "16_unified_sensitivity_summary",
    "17_execution_manifest",
    "18_exact_hash_ledger",
    "19_final_completion_state",
)


def _read_gate(root: Path) -> dict[str, Any]:
    path = root / GATE_PATH
    require(path.is_file(), f"Frozen 0B-05C gate artifact is missing: {GATE_PATH.as_posix()}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def preflight_not_authorized(root: Path = ROOT) -> dict[str, Any]:
    """Read-only preflight for the frozen candidate; it creates no root."""

    frozen = gate.preflight_not_authorized(root)
    payload = _read_gate(root)
    require(
        payload.get("decisions", {}).get("EV04_DECISION885_REPRODUCTION_GATE") == "MANDATORY/NOT_EXECUTED",
        "EV04 mandatory Decision885 control reproduction contract drifted",
    )
    return {
        "status": "PASS",
        "mode": "PREFLIGHT_ONLY",
        "authorization": dict(payload["authorization"]),
        "prospective_roots_present": False,
        "retrieval_executed": False,
        "evaluation_metrics_computed": False,
        "frozen_gate": frozen["status"],
    }


def preflight_authorized(root: Path = ROOT) -> dict[str, Any]:
    """Read-only validation for a future all-four-authorized commit."""

    proof = gate.preflight_authorized(root)
    require(
        proof["authorization"].get("EV03_NUMERICAL_EXECUTION") == "AUTHORIZED"
        and proof["authorization"].get("EV04_NUMERICAL_EXECUTION") == "AUTHORIZED"
        and proof["authorization"].get("D1A_NUMERICAL_EXECUTION") == "AUTHORIZED"
        and proof["authorization"].get("UNIFIED_0B05C_NUMERICAL_EXECUTION") == "AUTHORIZED",
        "All four numerical authorizations are required before the first side effect",
    )
    return proof


# Preserve the original CLI/API meaning: --preflight proves the closed state.
preflight = preflight_not_authorized


def _require_pass(result: Mapping[str, Any], label: str) -> Mapping[str, Any]:
    require(result.get("status") == "PASS", f"{label} did not PASS; corrected execution is blocked")
    return result


def run_authorized_pipeline(operations: Mapping[str, Callable[[], Mapping[str, Any]]]) -> dict[str, Any]:
    """Run the frozen 19-step order against explicit operations.

    This pure orchestration seam is used by tests with fakes and by the real
    implementation. A control result must pass before its corrected arm is
    reached, and D1a is placed after both corrected BM25 arms.
    """

    required = (
        "authorized_preflight", "ev03_control", "verify_ev03", "ev03_materialize", "ev03_build", "ev03_evaluate",
        "ev04_control", "verify_ev04", "ev04_materialize", "ev04_build", "ev04_evaluate", "d1a_execute",
        "integrity", "case_comparisons", "aggregate_comparisons", "summary", "manifest", "ledger", "final_state",
    )
    require(set(required).issubset(operations), "Authorized pipeline operations are incomplete")
    state: dict[str, Any] = {}
    state[PIPELINE_STEPS[0]] = _require_pass(operations["authorized_preflight"](), "Authorized unified preflight")
    state[PIPELINE_STEPS[1]] = operations["ev03_control"]()
    state[PIPELINE_STEPS[2]] = _require_pass(operations["verify_ev03"](), "EV03 control reproduction")
    state[PIPELINE_STEPS[3]] = operations["ev03_materialize"]()
    state[PIPELINE_STEPS[4]] = operations["ev03_build"]()
    state[PIPELINE_STEPS[5]] = operations["ev03_evaluate"]()
    state[PIPELINE_STEPS[6]] = operations["ev04_control"]()
    state[PIPELINE_STEPS[7]] = _require_pass(operations["verify_ev04"](), "EV04 Decision885 control reproduction")
    state[PIPELINE_STEPS[8]] = operations["ev04_materialize"]()
    state[PIPELINE_STEPS[9]] = operations["ev04_build"]()
    state[PIPELINE_STEPS[10]] = operations["ev04_evaluate"]()
    state[PIPELINE_STEPS[11]] = operations["d1a_execute"]()
    state[PIPELINE_STEPS[12]] = _require_pass(operations["integrity"](), "Unified integrity validation")
    state[PIPELINE_STEPS[13]] = operations["case_comparisons"]()
    state[PIPELINE_STEPS[14]] = operations["aggregate_comparisons"]()
    state[PIPELINE_STEPS[15]] = operations["summary"]()
    state[PIPELINE_STEPS[16]] = operations["manifest"]()
    state[PIPELINE_STEPS[17]] = operations["ledger"]()
    state[PIPELINE_STEPS[18]] = _require_pass(operations["final_state"](), "Final completion state")
    return {"status": "PASS", "execution_order": list(PIPELINE_STEPS), "steps": state}


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_json_new(path: Path, payload: Mapping[str, Any]) -> dict[str, Any]:
    require(not path.exists(), f"Authorized runner refuses overwrite or resume: {path.as_posix()}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return dict(payload)


def _arm_paths(root: Path, arm_name: str, spec: Mapping[str, Any]) -> dict[str, Path]:
    execution = spec["prospective_execution"]
    prefix = "normative_flat" if arm_name == "EV03" else "normative_hierarchical"
    return {
        "control_index": root / execution["control_reproduction_index_root"] / "index.pkl",
        "control_metadata": root / execution["control_reproduction_index_root"] / "index_metadata.json",
        "control_output": root / execution["control_reproduction_output_root"],
        "corrected_corpus": root / spec["corrective_corpus"]["prospective_path"],
        "corrected_index": root / execution["corrected_index_root"] / "index.pkl",
        "corrected_metadata": root / execution["corrected_index_root"] / "index_metadata.json",
        "corrected_output": root / execution["corrected_output_root"],
        "results_name": Path(f"{prefix}_results.csv"),
        "summary_name": Path(f"{prefix}_case_summary.csv"),
    }


def _default_operations(root: Path, proof: Mapping[str, Any]) -> dict[str, Callable[[], Mapping[str, Any]]]:
    """Bind the frozen pipeline to the versioned modules for a future run.

    Constructing the operations has no side effect. The factory is called only
    after the authorized preflight has validated all four authorizations.
    """

    from . import build_bm25_corrective_0b05c_v01 as builder
    from . import evaluate_normative_bm25_corrective_0b05c_v01 as evaluator
    from . import run_d1a_corrective_0b05c_v01 as d1a_runner

    bundle = proof["bundle"]
    gate_payload = _read_gate(root)
    specs = bundle["specifications"]
    runtime_root = root / gate.UNIFIED_RUNTIME_ROOT
    runtime_auth = runtime_root / "runtime_authorization_record.json"
    comparisons = {
        "EV03": (runtime_root / "ev03_case_level_comparison.json", runtime_root / "ev03_aggregate_comparison.json"),
        "EV04": (runtime_root / "ev04_case_level_comparison.json", runtime_root / "ev04_aggregate_comparison.json"),
    }
    summary_path = runtime_root / "unified_sensitivity_summary.json"
    manifest_path = runtime_root / "execution_manifest.json"
    ledger_path = runtime_root / "unified_output_hash_ledger.json"
    paths = {arm_name: _arm_paths(root, arm_name, spec) for arm_name, spec in specs.items()}
    control: dict[str, Mapping[str, Any]] = {}
    corrected: dict[str, Mapping[str, Any]] = {}
    case_outputs: dict[str, Mapping[str, Any]] = {}
    aggregate_outputs: dict[str, Mapping[str, Any]] = {}
    d1a_result: Mapping[str, Any] = {}

    def authorized_preflight() -> Mapping[str, Any]:
        return _write_json_new(runtime_auth, {
            "status": "PASS",
            "authorization": proof["authorization"],
            "all_four_authorizations_required_before_side_effects": True,
            "execution_order": list(PIPELINE_STEPS),
        })

    def reproduce(arm_name: str) -> Mapping[str, Any]:
        spec = specs[arm_name]
        arm = gate.ARMS[arm_name]
        path = paths[arm_name]
        corpus = root / spec["frozen_inputs"]["corpus"]["path"]
        builder.build(arm_name, corpus, path["control_index"], path["control_metadata"], root=root)
        result = evaluator.evaluate_arm(arm_name, corpus, path["control_index"], path["control_metadata"], path["control_output"], root=root)
        metadata_path = root / spec["primary_original_control"]["run_metadata"]["path"]
        frozen_metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        outputs = spec["primary_original_control"]["outputs"]
        schemas = {
            "EV03": (evaluator.EV03_CANDIDATE_FIELDS, evaluator.EV03_CASE_FIELDS),
            "EV04": (evaluator.EV04_CANDIDATE_FIELDS, evaluator.EV04_CASE_FIELDS),
        }
        expected_candidate_schema, expected_case_schema = schemas[arm_name]
        comparison = evaluator.compare_control_reproduction(
            root / outputs[arm["results_key"]]["path"], path["control_output"] / path["results_name"],
            root / outputs[arm["summary_key"]]["path"], path["control_output"] / path["summary_name"],
            frozen_metadata["metrics"], result["metrics"],
            expected_candidate_schema=expected_candidate_schema,
            expected_case_schema=expected_case_schema,
        )
        control[arm_name] = comparison
        return comparison

    def materialize(arm_name: str) -> Mapping[str, Any]:
        spec = specs[arm_name]
        source_bytes = gate.validate_current_text_identity(root, spec["frozen_inputs"]["corpus"], f"{arm_name} canonical corpus")
        digest = evaluator.materialize_corrective_corpus(source_bytes, paths[arm_name]["corrected_corpus"], spec["corrective_corpus"]["patches"], root=root)
        return {"status": "PASS", "corrected_corpus_sha256": digest}

    def build(arm_name: str) -> Mapping[str, Any]:
        path = paths[arm_name]
        return builder.build(arm_name, path["corrected_corpus"], path["corrected_index"], path["corrected_metadata"], root=root)

    def evaluate(arm_name: str) -> Mapping[str, Any]:
        path = paths[arm_name]
        result = evaluator.evaluate_arm(arm_name, path["corrected_corpus"], path["corrected_index"], path["corrected_metadata"], path["corrected_output"], root=root)
        corrected[arm_name] = result
        return result

    def d1a_execute() -> Mapping[str, Any]:
        nonlocal d1a_result
        d1a_result = d1a_runner.execute_authorized(root)
        return {"status": "PASS", "result": d1a_result}

    def integrity() -> Mapping[str, Any]:
        for arm_name in gate.ARMS:
            path = paths[arm_name]
            required_paths = (
                path["corrected_corpus"], path["control_index"], path["control_metadata"], path["corrected_index"], path["corrected_metadata"],
                path["control_output"] / path["results_name"], path["corrected_output"] / path["results_name"],
            )
            require(all(item.is_file() for item in required_paths), f"Required authorized artifact is missing for {arm_name}")
        return {"status": "PASS", "validated_arms": sorted(gate.ARMS)}

    def case_comparisons() -> Mapping[str, Any]:
        for arm_name, arm in gate.ARMS.items():
            spec = specs[arm_name]
            original_path = root / spec["primary_original_control"]["outputs"][arm["summary_key"]]["path"]
            corrective_path = paths[arm_name]["corrected_output"] / paths[arm_name]["summary_name"]
            case_outputs[arm_name] = _write_json_new(comparisons[arm_name][0], {
                "arm": arm_name,
                "rows": evaluator.produce_case_level_comparison(_read_csv(original_path), _read_csv(corrective_path)),
            })
        return {"status": "PASS", "arms": sorted(case_outputs)}

    def aggregate_comparisons() -> Mapping[str, Any]:
        for arm_name in gate.ARMS:
            spec = specs[arm_name]
            metadata_path = root / spec["primary_original_control"]["run_metadata"]["path"]
            original_metrics = json.loads(metadata_path.read_text(encoding="utf-8"))["metrics"]
            aggregate_outputs[arm_name] = _write_json_new(comparisons[arm_name][1], {
                "arm": arm_name,
                "metrics": evaluator.produce_aggregate_comparison(original_metrics, corrected[arm_name]["metrics"]),
            })
        return {"status": "PASS", "arms": sorted(aggregate_outputs)}

    def summary() -> Mapping[str, Any]:
        return _write_json_new(summary_path, evaluator.produce_unified_sensitivity_summary(
            {"control": control["EV03"], "corrective": corrected["EV03"], "case_comparison": case_outputs["EV03"], "aggregate_comparison": aggregate_outputs["EV03"]},
            {"control": control["EV04"], "corrective": corrected["EV04"], "case_comparison": case_outputs["EV04"], "aggregate_comparison": aggregate_outputs["EV04"]},
        ))

    def manifest() -> Mapping[str, Any]:
        return _write_json_new(manifest_path, {
            "status": "PASS",
            "execution_mode": "AUTHORIZED_UNIFIED_0B05C",
            "all_four_authorizations_required_before_side_effects": True,
            "control_reproductions": control,
            "corrected_arms": corrected,
            "d1a": {"status": "PASS", "result": d1a_result},
            "execution_order": list(PIPELINE_STEPS),
        })

    def ledger() -> Mapping[str, Any]:
        contract = gate_payload["hash_ledger_contract"]
        expected = evaluator.expected_ledger_paths(contract)
        evaluator.write_hash_ledger(ledger_path, contract, root=root)
        return {"status": "PASS", "expected_ledger_paths": len(expected)}

    return {
        "authorized_preflight": authorized_preflight,
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
        "d1a_execute": d1a_execute,
        "integrity": integrity,
        "case_comparisons": case_comparisons,
        "aggregate_comparisons": aggregate_comparisons,
        "summary": summary,
        "manifest": manifest,
        "ledger": ledger,
        "final_state": lambda: {"status": "PASS", "state": "COMPLETED"},
    }


def execute_authorized(root: Path = ROOT) -> dict[str, Any]:
    """Execute only after all four independently audited authorizations pass."""

    proof = preflight_authorized(root)
    return run_authorized_pipeline(_default_operations(root, proof))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="0B-05C corrective numerical execution runner.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--execute-authorized", action="store_true")
    args = parser.parse_args(argv)
    if args.execute_authorized:
        print(json.dumps(execute_authorized(ROOT), ensure_ascii=False, sort_keys=True))
        return 0
    print(json.dumps(preflight_not_authorized(ROOT), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
