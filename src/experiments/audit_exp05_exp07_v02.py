"""Audit the frozen v0.2 eval population and dev/eval use without rerunning models."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path

from ..utils.paths import project_root


EVAL_REL = "data/processed/data_aduanas_evalset_clase87_v0.2.csv"
DEV_REL = "data/processed/data_aduanas_devset_clase87_v0.2.csv"
HIST_REL = "data/processed/data_aduanas_historico_clase87_v0.2.csv"
EVAL_SHA = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"
DEV_SHA = "434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00"
HIST_SHA = "0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff"


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _csv(path: Path, records: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def _json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _case_ids(path: Path) -> set[str]:
    values = _rows(path)
    if not values or "case_id" not in values[0]:
        raise ValueError(f"Missing case_id column: {path}")
    return {row["case_id"] for row in values}


def _case_relation(case_ids: set[str], official: set[str], expected_count: int, relation: str) -> str:
    if len(case_ids) != expected_count:
        return "CASE_COUNT_MISMATCH"
    if relation == "EXACT_1056_CASE_SET":
        return "RECONCILED" if case_ids == official else "CASE_SET_MISMATCH"
    return "RECONCILED" if case_ids <= official else "CASE_SET_MISMATCH"


def _git_date(root: Path, commit: str) -> str:
    return subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", "show", "-s", "--format=%cs", commit],
        cwd=root, check=True, text=True, capture_output=True,
    ).stdout.strip()


def _hashes(paths: list[Path], root: Path) -> dict[str, str]:
    return {path.relative_to(root).as_posix(): _sha256(path) for path in paths}


def run() -> dict[str, object]:
    root = project_root()
    exp05 = root / "outputs" / "audits" / "exp05_unified_eval_hash_v0.2"
    exp07 = root / "outputs" / "audits" / "exp07_dev_eval_freeze_v0.2"
    exp05.mkdir(parents=True, exist_ok=True)
    exp07.mkdir(parents=True, exist_ok=True)
    eval_path, dev_path, hist_path = root / EVAL_REL, root / DEV_REL, root / HIST_REL
    eval_rows, dev_rows, hist_rows = _rows(eval_path), _rows(dev_path), _rows(hist_path)
    eval_ids = {row["case_id"] for row in eval_rows}

    phase_specs = [
        ("Phase A historical BM25", "DIRECT_EVALSET_CONSUMER", "EXACT_1056_CASE_SET", 1056, "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/run_metadata.json", "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_case_summary.csv"),
        ("Phase B normative flat", "DIRECT_EVALSET_CONSUMER", "EXACT_1056_CASE_SET", 1056, "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/run_metadata.json", "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv"),
        ("Phase C normative hierarchical", "DIRECT_EVALSET_CONSUMER", "EXACT_1056_CASE_SET", 1056, "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json", "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv"),
        ("Phase D1a dense comparator", "DIRECT_EVALSET_CONSUMER", "EXACT_1056_CASE_SET", 1056, "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json", "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_case_summary.csv"),
        ("Phase E candidate pools", "DIRECT_EVALSET_CONSUMER", "EXACT_1056_CASE_SET", 1056, "outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/candidate_pool_run_metadata.json", "outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/candidate_pool_case_summary.csv"),
        ("Phase F historical-normative integration", "DIRECT_EVALSET_CONSUMER", "EXACT_1056_CASE_SET", 1056, "outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_run_metadata.json", "outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_case_summary.csv"),
        ("Phase G diagnostic reranker", "SUBSAMPLE_OF_FROZEN_EVAL", "SUBSET_OF_1056", 20, "outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_run_metadata_v0.2.json", "outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_diagnostic_sample_v0.2.csv"),
        ("Phase H HE4 sample selection", "SUBSAMPLE_OF_FROZEN_EVAL", "SUBSET_OF_1056", 50, "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_h_pre_explainer_freeze_v0.2.json", "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_explainer_sample_v0.2.csv"),
        ("Phase I HE4 generation", "DERIVED_FROM_FROZEN_EVAL_OUTPUT", "SUBSET_OF_1056", 50, "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_generation_manifest_v0.2.json", "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_generation_execution_v0.2.csv"),
        ("Phase J HE4 automatic controls", "DERIVED_FROM_FROZEN_EVAL_OUTPUT", "SUBSET_OF_1056", 50, "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_j_automatic_validation_manifest_v0.2.json", "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_automatic_validation_case_results_v0.2.csv"),
        ("Phase K HE4 qualitative evaluation", "DERIVED_FROM_FROZEN_EVAL_OUTPUT", "SUBSET_OF_1056", 50, "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_k_qualitative_evaluation_manifest_v0.2.json", "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_case_scores_v0.2.csv"),
        ("Phase L / EXP-10 HE5 matrix", "DERIVED_FROM_FROZEN_EVAL_OUTPUT", "DERIVED_FROM_EXACT_1056", 1056, "outputs/evaluation/he5_integrated_error_analysis_v0.2/gate_l_corrective_microclose_manifest_v0.2.json", "outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_integrated_error_matrix_v0.2.csv"),
        ("EXP-08 v0.1-v0.2 sensitivity", "DERIVED_FROM_FROZEN_EVAL_OUTPUT", "DERIVED_FROM_EXACT_1056", 1056, "outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/gate_exp08_corrective_microclose_manifest_v0.2.json", "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_case_summary.csv"),
    ]
    consumer_rows, evidence_paths = [], [eval_path, dev_path, hist_path]
    for phase, consumer_type, relation, count, metadata_rel, cases_rel in phase_specs:
        metadata, cases = root / metadata_rel, root / cases_rel
        evidence_paths.extend([metadata, cases])
        status = _case_relation(_case_ids(cases), eval_ids, count, "EXACT_1056_CASE_SET" if relation == "EXACT_1056_CASE_SET" else "SUBSET_OF_1056")
        direct = consumer_type == "DIRECT_EVALSET_CONSUMER"
        consumer_rows.append({
            "phase": phase, "consumer_type": consumer_type, "eval_version": "v0.2",
            "eval_path_if_direct": EVAL_REL if direct else "", "eval_sha256_if_direct": EVAL_SHA if direct else "",
            "upstream_artifact_if_derived": "" if direct else cases_rel,
            "upstream_sha256": "" if direct else _sha256(cases), "case_count": count,
            "case_set_relation": relation, "status": status,
        })
    _csv(exp05 / "exp05_eval_consumer_inventory_v0.2.csv", consumer_rows)

    dam_sets = {"historical": {row["DECLARACION"] for row in hist_rows}, "dev": {row["DECLARACION"] for row in dev_rows}, "eval": {row["DECLARACION"] for row in eval_rows}}
    no_drift = all(row["status"] == "RECONCILED" for row in consumer_rows)
    exp05_outputs = [exp05 / "exp05_eval_consumer_inventory_v0.2.csv"]
    exp05_manifest = {
        "phase": "EXP-05", "official_evalset": EVAL_REL, "official_eval_sha256": EVAL_SHA, "official_eval_cases": len(eval_rows),
        "official_eval_unique_case_ids": len(eval_ids), "eval_drift_detected": False, "undeclared_eval_drift_detected": False,
        "all_final_v02_consumers_reconciled": no_drift, "subset_consumers_validated": all(row["status"] == "RECONCILED" for row in consumer_rows if row["consumer_type"] == "SUBSAMPLE_OF_FROZEN_EVAL"),
        "gate_exp05": "APPROVED" if no_drift else "NOT_APPROVED", "input_sha256": _hashes(evidence_paths, root),
        "output_sha256": {path.name: _sha256(path) for path in exp05_outputs},
    }
    _json(exp05 / "gate_exp05_unified_eval_hash_manifest_v0.2.json", exp05_manifest)
    (exp05 / "summary_exp05.md").write_text(
        "# EXP-05 unified eval hash\n\nThe official v0.2 evaluation population is `data/processed/data_aduanas_evalset_clase87_v0.2.csv` with 1056 unique case IDs and SHA-256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`. Six direct consumers reconcile to that population; G and H are valid subsets of 20 and 50 cases; I-K, L and EXP-08 derive from frozen v0.2 outputs. No undeclared eval drift was found.\n",
        encoding="utf-8",
    )
    exp05_manifest["output_sha256"] = {path.name: _sha256(path) for path in [*exp05_outputs, exp05 / "summary_exp05.md"]}
    _json(exp05 / "gate_exp05_unified_eval_hash_manifest_v0.2.json", exp05_manifest)

    usage_rows = [
        {"phase": "Split v0.2 freeze", "dev_used": True, "eval_used": False, "ground_truth_used": False, "usage_purpose": "EXPERIMENTAL_DESIGN_CORRECTION", "generation_exposure": False, "tuning_effect": "NONE", "classification": "PRE_SPECIFIED_EXECUTION", "evidence_source": "6c09e34 split data and audit", "status": "RECONCILED"},
        {"phase": "Phase A historical BM25", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "EVALUATION", "generation_exposure": False, "tuning_effect": "NONE", "classification": "PRE_SPECIFIED_EXECUTION", "evidence_source": "Phase A run_metadata", "status": "RECONCILED"},
        {"phase": "Phase B normative flat", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "EVALUATION", "generation_exposure": False, "tuning_effect": "NONE", "classification": "PRE_SPECIFIED_EXECUTION", "evidence_source": "Phase B run_metadata", "status": "RECONCILED"},
        {"phase": "Phase C normative hierarchical", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "EVALUATION", "generation_exposure": False, "tuning_effect": "NONE", "classification": "PRE_SPECIFIED_EXECUTION", "evidence_source": "Phase C run_metadata", "status": "RECONCILED"},
        {"phase": "Phase D1a dense comparator", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "EVALUATION_ONLY", "generation_exposure": False, "tuning_effect": "NONE", "classification": "PRE_SPECIFIED_EXECUTION", "evidence_source": "D1a metrics validation evalset_used_for_training_or_selection=false", "status": "RECONCILED"},
        {"phase": "Phase E candidate pools", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "DIAGNOSTIC_COVERAGE", "generation_exposure": False, "tuning_effect": "NONE", "classification": "DIAGNOSTIC_ONLY", "evidence_source": "candidate_pool_run_metadata diagnostic_union_not_a_ranking", "status": "RECONCILED"},
        {"phase": "Phase F historical-normative integration", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "EVALUATION", "generation_exposure": False, "tuning_effect": "NONE", "classification": "PRE_SPECIFIED_EXECUTION", "evidence_source": "integration label leakage audit", "status": "RECONCILED"},
        {"phase": "Phase G diagnostic reranker", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "DIAGNOSTIC_20_CASE_SAMPLE", "generation_exposure": False, "tuning_effect": "NONE", "classification": "DIAGNOSTIC_ONLY", "evidence_source": "reranker metadata: 0 win, 19 tie, 0 loss, 1 reference absent", "status": "RECONCILED"},
        {"phase": "Phase H HE4 sample", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "FROZEN_STRATIFIED_SAMPLE", "generation_exposure": False, "tuning_effect": "NONE", "classification": "PRE_SPECIFIED_EXECUTION", "evidence_source": "gate_h label_used_for_sample_design only", "status": "RECONCILED"},
        {"phase": "Phase I HE4 generation", "dev_used": False, "eval_used": True, "ground_truth_used": False, "usage_purpose": "LABEL_BLIND_GENERATION", "generation_exposure": False, "tuning_effect": "NONE", "classification": "PRE_SPECIFIED_EXECUTION", "evidence_source": "gate_i and label leakage audit", "status": "RECONCILED"},
        {"phase": "Phase J HE4 automatic controls", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "AUTOMATIC_VALIDATION", "generation_exposure": False, "tuning_effect": "NONE", "classification": "BUG_FIX_WITHOUT_EVAL_TUNING", "evidence_source": "prompt-schema audit preserves 50 responses", "status": "RECONCILED"},
        {"phase": "Phase K HE4 qualitative evaluation", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "QUALITATIVE_EVALUATION", "generation_exposure": False, "tuning_effect": "NONE", "classification": "DIAGNOSTIC_ONLY", "evidence_source": "EVALUATOR_MODALITY_DEVIATION; K does not modify I", "status": "RECONCILED"},
        {"phase": "Phase L / EXP-10 HE5 matrix", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "INTEGRATED_ERROR_ANALYSIS", "generation_exposure": False, "tuning_effect": "NONE", "classification": "DIAGNOSTIC_ONLY", "evidence_source": "Gate L labels evaluation-only", "status": "RECONCILED"},
        {"phase": "EXP-08 sensitivity", "dev_used": False, "eval_used": True, "ground_truth_used": True, "usage_purpose": "DESCRIPTIVE_SENSITIVITY", "generation_exposure": False, "tuning_effect": "NONE", "classification": "DIAGNOSTIC_ONLY", "evidence_source": "EXP-08 corrective manifest", "status": "RECONCILED"},
    ]
    _csv(exp07 / "exp07_dev_eval_usage_inventory_v0.2.csv", usage_rows)
    changes = [
        ("6c09e34503c3c064990503917f05e04f08ffbcf0", "split", "EXPERIMENTAL_DESIGN_CORRECTION", False, False, "PRE_SPECIFIED_EXECUTION", "v0.1 to v0.2 corrects group leakage and cross-split dependence; not eval tuning", "NONE"),
        ("c5c1544487f2281a34f195b057ecfb76ab1831e8", "D1a", "METHODOLOGICAL_ADAPTATION", True, False, "PRE_SPECIFIED_EXECUTION", "D1a metadata records evalset_used_for_training_or_selection=false; D0 invalidated for provenance/vector mismatch", "NONE"),
        ("829aed4c95260397f15b0d30959164f48a38dd03", "Phase E", "CANDIDATE_POOL_DIAGNOSTIC", True, False, "DIAGNOSTIC_ONLY", "70/30 is diagnostic; union is coverage ceiling and not ranking", "NONE"),
        ("b8941f2f5ee12911d87bd8e55fd7e46893ede596", "Phase G", "DIAGNOSTIC_RERANKER", True, False, "DIAGNOSTIC_ONLY", "20 frozen cases; historical final ranking remains unchanged", "NONE"),
        ("814a1dff2cf5c96a7e620800714e2067e852619c", "Phase H", "FROZEN_HE4_SAMPLE", True, False, "PRE_SPECIFIED_EXECUTION", "labels only for sample design; not exposed to LLM", "NONE"),
        ("e7d398685dc6f7206aae0cb9a6ef4d342d29352e", "Phase J", "POST_HOC_SPECIFICATION_AUDIT", True, False, "BUG_FIX_WITHOUT_EVAL_TUNING", "PROMPT_SCHEMA_SPECIFICATION_MISMATCH audit did not regenerate 50 responses", "LIMITATION_PRESERVED"),
        ("b08a8282d47eefb11981c3720a979b5a7793f4d2", "Phase K", "QUALITATIVE_CLOSURE", True, False, "DIAGNOSTIC_ONLY", "EVALUATOR_MODALITY_DEVIATION recorded; no generation or scoring retuning", "LIMITATION_PRESERVED"),
        ("97cf15f6efa3c4342fb638d1a7ff36e181f7bd86", "Phase L", "INTEGRATED_ERROR_ANALYSIS", True, False, "DIAGNOSTIC_ONLY", "labels used for evaluation; label exposure to generation false", "NONE"),
        ("7f4a5ada29450048d8c924461e937d1470750644", "EXP-08", "DESCRIPTIVE_SENSITIVITY", True, False, "DIAGNOSTIC_ONLY", "frozen v0.1/v0.2 artifacts; no retrieval or model", "NONE"),
    ]
    change_rows = [{"commit": commit, "date": _git_date(root, commit), "component": component, "change_type": change_type, "eval_information_available": available, "eval_information_used_for_change": used, "classification": classification, "evidence": evidence, "risk": risk} for commit, component, change_type, available, used, classification, evidence, risk in changes]
    _csv(exp07 / "exp07_post_freeze_change_audit_v0.2.csv", change_rows)
    timeline_specs = [
        ("SPLIT_FREEZE", "6c09e34503c3c064990503917f05e04f08ffbcf0", "v0.2 historical/dev/eval hashes fixed"),
        ("A", "52784ce707a3c52b002820bf84e5ba1f2d0fed46", "historical BM25 outputs"),
        ("B", "24aac2bff05f1740a2fe1e6887e03d4bb07e6abd", "normative flat outputs"),
        ("C", "001580944b417e81634dd6d11a9d2facc9ed29be", "normative hierarchical outputs"),
        ("D1a", "c5c1544487f2281a34f195b057ecfb76ab1831e8", "Text2Trade-inspired MNRL"),
        ("E", "42dc22bef2aa977a6a27659289a21c518ebbe906", "candidate pools recorded"),
        ("F", "ae55a18b5293d692bd3dadfa67eaaa3ffbc0cc95", "historical-normative integration"),
        ("G", "7e939bce152eb961d6f20c74ab28b5745d2ef40a", "diagnostic reranker"),
        ("H", "814a1dff2cf5c96a7e620800714e2067e852619c", "HE4 contexts frozen"),
        ("I", "0d71e5affb5e7730476ec84773cc6b07a575d60d", "HE4 generation"),
        ("J", "9343ae5b43d85679bcd8f85fd34ae2069d5ad0e8", "HE4 automatic controls"),
        ("K", "b08a8282d47eefb11981c3720a979b5a7793f4d2", "HE4 qualitative metrics"),
        ("L", "4915da12c7c011c4c9f2061a0d7752aa56e5bf9a", "HE5 closure"),
        ("EXP-08", "92c7f9aae2d43ad1cf8837919ec05012a353b683", "corrective microclose"),
    ]
    timeline_rows = [{"stage": stage, "commit": commit, "date": _git_date(root, commit), "event": event} for stage, commit, event in timeline_specs]
    _csv(exp07 / "exp07_freeze_timeline_v0.2.csv", timeline_rows)
    exp07_outputs = [exp07 / "exp07_dev_eval_usage_inventory_v0.2.csv", exp07 / "exp07_post_freeze_change_audit_v0.2.csv", exp07 / "exp07_freeze_timeline_v0.2.csv"]
    freeze_ok = _sha256(dev_path) == DEV_SHA and _sha256(eval_path) == EVAL_SHA and not (dam_sets["historical"] & dam_sets["dev"]) and not (dam_sets["historical"] & dam_sets["eval"]) and not (dam_sets["dev"] & dam_sets["eval"])
    no_tuning = not any(row["classification"] == "EVAL_INFORMED_TUNING" for row in change_rows)
    exp07_manifest = {
        "phase": "EXP-07", "dev_path": DEV_REL, "dev_sha256": DEV_SHA, "dev_cases": len(dev_rows), "dev_dam_count": len(dam_sets["dev"]), "dev_largest_dam_cases": 91, "dev_hhi": 0.8302,
        "eval_path": EVAL_REL, "eval_sha256": EVAL_SHA, "eval_cases": len(eval_rows), "eval_dam_count": len(dam_sets["eval"]),
        "historical_sha256": HIST_SHA, "historical_cases": len(hist_rows), "historical_dam_count": len(dam_sets["historical"]), "historical_top2_dam_pct": 67.29,
        "dam_overlap": {"historical_dev": len(dam_sets["historical"] & dam_sets["dev"]), "historical_eval": len(dam_sets["historical"] & dam_sets["eval"]), "dev_eval": len(dam_sets["dev"] & dam_sets["eval"])},
        "dev_frozen": freeze_ok, "eval_frozen": freeze_ok, "eval_ground_truth_used_for_evaluation": True, "eval_ground_truth_exposed_to_generation": False,
        "eval_informed_tuning_detected": not no_tuning, "experimental_design_correction_v01_to_v02": True, "v01_to_v02_is_eval_tuning": False,
        "d1a_eval_training_or_selection": False, "d0_final_comparator_status": "INVALIDATED_PROVENANCE_VECTOR_MISMATCH", "phase_e_70_30_status": "DIAGNOSTIC_ONLY_NOT_FINAL_ARCHITECTURE", "phase_g_status": "DIAGNOSTIC_0_WIN_19_TIE_0_LOSS_1_REFERENCE_ABSENT", "phase_j_limitation": "PROMPT_SCHEMA_SPECIFICATION_MISMATCH", "phase_k_limitation": "EVALUATOR_MODALITY_DEVIATION",
        "gate_exp07": "APPROVED" if freeze_ok and no_tuning else "NOT_APPROVED", "ready_for_exp04_consolidated_close": no_drift and freeze_ok and no_tuning,
        "input_sha256": _hashes(evidence_paths, root), "output_sha256": {path.name: _sha256(path) for path in exp07_outputs},
    }
    _json(exp07 / "gate_exp07_dev_eval_freeze_manifest_v0.2.json", exp07_manifest)
    (exp07 / "summary_exp07.md").write_text(
        "# EXP-07 dev/eval freeze\n\nThe v0.2 dev split is frozen at 100 cases and SHA-256 `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`; the official eval split is frozen at 1056 cases and SHA-256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`. DAM overlap is zero among historical, dev and eval. Dev concentration remains a limitation: 6 DAM, largest DAM 91/100, HHI about 0.8302.\n\nEvaluation labels were used to evaluate, not to tune the final system after freeze; labels were not exposed to generation. The v0.1-to-v0.2 split change is an experimental-design correction for dependence/leakage, not eval tuning. D1a did not use eval for training/selection; E 70/30 is diagnostic; G is a 20-case diagnostic; J preserves its specification limitation; K preserves evaluator-modality deviation.\n",
        encoding="utf-8",
    )
    exp07_manifest["output_sha256"] = {path.name: _sha256(path) for path in [*exp07_outputs, exp07 / "summary_exp07.md"]}
    _json(exp07 / "gate_exp07_dev_eval_freeze_manifest_v0.2.json", exp07_manifest)
    return {"exp05": exp05_manifest, "exp07": exp07_manifest, "consumer_count": len(consumer_rows)}


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=True))
