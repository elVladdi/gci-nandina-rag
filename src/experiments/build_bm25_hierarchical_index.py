from __future__ import annotations

import argparse
import json
import pickle
import platform
import time
from datetime import datetime, timezone
from pathlib import Path

from ..bm25_index import DEFAULT_STOPWORDS_ES, build_bm25_from_corpus, read_jsonl, sha256_file
from ..utils.paths import ensure_parent, load_json, project_root, resolve_project_path

DEFAULT_CONFIG = Path("src/configs/experiment_config.json")
DEFAULT_CORPUS = Path("data/processed/corpus_nandina_hierarchical_v0.1.jsonl")
DEFAULT_OUTPUT = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_METADATA = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1_run_metadata.json")


def build(args: argparse.Namespace) -> dict[str, object]:
    root = project_root()
    config_path = resolve_project_path(args.config)
    config = load_json(config_path)
    bm25_cfg = config.get("bm25", {})
    corpus_path = resolve_project_path(args.corpus)
    output_path = resolve_project_path(args.output)
    metadata_path = resolve_project_path(args.metadata)

    stopwords = None if args.no_stopwords else DEFAULT_STOPWORDS_ES
    start = time.time()
    rows = read_jsonl(corpus_path)
    index, stats = build_bm25_from_corpus(
        rows,
        type_field="tipo",
        code_field="codigo",
        title_field="titulo",
        text_field="texto_index_jerarquico",
        fallback_text_field="texto_index",
        target_type="nandina_8",
        k1=float(bm25_cfg.get("k1", 1.5)),
        b=float(bm25_cfg.get("b", 0.75)),
        stopwords=stopwords,
        enforce_8_digits=True,
    )

    ensure_parent(output_path)
    with output_path.open("wb") as handle:
        pickle.dump(index, handle)

    def report_path(path: Path) -> str:
        try:
            return path.resolve().relative_to(root).as_posix()
        except ValueError:
            return str(path.resolve())

    metadata: dict[str, object] = {
        "script": "src.experiments.build_bm25_hierarchical_index",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "timestamp_unix": int(time.time()),
        "environment": {
            "python_version": platform.python_version(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "input": {
            "corpus_path": report_path(corpus_path),
            "corpus_sha256": sha256_file(corpus_path),
            "config_path": report_path(config_path),
        },
        "bm25_params": {
            "k1": index.k1,
            "b": index.b,
            "use_stopwords": stopwords is not None,
            "stopwords_count": len(stopwords or []),
            "stopwords_source": "src.bm25_index.DEFAULT_STOPWORDS_ES",
            "text_field": "texto_index_jerarquico",
            "code_field": "codigo",
            "type_field": "tipo",
            "target_type": "nandina_8",
        },
        "index_stats": stats,
        "output": {
            "bm25_index_path": report_path(output_path),
            "bm25_index_sha256": sha256_file(output_path),
            "metadata_path": report_path(metadata_path),
            "elapsed_seconds": time.time() - start,
        },
    }
    ensure_parent(metadata_path)
    with metadata_path.open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2)
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build BM25 index over hierarchical NANDINA8 corpus.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA)
    parser.add_argument("--no-stopwords", action="store_true")
    return parser


def main() -> int:
    metadata = build(build_parser().parse_args())
    stats = metadata["index_stats"]
    print("OK: indice BM25 jerarquico construido")
    print(f"Docs indexados: {stats['docs_indexed']}")
    print(f"Vocabulario: {stats['vocab_size']}")
    print(f"Avgdl: {stats['avg_doc_len']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
