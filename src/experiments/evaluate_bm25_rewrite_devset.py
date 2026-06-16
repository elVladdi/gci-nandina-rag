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
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, load_json, project_root, resolve_project_path

DEFAULT_CONFIG = Path("src/configs/experiment_config.json")
DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_REWRITES = Path("outputs/evaluation/llm_query_rewrite_devset_v0.1/rewrites.jsonl")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/llm_query_rewrite_devset_v0.1")
DEFAULT_K_LIST = [1, 3, 5, 10]
EXPECTED_DEVSET_ROWS = 13


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


def _metrics_from_ranks(ranks: Sequence[int], k_list: Sequence[int], max_k: int) -> dict[str, Any]:
    metrics: dict[str, Any] = {
        "cases_total": len(ranks),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        f"no_match_top_{max_k}": sum(1 for rank in ranks if rank <= 0 or rank > max_k),
        "not_found": sum(1 for rank in ranks if rank <= 0),
    }
    for k in k_list:
        metrics[f"top_{k}_accuracy"] = _mean([acc_at_k(rank, k) for rank in ranks])
    return metrics


def _delta_rank(original_rank: int, rewritten_rank: int, missing_rank: int) -> int:
    original = original_rank if original_rank > 0 else missing_rank
    rewritten = rewritten_rank if rewritten_rank > 0 else missing_rank
    return original - rewritten


def _case_outcome(original_rank: int, rewritten_rank: int, max_k: int) -> str:
    original_hit = 0 < original_rank <= max_k
    rewritten_hit = 0 < rewritten_rank <= max_k
    if rewritten_hit and not original_hit:
        return "ganado"
    if original_hit and not rewritten_hit:
        return "perdido"
    if original_hit and rewritten_hit:
        if rewritten_rank < original_rank:
            return "ganado"
        if rewritten_rank > original_rank:
            return "perdido"
    return "sin_cambio"


def _candidate_columns(prefix: str, max_candidates: int) -> list[str]:
    columns: list[str] = []
    for rank in range(1, max_candidates + 1):
        columns.extend([f"{prefix}_{rank}_code", f"{prefix}_{rank}_score", f"{prefix}_{rank}_text"])
    return columns


def _add_candidates(row: dict[str, Any], prefix: str, hits: Sequence[Mapping[str, Any]], max_candidates: int) -> None:
    for rank in range(1, max_candidates + 1):
        hit = hits[rank - 1] if rank <= len(hits) else None
        row[f"{prefix}_{rank}_code"] = _clean(hit.get("code")) if hit else ""
        row[f"{prefix}_{rank}_score"] = hit.get("score", "") if hit else ""
        row[f"{prefix}_{rank}_text"] = _clean(hit.get("text")) if hit else ""


def _summary_markdown(metrics: Mapping[str, Any], k_list: Sequence[int], max_k: int) -> str:
    original = metrics["original_metrics"]
    rewritten = metrics["rewritten_metrics"]
    comparison = metrics["comparison"]
    lines = [
        "# BM25 original vs LLM query rewrite devset v0.1",
        "",
        "## Alcance",
        "",
        "Evaluacion BM25 sobre el devset preliminar de 13 casos. Se compara la descripcion original contra `consulta_reescrita` generada localmente por LLM. No se uso el evalset final.",
        "",
        "## Metricas",
        "",
        "| Metrica | Original | Reescrita | Delta |",
        "|---|---:|---:|---:|",
    ]
    for k in k_list:
        key = f"top_{k}_accuracy"
        lines.append(f"| Top-{k} accuracy | {original[key]:.4f} | {rewritten[key]:.4f} | {rewritten[key] - original[key]:+.4f} |")
    lines.append(f"| MRR | {original['mrr']:.4f} | {rewritten['mrr']:.4f} | {rewritten['mrr'] - original['mrr']:+.4f} |")
    lines.extend(
        [
            "",
            "## Comparacion por caso",
            "",
            f"- Casos ganados: {comparison['ganados']}.",
            f"- Casos perdidos: {comparison['perdidos']}.",
            f"- Casos sin cambio: {comparison['sin_cambio']}.",
            f"- Casos sin consulta reescrita usable: {comparison['empty_rewrite_cases']}.",
            f"- Profundidad usada para rank/MRR: {metrics['bm25_config']['retrieval_depth']}.",
            f"- Corte principal para ganado/perdido: Top-{max_k}.",
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
    rewrites_path = resolve_project_path(args.rewrites, base_dir=base_dir)
    output_dir = resolve_project_path(args.output_dir, base_dir=base_dir)
    index_path = resolve_project_path(
        args.index or paths.get("bm25_index_path", "data/processed/indexes/bm25_nandina8.pkl"),
        base_dir=base_dir,
    )
    k_list = _parse_k_list(args.k_list, bm25_cfg.get("k_list") or DEFAULT_K_LIST)
    max_k = max(k_list)
    retrieval_depth = args.retrieval_depth or int(bm25_cfg.get("top_n", max_k))
    retrieval_depth = max(retrieval_depth, max_k)

    dev_rows = _read_csv(devset_path)
    rewrite_rows = _read_jsonl(rewrites_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")
    if len(rewrite_rows) != len(dev_rows):
        raise ValueError(f"Rewrite row count is {len(rewrite_rows)}, expected {len(dev_rows)}.")

    index = load_bm25_index(index_path)
    result_rows: list[dict[str, Any]] = []
    start = time.time()

    for position, (dev_row, rewrite_row) in enumerate(zip(dev_rows, rewrite_rows), start=1):
        descripcion = _clean(dev_row.get("descripcion"))
        nandina_ref = _clean(dev_row.get("nandina"))
        consulta_reescrita = _clean(rewrite_row.get("consulta_reescrita"))
        original_hits = retrieve(index, descripcion, top_n=retrieval_depth)
        rewritten_hits = retrieve(index, consulta_reescrita, top_n=retrieval_depth) if consulta_reescrita else []
        original_rank = rank_of_true(original_hits, nandina_ref)
        rewritten_rank = rank_of_true(rewritten_hits, nandina_ref)
        outcome = _case_outcome(original_rank, rewritten_rank, max_k=max_k)
        row: dict[str, Any] = {
            "case_id": _clean(rewrite_row.get("case_id")) or f"dev-{position:02d}",
            "descripcion": descripcion,
            "consulta_reescrita": consulta_reescrita,
            "nandina_ref": nandina_ref,
            "original_rank": original_rank,
            "rewritten_rank": rewritten_rank,
            "delta_rank": _delta_rank(original_rank, rewritten_rank, missing_rank=retrieval_depth + 1),
            "outcome": outcome,
            "original_retrieved_count": len(original_hits),
            "rewritten_retrieved_count": len(rewritten_hits),
            "rewrite_json_valid": int(rewrite_row.get("json_valid", 0)),
            "rewrite_code_violation": int(rewrite_row.get("code_violation", 0)),
            "rewrite_forbidden_term_violation": int(rewrite_row.get("forbidden_term_violation", 0)),
            "rewrite_warnings": "; ".join(str(item) for item in rewrite_row.get("warnings", [])),
        }
        for k in k_list:
            row[f"original_hit_top_{k}"] = int(acc_at_k(original_rank, k))
            row[f"rewritten_hit_top_{k}"] = int(acc_at_k(rewritten_rank, k))
        _add_candidates(row, "original_candidate", original_hits, max_k)
        _add_candidates(row, "rewritten_candidate", rewritten_hits, max_k)
        result_rows.append(row)

    original_ranks = [int(row["original_rank"]) for row in result_rows]
    rewritten_ranks = [int(row["rewritten_rank"]) for row in result_rows]
    comparison = {
        "ganados": sum(1 for row in result_rows if row["outcome"] == "ganado"),
        "perdidos": sum(1 for row in result_rows if row["outcome"] == "perdido"),
        "sin_cambio": sum(1 for row in result_rows if row["outcome"] == "sin_cambio"),
        "empty_rewrite_cases": sum(1 for row in result_rows if not _clean(row["consulta_reescrita"])),
        "json_invalid_cases": sum(1 for row in result_rows if not int(row["rewrite_json_valid"])),
        "code_violation_cases": sum(int(row["rewrite_code_violation"]) for row in result_rows),
        "forbidden_term_cases": sum(int(row["rewrite_forbidden_term_violation"]) for row in result_rows),
    }
    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_rewrite_devset",
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
            "rewrites_path": _report_path(rewrites_path, root),
            "rewrites_abs_path": str(rewrites_path),
            "rewrites_sha256": sha256_file(rewrites_path),
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
            "docs_indexed": len(index.doc_ids),
            "avgdl": getattr(index, "avgdl", None),
            "vocab_size": len(getattr(index, "idf", {})),
        },
        "original_metrics": _metrics_from_ranks(original_ranks, k_list, max_k),
        "rewritten_metrics": _metrics_from_ranks(rewritten_ranks, k_list, max_k),
        "comparison": comparison,
        "warnings": [
            "Devset-only diagnostic; do not infer final evalset performance.",
            "Ganado/perdido is computed using rank movement within the evaluated Top-K depth.",
        ],
        "output": {
            "output_dir": _report_path(output_dir, root),
            "output_abs_dir": str(output_dir),
            "results_csv": _report_path(output_dir / "bm25_rewrite_results.csv", root),
            "metrics_json": _report_path(output_dir / "bm25_rewrite_metrics.json", root),
            "summary_md": _report_path(output_dir / "bm25_rewrite_summary.md", root),
        },
    }

    fieldnames = [
        "case_id",
        "descripcion",
        "consulta_reescrita",
        "nandina_ref",
        "original_rank",
        "rewritten_rank",
        "delta_rank",
        "outcome",
        "original_retrieved_count",
        "rewritten_retrieved_count",
        "rewrite_json_valid",
        "rewrite_code_violation",
        "rewrite_forbidden_term_violation",
        "rewrite_warnings",
    ]
    for k in k_list:
        fieldnames.extend([f"original_hit_top_{k}", f"rewritten_hit_top_{k}"])
    fieldnames.extend(_candidate_columns("original_candidate", max_k))
    fieldnames.extend(_candidate_columns("rewritten_candidate", max_k))

    _write_csv(output_dir / "bm25_rewrite_results.csv", result_rows, fieldnames)
    _write_json(output_dir / "bm25_rewrite_metrics.json", metrics)
    ensure_parent(output_dir / "bm25_rewrite_summary.md")
    (output_dir / "bm25_rewrite_summary.md").write_text(_summary_markdown(metrics, k_list, max_k), encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate BM25 on original vs LLM-rewritten devset descriptions.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--rewrites", type=Path, default=DEFAULT_REWRITES)
    parser.add_argument("--index", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--k-list", default=None)
    parser.add_argument("--retrieval-depth", type=int, default=None)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    original = metrics["original_metrics"]
    rewritten = metrics["rewritten_metrics"]
    print("OK: evaluacion BM25 original vs reescrito completada")
    print(f"Casos evaluados: {original['cases_total']}")
    for k in metrics["bm25_config"]["evaluated_k"]:
        key = f"top_{k}_accuracy"
        print(f"Top-{k}: original={original[key]:.4f} reescrita={rewritten[key]:.4f}")
    print(f"MRR: original={original['mrr']:.4f} reescrita={rewritten['mrr']:.4f}")
    print(f"Outputs: {metrics['output']['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
