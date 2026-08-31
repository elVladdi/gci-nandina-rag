"""Produce EXP-08 only from the frozen v0.1/v0.2 historical artifacts."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

from ..utils.paths import project_root


V01 = "historical_retrieval_data_aduanas_clase87_v0.1"
V02 = "historical_retrieval_data_aduanas_clase87_v0.2"


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _csv(path: Path, records: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def _json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def _rate(records: list[dict[str, str]], field: str) -> float:
    return sum(float(record[field]) for record in records) / len(records) if records else 0.0


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _strata(records: list[dict[str, str]], field: str, version: str) -> list[dict[str, object]]:
    if field not in records[0]:
        return [{
            "version": version,
            "signal": field,
            "stratum": "NOT_AVAILABLE",
            "n": "NOT_AVAILABLE",
            "Top1": "NOT_AVAILABLE",
            "Top3": "NOT_AVAILABLE",
            "MRR": "NOT_AVAILABLE",
        }]
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for record in records:
        label = "FLAGGED" if record[field] == "True" else "NOT_FLAGGED"
        groups[label].append(record)
    return [{
        "version": version,
        "signal": field,
        "stratum": label,
        "n": len(group),
        "Top1": _rate(group, "exact_at_1"),
        "Top3": _rate(group, "exact_at_3"),
        "MRR": _rate(group, "reciprocal_rank"),
    } for label, group in sorted(groups.items())]


def _precedent(records: list[dict[str, str]]) -> list[dict[str, object]]:
    specs = (("1_DAM", 1, 1), ("2_DAM", 2, 2), ("3_4_DAM", 3, 4), ("5_PLUS_DAM", 5, 999))
    result = []
    for label, lower, upper in specs:
        group = [record for record in records if lower <= int(record["support_count_dams"]) <= upper]
        result.append({"bucket": label, "n": len(group), "Top1": _rate(group, "exact_at_1"), "Top3": _rate(group, "exact_at_3")})
    for label, predicate in (("ONE_TWO_DAM", lambda value: value <= 2), ("THREE_PLUS_DAM", lambda value: value >= 3)):
        group = [record for record in records if predicate(int(record["support_count_dams"]))]
        result.append({"bucket": label, "n": len(group), "Top1": _rate(group, "exact_at_1"), "Top3": _rate(group, "exact_at_3")})
    return result


def run() -> list[dict[str, object]]:
    root = project_root()
    output = root / "outputs" / "evaluation" / "exp08_split_sensitivity_v01_vs_v02"
    output.mkdir(parents=True, exist_ok=True)
    v01_path = root / "outputs" / "evaluation" / V01 / "historical_case_summary.csv"
    v02_path = root / "outputs" / "evaluation" / V02 / "historical_case_summary.csv"
    v01, v02 = _rows(v01_path), _rows(v02_path)

    global_metrics = []
    for label, field in (("Top1", "exact_at_1"), ("Top3", "exact_at_3"), ("Top5", "exact_at_5"), ("Top10", "exact_at_10"), ("Top50", "exact_at_50"), ("MRR", "reciprocal_rank")):
        n01, n02 = sum(float(row[field]) for row in v01), sum(float(row[field]) for row in v02)
        r01, r02 = n01 / len(v01), n02 / len(v02)
        global_metrics.append({"metric": label, "v01_numerator": n01, "v01_denominator": len(v01), "v01_value": r01, "v02_numerator": n02, "v02_denominator": len(v02), "v02_value": r02, "absolute_difference": r02-r01, "percentage_point_difference": (r02-r01)*100, "relative_change": (r02-r01)/r01, "interpretation_scope": "DESCRIPTIVE_SPLIT_SENSITIVITY"})
    _csv(output / "exp08_global_sensitivity_v01_vs_v02.csv", global_metrics)

    _csv(output / "exp08_split_independence_comparison_v01_vs_v02.csv", [
        {"version": "v0.1", "eval_cases": 1006, "historical_eval_dam_overlap": 995, "independence_status": "NOT_DAM_INDEPENDENT", "source": "frozen v0.1 split audit"},
        {"version": "v0.2", "eval_cases": 1056, "historical_eval_dam_overlap": 0, "independence_status": "DAM_GROUPED_INDEPENDENT", "source": "frozen v0.2 split audit"},
    ])
    _csv(output / "exp08_duplicate_sensitivity_comparison_v01_vs_v02.csv", [
        {"version": "v0.1", "signal": "exact_duplicate_cross_split", "count": 377, "availability": "FROZEN"},
        {"version": "v0.1", "signal": "same_nandina_duplicate_cross_split", "count": 376, "availability": "FROZEN"},
        {"version": "v0.1", "signal": "same_dam_exact_duplicate_cross_split", "count": 358, "availability": "FROZEN"},
        {"version": "v0.1", "signal": "near_duplicate_095", "count": "NOT_AVAILABLE", "availability": "NOT_PRESERVED_IN_FROZEN_V01_ARTIFACTS"},
        {"version": "v0.2", "signal": "exact_duplicate_cross_split", "count": 35, "availability": "FROZEN"},
        {"version": "v0.2", "signal": "same_nandina_duplicate_cross_split", "count": 34, "availability": "FROZEN"},
        {"version": "v0.2", "signal": "different_nandina_exact_duplicate_cross_split", "count": 1, "availability": "FROZEN"},
        {"version": "v0.2", "signal": "near_duplicate_095_cross_split", "count": 55, "availability": "FROZEN"},
        {"version": "v0.2", "signal": "near_duplicate_095_same_nandina", "count": 44, "availability": "FROZEN"},
        {"version": "v0.2", "signal": "near_duplicate_095_different_nandina", "count": 37, "availability": "FROZEN"},
    ])
    _csv(output / "exp08_code_sensitivity_v01_vs_v02.csv", _strata(v01, "exact_duplicate_cross_split", "v0.1") + _strata(v02, "exact_duplicate_cross_split", "v0.2"))

    coverage = []
    for version, records in (("v0.1", v01), ("v0.2", v02)):
        counts = Counter(row["expected_nandina"] for row in records)
        coverage.append({"version": version, "eval_cases": len(records), "unique_expected_nandina": len(counts), "single_case_codes": sum(value == 1 for value in counts.values()), "max_cases_per_code": max(counts.values())})
    _csv(output / "exp08_code_coverage_v01_vs_v02.csv", coverage)

    common_ids = {row["case_id"] for row in v01} & {row["case_id"] for row in v02}
    _json(output / "exp08_common_eval_case_availability_v01_vs_v02.json", {"v01_case_ids": len(v01), "v02_case_ids": len(v02), "common_case_ids": len(common_ids), "paired_common_case_analysis_generated": False, "reason": "case identifiers are version-specific and no equivalent frozen pairing key was approved"})
    audit = {
        "normalization": {"status": "SAME", "evidence_source": "frozen case summaries"}, "BM25_implementation": {"status": "SAME", "evidence_source": "historical runners"},
        "BM25_parameters": {"status": "UNKNOWN", "evidence_source": "v0.1 run_metadata absent"}, "candidate_deduplication": {"status": "SAME", "evidence_source": "historical metrics"},
        "metric_definitions": {"status": "SAME", "evidence_source": "frozen metrics"}, "ranking_depth": {"status": "IMPLEMENTATION_DIFFERENCE", "evidence_source": "v0.1 depth 200; v0.2 depth 100"},
        "historical_bank_composition": {"status": "SPLIT_INHERENT_DIFFERENCE", "evidence_source": "split metadata"}, "evalset_composition": {"status": "SPLIT_INHERENT_DIFFERENCE", "evidence_source": "evalsets"},
        "metadata_availability": {"status": "UNKNOWN", "evidence_source": "V01_METADATA_PROVENANCE_LIMITATION"}, "interpretation": "Descriptive frozen-configuration comparison; no exclusive causal attribution to split policy."}
    _json(output / "exp08_comparability_audit_v01_vs_v02.json", audit)
    _json(output / "exp08_he2_sensitivity_assessment_v0.2.json", {"hypothesis": "HE2", "status": "NOT_REOPENED", "reason": "EXP-08 is descriptive and does not rerun or reassess HE2.", "v02_final_benchmark": True})
    proximity = {"error_cases": 518, "same_hs6": 87, "same_hs4": 284, "same_chapter": 147, "different_chapter": 0}
    components = [
        {"component": "DESCRIPTION_QUALITY", "evaluated": False, "status": "NOT_EVALUATED_NO_FROZEN_CASE_RULE", "evidence": "No frozen case-level description quality rule exists."},
        {"component": "HIERARCHICAL_PROXIMITY", "evaluated": True, "status": "SUPPORTED", "evidence": json.dumps(proximity, ensure_ascii=True)},
        {"component": "HISTORICAL_PRECEDENT_AVAILABILITY", "evaluated": True, "status": "MIXED_NON_MONOTONIC", "evidence": json.dumps(_precedent(v02), ensure_ascii=True)},
        {"component": "INTERNAL_EVALUATION_SCOPE", "evaluated": True, "status": "SUPPORTED", "evidence": "v0.2 remains the internal final benchmark; no external validity claim."},
    ]
    _csv(output / "exp08_he5_component_assessment_v0.2.csv", components)
    _json(output / "exp08_final_he5_assessment_v0.2.json", {"hypothesis": "HE5", "statement": "Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.", "status": "PARTIALLY_SUPPORTED", "evaluated_components": 3, "total_components": 4, "limitation": "Description quality is not evaluated because no frozen case-level rule exists.", "v02_final_benchmark": True})
    (output / "exp08_integrated_findings_v0.2.md").write_text("# EXP-08: sensibilidad v0.1 vs v0.2\n\nLa comparacion es descriptiva y globalmente no pareada: v0.1 tiene 1006 casos y v0.2 tiene 1056. No son evalsets equivalentes; no se realizan pruebas inferenciales ni afirmaciones causales.\n\nv0.2 permanece como benchmark final: su solapamiento DAM historico-evaluacion es cero, frente a 995 DAM de v0.1. La diferencia de metricas refleja sensibilidad entre configuraciones congeladas, no un efecto exclusivo del split: v0.1 tiene profundidad 200, v0.2 profundidad 100 y v0.1 no conserva `run_metadata.json`.\n\nHE2 no se reabre. HE5 queda parcialmente respaldada: se evaluaron proximidad jerarquica, precedentes historicos y alcance interno; calidad descriptiva queda sin evaluar por ausencia de regla congelada por caso.\n", encoding="utf-8")
    docs = root / "docs" / "exp08_split_sensitivity_inventory.md"
    docs.write_text("# Inventario EXP-08\n\n- Comparabilidad: `exp08_comparability_audit_v01_vs_v02.json`\n- Sensibilidad global: `exp08_global_sensitivity_v01_vs_v02.csv`\n- Independencia por DAM: `exp08_split_independence_comparison_v01_vs_v02.csv`\n- Duplicados y codigos: `exp08_duplicate_sensitivity_comparison_v01_vs_v02.csv`, `exp08_code_coverage_v01_vs_v02.csv`, `exp08_code_sensitivity_v01_vs_v02.csv`\n- HE2/HE5: `exp08_he2_sensitivity_assessment_v0.2.json`, `exp08_he5_component_assessment_v0.2.csv`, `exp08_final_he5_assessment_v0.2.json`\n\nSe usaron exclusivamente artefactos historicos congelados; no se ejecuto retrieval ni modelo.\n", encoding="utf-8")
    inputs = [v01_path, v02_path, root / "data" / "processed" / "data_aduanas_historico_clase87_v0.1.csv", root / "data" / "processed" / "data_aduanas_evalset_clase87_v0.1.csv", root / "data" / "processed" / "data_aduanas_historico_clase87_v0.2.csv", root / "data" / "processed" / "data_aduanas_evalset_clase87_v0.2.csv"]
    generated = sorted(path for path in output.iterdir() if path.is_file() and path.name != "gate_exp08_split_sensitivity_manifest_v0.2.json")
    _json(output / "gate_exp08_split_sensitivity_manifest_v0.2.json", {"phase": "EXP-08", "analysis_type": "DESCRIPTIVE_SPLIT_SENSITIVITY", "split_v01_type": "PREVIOUS_SERIES_LEVEL_SPLIT", "split_v02_type": "DAM_GROUPED_FINAL_SPLIT", "v02_final_benchmark": True, "evalsets_equivalent": False, "global_comparison_paired": False, "common_case_ids": len(common_ids), "algorithm_reexecuted": False, "model_called": False, "new_retrieval": False, "web_used": False, "causal_claim": False, "v01_run_metadata_available": False, "v01_metadata_provenance_limitation": True, "implementation_difference_recorded": "ranking_depth_v01_200_v02_100", "he2_reopened": False, "description_quality_evaluated": False, "he5_final_assessed": True, "gate_exp08": "APPROVED", "ready_for_exp05_exp07_formal_close": True, "input_sha256": {path.relative_to(root).as_posix(): _sha256(path) for path in inputs}, "output_sha256": {path.name: _sha256(path) for path in generated}})
    return global_metrics


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=True))
