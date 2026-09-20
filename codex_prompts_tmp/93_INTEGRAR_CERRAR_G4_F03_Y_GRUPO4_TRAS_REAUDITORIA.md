# PROMPT 93 — INTEGRAR G4-F03 CORREGIDO Y CERRAR GRUPO 4 TRAS REAUDITORÍA EXTERNA

## 0. Naturaleza y alcance

Esta ejecución es exclusivamente de **integración administrativa y cierre** después de la reauditoría externa satisfactoria del candidato corregido G4-F03 v02.

Estado externo gobernante al diseñar este prompt:

```text
PROMPT92_EXTERNAL_AUDIT = PASS
G4_F03_CORRECTION_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
G4_F03 = APPROVABLE_FOR_INTEGRATION_AND_CLOSURE
GROUP4 = IN_PROGRESS / NOT_CLOSED
G5_F01_AUTHORIZED = false
```

Esta ejecución autoriza únicamente:

1. integrar por fast-forward exacto el candidato corregido G4-F03 v02 a `main`;
2. cerrar administrativamente G4-F03;
3. cerrar administrativamente Grupo 4;
4. reconciliar el Plan Maestro;
5. dejar G5-F01 como **ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED**.

No autoriza:

- activar ni ejecutar G5-F01;
- iniciar Grupo 5;
- recalcular métricas, inferencia, bootstrap, CI o p-values;
- ejecutar experimentos o retrieval;
- reabrir EXP12;
- buscar literatura nueva;
- modificar el artículo;
- modificar el contenido científico de los artefactos auditados de G4-F03.

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
origin/docs/fichas-grupos-3-8 = 49b70a4fa8d4d7831fc8db06853d9004a564ec86
origin/codex/group4-f03-literature-contrast-closure-v02 = 38e22c19a0eb0d344e7675761a88d7968091eead
origin/codex/group4-f03-literature-contrast-closure-v01 = d8d04c3d516e429fd9117b09fc790a5afb9267c2
```

Gobernanza de ejecución y corrección:

```text
PROMPT91_SOURCE = a78a6ba29a12dfa505de0f22515ab142e0dffeb6
PROMPT91_RESPONSE = 9fe0f8cee64b1c8b37bd0bd106401bdb898b1b5a
PROMPT91_ACTIVATION_COMMIT = 16d84dfc3284c684cb6c7ecabc1763d435fa27d3
PROMPT91_POSTEXEC_FICHAS_COMMIT = 5a1d18690c1ea2eb94aa11d1372221389f32468b
G4_F03_SUPERSEDED_CANDIDATE_V01 = d8d04c3d516e429fd9117b09fc790a5afb9267c2

PROMPT92_SOURCE = 65bf62335feae79efa782fdc6b890b096f6e0e90
PROMPT92_RESPONSE = f8e6ff308011b1d3e06476cd79f4b056884f5ce8
PROMPT92_POSTCORRECTION_FICHAS_COMMIT = 49b70a4fa8d4d7831fc8db06853d9004a564ec86
G4_F03_CURRENT_CANDIDATE_V02 = 38e22c19a0eb0d344e7675761a88d7968091eead
```

Artículo observado al diseñar Prompt93:

```text
origin/article/main-manuscript = 88a3570fbc8c91af5f06798dcd82e2157121f394
```

La rama editorial es solo observacional y de solo lectura. Si avanza concurrentemente, registra el nuevo HEAD como advertencia no bloqueante, siempre que Prompt93 no la modifique.

Si `main`, Plan, fichas o candidato v02 presentan drift no explicado:

```text
STOP / G4_F03_CLOSURE_REF_DRIFT
```

---

## 2. RPRE de cierre obligatorio

Antes de modificar cualquier rama, registra y exige `PASS` para:

```text
RPRE_G4_F03_V02_EXTERNAL_AUDIT_PASS
RPRE_G4_F03_V02_PARENT_EQUALS_MAIN
RPRE_G4_F03_V02_ONE_COMMIT_AHEAD_ZERO_BEHIND
RPRE_G4_F03_V02_EXACT_TWO_PATHS
RPRE_G4_F03_V02_BLOBS_FROZEN
RPRE_G4_F03_V01_NOT_INTEGRATED
RPRE_G4_F03_NO_NEW_SCIENCE
RPRE_G4_F03_HE2_HE5_PRESERVATION
RPRE_G4_F03_GROUP4_CLOSURE_ONLY
RPRE_G5_F01_NOT_AUTHORIZED
RPRE_ARTICLE_READONLY
```

Si cualquiera falla:

```text
STOP / G4_F03_CLOSURE_RPRE_FAILED
```

---

## 3. Invariantes del candidato corregido v02

Verifica independientemente:

```text
CANDIDATE = 38e22c19a0eb0d344e7675761a88d7968091eead
PARENT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
COMMITS_AHEAD = 1
COMMITS_BEHIND = 0
CHANGED_PATH_COUNT = 2
```

Paths únicos:

```text
docs/analysis/group4/g4_literature_contrast_v0.1.md
outputs/audits/group4_closure_v0.1.json
```

Blobs auditados e inmutables:

```text
G4_F03_LITERATURE_CONTRAST_BLOB = 2baff53184b17c23380693235a2f3257de5e2bba
G4_F03_GROUP4_CLOSURE_CANDIDATE_BLOB = 64ccc2068c15d0890bb9b978de8ed63d6d891034
```

El candidato v01 `d8d04c3d...` permanece como historia auditable supersedida y **no debe integrarse**.

Verifica en el JSON v02, como mínimo:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
group4_closed = false
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
G5_F01_STARTED = false
```

El `status` y `group4_closed=false` son estados históricos del artefacto al ser generado; no los edites para reflejar el cierre operativo posterior.

---

## 4. Integración exacta a `main`

Integra `38e22c19a0eb0d344e7675761a88d7968091eead` a `main` mediante **fast-forward exacto**.

Precondición:

```text
origin/main = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
candidate_parent = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
```

Después de integrar debe cumplirse:

```text
origin/main = 38e22c19a0eb0d344e7675761a88d7968091eead
```

Prohibido:

- merge commit;
- squash;
- cherry-pick reconstruido;
- commit científico adicional;
- regenerar, reformatear o editar los dos artefactos.

Después del fast-forward verifica nuevamente los blobs exactos:

```text
docs/analysis/group4/g4_literature_contrast_v0.1.md
  = 2baff53184b17c23380693235a2f3257de5e2bba

outputs/audits/group4_closure_v0.1.json
  = 64ccc2068c15d0890bb9b978de8ed63d6d891034
```

---

## 5. Cierre administrativo de G4-F03 y Grupo 4

Trabaja en:

```text
branch = docs/fichas-grupos-3-8
base = 49b70a4fa8d4d7831fc8db06853d9004a564ec86
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo.

Actualiza la tabla operativa a:

```text
G4-F03 = CLOSED / APPROVED
G5-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5-F02 = PROSPECTIVE
G5-F03 = PROSPECTIVE
```

Añade un bloque de cierre que contenga, como mínimo:

```text
FICHA = G4-F03
PROMPT91_SOURCE = a78a6ba29a12dfa505de0f22515ab142e0dffeb6
PROMPT91_RESPONSE = 9fe0f8cee64b1c8b37bd0bd106401bdb898b1b5a
PROMPT92_SOURCE = 65bf62335feae79efa782fdc6b890b096f6e0e90
PROMPT92_RESPONSE = f8e6ff308011b1d3e06476cd79f4b056884f5ce8
SUPERSEDED_CANDIDATE_V01 = d8d04c3d516e429fd9117b09fc790a5afb9267c2
CURRENT_CANDIDATE_V02 = 38e22c19a0eb0d344e7675761a88d7968091eead
EXTERNAL_REAUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
INTEGRATION_COMMIT = 38e22c19a0eb0d344e7675761a88d7968091eead
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
FINAL_G4_F03_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = CLOSED / APPROVED
G5_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F01_AUTHORIZED = false
G5_F01_STARTED = false
```

Haz un único commit administrativo para esta rama.

---

## 6. Reconciliación del Plan Maestro

Trabaja en:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = 89fe5a0c13c8cad03e49280dc2a3edec8bc14a0b
file = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Modifica exclusivamente ese archivo.

Reconciliación obligatoria:

```text
Grupo 3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE

Grupo 4 = CLOSED / APPROVED
G4-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4-F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4-F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4-F03_INTEGRATION_COMMIT = 38e22c19a0eb0d344e7675761a88d7968091eead
G4-F03_EXTERNAL_REAUDIT = PASS
G4-F03_COMPARISON_REGISTRY_COUNT = 11
G4-F03_AUTHORIZED_DISCUSSION_POINT_COUNT = 8
G4-F03_FORBIDDEN_DISCUSSION_POINT_COUNT = 14

Grupo 5 = NOT_STARTED
G5-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Actualiza la fecha de actualización del Plan a `2026-09-20` si sigue mostrando una fecha anterior.

Preserva explícitamente los siguientes límites canónicos:

```text
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Y las fronteras de interpretación:

```text
historical retrieval superiority != global RAG accuracy
normative evidence != binding legal correctness
auditable explanation != classification or legal correctness
no cross-study numeric superiority
no SOTA claim
no novelty redecision
```

No elimines ni debilites las 11 limitaciones no bloqueantes canónicas de Grupo 2B.

Haz un único commit administrativo del Plan.

---

## 7. Prohibiciones de cierre

No:

- editar los artefactos científicos de G4-F01, G4-F02 o G4-F03;
- integrar la v01 supersedida;
- calcular nuevas métricas o inferencia;
- buscar literatura nueva;
- redecidir HE2 o HE5;
- reabrir EXP12;
- declarar novelty, SOTA o superioridad numérica cross-study;
- modificar `article/main-manuscript`;
- activar o ejecutar G5-F01;
- crear artefactos de Grupo 5;
- cerrar G5-F01, G5-F02 o G5-F03.

---

## 8. Verificación final obligatoria

Después de todos los push, ejecuta `git fetch origin` y verifica:

```text
origin/main = 38e22c19a0eb0d344e7675761a88d7968091eead

G4_F03_LITERATURE_CONTRAST_BLOB = 2baff53184b17c23380693235a2f3257de5e2bba
G4_F03_GROUP4_CLOSURE_CANDIDATE_BLOB = 64ccc2068c15d0890bb9b978de8ed63d6d891034

G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE

G5_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F01_AUTHORIZED = false
G5_F01_STARTED = false
GROUP5 = NOT_STARTED

NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED_BY_PROMPT93 = false
```

Verifica que:

- el commit de fichas cambió exclusivamente `04_REGISTRO_ESTADO_FICHAS.md`;
- el commit del Plan cambió exclusivamente `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`;
- no existe merge commit ni commit científico adicional sobre `main`;
- el artículo no fue modificado por Prompt93.

Si la rama editorial avanzó concurrentemente, registra su HEAD final como `WARNING / NONBLOCKING`.

---

## 9. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/93_RESPUESTA_INTEGRAR_CERRAR_G4_F03_Y_GRUPO4_TRAS_REAUDITORIA.md
```

El commit de respuesta debe añadir únicamente ese archivo.

Reporte terminal mínimo:

```text
PROMPT93 = COMPLETED

PREFLIGHT_MAIN = 203770565e1a68c30ab3f27b912fc0fd971e4e8f
PREFLIGHT_PLAN = 89fe5a0c13c8cad03e49280dc2a3edec8bc14a0b
PREFLIGHT_FICHAS = 49b70a4fa8d4d7831fc8db06853d9004a564ec86
CANDIDATE_V02 = 38e22c19a0eb0d344e7675761a88d7968091eead
CANDIDATE_PARENT = 203770565e1a68c30ab3f27b912fc0fd971e4e8f

MAIN_AFTER_INTEGRATION = 38e22c19a0eb0d344e7675761a88d7968091eead
G4_F03_LITERATURE_CONTRAST_BLOB = 2baff53184b17c23380693235a2f3257de5e2bba
G4_F03_GROUP4_CLOSURE_CANDIDATE_BLOB = 64ccc2068c15d0890bb9b978de8ed63d6d891034

FICHAS_CLOSURE_COMMIT = ...
PLAN_CLOSURE_COMMIT = ...

G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
G5_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F01_AUTHORIZED = false
G5_F01_STARTED = false
GROUP5 = NOT_STARTED

NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
NEW_LITERATURE_SEARCH_PERFORMED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED_BY_PROMPT93 = false

ARTICLE_HEAD_PREFLIGHT = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...
BLOCKERS = NONE
WARNINGS = ...
```

Si cualquier precondición falla, no auto-repares ni continúes: devuelve el `STOP` correspondiente y no modifiques ramas científicas o de gobernanza.
