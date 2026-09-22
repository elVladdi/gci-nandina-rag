# D-032 — Exact Markdown author handoff for technical integration

```text
DECISION_ID = D-032
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
BLOCK = INTRODUCTION_B01
PURPOSE = RESOLVE_TECHNICAL_TRANSFER_ONLY
SCIENTIFIC_CONTENT = FROZEN / NO_REWRITE
AUTHOR_APPROVAL = PRESERVED
```

## 1. Motivo

La ejecución de cierre técnico posterior a la aprobación autoral recuperó correctamente los dos Markdown exactos de Introduction B01 V02 y verificó sus hashes, pero no pudo transferirlos a GitHub desde el filesystem local de la IA ejecutora.

La auditoría `article/reviews/3_INTRODUCTION_B01_TECHNICAL_CLOSURE_REVIEW_V01.md` clasifica el resultado como `VALID_STOP`: los artefactos no están perdidos y su identidad está confirmada; el único residuo es su salida de la sesión ejecutora.

## 2. Excepción técnica estrecha a D-022

Se autoriza exclusivamente que la IA ejecutora entregue al autor, como archivos adjuntos descargables en chat, los dos Markdown exactos ya existentes:

```text
Introduction_B01_V02.md
EXPECTED_SHA256 = 6dd7c5c27246a229f1c40cd5a49e73d13775c8f65c5d18b3d96a534a395942b4

ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md
EXPECTED_SHA256 = 3137efd44373adb6411d3bdb917cc78a575aa27fe858385509bb42c168061cdf
```

Esta excepción permite únicamente la transferencia de archivo como adjunto. No autoriza pegar el contenido completo en el chat, Base64, fragmentación, reserialización, normalización de line endings, reformateo ni reconstrucción.

## 3. Regla de identidad

Antes de adjuntar cada archivo, la IA ejecutora debe recalcular SHA-256. Solo puede entregarlo si coincide exactamente con el valor gobernante.

Después de la entrega, el autor deberá conservar los archivos exactos y podrá trasladarlos a la IA Gestora para completar la materialización GitHub.

## 4. Prohibiciones

Durante esta acción queda prohibido:

- editar o regenerar los Markdown;
- reconstruirlos desde DOCX o desde `ARTICLE_MASTER_V006.md`;
- modificar Introduction, Related Work o secciones posteriores;
- modificar el DOCX;
- promover `ARTICLE_MASTER_V007`;
- abrir Decision-support architecture;
- actualizar ARTICLE_STATUS o ARTICLE_WRITING_PLAN;
- ejecutar un nuevo análisis científico.

## 5. Gate posterior

Una entrega exitosa deja:

```text
EXACT_MARKDOWN_AUTHOR_HANDOFF = COMPLETED
INTRODUCTION_B01_V02 = APPROVED / FROZEN / READY_FOR_TECHNICAL_GITHUB_MATERIALIZATION
ARTICLE_MASTER_V007 = NOT_YET_PROMOTED
DECISION_SUPPORT_ARCHITECTURE = NOT_YET_AUTHORIZED
```

La IA Gestora verificará los archivos recibidos y decidirá la integración canónica.
