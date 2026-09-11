# RESPUESTA PROMPT 35D — BINDINGS, ENTORNO Y VALIDACIÓN D1a v0.5

## Resultado

```makefile
PROMPT35D = COMPLETED
V05_CANDIDATE = BUILT / CURRENT_ENVIRONMENT_VERIFIED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT
GATE_STATUS = CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED
AUTHORIZATION_READINESS = NOT_AUTHORIZED

branch = codex/0b05c-v05-remediated-preauthorization-candidate-v3
commit = 1f30047b8b3d6d6d484cd6bb96716a0ac1fbd19e
parent = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
tree = 588aa4ae30354fd5e1cb74d488a085f9a7d07384
remote_commit = 1f30047b8b3d6d6d484cd6bb96716a0ac1fbd19e

rejected_prompt35c = 6511e6e72c5f77978699a290c8449c3c6736a71c / NOT_INTEGRATED / NOT_ANCESTOR
main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
origin_main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

El candidato v3 es un único commit con parent directo del `main` científico. Prompt35C se utilizó exclusivamente como fuente de archivos al working tree; su commit no es ancestro del candidato v3 y no fue integrado.

## Diff exacto

Diff contra `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`: **21 paths, 5673 inserciones, 5 eliminaciones**.

| Estado | Blob Git | Bytes | Path |
|---|---|---:|---|
| A | `91e15145699f029ac9d311831adcc83b4ee0ca48` | 2322 | `outputs/audits/0b05c_attempt05_failclosed_v0.4/attempt05_failclosed_record_v0.4.json` |
| M | `ad621a4f7349db08162bcdb91bacd78029398c20` | 29099 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json` |
| M | `859c5e23a9699f33a45b2e9aa9be087ea06a3e15` | 17472 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json` |
| M | `b58d4aca70f7af6dd52077d4b441dcdf1e7bba6c` | 21133 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json` |
| M | `91d87fb3d0e94e07628b3c31e79785d261752e39` | 29152 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json` |
| A | `3e3a0b37f18efb10e987e1e5ec884584a3333019` | 35681 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json` |
| A | `33904414b4d8b96cff16ccfeb29e969306684f9f` | 9561 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_hash_ledger_v0.5.json` |
| A | `6b76cbee47605694fbb2a1f82131ae88cefcbdb0` | 21220 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_manifest_v0.5.json` |
| A | `a046c7a9f463798608bb68dff999cb47415a5264` | 17694 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/d1a_numerical_execution_spec_v0.5.json` |
| A | `e7536586adf30dd6ba9cca2d23c86f5f9af95213` | 21403 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev03_numerical_execution_spec_v0.5.json` |
| A | `5fc85150c99dbe950b74acc0f0a1770c8a4cf930` | 29316 | `outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev04_numerical_execution_spec_v0.5.json` |
| A | `d08dbb1e66cc030e62d95c5b4cf262caa4cecc6b` | 7968 | `outputs/audits/0b05c_v05_preauthorization_readiness/preauthorization_readiness_v0.5.json` |
| A | `18c398f5709257326db67790a9ab7ec64a2da8f6` | 15020 | `src/experiments/evaluate_normative_bm25_corrective_0b05c_v05.py` |
| A | `3acb4634a2dad5509ea8d1cf6cd401a54b9077ce` | 64300 | `src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py` |
| A | `b9e333467e1ac0ab68130b2c31da86a17a8280cc` | 21634 | `src/experiments/run_0b05c_corrective_numerical_v05.py` |
| A | `309cf598ce2ad4413505ffee9ef1a5dfcbc2873f` | 19130 | `src/experiments/run_d1a_corrective_0b05c_v05.py` |
| A | `dea0da0151a892c20ca64376f9ccc2fbe61edd63` | 13545 | `tests/test_0b05c_v05_bindings_environment_d1a_v35d.py` |
| A | `b4c4d36d6f3eadd953d54f615babd50f18bcf7b4` | 7717 | `tests/test_0b05c_v05_comparator_aggregate_integrity.py` |
| A | `f46048c1e95737059134125f2ff55dc4007b568b` | 13839 | `tests/test_0b05c_v05_d1a_ledger_authorization_contracts.py` |
| A | `c0a210315f65e054896de2b2700f19471e676aec` | 7221 | `tests/test_0b05c_v05_environment_d1a_readiness.py` |
| A | `e784e11ab746df57ded9b1f78c09404d5111e6ed` | 8040 | `tests/test_0b05c_v05_summary_manifest_ledger_orchestration.py` |

No se modificaron Plan Maestro, `article/`, EXP11B, EXP12, corpus/config/EVAL congelados ni componentes históricos v0.1-v0.3. Los únicos cambios v0.4 son los cuatro JSON de estado y el fail-close sanitizado de Attempt05 ya admitidos por el bundle previo. No se modificó el authorization record v0.4.

## Cierre de findings

```makefile
F35D-01_AUTHORIZATION_CURRENT_DEPENDENCIES_NOT_BOUND = CLOSED_BY_CODE_TEST_AND_SHADOW
F35D-02_RUNTIME_PROJECT_DEPENDENCY_CLOSURE_INCOMPLETE = CLOSED_BY_CODE_TEST_AND_SHADOW
F35D-03_D1A_SUMMARY_REFERENCE_VALIDATION_REGRESSION = CLOSED_BY_CODE_TEST_AND_SHADOW
F35D-04_CURRENT_EXECUTION_ENVIRONMENT_NOT_AVAILABLE = CLOSED_BY_FRESH_CURRENT_REPROBE
F35D-05_ENVIRONMENT_TRANSITIVE_STACK_NOT_FULLY_BOUND = CLOSED_BY_EXACT_42_DISTRIBUTION_CONTRACT
```

### F35D-01 — Commit actual de autorización congelado

La futura autorización exige ahora:

- un único commit hijo directo del baseline;
- exactamente cinco paths y statuses;
- cuatro modificaciones de gate/spec y un alta nueva del record;
- bindings de dependencias validados contra baseline y commit actual;
- igualdad de blob SHA-1, SHA-256 canónico y size baseline→authorization;
- gate/spec filesystem iguales al commit autorizado;
- tracked tree limpio;
- proyección científica/técnica inmutable.

Contrato exacto del diff futuro:

```makefile
M = outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json
M = outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev03_numerical_execution_spec_v0.5.json
M = outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev04_numerical_execution_spec_v0.5.json
M = outputs/audits/0b05c_corrective_numerical_gate_v0.5/d1a_numerical_execution_spec_v0.5.json
A = outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_numerical_authorization_record_v0.5.json
```

```makefile
direct_parent_exact_five_path_shadow = PASS
baseline_dependency_bindings = PASS
authorization_commit_dependency_bindings = PASS
current_bindings_equal_baseline = true
actual_python_source_changed_in_authorization_commit = FAIL_CLOSED
non_direct_parent_authorization = FAIL_CLOSED
```

El negativo de source drift se ejecutó en un repositorio Git temporal real: el commit modificó los cinco paths permitidos y además un `.py`; fallaron tanto el shape exacto como la validación del binding actual.

### F35D-02 — Closure local y datos runtime

El closure se deriva recursivamente mediante AST desde bytes Git canónicos de cuatro entrypoints. Incluye imports absolutos, relativos, package initializers y `import_module()` constante. Se rederiva en preflight y debe coincidir exactamente con los bindings.

```makefile
project_local_import_closure_count = 31
runtime_data_dependency_count = 22
total_dependency_binding_count = 53
binding_fields = path / git_blob_sha1 / canonical_git_blob_sha256 / canonical_size_bytes
binding_validation = 53/53 PASS
```

Closure local completo:

```text
src/__init__.py
src/bm25_index.py
src/evaluation/__init__.py
src/evaluation/metrics.py
src/experiments/__init__.py
src/experiments/build_bm25_corrective_0b05c_v02.py
src/experiments/build_bm25_corrective_0b05c_v03.py
src/experiments/build_bm25_ev03_historical_recovered_v02.py
src/experiments/build_text2trade_mnrl_index_v02.py
src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py
src/experiments/evaluate_normative_bm25_corrective_0b05c_v04.py
src/experiments/evaluate_normative_bm25_corrective_0b05c_v05.py
src/experiments/evaluate_normative_bm25_flat_data_aduanas_v02.py
src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py
src/experiments/evaluate_text2trade_mnrl_data_aduanas_v02.py
src/experiments/prepare_0b05c_corrective_numerical_gate_v01.py
src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py
src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py
src/experiments/prepare_0b05c_corrective_numerical_gate_v04.py
src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py
src/experiments/run_0b05c_corrective_numerical_v02.py
src/experiments/run_0b05c_corrective_numerical_v05.py
src/experiments/run_d1a_corrective_0b05c_v01.py
src/experiments/run_d1a_corrective_0b05c_v02.py
src/experiments/run_d1a_corrective_0b05c_v05.py
src/experiments/verify_ev03_historical_builder_recovery_v02.py
src/retrieval/__init__.py
src/retrieval/bm25.py
src/retrieval/text2trade_mnrl_v02.py
src/utils/__init__.py
src/utils/paths.py
```

Los seis paths mínimos señalados por la auditoría están incluidos. Quitar cada uno del binding falla cerrado. Un fixture Git con un import local nuevo no binded también falla cerrado.

Nuevas dependencias runtime explícitas añadidas por `baseline_values()`:

```text
outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json
outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json
outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json
outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/run_metadata.json
```

Los otros 18 inputs versionados ya gobernados se preservaron: configs, corpus, EVAL, metadatos e índice BM25, controles EV03/EV04 y controles D1a.

### F35D-03 — Validación fuerte D1a

`d1a_summary_reference()` solo genera referencias después de validar contenido completo:

```makefile
aggregate = 17/17 METRICS / EXACT_ORDER / EXACT_FIELDS / FINITE / DENOMINATOR_AND_VALUES_COHERENT
case_level = 1056/1056 UNIQUE_CASE_IDS / EXACT_SCHEMA / NONEMPTY_NANDINA_REF / NONNEGATIVE_INTEGER_RANKS
execution_manifest = PASS / runner_version_v0.5 / EXACT_V05_RUNNER_OUTPUTS
internal_hash_ledger = EXACT_PATH_SET / NO_DUPLICATES / SHA64 / POSITIVE_SIZE / RECOMPUTED_EXACT
self_path_exclusion = EXACT
```

Negativos ejecutados y fail-closed:

- aggregate con métrica faltante;
- aggregate con NaN;
- case JSONL con 1055 filas;
- case ID duplicado;
- manifest con output v0.4 stale;
- ledger con path faltante;
- ledger con path extra;
- ledger con SHA incorrecto.

No se ejecutó D1a científico para estas pruebas; se usaron fixtures sintéticos temporales.

### F35D-04/F35D-05 — Entorno actual ejecutable

Procedimiento: se reutilizó el `.venv` aislado preexistente del proyecto. No se creó instalación global, no se instaló ni actualizó paquete alguno, no se descargó Python, modelo ni dato científico. El modelo y los artefactos de replay locales se usaron read-only; las rutas host-locales no se persistieron.

```makefile
LAST_KNOWN_TESTED_ENVIRONMENT = PROMPT35B_CODEX_LOCAL_EVIDENCE / NOT_CURRENT_REPROBE
CURRENT_EXECUTION_ENVIRONMENT_READINESS = PASS
python = 3.10.11
implementation = CPython
architecture = 64bit
platform_system = Windows
machine = AMD64
executable_sha256 = b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961
dependencies_installed_or_updated = false
```

Versiones críticas de módulos:

```text
numpy=2.2.6
sentence_transformers=5.5.1
torch=2.12.0+cpu
tqdm=4.68.2
transformers=5.12.1
tokenizers=0.22.2
safetensors=0.8.0
huggingface_hub=1.19.0
```

Closure transitivo gobernado de distribuciones, 42/42 exactas:

```text
annotated-doc=0.0.4
anyio=4.13.0
certifi=2026.5.20
click=8.4.1
colorama=0.4.6
exceptiongroup=1.3.1
filelock=3.29.4
fsspec=2026.4.0
h11=0.16.0
hf-xet=1.5.1
httpcore=1.0.9
httpx=0.28.1
huggingface_hub=1.19.0
idna=3.18
Jinja2=3.1.6
joblib=1.5.3
markdown-it-py=4.2.0
MarkupSafe=3.0.3
mdurl=0.1.2
mpmath=1.3.0
networkx=3.4.2
numpy=2.2.6
packaging=26.2
Pillow=12.3.0
Pygments=2.20.0
PyYAML=6.0.3
regex=2026.5.9
rich=15.0.0
safetensors=0.8.0
scikit-learn=1.7.2
scipy=1.15.3
sentence-transformers=5.5.1
setuptools=65.5.0
shellingham=1.5.4
sympy=1.14.0
threadpoolctl=3.6.0
tokenizers=0.22.2
torch=2.12.0
tqdm=4.68.2
transformers=5.12.1
typer=0.25.1
typing_extensions=4.15.0
```

Reprobe final fresco:

```makefile
project_imports = 31/31 PASS
model_manifest = 9/9 PASS_EXACT
model_missing = 0
model_extra = 0
model_mismatch = 0
offline_smoke = PASS
offline_smoke_shape = 32x384
offline_smoke_dtype = float32
offline_smoke_finite = true
offline_smoke_norm_min = 0.9999999403953552
offline_smoke_norm_max = 1.0000001192092896
offline_smoke_tolerance = 9.5367431640625e-07
historical_vector_replay = 21/21 PASS
replay_cosine_min = 0.9999999948279137
replay_max_absolute_difference = 1.1920928955078125e-07
replay_tolerance = 9.5367431640625e-07
disk_free_bytes = 456609849344
disk_required_margin_bytes = 1466744014
memory_available_bytes = 14968221696
memory_required_margin_bytes = 955233974
capacity = PASS
```

## Preflight y shadows

```makefile
preauthorization_closed_preflight = PASS / PREAUTHORIZATION_CLOSED_READONLY
d1a_closed_preflight = PASS / PREEXECUTION_CLOSED_READONLY
d1a_eval_identity = PASS_EXACT
d1a_runtime_config_changed_fields = EXACTLY_4
dependency_bindings = 53/53 PASS
stale_artifact_identities = PASS / 0_CURRENT_STALE
stale_source_identities = PASS / 0_CURRENT_STALE
absolute_host_paths_in_public_artifacts = 0
authorization_record_v05_present = false
future_v05_roots_present = 0/16
physical_runtime_ledger = PASS / MISSING_EXTRA_FAILURE_SNAPSHOT_NEGATIVES_FAIL_CLOSED
manifest_provenance = PASS / NEGATIVES_FAIL_CLOSED
synthetic_19_step_orchestration = PASS / NEGATIVES_FAIL_CLOSED
```

## Tests completos

Clasificación: `CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`.

### Tests shadow nuevos iniciales

```text
python -m unittest tests.test_0b05c_v05_bindings_environment_d1a_v35d -v
11 tests / 11 PASS / 0 FAIL / 0 ERROR / 0 SKIP / 122.688 s
```

### Primera suite ampliada

```text
python -m unittest tests.test_0b05c_v05_environment_d1a_readiness tests.test_0b05c_v05_comparator_aggregate_integrity tests.test_0b05c_v05_summary_manifest_ledger_orchestration tests.test_0b05c_v05_d1a_ledger_authorization_contracts tests.test_0b05c_v05_bindings_environment_d1a_v35d -v
55 tests / 52 PASS / 0 FAIL / 3 ERROR / 0 SKIP / 269.499 s
```

Los tres errores fueron incompatibilidades de fixtures/allowlist con los nuevos campos de provenance y la cadena de negativo stale D1a; no fueron fallos contractuales. Se corrigieron únicamente esos tests/allowlist.

### Retest focal de los tres errores

```text
3 tests / 3 PASS / 0 FAIL / 0 ERROR / 0 SKIP / 48.442 s
```

### Suite focalizada final

```text
python -m unittest tests.test_0b05c_v05_environment_d1a_readiness tests.test_0b05c_v05_comparator_aggregate_integrity tests.test_0b05c_v05_summary_manifest_ledger_orchestration tests.test_0b05c_v05_d1a_ledger_authorization_contracts tests.test_0b05c_v05_bindings_environment_d1a_v35d -v
55 tests / 55 PASS / 0 FAIL / 0 ERROR / 0 SKIP / 398.089 s
```

### Regresión v0.4 relevante

```text
python -m unittest tests.test_0b05c_corrective_numerical_gate_v04 tests.test_0b05c_ev04_mrr_contract_v04 tests.test_d1a_corrective_0b05c_runner_v04 -v
41 tests / 38 PASS / 2 FAIL / 1 ERROR / 0 SKIP / 15.691 s
EV04 MRR = 23/23 PASS
D1a v0.4 = 4/4 PASS
```

Los tres non-successes son los históricos ya conocidos del harness v0.4 consumido: espera ausencia del authorization record, espera seis JSON aunque el record es el séptimo y su preflight cerrado exige record ausente. Se reportan sin ocultarlos y sin modificar código histórico fuera de alcance.

## Preservaciones y estado

```makefile
MRR_AT_100 = EXACT_RATIONAL_SUM_THEN_ONE_FLOAT_CONVERSION
MRR_AT_200 = LEGACY_SUM_FLOAT_RECIPROCAL_RANK_IN_FROZEN_ROW_ORDER
MRR_101_200_CONTRIBUTION = EXACT_RATIONAL_DIFFERENCE
EV04_AGGREGATE_ROWS = 28
EV03_SEMANTICS = RECOVERED_HISTORICAL_DROP_SINGLE_CHARACTER_TOKENS
DECISION906_CHANGED_CODES = 87044110 / 87045110 ONLY
D1A_RETRAINING = FORBIDDEN
EVAL_N = 1056
PIPELINE_STEPS = 19
V04_PARTIAL_ROOTS = NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05

ATTEMPT05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
EV03_NUMERICAL_EXECUTION = NOT_AUTHORIZED
EV04_NUMERICAL_EXECUTION = NOT_AUTHORIZED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION = NOT_AUTHORIZED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED

Attempt05_reexecuted = false
Attempt06_authorized = false
Attempt06_executed = false
scientific_retrieval_executed = false
EV03_real_executed = false
EV04_real_executed = false
D1A_complete_executed = false
EVAL_real_executed = false
full_7644_document_encode_executed = false
full_1056_query_execution_executed = false
main_integrated = false
candidate_working_tree_clean = true
```

## Riesgos residuales

No se declara `RISK_ZERO`. Permanecen:

- `FULL_7644_DOCUMENT_ENCODE`
- `FULL_1056_QUERY_ENCODE_AND_EVALUATION`
- `RUNTIME_MEMORY_CPU_IO_PEAK`
- `FUTURE_OUTPUT_HASHES`
- `EXTRAORDINARY_HOST_FAILURE_AFTER_SIDE_EFFECTS`

## Dictamen

```makefile
BLOCKERS_IN_CODE_TEST_SHADOW_AND_CURRENT_ENVIRONMENT_SCOPE = NONE_DETECTED
EXTERNAL_AUDIT_REQUIRED = true
READY_FOR_ATTEMPT06 = NOT_DECLARED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

El candidato quedó publicado exclusivamente en `origin/codex/0b05c-v05-remediated-preauthorization-candidate-v3`. No se integró a `main` y no se abrió ni ejecutó ninguna autorización numérica.
