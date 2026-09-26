# D-058 — Experimental Design B03 integration and ARTICLE_MASTER_V012 promotion

```text
DECISION_ID = D-058
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B03
AUTHOR_APPROVAL = RECEIVED / PRESERVED
SCIENTIFIC_REVIEW = PASS
DOCX_COMPLETION_REVIEW = PASS
TECHNICAL_CLOSURE = PASS
EXPERIMENTAL_DESIGN_B03_V01 = APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Base de la decisión

Experimental Design B03 V01 superó la auditoría científica independiente y el microgate técnico de continuidad DOCX. El autor otorgó aprobación expresa y D-057 congeló el candidato para integración, sin autorizar todavía Section 4.5.

El autor materializó posteriormente `article/manuscript/ARTICLE_MASTER_V012.md`. La IA Gestora verificó la identidad del archivo publicado contra la identidad congelada del candidato B03:

- SHA-256 aprobado: `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`;
- Git blob esperado: `dfea73f5f462fc65cf98347f796deadc6da58455`;
- Git blob observado en `ARTICLE_MASTER_V012.md`: `dfea73f5f462fc65cf98347f796deadc6da58455`.

La coincidencia del blob confirma materialización byte-exacta del Markdown aprobado. No hubo reconstrucción editorial ni modificación científica durante la promoción.

## 2. Integración canónica

Se promueve `article/manuscript/ARTICLE_MASTER_V012.md` como master Markdown canónico.

Experimental Design B03 V01 y Section 4.4 pasan a `CLOSED / APPROVED / FROZEN / INTEGRATED`.

El DOCX acumulativo aprobado correspondiente permanece bajo custodia local del autor:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`

SHA-256:

`9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`

No se reabre ni modifica contenido científico previamente aprobado.

## 3. Gate posterior

Cerrada B03, Section 4.5 queda elegible para preparación editorial. Su redacción requiere un prompt atómico específico, verificación previa del ground truth experimental vivo y continuidad obligatoria tanto del Markdown canónico V012 como del DOCX acumulativo B03 exacto. La entrega Word no puede quedar condicional ni reconstruirse desde Markdown.

Sections 4.6–4.8 y Results continúan no autorizados.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_GROUND_TRUTH_AND_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```