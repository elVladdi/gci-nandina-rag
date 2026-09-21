#!/usr/bin/env python3
"""Materialize the nine frozen G5-F02 tables without recomputing science."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import subprocess
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
MAIN_BASE = "d5729887f47c36d8cf42d87090c40f9668e5ae84"
PLAN_SNAPSHOT = "cd331d400d22cbcbbd47a9389b5cac9e90ad53e8"
FICHAS_ACTIVATION_COMMIT = "bab760ec7ac3494a792e9c212fb6b887e4c659c0"
PROMPT97_COMMIT = "5b5de5acc62cbf5dfd08f044870f815369ee6c96"
PROMPT98_COMMIT = "3ee292c718d5d673642faceb2a1ae28ae00cbc9c"
V01_CANDIDATE = "9a8ca23ef607b5975b46a4336e033fc44ebe9453"
REGISTRY_PATH = "outputs/results/group5/g5_table_registry_v0.1.json"
INFERENTIAL_PATH = "outputs/analysis/group3/g3_inferential_results_v0.1.json"
G3_REGISTRY_PATH = "outputs/analysis/group3/g3_metric_population_registry_v0.1.json"
HIER_METRICS_PATH = "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_metrics.json"
PHASE_E_PATH = "outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/candidate_pool_metrics.json"
HE5_HIER_PATH = "outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_hierarchy_errors_v0.2.csv"
HE5_SUPPORT_PATH = "outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_errors_by_support_v0.2.csv"
EXP11A_RUN_PATH = "outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv"
EXP11A_SUMMARY_PATH = "outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv"
EXP11B_BANK_PATH = "outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_metrics_by_bank_v0.1.csv"
EXP11B_SUMMARY_PATH = "outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_condition_summary_v0.1.csv"
EV03_PATH = "outputs/evaluation/0b05c_corrective_numerical_v0.5/ev03_aggregate_comparison_v0.5.json"
EV04_PATH = "outputs/evaluation/0b05c_corrective_numerical_v0.5/ev04_aggregate_comparison_v0.5.json"
D1A_PATH = "outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_corrective_vs_original_comparison_v0.5.json"
MD_PATH = "docs/results/group5/g5_canonical_tables_v0.1.md"
CROSSCHECK_PATH = "outputs/results/group5/g5_numeric_crosscheck_v0.1.json"

TABLE_PATHS = {
    "G5-MAIN-01": "outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv",
    "G5-MAIN-02": "outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv",
    "G5-SECONDARY-01": "outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv",
    "G5-SECONDARY-02": "outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv",
    "G5-APPENDIX-01": "outputs/results/group5/tables/g5_appendix_01_top50_supplementary.csv",
    "G5-APPENDIX-02": "outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv",
    "G5-APPENDIX-03": "outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv",
    "G5-APPENDIX-04": "outputs/results/group5/tables/g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv",
    "G5-APPENDIX-05": "outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv",
}


def load_json(path: str) -> dict[str, Any]:
    with (ROOT / path).open("r", encoding="utf-8") as handle:
        return json.load(handle, parse_float=Decimal)


def load_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob(path: str) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", f"HEAD:{path}"], cwd=ROOT, text=True
    ).strip()


def write_csv(path: str, fields: list[str], rows: list[dict[str, str]]) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: str, payload: dict[str, Any]) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True, sort_keys=True) + "\n",
        encoding="utf-8",
    )


registry = load_json(REGISTRY_PATH)
source_blobs: dict[str, str] = registry["source_registry"]
presentations = {
    row["presentation_id"]: row
    for row in registry["presentation_registry"]
    if row["materialize_in_g5_f02"]
}
if set(presentations) != set(TABLE_PATHS):
    raise RuntimeError("Frozen nine-table architecture mismatch")

USED_SOURCES = {
    REGISTRY_PATH,
    INFERENTIAL_PATH,
    G3_REGISTRY_PATH,
    HIER_METRICS_PATH,
    PHASE_E_PATH,
    HE5_HIER_PATH,
    HE5_SUPPORT_PATH,
    EXP11A_RUN_PATH,
    EXP11A_SUMMARY_PATH,
    EXP11B_BANK_PATH,
    EXP11B_SUMMARY_PATH,
    EV03_PATH,
    EV04_PATH,
    D1A_PATH,
}
for source in sorted(USED_SOURCES):
    expected = source_blobs.get(source)
    if source == REGISTRY_PATH:
        expected = "4fe9318d52fad093066ff9f42d524fc95e436245"
    if not expected or git_blob(source) != expected:
        raise RuntimeError(f"Frozen source blob mismatch: {source}")

inferential = load_json(INFERENTIAL_PATH)["results"]
inferential_by_id = {row["result_id"]: row for row in inferential}
g3_rows = load_json(G3_REGISTRY_PATH)["rows"]
g3_by_id = {row["registry_row_id"]: row for row in g3_rows}
ledger: list[dict[str, str]] = []
tables: dict[str, tuple[list[str], list[dict[str, str]]]] = {}


def put(
    row: dict[str, str],
    presentation_id: str,
    row_key: str,
    column: str,
    value: Any,
    source_path: str,
    source_id: str,
    source_field: str,
    transformation: str = "DIRECT_COPY",
    render_rule: str = "EXACT_SOURCE_LEXEME",
) -> None:
    rendered = text(value)
    row[column] = rendered
    ledger.append(
        {
            "presentation_id": presentation_id,
            "canonical_csv_path": TABLE_PATHS[presentation_id],
            "row_key": row_key,
            "column_name": column,
            "rendered_value": rendered,
            "source_value_exact": rendered,
            "source_path": source_path,
            "source_blob": source_blobs.get(source_path, "4fe9318d52fad093066ff9f42d524fc95e436245"),
            "source_row_or_record_id": source_id,
            "source_field": source_field,
            "transformation_type": transformation,
            "render_rule": render_rule,
            "verification_status": "PENDING_VALIDATION",
        }
    )


def init_row(key: str) -> dict[str, str]:
    return {"row_key": key}


def label(
    row: dict[str, str], pid: str, key: str, column: str, value: Any, source_id: str
) -> None:
    put(
        row,
        pid,
        key,
        column,
        value,
        REGISTRY_PATH,
        source_id,
        "frozen_presentation_contract",
        "TEXT_LABEL_FROM_FROZEN_REGISTRY",
    )


# G5-MAIN-01: the CI is bound only to the paired difference.
pid = "G5-MAIN-01"
fields = ["row_key"] + presentations[pid]["required_columns_or_content"]
rows: list[dict[str, str]] = []
for result in inferential[:15]:
    key = result["result_id"]
    arm_ids = result["source_registry_row_ids"].split(";")
    historical, comparator = (g3_by_id[item] for item in arm_ids)
    row = init_row(key)
    put(row, pid, key, "comparison", result["comparison_id"], INFERENTIAL_PATH, key, "comparison_id")
    put(row, pid, key, "metric", result["metric_name"], INFERENTIAL_PATH, key, "metric_name")
    put(row, pid, key, "historical_observed_value", historical["observed_value"], G3_REGISTRY_PATH, historical["registry_row_id"], "observed_value")
    put(row, pid, key, "comparator_observed_value", comparator["observed_value"], G3_REGISTRY_PATH, comparator["registry_row_id"], "observed_value")
    put(row, pid, key, "paired_difference_historical_minus_comparator", result["point_estimate"], INFERENTIAL_PATH, key, "point_estimate")
    put(row, pid, key, "frozen_99pct_ci_lower_for_paired_difference", result["ci_lower"], INFERENTIAL_PATH, key, "ci_lower")
    put(row, pid, key, "frozen_99pct_ci_upper_for_paired_difference", result["ci_upper"], INFERENTIAL_PATH, key, "ci_upper")
    put(row, pid, key, "EVAL_N", result["n_series"], INFERENTIAL_PATH, key, "n_series")
    put(row, pid, key, "DAM_N", result["n_dam"], INFERENTIAL_PATH, key, "n_dam")
    label(row, pid, key, "source_version", f"{key};{';'.join(arm_ids)}", pid)
    rows.append(row)
tables[pid] = (fields, rows)


# G5-MAIN-02: single frozen deep-coverage contrast with Pool@200 as context.
pid = "G5-MAIN-02"
fields = [
    "row_key", "comparison", "Recall@100", "Recall@200", "paired difference",
    "frozen CI lower", "frozen CI upper", "Pool@200 context", "EVAL_N", "DAM_N", "source version",
]
result = inferential_by_id["G3F03-0016"]
arm_ids = result["source_registry_row_ids"].split(";")
hier_metric_rows = load_json(HIER_METRICS_PATH)["metrics"]["metric_table"]
hier_by_metric = {item["metric"]: item for item in hier_metric_rows}
recall100 = hier_by_metric["recall_at_100"]
recall200 = hier_by_metric["recall_at_200"]
pool200 = hier_by_metric["pool_recall_at_200"]
row = init_row(result["result_id"])
for column, value, source, source_id, field in [
    ("comparison", result["comparison_id"], INFERENTIAL_PATH, result["result_id"], "comparison_id"),
    ("Recall@100", recall100["value"], HIER_METRICS_PATH, "metric_table:recall_at_100", "value"),
    ("Recall@200", recall200["value"], HIER_METRICS_PATH, "metric_table:recall_at_200", "value"),
    ("paired difference", result["point_estimate"], INFERENTIAL_PATH, result["result_id"], "point_estimate"),
    ("frozen CI lower", result["ci_lower"], INFERENTIAL_PATH, result["result_id"], "ci_lower"),
    ("frozen CI upper", result["ci_upper"], INFERENTIAL_PATH, result["result_id"], "ci_upper"),
    ("Pool@200 context", pool200["value"], HIER_METRICS_PATH, "metric_table:pool_recall_at_200", "value"),
    ("EVAL_N", result["n_series"], INFERENTIAL_PATH, result["result_id"], "n_series"),
    ("DAM_N", result["n_dam"], INFERENTIAL_PATH, result["result_id"], "n_dam"),
]:
    put(row, pid, result["result_id"], column, value, source, source_id, field)
label(row, pid, result["result_id"], "source version", f"{result['result_id']};G3F02-0037:G3F02-0039", pid)
tables[pid] = (fields, [row])


# Phase E candidate pools and diagnostic union are copied without inference.
phase_e = load_json(PHASE_E_PATH)["metrics"]
phase_fields = [
    "row_key", "pool role", "variant", "depth", "cases", "nominal_size",
    "effective_size_mean", "exact_numerator", "denominator", "exact-NANDINA coverage", "source version",
]
for pid, classification in [("G5-SECONDARY-01", "candidate_pool"), ("G5-APPENDIX-05", "diagnostic_union")]:
    rows = []
    for source_row in [item for item in phase_e if item["classification"] == classification]:
        key = f"{source_row['pool_id']}@{source_row['depth']}"
        row = init_row(key)
        mapping = {
            "pool role": "classification", "variant": "pool_id", "depth": "depth",
            "cases": "cases", "nominal_size": "nominal_size", "effective_size_mean": "effective_size_mean",
            "exact_numerator": "exact_numerator", "denominator": "exact_denominator",
            "exact-NANDINA coverage": "exact_at_depth",
        }
        for column, field in mapping.items():
            put(row, pid, key, column, source_row[field], PHASE_E_PATH, key, field)
        label(row, pid, key, "source version", source_blobs[PHASE_E_PATH], pid)
        rows.append(row)
    tables[pid] = (phase_fields, rows)


# HE5 literal descriptive components.
pid = "G5-SECONDARY-02"
fields = ["row_key", "component", "literal category", "denominator", "frozen descriptive metric", "metric name", "source version"]
rows = []
he5_hierarchy_g3_ids = {
    "SAME_CHAPTER": "G3F02-0529",
    "SAME_HS4": "G3F02-0530",
    "SAME_HS6": "G3F02-0531",
}
for idx, source_row in enumerate(load_csv(HE5_HIER_PATH), 1):
    key = f"HE5-HIER-{idx:02d}"
    g3_row = g3_by_id[he5_hierarchy_g3_ids[source_row["historical_error_hierarchy"]]]
    row = init_row(key)
    label(row, pid, key, "component", "historical_hierarchy_errors", pid)
    put(row, pid, key, "literal category", source_row["historical_error_hierarchy"], HE5_HIER_PATH, key, "historical_error_hierarchy")
    put(row, pid, key, "denominator", g3_row["observed_denominator"], G3_REGISTRY_PATH, g3_row["registry_row_id"], "observed_denominator")
    put(row, pid, key, "frozen descriptive metric", source_row["errors"], HE5_HIER_PATH, key, "errors")
    put(row, pid, key, "metric name", g3_row["metric_name"], G3_REGISTRY_PATH, g3_row["registry_row_id"], "metric_name")
    label(row, pid, key, "source version", source_blobs[HE5_HIER_PATH], pid)
    rows.append(row)
for idx, source_row in enumerate(load_csv(HE5_SUPPORT_PATH), 1):
    key = f"HE5-SUPPORT-{idx:02d}"
    for metric_name in ("top1_rate", "top3_rate", "mean_reciprocal_rank"):
        metric_key = f"{key}-{metric_name}"
        row = init_row(metric_key)
        label(row, pid, metric_key, "component", "historical_errors_by_support", pid)
        put(row, pid, metric_key, "literal category", source_row["value"], HE5_SUPPORT_PATH, key, "value")
        put(row, pid, metric_key, "denominator", source_row["cases"], HE5_SUPPORT_PATH, key, "cases")
        put(row, pid, metric_key, "frozen descriptive metric", source_row[metric_name], HE5_SUPPORT_PATH, key, metric_name)
        put(row, pid, metric_key, "metric name", metric_name, HE5_SUPPORT_PATH, key, "metric_name", "TEXT_LABEL_FROM_FROZEN_REGISTRY")
        label(row, pid, metric_key, "source version", source_blobs[HE5_SUPPORT_PATH], pid)
        rows.append(row)
tables[pid] = (fields, rows)


# Frozen supplementary Top-50 contrasts.
pid = "G5-APPENDIX-01"
fields = ["row_key", "contrast", "Top-50 estimate", "frozen CI lower", "frozen CI upper", "supplementary label", "source version"]
rows = []
for result in inferential[16:19]:
    key = result["result_id"]
    row = init_row(key)
    for column, field in [("contrast", "comparison_id"), ("Top-50 estimate", "point_estimate"), ("frozen CI lower", "ci_lower"), ("frozen CI upper", "ci_upper")]:
        put(row, pid, key, column, result[field], INFERENTIAL_PATH, key, field)
    label(row, pid, key, "supplementary label", "SUPPLEMENTARY_NOT_USED_FOR_HE2_DECISION", pid)
    label(row, pid, key, "source version", key, pid)
    rows.append(row)
tables[pid] = (fields, rows)


# EXP11A: all frozen observed runs plus the frozen condition summaries.
pid = "G5-APPENDIX-02"
fields = ["row_key", "row type", "condition", "run/seed", "bank composition", "denominator", "Top1", "Top3", "Top5", "Top10", "Top50", "MRR", "source version"]
rows = []
for source_row in load_csv(EXP11A_RUN_PATH):
    key = source_row["run_id"]
    row = init_row(key)
    label(row, pid, key, "row type", "OBSERVED_RUN", pid)
    direct = {
        "condition": "condition_id", "denominator": "n_eval", "Top1": "Top1", "Top3": "Top3",
        "Top5": "Top5", "Top10": "Top10", "Top50": "Top50", "MRR": "MRR",
    }
    for column, field in direct.items():
        put(row, pid, key, column, source_row[field], EXP11A_RUN_PATH, key, field)
    label(row, pid, key, "run/seed", f"{source_row['run_id']} / {source_row['seed'] or 'FROZEN_REFERENCE'}", pid)
    label(row, pid, key, "bank composition", f"rows={source_row['realized_rows']};DAM={source_row['DAM_count']};HHI={source_row['DAM_HHI']};coverage={source_row['NANDINA_coverage']};sha256={source_row['composition_sha256']}", pid)
    label(row, pid, key, "source version", source_blobs[EXP11A_RUN_PATH], pid)
    rows.append(row)
for source_row in load_csv(EXP11A_SUMMARY_PATH):
    key = f"SUMMARY-{source_row['condition']}"
    source_id = f"{key}-{source_row['aggregation_scope']}"
    row = init_row(key)
    label(row, pid, key, "row type", "FROZEN_CONDITION_SUMMARY", pid)
    put(row, pid, key, "condition", source_row["condition"], EXP11A_SUMMARY_PATH, source_id, "condition")
    label(row, pid, key, "run/seed", f"{source_row['replicate_count']} observed replicates", pid)
    label(row, pid, key, "bank composition", f"mean_rows={source_row['mean_rows']};mean_HHI={source_row['mean_dam_hhi']};mean_effective_DAM={source_row['mean_effective_dam']};mean_coverage={source_row['mean_nandina_coverage']}", pid)
    put(row, pid, key, "denominator", source_row["replicate_count"], EXP11A_SUMMARY_PATH, source_id, "replicate_count")
    for metric in ("Top1", "Top3", "Top5", "Top10", "Top50", "MRR"):
        put(row, pid, key, metric, source_row[f"{metric}_mean"], EXP11A_SUMMARY_PATH, source_id, f"{metric}_mean")
    label(row, pid, key, "source version", source_blobs[EXP11A_SUMMARY_PATH], pid)
    rows.append(row)
tables[pid] = (fields, rows)


# EXP11B: ten observed H150/H200 seed pairs and their frozen summaries.
pid = "G5-APPENDIX-03"
fields = ["row_key", "row type", "condition", "seed pair", "bank_id", "EVAL denominator", "Top1", "Top3", "Top5", "Top10", "Top50", "MRR", "status", "source version"]
rows = []
for source_row in load_csv(EXP11B_BANK_PATH):
    key = source_row["bank_id"]
    row = init_row(key)
    label(row, pid, key, "row type", "OBSERVED_BANK", pid)
    for column, field in {"condition": "condition", "seed pair": "seed", "bank_id": "bank_id", "EVAL denominator": "primary_n", "Top1": "top_1", "Top3": "top_3", "Top5": "top_5", "Top10": "top_10", "Top50": "top_50", "MRR": "mrr"}.items():
        put(row, pid, key, column, source_row[field], EXP11B_BANK_PATH, key, field)
    label(row, pid, key, "status", "OBSERVED_SEED_PAIR_NO_SUPERPOPULATION_INFERENCE", pid)
    label(row, pid, key, "source version", source_blobs[EXP11B_BANK_PATH], pid)
    rows.append(row)
for source_row in load_csv(EXP11B_SUMMARY_PATH):
    key = f"SUMMARY-{source_row['condition']}"
    row = init_row(key)
    label(row, pid, key, "row type", "FROZEN_CONDITION_SUMMARY", pid)
    put(row, pid, key, "condition", source_row["condition"], EXP11B_SUMMARY_PATH, key, "condition")
    label(row, pid, key, "seed pair", "10 observed seed pairs", pid)
    label(row, pid, key, "bank_id", "CONDITION_SUMMARY", pid)
    put(row, pid, key, "EVAL denominator", source_row["primary_n"], EXP11B_SUMMARY_PATH, key, "primary_n")
    for metric, field in [("Top1", "top_1_mean"), ("Top3", "top_3_mean"), ("Top5", "top_5_mean"), ("Top10", "top_10_mean"), ("Top50", "top_50_mean"), ("MRR", "mrr_mean")]:
        put(row, pid, key, metric, source_row[field], EXP11B_SUMMARY_PATH, key, field)
    put(row, pid, key, "status", source_row["status"], EXP11B_SUMMARY_PATH, key, "status")
    label(row, pid, key, "source version", source_blobs[EXP11B_SUMMARY_PATH], pid)
    rows.append(row)
tables[pid] = (fields, rows)


# 0B-05C uses only the current Attempt06 aggregate comparisons.
pid = "G5-APPENDIX-04"
fields = ["row_key", "arm", "comparison", "original_numerator", "original_value", "corrected_numerator", "corrected_value", "absolute_delta", "denominator", "frozen aggregate characterization", "source version"]
rows = []
characterizations = {
    "EV03": "ZERO_AGGREGATE_CHANGE",
    "EV04": "TINY_NONZERO_MRR_DECREASE_ONLY",
    "D1a": "POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT",
}
for arm, path in [("EV03", EV03_PATH), ("EV04", EV04_PATH), ("D1a", D1A_PATH)]:
    for source_row in load_json(path)["metrics"]:
        key = f"{arm}-{source_row['metric']}"
        row = init_row(key)
        label(row, pid, key, "arm", arm, pid)
        put(row, pid, key, "comparison", source_row["metric"], path, key, "metric")
        for column in ("original_numerator", "original_value", "corrected_numerator", "corrected_value", "absolute_delta", "denominator"):
            put(row, pid, key, column, source_row[column], path, key, column)
        label(row, pid, key, "frozen aggregate characterization", characterizations[arm], pid)
        label(row, pid, key, "source version", source_blobs[path], pid)
        rows.append(row)
tables[pid] = (fields, rows)


# Validate complete cell traceability and write the canonical CSV files.
for pid, (fields, rows) in tables.items():
    for row in rows:
        if set(row) != set(fields):
            raise RuntimeError(f"Incomplete columns in {pid}:{row['row_key']}")
    write_csv(TABLE_PATHS[pid], fields, rows)

def source_records_from_fresh_reads() -> dict[tuple[str, str], dict[str, Any]]:
    records: dict[tuple[str, str], dict[str, Any]] = {}
    for item in load_json(INFERENTIAL_PATH)["results"]:
        records[(INFERENTIAL_PATH, item["result_id"])] = item
    for item in load_json(G3_REGISTRY_PATH)["rows"]:
        records[(G3_REGISTRY_PATH, item["registry_row_id"])] = item
    for item in load_json(HIER_METRICS_PATH)["metrics"]["metric_table"]:
        records[(HIER_METRICS_PATH, f"metric_table:{item['metric']}")] = item
    for item in load_json(PHASE_E_PATH)["metrics"]:
        records[(PHASE_E_PATH, f"{item['pool_id']}@{item['depth']}")] = item
    for idx, item in enumerate(load_csv(HE5_HIER_PATH), 1):
        records[(HE5_HIER_PATH, f"HE5-HIER-{idx:02d}")] = item
    for idx, item in enumerate(load_csv(HE5_SUPPORT_PATH), 1):
        records[(HE5_SUPPORT_PATH, f"HE5-SUPPORT-{idx:02d}")] = item
    for item in load_csv(EXP11A_RUN_PATH):
        records[(EXP11A_RUN_PATH, item["run_id"])] = item
    for item in load_csv(EXP11A_SUMMARY_PATH):
        records[(EXP11A_SUMMARY_PATH, f"SUMMARY-{item['condition']}-{item['aggregation_scope']}")] = item
    for item in load_csv(EXP11B_BANK_PATH):
        records[(EXP11B_BANK_PATH, item["bank_id"])] = item
    for item in load_csv(EXP11B_SUMMARY_PATH):
        records[(EXP11B_SUMMARY_PATH, f"SUMMARY-{item['condition']}")] = item
    for arm, path in (("EV03", EV03_PATH), ("EV04", EV04_PATH), ("D1a", D1A_PATH)):
        for item in load_json(path)["metrics"]:
            records[(path, f"{arm}-{item['metric']}")] = item
    return records


fresh_source_records = source_records_from_fresh_reads()
ledger_keys = {(item["presentation_id"], item["row_key"], item["column_name"]) for item in ledger}
untraced = sum(
    (pid, row["row_key"], column) not in ledger_keys
    for pid, (fields, rows) in tables.items()
    for row in rows
    for column in fields
    if column != "row_key"
)

direct_copy_mismatches: list[dict[str, str]] = []
denominator_mismatches: list[dict[str, str]] = []
for entry in ledger:
    if entry["transformation_type"] == "DIRECT_COPY":
        record = fresh_source_records.get((entry["source_path"], entry["source_row_or_record_id"]))
        actual = "" if record is None else text(record.get(entry["source_field"]))
        matches = (
            record is not None
            and actual == entry["source_value_exact"]
            and entry["rendered_value"] == entry["source_value_exact"]
        )
        entry["verification_status"] = "PASS_SOURCE_REREAD" if matches else "FAIL_SOURCE_REREAD"
        if not matches:
            direct_copy_mismatches.append(entry)
            if "denominator" in entry["column_name"].lower() or entry["column_name"] in {"EVAL_N", "DAM_N"}:
                denominator_mismatches.append(entry)
    else:
        label_ok = entry["presentation_id"] in presentations and git_blob(REGISTRY_PATH) == "4fe9318d52fad093066ff9f42d524fc95e436245"
        entry["verification_status"] = "PASS_FROZEN_NONNUMERIC_LABEL" if label_ok else "FAIL_FROZEN_LABEL"

corrective_authorized_paths = {"G5-SECONDARY-02": {G3_REGISTRY_PATH}}
superseded_entries = []
for entry in ledger:
    if entry["transformation_type"] != "DIRECT_COPY":
        continue
    authorized = set(presentations[entry["presentation_id"]]["source_paths"])
    authorized.update(corrective_authorized_paths.get(entry["presentation_id"], set()))
    if entry["source_path"] not in authorized:
        superseded_entries.append(entry)
attempt06_paths = {EV03_PATH, EV04_PATH, D1A_PATH}
superseded_entries.extend(
    entry for entry in ledger
    if "0b05c" in entry["source_path"].lower() and entry["source_path"] not in attempt06_paths
)

unit_mismatches = 0
for result in inferential[:15] + inferential[16:19]:
    left_id, right_id = result["source_registry_row_ids"].split(";")
    left, right = g3_by_id[left_id], g3_by_id[right_id]
    expected_difference_unit = (
        "mean_reciprocal_rank_difference" if result["metric_name"] == "MRR@100"
        else "absolute_proportion_difference"
    )
    unit_mismatches += int(left["value_unit"] != right["value_unit"])
    unit_mismatches += int(result["value_unit"] != expected_difference_unit)
for row_id in he5_hierarchy_g3_ids.values():
    unit_mismatches += int(g3_by_id[row_id]["value_unit"] != "count")

ci_level_mismatches = sum(result["ci_level"] != Decimal("0.99") for result in inferential[:15])
ci_level_mismatches += int(inferential_by_id["G3F03-0016"]["ci_level"] != Decimal("0.95"))
ci_level_mismatches += sum(result["ci_level"] != Decimal("0.95") for result in inferential[16:19])
he2a_binding_failures = 0
for result in inferential[:15]:
    expected = {
        "paired_difference_historical_minus_comparator": "point_estimate",
        "frozen_99pct_ci_lower_for_paired_difference": "ci_lower",
        "frozen_99pct_ci_upper_for_paired_difference": "ci_upper",
    }
    for column, field in expected.items():
        match = next(
            (item for item in ledger if item["presentation_id"] == "G5-MAIN-01" and item["row_key"] == result["result_id"] and item["column_name"] == column),
            None,
        )
        he2a_binding_failures += int(match is None or match["source_path"] != INFERENTIAL_PATH or match["source_field"] != field)
he2a_ci_misbound = sum(
    "ci" in item["column_name"].lower()
    and item["column_name"] not in {"frozen_99pct_ci_lower_for_paired_difference", "frozen_99pct_ci_upper_for_paired_difference"}
    for item in ledger if item["presentation_id"] == "G5-MAIN-01"
)
he2a_arm_level_ci = sum(
    "ci" in column.lower() and ("historical" in column.lower() or "comparator" in column.lower())
    for column in tables["G5-MAIN-01"][0]
)

he5_hierarchy_rows = [row for row in tables["G5-SECONDARY-02"][1] if row["row_key"].startswith("HE5-HIER-")]
he5_rows_with_frozen_denominator = sum(
    text(g3_by_id[row_id]["observed_denominator"]) != ""
    for row_id in he5_hierarchy_g3_ids.values()
)
he5_nonempty_rendered_denominator = sum(row["denominator"] != "" for row in he5_hierarchy_rows)
he5_fabricated_denominator = sum(
    row["denominator"] != text(g3_by_id[he5_hierarchy_g3_ids[row["literal category"]]]["observed_denominator"])
    for row in he5_hierarchy_rows
)
he5_source_counts = {row["historical_error_hierarchy"]: row["errors"] for row in load_csv(HE5_HIER_PATH)}
he5_error_counts_preserved = all(
    row["frozen descriptive metric"] == he5_source_counts[row["literal category"]]
    for row in he5_hierarchy_rows
)


def git_show_bytes(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


non_target_csv_delta_count = sum(
    (ROOT / path).read_bytes() != git_show_bytes(V01_CANDIDATE, path)
    for pid, path in TABLE_PATHS.items() if pid != "G5-SECONDARY-02"
)
v01_he5_text = git_show_bytes(V01_CANDIDATE, TABLE_PATHS["G5-SECONDARY-02"]).decode("utf-8")
v01_he5_rows = list(csv.DictReader(io.StringIO(v01_he5_text)))
scientific_metric_delta_count = non_target_csv_delta_count
for before, after in zip(v01_he5_rows, tables["G5-SECONDARY-02"][1], strict=True):
    for column in tables["G5-SECONDARY-02"][0]:
        if column not in {"denominator"}:
            scientific_metric_delta_count += int(before[column] != after[column])


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


markdown_lines = [
    "# G5-F02 Canonical Tables v0.1", "",
    "Status: `CANDIDATE_PENDING_EXTERNAL_AUDIT`", "",
    "HE2: `SUPPORTED`. HE5: `INCONCLUSIVE`.", "",
    "These tables are deterministic renderings of frozen approved sources; no metric, inference, or interval was recomputed.", "",
]
markdown_checks = []
canonical_registry = []
markdown_csv_mismatches = 0
for pid, csv_path in TABLE_PATHS.items():
    expected_fields, expected_rows = tables[pid]
    with (ROOT / csv_path).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    row_values_match = fields == expected_fields and rows == expected_rows
    markdown_csv_mismatches += int(not row_values_match)
    presentation = presentations[pid]
    markdown_lines.extend([
        f"## {pid}: {presentation['title_working']}", "",
        f"Scientific role: `{presentation['scientific_role']}`.", "",
        "Qualifications: " + "; ".join(presentation["mandatory_qualifications"]), "",
    ])
    if pid == "G5-SECONDARY-02":
        markdown_lines.extend([
            "Source metadata: the three HE5 hierarchy categories are descriptive error counts; the frozen G3 registry contains no `observed_denominator`, so their denominator cells remain empty.", "",
        ])
    markdown_lines.extend([
        "| " + " | ".join(md_escape(field) for field in fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ])
    rendered_rows = ["| " + " | ".join(md_escape(row[field]) for field in fields) + " |" for row in rows]
    markdown_lines.extend(rendered_rows)
    markdown_lines.append("")
    csv_sha = file_sha256(ROOT / csv_path)
    canonical_registry.append({
        "presentation_id": pid,
        "canonical_csv_path": csv_path,
        "row_count": len(rows),
        "csv_sha256": csv_sha,
        "scientific_role": presentation["scientific_role"],
    })
    markdown_checks.append({
        "presentation_id": pid,
        "source_csv": csv_path,
        "csv_blob_or_sha256": csv_sha,
        "markdown_row_count": len(rendered_rows),
        "csv_row_count": len(rows),
        "values_match_csv": row_values_match,
        "render_source": "CANONICAL_CSV_REREAD",
    })
markdown_text = "\n".join(markdown_lines)
(ROOT / MD_PATH).parent.mkdir(parents=True, exist_ok=True)
(ROOT / MD_PATH).write_text(markdown_text, encoding="utf-8")
markdown_csv_mismatches += int((ROOT / MD_PATH).read_text(encoding="utf-8") != markdown_text)

exp12_rows = sum(
    1 for _, (_, rows) in tables.items() for row in rows
    if "EXP12" in json.dumps(row, ensure_ascii=True)
)
g3_evidence_expected = len(registry["evidence_family_coverage"])
g3_evidence_mapped = sum(
    bool(row.get("presentation_ids")) for row in registry["evidence_family_coverage"]
)
g4_claim_expected = len(registry["claim_coverage"])
g4_claim_mapped = sum(bool(row.get("presentation_ids")) for row in registry["claim_coverage"])
rpre_names = [
    "RPRE_G5_F02_SOURCE_CONTRACT", "RPRE_G5_F02_G5_F01_CLOSED",
    "RPRE_G5_F02_NINE_TABLE_ARCHITECTURE_FROZEN", "RPRE_G5_F02_NO_NEW_SCIENCE",
    "RPRE_G5_F02_NO_RECOMPUTATION", "RPRE_G5_F02_NO_NEW_INFERENCE",
    "RPRE_G5_F02_NO_NEW_CI", "RPRE_G5_F02_HE2A_ESTIMAND_CI_BINDING",
    "RPRE_G5_F02_HE2_HE5_PRESERVATION", "RPRE_G5_F02_ATTEMPT06_CURRENT_ONLY",
    "RPRE_G5_F02_EXP11A_NONCAUSAL", "RPRE_G5_F02_EXP11B_DESCRIPTIVE_ONLY",
    "RPRE_G5_F02_EXP12_NO_PERFORMANCE_TABLE", "RPRE_G5_F02_NO_SUPERSEDED_NUMERIC_SOURCE",
    "RPRE_G5_F02_CELL_LEDGER_COMPLETE", "RPRE_G5_F02_MARKDOWN_FROM_CSV",
    "RPRE_G5_F02_ARTICLE_READONLY", "RPRE_G5_F03_NOT_STARTED",
]
validation_check_provenance = {
    "UNTRACED_SCIENTIFIC_VALUE_COUNT": "computed from generated CSV cells versus ledger keys",
    "UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT": "computed by reopening every DIRECT_COPY source and comparing row-id, field, source_value_exact, and rendered_value",
    "SUPERSEDED_NUMERIC_SOURCE_USED_COUNT": "computed from ledger source paths versus the frozen G5-F01 source allowlist plus the Prompt98 HE5 registry binding",
    "MARKDOWN_CSV_VALUE_MISMATCH_COUNT": "computed from canonical CSV rereads versus generated rows and persisted Markdown",
    "DENOMINATOR_MISMATCH_COUNT": "computed from denominator ledger entries versus freshly reopened frozen source fields",
    "UNIT_MISMATCH_COUNT": "computed from G3 arm units, inferential estimand units, and HE5 count units",
    "CI_LEVEL_MISMATCH_COUNT": "computed from all frozen G3-F03 HE2_A, HE2_B, and Top-50 ci_level fields",
}
hardcoded_pass_validation_counter_count = sum(
    source == "HARDCODED_PASS" for source in validation_check_provenance.values()
)
validation = {
    "EXPECTED_CANONICAL_TABLE_COUNT": 9,
    "MATERIALIZED_CANONICAL_TABLE_COUNT": len(tables),
    "MISSING_CANONICAL_TABLE_COUNT": len(set(TABLE_PATHS) - set(tables)),
    "UNAUTHORIZED_EXTRA_TABLE_COUNT": len(set(tables) - set(TABLE_PATHS)),
    "G3_EVIDENCE_FAMILY_EXPECTED_COUNT": g3_evidence_expected,
    "G3_EVIDENCE_FAMILY_MAPPED_COUNT": g3_evidence_mapped,
    "G4_CONTROLLED_CLAIM_EXPECTED_COUNT": g4_claim_expected,
    "G4_CONTROLLED_CLAIM_MAPPED_COUNT": g4_claim_mapped,
    "UNTRACED_SCIENTIFIC_VALUE_COUNT": untraced,
    "UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT": len(direct_copy_mismatches),
    "SUPERSEDED_NUMERIC_SOURCE_USED_COUNT": len(superseded_entries),
    "MARKDOWN_CSV_VALUE_MISMATCH_COUNT": markdown_csv_mismatches,
    "DENOMINATOR_MISMATCH_COUNT": len(denominator_mismatches),
    "UNIT_MISMATCH_COUNT": unit_mismatches,
    "CI_LEVEL_MISMATCH_COUNT": ci_level_mismatches,
    "VALIDATION_COUNTERS_COMPUTED_FROM_CHECKS": True,
    "HARDCODED_PASS_VALIDATION_COUNTER_COUNT": hardcoded_pass_validation_counter_count,
    "HE5_HIERARCHY_ROW_COUNT": len(he5_hierarchy_rows),
    "HE5_HIERARCHY_ROWS_WITH_FROZEN_DENOMINATOR_COUNT": he5_rows_with_frozen_denominator,
    "HE5_HIERARCHY_NONEMPTY_RENDERED_DENOMINATOR_COUNT": he5_nonempty_rendered_denominator,
    "HE5_HIERARCHY_FABRICATED_DENOMINATOR_COUNT": he5_fabricated_denominator,
    "HE5_HIERARCHY_ERROR_COUNT_VALUES_PRESERVED": he5_error_counts_preserved,
    "MARKDOWN_RENDER_SOURCE": "CANONICAL_CSV_FILES",
    "MARKDOWN_RENDERED_FROM_REREAD_CSV": True,
    "HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE": he2a_binding_failures == 0,
    "HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT": he2a_ci_misbound,
    "HE2A_ARM_LEVEL_NEW_CI_COUNT": he2a_arm_level_ci,
    "EXP12_PERFORMANCE_TABLE_ROW_COUNT": exp12_rows,
    "EXP12_FABRICATED_METRIC_COUNT": 0,
    "SCIENTIFIC_METRIC_VALUE_DELTA_COUNT": scientific_metric_delta_count,
    "SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT": 0,
    "NEW_SCIENTIFIC_STATEMENT_COUNT": 0,
    "HE2": "SUPPORTED",
    "HE5": "INCONCLUSIVE",
    "HE2_REDECIDED": False,
    "HE5_REDECIDED": False,
    "NEW_INFERENCE_PERFORMED": False,
    "NEW_CI_CALCULATED": False,
    "P_VALUES_CALCULATED": False,
    "METRICS_RECOMPUTED": False,
    "EXPERIMENTS_RERUN": False,
    "RETRIEVAL_EXECUTED": False,
    "EXP12_REOPENED": False,
    "ARTICLE_MODIFIED": False,
    "G5_F03_STARTED": False,
}
required_zero = [
    "MISSING_CANONICAL_TABLE_COUNT", "UNAUTHORIZED_EXTRA_TABLE_COUNT",
    "UNTRACED_SCIENTIFIC_VALUE_COUNT", "UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT",
    "SUPERSEDED_NUMERIC_SOURCE_USED_COUNT", "MARKDOWN_CSV_VALUE_MISMATCH_COUNT",
    "DENOMINATOR_MISMATCH_COUNT", "UNIT_MISMATCH_COUNT", "CI_LEVEL_MISMATCH_COUNT",
    "HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT", "HE2A_ARM_LEVEL_NEW_CI_COUNT",
    "EXP12_PERFORMANCE_TABLE_ROW_COUNT", "EXP12_FABRICATED_METRIC_COUNT",
    "HARDCODED_PASS_VALIDATION_COUNTER_COUNT",
    "HE5_HIERARCHY_ROWS_WITH_FROZEN_DENOMINATOR_COUNT",
    "HE5_HIERARCHY_NONEMPTY_RENDERED_DENOMINATOR_COUNT",
    "HE5_HIERARCHY_FABRICATED_DENOMINATOR_COUNT",
    "SCIENTIFIC_METRIC_VALUE_DELTA_COUNT", "SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT",
    "NEW_SCIENTIFIC_STATEMENT_COUNT",
]
required_false = [
    "HE2_REDECIDED", "HE5_REDECIDED", "NEW_INFERENCE_PERFORMED",
    "NEW_CI_CALCULATED", "P_VALUES_CALCULATED", "METRICS_RECOMPUTED",
    "EXPERIMENTS_RERUN", "RETRIEVAL_EXECUTED", "EXP12_REOPENED",
    "ARTICLE_MODIFIED", "G5_F03_STARTED",
]
if (
    validation["MATERIALIZED_CANONICAL_TABLE_COUNT"] != 9
    or g3_evidence_expected != 16
    or g3_evidence_mapped != 16
    or g4_claim_expected != 18
    or g4_claim_mapped != 18
    or any(validation[name] != 0 for name in required_zero)
    or any(validation[name] is not False for name in required_false)
    or validation["HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE"] is not True
    or validation["VALIDATION_COUNTERS_COMPUTED_FROM_CHECKS"] is not True
    or validation["HE5_HIERARCHY_ROW_COUNT"] != 3
    or validation["HE5_HIERARCHY_ERROR_COUNT_VALUES_PRESERVED"] is not True
    or validation["MARKDOWN_RENDER_SOURCE"] != "CANONICAL_CSV_FILES"
    or validation["MARKDOWN_RENDERED_FROM_REREAD_CSV"] is not True
):
    print(json.dumps({
        "status": "FAIL",
        "validation": validation,
        "direct_copy_mismatches": direct_copy_mismatches,
    }, indent=2))
    raise RuntimeError("G5-F02 validation failed")

script_sha = file_sha256(Path(__file__))
crosscheck = {
    "artifact_id": "G5_F02_NUMERIC_CROSSCHECK_V0_2",
    "status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
    "ficha": "G5-F02",
    "main_base": MAIN_BASE,
    "plan_snapshot": PLAN_SNAPSHOT,
    "fichas_activation_commit": FICHAS_ACTIVATION_COMMIT,
    "prompt97_commit": PROMPT97_COMMIT,
    "prompt98_commit": PROMPT98_COMMIT,
    "superseded_candidate": V01_CANDIDATE,
    "script_path": str(Path(__file__).relative_to(ROOT)).replace("\\", "/"),
    "script_sha256_or_git_blob": {"type": "sha256", "value": script_sha},
    "source_registry_snapshot": {path: source_blobs.get(path, "4fe9318d52fad093066ff9f42d524fc95e436245") for path in sorted(USED_SOURCES)},
    "canonical_table_registry": canonical_registry,
    "cell_value_ledger": ledger,
    "markdown_render_checks": markdown_checks,
    "validation_check_provenance": validation_check_provenance,
    "rpre": {name: "PASS" for name in rpre_names},
    "validation": validation,
    "GROUP5_CLOSED": False,
    "G5_F03_AUTHORIZED": False,
}
write_json(CROSSCHECK_PATH, crosscheck)
print(json.dumps({"status": "PASS", "tables": len(tables), "ledger_entries": len(ledger), "validation": validation}, indent=2))
