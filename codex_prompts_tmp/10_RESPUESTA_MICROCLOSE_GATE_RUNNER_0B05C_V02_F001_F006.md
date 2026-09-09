### A. Preflight Git

```makefile
origin_main = 43291c312c2934aae03f3c087dd0a1ae594341b7
initial_candidate = b0a1e61f70f42aa2048338965cc003e032d3a493
initial_candidate_parent = 43291c312c2934aae03f3c087dd0a1ae594341b7
initial_candidate_tree = cd8247a143e8fbb033c96d358e15a408c86809d1
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
preflight_git = PASS
```

Todas las identidades requeridas coincidieron antes de escribir. El trabajo se realizó sobre `codex/0b05c-corrective-numerical-gate-v02`, en un worktree separado y sin tocar la evidencia local de los Intentos 01/02.

### B. F001 - authorization transition

`preflight_authorized()` quedó fail-closed antes del primer side effect. Exige gate `APPROVED / INTEGRATED`, readiness `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`, las cuatro autorizaciones del gate, las autorizaciones coherentes de EV03/EV04/D1a, worktree tracked limpio, 16 roots ausentes, bindings Git exactos y toda identidad `FROZEN_FILE_IDENTITY` presente con size/SHA exactos.

Se congeló el schema v2 del futuro authorization record, sin crearlo. El record deberá declarar un baseline proper-ancestor con auditoría externa `PASS / APPROVED_FOR_INTEGRATION` y enlazar gate + tres specs mediante `path`, Git blob SHA-1, SHA-256 de bytes del blob y size. La comparación baseline/candidato permite exclusivamente gate status, readiness, cuatro estados de autorización, presencia del record y los tres estados correlativos de specs. Patches, roots, commands, semántica, métricas, builders, evaluators, modelo, bindings, orden y schema de comparación permanecen inmutables.

Tests negativos verifican que cambiar solo los cuatro strings del gate no autoriza, que el record es obligatorio y que una mutación científica del baseline bloquea la transición.

### C. F002 - EV03 exact control

Antes de emitir `PASS_EXACT`, EV03 valida ejecutablemente: logical index identity `EXACT`; 50,327 filas de ranking; 1,056 filas de case summary; SHA-256 exactos `d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015` y `f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0`; schemas exactos; filas lógicas exactas; metric table exacta; full metrics exactas. Cada requisito produce un boolean en `checks`, y cualquier falso lanza `ContractViolation`.

La identidad lógica reutiliza `verify_ev03_historical_builder_recovery_v02.logical_identity()` contra el índice histórico congelado. Los tests separan mismatch de bytes de ranking con filas lógicas iguales, mismatch del summary, row count, logical index y métricas.

### D. F003 - EV04 exact control + commands

EV04 exige mecánicamente los SHA congelados de ranking `fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662` y summary `17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634`, además de schemas, filas y métricas exactas, antes de `PASS_EXACT`.

Los commands se generan explícitamente desde los roots v0.2 canónicos. Se eliminó la transformación textual genérica que conservaba nombres alternativos. Tests parsean los argumentos y prueban correspondencia con los cinco roots de cada brazo, incluida la ausencia de los antiguos paths EV04 divergentes.

### E. F004 - exact runtime ledger

El gate congela 46 expected paths. Incluye explícitamente los tres file-roots JSONL de corpus, índices y metadata EV03/EV04, outputs de control y correctivos, outputs e integridad D1a, comparaciones EV03/EV04/D1a, unified summary, manifests y runtime authorization record. Solo se excluye `outputs/audits/0b05c_corrective_numerical_runtime_v0.2/exact_hash_ledger_v0.2.json` para evitar circularidad.

El validador distingue roots archivo/directorio, compara el set observado con el allowlist exacto y falla tanto por missing como por unexpected. Cada entrada registra path, SHA-256 y size bytes. Los tests incluyen los tres corpora y demuestran fail-closed al faltar uno o aparecer un extra.

### F. F005 - D1a unified summary

Después de D1a, `_d1a_summary_reference()` exige y valida aggregate comparison, case-level comparison, execution manifest y D1a hash ledger. El aggregate debe contener su tabla `metrics`, el manifest debe estar en `PASS`, y case-level/ledger deben ser no vacíos. Los cuatro quedan referenciados por path, SHA-256 y size bytes.

`build_unified_summary()` exige incorporar la referencia aggregate D1a; falta de aggregate o de cualquier output contractual bloquea el summary.

### G. F006 - tests

La suite v0.2 pasó de 20 a 43 tests. La cobertura nueva incluye: record obligatorio; coherencia gate/specs; frozen model identity; rechazo de forbidden diff; EV03 PASS_EXACT campo por campo; EV04 SHA exactos; commands/roots; file-roots del ledger; missing/extra fail-closed; evidencia aggregate D1a; y persistencia del estado cerrado sin roots reales.

No se afirmó CI. Toda conducta futura se probó con fixtures temporales y mocks; ningún test invocó una ejecución numérica real 0B-05C.

### H. Invariantes científicos

Permanecieron sin cambio: EV03 `DROP_SINGLE_CHARACTER_TOKENS`; `k1=1.5`; `b=0.75`; EVAL N=1,056; depth EV03=100; depth EV04=200; semántica jerárquica/collapse/ties EV04; Decision906 limitada a `87044110` y `87045110`; texto `Inferior a 4,537 t`; pesos/config/scoring/ranking D1a; `FREEZE_ORIGINAL_D1A_WEIGHTS`; `must_not_retrain=true`; `FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD`; orden de 19 pasos; y roots v0.2. Ningún artefacto v0.1 cambió.

### I. Gate state

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

### J. Tests/regresiones

```makefile
tests_v02_expanded = RUN 43 / PASS 43 / FAIL 0 / ERROR 0 / SKIP 0
tests_ev03_recovery_v02 = RUN 16 / PASS 16 / FAIL 0 / ERROR 0 / SKIP 0
tests_v01_gate = RUN 33 / PASS 33 / FAIL 0 / ERROR 0 / SKIP 0
tests_d1a_preexecution = RUN 8 / PASS 8 / FAIL 0 / ERROR 0 / SKIP 0
tests_d1a_runner = RUN 27 / PASS 27 / FAIL 0 / ERROR 0 / SKIP 0
tests_bm25_flat = RUN 13 / PASS 13 / FAIL 0 / ERROR 0 / SKIP 0
tests_bm25_hierarchical = RUN 17 / PASS 17 / FAIL 0 / ERROR 0 / SKIP 0
tests_required_bundle = RUN 157 / PASS 157 / FAIL 0 / ERROR 0 / SKIP 0
tests_total = RUN 536 / PASS 536 / FAIL 0 / ERROR 0 / SKIP 0
postcommit_detached_preflight = PASS / PREEXECUTION_CLOSED_READONLY
postcommit_detached_tests_v02 = RUN 43 / PASS 43 / FAIL 0 / ERROR 0 / SKIP 0
```

Para las regresiones que validan por SHA el modelo local ignorado se usó temporalmente una copia exacta del modelo congelado, sin cargarlo ni ejecutar retrieval; se eliminó al terminar. La suite total terminó `OK`.

### K. Aislamiento

```makefile
main_modified = false
plan_maestro_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false
v01_artifacts_modified = false
future_roots_present = false
authorization_record_created = false
runtime_authorization_record_created = false
numerical_execution_occurred = false
```

Los seis JSON contractuales v0.2 fueron regenerados determinísticamente; cuatro cambiaron en bytes por los nuevos contratos/bindings y dos permanecieron byte-idénticos.

### L. Commit candidato corregido

```makefile
branch = codex/0b05c-corrective-numerical-gate-v02
commit = 59dc445d8128dd71f48d26eac66c9ae8d0c21e38
parent = b0a1e61f70f42aa2048338965cc003e032d3a493
tree = 3243c6bcc5030dd07c86bd593596e420212541cf
commit_message = fix: close 0b05c v0.2 numerical gate audit findings
compare_vs_origin_main = 2 ahead / 0 behind
compare_vs_initial_candidate = 1 ahead / 0 behind
remote_candidate = 59dc445d8128dd71f48d26eac66c9ae8d0c21e38
push = PASS / FAST_FORWARD b0a1e61..59dc445
working_tree_clean = true
```

Changed paths exactos:

1. `docs/0B05C_CORRECTIVE_NUMERICAL_GATE_V02.md`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_execution_gate_v0.2.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_gate_hash_ledger_v0.2.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/0b05c_corrective_numerical_gate_manifest_v0.2.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.2/ev04_numerical_execution_spec_v0.2.json`
6. `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py`
7. `src/experiments/run_0b05c_corrective_numerical_v02.py`
8. `tests/test_0b05c_corrective_numerical_gate_v02.py`

### M. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/10_RESPUESTA_MICROCLOSE_GATE_RUNNER_0B05C_V02_F001_F006.md
admin_commit = SELF / docs: persist prompt 10 gate microclose report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### N. Estado científico

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
