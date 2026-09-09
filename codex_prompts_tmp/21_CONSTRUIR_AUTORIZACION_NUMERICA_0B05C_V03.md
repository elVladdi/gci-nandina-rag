# CODEX — CONSTRUIR AUTORIZACIÓN NUMÉRICA 0B-05C v0.3 PARA ATTEMPT04

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE CONSTRUCCIÓN DE LA AUTORIZACIÓN NUMÉRICA v0.3**.

El gate de recuperación v0.3 ya fue auditado externamente e integrado en `main`. Este bloque debe construir, en una rama científica separada, la transición prospectiva y auditable desde el baseline preautorización integrado hacia una autorización de **una sola ejecución futura** de Attempt04.

Este bloque:

- **NO ejecuta Attempt04**;
- **NO ejecuta retrieval, EV03, EV04, D1a, EVAL real ni el modelo**;
- **NO genera outputs runtime v0.3**;
- **NO integra a `main`**;
- únicamente construye el candidato de autorización que será auditado externamente antes de cualquier integración.

---

# 1. BASELINE GIT OBLIGATORIO

Haz fetch y verifica exactamente antes de escribir:

- `origin/main = 8b1444aed67d322714189846f98a3169145ea3d4`;
- tree = `7543d15b8b692408e5eaa4fc9b93f2a19f42eb78`;
- parent = `815309b2b4ab6df2307d534ba20ec76e8077dcff`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Verifica en `main` el baseline v0.3 integrado:

- gate path:
  `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`;
- EV03 spec v0.3;
- EV04 spec v0.3;
- D1a spec v0.3;
- `gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT`;
- `authorization_readiness = NOT_AUTHORIZATION_READY`;
- las cuatro autorizaciones numéricas del gate = `NOT_AUTHORIZED`;
- autorización propia de EV03 spec = `NOT_AUTHORIZED`;
- autorización propia de EV04 spec = `NOT_AUTHORIZED`;
- autorización propia de D1a spec = `NOT_AUTHORIZED`;
- `attempt04 = NOT_AUTHORIZED / NOT_EXECUTED` en gate y los tres specs;
- `authorization_record_present = false`;
- `runtime_authorization_record_present = false`;
- `corrective_retrieval_executed = false`;
- `corrective_metrics_computed = false`;
- el authorization record v0.3 no existe;
- ninguno de los 16 future roots v0.3 existe.

Si cualquier identidad o estado difiere: **STOP / NO AUTHORIZATION BUILD**.

No borres ni limpies evidencia local de Attempt01/02/03.

---

# 2. RAMA Y ALCANCE EXACTO

Crea desde exactamente `8b1444aed67d322714189846f98a3169145ea3d4` la rama:

`codex/0b05c-numerical-authorization-v03`

El candidato científico debe modificar **exactamente cinco paths**:

1. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev03_numerical_execution_spec_v0.3.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev04_numerical_execution_spec_v0.3.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/d1a_numerical_execution_spec_v0.3.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_numerical_authorization_record_v0.3.json`

No modifiques ningún otro archivo. En particular, no modifiques código, tests, manifest, hash ledger, documentación, v0.1/v0.2, failure record Attempt03, Plan, article, EXP11B ni EXP12.

---

# 3. AUTHORIZATION RECORD v0.3 — CONTRATO EXACTO

Crea el nuevo archivo:

`outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_numerical_authorization_record_v0.3.json`

Debe tener **exactamente** los cinco campos definidos por el contrato versionado:

- `artifact_id` = `0b05c_numerical_authorization_record_v0.3`;
- `schema_version` = `3`;
- `authorization_baseline_commit` = `8b1444aed67d322714189846f98a3169145ea3d4`;
- `baseline_external_audit` = `PASS / APPROVED_FOR_INTEGRATION`;
- `baseline_artifacts`.

`baseline_artifacts` debe contener exactamente:

- `unified_gate`;
- `ev03_spec`;
- `ev04_spec`;
- `d1a_spec`.

Para cada uno calcula **desde el commit baseline 8b1444...**, no desde working tree ni desde valores manuales:

- `path`;
- `git_blob_sha1`;
- `canonical_git_blob_sha256`;
- `canonical_size_bytes`.

Usa la implementación versionada en v0.3 (`authorization_artifact_binding` / `git_binding`) o una equivalencia byte-exacta. No inventes hashes.

Antes del commit valida el schema con `validate_authorization_record_schema()` y los bindings con `validate_authorization_record_bindings()`.

---

# 4. TRANSICIÓN AUTORIZADA EXACTA

La transición baseline → candidato debe cambiar exclusivamente los campos permitidos por la proyección inmutable F011.

## 4.1 Gate v0.3

Cambia únicamente:

- `gate_status`:
  `CANDIDATE_PENDING_EXTERNAL_AUDIT` → `APPROVED / INTEGRATED`;
- `authorization_readiness`:
  `NOT_AUTHORIZATION_READY` → `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- `authorization.EV03_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `authorization.EV04_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `authorization.D1A_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `authorization.UNIFIED_0B05C_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `authorization.authorization_record_present` → `true`;
- `attempt04` → `AUTHORIZED / NOT_EXECUTED`.

Deben permanecer sin cambios y en `false`:

- `corrective_retrieval_executed`;
- `corrective_metrics_computed`;
- `runtime_authorization_record_present`.

No cambies ningún otro campo del gate.

## 4.2 EV03 spec

Cambia únicamente:

- `authorization.EV03_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `attempt04` → `AUTHORIZED / NOT_EXECUTED`.

Todos los demás campos deben ser byte/semánticamente idénticos al baseline.

## 4.3 EV04 spec

Cambia únicamente:

- `authorization.EV04_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `attempt04` → `AUTHORIZED / NOT_EXECUTED`.

No modifiques MRR, ranking, corpus, patch, depth ni ninguna otra semántica.

## 4.4 D1a spec

Cambia únicamente:

- `authorization.D1A_NUMERICAL_EXECUTION` → `AUTHORIZED`;
- `attempt04` → `AUTHORIZED / NOT_EXECUTED`.

Todos los flags `D1A_CORRECTIVE_*_CREATED/COMPUTED` deben permanecer `false`.

---

# 5. PRUEBA MECÁNICA DE LA TRANSICIÓN

Después de materializar los cinco archivos, pero antes de cualquier ejecución numérica:

1. carga los cuatro artefactos del baseline directamente desde Git `8b1444...`;
2. carga los cuatro artefactos autorizados del candidato;
3. ejecuta la lógica versionada `validate_authorization_transition()`;
4. exige:
   - `status = PASS`;
   - `mode = BASELINE_TO_AUTHORIZED_IMMUTABLE_PROJECTION`;
   - `allowed_fields_only = true`;
   - `baseline_projection_sha256 == authorized_projection_sha256`.

Cualquier diferencia científica/técnica fuera de los campos autorizados debe detener el bloque.

---

# 6. PREFLIGHT AUTORIZADO — SOLO READ-ONLY

Después de crear **un único commit candidato**, usa un checkout/worktree detached limpio de ese commit.

Ejecuta únicamente el `preflight_authorized()` v0.3 de forma read-only.

Debe validar antes de cualquier side effect:

- gate `APPROVED / INTEGRATED`;
- readiness `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- cuatro autorizaciones del gate = `AUTHORIZED`;
- EV03/EV04/D1a specs propios = `AUTHORIZED`;
- Attempt04 coherente = `AUTHORIZED / NOT_EXECUTED`;
- authorization record presente, schema exacto y bindings exactos al baseline;
- baseline `8b1444...` es proper ancestor del candidato;
- proyección inmutable PASS;
- filesystem specs = committed specs;
- dependency bindings sin drift;
- modelo congelado con size/SHA exactos si está disponible y requerido por el preflight;
- 16 future roots v0.3 ausentes;
- `numerical_execution_occurred = false`.

**NO invoques `--execute-authorized`.**

Si por ausencia del archivo físico del modelo el preflight no puede completarse, reporta exactamente ese hecho y STOP: no simules ni omitas el control. En ese caso no declares el candidato listo para integración.

---

# 7. PROHIBICIONES DE EJECUCIÓN

En este bloque está prohibido:

- Attempt04;
- `--execute-authorized`;
- retrieval;
- EV03 real;
- EV04 real;
- D1a real;
- EVAL real;
- cargar/ejecutar inferencia del modelo;
- generar cualquier future root v0.3;
- crear runtime authorization record;
- producir métricas correctivas.

La única lectura permitida del modelo es la validación de identidad requerida por el preflight autorizado, sin inferencia.

---

# 8. COMMIT / PUSH

Haz exactamente **un commit científico candidato** sobre `8b1444aed67d322714189846f98a3169145ea3d4`.

Mensaje sugerido:

`chore: authorize single 0b05c v0.3 numerical execution`

Push únicamente a:

`codex/0b05c-numerical-authorization-v03`

No merge a `main`.
No rebase/amend/squash/cherry-pick/force-push.

El compare baseline → candidato debe ser:

- `1 ahead / 0 behind`;
- exactamente 1 commit;
- exactamente los 5 paths enumerados.

Reporta SHA, parent, tree y blobs de los cinco paths.

---

# 9. ESTADO CIENTÍFICO DEL CANDIDATO

Aunque los artefactos serializados del candidato representen la transición autorizada, **no declares Attempt04 ejecutado ni la autorización integrada**.

Estado de reporte correcto antes de auditoría externa:

- `0B05C_V03_AUTHORIZATION_CANDIDATE = BUILT / PENDING_EXTERNAL_AUDIT`;
- `ATTEMPT04 = AUTHORIZED_IN_CANDIDATE_ONLY / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

No uses `INTEGRATED` para describir la autorización candidata.

---

# 10. PERSISTENCIA ADMINISTRATIVA

Solo después del push científico:

1. fetch/checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/21_RESPUESTA_CONSTRUIR_AUTORIZACION_NUMERICA_0B05C_V03.md`;
3. commit administrativo response-only;
4. mensaje sugerido:
   `docs: persist prompt 21 v0.3 authorization candidate report`;
5. push normal, sin rebase/amend/force.

---

# 11. REPORTE FINAL OBLIGATORIO

Usa exactamente estas secciones:

### A. Preflight Git y baseline
### B. Authorization record v0.3
### C. Transición gate/specs
### D. Prueba de proyección inmutable
### E. Preflight autorizado read-only
### F. Prohibiciones y ausencia de ejecución
### G. Diff/commit/push
### H. Persistencia administrativa
### I. Estado científico

Distingue expresamente:

- hechos Git versionados;
- pruebas locales read-only de CODEX;
- ausencia de ejecución numérica.

Termina con:

`GROUP_2 = EN_CURSO`

`0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`

`0B05C_V03_AUTHORIZATION_CANDIDATE = BUILT / PENDING_EXTERNAL_AUDIT`

`ATTEMPT04 = AUTHORIZED_IN_CANDIDATE_ONLY / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`
