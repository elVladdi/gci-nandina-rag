# CODEX — MICROCLOSE ATTEMPT03 FAIL-CLOSED Y CONSUMIR AUTORIZACIÓN 0B-05C v0.2

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE MICROCLOSE CIENTÍFICO POST-FALLO** de Attempt03.

Attempt03 ya fue ejecutado una única vez bajo la autorización integrada v0.2 y reportó fallo fail-closed. Este bloque **NO autoriza ni ejecuta Attempt04**, no reintenta Attempt03 y no genera resultados numéricos.

Objetivos únicos:

1. versionar un registro científico mínimo y auditable del fallo de Attempt03, sin versionar outputs parciales locales;
2. consumir/revocar mecánicamente la readiness de la autorización v0.2 para impedir su reutilización automática;
3. congelar la causa técnica demostrable del fallo EV04 como deuda de recuperación posterior;
4. dejar preparado el repositorio para un futuro gate prospectivo v0.3 separado, todavía NO construido ni autorizado en este bloque.

---

## 1. IDENTIDADES OBLIGATORIAS DE PREFLIGHT

Haz fetch y verifica exactamente:

- `origin/main = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- tree de `41d3259...` = `4d0703327c2d9e05ecf19fd04f5a8c7d808bd0f6`;
- parent = `c44f447cb941c512cd70712cf7c3e4bc670ab05a`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- gate v0.2 en `main`:
  - `gate_status = APPROVED / INTEGRATED`;
  - `authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
  - cuatro autorizaciones = `AUTHORIZED`;
  - `authorization_record_present=true`;
  - `corrective_retrieval_executed=false`;
  - `corrective_metrics_computed=false`;
- authorization record v0.2 presente y baseline `c44f447...`;
- no existe en `main` un registro científico de Attempt03;
- no existe commit científico de outputs parciales Attempt03.

Fetch también `codex/prompts-temporary` y verifica como **evidencia administrativa externa, nunca como rama científica**:

- commit de persistencia Prompt15 = `a449a3127a52e4b17948fd7fe6a3040a24f02ebd`;
- response path = `codex_prompts_tmp/15_RESPUESTA_EJECUTAR_ATTEMPT03_NUMERICO_0B05C_V02.md`;
- Git blob SHA-1 esperado del response = `c83b7d9004433ee1f369989dd6a5c7b9800c8e0d`.

Si cualquiera difiere: **STOP / NO MICROCLOSE**.

No limpies ni borres evidencia local/ignored de Attempt01/02/03.

---

## 2. EVIDENCIA ESTÁTICA OBLIGATORIA DE CAUSA RAÍZ

Antes de escribir, verifica directamente en Git la cadena histórica:

- runner jerárquico original recreado: `ce239059d748a4baf8a2113df5398f50c0e14a58`;
- outputs EXP-04 jerárquicos iniciales: `001580944b417e81634dd6d11a9d2facc9ed29be`;
- microaudit MRR Gate C: `ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97`;
- source actual `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py` Git blob SHA-1 = `aadbec6bdc5c152def0a7e925d2cf30f16aa4c7d`;
- corrective evaluator `src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py` Git blob SHA-1 = `c6f4121fe5f5f50e71e27eb4cf1e28eb8986d062`.

Demuestra mecánicamente:

1. `metrics_from_cases()` en `ce23905...` y en el source actual genera una fila legacy `mrr` y no produce de origen el esquema enriquecido `mrr_at_100` / `mrr_at_200`;
2. el commit `ef9faef...` modificó los artefactos congelados `normative_hierarchical_metrics.json` y `run_metadata.json`, más tests/documentación, para introducir la microauditoría MRR@100/MRR@200;
3. `ef9faef...` **no modificó** `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`;
4. el `run_metadata.json` congelado actual contiene `metric_table` empezando por `mrr_at_100`, `mrr_at_200` y campos `mrr_at_100*`, `mrr_at_200*`, `mrr_101_200_contribution*`, `mrr_definition`;
5. `compare_control_reproduction()` exige igualdad completa `expected_metrics == actual_metrics`.

La clasificación causal a congelar es exactamente:

`EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT`

No clasifiques el fallo como ranking drift ni retrieval drift: el reporte local de Attempt03 declaró bytes/hashes exactos de ranking y case summary, mientras la divergencia fue de `metrics_exact`.

---

## 3. RAMA CIENTÍFICA DE MICROCLOSE

Desde exactamente `41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`, crea y usa:

`codex/0b05c-attempt03-failclosed-microclose`

Un único commit científico encima de `41d3259...`.

No rebase, amend, squash, cherry-pick ni force-push.

---

## 4. CAMBIOS CIENTÍFICOS PERMITIDOS — EXACTAMENTE DOS PATHS

Modifica/crea exclusivamente:

1. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`
2. nuevo: `outputs/audits/0b05c_attempt03_failclosed_v0.2/attempt03_failure_record_v0.2.json`

Ningún otro path científico puede cambiar.

### 4.1 Gate v0.2 — consumir readiness sin reescribir la historia

En el gate existente cambia **únicamente**:

`authorization_readiness`:

- de `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`
- a `ATTEMPT03_CONSUMED / REAUTHORIZATION_REQUIRED`

No cambies:

- `gate_status = APPROVED / INTEGRATED`;
- las cuatro autorizaciones `AUTHORIZED` — representan la autorización histórica concedida a Attempt03;
- `authorization_record_present=true`;
- `corrective_retrieval_executed=false`;
- `corrective_metrics_computed=false`;
- `runtime_authorization_record_present=false`;
- patches, roots, commands, semantics, metrics, builders, evaluators, model policy, code bindings, execution order, comparison schemas y runtime contracts.

La nueva readiness debe hacer que `preflight_authorized()` falle **antes de cualquier side effect** con la autorización v0.2 ya consumida.

### 4.2 Attempt03 failure record

Crea JSON UTF-8/LF con schema estable y sin timestamps inventados:

```json
{
  "artifact_id": "0b05c_attempt03_failure_record_v0.2",
  "schema_version": 1,
  "attempt_id": "ATTEMPT03",
  "authorization_commit": "41d3259ff09d8a63cc3a12a7f11a146a603ee3ef",
  "authorization_baseline_commit": "c44f447cb941c512cd70712cf7c3e4bc670ab05a",
  "status": "FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED",
  "authorization_consumed": true,
  "automatic_reuse_authorized": false,
  "attempt04_authorized": false,
  "exit_code_reported": 1,
  "completed_steps_reported": 6,
  "total_pipeline_steps": 19,
  "last_completed_step_reported": "06_EV03_corrected_evaluation",
  "last_started_step_reported": "07_EV04_Decision885_control_reproduction",
  "exception_reported": "src.experiments.run_d1a_corrective_0b05c_v01.ContractViolation: Mandatory control reproduction is not exact",
  "failure_class": "EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT",
  "runtime_partial_outputs": "LOCAL_PRESERVED_NOT_VERSIONED",
  "metric_impact": "NOT_DETERMINED",
  "downstream_reexecution": "NOT_YET_JUSTIFIED",
  "closure": "NOT_AUTHORIZED",
  "administrative_execution_report": {
    "branch": "codex/prompts-temporary",
    "commit": "a449a3127a52e4b17948fd7fe6a3040a24f02ebd",
    "path": "codex_prompts_tmp/15_RESPUESTA_EJECUTAR_ATTEMPT03_NUMERICO_0B05C_V02.md",
    "git_blob_sha1": "c83b7d9004433ee1f369989dd6a5c7b9800c8e0d",
    "evidence_classification": "CODEX_LOCAL_EXECUTION_REPORT_NOT_INDEPENDENTLY_VERSIONED_RUNTIME_OUTPUTS"
  },
  "static_root_cause_evidence": {
    "original_runner_commit": "ce239059d748a4baf8a2113df5398f50c0e14a58",
    "initial_outputs_commit": "001580944b417e81634dd6d11a9d2facc9ed29be",
    "gate_c_mrr_microaudit_commit": "ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97",
    "current_hierarchical_runner_git_blob_sha1": "aadbec6bdc5c152def0a7e925d2cf30f16aa4c7d",
    "corrective_evaluator_git_blob_sha1": "c6f4121fe5f5f50e71e27eb4cf1e28eb8986d062",
    "ranking_or_case_drift_established": false,
    "metric_schema_drift_established": true
  }
}
```

Puedes añadir únicamente campos de evidencia que sean necesarios para representar de manera inequívoca hechos ya contenidos en el reporte Prompt15 o verificables directamente desde Git. No introduzcas como hechos independientes los hashes de archivos parciales locales: si se incluyen, deben quedar explícitamente marcados como `REPORTED_LOCAL_ONLY / NOT_VERSIONED`.

---

## 5. VALIDACIÓN READ-ONLY OBLIGATORIA

Antes del push:

1. compare `41d3259...` → candidato = exactamente **1 commit / 2 paths**;
2. el failure record cumple schema y estados exactos;
3. la única diferencia del gate es `authorization_readiness`;
4. ejecuta `preflight_authorized()` de v0.2 de forma read-only sobre el candidato y exige que falle por readiness consumida **antes de crear cualquier future root**;
5. los 16 future roots no deben ser creados por este bloque;
6. no ejecutes `--execute-authorized`, retrieval, EV03, EV04, D1a ni modelo;
7. no copies ni stages el modelo;
8. `main`, Plan, article, EXP11B, EXP12 y artefactos v0.1 sin cambios.

No ejecutes tests que generen outputs científicos. Tests sintéticos/read-only son opcionales.

---

## 6. COMMIT Y PUSH

Si todo pasa:

- commit único sobre `41d3259...`;
- mensaje sugerido:
  `chore: record attempt03 fail-closed and consume v0.2 authorization`
- push únicamente a:
  `codex/0b05c-attempt03-failclosed-microclose`
- no merge a `main`.

Reporta commit SHA, parent, tree, compare y dos changed paths exactos.

---

## 7. PERSISTENCIA ADMINISTRATIVA

Solo después del push científico:

1. fetch/checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/16_RESPUESTA_MICROCLOSE_ATTEMPT03_FAIL_CLOSED_Y_CONSUMIR_AUTORIZACION_V02.md`;
3. commit administrativo separado, response-only;
4. mensaje sugerido:
   `docs: persist prompt 16 attempt03 fail-closed microclose report`;
5. push normal, sin rebase/amend/force.

---

## 8. REPORTE FINAL OBLIGATORIO

Responde únicamente con:

### A. Preflight Git
Identidades y estados iniciales.

### B. Auditoría estática de causa raíz
Prueba de `ce23905`/`0015809`/`ef9faef`, source actual y equality estricta.

### C. Failure record
Contenido, clasificación de evidencia y binding al Prompt15.

### D. Consumo de autorización v0.2
Cambio exacto de readiness y prueba de que el preflight v0.2 queda bloqueado.

### E. Diff y aislamiento
Dos paths exactos y ramas no tocadas.

### F. Commit candidato
Branch/SHA/parent/tree/compare/push.

### G. Persistencia administrativa
Response path y estado.

### H. Estado científico
Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED (HISTORICAL)`

`0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT03 (CANDIDATE_MICROCLOSE)`

`0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_CANDIDATE`

`EV04_RECOVERY_ROOT_CAUSE = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT`

`0B05C_V03_RECOVERY_GATE = NOT_YET_BUILT / NOT_AUTHORIZED`

`ATTEMPT04 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No construyas v0.3 todavía. No autorices Attempt04.