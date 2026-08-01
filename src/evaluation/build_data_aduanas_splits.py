from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from src.ingestion.sunat_series_parser import (
        DEFAULT_DUPLICATE_AUDIT,
        DEFAULT_INPUT as DEFAULT_SOURCE_XLSX,
        DEFAULT_LABEL_AUDIT,
        DEFAULT_METADATA as DEFAULT_NORMALIZED_METADATA,
        DEFAULT_OUTPUT_CSV as DEFAULT_NORMALIZED_CSV,
        DEFAULT_OUTPUT_XLSX,
    )
except ImportError:  # Allows direct execution as a script from the repository root.
    sys.path.append(str(Path(__file__).resolve().parents[2]))
    from src.ingestion.sunat_series_parser import (  # type: ignore
        DEFAULT_DUPLICATE_AUDIT,
        DEFAULT_INPUT as DEFAULT_SOURCE_XLSX,
        DEFAULT_LABEL_AUDIT,
        DEFAULT_METADATA as DEFAULT_NORMALIZED_METADATA,
        DEFAULT_OUTPUT_CSV as DEFAULT_NORMALIZED_CSV,
        DEFAULT_OUTPUT_XLSX,
    )


VERSION = "v0.1"
DEFAULT_OUTPUT_DIR = Path("data/processed")
DEFAULT_AUDIT_DIR = Path("outputs/audits/data_aduanas_splits_clase87_v0.1")
SPLIT_FILENAMES = {
    "historico": "data_aduanas_historico_clase87_v0.1.csv",
    "desarrollo": "data_aduanas_devset_clase87_v0.1.csv",
    "evaluacion": "data_aduanas_evalset_clase87_v0.1.csv",
}
METADATA_FILENAME = "data_aduanas_splits_clase87_v0.1_metadata.json"

PRIMARY_COLUMNS = [
    "case_id",
    "split",
    "id_unico",
    "DECLARACION",
    "SERIE",
    "Clase",
    "Partida",
    "Sub Partida",
    "NANDINA",
    "NANDINA ORIGINAL",
    "DESCRIPCION DE PARTIDA ARANCELARIA",
    "DESCRIPCION DE MERCANCIAS 1",
    "DESCRIPCION DE MERCANCIAS 2",
    "DESCRIPCION DE MERCANCIAS 3",
    "DESCRIPCION DE MERCANCIAS 4",
    "DESCRIPCION DE MERCANCIAS 5",
    "DESCRIPCION DE MERCANCIAS CONCATENADA",
]
REQUIRED_SOURCE_COLUMNS = [
    "id_unico",
    "DECLARACION",
    "SERIE",
    "Clase",
    "Partida",
    "Sub Partida",
    "NANDINA",
    "NANDINA ORIGINAL",
    "DESCRIPCION DE PARTIDA ARANCELARIA",
    "DESCRIPCION DE MERCANCIAS CONCATENADA",
]
NANDINA_RE = re.compile(r"^\d{8}$")
CRITICAL_WARNING_PATTERNS = [
    re.compile(r"NANDINA con menos de 8 digitos", re.IGNORECASE),
    re.compile(r"valor multiple para etiqueta '?(DECLARACION|SERIE|NANDINA)'?", re.IGNORECASE),
]


def clean(value: object) -> str:
    if value is None:
        return ""
    text = str(value).replace("\xa0", " ").strip()
    if text.lower() in {"nan", "nat", "none"}:
        return ""
    return re.sub(r"\s+", " ", text)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def ensure_can_write(paths: list[Path], overwrite: bool) -> None:
    existing = [str(path) for path in paths if path.exists()]
    if existing and not overwrite:
        raise FileExistsError("Ya existen salidas: " + ", ".join(existing) + ". Use --overwrite para reemplazarlas.")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"El CSV no contiene encabezados: {path}")
        fieldnames = [clean(field) for field in reader.fieldnames]
        rows = []
        for row in reader:
            rows.append({clean(key): clean(value) for key, value in row.items() if key is not None})
    return fieldnames, rows


def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Ya existe {path}. Use --overwrite para reemplazarlo.")
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, Any], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Ya existe {path}. Use --overwrite para reemplazarlo.")
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def regenerate_normalized_layer(args: argparse.Namespace) -> None:
    command = [
        sys.executable,
        "-m",
        "src.ingestion.sunat_series_parser",
        "--input",
        str(args.source_xlsx),
        "--output-csv",
        str(args.input),
        "--output-xlsx",
        str(args.normalized_xlsx_output),
        "--metadata",
        str(args.normalized_metadata),
        "--label-audit",
        str(args.normalized_label_audit),
        "--duplicate-audit",
        str(args.normalized_duplicate_audit),
    ]
    if args.overwrite:
        command.append("--overwrite")
    subprocess.run(command, cwd=Path.cwd(), check=True)


def missing_required(row: dict[str, str]) -> list[str]:
    missing = []
    for column in REQUIRED_SOURCE_COLUMNS:
        if not clean(row.get(column)):
            missing.append(column)
    return missing


def hierarchy_is_consistent(row: dict[str, str]) -> bool:
    nandina = clean(row.get("NANDINA"))
    return (
        bool(NANDINA_RE.fullmatch(nandina))
        and clean(row.get("Clase")).zfill(2) == nandina[:2]
        and clean(row.get("Partida")).zfill(4) == nandina[:4]
        and clean(row.get("Sub Partida")).zfill(6) == nandina[:6]
    )


def has_critical_warning(row: dict[str, str]) -> bool:
    warnings = clean(row.get("__parse_warnings"))
    return any(pattern.search(warnings) for pattern in CRITICAL_WARNING_PATTERNS)


def payload_for_duplicate(row: dict[str, str], columns: list[str]) -> str:
    payload = {column: row.get(column, "") for column in columns if not column.startswith("__")}
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def classify_rows(
    fieldnames: list[str],
    rows: list[dict[str, str]],
    scope_class: str,
) -> tuple[list[dict[str, str]], dict[str, Any], dict[str, list[dict[str, str]]]]:
    missing_columns = [column for column in REQUIRED_SOURCE_COLUMNS if column not in fieldnames]
    if missing_columns:
        raise ValueError("Faltan columnas obligatorias en la capa normalizada: " + ", ".join(missing_columns))

    scope_rows = [row for row in rows if clean(row.get("Clase")) == scope_class]
    inclusion_ready: list[dict[str, str]] = []
    excluded: dict[str, list[dict[str, str]]] = defaultdict(list)
    exclusion_counts = Counter()

    for row in scope_rows:
        missing = missing_required(row)
        invalid_reasons = []
        if missing:
            invalid_reasons.append("campos_obligatorios")
        if not NANDINA_RE.fullmatch(clean(row.get("NANDINA"))):
            invalid_reasons.append("nandina_invalida")
        if not hierarchy_is_consistent(row):
            invalid_reasons.append("jerarquia_inconsistente")
        if has_critical_warning(row):
            invalid_reasons.append("advertencia_parseo_critica")

        if invalid_reasons:
            reason = "+".join(invalid_reasons)
            tagged = dict(row)
            tagged["exclusion_reason"] = reason
            tagged["missing_required_columns"] = "|".join(missing)
            excluded["quality"].append(tagged)
            for item in invalid_reasons:
                exclusion_counts[item] += 1
            continue
        inclusion_ready.append(row)

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inclusion_ready:
        grouped[clean(row.get("id_unico"))].append(row)

    curated_rows: list[dict[str, str]] = []
    duplicate_audit_rows: list[dict[str, str]] = []
    duplicate_exact_groups = 0
    duplicate_conflict_groups = 0
    duplicate_exact_rows_excluded = 0
    duplicate_conflict_rows_excluded = 0

    for id_unico, members in sorted(grouped.items()):
        payloads = {payload_for_duplicate(row, fieldnames) for row in members}
        if len(members) == 1:
            curated_rows.append(members[0])
            continue

        status = "duplicado_exacto" if len(payloads) == 1 else "conflicto"
        duplicate_audit_rows.append(
            {
                "id_unico": id_unico,
                "total_rows": str(len(members)),
                "unique_payloads": str(len(payloads)),
                "status": status,
                "policy": "conservar_primera_fila" if status == "duplicado_exacto" else "excluir_grupo_completo",
                "excluded_rows": str(len(members) - 1 if status == "duplicado_exacto" else len(members)),
                "nandinas": ";".join(sorted({clean(row.get("NANDINA")) for row in members if clean(row.get("NANDINA"))})),
                "parse_warnings": " || ".join(clean(row.get("__parse_warnings")) for row in members if clean(row.get("__parse_warnings"))),
                "source_rows": ";".join(clean(row.get("__series_row_start")) for row in members),
            }
        )
        if status == "duplicado_exacto":
            duplicate_exact_groups += 1
            duplicate_exact_rows_excluded += len(members) - 1
            curated_rows.append(members[0])
            for row in members[1:]:
                tagged = dict(row)
                tagged["exclusion_reason"] = "id_unico_duplicado_exacto_excedente"
                excluded["duplicates"].append(tagged)
        else:
            duplicate_conflict_groups += 1
            duplicate_conflict_rows_excluded += len(members)
            for row in members:
                tagged = dict(row)
                tagged["exclusion_reason"] = "id_unico_conflictivo"
                excluded["duplicates"].append(tagged)

    stats = {
        "source_rows_total": len(rows),
        "source_rows_scope_class": len(scope_rows),
        "rows_after_inclusion_quality_rules": len(inclusion_ready),
        "rows_curated_after_duplicate_policy": len(curated_rows),
        "excluded_quality_rows": len(excluded["quality"]),
        "excluded_duplicate_rows": len(excluded["duplicates"]),
        "excluded_by_fields_or_quality": dict(sorted(exclusion_counts.items())),
        "duplicate_policy": {
            "key": "id_unico",
            "policy": "Los id_unico duplicados exactos se colapsan conservando la primera aparicion estable; los id_unico conflictivos se excluyen completos.",
            "exact_duplicate_groups": duplicate_exact_groups,
            "exact_duplicate_rows_excluded": duplicate_exact_rows_excluded,
            "conflict_duplicate_groups": duplicate_conflict_groups,
            "conflict_duplicate_rows_excluded": duplicate_conflict_rows_excluded,
        },
        "duplicate_audit_rows": duplicate_audit_rows,
    }
    return curated_rows, stats, excluded


def stratified_take(
    rows: list[dict[str, str]],
    target_size: int,
    rng: random.Random,
) -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, Any]]:
    if target_size <= 0 or not rows:
        return [], rows, {"target_size": target_size, "rule": "tamano_objetivo_cero_o_sin_filas"}
    if target_size >= len(rows):
        return list(rows), [], {"target_size": target_size, "rule": "tamano_objetivo_mayor_o_igual_disponible"}

    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[clean(row.get("NANDINA"))].append(row)
    for members in groups.values():
        members.sort(key=lambda item: clean(item.get("id_unico")))
        rng.shuffle(members)

    quotas: dict[str, int] = {}
    remainders: list[tuple[float, str]] = []
    total = len(rows)
    for nandina, members in groups.items():
        exact = target_size * len(members) / total
        base = int(exact)
        if base == 0 and len(members) > 1 and target_size >= len(groups):
            base = 1
        quotas[nandina] = min(base, len(members))
        remainders.append((exact - int(exact), nandina))

    assigned = sum(quotas.values())
    for _, nandina in sorted(remainders, reverse=True):
        if assigned >= target_size:
            break
        if quotas[nandina] < len(groups[nandina]):
            quotas[nandina] += 1
            assigned += 1

    while assigned > target_size:
        candidates = sorted(
            (nandina for nandina, quota in quotas.items() if quota > 0),
            key=lambda code: (quotas[code], len(groups[code]), code),
        )
        if not candidates:
            break
        quotas[candidates[0]] -= 1
        assigned -= 1

    selected: list[dict[str, str]] = []
    remaining: list[dict[str, str]] = []
    for nandina, members in groups.items():
        quota = quotas[nandina]
        selected.extend(members[:quota])
        remaining.extend(members[quota:])

    selected.sort(key=lambda item: clean(item.get("id_unico")))
    remaining.sort(key=lambda item: clean(item.get("id_unico")))
    stats = {
        "target_size": target_size,
        "actual_size": len(selected),
        "groups_available": len(groups),
        "groups_represented": len({row.get("NANDINA", "") for row in selected}),
        "singleton_groups": sum(1 for members in groups.values() if len(members) == 1),
        "rule": "muestreo estratificado proporcional por NANDINA; los estratos con cuota cero permanecen para particiones posteriores",
    }
    return selected, remaining, stats


def build_splits(
    curated_rows: list[dict[str, str]],
    historical_size: int,
    dev_size: int,
    seed: int,
) -> tuple[dict[str, list[dict[str, str]]], dict[str, Any]]:
    ordered = sorted(curated_rows, key=lambda row: (clean(row.get("NANDINA")), clean(row.get("id_unico"))))
    rng = random.Random(seed)
    historical, rest, historical_stats = stratified_take(ordered, historical_size, rng)
    dev, eval_rows, dev_stats = stratified_take(rest, dev_size, rng)
    splits = {
        "historico": historical,
        "desarrollo": dev,
        "evaluacion": eval_rows,
    }
    stats = {
        "seed": seed,
        "historical": historical_stats,
        "dev": dev_stats,
        "eval_rule": "remanente curado despues de historico y desarrollo",
    }
    return splits, stats


def output_columns(source_columns: list[str]) -> list[str]:
    columns = list(PRIMARY_COLUMNS)
    for column in source_columns:
        if column not in columns:
            columns.append(column)
    return columns


def add_split_columns(splits: dict[str, list[dict[str, str]]], columns: list[str]) -> dict[str, list[dict[str, str]]]:
    split_prefix = {
        "historico": "DA-HIST",
        "desarrollo": "DA-DEV",
        "evaluacion": "DA-EVAL",
    }
    prepared: dict[str, list[dict[str, str]]] = {}
    for split_name, rows in splits.items():
        prepared_rows = []
        for index, row in enumerate(sorted(rows, key=lambda item: clean(item.get("id_unico"))), start=1):
            output_row = {column: row.get(column, "") for column in columns}
            output_row["case_id"] = f"{split_prefix[split_name]}-{index:05d}"
            output_row["split"] = split_name
            prepared_rows.append(output_row)
        prepared[split_name] = prepared_rows
    return prepared


def validate_splits(splits: dict[str, list[dict[str, str]]], columns: list[str]) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    stats: dict[str, Any] = {"splits": {}}
    seen_global: dict[str, str] = {}

    for split_name, rows in splits.items():
        ids = [clean(row.get("id_unico")) for row in rows]
        duplicate_ids = sorted(id_unico for id_unico, count in Counter(ids).items() if id_unico and count > 1)
        if duplicate_ids:
            errors.append(f"{split_name}: id_unico repetidos: " + ", ".join(duplicate_ids[:20]))
        for id_unico in ids:
            if not id_unico:
                errors.append(f"{split_name}: id_unico vacio")
                continue
            previous = seen_global.get(id_unico)
            if previous and previous != split_name:
                errors.append(f"id_unico compartido entre {previous} y {split_name}: {id_unico}")
            seen_global[id_unico] = split_name

        for row_number, row in enumerate(rows, start=2):
            if list(row.keys()) != columns:
                errors.append(f"{split_name}: columnas u orden distintos en fila logica {row_number}")
                break
            if clean(row.get("Clase")) != "87":
                errors.append(f"{split_name}: Clase distinta de 87 en {row.get('case_id')}")
            if not NANDINA_RE.fullmatch(clean(row.get("NANDINA"))):
                errors.append(f"{split_name}: NANDINA invalida en {row.get('case_id')}: {row.get('NANDINA')!r}")
            if not hierarchy_is_consistent(row):
                errors.append(f"{split_name}: jerarquia inconsistente en {row.get('case_id')}")
            if not clean(row.get("DESCRIPCION DE MERCANCIAS CONCATENADA")):
                errors.append(f"{split_name}: descripcion concatenada vacia en {row.get('case_id')}")

        stats["splits"][split_name] = {
            "rows": len(rows),
            "unique_id_unico": len(set(ids)),
            "distinct_nandina": len({clean(row.get("NANDINA")) for row in rows if clean(row.get("NANDINA"))}),
            "distribution_by_nandina": dict(sorted(Counter(clean(row.get("NANDINA")) for row in rows).items())),
        }

    stats["global"] = {
        "rows_total": sum(len(rows) for rows in splits.values()),
        "unique_id_unico_total": len(seen_global),
        "distinct_nandina_total": len({clean(row.get("NANDINA")) for rows in splits.values() for row in rows if clean(row.get("NANDINA"))}),
        "nandina_coverage_by_split": {
            split_name: sorted({clean(row.get("NANDINA")) for row in rows if clean(row.get("NANDINA"))})
            for split_name, rows in splits.items()
        },
    }
    return errors, stats


def distribution_rows(splits: dict[str, list[dict[str, str]]]) -> list[dict[str, str]]:
    all_nandinas = sorted({clean(row.get("NANDINA")) for rows in splits.values() for row in rows if clean(row.get("NANDINA"))})
    rows = []
    for nandina in all_nandinas:
        item = {"NANDINA": nandina}
        for split_name, split_rows in splits.items():
            item[split_name] = str(sum(1 for row in split_rows if clean(row.get("NANDINA")) == nandina))
        rows.append(item)
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Construye particiones historico/desarrollo/evaluacion clase 87 desde data_aduanas normalizado."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_NORMALIZED_CSV, help="CSV normalizado de data_aduanas.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directorio de salidas procesadas.")
    parser.add_argument("--scope-class", default="87", help="Clase NANDINA a conservar.")
    parser.add_argument("--historical-size", type=int, default=3000, help="Tamano objetivo del historico.")
    parser.add_argument("--dev-size", type=int, default=100, help="Tamano objetivo del desarrollo.")
    parser.add_argument("--seed", type=int, default=2026, help="Semilla deterministica de split.")
    parser.add_argument("--overwrite", action="store_true", help="Permite sobrescribir salidas existentes.")
    parser.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT_DIR, help="Directorio de auditorias regenerables.")
    parser.add_argument("--regenerate-normalized", action="store_true", help="Regenera la capa normalizada desde el Excel fuente antes del split.")
    parser.add_argument("--source-xlsx", type=Path, default=DEFAULT_SOURCE_XLSX, help="Excel local fuente data_aduanas.")
    parser.add_argument("--normalized-xlsx-output", type=Path, default=DEFAULT_OUTPUT_XLSX, help="XLSX normalizado opcional al regenerar.")
    parser.add_argument("--normalized-metadata", type=Path, default=DEFAULT_NORMALIZED_METADATA, help="Metadata normalizada al regenerar.")
    parser.add_argument("--normalized-label-audit", type=Path, default=DEFAULT_LABEL_AUDIT, help="Auditoria de etiquetas al regenerar.")
    parser.add_argument("--normalized-duplicate-audit", type=Path, default=DEFAULT_DUPLICATE_AUDIT, help="Auditoria de duplicados al regenerar.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.scope_class != "87":
        print("ADVERTENCIA: este protocolo fue documentado para Clase = 87; se ejecutara el valor solicitado.")

    try:
        if args.regenerate_normalized:
            regenerate_normalized_layer(args)
        if not args.input.exists():
            raise FileNotFoundError(f"No existe el CSV normalizado: {args.input}")

        output_paths = [args.output_dir / filename for filename in SPLIT_FILENAMES.values()]
        metadata_path = args.output_dir / METADATA_FILENAME
        ensure_can_write([*output_paths, metadata_path], overwrite=args.overwrite)

        fieldnames, source_rows = read_csv(args.input)
        curated_rows, curation_stats, excluded = classify_rows(fieldnames, source_rows, clean(args.scope_class))
        split_rows, split_sampling_stats = build_splits(
            curated_rows=curated_rows,
            historical_size=args.historical_size,
            dev_size=args.dev_size,
            seed=args.seed,
        )
        columns = output_columns(fieldnames)
        prepared_splits = add_split_columns(split_rows, columns)
        validation_errors, validation_stats = validate_splits(prepared_splits, columns)
        if validation_errors:
            raise ValueError("Validacion fallida: " + " | ".join(validation_errors[:20]))

        for split_name, rows in prepared_splits.items():
            write_csv(args.output_dir / SPLIT_FILENAMES[split_name], columns, rows, overwrite=args.overwrite)

        audit_columns = list(fieldnames) + ["exclusion_reason", "missing_required_columns"]
        write_csv(args.audit_dir / "excluded_quality_rows.csv", audit_columns, excluded["quality"], overwrite=args.overwrite)
        write_csv(args.audit_dir / "excluded_duplicate_rows.csv", audit_columns, excluded["duplicates"], overwrite=args.overwrite)
        write_csv(
            args.audit_dir / "id_unico_duplicate_policy.csv",
            ["id_unico", "total_rows", "unique_payloads", "status", "policy", "excluded_rows", "nandinas", "parse_warnings", "source_rows"],
            curation_stats["duplicate_audit_rows"],
            overwrite=args.overwrite,
        )
        write_csv(
            args.audit_dir / "nandina_distribution_by_split.csv",
            ["NANDINA", "historico", "desarrollo", "evaluacion"],
            distribution_rows(prepared_splits),
            overwrite=args.overwrite,
        )

        metadata = {
            "dataset_name": "data_aduanas_splits_clase87_v0.1",
            "version": VERSION,
            "methodological_source_name": "data_aduanas",
            "scope_class": clean(args.scope_class),
            "input_path": str(args.input),
            "input_sha256": sha256_file(args.input),
            "output_dir": str(args.output_dir),
            "audit_dir": str(args.audit_dir),
            "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "parameters": {
                "historical_size": args.historical_size,
                "dev_size": args.dev_size,
                "seed": args.seed,
                "overwrite": args.overwrite,
                "regenerate_normalized": args.regenerate_normalized,
            },
            "outputs": {
                split_name: {
                    "path": str(args.output_dir / filename),
                    "sha256": sha256_file(args.output_dir / filename),
                }
                for split_name, filename in SPLIT_FILENAMES.items()
            },
            "columns": columns,
            "primary_columns": PRIMARY_COLUMNS,
            "curation": {key: value for key, value in curation_stats.items() if key != "duplicate_audit_rows"},
            "sampling": split_sampling_stats,
            "validation": {
                "errors": validation_errors,
                "stats": validation_stats,
                "rules": [
                    "tres particiones con columnas identicas y mismo orden",
                    "sin id_unico repetidos dentro de cada particion",
                    "sin id_unico compartidos entre particiones",
                    "todas las filas con Clase igual al alcance configurado",
                    "NANDINA de 8 digitos",
                    "Clase, Partida y Sub Partida consistentes con NANDINA",
                    "DESCRIPCION DE MERCANCIAS CONCATENADA no vacia",
                ],
            },
            "audit_outputs": {
                "excluded_quality_rows": str(args.audit_dir / "excluded_quality_rows.csv"),
                "excluded_duplicate_rows": str(args.audit_dir / "excluded_duplicate_rows.csv"),
                "id_unico_duplicate_policy": str(args.audit_dir / "id_unico_duplicate_policy.csv"),
                "nandina_distribution_by_split": str(args.audit_dir / "nandina_distribution_by_split.csv"),
            },
            "notes": [
                "Esta fase reemplaza metodologicamente el uso futuro principal del evalset_v0.1 anterior, sin borrarlo ni modificarlo.",
                "No se deduplica por descripcion + NANDINA; la llave de trazabilidad primaria es id_unico.",
                "Los CSV finales se consideran artefactos congelados de Fase 3 actualizada y requieren git add explicito porque data/processed esta ignorado por defecto.",
                "Las auditorias bajo outputs/audits son regenerables y permanecen ignoradas/locales.",
            ],
        }
        write_json(metadata_path, metadata, overwrite=args.overwrite)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print("Resultado: OK")
    print(f"Fuente clase {args.scope_class}: {curation_stats['source_rows_scope_class']}")
    print(f"Curadas finales: {curation_stats['rows_curated_after_duplicate_policy']}")
    print(f"Excluidas por calidad/campos: {curation_stats['excluded_quality_rows']}")
    print(f"Excluidas por duplicados: {curation_stats['excluded_duplicate_rows']}")
    for split_name, rows in prepared_splits.items():
        nandinas = {clean(row.get('NANDINA')) for row in rows if clean(row.get('NANDINA'))}
        print(f"{split_name}: {len(rows)} filas, {len(nandinas)} NANDINAS")
    print(f"Metadata: {metadata_path}")
    print(f"Auditorias: {args.audit_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
