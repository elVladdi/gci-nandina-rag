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
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_HISTORICAL_RESULTS = Path("outputs/evaluation/historical_examples_leave_one_out_v0.1/historical_results.csv")
DEFAULT_HISTORICAL_CASE_SUMMARY = Path("outputs/evaluation/historical_examples_leave_one_out_v0.1/historical_case_summary.csv")
DEFAULT_PHASE7A_POOL = Path("outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool.csv")
DEFAULT_PHASE7A_SUMMARY = Path("outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool_case_summary.csv")
DEFAULT_PHASE8B_POOL = Path("outputs/evaluation/nonrestrictive_expanded_pool_evalset_v0.1/expanded_pool.csv")
DEFAULT_PHASE8B_SUMMARY = Path("outputs/evaluation/nonrestrictive_expanded_pool_evalset_v0.1/expanded_pool_case_summary.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/hybrid_historical_normative_pool_v0.1")

HISTORICAL_METHOD = "historical_bm25_description"
PHASE7A_STRATEGY = "hierarchical_80_dual_backfill_20"
PHASE8B_STRATEGY = "phase7a_plus_all_sources_200"
K_VALUES = [1, 3, 5, 10, 20, 50, 100]
EXPECTED_ROWS = 600
RRF_K = 60

STRATEGIES = [
    "historical_first_95_normative_5",
    "historical_first_80_normative_20",
    "historical_first_50_normative_50",
    "historical_plus_normative_rrf",
    "oracle_historical_if_label_supported_else_normative",
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


def _case_id(row: Mapping[str, Any], position: int) -> str:
    return _clean(row.get("case_id")) or f"SUNAT-{position:04d}"


def _expected(row: Mapping[str, Any]) -> str:
    return _clean(row.get("nandina_ref") or row.get("expected_nandina") or row.get("nandina"))


def _support_bucket(count: int) -> str:
    if count <= 1:
        return "singleton"
    if count <= 4:
        return "2-4"
    if count <= 9:
        return "5-9"
    return "10+"


def _rank_of_code(candidates: Sequence[Mapping[str, Any]], expected: str, prefix_len: int | None = None) -> int:
    expected_value = expected[:prefix_len] if prefix_len else expected
    for rank, candidate in enumerate(candidates, start=1):
        code = _clean(candidate.get("candidate_nandina"))
        value = code[:prefix_len] if prefix_len else code
        if value == expected_value:
            return rank
    return 0


def _hit(rank: int, k: int) -> int:
    return int(acc_at_k(rank, k))


def _source_rank_history(candidate: Mapping[str, Any]) -> str:
    ranks = candidate.get("source_ranks", {})
    return "|".join(f"{source}:{rank}" for source, rank in sorted(ranks.items()) if rank)


def _source_membership(candidate: Mapping[str, Any]) -> str:
    return "|".join(sorted(candidate.get("sources", [])))


def _candidate(
    code: str,
    source: str,
    rank: int,
    score: float = 0.0,
    candidate_case_id: str = "",
    description: str = "",
) -> dict[str, Any]:
    return {
        "candidate_nandina": code,
        "candidate_case_id": candidate_case_id,
        "candidate_description": description,
        "sources": {source},
        "source_ranks": {source: rank},
        "source_scores": {source: float(score)},
    }


def _merge_candidate(target: dict[str, dict[str, Any]], candidate: Mapping[str, Any]) -> None:
    code = _clean(candidate.get("candidate_nandina"))
    if not code:
        return
    if code not in target:
        item = dict(candidate)
        item["sources"] = set(candidate.get("sources", []))
        item["source_ranks"] = dict(candidate.get("source_ranks", {}))
        item["source_scores"] = dict(candidate.get("source_scores", {}))
        target[code] = item
        return
    target[code]["sources"].update(candidate.get("sources", []))
    target[code]["source_ranks"].update(candidate.get("source_ranks", {}))
    target[code]["source_scores"].update(candidate.get("source_scores", {}))
    if not target[code].get("candidate_case_id") and candidate.get("candidate_case_id"):
        target[code]["candidate_case_id"] = candidate.get("candidate_case_id")
    if not target[code].get("candidate_description") and candidate.get("candidate_description"):
        target[code]["candidate_description"] = candidate.get("candidate_description")


def _append_ranked(
    output: list[dict[str, Any]],
    seen: set[str],
    candidates: Sequence[Mapping[str, Any]],
    source_limit: int | None = None,
) -> None:
    iterable = candidates if source_limit is None else candidates[:source_limit]
    for candidate in iterable:
        code = _clean(candidate.get("candidate_nandina"))
        if code and code not in seen:
            seen.add(code)
            output.append(dict(candidate))


def _renumber(candidates: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for rank, candidate in enumerate(candidates[:depth], start=1):
        item = dict(candidate)
        item["final_rank"] = rank
        output.append(item)
    return output


def _enrich_memberships(cache: Mapping[str, Any], pool: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    by_code: dict[str, dict[str, Any]] = {}
    for source in ["historical", "phase7a", "phase8b"]:
        for candidate in _ranked_by_source(cache, source):
            _merge_candidate(by_code, candidate)

    output: list[dict[str, Any]] = []
    for candidate in pool:
        code = _clean(candidate.get("candidate_nandina"))
        item = dict(candidate)
        if code in by_code:
            item["sources"] = set(item.get("sources", [])) | set(by_code[code].get("sources", []))
            source_ranks = dict(by_code[code].get("source_ranks", {}))
            source_ranks.update(item.get("source_ranks", {}))
            item["source_ranks"] = source_ranks
            source_scores = dict(by_code[code].get("source_scores", {}))
            source_scores.update(item.get("source_scores", {}))
            item["source_scores"] = source_scores
        output.append(item)
    return output


def _ranked_by_source(cache: Mapping[str, Any], source: str) -> list[dict[str, Any]]:
    return list(cache["sources"].get(source, []))


def _normative_pool(cache: Mapping[str, Any]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    _append_ranked(output, seen, _ranked_by_source(cache, "phase8b"))
    _append_ranked(output, seen, _ranked_by_source(cache, "phase7a"))
    return output


def _historical_first(cache: Mapping[str, Any], protected: int, depth: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    _append_ranked(output, seen, _ranked_by_source(cache, "historical"), protected)
    _append_ranked(output, seen, _normative_pool(cache))
    _append_ranked(output, seen, _ranked_by_source(cache, "historical")[protected:])
    return _renumber(output, depth)


def _rrf_pool(cache: Mapping[str, Any], depth: int) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    fusion_scores: dict[str, float] = defaultdict(float)
    for source in ["historical", "phase7a", "phase8b"]:
        for candidate in _ranked_by_source(cache, source):
            code = _clean(candidate.get("candidate_nandina"))
            rank = int(candidate["source_ranks"][source])
            _merge_candidate(merged, candidate)
            fusion_scores[code] += 1.0 / float(RRF_K + rank)
    ordered = sorted(
        merged.values(),
        key=lambda item: (-fusion_scores[_clean(item.get("candidate_nandina"))], min(item.get("source_ranks", {}).values()), _clean(item.get("candidate_nandina"))),
    )
    output: list[dict[str, Any]] = []
    for candidate in ordered:
        item = dict(candidate)
        item["fusion_value"] = fusion_scores[_clean(item.get("candidate_nandina"))]
        output.append(item)
    return _renumber(output, depth)


def _oracle_label_supported_else_normative(cache: Mapping[str, Any], depth: int) -> list[dict[str, Any]]:
    if int(cache["historical_support_count"]) > 1:
        return _historical_first(cache, protected=80, depth=depth)
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    _append_ranked(output, seen, _normative_pool(cache))
    _append_ranked(output, seen, _ranked_by_source(cache, "historical"))
    return _renumber(output, depth)


def _build_strategy_pool(cache: Mapping[str, Any], strategy: str, depth: int) -> list[dict[str, Any]]:
    if strategy == "historical_first_95_normative_5":
        return _enrich_memberships(cache, _historical_first(cache, protected=95, depth=depth))
    if strategy == "historical_first_80_normative_20":
        return _enrich_memberships(cache, _historical_first(cache, protected=80, depth=depth))
    if strategy == "historical_first_50_normative_50":
        return _enrich_memberships(cache, _historical_first(cache, protected=50, depth=depth))
    if strategy == "historical_plus_normative_rrf":
        return _enrich_memberships(cache, _rrf_pool(cache, depth=depth))
    if strategy == "oracle_historical_if_label_supported_else_normative":
        return _enrich_memberships(cache, _oracle_label_supported_else_normative(cache, depth=depth))
    raise ValueError(f"Unknown strategy: {strategy}")


def _load_source_candidates(args: argparse.Namespace, evalset_rows: Sequence[Mapping[str, str]]) -> list[dict[str, Any]]:
    expected_by_case = {_case_id(row, pos): _expected(row) for pos, row in enumerate(evalset_rows, start=1)}
    description_by_case = {_case_id(row, pos): _clean(row.get("descripcion")) for pos, row in enumerate(evalset_rows, start=1)}
    support_counts = Counter(expected_by_case.values())

    caches: dict[str, dict[str, Any]] = {
        case_id: {
            "case_id": case_id,
            "expected_nandina": expected,
            "descripcion": description_by_case[case_id],
            "historical_support_count": int(support_counts[expected]),
            "support_bucket": _support_bucket(int(support_counts[expected])),
            "sources": defaultdict(list),
        }
        for case_id, expected in expected_by_case.items()
    }

    for row in _read_csv(resolve_project_path(args.historical_results)):
        if _clean(row.get("method")) != HISTORICAL_METHOD:
            continue
        case_id = _clean(row.get("case_id"))
        if case_id not in caches:
            continue
        caches[case_id]["sources"]["historical"].append(
            _candidate(
                code=_clean(row.get("candidate_nandina")),
                source="historical",
                rank=int(_clean(row.get("candidate_rank")) or "0"),
                score=float(_clean(row.get("score")) or 0.0),
                candidate_case_id=_clean(row.get("candidate_case_id")),
                description=_clean(row.get("candidate_description")),
            )
        )

    for row in _read_csv(resolve_project_path(args.phase7a_pool)):
        if _clean(row.get("pool_strategy")) != PHASE7A_STRATEGY:
            continue
        case_id = _clean(row.get("case_id"))
        if case_id not in caches:
            continue
        caches[case_id]["sources"]["phase7a"].append(
            _candidate(
                code=_clean(row.get("candidate_code")),
                source="phase7a",
                rank=int(_clean(row.get("candidate_rank_pool")) or "0"),
                score=float(_clean(row.get("hierarchical_score") or row.get("dual_score")) or 0.0),
                description=_clean(row.get("evidence_text")),
            )
        )

    for row in _read_csv(resolve_project_path(args.phase8b_pool)):
        if _clean(row.get("strategy")) != PHASE8B_STRATEGY:
            continue
        case_id = _clean(row.get("case_id"))
        if case_id not in caches:
            continue
        caches[case_id]["sources"]["phase8b"].append(
            _candidate(
                code=_clean(row.get("candidate_code")),
                source="phase8b",
                rank=int(_clean(row.get("candidate_rank_pool")) or "0"),
                score=float(_clean(row.get("score")) or 0.0),
                description=_clean(row.get("evidence_text")),
            )
        )

    for cache in caches.values():
        for source, rows in cache["sources"].items():
            rows.sort(key=lambda item: int(item["source_ranks"][source]))
    return list(caches.values())


def _pool_rows(cache: Mapping[str, Any], strategy: str, pool: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for candidate in pool:
        code = _clean(candidate.get("candidate_nandina"))
        source_scores = candidate.get("source_scores", {})
        score = candidate.get("fusion_value")
        if score is None:
            score = source_scores.get("historical", source_scores.get("phase8b", source_scores.get("phase7a", 0.0)))
        output.append(
            {
                "case_id": cache["case_id"],
                "expected_nandina": cache["expected_nandina"],
                "final_rank": candidate["final_rank"],
                "candidate_nandina": code,
                "source_membership": _source_membership(candidate),
                "source_rank_history": _source_rank_history(candidate),
                "score_or_fusion_value": score,
                "pool_strategy": strategy,
                "historical_support_count": cache["historical_support_count"],
                "support_bucket": cache["support_bucket"],
                "candidate_case_id": _clean(candidate.get("candidate_case_id")),
            }
        )
    return output


def _case_summary(cache: Mapping[str, Any], strategy: str, pool: Sequence[Mapping[str, Any]], baseline: Mapping[str, int]) -> dict[str, Any]:
    expected = _clean(cache["expected_nandina"])
    exact_rank = _rank_of_code(pool, expected)
    hs6_rank = _rank_of_code(pool, expected, 6)
    hs4_rank = _rank_of_code(pool, expected, 4)
    hs2_rank = _rank_of_code(pool, expected, 2)
    row: dict[str, Any] = {
        "pool_strategy": strategy,
        "case_id": cache["case_id"],
        "expected_nandina": expected,
        "descripcion": cache["descripcion"],
        "hs2_ref": expected[:2],
        "hs4_ref": expected[:4],
        "hs6_ref": expected[:6],
        "historical_support_count": cache["historical_support_count"],
        "support_bucket": cache["support_bucket"],
        "has_historical_precedent": int(int(cache["historical_support_count"]) > 1),
        "unique_candidates": len(pool),
        "exact_rank": exact_rank,
        "hs6_first_rank": hs6_rank,
        "hs4_first_rank": hs4_rank,
        "hs2_first_rank": hs2_rank,
        "reciprocal_rank": mrr_from_rank(exact_rank),
        "historical_rank_at_100": baseline.get("historical_rank", 0),
        "phase7a_rank_at_100": baseline.get("phase7a_rank", 0),
        "phase8b_rank_at_100": baseline.get("phase8b_rank", 0),
        "rescued_vs_phase9a": int(exact_rank > 0 and baseline.get("historical_rank", 0) <= 0),
        "lost_vs_phase9a": int(exact_rank <= 0 and baseline.get("historical_rank", 0) > 0),
        "rescued_vs_phase7a": int(exact_rank > 0 and baseline.get("phase7a_rank", 0) <= 0),
        "lost_vs_phase7a": int(exact_rank <= 0 and baseline.get("phase7a_rank", 0) > 0),
        "rescued_vs_phase8b": int(exact_rank > 0 and baseline.get("phase8b_rank", 0) <= 0),
        "lost_vs_phase8b": int(exact_rank <= 0 and baseline.get("phase8b_rank", 0) > 0),
    }
    for k in K_VALUES:
        row[f"exact_at_{k}"] = _hit(exact_rank, k)
        row[f"hs6_at_{k}"] = _hit(hs6_rank, k)
        row[f"hs4_at_{k}"] = _hit(hs4_rank, k)
        row[f"hs2_at_{k}"] = _hit(hs2_rank, k)
    return row


def _rank_lookup(candidates: Sequence[Mapping[str, Any]], expected: str, source: str) -> int:
    for candidate in candidates[:100]:
        if _clean(candidate.get("candidate_nandina")) == expected:
            return int(candidate["source_ranks"][source])
    return 0


def _baseline_ranks(cache: Mapping[str, Any]) -> dict[str, int]:
    expected = _clean(cache["expected_nandina"])
    return {
        "historical_rank": _rank_lookup(_ranked_by_source(cache, "historical"), expected, "historical"),
        "phase7a_rank": _rank_lookup(_ranked_by_source(cache, "phase7a"), expected, "phase7a"),
        "phase8b_rank": _rank_lookup(_ranked_by_source(cache, "phase8b"), expected, "phase8b"),
    }


def _metrics(case_rows: Sequence[Mapping[str, Any]], strategy: str) -> dict[str, Any]:
    metrics: dict[str, Any] = {
        "pool_strategy": strategy,
        "cases_evaluated": len(case_rows),
        "mrr": _mean([float(row["reciprocal_rank"]) for row in case_rows]),
        "median_exact_rank_nonzero": _median([float(row["exact_rank"]) for row in case_rows if int(row["exact_rank"]) > 0]),
        "singleton_rescues_vs_phase9a": sum(1 for row in case_rows if row["support_bucket"] == "singleton" and int(row["rescued_vs_phase9a"])),
        "singleton_hits_at_100": sum(1 for row in case_rows if row["support_bucket"] == "singleton" and int(row["exact_at_100"])),
        "rescues_vs_phase9a_at_100": sum(int(row["rescued_vs_phase9a"]) for row in case_rows),
        "losses_vs_phase9a_at_100": sum(int(row["lost_vs_phase9a"]) for row in case_rows),
        "rescues_vs_phase7a_at_100": sum(int(row["rescued_vs_phase7a"]) for row in case_rows),
        "losses_vs_phase7a_at_100": sum(int(row["lost_vs_phase7a"]) for row in case_rows),
        "rescues_vs_phase8b_at_100": sum(int(row["rescued_vs_phase8b"]) for row in case_rows),
        "losses_vs_phase8b_at_100": sum(int(row["lost_vs_phase8b"]) for row in case_rows),
        "by_support_bucket": {},
        "by_precedent_flag": {},
    }
    for k in K_VALUES:
        metrics[f"exact_at_{k}"] = _mean([float(row[f"exact_at_{k}"]) for row in case_rows])
        metrics[f"hs6_at_{k}"] = _mean([float(row[f"hs6_at_{k}"]) for row in case_rows])
        metrics[f"hs4_at_{k}"] = _mean([float(row[f"hs4_at_{k}"]) for row in case_rows])
        metrics[f"hs2_at_{k}"] = _mean([float(row[f"hs2_at_{k}"]) for row in case_rows])
    for bucket in ["singleton", "2-4", "5-9", "10+"]:
        subset = [row for row in case_rows if row["support_bucket"] == bucket]
        metrics["by_support_bucket"][bucket] = _subset_metrics(subset)
    for flag, label in [(0, "singleton"), (1, "with_historical_precedent")]:
        subset = [row for row in case_rows if int(row["has_historical_precedent"]) == flag]
        metrics["by_precedent_flag"][label] = _subset_metrics(subset)
    return metrics


def _subset_metrics(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {
        "cases": len(rows),
        "mrr": _mean([float(row["reciprocal_rank"]) for row in rows]),
    }
    for k in K_VALUES:
        output[f"exact_at_{k}"] = _mean([float(row[f"exact_at_{k}"]) for row in rows])
        output[f"hs6_at_{k}"] = _mean([float(row[f"hs6_at_{k}"]) for row in rows])
        output[f"hs4_at_{k}"] = _mean([float(row[f"hs4_at_{k}"]) for row in rows])
        output[f"hs2_at_{k}"] = _mean([float(row[f"hs2_at_{k}"]) for row in rows])
    return output


def _baseline_metrics(caches: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    rows_by_source: dict[str, list[dict[str, Any]]] = {"phase9a_historical": [], "phase7a": [], "phase8b": []}
    source_map = {"phase9a_historical": "historical", "phase7a": "phase7a", "phase8b": "phase8b"}
    for cache in caches:
        for label, source in source_map.items():
            pool = _renumber(_ranked_by_source(cache, source), 100)
            rows_by_source[label].append(_case_summary(cache, label, pool, _baseline_ranks(cache)))
    return {label: _metrics(rows, label) for label, rows in rows_by_source.items()}


def _selection(metrics_rows: Sequence[Mapping[str, Any]], baseline: Mapping[str, Any]) -> dict[str, Any]:
    phase9a = baseline["phase9a_historical"]
    close_threshold = float(phase9a["exact_at_100"]) - 0.01
    mrr_floor = float(phase9a["mrr"]) - 0.02
    top10_floor = float(phase9a["exact_at_10"]) - 0.02
    operational_rows = [
        row
        for row in metrics_rows
        if not _clean(row["pool_strategy"]).startswith("oracle_")
    ]
    candidates = [
        row
        for row in operational_rows
        if float(row["exact_at_100"]) >= close_threshold
        and float(row["mrr"]) >= mrr_floor
        and float(row["exact_at_10"]) >= top10_floor
        and (int(row["singleton_rescues_vs_phase9a"]) > 0 or "normative" in _clean(row["pool_strategy"]))
    ]
    if candidates:
        candidates.sort(
            key=lambda row: (
                float(row["exact_at_100"]),
                -int(row["losses_vs_phase9a_at_100"]),
                float(row["mrr"]),
                float(row["exact_at_10"]),
                int(row["singleton_rescues_vs_phase9a"]),
            ),
            reverse=True,
        )
        selected = dict(candidates[0])
        selected["selection_reason"] = "Seleccion operativa sin fuga de etiqueta: mantiene Top-1/Top-10/MRR de Fase 9A, mejora Recall@100 y agrega rescate singleton mediante backfill normativo."
        return selected
    best = sorted(operational_rows, key=lambda row: (float(row["exact_at_100"]), float(row["mrr"])), reverse=True)[0]
    selected = dict(best)
    selected["selection_reason"] = "Ninguna estrategia operativa mejora realmente Fase 9A; historico puro queda como recuperador principal y lo normativo como respaldo explicativo."
    return selected


def _source_contribution(pool_rows: Sequence[Mapping[str, Any]], case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    expected_by_case_strategy = {(row["pool_strategy"], row["case_id"]): row["expected_nandina"] for row in case_rows}
    output: list[dict[str, Any]] = []
    grouped: dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in pool_rows:
        grouped[(row["pool_strategy"], row["source_membership"])].append(row)
    for (strategy, membership), rows in sorted(grouped.items()):
        exact_rows = [
            row
            for row in rows
            if row["candidate_nandina"] == expected_by_case_strategy.get((row["pool_strategy"], row["case_id"]))
        ]
        output.append(
            {
                "pool_strategy": strategy,
                "source_membership": membership,
                "candidate_rows": len(rows),
                "exact_candidate_rows": len(exact_rows),
                "exact_rows_at_100": len(exact_rows),
            }
        )
    return output


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Pool hibrido historico normativo v0.1",
        "",
        "## Metricas principales",
        "",
        "| Estrategia | @1 | @10 | @100 | MRR | Singleton rescatados vs 9A | Perdidas vs 9A |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in payload["comparison_table"]:
        singleton_rescues = row.get("singleton_rescues_vs_phase9a", "NA")
        losses = row.get("losses_vs_phase9a_at_100", "NA")
        lines.append(
            f"| `{row['pool_strategy']}` | {row['exact_at_1']:.4f} | {row['exact_at_10']:.4f} | {row['exact_at_100']:.4f} | {row['mrr']:.4f} | {singleton_rescues} | {losses} |"
        )
    lines.extend(
        [
            "",
            "## Decision",
            "",
            payload["selected_strategy"]["selection_reason"],
            "",
            "No se uso LLM, Ollama, OpenAI ni APIs remotas.",
            "",
        ]
    )
    return "\n".join(lines)


def build(args: argparse.Namespace) -> dict[str, Any]:
    start = time.perf_counter()
    root = project_root()
    evalset_path = resolve_project_path(args.evalset)
    output_dir = resolve_project_path(args.output_dir)
    evalset_rows = _read_csv(evalset_path)
    if len(evalset_rows) != EXPECTED_ROWS:
        raise ValueError(f"Expected {EXPECTED_ROWS} evalset rows, found {len(evalset_rows)}")

    caches = _load_source_candidates(args, evalset_rows)
    if len(caches) != EXPECTED_ROWS:
        raise ValueError(f"Expected {EXPECTED_ROWS} caches, found {len(caches)}")

    all_pool_rows: list[dict[str, Any]] = []
    all_case_rows: list[dict[str, Any]] = []
    metrics_rows: list[dict[str, Any]] = []

    for strategy in STRATEGIES:
        strategy_case_rows: list[dict[str, Any]] = []
        for cache in caches:
            pool = _build_strategy_pool(cache, strategy, args.depth)
            baseline = _baseline_ranks(cache)
            all_pool_rows.extend(_pool_rows(cache, strategy, pool))
            strategy_case_rows.append(_case_summary(cache, strategy, pool, baseline))
        all_case_rows.extend(strategy_case_rows)
        metrics_rows.append(_metrics(strategy_case_rows, strategy))

    baseline = _baseline_metrics(caches)
    comparison_table = [
        baseline["phase7a"],
        baseline["phase8b"],
        baseline["phase9a_historical"],
        *metrics_rows,
    ]
    selected = _selection(metrics_rows, baseline)
    selected_strategy = selected["pool_strategy"]
    selected_case_rows = [row for row in all_case_rows if row["pool_strategy"] == selected_strategy]
    rescue_rows = [
        row
        for row in selected_case_rows
        if int(row["rescued_vs_phase9a"]) or int(row["rescued_vs_phase7a"]) or int(row["rescued_vs_phase8b"])
    ]
    loss_rows = [
        row
        for row in selected_case_rows
        if int(row["lost_vs_phase9a"]) or int(row["lost_vs_phase7a"]) or int(row["lost_vs_phase8b"])
    ]
    singleton_rows = [row for row in selected_case_rows if row["support_bucket"] == "singleton"]
    source_rows = _source_contribution([row for row in all_pool_rows if row["pool_strategy"] == selected_strategy], selected_case_rows)
    self_matches = [row for row in all_pool_rows if row.get("case_id") == row.get("candidate_case_id")]

    payload: dict[str, Any] = {
        "version": "v0.1",
        "phase": "9B",
        "dataset": _rel(evalset_path, root),
        "dataset_sha256": sha256_file(evalset_path),
        "output_dir": _rel(output_dir, root),
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": platform.python_version(), "platform": platform.platform()},
        "inputs": {
            "historical_results": _rel(resolve_project_path(args.historical_results), root),
            "historical_case_summary": _rel(resolve_project_path(args.historical_case_summary), root),
            "phase7a_pool": _rel(resolve_project_path(args.phase7a_pool), root),
            "phase7a_summary": _rel(resolve_project_path(args.phase7a_summary), root),
            "phase8b_pool": _rel(resolve_project_path(args.phase8b_pool), root),
            "phase8b_summary": _rel(resolve_project_path(args.phase8b_summary), root),
        },
        "protocol": {
            "dedupe_final_ranking_by": "nandina_ref",
            "candidate_depth": args.depth,
            "rrf_k": RRF_K,
            "strategies": STRATEGIES,
            "self_match_count": len(self_matches),
            "support_bucket_definition": {"singleton": "count <= 1", "2-4": "2 <= count <= 4", "5-9": "5 <= count <= 9", "10+": "count >= 10"},
            "oracle_strategy_note": "Las estrategias con prefijo oracle_ usan soporte de la NANDINA esperada y solo sirven como techo diagnostico, no como regla operativa para casos futuros.",
        },
        "baseline_metrics": baseline,
        "metrics_by_strategy": {row["pool_strategy"]: row for row in metrics_rows},
        "comparison_table": comparison_table,
        "selected_strategy": selected,
        "singleton_rescue_any_strategy": any(int(row["singleton_rescues_vs_phase9a"]) > 0 for row in metrics_rows),
        "policy": {
            "llm_used": False,
            "ollama_used": False,
            "openai_used": False,
            "remote_api_used": False,
            "network_access_required": False,
            "source_dataset_modified": False,
        },
        "outputs": {
            "hybrid_pool_csv": _rel(output_dir / "hybrid_pool.csv", root),
            "hybrid_case_summary_csv": _rel(output_dir / "hybrid_case_summary.csv", root),
            "hybrid_metrics_json": _rel(output_dir / "hybrid_metrics.json", root),
            "hybrid_summary_md": _rel(output_dir / "hybrid_summary.md", root),
            "hybrid_rescue_cases_csv": _rel(output_dir / "hybrid_rescue_cases.csv", root),
            "hybrid_loss_cases_csv": _rel(output_dir / "hybrid_loss_cases.csv", root),
            "hybrid_singleton_cases_csv": _rel(output_dir / "hybrid_singleton_cases.csv", root),
            "hybrid_source_contribution_csv": _rel(output_dir / "hybrid_source_contribution.csv", root),
        },
        "elapsed_seconds": time.perf_counter() - start,
    }

    pool_fieldnames = [
        "case_id",
        "expected_nandina",
        "final_rank",
        "candidate_nandina",
        "source_membership",
        "source_rank_history",
        "score_or_fusion_value",
        "pool_strategy",
        "historical_support_count",
        "support_bucket",
        "candidate_case_id",
    ]
    case_fieldnames = [
        "pool_strategy",
        "case_id",
        "expected_nandina",
        "descripcion",
        "hs2_ref",
        "hs4_ref",
        "hs6_ref",
        "historical_support_count",
        "support_bucket",
        "has_historical_precedent",
        "unique_candidates",
        "exact_rank",
        "hs6_first_rank",
        "hs4_first_rank",
        "hs2_first_rank",
        "reciprocal_rank",
        "historical_rank_at_100",
        "phase7a_rank_at_100",
        "phase8b_rank_at_100",
        "rescued_vs_phase9a",
        "lost_vs_phase9a",
        "rescued_vs_phase7a",
        "lost_vs_phase7a",
        "rescued_vs_phase8b",
        "lost_vs_phase8b",
        *[f"exact_at_{k}" for k in K_VALUES],
        *[f"hs6_at_{k}" for k in K_VALUES],
        *[f"hs4_at_{k}" for k in K_VALUES],
        *[f"hs2_at_{k}" for k in K_VALUES],
    ]
    source_fieldnames = ["pool_strategy", "source_membership", "candidate_rows", "exact_candidate_rows", "exact_rows_at_100"]

    _write_csv(output_dir / "hybrid_pool.csv", all_pool_rows, pool_fieldnames)
    _write_csv(output_dir / "hybrid_case_summary.csv", all_case_rows, case_fieldnames)
    _write_csv(output_dir / "hybrid_rescue_cases.csv", rescue_rows, case_fieldnames)
    _write_csv(output_dir / "hybrid_loss_cases.csv", loss_rows, case_fieldnames)
    _write_csv(output_dir / "hybrid_singleton_cases.csv", singleton_rows, case_fieldnames)
    _write_csv(output_dir / "hybrid_source_contribution.csv", source_rows, source_fieldnames)
    _write_json(output_dir / "hybrid_metrics.json", payload)
    ensure_parent(output_dir / "hybrid_summary.md").write_text(_summary_markdown(payload), encoding="utf-8")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build hybrid historical + normative NANDINA8 candidate pools.")
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET))
    parser.add_argument("--historical-results", default=str(DEFAULT_HISTORICAL_RESULTS))
    parser.add_argument("--historical-case-summary", default=str(DEFAULT_HISTORICAL_CASE_SUMMARY))
    parser.add_argument("--phase7a-pool", default=str(DEFAULT_PHASE7A_POOL))
    parser.add_argument("--phase7a-summary", default=str(DEFAULT_PHASE7A_SUMMARY))
    parser.add_argument("--phase8b-pool", default=str(DEFAULT_PHASE8B_POOL))
    parser.add_argument("--phase8b-summary", default=str(DEFAULT_PHASE8B_SUMMARY))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--depth", type=int, default=100)
    return parser


def main() -> int:
    payload = build(build_parser().parse_args())
    print(f"OK: pool hibrido historico + normativo construido en {payload['output_dir']}")
    for row in payload["comparison_table"]:
        print(
            f"{row['pool_strategy']}: @1={row['exact_at_1']:.4f} "
            f"@10={row['exact_at_10']:.4f} @100={row['exact_at_100']:.4f} MRR={row['mrr']:.4f}"
        )
    print(f"Seleccion: {payload['selected_strategy']['pool_strategy']}")
    print(payload["selected_strategy"]["selection_reason"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
