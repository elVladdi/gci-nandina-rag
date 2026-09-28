# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.34
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-123
CANONICAL_MASTER = ARTICLE_MASTER_V023
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V023.md
CANONICAL_MASTER_MD_SHA256 = d3a54bd263f8f24690fa259eb732e4805515899f0219b6b822b4978e9b985446
CANONICAL_MASTER_MD_GIT_BLOB = 657c85211323ba60a65d54cccb31edb90c0d18c3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 42803266758c336b83be935c2bd6e2f9d828a4697617d9f8cd0b8bf32da41506
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
CURRENT_GATE = DISCUSSION_B01_V01_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
TARGET_IF_APPROVED = ARTICLE_MASTER_V024
DISCUSSION_B02_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V023.md` es el master Markdown canónico verificado. Results §5.1–§5.7 están cerrados, aprobados, congelados e integrados.

Discussion B01 V01 / §6.1 fue ejecutado bajo D-121/D-122 y superó la auditoría independiente de IA Gestora:

`article/reviews/7_DISCUSSION_B01_SECTION6_1_INTERNAL_REVIEW_V01.md@26ec9d29e671a4a8968cdd42f9b2c96dcc7f8229` — `PASS`.

D-123 abre el gate de aprobación del autor:

`article/governance/D123_DISCUSSION_B01_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@49a8024f1792ef00549c9595529f7ada7ef08864`.

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = GESTORA PASS / PENDING AUTHOR APPROVAL
6.2 Controlled use of the LLM for explanation              = NOT AUTHORIZED
6.3 Comparison with prior work                             = NOT AUTHORIZED
6.4 Implications for auditable decision support            = NOT AUTHORIZED
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Objeto exacto de aprobación B01

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.md
SHA256 = 0b6ea338cf325c1c59e23f91633791f97868c91eeaea44cca89f8d65c6ee7864
GIT_BLOB_EXPECTED = d0ecf9f4a44b8900dd1b65f289fb0b2abf6d29c0

ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.docx
SHA256 = cc0bb87adacbfbca7403335f6a1070acf27f04b05c2d6a8772b0608c3923f0e0
COMMENTS = 42
TRACKED_CHANGES = 0
PAGE_COUNT = 60
```

Response y sección:

```text
RESPONSE = article/responses/7_DISCUSSION_B01_SECTION6_1_RESPONSE_V01.md@9009add5283f55281ba9068b6f02c3f9637a5261
SECTION = article/sections/discussion/Discussion_B01_V01.md@6f57a3f32604985e5c0e268c0d3831753d6e77f0
SECTION_GIT_BLOB = 52cc461f96dfb157a91fd74232f7aa44f970fb77
```

## 4. Resultado de auditoría

La auditoría confirma que V023→B01 modifica exclusivamente los placeholders inglés y español de §6.1. El bloque contiene cinco párrafos por idioma y conserva Results, §6.2–§6.6, Conclusion y end matter.

El contraste con Lee et al. (2021) y Lee et al. (2023) fue revalidado directamente contra los papers fuente y es funcionalmente correcto. No se introduce comparación numérica directa entre estudios, causalidad, overall framework accuracy, superioridad global, corrección normativa/jurídica, novelty ni FINAL_GAP.

El DOCX fue auditado contra el baseline B07: 14/14 partes OOXML preservadas en conjunto, con cambios únicamente en `word/document.xml` y `word/comments.xml`; 40 comentarios heredados preservados; comentarios nuevos 40 y 41 correctamente anclados a las citas inglesas; 42 comentarios totales y 0 tracked changes. El render independiente produjo 60 páginas: 55 pixel-identical y cinco páginas afectadas sin defectos visuales.

## 5. Regla de promoción si el autor aprueba

La aprobación autorizará únicamente:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V024.md
EXPECTED_SHA256 = 0b6ea338cf325c1c59e23f91633791f97868c91eeaea44cca89f8d65c6ee7864
EXPECTED_GIT_BLOB = d0ecf9f4a44b8900dd1b65f289fb0b2abf6d29c0
```

V023 seguirá siendo canónico hasta aprobación, materialización y verificación byte-exacta de V024. El DOCX permanece bajo custodia local del autor. D-035 continúa activo.

Solo después de integrar B01 podrá IA Gestora decidir y abrir Discussion B02 / §6.2; B02 no queda autorizado por anticipado.

## 6. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_DISCUSSION_B01_V01
CURRENT_GATE = DISCUSSION_B01_V01_AUTHOR_APPROVAL
CANONICAL_MASTER_UNTIL_PROMOTION = ARTICLE_MASTER_V023
TARGET_IF_APPROVED = ARTICLE_MASTER_V024
DISCUSSION_B02_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V023 remains canonical and verified. Discussion B01 / Section 6.1 V01 passed independent Managing AI audit with no mandatory corrections and is pending explicit author approval. The audited Markdown candidate has SHA-256 `0b6ea338cf325c1c59e23f91633791f97868c91eeaea44cca89f8d65c6ee7864` and expected Git blob `d0ecf9f4a44b8900dd1b65f289fb0b2abf6d29c0`; the DOCX candidate has SHA-256 `cc0bb87adacbfbca7403335f6a1070acf27f04b05c2d6a8772b0608c3923f0e0`, 42 comments, zero tracked changes, and 60 pages.

```text
CURRENT_GATE = DISCUSSION_B01_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
DISCUSSION_B01 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
TARGET_IF_APPROVED = ARTICLE_MASTER_V024
DISCUSSION_B02_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```