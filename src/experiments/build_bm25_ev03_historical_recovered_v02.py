"""EV03-only recovery of the historical Decision885 BM25 build semantics.

The historical Python 3.11 bytecode and frozen index show that one-character
alphanumeric tokens were removed before stopword filtering.  This module keeps
that recovered policy local to EV03; it deliberately does not change the
repository-wide BM25 implementation or EV04.
"""

from __future__ import annotations

import argparse
import json
import math
import pickle
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

from ..bm25_index import (
    BM25Index,
    DEFAULT_STOPWORDS_ES,
    is_8_digits,
    read_jsonl,
    sha256_file,
    tokenize_es,
)


ROOT = Path(__file__).resolve().parents[2]
TOKEN_POLICY = "DROP_SINGLE_CHARACTER_TOKENS"


def tokenize_ev03_recovered_historical(
    text: Any,
    stopwords: set[str] | None = DEFAULT_STOPWORDS_ES,
) -> list[str]:
    """Apply the recovered EV03 policy without changing global tokenization."""

    tokens = [token for token in tokenize_es(text, stopwords=None) if len(token) > 1]
    if stopwords:
        tokens = [token for token in tokens if token not in stopwords]
    return tokens


def _pick_text(row: Mapping[str, Any], text_field: str, fallback_text_field: str) -> str:
    text = row.get(text_field)
    if text is None or not str(text).strip():
        text = row.get(fallback_text_field, "")
    return str(text).strip()


def build_ev03_recovered_historical_from_corpus(
    rows: Sequence[Mapping[str, Any]],
    *,
    k1: float = 1.5,
    b: float = 0.75,
    stopwords: set[str] | None = DEFAULT_STOPWORDS_ES,
) -> tuple[BM25Index, dict[str, Any]]:
    """Build NANDINA-8 documents with the recovered historical EV03 tokenizer."""

    if (float(k1), float(b)) != (1.5, 0.75):
        raise ValueError("Recovered EV03 builder requires frozen k1=1.5 and b=0.75")

    doc_ids: list[str] = []
    doc_texts: list[str] = []
    tokenized_docs: list[list[str]] = []
    skipped = {"wrong_type": 0, "invalid_code": 0, "empty_text": 0}

    for row in rows:
        if str(row.get("tipo", "")).strip() != "nandina_8":
            skipped["wrong_type"] += 1
            continue
        code = str(row.get("codigo", "")).strip()
        if not is_8_digits(code):
            skipped["invalid_code"] += 1
            continue
        title = str(row.get("titulo", "") or "").strip()
        text = _pick_text(row, "texto_index", "texto")
        document_text = f"{title} {text}".strip()
        tokens = tokenize_ev03_recovered_historical(document_text, stopwords=stopwords)
        if not tokens:
            skipped["empty_text"] += 1
            continue
        doc_ids.append(code)
        doc_texts.append(document_text)
        tokenized_docs.append(tokens)

    if not doc_ids:
        raise ValueError("Recovered EV03 builder produced no documents")

    doc_lens = np.array([len(tokens) for tokens in tokenized_docs], dtype=np.float32)
    avgdl = float(np.mean(doc_lens))
    document_frequency: Counter[str] = Counter()
    inv_index: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for doc_idx, tokens in enumerate(tokenized_docs):
        term_counts = Counter(tokens)
        document_frequency.update(term_counts.keys())
        for term, frequency in term_counts.items():
            inv_index[term].append((doc_idx, int(frequency)))

    document_count = len(tokenized_docs)
    idf = {
        term: math.log(1.0 + (document_count - frequency + 0.5) / (frequency + 0.5))
        for term, frequency in document_frequency.items()
    }
    index = BM25Index(
        k1=float(k1),
        b=float(b),
        doc_ids=doc_ids,
        doc_texts=doc_texts,
        doc_lens=doc_lens,
        avgdl=avgdl,
        idf=idf,
        inv_index=dict(inv_index),
    )
    stats = {
        "rows_input": len(rows),
        "docs_indexed": len(doc_ids),
        "vocab_size": len(idf),
        "avg_doc_len": avgdl,
        "min_doc_len": float(np.min(doc_lens)),
        "max_doc_len": float(np.max(doc_lens)),
        "skipped": skipped,
    }
    return index, stats


def build(
    corpus_path: Path,
    output_path: Path,
    metadata_path: Path,
    *,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Build a non-overwriting EV03 preexecution index and metadata."""

    corpus_path = (root / corpus_path).resolve() if not corpus_path.is_absolute() else corpus_path.resolve()
    output_path = (root / output_path).resolve() if not output_path.is_absolute() else output_path.resolve()
    metadata_path = (root / metadata_path).resolve() if not metadata_path.is_absolute() else metadata_path.resolve()
    if not corpus_path.is_file():
        raise FileNotFoundError(corpus_path)
    if output_path.exists() or metadata_path.exists():
        raise FileExistsError("Recovered EV03 builder refuses overwrite or resume")

    index, stats = build_ev03_recovered_historical_from_corpus(read_jsonl(corpus_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("xb") as handle:
        pickle.dump(index, handle)
    metadata = {
        "artifact_id": "0b05c_ev03_decision885_preexecution_index_v0.2",
        "arm": "EV03",
        "builder": "src/experiments/build_bm25_ev03_historical_recovered_v02.py",
        "EV03_RECOVERED_HISTORICAL_TOKEN_POLICY": TOKEN_POLICY,
        "scope": "EV03_ONLY",
        "input": {
            "corpus_path": corpus_path.relative_to(root).as_posix(),
            "corpus_sha256": sha256_file(corpus_path),
        },
        "bm25_params": {
            "k1": index.k1,
            "b": index.b,
            "use_stopwords": True,
            "stopwords_count": len(DEFAULT_STOPWORDS_ES),
        },
        "index_stats": stats,
        "output": {
            "bm25_index_path": output_path.relative_to(root).as_posix(),
            "bm25_index_sha256": sha256_file(output_path),
            "metadata_path": metadata_path.relative_to(root).as_posix(),
        },
    }
    with metadata_path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return metadata


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the recovered historical EV03 Decision885 control index v0.2")
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    args = parser.parse_args(argv)
    print(json.dumps(build(args.corpus, args.output, args.metadata), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
