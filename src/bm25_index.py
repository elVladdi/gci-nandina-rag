from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

__all__ = [
    "BM25Index",
    "DEFAULT_STOPWORDS_ES",
    "build_bm25_from_corpus",
    "is_8_digits",
    "normalize_text",
    "read_jsonl",
    "sha256_file",
    "tokenize_es",
]

_TOKEN_RE = re.compile(r"[a-z0-9]+", flags=re.IGNORECASE)

DEFAULT_STOPWORDS_ES = {
    "de",
    "la",
    "el",
    "y",
    "o",
    "u",
    "en",
    "a",
    "para",
    "por",
    "con",
    "sin",
    "del",
    "al",
    "un",
    "una",
    "unos",
    "unas",
    "lo",
    "las",
    "los",
    "su",
    "sus",
    "se",
    "que",
    "como",
    "mas",
    "menos",
    "muy",
    "ya",
    "no",
    "si",
    "es",
    "son",
    "ser",
    "estar",
    "esta",
    "este",
    "estas",
    "estos",
    "entre",
    "sobre",
    "desde",
    "hasta",
    "segun",
    "mediante",
    "tipo",
    "producto",
    "articulo",
    "mercancia",
    "codigo",
}


def normalize_text(text: Any) -> str:
    """Normalize Spanish technical text for deterministic lexical retrieval."""
    if text is None:
        return ""
    text = str(text).lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return text


def tokenize_es(text: Any, stopwords: Optional[set[str]] = None) -> List[str]:
    """Tokenize normalized Spanish text, optionally removing stopwords."""
    tokens = _TOKEN_RE.findall(normalize_text(text))
    if stopwords:
        tokens = [token for token in tokens if token not in stopwords]
    return tokens


def is_8_digits(code: Any) -> bool:
    """Return True when *code* is exactly an 8-digit NANDINA subheading."""
    return bool(re.fullmatch(r"\d{8}", str(code).strip()))


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    """Compute a SHA-256 digest for a local file."""
    digest = hashlib.sha256()
    with open(path, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def read_jsonl(path: str | Path) -> List[Dict[str, Any]]:
    """Read a JSON Lines file and report the line number on malformed rows."""
    rows: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {line_number}") from exc
    return rows


@dataclass
class BM25Index:
    """Small, pickle-friendly BM25 index used by the NANDINA notebooks/scripts."""

    k1: float
    b: float
    doc_ids: List[str]
    doc_texts: List[str]
    doc_lens: np.ndarray
    avgdl: float
    idf: Dict[str, float]
    inv_index: Dict[str, List[Tuple[int, int]]]

    def score(
        self,
        query: str,
        top_n: int = 10,
        stopwords: Optional[set[str]] = None,
    ) -> List[Tuple[int, float]]:
        """Return ``(doc_idx, score)`` pairs ordered by descending BM25 score."""
        query_terms = tokenize_es(query, stopwords=stopwords)
        if not query_terms or not self.doc_ids:
            return []

        query_tf = Counter(query_terms)
        scores: Dict[int, float] = defaultdict(float)
        avgdl = self.avgdl or 1.0

        for term, q_weight in query_tf.items():
            postings = self.inv_index.get(term)
            if not postings:
                continue
            idf = self.idf.get(term, 0.0)
            for doc_idx, term_freq in postings:
                doc_len = float(self.doc_lens[doc_idx])
                denom = term_freq + self.k1 * (1.0 - self.b + self.b * doc_len / avgdl)
                if denom:
                    scores[doc_idx] += q_weight * idf * (term_freq * (self.k1 + 1.0)) / denom

        ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        return [(int(doc_idx), float(score)) for doc_idx, score in ranked[:top_n]]


def _pick_text(row: Dict[str, Any], text_field: str, fallback_text_field: str) -> str:
    text = row.get(text_field)
    if text is None or not str(text).strip():
        text = row.get(fallback_text_field, "")
    return str(text).strip()


def build_bm25_from_corpus(
    rows: Sequence[Dict[str, Any]],
    type_field: str = "tipo",
    code_field: str = "codigo",
    title_field: str = "titulo",
    text_field: str = "texto_index",
    fallback_text_field: str = "texto",
    target_type: str = "nandina_8",
    k1: float = 1.5,
    b: float = 0.75,
    stopwords: Optional[set[str]] = None,
    enforce_8_digits: bool = True,
) -> Tuple[BM25Index, Dict[str, Any]]:
    """Build a BM25 index from curated JSONL corpus rows."""
    doc_ids: List[str] = []
    doc_texts: List[str] = []
    tokenized_docs: List[List[str]] = []
    skipped = {"wrong_type": 0, "invalid_code": 0, "empty_text": 0}

    for row in rows:
        if target_type and str(row.get(type_field, "")).strip() != target_type:
            skipped["wrong_type"] += 1
            continue

        code = str(row.get(code_field, "")).strip()
        if enforce_8_digits and not is_8_digits(code):
            skipped["invalid_code"] += 1
            continue

        title = str(row.get(title_field, "") or "").strip()
        text = _pick_text(row, text_field=text_field, fallback_text_field=fallback_text_field)
        document_text = f"{title} {text}".strip()
        tokens = tokenize_es(document_text, stopwords=stopwords)
        if not tokens:
            skipped["empty_text"] += 1
            continue

        doc_ids.append(code)
        doc_texts.append(document_text)
        tokenized_docs.append(tokens)

    if not doc_ids:
        raise ValueError("No documents were indexed; check corpus schema and filters.")

    doc_lens = np.array([len(tokens) for tokens in tokenized_docs], dtype=np.float32)
    avgdl = float(np.mean(doc_lens))
    n_docs = len(tokenized_docs)

    document_frequency: Counter[str] = Counter()
    inv_index: Dict[str, List[Tuple[int, int]]] = defaultdict(list)

    for doc_idx, tokens in enumerate(tokenized_docs):
        term_counts = Counter(tokens)
        document_frequency.update(term_counts.keys())
        for term, freq in term_counts.items():
            inv_index[term].append((doc_idx, int(freq)))

    idf = {
        term: math.log(1.0 + (n_docs - df + 0.5) / (df + 0.5))
        for term, df in document_frequency.items()
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


sys.modules.setdefault("bm25_index", sys.modules[__name__])
BM25Index.__module__ = "bm25_index"
