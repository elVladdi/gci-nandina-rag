# PROMPT121F-FIG6-R3 — Auditoría externa de IA Experimental

## Dictamen

```text
PROMPT121F_FIG6_R3_EXTERNAL_AUDIT = PASS
A043_EXTERNAL_AUDIT = PASS
A043 = CLOSED_FOR_THIS_REVIEW_STEP
FIGURE_6_APPROVED_CANDIDATE_INTEGRATED = true
121G_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## 1. Identidad de artefactos auditados

Se auditó la respuesta oficial publicada en:

```text
writing_prompts_tmp/121F_FIG6_R3_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
@ 7982b55aa45a9ec2ee6819153cc34610c2a71d6d
```

contra los binarios entregados para auditoría externa:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F_FIG6_R3.docx
SHA256 = 817b7614026f0ec470db06e268906686de2d859ebe2a6ac9372af5d14ac91902
SIZE = 4661445

g7_thesis_claim_traceability_v0.3_F_FIG6_R3.csv
SHA256 = 8d2b7f801f438b32cf32398df96d9df3d2077d532dbce0dad45e222eb99ed7b3
SIZE = 94876
ROWS = 104
```

Las identidades coinciden exactamente con lo declarado por la ejecución.

## 2. Verificación independiente del DOCX

Se comparó byte/estructuralmente el candidato R3 contra la entrada gobernante:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
```

Resultados:

```text
TABLE_OBJECT_COUNT = 24 / UNCHANGED
TABLE_XML_ALL_24 = BYTE_EQUIVALENT_AFTER_CANONICALIZATION
SEQ_FIGURA_COUNT = 12 / UNCHANGED
TRACKED_DELETION_COUNT = 0
COMMENTS = 193 -> 194
NEW_COMMENT_ID = 444
ALL_COMMENT_IDS_ANCHORED = true
INHERITED_COMMENT_XML_UNCHANGED = true
EXISTING_MEDIA_REMOVED = 0
EXISTING_MEDIA_CHANGED = 0
NEW_MEDIA_FILES = 1
```

El único medio nuevo es:

```text
word/media/image16.png
SIZE = 112767
SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
DIMENSIONS = 3000 x 2000
DPI ~= 300
```

El relationship nuevo apunta exclusivamente a `media/image16.png`; todos los relationships heredados permanecen idénticos.

La comparación de texto visible entre F y R3 identificó únicamente tres párrafos nuevos en el punto de Figura 6: línea temporal de revisión, párrafo contenedor de la candidata y caption propuesto. Todos los demás párrafos conservaron el mismo texto. El único párrafo heredado con modificación de formato fue el caption legacy de Figura 6, cambio exigido por el contrato REVIEW V03: amarillo + tachado. Las 24 tablas permanecieron estructuralmente idénticas; en particular, Tablas 14–15 no fueron alteradas.

## 3. Figura 6 y contrato REVIEW V03

Se verificó:

```text
FIGURE_6_LEGACY_PRESERVED = true
LEGACY_CAPTION_VISIBLE = true
LEGACY_CAPTION_YELLOW = true
LEGACY_CAPTION_STRIKETHROUGH = true
TEMPORARY_REVIEW_LABEL_PRESENT = true
APPROVED_PNG_INSERTED = true
APPROVED_PNG_SHA256_MATCH = true
SECOND_SEQ_FIGURE_CREATED = false
PROPOSED_CAPTION_YELLOW = true
FIGURE_NUMBER_6_PRESERVED = true
```

El caption propuesto conserva los límites científicos aprobados: 31 corridas observadas; cinco condiciones H25/H50-D1/H50-D2/H75/H100 con distribución 10/5/5/10/1; H100 como `n=1` y referencia congelada; variación conjunta de tamaño y composición; interpretación descriptiva/no causal; ausencia de IC, valores p, regresiones, suavizados y resúmenes como marcas; límite al benchmark interno y ausencia de afirmación de exactitud global del RAG o validez externa.

No se introducen en el texto visible `EXP11A`, G6, FIG015, prompts, commits, blobs, gates ni lenguaje interno de gobernanza. Los identificadores H25, H50-D1, H50-D2, H75 y H100 se conservan legítimamente como identificadores científicos de condición.

## 4. Comentario 444

El comentario 444 está correctamente anclado y contiene íntegramente los seis apartados obligatorios en español:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Describe la preservación de la figura legacy, la inserción de la candidata aprobada, la ausencia de recálculo, las 31 corridas, la estructura de condiciones, la naturaleza descriptiva/no causal y los límites de interpretación. Los 193 comentarios heredados permanecen XML-idénticos.

## 5. Trazabilidad

Se compararon los CSV de entrada y salida. El archivo R3 comienza byte por byte con todo el archivo F y añade una única fila nueva; por tanto, las 103 filas heredadas permanecen byte-idénticas.

La única fila añadida es:

```text
trace_id = G7F02-V03F-FIG6-001
plan_id = A043
change_type = FIGURE_UPDATE
status = APPLIED
comment_id = 444
canonical_table_or_figure_id = Figura 6
```

La fila registra preservación de legacy, inserción de candidata, ausencia de segundo `SEQ`, hash del PNG, `scientific_data_change=NO`, `scientific_geometry_change=NO`, límites del benchmark y HE5 inconclusa.

## 6. QA visual externo

Se renderizó el DOCX auditado y se inspeccionaron externamente las páginas 110–112, que cubren el cierre de Tabla 15, Figura 6 legacy, la línea temporal, la candidata, el caption propuesto y el inicio de 4.1.5.

Resultado:

```text
PAGE_110 = PASS
PAGE_111 = PASS
PAGE_112 = PASS
CLIPPING = NONE
IMAGE_DISTORTION = NONE
OVERLAP = NONE
H100_REF_LEGIBLE = true
PROPOSED_CAPTION_LEGIBLE = true
4_1_5_BOUNDARY_INTACT = true
```

La Figura 6 candidata conserva proporción 3:2 y la etiqueta `H100 (ref.)` no se solapa con H75.

## 7. Cierre y autorización

No se detectaron defectos científicos, editoriales, OOXML, de trazabilidad ni de alcance que requieran R4.

```text
A043 = PASS / CLOSED_FOR_THIS_REVIEW_STEP
121G_AUTHORIZED = true
121G_EXECUTED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
```

El siguiente bloque puede comenzar exclusivamente desde los artefactos R3 auditados y debe detenerse nuevamente para auditoría externa antes de cualquier bloque posterior.