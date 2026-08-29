from __future__ import annotations

import argparse
import csv
import importlib.metadata
import json
import math
import platform
import re
import statistics
import subprocess
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_HISTORICAL = Path("data/processed/data_aduanas_historico_clase87_v0.2.csv")
DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")
DEFAULT_SPLIT_METADATA = Path("data/processed/data_aduanas_splits_clase87_v0.2_metadata.json")
DEFAULT_SUPPORT_BY_EVAL_ROW = Path("outputs/audits/data_aduanas_splits_clase87_v0.2/historical_support_by_eval_row_v0.2.csv")
DEFAULT_EXACT_DUPLICATES = Path("outputs/audits/data_aduanas_splits_clase87_v0.2/exact_duplicates_cross_split_details_v0.2.csv")
DEFAULT_NEAR_DUPLICATES = Path("outputs/audits/data_aduanas_splits_clase87_v0.2/near_duplicates_hist_eval_details_v0.2.csv")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2")
DEFAULT_V01_METRICS = Path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/historical_metrics.json")

QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
METHOD = "historical_bm25_data_aduanas_clase87_v0.2"
EXPERIMENT_ID = "exp04_phase_a_historical_bm25_v0.2"
PHASE = "EXP-04_Fase_A_BM25_historico_v0.2"
EXPECTED_HISTORICAL_ROWS = 2950
EXPECTED_EVAL_ROWS = 1056
EXPECTED_EVAL_CODES = 42
EXPECTED_EVAL_SUPPORT_ROWS = 1056
EXPECTED_HISTORICAL_SHA256 = "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff"
EXPECTED_EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
EXPECTED_SUPPORT_BY_EVAL_ROW_SHA256 = "4fed0fe48a8d36718bb65e1adbb5eecce2ca671fbb5aa846bd22a2dc2762f385"
EXPECTED_EXACT_DUPLICATES_SHA256 = "691b094fbd4e6a142b235226abea27ba20897418b5929fa7dedcee48bc295525"
EXPECTED_NEAR_DUPLICATES_SHA256 = "0f1f0283c993dd57ab3e02ba064b8c964fd688777726f7ae80c04c47e9c9b955"
K_VALUES = [1, 3, 5, 10, 50]
HIERARCHICAL_K = [10, 50]
TOKEN_RE = re.compile(r"[a-z0-9]+")
CSV_ENCODING = "utf-8"


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
    with path.open("w", encoding=CSV_ENCODING, newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def _write_text(path: Path, text: str) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
        if not text.endswith("\n"):
            handle.write("\n")


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


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


def _series_support_bucket(count: int) -> str:
    if count == 1:
        return "1"
    if count <= 4:
        return "2-4"
    if count <= 9:
        return "5-9"
    return "10+"


def _dam_support_bucket(count: int) -> str:
    if count == 1:
        return "1 DAM"
    if count == 2:
        return "2 DAM"
    if count <= 4:
        return "3-4 DAM"
    return "5+ DAM"


def _position_bucket(rank: int) -> str:
    if rank == 1:
        return "1"
    if 2 <= rank <= 3:
        return "2-3"
    if 4 <= rank <= 5:
        return "4-5"
    if 6 <= rank <= 10:
        return "6-10"
    if 11 <= rank <= 50:
        return "11-50"
    return ">50_or_not_retrieved"


def _package_versions() -> dict[str, str]:
    versions: dict[str, str] = {}
    for package in ["pandas", "numpy"]:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = "not-installed"
    return versions


def _git_value(args: list[str], root: Path) -> str:
    try:
        result = subprocess.run(["git", *args], cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"
    return result.stdout.strip()


def _git_metadata(root: Path) -> dict[str, Any]:
    return {
        "branch": _git_value(["rev-parse", "--abbrev-ref", "HEAD"], root),
        "commit": _git_value(["rev-parse", "HEAD"], root),
        "dirty_status_short": _git_value(["status", "--short"], root).splitlines(),
    }


def _validate_hash(path: Path, expected: str, label: str) -> str:
    actual = sha256_file(path)
    if actual != expected:
        raise ValueError(f"{label} sha256 mismatch: expected {expected}, found {actual}")
    return actual


def _validate_rows(rows: Sequence[Mapping[str, str]], expected_rows: int, path: Path, split_name: str, prefix: str) -> None:
    if len(rows) != expected_rows:
        raise ValueError(f"{path} expected {expected_rows} rows, found {len(rows)}")
    case_ids: set[str] = set()
    for idx, row in enumerate(rows, start=1):
        case_id = _clean(row.get("case_id"))
        if not case_id.startswith(prefix):
            raise ValueError(f"{split_name} row {idx} has unexpected case_id prefix: {case_id}")
        if "V01" in case_id.upper() or "v0.1" in case_id.lower():
            raise ValueError(f"{split_name} row {idx} leaks v0.1 case_id: {case_id}")
        if case_id in case_ids:
            raise ValueError(f"{split_name} duplicate case_id: {case_id}")
        case_ids.add(case_id)
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

def _load_support_by_eval_case(path: Path, eval_case_ids: set[str]) -> dict[str, dict[str, Any]]:
    rows = _read_csv(path)
    if len(rows) != EXPECTED_EVAL_SUPPORT_ROWS:
        raise ValueError(f"Support audit expected {EXPECTED_EVAL_SUPPORT_ROWS} rows, found {len(rows)}")
    support: dict[str, dict[str, Any]] = {}
    for row in rows:
        case_id = _clean(row.get("case_id"))
        if case_id not in eval_case_ids:
            raise ValueError(f"Support audit case_id not in evalset: {case_id}")
        support[case_id] = {
            "support_count_series": int(_clean(row.get("support_count_series")) or 0),
            "support_count_dams": int(_clean(row.get("support_count_dams")) or 0),
            "support_bucket_audit": _clean(row.get("support_bucket")),
            "has_historical_support": _clean(row.get("has_historical_support")).lower() == "true",
        }
    if set(support) != eval_case_ids:
        missing = sorted(eval_case_ids - set(support))[:5]
        raise ValueError(f"Support audit missing eval case_id(s): {missing}")
    unsupported = [case_id for case_id, row in support.items() if not row["has_historical_support"]]
    if unsupported:
        raise ValueError(f"Expected all eval rows to have historical support; missing: {unsupported[:5]}")
    return support


def _load_exact_duplicate_flags(path: Path, eval_case_ids: set[str]) -> dict[str, dict[str, Any]]:
    flags = {
        case_id: {
            "exact_duplicate_cross_split": False,
            "exact_duplicate_same_nandina": False,
            "exact_duplicate_different_nandina": False,
            "exact_duplicate_pairs": 0,
        }
        for case_id in eval_case_ids
    }
    for row in _read_csv(path):
        if _clean(row.get("comparison")) != "historico-evaluacion":
            continue
        case_id = _clean(row.get("right_case_id"))
        if case_id not in flags:
            raise ValueError(f"Exact duplicate audit case_id not in evalset: {case_id}")
        same_nandina = _clean(row.get("same_nandina")).lower() == "true"
        flags[case_id]["exact_duplicate_cross_split"] = True
        flags[case_id]["exact_duplicate_pairs"] += 1
        if same_nandina:
            flags[case_id]["exact_duplicate_same_nandina"] = True
        else:
            flags[case_id]["exact_duplicate_different_nandina"] = True
    return flags


def _load_near_duplicate_flags(path: Path, eval_case_ids: set[str], threshold: float = 0.95) -> dict[str, dict[str, Any]]:
    flags = {
        case_id: {
            "near_duplicate_095": False,
            "near_duplicate_095_same_nandina": False,
            "near_duplicate_095_different_nandina": False,
            "near_duplicate_095_pairs": 0,
            "near_duplicate_095_max_jaccard": 0.0,
        }
        for case_id in eval_case_ids
    }
    for row in _read_csv(path):
        if _clean(row.get("comparison")) != "historico-evaluacion":
            continue
        jaccard = float(_clean(row.get("jaccard")) or 0.0)
        if jaccard < threshold:
            continue
        case_id = _clean(row.get("right_case_id"))
        if case_id not in flags:
            raise ValueError(f"Near duplicate audit case_id not in evalset: {case_id}")
        same_nandina = _clean(row.get("same_nandina")).lower() == "true"
        flags[case_id]["near_duplicate_095"] = True
        flags[case_id]["near_duplicate_095_pairs"] += 1
        flags[case_id]["near_duplicate_095_max_jaccard"] = max(flags[case_id]["near_duplicate_095_max_jaccard"], jaccard)
        if same_nandina:
            flags[case_id]["near_duplicate_095_same_nandina"] = True
        else:
            flags[case_id]["near_duplicate_095_different_nandina"] = True
    return flags


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


def _top1_error_family(expected: str, top1: str) -> str:
    if not top1:
        return "no_candidate"
    if expected[:6] == top1[:6]:
        return "same_sub_partida_6d"
    if expected[:4] == top1[:4]:
        return "same_partida_4d"
    if expected[:2] == top1[:2]:
        return "same_chapter_2d"
    return "different_chapter"


def _case_summary(
    row: Mapping[str, str],
    candidates: Sequence[Mapping[str, Any]],
    support: Mapping[str, Any],
    duplicate_flags: Mapping[str, Any],
    near_flags: Mapping[str, Any],
) -> dict[str, Any]:
    expected = _clean(row.get(LABEL_COLUMN))
    expected_partida = _clean(row.get("Partida"))
    expected_sub_partida = _clean(row.get("Sub Partida"))
    expected_clase = _clean(row.get("Clase"))
    exact_rank = _rank_of(candidates, expected)
    partida_rank = _rank_of(candidates, expected_partida, "candidate_partida")
    sub_partida_rank = _rank_of(candidates, expected_sub_partida, "candidate_sub_partida")
    clase_rank = _rank_of(candidates, expected_clase, "candidate_clase")
    top1 = _clean(candidates[0].get("candidate_nandina")) if candidates else ""
    summary: dict[str, Any] = {
        "case_id": _clean(row.get("case_id")),
        "id_unico": _clean(row.get("id_unico")),
        "declaracion": _clean(row.get("DECLARACION")),
        "serie": _clean(row.get("SERIE")),
        "expected_nandina": expected,
        "expected_partida": expected_partida,
        "expected_sub_partida": expected_sub_partida,
        "expected_clase": expected_clase,
        "query": _clean(row.get(QUERY_COLUMN)),
        "support_count_series": int(support["support_count_series"]),
        "support_count_dams": int(support["support_count_dams"]),
        "support_bucket_series": _series_support_bucket(int(support["support_count_series"])),
        "support_bucket_dams": _dam_support_bucket(int(support["support_count_dams"])),
        "support_bucket_audit": _clean(support["support_bucket_audit"]),
        "nandina_present_in_history": int(bool(support["has_historical_support"])),
        "unique_candidates": len(candidates),
        "top1_nandina": top1,
        "top1_error_family": "correct" if exact_rank == 1 else _top1_error_family(expected, top1),
        "exact_rank": exact_rank,
        "position_bucket": _position_bucket(exact_rank),
        "partida_first_rank": partida_rank,
        "sub_partida_first_rank": sub_partida_rank,
        "clase_first_rank": clase_rank,
        "reciprocal_rank": mrr_from_rank(exact_rank),
        **duplicate_flags,
        **near_flags,
    }
    for k in K_VALUES:
        summary[f"exact_at_{k}"] = int(acc_at_k(exact_rank, k))
    for k in HIERARCHICAL_K:
        summary[f"partida_at_{k}"] = int(acc_at_k(partida_rank, k))
        summary[f"sub_partida_at_{k}"] = int(acc_at_k(sub_partida_rank, k))
        summary[f"clase_at_{k}"] = int(acc_at_k(clase_rank, k))
    return summary

def _candidate_rows(row: Mapping[str, str], candidates: Sequence[Mapping[str, Any]], support: Mapping[str, Any]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for candidate in candidates:
        output.append(
            {
                "case_id": _clean(row.get("case_id")),
                "id_unico": _clean(row.get("id_unico")),
                "declaracion": _clean(row.get("DECLARACION")),
                "serie": _clean(row.get("SERIE")),
                "expected_nandina": _clean(row.get(LABEL_COLUMN)),
                "expected_partida": _clean(row.get("Partida")),
                "expected_sub_partida": _clean(row.get("Sub Partida")),
                "expected_clase": _clean(row.get("Clase")),
                "support_count_series": int(support["support_count_series"]),
                "support_count_dams": int(support["support_count_dams"]),
                "support_bucket_series": _series_support_bucket(int(support["support_count_series"])),
                "support_bucket_dams": _dam_support_bucket(int(support["support_count_dams"])),
                **candidate,
            }
        )
    return output


def _metric_row(name: str, numerator: float, denominator: int, value: float | None = None) -> dict[str, Any]:
    computed = float(numerator / denominator) if denominator else 0.0
    return {
        "metric": name,
        "numerator": numerator,
        "denominator": denominator,
        "value": computed if value is None else float(value),
    }


def _subset_metric_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    denominator = len(rows)
    metric_rows = [
        _metric_row("mrr", sum(float(row["reciprocal_rank"]) for row in rows), denominator),
    ]
    for k in K_VALUES:
        metric_rows.append(_metric_row(f"exact_at_{k}", sum(int(row[f"exact_at_{k}"]) for row in rows), denominator))
    for k in HIERARCHICAL_K:
        metric_rows.append(_metric_row(f"partida_at_{k}", sum(int(row[f"partida_at_{k}"]) for row in rows), denominator))
        metric_rows.append(_metric_row(f"sub_partida_at_{k}", sum(int(row[f"sub_partida_at_{k}"]) for row in rows), denominator))
        metric_rows.append(_metric_row(f"clase_at_{k}", sum(int(row[f"clase_at_{k}"]) for row in rows), denominator))
    return metric_rows


def _subset_metrics(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    metric_rows = _subset_metric_rows(rows)
    payload: dict[str, Any] = {row["metric"]: row["value"] for row in metric_rows}
    for row in metric_rows:
        payload[f"{row['metric']}_numerator"] = row["numerator"]
        payload[f"{row['metric']}_denominator"] = row["denominator"]
    payload["cases"] = len(rows)
    payload["median_exact_rank_nonzero"] = _median([float(row["exact_rank"]) for row in rows if int(row["exact_rank"]) > 0])
    return payload


def _metrics(case_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    payload = _subset_metrics(case_rows)
    payload["cases_evaluated"] = len(case_rows)
    payload["cases_nandina_present_in_history"] = sum(1 for row in case_rows if int(row["nandina_present_in_history"]))
    payload["cases_nandina_absent_in_history"] = sum(1 for row in case_rows if not int(row["nandina_present_in_history"]))
    payload["cases_with_at_least_50_candidates"] = sum(1 for row in case_rows if int(row["unique_candidates"]) >= 50)
    payload["min_unique_candidates"] = min((int(row["unique_candidates"]) for row in case_rows), default=0)
    payload["max_unique_candidates"] = max((int(row["unique_candidates"]) for row in case_rows), default=0)
    payload["metric_table"] = _subset_metric_rows(case_rows)
    return payload


def _metrics_by_group(case_rows: Sequence[Mapping[str, Any]], group_name: str, group_values: Sequence[tuple[str, Sequence[Mapping[str, Any]]]]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for value, rows in group_values:
        metrics = _subset_metrics(rows)
        output.append(
            {
                "group": group_name,
                "value": value,
                "cases": len(rows),
                "mrr": metrics["mrr"],
                **{f"exact_at_{k}": metrics[f"exact_at_{k}"] for k in K_VALUES},
                **{f"exact_at_{k}_numerator": metrics[f"exact_at_{k}_numerator"] for k in K_VALUES},
                **{f"exact_at_{k}_denominator": metrics[f"exact_at_{k}_denominator"] for k in K_VALUES},
            }
        )
    return output


def _position_distribution(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    total = len(case_rows)
    order = ["1", "2-3", "4-5", "6-10", "11-50", ">50_or_not_retrieved"]
    counts = Counter(_clean(row.get("position_bucket")) for row in case_rows)
    return [{"position_bucket": bucket, "cases": int(counts.get(bucket, 0)), "pct": float(counts.get(bucket, 0) / total) if total else 0.0} for bucket in order]


def _support_series_rows(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    order = ["1", "2-4", "5-9", "10+"]
    return _metrics_by_group(
        case_rows,
        "support_count_series",
        [(bucket, [row for row in case_rows if row["support_bucket_series"] == bucket]) for bucket in order],
    )


def _support_dam_rows(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    order = ["1 DAM", "2 DAM", "3-4 DAM", "5+ DAM"]
    return _metrics_by_group(
        case_rows,
        "support_count_dams",
        [(bucket, [row for row in case_rows if row["support_bucket_dams"] == bucket]) for bucket in order],
    )


def _exact_duplicate_sensitivity(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    groups = [
        ("exact_duplicate_present", [row for row in case_rows if bool(row["exact_duplicate_cross_split"])]),
        ("exact_duplicate_absent", [row for row in case_rows if not bool(row["exact_duplicate_cross_split"])]),
        ("exact_duplicate_same_nandina", [row for row in case_rows if bool(row["exact_duplicate_same_nandina"])]),
        ("exact_duplicate_different_nandina", [row for row in case_rows if bool(row["exact_duplicate_different_nandina"])]),
    ]
    return _metrics_by_group(case_rows, "exact_duplicate_cross_split", groups)


def _near_duplicate_sensitivity(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    groups = [
        ("near_duplicate_095_present", [row for row in case_rows if bool(row["near_duplicate_095"])]),
        ("near_duplicate_095_absent", [row for row in case_rows if not bool(row["near_duplicate_095"])]),
        ("near_duplicate_095_same_nandina", [row for row in case_rows if bool(row["near_duplicate_095_same_nandina"])]),
        ("near_duplicate_095_different_nandina", [row for row in case_rows if bool(row["near_duplicate_095_different_nandina"])]),
    ]
    return _metrics_by_group(case_rows, "near_duplicate_095", groups)


def _hierarchical_error_rows(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    error_rows = [row for row in case_rows if int(row["exact_at_1"]) == 0]
    total_errors = len(error_rows)
    counts = Counter(_clean(row.get("top1_error_family")) for row in error_rows)
    order = ["same_sub_partida_6d", "same_partida_4d", "same_chapter_2d", "different_chapter", "no_candidate"]
    return [
        {
            "top1_error_family": family,
            "errors": int(counts.get(family, 0)),
            "pct_of_top1_errors": float(counts.get(family, 0) / total_errors) if total_errors else 0.0,
            "pct_of_all_cases": float(counts.get(family, 0) / len(case_rows)) if case_rows else 0.0,
        }
        for family in order
    ]


def _support_by_nandina(historical_rows: Sequence[Mapping[str, str]], case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    historical_counts = Counter(_clean(row.get(LABEL_COLUMN)) for row in historical_rows)
    grouped_eval: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in case_rows:
        grouped_eval[_clean(row.get("expected_nandina"))].append(row)
    output: list[dict[str, Any]] = []
    for code in sorted(grouped_eval):
        rows = grouped_eval[code]
        metrics = _subset_metrics(rows)
        output.append(
            {
                "nandina": code,
                "historical_support_count_series": int(historical_counts.get(code, 0)),
                "eval_cases": len(rows),
                "recovered_at_50": int(metrics["exact_at_50_numerator"]),
                "failures_at_50": len(rows) - int(metrics["exact_at_50_numerator"]),
                "exact_at_1": metrics["exact_at_1"],
                "exact_at_10": metrics["exact_at_10"],
                "exact_at_50": metrics["exact_at_50"],
                "mrr": metrics["mrr"],
            }
        )
    output.sort(key=lambda item: (-int(item["failures_at_50"]), -int(item["eval_cases"]), item["nandina"]))
    return output


def _comparison_v01_v02(v01_metrics_path: Path, v02_metrics: Mapping[str, Any]) -> list[dict[str, Any]]:
    metrics = ["mrr", "exact_at_1", "exact_at_3", "exact_at_5", "exact_at_10", "exact_at_50", "partida_at_10", "sub_partida_at_10", "clase_at_10", "partida_at_50", "sub_partida_at_50", "clase_at_50"]
    if not v01_metrics_path.exists():
        return [{"metric": metric, "bm25_historical_v0_1": "missing", "bm25_historical_v0_2": v02_metrics.get(metric, ""), "delta_v02_minus_v01": ""} for metric in metrics]
    v01_payload = _read_json(v01_metrics_path)
    v01_metrics = v01_payload.get("metrics", {})
    rows: list[dict[str, Any]] = []
    for metric in metrics:
        old = float(v01_metrics.get(metric, 0.0))
        new = float(v02_metrics.get(metric, 0.0))
        rows.append({"metric": metric, "bm25_historical_v0_1": old, "bm25_historical_v0_2": new, "delta_v02_minus_v01": new - old})
    return rows

def _summary_markdown(payload: Mapping[str, Any]) -> str:
    metrics = payload["metrics"]
    rows = metrics["metric_table"]
    metric_lines = ["| Metrica | Numerador | Denominador | Valor |", "| --- | ---: | ---: | ---: |"]
    for row in rows:
        metric_lines.append(f"| {row['metric']} | {row['numerator']} | {row['denominator']} | {float(row['value']):.6f} |")
    lines = [
        "# EXP-04 Fase A - BM25 historico data_aduanas clase 87 v0.2",
        "",
        "## Alcance",
        "",
        "Se evaluo exclusivamente BM25 historico sobre el split congelado v0.2. No se uso BM25 normativo, BM25 jerarquico, Text2Trade, pools hibridos, RAG, reranking LLM, explicador LLM ni APIs remotas.",
        "",
        "## Validacion de entrada",
        "",
        f"- Historico v0.2: {payload['input_rows']['historical']} series, sha256 `{payload['inputs']['historical_sha256']}`.",
        f"- Evaluacion v0.2: {payload['input_rows']['evalset']} series, sha256 `{payload['inputs']['evalset_sha256']}`.",
        f"- Codigos NANDINA en evaluacion: {payload['validation']['eval_unique_nandina_codes']}.",
        f"- Casos de evaluacion con soporte historico: {payload['validation']['eval_cases_with_historical_support']}.",
        f"- Solapamiento `id_unico` historico/evaluacion: {payload['validation']['id_unico_overlap_count']}.",
        f"- Profundidad Top-50 habilitada: {payload['validation']['candidate_depth_supports_top_50']}.",
        "",
        "## Resultado global",
        "",
        *metric_lines,
        "",
        "## Duplicados y soporte",
        "",
        f"- Casos con duplicado exacto historico-evaluacion: {payload['validation']['eval_cases_with_exact_duplicate']}.",
        f"- Casos con near duplicate historico-evaluacion >=0.95: {payload['validation']['eval_cases_with_near_duplicate_095']}.",
        f"- Casos con al menos 50 candidatos BM25 unicos: {metrics['cases_with_at_least_50_candidates']}.",
        "",
        "## Decision",
        "",
        payload["decision"],
        "",
    ]
    return "\n".join(lines)


def _fieldnames_from(rows: Sequence[Mapping[str, Any]], preferred: Sequence[str]) -> list[str]:
    fields = list(preferred)
    seen = set(fields)
    for row in rows:
        for key in row:
            if key not in seen:
                fields.append(key)
                seen.add(key)
    return fields


def _output_paths(output_dir: Path) -> dict[str, Path]:
    return {
        "historical_results_csv": output_dir / "historical_results.csv",
        "historical_case_summary_csv": output_dir / "historical_case_summary.csv",
        "historical_failure_cases_csv": output_dir / "historical_failure_cases.csv",
        "historical_rescue_cases_csv": output_dir / "historical_rescue_cases.csv",
        "historical_support_by_nandina_csv": output_dir / "historical_support_by_nandina.csv",
        "position_distribution_csv": output_dir / "position_distribution.csv",
        "metrics_by_support_count_series_csv": output_dir / "metrics_by_support_count_series.csv",
        "metrics_by_support_count_dams_csv": output_dir / "metrics_by_support_count_dams.csv",
        "sensitivity_exact_duplicates_csv": output_dir / "sensitivity_exact_duplicates.csv",
        "sensitivity_near_duplicates_095_csv": output_dir / "sensitivity_near_duplicates_095.csv",
        "hierarchical_error_top1_csv": output_dir / "hierarchical_error_top1.csv",
        "comparison_bm25_historical_v0_1_v0_2_csv": output_dir / "comparison_bm25_historical_v0.1_v0.2.csv",
        "historical_metrics_json": output_dir / "historical_metrics.json",
        "run_metadata_json": output_dir / "run_metadata.json",
        "historical_summary_md": output_dir / "historical_summary.md",
    }


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    started = time.perf_counter()
    if args.candidate_depth < 50:
        raise ValueError("candidate_depth must be >= 50 for EXP-04 Fase A Top-50 reporting")
    root = project_root()
    historical_path = resolve_project_path(args.historical)
    eval_path = resolve_project_path(args.evalset)
    metadata_path = resolve_project_path(args.split_metadata)
    support_path = resolve_project_path(args.support_by_eval_row)
    exact_path = resolve_project_path(args.exact_duplicates)
    near_path = resolve_project_path(args.near_duplicates)
    v01_metrics_path = resolve_project_path(args.v01_metrics)
    output_dir = resolve_project_path(args.output_dir)

    path_strings = [str(args.historical), str(args.evalset), str(args.split_metadata), str(args.support_by_eval_row), str(args.exact_duplicates), str(args.near_duplicates)]
    if any("v0.1" in value.lower() for value in path_strings):
        raise ValueError("EXP-04 Fase A v0.2 cannot consume v0.1 split or audit inputs")

    historical_sha = _validate_hash(historical_path, EXPECTED_HISTORICAL_SHA256, "historical v0.2")
    eval_sha = _validate_hash(eval_path, EXPECTED_EVAL_SHA256, "evalset v0.2")
    support_sha = _validate_hash(support_path, EXPECTED_SUPPORT_BY_EVAL_ROW_SHA256, "support audit v0.2")
    exact_sha = _validate_hash(exact_path, EXPECTED_EXACT_DUPLICATES_SHA256, "exact duplicates audit v0.2")
    near_sha = _validate_hash(near_path, EXPECTED_NEAR_DUPLICATES_SHA256, "near duplicates audit v0.2")
    metadata_sha = sha256_file(metadata_path)
    split_metadata = _read_json(metadata_path)
    if split_metadata.get("version") != "v0.2":
        raise ValueError("Split metadata is not v0.2")
    if split_metadata.get("output_sha256", {}).get("data/processed/data_aduanas_historico_clase87_v0.2.csv") != historical_sha:
        raise ValueError("Split metadata historical hash does not match locked v0.2 input")
    if split_metadata.get("output_sha256", {}).get("data/processed/data_aduanas_evalset_clase87_v0.2.csv") != eval_sha:
        raise ValueError("Split metadata eval hash does not match locked v0.2 input")

    historical_rows = _read_csv(historical_path)
    eval_rows = _read_csv(eval_path)
    _validate_rows(historical_rows, EXPECTED_HISTORICAL_ROWS, historical_path, "historical", "DA-HIST-V02-")
    _validate_rows(eval_rows, EXPECTED_EVAL_ROWS, eval_path, "evalset", "DA-EVAL-V02-")
    overlap_count = _validate_no_overlap(historical_rows, eval_rows)
    eval_case_ids = {_clean(row.get("case_id")) for row in eval_rows}
    eval_codes = {_clean(row.get(LABEL_COLUMN)) for row in eval_rows}
    if len(eval_case_ids) != EXPECTED_EVAL_ROWS:
        raise ValueError("Eval case_id count is not unique")
    if len(eval_codes) != EXPECTED_EVAL_CODES:
        raise ValueError(f"Evalset expected {EXPECTED_EVAL_CODES} unique NANDINA codes, found {len(eval_codes)}")

    support_by_case = _load_support_by_eval_case(support_path, eval_case_ids)
    exact_flags = _load_exact_duplicate_flags(exact_path, eval_case_ids)
    near_flags = _load_near_duplicate_flags(near_path, eval_case_ids)
    if sum(1 for row in support_by_case.values() if row["has_historical_support"]) != EXPECTED_EVAL_SUPPORT_ROWS:
        raise ValueError("Expected 1056 eval rows with historical support")

    index = _build_bm25_index(historical_rows)
    candidate_rows: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []
    for row in eval_rows:
        case_id = _clean(row.get("case_id"))
        scores = _bm25_scores(_clean(row.get(QUERY_COLUMN)), index)
        candidates = _dedup_candidates(scores, historical_rows, args.history_depth, args.candidate_depth)
        case_rows.append(_case_summary(row, candidates, support_by_case[case_id], exact_flags[case_id], near_flags[case_id]))
        candidate_rows.extend(_candidate_rows(row, candidates, support_by_case[case_id]))

    metrics = _metrics(case_rows)
    position_rows = _position_distribution(case_rows)
    support_series_rows = _support_series_rows(case_rows)
    support_dam_rows = _support_dam_rows(case_rows)
    exact_sensitivity_rows = _exact_duplicate_sensitivity(case_rows)
    near_sensitivity_rows = _near_duplicate_sensitivity(case_rows)
    hierarchy_error_rows = _hierarchical_error_rows(case_rows)
    support_by_nandina = _support_by_nandina(historical_rows, case_rows)
    comparison_rows = _comparison_v01_v02(v01_metrics_path, metrics)
    failure_rows = [row for row in case_rows if not int(row["exact_at_50"])]
    rescue_rows = [row for row in case_rows if int(row["exact_at_50"])]

    decision = (
        "BM25 historico v0.2 mantiene una recuperacion fuerte sobre evaluacion v0.2 y queda habilitado como baseline historico congelado para comparaciones posteriores, sin activar componentes normativos ni LLM."
        if float(metrics["exact_at_50"]) >= 0.95
        else "BM25 historico v0.2 queda registrado como baseline, pero requiere comparacion cuidadosa antes de usarse como fuente dominante."
    )

    outputs = _output_paths(output_dir)
    payload: dict[str, Any] = {
        "version": "v0.2",
        "experiment_id": EXPERIMENT_ID,
        "phase": PHASE,
        "method": METHOD,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": platform.python_version(), "platform": platform.platform(), "packages": _package_versions()},
        "git": _git_metadata(root),
        "command": " ".join(sys.argv),
        "inputs": {
            "historical": _rel(historical_path, root),
            "historical_sha256": historical_sha,
            "evalset": _rel(eval_path, root),
            "evalset_sha256": eval_sha,
            "split_metadata": _rel(metadata_path, root),
            "split_metadata_sha256": metadata_sha,
            "split_config": split_metadata.get("config_file", ""),
            "split_config_sha256": split_metadata.get("config_sha256", ""),
            "support_by_eval_row": _rel(support_path, root),
            "support_by_eval_row_sha256": support_sha,
            "exact_duplicates": _rel(exact_path, root),
            "exact_duplicates_sha256": exact_sha,
            "near_duplicates": _rel(near_path, root),
            "near_duplicates_sha256": near_sha,
            "v01_historical_metrics_reference": _rel(v01_metrics_path, root),
        },
        "input_rows": {"historical": len(historical_rows), "evalset": len(eval_rows)},
        "parameters": {"history_depth": args.history_depth, "candidate_depth": args.candidate_depth, "k1": 1.5, "b": 0.75},
        "columns": {"query": QUERY_COLUMN, "label": LABEL_COLUMN},
        "validation": {
            "id_unico_overlap_count": overlap_count,
            "eval_case_ids_unique": len(eval_case_ids) == len(eval_rows),
            "eval_case_id_prefix": "DA-EVAL-V02-",
            "historical_case_id_prefix": "DA-HIST-V02-",
            "v01_case_ids_detected": 0,
            "eval_unique_nandina_codes": len(eval_codes),
            "eval_cases_with_historical_support": sum(1 for row in support_by_case.values() if row["has_historical_support"]),
            "candidate_depth_supports_top_50": args.candidate_depth >= 50,
            "cases_with_at_least_50_candidates": metrics["cases_with_at_least_50_candidates"],
            "eval_cases_with_exact_duplicate": sum(1 for row in case_rows if bool(row["exact_duplicate_cross_split"])),
            "eval_cases_with_near_duplicate_095": sum(1 for row in case_rows if bool(row["near_duplicate_095"])),
            "metrics_recomputed_from_case_summary": True,
            "historical_queries_non_empty": True,
            "eval_queries_non_empty": True,
            "nandina8_labels_valid": True,
            "candidates_deduplicated_by_nandina": True,
            "llm_used": False,
            "ollama_used": False,
            "text2trade_used": False,
            "remote_api_used": False,
            "normative_bm25_used_as_candidate_source": False,
            "hierarchical_bm25_used_as_candidate_source": False,
        },
        "metrics": metrics,
        "position_distribution": position_rows,
        "metrics_by_support_count_series": support_series_rows,
        "metrics_by_support_count_dams": support_dam_rows,
        "sensitivity_exact_duplicates": exact_sensitivity_rows,
        "sensitivity_near_duplicates_095": near_sensitivity_rows,
        "hierarchical_error_top1": hierarchy_error_rows,
        "comparison_bm25_historical_v0_1_v0_2": comparison_rows,
        "top_nandinas_with_most_failures_at_50": support_by_nandina[:15],
        "decision": decision,
        "outputs": {name: _rel(path, root) for name, path in outputs.items()},
        "elapsed_seconds": time.perf_counter() - started,
    }

    candidate_fieldnames = [
        "case_id", "id_unico", "declaracion", "serie", "expected_nandina", "expected_partida", "expected_sub_partida", "expected_clase",
        "support_count_series", "support_count_dams", "support_bucket_series", "support_bucket_dams", "candidate_rank", "candidate_nandina",
        "candidate_history_rank", "candidate_case_id", "candidate_id_unico", "candidate_partida", "candidate_sub_partida", "candidate_clase", "candidate_description", "score", "method",
    ]
    case_fieldnames = [
        "case_id", "id_unico", "declaracion", "serie", "expected_nandina", "expected_partida", "expected_sub_partida", "expected_clase", "query",
        "support_count_series", "support_count_dams", "support_bucket_series", "support_bucket_dams", "support_bucket_audit", "nandina_present_in_history",
        "unique_candidates", "top1_nandina", "top1_error_family", "exact_rank", "position_bucket", "partida_first_rank", "sub_partida_first_rank", "clase_first_rank", "reciprocal_rank",
        "exact_duplicate_cross_split", "exact_duplicate_same_nandina", "exact_duplicate_different_nandina", "exact_duplicate_pairs",
        "near_duplicate_095", "near_duplicate_095_same_nandina", "near_duplicate_095_different_nandina", "near_duplicate_095_pairs", "near_duplicate_095_max_jaccard",
        *[f"exact_at_{k}" for k in K_VALUES], *[f"partida_at_{k}" for k in HIERARCHICAL_K], *[f"sub_partida_at_{k}" for k in HIERARCHICAL_K], *[f"clase_at_{k}" for k in HIERARCHICAL_K],
    ]
    metrics_group_fields = ["group", "value", "cases", "mrr", *[f"exact_at_{k}" for k in K_VALUES], *[f"exact_at_{k}_numerator" for k in K_VALUES], *[f"exact_at_{k}_denominator" for k in K_VALUES]]

    _write_csv(outputs["historical_results_csv"], candidate_rows, candidate_fieldnames)
    _write_csv(outputs["historical_case_summary_csv"], case_rows, case_fieldnames)
    _write_csv(outputs["historical_failure_cases_csv"], failure_rows, case_fieldnames)
    _write_csv(outputs["historical_rescue_cases_csv"], rescue_rows, case_fieldnames)
    _write_csv(outputs["historical_support_by_nandina_csv"], support_by_nandina, _fieldnames_from(support_by_nandina, []))
    _write_csv(outputs["position_distribution_csv"], position_rows, ["position_bucket", "cases", "pct"])
    _write_csv(outputs["metrics_by_support_count_series_csv"], support_series_rows, metrics_group_fields)
    _write_csv(outputs["metrics_by_support_count_dams_csv"], support_dam_rows, metrics_group_fields)
    _write_csv(outputs["sensitivity_exact_duplicates_csv"], exact_sensitivity_rows, metrics_group_fields)
    _write_csv(outputs["sensitivity_near_duplicates_095_csv"], near_sensitivity_rows, metrics_group_fields)
    _write_csv(outputs["hierarchical_error_top1_csv"], hierarchy_error_rows, ["top1_error_family", "errors", "pct_of_top1_errors", "pct_of_all_cases"])
    _write_csv(outputs["comparison_bm25_historical_v0_1_v0_2_csv"], comparison_rows, ["metric", "bm25_historical_v0_1", "bm25_historical_v0_2", "delta_v02_minus_v01"])
    _write_json(outputs["historical_metrics_json"], payload)
    _write_text(outputs["historical_summary_md"], _summary_markdown(payload))

    run_metadata = {
        "experiment_id": EXPERIMENT_ID,
        "phase": PHASE,
        "created_at_utc": payload["created_at_utc"],
        "git": payload["git"],
        "command": payload["command"],
        "inputs": payload["inputs"],
        "outputs": payload["outputs"],
        "output_sha256": {
            name: sha256_file(path)
            for name, path in outputs.items()
            if name != "run_metadata_json" and path.exists()
        },
        "validation": payload["validation"],
        "parameters": payload["parameters"],
        "elapsed_seconds": payload["elapsed_seconds"],
    }
    _write_json(outputs["run_metadata_json"], run_metadata)
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate BM25 historical retrieval over data_aduanas class 87 v0.2.")
    parser.add_argument("--historical", default=str(DEFAULT_HISTORICAL))
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET))
    parser.add_argument("--split-metadata", default=str(DEFAULT_SPLIT_METADATA))
    parser.add_argument("--support-by-eval-row", default=str(DEFAULT_SUPPORT_BY_EVAL_ROW))
    parser.add_argument("--exact-duplicates", default=str(DEFAULT_EXACT_DUPLICATES))
    parser.add_argument("--near-duplicates", default=str(DEFAULT_NEAR_DUPLICATES))
    parser.add_argument("--v01-metrics", default=str(DEFAULT_V01_METRICS))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--history-depth", type=int, default=EXPECTED_HISTORICAL_ROWS)
    parser.add_argument("--candidate-depth", type=int, default=100)
    return parser


def main() -> int:
    payload = evaluate(build_parser().parse_args())
    metrics = payload["metrics"]
    print("OK: EXP-04 Fase A BM25 historico v0.2 evaluado")
    print(
        f"Top-1={metrics['exact_at_1']:.4f} Top-10={metrics['exact_at_10']:.4f} "
        f"Top-50={metrics['exact_at_50']:.4f} MRR={metrics['mrr']:.4f}"
    )
    print(
        f"Partida@50={metrics['partida_at_50']:.4f} "
        f"SubPartida@50={metrics['sub_partida_at_50']:.4f} Clase@50={metrics['clase_at_50']:.4f}"
    )
    print(payload["decision"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())