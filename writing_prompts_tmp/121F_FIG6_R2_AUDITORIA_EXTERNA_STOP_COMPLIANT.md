# PROMPT121F-FIG6-R2 — Auditoría externa de IA Experimental

## Dictamen

```text
PROMPT121F_FIG6_R2_EXTERNAL_AUDIT = PASS_STOPPED_PRECONDITION
STOP_COMPLIANT = true
EXECUTION_DEFECT = false
PNG_SOURCE_MODE = NONE
GIT_FETCH_USED = true
BASE64_TRANSPORT_USED = false
GITHUB_API_PNG_TRANSPORT_USED = false
A043_EXECUTED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Verificación independiente

Se auditó la respuesta oficial:

```text
writing_prompts_tmp/121F_FIG6_R2_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
@ b0082bda12c3fd41c991492efb6df5ca2e724529
```

contra el prompt R2 gobernante y los antecedentes FIG015/R1.

La ejecución verificó correctamente las entradas acumulativas autorizadas:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
SIZE = 4572575

g7_thesis_claim_traceability_v0.3_F.csv
SHA256 = 14d44b27012181bc943fa0325eb3c5964295ff040455ffe8c7c2b16f025eb337
ROWS = 103
```

El único bloqueo fue la imposibilidad de materializar el blob aprobado después de la única sincronización Git estándar autorizada:

```text
fatal: unable to access 'https://github.com/elVladdi/gci-nandina-rag.git/': Could not resolve host: github.com
```

La respuesta respetó el contrato: no repitió `git fetch`, no usó GitHub API para transportar el PNG, no usó Base64, URL raw/web ni regeneración desde SVG/renderer; no abrió el DOCX para edición, no modificó el CSV y no produjo salidas R2.

## Existencia remota del artefacto

La precondición fallida no implica ausencia del artefacto aprobado. El repositorio remoto en el estado auditado contiene:

```text
figures/group7/g7_thesis_fig_06_sensitivity.png
GIT_BLOB = 667765204adbdb7ab7567e9546f6ed8c71051d91
SIZE = 112767
APPROVED_SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
```

El fallo es de conectividad/materialización del entorno de ejecución, no científico ni de identidad de la figura.

## Consecuencia de gobernanza

No corresponde un nuevo intento de red ni un retorno a Base64. El siguiente intento de A043 deberá usar exclusivamente una copia del PNG aprobada y materializada fuera de la ejecución automatizada, colocada localmente por el operador/usuario antes de iniciar. La ejecución solo podrá verificar su SHA-256 y, si coincide, integrar A043. Si el archivo no está presente o el hash difiere, deberá detenerse.

Se mantiene como actor la **IA de Redacción Científica**. No corresponde CODEX para decidir o reinterpretar contenido editorial.

Hasta PASS externo de la integración:

```text
A043 = NOT_EXECUTED
121G_AUTHORIZED = false
G7_F03_AUTHORIZED = false
```
