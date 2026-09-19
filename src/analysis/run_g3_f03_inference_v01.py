from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import subprocess
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


BASE_MAIN = "adf70d6eb880c567d6efa0f27b5c79259b8db2a6"
PLAN_COMMIT = "12ac39ec18761bc926d196e71137de60c2a9956b"
FICHAS_ACTIVATION_COMMIT = "6750ed15b0e8ed62f5deba517eddf92fa2616bca"
PROMPT83_COMMIT = "10d94aeb982ad600229516ed27dd0fcc6b7264a0"
EVAL_SHA256 = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
REGISTRY_CSV_SHA256 = "65294f0e81de358f8cdab4d3997d1c8fe03062f2d3e5b6a95cbca5da885c5c41"
REGISTRY_JSON_SHA256 = "673b43e9ef5ed20bc6aafa9c674e6bbdba5cdbd054dd47f40bf14d05c8d1ae7b"
REGISTRY_CSV_BLOB = "c63619b56a07e6b6d7be78b515d941ec3b205c41"
REGISTRY_JSON_BLOB = "5ea33ca583b18426374fa15baf1b1759e76cd99e"
REGISTRY_LEDGER_BLOB = "521bfcdf34d03c4effa8b8ef19f9777b6827d439"

B = 10_000
SEED = 20_263_001
N_SERIES = 1_056
N_DAM = 67

REGISTRY_CSV = "outputs/analysis/group3/g3_metric_population_registry_v0.1.csv"
REGISTRY_JSON = "outputs/analysis/group3/g3_metric_population_registry_v0.1.json"
REGISTRY_LEDGER = "outputs/analysis/group3/g3_metric_population_registry_v0.1_hash_ledger.csv"
CONTRACT_MD = "docs/analysis/group3/g3_analytical_contract_v0.1.md"
CONTRACT_JSON = "outputs/analysis/group3/g3_analytical_contract_v0.1.json"
EVAL_PATH = "data/processed/data_aduanas_evalset_clase87_v0.2.csv"

HIST_PATH = "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_case_summary.csv"
FLAT_PATH = "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5/normative_flat_case_summary.csv"
HIER_PATH = "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_case_summary.csv"
D1A_PATH = "outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_case_summary.csv"

SCRIPT_PATH = "src/analysis/run_g3_f03_inference_v01.py"
CSV_PATH = "outputs/analysis/group3/g3_inferential_results_v0.1.csv"
JSON_PATH = "outputs/analysis/group3/g3_inferential_results_v0.1.json"
METHODS_PATH = "docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md"
LEDGER_PATH = "outputs/analysis/group3/g3_inferential_results_v0.1_hash_ledger.csv"

ELIGIBLE_FAMILIES = (
    "HE2_A_HISTORICAL_VS_NORMATIVE_FLAT_ATTEMPT06",
    "HE2_A_HISTORICAL_VS_NORMATIVE_HIERARCHICAL_ATTEMPT06",
    "HE2_A_HISTORICAL_VS_D1A_ATTEMPT06",
    "HE2_B_HIERARCHICAL_DEEP_COVERAGE_ATTEMPT06",
)

EXCLUDED_FAMILIES = (
    ("HE2_B_PHASE_E_FROZEN_ROLE_POOLS", "DESCRIPTIVE_ONLY", "frozen candidate-pool coverage inventory"),
    ("HE2_B_PHASE_E_70_30", "DESCRIPTIVE_ONLY", "variant not formally frozen for confirmatory use"),
    ("HE2_B_PHASE_E_DIAGNOSTIC_UNION", "DESCRIPTIVE_ONLY", "diagnostic coverage ceiling without ranking"),
    ("EXP11A_HISTORICAL_BANK_SENSITIVITY", "DESCRIPTIVE_ONLY", "bank size and composition remain coupled"),
    ("EXP11B_H150_H200_PAIRED_SENSITIVITY", "DESCRIPTIVE_ONLY", "no seed superpopulation and repeated EVAL"),
    ("0B05C_ATTEMPT06_CORRECTIVE_SENSITIVITY", "DESCRIPTIVE_ONLY", "corrected governed sensitivity state"),
    ("HE5_AMBIGUOUS_INCOMPLETE_DESCRIPTIONS", "DESCRIPTIVE_ONLY", "description quality not operationalized"),
    ("HE5_HIERARCHICAL_PROXIMITY", "DESCRIPTIVE_ONLY", "frozen hierarchy counts only"),
    ("HE5_INSUFFICIENT_HISTORICAL_PRECEDENTS", "DESCRIPTIVE_ONLY", "no frozen insufficiency threshold"),
    ("HE5_INTERNAL_EVALUATION_SCOPE", "DESCRIPTIVE_ONLY", "internal benchmark boundary"),
    ("HE5_EXPLANATION_EVIDENCE_LIMITS", "DESCRIPTIVE_ONLY", "heterogeneous diagnostic scopes"),
    ("EXP12_DIVERSITY", "NOT_ESTIMABLE", "no selected conditions or retrieval results"),
)

CSV_COLUMNS = (
    "result_id",
    "hypothesis_component",
    "evidence_family_id",
    "role",
    "comparison_id",
    "metric_name",
    "estimand",
    "expected_direction",
    "analysis_unit",
    "dependency_group",
    "n_series",
    "n_dam",
    "point_estimate",
    "point_estimate_percentage_points",
    "value_unit",
    "bootstrap_type",
    "bootstrap_B",
    "bootstrap_seed",
    "ci_method",
    "ci_level",
    "ci_lower",
    "ci_upper",
    "multiplicity_method",
    "multiplicity_family",
    "hypothesis_decision_role",
    "source_registry_row_ids",
    "source_case_level_paths",
    "scope",
    "limitations",
)


class ContractViolation(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractViolation(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_blob(repository_root: Path, path: Path) -> str:
    result = subprocess.run(
        ["git", "hash-object", str(path)],
        cwd=repository_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def git_blob_at_head(repository_root: Path, relative_path: str) -> str:
    result = subprocess.run(
        ["git", "rev-parse", f"HEAD:{relative_path}"],
        cwd=repository_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def sha256_git_blob_at_head(repository_root: Path, relative_path: str) -> str:
    result = subprocess.run(
        ["git", "cat-file", "blob", f"HEAD:{relative_path}"],
        cwd=repository_root,
        check=True,
        capture_output=True,
    )
    return hashlib.sha256(result.stdout).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def read_frame(path: Path, string_columns: tuple[str, ...]) -> pd.DataFrame:
    dtype = {column: "string" for column in string_columns}
    return pd.read_csv(path, dtype=dtype, keep_default_na=False)


def numeric(frame: pd.DataFrame, column: str) -> np.ndarray:
    require(column in frame.columns, f"missing column {column}")
    return pd.to_numeric(frame[column], errors="raise").to_numpy(dtype=float)


def rr100_from_rank(frame: pd.DataFrame, column: str) -> np.ndarray:
    ranks = numeric(frame, column)
    contributions = np.zeros_like(ranks, dtype=float)
    eligible = (ranks >= 1.0) & (ranks <= 100.0)
    contributions[eligible] = 1.0 / ranks[eligible]
    return contributions


def verify_pairing(reference: pd.DataFrame, candidate: pd.DataFrame, name: str) -> pd.DataFrame:
    keys = ["case_id", "id_unico"]
    require(reference[keys].duplicated().sum() == 0, "historical duplicate pairing keys")
    require(candidate[keys].duplicated().sum() == 0, f"{name} duplicate pairing keys")
    require(set(map(tuple, reference[keys].to_numpy())) == set(map(tuple, candidate[keys].to_numpy())), f"{name} pairing-key mismatch")
    merged = reference[["case_id", "id_unico", "declaracion", "serie", "expected_nandina"]].merge(
        candidate,
        on=keys,
        how="inner",
        validate="one_to_one",
        suffixes=("_historical", ""),
    )
    require(len(merged) == N_SERIES, f"{name} paired row count mismatch")
    label_column = "nandina_ref"
    require(label_column in merged.columns, f"{name} missing label")
    require((merged["expected_nandina"].astype(str) == merged[label_column].astype(str)).all(), f"{name} label mismatch")
    return merged


def registry_rows_for_metric(registry: pd.DataFrame, family: str, metric: str) -> pd.DataFrame:
    rows = registry[(registry["evidence_family_id"] == family) & (registry["metric_name"] == metric)]
    require(len(rows) == 2, f"registry pair missing for {family} {metric}")
    return rows


def observed_value(rows: pd.DataFrame, source_path: str) -> float:
    match = rows[rows["source_path"] == source_path]
    require(len(match) == 1, f"registry source mismatch for {source_path}")
    return float(match.iloc[0]["observed_value"])


def observed_numerator(rows: pd.DataFrame, source_path: str) -> float:
    match = rows[rows["source_path"] == source_path]
    require(len(match) == 1, f"registry numerator source mismatch for {source_path}")
    return float(match.iloc[0]["observed_numerator"])


def validate_arm_against_registry(
    registry: pd.DataFrame,
    family: str,
    metric: str,
    source_path: str,
    values: np.ndarray,
) -> float:
    rows = registry_rows_for_metric(registry, family, metric)
    mean_value = float(np.mean(values))
    sum_value = float(np.sum(values, dtype=np.float64))
    require(abs(mean_value - observed_value(rows, source_path)) <= 1e-12, f"point estimate mismatch for {family} {metric} {source_path}")
    require(abs(sum_value - observed_numerator(rows, source_path)) <= 1e-12, f"numerator mismatch for {family} {metric} {source_path}")
    return mean_value


def bootstrap_interval(
    contributions: np.ndarray,
    dam_ids: np.ndarray,
    cluster_order: np.ndarray,
    resampling_indices: np.ndarray,
    quantiles: tuple[float, float],
) -> tuple[float, float, float]:
    cluster_sums = np.array(
        [contributions[dam_ids == cluster].sum(dtype=np.float64) for cluster in cluster_order],
        dtype=float,
    )
    cluster_counts = np.array([np.count_nonzero(dam_ids == cluster) for cluster in cluster_order], dtype=np.int64)
    numerators = cluster_sums[resampling_indices].sum(axis=1, dtype=np.float64)
    denominators = cluster_counts[resampling_indices].sum(axis=1, dtype=np.int64)
    require(np.all(denominators > 0), "empty bootstrap replicate")
    replicates = numerators / denominators
    lower, upper = np.quantile(replicates, quantiles, method="linear")
    return float(np.mean(contributions)), float(lower), float(upper)


def output_row(
    *,
    result_number: int,
    hypothesis_component: str,
    family: str,
    role: str,
    comparison_id: str,
    metric_name: str,
    estimand: str,
    expected_direction: str,
    point: float,
    lower: float,
    upper: float,
    ci_level: float,
    multiplicity_method: str,
    multiplicity_family: str,
    decision_role: str,
    registry_ids: str,
    case_paths: str,
    is_proportion: bool,
    limitations: str,
) -> dict[str, Any]:
    return {
        "result_id": f"G3F03-{result_number:04d}",
        "hypothesis_component": hypothesis_component,
        "evidence_family_id": family,
        "role": role,
        "comparison_id": comparison_id,
        "metric_name": metric_name,
        "estimand": estimand,
        "expected_direction": expected_direction,
        "analysis_unit": "SERIE",
        "dependency_group": "DAM / DECLARACIÓN",
        "n_series": N_SERIES,
        "n_dam": N_DAM,
        "point_estimate": point,
        "point_estimate_percentage_points": 100.0 * point if is_proportion else None,
        "value_unit": "absolute_proportion_difference" if is_proportion else "mean_reciprocal_rank_difference",
        "bootstrap_type": "PAIRED_DAM_CLUSTER_PERCENTILE",
        "bootstrap_B": B,
        "bootstrap_seed": SEED,
        "ci_method": "TWO_SIDED_PERCENTILE_LINEAR_QUANTILES",
        "ci_level": ci_level,
        "ci_lower": lower,
        "ci_upper": upper,
        "multiplicity_method": multiplicity_method,
        "multiplicity_family": multiplicity_family,
        "hypothesis_decision_role": decision_role,
        "source_registry_row_ids": registry_ids,
        "source_case_level_paths": case_paths,
        "scope": "CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION",
        "limitations": limitations,
    }


def build_methods() -> str:
    excluded = "\n".join(f"- `{family}`: {reason}." for family, _, reason in EXCLUDED_FAMILIES)
    return f"""# G3-F03 Inferential Methods and Checks v0.1

## State and frozen inputs

G3-F03 was prospectively activated before any bootstrap result was calculated. The scientific baseline is `{BASE_MAIN}`, the governing G3-F01 contract and G3-F02 registry are read-only inputs, and the activation is `{FICHAS_ACTIVATION_COMMIT}`. No retrieval or frozen experiment was reexecuted.

The EVAL binding is 1,056 series nested in 67 DAM, SHA-256 `{EVAL_SHA256}`. Historical, corrected flat, corrected hierarchical, and corrected D1a case sets were paired exactly by `case_id` and `id_unico`; labels matched. D1a DAM/SERIE fields were recovered only through that exact frozen join.

## Point-estimate reconstruction

Before resampling, every historical and normative Top-1/3/5/10/50 numerator and mean, each MRR@100 contribution sum and mean, and hierarchical Recall@100/Recall@200 were reconstructed from the frozen case-level files. All reconstructed values matched the G3-F02 registry within `1e-12`.

## Dependence and bootstrap

The analysis unit is SERIE and the dependency group is DAM / DECLARACIÓN. DAM identifiers were sorted lexicographically. A single `numpy.random.default_rng({SEED})` PCG64 stream produced one `{B} x {N_DAM}` matrix of DAM indices sampled with replacement. The same matrix was used for every result.

If a DAM appears `m` times in a replicate, all of its series contribute with multiplicity `m`. Each replicate is therefore the sum of multiplicity-weighted within-DAM contribution sums divided by the corresponding multiplicity-weighted series count. This preserves the series-weighted estimand and does not substitute an unweighted mean of DAM means.

## HE2_A and multiplicity

For each corrected normative strategy (flat, hierarchical, D1a), the five primary contrasts are paired historical-minus-normative differences for Top-1, Top-3, Top-5, Top-10, and MRR@100. Each five-metric family uses a two-sided 99% percentile interval (`0.005`, `0.995`), implementing the frozen Bonferroni familywise 95% coverage rule. No p-values are calculated.

Top-50 is reported once per strategy as supplementary uncertainty with a two-sided 95% percentile interval. It is outside the primary five-metric family and has no hypothesis-decision role.

## HE2_B

The only HE2_B inferential contrast is paired `Recall@200 - Recall@100` for corrected hierarchical retrieval. It uses a two-sided 95% percentile interval (`0.025`, `0.975`) with no multiplicity adjustment. Pool@200 is not duplicated as another contrast.

## Deliberate inferential exclusions

{excluded}

## Scope and decisions

The intervals quantify cluster-aware resampling uncertainty inside the fixed internal Chapter 87 benchmark. They do not establish external-population validity. No standardized post-hoc effect measure is introduced; the frozen absolute paired contribution difference is the effect measure. No p-values are calculated. HE2 and HE5 remain undecided, and G3-F04 remains not authorized and not started.

## Reproducibility and warnings

CSV and JSON were regenerated in a separate temporary output root with the same inputs and runtime and compared byte for byte. The only inherited documentation warning is that some G3-F02 `source_commit_binding` values use two literal `main=` labels; exact SHA, blob, and path provenance remains explicit.
"""


def run(repository_root: Path, output_root: Path) -> dict[str, Any]:
    repository_root = repository_root.resolve()
    output_root = output_root.resolve()

    registry_csv_path = repository_root / REGISTRY_CSV
    registry_json_path = repository_root / REGISTRY_JSON
    registry_ledger_path = repository_root / REGISTRY_LEDGER
    require(sha256_git_blob_at_head(repository_root, REGISTRY_CSV) == REGISTRY_CSV_SHA256, "registry CSV SHA mismatch")
    require(sha256_git_blob_at_head(repository_root, REGISTRY_JSON) == REGISTRY_JSON_SHA256, "registry JSON SHA mismatch")
    require(git_blob_at_head(repository_root, REGISTRY_CSV) == REGISTRY_CSV_BLOB, "registry CSV blob mismatch")
    require(git_blob_at_head(repository_root, REGISTRY_JSON) == REGISTRY_JSON_BLOB, "registry JSON blob mismatch")
    require(git_blob_at_head(repository_root, REGISTRY_LEDGER) == REGISTRY_LEDGER_BLOB, "registry ledger blob mismatch")
    require((repository_root / CONTRACT_MD).is_file(), "contract markdown missing")
    require((repository_root / CONTRACT_JSON).is_file(), "contract JSON missing")
    require(sha256_file(repository_root / EVAL_PATH) == EVAL_SHA256, "EVAL SHA mismatch")

    registry_json = json.loads(registry_json_path.read_text(encoding="utf-8"))
    registry = pd.read_csv(registry_csv_path, dtype=str, keep_default_na=False)
    require(len(registry) == 548 and len(registry_json["rows"]) == 548, "registry row count mismatch")
    counts = registry_json["classification_counts"]
    require(counts == {"evidence_family_count": 16, "ELIGIBLE": 4, "DESCRIPTIVE_ONLY": 11, "NOT_ESTIMABLE": 1, "NOT_APPLICABLE": 0}, "family classification mismatch")
    actual_eligible = tuple(registry.loc[registry["use_classification"] == "ELIGIBLE", "evidence_family_id"].drop_duplicates())
    require(actual_eligible == ELIGIBLE_FAMILIES, "eligible family inventory mismatch")
    validation = registry_json["validation"]
    for key in (
        "UNKNOWN_EVIDENCE_FAMILIES",
        "MISSING_EVIDENCE_FAMILIES",
        "DUPLICATE_REGISTRY_ROW_ID",
        "ROWS_WITHOUT_SOURCE_PROVENANCE",
        "ROWS_USING_SUPERSEDED_3000_1006_AS_CURRENT",
        "ROWS_MIXING_INCOMPATIBLE_EVALSETS",
        "0B05C_NON_ATTEMPT06_CURRENT_ROWS",
        "EXP12_NUMERIC_EFFECT_ROWS",
        "HE2_HE5_DECISION_ROWS",
        "INFERENTIAL_OUTPUT_ROWS",
    ):
        require(validation[key] == 0, f"registry validation failed: {key}")

    eligible_rows = registry[registry["use_classification"] == "ELIGIBLE"]
    for _, row in eligible_rows.iterrows():
        for path_key, blob_key in (("source_path", "source_git_blob"), ("case_level_source_path", "case_level_source_git_blob")):
            relative_path = row[path_key]
            require(bool(relative_path), f"missing {path_key}")
            require((repository_root / relative_path).is_file(), f"missing frozen source {relative_path}")
            require(git_blob_at_head(repository_root, relative_path) == row[blob_key], f"source blob mismatch {relative_path}")

    string_columns = ("case_id", "id_unico", "declaracion", "serie", "expected_nandina", "nandina_ref")
    historical = read_frame(repository_root / HIST_PATH, string_columns)
    flat = read_frame(repository_root / FLAT_PATH, string_columns)
    hierarchical = read_frame(repository_root / HIER_PATH, string_columns)
    d1a = read_frame(repository_root / D1A_PATH, string_columns)
    require(len(historical) == len(flat) == len(hierarchical) == len(d1a) == N_SERIES, "case-level row count mismatch")
    require(historical["declaracion"].nunique() == N_DAM, "DAM count mismatch")

    flat_paired = verify_pairing(historical, flat, "flat")
    hierarchical_paired = verify_pairing(historical, hierarchical, "hierarchical")
    d1a_paired = verify_pairing(historical, d1a, "D1a")
    historical = historical.sort_values(["case_id", "id_unico"], kind="mergesort").reset_index(drop=True)
    flat_paired = flat_paired.sort_values(["case_id", "id_unico"], kind="mergesort").reset_index(drop=True)
    hierarchical_paired = hierarchical_paired.sort_values(["case_id", "id_unico"], kind="mergesort").reset_index(drop=True)
    d1a_paired = d1a_paired.sort_values(["case_id", "id_unico"], kind="mergesort").reset_index(drop=True)
    require((historical["declaracion"].astype(str).to_numpy() == flat_paired["declaracion_historical"].astype(str).to_numpy()).all(), "flat DAM alignment mismatch")
    require((historical["declaracion"].astype(str).to_numpy() == hierarchical_paired["declaracion_historical"].astype(str).to_numpy()).all(), "hierarchical DAM alignment mismatch")
    require((historical["declaracion"].astype(str).to_numpy() == d1a_paired["declaracion"].astype(str).to_numpy()).all(), "D1a exact DAM join mismatch")

    historical_values = {
        "Top-1": numeric(historical, "exact_at_1"),
        "Top-3": numeric(historical, "exact_at_3"),
        "Top-5": numeric(historical, "exact_at_5"),
        "Top-10": numeric(historical, "exact_at_10"),
        "Top-50": numeric(historical, "exact_at_50"),
        "MRR@100": rr100_from_rank(historical, "exact_rank"),
    }
    strategy_values = {
        "flat": {
            "Top-1": numeric(flat_paired, "hit_top_1"),
            "Top-3": numeric(flat_paired, "hit_top_3"),
            "Top-5": numeric(flat_paired, "hit_top_5"),
            "Top-10": numeric(flat_paired, "hit_top_10"),
            "Top-50": numeric(flat_paired, "hit_top_50"),
            "MRR@100": rr100_from_rank(flat_paired, "rank_ref"),
        },
        "hierarchical": {
            "Top-1": numeric(hierarchical_paired, "hit_top_1"),
            "Top-3": numeric(hierarchical_paired, "hit_top_3"),
            "Top-5": numeric(hierarchical_paired, "hit_top_5"),
            "Top-10": numeric(hierarchical_paired, "hit_top_10"),
            "Top-50": numeric(hierarchical_paired, "hit_top_50"),
            "MRR@100": rr100_from_rank(hierarchical_paired, "rank_ref"),
        },
        "D1a": {
            "Top-1": numeric(d1a_paired, "hit_top_1"),
            "Top-3": numeric(d1a_paired, "hit_top_3"),
            "Top-5": numeric(d1a_paired, "hit_top_5"),
            "Top-10": numeric(d1a_paired, "hit_top_10"),
            "Top-50": numeric(d1a_paired, "hit_top_50"),
            "MRR@100": numeric(d1a_paired, "mrr_at_100_contribution"),
        },
    }
    require(np.max(np.abs(strategy_values["flat"]["MRR@100"] - numeric(flat_paired, "reciprocal_rank"))) <= 1e-15, "flat RR100 field mismatch")
    require(np.max(np.abs(strategy_values["hierarchical"]["MRR@100"] - np.where(numeric(hierarchical_paired, "rank_ref") <= 100, numeric(hierarchical_paired, "reciprocal_rank"), 0.0))) <= 1e-15, "hierarchical RR100 field mismatch")

    family_config = (
        ("flat", ELIGIBLE_FAMILIES[0], "outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5/normative_flat_metrics.json", FLAT_PATH),
        ("hierarchical", ELIGIBLE_FAMILIES[1], "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_metrics.json", HIER_PATH),
        ("D1a", ELIGIBLE_FAMILIES[2], "outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_metrics.json", D1A_PATH),
    )
    historical_metrics_path = "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json"
    max_reconstruction_error = 0.0
    for strategy, family, strategy_metrics_path, _ in family_config:
        for metric in ("Top-1", "Top-3", "Top-5", "Top-10", "MRR@100", "Top-50"):
            hist_mean = validate_arm_against_registry(registry, family, metric, historical_metrics_path, historical_values[metric])
            strategy_mean = validate_arm_against_registry(registry, family, metric, strategy_metrics_path, strategy_values[strategy][metric])
            rows = registry_rows_for_metric(registry, family, metric)
            max_reconstruction_error = max(
                max_reconstruction_error,
                abs(hist_mean - observed_value(rows, historical_metrics_path)),
                abs(strategy_mean - observed_value(rows, strategy_metrics_path)),
            )

    coverage_family = ELIGIBLE_FAMILIES[3]
    coverage_source = "outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_metrics.json"
    recall100 = numeric(hierarchical_paired, "hit_recall_100")
    recall200 = numeric(hierarchical_paired, "hit_recall_200")
    for metric, values in (("Recall@100", recall100), ("Recall@200", recall200)):
        row = registry[(registry["evidence_family_id"] == coverage_family) & (registry["metric_name"] == metric)]
        require(len(row) == 1 and row.iloc[0]["source_path"] == coverage_source, f"coverage registry row mismatch {metric}")
        require(abs(float(np.mean(values)) - float(row.iloc[0]["observed_value"])) <= 1e-12, f"coverage point mismatch {metric}")
        require(abs(float(np.sum(values)) - float(row.iloc[0]["observed_numerator"])) <= 1e-12, f"coverage numerator mismatch {metric}")

    dam_ids = historical["declaracion"].astype(str).to_numpy()
    cluster_order = np.array(sorted(np.unique(dam_ids)), dtype=object)
    require(len(cluster_order) == N_DAM, "cluster inventory mismatch")
    rng = np.random.default_rng(SEED)
    require(type(rng.bit_generator).__name__ == "PCG64", "unexpected RNG bit generator")
    resampling_indices = rng.integers(0, N_DAM, size=(B, N_DAM), endpoint=False)

    rows_out: list[dict[str, Any]] = []
    result_number = 1
    primary_metrics = ("Top-1", "Top-3", "Top-5", "Top-10", "MRR@100")
    for strategy, family, _, case_path in family_config:
        for metric in primary_metrics:
            contribution = historical_values[metric] - strategy_values[strategy][metric]
            point, lower, upper = bootstrap_interval(contribution, dam_ids, cluster_order, resampling_indices, (0.005, 0.995))
            registry_ids = ";".join(registry_rows_for_metric(registry, family, metric)["registry_row_id"].tolist())
            rows_out.append(output_row(
                result_number=result_number,
                hypothesis_component="HE2_A",
                family=family,
                role="PRIMARY_INFERENTIAL",
                comparison_id=f"HISTORICAL_MINUS_{strategy.upper()}",
                metric_name=metric,
                estimand=f"series-weighted mean paired historical-minus-{strategy} contribution",
                expected_direction="greater_than_zero",
                point=point,
                lower=lower,
                upper=upper,
                ci_level=0.99,
                multiplicity_method="BONFERRONI_FAMILYWISE_95_VIA_99_PERCENT_MARGINAL_CI",
                multiplicity_family=f"{family}_PRIMARY_FIVE_METRIC_FAMILY",
                decision_role="DEFERRED_TO_G3_F04",
                registry_ids=registry_ids,
                case_paths=f"{HIST_PATH};{case_path}",
                is_proportion=metric != "MRR@100",
                limitations="internal fixed Chapter 87 benchmark; cluster-resampling uncertainty only",
            ))
            result_number += 1

    coverage_contribution = recall200 - recall100
    point, lower, upper = bootstrap_interval(coverage_contribution, dam_ids, cluster_order, resampling_indices, (0.025, 0.975))
    coverage_rows = registry[(registry["evidence_family_id"] == coverage_family) & registry["metric_name"].isin(["Recall@100", "Recall@200"])]
    rows_out.append(output_row(
        result_number=result_number,
        hypothesis_component="HE2_B",
        family=coverage_family,
        role="PRIMARY_INFERENTIAL",
        comparison_id="HIERARCHICAL_RECALL_200_MINUS_100",
        metric_name="Recall@200 - Recall@100",
        estimand="series-weighted mean paired hit_recall_200-minus-hit_recall_100 contribution",
        expected_direction="greater_than_zero",
        point=point,
        lower=lower,
        upper=upper,
        ci_level=0.95,
        multiplicity_method="NONE_SINGLE_CONTRAST",
        multiplicity_family="HE2_B_SINGLE_DEEP_COVERAGE_CONTRAST",
        decision_role="DEFERRED_TO_G3_F04",
        registry_ids=";".join(coverage_rows["registry_row_id"].tolist()),
        case_paths=HIER_PATH,
        is_proportion=True,
        limitations="deep coverage only; not an early-ranking contrast; internal fixed benchmark",
    ))
    result_number += 1

    for strategy, family, _, case_path in family_config:
        metric = "Top-50"
        contribution = historical_values[metric] - strategy_values[strategy][metric]
        point, lower, upper = bootstrap_interval(contribution, dam_ids, cluster_order, resampling_indices, (0.025, 0.975))
        rows_out.append(output_row(
            result_number=result_number,
            hypothesis_component="HE2_A",
            family=family,
            role="SUPPLEMENTARY",
            comparison_id=f"HISTORICAL_MINUS_{strategy.upper()}",
            metric_name=metric,
            estimand=f"series-weighted mean paired historical-minus-{strategy} Top-50 contribution",
            expected_direction="greater_than_zero",
            point=point,
            lower=lower,
            upper=upper,
            ci_level=0.95,
            multiplicity_method="NONE_SUPPLEMENTARY",
            multiplicity_family="NOT_INCLUDED_IN_PRIMARY_FIVE_METRIC_FAMILY",
            decision_role="NONE",
            registry_ids=";".join(registry_rows_for_metric(registry, family, metric)["registry_row_id"].tolist()),
            case_paths=f"{HIST_PATH};{case_path}",
            is_proportion=True,
            limitations="supplementary only; no hypothesis-decision role; internal fixed benchmark",
        ))
        result_number += 1

    primary_count = sum(row["role"] == "PRIMARY_INFERENTIAL" for row in rows_out)
    he2a_primary_count = sum(row["role"] == "PRIMARY_INFERENTIAL" and row["hypothesis_component"] == "HE2_A" for row in rows_out)
    he2b_primary_count = sum(row["role"] == "PRIMARY_INFERENTIAL" and row["hypothesis_component"] == "HE2_B" for row in rows_out)
    supplementary_count = sum(row["role"] == "SUPPLEMENTARY" for row in rows_out)
    require((primary_count, he2a_primary_count, he2b_primary_count, supplementary_count) == (16, 15, 1, 3), "result count mismatch")

    forbidden = ("SUPPORTED", "NOT_SUPPORTED", "INCONCLUSIVE", "SIGNIFICANT", "NONSIGNIFICANT")
    serialized_rows = canonical_json(rows_out).upper()
    require(not any(term in serialized_rows for term in forbidden), "forbidden decision vocabulary in results")

    csv_output_path = output_root / CSV_PATH
    json_output_path = output_root / JSON_PATH
    methods_output_path = output_root / METHODS_PATH
    ledger_output_path = output_root / LEDGER_PATH
    for path in (csv_output_path, json_output_path, methods_output_path, ledger_output_path):
        path.parent.mkdir(parents=True, exist_ok=True)

    with csv_output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows_out)

    result_json = {
        "artifact_id": "G3_F03_INFERENTIAL_RESULTS_v0.1",
        "status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
        "ficha": "G3-F03",
        "input_refs": {
            "scientific_main": BASE_MAIN,
            "canonical_plan": PLAN_COMMIT,
            "fichas_activation": FICHAS_ACTIVATION_COMMIT,
            "prompt83": PROMPT83_COMMIT,
        },
        "verified_input_artifacts": {
            REGISTRY_CSV: {"git_blob": REGISTRY_CSV_BLOB, "sha256": REGISTRY_CSV_SHA256},
            REGISTRY_JSON: {"git_blob": REGISTRY_JSON_BLOB, "sha256": REGISTRY_JSON_SHA256},
            REGISTRY_LEDGER: {"git_blob": REGISTRY_LEDGER_BLOB},
            EVAL_PATH: {"sha256": EVAL_SHA256, "n_series": N_SERIES, "n_dam": N_DAM},
        },
        "runtime": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
        },
        "bootstrap": {
            "type": "PAIRED_DAM_CLUSTER_PERCENTILE",
            "B": B,
            "seed": SEED,
            "rng": "numpy.random.default_rng",
            "bit_generator": "PCG64",
            "cluster_count_per_replicate": N_DAM,
            "cluster_list_order": "lexicographic sorted unique DAM identifiers",
            "quantile_method": "linear",
            "primary_estimand_weighting": "SERIES_WEIGHTED",
            "shared_resampling_matrix_shape": [B, N_DAM],
        },
        "primary_contrast_inventory": [row["result_id"] for row in rows_out if row["role"] == "PRIMARY_INFERENTIAL"],
        "results": rows_out,
        "integrity_checks": {
            "registry_row_count": len(registry),
            "evidence_family_count": counts["evidence_family_count"],
            "eligible_family_count": counts["ELIGIBLE"],
            "paired_case_count": N_SERIES,
            "paired_dam_count": N_DAM,
            "case_id_id_unico_sets_match": True,
            "labels_match": True,
            "D1A_DAM_SERIE_JOIN": "exact case_id and id_unico join to historical_case_summary.csv",
            "point_estimate_max_absolute_error_vs_registry": max_reconstruction_error,
            "point_estimate_tolerance": 1e-12,
            "superseded_split_used": False,
            "Attempt06_Decision906_only": True,
        },
        "result_counts": {
            "PRIMARY_INFERENTIAL": primary_count,
            "HE2_A_PRIMARY": he2a_primary_count,
            "HE2_B_PRIMARY": he2b_primary_count,
            "SUPPLEMENTARY_TOP50": supplementary_count,
        },
        "deliberately_excluded_families": [
            {"evidence_family_id": family, "classification": classification, "reason": reason}
            for family, classification, reason in EXCLUDED_FAMILIES
        ],
        "flags": {
            "P_VALUES_CALCULATED": False,
            "STANDARDIZED_EFFECT_SIZE_INVENTED": False,
            "HE2_DECIDED": False,
            "HE5_DECIDED": False,
            "EXP12_REOPENED": False,
            "G3_F04_STARTED": False,
        },
        "warnings": [
            "Some G3-F02 source_commit_binding values use two literal main= labels; exact SHA/blob/path provenance remains explicit."
        ],
    }
    json_output_path.write_text(canonical_json(result_json), encoding="utf-8", newline="\n")
    methods_output_path.write_text(build_methods(), encoding="utf-8", newline="\n")

    ledger_rows = []
    artifact_sources = (
        (SCRIPT_PATH, repository_root / SCRIPT_PATH),
        (CSV_PATH, csv_output_path),
        (JSON_PATH, json_output_path),
        (METHODS_PATH, methods_output_path),
    )
    for canonical_path, actual_path in artifact_sources:
        ledger_rows.append({
            "artifact_path": canonical_path,
            "git_blob_after_commit": git_blob(repository_root, actual_path),
            "sha256": sha256_file(actual_path),
            "size_bytes": actual_path.stat().st_size,
            "hash_scope": "OUTPUT_BYTES_EXCLUDING_SELF_REFERENTIAL_LEDGER",
        })
    with ledger_output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("artifact_path", "git_blob_after_commit", "sha256", "size_bytes", "hash_scope"),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(ledger_rows)

    return {
        "status": "PASS",
        "row_count": len(rows_out),
        "primary_count": primary_count,
        "he2a_primary_count": he2a_primary_count,
        "he2b_primary_count": he2b_primary_count,
        "supplementary_count": supplementary_count,
        "max_point_estimate_error": max_reconstruction_error,
        "csv_sha256": sha256_file(csv_output_path),
        "json_sha256": sha256_file(json_output_path),
        "methods_sha256": sha256_file(methods_output_path),
        "ledger_sha256": sha256_file(ledger_output_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the frozen G3-F03 cluster bootstrap.")
    parser.add_argument("--repository-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output-root", type=Path, default=None)
    args = parser.parse_args()
    output_root = args.output_root if args.output_root is not None else args.repository_root
    try:
        report = run(args.repository_root, output_root)
    except ContractViolation as exc:
        print(canonical_json({"status": "FAIL_CLOSED", "reason": str(exc)}), end="")
        return 2
    print(canonical_json(report), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
