# PROMPT121E-FIG45 — Respuesta de integración de Figuras 4 y 5 en REVIEW V03

```text
PROMPT121E_FIG45_EXECUTION = STOPPED_PRECONDITION
FIGURE_4_LEGACY_PRESERVED = true
FIGURE_4_APPROVED_CANDIDATE_INSERTED = false
FIGURE_5_LEGACY_PRESERVED = true
FIGURE_5_APPROVED_CANDIDATE_INSERTED = false
NEW_SEQ_FIGURE_FIELDS = 0
INHERITED_TRACE_ROWS = 99
NEW_TRACE_ROWS_ADDED = 0
INHERITED_COMMENT_COUNT = 189
COMMENTS_ADDED = 0
ALL_COMMENT_IDS_ANCHORED = true
TRACKED_DELETION_COUNT = 0
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = NOT_RUN_PRECONDITION_STOP
121F_EXECUTED = false
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

## 1. Verificación de las entradas autorizadas

La ejecución se inició desde las entradas exactas exigidas por el prompt y sus SHA-256 fueron recalculados antes de cualquier edición:

```text
INPUT_DOCX = Molleapasa_gv_G7F02_REVIEW_V03_E.docx
INPUT_DOCX_SHA256 = f6eb5a9f4db80faa36306df64ec51ddd865df2a081d69f65ca6a3e063ec2b7ba
INPUT_DOCX_SIZE_BYTES = 4199560
INPUT_DOCX_HASH_MATCH = true

INPUT_TRACE = g7_thesis_claim_traceability_v0.3_E.csv
INPUT_TRACE_SHA256 = c8bd644af8b660269f6bb7ea6f7cebf615ad9a3d23a42ac9a2814949ae8be05f
INPUT_TRACE_SIZE_BYTES = 87358
INPUT_TRACE_HASH_MATCH = true
```

La entrada Word conserva el estado estructural heredado esperado: 24 objetos de tabla, 189 comentarios con sus rangos y referencias anclados, 0 `w:del` y 12 campos `SEQ Figura` existentes.

## 2. Verificación de identidad de los candidatos aprobados

Se verificó en el commit de ejecución la identidad Git de ambos candidatos:

```text
FIGURE_4_PATH = figures/group7/g7_thesis_fig_04_he2.png
FIGURE_4_GIT_BLOB = eb77a4f2289a8701d22ba399d9432defd2092e2a
FIGURE_4_EXPECTED_SHA256 = 5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e
FIGURE_4_EXPECTED_SIZE_BYTES = 300119

FIGURE_5_PATH = figures/group7/g7_thesis_fig_05_coverage.png
FIGURE_5_GIT_BLOB = d63559e4da4b391d47968a60a41649c715d5408b
FIGURE_5_EXPECTED_SHA256 = aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0
FIGURE_5_EXPECTED_SIZE_BYTES = 164051
```

Las auditorías externas FIG011A y FIG011B identifican esos mismos candidatos como aprobados para integración posterior en el DOCX.

## 3. Precondición no satisfecha

El prompt establece expresamente: si no es posible acceder exactamente a los dos PNG aprobados, se debe detener la ejecución y no reconstruirlos ni sustituirlos por imágenes similares.

En el entorno de esta ejecución, el conector GitHub permite verificar los paths, blobs y contenido codificado de los binarios, pero no proporciona una materialización local íntegra del PNG utilizable por el editor OOXML. La única materialización local parcial disponible para Figura 4 tiene 4 500 bytes y SHA-256 `7e8e2103af50742576e4dae3a8ba9009d568d5cf80df2f338348a3b28798f6ae`, por lo que no coincide con el binario aprobado de 300 119 bytes. No existe una materialización local íntegra de Figura 5.

Por contrato, no se regeneraron los PNG desde SVG o scripts, no se reconstruyeron manualmente desde contenido parcial y no se utilizó ninguna imagen sustituta.

```text
EXACT_APPROVED_FIGURE_4_LOCAL_BINARY_AVAILABLE = false
EXACT_APPROVED_FIGURE_5_LOCAL_BINARY_AVAILABLE = false
PRECONDITION_FAILURE = EXACT_APPROVED_PNG_BYTES_NOT_MATERIALIZABLE
```

## 4. Integridad tras la detención

La detención ocurrió antes de editar el Word o la trazabilidad.

```text
OUTPUT_DOCX = NOT_GENERATED
OUTPUT_DOCX_SHA256 = NOT_APPLICABLE
OUTPUT_DOCX_SIZE_BYTES = NOT_APPLICABLE

OUTPUT_TRACE = NOT_GENERATED
OUTPUT_TRACE_SHA256 = NOT_APPLICABLE
OUTPUT_TRACE_SIZE_BYTES = NOT_APPLICABLE

A039_APPLIED = false
A040_APPLIED = false
DOCX_MODIFIED = false
TRACEABILITY_MODIFIED = false
FIGURE_4_CANDIDATE_INSERTED = false
FIGURE_5_CANDIDATE_INSERTED = false
COMMENTS_ADDED = 0
TRACE_ROWS_ADDED = 0
NEW_SEQ_FIGURE_FIELDS = 0
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

No se ejecutó 121F ni ningún bloque posterior. Para reanudar el mismo prompt sin ampliar alcance, deben ponerse a disposición del ejecutor los dos PNG exactos aprobados y verificarse sus SHA-256 antes de cualquier edición del DOCX.