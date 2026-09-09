# CODEX — INTEGRAR DIAGNÓSTICO ESTÁTICO EV04 ATTEMPT04 EN `main`

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE INTEGRACIÓN DEL DIAGNÓSTICO ESTÁTICO EV04 DE ATTEMPT04**.

El candidato de diagnóstico generado por Prompt26 fue auditado externamente y queda **APPROVED_FOR_INTEGRATION**.

Tu única tarea científica es integrar mediante **fast-forward exacto** ese candidato a `main`.

NO diagnostiques de nuevo.
NO modifiques ni regeneres el artefacto de diagnóstico.
NO construyas v0.4.
NO autorices ni ejecutes Attempt05.
NO ejecutes retrieval, EV03, EV04, D1a, EVAL ni el modelo.
NO modifiques el failure record histórico de Attempt04.
NO actualices Plan ni article.

---

# 1. IDENTIDADES GIT OBLIGATORIAS

Haz `fetch` y verifica exactamente antes de integrar:

## 1.1 `main`

- `origin/main = 58ecf012d7c4ed609c3b10787fb583f69700ab02`;
- tree = `bbd5c077cfd6a984670c799387029563ade1faf0`;
- parent = `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`.

## 1.2 Candidato aprobado

Rama:

`codex/0b05c-ev04-attempt04-static-metric-diagnosis-v03`

Debe apuntar exactamente a:

`6187ca29357c42c43675fb8e5ffdacbb4705ee83`

Ese commit debe tener:

- parent exacto: `58ecf012d7c4ed609c3b10787fb583f69700ab02`;
- tree exacto: `7c8199733df071eee299d80a57456223fb2834ad`;
- compare `main -> candidato`: `1 ahead / 0 behind`;
- merge-base exacto = `58ecf012d7c4ed609c3b10787fb583f69700ab02`;
- exactamente **1 commit**;
- exactamente **1 changed path**:
  `outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json`;
- blob Git de ese artefacto:
  `fca5712c615960b41cb2741c2164f19fc00df9dd`.

No debe existir ningún otro cambio.

## 1.3 Ramas no científicas

Verifica que permanezcan:

- Plan Maestro: `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article: `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Si cualquier identidad difiere: **STOP / NO INTEGRATION**.

---

# 2. VERIFICACIÓN READ-ONLY DEL ARTEFACTO APROBADO

Antes del fast-forward, comprueba mecánicamente en el candidato:

- `artifact_id = 0b05c_ev04_attempt04_metric_mismatch_diagnosis_v0.3`;
- `baseline_commit = 58ecf012d7c4ed609c3b10787fb583f69700ab02`;
- `attempt04_runtime_outputs_used = false`;
- `attempt05_authorized = false`;
- `retrieval_executed = false`;
- `evaluation_runner_executed = false`;
- `model_inference_executed = false`;
- `metric_impact = NOT_DETERMINED`;
- `closure = NOT_AUTHORIZED`;
- `root_cause_field_status = ISOLATED_FROM_VERSIONED_FROZEN_ARTIFACTS`;
- `root_cause_class = FLOAT_ACCUMULATION_PATH_MISMATCH`;
- deep diff exacto: `mismatch_count = 6`;
- los seis paths causales son exactamente:
  1. `$.metric_table[0].numerator`
  2. `$.metric_table[0].value`
  3. `$.mrr_101_200_contribution`
  4. `$.mrr_101_200_contribution_numerator`
  5. `$.mrr_at_100`
  6. `$.mrr_at_100_numerator`
- `run_metadata_metrics_equal_metrics_artifact = true`;
- `source_bindings_all_match_expected = true`;
- comparator estático: `metrics_exact_before_call = false` y `outcome = RAISED_CONTRACT_VIOLATION`;
- no se atribuye el valor congelado a una librería o función histórica concreta no demostrada.

No recalcules ni reescribas nada. Esta sección es solo validación del candidato ya auditado.

---

# 3. INTEGRACIÓN EXCLUSIVAMENTE FAST-FORWARD

Integra únicamente:

`58ecf012d7c4ed609c3b10787fb583f69700ab02`

→

`6187ca29357c42c43675fb8e5ffdacbb4705ee83`

mediante:

```bash
git merge --ff-only origin/codex/0b05c-ev04-attempt04-static-metric-diagnosis-v03
```

Reglas absolutas:

- no merge commit;
- no squash;
- no cherry-pick;
- no rebase;
- no amend;
- no force-push;
- no edición durante integración;
- no regeneración de artefactos;
- no commit adicional en `main`;
- push normal de `main` únicamente después de verificar el fast-forward.

---

# 4. VALIDACIÓN POST-INTEGRACIÓN

Después del push verifica:

1. `origin/main = 6187ca29357c42c43675fb8e5ffdacbb4705ee83`;
2. tree de `main = 7c8199733df071eee299d80a57456223fb2834ad`;
3. candidato y `origin/main` tienen diff vacío;
4. old-main → new-main sigue siendo exactamente `1 ahead / 0 behind` y 1 commit;
5. el único path integrado es el artefacto de diagnóstico;
6. blob integrado = `fca5712c615960b41cb2741c2164f19fc00df9dd`;
7. el failure record Attempt04 no cambió;
8. gate/specs/authorization record no cambiaron;
9. no se versionó ningún output parcial de Attempt04;
10. Attempt05 continúa no autorizado;
11. no existe v0.4;
12. Plan y article permanecen en sus heads congelados;
13. working tree tracked limpio.

---

# 5. PROHIBICIONES

Durante todo este bloque:

- no ejecutes diagnóstico adicional;
- no ejecutes cálculo numérico sobre EVAL;
- no ejecutes retrieval;
- no construyas índices;
- no invoques EV03/EV04/D1a;
- no hagas inferencia;
- no construyas v0.4;
- no autorices Attempt05;
- no decidas impacto métrico;
- no decidas downstream;
- no cierres 0B-05C;
- no abras EXP11B ni EXP12.

---

# 6. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Solo después de completar la integración y validación:

1. fetch + checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/27_RESPUESTA_INTEGRAR_DIAGNOSTICO_ESTATICO_EV04_ATTEMPT04_MAIN.md`;
3. no modifiques Prompt27 ni respuestas anteriores;
4. commit administrativo response-only;
5. push normal sin rebase/amend/force.

Nunca mezcles la rama administrativa con `main`.

---

# 7. REPORTE FINAL OBLIGATORIO

Usa exactamente estas secciones:

### A. Preflight Git
### B. Verificación del candidato
### C. Integración
### D. Validación post-integración
### E. Aislamiento
### F. Persistencia administrativa
### G. Estado científico

En G termina con:

`GROUP_2 = EN_CURSO`

`0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED`

`0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04`

`EV04_ATTEMPT04_STATIC_DIAGNOSIS = VERSIONED / INTEGRATED`

`EV04_ATTEMPT04_ROOT_CAUSE_FIELD = ISOLATED_FROM_VERSIONED_FROZEN_ARTIFACTS`

`EV04_ATTEMPT04_ROOT_CAUSE_CLASS = FLOAT_ACCUMULATION_PATH_MISMATCH`

`ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`
