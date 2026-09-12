# RESPUESTA PROMPT 37 - EJECUTAR ATTEMPT06 UNA SOLA VEZ

## Estado terminal

```makefile
PROMPT37 = COMPLETED
ATTEMPT06 = COMPLETED / PENDING_EXTERNAL_RESULT_AUDIT
ATTEMPT06_INVOCATIONS = 1
0B05C_METRIC_IMPACT = COMPUTED / PENDING_EXTERNAL_INTERPRETATION
0B05C_CLOSURE = NOT_YET_APPROVED
terminal_status = PASS
terminal_step = 19_final_completion_state
```

Attempt06 fue invocado exactamente una vez. No hubo retry, resume, segunda
invocacion ni ejecucion separada de EV03, EV04 o D1a.

## Precondiciones

Las siete precondiciones minimas pasaron antes de la invocacion:

```makefile
origin_main = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
authorization_branch = codex/0b05c-v05-attempt06-authorization
authorization_commit = a9b06b8748316d7f3c403eaa9d55b735e12d96c3
authorization_parent = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
authorization_tree = 59f663863e1897b2df7045931c1819ea94ec9fcb
authorization_ahead = 1
authorization_behind = 0
canonical_plan_head = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
authorization_diff_paths = 5/5 EXACT
prospective_roots_present_before = 0/16
tracked_working_tree_clean_before = true
prior_execution_branch_present = false
prior_attempt06_execution_record_present = false
```

Diff autorizado verificado:

```text
M outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json
A outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_numerical_authorization_record_v0.5.json
M outputs/audits/0b05c_corrective_numerical_gate_v0.5/d1a_numerical_execution_spec_v0.5.json
M outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev03_numerical_execution_spec_v0.5.json
M outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev04_numerical_execution_spec_v0.5.json
```

## Rama e invocacion

```makefile
execution_branch = codex/0b05c-v05-attempt06-execution
initial_execution_head = a9b06b8748316d7f3c403eaa9d55b735e12d96c3
command = .venv\Scripts\python.exe -B -m src.experiments.run_0b05c_corrective_numerical_v05 --execute-authorized
invocation_count = 1
started_at = 2026-09-11T23:50:57.0069945-05:00
completed_at = 2026-09-11T23:55:55.6747234-05:00
return_code = 0
pipeline_status = PASS
pipeline_mode = AUTHORIZED_EXECUTION
retry_performed = false
resume_performed = false
```

La propia invocacion ejecuto el preflight autorizado antes de los side effects.
No se realizo una invocacion separada del pipeline para repetir ese preflight.

```makefile
authorized_preflight = PASS
authorized_preflight_mode = AUTHORIZED_PREFLIGHT_ONLY
python = CPython 3.10.11 / Windows AMD64 / 64bit
executable_sha256 = b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961
historical_vector_replay = 21/21 PASS
project_local_import_closure = 31/31 PASS
```

## Pasos del pipeline

Los 19 pasos congelados terminaron en PASS o PASS_EXACT segun su contrato:

```text
01_unified_preflight = PASS
02_EV03_Decision885_control_reproduction = PASS_EXACT
03_EV03_control_reproduction_verification = PASS_EXACT
04_EV03_corrected_corpus_materialization = PASS
05_EV03_corrected_index_build_RECOVERED_HISTORICAL_SEMANTICS = PASS
06_EV03_corrected_evaluation = PASS
07_EV04_Decision885_control_reproduction_ENRICHED_MRR = PASS_EXACT
08_EV04_control_reproduction_verification_PASS_EXACT = PASS_EXACT
09_EV04_corrected_corpus_materialization = PASS
10_EV04_corrected_index_build = PASS
11_EV04_corrected_evaluation_ENRICHED_MRR = PASS
12_D1a_corrected_execution_under_future_v05_authorization = PASS
13_integrity_validation = PASS
14_case_level_comparisons = PASS
15_aggregate_comparisons = PASS
16_unified_sensitivity_summary = PASS
17_execution_manifest = PASS
18_exact_hash_ledger = PASS
19_final_completion_state = PASS / COMPLETED
```

## Roots producidos

Los 16 roots prospectivos v0.5 esperados fueron producidos:

```text
data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.5
outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.5
data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.5.jsonl
data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.5
outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5
data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.5
outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.5
data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.5.jsonl
data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.5
outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5
data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.5.jsonl
data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.5
outputs/evaluation/d1a_corrective_0b05c_v0.5
outputs/audits/d1a_corrective_0b05c_runtime_v0.5
outputs/evaluation/0b05c_corrective_numerical_v0.5
outputs/audits/0b05c_corrective_numerical_runtime_v0.5
```

```makefile
prospective_roots_produced = 16/16
governed_files_inside_roots = 48
ledger_governed_entries = 47
ledger_self_exclusion = 1
execution_record_outside_governed_roots = true
```

## Verificaciones read-only

```makefile
pipeline_steps_in_manifest = 19
execution_manifest_parseable = true
execution_manifest_status = PASS
exact_hash_ledger_parseable = true
exact_hash_ledger_status = PASS
exact_hash_ledger_mismatch_count = 0
staged_blobs_vs_ledger = 47/47 PASS
unified_sensitivity_summary_present = true
unified_sensitivity_summary_status = PASS
EV03_outputs_and_metrics_present = true
EV04_outputs_and_metrics_present = true
D1a_outputs_and_metrics_present = true
execution_failed_json_present = false
FAILED_status_inside_governed_roots = false
```

Referencias exactas principales:

```text
execution_manifest
  path = outputs/audits/0b05c_corrective_numerical_runtime_v0.5/execution_manifest_v0.5.json
  git_blob_sha1 = e17bafb045fc530002ee7e63f2fed2ed90840f32
  sha256 = 4fb2a6105c0129a720a4ac7b4dffa05600107ccf266084775d81a51b83d1ec2e

exact_hash_ledger
  path = outputs/audits/0b05c_corrective_numerical_runtime_v0.5/exact_hash_ledger_v0.5.json
  git_blob_sha1 = 3dd0cafe2917bb1e313c7cc809d716c361ee2ddb
  sha256 = 60ce7b65fe711eabd1b77bccb8a1892b4c24c67f8e56bdd96506657bd587a90c

unified_sensitivity_summary
  path = outputs/evaluation/0b05c_corrective_numerical_v0.5/unified_sensitivity_summary_v0.5.json
  git_blob_sha1 = e45202208bc9eb2e311beb11b4fbd7ea16ef7760
  sha256 = 1ae6440141674d7f9f397bee19c17c4bf01b72602a7bc571e51d926d3acd53f0

EV03_metrics
  path = outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5/normative_flat_metrics.json
  git_blob_sha1 = 922ecbee8316ee36cd8a53d3ac52f79fac4cd3ed
  sha256 = 25ad8581e408c89a4562cd56a2e1057ee386866e40b351c33290b4a0575920fd

EV04_metrics
  path = outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_metrics.json
  git_blob_sha1 = 780a005130d1ad68867b290b832c394f8f488a23
  sha256 = 01addbe9d4dbfa84ca8ee016611d7da02eaaa14d68392c99d763c0d9d0cc8656

D1a_metrics
  path = outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_metrics.json
  git_blob_sha1 = 73e062b927d059a9f4e52caab7b785eafb6f2e01
  sha256 = d6cc274c56a4f368c9f422b71a32558e01e87cad3cde7a210ebfd8a080b5a9b2
```

Resultados metricos factuales, pendientes de interpretacion externa:

```makefile
EVAL_cases = 1056
EV03_mrr = 0.04229731726741296
EV03_top_1 = 0.027462121212121212
EV03_recall_at_100 = 0.07102272727272728
EV04_mrr_at_100 = 0.041971783226435376
EV04_mrr_at_200 = 0.043332100440354404
EV04_mrr_101_200_contribution = 0.0013603172139190346
EV04_top_1 = 0.026515151515151516
EV04_recall_at_100 = 0.10132575757575757
EV04_recall_at_200 = 0.3039772727272727
D1a_mrr_at_100 = 0.038087139731859634
D1a_top_1 = 0.000946969696969697
D1a_recall_at_100 = 0.3456439393939394
```

No se formula interpretacion causal, conclusion cientifica ni cierre 0B-05C en
este reporte.

## Execution record

```text
path = outputs/audits/0b05c_attempt06_execution_v0.5/attempt06_execution_record_v0.5.json
git_blob_sha1 = 2f9e62ddd1204885e2f3486033dbc14125603bed
sha256 = 6432de036e9ab3103c9532d69bd307f0c7d2393b0338a6a7f6c6815034e73c74
status = COMPLETED / PENDING_EXTERNAL_RESULT_AUDIT
invocation_count = 1
pipeline_steps_expected = 19
pipeline_steps_completed = 19
retry_performed = false
resume_performed = false
absolute_host_paths = 0
```

## Commit post-ejecucion

```makefile
execution_branch = codex/0b05c-v05-attempt06-execution
post_execution_commit = 6846537602539506c8e90426daad05252cc982b9
post_execution_parent = a9b06b8748316d7f3c403eaa9d55b735e12d96c3
post_execution_tree = 6114b34bae36d9c7bb92c383509e2f6cb6e903c7
post_execution_changed_paths = 49
post_execution_commits = 1
execution_branch_published = true
local_remote_commit_identity = true
tracked_working_tree_clean = true
```

El commit contiene los 48 archivos de los 16 roots producidos y el execution
record externo a esos roots. GitHub acepto la publicacion. Emitio un aviso no
bloqueante porque dos CSV de resultados jerarquicos superan 50 MB, pero ambos
permanecen por debajo del limite individual de 100 MB y la rama remota quedo
publicada en el commit exacto indicado.

## Preservaciones

```makefile
Decision906_patch_scope = EXACTLY_87044110_AND_87045110
EVAL_N = 1056
D1a_retraining = false
MRR_at_100_contract = RATIONAL
MRR_at_200_contract = LEGACY
MRR_101_200_contribution_contract = RATIONAL
EV04_aggregate_rows = 28
EV03_historical_semantics = RECOVERED / PRESERVED
pipeline_topology = 19_STEPS / PRESERVED
v04_partial_roots_used_as_inputs = false
plan_modified = false
article_modified = false
exp11b_modified = false
exp12_modified = false
```

Referencias remotas finales:

```makefile
main = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
origin/main = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
origin/codex/0b05c-v05-attempt06-authorization = a9b06b8748316d7f3c403eaa9d55b735e12d96c3
origin/codex/0b05c-v05-attempt06-execution = 6846537602539506c8e90426daad05252cc982b9
canonical_plan_head = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

```makefile
NO_RETRY = true
NO_RESUME = true
NO_SEPARATE_EV03_EV04_D1A_EXECUTION = true
EXTERNAL_RESULT_AUDIT_REQUIRED = true
```
