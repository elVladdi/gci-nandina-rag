"""Build and validate the closed 0B-05C numerical gate v0.2."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[2]
BASE_COMMIT = "43291c312c2934aae03f3c087dd0a1ae594341b7"
AUDIT_ROOT = Path("outputs/audits/0b05c_corrective_numerical_gate_v0.2")
RECOVERY_ROOT = Path("outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2")
V01_ROOT = Path("outputs/audits/0b05c_corrective_numerical_gate_v0.1")
D1A_V01_SPEC = Path("outputs/audits/d1a_preexecution_0b05c_v0.1/d1a_0b05c_corrective_execution_spec_v0.1.json")

ARTIFACT_NAMES = (
    "ev03_numerical_execution_spec_v0.2.json",
    "ev04_numerical_execution_spec_v0.2.json",
    "d1a_numerical_execution_spec_v0.2.json",
    "0b05c_corrective_numerical_execution_gate_v0.2.json",
    "0b05c_corrective_numerical_gate_manifest_v0.2.json",
    "0b05c_corrective_numerical_gate_hash_ledger_v0.2.json",
)
GATE_PATH = AUDIT_ROOT / ARTIFACT_NAMES[3]
AUTHORIZATION_RECORD = AUDIT_ROOT / "0b05c_numerical_authorization_record_v0.2.json"
AUTHORIZED_GATE_STATUS = "APPROVED / INTEGRATED"
AUTHORIZED_READINESS = "AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION"
AUTHORIZATION_BASELINE_ARTIFACTS = {
    "unified_gate": (AUDIT_ROOT / ARTIFACT_NAMES[3]).as_posix(),
    "ev03_spec": (AUDIT_ROOT / ARTIFACT_NAMES[0]).as_posix(),
    "ev04_spec": (AUDIT_ROOT / ARTIFACT_NAMES[1]).as_posix(),
    "d1a_spec": (AUDIT_ROOT / ARTIFACT_NAMES[2]).as_posix(),
}

AUTHORIZATION = {
    "EV03_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "EV04_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "UNIFIED_0B05C_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "corrective_retrieval_executed": False,
    "corrective_metrics_computed": False,
    "authorization_record_present": False,
    "runtime_authorization_record_present": False,
}
SCIENTIFIC_STATE = {
    "0B05C_METRIC_IMPACT": "NOT_DETERMINED",
    "DOWNSTREAM_REEXECUTION": "NOT_YET_JUSTIFIED",
    "0B05C_CLOSURE": "NOT_AUTHORIZED",
}

EV03_ROOTS = (
    "data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.2",
    "outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.2",
    "data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.2.jsonl",
    "data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.2",
    "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.2",
)
EV04_ROOTS = (
    "data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.2",
    "outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.2",
    "data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.2.jsonl",
    "data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.2",
    "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.2",
)
D1A_ROOTS = (
    "data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.2.jsonl",
    "data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.2",
    "outputs/evaluation/d1a_corrective_0b05c_v0.2",
    "outputs/audits/d1a_corrective_0b05c_runtime_v0.2",
)
UNIFIED_ROOTS = (
    "outputs/evaluation/0b05c_corrective_numerical_v0.2",
    "outputs/audits/0b05c_corrective_numerical_runtime_v0.2",
)
FUTURE_ROOTS = EV03_ROOTS + EV04_ROOTS + D1A_ROOTS + UNIFIED_ROOTS

V01_ROOTS = (
    "data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.1",
    "outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1",
    "data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.1.jsonl",
    "data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.1",
    "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.1",
    "data/processed/indexes/bm25_nandina8_hierarchical_ev04_decision885_control_v0.1",
    "outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.1",
    "data/processed/corpus_nandina_hierarchical_ev04_corrective_decision906_v0.1.jsonl",
    "data/processed/indexes/bm25_nandina8_hierarchical_ev04_corrective_decision906_v0.1",
    "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.1",
    "data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.1.jsonl",
    "data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.1",
    "outputs/evaluation/text2trade_mnrl_d1a_corrective_sensitivity_v0.1",
    "outputs/audits/d1a_corrective_0b05c_runtime_v0.1",
    "outputs/evaluation/0b05c_corrective_numerical_v0.1",
)

PIPELINE_STEPS = (
    "01_unified_preflight",
    "02_EV03_Decision885_control_reproduction",
    "03_EV03_control_reproduction_verification",
    "04_EV03_corrected_corpus_materialization",
    "05_EV03_corrected_index_build_RECOVERED_HISTORICAL_SEMANTICS",
    "06_EV03_corrected_evaluation",
    "07_EV04_Decision885_control_reproduction",
    "08_EV04_control_reproduction_verification",
    "09_EV04_corrected_corpus_materialization",
    "10_EV04_corrected_index_build",
    "11_EV04_corrected_evaluation",
    "12_D1a_corrected_execution_under_v02_authorization",
    "13_integrity_validation",
    "14_case_level_comparisons",
    "15_aggregate_comparisons",
    "16_unified_sensitivity_summary",
    "17_execution_manifest",
    "18_exact_hash_ledger",
    "19_final_completion_state",
)

VERSIONED_PATHS = (
    "src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py",
    "src/experiments/build_bm25_corrective_0b05c_v02.py",
    "src/experiments/run_0b05c_corrective_numerical_v02.py",
    "src/experiments/run_d1a_corrective_0b05c_v02.py",
    "src/experiments/build_bm25_ev03_historical_recovered_v02.py",
    "src/experiments/verify_ev03_historical_builder_recovery_v02.py",
    "src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py",
    "src/experiments/build_bm25_index.py",
    "src/experiments/build_bm25_hierarchical_index.py",
    "src/experiments/evaluate_normative_bm25_flat_data_aduanas_v02.py",
    "src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py",
    "src/experiments/build_text2trade_mnrl_index_v02.py",
    "src/experiments/evaluate_text2trade_mnrl_data_aduanas_v02.py",
    "src/retrieval/bm25.py",
    "src/retrieval/text2trade_mnrl_v02.py",
    "src/bm25_index.py",
    "src/configs/experiment_config.json",
    "src/configs/text2trade_mnrl_v0.2.json",
    "data/processed/corpus_rag_v1_index.jsonl",
    "data/processed/corpus_nandina_hierarchical_v0.1.jsonl",
    "data/processed/data_aduanas_evalset_clase87_v0.2.csv",
    "data/processed/indexes/bm25_nandina8_run_metadata.json",
    "data/processed/indexes/text2trade_mnrl_nandina8_v0.2/retrieval_config.json",
    "data/processed/indexes/text2trade_mnrl_nandina8_v0.2/text2trade_mnrl_nandina8_v02_run_metadata.json",
    "data/processed/indexes/text2trade_mnrl_nandina8_v0.2/vector_integrity_gate_v0.2.json",
    "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv",
    "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv",
    "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/run_metadata.json",
    "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_results.csv",
    "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv",
    "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json",
    "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json",
    "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_case_summary.csv",
    "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_ranked_codes_top200.jsonl",
)
BINARY_PATHS = (
    "data/processed/indexes/bm25_nandina8.pkl",
)
MODEL_IDENTITY = {
    "path": "models/text2trade_mnrl_v0.2/model.safetensors",
    "classification": "FROZEN_FILE_IDENTITY",
    "size_bytes": 470637416,
    "sha256": "ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87",
    "current_checkout_presence_required": False,
}


class ContractViolation(RuntimeError):
    """Raised before side effects when the frozen contract is not satisfied."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractViolation(message)


def _git(root: Path, *args: str, binary: bool = False) -> bytes | str:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=not binary,
    )
    return result.stdout if binary else result.stdout.strip()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(root: Path, relative: Path | str) -> dict[str, Any]:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def canonical_json_bytes(payload: Mapping[str, Any]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def git_binding(root: Path, path: str, revision: str, classification: str = "VERSIONED_GIT_BLOB") -> dict[str, Any]:
    object_name = f":{path}" if revision == "INDEX" else f"{revision}:{path}"
    blob = str(_git(root, "rev-parse", object_name))
    data = _git(root, "cat-file", "blob", blob, binary=True)
    assert isinstance(data, bytes)
    return {
        "path": path,
        "classification": classification,
        "git_blob_sha1": blob,
        "canonical_git_blob_sha256": sha256_bytes(data),
        "canonical_size_bytes": len(data),
    }


def dependency_bindings(root: Path, revision: str) -> list[dict[str, Any]]:
    bindings = [git_binding(root, path, revision) for path in VERSIONED_PATHS]
    bindings.extend(git_binding(root, path, revision, "FROZEN_BINARY_GIT_BLOB") for path in BINARY_PATHS)
    bindings.append(dict(MODEL_IDENTITY))
    return bindings


def authorization_record_contract() -> dict[str, Any]:
    return {
        "record_path": AUTHORIZATION_RECORD.as_posix(),
        "artifact_id": "0b05c_numerical_authorization_record_v0.2",
        "schema_version": 2,
        "required_keys": [
            "artifact_id",
            "schema_version",
            "authorization_baseline_commit",
            "baseline_external_audit",
            "baseline_artifacts",
        ],
        "baseline_artifact_paths": dict(AUTHORIZATION_BASELINE_ARTIFACTS),
        "baseline_identity_fields": [
            "path",
            "git_blob_sha1",
            "canonical_git_blob_sha256",
            "canonical_size_bytes",
        ],
        "required_baseline_external_audit": "PASS / APPROVED_FOR_INTEGRATION",
        "baseline_commit_policy": "MUST_BE_A_PROPER_ANCESTOR_OF_HEAD",
    }


def authorization_snapshot(
    gate_payload: Mapping[str, Any],
    ev03_spec: Mapping[str, Any],
    ev04_spec: Mapping[str, Any],
    d1a_spec: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "gate": copy.deepcopy(dict(gate_payload)),
        "EV03": copy.deepcopy(dict(ev03_spec)),
        "EV04": copy.deepcopy(dict(ev04_spec)),
        "D1a": copy.deepcopy(dict(d1a_spec)),
    }


def immutable_authorization_projection(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    payload = copy.deepcopy(dict(snapshot))
    payload["gate"]["gate_status"] = "__AUTHORIZED_TRANSITION__"
    payload["gate"]["authorization_readiness"] = "__AUTHORIZED_TRANSITION__"
    for name in ("EV03", "EV04", "D1A", "UNIFIED_0B05C"):
        field = f"{name}_NUMERICAL_EXECUTION"
        require(field in payload["gate"]["authorization"], f"Missing gate authorization field: {field}")
        payload["gate"]["authorization"][field] = "__AUTHORIZED_TRANSITION__"
    require("authorization_record_present" in payload["gate"]["authorization"], "Missing authorization record state")
    payload["gate"]["authorization"]["authorization_record_present"] = "__AUTHORIZED_TRANSITION__"
    for arm in ("EV03", "EV04"):
        field = f"{arm}_NUMERICAL_EXECUTION"
        require(field in payload[arm]["authorization"], f"Missing {arm} authorization field")
        payload[arm]["authorization"][field] = "__AUTHORIZED_TRANSITION__"
    require("D1A_NUMERICAL_EXECUTION" in payload["D1a"]["authorization"], "Missing D1a authorization field")
    payload["D1a"]["authorization"]["D1A_NUMERICAL_EXECUTION"] = "__AUTHORIZED_TRANSITION__"
    return payload


def validate_authorization_transition(
    baseline: Mapping[str, Any],
    candidate: Mapping[str, Any],
    *,
    require_authorized: bool = True,
) -> None:
    require(
        immutable_authorization_projection(baseline) == immutable_authorization_projection(candidate),
        "Authorization candidate changed immutable scientific or execution content",
    )
    baseline_gate = baseline["gate"]
    candidate_gate = candidate["gate"]
    require(baseline_gate["gate_status"] == "CANDIDATE_PENDING_EXTERNAL_AUDIT", "Authorization baseline gate status changed")
    require(baseline_gate["authorization_readiness"] == "NOT_AUTHORIZATION_READY", "Authorization baseline readiness changed")
    target = "AUTHORIZED" if require_authorized else "NOT_AUTHORIZED"
    if require_authorized:
        require(candidate_gate["gate_status"] == AUTHORIZED_GATE_STATUS, "Authorized gate is not approved and integrated")
        require(candidate_gate["authorization_readiness"] == AUTHORIZED_READINESS, "Authorized gate readiness is invalid")
    for name in ("EV03", "EV04", "D1A", "UNIFIED_0B05C"):
        field = f"{name}_NUMERICAL_EXECUTION"
        require(baseline_gate["authorization"].get(field) == "NOT_AUTHORIZED", f"Baseline is not closed: {field}")
        require(candidate_gate["authorization"].get(field) == target, f"Authorization transition is invalid: {field}")
    for arm in ("EV03", "EV04"):
        field = f"{arm}_NUMERICAL_EXECUTION"
        require(baseline[arm]["authorization"].get(field) == "NOT_AUTHORIZED", f"Baseline spec is not closed: {field}")
        require(candidate[arm]["authorization"].get(field) == target, f"Authorized spec state is invalid: {field}")
    require(baseline["D1a"]["authorization"].get("D1A_NUMERICAL_EXECUTION") == "NOT_AUTHORIZED", "Baseline D1a spec is not closed")
    require(candidate["D1a"]["authorization"].get("D1A_NUMERICAL_EXECUTION") == target, "Authorized D1a spec state is invalid")
    require(baseline_gate["authorization"].get("authorization_record_present") is False, "Baseline authorization record state is not closed")
    require(candidate_gate["authorization"].get("authorization_record_present") is require_authorized, "Authorization record state is invalid")


def _git_json(root: Path, revision: str, path: str) -> dict[str, Any]:
    raw = _git(root, "show", f"{revision}:{path}", binary=True)
    assert isinstance(raw, bytes)
    payload = json.loads(raw.decode("utf-8"))
    require(isinstance(payload, dict), f"Git JSON is not an object: {revision}:{path}")
    return payload


def load_authorization_transition_from_git(root: Path, gate_payload: Mapping[str, Any]) -> dict[str, Any]:
    contract = gate_payload.get("authorization_transition_schema", {}).get("authorization_record")
    require(isinstance(contract, Mapping), "Authorization record contract is missing")
    record_path = str(contract.get("record_path", ""))
    require(record_path == AUTHORIZATION_RECORD.as_posix(), "Authorization record path changed")
    record = _git_json(root, "HEAD", record_path)
    require(set(record) == set(contract["required_keys"]), "Authorization record schema changed")
    require(record.get("artifact_id") == contract["artifact_id"], "Authorization record identity changed")
    require(record.get("schema_version") == contract["schema_version"], "Authorization record version changed")
    require(record.get("baseline_external_audit") == contract["required_baseline_external_audit"], "Authorization baseline is not externally approved")
    baseline_commit = record.get("authorization_baseline_commit")
    require(isinstance(baseline_commit, str) and re.fullmatch(r"[0-9a-f]{40}", baseline_commit) is not None, "Authorization baseline commit is malformed")
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", baseline_commit, "HEAD"], cwd=root).returncode == 0
    require(ancestor and baseline_commit != str(_git(root, "rev-parse", "HEAD")), "Authorization baseline must be a proper ancestor of HEAD")
    identities = record.get("baseline_artifacts")
    require(isinstance(identities, Mapping) and set(identities) == set(AUTHORIZATION_BASELINE_ARTIFACTS), "Authorization baseline artifact set changed")
    for key, path in AUTHORIZATION_BASELINE_ARTIFACTS.items():
        expected = git_binding(root, path, baseline_commit)
        expected.pop("classification")
        require(identities.get(key) == expected, f"Authorization baseline binding mismatch: {key}")

    def snapshot(revision: str) -> dict[str, Any]:
        return authorization_snapshot(
            _git_json(root, revision, AUTHORIZATION_BASELINE_ARTIFACTS["unified_gate"]),
            _git_json(root, revision, AUTHORIZATION_BASELINE_ARTIFACTS["ev03_spec"]),
            _git_json(root, revision, AUTHORIZATION_BASELINE_ARTIFACTS["ev04_spec"]),
            _git_json(root, revision, AUTHORIZATION_BASELINE_ARTIFACTS["d1a_spec"]),
        )

    baseline = snapshot(baseline_commit)
    candidate = snapshot("HEAD")
    require(candidate["gate"] == gate_payload, "Authorized gate is not the committed HEAD artifact")
    validate_authorization_transition(baseline, candidate)
    return {"record": record, "baseline_commit": baseline_commit, "baseline": baseline, "candidate": candidate}


def _patch_spec(spec: dict[str, Any], arm: str) -> dict[str, Any]:
    result = copy.deepcopy(spec)
    result["specification_id"] = f"{arm.lower()}_numerical_execution_spec_v0.2"
    result["specification_status"] = "CLOSED_PROSPECTIVELY/CANDIDATE_PENDING_EXTERNAL_AUDIT"
    result["authorization"] = {
        f"{arm}_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
        "corrective_metrics_computed": False,
        "corrective_retrieval_executed": False,
    }
    execution = result["prospective_execution"]
    if arm == "EV03":
        roots = EV03_ROOTS
        result["methodology"] = {
            "token_policy": "DROP_SINGLE_CHARACTER_TOKENS",
            "builder": "src/experiments/build_bm25_ev03_historical_recovered_v02.py",
            "global_builder_direct_use_for_ev03": False,
            "k1": 1.5,
            "b": 0.75,
            "ranking_depth": 100,
        }
        result["required_control"] = {
            "status": "PASS_EXACT",
            "logical_index_identity": "EXACT",
            "ranking_rows": 50327,
            "cases": 1056,
            "ranking_sha256": "d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015",
            "case_summary_sha256": "f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0",
            "ranking_bytes_exact": True,
            "case_summary_bytes_exact": True,
            "metric_table_exact": True,
            "full_metrics_exact": True,
        }
    else:
        roots = EV04_ROOTS
        result["methodology"] = {
            "token_policy": "ORIGINAL_HIERARCHICAL_V0.1",
            "inherits_ev03_drop_single_character_tokens": False,
            "text_field": "texto_index_jerarquico",
            "fallback_text_field": "texto_index",
            "collapse": "FIRST_OCCURRENCE_PER_UNIQUE_NANDINA8_CODE",
            "ranking_depth": 200,
            "k1": 1.5,
            "b": 0.75,
        }
        result["required_control"] = {
            "status": "PASS_EXACT",
            "mandatory": True,
            "reason": "ORIGINAL_IDENTITY_NOT_VERIFIABLE_FROM_FROZEN_ARTIFACTS",
            "ranking_sha256": "fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662",
            "case_summary_sha256": "17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634",
        }
    result["corrective_corpus"]["prospective_path"] = roots[2]
    execution["control_reproduction_index_root"] = roots[0]
    execution["control_reproduction_output_root"] = roots[1]
    execution["corrected_index_root"] = roots[3]
    execution["corrected_output_root"] = roots[4]
    execution["full_rebuild_policy"] = "FULL_NON_DESTRUCTIVE_REBUILD_NO_OVERWRITE_NO_RESUME"
    execution["unified_runner"] = "src/experiments/run_0b05c_corrective_numerical_v02.py"
    execution["future_roots"] = list(roots)
    execution["control_must_pass_before_corrected_arm"] = "PASS_EXACT"
    prefix = arm.lower()
    corpus = result["frozen_inputs"]["corpus"]["path"]
    execution["commands"] = {
        "d1a_execute_command": "python -m src.experiments.run_d1a_corrective_0b05c_v02 --execute-authorized",
        f"{prefix}_control_reproduction_build_command": (
            f"python -m src.experiments.build_bm25_corrective_0b05c_v02 --arm {arm} --corpus {corpus} "
            f"--output {roots[0]}/index.pkl --metadata {roots[0]}/index_metadata.json"
        ),
        f"{prefix}_control_reproduction_evaluate_command": (
            f"python -m src.experiments.evaluate_normative_bm25_corrective_0b05c_v01 --arm {arm} --corpus {corpus} "
            f"--index {roots[0]}/index.pkl --index-metadata {roots[0]}/index_metadata.json --output-dir {roots[1]}"
        ),
        f"{prefix}_corrected_build_command": (
            f"python -m src.experiments.build_bm25_corrective_0b05c_v02 --arm {arm} --corpus {roots[2]} "
            f"--output {roots[3]}/index.pkl --metadata {roots[3]}/index_metadata.json"
        ),
        f"{prefix}_corrected_evaluate_command": (
            f"python -m src.experiments.evaluate_normative_bm25_corrective_0b05c_v01 --arm {arm} --corpus {roots[2]} "
            f"--index {roots[3]}/index.pkl --index-metadata {roots[3]}/index_metadata.json --output-dir {roots[4]}"
        ),
        "unified_execution_command": "python -m src.experiments.run_0b05c_corrective_numerical_v02 --execute-authorized",
    }
    return result


def _replace_strings(value: Any, replacements: Mapping[str, str]) -> Any:
    if isinstance(value, str):
        for old, new in replacements.items():
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [_replace_strings(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: _replace_strings(item, replacements) for key, item in value.items()}
    return value


def _d1a_spec(root: Path, revision: str) -> dict[str, Any]:
    result = copy.deepcopy(read_json(root, D1A_V01_SPEC))
    result = _replace_strings(result, {
        "data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.1.jsonl": D1A_ROOTS[0],
        "data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.1": D1A_ROOTS[1],
        "outputs/evaluation/text2trade_mnrl_d1a_corrective_sensitivity_v0.1": D1A_ROOTS[2],
        "outputs/audits/d1a_corrective_0b05c_runtime_v0.1": D1A_ROOTS[3],
        "d1a_corrective_vs_original_comparison_v0.1.json": "d1a_corrective_vs_original_comparison_v0.2.json",
        "d1a_corrective_case_level_comparison_v0.1.jsonl": "d1a_corrective_case_level_comparison_v0.2.jsonl",
        "d1a_corrective_output_hash_ledger_v0.1.csv": "d1a_corrective_output_hash_ledger_v0.2.csv",
        "d1a_corrective_execution_manifest_v0.1.json": "d1a_corrective_execution_manifest_v0.2.json",
    })
    result["specification_id"] = "d1a_numerical_execution_spec_v0.2"
    result["specification_status"] = "CLOSED_PROSPECTIVELY/CANDIDATE_PENDING_EXTERNAL_AUDIT"
    result["authorization"] = {
        "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
        "D1A_CORRECTIVE_CORPUS_CREATED": False,
        "D1A_CORRECTIVE_INDEX_CREATED": False,
        "D1A_CORRECTIVE_METRICS_COMPUTED": False,
    }
    result["model_policy"]["MODEL_POLICY"] = "FREEZE_ORIGINAL_D1A_WEIGHTS"
    result["model_policy"]["must_not_retrain"] = True
    result["index_builder"]["policy"] = "FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD"
    result["index_builder"]["prospective_output_root"] = D1A_ROOTS[1]
    result["evaluation"]["ranking_depth"] = 200
    result["evaluation"]["prospective_output_root"] = D1A_ROOTS[2]
    runner_binding = git_binding(root, "src/experiments/run_d1a_corrective_0b05c_v02.py", revision)
    result["orchestration"]["runner"] = {
        "path": runner_binding["path"],
        "revision": "COMMITTED_GIT_BLOB",
        "git_blob_sha": runner_binding["git_blob_sha1"],
        "canonical_blob_sha256": runner_binding["canonical_git_blob_sha256"],
    }
    result["orchestration"]["future_roots"] = list(D1A_ROOTS)
    result["orchestration"]["runtime_root"] = D1A_ROOTS[3]
    result["orchestration"]["preflight_command"] = "python -B -m src.experiments.run_d1a_corrective_0b05c_v02 --preflight"
    result["orchestration"]["future_authorized_execution_command"] = "python -B -m src.experiments.run_d1a_corrective_0b05c_v02 --execute-authorized"
    result["v01_classification"] = "HISTORICAL / INTEGRATED / SUPERSEDED_FOR_NEW_EXECUTION"
    return result


def expected_runtime_ledger_paths(ev03: Mapping[str, Any], ev04: Mapping[str, Any], d1a: Mapping[str, Any]) -> list[str]:
    expected: set[str] = set()
    for arm, spec in (("EV03", ev03), ("EV04", ev04)):
        execution = spec["prospective_execution"]
        prefix = "normative_flat" if arm == "EV03" else "normative_hierarchical"
        for index_root in (execution["control_reproduction_index_root"], execution["corrected_index_root"]):
            expected.update({f"{index_root}/index.pkl", f"{index_root}/index_metadata.json"})
        for output_root in (execution["control_reproduction_output_root"], execution["corrected_output_root"]):
            expected.update({
                f"{output_root}/{prefix}_results.csv",
                f"{output_root}/{prefix}_case_summary.csv",
                f"{output_root}/{prefix}_metrics.json",
            })
        expected.add(spec["corrective_corpus"]["prospective_path"])
    d1a_contract = d1a["orchestration"]["hash_ledger_contract"]
    expected.update(d1a_contract["included_paths"])
    expected.add(d1a_contract["excluded_self_path"])
    evaluation_root, runtime_root = UNIFIED_ROOTS
    expected.update({
        f"{evaluation_root}/ev03_case_level_comparison_v0.2.json",
        f"{evaluation_root}/ev03_aggregate_comparison_v0.2.json",
        f"{evaluation_root}/ev04_case_level_comparison_v0.2.json",
        f"{evaluation_root}/ev04_aggregate_comparison_v0.2.json",
        f"{evaluation_root}/unified_sensitivity_summary_v0.2.json",
        f"{runtime_root}/runtime_authorization_record_v0.2.json",
        f"{runtime_root}/execution_manifest_v0.2.json",
    })
    return sorted(expected)


def build_bundle(root: Path = ROOT, revision: str = "HEAD") -> dict[str, Any]:
    ev03_v01 = read_json(root, V01_ROOT / "ev03_corrective_execution_spec_v0.1.json")
    ev04_v01 = read_json(root, V01_ROOT / "ev04_corrective_execution_spec_v0.1.json")
    ev03 = _patch_spec(ev03_v01, "EV03")
    ev04 = _patch_spec(ev04_v01, "EV04")
    d1a = _d1a_spec(root, revision)
    bindings = dependency_bindings(root, revision)
    runtime_ledger_path = f"{UNIFIED_ROOTS[1]}/exact_hash_ledger_v0.2.json"
    gate = {
        "gate_id": "0b05c_corrective_numerical_execution_gate_v0.2",
        "gate_version": "v0.2",
        "gate_status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
        "gate_scope": "UNIFIED_0B05C_NUMERICAL_PREEXECUTION",
        "authorization_readiness": "NOT_AUTHORIZATION_READY",
        "base_commit": BASE_COMMIT,
        "authorization": dict(AUTHORIZATION),
        "scientific_state": dict(SCIENTIFIC_STATE),
        "pipeline_steps": list(PIPELINE_STEPS),
        "future_roots": list(FUTURE_ROOTS),
        "v01_roots": {"classification": "HISTORICAL / INTEGRATED / SUPERSEDED_FOR_NEW_EXECUTION", "paths": list(V01_ROOTS)},
        "ev03_recovery": {
            "EV03_HISTORICAL_RECOVERY_V02": "APPROVED/VERSIONED/INTEGRATED",
            "LOGICAL_INDEX_IDENTITY": "EXACT",
            "EV03_DECISION885_CONTROL_REPRODUCTION": "PASS_EXACT",
            "methodology": "HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED",
            "AUTHENTIC_HISTORICAL_SOURCE_PY": "NOT_VERSIONED_AT_INDEX_CREATION",
            "token_policy": "DROP_SINGLE_CHARACTER_TOKENS",
        },
        "execution_contract": {
            "no_side_effect_before_four_authorizations": True,
            "no_retry": True,
            "no_resume": True,
            "no_overwrite": True,
            "final_completion_requires_previous_18_pass": True,
        },
        "authorization_transition_schema": {
            "future_separate_audited_block_required": True,
            "required_authorized_gate_status": AUTHORIZED_GATE_STATUS,
            "required_authorized_readiness": AUTHORIZED_READINESS,
            "allowed_gate_fields": ["gate_status", "authorization_readiness", "authorization.*_NUMERICAL_EXECUTION", "authorization.authorization_record_present"],
            "allowed_spec_fields": ["authorization.EV03_NUMERICAL_EXECUTION", "authorization.EV04_NUMERICAL_EXECUTION", "authorization.D1A_NUMERICAL_EXECUTION"],
            "forbidden_changes": ["patches", "roots", "commands", "ranking_semantics", "metric_contracts", "builders", "evaluators", "model_policy", "code_bindings", "execution_order", "comparison_schema"],
            "authorization_record": authorization_record_contract(),
            "runtime_authorization_record_created_only_by_future_authorized_execution": True,
        },
        "runtime_hash_ledger_contract": {
            "expected_paths": expected_runtime_ledger_paths(ev03, ev04, d1a),
            "discovery_roots": list(FUTURE_ROOTS),
            "excluded_self_path": runtime_ledger_path,
            "missing_or_unexpected_policy": "FAIL_CLOSED",
            "entry_fields": ["path", "sha256", "size_bytes"],
        },
        "runtime_authorization_provenance_contract": {
            "record_path": f"{UNIFIED_ROOTS[1]}/runtime_authorization_record_v0.2.json",
            "record_required_fields": [
                "status",
                "mode",
                "execution_authorization_commit",
                "authorization_baseline_commit",
                "authorization",
                "authorization_record",
                "baseline_external_audit",
                "authorized_artifacts",
            ],
            "authorization_record_reference_fields": ["path", "git_blob_sha1", "canonical_git_blob_sha256", "canonical_size_bytes"],
            "authorized_artifact_keys": ["unified_gate", "ev03_spec", "ev04_spec", "d1a_spec"],
            "manifest_reference_fields": ["path", "sha256", "size_bytes"],
            "source": "VALIDATED_COMMITTED_GIT_BLOBS_AT_AUTHORIZATION_HEAD",
        },
        "dependency_bindings": bindings,
        "authorization_record_path": AUTHORIZATION_RECORD.as_posix(),
    }
    manifest = {
        "artifact_id": "0b05c_corrective_numerical_gate_manifest_v0.2",
        "explicit_non_executed_state": dict(AUTHORIZATION),
        "frozen_inputs": [item for item in bindings if item["path"].startswith(("data/", "outputs/evaluation/", "models/"))],
        "code_bindings": [item for item in bindings if item["path"].startswith("src/")],
        "control_baselines": {"EV03": ev03["required_control"], "EV04": ev04["required_control"], "D1A": d1a["evaluation"]["primary_control"]},
        "future_execution_roots": list(FUTURE_ROOTS),
        "gate_audit_root": AUDIT_ROOT.as_posix(),
        "future_runtime_audit_roots": [D1A_ROOTS[3], UNIFIED_ROOTS[1]],
        "generated_at_future_runtime_outputs": {"classification": "FUTURE_GENERATED_OUTPUT_NOT_PRESENT", "paths": list(FUTURE_ROOTS)},
    }
    ledger_entries = list(bindings) + [
        {"path": path, "classification": "FUTURE_GENERATED_OUTPUT_NOT_PRESENT", "status": "ABSENT / NOT_GENERATED"}
        for path in FUTURE_ROOTS
    ]
    ledger = {
        "artifact_id": "0b05c_corrective_numerical_gate_hash_ledger_v0.2",
        "canonical_hash_method": "SHA256_OF_GIT_CAT_FILE_BLOB_BYTES",
        "entries": ledger_entries,
        "mismatch_count": 0,
        "future_hashes_invented": False,
    }
    return {"ev03": ev03, "ev04": ev04, "d1a": d1a, "gate": gate, "manifest": manifest, "ledger": ledger}


def write_artifacts(root: Path = ROOT, revision: str = "INDEX") -> dict[str, Any]:
    target = root / AUDIT_ROOT
    require(not target.exists(), f"Gate audit root already exists: {AUDIT_ROOT.as_posix()}")
    bundle = build_bundle(root, revision)
    target.mkdir(parents=True)
    payloads = (bundle["ev03"], bundle["ev04"], bundle["d1a"], bundle["gate"], bundle["manifest"], bundle["ledger"])
    for name, payload in zip(ARTIFACT_NAMES, payloads, strict=True):
        with (target / name).open("xb") as handle:
            handle.write(canonical_json_bytes(payload))
    return {"status": "PASS", "created": [str(AUDIT_ROOT / name) for name in ARTIFACT_NAMES]}


def _validate_recovery(root: Path) -> None:
    gate = read_json(root, RECOVERY_ROOT / "0b05c_corrective_numerical_gate_v0.2.json")
    control = read_json(root, RECOVERY_ROOT / "ev03_decision885_control_reproduction_v0.2.json")
    logical = read_json(root, RECOVERY_ROOT / "ev03_logical_index_identity_v0.2.json")
    require(gate["ev03_recovery"]["token_policy"] == "DROP_SINGLE_CHARACTER_TOKENS", "Recovered EV03 token policy drift")
    require(control["EV03_DECISION885_CONTROL_REPRODUCTION"] == "PASS_EXACT", "EV03 control recovery is not PASS_EXACT")
    require(logical["LOGICAL_INDEX_IDENTITY"] == "EXACT", "EV03 logical index identity is not EXACT")


def preflight(root: Path = ROOT, *, revision: str = "HEAD", require_clean: bool = True) -> dict[str, Any]:
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", BASE_COMMIT, "HEAD"], cwd=root).returncode == 0
    require(ancestor, f"Required base {BASE_COMMIT} is not an ancestor of HEAD")
    if require_clean:
        require(str(_git(root, "status", "--short", "--untracked-files=no")) == "", "Tracked working tree is not clean")
    _validate_recovery(root)
    require(not (root / AUTHORIZATION_RECORD).exists(), "Authorization record v0.2 must be absent")
    for relative in FUTURE_ROOTS:
        require(not (root / relative).exists(), f"Future numerical root already exists: {relative}")
    for relative in V01_ROOTS:
        require("v0.1" in relative, f"Malformed historical v0.1 root: {relative}")
    require(set(FUTURE_ROOTS).isdisjoint(V01_ROOTS), "v0.2 roots collide with v0.1 evidence roots")
    for name in ARTIFACT_NAMES:
        require((root / AUDIT_ROOT / name).is_file(), f"Missing gate artifact: {name}")
    actual = {
        key: read_json(root, AUDIT_ROOT / name)
        for key, name in zip(("ev03", "ev04", "d1a", "gate", "manifest", "ledger"), ARTIFACT_NAMES, strict=True)
    }
    expected = build_bundle(root, revision)
    require(actual == expected, "Gate artifacts differ from canonical generated contract")
    gate = actual["gate"]
    require(gate["authorization"] == AUTHORIZATION, "Candidate authorization state is not closed")
    require(gate["authorization_readiness"] == "NOT_AUTHORIZATION_READY", "Candidate unexpectedly became authorization-ready")
    require(gate["scientific_state"] == SCIENTIFIC_STATE, "Scientific state drift")
    for binding in gate["dependency_bindings"]:
        if binding["classification"] == "FROZEN_FILE_IDENTITY":
            continue
        require(git_binding(root, binding["path"], revision, binding["classification"]) == binding, f"Canonical binding mismatch: {binding['path']}")
    require(actual["ledger"]["mismatch_count"] == 0, "Hash ledger mismatch")
    return {
        "status": "PASS",
        "mode": "PREEXECUTION_CLOSED_READONLY",
        "authorization_readiness": "NOT_AUTHORIZATION_READY",
        "numerical_execution_occurred": False,
        "corrective_retrieval_executed": False,
        "corrective_metrics_computed": False,
        "future_roots_present": False,
        "binding_count": len(gate["dependency_bindings"]),
        "bundle": actual,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write-artifacts", action="store_true")
    group.add_argument("--preflight", action="store_true")
    args = parser.parse_args(argv)
    result = write_artifacts(ROOT) if args.write_artifacts else preflight(ROOT)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
