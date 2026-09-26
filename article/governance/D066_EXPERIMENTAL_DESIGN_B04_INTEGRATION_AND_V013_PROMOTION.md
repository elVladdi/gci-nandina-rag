# D-066 — Experimental Design B04 integration and ARTICLE_MASTER_V013 promotion

## Español

```text
DECISION_ID = D-066
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-065
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
AUTHOR_APPROVAL = RECEIVED
B04_V02_DIFFERENTIAL_AUDIT = PASS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
SECTION_4_6 = ELIGIBLE_FOR_GROUND_TRUTH_SYNC / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Verificación de materialización

El autor materializó `article/manuscript/ARTICLE_MASTER_V013.md` después de la aprobación expresa de B04 V02.

La IA Gestora verificó directamente en GitHub:

- Git blob esperado del candidato aprobado: `06beaa052e2f1bcc630647040762fe78d3838a62`;
- Git blob observado de `ARTICLE_MASTER_V013.md`: `06beaa052e2f1bcc630647040762fe78d3838a62`.

La coincidencia del blob confirma materialización byte-exacta del candidato Markdown B04 V02 aprobado. No hubo reconstrucción, normalización o reescritura durante la promoción.

### 2. Cierre de B04

Quedan integrados y congelados:

- `article/sections/experimental_design/Experimental_Design_B04_V02.md`;
- Section 4.5 en inglés y español;
- `article/manuscript/ARTICLE_MASTER_V013.md` como master Markdown canónico;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx` como baseline Word acumulativo bajo custodia local del autor.

El DOCX conserva la identidad ya auditada: SHA-256 `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`, 40 comentarios/anclajes y cero tracked changes.

### 3. Gate posterior

La siguiente sección científica según la estructura congelada es Section 4.6 `Evaluation framework and protocols`, con 4.6.1 candidate-retrieval evaluation, 4.6.2 documentary-evidence evaluation y 4.6.3 controlled-explanation evaluation.

Su redacción no queda autorizada por la sola promoción de V013. Primero la IA Gestora debe sincronizar las fuentes experimentales vivas y congeladas que gobiernan métricas, unidades de evaluación, protocolos y límites interpretativos, y emitir un prompt atómico específico.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_GROUND_TRUTH_SYNC_AND_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
ARTICLE_MASTER_V013 = CANONICAL / VERIFIED
SECTION_4_6 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-066
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-065
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
AUTHOR_APPROVAL = RECEIVED
B04_V02_DIFFERENTIAL_AUDIT = PASS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
SECTION_4_6 = ELIGIBLE_FOR_GROUND_TRUTH_SYNC / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The author materialized `article/manuscript/ARTICLE_MASTER_V013.md` after express approval of B04 V02. The Managing AI directly verified that the observed Git blob `06beaa052e2f1bcc630647040762fe78d3838a62` exactly matches the frozen expected blob. Therefore the promotion is byte-exact and B04/Section 4.5 is closed, approved, frozen, and integrated.

`ARTICLE_MASTER_V013.md` is now the canonical Markdown master. The approved cumulative Word baseline is `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx`, SHA-256 `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`, in local author custody, with 40 inherited citation comments and zero tracked changes.

Section 4.6 is the next scientific section but is not opened automatically. A Managing-AI ground-truth synchronization and an atomic B05 prompt are required before drafting.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_GROUND_TRUTH_SYNC_AND_PROMPT_PREPARATION
NEXT_ACTOR = MANAGING_AI
ARTICLE_MASTER_V013 = CANONICAL / VERIFIED
SECTION_4_6 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```