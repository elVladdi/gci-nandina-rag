### A. Preflight Git y baseline

```makefile
origin_main = 60aa7dd8715962f3c3e8b617e8797532529f39ed
baseline_tree = b846797096d4ca1e1301b4dafbd362c0d8e0d88b
baseline_parent = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
failure_record = outputs/audits/0b05c_attempt03_failclosed_v0.2/attempt03_failure_record_v0.2.json
failure_record_status = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED
authorization_consumed = true
automatic_reuse_authorized = false
attempt04_authorized = false
failure_class = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT
v02_authorization_readiness = ATTEMPT03_CONSUMED / REAUTHORIZATION_REQUIRED
v02_historical_four_authorizations = AUTHORIZED
v02_corrective_retrieval_executed = false
v02_corrective_metrics_computed = false
preflight_git = PASS
```

No se limpio, borro ni altero evidencia local/ignored de Attempt01, Attempt02 o Attempt03.

### B. Root cause binding

La comprobacion estatica read-only confirmo:

```makefile
original_hierarchical_runner_commit = ce239059d748a4baf8a2113df5398f50c0e14a58
initial_hierarchical_outputs_commit = 001580944b417e81634dd6d11a9d2facc9ed29be
gate_c_mrr_microaudit_commit = ef9faefbe9ddc0262e6e2f5b34feb915a69f97
current_hierarchical_runner_git_blob_sha1 = aadbec6bdc5c152def0a7e925d2cf30f16aa4c7d
legacy_metric_table_prefix = mrr
legacy_producer_has_original_mrr_at_100 = false
legacy_producer_has_original_mrr_at_200 = false
frozen_metric_table_prefix = mrr_at_100,mrr_at_200
frozen_top_level_legacy_mrr_equals = mrr_at_200
frozen_mrr_definition = legacy mrr field is MRR@200 because EXP-04 Fase C retrieval_depth=200; comparable flat-vs-hierarchical value is mrr_at_100
attempt03_ev04_ranking_exact = true
attempt03_ev04_case_summary_exact = true
attempt03_ev04_metrics_exact = false
ROOT_CAUSE_BINDING = PASS
```

La correccion no copia el payload esperado al observado. El productor v0.3 reconstruye el contrato enriquecido desde los `case_rows` reproducidos y mantiene la comparacion completa `PASS_EXACT`.

### C. Diseno v0.3

Se crearon cinco modulos prospectivos:

1. `src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py`
2. `src/experiments/build_bm25_corrective_0b05c_v03.py`
3. `src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`
4. `src/experiments/run_0b05c_corrective_numerical_v03.py`
5. `src/experiments/run_d1a_corrective_0b05c_v03.py`

Se crearon seis artefactos contractuales en `outputs/audits/0b05c_corrective_numerical_gate_v0.3/`, una documentacion tecnica y una suite v0.3.

```makefile
v03_future_root_count = 16
v03_roots_disjoint_from_v02 = true
v03_roots_absent = true
v02_partial_roots_policy = MAY_EXIST_AS_LOCAL_EVIDENCE / NEVER_ERROR / NEVER_INPUT / NEVER_REUSED
v02_partial_outputs_deleted = false
authorization_record_v03_present = false
runtime_authorization_record_v03_present = false
dependency_binding_count = 40
circular_dependency = false
```

Los wrappers nuevos de builder y D1a fueron necesarios para aislar identidades, metadata y roots v0.3. No se modifico ningun archivo v0.2 o v0.1.

### D. Contrato EV04 MRR enriquecido

Funcion dedicada:

`src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py:build_ev04_enriched_metrics`

```makefile
observed_source = REPRODUCED_CASE_ROWS
real_execution_denominator = len(case_rows) / REQUIRED_1056
mrr_at_100_numerator = sum(1/rank_ref for 1 <= rank_ref <= 100)
mrr_at_200_numerator = sum(1/rank_ref for 1 <= rank_ref <= 200)
mrr_at_100 = mrr_at_100_numerator / N
mrr_at_200 = mrr_at_200_numerator / N
legacy_mrr = mrr_at_200
legacy_mrr_numerator = mrr_at_200_numerator
legacy_mrr_denominator = N
mrr_101_200_contribution_numerator = mrr_at_200_numerator - mrr_at_100_numerator
mrr_101_200_contribution = mrr_101_200_contribution_numerator / N
metric_table_prefix = mrr_at_100,mrr_at_200
metric_row_schema = metric,numerator,denominator,value
control_validation = RANKING_EXACT + CASE_SUMMARY_EXACT + ENRICHED_METRICS_EXACT
```

Los tests sinteticos cubren ranks dentro y fuera de 100/200, aliases legacy, contribucion 101-200, orden/schema exactos, control enriquecido exacto, fields MRR eliminados/renombrados/reordenados y ranking mismatch con metricas iguales.

### E. Invariantes cientificos

```makefile
EV03_token_policy = DROP_SINGLE_CHARACTER_TOKENS
EV03_k1 = 1.5
EV03_b = 0.75
EV03_depth = 100
EV03_eval_n = 1056
EV03_control = PASS_EXACT / HISTORICAL

EV04_corpus = FROZEN_HIERARCHICAL_UNCHANGED
EV04_k1 = 1.5
EV04_b = 0.75
EV04_effective_depth = 200
EV04_duplicate_collapse = FIRST_OCCURRENCE_PER_UNIQUE_NANDINA8_CODE
EV04_eval_n = 1056
EV04_only_change = ENRICHED_MRR_METRIC_PRODUCER_CONTRACT

D906_patch_codes = 87044110,87045110
D906_patch_count = 2

D1A_model_size_bytes = 470637416
D1A_model_sha256 = ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87
D1A_full_index_rebuild = true
D1A_eval_n = 1056
D1A_metric_count = 17
SCIENTIFIC_DRIFT = false
```

### F. Tests

Ejecucion local, no CI:

```makefile
tests_v03_command = python -B -m unittest tests.test_0b05c_corrective_numerical_gate_v03 -v
tests_v03 = 18/18 PASS

tests_ev03_recovery_command = python -B -m unittest tests.test_0b05c_ev03_historical_builder_recovery_v02 -v
tests_ev03_recovery = 15 PASS / 0 FAIL / 0 ERROR / 1 SKIP

tests_frozen_ev04_command = python -B -m unittest tests.test_normative_bm25_hierarchical_v02 -v
tests_frozen_ev04 = 17/17 PASS

relevant_tests_total = 50 PASS / 0 FAIL / 0 ERROR / 1 SKIP
ci_executed = false
```

Como diagnostico adicional se ejecuto la suite historica `tests.test_0b05c_corrective_numerical_gate_v02`: 50 PASS, 4 FAIL y 2 ERROR. Sus seis non-successes exigen el antiguo estado candidato cerrado v0.2 y son incompatibles con el estado v0.2 posteriormente autorizado y consumido ya integrado en `main`; no corresponden a una regresion v0.3 y no se modificaron esos tests ni artefactos.

### G. Detached preflight

El preflight post-commit se ejecuto en checkout detached limpio del candidato, sin modelo y sin invocar ningun componente numerico:

```makefile
detached_preflight_status = PASS
detached_preflight_mode = PREEXECUTION_CLOSED_READONLY
gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
authorization_readiness = NOT_AUTHORIZATION_READY
future_v03_roots_present = false
v02_partial_roots_reused = false
numerical_execution_occurred = false
corrective_retrieval_executed = false
corrective_metrics_computed = false
runtime_v03_outputs_created = 0
attempt04 = NOT_AUTHORIZED / NOT_EXECUTED
```

No se invoco `--execute-authorized`, retrieval, EV03, EV04, D1a ni el modelo.

### H. Diff/commit/push

```makefile
branch = codex/0b05c-corrective-numerical-gate-v03
commit = 815309b2b4ab6df2307d534ba20ec76e8077dcff
parent = 60aa7dd8715962f3c3e8b617e8797532529f39ed
tree = 93d9024079385209f3a9306449620743fd9a947c
compare = 1 ahead / 0 behind
changed_path_count = 13
commit_message = fix: build 0b05c v0.3 recovery gate for EV04 MRR contract
remote_candidate = 815309b2b4ab6df2307d534ba20ec76e8077dcff
push = PASS / NEW_BRANCH
main_modified = false
origin_main = 60aa7dd8715962f3c3e8b617e8797532529f39ed
```

Changed paths completos:

1. `docs/0b05c_corrective_numerical_gate_v03.md`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_gate_hash_ledger_v0.3.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_gate_manifest_v0.3.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/d1a_numerical_execution_spec_v0.3.json`
6. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev03_numerical_execution_spec_v0.3.json`
7. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev04_numerical_execution_spec_v0.3.json`
8. `src/experiments/build_bm25_corrective_0b05c_v03.py`
9. `src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`
10. `src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py`
11. `src/experiments/run_0b05c_corrective_numerical_v03.py`
12. `src/experiments/run_d1a_corrective_0b05c_v03.py`
13. `tests/test_0b05c_corrective_numerical_gate_v03.py`

Los paths adicionales frente al minimo recomendado son `build_bm25_corrective_0b05c_v03.py` y `run_d1a_corrective_0b05c_v03.py`; ambos aislan roots/metadata v0.3 sin modificar ni reutilizar los wrappers v0.2.

### I. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/18_RESPUESTA_CONSTRUIR_GATE_RECUPERACION_0B05C_V03_EV04_MRR.md
admin_commit = SELF / docs: persist prompt 18 v0.3 EV04 recovery gate report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### J. Estado cientifico

GROUP_2 = EN_CURSO

0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED / HISTORICAL / AUTHORIZATION_CONSUMED

0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_VERSIONED / INTEGRATED

EV04_RECOVERY_ROOT_CAUSE = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT

0B05C_V03_RECOVERY_GATE = CANDIDATE_PENDING_EXTERNAL_AUDIT

0B05C_V03_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY

EV03_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

EV04_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

D1A_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

UNIFIED_0B05C_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

ATTEMPT04 = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
