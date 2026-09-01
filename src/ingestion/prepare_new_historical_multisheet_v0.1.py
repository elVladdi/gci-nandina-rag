"""Fail-closed source freeze and prospective multisheet contract for Gate 02.

This module does not ingest new historical data. Its only executable modes in
this gate are a preflight of the current reproducing source and a binary source
freeze. The future helper calls the established SUNAT parser with an explicit
sheet name and never selects the first worksheet by position.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import openpyxl

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.ingestion import sunat_series_parser


DEFAULT_CONTRACT_PATH = ROOT / "src" / "configs" / "new_historical_multisheet_contract_v0.1.json"
DEFAULT_MANIFEST_PATH = ROOT / "outputs" / "audits" / "new_historical_gate_v0.1" / "source_freeze_manifest_v0.1.json"
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
    return {
        "path": str(source_path),
        "sha256": source_sha,
        "size_bytes": source_size,
        "sheet_order": sheet_names,
        "new_data_sheets_present": any(name in sheet_names for name in contract["allowed_new_sheets"]),
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


def validate_new_sheet_names(requested_sheets: Iterable[str], contract: dict[str, Any]) -> list[str]:
    requested = list(requested_sheets)
    if not requested:
        raise ContractViolation("La ejecucion futura requiere al menos una hoja nueva explicita")
    if len(requested) != len(set(requested)):
        raise ContractViolation("Las hojas nuevas explicitas no pueden repetirse")
    historical = set(contract["historical_sheets"])
    allowed = set(contract["allowed_new_sheets"])
    for sheet in requested:
        if sheet in historical:
            raise ContractViolation(f"La hoja historica no puede declararse nueva: {sheet}")
        if sheet not in allowed:
            raise ContractViolation(f"Hoja nueva no autorizada por contrato: {sheet}")
    return requested


def validate_future_workbook_sheet_order(
    workbook_path: Path, requested_sheets: Iterable[str], contract: dict[str, Any]
) -> list[str]:
    requested = validate_new_sheet_names(requested_sheets, contract)
    sheet_names = inspect_workbook(workbook_path)
    expected_prefix = contract["historical_sheets"]
    require_equal(sheet_names[: len(expected_prefix)], expected_prefix, "Prefijo historico de hojas")
    actual_new = sheet_names[len(expected_prefix) :]
    allowed = contract["allowed_new_sheets"]
    if actual_new != [name for name in allowed if name in actual_new]:
        raise ContractViolation(f"Orden o nombres de hojas nuevas no autorizados: {actual_new!r}")
    for sheet in requested:
        if sheet not in actual_new:
            raise ContractViolation(f"Hoja nueva solicitada ausente del workbook: {sheet}")
    return requested


def parse_future_new_sheet(workbook_path: Path, sheet_name: str, contract: dict[str, Any]):
    """Delegate future parsing to the historical parser with an explicit sheet."""

    validate_future_workbook_sheet_order(workbook_path, [sheet_name], contract)
    return sunat_series_parser.parse_workbook(workbook_path, sheet_name=sheet_name)


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
    """Classify future rows without creating or modifying a historical dataset."""

    protected_dams = frozen_dev_eval_dams(contract)
    protected_ids = frozen_ids(contract)
    accepted: list[dict[str, str]] = []
    excluded_dev_eval_dam: list[dict[str, str]] = []
    existing_id_overlap: list[dict[str, str]] = []
    for row in rows:
        if row.get("DECLARACION", "").strip() in protected_dams:
            excluded_dev_eval_dam.append(row)
        elif row.get("id_unico", "").strip() in protected_ids:
            existing_id_overlap.append(row)
        else:
            accepted.append(row)
    return {
        "accepted_for_later_curation": accepted,
        "EXCLUDED_FIXED_DEV_EVAL_DAM": excluded_dev_eval_dam,
        "EXISTING_FROZEN_ID_UNICO_OVERLAP": existing_id_overlap,
    }


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
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not any((args.preflight, args.freeze_source, args.validate_new_sheets)):
        print("ERROR: se requiere --preflight, --freeze-source o --validate-new-sheets", file=sys.stderr)
        return 2
    try:
        contract = read_contract(args.contract)
        source_path = args.source or resolve_repo_path(contract["current_source"]["path"])
        preflight: dict[str, Any] | None = None
        if args.preflight or args.freeze_source:
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
        freeze: dict[str, Any] | None = None
        if args.freeze_source:
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
                    "historical_sheets": contract["historical_sheets"],
                    "allowed_new_sheets": contract["allowed_new_sheets"],
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
        return 0
    except ContractViolation as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
