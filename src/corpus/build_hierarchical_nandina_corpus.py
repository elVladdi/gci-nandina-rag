from __future__ import annotations

import argparse
import json
import re
import statistics
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_INPUT = Path("data/processed/corpus/nandina/nandina_corpus.jsonl")
DEFAULT_FLAT_CORPUS = Path("data/processed/corpus_rag_v1_index.jsonl")
DEFAULT_OUTPUT = Path("data/processed/corpus_nandina_hierarchical_v0.1.jsonl")
DEFAULT_METADATA = Path("data/processed/corpus_nandina_hierarchical_v0.1_metadata.json")

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
}
HEADER_REPLACEMENTS = [
    re.compile(r"\bC[oó]digo\s+Designaci[oó]n\s+de\s+la\s+Mercanc[ií]a\s+U\.?\s*F\.?\b", re.IGNORECASE),
    re.compile(r"\bC[oó]digo\b", re.IGNORECASE),
    re.compile(r"\bDesignaci[oó]n\s+de\s+la\s+Mercanc[ií]a\b", re.IGNORECASE),
    re.compile(r"\bU\.?\s*F\.?\b", re.IGNORECASE),
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
            rows.append(payload)
    return rows


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _norm(text: object) -> str:
    raw = _clean(text).lower()
    raw = unicodedata.normalize("NFKD", raw)
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch))
    raw = re.sub(r"[^a-z0-9]+", " ", raw)
    return re.sub(r"\s+", " ", raw).strip()


def _clean_description(text: object) -> str:
    value = _clean(text)
    for pattern in HEADER_REPLACEMENTS:
        value = pattern.sub(" ", value)
    value = value.replace("|", " ")
    value = re.sub(r"\s+", " ", value).strip(" -;:")
    return value


def _dedupe_parts(parts: Sequence[str]) -> list[str]:
    seen: set[str] = set()
    deduped: list[str] = []
    for part in parts:
        value = re.sub(r"\s+", " ", _clean(part)).strip(" ;")
        if not value:
            continue
        key = _norm(value)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(value)
    return deduped


def _first_by_code(rows: Sequence[Mapping[str, Any]], level: str) -> dict[str, Mapping[str, Any]]:
    mapping: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if row.get("level") == level:
            code = _clean(row.get("code_digits"))
            mapping.setdefault(code, row)
    return mapping


def _duplicate_conflicts(rows: Sequence[Mapping[str, Any]]) -> int:
    grouped: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in rows:
        grouped[(_clean(row.get("level")), _clean(row.get("code_digits")))].add(_clean(row.get("description")))
    return sum(1 for (level, code), descriptions in grouped.items() if code and level and len(descriptions) > 1)


def _median_text_length(rows: Sequence[Mapping[str, Any]], field: str) -> float:
    lengths = [len(_clean(row.get(field))) for row in rows if _clean(row.get(field))]
    return float(statistics.median(lengths)) if lengths else 0.0


def _report_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _build_text(row: Mapping[str, Any], parent4: Mapping[str, Any] | None, parent6: Mapping[str, Any] | None) -> str:
    code = _clean(row.get("code_digits"))
    section = _clean(row.get("section"))
    section_title = _clean(row.get("section_title"))
    chapter = _clean(row.get("chapter")) or code[:2]
    chapter_title = _clean(row.get("chapter_title"))
    unit = _clean(row.get("unit"))
    desc4 = _clean_description(parent4.get("description")) if parent4 else ""
    desc6 = _clean_description(parent6.get("description")) if parent6 else ""
    desc8 = _clean_description(row.get("description"))
    parts = [
        f"Seccion {section}: {section_title}" if section or section_title else "",
        f"Capitulo {chapter}: {chapter_title}" if chapter or chapter_title else "",
        f"Partida {code[:4]}: {desc4}" if desc4 else "",
        f"Subpartida HS {code[:6]}: {desc6}" if desc6 else "",
        f"NANDINA {code}: {desc8}" if desc8 else "",
        f"Unidad fisica: {unit}" if unit else "",
    ]
    return ". ".join(_dedupe_parts(parts)).strip()


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    input_path = resolve_project_path(args.input)
    output_path = resolve_project_path(args.output)
    metadata_path = resolve_project_path(args.metadata)
    flat_corpus_path = resolve_project_path(args.flat_corpus)

    rows = _read_jsonl(input_path)
    flat_rows = _read_jsonl(flat_corpus_path) if flat_corpus_path.exists() else []
    by4 = _first_by_code(rows, "partida_4d")
    by6 = _first_by_code(rows, "hs_6d")
    nandina8_rows = [row for row in rows if row.get("level") == "nandina_8d"]

    records: list[dict[str, Any]] = []
    missing4 = 0
    missing6 = 0
    generic_leaf = 0
    generic_hierarchical_text = 0
    for row in nandina8_rows:
        code = _clean(row.get("code_digits"))
        if not re.fullmatch(r"\d{8}", code):
            continue
        parent4 = by4.get(code[:4])
        parent6 = by6.get(code[:6])
        if parent4 is None:
            missing4 += 1
        if parent6 is None:
            missing6 += 1
        desc8 = _clean_description(row.get("description"))
        if _norm(desc8.rstrip(".:")) in GENERIC_PHRASES or len(desc8.rstrip(".:")) <= 12:
            generic_leaf += 1
        text = _build_text(row, parent4, parent6)
        if _norm(text.rstrip(".:")) in GENERIC_PHRASES or len(text.rstrip(".:")) <= 12:
            generic_hierarchical_text += 1
        page = row.get("page")
        record = {
            "doc_id": f"NANDINA_{code}",
            "tipo": "nandina_8",
            "codigo": code,
            "titulo": desc8,
            "texto": text,
            "fuente": "NANDINA",
            "version": "hierarchical_v0.1",
            "idioma": "es",
            "pagina_inicio": page,
            "pagina_fin": page,
            "section": _clean(row.get("section")),
            "section_title": _clean(row.get("section_title")),
            "chapter": _clean(row.get("chapter")) or code[:2],
            "chapter_title": _clean(row.get("chapter_title")),
            "partida_4d": code[:4],
            "descripcion_partida_4d": _clean_description(parent4.get("description")) if parent4 else "",
            "hs_6d": code[:6] if parent6 else "",
            "descripcion_hs_6d": _clean_description(parent6.get("description")) if parent6 else "",
            "nandina_8d": code,
            "descripcion_nandina_8d": desc8,
            "unidad_fisica": _clean(row.get("unit")),
            "source_page": page,
            "source_line_no": row.get("line_no_on_page"),
            "source_line_text": _clean(row.get("line_text")),
            "texto_index_jerarquico": text,
            "texto_index": text,
        }
        records.append(record)

    ensure_parent(output_path)
    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=False) + "\n")

    text_lengths = [len(record["texto_index_jerarquico"]) for record in records]
    metadata: dict[str, Any] = {
        "script": "src.corpus.build_hierarchical_nandina_corpus",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "input_path": _report_path(input_path, root),
        "input_sha256": sha256_file(input_path),
        "flat_corpus_path": _report_path(flat_corpus_path, root) if flat_corpus_path.exists() else "",
        "flat_corpus_sha256": sha256_file(flat_corpus_path) if flat_corpus_path.exists() else "",
        "total_nandina8_esperadas": len(nandina8_rows),
        "total_documentos_generados": len(records),
        "cantidad_con_padre_4d": len(records) - missing4,
        "cantidad_con_padre_hs6": len(records) - missing6,
        "cantidad_sin_padre_4d": missing4,
        "cantidad_sin_padre_hs6": missing6,
        "cantidad_sin_padres": sum(
            1
            for record in records
            if not record["descripcion_partida_4d"] and not record["descripcion_hs_6d"]
        ),
        "longitud_mediana_texto_index_jerarquico": float(statistics.median(text_lengths)) if text_lengths else 0.0,
        "longitud_mediana_texto_index_plano_actual": _median_text_length(flat_rows, "texto_index"),
        "cantidad_textos_todavia_genericos": generic_hierarchical_text,
        "cantidad_descripciones_8d_genericas_o_cortas": generic_leaf,
        "campos_usados": [
            "section",
            "section_title",
            "chapter",
            "chapter_title",
            "partida_4d",
            "descripcion_partida_4d",
            "hs_6d",
            "descripcion_hs_6d",
            "nandina_8d",
            "descripcion_nandina_8d",
            "unidad_fisica",
            "page",
            "line_text",
        ],
        "warnings": [
            f"{missing4} NANDINA8 records do not have an explicit 4D parent row.",
            f"{missing6} NANDINA8 records do not have an explicit HS6 parent row.",
            f"{_duplicate_conflicts(rows)} code/level groups have conflicting duplicate descriptions.",
            "HS6 context is nullable because the intermediate JSONL does not represent every HS6 heading as a separate row.",
        ],
        "output_path": _report_path(output_path, root),
        "output_sha256": sha256_file(output_path),
    }
    _write_json(metadata_path, metadata)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build hierarchical NANDINA8 corpus v0.1.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--flat-corpus", type=Path, default=DEFAULT_FLAT_CORPUS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA)
    return parser


def main() -> int:
    metadata = build(build_parser().parse_args())
    print("OK: corpus NANDINA jerarquico construido")
    print(f"Docs generados: {metadata['total_documentos_generados']}")
    print(f"Con padre 4D: {metadata['cantidad_con_padre_4d']}")
    print(f"Con padre HS6: {metadata['cantidad_con_padre_hs6']}")
    print(f"Mediana jerarquica: {metadata['longitud_mediana_texto_index_jerarquico']:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
