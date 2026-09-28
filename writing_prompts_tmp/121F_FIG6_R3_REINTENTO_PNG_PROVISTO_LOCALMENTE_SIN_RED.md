# PROMPT121F-FIG6-R3 — Reintento localizado con PNG aprobado provisto localmente, sin red

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No regeneres la Figura 6, no recalcules datos y no ejecutes 121G.

Lee íntegramente antes de ejecutar:

```text
writing_prompts_tmp/121F_FIG6_R2_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
@ b0082bda12c3fd41c991492efb6df5ca2e724529

writing_prompts_tmp/121F_FIG6_R2_AUDITORIA_EXTERNA_STOP_COMPLIANT.md
@ b7899aa9552464c5e119ed1217676e8362a493ef

figure_prompts_tmp/FIG015_AUDITORIA_EXTERNA_PASS.md
@ 4b916b6b2909fde6216654843aebdedcf2115cc3

writing_prompts_tmp/121F_FIG6_INTEGRAR_FIGURA6_REVIEW_V03.md
@ 67876fa408637051e07eb709a61d119ad9bf3745
```

Estado vinculante:

```text
PROMPT121F_FIG6_R2_EXTERNAL_AUDIT = PASS_STOPPED_PRECONDITION
FIG015_EXTERNAL_AUDIT = PASS
FIGURE_6_CANDIDATE_APPROVED_FOR_DOCX_INTEGRATION = true
A043_EXECUTED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
```

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

## 2. Figura 6 gobernante

```text
CANONICAL_FILENAME = g7_thesis_fig_06_sensitivity.png
EXPECTED_GIT_BLOB = 667765204adbdb7ab7567e9546f6ed8c71051d91
EXPECTED_SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
EXPECTED_SIZE = 112767
EXPECTED_DIMENSIONS = 3000 x 2000
```

La copia binaria aprobada debe haber sido **materializada localmente por el operador/usuario antes de iniciar esta ejecución**.

Busca únicamente, en este orden:

```text
figures/group7/g7_thesis_fig_06_sensitivity.png
./g7_thesis_fig_06_sensitivity.png
/mnt/data/g7_thesis_fig_06_sensitivity.png
```

Puedes aceptar otra ruta local únicamente si el archivo fue proporcionado explícitamente como attachment/input local de esta ejecución y su nombre corresponde inequívocamente a la Figura 6 aprobada.

## 3. Regla absoluta: SIN RED / SIN TRANSPORTE

Esta ejecución no debe intentar materializar el PNG desde ningún servicio remoto.

Está prohibido:

- `git fetch`, `git pull`, `git clone` o cualquier sincronización de red;
- GitHub API para transportar el PNG;
- Base64;
- URL raw/web;
- reconstrucción por chunks o fragmentos;
- regeneración desde SVG o renderer;
- captura de pantalla o imagen similar.

La única operación permitida sobre el PNG antes de integrarlo es lectura binaria local y validación.

Calcula SHA-256, tamaño y dimensiones. Deben coincidir exactamente con los valores gobernantes. Si no existe una copia local válida, termina inmediatamente:

```text
PROMPT121F_FIG6_R3_EXECUTION = STOPPED_PRECONDITION
TERMINAL_REASON = OPERATOR_PROVIDED_APPROVED_PNG_NOT_AVAILABLE
```

## 4. Alcance único tras superar la precondición

Si y solo si el PNG local coincide exactamente, ejecuta **A043** con el mismo contrato editorial y científico del prompt original:

```text
writing_prompts_tmp/121F_FIG6_INTEGRAR_FIGURA6_REVIEW_V03.md
@ 67876fa408637051e07eb709a61d119ad9bf3745
```

No amplíes alcance ni reinterpretes ese contrato.

En particular:

- conserva físicamente la Figura 6 legacy y su numeración oficial;
- conserva visible su caption legacy con el marcado de revisión gobernante;
- inserta la línea temporal de revisión gobernante;
- inserta el PNG aprobado verificado;
- inserta el caption propuesto completo aprobado, sin segundo `SEQ Figura`;
- añade exactamente un comentario Word nuevo en español con los seis encabezados obligatorios;
- añade exactamente una fila nueva de trazabilidad para A043;
- no modifiques 4.1.5 ni ningún bloque posterior;
- no ejecutes 121G.

## 5. Invariantes estructurales

Después de una ejecución completa deben cumplirse:

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

El binario embebido en `word/media/` debe conservar exactamente:

```text
SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
```

## 6. QA localizado

Renderiza e inspecciona únicamente las páginas necesarias para cubrir:

- final de Tabla 15 / interpretación inmediata;
- Figura 6 legacy;
- línea temporal de revisión;
- Figura 6 candidata;
- caption completo propuesto;
- inicio de 4.1.5.

Verifica no clipping, no deformación, proporción 3:2, caption legible, ausencia de solapamientos, legacy preservada y 4.1.5 intacta.

No cambies márgenes, secciones ni tamaño de página.

## 7. Salidas

No sobrescribas F. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F_FIG6_R3.docx
g7_thesis_claim_traceability_v0.3_F_FIG6_R3.csv
```

Publica la respuesta oficial en:

```text
writing_prompts_tmp/121F_FIG6_R3_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
```

Termina con:

```text
PROMPT121F_FIG6_R3_EXECUTION = COMPLETE | STOPPED_PRECONDITION
PNG_SOURCE_MODE = OPERATOR_PROVIDED_LOCAL | NONE
NETWORK_ACCESS_USED = false
BASE64_TRANSPORT_USED = false
GITHUB_API_PNG_TRANSPORT_USED = false
FIGURE_6_LOCAL_PNG_SHA256_MATCH = true|false
FIGURE_6_LOCAL_PNG_SIZE_MATCH = true|false
FIGURE_6_LOCAL_PNG_DIMENSIONS_MATCH = true|false
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
