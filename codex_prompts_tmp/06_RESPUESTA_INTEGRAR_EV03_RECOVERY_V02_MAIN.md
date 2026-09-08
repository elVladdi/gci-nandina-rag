### A. Preflight Git

```ini
initial_main=06cc75ec173eb6c4b134a45eeb88fe25999f396e
initial_origin_main=06cc75ec173eb6c4b134a45eeb88fe25999f396e
remote_candidate=43291c312c2934aae03f3c087dd0a1ae594341b7
candidate_parent=cef8d7ad58d877e933f8c86b9f721cb214d9058d
candidate_tree=9f21cb79c37cbcdf93006503bb4f888f1acfc975
intermediate_parent=06cc75ec173eb6c4b134a45eeb88fe25999f396e
intermediate_tree=281806931941e526e590f7d48c8aca01adde600e
ahead=2
behind=0
git_operation_in_progress=false
validation_worktree_tracked_clean=true
main_worktree_tracked_clean=true
```

La cadena verificada antes de cualquier escritura fue exactamente:

`06cc75ec173eb6c4b134a45eeb88fe25999f396e -> cef8d7ad58d877e933f8c86b9f721cb214d9058d -> 43291c312c2934aae03f3c087dd0a1ae594341b7`.

### B. Validacion preintegracion

El replay se ejecuto en un checkout detached limpio del candidato, sin escribir en el repositorio:

```ini
exit_code=0
status=PASS
mode=COMMITTED_REPLAY_READONLY
base_commit_ancestor=true
tracked_worktree_clean=true
canonical_dependency_bindings.status=PASS
canonical_dependency_bindings.checked=13
canonical_dependency_bindings.mismatch_count=0
LOGICAL_INDEX_IDENTITY=EXACT
EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT
ranking_bytes_exact=true
case_summary_bytes_exact=true
full_metrics_exact=true
repo_files_created=0
repo_files_modified=0
repo_files_deleted=0
audit_artifacts_modified=false
future_numerical_roots_present=false
ledger_mismatch_count=0
```

Suite recovery preintegracion:

```ini
RUN=16
PASS=16
FAIL=0
ERROR=0
SKIP=0
```

### C. Diff scope

El compare completo `06cc75ec173eb6c4b134a45eeb88fe25999f396e..43291c312c2934aae03f3c087dd0a1ae594341b7` contiene exactamente estos 12 paths:

```text
.gitattributes
docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_corrective_numerical_gate_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_manifest_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_corrective_execution_spec_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_decision885_control_reproduction_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_historical_builder_provenance_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_logical_index_identity_v0.2.json
src/experiments/build_bm25_ev03_historical_recovered_v02.py
src/experiments/verify_ev03_historical_builder_recovery_v02.py
tests/test_0b05c_ev03_historical_builder_recovery_v02.py
```

```ini
plan_maestro_paths_present=false
article_paths_present=false
exp11b_paths_present=false
exp12_paths_present=false
future_numerical_root_paths_present=false
intento_01_02_output_paths_present=false
scope_exact=true
```

### D. Integracion

```ini
integration_method=FAST_FORWARD_ONLY
command=git merge --ff-only origin/codex/0b05c-ev03-historical-builder-recovery-v02
final_HEAD=43291c312c2934aae03f3c087dd0a1ae594341b7
final_tree=9f21cb79c37cbcdf93006503bb4f888f1acfc975
merge_commit_created=false
squash=false
rebase=false
cherry_pick=false
amend=false
force_push=false
content_changed_beyond_candidate=false
push_command=git push origin main
push_result=PASS
```

El push remoto fue un fast-forward normal de `06cc75ec...` a `43291c3...` y publico unicamente `main`.

### E. Validacion postintegracion

Replay postintegracion sobre el worktree limpio de `main`:

```ini
exit_code=0
status=PASS
mode=COMMITTED_REPLAY_READONLY
base_commit_ancestor=true
tracked_worktree_clean=true
canonical_dependency_bindings.status=PASS
canonical_dependency_bindings.checked=13
canonical_dependency_bindings.mismatch_count=0
LOGICAL_INDEX_IDENTITY=EXACT
EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT
ranking_bytes_exact=true
case_summary_bytes_exact=true
full_metrics_exact=true
repo_files_created=0
repo_files_modified=0
repo_files_deleted=0
audit_artifacts_modified=false
future_numerical_roots_present=false
ledger_mismatch_count=0
```

Suite recovery postintegracion:

```ini
RUN=16
PASS=16
FAIL=0
ERROR=0
SKIP=0
```

Estado remoto y local final:

```ini
main=43291c312c2934aae03f3c087dd0a1ae594341b7
origin/main=43291c312c2934aae03f3c087dd0a1ae594341b7
integrated_tree=9f21cb79c37cbcdf93006503bb4f888f1acfc975
tree_identity=true
tracked_worktree_clean=true
```

### F. Aislamiento

```ini
canonical_plan_branch=docs/plan-maestro-temporal-2026-08-31
canonical_plan_head=f8b37c7f2b5d612ccf2cf9c4779cab7008362fc6
canonical_plan_modified=false
article_branch=article/main-manuscript
article_head=254b1e6df736fa9938ac86a515d65b36f4d361c5
article_modified=false
exp11b_modified=false
exp12_modified=false
v0.1_evidence_modified=false
candidate_branch_preserved=true
candidate_remote_head=43291c312c2934aae03f3c087dd0a1ae594341b7
numerical_runner_v0.2_present=false
authorization_record_v0.2_present=false
future_numerical_roots_v0.2_present=false
corrective_metrics_computed=false
numerical_execution_occurred=false
```

No se ejecuto EV03 corrected, EV04 corrected, D1a numerical ni el runner unificado. No se limpio, borro ni sobrescribio evidencia de los Intentos 01/02. No se actualizo Plan Maestro ni `article/main-manuscript`.

El bundle integrado mantiene:

```ini
gate_scope=EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY
authorization_readiness=NOT_AUTHORIZATION_READY
EV03_NUMERICAL_EXECUTION=NOT_AUTHORIZED
EV04_NUMERICAL_EXECUTION=NOT_AUTHORIZED
D1A_NUMERICAL_EXECUTION=NOT_AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION=NOT_AUTHORIZED
corrective_retrieval_executed=false
corrective_metrics_computed=false
runtime_authorization_record_present=false
```

### G. Estado de integracion

`EV03_HISTORICAL_RECOVERY_V02 = APPROVED / VERSIONED / INTEGRATED`

### H. Estado cientifico

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`
