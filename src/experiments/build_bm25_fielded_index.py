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
DEFAULT_CORPUS = Path("data/processed/corpus_nandina_fielded_v0.1.jsonl")
DEFAULT_EXPANDED_CORPUS = Path("data/processed/corpus_nandina_fielded_expanded_v0.1.jsonl")
DEFAULT_OUTPUT = Path("data/processed/indexes/bm25_nandina8_fielded_v0.1.pkl")
DEFAULT_EXPANDED_OUTPUT = Path("data/processed/indexes/bm25_nandina8_fielded_expanded_v0.1.pkl")
DEFAULT_METADATA = Path("data/processed/indexes/bm25_nandina8_fielded_v0.1_run_metadata.json")


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _build_one(corpus_path: Path, output_path: Path, *, k1: float, b: float, stopwords: set[str] | None) -> dict[str, Any]:
    rows = read_jsonl(corpus_path)
    index, stats = build_bm25_from_corpus(
        rows,
        type_field="tipo",
        code_field="codigo",
        title_field="titulo",
        text_field="texto_index_fielded",
        fallback_text_field="texto_index",
        target_type="nandina_8",
        k1=k1,
        b=b,
        stopwords=stopwords,
        enforce_8_digits=True,
    )
    ensure_parent(output_path)
    with output_path.open("wb") as handle:
        pickle.dump(index, handle)
    return {
        "corpus_path": corpus_path,
        "output_path": output_path,
        "stats": stats,
        "index": {
            "k1": index.k1,
            "b": index.b,
            "docs": len(index.doc_ids),
            "avgdl": float(index.avgdl),
            "vocab_size": len(index.idf),
        },
    }


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    config_path = resolve_project_path(args.config)
    config = load_json(config_path)
    bm25_cfg = config.get("bm25", {})
    corpus_path = resolve_project_path(args.corpus)
    expanded_corpus_path = resolve_project_path(args.expanded_corpus)
    output_path = resolve_project_path(args.output)
    expanded_output_path = resolve_project_path(args.expanded_output)
    metadata_path = resolve_project_path(args.metadata)

    stopwords = None if args.no_stopwords else DEFAULT_STOPWORDS_ES
    start = time.time()
    k1 = float(bm25_cfg.get("k1", 1.5))
    b = float(bm25_cfg.get("b", 0.75))
    fielded = _build_one(corpus_path, output_path, k1=k1, b=b, stopwords=stopwords)
    expanded = _build_one(expanded_corpus_path, expanded_output_path, k1=k1, b=b, stopwords=stopwords)

    metadata: dict[str, Any] = {
        "script": "src.experiments.build_bm25_fielded_index",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "timestamp_unix": int(time.time()),
        "elapsed_seconds": time.time() - start,
        "environment": {
            "python_version": platform.python_version(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "input": {
            "config_path": _rel(config_path, root),
            "fielded_corpus_path": _rel(corpus_path, root),
            "fielded_corpus_sha256": sha256_file(corpus_path),
            "fielded_expanded_corpus_path": _rel(expanded_corpus_path, root),
            "fielded_expanded_corpus_sha256": sha256_file(expanded_corpus_path),
        },
        "bm25_params": {
            "k1": k1,
            "b": b,
            "use_stopwords": stopwords is not None,
            "stopwords_count": len(stopwords or []),
            "stopwords_source": "src.bm25_index.DEFAULT_STOPWORDS_ES",
            "text_field": "texto_index_fielded",
            "code_field": "codigo",
            "type_field": "tipo",
            "target_type": "nandina_8",
        },
        "fielded": {
            "index_stats": fielded["stats"],
            "index": fielded["index"],
            "output_path": _rel(output_path, root),
            "output_sha256": sha256_file(output_path),
        },
        "fielded_expanded": {
            "index_stats": expanded["stats"],
            "index": expanded["index"],
            "output_path": _rel(expanded_output_path, root),
            "output_sha256": sha256_file(expanded_output_path),
        },
        "validations": {
            "llm_used": False,
            "text2trade_used": False,
            "evalset_executed": False,
        },
    }
    _write_json(metadata_path, metadata)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build BM25 indexes for fielded NANDINA corpora.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--expanded-corpus", type=Path, default=DEFAULT_EXPANDED_CORPUS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--expanded-output", type=Path, default=DEFAULT_EXPANDED_OUTPUT)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA)
    parser.add_argument("--no-stopwords", action="store_true")
    return parser


def main() -> int:
    metadata = build(build_parser().parse_args())
    print("OK: indices BM25 fielded construidos")
    print(f"Fielded docs: {metadata['fielded']['index']['docs']}")
    print(f"Fielded avgdl: {metadata['fielded']['index']['avgdl']:.2f}")
    print(f"Expanded avgdl: {metadata['fielded_expanded']['index']['avgdl']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
