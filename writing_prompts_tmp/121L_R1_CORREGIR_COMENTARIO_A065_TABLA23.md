# PROMPT121L-R1 — Corregir precisión del comentario 465 de A065 / Tabla 23

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. Esta es una corrección documental mínima de 121L después de auditoría externa `REVISION_REQUIRED`.

Lee íntegramente antes de editar:

```text
writing_prompts_tmp/121L_AUDITORIA_EXTERNA_REVISION_REQUIRED.md
commit = 442146ec410b742470304e55af5ada2c5d196169

writing_prompts_tmp/121L_EJECUTAR_G7_F02_V03_BLOQUE_L_4_3_DISCUSION_RESULTADOS.md
commit = 3b9cd5114b638913a9505e9f817af906f9a56e6f
GIT_BLOB = f454faacfbcdb2e95de05ec70f5ac2e4a5480483

writing_prompts_tmp/121L_RESPUESTA_G7_F02_V03_BLOQUE_L_4_3_DISCUSION_RESULTADOS.md
commit = 3819d394caca49889898747d8b5f9298b6b07dd6
GIT_BLOB = 8fd3272c01864190bdd0bbb82a3457633d23c01c
```

Ejecuta exclusivamente la corrección del comentario Word 465 descrita aquí. **No ejecutes A068–A082, Conclusiones, Recomendaciones, 121M ni ningún bloque posterior.**

---

## 1. Entradas exactas

Trabaja exclusivamente sobre los artefactos L auditados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_L.docx
SHA256 = 01599c2b012964dc934daa43cdf831e10598a97d7c9fd642b1ef9190df8caebe
SIZE = 4685977

g7_thesis_claim_traceability_v0.3_L.csv
SHA256 = d6d27bf608f141ff490fa2c91f73d3e28c0637e5a94107abd0aae64f6362d5ee
SIZE = 123152
ROWS = 128
```

Verifica hashes, tamaños y filas antes de editar. Si no coinciden, devuelve `STOPPED_PRECONDITION` y no modifiques nada.

No reconstruyas L desde K ni desde ninguna versión anterior.

Estado heredado obligatorio:

```text
TABLE_OBJECT_COUNT = 24
COMMENT_COUNT = 217
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
TABLE_23_ROW_COUNT = 9
TABLE_23_COLUMN_COUNT = 4
COMMENT_465_ANCHORED = true
A068_A082_EXECUTED = false
121M_EXECUTED = false
```

---

## 2. Defecto único a corregir

En el DOCX L, el comentario Word `w:id="465"`, correspondiente a A065 / Tabla 23, contiene seis apartados obligatorios. Su primer apartado dice actualmente:

```text
Cambio exacto: Se actualizan únicamente las celdas propias de relación y límite de comparación de la misma Tabla 23, además de una interpretación inmediata, preservando antecedentes y referencias bibliográficas.
```

Esta formulación es inexacta. La modificación real de Tabla 23 afectó únicamente las celdas de la columna `Relación con el piloto` dependientes de resultados propios desactualizados. La columna `Límite de comparación` permaneció sin cambios.

La respuesta oficial de 121L también declara expresamente:

```text
Se modificaron exclusivamente celdas de la columna `Relación con el piloto` dependientes de resultados propios superseded; los hallazgos atribuidos a los antecedentes y la columna de límites de comparación se conservaron.
```

No existe ningún otro defecto autorizado para corregir en este R1.

---

## 3. Acción exacta sobre comentario 465

Conserva el mismo comentario 465, su mismo ID y sus mismos anclajes en `document.xml`.

Sustituye únicamente el texto del primer apartado `Cambio exacto:` por esta formulación:

```text
Cambio exacto: Se actualizan únicamente las celdas de la columna «Relación con el piloto» de la Tabla 23 que dependían de resultados propios desactualizados, además de la interpretación inmediata asociada; se preservan los antecedentes, las referencias bibliográficas y la columna «Límite de comparación».
```

Reglas obligatorias:

- no cambies el ID 465;
- no muevas, amplíes ni reduzcas el rango anclado del comentario 465;
- no cambies `commentRangeStart`, `commentRangeEnd` ni `commentReference` del comentario 465;
- conserva exactamente los otros cinco apartados del comentario 465 y su orden:
  `Motivo del cambio:`, `Evidencia concreta:`, `Fuente gobernante:`, `Efecto en la tesis:`, `Límite de interpretación:`;
- no añadas secciones ni párrafos adicionales al comentario 465;
- no modifiques ningún otro comentario, incluido su contenido, ID, metadatos o anclajes;
- no añadas ni elimines comentarios.

Resultado esperado:

```text
COMMENT_465_TEXT_CORRECTED = true
COMMENT_465_ID_UNCHANGED = true
COMMENT_465_ANCHOR_UNCHANGED = true
COMMENTS_462_464_466_467_UNCHANGED = true
INHERITED_OTHER_COMMENTS_UNCHANGED = true
TOTAL_COMMENT_COUNT = 217
ALL_NONEMPTY_COMMENT_IDS_ANCHORED = true
NEW_COMMENTS_ADDED = 0
COMMENTS_REMOVED = 0
```

---

## 4. Prohibición de cambios visibles y científicos

**No modifiques ningún contenido visible de la tesis.**

En particular:

```text
word/document.xml = BYTE_IDENTICAL_TO_L
TABLE_23 = OOXML_IDENTICAL_TO_L
TABLE_22 = OOXML_IDENTICAL_TO_L
TABLE_24 = OOXML_IDENTICAL_TO_L
FIGURE_11 = IDENTICAL_TO_L
FIGURE_12 = IDENTICAL_TO_L
4_2 = IDENTICAL_TO_L
4_3_VISIBLE_CONTENT = IDENTICAL_TO_L
CONCLUSIONES_AND_AFTER = IDENTICAL_TO_L
```

No cambies:

- texto visible, marcado amarillo o tachado;
- tablas, celdas o captions;
- estilos, propiedades de tabla, numeración, campos, secciones, encabezados o pies;
- bibliografía ni referencias;
- figuras ni medios;
- ciencia, métricas, inferencia, disposiciones de hipótesis o limitaciones;
- la referencia legacy previa a Tabla 23 `La Tabla 24 resume...`, porque A082 continúa diferida.

No ejecutes experimentos, búsqueda web ni recálculo alguno.

---

## 5. Partes OOXML permitidas

La única modificación autorizada dentro del paquete DOCX es el contenido textual del comentario 465 en:

```text
word/comments.xml
```

Debe cumplirse:

```text
word/document.xml = BYTE_IDENTICAL_TO_L
word/commentsExtended.xml = BYTE_IDENTICAL_TO_L
word/commentsExtensible.xml = BYTE_IDENTICAL_TO_L
word/commentsIds.xml = BYTE_IDENTICAL_TO_L
ALL_MEDIA_BINARIES = BYTE_IDENTICAL_TO_L
ALL_OTHER_ZIP_PARTS_EXCEPT_word/comments.xml = BYTE_IDENTICAL_TO_L
```

Dentro de `word/comments.xml`, todos los comentarios distintos de `w:id="465"` deben permanecer XML-idénticos. En el comentario 465 solo puede cambiar el texto del primer apartado `Cambio exacto:` especificado en §3; sus atributos y los otros cinco apartados deben permanecer iguales.

---

## 6. Trazabilidad CSV

**No modifiques el CSV L.**

Genera el CSV R1 como copia byte-idéntica de L:

```text
INPUT_CSV_SHA256 = d6d27bf608f141ff490fa2c91f73d3e28c0637e5a94107abd0aae64f6362d5ee
INPUT_CSV_SIZE = 123152
ROWS = 128
NEW_TRACE_ROWS_ADDED = 0
TRACE_CSV_BYTE_IDENTICAL_TO_L = true
```

La corrección R1 queda documentada en la respuesta de ejecución y en la auditoría externa posterior, no mediante una nueva fila de trazabilidad.

---

## 7. Controles estructurales y de alcance

Después de la corrección verifica:

```text
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
COMMENT_COUNT = 217
ALL_NONEMPTY_COMMENT_IDS_ANCHORED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
NEW_REFERENCES = 0
NEW_MEDIA_FILES = 0
NEW_SEQ_FIGURE_FIELDS = 0
A068_A069_EXECUTED = false
A070_A082_EXECUTED = false
CONCLUSIONES_EXECUTED = false
RECOMENDACIONES_EXECUTED = false
121M_EXECUTED = false
```

---

## 8. QA visual y estructural

Dado que `document.xml` debe permanecer byte-idéntico, no debe existir cambio visual respecto de L. Aun así, realiza una verificación localizada de 4.3.5 / Tabla 23 y del límite hacia 4.3.6 para confirmar que el paquete sigue renderizando correctamente.

Verifica además que el comentario 465:

- conserva exactamente seis apartados;
- tiene el nuevo `Cambio exacto:` de §3;
- conserva los otros cinco apartados sin cambios;
- continúa correctamente anclado;
- no provoca pérdida de ningún otro anclaje.

Si se modifica contenido visible o cualquier parte no autorizada, devuelve `REVISION_REQUIRED` y no declares COMPLETE.

---

## 9. Salidas obligatorias

No sobrescribas L. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_L_R1.docx
g7_thesis_claim_traceability_v0.3_L_R1.csv
```

Calcula y reporta SHA-256 y tamaño de ambos; reporta filas del CSV.

Publica respuesta oficial en:

```text
writing_prompts_tmp/121L_R1_RESPUESTA_CORREGIR_COMENTARIO_A065_TABLA23.md
```

La respuesta debe reportar como mínimo:

```text
PROMPT121L_R1_EXECUTION = COMPLETE | REVISION_REQUIRED | STOPPED_PRECONDITION
COMMENT_465_TEXT_CORRECTED = true|false
COMMENT_465_ID_UNCHANGED = true|false
COMMENT_465_ANCHOR_UNCHANGED = true|false
COMMENT_465_SIX_FIELDS_VALID = true|false
OTHER_216_COMMENTS_UNCHANGED = true|false
TOTAL_COMMENT_COUNT = 217
ALL_NONEMPTY_COMMENT_IDS_ANCHORED = true|false
DOCUMENT_XML_BYTE_IDENTICAL_TO_L = true|false
ALL_OTHER_ZIP_PARTS_EXCEPT_COMMENTS_XML_BYTE_IDENTICAL_TO_L = true|false
TRACE_CSV_BYTE_IDENTICAL_TO_L = true|false
CSV_ROWS = 128
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
NEW_REFERENCES = 0
A068_A082_EXECUTED = false
121M_EXECUTED = false
LOCAL_VISUAL_REVIEW = PASS|FAIL
DOCX_L_R1_SHA256 = <hash>
DOCX_L_R1_SIZE = <bytes>
CSV_L_R1_SHA256 = <hash>
CSV_L_R1_SIZE = <bytes>
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

---

## 10. Parada obligatoria

Al finalizar, detente para auditoría externa.

No ejecutes A068–A082, Conclusiones, Recomendaciones, 121M, G7-F03 ni ningún bloque posterior.
