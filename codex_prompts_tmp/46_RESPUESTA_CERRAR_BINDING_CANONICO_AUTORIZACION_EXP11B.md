# RESPUESTA PROMPT 46 — CERRAR BINDING CANÓNICO DE AUTORIZACIÓN EXP11B

```makefile
PROMPT46 = COMPLETED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE_V03 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## 1. Referencias verificadas

```makefile
baseline_main = 09ff184854659110f7711b3eee65fc18927649da
initial_origin_main = 09ff184854659110f7711b3eee65fc18927649da
final_origin_main = 09ff184854659110f7711b3eee65fc18927649da
canonical_plan_head = 6e327d4bcde32a3804e6923015eaa505a0a53374
canonical_article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
v01_rejected_candidate = 26b9e2bcf6dad74231f208f9137ffb0e39caf2e1
v02_rejected_candidate = f5dddac0d296e74e5f92af3f863cbb3c74e757b9
v01_parent = 09ff184854659110f7711b3eee65fc18927649da
v02_parent = 09ff184854659110f7711b3eee65fc18927649da
v01_ancestor_of_main = false
v02_ancestor_of_main = false
v01_ancestor_of_v03 = false
v02_ancestor_of_v03 = false
v01_status = DO_NOT_INTEGRATE
v02_status = DO_NOT_INTEGRATE
v01_integrated = false
v02_integrated = false
```

`EXP11B_PORTABILITY_DEBT` permaneció `CLOSED / APPROVED / INTEGRATED`. No se usó como parent, no se integró y no se modificó ninguno de los candidatos rechazados v01/v02.

## 2. Candidato científico v0.3

```makefile
candidate_branch = codex/exp11b-retrieval-execution-package-v03
candidate_commit = 50d90a356a0fac0267c270568f3926430a246026
candidate_parent = 09ff184854659110f7711b3eee65fc18927649da
candidate_tree = adb47add84bc69ff854cd93b55a018150f31c5c3
commits_ahead_of_main = 1
commits_behind_main = 0
changed_path_count = 3
candidate_published = true
remote_candidate_head = 50d90a356a0fac0267c270568f3926430a246026
main_modified = false
```

Paths exactos añadidos:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.3.json
src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.3.json
src/experiments/run_exp11b_historical_retrieval_h150_h200_v03.py
```

No se modificó ningún archivo científico preexistente.

## 3. Identidad de los artefactos v0.3

```makefile
runner_path = src/experiments/run_exp11b_historical_retrieval_h150_h200_v03.py
runner_git_blob = 90bbeba27e4890613cb463fffc1cfc07252292c5
runner_sha256 = 32f495996b8f1486cc6ef5f3906e84eb417e480208a721fb8b1c3f6820e65e06

config_path = src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.3.json
config_git_blob = 08cc58f95b2d6989bf75e64b16c0d9aa8158f642
config_sha256 = 2b91c06762409d10478cbf112bb25486ef3ffa410e5819fb0704f61fe64aa6af

readiness_path = outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.3.json
readiness_git_blob = 49af7b0ea8c1440e2e1ed64a3e01fec31b29d9e5
readiness_sha256 = 2b48ddd3005601d56059257c26737e8f469fddef9ddaadeaf2c34d7b592c86ca
```

La config conserva la semántica científica congelada y fija la autorización futura exclusivamente en:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.3.json
```

## 4. Cierre de findings

```makefile
F005 = CLOSED
F006 = CLOSED
F003_NO_REGRESSION = PASS
F004_NO_REGRESSION = PASS
```

F005 quedó cerrado mediante resolución canónica estricta de la ruta de autorización, exigencia de que `HEAD:<canonical_authorization_path>` exista, comprobación de identidad del Git blob y del SHA-256 entre HEAD y working tree, y rechazo fail-closed de rutas alternativas, archivos no versionados y mutaciones locales.

F006 quedó cerrado desplazando el hook one-shot al límite exacto: después de validar SHA, filas e índice del primer banco y justo antes de la primera llamada a `_bm25_scores`. La creación exclusiva usa semántica `open(..., "x")` y ocurre una sola vez.

F003 conserva streaming por banco de case-level y candidates, sin acumuladores globales y con flush por banco. F004 conserva `current_run_id`, `current_bank_id`, `current_condition` y `current_stage`, además de atribución correcta de fallos pre-bank y de finalización.

## 5. Validación estática

```makefile
config_json = PASS
py_compile = PASS
import = PASS
cli_help = PASS
source_binding_count = 14
source_binding_mismatch_count = 0
```

## 6. Preflight único

```makefile
preflight_invocation_count = 1
preflight_status = PASS
preflight_mode = PREFLIGHT_ONLY
bank_validation = PASS_EXACT_20_OF_20
bank_count = 20
h150_bank_count = 10
h200_bank_count = 10
bank_identity_mismatch_count = 0
governed_identity_field_count = 14
eval_sha_match = true
h100_sha_match = true
canonical_source_binding_mismatch_count = 0
official_bank_write_count = 0
official_bank_content_mutated = false
```

Las 20 identidades del readiness son exactamente iguales al inventario congelado para los 14 campos gobernados y contienen 20 SHA bancarios únicos.

## 7. H100 full-output shadow único

```makefile
h100_shadow_invocation_count = 1
h100_shadow_status = PASS
h100_shadow_mode = SELF_TEST_H100_FULL_OUTPUT_SHADOW_ONLY
top1_numerator = 538
top3_numerator = 709
top5_numerator = 806
top10_numerator = 941
top50_numerator = 1047
mrr = 0.6297077493524843
mrr_expected = 0.6297077493524843
mrr_delta = 0.0
mrr_abs_tolerance = 1e-12
h150_h200_banks_opened = 0
temporary_cleanup = PASS
```

Los ocho contratos de salida se validaron `PASS`: run manifest JSON, metrics-by-bank CSV, case-level CSV, candidate-ranking CSV, condition-summary CSV, output-hash-ledger CSV, failure-ledger JSON y environment JSON.

## 8. Pruebas preventivas E–O

```makefile
NO_AUTH_GUARD = PASS_BLOCKED_BEFORE_SCORING
NO_AUTH_GUARD_EXIT_CODE = 2
NONCANONICAL_AUTH_GUARD = PASS_BLOCKED_BEFORE_MARKER
UNVERSIONED_AUTH_GUARD = PASS_BLOCKED_BEFORE_MARKER
DIRTY_AUTH_GUARD = PASS_BLOCKED_BEFORE_MARKER
INVALID_PACKAGE_BINDING_GUARD = PASS_BLOCKED_BEFORE_SCORING
CONSUMED_AUTH_GUARD = PASS_BLOCKED_BEFORE_SCORING
DESCENDANT_AUTHORIZATION_MODEL = PASS_CONTRACT_MODEL
AUTHORIZATION_HEAD_WORKTREE_BLOB_IDENTITY = PASS_EXACT
AUTHORIZATION_HEAD_WORKTREE_SHA256_IDENTITY = PASS_EXACT
FAILURE_BEFORE_FIRST_SCORING = PASS / marker_created=false
SCORING_BOUNDARY_CONSUMPTION_TEST = PASS
synthetic_bm25_score_call_count = 2
synthetic_marker_creation_count = 1
marker_created_before_first_score = true
FAILURE_CONTEXT_TEST = PASS_EXACT
FAILURE_CONTEXT_OUTPUT_FINALIZATION = PASS_NOT_MISATTRIBUTED
STREAMING_OUTPUT_MODEL = PASS_BOUNDED_PER_BANK
global_case_accumulator = false
global_candidate_accumulator = false
synthetic_artifact_cleanup = PASS
```

Todas las pruebas de autorización y consumo fueron sintéticas en repositorios/directorios temporales. No abrieron bancos H150/H200 ni tocaron rutas oficiales.

## 9. No contaminación y estado terminal

```makefile
OFFICIAL_OUTPUT_ROOT_EXISTS = false
OFFICIAL_AUTHORIZATION_EXISTS = false
REAL_CONSUMPTION_MARKER_EXISTS = false
H150_H200_SCORING_COUNT = 0
H150_H200_METRICS_OBSERVED = false
H150_H200_CASE_RANKINGS_OBSERVED = false
retrieval_executed = false
execution_authorized = false
future_authorization_required = true
EXP12_authorized = false
EXP12_executed = false
bank_mutation = false
```

No se creó autorización oficial, no se consumió autorización real, no se creó el output root oficial y no se ejecutó ni observó retrieval, métricas o rankings H150/H200.

## 10. Ámbitos preservados

```makefile
plan_modified = false
article_modified = false
EXP12_modified = false
H100_modified = false
DEV_modified = false
EVAL_modified = false
official_banks_modified = false
historical_retrieval_gate_modified = false
materialization_manifest_or_ledger_modified = false
portability_replay_proof_modified = false
portability_closure_modified = false
```

Los avisos de limpieza de metadatos de worktrees obsoletos emitidos por Git no afectaron el commit, el tree, los tres paths ni las referencias publicadas.

## 11. Persistencia administrativa

```makefile
administrative_branch = codex/prompts-temporary
administrative_response_path = codex_prompts_tmp/46_RESPUESTA_CERRAR_BINDING_CANONICO_AUTORIZACION_EXP11B.md
administrative_parent = 1d1552d5caaf22f79d1e2ddfd50fdd2538e83673
administrative_commit = SELF / origin/codex/prompts-temporary HEAD containing this response
administrative_changed_path_count = 1
scientific_files_in_administrative_commit = false
```

```makefile
PROMPT46 = COMPLETED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE_V03 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
