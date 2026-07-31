from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from ..bm25_index import sha256_file
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_SOURCE = Path("data/processed/corpus/nandina/nandina_corpus.jsonl")
DEFAULT_HIERARCHICAL_CORPUS = Path("data/processed/corpus_nandina_hierarchical_v0.1.jsonl")
DEFAULT_OUTPUT_DIR = Path("data/processed/corpus_levels")
VERSION = "v0.1"

LEVEL_OUTPUTS = {
    "hs2": "hs2_corpus_v0.1.jsonl",
    "hs4": "hs4_corpus_v0.1.jsonl",
    "hs6": "hs6_corpus_v0.1.jsonl",
    "nandina8": "nandina8_corpus_v0.1.jsonl",
}

LEVEL_ALIASES = {
    "partida_4d": "hs4",
    "hs_6d": "hs6",
    "nandina_8d": "nandina8",
}

HEADER_PATTERNS = [
    re.compile(r"\bC[o\u00f3]digo\s+Designaci[o\u00f3]n\s+de\s+la\s+Mercanc[i\u00ed]a\s+U\.?\s*F\.?\b", re.IGNORECASE),
    re.compile(r"\bC[o\u00f3]digo\b", re.IGNORECASE),
    re.compile(r"\bDesignaci[o\u00f3]n\s+de\s+la\s+Mercanc[i\u00ed]a\b", re.IGNORECASE),
    re.compile(r"\bU\.?\s*F\.?\b", re.IGNORECASE),
]

def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _clean_description(value: object) -> str:
    text = _clean(value)
    for pattern in HEADER_PATTERNS:
        text = pattern.sub(" ", text)
    text = text.replace("|", " ")
    text = re.sub(r"\s+", " ", text).strip(" -;:")
    return text


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


def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=False) + "\n")


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _dedupe_parts(parts: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for part in parts:
        value = re.sub(r"\s+", " ", _clean(part)).strip(" ;.")
        if not value:
            continue
        key = value.casefold()
        if key in seen:
            continue
        seen.add(key)
        output.append(value)
    return output


def _text(parts: Iterable[str]) -> str:
    return ". ".join(_dedupe_parts(parts)).strip()


def _first_by_code(rows: Sequence[Mapping[str, Any]], level: str) -> dict[str, Mapping[str, Any]]:
    by_code: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if row.get("level") != level:
            continue
        code = _clean(row.get("code_digits"))
        if code and code not in by_code:
            by_code[code] = row
    return by_code


def _chapter_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    chapters: dict[str, dict[str, Any]] = {}
    for row in rows:
        chapter = _clean(row.get("chapter"))
        title = _clean(row.get("chapter_title"))
        if not re.fullmatch(r"\d{2}", chapter) or not title:
            continue
        if chapter in chapters:
            continue
        section = _clean(row.get("section"))
        section_title = _clean(row.get("section_title"))
        text = _text(
            [
                f"Seccion: {section_title}" if section_title else "",
                f"Capitulo: {title}",
            ]
        )
        chapters[chapter] = {
            "doc_id": f"HS2_{chapter}",
            "nivel": "hs2",
            "codigo": chapter,
            "descripcion": title,
            "texto_padre": f"Seccion {section}: {section_title}".strip() if section or section_title else "",
            "texto_index": text,
            "fuente": "NANDINA",
            "version": VERSION,
            "metadata": {
                "source_level": "chapter",
                "section": section,
                "section_title": section_title,
                "chapter": chapter,
                "chapter_title": title,
                "source_page": row.get("page"),
                "source_line_no": row.get("line_no_on_page"),
            },
        }
    return [chapters[code] for code in sorted(chapters)]


def _hs4_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for code, row in sorted(_first_by_code(rows, "partida_4d").items()):
        if not re.fullmatch(r"\d{4}", code):
            continue
        description = _clean_description(row.get("description"))
        chapter_title = _clean(row.get("chapter_title"))
        section_title = _clean(row.get("section_title"))
        parent_text = _text(
            [
                f"Seccion: {section_title}" if section_title else "",
                f"Capitulo: {chapter_title}" if chapter_title else "",
            ]
        )
        records.append(
            {
                "doc_id": f"HS4_{code}",
                "nivel": "hs4",
                "codigo": code,
                "descripcion": description,
                "texto_padre": parent_text,
                "texto_index": _text([parent_text, f"Partida: {description}" if description else ""]),
                "fuente": "NANDINA",
                "version": VERSION,
                "metadata": {
                    "source_level": row.get("level"),
                    "code_raw": row.get("code_raw"),
                    "section": _clean(row.get("section")),
                    "section_title": section_title,
                    "chapter": code[:2],
                    "chapter_title": chapter_title,
                    "source_page": row.get("page"),
                    "source_line_no": row.get("line_no_on_page"),
                    "source_line_text": _clean(row.get("line_text")),
                },
            }
        )
    return records


def _hs6_rows(rows: Sequence[Mapping[str, Any]], by4: Mapping[str, Mapping[str, Any]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for code, row in sorted(_first_by_code(rows, "hs_6d").items()):
        if not re.fullmatch(r"\d{6}", code):
            continue
        description = _clean_description(row.get("description"))
        parent4 = by4.get(code[:4])
        parent4_description = _clean_description(parent4.get("description")) if parent4 else ""
        chapter_title = _clean(row.get("chapter_title"))
        section_title = _clean(row.get("section_title"))
        parent_text = _text(
            [
                f"Seccion: {section_title}" if section_title else "",
                f"Capitulo: {chapter_title}" if chapter_title else "",
                f"Partida: {parent4_description}" if parent4_description else "",
            ]
        )
        records.append(
            {
                "doc_id": f"HS6_{code}",
                "nivel": "hs6",
                "codigo": code,
                "descripcion": description,
                "texto_padre": parent_text,
                "texto_index": _text([parent_text, f"Subpartida HS: {description}" if description else ""]),
                "fuente": "NANDINA",
                "version": VERSION,
                "metadata": {
                    "source_level": row.get("level"),
                    "code_raw": row.get("code_raw"),
                    "section": _clean(row.get("section")),
                    "section_title": section_title,
                    "chapter": code[:2],
                    "chapter_title": chapter_title,
                    "partida_4d": code[:4],
                    "descripcion_partida_4d": parent4_description,
                    "source_page": row.get("page"),
                    "source_line_no": row.get("line_no_on_page"),
                    "source_line_text": _clean(row.get("line_text")),
                },
            }
        )
    return records


def _nandina8_rows(
    rows: Sequence[Mapping[str, Any]],
    by4: Mapping[str, Mapping[str, Any]],
    by6: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for code, row in sorted(_first_by_code(rows, "nandina_8d").items()):
        if not re.fullmatch(r"\d{8}", code):
            continue
        description = _clean_description(row.get("description"))
        parent4 = by4.get(code[:4])
        parent6 = by6.get(code[:6])
        parent4_description = _clean_description(parent4.get("description")) if parent4 else ""
        parent6_description = _clean_description(parent6.get("description")) if parent6 else ""
        chapter_title = _clean(row.get("chapter_title"))
        section_title = _clean(row.get("section_title"))
        parent_text = _text(
            [
                f"Seccion: {section_title}" if section_title else "",
                f"Capitulo: {chapter_title}" if chapter_title else "",
                f"Partida: {parent4_description}" if parent4_description else "",
                f"Subpartida HS: {parent6_description}" if parent6_description else "",
            ]
        )
        unit = _clean(row.get("unit"))
        records.append(
            {
                "doc_id": f"NANDINA8_{code}",
                "nivel": "nandina8",
                "codigo": code,
                "descripcion": description,
                "texto_padre": parent_text,
                "texto_index": _text(
                    [
                        parent_text,
                        f"NANDINA: {description}" if description else "",
                        f"Unidad fisica: {unit}" if unit else "",
                    ]
                ),
                "fuente": "NANDINA",
                "version": VERSION,
                "metadata": {
                    "source_level": row.get("level"),
                    "code_raw": row.get("code_raw"),
                    "section": _clean(row.get("section")),
                    "section_title": section_title,
                    "chapter": code[:2],
                    "chapter_title": chapter_title,
                    "partida_4d": code[:4],
                    "descripcion_partida_4d": parent4_description,
                    "hs_6d": code[:6] if parent6 else "",
                    "descripcion_hs_6d": parent6_description,
                    "nandina_8d": code,
                    "descripcion_nandina_8d": description,
                    "unidad_fisica": unit,
                    "source_page": row.get("page"),
                    "source_line_no": row.get("line_no_on_page"),
                    "source_line_text": _clean(row.get("line_text")),
                },
            }
        )
    return records


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    source_path = resolve_project_path(args.source)
    hierarchical_path = resolve_project_path(args.hierarchical_corpus)
    output_dir = resolve_project_path(args.output_dir)
    metadata_path = output_dir / "corpus_levels_metadata_v0.1.json"

    rows = _read_jsonl(source_path)
    by4 = _first_by_code(rows, "partida_4d")
    by6 = _first_by_code(rows, "hs_6d")
    corpora = {
        "hs2": _chapter_rows(rows),
        "hs4": _hs4_rows(rows),
        "hs6": _hs6_rows(rows, by4),
        "nandina8": _nandina8_rows(rows, by4, by6),
    }

    output_paths: dict[str, Path] = {}
    for level, records in corpora.items():
        output_path = output_dir / LEVEL_OUTPUTS[level]
        _write_jsonl(output_path, records)
        output_paths[level] = output_path

    level_counts = {level: len(records) for level, records in corpora.items()}
    text_lengths = {
        level: [len(_clean(row.get("texto_index"))) for row in records]
        for level, records in corpora.items()
    }
    metadata: dict[str, Any] = {
        "script": "src.corpus.build_hierarchical_level_corpora",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "version": VERSION,
        "inputs": {
            "source_path": _rel(source_path, root),
            "source_sha256": sha256_file(source_path),
            "hierarchical_corpus_path": _rel(hierarchical_path, root) if hierarchical_path.exists() else "",
            "hierarchical_corpus_sha256": sha256_file(hierarchical_path) if hierarchical_path.exists() else "",
        },
        "outputs": {
            level: {
                "path": _rel(path, root),
                "sha256": sha256_file(path),
                "documents": level_counts[level],
            }
            for level, path in output_paths.items()
        },
        "level_counts": level_counts,
        "source_level_counts": dict(Counter(_clean(row.get("level")) for row in rows)),
        "median_text_index_length": {
            level: float(statistics.median(lengths)) if lengths else 0.0
            for level, lengths in text_lengths.items()
        },
        "policy": {
            "codes_as_search_terms": "No: codes are retained as metadata; texto_index uses descriptions and parent context.",
            "llm_used": False,
            "text2trade_used": False,
            "remote_apis_used": False,
        },
    }
    _write_json(metadata_path, metadata)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build HS2/HS4/HS6/NANDINA8 corpora for hierarchical BM25 tests.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--hierarchical-corpus", type=Path, default=DEFAULT_HIERARCHICAL_CORPUS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser


def main() -> int:
    metadata = build(build_parser().parse_args())
    print("OK: corpus por niveles construido")
    for level, count in metadata["level_counts"].items():
        print(f"{level}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
