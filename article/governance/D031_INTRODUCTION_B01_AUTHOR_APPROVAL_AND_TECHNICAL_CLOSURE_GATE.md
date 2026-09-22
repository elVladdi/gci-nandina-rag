# D-031 — Introduction B01 author approval and technical-closure gate

```text
DECISION_ID = D-031
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
BLOCK = INTRODUCTION_B01
APPROVED_REVISION = V02
AUTHOR_APPROVAL = RECEIVED
SCIENTIFIC_CONTENT = APPROVED / FROZEN
DOCX_CANDIDATE = APPROVED
DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
CITATION_COMMENT_COUNT = 40
GITHUB_MARKDOWN_TRANSFER = PENDING_TECHNICAL_CLOSURE
CANONICAL_MASTER_PROMOTION = BLOCKED_ONLY_BY_TECHNICAL_CLOSURE
NEXT_SCIENTIFIC_BLOCK = NOT_AUTHORIZED_UNTIL_CLOSURE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Motivo

La IA Gestora auditó `Introduction B01 V02` y emitió `PASS`. El autor aprobó expresamente esa versión el 22 de septiembre de 2026.

El único residuo pendiente es técnico: durante la ejecución V04 no pudieron quedar referenciados en GitHub los dos Markdown científicos que ya habían sido generados localmente. Este residuo no afecta la aprobación científica del contenido ni el DOCX entregado.

## 2. Artefactos gobernantes

- revisión interna: `article/reviews/3_INTRODUCTION_B01_INTERNAL_REVIEW_V02.md@c611712b329f97c9d66b547cee8f469b0ab4f007`;
- aprobación del autor: `article/reviews/3_INTRODUCTION_B01_AUTHOR_APPROVAL_V01.md`;
- respuesta V04: `article/responses/3_INTRODUCTION_B01_RESPONSE_V04.md@d1057e570e3d43f69f5707f859ad5e6aac834ca8`;
- DOCX aprobado: `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx`;
- SHA-256 DOCX aprobado: `d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c`.

Los Markdown reportados por la ejecución V04 son:

```text
SECTION_MD = article/sections/introduction/Introduction_B01_V02.md
SECTION_MD_EXPECTED_SHA256 = 6dd7c5c27246a229f1c40cd5a49e73d13775c8f65c5d18b3d96a534a395942b4
MASTER_CANDIDATE_MD = article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md
MASTER_CANDIDATE_MD_EXPECTED_SHA256 = 3137efd44373adb6411d3bdb917cc78a575aa27fe858385509bb42c168061cdf
```

## 3. Freeze científico

Desde esta decisión, la Introduction V02 aprobada queda congelada. El cierre técnico no puede:

- reescribir, resumir, ampliar o estilizar la Introduction;
- añadir o eliminar citas;
- modificar RQ1–RQ4;
- cambiar las tres contribuciones;
- cambiar el alcance del testbed;
- modificar Related Work 2.1–2.6;
- modificar secciones posteriores;
- declarar novelty, SOTA o universal absence.

El cierre técnico solo puede materializar en GitHub los archivos Markdown ya aprobados y comprobar su identidad.

## 4. Regla de identidad de los Markdown

La primera opción obligatoria es recuperar los dos archivos locales exactos generados durante V02 y verificar sus SHA-256 contra los valores reportados en V04.

Si ambos hashes coinciden, pueden versionarse sin nueva revisión científica.

Si uno o ambos archivos exactos ya no están disponibles, la IA ejecutora **debe detenerse**. No puede reconstruirlos silenciosamente desde el DOCX o desde `ARTICLE_MASTER_V006.md`, porque una reconstrucción sería un nuevo artefacto binario/textual y requeriría autorización de la IA Gestora con trazabilidad explícita.

## 5. Integración canónica

Solo después de un cierre técnico exitoso:

1. `Introduction_B01_V02.md` podrá declararse `APPROVED / FROZEN / INTEGRATED`;
2. `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md` podrá promoverse, sin cambio científico, a `ARTICLE_MASTER_V007.md`;
3. el DOCX aprobado V02 pasará a ser el nuevo baseline acumulativo bajo custodia del autor;
4. `CANONICAL_CITATION_COMMENTS` pasará de 36 a 40;
5. la IA Gestora actualizará `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md`;
6. solo entonces podrá decidirse la apertura de `Decision-support architecture`.

## 6. Gate vigente

```text
CURRENT_GATE = INTRODUCTION_B01_TECHNICAL_CLOSURE
INTRODUCTION_B01_V02 = APPROVED / FROZEN / PENDING_TECHNICAL_INTEGRATION
NEXT_ACTOR = DRAFTING_AI / TECHNICAL_CLOSURE_ONLY
ARTICLE_MASTER_V007 = NOT_YET_AUTHORIZED_FOR_PROMOTION
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
