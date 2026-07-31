from __future__ import annotations

import argparse
import csv
import json
import math
import platform
import re
import statistics
import time
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/evalset_v0.1.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/historical_examples_leave_one_out_v0.1")
DEFAULT_PHASE7A_SUMMARY = Path("outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool_case_summary.csv")
DEFAULT_PHASE8B_SUMMARY = Path("outputs/evaluation/nonrestrictive_expanded_pool_evalset_v0.1/expanded_pool_case_summary.csv")

METHOD_BM25 = "historical_bm25_description"
METHOD_TFIDF = "historical_tfidf_char_word"
PHASE7A_STRATEGY = "hierarchical_80_dual_backfill_20"
PHASE8B_STRATEGY = "phase7a_plus_all_sources_200"
K_VALUES = [1, 3, 5, 10, 20, 50, 100]
EXPECTED_ROWS = 600

TOKEN_RE = re.compile(r"[a-z0-9]+")


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


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


def _median(values: Sequence[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def _normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text.lower())
    return "".join(char for char in normalized if not unicodedata.combining(char))


def _tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(_normalize_text(text))


def _case_id(row: Mapping[str, Any], position: int) -> str:
    return _clean(row.get("case_id")) or f"SUNAT-{position:04d}"


def _expected(row: Mapping[str, Any]) -> str:
    return _clean(row.get("nandina_ref") or row.get("nandina"))


def _hs_prefix(code: str, length: int) -> str:
    return _clean(code)[:length]


def _first_rank(candidates: Sequence[Mapping[str, Any]], expected: str, prefix_len: int | None = None) -> int:
    expected_value = _hs_prefix(expected, prefix_len) if prefix_len else expected
    for rank, candidate in enumerate(candidates, start=1):
        code = _clean(candidate.get("candidate_nandina"))
        value = _hs_prefix(code, prefix_len) if prefix_len else code
        if value == expected_value:
            return rank
    return 0


def _hit_at(rank: int, k: int) -> int:
    return int(acc_at_k(rank, k))


def _ranked_unique_candidates(
    case_index: int,
    scores: Mapping[int, float],
    rows: Sequence[Mapping[str, str]],
    method: str,
    limit: int,
) -> list[dict[str, Any]]:
    ordered = sorted(
        ((doc_index, score) for doc_index, score in scores.items() if doc_index != case_index),
        key=lambda item: (-float(item[1]), _case_id(rows[item[0]], item[0] + 1)),
    )
    seen_codes: set[str] = set()
    candidates: list[dict[str, Any]] = []
    for doc_index, score in ordered:
        candidate_code = _expected(rows[doc_index])
        if not candidate_code or candidate_code in seen_codes:
            continue
        seen_codes.add(candidate_code)
        candidates.append(
            {
                "candidate_nandina": candidate_code,
                "candidate_case_id": _case_id(rows[doc_index], doc_index + 1),
                "candidate_description": _clean(rows[doc_index].get("descripcion")),
                "score": float(score),
                "method": method,
            }
        )
        if len(candidates) >= limit:
            break
    return candidates


def _bm25_scores_for_case(
    case_index: int,
    query_tokens: Sequence[str],
    doc_counters: Sequence[Counter[str]],
    doc_lengths: Sequence[int],
    doc_freq: Mapping[str, int],
    total_length: int,
    k1: float = 1.5,
    b: float = 0.75,
) -> dict[int, float]:
    historical_n = len(doc_counters) - 1
    historical_length = total_length - doc_lengths[case_index]
    avgdl = historical_length / historical_n if historical_n else 0.0
    query_counter = Counter(query_tokens)
    scores: dict[int, float] = {}

    for term, query_tf in query_counter.items():
        df = int(doc_freq.get(term, 0))
        if term in doc_counters[case_index]:
            df -= 1
        if df <= 0:
            continue
        idf = math.log(1.0 + ((historical_n - df + 0.5) / (df + 0.5)))
        for doc_index, counter in enumerate(doc_counters):
            if doc_index == case_index:
                continue
            tf = counter.get(term, 0)
            if not tf:
                continue
            denominator = tf + k1 * (1.0 - b + b * (doc_lengths[doc_index] / avgdl))
            scores[doc_index] = scores.get(doc_index, 0.0) + idf * (tf * (k1 + 1.0) / denominator) * query_tf
    return scores


def _evaluate_bm25(rows: Sequence[Mapping[str, str]], limit: int) -> dict[str, Any]:
    descriptions = [_clean(row.get("descripcion")) for row in rows]
    tokenized = [_tokenize(text) for text in descriptions]
    counters = [Counter(tokens) for tokens in tokenized]
    lengths = [len(tokens) for tokens in tokenized]
    total_length = sum(lengths)
    doc_freq: Counter[str] = Counter()
    for counter in counters:
        doc_freq.update(counter.keys())

    candidate_rows: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []
    for case_index, row in enumerate(rows):
        scores = _bm25_scores_for_case(case_index, tokenized[case_index], counters, lengths, doc_freq, total_length)
        candidates = _ranked_unique_candidates(case_index, scores, rows, METHOD_BM25, limit)
        case_rows.append(_case_summary(case_index, row, candidates, METHOD_BM25))
        candidate_rows.extend(_candidate_rows(case_index, row, candidates, METHOD_BM25))
    return {"method": METHOD_BM25, "case_rows": case_rows, "candidate_rows": candidate_rows}


def _sklearn_available() -> bool:
    try:
        import sklearn  # noqa: F401
    except ImportError:
        return False
    return True


def _evaluate_tfidf(rows: Sequence[Mapping[str, str]], limit: int) -> dict[str, Any]:
    from scipy.sparse import hstack
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    descriptions = [_clean(row.get("descripcion")) for row in rows]
    candidate_rows: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []

    for case_index, row in enumerate(rows):
        historical_indices = [idx for idx in range(len(rows)) if idx != case_index]
        historical_docs = [descriptions[idx] for idx in historical_indices]
        word_vectorizer = TfidfVectorizer(
            lowercase=True,
            strip_accents="unicode",
            analyzer="word",
            token_pattern=r"(?u)\b[a-zA-Z0-9]+\b",
            ngram_range=(1, 2),
            min_df=1,
        )
        char_vectorizer = TfidfVectorizer(
            lowercase=True,
            strip_accents="unicode",
            analyzer="char_wb",
            ngram_range=(3, 5),
            min_df=1,
        )
        hist_word = word_vectorizer.fit_transform(historical_docs)
        query_word = word_vectorizer.transform([descriptions[case_index]])
        hist_char = char_vectorizer.fit_transform(historical_docs)
        query_char = char_vectorizer.transform([descriptions[case_index]])
        hist_matrix = hstack([hist_word, hist_char], format="csr")
        query_matrix = hstack([query_word, query_char], format="csr")
        similarities = cosine_similarity(query_matrix, hist_matrix).ravel()
        scores = {historical_indices[pos]: float(score) for pos, score in enumerate(similarities)}
        candidates = _ranked_unique_candidates(case_index, scores, rows, METHOD_TFIDF, limit)
        case_rows.append(_case_summary(case_index, row, candidates, METHOD_TFIDF))
        candidate_rows.extend(_candidate_rows(case_index, row, candidates, METHOD_TFIDF))
    return {"method": METHOD_TFIDF, "case_rows": case_rows, "candidate_rows": candidate_rows}


def _candidate_rows(
    case_index: int,
    row: Mapping[str, str],
    candidates: Sequence[Mapping[str, Any]],
    method: str,
) -> list[dict[str, Any]]:
    case_id = _case_id(row, case_index + 1)
    expected = _expected(row)
    output: list[dict[str, Any]] = []
    for rank, candidate in enumerate(candidates, start=1):
        output.append(
            {
                "case_id": case_id,
                "expected_nandina": expected,
                "candidate_rank": rank,
                "candidate_nandina": candidate["candidate_nandina"],
                "candidate_case_id": candidate["candidate_case_id"],
                "candidate_description": candidate["candidate_description"],
                "score": candidate["score"],
                "method": method,
            }
        )
    return output


def _case_summary(
    case_index: int,
    row: Mapping[str, str],
    candidates: Sequence[Mapping[str, Any]],
    method: str,
) -> dict[str, Any]:
    expected = _expected(row)
    exact_rank = _first_rank(candidates, expected)
    hs6_rank = _first_rank(candidates, expected, 6)
    hs4_rank = _first_rank(candidates, expected, 4)
    hs2_rank = _first_rank(candidates, expected, 2)
    top = candidates[0] if candidates else {}
    summary: dict[str, Any] = {
        "method": method,
        "case_id": _case_id(row, case_index + 1),
        "expected_nandina": expected,
        "descripcion": _clean(row.get("descripcion")),
        "hs2_ref": _hs_prefix(expected, 2),
        "hs4_ref": _hs_prefix(expected, 4),
        "hs6_ref": _hs_prefix(expected, 6),
        "unique_candidates": len(candidates),
        "exact_rank": exact_rank,
        "hs6_first_rank": hs6_rank,
        "hs4_first_rank": hs4_rank,
        "hs2_first_rank": hs2_rank,
        "reciprocal_rank": mrr_from_rank(exact_rank),
        "top_candidate_nandina": _clean(top.get("candidate_nandina")),
        "top_candidate_case_id": _clean(top.get("candidate_case_id")),
        "top_candidate_score": top.get("score", ""),
        "self_match_detected": str(_case_id(row, case_index + 1) == _clean(top.get("candidate_case_id"))).lower(),
    }
    for k in K_VALUES:
        summary[f"exact_at_{k}"] = _hit_at(exact_rank, k)
        summary[f"hs6_at_{k}"] = _hit_at(hs6_rank, k)
        summary[f"hs4_at_{k}"] = _hit_at(hs4_rank, k)
        summary[f"hs2_at_{k}"] = _hit_at(hs2_rank, k)
    return summary


def _distribution(case_rows: Sequence[Mapping[str, Any]], key: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in case_rows:
        grouped[_clean(row.get(key))].append(row)
    output: list[dict[str, Any]] = []
    for family, rows in sorted(grouped.items()):
        failures = [row for row in rows if int(row["exact_at_100"]) == 0]
        output.append(
            {
                key: family,
                "cases": len(rows),
                "exact_at_100": sum(int(row["exact_at_100"]) for row in rows),
                "failures_at_100": len(failures),
                "recall_at_100": _mean([float(row["exact_at_100"]) for row in rows]),
                "mrr": _mean([float(row["reciprocal_rank"]) for row in rows]),
            }
        )
    output.sort(key=lambda item: (-int(item["failures_at_100"]), -int(item["cases"]), str(item[key])))
    return output


def _metrics_for_method(case_rows: Sequence[Mapping[str, Any]], method: str) -> dict[str, Any]:
    metrics: dict[str, Any] = {
        "method": method,
        "cases_evaluated": len(case_rows),
        "mrr": _mean([float(row["reciprocal_rank"]) for row in case_rows]),
        "median_exact_rank_nonzero": _median([float(row["exact_rank"]) for row in case_rows if int(row["exact_rank"]) > 0]),
        "correct_not_in_top_100": sum(1 for row in case_rows if int(row["exact_at_100"]) == 0),
        "distribution_by_hs2": _distribution(case_rows, "hs2_ref"),
        "distribution_by_hs4": _distribution(case_rows, "hs4_ref"),
    }
    for k in K_VALUES:
        metrics[f"exact_at_{k}"] = _mean([float(row[f"exact_at_{k}"]) for row in case_rows])
        metrics[f"hs6_at_{k}"] = _mean([float(row[f"hs6_at_{k}"]) for row in case_rows])
        metrics[f"hs4_at_{k}"] = _mean([float(row[f"hs4_at_{k}"]) for row in case_rows])
        metrics[f"hs2_at_{k}"] = _mean([float(row[f"hs2_at_{k}"]) for row in case_rows])
    return metrics


def _baseline_hits(path: Path, phase: str) -> tuple[dict[str, bool], str]:
    if not path.exists():
        return {}, f"not_found: {_clean(path)}"
    rows = _read_csv(path)
    hits: dict[str, bool] = {}
    if phase == "phase7a":
        selected = [row for row in rows if _clean(row.get("pool_strategy")) == PHASE7A_STRATEGY]
        if not selected:
            return {}, f"strategy_not_found: {PHASE7A_STRATEGY}"
        for row in selected:
            hits[_clean(row.get("case_id"))] = bool(int(_clean(row.get("final_pool_at_100")) or "0"))
        return hits, "loaded"

    selected = [row for row in rows if _clean(row.get("strategy")) == PHASE8B_STRATEGY]
    if not selected:
        selected = rows
    for row in selected:
        hits[_clean(row.get("case_id"))] = bool(int(_clean(row.get("final_pool_at_100")) or "0"))
    return hits, "loaded"


def _best_method(metrics_by_method: Sequence[Mapping[str, Any]]) -> str:
    if not metrics_by_method:
        return ""
    ordered = sorted(
        metrics_by_method,
        key=lambda item: (float(item.get("exact_at_100") or 0.0), float(item.get("mrr") or 0.0), float(item.get("exact_at_10") or 0.0)),
        reverse=True,
    )
    return _clean(ordered[0].get("method"))


def _comparison_rows(
    best_case_rows: Sequence[Mapping[str, Any]],
    phase7a_hits: Mapping[str, bool],
    phase8b_hits: Mapping[str, bool],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rescue_rows: list[dict[str, Any]] = []
    failure_rows: list[dict[str, Any]] = []
    for row in best_case_rows:
        historical_hit = bool(int(row["exact_at_100"]))
        phase7a_hit = phase7a_hits.get(_clean(row.get("case_id")))
        phase8b_hit = phase8b_hits.get(_clean(row.get("case_id")))
        output = {
            "method": row["method"],
            "case_id": row["case_id"],
            "expected_nandina": row["expected_nandina"],
            "descripcion": row["descripcion"],
            "hs2_ref": row["hs2_ref"],
            "hs4_ref": row["hs4_ref"],
            "exact_rank": row["exact_rank"],
            "historical_at_100": int(historical_hit),
            "phase7a_at_100": "" if phase7a_hit is None else int(phase7a_hit),
            "phase8b_at_100": "" if phase8b_hit is None else int(phase8b_hit),
            "top_candidate_nandina": row["top_candidate_nandina"],
            "top_candidate_case_id": row["top_candidate_case_id"],
        }
        if historical_hit and ((phase7a_hit is False) or (phase8b_hit is False)):
            rescue_rows.append(
                {
                    **output,
                    "rescued_vs_phase7a": "" if phase7a_hit is None else int(not phase7a_hit),
                    "rescued_vs_phase8b": "" if phase8b_hit is None else int(not phase8b_hit),
                }
            )
        if not historical_hit:
            failure_rows.append(output)
    rescue_rows.sort(key=lambda item: (str(item["hs2_ref"]), str(item["hs4_ref"]), int(item["exact_rank"] or 999999), str(item["case_id"])))
    failure_rows.sort(key=lambda item: (str(item["hs2_ref"]), str(item["hs4_ref"]), str(item["case_id"])))
    return rescue_rows, failure_rows


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Recuperacion historica leave-one-out v0.1",
        "",
        "## Alcance",
        "",
        "Cada fila de `evalset_v0.1.csv` se uso como consulta y las demas filas como indice historico. La fila consultada se excluye explicitamente del indice y los candidatos finales se deduplican por `nandina_ref`.",
        "",
        "## Metodos",
        "",
    ]
    for method in payload["methods_evaluated"]:
        method_metrics = payload["metrics_by_method"][method]
        lines.append(
            f"- `{method}`: Exact@1={method_metrics['exact_at_1']:.4f}; Exact@10={method_metrics['exact_at_10']:.4f}; Exact@100={method_metrics['exact_at_100']:.4f}; MRR={method_metrics['mrr']:.4f}; fuera Top-100={method_metrics['correct_not_in_top_100']}."
        )
    for skipped in payload["methods_skipped"]:
        lines.append(f"- `{skipped['method']}` omitido: {skipped['reason']}.")
    lines.extend(
        [
            "",
            "## Comparacion",
            "",
            f"- Fase 7A disponible: {payload['comparisons']['phase7a_status']}.",
            f"- Fase 8B disponible: {payload['comparisons']['phase8b_status']}.",
            f"- Casos rescatados por el mejor historico frente a Fase 7A/8B: {payload['comparisons']['rescue_cases']}."
            f"",
            f"- Casos que siguen fuera del Top-100 historico: {payload['comparisons']['failure_cases']}."
            f"",
            "",
            "## Politica",
            "",
            "No se invocaron modelos generativos, servicios locales de chat ni APIs remotas; la corrida usa solo texto tabular local.",
            "",
        ]
    )
    return "\n".join(lines)


def build(args: argparse.Namespace) -> dict[str, Any]:
    start = time.perf_counter()
    root = project_root()
    evalset_path = resolve_project_path(args.evalset)
    output_dir = resolve_project_path(args.output_dir)
    phase7a_path = resolve_project_path(args.phase7a_summary)
    phase8b_path = resolve_project_path(args.phase8b_summary)
    rows = _read_csv(evalset_path)
    if len(rows) != EXPECTED_ROWS:
        raise ValueError(f"Expected {EXPECTED_ROWS} evalset rows, found {len(rows)}")

    method_outputs = [_evaluate_bm25(rows, args.limit)]
    skipped: list[dict[str, str]] = []
    if _sklearn_available():
        method_outputs.append(_evaluate_tfidf(rows, args.limit))
    else:
        skipped.append({"method": METHOD_TFIDF, "reason": "scikit-learn is not available in the active local runtime; no installation was attempted"})

    all_candidate_rows: list[dict[str, Any]] = []
    all_case_rows: list[dict[str, Any]] = []
    metrics_rows: list[dict[str, Any]] = []
    metrics_by_method: dict[str, dict[str, Any]] = {}
    for output in method_outputs:
        all_candidate_rows.extend(output["candidate_rows"])
        all_case_rows.extend(output["case_rows"])
        metrics = _metrics_for_method(output["case_rows"], output["method"])
        metrics_rows.append(metrics)
        metrics_by_method[output["method"]] = metrics

    best = _best_method(metrics_rows)
    best_case_rows = [row for row in all_case_rows if row["method"] == best]
    phase7a_hits, phase7a_status = _baseline_hits(phase7a_path, "phase7a")
    phase8b_hits, phase8b_status = _baseline_hits(phase8b_path, "phase8b")
    rescue_rows, failure_rows = _comparison_rows(best_case_rows, phase7a_hits, phase8b_hits)
    self_matches = [row for row in all_candidate_rows if row["case_id"] == row["candidate_case_id"]]

    payload: dict[str, Any] = {
        "version": "v0.1",
        "phase": "9A",
        "dataset": _rel(evalset_path, root),
        "dataset_sha256": sha256_file(evalset_path),
        "output_dir": _rel(output_dir, root),
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "protocol": {
            "leave_one_out": True,
            "query_field": "descripcion",
            "label_field": "nandina_ref",
            "index_cases_per_query": len(rows) - 1,
            "dedupe_final_ranking_by": "nandina_ref",
            "candidate_limit": args.limit,
            "self_match_count": len(self_matches),
        },
        "methods_evaluated": [output["method"] for output in method_outputs],
        "methods_skipped": skipped,
        "metrics_by_method": metrics_by_method,
        "metrics_table": metrics_rows,
        "best_method_by_exact_at_100": best,
        "comparisons": {
            "phase7a_summary": _rel(phase7a_path, root),
            "phase7a_status": phase7a_status,
            "phase8b_summary": _rel(phase8b_path, root),
            "phase8b_status": phase8b_status,
            "rescue_cases": len(rescue_rows),
            "failure_cases": len(failure_rows),
        },
        "policy": {
            "generative_model_used": False,
            "local_chat_service_used": False,
            "remote_api_used": False,
            "network_access_required": False,
            "source_dataset_modified": False,
        },
        "outputs": {
            "historical_results_csv": _rel(output_dir / "historical_results.csv", root),
            "historical_metrics_json": _rel(output_dir / "historical_metrics.json", root),
            "historical_summary_md": _rel(output_dir / "historical_summary.md", root),
            "historical_case_summary_csv": _rel(output_dir / "historical_case_summary.csv", root),
            "historical_failure_cases_csv": _rel(output_dir / "historical_failure_cases.csv", root),
            "historical_rescue_cases_csv": _rel(output_dir / "historical_rescue_cases.csv", root),
        },
        "elapsed_seconds": time.perf_counter() - start,
    }

    candidate_fieldnames = [
        "case_id",
        "expected_nandina",
        "candidate_rank",
        "candidate_nandina",
        "candidate_case_id",
        "candidate_description",
        "score",
        "method",
    ]
    case_fieldnames = [
        "method",
        "case_id",
        "expected_nandina",
        "descripcion",
        "hs2_ref",
        "hs4_ref",
        "hs6_ref",
        "unique_candidates",
        "exact_rank",
        "hs6_first_rank",
        "hs4_first_rank",
        "hs2_first_rank",
        "reciprocal_rank",
        *[f"exact_at_{k}" for k in K_VALUES],
        *[f"hs6_at_{k}" for k in K_VALUES],
        *[f"hs4_at_{k}" for k in K_VALUES],
        *[f"hs2_at_{k}" for k in K_VALUES],
        "top_candidate_nandina",
        "top_candidate_case_id",
        "top_candidate_score",
        "self_match_detected",
    ]
    failure_fieldnames = [
        "method",
        "case_id",
        "expected_nandina",
        "descripcion",
        "hs2_ref",
        "hs4_ref",
        "exact_rank",
        "historical_at_100",
        "phase7a_at_100",
        "phase8b_at_100",
        "top_candidate_nandina",
        "top_candidate_case_id",
    ]
    rescue_fieldnames = [*failure_fieldnames, "rescued_vs_phase7a", "rescued_vs_phase8b"]

    _write_csv(output_dir / "historical_results.csv", all_candidate_rows, candidate_fieldnames)
    _write_csv(output_dir / "historical_case_summary.csv", all_case_rows, case_fieldnames)
    _write_csv(output_dir / "historical_failure_cases.csv", failure_rows, failure_fieldnames)
    _write_csv(output_dir / "historical_rescue_cases.csv", rescue_rows, rescue_fieldnames)
    _write_json(output_dir / "historical_metrics.json", payload)
    ensure_parent(output_dir / "historical_summary.md").write_text(_summary_markdown(payload), encoding="utf-8")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate historical-example retrieval with leave-one-out over evalset_v0.1.")
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET), help="Project-relative evalset CSV.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Project-relative output directory.")
    parser.add_argument("--phase7a-summary", default=str(DEFAULT_PHASE7A_SUMMARY), help="Optional Fase 7A case summary for comparison.")
    parser.add_argument("--phase8b-summary", default=str(DEFAULT_PHASE8B_SUMMARY), help="Optional Fase 8B case summary for comparison.")
    parser.add_argument("--limit", type=int, default=100, help="Maximum unique NANDINA candidates per case and method.")
    return parser


def main() -> int:
    payload = build(build_parser().parse_args())
    print(f"OK: Fase 9A historica evaluada sobre {payload['dataset']}")
    for method in payload["methods_evaluated"]:
        metrics = payload["metrics_by_method"][method]
        print(
            f"{method}: Exact@1={metrics['exact_at_1']:.4f} "
            f"Exact@10={metrics['exact_at_10']:.4f} "
            f"Exact@100={metrics['exact_at_100']:.4f} "
            f"MRR={metrics['mrr']:.4f}"
        )
    for skipped in payload["methods_skipped"]:
        print(f"OMITIDO {skipped['method']}: {skipped['reason']}")
    print(f"Outputs: {payload['output_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
