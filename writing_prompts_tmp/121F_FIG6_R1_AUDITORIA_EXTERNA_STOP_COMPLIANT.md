# PROMPT121F-FIG6-R1 — Auditoría externa de IA Experimental

## Dictamen

```text
PROMPT121F_FIG6_R1_EXTERNAL_AUDIT = PASS_STOPPED_PRECONDITION
STOP_COMPLIANT = true
EXECUTION_DEFECT = false
LOCAL_PNG_USED = false
BASE64_TRANSPORT_USED = false
A043_EXECUTED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Verificación independiente

Se auditó la respuesta oficial:

```text
writing_prompts_tmp/121F_FIG6_R1_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
@ 6c32047e0228439dbc35a913188a691109c45cd3
```

contra el prompt gobernante:

```text
writing_prompts_tmp/121F_FIG6_R1_REINTENTO_LOCAL_FIRST_SIN_BASE64.md
@ d683d19bcdfde7b30e829f1c6bda1c8b9a3ac25e
```

La ejecución verificó correctamente las entradas acumulativas gobernantes:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
SIZE = 4572575

g7_thesis_claim_traceability_v0.3_F.csv
SHA256 = 14d44b27012181bc943fa0325eb3c5964295ff040455ffe8c7c2b16f025eb337
ROWS = 103
```

El único bloqueo fue `LOCAL_PNG_MISSING` para:

```text
figures/group7/g7_thesis_fig_06_sensitivity.png
```

El prompt R1 ordenaba expresamente detenerse si el PNG no existía en el checkout local y prohibía usar Base64 o GitHub como fallback. La ejecución cumplió esa regla: no abrió el DOCX para edición, no modificó el CSV, no generó salidas, no ejecutó A043 y no ejecutó 121G.

## Diagnóstico del bloqueo

El bloqueo es de **materialización/sincronización del checkout local**, no de inexistencia del artefacto aprobado.

El repositorio remoto en el propio commit de respuesta `6c32047e0228439dbc35a913188a691109c45cd3` sí contiene:

```text
PATH = figures/group7/g7_thesis_fig_06_sensitivity.png
GIT_BLOB = 667765204adbdb7ab7567e9546f6ed8c71051d91
SIZE = 112767
APPROVED_SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
```

Ese binario fue creado y aprobado en FIG015. Por tanto, no corresponde regenerarlo ni transportarlo mediante Base64. La resolución correcta es permitir que la siguiente ejecución materialice el blob binario aprobado desde el repositorio Git local. Si el objeto no existe todavía en el clone local, se autoriza una única sincronización mediante transporte Git estándar de la rama, seguida de materialización local por `git cat-file`/`git show` y verificación SHA-256. No se autoriza GitHub API, web, Base64, paginación por chunks ni regeneración desde SVG.

## Consecuencia de gobernanza

Se autoriza un nuevo reintento localizado de A043 manteniendo a la **IA de Redacción Científica** como actor. La única ampliación operativa respecto de R1 será resolver la precondición del PNG mediante Git local verificado antes de editar el DOCX.

Hasta PASS externo de la integración:

```text
A043 = NOT_EXECUTED
121G_AUTHORIZED = false
G7_F03_AUTHORIZED = false
```
