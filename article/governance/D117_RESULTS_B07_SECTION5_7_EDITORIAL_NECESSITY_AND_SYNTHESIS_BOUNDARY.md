# D-117 — Results B07 / Section 5.7 editorial necessity and synthesis boundary

## Español

```text
DECISION = D-117
PHASE = RESULTS
BLOCK = RESULTS_B07_SECTION_5_7
SECTION = 5.7 SUMMARY BY RESEARCH QUESTION
EDITORIAL_DECISION = RETAIN_AND_DRAFT
RATIONALE = IMPROVES_READABILITY_WITHOUT_NEW_RESULTS
SOURCE_MASTER = article/manuscript/ARTICLE_MASTER_V022.md
SOURCE_MASTER_SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
SOURCE_MASTER_GIT_BLOB = 088eecd537997a3438517f7d206f6d890b0aa064
SOURCE_OF_TRUTH = INTEGRATED_RESULTS_5_1_TO_5_6_ONLY
NEW_EXPERIMENTAL_RESULTS = PROHIBITED
NEW_INFERENCE = PROHIBITED
NEW_CLAIMS = PROHIBITED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

La estructura congelada define §5.7 como una síntesis opcional por pregunta de investigación, que debe omitirse si resulta redundante. Tras integrar §5.1–§5.6, IA Gestora determina que una síntesis compacta mejora la legibilidad porque los cuatro RQ no se corresponden uno-a-uno con las seis subsecciones de Results: RQ1 combina evidencia descriptiva de §5.2 con la inferencia de §5.6; RQ2 se apoya principalmente en §5.3; RQ3 en §5.4; y RQ4 requiere integrar controles de §5.1, sensibilidad/robustez de §5.5 y los límites inferenciales de §5.6. Por ello, §5.7 se retiene, pero únicamente como síntesis compacta y no como una nueva capa de interpretación.

## Contenido permitido por RQ

### RQ1 — candidate retrieval

Puede sintetizarse que el historical BM25 H100 alcanzó Top-1 = 50.95%, Top-3 = 67.14% y MRR@100 = 0.6297 sobre las 1,056 series EVAL; que presentó los mayores valores observados entre las familias comparadas en §5.2; y que los contrastes primarios HE2_A frente a flat normative BM25, hierarchical normative BM25 y corrected D1a tuvieron sus 15 intervalos de 99% completamente por encima de cero bajo el alcance inferencial congelado. La conclusión permitida es únicamente sobre candidate retrieval dentro del benchmark interno. No puede denominarse overall classification accuracy ni superioridad del framework completo.

### RQ2 — documentary evidence

Puede sintetizarse que los 3,168/3,168 candidate slots del Top-3 fijo tuvieron asociación documental exacta NANDINA-8; los 1,056/1,056 casos tuvieron evidencia exacta para sus tres candidatos; y la asociación documental preservó composición y orden del Top-3 en los 1,056 casos. La interpretación permitida es cobertura/asociación/trazabilidad/invariancia. No puede convertirse en corrección normativa sustantiva o jurídica.

### RQ3 — controlled explanation

Puede sintetizarse que los 50/50 casos preservaron el Top-3 y los controles estructurales/trazabilidad congelados, mientras 28/50 (56.0%) cumplieron el criterio cualitativo de auditabilidad; el scoring cualitativo fue realizado por un evaluador AI en `AI_EXPERT_ROLE`, no por humanos; y el `0/50` de schema compliance provino del `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` ya documentado. La interpretación permitida es una combinación de preservación estructural completa con auditabilidad cualitativa parcial bajo esa modalidad de evaluación. No implica human validation, legal correctness o faithful causal explanation.

### RQ4 — validity limits

Puede sintetizarse que v0.2 eliminó overlap de DAM e `id_unico` entre particiones, pero persistió similitud textual residual entre declaraciones distintas; que la sensibilidad del banco histórico depende conjuntamente de tamaño/composición y que H150/H200 produjo diferencias descriptivas pequeñas y mixtas; que la sensibilidad correctiva del recurso normativo fue method-dependent; que EXP12 diversity y description-quality no fueron estimables; y que HE5 permaneció `INCONCLUSIVE`. Estos elementos delimitan la interpretación del piloto offline y no establecen generalización externa, causalidad, suficiencia histórica universal ni validez jurídica.

## Forma editorial obligatoria

§5.7 debe ser breve y funcionar como puente de cierre de Results. Debe organizarse explícitamente por RQ1–RQ4, preferentemente en cuatro párrafos compactos o una tabla extremadamente simple si el Word puede conservarla sin introducir riesgo editorial. No debe repetir toda la numeración de §5.1–§5.6; debe elegir solo los anclajes indispensables para identificar evidencia, hallazgo principal y límite de interpretación.

No introducir literatura previa, explicación causal, implicaciones prácticas nuevas, recomendaciones, contribuciones, novelty, `FINAL_GAP`, ni lenguaje propio de Discussion o Conclusion. No agregar cifras que no estén ya integradas en §5.1–§5.6. No reinterpretar HE2/HE5 más allá de C28/C29.

## Estado

```text
RESULTS_B07_SECTION_5_7 = EDITORIALLY_JUSTIFIED / READY_FOR_PROMPT
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

Section 5.7 is retained because the four research questions cut across six Results subsections and a compact RQ-oriented synthesis improves readability before Discussion. The section may only summarize already integrated Results 5.1–5.6. It must add no new result, inference, claim, literature comparison, implication, novelty statement, or Discussion-level interpretation. RQ1 summarizes bounded candidate-retrieval evidence and HE2 inference; RQ2 summarizes documentary coverage/traceability/invariance; RQ3 summarizes structural preservation and partial qualitative auditability under AI-expert evaluation; and RQ4 summarizes the benchmark, sensitivity, non-estimability, normative-drift, and HE5 limitations.