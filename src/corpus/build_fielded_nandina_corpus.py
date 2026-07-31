from __future__ import annotations

import argparse
import json
import re
import statistics
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import is_8_digits, sha256_file
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_INPUT = Path("data/processed/corpus_nandina_hierarchical_v0.1.jsonl")
DEFAULT_EXPANSIONS = Path("src/corpus/controlled_lexical_expansions_v0.1.json")
DEFAULT_OUTPUT = Path("data/processed/corpus_nandina_fielded_v0.1.jsonl")
DEFAULT_EXPANDED_OUTPUT = Path("data/processed/corpus_nandina_fielded_expanded_v0.1.jsonl")
DEFAULT_METADATA = Path("data/processed/corpus_nandina_fielded_v0.1_metadata.json")

CODE_RE = re.compile(r"\b\d{4}(?:\d{2}){0,2}\b")
GENERIC_PHRASES = {"los demas", "las demas", "demas", "solido", "liquido", "ruedas", "partes", "otros", "otras"}


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _norm(text: object) -> str:
    raw = unicodedata.normalize("NFKD", _clean(text).lower())
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch))
    raw = re.sub(r"[^a-z0-9]+", " ", raw)
    return re.sub(r"\s+", " ", raw).strip()


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return payload


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


def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=False) + "\n")


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _strip_codes(text: str) -> str:
    return re.sub(r"\s+", " ", CODE_RE.sub(" ", _clean(text))).strip(" .;:")


def _dedupe_parts(parts: Sequence[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for part in parts:
        value = _strip_codes(part)
        key = _norm(value)
        if value and key and key not in seen:
            seen.add(key)
            output.append(value)
    return output


def _repeat_field(label: str, text: str, weight: int) -> list[str]:
    value = _strip_codes(text)
    if not value or weight <= 0:
        return []
    return [f"{label}: {value}"] * int(weight)


def _load_expansions(path: Path) -> tuple[dict[str, list[str]], dict[str, Any]]:
    payload = _read_json(path)
    by_code: dict[str, list[str]] = {}
    for entry in payload.get("entries", []):
        if not isinstance(entry, Mapping):
            continue
        terms = [_strip_codes(term) for term in entry.get("terms", []) if _strip_codes(term)]
        for code in entry.get("target_codes", []):
            code_text = _clean(code)
            if is_8_digits(code_text):
                by_code.setdefault(code_text, [])
                for term in terms:
                    if _norm(term) not in {_norm(existing) for existing in by_code[code_text]}:
                        by_code[code_text].append(term)
    return by_code, payload


def _field_text(row: Mapping[str, Any], *, chapter_weight: int, expansion_terms: Sequence[str]) -> str:
    parts = []
    parts.extend(_repeat_field("nandina8", _clean(row.get("descripcion_nandina_8d")), 4))
    parts.extend(_repeat_field("hs6", _clean(row.get("descripcion_hs_6d")), 3))
    parts.extend(_repeat_field("partida", _clean(row.get("descripcion_partida_4d")), 1))
    chapter_text = " ".join(_dedupe_parts([_clean(row.get("chapter_title")), _clean(row.get("section_title"))]))
    parts.extend(_repeat_field("capitulo", chapter_text, chapter_weight))
    parts.extend(_repeat_field("expansion", " ".join(_dedupe_parts(expansion_terms)), 2))
    return ". ".join(parts)


def _record_from_row(
    row: Mapping[str, Any],
    *,
    chapter_weight: int,
    expansion_terms: Sequence[str],
    expanded: bool,
) -> dict[str, Any]:
    code = _clean(row.get("codigo"))
    desc8 = _strip_codes(_clean(row.get("descripcion_nandina_8d")))
    desc6 = _strip_codes(_clean(row.get("descripcion_hs_6d")))
    desc4 = _strip_codes(_clean(row.get("descripcion_partida_4d")))
    chapter = _strip_codes(_clean(row.get("chapter_title")))
    expansion_text = " ".join(_dedupe_parts(expansion_terms)) if expanded else ""
    fielded_text = _field_text(row, chapter_weight=chapter_weight, expansion_terms=expansion_terms if expanded else [])
    return {
        "doc_id": f"NANDINA_{code}",
        "tipo": "nandina_8",
        "codigo": code,
        "titulo": desc8,
        "texto": fielded_text,
        "fuente": "NANDINA",
        "version": "fielded_expanded_v0.1" if expanded else "fielded_v0.1",
        "idioma": "es",
        "descripcion_8d": desc8,
        "descripcion_hs6": desc6,
        "descripcion_4d": desc4,
        "descripcion_capitulo": chapter,
        "texto_expansion_controlada": expansion_text,
        "texto_index_fielded": fielded_text,
        "texto_index": fielded_text,
        "metadata": {
            "source_doc_id": _clean(row.get("doc_id")),
            "section": _clean(row.get("section")),
            "section_title": _strip_codes(_clean(row.get("section_title"))),
            "chapter": _clean(row.get("chapter")),
            "partida_4d": _clean(row.get("partida_4d")),
            "hs_6d": _clean(row.get("hs_6d")),
            "unidad_fisica": _clean(row.get("unidad_fisica")),
            "source_page": row.get("source_page"),
            "source_line_no": row.get("source_line_no"),
            "field_weights": {
                "descripcion_8d": 4,
                "descripcion_hs6": 3,
                "descripcion_4d": 1,
                "descripcion_capitulo": chapter_weight,
                "texto_expansion_controlada": 2 if expanded else 0,
            },
            "expansion_terms": list(expansion_terms) if expanded else [],
        },
    }


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    input_path = resolve_project_path(args.input)
    expansions_path = resolve_project_path(args.expansions)
    output_path = resolve_project_path(args.output)
    expanded_output_path = resolve_project_path(args.expanded_output)
    metadata_path = resolve_project_path(args.metadata)

    rows = [row for row in _read_jsonl(input_path) if row.get("tipo") == "nandina_8" and is_8_digits(row.get("codigo"))]
    expansion_by_code, expansion_payload = _load_expansions(expansions_path)

    fielded_rows: list[dict[str, Any]] = []
    expanded_rows: list[dict[str, Any]] = []
    generic_8d = 0
    expanded_docs = 0
    for row in rows:
        code = _clean(row.get("codigo"))
        terms = expansion_by_code.get(code, [])
        if terms:
            expanded_docs += 1
        if _norm(row.get("descripcion_nandina_8d")) in GENERIC_PHRASES:
            generic_8d += 1
        fielded_rows.append(_record_from_row(row, chapter_weight=args.chapter_weight, expansion_terms=[], expanded=False))
        expanded_rows.append(
            _record_from_row(row, chapter_weight=args.chapter_weight, expansion_terms=terms, expanded=True)
        )

    _write_jsonl(output_path, fielded_rows)
    _write_jsonl(expanded_output_path, expanded_rows)

    text_lengths = [len(row["texto_index_fielded"]) for row in fielded_rows]
    expanded_lengths = [len(row["texto_index_fielded"]) for row in expanded_rows]
    expansion_counter = Counter(code for code, terms in expansion_by_code.items() if terms)
    metadata: dict[str, Any] = {
        "script": "src.corpus.build_fielded_nandina_corpus",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "input": {
            "hierarchical_corpus_path": _rel(input_path, root),
            "hierarchical_corpus_sha256": sha256_file(input_path),
            "expansions_path": _rel(expansions_path, root),
            "expansions_sha256": sha256_file(expansions_path),
        },
        "field_weights": {
            "descripcion_8d": 4,
            "descripcion_hs6": 3,
            "descripcion_4d": 1,
            "descripcion_capitulo": args.chapter_weight,
            "texto_expansion_controlada": 2,
        },
        "counts": {
            "input_docs": len(rows),
            "fielded_docs": len(fielded_rows),
            "expanded_docs": len(expanded_rows),
            "docs_with_expansion": expanded_docs,
            "generic_or_short_8d_descriptions": generic_8d,
            "expansion_target_codes_configured": len(expansion_counter),
            "expansion_entries": len(expansion_payload.get("entries", [])),
        },
        "text_lengths": {
            "fielded_median": float(statistics.median(text_lengths)) if text_lengths else 0.0,
            "expanded_median": float(statistics.median(expanded_lengths)) if expanded_lengths else 0.0,
        },
        "outputs": {
            "fielded_corpus_path": _rel(output_path, root),
            "fielded_corpus_sha256": sha256_file(output_path),
            "fielded_expanded_corpus_path": _rel(expanded_output_path, root),
            "fielded_expanded_corpus_sha256": sha256_file(expanded_output_path),
            "metadata_path": _rel(metadata_path, root),
        },
        "validations": {
            "llm_used": False,
            "text2trade_used": False,
            "evalset_executed": False,
            "searchable_text_contains_codes": False,
        },
        "expansions": expansion_payload,
    }
    _write_json(metadata_path, metadata)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build fielded and fielded-expanded NANDINA8 corpora.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--expansions", type=Path, default=DEFAULT_EXPANSIONS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--expanded-output", type=Path, default=DEFAULT_EXPANDED_OUTPUT)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA)
    parser.add_argument("--chapter-weight", type=int, default=0)
    return parser


def main() -> int:
    metadata = build(build_parser().parse_args())
    counts = metadata["counts"]
    print("OK: corpus NANDINA fielded construido")
    print(f"Docs fielded: {counts['fielded_docs']}")
    print(f"Docs con expansion: {counts['docs_with_expansion']}")
    print(f"Mediana fielded: {metadata['text_lengths']['fielded_median']:.1f}")
    print(f"Mediana expanded: {metadata['text_lengths']['expanded_median']:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
