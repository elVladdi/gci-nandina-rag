# CODEX — EJECUTAR ATTEMPT04 NUMÉRICO 0B-05C v0.3

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE LA ÚNICA EJECUCIÓN NUMÉRICA AUTORIZADA 0B-05C v0.3 — Attempt04**.

La autorización numérica v0.3 ya fue auditada externamente e integrada en `main`.

Baseline científico/autorizado exacto:

`e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`

Tree autorizado:

`d10ea04228d2754dc8156b0abaedfceee9fe297f`

Parent de autorización:

`8b1444aed67d322714189846f98a3169145ea3d4`

Estado autorizado externo:

- `0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`;
- `0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED`;
- `authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- EV03/EV04/D1a/UNIFIED = `AUTHORIZED`;
- `ATTEMPT04 = AUTHORIZED / NOT_EXECUTED`.

Este bloque **sí autoriza exactamente una invocación** de la ejecución numérica unificada v0.3.

Está absolutamente prohibido reintentar, reanudar, repetir, reparar manualmente o ejecutar componentes por separado.

No cierres 0B-05C ni determines todavía si el impacto métrico es material/no material. Eso corresponde a auditoría externa posterior.

---

# 1. PREFLIGHT GIT OBLIGATORIO — ANTES DE CUALQUIER SIDE EFFECT

Haz `fetch` y verifica exactamente:

- `origin/main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- tree de `e3476d9...` = `d10ea04228d2754dc8156b0abaedfceee9fe297f`;
- parent = `8b1444aed67d322714189846f98a3169145ea3d4`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Verifica en `main`:

### Gate v0.3

Path:

`outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`

Debe tener:

- `gate_status = APPROVED / INTEGRATED`;
- `authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- `authorization.EV03_NUMERICAL_EXECUTION = AUTHORIZED`;
- `authorization.EV04_NUMERICAL_EXECUTION = AUTHORIZED`;
- `authorization.D1A_NUMERICAL_EXECUTION = AUTHORIZED`;
- `authorization.UNIFIED_0B05C_NUMERICAL_EXECUTION = AUTHORIZED`;
- `authorization.authorization_record_present = true`;
- `authorization.runtime_authorization_record_present = false`;
- `authorization.corrective_retrieval_executed = false`;
- `authorization.corrective_metrics_computed = false`;
- `attempt04 = AUTHORIZED / NOT_EXECUTED`.

Blob Git esperado del gate autorizado:

`d4751f418b45dcf190d6c9b06bce68692afac071`

### Authorization record v0.3

Path:

`outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_numerical_authorization_record_v0.3.json`

Debe existir con:

- Git blob SHA-1 `1338201cf4935b9cc7796a2f571c07908248e086`;
- `artifact_id = 0b05c_numerical_authorization_record_v0.3`;
- `schema_version = 3`;
- `authorization_baseline_commit = 8b1444aed67d322714189846f98a3169145ea3d4`;
- `baseline_external_audit = PASS / APPROVED_FOR_INTEGRATION`;
- exactamente cuatro `baseline_artifacts`.

### Specs autorizados

- EV03 spec Git blob = `bba7d853d83460ae99c7587e9d3e2a7ebc55e2c8`, propia = `AUTHORIZED`, `attempt04 = AUTHORIZED / NOT_EXECUTED`, retrieval/metrics false;
- EV04 spec Git blob = `3a6f9219871777cdd932104d2fe6153a5cbc69eb`, propia = `AUTHORIZED`, `attempt04 = AUTHORIZED / NOT_EXECUTED`, retrieval/metrics false;
- D1a spec Git blob = `f53221abb1e2afa1a317f410d33febfae91343d1`, propia = `AUTHORIZED`, `attempt04 = AUTHORIZED / NOT_EXECUTED`, `D1A_CORRECTIVE_CORPUS_CREATED=false`, `D1A_CORRECTIVE_INDEX_CREATED=false`, `D1A_CORRECTIVE_METRICS_COMPUTED=false`.

### Roots preexistentes

Los 16 `future_roots` v0.3 declarados por el gate deben estar ausentes antes de la ejecución.

En particular no debe existir:

- `outputs/audits/0b05c_corrective_numerical_runtime_v0.3/runtime_authorization_record_v0.3.json`;
- `outputs/evaluation/0b05c_corrective_numerical_v0.3/unified_sensitivity_summary_v0.3.json`;
- ningún resultado correctivo v0.3 previo.

No borres ni limpies evidencia local/ignored de Attempt01/02/03.

Si cualquier identidad o estado difiere: **STOP / ATTEMPT04_NOT_STARTED**.

No consumas la autorización si el preflight Git no pasa.

---

# 2. RAMA Y WORKTREE AISLADO DE ATTEMPT04

No ejecutes directamente sobre `main`.

Desde exactamente:

`e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`

crea/usa la rama:

`codex/0b05c-numerical-attempt04-v03`

Antes de la ejecución:

- la rama debe apuntar exactamente a `e3476d9...` sin commits propios;
- el worktree tracked debe estar limpio;
- ningún future root v0.3 debe existir.

Preferencia: usa un worktree aislado dedicado a Attempt04.

Si el modelo congelado no está presente en ese worktree, puedes copiar **solo** la copia local exacta ya disponible hacia:

`models/text2trade_mnrl_v0.2/model.safetensors`

pero únicamente si verifica exactamente:

- size = `470637416` bytes;
- SHA-256 = `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`.

No descargues pesos.
No sustituyas modelo.
No cambies hashes.
Nunca stages ni commitees el modelo.

---

# 3. PREFLIGHT AUTORIZADO READ-ONLY

Antes de Attempt04 ejecuta una sola vez, de forma read-only, `preflight_authorized()` de:

`src.experiments.run_0b05c_corrective_numerical_v03`

Debe devolver como mínimo:

- `status = PASS`;
- `mode = AUTHORIZED_PREFLIGHT_ONLY`;
- `execution_authorization_commit = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- `authorization_baseline_commit = 8b1444aed67d322714189846f98a3169145ea3d4`;
- cuatro autorizaciones del gate = `AUTHORIZED`;
- tres specs propios = `AUTHORIZED`;
- Attempt04 coherente = `AUTHORIZED / NOT_EXECUTED`;
- authorization record válido;
- transición inmutable PASS;
- dependency bindings PASS;
- modelo con identidad exacta;
- 16 future roots ausentes;
- cero side effects.

Si falla: **STOP / ATTEMPT04_NOT_STARTED**.

No invoques la ejecución.
No ejecutes suites que produzcan outputs científicos.
No ejecutes EV03/EV04/D1a por separado.

---

# 4. ATTEMPT04 — EXACTAMENTE UNA INVOCACIÓN

Si y solo si la sección 3 pasa, ejecuta **exactamente una vez**:

```bash
python -B -m src.experiments.run_0b05c_corrective_numerical_v03 --execute-authorized
```

Reglas absolutas:

1. **Una sola invocación de `--execute-authorized`.**
2. No retry.
3. No resume.
4. No repetir por timeout, interrupción, excepción, exit code no cero o output parcial.
5. No ejecutar EV03, EV04 o D1a manualmente antes ni después.
6. No editar código/JSON/output para “hacer pasar” una etapa.
7. No borrar ni limpiar roots parciales si falla.
8. No cambiar la autorización durante o después de la corrida.
9. No iniciar Attempt05.
10. Una vez invocado `--execute-authorized`, considera la autorización de una sola ejecución **operativamente consumida**, independientemente de PASS o FAIL. Su microcierre/versionado posterior será decidido tras auditoría externa.

Captura para el reporte, sin crear archivos extra dentro de los roots contractuales:

- comando exacto;
- número de invocaciones de ejecución (=1);
- hora local de inicio/fin si está disponible;
- exit code;
- stdout/stderr relevante;
- último paso iniciado;
- último paso completado;
- excepción exacta si existe.

La llamada interna a `preflight_authorized()` realizada por `--execute-authorized` forma parte de esa única ejecución y no cuenta como segundo Attempt.

---

# 5. BIFURCACIÓN FAIL-CLOSED

## 5.A — Si el preflight autorizado falla antes de ejecutar

Clasifica:

`0B05C_ATTEMPT04 = NOT_STARTED / AUTHORIZATION_NOT_CONSUMED_BY_NUMERICAL_INVOCATION`

No hagas ejecución ni commit científico.
Persiste únicamente el reporte administrativo y termina.

## 5.B — Si Attempt04 fue invocado y falla

Ante exit code no cero, excepción, interrupción o timeout:

- **NO REINTENTAR**;
- no limpiar ni borrar ningún root/archivo generado;
- no ejecutar ninguna parte manualmente;
- no calcular métricas faltantes;
- no intentar completar ledger/manifest fuera del runner;
- no crear commit científico de resultados parciales;
- deja la evidencia local exactamente como quedó.

Haz únicamente inventario read-only:

- cuáles de los 16 future roots existen;
- archivos creados y tamaños/SHA-256 cuando sea razonable;
- presencia/ausencia de runtime authorization record;
- último paso iniciado/completado;
- error exacto.

Clasifica:

`0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / AUTHORIZATION_CONSUMED`

La autorización integrada queda como evidencia histórica de que Attempt04 estaba permitido, pero **no autoriza otro Attempt automáticamente**.

No push de outputs parciales.
No modifiques `main`.
Persiste el reporte administrativo y termina.

## 5.C — Si Attempt04 termina con exit code 0

No declares PASS científico solo por el exit code. Continúa con las verificaciones read-only de secciones 6–9.

---

# 6. VALIDACIÓN POST-EJECUCIÓN — SOLO SI EXIT CODE 0

## 6.1 Orden y completitud

La respuesta del runner debe declarar `status=PASS` y completar exactamente los 19 pasos en este orden:

1. `01_unified_preflight`
2. `02_EV03_Decision885_control_reproduction`
3. `03_EV03_control_reproduction_verification`
4. `04_EV03_corrected_corpus_materialization`
5. `05_EV03_corrected_index_build_RECOVERED_HISTORICAL_SEMANTICS`
6. `06_EV03_corrected_evaluation`
7. `07_EV04_Decision885_control_reproduction_ENRICHED_MRR`
8. `08_EV04_control_reproduction_verification_PASS_EXACT`
9. `09_EV04_corrected_corpus_materialization`
10. `10_EV04_corrected_index_build`
11. `11_EV04_corrected_evaluation_ENRICHED_MRR`
12. `12_D1a_corrected_execution_under_future_v03_authorization`
13. `13_integrity_validation`
14. `14_case_level_comparisons`
15. `15_aggregate_comparisons`
16. `16_unified_sensitivity_summary`
17. `17_execution_manifest`
18. `18_exact_hash_ledger`
19. `19_final_completion_state`

`verify_ev03` y `verify_ev04` deben haber pasado como `PASS_EXACT`, no como `PASS` simple.

## 6.2 EV03 Decision885 control

Exige y reporta:

- `PASS_EXACT`;
- `LOGICAL_INDEX_IDENTITY = EXACT`;
- ranking/case summary exactos contra el control congelado;
- hashes/bytes/rows/cases exactos;
- métricas exactas.

Los hashes congelados relevantes continúan siendo:

- ranking SHA-256 `d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015`;
- case summary SHA-256 `f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0`.

## 6.3 EV04 Decision885 control enriquecido

Exige y reporta:

- `PASS_EXACT`;
- ranking exacto;
- case summary exacto;
- enriched metrics exactas, incluido contrato MRR@100/MRR@200;
- ningún fallback a esquema legacy incompleto.

Hashes congelados relevantes:

- ranking SHA-256 `fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662`;
- case summary SHA-256 `17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634`.

Si EV03 o EV04 no es `PASS_EXACT`, el resultado completo no puede clasificarse PASS.

## 6.4 Runtime authorization provenance

Verifica:

`outputs/audits/0b05c_corrective_numerical_runtime_v0.3/runtime_authorization_record_v0.3.json`

Debe bindear como mínimo:

- `execution_authorization_commit = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- `authorization_baseline_commit = 8b1444aed67d322714189846f98a3169145ea3d4`;
- cuatro autorizaciones;
- authorization record comprometido;
- bindings autorizados de gate + EV03 + EV04 + D1a.

El execution manifest debe preservar esa procedencia.

## 6.5 D1a

Verifica coherencia de:

- corrected corpus;
- índice completo;
- evaluación N=1056;
- ranking Top200;
- case summary;
- comparación case-level;
- comparación aggregate;
- execution manifest;
- D1a hash ledger.

El aggregate comparison debe contener exactamente las 17 métricas congeladas, con nombres/orden/schema contractuales.

No cambies ni reentrenes el modelo.

## 6.6 Exact runtime ledger

Verifica:

`outputs/audits/0b05c_corrective_numerical_runtime_v0.3/exact_hash_ledger_v0.3.json`

Debe:

- tener `status=PASS`;
- `mismatch_count=0`;
- validar exactamente el allowlist de `runtime_hash_ledger_contract.expected_paths`;
- no tener faltantes ni extras en los `discovery_roots`;
- registrar path + SHA-256 + size para cada output;
- excluir solo su propio path según contrato.

---

# 7. EXTRAER RESULTADOS SIN INTERPRETAR EL IMPACTO

Solo si la validación completa de sección 6 pasa, reporta factual y mecánicamente:

## EV03

- métricas Decision885 control;
- métricas Decision906 corrected;
- deltas aggregate;
- número de casos cuyo ranking cambió;
- casos/códigos afectados por `87044110` / `87045110` cuando el artefacto los identifique.

## EV04

- mismas categorías;
- incluye explícitamente MRR@100 y MRR@200 cuando estén en el aggregate comparison.

## D1a

- 17 métricas originales;
- 17 métricas corregidas;
- `absolute_delta` de cada una;
- número de casos con cambio de ranking según comparación case-level.

## Unified

Resume únicamente el contenido generado por:

`outputs/evaluation/0b05c_corrective_numerical_v0.3/unified_sensitivity_summary_v0.3.json`

**No declares todavía** `0B05C_METRIC_IMPACT` como material/no material.
No decidas downstream.
No cierres 0B-05C.

---

# 8. INVENTARIO DEL WORKTREE — SOLO SI PASS COMPLETO

Después de un PASS completo:

- los cambios deben limitarse a outputs contractuales dentro de los 16 future roots v0.3;
- no debe haber cambios en gate/specs/authorization record/código/tests/docs/Plan/article/v0.1/v0.2/failure record Attempt03;
- no debe haber outputs científicos inesperados;
- el modelo local nunca se stagea.

Construye el conjunto de paths contractual como:

1. todos los paths de `runtime_hash_ledger_contract.expected_paths` del gate integrado;
2. más el propio:
   `outputs/audits/0b05c_corrective_numerical_runtime_v0.3/exact_hash_ledger_v0.3.json`.

Compara ese conjunto con los archivos realmente generados dentro de los `discovery_roots`.

Si hay faltantes o extras: **STOP / PASS_NOT_VERSIONABLE**.
No edites, muevas, comprimas ni elimines archivos para forzar coincidencia.

---

# 9. VERSIONADO DE RESULTADOS — SOLO SI PASS COMPLETO E INVENTARIO EXACTO

Si y solo si se cumplen las secciones 6–8:

1. stagea **únicamente** el conjunto contractual de outputs descrito en sección 8;
2. si están ignorados, usa `git add -f` solo sobre esos paths exactos;
3. nunca stages modelo, evidencia Attempt01/02/03, caches, temporales o archivos no contractuales;
4. verifica staged diff e inventario antes del commit;
5. crea un único commit científico en:
   `codex/0b05c-numerical-attempt04-v03`;
6. mensaje sugerido:
   `feat: execute 0b05c v0.3 numerical sensitivity attempt04`;
7. el parent del commit científico debe ser exactamente `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
8. push únicamente esa rama;
9. **NO merge a `main`**;
10. no modifiques gate/specs para marcar executed/consumed; eso se hará solo después de auditoría externa.

Reporta:

- commit SHA;
- parent;
- tree;
- changed path count;
- lista completa de paths versionados;
- push.

Si Git/GitHub rechaza un output por tamaño u otra limitación, no alteres/comprimas/dividas/eludas el contrato por iniciativa propia. STOP y reporta.

---

# 10. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Solo después de terminar el trabajo científico —NOT_STARTED, PASS o FAIL_CLOSED— realiza un paso administrativo separado:

1. fetch + checkout `codex/prompts-temporary`;
2. crea únicamente:

`codex_prompts_tmp/23_RESPUESTA_EJECUTAR_ATTEMPT04_NUMERICO_0B05C_V03.md`

3. no modifiques este Prompt23 ni respuestas anteriores;
4. commit administrativo solo con ese archivo;
5. mensaje sugerido:
   `docs: persist prompt 23 attempt04 numerical report`;
6. push normal sin rebase/amend/force.

No mezcles el commit administrativo con el científico.

---

# 11. REPORTE FINAL OBLIGATORIO

Responde únicamente con las secciones aplicables:

### A. Preflight Git y autorización
Heads/tree/Plan/article, gate/specs/record, roots ausentes y modelo.

### B. Preflight autorizado
Resultado exacto, modo y cero side effects.

### C. Attempt04
Comando, número de invocaciones, inicio/fin, exit code, último paso iniciado/completado y error si existe.

### D. Controles EV03/EV04
PASS_EXACT y checks/hashes o punto exacto del fallo.

### E. D1a
Estado de ejecución, artefactos y 17 métricas si PASS.

### F. Runtime provenance / manifest / ledger
Estado, bindings, mismatch/faltantes/extras.

### G. Resultados numéricos
EV03/EV04/D1a/unified sin interpretación de impacto, solo si PASS completo.

### H. Aislamiento
Paths contractuales, ausencia de cambios fuera de alcance, Plan/article/EXP11B/EXP12/v0.1/v0.2.

### I. Commit científico
Si PASS completo y versionable: branch/SHA/parent/tree/paths/push.
Si FAIL o NOT_STARTED: `NO_SCIENTIFIC_COMMIT`.

### J. Persistencia administrativa
Response branch/path y commit response-only.

### K. Estado científico final

## Si PASS completo y versionado

Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`

`0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT04`

`0B05C_ATTEMPT04 = EXECUTED / CANDIDATE_RESULTS_PENDING_EXTERNAL_AUDIT`

`EV03_V03_NUMERICAL_EXECUTION = EXECUTED / PENDING_EXTERNAL_AUDIT`

`EV04_V03_NUMERICAL_EXECUTION = EXECUTED / PENDING_EXTERNAL_AUDIT`

`D1A_V03_NUMERICAL_EXECUTION = EXECUTED / PENDING_EXTERNAL_AUDIT`

`UNIFIED_0B05C_V03_NUMERICAL_EXECUTION = EXECUTED / PENDING_EXTERNAL_AUDIT`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

## Si Attempt04 fue invocado y falla

Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`

`0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT04`

`0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`

`ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

## Si el preflight falla y la ejecución nunca fue invocada

Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`

`0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / NOT_CONSUMED_BY_NUMERICAL_INVOCATION`

`0B05C_ATTEMPT04 = NOT_STARTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No cierres 0B-05C.
No inicies EXP11B ni EXP12.
No actualices el Plan Maestro ni el artículo en este bloque.
