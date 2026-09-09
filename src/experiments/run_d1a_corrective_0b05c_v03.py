"""Closed prospective D1a adapter for the isolated 0B-05C v0.3 roots."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping

from . import run_d1a_corrective_0b05c_v01 as legacy
from .prepare_0b05c_corrective_numerical_gate_v03 import (
    AUDIT_ROOT,
    AUTHORIZATION_RECORD,
    D1A_ROOTS,
    ROOT,
    git_binding,
    read_json,
    require,
)


SPEC_PATH = AUDIT_ROOT / "d1a_numerical_execution_spec_v0.3.json"
REQUIRED_UNIFIED_AUTHORIZATIONS = {
    "EV03_NUMERICAL_EXECUTION": "AUTHORIZED",
    "EV04_NUMERICAL_EXECUTION": "AUTHORIZED",
    "D1A_NUMERICAL_EXECUTION": "AUTHORIZED",
    "UNIFIED_0B05C_NUMERICAL_EXECUTION": "AUTHORIZED",
}


def validate_unified_authorization_proof(proof: Mapping[str, Any]) -> None:
    require(proof.get("status") == "PASS", "Unified authorization proof did not PASS")
    require(proof.get("mode") == "AUTHORIZED_PREFLIGHT_ONLY", "Unified authorization proof mode is invalid")
    require(proof.get("authorization") == REQUIRED_UNIFIED_AUTHORIZATIONS, "Unified authorization proof does not contain all four authorizations")
    baseline = proof.get("authorization_baseline_commit")
    require(isinstance(baseline, str) and len(baseline) == 40, "Unified authorization baseline is missing")
    binding = proof.get("authorization_record_binding")
    require(isinstance(binding, Mapping) and binding.get("path") == AUTHORIZATION_RECORD.as_posix(), "Unified authorization record binding is missing")
    require(all(binding.get(key) for key in ("git_blob_sha1", "canonical_git_blob_sha256", "canonical_size_bytes")), "Unified authorization record binding is incomplete")


def preflight(root: Path = ROOT, *, revision: str = "HEAD") -> dict[str, Any]:
    spec = read_json(root, SPEC_PATH)
    require(spec["authorization"]["D1A_NUMERICAL_EXECUTION"] in {"NOT_AUTHORIZED", "AUTHORIZED"}, "D1a v0.3 authorization state is invalid")
    require(spec["model_policy"]["MODEL_POLICY"] == "FREEZE_ORIGINAL_D1A_WEIGHTS", "D1a model policy drift")
    require(spec["model_policy"]["must_not_retrain"] is True, "D1a retraining prohibition missing")
    require(spec["index_builder"]["policy"] == "FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD", "D1a atomic rebuild policy drift")
    require(spec["evaluation"]["ranking_depth"] == 200, "D1a depth drift")
    require(len(spec["orchestration"]["comparison_contract"]["aggregate_metrics"]) == 17, "D1a 17-metric contract drift")
    for relative in D1A_ROOTS:
        require(not (root / relative).exists(), f"D1a v0.3 future root exists: {relative}")
    legacy.validate_patch_contract(spec)
    corpus_bytes = legacy.canonical_frozen_text_bytes(root, spec["original_normative_corpus"], "Original normative corpus")
    corrected_sha = legacy.sha256_bytes(legacy.patched_corpus_bytes(corpus_bytes, spec))
    eval_input = root / spec["evaluation"]["eval_input"]["path"]
    require(legacy.sha256_file(eval_input) == spec["evaluation"]["eval_input"]["sha256"], "D1a EVAL identity drift")
    for item in (spec["evaluation"]["primary_control"], spec["evaluation"]["primary_control_case_summary"], spec["evaluation"]["primary_control_ranking_trace"]):
        require(legacy.sha256_file(root / item["path"]) == item["sha256"], f"D1a control identity drift: {item['path']}")
    for identity in (spec["orchestration"]["runner"], spec["index_builder"]["code_identity"], spec["evaluation"]["code_identity"]):
        current = git_binding(root, identity["path"], revision)
        require(current["git_blob_sha1"] == identity["git_blob_sha"], f"D1a code blob drift: {identity['path']}")
        require(current["canonical_git_blob_sha256"] == identity.get("canonical_blob_sha256", identity.get("sha256")), f"D1a canonical code SHA drift: {identity['path']}")
    return {
        "status": "PASS",
        "mode": "PREEXECUTION_CLOSED_READONLY",
        "numerical_execution_occurred": False,
        "corrected_corpus_sha256": corrected_sha,
        "prospective_roots_absent": list(D1A_ROOTS),
    }


def execute_authorized(root: Path = ROOT, *, authorization_proof: Mapping[str, Any] | None = None) -> dict[str, Any]:
    if authorization_proof is None:
        from .run_0b05c_corrective_numerical_v03 import preflight_authorized

        authorization_proof = preflight_authorized(root)
    validate_unified_authorization_proof(authorization_proof)
    spec = read_json(root, SPEC_PATH)
    require(spec["authorization"]["D1A_NUMERICAL_EXECUTION"] == "AUTHORIZED", "D1a v0.3 numerical execution is NOT_AUTHORIZED")
    proof = preflight(root)
    legacy.validate_binary_file_identity(root, spec["model_policy"]["weights"], "Frozen D1a model")
    derivation = spec["orchestration"]["config_derivation"]
    corrected_path = legacy.project_path(root, spec["corrected_normative_corpus"]["prospective_path"])
    runtime_root = legacy.project_path(root, spec["orchestration"]["runtime_root"])
    runtime_config = legacy.project_path(root, spec["orchestration"]["runtime_config_path"])
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
            subprocess.run([sys.executable, "-B", "-m", module, "--config", config_arg], cwd=root, check=True)
        paths = legacy.expected_paths(root, spec)
        legacy.require_all(paths["index"], "builder")
        legacy.require_all(paths["evaluation"], "evaluator")
        legacy.write_json(paths["runner"][0], legacy.build_aggregate_comparison(root, spec))
        legacy.write_jsonl(paths["runner"][1], legacy.build_case_comparison(root, spec))
        manifest_proof = {**proof, "mode": "PREFLIGHT_ONLY"}
        legacy.write_json(paths["runner"][3], legacy.build_execution_manifest(root, spec, manifest_proof))
        legacy.write_hash_ledger(root, spec)
        return legacy.authorized_execution_provenance(manifest_proof)
    except Exception as error:
        if runtime_root.exists():
            (runtime_root / "execution_failed.json").write_text(json.dumps({"status": "FAILED", "error": str(error)}, ensure_ascii=False) + "\n", encoding="utf-8")
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
