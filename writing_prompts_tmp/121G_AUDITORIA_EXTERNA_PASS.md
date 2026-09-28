# PROMPT121G — Auditoría externa IA Experimental

```text
PROMPT121G_EXTERNAL_AUDIT = PASS
A044_EXTERNAL_AUDIT = PASS
A045_EXTERNAL_AUDIT = PASS
121H_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## 1. Identidad de entregables auditados

Se auditaron directamente los binarios entregados por el operador:

```text
Molleapasa_gv_G7F02_REVIEW_V03_G.docx
SHA256 = aaa5dbd7f65b9db13c75b82fb7bcbbd75373fb67e4c3b683de0c7181ec13eeaf
SIZE = 4664480

g7_thesis_claim_traceability_v0.3_G.csv
SHA256 = 9b65ddc4773996c272a6d3809bcae8b3321058db123d16dee56be3985b171857
SIZE = 97500
ROWS = 106
```

Ambos hashes y tamaños coinciden con la respuesta oficial publicada en `writing_prompts_tmp/121G_RESPUESTA_G7_F02_V03_BLOQUE_G_4_1_5_INTEGRACION.md` en el commit `05d2550c8c06995e73b9bf335d1113afc8926852`.

## 2. Trazabilidad y comentarios

El CSV de entrada aprobado tenía 104 filas. Las 104 filas heredadas permanecen byte-idénticas y se añadieron exactamente dos filas nuevas:

- `G7F02-V03G-001` → A044 / 4.1.5 / Tabla 16.
- `G7F02-V03G-002` → A045 / Figura 7.

El DOCX conserva los 194 comentarios heredados sin modificación y añade exactamente los comentarios `445` y `446`. Ambos están anclados y contienen los seis apartados exigidos, íntegramente en español:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

El comentario 445 queda anclado a la nueva prosa de integración; el 446, a la línea temporal de supresión propuesta de Figura 7.

## 3. Auditoría estructural OOXML

Comparación directa entre la entrada aprobada `Molleapasa_gv_G7F02_REVIEW_V03_F_FIG6_R3.docx` y la salida G:

```text
TABLE_OBJECT_COUNT = 24
TABLES_1_TO_15_XML_IDENTICAL = true
TABLE_16_CHANGED_IN_PLACE = true
TABLE_16_TBLPR_UNCHANGED = true
TABLE_16_TBLGRID_UNCHANGED = true
TABLE_16_CELL_PROPERTIES_UNCHANGED = true
TABLES_17_TO_24_XML_IDENTICAL = true

SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
TRACKED_DELETION_COUNT = 0

INHERITED_COMMENT_COUNT = 194
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 196
ALL_COMMENT_IDS_ANCHORED = true
INHERITED_COMMENTS_XML_IDENTICAL = true

MEDIA_FILE_COUNT_BEFORE = 16
MEDIA_FILE_COUNT_AFTER = 16
NEW_MEDIA_FILES = 0
ALL_MEDIA_BINARIES_SHA256_IDENTICAL = true
```

Dentro del paquete DOCX solo cambiaron `word/document.xml` y las partes de comentarios necesarias para incorporar 445–446. No cambió ningún archivo de medios.

El documento es byte/XML-idéntico desde el inicio hasta el encabezado 4.1.5 inclusive. Desde el encabezado 4.1.6 hasta el final, todos los bloques OOXML son byte-canónicamente idénticos a la entrada R3. Por tanto, 4.1.6, Tabla 17, Figura 8 y todos los bloques posteriores permanecen fuera de alcance y sin modificación.

## 4. A044 — 4.1.5 y Tabla 16

La ciencia presentada coincide con las fuentes gobernantes:

```text
EVAL = 1056 series
RANKING_INVARIANCE = 1056 / 1056
TOP1_UNCHANGED = true
TOP3_UNCHANGED = true
POSITIONS_UNCHANGED = true
HISTORICAL_SCORES_UNCHANGED = true
NO_NEW_CANDIDATE_INSERTED = true
NO_CANDIDATE_REMOVED = true
TRACEABILITY = 3168 / 3168
```

La nueva prosa deja explícito que la recuperación histórica genera y ordena candidatos, mientras que la evidencia normativa se asocia posteriormente sin reordenamiento. También conserva correctamente los límites: benchmark interno, ausencia de inferencia de corrección jurídica, suficiencia normativa/probatoria o validez externa.

La Tabla 16 preserva el mismo objeto, 9 filas y 4 columnas. En cada celda modificada, el texto anterior permanece visible con amarillo + tachado y el texto nuevo aparece en amarillo sin tachado. La presentación activa nueva es coherente con los controles de invariancia y trazabilidad aprobados.

La nota nueva declara correctamente `3 168 = 1 056 × 3` y separa trazabilidad documental de corrección jurídica y suficiencia probatoria.

No se detectaron IDs internos ni lenguaje de gobernanza nuevo visible en 4.1.5.

## 5. A045 — Figura 7

La Figura 7 legacy permanece físicamente insertada y su binario no cambió. Se conserva el `SEQ Figura` oficial existente y no se creó numeración adicional. Su caption legacy permanece visible con amarillo + tachado y se añadió, inmediatamente después del elemento gráfico, la línea temporal de revisión:

```text
PROPUESTA DE SUPRESIÓN DEL ELEMENTO GRÁFICO ANTERIOR — SE CONSERVA PARA REVISIÓN / NO ES NUMERACIÓN FINAL
```

No se insertó imagen de reemplazo, no se renumeraron Figuras 8–12 y no se modificó la Lista de Figuras.

## 6. QA visual externo

Se renderizó independientemente el DOCX auditado. Por diferencias de paginación del render headless, la zona auditada quedó materializada en las páginas visibles 112–117 del render externo. La inspección confirmó:

- final de Figura 6 e inicio de 4.1.5 legibles;
- texto legacy y texto nuevo claramente diferenciados;
- Tabla 16 completa, legible y sin clipping;
- Figura 7 legacy visible y sin deformación;
- caption legacy de Figura 7 visible, amarillo y tachado;
- línea temporal de supresión visible;
- 4.1.6 y Tabla 17 intactas en la frontera posterior;
- sin solapamientos ni recortes materiales.

La página intermedia antes de Tabla 16 conserva espacio en blanco por paginación/keep behavior, pero no produce pérdida de contenido, clipping ni alteración científica y no constituye un defecto bloqueante.

## 7. Dictamen

```text
PROMPT121G_EXECUTION = VERIFIED
PROMPT121G_EXTERNAL_AUDIT = PASS
A044 = CLOSED_FOR_THIS_REVIEW_STEP
A045 = CLOSED_FOR_THIS_REVIEW_STEP
TABLE_16_UPDATED_IN_PLACE = VERIFIED
FIGURE_7_SUPPRESSION_PROPOSED = VERIFIED
FIGURE_7_LEGACY_PRESERVED = VERIFIED
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
SCIENTIFIC_FIDELITY = PASS
OOXML_COMMENT_INTEGRITY = PASS
VISUAL_QA_EXTERNAL = PASS
121H_AUTHORIZED = true
121H_EXECUTED = false
G7_F03_AUTHORIZED = false
```

121H puede limitarse a A046/A047: 4.1.6 + Tabla 17 y supresión propuesta de Figura 8. Ningún bloque posterior queda autorizado por este PASS.