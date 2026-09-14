# PROMPT 66 — CORREGIR COLISIÓN DE RUTAS EN AUTORIZACIÓN FORENSE EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque corrige exclusivamente un defecto pre-ejecución detectado por auditoría externa en el candidato de autorización forense generado por Prompt65. El diseño forense v0.1 ya integrado a `main` permanece científicamente válido; el defecto está en la **orquestación futura del marcador de consumo respecto del directorio de salida**.

Este bloque:

1. verifica el hallazgo de forma estática, sin ejecutar el diagnóstico oficial;
2. declara rechazado y no integrable el candidato de autorización v0.1;
3. crea un candidato de autorización v0.2 con un marcador de consumo fuera del directorio reservado de salida;
4. conserva intactos módulo, protocolo, tests, datos, thresholds, seed y comando diagnóstico.

Este bloque **NO ejecuta** `--execute-forensic-diagnostic`, NO recomputa el seed oficial, NO ejecuta planning, NO prueba otros seeds/thresholds, NO ejecuta retrieval/BM25/Top-k/MRR y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt65 concluye:

```text
PROMPT65_EXTERNAL_AUDIT = PARTIAL_PASS / AUTHORIZATION_V01_REJECTED_PREEXECUTION

EXP12_FEASIBILITY_FORENSIC_DESIGN_V01 = INTEGRATED / VERIFIED
FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false

EXP12-FOR-F001 = PREEXECUTION_MARKER_OUTPUT_PARENT_COLLISION / BLOCKING
EXP12_FEASIBILITY_FORENSIC_AUTHORIZATION_V01 = REJECTED / DO_NOT_INTEGRATE
```

Hallazgo exacto:

```text
output_path = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
v01_consumption_marker_path = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_forensic_attempt_001_consumption_marker.json
```

Ambos tienen el mismo directorio padre:

```text
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic
```

La semántica de ejecución congelada en Prompt65 exige crear el marcador **antes** de la única invocación. Sin embargo, el módulo integrado contiene en la ruta de éxito:

```python
output_path.parent.mkdir(parents=True, exist_ok=False)
```

Por ello, crear primero el marcador materializa el directorio padre y una ejecución que llegue a la escritura de salida fallaría al intentar crear de nuevo ese directorio con `exist_ok=False`.

Este defecto es técnico/procedimental, fue detectado **antes de cualquier ejecución forense oficial**, no altera el Attempt001 histórico ni requiere modificar el algoritmo diagnóstico.

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 79fc10d161c735a5d727e36ed65554a89f937e3b
origin/codex/exp12-feasibility-forensic-authorization-v01 = 2ab9426002222d70aa800d191ddd170d19bde8ab
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para v0.1 exige:

```text
parent = 79fc10d161c735a5d727e36ed65554a89f937e3b
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.1.json
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

No integres v0.1 a `main`.

---

## 3. Verificación estática obligatoria del hallazgo

Desde un checkout limpio de `main=79fc10d...`, lee sin ejecutar:

```text
src/experiments/diagnose_exp12_feasibility_failure_v01.py
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.1.json
```

Confirma exactamente:

```text
V01_OUTPUT_PARENT = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic
V01_MARKER_PARENT = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic
V01_OUTPUT_PARENT_EQUALS_MARKER_PARENT = true
MODULE_OUTPUT_PARENT_MKDIR_EXIST_OK = false
MARKER_REQUIRED_BEFORE_INVOCATION = true
EXP12-FOR-F001 = VERIFIED
```

No ejecutes el módulo ni sus funciones sobre datos oficiales para demostrar el hallazgo.

---

## 4. Candidato correctivo de autorización v0.2

Desde exactamente:

```text
79fc10d161c735a5d727e36ed65554a89f937e3b
```

crea la rama:

```text
codex/exp12-feasibility-forensic-authorization-v02
```

Crea un solo commit que añada exclusivamente:

```text
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.2.json
```

No modifiques v0.1, módulo, protocolo, tests, config, datos, Plan ni Article.

### 4.1 Identidad y trazabilidad

El nuevo JSON debe incluir como mínimo:

```text
artifact = EXP12_FEASIBILITY_FORENSIC_EXECUTION_AUTHORIZATION
version = v0.2
authorization_id = EXP12_FORENSIC_AUTH_002
diagnostic_attempt_id = EXP12_FORENSIC_ATTEMPT_001
status = AUTHORIZED_ONE_SHOT_FORENSIC_DIAGNOSTIC
scope = NON_GOVERNING_RECONSTRUCTION_SEED_20262001_10000_INDICES_AGGREGATE_ONLY

supersedes_candidate_authorization = EXP12_FORENSIC_AUTH_001
superseded_candidate_commit = 2ab9426002222d70aa800d191ddd170d19bde8ab
superseded_candidate_status = REJECTED_PREEXECUTION_NOT_INTEGRATED
supersession_reason = PREEXECUTION_MARKER_OUTPUT_PARENT_COLLISION

effective_only_if_external_audit_passes = true
effective_only_if_integrated_to_main = true
authorization_effective_in_candidate_branch = false
single_use = true
retry_allowed = false
resume_allowed = false
overwrite_allowed = false
partial_recomputation_allowed = false
```

La autorización histórica de planning debe permanecer:

```text
historical_planning_authorization_id = EXP12_PLANNING_AUTH_001
historical_planning_attempt_id = EXP12_PLANNING_ATTEMPT_001
historical_planning_attempt_status = FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED
historical_planning_retry_remains_prohibited = true
```

### 4.2 Bindings científicos/técnicos sin cambio

Conserva exactamente los mismos bindings aprobados de v0.1:

```text
diagnostic_design_commit = 79fc10d161c735a5d727e36ed65554a89f937e3b
scientific_base_commit = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
forensic_protocol_path = docs/exp12_feasibility_failure_forensic_protocol_v0.1.md
forensic_protocol_sha256 = 2c5079609acead65621598f05f413282ef15c6e1d94ae51c47363d826fad7891
diagnostic_module_path = src/experiments/diagnose_exp12_feasibility_failure_v01.py
diagnostic_module_sha256 = 8d5ab67d79e994c94055ba58bf22d12b1a35e053eb465c5aece9b8f540d0ff4c
forensic_test_path = tests/test_exp12_feasibility_failure_diagnostic_v01.py
forensic_test_sha256 = 5be6fe4f49ebfd6f005cb2286adc3662e8d0c9d03395b57ecd6e22efaa3a9411

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
```

### 4.3 Corrección única de orquestación

Mantén la salida exactamente en:

```text
output_path = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
```

Pero cambia el marcador futuro a un path cuyo padre NO sea el padre del output:

```text
consumption_marker_path = outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_consumption_marker.json
```

Registra expresamente:

```text
output_parent = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic
marker_parent = outputs/audits/exp12_planning_gate_v0.4
marker_parent_equals_output_parent = false
output_parent_must_be_absent_immediately_before_invocation = true
no_preinvocation_files_under_output_parent = true
stdout_stderr_capture_must_not_create_output_parent = true
```

El comando lógico diagnóstico debe permanecer **byte-semánticamente igual** al de v0.1; no cambies ninguno de sus argumentos.

### 4.4 Semántica futura one-shot

El futuro ejecutor, solo después de nueva aprobación externa e integración, deberá:

1. verificar refs, bindings y working tree limpio;
2. exigir que `output_path` y `output_parent` no existan antes del consumo;
3. exigir que el marcador v0.2 tampoco exista;
4. crear el marcador v0.2 fuera de `output_parent` inmediatamente antes de la invocación;
5. **no crear ningún archivo/directorio dentro de `output_parent` antes de lanzar el módulo**;
6. capturar stdout/stderr sin materializar archivos dentro de `output_parent` antes de la invocación;
7. ejecutar exactamente una invocación del comando congelado;
8. no reintentar, reanudar, sobrescribir ni recomputar parcialmente;
9. después de finalizar, versionar marcador, logs, reporte y salida si existe;
10. mantener el resultado como diagnóstico no gobernante y someterlo a auditoría externa antes de cualquier decisión posterior.

---

## 5. Verificaciones correctivas sin diagnóstico oficial

Antes de publicar v0.2 verifica:

```text
V02_OUTPUT_PARENT = outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic
V02_MARKER_PARENT = outputs/audits/exp12_planning_gate_v0.4
V02_OUTPUT_PARENT_EQUALS_MARKER_PARENT = false
```

En checkout limpio confirma también:

```text
FORENSIC_OUTPUT_EXISTS = false
FORENSIC_OUTPUT_TRACKED = false
FORENSIC_OUTPUT_UNTRACKED = false
FORENSIC_OUTPUT_PARENT_EXISTS = false
V02_CONSUMPTION_MARKER_EXISTS = false
V02_CONSUMPTION_MARKER_TRACKED = false
V02_CONSUMPTION_MARKER_UNTRACKED = false
```

No borres ni renombres nada para satisfacer estas condiciones.

No necesitas volver a ejecutar los 14 tests si los hashes de módulo/tests permanecen exactos; puedes verificar sus hashes y registrar que no fueron modificados. No ejecutes datos oficiales.

---

## 6. Prohibiciones absolutas

Durante Prompt66 NO:

- integres la autorización v0.1;
- integres la autorización v0.2;
- ejecutes `--execute-forensic-diagnostic`;
- ejecutes funciones diagnósticas sobre el pool oficial;
- recomputes el seed 20262001;
- pruebes otros seeds o thresholds;
- modifiques módulo/protocolo/tests/config/datos;
- cambies candidate_count, volumen, coverage, TVD o minimum feasible;
- selecciones condiciones;
- ejecutes planning/retrieval/BM25/Top-k/MRR;
- modifiques Plan o Article;
- avances a Grupo 2B o Grupo 3.

---

## 7. Verificaciones finales

Exige:

```text
origin/main = 79fc10d161c735a5d727e36ed65554a89f937e3b
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/exp12-feasibility-forensic-authorization-v01 = 2ab9426002222d70aa800d191ddd170d19bde8ab
```

Para v0.2 exige:

```text
parent = 79fc10d161c735a5d727e36ed65554a89f937e3b
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_execution_authorization_v0.2.json
```

Y confirma:

```text
EXP12_FORENSIC_AUTH_001 = REJECTED_PREEXECUTION_NOT_INTEGRATED
EXP12_FORENSIC_AUTH_002 = CANDIDATE / PENDING_EXTERNAL_AUDIT
FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 8. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/66_RESPUESTA_CORREGIR_COLISION_RUTAS_AUTORIZACION_FORENSE_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 9. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT66 = COMPLETED | STOP

main_final
plan_final
article_final

EXP12-FOR-F001
V01_OUTPUT_PARENT
V01_MARKER_PARENT
V01_OUTPUT_PARENT_EQUALS_MARKER_PARENT
MODULE_OUTPUT_PARENT_MKDIR_EXIST_OK
EXP12_FORENSIC_AUTH_001_STATUS

AUTHORIZATION_V02_BRANCH
AUTHORIZATION_V02_COMMIT
AUTHORIZATION_V02_PARENT
AUTHORIZATION_V02_COMMITS_AHEAD
AUTHORIZATION_V02_COMMITS_BEHIND
AUTHORIZATION_V02_CHANGED_PATH_COUNT
AUTHORIZATION_V02_CHANGED_PATH
AUTHORIZATION_V02_PUBLISHED
AUTHORIZATION_V02_ID
DIAGNOSTIC_ATTEMPT_ID

V02_OUTPUT_PARENT
V02_MARKER_PARENT
V02_OUTPUT_PARENT_EQUALS_MARKER_PARENT
FORENSIC_OUTPUT_PARENT_EXISTS
V02_CONSUMPTION_MARKER_EXISTS

FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT66 = COMPLETED
EXP12-FOR-F001 = VERIFIED / CORRECTED_IN_AUTHORIZATION_V02_CANDIDATE
EXP12_FORENSIC_AUTH_001 = REJECTED_PREEXECUTION_NOT_INTEGRATED
EXP12_FORENSIC_AUTH_002 = CANDIDATE / PENDING_EXTERNAL_AUDIT
FORENSIC_POOL_EXECUTION_PERFORMED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```
