# CODEX — INTEGRAR MICROCLOSE ATTEMPT04 FAIL-CLOSED A `main`

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE INTEGRACIÓN FAST-FORWARD** del microcierre de Attempt04 ya auditado externamente.

Candidato científico aprobado:

- rama: `codex/0b05c-attempt04-failclosed-microclose`;
- commit: `58ecf012d7c4ed609c3b10787fb583f69700ab02`;
- parent: `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- tree: `bbd5c077cfd6a984670c799387029563ade1faf0`;
- dictamen externo: `PASS / APPROVED_FOR_INTEGRATION`.

Este bloque **solo integra** ese commit a `main`.

NO diagnostiques el campo exacto del mismatch EV04.
NO construyas v0.4.
NO autorices Attempt05.
NO ejecutes Attempt05.
NO ejecutes retrieval, EV03, EV04, D1a, EVAL ni el modelo.
NO modifiques Plan, article, EXP11B ni EXP12.

---

# 1. PREFLIGHT GIT OBLIGATORIO

Haz fetch y verifica exactamente antes de integrar:

- `origin/main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- tree de `origin/main` = `d10ea04228d2754dc8156b0abaedfceee9fe297f`;
- rama candidata remota = `58ecf012d7c4ed609c3b10787fb583f69700ab02`;
- parent del candidato = `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- tree del candidato = `bbd5c077cfd6a984670c799387029563ade1faf0`;
- merge-base main↔candidato = `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- compare = `1 ahead / 0 behind`, exactamente 1 commit;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

El compare debe contener exactamente estos cinco paths:

1. `outputs/audits/0b05c_attempt04_failclosed_v0.3/attempt04_failure_record_v0.3.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/d1a_numerical_execution_spec_v0.3.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev03_numerical_execution_spec_v0.3.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev04_numerical_execution_spec_v0.3.json`

Blobs candidatos esperados:

- failure record = `31f1cea387b8630191371f767c03cf13990646b0`;
- gate = `58152fd4806d8efd54ae752cb2790c383417aa37`;
- D1a spec = `59ccb83b385d7cc6fd157cbe5e22ca7862809116`;
- EV03 spec = `b9d047805286edd0522d9279d25058db99328aef`;
- EV04 spec = `c4683ab80f24ac07266855e1cc6c1519db94128c`.

Si cualquier identidad o alcance difiere: **STOP / NO INTEGRATION**.

---

# 2. ESTADO DEL CANDIDATO QUE DEBE PRESERVARSE

Verifica read-only antes de integrar:

## Gate v0.3

- `gate_status = APPROVED / INTEGRATED`;
- `authorization_readiness = ATTEMPT04_CONSUMED / REAUTHORIZATION_REQUIRED`;
- `attempt04 = FAIL_CLOSED / AUTHORIZATION_CONSUMED`;
- las cuatro autorizaciones históricas permanecen `AUTHORIZED`;
- `authorization_record_present = true`;
- `runtime_authorization_record_present = false`;
- `corrective_retrieval_executed = false`;
- `corrective_metrics_computed = false`.

## EV03 / EV04 / D1a

Cada spec debe tener:

- `attempt04 = FAIL_CLOSED / AUTHORIZATION_CONSUMED`;
- su autorización histórica propia sigue `AUTHORIZED`;
- flags de outputs/cómputo continúan `false` donde corresponda.

## Failure record

Debe conservar:

- `artifact_id = 0b05c_attempt04_failure_record_v0.3`;
- `status = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`;
- `authorization_consumed = true`;
- `automatic_reuse_authorized = false`;
- `attempt05_authorized = false`;
- `runtime_evidence_classification = CODEX_LOCAL_EXECUTION_REPORT_NOT_INDEPENDENTLY_VERSIONED_RUNTIME_OUTPUTS`;
- `root_cause_field_status = NOT_YET_ISOLATED`;
- `partial_outputs = LOCAL_PRESERVED_NOT_VERSIONED`;
- `metric_impact = NOT_DETERMINED`;
- `downstream_reexecution = NOT_YET_JUSTIFIED`;
- `closure = NOT_AUTHORIZED`.

No alteres ni regeneres estos archivos.

---

# 3. INTEGRACIÓN

Integra únicamente por **fast-forward**:

`e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`
→ `58ecf012d7c4ed609c3b10787fb583f69700ab02`

Requisitos absolutos:

- no merge commit;
- no squash;
- no cherry-pick;
- no rebase;
- no amend;
- no force-push;
- no edición durante la integración;
- no regeneración de artefactos;
- no commit adicional en `main`.

Push normal de `main` únicamente si el fast-forward exacto es posible.

---

# 4. VALIDACIÓN POSTINTEGRACIÓN

Después del push verifica read-only:

- `origin/main = 58ecf012d7c4ed609c3b10787fb583f69700ab02`;
- tree = `bbd5c077cfd6a984670c799387029563ade1faf0`;
- candidato vs `origin/main` = diff vacío;
- compare antiguo main `e3476d9...` → nuevo main = `1 ahead / 0 behind`, 1 commit, exactamente 5 paths;
- blobs integrados iguales a los cinco blobs candidatos;
- authorization record v0.3 **no fue modificado**;
- Plan Maestro sigue `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article sigue `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- no se versionó ningún output parcial de Attempt04;
- no existe autorización para Attempt05;
- no se construyó v0.4;
- no se ejecutó ningún componente numérico.

El estado científico postintegración debe ser:

- Attempt04 fail-closed durable e integrado;
- autorización v0.3 consumida;
- reutilización automática bloqueada;
- causa de campo EV04 todavía no aislada;
- Attempt05 no autorizado.

---

# 5. PERSISTENCIA ADMINISTRATIVA

Después de finalizar la integración científica:

1. fetch + checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/25_RESPUESTA_INTEGRAR_MICROCLOSE_ATTEMPT04_FAIL_CLOSED_MAIN.md`;
3. no modifiques este Prompt25 ni respuestas anteriores;
4. commit administrativo response-only;
5. push normal sin rebase/amend/force.

No mezcles la rama administrativa con `main`.

---

# 6. REPORTE FINAL

Usa exactamente estas secciones:

### A. Preflight Git
### B. Verificación del candidato
### C. Integración
### D. Validación postintegración
### E. Aislamiento
### F. Persistencia administrativa
### G. Estado científico

Termina con:

`GROUP_2 = EN_CURSO`

`0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`

`0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT04`

`0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`

`0B05C_ATTEMPT04_FAILURE_RECORD = VERSIONED / INTEGRATED`

`EV04_ATTEMPT04_ROOT_CAUSE_FIELD = NOT_YET_ISOLATED`

`ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`
