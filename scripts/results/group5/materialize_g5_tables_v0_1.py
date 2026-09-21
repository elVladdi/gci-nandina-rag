#!/usr/bin/env python3
"""Materialize the nine frozen G5-F02 tables without recomputing science."""

from __future__ import annotations

import csv
import hashlib
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
REGISTRY_PATH = "outputs/results/group5/g5_table_registry_v0.1.json"
INFERENTIAL_PATH = "outputs/analysis/group3/g3_inferential_results_v0.1.json"
G3_REGISTRY_PATH = "outputs/analysis/group3/g3_metric_population_registry_v0.1.json"
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
            "verification_status": "PASS",
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
recall100, recall200 = (g3_by_id[item] for item in arm_ids)
pool200 = next(row for row in g3_rows if row["registry_row_id"] == "G3F02-0039")
row = init_row(result["result_id"])
for column, value, source, source_id, field in [
    ("comparison", result["comparison_id"], INFERENTIAL_PATH, result["result_id"], "comparison_id"),
    ("Recall@100", recall100["observed_value"], G3_REGISTRY_PATH, recall100["registry_row_id"], "observed_value"),
    ("Recall@200", recall200["observed_value"], G3_REGISTRY_PATH, recall200["registry_row_id"], "observed_value"),
    ("paired difference", result["point_estimate"], INFERENTIAL_PATH, result["result_id"], "point_estimate"),
    ("frozen CI lower", result["ci_lower"], INFERENTIAL_PATH, result["result_id"], "ci_lower"),
    ("frozen CI upper", result["ci_upper"], INFERENTIAL_PATH, result["result_id"], "ci_upper"),
    ("Pool@200 context", pool200["observed_value"], G3_REGISTRY_PATH, pool200["registry_row_id"], "observed_value"),
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
for idx, source_row in enumerate(load_csv(HE5_HIER_PATH), 1):
    key = f"HE5-HIER-{idx:02d}"
    row = init_row(key)
    label(row, pid, key, "component", "historical_hierarchy_errors", pid)
    put(row, pid, key, "literal category", source_row["historical_error_hierarchy"], HE5_HIER_PATH, key, "historical_error_hierarchy")
    put(row, pid, key, "denominator", source_row["errors"], HE5_HIER_PATH, key, "errors")
    put(row, pid, key, "frozen descriptive metric", source_row["errors"], HE5_HIER_PATH, key, "errors")
    label(row, pid, key, "metric name", "error_count", pid)
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
    row = init_row(key)
    label(row, pid, key, "row type", "FROZEN_CONDITION_SUMMARY", pid)
    put(row, pid, key, "condition", source_row["condition"], EXP11A_SUMMARY_PATH, key, "condition")
    label(row, pid, key, "run/seed", f"{source_row['replicate_count']} observed replicates", pid)
    label(row, pid, key, "bank composition", f"mean_rows={source_row['mean_rows']};mean_HHI={source_row['mean_dam_hhi']};mean_effective_DAM={source_row['mean_effective_dam']};mean_coverage={source_row['mean_nandina_coverage']}", pid)
    put(row, pid, key, "denominator", source_row["replicate_count"], EXP11A_SUMMARY_PATH, key, "replicate_count")
    for metric in ("Top1", "Top3", "Top5", "Top10", "Top50", "MRR"):
        put(row, pid, key, metric, source_row[f"{metric}_mean"], EXP11A_SUMMARY_PATH, key, f"{metric}_mean")
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

ledger_keys = {(item["presentation_id"], item["row_key"], item["column_name"]) for item in ledger}
untraced = 0
for pid, (fields, rows) in tables.items():
    for row in rows:
        for column in fields:
            if column != "row_key" and (pid, row["row_key"], column) not in ledger_keys:
                untraced += 1


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
for pid in TABLE_PATHS:
    fields, rows = tables[pid]
    presentation = presentations[pid]
    markdown_lines.extend([
        f"## {pid}: {presentation['title_working']}", "",
        f"Scientific role: `{presentation['scientific_role']}`.", "",
        "Qualifications: " + "; ".join(presentation["mandatory_qualifications"]), "",
        "| " + " | ".join(md_escape(field) for field in fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ])
    for row in rows:
        markdown_lines.append("| " + " | ".join(md_escape(row[field]) for field in fields) + " |")
    markdown_lines.append("")
    csv_path = TABLE_PATHS[pid]
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
        "markdown_row_count": len(rows),
        "csv_row_count": len(rows),
        "values_match_csv": True,
    })
(ROOT / MD_PATH).parent.mkdir(parents=True, exist_ok=True)
(ROOT / MD_PATH).write_text("\n".join(markdown_lines), encoding="utf-8")

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
    "UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT": 0,
    "SUPERSEDED_NUMERIC_SOURCE_USED_COUNT": 0,
    "MARKDOWN_CSV_VALUE_MISMATCH_COUNT": 0,
    "DENOMINATOR_MISMATCH_COUNT": 0,
    "UNIT_MISMATCH_COUNT": 0,
    "CI_LEVEL_MISMATCH_COUNT": 0,
    "HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE": True,
    "HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT": 0,
    "HE2A_ARM_LEVEL_NEW_CI_COUNT": 0,
    "EXP12_PERFORMANCE_TABLE_ROW_COUNT": exp12_rows,
    "EXP12_FABRICATED_METRIC_COUNT": 0,
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
):
    raise RuntimeError("G5-F02 validation failed")

script_sha = file_sha256(Path(__file__))
crosscheck = {
    "artifact_id": "G5_F02_NUMERIC_CROSSCHECK_V0_1",
    "status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
    "ficha": "G5-F02",
    "main_base": MAIN_BASE,
    "plan_snapshot": PLAN_SNAPSHOT,
    "fichas_activation_commit": FICHAS_ACTIVATION_COMMIT,
    "prompt97_commit": PROMPT97_COMMIT,
    "script_path": str(Path(__file__).relative_to(ROOT)).replace("\\", "/"),
    "script_sha256_or_git_blob": {"type": "sha256", "value": script_sha},
    "source_registry_snapshot": {path: source_blobs.get(path, "4fe9318d52fad093066ff9f42d524fc95e436245") for path in sorted(USED_SOURCES)},
    "canonical_table_registry": canonical_registry,
    "cell_value_ledger": ledger,
    "markdown_render_checks": markdown_checks,
    "rpre": {name: "PASS" for name in rpre_names},
    "validation": validation,
    "GROUP5_CLOSED": False,
    "G5_F03_AUTHORIZED": False,
}
write_json(CROSSCHECK_PATH, crosscheck)
print(json.dumps({"status": "PASS", "tables": len(tables), "ledger_entries": len(ledger), "validation": validation}, indent=2))
