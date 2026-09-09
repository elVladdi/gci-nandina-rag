"""Build and validate the closed 0B-05C recovery gate v0.3."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[2]
BASE_COMMIT = "60aa7dd8715962f3c3e8b617e8797532529f39ed"
AUDIT_ROOT = Path("outputs/audits/0b05c_corrective_numerical_gate_v0.3")
V02_AUDIT_ROOT = Path("outputs/audits/0b05c_corrective_numerical_gate_v0.2")
FAILURE_RECORD = Path("outputs/audits/0b05c_attempt03_failclosed_v0.2/attempt03_failure_record_v0.2.json")

ARTIFACT_NAMES = (
    "ev03_numerical_execution_spec_v0.3.json",
    "ev04_numerical_execution_spec_v0.3.json",
    "d1a_numerical_execution_spec_v0.3.json",
    "0b05c_corrective_numerical_execution_gate_v0.3.json",
    "0b05c_corrective_numerical_gate_manifest_v0.3.json",
    "0b05c_corrective_numerical_gate_hash_ledger_v0.3.json",
)
GATE_PATH = AUDIT_ROOT / ARTIFACT_NAMES[3]
AUTHORIZATION_RECORD = AUDIT_ROOT / "0b05c_numerical_authorization_record_v0.3.json"
AUTHORIZED_GATE_STATUS = "APPROVED / INTEGRATED"
AUTHORIZED_READINESS = "AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION"

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

V02_ROOTS = (
    "data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.2",
    "outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.2",
    "data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.2.jsonl",
    "data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.2",
    "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.2",
    "data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.2",
    "outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.2",
    "data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.2.jsonl",
    "data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.2",
    "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.2",
    "data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.2.jsonl",
    "data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.2",
    "outputs/evaluation/d1a_corrective_0b05c_v0.2",
    "outputs/audits/d1a_corrective_0b05c_runtime_v0.2",
    "outputs/evaluation/0b05c_corrective_numerical_v0.2",
    "outputs/audits/0b05c_corrective_numerical_runtime_v0.2",
)

EV03_ROOTS = (
    "data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.3",
    "outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.3",
    "data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.3.jsonl",
    "data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.3",
    "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.3",
)
EV04_ROOTS = (
    "data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.3",
    "outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.3",
    "data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.3.jsonl",
    "data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.3",
    "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.3",
)
D1A_ROOTS = (
    "data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.3.jsonl",
    "data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.3",
    "outputs/evaluation/d1a_corrective_0b05c_v0.3",
    "outputs/audits/d1a_corrective_0b05c_runtime_v0.3",
)
UNIFIED_ROOTS = (
    "outputs/evaluation/0b05c_corrective_numerical_v0.3",
    "outputs/audits/0b05c_corrective_numerical_runtime_v0.3",
)
FUTURE_ROOTS = EV03_ROOTS + EV04_ROOTS + D1A_ROOTS + UNIFIED_ROOTS

PIPELINE_STEPS = (
    "01_unified_preflight",
    "02_EV03_Decision885_control_reproduction",
    "03_EV03_control_reproduction_verification",
    "04_EV03_corrected_corpus_materialization",
    "05_EV03_corrected_index_build_RECOVERED_HISTORICAL_SEMANTICS",
    "06_EV03_corrected_evaluation",
    "07_EV04_Decision885_control_reproduction_ENRICHED_MRR",
    "08_EV04_control_reproduction_verification_PASS_EXACT",
    "09_EV04_corrected_corpus_materialization",
    "10_EV04_corrected_index_build",
    "11_EV04_corrected_evaluation_ENRICHED_MRR",
    "12_D1a_corrected_execution_under_future_v03_authorization",
    "13_integrity_validation",
    "14_case_level_comparisons",
    "15_aggregate_comparisons",
    "16_unified_sensitivity_summary",
    "17_execution_manifest",
    "18_exact_hash_ledger",
    "19_final_completion_state",
)

VERSIONED_PATHS = (
    "src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py",
    "src/experiments/build_bm25_corrective_0b05c_v03.py",
    "src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py",
    "src/experiments/run_0b05c_corrective_numerical_v03.py",
    "src/experiments/run_d1a_corrective_0b05c_v03.py",
    "src/experiments/run_0b05c_corrective_numerical_v02.py",
    "src/experiments/run_d1a_corrective_0b05c_v01.py",
    "src/experiments/prepare_0b05c_corrective_numerical_gate_v01.py",
    "src/experiments/build_bm25_ev03_historical_recovered_v02.py",
    "src/experiments/verify_ev03_historical_builder_recovery_v02.py",
    "src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py",
    "src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py",
    "src/experiments/build_bm25_index.py",
    "src/retrieval/bm25.py",
    "src/retrieval/text2trade_mnrl_v02.py",
    "src/bm25_index.py",
    "src/experiments/build_text2trade_mnrl_index_v02.py",
    "src/experiments/evaluate_text2trade_mnrl_data_aduanas_v02.py",
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
    FAILURE_RECORD.as_posix(),
    (V02_AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.2.json").as_posix(),
)
BINARY_PATHS = ("data/processed/indexes/bm25_nandina8.pkl",)
MODEL_IDENTITY = {
    "path": "models/text2trade_mnrl_v0.2/model.safetensors",
    "classification": "FROZEN_FILE_IDENTITY",
    "size_bytes": 470637416,
    "sha256": "ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87",
    "current_checkout_presence_required": False,
}

MRR_DEFINITION = (
    "legacy mrr field is MRR@200 because EXP-04 Fase C retrieval_depth=200; "
    "comparable flat-vs-hierarchical value is mrr_at_100"
)


class ContractViolation(RuntimeError):
    """Raised before side effects when the frozen contract is not satisfied."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractViolation(message)


def _git(root: Path, *args: str, binary: bool = False) -> bytes | str:
    result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=not binary)
    return result.stdout if binary else result.stdout.strip()


def canonical_json_bytes(payload: Mapping[str, Any]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def read_json(root: Path, relative: Path | str) -> dict[str, Any]:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def git_binding(root: Path, path: str, revision: str = "HEAD", classification: str = "VERSIONED_GIT_BLOB") -> dict[str, Any]:
    spec = f":{path}" if revision == "INDEX" else f"{revision}:{path}"
    raw = _git(root, "show", spec, binary=True)
    assert isinstance(raw, bytes)
    return {
        "path": path,
        "classification": classification,
        "git_blob_sha1": str(_git(root, "rev-parse", spec)),
        "canonical_git_blob_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_size_bytes": len(raw),
    }


def dependency_bindings(root: Path, revision: str) -> list[dict[str, Any]]:
    bindings = [git_binding(root, path, revision) for path in VERSIONED_PATHS]
    bindings.extend(git_binding(root, path, revision, "FROZEN_BINARY_GIT_BLOB") for path in BINARY_PATHS)
    bindings.append(dict(MODEL_IDENTITY))
    return bindings


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


def _spec(root: Path, arm: str, revision: str) -> dict[str, Any]:
    names = {
        "EV03": "ev03_numerical_execution_spec_v0.2.json",
        "EV04": "ev04_numerical_execution_spec_v0.2.json",
        "D1a": "d1a_numerical_execution_spec_v0.2.json",
    }
    source = read_json(root, V02_AUDIT_ROOT / names[arm])
    replacements = dict(zip(V02_ROOTS, FUTURE_ROOTS, strict=True))
    replacements.update({
        "build_bm25_corrective_0b05c_v02": "build_bm25_corrective_0b05c_v03",
        "evaluate_normative_bm25_corrective_0b05c_v01": "evaluate_normative_bm25_corrective_0b05c_v03",
        "run_0b05c_corrective_numerical_v02": "run_0b05c_corrective_numerical_v03",
        "run_d1a_corrective_0b05c_v02": "run_d1a_corrective_0b05c_v03",
        "d1a_corrective_vs_original_comparison_v0.2.json": "d1a_corrective_vs_original_comparison_v0.3.json",
        "d1a_corrective_case_level_comparison_v0.2.jsonl": "d1a_corrective_case_level_comparison_v0.3.jsonl",
        "d1a_corrective_output_hash_ledger_v0.2.csv": "d1a_corrective_output_hash_ledger_v0.3.csv",
        "d1a_corrective_execution_manifest_v0.2.json": "d1a_corrective_execution_manifest_v0.3.json",
    })
    result = _replace_strings(copy.deepcopy(source), replacements)
    result["specification_id"] = f"{arm.lower()}_numerical_execution_spec_v0.3"
    result["specification_status"] = "CLOSED_PROSPECTIVELY/CANDIDATE_PENDING_EXTERNAL_AUDIT"
    key = "D1A_NUMERICAL_EXECUTION" if arm == "D1a" else f"{arm}_NUMERICAL_EXECUTION"
    result["authorization"][key] = "NOT_AUTHORIZED"
    for flag in tuple(result["authorization"]):
        if flag != key:
            result["authorization"][flag] = False
    result["attempt04"] = "NOT_AUTHORIZED / NOT_EXECUTED"
    result["v02_attempt03_provenance"] = {
        "failure_record": FAILURE_RECORD.as_posix(),
        "classification": "HISTORICAL_FAIL_CLOSED_EVIDENCE_ONLY / NEVER_RUNTIME_INPUT",
    }
    if arm == "EV04":
        result["enriched_mrr_contract_v0.3"] = {
            "producer": "src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py:build_ev04_enriched_metrics",
            "source": "OBSERVED_REPRODUCED_CASE_ROWS",
            "denominator": "len(case_rows); REQUIRED_1056_IN_REAL_EXECUTION",
            "metric_table_prefix": ["mrr_at_100", "mrr_at_200"],
            "legacy_mrr_equals": "mrr_at_200",
            "mrr_definition": MRR_DEFINITION,
            "control_policy": "RANKING_EXACT + CASE_SUMMARY_EXACT + ENRICHED_METRICS_EXACT",
            "expected_case_count": 1056,
        }
        result["required_control"]["enriched_mrr_metrics_exact"] = True
    if arm == "D1a":
        binding = git_binding(root, "src/experiments/run_d1a_corrective_0b05c_v03.py", revision)
        result["orchestration"]["runner"] = {
            "path": binding["path"],
            "revision": "COMMITTED_GIT_BLOB",
            "git_blob_sha": binding["git_blob_sha1"],
            "canonical_blob_sha256": binding["canonical_git_blob_sha256"],
        }
    return result


def expected_runtime_paths(ev03: Mapping[str, Any], ev04: Mapping[str, Any], d1a: Mapping[str, Any]) -> list[str]:
    expected: set[str] = set()
    for arm, spec in (("EV03", ev03), ("EV04", ev04)):
        execution = spec["prospective_execution"]
        prefix = "normative_flat" if arm == "EV03" else "normative_hierarchical"
        for root in (execution["control_reproduction_index_root"], execution["corrected_index_root"]):
            expected.update({f"{root}/index.pkl", f"{root}/index_metadata.json"})
        for root in (execution["control_reproduction_output_root"], execution["corrected_output_root"]):
            expected.update({f"{root}/{prefix}_results.csv", f"{root}/{prefix}_case_summary.csv", f"{root}/{prefix}_metrics.json"})
        expected.add(spec["corrective_corpus"]["prospective_path"])
    expected.update(d1a["orchestration"]["hash_ledger_contract"]["included_paths"])
    expected.add(d1a["orchestration"]["hash_ledger_contract"]["excluded_self_path"])
    evaluation_root, runtime_root = UNIFIED_ROOTS
    expected.update({
        f"{evaluation_root}/ev03_case_level_comparison_v0.3.json",
        f"{evaluation_root}/ev03_aggregate_comparison_v0.3.json",
        f"{evaluation_root}/ev04_case_level_comparison_v0.3.json",
        f"{evaluation_root}/ev04_aggregate_comparison_v0.3.json",
        f"{evaluation_root}/unified_sensitivity_summary_v0.3.json",
        f"{runtime_root}/runtime_authorization_record_v0.3.json",
        f"{runtime_root}/execution_manifest_v0.3.json",
    })
    return sorted(expected)


def build_bundle(root: Path = ROOT, revision: str = "HEAD") -> dict[str, Any]:
    ev03 = _spec(root, "EV03", revision)
    ev04 = _spec(root, "EV04", revision)
    d1a = _spec(root, "D1a", revision)
    bindings = dependency_bindings(root, revision)
    gate = {
        "gate_id": "0b05c_corrective_numerical_execution_gate_v0.3",
        "gate_version": "v0.3",
        "gate_status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
        "gate_scope": "UNIFIED_0B05C_NUMERICAL_RECOVERY_PREEXECUTION",
        "base_commit": BASE_COMMIT,
        "authorization_readiness": "NOT_AUTHORIZATION_READY",
        "authorization": dict(AUTHORIZATION),
        "attempt04": "NOT_AUTHORIZED / NOT_EXECUTED",
        "scientific_state": dict(SCIENTIFIC_STATE),
        "pipeline_steps": list(PIPELINE_STEPS),
        "future_roots": list(FUTURE_ROOTS),
        "v02_attempt03": {
            "failure_record": FAILURE_RECORD.as_posix(),
            "failure_class": "EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT",
            "authorization_consumed": True,
            "automatic_reuse_authorized": False,
            "partial_roots_policy": "MAY_EXIST_AS_LOCAL_EVIDENCE / NEVER_ERROR / NEVER_INPUT / NEVER_REUSED",
            "roots": list(V02_ROOTS),
        },
        "root_isolation": {
            "v03_disjoint_from_v02": True,
            "v03_roots_must_be_absent_before_authorization_or_execution": True,
            "v02_partial_roots_are_never_inputs": True,
        },
        "ev03_invariants": {"token_policy": "DROP_SINGLE_CHARACTER_TOKENS", "k1": 1.5, "b": 0.75, "depth": 100, "eval_n": 1056},
        "ev04_invariants": {
            "token_policy": "ORIGINAL_HIERARCHICAL_V0.1",
            "k1": 1.5,
            "b": 0.75,
            "effective_depth": 200,
            "ranking": "UNIQUE_NANDINA8_FIRST_BM25_SCORE_OCCURRENCE",
            "eval_n": 1056,
            "only_change": "ENRICHED_MRR_METRIC_PRODUCER_CONTRACT",
            "mrr_definition": MRR_DEFINITION,
        },
        "d1a_invariants": {
            "model_size_bytes": 470637416,
            "model_sha256": MODEL_IDENTITY["sha256"],
            "metric_count": 17,
            "full_corrective_index_rebuild": True,
            "eval_n": 1056,
        },
        "patch_codes": ["87044110", "87045110"],
        "dependency_bindings": bindings,
        "authorization_record_path": AUTHORIZATION_RECORD.as_posix(),
        "authorization_transition": {
            "separate_external_audit_required": True,
            "required_gate_status": AUTHORIZED_GATE_STATUS,
            "required_readiness": AUTHORIZED_READINESS,
            "authorization_record_must_be_committed": True,
            "runtime_record_created_only_by_future_authorized_execution": True,
        },
        "runtime_hash_ledger_contract": {
            "expected_paths": expected_runtime_paths(ev03, ev04, d1a),
            "discovery_roots": list(FUTURE_ROOTS),
            "excluded_self_path": f"{UNIFIED_ROOTS[1]}/exact_hash_ledger_v0.3.json",
            "missing_or_unexpected_policy": "FAIL_CLOSED",
            "entry_fields": ["path", "sha256", "size_bytes"],
        },
    }
    manifest = {
        "artifact_id": "0b05c_corrective_numerical_gate_manifest_v0.3",
        "gate": GATE_PATH.as_posix(),
        "explicit_non_executed_state": dict(AUTHORIZATION),
        "attempt04": "NOT_AUTHORIZED / NOT_EXECUTED",
        "root_cause": gate["v02_attempt03"]["failure_class"],
        "future_execution_roots": list(FUTURE_ROOTS),
        "v02_partial_roots": {"classification": "HISTORICAL_LOCAL_EVIDENCE_ONLY", "paths": list(V02_ROOTS)},
        "code_bindings": [item for item in bindings if item["path"].startswith("src/")],
        "frozen_inputs": [item for item in bindings if item["path"].startswith(("data/", "outputs/evaluation/", "models/"))],
        "generated_at_future_runtime": {"classification": "ABSENT / NOT_GENERATED", "paths": list(FUTURE_ROOTS)},
        "no_circular_dependency": True,
    }
    ledger = {
        "artifact_id": "0b05c_corrective_numerical_gate_hash_ledger_v0.3",
        "canonical_hash_method": "SHA256_OF_GIT_CAT_FILE_BLOB_BYTES",
        "entries": bindings + [
            {"path": path, "classification": "FUTURE_GENERATED_OUTPUT_NOT_PRESENT", "status": "ABSENT / NOT_GENERATED"}
            for path in FUTURE_ROOTS
        ],
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
        (target / name).write_bytes(canonical_json_bytes(payload))
    return {"status": "PASS", "created": [str(AUDIT_ROOT / name) for name in ARTIFACT_NAMES]}


def _validate_v02_state(root: Path) -> None:
    failure = read_json(root, FAILURE_RECORD)
    require(failure["status"] == "FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED", "Attempt03 failure state drift")
    require(failure["authorization_consumed"] is True, "Attempt03 authorization is not consumed")
    require(failure["automatic_reuse_authorized"] is False, "Attempt03 reuse unexpectedly authorized")
    require(failure["attempt04_authorized"] is False, "Attempt04 unexpectedly authorized")
    require(failure["failure_class"] == "EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT", "Attempt03 failure class drift")
    v02 = read_json(root, V02_AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.2.json")
    require(v02["authorization_readiness"] == "ATTEMPT03_CONSUMED / REAUTHORIZATION_REQUIRED", "v0.2 readiness is not consumed")
    required = {key: "AUTHORIZED" for key in AUTHORIZATION if key.endswith("NUMERICAL_EXECUTION")}
    require({key: v02["authorization"].get(key) for key in required} == required, "v0.2 historical authorizations drifted")
    require(v02["authorization"]["corrective_retrieval_executed"] is False, "v0.2 retrieval state drift")
    require(v02["authorization"]["corrective_metrics_computed"] is False, "v0.2 metric state drift")


def preflight(root: Path = ROOT, *, revision: str = "HEAD", require_clean: bool = True) -> dict[str, Any]:
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", BASE_COMMIT, "HEAD"], cwd=root).returncode == 0
    require(ancestor, f"Required base {BASE_COMMIT} is not an ancestor of HEAD")
    if require_clean:
        require(str(_git(root, "status", "--short", "--untracked-files=no")) == "", "Tracked working tree is not clean")
    _validate_v02_state(root)
    require(set(FUTURE_ROOTS).isdisjoint(V02_ROOTS), "v0.3 roots collide with v0.2 Attempt03 roots")
    require(not (root / AUTHORIZATION_RECORD).exists(), "Authorization record v0.3 must be absent")
    for relative in FUTURE_ROOTS:
        require(not (root / relative).exists(), f"Future v0.3 numerical root already exists: {relative}")
    for name in ARTIFACT_NAMES:
        require((root / AUDIT_ROOT / name).is_file(), f"Missing v0.3 gate artifact: {name}")
    actual = {key: read_json(root, AUDIT_ROOT / name) for key, name in zip(("ev03", "ev04", "d1a", "gate", "manifest", "ledger"), ARTIFACT_NAMES, strict=True)}
    expected = build_bundle(root, revision)
    require(actual == expected, "v0.3 gate artifacts differ from canonical generated contract")
    gate = actual["gate"]
    require(gate["gate_status"] == "CANDIDATE_PENDING_EXTERNAL_AUDIT", "v0.3 gate status drift")
    require(gate["authorization_readiness"] == "NOT_AUTHORIZATION_READY", "v0.3 candidate unexpectedly authorization-ready")
    require(gate["authorization"] == AUTHORIZATION, "v0.3 candidate authorization state is not closed")
    require(gate["attempt04"] == "NOT_AUTHORIZED / NOT_EXECUTED", "Attempt04 state drift")
    serialized_specs = json.dumps([actual["ev03"], actual["ev04"], actual["d1a"]], sort_keys=True)
    require(all(path not in serialized_specs for path in V02_ROOTS), "A v0.2 partial root is referenced by a v0.3 spec")
    bound_paths = {item["path"] for item in gate["dependency_bindings"]}
    artifact_paths = {(AUDIT_ROOT / name).as_posix() for name in ARTIFACT_NAMES}
    require(bound_paths.isdisjoint(artifact_paths), "Circular gate artifact dependency introduced")
    for binding in gate["dependency_bindings"]:
        if binding["classification"] == "FROZEN_FILE_IDENTITY":
            continue
        require(git_binding(root, binding["path"], revision, binding["classification"]) == binding, f"Canonical binding mismatch: {binding['path']}")
    observed_v02 = [path for path in V02_ROOTS if (root / path).exists()]
    return {
        "status": "PASS",
        "mode": "PREEXECUTION_CLOSED_READONLY",
        "gate_status": gate["gate_status"],
        "authorization_readiness": gate["authorization_readiness"],
        "attempt04": gate["attempt04"],
        "numerical_execution_occurred": False,
        "corrective_retrieval_executed": False,
        "corrective_metrics_computed": False,
        "future_v03_roots_present": False,
        "v02_partial_roots_observed_and_ignored": observed_v02,
        "binding_count": len(gate["dependency_bindings"]),
    }


def main(argv: list[str] | None = None) -> int:
    import argparse

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
