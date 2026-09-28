# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.26
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-107
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
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
RESULTS_B05_PLUS = NOT_AUTHORIZED
CURRENT_GATE = RESULTS_B04_V01_PROMOTION_TO_V020_PENDING_MATERIALIZATION
AUTHOR_APPROVAL_GATE = CLOSED / APPROVED
TARGET_PROMOTION = ARTICLE_MASTER_V020
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Español

### 1. Estado acumulativo

El master canónico verificado continúa siendo `ARTICLE_MASTER_V019.md`. Results §5.1–§5.3 están cerrados, aprobados, congelados e integrados.

Results B04 / §5.4 V01 fue redactado bajo D-104/D-105, auditado con `PASS` por IA Gestora y aprobado explícitamente por el autor. D-107 registra la aprobación y autoriza la promoción byte-exacta a `ARTICLE_MASTER_V020.md`.

### 2. Candidatos B04 aprobados

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md
SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
GIT_BLOB_EXPECTED = 7393bf0db2d577d27168ccbb2a1060f1b337c872

ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 54
```

La auditoría Gestora verificó que el Markdown difiere de V019 solo en §5.4 inglesa y española. En Word, únicamente `word/document.xml` cambió; las demás partes OOXML permanecieron byte-exactas y el render completo fue `PASS`.

### 3. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = APPROVED / PROMOTION TO V020 PENDING
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

### 4. Promoción V020

La única promoción autorizada es:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V020.md
EXPECTED_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
EXPECTED_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872
```

D-035 continúa activo: IA Gestora no debe materializar el master grande mediante Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes. El autor debe subir el archivo exacto y la Gestora deberá auditar su identidad antes de cambiar el master canónico.

### 5. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = UPLOAD_EXACT_B04_V01_MD_AS_ARTICLE_MASTER_V020
TARGET_PATH = article/manuscript/ARTICLE_MASTER_V020.md
EXPECTED_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
EXPECTED_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872
AFTER_UPLOAD = IA_GESTORA_VERIFY_V020_AND_CONTINUE_TO_B05_GROUND_TRUTH_GATE
RESULTS_B05_PLUS = NOT_AUTHORIZED_UNTIL_VERIFIED_V020
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

V019 remains canonical until the approved B04 V01 Markdown candidate is materialized byte-exactly as V020 and independently verified. B04 / Section 5.4 is closed, approved, frozen, and ready for integration. Results B05+ remains unauthorized until verified V020 integration is complete.

```text
CURRENT_GATE = RESULTS_B04_V01_PROMOTION_TO_V020_PENDING_MATERIALIZATION
NEXT_ACTOR = AUTHOR
TARGET_PROMOTION = ARTICLE_MASTER_V020
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```