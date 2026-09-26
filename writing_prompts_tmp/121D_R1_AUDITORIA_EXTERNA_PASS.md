# PROMPT121D_R1 — Auditoría externa independiente

```text
PROMPT121D_R1_EXTERNAL_AUDIT = PASS
PROMPT121D_BLOCK_D = PASS / APPROVED_FOR_CONTINUATION
A035 = VERIFIED / COMPLETE
A036 = VERIFIED / KEEP
NUMERICAL_CORRECTION_REQUIRED = false
ADDITIONAL_REVISION_REQUIRED = false
FULL_RERUN_REQUIRED = false
NEXT_BLOCK_121E_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## 1. Artefactos auditados

Se auditó independientemente la corrección localizada de `PROMPT121D_R1` contra el prompt autorizado, el DOCX entregado, la trazabilidad acumulativa, el estado D previamente auditado y las fuentes científicas gobernantes.

```text
Molleapasa_gv_G7F02_REVIEW_V03_D_R1.docx
SHA256 = 5b9a1d59e1e459f2772410d268029b976a552c59629c789c90ebfbfa160fca4b
SIZE_BYTES = 4195516

g7_thesis_claim_traceability_v0.3_D_R1.csv
SHA256 = 82582814e17a4e535c6f79d30d7629cc88076d51962adc4b316cc79954d8559d
SIZE_BYTES = 77788
TRACE_ROWS = 88
```

Los hashes y tamaños fueron recalculados sobre los binarios entregados y coinciden exactamente con la respuesta oficial.

## 2. Trazabilidad acumulativa

La comparación contra la trazabilidad D confirmó:

```text
INHERITED_TRACE_ROWS = 84
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 4
NEW_TRACE_IDS = G7F02-V03D-R1-001 .. G7F02-V03D-R1-004
```

Las cuatro filas nuevas corresponden exclusivamente a:

1. párrafo de 4.1.1: partición v0.2 por DAM, conteos `28 / 6 / 67` y cero solapamiento;
2. Tabla 10, banco histórico: `28 DAM; 66 códigos NANDINA distintos`;
3. Tabla 10, desarrollo: `6 DAM; 9 códigos NANDINA distintos`;
4. Tabla 10, evaluación: `67 DAM; 42 códigos NANDINA distintos`.

No se detectó alteración de las 84 filas heredadas.

## 3. Verificación científica de A035

La fuente gobernante continúa siendo:

```text
data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
blob = bcb02c9c3493235a6f80991158c5b24fa7c04510
```

Los hechos congelados son:

```text
ANALYSIS_UNIT = SERIE
GROUPING_FIELD = DECLARACION / DAM
HISTORICAL = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
EVAL = 1056 series / 67 DAM / 42 NANDINA
CROSS_SPLIT_DAM_OVERLAP = 0
CROSS_SPLIT_ID_UNICO_OVERLAP = 0
```

La versión R1 materializa correctamente esos resultados. En Tabla 10 aparecen los tres conteos DAM junto con las coberturas NANDINA ya aprobadas. El párrafo posterior declara que la partición final v0.2 se materializó mediante asignación explícita por DAM, mantiene cada DAM íntegramente en una sola partición, reporta `28 / 6 / 67` DAM, registra cero solapamiento de DAM e `id_unico` y conserva explícitamente el límite de benchmark interno sin inferir muestreo probabilístico ni validez externa.

Por tanto, el hallazgo que motivó la revisión de Prompt121D queda cerrado.

## 4. A036 y alcance

`A036` permanece `VERIFIED / KEEP`.

La comparación estructural confirmó que 4.1.2 y Tabla 11 no recibieron modificación visible. Tampoco se detectaron cambios visibles fuera del alcance autorizado.

```text
A036_VISIBLE_CHANGE = false
TABLE_11_CHANGED = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

## 5. Integridad OOXML y comentarios

La auditoría independiente confirmó:

```text
ZIP_ENTRY_SET_PRESERVED = true
TOTAL_TABLE_OBJECT_COUNT = 24
CHANGED_TABLE_OBJECTS = TABLE_10_ONLY
TRACKED_DELETION_COUNT = 0
INHERITED_COMMENT_COUNT = 176
COMMENTS_ADDED = 4
TOTAL_COMMENT_COUNT = 180
NEW_COMMENT_IDS = 427..430
INHERITED_COMMENT_TEXT_CHANGED = 0
INHERITED_ORPHAN_COMMENT_IDS = NONE
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
COMMENTS_418_426_UNCHANGED = true
```

Solo cambiaron `word/document.xml` y `word/comments.xml`. En Tabla 10 se modificaron exclusivamente las tres celdas `Lectura` autorizadas. Los cuatro comentarios nuevos contienen los seis encabezados obligatorios y están vinculados a cambios reales.

La convención de revisión se preservó: material anterior modificado visible en amarillo y tachado, material nuevo en amarillo sin tachado y ausencia de `w:del`.

## 6. Revisión visual independiente

Se renderizó la salida y se inspeccionó localmente la zona afectada y sus fronteras. Tabla 10, el párrafo corregido y la transición hacia 4.1.2/Tabla 11 permanecen legibles.

```text
LOCAL_VISUAL_REVIEW = PASS
CLIPPING = NONE_OBSERVED
OVERFLOW = NONE_OBSERVED
BROKEN_TABLES = NONE_OBSERVED
UNEXPECTED_BLANK_PAGES = NONE_OBSERVED
```

No se identificó un defecto visual que requiera corrección antes de continuar.

## 7. Dictamen

```text
PROMPT121D_R1_EXTERNAL_AUDIT = PASS
PROMPT121D_BLOCK_D = PASS / APPROVED_FOR_CONTINUATION
A035 = VERIFIED / COMPLETE
A036 = VERIFIED / KEEP
INHERITED_TRACE_ROWS = 84
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 4
TOTAL_TRACE_ROWS = 88
TOTAL_COMMENT_COUNT = 180
TRACKED_DELETION_COUNT = 0
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS
NEXT_BLOCK_121E_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

La aprobación corresponde exclusivamente al Bloque D acumulado hasta `D_R1`. No constituye aprobación global de G7-F02 ni autoriza G7-F03.