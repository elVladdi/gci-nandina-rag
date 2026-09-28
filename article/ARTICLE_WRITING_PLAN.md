# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.16
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-090
CANONICAL_MASTER = ARTICLE_MASTER_V016
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V016.md
CANONICAL_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
CANONICAL_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B01_V017_PROMOTION_PENDING
EXPERIMENTAL_DESIGN = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
RESULTS_B01_CANDIDATE_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
RESULTS_B01_CANDIDATE_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
RESULTS_B01_CANDIDATE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V017
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V016.md` continúa siendo el master Markdown canónico hasta la promoción verificada de V017. Experimental Design permanece totalmente integrado.

Results B01 / §5.1 completó la secuencia de redacción, auditoría Gestora y aprobación autoral. D-090 autoriza exclusivamente la promoción byte-exacta del candidato aprobado a V017.

## 2. Results B01 / Section 5.1

```text
STATUS = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
RESPONSE = article/responses/6_RESULTS_B01_SECTION5_1_RESPONSE_V01.md@6796dd29f3c530e91c463a207aea9e9dd8e9d187
SECTION = article/sections/results/Results_B01_V01.md@28948cad188b7ad79ab44b6b9e19b90e659e5f1d
REVIEW = article/reviews/6_RESULTS_B01_SECTION5_1_INTERNAL_REVIEW_V01.md@76990c16e3bd1c0aea23bbe8311f86d98d05df56
AUTHOR_GATE = article/governance/D089_RESULTS_B01_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@cfba21a2ed00e3bb589a57e8f11184049fe87084
AUTHOR_APPROVAL = article/governance/D090_RESULTS_B01_AUTHOR_APPROVAL_AND_V017_AUTHORIZATION.md@5c54fca1858bf8e9dcf67417a79c0e9d31354241
```

Identidades congeladas:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md
SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c

ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

## 3. Promoción pendiente

El autor debe materializar el archivo Markdown aprobado sin modificación como:

`article/manuscript/ARTICLE_MASTER_V017.md`

IA Gestora verificará el Git blob exacto `35edb134f3d060bad4257d314cf415d9ecf17b6c`. Solo después de ese `PASS` V017 será declarado canónico y el DOCX B01 aprobado se convertirá en el Word acumulativo canónico.

## 4. Estructura de Results

```text
5.1 Data and partition checks             = APPROVED / PROMOTION_PENDING
5.2 Candidate retrieval performance       = NOT_AUTHORIZED
5.3 Documentary evidence retrieval        = NOT_AUTHORIZED
5.4 Controlled explanation quality        = NOT_AUTHORIZED
5.5 Sensitivity and robustness analyses   = NOT_AUTHORIZED
5.6 Inferential results                    = NOT_AUTHORIZED
5.7 Summary by research question           = NOT_AUTHORIZED
```

## 5. Gate inmediato

```text
NEXT_ACTOR = AUTHOR_FOR_BYTE_EXACT_MATERIALIZATION
NEXT_ACTION = MATERIALIZE_ARTICLE_MASTER_V017
AFTER_VERIFICATION_NEXT_ACTOR = IA_GESTORA
AFTER_VERIFICATION_NEXT_ACTION = INTEGRATE_B01_AND_PREPARE_RESULTS_B02_GROUND_TRUTH_GATE
RESULTS_B02_PLUS = NOT_AUTHORIZED_UNTIL_SEPARATE_GATE
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

No debe ejecutarse B02 antes de la verificación de V017. Una vez verificada, IA Gestora continuará automáticamente con el siguiente gate salvo bloqueo real.

---

# English

Results B01 / Section 5.1 is author-approved and frozen. The only pending action is byte-exact materialization of the approved Markdown candidate as `article/manuscript/ARTICLE_MASTER_V017.md`. V016 remains canonical until exact identity is verified. Results B02 and later sections remain unauthorized pending their own ground-truth and drafting gates.