### A. Preflight Git y autorizacion

```makefile
origin_main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
authorized_tree = d10ea04228d2754dc8156b0abaedfceee9fe297f
authorization_parent = 8b1444aed67d322714189846f98a3169145ea3d4
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5

attempt_branch = codex/0b05c-numerical-attempt04-v03
attempt_initial_head = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
attempt_initial_commits = 0
attempt_worktree_tracked_clean = true

gate_blob = d4751f418b45dcf190d6c9b06bce68692afac071
authorization_record_blob = 1338201cf4935b9cc7796a2f571c07908248e086
ev03_spec_blob = bba7d853d83460ae99c7587e9d3e2a7ebc55e2c8
ev04_spec_blob = 3a6f9219871777cdd932104d2fe6153a5cbc69eb
d1a_spec_blob = f53221abb1e2afa1a317f410d33febfae91343d1

gate_status = APPROVED / INTEGRATED
authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION
gate_four_numerical_authorizations = AUTHORIZED
spec_EV03_authorization = AUTHORIZED
spec_EV04_authorization = AUTHORIZED
spec_D1A_authorization = AUTHORIZED
attempt04 = AUTHORIZED / NOT_EXECUTED
authorization_record_present = true
runtime_authorization_record_present_before = false
corrective_retrieval_executed_before = false
corrective_metrics_computed_before = false
future_v03_roots_present_before = false

authorization_record_artifact_id = 0b05c_numerical_authorization_record_v0.3
authorization_record_schema_version = 3
authorization_baseline_commit = 8b1444aed67d322714189846f98a3169145ea3d4
baseline_external_audit = PASS / APPROVED_FOR_INTEGRATION
baseline_artifact_count = 4

model_source = LOCAL_EXISTING_COPY
model_copied_to_attempt_worktree = true
model_size_bytes = 470637416
model_sha256 = ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87
model_downloaded = false
model_staged = false
PRE_EXECUTION_IDENTITY = PASS
```

No se borro ni limpio evidencia local/ignored de Attempt01, Attempt02 o Attempt03.

### B. Preflight autorizado

Prueba local read-only de CODEX antes de la unica invocacion numerica:

```makefile
authorized_preflight_status = PASS
authorized_preflight_mode = AUTHORIZED_PREFLIGHT_ONLY
execution_authorization_commit = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
authorization_baseline_commit = 8b1444aed67d322714189846f98a3169145ea3d4
four_gate_authorizations = AUTHORIZED
three_spec_authorizations = AUTHORIZED
attempt04_coherence = AUTHORIZED / NOT_EXECUTED
authorization_record_validation = PASS
dependency_bindings = PASS
model_identity_validation = PASS / READ_ONLY
transition_status = PASS
transition_mode = BASELINE_TO_AUTHORIZED_IMMUTABLE_PROJECTION
transition_allowed_fields_only = true
baseline_projection_sha256 = d9159e6f59bf5103bf0f5b9edbf87109cff789d75e65edf11c76c9362848f1b3
authorized_projection_sha256 = d9159e6f59bf5103bf0f5b9edbf87109cff789d75e65edf11c76c9362848f1b3
future_v03_roots_present = false
preflight_numerical_execution_occurred = false
preflight_side_effects = 0
```

### C. Attempt04

```makefile
command = python -B -m src.experiments.run_0b05c_corrective_numerical_v03 --execute-authorized
execution_invocation_count = 1
start_local = 2026-09-09T13:13:13.1756678-05:00
end_local = 2026-09-09T13:13:24.1845895-05:00
exit_code = 1
last_step_started = 07_EV04_Decision885_control_reproduction_ENRICHED_MRR
last_step_completed = 06_EV03_corrected_evaluation
retry_count = 0
resume_count = 0
separate_component_invocations = 0
authorization_operationally_consumed = true
```

Excepcion exacta:

```text
src.experiments.run_d1a_corrective_0b05c_v01.ContractViolation: Mandatory control reproduction is not exact
```

Origen de la excepcion:

```text
run_0b05c_corrective_numerical_v03.py -> ev04_control -> reproduce("EV04")
evaluate_normative_bm25_corrective_0b05c_v01.py -> compare_control_reproduction()
```

No se reintento, reanudo, reparo ni completo manualmente ninguna etapa.

### D. Controles EV03/EV04

```makefile
EV03_control_step = COMPLETED
EV03_verification_step = PASS_EXACT / COMPLETED
EV03_LOGICAL_INDEX_IDENTITY = EXACT
EV03_ranking_sha256 = d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
EV03_ranking_matches_frozen_hash = true
EV03_case_summary_sha256 = f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0
EV03_case_summary_matches_frozen_hash = true

EV04_control_step = STARTED / FAILED_BEFORE_COMPLETION
EV04_verification_step = NOT_STARTED
EV04_PASS_EXACT = false
EV04_ranking_sha256 = fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662
EV04_ranking_matches_frozen_hash = true
EV04_case_summary_sha256 = 17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634
EV04_case_summary_matches_frozen_hash = true
EV04_combined_mandatory_control = FAIL_CLOSED
EV04_error = Mandatory control reproduction is not exact
```

No se ejecuto una comparacion adicional ni se calcularon metricas faltantes para diagnosticar el fallo.

### E. D1a

```makefile
D1A_step = NOT_STARTED
D1A_execution = false
D1A_corrected_corpus_present = false
D1A_index_present = false
D1A_evaluation_present = false
D1A_runtime_present = false
D1A_17_metrics_extracted = false
model_retrained = false
```

### F. Runtime provenance / manifest / ledger

El paso `01_unified_preflight` creo el runtime authorization record antes del fallo, y se preservo sin modificar:

```makefile
runtime_authorization_record_present = true
runtime_authorization_record_size_bytes = 2301
runtime_authorization_record_sha256 = 09a07533029d372ffbc46957afd0f03034418563d51141727b2a3bf4c8601621
runtime_record_status = PASS
runtime_record_mode = AUTHORIZED_PREFLIGHT_ONLY
runtime_record_execution_authorization_commit = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
runtime_record_authorization_baseline_commit = 8b1444aed67d322714189846f98a3169145ea3d4
runtime_record_authorization_record_blob = 1338201cf4935b9cc7796a2f571c07908248e086
runtime_record_authorized_artifact_count = 4

execution_manifest_present = false
exact_runtime_ledger_present = false
ledger_mismatch_count = NOT_AVAILABLE / STEP_NOT_REACHED
ledger_missing_or_extra_validation = NOT_EXECUTED
unified_sensitivity_summary_present = false
```

### G. Resultados numericos

```makefile
complete_scientific_PASS = false
aggregate_result_extraction_authorized = false
EV03_result_interpretation = NOT_PERFORMED
EV04_result_interpretation = NOT_PERFORMED
D1A_result_interpretation = NOT_PERFORMED
unified_result_interpretation = NOT_AVAILABLE
0B05C_METRIC_IMPACT = NOT_DETERMINED
```

No se interpreto impacto ni se decidio downstream.

### H. Aislamiento

Inventario read-only preservado al terminar la unica invocacion:

```makefile
future_root_count = 16
future_roots_present = 8
future_roots_absent = 8
files_observed_in_future_roots = 17
unexpected_manual_outputs_created = false
roots_deleted_or_cleaned = 0
```

Roots presentes:

1. `data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.3`
2. `outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.3`
3. `data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.3.jsonl`
4. `data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.3`
5. `outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.3`
6. `data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.3`
7. `outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.3`
8. `outputs/audits/0b05c_corrective_numerical_runtime_v0.3`

Roots ausentes:

1. `data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.3.jsonl`
2. `data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.3`
3. `outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.3`
4. `data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.3.jsonl`
5. `data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.3`
6. `outputs/evaluation/d1a_corrective_0b05c_v0.3`
7. `outputs/audits/d1a_corrective_0b05c_runtime_v0.3`
8. `outputs/evaluation/0b05c_corrective_numerical_v0.3`

Archivos preservados con identidad observada:

```text
918504 | b1421f526994b7df001b3d55e4990f92bc4a4c8b8d367a6c37e444b025461557 | data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.3/index.pkl
1488 | 8cf24dc610fa03906802a1a8d6ceac4f79bb840f6fb5be7bf08fd07e7bfd0826 | data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.3/index_metadata.json
497448 | f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0 | outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.3/normative_flat_case_summary.csv
5322 | ec90faa43c52b9d0436dd71933cf73081934c7b757e76d3dde853f528cead389 | outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.3/normative_flat_metrics.json
13145709 | d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015 | outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.3/normative_flat_results.csv
3614411 | 6ecb82fe594853ec8cdd4ffa1c25e198612c988e13b5bd5332afbdfff6a8e0f3 | data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.3.jsonl
918320 | 8f729ab4d841f2c4e52078d4dab6a2dc49049de3a71491d0424595aeaad3ce75 | data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.3/index.pkl
1527 | 4263cfc6d2aa29c17291239ac3c174e2495006a9fa8f1c29275e6b462bc93b32 | data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.3/index_metadata.json
497252 | 7c51c5fc56c5b969191fe2587625d979d5e1d954d5f45ffb76102c5062d29bff | outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.3/normative_flat_case_summary.csv
5318 | ffaf6c48407a90f23b2231322d07117bba6c73d9fcea977b6d70f8caf1c27c06 | outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.3/normative_flat_metrics.json
13135996 | 37577911c843ea97510f0696bdbeb3aa21a993d630772ce3c511dbb546264618 | outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.3/normative_flat_results.csv
6019545 | f828736ea700471c95d2b985bdd969d751cd36c3ca01c407049209010bdbe60b | data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.3/index.pkl
1723 | 299003e3e0efe3c7f00e4d1466ae1c3c528f8b87c31140b4fb175f7c83729fa3 | data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.3/index_metadata.json
607072 | 17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634 | outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.3/normative_hierarchical_case_summary.csv
8167 | b552473c80daf569ba6179457a90833327ed6d9617fb7c7902f7129184944801 | outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.3/normative_hierarchical_metrics.json
85426164 | fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662 | outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.3/normative_hierarchical_results.csv
2301 | 09a07533029d372ffbc46957afd0f03034418563d51141727b2a3bf4c8601621 | outputs/audits/0b05c_corrective_numerical_runtime_v0.3/runtime_authorization_record_v0.3.json
```

```makefile
main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
origin_main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
attempt_branch_head = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
tracked_worktree_clean = true
canonical_plan_head = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
canonical_plan_modified = false
article_modified = false
exp11b_modified_or_started = false
exp12_modified_or_started = false
v01_v02_modified = false
attempt03_failure_record_modified = false
partial_outputs_pushed = false
```

### I. Commit cientifico

```makefile
scientific_commit = NO_SCIENTIFIC_COMMIT
scientific_push = false
attempt_branch_published = false
partial_outputs_versioned = false
```

### J. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/23_RESPUESTA_EJECUTAR_ATTEMPT04_NUMERICO_0B05C_V03.md
admin_commit = SELF / docs: persist prompt 23 attempt04 numerical report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### K. Estado cientifico final

GROUP_2 = EN_CURSO

0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED

0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT04

0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED

ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
