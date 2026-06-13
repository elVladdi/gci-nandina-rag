from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any

from ..bm25_index import sha256_file
from ..utils.paths import ensure_parent, project_root

_CONTEXT_RE = re.compile(r"\bcontexto\s*:\s.*$", flags=re.IGNORECASE | re.DOTALL)


def build_texto_index(texto: Any) -> str:
    """Create a non-destructive lexical field for BM25 indexing."""
    if texto is None:
        return ""
    text = str(texto).strip()
    text = _CONTEXT_RE.sub("", text).strip()
    return re.sub(r"\s+", " ", text).strip()


def add_texto_index_to_jsonl(input_path: Path, output_path: Path) -> dict[str, Any]:
    """Add/refresh ``texto_index`` from ``texto`` in a JSONL corpus."""
    ensure_parent(output_path)
    rows = 0
    context_removed = 0

    with open(input_path, "r", encoding="utf-8") as fin, open(output_path, "w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            original = obj.get("texto", "")
            indexed = build_texto_index(original)
            obj["texto_index"] = indexed

            if isinstance(original, str) and re.search(r"\bcontexto\s*:", original, flags=re.IGNORECASE):
                if not re.search(r"\bcontexto\s*:", indexed, flags=re.IGNORECASE):
                    context_removed += 1

            fout.write(json.dumps(obj, ensure_ascii=False) + "\n")
            rows += 1

    return {
        "timestamp_unix": int(time.time()),
        "input": {"path": str(input_path), "sha256": sha256_file(input_path)},
        "output": {"path": str(output_path), "sha256": sha256_file(output_path)},
        "transform": {
            "strategy": "add_field_texto_index",
            "rule": "remove substring from 'Contexto:' to end-of-text; normalize whitespace",
        },
        "counts": {
            "rows_processed": rows,
            "rows_where_context_was_removed_estimate": context_removed,
        },
    }


def main() -> None:
    root = project_root()
    parser = argparse.ArgumentParser(description="Add texto_index to a curated JSONL corpus.")
    parser.add_argument("--input", type=Path, default=root / "data" / "processed" / "corpus_rag_v1.jsonl")
    parser.add_argument("--output", type=Path, default=root / "data" / "processed" / "corpus_rag_v1_index.jsonl")
    parser.add_argument(
        "--metadata",
        type=Path,
        default=root / "data" / "processed" / "corpus" / "curación" / "03_curacion_index_text_metadata.json",
    )
    args = parser.parse_args()

    metadata = add_texto_index_to_jsonl(args.input, args.output)
    ensure_parent(args.metadata)
    with open(args.metadata, "w", encoding="utf-8") as file:
        json.dump(metadata, file, ensure_ascii=False, indent=2)

    print(f"OK: corpus con texto_index generado en {args.output}")
    print(f"Filas procesadas: {metadata['counts']['rows_processed']}")


if __name__ == "__main__":
    main()
