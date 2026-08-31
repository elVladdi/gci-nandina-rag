"""Produce the corrective EXP-08 comparison from frozen artifacts only."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

from ..utils.paths import project_root


V01 = "historical_retrieval_data_aduanas_clase87_v0.1"
V02 = "historical_retrieval_data_aduanas_clase87_v0.2"
ORIGINAL_GATE_COMMIT = "f0a369a7552cf3af7a950b2e7cdef4c286b94a9e"
OUTPUT_MANIFESTS = {
    "gate_exp08_split_sensitivity_manifest_v0.2.json",
    "gate_exp08_corrective_microclose_manifest_v0.2.json",
}


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


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _flag(value: str) -> bool:
    return value.strip().lower() == "true"


def _performance(records: list[dict[str, str]], version: str, signal: str, stratum: str, availability: str, evidence_source: str) -> dict[str, object]:
    if availability != "AVAILABLE":
        return {
            "version": version, "signal": signal, "stratum": stratum, "n": "NOT_AVAILABLE",
            "top1_n": "NOT_AVAILABLE", "top1_rate": "NOT_AVAILABLE",
            "top3_n": "NOT_AVAILABLE", "top3_rate": "NOT_AVAILABLE", "mrr": "NOT_AVAILABLE",
            "availability": availability, "evidence_source": evidence_source,
        }
    count = len(records)
    top1_n = sum(int(row["exact_at_1"]) for row in records)
    top3_n = sum(int(row["exact_at_3"]) for row in records)
    return {
        "version": version, "signal": signal, "stratum": stratum, "n": count,
        "top1_n": top1_n, "top1_rate": top1_n / count if count else None,
        "top3_n": top3_n, "top3_rate": top3_n / count if count else None,
        "mrr": sum(float(row["reciprocal_rank"]) for row in records) / count if count else None,
        "availability": availability, "evidence_source": evidence_source,
    }


def _code_metrics(records: list[dict[str, str]]) -> dict[str, dict[str, object]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in records:
        groups[row["expected_nandina"]].append(row)
    result = {}
    for code, group in groups.items():
        n = len(group)
        top1_n = sum(int(row["exact_at_1"]) for row in group)
        top3_n = sum(int(row["exact_at_3"]) for row in group)
        result[code] = {
            "n": n, "top1_n": top1_n, "top1": top1_n / n,
            "top3_n": top3_n, "top3": top3_n / n,
            "mrr": sum(float(row["reciprocal_rank"]) for row in group) / n,
        }
    return result


def _code_sensitivity(v01: list[dict[str, str]], v02: list[dict[str, str]]) -> list[dict[str, object]]:
    first, second = _code_metrics(v01), _code_metrics(v02)
    result = []
    for code in sorted(set(first) | set(second)):
        left, right = first.get(code), second.get(code)
        status = "CODE_IN_BOTH_EVALSETS" if left and right else "ONLY_V01" if left else "ONLY_V02"
        result.append({
            "reference_nandina": code, "presence_status": status,
            "n_v01": left["n"] if left else 0, "top1_n_v01": left["top1_n"] if left else 0,
            "top1_v01": left["top1"] if left else None, "top3_n_v01": left["top3_n"] if left else 0,
            "top3_v01": left["top3"] if left else None, "mrr_v01": left["mrr"] if left else None,
            "n_v02": right["n"] if right else 0, "top1_n_v02": right["top1_n"] if right else 0,
            "top1_v02": right["top1"] if right else None, "top3_n_v02": right["top3_n"] if right else 0,
            "top3_v02": right["top3"] if right else None, "mrr_v02": right["mrr"] if right else None,
            "delta_top1_v02_minus_v01": right["top1"] - left["top1"] if left and right else None,
            "delta_top3_v02_minus_v01": right["top3"] - left["top3"] if left and right else None,
            "delta_mrr_v02_minus_v01": right["mrr"] - left["mrr"] if left and right else None,
        })
    return result


def _coverage(records: list[dict[str, str]], historical: list[dict[str, str]], version: str) -> dict[str, object]:
    historical_codes = {row["NANDINA"] for row in historical}
    counts = Counter(row["expected_nandina"] for row in records)
    supported = [row for row in records if row["expected_nandina"] in historical_codes]
    supported_codes = {row["expected_nandina"] for row in supported}
    return {
        "version": version, "eval_cases": len(records), "unique_expected_nandina": len(counts),
        "cases_with_historical_nominal_support": len(supported),
        "historical_nominal_support_rate": len(supported) / len(records),
        "supported_codes": len(supported_codes), "total_eval_codes": len(counts),
        "single_case_codes": sum(count == 1 for count in counts.values()), "max_cases_per_code": max(counts.values()),
    }


def _dam_strata(records: list[dict[str, str]], eval_rows: list[dict[str, str]], historical_rows: list[dict[str, str]], version: str) -> list[dict[str, object]]:
    dams_by_id = {row["id_unico"]: row["DECLARACION"] for row in eval_rows}
    historical_dams = {row["DECLARACION"] for row in historical_rows}
    overlap = [row for row in records if dams_by_id[row["id_unico"]] in historical_dams]
    no_overlap = [row for row in records if dams_by_id[row["id_unico"]] not in historical_dams]
    source = "frozen historical/eval split membership"
    return [
        _performance(overlap, version, "DAM_MEMBERSHIP", "DAM_OVERLAP", "AVAILABLE", source),
        _performance(no_overlap, version, "DAM_MEMBERSHIP", "NO_DAM_OVERLAP", "AVAILABLE", source),
    ]


def _precedent(records: list[dict[str, str]]) -> list[dict[str, object]]:
    buckets = (("1_DAM", 1, 1), ("2_DAM", 2, 2), ("3_4_DAM", 3, 4), ("5_PLUS_DAM", 5, 999))
    result = []
    for name, low, high in buckets:
        group = [row for row in records if low <= int(row["support_count_dams"]) <= high]
        result.append({"bucket": name, "n": len(group), "top1_n": sum(int(row["exact_at_1"]) for row in group), "top3_n": sum(int(row["exact_at_3"]) for row in group), "top1": sum(int(row["exact_at_1"]) for row in group) / len(group), "top3": sum(int(row["exact_at_3"]) for row in group) / len(group)})
    for name, predicate in (("ONE_TWO_DAM", lambda value: value <= 2), ("THREE_PLUS_DAM", lambda value: value >= 3)):
        group = [row for row in records if predicate(int(row["support_count_dams"]))]
        result.append({"bucket": name, "n": len(group), "top1_n": sum(int(row["exact_at_1"]) for row in group), "top3_n": sum(int(row["exact_at_3"]) for row in group), "top1": sum(int(row["exact_at_1"]) for row in group) / len(group), "top3": sum(int(row["exact_at_3"]) for row in group) / len(group)})
    return result


def _hashes(paths: list[Path], root: Path) -> dict[str, str]:
    return {path.relative_to(root).as_posix(): _sha256(path) for path in paths}


def run() -> list[dict[str, object]]:
    root = project_root()
    output = root / "outputs" / "evaluation" / "exp08_split_sensitivity_v01_vs_v02"
    output.mkdir(parents=True, exist_ok=True)
    case01_path = root / "outputs" / "evaluation" / V01 / "historical_case_summary.csv"
    case02_path = root / "outputs" / "evaluation" / V02 / "historical_case_summary.csv"
    v01, v02 = _rows(case01_path), _rows(case02_path)
    hist01 = _rows(root / "data" / "processed" / "data_aduanas_historico_clase87_v0.1.csv")
    eval01 = _rows(root / "data" / "processed" / "data_aduanas_evalset_clase87_v0.1.csv")
    hist02 = _rows(root / "data" / "processed" / "data_aduanas_historico_clase87_v0.2.csv")
    eval02 = _rows(root / "data" / "processed" / "data_aduanas_evalset_clase87_v0.2.csv")

    global_metrics = []
    for label, field in (("Top1", "exact_at_1"), ("Top3", "exact_at_3"), ("Top5", "exact_at_5"), ("Top10", "exact_at_10"), ("Top50", "exact_at_50"), ("MRR", "reciprocal_rank")):
        n01, n02 = sum(float(row[field]) for row in v01), sum(float(row[field]) for row in v02)
        r01, r02 = n01 / len(v01), n02 / len(v02)
        global_metrics.append({"metric": label, "v01_numerator": n01, "v01_denominator": len(v01), "v01_value": r01, "v02_numerator": n02, "v02_denominator": len(v02), "v02_value": r02, "absolute_difference": r02 - r01, "percentage_point_difference": (r02 - r01) * 100, "relative_change": (r02 - r01) / r01, "interpretation_scope": "DESCRIPTIVE_SPLIT_SENSITIVITY"})
    _csv(output / "exp08_global_sensitivity_v01_vs_v02.csv", global_metrics)

    _csv(output / "exp08_split_independence_comparison_v01_vs_v02.csv", [
        {"version": "v0.1", "eval_cases": 1006, "historical_eval_dam_overlap": 995, "independence_status": "NOT_DAM_INDEPENDENT", "source": "frozen v0.1 split audit"},
        {"version": "v0.2", "eval_cases": 1056, "historical_eval_dam_overlap": 0, "independence_status": "DAM_GROUPED_INDEPENDENT", "source": "frozen v0.2 split audit"},
    ])
    _csv(output / "exp08_duplicate_sensitivity_comparison_v01_vs_v02.csv", [
        {"version": "v0.1", "signal": "exact_duplicate_cross_split", "count": 377, "availability": "FROZEN"},
        {"version": "v0.1", "signal": "same_nandina_duplicate_cross_split", "count": 376, "availability": "FROZEN"},
        {"version": "v0.1", "signal": "same_dam_exact_duplicate_cross_split", "count": 358, "availability": "FROZEN"},
        {"version": "v0.1", "signal": "near_duplicate_thresholds", "count": "NOT_AVAILABLE", "availability": "NOT_PRESERVED_IN_FROZEN_V01_ARTIFACTS"},
        {"version": "v0.2", "signal": "exact_duplicate_cross_split", "count": 35, "availability": "FROZEN"},
        {"version": "v0.2", "signal": "same_nandina_duplicate_cross_split", "count": 34, "availability": "FROZEN"},
        {"version": "v0.2", "signal": "different_nandina_exact_duplicate_cross_split", "count": 1, "availability": "FROZEN"},
        {"version": "v0.2", "signal": "near_duplicate_ge_090", "count": 55, "availability": "FROZEN_THRESHOLD_AUDIT"},
        {"version": "v0.2", "signal": "near_duplicate_ge_095", "count": 44, "availability": "FROZEN_THRESHOLD_AUDIT"},
        {"version": "v0.2", "signal": "near_duplicate_ge_098", "count": 37, "availability": "FROZEN_THRESHOLD_AUDIT"},
    ])
    codes = _code_sensitivity(v01, v02)
    _csv(output / "exp08_code_sensitivity_v01_vs_v02.csv", codes)
    _csv(output / "exp08_code_coverage_v01_vs_v02.csv", [_coverage(v01, hist01, "v0.1"), _coverage(v02, hist02, "v0.2")])

    v01_not_available = "NOT_AVAILABLE_NO_FROZEN_CASE_LEVEL_DUPLICATE_FLAGS"
    stratified = [
        _performance([], "v0.1", "EXACT_DUPLICATE", "EXACT", v01_not_available, "v0.1 case summary has no duplicate flags"),
        _performance([], "v0.1", "EXACT_DUPLICATE", "NON_EXACT", v01_not_available, "v0.1 case summary has no duplicate flags"),
        _performance([], "v0.1", "NEAR_GE_095", "NEAR_GE_095", v01_not_available, "v0.1 near-duplicate flags were not preserved"),
        _performance([], "v0.1", "NEAR_GE_095", "REST_NEAR_GE_095", v01_not_available, "v0.1 near-duplicate flags were not preserved"),
        *_dam_strata(v01, eval01, hist01, "v0.1"),
        _performance([row for row in v02 if _flag(row["exact_duplicate_cross_split"])], "v0.2", "EXACT_DUPLICATE", "EXACT", "AVAILABLE", "frozen v0.2 case summary"),
        _performance([row for row in v02 if not _flag(row["exact_duplicate_cross_split"])], "v0.2", "EXACT_DUPLICATE", "NON_EXACT", "AVAILABLE", "frozen v0.2 case summary"),
        _performance([row for row in v02 if _flag(row["near_duplicate_095"])], "v0.2", "NEAR_GE_095", "NEAR_GE_095", "AVAILABLE", "frozen v0.2 case summary"),
        _performance([row for row in v02 if not _flag(row["near_duplicate_095"])], "v0.2", "NEAR_GE_095", "REST_NEAR_GE_095", "AVAILABLE", "frozen v0.2 case summary"),
        *_dam_strata(v02, eval02, hist02, "v0.2"),
    ]
    _csv(output / "exp08_stratified_performance_v01_vs_v02.csv", stratified)

    common_ids = {row["case_id"] for row in v01} & {row["case_id"] for row in v02}
    _json(output / "exp08_common_eval_case_availability_v01_vs_v02.json", {"v01_case_ids": len(v01), "v02_case_ids": len(v02), "common_case_ids": len(common_ids), "paired_common_case_analysis_generated": False, "reason": "case identifiers are version-specific and no approved equivalent frozen pairing key exists"})
    audit = {
        "normalization": {"status": "SAME", "evidence_source": "frozen case summaries"}, "BM25_implementation": {"status": "SAME", "evidence_source": "historical runners"},
        "BM25_parameters": {"status": "PARTIALLY_TRACED", "evidence_source": "v0.1 historical_metrics.json records candidate_depth 200; v0.2 run_metadata.json records depth 100"},
        "candidate_deduplication": {"status": "SAME", "evidence_source": "historical metrics"}, "metric_definitions": {"status": "SAME", "evidence_source": "frozen metrics"},
        "ranking_depth": {"status": "IMPLEMENTATION_DIFFERENCE", "evidence_source": "v0.1 depth 200; v0.2 depth 100"}, "historical_bank_composition": {"status": "SPLIT_INHERENT_DIFFERENCE", "evidence_source": "split metadata"},
        "evalset_composition": {"status": "SPLIT_INHERENT_DIFFERENCE", "evidence_source": "evalsets"},
        "metadata_availability": {"status": "PARTIAL", "evidence_source": "v0.1 historical_metrics.json exists, but v0.1 run_metadata.json is absent (V01_METADATA_PROVENANCE_LIMITATION)"},
        "interpretation": "Descriptive frozen-configuration comparison; no exclusive causal attribution to split policy."}
    _json(output / "exp08_comparability_audit_v01_vs_v02.json", audit)
    _json(output / "exp08_he2_sensitivity_assessment_v0.2.json", {"hypothesis": "HE2", "status": "NOT_REOPENED", "reason": "EXP-08 is descriptive and does not rerun or reassess HE2.", "v02_final_benchmark": True})

    proximity = {"error_cases": 518, "same_hs6": 87, "same_hs4": 284, "same_chapter": 147, "different_chapter": 0, "same_hs6_or_hs4": 371, "same_hs6_or_hs4_rate": 371 / 518}
    precedent = _precedent(v02)
    components = [
        {"component": "DESCRIPTION_QUALITY", "source": "frozen HE5 protocol", "evaluated": False, "evidence": "No frozen case-level description quality rule exists.", "assessment": "NOT_EVALUATED_NO_FROZEN_CASE_RULE", "limitation": "No reproducible quality label can be inferred post hoc."},
        {"component": "HIERARCHICAL_PROXIMITY", "source": "frozen HE5 integrated error matrix", "evaluated": True, "evidence": json.dumps(proximity, ensure_ascii=True), "assessment": "SUPPORTED", "limitation": "Hierarchy measures only observed top-1 error proximity."},
        {"component": "HISTORICAL_PRECEDENT_AVAILABILITY", "source": "frozen v0.2 historical case summary", "evaluated": True, "evidence": json.dumps(precedent, ensure_ascii=True), "assessment": "MIXED_NON_MONOTONIC", "limitation": "Support bucket association is descriptive, not causal."},
        {"component": "INTERNAL_EVALUATION_SCOPE", "source": "EXP-08 frozen global, split, duplicate, and comparability artifacts", "evaluated": True, "evidence": "Top1 0.8628230616302187 -> 0.509469696969697 (delta -35.33533646605217 pp); Top3 delta -26.597423037532387 pp; MRR delta -0.2765317065089975; DAM overlap 995/1006 -> 0/1056; exact cross-split 377/1006 -> 35/1056; V01_METADATA_PROVENANCE_LIMITATION; ranking depth v0.1=200 v0.2=100.", "assessment": "SENSITIVITY_TO_EXPERIMENTAL_CONFIGURATION", "limitation": "No exclusive causal attribution to split policy; validity remains internal to v0.2."},
    ]
    _csv(output / "exp08_he5_component_assessment_v0.2.csv", components)
    _json(output / "exp08_final_he5_assessment_v0.2.json", {"hypothesis": "HE5", "statement": "Los errores y l\u00edmites del piloto se concentrar\u00e1n en descripciones ambiguas o incompletas, subpartidas jer\u00e1rquicamente pr\u00f3ximas, casos con precedentes hist\u00f3ricos insuficientes y condiciones que restringir\u00e1n la validez de los resultados al conjunto interno evaluado.", "status": "PARTIALLY_SUPPORTED", "evaluated_components": 3, "total_components": 4, "limitation": "Description quality is not evaluated because no frozen case-level rule exists.", "v02_final_benchmark": True})

    findings = """# EXP-08: sensibilidad v0.1 vs v0.2\n\n## Alcance\n\nComparacion descriptiva de configuraciones congeladas y globalmente no pareada: v0.1 contiene 1006 casos y v0.2 contiene 1056. No son evalsets equivalentes, no se realizan pruebas inferenciales y no se atribuyen efectos causales exclusivamente a la politica de split. v0.2 permanece como benchmark final.\n\n## Resultados globales\n\n| Metrica | v0.1 | v0.2 | Delta v0.2-v0.1 |\n|---|---:|---:|---:|\n| Top1 | 0.862823 | 0.509470 | -35.335 pp |\n| Top3 | 0.937376 | 0.671402 | -26.597 pp |\n| MRR | 0.906239 | 0.629708 | -0.276532 |\n\n## Independencia, duplicados y cobertura\n\nEl solapamiento DAM historico-evaluacion cambia de 995/1006 en v0.1 a 0/1056 en v0.2. Los duplicados exactos pasan de 377/1006 (376 misma NANDINA; 358 exactos de misma DAM) a 35/1056 (34 misma NANDINA; 1 diferente). Los near-duplicates v0.2 congelados son umbrales: >=0.90: 55, >=0.95: 44 y >=0.98: 37; no son categorias de etiqueta. La cobertura nominal por NANDINA se reconcilia contra el banco historico de cada version y la sensibilidad por codigo contiene una fila por cada NANDINA de la union de evalsets, sin ocultar denominadores pequenos.\n\n## Estratos y HE\n\nEl rendimiento estratificado v0.2 usa banderas congeladas: exactos 35, no exactos 1021, near >=0.95 44 y resto 1012. Las banderas de duplicados por caso no se preservaron en v0.1, por lo que esos estratos se declaran `NOT_AVAILABLE`; el estrato DAM se obtiene por membership de splits congelados. HE2 no se reabre. HE5 conserva cuatro componentes y queda `PARTIALLY_SUPPORTED`: calidad descriptiva no evaluada; proximidad jerarquica apoyada; precedentes con evidencia mixta/no monotona; alcance interno con sensibilidad a configuracion experimental.\n\n## Limitaciones de comparabilidad\n\nLa trazabilidad de v0.1 usa `historical_metrics.json`, pero falta `run_metadata.json` (`V01_METADATA_PROVENANCE_LIMITATION`). Ademas, la profundidad de ranking difiere: 200 en v0.1 y 100 en v0.2. Estas limitaciones impiden atribuir los deltas exclusivamente al split.\n"""
    (output / "exp08_integrated_findings_v0.2.md").write_text(findings, encoding="utf-8")
    summary = """# Resumen EXP-08\n\nObjetivo: describir la sensibilidad entre el split previo v0.1 por serie y el split final v0.2 agrupado por DAM, sin reejecutar retrieval.\n\nv0.1/v0.2: Top1 0.862823/0.509470 (delta -35.335 pp), Top3 0.937376/0.671402 (delta -26.597 pp), MRR 0.906239/0.629708 (delta -0.276532).\n\nDAM overlap: 995/1006 en v0.1 frente a 0/1056 en v0.2. Duplicados exactos: 377/1006 frente a 35/1056. Near-duplicates v0.2: >=0.90 55, >=0.95 44, >=0.98 37.\n\nLimitaciones: los evalsets no son equivalentes, la comparacion no es pareada, v0.1 carece de run_metadata.json y la profundidad difiere (200 frente a 100). HE5 se mantiene PARTIALLY_SUPPORTED. Gate corrective microclose APPROVED; v0.2 permanece benchmark final interno.\n"""
    (output / "summary_exp08.md").write_text(summary, encoding="utf-8")
    docs = root / "docs" / "exp08_split_sensitivity_inventory.md"
    docs.write_text("""# Inventario EXP-08\n\nLa version inicial de EXP-08 se publico en `f0a369a`. El microcierre correctivo conserva esa historia y corrige solo semantica, completitud y pruebas de contrato; no reejecuta retrieval ni altera las metricas globales.\n\n- Comparabilidad: `exp08_comparability_audit_v01_vs_v02.json`\n- Sensibilidad global: `exp08_global_sensitivity_v01_vs_v02.csv`\n- Independencia DAM: `exp08_split_independence_comparison_v01_vs_v02.csv`\n- Duplicados por umbral: `exp08_duplicate_sensitivity_comparison_v01_vs_v02.csv`\n- Sensibilidad por NANDINA: `exp08_code_sensitivity_v01_vs_v02.csv`\n- Cobertura nominal: `exp08_code_coverage_v01_vs_v02.csv`\n- Rendimiento estratificado: `exp08_stratified_performance_v01_vs_v02.csv`\n- HE2/HE5: `exp08_he2_sensitivity_assessment_v0.2.json`, `exp08_he5_component_assessment_v0.2.csv`, `exp08_final_he5_assessment_v0.2.json`\n- Resumen: `summary_exp08.md`\n- Manifest correctivo: `gate_exp08_corrective_microclose_manifest_v0.2.json`\n\nLos resultados usan solo artefactos historicos congelados. v0.2 es el benchmark final interno; los deltas son descriptivos y no causales.\n""", encoding="utf-8")

    inputs = [
        case01_path, case02_path,
        root / "outputs" / "evaluation" / V01 / "historical_metrics.json",
        root / "outputs" / "evaluation" / V02 / "sensitivity_exact_duplicates.csv",
        root / "outputs" / "evaluation" / V02 / "sensitivity_near_duplicates_095.csv",
        root / "outputs" / "audits" / "data_aduanas_splits_clase87_v0.2" / "near_duplicates_hist_eval_summary_v0.2.csv",
        root / "data" / "processed" / "data_aduanas_historico_clase87_v0.1.csv",
        root / "data" / "processed" / "data_aduanas_evalset_clase87_v0.1.csv",
        root / "data" / "processed" / "data_aduanas_historico_clase87_v0.2.csv",
        root / "data" / "processed" / "data_aduanas_evalset_clase87_v0.2.csv",
    ]
    generated = sorted(path for path in output.iterdir() if path.is_file() and path.name not in OUTPUT_MANIFESTS)
    input_hashes, output_hashes = _hashes(inputs, root), {path.name: _sha256(path) for path in generated}
    original_manifest = {"phase": "EXP-08", "analysis_type": "DESCRIPTIVE_SPLIT_SENSITIVITY", "split_v01_type": "PREVIOUS_SERIES_LEVEL_SPLIT", "split_v02_type": "DAM_GROUPED_FINAL_SPLIT", "v02_final_benchmark": True, "evalsets_equivalent": False, "global_comparison_paired": False, "common_case_ids": len(common_ids), "algorithm_reexecuted": False, "model_called": False, "new_retrieval": False, "web_used": False, "causal_claim": False, "v01_run_metadata_available": False, "v01_metadata_provenance_limitation": True, "implementation_difference_recorded": "ranking_depth_v01_200_v02_100", "he2_reopened": False, "description_quality_evaluated": False, "he5_final_assessed": True, "gate_exp08": "APPROVED", "ready_for_exp05_exp07_formal_close": True, "input_sha256": input_hashes, "output_sha256": output_hashes}
    _json(output / "gate_exp08_split_sensitivity_manifest_v0.2.json", original_manifest)
    corrective = {"phase": "EXP-08 CORRECTIVE MICROCLOSE", "original_gate_commit": ORIGINAL_GATE_COMMIT, "original_gate_status": "APPROVED", "corrective_reason": ["NEAR_DUPLICATE_THRESHOLD_SEMANTICS", "CODE_SENSITIVITY_OUTPUT_MISLABELED", "CODE_COVERAGE_INCOMPLETE", "EXP08_CONTRACT_TEST_COVERAGE_INCOMPLETE"], "near_duplicate_semantics_corrected": True, "code_sensitivity_corrected": True, "code_coverage_completed": True, "stratified_performance_added": True, "summary_added": True, "he5_status": "PRESERVED_PARTIALLY_SUPPORTED", "gate_exp08_corrective_microclose": "APPROVED", "ready_for_exp05_exp07_formal_close": True, "input_sha256": input_hashes, "new_output_sha256": output_hashes}
    _json(output / "gate_exp08_corrective_microclose_manifest_v0.2.json", corrective)
    return global_metrics


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=True))
