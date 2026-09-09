# CODEX — INTEGRAR GATE DE RECUPERACIÓN 0B-05C v0.3 EN `main`

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE INTEGRACIÓN** del gate/runner 0B-05C v0.3 ya auditado externamente.

Este bloque es **solo integración Git**. NO autoriza Attempt04, NO crea authorization record v0.3, NO cambia estados de autorización, NO ejecuta retrieval, EV03, EV04, D1a, EVAL real ni modelo.

Candidato aprobado externamente para integración:

- rama: `codex/0b05c-corrective-numerical-gate-v03`
- head exacto: `8b1444aed67d322714189846f98a3169145ea3d4`
- tree exacto: `7543d15b8b692408e5eaa4fc9b93f2a19f42eb78`
- parent inmediato: `815309b2b4ab6df2307d534ba20ec76e8077dcff`
- base `main`: `60aa7dd8715962f3c3e8b617e8797532529f39ed`
- compare base→candidato: `2 ahead / 0 behind`, merge-base exacto `60aa7dd...`, 13 paths científicos/técnicos v0.3.

Auditoría externa independiente del candidato corregido:

`INTEGRATION_AUDIT = PASS`
`F011 = VERIFIED_CLOSED`
`F012 = VERIFIED_CLOSED`
`F013 = VERIFIED_CLOSED`
`F014 = VERIFIED_CLOSED`
`0B05C_V03_GATE = APPROVED_FOR_INTEGRATION`

---

## 1. PREFLIGHT GIT OBLIGATORIO

Haz fetch y verifica exactamente:

- `origin/main = 60aa7dd8715962f3c3e8b617e8797532529f39ed`;
- candidato remoto = `8b1444aed67d322714189846f98a3169145ea3d4`;
- tree candidato = `7543d15b8b692408e5eaa4fc9b93f2a19f42eb78`;
- parent inmediato = `815309b2b4ab6df2307d534ba20ec76e8077dcff`;
- `815309b2...` tiene parent `60aa7dd...`;
- compare `60aa7dd... -> 8b1444...` = exactamente 2 commits, 2 ahead / 0 behind, merge-base `60aa7dd...`;
- compare `815309b2... -> 8b1444...` = exactamente 1 commit, 1 ahead / 0 behind;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Los 13 paths acumulados base→candidato deben ser exactamente:

1. `docs/0b05c_corrective_numerical_gate_v03.md`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_gate_hash_ledger_v0.3.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_gate_manifest_v0.3.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/d1a_numerical_execution_spec_v0.3.json`
6. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev03_numerical_execution_spec_v0.3.json`
7. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev04_numerical_execution_spec_v0.3.json`
8. `src/experiments/build_bm25_corrective_0b05c_v03.py`
9. `src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`
10. `src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py`
11. `src/experiments/run_0b05c_corrective_numerical_v03.py`
12. `src/experiments/run_d1a_corrective_0b05c_v03.py`
13. `tests/test_0b05c_corrective_numerical_gate_v03.py`

Si cualquier identidad, relación o path difiere: **STOP / NO INTEGRATION**.

No borres ni limpies evidencia local/ignored de Attempt01/02/03.

---

## 2. VALIDACIÓN PREINTEGRACIÓN READ-ONLY

Desde checkout limpio del candidato verifica sin escribir:

- gate v0.3 `gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT`;
- `authorization_readiness = NOT_AUTHORIZATION_READY`;
- cuatro autorizaciones numéricas = `NOT_AUTHORIZED`;
- `attempt04 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `authorization_record_present=false`;
- `runtime_authorization_record_present=false`;
- `corrective_retrieval_executed=false`;
- `corrective_metrics_computed=false`;
- authorization record v0.3 real ausente;
- 16 future roots v0.3 ausentes.

Ejecuta únicamente el preflight cerrado/read-only del preparador v0.3:

`python -B -m src.experiments.prepare_0b05c_corrective_numerical_gate_v03 --preflight`

Debe producir `PASS / PREEXECUTION_CLOSED_READONLY` sin side effects.

NO invoques `preflight_authorized()` con record real.
NO ejecutes `--execute-authorized`.
NO ejecutes retrieval/model/EVAL.

---

## 3. INTEGRACIÓN — FAST-FORWARD ONLY

Integra el candidato completo en `main` exclusivamente mediante **fast-forward** desde `60aa7dd...` hasta exactamente `8b1444...`.

Requisitos:

- `git merge --ff-only` o mecanismo equivalente que deje `main` exactamente en el commit candidato;
- NO merge commit;
- NO squash;
- NO cherry-pick;
- NO rebase;
- NO amend;
- NO force-push;
- NO regeneración;
- NO edición de archivos;
- NO commit adicional sobre `main`.

Después del push debe cumplirse:

- `origin/main = 8b1444aed67d322714189846f98a3169145ea3d4`;
- tree de `main = 7543d15b8b692408e5eaa4fc9b93f2a19f42eb78`.

---

## 4. VALIDACIÓN POSTINTEGRACIÓN

Verifica read-only:

1. `origin/main` exacto `8b1444...`;
2. tree exacto `7543d15...`;
3. compare `60aa7dd... -> origin/main` sigue siendo exactamente 2 commits / 13 paths / 2 ahead / 0 behind;
4. los 13 paths integrados tienen identidad de contenido con el candidato;
5. el gate sigue cerrado y NO autorizado:
   - `gate_status=CANDIDATE_PENDING_EXTERNAL_AUDIT`;
   - `authorization_readiness=NOT_AUTHORIZATION_READY`;
   - cuatro ejecuciones `NOT_AUTHORIZED`;
   - Attempt04 `NOT_AUTHORIZED / NOT_EXECUTED`;
   - authorization record v0.3 ausente;
   - runtime authorization record v0.3 ausente;
   - retrieval=false;
   - metrics=false;
6. vuelve a ejecutar únicamente el preflight cerrado/read-only v0.3 y exige PASS;
7. Plan Maestro y article conservan exactamente sus heads previos;
8. EXP11B/EXP12 no fueron abiertos ni modificados;
9. no hay resultados runtime v0.3 versionados ni generados por este bloque.

La integración NO convierte por sí misma el gate en autorización operativa. La autorización v0.3 será un bloque posterior separado.

---

## 5. ESTADO CIENTÍFICO POSTINTEGRACIÓN

Si todo pasa, reporta distinguiendo estado externo de auditoría e interno serializado:

- auditoría externa del gate v0.3 = `PASS`;
- artefactos v0.3 = `VERSIONED / INTEGRATED`;
- estado serializado preautorización del gate = `CANDIDATE_PENDING_EXTERNAL_AUDIT / NOT_AUTHORIZATION_READY`;
- EV03/EV04/D1a/Unified = `NOT_AUTHORIZED / NOT_EXECUTED`;
- Attempt04 = `NOT_AUTHORIZED / NOT_EXECUTED`;
- impacto métrico = `NOT_DETERMINED`;
- downstream = `NOT_YET_JUSTIFIED`;
- cierre 0B-05C = `NOT_AUTHORIZED`.

No cambies el estado serializado para “reflejar” la integración: forma parte del baseline inmutable de la futura transición de autorización.

---

## 6. PERSISTENCIA ADMINISTRATIVA

Solo después de completar y validar la integración:

1. fetch/checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/20_RESPUESTA_INTEGRAR_GATE_RECUPERACION_0B05C_V03_MAIN.md`;
3. commit administrativo separado y response-only;
4. mensaje sugerido:
   `docs: persist prompt 20 v0.3 gate integration report`;
5. push normal, sin rebase/amend/force.

Nunca mezcles la rama administrativa con `main`.

---

## 7. REPORTE FINAL OBLIGATORIO

Responde únicamente con estas secciones:

### A. Preflight Git
### B. Validación preintegración
### C. Integración
### D. Validación postintegración
### E. Aislamiento
### F. Persistencia administrativa
### G. Estado científico

Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_VERSIONED / INTEGRATED`

`0B05C_V03_GATE_EXTERNAL_AUDIT = PASS`

`0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`

`0B05C_V03_SERIALIZED_PREAUTH_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / NOT_AUTHORIZATION_READY`

`EV03_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`ATTEMPT04 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No construyas la autorización v0.3 en este bloque.