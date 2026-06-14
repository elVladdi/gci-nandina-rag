from __future__ import annotations

import argparse
import csv
import hashlib
from collections import defaultdict
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, NamedTuple

try:
    from .validate_dataset import _read_csv, validate_evalset
except ImportError:  # Allows direct execution as a script from the repository root.
    from validate_dataset import _read_csv, validate_evalset  # type: ignore

DEFAULT_SOURCE_URL = "http://www.aduanet.gob.pe/aduanas/informgest/sgdespa.htm#REGIMENES_DEFINITIVOS"
DEFAULT_OUTPUT = Path("data/processed/evalset_v0.1.csv")
DEFAULT_ORIGEN_CASO = "SUNAT_ADUANET"
OUTPUT_COLUMNS = [
    "case_id",
    "descripcion",
    "nandina_ref",
    "regimen",
    "fuente_url",
    "fecha_consulta",
    "capitulo",
    "partida",
    "origen_caso",
    "observaciones",
]
COLUMN_ALIASES = {
    "descripcion": {
        "descripcion",
        "descripcionmercancia",
        "descripcioncomercial",
        "mercancia",
        "producto",
    },
    "nandina": {
        "nandina",
        "nandinaref",
        "codigo",
        "codigonandina",
        "codigoarancelario",
        "subpartida",
        "subpartidanandina",
    },
    "regimen": {"regimen", "regimenaduanero"},
    "observaciones": {"observaciones", "observacion", "comentarios", "comentario"},
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SERIES_RE = re.compile(r"^\d+(?:\.0)?$")
DEDUPE_KEY_SEPARATOR = "\\u241f"
SUNAT_DOTTED_CODE_RE = re.compile(
    r"(?<!\d)(\d{2})\s*\.\s*(\d{2})\s*\.\s*(\d{2})\s*\.\s*(\d{2})(?:\s*\.\s*\d{2})?(?!\d)"
)


class ExtractionResult(NamedTuple):
    detected_format: str
    rows: list[dict[str, str]]
    rows_input: int
    source_columns: list[str]
    detected_columns: dict[str, str]
    rules_applied: list[str]


def _clean(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\xa0", " ").strip()
    if text.lower() in {"nan", "nat", "none"}:
        return ""
    return re.sub(r"\s+", " ", text)


def _normalize_column_name(name: str) -> str:
    text = unicodedata.normalize("NFKD", _clean(name))
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _metadata_path(output_path: Path) -> Path:
    return output_path.with_name(f"{output_path.stem}_metadata.json")


def _load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("El CSV de entrada no contiene encabezados.")
        fieldnames = [_clean(field) for field in reader.fieldnames]
        rows = []
        for row in reader:
            rows.append({_clean(key): _clean(value) for key, value in row.items() if key is not None})
    return fieldnames, rows


def _load_xlsx(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    try:
        import pandas as pd
    except ImportError as exc:
        raise RuntimeError("Para leer .xlsx se requiere pandas instalado.") from exc

    try:
        frame = pd.read_excel(path, dtype=str, keep_default_na=False, engine="openpyxl")
    except ImportError as exc:
        raise RuntimeError("Para leer .xlsx se requiere openpyxl en requirements.txt e instalado en el entorno.") from exc

    fieldnames = [_clean(column) for column in frame.columns]
    rows = []
    for record in frame.to_dict(orient="records"):
        rows.append({_clean(key): _clean(value) for key, value in record.items()})
    return fieldnames, rows


def load_input(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return _load_csv(path)
    if suffix == ".xlsx":
        return _load_xlsx(path)
    raise ValueError(f"Formato no soportado: {suffix}. Use .xlsx o .csv.")


def try_detect_columns(fieldnames: Iterable[str]) -> dict[str, str] | None:
    detected: dict[str, str] = {}
    normalized_to_original = {_normalize_column_name(field): field for field in fieldnames}

    for canonical, aliases in COLUMN_ALIASES.items():
        for alias in aliases:
            if alias in normalized_to_original:
                detected[canonical] = normalized_to_original[alias]
                break

    missing = [column for column in ["descripcion", "nandina", "regimen"] if column not in detected]
    if missing:
        return None
    return detected


def detect_columns(fieldnames: Iterable[str]) -> dict[str, str]:
    detected = try_detect_columns(fieldnames)
    if detected is None:
        raise ValueError(
            "No se detectaron columnas obligatorias de entrada: descripcion, nandina, regimen. "
            + "Encabezados encontrados: "
            + ", ".join(fieldnames)
        )
    return detected


def normalize_nandina(raw_value: str) -> tuple[str, str]:
    value = _clean(raw_value)
    compact = re.sub(r"[.\s]+", "", value)
    if compact.isdigit() and len(compact) == 8:
        if compact != value:
            return compact, "nandina_normalizada_removiendo_puntos_o_espacios"
        return compact, ""
    return value, "nandina_no_normalizada_por_formato_no_8_digitos"


def is_blank_source_row(row: dict[str, str], detected: dict[str, str]) -> bool:
    relevant = [detected.get("descripcion"), detected.get("nandina"), detected.get("regimen")]
    return all(not _clean(row.get(column or "")) for column in relevant)


def build_evalset_rows(
    source_rows: list[dict[str, str]],
    detected: dict[str, str],
    source_url: str,
    fecha_consulta: str,
    origen_caso: str,
) -> list[dict[str, str]]:
    output_rows: list[dict[str, str]] = []

    for row in source_rows:
        if is_blank_source_row(row, detected):
            continue

        descripcion = _clean(row.get(detected["descripcion"]))
        nandina_ref, nandina_note = normalize_nandina(row.get(detected["nandina"], ""))
        regimen = _clean(row.get(detected["regimen"]))
        observaciones = _clean(row.get(detected.get("observaciones", "")))
        if nandina_note and nandina_note != "nandina_normalizada_removiendo_puntos_o_espacios":
            observaciones = "; ".join(part for part in [observaciones, nandina_note] if part)

        if re.fullmatch(r"\d{8}", nandina_ref):
            capitulo = nandina_ref[:2]
            partida = nandina_ref[:4]
        else:
            capitulo = ""
            partida = ""

        output_rows.append(
            {
                "case_id": f"SUNAT-{len(output_rows) + 1:04d}",
                "descripcion": descripcion,
                "nandina_ref": nandina_ref,
                "regimen": regimen,
                "fuente_url": source_url,
                "fecha_consulta": fecha_consulta,
                "capitulo": capitulo,
                "partida": partida,
                "origen_caso": origen_caso,
                "observaciones": observaciones,
            }
        )

    return output_rows


def extract_table(
    input_path: Path,
    source_url: str,
    fecha_consulta: str,
    origen_caso: str,
) -> ExtractionResult:
    fieldnames, source_rows = load_input(input_path)
    detected = detect_columns(fieldnames)
    output_rows = build_evalset_rows(source_rows, detected, source_url, fecha_consulta, origen_caso)
    return ExtractionResult(
        detected_format="table",
        rows=output_rows,
        rows_input=len(source_rows),
        source_columns=fieldnames,
        detected_columns=detected,
        rules_applied=[
            "limpieza de espacios al inicio y final",
            "normalizacion de encabezados sin acentos y sin distincion de mayusculas",
            "nandina_ref conserva ceros iniciales al leer como texto",
            "remocion de puntos y espacios en NANDINA solo si el resultado tiene 8 digitos",
            "capitulo derivado de los dos primeros digitos de nandina_ref",
            "partida derivada de los cuatro primeros digitos de nandina_ref",
            "case_id estable con patron SUNAT-0001",
            "fuente_url y fecha_consulta aplicadas desde argumentos",
        ],
    )


def _load_raw_sheets(path: Path) -> dict[str, list[list[str]]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return {"csv": [[_clean(value) for value in row] for row in csv.reader(handle)]}
    if suffix != ".xlsx":
        raise ValueError(f"Formato no soportado para sunat-block: {suffix}. Use .xlsx o .csv.")

    try:
        import pandas as pd
    except ImportError as exc:
        raise RuntimeError("Para leer .xlsx se requiere pandas instalado.") from exc

    try:
        excel = pd.ExcelFile(path, engine="openpyxl")
        sheets: dict[str, list[list[str]]] = {}
        for sheet_name in excel.sheet_names:
            frame = pd.read_excel(
                path,
                sheet_name=sheet_name,
                header=None,
                dtype=str,
                keep_default_na=False,
                engine="openpyxl",
            )
            sheets[sheet_name] = [[_clean(value) for value in row] for row in frame.values.tolist()]
        return sheets
    except ImportError as exc:
        raise RuntimeError("Para leer .xlsx se requiere openpyxl en requirements.txt e instalado en el entorno.") from exc


def _is_series_start(row: list[str]) -> bool:
    first = _clean(row[0]) if row else ""
    return bool(SERIES_RE.fullmatch(first))


def _series_value(row: list[str]) -> str:
    first = _clean(row[0]) if row else ""
    return first[:-2] if first.endswith(".0") else first


def _last_nonempty(row: list[str]) -> str:
    for value in reversed(row):
        cleaned = _clean(value)
        if cleaned:
            return cleaned
    return ""


def _find_sunat_code(row: list[str]) -> tuple[str, int] | None:
    for index, value in enumerate(row):
        match = SUNAT_DOTTED_CODE_RE.search(_clean(value))
        if match:
            return "".join(match.groups()), index
    return None


def _looks_textual(value: str) -> bool:
    return any(char.isalpha() for char in value)


def _partida_description(row: list[str], code_col: int) -> str:
    for value in row[code_col + 1 :]:
        cleaned = _clean(value)
        if cleaned and _looks_textual(cleaned):
            return cleaned
    return ""


def _row_text(row: list[str]) -> str:
    values = [_clean(value) for value in row if _clean(value)]
    return " ".join(values)


def _make_observaciones(
    sheet_name: str,
    series: str,
    start_row: int,
    end_row: int,
    descripcion_partida: str,
) -> str:
    parts = [
        f"hoja={sheet_name}",
        f"serie={series}",
        f"fila_inicio={start_row}",
        f"fila_fin={end_row}",
    ]
    if descripcion_partida:
        parts.append(f"descripcion_partida={descripcion_partida}")
    return "; ".join(parts)


def extract_sunat_block(
    input_path: Path,
    source_url: str,
    fecha_consulta: str,
    origen_caso: str,
) -> ExtractionResult:
    sheets = _load_raw_sheets(input_path)
    output_rows: list[dict[str, str]] = []
    raw_row_count = 0

    for sheet_name, rows in sheets.items():
        raw_row_count += len(rows)
        starts = [idx for idx, row in enumerate(rows) if _is_series_start(row)]
        for position, start_idx in enumerate(starts):
            end_idx = starts[position + 1] if position + 1 < len(starts) else len(rows)
            block = rows[start_idx:end_idx]
            code_info: tuple[int, str, int] | None = None
            for relative_idx, row in enumerate(block):
                found = _find_sunat_code(row)
                if found:
                    nandina_ref, code_col = found
                    code_info = (start_idx + relative_idx, nandina_ref, code_col)
                    break
            if code_info is None:
                continue

            code_row_idx, nandina_ref, code_col = code_info
            code_row = rows[code_row_idx]
            descripcion_partida = _partida_description(code_row, code_col)
            descripcion_lines = []
            for row in rows[code_row_idx + 1 : end_idx]:
                line = _row_text(row)
                if line:
                    descripcion_lines.append(line)
            descripcion = " ".join(descripcion_lines)
            regimen = _last_nonempty(rows[start_idx])
            capitulo = nandina_ref[:2]
            partida = nandina_ref[:4]
            start_row_number = start_idx + 1
            end_row_number = end_idx if end_idx > start_idx else start_row_number

            output_rows.append(
                {
                    "case_id": f"SUNAT-{len(output_rows) + 1:04d}",
                    "descripcion": descripcion,
                    "nandina_ref": nandina_ref,
                    "regimen": regimen,
                    "fuente_url": source_url,
                    "fecha_consulta": fecha_consulta,
                    "capitulo": capitulo,
                    "partida": partida,
                    "origen_caso": origen_caso,
                    "observaciones": _make_observaciones(
                        sheet_name=sheet_name,
                        series=_series_value(rows[start_idx]),
                        start_row=start_row_number,
                        end_row=end_row_number,
                        descripcion_partida=descripcion_partida,
                    ),
                }
            )

    if not output_rows:
        raise ValueError("No se detectaron bloques SUNAT con serie y codigo NANDINA punteado.")

    return ExtractionResult(
        detected_format="sunat-block",
        rows=output_rows,
        rows_input=raw_row_count,
        source_columns=[],
        detected_columns={
            "serie": "primera columna de la fila de inicio",
            "regimen": "ultima columna no vacia de la fila de inicio",
            "nandina": "codigo punteado dentro del bloque",
            "descripcion": "filas posteriores al codigo NANDINA dentro del bloque",
        },
        rules_applied=[
            "lectura de hoja sin encabezados",
            "deteccion de inicio de serie en primera columna numerica",
            "regimen tomado de la ultima columna no vacia de la fila de inicio",
            "deteccion de codigo NANDINA punteado dentro del bloque",
            "conversion de codigo SUNAT punteado a NANDINA-8 usando los primeros 8 digitos",
            "descripcion de partida tomada de la misma fila del codigo cuando existe",
            "descripcion de mercancia unida desde filas posteriores hasta antes de la siguiente serie",
            "capitulo derivado de los dos primeros digitos de nandina_ref",
            "partida derivada de los cuatro primeros digitos de nandina_ref",
            "case_id estable con patron SUNAT-0001",
            "observaciones con hoja, serie, fila_inicio, fila_fin y descripcion_partida",
        ],
    )


def extract_evalset(
    input_path: Path,
    input_format: str,
    source_url: str,
    fecha_consulta: str,
    origen_caso: str,
) -> ExtractionResult:
    if input_format == "table":
        return extract_table(input_path, source_url, fecha_consulta, origen_caso)
    if input_format == "sunat-block":
        return extract_sunat_block(input_path, source_url, fecha_consulta, origen_caso)

    table_error: Exception | None = None
    try:
        return extract_table(input_path, source_url, fecha_consulta, origen_caso)
    except Exception as exc:
        table_error = exc

    try:
        return extract_sunat_block(input_path, source_url, fecha_consulta, origen_caso)
    except Exception as block_error:
        raise ValueError(
            "No se pudo autodetectar formato table ni sunat-block. "
            f"Error table: {table_error}. Error sunat-block: {block_error}"
        ) from block_error


def dedupe_key(row: dict[str, str]) -> str:
    return DEDUPE_KEY_SEPARATOR.join(
        [
            _clean(row.get("descripcion")).lower(),
            _clean(row.get("nandina_ref")),
            _clean(row.get("regimen")).lower(),
        ]
    )


def deduplicate_exact(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, Any]]:
    seen: set[str] = set()
    kept_rows: list[dict[str, str]] = []
    groups: dict[str, list[str]] = defaultdict(list)

    for row in rows:
        key = dedupe_key(row)
        groups[key].append(row.get("case_id", ""))
        if key in seen:
            continue
        seen.add(key)
        kept_rows.append(row)

    duplicate_groups = {key: case_ids for key, case_ids in groups.items() if len(case_ids) > 1}
    excluded_rows = sum(len(case_ids) - 1 for case_ids in duplicate_groups.values())
    return kept_rows, {
        "method": "exact",
        "key": "descripcion normalizada + nandina_ref + regimen",
        "rows_before": len(rows),
        "rows_after": len(kept_rows),
        "duplicate_groups": len(duplicate_groups),
        "excluded_rows": excluded_rows,
        "policy": "conservar primera aparicion estable del extractor",
    }

def write_csv(path: Path, rows: list[dict[str, str]], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"El archivo de salida ya existe: {path}. Use --overwrite para reemplazarlo.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_metadata(path: Path, metadata: dict[str, Any], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"El metadata ya existe: {path}. Use --overwrite para reemplazarlo.")
    with path.open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def ensure_outputs_available(output_path: Path, metadata_path: Path, overwrite: bool) -> None:
    existing = [str(path) for path in [output_path, metadata_path] if path.exists()]
    if existing and not overwrite:
        raise FileExistsError("Ya existen salidas: " + ", ".join(existing) + ". Use --overwrite para reemplazarlas.")


def validate_fecha_consulta(value: str) -> str:
    if not DATE_RE.fullmatch(value):
        raise argparse.ArgumentTypeError("Use formato YYYY-MM-DD para --fecha-consulta.")
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise argparse.ArgumentTypeError("La fecha indicada no es valida.") from exc
    return value


def row_counts(rows: list[dict[str, str]]) -> dict[str, int]:
    return {
        "nandina_valida_8": sum(1 for row in rows if re.fullmatch(r"\d{8}", _clean(row.get("nandina_ref")))),
        "descripcion_no_vacia": sum(1 for row in rows if _clean(row.get("descripcion"))),
        "regimen_no_vacio": sum(1 for row in rows if _clean(row.get("regimen"))),
    }


def print_preview(rows: list[dict[str, str]], limit: int) -> None:
    print(f"Preview primeras {min(limit, len(rows))} filas:")
    writer = csv.DictWriter(sys.stdout, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
    writer.writeheader()
    for row in rows[:limit]:
        writer.writerow(row)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Construye data/processed/evalset_v0.1.csv desde un Excel o CSV preparado desde SUNAT."
    )
    parser.add_argument("--input", required=True, type=Path, help="Ruta al archivo .xlsx o .csv de entrada.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Ruta CSV de salida.")
    parser.add_argument("--source-url", default=DEFAULT_SOURCE_URL, help="URL fuente aplicada a todas las filas.")
    parser.add_argument("--fecha-consulta", required=True, type=validate_fecha_consulta, help="Fecha YYYY-MM-DD.")
    parser.add_argument("--origen-caso", default=DEFAULT_ORIGEN_CASO, help="Valor para la columna origen_caso.")
    parser.add_argument("--overwrite", action="store_true", help="Permite sobrescribir output y metadata si existen.")
    parser.add_argument(
        "--format",
        choices=["auto", "table", "sunat-block"],
        default="auto",
        dest="input_format",
        help="Formato de entrada. auto intenta table y luego sunat-block.",
    )
    parser.add_argument("--preview", type=int, default=None, help="Imprime las primeras N filas extraidas sin escribir salidas.")
    parser.add_argument("--dry-run", action="store_true", help="Extrae y valida en memoria sin escribir CSV ni metadata.")
    parser.add_argument("--dedupe", choices=["none", "exact"], default="none", help="Politica de deduplicacion antes de validar/escribir.")
    parser.add_argument("--audit-report-dir", type=Path, default=Path("outputs/audits/evalset_v0.1_duplicates"), help="Ruta al reporte de auditoria usado como evidencia de deduplicacion.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input
    output_path = args.output
    metadata_path = _metadata_path(output_path)
    dry_run = args.dry_run or args.preview is not None

    if not input_path.exists():
        print(f"ERROR: no existe el input: {input_path}", file=sys.stderr)
        return 2
    if not dry_run and input_path.resolve() == output_path.resolve():
        print("ERROR: --input y --output no pueden apuntar al mismo archivo.", file=sys.stderr)
        return 2

    try:
        if not dry_run:
            ensure_outputs_available(output_path, metadata_path, overwrite=args.overwrite)

        result = extract_evalset(
            input_path=input_path,
            input_format=args.input_format,
            source_url=args.source_url,
            fecha_consulta=args.fecha_consulta,
            origen_caso=_clean(args.origen_caso) or DEFAULT_ORIGEN_CASO,
        )
        output_rows = result.rows
        dedupe_stats: dict[str, Any] = {
            "method": "none",
            "key": None,
            "rows_before": len(result.rows),
            "rows_after": len(result.rows),
            "duplicate_groups": 0,
            "excluded_rows": 0,
            "policy": "sin deduplicacion",
        }
        if args.dedupe == "exact":
            output_rows, dedupe_stats = deduplicate_exact(result.rows)

        errors, warnings = validate_evalset(OUTPUT_COLUMNS, output_rows)
        counts = row_counts(output_rows)

        if not dry_run:
            write_csv(output_path, output_rows, overwrite=args.overwrite)
            output_fieldnames, validation_rows = _read_csv(output_path)
            errors, warnings = validate_evalset(output_fieldnames, validation_rows)
            counts = row_counts(validation_rows)
            metadata = {
                "input_path": str(input_path),
                "output_path": str(output_path),
                "metadata_path": str(metadata_path),
                "source_url": args.source_url,
                "fecha_consulta": args.fecha_consulta,
                "input_format_requested": args.input_format,
                "detected_format": result.detected_format,
                "rows_input": result.rows_input,
                "rows_extracted_before_dedupe": len(result.rows),
                "rows_output": len(validation_rows),
                "sha256_input": _sha256(input_path),
                "sha256_output": _sha256(output_path),
                "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "columnas_entrada": result.source_columns,
                "columnas_detectadas": result.detected_columns,
                "reglas_aplicadas": result.rules_applied
                + ["deduplicacion exacta antes de evaluacion" if args.dedupe == "exact" else "sin deduplicacion"]
                + ["validacion final con src.evaluation.validate_dataset.validate_evalset"],
                "deduplicacion": dedupe_stats,
                "audit_report_dir": str(args.audit_report_dir),
                "conteos_calidad": counts,
                "validation_warnings": warnings,
                "validation_errors": errors,
            }
            write_metadata(metadata_path, metadata, overwrite=args.overwrite)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Input: {input_path}")
    print(f"Formato solicitado: {args.input_format}")
    print(f"Formato detectado: {result.detected_format}")
    print(f"Filas entrada: {result.rows_input}")
    print(f"Casos extraidos antes de dedupe: {len(result.rows)}")
    print(f"Casos de salida: {len(output_rows)}")
    if args.dedupe == "exact":
        print(f"Dedupe exact: grupos={dedupe_stats['duplicate_groups']}, excluidos={dedupe_stats['excluded_rows']}")
    print(f"NANDINA valida de 8 digitos: {counts['nandina_valida_8']}")
    print(f"Descripcion no vacia: {counts['descripcion_no_vacia']}")
    print(f"Regimen no vacio: {counts['regimen_no_vacio']}")

    if dry_run:
        print("Modo sin escritura: no se genero CSV ni metadata.")
    else:
        print(f"Output: {output_path}")
        print(f"Metadata: {metadata_path}")

    if args.preview is not None:
        print_preview(output_rows, max(args.preview, 0))

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