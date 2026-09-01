"""Materialize the frozen EXP-11B H150/H200 bank identities without retrieval."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path("src/configs/exp11b_bank_materialization_v0.1.json")
ID = "id_unico"
DAM = "DECLARACION"
NANDINA = "NANDINA"


class ContractViolation(RuntimeError):
    """Raised when a frozen EXP-11B materialization invariant does not hold."""


@dataclass(frozen=True)
class Dataset:
    path: Path
    headers: tuple[str, ...]
    rows: tuple[dict[str, str], ...]


@dataclass(frozen=True)
class MaterializationInputs:
    h100: Dataset
    new_eligible: Dataset
    dev: Dataset
    eval: Dataset
    feasibility: dict[str, Any]
    config: dict[str, Any]


@dataclass(frozen=True)
class BankPlan:
    bank_id: str
    replicate_id: str
    seed: int
    condition: str
    selected_dams: tuple[str, ...]
    selected_new_rows: tuple[dict[str, str], ...]
    projected_new_rows: tuple[dict[str, str], ...]
    feasibility_entry: dict[str, Any]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_json_list(values: Iterable[str]) -> str:
    payload = json.dumps(list(values), ensure_ascii=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def composition_sha256(dams: Iterable[str]) -> str:
    return sha256_json_list(sorted(dams))


def canonical_json(payload: Mapping[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def resolve(root: Path, configured_path: str | Path) -> Path:
    path = Path(configured_path)
    return path if path.is_absolute() else root / path


def read_json(path: Path) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        raise ContractViolation(f"Cannot read JSON contract: {path}") from error
    if not isinstance(payload, dict):
        raise ContractViolation(f"JSON contract must be an object: {path}")
    return payload


def read_dataset(path: Path) -> Dataset:
    if not path.is_file():
        raise ContractViolation(f"Required dataset is missing: {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ContractViolation(f"Dataset has no header: {path}")
        headers = tuple(reader.fieldnames)
        if len(headers) != len(set(headers)):
            raise ContractViolation(f"Dataset has duplicated header columns: {path}")
        rows: list[dict[str, str]] = []
        for number, row in enumerate(reader, start=2):
            if None in row:
                raise ContractViolation(f"Dataset has more values than header columns at {path}:{number}")
            if any(value is None for value in row.values()):
                raise ContractViolation(f"Dataset has missing value cells at {path}:{number}")
            rows.append({key: str(value) for key, value in row.items()})
    return Dataset(path=path, headers=headers, rows=tuple(rows))


def require_columns(dataset: Dataset, columns: Iterable[str], label: str) -> None:
    missing = [column for column in columns if column not in dataset.headers]
    if missing:
        raise ContractViolation(f"{label} lacks required columns: {', '.join(missing)}")


def require_unique_nonempty_ids(rows: Iterable[Mapping[str, str]], label: str) -> tuple[str, ...]:
    ids = tuple(row.get(ID, "").strip() for row in rows)
    if not ids or any(not value for value in ids):
        raise ContractViolation(f"{label} has an empty {ID}")
    if len(ids) != len(set(ids)):
        raise ContractViolation(f"{label} has duplicate {ID} values")
    return ids


def dam_set(rows: Iterable[Mapping[str, str]], label: str) -> set[str]:
    dams = {row.get(DAM, "").strip() for row in rows}
    if not dams or "" in dams:
        raise ContractViolation(f"{label} has an empty {DAM}")
    return dams


def validate_file_contract(path: Path, expected_sha256: str, expected_rows: int | None, label: str) -> Dataset:
    if not path.is_file():
        raise ContractViolation(f"{label} is missing: {path}")
    actual_sha256 = sha256_file(path)
    if actual_sha256 != expected_sha256:
        raise ContractViolation(f"{label} SHA-256 mismatch: {actual_sha256}")
    dataset = read_dataset(path)
    if expected_rows is not None and len(dataset.rows) != expected_rows:
        raise ContractViolation(f"{label} row count mismatch: {len(dataset.rows)}")
    return dataset


def validate_config(config: Mapping[str, Any]) -> None:
    expected = {
        "contract_status": "EXP11B_BANK_MATERIALIZATION_ONLY",
        "bank_materialization_authorized": True,
        "retrieval_authorized": False,
        "retrieval_executed": False,
        "evaluation_metrics_allowed": False,
        "evaluation_metrics_computed": False,
        "banks_expected": 20,
    }
    for field, value in expected.items():
        if config.get(field) != value:
            raise ContractViolation(f"Materialization config field mismatch: {field}")
    if config.get("conditions") != ["H150", "H200"]:
        raise ContractViolation("Materialization conditions must be exactly H150 and H200")


def load_inputs(root: Path, config_path: Path | None = None) -> MaterializationInputs:
    config_file = resolve(root, config_path or CONFIG_PATH)
    config = read_json(config_file)
    validate_config(config)
    required = tuple(config["required_scientific_columns"])
    h100_spec = config["inputs"]["H100"]
    new_spec = config["inputs"]["NEW_ELIGIBLE"]
    h100 = validate_file_contract(resolve(root, h100_spec["path"]), h100_spec["sha256"], h100_spec["rows"], "H100")
    new_eligible = validate_file_contract(
        resolve(root, new_spec["path"]), new_spec["sha256"], new_spec["rows"], "NEW_ELIGIBLE"
    )
    feasibility_spec = config["feasibility"]
    feasibility_path = resolve(root, feasibility_spec["path"])
    if sha256_file(feasibility_path) != feasibility_spec["sha256"]:
        raise ContractViolation("Gate 03 feasibility SHA-256 mismatch")
    feasibility = read_json(feasibility_path)
    if feasibility.get("execution_authorized") is not False:
        raise ContractViolation("Gate 03 feasibility must remain execution_authorized=false")
    if feasibility.get("retrieval_executed") is not False:
        raise ContractViolation("Gate 03 feasibility must remain retrieval_executed=false")
    require_columns(h100, required, "H100")
    require_columns(new_eligible, required, "NEW_ELIGIBLE")
    require_unique_nonempty_ids(h100.rows, "H100")
    require_unique_nonempty_ids(new_eligible.rows, "NEW_ELIGIBLE")
    if set(require_unique_nonempty_ids(h100.rows, "H100")) & set(require_unique_nonempty_ids(new_eligible.rows, "NEW_ELIGIBLE")):
        raise ContractViolation("H100 and NEW_ELIGIBLE share id_unico values")
    h100_dams = dam_set(h100.rows, "H100")
    new_dams = dam_set(new_eligible.rows, "NEW_ELIGIBLE")
    if len(h100_dams) != h100_spec["dams"] or len(new_dams) != new_spec["dams"]:
        raise ContractViolation("Frozen DAM count mismatch")
    if h100_dams & new_dams:
        raise ContractViolation("H100 and NEW_ELIGIBLE DAM overlap")
    h100_codes = {row[NANDINA].strip() for row in h100.rows if row[NANDINA].strip()}
    if len(h100_codes) != h100_spec["nandina"]:
        raise ContractViolation("H100 NANDINA count mismatch")
    dev = read_dataset(resolve(root, config["inputs"]["DEV"]["path"]))
    evalset = read_dataset(resolve(root, config["inputs"]["EVAL"]["path"]))
    require_columns(dev, (DAM,), "DEV")
    require_columns(evalset, (DAM,), "EVAL")
    return MaterializationInputs(h100, new_eligible, dev, evalset, feasibility, config)


def project_new_row(row: Mapping[str, str], h100_headers: Iterable[str]) -> dict[str, str]:
    return {header: row.get(header, "") for header in h100_headers}


def rows_for_dams(rows: Iterable[dict[str, str]], dams: Iterable[str]) -> tuple[dict[str, str], ...]:
    selected = set(dams)
    return tuple(row for row in rows if row[DAM].strip() in selected)


def distribution_descriptor(rows: Iterable[Mapping[str, str]]) -> dict[str, Any]:
    rows = tuple(rows)
    counts: Counter[str] = Counter(row[DAM].strip() for row in rows)
    total = len(rows)
    hhi = sum((count / total) ** 2 for count in counts.values()) if total else 0.0
    largest = max(counts.values(), default=0)
    return {
        "rows": total,
        "dam_count": len(counts),
        "dam_hhi": hhi,
        "effective_dam_count": (1 / hhi) if hhi else 0.0,
        "largest_dam_rows": largest,
        "largest_dam_share": (largest / total) if total else 0.0,
    }


def increment_descriptor(rows: Iterable[Mapping[str, str]], h100_nandina: set[str]) -> dict[str, Any]:
    rows = tuple(rows)
    codes = {row[NANDINA].strip() for row in rows if row[NANDINA].strip()}
    return {
        **distribution_descriptor(rows),
        "nandina_count": len(codes),
        "nandina_shared_with_h100_count": len(codes & h100_nandina),
        "nandina_new_vs_h100_count": len(codes - h100_nandina),
    }


def total_bank_descriptor(
    h100_rows: Iterable[Mapping[str, str]], increment_rows: Iterable[Mapping[str, str]], h100_nandina: set[str]
) -> dict[str, Any]:
    rows = (*h100_rows, *increment_rows)
    codes = {row[NANDINA].strip() for row in rows if row[NANDINA].strip()}
    if len(h100_nandina) != 66:
        raise ContractViolation("H100 NANDINA coverage denominator must remain 66")
    return {
        **distribution_descriptor(rows),
        "nandina_count": len(codes),
        "H100_nandina_coverage_n": len(codes & h100_nandina),
        "H100_nandina_coverage_denominator": 66,
        "H100_nandina_coverage_pct": len(codes & h100_nandina) / 66 * 100,
        "new_nandina_count": len(codes - h100_nandina),
    }


def assert_descriptor_matches(actual: Mapping[str, Any], expected: Mapping[str, Any], label: str) -> None:
    if set(actual) != set(expected):
        raise ContractViolation(f"{label} descriptor fields mismatch")
    for key, value in expected.items():
        actual_value = actual[key]
        if isinstance(value, float):
            if abs(float(actual_value) - value) > 1e-12:
                raise ContractViolation(f"{label} descriptor mismatch: {key}")
        elif actual_value != value:
            raise ContractViolation(f"{label} descriptor mismatch: {key}")


def validate_replicates(inputs: MaterializationInputs) -> tuple[BankPlan, ...]:
    config = inputs.config
    feasibility = inputs.feasibility
    required_seeds = config["feasibility"]["accepted_seed_schedule"]
    replicates = feasibility.get("accepted_replicates")
    if not isinstance(replicates, list) or len(replicates) != config["feasibility"]["accepted_replicates"]:
        raise ContractViolation("Gate 03 must contain exactly ten accepted replicates")
    if feasibility.get("accepted_seed_schedule") != required_seeds:
        raise ContractViolation("Gate 03 accepted seed schedule mismatch")
    if [item.get("seed") for item in replicates] != required_seeds:
        raise ContractViolation("Accepted replicate seed values mismatch")
    if [item.get("replicate_id") for item in replicates] != [f"R{index:02d}" for index in range(1, 11)]:
        raise ContractViolation("Accepted replicate identifiers mismatch")

    h100_dams = dam_set(inputs.h100.rows, "H100")
    dev_dams = dam_set(inputs.dev.rows, "DEV")
    eval_dams = dam_set(inputs.eval.rows, "EVAL")
    h100_codes = {row[NANDINA].strip() for row in inputs.h100.rows if row[NANDINA].strip()}
    h100_ids = set(require_unique_nonempty_ids(inputs.h100.rows, "H100"))
    plans: list[BankPlan] = []
    by_replicate: dict[str, dict[str, BankPlan]] = {}

    for replicate in replicates:
        replicate_id = replicate["replicate_id"]
        plans_for_replicate: dict[str, BankPlan] = {}
        for condition in config["conditions"]:
            frozen = replicate.get(condition)
            if not isinstance(frozen, dict):
                raise ContractViolation(f"{replicate_id} lacks {condition} data")
            dams = frozen.get("dams")
            if not isinstance(dams, list) or not dams or len(dams) != len(set(dams)):
                raise ContractViolation(f"{replicate_id}-{condition} has invalid frozen DAM list")
            selected_dams = tuple(str(dam).strip() for dam in dams)
            if any(not dam for dam in selected_dams):
                raise ContractViolation(f"{replicate_id}-{condition} has an empty frozen DAM")
            if composition_sha256(selected_dams) != frozen.get("composition_sha256"):
                raise ContractViolation(f"{replicate_id}-{condition} composition SHA mismatch")
            selected_rows = rows_for_dams(inputs.new_eligible.rows, selected_dams)
            selected_dam_set = dam_set(selected_rows, f"{replicate_id}-{condition} increment")
            if selected_dam_set != set(selected_dams):
                raise ContractViolation(f"{replicate_id}-{condition} has missing or extra selected DAMs")
            if len(selected_rows) != frozen.get("realized_new_rows"):
                raise ContractViolation(f"{replicate_id}-{condition} realized new row count mismatch")
            projected_rows = tuple(project_new_row(row, inputs.h100.headers) for row in selected_rows)
            increment_ids = require_unique_nonempty_ids(projected_rows, f"{replicate_id}-{condition} increment")
            if h100_ids & set(increment_ids):
                raise ContractViolation(f"{replicate_id}-{condition} overlaps H100 ids")
            bank_rows = (*inputs.h100.rows, *projected_rows)
            if len(bank_rows) != frozen.get("realized_total_rows"):
                raise ContractViolation(f"{replicate_id}-{condition} realized total row count mismatch")
            require_unique_nonempty_ids(bank_rows, f"{replicate_id}-{condition} total bank")
            total_dams = dam_set(bank_rows, f"{replicate_id}-{condition} total bank")
            if not h100_dams <= total_dams:
                raise ContractViolation(f"{replicate_id}-{condition} is missing an H100 DAM")
            if total_dams & dev_dams or total_dams & eval_dams:
                raise ContractViolation(f"{replicate_id}-{condition} overlaps DEV or EVAL DAMs")
            assert_descriptor_matches(
                increment_descriptor(projected_rows, h100_codes),
                frozen["increment_descriptor"],
                f"{replicate_id}-{condition} increment",
            )
            assert_descriptor_matches(
                total_bank_descriptor(inputs.h100.rows, projected_rows, h100_codes),
                frozen["total_bank_descriptor"],
                f"{replicate_id}-{condition} total",
            )
            plan = BankPlan(
                bank_id=f"EXP11B_{replicate_id}_{condition}",
                replicate_id=replicate_id,
                seed=int(replicate["seed"]),
                condition=condition,
                selected_dams=selected_dams,
                selected_new_rows=selected_rows,
                projected_new_rows=projected_rows,
                feasibility_entry=frozen,
            )
            plans.append(plan)
            plans_for_replicate[condition] = plan
        h150 = plans_for_replicate["H150"]
        h200 = plans_for_replicate["H200"]
        if not set(h150.selected_dams) < set(h200.selected_dams):
            raise ContractViolation(f"{replicate_id} DAM nesting is not strict")
        h150_ids = h100_ids | set(require_unique_nonempty_ids(h150.projected_new_rows, f"{replicate_id}-H150"))
        h200_ids = h100_ids | set(require_unique_nonempty_ids(h200.projected_new_rows, f"{replicate_id}-H200"))
        if not h150_ids < h200_ids:
            raise ContractViolation(f"{replicate_id} total id_unico nesting is not strict")
        by_replicate[replicate_id] = plans_for_replicate
    if len(plans) != config["banks_expected"]:
        raise ContractViolation("Materialization plan must contain exactly twenty banks")
    return tuple(plans)


def preflight(root: Path = ROOT, config_path: Path | None = None) -> tuple[MaterializationInputs, tuple[BankPlan, ...]]:
    inputs = load_inputs(root, config_path)
    return inputs, validate_replicates(inputs)


def serialize_csv(headers: Iterable[str], rows: Iterable[Mapping[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=list(headers),
        extrasaction="raise",
        lineterminator="\n",
        quoting=csv.QUOTE_MINIMAL,
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def assert_empty_target(path: Path, label: str) -> None:
    if path.exists() and (not path.is_dir() or any(path.iterdir())):
        raise ContractViolation(f"{label} already contains output; refusing to overwrite: {path}")


def bank_filename(plan: BankPlan) -> str:
    return f"{plan.bank_id}.csv"


def audit_bank(plan: BankPlan, inputs: MaterializationInputs, path: Path) -> dict[str, Any]:
    output = read_dataset(path)
    if output.headers != inputs.h100.headers:
        raise ContractViolation(f"{plan.bank_id} header does not match H100 exactly")
    h100_count = len(inputs.h100.rows)
    if output.rows[:h100_count] != inputs.h100.rows:
        raise ContractViolation(f"{plan.bank_id} H100 core rows or order changed")
    if output.rows[h100_count:] != plan.projected_new_rows:
        raise ContractViolation(f"{plan.bank_id} increment rows or order changed")
    increment = output.rows[h100_count:]
    selected_dams = dam_set(increment, f"{plan.bank_id} increment")
    if selected_dams != set(plan.selected_dams):
        raise ContractViolation(f"{plan.bank_id} materialized selected DAMs differ from Gate 03")
    if len(increment) != plan.feasibility_entry["realized_new_rows"]:
        raise ContractViolation(f"{plan.bank_id} materialized new row count mismatch")
    if len(output.rows) != plan.feasibility_entry["realized_total_rows"]:
        raise ContractViolation(f"{plan.bank_id} materialized total row count mismatch")
    require_unique_nonempty_ids(increment, f"{plan.bank_id} increment")
    total_ids = require_unique_nonempty_ids(output.rows, f"{plan.bank_id} total")
    h100_codes = {row[NANDINA].strip() for row in inputs.h100.rows if row[NANDINA].strip()}
    assert_descriptor_matches(
        increment_descriptor(increment, h100_codes), plan.feasibility_entry["increment_descriptor"], f"{plan.bank_id} output increment"
    )
    total_descriptor = total_bank_descriptor(inputs.h100.rows, increment, h100_codes)
    assert_descriptor_matches(total_descriptor, plan.feasibility_entry["total_bank_descriptor"], f"{plan.bank_id} output total")
    return {
        "bank_id": plan.bank_id,
        "filename": path.name,
        "seed": plan.seed,
        "condition": plan.condition,
        "selected_dams": list(plan.selected_dams),
        "composition_sha256": plan.feasibility_entry["composition_sha256"],
        "size_bytes": path.stat().st_size,
        "bank_csv_sha256": sha256_file(path),
        "row_count": len(output.rows),
        "new_row_count": len(increment),
        "total_dam_count": len(dam_set(output.rows, plan.bank_id)),
        "new_dam_count": len(selected_dams),
        "H100_CORE_ROWS_MATCH": True,
        "H100_CORE_ORDER_MATCH": True,
        "H100_core_id_order_sha256": sha256_json_list(row[ID] for row in inputs.h100.rows),
        "increment_id_order_sha256": sha256_json_list(row[ID] for row in increment),
        "total_bank_id_order_sha256": sha256_json_list(total_ids),
        "increment_descriptor": increment_descriptor(increment, h100_codes),
        "total_bank_descriptor": total_descriptor,
        "selection_match": True,
        "descriptor_match": True,
    }


def assert_nesting_from_entries(entries: Iterable[Mapping[str, Any]]) -> None:
    by_replicate: dict[str, dict[str, Mapping[str, Any]]] = {}
    for entry in entries:
        replicate = entry["bank_id"].split("_")[1]
        by_replicate.setdefault(replicate, {})[entry["condition"]] = entry
    if sorted(by_replicate) != [f"R{index:02d}" for index in range(1, 11)]:
        raise ContractViolation("Materialized banks lack a complete replicate set")
    for replicate, conditions in by_replicate.items():
        h150 = conditions.get("H150")
        h200 = conditions.get("H200")
        if h150 is None or h200 is None:
            raise ContractViolation(f"Materialized {replicate} lacks H150 or H200")
        if not set(h150["selected_dams"]) < set(h200["selected_dams"]):
            raise ContractViolation(f"Materialized {replicate} DAM nesting mismatch")


def manifest_payload(
    root: Path,
    inputs: MaterializationInputs,
    entries: list[dict[str, Any]],
    started_utc: str,
    finished_utc: str,
    config_path: Path,
) -> dict[str, Any]:
    assert_nesting_from_entries(entries)
    return {
        "experiment_id": inputs.config["experiment_id"],
        "version": inputs.config["version"],
        "status": "CANDIDATE_FROZEN",
        "materialization_start_utc": started_utc,
        "materialization_finish_utc": finished_utc,
        "banks_materialized": True,
        "banks_versioned_in_git": False,
        "banks_regenerable_from_versioned_inputs": True,
        "retrieval_executed": False,
        "evaluation_metrics_computed": False,
        "bank_row_order_policy": inputs.config["bank_row_order_policy"],
        "serialization": inputs.config["serialization"],
        "config": {
            "path": str(config_path.relative_to(root)).replace("\\", "/"),
            "sha256": sha256_file(config_path),
        },
        "inputs": {
            "H100": {**inputs.config["inputs"]["H100"], "observed_sha256": sha256_file(inputs.h100.path)},
            "NEW_ELIGIBLE": {
                **inputs.config["inputs"]["NEW_ELIGIBLE"],
                "observed_sha256": sha256_file(inputs.new_eligible.path),
            },
            "feasibility": {
                **inputs.config["feasibility"],
                "observed_sha256": sha256_file(resolve(root, inputs.config["feasibility"]["path"])),
            },
        },
        "bank_count": len(entries),
        "H150_bank_count": sum(entry["condition"] == "H150" for entry in entries),
        "H200_bank_count": sum(entry["condition"] == "H200" for entry in entries),
        "hash_mismatches": 0,
        "h100_core_match_all": True,
        "selection_match_all": True,
        "descriptor_match_all": True,
        "nesting_match_all": True,
        "banks": entries,
    }


def write_audits(audit_dir: Path, config: Mapping[str, Any], manifest: Mapping[str, Any]) -> tuple[Path, Path]:
    audit_dir.mkdir(parents=True, exist_ok=False)
    output = config["output_contract"]
    manifest_path = audit_dir / output["manifest_filename"]
    hashes_path = audit_dir / output["hashes_filename"]
    manifest_path.write_text(canonical_json(manifest), encoding="utf-8", newline="\n")
    fields = [
        "bank_id", "filename", "seed", "condition", "row_count", "new_row_count", "total_dam_count", "new_dam_count",
        "bank_csv_sha256", "size_bytes", "composition_sha256", "H100_core_id_order_sha256",
        "increment_id_order_sha256", "total_bank_id_order_sha256",
    ]
    hashes_path.write_bytes(serialize_csv(fields, ({field: entry[field] for field in fields} for entry in manifest["banks"])))
    return manifest_path, hashes_path


def compare_manifest_identities(actual: Mapping[str, Any], expected: Mapping[str, Any]) -> None:
    fields = (
        "bank_id", "filename", "seed", "condition", "selected_dams", "composition_sha256", "size_bytes",
        "bank_csv_sha256", "row_count", "new_row_count", "total_dam_count", "new_dam_count",
        "H100_CORE_ROWS_MATCH", "H100_CORE_ORDER_MATCH", "H100_core_id_order_sha256",
        "increment_id_order_sha256", "total_bank_id_order_sha256", "increment_descriptor", "total_bank_descriptor",
        "selection_match", "descriptor_match",
    )
    actual_banks = actual.get("banks")
    expected_banks = expected.get("banks")
    if not isinstance(actual_banks, list) or not isinstance(expected_banks, list) or len(actual_banks) != 20 or len(expected_banks) != 20:
        raise ContractViolation("Manifest must contain exactly twenty banks")
    actual_by_id = {entry["bank_id"]: entry for entry in actual_banks}
    expected_by_id = {entry["bank_id"]: entry for entry in expected_banks}
    if set(actual_by_id) != set(expected_by_id):
        raise ContractViolation("Materialized bank identities differ from frozen manifest")
    for bank_id in sorted(actual_by_id):
        for field in fields:
            if actual_by_id[bank_id].get(field) != expected_by_id[bank_id].get(field):
                raise ContractViolation(f"Frozen manifest mismatch for {bank_id}: {field}")


def materialize(
    root: Path = ROOT,
    config_path: Path | None = None,
    output_dir: Path | None = None,
    audit_dir: Path | None = None,
    expected_manifest: Path | None = None,
) -> dict[str, Any]:
    inputs, plans = preflight(root, config_path)
    config_file = resolve(root, config_path or CONFIG_PATH)
    output_contract = inputs.config["output_contract"]
    target_bank_dir = resolve(root, output_dir or output_contract["bank_dir"])
    target_audit_dir = resolve(root, audit_dir or output_contract["audit_dir"])
    assert_empty_target(target_bank_dir, "Bank output directory")
    assert_empty_target(target_audit_dir, "Audit output directory")
    started_utc = utc_now()
    target_bank_dir.mkdir(parents=True, exist_ok=False)
    entries: list[dict[str, Any]] = []
    for plan in plans:
        path = target_bank_dir / bank_filename(plan)
        path.write_bytes(serialize_csv(inputs.h100.headers, (*inputs.h100.rows, *plan.projected_new_rows)))
        entries.append(audit_bank(plan, inputs, path))
    assert_nesting_from_entries(entries)
    finished_utc = utc_now()
    manifest = manifest_payload(root, inputs, entries, started_utc, finished_utc, config_file)
    manifest_path, hashes_path = write_audits(target_audit_dir, inputs.config, manifest)
    if expected_manifest is not None:
        compare_manifest_identities(manifest, read_json(expected_manifest))
    return {
        "manifest": manifest,
        "manifest_path": manifest_path,
        "hashes_path": hashes_path,
        "bank_dir": target_bank_dir,
        "audit_dir": target_audit_dir,
    }


def verify(
    root: Path = ROOT,
    config_path: Path | None = None,
    output_dir: Path | None = None,
    audit_dir: Path | None = None,
    expected_manifest: Path | None = None,
) -> dict[str, Any]:
    inputs, plans = preflight(root, config_path)
    output_contract = inputs.config["output_contract"]
    target_bank_dir = resolve(root, output_dir or output_contract["bank_dir"])
    target_audit_dir = resolve(root, audit_dir or output_contract["audit_dir"])
    if not target_bank_dir.is_dir() or not target_audit_dir.is_dir():
        raise ContractViolation("Bank and audit output directories must exist for verification")
    manifest_path = target_audit_dir / output_contract["manifest_filename"]
    hashes_path = target_audit_dir / output_contract["hashes_filename"]
    manifest = read_json(manifest_path)
    entries = [audit_bank(plan, inputs, target_bank_dir / bank_filename(plan)) for plan in plans]
    reconstructed = manifest_payload(
        root, inputs, entries, manifest["materialization_start_utc"], manifest["materialization_finish_utc"], resolve(root, config_path or CONFIG_PATH)
    )
    compare_manifest_identities(reconstructed, manifest)
    with hashes_path.open(encoding="utf-8", newline="") as handle:
        hash_rows = list(csv.DictReader(handle))
    if len(hash_rows) != 20 or {row["bank_id"] for row in hash_rows} != {entry["bank_id"] for entry in entries}:
        raise ContractViolation("Hash audit must contain exactly one row for every bank")
    if expected_manifest is not None:
        compare_manifest_identities(reconstructed, read_json(expected_manifest))
    return reconstructed


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--preflight", action="store_true")
    modes.add_argument("--materialize", action="store_true")
    modes.add_argument("--verify", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--audit-dir", type=Path)
    parser.add_argument("--expected-manifest", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.preflight:
            _, plans = preflight()
            print(f"PREFLIGHT_PASS banks={len(plans)} retrieval_executed=false")
        elif args.materialize:
            result = materialize(output_dir=args.output_dir, audit_dir=args.audit_dir, expected_manifest=args.expected_manifest)
            print(f"MATERIALIZATION_PASS banks={result['manifest']['bank_count']} manifest={result['manifest_path']}")
        else:
            manifest = verify(output_dir=args.output_dir, audit_dir=args.audit_dir, expected_manifest=args.expected_manifest)
            print(f"VERIFY_PASS banks={manifest['bank_count']} hash_mismatches={manifest['hash_mismatches']}")
        return 0
    except ContractViolation as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
