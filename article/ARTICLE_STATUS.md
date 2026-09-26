# Estado del artículo / Article Status

## Español

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4
LATEST_EDITORIAL_DECISION = D-065
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_5 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
APPROVED_B04_SECTION = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
APPROVED_B04_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md / LOCAL_AUTHOR_CUSTODY
APPROVED_B04_CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
APPROVED_B04_CANDIDATE_MD_GIT_BLOB_EXPECTED = 06beaa052e2f1bcc630647040762fe78d3838a62
APPROVED_B04_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_B04_CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V013
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V013_CANONICAL_INTEGRATION
ARTICLE_MASTER_V013 = AUTHORIZED / NOT_YET_VERIFIED_AS_MATERIALIZED
SECTION_4_6 = ELIGIBLE_AFTER_V013_INTEGRATION_AND_GROUND_TRUTH_SYNC / NOT_AUTHORIZED
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = SATISFIED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_B04_V02
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Estado científico y editorial

B02/Section 4.3 y B03/Section 4.4 permanecen `CLOSED / APPROVED / FROZEN / INTEGRATED`.

B04/Section 4.5 superó la auditoría científica inicial, ejecutó únicamente las correcciones estrechas B04-C01 y B04-C02 y superó la auditoría diferencial independiente registrada en `article/reviews/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01.md@1cb3e2c865d44bbffb2481185ded6df8bf9abc54`. El autor aprobó expresamente B04 V02. D-065 congela la versión y autoriza su promoción byte-exacta a `ARTICLE_MASTER_V013.md`.

La promoción todavía no se considera cerrada mientras GitHub no exponga `article/manuscript/ARTICLE_MASTER_V013.md` con Git blob `06beaa052e2f1bcc630647040762fe78d3838a62`. Hasta entonces `ARTICLE_MASTER_V012.md` continúa siendo el master canónico. No se permite reconstruir el candidato para realizar la promoción.

El DOCX aprobado B04 V02 permanece bajo custodia local del autor y será el baseline Word acumulativo de B05 después del cierre de V013. Conserva 40 comentarios heredados y cero tracked changes.

### Jerarquía científica gobernante

```text
commercial description
→ normalization
→ historical retrieval
→ historical Top-k ranking
→ fixed Top-3
→ candidate-specific documentary/normative evidence
→ evidence-context construction
→ local LLM
→ controlled explanation of the fixed Top-3
```

- historical retrieval genera/ordena candidatos;
- documentary/normative evidence no modifica el Top-3;
- el LLM local es downstream y solo explica el ranking fijado;
- `candidate retrieval ≠ overall classification accuracy`;
- `normative association ≠ substantive normative correctness`;
- `auditability ≠ legal correctness`;
- `configurability ≠ empirical generalization`;
- SERIE es unidad de análisis y DAM/declaración unidad de agrupamiento cuando la dependencia es relevante;
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`;
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`;
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`;
- `FINAL_GAP = NOT_DEFINED`;
- `NOVELTY = NOT_DECLARED`.

### Sincronización experimental registrada

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
GROUP6 = CLOSED / APPROVED
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

Este corte deberá reconstruirse contra el estado vivo antes de abrir B05/Section 4.6; su avance no abre automáticamente un gate editorial.

### Gate vigente

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V013_CANONICAL_INTEGRATION
NEXT_ACTION = MATERIALIZE_AND_VERIFY_ARTICLE_MASTER_V013
TARGET_PATH = article/manuscript/ARTICLE_MASTER_V013.md
EXPECTED_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
EXPECTED_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V012
B05 / SECTION_4_6 = NOT_AUTHORIZED_UNTIL_V013_INTEGRATION_AND_GROUND_TRUTH_SYNC
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4
LATEST_EDITORIAL_DECISION = D-065
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_5 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
CANONICAL_MASTER = ARTICLE_MASTER_V012
APPROVED_B04_CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
APPROVED_B04_CANDIDATE_MD_GIT_BLOB_EXPECTED = 06beaa052e2f1bcc630647040762fe78d3838a62
APPROVED_B04_CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V013
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V013_CANONICAL_INTEGRATION
ARTICLE_MASTER_V013 = AUTHORIZED / NOT_YET_VERIFIED_AS_MATERIALIZED
SECTION_4_6 = ELIGIBLE_AFTER_V013_INTEGRATION_AND_GROUND_TRUTH_SYNC / NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = SATISFIED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

B04 V02 passed independent differential audit and then received explicit author approval. D-065 freezes Section 4.5 and authorizes exact-byte promotion of the approved cumulative Markdown candidate to `article/manuscript/ARTICLE_MASTER_V013.md`. Promotion is not closed until GitHub exposes the expected blob `06beaa052e2f1bcc630647040762fe78d3838a62`; until then V012 remains canonical. The approved B04 V02 DOCX remains in local author custody and becomes the Word baseline for B05 only after V013 integration. Section 4.6 and Results remain unauthorized.