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
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/multiquery_rrf_devset_v0.1")
DEFAULT_DENSE_ARTIFACT_DIR = Path("data/processed/indexes/text2trade_nandina8_v1")
DEFAULT_K_LIST = [1, 3, 5, 10]
EXPECTED_DEVSET_ROWS = 13
QUERY_LABELS = ("Q0", "Q1", "Q2", "Q3")
METHOD_ORDER = [
    "BM25_Q0_baseline",
    "BM25_multiquery_RRF",
    "Text2Trade_Q0_baseline",
    "Text2Trade_multiquery_RRF",
    "Hybrid_BM25_Text2Trade_multiquery_RRF",
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


def _case_outcome(baseline_rank: int, candidate_rank: int) -> str:
    baseline = baseline_rank if baseline_rank > 0 else 10**9
    candidate = candidate_rank if candidate_rank > 0 else 10**9
    if candidate < baseline:
        return "ganado"
    if candidate > baseline:
        return "perdido"
    return "sin_cambio"


def _normalize_hit(hit: Mapping[str, Any], source: str) -> dict[str, Any]:
    payload = dict(hit)
    payload["source"] = source
    payload["sources"] = [f"{source}:{int(hit.get('rank', 0))}"]
    payload["rrf_score"] = float(hit.get("score", 0.0))
    return payload


def _rrf_fuse(source_hits: Mapping[str, Sequence[Mapping[str, Any]]], *, rrf_k: int) -> list[dict[str, Any]]:
    fused: dict[str, dict[str, Any]] = {}
    for source, hits in source_hits.items():
        best_seen_in_source: set[str] = set()
        for hit in hits:
            code = _clean(hit.get("code"))
            if not code or code in best_seen_in_source:
                continue
            best_seen_in_source.add(code)
            rank = int(hit.get("rank", 0))
            if rank <= 0:
                continue
            contribution = 1.0 / float(rrf_k + rank)
            entry = fused.setdefault(
                code,
                {
                    "code": code,
                    "rrf_score": 0.0,
                    "text": _clean(hit.get("text")),
                    "doc_idx": hit.get("doc_idx", ""),
                    "doc_id": _clean(hit.get("doc_id")),
                    "sources": [],
                    "source_ranks": {},
                },
            )
            entry["rrf_score"] += contribution
            entry["sources"].append(f"{source}:{rank}")
            entry["source_ranks"][source] = rank
            if not entry.get("text"):
                entry["text"] = _clean(hit.get("text"))
    ordered = sorted(fused.values(), key=lambda item: (-float(item["rrf_score"]), _clean(item["code"])))
    for rank, item in enumerate(ordered, start=1):
        item["rank"] = rank
        item["score"] = item["rrf_score"]
        item["sources"] = sorted(item["sources"])
    return ordered


def _rank_from_candidates(candidates: Sequence[Mapping[str, Any]], true_code: str) -> int:
    for idx, hit in enumerate(candidates, start=1):
        if _clean(hit.get("code")) == _clean(true_code):
            return idx
    return 0


def _family_hit(candidates: Sequence[Mapping[str, Any]], true_code: str, family_len: int, k: int) -> int:
    ref = _clean(true_code)[:family_len]
    if not ref:
        return 0
    for hit in candidates[:k]:
        if _clean(hit.get("code"))[:family_len] == ref:
            return 1
    return 0


def _metrics_for_method(
    rows: Sequence[Mapping[str, Any]],
    method: str,
    *,
    k_list: Sequence[int],
    max_k: int,
) -> dict[str, Any]:
    ranks = [int(row[f"rank_{method}"]) for row in rows]
    metrics: dict[str, Any] = {
        "cases_total": len(rows),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        f"no_match_top_{max_k}": sum(1 for rank in ranks if rank <= 0 or rank > max_k),
        "not_found": sum(1 for rank in ranks if rank <= 0),
    }
    for k in k_list:
        metrics[f"top_{k}_accuracy"] = _mean([acc_at_k(rank, k) for rank in ranks])
    metrics[f"top_{max_k}_hs4_accuracy"] = _mean(
        [
            _family_hit(json.loads(_clean(row.get(f"top_{max_k}_{method}_json")) or "[]"), _clean(row["nandina_ref"]), 4, max_k)
            for row in rows
        ]
    )
    metrics[f"top_{max_k}_hs2_accuracy"] = _mean(
        [
            _family_hit(json.loads(_clean(row.get(f"top_{max_k}_{method}_json")) or "[]"), _clean(row["nandina_ref"]), 2, max_k)
            for row in rows
        ]
    )
    return metrics


def _comparison_vs_baseline(rows: Sequence[Mapping[str, Any]], method: str) -> dict[str, int]:
    outcomes = [_case_outcome(int(row["rank_BM25_Q0_baseline"]), int(row[f"rank_{method}"])) for row in rows]
    return {
        "ganados": sum(1 for outcome in outcomes if outcome == "ganado"),
        "perdidos": sum(1 for outcome in outcomes if outcome == "perdido"),
        "sin_cambio": sum(1 for outcome in outcomes if outcome == "sin_cambio"),
    }


def _compact_top(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    compact: list[dict[str, Any]] = []
    for hit in candidates[:limit]:
        compact.append(
            {
                "rank": int(hit.get("rank", len(compact) + 1)),
                "code": _clean(hit.get("code")),
                "score": float(hit.get("rrf_score", hit.get("score", 0.0))),
                "sources": list(hit.get("sources", [])),
                "text": _clean(hit.get("text")),
            }
        )
    return compact


def _format_top(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    parts = []
    for hit in candidates[:limit]:
        sources = ",".join(str(item) for item in hit.get("sources", []))
        score = float(hit.get("rrf_score", hit.get("score", 0.0)))
        parts.append(f"{int(hit.get('rank', len(parts) + 1))}:{_clean(hit.get('code'))}:{score:.6f}:[{sources}]")
    return " | ".join(parts)


def _load_dense_retriever(artifact_dir: Path, model_path: Path | None) -> tuple[Any | None, str]:
    try:
        from ..retrieval.dense_text2trade import DenseText2TradeRetriever

        return DenseText2TradeRetriever(artifact_dir, model_path=model_path), ""
    except Exception as exc:  # noqa: BLE001 - fallback is a required experiment behavior.
        return None, f"{type(exc).__name__}: {exc}"


def _summary_markdown(metrics: Mapping[str, Any], available_methods: Sequence[str]) -> str:
    lines = [
        "# Multi-query + RRF devset v0.1",
        "",
        "## Alcance",
        "",
        "Evaluacion sobre el devset preliminar de 13 casos. No se uso el evalset final.",
        "",
        "## Metricas",
        "",
        "| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Top-10 HS4 | Top-10 HS2 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in available_methods:
        data = metrics["methods"][method]
        lines.append(
            f"| {method} | {data['top_1_accuracy']:.4f} | {data['top_3_accuracy']:.4f} | "
            f"{data['top_5_accuracy']:.4f} | {data['top_10_accuracy']:.4f} | {data['mrr']:.4f} | "
            f"{data['top_10_hs4_accuracy']:.4f} | {data['top_10_hs2_accuracy']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Comparacion contra BM25_Q0_baseline",
            "",
            "| Metodo | Ganados | Perdidos | Sin cambio |",
            "|---|---:|---:|---:|",
        ]
    )
    for method, data in metrics["comparison_vs_bm25_q0"].items():
        lines.append(f"| {method} | {data['ganados']} | {data['perdidos']} | {data['sin_cambio']} |")
    lines.extend(
        [
            "",
            "## Text2Trade",
            "",
            f"- Disponible: {metrics['dense']['available']}.",
        ]
    )
    if not metrics["dense"]["available"]:
        lines.append(f"- Motivo: {metrics['dense']['error']}.")
    lines.append("")
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
    dense_artifact_dir = resolve_project_path(args.dense_artifact_dir, base_dir=base_dir)
    dense_model_path = resolve_project_path(args.dense_model_path, base_dir=base_dir) if args.dense_model_path else dense_artifact_dir / "model"
    k_list = _parse_k_list(args.k_list, bm25_cfg.get("k_list") or DEFAULT_K_LIST)
    max_k = max(k_list)
    retrieval_depth = args.retrieval_depth or int(bm25_cfg.get("top_n", max_k))
    retrieval_depth = max(retrieval_depth, max_k)

    dev_rows = _read_csv(devset_path)
    multiquery_rows = _read_jsonl(multiqueries_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")
    if len(multiquery_rows) != len(dev_rows):
        raise ValueError(f"Multiquery row count is {len(multiquery_rows)}, expected {len(dev_rows)}.")

    bm25_index = load_bm25_index(index_path)
    dense_retriever, dense_error = (None, "Text2Trade disabled by --skip-dense") if args.skip_dense else _load_dense_retriever(
        dense_artifact_dir, dense_model_path
    )
    dense_available = dense_retriever is not None
    available_methods = ["BM25_Q0_baseline", "BM25_multiquery_RRF"]
    if dense_available:
        available_methods.extend(
            [
                "Text2Trade_Q0_baseline",
                "Text2Trade_multiquery_RRF",
                "Hybrid_BM25_Text2Trade_multiquery_RRF",
            ]
        )

    start = time.time()
    case_rows: list[dict[str, Any]] = []
    candidate_rows: list[dict[str, Any]] = []

    for position, (dev_row, mq_row) in enumerate(zip(dev_rows, multiquery_rows), start=1):
        descripcion = _clean(dev_row.get("descripcion"))
        nandina_ref = _clean(dev_row.get("nandina"))
        case_id = _clean(mq_row.get("case_id")) or f"dev-{position:02d}"
        queries = {
            "Q0": descripcion,
            "Q1": _clean(mq_row.get("q1_limpia")),
            "Q2": _clean(mq_row.get("q2_expandida")),
            "Q3": _clean(mq_row.get("q3_terminos_clave")),
        }

        bm25_sources: dict[str, list[dict[str, Any]]] = {}
        dense_sources: dict[str, list[dict[str, Any]]] = {}
        for label in QUERY_LABELS:
            query_text = queries[label]
            bm25_sources[f"BM25_{label}"] = bm25_retrieve(bm25_index, query_text, top_n=retrieval_depth) if query_text else []
            if dense_available:
                dense_sources[f"Dense_{label}"] = dense_retriever.retrieve(query_text, top_k=retrieval_depth) if query_text else []

        method_candidates: dict[str, list[dict[str, Any]]] = {
            "BM25_Q0_baseline": [_normalize_hit(hit, "BM25_Q0") for hit in bm25_sources["BM25_Q0"]],
            "BM25_multiquery_RRF": _rrf_fuse(bm25_sources, rrf_k=args.rrf_k),
        }
        if dense_available:
            method_candidates["Text2Trade_Q0_baseline"] = [_normalize_hit(hit, "Dense_Q0") for hit in dense_sources["Dense_Q0"]]
            method_candidates["Text2Trade_multiquery_RRF"] = _rrf_fuse(dense_sources, rrf_k=args.rrf_k)
            hybrid_sources: dict[str, Sequence[Mapping[str, Any]]] = {}
            hybrid_sources.update(bm25_sources)
            hybrid_sources.update(dense_sources)
            method_candidates["Hybrid_BM25_Text2Trade_multiquery_RRF"] = _rrf_fuse(hybrid_sources, rrf_k=args.rrf_k)

        case: dict[str, Any] = {
            "case_id": case_id,
            "nandina_ref": nandina_ref,
            "descripcion_original": descripcion,
            "Q0": queries["Q0"],
            "Q1": queries["Q1"],
            "Q2": queries["Q2"],
            "Q3": queries["Q3"],
            "multiquery_json_valid": int(mq_row.get("json_valid", 0)),
            "multiquery_code_violation": int(mq_row.get("code_violation", 0)),
            "multiquery_forbidden_term_violation": int(mq_row.get("forbidden_term_violation", 0)),
            "multiquery_warnings": "; ".join(str(item) for item in mq_row.get("warnings", [])),
        }
        for method in available_methods:
            candidates = method_candidates[method]
            rank = rank_of_true(candidates, nandina_ref) if method.endswith("baseline") else _rank_from_candidates(candidates, nandina_ref)
            case[f"rank_{method}"] = rank
            case[f"top_{max_k}_{method}"] = _format_top(candidates, max_k)
            case[f"top_{max_k}_{method}_json"] = json.dumps(_compact_top(candidates, max_k), ensure_ascii=False)

        for method in METHOD_ORDER:
            case.setdefault(f"rank_{method}", "")
            case.setdefault(f"top_{max_k}_{method}", "")
            case.setdefault(f"top_{max_k}_{method}_json", "[]")

        case_rows.append(case)

        for method in available_methods:
            for hit in method_candidates[method][:max_k]:
                candidate_rows.append(
                    {
                        "case_id": case_id,
                        "method": method,
                        "candidate_rank": int(hit.get("rank", 0)),
                        "candidate_code": _clean(hit.get("code")),
                        "candidate_score": float(hit.get("rrf_score", hit.get("score", 0.0))),
                        "candidate_sources": "; ".join(str(item) for item in hit.get("sources", [])),
                        "candidate_text": _clean(hit.get("text")),
                        "is_expected_nandina": int(_clean(hit.get("code")) == nandina_ref),
                    }
                )

    method_metrics = {
        method: _metrics_for_method(case_rows, method, k_list=k_list, max_k=max_k) for method in available_methods
    }
    comparison = {
        method: _comparison_vs_baseline(case_rows, method)
        for method in available_methods
        if method != "BM25_Q0_baseline"
    }
    best_method = max(available_methods, key=lambda method: (method_metrics[method]["mrr"], method_metrics[method]["top_10_accuracy"]))
    final_rrf_method = (
        "Hybrid_BM25_Text2Trade_multiquery_RRF" if dense_available else "BM25_multiquery_RRF"
    )

    for case in case_rows:
        case["best_method_available"] = final_rrf_method
        case["rank_best_method_available"] = case[f"rank_{final_rrf_method}"]
        case["resultado_frente_bm25_q0"] = _case_outcome(
            int(case["rank_BM25_Q0_baseline"]), int(case[f"rank_{final_rrf_method}"])
        )
        case["top_10_candidatos_finales_mejor_metodo"] = case[f"top_{max_k}_{final_rrf_method}"]
        case["fuentes_top_10_mejor_metodo_json"] = case[f"top_{max_k}_{final_rrf_method}_json"]

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_multiquery_rrf_devset",
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
        "rrf": {
            "rrf_k": args.rrf_k,
            "retrieval_depth_per_query": retrieval_depth,
            "queries_per_case": list(QUERY_LABELS),
        },
        "bm25": {
            "k1": getattr(bm25_index, "k1", None),
            "b": getattr(bm25_index, "b", None),
            "docs_indexed": len(bm25_index.doc_ids),
            "avgdl": getattr(bm25_index, "avgdl", None),
            "vocab_size": len(getattr(bm25_index, "idf", {})),
        },
        "dense": {
            "available": dense_available,
            "error": dense_error,
            "artifact_dir": _report_path(dense_artifact_dir, root),
            "model_path": _report_path(dense_model_path, root),
        },
        "available_methods": available_methods,
        "best_method_by_mrr": best_method,
        "final_rrf_method_available": final_rrf_method,
        "methods": method_metrics,
        "comparison_vs_bm25_q0": comparison,
        "quality": {
            "cases_total": len(case_rows),
            "multiquery_json_valid_cases": sum(int(row["multiquery_json_valid"]) for row in case_rows),
            "multiquery_code_violation_cases": sum(int(row["multiquery_code_violation"]) for row in case_rows),
            "multiquery_forbidden_term_cases": sum(int(row["multiquery_forbidden_term_violation"]) for row in case_rows),
        },
        "warnings": [
            "Devset-only diagnostic; do not infer final evalset performance.",
            "Q0 is copied from devset and is not generated by the LLM.",
        ],
        "output": {
            "output_dir": _report_path(output_dir, root),
            "output_abs_dir": str(output_dir),
            "rrf_results_csv": _report_path(output_dir / "rrf_results.csv", root),
            "rrf_metrics_json": _report_path(output_dir / "rrf_metrics.json", root),
            "rrf_summary_md": _report_path(output_dir / "rrf_summary.md", root),
            "rrf_case_comparison_13_cases_csv": _report_path(output_dir / "rrf_case_comparison_13_cases.csv", root),
        },
    }
    if not dense_available:
        metrics["warnings"].append(f"Text2Trade was not available: {dense_error}")

    case_fieldnames = [
        "case_id",
        "nandina_ref",
        "descripcion_original",
        "Q0",
        "Q1",
        "Q2",
        "Q3",
        "rank_BM25_Q0_baseline",
        "rank_BM25_multiquery_RRF",
        "rank_Text2Trade_Q0_baseline",
        "rank_Text2Trade_multiquery_RRF",
        "rank_Hybrid_BM25_Text2Trade_multiquery_RRF",
        "best_method_available",
        "rank_best_method_available",
        "resultado_frente_bm25_q0",
        "top_10_candidatos_finales_mejor_metodo",
        "fuentes_top_10_mejor_metodo_json",
        "multiquery_json_valid",
        "multiquery_code_violation",
        "multiquery_forbidden_term_violation",
        "multiquery_warnings",
    ]
    _write_csv(output_dir / "rrf_case_comparison_13_cases.csv", case_rows, case_fieldnames)
    _write_csv(
        output_dir / "rrf_results.csv",
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
    _write_json(output_dir / "rrf_metrics.json", metrics)
    ensure_parent(output_dir / "rrf_summary.md")
    (output_dir / "rrf_summary.md").write_text(_summary_markdown(metrics, available_methods), encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate BM25/Text2Trade multi-query RRF on the 13-case devset.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--multiqueries", type=Path, default=DEFAULT_MULTIQUERIES)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--index", type=Path, default=None)
    parser.add_argument("--dense-artifact-dir", type=Path, default=DEFAULT_DENSE_ARTIFACT_DIR)
    parser.add_argument("--dense-model-path", type=Path, default=None)
    parser.add_argument("--skip-dense", action="store_true")
    parser.add_argument("--k-list", default=None)
    parser.add_argument("--retrieval-depth", type=int, default=None)
    parser.add_argument("--rrf-k", type=int, default=60)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion multi-query RRF devset completada")
    print(f"Casos evaluados: {metrics['quality']['cases_total']}")
    print(f"Text2Trade disponible: {metrics['dense']['available']}")
    print(f"Mejor metodo por MRR: {metrics['best_method_by_mrr']}")
    print(f"Metodo RRF final disponible: {metrics['final_rrf_method_available']}")
    for method in metrics["available_methods"]:
        data = metrics["methods"][method]
        print(
            f"{method}: Top-1={data['top_1_accuracy']:.4f} Top-3={data['top_3_accuracy']:.4f} "
            f"Top-5={data['top_5_accuracy']:.4f} Top-10={data['top_10_accuracy']:.4f} MRR={data['mrr']:.4f}"
        )
    print(f"Outputs: {metrics['output']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
