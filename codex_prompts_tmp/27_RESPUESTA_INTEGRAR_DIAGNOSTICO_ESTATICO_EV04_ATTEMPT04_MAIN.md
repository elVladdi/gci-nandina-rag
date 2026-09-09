### A. Preflight Git

```makefile
pre_integration_main = 58ecf012d7c4ed609c3b10787fb583f69700ab02
pre_integration_origin_main = 58ecf012d7c4ed609c3b10787fb583f69700ab02
pre_integration_main_tree = bbd5c077cfd6a984670c799387029563ade1faf0
pre_integration_main_parent = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
approved_candidate = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
candidate_parent = 58ecf012d7c4ed609c3b10787fb583f69700ab02
candidate_tree = 7c8199733df071eee299d80a57456223fb2834ad
merge_base = 58ecf012d7c4ed609c3b10787fb583f69700ab02
compare_main_candidate = 1_ahead / 0_behind
candidate_commit_count = 1
candidate_changed_path_count = 1
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
preflight_identity = PASS
```

El unico path del candidato fue:

```text
outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json
```

```makefile
candidate_diagnosis_blob = fca5712c615960b41cb2741c2164f19fc00df9dd
candidate_scope = PASS / EXACTLY_1_NEW_PATH
```

### B. Verificacion del candidato

```makefile
artifact_id = 0b05c_ev04_attempt04_metric_mismatch_diagnosis_v0.3
baseline_commit = 58ecf012d7c4ed609c3b10787fb583f69700ab02
attempt04_runtime_outputs_used = false
attempt05_authorized = false
retrieval_executed = false
evaluation_runner_executed = false
model_inference_executed = false
metric_impact = NOT_DETERMINED
closure = NOT_AUTHORIZED
root_cause_field_status = ISOLATED_FROM_VERSIONED_FROZEN_ARTIFACTS
root_cause_class = FLOAT_ACCUMULATION_PATH_MISMATCH
deep_diff_mismatch_count = 6
run_metadata_metrics_equal_metrics_artifact = true
source_bindings_all_match_expected = true
static_comparator_metrics_exact_before_call = false
static_comparator_outcome = RAISED_CONTRACT_VIOLATION
historical_arithmetic_source_overattributed = false
candidate_read_only_verification = PASS
```

Los seis paths causales verificados fueron exactamente:

```text
$.metric_table[0].numerator
$.metric_table[0].value
$.mrr_101_200_contribution
$.mrr_101_200_contribution_numerator
$.mrr_at_100
$.mrr_at_100_numerator
```

El artefacto preserva expresamente que la evidencia versionada no establece que funcion o libreria historica produjo el valor congelado un ULP menor.

### C. Integracion

```makefile
integration_method = git merge --ff-only origin/codex/0b05c-ev04-attempt04-static-metric-diagnosis-v03
integration_from = 58ecf012d7c4ed609c3b10787fb583f69700ab02
integration_to = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
merge_commit_created = false
squash = false
cherry_pick = false
rebase = false
amend = false
force_push = false
files_edited_during_integration = false
artifact_regenerated = false
additional_main_commit = false
main_push = PASS / NORMAL_FAST_FORWARD_ONLY
```

### D. Validacion post-integracion

```makefile
post_integration_main = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
post_integration_origin_main = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
integrated_tree = 7c8199733df071eee299d80a57456223fb2834ad
candidate_vs_origin_main_diff = EMPTY
tree_identity = true
old_main_to_new_main = 1_ahead / 0_behind
integrated_commit_count = 1
integrated_changed_path_count = 1
integrated_path = outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json
integrated_diagnosis_blob = fca5712c615960b41cb2741c2164f19fc00df9dd
failure_record_modified = false
gate_specs_authorization_record_modified = false
partial_attempt04_outputs_versioned = false
attempt05_authorized = false
v0_4_present = false
canonical_plan_after_integration = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article_after_integration = 254b1e6df736fa9938ac86a515d65b36f4d361c5
working_tree_tracked_clean = true
```

### E. Aislamiento

```makefile
diagnosis_reexecuted = false
additional_eval_calculation_executed = false
retrieval_executed = false
indexes_built = false
ev03_executed = false
ev04_executed = false
d1a_executed = false
real_eval_executed = false
model_inference_executed = false
v0_4_built = false
attempt05_authorized_or_executed = false
metric_impact_decided = false
downstream_decided = false
0b05c_closed = false
canonical_plan_modified = false
article_modified = false
exp11b_modified_or_opened = false
exp12_modified_or_opened = false
```

### F. Persistencia administrativa

```makefile
admin_branch = codex/prompts-temporary
admin_response_path = codex_prompts_tmp/27_RESPUESTA_INTEGRAR_DIAGNOSTICO_ESTATICO_EV04_ATTEMPT04_MAIN.md
prompt27_modified = false
previous_responses_modified = false
admin_commit_scope = RESPONSE_ONLY
admin_push = PASS
```

### G. Estado cientifico

GROUP_2 = EN_CURSO

0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED

0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04

EV04_ATTEMPT04_STATIC_DIAGNOSIS = VERSIONED / INTEGRATED

EV04_ATTEMPT04_ROOT_CAUSE_FIELD = ISOLATED_FROM_VERSIONED_FROZEN_ARTIFACTS

EV04_ATTEMPT04_ROOT_CAUSE_CLASS = FLOAT_ACCUMULATION_PATH_MISMATCH

ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
