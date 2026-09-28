# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.20
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-097
CANONICAL_MASTER = ARTICLE_MASTER_V017
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V017.md
CANONICAL_MASTER_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
CANONICAL_MASTER_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B02_V02_PROMOTION_TO_V018_PENDING_MATERIALIZATION
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
RESULTS_B03_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = CLOSED / APPROVED
TARGET_PROMOTION = ARTICLE_MASTER_V018
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V017.md` continúa como master Markdown canónico verificado hasta completar la promoción B02. Experimental Design y Results B01 / §5.1 están cerrados, aprobados, congelados e integrados.

Results B02 V02 / §5.2 fue auditado con `PASS` por IA Gestora y aprobado explícitamente por el autor. D-097 registra la aprobación y autoriza la promoción byte-exacta a `ARTICLE_MASTER_V018.md`.

Candidato Markdown aprobado:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.md
SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
GIT_BLOB_EXPECTED = d392bdc2ae139ab692637c8c3a42ff6804f4d41a
```

Word aprobado bajo custodia local del autor:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx
SHA256 = 3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 52
```

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = APPROVED / PROMOTION TO V018 PENDING
5.3 Documentary evidence retrieval        = NOT AUTHORIZED
5.4 Controlled explanation quality        = NOT AUTHORIZED
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Gobernanza de B02

```text
B02_V02_RESPONSE = article/responses/6_RESULTS_B02_SECTION5_2_RESPONSE_V02.md@95036a4be7f9c1597d9c9ef6ec28b8e7d6bd1114
B02_V02_SECTION = article/sections/results/Results_B02_V02.md@778c816302fd486c50e4d681b4a68d0847f03291
B02_V02_REVIEW = article/reviews/6_RESULTS_B02_SECTION5_2_INTERNAL_REVIEW_V02.md@95dac70c547bfd3da9f99041c41263b8ef26fe71
B02_V02_REVIEW_RESULT = PASS
B02_AUTHOR_GATE = article/governance/D096_RESULTS_B02_V02_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@6ca323128fc75051844494fdb49664ec8b578bac
B02_AUTHOR_APPROVAL = article/governance/D097_RESULTS_B02_V02_AUTHOR_APPROVAL_AND_V018_AUTHORIZATION.md@fec59be3651ce14581d288d48844a808fa2f0d33
```

B02 queda `CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION`. V01 queda superseded por V02.

## 4. Promoción V018

La única promoción autorizada es:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.md
TARGET = article/manuscript/ARTICLE_MASTER_V018.md
EXPECTED_SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
EXPECTED_GIT_BLOB = d392bdc2ae139ab692637c8c3a42ff6804f4d41a
```

D-035 continúa activo: IA Gestora no debe materializar el master grande mediante Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes. El autor debe subir el archivo exacto y la Gestora deberá auditar su identidad antes de cambiar el master canónico.

## 5. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = UPLOAD_EXACT_B02_V02_MD_AS_ARTICLE_MASTER_V018
TARGET_PATH = article/manuscript/ARTICLE_MASTER_V018.md
EXPECTED_SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
EXPECTED_GIT_BLOB = d392bdc2ae139ab692637c8c3a42ff6804f4d41a
AFTER_UPLOAD = IA_GESTORA_VERIFY_V018_AND_CONTINUE_TO_B03_GROUND_TRUTH_GATE
RESULTS_B03_PLUS = NOT_AUTHORIZED_UNTIL_VERIFIED_V018
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V017 remains canonical until the approved B02 V02 Markdown candidate is materialized byte-exactly as V018 and independently verified. B02 / Section 5.2 is closed, approved, frozen, and ready for integration. Results B03+ remains unauthorized until verified V018 integration is complete.

```text
CURRENT_GATE = RESULTS_B02_V02_PROMOTION_TO_V018_PENDING_MATERIALIZATION
NEXT_ACTOR = AUTHOR
TARGET_PROMOTION = ARTICLE_MASTER_V018
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```