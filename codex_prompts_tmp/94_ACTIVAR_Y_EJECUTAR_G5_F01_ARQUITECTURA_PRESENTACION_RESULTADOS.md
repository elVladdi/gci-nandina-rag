# PROMPT 94 — ACTIVAR Y EJECUTAR G5-F01: ARQUITECTURA DE PRESENTACIÓN DE RESULTADOS

## 0. Naturaleza, alcance y autorización

Esta ejecución corresponde exclusivamente a **G5-F01 — Arquitectura de presentación de resultados**.

Estado canónico al diseñar este prompt:

```text
GROUP1 = CLOSED / APPROVED
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = NOT_STARTED
G5_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F02 = PROSPECTIVE / NOT_AUTHORIZED
```

El usuario ha indicado además que el flujo experimental debe continuar automáticamente después de cada auditoría satisfactoria. La **invocación explícita de este Prompt94** constituye autorización únicamente para activar y ejecutar G5-F01.

Esta ejecución autoriza:

1. activar administrativamente G5-F01;
2. construir una arquitectura trazable de presentación de resultados;
3. decidir, con base en objetivos, hipótesis, rol científico y evidencia aprobada, qué familias deben ir a tablas principales, tablas secundarias, anexos o texto;
4. producir el plan humano y el registro machine-readable definidos por la ficha.

Esta ejecución **no autoriza**:

- materializar las tablas científicas finales;
- recalcular o recomputar métricas;
- ejecutar inferencia, bootstrap, CI o p-values;
- ejecutar experimentos o retrieval;
- seleccionar resultados por conveniencia narrativa o por magnitud favorable;
- modificar decisiones de HE2 o HE5;
- reabrir EXP12;
- modificar el artículo o la tesis;
- activar ni ejecutar G5-F02;
- cerrar Grupo 5;
- iniciar Grupo 6.

---

## 1. Preflight obligatorio y refs congelados

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 38e22c19a0eb0d344e7675761a88d7968091eead
origin/docs/plan-maestro-temporal-2026-08-31 = 3ba3557eb10e741b8f49c420850940dee1df08ef
origin/docs/fichas-grupos-3-8 = a2dc08c8ce5e4d3490e2600065ea6bd8b84b3830
origin/article/main-manuscript = 88a3570fbc8c91af5f06798dcd82e2157121f394
```

Gobernanza inmediata:

```text
PROMPT92_SOURCE = 65bf62335feae79efa782fdc6b890b096f6e0e90
PROMPT92_RESPONSE = f8e6ff308011b1d3e06476cd79f4b056884f5ce8
G4_F03_CORRECTED_CANDIDATE = 38e22c19a0eb0d344e7675761a88d7968091eead
PROMPT93_SOURCE = e2ae3d294e92adf3b7539f3a947eee4c8593fed4
PROMPT93_RESPONSE = a86602a7220e844df31e5817fe8bfaed71e9c6c6
G4_F03_FICHAS_CLOSURE = a2dc08c8ce5e4d3490e2600065ea6bd8b84b3830
GROUP4_PLAN_CLOSURE = 3ba3557eb10e741b8f49c420850940dee1df08ef
```

Ficha rectora:

```text
docs/fichas/grupos_3_8/grupo_5/G5_F01_ARQUITECTURA_PRESENTACION_RESULTADOS.md
blob = f55ee2a65c145ef7377c983cef9276f4a77d109e
```

La rama editorial es **solo lectura / observacional**. Si `article/main-manuscript` avanza concurrentemente, registra el HEAD final como advertencia no bloqueante siempre que Prompt94 no la modifique.

Si `main`, Plan o fichas presentan drift no explicado:

```text
STOP / G5_F01_REF_DRIFT
```

---

## 2. Activación administrativa prospectiva obligatoria

Antes de crear cualquier output G5-F01, trabaja únicamente en:

```text
branch = docs/fichas-grupos-3-8
base = a2dc08c8ce5e4d3490e2600065ea6bd8b84b3830
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo para dejar:

```text
G5-F01 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G5-F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP5 = IN_PROGRESS
```

Añade bloque de activación con, como mínimo:

```text
FICHA = G5-F01
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT94_EXPLICIT_EXECUTION / STANDING_CONTINUATION_INSTRUCTION_2026-09-20
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
MAIN_AT_ACTIVATION = 38e22c19a0eb0d344e7675761a88d7968091eead
PLAN_AT_ACTIVATION = 3ba3557eb10e741b8f49c420850940dee1df08ef
FICHAS_AT_ACTIVATION = a2dc08c8ce5e4d3490e2600065ea6bd8b84b3830
ARTICLE_HEAD_OBSERVED = <HEAD observado>
PROMPT94_COMMIT = <commit fuente Prompt94>
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
GROUP5 = IN_PROGRESS
G5_F02_AUTHORIZED = false
```

Haz un único commit administrativo y push normal.

Si la activación no puede publicarse, detente antes de generar el candidato:

```text
STOP / G5_F01_ACTIVATION_PUBLICATION_FAILED
```

---

## 3. Objetivo científico-documental exacto

La ficha G5-F01 exige:

> Definir qué resultados van a tablas principales, tablas secundarias, anexos y texto, sin recalcular ni seleccionar por conveniencia narrativa.

El producto de G5-F01 es una **arquitectura de presentación**, no las tablas finales.

La jerarquía debe derivarse de:

1. objetivos e hipótesis congelados;
2. rol primario/secundario/descriptivo/sensibilidad/no-estimable de la evidencia;
3. decisiones cerradas de G3 y G4;
4. necesidad de trazabilidad y comprensión;
5. limitaciones metodológicas aprobadas.

Está prohibido usar como criterio de jerarquización:

- que un resultado sea favorable;
- que una diferencia sea grande;
- que una tabla “se vea mejor”;
- que un resultado apoye narrativamente una conclusión deseada;
- ocultar resultados nulos, mixtos, negativos, descriptivos o no estimables.

---

## 4. Fuentes rectoras mínimas y blobs congelados

Usa exclusivamente evidencia ya integrada en `main`. No derives ciencia nueva.

### 4.1 Grupo 3

Como mínimo:

```text
outputs/analysis/group3/g3_analytical_contract_v0.1.json
blob = 4c8f9312ef1e9fb4e1c67c07dfd6aeff3ec42628

outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
blob = c63619b56a07e6b6d7be78b515d941ec3b205c41

outputs/analysis/group3/g3_metric_population_registry_v0.1.json
blob = 5ea33ca583b18426374fa15baf1b1759e76cd99e

outputs/analysis/group3/g3_inferential_results_v0.1.csv
blob = cf3d8d85e099a300330da0214836e70af7a02253

outputs/analysis/group3/g3_inferential_results_v0.1.json
blob = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc

outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
blob = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61
```

Los campos históricos internos `status=CANDIDATE_PENDING_EXTERNAL_AUDIT` de artefactos científicos son estado de generación y **no** reabren G3. La verdad operacional vigente es Plan + registro de fichas.

### 4.2 Grupo 4

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
blob = da0351cb523fc7f3b45a83e072765a07f809b7fe

outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
blob = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
blob = 129a67b15db429b86af059d61753b1942c8f243f

outputs/analysis/group4/g4_limitations_registry_v0.1.json
blob = ae00b93431e912cb78a58344057d9bf7a51fcd47

docs/analysis/group4/g4_literature_contrast_v0.1.md
blob = 2baff53184b17c23380693235a2f3257de5e2bba

outputs/audits/group4_closure_v0.1.json
blob = 64ccc2068c15d0890bb9b978de8ed63d6d891034
```

El JSON histórico de cierre G4 conserva `group4_closed=false` porque es el artefacto candidato generado antes de auditoría/cierre. No lo interpretes como estado operacional actual. El Plan y las fichas posteriores gobiernan:

```text
GROUP4 = CLOSED / APPROVED
G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
```

### 4.3 Otras fuentes científicas ya aprobadas

Puedes seguir las rutas exactas referidas desde los registros G3/G4 hacia outputs experimentales anteriores cuando sea necesario para identificar:

- denominadores;
- unidad analítica;
- definición de métricas;
- incertidumbre ya calculada;
- Attempt06 corregido;
- sensibilidad EXP11A;
- sensibilidad EXP11B;
- estado EXP12.

No uses outputs supersedidos como fuente de presentación final.

---

## 5. Contrato científico congelado que debe preservarse

Debe mantenerse sin reinterpretación:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION when dependency applies
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_SERIES = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Además:

```text
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Y siguen prohibidas las siguientes equivalencias:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_CORRECTNESS
AUDITABLE_EXPLANATION != LEGAL_CORRECTNESS
```

Las 11 limitaciones no bloqueantes de Grupo 2B permanecen vigentes cuando afecten la presentación o calificación de una familia.

---

## 6. Inventario de cobertura obligatorio antes de decidir presentación

Antes de asignar tablas o anexos, construye internamente dos inventarios:

### 6.1 Cobertura de familias G3

El registro G3-F02 contiene **16 familias de evidencia**. Todas deben quedar mapeadas en el output machine-readable a una decisión de presentación explícita.

Para cada familia registra como mínimo:

```text
evidence_family_id
scientific_role
hypothesis_or_objective_link
presentation_ids
presentation_disposition
reason
source_paths
source_blobs_or_row_ids
```

Ninguna familia puede desaparecer por no ser favorable.

Condición final:

```text
G3_EVIDENCE_FAMILY_EXPECTED_COUNT = 16
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G3_EVIDENCE_FAMILY_UNMAPPED_COUNT = 0
```

### 6.2 Cobertura de claims G4-F01

La matriz G4-F01 contiene **18 claims controlados**. Cada claim debe mapearse a:

- una presentación tabular;
- texto de resultados;
- anexo/suplemento;
- o `NOT_PRESENTED_AS_RESULT_WITH_REASON` si es un guardrail/limitación que no constituye un resultado tabulable.

Condición final:

```text
G4_CONTROLLED_CLAIM_EXPECTED_COUNT = 18
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
G4_CONTROLLED_CLAIM_UNMAPPED_COUNT = 0
```

No conviertas claims prohibidos o guardrails en resultados positivos.

---

## 7. Familias que deben recibir tratamiento explícito

Sin imponer de antemano un número de tablas, la arquitectura debe tratar explícitamente, al menos, estas familias:

1. rendimiento del retrieval histórico H100 dentro del benchmark congelado;
2. brazos normativos corregidos relevantes para HE2, usando exclusivamente Attempt06 actual;
3. inferencia primaria HE2_A y contraste primario HE2_B;
4. cobertura profunda / Phase E solo con su rol descriptivo aprobado;
5. EXP11A como sensibilidad conjunta tamaño/composición y no causal;
6. EXP11B H150/H200 como sensibilidad descriptiva sobre diez pares de seeds observados;
7. 0B-05C Attempt06 como sensibilidad correctiva dependiente del método;
8. componentes HE5 jerárquico y de precedentes únicamente en rol descriptivo;
9. componente de calidad de descripción HE5 como `NOT_ESTIMABLE`, no como cero ni ausencia de efecto;
10. límite de validez interna de HE5;
11. EXP12 como `CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE`;
12. diagnósticos/auditorías necesarios para interpretar claims, claramente separados de resultados de rendimiento.

### Regla EXP12

EXP12 **no** debe aparecer como fila de rendimiento con valores vacíos, cero, NA interpretables como medición, ni como condición comparable a H100/H150/H200.

Debe asignarse a una de estas formas:

```text
TEXT_ONLY_NOT_ESTIMABLE
APPENDIX_PROTOCOL_CLOSURE_NO_PERFORMANCE
```

Condición obligatoria:

```text
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0
```

---

## 8. Destinos de presentación permitidos

Cada `presentation_id` del registro debe usar exactamente uno de estos destinos:

```text
MAIN_TABLE
SECONDARY_TABLE
APPENDIX_TABLE
TEXT_ONLY
NOT_PRESENTED_AS_RESULT_WITH_REASON
```

Cada decisión debe indicar `selection_basis`, usando solo categorías como:

```text
PRIMARY_HYPOTHESIS
PRIMARY_OBJECTIVE
SECONDARY_HYPOTHESIS_OR_COMPONENT
DESCRIPTIVE_CONTEXT
SENSITIVITY_ANALYSIS
VALIDITY_LIMITATION
AUDIT_DIAGNOSTIC
NOT_ESTIMABLE
GUARDRAIL_NOT_A_RESULT
```

No se permite `FAVORABLE_RESULT`, `LARGE_EFFECT`, `BEST_METRIC`, `NARRATIVE_CONVENIENCE` ni equivalentes.

---

## 9. Contrato del plan humano

Crea:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
```

Debe contener como mínimo:

1. alcance y estado de gobernanza;
2. fuentes congeladas y precedencia de verdad;
3. principios de jerarquización no oportunista;
4. unidad de análisis, dependencia y alcance empírico;
5. mapa de familias experimentales;
6. arquitectura propuesta de tablas principales;
7. arquitectura propuesta de tablas secundarias;
8. arquitectura propuesta de anexos/suplementos;
9. resultados destinados a texto únicamente;
10. separación resultados vs diagnósticos/auditorías;
11. reglas de denominador, N, incertidumbre y versión fuente;
12. tratamiento explícito de HE2;
13. tratamiento explícito de HE5;
14. tratamiento explícito de EXP11A;
15. tratamiento explícito de EXP11B;
16. tratamiento explícito de Attempt06;
17. tratamiento explícito de EXP12;
18. material que G5-F02 deberá materializar;
19. material que G5-F02 no debe materializar;
20. guardrails contra cherry-picking y sobreclaim.

No redactes Results ni Discussion del artículo/tesis. El documento es un **plan de presentación**, no prosa final de manuscrito.

---

## 10. Contrato machine-readable del registro de tablas

Crea:

```text
outputs/results/group5/g5_table_registry_v0.1.json
```

Estructura mínima global:

```text
artifact_id
status
ficha
main_base
plan_snapshot
fichas_activation_commit
prompt94_commit
article_head_observed
scientific_scope
source_registry
presentation_registry
evidence_family_coverage
claim_coverage
validation
```

Cada entrada `presentation_registry` debe incluir al menos:

```text
presentation_id
title_working
presentation_destination
scientific_role
selection_basis
hypothesis_or_objective_link
claim_ids
evidence_family_ids
source_paths
source_blobs_or_row_ids
denominator_definition
unit_of_analysis
dependency_group
uncertainty_presentation
required_columns_or_content
mandatory_qualifications
materialize_in_g5_f02
superseded_sources_forbidden
rationale
```

### Regla de números en G5-F01

No materialices todavía las celdas finales de tablas. Puedes registrar denominadores, definiciones, métricas, IDs, campos fuente e incertidumbre ya aprobada para diseñar la estructura, pero las tablas científicas numéricas se materializan en G5-F02.

Condición:

```text
FINAL_NUMERIC_TABLE_MATERIALIZED_COUNT = 0
NEW_METRIC_VALUE_DERIVED_COUNT = 0
```

---

## 11. Reglas de denominadores e incertidumbre

Para toda presentación que contenga o vaya a contener números en G5-F02, el registro G5-F01 debe congelar explícitamente:

- unidad de análisis;
- denominador pertinente;
- población/subpoblación;
- agrupamiento por DAM cuando aplique;
- si la incertidumbre es inferencial, descriptiva o no aplicable;
- fuente exacta de la incertidumbre ya calculada;
- versión/blobs fuente.

No conviertas:

- `10 × 1056` observaciones EXP11B en observaciones inferenciales independientes;
- repeticiones EXP11A en evidencia causal de tamaño;
- resultados descriptivos HE5 en inferencia;
- `NOT_ESTIMABLE` en cero;
- ausencia de retrieval EXP12 en desempeño nulo.

---

## 12. Attempt06 y fuentes supersedidas

Toda familia relacionada con 0B-05C debe usar exclusivamente el estado corregido vigente:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1a = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
OVERALL = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

No uses Attempt03/04/05 ni interpretaciones supersedidas como fuente final de cifras o títulos.

Condición:

```text
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
0B05C_GLOBAL_ZERO_IMPACT_CLAIM_COUNT = 0
```

---

## 13. RPRE obligatorio de G5-F01

Antes del candidato, registra y exige `PASS` para:

```text
RPRE_G5_F01_SOURCE_CONTRACT
RPRE_G5_F01_GROUP4_CLOSED
RPRE_G5_F01_NO_NEW_SCIENCE
RPRE_G5_F01_NO_RECOMPUTATION
RPRE_G5_F01_NO_CHERRY_PICKING
RPRE_G5_F01_G3_FAMILY_COVERAGE
RPRE_G5_F01_G4_CLAIM_COVERAGE
RPRE_G5_F01_DENOMINATOR_PRESERVATION
RPRE_G5_F01_UNCERTAINTY_ROLE_PRESERVATION
RPRE_G5_F01_ATTEMPT06_CURRENT_ONLY
RPRE_G5_F01_EXP11A_NONCAUSAL
RPRE_G5_F01_EXP11B_DESCRIPTIVE_ONLY
RPRE_G5_F01_EXP12_NO_PERFORMANCE_ROW
RPRE_G5_F01_HE2_HE5_PRESERVATION
RPRE_G5_F01_RESULTS_VS_AUDITS_SEPARATION
RPRE_G5_F01_ARTICLE_READONLY
RPRE_G5_F02_NOT_STARTED
```

Si falla cualquiera:

```text
STOP / G5_F01_RPRE_FAILED
```

---

## 14. Rama candidata y topología obligatoria

Crea desde `origin/main` exactamente:

```text
branch = codex/group5-f01-results-presentation-architecture-v01
base = 38e22c19a0eb0d344e7675761a88d7968091eead
```

Debe contener exactamente **un commit científico-documental** y únicamente dos paths nuevos:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
outputs/results/group5/g5_table_registry_v0.1.json
```

Al final:

```text
G5_F01_COMMITS_AHEAD = 1
G5_F01_COMMITS_BEHIND = 0
G5_F01_CHANGED_PATH_COUNT = 2
```

No modifiques ningún output previo, script, configuración, Plan, artículo ni artefacto G3/G4 dentro de la rama candidata.

---

## 15. Validaciones obligatorias del candidato

El JSON debe incluir, como mínimo:

```text
G3_EVIDENCE_FAMILY_EXPECTED_COUNT = 16
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G3_EVIDENCE_FAMILY_UNMAPPED_COUNT = 0

G4_CONTROLLED_CLAIM_EXPECTED_COUNT = 18
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
G4_CONTROLLED_CLAIM_UNMAPPED_COUNT = 0

EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0
FAVORABILITY_BASED_SELECTION_COUNT = 0
UNJUSTIFIED_OMISSION_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
FINAL_NUMERIC_TABLE_MATERIALIZED_COUNT = 0
NEW_METRIC_VALUE_DERIVED_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
G5_F02_STARTED = false
```

Si alguno de los conteos de cobertura no cuadra, no reduzcas artificialmente el universo: corrige el mapeo o detente.

---

## 16. Estado del candidato

Los dos outputs deben quedar como:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G5-F01
GROUP5_CLOSED = false
G5_F02_AUTHORIZED = false
```

No integres a `main` durante Prompt94.

---

## 17. Actualización administrativa postejecución

Después de publicar y validar el candidato, actualiza exclusivamente:

```text
branch = docs/fichas-grupos-3-8
base = <commit de activación Prompt94>
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Deja:

```text
G5-F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G5-F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP5 = IN_PROGRESS
```

Añade bloque con:

```text
FICHA = G5-F01
PROMPT94_COMMIT = <source>
ACTIVATION_COMMIT = <activation>
CANDIDATE_COMMIT = <candidate>
CANDIDATE_PARENT = 38e22c19a0eb0d344e7675761a88d7968091eead
CHANGED_PATH_COUNT = 2
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
FAVORABILITY_BASED_SELECTION_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP5 = IN_PROGRESS
G5_F02_AUTHORIZED = false
G5_F02_STARTED = false
PENDING_EXTERNAL_AUDIT = true
```

No actualices todavía el Plan Maestro; el Plan se reconciliará solo después de auditoría externa y cierre/integración de G5-F01.

---

## 18. Verificación final obligatoria

Tras todos los push, ejecuta `git fetch origin` y verifica:

```text
origin/main = 38e22c19a0eb0d344e7675761a88d7968091eead
origin/docs/plan-maestro-temporal-2026-08-31 = 3ba3557eb10e741b8f49c420850940dee1df08ef

G5_F01_COMMITS_AHEAD = 1
G5_F01_COMMITS_BEHIND = 0
G5_F01_CHANGED_PATH_COUNT = 2

G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G3_EVIDENCE_FAMILY_UNMAPPED_COUNT = 0
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
G4_CONTROLLED_CLAIM_UNMAPPED_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
FAVORABILITY_BASED_SELECTION_COUNT = 0
UNJUSTIFIED_OMISSION_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
FINAL_NUMERIC_TABLE_MATERIALIZED_COUNT = 0
NEW_METRIC_VALUE_DERIVED_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
ARTICLE_MODIFIED = false
GROUP5 = IN_PROGRESS
G5_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F02_STARTED = false
```

Si la rama editorial avanzó concurrentemente, registra el nuevo HEAD; no lo trates como bloqueo mientras Prompt94 no haya modificado esa rama.

---

## 19. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/94_RESPUESTA_ACTIVAR_Y_EJECUTAR_G5_F01_ARQUITECTURA_PRESENTACION_RESULTADOS.md
```

El commit de respuesta debe añadir únicamente ese archivo.

Reporte terminal mínimo:

```text
PROMPT94 = COMPLETED

PREFLIGHT_MAIN = 38e22c19a0eb0d344e7675761a88d7968091eead
PREFLIGHT_PLAN = 3ba3557eb10e741b8f49c420850940dee1df08ef
PREFLIGHT_FICHAS = a2dc08c8ce5e4d3490e2600065ea6bd8b84b3830
ARTICLE_HEAD_PREFLIGHT = ...

ACTIVATION_COMMIT = ...
CANDIDATE_BRANCH = codex/group5-f01-results-presentation-architecture-v01
CANDIDATE_COMMIT = ...
CANDIDATE_PARENT = 38e22c19a0eb0d344e7675761a88d7968091eead
CANDIDATE_COMMITS_AHEAD = 1
CANDIDATE_COMMITS_BEHIND = 0
CANDIDATE_CHANGED_PATH_COUNT = 2
PRESENTATION_PLAN_BLOB = ...
TABLE_REGISTRY_BLOB = ...

G3_EVIDENCE_FAMILY_EXPECTED_COUNT = 16
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G3_EVIDENCE_FAMILY_UNMAPPED_COUNT = 0
G4_CONTROLLED_CLAIM_EXPECTED_COUNT = 18
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
G4_CONTROLLED_CLAIM_UNMAPPED_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0
FAVORABILITY_BASED_SELECTION_COUNT = 0
UNJUSTIFIED_OMISSION_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
FINAL_NUMERIC_TABLE_MATERIALIZED_COUNT = 0
NEW_METRIC_VALUE_DERIVED_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
ARTICLE_MODIFIED_BY_PROMPT94 = false

POSTEXEC_FICHAS_COMMIT = ...
G5_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP5 = IN_PROGRESS
G5_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F02_STARTED = false

ARTICLE_HEAD_FINAL_OBSERVED = ...
BLOCKERS = NONE
WARNINGS = ...
```

No afirmes `PASS`, `APPROVED`, `INTEGRATED` ni `CLOSED` para G5-F01: esos estados dependen de auditoría externa posterior.
