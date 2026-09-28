# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.22
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-101
CANONICAL_MASTER = ARTICLE_MASTER_V018
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V018.md
CANONICAL_MASTER_MD_SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
CANONICAL_MASTER_MD_GIT_BLOB = d392bdc2ae139ab692637c8c3a42ff6804f4d41a
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B03_V01_AUTHOR_APPROVAL
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
RESULTS_B04_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = OPEN_FOR_B03_V01_ONLY
TARGET_PROMOTION_IF_APPROVED = ARTICLE_MASTER_V019
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V018.md` continúa como master Markdown canónico verificado. El Word acumulativo canónico continúa siendo `ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx`, SHA-256 `3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9`, bajo custodia local del autor, con 40 comentarios y 0 tracked changes.

Experimental Design, Results B01 / §5.1 y Results B02 / §5.2 están cerrados, aprobados, congelados e integrados.

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = GESTORA PASS / AUTHOR APPROVAL GATE OPEN
5.4 Controlled explanation quality        = NOT AUTHORIZED
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Results B03 V01 — candidato auditado

```text
RESPONSE = article/responses/6_RESULTS_B03_SECTION5_3_RESPONSE_V01.md@4a2f3962ca21904a3e73f6c2298654b25d551b94
SECTION = article/sections/results/Results_B03_V01.md@079158ec9263870ebcf32f3cc9612723ce9b1ee0

CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.md
SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
GIT_BLOB_EXPECTED = cb0dc9cf64f01d945e1ae952e558fd459335f95e

CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 54
```

Revisión Gestora:

`article/reviews/6_RESULTS_B03_SECTION5_3_INTERNAL_REVIEW_V01.md@17e4ffd25f99e6457c3ca951d1102c9db4414cd9` — `PASS`.

D-101:

`article/governance/D101_RESULTS_B03_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@040c14dc9440f044ceeae3c9a119ddf498655d61`.

La auditoría confirmó fidelidad numérica frente al EXP-04-F congelado, uso únicamente de C30-C34, conservación de las fronteras association/coverage vs correctness, modificación exclusiva de §5.3 en las dos partes, equivalencia EN/ES, continuidad OOXML y render correcto de 54 páginas.

## 4. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REQUEST_CHANGES_FOR_RESULTS_B03_V01
AUTHOR_APPROVAL_GATE = OPEN_FOR_B03_V01_ONLY
CANONICAL_MASTER = ARTICLE_MASTER_V018
TARGET_PROMOTION_IF_APPROVED = ARTICLE_MASTER_V019
RESULTS_B04_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

La aprobación autoral debe referirse al candidato exacto B03 V01 identificado por los hashes anteriores. Una aprobación no autoriza por sí misma B04: primero deberá materializarse y verificarse la promoción byte-exacta a V019 y cerrarse B03.

D-035 continúa activo. Los masters acumulativos grandes no deben materializarse mediante workarounds de Base64/chunking/fragmentación/reensamblado.

---

# English

V018 remains canonical. Results B03 V01 passed Gestora audit and is pending explicit author approval. The author-approval gate is open for the exact B03 V01 MD/DOCX candidates only. If approved, the next promotion target is V019; Results B04+ remains unauthorized until B03 integration is completed and verified.

```text
CURRENT_GATE = RESULTS_B03_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
AUTHOR_APPROVAL_GATE = OPEN_FOR_B03_V01_ONLY
TARGET_PROMOTION_IF_APPROVED = ARTICLE_MASTER_V019
RESULTS_B04_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```