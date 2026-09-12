# RESPUESTA PROMPT 45 — CORRECCION ONE-SHOT, BINDING Y STREAMING EXP11B

```makefile
PROMPT45 = COMPLETED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE_V02 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## 1. Refs iniciales y finales

```makefile
origin/main_initial = 09ff184854659110f7711b3eee65fc18927649da
origin/main_final = 09ff184854659110f7711b3eee65fc18927649da
origin/docs/plan-maestro-temporal-2026-08-31_initial = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/docs/plan-maestro-temporal-2026-08-31_final = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript_initial = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/article/main-manuscript_final = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/exp11b-retrieval-execution-package-v01 = 26b9e2bcf6dad74231f208f9137ffb0e39caf2e1
v01_parent = 09ff184854659110f7711b3eee65fc18927649da
v01_is_ancestor_of_main = false
EXP11B_PORTABILITY_DEBT = CLOSED / APPROVED / INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## 2. Candidato rechazado v01

```makefile
rejected_candidate = 26b9e2bcf6dad74231f208f9137ffb0e39caf2e1
rejected_candidate_status = DO_NOT_INTEGRATE
rejected_candidate_integrated = false
rejected_candidate_used_as_parent = false
rejected_candidate_cherry_picked = false
rejected_candidate_amended = false
```

El candidato v02 se reconstruyo limpiamente desde `origin/main`, sin ancestry ni contenido Git heredado del commit v01 rechazado.

## 3. Resolucion F001-F004

### F001 — Consumo one-shot real

```makefile
F001 = CLOSED
one_shot_consumption_required = true
exclusive_creation = open_mode_x
reuse_same_authorization_after_start = false
new_authorization_required_after_failure = true
```

El marcador gobernado se crea mediante apertura exclusiva inmediatamente antes del primer scoring oficial. Registra `authorization_id`, `attempt_id`, `approved_package_commit`, `execution_head`, `started_at_utc` y `status=CONSUMED_EXECUTION_STARTED`. No se elimina ni sobrescribe tras el inicio, incluso ante fallo.

### F002 — Binding de package commit

```makefile
F002 = CLOSED
approved_package_commit_exists_required = true
approved_package_commit_ancestor_of_execution_head_required = true
package_head_worktree_blob_identity_required = true
package_head_canonical_sha256_identity_required = true
noncanonical_config_path_guard = PASS_BLOCKED_BEFORE_SCORING
```

La autorizacion futura liga el commit cientifico aprobado, no exige que sea igual a `HEAD`. Un `execution_head` descendiente puede contener la autorizacion versionada, pero runner y config deben conservar los mismos Git blobs y SHA-256 canonicos que el paquete aprobado. El working tree se verifica contra el mismo blob Git, evitando relajacion de contenido y falsos drift por conversion EOL.

### F003 — Streaming y memoria acotada

```makefile
F003 = CLOSED
stream_case_level_output = true
stream_candidate_output = true
global_case_accumulator = false
global_candidate_accumulator = false
flush_frequency = PER_BANK
in_memory_scope = CURRENT_BANK_INDEX_PLUS_SMALL_SUMMARIES
partial_outputs_are_official = false
```

Los case-level y candidates se escriben directamente a writers CSV de staging. Solo se conservan en memoria el banco/indice activo, la consulta/candidatos actuales, 20 filas de metricas y metadatos pequenos.

### F004 — Contexto inequivoco de fallo

```makefile
F004 = CLOSED
tracked_context = current_run_id,current_bank_id,current_condition,current_stage
active_bank_failure_test = PASS_EXACT_ACTIVE_BANK_RUN_STAGE
prebank_failure_identity = NOT_STARTED
output_finalization_bank_identity = NOT_STARTED
output_finalization_context_test = PASS_NOT_MISATTRIBUTED
```

Los stages implementados son `BANK_VALIDATION`, `INDEX_BUILD`, `EVAL_SCORING`, `CASE_WRITE`, `METRIC_FINALIZATION` y `OUTPUT_FINALIZATION`. Un fallo de finalizacion global ya no se atribuye al ultimo banco completado.

## 4. Paths, blobs y SHA-256 v02

```text
src/experiments/run_exp11b_historical_retrieval_h150_h200_v02.py
  git_blob = cc834b041fedacabc5ffde107c4705b6f9dd6fd1
  sha256 = 7b8b25f3a250b5e71be19430486e5055cce4c90d2b9176078b7b5ccc82fb6e1d

src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.2.json
  git_blob = 711e505e8288c09f6c0703d8051ad0543fcf2d22
  sha256 = 4dc04ae4bfe34a1f4664646239121090e8e1eb90f24baf47eceb14761ebe4ea3

outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.2.json
  git_blob = 124602550f138292fa7ccdebfcfcf6d2ed4a6778
  sha256 = d0aa5fdaeaa31d23abaa1aa982f50e0cdd411f881f507e4440fda8465006ae4d
```

## 5. Validacion estatica

```makefile
config_json = PASS
py_compile = PASS
import = PASS
cli_help = PASS
cli_modes = --preflight,--self-test-h100,--execute-official
source_binding_count = 14
source_binding_mismatch_count = 0
scientific_semantics_changed = false
```

Se conservaron helpers canonicos EXP-04/EXP11A, normalizacion, tokenizer, `k1=1.5`, `b=0.75`, candidate depth 100, k `[1,3,5,10,50]`, desempate, deduplicacion, rank, MRR y denominador 1056.

## 6. Preflight unico de bancos

`--preflight` se ejecuto exactamente una vez.

```makefile
BANK_PREFLIGHT = PASS_EXACT_20_OF_20
preflight_invocation_count = 1
bank_count = 20
H150_count = 10
H200_count = 10
bank_identity_mismatch_count = 0
eval_sha_match = true
h100_sha_match = true
canonical_source_binding_mismatch_count = 0
official_output_root_exists = false
official_bank_write_count = 0
official_bank_content_mutated = false
classification = CODEX_LOCAL_BANK_PREFLIGHT / NOT_INDEPENDENT_GITHUB_RUNTIME_OBSERVATION
```

Identidades SHA-256 observadas, todas `PASS_EXACT` en los 14 campos gobernados:

```text
EXP11B_R01_H150 a95ccaa947994e9e01392c1f519f7a19ef015b560a2c3aa77f6bf3ee7a5961db
EXP11B_R01_H200 20c987e52f0d6a221ffaa756527b1b4b571117a57c839909908cd7e7441abe49
EXP11B_R02_H150 331762d93446c575abaf59c76c38eb55e106431c811dda48c99d489cff279000
EXP11B_R02_H200 0b6772d0ead99f352ffde4170bceb6e443da0b84a3b652bee845f05c765cb468
EXP11B_R03_H150 1001a3821aec92b1f7c785ba620100bb68acee0a2e4312bb041f75578eb13fb2
EXP11B_R03_H200 d27fcc4a9711cbc4d9126fc337518d09430a988fae554ee12246b1fec4205b77
EXP11B_R04_H150 2f21215da09a2e9bdb0fe72b9dae56a88f03109cbab901a0b236633aa7410850
EXP11B_R04_H200 b2488c0b0a0525f0d6a98dd54071fd715afefbab719d526e4779283d9bf67887
EXP11B_R05_H150 74524582ec2158d2e87ac46d06a2259b7d03a674212678d39713345517d08f11
EXP11B_R05_H200 80ac01f63c184237c8ff36a5ecd1fef38d18562114bd60842cb2bdc8f9ee5cae
EXP11B_R06_H150 66259a5fa9058b1f3c58601541aee4637f758878f18d8757e4c1bfc21de397a8
EXP11B_R06_H200 548159b34b19be379d7e1e54f170985466189c77796883fa4c8a2429c0d926fd
EXP11B_R07_H150 f00e9625b0684200e2a2fe91b3bcec1abeb05e3d444244177371ff7489b51345
EXP11B_R07_H200 221030d48308566f7e79f1ee7a37b1f9c9d6f7d4aadaba709a691fd417e1aa57
EXP11B_R08_H150 d7bf195592c749333820cb1c1bc8c3202a446a1d5a6ebc2ef051593f52356bb8
EXP11B_R08_H200 7005a43687d80bd4454389fb34f96577911b75558618ab4b63104341ae85875a
EXP11B_R09_H150 6353eb3081c31e829f978958ab0ab5d000633e1c678ef7aaf691444b33245f9d
EXP11B_R09_H200 2c72fb62deb0cecfe90b49b991bf6918ab4177a35aebb8e88bf74b08058fd841
EXP11B_R10_H150 163f5b9f6284a40b21da405b958cccb571df7b4932381ecb832a2c771ca850b9
EXP11B_R10_H200 ed570fccf8913fbd3416157013f152697dc1ed6358313e379e6b9e93af11cdf2
```

La identidad completa se encuentra en el readiness v0.2.

## 7. H100 full-output shadow unico

`--self-test-h100` se ejecuto exactamente una vez. Uso la misma capa de streaming, serializacion, manifests y hashes que la futura ejecucion oficial, exclusivamente con H100 y en un directorio temporal eliminado al finalizar.

```makefile
H100_FULL_OUTPUT_SHADOW = PASS
self_test_invocation_count = 1
Top1_numerator = 538
Top3_numerator = 709
Top5_numerator = 806
Top10_numerator = 941
Top50_numerator = 1047
all_numerator_deltas = 0
MRR_observed = 0.6297077493524843
MRR_expected = 0.6297077493524843
MRR_delta = 0.0
MRR_abs_tolerance = 1e-12
h150_h200_banks_opened = 0
temporary_cleanup = PASS
```

Schemas/artefactos temporales validados:

```makefile
run_manifest_json = PASS
metrics_by_bank_csv = PASS
case_level_csv = PASS
candidate_ranking_csv = PASS
condition_summary_csv = PASS
output_hash_ledger_csv = PASS
failure_ledger_json = PASS
environment_json = PASS
validated_file_count = 8
```

## 8. Guards y modelos preventivos

```makefile
NO_AUTH_GUARD = PASS_BLOCKED_BEFORE_SCORING
no_auth_exit_code = 2
no_auth_classification = OFFICIAL_EXECUTION_BLOCKED_NO_AUTHORIZATION
INVALID_PACKAGE_BINDING_GUARD = PASS_BLOCKED_BEFORE_SCORING
invalid_binding_classification = OFFICIAL_EXECUTION_BLOCKED_APPROVED_PACKAGE_COMMIT_MISSING
CONSUMED_AUTH_GUARD = PASS_BLOCKED_BEFORE_SCORING
consumed_classification = OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_ALREADY_CONSUMED
DESCENDANT_AUTHORIZATION_MODEL = PASS_CONTRACT_MODEL
descendant_model_scoring_count = 0
FAILURE_CONTEXT_TEST = PASS
STREAMING_OUTPUT_MODEL = PASS
synthetic_cleanup = PASS
```

El modelo descendiente se probo en un repositorio Git temporal con un commit de paquete y un commit descendiente de autorizacion. Runner/config permanecieron atados a los blobs y SHA-256 del paquete. No se uso ninguna ruta oficial ni se ejecuto scoring.

El marcador consumido se probo en un directorio temporal: la primera creacion exclusiva paso y la segunda fue rechazada antes de scoring. El marcador sintetico retuvo `CONSUMED_EXECUTION_STARTED` hasta el cleanup del temporal.

## 9. No contaminacion

```makefile
OFFICIAL_OUTPUT_ROOT_EXISTS = false
OFFICIAL_AUTHORIZATION_EXISTS = false
REAL_CONSUMPTION_MARKER_EXISTS = false
H150_H200_SCORING_COUNT = 0
H150_H200_METRICS_OBSERVED = false
H150_H200_CASE_RANKINGS_OBSERVED = false
official_bank_write_count = 0
official_bank_content_mutated = false
retrieval_executed = false
EXP12_authorized = false
EXP12_executed = false
```

No se creo autorizacion oficial, no se consumio autorizacion real y no se creo el output root oficial.

## 10. Identidad Git del candidato v02

```makefile
branch = codex/exp11b-retrieval-execution-package-v02
candidate_commit = f5dddac0d296e74e5f92af3f863cbb3c74e757b9
parent = 09ff184854659110f7711b3eee65fc18927649da
tree = b73915a7b9226a3379205eb00776e8065b3e7614
commits_ahead_of_main = 1
commits_behind_main = 0
changed_path_count = 3
remote_candidate = f5dddac0d296e74e5f92af3f863cbb3c74e757b9
candidate_published = true
```

Diff exacto:

```text
A outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.2.json
A src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.2.json
A src/experiments/run_exp11b_historical_retrieval_h150_h200_v02.py
```

```makefile
existing_scientific_files_modified = false
plan_maestro_modified = false
article_modified = false
EXP12_modified = false
H100_modified = false
DEV_modified = false
EVAL_modified = false
official_banks_modified = false
retrieval_gate_historical_modified = false
materialization_contract_modified = false
working_tree_clean = true
```

## 11. Entorno

```makefile
python_implementation = CPython
python_version = 3.12.14
platform = Windows-11-10.0.26200-SP0
machine = AMD64
numpy = 2.3.5
pandas = 3.0.1
runtime_classification = CODEX_LOCAL_PREEXECUTION_CHECKS / NOT_INDEPENDENT_GITHUB_RUNTIME_OBSERVATION
```

## 12. Persistencia administrativa

```makefile
administrative_branch = codex/prompts-temporary
administrative_parent = b7d5247f9f373768186784d8d1c2cad1fc69b1f4
administrative_path = codex_prompts_tmp/45_RESPUESTA_CORREGIR_PAQUETE_EJECUCION_EXP11B_ONE_SHOT_Y_STREAMING.md
administrative_commit = SELF / origin/codex/prompts-temporary HEAD containing this response
administrative_content_scope = RESPONSE_ONLY
```

## 13. Estado terminal

```makefile
PROMPT45 = COMPLETED
F001 = CLOSED
F002 = CLOSED
F003 = CLOSED
F004 = CLOSED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE_V02 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
BLOCKERS = NONE_FOR_EXTERNAL_AUDIT
```
