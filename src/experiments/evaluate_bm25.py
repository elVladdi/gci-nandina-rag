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
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, load_json, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_eval_v0.1")
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
        raise ValueError("k-list/top-k must contain positive integers")
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
                f"candidate_{rank}_text",
            ]
        )
    return columns


def _add_candidates(row: dict[str, Any], hits: Sequence[Mapping[str, Any]], max_candidates: int) -> None:
    for rank in range(1, max_candidates + 1):
        hit = hits[rank - 1] if rank <= len(hits) else None
        row[f"candidate_{rank}_code"] = _clean(hit.get("code")) if hit else ""
        row[f"candidate_{rank}_score"] = hit.get("score", "") if hit else ""
        row[f"candidate_{rank}_text"] = _clean(hit.get("text")) if hit else ""


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
        group_payload: dict[str, Any] = {
            "cases": len(group_rows),
            "retrieved_cases": retrieved,
            "retrieved_rate": _rate(retrieved, len(group_rows)),
            "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
            f"no_match_top_{max_k}": sum(1 for rank in ranks if rank <= 0 or rank > max_k),
        }
        for k in k_list:
            group_payload[f"top_{k}_accuracy"] = _mean([acc_at_k(rank, k) for rank in ranks])
        metrics[group_value] = group_payload

    audit = {
        "field": group_field,
        "min_group_size": min_group_size,
        "groups_total": len(grouped),
        "groups_reported": len(metrics),
        "groups_excluded_small_n": excluded_small,
        "cases_excluded_small_groups": excluded_cases,
    }
    return metrics, audit


def _rank_distribution(ranks: Sequence[int], max_k: int) -> dict[str, int]:
    counter = Counter(ranks)
    payload = {str(rank): counter.get(rank, 0) for rank in range(1, max_k + 1)}
    payload[f">{max_k}"] = sum(count for rank, count in counter.items() if rank > max_k)
    payload["not_found"] = counter.get(0, 0)
    return payload


def _summary_markdown(metrics: Mapping[str, Any], k_list: Sequence[int], max_k: int) -> str:
    global_metrics = metrics["global_metrics"]
    lines = [
        "# Evaluacion BM25 baseline v0.1",
        "",
        "## Alcance",
        "",
        "Se evaluo el baseline BM25 puro sobre el evalset final v0.1, usando cada `descripcion` como consulta y `nandina_ref` como codigo correcto esperado.",
        "",
        "## Configuracion",
        "",
        f"- Evalset: `{metrics['input']['evalset_path']}`.",
        f"- Indice BM25: `{metrics['input']['bm25_index_path']}`.",
        f"- Cortes evaluados: {', '.join(str(k) for k in k_list)}.",
        f"- Profundidad de recuperacion para rank/MRR: {metrics['bm25_config']['retrieval_depth']}.",
        f"- Parametros BM25: k1={metrics['bm25_config'].get('k1')}, b={metrics['bm25_config'].get('b')}.",
        "",
        "## Resultados globales",
        "",
        f"- Casos evaluados: {global_metrics['cases_total']}.",
        f"- Casos con al menos un resultado recuperado: {global_metrics['cases_with_retrieval']}.",
    ]
    for k in k_list:
        lines.append(f"- Top-{k} accuracy: {global_metrics[f'top_{k}_accuracy']:.4f}.")
    lines.extend(
        [
            f"- MRR: {global_metrics['mrr']:.4f}.",
            f"- Casos sin match en Top-{max_k}: {global_metrics[f'no_match_top_{max_k}']}.",
            "",
            "## Analisis por familia",
            "",
            f"Las metricas por capitulo y partida se reportan solo para grupos con al menos {metrics['grouping']['min_group_size']} casos. Los grupos pequenos se excluyen del reporte agregado para evitar lecturas inestables.",
            "",
            f"- Capitulos reportados: {metrics['grouping']['chapter']['groups_reported']} de {metrics['grouping']['chapter']['groups_total']}.",
            f"- Partidas reportadas: {metrics['grouping']['heading']['groups_reported']} de {metrics['grouping']['heading']['groups_total']}.",
            "",
            "## Limitaciones",
            "",
            "- La evaluacion mide recuperacion lexical BM25, no clasificacion oficial ni validacion juridica.",
            "- El alcance empirico del evalset esta concentrado en regimen 10/importacion para el consumo.",
            "- El MRR queda acotado por la profundidad de recuperacion configurada.",
            "- No se ejecuto LLM ni reescritura de consultas en esta subfase.",
            "",
            "## Siguiente paso sugerido",
            "",
            "Revisar los casos fallidos y la distribucion por familias antes de comparar contra variantes LLM+RAG o re-ranking en una fase posterior.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    config_path = resolve_project_path(args.config)
    config = load_json(config_path)
    paths = config.get("paths", {})
    bm25_cfg = config.get("bm25", {})
    base_dir = paths.get("base_dir") or "."

    evalset_path = resolve_project_path(args.evalset, base_dir=base_dir)
    index_path = resolve_project_path(
        args.index or paths.get("bm25_index_path", "data/processed/indexes/bm25_nandina8.pkl"),
        base_dir=base_dir,
    )
    output_dir = resolve_project_path(args.output_dir, base_dir=base_dir)

    config_k_list = bm25_cfg.get("k_list") or DEFAULT_K_LIST
    k_list = _parse_k_list(args.k_list, config_k_list)
    if args.top_k is not None:
        k_list = _parse_k_list(str(args.top_k), k_list)
    max_k = max(k_list)
    retrieval_depth = args.retrieval_depth or int(bm25_cfg.get("top_n", max_k))
    retrieval_depth = max(retrieval_depth, max_k)

    eval_rows = _read_csv(evalset_path)
    index = load_bm25_index(index_path)

    result_rows: list[dict[str, Any]] = []
    start = time.time()
    for position, row in enumerate(eval_rows, start=1):
        nandina_ref = _clean(row.get("nandina_ref"))
        descripcion = _clean(row.get("descripcion"))
        hits = retrieve(index, descripcion, top_n=retrieval_depth)
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
    global_metrics: dict[str, Any] = {
        "cases_total": len(result_rows),
        "cases_with_retrieval": retrieved_cases,
        "retrieval_rate": _rate(retrieved_cases, len(result_rows)),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "rank_distribution": _rank_distribution(ranks, max_k=max_k),
        f"no_match_top_{max_k}": sum(1 for rank in ranks if rank <= 0 or rank > max_k),
    }
    for k in k_list:
        global_metrics[f"top_{k}_accuracy"] = _mean([acc_at_k(rank, k) for rank in ranks])

    by_chapter, chapter_audit = _group_metrics(result_rows, "capitulo_ref", k_list, max_k, args.min_group_size)
    by_heading, heading_audit = _group_metrics(result_rows, "partida_ref", k_list, max_k, args.min_group_size)

    warnings: list[str] = []
    if len(result_rows) != 600:
        warnings.append(f"Evalset row count is {len(result_rows)}, expected 600 for v0.1.")
    if any(rank == 0 for rank in ranks):
        warnings.append("Some reference codes were not found within retrieval_depth.")
    if heading_audit["groups_excluded_small_n"]:
        warnings.append(
            "HS4 metrics exclude small groups below min_group_size; avoid strong conclusions for sparse headings."
        )

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25",
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
            "evalset_abs_path": str(evalset_path),
            "evalset_sha256": sha256_file(evalset_path),
            "bm25_index_path": _report_path(index_path, root),
            "bm25_index_abs_path": str(index_path),
            "bm25_index_sha256": sha256_file(index_path),
            "config_path": _report_path(config_path, root),
        },
        "bm25_config": {
            "k1": getattr(index, "k1", None),
            "b": getattr(index, "b", None),
            "retrieval_depth": retrieval_depth,
            "evaluated_k": k_list,
            "config_bm25": bm25_cfg,
            "docs_indexed": len(index.doc_ids),
            "avgdl": getattr(index, "avgdl", None),
            "vocab_size": len(getattr(index, "idf", {})),
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
            "BM25 lexical baseline only; no LLM was executed.",
            "Results depend on the frozen local BM25 index and corpus snapshot.",
            "Group metrics are descriptive and suppressed for small groups.",
        ],
        "output": {
            "output_dir": _report_path(output_dir, root),
            "output_abs_dir": str(output_dir),
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
    parser = argparse.ArgumentParser(description="Evaluate the pure BM25 baseline on a NANDINA evalset.")
    parser.add_argument("--config", type=Path, default=Path("src/configs/experiment_config.json"))
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET, help="Path to evalset CSV.")
    parser.add_argument("--evalset-version", default="v0.1")
    parser.add_argument("--index", type=Path, default=None, help="Path to BM25 pickle index.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--top-k", type=int, default=None, help="Single evaluation cutoff, for example 10.")
    parser.add_argument("--k-list", default=None, help="Comma-separated cutoffs, for example 1,3,5,10.")
    parser.add_argument("--retrieval-depth", type=int, default=None, help="Depth used to compute rank_ref/MRR.")
    parser.add_argument("--min-group-size", type=int, default=5)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    metrics = evaluate(args)
    global_metrics = metrics["global_metrics"]
    print("OK: evaluacion BM25 completada")
    print(f"Casos evaluados: {global_metrics['cases_total']}")
    for k in metrics["bm25_config"]["evaluated_k"]:
        print(f"Top-{k} accuracy: {global_metrics[f'top_{k}_accuracy']:.4f}")
    print(f"MRR: {global_metrics['mrr']:.4f}")
    print(f"Outputs: {metrics['output']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
