# PROMPT121F-FIG6-R2 — Reintento localizado de integración de Figura 6 mediante Git blob local, sin Base64

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No regeneres la Figura 6, no recalcules datos y no ejecutes 121G.

Lee íntegramente antes de ejecutar:

```text
writing_prompts_tmp/121F_FIG6_R1_REINTENTO_LOCAL_FIRST_SIN_BASE64.md
@ d683d19bcdfde7b30e829f1c6bda1c8b9a3ac25e

writing_prompts_tmp/121F_FIG6_R1_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
@ 6c32047e0228439dbc35a913188a691109c45cd3

writing_prompts_tmp/121F_FIG6_R1_AUDITORIA_EXTERNA_STOP_COMPLIANT.md
@ 66bb123888d903fd60d80fae189485f8d9f0255f

figure_prompts_tmp/FIG015_AUDITORIA_EXTERNA_PASS.md
@ 4b916b6b2909fde6216654843aebdedcf2115cc3

writing_prompts_tmp/121F_FIG6_INTEGRAR_FIGURA6_REVIEW_V03.md
@ 67876fa408637051e07eb709a61d119ad9bf3745
```

Estado vinculante:

```text
PROMPT121F_FIG6_R1_EXTERNAL_AUDIT = PASS_STOPPED_PRECONDITION
FIG015_EXTERNAL_AUDIT = PASS
FIGURE_6_CANDIDATE_APPROVED_FOR_DOCX_INTEGRATION = true
A043_EXECUTED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
```

El bloqueo R1 fue exclusivamente `LOCAL_PNG_MISSING`. El artefacto aprobado sí existe en el historial Git remoto y no debe regenerarse.

## 1. Entradas acumulativas exactas

Trabaja exclusivamente sobre:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
SIZE = 4572575

g7_thesis_claim_traceability_v0.3_F.csv
SHA256 = 14d44b27012181bc943fa0325eb3c5964295ff040455ffe8c7c2b16f025eb337
ROWS = 103
```

Si cualquiera no coincide exactamente, `STOPPED_PRECONDITION`.

## 2. Identidad gobernante de la Figura 6 aprobada

```text
PATH_CANONICAL = figures/group7/g7_thesis_fig_06_sensitivity.png
FIG015_SOURCE_COMMIT = 78894c96cd59df36673def8647db88c96d50f953
GIT_BLOB = 667765204adbdb7ab7567e9546f6ed8c71051d91
SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
SIZE = 112767
DIMENSIONS = 3000 x 2000
```

No aceptes ningún otro binario aunque visualmente parezca idéntico.

## 3. Regla de materialización — Git binario local, sin Base64

La ejecución debe obtener el PNG como **binario Git local**, no mediante GitHub API/Base64/web.

### 3.1 Preflight del repositorio

Localiza el checkout Git canónico accesible. Verifica como mínimo:

```text
git rev-parse --is-inside-work-tree
git remote -v
git status --porcelain
```

No borres, muevas ni sobrescribas archivos no rastreados preexistentes. No hagas `reset --hard`, `clean`, `checkout -f` ni operaciones destructivas.

### 3.2 Ruta preferente A — working tree

Si existe:

```text
figures/group7/g7_thesis_fig_06_sensitivity.png
```

calcula SHA-256. Si coincide exactamente con el SHA gobernante, úsalo directamente.

### 3.3 Ruta preferente B — objeto Git ya disponible localmente

Si el archivo no existe en el working tree o no coincide, verifica si el objeto aprobado existe en el repositorio Git local:

```text
git cat-file -e 667765204adbdb7ab7567e9546f6ed8c71051d91^{blob}
```

Si existe, materialízalo **sin Base64** en un archivo temporal binario, por ejemplo:

```text
<temp>/g7_thesis_fig_06_sensitivity_approved.png
```

usando `git cat-file blob 667765204adbdb7ab7567e9546f6ed8c71051d91` o `git show 78894c96cd59df36673def8647db88c96d50f953:figures/group7/g7_thesis_fig_06_sensitivity.png`, redirigiendo stdout en modo binario.

Calcula SHA-256 y exige coincidencia exacta antes de usarlo.

### 3.4 Ruta excepcional C — una sola sincronización Git estándar

Solo si el blob no existe en el repositorio Git local, se autoriza **una única sincronización por transporte Git estándar** de la rama remota necesaria para traer el objeto, por ejemplo:

```text
git fetch --no-tags origin codex/prompts-temporary
```

Después del fetch:

1. verifica que el blob `667765204adbdb7ab7567e9546f6ed8c71051d91` existe localmente;
2. materialízalo mediante `git cat-file`/`git show` a archivo temporal binario;
3. verifica SHA-256, tamaño y dimensiones;
4. usa únicamente ese archivo temporal verificado.

No cambies de rama ni reescribas el working tree para obtener el PNG si no es necesario.

### 3.5 Prohibiciones absolutas de transporte

Está prohibido:

- GitHub API para recuperar el PNG;
- web/raw URL para recuperar el PNG;
- Base64;
- paginación o chunks Base64;
- copiar líneas codificadas;
- reconstrucción por fragmentos;
- regenerar PNG desde SVG;
- regenerar PNG desde renderer;
- usar una imagen similar;
- usar capturas de pantalla.

Si tras A/B/C no puede materializarse el blob exacto con SHA gobernante, reporta `STOPPED_PRECONDITION` con motivo `APPROVED_GIT_BLOB_NOT_MATERIALIZABLE`.

## 4. Alcance editorial único — A043

Una vez verificado el PNG, ejecuta exclusivamente A043 según el contrato de `121F_FIG6_INTEGRAR_FIGURA6_REVIEW_V03.md` y el contrato REVIEW V03 ya aplicado a Figuras 4 y 5.

Debe ocurrir exactamente:

1. conservar físicamente la Figura 6 legacy y su numeración oficial;
2. conservar visible su caption legacy y marcar únicamente el texto superseded según contrato de revisión;
3. insertar la línea temporal de revisión exacta, amarilla y estilo normal/no-caption;
4. insertar el PNG aprobado verificado;
5. insertar el caption propuesto completo aprobado para tesis, amarillo, sin segundo `SEQ Figura`;
6. añadir exactamente un comentario Word nuevo, íntegramente en español y con los seis encabezados obligatorios;
7. añadir exactamente una fila nueva de trazabilidad A043;
8. no modificar 4.1.5 ni ningún contenido posterior;
9. no ejecutar 121G.

Caption científico: usa el aprobado por FIG012/FIG014. Debe conservar 31 corridas; H100 `n=1, referencia congelada`; sensibilidad conjunta tamaño–composición; interpretación descriptiva/no causal; ausencia de IC, valores p, regresiones, suavizados y resúmenes como marcas; alcance interno del Capítulo 87; sin exactitud global del RAG ni validez externa.

No muestres en texto visible de tesis `EXP11A`, G6, FIG015, prompts, commits, blobs, gates ni lenguaje de gobernanza.

## 5. Invariantes estructurales

Verifica antes y después:

```text
TABLE_OBJECT_COUNT = 24
INHERITED_TRACE_ROWS = 103
NEW_TRACE_ROWS_ADDED = 1
TOTAL_TRACE_ROWS = 104
INHERITED_COMMENT_COUNT = 193
COMMENTS_ADDED = 1
TOTAL_COMMENT_COUNT = 194
TRACKED_DELETION_COUNT = 0
SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
FIGURE_4_UNCHANGED = true
FIGURE_5_UNCHANGED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

El binario insertado dentro de `word/media/` debe coincidir exactamente por SHA-256 con:

```text
4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
```

## 6. QA visual localizado

Renderiza e inspecciona únicamente las páginas necesarias que cubran:

- final de Tabla 15 / interpretación inmediata;
- Figura 6 legacy;
- línea temporal de revisión;
- Figura 6 candidata;
- caption propuesto completo;
- inicio de 4.1.5.

Verifica no clipping, no deformación, proporción 3:2, caption legible, ausencia de solapamientos, legacy preservada y 4.1.5 intacta.

No cambies márgenes, secciones ni tamaño de página.

## 7. Salidas R2

No sobrescribas F ni salidas inexistentes/fallidas anteriores. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F_FIG6_R2.docx
g7_thesis_claim_traceability_v0.3_F_FIG6_R2.csv
```

Publica la respuesta oficial en:

```text
writing_prompts_tmp/121F_FIG6_R2_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
```

Reporta SHA-256 y tamaño exactos de DOCX/CSV y termina con:

```text
PROMPT121F_FIG6_R2_EXECUTION = COMPLETE | STOPPED_PRECONDITION
PNG_SOURCE_MODE = WORKING_TREE | LOCAL_GIT_BLOB | GIT_FETCH_THEN_LOCAL_BLOB | NONE
GIT_FETCH_USED = true|false
BASE64_TRANSPORT_USED = false
GITHUB_API_PNG_TRANSPORT_USED = false
FIGURE_6_APPROVED_BLOB_MATCH = true|false
FIGURE_6_LOCAL_PNG_SHA256_MATCH = true|false
FIGURE_6_LEGACY_PRESERVED = true|false
FIGURE_6_APPROVED_CANDIDATE_INSERTED = true|false
FIGURE_6_EMBEDDED_BINARY_SHA256_MATCH = true|false
NEW_SEQ_FIGURE_FIELDS = 0|<n>
INHERITED_TRACE_ROWS = 103
NEW_TRACE_ROWS_ADDED = 1|<n>
TOTAL_TRACE_ROWS = 104|<n>
INHERITED_COMMENT_COUNT = 193
COMMENTS_ADDED = 1|<n>
TOTAL_COMMENT_COUNT = 194|<n>
ALL_COMMENT_IDS_ANCHORED = true|false
TRACKED_DELETION_COUNT = 0|<n>
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0|<n>
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0|<n>
LOCAL_VISUAL_REVIEW = PASS|FAIL
A043_EXECUTED = true|false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa. No ejecutes 121G ni ningún bloque posterior.
