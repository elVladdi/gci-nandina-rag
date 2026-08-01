from __future__ import annotations

import argparse
import csv
import json
import platform
import re
import statistics
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_HISTORICAL = Path("data/processed/data_aduanas_historico_clase87_v0.1.csv")
DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.1.csv")
DEFAULT_HISTORICAL_RESULTS = Path(
    "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/historical_results.csv"
)
DEFAULT_HISTORICAL_CASE_SUMMARY = Path(
    "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/historical_case_summary.csv"
)
DEFAULT_HISTORICAL_METRICS = Path(
    "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/historical_metrics.json"
)
DEFAULT_NORMATIVE_POOL = Path("outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/candidate_pool.csv")
DEFAULT_NORMATIVE_METRICS = Path("outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/candidate_pool_metrics.json")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/hybrid_pool_data_aduanas_clase87_v0.1")

QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
EXPECTED_HISTORICAL_ROWS = 3000
EXPECTED_EVAL_ROWS = 1006
HISTORICAL_METHOD = "historical_bm25_data_aduanas_clase87"
NORMATIVE_STRATEGY = "hierarchical_70_dual_backfill_30"
K_VALUES = [1, 3, 5, 10, 20, 50, 100, 200]
HIERARCHICAL_K = [10, 50, 100, 200]
LOW_SUPPORT_THRESHOLD = 10

STRATEGIES = [
    "historical_only",
    "historical_first_90_normative_10",
    "historical_first_80_normative_20",
    "historical_first_70_normative_30",
    "historical_first_50_normative_50",
    "historical_with_normative_backfill_if_low_support",
    "historical_with_normative_backfill_if_missing_code",
    "normative_only_reference",
]


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _iter_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        for row in reader:
            yield {_clean(key): _clean(value) for key, value in row.items() if key is not None}


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


def _valid_nandina(code: str) -> bool:
    return bool(re.fullmatch(r"\d{8}", _clean(code)))


def _support_bucket(count: int) -> str:
    if count <= 0:
        return "0"
    if count == 1:
        return "1"
    if count <= 4:
        return "2-4"
    if count <= 9:
        return "5-9"
    return "10+"


def _validate_split(rows: Sequence[Mapping[str, str]], expected_rows: int, split_name: str) -> None:
    if len(rows) != expected_rows:
        raise ValueError(f"{split_name} expected {expected_rows} rows, found {len(rows)}")
    seen_ids: set[str] = set()
    for position, row in enumerate(rows, start=1):
        row_id = _clean(row.get("id_unico"))
        if not row_id:
            raise ValueError(f"{split_name} row {position} has empty id_unico")
        if row_id in seen_ids:
            raise ValueError(f"{split_name} duplicated id_unico: {row_id}")
        seen_ids.add(row_id)
        if not _valid_nandina(_clean(row.get(LABEL_COLUMN))):
            raise ValueError(f"{split_name} row {position} has invalid NANDINA: {row.get(LABEL_COLUMN)}")
        if _clean(row.get("Clase")) != "87":
            raise ValueError(f"{split_name} row {position} has Clase != 87")
        if not _clean(row.get(QUERY_COLUMN)):
            raise ValueError(f"{split_name} row {position} has empty query column")


def _validate_no_overlap(historical_rows: Sequence[Mapping[str, str]], eval_rows: Sequence[Mapping[str, str]]) -> int:
    historical_ids = {_clean(row.get("id_unico")) for row in historical_rows}
    eval_ids = {_clean(row.get("id_unico")) for row in eval_rows}
    overlap = historical_ids & eval_ids
    if overlap:
        raise ValueError(f"Historical/eval id_unico overlap detected: {sorted(overlap)[:5]}")
    return 0


def _candidate(
    code: str,
    source: str,
    rank: int,
    score: float = 0.0,
    evidence_text: str = "",
    candidate_case_id: str = "",
    candidate_id_unico: str = "",
    candidate_support_count: int = 0,
) -> dict[str, Any]:
    return {
        "candidate_nandina": code,
        "sources": {source},
        "source_ranks": {source: rank},
        "source_scores": {source: float(score)},
        "candidate_description": evidence_text,
        "candidate_case_id": candidate_case_id,
        "candidate_id_unico": candidate_id_unico,
        "candidate_historical_support_count": int(candidate_support_count),
        "candidate_support_bucket": _support_bucket(int(candidate_support_count)),
    }


def _merge_candidate(target: list[dict[str, Any]], candidate: Mapping[str, Any]) -> None:
    code = _clean(candidate.get("candidate_nandina"))
    if not code:
        return
    for item in target:
        if _clean(item.get("candidate_nandina")) == code:
            item["sources"] = set(item.get("sources", set())) | set(candidate.get("sources", set()))
            item["source_ranks"] = {**dict(item.get("source_ranks", {})), **dict(candidate.get("source_ranks", {}))}
            item["source_scores"] = {**dict(item.get("source_scores", {})), **dict(candidate.get("source_scores", {}))}
            if not item.get("candidate_description") and candidate.get("candidate_description"):
                item["candidate_description"] = candidate.get("candidate_description")
            if not item.get("candidate_case_id") and candidate.get("candidate_case_id"):
                item["candidate_case_id"] = candidate.get("candidate_case_id")
            if not item.get("candidate_id_unico") and candidate.get("candidate_id_unico"):
                item["candidate_id_unico"] = candidate.get("candidate_id_unico")
            return
    item = dict(candidate)
    item["sources"] = set(candidate.get("sources", set()))
    item["source_ranks"] = dict(candidate.get("source_ranks", {}))
    item["source_scores"] = dict(candidate.get("source_scores", {}))
    target.append(item)


def _append_ranked(
    output: list[dict[str, Any]],
    seen: set[str],
    candidates: Sequence[Mapping[str, Any]],
    source_limit: int | None = None,
) -> None:
    selected = candidates if source_limit is None else candidates[:source_limit]
    for candidate in selected:
        code = _clean(candidate.get("candidate_nandina"))
        if not code:
            continue
        if code in seen:
            _merge_candidate(output, candidate)
            continue
        seen.add(code)
        _merge_candidate(output, candidate)


def _renumber(candidates: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for rank, candidate in enumerate(candidates[:depth], start=1):
        item = dict(candidate)
        item["final_rank"] = rank
        output.append(item)
    return output


def _ranked(cache: Mapping[str, Any], source: str) -> list[dict[str, Any]]:
    return list(cache["sources"].get(source, []))


def _historical_then_normative(cache: Mapping[str, Any], depth: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    _append_ranked(output, seen, _ranked(cache, "historical"))
    _append_ranked(output, seen, _ranked(cache, "normative"))
    return _renumber(output, depth)


def _historical_first(cache: Mapping[str, Any], protected: int, depth: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    historical = _ranked(cache, "historical")
    normative = _ranked(cache, "normative")
    normative_slots = max(0, 100 - protected)
    _append_ranked(output, seen, historical, protected)
    _append_ranked(output, seen, normative, normative_slots)
    _append_ranked(output, seen, historical[protected:])
    _append_ranked(output, seen, normative[normative_slots:])
    return _renumber(output, depth)


def _top_historical_candidate_support(cache: Mapping[str, Any]) -> int:
    historical = _ranked(cache, "historical")
    if not historical:
        return 0
    return int(historical[0].get("candidate_historical_support_count", 0))


def _build_pool(cache: Mapping[str, Any], strategy: str, depth: int) -> tuple[list[dict[str, Any]], str]:
    if strategy == "historical_only":
        return _renumber(_ranked(cache, "historical"), depth), "historical_only_no_normative"
    if strategy == "normative_only_reference":
        return _renumber(_ranked(cache, "normative"), depth), f"normative_strategy={NORMATIVE_STRATEGY}"
    if strategy == "historical_first_90_normative_10":
        return _historical_first(cache, protected=90, depth=depth), "fixed_slots_90_historical_10_normative"
    if strategy == "historical_first_80_normative_20":
        return _historical_first(cache, protected=80, depth=depth), "fixed_slots_80_historical_20_normative"
    if strategy == "historical_first_70_normative_30":
        return _historical_first(cache, protected=70, depth=depth), "fixed_slots_70_historical_30_normative"
    if strategy == "historical_first_50_normative_50":
        return _historical_first(cache, protected=50, depth=depth), "fixed_slots_50_historical_50_normative"
    if strategy == "historical_with_normative_backfill_if_low_support":
        top_support = _top_historical_candidate_support(cache)
        if top_support < LOW_SUPPORT_THRESHOLD:
            return _historical_first(cache, protected=70, depth=depth), f"top_historical_candidate_support={top_support}<10"
        return _historical_then_normative(cache, depth=depth), f"top_historical_candidate_support={top_support}>=10"
    if strategy == "historical_with_normative_backfill_if_missing_code":
        if not _ranked(cache, "historical"):
            return _renumber(_ranked(cache, "normative"), depth), "no_historical_candidates_observed"
        return _historical_then_normative(cache, depth=depth), "historical_candidates_observed"
    raise ValueError(f"Unknown strategy: {strategy}")


def _rank_of(candidates: Sequence[Mapping[str, Any]], expected: str, prefix_len: int | None = None) -> int:
    expected_value = expected[:prefix_len] if prefix_len else expected
    for rank, candidate in enumerate(candidates, start=1):
        code = _clean(candidate.get("candidate_nandina"))
        value = code[:prefix_len] if prefix_len else code
        if value == expected_value:
            return rank
    return 0


def _source_membership(candidate: Mapping[str, Any]) -> str:
    sources = set(candidate.get("sources", set()))
    if {"historical", "normative"}.issubset(sources):
        return "both"
    if "historical" in sources:
        return "historical"
    if "normative" in sources:
        return "normative"
    return ""


def _source_rank_history(candidate: Mapping[str, Any]) -> str:
    return "|".join(f"{source}:{rank}" for source, rank in sorted(dict(candidate.get("source_ranks", {})).items()))


def _score_value(candidate: Mapping[str, Any]) -> float:
    scores = dict(candidate.get("source_scores", {}))
    if "historical" in scores:
        return float(scores["historical"])
    if "normative" in scores:
        return float(scores["normative"])
    return 0.0


def _case_summary(cache: Mapping[str, Any], strategy: str, pool: Sequence[Mapping[str, Any]], signal: str) -> dict[str, Any]:
    expected = _clean(cache["expected_nandina"])
    exact_rank = _rank_of(pool, expected)
    partida_rank = _rank_of(pool, expected, 4)
    sub_partida_rank = _rank_of(pool, expected, 6)
    clase_rank = _rank_of(pool, expected, 2)
    historical_rank = int(cache.get("historical_rank_at_200", 0))
    normative_rank = int(cache.get("normative_rank_at_200", 0))
    expected_candidate = next((candidate for candidate in pool if _clean(candidate.get("candidate_nandina")) == expected), {})
    row: dict[str, Any] = {
        "pool_strategy": strategy,
        "case_id": cache["case_id"],
        "id_unico": cache["id_unico"],
        "expected_nandina": expected,
        "expected_partida": expected[:4],
        "expected_sub_partida": expected[:6],
        "expected_clase": expected[:2],
        "query": cache["query"],
        "historical_support_count": cache["historical_support_count"],
        "support_bucket": cache["support_bucket"],
        "top_historical_candidate_support_count": _top_historical_candidate_support(cache),
        "strategy_decision_signal": signal,
        "unique_candidates": len(pool),
        "exact_rank": exact_rank,
        "partida_first_rank": partida_rank,
        "sub_partida_first_rank": sub_partida_rank,
        "clase_first_rank": clase_rank,
        "reciprocal_rank": mrr_from_rank(exact_rank),
        "historical_rank_at_100": historical_rank if 0 < historical_rank <= 100 else 0,
        "historical_rank_at_200": historical_rank,
        "normative_rank_at_100": normative_rank if 0 < normative_rank <= 100 else 0,
        "normative_rank_at_200": normative_rank,
        "expected_source_membership": _source_membership(expected_candidate),
        "rescued_vs_historical_at_100": int(exact_rank > 0 and exact_rank <= 100 and not (0 < historical_rank <= 100)),
        "lost_vs_historical_at_100": int(not (0 < exact_rank <= 100) and 0 < historical_rank <= 100),
        "rescued_vs_normative_at_100": int(exact_rank > 0 and exact_rank <= 100 and not (0 < normative_rank <= 100)),
        "lost_vs_normative_at_100": int(not (0 < exact_rank <= 100) and 0 < normative_rank <= 100),
        "normative_displaces_historical_at_100": int(exact_rank > 0 and exact_rank <= 100 and _source_membership(expected_candidate) == "normative"),
    }
    for k in K_VALUES:
        row[f"exact_at_{k}"] = int(acc_at_k(exact_rank, k))
    for k in HIERARCHICAL_K:
        row[f"partida_at_{k}"] = int(acc_at_k(partida_rank, k))
        row[f"sub_partida_at_{k}"] = int(acc_at_k(sub_partida_rank, k))
        row[f"clase_at_{k}"] = int(acc_at_k(clase_rank, k))
    return row


def _pool_rows(cache: Mapping[str, Any], strategy: str, pool: Sequence[Mapping[str, Any]], signal: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for candidate in pool:
        code = _clean(candidate.get("candidate_nandina"))
        rows.append(
            {
                "pool_strategy": strategy,
                "case_id": cache["case_id"],
                "id_unico": cache["id_unico"],
                "expected_nandina": cache["expected_nandina"],
                "candidate_rank": candidate["final_rank"],
                "candidate_nandina": code,
                "candidate_partida": code[:4],
                "candidate_sub_partida": code[:6],
                "candidate_clase": code[:2],
                "source_membership": _source_membership(candidate),
                "source_rank_history": _source_rank_history(candidate),
                "score_or_fusion_value": _score_value(candidate),
                "historical_support_count": cache["historical_support_count"],
                "support_bucket": cache["support_bucket"],
                "candidate_historical_support_count": candidate.get("candidate_historical_support_count", 0),
                "candidate_support_bucket": candidate.get("candidate_support_bucket", "0"),
                "candidate_case_id": _clean(candidate.get("candidate_case_id")),
                "candidate_id_unico": _clean(candidate.get("candidate_id_unico")),
                "candidate_description": _clean(candidate.get("candidate_description")),
                "strategy_decision_signal": signal,
                "is_expected_code": int(code == cache["expected_nandina"]),
            }
        )
    return rows


def _subset_metrics(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "cases": len(rows),
        "mrr": _mean([float(row["reciprocal_rank"]) for row in rows]),
        "median_exact_rank_nonzero": _median([float(row["exact_rank"]) for row in rows if int(row["exact_rank"]) > 0]),
    }
    for k in K_VALUES:
        payload[f"exact_at_{k}"] = _mean([float(row[f"exact_at_{k}"]) for row in rows])
    for k in HIERARCHICAL_K:
        payload[f"partida_at_{k}"] = _mean([float(row[f"partida_at_{k}"]) for row in rows])
        payload[f"sub_partida_at_{k}"] = _mean([float(row[f"sub_partida_at_{k}"]) for row in rows])
        payload[f"clase_at_{k}"] = _mean([float(row[f"clase_at_{k}"]) for row in rows])
    return payload


def _strategy_metrics(rows: Sequence[Mapping[str, Any]], strategy: str) -> dict[str, Any]:
    payload = _subset_metrics(rows)
    payload["pool_strategy"] = strategy
    payload["cases_evaluated"] = len(rows)
    payload["rescues_vs_historical_at_100"] = sum(int(row["rescued_vs_historical_at_100"]) for row in rows)
    payload["losses_vs_historical_at_100"] = sum(int(row["lost_vs_historical_at_100"]) for row in rows)
    payload["rescues_vs_normative_at_100"] = sum(int(row["rescued_vs_normative_at_100"]) for row in rows)
    payload["losses_vs_normative_at_100"] = sum(int(row["lost_vs_normative_at_100"]) for row in rows)
    payload["normative_displaces_historical_at_100"] = sum(int(row["normative_displaces_historical_at_100"]) for row in rows)
    payload["outside_top_100_cases"] = sum(1 for row in rows if not int(row["exact_at_100"]))
    payload["by_support_bucket"] = {
        bucket: _subset_metrics([row for row in rows if row["support_bucket"] == bucket])
        for bucket in ["0", "1", "2-4", "5-9", "10+"]
    }
    return payload


def _source_contribution(pool_rows: Sequence[Mapping[str, Any]], case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    expected_source = {
        (row["pool_strategy"], row["case_id"]): row["expected_source_membership"]
        for row in case_rows
        if int(row["exact_at_100"])
    }
    grouped_candidates: dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in pool_rows:
        grouped_candidates[(row["pool_strategy"], row["source_membership"])].append(row)
    output: list[dict[str, Any]] = []
    for strategy in STRATEGIES:
        for source in ["historical", "normative", "both"]:
            candidate_rows = grouped_candidates.get((strategy, source), [])
            exact_rows = [
                row
                for row in candidate_rows
                if row["candidate_nandina"] == row["expected_nandina"] and int(row["candidate_rank"]) <= 100
            ]
            expected_hits = sum(1 for key, membership in expected_source.items() if key[0] == strategy and membership == source)
            output.append(
                {
                    "pool_strategy": strategy,
                    "source_membership": source,
                    "candidate_rows": len(candidate_rows),
                    "exact_candidate_rows_at_100": len(exact_rows),
                    "cases_where_expected_source_at_100": expected_hits,
                }
            )
    return output


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _check_input_metrics(args: argparse.Namespace, evalset_path: Path, historical_path: Path) -> dict[str, Any]:
    historical_metrics_path = resolve_project_path(args.historical_metrics)
    normative_metrics_path = resolve_project_path(args.normative_metrics)
    historical_payload = _load_json(historical_metrics_path)
    normative_payload = _load_json(normative_metrics_path)
    eval_sha = sha256_file(evalset_path)
    historical_sha = sha256_file(historical_path)
    if historical_payload.get("inputs", {}).get("evalset_sha256") != eval_sha:
        raise ValueError("Historical 9A metrics evalset checksum does not match current evalset.")
    if historical_payload.get("inputs", {}).get("historical_sha256") != historical_sha:
        raise ValueError("Historical 9A metrics historical checksum does not match current historical split.")
    if normative_payload.get("input", {}).get("evalset_sha256") != eval_sha:
        raise ValueError("Normative 7A metrics evalset checksum does not match current evalset.")
    return {
        "historical_metrics": historical_payload,
        "normative_metrics": normative_payload,
    }


def _load_caches(args: argparse.Namespace) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    root = project_root()
    historical_path = resolve_project_path(args.historical)
    evalset_path = resolve_project_path(args.evalset)
    historical_rows = _read_csv(historical_path)
    eval_rows = _read_csv(evalset_path)
    _validate_split(historical_rows, EXPECTED_HISTORICAL_ROWS, "historical")
    _validate_split(eval_rows, EXPECTED_EVAL_ROWS, "evalset")
    overlap_count = _validate_no_overlap(historical_rows, eval_rows)
    input_payloads = _check_input_metrics(args, evalset_path, historical_path)
    support_counts = Counter(_clean(row.get(LABEL_COLUMN)) for row in historical_rows)

    caches_by_case: dict[str, dict[str, Any]] = {}
    for position, row in enumerate(eval_rows, start=1):
        case_id = _clean(row.get("case_id")) or f"DA-EVAL-{position:05d}"
        expected = _clean(row.get(LABEL_COLUMN))
        support_count = int(support_counts.get(expected, 0))
        caches_by_case[case_id] = {
            "case_id": case_id,
            "id_unico": _clean(row.get("id_unico")),
            "expected_nandina": expected,
            "query": _clean(row.get(QUERY_COLUMN)),
            "historical_support_count": support_count,
            "support_bucket": _support_bucket(support_count),
            "sources": defaultdict(list),
            "historical_rank_at_200": 0,
            "normative_rank_at_200": 0,
        }

    for row in _iter_csv(resolve_project_path(args.historical_results)):
        if _clean(row.get("method")) != HISTORICAL_METHOD:
            continue
        case_id = _clean(row.get("case_id"))
        if case_id not in caches_by_case:
            continue
        code = _clean(row.get("candidate_nandina"))
        rank = int(_clean(row.get("candidate_rank")) or "0")
        caches_by_case[case_id]["sources"]["historical"].append(
            _candidate(
                code=code,
                source="historical",
                rank=rank,
                score=float(_clean(row.get("score")) or 0.0),
                evidence_text=_clean(row.get("candidate_description")),
                candidate_case_id=_clean(row.get("candidate_case_id")),
                candidate_id_unico=_clean(row.get("candidate_id_unico")),
                candidate_support_count=int(support_counts.get(code, 0)),
            )
        )
        if code == caches_by_case[case_id]["expected_nandina"] and not caches_by_case[case_id]["historical_rank_at_200"]:
            caches_by_case[case_id]["historical_rank_at_200"] = rank

    for row in _iter_csv(resolve_project_path(args.normative_pool)):
        if _clean(row.get("pool_strategy")) != NORMATIVE_STRATEGY:
            continue
        case_id = _clean(row.get("case_id"))
        if case_id not in caches_by_case:
            continue
        code = _clean(row.get("candidate_code"))
        rank = int(_clean(row.get("candidate_rank_pool")) or "0")
        score = _clean(row.get("hierarchical_score")) or _clean(row.get("dual_score")) or "0"
        caches_by_case[case_id]["sources"]["normative"].append(
            _candidate(
                code=code,
                source="normative",
                rank=rank,
                score=float(score or 0.0),
                evidence_text=_clean(row.get("evidence_text")),
                candidate_support_count=int(support_counts.get(code, 0)),
            )
        )
        if code == caches_by_case[case_id]["expected_nandina"] and not caches_by_case[case_id]["normative_rank_at_200"]:
            caches_by_case[case_id]["normative_rank_at_200"] = rank

    for cache in caches_by_case.values():
        for source, rows in cache["sources"].items():
            rows.sort(key=lambda item: int(item["source_ranks"][source]))
        if not cache["sources"].get("historical"):
            raise ValueError(f"Case without historical candidates: {cache['case_id']}")
    cases_without_normative_candidates = sum(1 for cache in caches_by_case.values() if not cache["sources"].get("normative"))

    metadata = {
        "historical_rows": len(historical_rows),
        "eval_rows": len(eval_rows),
        "id_unico_overlap_count": overlap_count,
        "historical_sha256": sha256_file(historical_path),
        "evalset_sha256": sha256_file(evalset_path),
        "historical_results_sha256": sha256_file(resolve_project_path(args.historical_results)),
        "historical_case_summary_sha256": sha256_file(resolve_project_path(args.historical_case_summary)),
        "normative_pool_sha256": sha256_file(resolve_project_path(args.normative_pool)),
        "historical_metrics_sha256": sha256_file(resolve_project_path(args.historical_metrics)),
        "normative_metrics_sha256": sha256_file(resolve_project_path(args.normative_metrics)),
        "cases_without_normative_candidates": cases_without_normative_candidates,
        "historical_metrics": input_payloads["historical_metrics"]["metrics"],
        "normative_metrics_by_strategy": input_payloads["normative_metrics"]["metrics_by_strategy"],
        "paths": {
            "historical": _rel(historical_path, root),
            "evalset": _rel(evalset_path, root),
            "historical_results": _rel(resolve_project_path(args.historical_results), root),
            "historical_case_summary": _rel(resolve_project_path(args.historical_case_summary), root),
            "historical_metrics": _rel(resolve_project_path(args.historical_metrics), root),
            "normative_pool": _rel(resolve_project_path(args.normative_pool), root),
            "normative_metrics": _rel(resolve_project_path(args.normative_metrics), root),
        },
    }
    return list(caches_by_case.values()), metadata


def _comparison_table(metrics_by_strategy: Mapping[str, Mapping[str, Any]]) -> list[dict[str, Any]]:
    keys = [
        "pool_strategy",
        "exact_at_1",
        "exact_at_3",
        "exact_at_5",
        "exact_at_10",
        "exact_at_20",
        "exact_at_50",
        "exact_at_100",
        "exact_at_200",
        "mrr",
        "rescues_vs_historical_at_100",
        "losses_vs_historical_at_100",
        "outside_top_100_cases",
    ]
    return [{key: metrics.get(key, "") for key in keys} for metrics in metrics_by_strategy.values()]


def _select_strategy(metrics_by_strategy: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    historical = metrics_by_strategy["historical_only"]
    operational = [metrics_by_strategy[strategy] for strategy in STRATEGIES if strategy != "normative_only_reference"]
    non_degrading = [
        row
        for row in operational
        if float(row["exact_at_1"]) >= float(historical["exact_at_1"])
        and float(row["exact_at_10"]) >= float(historical["exact_at_10"])
        and float(row["mrr"]) >= float(historical["mrr"])
        and float(row["exact_at_100"]) >= float(historical["exact_at_100"])
    ]
    backfill_name = "historical_with_normative_backfill_if_missing_code"
    backfill = metrics_by_strategy[backfill_name]
    if (
        backfill in non_degrading
        and float(backfill["exact_at_100"]) == float(historical["exact_at_100"])
        and float(backfill["exact_at_200"]) >= float(historical["exact_at_200"])
    ):
        selected = dict(backfill)
        selected["selection_reason"] = (
            "Seleccion operativa: conserva el ranking historico como orden principal, no degrada Top-1, "
            "Top-10, Top-100 ni MRR, y agrega backfill normativo posterior para trazabilidad y robustez futura."
        )
        return selected
    if non_degrading:
        non_degrading.sort(
            key=lambda row: (
                float(row["exact_at_100"]),
                float(row["exact_at_20"]),
                float(row["mrr"]),
                -int(row["losses_vs_historical_at_100"]),
            ),
            reverse=True,
        )
        selected = dict(non_degrading[0])
        selected["selection_reason"] = (
            "Seleccion operativa: no degrada Top-1, Top-10 ni MRR frente al historico solo, "
            "mantiene o mejora Recall@100 y agrega backfill normativo trazable."
        )
        return selected
    selected = dict(historical)
    selected["selection_reason"] = (
        "Ningun hibrido mejora sin degradar el ranking temprano; historico solo queda como ranking operativo "
        "principal y lo normativo se reserva como backfill/trazabilidad."
    )
    return selected


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Pool hibrido data_aduanas clase 87 v0.1",
        "",
        "## Metricas principales",
        "",
        "| Estrategia | @1 | @10 | @20 | @50 | @100 | @200 | MRR | Rescates vs historico@100 | Perdidas vs historico@100 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in payload["comparison_table"]:
        lines.append(
            f"| `{row['pool_strategy']}` | {row['exact_at_1']:.4f} | {row['exact_at_10']:.4f} | "
            f"{row['exact_at_20']:.4f} | {row['exact_at_50']:.4f} | {row['exact_at_100']:.4f} | "
            f"{row['exact_at_200']:.4f} | {row['mrr']:.4f} | {row['rescues_vs_historical_at_100']} | "
            f"{row['losses_vs_historical_at_100']} |"
        )
    selected = payload["selected_strategy"]
    lines.extend(
        [
            "",
            "## Decision",
            "",
            f"Estrategia recomendada: `{selected['pool_strategy']}`.",
            selected["selection_reason"],
            "",
            "No se uso LLM, Ollama, Text2Trade, Dense, OpenAI ni APIs remotas.",
            "",
        ]
    )
    return "\n".join(lines)


def build(args: argparse.Namespace) -> dict[str, Any]:
    start = time.perf_counter()
    root = project_root()
    output_dir = resolve_project_path(args.output_dir)
    depth = int(args.depth)
    if depth < max(K_VALUES):
        raise ValueError(f"--depth must be at least {max(K_VALUES)}")
    caches, metadata = _load_caches(args)
    if len(caches) != EXPECTED_EVAL_ROWS:
        raise ValueError(f"Expected {EXPECTED_EVAL_ROWS} caches, found {len(caches)}")

    all_pool_rows: list[dict[str, Any]] = []
    all_case_rows: list[dict[str, Any]] = []
    metrics_by_strategy: dict[str, dict[str, Any]] = {}
    for strategy in STRATEGIES:
        strategy_case_rows: list[dict[str, Any]] = []
        for cache in caches:
            pool, signal = _build_pool(cache, strategy, depth=depth)
            all_pool_rows.extend(_pool_rows(cache, strategy, pool, signal))
            strategy_case_rows.append(_case_summary(cache, strategy, pool, signal))
        all_case_rows.extend(strategy_case_rows)
        metrics_by_strategy[strategy] = _strategy_metrics(strategy_case_rows, strategy)

    selected_strategy = _select_strategy(metrics_by_strategy)
    selected_name = selected_strategy["pool_strategy"]
    selected_rows = [row for row in all_case_rows if row["pool_strategy"] == selected_name]
    rescue_loss_rows = [
        row
        for row in selected_rows
        if int(row["rescued_vs_historical_at_100"])
        or int(row["lost_vs_historical_at_100"])
        or int(row["rescued_vs_normative_at_100"])
        or int(row["lost_vs_normative_at_100"])
    ]
    low_support_rows = [row for row in selected_rows if row["support_bucket"] in {"0", "1", "2-4", "5-9"}]
    source_rows = _source_contribution(all_pool_rows, all_case_rows)

    payload: dict[str, Any] = {
        "version": "v0.1",
        "phase": "9B_data_aduanas_clase87",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": platform.python_version(), "platform": platform.platform()},
        "inputs": metadata["paths"],
        "input_sha256": {
            key: value
            for key, value in metadata.items()
            if key.endswith("_sha256")
        },
        "input_rows": {"historical": metadata["historical_rows"], "evalset": metadata["eval_rows"]},
        "validation": {
            "id_unico_overlap_count": metadata["id_unico_overlap_count"],
            "cases_without_normative_candidates": metadata["cases_without_normative_candidates"],
            "queries_non_empty": True,
            "nandina8_labels_valid": True,
            "strategy_decision_uses_expected_label": False,
            "llm_used": False,
            "ollama_used": False,
            "text2trade_used": False,
            "dense_used": False,
            "openai_used": False,
            "remote_api_used": False,
            "outputs_versioned": False,
        },
        "parameters": {
            "candidate_depth": depth,
            "k_values": K_VALUES,
            "hierarchical_k": HIERARCHICAL_K,
            "strategies": STRATEGIES,
            "historical_method": HISTORICAL_METHOD,
            "normative_strategy": NORMATIVE_STRATEGY,
            "low_support_rule": "top historical candidate NANDINA support in historical bank < 10",
            "missing_code_rule": "if no historical candidates are observed, use normative first; otherwise append normative after historical",
        },
        "baseline_reference": {
            "phase9a_historical": {
                "exact_at_1": metadata["historical_metrics"]["exact_at_1"],
                "exact_at_10": metadata["historical_metrics"]["exact_at_10"],
                "exact_at_100": metadata["historical_metrics"]["exact_at_100"],
                "mrr": metadata["historical_metrics"]["mrr"],
            },
            "phase7a_normative": {
                "strategy": NORMATIVE_STRATEGY,
                "final_pool_at_100": metadata["normative_metrics_by_strategy"][NORMATIVE_STRATEGY]["final_pool_at_100"],
                "final_pool_at_200": metadata["normative_metrics_by_strategy"][NORMATIVE_STRATEGY]["final_pool_at_200"],
            },
        },
        "metrics_by_strategy": metrics_by_strategy,
        "comparison_table": _comparison_table(metrics_by_strategy),
        "selected_strategy": selected_strategy,
        "historical_failure_watchlist": [
            row
            for row in all_case_rows
            if row["pool_strategy"] == selected_name and row["expected_nandina"] in {"87089911", "87089950"}
        ],
        "outputs": {
            "hybrid_pool_csv": _rel(output_dir / "hybrid_pool.csv", root),
            "hybrid_case_summary_csv": _rel(output_dir / "hybrid_case_summary.csv", root),
            "hybrid_metrics_json": _rel(output_dir / "hybrid_metrics.json", root),
            "hybrid_summary_md": _rel(output_dir / "hybrid_summary.md", root),
            "hybrid_source_contribution_csv": _rel(output_dir / "hybrid_source_contribution.csv", root),
            "hybrid_rescue_loss_cases_csv": _rel(output_dir / "hybrid_rescue_loss_cases.csv", root),
            "hybrid_low_support_cases_csv": _rel(output_dir / "hybrid_low_support_cases.csv", root),
        },
        "elapsed_seconds": time.perf_counter() - start,
    }

    pool_fieldnames = [
        "pool_strategy",
        "case_id",
        "id_unico",
        "expected_nandina",
        "candidate_rank",
        "candidate_nandina",
        "candidate_partida",
        "candidate_sub_partida",
        "candidate_clase",
        "source_membership",
        "source_rank_history",
        "score_or_fusion_value",
        "historical_support_count",
        "support_bucket",
        "candidate_historical_support_count",
        "candidate_support_bucket",
        "candidate_case_id",
        "candidate_id_unico",
        "candidate_description",
        "strategy_decision_signal",
        "is_expected_code",
    ]
    case_fieldnames = [
        "pool_strategy",
        "case_id",
        "id_unico",
        "expected_nandina",
        "expected_partida",
        "expected_sub_partida",
        "expected_clase",
        "query",
        "historical_support_count",
        "support_bucket",
        "top_historical_candidate_support_count",
        "strategy_decision_signal",
        "unique_candidates",
        "exact_rank",
        "partida_first_rank",
        "sub_partida_first_rank",
        "clase_first_rank",
        "reciprocal_rank",
        "historical_rank_at_100",
        "historical_rank_at_200",
        "normative_rank_at_100",
        "normative_rank_at_200",
        "expected_source_membership",
        "rescued_vs_historical_at_100",
        "lost_vs_historical_at_100",
        "rescued_vs_normative_at_100",
        "lost_vs_normative_at_100",
        "normative_displaces_historical_at_100",
        *[f"exact_at_{k}" for k in K_VALUES],
        *[f"partida_at_{k}" for k in HIERARCHICAL_K],
        *[f"sub_partida_at_{k}" for k in HIERARCHICAL_K],
        *[f"clase_at_{k}" for k in HIERARCHICAL_K],
    ]
    source_fieldnames = [
        "pool_strategy",
        "source_membership",
        "candidate_rows",
        "exact_candidate_rows_at_100",
        "cases_where_expected_source_at_100",
    ]

    _write_csv(output_dir / "hybrid_pool.csv", all_pool_rows, pool_fieldnames)
    _write_csv(output_dir / "hybrid_case_summary.csv", all_case_rows, case_fieldnames)
    _write_csv(output_dir / "hybrid_source_contribution.csv", source_rows, source_fieldnames)
    _write_csv(output_dir / "hybrid_rescue_loss_cases.csv", rescue_loss_rows, case_fieldnames)
    _write_csv(output_dir / "hybrid_low_support_cases.csv", low_support_rows, case_fieldnames)
    _write_json(output_dir / "hybrid_metrics.json", payload)
    ensure_parent(output_dir / "hybrid_summary.md").write_text(_summary_markdown(payload), encoding="utf-8")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build hybrid historical + normative pools for data_aduanas class 87.")
    parser.add_argument("--historical", default=str(DEFAULT_HISTORICAL))
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET))
    parser.add_argument("--historical-results", default=str(DEFAULT_HISTORICAL_RESULTS))
    parser.add_argument("--historical-case-summary", default=str(DEFAULT_HISTORICAL_CASE_SUMMARY))
    parser.add_argument("--historical-metrics", default=str(DEFAULT_HISTORICAL_METRICS))
    parser.add_argument("--normative-pool", default=str(DEFAULT_NORMATIVE_POOL))
    parser.add_argument("--normative-metrics", default=str(DEFAULT_NORMATIVE_METRICS))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--depth", type=int, default=200)
    return parser


def main() -> int:
    payload = build(build_parser().parse_args())
    print(f"OK: pool hibrido data_aduanas clase 87 construido en {payload['outputs']['hybrid_metrics_json']}")
    for row in payload["comparison_table"]:
        print(
            f"{row['pool_strategy']}: @1={row['exact_at_1']:.4f} @10={row['exact_at_10']:.4f} "
            f"@100={row['exact_at_100']:.4f} @200={row['exact_at_200']:.4f} MRR={row['mrr']:.4f} "
            f"rescues={row['rescues_vs_historical_at_100']} losses={row['losses_vs_historical_at_100']}"
        )
    print(f"Seleccion: {payload['selected_strategy']['pool_strategy']}")
    print(payload["selected_strategy"]["selection_reason"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
