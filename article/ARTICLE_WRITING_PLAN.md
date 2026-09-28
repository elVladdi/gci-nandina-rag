# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.19
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-096
CANONICAL_MASTER = ARTICLE_MASTER_V017
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V017.md
CANONICAL_MASTER_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
CANONICAL_MASTER_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B02_V02_AUTHOR_APPROVAL
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
RESULTS_B03_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = OPEN_FOR_B02_V02_ONLY
TARGET_PROMOTION_IF_APPROVED = ARTICLE_MASTER_V018
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V017.md` continúa como master Markdown canónico verificado. El Word acumulativo canónico continúa siendo `ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx`, SHA-256 `f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f`, bajo custodia local del autor, con 40 comentarios y 0 tracked changes.

Experimental Design y Results B01 / §5.1 están cerrados, aprobados, congelados e integrados.

## 2. Estructura de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = GESTORA PASS / AUTHOR APPROVAL GATE OPEN
5.3 Documentary evidence retrieval        = NOT AUTHORIZED
5.4 Controlled explanation quality        = NOT AUTHORIZED
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Results B02 V02 — candidato auditado

```text
RESPONSE = article/responses/6_RESULTS_B02_SECTION5_2_RESPONSE_V02.md@95036a4be7f9c1597d9c9ef6ec28b8e7d6bd1114
SECTION = article/sections/results/Results_B02_V02.md@778c816302fd486c50e4d681b4a68d0847f03291

CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.md
SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
GIT_BLOB_EXPECTED = d392bdc2ae139ab692637c8c3a42ff6804f4d41a

CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx
SHA256 = 3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 52
```

Revisión Gestora:

`article/reviews/6_RESULTS_B02_SECTION5_2_INTERNAL_REVIEW_V02.md@95dac70c547bfd3da9f99041c41263b8ef26fe71` — `PASS`.

D-096:

`article/governance/D096_RESULTS_B02_V02_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@6ca323128fc75051844494fdb49664ec8b578bac`.

La auditoría confirmó que la V02 aplica únicamente las correcciones españolas estrechas autorizadas por D-094, preserva íntegramente la Parte I inglesa y todo el contenido científico/numérico de B02 V01, mantiene la continuidad OOXML y supera el render completo de 52 páginas.

## 4. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REQUEST_CHANGES_FOR_RESULTS_B02_V02
AUTHOR_APPROVAL_GATE = OPEN_FOR_B02_V02_ONLY
CANONICAL_MASTER = ARTICLE_MASTER_V017
TARGET_PROMOTION_IF_APPROVED = ARTICLE_MASTER_V018
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

La aprobación autoral debe referirse al candidato exacto V02 identificado por los hashes anteriores. Una aprobación no autoriza por sí misma B03: primero deberá materializarse y verificarse la promoción byte-exacta a V018 y cerrarse B02.

D-035 continúa activo. Los masters acumulativos grandes no deben materializarse mediante workarounds de Base64/chunking/fragmentación/reensamblado.

---

# English

V017 remains canonical. Results B02 V02 passed Gestora audit and is pending explicit author approval. The author-approval gate is open for the exact V02 MD/DOCX candidates only. If approved, the next promotion target is V018; Results B03+ remains unauthorized until B02 integration is completed and verified.

```text
CURRENT_GATE = RESULTS_B02_V02_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
AUTHOR_APPROVAL_GATE = OPEN_FOR_B02_V02_ONLY
TARGET_PROMOTION_IF_APPROVED = ARTICLE_MASTER_V018
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```