# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.15
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-089
CANONICAL_MASTER = ARTICLE_MASTER_V016
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V016.md
CANONICAL_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
CANONICAL_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B01_V01_AUTHOR_APPROVAL
EXPERIMENTAL_DESIGN = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B01_SECTION_5_1 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
RESULTS_B01_CANDIDATE_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
RESULTS_B01_CANDIDATE_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
RESULTS_B01_CANDIDATE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
RESULTS_B02_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = OPEN_FOR_RESULTS_B01_V01_ONLY
TARGET_IF_APPROVED = ARTICLE_MASTER_V017
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V016.md` continúa como master Markdown canónico verificado. El Word acumulativo canónico sigue siendo `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx`, SHA-256 `c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de`, bajo custodia local del autor, con 40 comentarios y 0 tracked changes.

Experimental Design está cerrado, aprobado, congelado e integrado. La fase activa es Results y avanza mediante bloques independientes sometidos a ground-truth sync, contrato, auditoría Gestora, aprobación autoral e integración byte-exacta.

## 2. Results B01 / Section 5.1

La IA de Redacción ejecutó B01 conforme a D-087/D-088 y produjo:

```text
RESPONSE = article/responses/6_RESULTS_B01_SECTION5_1_RESPONSE_V01.md@6796dd29f3c530e91c463a207aea9e9dd8e9d187
SECTION = article/sections/results/Results_B01_V01.md@28948cad188b7ad79ab44b6b9e19b90e659e5f1d

CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md
SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
GIT_BLOB_EXPECTED_FROM_BYTES = 35edb134f3d060bad4257d314cf415d9ecf17b6c

CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

## 3. Auditoría Gestora

Revisión independiente:

`article/reviews/6_RESULTS_B01_SECTION5_1_INTERNAL_REVIEW_V01.md@76990c16e3bd1c0aea23bbe8311f86d98d05df56`

Dictamen:

```text
OVERALL_VERDICT = PASS
GROUND_TRUTH_FIDELITY = PASS
SECTION_5_1_ONLY_DIFF = PASS
EN_ES_EQUIVALENCE = PASS
DOCX_OOXML_QA = PASS
FULL_DOCX_RENDER = PASS / 52 OF 52
D035_TIMEOUT_SAFE_HANDOFF = PASS
```

La auditoría confirmó que §5.1 contiene exclusivamente los resultados congelados de composición y controles de partición autorizados por D-087. No se filtraron resultados de candidate retrieval, evidencia documental, explicación, sensibilidades, inferencia, HE2/HE5 ni Discussion.

D-089 abrió el gate autoral exclusivamente para B01 V01:

`article/governance/D089_RESULTS_B01_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@cfba21a2ed00e3bb589a57e8f11184049fe87084`.

## 4. Gate vigente

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_REJECT_OR_REQUEST_CORRECTION_FOR_RESULTS_B01_V01
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V016
CANDIDATE_IF_APPROVED = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V017
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

La aprobación autoral de B01, si ocurre, autorizará únicamente la promoción byte-exacta del candidato aprobado a V017. Hasta esa verificación, V016 permanece canónico.

## 5. Estructura congelada de Results

```text
5.1 Data and partition checks             = PENDING_AUTHOR_APPROVAL
5.2 Candidate retrieval performance       = NOT_AUTHORIZED
5.3 Documentary evidence retrieval        = NOT_AUTHORIZED
5.4 Controlled explanation quality        = NOT_AUTHORIZED
5.5 Sensitivity and robustness analyses   = NOT_AUTHORIZED
5.6 Inferential results                    = NOT_AUTHORIZED
5.7 Summary by research question           = NOT_AUTHORIZED
```

---

# English

## 1. Current state

V016 remains the canonical verified Markdown master. Results B01 / Section 5.1 has been drafted and independently audited by the Managing AI with a PASS verdict but is not yet integrated.

```text
CURRENT_GATE = RESULTS_B01_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
RESULTS_B01 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
TARGET_IF_APPROVED = ARTICLE_MASTER_V017
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The exact candidate identities are frozen above. Author approval is required before any V017 promotion or Results B02 ground-truth gate may begin.