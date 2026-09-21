# Introduction B01 — Recuperación y entrega del DOCX B06 al autor

## 1. Propósito exclusivo

NO redactes Introduction todavía.

Ejecuta exclusivamente la recuperación del DOCX exacto generado durante `RELATED_WORK_B06_V01` y entrégalo efectivamente al autor conforme a D-027.

Este prompt existe porque el binario B06 fue reportado como generado, pero nunca fue transferido al autor. No abras ningún bloque científico nuevo.

## 2. Fuente de verdad del binario

La ejecución B06 reportó:

```text
FILE = ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx
EXPECTED_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0
EXPECTED_COMMENTS = 36
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_RENDER = 28/28 PASS
```

Consulta:

- `article/responses/2_RELATED_WORK_B06_RESPONSE_V01.md@f8756f5ed6ebed98a567186035082db96b618032`
- `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`
- `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`

## 3. Procedimiento obligatorio

1. Busca en el filesystem/sesión local activa el archivo exacto generado durante B06.
2. NO uses el DOCX B05 como sustituto.
3. NO reconstruyas el DOCX desde Markdown.
4. NO vuelvas a guardar el archivo en Word ni lo modifiques de ninguna forma antes de verificar su hash.
5. Calcula SHA-256.
6. Solo si el SHA-256 es exactamente:

`3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0`

continúa con la entrega.
7. Copia el binario exacto, sin modificación, a una ruta descargable de la sesión (por ejemplo `/mnt/data/ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx`) únicamente si esa copia preserva bytes.
8. Verifica nuevamente el SHA-256 de la copia entregable.
9. Entrega el archivo al autor mediante enlace/adjunto descargable en chat.

## 4. Si el archivo exacto está disponible

Versiona en GitHub:

`article/responses/3_INTRODUCTION_B01_B06_DOCX_RECOVERY_RESPONSE_V01.md`

con al menos:

```text
RECOVERY_RESULT = PASS
RECOVERED_FILE = ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx
RECOVERED_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e4f8c752d84bf0
BYTE_IDENTITY = PASS
AUTHOR_HANDOFF = COMPLETED
SCIENTIFIC_CONTENT_MODIFIED = NO
INTRODUCTION_DRAFTING = NOT_STARTED
```

En chat, D-027 permite excepcionalmente mostrar:

1. el enlace/adjunto al DOCX recuperado; y
2. el puntero mínimo GitHub de la respuesta.

Después, detente. NO ejecutes todavía Introduction B01.

## 5. Si el archivo exacto NO está disponible

No intentes recrearlo.

Versiona únicamente:

`article/responses/3_INTRODUCTION_B01_B06_DOCX_RECOVERY_RESPONSE_V01.md`

con:

```text
RECOVERY_RESULT = FAIL
STOP_CONDITION = DOCX_CUSTODY_RECOVERY_FAILED
EXPECTED_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0
AUTHOR_HANDOFF = NOT_COMPLETED
RECONSTRUCTION_ATTEMPTED = NO
INTRODUCTION_DRAFTING = NOT_STARTED
```

En chat responde únicamente con el puntero GitHub correspondiente y detente. La IA Gestora decidirá si procede una regeneración controlada con nueva identidad binaria.

## 6. Prohibiciones

- No redactar Introduction.
- No modificar Markdown científico.
- No modificar masters canónicos.
- No abrir Decision-support architecture ni secciones posteriores.
- No regenerar el Word.
- No sustituir el B06 por B05.
- No declarar `AUTHOR_HANDOFF = COMPLETED` sin haber entregado efectivamente el archivo descargable al autor.
