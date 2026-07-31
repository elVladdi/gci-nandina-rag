from __future__ import annotations

import argparse
import json
import pickle
import platform
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from ..bm25_index import DEFAULT_STOPWORDS_ES, build_bm25_from_corpus, read_jsonl, sha256_file
from ..utils.paths import ensure_parent, load_json, project_root, resolve_project_path

DEFAULT_CONFIG = Path("src/configs/experiment_config.json")
DEFAULT_CORPUS_DIR = Path("data/processed/corpus_levels")
DEFAULT_OUTPUT_DIR = Path("data/processed/indexes/bm25_levels")
VERSION = "v0.1"

LEVEL_CORPORA = {
    "hs2": "hs2_corpus_v0.1.jsonl",
    "hs4": "hs4_corpus_v0.1.jsonl",
    "hs6": "hs6_corpus_v0.1.jsonl",
    "nandina8": "nandina8_corpus_v0.1.jsonl",
}


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    config_path = resolve_project_path(args.config)
    corpus_dir = resolve_project_path(args.corpus_dir)
    output_dir = resolve_project_path(args.output_dir)
    metadata_path = output_dir / "index_metadata_v0.1.json"

    config = load_json(config_path)
    bm25_cfg = config.get("bm25", {})
    stopwords = None if args.no_stopwords else DEFAULT_STOPWORDS_ES
    start = time.time()

    indexes: dict[str, Any] = {}
    for level, filename in LEVEL_CORPORA.items():
        corpus_path = corpus_dir / filename
        output_path = output_dir / f"{level}_v0.1.pkl"
        rows = read_jsonl(corpus_path)
        index, stats = build_bm25_from_corpus(
            rows,
            type_field="nivel",
            code_field="codigo",
            title_field="descripcion",
            text_field="texto_index",
            fallback_text_field="descripcion",
            target_type=level,
            k1=float(bm25_cfg.get("k1", 1.5)),
            b=float(bm25_cfg.get("b", 0.75)),
            stopwords=stopwords,
            enforce_8_digits=False,
        )
        ensure_parent(output_path)
        with output_path.open("wb") as handle:
            pickle.dump(index, handle)
        indexes[level] = {
            "corpus_path": _rel(corpus_path, root),
            "corpus_sha256": sha256_file(corpus_path),
            "index_path": _rel(output_path, root),
            "index_sha256": sha256_file(output_path),
            "stats": stats,
        }

    metadata: dict[str, Any] = {
        "script": "src.experiments.build_bm25_level_indexes",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "version": VERSION,
        "environment": {
            "python_version": platform.python_version(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "inputs": {
            "config_path": _rel(config_path, root),
            "config_sha256": sha256_file(config_path),
            "corpus_dir": _rel(corpus_dir, root),
        },
        "bm25_params": {
            "k1": float(bm25_cfg.get("k1", 1.5)),
            "b": float(bm25_cfg.get("b", 0.75)),
            "use_stopwords": stopwords is not None,
            "stopwords_count": len(stopwords or []),
            "text_field": "texto_index",
            "code_field": "codigo",
            "type_field": "nivel",
            "codes_as_search_terms": "No: corpora keep codes as metadata and omit them from texto_index.",
        },
        "indexes": indexes,
        "outputs": {
            "metadata_path": _rel(metadata_path, root),
            "elapsed_seconds": time.time() - start,
        },
        "policy": {
            "llm_used": False,
            "text2trade_used": False,
            "remote_apis_used": False,
        },
    }
    _write_json(metadata_path, metadata)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build BM25 indexes for HS2/HS4/HS6/NANDINA8 level corpora.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--corpus-dir", type=Path, default=DEFAULT_CORPUS_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--no-stopwords", action="store_true")
    return parser


def main() -> int:
    metadata = build(build_parser().parse_args())
    print("OK: indices BM25 por nivel construidos")
    for level, item in metadata["indexes"].items():
        stats = item["stats"]
        print(f"{level}: docs={stats['docs_indexed']} vocab={stats['vocab_size']} avgdl={stats['avg_doc_len']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
