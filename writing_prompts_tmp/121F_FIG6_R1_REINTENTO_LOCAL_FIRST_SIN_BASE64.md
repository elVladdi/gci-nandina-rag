# PROMPT121F-FIG6-R1 — Reintento localizado de integración de Figura 6, local-first y sin transporte Base64

## 0. Actor y motivo

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No regeneres la Figura 6, no recalcules datos y no ejecutes 121G.

Este prompt sustituye operacionalmente el reintento idéntico de `writing_prompts_tmp/121F_FIG6_INTEGRAR_FIGURA6_REVIEW_V03.md` porque dos ejecuciones consecutivas agotaron el tiempo durante la recuperación fragmentada del PNG mediante Base64. El fallo fue de transporte/ejecución, no científico.

No reutilices como válido ningún resultado no publicado de los intentos con timeout. Parte exclusivamente de los artefactos gobernantes versionados y de los binarios locales verificados por hash.

## 1. Estado gobernante

Lee íntegramente:

```text
figure_prompts_tmp/FIG015_AUDITORIA_EXTERNA_PASS.md
@ 4b916b6b2909fde6216654843aebdedcf2115cc3

writing_prompts_tmp/121F_FIG6_INTEGRAR_FIGURA6_REVIEW_V03.md
@ 67876fa408637051e07eb709a61d119ad9bf3745
```

Estado vinculante:

```text
FIG015_EXTERNAL_AUDIT = PASS
FIGURE_6_CANDIDATE_APPROVED_FOR_DOCX_INTEGRATION = true
A043_EXECUTED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
```

## 2. Entradas exactas

Trabaja exclusivamente sobre:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
SIZE = 4572575

g7_thesis_claim_traceability_v0.3_F.csv
SHA256 = 14d44b27012181bc943fa0325eb3c5964295ff040455ffe8c7c2b16f025eb337
ROWS = 103
```

Figura 6 aprobada:

```text
PATH = figures/group7/g7_thesis_fig_06_sensitivity.png
GIT_BLOB = 667765204adbdb7ab7567e9546f6ed8c71051d91
SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
SIZE = 112767
DIMENSIONS = 3000 x 2000
```

## 3. Regla obligatoria de acceso al PNG — LOCAL FIRST / NO BASE64

Debes usar el checkout local del repositorio y leer directamente como binario:

```text
figures/group7/g7_thesis_fig_06_sensitivity.png
```

Antes de usarlo, calcula su SHA-256 y exige coincidencia exacta con:

```text
4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
```

### Prohibiciones explícitas

No uses GitHub como canal de transporte del PNG si el archivo local existe y su SHA-256 coincide.

Está prohibido:

- descargar o reconstruir el PNG mediante Base64;
- paginar Base64 por líneas o chunks;
- copiar fragmentos Base64 a archivos temporales;
- recuperar repetidamente el mismo PNG desde GitHub;
- regenerar el PNG desde SVG o renderer;
- sustituirlo por una imagen similar.

Si el PNG local no existe o su SHA-256 no coincide, reporta `STOPPED_PRECONDITION`. No recurras a Base64 como fallback.

GitHub puede usarse únicamente para leer textos/versiones/metadatos necesarios; no para transportar el binario PNG.

## 4. Alcance de edición

Ejecuta exclusivamente la integración A043 definida en el prompt original `121F_FIG6_INTEGRAR_FIGURA6_REVIEW_V03.md`.

Mantén el mismo contrato REVIEW V03 aplicado a Figuras 4 y 5:

1. conservar físicamente la Figura 6 legacy y su numeración oficial;
2. mantener visible el caption legacy, marcando únicamente el texto superseded según el contrato del prompt gobernante;
3. insertar una línea temporal de revisión resaltada en amarillo y estilo normal/no-caption;
4. insertar el PNG aprobado local verificado;
5. insertar el caption propuesto completo aprobado para tesis, resaltado en amarillo y sin crear un segundo `SEQ Figura`;
6. añadir exactamente un comentario Word nuevo, íntegramente en español y con los seis encabezados obligatorios;
7. añadir exactamente una fila nueva de trazabilidad para A043;
8. no modificar 4.1.5 ni ningún bloque posterior;
9. no ejecutar 121G.

El caption científico debe ser el aprobado por FIG012/FIG014 y conservar expresamente el carácter descriptivo/no causal, las 31 corridas, H100 como `n=1, referencia congelada`, la variación conjunta tamaño–composición, la ausencia de IC/valores p/regresiones/suavizados/resúmenes como marcas y el límite al benchmark interno.

No muestres `EXP11A`, G6, FIG015, prompts, commits, blobs, gates ni lenguaje de gobernanza en el texto visible de tesis.

## 5. Preservación estructural

Antes y después verifica como mínimo:

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

La imagen aprobada insertada debe conservar exactamente el SHA-256 gobernante cuando se compare el binario embebido en `word/media/`.

## 6. QA eficiente y localizado

No repitas análisis innecesarios de todo el documento.

Renderiza e inspecciona únicamente las páginas necesarias para cubrir:

- final de Tabla 15 / interpretación inmediata;
- Figura 6 legacy;
- línea temporal de revisión;
- Figura 6 candidata;
- caption completo propuesto;
- inicio de 4.1.5 como frontera posterior.

Verifica:

- no clipping;
- no deformación del PNG;
- proporción 3:2 preservada;
- caption legible;
- no solapamientos;
- Figura 6 legacy conservada;
- 4.1.5 intacta.

No cambies márgenes, secciones ni tamaño de página.

## 7. Salidas

No sobrescribas F. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F_FIG6_R1.docx
g7_thesis_claim_traceability_v0.3_F_FIG6_R1.csv
```

Publica la respuesta oficial en:

```text
writing_prompts_tmp/121F_FIG6_R1_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
```

La respuesta debe reportar SHA-256 y tamaño exactos de ambas salidas y terminar con:

```text
PROMPT121F_FIG6_R1_EXECUTION = COMPLETE | STOPPED_PRECONDITION
LOCAL_PNG_USED = true|false
BASE64_TRANSPORT_USED = false
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
