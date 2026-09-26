# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4 / OPERATIONAL_SYNC_PENDING_BEFORE_B05
LATEST_EDITORIAL_DECISION = D-064
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = V02_DIFFERENTIAL_PASS / PENDING_AUTHOR_APPROVAL / NOT_INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_AUTHOR_APPROVAL
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = DIFFERENTIAL_PASS / PENDING_AUTHOR_APPROVAL / NOT_INTEGRATED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
B04_V02_SECTION = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
B04_V02_SECTION_GIT_BLOB = fa6e9325a5acd6bf480cdbe90a467855cf877f1d
B04_V02_CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
B04_V02_CANDIDATE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
B04_V02_CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
B04_V02_DIFFERENTIAL_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01.md@1cb3e2c865d44bbffb2481185ded6df8bf9abc54
EXPERIMENTAL_REVIEW = NOT_REQUIRED
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Jerarquía científica gobernante

El objeto general continúa siendo un **framework configurable para apoyo auditable a la clasificación arancelaria**. La arquitectura de Section 3 sigue siendo su núcleo técnico:

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

La recuperación histórica genera y ordena candidatos. El Top-3 queda fijado antes de la etapa documental y generativa. La evidencia documental se asocia a candidatos ya fijados y no altera composición ni orden. El LLM local opera downstream para explicación controlada; no clasifica desde cero, no introduce códigos externos y no retroalimenta el ranking.

NANDINA de ocho dígitos, Chapter 87 y el contexto administrativo peruano son la instanciación empírica evaluada, no el alcance conceptual completo del framework. La configurabilidad para otros bancos históricos, espacios de clases, profundidades arancelarias, jurisdicciones o corpus compatibles no equivale a generalización empírica de desempeño.

### Estado de B02 y B03

B02/Section 4.3 y B03/Section 4.4 permanecen `CLOSED / APPROVED / FROZEN / INTEGRATED`. `ARTICLE_MASTER_V012.md` continúa siendo el master canónico hasta que exista aprobación autoral e integración técnica de B04 V02.

### Estado de B04 V02

B04 V01 fue auditado y requirió exclusivamente B04-C01 y B04-C02. La IA de Redacción ejecutó esas correcciones en B04 V02. La auditoría diferencial independiente de la IA Gestora está versionada en:

`article/reviews/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01.md@1cb3e2c865d44bbffb2481185ded6df8bf9abc54`

El dictamen es `PASS`. Se verificaron las identidades exactas del Markdown y DOCX candidatos, las cuatro sustituciones EN/ES autorizadas y ninguna mutación adicional. El DOCX conserva 40 comentarios/anclajes, cero tracked changes y todos los miembros OOXML fuera de `word/document.xml` permanecen byte-idénticos al baseline B04 V01. El cambio de 44 a 45 páginas corresponde a reflujo de layout por las sustituciones autorizadas y no a contenido adicional.

D-064 abre exclusivamente el gate de aprobación del autor. No existe autorización de integración ni de B05 hasta que el autor apruebe expresamente B04 V02.

### Sincronización externa registrada

Último corte experimental consumido y re-verificado durante B04:

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

B04 V02 no modifica hechos experimentales; `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

### Fronteras científicas obligatorias

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.
- `FRAMEWORK_GENERAL_SCOPE ≠ NANDINA_CHAPTER87_TESTBED`.
- `ARCHITECTURE = TECHNICAL_CORE_OF_FRAMEWORK`.
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`.
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`.
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.

### Gate vigente

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
AUTHOR_ACTION = APPROVE_OR_REJECT_B04_V02
CANDIDATE_SECTION = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md / LOCAL_AUTHOR_CUSTODY
CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANDIDATE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_MASTER = ARTICLE_MASTER_V012
INTEGRATION = NOT_AUTHORIZED_UNTIL_EXPRESS_AUTHOR_APPROVAL
B05 = NOT_AUTHORIZED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

`ARTICLE_WRITING_PLAN.md` V3.4 conserva todavía el gate operativo anterior a D-063. D-064 y este estado gobiernan mientras se realiza su sincronización; el Plan debe quedar actualizado antes de cualquier autorización de B05.

---

## English

### General state

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4 / OPERATIONAL_SYNC_PENDING_BEFORE_B05
LATEST_EDITORIAL_DECISION = D-064
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = V02_DIFFERENTIAL_PASS / PENDING_AUTHOR_APPROVAL / NOT_INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_AUTHOR_APPROVAL
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = DIFFERENTIAL_PASS / PENDING_AUTHOR_APPROVAL / NOT_INTEGRATED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
B04_V02_SECTION = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
B04_V02_SECTION_GIT_BLOB = fa6e9325a5acd6bf480cdbe90a467855cf877f1d
B04_V02_CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
B04_V02_CANDIDATE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
B04_V02_CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
B04_V02_DIFFERENTIAL_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01.md@1cb3e2c865d44bbffb2481185ded6df8bf9abc54
EXPERIMENTAL_REVIEW = NOT_REQUIRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Governing scientific hierarchy

The general object remains a **configurable framework for auditable tariff-classification decision support**. Section 3 remains its technical core. Historical retrieval generates and orders candidates; the Top-3 is frozen before documentary and generative stages; documentary evidence is associated with already fixed candidates without changing composition/order; and the local LLM operates downstream for controlled explanation without classification feedback.

Eight-digit NANDINA, Chapter 87, and the Peruvian administrative context are the evaluated empirical instantiation, not the full conceptual scope of the framework. Configurability is not empirical performance generalization.

### B02 and B03 state

B02/Section 4.3 and B03/Section 4.4 remain `CLOSED / APPROVED / FROZEN / INTEGRATED`. `ARTICLE_MASTER_V012.md` remains canonical until B04 V02 receives express author approval and technical integration.

### B04 V02 state

B04 V01 required only B04-C01 and B04-C02. The Drafting AI executed those corrections in B04 V02. The independent differential review is versioned at `article/reviews/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01.md@1cb3e2c865d44bbffb2481185ded6df8bf9abc54` and returned `PASS`.

The exact candidate identities were verified, the Markdown contains only the four authorized EN/ES substitutions, the DOCX preserves 40 inherited comment anchors and zero tracked changes, and all OOXML members other than `word/document.xml` remain byte-identical to the B04 V01 baseline. The 44→45 page change is accepted as authorized layout reflow, not additional content.

D-064 opens only the author-approval gate. Integration and B05 remain unauthorized until express author approval.

### Current external synchronization

B04 consumed and re-verified SRC-03 HEAD `87422102290a4f9a89c51e936cf7274d8e4687d8`, plan blob `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`, and development `main@db0d0ad0d8435921a7838db6720eaea86a263763`. B04 V02 does not alter experimental facts; `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

### Mandatory scientific boundaries

The distinctions among literature gap, project feature, contribution, result, novelty, framework scope, empirical testbed, candidate retrieval, global accuracy, normative association, substantive correctness, auditability, legal correctness, configurability, generalization, and the frozen EXP11A/EXP11B/EXP12 interpretations remain binding. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED`.

### Current gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
AUTHOR_ACTION = APPROVE_OR_REJECT_B04_V02
CANDIDATE_SECTION = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md / LOCAL_AUTHOR_CUSTODY
CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANDIDATE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_MASTER = ARTICLE_MASTER_V012
INTEGRATION = NOT_AUTHORIZED_UNTIL_EXPRESS_AUTHOR_APPROVAL
B05 = NOT_AUTHORIZED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

`ARTICLE_WRITING_PLAN.md` V3.4 still carries the pre-D-063 operational gate. D-064 and this status govern until it is synchronized; the plan must be updated before any B05 authorization.
