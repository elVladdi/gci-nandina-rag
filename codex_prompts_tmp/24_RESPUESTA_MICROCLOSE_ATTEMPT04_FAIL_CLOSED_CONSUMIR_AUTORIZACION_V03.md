### A. Preflight Git

```makefile
origin_main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
main_tree = d10ea04228d2754dc8156b0abaedfceee9fe297f
main_parent = 8b1444aed67d322714189846f98a3169145ea3d4
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
prompt23_response_present = true
prompt23_response_blob = f58472d09138c2c8e71f47707470d505530ba219
prompt23_admin_commit = 358ca3c20064304bc87f92eec31e5c9f0857ee32
baseline_identity = PASS
```

El gate v0.3 en `main` fue verificado como `APPROVED / INTEGRATED`, con readiness `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`, las cuatro autorizaciones numericas en `AUTHORIZED`, authorization record presente, runtime authorization record ausente y flags de retrieval/metricas en `false`. El estado `attempt04 = AUTHORIZED / NOT_EXECUTED` estaba presente en el gate y los tres specs. El authorization record v0.3 conserva `authorization_baseline_commit = 8b1444aed67d322714189846f98a3169145ea3d4`.

### B. Evidencia Prompt23 y clasificacion

```makefile
runtime_evidence_classification = CODEX_LOCAL_EXECUTION_REPORT_NOT_INDEPENDENTLY_VERSIONED_RUNTIME_OUTPUTS
command_reported = python -B -m src.experiments.run_0b05c_corrective_numerical_v03 --execute-authorized
invocation_count_reported = 1
exit_code_reported = 1
last_step_completed = 06_EV03_corrected_evaluation
last_step_started = 07_EV04_Decision885_control_reproduction_ENRICHED_MRR
exception_reported = src.experiments.run_d1a_corrective_0b05c_v01.ContractViolation: Mandatory control reproduction is not exact
ev03_control_reported = PASS_EXACT
ev04_ranking_sha256_reported = fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662
ev04_case_summary_sha256_reported = 17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634
ev04_pass_exact_reported = false
d1a_started_reported = false
runtime_authorization_record_local_reported = present
manifest_ledger_unified_summary_reached_reported = false
local_roots_present_reported = 8/16
local_files_preserved_reported = 17
partial_scientific_commit_reported = false
failure_class = EV04_DECISION885_CONTROL_REPRODUCTION_NOT_EXACT_AFTER_V03_MRR_RECOVERY
root_cause_field_status = NOT_YET_ISOLATED
```

Los hechos anteriores se registran exclusivamente como hechos reportados por la evidencia administrativa versionada de Prompt23. No se elevan a CI ni a verificacion Git independiente y no se atribuye el mismatch a ningun subcampo concreto.

### C. Transicion post-Attempt04

```makefile
gate_status = APPROVED / INTEGRATED
authorization_readiness = ATTEMPT04_CONSUMED / REAUTHORIZATION_REQUIRED
gate_attempt04 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ev03_attempt04 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ev04_attempt04 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
d1a_attempt04 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
EV03_NUMERICAL_EXECUTION = AUTHORIZED
EV04_NUMERICAL_EXECUTION = AUTHORIZED
D1A_NUMERICAL_EXECUTION = AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION = AUTHORIZED
authorization_record_present = true
runtime_authorization_record_present = false
corrective_retrieval_executed = false
corrective_metrics_computed = false
```

Las autorizaciones historicas permanecen como evidencia de la autorizacion concedida a Attempt04. La readiness consumida impide su reutilizacion automatica.

### D. Failure record

```makefile
failure_record = outputs/audits/0b05c_attempt04_failclosed_v0.3/attempt04_failure_record_v0.3.json
artifact_id = 0b05c_attempt04_failure_record_v0.3
status = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED
authorization_consumed = true
automatic_reuse_authorized = false
attempt05_authorized = false
partial_outputs = LOCAL_PRESERVED_NOT_VERSIONED
metric_impact = NOT_DETERMINED
downstream_reexecution = NOT_YET_JUSTIFIED
closure = NOT_AUTHORIZED
```

### E. Validacion fail-closed

```makefile
historical_authorizations_preserved = PASS
consumed_readiness_verified = PASS
attempt04_consumed_gate_and_specs = PASS
attempt05_authorized = false
authorization_record_modified = false
authorization_record_blob = 1338201cf4935b9cc7796a2f571c07908248e086
partial_attempt04_outputs_staged_or_versioned = false
plan_or_article_changed = false
preflight_authorized_read_only = REJECTED_AS_REQUIRED
preflight_rejection = src.experiments.prepare_0b05c_corrective_numerical_gate_v03.ContractViolation: Authorized v0.3 gate readiness is invalid
rejection_stage = CONSUMED_AUTHORIZATION_READINESS_BEFORE_ROOT_OR_MODEL_VALIDATION
numerical_component_invoked = false
```

### F. Aislamiento

```makefile
attempt04_local_evidence_deleted_or_modified = false
attempt01_04_ignored_evidence_cleaned = false
v0_4_built = false
attempt05_authorized_or_executed = false
retrieval_executed = false
ev03_executed = false
ev04_executed = false
d1a_executed = false
eval_executed = false
model_inference_executed = false
main_modified = false
canonical_plan_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false
```

### G. Diff/commit/push

```makefile
branch = codex/0b05c-attempt04-failclosed-microclose
candidate_commit = 58ecf012d7c4ed609c3b10787fb583f69700ab02
candidate_parent = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
candidate_tree = bbd5c077cfd6a984670c799387029563ade1faf0
base_to_candidate_commit_count = 1
changed_path_count = 5
push = PASS
remote_candidate = 58ecf012d7c4ed609c3b10787fb583f69700ab02
```

Changed paths:

```text
outputs/audits/0b05c_attempt04_failclosed_v0.3/attempt04_failure_record_v0.3.json
outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json
outputs/audits/0b05c_corrective_numerical_gate_v0.3/d1a_numerical_execution_spec_v0.3.json
outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev03_numerical_execution_spec_v0.3.json
outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev04_numerical_execution_spec_v0.3.json
```

Git blobs:

```makefile
failure_record_blob = 31f1cea387b8630191371f767c03cf13990646b0
gate_blob = 58152fd4806d8efd54ae752cb2790c383417aa37
d1a_spec_blob = 59ccb83b385d7cc6fd157cbe5e22ca7862809116
ev03_spec_blob = b9d047805286edd0522d9279d25058db99328aef
ev04_spec_blob = c4683ab80f24ac07266855e1cc6c1519db94128c
```

### H. Persistencia administrativa

```makefile
admin_branch = codex/prompts-temporary
admin_response_path = codex_prompts_tmp/24_RESPUESTA_MICROCLOSE_ATTEMPT04_FAIL_CLOSED_CONSUMIR_AUTORIZACION_V03.md
admin_commit_scope = RESPONSE_ONLY
admin_push = PASS
```

### I. Estado cientifico

GROUP_2 = EN_CURSO

0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED

0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT04

0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED

0B05C_ATTEMPT04_FAILURE_RECORD = CANDIDATE_PENDING_EXTERNAL_AUDIT

EV04_ATTEMPT04_ROOT_CAUSE_FIELD = NOT_YET_ISOLATED

ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
