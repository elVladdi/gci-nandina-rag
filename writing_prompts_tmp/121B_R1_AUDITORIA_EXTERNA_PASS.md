# PROMPT121B-R1 — AUDITORÍA EXTERNA IA EXPERIMENTAL

## Dictamen

```text
PROMPT121B_R1_EXTERNAL_AUDIT = PASS
PROMPT121B_EXTERNAL_AUDIT_FINAL = PASS_AFTER_R1
PROMPT121B_BLOCK_B = APPROVED

DOCX_IDENTITY = PASS
OOXML_SCOPE_CONFINEMENT = PASS
COMMENT_INTEGRITY = PASS
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
ORPHAN_COMMENT_IDS = NONE
VISIBLE_TEXT_CHANGES = 0
SCIENTIFIC_CHANGES = 0
TRACE_CONTENT_CHANGES = 0
VISUAL_PIXEL_DIFF = 0 / 132 pages

SCIENTIFIC_CORRECTION_REQUIRED = false
RERUN_REQUIRED = false
NEXT_BLOCK_121C_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Artefactos auditados

```text
INPUT_B = Molleapasa_gv_G7F02_REVIEW_V03_B.docx
INPUT_B_SHA256 = aecb2f7b008a16c85e7dc7a6d6b42cf30970e4f40b3f7ae19ae6f0f3e897244d

OUTPUT_R1 = Molleapasa_gv_G7F02_REVIEW_V03_B_R1.docx
OUTPUT_R1_SHA256 = 875194ffb8b7413ffba8cc6a5136e6496763ce5552af0f12879fcc30044a18e3
OUTPUT_R1_SIZE_BYTES = 4178136

TRACE_SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
TRACE_SIZE_BYTES = 31468

OFFICIAL_RESPONSE = writing_prompts_tmp/121B_R1_RESPUESTA_RESTAURAR_ANCLA_COMENTARIO_230.md
OFFICIAL_RESPONSE_COMMIT = bca4b72a837ad5e9183ab691e2c5b8501162c88e
```

Las identidades declaradas coinciden con los binarios auditados.

## Verificación OOXML independiente

La comparación entre B y B_R1 confirmó:

```text
ZIP_ENTRY_COUNT_B = 64
ZIP_ENTRY_COUNT_R1 = 64
ZIP_ENTRY_SET_PRESERVED = true
UNCOMPRESSED_PARTS_CHANGED = word/document.xml ONLY
COMMENTS_XML_BYTE_IDENTICAL = true

COMMENTS_XML_COUNT = 134
COMMENT_RANGE_START_COUNT = 134
COMMENT_RANGE_END_COUNT = 134
COMMENT_REFERENCE_COUNT = 134
COMMENT_ID_SETS_EQUAL = true
ORPHAN_COMMENT_IDS = NONE
DUPLICATED_COMMENT_IDS = NONE

COMMENT_230_IN_COMMENTS_XML = 1
COMMENT_230_RANGE_START = 1
COMMENT_230_RANGE_END = 1
COMMENT_230_REFERENCE = 1
COMMENT_384_IN_COMMENTS_XML = 1
COMMENT_384_RANGE_START = 1
COMMENT_384_RANGE_END = 1
COMMENT_384_REFERENCE = 1

TRACKED_DELETION_COUNT = 0
TOTAL_TABLE_OBJECT_COUNT = 24
```

En B, el comentario 230 estaba presente en `comments.xml` pero sin rango ni referencia. En B_R1 quedó nuevamente anclado sobre el párrafo heredado anterior de 3.7.6 identificado por `w14:paraId="7BE3FF08"`, sin alterar el texto del comentario ni el comentario 384.

## Ausencia de deriva visible o científica

La secuencia ordenada de nodos `w:t` es idéntica entre B y B_R1:

```text
VISIBLE_TEXT_NODE_COUNT_B = 2349
VISIBLE_TEXT_NODE_COUNT_R1 = 2349
VISIBLE_TEXT_SEQUENCE_EQUAL = true
VISIBLE_TEXT_CHANGES = 0
SCIENTIFIC_CHANGES = 0
```

El CSV de trazabilidad conserva el SHA-256 de B y no registra cambios de contenido.

## QA visual independiente

Se renderizó B_R1 y se comparó contra la renderización independiente ya disponible de B:

```text
PAGE_COUNT_B = 132
PAGE_COUNT_R1 = 132
PAGES_WITH_PIXEL_DELTA = 0
VISIBLE_CONTENT_DELTA = 0
PAGE_LAYOUT_DELTA = 0
```

La reparación del anclaje no produjo alteración visual en ninguna página.

## Cierre

La única regresión estructural detectada en Prompt121B quedó corregida sin tocar la ciencia ni la presentación. Por tanto, el Bloque B queda aprobado después de R1 y se autoriza exclusivamente el siguiente bloque modular de G7-F02.

```text
PROMPT121B_BLOCK_B = APPROVED
NEXT_BLOCK_121C_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```
