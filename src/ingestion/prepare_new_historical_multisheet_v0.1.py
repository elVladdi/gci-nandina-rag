"""Fail-closed source freeze and prospective multisheet contract for Gate 02.

This module freezes the current reproducing source and defines the future
ingestion path before any new data is observed. The future path calls the
established SUNAT parser with explicit sheet names and never selects a new sheet
by workbook position.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import openpyxl
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.ingestion import sunat_series_parser
from src.evaluation import build_data_aduanas_splits
from src.evaluation import group_split_by_dam


DEFAULT_CONTRACT_PATH = ROOT / "src" / "configs" / "new_historical_multisheet_contract_v0.1.json"
DEFAULT_MANIFEST_PATH = ROOT / "outputs" / "audits" / "new_historical_gate_v0.1" / "source_freeze_manifest_v0.1.json"
DEFAULT_INTERIM_OUTPUT_DIR = ROOT / "data" / "interim" / "new_historical_gate_v0.1"
DEFAULT_FUTURE_AUDIT_DIR = ROOT / "outputs" / "audits" / "new_historical_gate_v0.1"
DEFAULT_ARCHIVE_PATH = (
    ROOT.parent
    / "LLM_RGA_NANDINA_source_archive"
    / "Series - Descripciones_CURRENT_H100_REPRODUCING_SOURCE_db01d1fc.xlsx"
)


class ContractViolation(RuntimeError):
    """Raised whenever a frozen source or contract predicate is not true."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_contract(path: Path = DEFAULT_CONTRACT_PATH) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def resolve_repo_path(value: str | Path) -> Path:
    candidate = Path(value)
    return candidate if candidate.is_absolute() else ROOT / candidate


def inspect_workbook(path: Path) -> list[str]:
    try:
        workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    except Exception as exc:  # pragma: no cover - library exception detail varies
        raise ContractViolation(f"No se pudo inspeccionar workbook: {path}: {exc}") from exc
    try:
        return list(workbook.sheetnames)
    finally:
        workbook.close()


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ContractViolation(f"{label} invalido: esperado={expected!r} actual={actual!r}")


def validate_current_source(source_path: Path, contract: dict[str, Any]) -> dict[str, Any]:
    source = contract["current_source"]
    if not source_path.is_file():
        raise ContractViolation(f"Fuente actual no encontrada: {source_path}")
    source_sha = sha256_file(source_path)
    source_size = source_path.stat().st_size
    sheet_names = inspect_workbook(source_path)
    require_equal(source_sha, source["sha256"], "SHA-256 de fuente")
    require_equal(source_size, source["size_bytes"], "Tamano de fuente")
    require_equal(sheet_names, source["sheet_order"], "Orden de hojas de fuente")
    allowed_new_sheets = {sheet for sheet_set in valid_new_sheet_sets(contract) for sheet in sheet_set}
    return {
        "path": str(source_path),
        "sha256": source_sha,
        "size_bytes": source_size,
        "sheet_order": sheet_names,
        "new_data_sheets_present": any(name in sheet_names for name in allowed_new_sheets),
    }


def validate_frozen_datasets(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    observed: dict[str, dict[str, Any]] = {}
    for label, descriptor in contract["frozen_datasets"].items():
        dataset_path = resolve_repo_path(descriptor["path"])
        if not dataset_path.is_file():
            raise ContractViolation(f"Dataset congelado no encontrado: {label}: {dataset_path}")
        actual_sha = sha256_file(dataset_path)
        require_equal(actual_sha, descriptor["sha256"], f"SHA-256 {label}")
        observed[label] = {
            "path": descriptor["path"],
            "sha256": actual_sha,
            "size_bytes": dataset_path.stat().st_size,
        }
    return observed


def valid_new_sheet_sets(contract: dict[str, Any]) -> list[list[str]]:
    configured = contract.get("new_sheet_sets", {})
    valid_sets = list(configured.values())
    expected = [["NUEVA_01"], ["NUEVA_01", "NUEVA_02"]]
    require_equal(valid_sets, expected, "Conjuntos prospectivos de hojas nuevas")
    return valid_sets


def validate_new_sheet_names(requested_sheets: Iterable[str], contract: dict[str, Any]) -> list[str]:
    """Allow only the two frozen ordered sets for a real future ingestion."""

    requested = list(requested_sheets)
    if requested not in valid_new_sheet_sets(contract):
        raise ContractViolation(
            "Conjunto u orden de hojas nuevas no autorizado; solo se permite "
            "['NUEVA_01'] o ['NUEVA_01', 'NUEVA_02']"
        )
    return requested


def validate_future_workbook_sheet_order(
    workbook_path: Path, requested_sheets: Iterable[str], contract: dict[str, Any]
) -> list[str]:
    requested = validate_new_sheet_names(requested_sheets, contract)
    sheet_names = inspect_workbook(workbook_path)
    expected = [*contract["preexisting_source_sheets"], *requested]
    require_equal(sheet_names, expected, "Orden exacto de hojas del workbook ampliado")
    return requested


def parse_future_new_sheet(workbook_path: Path, sheet_name: str, contract: dict[str, Any]):
    """Delegate future parsing to the historical parser with an explicit sheet."""

    validate_future_workbook_sheet_order(workbook_path, [sheet_name], contract)
    return sunat_series_parser.parse_workbook(workbook_path, sheet_name=sheet_name)


def parse_future_new_sheets(
    workbook_path: Path, requested_sheets: Iterable[str], contract: dict[str, Any]
) -> list[tuple[str, Any]]:
    requested = validate_future_workbook_sheet_order(workbook_path, requested_sheets, contract)
    return [
        (sheet_name, sunat_series_parser.parse_workbook(workbook_path, sheet_name=sheet_name))
        for sheet_name in requested
    ]


def validate_future_output_dir(output_dir: Path) -> Path:
    """Keep prospective normalized/audit outputs separate from frozen CSVs."""

    resolved = output_dir.resolve()
    frozen_data_dir = (ROOT / "data" / "processed").resolve()
    if resolved == frozen_data_dir or frozen_data_dir in resolved.parents:
        raise ContractViolation("Las salidas prospectivas no pueden escribirse en data/processed congelado")
    return resolved


def frozen_dev_eval_dams(contract: dict[str, Any]) -> set[str]:
    dams: set[str] = set()
    for label in ("DEV", "EVAL"):
        dataset_path = resolve_repo_path(contract["frozen_datasets"][label]["path"])
        with dataset_path.open(encoding="utf-8-sig", newline="") as handle:
            dams.update(row.get("DECLARACION", "").strip() for row in csv.DictReader(handle))
    return {dam for dam in dams if dam}


def frozen_ids(contract: dict[str, Any]) -> set[str]:
    identifiers: set[str] = set()
    for descriptor in contract["frozen_datasets"].values():
        dataset_path = resolve_repo_path(descriptor["path"])
        with dataset_path.open(encoding="utf-8-sig", newline="") as handle:
            identifiers.update(row.get("id_unico", "").strip() for row in csv.DictReader(handle))
    return {identifier for identifier in identifiers if identifier}


def audit_future_rows(rows: Iterable[dict[str, str]], contract: dict[str, Any]) -> dict[str, list[dict[str, str]]]:
    """Record DEV/EVAL DAM and frozen-id causes independently for every row."""

    protected_dams = frozen_dev_eval_dams(contract)
    protected_ids = frozen_ids(contract)
    accepted: list[dict[str, str]] = []
    excluded_dev_eval_dam: list[dict[str, str]] = []
    existing_id_overlap: list[dict[str, str]] = []
    audited_rows: list[dict[str, str]] = []
    for row in rows:
        protected_dam = row.get("DECLARACION", "").strip() in protected_dams
        existing_id = row.get("id_unico", "").strip() in protected_ids
        reasons = []
        if protected_dam:
            reasons.append("EXCLUDED_FIXED_DEV_EVAL_DAM")
        if existing_id:
            reasons.append("EXISTING_FROZEN_ID_UNICO_OVERLAP")
        tagged = dict(row)
        tagged["protected_dev_eval_dam"] = str(protected_dam).lower()
        tagged["existing_frozen_id_overlap"] = str(existing_id).lower()
        tagged["eligible"] = str(not reasons).lower()
        tagged["exclusion_reasons"] = "|".join(reasons)
        audited_rows.append(tagged)
        if protected_dam:
            excluded_dev_eval_dam.append(tagged)
        if existing_id:
            existing_id_overlap.append(tagged)
        if not reasons:
            accepted.append(tagged)
    return {
        "accepted_for_later_curation": accepted,
        "EXCLUDED_FIXED_DEV_EVAL_DAM": excluded_dev_eval_dam,
        "EXISTING_FROZEN_ID_UNICO_OVERLAP": existing_id_overlap,
        "audited_rows": audited_rows,
    }


def stable_columns(rows: Iterable[dict[str, Any]], initial: Iterable[str] = ()) -> list[str]:
    columns = list(initial)
    for row in rows:
        for column in row:
            if column not in columns:
                columns.append(column)
    return columns


def write_csv_rows(path: Path, rows: list[dict[str, Any]], initial_columns: Iterable[str], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise ContractViolation(f"Output prospectivo ya existe: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = stable_columns(rows, initial_columns)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json_output(path: Path, payload: dict[str, Any], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise ContractViolation(f"Output prospectivo ya existe: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def execution_commit() -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else "UNKNOWN"


def capacity_descriptor(eligible_rows: int, contract: dict[str, Any]) -> dict[str, Any]:
    capacity = contract["capacity"]
    h150_min = capacity["minimum_net_new_eligible_rows_for_H150"]
    h200_min = capacity["minimum_net_new_eligible_rows_for_H200"]
    return {
        "H100_rows": capacity["H100_rows"],
        "H150_target": capacity["H150_target"],
        "H200_target": capacity["H200_target"],
        "minimum_net_new_eligible_rows_for_H150": h150_min,
        "minimum_net_new_eligible_rows_for_H200": h200_min,
        "H150_FEASIBLE": eligible_rows >= h150_min,
        "H200_FEASIBLE": eligible_rows >= h200_min,
    }


def parser_rows_and_columns(parsed_sheets: Iterable[tuple[str, Any]]) -> tuple[list[str], list[dict[str, str]], dict[str, int]]:
    columns: list[str] = []
    combined_rows: list[dict[str, str]] = []
    rows_by_sheet: dict[str, int] = {}
    for sheet_name, result in parsed_sheets:
        result_columns = list(result.columns)
        for column in result_columns:
            if column not in columns:
                columns.append(column)
        rows = [dict(row) for row in result.rows]
        for row in rows:
            for column in row:
                if column not in columns:
                    columns.append(column)
        combined_rows.extend(rows)
        rows_by_sheet[sheet_name] = len(rows)
    return columns, combined_rows, rows_by_sheet


def dataframe_for_duplicate_audit(rows: list[dict[str, str]]) -> pd.DataFrame:
    records = []
    for index, row in enumerate(rows, start=1):
        records.append(
            {
                group_split_by_dam.CASE_ID: f"NEW-HIST-V01-{index:07d}",
                group_split_by_dam.ID_UNICO: row.get("id_unico", ""),
                group_split_by_dam.DAM: row.get("DECLARACION", ""),
                group_split_by_dam.CODE: row.get("NANDINA", ""),
                group_split_by_dam.DESC: row.get("DESCRIPCION DE MERCANCIAS CONCATENADA", ""),
            }
        )
    return pd.DataFrame(
        records,
        columns=[
            group_split_by_dam.CASE_ID,
            group_split_by_dam.ID_UNICO,
            group_split_by_dam.DAM,
            group_split_by_dam.CODE,
            group_split_by_dam.DESC,
        ],
    )


def duplicate_nearduplicate_audit(rows: list[dict[str, str]], contract: dict[str, Any]) -> list[dict[str, Any]]:
    """Reuse the frozen exact/near description audit without excluding rows."""

    new_rows = dataframe_for_duplicate_audit(rows)
    audit_rows: list[dict[str, Any]] = []
    for label, descriptor in contract["frozen_datasets"].items():
        frozen = pd.read_csv(
            resolve_repo_path(descriptor["path"]),
            dtype=str,
            keep_default_na=False,
            encoding="utf-8-sig",
        )
        comparison = f"{label}_TO_NEW_ELIGIBLE"
        exact_summary, exact_details = group_split_by_dam.exact_duplicate_audit(frozen, new_rows, comparison)
        near_summary, near_details = group_split_by_dam.near_duplicate_audit(frozen, new_rows, comparison)
        audit_rows.append({"record_type": "exact_summary", **exact_summary})
        audit_rows.extend({"record_type": "exact_detail", **row} for row in exact_details)
        audit_rows.extend({"record_type": "near_summary", **row} for row in near_summary)
        audit_rows.extend({"record_type": "near_detail", **row} for row in near_details)
    return audit_rows


def prospective_output_paths(interim_dir: Path, audit_dir: Path) -> dict[str, Path]:
    interim = validate_future_output_dir(interim_dir)
    audit = validate_future_output_dir(audit_dir)
    return {
        "normalized_all": interim / "new_historical_normalized_all.csv",
        "curated": interim / "new_historical_curated.csv",
        "eligible": interim / "new_historical_eligible.csv",
        "exclusions": audit / "new_historical_exclusions.csv",
        "frozen_overlap": audit / "new_historical_frozen_overlap_audit.csv",
        "duplicate_nearduplicate": audit / "new_historical_duplicate_nearduplicate_audit.csv",
        "manifest": audit / "new_historical_ingestion_manifest.json",
        "hashes": audit / "new_historical_artifact_hashes.csv",
    }


def ingest_new_data(
    workbook_path: Path,
    requested_sheets: Iterable[str],
    contract: dict[str, Any],
    interim_dir: Path,
    audit_dir: Path,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Run the frozen future path without constructing H150/H200 or retrieval outputs."""

    frozen = validate_frozen_datasets(contract)
    requested = validate_future_workbook_sheet_order(workbook_path, requested_sheets, contract)
    output_paths = prospective_output_paths(interim_dir, audit_dir)
    parsed_sheets = parse_future_new_sheets(workbook_path, requested, contract)
    fieldnames, normalized_rows, parser_rows_by_sheet = parser_rows_and_columns(parsed_sheets)
    curated_rows, curation_stats, curation_excluded = build_data_aduanas_splits.classify_rows(
        fieldnames, normalized_rows, contract["future_curation"]["eligible_class"]
    )
    frozen_audit = audit_future_rows(curated_rows, contract)
    eligible_rows = frozen_audit["accepted_for_later_curation"]
    exclusions: list[dict[str, Any]] = []
    for stage, rows in curation_excluded.items():
        for row in rows:
            exclusions.append({"exclusion_stage": f"curation_{stage}", **row})
    for row in frozen_audit["audited_rows"]:
        if row["eligible"] == "false":
            exclusions.append({"exclusion_stage": "frozen_overlap", **row})
    duplicate_audit = duplicate_nearduplicate_audit(eligible_rows, contract)
    capacity = capacity_descriptor(len(eligible_rows), contract)

    write_csv_rows(output_paths["normalized_all"], normalized_rows, fieldnames, overwrite)
    write_csv_rows(output_paths["curated"], curated_rows, fieldnames, overwrite)
    write_csv_rows(output_paths["eligible"], eligible_rows, fieldnames, overwrite)
    write_csv_rows(output_paths["exclusions"], exclusions, ["exclusion_stage"], overwrite)
    write_csv_rows(output_paths["frozen_overlap"], frozen_audit["audited_rows"], fieldnames, overwrite)
    write_csv_rows(output_paths["duplicate_nearduplicate"], duplicate_audit, ["record_type"], overwrite)

    workbook_sha = sha256_file(workbook_path)
    manifest = {
        "version": "v0.1",
        "gate": "NEW_HISTORICAL_GATE_02",
        "workbook": {
            "path": str(workbook_path),
            "sha256": workbook_sha,
            "size_bytes": workbook_path.stat().st_size,
            "sheet_order": inspect_workbook(workbook_path),
        },
        "new_sheets_requested": requested,
        "parser": {
            "module": contract["future_parser"]["module"],
            "explicit_sheet_selection": True,
            "rows_by_sheet": parser_rows_by_sheet,
        },
        "python_version": sys.version,
        "execution_commit": execution_commit(),
        "frozen_datasets": frozen,
        "counts": {
            "rows_parsed": len(normalized_rows),
            "rows_class_87": curation_stats["source_rows_scope_class"],
            "rows_quality_eligible": curation_stats["rows_after_inclusion_quality_rules"],
            "rows_after_new_data_duplicate_policy": curation_stats["rows_curated_after_duplicate_policy"],
            "rows_excluded_fixed_dev_eval_dam": len(frozen_audit["EXCLUDED_FIXED_DEV_EVAL_DAM"]),
            "rows_with_frozen_id_overlap": len(frozen_audit["EXISTING_FROZEN_ID_UNICO_OVERLAP"]),
            "rows_final_eligible": len(eligible_rows),
            "unique_dam_final_eligible": len({row.get("DECLARACION", "") for row in eligible_rows if row.get("DECLARACION", "")}),
            "unique_nandina_final_eligible": len({row.get("NANDINA", "") for row in eligible_rows if row.get("NANDINA", "")}),
        },
        "curation": curation_stats,
        "capacity": capacity,
        "model_metric_selection_used": False,
        "retrieval_executed": False,
        "creates_H150_or_H200": False,
        "outputs": {key: str(path) for key, path in output_paths.items() if key != "hashes"},
    }
    write_json_output(output_paths["manifest"], manifest, overwrite)
    hash_rows = []
    for key, path in output_paths.items():
        if key == "hashes":
            continue
        hash_rows.append({"artifact": key, "path": str(path), "sha256": sha256_file(path), "size_bytes": path.stat().st_size})
    write_csv_rows(output_paths["hashes"], hash_rows, ["artifact", "path", "sha256", "size_bytes"], overwrite)
    return {"manifest": manifest, "paths": output_paths, "eligible_rows": eligible_rows}


def freeze_source_bytes(source_path: Path, archive_path: Path, expected_sha: str) -> dict[str, Any]:
    """Copy the source as bytes with Python; never load or serialize it as XLSX."""

    before_sha = sha256_file(source_path)
    require_equal(before_sha, expected_sha, "SHA-256 de fuente antes de freeze")
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    if archive_path.exists() and sha256_file(archive_path) != expected_sha:
        raise ContractViolation(f"Archivo de archivo existente no coincide: {archive_path}")
    shutil.copy2(source_path, archive_path)
    archive_sha = sha256_file(archive_path)
    after_sha = sha256_file(source_path)
    require_equal(archive_sha, expected_sha, "SHA-256 de copia archivada")
    require_equal(after_sha, before_sha, "SHA-256 de fuente despues de freeze")
    return {
        "source_sha256_before": before_sha,
        "source_sha256_after": after_sha,
        "archive_sha256": archive_sha,
        "archive_path": str(archive_path),
        "archive_size_bytes": archive_path.stat().st_size,
        "copy_method": "Python shutil.copy2 binary copy",
        "source_mutated": False,
    }


def write_manifest(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preflight", action="store_true", help="verifica fuente y datasets congelados")
    parser.add_argument("--freeze-source", action="store_true", help="copia la fuente actual como bytes mediante Python")
    parser.add_argument("--source", type=Path, default=None, help="workbook actual; por defecto, la ruta congelada")
    parser.add_argument("--archive-path", type=Path, default=DEFAULT_ARCHIVE_PATH, help="destino local externo del XLSX congelado")
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT_PATH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--future-workbook", type=Path, help="workbook ampliado para validacion futura, sin ingesta")
    parser.add_argument("--new-sheet", action="append", default=[], help="nombre explicito NUEVA_01 o NUEVA_02")
    parser.add_argument("--validate-new-sheets", action="store_true", help="valida contrato futuro; no procesa ni escribe datasets")
    parser.add_argument("--ingest-new-data", action="store_true", help="ejecuta el path prospectivo solo sobre hojas nuevas explicitas")
    parser.add_argument("--future-output-dir", type=Path, default=DEFAULT_INTERIM_OUTPUT_DIR)
    parser.add_argument("--future-audit-dir", type=Path, default=DEFAULT_FUTURE_AUDIT_DIR)
    parser.add_argument("--overwrite", action="store_true", help="permite reemplazar un output prospectivo existente")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not any((args.preflight, args.freeze_source, args.validate_new_sheets, args.ingest_new_data)):
        print("ERROR: se requiere --preflight, --freeze-source, --validate-new-sheets o --ingest-new-data", file=sys.stderr)
        return 2
    try:
        contract = read_contract(args.contract)
        source_path: Path | None = None
        if args.preflight or args.freeze_source:
            source_path = args.source or resolve_repo_path(contract["current_source"]["path"])
        preflight: dict[str, Any] | None = None
        if args.preflight or args.freeze_source:
            assert source_path is not None
            source = validate_current_source(source_path, contract)
            datasets = validate_frozen_datasets(contract)
            preflight = {
                "CURRENT_SOURCE_FREEZE_READY": True,
                "NEW_DATA_SHEETS_PRESENT": source["new_data_sheets_present"],
                "NEW_DATA_INGESTION_EXECUTED": False,
                "source": source,
                "frozen_datasets": datasets,
            }
        if args.validate_new_sheets:
            if args.future_workbook is None:
                raise ContractViolation("--validate-new-sheets requiere --future-workbook")
            validate_future_workbook_sheet_order(args.future_workbook, args.new_sheet, contract)
        ingestion: dict[str, Any] | None = None
        if args.ingest_new_data:
            if args.future_workbook is None:
                raise ContractViolation("--ingest-new-data requiere --future-workbook")
            ingestion = ingest_new_data(
                args.future_workbook,
                args.new_sheet,
                contract,
                args.future_output_dir,
                args.future_audit_dir,
                overwrite=args.overwrite,
            )
        freeze: dict[str, Any] | None = None
        if args.freeze_source:
            assert source_path is not None
            freeze = freeze_source_bytes(source_path, args.archive_path, contract["current_source"]["sha256"])
        if args.preflight or args.freeze_source:
            manifest = {
                "version": "v0.1",
                "gate": "NEW_HISTORICAL_GATE_02",
                "generated_at_utc": datetime.now(timezone.utc).isoformat(),
                "source_classification": contract["source_classification"],
                "source_statement": contract["source_statement"],
                "preflight": preflight,
                "freeze": freeze,
                "contract": {
                    "preexisting_source_sheets": contract["preexisting_source_sheets"],
                    "historically_processed_sheet": contract["historically_processed_sheet"],
                    "new_sheet_sets": contract["new_sheet_sets"],
                    "explicit_sheet_selection_required": True,
                    "H100_rebuild_from_expanded_workbook_forbidden": True,
                },
            }
            write_manifest(args.manifest, manifest)
        print("RESULT: PASS")
        if preflight:
            print("CURRENT_SOURCE_FREEZE_READY=true")
            print(f"NEW_DATA_SHEETS_PRESENT={str(preflight['NEW_DATA_SHEETS_PRESENT']).lower()}")
            print("NEW_DATA_INGESTION_EXECUTED=false")
        if freeze:
            print("CURRENT_H100_REPRODUCING_SOURCE_FROZEN=true")
            print(f"SOURCE_SHA={freeze['source_sha256_after']}")
            print(f"ARCHIVE_SHA={freeze['archive_sha256']}")
        if ingestion:
            print("NEW_DATA_INGESTION_EXECUTED=true")
            print(f"NEW_ELIGIBLE_HISTORICAL_ROWS={len(ingestion['eligible_rows'])}")
        return 0
    except ContractViolation as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
