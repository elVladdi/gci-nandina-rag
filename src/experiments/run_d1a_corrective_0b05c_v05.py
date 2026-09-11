"""D1a v0.5 adapter with mandatory environment readiness before side effects."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
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
AGGREGATE_FIELDS = {
    "metric", "original_numerator", "corrected_numerator", "denominator",
    "original_value", "corrected_value", "absolute_delta",
}
CASE_BASE_FIELDS = {
    "case_id", "nandina_ref", "original_rank_ref", "corrected_rank_ref",
    "ranking_changed", "rank_convention",
}
CASE_HIT_FIELDS = {
    f"{side}_{kind}_{k}"
    for side in ("original", "corrected")
    for kind in ("found_at", "hit")
    for k in (1, 3, 5, 10, 50, 100, 200)
}
CASE_PATCH_FIELDS = {
    f"{prefix}_{code}"
    for code in ("87044110", "87045110")
    for prefix in ("original_rank", "corrected_rank", "corrected_contains")
}
D1A_CASE_FIELDS = CASE_BASE_FIELDS | CASE_HIT_FIELDS | CASE_PATCH_FIELDS


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


def _number(value: Any, label: str) -> float:
    require(isinstance(value, (int, float)) and not isinstance(value, bool), f"D1a numeric field is invalid: {label}")
    converted = float(value)
    require(math.isfinite(converted), f"D1a numeric field is non-finite: {label}")
    return converted


def validate_aggregate_comparison(path: Path, spec: Mapping[str, Any]) -> dict[str, Any]:
    payload = legacy.load_json(path)
    rows = payload.get("metrics")
    expected_names = [label for label, _ in legacy.METRIC_SPECS]
    require(isinstance(rows, list) and len(rows) == 17, "D1a aggregate must contain exactly 17 metrics")
    require([row.get("metric") for row in rows] == expected_names, "D1a aggregate metric names/order changed")
    for row in rows:
        require(isinstance(row, Mapping) and set(row) == AGGREGATE_FIELDS, f"D1a aggregate row schema changed: {row}")
        denominator = row["denominator"]
        require(isinstance(denominator, int) and not isinstance(denominator, bool) and denominator > 0, "D1a denominator must be a positive integer")
        original_numerator = _number(row["original_numerator"], "original_numerator")
        corrected_numerator = _number(row["corrected_numerator"], "corrected_numerator")
        original_value = _number(row["original_value"], "original_value")
        corrected_value = _number(row["corrected_value"], "corrected_value")
        delta = _number(row["absolute_delta"], "absolute_delta")
        require(math.isclose(original_value, original_numerator / denominator, rel_tol=0.0, abs_tol=1e-12), "D1a original value/denominator mismatch")
        require(math.isclose(corrected_value, corrected_numerator / denominator, rel_tol=0.0, abs_tol=1e-12), "D1a corrected value/denominator mismatch")
        require(math.isclose(delta, corrected_value - original_value, rel_tol=0.0, abs_tol=1e-12), "D1a aggregate delta mismatch")
    require(expected_names == list(spec["orchestration"]["comparison_contract"]["aggregate_metrics"]), "D1a aggregate spec metric contract changed")
    return payload


def validate_case_level_comparison(path: Path, spec: Mapping[str, Any]) -> list[dict[str, Any]]:
    require(path.is_file() and path.stat().st_size > 0, "D1a case-level comparison is missing or empty")
    rows: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        require(line.strip() != "", f"D1a case-level comparison has blank row: {number}")
        row = json.loads(line)
        require(isinstance(row, dict) and set(row) == D1A_CASE_FIELDS, f"D1a case schema changed at row {number}")
        rows.append(row)
    require(len(rows) == 1056, "D1a case-level comparison must contain exactly 1056 rows")
    case_ids = [row["case_id"] for row in rows]
    require(all(isinstance(case_id, str) and case_id for case_id in case_ids), "D1a case_id is empty or malformed")
    require(len(set(case_ids)) == 1056, "D1a case IDs are duplicated")
    require(all(isinstance(row["nandina_ref"], str) and row["nandina_ref"] for row in rows), "D1a nandina_ref is empty")
    rank_fields = ["original_rank_ref", "corrected_rank_ref", *sorted(field for field in CASE_PATCH_FIELDS if "_rank_" in field)]
    for row in rows:
        for field in rank_fields:
            require(isinstance(row[field], int) and not isinstance(row[field], bool) and row[field] >= 0, f"D1a rank is invalid: {field}")
    required = set(spec["orchestration"]["comparison_contract"]["case_fields"])
    require(required <= D1A_CASE_FIELDS, "D1a spec requires fields outside the producer schema")
    return rows


def validate_execution_manifest(path: Path, spec: Mapping[str, Any]) -> dict[str, Any]:
    payload = legacy.load_json(path)
    require(payload.get("status") == "PASS", "D1a execution manifest status is not PASS")
    require(payload.get("runner_version") == "v0.5", "D1a execution manifest runner_version is stale")
    outputs = payload.get("runner_outputs")
    require(outputs == spec["orchestration"]["runner_outputs"], "D1a execution manifest runner outputs differ from v0.5 spec")
    require(not any("v0.1" in value or "v0.4" in value for value in outputs.values()), "D1a execution manifest references stale current output")
    return payload


def validate_internal_hash_ledger(root: Path, path: Path, spec: Mapping[str, Any]) -> list[dict[str, Any]]:
    require(path.is_file() and path.stat().st_size > 0, "D1a internal hash ledger is missing or empty")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames == ["path", "sha256", "size_bytes"], "D1a internal ledger schema changed")
        rows = list(reader)
    expected = list(spec["orchestration"]["hash_ledger_contract"]["included_paths"])
    observed = [row["path"] for row in rows]
    require(len(observed) == len(set(observed)), "D1a internal ledger contains duplicate paths")
    require(set(observed) == set(expected) and len(observed) == len(expected), "D1a internal ledger path set is not exact")
    excluded = spec["orchestration"]["hash_ledger_contract"]["excluded_self_path"]
    require(excluded == legacy.relative_path(root, path) and excluded not in observed, "D1a ledger self-path exclusion is not exact")
    for row in rows:
        target = legacy.project_path(root, row["path"])
        require(target.is_file() and target.stat().st_size > 0, f"D1a ledger target is missing: {row['path']}")
        digest = row["sha256"]
        require(len(digest) == 64 and all(char in "0123456789abcdef" for char in digest), f"D1a ledger SHA is malformed: {row['path']}")
        try:
            size = int(row["size_bytes"])
        except (TypeError, ValueError) as error:
            raise ContractViolation(f"D1a ledger size is malformed: {row['path']}") from error
        require(size > 0 and size == target.stat().st_size, f"D1a ledger size mismatch: {row['path']}")
        require(digest == legacy.sha256_file(target), f"D1a ledger SHA mismatch: {row['path']}")
    return rows


def d1a_summary_reference(root: Path, spec: Mapping[str, Any], result: Mapping[str, Any]) -> dict[str, Any]:
    require(result.get("status") == "PASS" and result.get("mode") == "AUTHORIZED_EXECUTION", "D1a result is not complete")
    paths = runner_output_paths(root, spec)
    validate_aggregate_comparison(paths["aggregate_comparison"], spec)
    validate_case_level_comparison(paths["case_level_comparison"], spec)
    validate_execution_manifest(paths["execution_manifest"], spec)
    validate_internal_hash_ledger(root, paths["hash_ledger"], spec)
    out: dict[str, Any] = {"status": "PASS"}
    for key in ("aggregate_comparison", "case_level_comparison", "execution_manifest", "hash_ledger"):
        path = paths[key]
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
