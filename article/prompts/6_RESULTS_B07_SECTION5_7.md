# Prompt — Results B07 / Section 5.7 Summary by research question

## Español

### Rol

Actúa exclusivamente como IA de Redacción del manuscrito. No cambies gobernanza, no abras Discussion y no avances fuera del bloque autorizado.

### Bloque autorizado

```text
BLOCK = RESULTS_B07_SECTION_5_7
SECTION = 5.7 SUMMARY BY RESEARCH QUESTION
EXECUTION_SCOPE = B07_V01_ONLY
CANONICAL_BASELINE_MD = article/manuscript/ARTICLE_MASTER_V022.md
CANONICAL_BASELINE_MD_SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
CANONICAL_BASELINE_MD_GIT_BLOB = 088eecd537997a3438517f7d206f6d890b0aa064
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
BASELINE_DOCX_SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
EDITORIAL_BOUNDARY = article/governance/D117_RESULTS_B07_SECTION5_7_EDITORIAL_NECESSITY_AND_SYNTHESIS_BOUNDARY.md
SOURCE_OF_TRUTH = INTEGRATED_RESULTS_5_1_TO_5_6_ONLY
```

### Lecturas obligatorias

1. `article/START_HERE.md` y todo onboarding obligatorio.
2. `article/governance/D117_RESULTS_B07_SECTION5_7_EDITORIAL_NECESSITY_AND_SYNTHESIS_BOUNDARY.md`.
3. `article/CLAIM_EVIDENCE_MATRIX.md`, especialmente C28 y C29 y los límites de C12/C13/C14/C18.
4. `article/manuscript/ARTICLE_MASTER_V022.md`, especialmente Sections 5.1–5.6.

No necesitas ni debes abrir un nuevo experimento. §5.7 sintetiza exclusivamente resultados ya integrados.

### Objetivo editorial

Redactar una síntesis compacta por RQ que cierre Results y reduzca la carga cognitiva antes de Discussion. Debe responder en forma resumida:

- qué evidencia principal responde cada RQ;
- cuál es el hallazgo principal permitido;
- cuál es el límite de interpretación más importante.

No repetir exhaustivamente §5.1–§5.6 y no convertir §5.7 en Discussion.

### Contenido autorizado

#### RQ1 — candidate retrieval

Usar solo anclajes ya integrados. Debe quedar claro que:

- EVAL contiene 1,056 series;
- historical BM25 H100 alcanzó Top-1 = 50.95%, Top-3 = 67.14% y MRR@100 = 0.6297;
- tuvo los mayores valores observados entre las cuatro familias de §5.2 para las métricas reportadas;
- los 15 CI primarios HE2_A historical-minus-comparator quedaron completamente por encima de cero bajo el alcance inferencial congelado;
- HE2 queda supported únicamente dentro de ese alcance;
- esto mide candidate retrieval, no overall classification accuracy ni superioridad del framework completo.

#### RQ2 — documentary evidence

Debe quedar claro que:

- 3,168/3,168 candidate slots tuvieron asociación documental exacta NANDINA-8;
- 1,056/1,056 casos tuvieron evidencia exacta para los tres candidatos;
- ranking y membership del Top-3 se preservaron en 1,056/1,056 casos;
- la interpretación es cobertura, asociación, trazabilidad e invariancia;
- no es substantive normative correctness ni legal correctness.

#### RQ3 — controlled explanation

Debe quedar claro que:

- los controles estructurales y de trazabilidad del Top-3 se preservaron en 50/50 casos;
- 28/50 casos (56.0%) cumplieron el criterio cualitativo de auditabilidad;
- el scoring fue realizado por un evaluador independiente en `AI_EXPERT_ROLE` / LLM-as-judge, no por humanos;
- el 0/50 de schema compliance corresponde al `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` ya documentado y no debe describirse como 50 explicaciones inválidas;
- la interpretación es preservación estructural completa con auditabilidad cualitativa parcial bajo esa modalidad de evaluación;
- no constituye human expert validation, legal correctness ni faithful causal explanation.

#### RQ4 — validity limits

Debe quedar claro que:

- v0.2 tuvo cero overlap de DAM e `id_unico` entre particiones, pero retuvo similitud textual residual entre declaraciones distintas;
- EXP11A refleja sensibilidad conjunta a tamaño/composición, no efecto causal aislado del tamaño;
- H150/H200 son descriptivos sobre seeds pareados y mostraron diferencias pequeñas y mixtas;
- la sensibilidad correctiva al recurso normativo fue method-dependent;
- EXP12 diversity y description-quality no fueron estimables;
- HE5 permaneció `INCONCLUSIVE`;
- estos resultados delimitan el piloto offline y no establecen generalización externa, causalidad ni validez jurídica.

### Forma obligatoria

Usa cuatro párrafos compactos en inglés, uno por RQ, seguidos por cuatro párrafos semánticamente equivalentes en español. No crear tabla nueva: mantener el bloque simple reduce riesgo OOXML y evita duplicar visualmente las subsecciones precedentes.

Cada párrafo debe empezar con `RQ1`, `RQ2`, `RQ3` o `RQ4` de forma natural. Mantén la sección total compacta; no reproduzcas listas completas de intervalos, matrices de sensibilidad ni todas las cifras de §5.1–§5.6.

### Límites obligatorios

No introducir:

- nuevos resultados;
- nuevas cifras no integradas en §5.1–§5.6;
- nuevos CI, p-values o tests;
- causalidad;
- external-population generalization;
- superpoblación de seeds/DAM/SERIE;
- overall classification accuracy;
- legal correctness o substantive normative correctness;
- comparación con literatura;
- explicación de mecanismos;
- recomendaciones prácticas;
- novelty;
- `FINAL_GAP`;
- Discussion;
- Conclusion.

No usar lenguaje de contribución novedosa. No añadir citas bibliográficas nuevas.

### Bilingüismo

Redacta primero la Parte I inglesa como publication-facing master y luego el espejo semántico español. Ambos deben ser equivalentes en contenido, cifras y límites. El español debe ser natural.

### Integridad acumulativa

Modificar exclusivamente los placeholders de §5.7 en inglés y español.

Preservar sin cambios:

- Sections 1–5.6;
- Discussion;
- Conclusion;
- end matter;
- 40 comentarios Word;
- estilos, relaciones y estructura OOXML heredada;
- 0 tracked changes.

No reconstruir el DOCX desde Markdown. Editar nativamente el Word acumulativo B06 V01.

D-035 permanece vinculante: prohibidos Base64 manual, chunking, fragmentación, reensamblado y workarounds equivalentes.

### Entregables

Generar:

```text
article/sections/results/Results_B07_V01.md
ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.md
ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.docx
article/responses/6_RESULTS_B07_SECTION5_7_RESPONSE_V01.md
```

Versionar en GitHub solo la sección y la response pequeñas. Entregar ambos masters acumulativos como archivos reales al autor.

La response debe registrar SHA-256 de ambos candidatos, Git blob esperado del Markdown, identidad del baseline, controles de scope, equivalencia EN/ES, equivalencia MD↔DOCX, comentarios, tracked changes, integridad OOXML, render completo y cumplimiento D-035.

Al terminar:

```text
RESULTS_B07_V01_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

Detente ahí.

---

## English

Execute only Results B07 / Section 5.7 from canonical V022 and the approved B06 cumulative DOCX. Draft a compact four-paragraph synthesis organized explicitly by RQ1–RQ4, using only already integrated Results 5.1–5.6 and the limits frozen in D-117. Add no new result, inference, metric, literature comparison, implication, contribution, novelty statement, Discussion, or Conclusion content. Modify only the English and Spanish Section 5.7 placeholders, preserve the cumulative Word natively, and stop after B07 V01.