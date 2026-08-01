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
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_HISTORICAL = Path("data/processed/data_aduanas_historico_clase87_v0.1.csv")
DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.1.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1")

QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
METHOD = "historical_bm25_data_aduanas_clase87"
K_VALUES = [1, 3, 5, 10, 20, 50, 100]
HIERARCHICAL_K = [10, 50, 100]
EXPECTED_HISTORICAL_ROWS = 3000
EXPECTED_EVAL_ROWS = 1006
TOKEN_RE = re.compile(r"[a-z0-9]+")


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


def _median(values: Sequence[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def _normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text.lower())
    return "".join(char for char in normalized if not unicodedata.combining(char))


def _tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(_normalize_text(text))


def _valid_nandina(code: str) -> bool:
    return bool(re.fullmatch(r"\d{8}", _clean(code)))


def _support_bucket(count: int) -> str:
    if count <= 0:
        return "0"
    if count == 1:
        return "1"
    if count <= 4:
        return "2-4"
    if count <= 9:
        return "5-9"
    return "10+"


def _validate_rows(rows: Sequence[Mapping[str, str]], expected_rows: int, path: Path, split_name: str) -> None:
    if len(rows) != expected_rows:
        raise ValueError(f"{path} expected {expected_rows} rows, found {len(rows)}")
    for idx, row in enumerate(rows, start=1):
        if not _clean(row.get("id_unico")):
            raise ValueError(f"{split_name} row {idx} has empty id_unico")
        if not _valid_nandina(_clean(row.get(LABEL_COLUMN))):
            raise ValueError(f"{split_name} row {idx} has invalid NANDINA: {row.get(LABEL_COLUMN)}")
        if _clean(row.get("Clase")) != "87":
            raise ValueError(f"{split_name} row {idx} has Clase != 87")
        if not _clean(row.get(QUERY_COLUMN)):
            raise ValueError(f"{split_name} row {idx} has empty query column")


def _validate_no_overlap(historical_rows: Sequence[Mapping[str, str]], eval_rows: Sequence[Mapping[str, str]]) -> int:
    historical_ids = {_clean(row.get("id_unico")) for row in historical_rows}
    eval_ids = {_clean(row.get("id_unico")) for row in eval_rows}
    overlap = historical_ids & eval_ids
    if overlap:
        raise ValueError(f"Historical/eval id_unico overlap detected: {sorted(overlap)[:5]}")
    return 0


def _build_bm25_index(rows: Sequence[Mapping[str, str]]) -> dict[str, Any]:
    tokenized = [_tokenize(_clean(row.get(QUERY_COLUMN))) for row in rows]
    doc_lengths = [len(tokens) for tokens in tokenized]
    postings: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for doc_index, tokens in enumerate(tokenized):
        counter = Counter(tokens)
        for term, tf in counter.items():
            postings[term].append((doc_index, int(tf)))
    doc_freq = {term: len(term_postings) for term, term_postings in postings.items()}
    return {
        "postings": dict(postings),
        "doc_freq": doc_freq,
        "doc_lengths": doc_lengths,
        "avgdl": float(sum(doc_lengths) / len(doc_lengths)) if doc_lengths else 0.0,
        "doc_count": len(rows),
    }


def _bm25_scores(query: str, index: Mapping[str, Any], k1: float = 1.5, b: float = 0.75) -> dict[int, float]:
    query_counter = Counter(_tokenize(query))
    scores: dict[int, float] = defaultdict(float)
    doc_count = int(index["doc_count"])
    avgdl = float(index["avgdl"])
    postings = index["postings"]
    doc_freq = index["doc_freq"]
    doc_lengths = index["doc_lengths"]
    for term, query_tf in query_counter.items():
        term_postings = postings.get(term)
        if not term_postings:
            continue
        df = int(doc_freq.get(term, len(term_postings)))
        idf = math.log(1.0 + ((doc_count - df + 0.5) / (df + 0.5)))
        for doc_index, tf in term_postings:
            denominator = tf + k1 * (1.0 - b + b * (float(doc_lengths[doc_index]) / avgdl))
            scores[doc_index] += idf * (tf * (k1 + 1.0) / denominator) * float(query_tf)
    return dict(scores)


def _dedup_candidates(
    scores: Mapping[int, float],
    historical_rows: Sequence[Mapping[str, str]],
    history_depth: int,
    candidate_depth: int,
) -> list[dict[str, Any]]:
    ordered_docs = sorted(scores.items(), key=lambda item: (-float(item[1]), _clean(historical_rows[item[0]].get("case_id"))))[:history_depth]
    seen_codes: set[str] = set()
    candidates: list[dict[str, Any]] = []
    for doc_rank, (doc_index, score) in enumerate(ordered_docs, start=1):
        row = historical_rows[doc_index]
        code = _clean(row.get(LABEL_COLUMN))
        if not code or code in seen_codes:
            continue
        seen_codes.add(code)
        candidates.append(
            {
                "candidate_rank": len(candidates) + 1,
                "candidate_nandina": code,
                "candidate_history_rank": doc_rank,
                "candidate_case_id": _clean(row.get("case_id")),
                "candidate_id_unico": _clean(row.get("id_unico")),
                "candidate_partida": _clean(row.get("Partida")),
                "candidate_sub_partida": _clean(row.get("Sub Partida")),
                "candidate_clase": _clean(row.get("Clase")),
                "candidate_description": _clean(row.get(QUERY_COLUMN)),
                "score": float(score),
                "method": METHOD,
            }
        )
        if len(candidates) >= candidate_depth:
            break
    return candidates


def _rank_of(candidates: Sequence[Mapping[str, Any]], expected: str, field: str = "candidate_nandina") -> int:
    for rank, candidate in enumerate(candidates, start=1):
        if _clean(candidate.get(field)) == expected:
            return rank
    return 0


def _case_summary(row: Mapping[str, str], candidates: Sequence[Mapping[str, Any]], support_count: int) -> dict[str, Any]:
    expected = _clean(row.get(LABEL_COLUMN))
    expected_partida = _clean(row.get("Partida"))
    expected_sub_partida = _clean(row.get("Sub Partida"))
    expected_clase = _clean(row.get("Clase"))
    exact_rank = _rank_of(candidates, expected)
    partida_rank = _rank_of(candidates, expected_partida, "candidate_partida")
    sub_partida_rank = _rank_of(candidates, expected_sub_partida, "candidate_sub_partida")
    clase_rank = _rank_of(candidates, expected_clase, "candidate_clase")
    summary: dict[str, Any] = {
        "case_id": _clean(row.get("case_id")),
        "id_unico": _clean(row.get("id_unico")),
        "expected_nandina": expected,
        "expected_partida": expected_partida,
        "expected_sub_partida": expected_sub_partida,
        "expected_clase": expected_clase,
        "query": _clean(row.get(QUERY_COLUMN)),
        "historical_support_count": support_count,
        "support_bucket": _support_bucket(support_count),
        "nandina_present_in_history": int(support_count > 0),
        "unique_candidates": len(candidates),
        "exact_rank": exact_rank,
        "partida_first_rank": partida_rank,
        "sub_partida_first_rank": sub_partida_rank,
        "clase_first_rank": clase_rank,
        "reciprocal_rank": mrr_from_rank(exact_rank),
    }
    for k in K_VALUES:
        summary[f"exact_at_{k}"] = int(acc_at_k(exact_rank, k))
    for k in HIERARCHICAL_K:
        summary[f"partida_at_{k}"] = int(acc_at_k(partida_rank, k))
        summary[f"sub_partida_at_{k}"] = int(acc_at_k(sub_partida_rank, k))
        summary[f"clase_at_{k}"] = int(acc_at_k(clase_rank, k))
    return summary


def _candidate_rows(row: Mapping[str, str], candidates: Sequence[Mapping[str, Any]], support_count: int) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for candidate in candidates:
        output.append(
            {
                "case_id": _clean(row.get("case_id")),
                "id_unico": _clean(row.get("id_unico")),
                "expected_nandina": _clean(row.get(LABEL_COLUMN)),
                "expected_partida": _clean(row.get("Partida")),
                "expected_sub_partida": _clean(row.get("Sub Partida")),
                "expected_clase": _clean(row.get("Clase")),
                "historical_support_count": support_count,
                "support_bucket": _support_bucket(support_count),
                **candidate,
            }
        )
    return output


def _subset_metrics(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "cases": len(rows),
        "mrr": _mean([float(row["reciprocal_rank"]) for row in rows]),
        "median_exact_rank_nonzero": _median([float(row["exact_rank"]) for row in rows if int(row["exact_rank"]) > 0]),
    }
    for k in K_VALUES:
        payload[f"exact_at_{k}"] = _mean([float(row[f"exact_at_{k}"]) for row in rows])
    for k in HIERARCHICAL_K:
        payload[f"partida_at_{k}"] = _mean([float(row[f"partida_at_{k}"]) for row in rows])
        payload[f"sub_partida_at_{k}"] = _mean([float(row[f"sub_partida_at_{k}"]) for row in rows])
        payload[f"clase_at_{k}"] = _mean([float(row[f"clase_at_{k}"]) for row in rows])
    return payload


def _metrics(case_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    payload = _subset_metrics(case_rows)
    payload["cases_evaluated"] = len(case_rows)
    payload["cases_nandina_present_in_history"] = sum(1 for row in case_rows if int(row["nandina_present_in_history"]))
    payload["cases_nandina_absent_in_history"] = sum(1 for row in case_rows if not int(row["nandina_present_in_history"]))
    payload["by_history_presence"] = {
        "present": _subset_metrics([row for row in case_rows if int(row["nandina_present_in_history"])]),
        "absent": _subset_metrics([row for row in case_rows if not int(row["nandina_present_in_history"])]),
    }
    payload["by_support_bucket"] = {
        bucket: _subset_metrics([row for row in case_rows if row["support_bucket"] == bucket])
        for bucket in ["0", "1", "2-4", "5-9", "10+"]
    }
    return payload


def _support_rows(historical_rows: Sequence[Mapping[str, str]], case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    historical_counts = Counter(_clean(row.get(LABEL_COLUMN)) for row in historical_rows)
    grouped_eval: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in case_rows:
        grouped_eval[_clean(row.get("expected_nandina"))].append(row)
    output: list[dict[str, Any]] = []
    for code in sorted(grouped_eval):
        rows = grouped_eval[code]
        output.append(
            {
                "nandina": code,
                "historical_support_count": int(historical_counts.get(code, 0)),
                "support_bucket": _support_bucket(int(historical_counts.get(code, 0))),
                "eval_cases": len(rows),
                "recovered_at_100": sum(int(row["exact_at_100"]) for row in rows),
                "failures_at_100": sum(1 for row in rows if not int(row["exact_at_100"])),
                "recall_at_100": _mean([float(row["exact_at_100"]) for row in rows]),
                "mrr": _mean([float(row["reciprocal_rank"]) for row in rows]),
            }
        )
    output.sort(key=lambda item: (-int(item["failures_at_100"]), -int(item["eval_cases"]), item["nandina"]))
    return output


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    metrics = payload["metrics"]
    lines = [
        "# Recuperacion historica data_aduanas clase 87 v0.1",
        "",
        "## Resultado global",
        "",
        f"- Historico: {payload['input_rows']['historical']} instancias.",
        f"- Evalset: {payload['input_rows']['evalset']} instancias.",
        f"- Solapamiento `id_unico`: {payload['validation']['id_unico_overlap_count']}.",
        f"- NANDINA presente en historico: {metrics['cases_nandina_present_in_history']}.",
        f"- NANDINA ausente en historico: {metrics['cases_nandina_absent_in_history']}.",
        "",
        "| Metrica | Valor |",
        "| --- | ---: |",
        f"| Top-1 | {metrics['exact_at_1']:.4f} |",
        f"| Top-10 | {metrics['exact_at_10']:.4f} |",
        f"| Recall@100 | {metrics['exact_at_100']:.4f} |",
        f"| MRR | {metrics['mrr']:.4f} |",
        f"| Partida@100 | {metrics['partida_at_100']:.4f} |",
        f"| Sub Partida@100 | {metrics['sub_partida_at_100']:.4f} |",
        f"| Clase@100 | {metrics['clase_at_100']:.4f} |",
        "",
        "## Decision",
        "",
        payload["decision"],
        "",
        "No se uso LLM, Ollama, Text2Trade ni APIs remotas.",
        "",
    ]
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    started = time.perf_counter()
    root = project_root()
    historical_path = resolve_project_path(args.historical)
    eval_path = resolve_project_path(args.evalset)
    output_dir = resolve_project_path(args.output_dir)
    historical_rows = _read_csv(historical_path)
    eval_rows = _read_csv(eval_path)
    _validate_rows(historical_rows, EXPECTED_HISTORICAL_ROWS, historical_path, "historical")
    _validate_rows(eval_rows, EXPECTED_EVAL_ROWS, eval_path, "evalset")
    overlap_count = _validate_no_overlap(historical_rows, eval_rows)

    support_counts = Counter(_clean(row.get(LABEL_COLUMN)) for row in historical_rows)
    index = _build_bm25_index(historical_rows)
    candidate_rows: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []
    for row in eval_rows:
        support_count = int(support_counts.get(_clean(row.get(LABEL_COLUMN)), 0))
        scores = _bm25_scores(_clean(row.get(QUERY_COLUMN)), index)
        candidates = _dedup_candidates(scores, historical_rows, args.history_depth, args.candidate_depth)
        case_rows.append(_case_summary(row, candidates, support_count))
        candidate_rows.extend(_candidate_rows(row, candidates, support_count))

    metrics = _metrics(case_rows)
    support_by_nandina = _support_rows(historical_rows, case_rows)
    failure_rows = [row for row in case_rows if not int(row["exact_at_100"])]
    rescue_rows = [row for row in case_rows if int(row["exact_at_100"])]
    decision = (
        "La recuperacion historica real supera ampliamente el pool normativo Fase 7A a Top-100 y debe dominar como recuperador de candidatos cuando existe soporte historico; las NANDINAS sin soporte historico siguen requiriendo respaldo normativo en Fase 9B."
        if float(metrics["exact_at_100"]) > 0.3489
        else "La recuperacion historica real no supera el pool normativo Fase 7A a Top-100; Fase 9B debe tratarla como fuente auxiliar y no dominante."
    )

    payload: dict[str, Any] = {
        "version": "v0.1",
        "phase": "9A_data_aduanas_clase87",
        "method": METHOD,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": platform.python_version(), "platform": platform.platform()},
        "inputs": {
            "historical": _rel(historical_path, root),
            "historical_sha256": sha256_file(historical_path),
            "evalset": _rel(eval_path, root),
            "evalset_sha256": sha256_file(eval_path),
        },
        "input_rows": {"historical": len(historical_rows), "evalset": len(eval_rows)},
        "parameters": {"history_depth": args.history_depth, "candidate_depth": args.candidate_depth},
        "columns": {"query": QUERY_COLUMN, "label": LABEL_COLUMN},
        "validation": {
            "id_unico_overlap_count": overlap_count,
            "historical_queries_non_empty": True,
            "eval_queries_non_empty": True,
            "nandina8_labels_valid": True,
            "candidates_deduplicated_by_nandina": True,
            "llm_used": False,
            "ollama_used": False,
            "text2trade_used": False,
            "remote_api_used": False,
            "normative_bm25_used_as_candidate_source": False,
        },
        "metrics": metrics,
        "top_nandinas_with_most_failures": support_by_nandina[:15],
        "top_nandinas_with_best_retrieval": sorted(
            support_by_nandina,
            key=lambda item: (-float(item["recall_at_100"]), -int(item["eval_cases"]), item["nandina"]),
        )[:15],
        "comparison_reference": {
            "phase7a_normative_best_pool_at_100": 0.3489,
            "phase7a_normative_pool_at_200_80_20_70_30": 0.6272,
            "note": "Referencia metodologica reportada por Fase 7A actualizada; esta fase no usa BM25 normativo como fuente de candidatos.",
        },
        "decision": decision,
        "outputs": {
            "historical_results_csv": _rel(output_dir / "historical_results.csv", root),
            "historical_metrics_json": _rel(output_dir / "historical_metrics.json", root),
            "historical_summary_md": _rel(output_dir / "historical_summary.md", root),
            "historical_case_summary_csv": _rel(output_dir / "historical_case_summary.csv", root),
            "historical_failure_cases_csv": _rel(output_dir / "historical_failure_cases.csv", root),
            "historical_rescue_cases_csv": _rel(output_dir / "historical_rescue_cases.csv", root),
            "historical_support_by_nandina_csv": _rel(output_dir / "historical_support_by_nandina.csv", root),
        },
        "elapsed_seconds": time.perf_counter() - started,
    }

    candidate_fieldnames = [
        "case_id",
        "id_unico",
        "expected_nandina",
        "expected_partida",
        "expected_sub_partida",
        "expected_clase",
        "historical_support_count",
        "support_bucket",
        "candidate_rank",
        "candidate_nandina",
        "candidate_history_rank",
        "candidate_case_id",
        "candidate_id_unico",
        "candidate_partida",
        "candidate_sub_partida",
        "candidate_clase",
        "candidate_description",
        "score",
        "method",
    ]
    case_fieldnames = [
        "case_id",
        "id_unico",
        "expected_nandina",
        "expected_partida",
        "expected_sub_partida",
        "expected_clase",
        "query",
        "historical_support_count",
        "support_bucket",
        "nandina_present_in_history",
        "unique_candidates",
        "exact_rank",
        "partida_first_rank",
        "sub_partida_first_rank",
        "clase_first_rank",
        "reciprocal_rank",
        *[f"exact_at_{k}" for k in K_VALUES],
        *[f"partida_at_{k}" for k in HIERARCHICAL_K],
        *[f"sub_partida_at_{k}" for k in HIERARCHICAL_K],
        *[f"clase_at_{k}" for k in HIERARCHICAL_K],
    ]
    support_fieldnames = [
        "nandina",
        "historical_support_count",
        "support_bucket",
        "eval_cases",
        "recovered_at_100",
        "failures_at_100",
        "recall_at_100",
        "mrr",
    ]

    _write_csv(output_dir / "historical_results.csv", candidate_rows, candidate_fieldnames)
    _write_csv(output_dir / "historical_case_summary.csv", case_rows, case_fieldnames)
    _write_csv(output_dir / "historical_failure_cases.csv", failure_rows, case_fieldnames)
    _write_csv(output_dir / "historical_rescue_cases.csv", rescue_rows, case_fieldnames)
    _write_csv(output_dir / "historical_support_by_nandina.csv", support_by_nandina, support_fieldnames)
    _write_json(output_dir / "historical_metrics.json", payload)
    ensure_parent(output_dir / "historical_summary.md").write_text(_summary_markdown(payload), encoding="utf-8")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate real historical retrieval over data_aduanas class 87.")
    parser.add_argument("--historical", default=str(DEFAULT_HISTORICAL))
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--history-depth", type=int, default=500)
    parser.add_argument("--candidate-depth", type=int, default=100)
    return parser


def main() -> int:
    payload = evaluate(build_parser().parse_args())
    metrics = payload["metrics"]
    print("OK: recuperacion historica data_aduanas clase 87 evaluada")
    print(
        f"Top-1={metrics['exact_at_1']:.4f} Top-10={metrics['exact_at_10']:.4f} "
        f"Recall@100={metrics['exact_at_100']:.4f} MRR={metrics['mrr']:.4f}"
    )
    print(
        f"Partida@100={metrics['partida_at_100']:.4f} "
        f"SubPartida@100={metrics['sub_partida_at_100']:.4f} Clase@100={metrics['clase_at_100']:.4f}"
    )
    print(payload["decision"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
