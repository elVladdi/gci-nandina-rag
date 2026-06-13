from __future__ import annotations

import pickle
import sys
from pathlib import Path
from typing import Any, Dict, List

from .. import bm25_index as bm25_module
from ..bm25_index import BM25Index

sys.modules.setdefault("bm25_index", bm25_module)


def load_bm25_index(path: str | Path) -> BM25Index:
    """Load a BM25Index pickle created by notebooks or package scripts."""
    with open(path, "rb") as file:
        index = pickle.load(file)
    if not isinstance(index, BM25Index):
        raise TypeError(f"Expected BM25Index in {path}, got {type(index)!r}")
    return index


def retrieve(index: BM25Index, query: str, top_n: int = 10) -> List[Dict[str, Any]]:
    """Run BM25 retrieval and return auditable hit dictionaries."""
    hits: List[Dict[str, Any]] = []
    for rank, (doc_idx, score) in enumerate(index.score(query, top_n=top_n), start=1):
        hits.append(
            {
                "rank": rank,
                "doc_idx": int(doc_idx),
                "code": str(index.doc_ids[doc_idx]),
                "score": float(score),
                "text": str(index.doc_texts[doc_idx]),
            }
        )
    return hits
