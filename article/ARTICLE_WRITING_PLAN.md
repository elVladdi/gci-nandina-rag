# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.12
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-085
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V015.md
CANONICAL_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = B07_V02_APPROVED_V016_PROMOTION_PENDING
EXPERIMENTAL_DESIGN_B01_TO_B06 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B07 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_8 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
AUTHOR_CORRECTION_B07_C01 = CLOSED / PASS
AUTHOR_DECISION_B07_V02 = APPROVED
B07_INTEGRATION = PENDING_BYTE_EXACT_PROMOTION
TARGET_MASTER = ARTICLE_MASTER_V016
V016_STATUS = AUTHORIZED / PENDING_MATERIALIZATION_AND_VERIFICATION
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V015.md` permanece como master Markdown canónico hasta que se materialice y verifique V016. El Word canónico vigente continúa siendo `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx` durante este gate de promoción.

B07 V02 / Section 4.8 fue aprobado explícitamente por el autor y queda cerrado, aprobado y congelado. La corrección B07-C01 eliminó del manuscrito la presentación narrativa del repositorio interno de desarrollo y concentró §4.8 en el recurso público de reproducibilidad.

## 2. Artefactos B07 V02 congelados

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md
SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_RENDER = PASS / 51 OF 51 PAGES
```

Response:
`article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V02.md@b28723a1c1b8d66d8791f23a88a7ff77a2b61161`

Auditoría Gestora:
`article/reviews/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_INTERNAL_REVIEW_V02.md@1a59ae7d81549f0c42c8d72d5f7fb1891258f7c6` — `PASS`.

Aprobación/autorización:
`article/governance/D085_EXPERIMENTAL_DESIGN_B07_AUTHOR_APPROVAL_AND_V016_AUTHORIZATION.md@abb391ddd25be771355dd28bcb840bc99ef1ca7c`.

## 3. Section 4.8 congelada

La versión aprobada:

- abre directamente con `gci-nandina-rag-reproducibility`;
- no menciona narrativamente el repositorio interno de desarrollo experimental;
- distingue recursos materializados, planificados/no materializados y entradas restringidas/no redistribuidas;
- distingue reproducción de referencia y replicación externa;
- mantiene que configurabilidad no es evidencia de generalización empírica;
- no afirma todavía una release computacional completa ni reproducción fresh-clone con un comando;
- mantiene el recheck obligatorio del repositorio público antes del freeze final/submission.

## 4. Gate de promoción V016

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = UPLOAD_APPROVED_B07_V02_MD_UNCHANGED_AS_ARTICLE_MASTER_V016
PROMOTION_SOURCE = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md
PROMOTION_TARGET = article/manuscript/ARTICLE_MASTER_V016.md
EXPECTED_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
EXPECTED_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
EXPECTED_EXIT = V016_MATERIALIZED_PENDING_GESTORA_VERIFICATION
RESULTS = NOT_AUTHORIZED
```

Después de la verificación byte-exacta de V016, IA Gestora podrá cerrar formalmente la integración de Experimental Design y preparar, mediante un gate separado, la fase siguiente. El cierre de Section 4 no autoriza Results automáticamente.

---

# English

## 1. Current state

B07 V02 / Section 4.8 is author-approved, closed, and frozen. The exact B07 V02 Markdown candidate is authorized for byte-exact promotion to `ARTICLE_MASTER_V016.md`; the exact DOCX remains in local author custody.

```text
B07_V02_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
B07_V02_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
B07_V02_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

## 2. Promotion gate

```text
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V015
TARGET_MASTER = ARTICLE_MASTER_V016
V016_STATUS = AUTHORIZED / PENDING_MATERIALIZATION_AND_VERIFICATION
NEXT_ACTOR = AUTHOR
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

After byte-exact V016 verification, Experimental Design may be formally integrated. Results requires a separate subsequent editorial gate.