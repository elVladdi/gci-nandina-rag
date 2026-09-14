# PROMPT 65 — INTEGRAR DISEÑO FORENSE Y PREPARAR AUTORIZACIÓN DE DIAGNÓSTICO EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto el paquete de diseño forense EXP12 v0.1 ya auditado externamente;
2. ejecutar un preflight técnico final **sin usar el pool oficial para diagnóstico**;
3. volver a ejecutar únicamente las pruebas sintéticas del paquete;
4. crear y publicar, en una rama separada, un **candidato de autorización one-shot exclusivamente para el diagnóstico forense no gobernante del seed 20262001**.

Este bloque **NO ejecuta** `--execute-forensic-diagnostic` sobre el pool oficial, NO reintenta el planning, NO ejecuta `generate_exp12_candidates` sobre datos oficiales, NO prueba otros seeds, NO selecciona D-HIGH/D-MID/D-LOW, NO cambia thresholds/seeds/quantiles/volumen/cobertura/TVD, NO ejecuta retrieval/BM25/Top-k/MRR y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt64 concluye:

```text
PROMPT64_EXTERNAL_AUDIT = PASS / APPROVED
PLAN_POST_FAILURE_V02 = INTEGRATED / VERIFIED
EXP12_FEASIBILITY_FORENSIC_DESIGN_V01 = APPROVED_FOR_INTEGRATION
FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato forense aprobado:

```text
branch = codex/exp12-feasibility-forensic-design-v01
commit = 79fc10d161c735a5d727e36ed65554a89f937e3b
parent = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
commits_ahead = 1
commits_behind = 0
changed_path_count = 4
```

Paths exactos:

```text
docs/exp12_feasibility_failure_forensic_protocol_v0.1.md
src/experiments/diagnose_exp12_feasibility_failure_v01.py
tests/test_exp12_feasibility_failure_diagnostic_v01.py
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_design_readiness_v0.1.json
```

El diseño fija:

```text
forensic_non_governing = true
forensic_seed = 20262001
candidate_indices = 0..9999
candidate_count = 10000
other_seeds_allowed = false
alternative_thresholds_allowed = false
condition_selection_allowed = false
retrieval_allowed = false
```

La auditoría externa verificó estáticamente que la instrumentación preserva el orden lógico del generador congelado —deduplicación, overlap EVAL, volumen, cobertura y TVD— y que el conteo final factible se define exactamente como el conjunto que supera simultáneamente todas las reglas congeladas. Las pruebas 14/14 fueron reportadas por Codex en Prompt64; no constituyen reejecución independiente de IA Experimental.

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
origin/codex/exp12-feasibility-forensic-design-v01 = 79fc10d161c735a5d727e36ed65554a89f937e3b
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

y exactamente los cuatro paths enumerados en §1.

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta del diseño forense

Integra exclusivamente:

```text
428dfecca5cff313f910032a28a8a3c7ae13c2ef
→
79fc10d161c735a5d727e36ed65554a89f937e3b
```

mediante fast-forward exacto de `main`.

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/main = 79fc10d161c735a5d727e36ed65554a89f937e3b
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 4. Fase B — preflight del paquete sin diagnóstico oficial

Trabaja sobre un checkout/worktree nuevo, aislado y limpio del `main` exacto ya integrado:

```text
79fc10d161c735a5d727e36ed65554a89f937e3b
```

Exige:

```text
TRACKED_WORKING_TREE_CLEAN = true
```

### 4.1 Identidad del paquete forense

Verifica identidad canónica Git/LF de:

```text
docs/exp12_feasibility_failure_forensic_protocol_v0.1.md
sha256 = 2c5079609acead65621598f05f413282ef15c6e1d94ae51c47363d826fad7891

src/experiments/diagnose_exp12_feasibility_failure_v01.py
sha256 = 8d5ab67d79e994c94055ba58bf22d12b1a35e053eb465c5aece9b8f540d0ff4c

tests/test_exp12_feasibility_failure_diagnostic_v01.py
sha256 = 5be6fe4f49ebfd6f005cb2286adc3662e8d0c9d03395b57ecd6e22efaa3a9411
```

Calcula y reporta además el SHA-256 canónico Git/LF del readiness artifact:

```text
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_design_readiness_v0.1.json
```

No modifiques ninguno.

### 4.2 Bindings históricos y científicos

Verifica por hash, sin ejecutar el diagnóstico:

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

Hashing no autoriza ni implica leer semánticamente labels, descripciones o performance EVAL.

### 4.3 Pruebas permitidas

Ejecuta exclusivamente:

```text
python -m unittest tests.test_exp12_feasibility_failure_diagnostic_v01 -v
```

Debe usar únicamente perfiles sintéticos conforme al test versionado.

Exige:

```text
14 tests
0 failures
0 errors
```

No ejecutes ninguna otra prueba que use datasets oficiales.

### 4.4 CLI fail-closed

Invoca el módulo **sin** `--execute-forensic-diagnostic` y exige:

```text
return_code = 2
status = NOT_EXECUTED
```

No suministres la bandera de ejecución.

### 4.5 Pristine state de salida diagnóstica

Ruta reservada:

```text
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
```

Exige antes de crear la autorización:

```text
FORENSIC_OUTPUT_EXISTS = false
FORENSIC_OUTPUT_TRACKED = false
FORENSIC_OUTPUT_UNTRACKED = false
FORENSIC_OUTPUT_PARENT_DIR_UNTRACKED = false
```

No borres, renombres ni sobrescribas nada para hacer pasar este gate.

---

## 5. Fase C — candidato de autorización one-shot del diagnóstico forense

Desde exactamente:

```text
79fc10d161c735a5d727e36ed65554a89f937e3b
```

crea la rama:

```text
codex/exp12-feasibility-forensic-authorization-v01
```

Un solo commit que añada exclusivamente:

```text
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.1.json
```

No modifiques código, protocolo, config, tests, datos, Plan ni Article.

### 5.1 Contenido mínimo obligatorio

El JSON debe incluir como mínimo:

```text
artifact = EXP12_FEASIBILITY_FORENSIC_EXECUTION_AUTHORIZATION
version = v0.1
authorization_id = EXP12_FORENSIC_AUTH_001
diagnostic_attempt_id = EXP12_FORENSIC_ATTEMPT_001
status = AUTHORIZED_ONE_SHOT_FORENSIC_DIAGNOSTIC
scope = NON_GOVERNING_RECONSTRUCTION_SEED_20262001_10000_INDICES_AGGREGATE_ONLY

effective_only_if_external_audit_passes = true
effective_only_if_integrated_to_main = true
authorization_effective_in_candidate_branch = false
single_use = true
retry_allowed = false
resume_allowed = false
overwrite_allowed = false
partial_recomputation_allowed = false

historical_planning_authorization_id = EXP12_PLANNING_AUTH_001
historical_planning_attempt_id = EXP12_PLANNING_ATTEMPT_001
historical_planning_attempt_status = FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED
historical_planning_retry_remains_prohibited = true

diagnostic_design_commit = 79fc10d161c735a5d727e36ed65554a89f937e3b
scientific_base_commit = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
forensic_protocol_path = docs/exp12_feasibility_failure_forensic_protocol_v0.1.md
forensic_protocol_sha256 = 2c5079609acead65621598f05f413282ef15c6e1d94ae51c47363d826fad7891
diagnostic_module_path = src/experiments/diagnose_exp12_feasibility_failure_v01.py
diagnostic_module_sha256 = 8d5ab67d79e994c94055ba58bf22d12b1a35e053eb465c5aece9b8f540d0ff4c

config_path = src/configs/exp12_historical_diversity_control_v0.5.json
config_sha256 = 1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264
runner_path = src/experiments/plan_exp12_historical_diversity_v01.py
runner_sha256 = cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac
sampling_universe_path = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sampling_universe_sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
h100_path = data/processed/data_aduanas_historico_clase87_v0.2.csv
h100_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
eval_path = data/processed/data_aduanas_evalset_clase87_v0.2.csv
eval_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
eval_usage = DECLARACION_OVERLAP_ONLY

forensic_non_governing = true
seed = 20262001
candidate_count = 10000
target_rows = 2950
volume_range = [2802,3098]
required_label_coverage_fraction = 1.0
maximum_tvd = 0.05
tvd_support = FULL_REFERENCE_SUPPORT_PLUS_OTHER
minimum_required_unique_feasible = 30
other_seeds_allowed = false
alternative_thresholds_allowed = false
condition_selection_allowed = false

output_path = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
```

Congela como comando lógico futuro exacto:

```text
python src/experiments/diagnose_exp12_feasibility_failure_v01.py \
  --config src/configs/exp12_historical_diversity_control_v0.5.json \
  --sampling-universe data/interim/new_historical_gate_v0.2/new_historical_eligible.csv \
  --h100 data/processed/data_aduanas_historico_clase87_v0.2.csv \
  --eval data/processed/data_aduanas_evalset_clase87_v0.2.csv \
  --output outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json \
  --seed 20262001 \
  --candidate-count 10000 \
  --target-rows 2950 \
  --minimum-rows 2802 \
  --maximum-rows 3098 \
  --required-label-coverage-fraction 1.0 \
  --maximum-tvd 0.05 \
  --execute-forensic-diagnostic
```

Registra resultados de §4 y además:

```text
forensic_pool_execution_performed = false
planning_reexecuted = false
condition_selection_performed = false
other_seeds_tested = false
alternative_thresholds_tested = false
retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
exp12_retrieval_authorized = false
group2b_started = false
group3_started = false
```

### 5.2 Semántica futura de ejecución

Solo después de integración y nueva aprobación externa, el futuro ejecutor deberá:

1. verificar refs, bindings, clean checkout y ausencia total del output reservado;
2. crear inmediatamente antes de la invocación un marcador de consumo separado;
3. ejecutar exactamente una invocación del comando congelado;
4. no reintentar, reanudar, sobrescribir ni recomputar parcialmente si falla;
5. versionar marcador, stdout, stderr, reporte y salida diagnóstica si existe;
6. no usar el resultado para modificar retroactivamente Attempt001;
7. no probar otros seeds ni thresholds;
8. someter el diagnóstico a auditoría externa antes de cualquier decisión metodológica posterior.

Reserva el futuro marcador en:

```text
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_forensic_attempt_001_consumption_marker.json
```

No lo crees en Prompt65.

---

## 6. Prohibiciones absolutas

Durante Prompt65 NO:

- ejecutes `--execute-forensic-diagnostic` sobre datos oficiales;
- ejecutes `generate_exp12_candidates` sobre datos oficiales;
- recomputes el seed oficial fuera de los perfiles sintéticos de test;
- pruebes otros seeds;
- pruebes thresholds alternativos;
- cambies candidate_count, minimum feasible, seeds, quantiles, volumen, coverage o TVD;
- selecciones condiciones oficiales;
- modifiques runner/config/datasets;
- crees outputs forenses oficiales;
- ejecutes planning oficial;
- ejecutes retrieval/BM25/Top-k/MRR;
- leas labels/descripciones/performance EVAL;
- autorices retrieval EXP12;
- modifiques Plan o Article;
- avances a Grupo 2B o Grupo 3.

---

## 7. Verificaciones finales

Exige:

```text
origin/main = 79fc10d161c735a5d727e36ed65554a89f937e3b
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato de autorización exige:

```text
parent = 79fc10d161c735a5d727e36ed65554a89f937e3b
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.1.json
```

Y confirma:

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

## 8. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/65_RESPUESTA_INTEGRAR_DISENO_FORENSE_Y_PREPARAR_AUTORIZACION_DIAGNOSTICO_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 9. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT65 = COMPLETED | STOP

main_initial
main_final
plan_final
article_final

FORENSIC_DESIGN_V01_INTEGRATED
INTEGRATION_MODE

FORENSIC_PROTOCOL_SHA_VALIDATION
FORENSIC_MODULE_SHA_VALIDATION
FORENSIC_TEST_SHA_VALIDATION
FORENSIC_READINESS_SHA256
SYNTHETIC_TEST_RESULT
CLI_WITHOUT_EXECUTE_FORENSIC_DIAGNOSTIC
FORENSIC_OUTPUT_PRISTINE

AUTHORIZATION_BRANCH
AUTHORIZATION_COMMIT
AUTHORIZATION_PARENT
AUTHORIZATION_CHANGED_PATH_COUNT
AUTHORIZATION_CHANGED_PATH
AUTHORIZATION_PUBLISHED
AUTHORIZATION_ID
DIAGNOSTIC_ATTEMPT_ID
AUTHORIZATION_STATUS
AUTHORIZATION_EFFECTIVE_IN_CANDIDATE_BRANCH = false

FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT65 = COMPLETED
EXP12_FEASIBILITY_FORENSIC_DESIGN_V01 = INTEGRATED
EXP12_FEASIBILITY_FORENSIC_AUTHORIZATION_V01 = CANDIDATE / PENDING_EXTERNAL_AUDIT
FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```
