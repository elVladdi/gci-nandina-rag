# CODEX — CONSTRUIR CANDIDATO DE AUTORIZACIÓN NUMÉRICA 0B-05C v0.2

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE LA TRANSICIÓN FORMAL DE AUTORIZACIÓN**, sin ejecutar ninguna sensibilidad numérica.

El gate/runner numérico 0B-05C v0.2 ya fue auditado externamente e integrado en `main`.

Baseline científico integrado y externamente aprobado:

`c44f447cb941c512cd70712cf7c3e4bc670ab05a`

La auditoría externa independiente del gate integrado establece:

`0B05C_NUMERICAL_GATE_V02 = PASS / APPROVED / VERSIONED / INTEGRATED`

Este Prompt 13 debe construir **un candidato separado de autorización**, basado exactamente en ese `main`, que permita una futura ejecución única de 0B-05C v0.2. **NO debes ejecutar `--execute-authorized`, retrieval, evaluación, D1a ni generar métricas.**

La salida de este bloque seguirá pendiente de auditoría externa antes de poder integrarse a `main`.

---

# 1. IDENTIDADES OBLIGATORIAS DE PREFLIGHT

Haz `fetch` y verifica antes de cualquier escritura:

- `origin/main = c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- tree de `c44f447...` = `41122fe6de833d7be83a2211e99cdd00561bc26e`;
- parent de `c44f447...` = `59dc445d8128dd71f48d26eac66c9ae8d0c21e38`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- gate integrado existe en:
  `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`;
- gate actual: `gate_status=CANDIDATE_PENDING_EXTERNAL_AUDIT`, `authorization_readiness=NOT_AUTHORIZATION_READY`, cuatro estados `NOT_AUTHORIZED`, `authorization_record_present=false`;
- los tres specs EV03/EV04/D1a tienen su autorización correspondiente `NOT_AUTHORIZED`;
- authorization record canónico v0.2 **no existe**;
- runtime authorization record **no existe**;
- los 16 `future_roots` v0.2 están ausentes;
- no existe ejecución correctiva ni métricas correctivas v0.2.

Si cualquiera de estas identidades o estados difiere: **STOP / NO AUTORIZAR**.

No limpiar ni borrar evidencia local/ignored de Intentos 01/02.

---

# 2. RAMA CANDIDATA DE AUTORIZACIÓN

No modifiques `main` directamente.

Desde exactamente `c44f447cb941c512cd70712cf7c3e4bc670ab05a`, crea y usa:

`codex/0b05c-numerical-authorization-v02`

La rama debe contener **un único commit científico de autorización** encima de `c44f447...`.

No rebase, no amend, no force-push, no squash, no cherry-pick.

---

# 3. TRANSICIÓN PERMITIDA — CAMBIOS EXACTOS

Respeta mecánicamente el `authorization_transition_schema` ya integrado.

El commit candidato debe modificar **únicamente** estos cuatro artefactos existentes y crear un quinto archivo:

1. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev03_numerical_execution_spec_v0.2.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev04_numerical_execution_spec_v0.2.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/d1a_numerical_execution_spec_v0.2.json`
5. **nuevo:** `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_numerical_authorization_record_v0.2.json`

No modifiques docs, manifest, gate hash ledger, código, tests, `.gitattributes`, Plan, article ni ningún otro path.

## 3.1 Gate unificado

En el gate, cambia exclusivamente:

- `gate_status`:
  - de `CANDIDATE_PENDING_EXTERNAL_AUDIT`
  - a `APPROVED / INTEGRATED`;
- `authorization_readiness`:
  - de `NOT_AUTHORIZATION_READY`
  - a `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- `authorization.EV03_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `authorization.EV04_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `authorization.D1A_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `authorization.UNIFIED_0B05C_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `authorization.authorization_record_present` → `true`.

Deben permanecer exactamente:

- `corrective_retrieval_executed=false`;
- `corrective_metrics_computed=false`;
- `runtime_authorization_record_present=false`;
- `0B05C_METRIC_IMPACT=NOT_DETERMINED`;
- `DOWNSTREAM_REEXECUTION=NOT_YET_JUSTIFIED`;
- `0B05C_CLOSURE=NOT_AUTHORIZED`;
- todos los patches, roots, commands, semantics, metrics, builders, evaluators, model policy, code bindings, order, comparison schema y runtime contracts.

## 3.2 EV03 spec

Cambia exclusivamente:

`authorization.EV03_NUMERICAL_EXECUTION: NOT_AUTHORIZED -> AUTHORIZED`

Mantén `corrective_retrieval_executed=false` y `corrective_metrics_computed=false` y todo lo demás byte-equivalente a nivel semántico/canónico.

## 3.3 EV04 spec

Cambia exclusivamente:

`authorization.EV04_NUMERICAL_EXECUTION: NOT_AUTHORIZED -> AUTHORIZED`

Mantén `corrective_retrieval_executed=false` y `corrective_metrics_computed=false` y todo lo demás inmutable.

## 3.4 D1a spec

Cambia exclusivamente:

`authorization.D1A_NUMERICAL_EXECUTION: NOT_AUTHORIZED -> AUTHORIZED`

Deben permanecer falsos:

- `D1A_CORRECTIVE_CORPUS_CREATED=false`;
- `D1A_CORRECTIVE_INDEX_CREATED=false`;
- `D1A_CORRECTIVE_METRICS_COMPUTED=false`.

Nada más puede cambiar.

---

# 4. AUTHORIZATION RECORD v0.2 — OBLIGATORIO

Crea exactamente:

`outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_numerical_authorization_record_v0.2.json`

Debe cumplir exactamente el schema v2 ya congelado en el gate y contener solo las keys requeridas:

- `artifact_id` = `0b05c_numerical_authorization_record_v0.2`;
- `schema_version` = `2`;
- `authorization_baseline_commit` = `c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- `baseline_external_audit` = `PASS / APPROVED_FOR_INTEGRATION`;
- `baseline_artifacts`.

`baseline_artifacts` debe contener exactamente:

- `unified_gate`;
- `ev03_spec`;
- `ev04_spec`;
- `d1a_spec`.

Para cada uno registra la identidad del artefacto **en el baseline `c44f447...`**, con exactamente:

- `path`;
- `git_blob_sha1`;
- `canonical_git_blob_sha256` = SHA-256 de los bytes de `git cat-file blob`;
- `canonical_size_bytes`.

No uses hashes del artefacto autorizado candidato como baseline. El baseline es siempre `c44f447...`.

No agregues timestamps, comentarios, campos derivados ni información no exigida por schema.

---

# 5. VALIDACIÓN MECÁNICA OBLIGATORIA

Después de construir el candidato, pero antes del push final, valida de manera read-only:

## 5.1 Diff exacto

Contra `c44f447...` deben existir exactamente cinco changed paths: los cuatro JSON de gate/specs y el authorization record nuevo.

No debe haber ningún otro cambio.

## 5.2 Transición immutable

Usa la lógica integrada en:

`src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py`

para demostrar que:

- el baseline es proper ancestor del candidato;
- `load_authorization_transition_from_git(...)` acepta el authorization record;
- `validate_authorization_transition(...)` acepta baseline → candidato;
- la immutable authorization projection es idéntica fuera de los campos permitidos;
- los cuatro baseline artifact bindings coinciden exactamente con `c44f447...`.

## 5.3 Authorized preflight read-only

Ejecuta **solo el preflight autorizado**, nunca la ejecución:

- invoca `preflight_authorized()` de `src.experiments.run_0b05c_corrective_numerical_v02` mediante un comando Python read-only;
- está prohibido invocar `execute_authorized()` o CLI `--execute-authorized`.

Para que `preflight_authorized()` pueda pasar, el modelo congelado debe estar disponible localmente con:

- path: `models/text2trade_mnrl_v0.2/model.safetensors`;
- size: `470637416` bytes;
- SHA-256: `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`.

Si el modelo no está disponible o no coincide: **STOP / NO AUTORIZAR**. No descargues otro modelo, no sustituyas pesos y no cambies hashes.

El preflight autorizado debe devolver `PASS / AUTHORIZED_PREFLIGHT_ONLY` sin crear ningún future root.

## 5.4 Estado no ejecutado

Tras el preflight autorizado:

- los 16 future roots siguen ausentes;
- runtime authorization record sigue ausente;
- corrected retrieval sigue false;
- corrected metrics sigue false;
- no hay resultados correctivos;
- ningún archivo de output runtime fue creado.

---

# 6. TESTS Y EVIDENCIA

Este commit cambia intencionalmente el estado de autorización. Por tanto, **no alteres la suite histórica de tests cerrados para hacerla pasar artificialmente**.

Antes de crear el commit de autorización, puedes registrar como baseline que la suite v0.2 de 56 tests pasó sobre `c44f447...` según el bloque de integración ya auditado.

Sobre el candidato autorizado, la evidencia obligatoria es:

- exact 5-path diff;
- transition validator = PASS;
- authorization-record validation = PASS;
- `preflight_authorized()` = PASS / AUTHORIZED_PREFLIGHT_ONLY;
- no side effects / no future roots.

Si ejecutas tests adicionales puramente read-only/sintéticos, repórtalos, pero **no ejecutes ningún retrieval/EVAL real**.

No afirmar CI si no existe.

---

# 7. COMMIT Y PUSH

Si todo lo anterior pasa:

- un único commit encima de `c44f447...`;
- mensaje sugerido:
  `chore: authorize single 0b05c v0.2 numerical execution`
- push únicamente a:
  `codex/0b05c-numerical-authorization-v02`
- no merge a `main`;
- no modificar `main`.

Reporta:

- commit SHA;
- parent exacto `c44f447...`;
- tree;
- compare vs `main`;
- changed paths exactos;
- Git blob SHA-1 + canonical SHA-256 + size de los cuatro baseline artifacts;
- Git blob SHA-1 + canonical SHA-256 + size del authorization record candidato;
- estado de preflight autorizado;
- ausencia de side effects.

---

# 8. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Durante el trabajo científico no modifiques `codex/prompts-temporary`.

Solo después de finalizar y pushear el candidato científico, realiza un paso administrativo separado:

1. fetch y checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/13_RESPUESTA_CONSTRUIR_AUTORIZACION_NUMERICA_0B05C_V02.md`;
3. no modifiques este Prompt 13 ni respuestas anteriores;
4. el commit administrativo debe contener solo ese archivo;
5. mensaje sugerido:
   `docs: persist prompt 13 authorization candidate report`;
6. push normal, sin rebase/amend/force.

La respuesta persistida debe contener el reporte científico completo A–J. En la interfaz puedes añadir después una sección K con la identidad del commit administrativo, evitando cualquier autorreferencia imposible dentro del propio archivo.

---

# 9. REPORTE FINAL OBLIGATORIO

Responde únicamente con:

### A. Preflight Git
Heads, baseline/tree, Plan, article, ausencia de authorization record/future roots.

### B. Baseline externo aprobado
Baseline `c44f447...` y estado `PASS / APPROVED_FOR_INTEGRATION`.

### C. Authorization transition
Lista exacta de campos cambiados en gate + tres specs.

### D. Authorization record
Schema v2 y cuatro baseline bindings con Git blob SHA-1, canonical SHA-256 y size.

### E. Immutable transition validation
Resultado de `load_authorization_transition_from_git` / `validate_authorization_transition` y diff permitido.

### F. Authorized preflight
Resultado de `preflight_authorized()`, identidad del modelo y prueba de cero side effects.

### G. Diff y aislamiento
Cinco paths exactos; main/Plan/article/EXP11B/EXP12/v0.1 sin cambios.

### H. Commit candidato
Branch, SHA, parent, tree, compare, push.

### I. Persistencia administrativa
Response path y estado de persistencia, sin inventar self SHA dentro del archivo.

### J. Estado científico
Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION_CANDIDATE = CREATED / PENDING_EXTERNAL_AUDIT`

`0B05C_V02_AUTHORIZATION_READINESS = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION (CANDIDATE_ONLY)`

`EV03_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED (CANDIDATE_ONLY)`

`EV04_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED (CANDIDATE_ONLY)`

`D1A_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED (CANDIDATE_ONLY)`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED (CANDIDATE_ONLY)`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No declares la autorización integrada ni ejecutes Attempt03. La auditoría externa posterior decidirá si este candidato puede integrarse.