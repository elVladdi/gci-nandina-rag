from __future__ import annotations

import argparse
import csv
import json
import platform
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_ABLATION_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/candidate_pool_devset_v0.1")

PRECISION_VARIANT = "C_hs6_leaf"
RECALL_VARIANT = "D_4d_hs6_leaf"
DUAL_METHOD = "BM25_dual_protected_top_5_backfill"
HIERARCHICAL_METHOD = "BM25_hierarchical_v0.1"
PROTECTED_TOP_N = 5
EXPECTED_ROWS = {"devset": 13, "evalset": 600}
POOL_STRATEGIES = {
    "hierarchical_first": None,
    "hierarchical_80_dual_backfill_20": 80,
    "hierarchical_70_dual_backfill_30": 70,
}


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


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _median(values: Sequence[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def _parse_depths(raw: str) -> list[int]:
    depths = sorted({int(item.strip()) for item in raw.split(",") if item.strip()})
    if not depths or any(depth <= 0 for depth in depths):
        raise ValueError("--pool-depths must contain positive integers")
    return depths


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _code_from_hit(hit: Mapping[str, Any]) -> str:
    return _clean(hit.get("code"))


def _rank_map(hits: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    ranks: dict[str, int] = {}
    for rank, hit in enumerate(hits, start=1):
        code = _code_from_hit(hit)
        if code and code not in ranks:
            ranks[code] = rank
    return ranks


def _score_map(hits: Sequence[Mapping[str, Any]]) -> dict[str, float]:
    scores: dict[str, float] = {}
    for hit in hits:
        code = _code_from_hit(hit)
        if code and code not in scores:
            scores[code] = float(hit.get("score", 0.0))
    return scores


def _text_map(hits: Sequence[Mapping[str, Any]]) -> dict[str, str]:
    texts: dict[str, str] = {}
    for hit in hits:
        code = _code_from_hit(hit)
        if code and code not in texts:
            texts[code] = _clean(hit.get("text"))
    return texts


def _dedupe_append(target: list[dict[str, Any]], seen: set[str], hits: Sequence[Mapping[str, Any]], limit: int | None = None) -> None:
    for hit in hits if limit is None else hits[:limit]:
        code = _code_from_hit(hit)
        if code and code not in seen:
            seen.add(code)
            target.append(dict(hit))


def _renumber(hits: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    ranked: list[dict[str, Any]] = []
    for rank, hit in enumerate(hits[:depth], start=1):
        item = dict(hit)
        item["rank"] = rank
        ranked.append(item)
    return ranked


def _protected_top_5_backfill(
    precision_hits: Sequence[Mapping[str, Any]],
    recall_hits: Sequence[Mapping[str, Any]],
    depth: int,
) -> list[dict[str, Any]]:
    fused: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(fused, seen, precision_hits, limit=PROTECTED_TOP_N)
    _dedupe_append(fused, seen, recall_hits)
    _dedupe_append(fused, seen, precision_hits[PROTECTED_TOP_N:])
    return _renumber(fused, depth)


def _final_pool(
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    depth: int,
    strategy: str,
) -> list[dict[str, Any]]:
    hierarchical_base = POOL_STRATEGIES[strategy]
    pool: list[dict[str, Any]] = []
    seen: set[str] = set()

    if hierarchical_base is None:
        _dedupe_append(pool, seen, hierarchical_hits)
        _dedupe_append(pool, seen, dual_hits)
        return _renumber(pool, depth)

    base_count = min(hierarchical_base, depth)
    _dedupe_append(pool, seen, hierarchical_hits, limit=base_count)
    _dedupe_append(pool, seen, dual_hits, limit=depth)
    if len(pool) < depth:
        _dedupe_append(pool, seen, hierarchical_hits[base_count:])
    return _renumber(pool, depth)


def _codes_in_top(hits: Sequence[Mapping[str, Any]], k: int) -> set[str]:
    return {_code_from_hit(hit) for hit in hits[:k] if _code_from_hit(hit)}


def _prefix_hit_in_top(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int) -> int:
    prefix = true_code[:prefix_len]
    return int(any(_code_from_hit(hit).startswith(prefix) for hit in hits[:k]))


def _exact_hit_in_top(hits: Sequence[Mapping[str, Any]], true_code: str, k: int) -> int:
    return int(true_code in _codes_in_top(hits, k))


def _union_exact_hit(
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    true_code: str,
    k: int,
) -> int:
    return int(true_code in (_codes_in_top(hierarchical_hits, k) | _codes_in_top(dual_hits, k)))


def _union_prefix_hit(
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    true_code: str,
    prefix_len: int,
    k: int,
) -> int:
    return int(
        _prefix_hit_in_top(hierarchical_hits, true_code, prefix_len, k)
        or _prefix_hit_in_top(dual_hits, true_code, prefix_len, k)
    )


def _first_rank_prefix(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int) -> int:
    prefix = true_code[:prefix_len]
    for rank, hit in enumerate(hits, start=1):
        if _code_from_hit(hit).startswith(prefix):
            return rank
    return 0


def _candidate_rows_for_case(
    case_id: str,
    descripcion: str,
    true_code: str,
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    pool_hits: Sequence[Mapping[str, Any]],
    strategy: str,
) -> list[dict[str, Any]]:
    hierarchical_ranks = _rank_map(hierarchical_hits)
    dual_ranks = _rank_map(dual_hits)
    hierarchical_scores = _score_map(hierarchical_hits)
    dual_scores = _score_map(dual_hits)
    evidence_by_code = {**_text_map(dual_hits), **_text_map(hierarchical_hits)}

    rows: list[dict[str, Any]] = []
    for pool_rank, hit in enumerate(pool_hits, start=1):
        code = _code_from_hit(hit)
        rows.append(
            {
                "pool_strategy": strategy,
                "case_id": case_id,
                "descripcion": descripcion,
                "nandina_ref": true_code,
                "candidate_code": code,
                "candidate_rank_pool": pool_rank,
                "candidate_rank_hierarchical": hierarchical_ranks.get(code, ""),
                "candidate_rank_dual": dual_ranks.get(code, ""),
                "source_hierarchical": str(code in hierarchical_ranks).lower(),
                "source_dual": str(code in dual_ranks).lower(),
                "hierarchical_score": hierarchical_scores.get(code, ""),
                "dual_score": dual_scores.get(code, ""),
                "hs2_candidate": code[:2],
                "hs4_candidate": code[:4],
                "is_expected_code": str(code == true_code).lower(),
                "is_expected_hs4": str(code[:4] == true_code[:4]).lower(),
                "is_expected_hs2": str(code[:2] == true_code[:2]).lower(),
                "evidence_text": evidence_by_code.get(code, ""),
            }
        )
    return rows


def _case_summary(
    case_id: str,
    descripcion: str,
    true_code: str,
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    pool_hits: Sequence[Mapping[str, Any]],
    depths: Sequence[int],
    strategy: str,
) -> dict[str, Any]:
    hierarchical_rank = rank_of_true(hierarchical_hits, true_code)
    dual_rank = rank_of_true(dual_hits, true_code)
    final_pool_rank = rank_of_true(pool_hits, true_code)
    summary: dict[str, Any] = {
        "pool_strategy": strategy,
        "case_id": case_id,
        "descripcion": descripcion,
        "nandina_ref": true_code,
        "hs2_ref": true_code[:2],
        "hs4_ref": true_code[:4],
        "unique_candidates_final_pool": len({_code_from_hit(hit) for hit in pool_hits if _code_from_hit(hit)}),
        "expected_code_rank_hierarchical": hierarchical_rank,
        "expected_code_rank_dual": dual_rank,
        "expected_code_rank_final_pool": final_pool_rank,
        "expected_hs4_first_rank_final_pool": _first_rank_prefix(pool_hits, true_code, 4),
        "expected_hs2_first_rank_final_pool": _first_rank_prefix(pool_hits, true_code, 2),
        "source_exact_category_only_hierarchical": int(hierarchical_rank > 0 and dual_rank <= 0),
        "source_exact_category_only_dual": int(dual_rank > 0 and hierarchical_rank <= 0),
        "source_exact_category_both": int(hierarchical_rank > 0 and dual_rank > 0),
        "source_exact_category_neither": int(hierarchical_rank <= 0 and dual_rank <= 0),
        "dual_adds_expected_against_hierarchical": int(dual_rank > 0 and hierarchical_rank <= 0),
    }
    for depth in depths:
        summary[f"hierarchical_at_{depth}"] = _exact_hit_in_top(hierarchical_hits, true_code, depth)
        summary[f"dual_at_{depth}"] = _exact_hit_in_top(dual_hits, true_code, depth)
        summary[f"union_oracle_at_{depth}"] = _union_exact_hit(hierarchical_hits, dual_hits, true_code, depth)
        summary[f"final_pool_at_{depth}"] = _exact_hit_in_top(pool_hits, true_code, depth)
        summary[f"hierarchical_hs4_at_{depth}"] = _prefix_hit_in_top(hierarchical_hits, true_code, 4, depth)
        summary[f"dual_hs4_at_{depth}"] = _prefix_hit_in_top(dual_hits, true_code, 4, depth)
        summary[f"union_oracle_hs4_at_{depth}"] = _union_prefix_hit(hierarchical_hits, dual_hits, true_code, 4, depth)
        summary[f"final_pool_hs4_at_{depth}"] = _prefix_hit_in_top(pool_hits, true_code, 4, depth)
        summary[f"hierarchical_hs2_at_{depth}"] = _prefix_hit_in_top(hierarchical_hits, true_code, 2, depth)
        summary[f"dual_hs2_at_{depth}"] = _prefix_hit_in_top(dual_hits, true_code, 2, depth)
        summary[f"union_oracle_hs2_at_{depth}"] = _union_prefix_hit(hierarchical_hits, dual_hits, true_code, 2, depth)
        summary[f"final_pool_hs2_at_{depth}"] = _prefix_hit_in_top(pool_hits, true_code, 2, depth)
    return summary


def _source_overlap_summary(case_summaries: Sequence[Mapping[str, Any]], strategy: str, max_depth: int) -> dict[str, Any]:
    rows = [row for row in case_summaries if row["pool_strategy"] == strategy]
    both = sum(int(row["source_exact_category_both"]) for row in rows)
    only_hierarchical = sum(int(row["source_exact_category_only_hierarchical"]) for row in rows)
    only_dual = sum(int(row["source_exact_category_only_dual"]) for row in rows)
    neither = sum(int(row["source_exact_category_neither"]) for row in rows)
    new_from_dual = sum(int(row["dual_adds_expected_against_hierarchical"]) for row in rows)
    return {
        "pool_strategy": strategy,
        "pool_depth": max_depth,
        "cases_where_only_hierarchical_recovers_expected": only_hierarchical,
        "cases_where_only_dual_recovers_expected": only_dual,
        "cases_where_both_recover_expected": both,
        "cases_where_neither_recovers_expected": neither,
        "union_oracle_expected_cases": both + only_hierarchical + only_dual,
        "final_pool_expected_cases": sum(int(row[f"final_pool_at_{max_depth}"]) for row in rows),
        "new_expected_cases_contributed_by_dual_vs_hierarchical": new_from_dual,
    }


def _strategy_metrics(
    case_summaries: Sequence[Mapping[str, Any]],
    source_overlap: Mapping[str, Any],
    depths: Sequence[int],
    strategy: str,
) -> dict[str, Any]:
    rows = [row for row in case_summaries if row["pool_strategy"] == strategy]
    candidate_counts = [int(row["unique_candidates_final_pool"]) for row in rows]
    payload: dict[str, Any] = {
        "pool_strategy": strategy,
        "cases_total": len(rows),
        "average_unique_candidates_per_case": _mean([float(value) for value in candidate_counts]),
        "median_unique_candidates_per_case": _median([float(value) for value in candidate_counts]),
        "source_overlap": dict(source_overlap),
    }
    metric_families = [
        "hierarchical",
        "dual",
        "union_oracle",
        "final_pool",
        "hierarchical_hs4",
        "dual_hs4",
        "union_oracle_hs4",
        "final_pool_hs4",
        "hierarchical_hs2",
        "dual_hs2",
        "union_oracle_hs2",
        "final_pool_hs2",
    ]
    for depth in depths:
        for family in metric_families:
            payload[f"{family}_at_{depth}"] = _mean([float(row[f"{family}_at_{depth}"]) for row in rows])
    return payload


def _metrics(
    dataset: str,
    case_summaries: Sequence[Mapping[str, Any]],
    source_overlaps: Sequence[Mapping[str, Any]],
    depths: Sequence[int],
    params: Mapping[str, Any],
) -> dict[str, Any]:
    by_strategy = {
        overlap["pool_strategy"]: _strategy_metrics(case_summaries, overlap, depths, overlap["pool_strategy"])
        for overlap in source_overlaps
    }
    best_strategy = max(
        by_strategy,
        key=lambda strategy: (
            by_strategy[strategy][f"final_pool_at_{max(depths)}"],
            by_strategy[strategy][f"final_pool_hs4_at_{max(depths)}"],
            by_strategy[strategy][f"final_pool_hs2_at_{max(depths)}"],
        ),
    )
    first = by_strategy["hierarchical_first"]
    payload: dict[str, Any] = {
        "dataset": dataset,
        "cases_total": first["cases_total"],
        "parameters": dict(params),
        "pool_strategies": list(by_strategy.keys()),
        "best_final_pool_strategy_at_max_depth": best_strategy,
        "metrics_by_strategy": by_strategy,
        "source_overlap_by_strategy": {row["pool_strategy"]: dict(row) for row in source_overlaps},
    }
    # Backward-compatible aliases point to hierarchical_first, which documents the initial cap behavior.
    payload.update(
        {
            "average_unique_candidates_per_case": first["average_unique_candidates_per_case"],
            "median_unique_candidates_per_case": first["median_unique_candidates_per_case"],
            "source_overlap": first["source_overlap"],
        }
    )
    for depth in depths:
        payload[f"pool_at_{depth}"] = first[f"final_pool_at_{depth}"]
        payload[f"pool_hs4_at_{depth}"] = first[f"final_pool_hs4_at_{depth}"]
        payload[f"pool_hs2_at_{depth}"] = first[f"final_pool_hs2_at_{depth}"]
        payload[f"union_oracle_at_{depth}"] = first[f"union_oracle_at_{depth}"]
    return payload


def _summary_markdown(metrics: Mapping[str, Any]) -> str:
    depths = metrics["parameters"]["pool_depths"]
    lines = [
        f"# Candidate pool {metrics['dataset']} v0.1",
        "",
        "## Alcance",
        "",
        "Construccion y evaluacion corregida de un pool combinado para Fase 7A. No se ejecuto LLM ni Text2Trade; no se modificaron reglas mirando resultados del evalset.",
        "",
        "## Arquitectura",
        "",
        f"- Ranking principal: `{HIERARCHICAL_METHOD}`.",
        f"- Fuente auxiliar: `{DUAL_METHOD}`.",
        "- `union_oracle` mide cobertura disponible en la union Top-K de ambos recuperadores; no es un ranking entregable.",
        "- `final_pool` mide el ranking recortado que recibiria el LLM segun cada estrategia.",
        "",
        "## Estrategias final_pool",
        "",
        "- `hierarchical_first`: jerarquico primero; dual solo entra si queda espacio.",
        "- `hierarchical_80_dual_backfill_20`: Top-80 jerarquico y hasta 20 candidatos nuevos del dual.",
        "- `hierarchical_70_dual_backfill_30`: Top-70 jerarquico y hasta 30 candidatos nuevos del dual.",
        "",
        "## Metricas exactas",
        "",
        "| Estrategia | Profundidad | Hierarchical | Dual | Union oracle | Final pool |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for strategy, item in metrics["metrics_by_strategy"].items():
        for depth in depths:
            lines.append(
                f"| {strategy} | {depth} | {item[f'hierarchical_at_{depth}']:.4f} | {item[f'dual_at_{depth}']:.4f} | {item[f'union_oracle_at_{depth}']:.4f} | {item[f'final_pool_at_{depth}']:.4f} |"
            )
    lines.extend(
        [
            "",
            "## Metricas HS4",
            "",
            "| Estrategia | Profundidad | Hierarchical HS4 | Dual HS4 | Union oracle HS4 | Final pool HS4 |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for strategy, item in metrics["metrics_by_strategy"].items():
        for depth in depths:
            lines.append(
                f"| {strategy} | {depth} | {item[f'hierarchical_hs4_at_{depth}']:.4f} | {item[f'dual_hs4_at_{depth}']:.4f} | {item[f'union_oracle_hs4_at_{depth}']:.4f} | {item[f'final_pool_hs4_at_{depth}']:.4f} |"
            )
    lines.extend(
        [
            "",
            "## Metricas HS2",
            "",
            "| Estrategia | Profundidad | Hierarchical HS2 | Dual HS2 | Union oracle HS2 | Final pool HS2 |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for strategy, item in metrics["metrics_by_strategy"].items():
        for depth in depths:
            lines.append(
                f"| {strategy} | {depth} | {item[f'hierarchical_hs2_at_{depth}']:.4f} | {item[f'dual_hs2_at_{depth}']:.4f} | {item[f'union_oracle_hs2_at_{depth}']:.4f} | {item[f'final_pool_hs2_at_{depth}']:.4f} |"
            )
    max_depth = max(depths)
    lines.extend(
        [
            "",
            "## Aporte del dual",
            "",
            "| Estrategia | Solo hierarchical | Solo dual | Ambos | Ninguno | Union oracle casos | Final pool casos |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for strategy, overlap in metrics["source_overlap_by_strategy"].items():
        lines.append(
            f"| {strategy} | {overlap['cases_where_only_hierarchical_recovers_expected']} | {overlap['cases_where_only_dual_recovers_expected']} | {overlap['cases_where_both_recover_expected']} | {overlap['cases_where_neither_recovers_expected']} | {overlap['union_oracle_expected_cases']} | {overlap['final_pool_expected_cases']} |"
        )
    lines.extend(
        [
            "",
            "## Decision de salida",
            "",
            f"Mejor estrategia entregable a profundidad {max_depth}: `{metrics['best_final_pool_strategy_at_max_depth']}`.",
            "La diferencia entre `union_oracle` y `final_pool` muestra cuanto potencial disponible se pierde por ordenamiento y recorte.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    dataset = args.dataset
    input_csv = resolve_project_path(args.input_csv or (DEFAULT_DEVSET if dataset == "devset" else DEFAULT_EVALSET))
    output_dir = resolve_project_path(args.output_dir or DEFAULT_OUTPUT_DIR)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    ablation_index_dir = resolve_project_path(args.ablation_index_dir)
    precision_index_path = ablation_index_dir / f"{PRECISION_VARIANT}.pkl"
    recall_index_path = ablation_index_dir / f"{RECALL_VARIANT}.pkl"
    pool_depths = _parse_depths(args.pool_depths)
    max_pool_depth = max(pool_depths)

    rows = _read_csv(input_csv)
    expected_rows = EXPECTED_ROWS[dataset]
    if len(rows) != expected_rows:
        raise ValueError(f"{dataset} row count is {len(rows)}, expected {expected_rows}.")

    start = time.time()
    hierarchical_index = load_bm25_index(hierarchical_index_path)
    precision_index = load_bm25_index(precision_index_path)
    recall_index = load_bm25_index(recall_index_path)

    candidate_rows: list[dict[str, Any]] = []
    case_summaries: list[dict[str, Any]] = []
    for position, input_row in enumerate(rows, start=1):
        descripcion = _clean(input_row.get("descripcion"))
        true_code = _clean(input_row.get("nandina_ref") or input_row.get("nandina"))
        default_case_id = f"{dataset}-{position:04d}" if dataset == "evalset" else f"{dataset}-{position:02d}"
        case_id = _clean(input_row.get("case_id")) or default_case_id

        hierarchical_hits = retrieve(hierarchical_index, descripcion, top_n=args.hier_depth)
        precision_hits = retrieve(precision_index, descripcion, top_n=args.dual_depth)
        recall_hits = retrieve(recall_index, descripcion, top_n=args.dual_depth)
        dual_hits = _protected_top_5_backfill(precision_hits, recall_hits, depth=args.dual_depth)

        for strategy in POOL_STRATEGIES:
            pool_hits = _final_pool(hierarchical_hits, dual_hits, max_pool_depth, strategy)
            candidate_rows.extend(
                _candidate_rows_for_case(case_id, descripcion, true_code, hierarchical_hits, dual_hits, pool_hits, strategy)
            )
            case_summaries.append(
                _case_summary(case_id, descripcion, true_code, hierarchical_hits, dual_hits, pool_hits, pool_depths, strategy)
            )

    source_overlaps = [_source_overlap_summary(case_summaries, strategy, max_pool_depth) for strategy in POOL_STRATEGIES]
    params = {
        "hier_depth": args.hier_depth,
        "dual_depth": args.dual_depth,
        "pool_depths": pool_depths,
        "pool_max_depth": max_pool_depth,
        "dual_rule": "protected_top_5_backfill",
        "protected_top_n": PROTECTED_TOP_N,
        "final_pool_strategies": list(POOL_STRATEGIES.keys()),
        "hierarchical_index_path": _rel(hierarchical_index_path, root),
        "precision_index_path": _rel(precision_index_path, root),
        "recall_index_path": _rel(recall_index_path, root),
    }
    metrics = _metrics(dataset, case_summaries, source_overlaps, pool_depths, params)
    metrics.update(
        {
            "script": "src.experiments.build_candidate_pool",
            "execution": {
                "datetime_utc": datetime.now(timezone.utc).isoformat(),
                "timestamp_unix": int(time.time()),
                "elapsed_seconds": time.time() - start,
                "environment": {
                    "python_version": platform.python_version(),
                    "system": platform.system(),
                    "release": platform.release(),
                    "machine": platform.machine(),
                },
            },
            "input": {
                "dataset_path": _rel(input_csv, root),
                "dataset_sha256": sha256_file(input_csv),
                "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
                "precision_index_sha256": sha256_file(precision_index_path),
                "recall_index_sha256": sha256_file(recall_index_path),
            },
            "controls": {
                "llm_executed": False,
                "text2trade_executed": False,
                "rules_adjusted_after_evalset": False,
                "devset_modified": False,
                "evalset_modified": False,
                "source_excel_modified": False,
            },
            "outputs": {
                "candidate_pool_csv": _rel(output_dir / "candidate_pool.csv", root),
                "candidate_pool_metrics_json": _rel(output_dir / "candidate_pool_metrics.json", root),
                "candidate_pool_summary_md": _rel(output_dir / "candidate_pool_summary.md", root),
                "candidate_pool_case_summary_csv": _rel(output_dir / "candidate_pool_case_summary.csv", root),
                "candidate_pool_source_overlap_csv": _rel(output_dir / "candidate_pool_source_overlap.csv", root),
            },
            "warnings": [
                "No LLM, Text2Trade, or source Excel execution is part of this script.",
                "union_oracle is a coverage diagnostic, not an orderable final ranking for LLM delivery.",
                "Evidence text is copied only from BM25 index hit text when exposed by the index.",
            ],
        }
    )

    candidate_fields = [
        "pool_strategy",
        "case_id",
        "descripcion",
        "nandina_ref",
        "candidate_code",
        "candidate_rank_pool",
        "candidate_rank_hierarchical",
        "candidate_rank_dual",
        "source_hierarchical",
        "source_dual",
        "hierarchical_score",
        "dual_score",
        "hs2_candidate",
        "hs4_candidate",
        "is_expected_code",
        "is_expected_hs4",
        "is_expected_hs2",
        "evidence_text",
    ]
    case_fields = list(case_summaries[0].keys()) if case_summaries else []
    _write_csv(output_dir / "candidate_pool.csv", candidate_rows, candidate_fields)
    _write_json(output_dir / "candidate_pool_metrics.json", metrics)
    ensure_parent(output_dir / "candidate_pool_summary.md")
    (output_dir / "candidate_pool_summary.md").write_text(_summary_markdown(metrics), encoding="utf-8")
    _write_csv(output_dir / "candidate_pool_case_summary.csv", case_summaries, case_fields)
    _write_csv(output_dir / "candidate_pool_source_overlap.csv", source_overlaps, list(source_overlaps[0].keys()))
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build and evaluate a combined NANDINA candidate pool.")
    parser.add_argument("--dataset", choices=["devset", "evalset"], required=True)
    parser.add_argument("--input-csv", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--hier-depth", type=int, default=100)
    parser.add_argument("--dual-depth", type=int, default=100)
    parser.add_argument("--pool-depths", default="10,20,50,100")
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--ablation-index-dir", type=Path, default=DEFAULT_ABLATION_INDEX_DIR)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print(f"OK: candidate pool {metrics['dataset']} completado")
    print(f"casos={metrics['cases_total']} estrategias={','.join(metrics['pool_strategies'])}")
    max_depth = max(metrics["parameters"]["pool_depths"])
    for strategy, item in metrics["metrics_by_strategy"].items():
        print(
            f"{strategy}: union_oracle@{max_depth}={item[f'union_oracle_at_{max_depth}']:.4f} "
            f"final_pool@{max_depth}={item[f'final_pool_at_{max_depth}']:.4f} "
            f"hs4={item[f'final_pool_hs4_at_{max_depth}']:.4f} "
            f"hs2={item[f'final_pool_hs2_at_{max_depth}']:.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
