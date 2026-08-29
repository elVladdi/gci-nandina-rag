from __future__ import annotations

import argparse
import csv
import importlib.metadata
import json
import platform
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import is_8_digits, read_jsonl, sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")
DEFAULT_CORPUS = Path("data/processed/corpus_rag_v1_index.jsonl")
DEFAULT_INDEX = Path("data/processed/indexes/bm25_nandina8.pkl")
DEFAULT_INDEX_METADATA = Path("data/processed/indexes/bm25_nandina8_run_metadata.json")
DEFAULT_CONFIG = Path("src/configs/experiment_config.json")
DEFAULT_HISTORICAL_CASE_SUMMARY = Path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_case_summary.csv")
DEFAULT_HISTORICAL_METADATA = Path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/run_metadata.json")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2")

EXPECTED_EVAL_ROWS = 1056
EXPECTED_EVAL_CODES = 42
EXPECTED_EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
EXPECTED_CORPUS_SHA256 = "83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0"
EXPECTED_INDEX_SHA256 = "fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b"
EXPECTED_CONFIG_SHA256 = "107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d"
EXPECTED_HISTORICAL_EVAL_SHA256 = EXPECTED_EVAL_SHA256

QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
METHOD = "normative_bm25_flat_data_aduanas_clase87_v0.2"
EXPERIMENT_ID = "exp04_phase_b_normative_bm25_flat_v0.2"
STRATEGY = "normative_bm25_flat"
DATASET_VERSION = "v0.2"
SCOPE_CLASS = "87"
K_VALUES = [1, 3, 5, 10, 50]
RECALL_K_VALUES = [50, 100]
HIERARCHICAL_K_VALUES = [10, 50, 100]
CSV_ENCODING = "utf-8"


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _normalize_code(value: object) -> str:
    return re.sub(r"\D", "", _clean(value))[:8]


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


def _package_versions() -> dict[str, str]:
    versions: dict[str, str] = {}
    for package in ["numpy", "pandas"]:
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


def _validate_eval_rows(rows: Sequence[Mapping[str, str]]) -> None:
    if len(rows) != EXPECTED_EVAL_ROWS:
        raise ValueError(f"Evalset expected {EXPECTED_EVAL_ROWS} rows, found {len(rows)}")
    case_ids: set[str] = set()
    for index, row in enumerate(rows, start=1):
        case_id = _clean(row.get("case_id"))
        if not case_id.startswith("DA-EVAL-V02-"):
            raise ValueError(f"Eval row {index} has unexpected case_id: {case_id}")
        if "V01" in case_id.upper() or "v0.1" in case_id.lower():
            raise ValueError(f"Eval row {index} leaks v0.1 case_id: {case_id}")
        if case_id in case_ids:
            raise ValueError(f"Duplicate eval case_id: {case_id}")
        case_ids.add(case_id)
        expected = _normalize_code(row.get(LABEL_COLUMN))
        if not is_8_digits(expected):
            raise ValueError(f"Eval row {index} has invalid NANDINA: {row.get(LABEL_COLUMN)}")
        if expected[:2] != SCOPE_CLASS:
            raise ValueError(f"Eval row {index} is outside class {SCOPE_CLASS}: {expected}")
        if not _clean(row.get(QUERY_COLUMN)):
            raise ValueError(f"Eval row {index} has empty query column")
    codes = {_normalize_code(row.get(LABEL_COLUMN)) for row in rows}
    if len(codes) != EXPECTED_EVAL_CODES:
        raise ValueError(f"Evalset expected {EXPECTED_EVAL_CODES} unique codes, found {len(codes)}")


def _load_corpus_map(rows: Sequence[Mapping[str, Any]]) -> tuple[dict[str, Mapping[str, Any]], dict[str, Any]]:
    nandina_rows = [row for row in rows if _clean(row.get("tipo")) == "nandina_8"]
    by_code: dict[str, Mapping[str, Any]] = {}
    duplicate_codes: list[str] = []
    for row in nandina_rows:
        code = _normalize_code(row.get("codigo"))
        if not is_8_digits(code):
            continue
        if code in by_code:
            duplicate_codes.append(code)
        by_code[code] = row
    fields = sorted({key for row in rows[:50] for key in row.keys()})
    stats = {
        "rows_total": len(rows),
        "nandina_8_rows": len(nandina_rows),
        "nandina_8_unique_codes": len(by_code),
        "duplicate_nandina_8_codes": len(duplicate_codes),
        "fields_observed_sample": fields,
        "source_values": sorted({_clean(row.get("fuente")) for row in rows if _clean(row.get("fuente"))}),
        "version_values": sorted({_clean(row.get("version")) for row in rows if _clean(row.get("version"))}),
        "type_counts": dict(sorted(Counter(_clean(row.get("tipo")) for row in rows).items())),
        "level": "nandina_8",
        "document_unit": "one corpus row per NANDINA-8 code filtered by tipo=nandina_8",
        "indexed_text": "titulo + texto_index, with texto fallback during index build",
        "known_duplicate_conflicts": "flat corpus_rag_v1_index has 7644 unique NANDINA-8 codes; hierarchy gaps/conflicts are documented in v0.1 corpus audits",
    }
    return by_code, stats


def _family_hit(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int) -> int:
    prefix = true_code[:prefix_len]
    if not prefix:
        return 0
    return int(any(_clean(hit.get("code")).startswith(prefix) for hit in hits[:k]))


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

def _coverage_class(rank: int, covered: bool) -> str:
    if not covered:
        return "reference_code_absent_from_corpus"
    if rank == 1:
        return "top_1"
    if 2 <= rank <= 3:
        return "rank_2_3"
    if 4 <= rank <= 5:
        return "rank_4_5"
    if 6 <= rank <= 10:
        return "rank_6_10"
    if 11 <= rank <= 50:
        return "rank_11_50"
    return "present_not_recovered_top_50"


def _metric_row(name: str, numerator: float, denominator: int) -> dict[str, Any]:
    return {"metric": name, "numerator": numerator, "denominator": denominator, "value": float(numerator / denominator) if denominator else 0.0}


def _metric_rows(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    denominator = len(case_rows)
    rows = [_metric_row("mrr", sum(float(row["reciprocal_rank"]) for row in case_rows), denominator)]
    for k in K_VALUES:
        rows.append(_metric_row(f"top_{k}", sum(int(row[f"hit_top_{k}"]) for row in case_rows), denominator))
    for k in RECALL_K_VALUES:
        rows.append(_metric_row(f"recall_at_{k}", sum(int(row[f"hit_recall_{k}"]) for row in case_rows), denominator))
    for k in HIERARCHICAL_K_VALUES:
        rows.append(_metric_row(f"partida_at_{k}", sum(int(row[f"partida_at_{k}"]) for row in case_rows), denominator))
        rows.append(_metric_row(f"sub_partida_at_{k}", sum(int(row[f"sub_partida_at_{k}"]) for row in case_rows), denominator))
        rows.append(_metric_row(f"clase_at_{k}", sum(int(row[f"clase_at_{k}"]) for row in case_rows), denominator))
    return rows


def _metrics(case_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    rows = _metric_rows(case_rows)
    payload: dict[str, Any] = {row["metric"]: row["value"] for row in rows}
    for row in rows:
        payload[f"{row['metric']}_numerator"] = row["numerator"]
        payload[f"{row['metric']}_denominator"] = row["denominator"]
    payload["cases_evaluated"] = len(case_rows)
    payload["cases_with_retrieval"] = sum(1 for row in case_rows if int(row["retrieved_count"]) > 0)
    payload["zero_retrieval_cases"] = sum(1 for row in case_rows if int(row["retrieved_count"]) == 0)
    payload["not_found_at_depth"] = sum(1 for row in case_rows if int(row["rank_ref"]) <= 0)
    payload["metric_table"] = rows
    return payload


def _position_distribution(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    total = len(case_rows)
    order = ["1", "2-3", "4-5", "6-10", "11-50", ">50_or_not_retrieved"]
    counts = Counter(_clean(row.get("position_bucket")) for row in case_rows)
    return [{"position_bucket": bucket, "cases": int(counts.get(bucket, 0)), "pct": float(counts.get(bucket, 0) / total) if total else 0.0} for bucket in order]


def _coverage_rows(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    total = len(case_rows)
    order = [
        "reference_code_absent_from_corpus",
        "present_not_recovered_top_50",
        "rank_11_50",
        "rank_6_10",
        "rank_4_5",
        "rank_2_3",
        "top_1",
    ]
    counts = Counter(_clean(row.get("coverage_class")) for row in case_rows)
    return [{"coverage_class": key, "cases": int(counts.get(key, 0)), "pct": float(counts.get(key, 0) / total) if total else 0.0} for key in order]


def _coverage_summary(case_rows: Sequence[Mapping[str, Any]], eval_codes: set[str], corpus_codes: set[str]) -> dict[str, Any]:
    covered_codes = eval_codes & corpus_codes
    code_absent = eval_codes - corpus_codes
    covered_cases = [row for row in case_rows if bool(row["reference_code_in_corpus"])]
    recovered_cases = [row for row in case_rows if int(row["rank_ref"]) > 0]
    return {
        "eval_unique_codes": len(eval_codes),
        "eval_codes_covered_by_corpus": len(covered_codes),
        "eval_codes_absent_from_corpus": len(code_absent),
        "missing_eval_codes": sorted(code_absent),
        "eval_cases": len(case_rows),
        "eval_cases_covered_by_corpus": len(covered_cases),
        "eval_cases_absent_from_corpus": len(case_rows) - len(covered_cases),
        "eval_cases_recovered_at_depth": len(recovered_cases),
        "eval_cases_covered_but_not_recovered_at_depth": sum(1 for row in covered_cases if int(row["rank_ref"]) <= 0),
        "eval_cases_covered_but_not_recovered_top_50": sum(1 for row in covered_cases if int(row["hit_top_50"]) == 0),
        "coverage_distribution": _coverage_rows(case_rows),
    }


def _compatibility_report(
    case_rows: Sequence[Mapping[str, Any]],
    historical_case_rows: Sequence[Mapping[str, str]],
    historical_metadata: Mapping[str, Any],
    eval_sha: str,
) -> dict[str, Any]:
    normative_by_case = {str(row["case_id"]): str(row["nandina_ref"]) for row in case_rows}
    historical_by_case = {str(row["case_id"]): str(row["expected_nandina"]) for row in historical_case_rows}
    same_cases = set(normative_by_case) == set(historical_by_case)
    shared_cases = set(normative_by_case) & set(historical_by_case)
    label_mismatches = sorted(case_id for case_id in shared_cases if normative_by_case[case_id] != historical_by_case[case_id])
    historical_eval_sha = _clean(historical_metadata.get("inputs", {}).get("evalset_sha256"))
    return {
        "artifact_id": "historical_vs_normative_flat_compatibility_v0.2",
        "total_cases_normative": len(normative_by_case),
        "total_cases_historical": len(historical_by_case),
        "identical_case_id_set": same_cases,
        "identical_labels": not label_mismatches and same_cases,
        "label_mismatch_count": len(label_mismatches),
        "label_mismatch_examples": label_mismatches[:10],
        "missing_in_normative": sorted(set(historical_by_case) - set(normative_by_case))[:10],
        "missing_in_historical": sorted(set(normative_by_case) - set(historical_by_case))[:10],
        "eval_hash_historical": historical_eval_sha,
        "eval_hash_normative": eval_sha,
        "compatible": bool(same_cases and not label_mismatches and historical_eval_sha == eval_sha),
    }


def _comparison_rows(historical_metrics: Mapping[str, Any], normative_metrics: Mapping[str, Any]) -> list[dict[str, Any]]:
    hist = historical_metrics.get("metrics", {})
    mapping = [
        ("Top-1", "exact_at_1", "top_1"),
        ("Top-3", "exact_at_3", "top_3"),
        ("Top-5", "exact_at_5", "top_5"),
        ("Top-10", "exact_at_10", "top_10"),
        ("Top-50", "exact_at_50", "top_50"),
        ("MRR", "mrr", "mrr"),
    ]
    rows: list[dict[str, Any]] = []
    for label, hist_key, norm_key in mapping:
        hist_value = float(hist.get(hist_key, 0.0))
        norm_value = float(normative_metrics.get(norm_key, 0.0))
        rows.append({"metric": label, "historical_v0_2": hist_value, "normative_flat_v0_2": norm_value, "delta_normative_minus_historical": norm_value - hist_value})
    return rows


def _build_case_row(
    eval_row: Mapping[str, str],
    hits: Sequence[Mapping[str, Any]],
    corpus_by_code: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    expected = _normalize_code(eval_row.get(LABEL_COLUMN))
    rank = rank_of_true(hits, expected)
    top1 = hits[0] if hits else {}
    covered = expected in corpus_by_code
    row: dict[str, Any] = {
        "case_id": _clean(eval_row.get("case_id")),
        "id_unico": _clean(eval_row.get("id_unico")),
        "declaracion": _clean(eval_row.get("DECLARACION")),
        "serie": _clean(eval_row.get("SERIE")),
        "query": _clean(eval_row.get(QUERY_COLUMN)),
        "nandina_ref": expected,
        "partida_ref": expected[:4],
        "sub_partida_ref": expected[:6],
        "clase_ref": expected[:2],
        "reference_code_in_corpus": covered,
        "reference_doc_id": _clean(corpus_by_code.get(expected, {}).get("doc_id")),
        "rank_ref": rank,
        "position_bucket": _position_bucket(rank),
        "coverage_class": _coverage_class(rank, covered),
        "retrieved_count": len(hits),
        "top1_code": _clean(top1.get("code")),
        "top1_doc_id": _clean(corpus_by_code.get(_clean(top1.get("code")), {}).get("doc_id")) if top1 else "",
        "top1_score": top1.get("score", "") if top1 else "",
        "reciprocal_rank": mrr_from_rank(rank),
        "method": METHOD,
    }
    for k in K_VALUES:
        row[f"hit_top_{k}"] = int(acc_at_k(rank, k))
    for k in RECALL_K_VALUES:
        row[f"hit_recall_{k}"] = int(acc_at_k(rank, k))
    for k in HIERARCHICAL_K_VALUES:
        row[f"partida_at_{k}"] = _family_hit(hits, expected, 4, k)
        row[f"sub_partida_at_{k}"] = _family_hit(hits, expected, 6, k)
        row[f"clase_at_{k}"] = _family_hit(hits, expected, 2, k)
    return row


def _candidate_rows(
    eval_row: Mapping[str, str],
    hits: Sequence[Mapping[str, Any]],
    corpus_by_code: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    expected = _normalize_code(eval_row.get(LABEL_COLUMN))
    rows: list[dict[str, Any]] = []
    for hit in hits:
        code = _clean(hit.get("code"))
        corpus_row = corpus_by_code.get(code, {})
        rows.append(
            {
                "case_id": _clean(eval_row.get("case_id")),
                "id_unico": _clean(eval_row.get("id_unico")),
                "nandina_ref": expected,
                "candidate_rank": int(hit["rank"]),
                "candidate_doc_id": _clean(corpus_row.get("doc_id")) or f"NANDINA_{code}",
                "candidate_code": code,
                "candidate_partida": code[:4],
                "candidate_sub_partida": code[:6],
                "candidate_clase": code[:2],
                "score": float(hit["score"]),
                "candidate_text": _clean(hit.get("text")),
                "is_reference_code": int(code == expected),
                "method": METHOD,
            }
        )
    return rows

def _output_paths(output_dir: Path) -> dict[str, Path]:
    return {
        "normative_results_csv": output_dir / "normative_results.csv",
        "normative_case_summary_csv": output_dir / "normative_case_summary.csv",
        "normative_failure_cases_csv": output_dir / "normative_failure_cases.csv",
        "normative_metrics_json": output_dir / "normative_metrics.json",
        "normative_coverage_summary_json": output_dir / "normative_coverage_summary.json",
        "normative_coverage_summary_csv": output_dir / "normative_coverage_summary.csv",
        "position_distribution_csv": output_dir / "position_distribution.csv",
        "historical_vs_normative_flat_compatibility_json": output_dir / "historical_vs_normative_flat_compatibility_v0.2.json",
        "historical_vs_normative_flat_metrics_comparison_csv": output_dir / "historical_vs_normative_flat_metrics_comparison_v0.2.csv",
        "run_metadata_json": output_dir / "run_metadata.json",
        "summary_md": output_dir / "summary.md",
    }


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    metrics = payload["metrics"]
    coverage = payload["coverage_summary"]
    compatibility = payload["compatibility"]
    metric_lines = ["| Metrica | Numerador | Denominador | Valor |", "| --- | ---: | ---: | ---: |"]
    for row in metrics["metric_table"]:
        metric_lines.append(f"| {row['metric']} | {row['numerator']} | {row['denominator']} | {float(row['value']):.6f} |")
    lines = [
        "# EXP-04 Fase B - BM25 normativo plano data_aduanas clase 87 v0.2",
        "",
        "## Alcance",
        "",
        "Se evaluo exclusivamente BM25 normativo plano sobre el evalset data_aduanas clase 87 v0.2. No se ejecuto BM25 jerarquico, esquema dual, candidate pool, Text2Trade, integracion, RAG, reranking LLM ni explicador LLM.",
        "",
        "## Corpus normativo plano",
        "",
        f"- Corpus: `{payload['inputs']['corpus']}`.",
        f"- Corpus SHA-256: `{payload['inputs']['corpus_sha256']}`.",
        f"- Indice: `{payload['inputs']['index']}`.",
        f"- Indice SHA-256: `{payload['inputs']['index_sha256']}`.",
        f"- Documentos NANDINA-8 indexados: {payload['corpus']['nandina_8_unique_codes']}.",
        f"- Texto indexado: {payload['corpus']['indexed_text']}.",
        "",
        "## Evalset",
        "",
        f"- Evalset: `{payload['inputs']['evalset']}`.",
        f"- Evalset SHA-256: `{payload['inputs']['evalset_sha256']}`.",
        f"- Casos evaluados: {metrics['cases_evaluated']}.",
        f"- Query: `{payload['columns']['query']}`.",
        f"- Etiqueta: `{payload['columns']['label']}`.",
        "",
        "## Resultado global",
        "",
        *metric_lines,
        "",
        "## Cobertura normativa",
        "",
        f"- Codigos eval cubiertos por corpus: {coverage['eval_codes_covered_by_corpus']}/{coverage['eval_unique_codes']}.",
        f"- Casos eval cubiertos por corpus: {coverage['eval_cases_covered_by_corpus']}/{coverage['eval_cases']}.",
        f"- Casos sin cobertura normativa: {coverage['eval_cases_absent_from_corpus']}.",
        f"- Casos con codigo en corpus pero no recuperado Top-50: {coverage['eval_cases_covered_but_not_recovered_top_50']}.",
        "",
        "## Compatibilidad con historico v0.2",
        "",
        f"- Mismo set case_id: {compatibility['identical_case_id_set']}.",
        f"- Mismas etiquetas por case_id: {compatibility['identical_labels']}.",
        f"- Compatible: {compatibility['compatible']}.",
        "",
    ]
    return "\n".join(lines)


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    started = time.perf_counter()
    root = project_root()
    eval_path = resolve_project_path(args.evalset)
    corpus_path = resolve_project_path(args.corpus)
    index_path = resolve_project_path(args.index)
    index_metadata_path = resolve_project_path(args.index_metadata)
    config_path = resolve_project_path(args.config)
    historical_case_summary_path = resolve_project_path(args.historical_case_summary)
    historical_metadata_path = resolve_project_path(args.historical_metadata)
    output_dir = resolve_project_path(args.output_dir)
    depth = max(args.retrieval_depth, max(K_VALUES), max(RECALL_K_VALUES), max(HIERARCHICAL_K_VALUES))

    input_args = [str(args.evalset), str(args.corpus), str(args.index), str(args.index_metadata), str(args.config)]
    if any("v0.1" in value.lower() for value in input_args):
        raise ValueError("EXP-04 Fase B v0.2 cannot consume v0.1 eval, corpus, index or config inputs")

    eval_sha = _validate_hash(eval_path, EXPECTED_EVAL_SHA256, "evalset v0.2")
    corpus_sha = _validate_hash(corpus_path, EXPECTED_CORPUS_SHA256, "flat normative corpus")
    index_sha = _validate_hash(index_path, EXPECTED_INDEX_SHA256, "flat BM25 index")
    config_sha = _validate_hash(config_path, EXPECTED_CONFIG_SHA256, "BM25 flat config")
    index_metadata_sha = sha256_file(index_metadata_path)

    eval_rows = _read_csv(eval_path)
    _validate_eval_rows(eval_rows)
    corpus_rows = read_jsonl(corpus_path)
    corpus_by_code, corpus_stats = _load_corpus_map(corpus_rows)
    eval_codes = {_normalize_code(row.get(LABEL_COLUMN)) for row in eval_rows}
    if not eval_codes <= set(corpus_by_code):
        missing = sorted(eval_codes - set(corpus_by_code))
        raise ValueError(f"Evalset has reference codes absent from flat normative corpus: {missing}")

    index_metadata = _read_json(index_metadata_path)
    if _clean(index_metadata.get("input", {}).get("corpus_sha256")) != corpus_sha:
        raise ValueError("Flat index metadata corpus hash does not match locked corpus")
    bm25_params = index_metadata.get("bm25_params", {})
    bm25_config = _read_json(config_path).get("bm25", {})
    index = load_bm25_index(index_path)
    if float(getattr(index, "k1", 0.0)) != float(bm25_params.get("k1")) or float(getattr(index, "b", 0.0)) != float(bm25_params.get("b")):
        raise ValueError("Loaded index BM25 parameters do not match index metadata")

    candidate_rows: list[dict[str, Any]] = []
    case_rows: list[dict[str, Any]] = []
    for eval_row in eval_rows:
        query = _clean(eval_row.get(QUERY_COLUMN))
        hits = retrieve(index, query, top_n=depth)
        case_rows.append(_build_case_row(eval_row, hits, corpus_by_code))
        candidate_rows.extend(_candidate_rows(eval_row, hits, corpus_by_code))

    metrics = _metrics(case_rows)
    coverage_summary = _coverage_summary(case_rows, eval_codes, set(corpus_by_code))
    position_rows = _position_distribution(case_rows)
    coverage_rows = coverage_summary["coverage_distribution"]
    historical_case_rows = _read_csv(historical_case_summary_path)
    historical_metadata = _read_json(historical_metadata_path)
    historical_metrics = _read_json(historical_metadata_path.parent / "historical_metrics.json")
    compatibility = _compatibility_report(case_rows, historical_case_rows, historical_metadata, eval_sha)
    comparison_rows = _comparison_rows(historical_metrics, metrics)
    if not compatibility["compatible"]:
        raise ValueError("Historical-vs-normative flat compatibility report is false; Gate B fails")

    payload: dict[str, Any] = {
        "version": DATASET_VERSION,
        "dataset_version": DATASET_VERSION,
        "experiment_id": EXPERIMENT_ID,
        "strategy": STRATEGY,
        "method": METHOD,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": platform.python_version(), "platform": platform.platform(), "packages": _package_versions()},
        "git": _git_metadata(root),
        "command": " ".join([sys.executable, *sys.argv]),
        "inputs": {
            "evalset": _rel(eval_path, root),
            "evalset_sha256": eval_sha,
            "corpus": _rel(corpus_path, root),
            "corpus_sha256": corpus_sha,
            "index": _rel(index_path, root),
            "index_sha256": index_sha,
            "index_metadata": _rel(index_metadata_path, root),
            "index_metadata_sha256": index_metadata_sha,
            "config": _rel(config_path, root),
            "config_sha256": config_sha,
            "historical_case_summary": _rel(historical_case_summary_path, root),
            "historical_metadata": _rel(historical_metadata_path, root),
        },
        "columns": {"query": QUERY_COLUMN, "label": LABEL_COLUMN},
        "parameters": {
            "retrieval_depth": depth,
            "k_values": K_VALUES,
            "recall_k_values": RECALL_K_VALUES,
            "hierarchical_k_values": HIERARCHICAL_K_VALUES,
            "k1": getattr(index, "k1", None),
            "b": getattr(index, "b", None),
            "use_stopwords_in_index_build": bm25_params.get("use_stopwords"),
            "configured_top_n": bm25_config.get("top_n"),
        },
        "corpus": corpus_stats,
        "index_stats": {
            "docs_indexed": len(index.doc_ids),
            "unique_codes": len(set(index.doc_ids)),
            "avgdl": getattr(index, "avgdl", None),
            "vocab_size": len(getattr(index, "idf", {})),
        },
        "validation": {
            "evalset_rows": len(eval_rows),
            "case_ids_unique": len({row["case_id"] for row in case_rows}) == len(case_rows),
            "all_case_ids_v02_eval": all(str(row["case_id"]).startswith("DA-EVAL-V02-") for row in case_rows),
            "v01_inputs_used": False,
            "true_labels_match_evalset": True,
            "same_case_ids_as_historical_v02": compatibility["identical_case_id_set"],
            "same_labels_as_historical_v02": compatibility["identical_labels"],
            "compatible_with_historical_v02": compatibility["compatible"],
            "llm_used": False,
            "text2trade_used": False,
            "hierarchical_bm25_used": False,
            "candidate_pool_used": False,
            "rag_used": False,
        },
        "metrics": metrics,
        "coverage_summary": coverage_summary,
        "position_distribution": position_rows,
        "compatibility": compatibility,
        "comparison_historical_vs_normative_flat": comparison_rows,
    }

    outputs = _output_paths(output_dir)
    payload["outputs"] = {name: _rel(path, root) for name, path in outputs.items()}

    case_fieldnames = [
        "case_id", "id_unico", "declaracion", "serie", "query", "nandina_ref", "partida_ref", "sub_partida_ref", "clase_ref",
        "reference_code_in_corpus", "reference_doc_id", "rank_ref", "position_bucket", "coverage_class", "retrieved_count", "top1_code", "top1_doc_id", "top1_score", "reciprocal_rank", "method",
        *[f"hit_top_{k}" for k in K_VALUES], *[f"hit_recall_{k}" for k in RECALL_K_VALUES],
        *[f"partida_at_{k}" for k in HIERARCHICAL_K_VALUES], *[f"sub_partida_at_{k}" for k in HIERARCHICAL_K_VALUES], *[f"clase_at_{k}" for k in HIERARCHICAL_K_VALUES],
    ]
    candidate_fieldnames = [
        "case_id", "id_unico", "nandina_ref", "candidate_rank", "candidate_doc_id", "candidate_code", "candidate_partida", "candidate_sub_partida", "candidate_clase", "score", "candidate_text", "is_reference_code", "method",
    ]
    coverage_fieldnames = ["coverage_class", "cases", "pct"]
    comparison_fieldnames = ["metric", "historical_v0_2", "normative_flat_v0_2", "delta_normative_minus_historical"]

    failure_rows = [row for row in case_rows if int(row["hit_top_50"]) == 0]
    _write_csv(outputs["normative_results_csv"], candidate_rows, candidate_fieldnames)
    _write_csv(outputs["normative_case_summary_csv"], case_rows, case_fieldnames)
    _write_csv(outputs["normative_failure_cases_csv"], failure_rows, case_fieldnames)
    _write_csv(outputs["normative_coverage_summary_csv"], coverage_rows, coverage_fieldnames)
    _write_csv(outputs["position_distribution_csv"], position_rows, ["position_bucket", "cases", "pct"])
    _write_csv(outputs["historical_vs_normative_flat_metrics_comparison_csv"], comparison_rows, comparison_fieldnames)
    _write_json(outputs["normative_metrics_json"], payload)
    _write_json(outputs["normative_coverage_summary_json"], coverage_summary)
    _write_json(outputs["historical_vs_normative_flat_compatibility_json"], compatibility)
    _write_text(outputs["summary_md"], _summary_markdown(payload))

    run_metadata = {
        "experiment_id": EXPERIMENT_ID,
        "strategy": STRATEGY,
        "dataset_version": DATASET_VERSION,
        "created_at_utc": payload["created_at_utc"],
        "git": payload["git"],
        "command": payload["command"],
        "inputs": payload["inputs"],
        "parameters": payload["parameters"],
        "outputs": payload["outputs"],
        "output_sha256": {
            name: sha256_file(path)
            for name, path in outputs.items()
            if name != "run_metadata_json" and path.exists()
        },
        "validation": payload["validation"],
        "metrics": payload["metrics"],
        "coverage_summary": payload["coverage_summary"],
        "compatibility": payload["compatibility"],
        "elapsed_seconds": time.perf_counter() - started,
    }
    _write_json(outputs["run_metadata_json"], run_metadata)
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate flat normative BM25 over data_aduanas class 87 v0.2.")
    parser.add_argument("--evalset", default=str(DEFAULT_EVALSET))
    parser.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    parser.add_argument("--index", default=str(DEFAULT_INDEX))
    parser.add_argument("--index-metadata", default=str(DEFAULT_INDEX_METADATA))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--historical-case-summary", default=str(DEFAULT_HISTORICAL_CASE_SUMMARY))
    parser.add_argument("--historical-metadata", default=str(DEFAULT_HISTORICAL_METADATA))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--retrieval-depth", type=int, default=100)
    return parser


def main() -> int:
    payload = evaluate(build_parser().parse_args())
    metrics = payload["metrics"]
    coverage = payload["coverage_summary"]
    print("OK: EXP-04 Fase B BM25 normativo plano v0.2 evaluado")
    print(
        f"Top-1={metrics['top_1']:.4f} Top-10={metrics['top_10']:.4f} "
        f"Top-50={metrics['top_50']:.4f} MRR={metrics['mrr']:.4f}"
    )
    print(f"Recall@100={metrics['recall_at_100']:.4f}")
    print(f"Cobertura codigos={coverage['eval_codes_covered_by_corpus']}/{coverage['eval_unique_codes']} casos={coverage['eval_cases_covered_by_corpus']}/{coverage['eval_cases']}")
    print(f"Compatible historico v0.2={payload['compatibility']['compatible']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())