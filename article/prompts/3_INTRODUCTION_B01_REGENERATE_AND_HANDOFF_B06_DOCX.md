# Introduction B01 — Regeneración controlada y entrega del DOCX B06

## 1. Propósito

Ejecuta exclusivamente la recuperación técnica autorizada por D-028 para regenerar el DOCX acumulativo B06 perdido y entregarlo efectivamente al autor.

NO redactes Introduction. NO modifiques contenido científico aprobado. NO abras Decision-support architecture ni ninguna sección posterior.

Esta tarea existe únicamente porque la recuperación del binario B06 original falló en:

`article/responses/3_INTRODUCTION_B01_B06_DOCX_RECOVERY_RESPONSE_V01.md@7d766844006f3ecd4d2603fcfa2af867bc3247d6`

Aplica obligatoriamente:

- `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
- `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`;
- `article/governance/D028_CONTROLLED_REGENERATION_OF_LOST_B06_DOCX.md@6e5c3aaa9de3892e8e5a20f53cbd63ed0512185b`;
- `article/responses/2_RELATED_WORK_B06_RESPONSE_V01.md@f8756f5ed6ebed98a567186035082db96b618032`;
- `article/reviews/2_RELATED_WORK_B06_INTERNAL_REVIEW_V02.md`;
- `article/sections/related_work/RelatedWork_B06_V01.md`;
- `article/manuscript/ARTICLE_MASTER_V006.md`.

## 2. Baseline DOCX obligatorio

Localiza el DOCX B05 aprobado disponible en la sesión y verifica ANTES de editar:

```text
BASELINE = ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx OR BYTE_IDENTICAL_LOCAL_RENAME
REQUIRED_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a
EXPECTED_INHERITED_COMMENTS = 32
EXPECTED_TRACKED_CHANGES = 0
```

Si el SHA-256 no coincide exactamente, detente y versiona únicamente la respuesta de fallo. No intentes usar otro DOCX ni reconstruir B05.

## 3. Fuente canónica del contenido B06

El contenido científico NO debe volver a redactarse.

Usa exactamente la Section 2.6 ya aprobada y congelada, contenida en:

- `article/sections/related_work/RelatedWork_B06_V01.md`;
- `article/manuscript/ARTICLE_MASTER_V006.md`;
- Git blob canónico `7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`.

Inserta exclusivamente B06 en su ubicación correspondiente de Part I English y Part II Spanish semantic-control mirror.

Sections 2.1–2.5 deben permanecer idénticas al baseline B05. No corrijas estilo, redacción, referencias, puntuación ni formato fuera de B06.

## 4. Reconstrucción de comentarios B06

Preserva los 32 comentarios heredados del baseline B05.

Recrea únicamente cuatro comentarios nuevos, uno por cada cita inglesa de B06. Para cada comentario:

1. reabre la fuente primaria;
2. verifica nuevamente el pasaje exacto que respalda el claim de B06;
3. ancla el comentario a la cita inglesa pertinente;
4. incluye evidencia verificable suficiente para auditoría, siguiendo el patrón acumulativo de comentarios del documento.

Fuentes primarias que deben verificarse:

- Lee et al. (2021), `Classification of Goods Using Text Descriptions With Sentences Retrieval`;
- Lee et al. (2023), `Explainable Product Classification for Customs`;
- Wang et al. (2026), `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification`, arXiv:2607.10588;
- Chen and Tanaka-Ishii (2026), `Executable explanation traces for legal LLM predictions via retrieval-augmented codification`, DOI `10.3389/frai.2026.1905145`.

Los comentarios recreados deben ser semánticamente adecuados y trazables. NO afirmes que son byte-for-byte idénticos a los comentarios perdidos.

## 5. Identidad del DOCX regenerado

Guarda el archivo local como:

`ARTICLE_MASTER_B06_REGENERATED_V01.docx`

El binario original perdido tenía SHA-256:

`3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0`

Ese hash se conserva solo como identidad histórica del binario perdido. Calcula un NUEVO SHA-256 para el archivo regenerado y regístralo como:

`REGENERATED_B06_DOCX_SHA256 = <sha256>`

No intentes manipular metadatos para reproducir el hash original.

## 6. QA obligatorio

Antes de entregar el archivo verifica expresamente:

```text
BASELINE_B05_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a / PASS
PRIOR_COMMENTS_PRESERVED = 32/32
B06_NEW_COMMENTS = 4
TOTAL_COMMENTS = 36
SECTIONS_2_1_TO_2_5_PRESERVED = PASS
B06_APPROVED_TEXT_PRESERVED_EN = PASS
B06_APPROVED_TEXT_PRESERVED_ES = PASS
B06_CITATION_COMMENT_COVERAGE = 4/4
TRACKED_CHANGES = 0
OOXML_INTEGRITY = PASS
RENDER = PASS / <N>_OF_<N>_PAGES
INTRODUCTION_DRAFTING = NOT_STARTED
LATER_SECTIONS_MODIFIED = NO
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Inspecciona el render completo y confirma ausencia de clipping, solapamiento, páginas truncadas o pérdida de contenido.

## 7. Entrega efectiva al autor

Después del QA, entrega `ARTICLE_MASTER_B06_REGENERATED_V01.docx` al autor como archivo descargable/adjunto en el chat.

Solo después de que el archivo haya sido efectivamente expuesto al autor mediante el mecanismo de descarga puedes registrar:

```text
AUTHOR_HANDOFF = COMPLETED
AUTHOR_CUSTODY = ESTABLISHED_FOR_REGENERATED_BINARY
```

Si la interfaz no permite exponer el archivo descargable, registra `AUTHOR_HANDOFF = FAILED` y detente. No continúes con Introduction.

## 8. Respuesta versionada en GitHub

Genera exclusivamente:

`article/responses/3_INTRODUCTION_B01_B06_DOCX_REGENERATION_RESPONSE_V01.md`

La respuesta debe registrar:

- baseline B05 y SHA-256 verificado;
- fuentes canónicas usadas para B06;
- preservación 32/32 comentarios;
- reconstrucción de 4/4 comentarios B06;
- total 36 comentarios;
- QA OOXML/render/tracked changes;
- nuevo SHA-256 del DOCX regenerado;
- estado real de `AUTHOR_HANDOFF`;
- confirmación de que Introduction no fue redactada;
- confirmación de que el binario original B06 sigue clasificado como perdido y no fue sustituido silenciosamente.

Crea un único commit semántico que añada exclusivamente esa respuesta Markdown. NO subas el DOCX a GitHub salvo instrucción posterior expresa.

## 9. Respuesta en chat

Si la regeneración y entrega al autor son exitosas, el chat puede contener, por excepción D-027:

1. el archivo descargable `ARTICLE_MASTER_B06_REGENERATED_V01.docx`;
2. únicamente el puntero:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/3_INTRODUCTION_B01_B06_DOCX_REGENERATION_RESPONSE_V01.md@<commit_sha>`

Después, detente.

Si la regeneración o la entrega falla, responde únicamente con el puntero GitHub correspondiente y detente.

Introduction B01 NO se reanuda dentro de esta ejecución.
