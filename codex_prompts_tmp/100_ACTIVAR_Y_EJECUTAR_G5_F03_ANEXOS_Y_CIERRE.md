# PROMPT100 — ACTIVAR Y EJECUTAR G5-F03: ANEXOS Y CIERRE

## 0. Rol y alcance

Actúa exclusivamente como ejecutor técnico del flujo experimental del repositorio `elVladdi/gci-nandina-rag`.

Ejecuta **solo G5-F03 — Anexos y cierre**. Esta ejecución debe producir un **candidato documental de cierre del Grupo 5**, sujeto todavía a auditoría externa. No cierres operacionalmente G5-F03 ni Grupo 5 en este prompt.

Queda prohibido:

- ejecutar o activar G6-F01 o cualquier ficha posterior;
- recalcular métricas, intervalos, p-values o inferencia;
- ejecutar experimentos o retrieval;
- crear nuevas tablas científicas o alterar las nueve tablas canónicas de G5-F02;
- reabrir EXP12;
- modificar HE2=`SUPPORTED` o HE5=`INCONCLUSIVE`;
- modificar el artículo;
- realizar búsqueda bibliográfica nueva;
- introducir resultados o afirmaciones científicas nuevas;
- sustituir fuentes congeladas por versiones superseded;
- interpretar un cierre documental como nueva evidencia científica.

La autorización de esta ejecución proviene exclusivamente de la invocación explícita de Prompt100, bajo la instrucción permanente de continuación del usuario de 2026-09-20.

---

## 1. Workspace local obligatorio

Trabaja sobre el repositorio local canónico del usuario:

`C:/Users/Vladimir/OneDrive/Documentos/Maestría UNMSM/LLM_RGA_NANDINA`

Requisitos:

1. confirma que `origin` sea `https://github.com/elVladdi/gci-nandina-rag.git`;
2. no crees un worktree nuevo;
3. no borres, limpies, resetees ni sobrescribas cambios locales preexistentes ajenos a este prompt;
4. si algún cambio local intersecta un path que Prompt100 necesita modificar, **STOP / G5_F03_LOCAL_PATH_CONFLICT** antes de escribir;
5. los artefactos producidos deben persistir en esa carpeta canónica y publicarse en las ramas indicadas.

Los avisos de metadata de worktrees que no impidan leer/escribir los paths gobernados pueden registrarse como warning no bloqueante.

---

## 2. Refs congelados y preflight

Antes de modificar nada, ejecuta `git fetch --all --prune` cuando sea posible y verifica las refs remotas.

Refs experimentales esperadas:

```text
MAIN_BASE = e471d4336ab965cd55b7f0e2ca7926445b1f0391
PLAN_BASE = 996bd57efc92528863bc8b6401d3708a17e0b3b7
FICHAS_BASE = 9d2ae999a0aef2ed47823a65e00536a91da816c8
PROMPT99_RESPONSE = 1060e72a7ca10eca8f1dcf9b60f9b7ffd7d447be
ARTICLE_OBSERVED_AT_DESIGN = 7b442bd96098630b9bf5ae9938dd20b157a104fc
```

Debe cumplirse:

```text
origin/main == MAIN_BASE
origin/docs/plan-maestro-temporal-2026-08-31 == PLAN_BASE
origin/docs/fichas-grupos-3-8 == FICHAS_BASE
```

Si cualquiera de esas tres refs experimentales cambió de forma inesperada:

`STOP / G5_F03_REF_DRIFT`

La rama editorial es concurrente y de solo lectura para este prompt. Si `origin/article/main-manuscript` avanzó respecto de `ARTICLE_OBSERVED_AT_DESIGN`, registra el nuevo HEAD como warning informativo; no bloquees por ese hecho si Prompt100 no modifica la rama editorial.

Verifica además que Prompt99 dejó:

```text
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = IN_PROGRESS
G5_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03_AUTHORIZED = false
G5_F03_STARTED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

---

## 3. Contrato científico congelado

No alteres ninguno de estos estados:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE

UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION

EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Semántica obligatoria de 0B-05C Attempt06:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1a = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
OVERALL = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

No uses la frase o conclusión global “sin impacto numérico”.

HE5 permanece `INCONCLUSIVE` porque sus componentes congelados no autorizan una conclusión global más fuerte:

- calidad de descripción: `NOT_ESTIMABLE`;
- proximidad jerárquica: `DESCRIPTIVE_ONLY`;
- suficiencia de precedentes históricos: `DESCRIPTIVE_ONLY`;
- validez interna: `DOCUMENTED_LIMITATION`.

EXP12 no tiene fila de rendimiento, no tiene métrica de retrieval y no aporta evidencia positiva ni negativa para decidir HE5.

---

## 4. Fuentes G5 congeladas

### 4.1 G5-F01

Usa como arquitectura de presentación congelada:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
blob = 9eaf780f3a2f6c8579dc80867ed3a86e96683894

outputs/results/group5/g5_table_registry_v0.1.json
blob = 4fe9318d52fad093066ff9f42d524fc95e436245
```

Los campos históricos `CANDIDATE_PENDING_EXTERNAL_AUDIT` dentro de estos artefactos representan su estado al momento de generación y **no** reabren G5-F01, que operacionalmente está cerrado y aprobado.

La arquitectura materializable contiene exactamente nueve presentaciones tabulares:

```text
G5-MAIN-01
G5-MAIN-02
G5-SECONDARY-01
G5-SECONDARY-02
G5-APPENDIX-01
G5-APPENDIX-02
G5-APPENDIX-03
G5-APPENDIX-04
G5-APPENDIX-05
```

Las cinco presentaciones de apéndice son:

```text
G5-APPENDIX-01 = Top-50 supplementary uncertainty
G5-APPENDIX-02 = EXP11A joint size-composition sensitivity
G5-APPENDIX-03 = EXP11B paired H150/H200 sensitivity
G5-APPENDIX-04 = 0B-05C Attempt06 corrective sensitivity
G5-APPENDIX-05 = Phase E diagnostic union ceiling
```

G5-F01 también contiene destinos `TEXT_ONLY` y `NOT_PRESENTED_AS_RESULT_WITH_REASON`; deben conservarse como tales, no transformarse en tablas de rendimiento.

### 4.2 G5-F02

Usa exclusivamente la versión corregida integrada en `MAIN_BASE`:

```text
scripts/results/group5/materialize_g5_tables_v0_1.py
blob = a2dc9f87d87f5ef144c1279828b85704ad6c206b

docs/results/group5/g5_canonical_tables_v0.1.md
blob = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d

outputs/results/group5/g5_numeric_crosscheck_v0.1.json
blob = a28af8df10f6d6bb4fdb02458288b41e34e1dc78

outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
blob = 727076a0d09735a87f45f6522d2a0ecead2cee17
```

Comprueba que las nueve tablas canónicas existan y que el crosscheck conserve los cierres aprobados. No regeneres ni modifiques estas tablas.

En `G5-SECONDARY-02`, las tres filas jerárquicas HE5 deben seguir teniendo denominador vacío y conteos congelados:

```text
SAME_CHAPTER -> denominator="" ; error_count=147
SAME_HS4     -> denominator="" ; error_count=284
SAME_HS6     -> denominator="" ; error_count=87
```

No inventes denominadores para esas filas.

---

## 5. Objetivo específico de G5-F03

La ficha G5-F03 exige cerrar la **organización tabular y suplementaria** de resultados y decidir qué evidencia detallada debe conservarse en anexos o suplementos, sin ocultar resultados desfavorables, nulos, descriptivos o no estimables.

Prompt100 debe producir solo:

1. un registro humano de anexos y suplementos;
2. un artefacto machine-readable de auditoría de cierre candidato del Grupo 5.

No copies innecesariamente los datos de las tablas ya materializadas. El registro debe apuntar a sus paths, roles, fuentes y calificaciones.

### 5.1 Cobertura mínima obligatoria

El registro debe cubrir de forma explícita:

- las cinco tablas `G5-APPENDIX-01..05`;
- las nueve tablas canónicas de G5-F02 como sistema de presentación completo;
- la trazabilidad de las 16 familias de evidencia G3 ya mapeadas por G5-F01;
- la trazabilidad de los 18 claims controlados G4 ya mapeados por G5-F01;
- las salidas `TEXT_ONLY` y `NOT_PRESENTED_AS_RESULT_WITH_REASON` que sean necesarias para preservar límites y no estimabilidad;
- los resultados negativos, nulos, descriptivos y no estimables materialmente relevantes;
- las limitaciones de validez relevantes, incluyendo las 11 limitaciones no bloqueantes heredadas del cierre de Grupo 2B cuando afecten interpretación, reproducibilidad o trazabilidad;
- la separación entre resultados científicos y evidencia de auditoría/forense/diagnóstica.

### 5.2 Evidencia que no puede ocultarse ni promoverse indebidamente

Debes conservar visibilidad de:

- HE5=`INCONCLUSIVE`;
- calidad de descripción HE5=`NOT_ESTIMABLE`;
- jerarquía HE5=`DESCRIPTIVE_ONLY`;
- precedentes históricos HE5=`DESCRIPTIVE_ONLY`;
- validez interna como limitación documentada;
- EXP11A como sensibilidad conjunta tamaño/composición, no causal;
- EXP11B como diez pares de semillas observados, descriptivo, sin inferencia a superpoblación de semillas;
- 0B-05C Attempt06 con la semántica corregida exacta;
- Phase E/deep coverage como evidencia descriptiva cuando corresponda;
- EXP12 como cierre sin retrieval y efecto de diversidad no estimable, sin fila de rendimiento;
- diagnósticos y auditorías separados de métricas de rendimiento.

No eleves ninguna de estas piezas a evidencia confirmatoria si su rol congelado no lo permite.

---

## 6. RPRE obligatorio antes de activar G5-F03

Ejecuta y documenta las siguientes verificaciones. Todas deben resultar `PASS`:

```text
RPRE_G5_F03_SOURCE_CONTRACT
RPRE_G5_F03_G5_F01_CLOSED
RPRE_G5_F03_G5_F02_CLOSED
RPRE_G5_F03_NO_NEW_SCIENCE
RPRE_G5_F03_NO_NEW_TABLES
RPRE_G5_F03_NO_RECOMPUTATION
RPRE_G5_F03_NO_NEW_INFERENCE
RPRE_G5_F03_APPENDIX_PRESENTATION_COVERAGE
RPRE_G5_F03_G3_FAMILY_TRACEABILITY
RPRE_G5_F03_G4_CLAIM_TRACEABILITY
RPRE_G5_F03_NEGATIVE_NULL_NOT_ESTIMABLE_VISIBILITY
RPRE_G5_F03_ATTEMPT06_CURRENT_ONLY
RPRE_G5_F03_EXP11A_NONCAUSAL
RPRE_G5_F03_EXP11B_DESCRIPTIVE_ONLY
RPRE_G5_F03_EXP12_NO_PERFORMANCE
RPRE_G5_F03_HE2_HE5_PRESERVATION
RPRE_G5_F03_RESULTS_VS_AUDITS_SEPARATION
RPRE_G5_F03_GROUP2B_LIMITATION_VISIBILITY
RPRE_G5_F03_ARTICLE_READONLY
RPRE_G5_F03_G6_NOT_STARTED
```

Si falla cualquiera:

`STOP / G5_F03_RPRE_FAILED`

No publiques activación ni candidato si el RPRE falla.

---

## 7. Activación gobernada de G5-F03

Solo después de RPRE PASS:

Rama:
`docs/fichas-grupos-3-8`

Base exacta:
`9d2ae999a0aef2ed47823a65e00536a91da816c8`

Modifica exclusivamente:
`docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md`

Publica un único commit de activación que registre al menos:

```text
FICHA = G5-F03
AUTHORIZATION_BASIS = PROMPT100_EXPLICIT_EXECUTION / STANDING_CONTINUATION_INSTRUCTION_2026-09-20
MAIN_BASE = e471d4336ab965cd55b7f0e2ca7926445b1f0391
PLAN_BASE = 996bd57efc92528863bc8b6401d3708a17e0b3b7
FICHAS_BASE = 9d2ae999a0aef2ed47823a65e00536a91da816c8
ARTICLE_HEAD_OBSERVED = <HEAD observado>
PROMPT100_SOURCE = <commit exacto de este prompt invocado por el usuario>
G5_F03 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
GROUP5 = IN_PROGRESS
G6_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

No modifiques el Plan Maestro en Prompt100.

Si la publicación del commit de activación falla:

`STOP / G5_F03_ACTIVATION_PUBLICATION_FAILED`

No generes el candidato si la activación no quedó publicada.

---

## 8. Candidato G5-F03

Crea o usa únicamente la rama:

`codex/group5-f03-appendix-closure-v01`

Base exacta:
`e471d4336ab965cd55b7f0e2ca7926445b1f0391`

La rama candidata debe quedar:

```text
COMMITS_AHEAD = 1
COMMITS_BEHIND = 0
```

Debe añadir **exactamente dos paths nuevos** y no modificar ningún otro archivo:

```text
docs/results/group5/g5_appendix_registry_v0.1.md
outputs/audits/group5_closure_v0.1.json
```

No modifiques los artefactos de G5-F01 o G5-F02.

### 8.1 `g5_appendix_registry_v0.1.md`

El documento humano debe incluir, como mínimo:

1. alcance y estado de gobernanza;
2. fuentes congeladas y versiones;
3. criterio de inclusión en anexo/suplemento;
4. catálogo de las cinco tablas `G5-APPENDIX-01..05`;
5. relación de las nueve tablas canónicas con principal/secundaria/apéndice;
6. evidencia `TEXT_ONLY` y guardrails que no deben convertirse en resultados tabulares;
7. trazabilidad y auditoría que debe conservarse sin confundirse con rendimiento;
8. resultados negativos, nulos, descriptivos y no estimables que deben permanecer visibles;
9. limitaciones de reproducibilidad/validez materialmente relevantes;
10. reglas para no usar fuentes superseded;
11. reglas específicas de HE2, HE5, EXP11A, EXP11B, 0B-05C Attempt06 y EXP12;
12. handoff explícito a Grupo 6 sin autorizarlo;
13. declaración de que el cierre todavía depende de auditoría externa.

No redactes una sección del artículo ni una sección narrativa final de la tesis.

### 8.2 `group5_closure_v0.1.json`

Debe ser JSON válido y contener al menos:

```text
artifact_id
status
ficha
main_base
plan_snapshot
fichas_activation_commit
prompt100_commit
article_head_observed
source_registry
appendix_registry
required_visibility_registry
presentation_coverage
limitation_coverage
validation
candidate_group5_closure_disposition
GROUP5_CLOSED
G6_F01_AUTHORIZED
```

Valores de gobernanza obligatorios:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G5-F03
candidate_group5_closure_disposition = APPROVABLE_FOR_GROUP5_CLOSURE_PENDING_EXTERNAL_AUDIT
GROUP5_CLOSED = false
G6_F01_AUTHORIZED = false
```

Cada entrada de `appendix_registry` debe contener al menos:

```text
appendix_id
title_working
content_type
scientific_role
source_paths
source_blobs_or_ids
related_presentation_ids
related_claim_ids
related_evidence_family_ids
inclusion_reason
mandatory_qualifications
is_scientific_result
is_audit_or_traceability
retention_destination
superseded_sources_forbidden
```

No inventes IDs científicos nuevos para reemplazar IDs existentes de G3/G4/G5. Los IDs documentales de registro pueden ser nuevos si son inequívocamente de G5-F03.

---

## 9. Validaciones obligatorias del candidato

El JSON de cierre debe derivar y reportar como mínimo:

```text
EXPECTED_CANONICAL_TABLE_PRESENTATION_COUNT = 9
ACCOUNTED_CANONICAL_TABLE_PRESENTATION_COUNT = 9
UNACCOUNTED_CANONICAL_TABLE_PRESENTATION_COUNT = 0

EXPECTED_APPENDIX_TABLE_PRESENTATION_COUNT = 5
ACCOUNTED_APPENDIX_TABLE_PRESENTATION_COUNT = 5
UNACCOUNTED_APPENDIX_TABLE_PRESENTATION_COUNT = 0

G3_EVIDENCE_FAMILY_EXPECTED_COUNT = 16
G3_EVIDENCE_FAMILY_TRACEABLE_COUNT = 16
G3_EVIDENCE_FAMILY_UNTRACEABLE_COUNT = 0

G4_CONTROLLED_CLAIM_EXPECTED_COUNT = 18
G4_CONTROLLED_CLAIM_TRACEABLE_COUNT = 18
G4_CONTROLLED_CLAIM_UNTRACEABLE_COUNT = 0

EXISTING_CANONICAL_TABLE_MODIFICATION_COUNT = 0
NEW_SCIENTIFIC_TABLE_CREATED_COUNT = 0
NEW_SCIENTIFIC_METRIC_VALUE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false

EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0
EXP12_REOPENED = false

ARTICLE_MODIFIED = false
G6_F01_STARTED = false
G6_F01_AUTHORIZED = false
GROUP5_CLOSED = false
```

También debe existir evidencia machine-readable de que:

```text
HE5_DESCRIPTION_NOT_ESTIMABLE_VISIBLE = true
HE5_HIERARCHY_DESCRIPTIVE_ONLY_VISIBLE = true
HE5_PRECEDENT_SUPPORT_DESCRIPTIVE_ONLY_VISIBLE = true
HE5_INTERNAL_VALIDITY_LIMITATION_VISIBLE = true
EXP11A_NONCAUSAL_QUALIFICATION_VISIBLE = true
EXP11B_NO_SUPERPOPULATION_QUALIFICATION_VISIBLE = true
ATTEMPT06_CURRENT_SEMANTICS_VISIBLE = true
EXP12_CLOSED_WITHOUT_RETRIEVAL_VISIBLE = true
RESULTS_AND_AUDITS_SEPARATED = true
GROUP2B_NONBLOCKING_LIMITATIONS_ACCOUNTED = true
```

Los contadores y booleanos deben derivarse de verificaciones reales sobre los artefactos y registros; no los fijes como PASS sin comprobarlos.

Si alguna condición obligatoria falla:

`STOP / G5_F03_CANDIDATE_VALIDATION_FAILED`

---

## 10. Publicación del candidato

Publica la rama candidata con un solo commit sobre `MAIN_BASE`.

Comprueba después de publicar:

- parent exacto = `MAIN_BASE`;
- un commit ahead;
- cero commits behind;
- exactamente dos paths añadidos;
- blobs exactos de ambos outputs;
- ningún artefacto científico previo modificado.

No integres el candidato a `main` en Prompt100.

---

## 11. Registro post-ejecución en fichas

Después de publicar y validar el candidato, vuelve a `docs/fichas-grupos-3-8` partiendo del commit de activación generado en §7.

Modifica exclusivamente:
`docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md`

Añade un bloque post-ejecución que registre al menos:

```text
FICHA = G5-F03
PROMPT100_SOURCE = <commit exacto>
CANDIDATE_BRANCH = codex/group5-f03-appendix-closure-v01
CANDIDATE_COMMIT = <sha>
APPENDIX_REGISTRY_BLOB = <blob>
GROUP5_CLOSURE_CANDIDATE_BLOB = <blob>
RPRE = PASS
CANDIDATE_VALIDATION = PASS
G5_F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP5 = IN_PROGRESS
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
G6_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
PENDING_EXTERNAL_AUDIT = true
```

No marques G5-F03 `CLOSED` o `APPROVED`.
No marques Group5 `CLOSED`.
No autorices G6-F01.
No modifiques el Plan Maestro todavía.

---

## 12. Inmutabilidad editorial y de ciencia

Durante Prompt100:

```text
ARTICLE_MODIFIED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
NEW_CI_CALCULATED = false
P_VALUES_CALCULATED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
```

Cualquier drift editorial concurrente debe quedar solo como observación, nunca como commit de Prompt100.

---

## 13. Respuesta oficial

Persiste la respuesta en:

`codex_prompts_tmp/100_RESPUESTA_ACTIVAR_Y_EJECUTAR_G5_F03_ANEXOS_Y_CIERRE.md`

en la rama `codex/prompts-temporary`.

El commit de respuesta debe añadir **solo** ese archivo de respuesta.

Reporta, como mínimo:

```text
PROMPT100 = COMPLETED | STOPPED

WORKSPACE_ROOT_OBSERVED = ...
WORKSPACE_ORIGIN_URL = ...
WORKSPACE_INITIAL_BRANCH = ...
WORKSPACE_INITIAL_HEAD = ...
WORKSPACE_INITIAL_DIRTY_COUNT = ...
WORKTREE_LIST_OBSERVED = ...
USER_CANONICAL_LOCAL_PATH_FROZEN = true|false
LOCAL_PERSISTENCE_IN_USER_FOLDER_ASSERTED = true|false

PREFLIGHT_MAIN = ...
PREFLIGHT_PLAN = ...
PREFLIGHT_FICHAS = ...
ARTICLE_HEAD_PREFLIGHT = ...
PROMPT100_COMMIT = ...

RPRE_G5_F03_SOURCE_CONTRACT = PASS|FAIL
RPRE_G5_F03_G5_F01_CLOSED = PASS|FAIL
RPRE_G5_F03_G5_F02_CLOSED = PASS|FAIL
RPRE_G5_F03_NO_NEW_SCIENCE = PASS|FAIL
RPRE_G5_F03_NO_NEW_TABLES = PASS|FAIL
RPRE_G5_F03_NO_RECOMPUTATION = PASS|FAIL
RPRE_G5_F03_NO_NEW_INFERENCE = PASS|FAIL
RPRE_G5_F03_APPENDIX_PRESENTATION_COVERAGE = PASS|FAIL
RPRE_G5_F03_G3_FAMILY_TRACEABILITY = PASS|FAIL
RPRE_G5_F03_G4_CLAIM_TRACEABILITY = PASS|FAIL
RPRE_G5_F03_NEGATIVE_NULL_NOT_ESTIMABLE_VISIBILITY = PASS|FAIL
RPRE_G5_F03_ATTEMPT06_CURRENT_ONLY = PASS|FAIL
RPRE_G5_F03_EXP11A_NONCAUSAL = PASS|FAIL
RPRE_G5_F03_EXP11B_DESCRIPTIVE_ONLY = PASS|FAIL
RPRE_G5_F03_EXP12_NO_PERFORMANCE = PASS|FAIL
RPRE_G5_F03_HE2_HE5_PRESERVATION = PASS|FAIL
RPRE_G5_F03_RESULTS_VS_AUDITS_SEPARATION = PASS|FAIL
RPRE_G5_F03_GROUP2B_LIMITATION_VISIBILITY = PASS|FAIL
RPRE_G5_F03_ARTICLE_READONLY = PASS|FAIL
RPRE_G5_F03_G6_NOT_STARTED = PASS|FAIL

ACTIVATION_FICHAS_COMMIT = ...

CANDIDATE_BRANCH = codex/group5-f03-appendix-closure-v01
CANDIDATE_COMMIT = ...
CANDIDATE_PARENT = ...
CANDIDATE_COMMITS_AHEAD = ...
CANDIDATE_COMMITS_BEHIND = ...
CANDIDATE_CHANGED_PATH_COUNT = ...
APPENDIX_REGISTRY_BLOB = ...
GROUP5_CLOSURE_CANDIDATE_BLOB = ...

EXPECTED_CANONICAL_TABLE_PRESENTATION_COUNT = 9
ACCOUNTED_CANONICAL_TABLE_PRESENTATION_COUNT = ...
UNACCOUNTED_CANONICAL_TABLE_PRESENTATION_COUNT = ...
EXPECTED_APPENDIX_TABLE_PRESENTATION_COUNT = 5
ACCOUNTED_APPENDIX_TABLE_PRESENTATION_COUNT = ...
UNACCOUNTED_APPENDIX_TABLE_PRESENTATION_COUNT = ...
G3_EVIDENCE_FAMILY_TRACEABLE_COUNT = ...
G4_CONTROLLED_CLAIM_TRACEABLE_COUNT = ...
EXISTING_CANONICAL_TABLE_MODIFICATION_COUNT = ...
NEW_SCIENTIFIC_TABLE_CREATED_COUNT = ...
NEW_SCIENTIFIC_METRIC_VALUE_COUNT = ...
NEW_INFERENCE_COUNT = ...
NEW_CI_COUNT = ...
NEW_P_VALUE_COUNT = ...
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = ...
EXP12_PERFORMANCE_TABLE_ROW_COUNT = ...
EXP12_FABRICATED_METRIC_COUNT = ...

HE5_DESCRIPTION_NOT_ESTIMABLE_VISIBLE = true|false
HE5_HIERARCHY_DESCRIPTIVE_ONLY_VISIBLE = true|false
HE5_PRECEDENT_SUPPORT_DESCRIPTIVE_ONLY_VISIBLE = true|false
HE5_INTERNAL_VALIDITY_LIMITATION_VISIBLE = true|false
EXP11A_NONCAUSAL_QUALIFICATION_VISIBLE = true|false
EXP11B_NO_SUPERPOPULATION_QUALIFICATION_VISIBLE = true|false
ATTEMPT06_CURRENT_SEMANTICS_VISIBLE = true|false
EXP12_CLOSED_WITHOUT_RETRIEVAL_VISIBLE = true|false
RESULTS_AND_AUDITS_SEPARATED = true|false
GROUP2B_NONBLOCKING_LIMITATIONS_ACCOUNTED = true|false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
NEW_CI_CALCULATED = false
P_VALUES_CALCULATED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false

POSTEXECUTION_FICHAS_COMMIT = ...
G5_F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP5 = IN_PROGRESS
G6_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false

WORKSPACE_FINAL_BRANCH = ...
WORKSPACE_FINAL_HEAD = ...
WORKSPACE_FINAL_DIRTY_COUNT = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...
BLOCKERS = ...
WARNINGS = ...
```

No declares `PASS`, `APPROVED`, `CLOSED` o `INTEGRATED` como resultado de auditoría externa. Prompt100 solo ejecuta y deja el candidato pendiente de auditoría independiente.