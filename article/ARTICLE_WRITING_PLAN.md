# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.25
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-106
CANONICAL_MASTER = ARTICLE_MASTER_V019
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V019.md
CANONICAL_MASTER_MD_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
CANONICAL_MASTER_MD_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
CURRENT_DRAFTING_PHASE = RESULTS
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B04_SECTION_5_4 = DRAFTED / GESTORA_AUDIT_PASS / PENDING_AUTHOR_APPROVAL
RESULTS_B05_PLUS = NOT_AUTHORIZED
CURRENT_GATE = RESULTS_B04_V01_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Español

### 1. Estado acumulativo

El master canónico verificado continúa siendo `ARTICLE_MASTER_V019.md`. Results §5.1–§5.3 están cerrados, aprobados, congelados e integrados.

Results B04 / §5.4 fue redactado bajo D-104/D-105 y auditado con `PASS` por IA Gestora.

```text
B04_RESPONSE = article/responses/6_RESULTS_B04_SECTION5_4_RESPONSE_V01.md@e04240de4cf43ae6821e5630af6d126aaf75c863
B04_SECTION = article/sections/results/Results_B04_V01.md@22f8586fe1f4f7fa8aa9585496be4f6621a56f94
B04_REVIEW = article/reviews/6_RESULTS_B04_SECTION5_4_INTERNAL_REVIEW_V01.md@1eb1aa4d45f27b03858220da18d8e423a81c0ed8
B04_REVIEW_RESULT = PASS
B04_AUTHOR_GATE = article/governance/D106_RESULTS_B04_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@95196c85de1296249579361dd70aac370294c809
```

### 2. Candidatos B04 auditados

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md
SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b

ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 54
```

La auditoría verificó que el Markdown difiere de V019 solo en §5.4 inglesa y española. En Word, únicamente `word/document.xml` cambió; las demás partes OOXML permanecieron byte-exactas. El render completo fue `PASS` y solo cambian las páginas 25–27 y 52–54 frente al baseline.

### 3. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = AUDIT PASS / AUTHOR APPROVAL PENDING
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

### 4. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = REVIEW_AND_EXPLICITLY_APPROVE_OR_REJECT_RESULTS_B04_V01
IF_APPROVED = IA_GESTORA_RECORD_AUTHOR_APPROVAL_AND_AUTHORIZE_BYTE_EXACT_PROMOTION_TO_ARTICLE_MASTER_V020
TARGET_PROMOTION_IF_APPROVED = ARTICLE_MASTER_V020
CANONICAL_MASTER_UNTIL_PROMOTION = ARTICLE_MASTER_V019
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

No se abre B05 hasta la aprobación explícita del autor y la promoción verificada de B04.

---

## English

V019 remains canonical. Results B04 / Section 5.4 V01 has passed independent Gestora audit and is awaiting explicit author approval. B05+ remains unauthorized. If the author approves B04, the next governed action is to record that approval and authorize byte-exact promotion of the approved Markdown candidate to `ARTICLE_MASTER_V020.md`; V019 remains canonical until that promotion is materialized and verified.
