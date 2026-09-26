# PROMPT117 — CORREGIR PRESENTACIÓN PARA REVISIÓN HUMANA DE G7-F02 — V02

## 0. Rol y objetivo

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

Esta ejecución NO reabre la redacción científica desde cero. Corrige exclusivamente la **presentación para revisión humana** del candidato generado por Prompt116.

La IA Experimental revisó el candidato V01 y emite:

```text
PROMPT116_EXTERNAL_AUDIT = REVISION_REQUIRED_FOR_REVIEWABILITY
SCIENTIFIC_AUDIT = DEFERRED_UNTIL_REVIEW_COPY_IS_AVAILABLE
SCIENTIFIC_CONTENT_REWRITE_AUTHORIZED = false
G7_F02_REMAINS = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
```

El problema no es que Prompt116 no haya generado cambios científicos, sino que la forma de presentarlos dificulta la revisión del autor: el texto sustituido fue retirado de la vista, el texto nuevo no está resaltado en amarillo y no existe una convención visual uniforme que permita comparar directamente **antes vs. después**.

Tu objetivo es producir una **copia de revisión V02**, conservando la ciencia de V01, pero haciendo cada cambio visible y explicable.

---

## 1. Entradas autoritativas

### 1.1 Tesis baseline original

```text
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
SIZE_BYTES = 4360620
ROLE = ORIGINAL_BASELINE / MUST_REMAIN_UNMODIFIED
```

Debes partir del baseline original para recuperar literalmente el texto anterior. No reconstruyas texto eliminado a partir de resúmenes.

### 1.2 Candidato científico V01

```text
FILENAME = Molleapasa_gv_G7F02_CANDIDATE_V01.docx
SHA256 = e09b93a87378b7158736a3f3a18e72379b52b4cb14eadb445d0e2e0ba91dff8d
SIZE_BYTES = 4518781
ROLE = SCIENTIFIC_CONTENT_TARGET / NOT_APPROVED
```

El contenido científico propuesto en V01 es el objetivo que debe quedar visible como texto nuevo en la copia V02. No aproveches esta corrección de presentación para reescribir, ampliar, reducir o reinterpretar el contenido científico.

### 1.3 Trazabilidad V01

```text
FILENAME = g7_thesis_claim_traceability_v0.1.csv
SHA256 = 90f25fdf03b22e9def5013f3edc892f01dffd1f2b2529c6c82b1408c52936f6c
ROW_COUNT = 53
CHANGE_TYPES = 45 REPLACE / 6 UPDATE / 2 NEW
ROLE = CHANGE_MAP
```

### 1.4 Respuesta Prompt116

```text
writing_prompts_tmp/116_RESPUESTA_EJECUTAR_G7_F02_ACTUALIZACION_CIENTIFICA_TESIS.md
COMMIT = f63f11444aff515244eea8af7e96d80ed9f2641a
```

---

## 2. Hallazgo vinculante de revisión

La inspección estructural del V01 encontró:

```text
VISIBLE_STRIKETHROUGH_RUNS = 0
VISIBLE_YELLOW_HIGHLIGHT_RUNS = 0
TRACKED_INSERTION_ELEMENTS = 112
TRACKED_DELETION_ELEMENTS = 0
COMMENTS_XML_PRESENT = true
MAIN_DOCUMENT_COMMENT_REFERENCES = 67
```

Por tanto, aunque existen inserciones y comentarios, V01 no cumple el esquema visual de revisión solicitado por el autor.

No intentes resolverlo únicamente cambiando la vista de Control de cambios de Word. La copia V02 debe ser legible de forma determinista incluso en vista normal.

---

## 3. Convención visual obligatoria

### 3.1 Texto sustituido o propuesto para eliminar

**Nunca lo borres físicamente en V02.**

Debe permanecer en su ubicación lógica y mostrarse simultáneamente con:

```text
STRIKETHROUGH = true
HIGHLIGHT = YELLOW
VISIBLE_TEXT = true
```

Usa formato directo visible (`w:strike` + `w:highlight val="yellow"` o equivalente Word), **no** `w:del` como mecanismo principal.

El autor debe poder leer siempre el texto anterior, aunque Word esté en “Sin marcas”.

### 3.2 Texto nuevo o texto de reemplazo

Debe aparecer inmediatamente después del texto anterior correspondiente y mostrarse con:

```text
STRIKETHROUGH = false
HIGHLIGHT = YELLOW
VISIBLE_TEXT = true
```

No dependas de `w:ins` para que el texto sea visible. Puede existir internamente solo si no altera la visualización, pero la identificación del texto nuevo debe depender del resaltado amarillo.

### 3.3 Texto no afectado

Debe permanecer visualmente idéntico al baseline, sin resaltado amarillo y sin tachado nuevo.

### 3.4 Regla fundamental

```text
OLD_TEXT = YELLOW + STRIKETHROUGH
NEW_TEXT = YELLOW
UNCHANGED_TEXT = NORMAL
```

No utilices otros colores para codificar cambios.

---

## 4. Comentario Word obligatorio por cambio

Cada unidad de cambio material debe tener un **comentario real de Microsoft Word**, no una nota escrita dentro del cuerpo.

Preserva intactos todos los comentarios preexistentes del baseline. Añade comentarios nuevos con autor identificable como:

```text
IA de Redacción Científica — G7-F02
```

Cada comentario nuevo debe comenzar con el `trace_id` correspondiente y explicar de forma breve:

1. qué se cambia;
2. por qué se cambia;
3. qué fuente gobernante lo exige;
4. cuál es el límite interpretativo relevante, si aplica.

Formato recomendado:

```text
[G7F02-003]
Cambio: se sustituye la partición legacy por la partición v0.2 DAM-disjoint.
Razón: el estado experimental congelado usa H100=2950/28, DEV=100/6 y EVAL=1056/67/42.
Fuente: docs/analysis/group3/g3_analytical_contract_v0.1.md @ <blob>.
Límite: benchmark interno de Clase 87; no representa muestreo probabilístico de toda la NANDINA.
```

No copies comentarios gigantes ni informes completos dentro de cada comentario. Deben servir para revisión rápida.

Si una fila de trazabilidad afecta varias ubicaciones separadas, cada ubicación visualmente independiente debe recibir su propio comentario con el mismo `trace_id` y un sufijo opcional (`a`, `b`, `c`).

---

## 5. Granularidad de las sustituciones

Aplica el marcado en la unidad más pequeña que permita comparar el cambio con claridad.

### 5.1 Cambio de palabra o frase

En el mismo párrafo:

```text
[texto anterior: amarillo + tachado] [texto nuevo: amarillo]
```

No taches el párrafo entero si solo cambió una frase.

### 5.2 Reemplazo completo de párrafo

Conserva el párrafo anterior completo en amarillo + tachado y coloca inmediatamente después el párrafo nuevo completo en amarillo.

### 5.3 Contenido nuevo sin antecedente

Inserta únicamente el contenido nuevo resaltado en amarillo y añade comentario `NEW` explicando por qué se incorpora.

### 5.4 Eliminación sin reemplazo

Conserva el contenido original en amarillo + tachado. No lo elimines. Añade comentario indicando que se propone suprimirlo y por qué.

---

## 6. Tablas

No borres silenciosamente ninguna tabla del baseline.

### 6.1 Cambio localizado de celdas

Si la estructura de la tabla sigue siendo válida:

- conserva la tabla;
- dentro de cada celda afectada, conserva el valor/texto anterior en amarillo + tachado;
- inmediatamente después añade el nuevo valor/texto en amarillo;
- añade comentario en la celda o en el fragmento nuevo.

### 6.2 Tabla completamente sustituida

Si la tabla legacy y la tabla nueva tienen estructuras materialmente distintas:

1. conserva la tabla legacy completa;
2. marca todo su contenido textual como amarillo + tachado;
3. conserva su caption, también amarillo + tachado;
4. inserta inmediatamente después la nueva tabla V01;
5. resalta en amarillo todo el texto nuevo de la tabla y su caption;
6. añade comentario al caption de la tabla legacy y al caption de la nueva, con el `trace_id` y la fuente G5 correspondiente.

No suprimas la tabla antigua de la copia de revisión.

---

## 7. Figuras

Una imagen no puede representarse literalmente con tachado de fuente. Por ello aplica esta convención especial:

### Figura anterior sustituida

- conserva la imagen anterior íntegra;
- no la borres ni la ocultes;
- coloca inmediatamente antes de ella la etiqueta textual:

```text
VERSIÓN ANTERIOR — PROPUESTA PARA SUSTITUCIÓN
```

con **amarillo + tachado**;
- marca el caption anterior como amarillo + tachado;
- ancla un comentario al caption explicando la sustitución y su `trace_id`.

### Figura nueva

- coloca inmediatamente después la figura nueva V01;
- añade antes la etiqueta:

```text
VERSIÓN PROPUESTA — NUEVA
```

resaltada en amarillo, sin tachado;
- resalta en amarillo el caption nuevo;
- añade comentario con el `trace_id`, ID G6 y motivo del cambio.

No elimines figuras antiguas en V02.

---

## 8. TOC, listas y paginación en la copia de revisión

La copia V02 es para **revisión**, no para presentación final.

Debido a que conservar texto/tablas/figuras anteriores junto con los nuevos aumentará la longitud del documento:

- NO uses la paginación de V02 como paginación final;
- NO elimines contenido solo para recuperar el número de páginas de V01;
- conserva la estructura institucional;
- evita regenerar agresivamente el Índice, Lista de Tablas o Lista de Figuras si ello introduce duplicados o hace ilegible la comparación;
- si las listas quedan deliberadamente pendientes de sincronización final, añade un comentario de revisión indicando que se actualizarán en la copia limpia después de la aprobación del autor.

La prioridad en V02 es la comparación humana, no la compactación.

---

## 9. Contenido científico: prohibición de deriva

V02 debe ser una representación marcada de **V01**, no una nueva versión científica.

```text
NEW_SCIENTIFIC_CLAIMS = 0
NEW_METRICS = 0
NEW_INFERENCE = 0
NEW_P_VALUES = 0
NEW_CI = 0
NEW_REFERENCES = 0
```

No modifiques disposiciones ni guardrails:

```text
HG = NO_FORMAL_DISPOSITION_FOUND
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE

EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN
ATTEMPT06 = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

Si descubres durante la reconstrucción una diferencia científica entre baseline, V01 y la trazabilidad que impida reproducir fielmente V01, STOP y reporta la discrepancia. No la resuelvas por criterio propio.

---

## 10. Trazabilidad V02

Genera:

```text
g7_thesis_claim_traceability_v0.2.csv
```

Debe conservar las mismas 53 filas de V01, mismo `trace_id`, mismo orden y mismo contenido científico de las columnas existentes.

Añade al final estas columnas:

```text
old_text_preserved_visible
old_text_strikethrough
old_text_yellow_highlight
new_text_yellow_highlight
review_comment_added
review_comment_anchor
review_comment_summary
review_markup_status
```

Valores esperados para cada fila aplicable:

```text
old_text_preserved_visible = YES / NOT_APPLICABLE_FOR_NEW
old_text_strikethrough = YES / NOT_APPLICABLE_FOR_NEW
old_text_yellow_highlight = YES / NOT_APPLICABLE_FOR_NEW
new_text_yellow_highlight = YES
review_comment_added = YES
review_markup_status = PASS
```

No cambies las fuentes científicas, blobs, claims ni IDs canónicos de V01.

---

## 11. Output Word

Genera exclusivamente una copia de revisión nueva:

```text
Molleapasa_gv_G7F02_REVIEW_V02.docx
```

No sobrescribas:

- la tesis baseline;
- `Molleapasa_gv_G7F02_CANDIDATE_V01.docx`.

La V02 queda como:

```text
REVIEW_COPY / NOT_APPROVED / PENDING_AUTHOR_AND_EXTERNAL_AUDIT
```

No la presentes como tesis final ni como candidato limpio de entrega institucional.

---

## 12. QA estructural obligatorio

Antes de entregar comprueba programáticamente como mínimo:

```text
BASELINE_SHA256_UNCHANGED = true
V01_SHA256_UNCHANGED = true
TRACE_V01_SHA256_UNCHANGED = true
DOCX_ZIP_INTEGRITY = PASS
VISIBLE_STRIKETHROUGH_COUNT > 0
YELLOW_HIGHLIGHT_COUNT > 0
NEW_G7F02_REVIEW_COMMENT_COUNT >= 53
ALL_53_TRACE_ROWS_HAVE_REVIEW_MARKUP_STATUS_PASS = true
TRACKED_DELETION_USED_AS_ONLY_OLD_TEXT_REPRESENTATION = false
OLD_TEXT_PHYSICALLY_REMOVED_FROM_REVIEW_COPY = false
```

Los conteos deben excluir comentarios preexistentes cuando calcules `NEW_G7F02_REVIEW_COMMENT_COUNT`.

Preserva todos los comentarios preexistentes.

---

## 13. QA visual obligatorio

Renderiza el DOCX completo y revisa **todas las páginas**.

Verifica:

- que el amarillo sea visible;
- que el tachado sea visible;
- que viejo y nuevo no se superpongan;
- que tablas no queden cortadas o ilegibles;
- que las figuras anterior/nueva puedan distinguirse;
- que comentarios estén estructuralmente anclados aunque no aparezcan en el render PDF;
- que encabezados, pies, márgenes y numeración no se corrompan;
- que no haya texto desaparecido por formato oculto.

La V02 puede tener muchas más páginas que V01. Eso **no es defecto** en una copia de revisión.

---

## 14. Prohibiciones

No:

- borres texto baseline afectado;
- borres tablas legacy afectadas;
- borres figuras legacy afectadas;
- confíes solo en Control de cambios para mostrar diferencias;
- conviertas el texto anterior en `w:del` invisible como único mecanismo;
- cambies el contenido científico de V01;
- modifiques proyecto aprobado o v13;
- modifiques `main`, Plan, fichas o artículo;
- cierres G7-F02;
- autorices G7-F03;
- actives Grupo 8;
- autoapruebes V02.

---

## 15. Entregables obligatorios

Entrega:

```text
1. Molleapasa_gv_G7F02_REVIEW_V02.docx
2. g7_thesis_claim_traceability_v0.2.csv
```

Publica además la respuesta en:

```text
writing_prompts_tmp/117_RESPUESTA_CORREGIR_MARCADO_REVISION_G7_F02_V02.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT117_EXECUTION
BASELINE_SHA256
V01_SHA256
TRACE_V01_SHA256
REVIEW_V02_FILENAME
REVIEW_V02_SHA256
TRACE_V02_FILENAME
TRACE_V02_SHA256
TRACE_ROW_COUNT
VISIBLE_STRIKETHROUGH_COUNT
YELLOW_HIGHLIGHT_COUNT
NEW_G7F02_REVIEW_COMMENT_COUNT
PREEXISTING_COMMENTS_PRESERVED
OLD_TEXT_PHYSICALLY_REMOVED
TABLE_REVIEW_MARKUP_COUNT
FIGURE_REVIEW_PAIR_COUNT
ALL_TRACE_ROWS_MARKUP_PASS
DOCX_ZIP_INTEGRITY
RENDER_PAGE_COUNT
VISUAL_REVIEW
SCIENTIFIC_CONTENT_DRIFT_FROM_V01
NEW_SCIENTIFIC_CLAIMS
NEW_METRICS
NEW_INFERENCE
NEW_P_VALUES
NEW_CI
NEW_REFERENCES
G7_F02_STATUS
G7_F03_AUTHORIZED
EXTERNAL_AUDIT
```

Terminal esperado:

```text
PROMPT117_EXECUTION = COMPLETE
G7_F02_STATUS = REVISION_CANDIDATE_PENDING_AUTHOR_AND_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
SCIENTIFIC_CONTENT_DRIFT_FROM_V01 = false
OLD_TEXT_PHYSICALLY_REMOVED = false
ALL_TRACE_ROWS_MARKUP_PASS = true
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```
