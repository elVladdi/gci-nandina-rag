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
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_FLAT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_FIELDED_INDEX = Path("data/processed/indexes/bm25_nandina8_fielded_v0.1.pkl")
DEFAULT_EXPANDED_INDEX = Path("data/processed/indexes/bm25_nandina8_fielded_expanded_v0.1.pkl")
DEFAULT_ABLATION_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_fielded_evalset_v0.1")
DEFAULT_REPORT = Path("docs/evaluacion_bm25_fielded_evalset_v0.1.md")

EXPECTED_EVALSET_ROWS = 600
K_LIST = [1, 3, 5, 10]
BM25_METHODS = (
    "BM25_flat_current",
    "BM25_hierarchical_v0.1",
    "BM25_fielded_weighted_v0.1",
    "BM25_fielded_weighted_expanded_v0.1",
)
POOL_METHOD = "phase7a_pool_hierarchical_80_dual_backfill_20"
METHODS = (*BM25_METHODS, POOL_METHOD)
CRITICAL_CODES = {"28151100", "84713000", "84717000", "39012000", "85414100", "83022000"}
CRITICAL_KEYWORDS = (
    "soda caustica",
    "sosa caustica",
    "hidroxido de sodio",
    "computadora portatil",
    "laptop",
    "notebook",
    "ssd",
    "disco solido",
    "polietileno",
    "led",
    "diodo emisor de luz",
    "patinete",
    "scooter",
    "ruedas",
)
PRECISION_VARIANT = "C_hs6_leaf"
RECALL_VARIANT = "D_4d_hs6_leaf"
DUAL_PROTECTED_TOP_N = 5
PHASE7A_BASE = 80


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


def _rank_metric(rank: int, depth: int) -> int:
    return rank if rank > 0 else depth + 1


def _case_outcome(base_rank: int, method_rank: int, depth: int) -> str:
    base_metric = _rank_metric(base_rank, depth)
    method_metric = _rank_metric(method_rank, depth)
    if method_metric < base_metric:
        return "ganado"
    if method_metric > base_metric:
        return "perdido"
    return "sin_cambio"


def _code_from_hit(hit: Mapping[str, Any]) -> str:
    return _clean(hit.get("code"))


def _renumber(hits: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for rank, hit in enumerate(hits[:depth], start=1):
        item = dict(hit)
        item["rank"] = rank
        output.append(item)
    return output


def _dedupe_append(target: list[dict[str, Any]], seen: set[str], hits: Sequence[Mapping[str, Any]], limit: int | None = None) -> None:
    iterable = hits if limit is None else hits[:limit]
    for hit in iterable:
        code = _code_from_hit(hit)
        if code and code not in seen:
            seen.add(code)
            target.append(dict(hit))


def _protected_top_5_backfill(
    precision_hits: Sequence[Mapping[str, Any]],
    recall_hits: Sequence[Mapping[str, Any]],
    depth: int,
) -> list[dict[str, Any]]:
    fused: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(fused, seen, precision_hits, limit=DUAL_PROTECTED_TOP_N)
    _dedupe_append(fused, seen, recall_hits)
    _dedupe_append(fused, seen, precision_hits[DUAL_PROTECTED_TOP_N:])
    return _renumber(fused, depth)


def _phase7a_pool(
    hierarchical_hits: Sequence[Mapping[str, Any]],
    dual_hits: Sequence[Mapping[str, Any]],
    depth: int,
) -> list[dict[str, Any]]:
    pool: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(pool, seen, hierarchical_hits, limit=min(PHASE7A_BASE, depth))
    _dedupe_append(pool, seen, dual_hits, limit=depth)
    if len(pool) < depth:
        _dedupe_append(pool, seen, hierarchical_hits[PHASE7A_BASE:])
    return _renumber(pool, depth)


def _family_hit(candidates: Sequence[Mapping[str, Any]], true_code: str, family_len: int, k: int) -> int:
    prefix = _clean(true_code)[:family_len]
    if not prefix:
        return 0
    return int(any(_code_from_hit(hit).startswith(prefix) for hit in candidates[:k]))


def _top_codes(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_code_from_hit(hit) for hit in candidates[:limit])


def _compact_top(candidates: Sequence[Mapping[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for hit in candidates[:limit]:
        rows.append(
            {
                "rank": int(hit.get("rank", len(rows) + 1)),
                "code": _code_from_hit(hit),
                "score": float(hit.get("score", 0.0)),
                "text": _clean(hit.get("text")),
            }
        )
    return rows


def _is_critical_case(description: str, true_code: str) -> int:
    lowered = description.lower()
    return int(true_code in CRITICAL_CODES or any(keyword in lowered for keyword in CRITICAL_KEYWORDS))


def _metrics_for_method(rows: Sequence[Mapping[str, Any]], method: str, *, depth: int) -> dict[str, Any]:
    ranks = [int(row[f"rank_{method}"]) for row in rows]
    metrics: dict[str, Any] = {
        "cases_total": len(rows),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "recall_at_50": _mean([acc_at_k(rank, 50) for rank in ranks]),
        "recall_at_100": _mean([acc_at_k(rank, 100) for rank in ranks]),
        "hs4_at_10": _mean([int(row[f"{method}_hs4_at_10"]) for row in rows]),
        "hs2_at_10": _mean([int(row[f"{method}_hs2_at_10"]) for row in rows]),
        "not_found_at_depth": sum(1 for rank in ranks if rank <= 0),
        "depth": depth,
    }
    for k in K_LIST:
        metrics[f"top_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
    return metrics


def _comparison_vs_hierarchical(rows: Sequence[Mapping[str, Any]], method: str, depth: int) -> dict[str, int]:
    base = "BM25_hierarchical_v0.1"
    return {
        "ganados": sum(
            1 for row in rows if _case_outcome(int(row[f"rank_{base}"]), int(row[f"rank_{method}"]), depth) == "ganado"
        ),
        "perdidos": sum(
            1 for row in rows if _case_outcome(int(row[f"rank_{base}"]), int(row[f"rank_{method}"]), depth) == "perdido"
        ),
        "sin_cambio": sum(
            1
            for row in rows
            if _case_outcome(int(row[f"rank_{base}"]), int(row[f"rank_{method}"]), depth) == "sin_cambio"
        ),
        "new_cases_hierarchical_not_found_method_found": sum(
            1 for row in rows if int(row[f"rank_{base}"]) <= 0 and int(row[f"rank_{method}"]) > 0
        ),
        "degraded_cases_hierarchical_found_method_lost": sum(
            1 for row in rows if int(row[f"rank_{base}"]) > 0 and int(row[f"rank_{method}"]) <= 0
        ),
        "degraded_cases_any_rank_worse": sum(
            1
            for row in rows
            if _rank_metric(int(row[f"rank_{method}"]), depth) > _rank_metric(int(row[f"rank_{base}"]), depth)
        ),
    }


def _short(value: object, limit: int = 100) -> str:
    text = _clean(value).replace("|", "/")
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def _row(cells: Sequence[Any]) -> str:
    return "| " + " | ".join(_short(cell, 120) for cell in cells) + " |"


def _summary_markdown(metrics: Mapping[str, Any], case_rows: Sequence[Mapping[str, Any]], critical_rows: Sequence[Mapping[str, Any]]) -> str:
    methods = metrics["methods"]
    comparison = metrics["comparison_vs_hierarchical"]
    decision = metrics["interpretation"]
    lines = [
        "# Evaluacion BM25 fielded evalset v0.1",
        "",
        "## Alcance",
        "",
        "Validacion en evalset final de la variante congelada `BM25_fielded_weighted_expanded_v0.1`. La variante fue seleccionada usando devset en Fase 7A-3; el diccionario de expansion y los pesos quedaron congelados antes de mirar el evalset.",
        "",
        "El evalset se ejecuto una sola vez en esta fase. Cualquier mejora o caida se interpreta como validacion externa preliminar, no como ajuste posterior.",
        "",
        "## Controles",
        "",
        "- La expansion controlada se aplica al corpus y no usa codigos como terminos buscables.",
        "- El pool Fase 7A se reporta separado como pool auxiliar, no como ranking BM25 puro.",
        "",
        "## Metricas comparativas",
        "",
        "| Metodo | Tipo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4@10 | HS2@10 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in METHODS:
        data = methods[method]
        method_type = "pool auxiliar" if method == POOL_METHOD else "ranking BM25"
        lines.append(
            f"| {method} | {method_type} | {data['top_1']:.4f} | {data['top_3']:.4f} | {data['top_5']:.4f} | "
            f"{data['top_10']:.4f} | {data['mrr']:.4f} | {data['recall_at_50']:.4f} | "
            f"{data['recall_at_100']:.4f} | {data['hs4_at_10']:.4f} | {data['hs2_at_10']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Comparacion contra BM25_hierarchical_v0.1",
            "",
            "| Metodo | Ganados | Perdidos | Sin cambio | Nuevos recuperados | Perdidos exactos | Casos peor rank |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for method, data in comparison.items():
        lines.append(
            f"| {method} | {data['ganados']} | {data['perdidos']} | {data['sin_cambio']} | "
            f"{data['new_cases_hierarchical_not_found_method_found']} | "
            f"{data['degraded_cases_hierarchical_found_method_lost']} | {data['degraded_cases_any_rank_worse']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretacion",
            "",
            decision["summary"],
            "",
            f"- Delta Top-10 expanded vs hierarchical: {decision['expanded_top10_delta']:+.4f}.",
            f"- Delta MRR expanded vs hierarchical: {decision['expanded_mrr_delta']:+.4f}.",
            f"- Delta Recall@100 expanded vs hierarchical: {decision['expanded_recall100_delta']:+.4f}.",
            "",
            "Separacion de efectos:",
            "",
            f"- Mejora de ranking: Top-10 {decision['expanded_top10_delta']:+.4f}; MRR {decision['expanded_mrr_delta']:+.4f}.",
            f"- Mejora de cobertura amplia: Recall@100 {decision['expanded_recall100_delta']:+.4f}.",
            "",
            "## Casos criticos",
            "",
            "| Caso | NANDINA | Rank hierarchical | Rank expanded | Top10 expanded |",
            "|---|---|---:|---:|---|",
        ]
    )
    for item in critical_rows[:40]:
        lines.append(
            _row(
                [
                    item["case_id"],
                    item["nandina_ref"],
                    item["rank_BM25_hierarchical_v0.1"],
                    item["rank_BM25_fielded_weighted_expanded_v0.1"],
                    item["top10_codes_BM25_fielded_weighted_expanded_v0.1"],
                ]
            )
        )
    lines.extend(
        [
            "",
            "## Limitaciones",
            "",
            "- Validacion externa preliminar: no habilita ajuste posterior del diccionario ni de pesos con base en evalset.",
            "- La expansion controlada puede beneficiar familias lexicales cubiertas y no necesariamente generaliza a todos los capitulos.",
            "- Las metricas miden recuperacion y ranking documental, no clasificacion oficial ni validacion legal.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    evalset_path = resolve_project_path(args.evalset)
    flat_index_path = resolve_project_path(args.flat_index)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    fielded_index_path = resolve_project_path(args.fielded_index)
    expanded_index_path = resolve_project_path(args.expanded_index)
    ablation_index_dir = resolve_project_path(args.ablation_index_dir)
    output_dir = resolve_project_path(args.output_dir)
    report_path = resolve_project_path(args.report)
    depth = args.retrieval_depth

    eval_rows = _read_csv(evalset_path)
    if len(eval_rows) != EXPECTED_EVALSET_ROWS:
        raise ValueError(f"Evalset row count is {len(eval_rows)}, expected {EXPECTED_EVALSET_ROWS}.")

    flat_index = load_bm25_index(flat_index_path)
    hierarchical_index = load_bm25_index(hierarchical_index_path)
    fielded_index = load_bm25_index(fielded_index_path)
    expanded_index = load_bm25_index(expanded_index_path)
    precision_index = load_bm25_index(ablation_index_dir / f"{PRECISION_VARIANT}.pkl")
    recall_index = load_bm25_index(ablation_index_dir / f"{RECALL_VARIANT}.pkl")

    start = time.time()
    case_rows: list[dict[str, Any]] = []
    for position, eval_row in enumerate(eval_rows, start=1):
        case_id = _clean(eval_row.get("case_id")) or f"eval-{position:04d}"
        description = _clean(eval_row.get("descripcion"))
        true_code = _clean(eval_row.get("nandina_ref") or eval_row.get("nandina"))

        flat_hits = retrieve(flat_index, description, top_n=depth)
        hierarchical_hits = retrieve(hierarchical_index, description, top_n=depth)
        fielded_hits = retrieve(fielded_index, description, top_n=depth)
        expanded_hits = retrieve(expanded_index, description, top_n=depth)
        precision_hits = retrieve(precision_index, description, top_n=depth)
        recall_hits = retrieve(recall_index, description, top_n=depth)
        dual_hits = _protected_top_5_backfill(precision_hits, recall_hits, depth)
        pool_hits = _phase7a_pool(hierarchical_hits, dual_hits, depth)

        method_candidates = {
            "BM25_flat_current": flat_hits,
            "BM25_hierarchical_v0.1": hierarchical_hits,
            "BM25_fielded_weighted_v0.1": fielded_hits,
            "BM25_fielded_weighted_expanded_v0.1": expanded_hits,
            POOL_METHOD: pool_hits,
        }
        row: dict[str, Any] = {
            "case_id": case_id,
            "descripcion": description,
            "nandina_ref": true_code,
            "regimen": _clean(eval_row.get("regimen")),
            "capitulo": _clean(eval_row.get("capitulo")),
            "partida": _clean(eval_row.get("partida")),
            "hs4_ref": true_code[:4],
            "hs2_ref": true_code[:2],
            "is_critical_case": _is_critical_case(description, true_code),
        }
        for method, candidates in method_candidates.items():
            rank = rank_of_true(candidates, true_code)
            row[f"rank_{method}"] = rank
            row[f"{method}_hs4_at_10"] = _family_hit(candidates, true_code, 4, 10)
            row[f"{method}_hs2_at_10"] = _family_hit(candidates, true_code, 2, 10)
            row[f"top10_codes_{method}"] = _top_codes(candidates)
            row[f"top10_json_{method}"] = json.dumps(_compact_top(candidates), ensure_ascii=False)
        for method in METHODS:
            if method != "BM25_hierarchical_v0.1":
                row[f"outcome_vs_hierarchical_{method}"] = _case_outcome(
                    int(row["rank_BM25_hierarchical_v0.1"]), int(row[f"rank_{method}"]), depth
                )
        case_rows.append(row)

    critical_rows = [row for row in case_rows if int(row["is_critical_case"])]
    methods = {method: _metrics_for_method(case_rows, method, depth=depth) for method in METHODS}
    comparison = {
        method: _comparison_vs_hierarchical(case_rows, method, depth)
        for method in METHODS
        if method != "BM25_hierarchical_v0.1"
    }
    hierarchical = methods["BM25_hierarchical_v0.1"]
    expanded = methods["BM25_fielded_weighted_expanded_v0.1"]
    top10_delta = expanded["top_10"] - hierarchical["top_10"]
    mrr_delta = expanded["mrr"] - hierarchical["mrr"]
    recall100_delta = expanded["recall_at_100"] - hierarchical["recall_at_100"]
    if top10_delta > 0 or mrr_delta > 0:
        summary = (
            "`BM25_fielded_weighted_expanded_v0.1` mejora metricas de ranking frente al jerarquico en evalset. "
            "El efecto se reporta como validacion externa preliminar de la variante congelada, sin ajuste posterior."
        )
    elif recall100_delta > 0:
        summary = (
            "`BM25_fielded_weighted_expanded_v0.1` solo mejora cobertura amplia frente al jerarquico en evalset; "
            "no mejora ranking temprano porque Top-10/MRR caen. El efecto no justifica reemplazar el ranking base."
        )
    else:
        summary = (
            "`BM25_fielded_weighted_expanded_v0.1` no mejora al ranking jerarquico en evalset; la ganancia del devset "
            "debe tratarse como probable sobreajuste del diccionario manual."
        )

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_fielded_evalset",
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
            "evalset_sha256": sha256_file(evalset_path),
            "flat_index_path": _rel(flat_index_path, root),
            "flat_index_sha256": sha256_file(flat_index_path),
            "hierarchical_index_path": _rel(hierarchical_index_path, root),
            "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
            "fielded_index_path": _rel(fielded_index_path, root),
            "fielded_index_sha256": sha256_file(fielded_index_path),
            "fielded_expanded_index_path": _rel(expanded_index_path, root),
            "fielded_expanded_index_sha256": sha256_file(expanded_index_path),
        },
        "method_types": {
            "BM25_flat_current": "ranking_bm25",
            "BM25_hierarchical_v0.1": "ranking_bm25",
            "BM25_fielded_weighted_v0.1": "ranking_bm25",
            "BM25_fielded_weighted_expanded_v0.1": "ranking_bm25",
            POOL_METHOD: "auxiliary_pool",
        },
        "selection_protocol": {
            "variant_selected_on": "devset",
            "evalset_runs_in_this_phase": 1,
            "frozen_variant": "BM25_fielded_weighted_expanded_v0.1",
            "post_evalset_tuning": False,
        },
        "retrieval": {"retrieval_depth": depth, "k_list": K_LIST},
        "methods": methods,
        "comparison_vs_hierarchical": comparison,
        "interpretation": {
            "summary": summary,
            "expanded_top10_delta": top10_delta,
            "expanded_mrr_delta": mrr_delta,
            "expanded_recall100_delta": recall100_delta,
        },
        "validations": {
            "evalset_rows": len(case_rows),
            "expected_evalset_rows": EXPECTED_EVALSET_ROWS,
            "case_comparison_rows": len(case_rows),
            "critical_case_rows": len(critical_rows),
            "evalset_executed_once": True,
            "post_evalset_tuning": False,
        },
        "outputs": {
            "fielded_evalset_results_csv": _rel(output_dir / "fielded_evalset_results.csv", root),
            "fielded_evalset_metrics_json": _rel(output_dir / "fielded_evalset_metrics.json", root),
            "fielded_evalset_summary_md": _rel(output_dir / "fielded_evalset_summary.md", root),
            "fielded_evalset_case_comparison_csv": _rel(output_dir / "fielded_evalset_case_comparison.csv", root),
            "fielded_evalset_critical_cases_csv": _rel(output_dir / "fielded_evalset_critical_cases.csv", root),
            "report_md": _rel(report_path, root),
        },
    }

    base_fields = [
        "case_id",
        "descripcion",
        "nandina_ref",
        "regimen",
        "capitulo",
        "partida",
        "hs4_ref",
        "hs2_ref",
        "is_critical_case",
    ]
    method_fields: list[str] = []
    for method in METHODS:
        method_fields.extend(
            [
                f"rank_{method}",
                f"{method}_hs4_at_10",
                f"{method}_hs2_at_10",
                f"top10_codes_{method}",
                f"top10_json_{method}",
            ]
        )
    outcome_fields = [f"outcome_vs_hierarchical_{method}" for method in METHODS if method != "BM25_hierarchical_v0.1"]
    all_fields = base_fields + method_fields + outcome_fields
    comparison_fields = base_fields + [field for field in all_fields if field.startswith("rank_") or field.startswith("outcome_")]

    _write_csv(output_dir / "fielded_evalset_results.csv", case_rows, all_fields)
    _write_csv(output_dir / "fielded_evalset_case_comparison.csv", case_rows, comparison_fields)
    _write_csv(output_dir / "fielded_evalset_critical_cases.csv", critical_rows, all_fields)
    _write_json(output_dir / "fielded_evalset_metrics.json", metrics)
    summary = _summary_markdown(metrics, case_rows, critical_rows)
    ensure_parent(output_dir / "fielded_evalset_summary.md")
    (output_dir / "fielded_evalset_summary.md").write_text(summary, encoding="utf-8")
    ensure_parent(report_path)
    report_path.write_text(summary, encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate frozen fielded BM25 variants on evalset.")
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--flat-index", type=Path, default=DEFAULT_FLAT_INDEX)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--fielded-index", type=Path, default=DEFAULT_FIELDED_INDEX)
    parser.add_argument("--expanded-index", type=Path, default=DEFAULT_EXPANDED_INDEX)
    parser.add_argument("--ablation-index-dir", type=Path, default=DEFAULT_ABLATION_INDEX_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion BM25 fielded evalset completada")
    print(f"Casos evaluados: {metrics['validations']['evalset_rows']}")
    for method in METHODS:
        data = metrics["methods"][method]
        print(
            f"{method}: top10={data['top_10']:.4f} mrr={data['mrr']:.4f} "
            f"recall50={data['recall_at_50']:.4f} recall100={data['recall_at_100']:.4f}"
        )
    print(metrics["interpretation"]["summary"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
