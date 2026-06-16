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
DEFAULT_FLAT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_HIER_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_VARIANTS_DIR = Path("data/processed/corpus_ablation_nandina_v0.1")
DEFAULT_ABLATION_INDEX_DIR = Path("data/processed/indexes/bm25_ablation_nandina_v0.1")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_dual_backfill_devset_v0.1")
DEFAULT_REPORT = Path("docs/evaluacion_bm25_dual_backfill_devset_v0.1.md")

EXPECTED_DEVSET_ROWS = 13
K_LIST = [1, 3, 5, 10]
PRECISION_VARIANT = "C_hs6_leaf"
RECALL_VARIANT = "D_4d_hs6_leaf"
CRITICAL_CODES = ["39012000", "85414100", "28151100", "02013000", "95030010"]
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


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _ensure_variant_index(
    variant_id: str,
    variants_dir: Path,
    index_dir: Path,
    k1: float,
    b: float,
    force_rebuild: bool,
) -> Any:
    index_path = index_dir / f"{variant_id}.pkl"
    if index_path.exists() and not force_rebuild:
        return load_bm25_index(index_path)

    corpus_path = variants_dir / f"{variant_id}.jsonl"
    rows = read_jsonl(corpus_path)
    index, _stats = build_bm25_from_corpus(
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
    return index


def _dedupe_append(target: list[dict[str, Any]], seen: set[str], hits: Sequence[Mapping[str, Any]], limit: int | None = None) -> None:
    for hit in hits if limit is None else hits[:limit]:
        code = _clean(hit.get("code"))
        if code and code not in seen:
            seen.add(code)
            target.append(dict(hit))


def _renumber(hits: Sequence[Mapping[str, Any]], depth: int) -> list[dict[str, Any]]:
    ranked: list[dict[str, Any]] = []
    for rank, hit in enumerate(hits[:depth], start=1):
        item = dict(hit)
        item["rank"] = rank
        ranked.append(item)
    return ranked


def _precision_then_backfill(
    precision_hits: Sequence[Mapping[str, Any]],
    recall_hits: Sequence[Mapping[str, Any]],
    depth: int,
    precision_top_k: int,
) -> list[dict[str, Any]]:
    fused: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(fused, seen, precision_hits, limit=precision_top_k)
    _dedupe_append(fused, seen, recall_hits)
    _dedupe_append(fused, seen, precision_hits[precision_top_k:])
    return _renumber(fused, depth)


def _protected_top_n_backfill(
    precision_hits: Sequence[Mapping[str, Any]],
    recall_hits: Sequence[Mapping[str, Any]],
    depth: int,
    protected_n: int,
) -> list[dict[str, Any]]:
    fused: list[dict[str, Any]] = []
    seen: set[str] = set()
    _dedupe_append(fused, seen, precision_hits, limit=protected_n)
    _dedupe_append(fused, seen, recall_hits)
    _dedupe_append(fused, seen, precision_hits[protected_n:])
    return _renumber(fused, depth)


def _oracle_backfill_if_precision_misses(
    precision_hits: Sequence[Mapping[str, Any]],
    recall_hits: Sequence[Mapping[str, Any]],
    true_code: str,
    depth: int,
    miss_at: int,
    protected_n: int,
) -> list[dict[str, Any]]:
    precision_rank = rank_of_true(precision_hits, true_code)
    if 0 < precision_rank <= miss_at:
        return _renumber(precision_hits, depth)
    return _protected_top_n_backfill(precision_hits, recall_hits, depth=depth, protected_n=protected_n)


def _same_prefix_in_top(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int = 10) -> int:
    prefix = true_code[:prefix_len]
    return int(any(_clean(hit.get("code")).startswith(prefix) for hit in hits[:k]))


def _top_codes(hits: Sequence[Mapping[str, Any]], limit: int = 10) -> str:
    return " ".join(_clean(hit.get("code")) for hit in hits[:limit])


def _outcome(method_rank: int, reference_rank: int, depth: int) -> str:
    method_value = _rank_metric(method_rank, depth)
    reference_value = _rank_metric(reference_rank, depth)
    if method_value < reference_value:
        return "ganado"
    if method_value > reference_value:
        return "perdido"
    return "sin_cambio"


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
    return {
        "ganados": outcomes.count("ganado"),
        "perdidos": outcomes.count("perdido"),
        "sin_cambio": outcomes.count("sin_cambio"),
    }


def _critical_status(method_rank: int, reference_rank: int, depth: int) -> str:
    outcome = _outcome(method_rank, reference_rank, depth)
    if outcome == "ganado":
        return "mejora"
    if outcome == "perdido":
        return "empeora"
    return "conserva"


def _smoke_rank(index: Any, query: str, expected_code: str, depth: int) -> dict[str, Any]:
    hits = retrieve(index, query, top_n=depth)
    return {
        "query": query,
        "expected_code": expected_code,
        "rank": rank_of_true(hits, expected_code),
        "top_10_codes": [_clean(hit.get("code")) for hit in hits[:10]],
    }


def _classify_strategy(metrics: Mapping[str, Any], comparisons: Mapping[str, Any], critical_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    flat = metrics["metrics_by_method"]["BM25_flat_current"]
    precision = metrics["metrics_by_method"]["C_hs6_leaf"]
    hierarchical = metrics["metrics_by_method"]["BM25_hierarchical_v0.1"]

    best_method = None
    best_score: tuple[float, ...] | None = None
    classifications: dict[str, str] = {}
    for method in metrics["dual_strategy_order"]:
        method_metrics = metrics["metrics_by_method"][method]
        critical_degraded = sum(
            1
            for row in critical_rows
            if _clean(row.get("source")) == "devset" and _clean(row.get(f"{method}_vs_reference")) == "empeora"
        )
        improves_recall = method_metrics["top_10"] > precision["top_10"] or method_metrics["recall_at_100"] > precision["recall_at_100"]
        improves_over_hier = (
            method_metrics["mrr"] > hierarchical["mrr"]
            or method_metrics["top_1"] > hierarchical["top_1"]
            or method_metrics["recall_at_100"] > hierarchical["recall_at_100"]
        )
        if (
            method_metrics["top_1"] >= flat["top_1"]
            and method_metrics["mrr"] >= flat["mrr"]
            and (method_metrics["top_10"] > flat["top_10"] or method_metrics["recall_at_100"] > flat["recall_at_100"])
            and critical_degraded == 0
        ):
            classification = "A. Candidato a congelar"
        elif improves_recall and critical_degraded <= 1:
            classification = "B. Candidato exploratorio"
        elif not improves_recall and not improves_over_hier:
            classification = "C. No candidato"
        else:
            classification = "B. Candidato exploratorio"
        classifications[method] = classification
        score = (
            2.0 if classification.startswith("A.") else 1.0 if classification.startswith("B.") else 0.0,
            -float(critical_degraded),
            method_metrics["top_1"],
            method_metrics["mrr"],
            method_metrics["top_10"],
            method_metrics["recall_at_100"],
            method_metrics["top_10_hs4"],
            method_metrics["top_10_hs2"],
            -float(comparisons[method]["vs_C_hs6_leaf"]["perdidos"]),
        )
        if best_score is None or score > best_score:
            best_score = score
            best_method = method
    return {
        "best_strategy": best_method,
        "best_strategy_score": list(best_score or ()),
        "classifications": classifications,
    }


def _summary_markdown(metrics: Mapping[str, Any], critical_rows: Sequence[Mapping[str, Any]]) -> str:
    methods = metrics["method_order"]
    lines = [
        "# Evaluacion BM25 dual backfill devset v0.1",
        "",
        "## Objetivo",
        "",
        "Evaluar una recuperacion dual defensiva para NANDINA: un indice de precision HS6+NANDINA8 como ranking base y un indice de recall 4D+HS6+NANDINA8 usado como backfill controlado. Esta fase usa solo devset; no se ejecuto evalset, LLM ni Text2Trade.",
        "",
        "## Motivacion",
        "",
        "La ablation 6B-2 mostro que `C_hs6_leaf` mejora Top-1/MRR y protege precision, mientras que las variantes con 4D mejoran recall pero degradan algunos casos. La fusion dual separa esas funciones para que el indice amplio agregue candidatos sin desplazar agresivamente el ranking de precision.",
        "",
        "## Indices usados",
        "",
        "- Precision: `C_hs6_leaf`, campo `texto_index_variant`, corpus de HS6 + NANDINA8.",
        "- Recall: `D_4d_hs6_leaf`, campo `texto_index_variant`, corpus de 4D + HS6 + NANDINA8.",
        "- Referencias: BM25 plano actual y BM25 jerarquico v0.1.",
        "",
        "## Estrategias",
        "",
        "- `precision_then_backfill_k10`: conserva Top-10 de precision y agrega candidatos nuevos de recall despues.",
        "- `protected_top_5_backfill`: protege Top-5 de precision, luego permite backfill amplio.",
        "- `protected_top_10_backfill`: protege Top-10 de precision, luego permite backfill amplio.",
        "- `oracle_backfill_if_precision_misses_top10`: diagnostico con etiqueta esperada; aplica backfill si la respuesta no aparece en Top-10 de precision.",
        "- `oracle_backfill_if_precision_misses_top50`: diagnostico con etiqueta esperada; aplica backfill si la respuesta no aparece en Top-50 de precision.",
        "",
        "## Metricas comparativas",
        "",
        "| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4 | HS2 | NF |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in methods:
        m = metrics["metrics_by_method"][method]
        lines.append(
            f"| {method} | {m['top_1']:.4f} | {m['top_3']:.4f} | {m['top_5']:.4f} | {m['top_10']:.4f} | {m['mrr']:.4f} | {m['recall_at_50']:.4f} | {m['recall_at_100']:.4f} | {m['top_10_hs4']:.4f} | {m['top_10_hs2']:.4f} | {m['not_found_at_depth']} |"
        )

    critical_methods = [
        "BM25_flat_current",
        "C_hs6_leaf",
        "BM25_hierarchical_v0.1",
        *metrics["dual_strategy_order"],
    ]
    lines.extend(
        [
            "",
            "## Casos criticos",
            "",
            "| Codigo | Fuente | " + " | ".join(critical_methods) + " |",
            "|---|---|" + "---:|" * len(critical_methods),
        ]
    )
    for row in critical_rows:
        lines.append(
            "| "
            + " | ".join([row["codigo"], row["source"], *[str(row.get(f"{method}_rank", "")) for method in critical_methods]])
            + " |"
        )
    lines.extend(
        [
            "",
            "## Smoke tests",
            "",
            "- `soda caustica solida` espera 28151100; ver `dual_backfill_smoke_tests.json` para ranks y Top-10 por metodo.",
            "- `ruedas` espera 83022000; ver `dual_backfill_smoke_tests.json` para ranks y Top-10 por metodo.",
            "",
            "## Decision metodologica",
            "",
            f"Estrategia mejor clasificada: `{metrics['decision']['best_strategy']}`.",
            f"Clasificacion: {metrics['decision']['classifications'].get(metrics['decision']['best_strategy'], '')}.",
            metrics["decision"]["recommendation"],
            "",
            "## Alcance",
            "",
            "Esta fase solo usa devset. No se leyo ni ejecuto el evalset final. Tampoco se ejecuto LLM, Text2Trade ni Excel fuente.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    devset_path = resolve_project_path(args.devset)
    flat_index_path = resolve_project_path(args.flat_index)
    hierarchical_index_path = resolve_project_path(args.hierarchical_index)
    variants_dir = resolve_project_path(args.variants_dir)
    ablation_index_dir = resolve_project_path(args.ablation_index_dir)
    output_dir = resolve_project_path(args.output_dir)
    report_path = resolve_project_path(args.report)
    depth = args.retrieval_depth

    dev_rows = _read_csv(devset_path)
    if len(dev_rows) != EXPECTED_DEVSET_ROWS:
        raise ValueError(f"Devset row count is {len(dev_rows)}, expected {EXPECTED_DEVSET_ROWS}.")

    start = time.time()
    flat_index = load_bm25_index(flat_index_path)
    hierarchical_index = load_bm25_index(hierarchical_index_path)
    precision_index = _ensure_variant_index(PRECISION_VARIANT, variants_dir, ablation_index_dir, args.k1, args.b, args.force_rebuild)
    recall_index = _ensure_variant_index(RECALL_VARIANT, variants_dir, ablation_index_dir, args.k1, args.b, args.force_rebuild)

    strategy_order = [
        "precision_then_backfill_k10",
        "protected_top_5_backfill",
        "protected_top_10_backfill",
        "oracle_backfill_if_precision_misses_top10",
        "oracle_backfill_if_precision_misses_top50",
    ]
    method_order = [
        "BM25_flat_current",
        "C_hs6_leaf",
        "BM25_hierarchical_v0.1",
        *strategy_order,
    ]
    rows: list[dict[str, Any]] = []
    for position, dev_row in enumerate(dev_rows, start=1):
        descripcion = _clean(dev_row.get("descripcion"))
        true_code = _clean(dev_row.get("nandina") or dev_row.get("nandina_ref"))
        flat_hits = retrieve(flat_index, descripcion, top_n=depth)
        hierarchical_hits = retrieve(hierarchical_index, descripcion, top_n=depth)
        precision_hits = retrieve(precision_index, descripcion, top_n=depth)
        recall_hits = retrieve(recall_index, descripcion, top_n=depth)
        strategy_hits = {
            "precision_then_backfill_k10": _precision_then_backfill(precision_hits, recall_hits, depth, precision_top_k=args.precision_top_k),
            "protected_top_5_backfill": _protected_top_n_backfill(precision_hits, recall_hits, depth, protected_n=5),
            "protected_top_10_backfill": _protected_top_n_backfill(precision_hits, recall_hits, depth, protected_n=10),
            "oracle_backfill_if_precision_misses_top10": _oracle_backfill_if_precision_misses(
                precision_hits, recall_hits, true_code, depth=depth, miss_at=10, protected_n=10
            ),
            "oracle_backfill_if_precision_misses_top50": _oracle_backfill_if_precision_misses(
                precision_hits, recall_hits, true_code, depth=depth, miss_at=50, protected_n=10
            ),
        }
        method_hits = {
            "BM25_flat_current": flat_hits,
            "C_hs6_leaf": precision_hits,
            "BM25_hierarchical_v0.1": hierarchical_hits,
            **strategy_hits,
        }
        row: dict[str, Any] = {
            "case_id": f"dev-{position:02d}",
            "descripcion": descripcion,
            "nandina_ref": true_code,
            "hs4_ref": true_code[:4],
            "hs2_ref": true_code[:2],
        }
        for method, hits in method_hits.items():
            rank = rank_of_true(hits, true_code)
            row[f"{method}_rank"] = rank
            row[f"{method}_top10_hs4"] = _same_prefix_in_top(hits, true_code, 4)
            row[f"{method}_top10_hs2"] = _same_prefix_in_top(hits, true_code, 2)
            row[f"{method}_top10_codes"] = _top_codes(hits)
        rows.append(row)

    metrics_by_method = {method: _method_metrics(rows, method) for method in method_order}
    comparisons: dict[str, Any] = {}
    for method in method_order:
        comparisons[method] = {
            "vs_BM25_flat_current": _comparison(rows, method, "BM25_flat_current", depth),
            "vs_C_hs6_leaf": _comparison(rows, method, "C_hs6_leaf", depth),
            "vs_BM25_hierarchical_v0.1": _comparison(rows, method, "BM25_hierarchical_v0.1", depth),
        }

    critical_rows: list[dict[str, Any]] = []
    reference_for_code = {
        "39012000": "BM25_flat_current",
        "85414100": "BM25_flat_current",
        "28151100": "BM25_hierarchical_v0.1",
        "02013000": "BM25_hierarchical_v0.1",
        "95030010": "BM25_hierarchical_v0.1",
    }
    for row in rows:
        if row["nandina_ref"] in CRITICAL_CODES:
            reference = reference_for_code[row["nandina_ref"]]
            item: dict[str, Any] = {
                "source": "devset",
                "codigo": row["nandina_ref"],
                "case_id": row["case_id"],
                "descripcion": row["descripcion"],
                "reference_method": reference,
            }
            for method in method_order:
                item[f"{method}_rank"] = row[f"{method}_rank"]
                item[f"{method}_vs_reference"] = _critical_status(int(row[f"{method}_rank"]), int(row[f"{reference}_rank"]), depth)
            critical_rows.append(item)

    smoke_tests: dict[str, Any] = {}
    smoke_indexes = {
        "BM25_flat_current": flat_index,
        "C_hs6_leaf": precision_index,
        "BM25_hierarchical_v0.1": hierarchical_index,
    }
    for smoke_id, query, expected_code in SMOKE_TESTS:
        flat_hits = retrieve(flat_index, query, top_n=depth)
        precision_hits = retrieve(precision_index, query, top_n=depth)
        hierarchical_hits = retrieve(hierarchical_index, query, top_n=depth)
        recall_hits = retrieve(recall_index, query, top_n=depth)
        dual_hits = {
            "precision_then_backfill_k10": _precision_then_backfill(precision_hits, recall_hits, depth, args.precision_top_k),
            "protected_top_5_backfill": _protected_top_n_backfill(precision_hits, recall_hits, depth, protected_n=5),
            "protected_top_10_backfill": _protected_top_n_backfill(precision_hits, recall_hits, depth, protected_n=10),
            "oracle_backfill_if_precision_misses_top10": _protected_top_n_backfill(precision_hits, recall_hits, depth, protected_n=10),
            "oracle_backfill_if_precision_misses_top50": _protected_top_n_backfill(precision_hits, recall_hits, depth, protected_n=10),
        }
        smoke_tests[smoke_id] = {
            method: _smoke_rank(index, query, expected_code, depth)
            for method, index in smoke_indexes.items()
        }
        smoke_tests[smoke_id].update(
            {
                method: {
                    "query": query,
                    "expected_code": expected_code,
                    "rank": rank_of_true(hits, expected_code),
                    "top_10_codes": [_clean(hit.get("code")) for hit in hits[:10]],
                }
                for method, hits in dual_hits.items()
            }
        )
        if expected_code == "83022000":
            item = {
                "source": "smoke",
                "codigo": expected_code,
                "case_id": smoke_id,
                "descripcion": query,
                "reference_method": "BM25_flat_current",
            }
            for method in method_order:
                rank = int(smoke_tests[smoke_id][method]["rank"])
                item[f"{method}_rank"] = rank
                item[f"{method}_vs_reference"] = _critical_status(rank, int(smoke_tests[smoke_id]["BM25_flat_current"]["rank"]), depth)
            critical_rows.append(item)

    metrics_shell: dict[str, Any] = {
        "method_order": method_order,
        "dual_strategy_order": strategy_order,
        "metrics_by_method": metrics_by_method,
    }
    decision_base = {"method_order": method_order, "dual_strategy_order": strategy_order, "metrics_by_method": metrics_by_method}
    strategy_decision = _classify_strategy(decision_base, comparisons, critical_rows)
    best_strategy = strategy_decision["best_strategy"]
    best_class = strategy_decision["classifications"].get(best_strategy or "", "C. No candidato")
    if best_class.startswith("A."):
        recommendation = f"`{best_strategy}` puede pasar a evalset en una subfase separada de confirmacion, manteniendo congelados parametros e insumos."
    elif best_class.startswith("B."):
        recommendation = f"`{best_strategy}` es candidato exploratorio: mejora recall o balance, pero conserva degradaciones menores; conviene iterar antes de evalset."
    else:
        recommendation = "No hay candidato dual: no mejora suficientemente frente a C_hs6_leaf ni frente al jerarquico v0.1."
    decision = {**strategy_decision, "recommendation": recommendation}

    metrics: dict[str, Any] = {
        "script": "src.experiments.evaluate_bm25_dual_backfill_devset",
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
            "flat_index_path": _rel(flat_index_path, root),
            "flat_index_sha256": sha256_file(flat_index_path),
            "hierarchical_index_path": _rel(hierarchical_index_path, root),
            "hierarchical_index_sha256": sha256_file(hierarchical_index_path),
            "precision_variant": PRECISION_VARIANT,
            "precision_index_path": _rel(ablation_index_dir / f"{PRECISION_VARIANT}.pkl", root),
            "recall_variant": RECALL_VARIANT,
            "recall_index_path": _rel(ablation_index_dir / f"{RECALL_VARIANT}.pkl", root),
        },
        "bm25_config": {
            "k1": args.k1,
            "b": args.b,
            "retrieval_depth": depth,
            "precision_top_k": args.precision_top_k,
            "stopwords_count": len(DEFAULT_STOPWORDS_ES),
            "stopwords_source": "src.bm25_index.DEFAULT_STOPWORDS_ES",
        },
        "method_order": method_order,
        "dual_strategy_order": strategy_order,
        "metrics_by_method": metrics_by_method,
        "comparisons": comparisons,
        "decision": decision,
        "outputs": {
            "dual_backfill_results_csv": _rel(output_dir / "dual_backfill_results.csv", root),
            "dual_backfill_metrics_json": _rel(output_dir / "dual_backfill_metrics.json", root),
            "dual_backfill_summary_md": _rel(output_dir / "dual_backfill_summary.md", root),
            "dual_backfill_case_comparison_13_cases_csv": _rel(output_dir / "dual_backfill_case_comparison_13_cases.csv", root),
            "dual_backfill_critical_cases_csv": _rel(output_dir / "dual_backfill_critical_cases.csv", root),
            "dual_backfill_smoke_tests_json": _rel(output_dir / "dual_backfill_smoke_tests.json", root),
            "report_md": _rel(report_path, root),
        },
        "warnings": [
            "Only devset was evaluated; evalset was not read or executed.",
            "Oracle strategies use the expected label and are diagnostic only, not production-applicable.",
            "No LLM, Text2Trade, or source Excel execution is part of this script.",
        ],
    }

    result_fields = ["case_id", "descripcion", "nandina_ref", "hs4_ref", "hs2_ref"]
    for method in method_order:
        result_fields.extend([f"{method}_rank", f"{method}_top10_hs4", f"{method}_top10_hs2", f"{method}_top10_codes"])
    _write_csv(output_dir / "dual_backfill_results.csv", rows, result_fields)
    _write_csv(output_dir / "dual_backfill_case_comparison_13_cases.csv", rows, result_fields)

    critical_fields = ["source", "codigo", "case_id", "descripcion", "reference_method"]
    for method in method_order:
        critical_fields.extend([f"{method}_rank", f"{method}_vs_reference"])
    _write_csv(output_dir / "dual_backfill_critical_cases.csv", critical_rows, critical_fields)
    _write_json(output_dir / "dual_backfill_metrics.json", metrics)
    _write_json(output_dir / "dual_backfill_smoke_tests.json", smoke_tests)
    summary = _summary_markdown(metrics, critical_rows)
    ensure_parent(output_dir / "dual_backfill_summary.md")
    (output_dir / "dual_backfill_summary.md").write_text(summary, encoding="utf-8")
    ensure_parent(report_path)
    report_path.write_text(summary, encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate defensive dual BM25 backfill retrieval on devset only.")
    parser.add_argument("--devset", type=Path, default=DEFAULT_DEVSET)
    parser.add_argument("--flat-index", type=Path, default=DEFAULT_FLAT_INDEX)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIER_INDEX)
    parser.add_argument("--variants-dir", type=Path, default=DEFAULT_VARIANTS_DIR)
    parser.add_argument("--ablation-index-dir", type=Path, default=DEFAULT_ABLATION_INDEX_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--retrieval-depth", type=int, default=100)
    parser.add_argument("--precision-top-k", type=int, default=10)
    parser.add_argument("--k1", type=float, default=1.5)
    parser.add_argument("--b", type=float, default=0.75)
    parser.add_argument("--force-rebuild", action="store_true")
    return parser


def main() -> int:
    metrics = evaluate(build_parser().parse_args())
    print("OK: evaluacion BM25 dual backfill devset completada")
    print(f"Estrategia mejor clasificada: {metrics['decision']['best_strategy']}")
    print(f"Clasificacion: {metrics['decision']['classifications'].get(metrics['decision']['best_strategy'], '')}")
    for method in metrics["method_order"]:
        item = metrics["metrics_by_method"][method]
        print(
            f"{method}: top1={item['top_1']:.4f} top10={item['top_10']:.4f} "
            f"mrr={item['mrr']:.4f} r100={item['recall_at_100']:.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
