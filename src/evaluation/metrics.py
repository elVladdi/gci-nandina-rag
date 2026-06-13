from __future__ import annotations

from typing import Any, Mapping, Sequence


def rank_of_true(hits: Sequence[Mapping[str, Any]], true_code: str) -> int:
    """Return the 1-based rank of a true NANDINA code, or 0 if absent."""
    for idx, hit in enumerate(hits, start=1):
        if str(hit.get("code")) == str(true_code):
            return idx
    return 0


def mrr_from_rank(rank: int) -> float:
    return 0.0 if rank <= 0 else 1.0 / float(rank)


def acc_at_k(rank: int, k: int) -> float:
    return 1.0 if 0 < rank <= k else 0.0
