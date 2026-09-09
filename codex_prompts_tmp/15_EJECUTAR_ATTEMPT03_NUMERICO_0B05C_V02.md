# CODEX — EJECUTAR ATTEMPT03 NUMÉRICO 0B-05C v0.2

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE LA ÚNICA EJECUCIÓN NUMÉRICA AUTORIZADA 0B-05C v0.2 — Attempt03**.

La autorización numérica v0.2 ya fue auditada externamente e integrada en `main`.

Baseline científico/autorizado exacto:

`41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`

Estado externo autorizado:

- `0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED`;
- `0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED`;
- `0B05C_V02_AUTHORIZATION_READINESS = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- EV03/EV04/D1a/UNIFIED = `AUTHORIZED / NOT_EXECUTED`.

Este bloque **sí autoriza exactamente una invocación de la ejecución numérica unificada**. Está prohibido reintentar, reanudar, repetir o ejecutar componentes por separado.

No cierres 0B-05C ni decidas impacto/downstream. Eso corresponde a auditoría externa posterior.

---

# 1. PREFLIGHT GIT OBLIGATORIO — ANTES DE CUALQUIER SIDE EFFECT

Haz `fetch` y verifica exactamente:

- `origin/main = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- tree de `41d3259...` = `4d0703327c2d9e05ecf19fd04f5a8c7d808bd0f6`;
- parent de `41d3259...` = `c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- gate autorizado en `main` con:
  - `gate_status = APPROVED / INTEGRATED`;
  - `authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
  - cuatro estados `AUTHORIZED`;
  - `authorization_record_present=true`;
  - `runtime_authorization_record_present=false`;
  - `corrective_retrieval_executed=false`;
  - `corrective_metrics_computed=false`;
- authorization record v0.2 comprometido y válido, baseline `c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- EV03 spec = `AUTHORIZED`, retrieval/metrics false;
- EV04 spec = `AUTHORIZED`, retrieval/metrics false;
- D1a spec = `AUTHORIZED`, corpus/index/metrics-created false;
- los 16 `future_roots` v0.2 están ausentes;
- no existe `runtime_authorization_record_v0.2.json`;
- no existe `unified_sensitivity_summary_v0.2.json`;
- no hay resultados correctivos v0.2 previos.

No limpies ni borres ninguna evidencia local/ignored de Attempt01/Attempt02.

Si cualquier identidad/estado difiere: **STOP / ATTEMPT03_NOT_STARTED**.

---

# 2. RAMA Y WORKTREE DE EJECUCIÓN

No ejecutes directamente sobre una rama con commits adicionales ni modifiques `main`.

Desde exactamente `41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`, crea/usa:

`codex/0b05c-numerical-attempt03-v02`

Antes de ejecutar, la rama debe apuntar exactamente a `41d3259...` sin commits propios y el worktree tracked debe estar limpio.

Preferencia: usa un worktree aislado para Attempt03. Si el modelo congelado no está presente en ese worktree, puedes copiar **solo** la copia local exacta ya disponible hacia:

`models/text2trade_mnrl_v0.2/model.safetensors`

pero únicamente si verifica exactamente:

- size = `470637416` bytes;
- SHA-256 = `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`.

No descargues pesos, no sustituyas modelo, no cambies hashes y nunca stages/commitees el modelo.

---

# 3. PREFLIGHT AUTORIZADO READ-ONLY

Antes de Attempt03 invoca una sola vez, de forma read-only, `preflight_authorized()` de:

`src.experiments.run_0b05c_corrective_numerical_v02`

Debe devolver:

- `status=PASS`;
- `mode=AUTHORIZED_PREFLIGHT_ONLY`;
- `execution_authorization_commit=41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- `authorization_baseline_commit=c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- cuatro autorizaciones `AUTHORIZED`;
- modelo exacto;
- 16 roots ausentes;
- cero side effects.

Si falla: **STOP / ATTEMPT03_NOT_STARTED**. No invoques la ejecución.

No ejecutes suites que puedan crear outputs científicos y no ejecutes componentes EV03/EV04/D1a por separado.

---

# 4. ATTEMPT03 — EXACTAMENTE UNA INVOCACIÓN

Si y solo si el preflight anterior pasa, ejecuta **exactamente una vez**:

```bash
python -B -m src.experiments.run_0b05c_corrective_numerical_v02 --execute-authorized
```

Reglas absolutas:

1. **Una sola invocación.**
2. No retry.
3. No resume.
4. No volver a lanzar por timeout, interrupción, excepción, salida distinta de cero o resultado parcial.
5. No ejecutar EV03, EV04 o D1a manualmente antes ni después.
6. No editar archivos para “hacer pasar” una etapa.
7. No borrar/limpiar roots parciales si falla.
8. No cambiar autorización durante o después de la corrida.

Captura para el reporte, sin crear archivos extra dentro de los contractual runtime roots:

- comando exacto;
- hora de inicio/fin local si está disponible;
- exit code;
- stdout/stderr relevante;
- último paso iniciado/completado;
- excepción exacta si existe.

La invocación interna del preflight realizada por `--execute-authorized` forma parte de esa única ejecución y no cuenta como un segundo Attempt.

---

# 5. BIFURCACIÓN FAIL-CLOSED

## 5.A Si Attempt03 falla

Ante cualquier exit code no cero/excepción/interrupción:

- **NO REINTENTAR**;
- no limpiar ni borrar ningún root/archivo generado;
- no ejecutar ninguna parte manualmente;
- no calcular métricas faltantes;
- no intentar completar ledger/manifest por fuera del runner;
- no crear un commit científico de resultados parciales;
- deja la evidencia local exactamente como quedó.

Haz únicamente inventario read-only:

- cuáles de los 16 future roots existen;
- archivos creados y tamaños/hashes cuando sea razonable;
- presencia/ausencia de runtime authorization record;
- último paso alcanzado;
- error exacto.

Clasifica:

`0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`

La autorización integrada sigue siendo evidencia histórica de que Attempt03 estaba permitido, pero **no autoriza un Attempt04 automáticamente**.

Persiste el reporte administrativo y termina. No push de outputs parciales.

## 5.B Si Attempt03 termina con exit code 0

No des por válido el resultado solo por el exit code. Continúa con las verificaciones read-only de las secciones 6–9.

---

# 6. VALIDACIÓN POST-EJECUCIÓN OBLIGATORIA — SOLO SI EXIT 0

Verifica sin modificar outputs:

## 6.1 Orden y completitud

La respuesta del runner debe declarar `status=PASS` y completar los 19 pasos, en el orden congelado:

1. `01_unified_preflight`
2. `02_EV03_Decision885_control_reproduction`
3. `03_EV03_control_reproduction_verification`
4. `04_EV03_corrected_corpus_materialization`
5. `05_EV03_corrected_index_build_RECOVERED_HISTORICAL_SEMANTICS`
6. `06_EV03_corrected_evaluation`
7. `07_EV04_Decision885_control_reproduction`
8. `08_EV04_control_reproduction_verification`
9. `09_EV04_corrected_corpus_materialization`
10. `10_EV04_corrected_index_build`
11. `11_EV04_corrected_evaluation`
12. `12_D1a_corrected_execution_under_v02_authorization`
13. `13_integrity_validation`
14. `14_case_level_comparisons`
15. `15_aggregate_comparisons`
16. `16_unified_sensitivity_summary`
17. `17_execution_manifest`
18. `18_exact_hash_ledger`
19. `19_final_completion_state`

## 6.2 Controles originales

Exige y reporta:

- EV03 Decision885 control = `PASS_EXACT`;
- todos sus checks exactos true, incluido `LOGICAL_INDEX_IDENTITY=EXACT`, hashes/bytes/rows/cases/métricas;
- EV04 Decision885 control = `PASS_EXACT`;
- hashes exactos de ranking y case summary congelados.

Si cualquiera no es exacto, el resultado no puede clasificarse PASS aunque el proceso haya terminado.

## 6.3 Runtime authorization provenance

Verifica:

`outputs/audits/0b05c_corrective_numerical_runtime_v0.2/runtime_authorization_record_v0.2.json`

Debe bindear:

- `execution_authorization_commit=41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- baseline `c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- cuatro autorizaciones;
- authorization record comprometido;
- bindings autorizados gate + EV03 + EV04 + D1a.

El execution manifest debe referenciar ese runtime record mediante path + SHA-256 + size.

## 6.4 D1a

Verifica que existan y sean coherentes:

- corrected corpus;
- index completo;
- evaluación N=1056;
- ranking Top200;
- case summary;
- comparison case-level;
- aggregate comparison;
- execution manifest;
- D1a hash ledger.

El aggregate comparison debe contener exactamente las 17 métricas congeladas, nombres/orden/schema exactos.

## 6.5 Exact runtime ledger

Verifica:

`outputs/audits/0b05c_corrective_numerical_runtime_v0.2/exact_hash_ledger_v0.2.json`

Debe:

- tener `status=PASS`;
- `mismatch_count=0`;
- contener exactamente el allowlist contractual;
- no tener faltantes ni extras;
- incluir path + SHA-256 + size para cada output;
- excluir únicamente al propio ledger según contrato.

---

# 7. EXTRAER RESULTADOS SIN DECIDIR AÚN EL IMPACTO

Solo si la validación completa de sección 6 pasa, reporta factual y mecánicamente:

## EV03

- métricas Decision885 control;
- métricas Decision906 corrected;
- deltas aggregate;
- cantidad de casos con ranking cambiado;
- casos/códigos afectados por `87044110` / `87045110` cuando estén en los artefactos.

## EV04

Mismos elementos.

## D1a

- las 17 métricas originales;
- las 17 métricas corregidas;
- `absolute_delta` de cada una;
- cantidad de casos con cambio de ranking según comparación case-level.

## Unified

Resume únicamente la evidencia generada por `unified_sensitivity_summary_v0.2.json`.

**No declares todavía** `0B05C_METRIC_IMPACT` como material/no material, no decidas downstream y no cierres 0B-05C. Esa interpretación la hará la auditoría externa.

---

# 8. ESTADO DEL WORKTREE Y PATHS — SOLO SI PASS COMPLETO

Después de una ejecución PASS completa:

- los cambios del worktree deben limitarse a outputs contractuales generados dentro de los 16 future roots;
- no debe haber cambios en gate/specs/authorization record/código/tests/docs/Plan/article/v0.1;
- no debe haber outputs científicos inesperados;
- el modelo local no se stagea ni se versiona.

Compara el inventario real contra `runtime_hash_ledger_contract.expected_paths`.

Si aparece cualquier archivo inesperado dentro del contrato: **STOP / PASS_NOT_VERSIONABLE** y no commits resultados hasta auditoría externa.

---

# 9. VERSIONADO DE RESULTADOS — SOLO SI PASS COMPLETO E INVENTARIO EXACTO

Si y solo si se cumplen secciones 6–8:

1. stagea **únicamente** los outputs contractuales generados de Attempt03;
2. si están ignorados, usa `git add -f` solo sobre los paths exactos del allowlist contractual;
3. nunca stages modelo, evidencia Attempt01/02, caches, temporales o archivos no contractuales;
4. verifica staged diff/inventory antes del commit;
5. crea un único commit científico en:
   `codex/0b05c-numerical-attempt03-v02`;
6. mensaje sugerido:
   `feat: execute 0b05c v0.2 numerical sensitivity attempt03`;
7. push únicamente esa rama;
8. **NO merge a `main`**;
9. no modifiques gate/specs para marcar executed; eso será un bloque posterior después de auditoría.

Reporta commit SHA, parent exacto `41d3259...`, tree, changed path count y lista completa de paths versionados.

Si Git/GitHub rechaza algún output por tamaño u otra limitación: no alteres/comprimas/eludas el contrato por iniciativa propia. STOP y reporta el bloqueo.

---

# 10. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Solo después de terminar el trabajo científico —PASS o FAIL_CLOSED— realiza un paso administrativo separado:

1. fetch + checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/15_RESPUESTA_EJECUTAR_ATTEMPT03_NUMERICO_0B05C_V02.md`;
3. no modifiques este Prompt 15 ni respuestas anteriores;
4. commit administrativo solo con ese archivo;
5. mensaje sugerido:
   `docs: persist prompt 15 attempt03 numerical report`;
6. push normal sin rebase/amend/force.

No mezcles el commit administrativo con el científico.

---

# 11. REPORTE FINAL OBLIGATORIO

Responde únicamente con las secciones aplicables:

### A. Preflight Git y autorización
Heads/tree/Plan/article, gate/specs/record, roots ausentes, model identity.

### B. Preflight autorizado
Resultado exacto y cero side effects.

### C. Attempt03
Comando, número de invocaciones (=1), exit code, último paso/19 pasos, error si existe.

### D. Controles EV03/EV04
PASS_EXACT y checks/hashes o punto exacto de fallo.

### E. D1a
Estado de ejecución, artefactos y 17 métricas si PASS.

### F. Runtime provenance / manifest / ledger
Estado y bindings; mismatch/faltantes/extras.

### G. Resultados numéricos
EV03/EV04/D1a/unified sin interpretación de impacto, solo si PASS completo.

### H. Aislamiento
Cambios permitidos, ausencia de cambios en ciencia congelada, Plan/article/EXP11B/EXP12/v0.1.

### I. Commit científico
Si PASS completo: branch/SHA/parent/tree/paths/push. Si FAIL: `NO_SCIENTIFIC_COMMIT`.

### J. Persistencia administrativa
Response branch/path y PASS.

### K. Estado científico final

Si PASS completo y versionado, termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED`

`0B05C_ATTEMPT03 = EXECUTED / CANDIDATE_RESULTS_PENDING_EXTERNAL_AUDIT`

`EV03_V02_NUMERICAL_EXECUTION = EXECUTED / PENDING_EXTERNAL_AUDIT`

`EV04_V02_NUMERICAL_EXECUTION = EXECUTED / PENDING_EXTERNAL_AUDIT`

`D1A_V02_NUMERICAL_EXECUTION = EXECUTED / PENDING_EXTERNAL_AUDIT`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = EXECUTED / PENDING_EXTERNAL_AUDIT`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

Si falla, termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED`

`0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No declares 0B-05C cerrado y no inicies EXP11B/EXP12.