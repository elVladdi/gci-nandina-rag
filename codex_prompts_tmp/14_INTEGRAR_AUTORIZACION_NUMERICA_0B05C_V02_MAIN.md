# CODEX — INTEGRAR AUTORIZACIÓN NUMÉRICA 0B-05C v0.2 EN `main`

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE INTEGRACIÓN GIT** del candidato de autorización numérica 0B-05C v0.2 ya auditado externamente.

La auditoría externa independiente clasifica el candidato como:

`0B05C_V02_AUTHORIZATION_CANDIDATE = PASS / APPROVED_FOR_INTEGRATION`

Candidato remoto exacto:

`codex/0b05c-numerical-authorization-v02 = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`

Baseline científico integrado actual esperado:

`origin/main = c44f447cb941c512cd70712cf7c3e4bc670ab05a`

La tarea es **integrar exactamente ese candidato en `main` mediante fast-forward puro**, sin editar contenido y **sin ejecutar Attempt03, retrieval, EVAL, D1a ni ninguna sensibilidad numérica**.

---

## 1. IDENTIDADES OBLIGATORIAS ANTES DE CUALQUIER ESCRITURA

Haz `fetch` de las ramas remotas y verifica exactamente:

- `origin/main = c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- `origin/codex/0b05c-numerical-authorization-v02 = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- parent de `41d3259...` = `c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- tree de `41d3259...` = `4d0703327c2d9e05ecf19fd04f5a8c7d808bd0f6`;
- compare `origin/main...origin/codex/0b05c-numerical-authorization-v02` = `ahead 1 / behind 0`;
- merge-base exacto = `c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Si cualquiera difiere: **STOP / NO INTEGRAR**.

No limpiar, borrar ni alterar evidencia local/ignored de los Intentos 01/02.

---

## 2. VALIDACIÓN PREINTEGRACIÓN DEL CANDIDATO EXACTO

Desde un checkout limpio/detached de `41d3259...`, verifica de forma read-only:

### 2.1 Diff contractual

Contra `c44f447...` deben existir exactamente cinco changed paths y ningún otro:

1. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_numerical_authorization_record_v0.2.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/d1a_numerical_execution_spec_v0.2.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev03_numerical_execution_spec_v0.2.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev04_numerical_execution_spec_v0.2.json`

No puede existir ningún cambio de código, tests, docs, manifest, gate ledger, `.gitattributes`, Plan, article ni v0.1.

### 2.2 Transición de autorización

Usa la lógica ya integrada de `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py` y confirma:

- baseline `c44f447...` es proper ancestor del candidato;
- authorization record schema v2 exacto;
- `authorization_baseline_commit = c44f447...`;
- `baseline_external_audit = PASS / APPROVED_FOR_INTEGRATION`;
- bindings baseline exactos para `unified_gate`, `ev03_spec`, `ev04_spec`, `d1a_spec`;
- `load_authorization_transition_from_git(...) = PASS`;
- `validate_authorization_transition(...) = PASS`;
- immutable authorization projection idéntica fuera de los campos permitidos.

### 2.3 Estado candidato

Debe verificarse:

- gate `gate_status = APPROVED / INTEGRATED`;
- `authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- cuatro autorizaciones del gate = `AUTHORIZED`;
- EV03 spec = `AUTHORIZED`;
- EV04 spec = `AUTHORIZED`;
- D1a spec = `AUTHORIZED`;
- `authorization_record_present = true`;
- `runtime_authorization_record_present = false`;
- `corrective_retrieval_executed = false`;
- `corrective_metrics_computed = false`;
- D1a corpus/index/metrics flags siguen `false`;
- los 16 future roots siguen ausentes;
- no existen resultados correctivos v0.2.

### 2.4 Authorized preflight read-only

Antes de integrar, ejecuta únicamente `preflight_authorized()` de:

`src.experiments.run_0b05c_corrective_numerical_v02`

Nunca invoques `execute_authorized()` ni `--execute-authorized`.

El modelo congelado debe estar disponible localmente y coincidir exactamente:

- `models/text2trade_mnrl_v0.2/model.safetensors`;
- size `470637416` bytes;
- SHA-256 `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`.

Si el modelo falta o no coincide: **STOP / NO INTEGRAR**. No descargar ni sustituir pesos.

El resultado obligatorio es:

`PASS / AUTHORIZED_PREFLIGHT_ONLY`

con cero side effects y 16 future roots ausentes.

---

## 3. INTEGRACIÓN — FAST-FORWARD PURO

Solo si todo lo anterior pasa:

1. checkout de `main` limpio;
2. verifica nuevamente `main = origin/main = c44f447...`;
3. integra exclusivamente con fast-forward puro hasta `41d3259...`;
4. `main` debe quedar exactamente en `41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
5. el tree debe ser exactamente `4d0703327c2d9e05ecf19fd04f5a8c7d808bd0f6`;
6. push normal únicamente a `origin/main`.

Prohibido:

- merge commit;
- squash;
- cherry-pick;
- rebase;
- amend;
- force-push;
- edición manual;
- regeneración de artefactos;
- commit adicional en `main`.

---

## 4. VALIDACIÓN POSTINTEGRACIÓN

Después del push, vuelve a fetch y verifica:

- `origin/main = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- tree remoto = `4d0703327c2d9e05ecf19fd04f5a8c7d808bd0f6`;
- compare antiguo `main` → nuevo `main` = 1 commit / 5 paths exactos;
- Plan Maestro sigue `fe847f708...`;
- article sigue `254b1e6...`;
- ningún otro branch científico fue modificado.

Desde checkout limpio/detached del nuevo `origin/main`, ejecuta nuevamente **solo** `preflight_authorized()` read-only y confirma:

`PASS / AUTHORIZED_PREFLIGHT_ONLY`

Debe seguir siendo cierto:

- 16 future roots ausentes;
- runtime authorization record ausente;
- corrected retrieval = false;
- corrected metrics = false;
- no resultados correctivos;
- `numerical_execution_occurred = false`.

**No ejecutes Attempt03 en este bloque.**

No afirmes CI si no existe CI.

---

## 5. ESTADO CIENTÍFICO POSTINTEGRACIÓN

La integración convierte la autorización candidata en autorización versionada e integrada, pero no constituye ejecución.

Estado esperado:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION_READINESS = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`

`EV03_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

---

## 6. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Durante la integración científica no modifiques `codex/prompts-temporary`.

Solo después de finalizar y validar la integración:

1. fetch y checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/14_RESPUESTA_INTEGRAR_AUTORIZACION_NUMERICA_0B05C_V02_MAIN.md`;
3. no modifiques este Prompt 14 ni respuestas anteriores;
4. el commit administrativo debe contener solo ese archivo;
5. mensaje sugerido: `docs: persist prompt 14 authorization integration report`;
6. push normal, sin rebase/amend/force.

No exijas que el archivo persistido contenga el SHA de su propio commit administrativo. En la interfaz puedes añadir esa identidad después de crear el commit.

---

## 7. REPORTE FINAL OBLIGATORIO

Responde únicamente con:

### A. Preflight Git
Heads, parent/tree, compare, Plan, article.

### B. Preintegration authorization validation
Cinco paths, authorization record/baseline bindings, transition validator y estado autorizado/no ejecutado.

### C. Authorized preflight preintegration
Resultado, identidad del modelo y prueba de cero side effects.

### D. Integración
Método, rango, main final, tree, push, ausencia de commit adicional.

### E. Postintegration validation
Remote main/tree, preflight autorizado read-only, future roots/resultados ausentes.

### F. Aislamiento
Plan/article/EXP11B/EXP12/v0.1 sin cambios y ninguna ejecución.

### G. Persistencia administrativa
Response path y estado de persistencia.

### H. Estado científico
Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION_READINESS = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`

`EV03_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No ejecutes Attempt03. La auditoría externa posterior de esta integración decidirá el inicio de la corrida única.