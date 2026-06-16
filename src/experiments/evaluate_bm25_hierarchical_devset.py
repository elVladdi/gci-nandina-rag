from __future__ import annotations

import argparse
import csv
import json
import platform
import re
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_FLAT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_HIER_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_hierarchical_devset_v0.1")
DEFAULT_REPORT = Path("docs/evaluacion_bm25_corpus_jerarquico_devset_v0.1.md")
EXPECTED_DEVSET_ROWS = 13
K_LIST = [1, 3, 5, 10]
GENERIC_PHRASES = {
    "los demas",
    "las demas",
    "los dems",
    "las dems",
    "demas",
    "solido",
    "liquido",
    "ruedas",
    "partes",
    "otros",
    "otras",
}


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _norm(text: object) -> str:
    raw = _clean(text).lower()
    raw = unicodedata.normalize("NFKD", raw)
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch))
    raw = re.sub(r"[^a-z0-9]+", " ", raw)
    return re.sub(r"\s+", " ", raw).strip()


def _is_short_or_generic(text: object) -> bool:
    value = _clean(text).rstrip(".:")
    return len(value) <= 12 or _norm(value) in GENERIC_PHRASES


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


def _rank_metric(rank: int, depth: int) -> int:
    return rank if rank > 0 else depth + 1


def _outcome(flat_rank: int, hier_rank: int, depth: int) -> str:
    flat_metric = _rank_metric(flat_rank, depth)
    hier_metric = _rank_metric(hier_rank, depth)
    if hier_metric < flat_metric:
        return "ganado"
    if hier_metric > flat_metric:
        return "perdido"
    return "sin_cambio"


def _same_prefix_in_top(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int = 10) -> int:
    prefix = true_code[:prefix_len]
    return int(any(_clean(hit.get("code")).startswith(prefix) for hit in hits[:k]))


def _top_codes(hits: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_clean(hit.get("code")) for hit in hits[:limit])


def _candidate_columns(prefix: str, limit: int) -> list[str]:
    columns: list[str] = []
    for rank in range(1, limit + 1):
        columns.extend([f"{prefix}_{rank}_code", f"{prefix}_{rank}_score", f"{prefix}_{rank}_text"])
    return columns


def _add_candidates(row: dict[str, Any], prefix: str, hits: Sequence[Mapping[str, Any]], limit: int) -> None:
    for rank in range(1, limit + 1):
        hit = hits[rank - 1] if rank <= len(hits) else None
        row[f"{prefix}_{rank}_code"] = _clean(hit.get("code")) if hit else ""
        row[f"{prefix}_{rank}_score"] = hit.get("score", "") if hit else ""
        row[f"{prefix}_{rank}_text"] = _clean(hit.get("text")) if hit else ""


def _doc_text_by_code(index: Any, code: str) -> str:
    try:
        position = list(index.doc_ids).index(code)
    except ValueError:
        return ""
    return _clean(index.doc_texts[position])


def _metrics_from_ranks(rows: Sequence[Mapping[str, Any]], prefix: str) -> dict[str, Any]:
    ranks = [int(row[f"{prefix}_rank"]) for row in rows]
    metrics: dict[str, Any] = {
        "cases_total": len(rows),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "recall_at_50": _mean([acc_at_k(rank, 50) for rank in ranks]),
        "recall_at_100": _mean([acc_at_k(rank, 100) for rank in ranks]),
        "top_10_hs4": _mean([float(row[f"{prefix}_top10_hs4"]) for row in rows]),
        "top_10_hs2": _mean([float(row[f"{prefix}_top10_hs2"]) for row in rows]),
        "not_found_at_depth": sum(1 for rank in ranks if rank <= 0),
    }
    for k in K_LIST:
        metrics[f"top_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
    return metrics


def _smoke_rank(index: Any, query: str, expected_code: str, depth: int) -> dict[str, Any]:
    hits = retrieve(index, query, top_n=depth)
    rank = rank_of_true(hits, expected_code)
    return {
        "query": query,
        "expected_code": expected_code,
        "rank": rank,
        "top_10_codes": [_clean(hit.get("code")) for hit in hits[:10]],
    }


def _summary_markdown(metrics: Mapping[str, Any]) -> str:
    flat = metrics["flat_metrics"]
    hier = metrics["hierarchical_metrics"]
    comparison = metrics["comparison"]
    smoke = metrics["smoke_tests"]
    lines = [
        "# Evaluacion BM25 corpus jerarquico devset v0.1",
        "",
        "## Objetivo",
        "",
        "Comparar el ranking BM25 inicial actual contra un indice BM25 construido sobre un corpus NANDINA8 con contexto jerarquico 4D/6D/8D. La evaluacion usa solo el devset intermedio de 13 casos; no se ejecuto evalset, LLM ni Text2Trade.",
        "",
        "## Por que se reconstruyo el corpus",
        "",
        "El corpus plano actual indexa varias subpartidas con textos demasiado breves, por ejemplo `Solido`, `Ruedas` o `Los demas`. El corpus jerarquico agrega seccion, capitulo, partida 4D, HS6 cuando existe, descripcion NANDINA8 y unidad fisica en `texto_index_jerarquico`.",
        "",
        "## Metricas comparativas",
        "",
        "| Metrica | BM25 actual | BM25 jerarquico | Delta |",
        "|---|---:|---:|---:|",
    ]
    for key, label in [
        ("top_1", "Top-1"),
        ("top_3", "Top-3"),
        ("top_5", "Top-5"),
        ("top_10", "Top-10"),
        ("mrr", "MRR"),
        ("recall_at_50", "Recall@50"),
        ("recall_at_100", "Recall@100"),
        ("top_10_hs4", "Top-10 HS4"),
        ("top_10_hs2", "Top-10 HS2"),
    ]:
        lines.append(f"| {label} | {flat[key]:.4f} | {hier[key]:.4f} | {hier[key] - flat[key]:+.4f} |")
    lines.extend(
        [
            "",
            "## Casos ganados y perdidos",
            "",
            f"- Ganados: {comparison['ganados']}.",
            f"- Perdidos: {comparison['perdidos']}.",
            f"- Sin cambio: {comparison['sin_cambio']}.",
            f"- Antes no encontrados y ahora encontrados: {comparison['antes_no_encontrados_ahora_encontrados']}.",
            f"- Casos degradados: {comparison['casos_degradados']}.",
            "",
            "## Ejemplos concretos",
            "",
            "- `28151100`: antes el texto plano era `Solido`; despues queda enriquecido con la partida 28.15 sobre hidroxido de sodio, sosa o soda caustica, mas la forma solida.",
            "- `Los demas`: las descripciones genericas dejan de depender solo de la frase generica porque el texto indexable incorpora el contexto de partida/capitulo disponible.",
            "",
            "## Smoke tests",
            "",
            f"- Consulta `soda caustica solida`: BM25 actual rank {smoke['soda_caustica_solida']['flat']['rank']}; jerarquico rank {smoke['soda_caustica_solida']['hierarchical']['rank']}.",
            f"- Consulta `ruedas`: BM25 actual rank {smoke['ruedas']['flat']['rank']}; jerarquico rank {smoke['ruedas']['hierarchical']['rank']}.",
            "",
            "## Decision metodologica",
            "",
            f"{metrics['recommendation']}",
            "",
            "## Limitaciones",
            "",
            "- El devset tiene 13 casos y solo sirve como senal temprana.",
            "- La cobertura HS6 del JSONL intermedio es incompleta; muchos registros usan contexto 4D sin HS6 explicito.",
            "- La comparacion no valida fundamento legal ni clasificacion oficial, solo recuperacion lexical BM25.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    devset_path = resolve_project_path(args.devset)
    flat_index_path = resolve_project_path(args.flat_index)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    output_dir = resolve_project_path(args.output_dir)
    report_doc_path = resolve_project_path(args.report)
    depth = args.retrieval_depth
    candidate_limit = args.candidate_limit

    dev_rows = _read_csv(devset_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")

    flat_index = load_bm25_index(flat_index_path)
    hierarchical_index = load_bm25_index(hierarchical_index_path)
    start = time.time()
    result_rows: list[dict[str, Any]] = []
    for position, dev_row in enumerate(dev_rows, start=1):
        descripcion = _clean(dev_row.get("descripcion"))
        true_code = _clean(dev_row.get("nandina") or dev_row.get("nandina_ref"))
        flat_hits = retrieve(flat_index, descripcion, top_n=depth)
        hierarchical_hits = retrieve(hierarchical_index, descripcion, top_n=depth)
        flat_rank = rank_of_true(flat_hits, true_code)
        hierarchical_rank = rank_of_true(hierarchical_hits, true_code)
        flat_true_text = _doc_text_by_code(flat_index, true_code)
        hierarchical_true_text = _doc_text_by_code(hierarchical_index, true_code)
        outcome = _outcome(flat_rank, hierarchical_rank, depth)
        row: dict[str, Any] = {
            "case_id": f"dev-{position:02d}",
            "descripcion": descripcion,
            "nandina_ref": true_code,
            "hs4_ref": true_code[:4],
            "hs2_ref": true_code[:2],
            "flat_rank": flat_rank,
            "hierarchical_rank": hierarchical_rank,
            "rank_delta_positive_improves": _rank_metric(flat_rank, depth) - _rank_metric(hierarchical_rank, depth),
            "outcome": outcome,
            "flat_top10_hs4": _same_prefix_in_top(flat_hits, true_code, 4),
            "hierarchical_top10_hs4": _same_prefix_in_top(hierarchical_hits, true_code, 4),
            "flat_top10_hs2": _same_prefix_in_top(flat_hits, true_code, 2),
            "hierarchical_top10_hs2": _same_prefix_in_top(hierarchical_hits, true_code, 2),
            "flat_true_text": flat_true_text,
            "hierarchical_true_text": hierarchical_true_text,
            "flat_true_text_short_or_generic": int(_is_short_or_generic(flat_true_text)),
            "flat_top10_codes": _top_codes(flat_hits),
            "hierarchical_top10_codes": _top_codes(hierarchical_hits),
        }
        for prefix, rank in [("flat", flat_rank), ("hierarchical", hierarchical_rank)]:
            for k in K_LIST:
                row[f"{prefix}_hit_top_{k}"] = int(acc_at_k(rank, k))
            row[f"{prefix}_recall_at_50"] = int(acc_at_k(rank, 50))
            row[f"{prefix}_recall_at_100"] = int(acc_at_k(rank, 100))
        _add_candidates(row, "flat_candidate", flat_hits, candidate_limit)
        _add_candidates(row, "hierarchical_candidate", hierarchical_hits, candidate_limit)
        result_rows.append(row)

    flat_metrics = _metrics_from_ranks(result_rows, "flat")
    hierarchical_metrics = _metrics_from_ranks(result_rows, "hierarchical")
    generic_rows = [row for row in result_rows if row["flat_true_text_short_or_generic"]]
    generic_analysis = {
        "cases_with_flat_true_text_short_or_generic": len(generic_rows),
        "flat_mrr": _mean([mrr_from_rank(int(row["flat_rank"])) for row in generic_rows]),
        "hierarchical_mrr": _mean([mrr_from_rank(int(row["hierarchical_rank"])) for row in generic_rows]),
        "flat_top_10": _mean([acc_at_k(int(row["flat_rank"]), 10) for row in generic_rows]),
        "hierarchical_top_10": _mean([acc_at_k(int(row["hierarchical_rank"]), 10) for row in generic_rows]),
    }
    comparison = {
        "ganados": sum(1 for row in result_rows if row["outcome"] == "ganado"),
        "perdidos": sum(1 for row in result_rows if row["outcome"] == "perdido"),
        "sin_cambio": sum(1 for row in result_rows if row["outcome"] == "sin_cambio"),
        "antes_no_encontrados_ahora_encontrados": sum(
            1 for row in result_rows if int(row["flat_rank"]) == 0 and int(row["hierarchical_rank"]) > 0
        ),
        "casos_degradados": sum(
            1
            for row in result_rows
            if _rank_metric(int(row["hierarchical_rank"]), depth) > _rank_metric(int(row["flat_rank"]), depth)
        ),
    }
    smoke_tests = {
        "soda_caustica_solida": {
            "flat": _smoke_rank(flat_index, "soda caustica solida", "28151100", depth),
            "hierarchical": _smoke_rank(hierarchical_index, "soda caustica solida", "28151100", depth),
        },
        "ruedas": {
            "flat": _smoke_rank(flat_index, "ruedas", "83022000", depth),
            "hierarchical": _smoke_rank(hierarchical_index, "ruedas", "83022000", depth),
        },
    }

    should_scale = (
        hierarchical_metrics["recall_at_100"] >= flat_metrics["recall_at_100"]
        and hierarchical_metrics["top_10"] >= flat_metrics["top_10"]
        and comparison["perdidos"] == 0
    )
    recommendation = (
        "Escalar al evalset en una subfase separada, porque el corpus jerarquico no degrada el devset y mejora o conserva el recall amplio."
        if should_scale
        else "No escalar todavia al evalset como sustituto directo: revisar degradaciones del devset y considerar una variante hibrida que preserve senales cortas utiles del corpus plano."
    )

    def rel_path(path: Path) -> str:
        try:
            return path.resolve().relative_to(root).as_posix()
        except ValueError:
            return str(path.resolve())

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_hierarchical_devset",
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
            "devset_path": rel_path(devset_path),
            "devset_sha256": sha256_file(devset_path),
            "flat_index_path": rel_path(flat_index_path),
            "flat_index_sha256": sha256_file(flat_index_path),
            "hierarchical_index_path": rel_path(hierarchical_index_path),
            "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
        },
        "bm25_config": {
            "retrieval_depth": depth,
            "k_list": K_LIST,
            "flat_docs": len(flat_index.doc_ids),
            "hierarchical_docs": len(hierarchical_index.doc_ids),
            "flat_avgdl": float(getattr(flat_index, "avgdl", 0.0)),
            "hierarchical_avgdl": float(getattr(hierarchical_index, "avgdl", 0.0)),
            "flat_vocab_size": len(getattr(flat_index, "idf", {})),
            "hierarchical_vocab_size": len(getattr(hierarchical_index, "idf", {})),
        },
        "flat_metrics": flat_metrics,
        "hierarchical_metrics": hierarchical_metrics,
        "comparison": comparison,
        "generic_short_analysis": generic_analysis,
        "smoke_tests": smoke_tests,
        "recommendation": recommendation,
        "outputs": {
            "results_csv": rel_path(output_dir / "results.csv"),
            "metrics_json": rel_path(output_dir / "metrics.json"),
            "summary_md": rel_path(output_dir / "summary.md"),
            "case_comparison_13_cases_csv": rel_path(output_dir / "case_comparison_13_cases.csv"),
            "failure_analysis_csv": rel_path(output_dir / "failure_analysis.csv"),
            "report_md": rel_path(report_doc_path),
        },
        "warnings": [
            "This evaluation used devset only; evalset was not read or executed.",
            "No LLM or Text2Trade execution is part of this script.",
        ],
    }

    base_columns = [
        "case_id",
        "descripcion",
        "nandina_ref",
        "hs4_ref",
        "hs2_ref",
        "flat_rank",
        "hierarchical_rank",
        "rank_delta_positive_improves",
        "outcome",
        "flat_top10_hs4",
        "hierarchical_top10_hs4",
        "flat_top10_hs2",
        "hierarchical_top10_hs2",
        "flat_true_text_short_or_generic",
        "flat_true_text",
        "hierarchical_true_text",
        "flat_top10_codes",
        "hierarchical_top10_codes",
    ]
    hit_columns: list[str] = []
    for prefix in ["flat", "hierarchical"]:
        hit_columns.extend([f"{prefix}_hit_top_{k}" for k in K_LIST])
        hit_columns.extend([f"{prefix}_recall_at_50", f"{prefix}_recall_at_100"])
    candidate_columns = _candidate_columns("flat_candidate", candidate_limit) + _candidate_columns(
        "hierarchical_candidate", candidate_limit
    )
    fieldnames = base_columns + hit_columns + candidate_columns
    _write_csv(output_dir / "results.csv", result_rows, fieldnames)
    _write_csv(output_dir / "case_comparison_13_cases.csv", result_rows, base_columns + hit_columns)
    failures = [
        row
        for row in result_rows
        if row["outcome"] == "perdido" or int(row["hierarchical_rank"]) <= 0 or int(row["hierarchical_rank"]) > 10
    ]
    _write_csv(output_dir / "failure_analysis.csv", failures, base_columns + hit_columns)
    _write_json(output_dir / "metrics.json", metrics)
    ensure_parent(output_dir / "summary.md")
    (output_dir / "summary.md").write_text(_summary_markdown(metrics), encoding="utf-8")
    ensure_parent(report_doc_path)
    report_doc_path.write_text(_summary_markdown(metrics), encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare current BM25 and hierarchical BM25 on devset only.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--flat-index", type=Path, default=DEFAULT_FLAT_INDEX)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIER_INDEX)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    parser.add_argument("--candidate-limit", type=int, default=10)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    flat = metrics["flat_metrics"]
    hier = metrics["hierarchical_metrics"]
    print("OK: evaluacion BM25 jerarquico devset completada")
    print(f"Casos evaluados: {flat['cases_total']}")
    for key in ["top_1", "top_3", "top_5", "top_10", "mrr", "recall_at_50", "recall_at_100"]:
        print(f"{key}: actual={flat[key]:.4f} jerarquico={hier[key]:.4f}")
    print(f"Ganados: {metrics['comparison']['ganados']}")
    print(f"Perdidos: {metrics['comparison']['perdidos']}")
    print(f"Sin cambio: {metrics['comparison']['sin_cambio']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
