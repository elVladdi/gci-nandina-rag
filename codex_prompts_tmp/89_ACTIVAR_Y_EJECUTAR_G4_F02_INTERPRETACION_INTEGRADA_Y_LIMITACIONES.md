# PROMPT 89 — ACTIVAR Y EJECUTAR G4-F02: INTERPRETACIÓN INTEGRADA Y LIMITACIONES

## 0. Naturaleza, alcance y autorización

Esta ejecución corresponde exclusivamente a **G4-F02 — Interpretación integrada y limitaciones**.

La invocación explícita de este Prompt89 por el usuario constituye autorización únicamente para activar y ejecutar G4-F02. No autoriza G4-F03 ni ningún bloque posterior.

Estado de entrada esperado:

```text
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = IN_PROGRESS
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F03 = PROSPECTIVE / NOT_AUTHORIZED
```

Objetivo científico-documental único:

> Construir una síntesis interpretativa trazable y un registro explícito de limitaciones a partir de la evidencia ya aprobada, **sin producir ciencia nueva**, **sin recalcular resultados**, **sin redecidir hipótesis** y **sin incorporar todavía contraste con literatura**.

G4-F02 no redacta el artículo ni la tesis final. Produce artefactos de análisis controlado que servirán como fuente para los grupos posteriores.

---

## 1. Preflight obligatorio y refs congelados

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de escribir cualquier artefacto:

1. `git fetch origin`.
2. Verifica exactamente:

```text
origin/main = 9f549ebdf940f9d806d5088697394d0c927f9fdc
origin/docs/plan-maestro-temporal-2026-08-31 = 2237ddc46bc1c7bfac203753bdcf2c7d4592f83e
origin/docs/fichas-grupos-3-8 = 67a5205a1c96893b74e16b5e220ad7c29bc3a4af
```

Artículo observado al diseñar Prompt89:

```text
origin/article/main-manuscript = ad23623e177e3fcc6b231a655d733710b33b64c7
```

La rama editorial es **solo observacional**. Si avanza concurrentemente, registra el nuevo HEAD observado, pero no la modifiques y no uses ese drift como fuente experimental.

Si `main`, Plan o fichas presentan drift no explicado respecto de los refs anteriores:

```text
STOP / G4_F02_PREFLIGHT_REF_DRIFT
```

La ejecución debe registrar también el SHA exacto de Prompt89 recibido en la invocación del usuario.

---

## 2. Ficha gobernante y frontera con G4-F03

Lee íntegramente:

```text
docs/fichas/grupos_3_8/grupo_4/G4_F02_INTERPRETACION_INTEGRADA_Y_LIMITACIONES.md
```

en la rama:

```text
docs/fichas-grupos-3-8
```

Su contrato obligatorio es:

- distinguir **hallazgo**, **explicación plausible** y **especulación**;
- interpretar EXP11A como sensibilidad bajo composición natural, sin efecto causal aislado de tamaño;
- interpretar EXP11B únicamente en el alcance H150/H200 observado;
- incorporar Attempt06 como versión válida y vigente de 0B-05C;
- presentar EXP12 como precondición de planning fallida bajo búsqueda congelada, sin afirmar inviabilidad matemática global;
- integrar las 11 limitaciones no bloqueantes de Grupo 2B cuando sean relevantes;
- no contradecir Grupo 3 ni introducir inferencias causales o generalizaciones no autorizadas.

Lee también, únicamente para fijar la frontera de alcance:

```text
docs/fichas/grupos_3_8/grupo_4/G4_F03_CONTRASTE_LITERATURA_Y_CIERRE.md
```

**No ejecutes G4-F03.**

En particular, G4-F02 no puede:

- contrastar los resultados con literatura externa;
- decidir compatibilidad de métricas con estudios publicados;
- producir discussion points basados en literatura;
- buscar nuevas fuentes;
- usar web;
- cerrar Grupo 4.

Esas funciones corresponden a G4-F03.

---

## 3. RPRE obligatorio antes de la activación

Realiza una revisión preventiva de riesgos y registra al menos:

```text
RPRE_G4_F02_SOURCE_CONTRACT
RPRE_G4_F02_NO_NEW_SCIENCE
RPRE_G4_F02_FINDING_EXPLANATION_SPECULATION_BOUNDARY
RPRE_G4_F02_EXP11A_CAUSAL_GUARDRAIL
RPRE_G4_F02_EXP11B_SCOPE_GUARDRAIL
RPRE_G4_F02_0B05C_ATTEMPT06_CURRENT_STATE
RPRE_G4_F02_EXP12_FAIL_CLOSED_SEMANTICS
RPRE_G4_F02_GROUP2B_LIMITATION_COMPLETENESS
RPRE_G4_F02_G3_CONSISTENCY
RPRE_G4_F02_ARTICLE_ISOLATION
RPRE_G4_F02_G4_F03_NOT_STARTED
```

Todos deben resultar `PASS` antes de continuar.

Si alguno falla:

```text
STOP / G4_F02_RPRE_FAILED
```

No intentes resolver un fallo modificando ciencia previa.

---

## 4. Activación prospectiva obligatoria ANTES de producir la síntesis

La activación debe quedar materializada **antes de crear o modificar los outputs G4-F02**.

Trabaja sobre:

```text
branch = docs/fichas-grupos-3-8
base = 67a5205a1c96893b74e16b5e220ad7c29bc3a4af
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo y cambia:

```text
G4-F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G4-F03 = PROSPECTIVE / NOT_AUTHORIZED
```

Añade un bloque de activación con, como mínimo:

```text
FICHA = G4-F02
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT89_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
ACTIVATION_DATE = <fecha de ejecución>
MAIN_AT_ACTIVATION = 9f549ebdf940f9d806d5088697394d0c927f9fdc
PLAN_AT_ACTIVATION = 2237ddc46bc1c7bfac203753bdcf2c7d4592f83e
FICHAS_AT_ACTIVATION = 67a5205a1c96893b74e16b5e220ad7c29bc3a4af
ARTICLE_HEAD_OBSERVED = <HEAD observado>
PROMPT89_COMMIT = <SHA exacto recibido en la invocación>
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
G4_F03_AUTHORIZED = false
```

Haz un único commit de activación y push normal.

Después de `git fetch origin`, confirma que la activación está materializada en remoto.

Solo entonces puedes empezar la producción de los artefactos G4-F02.

---

## 5. Rama científica de trabajo

Desde el `main` congelado crea:

```text
branch = codex/group4-f02-interpretation-limitations-v01
base = 9f549ebdf940f9d806d5088697394d0c927f9fdc
```

La rama candidata debe contener **un solo commit científico/documental G4-F02** y quedar:

```text
COMMITS_AHEAD_OF_MAIN = 1
COMMITS_BEHIND_MAIN = 0
```

No integres esa rama a `main`. La integración solo podrá ocurrir después de auditoría externa independiente.

---

## 6. Fuentes permitidas y jerarquía de evidencia

### 6.1 Fuentes rectoras inmediatas

Usa como fuente primaria de claims y sus límites:

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
```

Blobs actualmente aprobados:

```text
CSV_BLOB = da0351cb523fc7f3b45a83e072765a07f809b7fe
JSON_BLOB = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab
```

No reformules el sentido de los 18 claims controlados de G4-F01 y no eleves su fuerza.

### 6.2 Fuentes Grupo 3

Puedes consultar para trazabilidad y contexto interpretativo:

```text
docs/analysis/group3/g3_claim_registry_v0.1.md
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
outputs/audits/group3_closure_v0.1.json
outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
outputs/analysis/group3/g3_inferential_results_v0.1.csv
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
```

Los estados científicos canónicos permanecen:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

G4-F02 **no los redecide**.

### 6.3 Grupo 2B — limitaciones y reproducibilidad

Para las limitaciones usa:

```text
docs/group2b_reproducibility_traceability_readiness_v0.2.md
outputs/audits/group2b_reproducibility_readiness_v0.2.json
```

Importante: esos artefactos conservan internamente su **estado histórico de candidato** al momento de generarse. No interpretes campos como `CANDIDATE_PENDING_EXTERNAL_AUDIT` o `group2b_closed=false` como estado operativo vigente.

El estado canónico actual se toma del Plan Maestro:

```text
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
BLOCKING_GAP_COUNT = 0
NONBLOCKING_LIMITATION_COUNT = 11
HISTORICAL_ONLY_COUNT = 5
ENVIRONMENT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
CLEAN_CHECKOUT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
SCIENTIFIC_REEXECUTION_REQUIRED = false
RESULTS_RECOMPUTATION_REQUIRED = false
```

No describas Group 2B como reproducibilidad perfecta.

---

## 7. Las 11 limitaciones no bloqueantes de Grupo 2B

El registro G4-F02 debe conservar de forma explícita **11 limitaciones separadas**. No combines las dos limitaciones históricas irreversibles en una sola fila.

Usa esta desagregación controlada:

```text
G2B-L01 = incomplete historical environment
G2B-L02 = unrecoverable historical EXP04-C runner
G2B-L03 = unrecoverable EXP08 v0.1 metadata
G2B-L04 = non-byte-exact LLM evaluation
G2B-L05 = EXP11A size/composition coupling
G2B-L06 = user-attested NUEVA_02 acquisition
G2B-L07 = local-only EXP11B banks and candidate ranking
G2B-L08 = portability runtime not independently rerun by the external auditor
G2B-L09 = local-only D1a weights
G2B-L10 = failed one-shot EXP12 planning outcome
G2B-L11 = non-governing nature of the EXP12 forensic diagnostic
```

Preserva su carácter **NONBLOCKING_DECLARED_LIMITATION** donde corresponda.

No transformes una limitación de reproducibilidad en un defecto de validez estadística si la fuente no lo establece.

No transformes `HASH_BOUND_LOCAL_ONLY` en “missing”, “unverified”, “invalid” o “unreproducible” sin evidencia adicional.

No transformes `DECLARED_NOT_RECOVERABLE` en “error experimental” ni en motivo para invalidar resultados ya cerrados.

---

## 8. Interpretaciones científicas obligatorias

### 8.1 HE2 y rendimiento

La síntesis puede afirmar únicamente lo ya permitido por G4-F01/G3:

- el retrieval histórico superó a flat normativo, hierarchical normativo y D1a corregido en las cinco métricas primarias HE2_A bajo el benchmark interno congelado;
- la cobertura hierarchical aumentó de Recall@100 a Recall@200 bajo el contraste HE2_B autorizado;
- Phase E mostró tendencia descriptiva consistente con mayor cobertura de pool a profundidades crecientes;
- Top-50 es suplementario y no cambia la decisión de HE2.

Debe conservarse:

```text
HE2 = SUPPORTED
```

Pero nunca inferir:

- exactitud end-to-end del RAG completo;
- superioridad causal del diseño;
- generalización a otros capítulos, aduanas, países o producción;
- corrección jurídica de los candidatos.

### 8.2 HE5

Debe conservarse:

```text
HE5 = INCONCLUSIVE
```

Razones mínimas que deben quedar explícitas:

- calidad/ambigüedad de descripción no fue operacionalizada como estimando de prevalencia;
- proximidad jerárquica solo tiene evidencia descriptiva y sin umbral congelado de concentración;
- soporte histórico usa buckets literales `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`, sin umbral prospectivo para “insuficiente”;
- el alcance empírico es interno, offline y limitado a Clase 87.

No conviertas ausencia de estimabilidad en evidencia a favor ni en contra de HE5.

### 8.3 EXP11A

Interpreta exclusivamente como:

```text
JOINT_BANK_SIZE_COMPOSITION_SENSITIVITY
NONCAUSAL
```

La composición natural cambia junto con el tamaño del banco.

Prohibido:

```text
isolated causal bank-size effect
monotonic causal effect of bank size
```

### 8.4 EXP11B

Interpreta únicamente los resultados descriptivos observados de H150/H200 y los diez pares de seeds aceptados.

Debe quedar explícito:

- las diez seeds no constituyen una superpoblación estadística congelada;
- `10 x 1056` no son observaciones independientes;
- no existe inferencia autorizada más allá de las condiciones H150/H200 observadas.

### 8.5 0B-05C

Usa exclusivamente el estado actual corregido Attempt06:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1A = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

Prohibido resumir 0B-05C como “sin impacto numérico” global.

No uses Attempts01–05 ni resultados no corregidos como estado actual.

### 8.6 EXP12

EXP12 debe describirse exclusivamente como:

```text
CLOSED_WITHOUT_RETRIEVAL
PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
D_HIGH_D_MID_D_LOW = NOT_SELECTED
DIVERSITY_EFFECT = NOT_ESTIMABLE
RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```

Puede afirmarse que la búsqueda congelada no produjo el mínimo de condiciones únicas factibles requerido por el diseño.

No puede afirmarse:

- inviabilidad matemática global;
- imposibilidad de cualquier diseño alternativo;
- caracterización de otras seeds no ejecutadas;
- que EXP12 demuestre o refute HE5;
- que el método haya sido “descartado” por Group2B;
- que deba reabrirse el diseño actual.

---

## 9. Taxonomía obligatoria: hallazgo, explicación plausible y especulación

Cada interpretación sustantiva de la síntesis debe clasificarse en una de estas tres categorías:

### `FINDING`

Solo cuando el enunciado está directamente soportado por un claim/resultado aprobado.

Debe incluir referencia trazable a `G3C-*`, `G4F01-*`, `G3F03-*` o `G3F02-*` según corresponda.

### `PLAUSIBLE_EXPLANATION`

Solo cuando la explicación es coherente con evidencia descriptiva aprobada pero **no fue causalmente identificada**.

Debe usar lenguaje condicional, por ejemplo:

```text
may be consistent with
could reflect
is compatible with
```

Debe señalar expresamente:

```text
CAUSAL_STATUS = NOT_ESTABLISHED
```

No introduzcas mecanismos no observados como si fueran hechos.

### `SPECULATION_NOT_SUPPORTED`

Ideas posibles pero no sustentadas por los artefactos actuales deben aparecer únicamente como límite de interpretación, nunca como claim utilizable.

Deben marcarse:

```text
DOWNSTREAM_USE = PROHIBITED_AS_EMPIRICAL_CLAIM
```

Si una afirmación no puede clasificarse de forma segura, colócala en esta categoría o elimínala.

---

## 10. Outputs exactos

Genera exactamente estos dos paths científicos/documentales en la rama candidata:

```text
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
```

No añadas otros archivos.

### 10.1 `g4_interpretation_synthesis_v0.1.md`

Debe contener, como mínimo:

1. `Scope and evidence boundary`.
2. `Approved findings`.
3. `Historical-bank sensitivity: EXP11A and EXP11B`.
4. `Corrective numerical state: 0B-05C Attempt06`.
5. `Negative / non-estimable evidence: HE5 and EXP12`.
6. `Finding / plausible explanation / speculation register`.
7. `Reproducibility and traceability limitations from Group2B`.
8. `Integrated limitations for downstream writing`.
9. `Forbidden interpretations / overclaims`.
10. `Handoff boundary to G4-F03`.

No escribas prosa de artículo lista para publicación. Debe ser un artefacto analítico y de gobernanza, no un borrador narrativo final.

### 10.2 `g4_limitations_registry_v0.1.json`

Debe contener:

```text
artifact_id
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G4-F02
input_refs
source_blobs
hypothesis_dispositions
rpre
limitations[]
validation
flags
```

Cada objeto de `limitations[]` debe incluir al menos:

```text
limitation_id
source_family
source_path
source_record_or_claim_ids
limitation_text_controlled
limitation_type
severity
current_status
interpretive_role
relevance_to_g4_f02
affected_claim_ids
allowed_statement
mandatory_qualification
forbidden_overclaim
downstream_sections
evidence_status
```

Las 11 limitaciones `G2B-L01 ... G2B-L11` deben existir como registros separados.

Puedes añadir limitaciones derivadas de G3/G4-F01 con IDs separados (`G4-Lxx`), pero **no las cuentes dentro de las 11 de Group2B**.

---

## 11. Validaciones mínimas obligatorias

El JSON debe incluir y satisfacer como mínimo:

```text
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_LIMITATION_IDS_UNIQUE = true
GROUP2B_LIMITATION_IDS_COMPLETE = true
MISSING_LIMITATION_SOURCE_COUNT = 0
MISSING_MANDATORY_QUALIFICATION_COUNT = 0
MISSING_FORBIDDEN_OVERCLAIM_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false

EXP11A_CAUSAL_SIZE_EFFECT_CLAIM_COUNT = 0
EXP11B_SEED_SUPERPOPULATION_INFERENCE_COUNT = 0
0B05C_SUPERSEDED_CURRENT_STATE_COUNT = 0
0B05C_GLOBAL_ZERO_IMPACT_CLAIM_COUNT = 0
EXP12_GLOBAL_INFEASIBILITY_CLAIM_COUNT = 0
EXP12_HE5_POSITIVE_EVIDENCE_COUNT = 0
EXP12_HE5_NEGATIVE_EVIDENCE_COUNT = 0

NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
LITERATURE_CONTRAST_PERFORMED = false
ARTICLE_MODIFIED = false
G4_F03_AUTHORIZED = false
G4_F03_STARTED = false
```

Además valida que todo enunciado sustantivo de la síntesis esté clasificado como `FINDING`, `PLAUSIBLE_EXPLANATION` o `SPECULATION_NOT_SUPPORTED` y tenga trazabilidad suficiente.

Si cualquier control falla, no publiques candidato:

```text
STOP / G4_F02_VALIDATION_FAILED
```

---

## 12. Prohibiciones absolutas

No:

- ejecutar experimentos;
- ejecutar retrieval, BM25, reranking o LLM;
- recalcular métricas;
- recalcular intervalos bootstrap;
- calcular p-values;
- crear nuevos contrastes;
- redecidir HE2 o HE5;
- reclasificar retrospectivamente buckets de soporte;
- crear una regla post-hoc de calidad/ambigüedad textual;
- convertir evidencia descriptiva en inferencia causal;
- generalizar fuera del benchmark interno Clase 87;
- reabrir EXP12;
- afirmar inviabilidad matemática global de EXP12;
- usar EXP12 como evidencia positiva o negativa de HE5;
- sustituir Attempt06 por intentos previos de 0B-05C;
- afirmar exactitud global del RAG a partir de retrieval histórico;
- afirmar corrección jurídica vinculante a partir de evidencia normativa;
- afirmar que una explicación auditable valida la clasificación;
- buscar, citar o contrastar literatura externa;
- modificar `article/main-manuscript`;
- modificar los artefactos aprobados de G3 o G4-F01;
- integrar el candidato a `main`;
- activar G4-F03;
- cerrar Grupo 4.

---

## 13. Commit candidato y verificación

El commit candidato debe contener exactamente dos paths:

```text
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
```

Después del commit y push, verifica:

```text
candidate_parent = 9f549ebdf940f9d806d5088697394d0c927f9fdc
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
```

Registra los blobs Git resultantes de ambos archivos.

No hagas merge ni fast-forward a `main`.

---

## 14. Estado postejecución en el registro de fichas

Solo después de materializar y verificar el candidato, vuelve a `docs/fichas-grupos-3-8` desde el commit de activación y modifica exclusivamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Deja:

```text
G4-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G4-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque que registre al menos:

```text
G4_F02_BRANCH = codex/group4-f02-interpretation-limitations-v01
G4_F02_CANDIDATE_COMMIT = <SHA>
G4_F02_CANDIDATE_PARENT = 9f549ebdf940f9d806d5088697394d0c927f9fdc
G4_F02_CHANGED_PATH_COUNT = 2
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
LITERATURE_CONTRAST_PERFORMED = false
PENDING_EXTERNAL_AUDIT = true
G4_F03_AUTHORIZED = false
RESULT = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

Haz un único commit postejecución y push normal.

No modifiques el Plan Maestro todavía. El Plan se reconciliará solo después de auditoría externa y cierre aprobado de G4-F02.

---

## 15. Aislamiento editorial

Antes y después de ejecutar, registra el HEAD de:

```text
origin/article/main-manuscript
```

Si cambia por actividad concurrente:

```text
ARTICLE_CONCURRENT_DRIFT = OBSERVED
ARTICLE_MODIFIED_BY_PROMPT89 = false
```

No inspecciones ese drift para alterar conclusiones experimentales.

No escribas en esa rama.

---

## 16. Persistencia de la respuesta

Crea exclusivamente en la rama:

```text
codex/prompts-temporary
```

el archivo:

```text
codex_prompts_tmp/89_RESPUESTA_ACTIVAR_Y_EJECUTAR_G4_F02_INTERPRETACION_INTEGRADA_Y_LIMITACIONES.md
```

El commit de respuesta debe añadir exclusivamente dicho archivo.

Reporte terminal mínimo:

```text
PROMPT89 = COMPLETED

PREFLIGHT_MAIN = 9f549ebdf940f9d806d5088697394d0c927f9fdc
PREFLIGHT_PLAN = 2237ddc46bc1c7bfac203753bdcf2c7d4592f83e
PREFLIGHT_FICHAS = 67a5205a1c96893b74e16b5e220ad7c29bc3a4af
ARTICLE_HEAD_OBSERVED = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...
ARTICLE_MODIFIED_BY_PROMPT89 = false

RPRE_G4_F02_SOURCE_CONTRACT = PASS
RPRE_G4_F02_NO_NEW_SCIENCE = PASS
RPRE_G4_F02_FINDING_EXPLANATION_SPECULATION_BOUNDARY = PASS
RPRE_G4_F02_EXP11A_CAUSAL_GUARDRAIL = PASS
RPRE_G4_F02_EXP11B_SCOPE_GUARDRAIL = PASS
RPRE_G4_F02_0B05C_ATTEMPT06_CURRENT_STATE = PASS
RPRE_G4_F02_EXP12_FAIL_CLOSED_SEMANTICS = PASS
RPRE_G4_F02_GROUP2B_LIMITATION_COMPLETENESS = PASS
RPRE_G4_F02_G3_CONSISTENCY = PASS
RPRE_G4_F02_ARTICLE_ISOLATION = PASS
RPRE_G4_F02_G4_F03_NOT_STARTED = PASS

G4_F02_ACTIVATION_COMMIT = ...
G4_F02_BRANCH = codex/group4-f02-interpretation-limitations-v01
G4_F02_CANDIDATE_COMMIT = ...
G4_F02_CANDIDATE_PARENT = 9f549ebdf940f9d806d5088697394d0c927f9fdc
G4_F02_COMMITS_AHEAD = 1
G4_F02_COMMITS_BEHIND = 0
G4_F02_CHANGED_PATH_COUNT = 2
G4_F02_CHANGED_PATHS = docs/analysis/group4/g4_interpretation_synthesis_v0.1.md; outputs/analysis/group4/g4_limitations_registry_v0.1.json
SYNTHESIS_BLOB = ...
LIMITATIONS_REGISTRY_BLOB = ...

GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_LIMITATION_IDS_COMPLETE = true
MISSING_LIMITATION_SOURCE_COUNT = 0
MISSING_MANDATORY_QUALIFICATION_COUNT = 0
MISSING_FORBIDDEN_OVERCLAIM_COUNT = 0
EXP11A_CAUSAL_SIZE_EFFECT_CLAIM_COUNT = 0
EXP11B_SEED_SUPERPOPULATION_INFERENCE_COUNT = 0
0B05C_SUPERSEDED_CURRENT_STATE_COUNT = 0
0B05C_GLOBAL_ZERO_IMPACT_CLAIM_COUNT = 0
EXP12_GLOBAL_INFEASIBILITY_CLAIM_COUNT = 0
EXP12_HE5_POSITIVE_EVIDENCE_COUNT = 0
EXP12_HE5_NEGATIVE_EVIDENCE_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
LITERATURE_CONTRAST_PERFORMED = false
G4_F03_STARTED = false

G4_F02_POSTEXEC_FICHAS_COMMIT = ...
G4_F02_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G4_F03_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED

BLOCKERS = NONE
WARNINGS = ...
```

Si existe cualquier bloqueo, responde con `PROMPT89 = BLOCKED` y el motivo exacto. No improvises reparaciones ni avances a G4-F03.
