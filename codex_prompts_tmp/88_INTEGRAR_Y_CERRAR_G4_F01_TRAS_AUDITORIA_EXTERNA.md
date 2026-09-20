# PROMPT 88 — INTEGRAR Y CERRAR G4-F01 TRAS AUDITORÍA EXTERNA

## 0. Naturaleza y límite

La IA Experimental ha auditado externamente el candidato de G4-F01 generado por Prompt87 y ha emitido `PASS`.

Esta ejecución es exclusivamente administrativa y de integración. No puede crear ciencia nueva, recalcular métricas, recalcular inferencia, modificar claims, redecidir HE2/HE5, redactar artículo ni activar G4-F02.

Estado de entrada esperado:

```text
GROUP3 = CLOSED / APPROVED
G4_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G4_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Objetivo único:

```text
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = IN_PROGRESS
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

No cierres Grupo 4 y no avances a G4-F02.

---

## 1. Repositorio y refs exactos

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de modificar nada, ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 09278a10063a1e175ee2991b60f7649dd2ee40f4
origin/docs/plan-maestro-temporal-2026-08-31 = 06b24245f4c974b7550863d21ed05f4d63c2792b
origin/docs/fichas-grupos-3-8 = f3833a24cb10668a10d929c3743f935f2aba55a9
origin/codex/group4-f01-result-claim-evidence-v01 = 9f549ebdf940f9d806d5088697394d0c927f9fdc
```

Prompt87 fuente:

```text
03effc90c1294fb7a20ff7f872d4a155ed7f6be9
```

Prompt87 response:

```text
e46f4d2a2df34eaff3d61999af5db658ec0c76c8
```

Artículo observado tras Prompt87:

```text
origin/article/main-manuscript = 5e58b5a45b1dcc50a4a324f38e5cc0c9746ef3dc
```

El artículo es solo observacional. Drift editorial concurrente no bloquea esta ejecución si Prompt88 no modifica esa rama.

Si `main`, Plan, fichas o el candidato científico presentan drift no explicado:

```text
STOP / G4_F01_CLOSURE_REF_DRIFT
```

---

## 2. Candidato auditado e inmutable

Rama:

```text
codex/group4-f01-result-claim-evidence-v01
```

Commit candidato auditado:

```text
9f549ebdf940f9d806d5088697394d0c927f9fdc
```

Padre exacto:

```text
09278a10063a1e175ee2991b60f7649dd2ee40f4
```

Debe continuar cumpliéndose:

```text
COMMITS_AHEAD_OF_MAIN = 1
COMMITS_BEHIND_MAIN = 0
CHANGED_PATH_COUNT = 2
```

Paths exactos:

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
```

Blobs auditados:

```text
CSV_BLOB = da0351cb523fc7f3b45a83e072765a07f809b7fe
JSON_BLOB = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab
```

No modifiques, regeneres, reformatees ni normalices estos archivos.

Verifica además que el candidato conserva:

```text
CONTROLLED_CLAIM_COUNT = 18
CSV_PRIMARY_ROW_COUNT = 18
JSON_MATRIX_ROW_COUNT = 18
NEW_CLAIM_COUNT = 0
DROPPED_CLAIM_COUNT = 0
DUPLICATE_CLAIM_ID_COUNT = 0
OVERSTRENGTH_CLAIM_COUNT = 0
G3C010_HE5_POSITIVE_EVIDENCE_COUNT = 0
G3C010_HE5_NEGATIVE_EVIDENCE_COUNT = 0
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
G4_F02_STARTED = false
```

Si cualquier blob o condición difiere:

```text
STOP / AUDITED_G4_F01_CANDIDATE_CHANGED
```

---

## 3. Integración a `main`

Integra exclusivamente el commit candidato auditado mediante **fast-forward puro**.

Precondición:

```text
origin/main = 09278a10063a1e175ee2991b60f7649dd2ee40f4
candidate_parent = 09278a10063a1e175ee2991b60f7649dd2ee40f4
```

Después de la integración debe cumplirse exactamente:

```text
origin/main = 9f549ebdf940f9d806d5088697394d0c927f9fdc
```

No generes merge commit, squash, cherry-pick reconstruido ni commit científico adicional.

Tras push, vuelve a hacer `git fetch origin` y verifica:

```text
MAIN_FINAL = 9f549ebdf940f9d806d5088697394d0c927f9fdc
CSV_BLOB_FINAL = da0351cb523fc7f3b45a83e072765a07f809b7fe
JSON_BLOB_FINAL = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab
```

Si no coincide:

```text
STOP / G4_F01_FAST_FORWARD_INTEGRATION_FAILED
```

---

## 4. Cierre administrativo en registro de fichas

Trabaja desde:

```text
branch = docs/fichas-grupos-3-8
base = f3833a24cb10668a10d929c3743f935f2aba55a9
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica únicamente ese archivo.

Actualiza la tabla a:

```text
G4-F01 = CLOSED / APPROVED
G4-F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4-F03 = PROSPECTIVE
```

Añade un bloque de cierre que registre, como mínimo:

```text
FICHA = G4-F01
PROMPT87_COMMIT = 03effc90c1294fb7a20ff7f872d4a155ed7f6be9
PROMPT87_RESPONSE_COMMIT = e46f4d2a2df34eaff3d61999af5db658ec0c76c8
ACTIVATION_COMMIT = 1e4800ab6fe4e03c647aa5b53c2f29963c89f7e5
CANDIDATE_COMMIT = 9f549ebdf940f9d806d5088697394d0c927f9fdc
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
INTEGRATION_COMMIT = 9f549ebdf940f9d806d5088697394d0c927f9fdc
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
FINAL_G4_F01_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = IN_PROGRESS
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F02_AUTHORIZED = false
```

Haz un solo commit administrativo para este cierre y push normal.

No actives G4-F02.

---

## 5. Reconciliación del Plan Maestro

Trabaja desde:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = 06b24245f4c974b7550863d21ed05f4d63c2792b
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
G4_F01_INTEGRATION_COMMIT = 9f549ebdf940f9d806d5088697394d0c927f9fdc
G4_F01_EXTERNAL_AUDIT = PASS
G4_F01_CONTROLLED_CLAIM_COUNT = 18
G4_F01_OVERSTRENGTH_CLAIM_COUNT = 0
G4_F01_NEW_INFERENCE_PERFORMED = false
G4_F01_METRICS_RECOMPUTED = false
NEXT_ELIGIBLE_FICHA = G4-F02
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F02_AUTHORIZED = false
```

Preserva explícitamente las restricciones científicas relevantes:

- EXP11A = sensibilidad conjunta tamaño/composición, no efecto causal aislado.
- EXP11B = sensibilidad descriptiva, no inferencia de superpoblación de seeds.
- 0B-05C = Attempt06 corregido vigente; no resumir como impacto numérico cero global.
- EXP12 = NOT_ESTIMABLE y cerrado sin retrieval.
- retrieval histórico superior ≠ exactitud global del RAG.
- evidencia normativa ≠ corrección jurídica vinculante.
- explicación auditable ≠ clasificación o corrección legal.
- G3C-010/EXP12 no es evidencia positiva ni negativa de HE5.

No añadas resultados científicos nuevos.

Haz un solo commit administrativo del Plan y push normal.

---

## 6. Prohibiciones absolutas

No:

- modificar los dos artefactos G4-F01 auditados;
- recalcular métricas, agregados, CI, bootstrap o p-values;
- redecidir HE2 o HE5;
- añadir, eliminar o reformular los 18 claims;
- reabrir EXP12;
- ejecutar retrieval;
- modificar `article/main-manuscript`;
- activar o ejecutar G4-F02;
- ejecutar G4-F03;
- cerrar Grupo 4.

---

## 7. Verificación final obligatoria

Tras todos los push, ejecuta `git fetch origin` y verifica:

```text
MAIN_FINAL = 9f549ebdf940f9d806d5088697394d0c927f9fdc
CSV_BLOB_FINAL = da0351cb523fc7f3b45a83e072765a07f809b7fe
JSON_BLOB_FINAL = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab

G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4 = IN_PROGRESS
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F02_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
```

Verifica que `article/main-manuscript` no fue modificado por Prompt88. Si avanzó concurrentemente, registra la advertencia y el HEAD final observado.

---

## 8. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/88_RESPUESTA_INTEGRAR_Y_CERRAR_G4_F01_TRAS_AUDITORIA_EXTERNA.md
```

Ese commit de respuesta debe añadir únicamente dicho archivo.

Reporte terminal mínimo:

```text
PROMPT88 = COMPLETED

PREFLIGHT_MAIN = ...
PREFLIGHT_PLAN = ...
PREFLIGHT_FICHAS = ...
ARTICLE_HEAD_OBSERVED = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...
ARTICLE_MODIFIED_BY_PROMPT88 = false

G4_F01_CANDIDATE_COMMIT = 9f549ebdf940f9d806d5088697394d0c927f9fdc
MAIN_FINAL = 9f549ebdf940f9d806d5088697394d0c927f9fdc
CSV_BLOB_FINAL = da0351cb523fc7f3b45a83e072765a07f809b7fe
JSON_BLOB_FINAL = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab
PLAN_CLOSURE_COMMIT = ...
FICHAS_CLOSURE_COMMIT = ...

G4_F01_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP4_FINAL_STATE = IN_PROGRESS
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F02_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
SCIENTIFIC_ARTIFACTS_MODIFIED = false
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false

BLOCKERS = NONE
WARNINGS = ...
```

Si cualquier precondición falla, no intentes reparar ciencia ni gobernanza por tu cuenta: detén la ejecución y reporta el bloqueo exacto.