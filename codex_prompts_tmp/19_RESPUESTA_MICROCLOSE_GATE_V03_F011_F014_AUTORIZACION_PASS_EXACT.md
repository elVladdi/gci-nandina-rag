### A. Preflight

```makefile
origin_main = 60aa7dd8715962f3c3e8b617e8797532529f39ed
candidate_branch = codex/0b05c-corrective-numerical-gate-v03
candidate_previous_head = 815309b2b4ab6df2307d534ba20ec76e8077dcff
candidate_previous_parent = 60aa7dd8715962f3c3e8b617e8797532529f39ed
candidate_previous_tree = 93d9024079385209f3a9306449620743fd9a947c
candidate_previous_compare_main = 1 ahead / 0 behind
candidate_previous_changed_paths = 13
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
authorization_readiness = NOT_AUTHORIZATION_READY
four_v03_numerical_authorizations = NOT_AUTHORIZED
attempt04 = NOT_AUTHORIZED / NOT_EXECUTED
authorization_record_v03_present = false
runtime_authorization_record_v03_present = false
future_v03_roots_present = false
preflight_git = PASS
```

No se borro ni altero evidencia local de Attempt01, Attempt02 o Attempt03.

### B. F011 — Authorization transition

Se implemento un contrato prospectivo fail-closed para la transicion baseline a autorizado:

```makefile
authorization_record_artifact_id = 0b05c_numerical_authorization_record_v0.3
authorization_record_schema_version = 3
baseline_relationship = PROPER_ANCESTOR_OF_AUTHORIZATION_COMMIT
baseline_artifact_count = 4
baseline_artifacts = unified_gate,ev03_spec,ev04_spec,d1a_spec
baseline_binding_fields = path,git_blob_sha1,canonical_git_blob_sha256,canonical_size_bytes
baseline_bindings_recomputed_from_git = true
baseline_bindings_exact_match_required = true
immutable_projection_required = true
structured_transition_proof_returned = true
F011 = CLOSED / PASS
```

La proyeccion del gate permite exclusivamente `gate_status`, `authorization_readiness`, las cuatro autorizaciones numericas, `authorization_record_present` y `attempt04`. En cada spec permite solo su autorizacion propia y `attempt04`. Cualquier cambio simultaneo en contenido cientifico o tecnico, roots, patches, MRR, retrieval, EVAL, BM25, modelo, code bindings, pipeline, runtime ledger o flags de ejecucion falla de forma cerrada.

No se creo ningun authorization record real.

### C. F012 — Spec authorization consistency

`preflight_authorized()` carga EV03, EV04 y D1a antes de cualquier posible side effect y exige:

```makefile
EV03_spec_required_state = AUTHORIZED
EV04_spec_required_state = AUTHORIZED
D1A_spec_required_state = AUTHORIZED
attempt04_required_state = AUTHORIZED / NOT_EXECUTED
attempt04_cross_artifact_coherence = REQUIRED
filesystem_vs_committed_specs_identity = REQUIRED
single_unauthorized_spec_policy = FAIL_CLOSED
F012 = CLOSED / PASS
```

Los tests sinteticos verificaron independientemente el rechazo de EV03, EV04 y D1a cuando una sola autorizacion permanece `NOT_AUTHORIZED`.

### D. F013 — PASS_EXACT orchestration

```makefile
pipeline_step_count = 19
pipeline_order_exact = true
verify_ev03_required_status = PASS_EXACT
verify_ev04_required_status = PASS_EXACT
simple_PASS_at_verify_ev03 = REJECTED
simple_PASS_at_verify_ev04 = REJECTED
final_state_required_predecessors = 18
final_state_required_status = PASS
F013 = CLOSED / PASS
```

No se debilito el orden contractual de los 19 pasos.

### E. F014 — Test PASS_EXACT real

El test sintetico usa ranking y case files identicos, calcula sus SHA-256 observados, compara metricas enriquecidas iguales y pasa por `validate_control_exact()`.

```makefile
synthetic_ranking_identity = EXACT
synthetic_case_summary_identity = EXACT
synthetic_expected_hashes = COMPUTED_FROM_FILES
synthetic_enriched_metrics = EXACT
synthetic_final_status = PASS_EXACT
negative_ranking_test_preserved = true
negative_metric_tests_preserved = true
F014 = CLOSED / PASS
```

### F. Preservacion cientifica

```makefile
EV03_token_policy = DROP_SINGLE_CHARACTER_TOKENS
EV03_k1 = 1.5
EV03_b = 0.75
EV03_depth = 100
EV03_eval_n = 1056

EV04_corpus = FROZEN_HIERARCHICAL_UNCHANGED
EV04_k1 = 1.5
EV04_b = 0.75
EV04_effective_depth = 200
EV04_duplicate_collapse = FIRST_OCCURRENCE_PER_UNIQUE_NANDINA8_CODE
EV04_eval_n = 1056
EV04_enriched_mrr_producer = UNCHANGED

D906_patch_codes = 87044110,87045110
D906_patch_count = 2

D1A_model_size_bytes = 470637416
D1A_model_sha256 = ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87
D1A_metric_count = 17

v03_future_root_count = 16
v03_roots_disjoint_from_v02 = true
evaluator_v03_modified = false
builder_v03_modified = false
d1a_runner_v03_modified = false
v01_v02_modified = false
plan_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false
scientific_drift = false
```

Los seis JSON v0.3 fueron regenerados mediante el preparador canonico. Tres conservaron identidad byte a byte y tres cambiaron por los bindings y el contrato de autorizacion endurecido.

### G. Tests

Ejecucion local, no CI, sin retrieval/EVAL/modelo real:

```makefile
tests_v03 = 26/26 PASS
tests_ev03_recovery = 15 PASS / 0 FAIL / 0 ERROR / 1 SKIP
tests_frozen_ev04 = 17/17 PASS
relevant_tests_total = 58 PASS / 0 FAIL / 0 ERROR / 1 SKIP
ci_executed = false
real_eval_executed = false
retrieval_executed = false
model_loaded = false
```

La suite v0.3 cubre MRR derivado de rows, `PASS_EXACT` real, rechazo de `PASS` simple en EV03/EV04, proper ancestor, schema/artifact id, binding mismatch, cambio cientifico simultaneo, los tres specs no autorizados y permanencia del candidato cerrado.

### H. Detached preflight

El preflight post-commit se ejecuto desde checkout detached limpio del nuevo candidato:

```makefile
detached_head = 8b1444aed67d322714189846f98a3169145ea3d4
detached_preflight_status = PASS
detached_preflight_mode = PREEXECUTION_CLOSED_READONLY
gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
authorization_readiness = NOT_AUTHORIZATION_READY
future_v03_roots_present = false
numerical_execution_occurred = false
corrective_retrieval_executed = false
corrective_metrics_computed = false
attempt04 = NOT_AUTHORIZED / NOT_EXECUTED
working_tree_clean = true
```

No se invoco `preflight_authorized()` con record real ni `--execute-authorized`.

### I. Diff/commit/push

```makefile
branch = codex/0b05c-corrective-numerical-gate-v03
new_head = 8b1444aed67d322714189846f98a3169145ea3d4
parent = 815309b2b4ab6df2307d534ba20ec76e8077dcff
tree = 7543d15b8b692408e5eaa4fc9b93f2a19f42eb78
compare_815309b2_to_new_head = 1 ahead / 0 behind
compare_60aa7dd8_to_new_head = 2 ahead / 0 behind
microclose_changed_path_count = 7
commit_message = fix: harden v0.3 authorization and pass-exact contracts
remote_candidate = 8b1444aed67d322714189846f98a3169145ea3d4
push = PASS / FAST_FORWARD
main_modified = false
origin_main = 60aa7dd8715962f3c3e8b617e8797532529f39ed
```

Paths modificados exclusivamente por este microclose:

1. `docs/0b05c_corrective_numerical_gate_v03.md`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_gate_hash_ledger_v0.3.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_gate_manifest_v0.3.json`
5. `src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py`
6. `src/experiments/run_0b05c_corrective_numerical_v03.py`
7. `tests/test_0b05c_corrective_numerical_gate_v03.py`

### J. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/19_RESPUESTA_MICROCLOSE_GATE_V03_F011_F014_AUTORIZACION_PASS_EXACT.md
admin_commit = SELF / docs: persist prompt 19 v0.3 authorization microclose report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### K. Estado cientifico

GROUP_2 = EN_CURSO

0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_VERSIONED / INTEGRATED

0B05C_V03_RECOVERY_GATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / CORRECTED_F011_F014

0B05C_V03_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY

EV03_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

EV04_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

D1A_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

UNIFIED_0B05C_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

ATTEMPT04 = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
