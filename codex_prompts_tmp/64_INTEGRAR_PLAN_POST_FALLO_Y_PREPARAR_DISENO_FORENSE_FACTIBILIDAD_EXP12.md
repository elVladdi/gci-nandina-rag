# PROMPT 64 — INTEGRAR PLAN POST-FALLO Y PREPARAR DISEÑO FORENSE DE FACTIBILIDAD EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto el candidato v02 del Plan Maestro post-fallo EXP12 ya auditado externamente;
2. preparar, sobre una rama separada de `main`, un **paquete diagnóstico forense no gobernante** que permita explicar por qué el seed oficial `20262001` produjo menos de 30 candidatos factibles;
3. probar el paquete únicamente con datos sintéticos;
4. publicar el paquete para auditoría externa.

Este bloque **NO ejecuta el diagnóstico sobre el pool oficial**, NO reintenta el planning, NO ejecuta `generate_exp12_candidates` sobre datos oficiales, NO prueba otros seeds, NO selecciona D-HIGH/D-MID/D-LOW, NO cambia thresholds/seeds/quantiles/volumen/cobertura/TVD, NO ejecuta retrieval/BM25/Top-k/MRR y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt63 concluye:

```text
PROMPT63_EXTERNAL_AUDIT = PASS / APPROVED
PLAN_FAILURE_RECONCILIATION_V02 = APPROVED_FOR_INTEGRATION
PLAN_SUBSTANTIVE_CONTENT_CHANGED = false

EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_PLANNING_GATE = FAILED_UNDER_FROZEN_PLANNING_SEARCH
EXP12_PLANNING_RETRY = PROHIBITED_UNDER_AUTH_001
EXP12-P61-F001 = FAILURE_OBSERVABILITY_GAP / NON_INVALIDATING_FOR_ATTEMPT
NEXT_ELIGIBLE_BLOCK = EXP12_FEASIBILITY_FAILURE_FORENSIC_DESIGN
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato Plan v02 aprobado:

```text
branch = codex/plan-maestro-exp12-planning-failure-v02
commit = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
parent = 573a0c3ca4f28e8736671265e63fcfc852674290
```

El microclose `573a0c3... -> 5a3df4c...` modifica únicamente:

```text
Fecha de actualización: 2026-09-13 -> 2026-09-14
```

El candidato completo v02 es descendiente lineal de la rama canónica del Plan:

```text
canonical Plan = 532f7ad93b01881817a6c8cec9f6eb486e37b684
v02 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
commits_ahead = 2
commits_behind = 0
```

y ambos commits modifican únicamente el Plan Maestro.

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
origin/docs/plan-maestro-temporal-2026-08-31 = 532f7ad93b01881817a6c8cec9f6eb486e37b684
origin/codex/plan-maestro-exp12-planning-failure-v02 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Verifica para el Plan v02:

```text
base = 532f7ad93b01881817a6c8cec9f6eb486e37b684
head = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
commits_ahead = 2
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta del Plan v02

Mueve exclusivamente:

```text
docs/plan-maestro-temporal-2026-08-31
```

mediante fast-forward exacto:

```text
532f7ad93b01881817a6c8cec9f6eb486e37b684
→
5a3df4c2665ac5d1b57f7ef19b800d39758e6920
```

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/main = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 4. Principio metodológico del diagnóstico forense

El Attempt001 oficial es histórico e irreversible:

```text
EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED
```

El diagnóstico futuro **NO será un retry ni un planning oficial**. Será una reconstrucción forense explícitamente no gobernante del único seed que produjo el fallo observado:

```text
FORENSIC_SEED = 20262001
FORENSIC_CANDIDATE_INDEX_COUNT = 10000
```

Su única finalidad permitida será determinar el **breakdown exacto de factibilidad bajo las reglas ya congeladas**, sin seleccionar condiciones ni generar resultados oficiales.

El diagnóstico:

- no puede sustituir ni reinterpretar el Attempt001;
- no puede convertir su salida en `exp12_planning_summary`;
- no puede seleccionar D-HIGH/D-MID/D-LOW;
- no puede probar seeds distintos de `20262001`;
- no puede probar thresholds alternativos;
- no puede calcular escenarios “what-if”;
- no puede modificar el contrato v0.5;
- no puede autorizar un nuevo planning;
- no puede ejecutar retrieval ni evaluación;
- cualquier decisión posterior deberá ser prospectiva y auditada separadamente.

---

## 5. Fase B — preparar paquete forense en rama separada

Desde exactamente:

```text
428dfecca5cff313f910032a28a8a3c7ae13c2ef
```

crea:

```text
codex/exp12-feasibility-forensic-design-v01
```

Crea/modifica exclusivamente estos cuatro paths:

```text
docs/exp12_feasibility_failure_forensic_protocol_v0.1.md
src/experiments/diagnose_exp12_feasibility_failure_v01.py
tests/test_exp12_feasibility_failure_diagnostic_v01.py
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_design_readiness_v0.1.json
```

Un solo commit. No modifiques ningún archivo existente de contrato, runner, datos, Plan o Article.

---

## 6. Protocolo forense obligatorio

El documento:

```text
docs/exp12_feasibility_failure_forensic_protocol_v0.1.md
```

debe fijar como mínimo:

```text
status = FORENSIC_DESIGN_PENDING_EXTERNAL_AUDIT
scientific_base_commit = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
authorization_id_historical = EXP12_PLANNING_AUTH_001
attempt_id_historical = EXP12_PLANNING_ATTEMPT_001
historical_attempt_status = FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED
forensic_non_governing = true
forensic_seed = 20262001
candidate_indices = 0..9999
other_seeds_allowed = false
alternative_thresholds_allowed = false
condition_selection_allowed = false
retrieval_allowed = false
```

Bindings exactos:

```text
config = src/configs/exp12_historical_diversity_control_v0.5.json
config_sha256 = 1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264
runner = src/experiments/plan_exp12_historical_diversity_v01.py
runner_sha256 = cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac
sampling_universe = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sampling_universe_sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
H100 = data/processed/data_aduanas_historico_clase87_v0.2.csv
H100_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
EVAL = data/processed/data_aduanas_evalset_clase87_v0.2.csv
EVAL_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

El uso futuro de EVAL queda restringido a `DECLARACION` para overlap, exactamente como en el planning congelado. Prohibido leer NANDINA, descripciones o performance EVAL.

---

## 7. Implementación diagnóstica separada

Crea:

```text
src/experiments/diagnose_exp12_feasibility_failure_v01.py
```

### 7.1 Reutilización de semántica congelada

No copies ni reinterpretes fórmulas si pueden reutilizarse directamente del runner aprobado. Importa/reutiliza las primitivas necesarias de:

```text
src/experiments/plan_exp12_historical_diversity_v01.py
```

incluyendo, según corresponda:

- validador v0.5;
- validación de identidades de fuente;
- orden determinista SHA256;
- `_prefixes`;
- `_nearest_prefix`;
- `_candidate_label_counts`;
- `dam_concentration_metrics`;
- `total_variation_distance_full_support`.

No modifiques el runner oficial.

### 7.2 Alcance fijo

La implementación debe fallar si se intenta usar:

```text
seed != 20262001
candidate_count != 10000
maximum_tvd != 0.05
required_label_coverage_fraction != 1.0
volume_range != [2802,3098]
target_rows != 2950
```

Debe validar el contrato v0.5 y todos los bindings antes de cualquier diagnóstico.

### 7.3 Breakdown obligatorio

Para exactamente los 10,000 `candidate_index` del seed 20262001, registra sin seleccionar condiciones:

```text
candidate_indices_attempted

duplicate_dam_set_rejections
eval_overlap_rejections
unique_nonoverlap_candidates

volume_below_min_count
volume_within_range_count
volume_above_max_count

coverage_pass_count_among_volume_pass
coverage_fail_count_among_volume_pass

tvd_pass_count_among_volume_pass
tvd_fail_count_among_volume_pass

coverage_and_tvd_pass_count
coverage_pass_tvd_fail_count
coverage_fail_tvd_pass_count
coverage_and_tvd_fail_count

final_unique_feasible_count
minimum_required_unique_feasible = 30
historical_failure_condition_reproduced = (final_unique_feasible_count < 30)
```

Las cuatro celdas de cobertura×TVD deben sumar exactamente `volume_within_range_count`.

`final_unique_feasible_count` debe corresponder exactamente a candidatos que simultáneamente:

- no son duplicados;
- no solapan DAM EVAL;
- están dentro de `[2802,3098]`;
- tienen cobertura H100 `1.0`;
- tienen TVD full-support `<=0.05`.

### 7.4 Controles de contabilidad

Incluye invariantes fail-closed, como mínimo:

```text
candidate_indices_attempted = 10000
candidate_indices_attempted = duplicate_dam_set_rejections + eval_overlap_rejections + unique_nonoverlap_candidates
unique_nonoverlap_candidates = volume_below_min_count + volume_within_range_count + volume_above_max_count
volume_within_range_count = coverage_and_tvd_pass_count + coverage_pass_tvd_fail_count + coverage_fail_tvd_pass_count + coverage_and_tvd_fail_count
final_unique_feasible_count = coverage_and_tvd_pass_count
```

Respeta exactamente el orden de evaluación del generador oficial cuando una categoría dependa de ese orden.

### 7.5 Salida futura

Reserva, pero **NO crees en Prompt64**, la futura salida diagnóstica:

```text
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
```

La salida futura debe contener solo agregados de diagnóstico y bindings. No debe persistir:

- selección D-HIGH/D-MID/D-LOW;
- HHI de condiciones seleccionadas;
- ranking de candidatos;
- recomendaciones de nuevos thresholds;
- resultados retrieval;
- métricas EVAL.

No persistir listas de DAM candidatas salvo que sean estrictamente necesarias para una comprobación de integridad y, en tal caso, deben almacenarse solo como hashes no accionables; por defecto, no las incluyas.

### 7.6 CLI fail-closed

El módulo debe ser no ejecutor por defecto. Requiere una bandera explícita futura, por ejemplo:

```text
--execute-forensic-diagnostic
```

Sin esa bandera:

```text
status = NOT_EXECUTED
return_code != 0
```

En Prompt64 **NO uses** esa bandera sobre el pool oficial.

---

## 8. Pruebas sintéticas obligatorias

Crea:

```text
tests/test_exp12_feasibility_failure_diagnostic_v01.py
```

Las pruebas deben usar exclusivamente perfiles sintéticos y no leer el pool oficial, H100 oficial ni EVAL oficial.

Incluye como mínimo:

1. contabilidad exacta de 10,000 o de un `candidate_count` sintético inyectado solo en función interna de test, sin relajar el CLI/productivo;
2. caso con duplicados y verificación de `duplicate_dam_set_rejections`;
3. caso con candidato bajo/within/sobre volumen;
4. caso coverage PASS/TVD PASS;
5. coverage PASS/TVD FAIL;
6. coverage FAIL/TVD PASS;
7. coverage FAIL/TVD FAIL;
8. `final_unique_feasible_count == coverage_and_tvd_pass_count`;
9. equivalencia del **conteo final factible** entre la instrumentación diagnóstica y `generate_exp12_candidates(...)` para un caso sintético bajo mismos parámetros;
10. rechazo de seed distinto de `20262001` en la interfaz productiva;
11. rechazo de cambios a thresholds/volumen/candidate_count en la interfaz productiva;
12. CLI sin bandera = fail-closed y no ejecuta diagnóstico.

No ejecutes pruebas sobre datos oficiales.

---

## 9. Readiness artifact

Crea:

```text
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_design_readiness_v0.1.json
```

Debe registrar:

```text
artifact = EXP12_FEASIBILITY_FORENSIC_DESIGN_READINESS
version = v0.1
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
historical_attempt = EXP12_PLANNING_ATTEMPT_001
historical_authorization_consumed = true
forensic_non_governing = true
forensic_pool_execution_performed = false
planning_retry_performed = false
other_seeds_tested = false
alternative_thresholds_tested = false
condition_selection_performed = false
retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
```

Incluye hashes SHA-256 de los tres artefactos creados previamente en este paquete y el resultado de las pruebas sintéticas.

---

## 10. Prohibiciones absolutas

Durante Prompt64 NO:

- ejecutes diagnóstico sobre `new_historical_eligible.csv`;
- ejecutes `generate_exp12_candidates` sobre datos oficiales;
- ejecutes `execute_planning`;
- reintentes el Attempt001;
- crees otro `exp12_planning_summary`;
- pruebes seeds 20262002..20262010;
- pruebes candidate_count distinto de 10000 sobre datos oficiales;
- pruebes TVD distinta de 0.05;
- pruebes coverage distinta de 1.0;
- pruebes otro rango de volumen;
- calcules escenarios alternativos o “what-if”;
- selecciones condiciones;
- cambies config v0.5 o runner oficial;
- modifiques datasets;
- ejecutes retrieval/BM25/Top-k/MRR;
- leas NANDINA/descripciones/performance EVAL;
- crees autorización de nuevo planning;
- modifiques Article;
- avances a Grupo 2B o Grupo 3.

---

## 11. Verificaciones finales

Exige al final:

```text
origin/main = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato forense exige:

```text
parent = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
commits_ahead = 1
commits_behind = 0
changed_path_count = 4
```

y exactamente los cuatro paths fijados en §5.

Confirma:

```text
FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_RETRIEVAL_AUTHORIZED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 12. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/64_RESPUESTA_INTEGRAR_PLAN_POST_FALLO_Y_PREPARAR_DISENO_FORENSE_FACTIBILIDAD_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 13. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT64 = COMPLETED | STOP

main_final
plan_initial
plan_final
article_final
PLAN_POST_FAILURE_V02_INTEGRATED
PLAN_INTEGRATION_MODE

FORENSIC_BRANCH
FORENSIC_COMMIT
FORENSIC_PARENT
FORENSIC_CHANGED_PATH_COUNT
FORENSIC_CHANGED_PATHS
FORENSIC_PUBLISHED

FORENSIC_PROTOCOL_PATH
FORENSIC_DIAGNOSTIC_MODULE_PATH
FORENSIC_TEST_PATH
FORENSIC_READINESS_PATH
SYNTHETIC_TEST_COMMAND
SYNTHETIC_TEST_RESULT

FORENSIC_SEED = 20262001
FORENSIC_CANDIDATE_COUNT = 10000
FORENSIC_NON_GOVERNING = true
FORENSIC_POOL_EXECUTION_PERFORMED = false
OTHER_SEEDS_TESTED = false
ALTERNATIVE_THRESHOLDS_TESTED = false
CONDITION_SELECTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT64 = COMPLETED
PLAN_POST_FAILURE_V02 = INTEGRATED
EXP12_FEASIBILITY_FORENSIC_DESIGN_V01 = CANDIDATE / PENDING_EXTERNAL_AUDIT
FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```
