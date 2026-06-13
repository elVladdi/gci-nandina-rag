from __future__ import annotations

import argparse
from pathlib import Path

from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import load_json, project_root, resolve_project_path


def main() -> None:
    root = project_root()
    parser = argparse.ArgumentParser(description="Run a minimal BM25 retrieval smoke test.")
    parser.add_argument("--config", type=Path, default=root / "src" / "configs" / "experiment_config.json")
    parser.add_argument("--index", type=Path, default=None)
    parser.add_argument("--query", default="computadora portatil con procesador y memoria")
    parser.add_argument("--top-n", type=int, default=5)
    args = parser.parse_args()

    config = load_json(args.config)
    paths = config.get("paths", {})
    index_path = args.index or resolve_project_path(
        paths.get("bm25_index_path", "data/processed/indexes/bm25_nandina8.pkl"),
        base_dir=paths.get("base_dir") or ".",
    )

    index = load_bm25_index(index_path)
    hits = retrieve(index, args.query, top_n=args.top_n)

    print(f"Indice: {index_path}")
    print(f"Query: {args.query}")
    for hit in hits:
        text = hit["text"][:120].replace("\n", " ")
        print(f"{hit['rank']:02d}. {hit['code']} | score={hit['score']:.4f} | {text}")


if __name__ == "__main__":
    main()
