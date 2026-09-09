# CODEX — INTEGRAR GATE/RUNNER NUMÉRICO 0B-05C v0.2 EN `main`

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE INTEGRACIÓN GIT** del candidato ya auditado del gate/runner numérico 0B-05C v0.2.

La auditoría externa independiente ha cerrado F001–F010 y clasifica el candidato científico como:

`0B05C_NUMERICAL_GATE_V02 = PASS / APPROVED_FOR_INTEGRATION`

Candidato remoto exacto:

`codex/0b05c-corrective-numerical-gate-v02 = c44f447cb941c512cd70712cf7c3e4bc670ab05a`

Base científica actual esperada:

`origin/main = 43291c312c2934aae03f3c087dd0a1ae594341b7`

La tarea es **integrar exactamente ese candidato en `main` mediante fast-forward puro**, sin modificar contenido y sin autorizar ni ejecutar ninguna sensibilidad numérica.

---

## 1. IDENTIDADES OBLIGATORIAS ANTES DE CUALQUIER ESCRITURA

Haz `fetch` de las ramas remotas y verifica exactamente:

- `origin/main = 43291c312c2934aae03f3c087dd0a1ae594341b7`;
- `origin/codex/0b05c-corrective-numerical-gate-v02 = c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- parent de `c44f447...` = `59dc445d8128dd71f48d26eac66c9ae8d0c21e38`;
- tree de `c44f447...` = `41122fe6de833d7be83a2211e99cdd00561bc26e`;
- cadena candidata exacta desde `main`:
  - `43291c312...`
  - `b0a1e61f70f42aa2048338965cc003e032d3a493`
  - `59dc445d8128dd71f48d26eac66c9ae8d0c21e38`
  - `c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- compare `origin/main...origin/codex/0b05c-corrective-numerical-gate-v02` = `ahead 3 / behind 0` y merge-base exacto `43291c312...`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Si cualquiera difiere: **STOP / NO INTEGRAR**.

El worktree tracked usado para integración debe estar limpio y no debe existir ninguna operación Git en progreso.

No limpies, borres ni alteres evidencia local/ignored de Intentos 01/02.

---

## 2. DIFF CANDIDATO QUE DEBE INTEGRARSE SIN DERIVA

Verifica que el compare completo `43291c312... -> c44f447...` contenga exactamente estos 13 paths y ningún otro:

1. `.gitattributes`
2. `docs/0B05C_CORRECTIVE_NUMERICAL_GATE_V02.md`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_gate_hash_ledger_v0.2.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_gate_manifest_v0.2.json`
6. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/d1a_numerical_execution_spec_v0.2.json`
7. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev03_numerical_execution_spec_v0.2.json`
8. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev04_numerical_execution_spec_v0.2.json`
9. `src/experiments/build_bm25_corrective_0b05c_v02.py`
10. `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py`
11. `src/experiments/run_0b05c_corrective_numerical_v02.py`
12. `src/experiments/run_d1a_corrective_0b05c_v02.py`
13. `tests/test_0b05c_corrective_numerical_gate_v02.py`

No edites ninguno de esos paths. La integración debe preservar exactamente los blobs del commit `c44f447...`.

---

## 3. VALIDACIÓN PREINTEGRACIÓN

Desde un checkout/worktree limpio del candidato `c44f447...`, ejecuta exclusivamente validaciones de pre-ejecución:

1. `python -B -m src.experiments.run_0b05c_corrective_numerical_v02 --preflight`
   - debe devolver `PASS`;
   - `mode = PREEXECUTION_CLOSED_READONLY`;
   - `authorization_readiness = NOT_AUTHORIZATION_READY`;
   - no debe crear roots científicos.

2. Suite v0.2:
   - `tests/test_0b05c_corrective_numerical_gate_v02.py`;
   - reporta RUN/PASS/FAIL/ERROR/SKIP.

No afirmes CI. Estos resultados son evidencia local de Codex.

**PROHIBIDO ejecutar `--execute-authorized`.**

Comprueba además en los artefactos versionados:

- `gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT` antes de integración;
- `authorization_readiness = NOT_AUTHORIZATION_READY`;
- EV03/EV04/D1a/UNIFIED = `NOT_AUTHORIZED`;
- `authorization_record_present = false`;
- `runtime_authorization_record_present = false`;
- `corrective_retrieval_executed = false`;
- `corrective_metrics_computed = false`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

No cambies estos estados durante la integración.

---

## 4. INTEGRACIÓN — FAST-FORWARD ONLY

Trabaja sobre `main` actualizado desde `origin/main`.

La única integración permitida es equivalente a:

`git merge --ff-only origin/codex/0b05c-corrective-numerical-gate-v02`

Debe resultar:

`HEAD(main) = c44f447cb941c512cd70712cf7c3e4bc670ab05a`

No crear commit de merge.
No squash.
No cherry-pick.
No rebase.
No amend.
No force-push.
No edición manual.
No regeneración de artefactos.

Si `--ff-only` no es posible: **STOP**.

Push normal exclusivamente a `origin/main`.

---

## 5. VALIDACIÓN POSTINTEGRACIÓN

Después del push, verifica independientemente con refs remotos:

- `origin/main = c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- tree = `41122fe6de833d7be83a2211e99cdd00561bc26e`;
- Plan Maestro sigue exactamente `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article sigue exactamente `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- compare antiguo main `43291c312...` -> nuevo main `c44f447...` sigue exactamente 3 commits y los 13 paths anteriores;
- no existe authorization record v0.2 versionado;
- no existe runtime authorization record v0.2 versionado;
- ningún estado operativo fue cambiado a `AUTHORIZED`;
- ningún resultado correctivo fue generado/versionado.

Desde checkout limpio/detached del nuevo `origin/main`, repite:

1. `python -B -m src.experiments.run_0b05c_corrective_numerical_v02 --preflight`;
2. suite v0.2 completa.

Ambos deben PASS y no crear roots científicos persistentes.

---

## 6. ESTADO CIENTÍFICO DESPUÉS DE INTEGRAR

La integración **NO es autorización de ejecución**.

El reporte debe dejar explícito:

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED`

pero simultáneamente:

`0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

El siguiente bloque será una **transición de autorización separada y auditada**. No la construyas ni la ejecutes aquí.

---

## 7. RAMAS QUE NO DEBES MODIFICAR

Durante el trabajo científico de integración no modifiques:

- `docs/plan-maestro-temporal-2026-08-31`;
- `article/main-manuscript`;
- `codex/prompts-temporary`;
- EXP11B;
- EXP12.

### Excepción administrativa obligatoria

Al terminar el trabajo científico y haber hecho todas las validaciones, **sí debes cambiar únicamente a `codex/prompts-temporary` para persistir tu reporte final**, como se define en la sección 8. Esa persistencia administrativa no puede modificar ni repetir el trabajo científico y debe ser un commit separado.

---

## 8. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Al finalizar, persiste **exactamente tu reporte final** en:

Rama:

`codex/prompts-temporary`

Archivo nuevo obligatorio:

`codex_prompts_tmp/12_RESPUESTA_INTEGRAR_GATE_RUNNER_NUMERICO_0B05C_V02_MAIN.md`

Reglas:

- no sobrescribas ni modifiques `12_INTEGRAR_GATE_RUNNER_NUMERICO_0B05C_V02_MAIN.md`;
- no modifiques respuestas anteriores;
- antes de escribir, `fetch` de la rama administrativa y asegúrate de no perder commits concurrentes;
- el commit administrativo debe contener exclusivamente el archivo de respuesta anterior;
- mensaje sugerido: `docs: persist prompt 12 integration report`;
- push normal, sin force/rebase/amend;
- no mezcles este commit administrativo con `main`.

Si no puedes persistir la respuesta, reporta `RESPONSE_PERSISTENCE=FAIL`, pero no repitas la integración científica ya completada.

---

## 9. REPORTE FINAL OBLIGATORIO

Responde únicamente con secciones A–H:

### A. Preflight Git
Refs, commit chain, tree, compare y worktree.

### B. Preintegration validation
Preflight read-only, suite v0.2 y estados cerrados.

### C. Diff contractual
Confirma los 13 paths exactos y ausencia de deriva.

### D. Integración
Método `FAST_FORWARD_ONLY`, nuevo HEAD/tree, push y ausencia de commit adicional.

### E. Postintegration validation
Refs remotos, preflight detached, tests, ausencia de autorización/ejecución/resultados.

### F. Aislamiento
Plan/article/admin durante integración científica sin cambios; EXP11B/EXP12 intactos.

### G. Persistencia administrativa
Response path, commit administrativo, único archivo y `RESPONSE_PERSISTENCE`.

### H. Estado científico
Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No avances a la autorización.