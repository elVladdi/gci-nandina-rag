# PROMPT 62 — INTEGRAR EVIDENCIA DE FALLO ONE-SHOT EXP12 Y RECONCILIAR ESTADO

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto la evidencia auditada del intento one-shot fallido de EXP12 planning;
2. verificar y documentar el estado terminal del intento **sin recomputar candidatos**;
3. crear un candidato separado de actualización del Plan Maestro que refleje el fallo contractual y el consumo irreversible de la autorización;
4. publicar el candidato del Plan para nueva auditoría externa.

Este bloque **NO reintenta** el planning, NO ejecuta `generate_exp12_candidates`, NO ejecuta `execute_planning`, NO calcula candidatos adicionales, NO cambia thresholds/seeds/quantiles/volumen/TVD, NO ejecuta retrieval/BM25/Top-k/MRR y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt61 concluye:

```text
PROMPT61_EXTERNAL_AUDIT = PASS_EXECUTION_PROTOCOL / PLANNING_FAILED_VALIDLY

EXP12_PLANNING_ATTEMPT_001 =
FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED / EVIDENCE_APPROVED_FOR_INTEGRATION

AUTHORIZATION_ID = EXP12_PLANNING_AUTH_001
ATTEMPT_ID = EXP12_PLANNING_ATTEMPT_001
OFFICIAL_INVOCATION_COUNT = 1
EXIT_CODE = 1
FAILURE_TYPE = ContractViolation
FAILURE_MESSAGE = Seed 20262001 produced fewer than 30 unique feasible candidates

RETRY_EXECUTED = false
RESUME_EXECUTED = false
OVERWRITE_EXECUTED = false
PARTIAL_RECOMPUTATION_EXECUTED = false

EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

La evidencia oficial publicada es:

```text
branch = codex/exp12-planning-attempt001-evidence-v01
commit = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
parent = 9428cb3dd205069f02c23ce16c7a9bbc874a0df1
```

Paths exactos permitidos y observados:

```text
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_consumption_marker.json
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_execution_report_v0.1.json
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_stdout.log
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_stderr.log
```

No se creó el summary de planning ni el output directory oficial.

### Hallazgo externo de observabilidad

La ejecución falló correctamente en modo fail-closed, pero el runner lanza la excepción después de completar `generate_exp12_candidates(...)` para el seed 20262001 y antes de escribir el summary. Por ello, la evidencia versionada permite afirmar únicamente:

```text
feasible_count(seed=20262001) < 30
```

pero **no conserva el valor exacto** ni un breakdown por filtro (volumen / cobertura / TVD / deduplicación).

Clasificación:

```text
EXP12-P61-F001 = FAILURE_OBSERVABILITY_GAP / NON_INVALIDATING_FOR_ATTEMPT
```

Este hallazgo NO autoriza recomputación, retry ni cambio del contrato. Tampoco demuestra por sí solo un bug del algoritmo.

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 9428cb3dd205069f02c23ce16c7a9bbc874a0df1
origin/codex/exp12-planning-attempt001-evidence-v01 = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
origin/docs/plan-maestro-temporal-2026-08-31 = 532f7ad93b01881817a6c8cec9f6eb486e37b684
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para la evidencia exige:

```text
parent = 9428cb3dd205069f02c23ce16c7a9bbc874a0df1
commits_ahead = 1
commits_behind = 0
changed_path_count = 4
```

y exactamente los cuatro paths enumerados en §1.

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta de la evidencia del intento

Integra exclusivamente:

```text
9428cb3dd205069f02c23ce16c7a9bbc874a0df1
→
428dfecca5cff313f910032a28a8a3c7ae13c2ef
```

mediante fast-forward exacto de `main`.

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/main = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
```

No muevas Plan ni Article en esta fase.

---

## 4. Fase B — verificación terminal READ-ONLY del intento

Desde el `main` ya integrado, lee íntegramente únicamente:

```text
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_execution_authorization_v0.1.json
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_consumption_marker.json
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_execution_report_v0.1.json
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_stdout.log
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_stderr.log
src/experiments/plan_exp12_historical_diversity_v01.py
```

No leas EVAL ni datasets para esta fase.

Verifica estáticamente:

```text
AUTHORIZATION_STATUS = AUTHORIZED_ONE_SHOT
AUTHORIZATION_SINGLE_USE = true
AUTHORIZATION_RETRY_ALLOWED = false
CONSUMPTION_MARKER_STATUS = CONSUMED_EXECUTION_STARTED
OFFICIAL_INVOCATION_COUNT = 1
EXIT_CODE = 1
FAILURE_TYPE = ContractViolation
FAILURE_MESSAGE = Seed 20262001 produced fewer than 30 unique feasible candidates
PLANNING_SUMMARY_EXISTS = false
OUTPUT_DIR_EXISTS_IN_GIT = false
```

Inspeccionando únicamente el flujo del runner, registra:

```text
FAILURE_RAISE_LOCATION = after generate_exp12_candidates(seed=20262001) returns and before run is appended to summary
EXACT_FEASIBLE_COUNT_PERSISTED = false
FILTER_BREAKDOWN_PERSISTED = false
EXACT_FEASIBLE_COUNT_RECOVERABLE_WITHOUT_RECOMPUTATION = false
```

No ejecutes funciones del runner.

No atribuyas causalidad del fallo a TVD, cobertura, volumen, deduplicación ni otra regla sin evidencia persistida.

---

## 5. Fase C — candidato de reconciliación del Plan Maestro

Crea desde exactamente:

```text
532f7ad93b01881817a6c8cec9f6eb486e37b684
```

la rama:

```text
codex/plan-maestro-exp12-planning-failure-v01
```

Modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Un solo commit.

### 5.1 Estado actual obligatorio

Actualiza el estado vigente y el orden maestro para reflejar:

```text
main = origin/main = 428dfecca5cff313f910032a28a8a3c7ae13c2ef

EXP12_PLANNING_AUTHORIZATION_V01 = INTEGRATED / CONSUMED
EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_PLANNING_ATTEMPT_001_FAILURE = Seed 20262001 produced fewer than 30 unique feasible candidates
EXP12_PLANNING_SUMMARY = NOT_CREATED
EXP12_PLANNING_OFFICIAL_CONDITIONS = NOT_SELECTED
EXP12_PLANNING_RETRY = PROHIBITED_UNDER_AUTH_001
EXP12_PLANNING_GATE = FAILED_UNDER_FROZEN_PLANNING_SEARCH
EXP12-P61-F001 = FAILURE_OBSERVABILITY_GAP / NON_INVALIDATING_FOR_ATTEMPT

EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B = NOT_STARTED
GROUP3 = NOT_STARTED
```

El siguiente bloque debe quedar como:

```text
NEXT_ELIGIBLE_BLOCK = EXP12_FEASIBILITY_FAILURE_FORENSIC_DESIGN
```

No declares todavía que EXP12 sea definitivamente imposible. El intento demuestra que **el planning congelado falló para el primer seed bajo el gate mínimo de 30 factibles**, pero la evidencia persistida no identifica qué restricción produjo el cuello de botella ni si existe un defecto técnico o una limitación estructural.

### 5.2 Historia que debe conservarse

No borres ni reescribas:

- source binding v0.4;
- corrección TVD v0.5;
- autorización one-shot;
- identidad de seeds y thresholds congelados;
- procedencia de NUEVA_02;
- estados históricos F007;
- cierre EXP11B;
- ninguna limitación previa.

Añade una entrada cronológica de 2026-09-14 para Prompt61.

---

## 6. Prohibiciones absolutas

Durante Prompt62 NO:

- ejecutes `generate_exp12_candidates`;
- ejecutes `execute_planning`;
- ejecutes el CLI con `--execute-planning`;
- recomputes el seed 20262001;
- pruebes otros seeds;
- calcules HHI/TVD de candidatos nuevos;
- cuentes candidatos factibles mediante recomputación;
- cambies candidate_count, minimum_unique_feasible, seeds, quantiles, volumen, coverage o maximum_tvd;
- cambies runner/config/tests/data;
- ejecutes retrieval/BM25/Top-k/MRR;
- leas labels/descripciones/performance EVAL;
- crees otra autorización de planning;
- autorices retrieval EXP12;
- avances a Grupo 2B o Grupo 3.

---

## 7. Verificaciones finales

Exige:

```text
origin/main = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
origin/docs/plan-maestro-temporal-2026-08-31 = 532f7ad93b01881817a6c8cec9f6eb486e37b684
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

La rama canónica del Plan NO se mueve todavía.

Para el candidato del Plan exige:

```text
parent = 532f7ad93b01881817a6c8cec9f6eb486e37b684
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Y confirma:

```text
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_RETRIEVAL_AUTHORIZED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 8. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/62_RESPUESTA_INTEGRAR_EVIDENCIA_FALLO_PLANNING_EXP12_Y_RECONCILIAR_ESTADO.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 9. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT62 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_final

ATTEMPT001_EVIDENCE_INTEGRATED
INTEGRATION_MODE

AUTHORIZATION_STATUS
AUTHORIZATION_SINGLE_USE
AUTHORIZATION_RETRY_ALLOWED
CONSUMPTION_MARKER_STATUS
OFFICIAL_INVOCATION_COUNT
EXIT_CODE
FAILURE_TYPE
FAILURE_MESSAGE
PLANNING_SUMMARY_EXISTS
OUTPUT_DIR_EXISTS_IN_GIT
FAILURE_RAISE_LOCATION
EXACT_FEASIBLE_COUNT_PERSISTED
FILTER_BREAKDOWN_PERSISTED
EXACT_FEASIBLE_COUNT_RECOVERABLE_WITHOUT_RECOMPUTATION

PLAN_CANDIDATE_BRANCH
PLAN_CANDIDATE_COMMIT
PLAN_CANDIDATE_PARENT
PLAN_CANDIDATE_CHANGED_PATH_COUNT
PLAN_CANDIDATE_PUBLISHED

EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_PLANNING_GATE = FAILED_UNDER_FROZEN_PLANNING_SEARCH
NEXT_ELIGIBLE_BLOCK = EXP12_FEASIBILITY_FAILURE_FORENSIC_DESIGN
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT62 = COMPLETED
EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_PLANNING_GATE = FAILED_UNDER_FROZEN_PLANNING_SEARCH
EXP12_PLANNING_REEXECUTED = false
NEXT_ELIGIBLE_BLOCK = EXP12_FEASIBILITY_FAILURE_FORENSIC_DESIGN
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```
