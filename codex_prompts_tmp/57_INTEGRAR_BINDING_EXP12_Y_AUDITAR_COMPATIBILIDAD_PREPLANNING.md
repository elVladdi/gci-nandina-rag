# PROMPT 57 — INTEGRAR BINDING EXP12 Y AUDITAR COMPATIBILIDAD PRE-PLANNING

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto el candidato de binding de fuente EXP12 v0.4 ya auditado externamente;
2. ejecutar una **auditoría técnica pre-planning, sin candidate generation**, para determinar si el código actual puede ejecutar de forma válida el planeamiento EXP12 sobre el nuevo universo fuente;
3. versionar únicamente un artefacto pequeño de evidencia de compatibilidad en una rama separada para auditoría externa.

Este bloque **NO ejecuta los 10,000 candidatos por seed**, NO selecciona D-HIGH/D-MID/D-LOW, NO ejecuta retrieval/BM25/Top-k/MRR, NO autoriza EXP12 y NO modifica todavía el algoritmo o los thresholds.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt56 concluye:

```text
PROMPT56_EXTERNAL_AUDIT = PASS / APPROVED
EXP12_SOURCE_BINDING_V04 = APPROVED_FOR_INTEGRATION
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato aprobado:

```text
branch = codex/exp12-source-binding-v04
commit = 5a402dc67c0b79e461bd272258534b731af38c3d
parent = 55847ed375202533f20fd09d72af41ced153a818
changed_path_count = 2
```

Los únicos paths del candidato son:

```text
src/configs/exp12_historical_diversity_control_v0.4.json
outputs/audits/exp12_source_activation_v0.2/exp12_sampling_universe_binding_v0.4.json
```

El universo fuente aprobado y bound es:

```text
path = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
rows = 7190
dam_count = 101
nandina_count = 84
H100_reference_coverage = 66/66
```

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 55847ed375202533f20fd09d72af41ced153a818
origin/codex/exp12-source-binding-v04 = 5a402dc67c0b79e461bd272258534b731af38c3d
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato source-binding exige:

```text
parent = 55847ed375202533f20fd09d72af41ced153a818
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta del source binding v0.4

Integra exclusivamente:

```text
55847ed375202533f20fd09d72af41ced153a818
→
5a402dc67c0b79e461bd272258534b731af38c3d
```

mediante fast-forward exacto de `main`.

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después del push exige:

```text
origin/main = 5a402dc67c0b79e461bd272258534b731af38c3d
```

No muevas Plan ni Article.

---

## 4. Fase B — auditoría técnica pre-planning de solo lectura

Lee íntegramente, desde el `main` ya integrado:

```text
src/configs/exp12_historical_diversity_control_v0.4.json
src/configs/exp12_historical_diversity_control_v0.3.json
src/experiments/plan_historical_bank_conditions_v03.py
data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
data/processed/data_aduanas_historico_clase87_v0.2.csv
```

Para EVAL usa exclusivamente:

```text
data/processed/data_aduanas_evalset_clase87_v0.2.csv
```

pero **solo puedes leer el identificador DAM/DECLARACION** para una comprobación de overlap. No leas NANDINA, descripciones ni métricas EVAL.

### 4.1 Identidad de entradas

Verifica:

```text
config_v04 exists
sampling_universe SHA = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
sampling_universe rows = 7190
sampling_universe DAM = 101
sampling_universe NANDINA total = 84
H100 SHA = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
H100 reference codes = 66
EVAL SHA = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
EVAL DAM overlap with sampling universe = 0
```

No materialices bancos ni subconjuntos.

### 4.2 Compatibilidad del validador actual

Sin ejecutar generación de candidatos, evalúa exclusivamente la función existente:

```text
validate_exp12_contract
```

de:

```text
src/experiments/plan_historical_bank_conditions_v03.py
```

contra `exp12_historical_diversity_control_v0.4.json`.

Esta llamada es una validación estática de contrato; no debe leer datasets ni generar candidatos.

Registra:

```text
LEGACY_V03_VALIDATE_EXP12_CONTRACT_RETURN = PASS | FAIL
LEGACY_V03_VALIDATE_EXP12_CONTRACT_ERROR = <exact error or null>
```

No cambies el código para hacer que pase.

Inspecciona además estáticamente si el CLI `main()` actual de `plan_historical_bank_conditions_v03.py` ofrece una ruta explícita para ejecutar el planeamiento EXP12 source-bound v0.4. Registra:

```text
LEGACY_V03_CLI_HAS_EXP12_SOURCE_BOUND_ENTRYPOINT = true/false
```

No invoques candidate generation.

### 4.3 Inventario de etiquetas fuera de H100

El nuevo universo tiene 84 NANDINA totales y H100 tiene 66 códigos de referencia. Calcula descriptivamente, sin construir candidatos:

```text
pool_total_nandina_codes
reference_h100_code_count
pool_reference_codes_present
pool_nonreference_code_count
pool_nonreference_codes
pool_rows_with_nonreference_code
pool_nonreference_row_fraction
pool_dams_with_any_nonreference_code
```

Esta inspección usa únicamente el pool histórico y H100. No usa EVAL labels ni desempeño.

### 4.4 Semántica exacta del control de distribución actual

Inspecciona, sin modificar nada:

```text
src/configs/exp12_historical_diversity_control_v0.4.json -> label_control.distribution_distance
src/experiments/plan_historical_bank_conditions_v03.py -> total_variation_distance
```

Registra literalmente:

```text
CONFIG_DISTRIBUTION_DISTANCE_FORMULA
CODE_TVD_ITERATION_SUPPORT
CODE_TVD_CANDIDATE_DENOMINATOR
CODE_TVD_REFERENCE_DENOMINATOR
NONREFERENCE_CODES_EXPLICITLY_INCLUDED_IN_DISTANCE_SUM = true/false
```

Determina únicamente como hecho matemático/código si, cuando un candidato contiene etiquetas no presentes en H100, la función implementada suma explícitamente una categoría adicional para esa masa no-referencia:

```text
FULL_SUPPORT_OTHER_BUCKET_IMPLEMENTED = true/false
```

No cambies fórmula, nombre, threshold ni código en Prompt57.

### 4.5 Disponibilidad de runner oficial de planning

Sin ejecutar el planeamiento, verifica si actualmente existe en `main` un runner/entrypoint que, a partir de v0.4, haga explícitamente todo lo siguiente:

```text
- valida config v0.4 source-bound;
- verifica SHA/rows/DAM/NANDINA del sampling universe;
- usa EVAL solo para DAM-overlap;
- usa H100 únicamente como referencia de distribución/labels;
- ejecuta exactamente 10,000 candidatos para cada seed congelado;
- aplica volumen [2802,3098];
- cobertura 1.0;
- TVD <= 0.05;
- mínimo 30 candidatos factibles;
- selecciona q10/q50/q90 de HHI;
- exige sets DAM distintos;
- exige HHI_DLOW > HHI_DMID > HHI_DHIGH;
- reporta los descriptores de manipulación congelados;
- no ejecuta retrieval.
```

Registra:

```text
OFFICIAL_EXP12_PLANNING_RUNNER_AVAILABLE = true/false
OFFICIAL_EXP12_PLANNING_RUNNER_PATH = <path|null>
```

No crees ese runner todavía.

---

## 5. Artefacto de evidencia

Crea exclusivamente:

```text
outputs/audits/exp12_planning_gate_v0.1/exp12_preplanning_compatibility_audit_v0.1.json
```

Debe contener como mínimo todos los resultados de 4.1–4.5 y además:

```text
artifact = EXP12_PREPLANNING_COMPATIBILITY_AUDIT
version = v0.1
main_commit = 5a402dc67c0b79e461bd272258534b731af38c3d
config_path = src/configs/exp12_historical_diversity_control_v0.4.json
sampling_universe_path = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
candidate_generation_executed = false
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

No declares PASS/FAIL metodológico global de IA Experimental. Codex debe reportar hechos observados y bloqueos técnicos, no decidir si se modifica el contrato.

---

## 6. Versionado separado

Crea desde exactamente:

```text
5a402dc67c0b79e461bd272258534b731af38c3d
```

la rama:

```text
codex/exp12-preplanning-compatibility-audit-v01
```

Un solo commit que añada exclusivamente:

```text
outputs/audits/exp12_planning_gate_v0.1/exp12_preplanning_compatibility_audit_v0.1.json
```

No modifiques código, configs, datos, Plan ni Article.

Publica la rama para auditoría externa. No la integres a `main`.

---

## 7. Prohibiciones absolutas

Durante Prompt57 NO:

- ejecutes `generate_exp12_candidates` sobre el pool oficial;
- ejecutes 10,000 candidatos por seed;
- selecciones D-HIGH/D-MID/D-LOW;
- calcules HHI/TVD de candidatos oficiales;
- materialices bancos EXP12;
- ejecutes retrieval/BM25/Top-k/MRR;
- leas labels, descripciones o desempeño EVAL;
- cambies `maximum_tvd = 0.05`;
- cambies cobertura 1.0;
- cambies [2802,3098];
- cambies seeds;
- cambies quantiles;
- cambies candidate_count;
- modifiques v0.3 o v0.4;
- modifiques el planner v03;
- crees un planner/runner nuevo;
- crees autorización EXP12;
- modifiques Plan;
- modifiques Article;
- avances a Grupo 2B o Grupo 3.

---

## 8. Verificaciones finales

Exige:

```text
origin/main = 5a402dc67c0b79e461bd272258534b731af38c3d
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para la rama de auditoría:

```text
parent = 5a402dc67c0b79e461bd272258534b731af38c3d
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
```

Y:

```text
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 9. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/57_RESPUESTA_INTEGRAR_BINDING_EXP12_Y_AUDITAR_COMPATIBILIDAD_PREPLANNING.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 10. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT57 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

EXP12_SOURCE_BINDING_V04_INTEGRATED = true/false
INTEGRATION_MODE

AUDIT_BRANCH
AUDIT_COMMIT
AUDIT_PARENT
AUDIT_CHANGED_PATH_COUNT
AUDIT_ARTIFACT_PATH
AUDIT_ARTIFACT_SHA256

SAMPLING_UNIVERSE_SHA_VALIDATION
SAMPLING_UNIVERSE_ROWS
SAMPLING_UNIVERSE_DAM_COUNT
SAMPLING_UNIVERSE_NANDINA_COUNT
EVAL_DAM_OVERLAP_COUNT

LEGACY_V03_VALIDATE_EXP12_CONTRACT_RETURN
LEGACY_V03_VALIDATE_EXP12_CONTRACT_ERROR
LEGACY_V03_CLI_HAS_EXP12_SOURCE_BOUND_ENTRYPOINT

POOL_NONREFERENCE_CODE_COUNT
POOL_NONREFERENCE_CODES
POOL_ROWS_WITH_NONREFERENCE_CODE
POOL_NONREFERENCE_ROW_FRACTION
POOL_DAMS_WITH_ANY_NONREFERENCE_CODE

CONFIG_DISTRIBUTION_DISTANCE_FORMULA
CODE_TVD_ITERATION_SUPPORT
CODE_TVD_CANDIDATE_DENOMINATOR
CODE_TVD_REFERENCE_DENOMINATOR
NONREFERENCE_CODES_EXPLICITLY_INCLUDED_IN_DISTANCE_SUM
FULL_SUPPORT_OTHER_BUCKET_IMPLEMENTED

OFFICIAL_EXP12_PLANNING_RUNNER_AVAILABLE
OFFICIAL_EXP12_PLANNING_RUNNER_PATH

EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT57 = COMPLETED
EXP12_SOURCE_BINDING_V04 = INTEGRATED
EXP12_PREPLANNING_COMPATIBILITY_AUDIT = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP12_PLANNING_EXECUTED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
