# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.38
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-131
CANONICAL_MASTER = ARTICLE_MASTER_V025
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V025.md
CANONICAL_MASTER_MD_SHA256 = a805cd220904fb4972d0db59764425aff87a49c8ec1cd34936e85913778feee5
CANONICAL_MASTER_MD_GIT_BLOB = 829a6f5df87cf91dcafe89c48c1afd48ddbd2faf
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cc8f765bc197acbb210ebcb01da104ebd282481013d549ca51c8cf80268786c7
CANONICAL_CITATION_COMMENTS = 44
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B03_SECTION_6_3 = AUDITED / PASS / PENDING_AUTHOR_APPROVAL
CURRENT_GATE = DISCUSSION_B03_V01_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
NEXT_ACTOR = AUTHOR
DISCUSSION_B04_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V025.md` permanece como master Markdown canónico verificado. Results §5.1–§5.7 y Discussion §6.1–§6.2 están cerrados, aprobados, congelados e integrados.

Discussion B03 / §6.3 V01 fue ejecutado, auditado por IA Gestora y recibió veredicto `PASS` sin correcciones obligatorias. Aún no está integrado: se encuentra en gate de aprobación del autor bajo D-131.

El Word acumulativo canónico anterior continúa siendo:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx
SHA256 = cc8f765bc197acbb210ebcb01da104ebd282481013d549ca51c8cf80268786c7
COMMENTS = 44
TRACKED_CHANGES = 0
PAGE_COUNT = 62
```

El candidato B03 auditado es:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.md
SHA256 = 76107b20419329ef7a5c6643fec892fbdc0e0779c1ab58f6de41bc36711f4156
GIT_BLOB = f6a63be554317e62103aa96c1091f4039249e5ee
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx
SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 64
```

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = INTEGRATED
6.3 Comparison with prior work                             = AUDITED PASS / PENDING AUTHOR APPROVAL
6.4 Implications for auditable decision support            = NOT AUTHORIZED
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Trazabilidad B03

Boundary:
`article/governance/D129_DISCUSSION_B03_SECTION6_3_INTERPRETIVE_BOUNDARY_AND_LITERATURE_TRACE.md@03222ca5666de2a408bd3131e22c1bd56e85dd36`

Prompt:
`article/prompts/7_DISCUSSION_B03_SECTION6_3.md@2203f81bfb3020219aac9c32e4605b357fa8cf81`

Prompt review:
`article/reviews/7_DISCUSSION_B03_SECTION6_3_PROMPT_INTERNAL_REVIEW_V01.md@03fac8bded59a495c5c1d72d126aded0fab15bff` — `PASS`.

Execution authorization:
`article/governance/D130_DISCUSSION_B03_SECTION6_3_EXECUTION_AUTHORIZATION.md@156521548817b30dec11171926876f16477db358`.

Drafting response:
`article/responses/7_DISCUSSION_B03_SECTION6_3_RESPONSE_V01.md@ffc6b710906163c0f22da135a87cb4eb54e72906`.

Section artifact:
`article/sections/discussion/Discussion_B03_V01.md@e7c5747786bb22e92145a7adf397cdb1af7a3656`.

Gestora internal review:
`article/reviews/7_DISCUSSION_B03_SECTION6_3_INTERNAL_REVIEW_V01.md@91f7eb3485b869025b41e0766d6eeb272bcaaf7b` — `PASS`.

Author approval gate:
`article/governance/D131_DISCUSSION_B03_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@dfd89e4288a601f13f0b3d3aaeb3a34c4e07a9d0`.

## 4. Contrato científico B03 auditado

§6.3 compara prior work por función, autoridad y secuenciación de componentes y no por porcentajes de desempeño. Reconoce a Lee et al. (2023) como prior art cercano de candidate prediction seguida de evidence retrieval. Marra de Artiñano et al. (2023) y Kim et al. (2025) se usan para contrastar configuraciones en las que el LLM participa en clasificación con el rol explanation-only downstream del presente estudio.

El posicionamiento permitido se limita al contrato operativo explícito: historical retrieval fija el Top-3 antes de documentary evidence; las etapas downstream no pueden modificar membership ni orden; y candidate retrieval, documentary association y controlled explanation se evalúan como objetos separados.

Ese posicionamiento no autoriza novelty, first-ever, state-of-the-art, superioridad global, causalidad, cross-study numerical superiority, legal correctness ni external generalization.

## 5. Auditoría Word y citas

La ejecución añadió exactamente cuatro nuevas citas/comentarios ingleses —Lee et al. (2021), Lee et al. (2023), Marra de Artiñano et al. (2023) y Kim et al. (2025)— y preservó los 44 comentarios heredados. El candidato Word contiene 48 comentarios, 0 tracked changes y 64 páginas. Solo `word/document.xml` y `word/comments.xml` cambiaron respecto del baseline B02. El render completo y la equivalencia EN/ES pasaron auditoría.

## 6. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_DISCUSSION_B03_V01
AUTHOR_APPROVAL_GATE = OPEN
CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.md
CANDIDATE_MD_SHA256 = 76107b20419329ef7a5c6643fec892fbdc0e0779c1ab58f6de41bc36711f4156
CANDIDATE_MD_GIT_BLOB = f6a63be554317e62103aa96c1091f4039249e5ee
CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx
CANDIDATE_DOCX_SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
IF_APPROVED = AUTHOR_MATERIALIZES_ARTICLE_MASTER_V026_MD / IA_GESTORA_VERIFIES_AND_INTEGRATES
DISCUSSION_B04_PLUS = NOT_AUTHORIZED_UNTIL_B03_INTEGRATION
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V025 remains the canonical master. Results Sections 5.1–5.7 and Discussion Sections 6.1–6.2 are integrated. Discussion B03 / Section 6.3 has passed Managing-AI audit with no mandatory corrections and is pending explicit author approval under D-131. The candidate contains exactly four new English citation comments, 48 total comments, zero tracked changes, and passed full-render visual QA. Section 6.4+, Conclusion, novelty, first-ever, state-of-the-art, cross-study numerical superiority, legal-correctness, and external-generalization claims remain unauthorized.

```text
PLAN_VERSION = V3.38
CURRENT_GATE = DISCUSSION_B03_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
DISCUSSION_B03 = AUDITED / PASS / PENDING_AUTHOR_APPROVAL
DISCUSSION_B04_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```