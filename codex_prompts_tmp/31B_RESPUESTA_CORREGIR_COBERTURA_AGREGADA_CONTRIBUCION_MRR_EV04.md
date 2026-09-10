# RESPUESTA PROMPT 31B — COBERTURA AGREGADA EV04 CORREGIDA

## Identidad Git

```makefile
repository = elVladdi/gci-nandina-rag
baseline = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
origin_main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9

rejected_prompt31_candidate = 69a05710295556e365086c52f93933c5b3a2ad1c
rejected_prompt31a_candidate = 9cfbf28f221f2f2761b3a4b7ab60cd870a8557de
rejected_candidates_modified = false

branch = codex/0b05c-v04-complete-preexecution-candidate-v03
candidate_commit = 588962100362174df6486a3c6446276d8749743c
candidate_parent = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
candidate_tree = cc58251fee6d9d0855037f6bb342c3c1259e09d2
scientific_commit_count = 1
prompt31_candidate_is_ancestor = false
prompt31a_candidate_is_ancestor = false
remote_candidate = 588962100362174df6486a3c6446276d8749743c
published = true

canonical_plan_head = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

## Paths Y Blobs

El candidato contiene exactamente los mismos 14 paths v0.4 permitidos y ningún path histórico/v0.3:

| Git blob SHA-1 | Path |
|---|---|
| `82032bbc7d8bc1997f734f0e7565892e795e398e` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json` |
| `9186b0cb40cf3d3d9a4c8552181918037d9385e8` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_gate_hash_ledger_v0.4.json` |
| `eb3fdc0e850f6ad22d9cbebe386bab1260d8af77` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_gate_manifest_v0.4.json` |
| `805f0d60c16fcbead5af1d1929b6be963a692bd8` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json` |
| `053533ff9ea78404848c69790a8c46839444c1f3` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json` |
| `5c3d7d83c447b542049bf290819b4eb790780b43` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json` |
| `61cb524538e11f5f45f67d3b106deea2de7188cd` | `outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json` |
| `8b8b93c1a075fce555eabd4dd301533df89e6a1a` | `src/experiments/evaluate_normative_bm25_corrective_0b05c_v04.py` |
| `54b150a4bdde5f105ce89e7335fd7eaf6db999ed` | `src/experiments/prepare_0b05c_corrective_numerical_gate_v04.py` |
| `c545d32cb6ea6d037e7ee88c9916bff072c3b257` | `src/experiments/run_0b05c_corrective_numerical_v04.py` |
| `a6fc65a27f5dace40cd4651b400e1d6a4ac52bfa` | `src/experiments/run_d1a_corrective_0b05c_v04.py` |
| `d153189592a5407cbdb54ddbd976e6f76d558141` | `tests/test_0b05c_corrective_numerical_gate_v04.py` |
| `257a46d7b01262dbe2e081b8724d101d56a89c20` | `tests/test_0b05c_ev04_mrr_contract_v04.py` |
| `10396f1e5456ea6354d299a3c266115060cd507f` | `tests/test_d1a_corrective_0b05c_runner_v04.py` |

```makefile
changed_path_count = 14
historical_or_v03_paths_modified = false
git_diff_check = PASS
```

## Finding

```makefile
F31B-01 = CLOSED / PASS
```

Se añadió `produce_ev04_aggregate_comparison_v04()`. El helper conserva las 27 filas del `metric_table` canónico e inserta una fila contractual propia para `mrr_101_200_contribution` en la tercera posición. Valida presencia, tipo numérico finito, case-count entero e igualdad exacta de denominadores antes de emitir la comparación.

El runner unificado aplica ahora:

```makefile
EV03_aggregate_helper = legacy / unchanged
EV04_aggregate_helper = produce_ev04_aggregate_comparison_v04
```

## Cobertura Agregada

```makefile
canonical_ev04_key_count = 92
canonical_ev04_metric_table_rows = 27
ev04_aggregate_rows = 28
zero_delta = 28/28 PASS
contribution_position = 3
mrr_legacy_duplicated = false
mrr_at_200_equals_mrr = true
reportable_v04_mrr_metric_omitted = false
unified_summary_accepts_28_rows = PASS
```

Orden exacto de `EV04_AGGREGATE_METRIC_ORDER`:

1. `mrr_at_100`
2. `mrr_at_200`
3. `mrr_101_200_contribution`
4. `top_1`
5. `top_3`
6. `top_5`
7. `top_10`
8. `top_50`
9. `recall_at_50`
10. `recall_at_100`
11. `recall_at_200`
12. `pool_recall_at_200`
13. `exact_at_10`
14. `hs6_at_10`
15. `hs4_at_10`
16. `chapter_at_10`
17. `exact_at_50`
18. `hs6_at_50`
19. `hs4_at_50`
20. `chapter_at_50`
21. `exact_at_100`
22. `hs6_at_100`
23. `hs4_at_100`
24. `chapter_at_100`
25. `exact_at_200`
26. `hs6_at_200`
27. `hs4_at_200`
28. `chapter_at_200`

La auditoría read-only sobre el frozen original case summary de 1056 casos confirmó `92 keys`, `27 metric_table rows`, `28 aggregate rows`, orden exacto y delta `0.0` en las 28 filas.

## Controles Negativos

```makefile
contribution_value_mutation_visible = PASS
contribution_numerator_mutation_visible = PASS
missing_contribution = FAIL_CLOSED
missing_contribution_numerator = FAIL_CLOSED
denominator_mismatch = FAIL_CLOSED
nonfinite_contribution = FAIL_CLOSED
```

Una mutación conjunta de valor y numerador aparece explícitamente en la tercera fila y produce delta no cero. `mrr_definition` y los campos auxiliares no se convierten en filas; el alias legacy `mrr` no se duplica.

## Estado F31A

```makefile
F31A-01 = CLOSED / PASS
F31A-02 = CLOSED / PASS
F31A-03 = CLOSED / PASS
F31A-04 = CLOSED / PASS
```

La transición positiva in-memory, el immutable projection, el adapter D1a v0.4, el baseline agregado canónico EV04 y los tres `specification_status = PREEXECUTION_SPEC_DEFINED` permanecen vigentes.

## Shadow G2 Actualizado

Clasificación: `CODEX_LOCAL_PURE_READ_ONLY_OR_DISPOSABLE_GIT_TEST / NOT_INDEPENDENT_GITHUB_CI`.

Se creó una rama hija local no publicada del commit provisional 31B. El commit sintético cambió únicamente los cuatro artefactos autorizables y añadió el authorization record v0.4 contractual. El modelo congelado se copió solo al worktree ignorado para verificar identidad. Resultado:

```makefile
authorized_preflight_status = PASS
authorized_preflight_mode = AUTHORIZED_PREFLIGHT_ONLY
d1a_read_only_preflight = PASS
d1a_preflight_mode = PREEXECUTION_CLOSED_READONLY
future_roots_present = false
numerical_execution_occurred = false
execute_authorized_called = false
synthetic_authorization_pushed = false
disposable_worktree_deleted = true
disposable_branch_deleted = true
```

## Pruebas

Clasificación: `CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`.

```makefile
tests_v04_relevant = 41/41 PASS
closed_preflight_v04 = PASS / PREEXECUTION_CLOSED_READONLY
real_schema_audit = 92 keys / 27 metric_table rows / PASS
real_aggregate_audit = 28 rows / 28 zero deltas / PASS
shadow_g2_refresh = PASS
git_diff_check = PASS
```

Comando principal:

```text
python -B -m unittest tests.test_0b05c_ev04_mrr_contract_v04 tests.test_0b05c_corrective_numerical_gate_v04 tests.test_d1a_corrective_0b05c_runner_v04
```

Las suites históricas v0.1/v0.2/v0.3 no se repitieron porque sus blobs y paths no cambiaron.

## Estado Final

```makefile
main_modified = false
canonical_plan_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false

authorization_record_v0.4_present = false
V04_AUTHORIZATION = NOT_CREATED
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
retrieval_executed = false
EV03_real_executed = false
EV04_real_executed = false
D1a_real_executed = false
EVAL_real_executed = false
model_inference_executed = false
prospective_roots_present = false
numerical_execution_occurred = false

0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
working_tree_git_status_clean = true
baseline_legacy_eol_path_committed_change = false
BLOCKERS = NONE
```

**RESULTADO FINAL: F31B-01 CERRADO; CANDIDATO v03 PUBLICADO PARA AUDITORÍA EXTERNA; ATTEMPT05 NO AUTORIZADO Y NO EJECUTADO.**
