# RESPUESTA PROMPT 48 — INTEGRAR AUTORIZACIÓN Y EJECUTAR ONE-SHOT EXP11B H150/H200

```makefile
PROMPT48 = COMPLETED
EXP11B_RETRIEVAL_AUTHORIZATION = APPROVED / INTEGRATED / CONSUMED
EXP11B_RETRIEVAL_ATTEMPT_001 = EXECUTED_ONCE / COMPLETED / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL_RESULTS = CANDIDATE / NOT_INTEGRATED / PENDING_EXTERNAL_AUDIT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## 1. Integración de autorización

```makefile
main_initial = 50d90a356a0fac0267c270568f3926430a246026
origin_main_initial = 50d90a356a0fac0267c270568f3926430a246026
main_after_authorization_integration = ea4bc0bde3246b40a25453dabeef5d571cf7c021
origin_main_after_authorization_integration = ea4bc0bde3246b40a25453dabeef5d571cf7c021
authorization_integration_mode = FAST_FORWARD_EXACT
authorization_commit = ea4bc0bde3246b40a25453dabeef5d571cf7c021
authorization_parent = 50d90a356a0fac0267c270568f3926430a246026
authorization_blob = 7a23c64857b8f28302be7ce75d1269cbe60cc25b
authorization_sha256 = f9a9b468b3d856492dd6a272ad8cf73932dba91b02e34a42d715352f3dd45fd0
authorization_size_bytes = 1440
authorization_changed_path_count = 1
additional_commit_on_main = false
```

La autorización se integró mediante `git merge --ff-only`. No hubo merge commit, squash, cherry-pick, rebase, amend, reconstrucción ni modificación del JSON aprobado.

## 2. Precondiciones locales

```makefile
working_tree_tracked_clean = true
preexecution_output_root_exists = false
preexecution_specific_marker_exists = false
preexecution_residual_staging_count = 0
preexecution_residual_failed_count = 0
canonical_bank_csv_count = 20
runner_blob_at_HEAD = 90bbeba27e4890613cb463fffc1cfc07252292c5
config_blob_at_HEAD = 08cc58f95b2d6989bf75e64b16c0d9aa8158f642
authorization_blob_at_HEAD = 7a23c64857b8f28302be7ce75d1269cbe60cc25b
```

Solo estaban presentes los tres untracked históricos permitidos: `Referencias/Antecedentes/`, `Referencias/Glosario/` y `data/Series - Descripciones.xlsx`. No participaron en la ejecución ni en ningún commit.

## 3. Única invocación oficial

```makefile
python_executable = C:\Users\Vladimir\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
python_version = 3.12.14
platform = Windows-11-10.0.26200-SP0
free_disk_bytes_before_execution = 456541753344
exact_command = C:\Users\Vladimir\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m src.experiments.run_exp11b_historical_retrieval_h150_h200_v03 --execute-official
official_execute_invocation_count = 1
execution_started_at_utc = 2026-09-12T21:36:59.5137212Z
execution_completed_at_utc = 2026-09-12T21:40:22.6301415Z
exit_code = 0
stdout_sha256 = 35e6d5235df6ad7b14be1a2195c9c2a03e26e307117b2cb772d8ce96cfecb00d
stdout_size_bytes = 467
stderr_sha256 = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_size_bytes = 0
retry_count = 0
resume_used = false
overwrite_used = false
partial_recomputation_used = false
```

Resumen relevante del stdout: `status=COMPLETED`, `authorization_consumed=true`, `bank_count=20`. No se realizó una segunda invocación.

## 4. Consumo one-shot

```makefile
authorization_consumed = true
consumption_marker_path = outputs/audits/exp11b_retrieval_execution_attempts/EXP11B_H150_H200_AUTH_001--EXP11B_H150_H200_ATTEMPT_001.json
consumption_marker_sha256 = 6f6174ea61018d37e41bae2a69761680600fdc0f412a23781e8027d78c21940d
consumption_marker_size_bytes = 332
consumption_marker_status = CONSUMED_EXECUTION_STARTED
marker_authorization_id = EXP11B_H150_H200_AUTH_001
marker_attempt_id = EXP11B_H150_H200_ATTEMPT_001
marker_approved_package_commit = 50d90a356a0fac0267c270568f3926430a246026
marker_execution_head = ea4bc0bde3246b40a25453dabeef5d571cf7c021
marker_started_at_utc = 2026-09-12T21:37:04.837890Z
```

## 5. Validación read-only de outputs

```makefile
OFFICIAL_OUTPUT_ROOT_EXISTS = true
official_output_root = outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1
output_file_count = 8
run_manifest_status = COMPLETED
retrieval_executed = true
evaluation_metrics_computed = true
run_count = 20
unique_run_id_count = 20
unique_bank_id_count = 20
H150_run_count = 10
H200_run_count = 10
all_run_status = COMPLETED
metrics_by_bank_row_count = 20
case_level_row_count = 21120
rows_per_bank_case_level = 1056
candidate_ranking_row_count = 1350992
candidate_rank_min = 1
candidate_rank_max = 75
candidate_unique_bank_count = 20
condition_summary_row_count = 2
hash_ledger_row_count = 7
failure_ledger_status = NO_FAILURES
failure_stage = NONE
environment_git_commit = ea4bc0bde3246b40a25453dabeef5d571cf7c021
bank_identity_postcheck = PASS_EXACT_20_OF_20
official_bank_content_mutated = false
staging_sibling_count = 0
failed_sibling_count = 0
```

Los headers de metrics, case-level, candidates, condition summary y hash ledger coincidieron exactamente con los contratos congelados. Los siete hashes y tamaños declarados por el ledger fueron recalculados por lectura y coincidieron de forma exacta.

## 6. Observaciones brutas por condición

```makefile
H150_top_1_mean = 0.512689393939394
H150_top_3_mean = 0.6899621212121212
H150_top_5_mean = 0.7833333333333333
H150_top_10_mean = 0.8915719696969697
H150_top_50_mean = 0.9895833333333334
H150_mrr_mean = 0.6332675214603809

H200_top_1_mean = 0.5141098484848485
H200_top_3_mean = 0.6894886363636363
H200_top_5_mean = 0.7820075757575757
H200_top_10_mean = 0.8952651515151515
H200_top_50_mean = 0.9852272727272726
H200_mrr_mean = 0.6333104425906166
```

Estos valores se registran únicamente como observaciones brutas. No se declara aprobación metodológica ni cierre de EXP11B.

## 7. Identidad de artefactos oficiales

| Artefacto | SHA-256 | Bytes | Filas | Persistencia |
|---|---|---:|---:|---|
| `exp11b_retrieval_candidates_v0.1.csv` | `1dde84b65d8fb060211120ac73a04f1d5a5f7593e6381ed601fbdfb3f4bc9024` | 264935868 | 1350992 | LOCAL_ONLY_GIT_BLOB_LIMIT_GUARD |
| `exp11b_retrieval_case_level_v0.1.csv` | `b121a64ee19ea08733f85c6b93034b040bf0cb6b91a423df1d2c7cc89c4f9a35` | 4135216 | 21120 | VERSIONED |
| `exp11b_retrieval_condition_summary_v0.1.csv` | `42754c29326800a3f10c38bf22fa6b37dfab7b635dfda9fa1108100591ec2905` | 401 | 2 | VERSIONED |
| `exp11b_retrieval_environment_v0.1.json` | `1351374ee48b0d4ad60da351863870d4fb16fcf065f9d6a43d43e5b79ec10e1c` | 431 | N/A | VERSIONED |
| `exp11b_retrieval_failures_v0.1.json` | `6d485227c61d11ca027978ffb6fcd21cfbb7a05d436239572a55d08363efed40` | 210 | N/A | VERSIONED |
| `exp11b_retrieval_metrics_by_bank_v0.1.csv` | `919e602bd5a728185ec8aecc02127758d98319a16911f89d07eecde050525ef8` | 4490 | 20 | VERSIONED |
| `exp11b_retrieval_output_hashes_v0.1.csv` | `c766968016e2d699fe5fb6221fdd2486d67c27a61b68348d6eb696ce0b115aec` | 964 | 7 | VERSIONED |
| `exp11b_retrieval_run_manifest_v0.1.json` | `70cdf4e9362b47cd6e9f263577cb0c8173aef5ce24df49b352b0c2ebc447163e` | 13868 | N/A | VERSIONED |

## 8. Execution record

```makefile
execution_record_path = outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_official_execution_record_v0.1.json
execution_record_sha256 = 83d37a5439d8000e6f2feac932e96497e79ae906be515814e3d5ca53c41ad009
execution_record_size_bytes = 5842
execution_record_status = CANDIDATE_OFFICIAL_EXECUTION_COMPLETED_PENDING_EXTERNAL_AUDIT
runtime_evidence_classification = CODEX_LOCAL_OFFICIAL_EXECUTION_EVIDENCE / PENDING_EXTERNAL_AUDIT
```

## 9. Candidato de resultados

```makefile
RESULT_CANDIDATE_BRANCH = codex/exp11b-retrieval-h150-h200-results-v01
RESULT_CANDIDATE_COMMIT = dfd04f0db26383624d54e52bf4fd72f06bbb869c
RESULT_CANDIDATE_PARENT = ea4bc0bde3246b40a25453dabeef5d571cf7c021
RESULT_CANDIDATE_TREE = ea9ece98c4bc88b934b0d894f514b45a42a00f10
RESULT_CANDIDATE_COMMITS_AHEAD_OF_MAIN = 1
RESULT_CANDIDATE_COMMITS_BEHIND_MAIN = 0
RESULT_CANDIDATE_CHANGED_PATH_COUNT = 9
RESULT_CANDIDATE_PUBLISHED = true
RESULT_CANDIDATE_INTEGRATED = false
```

Artefactos versionados:

```text
outputs/audits/exp11b_retrieval_execution_attempts/EXP11B_H150_H200_AUTH_001--EXP11B_H150_H200_ATTEMPT_001.json
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_official_execution_record_v0.1.json
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_case_level_v0.1.csv
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_condition_summary_v0.1.csv
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_environment_v0.1.json
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_failures_v0.1.json
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_metrics_by_bank_v0.1.csv
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_output_hashes_v0.1.csv
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_run_manifest_v0.1.json
```

Artefacto local-only por guard de tamaño:

```makefile
local_only_large_artifacts = outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_candidates_v0.1.csv
local_only_large_artifact_sha256 = 1dde84b65d8fb060211120ac73a04f1d5a5f7593e6381ed601fbdfb3f4bc9024
local_only_large_artifact_size_bytes = 264935868
local_only_large_artifact_status = LOCAL_OFFICIAL_ARTIFACT_NOT_VERSIONED_DUE_TO_GIT_BLOB_LIMIT_GUARD
```

El artefacto local-only no fue comprimido, dividido, reescrito ni añadido a Git.

## 10. Ámbitos preservados

```makefile
plan_head_final = 6e327d4bcde32a3804e6923015eaa505a0a53374
article_head_final = 254b1e6df736fa9938ac86a515d65b36f4d361c5
plan_modified = false
article_modified = false
EXP12_authorized = false
EXP12_executed = false
GROUP2B_started = false
GROUP3_started = false
authorization_modified_after_integration = false
runner_modified = false
config_modified = false
banks_rematerialized = false
```

## 11. Persistencia administrativa

```makefile
administrative_branch = codex/prompts-temporary
administrative_prompt_commit = 65fec5fc39cf3d121f2b087953d685c16e3dafdf
administrative_response_path = codex_prompts_tmp/48_RESPUESTA_INTEGRAR_AUTORIZACION_Y_EJECUTAR_ONE_SHOT_EXP11B_H150_H200.md
administrative_commit = SELF / origin/codex/prompts-temporary HEAD containing this response
administrative_changed_path_count = 1
scientific_files_in_administrative_commit = false
```

```makefile
PROMPT48 = COMPLETED
EXP11B_RETRIEVAL_AUTHORIZATION = APPROVED / INTEGRATED / CONSUMED
EXP11B_RETRIEVAL_ATTEMPT_001 = EXECUTED_ONCE / COMPLETED / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL_RESULTS = CANDIDATE / NOT_INTEGRATED / PENDING_EXTERNAL_AUDIT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
