# PROMPT 92 — CORREGIR G4-F03: CONSISTENCIA ENTRE ARTEFACTO HUMANO Y REGISTRO MACHINE-READABLE

## 0. Naturaleza, alcance y autorización

Esta ejecución corresponde exclusivamente a una **corrección documental y de trazabilidad** del candidato G4-F03 producido por Prompt91.

La auditoría externa independiente de Prompt91 determinó:

```text
PROMPT91_EXTERNAL_AUDIT = PASS_WITH_CORRECTION_REQUIRED
G4_F03_SCIENTIFIC_CONTENT = SUBSTANTIVELY_PASS
G4_F03_TRACEABILITY_CONSISTENCY = FAIL
SCIENTIFIC_RECOMPUTATION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
CORRECTION_SCOPE = DOCUMENTARY_REGISTRY_RECONCILIATION_ONLY
G4_F03 = NOT_APPROVABLE_FOR_INTEGRATION_YET
GROUP4 = IN_PROGRESS / NOT_CLOSED
G5_F01_AUTHORIZED = false
```

La invocación explícita de este Prompt92 por el usuario autoriza únicamente la generación de un **candidato corregido G4-F03 v02** y la actualización administrativa necesaria para dejarlo pendiente de auditoría externa.

No autoriza:

- integración a `main`;
- cierre de Grupo 4;
- activación o ejecución de G5-F01;
- nueva literatura;
- nueva ciencia;
- recomputación de métricas o inferencia;
- modificación del artículo.

---

## 1. Preflight obligatorio y refs congelados

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
origin/docs/plan-maestro-temporal-2026-08-31 = 89fe5a0c13c8cad03e49280dc2a3edec8bc14a0b
origin/docs/fichas-grupos-3-8 = 5a1d18690c1ea2eb94aa11d1372221389f32468b
origin/codex/group4-f03-literature-contrast-closure-v01 = d8d04c3d516e429fd9117b09fc790a5afb9267c2
```

Referencias de gobernanza:

```text
PROMPT91_SOURCE = a78a6ba29a12dfa505de0f22515ab142e0dffeb6
PROMPT91_RESPONSE = 9fe0f8cee64b1c8b37bd0bd106401bdb898b1b5a
PROMPT91_ACTIVATION_COMMIT = 16d84dfc3284c684cb6c7ecabc1763d435fa27d3
PROMPT91_POSTEXEC_FICHAS_COMMIT = 5a1d18690c1ea2eb94aa11d1372221389f32468b
PROMPT91_CANDIDATE_V01 = d8d04c3d516e429fd9117b09fc790a5afb9267c2
```

Blobs del candidato v01 que deben usarse como fuente de corrección:

```text
V01_LITERATURE_CONTRAST_BLOB = cb9a8309de29045ecaa19fd7f2e12803b40a9d43
V01_GROUP4_CLOSURE_CANDIDATE_BLOB = f02d2abcce3e7ac9958d4901c300b99c7d841bd7
```

Artículo observado al diseñar esta corrección:

```text
origin/article/main-manuscript = 4af2fe11c4992fe0fefc6265a397e8b40f48ea1f
```

La rama editorial es solo lectura y observacional. Si avanza concurrentemente, registra el nuevo HEAD pero no la modifiques.

Si `main`, Plan, fichas o candidato v01 presentan drift no explicado:

```text
STOP / G4_F03_CORRECTION_REF_DRIFT
```

---

## 2. Defectos externos que deben corregirse exactamente

La auditoría externa identificó tres defectos de consistencia, no de contenido científico.

### D92-01 — `comparison_registry` no coincide entre Markdown y JSON

El Markdown v01 contiene **11** filas sustantivas en la matriz de contraste, mientras el JSON v01 contiene **10** entradas `CMP-001..CMP-010`.

La fila independiente omitida en el JSON es el contraste:

```text
Evidencia normativa posterior al ranking
↔ autoridad, vigencia y trazabilidad normativa de 0B05C
↔ QUALITATIVE_ONLY
↔ fuente oficial/asociación normativa/recuperación documental no equivalen a suficiencia jurídica ni clasificación correcta
```

La versión corregida debe contener **11 entradas idénticas semánticamente** en ambos artefactos.

### D92-02 — `AUTHORIZED_DISCUSSION_POINTS` no coincide entre Markdown y JSON

El Markdown v01 contiene **8** puntos autorizados `ADP-001..ADP-008`.

El JSON v01 contiene **6** puntos y, además, reutiliza `ADP-005` y `ADP-006` con significados diferentes.

La versión corregida debe contener exactamente **8 puntos `ADP-001..ADP-008`**, con identidad uno-a-uno entre Markdown y JSON en:

```text
discussion_id
project_claim_ids
literature_source_ids_or_paths
comparison_class
allowed_statement
mandatory_qualification
scientific_role
```

### D92-03 — ADP-003 usa anchors editoriales prohibidos como si fueran claims positivos autorizados

El v01 usa:

```text
C12; C13; C18
```

como `project_claim_ids` de ADP-003.

Sin embargo, en `article/CLAIM_EVIDENCE_MATRIX.md` esos tres IDs son `PROHIBITED`:

```text
C12 = evidencia normativa asociada demuestra corrección normativa sustantiva → PROHIBITED
C13 = explicaciones HE4 demuestran corrección jurídica completa → PROHIBITED
C18 = el estudio produce clasificaciones jurídicamente vinculantes → PROHIBITED
```

No uses esos IDs como anchors positivos de un punto autorizado.

Para ADP-003 usa exclusivamente los guardrails científicos aprobados de G4-F01:

```text
G3C-017 = Retrieved normative evidence does not equal binding legal correctness.
G3C-018 = Auditable explanation does not equal classification or legal correctness.
```

Sus filas G4-F01 correspondientes son `G4F01-0017` y `G4F01-0018`.

---

## 3. RPRE correctivo obligatorio

Antes de crear el candidato v02 registra y exige `PASS` para:

```text
RPRE_G4_F03_CORRECTION_SOURCE_CONTRACT
RPRE_G4_F03_CORRECTION_SCOPE_ONLY
RPRE_G4_F03_NO_NEW_SCIENCE
RPRE_G4_F03_NO_NEW_LITERATURE
RPRE_G4_F03_MARKDOWN_JSON_REGISTRY_SYNCHRONIZATION
RPRE_G4_F03_PROHIBITED_CLAIM_ANCHOR_GUARDRAIL
RPRE_G4_F03_HE2_HE5_PRESERVATION
RPRE_G4_F03_ARTICLE_READONLY
RPRE_G4_F03_GROUP4_NOT_CLOSED
RPRE_G4_F03_G5_NOT_STARTED
```

Si cualquiera falla:

```text
STOP / G4_F03_CORRECTION_RPRE_FAILED
```

---

## 4. Candidato v01 inmutable y rama correctiva v02

No modifiques la rama ni el commit v01.

El candidato v01 queda como historia auditable y será supersedido solo si el v02 supera auditoría externa.

Crea desde `origin/main` exactamente:

```text
branch = codex/group4-f03-literature-contrast-closure-v02
base = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
```

La rama v02 debe contener **un solo commit documental G4-F03**:

```text
COMMITS_AHEAD_OF_MAIN = 1
COMMITS_BEHIND_MAIN = 0
CHANGED_PATH_COUNT = 2
```

Paths únicos:

```text
docs/analysis/group4/g4_literature_contrast_v0.1.md
outputs/audits/group4_closure_v0.1.json
```

Usa como base semántica el contenido del v01. No agregues hallazgos, resultados, referencias, comparaciones o interpretaciones nuevas fuera de las correcciones D92-01 a D92-03 y de los campos de validación necesarios para demostrar consistencia.

---

## 5. Contrato canónico de `comparison_registry`

La matriz Markdown y `comparison_registry` JSON deben contener exactamente los siguientes 11 registros, en este orden y con los mismos IDs:

```text
CMP-001 = HE2 / historical retrieval internal advantage vs frozen external classification-retrieval literature / NOT_DIRECTLY_COMPARABLE
CMP-002 = historical ranking -> post-ranking normative evidence -> fixed Top-3 explanation / QUALITATIVE_ONLY
CMP-003 = local LLM cannot introduce or reorder codes / PARTIALLY_COMPARABLE
CMP-004 = separation of ranking performance, documentary evidence and controlled explanation / QUALITATIVE_ONLY
CMP-005 = versioned artifact traceability and result->claim->evidence bridge / PARTIALLY_COMPARABLE
CMP-006 = post-ranking normative evidence vs official-source authority/currency/traceability in 0B05C / QUALITATIVE_ONLY
CMP-007 = DAM-grouped dependence control / QUALITATIVE_ONLY
CMP-008 = EXP11A joint size-composition sensitivity / NOT_DIRECTLY_COMPARABLE
CMP-009 = EXP11B descriptive H150/H200 over ten observed seed pairs / NOT_DIRECTLY_COMPARABLE
CMP-010 = 0B05C Attempt06 method-dependent impact / PARTIALLY_COMPARABLE
CMP-011 = EXP12 closed without retrieval / diversity effect not estimable / NOT_DIRECTLY_COMPARABLE
```

Para cada registro conserva del v01 la justificación de compatibilidad y frontera interpretativa correspondientes. No fortalezcas ninguna comparación.

El Markdown debe hacer visibles los `comparison_id` para permitir comprobación uno-a-uno.

---

## 6. Contrato canónico de `AUTHORIZED_DISCUSSION_POINTS`

Conserva los ocho puntos granulares del Markdown v01, salvo la sustitución de anchors de ADP-003 requerida por D92-03.

La versión corregida debe usar exactamente esta estructura semántica:

```text
ADP-001
project_claim_ids = HE2; G4-F01
literature = 0B01; 0B02; 0B04A
comparison_class = NOT_DIRECTLY_COMPARABLE
allowed = El retrieval histórico obtuvo mejor rendimiento interno que los brazos normativos corregidos.
qualification = Solo en el benchmark congelado; no comparar porcentajes externos.
role = METHODOLOGICAL

ADP-002
project_claim_ids = C01; C02; C03
literature = 0B03A; 0B03B; 0B04B
comparison_class = QUALITATIVE_ONLY
allowed = El piloto separa ranking, evidencia normativa y explicación del Top-3 fijo.
qualification = Diferencia funcional, sin superioridad ni exclusividad.
role = TECHNICAL

ADP-003
project_claim_ids = G3C-017; G3C-018
literature = 0B02; 0B03A; 0B03B
comparison_class = QUALITATIVE_ONLY
allowed = Evidencia, rationale y citas tienen roles distinguibles de la auditabilidad formal.
qualification = Ninguno demuestra clasificación correcta ni legal correctness.
role = TRACEABILITY

ADP-004
project_claim_ids = G4-F02
literature = 0B05A; 0B05C
comparison_class = PARTIALLY_COMPARABLE
allowed = La procedencia y la identidad de artefactos mejoran la inspección de la cadena experimental.
qualification = No certifican calidad, suficiencia jurídica ni correctness.
role = TRACEABILITY

ADP-005
project_claim_ids = EXP11A
literature = 0B04A; 0B05A
comparison_class = NOT_DIRECTLY_COMPARABLE
allowed = EXP11A documenta sensibilidad conjunta a tamaño y composición.
qualification = Es no causal y no aísla el efecto de tamaño.
role = LIMITATION

ADP-006
project_claim_ids = EXP11B
literature = 0B04A; 0B05A
comparison_class = NOT_DIRECTLY_COMPARABLE
allowed = EXP11B describe H150/H200 sobre diez pares de seeds observados.
qualification = Sin inferencia a superpoblación de seeds.
role = LIMITATION

ADP-007
project_claim_ids = C21; C22; C23; C24; C25
literature = 0B05C
comparison_class = PARTIALLY_COMPARABLE
allowed = El impacto correctivo 0B05C es dependiente del método.
qualification = No resumir como impacto global cero ni inferir causalidad o significancia.
role = LIMITATION

ADP-008
project_claim_ids = EXP12
literature = 0B05A
comparison_class = NOT_DIRECTLY_COMPARABLE
allowed = El efecto de diversidad de EXP12 quedó no estimable bajo su contrato congelado.
qualification = No implica inviabilidad global ni informa HE5.
role = LIMITATION
```

Los campos pueden conservar el idioma técnico ya usado en el JSON, pero Markdown y JSON deben ser **semánticamente y estructuralmente idénticos**. No combines ADP-005, ADP-006 y ADP-008.

---

## 7. `FORBIDDEN_DISCUSSION_POINTS`

Conserva los 14 puntos `FDP-001..FDP-014` del v01.

Markdown y JSON deben coincidir exactamente en:

```text
discussion_id
forbidden_statement
```

No agregues ni elimines prohibiciones salvo que sea necesario para corregir una discrepancia puramente representacional; el conteo final debe seguir siendo 14.

---

## 8. Guardrails científicos que no pueden cambiar

Debe conservarse exactamente:

```text
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
WEB_SEARCH_PERFORMED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
NEW_REFERENCE_ADMITTED = false
CROSS_STUDY_NUMERIC_SUPERIORITY_CLAIM_COUNT = 0
SOTA_CLAIM_COUNT = 0
NEW_NOVELTY_CLAIM_COUNT = 0
FINAL_GAP_REDECISION_COUNT = 0
ARTICLE_MODIFIED = false
G5_F01_STARTED = false
```

No cambies las categorías de contribución `TECHNICAL_CONTRIBUTION`, `METHODOLOGICAL_CONTRIBUTION` y `TRACEABILITY_CONTRIBUTION` salvo ajustes puramente representacionales requeridos para mantener igualdad entre artefactos.

---

## 9. Validaciones nuevas obligatorias

El JSON v02 debe incluir, además de las validaciones heredadas de Prompt91:

```text
MARKDOWN_JSON_COMPARISON_REGISTRY_MATCH = true
MARKDOWN_JSON_AUTHORIZED_DISCUSSION_POINTS_MATCH = true
MARKDOWN_JSON_FORBIDDEN_DISCUSSION_POINTS_MATCH = true
AUTHORIZED_DISCUSSION_POINT_PROHIBITED_EDITORIAL_CLAIM_ANCHOR_COUNT = 0
COMPARISON_REGISTRY_COUNT = 11
AUTHORIZED_DISCUSSION_POINT_COUNT = 8
FORBIDDEN_DISCUSSION_POINT_COUNT = 14
SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT = 0
NEW_SCIENTIFIC_STATEMENT_COUNT = 0
```

Debes validar estas condiciones programáticamente o mediante comparación estructurada reproducible antes del commit.

Si cualquiera falla:

```text
STOP / G4_F03_V02_REGISTRY_RECONCILIATION_FAILED
```

---

## 10. Estado del artefacto corregido

Ambos outputs v02 deben seguir siendo candidatos pendientes de auditoría externa.

En el JSON:

```text
artifact_id = GROUP4_CLOSURE_CANDIDATE_V0.1
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G4-F03
group4_closed = false
```

Añade trazabilidad correctiva, por ejemplo:

```text
superseded_candidate_commit = d8d04c3d516e429fd9117b09fc790a5afb9267c2
correction_reason = HUMAN_MACHINE_REGISTRY_RECONCILIATION
scientific_recomputation_required = false
new_inference_required = false
```

No cambies el `artifact_id` histórico salvo que el esquema existente obligue técnicamente a versionarlo; si no existe tal obligación, conserva el identificador y deja la corrección trazada mediante commit y campos anteriores.

---

## 11. Prohibiciones absolutas

No:

- modificar `main`;
- modificar el Plan Maestro;
- modificar la rama candidata v01;
- modificar G3, G4-F01 o G4-F02;
- recalcular resultados, métricas, CI, bootstrap o p-values;
- ejecutar experimentos o retrieval;
- buscar literatura en web;
- incorporar referencias nuevas;
- redecidir HE2 o HE5;
- reabrir EXP12;
- declarar novelty, SOTA o superioridad cross-study;
- modificar `article/main-manuscript`;
- cerrar operativamente Grupo 4;
- activar o ejecutar G5-F01;
- iniciar Grupo 5.

---

## 12. Actualización administrativa del registro de fichas

Después de crear y validar el candidato v02, trabaja en:

```text
branch = docs/fichas-grupos-3-8
base = 5a1d18690c1ea2eb94aa11d1372221389f32468b
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo.

No cambies el estado operativo de la tabla:

```text
G4-F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G5-F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP4 = IN_PROGRESS
```

Añade un bloque correctivo con, como mínimo:

```text
FICHA = G4-F03
CORRECTIVE_PROMPT = PROMPT92
CORRECTION_SCOPE = DOCUMENTARY_REGISTRY_RECONCILIATION_ONLY
SUPERSEDED_CANDIDATE = d8d04c3d516e429fd9117b09fc790a5afb9267c2
CURRENT_CANDIDATE = <commit v02>
SCIENTIFIC_RECOMPUTATION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = IN_PROGRESS
GROUP4_CLOSED = false
G5_F01_AUTHORIZED = false
G5_F01_STARTED = false
PENDING_EXTERNAL_AUDIT = true
```

Haz un único commit administrativo y push normal.

---

## 13. Verificación final obligatoria

Tras todos los push, ejecuta `git fetch origin` y verifica:

```text
origin/main = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
origin/docs/plan-maestro-temporal-2026-08-31 = 89fe5a0c13c8cad03e49280dc2a3edec8bc14a0b

G4_F03_V02_COMMITS_AHEAD = 1
G4_F03_V02_COMMITS_BEHIND = 0
G4_F03_V02_CHANGED_PATH_COUNT = 2

MARKDOWN_JSON_COMPARISON_REGISTRY_MATCH = true
MARKDOWN_JSON_AUTHORIZED_DISCUSSION_POINTS_MATCH = true
MARKDOWN_JSON_FORBIDDEN_DISCUSSION_POINTS_MATCH = true
AUTHORIZED_DISCUSSION_POINT_PROHIBITED_EDITORIAL_CLAIM_ANCHOR_COUNT = 0
COMPARISON_REGISTRY_COUNT = 11
AUTHORIZED_DISCUSSION_POINT_COUNT = 8
FORBIDDEN_DISCUSSION_POINT_COUNT = 14
SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT = 0
NEW_SCIENTIFIC_STATEMENT_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
WEB_SEARCH_PERFORMED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
NEW_REFERENCE_ADMITTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
GROUP4_CLOSED = false
G5_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F01_STARTED = false
```

Si `article/main-manuscript` avanzó concurrentemente, registra el nuevo HEAD como advertencia no bloqueante siempre que Prompt92 no haya modificado esa rama.

---

## 14. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/92_RESPUESTA_CORREGIR_G4_F03_CONSISTENCIA_REGISTROS_CONTRASTE_LITERATURA.md
```

Ese commit de respuesta debe añadir únicamente dicho archivo.

Reporte terminal mínimo:

```text
PROMPT92 = COMPLETED

PREFLIGHT_MAIN = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
PREFLIGHT_PLAN = 89fe5a0c13c8cad03e49280dc2a3edec8bc14a0b
PREFLIGHT_FICHAS = 5a1d18690c1ea2eb94aa11d1372221389f32468b
V01_CANDIDATE = d8d04c3d516e429fd9117b09fc790a5afb9267c2
V02_BRANCH = codex/group4-f03-literature-contrast-closure-v02
V02_CANDIDATE = ...
V02_PARENT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
V02_COMMITS_AHEAD = 1
V02_COMMITS_BEHIND = 0
V02_CHANGED_PATH_COUNT = 2
V02_LITERATURE_CONTRAST_BLOB = ...
V02_GROUP4_CLOSURE_CANDIDATE_BLOB = ...

MARKDOWN_JSON_COMPARISON_REGISTRY_MATCH = true
MARKDOWN_JSON_AUTHORIZED_DISCUSSION_POINTS_MATCH = true
MARKDOWN_JSON_FORBIDDEN_DISCUSSION_POINTS_MATCH = true
AUTHORIZED_DISCUSSION_POINT_PROHIBITED_EDITORIAL_CLAIM_ANCHOR_COUNT = 0
COMPARISON_REGISTRY_COUNT = 11
AUTHORIZED_DISCUSSION_POINT_COUNT = 8
FORBIDDEN_DISCUSSION_POINT_COUNT = 14
SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT = 0
NEW_SCIENTIFIC_STATEMENT_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
WEB_SEARCH_PERFORMED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
NEW_REFERENCE_ADMITTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED_BY_PROMPT92 = false
GROUP4_CLOSED = false

POSTCORRECTION_FICHAS_COMMIT = ...
G4_F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G5_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F01_STARTED = false

BLOCKERS = NONE
WARNINGS = ...
```

Si cualquier precondición falla, detén la ejecución y reporta el bloqueo exacto. No intentes reparar ciencia o gobernanza fuera de este alcance.