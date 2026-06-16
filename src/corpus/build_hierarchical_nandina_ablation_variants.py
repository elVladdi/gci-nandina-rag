from __future__ import annotations

import argparse
import json
import re
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from ..bm25_index import sha256_file
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_INPUT = Path("data/processed/corpus/nandina/nandina_corpus.jsonl")
DEFAULT_OUTPUT_DIR = Path("data/processed/corpus_ablation_nandina_v0.1")

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


def _clean_description(text: object) -> str:
    value = _clean(text)
    for pattern in HEADER_REPLACEMENTS:
        value = pattern.sub(" ", value)
    value = value.replace("|", " ")
    value = re.sub(r"\s+", " ", value).strip(" -;:")
    return value


def _join(parts: Sequence[str]) -> str:
    values = [re.sub(r"\s+", " ", _clean(part)).strip(" ;") for part in parts]
    return ". ".join(value for value in values if value).strip()


def _repeat(text: str, times: int) -> list[str]:
    value = _clean(text)
    return [value for _ in range(max(1, times))] if value else []


def _first_by_code(rows: Sequence[Mapping[str, Any]], level: str) -> dict[str, Mapping[str, Any]]:
    mapping: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if row.get("level") == level:
            code = _clean(row.get("code_digits"))
            mapping.setdefault(code, row)
    return mapping


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _variant_builders(leaf_repeat: int) -> dict[str, Callable[[Mapping[str, Any]], str]]:
    return {
        "A_leaf_only": lambda ctx: _join([ctx["desc8"]]),
        "B_4d_leaf": lambda ctx: _join([ctx["desc4"], ctx["desc8"]]),
        "C_hs6_leaf": lambda ctx: _join([ctx["desc6"], ctx["desc8"]]),
        "D_4d_hs6_leaf": lambda ctx: _join([ctx["desc4"], ctx["desc6"], ctx["desc8"]]),
        "E_4d_hs6_leaf_weighted": lambda ctx: _join(
            [ctx["desc4"], ctx["desc6"], *_repeat(ctx["desc8"], leaf_repeat)]
        ),
        "F_hs6_leaf_weighted": lambda ctx: _join([ctx["desc6"], *_repeat(ctx["desc8"], leaf_repeat)]),
        "G_chapter_4d_hs6_leaf_weighted": lambda ctx: _join(
            [ctx["chapter_title"], ctx["desc4"], ctx["desc6"], *_repeat(ctx["desc8"], leaf_repeat)]
        ),
    }


def _base_record(
    row: Mapping[str, Any],
    parent4: Mapping[str, Any] | None,
    parent6: Mapping[str, Any] | None,
    input_sha256: str,
    variant_id: str,
    text: str,
) -> dict[str, Any]:
    code = _clean(row.get("code_digits"))
    return {
        "doc_id": f"NANDINA_{code}_{variant_id}",
        "codigo": code,
        "tipo": "nandina_8",
        "variant_id": variant_id,
        "texto_index_variant": text,
        "titulo": _clean_description(row.get("description")),
        "descripcion_nandina8": _clean_description(row.get("description")),
        "partida_4d": code[:4],
        "descripcion_partida_4d": _clean_description(parent4.get("description")) if parent4 else "",
        "hs_6d": code[:6] if parent6 else "",
        "descripcion_hs_6d": _clean_description(parent6.get("description")) if parent6 else "",
        "has_parent_4d": bool(parent4),
        "has_parent_hs6": bool(parent6),
        "chapter": _clean(row.get("chapter")) or code[:2],
        "chapter_title": _clean(row.get("chapter_title")),
        "section": _clean(row.get("section")),
        "section_title": _clean(row.get("section_title")),
        "unit": _clean(row.get("unit")),
        "source_page": row.get("page"),
        "source_line_no": row.get("line_no_on_page"),
        "source_line_text": _clean(row.get("line_text")),
        "source_input_sha256": input_sha256,
    }


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    input_path = resolve_project_path(args.input)
    output_dir = resolve_project_path(args.output_dir)
    input_sha = sha256_file(input_path)

    rows = _read_jsonl(input_path)
    by4 = _first_by_code(rows, "partida_4d")
    by6 = _first_by_code(rows, "hs_6d")
    nandina8_rows = [row for row in rows if row.get("level") == "nandina_8d" and re.fullmatch(r"\d{8}", _clean(row.get("code_digits")))]
    builders = _variant_builders(args.leaf_repeat)

    metadata: dict[str, Any] = {
        "script": "src.corpus.build_hierarchical_nandina_ablation_variants",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "input_path": _rel(input_path, root),
        "input_sha256": input_sha,
        "output_dir": _rel(output_dir, root),
        "leaf_repeat": args.leaf_repeat,
        "variants_generated": list(builders.keys()),
        "variant_stats": {},
        "warnings": [],
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    missing4 = 0
    missing6 = 0
    for variant_id, builder in builders.items():
        output_path = output_dir / f"{variant_id}.jsonl"
        lengths: list[int] = []
        docs = 0
        with output_path.open("w", encoding="utf-8", newline="\n") as handle:
            for row in nandina8_rows:
                code = _clean(row.get("code_digits"))
                parent4 = by4.get(code[:4])
                parent6 = by6.get(code[:6])
                if variant_id == "A_leaf_only":
                    missing4 += int(parent4 is None)
                    missing6 += int(parent6 is None)
                ctx = {
                    "desc8": _clean_description(row.get("description")),
                    "desc4": _clean_description(parent4.get("description")) if parent4 else "",
                    "desc6": _clean_description(parent6.get("description")) if parent6 else "",
                    "chapter_title": _clean(row.get("chapter_title")),
                }
                text = builder(ctx)
                record = _base_record(row, parent4, parent6, input_sha, variant_id, text)
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                lengths.append(len(text))
                docs += 1
        metadata["variant_stats"][variant_id] = {
            "path": _rel(output_path, root),
            "sha256": sha256_file(output_path),
            "total_documents": docs,
            "median_text_length": float(statistics.median(lengths)) if lengths else 0.0,
            "min_text_length": min(lengths) if lengths else 0,
            "max_text_length": max(lengths) if lengths else 0,
            "with_parent_4d": sum(1 for row in nandina8_rows if by4.get(_clean(row.get("code_digits"))[:4])),
            "with_parent_hs6": sum(1 for row in nandina8_rows if by6.get(_clean(row.get("code_digits"))[:6])),
            "without_parent_4d": sum(1 for row in nandina8_rows if not by4.get(_clean(row.get("code_digits"))[:4])),
            "without_parent_hs6": sum(1 for row in nandina8_rows if not by6.get(_clean(row.get("code_digits"))[:6])),
        }

    if missing4:
        metadata["warnings"].append(f"{missing4} NANDINA8 rows do not have an explicit 4D parent.")
    if missing6:
        metadata["warnings"].append(f"{missing6} NANDINA8 rows do not have an explicit HS6 parent; HS6 variants fall back to leaf text.")
    metadata["total_nandina8_input"] = len(nandina8_rows)
    _write_json(output_dir / "ablation_variants_metadata.json", metadata)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build NANDINA hierarchy ablation corpus variants A-G.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--leaf-repeat", type=int, default=3)
    return parser


def main() -> int:
    metadata = build(build_parser().parse_args())
    print("OK: variantes de corpus ablation generadas")
    print(f"Input NANDINA8: {metadata['total_nandina8_input']}")
    print(f"Variantes: {', '.join(metadata['variants_generated'])}")
    for variant_id, stats in metadata["variant_stats"].items():
        print(f"{variant_id}: docs={stats['total_documents']} mediana_chars={stats['median_text_length']:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
