"""Prospective one-shot EXP-11B H150/H200 historical retrieval runner.

Prompt44 prepares this package but does not authorize official execution. The
preflight only validates frozen contracts and banks; the H100 self-test never
opens an H150/H200 bank; and official execution is guarded by a separate,
future authorization artifact.
"""

from __future__ import annotations

import argparse
import csv
import importlib.metadata
import json
import platform
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import mrr_from_rank
from ..utils.paths import project_root, resolve_project_path
from . import evaluate_historical_retrieval_data_aduanas_v02 as historical
from . import materialize_exp11b_banks_v01 as materializer


DEFAULT_CONFIG = Path("src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.1.json")
RUNNER_PATH = Path("src/experiments/run_exp11b_historical_retrieval_h150_h200_v01.py")
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
    "run_id",
    "bank_id",
    "condition",
    "seed",
    "case_id",
    "id_unico",
    "reference_nandina",
    "reference_rank",
    "reciprocal_rank",
    "hit_at_1",
    "hit_at_3",
    "hit_at_5",
    "hit_at_10",
    "hit_at_50",
    "top1_nandina",
    "candidate_count",
    "ranking_depth",
    "method",
)
CANDIDATE_FIELDS = (
    "run_id",
    "bank_id",
    "condition",
    "seed",
    "case_id",
    "candidate_rank",
    "candidate_nandina",
    "candidate_history_rank",
    "candidate_case_id",
    "candidate_id_unico",
    "score",
    "method",
)
METRIC_FIELDS = (
    "run_id",
    "bank_id",
    "condition",
    "seed",
    "primary_n",
    "top_1_numerator",
    "top_1",
    "top_3_numerator",
    "top_3",
    "top_5_numerator",
    "top_5",
    "top_10_numerator",
    "top_10",
    "top_50_numerator",
    "top_50",
    "mrr_numerator",
    "mrr",
)


class ContractViolation(RuntimeError):
    """Raised when a prospective EXP-11B execution invariant fails."""


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


def _git(root: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args], cwd=root, check=True, text=True, capture_output=True
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise ContractViolation(f"Git binding command failed: {' '.join(args)}") from error
    return result.stdout.strip()


def _working_blob(root: Path, relative_path: str) -> str:
    path = root / relative_path
    if not path.is_file():
        raise ContractViolation(f"Bound source is missing: {relative_path}")
    return _git(root, "hash-object", f"--path={relative_path}", str(path))


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
        "contract_status": "CANDIDATE_EXECUTION_PACKAGE_PENDING_EXTERNAL_AUDIT",
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


def _validate_source_bindings(root: Path, config: Mapping[str, Any]) -> list[dict[str, str]]:
    observed: list[dict[str, str]] = []
    for binding in config.get("source_bindings", []):
        path = str(binding["path"])
        expected = str(binding["git_blob"])
        actual = _working_blob(root, path)
        if actual != expected:
            raise ContractViolation(f"Source binding mismatch for {path}: {actual}")
        if binding.get("sha256"):
            actual_sha = sha256_file(root / path)
            if actual_sha != binding["sha256"]:
                raise ContractViolation(f"Source SHA-256 mismatch for {path}: {actual_sha}")
        observed.append({"path": path, "git_blob": actual, "role": str(binding["role"])})
    return observed


def _validate_eval_and_h100(root: Path, config: Mapping[str, Any]) -> dict[str, Any]:
    observed: dict[str, Any] = {}
    for name in ("eval", "h100_control"):
        binding = config["input_bindings"][name]
        path = resolve_project_path(binding["path"])
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
    inventory_path = root / config["bank_contract_sources"]["inventory_path"]
    manifest_path = root / config["bank_contract_sources"]["manifest_path"]
    ledger_path = root / config["bank_contract_sources"]["ledger_path"]
    inventory = _read_json(inventory_path).get("bank_identities")
    manifest = _read_json(manifest_path).get("banks")
    ledger = _load_ledger(ledger_path)
    if not all(isinstance(items, list) and len(items) == 20 for items in (inventory, manifest, ledger)):
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
    observed_entries: list[dict[str, Any]] = []
    before = {name: (sha256_file(bank_dir / name), (bank_dir / name).stat().st_size) for name in files}
    for bank_id in sorted(expected_ids):
        observed = materializer.audit_bank(plans[bank_id], inputs, bank_dir / inventory_by_id[bank_id]["filename"])
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
    if authorization.exists() and not allow_authorization_artifact:
        raise ContractViolation("Future authorization artifact must not exist during package readiness")
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
        "retrieval_executed": False,
        "metrics_computed": False,
        "official_bank_write_count": banks["official_bank_write_count"],
        "official_bank_content_mutated": banks["official_bank_content_mutated"],
        "runtime_evidence_classification": banks["classification"],
        "bank_identities": banks["bank_identities"],
    }


def _evaluate_bank(
    bank_id: str,
    condition: str,
    seed: int,
    bank_rows: Sequence[Mapping[str, str]],
    eval_rows: Sequence[Mapping[str, str]],
    include_candidates: bool,
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    index = historical._build_bm25_index(bank_rows)
    counts = {k: 0 for k in (1, 3, 5, 10, 50)}
    mrr_total = 0.0
    case_rows: list[dict[str, Any]] = []
    candidate_rows: list[dict[str, Any]] = []
    run_id = f"{bank_id}_OFFICIAL_V01"
    for eval_row in eval_rows:
        query = historical._clean(eval_row.get(historical.QUERY_COLUMN))
        reference = historical._clean(eval_row.get(historical.LABEL_COLUMN))
        scores = historical._bm25_scores(query, index, k1=1.5, b=0.75)
        candidates = historical._dedup_candidates(scores, bank_rows, len(bank_rows), 100)
        rank = historical._rank_of(candidates, reference)
        reciprocal = mrr_from_rank(rank)
        mrr_total += reciprocal
        for k in counts:
            counts[k] += int(0 < rank <= k)
        case_id = historical._clean(eval_row.get("case_id"))
        case_rows.append(
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
        if include_candidates:
            for candidate in candidates:
                candidate_rows.append(
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
    return metrics, case_rows, candidate_rows


def run_h100_self_test(config_path: Path) -> dict[str, Any]:
    root = project_root()
    config = _read_json(config_path)
    _validate_config(config)
    _validate_source_bindings(root, config)
    inputs = _validate_eval_and_h100(root, config)
    h100_rows = historical._read_csv(Path(inputs["h100_control"]["path"]))
    eval_rows = historical._read_csv(Path(inputs["eval"]["path"]))
    temporary_cleanup = False
    with tempfile.TemporaryDirectory(prefix="exp11b_h100_self_test_") as temporary:
        temporary_path = Path(temporary)
        metrics, _cases, _candidates = _evaluate_bank(
            "H100_CONTROL", "H100", 0, h100_rows, eval_rows, include_candidates=False
        )
        _write_json(temporary_path / "h100_self_test_summary.json", metrics)
    temporary_cleanup = not Path(temporary).exists()
    expected = config["input_bindings"]["h100_reference_metrics"]
    deltas: dict[str, Any] = {}
    for k, numerator in expected["top_numerators"].items():
        observed = int(metrics[f"top_{k}_numerator"])
        if observed != int(numerator):
            raise ContractViolation(f"H100 Top{k} numerator mismatch: {observed}")
        deltas[f"top_{k}_numerator_delta"] = observed - int(numerator)
    mrr_delta = float(metrics["mrr"]) - float(expected["mrr"])
    if abs(mrr_delta) > float(expected["mrr_abs_tolerance"]):
        raise ContractViolation(f"H100 MRR mismatch: delta={mrr_delta}")
    if not temporary_cleanup:
        raise ContractViolation("Temporary H100 self-test output was not removed")
    return {
        "status": "PASS",
        "mode": "SELF_TEST_H100_ONLY",
        "top_numerators": {str(k): int(metrics[f"top_{k}_numerator"]) for k in (1, 3, 5, 10, 50)},
        "mrr": metrics["mrr"],
        "mrr_expected": expected["mrr"],
        "mrr_delta": mrr_delta,
        "mrr_abs_tolerance": expected["mrr_abs_tolerance"],
        "numerator_deltas": deltas,
        "temporary_self_test_cleanup": "PASS",
        "h150_h200_banks_opened": 0,
        "official_output_root_exists": (root / config["paths"]["official_output_root"]).exists(),
    }


def _validate_authorization(root: Path, config: Mapping[str, Any], authorization_path: Path) -> dict[str, Any]:
    if not authorization_path.is_file():
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_NO_AUTHORIZATION")
    authorization = _read_json(authorization_path)
    if authorization.get("authorization_status") != "AUTHORIZED_ONE_SHOT":
        raise ContractViolation("OFFICIAL_EXECUTION_BLOCKED_INVALID_AUTHORIZATION_STATUS")
    package_commit = _git(root, "rev-parse", "HEAD")
    runner_blob = _working_blob(root, RUNNER_PATH.as_posix())
    config_blob = _working_blob(root, CONFIG_PATH.as_posix())
    bindings_by_role = {str(item["role"]): item for item in config["source_bindings"]}
    required = {
        "package_commit": package_commit,
        "runner_git_blob": runner_blob,
        "config_git_blob": config_blob,
        "eval_sha256": config["input_bindings"]["eval"]["sha256"],
        "ledger_sha256": bindings_by_role["frozen_bank_ledger"]["sha256"],
        "manifest_sha256": bindings_by_role["bank_materialization_manifest"]["sha256"],
        "closure_record_blob": bindings_by_role["portability_closure_record"]["git_blob"],
        "expected_banks": 20,
        "official_output_root": config["paths"]["official_output_root"],
    }
    for field, expected in required.items():
        if authorization.get(field) != expected:
            raise ContractViolation(f"OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_BINDING_MISMATCH:{field}")
    return authorization


def _package_versions() -> dict[str, str]:
    output: dict[str, str] = {}
    for package in ("numpy", "pandas"):
        try:
            output[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            output[package] = "not-installed"
    return output


def execute_official(config_path: Path, bank_dir_override: Path | None, authorization_path: Path) -> dict[str, Any]:
    root = project_root()
    config = _read_json(config_path)
    _validate_config(config)
    authorization = _validate_authorization(root, config, authorization_path)
    preflight = build_preflight(config_path, bank_dir_override, allow_authorization_artifact=True)
    output_root = root / config["paths"]["official_output_root"]
    if output_root.exists():
        raise ContractViolation("Official output root exists; overwrite and resume are forbidden")
    bank_dir = bank_dir_override or (root / config["paths"]["bank_directory"])
    eval_rows = historical._read_csv(root / config["paths"]["eval"])
    staging = output_root.with_name(output_root.name + f".staging-{uuid.uuid4().hex}")
    if staging.exists():
        raise ContractViolation(f"Unexpected staging path collision: {staging}")
    staging.mkdir(parents=True)
    metrics_rows: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []
    candidate_rows: list[dict[str, Any]] = []
    runs: list[dict[str, Any]] = []
    try:
        for identity in preflight["bank_identities"]:
            bank_path = bank_dir / identity["filename"]
            bank_rows = historical._read_csv(bank_path)
            metrics, cases, candidates = _evaluate_bank(
                identity["bank_id"], identity["condition"], int(identity["seed"]), bank_rows, eval_rows, True
            )
            metrics_rows.append(metrics)
            case_rows.extend(cases)
            candidate_rows.extend(candidates)
            runs.append(
                {
                    "run_id": metrics["run_id"],
                    "bank_id": identity["bank_id"],
                    "condition": identity["condition"],
                    "seed": identity["seed"],
                    "base_commit": _git(root, "rev-parse", "HEAD"),
                    "retrieval_config_sha256": sha256_file(config_path),
                    "bank_csv_sha256": identity["bank_csv_sha256"],
                    "evalset_sha256": config["input_bindings"]["eval"]["sha256"],
                    "environment": "exp11b_retrieval_environment_v0.1.json",
                    "status": "COMPLETED",
                }
            )
        files = config["output_contract"]["files"]
        _write_csv(staging / files["metrics_by_bank_csv"], metrics_rows, METRIC_FIELDS)
        _write_csv(staging / files["case_level_csv"], case_rows, CASE_FIELDS)
        _write_csv(staging / files["candidate_ranking_csv"], candidate_rows, CANDIDATE_FIELDS)
        summary_rows: list[dict[str, Any]] = []
        for condition in ("H150", "H200"):
            rows = [row for row in metrics_rows if row["condition"] == condition]
            summary = {"condition": condition, "expected_runs": 10, "completed_runs": len(rows), "primary_n": 1056}
            for metric in ("top_1", "top_3", "top_5", "top_10", "top_50", "mrr"):
                summary[f"{metric}_mean"] = sum(float(row[metric]) for row in rows) / len(rows)
            summary["status"] = "COMPLETED"
            summary_rows.append(summary)
        _write_csv(
            staging / files["condition_summary_csv"],
            summary_rows,
            ("condition", "expected_runs", "completed_runs", "primary_n", "top_1_mean", "top_3_mean", "top_5_mean", "top_10_mean", "top_50_mean", "mrr_mean", "status"),
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
                "authorization": authorization,
                "runs": runs,
                "retrieval_executed": True,
                "evaluation_metrics_computed": True,
                "completed_at_utc": _utc_now(),
            },
        )
        hash_rows = []
        for path in sorted(staging.iterdir(), key=lambda item: item.name):
            if path.name == files["output_hash_ledger_csv"]:
                continue
            hash_rows.append({"artifact": path.name, "sha256": sha256_file(path), "size_bytes": path.stat().st_size, "role": "official_exp11b_output"})
        _write_csv(staging / files["output_hash_ledger_csv"], hash_rows, ("artifact", "sha256", "size_bytes", "role"))
        staging.replace(output_root)
    except Exception as error:
        failure = {
            "run_id": "EXP11B_H150_H200_ONE_SHOT",
            "bank_id": runs[-1]["bank_id"] if runs else "NOT_STARTED",
            "status": "FAIL_CLOSED",
            "failure_stage": "OFFICIAL_EXECUTION",
            "error": f"{type(error).__name__}: {error}",
            "preserved_at_utc": _utc_now(),
        }
        _write_json(staging / config["output_contract"]["files"]["failure_ledger_json"], failure)
        failed = output_root.with_name(output_root.name + f".failed-{uuid.uuid4().hex}")
        staging.replace(failed)
        raise
    return {"status": "COMPLETED", "output_root": str(output_root), "bank_count": len(metrics_rows)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate or prospectively execute the frozen EXP-11B H150/H200 historical BM25 package."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true", help="Validate contracts and banks only; never run retrieval.")
    mode.add_argument("--self-test-h100", action="store_true", help="Run the frozen H100 semantic control only.")
    mode.add_argument("--execute-official", action="store_true", help="Require a separate one-shot authorization before any retrieval.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--bank-dir", default=None, help="Read-only override for the local official bank directory.")
    parser.add_argument("--authorization", default=None, help="Path to the future one-shot authorization artifact.")
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
            authorization = Path(args.authorization).expanduser().resolve() if args.authorization else resolve_project_path(config["paths"]["future_authorization"])
            result = execute_official(config_path, bank_dir, authorization)
    except ContractViolation as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
