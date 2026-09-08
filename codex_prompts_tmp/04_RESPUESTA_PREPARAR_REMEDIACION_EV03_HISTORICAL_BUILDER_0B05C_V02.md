## A. Git/base

```makefile
repo = elVladdi/gci-nandina-rag
repo_local = C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
branch = codex/0b05c-ev03-historical-builder-recovery-v02
initial_HEAD = 06cc75ec173eb6c4b134a45eeb88fe25999f396e
initial_tree = c84da63249619e94ae69fb2a6f080dd3f84cbcf4
main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e
origin/main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e
tracked_working_tree_initially_clean = true
candidate_worktree = C:\Users\Vladimir\Documents\LLM-RAG NANDINA\ev03-recovery-v02
clean_validation_worktree = C:\Users\Vladimir\Documents\LLM-RAG NANDINA\ev03-recovery-v02-clean
attempt_02_worktree_modified = false
attempt_02_evidence_preserved = true
```

La rama candidata no existía local ni remotamente antes de su creación. Se creó desde el commit base exacto. No se ejecutó merge, rebase, cherry-pick, cleanup ni modificación de `main`.

Los seis artefactos del Intento 02 conservan sus identidades:

```text
data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.1/index.pkl
  SHA-256 0db8772a513765aa2d4f214548c1d279a99789ac6fbacc6d72dc99937b43cf6c
data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.1/index_metadata.json
  SHA-256 6b19a88b27af460ff2d83bf0adcb224617f4e5d1848eb1cb83fc81800ea6874f
outputs/evaluation/0b05c_corrective_numerical_v0.1/runtime_authorization_record.json
  SHA-256 2c1c435f0fec9ef32003e13129dd70bf747d4fa2f9086c7d16a582c7512c0f0c
outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1/normative_flat_case_summary.csv
  SHA-256 bcf60ce0a9e62c95a39140139c911148d1a8f5d8a40f261daca57daf8e704527
outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1/normative_flat_metrics.json
  SHA-256 c2cb91059d2e860e4660bb779647a239a01871db2d39feb8d0928c8d766c2181
outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.1/normative_flat_results.csv
  SHA-256 181deea25633244b85898443deba54babc352c46dd3e23c16a478eb57bf35c29
```

## B. Procedencia histórica

```text
689f7436a8e2011b3399140c90c7eb6e777b2026  primera aparición del bytecode Python 3.11
975bc9879ec89cc945d5432ef0bac3b37598f72c  primera aparición del índice y metadata
d73ff147b02d69c65218de4b4bd08d501ff9f5d7  primera aparición del fuente y notebook
df60c77287c8fd5f128b136625dc149bc5aaaeb2  ejecución histórica EV03 v0.2
```

En el commit `975bc987...`:

```makefile
src/__pycache__/bm25_index.cpython-311.pyc = PRESENT
data/processed/indexes/bm25_nandina8.pkl = PRESENT
data/processed/indexes/bm25_nandina8_run_metadata.json = PRESENT
src/bm25_index.py = ABSENT
notebooks/04_BM25_Indexacion_NANDINA.ipynb = ABSENT
```

Identidades principales:

```text
Bytecode versionado
  Git blob SHA-1: f4d270b38c596abfeb1ee9c312a51d633556bd1a
  SHA-256:        2c2082f44891dc5a16fd9b8aae7c6e69fd10faf86f6f1a798d31d916e7532c0a
  Clasificación:  DERIVED_BYTECODE_EVIDENCE_NOT_AUTHENTIC_SOURCE_PY

Índice histórico
  Git blob SHA-1: 5bf6be9c0a5622bb53b8c2d64fb714ccf0020807
  SHA-256:        fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b

Metadata histórica
  Git blob SHA-1: f456e9f85df0f9a2aa58882bed27211aa1d11a30
  SHA-256:        89d9e87e8c099ecf1ab7a4bca898ed5cdceef1bead21563527756dfe01a3dce0

Fuente actual divergente
  Git blob SHA-1: 718895e0658a55cc1590c84ef807f901b75e7c7f
```

Metadata histórica verificada:

```makefile
python = 3.11.7
docs_before_filter = 7748
docs_indexed = 7644
avg_doc_len_tokens = 5.793302059173584
vocabulary_size = 5646
stopwords_active = true
stopwords_count = 51
corpus_sha256 = 83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0
AUTHENTIC_HISTORICAL_SOURCE_PY = NOT_VERSIONED_AT_INDEX_CREATION
```

Identidades congeladas adicionales:

```text
Corpus SHA-256: 83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0
EVAL SHA-256:   3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
Config Git blob SHA-1: 09e715ce30b789805644aa87b16df78e04d0352a
Config canonical Git-blob SHA-256: 107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d
Config working-tree CRLF SHA-256 observado: ee23e112fb553a355d9787403eb7fa8688295737f76c7acaff052cc9d0ecb2d3
```

La diferencia de representación del config se registró separando identidad canónica Git de bytes CRLF del checkout; no implica cambio semántico.

## C. Causa reproducida

```makefile
EV03_REPRODUCTION_ROOT_CAUSE = CURRENT_BUILDER_SEMANTICS_MISMATCH
current_global_policy = KEEP_SINGLE_CHARACTER_TOKENS
recovered_EV03_policy = DROP_SINGLE_CHARACTER_TOKENS
```

El builder actual produjo 5,674 términos y `avgdl=6.037153244018555`. La semántica recuperada produjo 5,646 términos y `avgdl=5.793302059173584`, iguales al índice histórico.

La prueba controlada confirmó:

```text
Entrada:  "A x 1 22 motor"
Salida recuperada: ["22", "motor"]
```

Los tokens de longitud igual o superior a dos, lowercase, normalización NFKD y stopwords conservan la semántica existente. El filtro recuperado se aplica exclusivamente al builder EV03 v0.2.

## D. Implementación v0.2

Paths creados:

```text
src/experiments/build_bm25_ev03_historical_recovered_v02.py
  Builder EV03 dedicado; elimina tokens len=1 y congela k1/b, stopwords, campos y orden.

src/experiments/verify_ev03_historical_builder_recovery_v02.py
  Runner build-only del control Decision885; no contiene modo corrected ni autorización numérica.

tests/test_0b05c_ev03_historical_builder_recovery_v02.py
  Doce pruebas contractuales, incluida reproducción full en memoria apta para checkout limpio.

docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md
  Alcance, procedencia, límite epistemológico y política recuperada.

outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/
  ev03_historical_builder_provenance_v0.2.json
  ev03_logical_index_identity_v0.2.json
  ev03_decision885_control_reproduction_v0.2.json
  ev03_corrective_execution_spec_v0.2.json
  0b05c_corrective_numerical_gate_v0.2.json
  0b05c_ev03_historical_builder_recovery_manifest_v0.2.json
  0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json
```

No se modificó ningún archivo preexistente.

## E. Aislamiento

```makefile
src/bm25_index.py_modified = false
src/bm25_index.py_HEAD_blob = 718895e0658a55cc1590c84ef807f901b75e7c7f
EV04_modified = false
EV04_uses_DROP_SINGLE_CHARACTER_TOKENS = false
EXP11B_modified = false
EXP12_modified = false
main_modified = false
Plan_Maestro_modified = false
article_modified = false
outputs_v0.1_modified = false
attempt_02_artifacts_reused_as_v02_outputs = false
```

Los roots v0.1 fueron declarados explícitamente como evidencia excluida del universo de outputs v0.2.

## F. Logical index identity

Método canónico: JSON UTF-8 ordenado; floats IDF mediante `float.hex()`; `doc_lens` mediante `dtype|shape|contiguous_bytes`.

```text
Campo                         Histórico / Recuperado
k1                            1.5 / 1.5
b                             0.75 / 0.75
doc_ids_count                 7644 / 7644
doc_ids SHA-256               2cfff892b1c6f8d5193a0542a1ded4b551f9a2fdf8e68f2b6858030a3da2f4f1
doc_texts_count               7644 / 7644
doc_texts SHA-256             43a0ecb872c3cca2834141643bf9e9db2a89ac85ea4ffc2341986f14edf938b1
doc_lens min/max/mean         2 / 24 / 5.793302059173584
doc_lens SHA-256              b25e18913d58145cb248c0a465bfe68afb0bc6e7d2f9286c03d1df52c7069ecd
vocabulary_size               5646 / 5646
IDF SHA-256                   3625597ae8bad7133da7a3428e9fc48f2724c92222925f1973d34e7061910a8f
postings_count                21541 / 21541
inverted-index SHA-256        10f8870d6326634a5bd8a73c473ee441986fb5698b88ea69195abd58ed511ee9
```

```makefile
k1_exact = true
b_exact = true
doc_ids_and_order_exact = true
doc_texts_and_order_exact = true
doc_lens_exact = true
avgdl_exact = true
idf_mapping_exact = true
inverted_index_exact = true
LOGICAL_INDEX_IDENTITY = EXACT
PICKLE_BYTE_IDENTITY = NOT_REQUIRED
```

El pickle reconstruido tiene SHA-256 `b1421f526994b7df001b3d55e4990f92bc4a4c8b8d367a6c37e444b025461557`, distinto del pickle histórico, pero su estructura lógica es exacta.

## G. EV03 Decision885 full control reproduction

Comando build-only ejecutado:

```powershell
python -B -m src.experiments.verify_ev03_historical_builder_recovery_v02 --verify-control
```

```makefile
exit_code = 0
EV03_DECISION885_CONTROL_REPRODUCTION = PASS_EXACT
ranking_rows = 50327
ranking_sha256 = d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
ranking_frozen_sha256 = d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
ranking_schema_exact = true
ranking_rows_exact = true
ranking_bytes_exact = true
case_rows = 1056
case_summary_sha256 = f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0
case_summary_frozen_sha256 = f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0
case_summary_schema_exact = true
case_summary_rows_exact = true
case_summary_bytes_exact = true
metric_table_exact = true
full_metrics_exact = true
```

Caso testigo:

```makefile
case_id = DA-EVAL-V02-00001
top1_code = 39173210
top1_score = 21.311974833146948
retrieved_count = 38
```

No se ejecutó el corpus Decision906 ni se calcularon métricas correctivas.

## H. Gate v0.2

```makefile
gate_path = outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_corrective_numerical_gate_v0.2.json
ev03_spec_path = outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_corrective_execution_spec_v0.2.json
manifest_path = outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_manifest_v0.2.json
ledger_path = outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json
gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
EV03_NUMERICAL_EXECUTION = NOT_AUTHORIZED
EV04_NUMERICAL_EXECUTION = NOT_AUTHORIZED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION = NOT_AUTHORIZED
corrective_retrieval_executed = false
corrective_metrics_computed = false
runtime_authorization_record_present = false
future_numerical_roots_present = false
```

Roots de preexecution verification utilizados, distintos de v0.1 y de ejecución futura:

```text
data/processed/indexes/bm25_nandina8_ev03_decision885_preexecution_v0.2/
outputs/evaluation/0b05c_ev03_decision885_preexecution_v0.2/
```

## I. Tests

```text
python -B -m unittest tests.test_0b05c_ev03_historical_builder_recovery_v02 -v
  RUN=12 PASS=12 FAIL=0 ERROR=0 SKIP=0

Misma suite en checkout limpio detached:
  RUN=12 PASS=12 FAIL=0 ERROR=0 SKIP=0

python -B -m unittest tests.test_historical_bm25_v02 tests.test_normative_bm25_flat_v02 tests.test_0b05c_ev03_historical_builder_recovery_v02 -v
  RUN=35 PASS=35 FAIL=0 ERROR=0 SKIP=0

python -B -m unittest tests.test_0b05c_f003_microclose_v01 tests.test_0b05c_f003_residual_v01 -v
  RUN=17 PASS=17 FAIL=0 ERROR=0 SKIP=0

tests/test_d1a_preexecution_0b05c_v01.py + tests/test_d1a_corrective_0b05c_runner_v01.py
  RUN=34 PASS=34 FAIL=0 ERROR=0 SKIP=0

tests/test_0b05c_corrective_numerical_gate_v01.py
  RUN=0; setUpClass ERROR=1
  Causa: el worktree limpio no contiene el modelo D1a local ignorado; Frozen D1a model SHA changed.
  Clasificación: dependencia local preexistente del gate v0.1, no introducida por la candidatura v0.2.

suite_global = NOT_RUN
new_candidate_test_failures = 0
```

Ningún test invocó EV03 corrected, EV04 corrected, D1a numerical ni `--execute-authorized`.

## J. Provenance/ledger

Artefactos versionados. Se distingue SHA-256 del contenido canónico del Git blob SHA-1:

```text
docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md
  2019 bytes | SHA-256 02b218317297e7201f6e6b0457a80e3fed1f66118b3fe43d3d76c380093c0cc2 | Git blob c7f92dc71a43a74e76a9ac92b977f76e59401349
src/experiments/build_bm25_ev03_historical_recovered_v02.py
  6777 bytes | SHA-256 e841f6ecf2b8a5c2e8bcad6124cf988147b826f61807ed59021802f6e0f97866 | Git blob b2ca6d5e4513a4ff36631a71942379f5669100a2
src/experiments/verify_ev03_historical_builder_recovery_v02.py
  18641 bytes | SHA-256 4a9e91f564ec86a0820f18c26061cb297e95a456fc035162c67bfeec81c2bd33 | Git blob 790c943aff026193093ceb4cf6cc04ea258a5e1d
tests/test_0b05c_ev03_historical_builder_recovery_v02.py
  7018 bytes | SHA-256 40d959ecd9a9999350f3b4ac064c0f02634d25d4412d0f73b4fc3cbbd568cfd5 | Git blob e397991ba275567aa679a76faf1ae0280d39ed08
0b05c_corrective_numerical_gate_v0.2.json
  1625 bytes | SHA-256 013a7958d5d8ec182c22d957dd3408ad7d818b4a590bef1946a9fbbcce0266d3 | Git blob 0ff26a269a2ff7c4a163daaea90a94432fea2809
0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json
  4588 bytes | SHA-256 f36a2bb9bb4e2f0fb7018916897126cef20f907ab396972d9fc6c85962f2dcdb | Git blob 0335f06f6a85a56800796ae6b71b53da773e531f
0b05c_ev03_historical_builder_recovery_manifest_v0.2.json
  2431 bytes | SHA-256 d9092bef2bf91506a10700b069dbd75387c4a55d36eb37a60ca1913cee2bcd72 | Git blob 71d93c8f76aae3de6442b485c830c110e7860b6c
ev03_corrective_execution_spec_v0.2.json
  2221 bytes | SHA-256 b7a6a3c364697d6fd961e968fa816fabbdace1c07d44ad615fc956b3f0300b55 | Git blob 149aa3d7ae66cea3fce8fa003fd7e510352eb045
ev03_decision885_control_reproduction_v0.2.json
  1614 bytes | SHA-256 7144245db296a3fc84fc918a903486563de36b753505b64af4641c8fbd39e47e | Git blob 59313ef329f1cde2c83e4dd9836e4f98dc791a9a
ev03_historical_builder_provenance_v0.2.json
  2160 bytes | SHA-256 5a1857c5f4b408679c12c40e85438e0abc9a59c57d22c8b7d84f71023109f72c | Git blob cab94551638b4b726e599fb94023c090051df5e3
ev03_logical_index_identity_v0.2.json
  2043 bytes | SHA-256 b89ff4ac200a7be68856898b4f167e95a549df6f310fc74c8227a975385b47e5 | Git blob a8bffebe59c09ebd0275211f669389a7b836370a
```

Artefactos deliberadamente no versionados y registrados en el ledger:

```text
data/processed/indexes/bm25_nandina8_ev03_decision885_preexecution_v0.2/index.pkl
  918504 bytes | SHA-256 b1421f526994b7df001b3d55e4990f92bc4a4c8b8d367a6c37e444b025461557
  Razón: pickle binario regenerable; identidad lógica completa versionada.

data/processed/indexes/bm25_nandina8_ev03_decision885_preexecution_v0.2/index_metadata.json
  1154 bytes | SHA-256 201187eff7e4b827931e5ebc726005715c9287618113ee400dce5fa5a84a32f0
  Razón: metadata de output build-only regenerable y registrada en ledger/manifest.

outputs/evaluation/0b05c_ev03_decision885_preexecution_v0.2/normative_flat_results.csv
  13145709 bytes | SHA-256 d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
  Razón: duplicado byte-exacto del ranking congelado ya versionado.

outputs/evaluation/0b05c_ev03_decision885_preexecution_v0.2/normative_flat_case_summary.csv
  497448 bytes | SHA-256 f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0
  Razón: duplicado byte-exacto del case summary congelado ya versionado.

outputs/evaluation/0b05c_ev03_decision885_preexecution_v0.2/normative_flat_metrics.json
  5263 bytes | SHA-256 7ebba51b3d692a420294a7be7878a83d66df830b4215ab26148b5d1128ec2239
  Razón: wrapper regenerable; metric table y full metrics exactos versionados en evidencia.
```

```makefile
ledger_entries = 20
ledger_hash_mismatches = 0
HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED = true
```

## K. Candidate commit

```makefile
branch = codex/0b05c-ev03-historical-builder-recovery-v02
candidate_commit = cef8d7ad58d877e933f8c86b9f721cb214d9058d
parent = 06cc75ec173eb6c4b134a45eeb88fe25999f396e
tree = 281806931941e526e590f7d48c8aca01adde600e
message = feat: recover historical EV03 builder semantics v0.2
files_changed = 11
commits_ahead_origin_main = 1
commits_behind_origin_main = 0
remote_candidate = cef8d7ad58d877e933f8c86b9f721cb214d9058d
push_status = PASS
main_pushed = false
working_tree_tracked_clean = true
```

## L. Estado científico

```makefile
corrected_EV03_executed = false
corrected_EV04_executed = false
D1a_numerical_executed = false
authorization_record_v02_created = false
runtime_authorization_record_v02_created = false
scientific_metrics_corrective_computed = false
```

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`
