### A. Baseline Git y fuentes

```makefile
main = 58ecf012d7c4ed609c3b10787fb583f69700ab02
origin_main = 58ecf012d7c4ed609c3b10787fb583f69700ab02
main_parent = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
failure_record_root_cause_field_status = NOT_YET_ISOLATED
gate_authorization_readiness = ATTEMPT04_CONSUMED / REAUTHORIZATION_REQUIRED
attempt05_authorized = false
baseline_preflight = PASS
```

Bindings Git verificados:

```makefile
failure_record_blob = 31f1cea387b8630191371f767c03cf13990646b0
gate_v0_3_blob = 58152fd4806d8efd54ae752cb2790c383417aa37
evaluator_v0_3_blob = 3fb1346dcee357d7b1d2d430e3ca98c0bba1d1a0
comparator_legacy_blob = c6f4121fe5f5f50e71e27eb4cf1e28eb8986d062
frozen_run_metadata_blob = 3cbbabd9d9446958e5a0b386f13bd32aec817fa1
frozen_case_summary_blob = 5421bf1bf2082e2ba66ce045f804f1d02b77fd58
frozen_metrics_artifact_blob = bc3b34cae7d8832426e6b2b56cb3d2d1541cdd57
frozen_ranking_blob = 9a1543570c18e3cba32f6cf20506d166fd238896
source_bindings_all_match_expected = true
```

### B. Reconstruccion pura v0.3

```makefile
evidence_scope = VERSIONED_FROZEN_ARTIFACTS_AND_PURE_READ_ONLY_COMPUTATION
case_count = 1056
base_metrics = hierarchical.metrics_from_cases(case_rows)
reconstructed_v03 = build_ev04_enriched_metrics(case_rows, base_metrics, require_real_case_count=True)
expected_top_level_key_count = 92
reconstructed_top_level_key_count = 92
missing_keys = 0
extra_keys = 0
expected_metrics_equal_reconstructed_v03 = false
metric_table_equal = false
metric_table_names_and_order_equal = true
metric_table_row_schemas_equal = true
metric_table_row_schema = metric,numerator,denominator,value
```

Las 92 keys top-level del esperado y del reconstruido son, en el mismo orden:

```text
mrr, top_1, top_3, top_5, top_10, top_50, recall_at_50, recall_at_100,
recall_at_200, pool_recall_at_200, exact_at_10, hs6_at_10, hs4_at_10,
chapter_at_10, exact_at_50, hs6_at_50, hs4_at_50, chapter_at_50,
exact_at_100, hs6_at_100, hs4_at_100, chapter_at_100, exact_at_200,
hs6_at_200, hs4_at_200, chapter_at_200, mrr_numerator, mrr_denominator,
top_1_numerator, top_1_denominator, top_3_numerator, top_3_denominator,
top_5_numerator, top_5_denominator, top_10_numerator, top_10_denominator,
top_50_numerator, top_50_denominator, recall_at_50_numerator,
recall_at_50_denominator, recall_at_100_numerator, recall_at_100_denominator,
recall_at_200_numerator, recall_at_200_denominator,
pool_recall_at_200_numerator, pool_recall_at_200_denominator,
exact_at_10_numerator, exact_at_10_denominator, hs6_at_10_numerator,
hs6_at_10_denominator, hs4_at_10_numerator, hs4_at_10_denominator,
chapter_at_10_numerator, chapter_at_10_denominator, exact_at_50_numerator,
exact_at_50_denominator, hs6_at_50_numerator, hs6_at_50_denominator,
hs4_at_50_numerator, hs4_at_50_denominator, chapter_at_50_numerator,
chapter_at_50_denominator, exact_at_100_numerator, exact_at_100_denominator,
hs6_at_100_numerator, hs6_at_100_denominator, hs4_at_100_numerator,
hs4_at_100_denominator, chapter_at_100_numerator, chapter_at_100_denominator,
exact_at_200_numerator, exact_at_200_denominator, hs6_at_200_numerator,
hs6_at_200_denominator, hs4_at_200_numerator, hs4_at_200_denominator,
chapter_at_200_numerator, chapter_at_200_denominator, cases_evaluated,
cases_with_retrieval, zero_retrieval_cases, not_found_at_depth, metric_table,
mrr_at_100, mrr_at_200, mrr_at_100_numerator, mrr_at_200_numerator,
mrr_at_100_denominator, mrr_at_200_denominator, mrr_definition,
mrr_101_200_contribution_numerator, mrr_101_200_contribution
```

Los nombres y el orden del `metric_table` esperado y reconstruido son identicos:

```text
mrr_at_100, mrr_at_200, top_1, top_3, top_5, top_10, top_50,
recall_at_50, recall_at_100, recall_at_200, pool_recall_at_200,
exact_at_10, hs6_at_10, hs4_at_10, chapter_at_10, exact_at_50,
hs6_at_50, hs4_at_50, chapter_at_50, exact_at_100, hs6_at_100,
hs4_at_100, chapter_at_100, exact_at_200, hs6_at_200, hs4_at_200,
chapter_at_200
```

### C. Deep diff completo

```makefile
comparison = EXACT_PYTHON_NO_TOLERANCE_WITH_TYPE_AUDIT
mismatch_count = 6
missing_or_extra_key_mismatches = 0
type_only_mismatches = 0
```

| json_path | expected_type | observed_type | expected_repr | observed_repr | expected_float_hex | observed_float_hex | ULP | absolute_delta |
|---|---|---|---:|---:|---|---|---:|---:|
| `$.metric_table[0].numerator` | float | float | `44.33224687474574` | `44.33224687474575` | `0x1.62a8710ca9d97p+5` | `0x1.62a8710ca9d98p+5` | 1 | `7.105427357601002e-15` |
| `$.metric_table[0].value` | float | float | `0.04198129438896377` | `0.04198129438896378` | `0x1.57e927ce3818bp-5` | `0x1.57e927ce3818cp-5` | 1 | `6.938893903907228e-18` |
| `$.mrr_101_200_contribution` | float | float | `0.0013603172139190387` | `0.001360317213919032` | `0x1.649957c8abdd1p-10` | `0x1.649957c8abdb2p-10` | 31 | `6.7220534694101275e-18` |
| `$.mrr_101_200_contribution_numerator` | float | float | `1.436494977898505` | `1.436494977898498` | `0x1.6fbe2286f13c0p+0` | `0x1.6fbe2286f13a0p+0` | 32 | `7.105427357601002e-15` |
| `$.mrr_at_100` | float | float | `0.04198129438896377` | `0.04198129438896378` | `0x1.57e927ce3818bp-5` | `0x1.57e927ce3818cp-5` | 1 | `6.938893903907228e-18` |
| `$.mrr_at_100_numerator` | float | float | `44.33224687474574` | `44.33224687474575` | `0x1.62a8710ca9d97p+5` | `0x1.62a8710ca9d98p+5` | 1 | `7.105427357601002e-15` |

En los seis registros `equal_python = false`.

### D. Control historico secundario

```makefile
run_metadata_metrics_equal_metrics_artifact = true
historical_secondary_mismatch_count = 0
historical_secondary_mismatch_paths = []
runner_v03_expected_source = run_metadata.json["metrics"]
```

### E. Microauditoria aritmetica MRR

Las cuatro rutas obligatorias produjeron exactamente los mismos bits:

```text
sum(1.0 / rank_ref)
sum(float(reciprocal_rank))
math.fsum(1.0 / rank_ref)
math.fsum(float(reciprocal_rank))
```

| campo reconstruido por cada ruta | repr | float.hex() |
|---|---:|---|
| numerator MRR@100 | `44.33224687474575` | `0x1.62a8710ca9d98p+5` |
| MRR@100 / 1056 | `0.04198129438896378` | `0x1.57e927ce3818cp-5` |
| numerator MRR@200 | `45.76874185264425` | `0x1.6e266220e1635p+5` |
| MRR@200 / 1056 | `0.04334161160288281` | `0x1.630df28c7d779p-5` |
| numerator 101-200 por resta 200-100 | `1.436494977898498` | `0x1.6fbe2286f13a0p+0` |
| contribucion 101-200 / 1056 | `0.001360317213919032` | `0x1.649957c8abdb2p-10` |

Valores congelados relevantes:

| campo congelado | repr | float.hex() |
|---|---:|---|
| `mrr_at_100_numerator` | `44.33224687474574` | `0x1.62a8710ca9d97p+5` |
| `mrr_at_100` | `0.04198129438896377` | `0x1.57e927ce3818bp-5` |
| `mrr_at_200_numerator` / `mrr_numerator` | `45.76874185264425` | `0x1.6e266220e1635p+5` |
| `mrr_at_200` / `mrr` | `0.04334161160288281` | `0x1.630df28c7d779p-5` |
| `mrr_101_200_contribution_numerator` | `1.436494977898505` | `0x1.6fbe2286f13c0p+0` |
| `mrr_101_200_contribution` | `0.0013603172139190387` | `0x1.649957c8abdd1p-10` |

```makefile
all_four_routes_match_frozen_mrr_at_100 = false
all_four_routes_match_frozen_mrr_at_200 = true
legacy_mrr_numerator_bit_exact = true
legacy_mrr_bit_exact = true
metric_table_mrr_at_100_bit_exact = false
metric_table_mrr_at_200_bit_exact = true
```

Las cuatro rutas read-only convergen bit-a-bit al valor reconstruido v0.3. Ninguna reproduce el MRR@100 congelado, que es un ULP menor. La diferencia entre v0.3 y el congelado se propaga mediante `numerator_200 - numerator_100` a los dos campos de contribucion 101-200 y a la fila `mrr_at_100` del `metric_table`; MRR@200 permanece exacto. La evidencia versionada no establece que ruta aritmetica historica produjo el valor congelado un ULP menor.

### F. Comparator estatico

```makefile
frozen_ranking_used_as_expected_and_actual = true
frozen_case_summary_used_as_expected_and_actual = true
ranking_schema_exact = true
case_summary_schema_exact = true
metrics_exact_before_call = false
compare_control_reproduction_outcome = RAISED_CONTRACT_VIOLATION
exception = src.experiments.run_d1a_corrective_0b05c_v01.ContractViolation: Mandatory control reproduction is not exact
retrieval_executed = false
evaluation_runner_executed = false
```

La prueba aisla estaticamente el factor metricas; no convierte esta demostracion en evidencia de runtime.

### G. Clasificacion causal

```makefile
ROOT_CAUSE_FIELD_STATUS = ISOLATED_FROM_VERSIONED_FROZEN_ARTIFACTS
root_cause_class = FLOAT_ACCUMULATION_PATH_MISMATCH
root_cause_json_path_count = 6
```

```text
$.metric_table[0].numerator
$.metric_table[0].value
$.mrr_101_200_contribution
$.mrr_101_200_contribution_numerator
$.mrr_at_100
$.mrr_at_100_numerator
```

### H. Aislamiento y prohibiciones

```makefile
attempt04_runtime_outputs_used = false
retrieval_executed = false
indexes_built = false
evaluate_arm_called = false
ev03_executed = false
ev04_executed = false
d1a_executed = false
real_eval_executed = false
model_inference_executed = false
v0_4_built = false
attempt05_authorized = false
code_modified = false
tests_modified = false
gate_modified = false
specs_modified = false
authorization_record_modified = false
failure_record_modified = false
canonical_plan_modified = false
article_modified = false
exp11b_modified = false
exp12_modified_or_opened = false
prospective_roots_present = false
```

### I. Commit cientifico candidato

```makefile
branch = codex/0b05c-ev04-attempt04-static-metric-diagnosis-v03
candidate_commit = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
candidate_parent = 58ecf012d7c4ed609c3b10787fb583f69700ab02
candidate_tree = 7c8199733df071eee299d80a57456223fb2834ad
base_to_candidate_commit_count = 1
changed_path_count = 1
changed_path = outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json
diagnosis_blob = fca5712c615960b41cb2741c2164f19fc00df9dd
candidate_push = PASS
remote_candidate = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
working_tree_clean = true
```

### J. Persistencia administrativa

```makefile
admin_branch = codex/prompts-temporary
admin_response_path = codex_prompts_tmp/26_RESPUESTA_DIAGNOSTICO_ESTATICO_MISMATCH_METRICAS_EV04_ATTEMPT04.md
prompt26_modified = false
previous_responses_modified = false
admin_commit_scope = RESPONSE_ONLY
admin_push = PASS
```

### K. Estado cientifico

GROUP_2 = EN_CURSO

0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED

0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04

EV04_ATTEMPT04_ROOT_CAUSE_FIELD = ISOLATED_FROM_VERSIONED_FROZEN_ARTIFACTS

ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
