from __future__ import annotations

import argparse
import csv
import json
import platform
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_LEVEL_INDEX_DIR = Path("data/processed/indexes/bm25_levels")
DEFAULT_PHASE7A_DEVSET_METRICS = Path("outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool_metrics.json")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/hierarchical_bm25_devset_v0.1")

K_VALUES = [10, 20, 50, 100]
HS2_TOP_M = [3, 5]
HS4_TOP_M = [5, 10, 20]
HS6_TOP_M = [10, 20, 50]
FINAL_TOP_N = [10, 50, 100]
EXPECTED_DEVSET_ROWS = 13


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


def _top_codes(hits: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_clean(hit.get("code")) for hit in hits[:limit])


def _renumber(hits: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for rank, hit in enumerate(hits[:depth], start=1):
        item = dict(hit)
        item["rank"] = rank
        output.append(item)
    return output


def _codes(hits: Sequence[Mapping[str, Any]], limit: int) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for hit in hits[:limit]:
        code = _clean(hit.get("code"))
        if code and code not in seen:
            seen.add(code)
            output.append(code)
    return output


def _filter_nandina(full_hits: Sequence[Mapping[str, Any]], prefixes: Iterable[str], depth: int) -> list[dict[str, Any]]:
    clean_prefixes = tuple(sorted({_clean(prefix) for prefix in prefixes if _clean(prefix)}))
    if not clean_prefixes:
        return []
    return _renumber(
        [dict(hit) for hit in full_hits if _clean(hit.get("code")).startswith(clean_prefixes)],
        depth,
    )


def _strategy_configs() -> list[dict[str, Any]]:
    configs: list[dict[str, Any]] = []
    for final_top in FINAL_TOP_N:
        configs.append(
            {
                "strategy": "direct_nandina8",
                "hs2_top_m": 0,
                "hs4_top_m": 0,
                "hs6_top_m": 0,
                "final_top_n": final_top,
            }
        )
    for hs4_top in HS4_TOP_M:
        for final_top in FINAL_TOP_N:
            configs.append(
                {
                    "strategy": "hs4_then_nandina8",
                    "hs2_top_m": 0,
                    "hs4_top_m": hs4_top,
                    "hs6_top_m": 0,
                    "final_top_n": final_top,
                }
            )
    for hs6_top in HS6_TOP_M:
        for final_top in FINAL_TOP_N:
            configs.append(
                {
                    "strategy": "hs6_then_nandina8",
                    "hs2_top_m": 0,
                    "hs4_top_m": 0,
                    "hs6_top_m": hs6_top,
                    "final_top_n": final_top,
                }
            )
    for hs4_top in HS4_TOP_M:
        for hs6_top in HS6_TOP_M:
            for final_top in FINAL_TOP_N:
                configs.append(
                    {
                        "strategy": "hs4_hs6_union_then_nandina8",
                        "hs2_top_m": 0,
                        "hs4_top_m": hs4_top,
                        "hs6_top_m": hs6_top,
                        "final_top_n": final_top,
                    }
                )
    for hs2_top in HS2_TOP_M:
        for hs4_top in HS4_TOP_M:
            for hs6_top in HS6_TOP_M:
                for final_top in FINAL_TOP_N:
                    configs.append(
                        {
                            "strategy": "hs2_hs4_hs6_union_then_nandina8",
                            "hs2_top_m": hs2_top,
                            "hs4_top_m": hs4_top,
                            "hs6_top_m": hs6_top,
                            "final_top_n": final_top,
                        }
                    )
    return configs


def _hits_for_config(cache: Mapping[str, Any], config: Mapping[str, Any]) -> list[dict[str, Any]]:
    final_top = int(config["final_top_n"])
    strategy = _clean(config["strategy"])
    if strategy == "direct_nandina8":
        return _renumber(cache["nandina8_full"], final_top)

    prefixes: set[str] = set()
    if strategy in {"hs4_then_nandina8", "hs4_hs6_union_then_nandina8", "hs2_hs4_hs6_union_then_nandina8"}:
        prefixes.update(_codes(cache["hs4"], int(config["hs4_top_m"])))
    if strategy in {"hs6_then_nandina8", "hs4_hs6_union_then_nandina8", "hs2_hs4_hs6_union_then_nandina8"}:
        prefixes.update(_codes(cache["hs6"], int(config["hs6_top_m"])))
    if strategy == "hs2_hs4_hs6_union_then_nandina8":
        prefixes.update(_codes(cache["hs2"], int(config["hs2_top_m"])))
    return _filter_nandina(cache["nandina8_full"], prefixes, final_top)


def _case_id(row: Mapping[str, Any], position: int) -> str:
    return _clean(row.get("case_id")) or f"devset-{position:02d}"


def _metrics(case_rows: Sequence[Mapping[str, Any]], config: Mapping[str, Any]) -> dict[str, Any]:
    ranks = [int(row["rank"]) for row in case_rows]
    retrieved_counts = [int(row["retrieved_count"]) for row in case_rows]
    metrics: dict[str, Any] = {
        "strategy": config["strategy"],
        "hs2_top_m": config["hs2_top_m"],
        "hs4_top_m": config["hs4_top_m"],
        "hs6_top_m": config["hs6_top_m"],
        "final_top_n": config["final_top_n"],
        "cases_total": len(case_rows),
        "cases_with_results": sum(1 for count in retrieved_counts if count > 0),
        "average_retrieved": _mean([float(count) for count in retrieved_counts]),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "not_found": sum(1 for rank in ranks if rank <= 0),
        "top_10_hs2": _mean([float(row["hs2_hit_at_10"]) for row in case_rows]),
        "top_10_hs4": _mean([float(row["hs4_hit_at_10"]) for row in case_rows]),
        "top_10_hs6": _mean([float(row["hs6_hit_at_10"]) for row in case_rows]),
    }
    for k in K_VALUES:
        metrics[f"recall_at_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
        metrics[f"hs2_at_{k}"] = _mean([float(row[f"hs2_hit_at_{k}"]) for row in case_rows])
        metrics[f"hs4_at_{k}"] = _mean([float(row[f"hs4_hit_at_{k}"]) for row in case_rows])
        metrics[f"hs6_at_{k}"] = _mean([float(row[f"hs6_hit_at_{k}"]) for row in case_rows])
    return metrics


def _rank_prefix(hits: Sequence[Mapping[str, Any]], expected_code: str, prefix_len: int) -> int:
    prefix = expected_code[:prefix_len]
    for rank, hit in enumerate(hits, start=1):
        if _clean(hit.get("code")).startswith(prefix):
            return rank
    return 0


def _case_metrics(
    case_id: str,
    description: str,
    expected_code: str,
    config: Mapping[str, Any],
    hits: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    rank = rank_of_true(hits, expected_code)
    row: dict[str, Any] = {
        "case_id": case_id,
        "descripcion": description,
        "nandina_ref": expected_code,
        "hs2_ref": expected_code[:2],
        "hs4_ref": expected_code[:4],
        "hs6_ref": expected_code[:6],
        "strategy": config["strategy"],
        "hs2_top_m": config["hs2_top_m"],
        "hs4_top_m": config["hs4_top_m"],
        "hs6_top_m": config["hs6_top_m"],
        "final_top_n": config["final_top_n"],
        "rank": rank,
        "retrieved_count": len(hits),
        "top_10_codes": _top_codes(hits, 10),
    }
    for k in K_VALUES:
        row[f"hit_at_{k}"] = int(acc_at_k(rank, k))
        row[f"hs2_hit_at_{k}"] = int(_rank_prefix(hits[:k], expected_code, 2) > 0)
        row[f"hs4_hit_at_{k}"] = int(_rank_prefix(hits[:k], expected_code, 4) > 0)
        row[f"hs6_hit_at_{k}"] = int(_rank_prefix(hits[:k], expected_code, 6) > 0)
    return row


def _load_phase7a(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"available": False}
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    strategy = "hierarchical_80_dual_backfill_20"
    metrics = payload.get("metrics_by_strategy", {}).get(strategy, {})
    return {
        "available": bool(metrics),
        "path": str(path),
        "strategy": strategy,
        "final_pool_at_100": metrics.get("final_pool_at_100"),
        "final_pool_hs4_at_100": metrics.get("final_pool_hs4_at_100"),
        "final_pool_hs2_at_100": metrics.get("final_pool_hs2_at_100"),
    }


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    best = payload["selected_candidate"]
    direct = payload["baselines"]["direct_nandina8_top100"]
    phase7a = payload["baselines"]["phase7a_pool_hierarchical_80_dual_backfill_20"]
    lines = [
        "# Evaluacion jerarquica BM25 devset v0.1",
        "",
        "## Alcance",
        "",
        "Fase 8A prueba recuperacion jerarquica HS2/HS4/HS6 hacia NANDINA8 usando solo devset para seleccionar estrategia. No se ejecuto LLM, Ollama, OpenAI, Text2Trade ni APIs remotas.",
        "",
        "## Estrategia candidata",
        "",
        f"- Estrategia: `{best['strategy']}`.",
        f"- HS2 Top-M: {best['hs2_top_m']}.",
        f"- HS4 Top-M: {best['hs4_top_m']}.",
        f"- HS6 Top-M: {best['hs6_top_m']}.",
        f"- NANDINA8 final Top-N: {best['final_top_n']}.",
        f"- Recall@100 devset: {best['recall_at_100']:.4f}.",
        f"- Top-10 exacto devset: {best['recall_at_10']:.4f}.",
        f"- MRR devset: {best['mrr']:.4f}.",
        "",
        "## Comparacion devset",
        "",
        "| Metodo | Top-10 | Recall@50 | Recall@100 | HS4@100 | HS2@100 | MRR |",
        "|---|---:|---:|---:|---:|---:|---:|",
        f"| direct_nandina8 Top-100 | {direct['recall_at_10']:.4f} | {direct['recall_at_50']:.4f} | {direct['recall_at_100']:.4f} | {direct['hs4_at_100']:.4f} | {direct['hs2_at_100']:.4f} | {direct['mrr']:.4f} |",
        f"| candidato Fase 8A | {best['recall_at_10']:.4f} | {best['recall_at_50']:.4f} | {best['recall_at_100']:.4f} | {best['hs4_at_100']:.4f} | {best['hs2_at_100']:.4f} | {best['mrr']:.4f} |",
    ]
    if phase7a.get("available"):
        lines.append(
            f"| phase7a_pool_hierarchical_80_dual_backfill_20 | NA | NA | {phase7a['final_pool_at_100']:.4f} | {phase7a['final_pool_hs4_at_100']:.4f} | {phase7a['final_pool_hs2_at_100']:.4f} | NA |"
        )
    lines.extend(
        [
            "",
            "## Decision",
            "",
            payload["recommendation"],
            "",
            "El evalset no se uso para seleccionar estrategia; queda reservado para una posible Fase 8B si se decide validar el candidato congelado.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    devset_path = resolve_project_path(args.devset)
    level_index_dir = resolve_project_path(args.level_index_dir)
    output_dir = resolve_project_path(args.output_dir)
    phase7a_path = resolve_project_path(args.phase7a_devset_metrics)
    start = time.time()

    dev_rows = _read_csv(devset_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")

    indexes = {
        "hs2": load_bm25_index(level_index_dir / "hs2_v0.1.pkl"),
        "hs4": load_bm25_index(level_index_dir / "hs4_v0.1.pkl"),
        "hs6": load_bm25_index(level_index_dir / "hs6_v0.1.pkl"),
        "nandina8": load_bm25_index(level_index_dir / "nandina8_v0.1.pkl"),
    }
    configs = _strategy_configs()
    max_docs_nandina8 = len(indexes["nandina8"].doc_ids)

    query_caches: list[dict[str, Any]] = []
    for position, row in enumerate(dev_rows, start=1):
        description = _clean(row.get("descripcion"))
        query_caches.append(
            {
                "case_id": _case_id(row, position),
                "descripcion": description,
                "expected_code": _clean(row.get("nandina") or row.get("nandina_ref")),
                "hs2": retrieve(indexes["hs2"], description, top_n=max(HS2_TOP_M)),
                "hs4": retrieve(indexes["hs4"], description, top_n=max(HS4_TOP_M)),
                "hs6": retrieve(indexes["hs6"], description, top_n=max(HS6_TOP_M)),
                "nandina8_full": retrieve(indexes["nandina8"], description, top_n=max_docs_nandina8),
            }
        )

    all_case_rows: list[dict[str, Any]] = []
    result_rows: list[dict[str, Any]] = []
    grouped_case_rows: dict[tuple[str, int, int, int, int], list[dict[str, Any]]] = {}
    for config in configs:
        key = (
            _clean(config["strategy"]),
            int(config["hs2_top_m"]),
            int(config["hs4_top_m"]),
            int(config["hs6_top_m"]),
            int(config["final_top_n"]),
        )
        case_rows: list[dict[str, Any]] = []
        for cache in query_caches:
            hits = _hits_for_config(cache, config)
            case_row = _case_metrics(
                cache["case_id"],
                cache["descripcion"],
                cache["expected_code"],
                config,
                hits,
            )
            case_rows.append(case_row)
            all_case_rows.append(case_row)
        grouped_case_rows[key] = case_rows
        result_rows.append(_metrics(case_rows, config))

    result_rows.sort(
        key=lambda row: (
            -float(row["recall_at_100"]),
            -float(row["recall_at_50"]),
            -float(row["recall_at_10"]),
            -float(row["mrr"]),
            int(row["final_top_n"]),
            _clean(row["strategy"]),
        )
    )
    selected = result_rows[0]
    direct_top100 = next(
        row
        for row in result_rows
        if row["strategy"] == "direct_nandina8" and int(row["final_top_n"]) == 100
    )
    selected_key = (
        _clean(selected["strategy"]),
        int(selected["hs2_top_m"]),
        int(selected["hs4_top_m"]),
        int(selected["hs6_top_m"]),
        int(selected["final_top_n"]),
    )
    selected_case_rows = grouped_case_rows[selected_key]

    phase7a = _load_phase7a(phase7a_path)
    if phase7a.get("available"):
        phase7a["path"] = _rel(phase7a_path, root)
    improves_direct = float(selected["recall_at_100"]) > float(direct_top100["recall_at_100"])
    phase7a_value = phase7a.get("final_pool_at_100")
    improves_phase7a = phase7a.get("available") and phase7a_value is not None and float(selected["recall_at_100"]) > float(phase7a_value)
    if improves_direct:
        recommendation = (
            "Se recomienda una Fase 8B controlada sobre evalset con la estrategia candidata congelada, "
            "porque en devset mejora Recall@100 frente a NANDINA8 directo."
        )
    else:
        recommendation = (
            "No se recomienda pasar todavia a Fase 8B como sustituto: en devset no mejora Recall@100 "
            "frente a NANDINA8 directo. Puede conservarse como diagnostico de techo/familias."
        )

    metrics_payload: dict[str, Any] = {
        "script": "src.experiments.evaluate_hierarchical_bm25_devset",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": time.time() - start,
        "environment": {
            "python_version": platform.python_version(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "inputs": {
            "devset_path": _rel(devset_path, root),
            "devset_sha256": sha256_file(devset_path),
            "level_index_dir": _rel(level_index_dir, root),
            "phase7a_devset_metrics": _rel(phase7a_path, root) if phase7a_path.exists() else "",
        },
        "parameters": {
            "k_values": K_VALUES,
            "hs2_top_m": HS2_TOP_M,
            "hs4_top_m": HS4_TOP_M,
            "hs6_top_m": HS6_TOP_M,
            "final_top_n": FINAL_TOP_N,
            "strategy_count": len(configs),
        },
        "selected_candidate": selected,
        "baselines": {
            "direct_nandina8_top100": direct_top100,
            "phase7a_pool_hierarchical_80_dual_backfill_20": phase7a,
        },
        "comparisons": {
            "candidate_improves_recall100_vs_direct_nandina8": bool(improves_direct),
            "candidate_improves_recall100_vs_phase7a_pool": bool(improves_phase7a),
        },
        "results": result_rows,
        "strategy_counts": dict(Counter(row["strategy"] for row in result_rows)),
        "recommendation": recommendation,
        "policy": {
            "dataset_used_for_selection": "devset",
            "evalset_used_for_selection": False,
            "llm_used": False,
            "ollama_used": False,
            "openai_used": False,
            "text2trade_used": False,
            "remote_apis_used": False,
        },
        "outputs": {
            "results_csv": _rel(output_dir / "hierarchical_devset_results.csv", root),
            "metrics_json": _rel(output_dir / "hierarchical_devset_metrics.json", root),
            "summary_md": _rel(output_dir / "hierarchical_devset_summary.md", root),
            "case_comparison_csv": _rel(output_dir / "hierarchical_devset_case_comparison.csv", root),
        },
    }

    result_fieldnames = [
        "strategy",
        "hs2_top_m",
        "hs4_top_m",
        "hs6_top_m",
        "final_top_n",
        "cases_total",
        "cases_with_results",
        "average_retrieved",
        "mrr",
        "not_found",
        "recall_at_10",
        "recall_at_20",
        "recall_at_50",
        "recall_at_100",
        "hs2_at_10",
        "hs2_at_20",
        "hs2_at_50",
        "hs2_at_100",
        "hs4_at_10",
        "hs4_at_20",
        "hs4_at_50",
        "hs4_at_100",
        "hs6_at_10",
        "hs6_at_20",
        "hs6_at_50",
        "hs6_at_100",
        "top_10_hs2",
        "top_10_hs4",
        "top_10_hs6",
    ]
    case_fieldnames = [
        "case_id",
        "descripcion",
        "nandina_ref",
        "hs2_ref",
        "hs4_ref",
        "hs6_ref",
        "strategy",
        "hs2_top_m",
        "hs4_top_m",
        "hs6_top_m",
        "final_top_n",
        "rank",
        "retrieved_count",
        "hit_at_10",
        "hit_at_20",
        "hit_at_50",
        "hit_at_100",
        "hs2_hit_at_10",
        "hs2_hit_at_20",
        "hs2_hit_at_50",
        "hs2_hit_at_100",
        "hs4_hit_at_10",
        "hs4_hit_at_20",
        "hs4_hit_at_50",
        "hs4_hit_at_100",
        "hs6_hit_at_10",
        "hs6_hit_at_20",
        "hs6_hit_at_50",
        "hs6_hit_at_100",
        "top_10_codes",
    ]
    _write_csv(output_dir / "hierarchical_devset_results.csv", result_rows, result_fieldnames)
    _write_csv(output_dir / "hierarchical_devset_case_comparison.csv", selected_case_rows, case_fieldnames)
    _write_json(output_dir / "hierarchical_devset_metrics.json", metrics_payload)
    ensure_parent(output_dir / "hierarchical_devset_summary.md")
    (output_dir / "hierarchical_devset_summary.md").write_text(_summary_markdown(metrics_payload), encoding="utf-8")
    return metrics_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate hierarchical HS2/HS4/HS6 -> NANDINA8 BM25 on devset.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--level-index-dir", type=Path, default=DEFAULT_LEVEL_INDEX_DIR)
    parser.add_argument("--phase7a-devset-metrics", type=Path, default=DEFAULT_PHASE7A_DEVSET_METRICS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    best = metrics["selected_candidate"]
    print("OK: evaluacion jerarquica BM25 devset completada")
    print(
        "Candidato: "
        f"{best['strategy']} hs2={best['hs2_top_m']} hs4={best['hs4_top_m']} "
        f"hs6={best['hs6_top_m']} final={best['final_top_n']}"
    )
    print(f"Recall@100: {best['recall_at_100']:.4f}")
    print(f"Top-10: {best['recall_at_10']:.4f}")
    print(f"MRR: {best['mrr']:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
