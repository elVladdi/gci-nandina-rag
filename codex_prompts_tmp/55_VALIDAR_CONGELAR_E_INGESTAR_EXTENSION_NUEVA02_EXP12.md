# PROMPT 55 — VALIDAR, CONGELAR E INGESTAR EXTENSIÓN `NUEVA_02` PARA EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

El usuario informa que el workbook local:

```text
data/Series - Descripciones.xlsx
```

ya contiene una pestaña `NUEVA_02`.

Este bloque realiza exclusivamente, en este orden:

1. verificar el estado canónico y la identidad del workbook local ampliado;
2. comprobar que las hojas preexistentes `Hoja2`, `Hoja1` y `NUEVA_01` no sufrieron deriva de contenido respecto del workbook congelado de `NUEVA_01`;
3. validar de forma no ingerente el conjunto exacto `[NUEVA_01, NUEVA_02]`;
4. congelar por copia binaria el workbook ampliado en el directorio externo de archivo ya gobernado;
5. ejecutar una sola ingesta controlada de las hojas nuevas `NUEVA_01` + `NUEVA_02` hacia **directorios nuevos v0.2**, sin sobrescribir la evidencia v0.1;
6. calcular únicamente la factibilidad estructural de cobertura de códigos H100 para EXP12;
7. versionar los artefactos nuevos en un candidato separado para auditoría externa.

Este bloque **NO ejecuta EXP12**, NO genera los 10,000 candidatos por seed, NO ejecuta retrieval/BM25/Top-k/MRR, NO modifica H100/DEV/EVAL, NO modifica el Plan ni Article y NO abre Grupo 2B ni Grupo 3.

---

# 1. Estado canónico obligatorio al inicio

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Debe seguir vigente:

```text
EXP12_SOURCE_SCOPE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
H100_ROLE_IN_EXP12 = REFERENCE_LABEL_SET_AND_DISTRIBUTION_ONLY
H100_ROWS_ALLOWED_AS_EXP12_CANDIDATE_SAMPLING_ROWS = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Si existe drift de refs, detente:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

# 2. Fuentes y contratos que debes leer íntegramente

Antes de cualquier validación local, lee:

```text
docs/protocolo_expansion_historico_multisheet_v0.1.md
src/configs/new_historical_multisheet_contract_v0.1.json
src/ingestion/prepare_new_historical_multisheet_v0.1.py
outputs/audits/new_historical_gate_v0.1/new_historical_ingestion_manifest.json
outputs/audits/exp12_source_activation_v0.1/exp12_f007_source_activation_audit_v0.2.json
```

Hechos congelados:

```text
CURRENT_EXP12_SOURCE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
CURRENT_ELIGIBLE_ROWS_V01 = 6029
CURRENT_H100_REFERENCE_COVERAGE_V01 = 45/66
CURRENT_SOURCE_STATUS_V01 = FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE
VALID_NEW_SHEET_SET_2 = [NUEVA_01, NUEVA_02]
EXPECTED_WORKBOOK_SHEET_ORDER = [Hoja2, Hoja1, NUEVA_01, NUEVA_02]
```

El workbook `NUEVA_01` congelado debe obtenerse **de la ruta exacta registrada en**:

```text
outputs/audits/new_historical_gate_v0.1/new_historical_ingestion_manifest.json
```

No adivines otra copia.

---

# 3. Fase A — preflight read-only del workbook ampliado

Trabaja exclusivamente sobre:

```text
CURRENT_WORKBOOK = data/Series - Descripciones.xlsx
```

No lo modifiques ni lo guardes.

Registra:

```text
absolute_path
size_bytes
sha256
sheet_order
```

Exige exactamente:

```text
sheet_order = [Hoja2, Hoja1, NUEVA_01, NUEVA_02]
```

Si no se cumple:

```text
STOP / INVALID_EXPANDED_WORKBOOK_SHEET_ORDER
```

## 3.1 Preservación de hojas preexistentes

Antes de ingerir, verifica que `Hoja2`, `Hoja1` y `NUEVA_01` del workbook ampliado conservan el mismo **contenido de celdas** que el workbook congelado de `NUEVA_01` registrado por el manifiesto v0.1.

No exijas identidad binaria del XLSX completo: al añadir `NUEVA_02`, el contenedor ZIP puede cambiar aunque las hojas preexistentes mantengan su contenido.

Para cada una de estas tres hojas calcula, tanto en el baseline congelado como en el workbook ampliado, un fingerprint determinista read-only que incluya como mínimo:

```text
sheet_name
max_row
max_column
para cada celda no vacía en orden fila-columna:
    coordinate
    data_type
    valor/fórmula exacta serializada de forma determinista
```

Usa `openpyxl` con `data_only=False` y sin guardar los workbooks.

Exige:

```text
Hoja2_content_fingerprint_match = true
Hoja1_content_fingerprint_match = true
NUEVA_01_content_fingerprint_match = true
```

Si cualquiera difiere:

```text
STOP / PREEXISTING_SHEET_CONTENT_DRIFT
```

Registra los fingerprints baseline y current.

## 3.2 Parseabilidad mínima de `NUEVA_02`

Sin escribir datasets, usa el parser histórico gobernado para leer explícitamente `NUEVA_02` y registra:

```text
parsed_rows
parsed_columns
```

Exige:

```text
parsed_rows > 0
```

Si el parser falla o produce 0 filas:

```text
STOP / NUEVA02_NOT_PARSEABLE
```

Esto sigue siendo preflight; no es ingesta oficial.

---

# 4. Fase B — validación contractual no ingerente

Ejecuta exactamente una vez:

```powershell
python src/ingestion/prepare_new_historical_multisheet_v0.1.py \
  --validate-new-sheets \
  --future-workbook "data/Series - Descripciones.xlsx" \
  --new-sheet NUEVA_01 \
  --new-sheet NUEVA_02
```

Debe terminar:

```text
return_code = 0
RESULT: PASS
```

No uses todavía `--ingest-new-data`.

Si falla:

```text
STOP / NEW_SHEET_SET_VALIDATION_FAILED
```

No repares ni edites el XLSX.

---

# 5. Fase C — congelamiento binario de la fuente ampliada

Solo después de superar Fases A y B.

Toma el SHA-256 y tamaño del `CURRENT_WORKBOOK` y crea una copia byte-identical en el mismo directorio externo de archivo utilizado por el manifiesto v0.1.

Nombre obligatorio:

```text
Series - Descripciones_EXPANDED_NUEVA_01_NUEVA_02_SOURCE_<sha8>.xlsx
```

con `<sha8>` = primeros 8 caracteres del SHA-256 completo.

La copia debe realizarse mediante Python `shutil.copy2`, nunca abriendo/guardando con Excel/openpyxl.

Antes y después exige:

```text
source_sha_before = source_sha_after = archive_sha
source_size = archive_size
source_mutated = false
copy_method = Python shutil.copy2 binary copy
```

Si el destino ya existe:

- si SHA y tamaño son idénticos, reutilízalo sin reescribir;
- si difieren, detente con `STOP / ARCHIVE_PATH_COLLISION`.

Desde este punto, la ingesta debe usar **la copia archivada congelada**, no el workbook mutable de `data/`.

---

# 6. Fase D — ingesta controlada v0.2

## 6.1 No sobrescribir v0.1

Los siguientes directorios existentes son evidencia histórica y son inmutables durante este bloque:

```text
data/interim/new_historical_gate_v0.1/
outputs/audits/new_historical_gate_v0.1/
```

No uses `--overwrite` sobre ellos.

Los nuevos destinos son exclusivamente:

```text
data/interim/new_historical_gate_v0.2/
outputs/audits/new_historical_gate_v0.2/
```

Antes de ejecutar exige que ambos directorios v0.2 **no existan** o estén completamente vacíos.

Si contienen cualquier archivo previo:

```text
STOP / V02_OUTPUT_PREEXISTS
```

## 6.2 Única ingesta permitida

Ejecuta una sola vez, sobre la **copia archivada congelada**:

```powershell
python src/ingestion/prepare_new_historical_multisheet_v0.1.py \
  --ingest-new-data \
  --future-workbook <ARCHIVED_FROZEN_WORKBOOK> \
  --new-sheet NUEVA_01 \
  --new-sheet NUEVA_02 \
  --future-output-dir data/interim/new_historical_gate_v0.2 \
  --future-audit-dir outputs/audits/new_historical_gate_v0.2
```

No uses `--overwrite`.

Registra comando exacto, timestamps, exit code, stdout/stderr hashes y entorno Python.

Si falla:

- no reintentes automáticamente;
- no borres los outputs parciales;
- reporta `STOP / V02_INGESTION_FAILED` con evidencia;
- no ejecutes ninguna fase posterior.

---

# 7. Fase E — auditoría estructural EXP12 sobre el pool v0.2

Solo si la ingesta termina correctamente.

Usa exclusivamente:

```text
data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
```

como pool nuevo elegible candidato para EXP12.

Usa H100 únicamente como referencia de códigos:

```text
data/processed/data_aduanas_historico_clase87_v0.2.csv
SHA-256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
```

Calcula sin candidate generation y sin retrieval:

```text
v02_rows_total
v02_unique_dam
v02_unique_nandina_total
H100_reference_code_count
H100_reference_codes_present
H100_reference_codes_missing
H100_reference_coverage_fraction
missing_H100_reference_codes
```

Verifica además a partir de los artefactos de ingesta:

```text
rows_excluded_fixed_dev_eval_dam
rows_with_frozen_id_overlap
```

No leas desempeño EVAL ni uses resultados de modelos.

## 7.1 Estado estructural

Si:

```text
H100_reference_codes_present = 66
H100_reference_codes_missing = 0
H100_reference_coverage_fraction = 1.0
```

registra:

```text
EXP12_EXTENSION_COVERAGE_STATUS = PASS_66_OF_66_CANDIDATE
```

Esto **NO autoriza EXP12** y NO autoriza todavía los 10,000 candidatos por seed.

Si la cobertura sigue siendo menor de 1.0:

```text
EXP12_EXTENSION_COVERAGE_STATUS = FAIL_CLOSED_STILL_INSUFFICIENT
```

Reporta la lista residual exacta y detente científicamente allí.

---

# 8. Artefactos adicionales obligatorios v0.2

Crea, sin modificar outputs del script:

```text
outputs/audits/new_historical_gate_v0.2/source_extension_freeze_v0.2.json
outputs/audits/new_historical_gate_v0.2/exp12_source_coverage_audit_v0.2.json
```

## 8.1 `source_extension_freeze_v0.2.json`

Debe incluir al menos:

```text
source_workbook_path
source_sha256
source_size_bytes
source_sheet_order
baseline_nueva01_workbook_path
baseline_nueva01_workbook_sha256
preexisting_sheet_fingerprints_baseline
preexisting_sheet_fingerprints_current
preexisting_sheet_content_match = true
nueva02_parsed_rows
nueva02_parsed_columns
validate_new_sheets_return_code
validate_new_sheets_result
archive_path
archive_sha256
archive_size_bytes
copy_method
source_mutated = false
```

## 8.2 `exp12_source_coverage_audit_v0.2.json`

Debe incluir al menos:

```text
EXP12_SOURCE_SCOPE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
H100_ROLE_IN_EXP12 = REFERENCE_LABEL_SET_AND_DISTRIBUTION_ONLY
pool_path
pool_sha256
pool_rows
pool_unique_dam
pool_unique_nandina_total
H100_reference_code_count = 66
H100_reference_codes_present
H100_reference_codes_missing
H100_reference_coverage_fraction
missing_H100_reference_codes
required_label_coverage_fraction = 1.0
EXP12_EXTENSION_COVERAGE_STATUS
retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
candidate_generation_executed = false
exp12_authorized = false
exp12_executed = false
```

---

# 9. Versionado en candidato separado

No modifiques `main` durante Prompt55.

Crea desde exactamente:

```text
2b9571eee76ecffcaef1abc7fd4a12051f76f906
```

la rama:

```text
codex/exp12-new-historical-gate-extension-v02
```

Un solo commit.

Versiona únicamente artefactos nuevos v0.2 producidos por este bloque bajo:

```text
data/interim/new_historical_gate_v0.2/
outputs/audits/new_historical_gate_v0.2/
```

No versiones el XLSX fuente ni la copia archivada externa.

No modifiques ningún archivo existente fuera de esas dos raíces.

Los directorios pueden estar ignorados por Git; usa `git add -f` exclusivamente para los nuevos artefactos v0.2 gobernados.

## 9.1 Guard de transporte Git

Para cada artefacto nuevo calcula tamaño y SHA-256.

```text
MAX_SINGLE_GIT_ARTIFACT_BYTES = 90000000
```

- si `< 90,000,000` bytes: versiónalo;
- si `>= 90,000,000` bytes: NO lo comprimas, no lo trocees y no lo reescribas; déjalo como artefacto local oficial v0.2 y registra exactos `path`, `sha256`, `size_bytes` y estado `LOCAL_OFFICIAL_ARTIFACT_NOT_VERSIONED_DUE_TO_GIT_BLOB_LIMIT_GUARD` en el reporte y en un manifiesto pequeño versionado.

Crea si es necesario:

```text
outputs/audits/new_historical_gate_v0.2/versioning_manifest_v0.2.json
```

El candidato debe quedar pendiente de auditoría externa. No lo integres a `main`.

---

# 10. Prohibiciones absolutas

Durante Prompt55 NO:

- edites o vuelvas a guardar `data/Series - Descripciones.xlsx`;
- modifiques el workbook baseline archivado de `NUEVA_01`;
- modifiques H100, DEV o EVAL;
- sobrescribas `new_historical_gate_v0.1`;
- uses `--overwrite`;
- generes bancos EXP12;
- ejecutes `generate_exp12_candidates`;
- ejecutes 10,000 candidatos por seed;
- ejecutes retrieval/BM25/Top-k/MRR;
- leas desempeño EVAL;
- modifiques `src/configs/exp12_historical_diversity_control_v0.3.json`;
- crees autorización EXP12;
- modifiques Plan;
- modifiques Article;
- modifiques `main`;
- abras Grupo 2B o Grupo 3;
- vuelvas a ejecutar EXP11B.

---

# 11. Verificaciones finales obligatorias

Al finalizar exige:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato:

```text
parent = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
commits_ahead = 1
commits_behind = 0
all_changed_paths are under data/interim/new_historical_gate_v0.2/ or outputs/audits/new_historical_gate_v0.2/
```

Y:

```text
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_BM25_EXECUTED = false
EXP12_TOP_K_COMPUTED = false
EXP12_MRR_COMPUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

# 12. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/55_RESPUESTA_VALIDAR_CONGELAR_E_INGESTAR_EXTENSION_NUEVA02_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

# 13. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT55 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

CURRENT_WORKBOOK_PATH
CURRENT_WORKBOOK_SHA256
CURRENT_WORKBOOK_SIZE_BYTES
CURRENT_WORKBOOK_SHEET_ORDER

BASELINE_NUEVA01_WORKBOOK_PATH
BASELINE_NUEVA01_WORKBOOK_SHA256
Hoja2_content_fingerprint_match
Hoja1_content_fingerprint_match
NUEVA_01_content_fingerprint_match
NUEVA_02_PARSED_ROWS
NUEVA_02_PARSED_COLUMNS

VALIDATE_NEW_SHEETS_RETURN_CODE
VALIDATE_NEW_SHEETS_RESULT

ARCHIVE_PATH
ARCHIVE_SHA256
ARCHIVE_SIZE_BYTES
SOURCE_MUTATED

INGESTION_COMMAND
INGESTION_RETURN_CODE
INGESTION_RESULT

V02_POOL_PATH
V02_POOL_SHA256
V02_ROWS
V02_UNIQUE_DAM
V02_UNIQUE_NANDINA_TOTAL
H100_REFERENCE_CODES_PRESENT
H100_REFERENCE_CODE_COUNT
H100_REFERENCE_CODES_MISSING
H100_REFERENCE_COVERAGE_FRACTION
MISSING_H100_REFERENCE_CODES
EXP12_EXTENSION_COVERAGE_STATUS

CANDIDATE_BRANCH
CANDIDATE_COMMIT
CANDIDATE_PARENT
CANDIDATE_CHANGED_PATH_COUNT
LOCAL_ONLY_LARGE_ARTIFACT_COUNT

EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_BM25_EXECUTED = false
EXP12_TOP_K_COMPUTED = false
EXP12_MRR_COMPUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima si todo culmina:

```text
PROMPT55 = COMPLETED
NEW_HISTORICAL_GATE_EXTENSION_V02 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP12_EXTENSION_COVERAGE_STATUS = <PASS_66_OF_66_CANDIDATE | FAIL_CLOSED_STILL_INSUFFICIENT>
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
