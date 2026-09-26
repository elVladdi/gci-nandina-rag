# D-055 — Experimental Design B02 integration and ARTICLE_MASTER_V011 promotion

```text
DECISION_ID = D-055
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B02
AUTHOR_APPROVAL = RECEIVED / PRESERVED
SCIENTIFIC_REVIEW = PASS
TECHNICAL_CLOSURE = PASS
EXPERIMENTAL_DESIGN_B02_V02 = APPROVED / FROZEN / INTEGRATED
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V011
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V011.md
CANONICAL_MASTER_MD_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
CANONICAL_MASTER_MD_GIT_BLOB = c2aee16c219ed33c16e8e647fbd56f4dacc2cd61
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf
CANONICAL_CITATION_COMMENTS = 40
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Base de la decisión

Experimental Design B02 V02 superó la auditoría científica y diferencial independiente, recibió aprobación autoral expresa y quedó congelado para integración mediante D-054. El gate posterior era exclusivamente técnico: materializar el Markdown exacto aprobado como nuevo master canónico.

El autor materializó `article/manuscript/ARTICLE_MASTER_V011.md` en `article/main-manuscript`. La IA Gestora verificó identidad exacta contra el artefacto aprobado mediante dos controles independientes:

- SHA-256 del artefacto aprobado y del handoff local: `ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f`;
- Git blob esperado para esos mismos 146647 bytes: `c2aee16c219ed33c16e8e647fbd56f4dacc2cd61`, idéntico al blob publicado por GitHub para `ARTICLE_MASTER_V011.md`.

La materialización es, por tanto, byte-exacta. No hubo reconstrucción editorial ni modificación científica durante la promoción.

## 2. Integración canónica

Se promueve:

`article/manuscript/ARTICLE_MASTER_V011.md`

como master Markdown canónico.

Experimental Design B02 V02 y Section 4.3 pasan a `CLOSED / APPROVED / FROZEN / INTEGRATED`.

El DOCX aprobado correspondiente permanece bajo custodia local efectiva del autor conforme a D-021/D-027:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx`

SHA-256:

`d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf`

No se reabre ni modifica ninguna sección previamente aprobada.

## 3. Gate posterior

Cerrada la integración de B02, Section 4.4 `Partition validity and dependence controls` queda elegible para apertura editorial. Su redacción no puede comenzar hasta que la IA Gestora emita un prompt atómico específico y verifique previamente el ground truth experimental vivo que gobierna particiones, agrupamiento DAM, duplicados/near-duplicates y controles de dependencia.

Sections 4.5–4.8 y Results continúan no autorizados.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B03_SECTION_4_4_GROUND_TRUTH_AND_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
