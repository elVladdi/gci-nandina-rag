# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4
LATEST_EDITORIAL_DECISION = D-062
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
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V03_ONLY
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION
B04_PROMPT_V03 = PASS / ACTIVE / AUTHORIZED
B04_PROMPT_V03_COMMIT = 36f0093f0cdfbd78560f7af6a9e25be6e1f67035
B04_PROMPT_V03_GIT_BLOB = 6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
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

B02/Section 4.3 y B03/Section 4.4 permanecen `CLOSED / APPROVED / FROZEN / INTEGRATED`. `ARTICLE_MASTER_V012.md` es el master canónico. La omisión inicial del DOCX en B03 quedó resuelta antes de la aprobación autoral y no reabre B03.

### Corrección del tramo reciente

La auditoría reforzada `INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02` ratificó V011/V012 y detectó dos defectos persistentes: controles editoriales desfasados y orden incorrecto de onboarding en Prompt B04 V02. D-061 ordenó corregirlos.

Los controles fueron sincronizados. El Prompt B04 V03 fue materializado en:

`article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035`

Git blob:

`6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36`

La revisión interna `5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_PROMPT_V03_INTERNAL_REVIEW_V01.md@f19f2005d6de7b83b649677a7d29ca384765b54b` emitió `PASS`. D-062 autoriza su ejecución y deja V01/V02 como artefactos históricos no ejecutables.

### Sincronización externa registrada

Último corte experimental consumible registrado por el artículo:

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

La IA de Redacción debe consultar SRC-03 y `main` vivos durante B04 y registrar el snapshot observado; un cambio de SHA no bloquea por sí solo si no cambia materialmente los hechos consumidos.

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
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
NEXT_ACTOR = IA_REDACCION
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
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
LATEST_EDITORIAL_DECISION = D-062
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
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V03_ONLY
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION
B04_PROMPT_V03 = PASS / ACTIVE / AUTHORIZED
B04_PROMPT_V03_COMMIT = 36f0093f0cdfbd78560f7af6a9e25be6e1f67035
B04_PROMPT_V03_GIT_BLOB = 6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Governing scientific hierarchy

The general object remains a **configurable framework for auditable tariff-classification decision support**. Section 3 remains its technical core. Historical retrieval generates and orders candidates; the Top-3 is frozen before documentary and generative stages; documentary evidence is associated with already fixed candidates without changing composition/order; and the local LLM operates downstream for controlled explanation without classification feedback.

Eight-digit NANDINA, Chapter 87, and the Peruvian administrative context are the evaluated empirical instantiation, not the full conceptual scope of the framework. Configurability is not empirical performance generalization.

### B02 and B03 state

B02/Section 4.3 and B03/Section 4.4 remain `CLOSED / APPROVED / FROZEN / INTEGRATED`. `ARTICLE_MASTER_V012.md` is canonical. The initial B03 DOCX omission was closed before author approval and does not reopen B03.

### Recent correction

The reinforced `INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02` ratified V011/V012 and identified stale control files plus a B04 V02 onboarding-order defect. D-061 required correction. The controls were synchronized, Prompt B04 V03 was materialized at `article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035` with blob `6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36`, and the internal prompt review at `f19f2005d6de7b83b649677a7d29ca384765b54b` returned `PASS`. D-062 authorizes V03 execution and leaves V01/V02 historical and non-executable.

### Registered external synchronization

The last experimental cut registered as consumable by the article remains SRC-03 HEAD `87422102290a4f9a89c51e936cf7274d8e4687d8`, plan blob `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`, and development `main@db0d0ad0d8435921a7838db6720eaea86a263763`. The Drafting AI must re-read live SRC-03/main during B04 and record the observed snapshot; SHA drift alone is not a blocker when the consumed facts are materially unchanged.

### Mandatory scientific boundaries

The distinctions among literature gap, project feature, contribution, result, novelty, framework scope, empirical testbed, candidate retrieval, global accuracy, normative association, substantive correctness, auditability, legal correctness, configurability, generalization, and the frozen EXP11A/EXP11B/EXP12 interpretations remain binding. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED`.

### Current gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
NEXT_ACTOR = DRAFTING_AI
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```