# RESPUESTA PROMPT 35B — INTEGRACIÓN DE AUDITORÍA Y CANDIDATO v0.5 REMEDIADO

## Resultado ejecutivo

```makefile
PROMPT35A_INTEGRATION = PASS / FAST_FORWARD_ONLY
V05_CANDIDATE = BUILT / TESTED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT
ATTEMPT05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
NUMERICAL_EXECUTION_OCCURRED = false
SCIENTIFIC_RETRIEVAL_EXECUTED = false
SCIENTIFIC_EVAL_EXECUTED = false
FULL_D1A_EXECUTED = false
```

La evidencia de pruebas y shadows de este reporte se clasifica como:

`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`

## Fase A — integración exacta de Prompt35A

```makefile
pre_integration_main = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
pre_integration_origin_main = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
approved_audit_branch = codex/0b05c-preauthorization-risk-audit-12-19
approved_audit_commit = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
approved_audit_parent = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
approved_audit_tree = 11f7c59d66c858022c1d75282a8c77b93606c8aa
ahead_behind = 1 / 0
integration_method = git merge --ff-only
post_integration_main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
post_integration_origin_main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
merge_commit_created = false
```

Único contenido integrado frente a `812cb69...`:

| Path | Blob | Bytes |
|---|---|---:|
| `outputs/audits/0b05c_preauthorization_risk_audit_v0.4/preauthorization_risk_audit_steps12_19_v0.4.json` | `4bbb25940f5a14f88c4ed51daaa8475116facd29` | 26355 |

Refs protegidas verificadas e intactas:

```makefile
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

## Candidato técnico v0.5

```makefile
branch = codex/0b05c-v05-remediated-preauthorization-candidate
commit = a3d4c7b6067e1ed6ac10606a9c2a8ab46336bfda
remote_commit = a3d4c7b6067e1ed6ac10606a9c2a8ab46336bfda
parent = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
tree = 8a48c32ba4c6ce21ba4ac941cad3d1ac064f9981
commit_count_over_parent = 1
published = true
integrated_to_main = false
main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
origin_main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
working_tree_tracked_clean = true
```

## Paths y blobs exactos

El commit modifica exactamente 19 paths:

| Estado | Path | Blob | Bytes |
|---|---|---|---:|
| A | `outputs/audits/0b05c_attempt05_failclosed_v0.4/attempt05_failclosed_record_v0.4.json` | `91e15145699f029ac9d311831adcc83b4ee0ca48` | 2322 |
| M | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json` | `ad621a4f7349db08162bcdb91bacd78029398c20` | 29099 |
| M | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json` | `859c5e23a9699f33a45b2e9aa9be087ea06a3e15` | 17472 |
| M | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json` | `b58d4aca70f7af6dd52077d4b441dcdf1e7bba6c` | 21133 |
| M | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json` | `91d87fb3d0e94e07628b3c31e79785d261752e39` | 29152 |
| A | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json` | `904aa3256c00dd344ed0397163475d9c0e6ce5eb` | 11099 |
| A | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_hash_ledger_v0.5.json` | `33904414b4d8b96cff16ccfeb29e969306684f9f` | 9561 |
| A | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_manifest_v0.5.json` | `573f07a99fa43cb617426b543796ca50ddc2672e` | 3486 |
| A | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/d1a_numerical_execution_spec_v0.5.json` | `85b3f6d43af3e6a2a451f474365e59edf055ad8c` | 17636 |
| A | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev03_numerical_execution_spec_v0.5.json` | `240465db51cd5688be886be9ad173ba0fe6d1aa5` | 21403 |
| A | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev04_numerical_execution_spec_v0.5.json` | `f263abcc1495515b38b2096ddb7dd671fe91ce4c` | 29316 |
| A | `outputs/audits/0b05c_v05_preauthorization_readiness/preauthorization_readiness_v0.5.json` | `bb8871c82037c70a5f71b9af158c35659f9c2143` | 4707 |
| A | `src/experiments/evaluate_normative_bm25_corrective_0b05c_v05.py` | `92c8e92c3069a17c66b0c28ba632728e665efad8` | 12634 |
| A | `src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py` | `9953c96d0b5013df93cf4c52467cc5cbdd40914b` | 26286 |
| A | `src/experiments/run_0b05c_corrective_numerical_v05.py` | `7cd0e71b2e19a134e2309cecf38f1ba846134fcf` | 20640 |
| A | `src/experiments/run_d1a_corrective_0b05c_v05.py` | `6020fc892703644d0000549c68ebb0761133efd7` | 7530 |
| A | `tests/test_0b05c_v05_comparator_aggregate_integrity.py` | `a2a7ec0d5564e7e70706c8ec1ad5c13a546d31e2` | 6621 |
| A | `tests/test_0b05c_v05_environment_d1a_readiness.py` | `ff2892754fa4dbebc604c6e48dd78a657a140ce0` | 6376 |
| A | `tests/test_0b05c_v05_summary_manifest_ledger_orchestration.py` | `dc3e783dbf301bb77cbdd16841818cc97b696c7b` | 6362 |

No se modificó ningún componente histórico v0.1–v0.3. En v0.4 solo cambiaron los campos de estado autorizados en los cuatro JSON indicados; el authorization record v0.4 permanece byte-identical al baseline.

## Cierre histórico de Attempt05

Se materializó el registro sanitizado `attempt05_failclosed_record_v0.4.json` con referencias por branch, commit y blob a la evidencia preservada en `5144bbdfc3b36e6172ecdd604a3e71d256ab248b`.

```makefile
failure_class = MISSING_RUNTIME_PYTHON_DEPENDENCY
terminal_error = ModuleNotFoundError: No module named 'sentence_transformers'
last_completed_step_reported = 11
last_started_step_reported = 12
evidence_classification = CODEX_EXECUTION_RECORD_EVIDENCE / NOT_INDEPENDENT_GIT_OBSERVATION
ATTEMPT05_AUTHORIZATION = OPERATIONALLY_CONSUMED
ATTEMPT05_RETRY = FORBIDDEN
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
```

También quedó corregida la provenance de `requirements.txt`: blob Git `19273fcbb593fcb089c79dfab7acf9d8076e44bc`, 80 bytes canónicos Git y SHA-256 `698fcd824a8ff840f5deb53e6a8dcda007014ee5108b89190bf4f8d312512724`; la observación de 89 bytes y SHA-256 `5d063a971db0a2d88826f4dd2a6239ae482bdbf1554fe468b0b8b7918d5fb50b` se clasifica exclusivamente como `LOCAL_CHECKOUT_CRLF_BYTES`.

No se copiaron stderr/stdout crudos ni rutas absolutas host-locales al candidato.

## Cierre de blockers y hardening

```makefile
R12-02_INTERPRETER_READINESS_NOT_GATED = CLOSED_BY_CODE_TEST_AND_SHADOW
R12-03_COMPLETE_MODEL_DIRECTORY_NOT_GATED = CLOSED_BY_CODE_TEST_AND_SHADOW
R14-01_EV03_EMPTY_RANKING_CASES_BREAK_COMPARISON = CLOSED_BY_CODE_TEST_AND_SHADOW
R15-02_NONFINITE_NONCONTRIBUTION_METRICS_NOT_REJECTED = CLOSED_BY_CODE_TEST_AND_SHADOW
R16-01_UNIFIED_SUMMARY_SCHEMA_UNDERVALIDATED = CLOSED_BY_CODE_TEST_AND_SHADOW
R13_INTEGRITY_HARDENING = CLOSED_BY_CODE_TEST_AND_SHADOW
R15_EV04_PERSIST_RELOAD = CLOSED_BY_CODE_TEST_AND_SHADOW
R17_MANIFEST_HARDENING = CLOSED_BY_CODE_TEST_AND_SHADOW
R18_LEDGER_REDERIVATION = CLOSED_BY_CODE_TEST_AND_SHADOW
R19_FINAL_STATE_ORCHESTRATION = CLOSED_BY_CODE_TEST_AND_SHADOW
```

- R12 vuelve obligatorios el fingerprint del intérprete, imports directos y transitivos, los nueve archivos gobernados del modelo, smoke offline, recursos y preflight antes de cualquier side effect futuro.
- R13 valida existencia, lectura, schemas, unicidad de 1056 casos, coherencia ranking/summary, finitud de métricas, outputs D1a y snapshots hash/size read-after-write.
- R14 acepta ranking EV03 vacío solo con summary vacío coherente y rechaza falsos vacíos, counts discordantes y ranks no contiguos.
- R15 valida numericidad no-bool, finitud, denominadores, set exacto de campos y orden contractual de filas sin depender del orden de keys JSON.
- R16 exige aggregates EV03 de 17 filas, EV04 de 28 filas y las cuatro referencias D1a completas y validadas.
- R17 valida schema, finitud, provenance, 19 pasos, ausencia de roots v0.4 y no-overwrite antes de serializar con `allow_nan=False`.
- R18 deriva independientemente `EXPECTED_SET` y `PRODUCER_SET`; cardinalidad resultante `47 == 47`, sin `execution_failed.json` en success path.
- R19 conserva la orquestación de 19 pasos y falla cerrado ante missing, reorder, FAIL previo o final prematuro.

## Roots y autorización

Los 16 roots prospectivos v0.5 fueron comprobados individualmente y permanecen ausentes.

```makefile
V04_PARTIAL_ROOTS = NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05
v04_partial_outputs_copied = false
v05_prospective_roots_present = false
authorization_record_v0.5_present = false
gate_status = CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED
authorization_readiness = NOT_AUTHORIZED
EV03_NUMERICAL_EXECUTION = NOT_AUTHORIZED
EV04_NUMERICAL_EXECUTION = NOT_AUTHORIZED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION = NOT_AUTHORIZED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
```

## Environment candidato sanitizado

```makefile
environment_status = PASS
environment_classification = TESTED_EXECUTION_ENVIRONMENT / NOT_HISTORICAL_PROVENANCE
python = 3.10.11
executable_sha256 = b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961
numpy = 2.2.6
sentence_transformers = 5.5.1
torch = 2.12.0+cpu
tqdm = 4.68.2
transformers = 5.12.1
tokenizers = 0.22.2
safetensors = 0.8.0
huggingface_hub = 1.19.0
d1a_builder_import = PASS
d1a_evaluator_import = PASS
complete_model_manifest = PASS_EXACT / 9_FILES / 0_MISSING / 0_MISMATCH / 0_EXTRA
```

La provenance histórica versionada solo sustenta Python `3.10.11` y torch `2.12.0+cpu`; no se atribuyó retrospectivamente una versión histórica de `sentence_transformers`.

Smoke offline permitido:

```makefile
input = 32_SYNTHETIC_STRINGS
device = CPU
batch_size = 32
max_seq_length = 128
shape = 32x384
dtype = float32
all_finite = true
norm_min = 0.9999999403953552
norm_max = 1.0000001192092896
tolerance = 9.5367431640625e-07
network_used = false
```

Recursos observados:

```makefile
disk_free_bytes = 462320009216
disk_required_margin_bytes = 1466744014
memory_total_bytes = 34070192128
memory_available_bytes = 16895401984
memory_required_margin_bytes = 955233974
capacity_status = PASS_WITH_OBSERVED_FOOTPRINT_DERIVED_MARGINS
```

## Replay histórico opcional-fuerte

Los artefactos históricos locales gobernados estaban disponibles y sus hashes pasaron. Se ejecutó replay read-only de las 21 muestras de integridad:

```makefile
historical_vector_replay = PASS
classification = ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT
sample_count = 21
cosine_min = 0.9999999948279137
max_absolute_difference = 1.1920928955078125e-07
tolerance = 9.5367431640625e-07
```

No se publicaron vectores ni textos del replay.

## Shadow integral

```makefile
input_patch_config = PASS / TWO_CODES_ONLY / FOUR_CONFIG_FIELDS_ONLY
ev03_original_vs_original = PASS / 1056_CASES / 10_VALID_EMPTY_RANKINGS
ev04_frozen_structure = PASS / 1056_CASES
aggregate_positive = PASS / EV03_17 / EV04_28
aggregate_nan_inf_negatives = PASS_FAIL_CLOSED
unified_summary_positive_and_negatives = PASS
manifest_round_trip_and_negatives = PASS
ledger_expected_vs_producer = PASS / 47_EQUALS_47
ledger_negatives = PASS_FAIL_CLOSED
synthetic_19_step_pipeline = PASS / NEGATIVES_FAIL_CLOSED
preauthorization_closed_preflight = PASS / PREAUTHORIZATION_CLOSED_READONLY
```

## Pruebas

Comando focalizado final:

```text
python -m unittest tests.test_0b05c_v05_environment_d1a_readiness tests.test_0b05c_v05_comparator_aggregate_integrity tests.test_0b05c_v05_summary_manifest_ledger_orchestration
```

Resultado final tras la última corrección y regeneración de artefactos:

```makefile
focused_v05_total = 31
focused_v05_pass = 31
focused_v05_skip = 0
focused_v05_fail = 0
focused_v05_error = 0
focused_v05_duration_seconds = 0.821
environment_shadow_duration_seconds = 15.94
```

Regresión razonable v0.4 + v0.5 ejecutada:

```text
python -m unittest tests.test_0b05c_corrective_numerical_gate_v04 tests.test_0b05c_ev04_mrr_contract_v04 tests.test_d1a_corrective_0b05c_runner_v04 tests.test_0b05c_v05_environment_d1a_readiness tests.test_0b05c_v05_comparator_aggregate_integrity tests.test_0b05c_v05_summary_manifest_ledger_orchestration
```

```makefile
regression_total = 72
regression_pass = 69
regression_skip = 0
regression_fail = 2
regression_error = 1
v05_regression_failures = 0
```

Los tres non-successes corresponden a assertions históricas v0.4 que presuponen ausencia del authorization record o estado preautorización, aunque la autorización v0.4 ya fue integrada y consumida antes de este candidato. No se modificaron esos tests ni componentes históricos fuera del alcance permitido.

Suite total ejecutada:

```text
python -m unittest discover -s tests -p "test_*.py"
```

```makefile
tests_total = 614
tests_pass = 595
tests_skip = 1
tests_fail = 13
tests_error = 5
tests_duration_seconds = 163.396
v05_test_failures = 0
```

Los 18 non-successes de la suite total quedan clasificados como incompatibilidades históricas de harness v0.1–v0.4 con estados de autorización ya integrados/consumidos y, en un worktree limpio, ausencia del modelo local ignorado. No apareció ningún fallo en los 31 tests v0.5. No se instalaron ni actualizaron dependencias y no se relajó ningún contrato para ocultar esos resultados.

## Riesgos residuales

Permanecen explícitamente abiertos:

1. `FULL_7644_DOCUMENT_ENCODE`.
2. `FULL_1056_QUERY_ENCODE_AND_EVALUATION`.
3. `RUNTIME_MEMORY_CPU_IO_PEAK`.
4. `FUTURE_OUTPUT_HASHES`.
5. `EXTRAORDINARY_HOST_FAILURE_AFTER_SIDE_EFFECTS`.

Mitigaciones obligatorias antes de una autorización futura:

1. Repetir environment y capacity preflight antes de integrar autorización.
2. Usar el mismo intérprete fingerprinted.
3. Exigir ausencia de los 16 roots v0.5.
4. Permitir una única invocación futura, sin retry ni resume.
5. Preservar evidencia fail-closed.

No se declara `RISK_ZERO` ni garantía de éxito runtime.

## Verificaciones finales

```makefile
diff_base = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
changed_path_count = 19
paths_outside_scope = 0
absolute_host_paths_in_public_artifacts = false
authorization_record_v0.5_present = false
v05_prospective_roots_present = false
v04_partial_roots_used_as_input = false
v04_partial_roots_reused = false
v04_partial_roots_cleaned = false
model_or_vectors_published = false
dependencies_installed_or_updated = false
Attempt05_reexecuted = false
Attempt06_authorized = false
Attempt06_executed = false
main_modified_beyond_prompt35a = false
plan_modified = false
article_modified = false
exp11b_modified = false
exp12_modified = false
candidate_local_remote_identity = true
working_tree_tracked_clean = true
```

## Estado de detención

```makefile
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
NEXT_ACTION = EXTERNAL_AUDIT_REQUIRED
```
