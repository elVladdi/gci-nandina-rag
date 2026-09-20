# PROMPT 90 — INTEGRAR Y CERRAR G4-F02 TRAS AUDITORÍA EXTERNA

## 0. Naturaleza y límite

La IA Experimental auditó externamente el candidato de **G4-F02 — Interpretación integrada y limitaciones** producido por Prompt89 y emitió `PASS`.

Esta ejecución es exclusivamente de **integración y cierre administrativo**. No puede crear ciencia nueva, recalcular métricas, recalcular inferencia, modificar interpretaciones aprobadas, redecidir HE2/HE5, contrastar literatura, redactar artículo/tesis ni activar G4-F03.

Estado de entrada esperado:

```text
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = IN_PROGRESS
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G4_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Objetivo único:

```text
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = IN_PROGRESS
G4_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

No cierres Grupo 4 y no avances a G4-F03.

---

## 1. Repositorio y refs exactos

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de modificar nada, ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 9f549ebdf940f9d806d5088697394d0c927f9fdc
origin/docs/plan-maestro-temporal-2026-08-31 = 2237ddc46bc1c7bfac203753bdcf2c7d4592f83e
origin/docs/fichas-grupos-3-8 = 15299783fe6fba30f0cfb02a491adeae8f99b118
origin/codex/group4-f02-interpretation-limitations-v01 = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
```

Prompt89 fuente:

```text
d9494b356cd00fcd97b8b338896df6e88aa279ac
```

Prompt89 response original:

```text
89e834743c83e56b74701c8c723cc9f303db44f0
```

Prompt89 response final tras corrección administrativa del HEAD editorial observado:

```text
5807bc5283fff4e4002969504f309bab900cf468
```

La corrección `5807bc...` solo actualizó metadata del reporte de Prompt89 y no modificó ciencia ni gobernanza experimental.

Artículo observado al diseñar Prompt90:

```text
origin/article/main-manuscript = 2491a532a21ca43b247a0d6ae11c5ceaeb1deda0
```

La rama editorial es solo observacional. Drift editorial concurrente no bloquea esta ejecución si Prompt90 no modifica esa rama.

Si `main`, Plan, fichas o candidato científico presentan drift no explicado:

```text
STOP / G4_F02_CLOSURE_REF_DRIFT
```

---

## 2. Candidato auditado e inmutable

Rama:

```text
codex/group4-f02-interpretation-limitations-v01
```

Commit candidato auditado:

```text
203770565e1a68c30ab3f27b912fc0fd971e4e8f
```

Padre exacto:

```text
9f549ebdf940f9d806d5088697394d0c927f9fdc
```

Debe continuar cumpliéndose:

```text
COMMITS_AHEAD_OF_MAIN = 1
COMMITS_BEHIND_MAIN = 0
CHANGED_PATH_COUNT = 2
```

Paths exactos:

```text
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
```

Blobs auditados:

```text
SYNTHESIS_BLOB = 129a67b15db429b86af059d61753b1942c8f243f
LIMITATIONS_REGISTRY_BLOB = ae00b93431e912cb78a58344057d9bf7a51fcd47
```

No modifiques, regeneres, reformatees, traduzcas ni normalices estos artefactos.

Verifica además que el candidato conserva, como mínimo:

```text
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_LIMITATION_IDS_COMPLETE = true
MISSING_LIMITATION_SOURCE_COUNT = 0
MISSING_MANDATORY_QUALIFICATION_COUNT = 0
MISSING_FORBIDDEN_OVERCLAIM_COUNT = 0
SUBSTANTIVE_STATEMENT_CLASSIFICATION_COMPLETE = true
SUBSTANTIVE_STATEMENT_TRACEABILITY_COMPLETE = true

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
G4_F03_STARTED = false
```

Verifica asimismo que los 11 IDs `G2B-L01` ... `G2B-L11` sigan presentes individualmente y que las dos limitaciones históricas irreversibles permanezcan separadas:

```text
G2B-L02 = unrecoverable historical EXP04-C runner
G2B-L03 = unrecoverable EXP08 v0.1 metadata
```

Si cualquier blob o condición difiere:

```text
STOP / AUDITED_G4_F02_CANDIDATE_CHANGED
```

---

## 3. Integración a `main`

Integra exclusivamente el commit candidato auditado mediante **fast-forward puro**.

Precondición:

```text
origin/main = 9f549ebdf940f9d806d5088697394d0c927f9fdc
candidate_parent = 9f549ebdf940f9d806d5088697394d0c927f9fdc
```

Después de la integración debe cumplirse exactamente:

```text
origin/main = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
```

No generes merge commit, squash, cherry-pick reconstruido ni commit científico adicional.

Tras push, vuelve a ejecutar `git fetch origin` y verifica:

```text
MAIN_FINAL = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
SYNTHESIS_BLOB_FINAL = 129a67b15db429b86af059d61753b1942c8f243f
LIMITATIONS_REGISTRY_BLOB_FINAL = ae00b93431e912cb78a58344057d9bf7a51fcd47
```

Si no coincide:

```text
STOP / G4_F02_FAST_FORWARD_INTEGRATION_FAILED
```

---

## 4. Cierre administrativo en registro de fichas

Trabaja desde:

```text
branch = docs/fichas-grupos-3-8
base = 15299783fe6fba30f0cfb02a491adeae8f99b118
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica únicamente ese archivo.

Actualiza la tabla a:

```text
G4-F01 = CLOSED / APPROVED
G4-F02 = CLOSED / APPROVED
G4-F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque de cierre que registre, como mínimo:

```text
FICHA = G4-F02
PROMPT89_COMMIT = d9494b356cd00fcd97b8b338896df6e88aa279ac
PROMPT89_RESPONSE_ORIGINAL_COMMIT = 89e834743c83e56b74701c8c723cc9f303db44f0
PROMPT89_RESPONSE_FINAL_COMMIT = 5807bc5283fff4e4002969504f309bab900cf468
ACTIVATION_COMMIT = c8f33eaa0b55ac6ce2e06bb464f9a6bcca8e1c69
CANDIDATE_COMMIT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
INTEGRATION_COMMIT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
FINAL_G4_F02_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = IN_PROGRESS
G4_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F03_AUTHORIZED = false
```

Haz un solo commit administrativo para este cierre y push normal.

No actives G4-F03.

---

## 5. Reconciliación del Plan Maestro

Trabaja desde:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = 2237ddc46bc1c7bfac203753bdcf2c7d4592f83e
file = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Modifica únicamente ese archivo.

Registra el nuevo estado canónico sin borrar ni reinterpretar cierres anteriores:

```text
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE

GROUP4 = IN_PROGRESS
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02_INTEGRATION_COMMIT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
G4_F02_EXTERNAL_AUDIT = PASS
G4_F02_GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
G4_F02_NEW_INFERENCE_PERFORMED = false
G4_F02_METRICS_RECOMPUTED = false
G4_F02_LITERATURE_CONTRAST_PERFORMED = false
NEXT_ELIGIBLE_FICHA = G4-F03
G4_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F03_AUTHORIZED = false
```

Preserva explícitamente las interpretaciones y límites aprobados por G4-F02:

- HE2 sigue `SUPPORTED`; no fue redecidida.
- HE5 sigue `INCONCLUSIVE`; no fue redecidida.
- EXP11A = sensibilidad conjunta tamaño/composición; no efecto causal aislado ni monotónico de tamaño.
- EXP11B = sensibilidad descriptiva H150/H200 en diez pares de seeds observados; no inferencia de superpoblación de seeds ni independencia de `10 x 1056` casos.
- 0B-05C = Attempt06 corregido vigente: EV03 cero agregado, EV04 pequeña disminución no nula de MRR, D1a cambio no nulo; está prohibido resumir el bloque como impacto numérico global cero.
- EXP12 = `CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH / DIVERSITY_EFFECT_NOT_ESTIMABLE`; no afirmar inviabilidad matemática global ni caracterizar seeds no ejecutadas.
- EXP12 no es evidencia positiva ni negativa de HE5.
- Grupo 2B conserva 11 limitaciones no bloqueantes; no declarar reproducibilidad perfecta.
- `HASH_BOUND_LOCAL_ONLY` no significa missing/unverified/invalid/unreproducible.
- `DECLARED_NOT_RECOVERABLE` no significa error experimental ni invalida resultados cerrados.
- retrieval histórico superior ≠ exactitud global del RAG.
- evidencia normativa ≠ corrección jurídica vinculante.
- explicación auditable ≠ clasificación o corrección legal.
- alcance empírico = benchmark interno offline de Clase 87.

No añadas resultados científicos nuevos.

Haz un solo commit administrativo del Plan y push normal.

---

## 6. Prohibiciones absolutas

No:

- modificar los dos artefactos G4-F02 auditados;
- recalcular métricas, agregados, CI, bootstrap o p-values;
- ejecutar experimentos o retrieval;
- redecidir HE2 o HE5;
- reformular como hallazgo una explicación plausible o especulación no soportada;
- modificar las 11 limitaciones aprobadas o combinarlas;
- reabrir EXP12;
- afirmar inviabilidad matemática global de EXP12;
- ejecutar búsqueda web o contraste con literatura;
- modificar `article/main-manuscript`;
- redactar artículo o tesis;
- activar o ejecutar G4-F03;
- cerrar Grupo 4;
- iniciar Grupo 5.

---

## 7. Verificación final obligatoria

Tras todos los push, ejecuta `git fetch origin` y verifica:

```text
MAIN_FINAL = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
SYNTHESIS_BLOB_FINAL = 129a67b15db429b86af059d61753b1942c8f243f
LIMITATIONS_REGISTRY_BLOB_FINAL = ae00b93431e912cb78a58344057d9bf7a51fcd47

G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = IN_PROGRESS
G4_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F03_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
LITERATURE_CONTRAST_PERFORMED = false
```

Verifica que `article/main-manuscript` no fue modificado por Prompt90. Si avanzó concurrentemente, registra la advertencia y el HEAD final observado.

---

## 8. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/90_RESPUESTA_INTEGRAR_Y_CERRAR_G4_F02_TRAS_AUDITORIA_EXTERNA.md
```

Ese commit de respuesta debe añadir únicamente dicho archivo.

Reporte terminal mínimo:

```text
PROMPT90 = COMPLETED

PREFLIGHT_MAIN = ...
PREFLIGHT_PLAN = ...
PREFLIGHT_FICHAS = ...
ARTICLE_HEAD_OBSERVED = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...
ARTICLE_MODIFIED_BY_PROMPT90 = false

G4_F02_CANDIDATE_COMMIT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
MAIN_FINAL = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
SYNTHESIS_BLOB_FINAL = 129a67b15db429b86af059d61753b1942c8f243f
LIMITATIONS_REGISTRY_BLOB_FINAL = ae00b93431e912cb78a58344057d9bf7a51fcd47
PLAN_CLOSURE_COMMIT = ...
FICHAS_CLOSURE_COMMIT = ...

G4_F02_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4_FINAL_STATE = IN_PROGRESS
G4_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F03_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
SCIENTIFIC_ARTIFACTS_MODIFIED = false
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
LITERATURE_CONTRAST_PERFORMED = false

BLOCKERS = NONE
WARNINGS = ...
```

Si cualquier precondición falla, no intentes reparar ciencia ni gobernanza por tu cuenta: detén la ejecución y reporta el bloqueo exacto.
