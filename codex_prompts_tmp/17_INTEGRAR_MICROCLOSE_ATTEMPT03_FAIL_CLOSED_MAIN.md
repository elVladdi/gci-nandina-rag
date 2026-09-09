# CODEX — INTEGRAR MICROCLOSE ATTEMPT03 FAIL-CLOSED EN `main`

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE INTEGRACIÓN** del microclose científico post-fallo de Attempt03 ya auditado externamente.

Candidato aprobado externamente:

- rama: `codex/0b05c-attempt03-failclosed-microclose`
- commit: `60aa7dd8715962f3c3e8b617e8797532529f39ed`
- parent exacto: `41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`
- tree exacto: `b846797096d4ca1e1301b4dafbd362c0d8e0d88b`

Objetivo único: integrar ese commit en `main` mediante **FAST-FORWARD ONLY**, sin modificar su contenido.

Este bloque NO autoriza ni ejecuta Attempt04, NO construye v0.3, NO ejecuta retrieval/EV03/EV04/D1a y NO genera resultados numéricos.

---

## 1. PREFLIGHT GIT OBLIGATORIO

Haz `fetch` y verifica exactamente antes de escribir:

- `origin/main = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- candidato remoto = `60aa7dd8715962f3c3e8b617e8797532529f39ed`;
- parent del candidato = `41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- tree del candidato = `b846797096d4ca1e1301b4dafbd362c0d8e0d88b`;
- compare `41d3259...` → `60aa7dd...` = exactamente `1 ahead / 0 behind`, 1 commit y 2 paths;
- merge-base = `41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Los dos únicos paths del candidato deben ser:

1. `outputs/audits/0b05c_attempt03_failclosed_v0.2/attempt03_failure_record_v0.2.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`

Si cualquier identidad o path difiere: **STOP / NO INTEGRATION**.

No limpies ni borres evidencia local/ignored de Attempt01/02/03.

---

## 2. VALIDACIÓN DEL CANDIDATO ANTES DE INTEGRAR

Verifica read-only:

### 2.1 Failure record

Debe existir exactamente:

`outputs/audits/0b05c_attempt03_failclosed_v0.2/attempt03_failure_record_v0.2.json`

y declarar, entre otros:

- `artifact_id = 0b05c_attempt03_failure_record_v0.2`;
- `schema_version = 1`;
- `attempt_id = ATTEMPT03`;
- `status = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`;
- `authorization_consumed = true`;
- `automatic_reuse_authorized = false`;
- `attempt04_authorized = false`;
- `authorization_commit = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- `authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- `failure_class = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT`;
- `runtime_partial_outputs = LOCAL_PRESERVED_NOT_VERSIONED`;
- `metric_impact = NOT_DETERMINED`;
- `downstream_reexecution = NOT_YET_JUSTIFIED`;
- `closure = NOT_AUTHORIZED`.

El binding administrativo debe seguir apuntando a Prompt15:

- commit `a449a3127a52e4b17948fd7fe6a3040a24f02ebd`;
- path `codex_prompts_tmp/15_RESPUESTA_EJECUTAR_ATTEMPT03_NUMERICO_0B05C_V02.md`;
- Git blob SHA-1 `c83b7d9004433ee1f369989dd6a5c7b9800c8e0d`;
- clasificación `CODEX_LOCAL_EXECUTION_REPORT_NOT_INDEPENDENTLY_VERSIONED_RUNTIME_OUTPUTS`.

### 2.2 Gate v0.2 consumido

La única diferencia del gate frente al baseline `41d3259...` debe ser:

`authorization_readiness`:

- antes: `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`
- después: `ATTEMPT03_CONSUMED / REAUTHORIZATION_REQUIRED`

Debe permanecer sin cambios:

- `gate_status = APPROVED / INTEGRATED`;
- cuatro autorizaciones históricas = `AUTHORIZED`;
- `authorization_record_present=true`;
- `corrective_retrieval_executed=false`;
- `corrective_metrics_computed=false`;
- `runtime_authorization_record_present=false`.

No aceptes ningún cambio adicional de ciencia, contratos, código o resultados.

### 2.3 Reutilización bloqueada

Sin ejecutar modelo ni componentes, puedes invocar read-only `preflight_authorized()` sobre el candidato y exige que falle por readiness consumida con:

`Authorized gate readiness is invalid`

Debe fallar antes de cualquier side effect. No debe crear future roots.

No ejecutes `--execute-authorized`.

---

## 3. INTEGRACIÓN — FAST-FORWARD ONLY

Si todo lo anterior pasa:

1. checkout `main` limpio;
2. confirma otra vez `origin/main = 41d3259...`;
3. integra exclusivamente mediante fast-forward al commit `60aa7dd...`;
4. push normal a `origin/main`;
5. no merge commit, squash, cherry-pick, rebase, amend ni force-push.

Después del push exige:

- `origin/main = 60aa7dd8715962f3c3e8b617e8797532529f39ed`;
- tree remoto = `b846797096d4ca1e1301b4dafbd362c0d8e0d88b`;
- compare antiguo main → nuevo main = exactamente 1 commit / 2 paths;
- candidate tree = integrated tree.

---

## 4. VALIDACIÓN POST-INTEGRACIÓN

Solo read-only:

- failure record presente en `main` con contenido idéntico al candidato;
- gate readiness = `ATTEMPT03_CONSUMED / REAUTHORIZATION_REQUIRED`;
- cuatro autorizaciones históricas siguen `AUTHORIZED`;
- no hay Attempt04 autorizado;
- `preflight_authorized()` queda mecánicamente bloqueado por readiness consumida antes de side effects;
- no se crearon future roots por este bloque;
- no se generaron resultados correctivos;
- no se modificaron Plan, article, EXP11B, EXP12 ni v0.1.

No ejecutes suites o comandos que produzcan outputs científicos.

---

## 5. PERSISTENCIA ADMINISTRATIVA

Solo después de finalizar y validar la integración científica:

1. fetch/checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/17_RESPUESTA_INTEGRAR_MICROCLOSE_ATTEMPT03_FAIL_CLOSED_MAIN.md`;
3. commit administrativo separado, response-only;
4. mensaje sugerido:
   `docs: persist prompt 17 attempt03 fail-closed integration report`;
5. push normal, sin rebase/amend/force.

Nunca mezcles `codex/prompts-temporary` con `main`.

---

## 6. REPORTE FINAL OBLIGATORIO

Responde únicamente con:

### A. Preflight Git
Identidades de main, candidato, parent, tree, compare, Plan y article.

### B. Validación preintegración
Failure record, diff exacto del gate y bloqueo de reutilización.

### C. Integración
Método FAST_FORWARD_ONLY y SHA/tree finales.

### D. Validación postintegración
Main remoto, dos paths exactos, readiness consumida, ausencia de side effects/Attempt04.

### E. Aislamiento
Plan/article/EXP11B/EXP12/v0.1 sin cambios.

### F. Persistencia administrativa
Response path y commit response-only.

### G. Estado científico
Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED (HISTORICAL)`

`0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT03`

`0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_VERSIONED / INTEGRATED`

`EV04_RECOVERY_ROOT_CAUSE = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT`

`0B05C_V03_RECOVERY_GATE = NOT_YET_BUILT / NOT_AUTHORIZED`

`ATTEMPT04 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No construyas v0.3. No autorices Attempt04.