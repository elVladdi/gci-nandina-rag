### A. Preflight Git

```makefile
origin_main = c44f447cb941c512cd70712cf7c3e4bc670ab05a
baseline_tree = 41122fe6de833d7be83a2211e99cdd00561bc26e
baseline_parent = 59dc445d8128dd71f48d26eac66c9ae8d0c21e38
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
baseline_gate_present = true
baseline_gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
baseline_authorization_readiness = NOT_AUTHORIZATION_READY
baseline_four_authorizations = NOT_AUTHORIZED
baseline_specs_authorization = NOT_AUTHORIZED
baseline_authorization_record_present = false
baseline_runtime_authorization_record_present = false
baseline_future_roots_present = false
baseline_corrective_retrieval_executed = false
baseline_corrective_metrics_computed = false
preflight_git = PASS
```

Todas las identidades y estados obligatorios coincidieron antes de escribir. No se limpió ni alteró evidencia local/ignored de los Intentos 01/02.

### B. Baseline externo aprobado

```makefile
authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
baseline_external_audit = PASS / APPROVED_FOR_INTEGRATION
0B05C_NUMERICAL_GATE_V02 = PASS / APPROVED / VERSIONED / INTEGRATED
baseline_tests_v02 = RUN 56 / PASS 56 / FAIL 0 / ERROR 0 / SKIP 0
```

La evidencia de los 56 tests corresponde al bloque de integración previamente ejecutado y auditado sobre el mismo baseline exacto. No se afirmó CI.

### C. Authorization transition

La transición modificó exclusivamente los campos permitidos:

Gate unificado:

1. `gate_status`: `CANDIDATE_PENDING_EXTERNAL_AUDIT` -> `APPROVED / INTEGRATED`.
2. `authorization_readiness`: `NOT_AUTHORIZATION_READY` -> `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`.
3. `authorization.EV03_NUMERICAL_EXECUTION`: `NOT_AUTHORIZED` -> `AUTHORIZED`.
4. `authorization.EV04_NUMERICAL_EXECUTION`: `NOT_AUTHORIZED` -> `AUTHORIZED`.
5. `authorization.D1A_NUMERICAL_EXECUTION`: `NOT_AUTHORIZED` -> `AUTHORIZED`.
6. `authorization.UNIFIED_0B05C_NUMERICAL_EXECUTION`: `NOT_AUTHORIZED` -> `AUTHORIZED`.
7. `authorization.authorization_record_present`: `false` -> `true`.

Specs:

8. EV03 `authorization.EV03_NUMERICAL_EXECUTION`: `NOT_AUTHORIZED` -> `AUTHORIZED`.
9. EV04 `authorization.EV04_NUMERICAL_EXECUTION`: `NOT_AUTHORIZED` -> `AUTHORIZED`.
10. D1a `authorization.D1A_NUMERICAL_EXECUTION`: `NOT_AUTHORIZED` -> `AUTHORIZED`.

Permanecieron sin cambio `corrective_retrieval_executed=false`, `corrective_metrics_computed=false`, `runtime_authorization_record_present=false`, los tres estados D1a de creación/cómputo en `false`, la proyección científica inmutable y todos los contratos de ejecución.

### D. Authorization record

```makefile
artifact_id = 0b05c_numerical_authorization_record_v0.2
schema_version = 2
authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
baseline_external_audit = PASS / APPROVED_FOR_INTEGRATION
record_keys_exact = true
baseline_artifact_keys_exact = unified_gate, ev03_spec, ev04_spec, d1a_spec
```

Bindings exactos de los artefactos en el baseline `c44f447...`:

```makefile
unified_gate_path = outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json
unified_gate_git_blob_sha1 = a543c656b15b1c828c8526a5804f4af4efdb0718
unified_gate_canonical_git_blob_sha256 = 772ae932536757b5b9d7ef0f28c430431544d031aa099141d50d9dc9cf3824d9
unified_gate_canonical_size_bytes = 26638

ev03_spec_path = outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev03_numerical_execution_spec_v0.2.json
ev03_spec_git_blob_sha1 = 1e6440894dfd3ec4770bf2936e1f2ec14e156ecc
ev03_spec_canonical_git_blob_sha256 = d790c0fad5b93d6c6969b800fb95320a0f2d62454821558e17a04c2177011da3
ev03_spec_canonical_size_bytes = 20601

ev04_spec_path = outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev04_numerical_execution_spec_v0.2.json
ev04_spec_git_blob_sha1 = d122238645c155b561a15667f900b785e6863ebc
ev04_spec_canonical_git_blob_sha256 = e0cbdf2d4994969f3e1a5ead61e8d75fdde769547721758d49ed34039be6849c
ev04_spec_canonical_size_bytes = 26995

d1a_spec_path = outputs/audits/0b05c_corrective_numerical_gate_v0.2/d1a_numerical_execution_spec_v0.2.json
d1a_spec_git_blob_sha1 = e40eb6eb385f614f4581d23537a8751351de5009
d1a_spec_canonical_git_blob_sha256 = a45f10659797a6c734f8416a0a09b0038636cf70893279d4d2c53ed78aff3eb3
d1a_spec_canonical_size_bytes = 16940
```

Identidad del authorization record comprometido en el candidato:

```makefile
authorization_record_git_blob_sha1 = 5d963214a8ab0a614dc6917a71b0136397625fe9
authorization_record_canonical_git_blob_sha256 = 06403316f34eafa70af63f07061aeb21d83611ba285f7cc4e4c1108abfaddfbe
authorization_record_canonical_size_bytes = 1638
```

### E. Immutable transition validation

```makefile
baseline_is_proper_ancestor = true
load_authorization_transition_from_git = PASS
validate_authorization_transition = PASS
immutable_authorization_projection_equal = true
baseline_artifact_binding_validation = PASS
allowed_diff_only = PASS
unexpected_changed_fields = 0
```

El record fue leído desde el `HEAD` candidato y sus cuatro bindings fueron recalculados contra el baseline comprometido. No se usaron hashes del candidato como identidades baseline.

### F. Authorized preflight

```makefile
authorized_preflight_status = PASS
authorized_preflight_mode = AUTHORIZED_PREFLIGHT_ONLY
execution_authorization_commit = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
four_authorizations = AUTHORIZED
model_path = models/text2trade_mnrl_v0.2/model.safetensors
model_size_bytes = 470637416
model_sha256 = ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87
future_roots_present = false
runtime_authorization_record_present = false
corrective_retrieval_executed = false
corrective_metrics_computed = false
corrective_results_present = false
numerical_execution_occurred = false
```

El modelo congelado local fue verificado por size y SHA-256. Se invocó únicamente `preflight_authorized()` de forma read-only. No se invocó `execute_authorized()`, `--execute-authorized`, retrieval, EVAL, D1a ni Attempt03. La copia temporal exacta usada en el worktree de validación se retiró después del preflight.

### G. Diff y aislamiento

El compare contra `c44f447...` contiene exactamente cinco paths:

1. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_numerical_authorization_record_v0.2.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/d1a_numerical_execution_spec_v0.2.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev03_numerical_execution_spec_v0.2.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev04_numerical_execution_spec_v0.2.json`

```makefile
changed_path_count = 5
unexpected_paths = 0
main = c44f447cb941c512cd70712cf7c3e4bc670ab05a
origin_main = c44f447cb941c512cd70712cf7c3e4bc670ab05a
main_modified = false
canonical_plan_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false
v01_artifacts_modified = false
runtime_outputs_created = false
```

### H. Commit candidato

```makefile
branch = codex/0b05c-numerical-authorization-v02
commit = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
parent = c44f447cb941c512cd70712cf7c3e4bc670ab05a
tree = 4d0703327c2d9e05ecf19fd04f5a8c7d808bd0f6
commit_message = chore: authorize single 0b05c v0.2 numerical execution
compare_vs_main = 1 ahead / 0 behind
remote_candidate = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
push = PASS / NEW_BRANCH
working_tree_clean = true
```

No se hizo merge a `main`, rebase, amend, squash, cherry-pick ni force-push.

### I. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/13_RESPUESTA_CONSTRUIR_AUTORIZACION_NUMERICA_0B05C_V02.md
admin_commit = SELF / docs: persist prompt 13 authorization candidate report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### J. Estado científico

GROUP_2 = EN_CURSO

0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED

0B05C_V02_AUTHORIZATION_CANDIDATE = CREATED / PENDING_EXTERNAL_AUDIT

0B05C_V02_AUTHORIZATION_READINESS = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION (CANDIDATE_ONLY)

EV03_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED (CANDIDATE_ONLY)

EV04_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED (CANDIDATE_ONLY)

D1A_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED (CANDIDATE_ONLY)

UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = AUTHORIZED / NOT_EXECUTED (CANDIDATE_ONLY)

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
