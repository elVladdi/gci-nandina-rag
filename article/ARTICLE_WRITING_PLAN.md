# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.11
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-084
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V015.md
CANONICAL_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = B07_V02_AUTHOR_APPROVAL
EXPERIMENTAL_DESIGN_B01_TO_B06 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B07 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
SECTION_4_8 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_CORRECTION_B07_C01 = CLOSED / PASS
AUTHOR_APPROVAL_GATE = OPEN_FOR_B07_V02_ONLY
B07_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V015.md` permanece como master Markdown canónico verificado y `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx` como Word canónico bajo custodia local del autor.

B07 V01 fue rechazado por el autor únicamente porque Section 4.8 presentaba narrativamente el repositorio interno de desarrollo experimental. D-082 convirtió esa observación en B07-C01; D-083 autorizó la corrección estrecha y B07 V02 la ejecutó.

## 2. B07 V02 auditado

Response:

`article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V02.md@b28723a1c1b8d66d8791f23a88a7ff77a2b61161`

Artefacto de sección:

`article/sections/experimental_design/Experimental_Design_B07_V02.md@112669ae8998311d17b4510a2fc8afd7c1fdda49`

Auditoría Gestora:

`article/reviews/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_INTERNAL_REVIEW_V02.md@1a59ae7d81549f0c42c8d72d5f7fb1891258f7c6` — `PASS`.

Decisión vigente:

`article/governance/D084_EXPERIMENTAL_DESIGN_B07_V02_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@d60fa9c4d781f653ac1b09b48940be63fcd2827d`.

### 2.1 Candidatos exactos ante el autor

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md
SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_RENDER = PASS / 51 OF 51 PAGES
VISUAL_QA = PASS
```

## 3. Resultado de B07-C01

La corrección queda cerrada:

```text
PUBLIC_REPRO_REPOSITORY = gci-nandina-rag-reproducibility
INTERNAL_DEVELOPMENT_REPOSITORY_MENTION_IN_SECTION_4_8 = NONE
PUBLIC_RESOURCE_FOCUS = PASS
MATERIALIZED_VS_PLANNED_VS_RESTRICTED = PASS
REFERENCE_REPRODUCTION_VS_EXTERNAL_REPLICATION = PASS
CONFIGURABILITY_IS_NOT_GENERALIZATION = PASS
```

Section 4.8 V02 abre directamente con el repositorio público. No presenta ni describe el repositorio interno de desarrollo como recurso de reproducibilidad. Las entradas no públicas se describen únicamente por su condición de restringidas/no redistribuidas.

El snapshot público permanece en HEAD `254831cd955103faa2517065a7eed7fb340bbccc`, tree `078a85255fa1f3234b4f7ed51ef2660b903d486e`.

## 4. Continuidad y D-035

El cambio acumulativo está confinado a Section 4.8 EN/ES. Se preservan Sections 1–4.7 y Results+. El DOCX conserva 14/14 entradas OOXML, 40 comentarios y anchors y 0 tracked changes; solo `word/document.xml` cambió. El render independiente produce 51 páginas y pasa QA visual.

D-035 continúa satisfecho: los candidatos acumulativos fueron entregados como archivos reales y no se observó Base64 manual, chunking, fragmentación o reensamblado.

## 5. Gate autoral

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_B07_V02_OR_REQUEST_CHANGES
AUTHOR_APPROVAL_GATE = OPEN_FOR_B07_V02_ONLY
B07_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
```

Si B07 V02 es aprobado, la siguiente operación será congelar los candidatos exactos, autorizar V016, materializarla y verificarla byte-exactamente. El cierre de Experimental Design no autoriza Results automáticamente.

---

# English

## 1. Current state

`ARTICLE_MASTER_V015.md` remains canonical. B07 V02 passed independent review after the narrow author-requested correction that removed the internal experimental-development repository from Section 4.8 manuscript prose.

```text
B07_V02_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
B07_V02_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
B07_V02_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_RENDER = PASS / 51 OF 51 PAGES
```

Section 4.8 now focuses directly on the public reproducibility repository, preserves the materialized/planned/restricted boundaries, distinguishes reference reproduction from external replication, and does not infer empirical generalization from configurability.

## 2. Gate

```text
CURRENT_GATE = B07_V02_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
B07_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
