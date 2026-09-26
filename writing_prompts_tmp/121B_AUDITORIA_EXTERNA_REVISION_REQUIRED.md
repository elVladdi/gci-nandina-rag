# PROMPT121B — AUDITORÍA EXTERNA IA EXPERIMENTAL

## Dictamen

```text
PROMPT121B_EXTERNAL_AUDIT = REVISION_REQUIRED
SCIENTIFIC_NUMERIC_ALIGNMENT = PASS
AUTHORIZED_SCOPE_VISIBLE_CONTENT = PASS
TRACEABILITY_ROWS = PASS
NEW_COMMENT_SCHEMA = PASS
LOCAL_VISUAL_QA = PASS
DOCX_STRUCTURAL_COMMENT_INTEGRITY = FAIL
INHERITED_COMMENT_230_CONTENT = PRESERVED
INHERITED_COMMENT_230_ANCHOR = LOST
ORPHAN_COMMENT_IDS = 230
SCIENTIFIC_CORRECTION_REQUIRED = false
FULL_121B_RERUN_REQUIRED = false
MINIMAL_TECHNICAL_CORRECTION_REQUIRED = true
NEXT_BLOCK_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

El Bloque B no puede aprobarse todavía. La ciencia, las cifras, el alcance visible, la trazabilidad y el QA visual pasan la auditoría; existe un único defecto estructural OOXML: el comentario heredado `w:id="230"` continúa presente en `word/comments.xml`, pero perdió sus tres anclajes en `word/document.xml` durante la edición acumulativa.

---

## 1. Artefactos auditados

```text
DOCX = Molleapasa_gv_G7F02_REVIEW_V03_B.docx
DOCX_SHA256 = aecb2f7b008a16c85e7dc7a6d6b42cf30970e4f40b3f7ae19ae6f0f3e897244d
DOCX_SIZE_BYTES = 4178114

TRACE = g7_thesis_claim_traceability_v0.3_B.csv
TRACE_SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
TRACE_SIZE_BYTES = 31468

OFFICIAL_RESPONSE = writing_prompts_tmp/121B_RESPUESTA_G7_F02_V03_BLOQUE_B.md
OFFICIAL_RESPONSE_COMMIT = 970bd81f0ddab7ccd96de00b503f9fdb157a92bd
```

Las identidades de los dos artefactos entregados coinciden exactamente con la respuesta oficial de Prompt121B.

## 2. Verificación científica y de contenido visible

La auditoría independiente confirma que las modificaciones visibles del Bloque B se mantienen dentro del alcance autorizado y son coherentes con las fuentes primarias gobernantes:

```text
TOTAL_CURATED_SERIES = 4106
HISTORICAL = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
EVAL = 1056 series / 67 DAM / 42 NANDINA
DAM_OVERLAP_BETWEEN_SPLITS = 0
ID_UNICO_OVERLAP_BETWEEN_SPLITS = 0
FINAL_SPLIT_REPRODUCTION = EXPLICIT_DAM_ASSIGNMENT
FINAL_SPLIT_HEURISTIC_SEARCH = false
MODEL_METRIC_SELECTION = false
```

También queda correctamente delimitada la inferencia de HE2: remuestreo pareado por conglomerados de DAM dentro del benchmark interno, sin generalización poblacional externa ni valores p. La redacción de reproducibilidad conserva las limitaciones documentadas y no deriva una disposición formal de HE1.

A021 y A022 permanecieron sin cambio visible, como correspondía al no confirmarse una discrepancia primaria que autorizara su modificación. A075 quedó aplicado (`Tabla 8` → `Tabla 7`).

No se identificó una corrección científica, numérica o metodológica adicional necesaria en este bloque.

## 3. Trazabilidad CSV

La comparación independiente confirma:

```text
INPUT_TRACE_ROWS = 14
OUTPUT_TRACE_ROWS = 42
INHERITED_TRACE_ROWS_EXACTLY_PRESERVED = 14
NEW_TRACE_ROWS = 28
NEW_TRACE_ID_RANGE = G7F02-V03B-001 .. G7F02-V03B-028
```

Las 14 filas heredadas son idénticas a las de la entrada A_R1. Las 28 filas nuevas corresponden a cambios reales de B y mantienen el esquema acumulativo. No se generaron filas para A021/A022, que permanecieron `KEEP` sin cambio visible.

## 4. Comentarios Word — hallazgo estructural

La entrada A_R1 tenía:

```text
COMMENTS_XML_COUNT = 106
COMMENT_REFERENCE_COUNT = 106
ALL_COMMENTS_ANCHORED = true
```

La salida B tiene:

```text
COMMENTS_XML_COUNT = 134
NEW_COMMENTS = 28
NEW_COMMENT_IDS = 357..384
COMMENT_REFERENCE_COUNT = 133
ORPHAN_COMMENT_IDS = 230
```

Los 28 comentarios nuevos están presentes, correctamente anclados y contienen los seis encabezados obligatorios. El defecto afecta únicamente al comentario heredado `230`.

### Comentario heredado 230

Su contenido sigue presente en `word/comments.xml` y no debe modificarse:

> Razón metodológica: la redacción anterior suponía una vinculación exacta entre cada corrida y una confirmación del repositorio. Los scripts y documentos están versionados, pero no se verificó que todos los metadatos de ejecución registraran sistemáticamente el hash del commit; por ello, se delimitó la trazabilidad al historial, las rutas, las fechas y los documentos efectivamente disponibles.

En A_R1 este comentario estaba anclado al párrafo anterior de 3.7.6 relativo al uso del repositorio Git/GitHub y a la limitación del hash de commit. En B dicho párrafo se conserva físicamente como texto anterior tachado y resaltado, pero desaparecieron de `word/document.xml`:

```xml
<w:commentRangeStart w:id="230"/>
<w:commentRangeEnd w:id="230"/>
<w:commentReference w:id="230"/>
```

Por tanto, el comentario existe pero quedó huérfano. Esto constituye una regresión estructural de la copia acumulativa y debe corregirse antes de aprobar el Bloque B.

El comentario nuevo `384`, asociado a la actualización de 3.7.6, está correctamente anclado y no sustituye al comentario heredado 230.

## 5. Integridad OOXML y alcance

Se verificó:

```text
ZIP_ENTRY_COUNT_INPUT = 64
ZIP_ENTRY_COUNT_OUTPUT = 64
ZIP_ENTRY_SET_PRESERVED = true
DOCX_PARTS_CHANGED = word/document.xml; word/comments.xml
TOTAL_TABLE_OBJECT_COUNT = 24
TABLE_OBJECT_COUNT_DELTA = 0
TRACKED_DELETION_COUNT = 0
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
```

No se detectaron alteraciones visibles fuera del alcance científico autorizado. El hallazgo no exige repetir 121B ni rehacer su redacción; exige exclusivamente reparar el anclaje estructural heredado del comentario 230.

## 6. QA visual independiente

Se renderizó independientemente el DOCX de salida completo. La renderización produjo 132 páginas. Se inspeccionaron las páginas 64–79 y la página 80 como frontera de continuidad.

```text
PAGES_64_79 = PASS
PAGE_80_BOUNDARY = PASS
TABLES_4_7_VISUAL = PASS
CLIPPING = NONE_OBSERVED
OVERFLOW = NONE_OBSERVED
UNEXPECTED_BLANK_PAGES_IN_RANGE = NONE
```

El defecto del comentario 230 es estructural y no afecta la apariencia visual de la página.

## 7. Corrección autorizable

Se requiere una corrección mínima técnica `PROMPT121B-R1` con alcance exclusivo:

1. partir exactamente del DOCX B auditado;
2. restaurar en `word/document.xml` el anclaje del comentario heredado `230` sobre el mismo párrafo anterior conservado en 3.7.6;
3. no modificar el texto del comentario 230;
4. no modificar el comentario 384 ni ningún otro comentario;
5. no modificar texto visible, estilos, resaltados, tachados, tablas, figuras, listas o contenido científico;
6. conservar `word/comments.xml` byte a byte si es técnicamente posible;
7. conservar el CSV de trazabilidad B byte a byte, porque no existe cambio científico ni editorial visible que registrar;
8. verificar al cierre que los 134 comentarios estén anclados y que no exista ningún ID huérfano.

Terminal requerido tras la corrección:

```text
COMMENT_230_ANCHORED = true
COMMENTS_XML_COUNT = 134
COMMENT_REFERENCE_COUNT = 134
ORPHAN_COMMENT_IDS = NONE
VISIBLE_TEXT_CHANGES = 0
COMMENT_TEXT_CHANGES = 0
TRACE_CHANGES = 0
SCIENTIFIC_CHANGES = 0
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Hasta que R1 pase auditoría externa:

```text
NEXT_BLOCK_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```
