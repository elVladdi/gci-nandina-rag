### A. Preflight Git

```makefile
branch = codex/0b05c-corrective-numerical-gate-v02
base_candidate = 59dc445d8128dd71f48d26eac66c9ae8d0c21e38
base_candidate_parent = b0a1e61f70f42aa2048338965cc003e032d3a493
base_candidate_tree = 3243c6bcc5030dd07c86bd593596e420212541cf
origin_main = 43291c312c2934aae03f3c087dd0a1ae594341b7
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
preflight_git = PASS
```

Las identidades requeridas coincidieron antes de escribir. La rama científica estaba limpia y sincronizada con el microclose del Prompt 10. El trabajo se realizó en su worktree separado, sin modificar `main`.

### B. F007 - metadata builder/evaluator

Antes, el builder v0.2 publicaba `input_sha256` e `index_sha256` top-level junto con `bm25_params` y `semantics`, pero no el contrato anidado consumido por `validate_dynamic_inputs()`.

Ahora preserva esos campos históricos y añade inequívocamente: `arm`; `bm25_params.k1`; `bm25_params.b`; `input.corpus_path`; `input.corpus_sha256`; `input.config_path`; `input.config_sha256`; `output.bm25_index_path`; `output.bm25_index_sha256`; y `output.metadata_path`. No se modificó el evaluator v0.1.

El test positivo crea config BM25 1.5/0.75 y corpus NANDINA sintético dentro de `TemporaryDirectory`, ejecuta realmente `build_bm25_corrective_0b05c_v02.build()`, pasa su índice y metadata a `evaluate_normative_bm25_corrective_0b05c_v01.validate_dynamic_inputs()`, comprueba ambos SHA y carga el índice con el `doc_id` esperado. El test negativo muta `input.corpus_sha256` y confirma `ContractViolation`. No se invocó EVAL real ni `evaluate_arm()` sobre datos reales.

### C. F008 - D1a unified authorization binding

`run_d1a_corrective_0b05c_v02.execute_authorized()` acepta ahora un `authorization_proof` validado. Sin proof, el camino standalone importa localmente el runner unificado y ejecuta primero `preflight_authorized(ROOT)`, antes de cualquier side effect; así se evita una dependencia circular a import time. El proof debe declarar `PASS`, modo `AUTHORIZED_PREFLIGHT_ONLY`, las cuatro autorizaciones `AUTHORIZED`, baseline válido, authorization record y binding completo, además de bindings de gate y los tres specs.

El runner unificado conserva el proof obtenido en el paso `01_unified_preflight` y lo pasa a D1a en el paso 12. D1a no repite entonces el control de roots ausentes después de EV03/EV04, pero vuelve a validar la prueba y su autorización propia. Los tests demuestran fail-closed con autorización D1a parcial, fail-closed del camino directo con gate unificado cerrado y aceptación segura de un proof sintético completo sin reejecutar el preflight unificado. Ningún test creó roots reales.

### D. F009 - runtime authorization provenance

Se congeló el constructor contractual del futuro `runtime_authorization_record_v0.2.json`. Preserva: `status`; `mode`; `execution_authorization_commit`; `authorization_baseline_commit`; las cuatro autorizaciones; referencia al authorization record mediante `path`, Git blob SHA-1, SHA-256 canónico y size; `baseline_external_audit`; y bindings autorizados de `unified_gate`, `ev03_spec`, `ev04_spec` y `d1a_spec`.

El futuro execution manifest referencia el runtime authorization record mediante `path`, `sha256` y `size_bytes`, y conserva `execution_authorization_commit` y `authorization_baseline_commit`. El ledger mantiene runtime record y manifest en su allowlist. Tests con fixtures verifican preservación completa del proof, referencia hash/size del manifest y rechazo por baseline o record binding ausente. No se creó ningún record real.

### E. F010 - D1a aggregate integrity

`_d1a_summary_reference()` exige ahora exactamente las 17 métricas del `comparison_contract.aggregate_metrics`, con nombres únicos y orden exacto: Top@1, Top@3, Top@5, Top@10, Top@50, Recall@100, Recall@200, MRR@100, MRR@200, Exact@100, Exact@200, HS6@100, HS6@200, HS4@100, HS4@200, Chapter@100 y Chapter@200.

Cada fila debe contener exactamente la evidencia contractual necesaria: `metric`, `original_numerator`, `corrected_numerator`, `denominator`, `original_value`, `corrected_value` y `absolute_delta`; todos los campos numéricos deben ser números finitos y no booleanos. Los tests rechazan lista vacía, métrica faltante, nombre/orden alterado y fila incompleta; el fixture completo de 17 métricas pasa.

### F. Preservación F001-F006

F001-F006 permanecen cerrados. No se debilitó el transition/record schema de autorización, EV03 `PASS_EXACT`, EV04 `PASS_EXACT`, la coherencia commands/roots, el exact runtime ledger ni las referencias D1a del unified summary. La suite v0.2 ampliada y las regresiones v0.1/D1a/BM25 pasaron sin failures ni errors.

### G. Invariantes científicos

Permanecieron sin cambio: EV03 `DROP_SINGLE_CHARACTER_TOKENS`; `k1=1.5`; `b=0.75`; EVAL N=1,056; depth EV03=100; depth EV04=200; jerarquía/collapse/ties EV04; Decision906 exactamente para `87044110` y `87045110`; texto congelado `Inferior a 4,537 t`; weights/config/scoring/ranking D1a; `FREEZE_ORIGINAL_D1A_WEIGHTS`; `must_not_retrain=true`; `FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD`; orden de 19 pasos; y los 16 roots v0.2. No cambió ningún artefacto v0.1.

### H. Gate state

```makefile
gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
authorization_readiness = NOT_AUTHORIZATION_READY
EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED
EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED
D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED
UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED
authorization_record_v02 = ABSENT
runtime_authorization_record_v02 = ABSENT
future_roots_present = false
corrective_retrieval_executed = false
corrective_metrics_computed = false
```

### I. Tests v0.2

```makefile
tests_v02_expanded = RUN 56 / PASS 56 / FAIL 0 / ERROR 0 / SKIP 0
builder_to_evaluator_temp_positive = PASS
builder_to_evaluator_mutated_metadata_negative = PASS
F008_authorization_binding_tests = PASS
F009_runtime_provenance_tests = PASS
F010_aggregate_integrity_tests = PASS
```

No se afirmó CI. Los caminos futuros se probaron con fixtures temporales y mocks; ninguna prueba alcanzó el pipeline numérico real.

### J. Regresiones

```makefile
tests_ev03_recovery_v02 = RUN 16 / PASS 16 / FAIL 0 / ERROR 0 / SKIP 0
tests_v01_gate = RUN 33 / PASS 33 / FAIL 0 / ERROR 0 / SKIP 0
tests_d1a_preexecution = RUN 8 / PASS 8 / FAIL 0 / ERROR 0 / SKIP 0
tests_d1a_runner = RUN 27 / PASS 27 / FAIL 0 / ERROR 0 / SKIP 0
tests_bm25_flat = RUN 13 / PASS 13 / FAIL 0 / ERROR 0 / SKIP 0
tests_bm25_hierarchical = RUN 17 / PASS 17 / FAIL 0 / ERROR 0 / SKIP 0
tests_required_bundle = RUN 170 / PASS 169 / FAIL 0 / ERROR 0 / SKIP 1
tests_total = RUN 549 / PASS 548 / FAIL 0 / ERROR 0 / SKIP 1
```

Cada módulo obligatorio ejecutado aisladamente pasó todos sus tests. La ejecución agregada y la suite total terminaron `OK`, con un único skip y sin failures/errors. Para la regresión que verifica la identidad SHA del modelo local ignorado se usó temporalmente una copia exacta del archivo congelado, sin cargarlo ni ejecutar retrieval, y se eliminó al finalizar.

### K. Postcommit detached validation

```makefile
postcommit_detached_head = c44f447cb941c512cd70712cf7c3e4bc670ab05a
postcommit_detached_preflight = PASS / PREEXECUTION_CLOSED_READONLY
postcommit_detached_tests_v02 = RUN 56 / PASS 56 / FAIL 0 / ERROR 0 / SKIP 0
postcommit_future_roots_present = false
```

El preflight fue exclusivamente read-only. No se ejecutó `--execute-authorized`.

### L. Aislamiento

```makefile
main_modified = false
plan_maestro_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false
v01_artifacts_modified = false
authorization_record_created = false
runtime_authorization_record_created = false
future_roots_present = false
numerical_execution_occurred = false
corrective_metrics_computed = false
```

Los seis JSON contractuales v0.2 se regeneraron determinísticamente; cuatro cambiaron por bindings/schema y dos permanecieron byte-idénticos.

### M. Commit candidato

```makefile
branch = codex/0b05c-corrective-numerical-gate-v02
commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
parent = 59dc445d8128dd71f48d26eac66c9ae8d0c21e38
tree = 41122fe6de833d7be83a2211e99cdd00561bc26e
commit_message = fix: close remaining 0b05c v0.2 execution contract gaps
compare_vs_origin_main = 3 ahead / 0 behind
compare_vs_prompt10_candidate = 1 ahead / 0 behind
remote_candidate = c44f447cb941c512cd70712cf7c3e4bc670ab05a
push = PASS / FAST_FORWARD 59dc445..c44f447
working_tree_clean = true
```

Changed paths exactos:

1. `docs/0B05C_CORRECTIVE_NUMERICAL_GATE_V02.md`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_gate_hash_ledger_v0.2.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_gate_manifest_v0.2.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/d1a_numerical_execution_spec_v0.2.json`
6. `src/experiments/build_bm25_corrective_0b05c_v02.py`
7. `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py`
8. `src/experiments/run_0b05c_corrective_numerical_v02.py`
9. `src/experiments/run_d1a_corrective_0b05c_v02.py`
10. `tests/test_0b05c_corrective_numerical_gate_v02.py`

### N. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/11_RESPUESTA_MICROCLOSE_GATE_RUNNER_0B05C_V02_F007_F010.md
admin_commit = SELF / docs: persist prompt 11 gate microclose report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### O. Estado científico

GROUP_2 = EN_CURSO

0B05C_NUMERICAL_GATE_V02 = CANDIDATE_PENDING_EXTERNAL_AUDIT

0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY

EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
