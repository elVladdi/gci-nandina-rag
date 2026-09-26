# PROMPT121B-R1 — Respuesta: restauración mínima del ancla heredada del comentario 230

```text
PROMPT121B_R1_EXECUTION = COMPLETE
INPUT_DOCX_SHA256 = aecb2f7b008a16c85e7dc7a6d6b42cf30970e4f40b3f7ae19ae6f0f3e897244d
OUTPUT_DOCX_SHA256 = 875194ffb8b7413ffba8cc6a5136e6496763ce5552af0f12879fcc30044a18e3
OUTPUT_DOCX_SIZE_BYTES = 4178136
INPUT_TRACE_SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
OUTPUT_TRACE_SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
TRACE_BYTE_IDENTICAL = true
DOCX_UNCOMPRESSED_PARTS_CHANGED = word/document.xml ONLY
COMMENTS_XML_BYTE_IDENTICAL = true
COMMENTS_XML_COUNT = 134
COMMENT_RANGE_START_COUNT = 134
COMMENT_RANGE_END_COUNT = 134
COMMENT_REFERENCE_COUNT = 134
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
ORPHAN_COMMENT_IDS = NONE
VISIBLE_TEXT_CHANGES = 0
COMMENT_TEXT_CHANGES = 0
TRACE_CONTENT_CHANGES = 0
SCIENTIFIC_CHANGES = 0
TRACKED_DELETION_COUNT = 0
TOTAL_TABLE_OBJECT_COUNT = 24
LOCAL_VISUAL_REVIEW = PASS
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

## Entradas verificadas

Antes de modificar el paquete se recalcularon las identidades autoritativas:

```text
Molleapasa_gv_G7F02_REVIEW_V03_B.docx
SHA256 = aecb2f7b008a16c85e7dc7a6d6b42cf30970e4f40b3f7ae19ae6f0f3e897244d
SIZE_BYTES = 4178114

g7_thesis_claim_traceability_v0.3_B.csv
SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
SIZE_BYTES = 31468
```

También se verificó la referencia técnica opcional autorizada:

```text
Molleapasa_gv_G7F02_REVIEW_V03_A_R1.docx
SHA256 = c6ab7325068fbeb76e283b543da372c09f114bcaca57094afae61681f419ed90
SIZE_BYTES = 4170741
```

En A_R1, `w:id="230"` estaba anclado sobre el fragmento `El ` dentro del párrafo de 3.7.6 que comienza con `El repositorio Git/GitHub del proyecto...`.

## Reparación OOXML aplicada

Se modificó exclusivamente `word/document.xml` de la salida B. El párrafo heredado anterior de 3.7.6 fue identificado inequívocamente por su contenido y por `w14:paraId="7BE3FF08"`. El comentario nuevo `384` se encontraba en el mismo párrafo y permaneció intacto.

La salida B había consolidado todo el texto anterior tachado/resaltado en un único `w:r`/`w:t`. Como el contrato exige conservar exactamente el número y la secuencia de nodos `w:t`, no era posible volver a aislar el fragmento `El ` sin dividir ese nodo de texto. Por ello, la restauración técnicamente compatible con todas las invariantes ancló `230` sobre el `w:r` completo que contiene exclusivamente el texto anterior heredado, insertando:

```xml
<w:commentRangeStart w:id="230"/>
[run heredado anterior, sin modificación]
<w:commentRangeEnd w:id="230"/>
[run de w:commentReference w:id="230" recuperado de A_R1]
```

No se modificó ningún `w:t`, ningún `w:rPr` o `w:pPr` preexistente. El único `w:rPr` añadido pertenece al run de referencia del comentario 230 y reproduce el run heredado de A_R1. Al eliminar únicamente las tres inserciones de anclaje de la salida, `word/document.xml` vuelve byte a byte al `document.xml` de entrada B.

## QA estructural

```text
DOCX_ZIP_INTEGRITY = PASS
ZIP_ENTRY_COUNT = 64
ZIP_ENTRY_SET_PRESERVED = true
DOCX_UNCOMPRESSED_PARTS_CHANGED = word/document.xml ONLY
COMMENTS_XML_BYTE_IDENTICAL = true
COMMENTS_XML_COUNT = 134
COMMENT_RANGE_START_COUNT = 134
COMMENT_RANGE_END_COUNT = 134
COMMENT_REFERENCE_COUNT = 134
COMMENT_ID_SETS_EQUAL = true
COMMENT_230_EXISTS_IN_COMMENTS_XML = true
COMMENT_230_RANGE_START = true
COMMENT_230_RANGE_END = true
COMMENT_230_REFERENCE = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
ORPHAN_COMMENT_IDS = NONE
TRACKED_DELETION_COUNT = 0
TOTAL_TABLE_OBJECT_COUNT = 24
```

Los conjuntos de IDs de `comments.xml`, `commentRangeStart`, `commentRangeEnd` y `commentReference` son idénticos. No existe ningún ID huérfano ni duplicado.

## Ausencia de cambios visibles

```text
VISIBLE_TEXT_NODE_COUNT_BEFORE = 2349
VISIBLE_TEXT_NODE_COUNT_AFTER = 2349
VISIBLE_TEXT_SEQUENCE_SHA256_BEFORE = 43a8f5570789d88d6699bd9d2b2218f530661ab718f1751523cec0a024d13b69
VISIBLE_TEXT_SEQUENCE_SHA256_AFTER = 43a8f5570789d88d6699bd9d2b2218f530661ab718f1751523cec0a024d13b69
VISIBLE_TEXT_CHANGES = 0
COMMENT_TEXT_CHANGES = 0
TRACE_CONTENT_CHANGES = 0
SCIENTIFIC_CHANGES = 0
```

El CSV acumulativo fue copiado binariamente como `g7_thesis_claim_traceability_v0.3_B_R1.csv`; conserva exactamente 31 468 bytes y el mismo SHA-256 de B. No fue reserializado.

## QA visual

La entrada B y la salida B_R1 se renderizaron independientemente en 132 páginas. La comparación píxel a píxel de las 132 páginas produjo:

```text
PAGE_COUNT_INPUT = 132
PAGE_COUNT_OUTPUT = 132
PAGES_WITH_PIXEL_DELTA = 0
PAGE_LAYOUT_DELTA = 0
VISIBLE_CONTENT_DELTA = 0
CLIPPING = NONE
OVERFLOW = NONE
```

Se inspeccionaron además de forma localizada las páginas 78, 79 y 80. El párrafo reparado de 3.7.6 se encuentra en la página 79 y no presenta desplazamiento, recorte ni alteración visual.

## Salida

```text
Molleapasa_gv_G7F02_REVIEW_V03_B_R1.docx
SHA256 = 875194ffb8b7413ffba8cc6a5136e6496763ce5552af0f12879fcc30044a18e3
SIZE_BYTES = 4178136

g7_thesis_claim_traceability_v0.3_B_R1.csv
SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
SIZE_BYTES = 31468
TRACE_BYTE_IDENTICAL = true
```

## Estado terminal

```text
PROMPT121B_R1_EXECUTION = COMPLETE
DOCX_UNCOMPRESSED_PARTS_CHANGED = word/document.xml ONLY
COMMENTS_XML_BYTE_IDENTICAL = true
COMMENTS_XML_COUNT = 134
COMMENT_RANGE_START_COUNT = 134
COMMENT_RANGE_END_COUNT = 134
COMMENT_REFERENCE_COUNT = 134
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
ORPHAN_COMMENT_IDS = NONE
VISIBLE_TEXT_CHANGES = 0
COMMENT_TEXT_CHANGES = 0
TRACE_CONTENT_CHANGES = 0
TRACE_BYTE_IDENTICAL = true
SCIENTIFIC_CHANGES = 0
TRACKED_DELETION_COUNT = 0
TOTAL_TABLE_OBJECT_COUNT = 24
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Se detiene la ejecución. No se ejecutó 121C ni ningún bloque posterior.
