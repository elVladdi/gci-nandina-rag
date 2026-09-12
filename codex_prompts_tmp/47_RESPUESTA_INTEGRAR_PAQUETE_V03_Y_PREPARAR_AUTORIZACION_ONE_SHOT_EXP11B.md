# RESPUESTA PROMPT 47 — INTEGRAR PAQUETE V03 Y PREPARAR AUTORIZACIÓN ONE-SHOT EXP11B

```makefile
PROMPT47 = COMPLETED
EXP11B_RETRIEVAL_AUTHORIZATION = CANDIDATE / PENDING_EXTERNAL_AUDIT / NOT_INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED_ON_MAIN / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## 1. Precondiciones y referencias

```makefile
main_initial = 09ff184854659110f7711b3eee65fc18927649da
origin_main_initial = 09ff184854659110f7711b3eee65fc18927649da
approved_package_branch = codex/exp11b-retrieval-execution-package-v03
approved_package_commit = 50d90a356a0fac0267c270568f3926430a246026
approved_package_parent = 09ff184854659110f7711b3eee65fc18927649da
approved_package_ahead_of_main = 1
approved_package_behind_main = 0
approved_package_changed_path_count = 3
plan_head_initial = 6e327d4bcde32a3804e6923015eaa505a0a53374
article_head_initial = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Los candidatos rechazados permanecieron inmutables y no fueron integrados ni usados como ancestros del paquete v0.3:

```makefile
v01_rejected = 26b9e2bcf6dad74231f208f9137ffb0e39caf2e1 / DO_NOT_INTEGRATE
v02_rejected = f5dddac0d296e74e5f92af3f863cbb3c74e757b9 / DO_NOT_INTEGRATE
v01_ancestor_of_main_final = false
v02_ancestor_of_main_final = false
```

## 2. Fase A — integración del paquete v0.3

```makefile
package_integration_mode = FAST_FORWARD_EXACT
package_integrated_commit = 50d90a356a0fac0267c270568f3926430a246026
package_integrated_tree = adb47add84bc69ff854cd93b55a018150f31c5c3
main_final = 50d90a356a0fac0267c270568f3926430a246026
origin_main_final = 50d90a356a0fac0267c270568f3926430a246026
additional_commit_on_main = false
package_tree_identity = true
```

Paths exactos integrados:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.3.json
src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.3.json
src/experiments/run_exp11b_historical_retrieval_h150_h200_v03.py
```

La integración se realizó con `git merge --ff-only`; no hubo merge commit, squash, cherry-pick, rebase, amend ni reconstrucción.

## 3. Referencias documentales preservadas

```makefile
plan_head_final = 6e327d4bcde32a3804e6923015eaa505a0a53374
article_head_final = 254b1e6df736fa9938ac86a515d65b36f4d361c5
plan_modified = false
article_modified = false
```

## 4. Fase B — candidato de autorización one-shot

```makefile
AUTHORIZATION_CANDIDATE_BRANCH = codex/exp11b-retrieval-authorization-v03
AUTHORIZATION_CANDIDATE_COMMIT = ea4bc0bde3246b40a25453dabeef5d571cf7c021
AUTHORIZATION_CANDIDATE_PARENT = 50d90a356a0fac0267c270568f3926430a246026
AUTHORIZATION_CANDIDATE_TREE = 428c71afd0b435654eacd82f4e2ee9e99dabc1bf
AUTHORIZATION_CHANGED_PATH_COUNT = 1
AUTHORIZATION_COMMITS_AHEAD_OF_MAIN = 1
AUTHORIZATION_COMMITS_BEHIND_MAIN = 0
AUTHORIZATION_CANDIDATE_PUBLISHED = true
AUTHORIZATION_CANDIDATE_INTEGRATED = false
```

Único path añadido:

```makefile
AUTHORIZATION_PATH = outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.3.json
AUTHORIZATION_GIT_BLOB = 7a23c64857b8f28302be7ce75d1269cbe60cc25b
AUTHORIZATION_SHA256 = f9a9b468b3d856492dd6a272ad8cf73932dba91b02e34a42d715352f3dd45fd0
AUTHORIZATION_BYTE_LENGTH = 1440
```

Contenido contractual verificado:

```makefile
authorization_id = EXP11B_H150_H200_AUTH_001
attempt_id = EXP11B_H150_H200_ATTEMPT_001
authorization_status = AUTHORIZED_ONE_SHOT
approved_package_commit = 50d90a356a0fac0267c270568f3926430a246026
runner_git_blob = 90bbeba27e4890613cb463fffc1cfc07252292c5
runner_sha256 = 32f495996b8f1486cc6ef5f3906e84eb417e480208a721fb8b1c3f6820e65e06
config_git_blob = 08cc58f95b2d6989bf75e64b16c0d9aa8158f642
config_sha256 = 2b91c06762409d10478cbf112bb25486ef3ffa410e5819fb0704f61fe64aa6af
eval_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
bank_manifest_sha256 = 67512d88a46dcd85427d9eca4be07eeea3f6ec2821bf77e7acfec5a09a706cf4
bank_ledger_sha256 = 9686c2f642ec47c36079a3085c4d68a3f1b555588a8623ecca59333e12e0f56c
portability_closure_blob = bfbeedff9025ae928a85ab8b65a261ff475422cb
expected_banks = 20
official_output_root = outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1
authorization_candidate_status = PENDING_EXTERNAL_AUDIT_NOT_EFFECTIVE_ON_MAIN
```

## 5. Validación no consumidora

Se importó el runner v0.3 y se invocó exclusivamente `_validate_authorization()` contra la ruta canónica. No se invocó `--execute-official`, `_consume_authorization`, `_bm25_scores` ni ningún pipeline de retrieval.

```makefile
AUTHORIZATION_JSON_VALID = PASS
AUTHORIZATION_HEAD_TRACKED = PASS
AUTHORIZATION_HEAD_WORKTREE_BLOB_IDENTITY = PASS_EXACT
AUTHORIZATION_HEAD_WORKTREE_SHA256_IDENTITY = PASS_EXACT
AUTHORIZATION_HEAD_WORKTREE_BYTES_IDENTITY = PASS_EXACT
APPROVED_PACKAGE_IS_ANCESTOR_OF_AUTHORIZATION_HEAD = PASS
RUNNER_PACKAGE_HEAD_WORKTREE_IDENTITY = PASS_EXACT
CONFIG_PACKAGE_HEAD_WORKTREE_IDENTITY = PASS_EXACT
NONCONSUMING_AUTHORIZATION_VALIDATION = PASS
```

Objeto devuelto por la validación no consumidora:

```makefile
validated_approved_package_commit = 50d90a356a0fac0267c270568f3926430a246026
validated_execution_head = ea4bc0bde3246b40a25453dabeef5d571cf7c021
validated_authorization_path = outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.3.json
validated_authorization_git_blob = 7a23c64857b8f28302be7ce75d1269cbe60cc25b
validated_authorization_sha256 = f9a9b468b3d856492dd6a272ad8cf73932dba91b02e34a42d715352f3dd45fd0
```

## 6. Estado no consumidor y no contaminación

```makefile
OFFICIAL_OUTPUT_ROOT_EXISTS = false
REAL_CONSUMPTION_MARKER_EXISTS = false
REAL_CONSUMPTION_MARKER_ROOT_EXISTS = false
H150_H200_SCORING_COUNT = 0
H150_H200_RESULTS_OBSERVED = false
H150_H200_METRICS_OBSERVED = false
H150_H200_RANKINGS_OBSERVED = false
authorization_consumed = false
execute_official_invocation_count = 0
retrieval_executed = false
```

El JSON contiene `AUTHORIZED_ONE_SHOT` como contenido prospectivo del candidato, pero no es autorización efectiva porque el commit no está integrado en `main` y permanece pendiente de auditoría externa.

## 7. Ámbitos no modificados

```makefile
runner_modified_in_authorization_candidate = false
config_modified_in_authorization_candidate = false
readiness_modified_in_authorization_candidate = false
official_banks_modified = false
historical_gate_modified = false
plan_modified = false
article_modified = false
EXP12_modified = false
EXP12_authorized = false
EXP12_executed = false
GROUP2B_started = false
GROUP3_started = false
```

## 8. Persistencia administrativa

```makefile
administrative_branch = codex/prompts-temporary
administrative_prompt_commit = b43ff32508994304edeec50f504db1e9177c68dd
administrative_response_path = codex_prompts_tmp/47_RESPUESTA_INTEGRAR_PAQUETE_V03_Y_PREPARAR_AUTORIZACION_ONE_SHOT_EXP11B.md
administrative_commit = SELF / origin/codex/prompts-temporary HEAD containing this response
administrative_changed_path_count = 1
scientific_files_in_administrative_commit = false
```

```makefile
PROMPT47 = COMPLETED
EXP11B_RETRIEVAL_AUTHORIZATION = CANDIDATE / PENDING_EXTERNAL_AUDIT / NOT_INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED_ON_MAIN / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
