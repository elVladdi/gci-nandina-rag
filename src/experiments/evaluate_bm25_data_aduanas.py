from __future__ import annotations

import argparse
import csv
import json
import platform
import re
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.1.csv")
DEFAULT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1")
DEFAULT_REPORT = Path("docs/evaluacion_bm25_data_aduanas_clase87_v0.1.md")
QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
K_LIST = [1, 3, 5, 10]
RECALL_K_LIST = [50, 100]
FAMILY_K_LIST = [10, 50, 100]
EXPECTED_SCOPE_CLASS = "87"
RESULT_CANDIDATES = 10
FAILURE_SAMPLE_SIZE = 50


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


def _normalize_code(value: object) -> str:
    return re.sub(r"\D", "", _clean(value))


def _family_hit(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int) -> int:
    prefix = true_code[:prefix_len]
    if not prefix:
        return 0
    return int(any(_clean(hit.get("code")).startswith(prefix) for hit in hits[:k]))


def _top_codes(hits: Sequence[Mapping[str, Any]], limit: int = RESULT_CANDIDATES) -> str:
    return " ".join(_clean(hit.get("code")) for hit in hits[:limit])


def _candidate_columns(max_candidates: int) -> list[str]:
    columns: list[str] = []
    for rank in range(1, max_candidates + 1):
        columns.extend([f"candidate_{rank}_code", f"candidate_{rank}_score", f"candidate_{rank}_text"])
    return columns


def _add_candidates(row: dict[str, Any], hits: Sequence[Mapping[str, Any]], max_candidates: int) -> None:
    for rank in range(1, max_candidates + 1):
        hit = hits[rank - 1] if rank <= len(hits) else None
        row[f"candidate_{rank}_code"] = _clean(hit.get("code")) if hit else ""
        row[f"candidate_{rank}_score"] = hit.get("score", "") if hit else ""
        row[f"candidate_{rank}_text"] = _clean(hit.get("text")) if hit else ""


def _rank_distribution(ranks: Sequence[int], max_k: int) -> dict[str, int]:
    counter = Counter(ranks)
    payload = {str(rank): counter.get(rank, 0) for rank in range(1, max_k + 1)}
    payload[f">{max_k}"] = sum(count for rank, count in counter.items() if rank > max_k)
    payload["not_found"] = counter.get(0, 0)
    return payload


def _metric_rows(metrics: Mapping[str, Any]) -> list[tuple[str, str]]:
    global_metrics = metrics["global_metrics"]
    hierarchical = metrics["hierarchical_metrics"]
    rows = [
        ("Casos evaluados", str(global_metrics["cases_total"])),
        ("Casos con recuperacion", str(global_metrics["cases_with_retrieval"])),
        ("Top-1 NANDINA8", f"{global_metrics['top_1_accuracy']:.4f}"),
        ("Top-3 NANDINA8", f"{global_metrics['top_3_accuracy']:.4f}"),
        ("Top-5 NANDINA8", f"{global_metrics['top_5_accuracy']:.4f}"),
        ("Top-10 NANDINA8", f"{global_metrics['top_10_accuracy']:.4f}"),
        ("MRR", f"{global_metrics['mrr']:.4f}"),
        ("Recall@50", f"{global_metrics['recall_at_50']:.4f}"),
        ("Recall@100", f"{global_metrics['recall_at_100']:.4f}"),
        ("Partida@100", f"{hierarchical['partida_at_100']:.4f}"),
        ("Sub Partida@100", f"{hierarchical['sub_partida_at_100']:.4f}"),
        ("Clase@100", f"{hierarchical['clase_at_100']:.4f}"),
        ("Sin match a profundidad", str(global_metrics["not_found_at_depth"])),
    ]
    return rows


def _summary_markdown(metrics: Mapping[str, Any]) -> str:
    global_metrics = metrics["global_metrics"]
    hierarchical = metrics["hierarchical_metrics"]
    lines = [
        "# Evaluacion BM25 data_aduanas clase 87 v0.1",
        "",
        "## Objetivo",
        "",
        "Evaluar el baseline BM25 normativo plano sobre el nuevo evalset `data_aduanas` de Clase = 87, sin reemplazar ni reinterpretar la evaluacion BM25 v0.1 historica de 600 casos.",
        "",
        "## Insumos",
        "",
        f"- Fuente metodologica: `data_aduanas`.",
        f"- Alcance: Clase = `{metrics['scope']['class']}`.",
        f"- Evalset: `{metrics['input']['evalset_path']}`.",
        f"- Filas evaluadas: {global_metrics['cases_total']}.",
        f"- Columna de consulta: `{metrics['columns']['query_column']}`.",
        f"- Etiqueta esperada: `{metrics['columns']['label_column']}`.",
        f"- Indice BM25 normativo: `{metrics['input']['bm25_index_path']}`.",
        f"- Profundidad de recuperacion: {metrics['bm25_config']['retrieval_depth']}.",
        "",
        "## Metricas exactas",
        "",
        "| Metrica | Valor |",
        "| --- | ---: |",
    ]
    for label, value in _metric_rows(metrics)[:9]:
        lines.append(f"| {label} | {value} |")

    lines.extend(
        [
            "",
            "## Metricas jerarquicas",
            "",
            "| Corte | Partida HS4 | Sub Partida HS6 | Clase HS2 |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for k in FAMILY_K_LIST:
        lines.append(
            f"| Top-{k} | {hierarchical[f'partida_at_{k}']:.4f} | "
            f"{hierarchical[f'sub_partida_at_{k}']:.4f} | {hierarchical[f'clase_at_{k}']:.4f} |"
        )

    lines.extend(
        [
            "",
            "## Lectura metodologica",
            "",
            "BM25 normativo se conserva como baseline lexical de referencia. En este evalset de descripciones comerciales clase 87, el desempeno exacto NANDINA8 es bajo frente a la profundidad amplia de recuperacion. La brecha entre aciertos exactos y aciertos jerarquicos muestra que el indice normativo puede acercarse a familias arancelarias, pero no debe tratarse como recuperacion historica principal.",
            "",
            "## Comparabilidad con Fase 4 anterior",
            "",
            "La Fase 4 historica v0.1 evaluo BM25 sobre `data/processed/evalset_v0.1.csv` con 600 casos de otra fuente y alcance. Esta actualizacion evalua `data_aduanas` Clase = 87 con otro tamano, fuente y distribucion. Las metricas no son una comparacion pareada ni deben leerse como mejora o degradacion sobre el mismo conjunto; sirven para contrastar dos baselines de alcance distinto.",
            "",
            "## Decision",
            "",
            "BM25 normativo sirve como baseline auditable de referencia para fases futuras sobre `data_aduanas`, pero no como recuperacion historica principal. Para pipelines posteriores, lo normativo debe operar como respaldo/trazabilidad y comparador minimo, mientras la recuperacion historica clase 87 debe evaluarse por separado contra su propio banco historico.",
            "",
            "## Controles",
            "",
            "- No se ejecuto LLM.",
            "- No se ejecuto Text2Trade.",
            "- No se modifico el evalset historico v0.1 ni los splits de Fase 3.",
            "- Los outputs bajo `outputs/` son regenerables e ignorados por Git.",
            "",
        ]
    )
    if global_metrics["zero_retrieval_cases"]:
        lines.extend(
            [
                "## Advertencias",
                "",
                f"- Casos sin resultados recuperados: {global_metrics['zero_retrieval_cases']}.",
                "",
            ]
        )
    return "\n".join(lines)


def _validate_inputs(rows: Sequence[Mapping[str, str]], query_column: str, label_column: str) -> list[str]:
    warnings: list[str] = []
    if not rows:
        raise ValueError("Evalset is empty.")
    missing = [column for column in [query_column, label_column] if column not in rows[0]]
    if missing:
        raise ValueError(f"Missing required columns in evalset: {missing}")
    empty_queries = sum(1 for row in rows if not _clean(row.get(query_column)))
    invalid_labels = sum(1 for row in rows if not re.fullmatch(r"\d{8}", _normalize_code(row.get(label_column))))
    if empty_queries:
        raise ValueError(f"Found empty queries in {query_column}: {empty_queries}")
    if invalid_labels:
        raise ValueError(f"Found non-NANDINA8 expected labels in {label_column}: {invalid_labels}")
    non_scope = sum(1 for row in rows if _normalize_code(row.get(label_column))[:2] != EXPECTED_SCOPE_CLASS)
    if non_scope:
        warnings.append(f"{non_scope} rows have expected code outside Clase {EXPECTED_SCOPE_CLASS}.")
    return warnings


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    evalset_path = resolve_project_path(args.evalset)
    index_path = resolve_project_path(args.index)
    output_dir = resolve_project_path(args.output_dir)
    report_path = resolve_project_path(args.report)
    depth = max(args.retrieval_depth, max(RECALL_K_LIST), max(FAMILY_K_LIST), max(K_LIST))

    eval_rows = _read_csv(evalset_path)
    warnings = _validate_inputs(eval_rows, args.query_column, args.label_column)
    index = load_bm25_index(index_path)

    start = time.time()
    result_rows: list[dict[str, Any]] = []
    for position, eval_row in enumerate(eval_rows, start=1):
        query = _clean(eval_row.get(args.query_column))
        expected = _normalize_code(eval_row.get(args.label_column))
        hits = retrieve(index, query, top_n=depth)
        rank = rank_of_true(hits, expected)
        result: dict[str, Any] = {
            "case_id": _clean(eval_row.get("case_id")) or f"data-aduanas-eval-{position:05d}",
            "query": query,
            "nandina_ref": expected,
            "partida_ref": expected[:4],
            "sub_partida_ref": expected[:6],
            "clase_ref": expected[:2],
            "rank_ref": rank,
            "retrieved_count": len(hits),
            "top_codes": _top_codes(hits),
        }
        for k in K_LIST:
            result[f"hit_top_{k}"] = int(acc_at_k(rank, k))
        for k in RECALL_K_LIST:
            result[f"hit_recall_{k}"] = int(acc_at_k(rank, k))
        for k in FAMILY_K_LIST:
            result[f"partida_at_{k}"] = _family_hit(hits, expected, 4, k)
            result[f"sub_partida_at_{k}"] = _family_hit(hits, expected, 6, k)
            result[f"clase_at_{k}"] = _family_hit(hits, expected, 2, k)
        _add_candidates(result, hits, RESULT_CANDIDATES)
        result_rows.append(result)

    ranks = [int(row["rank_ref"]) for row in result_rows]
    retrieved_counts = [int(row["retrieved_count"]) for row in result_rows]
    global_metrics: dict[str, Any] = {
        "cases_total": len(result_rows),
        "cases_with_retrieval": sum(1 for count in retrieved_counts if count > 0),
        "retrieval_rate": _mean([1.0 if count > 0 else 0.0 for count in retrieved_counts]),
        "zero_retrieval_cases": sum(1 for count in retrieved_counts if count == 0),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "not_found_at_depth": sum(1 for rank in ranks if rank <= 0),
        "rank_distribution": _rank_distribution(ranks, max_k=max(K_LIST)),
    }
    for k in K_LIST:
        global_metrics[f"top_{k}_accuracy"] = _mean([acc_at_k(rank, k) for rank in ranks])
    for k in RECALL_K_LIST:
        global_metrics[f"recall_at_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])

    hierarchical_metrics: dict[str, Any] = {}
    for k in FAMILY_K_LIST:
        hierarchical_metrics[f"partida_at_{k}"] = _mean([float(row[f"partida_at_{k}"]) for row in result_rows])
        hierarchical_metrics[f"sub_partida_at_{k}"] = _mean([float(row[f"sub_partida_at_{k}"]) for row in result_rows])
        hierarchical_metrics[f"clase_at_{k}"] = _mean([float(row[f"clase_at_{k}"]) for row in result_rows])

    failure_rows = [row for row in result_rows if int(row["rank_ref"]) <= 0 or int(row["rank_ref"]) > max(K_LIST)]
    failure_sample = failure_rows[: args.failure_sample_size]
    if global_metrics["not_found_at_depth"]:
        warnings.append("Some expected NANDINA8 labels were not found within retrieval_depth.")
    if global_metrics["zero_retrieval_cases"]:
        warnings.append("Some queries produced zero BM25 results.")

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_data_aduanas",
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
            "evalset_path": _rel(evalset_path, root),
            "evalset_abs_path": str(evalset_path),
            "evalset_sha256": sha256_file(evalset_path),
            "bm25_index_path": _rel(index_path, root),
            "bm25_index_abs_path": str(index_path),
            "bm25_index_sha256": sha256_file(index_path),
        },
        "scope": {
            "source": "data_aduanas",
            "class": EXPECTED_SCOPE_CLASS,
            "evalset_role": "main evalset for future phases after updated Phase 3",
        },
        "columns": {
            "query_column": args.query_column,
            "label_column": args.label_column,
        },
        "bm25_config": {
            "retrieval_depth": depth,
            "k_list": K_LIST,
            "recall_k_list": RECALL_K_LIST,
            "family_k_list": FAMILY_K_LIST,
            "k1": getattr(index, "k1", None),
            "b": getattr(index, "b", None),
            "docs_indexed": len(index.doc_ids),
            "avgdl": getattr(index, "avgdl", None),
            "vocab_size": len(getattr(index, "idf", {})),
        },
        "global_metrics": global_metrics,
        "hierarchical_metrics": hierarchical_metrics,
        "validations": {
            "evalset_rows": len(eval_rows),
            "results_rows": len(result_rows),
            "results_match_evalset_rows": len(eval_rows) == len(result_rows),
            "empty_queries": 0,
            "invalid_expected_labels": 0,
            "expected_labels_nandina8": True,
            "llm_executed": False,
            "text2trade_executed": False,
        },
        "comparability_note": (
            "Historical Phase 4 v0.1 used evalset_v0.1.csv with 600 cases; this run uses data_aduanas "
            "Clase 87 evalset with a different source, scope and size. Metrics are not paired."
        ),
        "warnings": warnings,
        "output": {
            "output_dir": _rel(output_dir, root),
            "output_abs_dir": str(output_dir),
            "results_csv": _rel(output_dir / "results.csv", root),
            "metrics_json": _rel(output_dir / "metrics.json", root),
            "summary_md": _rel(output_dir / "summary.md", root),
            "failure_sample_csv": _rel(output_dir / "failure_sample.csv", root),
            "report_md": _rel(report_path, root),
        },
    }

    base_fields = [
        "case_id",
        "query",
        "nandina_ref",
        "partida_ref",
        "sub_partida_ref",
        "clase_ref",
        "rank_ref",
        "retrieved_count",
        "top_codes",
    ]
    hit_fields = [f"hit_top_{k}" for k in K_LIST] + [f"hit_recall_{k}" for k in RECALL_K_LIST]
    family_fields: list[str] = []
    for k in FAMILY_K_LIST:
        family_fields.extend([f"partida_at_{k}", f"sub_partida_at_{k}", f"clase_at_{k}"])
    fieldnames = base_fields + hit_fields + family_fields + _candidate_columns(RESULT_CANDIDATES)

    _write_csv(output_dir / "results.csv", result_rows, fieldnames)
    _write_csv(output_dir / "failure_sample.csv", failure_sample, fieldnames)
    _write_json(output_dir / "metrics.json", metrics)
    summary = _summary_markdown(metrics)
    ensure_parent(output_dir / "summary.md")
    (output_dir / "summary.md").write_text(summary, encoding="utf-8")
    ensure_parent(report_path)
    report_path.write_text(summary, encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate normative BM25 on data_aduanas Clase 87 evalset.")
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--query-column", default=QUERY_COLUMN)
    parser.add_argument("--label-column", default=LABEL_COLUMN)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    parser.add_argument("--failure-sample-size", type=int, default=FAILURE_SAMPLE_SIZE)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    global_metrics = metrics["global_metrics"]
    hierarchical = metrics["hierarchical_metrics"]
    print("OK: evaluacion BM25 data_aduanas clase 87 completada")
    print(f"Casos evaluados: {global_metrics['cases_total']}")
    for k in K_LIST:
        print(f"Top-{k} NANDINA8: {global_metrics[f'top_{k}_accuracy']:.4f}")
    print(f"MRR: {global_metrics['mrr']:.4f}")
    print(f"Recall@50: {global_metrics['recall_at_50']:.4f}")
    print(f"Recall@100: {global_metrics['recall_at_100']:.4f}")
    print(f"Partida@100: {hierarchical['partida_at_100']:.4f}")
    print(f"Sub Partida@100: {hierarchical['sub_partida_at_100']:.4f}")
    print(f"Clase@100: {hierarchical['clase_at_100']:.4f}")
    print(f"Outputs: {metrics['output']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
