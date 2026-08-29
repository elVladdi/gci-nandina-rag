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
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..bm25_index import is_8_digits, read_jsonl, sha256_file
from ..evaluation.metrics import acc_at_k, mrr_from_rank, rank_of_true
from ..retrieval.bm25 import load_bm25_index, retrieve
from ..utils.paths import ensure_parent, project_root, resolve_project_path

DEFAULT_EVALSET = Path("data/processed/data_aduanas_evalset_clase87_v0.2.csv")
DEFAULT_HIERARCHICAL_CORPUS = Path("data/processed/corpus_nandina_hierarchical_v0.1.jsonl")
DEFAULT_HIERARCHICAL_CORPUS_METADATA = Path("data/processed/corpus_nandina_hierarchical_v0.1_metadata.json")
DEFAULT_HIERARCHICAL_INDEX = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl")
DEFAULT_HIERARCHICAL_INDEX_METADATA = Path("data/processed/indexes/bm25_nandina8_hierarchical_v0.1_run_metadata.json")
DEFAULT_HIERARCHICAL_AUDIT = Path("outputs/corpus/auditoria_nandina_jerarquica_v0.1/audit_summary.json")
DEFAULT_CONFIG = Path("src/configs/experiment_config.json")
DEFAULT_HISTORICAL_CASE_SUMMARY = Path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_case_summary.csv")
DEFAULT_HISTORICAL_METADATA = Path("outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/run_metadata.json")
DEFAULT_FLAT_CASE_SUMMARY = Path("outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv")
DEFAULT_FLAT_METRICS = Path("outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json")
DEFAULT_FLAT_METADATA = Path("outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/run_metadata.json")
DEFAULT_OUTPUT_DIR = Path("outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2")

EXPECTED_EVAL_ROWS = 1056
EXPECTED_EVAL_CODES = 42
EXPECTED_EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
EXPECTED_HIERARCHICAL_CORPUS_SHA256 = "f389ae6c303279cfea23697cbedb3315a5254254c2efc2450cf28f81243df175"
EXPECTED_HIERARCHICAL_SOURCE_CORPUS_SHA256 = "4f5f2d33e864ee2d5992e76e68b7a7fa1163f98564b79d2533f5131acb5ace58"
EXPECTED_HIERARCHICAL_INDEX_SHA256 = "f828736ea700471c95d2b985bdd969d751cd36c3ca01c407049209010bdbe60b"
EXPECTED_CONFIG_SHA256 = "107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d"
EXPECTED_FLAT_OUTPUT_HASHES = {
    "normative_results.csv": "d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015",
    "normative_case_summary.csv": "f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0",
    "normative_metrics.json": "56a702398d3b9d1483ecd1be3ca79587682ad8fd3afd84858917f248b5ae0460",
    "run_metadata.json": "e57d1ebd360790c64b485f5fb4d7aa34be500e48f4ebf48ab7c0437874caba44",
}
EXPECTED_HISTORICAL_OUTPUT_HASHES = {
    "historical_results.csv": "c350b63e0180a4c28573d2626c76d030308913b690c524d2d62ea439cf34a6c8",
    "historical_case_summary.csv": "f8f4ac6d585194aace74c50f495720cc87b0c09a28438d888b0030dfaddd0d56",
    "historical_metrics.json": "5334e64ab2b3f812f939b652fe1ee8ad8db24b673ebb48fd4d7b1ddb0dd444fa",
    "run_metadata.json": "edb8bd3343418714fb6736f896c8831aeebe8ecec2f31599bb84ad32722a3a32",
}
QUERY_COLUMN = "DESCRIPCION DE MERCANCIAS CONCATENADA"
LABEL_COLUMN = "NANDINA"
METHOD = "normative_bm25_hierarchical_data_aduanas_clase87_v0.2"
EXPERIMENT_ID = "exp04_phase_c_normative_bm25_hierarchical_v0.2"
STRATEGY = "normative_bm25_hierarchical"
DATASET_VERSION = "v0.2"
SCOPE_CLASS = "87"
K_VALUES = [1, 3, 5, 10, 50]
RECALL_K_VALUES = [50, 100, 200]
HIERARCHICAL_K_VALUES = [10, 50, 100, 200]
GENERIC_PHRASES = {"los demas", "las demas", "los dems", "las dems", "demas", "solido", "liquido", "ruedas", "partes", "otros", "otras"}


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def code8(value: object) -> str:
    return re.sub(r"\D", "", clean(value))[:8]


def norm(value: object) -> str:
    raw = unicodedata.normalize("NFKD", clean(value).lower())
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch))
    raw = re.sub(r"[^a-z0-9]+", " ", raw)
    return re.sub(r"\s+", " ", raw).strip()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return [{clean(k): clean(v) for k, v in row.items() if k is not None} for row in reader]


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def write_text(path: Path, text: str) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text.rstrip() + "\n")


def rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def git_value(args: list[str], root: Path) -> str:
    try:
        result = subprocess.run(["git", *args], cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"
    return result.stdout.strip()


def git_metadata(root: Path) -> dict[str, Any]:
    return {
        "branch": git_value(["rev-parse", "--abbrev-ref", "HEAD"], root),
        "commit": git_value(["rev-parse", "HEAD"], root),
        "dirty_status_short": git_value(["status", "--short"], root).splitlines(),
    }


def package_versions() -> dict[str, str]:
    out: dict[str, str] = {}
    for package in ["numpy", "pandas"]:
        try:
            out[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            out[package] = "not-installed"
    return out


def validate_hash(path: Path, expected: str, label: str) -> str:
    actual = sha256_file(path)
    if actual != expected:
        raise ValueError(f"{label} sha256 mismatch: expected {expected}, found {actual}")
    return actual


def validate_eval(rows: Sequence[Mapping[str, str]]) -> None:
    if len(rows) != EXPECTED_EVAL_ROWS:
        raise ValueError(f"Evalset expected {EXPECTED_EVAL_ROWS} rows, found {len(rows)}")
    seen: set[str] = set()
    for idx, row in enumerate(rows, start=1):
        case_id = clean(row.get("case_id"))
        expected = code8(row.get(LABEL_COLUMN))
        if not case_id.startswith("DA-EVAL-V02-"):
            raise ValueError(f"Unexpected case_id at row {idx}: {case_id}")
        if case_id in seen:
            raise ValueError(f"Duplicate case_id: {case_id}")
        if not is_8_digits(expected) or expected[:2] != SCOPE_CLASS:
            raise ValueError(f"Invalid/out-of-scope NANDINA at row {idx}: {expected}")
        if not clean(row.get(QUERY_COLUMN)):
            raise ValueError(f"Empty query at row {idx}")
        seen.add(case_id)
    codes = {code8(row.get(LABEL_COLUMN)) for row in rows}
    if len(codes) != EXPECTED_EVAL_CODES:
        raise ValueError(f"Evalset expected {EXPECTED_EVAL_CODES} codes, found {len(codes)}")


def corpus_maps(rows: Sequence[Mapping[str, Any]], metadata: Mapping[str, Any], audit: Mapping[str, Any]) -> tuple[dict[str, Mapping[str, Any]], dict[str, dict[str, bool]], dict[str, Any]]:
    nandina_rows = [row for row in rows if clean(row.get("tipo")) == "nandina_8"]
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    first: dict[str, Mapping[str, Any]] = {}
    for row in nandina_rows:
        code = code8(row.get("codigo"))
        if is_8_digits(code):
            grouped[code].append(row)
            first.setdefault(code, row)
    duplicate_details = {
        code: [{"doc_id": clean(row.get("doc_id")), "titulo": clean(row.get("titulo")), "partida_4d": clean(row.get("partida_4d")), "hs_6d": clean(row.get("hs_6d")), "source_page": row.get("source_page"), "texto_index_jerarquico_length": len(clean(row.get("texto_index_jerarquico")))} for row in group]
        for code, group in sorted(grouped.items()) if len(group) > 1
    }
    flags: dict[str, dict[str, bool]] = {}
    for code, row in first.items():
        missing4 = not clean(row.get("descripcion_partida_4d"))
        missing6 = not clean(row.get("descripcion_hs_6d")) or not clean(row.get("hs_6d"))
        desc8 = clean(row.get("descripcion_nandina_8d") or row.get("titulo"))
        flags[code] = {
            "missing_parent_4d": missing4,
            "missing_parent_hs6": missing6,
            "missing_both_parents": missing4 and missing6,
            "duplicate_code_documents": code in duplicate_details,
            "generic_or_short_leaf_description": norm(desc8.rstrip(".:")) in GENERIC_PHRASES or len(desc8.rstrip(".:")) <= 12,
        }
    lengths = [len(clean(row.get("texto_index_jerarquico") or row.get("texto_index"))) for row in nandina_rows]
    stats = {
        "path_methodology_version": "v0.1",
        "source_methodology": "src.corpus.build_hierarchical_nandina_corpus",
        "records_total": len(rows),
        "nandina_8_rows": len(nandina_rows),
        "nandina_8_unique_codes": len(grouped),
        "nandina_8_codes_with_multiple_documents": len(duplicate_details),
        "total_extra_documents_from_duplicate_codes": len(nandina_rows) - len(grouped),
        "max_documents_per_code": max((len(v) for v in grouped.values()), default=0),
        "duplicate_code_details": duplicate_details,
        "fields": sorted({key for row in rows for key in row.keys()}),
        "source_values": sorted({clean(row.get("fuente")) for row in rows if clean(row.get("fuente"))}),
        "version_values": sorted({clean(row.get("version")) for row in rows if clean(row.get("version"))}),
        "type_counts": dict(sorted(Counter(clean(row.get("tipo")) for row in rows).items())),
        "text_length": {"min": min(lengths) if lengths else 0, "max": max(lengths) if lengths else 0, "median": sorted(lengths)[len(lengths) // 2] if lengths else 0},
        "hierarchical_levels_in_text": ["section", "chapter", "partida_4d", "hs_6d", "nandina_8d", "unidad_fisica"],
        "document_unit": "one hierarchical document row per NANDINA-8 source row; effective evaluation collapses duplicate rows to unique NANDINA-8 codes by first BM25 score occurrence",
        "indexed_text": "titulo + texto_index_jerarquico, with texto_index fallback during index build",
        "build_rule": "Seccion + Capitulo + Partida 4D + Subpartida HS6 nullable + NANDINA 8D + Unidad fisica, deduplicated by normalized text fragment.",
        "own_code_information": ["codigo/nandina_8d", "descripcion_nandina_8d", "unidad_fisica"],
        "parent_information": ["section", "section_title", "chapter", "chapter_title", "partida_4d", "descripcion_partida_4d", "hs_6d nullable", "descripcion_hs_6d nullable"],
        "normative_context": "No standalone notes are appended by the builder; notes/context only appear if already embedded in source descriptions, including known extraction contamination warnings.",
        "metadata_counts": {key: metadata.get(key) for key in ["total_nandina8_esperadas", "total_documentos_generados", "cantidad_sin_padre_4d", "cantidad_sin_padre_hs6", "cantidad_sin_padres", "cantidad_textos_todavia_genericos", "cantidad_descripciones_8d_genericas_o_cortas"]},
        "versioned_audit_counts": {
            "source_records_total": audit.get("counts", {}).get("total_records"),
            "source_partida_4d": audit.get("counts", {}).get("partida_4d"),
            "source_hs_6d": audit.get("counts", {}).get("hs_6d"),
            "source_nandina_8d": audit.get("counts", {}).get("nandina_8d"),
            "source_missing_parent_4d": audit.get("hierarchy", {}).get("nandina8_missing_parent_4d"),
            "source_missing_parent_hs6": audit.get("hierarchy", {}).get("nandina8_missing_parent_hs6"),
            "source_conflicting_parent_duplicates": audit.get("hierarchy", {}).get("conflicting_parent_duplicates"),
            "source_header_contamination": audit.get("counts", {}).get("descriptions_with_header_contamination"),
            "source_generic_or_short_rows": audit.get("generic_descriptions", {}).get("rows_flagged"),
        },
        "known_warnings": metadata.get("warnings", []),
    }
    stats["methodology_linkage"] = {
        "metadata_matches_current_corpus": metadata.get("output_sha256") == EXPECTED_HIERARCHICAL_CORPUS_SHA256,
        "metadata_source_sha256_matches_audit": metadata.get("input_sha256") == audit.get("input", {}).get("sha256") == EXPECTED_HIERARCHICAL_SOURCE_CORPUS_SHA256,
        "current_counts_match_metadata": len(nandina_rows) == metadata.get("total_documentos_generados") == metadata.get("total_nandina8_esperadas"),
        "current_counts_match_audit_source_nandina8": len(nandina_rows) == audit.get("hierarchy", {}).get("nandina8_total"),
        "linked_to_approved_methodology": True,
    }
    return first, flags, stats


def collapse_hits(raw_hits: Sequence[Mapping[str, Any]], depth: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    counts = Counter(clean(hit.get("code")) for hit in raw_hits if clean(hit.get("code")))
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for hit in raw_hits:
        code = clean(hit.get("code"))
        if not code or code in seen:
            continue
        seen.add(code)
        item = dict(hit)
        item["raw_rank"] = int(hit.get("rank", 0))
        item["rank"] = len(out) + 1
        out.append(item)
        if len(out) >= depth:
            break
    repeated = sorted(code for code, count in counts.items() if count > 1)
    return out, {
        "raw_retrieved_count": len(raw_hits),
        "raw_unique_codes": len(counts),
        "raw_repeated_code_count": len(repeated),
        "raw_repeated_codes": repeated[:10],
        "effective_retrieved_count": len(out),
        "effective_unique_codes": len({hit["code"] for hit in out}),
        "effective_has_repeated_codes": len(out) != len({hit["code"] for hit in out}),
        "collapse_rule": "first BM25 occurrence by score order wins; later occurrences of the same NANDINA-8 code are ignored before Top-k/MRR/coverage calculation",
    }


def family_hit(hits: Sequence[Mapping[str, Any]], true_code: str, prefix_len: int, k: int) -> int:
    return int(any(clean(hit.get("code")).startswith(true_code[:prefix_len]) for hit in hits[:k]))


def position_bucket(rank: int) -> str:
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
    if 51 <= rank <= 100:
        return "51-100"
    if 101 <= rank <= 200:
        return "101-200"
    return ">200_or_not_retrieved"


def evidence_class(row: Mapping[str, Any], k: int) -> str:
    if not row["reference_code_in_corpus"]:
        return "reference_absent"
    if int(row[f"exact_at_{k}"]):
        return "exact_recovered"
    if int(row[f"hs6_at_{k}"]):
        return "hs6_recovered_without_exact"
    if int(row[f"hs4_at_{k}"]):
        return "hs4_recovered_without_hs6_or_exact"
    if int(row[f"chapter_at_{k}"]):
        return "chapter_only"
    return "no_hierarchical_evidence"


def metric_row(name: str, numerator: float, denominator: int) -> dict[str, Any]:
    return {"metric": name, "numerator": numerator, "denominator": denominator, "value": float(numerator / denominator) if denominator else 0.0}


def metrics_from_cases(case_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    denominator = len(case_rows)
    rows = [metric_row("mrr", sum(float(row["reciprocal_rank"]) for row in case_rows), denominator)]
    for k in K_VALUES:
        rows.append(metric_row(f"top_{k}", sum(int(row[f"hit_top_{k}"]) for row in case_rows), denominator))
    for k in RECALL_K_VALUES:
        rows.append(metric_row(f"recall_at_{k}", sum(int(row[f"hit_recall_{k}"]) for row in case_rows), denominator))
    rows.append(metric_row("pool_recall_at_200", sum(int(row["hit_recall_200"]) for row in case_rows), denominator))
    for k in HIERARCHICAL_K_VALUES:
        for name in ["exact", "hs6", "hs4", "chapter"]:
            rows.append(metric_row(f"{name}_at_{k}", sum(int(row[f"{name}_at_{k}"]) for row in case_rows), denominator))
    out: dict[str, Any] = {row["metric"]: row["value"] for row in rows}
    for row in rows:
        out[f"{row['metric']}_numerator"] = row["numerator"]
        out[f"{row['metric']}_denominator"] = row["denominator"]
    out.update({
        "cases_evaluated": denominator,
        "cases_with_retrieval": sum(int(row["retrieved_count"]) > 0 for row in case_rows),
        "zero_retrieval_cases": sum(int(row["retrieved_count"]) == 0 for row in case_rows),
        "not_found_at_depth": sum(int(row["rank_ref"]) <= 0 for row in case_rows),
        "metric_table": rows,
    })
    return out


def position_distribution(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    total = len(case_rows)
    counts = Counter(clean(row.get("position_bucket")) for row in case_rows)
    return [{"position_bucket": bucket, "cases": int(counts.get(bucket, 0)), "pct": float(counts.get(bucket, 0) / total) if total else 0.0} for bucket in ["1", "2-3", "4-5", "6-10", "11-50", "51-100", "101-200", ">200_or_not_retrieved"]]


def coverage_distribution(case_rows: Sequence[Mapping[str, Any]], field: str) -> list[dict[str, Any]]:
    total = len(case_rows)
    counts = Counter(clean(row.get(field)) for row in case_rows)
    order = ["reference_absent", "exact_recovered", "hs6_recovered_without_exact", "hs4_recovered_without_hs6_or_exact", "chapter_only", "no_hierarchical_evidence"]
    return [{"coverage_class": item, "cases": int(counts.get(item, 0)), "pct": float(counts.get(item, 0) / total) if total else 0.0} for item in order]


def previous_hashes(root: Path) -> dict[str, Any]:
    out: dict[str, Any] = {"flat": {}, "historical": {}, "all_match_expected": True}
    groups = [("flat", root / "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2", EXPECTED_FLAT_OUTPUT_HASHES), ("historical", root / "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2", EXPECTED_HISTORICAL_OUTPUT_HASHES)]
    for label, folder, expected_map in groups:
        for name, expected in expected_map.items():
            actual = sha256_file(folder / name)
            out[label][name] = {"expected": expected, "actual": actual, "matches": actual == expected}
            out["all_match_expected"] = out["all_match_expected"] and actual == expected
    return out


def compatibility(case_rows: Sequence[Mapping[str, Any]], hist_rows: Sequence[Mapping[str, str]], flat_rows: Sequence[Mapping[str, str]], hist_meta: Mapping[str, Any], flat_meta: Mapping[str, Any], eval_sha: str) -> dict[str, Any]:
    hier = {str(row["case_id"]): str(row["nandina_ref"]) for row in case_rows}
    hist = {str(row["case_id"]): str(row["expected_nandina"]) for row in hist_rows}
    flat = {str(row["case_id"]): str(row["nandina_ref"]) for row in flat_rows}
    same_cases = set(hier) == set(hist) == set(flat)
    shared = set(hier) & set(hist) & set(flat)
    mismatches = sorted(case_id for case_id in shared if len({hier[case_id], hist[case_id], flat[case_id]}) != 1)
    hist_sha = clean(hist_meta.get("inputs", {}).get("evalset_sha256"))
    flat_sha = clean(flat_meta.get("inputs", {}).get("evalset_sha256"))
    return {
        "artifact_id": "historical_flat_vs_normative_hierarchical_compatibility_v0.2",
        "total_cases_hierarchical": len(hier),
        "total_cases_historical": len(hist),
        "total_cases_flat": len(flat),
        "identical_case_id_set": same_cases,
        "identical_labels": same_cases and not mismatches,
        "label_mismatch_count": len(mismatches),
        "label_mismatch_examples": mismatches[:10],
        "eval_hash_historical": hist_sha,
        "eval_hash_flat": flat_sha,
        "eval_hash_hierarchical": eval_sha,
        "compatible": bool(same_cases and not mismatches and hist_sha == flat_sha == eval_sha == EXPECTED_EVAL_SHA256),
    }


def comparison(flat_metrics: Mapping[str, Any], hier_metrics: Mapping[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    flat = flat_metrics.get("metrics", flat_metrics)
    metric_map = [("Top-1", "top_1", "top_1"), ("Top-3", "top_3", "top_3"), ("Top-5", "top_5", "top_5"), ("Top-10", "top_10", "top_10"), ("Top-50", "top_50", "top_50"), ("Recall@100", "recall_at_100", "recall_at_100"), ("MRR", "mrr", "mrr")]
    cov_map = [("Exact@100", "recall_at_100", "exact_at_100"), ("HS-6@100", "sub_partida_at_100", "hs6_at_100"), ("HS-4@100", "partida_at_100", "hs4_at_100"), ("Chapter@100", "clase_at_100", "chapter_at_100")]
    metric_rows = [{"metric": label, "flat_v0_2": float(flat[fkey]), "hierarchical_v0_2": float(hier_metrics[hkey]), "delta_hierarchical_minus_flat": float(hier_metrics[hkey]) - float(flat[fkey])} for label, fkey, hkey in metric_map]
    cov_rows = [{"coverage": label, "flat_v0_2": float(flat[fkey]), "hierarchical_v0_2": float(hier_metrics[hkey]), "delta_hierarchical_minus_flat": float(hier_metrics[hkey]) - float(flat[fkey])} for label, fkey, hkey in cov_map]
    for label, key in [("Exact@200", "exact_at_200"), ("HS-6@200", "hs6_at_200"), ("HS-4@200", "hs4_at_200"), ("Chapter@200", "chapter_at_200")]:
        cov_rows.append({"coverage": label, "flat_v0_2": "not_available_frozen_depth_100", "hierarchical_v0_2": hier_metrics[key], "delta_hierarchical_minus_flat": "not_computed"})
    return metric_rows, cov_rows


def stratified(case_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    groups = {
        "all_cases": list(case_rows),
        "missing_parent_4d": [row for row in case_rows if row["flag_missing_parent_4d"]],
        "missing_parent_hs6": [row for row in case_rows if row["flag_missing_parent_hs6"]],
        "missing_both_parents": [row for row in case_rows if row["flag_missing_both_parents"]],
        "duplicate_code_documents": [row for row in case_rows if row["flag_duplicate_code_documents"]],
        "generic_or_short_leaf_description": [row for row in case_rows if row["flag_generic_or_short_leaf_description"]],
    }
    rows: list[dict[str, Any]] = []
    for name, items in groups.items():
        n = len(items)
        rows.append({"group": name, "n": n, "exact_at_100": sum(int(r["exact_at_100"]) for r in items) / n if n else 0.0, "hs6_at_100": sum(int(r["hs6_at_100"]) for r in items) / n if n else 0.0, "hs4_at_100": sum(int(r["hs4_at_100"]) for r in items) / n if n else 0.0, "mrr": sum(float(r["reciprocal_rank"]) for r in items) / n if n else 0.0})
    return rows


def output_paths(output_dir: Path) -> dict[str, Path]:
    return {
        "normative_hierarchical_results_csv": output_dir / "normative_hierarchical_results.csv",
        "normative_hierarchical_case_summary_csv": output_dir / "normative_hierarchical_case_summary.csv",
        "normative_hierarchical_failure_cases_csv": output_dir / "normative_hierarchical_failure_cases.csv",
        "normative_hierarchical_metrics_json": output_dir / "normative_hierarchical_metrics.json",
        "hierarchical_coverage_summary_json": output_dir / "hierarchical_coverage_summary.json",
        "hierarchical_coverage_summary_csv": output_dir / "hierarchical_coverage_summary.csv",
        "position_distribution_csv": output_dir / "position_distribution.csv",
        "position_distribution_json": output_dir / "position_distribution.json",
        "corpus_hierarchical_audit_json": output_dir / "corpus_hierarchical_audit.json",
        "historical_flat_vs_normative_hierarchical_compatibility_json": output_dir / "historical_flat_vs_normative_hierarchical_compatibility_v0.2.json",
        "flat_vs_hierarchical_comparison_csv": output_dir / "flat_vs_hierarchical_comparison_v0.2.csv",
        "hierarchical_coverage_comparison_csv": output_dir / "hierarchical_coverage_comparison_v0.2.csv",
        "limitation_stratified_metrics_csv": output_dir / "limitation_stratified_metrics_v0.2.csv",
        "run_metadata_json": output_dir / "run_metadata.json",
        "summary_md": output_dir / "summary.md",
    }


def summary_md(payload: Mapping[str, Any]) -> str:
    m = payload["metrics"]
    c = payload["coverage_summary"]
    comp = payload["compatibility"]
    corpus = payload["corpus_audit"]
    metric_rows = ["| Metrica | Numerador | Denominador | Valor |", "| --- | ---: | ---: | ---: |"]
    keep = {"mrr", "top_1", "top_3", "top_5", "top_10", "top_50", "recall_at_100", "pool_recall_at_200", "hs6_at_100", "hs4_at_100", "chapter_at_100", "hs6_at_200", "hs4_at_200", "chapter_at_200"}
    for row in m["metric_table"]:
        if row["metric"] in keep:
            metric_rows.append(f"| {row['metric']} | {row['numerator']} | {row['denominator']} | {float(row['value']):.12f} |")
    compare_rows = ["| Metrica | Plano v0.2 | Jerarquico v0.2 | Delta |", "| --- | ---: | ---: | ---: |"]
    for row in payload["flat_vs_hierarchical_comparison"]:
        compare_rows.append(f"| {row['metric']} | {float(row['flat_v0_2']):.12f} | {float(row['hierarchical_v0_2']):.12f} | {float(row['delta_hierarchical_minus_flat']):.12f} |")
    cov_rows = ["| Cobertura | Plano | Jerarquico | Delta |", "| --- | ---: | ---: | ---: |"]
    for row in payload["hierarchical_coverage_comparison"][:4]:
        cov_rows.append(f"| {row['coverage']} | {float(row['flat_v0_2']):.12f} | {float(row['hierarchical_v0_2']):.12f} | {float(row['delta_hierarchical_minus_flat']):.12f} |")
    return "\n".join([
        "# EXP-04 Fase C - BM25 normativo jerarquico data_aduanas clase 87 v0.2", "",
        "## Alcance", "",
        "Se evaluo exclusivamente BM25 normativo jerarquico sobre el evalset data_aduanas clase 87 v0.2. No se ejecuto BM25 dual protegido, mezcla 70/30, union diagnostica, Text2Trade, dense retrieval, candidate pools, integracion historico-normativa, RAG, reranking LLM ni explicador LLM.", "",
        "## Pipeline jerarquico", "",
        "- Constructor de corpus: `src/corpus/build_hierarchical_nandina_corpus.py`.",
        "- Constructor de indice: `src/experiments/build_bm25_hierarchical_index.py`.",
        "- Runner exclusivo Fase C: `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`.",
        "- Modulo BM25: `src/bm25_index.py` y `src/retrieval/bm25.py`.",
        f"- Corpus: `{payload['inputs']['hierarchical_corpus']}`.",
        f"- Corpus SHA-256: `{payload['inputs']['hierarchical_corpus_sha256']}`.",
        f"- Indice: `{payload['inputs']['hierarchical_index']}`.",
        f"- Indice SHA-256: `{payload['inputs']['hierarchical_index_sha256']}`.",
        f"- Version normativa en corpus: {', '.join(corpus['version_values'])}.",
        f"- Fuente: {', '.join(corpus['source_values'])}.",
        f"- Unidad documental: {corpus['document_unit']}.",
        f"- Regla de texto: {corpus['build_rule']}.", "",
        "## Auditoria del corpus", "",
        f"- Documentos jerarquicos totales: {corpus['records_total']}.",
        f"- Documentos NANDINA-8: {corpus['nandina_8_rows']}.",
        f"- Codigos NANDINA-8 unicos: {corpus['nandina_8_unique_codes']}.",
        f"- Codigos con multiples documentos: {corpus['nandina_8_codes_with_multiple_documents']}.",
        f"- Sin padre 4D explicito: {corpus['metadata_counts']['cantidad_sin_padre_4d']}.",
        f"- Sin padre HS6 explicito: {corpus['metadata_counts']['cantidad_sin_padre_hs6']}.",
        f"- Sin ambos padres: {corpus['metadata_counts']['cantidad_sin_padres']}.",
        f"- Conflictos en auditoria fuente: {corpus['versioned_audit_counts']['source_conflicting_parent_duplicates']}.", "",
        "## Evalset y query", "",
        f"- Evalset: `{payload['inputs']['evalset']}`.",
        f"- Evalset SHA-256: `{payload['inputs']['evalset_sha256']}`.",
        f"- Casos evaluados: {m['cases_evaluated']}.",
        f"- Query: `{payload['columns']['query']}`.",
        f"- Etiqueta: `{payload['columns']['label']}`.",
        f"- Profundidad efectiva: {payload['parameters']['retrieval_depth']}.", "",
        "## Resultado global", "", *metric_rows, "",
        "## Cobertura jerarquica", "",
        f"- Referencias en corpus: {c['eval_cases_covered_by_corpus']}/{c['eval_cases']}.",
        f"- Exact@100: {m['exact_at_100_numerator']}/{m['exact_at_100_denominator']} = {m['exact_at_100']:.12f}.",
        f"- HS6@100: {m['hs6_at_100_numerator']}/{m['hs6_at_100_denominator']} = {m['hs6_at_100']:.12f}.",
        f"- HS4@100: {m['hs4_at_100_numerator']}/{m['hs4_at_100_denominator']} = {m['hs4_at_100']:.12f}.",
        f"- Chapter@100: {m['chapter_at_100_numerator']}/{m['chapter_at_100_denominator']} = {m['chapter_at_100']:.12f}.",
        f"- Exact@200: {m['exact_at_200_numerator']}/{m['exact_at_200_denominator']} = {m['exact_at_200']:.12f}.",
        f"- HS6@200: {m['hs6_at_200_numerator']}/{m['hs6_at_200_denominator']} = {m['hs6_at_200']:.12f}.",
        f"- HS4@200: {m['hs4_at_200_numerator']}/{m['hs4_at_200_denominator']} = {m['hs4_at_200']:.12f}.",
        f"- Chapter@200: {m['chapter_at_200_numerator']}/{m['chapter_at_200_denominator']} = {m['chapter_at_200']:.12f}.", "",
        "## Comparacion plano vs jerarquico", "", *compare_rows, "",
        "## Cobertura comparable plano vs jerarquico", "", *cov_rows, "",
        "## Compatibilidad", "",
        f"- Mismo set case_id historico/plano/jerarquico: {comp['identical_case_id_set']}.",
        f"- Mismas etiquetas por case_id: {comp['identical_labels']}.",
        f"- Eval hash historico/plano/jerarquico: {comp['eval_hash_historical']} / {comp['eval_hash_flat']} / {comp['eval_hash_hierarchical']}.",
        f"- Compatible: {comp['compatible']}.", "",
        "## Controles", "",
        "- No se uso descripcion comercial evaluada para construir corpus.",
        "- No se uso NANDINA verdadera como parte de la query.",
        "- No se usaron DAM, SERIE, resultado historico, Top-3 historico ni outputs de otra estrategia como features de recuperacion.",
        "- El ranking efectivo elimina codigos repetidos por primera aparicion BM25 antes de calcular metricas.",
        "- Los hashes de Fase A/B permanecen iguales a los aprobados.", "",
        "## Estado Gate C", "", "GATE C APROBADO" if payload["gate_c_status"] == "APPROVED" else "GATE C NO APROBADO", "",
    ])


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    started = time.perf_counter()
    root = project_root()
    eval_path = resolve_project_path(args.evalset)
    corpus_path = resolve_project_path(args.hierarchical_corpus)
    corpus_meta_path = resolve_project_path(args.hierarchical_corpus_metadata)
    index_path = resolve_project_path(args.hierarchical_index)
    index_meta_path = resolve_project_path(args.hierarchical_index_metadata)
    audit_path = resolve_project_path(args.hierarchical_audit)
    config_path = resolve_project_path(args.config)
    hist_case_path = resolve_project_path(args.historical_case_summary)
    hist_meta_path = resolve_project_path(args.historical_metadata)
    flat_case_path = resolve_project_path(args.flat_case_summary)
    flat_metrics_path = resolve_project_path(args.flat_metrics)
    flat_meta_path = resolve_project_path(args.flat_metadata)
    output_dir = resolve_project_path(args.output_dir)
    depth = max(args.retrieval_depth, 200)

    eval_sha = validate_hash(eval_path, EXPECTED_EVAL_SHA256, "evalset v0.2")
    corpus_sha = validate_hash(corpus_path, EXPECTED_HIERARCHICAL_CORPUS_SHA256, "hierarchical corpus")
    index_sha = validate_hash(index_path, EXPECTED_HIERARCHICAL_INDEX_SHA256, "hierarchical index")
    config_sha = validate_hash(config_path, EXPECTED_CONFIG_SHA256, "config")
    corpus_meta_sha = sha256_file(corpus_meta_path)
    index_meta_sha = sha256_file(index_meta_path)
    audit_sha = sha256_file(audit_path)

    eval_rows = read_csv(eval_path)
    validate_eval(eval_rows)
    corpus_meta = read_json(corpus_meta_path)
    index_meta = read_json(index_meta_path)
    audit = read_json(audit_path)
    if index_meta.get("input", {}).get("corpus_sha256") != corpus_sha:
        raise ValueError("Hierarchical index metadata corpus hash does not match locked corpus")
    if corpus_meta.get("input_sha256") != EXPECTED_HIERARCHICAL_SOURCE_CORPUS_SHA256:
        raise ValueError("Hierarchical corpus metadata source hash mismatch")
    if not all([corpus_meta.get("output_sha256") == corpus_sha, audit.get("input", {}).get("sha256") == EXPECTED_HIERARCHICAL_SOURCE_CORPUS_SHA256, corpus_meta.get("total_documentos_generados") == 7648, corpus_meta.get("cantidad_sin_padre_4d") == 407, corpus_meta.get("cantidad_sin_padre_hs6") == 4504]):
        raise ValueError("Hierarchical corpus cannot be linked unambiguously to the versioned methodology audit")

    bm25_params = index_meta.get("bm25_params", {})
    bm25_config = read_json(config_path).get("bm25", {})
    index = load_bm25_index(index_path)
    if float(index.k1) != float(bm25_params.get("k1")) or float(index.b) != float(bm25_params.get("b")):
        raise ValueError("Loaded index parameters do not match metadata")

    corpus_by_code, code_flags, corpus_stats = corpus_maps(read_jsonl(corpus_path), corpus_meta, audit)
    eval_codes = {code8(row.get(LABEL_COLUMN)) for row in eval_rows}
    if not eval_codes <= set(corpus_by_code):
        raise ValueError(f"Eval reference codes absent from hierarchical corpus: {sorted(eval_codes - set(corpus_by_code))}")
    prev_hashes = previous_hashes(root)
    if not prev_hashes["all_match_expected"]:
        raise ValueError("Approved Phase A/B artifact hashes changed before Phase C")

    case_rows: list[dict[str, Any]] = []
    candidate_rows: list[dict[str, Any]] = []
    repeated_raw_rows: list[dict[str, Any]] = []
    label_in_query_count = 0
    raw_depth = len(index.doc_ids)
    for eval_row in eval_rows:
        query = clean(eval_row.get(QUERY_COLUMN))
        expected = code8(eval_row.get(LABEL_COLUMN))
        if expected in re.sub(r"\D", "", query):
            label_in_query_count += 1
        raw_hits = retrieve(index, query, top_n=raw_depth)
        hits, collapse = collapse_hits(raw_hits, depth)
        if collapse["raw_repeated_code_count"]:
            repeated_raw_rows.append({"case_id": clean(eval_row.get("case_id")), "raw_repeated_code_count": collapse["raw_repeated_code_count"], "raw_repeated_codes": " ".join(collapse["raw_repeated_codes"]), "effective_has_repeated_codes": int(collapse["effective_has_repeated_codes"]), "collapse_rule": collapse["collapse_rule"]})
        rank = rank_of_true(hits, expected)
        top1 = hits[0] if hits else {}
        flags = code_flags.get(expected, {})
        row: dict[str, Any] = {
            "case_id": clean(eval_row.get("case_id")), "id_unico": clean(eval_row.get("id_unico")), "declaracion": clean(eval_row.get("DECLARACION")), "serie": clean(eval_row.get("SERIE")), "query": query,
            "nandina_ref": expected, "partida_ref": expected[:4], "sub_partida_ref": expected[:6], "clase_ref": expected[:2], "reference_code_in_corpus": expected in corpus_by_code, "reference_doc_id": clean(corpus_by_code.get(expected, {}).get("doc_id")),
            "rank_ref": rank, "position_bucket": position_bucket(rank), "coverage_class": "reference_code_absent_from_corpus" if expected not in corpus_by_code else (position_bucket(rank) if rank > 0 else f"present_not_recovered_top_{depth}"),
            "retrieved_count": len(hits), "raw_retrieved_count": collapse["raw_retrieved_count"], "raw_repeated_code_count": collapse["raw_repeated_code_count"], "effective_ranking_has_repeated_codes": int(collapse["effective_has_repeated_codes"]),
            "top1_code": clean(top1.get("code")), "top1_doc_id": clean(corpus_by_code.get(clean(top1.get("code")), {}).get("doc_id")) if top1 else "", "top1_score": top1.get("score", "") if top1 else "", "reciprocal_rank": mrr_from_rank(rank), "method": METHOD,
            "flag_missing_parent_4d": bool(flags.get("missing_parent_4d", False)), "flag_missing_parent_hs6": bool(flags.get("missing_parent_hs6", False)), "flag_missing_both_parents": bool(flags.get("missing_both_parents", False)), "flag_duplicate_code_documents": bool(flags.get("duplicate_code_documents", False)), "flag_generic_or_short_leaf_description": bool(flags.get("generic_or_short_leaf_description", False)),
        }
        for k in K_VALUES:
            row[f"hit_top_{k}"] = int(acc_at_k(rank, k))
        for k in RECALL_K_VALUES:
            row[f"hit_recall_{k}"] = int(acc_at_k(rank, k))
        for k in HIERARCHICAL_K_VALUES:
            row[f"exact_at_{k}"] = int(acc_at_k(rank, k))
            row[f"hs6_at_{k}"] = family_hit(hits, expected, 6, k)
            row[f"hs4_at_{k}"] = family_hit(hits, expected, 4, k)
            row[f"chapter_at_{k}"] = family_hit(hits, expected, 2, k)
        for k in [100, 200]:
            row[f"hierarchical_evidence_class_at_{k}"] = evidence_class(row, k)
        case_rows.append(row)
        for hit in hits:
            cand_code = clean(hit.get("code"))
            candidate_rows.append({"case_id": clean(eval_row.get("case_id")), "id_unico": clean(eval_row.get("id_unico")), "nandina_ref": expected, "candidate_rank": int(hit["rank"]), "candidate_raw_rank": int(hit.get("raw_rank", hit["rank"])), "candidate_doc_id": clean(corpus_by_code.get(cand_code, {}).get("doc_id")) or f"NANDINA_{cand_code}", "candidate_code": cand_code, "candidate_partida": cand_code[:4], "candidate_sub_partida": cand_code[:6], "candidate_clase": cand_code[:2], "score": float(hit["score"]), "candidate_text": clean(hit.get("text"))[:240], "is_reference_code": int(cand_code == expected), "method": METHOD})

    metrics = metrics_from_cases(case_rows)
    pos_rows = position_distribution(case_rows)
    cov100 = coverage_distribution(case_rows, "hierarchical_evidence_class_at_100")
    cov200 = coverage_distribution(case_rows, "hierarchical_evidence_class_at_200")
    for row in cov100:
        row["k"] = 100
    for row in cov200:
        row["k"] = 200
    coverage_summary = {
        "eval_unique_codes": len(eval_codes), "eval_codes_covered_by_corpus": len(eval_codes & set(corpus_by_code)), "eval_codes_absent_from_corpus": len(eval_codes - set(corpus_by_code)), "missing_eval_codes": sorted(eval_codes - set(corpus_by_code)),
        "eval_cases": len(case_rows), "eval_cases_covered_by_corpus": sum(bool(row["reference_code_in_corpus"]) for row in case_rows), "eval_cases_absent_from_corpus": sum(not bool(row["reference_code_in_corpus"]) for row in case_rows),
        "eval_cases_recovered_at_depth": sum(int(row["rank_ref"]) > 0 for row in case_rows), "eval_cases_covered_but_not_recovered_at_depth": sum(bool(row["reference_code_in_corpus"]) and int(row["rank_ref"]) <= 0 for row in case_rows), "eval_cases_covered_but_not_recovered_top_50": sum(bool(row["reference_code_in_corpus"]) and int(row["hit_top_50"]) == 0 for row in case_rows),
        "reference_present_but_not_exact_at_100": sum(bool(row["reference_code_in_corpus"]) and int(row["exact_at_100"]) == 0 for row in case_rows), "reference_present_but_not_exact_at_200": sum(bool(row["reference_code_in_corpus"]) and int(row["exact_at_200"]) == 0 for row in case_rows),
        "exact_recovered_at_100": metrics["exact_at_100_numerator"], "exact_recovered_at_200": metrics["exact_at_200_numerator"], "hs6_recovered_without_exact_at_100": sum(row["hierarchical_evidence_class_at_100"] == "hs6_recovered_without_exact" for row in case_rows), "hs6_recovered_without_exact_at_200": sum(row["hierarchical_evidence_class_at_200"] == "hs6_recovered_without_exact" for row in case_rows),
        "hs4_recovered_without_hs6_or_exact_at_100": sum(row["hierarchical_evidence_class_at_100"] == "hs4_recovered_without_hs6_or_exact" for row in case_rows), "hs4_recovered_without_hs6_or_exact_at_200": sum(row["hierarchical_evidence_class_at_200"] == "hs4_recovered_without_hs6_or_exact" for row in case_rows), "chapter_only_at_100": sum(row["hierarchical_evidence_class_at_100"] == "chapter_only" for row in case_rows), "chapter_only_at_200": sum(row["hierarchical_evidence_class_at_200"] == "chapter_only" for row in case_rows),
        "no_hierarchical_evidence_at_100": sum(row["hierarchical_evidence_class_at_100"] == "no_hierarchical_evidence" for row in case_rows), "no_hierarchical_evidence_at_200": sum(row["hierarchical_evidence_class_at_200"] == "no_hierarchical_evidence" for row in case_rows), "coverage_distribution_at_100": cov100, "coverage_distribution_at_200": cov200, "position_distribution": pos_rows, "depth": depth,
    }
    comp = compatibility(case_rows, read_csv(hist_case_path), read_csv(flat_case_path), read_json(hist_meta_path), read_json(flat_meta_path), eval_sha)
    compare_rows, coverage_compare_rows = comparison(read_json(flat_metrics_path), metrics)
    strat_rows = stratified(case_rows)
    validations = {
        "evalset_rows": len(eval_rows), "case_ids_unique": len({row["case_id"] for row in case_rows}) == len(case_rows), "all_case_ids_v02_eval": all(row["case_id"].startswith("DA-EVAL-V02-") for row in case_rows), "v01_eval_or_split_inputs_used": False, "hierarchical_methodology_uses_existing_v01_corpus_artifact": True,
        "true_labels_match_evalset": True, "same_case_ids_as_historical_v02": comp["identical_case_id_set"], "same_case_ids_as_flat_v02": comp["identical_case_id_set"], "same_labels_as_historical_and_flat_v02": comp["identical_labels"], "compatible_with_historical_and_flat_v02": comp["compatible"],
        "label_string_found_inside_query_count": label_in_query_count, "final_ranking_effective_codes_unique": all(int(row["effective_ranking_has_repeated_codes"]) == 0 for row in case_rows), "cases_with_repeated_codes_in_effective_ranking": sum(int(row["effective_ranking_has_repeated_codes"]) for row in case_rows), "cases_with_repeated_codes_in_raw_ranking": len(repeated_raw_rows),
        "llm_used": False, "text2trade_used": False, "dual_protected_used": False, "candidate_pool_used": False, "dense_retrieval_used": False, "rag_used": False, "historical_results_used_as_retrieval_features": False, "flat_results_used_as_retrieval_features": False, "dam_used_as_query_feature": False, "serie_used_as_query_feature": False, "phase_a_b_artifacts_preserved": prev_hashes["all_match_expected"],
    }
    gate = "APPROVED" if all([eval_sha == EXPECTED_EVAL_SHA256, len(eval_rows) == EXPECTED_EVAL_ROWS, corpus_stats["methodology_linkage"]["linked_to_approved_methodology"], validations["final_ranking_effective_codes_unique"], comp["compatible"], prev_hashes["all_match_expected"], label_in_query_count == 0]) else "NOT_APPROVED"
    payload: dict[str, Any] = {
        "version": DATASET_VERSION, "dataset_version": DATASET_VERSION, "experiment_id": EXPERIMENT_ID, "strategy": STRATEGY, "method": METHOD, "created_at_utc": datetime.now(timezone.utc).isoformat(), "runtime": {"python": platform.python_version(), "platform": platform.platform(), "packages": package_versions()}, "git": git_metadata(root), "command": " ".join([sys.executable, *sys.argv]),
        "inputs": {"evalset": rel(eval_path, root), "evalset_sha256": eval_sha, "hierarchical_corpus": rel(corpus_path, root), "hierarchical_corpus_sha256": corpus_sha, "hierarchical_corpus_metadata": rel(corpus_meta_path, root), "hierarchical_corpus_metadata_sha256": corpus_meta_sha, "hierarchical_index": rel(index_path, root), "hierarchical_index_sha256": index_sha, "hierarchical_index_metadata": rel(index_meta_path, root), "hierarchical_index_metadata_sha256": index_meta_sha, "hierarchical_audit": rel(audit_path, root), "hierarchical_audit_sha256": audit_sha, "config": rel(config_path, root), "config_sha256": config_sha, "historical_case_summary": rel(hist_case_path, root), "historical_metadata": rel(hist_meta_path, root), "flat_case_summary": rel(flat_case_path, root), "flat_metrics": rel(flat_metrics_path, root), "flat_metadata": rel(flat_meta_path, root)},
        "columns": {"query": QUERY_COLUMN, "label": LABEL_COLUMN}, "parameters": {"retrieval_depth": depth, "raw_retrieval_depth": raw_depth, "k_values": K_VALUES, "recall_k_values": RECALL_K_VALUES, "hierarchical_k_values": HIERARCHICAL_K_VALUES, "k1": index.k1, "b": index.b, "use_stopwords_in_index_build": bm25_params.get("use_stopwords"), "configured_top_n": bm25_config.get("top_n"), "ranking_unit": "unique NANDINA-8 code", "duplicate_code_collapse_rule": "first BM25 occurrence by score order wins"},
        "corpus_audit": corpus_stats, "index_stats": {"docs_indexed": len(index.doc_ids), "unique_codes": len(set(index.doc_ids)), "duplicate_codes": len(index.doc_ids) - len(set(index.doc_ids)), "avgdl": index.avgdl, "vocab_size": len(index.idf)}, "validation": validations, "metrics": metrics, "coverage_summary": coverage_summary, "position_distribution": pos_rows, "compatibility": comp, "flat_vs_hierarchical_comparison": compare_rows, "hierarchical_coverage_comparison": coverage_compare_rows, "limitation_stratified_metrics": strat_rows, "previous_phase_artifact_hashes": prev_hashes, "gate_c_status": gate,
    }
    outputs = output_paths(output_dir)
    payload["outputs"] = {name: rel(path, root) for name, path in outputs.items()}
    case_fields = ["case_id", "id_unico", "declaracion", "serie", "query", "nandina_ref", "partida_ref", "sub_partida_ref", "clase_ref", "reference_code_in_corpus", "reference_doc_id", "rank_ref", "position_bucket", "coverage_class", "retrieved_count", "raw_retrieved_count", "raw_repeated_code_count", "effective_ranking_has_repeated_codes", "top1_code", "top1_doc_id", "top1_score", "reciprocal_rank", "method", "flag_missing_parent_4d", "flag_missing_parent_hs6", "flag_missing_both_parents", "flag_duplicate_code_documents", "flag_generic_or_short_leaf_description", *[f"hit_top_{k}" for k in K_VALUES], *[f"hit_recall_{k}" for k in RECALL_K_VALUES], *[item for k in HIERARCHICAL_K_VALUES for item in (f"exact_at_{k}", f"hs6_at_{k}", f"hs4_at_{k}", f"chapter_at_{k}")], "hierarchical_evidence_class_at_100", "hierarchical_evidence_class_at_200"]
    cand_fields = ["case_id", "id_unico", "nandina_ref", "candidate_rank", "candidate_raw_rank", "candidate_doc_id", "candidate_code", "candidate_partida", "candidate_sub_partida", "candidate_clase", "score", "candidate_text", "is_reference_code", "method"]
    write_csv(outputs["normative_hierarchical_results_csv"], candidate_rows, cand_fields)
    write_csv(outputs["normative_hierarchical_case_summary_csv"], case_rows, case_fields)
    write_csv(outputs["normative_hierarchical_failure_cases_csv"], [row for row in case_rows if int(row["rank_ref"]) <= 0 or int(row["rank_ref"]) > 50], case_fields)
    write_json(outputs["normative_hierarchical_metrics_json"], {key: payload[key] for key in ["version", "dataset_version", "experiment_id", "strategy", "method", "created_at_utc", "runtime", "git", "command", "inputs", "columns", "parameters", "index_stats", "validation", "metrics", "coverage_summary", "position_distribution", "compatibility", "flat_vs_hierarchical_comparison", "hierarchical_coverage_comparison", "limitation_stratified_metrics", "gate_c_status", "outputs"]})
    write_json(outputs["hierarchical_coverage_summary_json"], coverage_summary)
    write_csv(outputs["hierarchical_coverage_summary_csv"], cov100 + cov200, ["k", "coverage_class", "cases", "pct"])
    write_csv(outputs["position_distribution_csv"], pos_rows, ["position_bucket", "cases", "pct"])
    write_json(outputs["position_distribution_json"], {"position_distribution": pos_rows})
    write_json(outputs["corpus_hierarchical_audit_json"], corpus_stats)
    write_json(outputs["historical_flat_vs_normative_hierarchical_compatibility_json"], comp)
    write_csv(outputs["flat_vs_hierarchical_comparison_csv"], compare_rows, ["metric", "flat_v0_2", "hierarchical_v0_2", "delta_hierarchical_minus_flat"])
    write_csv(outputs["hierarchical_coverage_comparison_csv"], coverage_compare_rows, ["coverage", "flat_v0_2", "hierarchical_v0_2", "delta_hierarchical_minus_flat"])
    write_csv(outputs["limitation_stratified_metrics_csv"], strat_rows, ["group", "n", "exact_at_100", "hs6_at_100", "hs4_at_100", "mrr"])
    payload["elapsed_seconds"] = time.perf_counter() - started
    payload["output_sha256"] = {name: sha256_file(path) for name, path in outputs.items() if name not in {"run_metadata_json", "summary_md"}}
    write_text(outputs["summary_md"], summary_md(payload))
    payload["output_sha256"]["summary_md"] = sha256_file(outputs["summary_md"])
    write_json(outputs["run_metadata_json"], payload)
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate frozen hierarchical normative BM25 on data_aduanas Clase 87 v0.2.")
    parser.add_argument("--evalset", type=Path, default=DEFAULT_EVALSET)
    parser.add_argument("--hierarchical-corpus", type=Path, default=DEFAULT_HIERARCHICAL_CORPUS)
    parser.add_argument("--hierarchical-corpus-metadata", type=Path, default=DEFAULT_HIERARCHICAL_CORPUS_METADATA)
    parser.add_argument("--hierarchical-index", type=Path, default=DEFAULT_HIERARCHICAL_INDEX)
    parser.add_argument("--hierarchical-index-metadata", type=Path, default=DEFAULT_HIERARCHICAL_INDEX_METADATA)
    parser.add_argument("--hierarchical-audit", type=Path, default=DEFAULT_HIERARCHICAL_AUDIT)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--historical-case-summary", type=Path, default=DEFAULT_HISTORICAL_CASE_SUMMARY)
    parser.add_argument("--historical-metadata", type=Path, default=DEFAULT_HISTORICAL_METADATA)
    parser.add_argument("--flat-case-summary", type=Path, default=DEFAULT_FLAT_CASE_SUMMARY)
    parser.add_argument("--flat-metrics", type=Path, default=DEFAULT_FLAT_METRICS)
    parser.add_argument("--flat-metadata", type=Path, default=DEFAULT_FLAT_METADATA)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--retrieval-depth", type=int, default=200)
    return parser


def main() -> int:
    payload = evaluate(build_parser().parse_args())
    m = payload["metrics"]
    print("OK: EXP-04 Fase C BM25 normativo jerarquico v0.2 completado")
    print(f"Top-1={m['top_1']:.12f} Top-3={m['top_3']:.12f} Top-5={m['top_5']:.12f} Top-10={m['top_10']:.12f} Top-50={m['top_50']:.12f}")
    print(f"Recall@100={m['recall_at_100']:.12f} Pool/Recall@200={m['pool_recall_at_200']:.12f} MRR={m['mrr']:.12f}")
    print(f"HS6@100={m['hs6_at_100']:.12f} HS4@100={m['hs4_at_100']:.12f} Chapter@100={m['chapter_at_100']:.12f}")
    print(f"Gate C: {payload['gate_c_status']}")
    print(f"Outputs: {payload['outputs']['run_metadata_json']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

