# PROMPT121D — Respuesta: Bloque D, Resultados 4.1.1–4.1.2

```text
PROMPT121D_EXECUTION = COMPLETE
INPUT_DOCX_SHA256 = 38b2b089a87b973a81be37108a2d303492de8a4a79a3acf99264750c1130deff
OUTPUT_DOCX_SHA256 = cedc46234c81a94626524d21847b27e5f59bbffb94b8de9bff323498c8c3d575
OUTPUT_DOCX_SIZE_BYTES = 4194621
INPUT_TRACE_SHA256 = 1ed85863b6a588ef2ce80cbfa05d105f1792de17fead99d2c634fafa19296c1f
OUTPUT_TRACE_SHA256 = 924f6220e8114bce6f8465e8f2c403cc8e9ebe2a3506136dd4d0533820974828
INHERITED_TRACE_ROWS = 75
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 9
COMMENTS_ADDED = 9
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

## Entradas verificadas

Antes de editar se recalcularon las identidades de las dos entradas vinculantes:

```text
Molleapasa_gv_G7F02_REVIEW_V03_C.docx
SHA256 = 38b2b089a87b973a81be37108a2d303492de8a4a79a3acf99264750c1130deff
SIZE_BYTES = 4193389

g7_thesis_claim_traceability_v0.3_C.csv
SHA256 = 1ed85863b6a588ef2ce80cbfa05d105f1792de17fead99d2c634fafa19296c1f
TRACE_ROWS = 75
```

Ambas entradas coincidieron con Prompt121D.

## A035 — 4.1.1 y Tabla 10

Se actualizaron exclusivamente los valores y descriptores de la partición final que todavía correspondían al estado legacy. La fuente gobernante fue:

```text
data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
blob = bcb02c9c3493235a6f80991158c5b24fa7c04510
```

La fuente confirma:

```text
HISTORICAL = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
EVAL = 1056 series / 67 DAM / 42 NANDINA
DAM_OVERLAP = 0
ID_UNICO_OVERLAP = 0
EVAL_CASES_WITH_HISTORICAL_SUPPORT = 1056 / 1056
EVAL_CODES_WITH_HISTORICAL_SUPPORT = 42 / 42
```

Se materializaron nueve cambios reales:

1. 4.1.1: `3 000 casos al banco histórico` → `2 950 casos al banco histórico`.
2. 4.1.1: `1 006 al conjunto de evaluación` → `1 056 al conjunto de evaluación`.
3. 4.1.1: `69 códigos disponibles después de la curación` → `66 códigos en la partición histórica`.
4. 4.1.1: `62 códigos` → `42 códigos` para el conjunto de evaluación.
5. Tabla 10 — Banco histórico, cantidad: `3 000` → `2 950`.
6. Tabla 10 — Banco histórico, cobertura: `69 códigos NANDINA distintos` → `66 códigos NANDINA distintos`.
7. Tabla 10 — Desarrollo, cobertura: `44 códigos NANDINA distintos` → `9 códigos NANDINA distintos`.
8. Tabla 10 — Evaluación, cantidad: `1 006` → `1 056`.
9. Tabla 10 — Evaluación, cobertura: `62 códigos NANDINA distintos` → `42 códigos NANDINA distintos`.

Se conservaron sin cambio los valores de 4 232 series iniciales y 4 106 series curadas, así como los demás resultados de curación y deduplicación.

## A036 — 4.1.2 y Tabla 11

A036 se ejecutó como `VERIFY / KEEP`. No se modificó texto, cifra, tabla, comentario ni trazabilidad en 4.1.2.

Se contrastó el estado visible contra el artefacto primario congelado:

```text
docs/auditoria_corpus_nandina_jerarquico_v0.1.md
blob = d06ae12f3cf4b8015a8b8176c1d621e0df9afb04
```

La auditoría confirma, entre otros valores, 9 785 registros totales, 1 020 partidas 4D, 1 117 registros HS-6, 7 648 registros NANDINA8, 407 NANDINA8 sin padre 4D, 4 504 sin padre HS-6 explícito, 56 grupos de padres duplicados conflictivos y 17 descripciones con posible contaminación. No se identificó una discrepancia material que autorizara una modificación adicional en este bloque.

## Convención de revisión y comentarios

Los nueve cambios de A035 conservan la convención obligatoria:

```text
TEXTO_ANTERIOR_MODIFICADO = AMARILLO + TACHADO + VISIBLE
TEXTO_NUEVO = AMARILLO + NO_TACHADO
TEXTO_SIN_CAMBIO = NORMAL
```

Se añadieron únicamente los comentarios `418–426`, uno por cambio real. Cada comentario contiene los seis encabezados obligatorios en español. No se añadió comentario ni fila de trazabilidad para A036 porque no hubo modificación.

## Trazabilidad

Las 75 filas heredadas de C permanecen byte-semánticamente preservadas como prefijo del CSV de salida. Se añadieron exclusivamente:

```text
G7F02-V03D-001 ... G7F02-V03D-009
```

Resultado:

```text
TRACE_ROWS_BEFORE = 75
TRACE_ROWS_AFTER = 84
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 9
```

## QA OOXML

```text
ZIP_ENTRY_COUNT = 64
DOCX_UNCOMPRESSED_PARTS_CHANGED = word/comments.xml; word/document.xml
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
COMMENTS_BEFORE = 167
COMMENTS_ADDED = 9
COMMENTS_AFTER = 176
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
TABLE_11_CHANGED = false
SECTION_4_1_2_CHANGED = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

Todos los comentarios heredados conservaron su contenido. No quedó ningún comentario huérfano.

## QA visual localizado

La salida se renderizó y se inspeccionaron las páginas 95–99 de la renderización, que comprenden la frontera anterior, 4.1.1, Tabla 10, 4.1.2, Tabla 11 y la frontera posterior hacia 4.1.3.

```text
PAGES_REVIEWED = 95; 96; 97; 98; 99
LOCAL_VISUAL_REVIEW = PASS
CLIPPING = NONE_OBSERVED
OVERFLOW = NONE_OBSERVED
UNEXPECTED_BLANK_PAGES = NONE_OBSERVED
TABLE_10_VISUAL = PASS
TABLE_11_VISUAL = PASS
```

## Salidas

```text
Molleapasa_gv_G7F02_REVIEW_V03_D.docx
SHA256 = cedc46234c81a94626524d21847b27e5f59bbffb94b8de9bff323498c8c3d575
SIZE_BYTES = 4194621

g7_thesis_claim_traceability_v0.3_D.csv
SHA256 = 924f6220e8114bce6f8465e8f2c403cc8e9ebe2a3506136dd4d0533820974828
SIZE_BYTES = 75082
TRACE_ROWS = 84
```

## Estado terminal

```text
PROMPT121D_EXECUTION = COMPLETE
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
TRACKED_DELETION_COUNT = 0
ALL_COMMENT_IDS_ANCHORED = true
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Se detiene la ejecución. No se ejecutó 121E ni ningún bloque posterior.
