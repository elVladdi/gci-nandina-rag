from __future__ import annotations

import argparse
import csv
import json
import pickle
import platform
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import DEFAULT_STOPWORDS_ES, build_bm25_from_corpus, read_jsonl, sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_DEVSET = Path("data/processed/devset_validacion_intermedia.csv")
DEFAULT_VARIANTS_DIR = Path("data/processed/corpus_ablation_nandina_v0.1")
DEFAULT_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_hierarchy_ablation_devset_v0.1")
DEFAULT_REPORT = Path("docs/evaluacion_bm25_hierarchy_ablation_devset_v0.1.md")
DEFAULT_FLAT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_HIER_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")

EXPECTED_DEVSET_ROWS = 13
K_LIST = [1, 3, 5, 10]
VARIANTS = [
    "A_leaf_only",
    "B_4d_leaf",
    "C_hs6_leaf",
    "D_4d_hs6_leaf",
    "E_4d_hs6_leaf_weighted",
    "F_hs6_leaf_weighted",
    "G_chapter_4d_hs6_leaf_weighted",
]
CRITICAL_CODES = ["39012000", "85414100", "28151100", "02013000", "95030010", "84717000", "63064000"]
SMOKE_TESTS = [
    ("soda_caustica_solida", "soda caustica solida", "28151100"),
    ("ruedas", "ruedas", "83022000"),
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


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _rank_metric(rank: int, depth: int) -> int:
    return rank if rank > 0 else depth + 1


def _outcome(candidate_rank: int, reference_rank: int, depth: int) -> str:
    candidate = _rank_metric(candidate_rank, depth)
    reference = _rank_metric(reference_rank, depth)
    if candidate < reference:
        return "ganado"
    if candidate > reference:
        return "perdido"
    return "sin_cambio"


def _same_prefix_in_top(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int = 10) -> int:
    prefix = true_code[:prefix_len]
    return int(any(_clean(hit.get("code")).startswith(prefix) for hit in hits[:k]))


def _top_codes(hits: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_clean(hit.get("code")) for hit in hits[:limit])


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _method_metrics(rows: Sequence[Mapping[str, Any]], method: str) -> dict[str, Any]:
    ranks = [int(row[f"{method}_rank"]) for row in rows]
    metrics: dict[str, Any] = {
        "cases_total": len(rows),
        "mrr": _mean([mrr_from_rank(rank) for rank in ranks]),
        "recall_at_50": _mean([acc_at_k(rank, 50) for rank in ranks]),
        "recall_at_100": _mean([acc_at_k(rank, 100) for rank in ranks]),
        "top_10_hs4": _mean([float(row[f"{method}_top10_hs4"]) for row in rows]),
        "top_10_hs2": _mean([float(row[f"{method}_top10_hs2"]) for row in rows]),
        "not_found_at_depth": sum(1 for rank in ranks if rank <= 0),
    }
    for k in K_LIST:
        metrics[f"top_{k}"] = _mean([acc_at_k(rank, k) for rank in ranks])
    return metrics


def _comparison(rows: Sequence[Mapping[str, Any]], method: str, reference: str, depth: int) -> dict[str, Any]:
    outcomes = [_outcome(int(row[f"{method}_rank"]), int(row[f"{reference}_rank"]), depth) for row in rows]
    severe = 0
    for row in rows:
        candidate = int(row[f"{method}_rank"])
        ref = int(row[f"{reference}_rank"])
        candidate_metric = _rank_metric(candidate, depth)
        ref_metric = _rank_metric(ref, depth)
        if candidate_metric - ref_metric > 10 or (0 < ref <= 10 and (candidate <= 0 or candidate > 10)):
            severe += 1
    return {
        "ganados": outcomes.count("ganado"),
        "perdidos": outcomes.count("perdido"),
        "sin_cambio": outcomes.count("sin_cambio"),
        "severe_degradations": severe,
    }


def _build_variant_index(
    variant_id: str,
    corpus_path: Path,
    index_path: Path,
    k1: float,
    b: float,
    force_rebuild: bool,
) -> tuple[Any, dict[str, Any]]:
    if index_path.exists() and not force_rebuild:
        return load_bm25_index(index_path), {"rebuilt": False, "index_path": str(index_path)}
    rows = read_jsonl(corpus_path)
    index, stats = build_bm25_from_corpus(
        rows,
        type_field="tipo",
        code_field="codigo",
        title_field="titulo",
        text_field="texto_index_variant",
        fallback_text_field="texto_index_variant",
        target_type="nandina_8",
        k1=k1,
        b=b,
        stopwords=DEFAULT_STOPWORDS_ES,
        enforce_8_digits=True,
    )
    ensure_parent(index_path)
    with index_path.open("wb") as handle:
        pickle.dump(index, handle)
    return index, {"rebuilt": True, "index_path": str(index_path), "index_stats": stats}


def _smoke_rank(index: Any, query: str, expected_code: str, depth: int) -> dict[str, Any]:
    hits = retrieve(index, query, top_n=depth)
    return {
        "query": query,
        "expected_code": expected_code,
        "rank": rank_of_true(hits, expected_code),
        "top_10_codes": [_clean(hit.get("code")) for hit in hits[:10]],
    }


def _critical_preservation(rows: Sequence[Mapping[str, Any]], method: str, depth: int) -> dict[str, Any]:
    preserve_flat_codes = {"39012000", "85414100"}
    preserve_hier_codes = {"28151100", "02013000", "95030010"}
    checks: list[bool] = []
    details: dict[str, Any] = {}
    for row in rows:
        code = _clean(row.get("nandina_ref"))
        method_rank = int(row[f"{method}_rank"])
        if code in preserve_flat_codes:
            flat_rank = int(row["BM25_flat_current_rank"])
            ok = _rank_metric(method_rank, depth) <= _rank_metric(flat_rank, depth)
            checks.append(ok)
            details[code] = {"method_rank": method_rank, "reference": "BM25_flat_current", "reference_rank": flat_rank, "ok": ok}
        if code in preserve_hier_codes:
            hier_rank = int(row["BM25_hierarchical_v0.1_rank"])
            ok = _rank_metric(method_rank, depth) <= _rank_metric(hier_rank, depth)
            checks.append(ok)
            details[code] = {"method_rank": method_rank, "reference": "BM25_hierarchical_v0.1", "reference_rank": hier_rank, "ok": ok}
    return {
        "all_critical_preserved": bool(checks) and all(checks),
        "checks_total": len(checks),
        "checks_passed": sum(1 for item in checks if item),
        "details": details,
    }


def _select_candidate(
    metrics_by_method: Mapping[str, Mapping[str, Any]],
    comparisons: Mapping[str, Any],
    rows: Sequence[Mapping[str, Any]],
    depth: int,
) -> dict[str, Any]:
    flat = metrics_by_method["BM25_flat_current"]
    hierarchical = metrics_by_method["BM25_hierarchical_v0.1"]
    candidates: list[tuple[tuple[float, ...], str]] = []
    preservation: dict[str, Any] = {}
    for variant_id in VARIANTS:
        metrics = metrics_by_method[variant_id]
        cmp_flat = comparisons[variant_id]["vs_BM25_flat_current"]
        cmp_hier = comparisons[variant_id]["vs_BM25_hierarchical_v0.1"]
        preservation[variant_id] = _critical_preservation(rows, variant_id, depth)
        criteria_ok = (
            metrics["top_1"] >= flat["top_1"]
            and (
                metrics["top_10"] > flat["top_10"]
                or metrics["mrr"] > flat["mrr"]
                or metrics["recall_at_100"] > flat["recall_at_100"]
            )
        )
        severe_penalty = cmp_flat["severe_degradations"] + cmp_hier["severe_degradations"]
        score = (
            1.0 if criteria_ok else 0.0,
            -float(severe_penalty),
            metrics["top_1"],
            metrics["top_10"],
            metrics["mrr"],
            metrics["recall_at_100"],
            metrics["top_10_hs4"],
            metrics["top_10_hs2"],
            -abs(metrics["top_10_hs4"] - hierarchical["top_10_hs4"]),
        )
        candidates.append((score, variant_id))
    candidates.sort(reverse=True)
    best_tradeoff = candidates[0][1]
    freeze_candidates = [
        variant_id
        for _score, variant_id in candidates
        if preservation[variant_id]["all_critical_preserved"]
        and metrics_by_method[variant_id]["top_1"] >= flat["top_1"]
        and (
            metrics_by_method[variant_id]["top_10"] > flat["top_10"]
            or metrics_by_method[variant_id]["mrr"] > flat["mrr"]
            or metrics_by_method[variant_id]["recall_at_100"] > flat["recall_at_100"]
        )
    ]
    freeze_candidate = freeze_candidates[0] if freeze_candidates else None
    return {
        "candidate_variant": freeze_candidate,
        "best_tradeoff_variant": best_tradeoff,
        "selection_score": list(candidates[0][0]),
        "critical_preservation": preservation,
        "rationale": (
            "Best trade-off is ordered by Top-1 non-regression, broad metric improvement, severe degradations, Top-10, MRR and Recall. A freeze candidate is declared only if it also preserves the critical flat wins and hierarchical wins."
        ),
    }


def _summary_markdown(metrics: Mapping[str, Any], rank_rows: Sequence[Mapping[str, Any]]) -> str:
    methods = metrics["method_order"]
    selected = metrics["candidate_selection"].get("candidate_variant")
    best_tradeoff = metrics["candidate_selection"].get("best_tradeoff_variant")
    lines = [
        "# Evaluacion BM25 hierarchy ablation devset v0.1",
        "",
        "## Objetivo",
        "",
        "Ejecutar la Fase 6B-2: ablation de composicion jerarquica y ponderacion del texto indexado NANDINA para BM25, usando solo el devset intermedio de 13 casos.",
        "",
        "## Motivacion",
        "",
        "El corpus jerarquico v0.1 mejoro recall y Top-10, pero tambien introdujo ruido de padres generales. Esta ablation separa hoja, 4D, HS6, capitulo y repeticion de hoja para ver que composicion conserva las mejoras sin degradar casos sensibles.",
        "",
        "## Variantes",
        "",
        "- A_leaf_only: solo descripcion NANDINA8.",
        "- B_4d_leaf: partida 4D + NANDINA8.",
        "- C_hs6_leaf: HS6 + NANDINA8; si no hay HS6, solo hoja.",
        "- D_4d_hs6_leaf: 4D + HS6 + NANDINA8.",
        "- E_4d_hs6_leaf_weighted: 4D + HS6 + hoja repetida.",
        "- F_hs6_leaf_weighted: HS6 + hoja repetida.",
        "- G_chapter_4d_hs6_leaf_weighted: capitulo + 4D + HS6 + hoja repetida.",
        "",
        "## Metricas",
        "",
        "| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | Top-10 HS4 | Top-10 HS2 | NF | Sev vs flat | Sev vs hier |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in methods:
        m = metrics["metrics_by_method"][method]
        cmp_flat = metrics["comparisons"].get(method, {}).get("vs_BM25_flat_current", {})
        cmp_hier = metrics["comparisons"].get(method, {}).get("vs_BM25_hierarchical_v0.1", {})
        lines.append(
            f"| {method} | {m['top_1']:.4f} | {m['top_3']:.4f} | {m['top_5']:.4f} | {m['top_10']:.4f} | {m['mrr']:.4f} | {m['recall_at_50']:.4f} | {m['recall_at_100']:.4f} | {m['top_10_hs4']:.4f} | {m['top_10_hs2']:.4f} | {m['not_found_at_depth']} | {cmp_flat.get('severe_degradations', 0)} | {cmp_hier.get('severe_degradations', 0)} |"
        )
    lines.extend(
        [
            "",
            "## Matriz de ranks",
            "",
            "| Caso | NANDINA | " + " | ".join(methods) + " |",
            "|---|---|" + "---:|" * len(methods),
        ]
    )
    for row in rank_rows:
        lines.append("| " + " | ".join([row["case_id"], row["nandina_ref"], *[str(row.get(method, "")) for method in methods]]) + " |")
    lines.extend(
        [
            "",
            "## Casos criticos",
            "",
            "Los casos criticos completos quedan en `ablation_critical_cases.csv`. En esta corrida se rastrearon 39012000, 85414100, 28151100, 02013000, 95030010, 84717000, 63064000 y el smoke test de 83022000 para `ruedas`.",
            "",
            "## Smoke tests",
            "",
            "- `soda caustica solida`: revisar `ablation_smoke_tests.json` para el rank de 28151100 por metodo.",
            "- `ruedas`: revisar `ablation_smoke_tests.json` para el rank de 83022000 por metodo.",
            "",
            "## Decision metodologica",
            "",
            f"Variante candidata para congelar: `{selected or 'ninguna'}`.",
            f"Mejor trade-off exploratorio: `{best_tradeoff}`.",
            metrics["candidate_selection"]["rationale"],
            "",
            "## Recomendacion",
            "",
            metrics["recommendation"],
            "",
            "## Limitaciones",
            "",
            "- Devset pequeno de 13 casos; no se ejecuto evalset.",
            "- La repeticion de hoja es una ponderacion lexical simple, no un re-ranker.",
            "- No se ejecuto LLM, Text2Trade ni evidencia documental Arancel/RGI/notas.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    devset_path = resolve_project_path(args.devset)
    variants_dir = resolve_project_path(args.variants_dir)
    index_dir = resolve_project_path(args.index_dir)
    output_dir = resolve_project_path(args.output_dir)
    report_path = resolve_project_path(args.report)
    flat_index_path = resolve_project_path(args.flat_index)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    depth = args.retrieval_depth

    dev_rows = _read_csv(devset_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")

    start = time.time()
    methods: dict[str, Any] = {
        "BM25_flat_current": load_bm25_index(flat_index_path),
        "BM25_hierarchical_v0.1": load_bm25_index(hierarchical_index_path),
    }
    index_metadata: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_hierarchy_ablation_devset",
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "bm25_params": {
            "k1": args.k1,
            "b": args.b,
            "stopwords_source": "src.bm25_index.DEFAULT_STOPWORDS_ES",
            "text_field": "texto_index_variant",
            "code_field": "codigo",
            "type": "nandina_8",
        },
        "variant_indexes": {},
    }
    for variant_id in VARIANTS:
        corpus_path = variants_dir / f"{variant_id}.jsonl"
        index_path = index_dir / f"{variant_id}.pkl"
        index, build_info = _build_variant_index(
            variant_id,
            corpus_path,
            index_path,
            k1=args.k1,
            b=args.b,
            force_rebuild=args.force_rebuild,
        )
        methods[variant_id] = index
        index_metadata["variant_indexes"][variant_id] = {
            **build_info,
            "corpus_path": _rel(corpus_path, root),
            "corpus_sha256": sha256_file(corpus_path),
            "index_path": _rel(index_path, root),
            "index_sha256": sha256_file(index_path),
        }
    ensure_parent(index_dir / "ablation_index_metadata.json")
    _write_json(index_dir / "ablation_index_metadata.json", index_metadata)

    method_order = ["BM25_flat_current", "BM25_hierarchical_v0.1", *VARIANTS]
    case_rows: list[dict[str, Any]] = []
    for position, dev_row in enumerate(dev_rows, start=1):
        descripcion = _clean(dev_row.get("descripcion"))
        true_code = _clean(dev_row.get("nandina") or dev_row.get("nandina_ref"))
        row: dict[str, Any] = {
            "case_id": f"dev-{position:02d}",
            "descripcion": descripcion,
            "nandina_ref": true_code,
            "hs4_ref": true_code[:4],
            "hs2_ref": true_code[:2],
        }
        for method, index in methods.items():
            hits = retrieve(index, descripcion, top_n=depth)
            rank = rank_of_true(hits, true_code)
            row[f"{method}_rank"] = rank
            row[f"{method}_top10_hs4"] = _same_prefix_in_top(hits, true_code, 4)
            row[f"{method}_top10_hs2"] = _same_prefix_in_top(hits, true_code, 2)
            row[f"{method}_top10_codes"] = _top_codes(hits)
        case_rows.append(row)

    metrics_by_method = {method: _method_metrics(case_rows, method) for method in method_order}
    comparisons: dict[str, Any] = {}
    for method in method_order:
        comparisons[method] = {
            "vs_BM25_flat_current": _comparison(case_rows, method, "BM25_flat_current", depth),
            "vs_BM25_hierarchical_v0.1": _comparison(case_rows, method, "BM25_hierarchical_v0.1", depth),
        }

    rank_rows: list[dict[str, Any]] = []
    for row in case_rows:
        rank_rows.append(
            {
                "case_id": row["case_id"],
                "descripcion": row["descripcion"],
                "nandina_ref": row["nandina_ref"],
                **{method: row[f"{method}_rank"] for method in method_order},
            }
        )

    critical_rows: list[dict[str, Any]] = []
    for row in case_rows:
        if row["nandina_ref"] in CRITICAL_CODES:
            critical_rows.append(
                {
                    "case_id": row["case_id"],
                    "descripcion": row["descripcion"],
                    "nandina_ref": row["nandina_ref"],
                    **{method: row[f"{method}_rank"] for method in method_order},
                    **{f"{method}_top10_codes": row[f"{method}_top10_codes"] for method in method_order},
                }
            )

    smoke_tests: dict[str, Any] = {}
    for smoke_id, query, expected_code in SMOKE_TESTS:
        smoke_tests[smoke_id] = {
            method: _smoke_rank(index, query, expected_code, depth)
            for method, index in methods.items()
        }

    candidate_selection = _select_candidate(metrics_by_method, comparisons, case_rows, depth)
    selected = candidate_selection["candidate_variant"]
    best_tradeoff = candidate_selection["best_tradeoff_variant"]
    selected_for_thresholds = selected or best_tradeoff
    selected_metrics = metrics_by_method[selected_for_thresholds]
    flat_metrics = metrics_by_method["BM25_flat_current"]
    hierarchical_metrics = metrics_by_method["BM25_hierarchical_v0.1"]
    if selected and (
        selected_metrics["top_1"] >= flat_metrics["top_1"]
        and selected_metrics["top_10"] >= flat_metrics["top_10"]
        and selected_metrics["recall_at_100"] >= flat_metrics["recall_at_100"]
        and comparisons[selected]["vs_BM25_hierarchical_v0.1"]["severe_degradations"]
        <= comparisons["BM25_hierarchical_v0.1"]["vs_BM25_flat_current"]["severe_degradations"]
    ):
        recommendation = (
            f"No ejecutar evalset aun automaticamente, pero preparar `{selected_for_thresholds}` como candidata para una subfase de confirmacion: empata o mejora metricas clave frente al plano y controla degradaciones frente al jerarquico."
        )
    else:
        recommendation = (
            "No escalar al evalset todavia. Ninguna variante domina claramente bajo todos los criterios; conviene una siguiente iteracion hibrida o de ponderacion mas fina."
        )

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_hierarchy_ablation_devset",
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
            "devset_path": _rel(devset_path, root),
            "devset_sha256": sha256_file(devset_path),
            "variants_dir": _rel(variants_dir, root),
            "flat_index_path": _rel(flat_index_path, root),
            "flat_index_sha256": sha256_file(flat_index_path),
            "hierarchical_index_path": _rel(hierarchical_index_path, root),
            "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
        },
        "bm25_config": {
            "k1": args.k1,
            "b": args.b,
            "retrieval_depth": depth,
            "k_list": K_LIST,
            "stopwords_count": len(DEFAULT_STOPWORDS_ES),
        },
        "method_order": method_order,
        "metrics_by_method": metrics_by_method,
        "comparisons": comparisons,
        "candidate_selection": candidate_selection,
        "recommendation": recommendation,
        "outputs": {
            "ablation_metrics_json": _rel(output_dir / "ablation_metrics.json", root),
            "ablation_summary_md": _rel(output_dir / "ablation_summary.md", root),
            "ablation_case_comparison_13_cases_csv": _rel(output_dir / "ablation_case_comparison_13_cases.csv", root),
            "ablation_critical_cases_csv": _rel(output_dir / "ablation_critical_cases.csv", root),
            "ablation_rank_matrix_csv": _rel(output_dir / "ablation_rank_matrix.csv", root),
            "ablation_smoke_tests_json": _rel(output_dir / "ablation_smoke_tests.json", root),
            "report_md": _rel(report_path, root),
        },
        "warnings": [
            "Only devset was evaluated; evalset was not read or executed.",
            "No LLM or Text2Trade execution is part of this script.",
        ],
    }

    case_fields = ["case_id", "descripcion", "nandina_ref", "hs4_ref", "hs2_ref"]
    for method in method_order:
        case_fields.extend([f"{method}_rank", f"{method}_top10_hs4", f"{method}_top10_hs2", f"{method}_top10_codes"])
    _write_csv(output_dir / "ablation_case_comparison_13_cases.csv", case_rows, case_fields)
    _write_csv(output_dir / "ablation_rank_matrix.csv", rank_rows, ["case_id", "descripcion", "nandina_ref", *method_order])
    critical_fields = ["case_id", "descripcion", "nandina_ref", *method_order, *[f"{method}_top10_codes" for method in method_order]]
    _write_csv(output_dir / "ablation_critical_cases.csv", critical_rows, critical_fields)
    _write_json(output_dir / "ablation_metrics.json", metrics)
    _write_json(output_dir / "ablation_smoke_tests.json", smoke_tests)
    summary = _summary_markdown(metrics, rank_rows)
    ensure_parent(output_dir / "ablation_summary.md")
    (output_dir / "ablation_summary.md").write_text(summary, encoding="utf-8")
    ensure_parent(report_path)
    report_path.write_text(summary, encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate BM25 hierarchy ablation variants on devset only.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--variants-dir", type=Path, default=DEFAULT_VARIANTS_DIR)
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--flat-index", type=Path, default=DEFAULT_FLAT_INDEX)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIER_INDEX)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    parser.add_argument("--k1", type=float, default=1.5)
    parser.add_argument("--b", type=float, default=0.75)
    parser.add_argument("--force-rebuild", action="store_true")
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion ablation BM25 devset completada")
    print(f"Metodos: {', '.join(metrics['method_order'])}")
    print(f"Candidata: {metrics['candidate_selection']['candidate_variant']}")
    for method in metrics["method_order"]:
        m = metrics["metrics_by_method"][method]
        print(f"{method}: top1={m['top_1']:.4f} top10={m['top_10']:.4f} mrr={m['mrr']:.4f} r100={m['recall_at_100']:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
