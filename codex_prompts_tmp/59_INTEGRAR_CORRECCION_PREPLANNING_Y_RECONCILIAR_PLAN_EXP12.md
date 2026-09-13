# PROMPT 59 — INTEGRAR CORRECCIÓN PRE-PLANNING Y RECONCILIAR PLAN EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto el paquete correctivo pre-planning EXP12 v0.5 ya auditado externamente;
2. crear un candidato separado de actualización del Plan Maestro que refleje el estado real posterior a esa integración;
3. publicar ambos estados para auditoría externa.

Este bloque **NO ejecuta el planeamiento EXP12**, NO ejecuta `generate_exp12_candidates`, NO ejecuta los 10,000 candidatos por seed, NO selecciona D-HIGH/D-MID/D-LOW, NO ejecuta retrieval/BM25/Top-k/MRR, NO crea autorización de ejecución EXP12 y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt58 concluye:

```text
PROMPT58_EXTERNAL_AUDIT = PASS / APPROVED
EXP12_PREPLANNING_CORRECTION_V01 = APPROVED_FOR_INTEGRATION
EXP12_PLANNING = NOT_YET_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato aprobado:

```text
branch = codex/exp12-preplanning-correction-v01
commit = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
parent = 025136e9067a415388699a55b9aa718145ae193e
changed_path_count = 4
```

Paths exactos:

```text
outputs/audits/exp12_planning_gate_v0.2/exp12_preplanning_correction_readiness_v0.2.json
src/configs/exp12_historical_diversity_control_v0.5.json
src/experiments/plan_exp12_historical_diversity_v01.py
tests/test_exp12_preplanning_compatibility_v01.py
```

Hechos metodológicos aprobados que deben preservarse:

```text
EXP12_TVD_SUPPORT = FULL_REFERENCE_SUPPORT_PLUS_OTHER
maximum_tvd = 0.05
required_label_coverage_fraction = 1.0
target_rows = 2950
volume_range = [2802,3098]
candidate_count = 10000
minimum_unique_feasible_candidates = 30
seed_schedule = [20262001..20262010]
quantiles = D-HIGH 0.1 / D-MID 0.5 / D-LOW 0.9
sampling_universe = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sampling_universe_sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
sampling_universe_rows = 7190
sampling_universe_dam_count = 101
sampling_universe_nandina_count = 84
H100_reference_coverage = 66/66
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 025136e9067a415388699a55b9aa718145ae193e
origin/codex/exp12-preplanning-correction-v01 = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato correctivo exige:

```text
parent = 025136e9067a415388699a55b9aa718145ae193e
commits_ahead = 1
commits_behind = 0
changed_path_count = 4
```

y que los cuatro paths sean exactamente los enumerados arriba.

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta del paquete correctivo

Integra exclusivamente:

```text
025136e9067a415388699a55b9aa718145ae193e
→
6437a05325bdb01f3cd4964e1b0fae7d3641cc11
```

mediante fast-forward exacto de `main`.

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después del push exige:

```text
origin/main = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
```

No muevas Plan ni Article en esta fase.

---

## 4. Fase B — reconciliación candidata del Plan Maestro

Trabaja exclusivamente sobre la rama canónica del Plan:

```text
docs/plan-maestro-temporal-2026-08-31
```

Baseline obligatorio:

```text
00adb8f6fc668609500be913203be50a5d402554
```

Crea una rama candidata nueva desde ese commit:

```text
codex/plan-maestro-exp12-preplanning-v01
```

Modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Un solo commit.

### 4.1 Estado que debe reflejar el Plan

Actualiza el resumen global y las secciones EXP12/orden maestro para reflejar, sin borrar la historia previa:

```text
main = origin/main = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11

EXP11B = CLOSED / APPROVED / INTEGRATED

EXP12_NEW_HISTORICAL_GATE_EXTENSION_V02 = INTEGRATED
EXP12_SAMPLING_UNIVERSE = SOURCE_BOUND / APPROVED
EXP12_SAMPLING_UNIVERSE_PATH = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
EXP12_SAMPLING_UNIVERSE_SHA256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
EXP12_SAMPLING_UNIVERSE_ROWS = 7190
EXP12_SAMPLING_UNIVERSE_DAM = 101
EXP12_SAMPLING_UNIVERSE_NANDINA = 84
EXP12_H100_REFERENCE_COVERAGE = 66/66

EXP12_SOURCE_BINDING_V04 = INTEGRATED
EXP12_PREPLANNING_COMPATIBILITY_AUDIT_V01 = INTEGRATED
EXP12_PREPLANNING_CORRECTION_V01 = INTEGRATED

EXP12_TVD_SUPPORT = FULL_REFERENCE_SUPPORT_PLUS_OTHER
EXP12_TVD_MAXIMUM = 0.05
EXP12_LABEL_COVERAGE_REQUIRED = 1.0
EXP12_TARGET_ROWS = 2950
EXP12_VOLUME_RANGE = [2802,3098]
EXP12_CANDIDATE_COUNT = 10000
EXP12_MINIMUM_UNIQUE_FEASIBLE = 30
EXP12_SEEDS = 20262001..20262010
EXP12_QUANTILES = 0.1 / 0.5 / 0.9

EXP12_PLANNING = NOT_YET_EXECUTED / NOT_YET_AUTHORIZED
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
NEXT_ELIGIBLE_BLOCK = EXP12_PLANNING_EXECUTION_GATE
Grupo 2B = NOT_STARTED
Grupo 3 = NOT_STARTED
```

### 4.2 Procedencia de NUEVA_02

Registra de forma cauta, sin convertir la declaración del usuario en evidencia independiente:

```text
NUEVA_02_ACQUISITION_UNIT = COMPLETE_DAM_WITH_ALL_ORIGINAL_SERIES
NUEVA_02_ACQUISITION_METHOD = SAME_SEARCH_EXTRACTION_COPY_METHOD_AS_INITIAL_DATA_AND_NUEVA_01
NUEVA_02_SELECTION_BASIS = PREDECLARED_H100_LABEL_COVERAGE_GAP
NUEVA_02_MODEL_OR_EVAL_PERFORMANCE_SELECTION = NOT_USED
NUEVA_02_PROVENANCE_EVIDENCE_CLASS = USER_ATTESTED / NOT_INDEPENDENTLY_REPLAYED_AT_ACQUISITION
```

No la presentes como verificación independiente de IA Experimental o Codex.

### 4.3 Historia que debe conservarse

No elimines ni reescribas retrospectivamente:

- el estado anterior `45/66` del gate v0.1;
- el rechazo de F007 v0.1;
- la corrección F007 v0.2;
- que `NUEVA_02` fue una extensión posterior;
- que el planeamiento basado en la interpretación B de Prompt50 es no gobernante;
- resultados/cierre EXP11B;
- ninguna limitación ya aprobada.

Puedes marcar explícitamente estados anteriores como **SUPERSEDED_BY_LATER_GATE** cuando corresponda, sin borrar su trazabilidad.

---

## 5. Prohibiciones absolutas

Durante Prompt59 NO:

- ejecutes `plan_exp12_historical_diversity_v01.py --execute-planning`;
- ejecutes `generate_exp12_candidates` sobre el pool oficial;
- ejecutes los 10,000 candidatos por seed;
- calcules resultados oficiales de HHI/TVD por seed;
- selecciones D-HIGH/D-MID/D-LOW oficiales;
- materialices bancos EXP12;
- leas labels/descripciones/performance EVAL;
- ejecutes retrieval/BM25/Top-k/MRR;
- cambies v0.5;
- cambies runner o tests;
- cambies thresholds, seeds, quantiles, volumen o candidate_count;
- crees autorización EXP12;
- modifiques Article;
- avances a Grupo 2B o Grupo 3.

---

## 6. Verificaciones finales

Exige al final:

```text
origin/main = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

La rama canónica del Plan debe permanecer en `00adb8f6...`; el candidato todavía no se integra.

Para el candidato del Plan exige:

```text
parent = 00adb8f6fc668609500be913203be50a5d402554
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Y confirma:

```text
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 7. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/59_RESPUESTA_INTEGRAR_CORRECCION_PREPLANNING_Y_RECONCILIAR_PLAN_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 8. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT59 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

PREPLANNING_CORRECTION_V01_INTEGRATED = true/false
INTEGRATION_MODE
INTEGRATED_COMMIT

PLAN_CANDIDATE_BRANCH
PLAN_CANDIDATE_COMMIT
PLAN_CANDIDATE_PARENT
PLAN_CANDIDATE_TREE
PLAN_CANDIDATE_COMMITS_AHEAD
PLAN_CANDIDATE_COMMITS_BEHIND
PLAN_CANDIDATE_CHANGED_PATH_COUNT
PLAN_CANDIDATE_CHANGED_PATHS
PLAN_CANDIDATE_PUBLISHED

EXP12_SOURCE_BOUND_STATUS
EXP12_PREPLANNING_CORRECTION_STATUS
EXP12_TVD_SUPPORT
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT59 = COMPLETED
EXP12_PREPLANNING_CORRECTION_V01 = INTEGRATED
PLAN_RECONCILIATION_EXP12_PREPLANNING = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP12_PLANNING_EXECUTED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
