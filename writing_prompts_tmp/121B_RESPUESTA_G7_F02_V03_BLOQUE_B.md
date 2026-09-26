# PROMPT121B — Respuesta G7-F02 V03, Bloque B: Metodología 3.5–3.7.6

```text
PROMPT121B_EXECUTION = COMPLETE
INPUT_DOCX_SHA256 = c6ab7325068fbeb76e283b543da372c09f114bcaca57094afae61681f419ed90
OUTPUT_DOCX_SHA256 = aecb2f7b008a16c85e7dc7a6d6b42cf30970e4f40b3f7ae19ae6f0f3e897244d
OUTPUT_DOCX_SIZE_BYTES = 4178114
INPUT_TRACE_SHA256 = c104eb43d7bf61e2a2653ae8cf1f41fb964341f3347a5c2b94e4ec17b5aba97a
OUTPUT_TRACE_SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
OUTPUT_TRACE_SIZE_BYTES = 31468
SECTIONS_MODIFIED = 3.5; 3.6; 3.7 (Tabla 6 únicamente); 3.7.4; 3.7.5; 3.7.6
TABLES_MODIFIED = 4; 5; 6; 7
A075_APPLIED = true
COMMENTS_ADDED = 28
TRACE_ROWS_INHERITED = 14
TRACE_ROWS_ADDED = 28
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
TRACKED_DELETION_COUNT = 0
LOCAL_VISUAL_REVIEW = PASS / PAGES_64_79_ALL_INSPECTED / PAGE_80_BOUNDARY_INSPECTED
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

## Entradas verificadas

Antes de editar se recalcularon las identidades de los dos artefactos acumulativos autorizados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_A_R1.docx
SHA256 = c6ab7325068fbeb76e283b543da372c09f114bcaca57094afae61681f419ed90
SIZE_BYTES = 4170741

g7_thesis_claim_traceability_v0.3_A_R1.csv
SHA256 = c104eb43d7bf61e2a2653ae8cf1f41fb964341f3347a5c2b94e4ec17b5aba97a
SIZE_BYTES = 8310
TRACE_ROWS = 14
```

Ambos coincidieron exactamente con las precondiciones de Prompt121B. Se partió exclusivamente de la salida aprobada del Bloque A/R1; no se utilizó V01, V02 ni la versión anterior a R1 como fuente de redacción.

## Ejecución de A016–A025 y A075

Se materializaron exclusivamente las intervenciones autorizadas:

- **A016 — 3.5:** se eliminó la contradicción entre muestreo no probabilístico e inferencia interna. Se mantuvo que no se calculó un tamaño muestral probabilístico para una población externa y se precisó que HE2 cuantifica incertidumbre dentro del benchmark interno mediante remuestreo pareado por conglomerados de DAM. Se actualizaron los tamaños finales a 2 950 / 100 / 1 056 y las menciones del conjunto de evaluación de 1 006 a 1 056 dentro de 3.5.
- **A017 — Tabla 4:** se conservó el mismo objeto. Se actualizó banco histórico 3 000→2 950, evaluación 1 006→1 056 y se incorporaron en las celdas existentes los conteos 28/6/67 DAM y 66/9/42 subpartidas NANDINA. Las submuestras de 20 y 50 permanecieron sin modificación.
- **A018 — 3.6:** se sustituyó la descripción legacy de la partición final por la materialización agrupada por DAM de v0.2. Se corrigieron 69→66 subpartidas en el banco histórico, 62→42 en evaluación y 3 000/100/1 006→2 950/100/1 056. Se explicitó cero solapamiento de DAM e `id_unico`, asignaciones explícitas de DAM y el carácter meramente metadata de la semilla 2026 para reproducir la composición final.
- **A019 — Tabla 5:** se conservaron estructura y objeto; solo se actualizaron las celdas de Partición e Independencia para reflejar agrupación por DAM, cero solapamiento y prevención de dependencia/fuga entre series de una misma declaración y entre particiones.
- **A020 — Tabla 6:** se conservaron las filas válidas de acopio, análisis documental y normalización. En Curación y partición se actualizó únicamente la condición y el producto final a v0.2 DAM-disjoint con 2 950/100/1 056.
- **A021 — 3.7.1:** `VERIFY / KEEP`. Se contrastó con las fuentes primarias del corpus (`text_index.py`, auditoría jerárquica, construcción del corpus jerárquico y `bm25_index.py`). No se confirmó una discrepancia material; por tanto, no se modificó la sección y no se añadió comentario ni fila de trazabilidad.
- **A022 — 3.7.3:** `TERMINOLOGY_ONLY / KEEP`. La revisión de `sunat_series_parser.py` no confirmó obsolescencia terminológica que autorizara cambio; la sección quedó intacta, sin comentario ni fila de trazabilidad.
- **A023 — 3.7.4:** se distinguió la curación/validación del marco de 4 106 series de la materialización posterior de la partición final v0.2. Se mantuvieron las reglas de campos obligatorios, NANDINA de ocho dígitos, coherencia jerárquica, parseo y duplicados. La partición final se vinculó a `src/evaluation/group_split_by_dam.py` y `src/configs/data_aduanas_split_clase87_v0.2.json`, con composición 2 950/100/1 056 y cero solapamiento de DAM e `id_unico`.
- **A024 — 3.7.5 / Tabla 7:** se conservó el mismo objeto y se modificó exclusivamente la fila Curación y partición. Se distinguieron `build_data_aduanas_splits.py` para la curación previa y `group_split_by_dam.py` + configuración v0.2 para la partición final; los artefactos finales quedaron identificados como los tres CSV v0.2 y el metadato v0.2.
- **A025 — 3.7.6:** se mantuvieron las condiciones válidas de ejecución local del LLM y se actualizó únicamente el párrafo de reproducibilidad. La nueva redacción describe trazabilidad/versionamiento sustancial con limitaciones documentadas: activos locales o ligados por hash, componentes históricos no recuperables, información incompleta de ciertos entornos y ejecuciones de LLM/evaluación por IA no reproducibles byte a byte. No se derivó de ello una decisión formal sobre HE1.
- **A075:** se corrigió de forma mínima `La Tabla 8 relaciona...` a `La Tabla 7 relaciona...`; la Tabla 7 no fue renumerada.

## Verificación científica del split final

La edición quedó consistente con las fuentes primarias de la partición v0.2:

```text
TOTAL_CURATED_SERIES = 4106
HISTORICAL = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
EVAL = 1056 series / 67 DAM / 42 NANDINA
DAM_OVERLAP_BETWEEN_SPLITS = 0
ID_UNICO_OVERLAP_BETWEEN_SPLITS = 0
FULL_ASSIGNMENT = true
FINAL_SPLIT_REPRODUCTION = EXPLICIT_DAM_ASSIGNMENT
FINAL_SPLIT_HEURISTIC_SEARCH = false
MODEL_METRIC_SELECTION = false
```

En el texto activo —excluyendo deliberadamente el material anterior tachado que debe permanecer visible por el contrato de revisión— ya no quedan dentro de 3.5–3.7.6 las formulaciones legacy `1 006`, `banco histórico de 3 000`, `69 subpartidas`, `cubrió 62`, `estratificación proporcional por NANDINA` como regla final, ni `La Tabla 8 relaciona`. Tampoco aparece en este bloque activo `reproducibilidad completa` ni `reproducibilidad total`.

## QA estructural y de alcance

```text
DOCX_ZIP_INTEGRITY = PASS
ZIP_ENTRY_COUNT_INPUT = 64
ZIP_ENTRY_COUNT_OUTPUT = 64
ZIP_ENTRY_SET_PRESERVED = true
DOCX_PARTS_CHANGED = word/document.xml; word/comments.xml
TOTAL_TABLE_OBJECT_COUNT = 24
TABLE_OBJECT_COUNT_DELTA = 0
TRACKED_DELETION_COUNT = 0
TOTAL_COMMENT_COUNT = 134
COMMENTS_ADDED = 28
NEW_COMMENT_IDS = 357..384
NEW_COMMENT_SCHEMA_PASS = true
INHERITED_COMMENTS_SEMANTICALLY_CHANGED = 0
INHERITED_TRACE_ROWS = 14
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 28
TOTAL_TRACE_ROWS = 42
A075_APPLIED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
BASELINE_BLOCK_A_CONTENT_PRESERVED = true
SECTION_3_7_7_ONWARD_PRESERVED = true
TABLES_8_24_PRESERVED = true
```

La comparación estructural localizó cambios únicamente en los párrafos y celdas autorizados de 3.5–3.7.6 y Tablas 4–7. El contenido previamente aprobado de 3.1–3.4 permaneció intacto. Los 14 registros de trazabilidad heredados son idénticos a la entrada.

## QA visual localizado

La salida acumulativa se renderizó después de las modificaciones. La renderización final contiene 132 páginas. El bloque afectado comienza en la página 64 y 3.7.7 comienza en la página 80.

Se inspeccionaron individualmente todas las páginas afectadas **64–79** y, además, la página **80** como frontera de continuidad. No se observaron clipping, desbordes, pérdida de texto, tablas cortadas de forma ilegible, desaparición de bordes, captions separados indebidamente ni páginas vacías accidentales. Las Tablas 4–7 permanecen legibles y el marcado amarillo/tachado conserva la comparación entre texto anterior y texto nuevo.

```text
LOCAL_RENDER_PAGE_RANGE_REVIEWED = 64..79
BOUNDARY_PAGE_REVIEWED = 80
LOCAL_VISUAL_REVIEW = PASS
```

## Salidas

```text
Molleapasa_gv_G7F02_REVIEW_V03_B.docx
SHA256 = aecb2f7b008a16c85e7dc7a6d6b42cf30970e4f40b3f7ae19ae6f0f3e897244d
SIZE_BYTES = 4178114

g7_thesis_claim_traceability_v0.3_B.csv
SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
SIZE_BYTES = 31468
```

## Estado terminal

```text
PROMPT121B_EXECUTION = COMPLETE
A075_APPLIED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
TRACKED_DELETION_COUNT = 0
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Se detiene la ejecución. No se ejecutó ningún bloque posterior.