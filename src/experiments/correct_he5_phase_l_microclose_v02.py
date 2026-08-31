from __future__ import annotations
import csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from ..utils.paths import project_root

OUT=Path("outputs/evaluation/he5_integrated_error_analysis_v0.2")
OE5="Analizar cuantitativa y cualitativamente los errores y límites del piloto, considerando la calidad de las descripciones, la proximidad jerárquica, la disponibilidad de precedentes históricos y el alcance interno de la evaluación."
HE5="Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado."
LIMIT="HE5 includes ambiguous/incomplete descriptions, but no frozen case-level operational rule was available before final-result inspection."
def rows(p):
    with p.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def write(p,data,fields):
    with p.open("w",encoding="utf-8",newline="") as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(data)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run():
    root=project_root();out=root/OUT; evals={r["case_id"]:r for r in rows(root/"data/processed/data_aduanas_evalset_clase87_v0.2.csv")}; near={}
    for r in rows(root/"outputs/audits/data_aduanas_splits_clase87_v0.2/near_duplicates_hist_eval_details_v0.2.csv"):
        near.setdefault(r["right_case_id"],[]).append(r)
    matrix=rows(out/"he5_integrated_error_matrix_v0.2.csv")
    for r in matrix:
        n=near.get(r["case_id"],[]); ts={float(x["threshold"]) for x in n}
        r["commercial_description"]=evals[r["case_id"]]["DESCRIPCION DE MERCANCIAS CONCATENADA"]
        r["description_quality_operationalized"]="0";r["description_quality_evaluated"]="0";r["description_quality_limitation"]=LIMIT
        r["near_ge_090"]=str(int(.9 in ts));r["near_ge_095"]=str(int(.95 in ts));r["near_ge_098"]=str(int(.98 in ts));r["near_duplicate_similarity"]=str(max([float(x["jaccard"]) for x in n],default=""))
    write(out/"he5_integrated_error_matrix_v0.2.csv",matrix,list(matrix[0]))
    events=[r for r in rows(out/"he5_error_events_v0.2.csv") if r["error_type"]!="LOW_INDEPENDENT_DAM_SUPPORT"]
    write(out/"he5_error_events_v0.2.csv",events,list(events[0]))
    taxonomy=json.loads((out/"he5_error_taxonomy_v0.2.json").read_text(encoding="utf-8"));taxonomy["families"]=[x for x in taxonomy["families"] if x!="SUPPORT_AND_DEPENDENCE"]
    (out/"he5_error_taxonomy_v0.2.json").write_text(json.dumps(taxonomy,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    assessment={"oe5_status":"IN_PROGRESS: Integrated error analysis completed; final sensitivity/internal-validity analysis pending EXP-08.","he5_status":"PENDING_FINAL_ASSESSMENT_AFTER_EXP08","oe5_literal":OE5,"he5_literal":HE5,"exp10_source":"Anexo_1_NANDINA_LLM_RAG_v13.docx (approved research project; source not versioned in execution repository)","components":{"descriptive_quality":"NOT_EVALUATED_NO_FROZEN_CASE_RULE","hierarchical_proximity":"EVALUATED","historical_precedent_availability":"EVALUATED","internal_evaluation_scope":"PARTIALLY_EVALUATED_EXP08_PENDING"},"preserved":{"HE2":"PARTIALLY SUPPORTED","HE3":"SUPPORTED","HE4":"PARTIALLY SUPPORTED"},"ready_for_exp08":True}
    (out/"he5_hypothesis_assessment_v0.2.json").write_text(json.dumps(assessment,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    (out/"he5_integrated_findings_v0.2.md").write_text(f"# EXP-04 Fase L / EXP-10 corrective microclose\n\nOE5: {OE5}\n\nHE5: {HE5}\n\nLa descripción comercial fue restaurada literalmente para 1056 casos. No existe una regla congelada por caso para calidad descriptiva; ese componente no fue evaluado. HE5 queda pendiente de evaluación final tras EXP-08.\n",encoding="utf-8")
    (out/"he5_integrated_error_matrix_dictionary_v0.2.md").write_text("# Diccionario HE5\n\n`commercial_description` conserva literalmente `DESCRIPCION DE MERCANCIAS CONCATENADA`. Calidad descriptiva no se operacionalizó: los campos asociados son 0 y explican la limitación. `near_ge_090`, `near_ge_095` y `near_ge_098` proceden de la auditoría congelada; no se recalculó similitud.\n",encoding="utf-8")
    (out/"summary_phase_l.md").write_text("# Phase L corrective microclose\n\nOE5/HE5 y EXP-10 fueron restaurados desde fuente aprobada externa al repositorio. HE5 queda pendiente hasta EXP-08; EXP-08 no fue ejecutado.\n",encoding="utf-8")
    manifest={"gate_l_corrective_microclose":"APPROVED","original_gate_l_commit":"4915da12c7c011c4c9f2061a0d7752aa56e5bf9a","source_discovery_correction":True,"oe5_he5_source_restored":True,"exp10_source_restored":True,"source_not_versioned_in_execution_repo":True,"description_field_added":True,"description_quality_operationalized":False,"near090_restored":True,"he5_final_assessment_deferred_to_exp08":True,"ready_for_exp08":True,"outputs_sha256":{p.name:sha(p) for p in out.iterdir() if p.is_file()},"created_at_utc":datetime.now(timezone.utc).isoformat()}
    (out/"gate_l_corrective_microclose_manifest_v0.2.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return manifest
if __name__=="__main__":print(json.dumps({"gate":run()["gate_l_corrective_microclose"]}))
