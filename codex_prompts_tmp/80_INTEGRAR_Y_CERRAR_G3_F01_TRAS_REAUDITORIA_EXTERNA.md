# PROMPT 80 — INTEGRAR Y CERRAR G3-F01 TRAS REAUDITORÍA EXTERNA

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

La IA Experimental realizó la reauditoría externa independiente del contrato analítico corregido de G3-F01 en:

```text
branch = codex/group3-f01-analytical-contract-v01
head = 366bf529c29cb999bfd043db33674a510ba184c7
base_main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
```

Dictamen externo:

```text
G3_F01_SCIENTIFIC_REAUDIT = PASS
G3_F01_ADMINISTRATIVE_RECONCILIATION = REQUIRED_BEFORE_CLOSURE
SCIENTIFIC_RERUN_REQUIRED = false
INFERENTIAL_EXECUTION_AUTHORIZED = false
G3_F02_AUTHORIZED = false
```

La corrección Prompt79 resolvió los hallazgos científicos/metodológicos del contrato: completó bindings y campos por familia, corrigió la evidencia de HE2, preservó SERIE como unidad analítica con DAM como agrupamiento de dependencia, prohibió pseudorreplicación de EXP11B, mantuvo HE5 conservador, documentó la desviación de acceso de SRC-01 y dejó explícita la reconciliación administrativa pendiente.

Este Prompt80 tiene un único objetivo: **integrar el contrato G3-F01 aprobado, reconciliar retrospectivamente su activación documental y cerrar G3-F01 sin abrir ni ejecutar G3-F02**.

No recalcules métricas. No ejecutes bootstrap. No calcules intervalos, p-values o decisiones HE2/HE5. No reejecutes ningún experimento. No modifiques `article/main-manuscript`.

---

## 1. Preflight remoto obligatorio

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
origin/codex/group3-f01-analytical-contract-v01 = 366bf529c29cb999bfd043db33674a510ba184c7
origin/codex/prompts-temporary = <commit que contiene este Prompt80>
```

La rama editorial puede haber avanzado y no gobierna este cierre administrativo. No la modifiques.

Si `main`, Plan, fichas o la rama científica candidata difieren de los SHA anteriores:

```text
STOP / SCIENTIFIC_OR_GOVERNANCE_REF_DRIFT
```

No resuelvas drift mediante rebase, merge, cherry-pick, force-push ni reconstrucción manual.

---

## 2. Verificación final del candidato aprobado

Verifica por comparación Git:

```text
base = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
head = 366bf529c29cb999bfd043db33674a510ba184c7
commits_ahead = 2
commits_behind = 0
changed_path_count = 2
```

Los únicos paths científicos deben ser:

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

Confirma además en el JSON corregido:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G3-F01
revision = PROMPT79_CORRECTIVE_MICROCLOSE
UNIT_OF_ANALYSIS = SERIE
PRIMARY_ANALYTICAL_UNIT = SERIE
DEPENDENCE_HANDLING = DAM_CLUSTER_AWARE
EVAL_V02_N = 1056
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
EVIDENCE_FAMILY_COUNT = 16
ELIGIBLE = 4
DESCRIPTIVE_ONLY = 11
NOT_ESTIMABLE = 1
EXP12_REOPENED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
```

El valor `CANDIDATE_PENDING_EXTERNAL_AUDIT` se conserva dentro del artefacto como estado histórico de generación. **No edites los dos artefactos científicos después de la reauditoría.** La aprobación/cierre se materializará en los registros canónicos de gobernanza.

Si algo no coincide:

```text
STOP / G3_F01_APPROVED_CANDIDATE_MISMATCH
```

---

## 3. Integración científica a `main`

Integra mediante **fast-forward puro** el candidato aprobado:

```text
366bf529c29cb999bfd043db33674a510ba184c7
```

a `main`.

Condiciones obligatorias:

- `main` debe seguir exactamente en `a33fc7e10b5bc25a053e982f0ff24ff60eda042f` antes de integrar;
- no crear merge commit;
- no squash;
- no rebase;
- no amend;
- no modificar los dos artefactos científicos;
- no incorporar ningún path adicional.

Después verifica:

```text
origin/main = 366bf529c29cb999bfd043db33674a510ba184c7
```

Si el fast-forward no es posible, detente.

---

## 4. Reconciliación del registro de fichas

Trabaja exclusivamente sobre:

```text
branch = docs/fichas-grupos-3-8
base = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

Modifica únicamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

No reescribas el historial ni simules que el registro de activación existió antes de Prompt76.

Debes agregar un registro explícito y trazable para G3-F01 con, como mínimo:

```text
FICHA = G3-F01
INITIAL_STATE = PROSPECTIVE
USER_AUTHORIZATION_TO_START_GROUP3 = YES
ACTIVATION_AUTHORIZATION = G3-F01 AUTHORIZED FOR EXECUTION
ACTIVATION_REGISTRY_PREEXECUTION_MATERIALIZED = NO
ACTIVATION_REGISTRY_RECONCILIATION = POST_HOC_ADMINISTRATIVE_RECONCILIATION

MAIN_AT_ACTIVATION = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
PLAN_AT_ACTIVATION = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
ARTICLE_AT_PROMPT76 = 254b1e6df736fa9938ac86a515d65b36f4d361c5
FICHAS_SNAPSHOT = a42531ad96fc12bea2f2394b0ff8eb49b66a4238

PROMPT76_COMMIT = 409dd7b7302bce1d41cc69e24b9debe3db05982e
INITIAL_CANDIDATE_COMMIT = c727da94f5d38f530a839631c3ac9e427a1eb27e
INITIAL_EXTERNAL_AUDIT = BLOCKED_FOR_CORRECTION
PROMPT79_COMMIT = 5dfe480ccbdb2802ced76aff14bbe6befb797742
CORRECTED_CANDIDATE_COMMIT = 366bf529c29cb999bfd043db33674a510ba184c7
CORRECTED_EXTERNAL_REAUDIT = PASS
SCIENTIFIC_RERUN_REQUIRED = false
INFERENTIAL_CALCULATION_PERFORMED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
FINAL_G3_F01_STATE = CLOSED / APPROVED
CLOSURE_DATE = 2026-09-19
```

Deja G3-F02 expresamente:

```text
ELIGIBLE_AFTER_G3_F01_CLOSURE / NOT_AUTHORIZED / NOT_EXECUTED
```

No cambies ninguna ficha G3-F02 o posterior a ACTIVE.

Publica un único commit administrativo en `docs/fichas-grupos-3-8` que modifique solamente ese registro.

---

## 5. Reconciliación del Plan Maestro

Trabaja exclusivamente sobre:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
```

Modifica únicamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Conserva íntegramente los estados cerrados previos, especialmente:

```text
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP12 = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
FUTURE_0B05C_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
```

Reconcílialo para reflejar exactamente:

```text
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F01_MAIN_INTEGRATION_COMMIT = 366bf529c29cb999bfd043db33674a510ba184c7
G3_F01_CORRECTED_EXTERNAL_REAUDIT = PASS
G3_F01_SCIENTIFIC_RERUN_REQUIRED = false
G3_F01_INFERENTIAL_CALCULATION_PERFORMED = false
G3_F01_HE2_DECIDED = false
G3_F01_HE5_DECIDED = false

NEXT_ELIGIBLE_FICHA = G3-F02
G3_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
STATISTICAL_INFERENCE = NOT_YET_AUTHORIZED
HE2_FINAL_DECISION = NOT_AUTHORIZED
HE5_FINAL_DECISION = NOT_AUTHORIZED
```

La reconciliación del Plan no autoriza por sí misma G3-F02.

Publica un único commit administrativo en la rama del Plan modificando solo ese archivo.

---

## 6. Verificación post-integración

Tras publicar los tres frentes, ejecuta `git fetch origin` y confirma:

```text
origin/main = 366bf529c29cb999bfd043db33674a510ba184c7
origin/docs/fichas-grupos-3-8 = <nuevo commit de reconciliación de registro>
origin/docs/plan-maestro-temporal-2026-08-31 = <nuevo commit de reconciliación del Plan>
```

Verifica además:

- los dos artefactos G3-F01 en `main` son byte-idénticos a los blobs auditados en `366bf529...`;
- `04_REGISTRO_ESTADO_FICHAS.md` registra explícitamente que la activación preejecución **no** fue materializada y que la reconciliación es post hoc;
- G3-F02 continúa `NOT_AUTHORIZED / NOT_EXECUTED`;
- no se modificó `article/main-manuscript`;
- no se ejecutó ningún cálculo científico.

---

## 7. Persistencia administrativa de Prompt80

En `codex/prompts-temporary`, crea únicamente:

```text
codex_prompts_tmp/80_RESPUESTA_INTEGRAR_Y_CERRAR_G3_F01_TRAS_REAUDITORIA_EXTERNA.md
```

La respuesta debe registrar:

- refs preflight;
- SHA de integración final de `main`;
- SHA nuevo de `docs/fichas-grupos-3-8`;
- SHA nuevo del Plan Maestro;
- paths modificados por cada rama;
- confirmación de fast-forward puro;
- confirmación de byte-identidad de los artefactos auditados;
- estado final de G3-F01;
- estado de G3-F02;
- confirmación de ausencia de cálculo inferencial o reejecución científica.

El commit de respuesta administrativa debe contener únicamente ese archivo.

---

## 8. Prohibiciones absolutas

No:

- reejecutar experimentos;
- recalcular métricas;
- calcular bootstrap, intervalos, p-values o tamaños de efecto;
- decidir HE2 o HE5;
- iniciar G3-F02;
- modificar `article/main-manuscript`;
- cambiar los dos artefactos científicos auditados;
- reabrir EXP12;
- alterar resultados cerrados de EXP11A, EXP11B, 0B-05C o Group2B;
- usar merge commit, squash, rebase, amend o force-push para la integración científica.

---

## 9. Reporte terminal obligatorio

Devuelve únicamente:

```text
PROMPT80 = COMPLETED | STOP

G3_F01_EXTERNAL_REAUDIT = PASS
G3_F01_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN

MAIN_PRE =
MAIN_FINAL =
MAIN_FAST_FORWARD_ONLY = true|false
G3_F01_ARTIFACTS_BYTE_IDENTICAL = true|false

FICHAS_PRE =
FICHAS_FINAL =
FICHAS_CHANGED_PATHS =
ACTIVATION_REGISTRY_RECONCILIATION = COMPLETED|FAILED

PLAN_PRE =
PLAN_FINAL =
PLAN_CHANGED_PATHS =

SCIENTIFIC_REEXECUTION_PERFORMED = false
INFERENTIAL_CALCULATION_PERFORMED = false
HE2_DECIDED = false
HE5_DECIDED = false

GROUP3 = IN_PROGRESS
G3_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G3_F02_STARTED = false

PROMPT80_RESPONSE_COMMIT =
ADMIN_REMOTE_HEAD_FINAL =

BLOCKERS =
```

Detente ahí. No prepares ni ejecutes G3-F02.