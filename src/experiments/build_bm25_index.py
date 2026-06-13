from __future__ import annotations

import argparse
import json
import pickle
import platform
import time
from pathlib import Path

from ..bm25_index import DEFAULT_STOPWORDS_ES, build_bm25_from_corpus, read_jsonl, sha256_file
from ..utils.paths import ensure_parent, load_json, project_root, resolve_project_path


def main() -> None:
    root = project_root()
    parser = argparse.ArgumentParser(description="Build the NANDINA-8 BM25 index.")
    parser.add_argument("--config", type=Path, default=root / "src" / "configs" / "experiment_config.json")
    parser.add_argument("--corpus", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--metadata", type=Path, default=None)
    parser.add_argument("--no-stopwords", action="store_true")
    args = parser.parse_args()

    config = load_json(args.config)
    paths = config.get("paths", {})
    base_dir = paths.get("base_dir") or "."

    corpus_path = args.corpus or resolve_project_path(
        paths.get("corpus_path", "data/processed/corpus_rag_v1_index.jsonl"),
        base_dir=base_dir,
    )
    output_path = args.output or resolve_project_path(
        paths.get("bm25_index_path", "data/processed/indexes/bm25_nandina8.pkl"),
        base_dir=base_dir,
    )
    metadata_path = args.metadata or output_path.with_name("bm25_nandina8_run_metadata.json")

    bm25_cfg = config.get("bm25", {})
    stopwords = None if args.no_stopwords else DEFAULT_STOPWORDS_ES
    start = time.time()
    rows = read_jsonl(corpus_path)
    index, stats = build_bm25_from_corpus(
        rows,
        k1=float(bm25_cfg.get("k1", 1.5)),
        b=float(bm25_cfg.get("b", 0.75)),
        stopwords=stopwords,
    )

    ensure_parent(output_path)
    with open(output_path, "wb") as file:
        pickle.dump(index, file)

    metadata = {
        "script": "src.experiments.build_bm25_index",
        "timestamp_unix": int(time.time()),
        "environment": {
            "python_version": platform.python_version(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "input": {"corpus_path": str(corpus_path), "corpus_sha256": sha256_file(corpus_path)},
        "bm25_params": {
            "k1": index.k1,
            "b": index.b,
            "use_stopwords": stopwords is not None,
            "stopwords_count": len(stopwords or []),
        },
        "index_stats": stats,
        "output": {
            "bm25_index_path": str(output_path),
            "metadata_path": str(metadata_path),
            "elapsed_seconds": time.time() - start,
        },
    }
    ensure_parent(metadata_path)
    with open(metadata_path, "w", encoding="utf-8") as file:
        json.dump(metadata, file, ensure_ascii=False, indent=2)

    print("OK: indice BM25 construido")
    print(f"Docs indexados: {stats['docs_indexed']}")
    print(f"Vocabulario: {stats['vocab_size']}")
    print(f"Artefacto: {output_path}")
    print(f"Metadatos: {metadata_path}")


if __name__ == "__main__":
    main()
