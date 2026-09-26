# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4
LATEST_EDITORIAL_DECISION = D-061
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = ELIGIBLE / EXECUTION_BLOCKED_UNTIL_B04_PROMPT_V03
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION / PROCEDURAL_ONBOARDING_ORDER_DEFECT
B04_PROMPT_V03 = REQUIRED / NOT_YET_MATERIALIZED
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
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

NANDINA de ocho dígitos, Chapter 87 y el contexto administrativo peruano son la **instanciación empírica** evaluada, no el alcance conceptual completo del framework. La configurabilidad para otros bancos históricos, espacios de clases, profundidades arancelarias, jurisdicciones o corpus compatibles no equivale a generalización empírica de desempeño.

### Cierre de B02 y B03

D-055 cerró e integró B02/Section 4.3 mediante la promoción byte-exacta de `ARTICLE_MASTER_V011.md`.

D-057 registró la aprobación autoral de B03. D-058 verificó la promoción byte-exacta del candidato B03 y estableció `ARTICLE_MASTER_V012.md` como master canónico. Quedan por tanto congeladas e integradas:

- Section 4.3 `Documentary corpus and evidence resource`;
- Section 4.4 `Partition validity and dependence controls`;
- sus espejos españoles;
- el DOCX acumulativo B03 bajo custodia local del autor.

La omisión inicial del DOCX en el primer prompt B03 fue cerrada mediante microgate técnico antes de la aprobación autoral. No se reabre B03.

### Reauditoría del tramo reciente

`article/reviews/INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02.md` confirmó:

- B02/4.3 y B03/4.4 no requieren reapertura científica;
- V011 y V012 permanecen válidos;
- D-059 y B04 Prompt V01 redujeron indebidamente 4.5 al subproblema de recuperación histórica y quedaron superseded;
- B04 Prompt V02 corrigió el alcance científico sustancial, pero mantuvo un defecto procedimental en el orden de onboarding;
- `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` debían sincronizarse antes de una ejecución B04 válida.

D-061 gobierna la corrección actual. El siguiente prompt válido debe ser B04 V03, autosuficiente, con el orden exacto de onboarding y con todo el alcance científico y las obligaciones acumulativas válidas preservadas.

### Sincronización externa vigente

Último corte experimental consumible registrado por el artículo:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
GROUP6 = CLOSED / APPROVED
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_CLOSURE_COMMIT = e93b44164a9619dad1f527a3b2d4479265858e39
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F01_CLOSURE_COMMIT = db0d0ad0d8435921a7838db6720eaea86a263763
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

Estos grupos son dependencias externas administradas por la IA Experimental. Su avance no abre automáticamente Results ni modifica un gate editorial local.

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
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
NEXT_ACTOR = IA_GESTORA
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
SECTION_4_5 = ELIGIBLE / BLOCKED_UNTIL_PROMPT_V03_MATERIALIZATION
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

### General state

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4
LATEST_EDITORIAL_DECISION = D-061
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = ELIGIBLE / EXECUTION_BLOCKED_UNTIL_B04_PROMPT_V03
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION / PROCEDURAL_ONBOARDING_ORDER_DEFECT
B04_PROMPT_V03 = REQUIRED / NOT_YET_MATERIALIZED
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Governing scientific hierarchy

The general object remains a **configurable framework for auditable tariff-classification decision support**. Section 3 remains its technical core:

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

Historical retrieval generates and orders candidates. The Top-3 is frozen before documentary and generative stages. Documentary evidence is associated with already fixed candidates and does not alter their composition or order. The local LLM operates downstream for controlled explanation; it does not classify from scratch, introduce external codes, or feed back into the ranking.

Eight-digit NANDINA, Chapter 87, and the Peruvian administrative context are the evaluated **empirical instantiation**, not the full conceptual scope of the framework. Configurability for other historical banks, class spaces, tariff depths, jurisdictions, or compatible corpora is not evidence of empirical performance generalization.

### B02 and B03 closure

D-055 closed and integrated B02/Section 4.3 through byte-exact promotion of `ARTICLE_MASTER_V011.md`.

D-057 recorded author approval of B03. D-058 verified byte-exact promotion of the B03 candidate and established `ARTICLE_MASTER_V012.md` as the canonical master. Section 4.3, Section 4.4, their Spanish mirrors, and the cumulative B03 DOCX are therefore frozen and integrated.

The initial DOCX omission in the first B03 prompt was closed through a technical microgate before author approval. B03 is not reopened.

### Recent-interval re-audit

`article/reviews/INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02.md` confirmed that B02/4.3 and B03/4.4 require no scientific reopening and that V011/V012 remain valid. It also confirmed that D-059 and B04 Prompt V01 improperly narrowed Section 4.5 and were superseded; B04 Prompt V02 substantially corrected the scientific scope but retained a procedural onboarding-order defect; and both `ARTICLE_STATUS.md` and `ARTICLE_WRITING_PLAN.md` required synchronization before a valid B04 execution.

D-061 governs the current correction. The next valid drafting contract must be a self-contained B04 Prompt V03 using the exact onboarding order while preserving all valid scientific scope and cumulative obligations.

### Current external synchronization

The latest experimental cut registered as consumable by the article remains:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
GROUP6 = CLOSED / APPROVED
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_CLOSURE_COMMIT = e93b44164a9619dad1f527a3b2d4479265858e39
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F01_CLOSURE_COMMIT = db0d0ad0d8435921a7838db6720eaea86a263763
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

These groups remain external dependencies managed by the Experimental AI. Their progress does not automatically open Results or alter a local editorial gate.

### Mandatory scientific boundaries

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

### Current gate

```text
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
NEXT_ACTOR = MANAGING_AI
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
SECTION_4_5 = ELIGIBLE / BLOCKED_UNTIL_PROMPT_V03_MATERIALIZATION
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```