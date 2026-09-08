### A. Estado Git

- rama: `codex/0b05c-ev03-historical-builder-recovery-v02`
- base cientifica inmutable: `06cc75ec173eb6c4b134a45eeb88fe25999f396e`
- HEAD inicial auditado: `cef8d7ad58d877e933f8c86b9f721cb214d9058d`
- HEAD final: `43291c312c2934aae03f3c087dd0a1ae594341b7`
- main: `06cc75ec173eb6c4b134a45eeb88fe25999f396e`
- origin/main: `06cc75ec173eb6c4b134a45eeb88fe25999f396e`
- parent del commit final: `cef8d7ad58d877e933f8c86b9f721cb214d9058d`
- tree del commit final: `9f21cb79c37cbcdf93006503bb4f888f1acfc975`
- tree inicial auditado preservado: `281806931941e526e590f7d48c8aca01adde600e`
- worktree de correccion: `C:/Users/Vladimir/Documents/LLM-RAG NANDINA/ev03-recovery-v02`
- worktree postcommit detached: `C:/Users/Vladimir/Documents/LLM-RAG NANDINA/ev03-recovery-v02-postcommit-clean`
- estado final del worktree de correccion: limpio y sincronizado con origin.
- estado final del checkout postcommit: limpio, detached en `43291c312c2934aae03f3c087dd0a1ae594341b7`.

### B. F001

`F001 = CLOSED / CANDIDATE_READY_FOR_EXTERNAL_AUDIT`.

El verificador ya no exige `HEAD == BASE_COMMIT` ni exige ausencia de `AUDIT_ROOT`. El modo comprometido nuevo es:

`python -B -m src.experiments.verify_ev03_historical_builder_recovery_v02 --verify-committed`

Ese modo demuestra que `06cc75ec...` es ancestro de HEAD, exige un tracked worktree limpio, valida fail-closed los bindings canonicos, lee sin sobrescribir los siete artefactos versionados y construye el indice/control exclusivamente en `tempfile.TemporaryDirectory()` fuera del repositorio. No usa destinos bajo `data/processed/*` ni `outputs/*`.

Resultado postcommit desde checkout limpio:

```ini
status=PASS
mode=COMMITTED_REPLAY_READONLY
base_commit_ancestor=true
tracked_worktree_clean=true
LOGICAL_INDEX_IDENTITY=EXACT
EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT
ranking_bytes_exact=true
case_summary_bytes_exact=true
full_metrics_exact=true
repo_files_created=0
repo_files_modified=0
repo_files_deleted=0
audit_artifacts_modified=false
future_numerical_roots_present=false
```

### C. F002

`F002 = CLOSED / CANDIDATE_READY_FOR_EXTERNAL_AUDIT`.

La suite recovery se amplio de 12 a 16 tests. Los tests nuevos cubren:

- scope `EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY` y `NOT_AUTHORIZATION_READY`;
- completitud y portabilidad de los bindings canonicos;
- mutacion sintetica del SHA-256 canonico del builder, rechazada fail-closed;
- subprocess real de `--verify-committed` desde el checkout postcommit limpio;
- exit code 0 y parse del JSON final;
- identidad logica, ranking, case summary y metricas exactas;
- tracked worktree sin cambios antes/despues;
- hashes de los artifacts comprometidos sin cambios;
- ausencia de los nueve future numerical roots;
- cero archivos creados, modificados o eliminados en el repositorio.

Resultado postcommit: `RUN=16 / PASS=16 / FAIL=0 / ERROR=0 / SKIP=0`.

### D. F003

`F003 = CLOSED / CANDIDATE_READY_FOR_EXTERNAL_AUDIT`.

Se agregaron reglas `text eol=lf` exclusivamente para:

- `src/experiments/build_bm25_ev03_historical_recovered_v02.py`
- `src/experiments/verify_ev03_historical_builder_recovery_v02.py`
- `tests/test_0b05c_ev03_historical_builder_recovery_v02.py`
- `docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/**`

Las identidades autoritativas de texto ahora son `git_blob_sha1` y `canonical_git_blob_sha256`, calculado sobre `git cat-file blob`. Para `src/configs/experiment_config.json`:

```ini
git_blob_sha1=09e715ce30b789805644aa87b16df78e04d0352a
canonical_git_blob_sha256=107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d
```

El valor `ee23e112fb553a355d9787403eb7fa8688295737f76c7acaff052cc9d0ecb2d3` queda preservado unicamente como `WORKTREE_SHA256_DIAGNOSTIC_ONLY_WINDOWS_CRLF`, con `authoritative=false`; no se presenta como identidad congelada.

### E. F004

`F004 = CLOSED_FOR_RECOVERY_PREEXECUTION / NUMERICAL_AUTHORIZATION_REMAINS_BLOCKED`.

Bindings exactos `classification | path | git_blob_sha1 | canonical_git_blob_sha256`:

```text
VERSIONED_GIT_BLOB | src/experiments/build_bm25_ev03_historical_recovered_v02.py | b2ca6d5e4513a4ff36631a71942379f5669100a2 | e841f6ecf2b8a5c2e8bcad6124cf988147b826f61807ed59021802f6e0f97866
VERSIONED_GIT_BLOB | src/experiments/verify_ev03_historical_builder_recovery_v02.py | 243b92f5ee1cf6a6aae7bdc8e51b7c235f52fb0e | 9b56678abb6eb3c9b07b74538412f3a0e1507242129a611f309558d9d6429d2b
VERSIONED_GIT_BLOB | src/bm25_index.py | 718895e0658a55cc1590c84ef807f901b75e7c7f | 1be4319cdc2a5d14fdbf95253902b23f355eccfdb24f421942e1a52514f2e6c2
VERSIONED_GIT_BLOB | src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py | c6f4121fe5f5f50e71e27eb4cf1e28eb8986d062 | 7e34b5f8fabb901aeded1fcb76c8a48d2963a80d4d2fdceb767a8084b1bc1b16
VERSIONED_GIT_BLOB | src/retrieval/bm25.py | b089b02968a5146377fb26718cfaaa48f3ae4897 | 1d19b2ace176ba45dc48e0143386e69a9529e0aea6c5ad537fe5d5f97cea8748
VERSIONED_GIT_BLOB | src/configs/experiment_config.json | 09e715ce30b789805644aa87b16df78e04d0352a | 107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d
VERSIONED_GIT_BLOB | data/processed/corpus_rag_v1_index.jsonl | a74d44f27e77d5c652c497a4f20fc786855daf8a | 83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0
VERSIONED_GIT_BLOB | data/processed/data_aduanas_evalset_clase87_v0.2.csv | 83d069fd7c0a5f42099e6d3347bd36e4e8158371 | 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
FROZEN_BINARY_GIT_BLOB | data/processed/indexes/bm25_nandina8.pkl | 5bf6be9c0a5622bb53b8c2d64fb714ccf0020807 | fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b
VERSIONED_GIT_BLOB | data/processed/indexes/bm25_nandina8_run_metadata.json | f456e9f85df0f9a2aa58882bed27211aa1d11a30 | 89d9e87e8c099ecf1ab7a4bca898ed5cdceef1bead21563527756dfe01a3dce0
VERSIONED_GIT_BLOB | outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv | fe830e00bfa4803e85bb27b676d95c59c7b73b3a | d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
VERSIONED_GIT_BLOB | outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_case_summary.csv | 54846f72884f0363f5054d1953b23955029c5636 | f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0
VERSIONED_GIT_BLOB | outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/run_metadata.json | 1e23a522b406245274b33318ba2983d68e5f0c27 | e57d1ebd360790c64b485f5fb4d7aa34be500e48f4ebf48ab7c0437874caba44
```

El verificador comprometido comprobo los 13 bindings con `mismatch_count=0`. No se introdujo autorreferencia por commit: el contrato usa identidades de blobs individuales.

### F. Reproduccion EV03

```ini
LOGICAL_INDEX_IDENTITY=EXACT
EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT
ranking_rows=50327
ranking_sha256=d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
ranking_bytes_exact=true
case_summary_rows=1056
case_summary_sha256=f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0
case_summary_bytes_exact=true
metric_table_exact=true
full_metrics_exact=true
witness_case_id=DA-EVAL-V02-00001
witness_top1_code=39173210
witness_top1_score=21.311974833146948
witness_retrieved_count=38
```

Se preserva `EV03_REPRODUCTION_ROOT_CAUSE=CURRENT_BUILDER_SEMANTICS_MISMATCH`, `EV03_RECOVERED_HISTORICAL_TOKEN_POLICY=DROP_SINGLE_CHARACTER_TOKENS` y `AUTHENTIC_HISTORICAL_SOURCE_PY=NOT_VERSIONED_AT_INDEX_CREATION`.

### G. Scope/gate

```ini
gate_status=CANDIDATE_PENDING_EXTERNAL_AUDIT
gate_scope=EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY
authorization_readiness=NOT_AUTHORIZATION_READY
EV03_NUMERICAL_EXECUTION=NOT_AUTHORIZED
EV04_NUMERICAL_EXECUTION=NOT_AUTHORIZED
D1A_NUMERICAL_EXECUTION=NOT_AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION=NOT_AUTHORIZED
corrective_retrieval_executed=false
corrective_metrics_computed=false
runtime_authorization_record_present=false
```

No se creo `run_0b05c_corrective_numerical_v02.py` ni authorization record.

### H. Aislamiento

- `main` y `origin/main` permanecen en `06cc75ec173eb6c4b134a45eeb88fe25999f396e`.
- Plan Maestro: sin cambios.
- `article/` y `main-manuscript`: sin cambios.
- EXP11B: sin cambios y sin ejecucion H150/H200.
- EXP12: no abierto y sin cambios.
- contratos, roots y evidencia v0.1: sin cambios.
- los seis outputs ignorados del Intento 02 siguen presentes en el checkout original; el trabajo se realizo en un worktree separado y no se escribio ni borro ninguno.
- EV03 corrected, EV04 corrected, D1a numerical y runner unificado: no ejecutados.

### I. Ledger/manifest

Artifacts versionados del bundle:

```text
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_historical_builder_provenance_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_logical_index_identity_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_decision885_control_reproduction_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_corrective_execution_spec_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_corrective_numerical_gate_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_manifest_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json
```

El ledger distingue `VERSIONED_GIT_BLOB`, `FROZEN_BINARY_GIT_BLOB` y `GENERATED_LOCAL_OUTPUT`. Los outputs del replay se identifican como temporales; ranking/case summary usan SHA-256 de sus bytes generados y las metricas usan SHA-256 del objeto canonico de metricas, sin convertir hashes dependientes del checkout en identidades Git.

```ini
canonical_dependency_binding_count=13
ledger_mismatch_count=0
repository_generated_paths=[]
audit_artifacts_modified_by_committed_replay=false
```

### J. Tests

```text
EV03 recovery precommit: RUN=16 PASS=15 FAIL=0 ERROR=0 SKIP=1
  SKIP esperado: el subprocess committed replay exige checkout tracked limpio.
Committed replay postcommit limpio: RUN=1 PASS=1 FAIL=0 ERROR=0 SKIP=0
EV03 recovery postcommit limpio: RUN=16 PASS=16 FAIL=0 ERROR=0 SKIP=0
Historical BM25 v0.2: RUN=10 PASS=10 FAIL=0 ERROR=0 SKIP=0
Normative BM25 flat v0.2: RUN=13 PASS=13 FAIL=0 ERROR=0 SKIP=0
F003 microclose + residual v0.1: RUN=17 PASS=17 FAIL=0 ERROR=0 SKIP=0
D1a preexecution + corrective runner: RUN=35 PASS=35 FAIL=0 ERROR=0 SKIP=0
```

`POSTCOMMIT_CLEAN_REPLAY=PASS`.

No se ejecuto ningun runner numerico. No se observaron fallos ni errores en la validacion final requerida.

### K. Commit candidato corregido

```ini
commit=43291c312c2934aae03f3c087dd0a1ae594341b7
parent=cef8d7ad58d877e933f8c86b9f721cb214d9058d
tree=9f21cb79c37cbcdf93006503bb4f888f1acfc975
message=fix: make EV03 recovery v0.2 self-verifiable and portable
push=PASS
remote_head=43291c312c2934aae03f3c087dd0a1ae594341b7
ahead=0
behind=0
```

Changed files del microclose contra `cef8d7ad...` (10):

```text
.gitattributes
docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_corrective_numerical_gate_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_manifest_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_corrective_execution_spec_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_decision885_control_reproduction_v0.2.json
outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_historical_builder_provenance_v0.2.json
src/experiments/verify_ev03_historical_builder_recovery_v02.py
tests/test_0b05c_ev03_historical_builder_recovery_v02.py
```

Contra la base `06cc75ec...`, la candidatura final mantiene exactamente los 12 paths del recovery: el builder y los siete artifacts originales, mas documentacion, tests, verificador y las reglas LF de `.gitattributes`. No hay paths de Plan Maestro, article, EXP11B, EXP12 ni outputs numericos futuros.

### L. Limitaciones

- No existe evidencia de CI independiente en esta operacion; las validaciones se ejecutaron localmente en el runtime Python disponible y en un segundo checkout limpio detached.
- `AUTHENTIC_HISTORICAL_SOURCE_PY=NOT_VERSIONED_AT_INDEX_CREATION`; el `.pyc` preservado sigue clasificado como evidencia derivada y no como fuente autentica.
- No existe todavia un runner numerico v0.2 ni runtime authorization record.
- La candidatura no esta aprobada para integracion ni autorizacion por este reporte; queda pendiente de auditoria externa.

### M. Estado cientifico

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`
