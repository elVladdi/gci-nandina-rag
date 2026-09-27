# PROMPT121F — Respuesta G7-F02 REVIEW V03 — Bloque F: resultados 4.1.4 y Tablas 14–15

```text
PROMPT121F_EXECUTION = COMPLETE
A041_APPLIED = true
A042_APPLIED = true
A043_EXECUTED = false
TABLE_14_UPDATED_IN_PLACE = true
TABLE_15_UPDATED_IN_PLACE = true
FIGURE_6_CHANGED = false
INHERITED_TRACE_ROWS = 101
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 2
INHERITED_COMMENT_COUNT = 191
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 193
TRACKED_DELETION_COUNT = 0
ALL_COMMENT_IDS_ANCHORED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS
121G_EXECUTED = false
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

## 1. Precondiciones y fuentes gobernantes

Se leyó el artefacto exacto de congelamiento de fuentes requerido por 121F:

```text
REF = d91298758dba674003bf650e7a303c36bd0b74d9
PATH = docs/writing/group7/g7_writing_source_freeze_v0.1.json
ARTIFACT_ID = G7_F01_WRITING_SOURCE_FREEZE_v0.1
```

También se verificaron las fuentes científicas gobernantes fijadas por el prompt para este bloque:

- `docs/results/group5/g5_canonical_tables_v0.1.md` — blob `9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d`.
- `outputs/results/group5/g5_table_registry_v0.1.json` — blob `4fe9318d52fad093066ff9f42d524fc95e436245`.
- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json` — blob `a43893eca3dd756a1ff11935a9cf55afb728e8f4`.
- `outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_errors_by_support_v0.2.csv` — blob `0f70928ba83eec87c116e62cf104f505293bc092`.

Los binarios de entrada coincidieron con los SHA-256 exigidos antes de cualquier edición:

```text
INPUT_DOCX_SHA256 = a8c3054b12174fc72138fc5ee84f9d075e791a236e0eb7ca82fa89edbae4f310
INPUT_DOCX_SIZE_BYTES = 4570032
INPUT_TRACE_SHA256 = d4e660771a189c962d7237a73bb897de9871ad57d4ad32a7d5b0b2c451e1a356
INPUT_TRACE_ROWS = 101
```

## 2. A041 — recuperación histórica y Tabla 14

Se actualizó exclusivamente 4.1.4 y el mismo objeto de Tabla 14, manteniendo la convención REVIEW V03.

La presentación activa quedó sincronizada con el estado v0.2:

```text
BANCO_HISTORICO = 2 950 series
EVAL = 1 056 series / 67 DAM / 42 NANDINA
Top-1 = 0,5095 = 538/1 056
Top-3 = 0,6714 = 709/1 056
Top-5 = 0,7633 = 806/1 056
Top-10 = 0,8911 = 941/1 056
Top-50 = 0,9915 = 1 047/1 056 / SUPLEMENTARIO
MRR@100 = 0,6297
```

El título activo de Tabla 14 quedó como `Desempeño de la recuperación histórica en el conjunto interno de evaluación`. Las filas legacy que dejaron de formar parte de la presentación gobernante permanecen físicamente visibles con amarillo + tachado. No se creó un nuevo objeto de tabla.

## 3. A042 — soporte histórico por DAM y Tabla 15

Se actualizó el mismo objeto de Tabla 15 para representar el soporte histórico por número de DAM históricas que contienen la subpartida de referencia.

La presentación activa utiliza:

```text
1 DAM    | 27  | Top-1 0,3704 | Top-3 0,7037 | MRR 0,5644
2 DAM    | 21  | Top-1 0,0476 | Top-3 0,1905 | MRR 0,2394
3–4 DAM  | 425 | Top-1 0,6918 | Top-3 0,7671 | MRR 0,7602
5+ DAM   | 583 | Top-1 0,3997 | Top-3 0,6175 | MRR 0,5517
```

El título activo quedó como `Desempeño descriptivo de la recuperación histórica según soporte histórico por DAM`. Los buckets y columnas anteriores retirados de la presentación activa permanecen visibles como material superseded de revisión, con amarillo + tachado. La interpretación se mantiene descriptiva: no establece un gradiente monotónico simple, umbral post hoc de suficiencia, causalidad ni inferencia poblacional externa; HE5 permanece inconclusa con la evidencia disponible.

## 4. Comentarios y trazabilidad

Se añadieron exactamente dos comentarios nuevos, IDs `442` y `443`, con los seis apartados obligatorios en español. Los 191 comentarios heredados no fueron modificados.

Se conservaron byte-lógicamente las 101 filas heredadas de trazabilidad y se añadieron únicamente:

```text
G7F02-V03F-001 | A041 | TABLE_STRUCTURE_UPDATE / EXISTING_TABLE_ROW_UPDATE
G7F02-V03F-002 | A042 | TABLE_STRUCTURE_UPDATE / EXISTING_TABLE_ROW_UPDATE
```

Resultado: `TOTAL_TRACE_ROWS = 103`.

## 5. Validación estructural y visual

```text
BASELINE_TABLE_OBJECT_COUNT = 24
FINAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
TOTAL_COMMENT_COUNT = 193
COMMENT_442_ANCHORED = true
COMMENT_443_ANCHORED = true
ALL_COMMENT_IDS_ANCHORED = true
SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
FIGURE_4_CHANGED = false
FIGURE_5_CHANGED = false
FIGURE_6_CHANGED = false
A043_EXECUTED = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

El paquete DOCX conserva el mismo conjunto de 66 entradas. Los únicos contenidos OOXML modificados fueron `word/document.xml` y las cuatro partes de comentarios; todos los binarios de `word/media/` permanecen byte-idénticos.

Se renderizó el DOCX final y se inspeccionaron las páginas 106–110, que cubren la frontera anterior, el inicio de 4.1.4, Tabla 14, su interpretación, Tabla 15, su interpretación, Figura 6 legacy y el inicio de 4.1.5. No se observaron clipping, desbordamiento, superposición, filas ilegibles ni duplicación de tablas. Figura 6 y 4.1.5 permanecen intactas.

## 6. Salidas definitivas

```text
OUTPUT_DOCX = Molleapasa_gv_G7F02_REVIEW_V03_F.docx
OUTPUT_DOCX_SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
OUTPUT_DOCX_SIZE_BYTES = 4572575

OUTPUT_TRACE = g7_thesis_claim_traceability_v0.3_F.csv
OUTPUT_TRACE_SHA256 = 14d44b27012181bc943fa0325eb3c5964295ff040455ffe8c7c2b16f025eb337
OUTPUT_TRACE_SIZE_BYTES = 93547
```

La ejecución se detiene aquí para auditoría externa. No se ejecutó A043, 121G ni ningún bloque posterior.
