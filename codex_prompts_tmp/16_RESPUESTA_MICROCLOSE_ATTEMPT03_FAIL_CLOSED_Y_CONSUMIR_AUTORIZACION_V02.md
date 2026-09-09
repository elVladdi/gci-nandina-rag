### A. Preflight Git

```makefile
origin_main = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
main_tree = 4d0703327c2d9e05ecf19fd04f5a8c7d808bd0f6
main_parent = c44f447cb941c512cd70712cf7c3e4bc670ab05a
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
gate_status = APPROVED / INTEGRATED
authorization_readiness_initial = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION
gate_four_authorizations = AUTHORIZED
authorization_record_present = true
authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
corrective_retrieval_executed = false
corrective_metrics_computed = false
attempt03_failure_record_present_on_main = false
attempt03_scientific_commit_present_before_microclose = false
attempt03_partial_outputs_committed = false
```

Evidencia administrativa Prompt15 verificada directamente en Git:

```makefile
prompt15_admin_commit = a449a3127a52e4b17948fd7fe6a3040a24f02ebd
prompt15_response_path = codex_prompts_tmp/15_RESPUESTA_EJECUTAR_ATTEMPT03_NUMERICO_0B05C_V02.md
prompt15_response_git_blob_sha1 = c83b7d9004433ee1f369989dd6a5c7b9800c8e0d
prompt15_evidence_classification = ADMINISTRATIVE_EXTERNAL_EVIDENCE / NOT_SCIENTIFIC_BRANCH
preflight_git = PASS
```

No se limpió, borró ni alteró evidencia local/ignored de Attempt01, Attempt02 o Attempt03.

### B. Auditoría estática de causa raíz

La cadena histórica y sus identidades fueron verificadas directamente en Git:

```makefile
original_hierarchical_runner_commit = ce239059d748a4baf8a2113df5398f50c0e14a58
original_hierarchical_runner_subject = feat: add EXP-04 hierarchical normative BM25 v0.2 runner
initial_hierarchical_outputs_commit = 001580944b417e81634dd6d11a9d2facc9ed29be
initial_hierarchical_outputs_parent = ce239059d748a4baf8a2113df5398f50c0e14a58
gate_c_mrr_microaudit_commit = ef9faefbe9ddc0262e6e2f5b34feb915a69f97
current_hierarchical_runner_git_blob_sha1 = aadbec6bdc5c152def0a7e925d2cf30f16aa4c7d
corrective_evaluator_git_blob_sha1 = c6f4121fe5f5f50e71e27eb4cf1e28eb8986d062
```

`metrics_from_cases()` en `ce239059...` inicia su tabla con una única fila legacy `mrr`; el source actual conserva esa misma producción y no genera originalmente filas `mrr_at_100`/`mrr_at_200`.

El commit `0015809...` versionó los outputs jerárquicos iniciales. El commit `ef9faef...` modificó los artefactos congelados `normative_hierarchical_metrics.json` y `run_metadata.json`, junto con microaudit, comparaciones, tests y documentación. Su diff no incluye `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`.

El `run_metadata.json` congelado actual fue verificado con:

```makefile
metric_table_prefix = mrr_at_100,mrr_at_200
mrr_at_100_fields_present = true
mrr_at_200_fields_present = true
mrr_101_200_contribution_fields_present = true
mrr_definition_present = true
```

El corrective evaluator fija literalmente `metrics_equal = expected_metrics == actual_metrics` y exige esa igualdad completa antes de aceptar el control. La evidencia Prompt15 reportó hashes/bytes exactos para ranking y case summary, pero `metrics_exact=false`.

```makefile
ranking_or_case_drift_established = false
metric_schema_drift_established = true
failure_class = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT
STATIC_ROOT_CAUSE_AUDIT = PASS
```

### C. Failure record

Se creó el registro científico mínimo:

`outputs/audits/0b05c_attempt03_failclosed_v0.2/attempt03_failure_record_v0.2.json`

```makefile
artifact_id = 0b05c_attempt03_failure_record_v0.2
schema_version = 1
attempt_id = ATTEMPT03
authorization_commit = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
status = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED
authorization_consumed = true
automatic_reuse_authorized = false
attempt04_authorized = false
exit_code_reported = 1
completed_steps_reported = 6
total_pipeline_steps = 19
last_completed_step_reported = 06_EV03_corrected_evaluation
last_started_step_reported = 07_EV04_Decision885_control_reproduction
failure_class = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT
runtime_partial_outputs = LOCAL_PRESERVED_NOT_VERSIONED
metric_impact = NOT_DETERMINED
downstream_reexecution = NOT_YET_JUSTIFIED
closure = NOT_AUTHORIZED
```

La excepción reportada quedó congelada exactamente como:

```text
src.experiments.run_d1a_corrective_0b05c_v01.ContractViolation: Mandatory control reproduction is not exact
```

El record se enlaza al response Prompt15 mediante rama, commit `a449a3127a52e4b17948fd7fe6a3040a24f02ebd`, path y blob `c83b7d9004433ee1f369989dd6a5c7b9800c8e0d`, clasificado como `CODEX_LOCAL_EXECUTION_REPORT_NOT_INDEPENDENTLY_VERSIONED_RUNTIME_OUTPUTS`. No se incorporaron ni versionaron hashes de outputs parciales locales.

### D. Consumo de autorización v0.2

La única modificación del gate fue:

```makefile
authorization_readiness_before = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION
authorization_readiness_after = ATTEMPT03_CONSUMED / REAUTHORIZATION_REQUIRED
gate_other_fields_changed = false
historical_four_authorizations = AUTHORIZED
authorization_record_present = true
corrective_retrieval_executed = false
corrective_metrics_computed = false
runtime_authorization_record_present = false
```

Sobre el commit candidato se invocó únicamente `preflight_authorized()` de forma read-only, sin modelo y sin ejecutar componentes:

```makefile
preflight_authorized = BLOCKED / PASS_EXPECTED_FAIL_CLOSED
exception_type = src.experiments.prepare_0b05c_corrective_numerical_gate_v02.ContractViolation
exception = Authorized gate readiness is invalid
future_roots_before = 0
future_roots_after = 0
side_effects = false
authorization_reuse_blocked = true
```

No se invocó `--execute-authorized`, retrieval, EV03, EV04, D1a ni modelo. No se reintentó Attempt03 y no se construyó ni autorizó Attempt04.

### E. Diff y aislamiento

El compare `41d3259ff09d8a63cc3a12a7f11a146a603ee3ef..60aa7dd8715962f3c3e8b617e8797532529f39ed` contiene exactamente dos paths:

1. `outputs/audits/0b05c_attempt03_failclosed_v0.2/attempt03_failure_record_v0.2.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`

```makefile
changed_path_count = 2
unexpected_paths = 0
main = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
origin_main = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
main_modified = false
canonical_plan_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false
v01_artifacts_modified = false
attempt03_partial_outputs_versioned = false
attempt03_local_evidence_modified = false
model_copied_or_staged = false
```

### F. Commit candidato

```makefile
branch = codex/0b05c-attempt03-failclosed-microclose
commit = 60aa7dd8715962f3c3e8b617e8797532529f39ed
parent = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
tree = b846797096d4ca1e1301b4dafbd362c0d8e0d88b
commit_message = chore: record attempt03 fail-closed and consume v0.2 authorization
compare_vs_main = 1 ahead / 0 behind
remote_candidate = 60aa7dd8715962f3c3e8b617e8797532529f39ed
push = PASS / NEW_BRANCH
working_tree_clean = true
```

No se hizo merge a `main`, rebase, amend, squash, cherry-pick ni force-push.

### G. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/16_RESPUESTA_MICROCLOSE_ATTEMPT03_FAIL_CLOSED_Y_CONSUMIR_AUTORIZACION_V02.md
admin_commit = SELF / docs: persist prompt 16 attempt03 fail-closed microclose report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### H. Estado científico

GROUP_2 = EN_CURSO

0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED (HISTORICAL)

0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT03 (CANDIDATE_MICROCLOSE)

0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_CANDIDATE

EV04_RECOVERY_ROOT_CAUSE = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT

0B05C_V03_RECOVERY_GATE = NOT_YET_BUILT / NOT_AUTHORIZED

ATTEMPT04 = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
