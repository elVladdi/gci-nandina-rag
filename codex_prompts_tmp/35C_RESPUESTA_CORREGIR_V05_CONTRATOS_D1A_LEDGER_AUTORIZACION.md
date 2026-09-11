# RESPUESTA PROMPT 35C — CANDIDATO v0.5 CORREGIDO

## Resultado

```makefile
PROMPT35C = COMPLETED
V05_CORRECTED_CANDIDATE = BUILT / TESTED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT
GATE_STATUS = CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED
AUTHORIZATION_READINESS = NOT_AUTHORIZED

branch = codex/0b05c-v05-remediated-preauthorization-candidate-v2
commit = 6511e6e72c5f77978699a290c8449c3c6736a71c
parent = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
tree = c027983bb1711688c2e860786f9065542397bb89
remote_commit = 6511e6e72c5f77978699a290c8449c3c6736a71c

rejected_candidate = a3d4c7b6067e1ed6ac10606a9c2a8ab46336bfda / NOT_INTEGRATED / NOT_ANCESTOR
main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
origin_main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

El candidato corregido es un único commit con parent directo en `main`. El candidato rechazado de Prompt35B no fue integrado ni forma parte de su historia; el merge-base entre ambos candidatos es `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`.

## Diff exacto

Resultado contra `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`: **20 paths, 4657 inserciones y 5 eliminaciones**.

| Estado | Blob Git | Bytes | Path |
|---|---|---:|---|
| A | `91e15145699f029ac9d311831adcc83b4ee0ca48` | 2322 | `outputs/audits/0b05c_attempt05_failclosed_v0.4/attempt05_failclosed_record_v0.4.json` |
| M | `ad621a4f7349db08162bcdb91bacd78029398c20` | 29099 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json` |
| M | `859c5e23a9699f33a45b2e9aa9be087ea06a3e15` | 17472 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json` |
| M | `b58d4aca70f7af6dd52077d4b441dcdf1e7bba6c` | 21133 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json` |
| M | `91d87fb3d0e94e07628b3c31e79785d261752e39` | 29152 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json` |
| A | `f083f663cd03f000709e38a02cfb1070ccb687e2` | 23640 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json` |
| A | `33904414b4d8b96cff16ccfeb29e969306684f9f` | 9561 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_hash_ledger_v0.5.json` |
| A | `96b75ca5c6d3df612a3b5b05eec10311a02f6036` | 14834 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_manifest_v0.5.json` |
| A | `60486205b36ede412076e33c838030c794f6e0fa` | 17694 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/d1a_numerical_execution_spec_v0.5.json` |
| A | `e7536586adf30dd6ba9cca2d23c86f5f9af95213` | 21403 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev03_numerical_execution_spec_v0.5.json` |
| A | `5fc85150c99dbe950b74acc0f0a1770c8a4cf930` | 29316 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev04_numerical_execution_spec_v0.5.json` |
| A | `7edd002cb480958992b29ec9702e5e005f04211a` | 5230 | `outputs/audits/0b05c_v05_preauthorization_readiness/preauthorization_readiness_v0.5.json` |
| A | `18c398f5709257326db67790a9ab7ec64a2da8f6` | 15020 | `src/experiments/evaluate_normative_bm25_corrective_0b05c_v05.py` |
| A | `b4189fe53c84df0497dd3731e32b4a8535af354e` | 52241 | `src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py` |
| A | `7bce4de212c96f536f8ae05919b83bf02d74a05f` | 21252 | `src/experiments/run_0b05c_corrective_numerical_v05.py` |
| A | `d474b856df8789e885b33172d1bd980b27bb60a3` | 12169 | `src/experiments/run_d1a_corrective_0b05c_v05.py` |
| A | `b4c4d36d6f3eadd953d54f615babd50f18bcf7b4` | 7717 | `tests/test_0b05c_v05_comparator_aggregate_integrity.py` |
| A | `52db6b75e4f83d296b4a21d9e7ac084135f70bb3` | 13653 | `tests/test_0b05c_v05_d1a_ledger_authorization_contracts.py` |
| A | `ff2892754fa4dbebc604c6e48dd78a657a140ce0` | 6376 | `tests/test_0b05c_v05_environment_d1a_readiness.py` |
| A | `fda54fe3ae07801070794038b1dc600105afa2e4` | 7515 | `tests/test_0b05c_v05_summary_manifest_ledger_orchestration.py` |

No se modificaron Plan Maestro, `article/`, EXP11B, EXP12, configuraciones, corpus, EVAL ni componentes históricos v0.1-v0.3. Los únicos cambios v0.4 son los cuatro JSON de estado y el fail-close sanitizado de Attempt05 autorizados por el alcance. El authorization record v0.4 no cambió.

## Cierre de findings

```makefile
F35C-01 = CLOSED_BY_CODE_TEST_AND_SHADOW
F35C-02 = CLOSED_BY_CODE_TEST_AND_SHADOW
F35C-03 = CLOSED_BY_CODE_TEST_AND_SHADOW
F35C-04 = CLOSED_BY_CODE_TEST_AND_SHADOW
F35C-05 = CLOSED_BY_CODE_TEST_AND_SHADOW
F35C-06 = CLOSED_BY_CODE_TEST_AND_SHADOW
```

### F35C-01 — Contrato D1a único v0.5

Los tres `specification_id` son v0.5. El adapter D1a v0.5 define y produce sus propios cuatro outputs, sin depender de `RUNNER_FILENAMES` v0.1. El binding canónico del runner D1a apunta al archivo v0.5 real:

```makefile
path = src/experiments/run_d1a_corrective_0b05c_v05.py
git_blob_sha1 = d474b856df8789e885b33172d1bd980b27bb60a3
canonical_sha256 = 90dd1419d5650470396eeaa1bcab9342f96aa42b9dd631b8195f88a18d186a65
canonical_size_bytes = 12169
```

Tabla de identidad three-way:

| D1A_SPEC_RUNNER_SET | D1A_ACTUAL_PRODUCER_SET | UNIFIED_LEDGER_D1A_RUNNER_SUBSET | Resultado |
|---|---|---|---|
| `d1a_corrective_vs_original_comparison_v0.5.json` | igual | igual | PASS |
| `d1a_corrective_case_level_comparison_v0.5.jsonl` | igual | igual | PASS |
| `d1a_corrective_output_hash_ledger_v0.5.csv` | igual | igual | PASS |
| `d1a_corrective_execution_manifest_v0.5.json` | igual | igual | PASS |

Las mutaciones independientes de nombres en cada lado fallaron de forma cerrada. El ledger contractual D1a coincide con los productores reales del adapter sin ejecutar D1a científico.

### F35C-02 — Sets independientes y observación física

`EXPECTED_SET` se deriva exclusivamente de specs/contratos declarativos. `PRODUCER_SET` se deriva de constantes y path-builders concretos de los productores de los pasos 1-17 y no lee `runtime_hash_ledger_contract.expected_paths`.

```makefile
EXPECTED_SET = 47
PRODUCER_SET = 47
EXPECTED_SET_EQUALS_PRODUCER_SET = true
```

El ledger runtime descubre recursivamente archivos físicos bajo los roots contractuales y exige `OBSERVED_SET == EXPECTED_SET`, excluyendo solo su self-path. Resultado de negativos reales en `tempdir`:

```makefile
physical_exact_set = PASS
physical_missing_file = FAIL_CLOSED
physical_unexpected_on_disk_file = FAIL_CLOSED
physical_execution_failed_json = FAIL_CLOSED
physical_path_collision = FAIL_CLOSED
physical_snapshot_byte_mutation = FAIL_CLOSED
```

### F35C-03 — Transición futura de autorización

Se implementaron contrato/schema exacto, ancestry proper-ancestor, bindings Git canónicos, proyección inmutable, mutabilidad limitada, carga desde Git y validación filesystem-versus-commit. `preflight_authorized()` ejecuta esta transición antes del environment gate y antes de cualquier side effect.

```makefile
candidate_source_binding_count = 35
candidate_source_bindings_exact = 35/35 PASS
positive_authorization_transition_shadow = PASS
positive_authorized_preflight_shadow = PASS / NO_SIDE_EFFECT
scientific_field_drift_negative = FAIL_CLOSED
root_path_drift_negative = FAIL_CLOSED
environment_contract_drift_negative = FAIL_CLOSED
code_binding_drift_negative = FAIL_CLOSED
authorization_missing_field_negative = FAIL_CLOSED
authorization_extra_field_negative = FAIL_CLOSED
binding_sha_negative = FAIL_CLOSED
improper_ancestor_negative = FAIL_CLOSED
filesystem_commit_mismatch_negative = FAIL_CLOSED
```

No se creó authorization record v0.5 real.

### F35C-04 — Ranking, summary y métricas completas

Los checks exigen `nandina_ref` consistente, ranks contiguos, `retrieved_count` exacto, top1 efectivo y `rank_ref` igual a la posición real o cero. Los contratos de ranking vacío se preservaron. Los negativos de `rank_ref` incorrecto y `candidate_row.nandina_ref` discordante fallaron cerrados.

```makefile
EV03_original_vs_original = PASS / 1056_CASES / 10_VALID_EMPTY_RANKINGS
EV03_full_metric_integrity = PASS / 56_KEYS
EV04_full_metric_integrity = PASS / 92_KEYS / 27_ROWS
EV04_aggregate = PASS / 28_ROWS / CONTRIBUTION_THIRD
EV03_aggregate = PASS / 17_ROWS
persist_reload_key_order_independent = PASS
NaN_Inf_and_denominator_negatives = FAIL_CLOSED
```

Se preservaron MRR@100 racional exacto, MRR@200 legacy por suma float en orden congelado y la contribución 101-200 como diferencia racional exacta.

### F35C-05 — Provenance fuerte del manifest

El schema exacto del manifest incluye commit de autorización, baseline, prueba de transición, cuatro flags, binding del authorization record, bindings de gate/specs autorizados, environment fingerprint, orden de 19 pasos, roots y referencias de resultados. Pasaron `allow_nan=False`, round-trip y no-overwrite. Provenance incompleta/inconsistente, orden inválido y roots v0.4 fallaron cerrados.

### F35C-06 — Identidades obsoletas

Se añadió allowlist explícita para tokens históricos permitidos y auditoría fail-closed de sources/artifacts v0.5.

```makefile
stale_current_identity_count = 0
stale_current_identity_audit = PASS
historical_allowlisted_occurrences = 22
artifact_historical_v04_occurrences = 16 / EXPLICIT_V04_PARTIAL_ROOTS_NEVER_INPUT
absolute_host_paths_in_public_artifacts = 0
```

Los tokens históricos permitidos se limitan a Attempt05 failclosed, `v04_partial_roots`/`NEVER_INPUT` y referencias históricas etiquetadas. Ningún output, specification ID, comando, source identity o binding corriente v0.5 apunta a v0.1/v0.4.

## Environment y replay

La evidencia local ya obtenida se preservó, sin instalar ni actualizar dependencias:

```makefile
environment_status = PASS
environment_classification = TESTED_EXECUTION_ENVIRONMENT / NOT_HISTORICAL_PROVENANCE
fingerprinted_python = 3.10.11
fingerprinted_executable_sha256 = b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961
model_manifest = 9/9 PASS_EXACT / 0_MISSING / 0_EXTRA / 0_MISMATCH
offline_smoke = PASS / 32x384 / float32 / FINITE / NORMALIZED / CPU / NETWORK_FALSE
historical_replay = PASS / 21_VECTORS
historical_replay_cosine_min = 0.9999999948279137
historical_replay_max_abs_difference = 1.1920928955078125e-07
historical_replay_tolerance = 9.5367431640625e-07
capacity = PASS_WITH_OBSERVED_FOOTPRINT_DERIVED_MARGINS
dependencies_installed_or_updated = false
```

Reprobe final: el intérprete fingerprinted no seguía disponible. El runtime bundled presente tenía SHA-256 `b7a12c3af0b4db44191eec14ea095eba731b7328917f570806183093d19ddca2` y carecía de `sentence_transformers`; por prohibición expresa no se instalaron dependencias ni se sustituyó el fingerprint. Esta indisponibilidad queda registrada como `FINGERPRINTED_INTERPRETER_NOT_AVAILABLE`, sin invalidar la evidencia local previa ni convertirla en CI independiente.

## Tests

Clasificación: `CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`.

### Suite focalizada v0.5 final

```powershell
& '<bundled-runtime-python>' -m unittest tests.test_0b05c_v05_environment_d1a_readiness tests.test_0b05c_v05_comparator_aggregate_integrity tests.test_0b05c_v05_summary_manifest_ledger_orchestration tests.test_0b05c_v05_d1a_ledger_authorization_contracts -v
```

```makefile
tests_v05 = 44
pass = 44
fail = 0
error = 0
skip = 0
duration_seconds = 11.000
```

### Regresión v0.4 relevante

```powershell
& '<bundled-runtime-python>' -m unittest tests.test_0b05c_corrective_numerical_gate_v04 tests.test_0b05c_ev04_mrr_contract_v04 tests.test_d1a_corrective_0b05c_runner_v04 -v
```

```makefile
tests_v04 = 41
pass = 38
fail = 2
error = 1
skip = 0
duration_seconds = 13.302
EV04_MRR = 23/23 PASS
D1A_v04 = 4/4 PASS
```

Los tres non-successes son exclusivamente supuestos obsoletos del harness histórico frente al estado v0.4 ya consumido: una aserción exige ausencia del authorization record, otra exige exactamente seis artefactos aunque el record sea el séptimo, y el preflight histórico exige que el record esté ausente. No apareció una regresión científica nueva y no se modificaron esos tests históricos fuera de alcance.

## Shadow integral

```makefile
preauthorization_closed_preflight = PASS / PREAUTHORIZATION_CLOSED_READONLY
environment_model_smoke = PASS_EVIDENCE_PRESERVED
historical_21_vector_replay = PASS_EVIDENCE_PRESERVED
EV03_frozen_control = PASS
R13_positive_and_negatives = PASS / NEGATIVES_FAIL_CLOSED
EV04_full_metrics_persist_reload = PASS
aggregate_positive_and_nan_inf_negatives = PASS / NEGATIVES_FAIL_CLOSED
unified_summary_positive_and_negatives = PASS
D1A_three_way_identity = PASS
D1A_ledger_vs_actual_producers = PASS
manifest_provenance_roundtrip_negatives = PASS
expected_vs_independent_producer = PASS / 47_EQUALS_47
observed_filesystem_negatives = PASS_FAIL_CLOSED
authorization_transition_shadow = PASS / NEGATIVES_FAIL_CLOSED
synthetic_19_step_pipeline = PASS / NEGATIVES_FAIL_CLOSED
stale_identity_audit = PASS
```

## Estado científico y de seguridad

```makefile
EV03_NUMERICAL_EXECUTION = NOT_AUTHORIZED
EV04_NUMERICAL_EXECUTION = NOT_AUTHORIZED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION = NOT_AUTHORIZED
ATTEMPT05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED

authorization_record_v05_present = false
future_v05_roots_defined = 16
future_v05_roots_present = 0
scientific_retrieval_executed = false
EV03_real_executed = false
EV04_real_executed = false
D1A_complete_executed = false
EVAL_real_executed = false
model_inference_executed_in_this_block = false
Attempt05_reexecuted = false
Attempt06_authorized = false
Attempt06_executed = false
dependencies_installed_or_updated = false
main_integrated = false
candidate_working_tree_clean = true
```

## Riesgos residuales

No se declara riesgo cero. Permanecen:

- `FULL_7644_DOCUMENT_ENCODE`
- `FULL_1056_QUERY_ENCODE_AND_EVALUATION`
- `RUNTIME_MEMORY_CPU_IO_PEAK`
- `FUTURE_OUTPUT_HASHES`
- `EXTRAORDINARY_HOST_FAILURE_AFTER_SIDE_EFFECTS`

## Dictamen

```makefile
BLOCKERS = NONE_DETECTED_IN_CODE_TEST_AND_SHADOW_SCOPE
EXTERNAL_AUDIT_REQUIRED = true
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
```

El candidato corregido quedó publicado exclusivamente en `origin/codex/0b05c-v05-remediated-preauthorization-candidate-v2`. No se integró a `main` y no se abrió ninguna autorización numérica.
