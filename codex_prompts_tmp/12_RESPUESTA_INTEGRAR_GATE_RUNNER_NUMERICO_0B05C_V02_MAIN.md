### A. Preflight Git

```makefile
integration_branch = main
preintegration_main = 43291c312c2934aae03f3c087dd0a1ae594341b7
preintegration_origin_main = 43291c312c2934aae03f3c087dd0a1ae594341b7
approved_candidate = c44f447cb941c512cd70712cf7c3e4bc670ab05a
candidate_parent = 59dc445d8128dd71f48d26eac66c9ae8d0c21e38
candidate_tree = 41122fe6de833d7be83a2211e99cdd00561bc26e
candidate_chain = 43291c312c2934aae03f3c087dd0a1ae594341b7 -> b0a1e61f70f42aa2048338965cc003e032d3a493 -> 59dc445d8128dd71f48d26eac66c9ae8d0c21e38 -> c44f447cb941c512cd70712cf7c3e4bc670ab05a
compare_candidate_vs_origin_main = 3 ahead / 0 behind
merge_base = 43291c312c2934aae03f3c087dd0a1ae594341b7
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
tracked_worktree_clean = true
git_operation_in_progress = false
preflight_git = PASS
```

Todas las identidades obligatorias coincidieron antes de la integración. No se limpió, borró ni alteró evidencia local/ignored de los Intentos 01/02.

### B. Preintegration validation

Desde el checkout limpio del candidato exacto se ejecutaron únicamente validaciones cerradas de pre-ejecución:

```makefile
preintegration_preflight = PASS
preintegration_preflight_mode = PREEXECUTION_CLOSED_READONLY
authorization_readiness = NOT_AUTHORIZATION_READY
tests_v02 = RUN 56 / PASS 56 / FAIL 0 / ERROR 0 / SKIP 0
future_roots_present = false
numerical_execution_occurred = false
```

Los artefactos versionados conservaron:

```makefile
gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED
EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED
D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED
UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED
authorization_record_present = false
runtime_authorization_record_present = false
corrective_retrieval_executed = false
corrective_metrics_computed = false
0B05C_METRIC_IMPACT = NOT_DETERMINED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```

No se afirmó CI; los resultados son evidencia local de Codex. No se ejecutó `--execute-authorized`.

### C. Diff contractual

El compare completo `43291c312c2934aae03f3c087dd0a1ae594341b7..c44f447cb941c512cd70712cf7c3e4bc670ab05a` contiene exactamente 13 paths y ningún otro:

1. `.gitattributes`
2. `docs/0B05C_CORRECTIVE_NUMERICAL_GATE_V02.md`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_gate_hash_ledger_v0.2.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_gate_manifest_v0.2.json`
6. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/d1a_numerical_execution_spec_v0.2.json`
7. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev03_numerical_execution_spec_v0.2.json`
8. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev04_numerical_execution_spec_v0.2.json`
9. `src/experiments/build_bm25_corrective_0b05c_v02.py`
10. `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py`
11. `src/experiments/run_0b05c_corrective_numerical_v02.py`
12. `src/experiments/run_d1a_corrective_0b05c_v02.py`
13. `tests/test_0b05c_corrective_numerical_gate_v02.py`

```makefile
contractual_path_count = 13
unexpected_paths = 0
candidate_content_edited_during_integration = false
blob_drift = false
```

### D. Integración

```makefile
integration_method = FAST_FORWARD_ONLY
integration_range = 43291c312c2934aae03f3c087dd0a1ae594341b7..c44f447cb941c512cd70712cf7c3e4bc670ab05a
postintegration_main = c44f447cb941c512cd70712cf7c3e4bc670ab05a
integrated_tree = 41122fe6de833d7be83a2211e99cdd00561bc26e
candidate_tree_equals_integrated_tree = true
merge_commit_created = false
additional_commit_created = false
push_target = origin/main
push = PASS / FAST_FORWARD 43291c3..c44f447
```

No hubo squash, cherry-pick, rebase, amend, force-push, edición manual ni regeneración de artefactos.

### E. Postintegration validation

```makefile
postintegration_origin_main = c44f447cb941c512cd70712cf7c3e4bc670ab05a
postintegration_remote_tree = 41122fe6de833d7be83a2211e99cdd00561bc26e
compare_old_main_vs_new_main = 3 commits / 13 paths exactos
postintegration_detached_preflight = PASS
postintegration_detached_preflight_mode = PREEXECUTION_CLOSED_READONLY
postintegration_detached_tests_v02 = RUN 56 / PASS 56 / FAIL 0 / ERROR 0 / SKIP 0
authorization_record_v02_versioned = false
runtime_authorization_record_v02_versioned = false
future_roots_present = false
operational_state_authorized = false
corrective_results_generated = false
corrective_results_versioned = false
numerical_execution_occurred = false
corrective_retrieval_executed = false
corrective_metrics_computed = false
working_tree_clean = true
```

El preflight y la suite se repitieron desde checkout detached del nuevo `origin/main`. Ambos pasaron y no crearon roots científicos persistentes.

### F. Aislamiento

```makefile
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
canonical_plan_modified = false
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
article_modified = false
prompt_branch_modified_during_scientific_integration = false
exp11b_modified = false
exp12_opened = false
authorization_created = false
numerical_sensitivity_executed = false
```

La rama administrativa se tocó únicamente después de finalizar y validar la integración científica, para persistir este reporte en un commit separado.

### G. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/12_RESPUESTA_INTEGRAR_GATE_RUNNER_NUMERICO_0B05C_V02_MAIN.md
admin_commit = SELF / docs: persist prompt 12 integration report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### H. Estado científico

GROUP_2 = EN_CURSO

0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED

0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY

EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
