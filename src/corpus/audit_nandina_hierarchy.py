from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_INPUT = Path("data/processed/corpus/nandina/nandina_corpus.jsonl")
DEFAULT_OUTPUT_DIR = Path("outputs/corpus/auditoria_nandina_jerarquica_v0.1")
DEFAULT_DOC = Path("docs/auditoria_corpus_nandina_jerarquico_v0.1.md")

GENERIC_PHRASES = {
    "los demas",
    "las demas",
    "los dems",
    "las dems",
    "demas",
    "solido",
    "liquido",
    "ruedas",
    "partes",
    "otros",
    "otras",
    "los otros",
    "las otras",
}
HEADER_PATTERNS = [
    re.compile(r"\bc[oó]digo\b", flags=re.IGNORECASE),
    re.compile(r"\bdesignaci[oó]n\s+de\s+la\s+mercanc[ií]a\b", flags=re.IGNORECASE),
    re.compile(r"\bu\.?\s*f\.?\b", flags=re.IGNORECASE),
]


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {line_number}") from exc
            if not isinstance(payload, dict):
                raise ValueError(f"Expected JSON object in {path} at line {line_number}")
            payload["_line_number"] = line_number
            rows.append(payload)
    return rows


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _norm(text: object) -> str:
    raw = _clean(text).lower()
    raw = unicodedata.normalize("NFKD", raw)
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch))
    raw = re.sub(r"[^a-z0-9]+", " ", raw)
    return re.sub(r"\s+", " ", raw).strip()


def _has_header_contamination(text: object) -> bool:
    value = _clean(text)
    return any(pattern.search(value) for pattern in HEADER_PATTERNS)


def _is_short_description(text: object) -> bool:
    return len(_clean(text).rstrip(".:")) <= 12


def _is_generic_description(text: object, frequent_short: set[str]) -> bool:
    normalized = _norm(_clean(text).rstrip(".:"))
    return normalized in GENERIC_PHRASES or normalized in frequent_short or _is_short_description(text)


def _first_by_code(rows: Sequence[Mapping[str, Any]], level: str) -> dict[str, Mapping[str, Any]]:
    mapping: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if row.get("level") == level:
            code = _clean(row.get("code_digits"))
            mapping.setdefault(code, row)
    return mapping


def _conflicting_duplicates(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(_clean(row.get("level")), _clean(row.get("code_digits")))].append(row)
    conflicts: list[dict[str, Any]] = []
    for (level, code), group in sorted(grouped.items()):
        descriptions = sorted({_clean(item.get("description")) for item in group})
        if code and len(group) > 1 and len(descriptions) > 1:
            conflicts.append(
                {
                    "level": level,
                    "code": code,
                    "records": len(group),
                    "distinct_descriptions": len(descriptions),
                    "sample_descriptions": descriptions[:5],
                }
            )
    return conflicts


def _out_of_order_examples(rows: Sequence[Mapping[str, Any]], limit: int = 25) -> list[dict[str, Any]]:
    examples: list[dict[str, Any]] = []
    previous_code = ""
    previous_line = 0
    previous_level = ""
    for row in rows:
        code = _clean(row.get("code_digits"))
        if code and previous_code and code < previous_code:
            examples.append(
                {
                    "previous_line": previous_line,
                    "previous_code": previous_code,
                    "previous_level": previous_level,
                    "line_number": row.get("_line_number"),
                    "code": code,
                    "level": row.get("level"),
                }
            )
            if len(examples) >= limit:
                break
        if code:
            previous_code = code
            previous_line = int(row.get("_line_number") or 0)
            previous_level = _clean(row.get("level"))
    return examples


def _report_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _summary_markdown(summary: Mapping[str, Any], examples: Sequence[Mapping[str, Any]]) -> str:
    counts = summary["counts"]
    hierarchy = summary["hierarchy"]
    generic = summary["generic_descriptions"]
    lines = [
        "# Auditoria corpus NANDINA jerarquico v0.1",
        "",
        "## Objetivo",
        "",
        "Auditar si `data/processed/corpus/nandina/nandina_corpus.jsonl` permite construir un corpus NANDINA8 autocontenido con contexto jerarquico 4D/6D/8D, sin modificar el corpus plano ni el indice BM25 vigente.",
        "",
        "## Archivo auditado",
        "",
        f"- Input: `{summary['input']['path']}`.",
        f"- SHA256: `{summary['input']['sha256']}`.",
        "",
        "## Conteos",
        "",
        f"- Total de registros: {counts['total_records']}.",
        f"- `partida_4d`: {counts['by_level'].get('partida_4d', 0)}.",
        f"- `hs_6d`: {counts['by_level'].get('hs_6d', 0)}.",
        f"- `nandina_8d`: {counts['by_level'].get('nandina_8d', 0)}.",
        f"- Descripciones vacias: {counts['empty_descriptions']}.",
        f"- Descripciones muy cortas: {counts['short_descriptions']}.",
        "",
        "## Problemas detectados",
        "",
        f"- NANDINA8 sin padre 4D: {hierarchy['nandina8_missing_parent_4d']}.",
        f"- NANDINA8 sin padre HS6 explicito: {hierarchy['nandina8_missing_parent_hs6']}.",
        f"- Padres duplicados conflictivos: {hierarchy['conflicting_parent_duplicates']}.",
        f"- Saltos de orden detectados: {hierarchy['out_of_order_examples_count']} ejemplos muestreados.",
        f"- Descripciones con posible encabezado contaminante: {counts['descriptions_with_header_contamination']}.",
        f"- Descripciones genericas o muy cortas listadas: {generic['rows_flagged']}.",
        "",
        "## Evidencia de jerarquia",
        "",
        "El corpus trae `section`, `section_title`, `chapter` y `chapter_title` en los registros. La relacion 8D -> 4D se reconstruye por prefijo en la mayoria de los casos. La relacion 8D -> HS6 solo existe cuando hay un registro `hs_6d` con el mismo prefijo de seis digitos; muchos codigos 8D dependen directamente de una partida 4D o de subtitulos que quedaron embebidos en la descripcion 4D.",
        "",
        "## Ejemplos positivos",
        "",
        "| NANDINA8 | Partida 4D | HS6 | Descripcion 8D | Contexto 4D |",
        "|---|---|---|---|---|",
    ]
    for row in examples[:10]:
        lines.append(
            f"| {row.get('nandina_8d', '')} | {row.get('parent_4d', '')} | {row.get('parent_hs6', '')} | {row.get('description_8d', '')} | {row.get('description_4d', '')} |"
        )
    lines.extend(
        [
            "",
            "## Decision metodologica",
            "",
            "Si es posible construir una primera version del corpus jerarquico desde este JSONL. La construccion debe conservar advertencias: los padres HS6 faltan con frecuencia y algunas descripciones 4D tienen texto contaminado por encabezados o notas de extraccion. No hace falta volver al PDF/notebook para una v0.1 de ranking inicial, pero si conviene hacerlo despues si se busca una jerarquia HS6 completa y limpia.",
            "",
            "## Archivos de auditoria",
            "",
            f"- `{summary['output']['audit_summary_json']}`.",
            f"- `{summary['output']['missing_parents_csv']}`.",
            f"- `{summary['output']['generic_descriptions_csv']}`.",
            f"- `{summary['output']['hierarchy_examples_csv']}`.",
            "",
        ]
    )
    return "\n".join(lines)


def run(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    input_path = resolve_project_path(args.input)
    output_dir = resolve_project_path(args.output_dir)
    doc_path = resolve_project_path(args.doc)

    rows = _read_jsonl(input_path)
    levels = Counter(_clean(row.get("level")) for row in rows)
    desc_counter = Counter(_norm(row.get("description")) for row in rows if _clean(row.get("description")))
    frequent_short = {
        desc for desc, count in desc_counter.items() if count >= args.frequent_threshold and len(desc) <= 30
    }

    by4 = _first_by_code(rows, "partida_4d")
    by6 = _first_by_code(rows, "hs_6d")
    nandina8 = [row for row in rows if row.get("level") == "nandina_8d"]

    missing_rows: list[dict[str, Any]] = []
    example_rows: list[dict[str, Any]] = []
    for row in nandina8:
        code = _clean(row.get("code_digits"))
        parent4 = by4.get(code[:4])
        parent6 = by6.get(code[:6])
        missing4 = parent4 is None
        missing6 = parent6 is None
        if missing4 or missing6:
            missing_rows.append(
                {
                    "nandina_8d": code,
                    "description_8d": _clean(row.get("description")),
                    "missing_parent_4d": int(missing4),
                    "missing_parent_hs6": int(missing6),
                    "expected_parent_4d": code[:4],
                    "expected_parent_hs6": code[:6],
                    "section": _clean(row.get("section")),
                    "chapter": _clean(row.get("chapter")),
                    "page": row.get("page", ""),
                    "line_number": row.get("_line_number", ""),
                }
            )
        if parent4 is not None and (parent6 is not None or len(example_rows) < 50):
            example_rows.append(
                {
                    "nandina_8d": code,
                    "description_8d": _clean(row.get("description")),
                    "parent_4d": _clean(parent4.get("code_digits")) if parent4 else "",
                    "description_4d": _clean(parent4.get("description")) if parent4 else "",
                    "parent_hs6": _clean(parent6.get("code_digits")) if parent6 else "",
                    "description_hs6": _clean(parent6.get("description")) if parent6 else "",
                    "section": _clean(row.get("section")),
                    "section_title": _clean(row.get("section_title")),
                    "chapter": _clean(row.get("chapter")),
                    "chapter_title": _clean(row.get("chapter_title")),
                    "page": row.get("page", ""),
                }
            )

    generic_rows: list[dict[str, Any]] = []
    for row in rows:
        description = _clean(row.get("description"))
        normalized = _norm(description.rstrip(".:"))
        if _is_generic_description(description, frequent_short):
            generic_rows.append(
                {
                    "level": _clean(row.get("level")),
                    "code_digits": _clean(row.get("code_digits")),
                    "description": description,
                    "normalized_description": normalized,
                    "description_frequency": desc_counter.get(normalized, 0),
                    "is_known_generic": int(normalized in GENERIC_PHRASES),
                    "is_short": int(_is_short_description(description)),
                    "section": _clean(row.get("section")),
                    "chapter": _clean(row.get("chapter")),
                    "page": row.get("page", ""),
                    "line_number": row.get("_line_number", ""),
                }
            )

    conflicts = _conflicting_duplicates(rows)
    out_of_order = _out_of_order_examples(rows)
    contaminated = [
        row for row in rows if _has_header_contamination(row.get("description"))
    ]

    summary: dict[str, Any] = {
        "script": "src.corpus.audit_nandina_hierarchy",
        "execution": {"datetime_utc": datetime.now(timezone.utc).isoformat()},
        "input": {"path": _report_path(input_path, root), "sha256": sha256_file(input_path)},
        "counts": {
            "total_records": len(rows),
            "by_level": dict(sorted(levels.items())),
            "partida_4d": levels.get("partida_4d", 0),
            "hs_6d": levels.get("hs_6d", 0),
            "nandina_8d": levels.get("nandina_8d", 0),
            "empty_descriptions": sum(1 for row in rows if not _clean(row.get("description"))),
            "short_descriptions": sum(1 for row in rows if _is_short_description(row.get("description"))),
            "descriptions_with_header_contamination": len(contaminated),
        },
        "generic_descriptions": {
            "known_phrase_counts": {
                phrase: sum(1 for row in rows if _norm(_clean(row.get("description")).rstrip(".:")) == phrase)
                for phrase in sorted(GENERIC_PHRASES)
            },
            "frequent_short_descriptions": dict(
                sorted(
                    ((desc, desc_counter[desc]) for desc in frequent_short),
                    key=lambda item: (-item[1], item[0]),
                )[:50]
            ),
            "rows_flagged": len(generic_rows),
        },
        "hierarchy": {
            "nandina8_total": len(nandina8),
            "nandina8_with_parent_4d": len(nandina8) - sum(1 for row in missing_rows if row["missing_parent_4d"]),
            "nandina8_with_parent_hs6": len(nandina8) - sum(1 for row in missing_rows if row["missing_parent_hs6"]),
            "nandina8_missing_parent_4d": sum(1 for row in missing_rows if row["missing_parent_4d"]),
            "nandina8_missing_parent_hs6": sum(1 for row in missing_rows if row["missing_parent_hs6"]),
            "conflicting_parent_duplicates": len(conflicts),
            "conflicting_parent_duplicate_examples": conflicts[:20],
            "out_of_order_examples_count": len(out_of_order),
            "out_of_order_examples": out_of_order,
            "contaminated_parent_examples": [
                {
                    "level": row.get("level"),
                    "code_digits": row.get("code_digits"),
                    "description": row.get("description"),
                    "page": row.get("page"),
                }
                for row in contaminated[:20]
            ],
        },
        "decision": {
            "can_build_from_jsonl": True,
            "rationale": "The JSONL contains NANDINA8 records plus section/chapter metadata and enough 4D parents by prefix for a first hierarchical BM25 corpus. HS6 coverage is incomplete and must be represented as nullable context.",
        },
        "output": {
            "audit_summary_json": _report_path(output_dir / "audit_summary.json", root),
            "audit_summary_md": _report_path(output_dir / "audit_summary.md", root),
            "missing_parents_csv": _report_path(output_dir / "missing_parents.csv", root),
            "generic_descriptions_csv": _report_path(output_dir / "generic_descriptions.csv", root),
            "hierarchy_examples_csv": _report_path(output_dir / "hierarchy_examples.csv", root),
            "doc_md": _report_path(doc_path, root),
        },
    }

    _write_json(output_dir / "audit_summary.json", summary)
    ensure_parent(output_dir / "audit_summary.md")
    (output_dir / "audit_summary.md").write_text(_summary_markdown(summary, example_rows), encoding="utf-8")
    _write_csv(
        output_dir / "missing_parents.csv",
        missing_rows,
        [
            "nandina_8d",
            "description_8d",
            "missing_parent_4d",
            "missing_parent_hs6",
            "expected_parent_4d",
            "expected_parent_hs6",
            "section",
            "chapter",
            "page",
            "line_number",
        ],
    )
    _write_csv(
        output_dir / "generic_descriptions.csv",
        generic_rows,
        [
            "level",
            "code_digits",
            "description",
            "normalized_description",
            "description_frequency",
            "is_known_generic",
            "is_short",
            "section",
            "chapter",
            "page",
            "line_number",
        ],
    )
    _write_csv(
        output_dir / "hierarchy_examples.csv",
        example_rows,
        [
            "nandina_8d",
            "description_8d",
            "parent_4d",
            "description_4d",
            "parent_hs6",
            "description_hs6",
            "section",
            "section_title",
            "chapter",
            "chapter_title",
            "page",
        ],
    )
    ensure_parent(doc_path)
    doc_path.write_text(_summary_markdown(summary, example_rows), encoding="utf-8")
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit the intermediate NANDINA JSONL hierarchy.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--doc", type=Path, default=DEFAULT_DOC)
    parser.add_argument("--frequent-threshold", type=int, default=10)
    return parser


def main() -> int:
    summary = run(build_parser().parse_args())
    print("OK: auditoria NANDINA jerarquica completada")
    print(f"Registros: {summary['counts']['total_records']}")
    print(f"NANDINA8: {summary['hierarchy']['nandina8_total']}")
    print(f"Sin padre 4D: {summary['hierarchy']['nandina8_missing_parent_4d']}")
    print(f"Sin padre HS6: {summary['hierarchy']['nandina8_missing_parent_hs6']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
