# CODEX — MICROCLOSE DEL ORDEN MAESTRO ACTUAL TRAS RECONCILIACIÓN 0B-05C

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE GOBERNANZA DOCUMENTAL**.

La reconciliación 0B-05C del Plan Maestro fue correctamente aplicada en el commit:

`876ca310af523c512b32bb85a3ffb2993d6f20cf`

sobre la rama canónica:

`docs/plan-maestro-temporal-2026-08-31`

La auditoría externa posterior acepta esa reconciliación de 0B-05C, pero detectó un hallazgo residual **preexistente** en la sección `## 13. Orden maestro actual`: todavía aparecen como pendientes (`⏳`) pasos de NUEVA_01 / Real Ingest / Gate de nueva data que el propio historial del Plan demuestra que ya fueron completados y cerrados.

Este microclose debe corregir **únicamente esa inconsistencia de estado en el orden maestro actual**. No debe reabrir ni reinterpretar resultados científicos.

NO modifiques `main`. NO modifiques `article/main-manuscript`. NO construyas el gate numérico 0B-05C v0.2. NO autorices ni ejecutes ningún experimento. NO modifiques EXP11B ni EXP12 salvo la representación textual ya existente dentro del `Orden maestro actual` si fuera estrictamente necesaria para conservar continuidad.

---

## 1. IDENTIDADES OBLIGATORIAS ANTES DE EDITAR

Verifica y exige exactamente:

- `main = origin/main = 43291c312c2934aae03f3c087dd0a1ae594341b7`
- Plan branch = `docs/plan-maestro-temporal-2026-08-31`
- Plan HEAD = `876ca310af523c512b32bb85a3ffb2993d6f20cf`
- Plan tree = `a12093d8f04d2d81125ab6f32b98db2e56e26920`
- `article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`

Archivo único autorizado para modificación científica/documental:

`docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`

Si alguna identidad no coincide: STOP y reporta sin improvisar.

---

## 2. HALLAZGO A CERRAR

Clasificación externa:

`PLAN07-F001 = PREEXISTING_STALE_CURRENT_ORDER / NONBLOCKING_FOR_0B05C_GATE`

En `## 13. Orden maestro actual` aún aparecen secuencias como:

- `Usuario agrega NUEVA_01 según contrato ⏳`
- `Python valida e ingiere exclusivamente NUEVA_01`
- `Gate de capacidad / integridad de nueva data`
- `Python procesa exclusivamente nueva(s) hoja(s)`
- `NEW_HISTORICAL_GATE de datos ampliados`

como si todavía fueran etapas pendientes, aunque el historial posterior del mismo Plan registra:

- Real Ingest 01 completado con NUEVA_01;
- pool elegible congelado de 6,029 filas / 43 DAM / 56 NANDINA;
- capacidad H150/H200 factible;
- NEW HISTORICAL GATE 03 cerrado / aprobado / integrado;
- EXP11B Bank Materialization cerrado / aprobado / integrado;
- EXP11B Retrieval Execution Gate aprobado / integrado;
- EXP11B Retrieval Execution todavía NOT_AUTHORIZED / NOT_EXECUTED;
- recuperación EV03 v0.2 integrada;
- siguiente paso inmediato 0B-05C = construir y auditar gate/runner numérico v0.2.

La sección se denomina `Orden maestro actual`, por lo que no debe conservar estados `⏳` de etapas ya completadas.

---

## 3. CORRECCIÓN AUTORIZADA

Edita **solo la sección `## 13. Orden maestro actual`** y únicamente lo necesario para que la secuencia represente el estado actual.

Debe quedar conceptualmente equivalente a:

```text
Grupo 1 ✅
  ↓
Grupo 2A ✅
  ↓
EXP-11A ✅
  ↓
NEW_HISTORICAL_GATE — Forensic Audit 01 ✅
  ↓
Gate 02 ✅ CLOSED / APPROVED / INTEGRATED
  ↓
Real Ingest 01 — NUEVA_01 ✅ COMPLETED / APPROVED
  - pool elegible: 6,029 filas / 43 DAM / 56 NANDINA
  - H150/H200 feasible
  ↓
NEW_HISTORICAL_GATE 03 ✅ CLOSED / APPROVED / INTEGRATED
  ↓
EXP11B Bank Materialization ✅ CLOSED / APPROVED / INTEGRATED
  ↓
EXP11B Retrieval Execution Gate ✅ APPROVED / INTEGRATED
  ↓
EXP11B Retrieval Execution ⛔ NOT_AUTHORIZED / NOT_EXECUTED
  - EXP11B_PORTABILITY_DEBT=OPEN
  ↓
0B-05C v0.1 Corrective Numerical Gate and Authorization ✅ HISTORICAL / INTEGRATED / SUPERSEDED FOR NEW EXECUTION
  [preservar sus sublíneas actuales]
  ↓
EV03 Historical Recovery v0.2 ✅ APPROVED / VERSIONED / INTEGRATED
  [preservar sus sublíneas actuales]
  ↓
0B-05C Numerical Gate/Runner v0.2 ⏳ NEXT / NOT_YET_BUILT / NOT_AUTHORIZATION_READY
  - construct and audit a separate prospective v0.2 numerical gate/runner
  - the integrated recovery does not constitute numerical authorization
  ↓
EXP11B H150/H200 retrieval ⛔ NOT_AUTHORIZED / NOT_EXECUTED
  ↓
EXP-12 ⛔ NOT_AUTHORIZED / NOT_EXECUTED
  ↓
Grupo 2B
  ↓
Grupo 3
  ↓
Grupos 4–8
  ↓
Freeze científico
  ↓
Repositorio público / artículos / tesis final
```

Puedes ajustar mínimamente la redacción para respetar el estilo actual del Plan, pero no modificar hechos ni estados.

No borres el historial detallado de Real Ingest, Gate03 o Bank Materialization. Esos registros históricos deben permanecer íntegros.

---

## 4. ESTADOS QUE DEBEN PERMANECER INTACTOS

Confirma después de editar:

- `GROUP_2 = EN_CURSO`
- `EV03_HISTORICAL_RECOVERY_V02 = APPROVED / VERSIONED / INTEGRATED`
- `0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`
- EV03/EV04/D1a/unified v0.2 = `NOT_AUTHORIZED / NOT_EXECUTED`
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`
- `0B05C_CLOSURE = NOT_AUTHORIZED`
- `EXP11B_PORTABILITY_DEBT = OPEN`
- EXP11B retrieval = `NOT_AUTHORIZED / NOT_EXECUTED`
- EXP12 = `NOT_AUTHORIZED / NOT_EXECUTED`
- Grupo 3 sigue pendiente.

No cambies la fecha de actualización; ya es `2026-09-08`.

---

## 5. VALIDACIÓN

Antes de commit:

1. `git diff --check` = PASS.
2. Diff limitado al único archivo del Plan.
3. Dentro del archivo, el diff debe limitarse a la sección `## 13. Orden maestro actual`.
4. Verifica que ya no aparezcan como pendientes en esa sección los pasos completados de NUEVA_01 / Real Ingest / Gate03.
5. Verifica que el próximo paso explícito de 0B-05C continúe siendo construir/auditar gate/runner v0.2.
6. No debe aparecer ninguna autorización numérica v0.2.
7. `main` y article deben permanecer en sus SHAs iniciales.

---

## 6. COMMIT Y PUSH DEL PLAN

Si todo pasa:

- un único commit sobre `docs/plan-maestro-temporal-2026-08-31`;
- mensaje sugerido: `docs: close stale current-order states in master plan`;
- push únicamente de esa rama;
- no merge a main;
- no amend, no rebase, no force-push.

---

## 7. PERSISTENCIA OBLIGATORIA DE TU RESPUESTA EN LA RAMA DE PROMPTS

Esta sección es **administrativa y obligatoria**.

Después de completar o detener el trabajo del Plan, guarda el **reporte final exacto que vas a entregar al usuario** en:

`codex_prompts_tmp/08_RESPUESTA_MICROCLOSE_PLAN_ORDEN_MAESTRO_POST_RECOVERY_V02.md`

sobre la rama:

`codex/prompts-temporary`

Reglas:

1. No sobrescribas ni modifiques este prompt `08_MICROCLOSE_PLAN_ORDEN_MAESTRO_POST_RECOVERY_V02.md`.
2. No mezcles cambios de la rama del Plan con la rama de prompts.
3. Usa un worktree/checkout administrativo separado si es necesario.
4. El archivo `08_RESPUESTA_...md` debe contener literalmente el mismo reporte final que entregues en la interfaz.
5. Commit/push de esa respuesta **solo** a `codex/prompts-temporary`.
6. Si la persistencia administrativa falla, no alteres el resultado científico/documental; reporta explícitamente `RESPONSE_PERSISTENCE=FAIL` y la causa.
7. La creación del archivo de respuesta no autoriza ningún otro cambio en `codex/prompts-temporary`.

---

## 8. REPORTE FINAL

Entrega secciones A–G:

### A. Preflight
SHAs de main, Plan y article; tree del Plan; worktree clean.

### B. Hallazgo
`PLAN07-F001` y evidencia exacta de la inconsistencia previa.

### C. Corrección
líneas/segmento del `Orden maestro actual` corregidas y estados finales.

### D. Validación
scope de diff, `git diff --check`, búsqueda de estados stale, invariantes 0B-05C/EXP11B/EXP12.

### E. Commit Plan
SHA, parent, tree, file changed, push.

### F. Persistencia administrativa
path exacto de `08_RESPUESTA_...md`, commit de `codex/prompts-temporary`, push y `RESPONSE_PERSISTENCE=PASS/FAIL`.

### G. Estado final
Terminar con:

`PLAN07-F001 = CLOSED / PASS`

`GROUP_2 = EN_CURSO`

`0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

`EXP11B_PORTABILITY_DEBT = OPEN`

`EXP11B_RETRIEVAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EXP12 = NOT_AUTHORIZED / NOT_EXECUTED`
