# Introduction B01 — Handoff de los Markdown exactos recuperados

## 1. Objetivo único

Entrega al autor, como archivos adjuntos descargables en chat, los dos Markdown exactos de `Introduction B01 V02` que ya recuperaste y verificaste en la ejecución anterior.

No redactes, no reconstruyas y no modifiques contenido científico.

## 2. Gobernanza obligatoria

Aplica:

- `article/governance/D031_INTRODUCTION_B01_AUTHOR_APPROVAL_AND_TECHNICAL_CLOSURE_GATE.md`;
- `article/governance/D032_EXACT_MARKDOWN_AUTHOR_HANDOFF_FOR_TECHNICAL_INTEGRATION.md`;
- `article/reviews/3_INTRODUCTION_B01_TECHNICAL_CLOSURE_REVIEW_V01.md`;
- `article/responses/3_INTRODUCTION_B01_TECHNICAL_CLOSURE_RESPONSE_V01.md@0e65c4e443afccfbf5acaa2a004956dd1bb71576`.

## 3. Archivos gobernantes

Los archivos locales exactos declarados por la ejecución anterior son:

```text
/mnt/data/Introduction_B01_V02.md
EXPECTED_SHA256 = 6dd7c5c27246a229f1c40cd5a49e73d13775c8f65c5d18b3d96a534a395942b4

/mnt/data/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md
EXPECTED_SHA256 = 3137efd44373adb6411d3bdb917cc78a575aa27fe858385509bb42c168061cdf
```

Recalcula SHA-256 inmediatamente antes de la entrega.

## 4. Condición de éxito

Solo si ambos hashes coinciden exactamente:

1. adjunta `Introduction_B01_V02.md` como archivo descargable;
2. adjunta `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md` como archivo descargable;
3. no cambies nombre, bytes, encoding, line endings ni newline final;
4. no pegues su contenido completo en el chat;
5. no uses Base64 ni fragmentación.

## 5. Registro GitHub

Después de la entrega efectiva crea únicamente:

`article/responses/3_INTRODUCTION_B01_EXACT_MARKDOWN_HANDOFF_RESPONSE_V01.md`

con:

```text
BLOCK = INTRODUCTION_B01
TASK = EXACT_MARKDOWN_AUTHOR_HANDOFF
SECTION_MD_SHA256 = 6dd7c5c27246a229f1c40cd5a49e73d13775c8f65c5d18b3d96a534a395942b4
SECTION_MD_IDENTITY = PASS
MASTER_CANDIDATE_MD_SHA256 = 3137efd44373adb6411d3bdb917cc78a575aa27fe858385509bb42c168061cdf
MASTER_CANDIDATE_MD_IDENTITY = PASS
AUTHOR_HANDOFF_SECTION_MD = COMPLETED
AUTHOR_HANDOFF_MASTER_CANDIDATE_MD = COMPLETED
SCIENTIFIC_CONTENT_MODIFIED = NO
RECONSTRUCTION_ATTEMPTED = NO
ARTICLE_MASTER_V007 = NOT_PROMOTED
DECISION_SUPPORT_ARCHITECTURE = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El commit debe añadir exclusivamente esa respuesta. Los Markdown no se suben a GitHub en esta ejecución.

## 6. Stop condition

Si alguno de los archivos ya no existe o su hash no coincide:

- no reconstruyas;
- no sustituyas;
- no generes una nueva versión;
- no entregues un archivo no idéntico;
- registra únicamente una respuesta de blocker con `EXACT_MARKDOWN_HANDOFF = FAIL` y detente.

## 7. Prohibiciones

No modificar DOCX, Introduction, Related Work, Architecture, status, plan, governance ni ningún otro artefacto científico.

## 8. Respuesta final de chat

Después de adjuntar efectivamente ambos archivos y versionar la respuesta, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/3_INTRODUCTION_B01_EXACT_MARKDOWN_HANDOFF_RESPONSE_V01.md@<commit_sha>`

Los dos adjuntos deben estar disponibles en el mismo mensaje o inmediatamente antes de ese puntero.
