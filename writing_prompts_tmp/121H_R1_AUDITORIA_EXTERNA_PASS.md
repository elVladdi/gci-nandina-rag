# PROMPT121H-R1 — Auditoría externa IA Experimental — PASS

```text
PROMPT121H_R1_EXTERNAL_AUDIT = PASS
A046_EXTERNAL_AUDIT = PASS_AFTER_R1
A047_EXTERNAL_AUDIT = PASS
SAMPLE_DESCRIPTION_CORRECTED = true
COMMENT_288_ANCHOR_RESTORED = true
COMMENT_288_CONTENT_UNCHANGED = true
ALL_COMMENT_IDS_ANCHORED = true
TRACE_CSV_BYTE_IDENTICAL_TO_H = true
TABLE_17_UNCHANGED_FROM_H = true
FIGURE_8_UNCHANGED_FROM_H = true
4_1_7_AND_AFTER_UNCHANGED_FROM_H = true
EXTERNAL_VISUAL_QA = PASS
121I_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## 1. Artefactos auditados

```text
Molleapasa_gv_G7F02_REVIEW_V03_H_R1.docx
SHA256 = 810b42ba934e411e893357e5713651e7b8f7d08df3c74b739eac49d387cff909
SIZE = 4667064

g7_thesis_claim_traceability_v0.3_H_R1.csv
SHA256 = bc9bf9cebe931e8747ca91c80f86726459f5a99b24e0c7dd076e3fa2e7314a31
SIZE = 100004
ROWS = 108
```

Los hashes, tamaños y conteo de filas coinciden con la respuesta oficial de ejecución R1. El CSV R1 es byte-idéntico al CSV H.

## 2. Verificación independiente de alcance OOXML

La comparación binaria del paquete H frente a H_R1 mostró 67 miembros en ambos DOCX y un único miembro modificado:

```text
word/document.xml
```

No se añadió ni eliminó ningún miembro del paquete. `word/comments.xml` permaneció byte-idéntico. La comparación del cuerpo identificó exactamente dos párrafos modificados:

1. primer párrafo de 4.1.6, para marcar el texto legacy completo como amarillo + tachado y añadir inmediatamente la descripción vigente de la muestra en amarillo sin tachado;
2. párrafo legacy de resultados de 4.1.6, exclusivamente para restaurar el anclaje heredado del comentario 288.

No se detectaron otros cambios de cuerpo.

## 3. R1-A — descripción de muestra diagnóstica

La presentación visible de 4.1.6 ahora conserva el texto legacy completo con amarillo + tachado y añade inmediatamente después una redacción activa que expresa:

- muestra de 20 casos;
- selección aleatoria uniforme sin reemplazo;
- marco de 1 056 series elegibles del conjunto de evaluación;
- al menos diez candidatos disponibles en el pool cerrado;
- semilla fija 0;
- diez candidatos entregados al LLM por caso;
- ejecución local, temperatura cero y sin acceso a códigos externos al pool.

La redacción es consistente con los artefactos gobernantes `reranker_diagnostic_sample_v0.2.csv`, `reranker_case_results_v0.2.csv` y `reranker_inputs_v0.2.jsonl`. No introduce inferencia poblacional externa, valores p ni intervalos de confianza.

## 4. R1-B — comentario 288

En H, el comentario 288 existía en `comments.xml` pero carecía de sus tres referencias en `document.xml`. En H_R1 se verificó exactamente una instancia de cada referencia:

```text
w:commentRangeStart w:id="288" = 1
w:commentRangeEnd   w:id="288" = 1
w:commentReference  w:id="288" = 1
```

El rango coincide con el rango heredado de G: abarca el texto legacy preservado del párrafo de resultados de 4.1.6. El contenido del comentario 288 no cambió porque `comments.xml` es byte-idéntico a H.

Conteo independiente:

```text
COMMENTS = 198
COMMENT_RANGE_START = 198
COMMENT_RANGE_END = 198
COMMENT_REFERENCE = 198
MISSING_COMMENT_ANCHORS = 0
COMMENT_447_ANCHORED = true
COMMENT_448_ANCHORED = true
```

## 5. Invariantes estructurales

La auditoría independiente confirmó:

```text
TABLE_OBJECT_COUNT_H = 24
TABLE_OBJECT_COUNT_H_R1 = 24
ALL_TABLE_XML_UNCHANGED_FROM_H = true
TABLE_17_UNCHANGED_FROM_H = true

SEQ_FIGURA_COUNT_H = 12
SEQ_FIGURA_COUNT_H_R1 = 12
NEW_SEQ_FIGURE_FIELDS = 0

MEDIA_FILE_COUNT_H = 16
MEDIA_FILE_COUNT_H_R1 = 16
ALL_MEDIA_NAMES_UNCHANGED = true
ALL_MEDIA_BINARIES_UNCHANGED_FROM_H = true
FIGURE_8_UNCHANGED_FROM_H = true

TRACKED_DELETION_COUNT = 0
4_1_7_BODY_INDEX_H = 561
4_1_7_BODY_INDEX_H_R1 = 561
4_1_7_AND_AFTER_OOXML_UNCHANGED_FROM_H = true
```

La comparación de todos los elementos del cuerpo desde el encabezado `4.1.7. Resultados de la explicación auditable del Top-3` hasta el final resultó idéntica entre H y H_R1.

## 6. QA visual externo

H_R1 se renderizó independientemente a PDF/PNG con LibreOffice mediante el flujo de auditoría DOCX. El render produjo 148 páginas. Se revisaron las páginas 116–119:

- página 116: el párrafo legacy de selección aparece amarillo + tachado y la nueva descripción vigente aparece inmediatamente después, amarilla y sin tachado;
- página 117: Tabla 17 conserva su presentación H y permanece legible;
- página 118: síntesis vigente, Figura 8 legacy y línea de supresión propuesta permanecen legibles y sin alteración material;
- página 119: 4.1.7 inicia intacta.

No se observaron clipping, solapamientos, desbordes, segunda numeración de figura ni alteración del inicio de 4.1.7.

## 7. Dictamen

Los dos defectos que motivaron `121H_EXTERNAL_AUDIT = REVISION_REQUIRED` quedaron corregidos sin ampliación de alcance. A046 queda cerrado después de R1 y A047 conserva su PASS previo.

```text
PROMPT121H_EXTERNAL_AUDIT_FINAL = PASS_AFTER_R1
121H_CLOSED_FOR_DOWNSTREAM = true
121I_AUTHORIZED = true
```

La autorización de 121I no autoriza 121J ni ningún bloque posterior. G7-F02 continúa `ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED` hasta completar y auditar los bloques restantes.
