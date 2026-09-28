# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.23
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-102
CANONICAL_MASTER = ARTICLE_MASTER_V018
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V018.md
CANONICAL_MASTER_MD_SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
CANONICAL_MASTER_MD_GIT_BLOB = d392bdc2ae139ab692637c8c3a42ff6804f4d41a
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B03_V01_PROMOTION_TO_V019_PENDING_MATERIALIZATION
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
RESULTS_B04_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = CLOSED / APPROVED
TARGET_PROMOTION = ARTICLE_MASTER_V019
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V018.md` continúa como master Markdown canónico verificado hasta completar la promoción B03. Experimental Design, Results B01 / §5.1 y Results B02 / §5.2 están cerrados, aprobados, congelados e integrados.

Results B03 V01 / §5.3 fue auditado con `PASS` por IA Gestora y aprobado explícitamente por el autor. D-102 registra la aprobación y autoriza la promoción byte-exacta a `ARTICLE_MASTER_V019.md`.

Candidato Markdown aprobado:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.md
SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
GIT_BLOB_EXPECTED = cb0dc9cf64f01d945e1ae952e558fd459335f95e
```

Word aprobado bajo custodia local del autor:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 54
```

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = APPROVED / PROMOTION TO V019 PENDING
5.4 Controlled explanation quality        = NOT AUTHORIZED
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Gobernanza de B03

```text
B03_RESPONSE = article/responses/6_RESULTS_B03_SECTION5_3_RESPONSE_V01.md@4a2f3962ca21904a3e73f6c2298654b25d551b94
B03_SECTION = article/sections/results/Results_B03_V01.md@079158ec9263870ebcf32f3cc9612723ce9b1ee0
B03_REVIEW = article/reviews/6_RESULTS_B03_SECTION5_3_INTERNAL_REVIEW_V01.md@17e4ffd25f99e6457c3ca951d1102c9db4414cd9
B03_REVIEW_RESULT = PASS
B03_AUTHOR_GATE = article/governance/D101_RESULTS_B03_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@040c14dc9440f044ceeae3c9a119ddf498655d61
B03_AUTHOR_APPROVAL = article/governance/D102_RESULTS_B03_V01_AUTHOR_APPROVAL_AND_V019_AUTHORIZATION.md@a2cff866d6c6d9060a2cfdfdd2236f05ccf709b6
```

B03 queda `CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION`.

## 4. Promoción V019

La única promoción autorizada es:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V019.md
EXPECTED_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
EXPECTED_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e
```

D-035 continúa activo: IA Gestora no debe materializar el master grande mediante Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes. El autor debe subir el archivo exacto y la Gestora deberá auditar su identidad antes de cambiar el master canónico.

## 5. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = UPLOAD_EXACT_B03_V01_MD_AS_ARTICLE_MASTER_V019
TARGET_PATH = article/manuscript/ARTICLE_MASTER_V019.md
EXPECTED_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
EXPECTED_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e
AFTER_UPLOAD = IA_GESTORA_VERIFY_V019_AND_CONTINUE_TO_B04_GROUND_TRUTH_GATE
RESULTS_B04_PLUS = NOT_AUTHORIZED_UNTIL_VERIFIED_V019
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V018 remains canonical until the approved B03 V01 Markdown candidate is materialized byte-exactly as V019 and independently verified. B03 / Section 5.3 is closed, approved, frozen, and ready for integration. Results B04+ remains unauthorized until verified V019 integration is complete.

```text
CURRENT_GATE = RESULTS_B03_V01_PROMOTION_TO_V019_PENDING_MATERIALIZATION
NEXT_ACTOR = AUTHOR
TARGET_PROMOTION = ARTICLE_MASTER_V019
RESULTS_B04_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```