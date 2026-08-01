from __future__ import annotations

import argparse
import csv
import json
import platform
import re
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.1.csv")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_ABLATION_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1")

QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
EXPECTED_EVALSET_ROWS = 1006
EXPECTED_SCOPE_CLASS = "87"
PRECISION_VARIANT = "C_hs6_leaf"
RECALL_VARIANT = "D_4d_hs6_leaf"
PROTECTED_TOP_N = 5
HIERARCHICAL_METHOD = "BM25_hierarchical_v0.1"
DUAL_METHOD = "BM25_dual_protected_top_5_backfill"
POOL_DEPTHS = [10, 20, 50, 100, 200]
FAMILY_DEPTHS = [10, 50, 100, 200]

POOL_STRATEGIES: dict[str, dict[str, Any]] = {
    "hierarchical_only": {"kind": "single_source", "source": "hierarchical"},
    "dual_only": {"kind": "single_source", "source": "dual"},
    "hierarchical_first_100": {"kind": "hybrid", "hierarchical_slots_in_first_100": 100},
    "hierarchical_80_dual_backfill_20": {"kind": "hybrid", "hierarchical_slots_in_first_100": 80},
    "hierarchical_70_dual_backfill_30": {"kind": "hybrid", "hierarchical_slots_in_first_100": 70},
}


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _normalize_code(value: object) -> str:
    digits = re.sub(r"\D", "", _clean(value))
    return digits[:8]


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


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _code_from_hit(hit: Mapping[str, Any]) -> str:
    return _normalize_code(hit.get("code") or hit.get("candidate_code"))


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


def _dedupe_append(
    target: list[dict[str, Any]],
    seen: set[str],
    hits: Sequence[Mapping[str, Any]],
    source: str,
    limit: int | None = None,
) -> None:
    selected = hits if limit is None else hits[:limit]
    for hit in selected:
        code = _code_from_hit(hit)
        if not code:
            continue
        if code in seen:
            for item in target:
                if _code_from_hit(item) == code:
                    sources = set(item.get("source_membership", []))
                    sources.add(source)
                    item["source_membership"] = sorted(sources)
                    break
            continue
        seen.add(code)
        item = dict(hit)
        item["code"] = code
        item["source_membership"] = [source]
        target.append(item)


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
    _dedupe_append(fused, seen, precision_hits, "dual_precision", limit=PROTECTED_TOP_N)
    _dedupe_append(fused, seen, recall_hits, "dual_recall")
    _dedupe_append(fused, seen, precision_hits[PROTECTED_TOP_N:], "dual_precision")
    return _renumber(fused, depth)


def _final_pool(
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    depth: int,
    strategy: str,
) -> list[dict[str, Any]]:
    config = POOL_STRATEGIES[strategy]
    pool: list[dict[str, Any]] = []
    seen: set[str] = set()

    if config["kind"] == "single_source":
        source = config["source"]
        hits = hierarchical_hits if source == "hierarchical" else dual_hits
        _dedupe_append(pool, seen, hits, source)
        return _renumber(pool, depth)

    first_100_hierarchical = int(config["hierarchical_slots_in_first_100"])
    first_block_depth = min(100, depth)
    hierarchical_base = min(first_100_hierarchical, first_block_depth)
    dual_base = max(0, first_block_depth - hierarchical_base)

    _dedupe_append(pool, seen, hierarchical_hits, "hierarchical", limit=hierarchical_base)
    _dedupe_append(pool, seen, dual_hits, "dual", limit=dual_base)

    if len(pool) < first_block_depth:
        _dedupe_append(pool, seen, hierarchical_hits[hierarchical_base:], "hierarchical")
        _dedupe_append(pool, seen, dual_hits[dual_base:], "dual")

    if depth > 100:
        _dedupe_append(pool, seen, dual_hits[dual_base:], "dual")
        _dedupe_append(pool, seen, hierarchical_hits[hierarchical_base:], "hierarchical")

    return _renumber(pool, depth)


def _codes_in_top(hits: Sequence[Mapping[str, Any]], k: int) -> set[str]:
    return {_code_from_hit(hit) for hit in hits[:k] if _code_from_hit(hit)}


def _exact_hit_in_top(hits: Sequence[Mapping[str, Any]], true_code: str, k: int) -> int:
    return int(true_code in _codes_in_top(hits, k))


def _prefix_hit_in_top(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int) -> int:
    prefix = true_code[:prefix_len]
    if not prefix:
        return 0
    return int(any(_code_from_hit(hit).startswith(prefix) for hit in hits[:k]))


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


def _first_prefix_rank(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int) -> int:
    prefix = true_code[:prefix_len]
    for rank, hit in enumerate(hits, start=1):
        if _code_from_hit(hit).startswith(prefix):
            return rank
    return 0


def _validate_evalset(rows: Sequence[Mapping[str, str]], query_column: str, label_column: str) -> list[str]:
    warnings: list[str] = []
    if len(rows) != EXPECTED_EVALSET_ROWS:
        raise ValueError(f"Evalset row count is {len(rows)}, expected {EXPECTED_EVALSET_ROWS}.")
    if not rows:
        raise ValueError("Evalset is empty.")
    missing = [column for column in [query_column, label_column] if column not in rows[0]]
    if missing:
        raise ValueError(f"Missing required columns in evalset: {missing}")
    empty_queries = sum(1 for row in rows if not _clean(row.get(query_column)))
    invalid_labels = sum(1 for row in rows if not re.fullmatch(r"\d{8}", _normalize_code(row.get(label_column))))
    non_scope = sum(1 for row in rows if _normalize_code(row.get(label_column))[:2] != EXPECTED_SCOPE_CLASS)
    if empty_queries:
        raise ValueError(f"Found empty queries in {query_column}: {empty_queries}")
    if invalid_labels:
        raise ValueError(f"Found non-NANDINA8 expected labels in {label_column}: {invalid_labels}")
    if non_scope:
        warnings.append(f"{non_scope} rows have expected code outside Clase {EXPECTED_SCOPE_CLASS}.")
    return warnings


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
                "source_membership_final_pool": "|".join(hit.get("source_membership", [])),
                "hierarchical_score": hierarchical_scores.get(code, ""),
                "dual_score": dual_scores.get(code, ""),
                "clase_candidate": code[:2],
                "partida_candidate": code[:4],
                "sub_partida_candidate": code[:6],
                "is_expected_code": str(code == true_code).lower(),
                "is_expected_clase": str(code[:2] == true_code[:2]).lower(),
                "is_expected_partida": str(code[:4] == true_code[:4]).lower(),
                "is_expected_sub_partida": str(code[:6] == true_code[:6]).lower(),
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
        "clase_ref": true_code[:2],
        "partida_ref": true_code[:4],
        "sub_partida_ref": true_code[:6],
        "unique_candidates_final_pool": len({_code_from_hit(hit) for hit in pool_hits if _code_from_hit(hit)}),
        "expected_code_rank_hierarchical": hierarchical_rank,
        "expected_code_rank_dual": dual_rank,
        "expected_code_rank_final_pool": final_pool_rank,
        "expected_clase_first_rank_final_pool": _first_prefix_rank(pool_hits, true_code, 2),
        "expected_partida_first_rank_final_pool": _first_prefix_rank(pool_hits, true_code, 4),
        "expected_sub_partida_first_rank_final_pool": _first_prefix_rank(pool_hits, true_code, 6),
    }
    for depth in depths:
        summary[f"hierarchical_at_{depth}"] = _exact_hit_in_top(hierarchical_hits, true_code, depth)
        summary[f"dual_at_{depth}"] = _exact_hit_in_top(dual_hits, true_code, depth)
        summary[f"union_oracle_at_{depth}"] = _union_exact_hit(hierarchical_hits, dual_hits, true_code, depth)
        summary[f"final_pool_at_{depth}"] = _exact_hit_in_top(pool_hits, true_code, depth)
        for prefix_len, label in [(2, "clase"), (4, "partida"), (6, "sub_partida")]:
            summary[f"hierarchical_{label}_at_{depth}"] = _prefix_hit_in_top(hierarchical_hits, true_code, prefix_len, depth)
            summary[f"dual_{label}_at_{depth}"] = _prefix_hit_in_top(dual_hits, true_code, prefix_len, depth)
            summary[f"union_oracle_{label}_at_{depth}"] = _union_prefix_hit(
                hierarchical_hits, dual_hits, true_code, prefix_len, depth
            )
            summary[f"final_pool_{label}_at_{depth}"] = _prefix_hit_in_top(pool_hits, true_code, prefix_len, depth)
        summary[f"dual_rescues_vs_hierarchical_at_{depth}"] = int(
            summary[f"dual_at_{depth}"] == 1 and summary[f"hierarchical_at_{depth}"] == 0
        )
        summary[f"dual_loses_vs_hierarchical_at_{depth}"] = int(
            summary[f"hierarchical_at_{depth}"] == 1 and summary[f"dual_at_{depth}"] == 0
        )
        summary[f"both_recover_at_{depth}"] = int(
            summary[f"hierarchical_at_{depth}"] == 1 and summary[f"dual_at_{depth}"] == 1
        )
        summary[f"neither_recovers_at_{depth}"] = int(
            summary[f"hierarchical_at_{depth}"] == 0 and summary[f"dual_at_{depth}"] == 0
        )
        summary[f"final_pool_rescues_vs_hierarchical_at_{depth}"] = int(
            summary[f"final_pool_at_{depth}"] == 1 and summary[f"hierarchical_at_{depth}"] == 0
        )
        summary[f"final_pool_loses_vs_hierarchical_at_{depth}"] = int(
            summary[f"hierarchical_at_{depth}"] == 1 and summary[f"final_pool_at_{depth}"] == 0
        )
    return summary


def _strategy_metrics(
    case_summaries: Sequence[Mapping[str, Any]],
    depths: Sequence[int],
    strategy: str,
) -> dict[str, Any]:
    rows = [row for row in case_summaries if row["pool_strategy"] == strategy]
    candidate_counts = [int(row["unique_candidates_final_pool"]) for row in rows]
    payload: dict[str, Any] = {
        "pool_strategy": strategy,
        "operational_final_pool": True,
        "cases_total": len(rows),
        "average_unique_candidates_per_case": _mean([float(value) for value in candidate_counts]),
        "median_unique_candidates_per_case": _median([float(value) for value in candidate_counts]),
    }
    families = [
        "hierarchical",
        "dual",
        "union_oracle",
        "final_pool",
        "hierarchical_clase",
        "dual_clase",
        "union_oracle_clase",
        "final_pool_clase",
        "hierarchical_partida",
        "dual_partida",
        "union_oracle_partida",
        "final_pool_partida",
        "hierarchical_sub_partida",
        "dual_sub_partida",
        "union_oracle_sub_partida",
        "final_pool_sub_partida",
    ]
    for depth in depths:
        for family in families:
            payload[f"{family}_at_{depth}"] = _mean([float(row[f"{family}_at_{depth}"]) for row in rows])
        payload[f"dual_rescues_vs_hierarchical_at_{depth}"] = sum(
            int(row[f"dual_rescues_vs_hierarchical_at_{depth}"]) for row in rows
        )
        payload[f"dual_loses_vs_hierarchical_at_{depth}"] = sum(
            int(row[f"dual_loses_vs_hierarchical_at_{depth}"]) for row in rows
        )
        payload[f"both_recover_at_{depth}"] = sum(int(row[f"both_recover_at_{depth}"]) for row in rows)
        payload[f"neither_recovers_at_{depth}"] = sum(int(row[f"neither_recovers_at_{depth}"]) for row in rows)
        payload[f"final_pool_rescues_vs_hierarchical_at_{depth}"] = sum(
            int(row[f"final_pool_rescues_vs_hierarchical_at_{depth}"]) for row in rows
        )
        payload[f"final_pool_loses_vs_hierarchical_at_{depth}"] = sum(
            int(row[f"final_pool_loses_vs_hierarchical_at_{depth}"]) for row in rows
        )
    return payload


def _source_contribution_rows(
    metrics_by_strategy: Mapping[str, Mapping[str, Any]],
    depths: Sequence[int],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for strategy, metrics in metrics_by_strategy.items():
        for depth in depths:
            rows.append(
                {
                    "pool_strategy": strategy,
                    "depth": depth,
                    "hierarchical_at_k": metrics[f"hierarchical_at_{depth}"],
                    "dual_at_k": metrics[f"dual_at_{depth}"],
                    "union_oracle_at_k": metrics[f"union_oracle_at_{depth}"],
                    "final_pool_at_k": metrics[f"final_pool_at_{depth}"],
                    "dual_rescues_vs_hierarchical_cases": metrics[f"dual_rescues_vs_hierarchical_at_{depth}"],
                    "dual_loses_vs_hierarchical_cases": metrics[f"dual_loses_vs_hierarchical_at_{depth}"],
                    "both_recover_cases": metrics[f"both_recover_at_{depth}"],
                    "neither_recovers_cases": metrics[f"neither_recovers_at_{depth}"],
                    "final_pool_rescues_vs_hierarchical_cases": metrics[
                        f"final_pool_rescues_vs_hierarchical_at_{depth}"
                    ],
                    "final_pool_loses_vs_hierarchical_cases": metrics[f"final_pool_loses_vs_hierarchical_at_{depth}"],
                }
            )
    return rows


def _rescue_loss_rows(case_summaries: Sequence[Mapping[str, Any]], max_depth: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in case_summaries:
        category = ""
        if int(row[f"dual_rescues_vs_hierarchical_at_{max_depth}"]):
            category = "dual_rescues_vs_hierarchical"
        elif int(row[f"dual_loses_vs_hierarchical_at_{max_depth}"]):
            category = "dual_loses_vs_hierarchical"
        elif int(row[f"both_recover_at_{max_depth}"]):
            category = "both_recover"
        elif int(row[f"neither_recovers_at_{max_depth}"]):
            category = "neither_recovers"
        rows.append(
            {
                "pool_strategy": row["pool_strategy"],
                "case_id": row["case_id"],
                "nandina_ref": row["nandina_ref"],
                "descripcion": row["descripcion"],
                "depth": max_depth,
                "source_category": category,
                "expected_code_rank_hierarchical": row["expected_code_rank_hierarchical"],
                "expected_code_rank_dual": row["expected_code_rank_dual"],
                "expected_code_rank_final_pool": row["expected_code_rank_final_pool"],
                f"hierarchical_at_{max_depth}": row[f"hierarchical_at_{max_depth}"],
                f"dual_at_{max_depth}": row[f"dual_at_{max_depth}"],
                f"union_oracle_at_{max_depth}": row[f"union_oracle_at_{max_depth}"],
                f"final_pool_at_{max_depth}": row[f"final_pool_at_{max_depth}"],
                f"final_pool_rescues_vs_hierarchical_at_{max_depth}": row[
                    f"final_pool_rescues_vs_hierarchical_at_{max_depth}"
                ],
                f"final_pool_loses_vs_hierarchical_at_{max_depth}": row[
                    f"final_pool_loses_vs_hierarchical_at_{max_depth}"
                ],
            }
        )
    return rows


def _summary_markdown(metrics: Mapping[str, Any]) -> str:
    depths = metrics["parameters"]["pool_depths"]
    max_depth = max(depths)
    lines = [
        "# Candidate pool normativo data_aduanas clase 87 v0.1",
        "",
        "## Alcance",
        "",
        "Construccion y evaluacion de pools normativos para `data_aduanas` clase 87. No usa historico real, Dense, LLM, Ollama, Text2Trade ni APIs remotas.",
        "",
        "## Fuentes normativas",
        "",
        f"- Ranking jerarquico: `{HIERARCHICAL_METHOD}`.",
        f"- Fuente dual auxiliar: `{DUAL_METHOD}`.",
        "- `union_oracle` mide cobertura potencial de la union Top-K de ambos recuperadores; no es un pool operativo ordenado.",
        "- `final_pool` mide el pool efectivamente entregable para cada estrategia.",
        "",
        "## Metricas exactas",
        "",
        "| Estrategia | K | Hierarchical | Dual | Union oracle | Final pool |",
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
            "## Metricas jerarquicas",
            "",
            "| Estrategia | K | Partida final | Sub Partida final | Clase final |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for strategy, item in metrics["metrics_by_strategy"].items():
        for depth in FAMILY_DEPTHS:
            lines.append(
                f"| {strategy} | {depth} | {item[f'final_pool_partida_at_{depth}']:.4f} | {item[f'final_pool_sub_partida_at_{depth}']:.4f} | {item[f'final_pool_clase_at_{depth}']:.4f} |"
            )
    lines.extend(
        [
            "",
            "## Aporte dual",
            "",
            f"| Estrategia | Rescates dual@{max_depth} | Perdidas dual@{max_depth} | Ambos@{max_depth} | Ninguno@{max_depth} | Rescates final@{max_depth} | Perdidas final@{max_depth} |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for strategy, item in metrics["metrics_by_strategy"].items():
        lines.append(
            f"| {strategy} | {item[f'dual_rescues_vs_hierarchical_at_{max_depth}']} | {item[f'dual_loses_vs_hierarchical_at_{max_depth}']} | {item[f'both_recover_at_{max_depth}']} | {item[f'neither_recovers_at_{max_depth}']} | {item[f'final_pool_rescues_vs_hierarchical_at_{max_depth}']} | {item[f'final_pool_loses_vs_hierarchical_at_{max_depth}']} |"
        )
    lines.extend(
        [
            "",
            "## Decision",
            "",
            f"Mejor pool operativo por exactitud a Top-100: `{metrics['best_final_pool_strategy_at_100']}`.",
            f"Mejor pool operativo por exactitud a Top-{max_depth}: `{metrics['best_final_pool_strategy_at_max_depth']}`.",
            "El pool normativo queda como respaldo/trazabilidad frente al futuro pool historico de Fase 9; no se promueve como fuente principal para clase 87.",
            "",
        ]
    )
    return "\n".join(lines)


def build(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    input_csv = resolve_project_path(args.input_csv)
    output_dir = resolve_project_path(args.output_dir)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    ablation_index_dir = resolve_project_path(args.ablation_index_dir)
    precision_index_path = ablation_index_dir / f"{PRECISION_VARIANT}.pkl"
    recall_index_path = ablation_index_dir / f"{RECALL_VARIANT}.pkl"
    pool_depths = sorted({int(depth.strip()) for depth in args.pool_depths.split(",") if depth.strip()})
    if not pool_depths or any(depth <= 0 for depth in pool_depths):
        raise ValueError("--pool-depths must contain positive integers.")
    max_pool_depth = max(pool_depths)

    rows = _read_csv(input_csv)
    warnings = _validate_evalset(rows, args.query_column, args.label_column)
    start = time.time()

    hierarchical_index = load_bm25_index(hierarchical_index_path)
    precision_index = load_bm25_index(precision_index_path)
    recall_index = load_bm25_index(recall_index_path)

    candidate_rows: list[dict[str, Any]] = []
    case_summaries: list[dict[str, Any]] = []
    for position, input_row in enumerate(rows, start=1):
        descripcion = _clean(input_row.get(args.query_column))
        true_code = _normalize_code(input_row.get(args.label_column))
        case_id = _clean(input_row.get("case_id")) or f"DA-EVAL-{position:05d}"

        hierarchical_hits = retrieve(hierarchical_index, descripcion, top_n=max_pool_depth)
        precision_hits = retrieve(precision_index, descripcion, top_n=max_pool_depth)
        recall_hits = retrieve(recall_index, descripcion, top_n=max_pool_depth)
        dual_hits = _protected_top_5_backfill(precision_hits, recall_hits, depth=max_pool_depth)

        for strategy in POOL_STRATEGIES:
            pool_hits = _final_pool(hierarchical_hits, dual_hits, max_pool_depth, strategy)
            candidate_rows.extend(
                _candidate_rows_for_case(case_id, descripcion, true_code, hierarchical_hits, dual_hits, pool_hits, strategy)
            )
            case_summaries.append(
                _case_summary(case_id, descripcion, true_code, hierarchical_hits, dual_hits, pool_hits, pool_depths, strategy)
            )

    metrics_by_strategy = {
        strategy: _strategy_metrics(case_summaries, pool_depths, strategy)
        for strategy in POOL_STRATEGIES
    }
    best_100 = max(
        metrics_by_strategy,
        key=lambda strategy: (
            metrics_by_strategy[strategy].get("final_pool_at_100", 0.0),
            metrics_by_strategy[strategy].get("final_pool_partida_at_100", 0.0),
            metrics_by_strategy[strategy].get("final_pool_clase_at_100", 0.0),
        ),
    )
    best_max = max(
        metrics_by_strategy,
        key=lambda strategy: (
            metrics_by_strategy[strategy][f"final_pool_at_{max_pool_depth}"],
            metrics_by_strategy[strategy][f"final_pool_partida_at_{max_pool_depth}"],
            metrics_by_strategy[strategy][f"final_pool_clase_at_{max_pool_depth}"],
        ),
    )

    source_contribution = _source_contribution_rows(metrics_by_strategy, pool_depths)
    rescue_loss = _rescue_loss_rows(case_summaries, max_pool_depth)
    params = {
        "dataset": "data_aduanas_evalset_clase87",
        "query_column": args.query_column,
        "label_column": args.label_column,
        "pool_depths": pool_depths,
        "pool_max_depth": max_pool_depth,
        "hier_depth": max_pool_depth,
        "dual_depth": max_pool_depth,
        "dual_rule": "protected_top_5_backfill",
        "protected_top_n": PROTECTED_TOP_N,
        "final_pool_strategies": list(POOL_STRATEGIES.keys()),
        "union_oracle_strategy": "union_oracle_100_diagnostic_only_not_ordered_pool",
        "top_200_extension_policy": (
            "The first 100 slots keep inherited Phase 7A rules; ranks 101-200 are filled deterministically "
            "with remaining normative candidates from hierarchical and dual sources."
        ),
        "historical_real_used_for_retrieval": False,
        "flat_bm25_used_as_source": False,
        "hierarchical_index_path": _rel(hierarchical_index_path, root),
        "precision_index_path": _rel(precision_index_path, root),
        "recall_index_path": _rel(recall_index_path, root),
    }
    metrics: dict[str, Any] = {
        "script": "src.experiments.build_candidate_pool_data_aduanas",
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
        "scope": {
            "source": "data_aduanas",
            "class": EXPECTED_SCOPE_CLASS,
            "phase": "7A updated normative candidate pool",
            "historical_role": "reference_for_future_phase_9_only_not_retrieval_source",
        },
        "input": {
            "evalset_path": _rel(input_csv, root),
            "evalset_sha256": sha256_file(input_csv),
            "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
            "precision_index_sha256": sha256_file(precision_index_path),
            "recall_index_sha256": sha256_file(recall_index_path),
        },
        "parameters": params,
        "cases_total": len(rows),
        "pool_strategies": list(POOL_STRATEGIES.keys()),
        "diagnostic_ceiling": {
            "union_oracle_100": metrics_by_strategy["hierarchical_only"]["union_oracle_at_100"],
            f"union_oracle_{max_pool_depth}": metrics_by_strategy["hierarchical_only"][
                f"union_oracle_at_{max_pool_depth}"
            ],
            "note": "Union oracle is computed from Top-K hierarchical plus Top-K dual and is not an ordered deliverable pool.",
        },
        "best_final_pool_strategy_at_100": best_100,
        "best_final_pool_strategy_at_max_depth": best_max,
        "metrics_by_strategy": metrics_by_strategy,
        "validations": {
            "evalset_rows": len(rows),
            "expected_rows": EXPECTED_EVALSET_ROWS,
            "empty_queries": 0,
            "invalid_expected_labels": 0,
            "expected_labels_nandina8": True,
            "case_summary_rows": len(case_summaries),
            "case_summary_rows_per_strategy": len(rows),
            "candidate_pool_rows": len(candidate_rows),
            "candidate_pool_rows_expected_if_all_strategies_full_depth": len(rows) * len(POOL_STRATEGIES) * max_pool_depth,
            "union_oracle_distinct_from_final_pool": any(
                abs(
                    metrics_by_strategy[strategy]["union_oracle_at_100"]
                    - metrics_by_strategy[strategy]["final_pool_at_100"]
                )
                > 0.0
                for strategy in POOL_STRATEGIES
            ),
        },
        "controls": {
            "llm_executed": False,
            "ollama_executed": False,
            "text2trade_executed": False,
            "dense_executed": False,
            "remote_apis_used": False,
            "historical_real_retrieval_used": False,
            "rules_adjusted_after_evalset": False,
            "legacy_evalset_modified": False,
            "legacy_devset_modified": False,
            "data_aduanas_splits_modified": False,
            "source_excel_modified": False,
        },
        "outputs": {
            "candidate_pool_csv": _rel(output_dir / "candidate_pool.csv", root),
            "candidate_pool_case_summary_csv": _rel(output_dir / "candidate_pool_case_summary.csv", root),
            "candidate_pool_metrics_json": _rel(output_dir / "candidate_pool_metrics.json", root),
            "candidate_pool_summary_md": _rel(output_dir / "candidate_pool_summary.md", root),
            "source_contribution_csv": _rel(output_dir / "source_contribution.csv", root),
            "rescue_loss_cases_csv": _rel(output_dir / "rescue_loss_cases.csv", root),
        },
        "warnings": warnings
        + [
            "No historical real data is used for retrieval in this Phase 7A normative pool.",
            "union_oracle is a diagnostic ceiling, not an ordered final pool.",
            "Outputs are regenerable and should remain ignored by Git.",
        ],
    }

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
        "source_membership_final_pool",
        "hierarchical_score",
        "dual_score",
        "clase_candidate",
        "partida_candidate",
        "sub_partida_candidate",
        "is_expected_code",
        "is_expected_clase",
        "is_expected_partida",
        "is_expected_sub_partida",
        "evidence_text",
    ]
    case_fields = list(case_summaries[0].keys()) if case_summaries else []
    source_fields = list(source_contribution[0].keys()) if source_contribution else []
    rescue_loss_fields = list(rescue_loss[0].keys()) if rescue_loss else []

    _write_csv(output_dir / "candidate_pool.csv", candidate_rows, candidate_fields)
    _write_csv(output_dir / "candidate_pool_case_summary.csv", case_summaries, case_fields)
    _write_json(output_dir / "candidate_pool_metrics.json", metrics)
    ensure_parent(output_dir / "candidate_pool_summary.md")
    (output_dir / "candidate_pool_summary.md").write_text(_summary_markdown(metrics), encoding="utf-8")
    _write_csv(output_dir / "source_contribution.csv", source_contribution, source_fields)
    _write_csv(output_dir / "rescue_loss_cases.csv", rescue_loss, rescue_loss_fields)
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build normative candidate pools for data_aduanas Clase 87.")
    parser.add_argument("--input-csv", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--query-column", default=QUERY_COLUMN)
    parser.add_argument("--label-column", default=LABEL_COLUMN)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--ablation-index-dir", type=Path, default=DEFAULT_ABLATION_INDEX_DIR)
    parser.add_argument("--pool-depths", default="10,20,50,100,200")
    return parser


def main() -> int:
    metrics = build(build_parser().parse_args())
    print("OK: candidate pool normativo data_aduanas clase 87 completado")
    print(f"casos={metrics['cases_total']} estrategias={','.join(metrics['pool_strategies'])}")
    print(f"union_oracle@100={metrics['diagnostic_ceiling']['union_oracle_100']:.4f}")
    for strategy, item in metrics["metrics_by_strategy"].items():
        print(
            f"{strategy}: final_pool@100={item['final_pool_at_100']:.4f} "
            f"final_pool@200={item['final_pool_at_200']:.4f} "
            f"partida@100={item['final_pool_partida_at_100']:.4f} "
            f"subpartida@100={item['final_pool_sub_partida_at_100']:.4f} "
            f"clase@100={item['final_pool_clase_at_100']:.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
