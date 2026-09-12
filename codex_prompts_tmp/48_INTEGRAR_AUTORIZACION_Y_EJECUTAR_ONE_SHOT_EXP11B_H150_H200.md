# PROMPT 48 — INTEGRAR AUTORIZACIÓN Y EJECUTAR ONE-SHOT EXP11B H150/H200

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque es la **ejecución científica oficial one-shot** de `EXP11B Retrieval H150/H200`.

Debes, en este orden:

1. integrar exactamente en `main` la autorización one-shot previamente auditada y aprobada externamente;
2. ejecutar **una sola vez** el runner oficial EXP11B v0.3 contra los 20 bancos H150/H200;
3. si la ejecución termina correctamente, validar la integridad de los outputs sin recalcular ni alterar resultados;
4. publicar un **candidato de resultados/evidencia**, sin integrarlo a `main`, para auditoría externa posterior.

No ejecutes EXP12, Grupo 2B, Grupo 3 ni ningún bloque posterior.

---

# 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt47 concluyó:

```text
PROMPT47_EXTERNAL_AUDIT = PASS / APPROVED
EXP11B_EXECUTION_PACKAGE_V03 = APPROVED / INTEGRATED_IN_MAIN
EXP11B_RETRIEVAL_AUTHORIZATION_V03 = APPROVED_FOR_INTEGRATION_AND_ONE_SHOT_EXECUTION
EXP11B_RETRIEVAL = NOT_YET_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Paquete científico integrado:

```text
main/package commit = 50d90a356a0fac0267c270568f3926430a246026
runner blob = 90bbeba27e4890613cb463fffc1cfc07252292c5
runner SHA256 = 32f495996b8f1486cc6ef5f3906e84eb417e480208a721fb8b1c3f6820e65e06
config blob = 08cc58f95b2d6989bf75e64b16c0d9aa8158f642
config SHA256 = 2b91c06762409d10478cbf112bb25486ef3ffa410e5819fb0704f61fe64aa6af
```

Autorización aprobada:

```text
branch = codex/exp11b-retrieval-authorization-v03
commit = ea4bc0bde3246b40a25453dabeef5d571cf7c021
parent = 50d90a356a0fac0267c270568f3926430a246026
path = outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.3.json
blob = 7a23c64857b8f28302be7ce75d1269cbe60cc25b
SHA256 = f9a9b468b3d856492dd6a272ad8cf73932dba91b02e34a42d715352f3dd45fd0
byte_length = 1440
```

La autorización contiene:

```text
authorization_id = EXP11B_H150_H200_AUTH_001
attempt_id = EXP11B_H150_H200_ATTEMPT_001
authorization_status = AUTHORIZED_ONE_SHOT
approved_package_commit = 50d90a356a0fac0267c270568f3926430a246026
expected_banks = 20
official_output_root = outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1
```

El campo histórico:

```text
authorization_candidate_status = PENDING_EXTERNAL_AUDIT_NOT_EFFECTIVE_ON_MAIN
```

refleja el estado del artefacto **cuando fue creado**. No lo edites ni reconstruyas. La decisión externa de Prompt47 y su integración exacta en `main` son las que vuelven efectiva la autorización. Debe preservarse la identidad exacta del candidato aprobado.

Los candidatos rechazados anteriores siguen siendo evidencia histórica inmutable y no deben integrarse:

```text
26b9e2bcf6dad74231f208f9137ffb0e39caf2e1 = DO_NOT_INTEGRATE
f5dddac0d296e74e5f92af3f863cbb3c74e757b9 = DO_NOT_INTEGRATE
```

---

# 2. Precondiciones Git obligatorias

Antes de cualquier integración o ejecución, ejecuta `git fetch` y verifica exactamente:

```text
origin/main = 50d90a356a0fac0267c270568f3926430a246026
origin/codex/exp11b-retrieval-authorization-v03 = ea4bc0bde3246b40a25453dabeef5d571cf7c021
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Verifica:

```text
ea4bc0bde3246b40a25453dabeef5d571cf7c021
  parent = 50d90a356a0fac0267c270568f3926430a246026
  commits_ahead_of_main = 1
  commits_behind_main = 0
  changed_path_count = 1
```

El único path del candidato debe ser:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.3.json
```

Verifica también que el blob y SHA-256 de la autorización son exactamente los aprobados.

Si cualquier referencia, parent, diff, blob o hash difiere:

```text
STOP / PRECONDITION_REF_OR_ARTIFACT_DRIFT
```

No corrijas ni reconstruyas automáticamente.

---

# 3. Precondiciones locales no consumidoras

Antes de integrar la autorización, verifica sin scoring:

```text
working_tree_clean = true
official_output_root_exists = false
specific_consumption_marker_exists = false
```

Marcador específico prohibido antes de la ejecución:

```text
outputs/audits/exp11b_retrieval_execution_attempts/
EXP11B_H150_H200_AUTH_001--EXP11B_H150_H200_ATTEMPT_001.json
```

Verifica también que no exista ningún sibling residual asociado al output oficial con forma:

```text
exp11b_historical_retrieval_h150_h200_v0.1.staging-*
exp11b_historical_retrieval_h150_h200_v0.1.failed-*
```

No rematerialices bancos y no ejecutes un retrieval de prueba H150/H200.

Si alguna de estas condiciones falla:

```text
STOP / PREEXECUTION_LOCAL_STATE_NOT_CLEAN
```

No integres la autorización y no ejecutes.

---

# 4. Fase A — integrar exactamente la autorización aprobada

Integra mediante **fast-forward exacto**:

```text
50d90a356a0fac0267c270568f3926430a246026
→
ea4bc0bde3246b40a25453dabeef5d571cf7c021
```

Usa `--ff-only`.

NO hagas:

- merge commit;
- squash;
- cherry-pick;
- rebase;
- amend;
- reconstrucción del JSON;
- modificación de ningún otro archivo.

Después del push exige:

```text
origin/main = ea4bc0bde3246b40a25453dabeef5d571cf7c021
```

No debe existir ningún commit adicional en `main`.

Desde este momento:

```text
EXP11B_RETRIEVAL_AUTHORIZATION = EFFECTIVE / ONE_SHOT / NOT_YET_CONSUMED
```

No modifiques Plan Maestro ni Article.

---

# 5. Fase B — comprobación inmediata previa a la única invocación

Ya sobre `main = ea4bc0...`, vuelve a comprobar:

```text
HEAD = ea4bc0bde3246b40a25453dabeef5d571cf7c021
working_tree_clean = true
official_output_root_exists = false
specific_consumption_marker_exists = false
runner_blob_at_HEAD = 90bbeba27e4890613cb463fffc1cfc07252292c5
config_blob_at_HEAD = 08cc58f95b2d6989bf75e64b16c0d9aa8158f642
authorization_blob_at_HEAD = 7a23c64857b8f28302be7ce75d1269cbe60cc25b
```

Registra:

```text
python_executable
python_version
platform
free_disk_bytes_on_output_filesystem
execution_started_at_utc
```

No instales ni actualices dependencias en este bloque.

Si aparece cualquier drift antes de invocar el runner:

```text
STOP / PREEXECUTION_DRIFT_AFTER_AUTH_INTEGRATION
```

La autorización seguirá integrada pero **no consumida**. No hagas retry ni fabriques otra autorización. Reporta y detente.

---

# 6. Fase C — única ejecución científica oficial

Ejecuta exactamente **una sola vez** el modo oficial del runner v0.3, desde la raíz del repositorio y usando el mismo entorno Python validado durante la preparación del paquete.

Invocación lógica obligatoria:

```text
python -m src.experiments.run_exp11b_historical_retrieval_h150_h200_v03 --execute-official
```

Puedes usar la ruta concreta del intérprete equivalente al `python` anterior, pero:

- no uses `--bank-dir`;
- no uses una ruta alternativa de autorización;
- no cambies `--config`;
- no llames primero a `--preflight` o `--self-test-h100`;
- no invoques una segunda vez `--execute-official` bajo ninguna circunstancia.

Debes registrar:

```text
official_execute_invocation_count = 1
exact_command
exit_code
stdout_capture
stderr_capture
execution_completed_at_utc
```

Los captures pueden ser temporales durante la ejecución, pero su SHA-256, tamaño y contenido relevante deben quedar resumidos en el execution record definido más adelante. No alteres los outputs científicos para incluirlos.

## Regla absoluta de no-retry

Sea cual sea el resultado de la invocación:

```text
NO SECOND OFFICIAL INVOCATION
NO RETRY
NO RESUME
NO OVERWRITE
NO PARTIAL RECOMPUTATION
```

---

# 7. Ruta de fallo de la ejecución oficial

Si `exit_code != 0` o el proceso termina de forma anómala:

1. **no vuelvas a ejecutar**;
2. determina si el marcador one-shot fue creado;
3. preserva cualquier `.failed-*`, failure ledger y staging transformado por el runner;
4. no borres ni reemplaces el marcador si existe;
5. no crees una nueva autorización;
6. no avances a EXP12.

Crea, sin modificar evidencia existente, un único registro:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/
exp11b_retrieval_attempt001_failure_record_v0.1.json
```

Debe incluir al menos:

```text
status = OFFICIAL_EXECUTION_FAILED_PENDING_EXTERNAL_AUDIT
authorization_id
attempt_id
execution_head
exact_command
official_execute_invocation_count = 1
exit_code
stdout_sha256 / size_bytes
stderr_sha256 / size_bytes
consumption_marker_exists
consumption_marker_sha256 si existe
failed_output_paths
hashes/sizes de failure evidence disponible
no_retry = true
EXP11B_RETRIEVAL = FAILED_ATTEMPT_PENDING_EXTERNAL_AUDIT
EXP12_authorized = false
```

Publícalo en una rama candidata creada desde `main = ea4bc0...`:

```text
codex/exp11b-retrieval-attempt001-failure-evidence-v01
```

Puedes versionar además el marcador y failure ledger si existen y tienen tamaño razonable. No modifiques sus bytes.

Después: `STOP`. No construyas candidato de éxito.

---

# 8. Ruta de éxito — validación de outputs oficiales

Solo si la invocación termina con `exit_code = 0`, valida **sin recalcular retrieval** el output root:

```text
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1
```

Debe contener exactamente los ocho artefactos contractuales:

```text
exp11b_retrieval_run_manifest_v0.1.json
exp11b_retrieval_metrics_by_bank_v0.1.csv
exp11b_retrieval_case_level_v0.1.csv
exp11b_retrieval_candidates_v0.1.csv
exp11b_retrieval_condition_summary_v0.1.csv
exp11b_retrieval_output_hashes_v0.1.csv
exp11b_retrieval_failures_v0.1.json
exp11b_retrieval_environment_v0.1.json
```

Debe existir además el marcador:

```text
outputs/audits/exp11b_retrieval_execution_attempts/
EXP11B_H150_H200_AUTH_001--EXP11B_H150_H200_ATTEMPT_001.json
```

Valida por lectura/streaming, sin modificar archivos:

```text
marker.status = CONSUMED_EXECUTION_STARTED
marker.authorization_id = EXP11B_H150_H200_AUTH_001
marker.attempt_id = EXP11B_H150_H200_ATTEMPT_001
marker.approved_package_commit = 50d90a356a0fac0267c270568f3926430a246026
marker.execution_head = ea4bc0bde3246b40a25453dabeef5d571cf7c021
```

### 8.1 Run manifest

Exige:

```text
experiment_id = EXP-11B
status = COMPLETED
retrieval_executed = true
evaluation_metrics_computed = true
run_count = 20
unique_bank_count = 20
H150_run_count = 10
H200_run_count = 10
all_run_status = COMPLETED
```

La autorización embebida debe conservar como mínimo:

```text
authorization_id = EXP11B_H150_H200_AUTH_001
attempt_id = EXP11B_H150_H200_ATTEMPT_001
approved_package_commit = 50d90a356a0fac0267c270568f3926430a246026
execution_head = ea4bc0bde3246b40a25453dabeef5d571cf7c021
authorization_git_blob = 7a23c64857b8f28302be7ce75d1269cbe60cc25b
authorization_sha256 = f9a9b468b3d856492dd6a272ad8cf73932dba91b02e34a42d715352f3dd45fd0
```

### 8.2 Metrics by bank

Exige:

```text
data_row_count = 20
unique_run_id_count = 20
unique_bank_id_count = 20
H150_rows = 10
H200_rows = 10
all_primary_n = 1056
```

No apliques ningún criterio de “resultado esperado”. No repitas ni cambies la corrida por valores altos, bajos o inesperados.

### 8.3 Case level

Exige:

```text
data_row_count = 20 * 1056 = 21120
unique_bank_id_count = 20
rows_per_bank = 1056 para cada banco
```

Valida headers contra el contrato congelado.

### 8.4 Candidate ranking

No cargues todo el archivo en memoria si es grande. Valídalo en streaming:

```text
header = contrato congelado
row_count > 0
unique_bank_id_count = 20
candidate_rank_min >= 1
candidate_rank_max <= 100
```

Registra `sha256` y `size_bytes` exactos.

### 8.5 Condition summary

Exige exactamente dos filas:

```text
H150: expected_runs = 10, completed_runs = 10, primary_n = 1056, status = COMPLETED
H200: expected_runs = 10, completed_runs = 10, primary_n = 1056, status = COMPLETED
```

Registra los valores observados de:

```text
top_1_mean
top_3_mean
top_5_mean
top_10_mean
top_50_mean
mrr_mean
```

sin interpretación metodológica adicional.

### 8.6 Failure ledger

Exige:

```text
status = NO_FAILURES
failure_stage = NONE
```

### 8.7 Environment

Exige que el `git_commit` observado sea:

```text
ea4bc0bde3246b40a25453dabeef5d571cf7c021
```

Registra Python, plataforma, paquetes y command.

### 8.8 Hash ledger

Debe contener exactamente siete filas, una por cada artefacto oficial distinto del propio ledger.

Recalcula SHA-256 y `size_bytes` de esos siete archivos y exige coincidencia exacta con el ledger.

Calcula además SHA-256 y tamaño del propio ledger.

### 8.9 Ausencia de residuos de fallo

Tras éxito exige:

```text
staging_sibling_count = 0
failed_sibling_count = 0
```

Verifica nuevamente, en modo read-only, que las identidades/hashes de los 20 bancos oficiales siguen coincidiendo con el contrato congelado.

---

# 9. Registro oficial de ejecución para auditoría

Solo tras una ejecución exitosa y las validaciones anteriores, crea:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/
exp11b_retrieval_official_execution_record_v0.1.json
```

Este archivo es **evidencia de ejecución**, no un nuevo resultado científico ni una reinterpretación.

Debe registrar al menos:

```text
artifact = EXP11B_RETRIEVAL_OFFICIAL_EXECUTION_RECORD
version = v0.1
status = CANDIDATE_OFFICIAL_EXECUTION_COMPLETED_PENDING_EXTERNAL_AUDIT
experiment_id = EXP-11B
scope = H150_H200_HISTORICAL_RETRIEVAL_ONLY
package_commit = 50d90a356a0fac0267c270568f3926430a246026
authorization_commit = ea4bc0bde3246b40a25453dabeef5d571cf7c021
authorization_blob = 7a23c64857b8f28302be7ce75d1269cbe60cc25b
authorization_sha256 = f9a9b468b3d856492dd6a272ad8cf73932dba91b02e34a42d715352f3dd45fd0
authorization_id = EXP11B_H150_H200_AUTH_001
attempt_id = EXP11B_H150_H200_ATTEMPT_001
execution_head = ea4bc0bde3246b40a25453dabeef5d571cf7c021
official_execute_invocation_count = 1
exact_command
exit_code = 0
execution_started_at_utc
execution_completed_at_utc
python_executable
python_version
platform
free_disk_bytes_before_execution
marker_path
marker_sha256
marker_size_bytes
marker_status = CONSUMED_EXECUTION_STARTED
official_output_root
output_artifacts: path + sha256 + size_bytes + row_count cuando aplique
metrics_by_bank_row_count = 20
case_level_row_count = 21120
candidate_ranking_row_count
condition_summary_row_count = 2
bank_identity_postcheck = PASS_EXACT_20_OF_20
stdout_sha256 / size_bytes
stderr_sha256 / size_bytes
retry_count = 0
resume_used = false
overwrite_used = false
partial_recomputation_used = false
EXP12_authorized = false
runtime_evidence_classification = CODEX_LOCAL_OFFICIAL_EXECUTION_EVIDENCE / PENDING_EXTERNAL_AUDIT
```

Incluye también los valores H150/H200 del condition summary como **observaciones brutas**, no como conclusión externa.

---

# 10. Candidato de resultados y política de artefactos grandes

No integres resultados directamente en `main`.

Crea desde:

```text
main = ea4bc0bde3246b40a25453dabeef5d571cf7c021
```

la rama:

```text
codex/exp11b-retrieval-h150-h200-results-v01
```

Versiona con `git add -f` los artefactos oficiales y de auditoría **sin modificar sus bytes**.

Como el repositorio ignora `outputs/` y GitHub impone límites por blob, antes de `git add` calcula el tamaño de cada artefacto.

Regla de transporte Git:

```text
MAX_SINGLE_GIT_ARTIFACT_BYTES = 90000000
```

Para cada artefacto oficial:

- si `size_bytes < 90000000`, versiónalo íntegramente;
- si `size_bytes >= 90000000`, **no** lo añadas a Git, no lo comprimas, no lo trocees y no lo reescribas; consérvalo localmente intacto y regístralo en `exp11b_retrieval_official_execution_record_v0.1.json` como:

```text
versioning_status = LOCAL_OFFICIAL_ARTIFACT_NOT_VERSIONED_DUE_TO_GIT_BLOB_LIMIT_GUARD
sha256 = <exacto>
size_bytes = <exacto>
```

Esta regla es únicamente de transporte/persistencia y **no afecta el cálculo científico**.

Siempre intenta versionar, si están por debajo del umbral:

```text
run manifest
metrics by bank
case level
candidate ranking
condition summary
output hash ledger
failure ledger
environment
```

Siempre versiona además:

```text
outputs/audits/exp11b_retrieval_execution_attempts/
EXP11B_H150_H200_AUTH_001--EXP11B_H150_H200_ATTEMPT_001.json

outputs/audits/exp11b_retrieval_execution_gate_v0.1/
exp11b_retrieval_official_execution_record_v0.1.json
```

El candidato de resultados debe contener **un único commit** sobre `ea4bc0...`.

No modifiques ningún archivo preexistente científico, config, autorización, Plan Maestro o Article en este candidato.

Reporta exactamente qué artefactos quedaron versionados y cuáles permanecieron local-only por el guard de tamaño.

---

# 11. Estado terminal permitido si la ejecución fue exitosa

Al final de Prompt48, el máximo estado permitido es:

```text
PROMPT48 = COMPLETED
EXP11B_RETRIEVAL_AUTHORIZATION = APPROVED / INTEGRATED / CONSUMED
EXP11B_RETRIEVAL_ATTEMPT_001 = EXECUTED_ONCE / COMPLETED / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL_RESULTS = CANDIDATE / NOT_INTEGRATED / PENDING_EXTERNAL_AUDIT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No declares:

```text
EXP11B = CLOSED
EXP11B_RESULTS = APPROVED
EXP12 = AUTHORIZED
```

Eso corresponde únicamente a la auditoría externa posterior.

---

# 12. Prohibiciones absolutas

NO:

- ejecutar una segunda vez `--execute-official`;
- ejecutar un retry aunque el primer intento falle antes o después del consumo;
- hacer resume;
- hacer overwrite;
- rematerializar bancos;
- modificar autorización, runner o config;
- modificar parámetros BM25;
- filtrar resultados por conveniencia;
- cambiar semillas;
- cambiar EVAL;
- cambiar el denominador 1056;
- borrar el marcador one-shot;
- borrar evidencia de fallo;
- promover outputs parciales a oficiales;
- integrar el candidato de resultados a `main`;
- modificar Plan Maestro;
- modificar Article;
- ejecutar EXP12;
- iniciar Grupo 2B o Grupo 3.

---

# 13. Persistencia administrativa

Después de completar la ruta de éxito o fallo:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch`;
3. no hagas rebase/amend/force;
4. crea únicamente:

```text
codex_prompts_tmp/48_RESPUESTA_INTEGRAR_AUTORIZACION_Y_EJECUTAR_ONE_SHOT_EXP11B_H150_H200.md
```

El commit administrativo debe contener solo esa respuesta.

---

# 14. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT48 = COMPLETED | STOP

main_initial
main_after_authorization_integration
authorization_integration_mode
authorization_commit
authorization_blob
authorization_sha256

preexecution_output_root_exists
preexecution_specific_marker_exists
preexecution_residual_staging_count
preexecution_residual_failed_count

python_executable
python_version
platform
free_disk_bytes_before_execution
exact_command
official_execute_invocation_count
execution_started_at_utc
execution_completed_at_utc
exit_code
stdout_sha256
stderr_sha256

authorization_consumed
consumption_marker_path
consumption_marker_sha256
consumption_marker_status

OFFICIAL_OUTPUT_ROOT_EXISTS
output_file_count
run_manifest_status
run_count
metrics_by_bank_row_count
case_level_row_count
candidate_ranking_row_count
condition_summary_row_count
hash_ledger_row_count
failure_ledger_status
environment_git_commit
bank_identity_postcheck
staging_sibling_count
failed_sibling_count

H150_top_1_mean
H150_top_3_mean
H150_top_5_mean
H150_top_10_mean
H150_top_50_mean
H150_mrr_mean
H200_top_1_mean
H200_top_3_mean
H200_top_5_mean
H200_top_10_mean
H200_top_50_mean
H200_mrr_mean

execution_record_path
execution_record_sha256

RESULT_CANDIDATE_BRANCH
RESULT_CANDIDATE_COMMIT
RESULT_CANDIDATE_PARENT
RESULT_CANDIDATE_TREE
RESULT_CANDIDATE_CHANGED_PATH_COUNT
versioned_artifacts
local_only_large_artifacts

plan_head_final
article_head_final
EXP12_authorized
EXP12_executed
```

Si hubo fallo, sustituye la sección de resultados por los campos del failure record y detente.

No declares auditoría externa PASS. Solo IA Experimental puede aprobar o rechazar los resultados oficiales.
