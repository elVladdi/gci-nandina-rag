"""Build and validate the closed 0B-05C numerical gate v0.2."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
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

AUTHORIZATION = {
    "EV03_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "EV04_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "D1A_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "UNIFIED_0B05C_NUMERICAL_EXECUTION": "NOT_AUTHORIZED",
    "corrective_retrieval_executed": False,
    "corrective_metrics_computed": False,
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
    execution["commands"] = {
        key: value.replace("run_d1a_corrective_0b05c_v01", "run_d1a_corrective_0b05c_v02")
        .replace("build_bm25_corrective_0b05c_v01", "build_bm25_corrective_0b05c_v02")
        .replace("run_0b05c_corrective_numerical_v01", "run_0b05c_corrective_numerical_v02")
        .replace("v0.1", "v0.2")
        for key, value in execution["commands"].items()
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


def build_bundle(root: Path = ROOT, revision: str = "HEAD") -> dict[str, Any]:
    ev03_v01 = read_json(root, V01_ROOT / "ev03_corrective_execution_spec_v0.1.json")
    ev04_v01 = read_json(root, V01_ROOT / "ev04_corrective_execution_spec_v0.1.json")
    ev03 = _patch_spec(ev03_v01, "EV03")
    ev04 = _patch_spec(ev04_v01, "EV04")
    d1a = _d1a_spec(root, revision)
    bindings = dependency_bindings(root, revision)
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
            "required_current_gate_status": "APPROVED / INTEGRATED",
            "required_four_state_transition": "NOT_AUTHORIZED -> AUTHORIZED / NOT_EXECUTED",
            "runtime_authorization_record_created_only_by_future_authorized_execution": True,
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
