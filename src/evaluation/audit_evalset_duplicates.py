from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from .build_evalset_from_sunat_excel import (
        DEFAULT_ORIGEN_CASO,
        DEFAULT_SOURCE_URL,
        OUTPUT_COLUMNS,
        _clean,
        _sha256,
        extract_evalset,
        validate_fecha_consulta,
    )
except ImportError:  # Allows direct execution as a script from the repository root.
    from build_evalset_from_sunat_excel import (  # type: ignore
        DEFAULT_ORIGEN_CASO,
        DEFAULT_SOURCE_URL,
        OUTPUT_COLUMNS,
        _clean,
        _sha256,
        extract_evalset,
        validate_fecha_consulta,
    )

DEFAULT_OUTPUT_DIR = Path("outputs/audits/evalset_v0.1_duplicates")
DUPLICATE_KEY_SEPARATOR = "\u241f"


def duplicate_key(row: dict[str, str]) -> str:
    return DUPLICATE_KEY_SEPARATOR.join(
        [
            _clean(row.get("descripcion")).lower(),
            _clean(row.get("nandina_ref")),
            _clean(row.get("regimen")).lower(),
        ]
    )


def duplicate_key_hash(key: str) -> str:
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def is_valid_row(row: dict[str, str]) -> bool:
    return all(
        [
            _clean(row.get("case_id")),
            _clean(row.get("descripcion")),
            bool(re.fullmatch(r"\d{8}", _clean(row.get("nandina_ref")))),
            _clean(row.get("regimen")),
            _clean(row.get("fuente_url")),
            _clean(row.get("fecha_consulta")),
        ]
    )


def distribution(rows: list[dict[str, str]], column: str) -> dict[str, int]:
    counter = Counter(_clean(row.get(column)) or "<VACIO>" for row in rows)
    return dict(sorted(counter.items(), key=lambda item: (-item[1], item[0])))


def semantic_groups(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[duplicate_key(row)].append(row)
    return groups


def description_review_groups(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[_clean(row.get("descripcion")).lower()].append(row)

    review_groups: list[dict[str, Any]] = []
    for description, members in grouped.items():
        variants = sorted({(_clean(row.get("nandina_ref")), _clean(row.get("regimen"))) for row in members})
        if description and len(variants) > 1:
            review_groups.append(
                {
                    "descripcion": members[0].get("descripcion", ""),
                    "filas": len(members),
                    "variantes_nandina_regimen": [f"{nandina}|{regimen}" for nandina, regimen in variants],
                    "case_ids": [row.get("case_id", "") for row in members],
                }
            )
    return sorted(review_groups, key=lambda item: (-item["filas"], item["descripcion"]))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Ya existe {path}. Use --overwrite para reemplazarlo.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, Any], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Ya existe {path}. Use --overwrite para reemplazarlo.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def build_duplicate_group_rows(groups: dict[str, list[dict[str, str]]]) -> list[dict[str, Any]]:
    duplicate_rows: list[dict[str, Any]] = []
    group_number = 1
    for key, members in sorted(groups.items(), key=lambda item: (-len(item[1]), item[0])):
        if len(members) <= 1:
            continue
        first = members[0]
        duplicate_rows.append(
            {
                "group_id": f"DUP-{group_number:04d}",
                "duplicate_key_hash": duplicate_key_hash(key),
                "group_size": len(members),
                "duplicate_excess": len(members) - 1,
                "kept_case_id_recommended": first.get("case_id", ""),
                "all_case_ids": "|".join(row.get("case_id", "") for row in members),
                "nandina_ref": first.get("nandina_ref", ""),
                "regimen": first.get("regimen", ""),
                "descripcion": first.get("descripcion", ""),
                "observaciones": " || ".join(row.get("observaciones", "") for row in members),
            }
        )
        group_number += 1
    return duplicate_rows


def audit_rows(rows: list[dict[str, str]]) -> dict[str, Any]:
    groups = semantic_groups(rows)
    duplicate_group_rows = build_duplicate_group_rows(groups)
    duplicate_group_count = len(duplicate_group_rows)
    duplicate_excess_rows = sum(row["duplicate_excess"] for row in duplicate_group_rows)
    valid_rows = [row for row in rows if is_valid_row(row)]

    extraction_summary = {
        "total_extraido": len(rows),
        "validos": len(valid_rows),
        "invalidos": len(rows) - len(valid_rows),
        "combinaciones_unicas_descripcion_nandina_regimen": len(groups),
        "grupos_duplicados": duplicate_group_count,
        "filas_duplicadas_excedentes": duplicate_excess_rows,
        "casos_si_conserva_primer_duplicado_exacto": len(groups),
        "nandina_valida_8": sum(1 for row in rows if re.fullmatch(r"\d{8}", _clean(row.get("nandina_ref")))),
        "descripcion_no_vacia": sum(1 for row in rows if _clean(row.get("descripcion"))),
        "regimen_no_vacio": sum(1 for row in rows if _clean(row.get("regimen"))),
    }

    duplicate_summary = {
        "criterio_duplicado": "descripcion + nandina_ref + regimen normalizados en minusculas para texto",
        "total_casos_extraidos": len(rows),
        "total_combinaciones_unicas": len(groups),
        "numero_grupos_duplicados": duplicate_group_count,
        "numero_filas_duplicadas_excedentes": duplicate_excess_rows,
        "casos_resultantes_si_se_conserva_primero": len(groups),
        "distribucion_por_regimen": distribution(rows, "regimen"),
        "distribucion_por_capitulo": distribution(rows, "capitulo"),
        "distribucion_por_nandina": distribution(rows, "nandina_ref"),
        "grupos_misma_descripcion_con_nandina_o_regimen_distinto": description_review_groups(rows),
    }

    return {
        "duplicate_group_rows": duplicate_group_rows,
        "duplicate_summary": duplicate_summary,
        "extraction_summary": extraction_summary,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audita duplicados del evalset SUNAT antes de generar el dataset final.")
    parser.add_argument("--input", required=True, type=Path, help="Ruta al Excel o CSV fuente.")
    parser.add_argument(
        "--format",
        choices=["auto", "table", "sunat-block"],
        default="auto",
        dest="input_format",
        help="Formato de entrada para reutilizar el extractor.",
    )
    parser.add_argument("--source-url", default=DEFAULT_SOURCE_URL, help="URL fuente aplicada a todas las filas.")
    parser.add_argument("--fecha-consulta", required=True, type=validate_fecha_consulta, help="Fecha YYYY-MM-DD.")
    parser.add_argument("--origen-caso", default=DEFAULT_ORIGEN_CASO, help="Valor para origen_caso.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directorio de reportes de auditoria.")
    parser.add_argument("--overwrite", action="store_true", help="Permite reemplazar reportes de auditoria existentes.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.exists():
        print(f"ERROR: no existe el input: {args.input}")
        return 2

    result = extract_evalset(
        input_path=args.input,
        input_format=args.input_format,
        source_url=args.source_url,
        fecha_consulta=args.fecha_consulta,
        origen_caso=_clean(args.origen_caso) or DEFAULT_ORIGEN_CASO,
    )
    audit = audit_rows(result.rows)

    output_dir = args.output_dir
    extracted_path = output_dir / "extracted_preview.csv"
    duplicate_groups_path = output_dir / "duplicate_groups.csv"
    duplicate_summary_path = output_dir / "duplicate_summary.json"
    extraction_summary_path = output_dir / "extraction_summary.json"

    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    common_context = {
        "input_path": str(args.input),
        "input_sha256": _sha256(args.input),
        "input_format_requested": args.input_format,
        "detected_format": result.detected_format,
        "source_url": args.source_url,
        "fecha_consulta": args.fecha_consulta,
        "origen_caso": _clean(args.origen_caso) or DEFAULT_ORIGEN_CASO,
        "generated_at_utc": generated_at,
        "output_dir": str(output_dir),
        "reglas_extraccion": result.rules_applied,
    }

    write_csv(extracted_path, OUTPUT_COLUMNS, result.rows, overwrite=args.overwrite)
    write_csv(
        duplicate_groups_path,
        [
            "group_id",
            "duplicate_key_hash",
            "group_size",
            "duplicate_excess",
            "kept_case_id_recommended",
            "all_case_ids",
            "nandina_ref",
            "regimen",
            "descripcion",
            "observaciones",
        ],
        audit["duplicate_group_rows"],
        overwrite=args.overwrite,
    )
    write_json(duplicate_summary_path, {**common_context, **audit["duplicate_summary"]}, overwrite=args.overwrite)
    write_json(extraction_summary_path, {**common_context, **audit["extraction_summary"]}, overwrite=args.overwrite)

    summary = audit["extraction_summary"]
    print(f"Formato detectado: {result.detected_format}")
    print(f"Total extraido: {summary['total_extraido']}")
    print(f"Validos: {summary['validos']}")
    print(f"Invalidos: {summary['invalidos']}")
    print(f"Combinaciones unicas descripcion + nandina_ref + regimen: {summary['combinaciones_unicas_descripcion_nandina_regimen']}")
    print(f"Grupos duplicados: {summary['grupos_duplicados']}")
    print(f"Filas duplicadas excedentes: {summary['filas_duplicadas_excedentes']}")
    print(f"Casos si se conserva primer duplicado exacto: {summary['casos_si_conserva_primer_duplicado_exacto']}")
    print(f"Reportes escritos en: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())