"""D1a v0.5 adapter with mandatory environment readiness before side effects."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping

from . import run_d1a_corrective_0b05c_v01 as legacy
from .prepare_0b05c_corrective_numerical_gate_v05 import (
    AUDIT_ROOT, AUTHORIZATION_RECORD, D1A_EVALUATION_FILENAMES, D1A_INDEX_FILENAMES,
    D1A_RUNNER_OUTPUTS, FUTURE_ROOTS, ROOT, ContractViolation,
    preauthorization_environment_preflight, require,
)


SPEC_PATH = AUDIT_ROOT / "d1a_numerical_execution_spec_v0.5.json"
D1A_ROOTS = FUTURE_ROOTS[10:14]
REQUIRED_UNIFIED_AUTHORIZATIONS = {
    "EV03_NUMERICAL_EXECUTION": "AUTHORIZED",
    "EV04_NUMERICAL_EXECUTION": "AUTHORIZED",
    "D1A_NUMERICAL_EXECUTION": "AUTHORIZED",
    "UNIFIED_0B05C_NUMERICAL_EXECUTION": "AUTHORIZED",
}


def runner_output_paths(root: Path, spec: Mapping[str, Any]) -> dict[str, Path]:
    declared = spec["orchestration"]["runner_outputs"]
    require(set(declared) == set(D1A_RUNNER_OUTPUTS), "D1a runner output key set is not exact")
    expected = {key: f"{spec['evaluation']['prospective_output_root']}/{name}" for key, name in D1A_RUNNER_OUTPUTS.items()}
    require(declared == expected, "D1a runner output names are not the v0.5 authority")
    return {key: legacy.project_path(root, relative) for key, relative in declared.items()}


def expected_paths(root: Path, spec: Mapping[str, Any]) -> dict[str, list[Path]]:
    derivation = spec["orchestration"]["config_derivation"]
    index_root = legacy.project_path(root, derivation["corrected_index_root"])
    evaluation_root = legacy.project_path(root, spec["evaluation"]["prospective_output_root"])
    runner = runner_output_paths(root, spec)
    return {
        "index": [index_root / name for name in D1A_INDEX_FILENAMES],
        "evaluation": [evaluation_root / name for name in D1A_EVALUATION_FILENAMES],
        "runner": [runner[key] for key in ("aggregate_comparison", "case_level_comparison", "hash_ledger", "execution_manifest")],
    }


def actual_producer_set(root: Path, spec: Mapping[str, Any]) -> set[str]:
    paths = expected_paths(root, spec)
    produced = {legacy.relative_path(root, path) for group in paths.values() for path in group}
    produced.add(spec["corrected_normative_corpus"]["prospective_path"])
    produced.add(spec["orchestration"]["runtime_config_path"])
    return produced


def contractual_ledger_paths(root: Path, spec: Mapping[str, Any]) -> list[Path]:
    paths = expected_paths(root, spec)
    actual = [
        legacy.project_path(root, spec["corrected_normative_corpus"]["prospective_path"]),
        legacy.project_path(root, spec["orchestration"]["runtime_config_path"]),
        *paths["index"], *paths["evaluation"], paths["runner"][0], paths["runner"][1], paths["runner"][3],
    ]
    contract = spec["orchestration"]["hash_ledger_contract"]
    declared = [legacy.project_path(root, relative) for relative in contract["included_paths"]]
    require(declared == actual, "D1a v0.5 hash-ledger contract differs from actual producers")
    require(legacy.project_path(root, contract["excluded_self_path"]) == paths["runner"][2], "D1a v0.5 ledger self path mismatch")
    return declared


def d1a_path_contract_sets(root: Path, spec: Mapping[str, Any]) -> dict[str, set[str]]:
    spec_set = set(spec["orchestration"]["runner_outputs"].values())
    producer_set = {legacy.relative_path(root, path) for path in expected_paths(root, spec)["runner"]}
    return {"D1A_SPEC_RUNNER_SET": spec_set, "D1A_ACTUAL_PRODUCER_SET": producer_set}


def write_hash_ledger(root: Path, spec: Mapping[str, Any]) -> Path:
    paths = expected_paths(root, spec)
    contractual = contractual_ledger_paths(root, spec)
    legacy.require_all(contractual, "D1a v0.5 hash ledger")
    ledger = paths["runner"][2]
    require(not ledger.exists(), f"Refusing to overwrite D1a v0.5 ledger: {ledger}")
    rows = [{"path": legacy.relative_path(root, path), "sha256": legacy.sha256_file(path), "size_bytes": path.stat().st_size} for path in contractual]
    legacy.write_csv(ledger, rows, ["path", "sha256", "size_bytes"])
    return ledger


def build_aggregate_comparison(root: Path, spec: Mapping[str, Any]) -> dict[str, Any]:
    payload = legacy.build_aggregate_comparison(root, spec)
    payload["comparison_id"] = "d1a_corrective_vs_original_v0.5"
    return payload


def build_execution_manifest(root: Path, spec: Mapping[str, Any], proof: Mapping[str, Any]) -> dict[str, Any]:
    payload = legacy.build_execution_manifest(root, spec, proof)
    payload["runner_version"] = "v0.5"
    payload["runner_outputs"] = dict(spec["orchestration"]["runner_outputs"])
    return payload


def d1a_summary_reference(root: Path, spec: Mapping[str, Any], result: Mapping[str, Any]) -> dict[str, Any]:
    require(result.get("status") == "PASS" and result.get("mode") == "AUTHORIZED_EXECUTION", "D1a result is not complete")
    paths = runner_output_paths(root, spec)
    out: dict[str, Any] = {"status": "PASS"}
    for key in ("aggregate_comparison", "case_level_comparison", "execution_manifest", "hash_ledger"):
        path = paths[key]
        require(path.is_file() and path.stat().st_size > 0, f"D1a v0.5 output is missing: {key}")
        out[key] = {"path": legacy.relative_path(root, path), "sha256": legacy.sha256_file(path), "size_bytes": path.stat().st_size}
    return out


def _read_spec(root: Path) -> dict[str, Any]:
    payload = json.loads((root / SPEC_PATH).read_text(encoding="utf-8"))
    require(isinstance(payload, dict), "D1a v0.5 spec is malformed")
    return payload


def validate_unified_authorization_proof(proof: Mapping[str, Any]) -> None:
    require(proof.get("status") == "PASS" and proof.get("mode") == "AUTHORIZED_PREFLIGHT_ONLY", "Unified v0.5 authorization proof is invalid")
    require(proof.get("authorization") == REQUIRED_UNIFIED_AUTHORIZATIONS, "Unified v0.5 authorization set is incomplete")
    binding = proof.get("authorization_record_binding")
    require(isinstance(binding, Mapping) and binding.get("path") == AUTHORIZATION_RECORD.as_posix(), "v0.5 authorization record binding is missing")


def preflight(root: Path = ROOT) -> dict[str, Any]:
    spec = _read_spec(root)
    require(spec["authorization"]["D1A_NUMERICAL_EXECUTION"] in {"NOT_AUTHORIZED", "AUTHORIZED"}, "D1a v0.5 authorization state is invalid")
    require(spec["model_policy"]["MODEL_POLICY"] == "FREEZE_ORIGINAL_D1A_WEIGHTS", "D1a frozen model policy drift")
    require(spec["model_policy"]["must_not_retrain"] is True, "D1a retraining prohibition is missing")
    require(spec["evaluation"]["ranking_depth"] == 200, "D1a retrieval depth drift")
    require(len(spec["orchestration"]["comparison_contract"]["aggregate_metrics"]) == 17, "D1a metric contract drift")
    require(all(not (root / path).exists() for path in D1A_ROOTS), "A D1a v0.5 prospective root exists")
    legacy.validate_patch_contract(spec)
    corpus = legacy.canonical_frozen_text_bytes(root, spec["original_normative_corpus"], "Original normative corpus")
    corrected_sha = legacy.sha256_bytes(legacy.patched_corpus_bytes(corpus, spec))
    evaluation = spec["evaluation"]
    require(legacy.sha256_file(root / evaluation["eval_input"]["path"]) == evaluation["eval_input"]["sha256"], "D1a EVAL identity drift")
    for item in (evaluation["primary_control"], evaluation["primary_control_case_summary"], evaluation["primary_control_ranking_trace"]):
        require(legacy.sha256_file(root / item["path"]) == item["sha256"], f"D1a control identity drift: {item['path']}")
    config_identity = spec["orchestration"]["original_config"]
    config_bytes = legacy.canonical_frozen_text_bytes(root, config_identity, "Original frozen config")
    runtime = legacy.derive_runtime_config(legacy.load_json_bytes(config_bytes, config_identity["path"]), spec, corrected_sha)
    changed = legacy.diff_paths(legacy.load_json_bytes(config_bytes, config_identity["path"]), runtime)
    require(changed == {"frozen_inputs.normative_corpus", "frozen_inputs.normative_corpus_sha256", "index.output_dir", "outputs.evaluation_dir"}, "D1a runtime config diff changed")
    return {"status": "PASS", "mode": "PREEXECUTION_CLOSED_READONLY", "corrected_corpus_sha256": corrected_sha, "runtime_config_changed_fields": sorted(changed), "eval_identity": "PASS_EXACT", "prospective_roots_present": False, "numerical_execution_occurred": False}


def execute_authorized(
    root: Path = ROOT,
    *,
    authorization_proof: Mapping[str, Any] | None = None,
    interpreter: Path | str | None = None,
) -> dict[str, Any]:
    """Future-only execution path; current v0.5 candidate always fails before here."""

    if authorization_proof is None:
        from .run_0b05c_corrective_numerical_v05 import preflight_authorized
        authorization_proof = preflight_authorized(root, interpreter=interpreter)
    validate_unified_authorization_proof(authorization_proof)
    spec = _read_spec(root)
    require(spec["authorization"]["D1A_NUMERICAL_EXECUTION"] == "AUTHORIZED", "D1a v0.5 numerical execution is NOT_AUTHORIZED")
    environment = preauthorization_environment_preflight(root, interpreter)
    require(environment["status"] == "PASS", "D1a v0.5 environment gate did not PASS")
    proof = preflight(root)
    derivation = spec["orchestration"]["config_derivation"]
    corrected_path = legacy.project_path(root, spec["corrected_normative_corpus"]["prospective_path"])
    runtime_root = legacy.project_path(root, spec["orchestration"]["runtime_root"])
    runtime_config = legacy.project_path(root, spec["orchestration"]["runtime_config_path"])
    executable = str(Path(interpreter or sys.executable).resolve())
    try:
        with corrected_path.open("xb") as handle:
            handle.write(legacy.patched_corpus_bytes(legacy.canonical_frozen_text_bytes(root, spec["original_normative_corpus"], "Original normative corpus"), spec))
        runtime_root.mkdir(parents=True)
        config_identity = spec["orchestration"]["original_config"]
        config_bytes = legacy.canonical_frozen_text_bytes(root, config_identity, "Original frozen config")
        runtime = legacy.derive_runtime_config(legacy.load_json_bytes(config_bytes, derivation["original_config_path"]), spec, proof["corrected_corpus_sha256"])
        legacy.write_json(runtime_config, runtime)
        config_arg = legacy.relative_path(root, runtime_config)
        for module in ("src.experiments.build_text2trade_mnrl_index_v02", "src.experiments.evaluate_text2trade_mnrl_data_aduanas_v02"):
            subprocess.run([executable, "-B", "-m", module, "--config", config_arg], cwd=root, check=True)
        paths = expected_paths(root, spec)
        legacy.require_all(paths["index"], "builder"); legacy.require_all(paths["evaluation"], "evaluator")
        legacy.write_json(paths["runner"][0], build_aggregate_comparison(root, spec))
        legacy.write_jsonl(paths["runner"][1], legacy.build_case_comparison(root, spec))
        manifest_proof = {**proof, "mode": "PREFLIGHT_ONLY", "environment": environment["interpreter"]}
        legacy.write_json(paths["runner"][3], build_execution_manifest(root, spec, manifest_proof))
        write_hash_ledger(root, spec)
        return legacy.authorized_execution_provenance(manifest_proof)
    except Exception as error:
        if runtime_root.exists():
            (runtime_root / "execution_failed.json").write_text(json.dumps({"status": "FAILED", "error": type(error).__name__}, ensure_ascii=False) + "\n", encoding="utf-8")
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--execute-authorized", action="store_true")
    args = parser.parse_args(argv)
    result = execute_authorized(ROOT) if args.execute_authorized else preflight(ROOT)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
