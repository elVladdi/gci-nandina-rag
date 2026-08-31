from __future__ import annotations

"""Build the EXP-10/HE5 matrix strictly from frozen v0.2 artifacts."""

import csv
import hashlib
import json
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from ..utils.paths import ensure_parent, project_root

OUT = Path("outputs/evaluation/he5_integrated_error_analysis_v0.2")
EVAL_SHA = "3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def indexed(path: Path) -> dict[str, dict[str, str]]:
    return {row["case_id"]: row for row in csv_rows(path)}


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)


def write_json(path: Path, data: dict) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def flag(value: str) -> int:
    return int(value in {"1", "True", "true", "SI", "yes"})


def rate(n: int, d: int) -> float:
    return round(n / d, 6) if d else 0.0


def run() -> dict:
    root = project_root(); out = root / OUT
    paths = {
        "evalset": root / "data/processed/data_aduanas_evalset_clase87_v0.2.csv",
        "historical": root / "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_case_summary.csv",
        "flat": root / "outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv",
        "hierarchical": root / "outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv",
        "dense": root / "outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_case_summary.csv",
        "pools": root / "outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/candidate_pool_case_summary.csv",
        "integration": root / "outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_case_summary.csv",
        "reranker": root / "outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_case_results_v0.2.csv",
        "he4_j": root / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_automatic_validation_case_results_v0.2.csv",
        "he4_k": root / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_case_scores_v0.2.csv",
        "he4_sample": root / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_explainer_sample_v0.2.csv",
        "k_manifest": root / "outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_k_qualitative_evaluation_manifest_v0.2.json",
        "a_metrics": root / "outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json",
    }
    if sha(paths["evalset"]) != EVAL_SHA: raise RuntimeError("Frozen evalset hash mismatch")
    evals = csv_rows(paths["evalset"]); ids = [r["case_id"] for r in evals]
    if len(evals) != 1056 or len(set(ids)) != 1056: raise RuntimeError("Expected 1056 unique frozen evaluation cases")
    hist, flat, hier, dense, integ, rerank, he4j, he4k, he4sample = (indexed(paths[k]) for k in ("historical", "flat", "hierarchical", "dense", "integration", "reranker", "he4_j", "he4_k", "he4_sample"))
    pools = {(r["case_id"],r["pool_id"],r["depth"]): r for r in csv_rows(paths["pools"])}
    matrix, events = [], []
    def event(cid: str, typ: str, family: str, source: str, klass: str) -> None: events.append({"case_id":cid,"error_type":typ,"error_family":family,"evidence_source":source,"pre_specification_class":klass})
    for e in evals:
        cid=e["case_id"]; h,f,c,d,i=hist[cid],flat[cid],hier[cid],dense[cid],integ[cid]; j,k,rr,s=he4j.get(cid),he4k.get(cid),rerank.get(cid),he4sample.get(cid)
        r={"case_id":cid,"id_unico":e["id_unico"],"DAM":e["1.1. ADUANA"],"SERIE":e["SERIE"],"reference_nandina":e["NANDINA"],"support_count_series":h["support_count_series"],"support_count_dams":h["support_count_dams"],"support_bucket_dams":h["support_bucket_dams"],"historical_reference_rank":h["exact_rank"],"historical_top1_correct":h["exact_at_1"],"historical_top3_correct":h["exact_at_3"],"historical_top5_correct":h["exact_at_5"],"historical_top10_correct":h["exact_at_10"],"historical_top50_recovered":h["exact_at_50"],"historical_mrr_contribution":h["reciprocal_rank"],"historical_top1_code":h["top1_nandina"],"historical_candidate_count_effective":h["unique_candidates"],"historical_error_hierarchy":"EXACT_NANDINA8" if flag(h["exact_at_1"]) else {"same_sub_partida_6d":"SAME_HS6","same_partida_4d":"SAME_HS4","same_chapter_2d":"SAME_CHAPTER"}.get(h["top1_error_family"],"DIFFERENT_CHAPTER"),"exact_normalized_description_in_history":h["exact_duplicate_cross_split"],"exact_duplicate_same_label":h["exact_duplicate_same_nandina"],"exact_duplicate_different_label":h["exact_duplicate_different_nandina"],"near_duplicate_similarity":h["near_duplicate_095_max_jaccard"],"near_ge_095":h["near_duplicate_095"]}
        for p,prefix in ((f,"flat"),(c,"hierarchical"),(d,"dense")):
            r.update({f"{prefix}_exact_rank":p["rank_ref"],f"{prefix}_top1":p["hit_top_1"],f"{prefix}_top3":p["hit_top_3"],f"{prefix}_top5":p["hit_top_5"],f"{prefix}_top10":p["hit_top_10"],f"{prefix}_top50":p["hit_top_50"],f"{prefix}_recall100":p["hit_recall_100"],f"{prefix}_recall200":p.get("hit_recall_200","")})
        for pool,name in (("hierarchical_only","hierarchical_pool"),("dual_only","dual_pool"),("hierarchical_70_dual_backfill_30","pool_70_30")):
            r[f"{name}_contains_reference_100"]=pools[(cid,pool,"100")]["exact_at_depth"]; r[f"{name}_contains_reference_200"]=pools[(cid,pool,"200")]["exact_at_depth"]
        r.update({"integration_top3_available":1,"exact_normative_evidence_all_top3":i["top3_has_exact_evidence"],"historical_precedent_all_top3":i["precedent_coverage_candidates"],"traceability_complete":i["traceability_complete_candidates"],"reranker_evaluated":int(rr is not None),"reranker_reference_in_pool":"" if rr is None else int(rr["outcome"]!="REFERENCE_ABSENT"),"reranker_before_rank":"" if rr is None else rr["reference_rank_before"],"reranker_after_rank":"" if rr is None else rr["reference_rank_after"],"reranker_outcome":"NOT_EVALUATED" if rr is None else rr["outcome"],"he4_evaluated":int(k is not None),"he4_selection_bucket":"" if s is None else s["selection_target"],"he4_automatic_available":int(j is not None),"he4_qualitative_available":int(k is not None)})
        for old,new in (("candidate_set_exact","he4_candidate_set_exact"),("top3_order_preserved","he4_top3_order_preserved"),("historical_reference_valid","he4_historical_reference_valid"),("normative_reference_valid","he4_normative_reference_valid"),("generic_normative_warning_when_required","he4_generic_normative_warning_pass"),("traceability_complete","he4_traceability_complete")): r[new]="" if j is None else j[old]
        for old,new in (("recomputed_total_score","he4_total_score"),("recomputed_auditable","he4_auditable"),("trazabilidad_score","he4_trazabilidad"),("verificabilidad_score","he4_verificabilidad"),("separacion_historico_normativo_score","he4_separacion_historico_normativo"),("prudencia_de_la_conclusion_score","he4_prudencia"),("consistencia_con_top3_fijo_score","he4_consistencia_top3"),("deteccion_de_evidencia_normativa_generica_score","he4_deteccion_normativa_generica"),("comparacion_entre_candidatos_score","he4_comparacion"),("utilidad_para_auditoria_humana_score","he4_utilidad_auditoria"),("hard_violation","he4_hard_violation")): r[new]="" if k is None else k[old]
        if not flag(r["historical_top1_correct"]): event(cid,"HISTORICAL_TOP1_ERROR","HISTORICAL_RETRIEVAL","A","PRE_SPECIFIED")
        if not flag(r["historical_top3_correct"]): event(cid,"HISTORICAL_TOP3_MISS","HISTORICAL_RETRIEVAL","A","PRE_SPECIFIED")
        if r["support_bucket_dams"]=="A. 1 DAM historica": event(cid,"LOW_INDEPENDENT_DAM_SUPPORT","SUPPORT_AND_DEPENDENCE","A","PRE_SPECIFIED")
        if flag(r["exact_normalized_description_in_history"]): event(cid,"EXACT_DUPLICATE_PRESENT","DUPLICATE_SENSITIVITY","split audit","PRE_SPECIFIED")
        if flag(r["near_ge_095"]): event(cid,"NEAR_DUPLICATE_PRESENT","DUPLICATE_SENSITIVITY","split audit","PRE_SPECIFIED")
        if not flag(r["flat_top10"]): event(cid,"NORMATIVE_EARLY_RANK_MISS","NORMATIVE_RETRIEVAL","B","TECHNICAL_DERIVED")
        if flag(r["hierarchical_recall200"]) and not flag(r["hierarchical_top50"]): event(cid,"NORMATIVE_DEEP_ONLY_RECOVERY","NORMATIVE_RETRIEVAL","C","TECHNICAL_DERIVED")
        if not flag(r["hierarchical_recall200"]): event(cid,"NORMATIVE_NOT_RECOVERED","NORMATIVE_RETRIEVAL","C","TECHNICAL_DERIVED")
        if not flag(r["dense_recall200"]): event(cid,"DENSE_MISS","NORMATIVE_RETRIEVAL","D1a","TECHNICAL_DERIVED")
        if not flag(r["hierarchical_pool_contains_reference_200"]): event(cid,"POOL_REFERENCE_MISS","NORMATIVE_RETRIEVAL","E","TECHNICAL_DERIVED")
        if r["historical_error_hierarchy"] in {"SAME_HS6","SAME_HS4","SAME_CHAPTER"}: event(cid,"HIERARCHICAL_"+r["historical_error_hierarchy"]+"_ERROR","HISTORICAL_RETRIEVAL","A","PRE_SPECIFIED")
        if j and not flag(j["generic_normative_warning_when_required"]): event(cid,"GENERIC_NORMATIVE_WARNING_MISS","EXPLANATION_AUDITABILITY","J","TECHNICAL_DERIVED")
        if k and int(k["verificabilidad_score"])<2: event(cid,"HE4_LOW_VERIFIABILITY","EXPLANATION_AUDITABILITY","K","TECHNICAL_DERIVED")
        if k and int(k["separacion_historico_normativo_score"])<2: event(cid,"HE4_HISTORICAL_NORMATIVE_SEPARATION_WEAK","EXPLANATION_AUDITABILITY","K","TECHNICAL_DERIVED")
        if k and k["recomputed_auditable"]!="SI": event(cid,"HE4_NOT_AUDITABLE","EXPLANATION_AUDITABILITY","K","TECHNICAL_DERIVED")
        mine=[x["error_type"] for x in events if x["case_id"]==cid]; r["error_types"]="|".join(mine); r["error_count"]=len(mine); matrix.append(r)
    write_csv(out/"he5_integrated_error_matrix_v0.2.csv",matrix,list(matrix[0])); write_csv(out/"he5_error_events_v0.2.csv",events,list(events[0]))
    def grouped(field):
        g=defaultdict(list)
        for r in matrix:g[r[field]].append(r)
        return [{"group":field,"value":key,"cases":len(v),"top1_numerator":sum(flag(x["historical_top1_correct"]) for x in v),"top1_rate":rate(sum(flag(x["historical_top1_correct"]) for x in v),len(v)),"top3_numerator":sum(flag(x["historical_top3_correct"]) for x in v),"top3_rate":rate(sum(flag(x["historical_top3_correct"]) for x in v),len(v)),"mean_reciprocal_rank":round(statistics.mean(float(x["historical_mrr_contribution"]) for x in v),6)} for key,v in sorted(g.items())]
    support=grouped("support_bucket_dams"); duplicates=grouped("exact_normalized_description_in_history")+grouped("near_ge_095"); hierarchy=[{"historical_error_hierarchy":k,"errors":v} for k,v in sorted(Counter(r["historical_error_hierarchy"] for r in matrix if r["historical_error_hierarchy"]!="EXACT_NANDINA8").items())]
    normative=[{"component":name,"top1":sum(flag(r[key]) for r in matrix),"top10":sum(flag(r[key10]) for r in matrix),"recall200":sum(flag(r[key200]) for r in matrix)} for name,key,key10,key200 in (("flat","flat_top1","flat_top10","flat_recall100"),("hierarchical","hierarchical_top1","hierarchical_top10","hierarchical_recall200"),("dense_d1a","dense_top1","dense_top10","dense_recall200"))]
    cross=Counter((r["historical_top3_correct"],r["hierarchical_recall200"]) for r in matrix); crossrows=[{"historical_top3_correct":a,"hierarchical_reference_recovered_200":b,"cases":n} for (a,b),n in sorted(cross.items())]
    coverage=[{"component":"historical_A","eligible_cases":1056,"evaluated_cases":1056,"coverage_rate":1.0,"reason_not_full_coverage":""},{"component":"normative_B_C_D1a_E_F","eligible_cases":1056,"evaluated_cases":1056,"coverage_rate":1.0,"reason_not_full_coverage":""},{"component":"reranker_G","eligible_cases":1056,"evaluated_cases":sum(r["reranker_evaluated"] for r in matrix),"coverage_rate":rate(sum(r["reranker_evaluated"] for r in matrix),1056),"reason_not_full_coverage":"diagnostic sample"},{"component":"HE4_J_K","eligible_cases":1056,"evaluated_cases":sum(r["he4_evaluated"] for r in matrix),"coverage_rate":rate(sum(r["he4_evaluated"] for r in matrix),1056),"reason_not_full_coverage":"frozen HE4 sample"}]
    for name,rows,fields in (("he5_historical_errors_by_support_v0.2.csv",support,list(support[0])),("he5_historical_hierarchy_errors_v0.2.csv",hierarchy,["historical_error_hierarchy","errors"]),("he5_duplicate_sensitivity_v0.2.csv",duplicates,list(duplicates[0])),("he5_normative_failure_analysis_v0.2.csv",normative,list(normative[0])),("he5_historical_vs_normative_v0.2.csv",crossrows,list(crossrows[0])),("he5_component_coverage_v0.2.csv",coverage,list(coverage[0]))): write_csv(out/name,rows,fields)
    taxonomy={"classification":{"PRE_SPECIFIED":"historical retrieval, support and duplicate sensitivity","TECHNICAL_DERIVED":"frozen-output integration without new retrieval","EXPLORATORY":"critical-case combinations; not used for HE5 confirmation"},"families":sorted({e["error_family"] for e in events}),"global_protocol_limitations":["PROMPT_SCHEMA_SPECIFICATION_MISMATCH","EVALUATOR_MODALITY_DEVIATION"]}; write_json(out/"he5_error_taxonomy_v0.2.json",taxonomy)
    am=json.loads(paths["a_metrics"].read_text(encoding="utf-8"))["metrics"]; (out/"he5_integrated_findings_v0.2.md").write_text(f"# EXP-04 Fase L / EXP-10\n\n- Matriz: 1056 casos unicos del evalset v0.2.\n- A: Top-1 {am['exact_at_1_numerator']}/1056, Top-3 {am['exact_at_3_numerator']}/1056, MRR {am['mrr']:.6f}.\n- HE5: NOT EVALUABLE; no se encontro formulacion literal versionada de OE5/HE5.\n- Sensibilidades de soporte/duplicados: preespecificadas; integracion B-K: tecnica; casos multi-senal: exploratorios.\n- Limitaciones separadas: PROMPT_SCHEMA_SPECIFICATION_MISMATCH y EVALUATOR_MODALITY_DEVIATION.\n",encoding="utf-8",newline="\n")
    (out/"he5_integrated_error_matrix_dictionary_v0.2.md").write_text("# Diccionario HE5\n\nUna fila por `case_id`. Los campos de G y HE4 son nulos fuera de sus muestras; no se imputan como fallos. `reference_nandina` se usa solo para evaluacion. Aporta A: `historical_*`; B-D: recuperacion normativa; E: pools; F: evidencia; G: reranker; H-K: HE4. `error_types` usa `|`; los eventos son PRE_SPECIFIED, TECHNICAL_DERIVED o EXPLORATORY.\n",encoding="utf-8",newline="\n")
    write_json(out/"he5_hypothesis_assessment_v0.2.json",{"oe5":"NOT EVALUABLE: no formulacion literal versionada localizada","he5":"NOT EVALUABLE: no formulacion literal versionada localizada","preserved":{"HE2":"PARTIALLY SUPPORTED","HE3":"SUPPORTED","HE4":"PARTIALLY SUPPORTED"},"gate_l":"APPROVED","ready_for_exp08":True,"not_project_complete":True})
    outputs={p.name:sha(p) for p in out.iterdir() if p.is_file()}; manifest={"phase":"EXP-04 L / EXP-10","gate_l":"APPROVED","ready_for_exp08":True,"label_used_for_evaluation":True,"label_exposed_to_generation":False,"no_model_call":True,"no_new_retrieval":True,"no_web":True,"inputs_sha256":{k:sha(v) for k,v in paths.items()},"outputs_sha256":outputs,"created_at_utc":datetime.now(timezone.utc).isoformat()}; write_json(out/"gate_l_integrated_error_analysis_manifest_v0.2.json",manifest); (out/"summary_phase_l.md").write_text("# Phase L\n\nGate L APPROVED. HE5 remains NOT EVALUABLE because its source formulation is absent; EXP-08 was not executed.\n",encoding="utf-8",newline="\n")
    return manifest

if __name__ == "__main__": print(json.dumps({"gate_l":run()["gate_l"]}))
