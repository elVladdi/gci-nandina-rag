"""Freeze and validate the prospective EXP-11B retrieval execution gate.

This module never imports or invokes the BM25 evaluator.  It validates the
already frozen contracts and writes only gate metadata when --freeze is used.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[2]
CONFIG_RELATIVE_PATH = Path("src/configs/exp11b_retrieval_execution_gate_v0.1.json")
REQUIRED_FALSE_FLAGS = (
    "retrieval_executed",
    "evaluation_metrics_computed",
    "h150_h200_results_observed",
    "exp11b_retrieval_authorized",
)
REQUIRED_LEDGER_FIELDS = (
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


class ContractViolation(ValueError):
    """Raised whenever a prospective retrieval contract is not exact."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ContractViolation(f"Expected JSON object: {path}")
    return payload


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ContractViolation(f"CSV without header: {path}")
        return [dict(row) for row in reader]


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractViolation(message)


def project_path(root: Path, relative_path: str) -> Path:
    path = (root / relative_path).resolve()
    require(path.is_relative_to(root.resolve()), f"Path escapes project root: {relative_path}")
    return path


def validate_file_contract(root: Path, entry: Mapping[str, Any], label: str) -> dict[str, Any]:
    path = project_path(root, str(entry["path"]))
    require(path.is_file(), f"Missing {label}: {entry['path']}")
    observed = sha256_file(path)
    expected = str(entry["sha256"])
    require(observed == expected, f"SHA256 mismatch for {label}: expected {expected}, found {observed}")
    return {"label": label, "path": entry["path"], "sha256": observed, "size_bytes": path.stat().st_size}


def validate_static_contract(config: Mapping[str, Any]) -> None:
    require(config.get("gate") == "EXP11B_RETRIEVAL_EXECUTION_GATE", "Incorrect gate identifier")
    require(config.get("gate_status") == "CANDIDATE_PENDING_EXTERNAL_AUDIT", "Retrieval gate status is not pending external audit")
    require(config.get("integrated_base_commit") == "95ffec45ae5a734545ae7bb2d8d530f42f8f056c", "Unexpected integrated base commit")
    for flag in REQUIRED_FALSE_FLAGS:
        require(config.get(flag) is False, f"{flag} must remain false")
    future = config["future_execution"]
    require(future["expected_banks"] == 20, "Expected bank count must be 20")
    require(future["official_runs_per_bank"] == 1, "Only one official run per bank is allowed")
    for key in ("automatic_retries", "silent_resume", "silent_overwrite", "partial_recomputation_is_official", "replace_failed_outputs", "rerun_for_unexpected_results", "configuration_mutable_after_start"):
        require(future[key] is False, f"Future execution policy must forbid {key}")
    bm25 = config["canonical_retrieval_semantics"]
    require(bm25["k1"] == 1.5 and bm25["b"] == 0.75, "BM25 k1/b differs from historical v0.2")
    require(bm25["k_values"] == [1, 3, 5, 10, 50], "Frozen k values differ from historical v0.2")
    require(bm25["candidate_depth"] == 100, "Candidate depth must remain 100")
    require(bm25["normalization"] == "unicode_NFKD_lowercase_remove_combining_marks", "Normalization differs from historical v0.2")
    require(bm25["tokenizer"] == "regex_[a-z0-9]+", "Tokenizer differs from historical v0.2")
    require(bm25["ranking_order"] == "descending_score_then_ascending_historical_case_id", "Tie handling differs from historical v0.2")
    require(bm25["candidate_deduplication"] == "first_ranked_historical_row_per_NANDINA", "Candidate deduplication differs from historical v0.2")
    require(config["common_clean"]["primary_denominator"] == 1056, "Primary denominator must remain 1056")
    require(config["common_clean"]["complementary_only"] is True, "Common-clean must remain complementary")
    require(config["future_output_contract"]["must_not_exist_until_authorized_execution"] is True, "Future result output must not be created by the gate")


def validate_base_commit(root: Path, config: Mapping[str, Any]) -> str:
    base = str(config["integrated_base_commit"])
    result = subprocess.run(["git", "merge-base", "--is-ancestor", base, "HEAD"], cwd=root, capture_output=True, text=True)
    require(result.returncode == 0, f"Candidate branch does not descend from integrated base {base}")
    return base


def validate_common_clean(root: Path, config: Mapping[str, Any]) -> dict[str, Any]:
    contract = config["materialization_contract"]
    mask_path = project_path(root, contract["gate03_common_clean_mask"]["path"])
    feasibility_path = project_path(root, contract["gate03_feasibility"]["path"])
    rows = read_csv(mask_path)
    require(len(rows) == 1056, "Common-clean mask must contain all 1056 primary cases")
    summary = load_json(feasibility_path).get("common_clean_mask_summary", {})
    frozen = config["common_clean"]
    require(summary.get("primary_eval_denominator") == frozen["primary_denominator"], "Gate 03 primary denominator differs")
    require(summary.get("primary_denominator_affected") is False, "Gate 03 alters the primary denominator")
    require(summary.get("selection_affected") is False, "Gate 03 common-clean affects selection")
    observed: dict[str, int] = {}
    for name, expected in frozen["sets"].items():
        column = expected["mask_column"]
        require(all(column in row for row in rows), f"Common-clean mask misses {column}")
        affected = sum(str(row[column]).lower() == "true" for row in rows)
        require(affected == expected["affected"], f"Common-clean affected count differs for {name}")
        require(len(rows) - affected == expected["clean_denominator"], f"Common-clean denominator differs for {name}")
        observed[name] = affected
    return {"primary_n": len(rows), "affected": observed, "clean_denominators": summary.get("clean_denominators")}


def validate_bank_identity_contract(
    config: Mapping[str, Any], ledger_rows: Sequence[Mapping[str, str]], manifest_banks: Sequence[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    contract = config["materialization_contract"]
    require(len(ledger_rows) == 20, f"Expected 20 ledger rows, found {len(ledger_rows)}")
    require(len(manifest_banks) == 20, f"Expected 20 materialization manifest banks, found {len(manifest_banks)}")
    required_fields = list(contract["required_ledger_fields"])
    require(required_fields == list(REQUIRED_LEDGER_FIELDS), "Ledger field contract differs from F003")
    for row in ledger_rows:
        require(all(field in row for field in required_fields), f"Ledger row misses F003 field(s): {row.get('bank_id', '<unknown>')}")
    expected_ids = list(contract["expected_bank_ids"])
    observed_ids = [str(row["bank_id"]) for row in ledger_rows]
    require(observed_ids == expected_ids, "Ledger bank ID order differs from the frozen contract")
    require(len(set(observed_ids)) == 20, "Ledger contains duplicate bank IDs")
    require(sum(row["condition"] == "H150" for row in ledger_rows) == 10, "Expected ten H150 banks")
    require(sum(row["condition"] == "H200" for row in ledger_rows) == 10, "Expected ten H200 banks")
    expected_seeds = list(contract["expected_seed_schedule"])
    require([int(row["seed"]) for row in ledger_rows[::2]] == expected_seeds, "H150 seed schedule differs")
    require([int(row["seed"]) for row in ledger_rows[1::2]] == expected_seeds, "H200 seed schedule differs")
    manifest_by_id = {str(bank["bank_id"]): bank for bank in manifest_banks}
    require(set(manifest_by_id) == set(expected_ids), "Materialization manifest bank IDs differ from ledger")
    identity_rows: list[dict[str, Any]] = []
    for row in ledger_rows:
        bank_id = str(row["bank_id"])
        manifest_bank = manifest_by_id[bank_id]
        for field in required_fields:
            require(field in manifest_bank, f"Materialization manifest misses F003 field for {bank_id}: {field}")
            require(
                str(manifest_bank[field]) == str(row[field]),
                f"F003 identity mismatch for {bank_id}: {field}",
            )
        identity_rows.append({
            "bank_id": bank_id,
            "filename": row["filename"],
            "seed": int(row["seed"]),
            "condition": row["condition"],
            "row_count": int(row["row_count"]),
            "new_row_count": int(row["new_row_count"]),
            "total_dam_count": int(row["total_dam_count"]),
            "new_dam_count": int(row["new_dam_count"]),
            "size_bytes": int(row["size_bytes"]),
            "code_count": int(manifest_bank["total_bank_descriptor"]["nandina_count"]),
            "bank_csv_sha256": row["bank_csv_sha256"],
            "composition_sha256": row["composition_sha256"],
            "H100_core_id_order_sha256": row["H100_core_id_order_sha256"],
            "increment_id_order_sha256": row["increment_id_order_sha256"],
            "total_bank_id_order_sha256": row["total_bank_id_order_sha256"],
        })
    return identity_rows


def validate_inputs(root: Path, config: Mapping[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for label, entry in config["frozen_inputs"].items():
        checks.append(validate_file_contract(root, entry, label))
    for entry in config["canonical_source_files"]:
        checks.append(validate_file_contract(root, entry, str(entry["role"])))
    materialization = config["materialization_contract"]
    for label in ("manifest", "ledger", "current_materialization_config", "gate03_feasibility", "gate03_common_clean_mask", "gate03_config"):
        checks.append(validate_file_contract(root, materialization[label], f"materialization_{label}"))
    manifest = load_json(project_path(root, materialization["manifest"]["path"]))
    require(manifest.get("retrieval_executed") is False, "Materialization manifest reports retrieval")
    require(manifest.get("evaluation_metrics_computed") is False, "Materialization manifest reports metrics")
    require(manifest.get("banks_materialized") is True, "Materialization manifest does not confirm banks")
    require(manifest.get("hash_mismatches") == 0, "Materialization manifest has hash mismatches")
    notice = materialization["known_provenance_notice"]
    require(manifest.get("config", {}).get("sha256") == notice["manifest_embedded_config_sha256"], "Unexpected embedded materialization config fingerprint")
    ledger = read_csv(project_path(root, materialization["ledger"]["path"]))
    identities = validate_bank_identity_contract(config, ledger, manifest.get("banks", []))
    common_clean = validate_common_clean(root, config)
    return checks, identities, common_clean


def validate_future_output_root_absent(root: Path, config: Mapping[str, Any]) -> None:
    if config["exp11b_retrieval_authorized"] is False:
        future_root = project_path(root, config["future_output_contract"]["official_output_root"])
        require(
            not future_root.exists(),
            f"Official H150/H200 output root must be absent while retrieval is unauthorized: {future_root}",
        )


def preflight(root: Path = ROOT, config_path: Path | None = None) -> dict[str, Any]:
    config_file = config_path or root / CONFIG_RELATIVE_PATH
    config = load_json(config_file)
    validate_static_contract(config)
    validate_future_output_root_absent(root, config)
    base = validate_base_commit(root, config)
    checks, identities, common_clean = validate_inputs(root, config)
    return {
        "gate": config["gate"],
        "gate_status": config["gate_status"],
        "base_commit": base,
        "status": "PREFLIGHT_PASS_CANDIDATE_PENDING_EXTERNAL_AUDIT",
        "input_checks": checks,
        "bank_identities": identities,
        "common_clean": common_clean,
        "flags": {flag: config[flag] for flag in REQUIRED_FALSE_FLAGS},
    }


def freeze_gate(root: Path = ROOT, audit_dir: Path | None = None, config_path: Path | None = None) -> dict[str, Any]:
    config_file = config_path or root / CONFIG_RELATIVE_PATH
    config = load_json(config_file)
    report = preflight(root, config_file)
    target = audit_dir or project_path(root, config["freeze_artifacts"]["directory"])
    require(not target.exists() or not any(target.iterdir()), f"Freeze output directory is not empty: {target}")
    target.mkdir(parents=True, exist_ok=True)
    inventory_path = target / config["freeze_artifacts"]["input_inventory_filename"]
    manifest_path = target / config["freeze_artifacts"]["manifest_filename"]
    inventory = {
        "gate": config["gate"],
        "integrated_base_commit": config["integrated_base_commit"],
        "input_checks": report["input_checks"],
        "bank_identities": report["bank_identities"],
        "common_clean": report["common_clean"],
        "canonical_retrieval_semantics": config["canonical_retrieval_semantics"],
    }
    write_json(inventory_path, inventory)
    manifest = {
        "gate": config["gate"],
        "gate_status": config["gate_status"],
        "base_commit": config["integrated_base_commit"],
        "retrieval_executed": False,
        "evaluation_metrics_computed": False,
        "h150_h200_results_observed": False,
        "exp11b_retrieval_authorized": False,
        "execution_mode": config["execution_mode"],
        "config_path": str(config_file.relative_to(root).as_posix()),
        "config_sha256": sha256_file(config_file),
        "input_inventory": inventory_path.name,
        "input_inventory_sha256": sha256_file(inventory_path),
        "bank_count": len(report["bank_identities"]),
        "future_execution": config["future_execution"],
        "future_output_contract": config["future_output_contract"],
        "known_provenance_notice": config["materialization_contract"]["known_provenance_notice"],
    }
    write_json(manifest_path, manifest)
    return {"manifest": manifest_path, "input_inventory": inventory_path, "preflight": report}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate or freeze the prospective EXP-11B retrieval execution gate without retrieval.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true", help="Validate frozen contracts without writing outputs or executing retrieval.")
    mode.add_argument("--freeze", action="store_true", help="Write gate metadata only into an empty audit directory.")
    parser.add_argument("--audit-dir", help="Override the gate audit directory for --freeze.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.preflight:
        report = preflight()
        print(f"PREFLIGHT_PASS banks={len(report['bank_identities'])} retrieval_executed=false")
        return 0
    target = Path(args.audit_dir).resolve() if args.audit_dir else None
    result = freeze_gate(audit_dir=target)
    print(f"FREEZE_PASS manifest={result['manifest']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
