from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable

EVALSET_REQUIRED_COLUMNS = [
    "case_id",
    "descripcion",
    "nandina_ref",
    "regimen",
    "fuente_url",
    "fecha_consulta",
]
EVALSET_OPTIONAL_COLUMNS = ["capitulo", "partida", "origen_caso", "observaciones"]
DEVSET_REQUIRED_COLUMNS = ["descripcion", "nandina"]
TARGET_EVALSET_SIZE = 300
NANDINA8_RE = re.compile(r"^\d{8}$")


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _row_label(row_number: int) -> str:
    return f"fila {row_number}"


def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            return [], []
        fieldnames = [_clean(name) for name in reader.fieldnames]
        rows = []
        for row in reader:
            rows.append({_clean(key): _clean(value) for key, value in row.items() if key is not None})
    return fieldnames, rows


def _missing_columns(fieldnames: Iterable[str], required: Iterable[str]) -> list[str]:
    present = set(fieldnames)
    return [column for column in required if column not in present]


def _duplicate_values(values: Iterable[str]) -> list[str]:
    counts = Counter(value for value in values if value)
    return sorted(value for value, count in counts.items() if count > 1)


def _validate_nandina8(value: str) -> bool:
    return bool(NANDINA8_RE.fullmatch(value))


def validate_evalset(fieldnames: list[str], rows: list[dict[str, str]]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    missing = _missing_columns(fieldnames, EVALSET_REQUIRED_COLUMNS)
    if missing:
        errors.append("Faltan columnas obligatorias del evalset: " + ", ".join(missing))
        return errors, warnings

    known_columns = set(EVALSET_REQUIRED_COLUMNS + EVALSET_OPTIONAL_COLUMNS)
    extra_columns = [column for column in fieldnames if column not in known_columns]
    if extra_columns:
        warnings.append("Columnas no previstas en el protocolo: " + ", ".join(extra_columns))

    case_ids: list[str] = []
    semantic_keys: list[str] = []

    for index, row in enumerate(rows, start=2):
        label = _row_label(index)
        case_id = _clean(row.get("case_id"))
        descripcion = _clean(row.get("descripcion"))
        nandina_ref = _clean(row.get("nandina_ref"))
        regimen = _clean(row.get("regimen"))
        fuente_url = _clean(row.get("fuente_url"))
        fecha_consulta = _clean(row.get("fecha_consulta"))

        if not case_id:
            errors.append(f"{label}: case_id vacio")
        if not descripcion:
            errors.append(f"{label}: descripcion vacia")
        if not _validate_nandina8(nandina_ref):
            errors.append(f"{label}: nandina_ref debe tener exactamente 8 digitos: {nandina_ref!r}")
        if not regimen:
            errors.append(f"{label}: regimen vacio")
        if not fuente_url:
            errors.append(f"{label}: fuente_url vacia")
        if not fecha_consulta:
            errors.append(f"{label}: fecha_consulta vacia")

        capitulo = _clean(row.get("capitulo"))
        if capitulo and _validate_nandina8(nandina_ref) and capitulo.zfill(2) != nandina_ref[:2]:
            errors.append(
                f"{label}: capitulo={capitulo!r} no coincide con nandina_ref[:2]={nandina_ref[:2]!r}"
            )

        partida = _clean(row.get("partida"))
        if partida and _validate_nandina8(nandina_ref) and partida.zfill(4) != nandina_ref[:4]:
            errors.append(
                f"{label}: partida={partida!r} no coincide con nandina_ref[:4]={nandina_ref[:4]!r}"
            )

        case_ids.append(case_id)
        semantic_keys.append("\u241f".join([descripcion.lower(), nandina_ref, regimen.lower()]))

    duplicate_case_ids = _duplicate_values(case_ids)
    if duplicate_case_ids:
        errors.append("case_id duplicado: " + ", ".join(duplicate_case_ids))

    duplicate_semantic_keys = _duplicate_values(semantic_keys)
    if duplicate_semantic_keys:
        errors.append(
            "Duplicados por descripcion + nandina_ref + regimen: "
            + "; ".join(key.replace("\u241f", " | ") for key in duplicate_semantic_keys)
        )

    if len(rows) < TARGET_EVALSET_SIZE:
        warnings.append(
            f"El dataset tiene {len(rows)} casos; el objetivo metodologico es aproximadamente {TARGET_EVALSET_SIZE}."
        )

    return errors, warnings


def validate_devset(fieldnames: list[str], rows: list[dict[str, str]]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = [
        "Modo devset preliminar: este archivo sirve para desarrollo/smoke tests y no para evaluacion final."
    ]

    missing = _missing_columns(fieldnames, DEVSET_REQUIRED_COLUMNS)
    if missing:
        errors.append("Faltan columnas obligatorias del devset preliminar: " + ", ".join(missing))
        return errors, warnings

    semantic_keys: list[str] = []
    for index, row in enumerate(rows, start=2):
        label = _row_label(index)
        descripcion = _clean(row.get("descripcion"))
        nandina = _clean(row.get("nandina"))
        if not descripcion:
            errors.append(f"{label}: descripcion vacia")
        if not _validate_nandina8(nandina):
            errors.append(f"{label}: nandina debe tener exactamente 8 digitos: {nandina!r}")
        semantic_keys.append("\u241f".join([descripcion.lower(), nandina]))

    duplicate_semantic_keys = _duplicate_values(semantic_keys)
    if duplicate_semantic_keys:
        warnings.append(
            "Duplicados preliminares por descripcion + nandina: "
            + "; ".join(key.replace("\u241f", " | ") for key in duplicate_semantic_keys)
        )

    warnings.append(f"Conteo devset preliminar: {len(rows)} casos.")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida el esquema y reglas minimas del evalset NANDINA v0.1."
    )
    parser.add_argument("csv_path", type=Path, help="Ruta al CSV a validar.")
    parser.add_argument(
        "--devset",
        "--allow-devset-schema",
        action="store_true",
        dest="allow_devset_schema",
        help="Permite validar el devset preliminar con columnas descripcion,nandina.",
    )
    args = parser.parse_args()

    if not args.csv_path.exists():
        print(f"ERROR: no existe el archivo: {args.csv_path}", file=sys.stderr)
        return 2

    fieldnames, rows = _read_csv(args.csv_path)
    if not fieldnames:
        print("ERROR: el CSV no contiene encabezados.", file=sys.stderr)
        return 2

    if args.allow_devset_schema:
        errors, warnings = validate_devset(fieldnames, rows)
        schema_name = "devset preliminar"
    else:
        errors, warnings = validate_evalset(fieldnames, rows)
        schema_name = "evalset v0.1"

    print(f"Archivo: {args.csv_path}")
    print(f"Esquema validado: {schema_name}")
    print(f"Columnas: {', '.join(fieldnames)}")
    print(f"Conteo total: {len(rows)}")

    for warning in warnings:
        print(f"ADVERTENCIA: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"Resultado: FALLA ({len(errors)} error(es) critico(s)).", file=sys.stderr)
        return 1

    print("Resultado: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
