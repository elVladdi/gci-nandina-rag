# D-065 — Experimental Design B04 author approval and ARTICLE_MASTER_V013 authorization

## Español

```text
DECISION_ID = D-065
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-064
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
SECTION = 4.5 Experimental system configuration and execution
B04_V02_DIFFERENTIAL_AUDIT = PASS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_5 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
BASELINE_CANONICAL_MASTER = ARTICLE_MASTER_V012
APPROVED_B04_SECTION = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
APPROVED_B04_SECTION_GIT_BLOB = fa6e9325a5acd6bf480cdbe90a467855cf877f1d
APPROVED_B04_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md
APPROVED_B04_CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
APPROVED_B04_CANDIDATE_MD_GIT_BLOB_EXPECTED = 06beaa052e2f1bcc630647040762fe78d3838a62
APPROVED_B04_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_B04_CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V013
TARGET_CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Base de la decisión

B04 V02 superó la auditoría diferencial independiente registrada en `article/reviews/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01.md@1cb3e2c865d44bbffb2481185ded6df8bf9abc54`. La revisión verificó que las únicas diferencias respecto de B04 V01 son las cuatro sustituciones EN/ES autorizadas por D-063, que el DOCX conserva 40 comentarios/anclajes heredados y cero tracked changes, y que la variación de 44 a 45 páginas se debe exclusivamente a reflujo de layout.

El autor aprobó expresamente B04 V02 después de la apertura formal del `AUTHOR_APPROVAL_GATE` mediante D-064. La aprobación autoral queda registrada como gate independiente del PASS técnico/editorial.

## 2. Congelamiento

Quedan congelados:

- `article/sections/experimental_design/Experimental_Design_B04_V02.md`;
- el contenido científico aprobado de Section 4.5 en inglés y español;
- el candidato Markdown acumulativo con SHA-256 `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43` y Git blob esperado `06beaa052e2f1bcc630647040762fe78d3838a62`;
- el candidato DOCX acumulativo con SHA-256 `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`.

No se autoriza ninguna reescritura de Section 4.5 durante la promoción.

## 3. Promoción autorizada

Se autoriza materializar los bytes exactos del candidato Markdown B04 V02 aprobado como:

`article/manuscript/ARTICLE_MASTER_V013.md`

La promoción es exclusivamente técnica y debe verificarse contra:

- SHA-256: `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43`;
- Git blob esperado: `06beaa052e2f1bcc630647040762fe78d3838a62`.

No está permitido reconstruir, normalizar, remaquetar o reescribir el candidato durante la promoción. Si los bytes exactos no están materializados en GitHub, `ARTICLE_MASTER_V012` continúa siendo canónico hasta cerrar este gate técnico.

El DOCX aprobado permanece bajo custodia local del autor conforme a D-021/D-027 y se convierte en el baseline Word acumulativo que deberá gobernar B05 una vez cerrada la promoción V013.

## 4. Gate posterior

Section 4.6 no queda autorizada por la sola aprobación autoral. Primero debe materializarse y verificarse `ARTICLE_MASTER_V013.md`, eliminarse el drift operativo aún presente en `ARTICLE_WRITING_PLAN.md`, y reconstruirse el ground truth experimental vivo pertinente a los protocolos de evaluación antes de emitir un nuevo prompt atómico.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V013_CANONICAL_INTEGRATION
NEXT_ACTOR = IA_GESTORA / TECHNICAL_INTEGRATION_ONLY
ARTICLE_MASTER_V013 = AUTHORIZED / NOT_YET_VERIFIED_AS_MATERIALIZED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_5 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_6 = ELIGIBLE_AFTER_V013_INTEGRATION_AND_GROUND_TRUTH_SYNC / NOT_AUTHORIZED
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

```text
DECISION_ID = D-065
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-064
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
B04_V02_DIFFERENTIAL_AUDIT = PASS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_5 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
BASELINE_CANONICAL_MASTER = ARTICLE_MASTER_V012
APPROVED_B04_SECTION = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
APPROVED_B04_CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
APPROVED_B04_CANDIDATE_MD_GIT_BLOB_EXPECTED = 06beaa052e2f1bcc630647040762fe78d3838a62
APPROVED_B04_CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V013
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

B04 V02 passed independent differential review and then received express author approval. Section 4.5 and the exact cumulative Markdown/DOCX candidates are therefore frozen and ready for integration. Exact-byte materialization of the approved Markdown candidate as `article/manuscript/ARTICLE_MASTER_V013.md` is authorized, subject to SHA-256 `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43` and expected Git blob `06beaa052e2f1bcc630647040762fe78d3838a62`. Section 4.6 remains unauthorized until V013 integration, writing-plan synchronization, and relevant live experimental-ground-truth reconstruction are complete.