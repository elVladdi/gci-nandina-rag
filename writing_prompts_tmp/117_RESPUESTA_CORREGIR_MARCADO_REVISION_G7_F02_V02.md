# PROMPT117 — Respuesta de corrección de marcado para revisión humana de G7-F02 — V02

```text
PROMPT117_EXECUTION = COMPLETE
ACTOR = IA_DE_REDACCION_CIENTIFICA
SOURCE_PROMPT = writing_prompts_tmp/117_CORREGIR_MARCADO_REVISION_G7_F02_V02.md
SOURCE_PROMPT_COMMIT = 678613594e661b53b3d688a684d9dd2dd57f4fb7
BASELINE_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
V01_SHA256 = e09b93a87378b7158736a3f3a18e72379b52b4cb14eadb445d0e2e0ba91dff8d
TRACE_V01_SHA256 = 90f25fdf03b22e9def5013f3edc892f01dffd1f2b2529c6c82b1408c52936f6c
REVIEW_V02_FILENAME = Molleapasa_gv_G7F02_REVIEW_V02.docx
REVIEW_V02_SHA256 = 63db3d99cf3b123ee69e18e8191077495ba8717fcacf4f0476a1d7a00dba70e3
REVIEW_V02_SIZE_BYTES = 4590955
TRACE_V02_FILENAME = g7_thesis_claim_traceability_v0.2.csv
TRACE_V02_SHA256 = 5acb69066a9e1c2b5850406c4c71f7413df77cbf5a0400685cba372c9d787d2f
TRACE_ROW_COUNT = 53
VISIBLE_STRIKETHROUGH_COUNT = 1095
YELLOW_HIGHLIGHT_COUNT = 1840
NEW_G7F02_REVIEW_COMMENT_COUNT = 67
PREEXISTING_COMMENTS_PRESERVED = true
OLD_TEXT_PHYSICALLY_REMOVED = false
TABLE_REVIEW_MARKUP_COUNT = 35
FIGURE_REVIEW_PAIR_COUNT = 3
ALL_TRACE_ROWS_MARKUP_PASS = true
DOCX_ZIP_INTEGRITY = PASS
RENDER_PAGE_COUNT = 154
VISUAL_REVIEW = PASS / ALL_154_PAGES_INSPECTED
SCIENTIFIC_CONTENT_DRIFT_FROM_V01 = false
NEW_SCIENTIFIC_CLAIMS = 0
NEW_METRICS = 0
NEW_INFERENCE = 0
NEW_P_VALUES = 0
NEW_CI = 0
NEW_REFERENCES = 0
G7_F02_STATUS = REVISION_CANDIDATE_PENDING_AUTHOR_AND_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

## 1. Identidad de entradas

Antes y después de construir la copia de revisión se verificó que los tres insumos autoritativos conservaran exactamente sus SHA-256 congelados:

- baseline original: `08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed`;
- candidato científico V01: `e09b93a87378b7158736a3f3a18e72379b52b4cb14eadb445d0e2e0ba91dff8d`;
- trazabilidad V01: `90f25fdf03b22e9def5013f3edc892f01dffd1f2b2529c6c82b1408c52936f6c`.

Ninguno de esos tres archivos fue sobrescrito.

## 2. Convención de revisión materializada

La V02 es una copia de revisión, no una nueva versión científica. Se aplicó de forma visible y determinista la convención exigida:

```text
OLD_TEXT = YELLOW + STRIKETHROUGH + VISIBLE
NEW_TEXT = YELLOW + NO_STRIKETHROUGH + VISIBLE
UNCHANGED_TEXT = NORMAL
```

El texto anterior afectado permanece físicamente en la copia. No se utilizó `w:del` como único mecanismo de representación del texto anterior; el documento principal contiene `0` elementos tracked-deletion. La comprobación estructural verificó además que los bloques del baseline dentro del ámbito científico de revisión permanecen como subsecuencia ordenada de V02 y que los bloques científicos de V01 permanecen igualmente como subsecuencia ordenada de V02.

Conteos estructurales:

```text
VISIBLE_STRIKETHROUGH_COUNT = 1095
YELLOW_HIGHLIGHT_COUNT = 1840
TRACKED_DELETION_COUNT = 0
BASELINE_REVIEW_SCOPE_PRESERVED_AS_SUBSEQUENCE = true
V01_REVIEW_SCOPE_PRESERVED_AS_SUBSEQUENCE = true
```

## 3. Comentarios de revisión

Se preservaron los `92` comentarios preexistentes. Se añadieron `67` comentarios nuevos con autor:

`IA de Redacción Científica — G7-F02`

Los comentarios nuevos cubren las 53 filas de trazabilidad y las ubicaciones visualmente independientes que requirieron anclajes adicionales, incluidos captions antiguos/nuevos de tablas y figuras cuando correspondía.

```text
PREEXISTING_COMMENT_COUNT = 92
NEW_G7F02_REVIEW_COMMENT_COUNT = 67
TOTAL_COMMENT_COUNT = 159
MAIN_DOCUMENT_COMMENT_REFERENCE_COUNT = 159
PREEXISTING_COMMENTS_PRESERVED = true
```

## 4. Tablas y figuras

La copia conserva el contenido legacy afectado y muestra a continuación el contenido propuesto de V01 cuando la sustitución es material.

`TABLE_REVIEW_MARKUP_COUNT = 35` corresponde al número de instancias de tabla con marcado de revisión detectadas estructuralmente en V02; incluye las representaciones anterior/nueva y cambios localizados dentro del conjunto de 14 unidades tabulares modificadas por Prompt116.

Para figuras se verificaron las tres parejas científicas G6 requeridas:

```text
FIGURE_REVIEW_PAIR_COUNT = 3
FIGURE_NEW_LABEL_COUNT = 3
```

Las figuras sustituidas permanecen visibles con la etiqueta de versión anterior y las nuevas figuras V01 se presentan con la etiqueta de versión propuesta conforme a Prompt117.

## 5. Trazabilidad V02

`g7_thesis_claim_traceability_v0.2.csv` conserva exactamente las mismas 53 filas, el mismo `trace_id`, el mismo orden y el contenido científico de todas las columnas preexistentes de V01. Se añadieron únicamente las ocho columnas de marcado de revisión exigidas por Prompt117.

```text
TRACE_EXISTING_COLUMNS_PRESERVED = true
ALL_53_TRACE_ROWS_HAVE_REVIEW_MARKUP_STATUS_PASS = true
ALL_TRACE_ROWS_MARKUP_PASS = true
```

## 6. QA estructural y visual

El DOCX pasó prueba de integridad ZIP. Posteriormente se renderizó completo con el flujo de QA de documentos y se inspeccionaron visualmente las 154 páginas resultantes.

Se comprobó en el documento renderizado que:

- el amarillo y el tachado son visibles;
- texto anterior y texto nuevo permanecen diferenciables sin depender de la vista de Control de cambios;
- no se observaron superposiciones materiales entre bloques anterior/nuevo;
- las tablas permanecen legibles dentro del propósito de una copia de revisión;
- las figuras anterior/nueva son distinguibles;
- encabezados, pies, márgenes y numeración no presentan corrupción material;
- no se observó desaparición de texto por formato oculto.

La ampliación desde 97 páginas en V01 hasta 154 páginas en V02 es consecuencia esperada de conservar simultáneamente material anterior y propuesto y no se interpreta como defecto de paginación final.

```text
DOCX_ZIP_INTEGRITY = PASS
RENDER_PAGE_COUNT = 154
VISUAL_REVIEW = PASS / ALL_154_PAGES_INSPECTED
```

## 7. Control de deriva científica

No se reescribió la ciencia de V01. La ejecución se limitó a recuperar el baseline afectado, hacerlo visible junto al contenido científico V01 y añadir marcado/comentarios de revisión.

Se preservan sin modificación las disposiciones y guardrails fijados por Prompt117:

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

```text
SCIENTIFIC_CONTENT_DRIFT_FROM_V01 = false
NEW_SCIENTIFIC_CLAIMS = 0
NEW_METRICS = 0
NEW_INFERENCE = 0
NEW_P_VALUES = 0
NEW_CI = 0
NEW_REFERENCES = 0
```

## 8. Estado terminal

```text
PROMPT117_EXECUTION = COMPLETE
G7_F02_STATUS = REVISION_CANDIDATE_PENDING_AUTHOR_AND_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
SCIENTIFIC_CONTENT_DRIFT_FROM_V01 = false
OLD_TEXT_PHYSICALLY_REMOVED = false
ALL_TRACE_ROWS_MARKUP_PASS = true
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

No se modificaron `main`, Plan Maestro, fichas, artículo, proyecto aprobado ni v13. G7-F02 no fue cerrado ni autoaprobado.