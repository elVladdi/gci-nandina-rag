# PROMPT 67 — INTEGRAR AUTORIZACIÓN v0.2 Y EJECUTAR ONE-SHOT DIAGNÓSTICO FORENSE EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto la autorización forense v0.2 ya auditada externamente;
2. ejecutar un preflight final en checkout aislado y limpio;
3. consumir la autorización mediante un marcador situado **fuera del directorio reservado de output**;
4. ejecutar **exactamente una vez** el diagnóstico forense no gobernante del seed `20262001` sobre los 10,000 índices congelados;
5. preservar y versionar marcador, logs, reporte y salida diagnóstica —si existe— para auditoría externa.

Este bloque **NO reintenta ni reanuda el planning histórico**, NO ejecuta un nuevo planning oficial, NO prueba otros seeds, NO prueba thresholds alternativos, NO selecciona D-HIGH/D-MID/D-LOW, NO ejecuta retrieval/BM25/Top-k/MRR y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt66 concluye:

```text
PROMPT66_EXTERNAL_AUDIT = PASS / APPROVED
EXP12-FOR-F001 = VERIFIED / CORRECTED_IN_AUTHORIZATION_V02_CANDIDATE
EXP12_FORENSIC_AUTH_001 = REJECTED_PREEXECUTION_NOT_INTEGRATED
EXP12_FORENSIC_AUTH_002 = APPROVED_FOR_INTEGRATION_AND_ONE_SHOT_FORENSIC_DIAGNOSTIC
FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato aprobado:

```text
branch = codex/exp12-feasibility-forensic-authorization-v02
commit = d9431e71c363d9d6d372e8476d4f2c071dc905b7
parent = 79fc10d161c735a5d727e36ed65554a89f937e3b
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.2.json
```

Autorización:

```text
authorization_id = EXP12_FORENSIC_AUTH_002
diagnostic_attempt_id = EXP12_FORENSIC_ATTEMPT_001
status = AUTHORIZED_ONE_SHOT_FORENSIC_DIAGNOSTIC
scope = NON_GOVERNING_RECONSTRUCTION_SEED_20262001_10000_INDICES_AGGREGATE_ONLY
single_use = true
retry_allowed = false
resume_allowed = false
overwrite_allowed = false
partial_recomputation_allowed = false
```

La autorización v0.1 `EXP12_FORENSIC_AUTH_001` permanece rechazada pre-ejecución, nunca integrada y nunca consumida.

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 79fc10d161c735a5d727e36ed65554a89f937e3b
origin/codex/exp12-feasibility-forensic-authorization-v02 = d9431e71c363d9d6d372e8476d4f2c071dc905b7
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para la autorización v0.2 exige:

```text
parent = 79fc10d161c735a5d727e36ed65554a89f937e3b
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.2.json
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta de autorización v0.2

Integra exclusivamente:

```text
79fc10d161c735a5d727e36ed65554a89f937e3b
→
d9431e71c363d9d6d372e8476d4f2c071dc905b7
```

mediante fast-forward exacto de `main`.

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/main = d9431e71c363d9d6d372e8476d4f2c071dc905b7
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 4. Fase B — checkout aislado y preflight final

Ejecuta desde un checkout/worktree nuevo, aislado y limpio del commit exacto:

```text
d9431e71c363d9d6d372e8476d4f2c071dc905b7
```

Exige:

```text
TRACKED_WORKING_TREE_CLEAN = true
```

### 4.1 Identidades congeladas

Verifica por SHA-256 canónico Git/LF cuando corresponda:

```text
forensic_protocol = docs/exp12_feasibility_failure_forensic_protocol_v0.1.md
sha256 = 2c5079609acead65621598f05f413282ef15c6e1d94ae51c47363d826fad7891

diagnostic_module = src/experiments/diagnose_exp12_feasibility_failure_v01.py
sha256 = 8d5ab67d79e994c94055ba58bf22d12b1a35e053eb465c5aece9b8f540d0ff4c

test = tests/test_exp12_feasibility_failure_diagnostic_v01.py
sha256 = 5be6fe4f49ebfd6f005cb2286adc3662e8d0c9d03395b57ecd6e22efaa3a9411

readiness = outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_design_readiness_v0.1.json
sha256 = 7ba3b7023d0c9830e02742322ef9bac01ad0bf70e838b8d0761ce87e4ed79d08

config = src/configs/exp12_historical_diversity_control_v0.5.json
sha256 = 1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264

runner = src/experiments/plan_exp12_historical_diversity_v01.py
sha256 = cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac

sampling_universe = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457

H100 = data/processed/data_aduanas_historico_clase87_v0.2.csv
sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff

EVAL = data/processed/data_aduanas_evalset_clase87_v0.2.csv
sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

No leas NANDINA, descripciones ni performance de EVAL; su uso durante el diagnóstico permanece limitado a `DECLARACION` para overlap mediante el módulo versionado.

### 4.2 Contrato de autorización

Lee íntegramente:

```text
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.2.json
```

y exige, entre otros:

```text
authorization_id = EXP12_FORENSIC_AUTH_002
diagnostic_attempt_id = EXP12_FORENSIC_ATTEMPT_001
authorization_effective_in_candidate_branch = false
effective_only_if_external_audit_passes = true
effective_only_if_integrated_to_main = true
single_use = true
retry_allowed = false
resume_allowed = false
overwrite_allowed = false
partial_recomputation_allowed = false
historical_planning_retry_remains_prohibited = true
forensic_non_governing = true
seed = 20262001
candidate_count = 10000
target_rows = 2950
volume_range = [2802,3098]
required_label_coverage_fraction = 1.0
maximum_tvd = 0.05
minimum_required_unique_feasible = 30
other_seeds_allowed = false
alternative_thresholds_allowed = false
condition_selection_allowed = false
```

### 4.3 Fail-closed del CLI

Antes de consumir la autorización, invoca el módulo **sin** `--execute-forensic-diagnostic` y exige:

```text
return_code = 2
status = NOT_EXECUTED
```

No suministres la bandera en esta comprobación.

### 4.4 Pristine state inmediatamente antes del consumo

Ruta de output reservada:

```text
OUTPUT = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
OUTPUT_PARENT = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic
```

Marcador v0.2:

```text
MARKER = outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_consumption_marker.json
```

Exige inmediatamente antes de consumir:

```text
OUTPUT_EXISTS = false
OUTPUT_TRACKED = false
OUTPUT_UNTRACKED = false
OUTPUT_PARENT_EXISTS = false
OUTPUT_PARENT_TRACKED = false
OUTPUT_PARENT_UNTRACKED = false
MARKER_EXISTS = false
MARKER_TRACKED = false
MARKER_UNTRACKED = false
```

No borres, renombres ni sobrescribas nada para hacer pasar este gate.

No crees stdout, stderr, reporte, temporales ni ningún otro archivo bajo `OUTPUT_PARENT` antes de la invocación.

---

## 5. Fase C — consumo one-shot de autorización forense

Solo si todo §4 pasa, crea **inmediatamente antes de la invocación**:

```text
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_consumption_marker.json
```

El marcador debe incluir como mínimo:

```text
artifact = EXP12_FEASIBILITY_FORENSIC_CONSUMPTION_MARKER
version = v0.2
authorization_id = EXP12_FORENSIC_AUTH_002
diagnostic_attempt_id = EXP12_FORENSIC_ATTEMPT_001
status = CONSUMED_EXECUTION_STARTED
authorization_commit = d9431e71c363d9d6d372e8476d4f2c071dc905b7
diagnostic_design_commit = 79fc10d161c735a5d727e36ed65554a89f937e3b
scientific_base_commit = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
consumed_at_utc = <UTC timestamp>
logical_command = <exact command §6>
retry_allowed = false
resume_allowed = false
overwrite_allowed = false
partial_recomputation_allowed = false
forensic_non_governing = true
```

Después de crear el marcador, la autorización queda consumida aunque la ejecución falle.

Vuelve a comprobar que:

```text
OUTPUT_PARENT_EXISTS = false
```

antes de lanzar el proceso. Si el marcador provocó de cualquier forma la creación de `OUTPUT_PARENT`, detente sin invocar y registra el estado como autorización consumida / ejecución no iniciada. No borres nada.

---

## 6. Fase D — única invocación diagnóstica autorizada

Ejecuta **exactamente una vez**:

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

Registra:

```text
EXECUTION_START_UTC
EXECUTION_END_UTC
RUNTIME_PYTHON_PATH
RUNTIME_PYTHON_VERSION
EXIT_CODE
STDOUT
STDERR
```

**No captures stdout/stderr creando archivos dentro de `OUTPUT_PARENT` antes o durante el arranque.** Captúralos en memoria o en una ubicación temporal externa al repositorio/worktree y materializa los logs versionables únicamente después de que la única invocación haya terminado.

No ejecutes una segunda invocación bajo ninguna circunstancia.

Si hay error, excepción, timeout, interrupción o salida no cero:

```text
EXP12_FORENSIC_ATTEMPT_001 = FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED
```

No reintentes, no reanudes y no reconstruyas resultados.

Si termina con código 0:

```text
EXP12_FORENSIC_ATTEMPT_001 = COMPLETED_ONE_SHOT / PENDING_EXTERNAL_AUDIT
```

---

## 7. Fase E — verificación post-ejecución sin recomputación

No vuelvas a ejecutar ninguna función diagnóstica ni candidate generation.

### 7.1 En caso de éxito

Exige exactamente:

```text
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
```

Lee únicamente esa salida y verifica estáticamente:

```text
artifact = EXP12_FEASIBILITY_FAILURE_DIAGNOSTIC
version = v0.1
status = NON_GOVERNING_FORENSIC_RESULT
forensic_non_governing = true
seed = 20262001
candidate_count = 10000
condition_selection_performed = false
retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
```

Y los invariantes:

```text
candidate_indices_attempted = 10000
candidate_indices_attempted = duplicate_dam_set_rejections + eval_overlap_rejections + unique_nonoverlap_candidates
unique_nonoverlap_candidates = volume_below_min_count + volume_within_range_count + volume_above_max_count
volume_within_range_count = coverage_and_tvd_pass_count + coverage_pass_tvd_fail_count + coverage_fail_tvd_pass_count + coverage_and_tvd_fail_count
volume_within_range_count = coverage_pass_count_among_volume_pass + coverage_fail_count_among_volume_pass
volume_within_range_count = tvd_pass_count_among_volume_pass + tvd_fail_count_among_volume_pass
final_unique_feasible_count = coverage_and_tvd_pass_count
minimum_required_unique_feasible = 30
historical_failure_condition_reproduced = (final_unique_feasible_count < 30)
```

No interpretes todavía causalidad ni propongas cambios metodológicos. Reporta únicamente los agregados persistidos.

Confirma también que la salida no contenga listas de DAM candidatas, rankings, selección D-HIGH/D-MID/D-LOW, recomendaciones de thresholds, métricas de retrieval ni métricas EVAL.

### 7.2 En caso de fallo

Preserva exactamente cualquier estado existente. No borres `OUTPUT_PARENT`, el output parcial ni el marcador. No intentes completar la salida manualmente.

---

## 8. Evidencia y versionado

Después de terminar la única invocación, crea fuera de `OUTPUT_PARENT`:

```text
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_stdout.log
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_stderr.log
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_execution_report_v0.1.json
```

El reporte debe contener como mínimo:

- identidad de autorización y attempt;
- commits de autorización, diseño y base científica;
- timestamps y runtime Python;
- comando lógico exacto;
- exit code y estado terminal;
- SHA-256 de marcador, stdout, stderr y output si existe;
- resultados de preflight;
- agregados persistidos en output si existe, sin recomputación;
- `retry_executed=false`;
- `resume_executed=false`;
- `overwrite_executed=false`;
- `partial_recomputation_executed=false`;
- `planning_reexecuted=false`;
- `other_seeds_tested=false`;
- `alternative_thresholds_tested=false`;
- `condition_selection_performed=false`;
- `retrieval_executed=false`;
- `bm25_executed=false`;
- `top_k_computed=false`;
- `mrr_computed=false`;
- `exp12_retrieval_authorized=false`.

Desde exactamente:

```text
d9431e71c363d9d6d372e8476d4f2c071dc905b7
```

crea una rama nueva:

```text
codex/exp12-feasibility-forensic-attempt001-evidence-v01
```

Un solo commit de evidencia. Puede añadir exclusivamente:

```text
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_consumption_marker.json
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_stdout.log
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_stderr.log
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_execution_report_v0.1.json
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
```

El último path se incluye solo si fue creado por la única invocación.

No modifiques código, protocolo, config, tests, datasets, Plan ni Article. Publica la rama para auditoría externa. **No la integres a main.**

---

## 9. Prohibiciones absolutas

Durante Prompt67 NO:

- integres la autorización v0.1 rechazada;
- ejecutes más de una invocación con `--execute-forensic-diagnostic`;
- reintentes o reanudes tras cualquier fallo;
- ejecutes `generate_exp12_candidates` directamente;
- ejecutes un nuevo planning oficial;
- pruebes otros seeds;
- pruebes thresholds alternativos;
- cambies candidate_count, minimum feasible, volumen, coverage o TVD;
- selecciones D-HIGH/D-MID/D-LOW;
- modifiques módulo/protocolo/config/tests/datasets;
- uses resultados forenses para cambiar retrospectivamente Attempt001;
- ejecutes retrieval/BM25/Top-k/MRR;
- leas labels/descripciones/performance EVAL fuera del módulo congelado;
- autorices retrieval EXP12;
- modifiques Plan o Article;
- avances a Grupo 2B o Grupo 3.

---

## 10. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/67_RESPUESTA_INTEGRAR_AUTORIZACION_V02_Y_EJECUTAR_ONE_SHOT_DIAGNOSTICO_FORENSE_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 11. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT67 = COMPLETED | FAILED_ONE_SHOT | STOP

main_initial
main_final
plan_final
article_final

AUTHORIZATION_V02_INTEGRATED
AUTHORIZATION_ID
DIAGNOSTIC_ATTEMPT_ID
AUTHORIZATION_CONSUMED
CONSUMPTION_MARKER_PATH

PREFLIGHT_TRACKED_WORKING_TREE_CLEAN
PREFLIGHT_BINDINGS
PREFLIGHT_CLI_FAIL_CLOSED
PREFLIGHT_OUTPUT_PRISTINE
PREFLIGHT_OUTPUT_PARENT_PRISTINE
PREFLIGHT_MARKER_PRISTINE

EXECUTION_START_UTC
EXECUTION_END_UTC
RUNTIME_PYTHON_PATH
RUNTIME_PYTHON_VERSION
OFFICIAL_FORENSIC_INVOCATION_COUNT
EXIT_CODE
TERMINAL_STATUS

EVIDENCE_BRANCH
EVIDENCE_COMMIT
EVIDENCE_PARENT
EVIDENCE_CHANGED_PATHS
EVIDENCE_PUBLISHED

FORENSIC_OUTPUT_CREATED
FORENSIC_OUTPUT_SHA256
CANDIDATE_INDICES_ATTEMPTED
DUPLICATE_DAM_SET_REJECTIONS
EVAL_OVERLAP_REJECTIONS
UNIQUE_NONOVERLAP_CANDIDATES
VOLUME_BELOW_MIN_COUNT
VOLUME_WITHIN_RANGE_COUNT
VOLUME_ABOVE_MAX_COUNT
COVERAGE_PASS_COUNT_AMONG_VOLUME_PASS
COVERAGE_FAIL_COUNT_AMONG_VOLUME_PASS
TVD_PASS_COUNT_AMONG_VOLUME_PASS
TVD_FAIL_COUNT_AMONG_VOLUME_PASS
COVERAGE_AND_TVD_PASS_COUNT
COVERAGE_PASS_TVD_FAIL_COUNT
COVERAGE_FAIL_TVD_PASS_COUNT
COVERAGE_AND_TVD_FAIL_COUNT
FINAL_UNIQUE_FEASIBLE_COUNT
MINIMUM_REQUIRED_UNIQUE_FEASIBLE
HISTORICAL_FAILURE_CONDITION_REPRODUCED

RETRY_EXECUTED = false
RESUME_EXECUTED = false
OVERWRITE_EXECUTED = false
PARTIAL_RECOMPUTATION_EXECUTED = false
EXP12_PLANNING_REEXECUTED = false
OTHER_SEEDS_TESTED = false
ALTERNATIVE_THRESHOLDS_TESTED = false
CONDITION_SELECTION_PERFORMED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Si la invocación falla y no existe output, reporta los agregados como `NOT_AVAILABLE_WITHOUT_RECOMPUTATION` y no los reconstruyas.

Respuesta terminal máxima:

```text
PROMPT67 = COMPLETED | FAILED_ONE_SHOT
EXP12_FORENSIC_ATTEMPT_001 = COMPLETED_ONE_SHOT_PENDING_EXTERNAL_AUDIT | FAILED_ONE_SHOT_AUTHORIZATION_CONSUMED
OFFICIAL_FORENSIC_INVOCATION_COUNT = 1
NO_RETRY = true
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```
