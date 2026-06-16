from __future__ import annotations

import argparse
import csv
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve as bm25_retrieve
from ..utils.paths import ensure_parent, load_json, project_root, resolve_project_path

DEFAULT_CONFIG = Path("src/configs/experiment_config.json")
DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_MULTIQUERIES = Path("outputs/evaluation/multiquery_rrf_devset_v0.1/multiqueries.jsonl")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/weighted_bm25_multiquery_devset_v0.1")
DEFAULT_K_LIST = [1, 3, 5, 10]
DEFAULT_WEIGHTS = {"Q0": 3.0, "Q1": 1.0, "Q2": 0.5}
EXPECTED_DEVSET_ROWS = 13
METHODS = [
    "BM25_Q0_baseline",
    "BM25_Q0_Q1_Q2_weighted_RRF",
    "BM25_Q0_Q1_Q2_weighted_RRF_protected",
]


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {line_number}") from exc
            if not isinstance(payload, dict):
                raise ValueError(f"Invalid JSON object in {path} at line {line_number}")
            rows.append(payload)
    return rows


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


def _report_path(path: Path, root: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return str(resolved)


def _parse_k_list(raw: str | None, fallback: Sequence[int]) -> list[int]:
    if raw:
        values = [int(part.strip()) for part in raw.split(",") if part.strip()]
    else:
        values = list(fallback)
    values = sorted(set(values))
    if not values or any(value <= 0 for value in values):
        raise ValueError("k-list must contain positive integers")
    return values


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _rank(candidates: Sequence[Mapping[str, Any]], true_code: str) -> int:
    for idx, hit in enumerate(candidates, start=1):
        if _clean(hit.get("code")) == _clean(true_code):
            return idx
    return 0


def _case_outcome(baseline_rank: int, candidate_rank: int) -> str:
    baseline = baseline_rank if baseline_rank > 0 else 10**9
    candidate = candidate_rank if candidate_rank > 0 else 10**9
    if candidate < baseline:
        return "ganado"
    if candidate > baseline:
        return "perdido"
    return "sin_cambio"


def _family_hit(candidates: Sequence[Mapping[str, Any]], true_code: str, family_len: int, k: int) -> int:
    ref = _clean(true_code)[:family_len]
    if not ref:
        return 0
    for hit in candidates[:k]:
        if _clean(hit.get("code"))[:family_len] == ref:
            return 1
    return 0


def _recall_at_rank(rank: int, k: int) -> int:
    return int(0 < rank <= k)


def _pool_recall(source_hits: Mapping[str, Sequence[Mapping[str, Any]]], true_code: str, k: int) -> int:
    for hits in source_hits.values():
        for hit in hits[:k]:
            if _clean(hit.get("code")) == _clean(true_code):
                return 1
    return 0


def _normalize_baseline(hits: Sequence[Mapping[str, Any]], source: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for hit in hits:
        payload = dict(hit)
        payload["rank"] = int(hit.get("rank", len(rows) + 1))
        payload["sources"] = [f"{source}:{payload['rank']}"]
        payload["weighted_score"] = float(hit.get("score", 0.0))
        payload["score"] = payload["weighted_score"]
        rows.append(payload)
    return rows


def _weighted_rrf(
    source_hits: Mapping[str, Sequence[Mapping[str, Any]]],
    *,
    weights: Mapping[str, float],
    rrf_k: int,
) -> list[dict[str, Any]]:
    fused: dict[str, dict[str, Any]] = {}
    for label, hits in source_hits.items():
        weight = float(weights[label])
        source = f"BM25_{label}"
        seen: set[str] = set()
        for hit in hits:
            code = _clean(hit.get("code"))
            if not code or code in seen:
                continue
            seen.add(code)
            rank = int(hit.get("rank", 0))
            if rank <= 0:
                continue
            contribution = weight * (1.0 / float(rrf_k + rank))
            entry = fused.setdefault(
                code,
                {
                    "code": code,
                    "weighted_score": 0.0,
                    "score": 0.0,
                    "text": _clean(hit.get("text")),
                    "doc_idx": hit.get("doc_idx", ""),
                    "sources": [],
                    "source_ranks": {},
                    "source_weights": {},
                },
            )
            entry["weighted_score"] += contribution
            entry["score"] = entry["weighted_score"]
            entry["sources"].append(f"{source}:{rank}:w{weight:g}")
            entry["source_ranks"][source] = rank
            entry["source_weights"][source] = weight
            if not entry.get("text"):
                entry["text"] = _clean(hit.get("text"))
    ordered = sorted(fused.values(), key=lambda item: (-float(item["weighted_score"]), _clean(item["code"])))
    for rank, item in enumerate(ordered, start=1):
        item["rank"] = rank
        item["sources"] = sorted(item["sources"])
    return ordered


def _protected_ranking(
    weighted: Sequence[Mapping[str, Any]],
    q0_hits: Sequence[Mapping[str, Any]],
    *,
    protected_k: int,
) -> list[dict[str, Any]]:
    by_code = {_clean(hit.get("code")): dict(hit) for hit in weighted}
    protected_codes = [_clean(hit.get("code")) for hit in q0_hits[:protected_k] if _clean(hit.get("code"))]
    protected_set = set(protected_codes)

    protected_hits = []
    for code in protected_codes:
        if code in by_code:
            protected_hits.append(by_code[code])
    protected_hits = sorted(protected_hits, key=lambda item: (-float(item["weighted_score"]), protected_codes.index(_clean(item["code"]))))

    tail = [dict(hit) for hit in weighted if _clean(hit.get("code")) not in protected_set]
    ordered = protected_hits + tail
    for rank, item in enumerate(ordered, start=1):
        item["rank"] = rank
    return ordered


def _compact_top(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    compact: list[dict[str, Any]] = []
    for hit in candidates[:limit]:
        compact.append(
            {
                "rank": int(hit.get("rank", len(compact) + 1)),
                "code": _clean(hit.get("code")),
                "score": float(hit.get("weighted_score", hit.get("score", 0.0))),
                "sources": list(hit.get("sources", [])),
                "text": _clean(hit.get("text")),
            }
        )
    return compact


def _format_top(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    parts: list[str] = []
    for hit in candidates[:limit]:
        sources = ",".join(str(item) for item in hit.get("sources", []))
        score = float(hit.get("weighted_score", hit.get("score", 0.0)))
        parts.append(f"{int(hit.get('rank', len(parts) + 1))}:{_clean(hit.get('code'))}:{score:.6f}:[{sources}]")
    return " | ".join(parts)


def _metrics_for_method(
    rows: Sequence[Mapping[str, Any]],
    method: str,
    *,
    k_list: Sequence[int],
    max_k: int,
) -> dict[str, Any]:
    ranks = [int(row[f"rank_{method}"]) for row in rows]
    top_json_field = f"top_{max_k}_{method}_json"
    metrics: dict[str, Any] = {
        "cases_total": len(rows),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        f"no_match_top_{max_k}": sum(1 for rank in ranks if rank <= 0 or rank > max_k),
        "not_found": sum(1 for rank in ranks if rank <= 0),
    }
    for k in k_list:
        metrics[f"top_{k}_accuracy"] = _mean([acc_at_k(rank, k) for rank in ranks])
    metrics[f"top_{max_k}_hs4_accuracy"] = _mean(
        [_family_hit(json.loads(_clean(row.get(top_json_field)) or "[]"), _clean(row["nandina_ref"]), 4, max_k) for row in rows]
    )
    metrics[f"top_{max_k}_hs2_accuracy"] = _mean(
        [_family_hit(json.loads(_clean(row.get(top_json_field)) or "[]"), _clean(row["nandina_ref"]), 2, max_k) for row in rows]
    )
    metrics["recall_50"] = _mean([int(row[f"recall_50_{method}"]) for row in rows])
    metrics["recall_100"] = _mean([int(row[f"recall_100_{method}"]) for row in rows])
    return metrics


def _comparison(rows: Sequence[Mapping[str, Any]], method: str) -> dict[str, int]:
    outcomes = [_case_outcome(int(row["rank_BM25_Q0_baseline"]), int(row[f"rank_{method}"])) for row in rows]
    return {
        "ganados": sum(1 for outcome in outcomes if outcome == "ganado"),
        "perdidos": sum(1 for outcome in outcomes if outcome == "perdido"),
        "sin_cambio": sum(1 for outcome in outcomes if outcome == "sin_cambio"),
    }


def _summary_markdown(metrics: Mapping[str, Any]) -> str:
    lines = [
        "# Weighted BM25 multi-query devset v0.1",
        "",
        "## Alcance",
        "",
        "Evaluacion BM25 devset con Q0, Q1 y Q2. No se ejecuto LLM, Text2Trade ni evalset final.",
        "",
        "## Metricas",
        "",
        "| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Top-10 HS4 | Top-10 HS2 | Recall@50 | Recall@100 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in METHODS:
        data = metrics["methods"][method]
        lines.append(
            f"| {method} | {data['top_1_accuracy']:.4f} | {data['top_3_accuracy']:.4f} | "
            f"{data['top_5_accuracy']:.4f} | {data['top_10_accuracy']:.4f} | {data['mrr']:.4f} | "
            f"{data['top_10_hs4_accuracy']:.4f} | {data['top_10_hs2_accuracy']:.4f} | "
            f"{data['recall_50']:.4f} | {data['recall_100']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Diagnostico",
            "",
            f"- Expulsiones Top-10 sin proteccion: {metrics['diagnostics']['q0_top10_expected_expelled_by_weighted_cases']}.",
            f"- Expulsiones evitadas por proteccion: {metrics['diagnostics']['protection_prevented_expected_top10_expulsion_cases']}.",
            f"- Casos donde Q1/Q2 trajeron la NANDINA y Q0 no: {metrics['diagnostics']['q1_q2_brought_expected_when_q0_absent_cases']}.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    config_path = resolve_project_path(args.config)
    config = load_json(config_path)
    paths = config.get("paths", {})
    base_dir = paths.get("base_dir") or "."
    bm25_cfg = config.get("bm25", {})

    devset_path = resolve_project_path(args.devset, base_dir=base_dir)
    multiqueries_path = resolve_project_path(args.multiqueries, base_dir=base_dir)
    output_dir = resolve_project_path(args.output_dir, base_dir=base_dir)
    index_path = resolve_project_path(
        args.index or paths.get("bm25_index_path", "data/processed/indexes/bm25_nandina8.pkl"),
        base_dir=base_dir,
    )
    k_list = _parse_k_list(args.k_list, bm25_cfg.get("k_list") or DEFAULT_K_LIST)
    max_k = max(k_list)
    retrieval_depth = max(args.retrieval_depth or int(bm25_cfg.get("top_n", 100)), 100, max_k)
    weights = {"Q0": args.q0_weight, "Q1": args.q1_weight, "Q2": args.q2_weight}

    if not multiqueries_path.exists():
        raise FileNotFoundError(f"Required previous multiquery output not found: {multiqueries_path}")

    dev_rows = _read_csv(devset_path)
    multiquery_rows = _read_jsonl(multiqueries_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")
    if len(multiquery_rows) != len(dev_rows):
        raise ValueError(f"Multiquery row count is {len(multiquery_rows)}, expected {len(dev_rows)}.")

    bm25_index = load_bm25_index(index_path)
    case_rows: list[dict[str, Any]] = []
    candidate_rows: list[dict[str, Any]] = []
    start = time.time()

    for position, (dev_row, mq_row) in enumerate(zip(dev_rows, multiquery_rows), start=1):
        descripcion = _clean(dev_row.get("descripcion"))
        nandina_ref = _clean(dev_row.get("nandina"))
        case_id = _clean(mq_row.get("case_id")) or f"dev-{position:02d}"
        queries = {
            "Q0": descripcion,
            "Q1": _clean(mq_row.get("q1_limpia")),
            "Q2": _clean(mq_row.get("q2_expandida")),
        }

        source_hits = {label: bm25_retrieve(bm25_index, query, top_n=retrieval_depth) if query else [] for label, query in queries.items()}
        baseline = _normalize_baseline(source_hits["Q0"], "BM25_Q0")
        weighted = _weighted_rrf(source_hits, weights=weights, rrf_k=args.rrf_k)
        protected = _protected_ranking(weighted, source_hits["Q0"], protected_k=max_k)
        method_candidates = {
            "BM25_Q0_baseline": baseline,
            "BM25_Q0_Q1_Q2_weighted_RRF": weighted,
            "BM25_Q0_Q1_Q2_weighted_RRF_protected": protected,
        }

        q0_rank = rank_of_true(source_hits["Q0"], nandina_ref)
        q1_rank = rank_of_true(source_hits["Q1"], nandina_ref)
        q2_rank = rank_of_true(source_hits["Q2"], nandina_ref)
        weighted_rank = _rank(weighted, nandina_ref)
        protected_rank = _rank(protected, nandina_ref)
        q0_top10_expected_expelled = int(0 < q0_rank <= max_k and (weighted_rank <= 0 or weighted_rank > max_k))
        protection_prevented = int(q0_top10_expected_expelled and 0 < protected_rank <= max_k)
        q1_q2_brought_when_q0_absent = int(q0_rank <= 0 and (q1_rank > 0 or q2_rank > 0))

        case: dict[str, Any] = {
            "case_id": case_id,
            "nandina_ref": nandina_ref,
            "Q0": queries["Q0"],
            "Q1": queries["Q1"],
            "Q2": queries["Q2"],
            "rank_BM25_Q0_baseline": q0_rank,
            "rank_BM25_Q0_Q1_Q2_weighted_RRF": weighted_rank,
            "rank_BM25_Q0_Q1_Q2_weighted_RRF_protected": protected_rank,
            "rank_Q1": q1_rank,
            "rank_Q2": q2_rank,
            "recall_50_Q0": _recall_at_rank(q0_rank, 50),
            "recall_100_Q0": _recall_at_rank(q0_rank, 100),
            "recall_50_pool_Q0_Q1_Q2": _pool_recall(source_hits, nandina_ref, 50),
            "recall_100_pool_Q0_Q1_Q2": _pool_recall(source_hits, nandina_ref, 100),
            "resultado_weighted_vs_Q0": _case_outcome(q0_rank, weighted_rank),
            "resultado_protected_vs_Q0": _case_outcome(q0_rank, protected_rank),
            "q0_top10_protegido": int(len(source_hits["Q0"]) >= max_k),
            "nandina_esperada_expulsada_sin_proteccion": q0_top10_expected_expelled,
            "proteccion_evito_expulsion_nandina_esperada": protection_prevented,
            "q1_q2_trajeron_nandina_si_q0_no": q1_q2_brought_when_q0_absent,
            "multiqueries_source": _report_path(multiqueries_path, root),
        }
        for method, candidates in method_candidates.items():
            rank = _rank(candidates, nandina_ref)
            case[f"rank_{method}"] = rank
            case[f"recall_50_{method}"] = _recall_at_rank(rank, 50)
            case[f"recall_100_{method}"] = _recall_at_rank(rank, 100)
            case[f"top_{max_k}_{method}"] = _format_top(candidates, max_k)
            case[f"top_{max_k}_{method}_json"] = json.dumps(_compact_top(candidates, max_k), ensure_ascii=False)
        case["top_10_final_weighted"] = case[f"top_{max_k}_BM25_Q0_Q1_Q2_weighted_RRF"]
        case["top_10_final_protected"] = case[f"top_{max_k}_BM25_Q0_Q1_Q2_weighted_RRF_protected"]
        case_rows.append(case)

        for method, candidates in method_candidates.items():
            for hit in candidates[:max_k]:
                candidate_rows.append(
                    {
                        "case_id": case_id,
                        "method": method,
                        "candidate_rank": int(hit.get("rank", 0)),
                        "candidate_code": _clean(hit.get("code")),
                        "candidate_score": float(hit.get("weighted_score", hit.get("score", 0.0))),
                        "candidate_sources": "; ".join(str(item) for item in hit.get("sources", [])),
                        "candidate_text": _clean(hit.get("text")),
                        "is_expected_nandina": int(_clean(hit.get("code")) == nandina_ref),
                    }
                )

    method_metrics = {method: _metrics_for_method(case_rows, method, k_list=k_list, max_k=max_k) for method in METHODS}
    comparison = {method: _comparison(case_rows, method) for method in METHODS if method != "BM25_Q0_baseline"}
    diagnostics = {
        "q0_top10_expected_expelled_by_weighted_cases": sum(int(row["nandina_esperada_expulsada_sin_proteccion"]) for row in case_rows),
        "protection_prevented_expected_top10_expulsion_cases": sum(
            int(row["proteccion_evito_expulsion_nandina_esperada"]) for row in case_rows
        ),
        "q1_q2_brought_expected_when_q0_absent_cases": sum(int(row["q1_q2_trajeron_nandina_si_q0_no"]) for row in case_rows),
        "q0_recall_50": _mean([int(row["recall_50_Q0"]) for row in case_rows]),
        "q0_recall_100": _mean([int(row["recall_100_Q0"]) for row in case_rows]),
        "pool_q0_q1_q2_recall_50": _mean([int(row["recall_50_pool_Q0_Q1_Q2"]) for row in case_rows]),
        "pool_q0_q1_q2_recall_100": _mean([int(row["recall_100_pool_Q0_Q1_Q2"]) for row in case_rows]),
        "q1_q2_new_correct_cases": [
            row["case_id"] for row in case_rows if int(row["q1_q2_trajeron_nandina_si_q0_no"])
        ],
        "weighted_lost_cases": [row["case_id"] for row in case_rows if row["resultado_weighted_vs_Q0"] == "perdido"],
        "protected_lost_cases": [row["case_id"] for row in case_rows if row["resultado_protected_vs_Q0"] == "perdido"],
    }

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_weighted_bm25_multiquery_devset",
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
            "devset_path": _report_path(devset_path, root),
            "devset_abs_path": str(devset_path),
            "devset_sha256": sha256_file(devset_path),
            "multiqueries_path": _report_path(multiqueries_path, root),
            "multiqueries_abs_path": str(multiqueries_path),
            "multiqueries_sha256": sha256_file(multiqueries_path),
            "bm25_index_path": _report_path(index_path, root),
            "bm25_index_abs_path": str(index_path),
            "bm25_index_sha256": sha256_file(index_path),
            "config_path": _report_path(config_path, root),
        },
        "bm25": {
            "k1": getattr(bm25_index, "k1", None),
            "b": getattr(bm25_index, "b", None),
            "docs_indexed": len(bm25_index.doc_ids),
            "avgdl": getattr(bm25_index, "avgdl", None),
            "vocab_size": len(getattr(bm25_index, "idf", {})),
            "retrieval_depth_per_query": retrieval_depth,
        },
        "weighted_rrf": {
            "rrf_k": args.rrf_k,
            "weights": weights,
            "queries_used": ["Q0", "Q1", "Q2"],
            "queries_ignored": ["Q3"],
            "protected_top_k": max_k,
            "uses_expected_label_for_protection": False,
        },
        "methods": method_metrics,
        "comparison_vs_bm25_q0": comparison,
        "diagnostics": diagnostics,
        "quality": {
            "cases_total": len(case_rows),
            "multiquery_rows_used": len(multiquery_rows),
            "used_existing_multiqueries_jsonl": True,
            "llm_executed": False,
            "text2trade_executed": False,
            "evalset_executed": False,
        },
        "warnings": [
            "Devset-only diagnostic; do not infer final evalset performance.",
            "Q0 was read from devset; Q1/Q2 were read from the previous multiqueries.jsonl.",
            "Q3 was intentionally ignored.",
        ],
        "output": {
            "output_dir": _report_path(output_dir, root),
            "output_abs_dir": str(output_dir),
            "weighted_results_csv": _report_path(output_dir / "weighted_results.csv", root),
            "weighted_metrics_json": _report_path(output_dir / "weighted_metrics.json", root),
            "weighted_summary_md": _report_path(output_dir / "weighted_summary.md", root),
            "weighted_case_comparison_13_cases_csv": _report_path(output_dir / "weighted_case_comparison_13_cases.csv", root),
        },
    }

    case_fieldnames = [
        "case_id",
        "nandina_ref",
        "Q0",
        "Q1",
        "Q2",
        "rank_BM25_Q0_baseline",
        "rank_BM25_Q0_Q1_Q2_weighted_RRF",
        "rank_BM25_Q0_Q1_Q2_weighted_RRF_protected",
        "recall_50_Q0",
        "recall_100_Q0",
        "recall_50_pool_Q0_Q1_Q2",
        "recall_100_pool_Q0_Q1_Q2",
        "resultado_weighted_vs_Q0",
        "resultado_protected_vs_Q0",
        "q0_top10_protegido",
        "nandina_esperada_expulsada_sin_proteccion",
        "proteccion_evito_expulsion_nandina_esperada",
        "q1_q2_trajeron_nandina_si_q0_no",
        "rank_Q1",
        "rank_Q2",
        "top_10_final_weighted",
        "top_10_final_protected",
        "multiqueries_source",
    ]
    _write_csv(output_dir / "weighted_case_comparison_13_cases.csv", case_rows, case_fieldnames)
    _write_csv(
        output_dir / "weighted_results.csv",
        candidate_rows,
        [
            "case_id",
            "method",
            "candidate_rank",
            "candidate_code",
            "candidate_score",
            "candidate_sources",
            "candidate_text",
            "is_expected_nandina",
        ],
    )
    _write_json(output_dir / "weighted_metrics.json", metrics)
    ensure_parent(output_dir / "weighted_summary.md")
    (output_dir / "weighted_summary.md").write_text(_summary_markdown(metrics), encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate weighted BM25 multi-query with protected Q0 Top-10 on devset.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--multiqueries", type=Path, default=DEFAULT_MULTIQUERIES)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--index", type=Path, default=None)
    parser.add_argument("--k-list", default=None)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument("--q0-weight", type=float, default=DEFAULT_WEIGHTS["Q0"])
    parser.add_argument("--q1-weight", type=float, default=DEFAULT_WEIGHTS["Q1"])
    parser.add_argument("--q2-weight", type=float, default=DEFAULT_WEIGHTS["Q2"])
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion weighted BM25 multi-query devset completada")
    print(f"Casos evaluados: {metrics['quality']['cases_total']}")
    print(f"Multiqueries existente usado: {metrics['quality']['used_existing_multiqueries_jsonl']}")
    for method in METHODS:
        data = metrics["methods"][method]
        print(
            f"{method}: Top-1={data['top_1_accuracy']:.4f} Top-3={data['top_3_accuracy']:.4f} "
            f"Top-5={data['top_5_accuracy']:.4f} Top-10={data['top_10_accuracy']:.4f} "
            f"MRR={data['mrr']:.4f} R@50={data['recall_50']:.4f} R@100={data['recall_100']:.4f}"
        )
    print(f"Expulsiones evitadas por proteccion: {metrics['diagnostics']['protection_prevented_expected_top10_expulsion_cases']}")
    print(f"Q1/Q2 trajeron NANDINA si Q0 no: {metrics['diagnostics']['q1_q2_brought_expected_when_q0_absent_cases']}")
    print(f"Outputs: {metrics['output']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
