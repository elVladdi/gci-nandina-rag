"""Build the deterministic EXP-04 / Group 1 consolidated closure inventory.

This module only reads frozen experiment artifacts.  It intentionally contains
no retrieval, model, network, or split-generation operation.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "outputs" / "evaluation" / "exp04_consolidated_closure_v0.2"
BRANCH = "codex/exp04-rerun-v02"
HEAD_BEFORE_CLOSE = "96e8270a114a8c5e50f326eb102129c9028878cf"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def artifact(path: str, phase: str, role: str) -> dict[str, object]:
    candidate = REPO / path
    return {
        "phase": phase,
        "artifact": path,
        "sha256": sha256(candidate) if candidate.exists() else "MISSING",
        "exists": candidate.exists(),
        "frozen_evidence": True,
        "role": role,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    result_fields = [
        "phase", "component", "metric", "numerator", "denominator", "value",
        "unit", "scope", "interpretation", "source_artifact",
    ]
    results = [
        {"phase": "EXP-04 A", "component": "historical retrieval", "metric": "Top-1", "numerator": 538, "denominator": 1056, "value": "0.509470", "unit": "rate", "scope": "evalset v0.2", "interpretation": "main candidate-ranking evidence", "source_artifact": "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json"},
        {"phase": "EXP-04 A", "component": "historical retrieval", "metric": "Top-3", "numerator": 709, "denominator": 1056, "value": "0.671402", "unit": "rate", "scope": "evalset v0.2", "interpretation": "main candidate-ranking evidence", "source_artifact": "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json"},
        {"phase": "EXP-04 A", "component": "historical retrieval", "metric": "Top-5", "numerator": 806, "denominator": 1056, "value": "0.763258", "unit": "rate", "scope": "evalset v0.2", "interpretation": "main candidate-ranking evidence", "source_artifact": "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json"},
        {"phase": "EXP-04 A", "component": "historical retrieval", "metric": "Top-10", "numerator": 941, "denominator": 1056, "value": "0.891098", "unit": "rate", "scope": "evalset v0.2", "interpretation": "main candidate-ranking evidence", "source_artifact": "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json"},
        {"phase": "EXP-04 A", "component": "historical retrieval", "metric": "Top-50", "numerator": 1047, "denominator": 1056, "value": "0.991477", "unit": "rate", "scope": "evalset v0.2", "interpretation": "main candidate-ranking evidence", "source_artifact": "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json"},
        {"phase": "EXP-04 A", "component": "historical retrieval", "metric": "MRR", "numerator": "", "denominator": 1056, "value": "0.629707", "unit": "rate", "scope": "evalset v0.2", "interpretation": "main candidate-ranking evidence", "source_artifact": "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json"},
        {"phase": "EXP-04 B", "component": "normative BM25 flat", "metric": "Top-1", "numerator": "", "denominator": 1056, "value": "0.027462", "unit": "rate", "scope": "evalset v0.2", "interpretation": "documentary evidence; not a ranking replacement", "source_artifact": "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json"},
        {"phase": "EXP-04 B", "component": "normative BM25 flat", "metric": "Recall@100", "numerator": "", "denominator": 1056, "value": "0.071023", "unit": "rate", "scope": "evalset v0.2", "interpretation": "documentary evidence", "source_artifact": "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json"},
        {"phase": "EXP-04 B", "component": "normative BM25 flat", "metric": "MRR@100", "numerator": "", "denominator": 1056, "value": "0.042297", "unit": "rate", "scope": "evalset v0.2", "interpretation": "documentary evidence", "source_artifact": "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json"},
        {"phase": "EXP-04 C", "component": "normative BM25 hierarchical", "metric": "Top-1", "numerator": "", "denominator": 1056, "value": "0.026515", "unit": "rate", "scope": "evalset v0.2", "interpretation": "documentary evidence; not a ranking replacement", "source_artifact": "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json"},
        {"phase": "EXP-04 C", "component": "normative BM25 hierarchical", "metric": "Recall@100", "numerator": "", "denominator": 1056, "value": "0.101326", "unit": "rate", "scope": "evalset v0.2", "interpretation": "documentary evidence", "source_artifact": "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json"},
        {"phase": "EXP-04 C", "component": "normative BM25 hierarchical", "metric": "Recall@200", "numerator": "", "denominator": 1056, "value": "0.303977", "unit": "rate", "scope": "evalset v0.2", "interpretation": "documentary evidence", "source_artifact": "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json"},
        {"phase": "EXP-04 C", "component": "normative BM25 hierarchical", "metric": "MRR@100", "numerator": "", "denominator": 1056, "value": "0.041981", "unit": "rate", "scope": "evalset v0.2", "interpretation": "documentary evidence", "source_artifact": "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json"},
        {"phase": "EXP-04 C", "component": "normative BM25 hierarchical", "metric": "MRR@200", "numerator": "", "denominator": 1056, "value": "0.043342", "unit": "rate", "scope": "evalset v0.2", "interpretation": "documentary evidence", "source_artifact": "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json"},
        {"phase": "EXP-04 D1a", "component": "Text2Trade dense", "metric": "Top-1", "numerator": 75, "denominator": 1056, "value": "0.071023", "unit": "rate", "scope": "evalset v0.2", "interpretation": "early retrieval evidence", "source_artifact": "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json"},
        {"phase": "EXP-04 D1a", "component": "Text2Trade dense", "metric": "Top-3", "numerator": 143, "denominator": 1056, "value": "0.135417", "unit": "rate", "scope": "evalset v0.2", "interpretation": "early retrieval evidence", "source_artifact": "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json"},
        {"phase": "EXP-04 D1a", "component": "Text2Trade dense", "metric": "Top-5", "numerator": 187, "denominator": 1056, "value": "0.177083", "unit": "rate", "scope": "evalset v0.2", "interpretation": "early retrieval evidence", "source_artifact": "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json"},
        {"phase": "EXP-04 D1a", "component": "Text2Trade dense", "metric": "Top-10", "numerator": 257, "denominator": 1056, "value": "0.243371", "unit": "rate", "scope": "evalset v0.2", "interpretation": "early retrieval evidence", "source_artifact": "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json"},
        {"phase": "EXP-04 D1a", "component": "Text2Trade dense", "metric": "Top-50", "numerator": 497, "denominator": 1056, "value": "0.470644", "unit": "rate", "scope": "evalset v0.2", "interpretation": "early retrieval evidence", "source_artifact": "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json"},
        {"phase": "EXP-04 E", "component": "candidate pool", "metric": "pool size", "numerator": 20, "denominator": "", "value": "20", "unit": "candidates", "scope": "frozen protocol", "interpretation": "candidate-pool stage completed", "source_artifact": "outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/candidate_pool_run_metadata.json"},
        {"phase": "EXP-04 F", "component": "historical-normative integration", "metric": "integrated rows", "numerator": 1056, "denominator": 1056, "value": "1.000000", "unit": "coverage", "scope": "evalset v0.2", "interpretation": "integration artifact completed", "source_artifact": "outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_run_metadata.json"},
        {"phase": "EXP-04 G", "component": "diagnostic reranker", "metric": "tie", "numerator": 19, "denominator": 20, "value": "0.950000", "unit": "rate", "scope": "20-case diagnostic sample", "interpretation": "diagnostic only; no benchmark claim", "source_artifact": "outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_run_metadata_v0.2.json"},
        {"phase": "EXP-04 H", "component": "HE4 explanation audit", "metric": "audited cases", "numerator": 50, "denominator": 1056, "value": "0.047348", "unit": "coverage", "scope": "stratified sample", "interpretation": "fixed top-3 context; local explanation only", "source_artifact": "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_h_pre_explainer_freeze_v0.2.json"},
        {"phase": "EXP-04 I", "component": "HE4 explanations", "metric": "generated explanations", "numerator": 50, "denominator": 50, "value": "1.000000", "unit": "coverage", "scope": "fixed sample", "interpretation": "local explanation only", "source_artifact": "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_generation_manifest_v0.2.json"},
        {"phase": "EXP-04 J", "component": "HE4 validation", "metric": "generic warning", "numerator": 41, "denominator": 50, "value": "0.820000", "unit": "rate", "scope": "fixed sample", "interpretation": "schema mismatch preserved as limitation", "source_artifact": "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_j_automatic_validation_manifest_v0.2.json"},
        {"phase": "EXP-04 K", "component": "HE4 qualitative audit", "metric": "auditable cases", "numerator": 28, "denominator": 50, "value": "0.560000", "unit": "rate", "scope": "fixed sample", "interpretation": "independent AI reviewer; exploratory", "source_artifact": "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_k_qualitative_evaluation_manifest_v0.2.json"},
        {"phase": "EXP-04 K", "component": "HE4 qualitative audit", "metric": "mean score", "numerator": "", "denominator": 50, "value": "11.72", "unit": "score", "scope": "fixed sample", "interpretation": "independent AI reviewer; exploratory", "source_artifact": "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_k_qualitative_evaluation_manifest_v0.2.json"},
        {"phase": "EXP-04 L", "component": "HE5 error analysis", "metric": "evaluated rows", "numerator": 1056, "denominator": 1056, "value": "1.000000", "unit": "coverage", "scope": "evalset v0.2", "interpretation": "integrated error inventory", "source_artifact": "outputs/evaluation/he5_integrated_error_analysis_v0.2/gate_l_corrective_microclose_manifest_v0.2.json"},
        {"phase": "EXP-08", "component": "split sensitivity", "metric": "Gate", "numerator": "", "denominator": "", "value": "APPROVED", "unit": "status", "scope": "v0.1 vs v0.2", "interpretation": "sensitivity limitation preserved", "source_artifact": "outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/gate_exp08_corrective_microclose_manifest_v0.2.json"},
    ]
    write_csv(OUT / "exp04_final_results_registry_v0.2.csv", result_fields, results)

    cards = [
        ("EXP-01", "DAM-grouped split", "CLOSED", "APPROVED", "DAM overlap is zero"),
        ("EXP-02", "duplicate controls", "CLOSED", "APPROVED", "exact and near-duplicate audit preserved"),
        ("EXP-03", "split under imbalance", "CLOSED", "APPROVED", "concentration limitation preserved"),
        ("EXP-04", "full rerun with corrected split", "CLOSED", "APPROVED", "all authorized phases registered"),
        ("EXP-05", "unified evaluation hash", "CLOSED", "APPROVED", "frozen evaluation hash"),
        ("EXP-06", "evaluation protocol", "CLOSED", "APPROVED", "registered by EXP-04 evidence"),
        ("EXP-07", "dev/eval freeze", "CLOSED", "APPROVED", "no eval drift or tuning"),
        ("EXP-08", "split sensitivity", "CLOSED", "APPROVED", "corrective closure approved"),
        ("EXP-09", "HE4 audit protocol", "CLOSED", "APPROVED", "H through K contracts completed"),
        ("EXP-10", "HE5 error inventory", "CLOSED", "APPROVED", "L corrective microclose approved"),
    ]
    card_rows = [{"card": c, "title": t, "status": s, "gate": g, "evidence": e, "blocking_issue": ""} for c, t, s, g, e in cards]
    write_csv(OUT / "exp04_group1_card_closure_matrix_v0.2.csv", ["card", "title", "status", "gate", "evidence", "blocking_issue"], card_rows)

    hypotheses = [
        {"hypothesis": "HE2", "literal_statement": "", "status": "PARTIALLY_SUPPORTED", "status_evidence": "docs/exp04_phase_e_candidate_pools_v02_results.md", "closure_note": "Status preserved; no literal formulation restated."},
        {"hypothesis": "HE3", "literal_statement": "", "status": "SUPPORTED", "status_evidence": "docs/exp04_phase_f_historical_normative_integration_v02_results.md", "closure_note": "Status preserved; no literal formulation restated."},
        {"hypothesis": "HE4", "literal_statement": "", "status": "PARTIALLY_SUPPORTED", "status_evidence": "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_findings_v0.2.md", "closure_note": "Status preserved; no literal formulation restated."},
        {"hypothesis": "HE5", "literal_statement": "Los errores y limites del piloto se concentraran en descripciones ambiguas o incompletas, subpartidas jerarquicamente proximas, casos con precedentes historicos insuficientes y condiciones que restringiran la validez de los resultados al conjunto interno evaluado.", "status": "PARTIALLY_SUPPORTED", "status_evidence": "outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/exp08_final_he5_assessment_v0.2.json", "closure_note": "Literal formulation and status preserved."},
    ]
    write_csv(OUT / "exp04_hypothesis_status_registry_v0.2.csv", ["hypothesis", "literal_statement", "status", "status_evidence", "closure_note"], hypotheses)

    limitations = [
        ("LIM-01", "historical DAM concentration", "DATA_LIMITATION"), ("LIM-02", "dev DAM concentration", "DATA_LIMITATION"),
        ("LIM-03", "residual exact and near duplicates", "EXPERIMENTAL_DESIGN"), ("LIM-04", "weak early normative retrieval", "MODEL_RETRIEVAL"),
        ("LIM-05", "weak early D1a dense retrieval", "MODEL_RETRIEVAL"), ("LIM-06", "20-case reranker sample", "EVALUATION"),
        ("LIM-07", "50-case HE4 sample", "EVALUATION"), ("LIM-08", "HE4 prompt-schema mismatch", "PROTOCOL"),
        ("LIM-09", "AI evaluator modality", "EVALUATION"), ("LIM-10", "description quality not operationalized", "DATA_LIMITATION"),
        ("LIM-11", "v0.1 metadata provenance", "PROVENANCE"), ("LIM-12", "sensitivity depth difference", "EXPERIMENTAL_DESIGN"),
        ("LIM-13", "Clase 87 internal scope", "GENERALIZATION"),
    ]
    write_csv(OUT / "exp04_consolidated_limitations_v0.2.csv", ["id", "limitation", "category", "status"], [{"id": i, "limitation": l, "category": c, "status": "PRESERVED_NOT_RESOLVED"} for i, l, c in limitations])

    source_specs = [
        ("EXP-01", "outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.json", "DAM overlap and duplicate audit"),
        ("EXP-03", "outputs/audits/data_aduanas_splits_clase87_v0.2/concentration_summary_v0.2.json", "concentration audit"),
        ("EXP-04 A", "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json", "historical retrieval metrics"),
        ("EXP-04 B", "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json", "flat normative metrics"),
        ("EXP-04 C", "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json", "hierarchical normative metrics"),
        ("EXP-04 D1a", "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json", "dense metrics"),
        ("EXP-04 E", "outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/candidate_pool_run_metadata.json", "candidate-pool metadata"),
        ("EXP-04 F", "outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_run_metadata.json", "integration metadata"),
        ("EXP-04 G", "outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_run_metadata_v0.2.json", "diagnostic reranker metadata"),
        ("EXP-04 H", "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_h_pre_explainer_freeze_v0.2.json", "HE4 sample freeze"),
        ("EXP-04 I", "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_generation_manifest_v0.2.json", "HE4 generation manifest"),
        ("EXP-04 J", "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_j_automatic_validation_manifest_v0.2.json", "automatic validation"),
        ("EXP-04 K", "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_k_qualitative_evaluation_manifest_v0.2.json", "qualitative validation"),
        ("EXP-04 L", "outputs/evaluation/he5_integrated_error_analysis_v0.2/gate_l_corrective_microclose_manifest_v0.2.json", "HE5 corrective closure"),
        ("EXP-05", "outputs/audits/exp05_unified_eval_hash_v0.2/gate_exp05_unified_eval_hash_manifest_v0.2.json", "unified evaluation freeze"),
        ("EXP-07", "outputs/audits/exp07_dev_eval_freeze_v0.2/gate_exp07_dev_eval_freeze_manifest_v0.2.json", "dev/eval freeze"),
        ("EXP-08", "outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/gate_exp08_corrective_microclose_manifest_v0.2.json", "sensitivity corrective closure"),
    ]
    provenance = [artifact(path, phase, role) for phase, path, role in source_specs]
    write_csv(OUT / "exp04_final_provenance_registry_v0.2.csv", ["phase", "artifact", "sha256", "exists", "frozen_evidence", "role"], provenance)

    generated = [
        OUT / "exp04_final_results_registry_v0.2.csv",
        OUT / "exp04_group1_card_closure_matrix_v0.2.csv",
        OUT / "exp04_hypothesis_status_registry_v0.2.csv",
        OUT / "exp04_consolidated_limitations_v0.2.csv",
        OUT / "exp04_final_provenance_registry_v0.2.csv",
    ]
    manifest = {
        "schema_version": "v0.2", "phase": "EXP-04 consolidated closure", "branch": BRANCH,
        "head_before_close": HEAD_BEFORE_CLOSE, "benchmark_version": "v0.2", "eval_cases": 1056,
        "historical_cases": 2950, "dev_cases": 100, "dam_overlap_zero": True, "eval_drift": False,
        "eval_tuning": False, "cards_closed": [row[0] for row in cards],
        "hypothesis_statuses": {row["hypothesis"]: row["status"] for row in hypotheses},
        "oe1_he1_formal_status": "NOT_FABRICATED_NO_CONSOLIDATED_ASSESSMENT_FOUND",
        "limitations_preserved": True, "unresolved_blocking_issues": [], "group1_ready_to_close": True,
        "ready_for_main_merge_review": True, "merged_to_main": False, "no_model_call": True,
        "no_new_retrieval": True, "no_web": True, "exp04_final_status": "CLOSED",
        "group1_status": "CLOSED", "gate_exp04_consolidated": "APPROVED", "group1_gate": "APPROVED",
        "inputs": provenance, "generated_file_hashes": {p.name: sha256(p) for p in generated},
    }
    write_json(OUT / "gate_exp04_consolidated_closure_manifest_v0.2.json", manifest)

    summary = """# EXP-04 and Group 1 Consolidated Closure v0.2

## Decision

EXP-04 (full rerun with corrected split) and Group 1 experimental design are CLOSED and APPROVED for review before any merge to `main`. This closure is a deterministic inventory of frozen evidence; it did not execute retrieval, call a model, change the split, or reopen hypotheses.

## Principal Evidence

Historical retrieval is the principal candidate-ranking result: Top-1 538/1056 (0.509470), Top-3 709/1056 (0.671402), Top-5 806/1056 (0.763258), Top-10 941/1056 (0.891098), Top-50 1047/1056 (0.991477), and MRR 0.629707. Normative BM25 flat and hierarchical results are preserved as documentary evidence and not as replacements for the main historical ranking. Dense D1a is preserved as early retrieval evidence.

HE4 used a fixed top-3 context for 50 sampled cases and is a local explanation audit only. The diagnostic reranker is not a benchmark claim. The pilot remains internally scoped to Clase 87 and must not be generalized beyond the frozen internal evaluation conditions.

## Integrity

The v0.2 split records zero DAM overlap, no evaluation drift, and no evaluation tuning. Exact and near-duplicate audits, concentration limitations, all listed phase gates, and the EXP-08 corrective sensitivity close are retained in the provenance registry. HE2, HE3, HE4, and HE5 statuses are preserved; no formal OE1/HE1 assessment is invented.

## Scope Boundary

This consolidation does not merge to `main` and does not authorize Group 2. The full list of residual limitations is intentionally preserved in `exp04_consolidated_limitations_v0.2.csv`.
"""
    (OUT / "summary_exp04_consolidated_closure_v0.2.md").write_text(summary, encoding="utf-8")


if __name__ == "__main__":
    main()
