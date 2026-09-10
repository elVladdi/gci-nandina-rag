# RESPUESTA PROMPT 31A — CANDIDATO v0.4 CORREGIDO

## Identidad Git

```makefile
repository = elVladdi/gci-nandina-rag
baseline = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
origin_main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
rejected_candidate = 69a05710295556e365086c52f93933c5b3a2ad1c
rejected_branch = codex/0b05c-v04-complete-preexecution-candidate
rejected_candidate_modified = false

branch = codex/0b05c-v04-complete-preexecution-candidate-v02
candidate_commit = 9cfbf28f221f2f2761b3a4b7ab60cd870a8557de
candidate_parent = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
candidate_tree = c16f2e6df6b7791636cedb7516edc7a081421729
scientific_commit_count = 1
rejected_candidate_is_ancestor = false
remote_candidate = 9cfbf28f221f2f2761b3a4b7ab60cd870a8557de
published = true
```

El candidato corregido fue construido directamente desde el baseline protegido. El diff del candidato rechazado se llevó al índice sin crear un commit intermedio; `69a057...` no forma parte de la ancestry de la rama v02.

## Paths Y Blobs

El diff contra `ba4bd293...` contiene exactamente 14 paths nuevos:

| Git blob SHA-1 | Path |
|---|---|
| `3aa1566aaf11ada66986ee61344f2fa7c816657e` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json` |
| `c9483bd8de06c05d30881687dbbf69151d9c6321` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_gate_hash_ledger_v0.4.json` |
| `136876968dd3f854b167e0b67c57280b725162ea` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_gate_manifest_v0.4.json` |
| `805f0d60c16fcbead5af1d1929b6be963a692bd8` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json` |
| `053533ff9ea78404848c69790a8c46839444c1f3` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json` |
| `5c3d7d83c447b542049bf290819b4eb790780b43` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json` |
| `12f8d8b67247cf492acfdb2b9c52ff35098fffbd` | `outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json` |
| `57b88a3da6b0b61918e4a20398d20ab7a26cb06e` | `src/experiments/evaluate_normative_bm25_corrective_0b05c_v04.py` |
| `54b150a4bdde5f105ce89e7335fd7eaf6db999ed` | `src/experiments/prepare_0b05c_corrective_numerical_gate_v04.py` |
| `ce883250fae437809e47068c3574c8f6131ff768` | `src/experiments/run_0b05c_corrective_numerical_v04.py` |
| `a6fc65a27f5dace40cd4651b400e1d6a4ac52bfa` | `src/experiments/run_d1a_corrective_0b05c_v04.py` |
| `d153189592a5407cbdb54ddbd976e6f76d558141` | `tests/test_0b05c_corrective_numerical_gate_v04.py` |
| `862ec0fa965cbfd4654b5842c1a0ee49fb2d9a10` | `tests/test_0b05c_ev04_mrr_contract_v04.py` |
| `10396f1e5456ea6354d299a3c266115060cd507f` | `tests/test_d1a_corrective_0b05c_runner_v04.py` |

```makefile
changed_path_count = 14
historical_or_v03_paths_modified = false
git_diff_check = PASS
```

## Hallazgos

```makefile
F31A-01 = CLOSED / PASS
F31A-02 = CLOSED / PASS
F31A-03 = CLOSED / PASS
F31A-04 = CLOSED / PASS
```

- **F31A-01:** `validate_authorization_transition()` usa los estados realmente materializados: `CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED` y `NOT_AUTHORIZED`. La transición positiva in-memory pasa y una mutación inmutable falla de forma cerrada. Ancestry, bindings, authorization record e immutable projection permanecen estrictos.
- **F31A-02:** se añadió el adapter D1a v0.4. Lee el spec, authorization record y roots v0.4, acepta el proof v0.4 y rechaza el path de autorización v0.3. Conserva modelo, config, builder y evaluator originales.
- **F31A-03:** EV03 conserva su baseline histórico. EV04 toma el baseline agregado de `control["EV04"]["expected_metrics"]`, derivado canónicamente del frozen original case summary. El `run_metadata["metrics"]` histórico `.77` ya no es oracle agregado EV04. MRR@200 mantiene el contrato legacy.
- **F31A-04:** los tres specs declaran `specification_status = PREEXECUTION_SPEC_DEFINED`; autorización y auditoría quedan en campos separados.

## Shadow A-G

```makefile
Shadow_A = PASS
Shadow_B = PASS
Shadow_C = PASS
Shadow_D = PASS
Shadow_E = PASS
Shadow_F = PASS
Shadow_G1 = PASS
Shadow_G2 = PASS
```

G1 validó la transición positiva pura en memoria y el rechazo de una alteración no autorizable.

G2 se ejecutó como `CODEX_LOCAL_PURE_READ_ONLY_OR_DISPOSABLE_GIT_TEST / NOT_INDEPENDENT_GITHUB_CI`. Se creó una rama hija local y no publicada del commit provisional, se cambiaron únicamente los cuatro artefactos autorizables y se añadió el authorization record v0.4 contractual. El modelo congelado local se copió solo al worktree ignorado para verificar su identidad. El resultado fue:

```makefile
status = PASS
mode = AUTHORIZED_PREFLIGHT_ONLY
numerical_execution_occurred = false
d1a_read_only_preflight = PASS
d1a_mode = PREEXECUTION_CLOSED_READONLY
prospective_roots_present = false
synthetic_authorization_pushed = false
disposable_worktree_deleted = true
disposable_branch_deleted = true
```

No se llamó `execute_authorized()` ni se alcanzó ningún pipeline numérico.

## Aggregate EV04

El control canonical expected EV04 comparado consigo mismo produjo 27 filas con delta exactamente cero, incluidas `mrr_at_100`, `mrr_at_200` y `mrr_101_200_contribution`. La prueba también demostró que el helper EV04 funciona sin `primary_original_control.run_metadata`, mientras `mrr_at_200 == mrr` conserva el alias legacy.

```makefile
ev04_zero_delta_all_rows = PASS
ev04_historical_dot77_used_as_aggregate_oracle = false
mrr200_legacy_contract_preserved = true
```

## Pruebas

Todas las pruebas fueron locales y se clasifican como `CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`.

```makefile
tests_v04_corrected = 38/38 PASS
closed_preflight_v04 = PASS / PREEXECUTION_CLOSED_READONLY
positive_transition_g1 = PASS
positive_preflight_g2 = PASS / AUTHORIZED_PREFLIGHT_ONLY
d1a_v04_proof_validation = PASS
ev04_zero_delta = PASS
git_diff_check = PASS
```

Comando principal ejecutado:

```text
python -B -m unittest tests.test_0b05c_ev04_mrr_contract_v04 tests.test_0b05c_corrective_numerical_gate_v04 tests.test_d1a_corrective_0b05c_runner_v04
```

Las regresiones históricas ya ejecutadas en Prompt31 se preservaron sin repetición porque ningún path histórico cambió:

```makefile
tests_v03_preauthorization = 26/26 PASS
tests_ev03_recovery = 15 PASS / 1 SKIP
tests_v02_preauthorization = 56/56 PASS
tests_v01_preauthorization = 49/49 PASS
```

## Estado Final

```makefile
main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
origin_main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
main_modified = false

canonical_plan_head = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
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
working_tree_clean = true
BLOCKERS = NONE
```

**RESULTADO FINAL: CANDIDATO v0.4 CORREGIDO PUBLICADO PARA AUDITORÍA EXTERNA; ATTEMPT05 NO AUTORIZADO Y NO EJECUTADO.**
