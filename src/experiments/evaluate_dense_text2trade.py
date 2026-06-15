from __future__ import annotations

import argparse
import csv
import json
import platform
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.dense_text2trade import DenseText2TradeRetriever
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_ARTIFACT_DIR = Path("data/processed/indexes/text2trade_nandina8_v1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/text2trade_dense_eval_v0.1")
DEFAULT_K_LIST = [1, 3, 5, 10]
RESULT_BASE_COLUMNS = [
    "case_id",
    "descripcion",
    "nandina_ref",
    "regimen",
    "capitulo_ref",
    "partida_ref",
    "rank_ref",
    "retrieved_count",
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


def _report_path(path: Path, root: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return str(resolved)


def _parse_k_list(raw: str | None, fallback: Iterable[int]) -> list[int]:
    if not raw:
        values = list(fallback)
    else:
        values = [int(part.strip()) for part in raw.split(",") if part.strip()]
    values = sorted(set(values))
    if not values or any(value <= 0 for value in values):
        raise ValueError("k-list must contain positive integers")
    return values


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _rate(numerator: int, denominator: int) -> float:
    return float(numerator / denominator) if denominator else 0.0


def _chapter(row: Mapping[str, str], nandina_ref: str) -> str:
    value = _clean(row.get("capitulo"))
    return value.zfill(2) if value else nandina_ref[:2]


def _heading(row: Mapping[str, str], nandina_ref: str) -> str:
    value = _clean(row.get("partida"))
    return value.zfill(4) if value else nandina_ref[:4]


def _hit_column(k: int) -> str:
    return f"hit_top_{k}"


def _candidate_columns(max_candidates: int) -> list[str]:
    columns: list[str] = []
    for rank in range(1, max_candidates + 1):
        columns.extend(
            [
                f"candidate_{rank}_code",
                f"candidate_{rank}_score",
                f"candidate_{rank}_doc_id",
                f"candidate_{rank}_text",
            ]
        )
    return columns


def _add_candidates(row: dict[str, Any], hits: Sequence[Mapping[str, Any]], max_candidates: int) -> None:
    for rank in range(1, max_candidates + 1):
        hit = hits[rank - 1] if rank <= len(hits) else None
        row[f"candidate_{rank}_code"] = _clean(hit.get("code")) if hit else ""
        row[f"candidate_{rank}_score"] = hit.get("score", "") if hit else ""
        row[f"candidate_{rank}_doc_id"] = _clean(hit.get("doc_id")) if hit else ""
        row[f"candidate_{rank}_text"] = _clean(hit.get("text")) if hit else ""


def _rank_distribution(ranks: Sequence[int], max_k: int) -> dict[str, int]:
    counter = Counter(ranks)
    payload = {str(rank): counter.get(rank, 0) for rank in range(1, max_k + 1)}
    payload[f">{max_k}"] = sum(count for rank, count in counter.items() if rank > max_k)
    payload["not_found"] = counter.get(0, 0)
    return payload


def _topk_family_hit(row: Mapping[str, Any], family_len: int, k: int) -> int:
    ref = _clean(row.get("nandina_ref"))[:family_len]
    if not ref:
        return 0
    for rank in range(1, k + 1):
        if _clean(row.get(f"candidate_{rank}_code"))[:family_len] == ref:
            return 1
    return 0


def _family_metrics(rows: Sequence[Mapping[str, Any]], k_list: Sequence[int], family_len: int) -> dict[str, float]:
    return {f"top_{k}_hs{family_len}_accuracy": _mean([_topk_family_hit(row, family_len, k) for row in rows]) for k in k_list}


def _group_metrics(
    rows: Sequence[Mapping[str, Any]],
    group_field: str,
    k_list: Sequence[int],
    max_k: int,
    min_group_size: int,
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        group_value = _clean(row.get(group_field))
        if group_value:
            grouped[group_value].append(row)

    metrics: dict[str, dict[str, Any]] = {}
    excluded_small = 0
    excluded_cases = 0
    for group_value, group_rows in sorted(grouped.items()):
        if len(group_rows) < min_group_size:
            excluded_small += 1
            excluded_cases += len(group_rows)
            continue
        ranks = [int(row["rank_ref"]) for row in group_rows]
        retrieved = sum(1 for row in group_rows if int(row["retrieved_count"]) > 0)
        payload: dict[str, Any] = {
            "cases": len(group_rows),
            "retrieved_cases": retrieved,
            "retrieved_rate": _rate(retrieved, len(group_rows)),
            "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
            f"no_match_top_{max_k}": sum(1 for rank in ranks if rank <= 0 or rank > max_k),
        }
        for k in k_list:
            payload[f"top_{k}_accuracy"] = _mean([acc_at_k(rank, k) for rank in ranks])
        payload.update(_family_metrics(group_rows, [max_k], 4))
        payload.update(_family_metrics(group_rows, [max_k], 2))
        metrics[group_value] = payload

    audit = {
        "field": group_field,
        "min_group_size": min_group_size,
        "groups_total": len(grouped),
        "groups_reported": len(metrics),
        "groups_excluded_small_n": excluded_small,
        "cases_excluded_small_groups": excluded_cases,
    }
    return metrics, audit


def _summary_markdown(metrics: Mapping[str, Any], k_list: Sequence[int], max_k: int) -> str:
    global_metrics = metrics["global_metrics"]
    lines = [
        "# Evaluacion dense Text2Trade v0.1",
        "",
        "## Alcance",
        "",
        "Se evaluo recuperacion densa Text2Trade por fuerza bruta sobre el evalset final v0.1. No se uso HNSW ni LLM.",
        "",
        "## Configuracion",
        "",
        f"- Evalset: `{metrics['input']['evalset_path']}`.",
        f"- Artefacto denso: `{metrics['input']['artifact_dir']}`.",
        f"- Modelo local: `{metrics['dense_config']['model_path']}`.",
        f"- Modo de recuperacion: {metrics['dense_config']['retrieval_mode']}.",
        f"- Profundidad de recuperacion para rank/MRR: {metrics['dense_config']['retrieval_depth']}.",
        f"- Cortes evaluados: {', '.join(str(k) for k in k_list)}.",
        "",
        "## Resultados globales",
        "",
        f"- Casos evaluados: {global_metrics['cases_total']}.",
        f"- Casos con al menos un resultado recuperado: {global_metrics['cases_with_retrieval']}.",
    ]
    for k in k_list:
        lines.append(f"- Top-{k} accuracy NANDINA8 exacta: {global_metrics[f'top_{k}_accuracy']:.4f}.")
    lines.extend(
        [
            f"- MRR: {global_metrics['mrr']:.4f}.",
            f"- Top-{max_k} HS4: {global_metrics[f'top_{max_k}_hs4_accuracy']:.4f}.",
            f"- Top-{max_k} HS2: {global_metrics[f'top_{max_k}_hs2_accuracy']:.4f}.",
            f"- Casos sin match exacto en Top-{max_k}: {global_metrics[f'no_match_top_{max_k}']}.",
            "",
            "## Limitaciones",
            "",
            "- Evaluacion por fuerza bruta sobre vectores congelados; no reproduce el backend HNSW declarado.",
            "- `hnsw.index` esta ausente fisicamente.",
            "- La evaluacion depende de la carga local del modelo Text2Trade guardado.",
            "- El evalset tiene 1 caso con regimen 12; se reporta como alerta sin modificar el dataset.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    evalset_path = resolve_project_path(args.evalset)
    artifact_dir = resolve_project_path(args.artifact_dir)
    output_dir = resolve_project_path(args.output_dir)
    model_path = resolve_project_path(args.model_path) if args.model_path else artifact_dir / "model"

    k_list = _parse_k_list(args.k_list, DEFAULT_K_LIST)
    max_k = max(k_list)
    retrieval_depth = max(args.retrieval_depth or max_k, max_k)

    eval_rows = _read_csv(evalset_path)
    retriever = DenseText2TradeRetriever(artifact_dir, model_path=model_path)

    result_rows: list[dict[str, Any]] = []
    start = time.time()
    for position, row in enumerate(eval_rows, start=1):
        nandina_ref = _clean(row.get("nandina_ref"))
        descripcion = _clean(row.get("descripcion"))
        hits = retriever.retrieve(descripcion, top_k=retrieval_depth)
        rank_ref = rank_of_true(hits, nandina_ref)
        result: dict[str, Any] = {
            "case_id": _clean(row.get("case_id")) or f"case-{position:04d}",
            "descripcion": descripcion,
            "nandina_ref": nandina_ref,
            "regimen": _clean(row.get("regimen")),
            "capitulo_ref": _chapter(row, nandina_ref),
            "partida_ref": _heading(row, nandina_ref),
            "rank_ref": rank_ref,
            "retrieved_count": len(hits),
        }
        for k in k_list:
            result[_hit_column(k)] = int(acc_at_k(rank_ref, k))
        for required_k in DEFAULT_K_LIST:
            result.setdefault(_hit_column(required_k), int(acc_at_k(rank_ref, required_k)))
        _add_candidates(result, hits, max_k)
        result_rows.append(result)

    ranks = [int(row["rank_ref"]) for row in result_rows]
    retrieved_cases = sum(1 for row in result_rows if int(row["retrieved_count"]) > 0)
    regimen_counts = Counter(_clean(row.get("regimen")) for row in result_rows)
    global_metrics: dict[str, Any] = {
        "cases_total": len(result_rows),
        "cases_with_retrieval": retrieved_cases,
        "retrieval_rate": _rate(retrieved_cases, len(result_rows)),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "rank_distribution": _rank_distribution(ranks, max_k=max_k),
        f"no_match_top_{max_k}": sum(1 for rank in ranks if rank <= 0 or rank > max_k),
        "cases_with_zero_results": sum(1 for row in result_rows if int(row["retrieved_count"]) == 0),
        "regimen_counts": dict(sorted(regimen_counts.items())),
    }
    for k in k_list:
        global_metrics[f"top_{k}_accuracy"] = _mean([acc_at_k(rank, k) for rank in ranks])
    global_metrics.update(_family_metrics(result_rows, k_list, 4))
    global_metrics.update(_family_metrics(result_rows, k_list, 2))

    by_chapter, chapter_audit = _group_metrics(result_rows, "capitulo_ref", k_list, max_k, args.min_group_size)
    by_heading, heading_audit = _group_metrics(result_rows, "partida_ref", k_list, max_k, args.min_group_size)

    warnings: list[str] = []
    if len(result_rows) != 600:
        warnings.append(f"Evalset row count is {len(result_rows)}, expected 600 for v0.1.")
    if regimen_counts.get("12", 0):
        warnings.append(f"Evalset contains {regimen_counts.get('12', 0)} case(s) with regimen=12; not modified.")
    if any(rank == 0 for rank in ranks):
        warnings.append("Some reference codes were not found within retrieval_depth.")
    if not (artifact_dir / "index" / "hnsw.index").exists():
        warnings.append("Configured HNSW index file is absent; this run used brute-force dense retrieval.")

    dense_summary = retriever.artifact_summary()
    dense_summary.update(
        {
            "artifact_dir": _report_path(artifact_dir, root),
            "vectors_path": _report_path(artifact_dir / "index" / "vectors.npy", root),
            "id_map_path": _report_path(artifact_dir / "index" / "id_map.json", root),
            "docstore_path": _report_path(artifact_dir / "store" / "nandina8_docstore.jsonl", root),
            "model_path": _report_path(model_path, root),
        }
    )

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_dense_text2trade",
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
        "evalset_version": args.evalset_version,
        "input": {
            "evalset_path": _report_path(evalset_path, root),
            "evalset_sha256": sha256_file(evalset_path),
            "artifact_dir": _report_path(artifact_dir, root),
        },
        "dense_config": {
            **dense_summary,
            "retrieval_depth": retrieval_depth,
            "evaluated_k": k_list,
            "retrieval_mode": "brute_force_dense_dot_product",
            "uses_hnsw": False,
            "uses_llm": False,
            "hnsw_index_exists": (artifact_dir / "index" / "hnsw.index").exists(),
        },
        "global_metrics": global_metrics,
        "metrics_by_chapter": by_chapter,
        "metrics_by_heading": by_heading,
        "grouping": {
            "min_group_size": args.min_group_size,
            "chapter": chapter_audit,
            "heading": heading_audit,
        },
        "warnings": warnings,
        "limitations": [
            "Dense brute-force retrieval only; HNSW index was not used.",
            "No LLM was executed.",
            "Results depend on the frozen local Text2Trade model and vector artifacts.",
            "The evalset is concentrated in regimen 10 and contains one observed regimen 12 case.",
        ],
        "output": {
            "output_dir": _report_path(output_dir, root),
            "results_csv": _report_path(output_dir / "results.csv", root),
            "metrics_json": _report_path(output_dir / "metrics.json", root),
            "summary_md": _report_path(output_dir / "summary.md", root),
        },
    }

    hit_columns = [_hit_column(k) for k in sorted(set(DEFAULT_K_LIST + list(k_list)))]
    fieldnames = RESULT_BASE_COLUMNS[:6] + hit_columns + RESULT_BASE_COLUMNS[6:] + _candidate_columns(max_k)
    _write_csv(output_dir / "results.csv", result_rows, fieldnames)
    _write_json(output_dir / "metrics.json", metrics)
    ensure_parent(output_dir / "summary.md")
    (output_dir / "summary.md").write_text(_summary_markdown(metrics, k_list, max_k), encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate dense Text2Trade retrieval by brute force.")
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--evalset-version", default="v0.1")
    parser.add_argument("--artifact-dir", type=Path, default=DEFAULT_ARTIFACT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--k-list", default="1,3,5,10")
    parser.add_argument("--retrieval-depth", type=int, default=10)
    parser.add_argument("--model-path", type=Path, default=None)
    parser.add_argument("--min-group-size", type=int, default=5)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    metrics = evaluate(args)
    global_metrics = metrics["global_metrics"]
    print("OK: evaluacion densa Text2Trade completada")
    print(f"Casos evaluados: {global_metrics['cases_total']}")
    for k in metrics["dense_config"]["evaluated_k"]:
        print(f"Top-{k} accuracy: {global_metrics[f'top_{k}_accuracy']:.4f}")
    print(f"MRR: {global_metrics['mrr']:.4f}")
    print(f"Top-10 HS4: {global_metrics.get('top_10_hs4_accuracy', 0.0):.4f}")
    print(f"Top-10 HS2: {global_metrics.get('top_10_hs2_accuracy', 0.0):.4f}")
    print(f"Outputs: {metrics['output']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
