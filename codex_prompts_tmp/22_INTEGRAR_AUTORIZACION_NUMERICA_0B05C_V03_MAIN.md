# CODEX — INTEGRAR AUTORIZACIÓN NUMÉRICA 0B-05C v0.3 EN `main`

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE INTEGRACIÓN** del candidato de autorización numérica 0B-05C v0.3 ya auditado externamente.

Este bloque **NO ejecuta Attempt04** y **NO ejecuta retrieval, EV03, EV04, D1a, EVAL real ni inferencia del modelo**.

Objetivo único: integrar por **fast-forward exacto** el candidato autorizado v0.3 en `main`, sin editar ni regenerar ningún archivo científico.

Candidato aprobado externamente:

- rama: `codex/0b05c-numerical-authorization-v03`
- commit: `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`
- parent/baseline: `8b1444aed67d322714189846f98a3169145ea3d4`
- tree: `d10ea04228d2754dc8156b0abaedfceee9fe297f`
- compare baseline→candidate: `1 ahead / 0 behind`, exactamente 1 commit y exactamente 5 paths.

Dictamen externo previo:

`0B05C_V03_AUTHORIZATION_CANDIDATE_AUDIT = PASS / APPROVED_FOR_INTEGRATION`

---

# 1. PREFLIGHT GIT OBLIGATORIO

Haz fetch y verifica **antes de modificar `main`**:

- `origin/main = 8b1444aed67d322714189846f98a3169145ea3d4`;
- tree de `main` = `7543d15b8b692408e5eaa4fc9b93f2a19f42eb78`;
- rama candidata remota = `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- parent del candidato = `8b1444aed67d322714189846f98a3169145ea3d4`;
- tree del candidato = `d10ea04228d2754dc8156b0abaedfceee9fe297f`;
- merge-base baseline/candidato = baseline exacto;
- candidate `1 ahead / 0 behind`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

El compare baseline→candidato debe contener **exactamente estos cinco paths**:

1. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_numerical_authorization_record_v0.3.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/d1a_numerical_execution_spec_v0.3.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev03_numerical_execution_spec_v0.3.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev04_numerical_execution_spec_v0.3.json`

Si cualquier identidad, relación o path difiere: **STOP / NO INTEGRATION**.

---

# 2. VALIDACIÓN READ-ONLY DEL CANDIDATO ANTES DEL FF

Desde un checkout/worktree detached limpio del candidato, verifica read-only:

## Gate

- `gate_status = APPROVED / INTEGRATED`;
- `authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- cuatro autorizaciones numéricas = `AUTHORIZED`;
- `authorization_record_present = true`;
- `attempt04 = AUTHORIZED / NOT_EXECUTED`;
- `corrective_retrieval_executed = false`;
- `corrective_metrics_computed = false`;
- `runtime_authorization_record_present = false`.

## Specs

- EV03 propio = `AUTHORIZED`;
- EV04 propio = `AUTHORIZED`;
- D1a propio = `AUTHORIZED`;
- `attempt04 = AUTHORIZED / NOT_EXECUTED` en los tres;
- flags D1a `D1A_CORRECTIVE_*_CREATED/COMPUTED = false`.

## Authorization record

Debe existir exactamente en:

`outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_numerical_authorization_record_v0.3.json`

Y debe tener:

- `artifact_id = 0b05c_numerical_authorization_record_v0.3`;
- `schema_version = 3`;
- `authorization_baseline_commit = 8b1444aed67d322714189846f98a3169145ea3d4`;
- `baseline_external_audit = PASS / APPROVED_FOR_INTEGRATION`;
- exactamente cuatro baseline artifacts: gate, EV03, EV04, D1a.

Los Git blob SHA-1 baseline deben ser exactamente:

- unified gate: `5bca7e9b09d5fcc62d066aeed7727338f71c1497`;
- EV03 spec: `469854c41c62652e83255a190a27f14c4503ee60`;
- EV04 spec: `eaae5ab72bee3bd5db798d65457e8e5ba0ece524`;
- D1a spec: `f1f53c8e7095e538e2e70130f4eef2773ee1f259`.

Ejecuta únicamente `preflight_authorized()` read-only contra el candidato. Debe retornar `PASS / AUTHORIZED_PREFLIGHT_ONLY` y comprobar la transición baseline→authorized, bindings, specs, modelo por identidad y ausencia de los 16 roots v0.3.

**NO invoques `--execute-authorized`.**

Si el preflight autorizado no pasa por cualquier razón: **STOP / NO INTEGRATION**.

---

# 3. INTEGRACIÓN

Si y solo si todo lo anterior pasa:

1. checkout `main`;
2. confirma nuevamente `HEAD = origin/main = 8b1444aed67d322714189846f98a3169145ea3d4`;
3. integra exclusivamente por fast-forward el commit `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
4. push normal a `origin/main`.

Resultado obligatorio:

- `main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- `origin/main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- tree = `d10ea04228d2754dc8156b0abaedfceee9fe297f`;
- no merge commit;
- no squash;
- no cherry-pick;
- no rebase;
- no amend;
- no force-push;
- no commit adicional en `main`;
- no edición/regeneración durante integración.

---

# 4. VALIDACIÓN POSTINTEGRACIÓN

Después del push, verifica desde `origin/main`:

- candidate vs `origin/main` = diff vacío;
- compare `8b1444... -> origin/main` = 1 commit / 5 paths exactos;
- los blobs de los cinco paths coinciden con el candidato:
  - gate `d4751f418b45dcf190d6c9b06bce68692afac071`;
  - authorization record `1338201cf4935b9cc7796a2f571c07908248e086`;
  - D1a spec `f53221abb1e2afa1a317f410d33febfae91343d1`;
  - EV03 spec `bba7d853d83460ae99c7587e9d3e2a7ebc55e2c8`;
  - EV04 spec `3a6f9219871777cdd932104d2fe6153a5cbc69eb`.

Ejecuta otra vez, solo read-only, `preflight_authorized()` desde el `main` integrado. Debe seguir devolviendo `PASS / AUTHORIZED_PREFLIGHT_ONLY` y **no crear ningún output**.

Confirma:

- future roots v0.3 ausentes;
- runtime authorization record ausente;
- corrective retrieval = false;
- corrective metrics = false;
- Attempt04 = `AUTHORIZED / NOT_EXECUTED`;
- working tree tracked-clean.

---

# 5. PROHIBICIONES ABSOLUTAS

En este bloque NO:

- ejecutes Attempt04;
- invoques `--execute-authorized`;
- ejecutes retrieval;
- ejecutes EV03/EV04;
- ejecutes D1a;
- ejecutes EVAL real;
- hagas inferencia con el modelo;
- generes roots runtime v0.3;
- crees runtime authorization record;
- produzcas métricas correctivas;
- modifiques Plan Maestro;
- modifiques article;
- abras EXP11B o EXP12;
- modifiques v0.1/v0.2 ni failure record Attempt03.

La validación read-only de tamaño/SHA del modelo requerida por `preflight_authorized()` sí está permitida.

---

# 6. PERSISTENCIA ADMINISTRATIVA

Solo después de completar y verificar la integración:

1. fetch/checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/22_RESPUESTA_INTEGRAR_AUTORIZACION_NUMERICA_0B05C_V03_MAIN.md`;
3. commit administrativo response-only;
4. mensaje sugerido:
   `docs: persist prompt 22 v0.3 authorization integration report`;
5. push normal, sin rebase/amend/force.

Nunca mezcles la rama administrativa con `main`.

---

# 7. REPORTE FINAL

Usa exactamente estas secciones:

### A. Preflight Git
### B. Validación preintegración
### C. Integración
### D. Validación postintegración
### E. Aislamiento y no ejecución
### F. Persistencia administrativa
### G. Estado científico

Termina con:

`GROUP_2 = EN_CURSO`

`0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`

`0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED`

`ATTEMPT04 = AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`
