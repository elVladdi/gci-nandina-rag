# RESPUESTA PROMPT 55 - VALIDAR, CONGELAR E INGESTAR EXTENSION NUEVA_02 PARA EXP12

```text
PROMPT55 = COMPLETED

main_initial = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
main_final = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
plan_initial = 00adb8f6fc668609500be913203be50a5d402554
plan_final = 00adb8f6fc668609500be913203be50a5d402554
article_initial = 254b1e6df736fa9938ac86a515d65b36f4d361c5
article_final = 254b1e6df736fa9938ac86a515d65b36f4d361c5

EXP12_SOURCE_SCOPE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
H100_ROLE_IN_EXP12 = REFERENCE_LABEL_SET_AND_DISTRIBUTION_ONLY
H100_ROWS_ALLOWED_AS_EXP12_CANDIDATE_SAMPLING_ROWS = false

CURRENT_WORKBOOK_PATH = C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA\data\Series - Descripciones.xlsx
CURRENT_WORKBOOK_SHA256 = 1d62b74d5931275cf4740e90292805cfc8c63823817371e0c5ca358323bee64d
CURRENT_WORKBOOK_SIZE_BYTES = 18069347
CURRENT_WORKBOOK_SHEET_ORDER = [Hoja2, Hoja1, NUEVA_01, NUEVA_02]

BASELINE_NUEVA01_WORKBOOK_PATH = C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA_source_archive\Series - Descripciones_EXPANDED_NUEVA_01_SOURCE_087efd97.xlsx
BASELINE_NUEVA01_WORKBOOK_SHA256 = 087efd97cb17fd166c2e7eb5089690577491e99ab5d415f9e3a8614923ee4ba3
FINGERPRINT_CONTRACT = sha256(canonical JSONL header plus nonempty cells in row-column order; data_only=false)

Hoja2_baseline_content_fingerprint = 09d1fb1f238c3dab9d15278773bfdaea8601ec6fd07dd08f4ee048ce9ea09346
Hoja2_current_content_fingerprint = 09d1fb1f238c3dab9d15278773bfdaea8601ec6fd07dd08f4ee048ce9ea09346
Hoja2_max_row = 126524
Hoja2_max_column = 9
Hoja2_nonempty_cell_count = 387742
Hoja2_content_fingerprint_match = true

Hoja1_baseline_content_fingerprint = 7317c42350b49b0b80c54de66becfc8f14a0a7b518bcada33bc628966d12e862
Hoja1_current_content_fingerprint = 7317c42350b49b0b80c54de66becfc8f14a0a7b518bcada33bc628966d12e862
Hoja1_max_row = 41578
Hoja1_max_column = 10
Hoja1_nonempty_cell_count = 133038
Hoja1_content_fingerprint_match = true

NUEVA_01_baseline_content_fingerprint = c14e337179e97d7fa8236c690557a4580d00c165e3e3b4b357f29c9d92cb06cd
NUEVA_01_current_content_fingerprint = c14e337179e97d7fa8236c690557a4580d00c165e3e3b4b357f29c9d92cb06cd
NUEVA_01_max_row = 169130
NUEVA_01_max_column = 9
NUEVA_01_nonempty_cell_count = 517142
NUEVA_01_content_fingerprint_match = true

NUEVA_02_PARSED_ROWS = 3250
NUEVA_02_PARSED_COLUMNS = 112

VALIDATE_NEW_SHEETS_INVOCATION_COUNT = 1
VALIDATE_NEW_SHEETS_RETURN_CODE = 0
VALIDATE_NEW_SHEETS_RESULT = RESULT: PASS

ARCHIVE_PATH = C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA_source_archive\Series - Descripciones_EXPANDED_NUEVA_01_NUEVA_02_SOURCE_1d62b74d.xlsx
ARCHIVE_SHA256 = 1d62b74d5931275cf4740e90292805cfc8c63823817371e0c5ca358323bee64d
ARCHIVE_SIZE_BYTES = 18069347
ARCHIVE_COPY_METHOD = Python shutil.copy2 binary copy
SOURCE_SHA_BEFORE = 1d62b74d5931275cf4740e90292805cfc8c63823817371e0c5ca358323bee64d
SOURCE_SHA_AFTER = 1d62b74d5931275cf4740e90292805cfc8c63823817371e0c5ca358323bee64d
SOURCE_MUTATED = false

INGESTION_COMMAND = C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA\.venv\Scripts\python.exe src/ingestion/prepare_new_historical_multisheet_v0.1.py --ingest-new-data --future-workbook "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA_source_archive\Series - Descripciones_EXPANDED_NUEVA_01_NUEVA_02_SOURCE_1d62b74d.xlsx" --new-sheet NUEVA_01 --new-sheet NUEVA_02 --future-output-dir data/interim/new_historical_gate_v0.2 --future-audit-dir outputs/audits/new_historical_gate_v0.2
INGESTION_INVOCATION_COUNT = 1
INGESTION_STARTED_AT_UTC = 2026-09-13T18:06:47.4948553+00:00
INGESTION_ENDED_AT_UTC = 2026-09-13T18:07:30.0228112+00:00
INGESTION_RETURN_CODE = 0
INGESTION_RESULT = RESULT: PASS / NEW_DATA_INGESTION_EXECUTED=true / NEW_ELIGIBLE_HISTORICAL_ROWS=7190
INGESTION_STDOUT_SHA256_UTF8 = 4503a3ed3485d5cce724d512586f16460783c44f9b7897c07a5c28083573822b
INGESTION_STDERR_SHA256_UTF8 = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
INGESTION_PYTHON_VERSION = 3.10.11
INGESTION_PYTHON_IMPLEMENTATION = CPython

V02_POOL_PATH = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
V02_POOL_SHA256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
V02_ROWS = 7190
V02_UNIQUE_DAM = 101
V02_UNIQUE_NANDINA_TOTAL = 84
H100_REFERENCE_CODES_PRESENT = 66
H100_REFERENCE_CODE_COUNT = 66
H100_REFERENCE_CODES_MISSING = 0
H100_REFERENCE_COVERAGE_FRACTION = 1.0
MISSING_H100_REFERENCE_CODES = []
ROWS_EXCLUDED_FIXED_DEV_EVAL_DAM = 0
ROWS_WITH_FROZEN_ID_OVERLAP = 0
EXP12_EXTENSION_COVERAGE_STATUS = PASS_66_OF_66_CANDIDATE

CANDIDATE_BRANCH = codex/exp12-new-historical-gate-extension-v02
CANDIDATE_COMMIT = 55847ed375202533f20fd09d72af41ced153a818
CANDIDATE_PARENT = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
CANDIDATE_TREE = 4fc757c88a05576722605b214fa5fb1ee8572226
CANDIDATE_COMMITS_AHEAD = 1
CANDIDATE_COMMITS_BEHIND = 0
CANDIDATE_CHANGED_PATH_COUNT = 10
CANDIDATE_PUBLISHED = true
CANDIDATE_REMOTE_COMMIT = 55847ed375202533f20fd09d72af41ced153a818
LOCAL_ONLY_LARGE_ARTIFACT_COUNT = 0
MAX_SINGLE_GIT_ARTIFACT_BYTES = 90000000
ALL_VERSIONED_ARTIFACTS_BELOW_GIT_BLOB_LIMIT_GUARD = true
INDEX_BYTES_IDENTICAL_TO_PRODUCED_ARTIFACT_BYTES = true

CANDIDATE_CHANGED_PATHS =
data/interim/new_historical_gate_v0.2/new_historical_curated.csv
data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
data/interim/new_historical_gate_v0.2/new_historical_normalized_all.csv
outputs/audits/new_historical_gate_v0.2/exp12_source_coverage_audit_v0.2.json
outputs/audits/new_historical_gate_v0.2/new_historical_artifact_hashes.csv
outputs/audits/new_historical_gate_v0.2/new_historical_duplicate_nearduplicate_audit.csv
outputs/audits/new_historical_gate_v0.2/new_historical_exclusions.csv
outputs/audits/new_historical_gate_v0.2/new_historical_frozen_overlap_audit.csv
outputs/audits/new_historical_gate_v0.2/new_historical_ingestion_manifest.json
outputs/audits/new_historical_gate_v0.2/source_extension_freeze_v0.2.json

VERSIONED_ARTIFACTS_SIZE_SHA256 =
data/interim/new_historical_gate_v0.2/new_historical_curated.csv | 9204410 | f9d5908b4764fadc24ec842fd55fb967cbcd10fd570eec698679e7f22cbfcba2
data/interim/new_historical_gate_v0.2/new_historical_eligible.csv | 9333907 | f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
data/interim/new_historical_gate_v0.2/new_historical_normalized_all.csv | 23870935 | be8cba34904568c1e6606276d12f477baf924302bdcf571b608c36728ce4303d
outputs/audits/new_historical_gate_v0.2/exp12_source_coverage_audit_v0.2.json | 1342 | 147c6a881ed6bfbbc824164fefb9b9c1c498cab5db11cb9b4eea7b5299974d40
outputs/audits/new_historical_gate_v0.2/new_historical_artifact_hashes.csv | 1641 | 658aecaa191096b6bddc5a8577e91daf5d5ee3073f8eaddc0488ce90a88c78c1
outputs/audits/new_historical_gate_v0.2/new_historical_duplicate_nearduplicate_audit.csv | 4865079 | 6cd2327a4559f2ccbb1a0afaa218c737002a55d4f8a0d4bbeba9e6626b345920
outputs/audits/new_historical_gate_v0.2/new_historical_exclusions.csv | 19 | a3ab12880ce02422f61fe98d1ec7256a19719c7f5751159d5020b58e8c5b0d96
outputs/audits/new_historical_gate_v0.2/new_historical_frozen_overlap_audit.csv | 9333907 | f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
outputs/audits/new_historical_gate_v0.2/new_historical_ingestion_manifest.json | 4210 | cbd3cf30b077363538a169edd469d6b3ee7c1dea06376005048455fe11c60774
outputs/audits/new_historical_gate_v0.2/source_extension_freeze_v0.2.json | 4263 | f1071908ff21e7c07262b65bd72bd445d2980f026465ea92728fa958a4fc3703

NEW_HISTORICAL_INGESTION_EXECUTED = true
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_BM25_EXECUTED = false
EXP12_TOP_K_COMPUTED = false
EXP12_MRR_COMPUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false

PLAN_MODIFIED = false
ARTICLE_MODIFIED = false
MAIN_MODIFIED = false
XLSX_VERSIONED = false
TRACKED_WORKING_TREE_CLEAN = true
UNTRACKED_PRESERVED = Referencias/Antecedentes/; Referencias/Glosario/; data/Series - Descripciones.xlsx
```

```text
PROMPT55 = COMPLETED
NEW_HISTORICAL_GATE_EXTENSION_V02 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP12_EXTENSION_COVERAGE_STATUS = PASS_66_OF_66_CANDIDATE
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
