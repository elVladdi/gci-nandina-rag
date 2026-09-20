# PROMPT 91 — ACTIVAR Y EJECUTAR G4-F03: CONTRASTE CON LITERATURA Y CANDIDATO DE CIERRE DE GRUPO 4

## 0. Naturaleza, alcance y autorización

Esta ejecución corresponde exclusivamente a **G4-F03 — Contraste con literatura y cierre de Grupo 4**.

La invocación explícita de este Prompt91 por el usuario constituye autorización únicamente para **activar y ejecutar G4-F03**. No autoriza G5-F01 ni ningún bloque posterior.

Estado de entrada esperado:

```text
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = IN_PROGRESS
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F01 = PROSPECTIVE / NOT_AUTHORIZED
```

Objetivo único:

> Posicionar los hallazgos e interpretaciones ya aprobados de Grupo 4 frente a la literatura **ya registrada y congelada en el entorno editorial**, distinguiendo comparaciones directas, comparaciones cualitativas y no-comparabilidad; separar contribución técnica, metodológica y de trazabilidad; y producir un **candidato de cierre de Grupo 4** sin crear ciencia nueva, sin declarar novelty nueva y sin redactar el artículo.

G4-F03 no reabre G3 ni G4-F01/G4-F02, no recalcula resultados y no sustituye la gobernanza editorial del artículo.

---

## 1. Preflight obligatorio y refs congelados

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de modificar cualquier archivo, ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
origin/docs/plan-maestro-temporal-2026-08-31 = 89fe5a0c13c8cad03e49280dc2a3edec8bc14a0b
origin/docs/fichas-grupos-3-8 = 448d1916571f32f151457e832e462ef2e77b1800
```

Artículo observado al diseñar Prompt91:

```text
origin/article/main-manuscript = 80cda7feeb2cc4979fdc6ccdfc04bd3ba05d97ea
```

La rama editorial es **solo lectura y observacional**. Puede avanzar concurrentemente. Un cambio de HEAD no bloquea por sí solo esta ejecución si los artefactos bibliográficos requeridos conservan exactamente los blobs congelados indicados en este prompt.

Si `main`, Plan o fichas presentan drift no explicado:

```text
STOP / G4_F03_PREFLIGHT_REF_DRIFT
```

La ejecución debe registrar el SHA exacto de Prompt91 recibido en la invocación del usuario.

---

## 2. Ficha gobernante

Lee íntegramente:

```text
docs/fichas/grupos_3_8/grupo_4/G4_F03_CONTRASTE_LITERATURA_Y_CIERRE.md
```

en la rama:

```text
docs/fichas-grupos-3-8
```

Contrato obligatorio:

- comparar solo métricas, datasets, tareas y niveles HS conceptualmente compatibles;
- identificar expresamente cuándo el contraste es solo cualitativo;
- separar contribución **técnica**, **metodológica** y de **trazabilidad**;
- producir discussion points permitidos y prohibidos;
- usar literatura ya registrada/validada en el entorno editorial;
- no convertir diferencias metodológicas en comparaciones directas inválidas.

No cierres operativamente Grupo 4 en esta ejecución. Debes producir un **candidato de cierre pendiente de auditoría externa**.

---

## 3. RPRE obligatorio antes de activar G4-F03

Realiza revisión preventiva de riesgos y registra, como mínimo:

```text
RPRE_G4_F03_SOURCE_CONTRACT
RPRE_G4_F03_NO_NEW_SCIENCE
RPRE_G4_F03_LITERATURE_FROZEN_ONLY
RPRE_G4_F03_COMPARABILITY_GUARDRAIL
RPRE_G4_F03_NO_CROSS_STUDY_NUMERIC_SUPERIORITY
RPRE_G4_F03_NO_NEW_NOVELTY_CLAIM
RPRE_G4_F03_G4F01_G4F02_CONSISTENCY
RPRE_G4_F03_HE2_HE5_PRESERVATION
RPRE_G4_F03_EXP11A_EXP11B_GUARDRAILS
RPRE_G4_F03_0B05C_ATTEMPT06_CURRENT_STATE
RPRE_G4_F03_EXP12_FAIL_CLOSED_SEMANTICS
RPRE_G4_F03_ARTICLE_READONLY
RPRE_G4_F03_G5_NOT_STARTED
```

Todos deben resultar `PASS` antes de continuar.

Si alguno falla:

```text
STOP / G4_F03_RPRE_FAILED
```

No intentes resolver un fallo alterando ciencia previa ni la gobernanza editorial.

---

## 4. Activación prospectiva obligatoria

Antes de crear los outputs G4-F03, trabaja sobre:

```text
branch = docs/fichas-grupos-3-8
base = 448d1916571f32f151457e832e462ef2e77b1800
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo y cambia:

```text
G4-F03 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G5-F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque de activación con, como mínimo:

```text
FICHA = G4-F03
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT91_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
ACTIVATION_DATE = <fecha real de ejecución>
MAIN_AT_ACTIVATION = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
PLAN_AT_ACTIVATION = 89fe5a0c13c8cad03e49280dc2a3edec8bc14a0b
FICHAS_AT_ACTIVATION = 448d1916571f32f151457e832e462ef2e77b1800
ARTICLE_HEAD_OBSERVED = <HEAD observado>
PROMPT91_COMMIT = <SHA exacto recibido en la invocación>
GROUP3 = CLOSED / APPROVED
GROUP4 = IN_PROGRESS
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
G5_F01_AUTHORIZED = false
```

Haz un único commit de activación y push normal. Después de `git fetch origin`, confirma que la activación está materializada en remoto.

Solo entonces puedes producir los artefactos G4-F03.

---

## 5. Rama científica/documental de trabajo

Desde el `main` congelado crea:

```text
branch = codex/group4-f03-literature-contrast-closure-v01
base = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
```

La rama candidata debe contener **un solo commit científico/documental G4-F03** y quedar:

```text
COMMITS_AHEAD_OF_MAIN = 1
COMMITS_BEHIND_MAIN = 0
```

No integres esta rama a `main`. La integración y el cierre operativo de Grupo 4 solo podrán ocurrir después de auditoría externa independiente.

---

## 6. Fuentes experimentales rectoras

### 6.1 G4-F01

Usa como puente claim-evidencia aprobado:

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
```

Blobs aprobados:

```text
CSV_BLOB = da0351cb523fc7f3b45a83e072765a07f809b7fe
JSON_BLOB = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab
```

### 6.2 G4-F02

Usa como interpretación controlada y registro de límites:

```text
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
```

Blobs aprobados:

```text
SYNTHESIS_BLOB = 129a67b15db429b86af059d61753b1942c8f243f
LIMITATIONS_REGISTRY_BLOB = ae00b93431e912cb78a58344057d9bf7a51fcd47
```

### 6.3 Estado científico que no puede redecidirse

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

G4-F03 no recalcula ni redecide ninguna hipótesis.

---

## 7. Corpus bibliográfico permitido y congelado

Usa **exclusivamente** literatura ya validada/congelada en `article/main-manuscript`.

Gobernanza editorial de solo lectura:

```text
article/SOURCE_REGISTRY.md
BLOB = a93b5c92ca0e4a077c22ae9c30d1590202ad1a8c

article/BIBLIOGRAPHIC_FRAMEWORK.md
BLOB = 78a08a0ad794eaa337bbace9bd7c082c50b464c3

article/CLAIM_EVIDENCE_MATRIX.md
BLOB = 255daa8cef57d659b426470d82b11db58fe688a5
```

Literatura canónica prioritaria:

```text
article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md
BLOB = 644483ac6bed8c3a5df572a2ab53db698568e2fe

article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md
BLOB = 55636236193afbd523609f8b0ccee987035d35ef

article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md
BLOB = 4c25a91cc9562d72d7734976940ff37819e919c0

article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md
BLOB = 1bb70fdc93bafb8c883a0383ec2e67fe652cfab2

article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md
BLOB = 6c8bbf48fd64aac87b54374a8c9af8ce7b1945f0

article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md
BLOB = cde65f51d2959f90c321458cd8fa50073d1ba056

article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md
BLOB = 0c342a37feb927f1fa2b384125229f38add382aa

article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_FROZEN.md
BLOB = 406cc7f91595736fdad98265109858102f238ea1
```

Verifica los blobs antes de usar cada fuente. Si el HEAD editorial avanzó pero estos blobs permanecen idénticos, continúa y registra el nuevo HEAD observado. Si cambia cualquier blob requerido:

```text
STOP / G4_F03_FROZEN_LITERATURE_SOURCE_DRIFT
```

### Prohibición de expansión bibliográfica

En esta ejecución:

```text
WEB_SEARCH = PROHIBITED
NEW_LITERATURE_SEARCH = PROHIBITED
NEW_REFERENCE_ADMISSION = PROHIBITED
ARTICLE_SOURCE_REGISTRY_MODIFICATION = PROHIBITED
```

Si el corpus congelado no permite una comparación válida, registra `NOT_DIRECTLY_COMPARABLE` o `INSUFFICIENT_FROZEN_LITERATURE_FOR_DIRECT_COMPARISON`. No busques una referencia nueva para forzar el contraste.

No uses como soporte directo un paper cuyo freeze lo mantenga `REVIEW_REQUIRED` para metadata/citación cerrada, salvo que el contraste use únicamente una afirmación explícitamente congelada como permitida y deje visible su caveat.

---

## 8. Contrato de comparabilidad

Cada contraste entre un hallazgo del proyecto y un antecedente debe clasificarse en una de estas categorías:

```text
DIRECTLY_COMPARABLE
PARTIALLY_COMPARABLE
QUALITATIVE_ONLY
NOT_DIRECTLY_COMPARABLE
```

### 8.1 Requisitos mínimos para `DIRECTLY_COMPARABLE`

Solo puede utilizarse si están alineados, como mínimo:

- tarea científica;
- tipo de salida;
- nivel HS relevante;
- definición exacta de métrica;
- denominador;
- protocolo de evaluación;
- tratamiento de rejection/fallback si existe;
- unidad de validación/partición suficientemente comparable;
- interpretación estadística compatible.

Si cualquiera de estos elementos impide una comparación limpia, usa `PARTIALLY_COMPARABLE`, `QUALITATIVE_ONLY` o `NOT_DIRECTLY_COMPARABLE`.

### 8.2 Regla numérica estricta

No escribas claims del tipo:

```text
our method outperforms paper X
higher accuracy than prior work
state of the art
best performance in the literature
```

basados en porcentajes heterogéneos entre datasets, tareas, niveles HS o protocolos distintos.

Debe cumplirse:

```text
CROSS_STUDY_NUMERIC_SUPERIORITY_CLAIM_COUNT = 0
SOTA_CLAIM_COUNT = 0
```

Los resultados internos de HE2 sí pueden describirse como comparación **interna al benchmark congelado**, no como superioridad frente a literatura externa.

### 8.3 Distinciones obligatorias

Preserva expresamente:

```text
Top-k retrieval ≠ classification accuracy ≠ weighted F1 ≠ MRR ≠ Hits@k
ranking histórico ≠ deep search regulatorio
precedent retrieval ≠ normative evidence retrieval
RAG classification ≠ RAG evidence support ≠ customs QA RAG
visible evidence/citations ≠ formal auditability ≠ legal correctness
constraint/path validity ≠ independent legal correctness
provenance/reproducibility ≠ output-level auditability ≠ correctness
```

---

## 9. Ejes de contraste obligatorios

El artefacto debe cubrir, al menos, los siguientes ejes.

### 9.1 Rendimiento y retrieval — HE2

Contrasta cualitativamente el hallazgo interno de HE2 con trabajos de clasificación/retrieval HS ya congelados.

Debe quedar claro que:

- el retrieval histórico superó internamente a los tres brazos normativos corregidos en las cinco métricas primarias HE2_A;
- esa superioridad es **interna al benchmark congelado**;
- no es directamente comparable con accuracies/F1/Top-k reportados en datasets y protocolos externos;
- literatura previa ya contiene Top-k, semantic retrieval, sentence retrieval, precedent retrieval y clasificación directa; por tanto, ninguno de esos componentes aislados es novedoso.

### 9.2 Arquitectura y rol del LLM

Contrasta con THE-RAG, ICCA-RAG y los trabajos agentic/hierarchical congelados.

Preserva:

- otros sistemas ya usan RAG, reglas, jerarquía, agentes, KG, evidencia y rationale;
- en varios de ellos la evidencia/reglas participan en la **decisión del código**;
- el presente piloto separa `ranking histórico -> evidencia normativa posterior -> explicación controlada del Top-3 fijo`;
- el LLM local no clasifica desde cero ni puede introducir/reordenar códigos;
- esta diferencia es de **arquitectura/contrato de decisión**, no prueba automática de superioridad o novelty absoluta.

### 9.3 Auditabilidad, trazabilidad y correctness

Contrasta con Explainable Product Classification for Customs, Grainger, ICCA-RAG, workflows agentic, provenance/reproducibility y audit trail.

Debe conservarse:

- evidencia visible, citations, rationale, faithfulness, provenance o transparency trail no equivalen automáticamente a evaluación formal de auditabilidad por salida;
- auditabilidad no equivale a corrección jurídica;
- evidencia normativa recuperada no equivale a ruling vinculante;
- el presente trabajo aporta separación explícita entre rendimiento de ranking, evidencia documental y explicación auditable, pero no demuestra legal correctness.

### 9.4 Dependencia, partición y validez interna

Contrasta únicamente en términos metodológicos.

- ausencia de DAM-equivalent group split en antecedentes no demuestra leakage;
- el control por DAM del presente trabajo es una decisión de diseño para su estructura de observaciones relacionadas;
- no presentes esa diferencia como defecto probado de trabajos previos.

### 9.5 Sensibilidad y límites

Integra sin alterar:

```text
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

No busques paralelos bibliográficos artificiales para EXP12 si el corpus congelado no contiene un diseño conceptualmente comparable.

---

## 10. Contribución: categorías permitidas

La síntesis debe separar expresamente:

### `TECHNICAL_CONTRIBUTION`

Arquitectura funcional y contrato de componentes implementados en el piloto.

### `METHODOLOGICAL_CONTRIBUTION`

Diseño/evaluación: separación de funciones, control de dependencia, métricas/claims delimitados, sensibilidad no causal donde corresponde y fronteras de validez.

### `TRACEABILITY_CONTRIBUTION`

Puente resultado→claim→evidencia, registro explícito de limitaciones, provenance/identidad de artefactos y explicación auditable documentada.

Estas categorías describen la contribución del trabajo frente al corpus congelado; **no autorizan por sí mismas un claim de novelty**.

Debe cumplirse:

```text
NEW_NOVELTY_CLAIM_COUNT = 0
FINAL_GAP_REDECISION_COUNT = 0
```

No declares “first”, “first-ever”, “novel”, “unique”, “unprecedented” ni equivalentes salvo que ya exista una decisión editorial explícita y congelada que autorice exactamente esa formulación. Si no existe, no la uses.

---

## 11. Discussion points autorizados y prohibidos

Genera dos registros separados.

### 11.1 `AUTHORIZED_DISCUSSION_POINTS`

Cada punto debe incluir:

```text
discussion_id
project_claim_ids
literature_source_ids_or_paths
comparison_class
allowed_statement
mandatory_qualification
scientific_role = TECHNICAL | METHODOLOGICAL | TRACEABILITY | LIMITATION
```

### 11.2 `FORBIDDEN_DISCUSSION_POINTS`

Incluye como mínimo prohibiciones contra:

- superioridad numérica cross-study no comparable;
- SOTA;
- novelty absoluta no gobernada;
- causalidad de EXP11A;
- superpoblación de seeds EXP11B;
- impacto global cero de 0B-05C;
- inviabilidad matemática global de EXP12;
- uso de EXP12 como evidencia a favor/en contra de HE5;
- exactitud global del RAG derivada de retrieval histórico;
- corrección jurídica derivada de evidencia normativa;
- explicación auditable tratada como validación de clasificación;
- leakage atribuido a antecedentes solo por ausencia de group split documentado.

---

## 12. Outputs exactos

Crea exclusivamente en la rama candidata:

```text
docs/analysis/group4/g4_literature_contrast_v0.1.md
outputs/audits/group4_closure_v0.1.json
```

No crees otros artefactos científicos/documentales en esa rama.

### 12.1 `g4_literature_contrast_v0.1.md`

Debe contener como mínimo:

1. Scope y corpus congelado usado.
2. Reglas de comparabilidad.
3. Matriz `project finding ↔ literature ↔ comparison class ↔ interpretation boundary`.
4. Contraste HE2/retrieval.
5. Contraste arquitectura/RAG/LLM/agentes.
6. Contraste auditabilidad/trazabilidad/correctness.
7. Contraste metodológico de dependencia/partición.
8. Sensibilidades y no-estimabilidad.
9. Contribución técnica/metodológica/trazabilidad.
10. `AUTHORIZED_DISCUSSION_POINTS`.
11. `FORBIDDEN_DISCUSSION_POINTS`.
12. Handoff a Grupo 5.

No redactes una sección Discussion lista para publicar.

### 12.2 `group4_closure_v0.1.json`

Debe ser un registro machine-readable de candidato de cierre, con al menos:

```text
artifact_id
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G4-F03
group4_closed = false
main_base
plan_snapshot
fichas_activation_commit
prompt91_commit
article_head_observed
article_head_final_observed
required_literature_blobs
experimental_source_blobs
comparison_registry
authorized_discussion_points
forbidden_discussion_points
contribution_categories
validation
```

La sección `validation` debe incluir, como mínimo:

```text
FROZEN_LITERATURE_SOURCE_COUNT_USED >= 1
UNVERIFIED_NEW_REFERENCE_COUNT = 0
WEB_SEARCH_PERFORMED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
NEW_REFERENCE_ADMITTED = false
CROSS_STUDY_NUMERIC_SUPERIORITY_CLAIM_COUNT = 0
SOTA_CLAIM_COUNT = 0
NEW_NOVELTY_CLAIM_COUNT = 0
FINAL_GAP_REDECISION_COUNT = 0
DIRECT_COMPARISON_WITHOUT_COMPATIBILITY_JUSTIFICATION_COUNT = 0
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false
EXP11A_CAUSAL_SIZE_EFFECT_CLAIM_COUNT = 0
EXP11B_SEED_SUPERPOPULATION_INFERENCE_COUNT = 0
0B05C_GLOBAL_ZERO_IMPACT_CLAIM_COUNT = 0
EXP12_GLOBAL_INFEASIBILITY_CLAIM_COUNT = 0
EXP12_HE5_POSITIVE_EVIDENCE_COUNT = 0
EXP12_HE5_NEGATIVE_EVIDENCE_COUNT = 0
GLOBAL_RAG_ACCURACY_FROM_HISTORICAL_RETRIEVAL_COUNT = 0
LEGAL_CORRECTNESS_FROM_NORMATIVE_EVIDENCE_COUNT = 0
EXPLANATION_EQUALS_CLASSIFICATION_VALIDATION_COUNT = 0
LEAKAGE_ASSERTED_FROM_MISSING_GROUP_SPLIT_COUNT = 0
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
G5_F01_STARTED = false
```

---

## 13. Prohibiciones absolutas

No:

- modificar artefactos G3, G4-F01 o G4-F02;
- recalcular métricas, CI, bootstrap, p-values o agregados;
- reejecutar experimentos o retrieval;
- redecidir HE2 o HE5;
- reabrir EXP12;
- buscar literatura en web;
- incorporar nuevas referencias;
- modificar `article/main-manuscript`;
- modificar `article/SOURCE_REGISTRY.md`, `BIBLIOGRAPHIC_FRAMEWORK.md`, `CLAIM_EVIDENCE_MATRIX.md` o archivos frozen;
- redactar Results, Discussion, Conclusions, artículo o tesis;
- declarar novelty o SOTA no gobernados;
- cerrar operativamente Grupo 4 antes de auditoría externa;
- activar o ejecutar G5-F01;
- iniciar Grupo 5.

---

## 14. Validación del candidato

Antes del push confirma:

```text
CHANGED_PATH_COUNT = 2
COMMITS_AHEAD_OF_MAIN = 1
COMMITS_BEHIND_MAIN = 0
```

Paths exactos:

```text
docs/analysis/group4/g4_literature_contrast_v0.1.md
outputs/audits/group4_closure_v0.1.json
```

Verifica además todas las flags de `validation` de la Sección 12.2.

Si alguna falla:

```text
STOP / G4_F03_CANDIDATE_VALIDATION_FAILED
```

No integres el candidato.

---

## 15. Estado postejecución en fichas

Después de producir y validar el candidato, actualiza únicamente:

```text
branch = docs/fichas-grupos-3-8
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

desde el commit de activación generado en la Sección 4.

Deja:

```text
G4-F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G5-F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP4 = IN_PROGRESS
```

Añade bloque de candidato con, como mínimo:

```text
G4_F03_BRANCH = codex/group4-f03-literature-contrast-closure-v01
G4_F03_CANDIDATE_COMMIT = <commit>
G4_F03_CANDIDATE_PARENT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
G4_F03_CHANGED_PATH_COUNT = 2
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
NEW_NOVELTY_CLAIM_COUNT = 0
CROSS_STUDY_NUMERIC_SUPERIORITY_CLAIM_COUNT = 0
PENDING_EXTERNAL_AUDIT = true
GROUP4_CLOSED = false
G5_F01_AUTHORIZED = false
RESULT = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

Haz un único commit postejecución y push normal.

No modifiques el Plan Maestro en Prompt91. El Plan solo se reconciliará tras auditoría externa e integración aprobada.

---

## 16. Verificación final obligatoria

Tras todos los push, ejecuta `git fetch origin` y verifica:

```text
origin/main = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
origin/docs/plan-maestro-temporal-2026-08-31 = 89fe5a0c13c8cad03e49280dc2a3edec8bc14a0b

G4_F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP4 = IN_PROGRESS
GROUP4_CLOSED = false
G5_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F01_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
WEB_SEARCH_PERFORMED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
NEW_REFERENCE_ADMITTED = false
CROSS_STUDY_NUMERIC_SUPERIORITY_CLAIM_COUNT = 0
SOTA_CLAIM_COUNT = 0
NEW_NOVELTY_CLAIM_COUNT = 0
ARTICLE_MODIFIED = false
```

Verifica que `article/main-manuscript` no fue modificado por Prompt91. Si avanzó concurrentemente, registra el HEAD final observado y comprueba que los blobs bibliográficos realmente usados permanecieron congelados.

---

## 17. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/91_RESPUESTA_ACTIVAR_Y_EJECUTAR_G4_F03_CONTRASTE_LITERATURA_Y_CIERRE.md
```

Ese commit de respuesta debe añadir únicamente dicho archivo.

Reporte terminal mínimo:

```text
PROMPT91 = COMPLETED

PREFLIGHT_MAIN = ...
PREFLIGHT_PLAN = ...
PREFLIGHT_FICHAS = ...
ARTICLE_HEAD_OBSERVED = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...
ARTICLE_MODIFIED_BY_PROMPT91 = false

RPRE_G4_F03_SOURCE_CONTRACT = PASS
RPRE_G4_F03_NO_NEW_SCIENCE = PASS
RPRE_G4_F03_LITERATURE_FROZEN_ONLY = PASS
RPRE_G4_F03_COMPARABILITY_GUARDRAIL = PASS
RPRE_G4_F03_NO_CROSS_STUDY_NUMERIC_SUPERIORITY = PASS
RPRE_G4_F03_NO_NEW_NOVELTY_CLAIM = PASS
RPRE_G4_F03_G4F01_G4F02_CONSISTENCY = PASS
RPRE_G4_F03_HE2_HE5_PRESERVATION = PASS
RPRE_G4_F03_ARTICLE_READONLY = PASS
RPRE_G4_F03_G5_NOT_STARTED = PASS

G4_F03_ACTIVATION_COMMIT = ...
G4_F03_BRANCH = codex/group4-f03-literature-contrast-closure-v01
G4_F03_CANDIDATE_COMMIT = ...
G4_F03_CANDIDATE_PARENT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
G4_F03_COMMITS_AHEAD = 1
G4_F03_COMMITS_BEHIND = 0
G4_F03_CHANGED_PATH_COUNT = 2
G4_F03_CHANGED_PATHS = docs/analysis/group4/g4_literature_contrast_v0.1.md; outputs/audits/group4_closure_v0.1.json
LITERATURE_CONTRAST_BLOB = ...
GROUP4_CLOSURE_CANDIDATE_BLOB = ...

FROZEN_LITERATURE_SOURCE_COUNT_USED = ...
UNVERIFIED_NEW_REFERENCE_COUNT = 0
WEB_SEARCH_PERFORMED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
NEW_REFERENCE_ADMITTED = false
CROSS_STUDY_NUMERIC_SUPERIORITY_CLAIM_COUNT = 0
SOTA_CLAIM_COUNT = 0
NEW_NOVELTY_CLAIM_COUNT = 0
DIRECT_COMPARISON_WITHOUT_COMPATIBILITY_JUSTIFICATION_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false

G4_F03_POSTEXEC_FICHAS_COMMIT = ...
G4_F03_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP4_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
G5_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F01_STARTED = false

BLOCKERS = NONE
WARNINGS = ...
```

Si cualquier precondición falla, detén la ejecución y reporta el bloqueo exacto. No intentes reparar ciencia, literatura o gobernanza por cuenta propia.