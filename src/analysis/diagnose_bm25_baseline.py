from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from ..retrieval.bm25 import load_bm25_index
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_RESULTS = Path("outputs/evaluation/bm25_eval_v0.1/results.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/bm25_eval_v0.1")
DEFAULT_K_LIST = [1, 3, 5, 10]


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV without header: {path}")
        return [{_clean(key): _clean(value) for key, value in row.items() if key is not None} for row in reader]


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _report_path(path: Path, root: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return str(resolved)


def _parse_k_list(raw: str | None) -> list[int]:
    values = DEFAULT_K_LIST if not raw else [int(part.strip()) for part in raw.split(",") if part.strip()]
    values = sorted(set(values))
    if not values or any(value <= 0 for value in values):
        raise ValueError("k-list must contain positive integers")
    return values


def _rate(numerator: int, denominator: int) -> float:
    return float(numerator / denominator) if denominator else 0.0


def _mean(values: Sequence[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _code_prefix(code: str, width: int) -> str:
    code = _clean(code)
    return code[:width] if len(code) >= width else ""


def _candidate_codes(row: Mapping[str, str], k: int) -> list[str]:
    codes: list[str] = []
    for rank in range(1, k + 1):
        code = _clean(row.get(f"candidate_{rank}_code"))
        if code:
            codes.append(code)
    return codes


def _candidate_payload(row: Mapping[str, str], k: int) -> list[dict[str, Any]]:
    payload: list[dict[str, Any]] = []
    for rank in range(1, k + 1):
        code = _clean(row.get(f"candidate_{rank}_code"))
        if not code:
            continue
        score_raw = _clean(row.get(f"candidate_{rank}_score"))
        try:
            score: float | str = float(score_raw)
        except ValueError:
            score = score_raw
        payload.append(
            {
                "rank": rank,
                "code": code,
                "score": score,
                "text": _clean(row.get(f"candidate_{rank}_text")),
            }
        )
    return payload


def _has_exact(row: Mapping[str, str], k: int) -> bool:
    return _clean(row.get("nandina_ref")) in _candidate_codes(row, k)


def _has_prefix(row: Mapping[str, str], k: int, width: int) -> bool:
    ref_prefix = _code_prefix(_clean(row.get("nandina_ref")), width)
    return bool(ref_prefix) and any(_code_prefix(code, width) == ref_prefix for code in _candidate_codes(row, k))


def _coverage_by_group(rows: Sequence[Mapping[str, Any]], group_field: str, index_codes: set[str]) -> dict[str, Any]:
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[_clean(row.get(group_field))].append(row)

    output: dict[str, Any] = {}
    for group, group_rows in sorted(grouped.items()):
        codes = {_clean(row.get("nandina_ref")) for row in group_rows if _clean(row.get("nandina_ref"))}
        covered_codes = codes & index_codes
        cases_covered = sum(1 for row in group_rows if _clean(row.get("nandina_ref")) in index_codes)
        output[group] = {
            "cases": len(group_rows),
            "unique_nandina8": len(codes),
            "unique_nandina8_in_index": len(covered_codes),
            "unique_nandina8_missing_index": len(codes - index_codes),
            "unique_code_coverage_rate": _rate(len(covered_codes), len(codes)),
            "cases_with_code_in_index": cases_covered,
            "case_coverage_rate": _rate(cases_covered, len(group_rows)),
        }
    return output


def _hierarchical_metrics(rows: Sequence[Mapping[str, Any]], k_list: Sequence[int]) -> dict[str, Any]:
    metrics: dict[str, Any] = {}
    total = len(rows)
    for k in k_list:
        exact_hits = sum(1 for row in rows if _has_exact(row, k))
        hs4_hits = sum(1 for row in rows if _has_prefix(row, k, 4))
        hs2_hits = sum(1 for row in rows if _has_prefix(row, k, 2))
        metrics[f"top_{k}"] = {
            "nandina8_exact_accuracy": _rate(exact_hits, total),
            "hs4_partida_accuracy": _rate(hs4_hits, total),
            "hs2_capitulo_accuracy": _rate(hs2_hits, total),
            "nandina8_exact_hits": exact_hits,
            "hs4_partida_hits": hs4_hits,
            "hs2_capitulo_hits": hs2_hits,
        }
    return metrics


def _failure_reason(row: Mapping[str, Any]) -> str:
    if not bool(row["correct_in_index"]):
        return "correct_code_missing_from_index"
    if int(row["retrieved_count"]) == 0:
        return "zero_retrieval"
    if bool(row["exact_top_10"]):
        return "exact_match_top_10"
    if bool(row["hs4_top_10"]):
        return "hs4_match_only"
    if bool(row["hs2_top_10"]):
        return "hs2_match_only"
    return "no_hs2_family_match_top_10"


def _annotate_rows(results: Sequence[Mapping[str, str]], index_codes: set[str]) -> list[dict[str, Any]]:
    annotated: list[dict[str, Any]] = []
    for row in results:
        nandina_ref = _clean(row.get("nandina_ref"))
        enriched = dict(row)
        enriched["correct_in_index"] = nandina_ref in index_codes
        enriched["exact_top_10"] = _has_exact(row, 10)
        enriched["hs4_top_10"] = _has_prefix(row, 10, 4)
        enriched["hs2_top_10"] = _has_prefix(row, 10, 2)
        enriched["retrieved_count"] = int(_clean(row.get("retrieved_count")) or "0")
        enriched["rank_ref"] = int(_clean(row.get("rank_ref")) or "0")
        enriched["diagnostic_reason"] = _failure_reason(enriched)
        annotated.append(enriched)
    return annotated


def _group_performance(
    rows: Sequence[Mapping[str, Any]],
    group_field: str,
    k_list: Sequence[int],
    min_group_size: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[_clean(row.get(group_field))].append(row)

    reported: dict[str, Any] = {}
    excluded_groups = 0
    excluded_cases = 0
    for group, group_rows in sorted(grouped.items()):
        if len(group_rows) < min_group_size:
            excluded_groups += 1
            excluded_cases += len(group_rows)
            continue
        payload: dict[str, Any] = {
            "cases": len(group_rows),
            "correct_code_in_index_rate": _mean([1.0 if row["correct_in_index"] else 0.0 for row in group_rows]),
            "zero_retrieval_cases": sum(1 for row in group_rows if int(row["retrieved_count"]) == 0),
            "no_exact_top_10_cases": sum(1 for row in group_rows if not row["exact_top_10"]),
        }
        for k in k_list:
            payload[f"exact_top_{k}_accuracy"] = _mean([1.0 if _has_exact(row, k) else 0.0 for row in group_rows])
            payload[f"hs4_top_{k}_accuracy"] = _mean([1.0 if _has_prefix(row, k, 4) else 0.0 for row in group_rows])
            payload[f"hs2_top_{k}_accuracy"] = _mean([1.0 if _has_prefix(row, k, 2) else 0.0 for row in group_rows])
        reported[group] = payload

    audit = {
        "field": group_field,
        "min_group_size": min_group_size,
        "groups_total": len(grouped),
        "groups_reported": len(reported),
        "groups_excluded_small_n": excluded_groups,
        "cases_excluded_small_groups": excluded_cases,
    }
    return reported, audit


def _rank_groups(groups: Mapping[str, Mapping[str, Any]], metric: str, reverse: bool = True, limit: int = 10) -> list[dict[str, Any]]:
    ranked = sorted(
        (
            {"group": group, "cases": payload.get("cases", 0), metric: payload.get(metric, 0)}
            for group, payload in groups.items()
        ),
        key=lambda item: (item[metric], item["cases"], item["group"]),
        reverse=reverse,
    )
    return ranked[:limit]


def _failure_sample(rows: Sequence[Mapping[str, Any]], limit: int) -> list[dict[str, Any]]:
    failures = [row for row in rows if row["diagnostic_reason"] != "exact_match_top_10"]
    by_reason: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in failures:
        by_reason[str(row["diagnostic_reason"])].append(row)

    selected: list[Mapping[str, Any]] = []
    per_reason = max(1, limit // max(1, len(by_reason)))
    for reason in sorted(by_reason):
        selected.extend(by_reason[reason][:per_reason])
    if len(selected) < limit:
        already = {str(row.get("case_id")) for row in selected}
        selected.extend(row for row in failures if str(row.get("case_id")) not in already)

    sample_rows: list[dict[str, Any]] = []
    for row in selected[:limit]:
        sample_rows.append(
            {
                "case_id": row.get("case_id", ""),
                "descripcion": row.get("descripcion", ""),
                "nandina_ref": row.get("nandina_ref", ""),
                "capitulo_ref": row.get("capitulo_ref", ""),
                "partida_ref": row.get("partida_ref", ""),
                "rank_ref": row.get("rank_ref", 0),
                "retrieved_count": row.get("retrieved_count", 0),
                "correct_in_index": int(bool(row.get("correct_in_index"))),
                "diagnostic_reason": row.get("diagnostic_reason", ""),
                "top5_candidates": json.dumps(_candidate_payload(row, 5), ensure_ascii=False),
            }
        )
    return sample_rows


def _summary_markdown(diagnostics: Mapping[str, Any]) -> str:
    coverage = diagnostics["coverage"]
    exact_top10 = diagnostics["hierarchical_metrics"]["top_10"]["nandina8_exact_accuracy"]
    hs4_top10 = diagnostics["hierarchical_metrics"]["top_10"]["hs4_partida_accuracy"]
    hs2_top10 = diagnostics["hierarchical_metrics"]["top_10"]["hs2_capitulo_accuracy"]
    failures = diagnostics["failure_diagnostics"]
    lines = [
        "# Diagnostico BM25 baseline v0.1",
        "",
        "## Insumos",
        "",
        f"- Evalset: `{diagnostics['input']['evalset_path']}`.",
        f"- Indice BM25: `{diagnostics['input']['bm25_index_path']}`.",
        f"- Resultados BM25: `{diagnostics['input']['results_csv']}`.",
        "",
        "## Cobertura del indice",
        "",
        f"- NANDINA8 unicas en evalset: {coverage['unique_nandina8_evalset']}.",
        f"- NANDINA8 unicas presentes en indice: {coverage['unique_nandina8_in_index']}.",
        f"- NANDINA8 unicas ausentes del indice: {coverage['unique_nandina8_missing_index']}.",
        f"- Cobertura unica NANDINA8: {coverage['unique_nandina8_coverage_rate']:.4f}.",
        f"- Casos cuyo codigo correcto existe en el indice: {coverage['cases_with_code_in_index']} de {coverage['cases_total']}.",
        "",
        "## Evaluacion jerarquica",
        "",
        f"- Top-10 exacto NANDINA8: {exact_top10:.4f}.",
        f"- Top-10 partida HS4: {hs4_top10:.4f}.",
        f"- Top-10 capitulo HS2: {hs2_top10:.4f}.",
        "",
        "## Fallos principales",
        "",
        f"- Codigo correcto existe en indice pero no aparece en Top-10: {failures['correct_in_index_but_not_top_10']}.",
        f"- Codigo correcto no existe en indice: {failures['correct_code_missing_from_index']}.",
        f"- Cero resultados recuperados: {failures['zero_retrieval']}.",
        f"- Aparece capitulo correcto pero no partida: {failures['hs2_match_without_hs4']}.",
        f"- Aparece partida correcta pero no NANDINA8 exacta: {failures['hs4_match_without_exact']}.",
        "",
        "## Lectura diagnostica",
        "",
        diagnostics["interpretation"]["brief_explanation"],
        "",
        "## Siguiente comparacion",
        "",
        diagnostics["recommendation"],
        "",
    ]
    return "\n".join(lines)


def diagnose(args: argparse.Namespace) -> dict[str, Any]:
    root = project_root()
    evalset_path = resolve_project_path(args.evalset)
    index_path = resolve_project_path(args.index)
    results_path = resolve_project_path(args.results)
    output_dir = resolve_project_path(args.output_dir)
    k_list = _parse_k_list(args.k_list)

    eval_rows = _read_csv(evalset_path)
    result_rows = _read_csv(results_path)
    index = load_bm25_index(index_path)
    index_codes = {str(code).strip() for code in index.doc_ids}

    by_case = {_clean(row.get("case_id")): row for row in result_rows}
    if len(by_case) != len(result_rows):
        raise ValueError("results.csv contains duplicate case_id values")

    annotated = _annotate_rows(result_rows, index_codes)
    total = len(annotated)
    eval_codes = {_clean(row.get("nandina_ref")) for row in eval_rows if _clean(row.get("nandina_ref"))}
    covered_codes = eval_codes & index_codes
    cases_with_code = sum(1 for row in annotated if row["correct_in_index"])

    coverage = {
        "cases_total": total,
        "unique_nandina8_evalset": len(eval_codes),
        "unique_nandina8_in_index": len(covered_codes),
        "unique_nandina8_missing_index": len(eval_codes - index_codes),
        "unique_nandina8_coverage_rate": _rate(len(covered_codes), len(eval_codes)),
        "cases_with_code_in_index": cases_with_code,
        "cases_missing_code_in_index": total - cases_with_code,
        "case_code_coverage_rate": _rate(cases_with_code, total),
        "by_chapter": _coverage_by_group(annotated, "capitulo_ref", index_codes),
        "by_heading": _coverage_by_group(annotated, "partida_ref", index_codes),
    }

    hierarchical = _hierarchical_metrics(annotated, k_list)
    reason_counts = Counter(str(row["diagnostic_reason"]) for row in annotated)
    failure_diagnostics = {
        "correct_in_index_but_not_top_10": sum(
            1 for row in annotated if row["correct_in_index"] and not row["exact_top_10"]
        ),
        "correct_code_missing_from_index": sum(1 for row in annotated if not row["correct_in_index"]),
        "zero_retrieval": sum(1 for row in annotated if int(row["retrieved_count"]) == 0),
        "hs2_match_without_hs4": sum(1 for row in annotated if row["hs2_top_10"] and not row["hs4_top_10"]),
        "hs4_match_without_exact": sum(1 for row in annotated if row["hs4_top_10"] and not row["exact_top_10"]),
        "reason_counts": dict(sorted(reason_counts.items())),
    }

    by_chapter, chapter_audit = _group_performance(annotated, "capitulo_ref", k_list, args.min_group_size)
    by_heading, heading_audit = _group_performance(annotated, "partida_ref", k_list, args.min_group_size)
    failures_by_chapter = _rank_groups(by_chapter, "no_exact_top_10_cases", reverse=True)
    failures_by_heading = _rank_groups(by_heading, "no_exact_top_10_cases", reverse=True)
    best_chapter_hs2 = _rank_groups(by_chapter, "hs2_top_10_accuracy", reverse=True)
    best_heading_hs4 = _rank_groups(by_heading, "hs4_top_10_accuracy", reverse=True)

    hs4_gain = hierarchical["top_10"]["hs4_partida_accuracy"] - hierarchical["top_10"]["nandina8_exact_accuracy"]
    hs2_gain = hierarchical["top_10"]["hs2_capitulo_accuracy"] - hierarchical["top_10"]["nandina8_exact_accuracy"]
    if coverage["unique_nandina8_coverage_rate"] >= 0.95:
        coverage_note = (
            "La cobertura es alta: el bajo desempeno exacto no se explica principalmente por codigos "
            "NANDINA8 ausentes del indice."
        )
    else:
        coverage_note = (
            "La cobertura es incompleta y puede explicar parte del bajo desempeno exacto."
        )
    brief = (
        f"{coverage_note} El Top-10 exacto es {hierarchical['top_10']['nandina8_exact_accuracy']:.4f}, "
        f"mientras que el Top-10 HS4 es {hierarchical['top_10']['hs4_partida_accuracy']:.4f} "
        f"y el Top-10 HS2 es {hierarchical['top_10']['hs2_capitulo_accuracy']:.4f}. "
        "Esto apunta a una brecha de lexicalizacion y granularidad: BM25 a veces llega a la familia "
        "correcta, pero rara vez a la subpartida NANDINA8 exacta."
    )

    diagnostics: dict[str, Any] = {
        "script": "src.analysis.diagnose_bm25_baseline",
        "execution": {"datetime_utc": datetime.now(timezone.utc).isoformat()},
        "input": {
            "evalset_path": _report_path(evalset_path, root),
            "bm25_index_path": _report_path(index_path, root),
            "results_csv": _report_path(results_path, root),
        },
        "parameters": {"k_list": k_list, "min_group_size": args.min_group_size},
        "coverage": coverage,
        "hierarchical_metrics": hierarchical,
        "failure_diagnostics": failure_diagnostics,
        "performance_by_chapter": by_chapter,
        "performance_by_heading": by_heading,
        "grouping": {"chapter": chapter_audit, "heading": heading_audit},
        "families_with_most_failures": {
            "by_chapter": failures_by_chapter,
            "by_heading": failures_by_heading,
        },
        "families_with_best_partial_performance": {
            "by_chapter_hs2_top_10": best_chapter_hs2,
            "by_heading_hs4_top_10": best_heading_hs4,
        },
        "interpretation": {
            "coverage_problem": coverage["unique_nandina8_coverage_rate"] < 0.95,
            "hs4_gain_over_exact_top_10": hs4_gain,
            "hs2_gain_over_exact_top_10": hs2_gain,
            "brief_explanation": brief,
        },
        "recommendation": (
            "Mantener BM25 puro como baseline lexical debil y comparar luego contra Text2Trade/recuperacion "
            "densa, re-ranking o LLM+RAG usando el mismo evalset y las mismas metricas jerarquicas."
        ),
        "outputs": {
            "diagnostics_json": _report_path(output_dir / "diagnostics.json", root),
            "diagnostics_md": _report_path(output_dir / "diagnostics.md", root),
            "failure_sample_csv": _report_path(output_dir / "failure_sample.csv", root),
        },
    }

    sample_rows = _failure_sample(annotated, args.sample_size)
    _write_json(output_dir / "diagnostics.json", diagnostics)
    ensure_parent(output_dir / "diagnostics.md")
    (output_dir / "diagnostics.md").write_text(_summary_markdown(diagnostics), encoding="utf-8")
    _write_csv(
        output_dir / "failure_sample.csv",
        sample_rows,
        [
            "case_id",
            "descripcion",
            "nandina_ref",
            "capitulo_ref",
            "partida_ref",
            "rank_ref",
            "retrieved_count",
            "correct_in_index",
            "diagnostic_reason",
            "top5_candidates",
        ],
    )
    return diagnostics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Diagnose the BM25 baseline evaluation on evalset v0.1.")
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--k-list", default="1,3,5,10")
    parser.add_argument("--min-group-size", type=int, default=5)
    parser.add_argument("--sample-size", type=int, default=50)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    diagnostics = diagnose(args)
    coverage = diagnostics["coverage"]
    top10 = diagnostics["hierarchical_metrics"]["top_10"]
    print("OK: diagnostico BM25 completado")
    print(f"Casos: {coverage['cases_total']}")
    print(f"Cobertura unica NANDINA8: {coverage['unique_nandina8_coverage_rate']:.4f}")
    print(f"Top-10 exacto: {top10['nandina8_exact_accuracy']:.4f}")
    print(f"Top-10 HS4: {top10['hs4_partida_accuracy']:.4f}")
    print(f"Top-10 HS2: {top10['hs2_capitulo_accuracy']:.4f}")
    print(f"Outputs: {diagnostics['outputs']['diagnostics_json']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
