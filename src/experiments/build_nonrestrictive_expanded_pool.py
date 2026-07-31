from __future__ import annotations

import argparse
import csv
import json
import platform
import statistics
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from ..bm25_index import sha256_file
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_FIELDED_INDEX = Path("data/processed/indexes/bm25_nandina8_fielded_v0.1.pkl")
DEFAULT_FIELDED_EXPANDED_INDEX = Path("data/processed/indexes/bm25_nandina8_fielded_expanded_v0.1.pkl")
DEFAULT_LEVEL_INDEX_DIR = Path("data/processed/indexes/bm25_levels")
DEFAULT_PHASE7A_DEVSET_POOL = Path("outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool.csv")
DEFAULT_PHASE7A_EVALSET_POOL = Path("outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool.csv")
DEFAULT_DEVSET_OUTPUT_DIR = Path("outputs/evaluation/nonrestrictive_expanded_pool_devset_v0.1")
DEFAULT_EVALSET_OUTPUT_DIR = Path("outputs/evaluation/nonrestrictive_expanded_pool_evalset_v0.1")

PHASE7A_STRATEGY = "hierarchical_80_dual_backfill_20"
EXPECTED_ROWS = {"devset": 13, "evalset": 600}
HS2_TOP_M = [3, 5]
HS4_TOP_M = [5, 10, 20]
HS6_TOP_M = [10, 20, 50]
PROTECTED_BASE = [50, 80]
K_VALUES = [10, 20, 50, 100, 200]

SOURCE_ORDER = [
    "phase7a_pool",
    "BM25_hierarchical_v0.1",
    "BM25_fielded_weighted_v0.1",
    "BM25_fielded_weighted_expanded_v0.1",
    "hs2_family_backfill",
    "hs4_family_backfill",
    "hs6_family_backfill",
    "level_nandina8_direct",
]


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _median(values: Sequence[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def _code(hit: Mapping[str, Any]) -> str:
    return _clean(hit.get("code") or hit.get("candidate_code"))


def _rank_of_code(hits: Sequence[Mapping[str, Any]], expected_code: str) -> int:
    for rank, hit in enumerate(hits, start=1):
        if _code(hit) == expected_code:
            return rank
    return 0


def _first_prefix_rank(hits: Sequence[Mapping[str, Any]], expected_code: str, prefix_len: int) -> int:
    prefix = expected_code[:prefix_len]
    for rank, hit in enumerate(hits, start=1):
        if _code(hit).startswith(prefix):
            return rank
    return 0


def _hit_at(rank: int, k: int) -> int:
    return int(0 < rank <= k)


def _source_hit(hits: Sequence[Mapping[str, Any]], expected_code: str, depth: int) -> int:
    return int(any(_code(hit) == expected_code for hit in hits[:depth]))


def _load_phase7a_pool(path: Path) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            return {}
        for row in reader:
            if _clean(row.get("pool_strategy")) != PHASE7A_STRATEGY:
                continue
            code = _clean(row.get("candidate_code"))
            case_id = _clean(row.get("case_id"))
            if not code or not case_id:
                continue
            try:
                rank = int(_clean(row.get("candidate_rank_pool")))
            except ValueError:
                continue
            grouped[case_id].append(
                {
                    "code": code,
                    "rank": rank,
                    "score": row.get("hierarchical_score") or row.get("dual_score") or "",
                    "text": _clean(row.get("evidence_text")),
                    "source_membership": ["phase7a_pool"],
                }
            )
    for hits in grouped.values():
        hits.sort(key=lambda item: int(item["rank"]))
    return dict(grouped)


def _case_id(dataset: str, row: Mapping[str, Any], position: int) -> str:
    return _clean(row.get("case_id")) or f"{dataset}-{position:02d}"


def _expected(row: Mapping[str, Any]) -> str:
    return _clean(row.get("nandina") or row.get("nandina_ref"))


def _tag_hits(hits: Sequence[Mapping[str, Any]], source: str) -> list[dict[str, Any]]:
    tagged: list[dict[str, Any]] = []
    for hit in hits:
        item = dict(hit)
        item["code"] = _code(item)
        item["source_membership"] = [source]
        tagged.append(item)
    return tagged


def _family_backfill(
    nandina_hits: Sequence[Mapping[str, Any]],
    family_hits: Sequence[Mapping[str, Any]],
    prefix_len: int,
    top_m: int,
    source: str,
) -> list[dict[str, Any]]:
    prefixes = tuple(_code(hit) for hit in family_hits[:top_m] if _code(hit))
    if not prefixes:
        return []
    output: list[dict[str, Any]] = []
    for hit in nandina_hits:
        code = _code(hit)
        if code.startswith(prefixes):
            item = dict(hit)
            item["code"] = code
            item["source_membership"] = [source]
            item[f"matched_hs{prefix_len}"] = ",".join(prefix for prefix in prefixes if code.startswith(prefix))
            output.append(item)
    return output


def _append_candidates(
    target: list[dict[str, Any]],
    seen: dict[str, dict[str, Any]],
    hits: Sequence[Mapping[str, Any]],
    source: str,
    limit: int | None = None,
) -> None:
    iterable = hits if limit is None else hits[:limit]
    for hit in iterable:
        code = _code(hit)
        if not code:
            continue
        if code in seen:
            memberships = set(seen[code].get("source_membership", []))
            memberships.add(source)
            seen[code]["source_membership"] = sorted(memberships)
            continue
        item = dict(hit)
        item["code"] = code
        item["source_membership"] = sorted(set(item.get("source_membership", []) + [source]))
        seen[code] = item
        target.append(item)


def _renumber(hits: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for rank, hit in enumerate(hits[:depth], start=1):
        item = dict(hit)
        item["rank"] = rank
        output.append(item)
    return output


def _pool_from_sources(cache: Mapping[str, Any], config: Mapping[str, Any]) -> list[dict[str, Any]]:
    strategy = _clean(config["strategy"])
    depth = int(config["pool_depth"])
    protected = int(config["protected_base"])
    pool: list[dict[str, Any]] = []
    seen: dict[str, dict[str, Any]] = {}

    phase7a = cache["sources"].get("phase7a_pool", [])
    hierarchical = cache["sources"].get("BM25_hierarchical_v0.1", [])
    fielded = cache["sources"].get("BM25_fielded_weighted_v0.1", [])
    expanded = cache["sources"].get("BM25_fielded_weighted_expanded_v0.1", [])
    direct = cache["sources"].get("level_nandina8_direct", [])
    hs2_family = _family_backfill(direct, cache["hs2"], 2, int(config["hs2_top_m"]), "hs2_family_backfill")
    hs4_family = _family_backfill(direct, cache["hs4"], 4, int(config["hs4_top_m"]), "hs4_family_backfill")
    hs6_family = _family_backfill(direct, cache["hs6"], 6, int(config["hs6_top_m"]), "hs6_family_backfill")

    if strategy == "base_phase7a_pool_100":
        _append_candidates(pool, seen, phase7a, "phase7a_pool", limit=100)
        return _renumber(pool, depth)

    if strategy == "hierarchical_plus_fielded_100":
        _append_candidates(pool, seen, hierarchical, "BM25_hierarchical_v0.1", limit=protected)
        _append_candidates(pool, seen, fielded, "BM25_fielded_weighted_v0.1")
        _append_candidates(pool, seen, expanded, "BM25_fielded_weighted_expanded_v0.1")
        _append_candidates(pool, seen, hierarchical[protected:], "BM25_hierarchical_v0.1")
        return _renumber(pool, depth)

    _append_candidates(pool, seen, phase7a, "phase7a_pool", limit=protected)
    if strategy in {"phase7a_plus_fielded_100", "phase7a_plus_all_sources_200"}:
        _append_candidates(pool, seen, fielded, "BM25_fielded_weighted_v0.1")
        _append_candidates(pool, seen, expanded, "BM25_fielded_weighted_expanded_v0.1")
    if strategy in {
        "phase7a_plus_hs4_backfill_100",
        "phase7a_plus_hs4_hs6_backfill_100",
        "phase7a_plus_hs4_hs6_backfill_200",
        "phase7a_plus_hs2_hs4_hs6_backfill_100",
        "phase7a_plus_hs2_hs4_hs6_backfill_200",
        "phase7a_plus_all_sources_200",
    }:
        _append_candidates(pool, seen, hs4_family, "hs4_family_backfill")
    if strategy in {
        "phase7a_plus_hs6_backfill_100",
        "phase7a_plus_hs4_hs6_backfill_100",
        "phase7a_plus_hs4_hs6_backfill_200",
        "phase7a_plus_hs2_hs4_hs6_backfill_100",
        "phase7a_plus_hs2_hs4_hs6_backfill_200",
        "phase7a_plus_all_sources_200",
    }:
        _append_candidates(pool, seen, hs6_family, "hs6_family_backfill")
    if strategy in {
        "phase7a_plus_hs2_hs4_hs6_backfill_100",
        "phase7a_plus_hs2_hs4_hs6_backfill_200",
        "phase7a_plus_all_sources_200",
    }:
        _append_candidates(pool, seen, hs2_family, "hs2_family_backfill")
    if strategy == "phase7a_plus_all_sources_200":
        _append_candidates(pool, seen, direct, "level_nandina8_direct")
        _append_candidates(pool, seen, hierarchical, "BM25_hierarchical_v0.1")
    _append_candidates(pool, seen, phase7a[protected:], "phase7a_pool")
    return _renumber(pool, depth)


def _strategy_configs(all_strategies: bool = True, selected: Mapping[str, Any] | None = None) -> list[dict[str, Any]]:
    if selected is not None:
        return [dict(selected)]
    configs: list[dict[str, Any]] = [
        {"strategy": "base_phase7a_pool_100", "pool_depth": 100, "protected_base": 100, "hs2_top_m": 0, "hs4_top_m": 0, "hs6_top_m": 0},
    ]
    for protected in PROTECTED_BASE:
        configs.append({"strategy": "hierarchical_plus_fielded_100", "pool_depth": 100, "protected_base": protected, "hs2_top_m": 0, "hs4_top_m": 0, "hs6_top_m": 0})
        configs.append({"strategy": "phase7a_plus_fielded_100", "pool_depth": 100, "protected_base": protected, "hs2_top_m": 0, "hs4_top_m": 0, "hs6_top_m": 0})
        for hs4 in HS4_TOP_M:
            configs.append({"strategy": "phase7a_plus_hs4_backfill_100", "pool_depth": 100, "protected_base": protected, "hs2_top_m": 0, "hs4_top_m": hs4, "hs6_top_m": 0})
        for hs6 in HS6_TOP_M:
            configs.append({"strategy": "phase7a_plus_hs6_backfill_100", "pool_depth": 100, "protected_base": protected, "hs2_top_m": 0, "hs4_top_m": 0, "hs6_top_m": hs6})
        for hs4 in HS4_TOP_M:
            for hs6 in HS6_TOP_M:
                configs.append({"strategy": "phase7a_plus_hs4_hs6_backfill_100", "pool_depth": 100, "protected_base": protected, "hs2_top_m": 0, "hs4_top_m": hs4, "hs6_top_m": hs6})
                configs.append({"strategy": "phase7a_plus_hs4_hs6_backfill_200", "pool_depth": 200, "protected_base": protected, "hs2_top_m": 0, "hs4_top_m": hs4, "hs6_top_m": hs6})
        for hs2 in HS2_TOP_M:
            for hs4 in HS4_TOP_M:
                for hs6 in HS6_TOP_M:
                    configs.append({"strategy": "phase7a_plus_hs2_hs4_hs6_backfill_100", "pool_depth": 100, "protected_base": protected, "hs2_top_m": hs2, "hs4_top_m": hs4, "hs6_top_m": hs6})
                    configs.append({"strategy": "phase7a_plus_hs2_hs4_hs6_backfill_200", "pool_depth": 200, "protected_base": protected, "hs2_top_m": hs2, "hs4_top_m": hs4, "hs6_top_m": hs6})
                    configs.append({"strategy": "phase7a_plus_all_sources_200", "pool_depth": 200, "protected_base": protected, "hs2_top_m": hs2, "hs4_top_m": hs4, "hs6_top_m": hs6})
    return configs if all_strategies else configs[:1]


def _load_indexes(args: argparse.Namespace) -> dict[str, Any]:
    level_dir = resolve_project_path(args.level_index_dir)
    indexes: dict[str, Any] = {
        "BM25_hierarchical_v0.1": load_bm25_index(resolve_project_path(args.hierarchical_index)),
        "hs2": load_bm25_index(level_dir / "hs2_v0.1.pkl"),
        "hs4": load_bm25_index(level_dir / "hs4_v0.1.pkl"),
        "hs6": load_bm25_index(level_dir / "hs6_v0.1.pkl"),
        "level_nandina8_direct": load_bm25_index(level_dir / "nandina8_v0.1.pkl"),
    }
    fielded_path = resolve_project_path(args.fielded_index)
    expanded_path = resolve_project_path(args.fielded_expanded_index)
    if fielded_path.exists():
        indexes["BM25_fielded_weighted_v0.1"] = load_bm25_index(fielded_path)
    if expanded_path.exists():
        indexes["BM25_fielded_weighted_expanded_v0.1"] = load_bm25_index(expanded_path)
    return indexes


def _build_caches(
    dataset: str,
    rows: Sequence[Mapping[str, Any]],
    indexes: Mapping[str, Any],
    phase7a_pool: Mapping[str, Sequence[Mapping[str, Any]]],
    max_pool_depth: int,
) -> list[dict[str, Any]]:
    nandina_full_depth = len(indexes["level_nandina8_direct"].doc_ids)
    caches: list[dict[str, Any]] = []
    for position, row in enumerate(rows, start=1):
        case_id = _case_id(dataset, row, position)
        query = _clean(row.get("descripcion"))
        source_hits: dict[str, list[dict[str, Any]]] = {
            "phase7a_pool": [dict(hit) for hit in phase7a_pool.get(case_id, [])],
            "BM25_hierarchical_v0.1": _tag_hits(retrieve(indexes["BM25_hierarchical_v0.1"], query, top_n=max_pool_depth), "BM25_hierarchical_v0.1"),
            "level_nandina8_direct": _tag_hits(retrieve(indexes["level_nandina8_direct"], query, top_n=nandina_full_depth), "level_nandina8_direct"),
        }
        for optional in ["BM25_fielded_weighted_v0.1", "BM25_fielded_weighted_expanded_v0.1"]:
            if optional in indexes:
                source_hits[optional] = _tag_hits(retrieve(indexes[optional], query, top_n=max_pool_depth), optional)
            else:
                source_hits[optional] = []
        caches.append(
            {
                "case_id": case_id,
                "descripcion": query,
                "expected_code": _expected(row),
                "sources": source_hits,
                "hs2": retrieve(indexes["hs2"], query, top_n=max(HS2_TOP_M)),
                "hs4": retrieve(indexes["hs4"], query, top_n=max(HS4_TOP_M)),
                "hs6": retrieve(indexes["hs6"], query, top_n=max(HS6_TOP_M)),
            }
        )
    return caches


def _case_summary(cache: Mapping[str, Any], config: Mapping[str, Any], pool: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    expected = _clean(cache["expected_code"])
    phase7a = cache["sources"].get("phase7a_pool", [])
    base_rank = _rank_of_code(phase7a, expected)
    final_rank = _rank_of_code(pool, expected)
    row: dict[str, Any] = {
        "strategy": config["strategy"],
        "pool_depth": config["pool_depth"],
        "protected_base": config["protected_base"],
        "hs2_top_m": config["hs2_top_m"],
        "hs4_top_m": config["hs4_top_m"],
        "hs6_top_m": config["hs6_top_m"],
        "case_id": cache["case_id"],
        "descripcion": cache["descripcion"],
        "nandina_ref": expected,
        "hs2_ref": expected[:2],
        "hs4_ref": expected[:4],
        "hs6_ref": expected[:6],
        "unique_candidates_final_pool": len({_code(hit) for hit in pool if _code(hit)}),
        "expected_code_rank_phase7a": base_rank,
        "expected_code_rank_final_pool": final_rank,
        "expected_hs2_first_rank_final_pool": _first_prefix_rank(pool, expected, 2),
        "expected_hs4_first_rank_final_pool": _first_prefix_rank(pool, expected, 4),
        "expected_hs6_first_rank_final_pool": _first_prefix_rank(pool, expected, 6),
        "rescued_vs_phase7a": int(base_rank <= 0 and final_rank > 0),
        "lost_vs_phase7a": int(base_rank > 0 and final_rank <= 0),
        "rescued_vs_phase7a_at_100": int(base_rank <= 0 and 0 < final_rank <= 100),
        "lost_vs_phase7a_at_100": int(0 < base_rank <= 100 and not (0 < final_rank <= 100)),
        "rescued_vs_phase7a_at_200": int(base_rank <= 0 and 0 < final_rank <= 200),
        "lost_vs_phase7a_at_200": int(0 < base_rank <= 100 and not (0 < final_rank <= 200)),
        "no_source_has_expected": int(not any(_source_hit(hits, expected, int(config["pool_depth"])) for hits in cache["sources"].values())),
    }
    for k in K_VALUES:
        if k <= int(config["pool_depth"]):
            row[f"final_pool_at_{k}"] = _hit_at(final_rank, k)
        else:
            row[f"final_pool_at_{k}"] = ""
    for prefix_len, label in [(2, "hs2"), (4, "hs4"), (6, "hs6")]:
        row[f"{label}_at_100"] = int(_first_prefix_rank(pool[:100], expected, prefix_len) > 0)
    for source in SOURCE_ORDER:
        row[f"source_hit_{source}"] = _source_hit(cache["sources"].get(source, []), expected, int(config["pool_depth"]))
    return row


def _candidate_rows(cache: Mapping[str, Any], config: Mapping[str, Any], pool: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    expected = _clean(cache["expected_code"])
    for rank, hit in enumerate(pool, start=1):
        code = _code(hit)
        memberships = hit.get("source_membership", [])
        rows.append(
            {
                "strategy": config["strategy"],
                "pool_depth": config["pool_depth"],
                "protected_base": config["protected_base"],
                "hs2_top_m": config["hs2_top_m"],
                "hs4_top_m": config["hs4_top_m"],
                "hs6_top_m": config["hs6_top_m"],
                "case_id": cache["case_id"],
                "descripcion": cache["descripcion"],
                "nandina_ref": expected,
                "candidate_code": code,
                "candidate_rank_pool": rank,
                "source_membership": "|".join(memberships),
                "is_expected_code": str(code == expected).lower(),
                "is_expected_hs2": str(code.startswith(expected[:2])).lower(),
                "is_expected_hs4": str(code.startswith(expected[:4])).lower(),
                "is_expected_hs6": str(code.startswith(expected[:6])).lower(),
                "score": hit.get("score", ""),
                "evidence_text": _clean(hit.get("text")),
            }
        )
    return rows


def _metrics_for_strategy(case_rows: Sequence[Mapping[str, Any]], config: Mapping[str, Any]) -> dict[str, Any]:
    depth = int(config["pool_depth"])
    metrics: dict[str, Any] = {
        "strategy": config["strategy"],
        "pool_depth": depth,
        "protected_base": config["protected_base"],
        "hs2_top_m": config["hs2_top_m"],
        "hs4_top_m": config["hs4_top_m"],
        "hs6_top_m": config["hs6_top_m"],
        "cases_total": len(case_rows),
        "average_pool_size": _mean([float(row["unique_candidates_final_pool"]) for row in case_rows]),
        "median_pool_size": _median([float(row["unique_candidates_final_pool"]) for row in case_rows]),
        "rescued_vs_phase7a": sum(int(row["rescued_vs_phase7a"]) for row in case_rows),
        "lost_vs_phase7a": sum(int(row["lost_vs_phase7a"]) for row in case_rows),
        "rescued_vs_phase7a_at_100": sum(int(row["rescued_vs_phase7a_at_100"]) for row in case_rows),
        "lost_vs_phase7a_at_100": sum(int(row["lost_vs_phase7a_at_100"]) for row in case_rows),
        "rescued_vs_phase7a_at_200": sum(int(row["rescued_vs_phase7a_at_200"]) for row in case_rows),
        "lost_vs_phase7a_at_200": sum(int(row["lost_vs_phase7a_at_200"]) for row in case_rows),
        "no_source_has_expected": sum(int(row["no_source_has_expected"]) for row in case_rows),
        "hs2_at_100": _mean([float(row["hs2_at_100"]) for row in case_rows]),
        "hs4_at_100": _mean([float(row["hs4_at_100"]) for row in case_rows]),
        "hs6_at_100": _mean([float(row["hs6_at_100"]) for row in case_rows]),
    }
    for k in K_VALUES:
        if k <= depth:
            metrics[f"final_pool_at_{k}"] = _mean([float(row[f"final_pool_at_{k}"]) for row in case_rows])
        else:
            metrics[f"final_pool_at_{k}"] = None
    # Union oracle is measured across all available nonrestrictive sources for the same final depth.
    for k in [100, 200]:
        if k <= depth:
            metrics[f"union_oracle_at_{k}"] = _mean([float(row[f"source_union_hit_at_{k}"]) for row in case_rows if f"source_union_hit_at_{k}" in row])
        else:
            metrics[f"union_oracle_at_{k}"] = None
    return metrics


def _add_union_oracle(case_rows: list[dict[str, Any]], caches: Sequence[Mapping[str, Any]]) -> None:
    by_case = {cache["case_id"]: cache for cache in caches}
    for row in case_rows:
        cache = by_case[row["case_id"]]
        expected = _clean(cache["expected_code"])
        for k in [100, 200]:
            hit = 0
            for hits in cache["sources"].values():
                if _source_hit(hits, expected, k):
                    hit = 1
                    break
            row[f"source_union_hit_at_{k}"] = hit


def _source_contribution(case_rows: Sequence[Mapping[str, Any]], candidate_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    grouped_cases: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    expected_memberships: dict[tuple[str, str], set[str]] = defaultdict(set)

    for candidate in candidate_rows:
        if _clean(candidate.get("is_expected_code")) != "true":
            continue
        key = json.dumps(
            {
                "strategy": candidate["strategy"],
                "pool_depth": candidate["pool_depth"],
                "protected_base": candidate["protected_base"],
                "hs2_top_m": candidate["hs2_top_m"],
                "hs4_top_m": candidate["hs4_top_m"],
                "hs6_top_m": candidate["hs6_top_m"],
            },
            sort_keys=True,
        )
        case_id = _clean(candidate.get("case_id"))
        memberships = [source for source in _clean(candidate.get("source_membership")).split("|") if source]
        expected_memberships[(key, case_id)].update(memberships)

    for row in case_rows:
        key = json.dumps(
            {
                "strategy": row["strategy"],
                "pool_depth": row["pool_depth"],
                "protected_base": row["protected_base"],
                "hs2_top_m": row["hs2_top_m"],
                "hs4_top_m": row["hs4_top_m"],
                "hs6_top_m": row["hs6_top_m"],
            },
            sort_keys=True,
        )
        grouped_cases[key].append(row)

    for key, items in grouped_cases.items():
        config = json.loads(key)
        for source in SOURCE_ORDER:
            recovered = []
            only = []
            rescued_100 = 0
            rescued_200 = 0
            for row in items:
                memberships = expected_memberships.get((key, _clean(row.get("case_id"))), set())
                if source not in memberships:
                    continue
                recovered.append(row)
                if memberships == {source}:
                    only.append(row)
                rescued_100 += int(row.get("rescued_vs_phase7a_at_100", 0))
                rescued_200 += int(row.get("rescued_vs_phase7a_at_200", 0))
            rows.append(
                {
                    **config,
                    "source": source,
                    "cases_recovered_by_source": len(recovered),
                    "cases_recovered_only_by_source": len(only),
                    "cases_rescued_vs_phase7a_at_100": rescued_100,
                    "cases_rescued_vs_phase7a_at_200": rescued_200,
                    "cases_lost_vs_phase7a_at_100": sum(int(row["lost_vs_phase7a_at_100"]) for row in items),
                    "cases_lost_vs_phase7a_at_200": sum(int(row["lost_vs_phase7a_at_200"]) for row in items),
                }
            )
    return rows


def _selection_key(row: Mapping[str, Any]) -> tuple[Any, ...]:
    depth = int(row["pool_depth"])
    selected_recall = row["final_pool_at_200"] if depth == 200 else row["final_pool_at_100"]
    strategy_complexity = {
        "base_phase7a_pool_100": 0,
        "phase7a_plus_hs4_backfill_100": 1,
        "phase7a_plus_hs6_backfill_100": 1,
        "phase7a_plus_hs4_hs6_backfill_100": 2,
        "phase7a_plus_fielded_100": 2,
        "hierarchical_plus_fielded_100": 3,
        "phase7a_plus_hs2_hs4_hs6_backfill_100": 3,
        "phase7a_plus_hs4_hs6_backfill_200": 4,
        "phase7a_plus_hs2_hs4_hs6_backfill_200": 5,
        "phase7a_plus_all_sources_200": 6,
    }.get(_clean(row["strategy"]), 9)
    return (
        float(selected_recall or 0.0),
        -int(row["lost_vs_phase7a"]),
        float(row["final_pool_at_100"] or 0.0),
        -strategy_complexity,
        -int(row["pool_depth"]),
        -int(row["protected_base"]),
    )


def _summary_markdown(dataset: str, payload: Mapping[str, Any]) -> str:
    selected = payload["selected_strategy"]
    base = payload["base_phase7a_metrics"]
    selected_final_200 = "NA" if selected["final_pool_at_200"] is None else f"{selected['final_pool_at_200']:.4f}"
    lines = [
        f"# Pool expandido no restrictivo {dataset} v0.1",
        "",
        "## Alcance",
        "",
        "Construccion de pool no restrictivo: las familias HS2/HS4/HS6 se usan como fuentes auxiliares de backfill y no como filtro excluyente. No se ejecuto LLM, Ollama, OpenAI, Text2Trade ni APIs remotas.",
        "",
        "## Estrategia seleccionada",
        "",
        f"- Estrategia: `{selected['strategy']}`.",
        f"- Pool depth: {selected['pool_depth']}.",
        f"- Protected base: {selected['protected_base']}.",
        f"- HS2/HS4/HS6 Top-M: {selected['hs2_top_m']}/{selected['hs4_top_m']}/{selected['hs6_top_m']}.",
        "",
        "## Metricas",
        "",
        "| Metodo | Pool | Final@10 | Final@20 | Final@50 | Final@100 | Final@200 | HS2@100 | HS4@100 | HS6@100 | Rescates@100 | Perdidas@100 | Rescates@200 | Perdidas@200 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        f"| phase7a base | 100 | {base['final_pool_at_10']:.4f} | {base['final_pool_at_20']:.4f} | {base['final_pool_at_50']:.4f} | {base['final_pool_at_100']:.4f} | NA | {base['hs2_at_100']:.4f} | {base['hs4_at_100']:.4f} | {base['hs6_at_100']:.4f} | {base['rescued_vs_phase7a_at_100']} | {base['lost_vs_phase7a_at_100']} | NA | NA |",
        f"| seleccionado | {selected['pool_depth']} | {selected['final_pool_at_10']:.4f} | {selected['final_pool_at_20']:.4f} | {selected['final_pool_at_50']:.4f} | {selected['final_pool_at_100']:.4f} | {selected_final_200} | {selected['hs2_at_100']:.4f} | {selected['hs4_at_100']:.4f} | {selected['hs6_at_100']:.4f} | {selected['rescued_vs_phase7a_at_100']} | {selected['lost_vs_phase7a_at_100']} | {selected['rescued_vs_phase7a_at_200']} | {selected['lost_vs_phase7a_at_200']} |",
        "",
        payload["recommendation"],
        "",
    ]
    return "\n".join(lines)


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    dataset = args.dataset
    input_csv = resolve_project_path(args.devset if dataset == "devset" else args.evalset)
    phase7a_csv = resolve_project_path(args.phase7a_devset_pool if dataset == "devset" else args.phase7a_evalset_pool)
    output_dir = resolve_project_path(args.devset_output_dir if dataset == "devset" else args.evalset_output_dir)
    selected_config_path = resolve_project_path(args.selected_config) if args.selected_config else None
    start = time.time()

    rows = _read_csv(input_csv)
    if len(rows) != EXPECTED_ROWS[dataset]:
        raise ValueError(f"{dataset} row count is {len(rows)}, expected {EXPECTED_ROWS[dataset]}.")
    indexes = _load_indexes(args)
    phase7a = _load_phase7a_pool(phase7a_csv)

    if dataset == "evalset":
        if selected_config_path is None or not selected_config_path.exists():
            raise ValueError("Evalset requires --selected-config generated from devset.")
        selected_payload = json.loads(selected_config_path.read_text(encoding="utf-8"))
        configs = _strategy_configs(selected=selected_payload["selected_strategy_config"])
    else:
        configs = _strategy_configs()

    max_depth = max(int(config["pool_depth"]) for config in configs)
    caches = _build_caches(dataset, rows, indexes, phase7a, max(200, max_depth))
    all_candidate_rows: list[dict[str, Any]] = []
    all_case_rows: list[dict[str, Any]] = []
    metrics_rows: list[dict[str, Any]] = []
    selected_case_rows: list[dict[str, Any]] = []
    selected_candidate_rows: list[dict[str, Any]] = []

    for config in configs:
        case_rows: list[dict[str, Any]] = []
        candidate_rows: list[dict[str, Any]] = []
        for cache in caches:
            pool = _pool_from_sources(cache, config)
            case_rows.append(_case_summary(cache, config, pool))
            candidate_rows.extend(_candidate_rows(cache, config, pool))
        _add_union_oracle(case_rows, caches)
        metrics = _metrics_for_strategy(case_rows, config)
        metrics_rows.append(metrics)
        all_case_rows.extend(case_rows)
        all_candidate_rows.extend(candidate_rows)
        if dataset == "evalset":
            selected_case_rows = case_rows
            selected_candidate_rows = candidate_rows

    metrics_rows.sort(key=_selection_key, reverse=True)
    selected_metrics = metrics_rows[0]
    if dataset == "devset":
        selected_config = {
            "strategy": selected_metrics["strategy"],
            "pool_depth": selected_metrics["pool_depth"],
            "protected_base": selected_metrics["protected_base"],
            "hs2_top_m": selected_metrics["hs2_top_m"],
            "hs4_top_m": selected_metrics["hs4_top_m"],
            "hs6_top_m": selected_metrics["hs6_top_m"],
        }
        selected_case_rows = [
            row
            for row in all_case_rows
            if all(str(row[key]) == str(selected_config[key]) for key in selected_config)
        ]
        selected_candidate_rows = [
            row
            for row in all_candidate_rows
            if all(str(row[key]) == str(selected_config[key]) for key in selected_config)
        ]
    else:
        selected_config = configs[0]

    base_metrics = next(row for row in metrics_rows if row["strategy"] == "base_phase7a_pool_100") if dataset == "devset" else None
    if dataset == "evalset":
        base_config = {"strategy": "base_phase7a_pool_100", "pool_depth": 100, "protected_base": 100, "hs2_top_m": 0, "hs4_top_m": 0, "hs6_top_m": 0}
        base_case_rows = []
        for cache in caches:
            base_case_rows.append(_case_summary(cache, base_config, _pool_from_sources(cache, base_config)))
        _add_union_oracle(base_case_rows, caches)
        base_metrics = _metrics_for_strategy(base_case_rows, base_config)

    recommendation = (
        "La estrategia seleccionada mejora o conserva la cobertura amplia frente al pool Fase 7A sin usar filtros excluyentes."
        if float(selected_metrics["final_pool_at_100"] or 0.0) >= float(base_metrics["final_pool_at_100"] or 0.0)
        else "La estrategia seleccionada no mejora Recall@100 frente al pool Fase 7A; revisar antes de escalar."
    )

    source_rows = _source_contribution(selected_case_rows if dataset == "evalset" else all_case_rows, selected_candidate_rows if dataset == "evalset" else all_candidate_rows)
    rescued_rows = [row for row in selected_case_rows if int(row["rescued_vs_phase7a"])]
    missed_rows = [row for row in selected_case_rows if int(row["expected_code_rank_final_pool"]) <= 0]

    payload: dict[str, Any] = {
        "script": "src.experiments.build_nonrestrictive_expanded_pool",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": time.time() - start,
        "dataset": dataset,
        "environment": {
            "python_version": platform.python_version(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "inputs": {
            "input_csv": _rel(input_csv, root),
            "input_sha256": sha256_file(input_csv),
            "phase7a_pool_csv": _rel(phase7a_csv, root),
            "phase7a_pool_sha256": sha256_file(phase7a_csv),
        },
        "available_sources": [source for source in SOURCE_ORDER if source == "phase7a_pool" or source in indexes or source.endswith("_backfill")],
        "parameters": {
            "hs2_top_m": HS2_TOP_M,
            "hs4_top_m": HS4_TOP_M,
            "hs6_top_m": HS6_TOP_M,
            "protected_base": PROTECTED_BASE,
            "strategy_count": len(configs),
            "source_contribution_policy": "Computed from source_membership of expected candidates in the final expanded pool, including family backfill memberships.",
            "selection_rule": "devset only: maximize final_pool_at_200 for Top-200 strategies or final_pool_at_100 for Top-100; then minimize lost_vs_phase7a; then prefer simpler and Top-100.",
        },
        "selected_strategy_config": selected_config,
        "selected_strategy": selected_metrics,
        "base_phase7a_metrics": base_metrics,
        "metrics_by_strategy": metrics_rows,
        "recommendation": recommendation,
        "policy": {
            "llm_used": False,
            "ollama_used": False,
            "openai_used": False,
            "text2trade_used": False,
            "requests_used": False,
            "http_used": False,
            "remote_apis_used": False,
            "evalset_used_for_strategy_selection": False,
        },
        "outputs": {
            "expanded_pool_csv": _rel(output_dir / "expanded_pool.csv", root),
            "expanded_pool_case_summary_csv": _rel(output_dir / "expanded_pool_case_summary.csv", root),
            "expanded_pool_metrics_json": _rel(output_dir / "expanded_pool_metrics.json", root),
            "expanded_pool_summary_md": _rel(output_dir / "expanded_pool_summary.md", root),
            "source_contribution_csv": _rel(output_dir / "source_contribution.csv", root),
            "rescued_cases_csv": _rel(output_dir / "rescued_cases.csv", root),
            "missed_cases_csv": _rel(output_dir / "missed_cases.csv", root),
        },
    }

    candidate_fieldnames = [
        "strategy", "pool_depth", "protected_base", "hs2_top_m", "hs4_top_m", "hs6_top_m", "case_id", "descripcion",
        "nandina_ref", "candidate_code", "candidate_rank_pool", "source_membership", "is_expected_code", "is_expected_hs2",
        "is_expected_hs4", "is_expected_hs6", "score", "evidence_text",
    ]
    case_fieldnames = [
        "strategy", "pool_depth", "protected_base", "hs2_top_m", "hs4_top_m", "hs6_top_m", "case_id", "descripcion",
        "nandina_ref", "hs2_ref", "hs4_ref", "hs6_ref", "unique_candidates_final_pool", "expected_code_rank_phase7a",
        "expected_code_rank_final_pool", "expected_hs2_first_rank_final_pool", "expected_hs4_first_rank_final_pool",
        "expected_hs6_first_rank_final_pool", "rescued_vs_phase7a", "lost_vs_phase7a", "no_source_has_expected",
        "final_pool_at_10", "final_pool_at_20", "final_pool_at_50", "final_pool_at_100", "final_pool_at_200",
        "hs2_at_100", "hs4_at_100", "hs6_at_100", "source_union_hit_at_100", "source_union_hit_at_200",
    ] + [f"source_hit_{source}" for source in SOURCE_ORDER]
    source_fieldnames = ["strategy", "pool_depth", "protected_base", "hs2_top_m", "hs4_top_m", "hs6_top_m", "source", "cases_recovered_by_source", "cases_recovered_only_by_source", "cases_rescued_vs_phase7a_at_100", "cases_rescued_vs_phase7a_at_200", "cases_lost_vs_phase7a_at_100", "cases_lost_vs_phase7a_at_200"]

    _write_csv(output_dir / "expanded_pool.csv", selected_candidate_rows, candidate_fieldnames)
    _write_csv(output_dir / "expanded_pool_case_summary.csv", selected_case_rows, case_fieldnames)
    _write_json(output_dir / "expanded_pool_metrics.json", payload)
    (ensure_parent(output_dir / "expanded_pool_summary.md")).write_text(_summary_markdown(dataset, payload), encoding="utf-8")
    _write_csv(output_dir / "source_contribution.csv", source_rows, source_fieldnames)
    _write_csv(output_dir / "rescued_cases.csv", rescued_rows, case_fieldnames)
    _write_csv(output_dir / "missed_cases.csv", missed_rows, case_fieldnames)

    if dataset == "devset":
        _write_json(output_dir / "selected_strategy_config.json", {"selected_strategy_config": selected_config, "selected_strategy": selected_metrics})
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build nonrestrictive expanded NANDINA8 candidate pool.")
    parser.add_argument("--dataset", choices=["devset", "evalset"], default="devset")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--fielded-index", type=Path, default=DEFAULT_FIELDED_INDEX)
    parser.add_argument("--fielded-expanded-index", type=Path, default=DEFAULT_FIELDED_EXPANDED_INDEX)
    parser.add_argument("--level-index-dir", type=Path, default=DEFAULT_LEVEL_INDEX_DIR)
    parser.add_argument("--phase7a-devset-pool", type=Path, default=DEFAULT_PHASE7A_DEVSET_POOL)
    parser.add_argument("--phase7a-evalset-pool", type=Path, default=DEFAULT_PHASE7A_EVALSET_POOL)
    parser.add_argument("--devset-output-dir", type=Path, default=DEFAULT_DEVSET_OUTPUT_DIR)
    parser.add_argument("--evalset-output-dir", type=Path, default=DEFAULT_EVALSET_OUTPUT_DIR)
    parser.add_argument("--selected-config", type=Path, default=DEFAULT_DEVSET_OUTPUT_DIR / "selected_strategy_config.json")
    return parser


def main() -> int:
    payload = build(build_parser().parse_args())
    selected = payload["selected_strategy"]
    print(f"OK: pool expandido no restrictivo {payload['dataset']} construido")
    print(
        f"Seleccion: {selected['strategy']} depth={selected['pool_depth']} "
        f"protect={selected['protected_base']} hs2={selected['hs2_top_m']} "
        f"hs4={selected['hs4_top_m']} hs6={selected['hs6_top_m']}"
    )
    print(f"final_pool@100={selected['final_pool_at_100']:.4f}")
    if selected["final_pool_at_200"] is not None:
        print(f"final_pool@200={selected['final_pool_at_200']:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
