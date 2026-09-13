# PROMPT 58 — INTEGRAR AUDITORÍA PRE-PLANNING Y PREPARAR CORRECCIÓN DE COMPATIBILIDAD EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto la auditoría pre-planning EXP12 v0.1 ya auditada externamente;
2. preparar un **paquete correctivo pre-planning** que resuelva los tres bloqueos técnicos confirmados antes de ejecutar candidate generation oficial;
3. versionar ese paquete en una rama separada para nueva auditoría externa.

Este bloque **NO ejecuta los 10,000 candidatos por seed sobre el pool oficial**, NO selecciona D-HIGH/D-MID/D-LOW oficiales, NO ejecuta retrieval/BM25/Top-k/MRR, NO autoriza EXP12 y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt57 concluye:

```text
PROMPT57_EXTERNAL_AUDIT = PASS / APPROVED
EXP12_PREPLANNING_COMPATIBILITY_AUDIT = APPROVED_FOR_INTEGRATION

CONFIRMED_TECHNICAL_BLOCKERS =
1. LEGACY_V03_VALIDATE_EXP12_CONTRACT_REJECTS_V04_SOURCE_BOUND_STATUS
2. LEGACY_V03_CLI_HAS_NO_EXP12_SOURCE_BOUND_ENTRYPOINT
3. CURRENT_TVD_SUM_DOES_NOT_EXPLICITLY_INCLUDE_NONREFERENCE_SUPPORT_OR_AN_OTHER_BUCKET

EXP12_PLANNING = BLOCKED_PENDING_PREEXECUTION_CORRECTION
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

La auditoría confirmó además que el pool aprobado contiene:

```text
rows = 7190
DAM = 101
NANDINA total = 84
H100 reference codes = 66
nonreference codes = 18
rows with nonreference code = 237
nonreference row fraction = 0.032962447844228096
```

No existe resultado EXP12 oficial y no se ha ejecutado candidate generation oficial. Por tanto, la corrección siguiente es **prospectiva y pre-ejecución**.

---

## 2. Decisión metodológica externa sobre TVD

IA Experimental fija prospectivamente, antes de cualquier planeamiento oficial, la siguiente interpretación matemática:

```text
EXP12_TVD_SUPPORT = FULL_REFERENCE_SUPPORT_PLUS_OTHER
```

La referencia H100 tiene probabilidad cero fuera de sus 66 códigos. Para un candidato que puede contener códigos NANDINA no presentes en H100, la TVD correcta debe calcularse sobre soporte común completo mediante una categoría agregada `OTHER`:

```text
p_c = candidate_count(c) / candidate_rows              para cada c en H100
q_c = H100_count(c) / H100_rows                        para cada c en H100
p_OTHER = sum(candidate_count(x) for x not in H100) / candidate_rows
q_OTHER = 0

TVD = 0.5 * (
    sum_{c in H100} abs(p_c - q_c)
    + abs(p_OTHER - q_OTHER)
)
```

Agregar todos los códigos no-H100 a `OTHER` es matemáticamente equivalente a incluir individualmente cada código extra porque la referencia asigna masa cero a todos ellos.

Esta corrección:

- **NO cambia** `maximum_tvd = 0.05`;
- **NO cambia** cobertura requerida `1.0` sobre los 66 códigos H100;
- **NO cambia** volumen, seeds, cuantiles, HHI ni candidate_count;
- evita subestimar la distancia cuando existe masa no-referencia;
- se realiza antes de observar cualquier resultado oficial de EXP12;
- no debe elegirse ni ajustarse para obtener factibilidad.

No uses renormalización condicional que descarte la masa no-referencia.

---

## 3. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 5a402dc67c0b79e461bd272258534b731af38c3d
origin/codex/exp12-preplanning-compatibility-audit-v01 = 025136e9067a415388699a55b9aa718145ae193e
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato de auditoría exige:

```text
parent = 5a402dc67c0b79e461bd272258534b731af38c3d
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.1/exp12_preplanning_compatibility_audit_v0.1.json
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 4. Fase A — integración exacta de la auditoría pre-planning

Integra exclusivamente:

```text
5a402dc67c0b79e461bd272258534b731af38c3d
→
025136e9067a415388699a55b9aa718145ae193e
```

mediante fast-forward exacto de `main`.

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/main = 025136e9067a415388699a55b9aa718145ae193e
```

No muevas Plan ni Article.

---

## 5. Fase B — crear contrato correctivo EXP12 v0.5

### 5.1 Baseline

Lee íntegramente desde el `main` integrado:

```text
src/configs/exp12_historical_diversity_control_v0.4.json
outputs/audits/exp12_planning_gate_v0.1/exp12_preplanning_compatibility_audit_v0.1.json
src/experiments/plan_historical_bank_conditions_v03.py
```

No edites v0.4 ni el planner v03. Son evidencia histórica.

Crea:

```text
src/configs/exp12_historical_diversity_control_v0.5.json
```

partiendo semánticamente de v0.4.

### 5.2 Cambios permitidos en v0.5

Como mínimo:

```text
experiment_id = exp12_historical_diversity_control_v0.5
version = v0.5
contract_status = PREPLANNING_COMPATIBILITY_CORRECTED_PENDING_EXTERNAL_AUDIT
method_contract = FROZEN_METHOD_SOURCE_BOUND_TVD_FULL_SUPPORT_PENDING_EXTERNAL_AUDIT
execution_authorized = false
```

Mantén el mismo `sampling_universe` source-bound de v0.4 sin alterar path/SHA/rows/DAM/NANDINA.

En `label_control`, preserva:

```text
required_label_coverage_fraction = 1.0
maximum_tvd = 0.05
reference = H100_FROZEN_REFERENCE
reference_label_set = all NANDINA present in reference_h100
reference_label_distribution = series proportion by NANDINA in reference_h100
```

Cambia únicamente la semántica de distancia para que quede explícita y auditable. Debe incluir campos equivalentes a:

```text
distribution_distance = TVD_FULL_SUPPORT_H100_PLUS_OTHER
distribution_distance_formula = 0.5 * (sum_{c in H100} abs(p_c - q_c) + abs(p_OTHER - 0))
nonreference_support_policy = AGGREGATE_ALL_NON_H100_CODES_AS_OTHER_WITH_REFERENCE_MASS_ZERO
candidate_probability_denominator = ALL_CANDIDATE_ROWS
reference_probability_denominator = ALL_H100_ROWS
conditional_renormalization_over_h100_only = false
```

Puedes conservar también una nota histórica sobre la fórmula v0.4, pero no la presentes como vigente.

En `future_manipulation_check.execution_gate` usa un estado equivalente a:

```text
PREPLANNING_COMPATIBILITY_PACKAGE_PENDING_EXTERNAL_AUDIT
```

No introduzcas ningún threshold nuevo.

### 5.3 Parámetros que deben permanecer idénticos a v0.4

Salvo los campos de versión/estado y la aclaración matemática TVD anterior, deben permanecer semánticamente idénticos:

```text
fixed_eval completo
sampling_universe completo
reference_h100 completo
volume_control completo
replicate_policy completo
conditions completo
primary_diversity_variable completo
label_control.required_label_coverage_fraction
label_control.maximum_tvd
selection completo
candidate_generation completo
feasibility_filter completo
condition_selection completo
future_manipulation_check.required_reports
future_manipulation_check.hhi_span_formula
future_manipulation_check.effective_dam_ratio_formula
future_manipulation_check.strict_hhi_order_fail_closed
future_manipulation_check.manipulation_strength_review_required
future_manipulation_check.new_threshold_introduced
primary_diversity_measures
secondary_diversity_measures
duplicate_measurement
controls
evaluation_contract
output_contract
```

---

## 6. Fase C — crear implementación EXP12 pre-planning separada

No modifiques:

```text
src/experiments/plan_historical_bank_conditions_v03.py
```

Crea un módulo nuevo dedicado:

```text
src/experiments/plan_exp12_historical_diversity_v01.py
```

Debe implementar exclusivamente la ruta EXP12 source-bound y no tocar EXP11.

### 6.1 Validador v0.5

Debe validar fail-closed, como mínimo:

```text
contract_status = PREPLANNING_COMPATIBILITY_CORRECTED_PENDING_EXTERNAL_AUDIT
method_contract = FROZEN_METHOD_SOURCE_BOUND_TVD_FULL_SUPPORT_PENDING_EXTERNAL_AUDIT
execution_authorized = false
sampling_universe.source = NEW_HISTORICAL_GATE_EXTENSION_V02_APPROVED
sampling_universe.path exacto
sampling_universe.sha256 exacto
sampling_universe.rows = 7190
sampling_universe.dam_count = 101
sampling_universe.nandina_count = 84
sampling_universe.must_not_fallback_to_h100 = true
fixed EVAL SHA exacto
H100 SHA exacto
volume [2802,3098]
target_rows = 2950
candidate_count = 10000
seed schedule exacta 20262001..20262010
coverage = 1.0
maximum_tvd = 0.05
minimum feasible candidates = 30
quantiles D-HIGH=0.1, D-MID=0.5, D-LOW=0.9
strict HHI ordering
complete DAM requirement
uses_eval_performance = false
uses_eval_labels_for_selection = false
```

No debe aceptar v0.4 como si fuera v0.5.

### 6.2 Función TVD corregida

Implementa una función explícita con semántica full-support.

Debe:

- usar todas las filas del candidato como denominador;
- usar todas las filas H100 como denominador de referencia;
- sumar las diferencias absolutas para los 66 códigos H100;
- sumar además la masa total de códigos no-H100 como `OTHER` frente a referencia 0;
- validar que la suma de conteos del candidato sea consistente con `candidate_rows`;
- no renormalizar excluyendo códigos no-H100.

### 6.3 Candidate generation

Implementa la misma lógica congelada de v0.4/v03:

```text
10,000 candidate_index por seed
orden = SHA256(seed:candidate_index:dam_id)
complete-DAM prefix nearest to target_rows=2950
tie break = fewer DAMs, then SHA of sorted DAM ids
deduplicate by sorted DAM tuple
reject EVAL DAM overlap
volume [2802,3098]
coverage H100 = 1.0
TVD full-support <= 0.05
```

No ejecutes esta función sobre el pool oficial en Prompt58.

### 6.4 Selección de condiciones

Implementa sin ejecutar oficialmente:

```text
minimum unique feasible = 30
sort HHI ascending
D-HIGH q=0.1
D-MID q=0.5
D-LOW q=0.9
quantile index = floor(q*(n-1))
distinct DAM sets
HHI_DLOW > HHI_DMID > HHI_DHIGH
```

### 6.5 Runner/CLI oficial futuro

El módulo debe proporcionar un CLI explícito para el planeamiento EXP12, pero fail-closed por defecto.

Debe requerir una bandera inequívoca, por ejemplo:

```text
--execute-planning
```

Sin esa bandera no debe generar candidatos oficiales.

La ejecución futura deberá aceptar explícitamente:

```text
--config src/configs/exp12_historical_diversity_control_v0.5.json
--sampling-universe <path exacto>
--h100 <path exacto>
--eval <path exacto>
--output-dir <dir nuevo>
--execute-planning
```

El runner futuro debe usar EVAL exclusivamente para DAM/DECLARACION overlap durante planning. No debe leer NANDINA, descripciones ni performance EVAL.

No ejecutes `--execute-planning` en Prompt58.

---

## 7. Fase D — pruebas sintéticas obligatorias

Crea:

```text
tests/test_exp12_preplanning_compatibility_v01.py
```

Las pruebas deben ser **sintéticas** y no ejecutar los 100,000 candidatos sobre el pool oficial.

Incluye al menos:

### 7.1 TVD sin códigos extra

Cuando candidato y referencia tienen el mismo soporte y distribución, TVD = 0.

### 7.2 TVD con `OTHER`

Ejemplo mínimo obligatorio o equivalente:

```text
reference = A:50, B:50
candidate = A:45, B:45, X:10
candidate_rows = 100
```

Debe resultar:

```text
TVD = 0.10
```

No `0.05`.

### 7.3 Consistencia de denominador

Si `candidate_rows != sum(candidate_label_counts.values())`, debe fallar explícitamente.

### 7.4 Validador

- v0.5 válido debe pasar;
- una copia con `maximum_tvd != 0.05` debe fallar;
- una copia con `candidate_count != 10000` debe fallar;
- una copia con `execution_authorized=true` debe fallar para este paquete pre-planning;
- v0.4 debe ser rechazado por el validador v0.5.

### 7.5 Fail-closed CLI

Sin `--execute-planning`, el CLI no debe ejecutar candidate generation oficial.

Las pruebas no deben modificar datos oficiales.

---

## 8. Artefacto de readiness obligatorio

Crea:

```text
outputs/audits/exp12_planning_gate_v0.2/exp12_preplanning_correction_readiness_v0.2.json
```

Debe incluir como mínimo:

```text
artifact = EXP12_PREPLANNING_CORRECTION_READINESS
version = v0.2
baseline_audit_commit = 025136e9067a415388699a55b9aa718145ae193e
baseline_config = src/configs/exp12_historical_diversity_control_v0.4.json
candidate_config = src/configs/exp12_historical_diversity_control_v0.5.json
planning_module = src/experiments/plan_exp12_historical_diversity_v01.py
test_path = tests/test_exp12_preplanning_compatibility_v01.py
```

Registra:

```text
blocker_legacy_validator = CLOSED_BY_SEPARATE_V05_VALIDATOR_CANDIDATE
blocker_missing_exp12_cli = CLOSED_BY_DEDICATED_FAIL_CLOSED_RUNNER_CANDIDATE
blocker_tvd_partial_support = CLOSED_BY_FULL_SUPPORT_OTHER_CORRECTION_CANDIDATE
```

Incluye:

```text
tvd_semantics = FULL_REFERENCE_SUPPORT_PLUS_OTHER
maximum_tvd = 0.05
coverage_fraction_required = 1.0
thresholds_changed = false
seeds_changed = false
quantiles_changed = false
candidate_count_changed = false
volume_bounds_changed = false
results_used_to_choose_correction = false
```

Incluye hashes SHA-256 de los tres nuevos artefactos principales y resultado exacto de pytest.

Además:

```text
official_pool_candidate_generation_executed = false
planning_10000_candidates_per_seed_executed = false
condition_selection_executed = false
retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
eval_labels_read = false
eval_descriptions_read = false
eval_performance_read = false
exp12_authorized = false
exp12_executed = false
group2b_started = false
group3_started = false
```

---

## 9. Versionado del paquete correctivo

Después de integrar la Fase A, crea desde exactamente:

```text
025136e9067a415388699a55b9aa718145ae193e
```

la rama:

```text
codex/exp12-preplanning-correction-v01
```

Un solo commit que añada exclusivamente:

```text
src/configs/exp12_historical_diversity_control_v0.5.json
src/experiments/plan_exp12_historical_diversity_v01.py
tests/test_exp12_preplanning_compatibility_v01.py
outputs/audits/exp12_planning_gate_v0.2/exp12_preplanning_correction_readiness_v0.2.json
```

No modifiques ningún archivo existente.

Publica la rama para auditoría externa. No la integres a `main` en Prompt58.

No modifiques Plan ni Article todavía.

---

## 10. Prohibiciones absolutas

Durante Prompt58 NO:

- ejecutes candidate generation sobre `new_historical_eligible.csv` oficial;
- ejecutes 10,000 candidatos por seed oficiales;
- selecciones condiciones oficiales;
- materialices bancos EXP12 oficiales;
- cambies `maximum_tvd = 0.05`;
- cambies cobertura 1.0;
- cambies [2802,3098];
- cambies seeds;
- cambies quantiles;
- cambies candidate_count;
- renormalices el candidato solo sobre códigos H100;
- uses labels/descripciones/performance EVAL;
- ejecutes retrieval/BM25/Top-k/MRR;
- modifiques v0.4;
- modifiques planner v03;
- crees autorización EXP12;
- modifiques Plan;
- modifiques Article;
- avances a Grupo 2B o Grupo 3.

---

## 11. Verificaciones finales

Exige al final:

```text
origin/main = 025136e9067a415388699a55b9aa718145ae193e
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el paquete correctivo:

```text
parent = 025136e9067a415388699a55b9aa718145ae193e
commits_ahead = 1
commits_behind = 0
changed_path_count = 4
```

Y:

```text
OFFICIAL_EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 12. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/58_RESPUESTA_INTEGRAR_AUDITORIA_PREPLANNING_Y_PREPARAR_CORRECCION_COMPATIBILIDAD_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 13. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT58 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

PREPLANNING_AUDIT_V01_INTEGRATED = true/false
INTEGRATION_MODE

CORRECTION_BRANCH
CORRECTION_COMMIT
CORRECTION_PARENT
CORRECTION_CHANGED_PATH_COUNT
CORRECTION_CHANGED_PATHS

CONFIG_V05_PATH
CONFIG_V05_SHA256
PLANNING_MODULE_PATH
PLANNING_MODULE_SHA256
TEST_PATH
TEST_SHA256
READINESS_PATH
READINESS_SHA256

TVD_SEMANTICS = FULL_REFERENCE_SUPPORT_PLUS_OTHER
MAXIMUM_TVD = 0.05
THRESHOLDS_CHANGED = false
SEEDS_CHANGED = false
QUANTILES_CHANGED = false
CANDIDATE_COUNT_CHANGED = false
VOLUME_BOUNDS_CHANGED = false

PYTEST_COMMAND
PYTEST_RETURN_CODE
PYTEST_SUMMARY

OFFICIAL_EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT58 = COMPLETED
EXP12_PREPLANNING_COMPATIBILITY_AUDIT = INTEGRATED
EXP12_PREPLANNING_CORRECTION = CANDIDATE / PENDING_EXTERNAL_AUDIT
OFFICIAL_EXP12_PLANNING_EXECUTED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
