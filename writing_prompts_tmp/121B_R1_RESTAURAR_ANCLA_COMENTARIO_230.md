# PROMPT121B-R1 — RESTAURAR ANCLA HEREDADA DEL COMENTARIO 230

## 0. Rol

Actúa como **CODEX**, exclusivamente como ejecutor técnico de una reparación OOXML mínima sobre la copia REVIEW V03 de la tesis.

Esta ejecución **no es una nueva ronda de redacción científica**. No debes reinterpretar, reescribir, mejorar ni corregir contenido visible. La IA Experimental ya auditó Prompt121B y determinó que la ciencia, las cifras, la trazabilidad y el QA visual pasan; existe un único defecto estructural: el comentario heredado `230` quedó presente en `word/comments.xml` pero perdió su ancla en `word/document.xml`.

La auditoría vinculante está versionada en:

```text
writing_prompts_tmp/121B_AUDITORIA_EXTERNA_REVISION_REQUIRED.md
commit = 075cef69e237e924da28b90d265c8a1b05e8db83
```

## 1. Estado vinculante

```text
PROMPT121B_EXTERNAL_AUDIT = REVISION_REQUIRED
SCIENTIFIC_NUMERIC_ALIGNMENT = PASS
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

## 2. Entrada autoritativa

Usa exclusivamente como documento a reparar:

```text
Molleapasa_gv_G7F02_REVIEW_V03_B.docx
SHA256 = aecb2f7b008a16c85e7dc7a6d6b42cf30970e4f40b3f7ae19ae6f0f3e897244d
SIZE_BYTES = 4178114
```

Trazabilidad acumulativa asociada:

```text
g7_thesis_claim_traceability_v0.3_B.csv
SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
SIZE_BYTES = 31468
TRACE_ROWS = 42
```

Antes de cualquier operación, recalcula ambos SHA-256. Si cualquiera no coincide exactamente, **STOP**.

### Referencia técnica opcional y solo para reconstruir el ancla

Si se encuentra disponible localmente, puedes inspeccionar:

```text
Molleapasa_gv_G7F02_REVIEW_V03_A_R1.docx
SHA256 = c6ab7325068fbeb76e283b543da372c09f114bcaca57094afae61681f419ed90
SIZE_BYTES = 4170741
```

Su único uso autorizado es observar la posición OOXML original de `w:id="230"` y reproducir esa misma relación de anclaje sobre el párrafo heredado que continúa físicamente visible en B. **No copies texto, estilos, contenido científico, comentarios adicionales ni ninguna otra estructura desde A_R1.**

Si el párrafo de destino no puede identificarse inequívocamente, **STOP** y reporta la ambigüedad. No improvises un anclaje.

## 3. Defecto exacto a corregir

En el DOCX B:

```text
COMMENTS_XML_COUNT = 134
COMMENT_REFERENCE_COUNT = 133
ORPHAN_COMMENT_IDS = 230
```

El comentario `230` sigue presente en `word/comments.xml` con su contenido heredado. No debe cambiarse.

En la entrada A_R1, el comentario 230 estaba anclado al párrafo anterior de **3.7.6. Registro experimental y condiciones de ejecución** que comienza:

```text
El repositorio Git/GitHub del proyecto se utilizó como instrumento transversal para el control de versiones y la documentación del experimento.
```

y que incluye la delimitación histórica relativa a que los metadatos de todas las corridas no registraron sistemáticamente el hash del commit.

En B ese párrafo anterior continúa físicamente visible con el marcado de revisión correspondiente, seguido de la nueva formulación de reproducibilidad. Debes restaurar el ancla heredada del comentario 230 **sobre ese mismo texto anterior preservado**, sin tocar su contenido ni su formato.

El comentario nuevo `384` está correctamente anclado y debe quedar intacto.

## 4. Alcance EXCLUSIVO de la reparación

Realiza únicamente en `word/document.xml` las inserciones OOXML necesarias para que `w:id="230"` vuelva a tener:

```xml
<w:commentRangeStart w:id="230"/>
<w:commentRangeEnd w:id="230"/>
<w:commentReference w:id="230"/>
```

La posición debe reproducir, en la medida técnicamente posible, el anclaje heredado observado en A_R1 sobre el párrafo anterior conservado en 3.7.6.

### Debe permanecer byte-idéntico

No modifiques:

```text
word/comments.xml
```

ni ningún otro miembro ZIP salvo `word/document.xml`.

Cuando la biblioteca usada para reempaquetar el DOCX altere metadatos ZIP sin alterar el contenido interno, la validación debe hacerse sobre los **bytes descomprimidos de cada entrada**. Ninguna entrada distinta de `word/document.xml` puede cambiar en contenido.

## 5. Prohibiciones absolutas

No modifiques:

- ningún texto visible;
- ninguna cifra;
- ninguna hipótesis;
- ninguna tabla;
- ninguna figura;
- ninguna lista;
- ningún caption;
- ningún estilo, tamaño, color, resaltado o tachado;
- ningún comentario existente, incluido 230 y 384;
- ningún ID de comentario;
- ningún rango de comentario distinto de 230;
- ninguna relación, bookmark, campo, encabezado, pie o configuración;
- ningún contenido desde 3.1 hasta el final;
- ninguna fuente científica;
- el CSV de trazabilidad en contenido;
- GitHub fuera de la respuesta textual de esta ejecución.

No ejecutes 121C ni ningún bloque posterior.

## 6. Trazabilidad CSV

No existe cambio científico, editorial visible ni nueva decisión que registrar.

Por tanto:

```text
TRACE_ROWS_BEFORE = 42
TRACE_ROWS_AFTER = 42
TRACE_CONTENT_CHANGES = 0
```

Para mantener un par acumulativo de entregables puedes copiar el CSV con nombre:

```text
g7_thesis_claim_traceability_v0.3_B_R1.csv
```

pero sus bytes deben ser **idénticos** al CSV B de entrada y su SHA-256 debe permanecer exactamente:

```text
4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
```

No lo abras y vuelvas a serializar; si generas la copia, haz una copia binaria exacta.

## 7. Salida DOCX

Genera:

```text
Molleapasa_gv_G7F02_REVIEW_V03_B_R1.docx
```

No sobrescribas B.

No añadas el DOCX ni el CSV binario a Git.

## 8. QA OOXML obligatorio

Verifica antes y después de la reparación:

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

Además, compara todos los IDs de comentarios:

```text
COMMENTS_XML_IDS
COMMENT_RANGE_START_IDS
COMMENT_RANGE_END_IDS
COMMENT_REFERENCE_IDS
```

y exige igualdad de conjuntos. Si aparece cualquier otro huérfano, duplicación o pérdida de ID, **STOP**.

## 9. Prueba de ausencia de cambios visibles

Extrae la secuencia ordenada de todos los nodos `w:t` de `word/document.xml` antes y después de la reparación y verifica:

```text
VISIBLE_TEXT_NODE_COUNT_BEFORE = VISIBLE_TEXT_NODE_COUNT_AFTER
VISIBLE_TEXT_SEQUENCE_SHA256_BEFORE = VISIBLE_TEXT_SEQUENCE_SHA256_AFTER
VISIBLE_TEXT_CHANGES = 0
```

Verifica también que no cambió ningún `w:rPr` o `w:pPr` salvo que el mecanismo de `w:commentReference` requiera crear exclusivamente el run de referencia sin contenido visible; en ese caso documenta exactamente esa inserción y confirma que no altera formato del texto existente.

La comparación semántica no es suficiente: el texto visible debe ser idéntico.

## 10. QA visual localizado

Renderiza la salida y revisa la página que contiene el párrafo reparado de 3.7.6 —esperada alrededor de la página 80 en la renderización B— y una página adyacente si el renderer desplaza la paginación.

Exige:

```text
PAGE_LAYOUT_DELTA = 0
VISIBLE_CONTENT_DELTA = 0
CLIPPING = NONE
OVERFLOW = NONE
```

La reparación de comentario no debe cambiar la paginación ni la disposición visual.

## 11. Respuesta oficial

Publica únicamente la respuesta textual en:

```text
writing_prompts_tmp/121B_R1_RESPUESTA_RESTAURAR_ANCLA_COMENTARIO_230.md
```

rama:

```text
codex/prompts-temporary
```

Incluye al menos:

```text
PROMPT121B_R1_EXECUTION
INPUT_DOCX_SHA256
OUTPUT_DOCX_SHA256
OUTPUT_DOCX_SIZE_BYTES
INPUT_TRACE_SHA256
OUTPUT_TRACE_SHA256
TRACE_BYTE_IDENTICAL
DOCX_UNCOMPRESSED_PARTS_CHANGED
COMMENTS_XML_BYTE_IDENTICAL
COMMENTS_XML_COUNT
COMMENT_RANGE_START_COUNT
COMMENT_RANGE_END_COUNT
COMMENT_REFERENCE_COUNT
COMMENT_230_ANCHORED
COMMENT_384_UNCHANGED
ORPHAN_COMMENT_IDS
VISIBLE_TEXT_CHANGES
COMMENT_TEXT_CHANGES
TRACE_CONTENT_CHANGES
SCIENTIFIC_CHANGES
TRACKED_DELETION_COUNT
TOTAL_TABLE_OBJECT_COUNT
LOCAL_VISUAL_REVIEW
G7_F02_STATE
G7_F03_AUTHORIZED
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Terminal esperado:

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

Detente. No ejecutes 121C ni ningún bloque posterior.