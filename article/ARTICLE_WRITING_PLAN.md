# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.36
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-127
CANONICAL_MASTER = ARTICLE_MASTER_V024
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V024.md
CANONICAL_MASTER_MD_SHA256 = 0b6ea338cf325c1c59e23f91633791f97868c91eeaea44cca89f8d65c6ee7864
CANONICAL_MASTER_MD_GIT_BLOB = d0ecf9f4a44b8900dd1b65f289fb0b2abf6d29c0
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cc0bb87adacbfbca7403335f6a1070acf27f04b05c2d6a8772b0608c3923f0e0
CANONICAL_CITATION_COMMENTS = 42
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
CURRENT_GATE = DISCUSSION_B02_V01_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
TARGET_IF_APPROVED = ARTICLE_MASTER_V025
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V024.md` es el master Markdown canónico verificado. Results §5.1–§5.7 y Discussion §6.1 están cerrados, aprobados, congelados e integrados.

Discussion B02 V01 / §6.2 fue ejecutado bajo D-125/D-126 y superó la auditoría independiente de IA Gestora:

`article/reviews/7_DISCUSSION_B02_SECTION6_2_INTERNAL_REVIEW_V01.md@60a50d8191ec443f001cb6480295c9e18c30e9ac` — `PASS`.

D-127 abre el gate de aprobación del autor:

`article/governance/D127_DISCUSSION_B02_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@a705f2dc7a43e32797a2dbe43d335ffedeb0ee90`.

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = GESTORA PASS / PENDING AUTHOR APPROVAL
6.3 Comparison with prior work                             = NOT AUTHORIZED
6.4 Implications for auditable decision support            = NOT AUTHORIZED
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Objeto exacto de aprobación B02

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.md
SHA256 = a805cd220904fb4972d0db59764425aff87a49c8ec1cd34936e85913778feee5
GIT_BLOB_EXPECTED = 829a6f5df87cf91dcafe89c48c1afd48ddbd2faf

ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx
SHA256 = cc8f765bc197acbb210ebcb01da104ebd282481013d549ca51c8cf80268786c7
COMMENTS = 44
TRACKED_CHANGES = 0
PAGE_COUNT = 62
```

Response y sección:

```text
RESPONSE = article/responses/7_DISCUSSION_B02_SECTION6_2_RESPONSE_V01.md@77a4e87fe7293c26d2af2e1160e2000117fb21a1
SECTION = article/sections/discussion/Discussion_B02_V01.md@9f95e5d0367f305e73a71913b6e37e1bc0e09069
SECTION_GIT_BLOB = e9f8abaf6d023e7fe3c46460cab8fd345bec1caf
```

## 4. Resultado de auditoría

La auditoría confirma que V024→B02 modifica exclusivamente los placeholders inglés y español de §6.2. Revertir esos dos bloques reproduce exactamente el SHA-256 canónico de V024.

El bloque interpreta el LLM como componente downstream explanation-only. Conserva simultáneamente los resultados RQ3 congelados:

```text
STRUCTURAL_PRESERVATION = 50/50 CASES
SLOT_LEVEL_CONTROLS = 150/150 SLOTS
QUALITATIVE_AUDITABILITY = 28/50 = 56.0%
VERIFIABILITY_MEAN = 0.54/2
HISTORICAL_NORMATIVE_SEPARATION_MEAN = 1.04/2
SCHEMA_COMPLIANCE = 0/50 / PROMPT_SCHEMA_SPECIFICATION_MISMATCH ONLY
QUALITATIVE_EVALUATOR = LLM_AS_JUDGE / NOT HUMAN
```

No se introducen claims de reducción de alucinaciones, seguridad, causalidad, validación humana, overall framework accuracy, superioridad global, corrección normativa/jurídica, faithful causal explanation, novelty ni `FINAL_GAP`.

El contraste de literatura se limita a Marra de Artiñano et al. (2023) y Kim et al. (2025) en términos de autoridad y secuenciación funcional del LLM. No se realizan comparaciones numéricas entre estudios.

El DOCX conserva 14/14 partes OOXML; únicamente cambian `word/document.xml` y `word/comments.xml`. Los comentarios 0–41 están preservados canónicamente y se añaden exactamente los comentarios 42 y 43 anclados a las dos citas inglesas. El total es 44 comentarios, 0 tracked changes. El render independiente produjo 62 páginas y superó QA visual.

## 5. Regla de promoción si el autor aprueba

La aprobación autorizará únicamente:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V025.md
EXPECTED_SHA256 = a805cd220904fb4972d0db59764425aff87a49c8ec1cd34936e85913778feee5
EXPECTED_GIT_BLOB = 829a6f5df87cf91dcafe89c48c1afd48ddbd2faf
```

V024 seguirá siendo canónico hasta aprobación, materialización y verificación byte-exacta de V025. El DOCX permanece bajo custodia local del autor. D-035 continúa activo.

Solo después de integrar B02 podrá IA Gestora decidir y abrir Discussion B03 / §6.3. B03 no queda autorizado por anticipado.

## 6. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_DISCUSSION_B02_V01
CURRENT_GATE = DISCUSSION_B02_V01_AUTHOR_APPROVAL
CANONICAL_MASTER_UNTIL_PROMOTION = ARTICLE_MASTER_V024
TARGET_IF_APPROVED = ARTICLE_MASTER_V025
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V024 remains canonical and verified. Discussion B02 / Section 6.2 V01 passed independent Managing-AI audit with no mandatory corrections and is pending explicit author approval. The audited Markdown candidate has SHA-256 `a805cd220904fb4972d0db59764425aff87a49c8ec1cd34936e85913778feee5` and expected Git blob `829a6f5df87cf91dcafe89c48c1afd48ddbd2faf`; the DOCX candidate has SHA-256 `cc8f765bc197acbb210ebcb01da104ebd282481013d549ca51c8cf80268786c7`, 44 comments, zero tracked changes, and 62 pages.

```text
CURRENT_GATE = DISCUSSION_B02_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
DISCUSSION_B02 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
TARGET_IF_APPROVED = ARTICLE_MASTER_V025
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```