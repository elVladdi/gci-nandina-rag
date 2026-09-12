"""Fail-closed prospective EXP-11B H150/H200 retrieval runner v0.3.

This package is not an authorization. Preflight reads bank identities only,
the H100 self-test uses temporary output, and official scoring requires a
separate one-shot authorization whose consumption marker is created
exclusively immediately before scoring begins.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import json
import platform
import re
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence, TextIO

from ..bm25_index import sha256_file
from ..evaluation.metrics import mrr_from_rank
from ..utils.paths import project_root, resolve_project_path
from . import evaluate_historical_retrieval_data_aduanas_v02 as historical
from . import materialize_exp11b_banks_v01 as materializer


DEFAULT_CONFIG = Path("src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.3.json")
RUNNER_PATH = Path("src/experiments/run_exp11b_historical_retrieval_h150_h200_v03.py")
CONFIG_PATH = DEFAULT_CONFIG
METHOD = "historical_bm25_data_aduanas_class87_exp11b_v0.1"
REQUIRED_IDENTITY_FIELDS = (
    "bank_id",
    "filename",
    "seed",
    "condition",
    "row_count",
    "new_row_count",
    "total_dam_count",
    "new_dam_count",
    "bank_csv_sha256",
    "size_bytes",
    "composition_sha256",
    "H100_core_id_order_sha256",
    "increment_id_order_sha256",
    "total_bank_id_order_sha256",
)
INTEGER_IDENTITY_FIELDS = {
    "seed",
    "row_count",
    "new_row_count",
    "total_dam_count",
    "new_dam_count",
    "size_bytes",
}
CASE_FIELDS = (
    "run_id", "bank_id", "condition", "seed", "case_id", "id_unico",
    "reference_nandina", "reference_rank", "reciprocal_rank", "hit_at_1",
    "hit_at_3", "hit_at_5", "hit_at_10", "hit_at_50", "top1_nandina",
    "candidate_count", "ranking_depth", "method",
)
CANDIDATE_FIELDS = (
    "run_id", "bank_id", "condition", "seed", "case_id", "candidate_rank",
    "candidate_nandina", "candidate_history_rank", "candidate_case_id",
    "candidate_id_unico", "score", "method",
)
METRIC_FIELDS = (
    "run_id", "bank_id", "condition", "seed", "primary_n",
    "top_1_numerator", "top_1", "top_3_numerator", "top_3",
    "top_5_numerator", "top_5", "top_10_numerator", "top_10",
    "top_50_numerator", "top_50", "mrr_numerator", "mrr",
)
SUMMARY_FIELDS = (
    "condition", "expected_runs", "completed_runs", "primary_n",
    "top_1_mean", "top_3_mean", "top_5_mean", "top_10_mean",
    "top_50_mean", "mrr_mean", "status",
)
HASH_FIELDS = ("artifact", "sha256", "size_bytes", "role")
FAILURE_STAGES = {
    "NOT_STARTED",
    "BANK_VALIDATION",
    "INDEX_BUILD",
    "EVAL_SCORING",
    "CASE_WRITE",
    "METRIC_FINALIZATION",
    "OUTPUT_FINALIZATION",
}


class ContractViolation(RuntimeError):
    """Raised when a prospective execution invariant fails."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _read_json(path: Path) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        raise ContractViolation(f"Cannot read JSON contract: {path}") from error
    if not isinstance(payload, dict):
        raise ContractViolation(f"JSON contract must be an object: {path}")
    return payload


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fields: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _open_stream(path: Path, fields: Sequence[str]) -> tuple[TextIO, csv.DictWriter]:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = path.open("w", encoding="utf-8", newline="")
    writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    return handle, writer


def _git(root: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args], cwd=root, check=True, text=True, capture_output=True
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise ContractViolation(f"Git binding command failed: {' '.join(args)}") from error
    return result.stdout.strip()


def _git_bytes(root: Path, *args: str) -> bytes:
    try:
        result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError) as error:
        raise ContractViolation(f"Git binding command failed: {' '.join(args)}") from error
    return result.stdout


def _working_blob(root: Path, relative_path: str) -> str:
    path = root / relative_path
    if not path.is_file():
        raise ContractViolation(f"Bound source is missing: {relative_path}")
    return _git(root, "hash-object", f"--path={relative_path}", str(path))


def _blob_at(root: Path, commit: str, relative_path: str) -> str:
    return _git(root, "rev-parse", f"{commit}:{relative_path}")


def _sha256_at(root: Path, commit: str, relative_path: str) -> str:
    return hashlib.sha256(_git_bytes(root, "show", f"{commit}:{relative_path}")).hexdigest()


def _is_ancestor(root: Path, ancestor: str, descendant: str) -> bool:
    result = subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        cwd=root,
        capture_output=True,
    )
    if result.returncode not in (0, 1):
        raise ContractViolation("Git ancestry check failed")
    return result.returncode == 0


def _normalize_identity(field: str, value: Any) -> Any:
    if field in INTEGER_IDENTITY_FIELDS:
        try:
            return int(value)
        except (TypeError, ValueError) as error:
            raise ContractViolation(f"Identity field {field} is not an integer: {value!r}") from error
    return str(value)


def _identity(entry: Mapping[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED_IDENTITY_FIELDS if field not in entry]
    if missing:
        raise ContractViolation(f"Bank identity lacks fields: {missing}")
    return {field: _normalize_identity(field, entry[field]) for field in REQUIRED_IDENTITY_FIELDS}


def _load_ledger(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ContractViolation(f"Ledger has no header: {path}")
        return [dict(row) for row in reader]


def _validate_config(config: Mapping[str, Any]) -> None:
    expected = {
        "experiment_id": "EXP-11B",
        "scope": "H150_H200_HISTORICAL_RETRIEVAL_ONLY",
        "contract_status": "CANDIDATE_EXECUTION_PACKAGE_V03_PENDING_EXTERNAL_AUDIT",
        "package_parent_commit": "09ff184854659110f7711b3eee65fc18927649da",
        "execution_authorized": False,
        "execution_executed": False,
        "expected_banks": 20,
        "official_runs_per_bank": 1,
        "primary_eval_n": 1056,
        "candidate_depth": 100,
        "k_values": [1, 3, 5, 10, 50],
        "automatic_retries": False,
        "silent_resume": False,
        "silent_overwrite": False,
        "rerun_for_unexpected_results": False,
        "configuration_mutable_after_authorization": False,
        "one_shot_consumption_required": True,
        "reuse_same_authorization_after_start": False,
        "new_authorization_required_after_failure": True,
        "approved_package_commit_must_be_ancestor_of_execution_head": True,
        "runner_config_byte_identity_required": True,
        "stream_case_level_output": True,
        "stream_candidate_output": True,
        "partial_outputs_are_official": False,
        "canonical_authorization_path_required": True,
        "authorization_must_be_versioned_in_execution_head": True,
        "authorization_worktree_identity_required": True,
        "noncanonical_authorization_override_allowed": False,
        "consumption_boundary": "IMMEDIATELY_BEFORE_FIRST_BM25_SCORE",
    }
    for field, value in expected.items():
        if config.get(field) != value:
            raise ContractViolation(f"Execution config field mismatch: {field}")
    scientific = config.get("scientific_contract", {})
    required_scientific = {
        "query_column": historical.QUERY_COLUMN,
        "label_column": historical.LABEL_COLUMN,
        "normalization": "unicode_NFKD_lowercase_remove_combining_marks",
        "tokenizer": "regex_[a-z0-9]+",
        "k1": 1.5,
        "b": 0.75,
        "history_depth": "bank_row_count",
        "candidate_depth": 100,
        "k_values": [1, 3, 5, 10, 50],
        "ranking_order": "descending_score_then_ascending_historical_case_id",
        "candidate_deduplication": "first_ranked_historical_row_per_NANDINA",
        "reference_rank": "one_based_rank_after_NANDINA_deduplication_or_zero_when_absent",
        "reciprocal_rank": "zero_when_rank_is_zero_else_1_over_rank",
        "primary_denominator": 1056,
    }
    for field, value in required_scientific.items():
        if scientific.get(field) != value:
            raise ContractViolation(f"Scientific contract field mismatch: {field}")
    if config.get("paths", {}).get("future_authorization") != (
        "outputs/audits/exp11b_retrieval_execution_gate_v0.1/"
        "exp11b_retrieval_execution_authorization_v0.3.json"
    ):
        raise ContractViolation("Canonical authorization path contract mismatch")
    authorization = config.get("authorization_contract", {})
    if authorization.get("required_status") != "AUTHORIZED_ONE_SHOT":
        raise ContractViolation("Authorization status contract mismatch")
    required_fields = set(authorization.get("required_fields", []))
    mandatory = {
        "authorization_id", "attempt_id", "authorization_status",
        "approved_package_commit", "runner_path", "runner_git_blob", "runner_sha256",
        "config_path", "config_git_blob", "config_sha256", "eval_sha256",
        "bank_manifest_sha256", "bank_ledger_sha256", "portability_closure_blob",
        "expected_banks", "official_output_root",
    }
    if required_fields != mandatory:
        raise ContractViolation("Authorization required-field contract mismatch")


def _validate_source_bindings(root: Path, config: Mapping[str, Any]) -> list[dict[str, str]]:
    observed: list[dict[str, str]] = []
    for binding in config.get("source_bindings", []):
        path = str(binding["path"])
        actual_blob = _working_blob(root, path)
        if actual_blob != str(binding["git_blob"]):
            raise ContractViolation(f"Source binding mismatch for {path}: {actual_blob}")
        if binding.get("sha256") and sha256_file(root / path) != binding["sha256"]:
            raise ContractViolation(f"Source SHA-256 mismatch for {path}")
        observed.append({"path": path, "git_blob": actual_blob, "role": str(binding["role"])})
    return observed


def _validate_eval_and_h100(root: Path, config: Mapping[str, Any]) -> dict[str, Any]:
    observed: dict[str, Any] = {}
    for name in ("eval", "h100_control"):
        binding = config["input_bindings"][name]
        path = root / binding["path"]
        actual_sha = sha256_file(path)
        if actual_sha != binding["sha256"]:
            raise ContractViolation(f"{name} SHA-256 mismatch: {actual_sha}")
        rows = historical._read_csv(path)
        if len(rows) != int(binding["rows"]):
            raise ContractViolation(f"{name} row-count mismatch: {len(rows)}")
        observed[name] = {"path": str(path), "sha256": actual_sha, "rows": len(rows)}
    return observed


def _validate_banks(root: Path, config: Mapping[str, Any], bank_dir: Path) -> dict[str, Any]:
    if not bank_dir.is_dir():
        raise ContractViolation(f"Official bank directory is unavailable: {bank_dir}")
    sources = config["bank_contract_sources"]
    inventory = _read_json(root / sources["inventory_path"]).get("bank_identities")
    manifest = _read_json(root / sources["manifest_path"]).get("banks")
    ledger = _load_ledger(root / sources["ledger_path"])
    if not all(isinstance(rows, list) and len(rows) == 20 for rows in (inventory, manifest, ledger)):
        raise ContractViolation("Frozen bank contracts must each contain exactly 20 identities")
    inventory_by_id = {str(row["bank_id"]): row for row in inventory}
    manifest_by_id = {str(row["bank_id"]): row for row in manifest}
    ledger_by_id = {str(row["bank_id"]): row for row in ledger}
    configured = {str(row["bank_id"]): row for row in config["bank_bindings"]}
    expected_ids = set(inventory_by_id)
    if len(expected_ids) != 20 or set(manifest_by_id) != expected_ids or set(ledger_by_id) != expected_ids:
        raise ContractViolation("Frozen bank IDs differ across inventory, manifest, and ledger")
    if set(configured) != expected_ids:
        raise ContractViolation("Configured bank IDs differ from frozen inventory")
    for bank_id in sorted(expected_ids):
        frozen = _identity(inventory_by_id[bank_id])
        if _identity(manifest_by_id[bank_id]) != frozen or _identity(ledger_by_id[bank_id]) != frozen:
            raise ContractViolation(f"Frozen identity sources disagree for {bank_id}")
        short = configured[bank_id]
        if (
            short.get("filename") != frozen["filename"]
            or short.get("bank_csv_sha256") != frozen["bank_csv_sha256"]
            or int(short.get("size_bytes")) != frozen["size_bytes"]
        ):
            raise ContractViolation(f"Configured bank binding differs for {bank_id}")
    files = sorted(path.name for path in bank_dir.glob("*.csv"))
    expected_files = sorted(str(row["filename"]) for row in inventory)
    if files != expected_files:
        raise ContractViolation("Official bank filenames differ from the frozen set")
    inputs = materializer.load_inputs(root)
    plans = {plan.bank_id: plan for plan in materializer.validate_replicates(inputs)}
    if set(plans) != expected_ids:
        raise ContractViolation("Versioned materialization plans differ from frozen bank IDs")
    before = {name: (sha256_file(bank_dir / name), (bank_dir / name).stat().st_size) for name in files}
    observed_entries: list[dict[str, Any]] = []
    for bank_id in sorted(expected_ids):
        observed = materializer.audit_bank(
            plans[bank_id], inputs, bank_dir / inventory_by_id[bank_id]["filename"]
        )
        if _identity(observed) != _identity(inventory_by_id[bank_id]):
            raise ContractViolation(f"Official bank identity mismatch: {bank_id}")
        observed_entries.append(_identity(observed))
    after = {name: (sha256_file(bank_dir / name), (bank_dir / name).stat().st_size) for name in files}
    if before != after:
        raise ContractViolation("Official bank content changed during read-only validation")
    return {
        "classification": "CODEX_LOCAL_BANK_PREFLIGHT / NOT_INDEPENDENT_GITHUB_RUNTIME_OBSERVATION",
        "bank_count": len(observed_entries),
        "h150_count": sum(row["condition"] == "H150" for row in observed_entries),
        "h200_count": sum(row["condition"] == "H200" for row in observed_entries),
        "bank_identity_mismatch_count": 0,
        "official_bank_write_count": 0,
        "official_bank_content_mutated": False,
        "bank_directory": str(bank_dir.resolve()),
        "bank_identities": observed_entries,
    }


def build_preflight(
    config_path: Path,
    bank_dir_override: Path | None = None,
    allow_authorization_artifact: bool = False,
) -> dict[str, Any]:
    root = project_root()
    config = _read_json(config_path)
    _validate_config(config)
    output_root = root / config["paths"]["official_output_root"]
    if output_root.exists():
        raise ContractViolation(f"Official output root already exists: {output_root}")
    authorization = root / config["paths"]["future_authorization"]
    marker_root = root / config["paths"]["attempt_marker_root"]
    if authorization.exists() and not allow_authorization_artifact:
        raise ContractViolation("Future authorization artifact must not exist during package readiness")
    if marker_root.exists() and not allow_authorization_artifact:
        raise ContractViolation("Real consumption marker root must not exist during package readiness")
    source_bindings = _validate_source_bindings(root, config)
    inputs = _validate_eval_and_h100(root, config)
    bank_dir = bank_dir_override or (root / config["paths"]["bank_directory"])
    banks = _validate_banks(root, config, bank_dir.resolve())
    return {
        "status": "PASS",
        "mode": "PREFLIGHT_ONLY",
        "baseline_commit": _git(root, "rev-parse", "HEAD"),
        "bank_count": banks["bank_count"],
        "h150_count": banks["h150_count"],
        "h200_count": banks["h200_count"],
        "bank_identity_mismatch_count": banks["bank_identity_mismatch_count"],
        "eval_sha_match": inputs["eval"]["sha256"] == config["input_bindings"]["eval"]["sha256"],
        "h100_sha_match": inputs["h100_control"]["sha256"] == config["input_bindings"]["h100_control"]["sha256"],
        "canonical_source_binding_mismatch_count": 0,
        "source_binding_count": len(source_bindings),
        "official_output_root_exists": False,
        "authorization_artifact_exists": authorization.exists(),
        "real_consumption_marker_root_exists": marker_root.exists(),
        "retrieval_executed": False,
        "metrics_computed": False,
        "official_bank_write_count": banks["official_bank_write_count"],
        "official_bank_content_mutated": banks["official_bank_content_mutated"],
        "runtime_evidence_classification": banks["classification"],
        "bank_identities": banks["bank_identities"],
    }


def _safe_identifier(value: Any, field: str) -> str:
    text = str(value)
    if not re.fullmatch(r"[A-Za-z0-9._-]+", text):
        raise ContractViolation(f"OFFICIAL_EXECUTION_BLOCKED_INVALID_IDENTIFIER:{field}")
    return text


def _binding_by_role(config: Mapping[str, Any], role: str) -> Mapping[str, Any]:
    for item in config["source_bindings"]:
        if item["role"] == role:
            return item
    raise ContractViolation(f"Missing source binding role: {role}")


def _validate_authorization(
    root: Path,
    config: Mapping[str, Any],
    authorization_path: Path,
    runner_path: Path = RUNNER_PATH,
    config_path: Path = CONFIG_PATH,
) -> dict[str, Any]:
    canonical_relative = Path(config["paths"]["future_authorization"])
    canonical_path = (root / canonical_relative).resolve()
    if authorization_path.resolve() != canonical_path:
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_NONCANONICAL_AUTHORIZATION_PATH")
    if not authorization_path.is_file():
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_NO_AUTHORIZATION")
    if authorization_path.is_symlink():
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_NOT_REGULAR_FILE")
    execution_head = _git(root, "rev-parse", "HEAD")
    canonical_relative_text = canonical_relative.as_posix()
    try:
        authorization_head_blob = _blob_at(root, execution_head, canonical_relative_text)
        authorization_head_sha = _sha256_at(root, execution_head, canonical_relative_text)
    except ContractViolation as error:
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_NOT_VERSIONED") from error
    authorization_working_blob = _working_blob(root, canonical_relative_text)
    authorization_working_sha = sha256_file(authorization_path)
    if (
        authorization_working_blob != authorization_head_blob
        or authorization_working_sha != authorization_head_sha
    ):
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_WORKTREE_DRIFT")
    authorization = _read_json(authorization_path)
    missing = [field for field in config["authorization_contract"]["required_fields"] if field not in authorization]
    if missing:
        raise ContractViolation(f"OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_FIELDS_MISSING:{','.join(missing)}")
    if authorization.get("authorization_status") != "AUTHORIZED_ONE_SHOT":
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_INVALID_AUTHORIZATION_STATUS")
    _safe_identifier(authorization["authorization_id"], "authorization_id")
    _safe_identifier(authorization["attempt_id"], "attempt_id")
    approved = str(authorization["approved_package_commit"])
    try:
        _git(root, "cat-file", "-e", f"{approved}^{{commit}}")
    except ContractViolation as error:
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_APPROVED_PACKAGE_COMMIT_MISSING") from error
    if not _is_ancestor(root, approved, execution_head):
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_PACKAGE_NOT_ANCESTOR")
    expected_paths = {
        "runner_path": runner_path.as_posix(),
        "config_path": config_path.as_posix(),
    }
    for field, expected in expected_paths.items():
        if authorization.get(field) != expected:
            raise ContractViolation(f"OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_BINDING_MISMATCH:{field}")
    file_bindings = (
        ("runner", runner_path.as_posix()),
        ("config", config_path.as_posix()),
    )
    for prefix, relative_path in file_bindings:
        expected_blob = str(authorization[f"{prefix}_git_blob"])
        expected_sha = str(authorization[f"{prefix}_sha256"])
        package_blob = _blob_at(root, approved, relative_path)
        head_blob = _blob_at(root, execution_head, relative_path)
        working_blob = _working_blob(root, relative_path)
        package_sha = _sha256_at(root, approved, relative_path)
        head_sha = _sha256_at(root, execution_head, relative_path)
        if not (package_blob == head_blob == working_blob == expected_blob):
            raise ContractViolation(f"OFFICIAL_EXECUTION_BLOCKED_{prefix.upper()}_BLOB_DRIFT")
        if not (package_sha == head_sha == expected_sha):
            raise ContractViolation(f"OFFICIAL_EXECUTION_BLOCKED_{prefix.upper()}_SHA_DRIFT")
    required = {
        "eval_sha256": config["input_bindings"]["eval"]["sha256"],
        "bank_manifest_sha256": _binding_by_role(config, "bank_materialization_manifest")["sha256"],
        "bank_ledger_sha256": _binding_by_role(config, "frozen_bank_ledger")["sha256"],
        "portability_closure_blob": _binding_by_role(config, "portability_closure_record")["git_blob"],
        "expected_banks": 20,
        "official_output_root": config["paths"]["official_output_root"],
    }
    for field, expected in required.items():
        if authorization.get(field) != expected:
            raise ContractViolation(f"OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_BINDING_MISMATCH:{field}")
    return {
        **authorization,
        "execution_head": execution_head,
        "authorization_path": canonical_relative_text,
        "authorization_git_blob": authorization_head_blob,
        "authorization_sha256": authorization_head_sha,
    }


def _marker_path(marker_root: Path, authorization: Mapping[str, Any]) -> Path:
    authorization_id = _safe_identifier(authorization["authorization_id"], "authorization_id")
    attempt_id = _safe_identifier(authorization["attempt_id"], "attempt_id")
    return marker_root / f"{authorization_id}--{attempt_id}.json"


def _consume_authorization(
    marker_root: Path,
    authorization: Mapping[str, Any],
    execution_head: str,
    started_at_utc: str | None = None,
) -> Path:
    marker_root.mkdir(parents=True, exist_ok=True)
    marker = _marker_path(marker_root, authorization)
    payload = {
        "authorization_id": authorization["authorization_id"],
        "attempt_id": authorization["attempt_id"],
        "approved_package_commit": authorization["approved_package_commit"],
        "execution_head": execution_head,
        "started_at_utc": started_at_utc or _utc_now(),
        "status": "CONSUMED_EXECUTION_STARTED",
    }
    try:
        with marker.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
    except FileExistsError as error:
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_ALREADY_CONSUMED") from error
    return marker


def _new_context() -> dict[str, str]:
    return {
        "current_run_id": "NOT_STARTED",
        "current_bank_id": "NOT_STARTED",
        "current_condition": "NOT_STARTED",
        "current_stage": "NOT_STARTED",
    }


def _set_context(context: dict[str, str], **values: str) -> None:
    context.update(values)
    if context["current_stage"] not in FAILURE_STAGES:
        raise ContractViolation(f"Unknown failure stage: {context['current_stage']}")


def _failure_payload(context: Mapping[str, str], error: BaseException) -> dict[str, Any]:
    return {
        "run_id": context["current_run_id"],
        "bank_id": context["current_bank_id"],
        "condition": context["current_condition"],
        "status": "FAIL_CLOSED",
        "failure_stage": context["current_stage"],
        "error": f"{type(error).__name__}: {error}",
        "preserved_at_utc": _utc_now(),
    }


def _evaluate_bank_streaming(
    identity: Mapping[str, Any],
    bank_rows: Sequence[Mapping[str, str]],
    eval_rows: Sequence[Mapping[str, str]],
    case_writer: csv.DictWriter,
    candidate_writer: csv.DictWriter,
    context: dict[str, str],
    before_first_score: Callable[[], None] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    bank_id = str(identity["bank_id"])
    condition = str(identity["condition"])
    seed = int(identity["seed"])
    run_id = f"{bank_id}_OFFICIAL_V01"
    _set_context(
        context,
        current_run_id=run_id,
        current_bank_id=bank_id,
        current_condition=condition,
        current_stage="INDEX_BUILD",
    )
    index = historical._build_bm25_index(bank_rows)
    counts = {k: 0 for k in (1, 3, 5, 10, 50)}
    mrr_total = 0.0
    score_boundary = before_first_score
    for eval_row in eval_rows:
        _set_context(context, current_stage="EVAL_SCORING")
        query = historical._clean(eval_row.get(historical.QUERY_COLUMN))
        reference = historical._clean(eval_row.get(historical.LABEL_COLUMN))
        if score_boundary is not None:
            score_boundary()
            score_boundary = None
        scores = historical._bm25_scores(query, index, k1=1.5, b=0.75)
        candidates = historical._dedup_candidates(scores, bank_rows, len(bank_rows), 100)
        rank = historical._rank_of(candidates, reference)
        reciprocal = mrr_from_rank(rank)
        mrr_total += reciprocal
        for k in counts:
            counts[k] += int(0 < rank <= k)
        case_id = historical._clean(eval_row.get("case_id"))
        _set_context(context, current_stage="CASE_WRITE")
        case_writer.writerow(
            {
                "run_id": run_id,
                "bank_id": bank_id,
                "condition": condition,
                "seed": seed,
                "case_id": case_id,
                "id_unico": historical._clean(eval_row.get("id_unico")),
                "reference_nandina": reference,
                "reference_rank": rank,
                "reciprocal_rank": reciprocal,
                "hit_at_1": int(0 < rank <= 1),
                "hit_at_3": int(0 < rank <= 3),
                "hit_at_5": int(0 < rank <= 5),
                "hit_at_10": int(0 < rank <= 10),
                "hit_at_50": int(0 < rank <= 50),
                "top1_nandina": historical._clean(candidates[0].get("candidate_nandina")) if candidates else "",
                "candidate_count": len(candidates),
                "ranking_depth": 100,
                "method": METHOD,
            }
        )
        for candidate in candidates:
            candidate_writer.writerow(
                {
                    "run_id": run_id,
                    "bank_id": bank_id,
                    "condition": condition,
                    "seed": seed,
                    "case_id": case_id,
                    "candidate_rank": candidate["candidate_rank"],
                    "candidate_nandina": candidate["candidate_nandina"],
                    "candidate_history_rank": candidate["candidate_history_rank"],
                    "candidate_case_id": candidate["candidate_case_id"],
                    "candidate_id_unico": candidate["candidate_id_unico"],
                    "score": candidate["score"],
                    "method": METHOD,
                }
            )
    _set_context(context, current_stage="METRIC_FINALIZATION")
    n_eval = len(eval_rows)
    metrics: dict[str, Any] = {
        "run_id": run_id,
        "bank_id": bank_id,
        "condition": condition,
        "seed": seed,
        "primary_n": n_eval,
        "mrr_numerator": mrr_total,
        "mrr": mrr_total / n_eval if n_eval else 0.0,
    }
    for k, numerator in counts.items():
        metrics[f"top_{k}_numerator"] = numerator
        metrics[f"top_{k}"] = numerator / n_eval if n_eval else 0.0
    run = {
        "run_id": run_id,
        "bank_id": bank_id,
        "condition": condition,
        "seed": seed,
        "base_commit": "SET_BY_CALLER",
        "retrieval_config_sha256": "SET_BY_CALLER",
        "bank_csv_sha256": identity["bank_csv_sha256"],
        "evalset_sha256": "SET_BY_CALLER",
        "environment": "exp11b_retrieval_environment_v0.1.json",
        "status": "COMPLETED",
    }
    return metrics, run


def _package_versions() -> dict[str, str]:
    output: dict[str, str] = {}
    for package in ("numpy", "pandas"):
        try:
            output[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            output[package] = "not-installed"
    return output


def _summary_rows(metrics_rows: Sequence[Mapping[str, Any]], expected_by_condition: Mapping[str, int]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for condition, expected_runs in expected_by_condition.items():
        rows = [row for row in metrics_rows if row["condition"] == condition]
        if not rows:
            raise ContractViolation(f"No completed metric rows for condition {condition}")
        summary: dict[str, Any] = {
            "condition": condition,
            "expected_runs": expected_runs,
            "completed_runs": len(rows),
            "primary_n": 1056,
            "status": "COMPLETED",
        }
        for metric in ("top_1", "top_3", "top_5", "top_10", "top_50", "mrr"):
            summary[f"{metric}_mean"] = sum(float(row[metric]) for row in rows) / len(rows)
        summaries.append(summary)
    return summaries


def _finalize_outputs(
    root: Path,
    config_path: Path,
    config: Mapping[str, Any],
    staging: Path,
    metrics_rows: Sequence[Mapping[str, Any]],
    runs: Sequence[Mapping[str, Any]],
    authorization: Mapping[str, Any],
    expected_by_condition: Mapping[str, int],
) -> None:
    files = config["output_contract"]["files"]
    _write_csv(staging / files["metrics_by_bank_csv"], metrics_rows, METRIC_FIELDS)
    _write_csv(
        staging / files["condition_summary_csv"],
        _summary_rows(metrics_rows, expected_by_condition),
        SUMMARY_FIELDS,
    )
    environment = {
        "python": sys.version,
        "platform": platform.platform(),
        "packages": _package_versions(),
        "git_commit": _git(root, "rev-parse", "HEAD"),
        "command": " ".join(sys.argv),
    }
    _write_json(staging / files["environment_json"], environment)
    _write_json(
        staging / files["failure_ledger_json"],
        {
            "run_id": "EXP11B_H150_H200_ONE_SHOT",
            "bank_id": "NONE",
            "condition": "NONE",
            "status": "NO_FAILURES",
            "failure_stage": "NONE",
            "error": "",
            "preserved_at_utc": _utc_now(),
        },
    )
    _write_json(
        staging / files["run_manifest_json"],
        {
            "experiment_id": "EXP-11B",
            "status": "COMPLETED",
            "authorization": dict(authorization),
            "runs": list(runs),
            "retrieval_executed": True,
            "evaluation_metrics_computed": True,
            "completed_at_utc": _utc_now(),
        },
    )
    hash_rows = []
    for path in sorted(staging.iterdir(), key=lambda item: item.name):
        if path.name == files["output_hash_ledger_csv"]:
            continue
        hash_rows.append(
            {
                "artifact": path.name,
                "sha256": sha256_file(path),
                "size_bytes": path.stat().st_size,
                "role": "official_exp11b_output",
            }
        )
    _write_csv(staging / files["output_hash_ledger_csv"], hash_rows, HASH_FIELDS)


def _run_streaming_package(
    root: Path,
    config_path: Path,
    config: Mapping[str, Any],
    final_root: Path,
    bank_specs: Sequence[Mapping[str, Any]],
    eval_rows: Sequence[Mapping[str, str]],
    authorization: Mapping[str, Any],
    expected_by_condition: Mapping[str, int],
    before_first_scoring: Callable[[], None] | None = None,
) -> dict[str, Any]:
    if final_root.exists():
        raise ContractViolation(f"Output root already exists: {final_root}")
    staging = final_root.with_name(final_root.name + f".staging-{uuid.uuid4().hex}")
    staging.mkdir(parents=True)
    files = config["output_contract"]["files"]
    context = _new_context()
    metrics_rows: list[dict[str, Any]] = []
    runs: list[dict[str, Any]] = []
    first_bank = True
    case_handle: TextIO | None = None
    candidate_handle: TextIO | None = None
    try:
        case_handle, case_writer = _open_stream(staging / files["case_level_csv"], CASE_FIELDS)
        candidate_handle, candidate_writer = _open_stream(
            staging / files["candidate_ranking_csv"], CANDIDATE_FIELDS
        )
        for spec in bank_specs:
            identity = spec["identity"]
            _set_context(
                context,
                current_run_id=f"{identity['bank_id']}_OFFICIAL_V01",
                current_bank_id=str(identity["bank_id"]),
                current_condition=str(identity["condition"]),
                current_stage="BANK_VALIDATION",
            )
            bank_path = Path(spec["path"])
            if sha256_file(bank_path) != identity["bank_csv_sha256"]:
                raise ContractViolation(f"Bank SHA drift before scoring: {identity['bank_id']}")
            bank_rows = historical._read_csv(bank_path)
            if len(bank_rows) != int(identity["row_count"]):
                raise ContractViolation(f"Bank row-count drift before scoring: {identity['bank_id']}")
            metrics, run = _evaluate_bank_streaming(
                identity,
                bank_rows,
                eval_rows,
                case_writer,
                candidate_writer,
                context,
                before_first_score=before_first_scoring if first_bank else None,
            )
            first_bank = False
            run["base_commit"] = _git(root, "rev-parse", "HEAD")
            run["retrieval_config_sha256"] = sha256_file(config_path)
            run["evalset_sha256"] = config["input_bindings"]["eval"]["sha256"]
            metrics_rows.append(metrics)
            runs.append(run)
            case_handle.flush()
            candidate_handle.flush()
            del bank_rows
        case_handle.close()
        candidate_handle.close()
        case_handle = None
        candidate_handle = None
        _set_context(
            context,
            current_run_id="EXP11B_H150_H200_ONE_SHOT",
            current_bank_id="NOT_STARTED",
            current_condition="NOT_STARTED",
            current_stage="OUTPUT_FINALIZATION",
        )
        _finalize_outputs(
            root, config_path, config, staging, metrics_rows, runs, authorization, expected_by_condition
        )
        staging.replace(final_root)
    except Exception as error:
        if case_handle is not None:
            case_handle.close()
        if candidate_handle is not None:
            candidate_handle.close()
        _write_json(staging / files["failure_ledger_json"], _failure_payload(context, error))
        failed = final_root.with_name(final_root.name + f".failed-{uuid.uuid4().hex}")
        staging.replace(failed)
        raise
    return {
        "status": "COMPLETED",
        "output_root": str(final_root),
        "bank_count": len(metrics_rows),
        "metrics_rows": metrics_rows,
        "stream_case_level_output": True,
        "stream_candidate_output": True,
        "global_case_accumulator": False,
        "global_candidate_accumulator": False,
    }


def _read_csv_header(path: Path) -> list[str]:
    with path.open(encoding="utf-8", newline="") as handle:
        return next(csv.reader(handle))


def _validate_output_schema(root: Path, config: Mapping[str, Any], output_root: Path) -> dict[str, Any]:
    gate = _read_json(root / config["output_contract"]["gate_contract_path"])
    frozen = gate["future_output_contract"]["files"]
    files = config["output_contract"]["files"]
    schema_results: dict[str, str] = {}
    for key, contract in frozen.items():
        if files.get(key) != contract["filename"]:
            raise ContractViolation(f"Output filename contract mismatch: {key}")
        path = output_root / files[key]
        if not path.is_file():
            raise ContractViolation(f"Shadow output missing: {path.name}")
        if "columns" in contract:
            if _read_csv_header(path) != contract["columns"]:
                raise ContractViolation(f"Output columns mismatch: {key}")
        else:
            payload = _read_json(path)
            required = set(contract["required_fields"])
            if key == "run_manifest_json":
                runs = payload.get("runs")
                if not isinstance(runs, list) or not runs:
                    raise ContractViolation("Run manifest has no run records")
                if any(not required.issubset(run) for run in runs):
                    raise ContractViolation("Run manifest record schema mismatch")
            elif not required.issubset(payload):
                raise ContractViolation(f"Output JSON schema mismatch: {key}")
        schema_results[key] = "PASS"
    return {"status": "PASS", "schemas": schema_results, "validated_file_count": len(schema_results)}


def run_h100_self_test(config_path: Path) -> dict[str, Any]:
    root = project_root()
    config = _read_json(config_path)
    _validate_config(config)
    _validate_source_bindings(root, config)
    inputs = _validate_eval_and_h100(root, config)
    h100_path = Path(inputs["h100_control"]["path"])
    eval_rows = historical._read_csv(Path(inputs["eval"]["path"]))
    temporary_path_text = ""
    with tempfile.TemporaryDirectory(prefix="exp11b_h100_full_output_shadow_") as temporary:
        temporary_path = Path(temporary)
        temporary_path_text = str(temporary_path)
        shadow_root = temporary_path / "shadow_output"
        identity = {
            "bank_id": "H100_CONTROL",
            "condition": "H100",
            "seed": 0,
            "filename": h100_path.name,
            "row_count": 2950,
            "bank_csv_sha256": config["input_bindings"]["h100_control"]["sha256"],
        }
        result = _run_streaming_package(
            root,
            config_path,
            config,
            shadow_root,
            [{"identity": identity, "path": h100_path}],
            eval_rows,
            {
                "authorization_id": "SYNTHETIC_H100_SHADOW",
                "attempt_id": "SYNTHETIC_H100_SHADOW",
                "authorization_status": "SHADOW_ONLY_NOT_OFFICIAL",
            },
            {"H100": 1},
        )
        schema = _validate_output_schema(root, config, shadow_root)
        metrics = result["metrics_rows"][0]
        expected = config["input_bindings"]["h100_reference_metrics"]
        deltas: dict[str, int] = {}
        for k, numerator in expected["top_numerators"].items():
            observed = int(metrics[f"top_{k}_numerator"])
            if observed != int(numerator):
                raise ContractViolation(f"H100 Top{k} numerator mismatch: {observed}")
            deltas[f"top_{k}_numerator_delta"] = observed - int(numerator)
        mrr_delta = float(metrics["mrr"]) - float(expected["mrr"])
        if abs(mrr_delta) > float(expected["mrr_abs_tolerance"]):
            raise ContractViolation(f"H100 MRR mismatch: delta={mrr_delta}")
        shadow_files = sorted(path.name for path in shadow_root.iterdir())
    temporary_cleanup = not Path(temporary_path_text).exists()
    if not temporary_cleanup:
        raise ContractViolation("Temporary H100 full-output shadow was not removed")
    return {
        "status": "PASS",
        "mode": "SELF_TEST_H100_FULL_OUTPUT_SHADOW_ONLY",
        "top_numerators": {str(k): int(metrics[f"top_{k}_numerator"]) for k in (1, 3, 5, 10, 50)},
        "numerator_deltas": deltas,
        "mrr": metrics["mrr"],
        "mrr_expected": expected["mrr"],
        "mrr_delta": mrr_delta,
        "mrr_abs_tolerance": expected["mrr_abs_tolerance"],
        "output_schema_validation": schema,
        "shadow_files": shadow_files,
        "temporary_self_test_cleanup": "PASS",
        "h150_h200_banks_opened": 0,
        "official_output_root_exists": (root / config["paths"]["official_output_root"]).exists(),
        "stream_case_level_output": result["stream_case_level_output"],
        "stream_candidate_output": result["stream_candidate_output"],
        "global_case_accumulator": result["global_case_accumulator"],
        "global_candidate_accumulator": result["global_candidate_accumulator"],
    }


def execute_official(config_path: Path, bank_dir_override: Path | None, authorization_path: Path) -> dict[str, Any]:
    root = project_root()
    if config_path.resolve() != (root / CONFIG_PATH).resolve():
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_NONCANONICAL_CONFIG_PATH")
    config = _read_json(config_path)
    _validate_config(config)
    authorization = _validate_authorization(root, config, authorization_path)
    preflight = build_preflight(config_path, bank_dir_override, allow_authorization_artifact=True)
    output_root = root / config["paths"]["official_output_root"]
    if output_root.exists():
        raise ContractViolation("Official output root exists; overwrite and resume are forbidden")
    bank_dir = bank_dir_override or (root / config["paths"]["bank_directory"])
    eval_rows = historical._read_csv(root / config["paths"]["eval"])
    bank_specs = [
        {"identity": identity, "path": bank_dir / identity["filename"]}
        for identity in preflight["bank_identities"]
    ]
    marker_root = root / config["paths"]["attempt_marker_root"]
    marker = _marker_path(marker_root, authorization)
    if marker.exists():
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_ALREADY_CONSUMED")

    def consume_immediately_before_scoring() -> None:
        _consume_authorization(marker_root, authorization, authorization["execution_head"])

    result = _run_streaming_package(
        root,
        config_path,
        config,
        output_root,
        bank_specs,
        eval_rows,
        authorization,
        {"H150": 10, "H200": 10},
        before_first_scoring=consume_immediately_before_scoring,
    )
    return {
        "status": result["status"],
        "output_root": result["output_root"],
        "bank_count": result["bank_count"],
        "authorization_consumed": True,
        "consumption_marker": str(marker),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate or prospectively execute the frozen EXP-11B H150/H200 historical BM25 package v0.3."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true", help="Validate contracts and banks only; never run retrieval.")
    mode.add_argument("--self-test-h100", action="store_true", help="Run the frozen H100 full-output shadow only.")
    mode.add_argument("--execute-official", action="store_true", help="Require and consume a separate one-shot authorization before scoring.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--bank-dir", default=None, help="Read-only override for the local official bank directory.")
    parser.add_argument(
        "--authorization",
        default=None,
        help="Must resolve exactly to the canonical future authorization path.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    config_path = resolve_project_path(args.config)
    bank_dir = Path(args.bank_dir).expanduser().resolve() if args.bank_dir else None
    try:
        if args.preflight:
            result = build_preflight(config_path, bank_dir)
        elif args.self_test_h100:
            result = run_h100_self_test(config_path)
        else:
            config = _read_json(config_path)
            authorization = (
                Path(args.authorization).expanduser().resolve()
                if args.authorization
                else resolve_project_path(config["paths"]["future_authorization"])
            )
            result = execute_official(config_path, bank_dir, authorization)
    except ContractViolation as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
