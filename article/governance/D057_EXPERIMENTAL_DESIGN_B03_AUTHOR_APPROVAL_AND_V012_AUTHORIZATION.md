# D-057 — Experimental Design B03 author approval and ARTICLE_MASTER_V012 authorization

```text
DECISION_ID = D-057
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B03
SECTION = 4.4 Partition validity and dependence controls
SCIENTIFIC_REVIEW = PASS
DOCX_COMPLETION_REVIEW = PASS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_4 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
BASELINE_CANONICAL_MASTER = ARTICLE_MASTER_V011
BASELINE_CANONICAL_MASTER_MD_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
APPROVED_B03_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.md
APPROVED_B03_CANDIDATE_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
APPROVED_B03_CANDIDATE_MD_GIT_BLOB_EXPECTED = dfea73f5f462fc65cf98347f796deadc6da58455
APPROVED_B03_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_B03_CANDIDATE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V012
TARGET_CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Base de la decisión

Experimental Design B03 V01 superó la auditoría científica independiente registrada en `article/reviews/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4_INTERNAL_REVIEW_V01.md`. La única incidencia detectada fue la continuidad DOCX, cerrada mediante el microgate técnico `5_EXPERIMENTAL_DESIGN_B03_DOCX_COMPLETION_V01` y la revisión independiente `article/reviews/5_EXPERIMENTAL_DESIGN_B03_DOCX_COMPLETION_INTERNAL_REVIEW_V01.md`.

La revisión técnica verificó directamente el candidato Word acumulativo `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`, SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`, con integridad OOXML, 40 comentarios y anclajes preservados, tracked changes = 0, Section 4.4 EN/ES presente y frontera con 4.5 preservada.

El autor aprobó expresamente B03 después de la apertura formal del `AUTHOR_APPROVAL_GATE`. Esa aprobación no se presume ni se deriva del PASS técnico: queda registrada como decisión autoral independiente.

## 2. Congelamiento

Quedan congelados:

- `article/sections/experimental_design/Experimental_Design_B03_V01.md`;
- el contenido científico aprobado de Section 4.4 en inglés y español;
- el candidato Markdown acumulativo identificado por SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`;
- el candidato DOCX acumulativo identificado por SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`.

No se autoriza ninguna reescritura de Section 4.4 durante la integración.

## 3. Promoción autorizada

Se autoriza materializar los bytes exactos del candidato Markdown B03 aprobado como:

`article/manuscript/ARTICLE_MASTER_V012.md`

La promoción es un gate exclusivamente técnico. La identidad debe verificarse contra:

- SHA-256: `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`;
- Git blob esperado: `dfea73f5f462fc65cf98347f796deadc6da58455`.

No está permitido reconstruir, remaquetar, normalizar o reescribir el candidato durante la promoción. Si los bytes exactos no están disponibles, la integración queda bloqueada hasta handoff del artefacto exacto.

El DOCX permanece bajo custodia local del autor conforme a D-021/D-027 y pasa a ser el candidato Word aprobado que deberá convertirse en baseline canónico cuando se cierre la promoción V012.

## 4. Gate posterior

Section 4.5 no se abre por la sola aprobación autoral. Primero debe materializarse y verificarse `ARTICLE_MASTER_V012.md`. Tras ese cierre técnico, la IA Gestora deberá sincronizar el ground truth experimental vivo pertinente a 4.5 y emitir un prompt atómico específico antes de cualquier redacción.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B03_V012_CANONICAL_INTEGRATION
NEXT_ACTOR = IA_GESTORA / TECHNICAL_INTEGRATION_ONLY
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_4 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
ARTICLE_MASTER_V012 = AUTHORIZED / NOT_YET_MATERIALIZED
SECTION_4_5 = ELIGIBLE_AFTER_V012_INTEGRATION / NOT_AUTHORIZED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

B03 V01 passed independent scientific review and the subsequent DOCX-completion review. The author then expressly approved B03. Section 4.4 and both approved cumulative candidates are therefore frozen and ready for integration. Exact-byte materialization of the approved B03 Markdown candidate as `article/manuscript/ARTICLE_MASTER_V012.md` is authorized, subject to SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78` and expected Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`. Section 4.5 remains unauthorized until the V012 canonical-integration gate is closed.