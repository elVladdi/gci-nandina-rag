# RESPUESTA PROMPT 35F - RESTAURAR CPYTHON 3.10.11 Y PUBLICAR v4

## Estado final

```makefile
PROMPT35F = COMPLETED
ENVIRONMENT_RESTORATION = PASS / ISOLATED / EXACT
F35E_01_HISTORICAL_REPLAY_CONTRACT = CLOSED_BY_CODE_TEST_AND_FRESH_EXACT_REPROBE
V05_CANDIDATE_V4 = BUILT / PUBLISHED / PENDING_EXTERNAL_AUDIT
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

## Trust check del instalador

La descarga se realizo exclusivamente desde la fuente autorizada y se elimino al terminar. No se versiono ni publico el instalador.

```makefile
installer_host = www.python.org
installer_name = python-3.10.11-amd64.exe
installer_size_bytes = 29037240
installer_authenticode_status = Valid
installer_signer = Python Software Foundation
installer_sha256 = d8dede5005564b408ba50317108b765ed9c3c510342a598f9fd42681cbe0648b
installer_committed = false
installer_published = false
installer_temp_present_after_completion = false
```

El `TargetDir` se derivo de `home` en `.venv/pyvenv.cfg`. Se verifico que corresponde a una ubicacion per-user, que el contrato del venv declara `version = 3.10.11` y que no es una ruta global o de sistema.

Al verificar el target con acceso per-user autorizado se encontro intacta la instalacion CPython original, con archivos anteriores a Prompt35F. El diagnostico de ausencia de Prompt35E fue una limitacion de acceso del sandbox: no fue necesario ejecutar el instalador sobre una instalacion existente. Se preservo el runtime exacto y se probo primero el `.venv` existente, como exige el prompt.

```makefile
restoration_mode = EXISTING_PER_USER_CPYTHON_REACTIVATED_AND_VERIFIED
installer_execution_count = 0
fallback_venv_created = false
existing_venv_reused = true
global_python_modified = false
global_path_modified = false
global_launcher_modified = false
packages_installed = NONE
packages_updated = NONE
models_downloaded = false
scientific_data_downloaded = false
```

## Precondiciones Git

```makefile
main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
origin/main = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5

prompt35d_reference = 1f30047b8b3d6d6d484cd6bb96716a0ac1fbd19e
prompt35d_integrated = false
prompt35d_used_as_ancestor = false
remote_v4_before_prompt35f = ABSENT
authorization_record_v05_in_main = ABSENT
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
prospective_roots_v05_before_build = 0/16
v04_partial_roots_used_as_scientific_inputs = false
```

## Candidato v4

```makefile
branch = codex/0b05c-v05-remediated-preauthorization-candidate-v4
commit = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
parent = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
tree = 6ffb42b20182e9abf1f1adb95083a95bae5dfd67
commit_count_ahead_of_parent = 1
commit_count_behind_parent = 0
merge_commit = false
local_remote_commit_identity = true
local_remote_tree_identity = true
published_branch = origin/codex/0b05c-v05-remediated-preauthorization-candidate-v4
main_integrated = false
working_tree_clean = true
```

El worktree v4 detenido por Prompt35E fue devuelto primero al baseline exacto con limpieza de indice y working tree. Despues se recuperaron los 21 paths de Prompt35D desde Git como contenido, no como historia, y F35E se reaplico. El commit final tiene parent directo `c873ff1...`.

## Diff exacto contra c873ff1

```text
A  91e15145699f029ac9d311831adcc83b4ee0ca48  outputs/audits/0b05c_attempt05_failclosed_v0.4/attempt05_failclosed_record_v0.4.json
M  ad621a4f7349db08162bcdb91bacd78029398c20  outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json
M  859c5e23a9699f33a45b2e9aa9be087ea06a3e15  outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json
M  b58d4aca70f7af6dd52077d4b441dcdf1e7bba6c  outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json
M  91d87fb3d0e94e07628b3c31e79785d261752e39  outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json
A  1d80f63477a15bf299aa17c076b80f40e1d54b50  outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json
A  33904414b4d8b96cff16ccfeb29e969306684f9f  outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_hash_ledger_v0.5.json
A  d75ce4f4f3e7943a6ac6f02d96a207c0120b255a  outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_manifest_v0.5.json
A  a046c7a9f463798608bb68dff999cb47415a5264  outputs/audits/0b05c_corrective_numerical_gate_v0.5/d1a_numerical_execution_spec_v0.5.json
A  e7536586adf30dd6ba9cca2d23c86f5f9af95213  outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev03_numerical_execution_spec_v0.5.json
A  5fc85150c99dbe950b74acc0f0a1770c8a4cf930  outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev04_numerical_execution_spec_v0.5.json
A  7fcd809c5388baaca923d3479a453aecc32f3eb6  outputs/audits/0b05c_v05_preauthorization_readiness/preauthorization_readiness_v0.5.json
A  18c398f5709257326db67790a9ab7ec64a2da8f6  src/experiments/evaluate_normative_bm25_corrective_0b05c_v05.py
A  44a3cb39702d2104e527439d3f67b0a457283dff  src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py
A  73f782abb2cef6479976f3beda8270b284fafde3  src/experiments/run_0b05c_corrective_numerical_v05.py
A  309cf598ce2ad4413505ffee9ef1a5dfcbc2873f  src/experiments/run_d1a_corrective_0b05c_v05.py
A  dea0da0151a892c20ca64376f9ccc2fbe61edd63  tests/test_0b05c_v05_bindings_environment_d1a_v35d.py
A  b4c4d36d6f3eadd953d54f615babd50f18bcf7b4  tests/test_0b05c_v05_comparator_aggregate_integrity.py
A  f46048c1e95737059134125f2ff55dc4007b568b  tests/test_0b05c_v05_d1a_ledger_authorization_contracts.py
A  c41f17f398f369ce674ed9b1048d58fe36261578  tests/test_0b05c_v05_environment_d1a_readiness.py
A  8a19be22abb53ccc26292387c011960e83adfed8  tests/test_0b05c_v05_historical_replay_contract_v35e.py
A  3506521052331ef9438136b740e88f3f050f730d  tests/test_0b05c_v05_summary_manifest_ledger_orchestration.py
```

```makefile
changed_paths = 22
insertions = 6091
deletions = 5
diff_check = PASS
absolute_host_paths_in_scientific_candidate = 0
```

Los unicos cambios v0.4 son los cinco paths de estado/fail-close ya contenidos en Prompt35D. No se modificaron paths historicos v0.1-v0.3, Plan, Article, EXP11B ni EXP12.

## Diferencias conceptuales frente a Prompt35D

```text
M  outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json
M  outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_gate_manifest_v0.5.json
M  outputs/audits/0b05c_v05_preauthorization_readiness/preauthorization_readiness_v0.5.json
M  src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py
M  src/experiments/run_0b05c_corrective_numerical_v05.py
M  tests/test_0b05c_v05_environment_d1a_readiness.py
A  tests/test_0b05c_v05_historical_replay_contract_v35e.py
M  tests/test_0b05c_v05_summary_manifest_ledger_orchestration.py
```

Los seis artefactos gobernados v0.5 fueron regenerados desde el codigo final. Los tres que no aparecen en esta comparacion conservaron bytes identicos a Prompt35D.

## F35E materializado

```makefile
historical_vector_replay_required = true
required_replay_status = PASS
required_replay_sample_count = 21
required_replay_classification = ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT
optional_or_not_available_can_return_preflight_pass = false

vectors_presence_sha_size = FAIL_CLOSED
docstore_presence_sha_size = FAIL_CLOSED
id_map_presence_sha_size = FAIL_CLOSED
vector_integrity_gate_presence_sha_metadata = FAIL_CLOSED
sample_presence_sha_csv = FAIL_CLOSED
sample_exact_rows = 21
sample_unique_vector_indices = 21
sample_index_range = VECTORS_DOCSTORE_ID_MAP
sample_stored_text_sha256 = EXACT_AND_RECOMPUTED
sample_doc_id_code_mapping = EXACT

runtime_authorization_record_preserves_required_replay = true
future_execution_manifest_preserves_required_replay = true
readiness_preserves_required_replay = true
```

La autoridad de sizes ya existente es `docs/exp04_text2trade_mnrl_d1a_v02_reproducibility_manifest.json`. Se incorporo como dependencia runtime versionada. Por esa derivacion requerida y documentada:

```makefile
project_local_import_closure = 31
runtime_data_dependencies = 23
total_candidate_bindings = 54
bindings_formula = 31_SOURCE + 23_DATA
```

No se invento ningun SHA ni size.

## Environment fingerprint final

```makefile
python_version = 3.10.11
python_implementation = CPython
architecture = 64bit
platform_system = Windows
machine = AMD64
pointer_bits = 64
venv_launcher_sha256 = b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961
```

Dependencias criticas exactas:

```text
numpy 2.2.6
sentence_transformers 5.5.1
torch 2.12.0+cpu
tqdm 4.68.2
transformers 5.12.1
tokenizers 0.22.2
safetensors 0.8.0
huggingface_hub 1.19.0
```

Closure de 42 distribuciones exacta:

```text
annotated-doc 0.0.4
anyio 4.13.0
certifi 2026.5.20
click 8.4.1
colorama 0.4.6
exceptiongroup 1.3.1
filelock 3.29.4
fsspec 2026.4.0
h11 0.16.0
hf-xet 1.5.1
httpcore 1.0.9
httpx 0.28.1
huggingface_hub 1.19.0
idna 3.18
Jinja2 3.1.6
joblib 1.5.3
markdown-it-py 4.2.0
MarkupSafe 3.0.3
mdurl 0.1.2
mpmath 1.3.0
networkx 3.4.2
numpy 2.2.6
packaging 26.2
Pillow 12.3.0
Pygments 2.20.0
PyYAML 6.0.3
regex 2026.5.9
rich 15.0.0
safetensors 0.8.0
scikit-learn 1.7.2
scipy 1.15.3
sentence-transformers 5.5.1
setuptools 65.5.0
shellingham 1.5.4
sympy 1.14.0
threadpoolctl 3.6.0
tokenizers 0.22.2
torch 2.12.0
tqdm 4.68.2
transformers 5.12.1
typer 0.25.1
typing_extensions 4.15.0
```

## Reprobe fresco exacto

```makefile
reprobe_status = PASS
reprobe_mode = PREAUTHORIZATION_ENVIRONMENT_READINESS_ONLY
executable_sha_exact = PASS
python_platform_exact = PASS
critical_packages_8_exact = PASS
transitive_distributions_42_exact = PASS
project_local_imports_31_exact = PASS
runtime_data_dependency_bindings_23_exact = PASS
model_manifest = 9/9 PASS_EXACT

offline_smoke_shape = 32x384
offline_smoke_dtype = float32
offline_smoke_all_finite = true
offline_smoke_norm_min = 0.9999999403953552
offline_smoke_norm_max = 1.0000001192092896
offline_smoke_tolerance = 0.00000095367431640625
offline_smoke_norms_within_tolerance = true

historical_vector_replay_required = true
historical_vector_replay_status = PASS
historical_vector_replay_sample_count = 21
historical_vector_replay_cosine_min = 0.9999999948279137
historical_vector_replay_max_absolute_difference = 0.00000011920928955078125
historical_vector_replay_tolerance = 0.00000095367431640625
historical_vector_replay_classification = ENVIRONMENT_PARITY_EVIDENCE / NOT_NEW_SCIENTIFIC_RESULT

disk_free_bytes = 454952071168
disk_required_margin_bytes = 1466744014
memory_total_bytes = 34070192128
memory_available_bytes = 16363737088
memory_required_margin_bytes = 955233974
capacity = PASS

authorization_record_v05_present = false
prospective_roots_v05_present = 0/16
scientific_execution = false
```

El preflight cerrado post-commit volvio a pasar desde `HEAD` con `54` bindings, `31` imports, `23` dependencias, authorization record ausente y `0/16` roots.

## Tests

Todos los tests locales se clasifican exclusivamente como:

`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`

### Suite F35E inicial

```makefile
tests_f35e_initial = 15/15 PASS
elapsed = 51.870s
```

### Suite focalizada v0.5 final

```makefile
tests_v05_focused = 71/71 PASS
failures = 0
errors = 0
skips = 0
elapsed = 514.927s
```

Incluye:

- F35E final, 16 tests;
- bindings y autorizacion;
- D1a strong validation;
- manifest, physical ledger y orquestacion de 19 pasos;
- comparator y aggregate integrity;
- environment readiness.

Negativos ambientales repetidos:

```makefile
required_replay_NOT_AVAILABLE = FAIL_CLOSED / PASS
replay_sample_count_not_21 = FAIL_CLOSED / PASS
package_version_drift = FAIL_CLOSED / PASS
executable_sha_drift = FAIL_CLOSED / PASS
project_import_closure_drift = FAIL_CLOSED / PASS
capacity_below_margin = FAIL_CLOSED / PASS
```

Negativos fisicos F35E 1-13:

```makefile
vectors_absent = FAIL_CLOSED / PASS
docstore_absent = FAIL_CLOSED / PASS
id_map_absent = FAIL_CLOSED / PASS
sample_absent = FAIL_CLOSED / PASS
sample_sha_mismatch = FAIL_CLOSED / PASS
sample_20_rows = FAIL_CLOSED / PASS
sample_22_rows = FAIL_CLOSED / PASS
duplicate_vector_index = FAIL_CLOSED / PASS
out_of_range_vector_index = FAIL_CLOSED / PASS
malformed_stored_text_sha256 = FAIL_CLOSED / PASS
replay_status_not_PASS = FAIL_CLOSED / PASS
replay_sample_count_not_21 = FAIL_CLOSED / PASS
optional_or_not_available_preflight_result = FAIL_CLOSED / PASS
positive_physical_21_of_21 = PASS / ZERO_SCIENTIFIC_SIDE_EFFECTS
```

### Regresion v0.4 relevante

```makefile
tests_v04_total = 41
tests_v04_pass = 38
tests_v04_failures = 2
tests_v04_errors = 1
tests_v04_skips = 0
elapsed = 13.382s
new_non_successes = 0
```

Los tres non-successes son exactamente los historicos ya conocidos: el harness v0.4 consumido espera authorization record ausente, espera seis JSON aunque el record es el septimo y el preflight cerrado v0.4 rechaza el record presente. EV04 MRR y D1a v0.4 permanecen pasando.

## Preservaciones

```makefile
MRR_AT_100 = EXACT_RATIONAL_SUM_THEN_ONE_FLOAT_CONVERSION / UNCHANGED
MRR_AT_200 = LEGACY_SUM_FLOAT_RECIPROCAL_RANK_IN_FROZEN_ROW_ORDER / UNCHANGED
MRR_101_200_CONTRIBUTION = EXACT_RATIONAL_DIFFERENCE / UNCHANGED
EV04_AGGREGATE_ROWS = 28 / UNCHANGED
EV03_SEMANTICS = RECOVERED_HISTORICAL_DROP_SINGLE_CHARACTER_TOKENS / UNCHANGED
DECISION906_CHANGED_CODES = 87044110,87045110 ONLY
D1A_RETRAINING = FORBIDDEN
EVAL_N = 1056
PIPELINE_STEPS = 19
FUTURE_ROOTS = 16
V04_PARTIAL_ROOTS = NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05
FUTURE_AUTHORIZATION_COMMIT = DIRECT_PARENT_EXACT_FIVE_PATH_DIFF
D1A_STRONG_VALIDATION = PRESERVED
PHYSICAL_RUNTIME_LEDGER = PRESERVED
MANIFEST_PROVENANCE = PRESERVED_AND_EXTENDED_WITH_REQUIRED_REPLAY
ATTEMPT05_FAIL_CLOSE = PRESERVED

plan_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false
main_modified = false
authorization_record_v05_created = false
Attempt06_authorized = false
Attempt06_executed = false
Attempt05_reexecuted = false
retrieval_scientific_executed = false
EV03_real_executed = false
EV04_real_executed = false
D1a_complete_executed = false
EVAL_real_executed = false
```

## Riesgos residuales

Permanecen como riesgos runtime inevitables, sin convertirlos en resultados:

```text
FULL_7644_DOCUMENT_ENCODE
FULL_1056_QUERY_ENCODE_AND_EVALUATION
RUNTIME_MEMORY_CPU_IO_PEAK
FUTURE_OUTPUT_HASHES
EXTRAORDINARY_HOST_FAILURE_AFTER_SIDE_EFFECTS
```

```makefile
READY_FOR_ATTEMPT06 = NOT_DECLARED
EXTERNAL_AUDIT_REQUIRED = true
AUTHORIZED = false
CLOSED = false
```
