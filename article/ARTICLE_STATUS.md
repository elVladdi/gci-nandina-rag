# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4
LATEST_EDITORIAL_DECISION = D-063
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = V01_EXECUTED / NARROW_CORRECTION_REQUIRED
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_NARROW_PRECISION_CORRECTION
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = SCIENTIFIC_SCOPE_PASS / TWO_NARROW_PRECISION_CORRECTIONS_REQUIRED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION
B04_PROMPT_V03 = EXECUTED / SUPERSEDED_BY_CORRECTION_GATE
B04_CORRECTION_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_V01_NARROW_PRECISION_CORRECTION.md@6432e884a632e1884926ee35ffaae3c2b882fb87
B04_V01_CANDIDATE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
B04_V01_CANDIDATE_MD_GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676
B04_V01_CANDIDATE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = SUSPENDED_UNTIL_B04_V02_CORRECTION_VERIFIED
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

### Estado de B04 V01

B04 V01 fue ejecutado bajo el Prompt V03 y entregó section artifact, master Markdown candidato y DOCX acumulativo candidato. La auditoría independiente de la IA Gestora está versionada en:

`article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md@09ed0ec3a42549522942f5252f0b78713bb94524`

La auditoría verificó alcance científico, trazabilidad primaria, equivalencia EN/ES, diferencial Markdown, integridad OOXML, 40 comentarios/anclajes heredados y cero tracked changes. No se requiere revisión de IA Experimental.

D-063 autoriza únicamente dos correcciones estrechas de precisión:

- B04-C01: distinguir el banco H100 de 2,950 registros y `history_depth=2950` de la materialización efectiva de scores para coincidencias léxicas;
- B04-C02: describir condicionalmente el match documental NANDINA-8 para no anticipar en Methods el outcome observado de cobertura exacta de Phase F.

No se autoriza reescritura general de 4.5. El gate de aprobación autoral permanece suspendido hasta verificar B04 V02.

### Corrección del tramo reciente

La auditoría reforzada `INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02` ratificó V011/V012 y detectó controles editoriales desfasados y un defecto de onboarding en Prompt B04 V02. D-061 ordenó corregirlos. El Prompt B04 V03 fue materializado, auditado con PASS y autorizado por D-062. D-063 gobierna ahora exclusivamente el microgate correctivo posterior a la ejecución de B04 V01.

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

La corrección B04 V02 no modifica hechos experimentales; por ello `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

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
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_NARROW_PRECISION_CORRECTION
NEXT_ACTOR = IA_REDACCION
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_V01_NARROW_PRECISION_CORRECTION.md@6432e884a632e1884926ee35ffaae3c2b882fb87
BASELINE_SECTION = article/sections/experimental_design/Experimental_Design_B04_V01.md@ade9d022663458d7bbe5aee939e1d7899365a7c8
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md / LOCAL_AUTHOR_CUSTODY
BASELINE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
BASELINE_MD_GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx / LOCAL_AUTHOR_CUSTODY
BASELINE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_DIFFERENTIAL_AUDIT
AUTHOR_APPROVAL_GATE = SUSPENDED
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
LATEST_EDITORIAL_DECISION = D-063
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = V01_EXECUTED / NARROW_CORRECTION_REQUIRED
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_NARROW_PRECISION_CORRECTION
SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = SCIENTIFIC_SCOPE_PASS / TWO_NARROW_PRECISION_CORRECTIONS_REQUIRED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = SUSPENDED_UNTIL_B04_V02_CORRECTION_VERIFIED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Governing scientific hierarchy

The general object remains a **configurable framework for auditable tariff-classification decision support**. Section 3 remains its technical core. Historical retrieval generates and orders candidates; the Top-3 is frozen before documentary and generative stages; documentary evidence is associated with already fixed candidates without changing composition/order; and the local LLM operates downstream for controlled explanation without classification feedback.

Eight-digit NANDINA, Chapter 87, and the Peruvian administrative context are the evaluated empirical instantiation, not the full conceptual scope of the framework. Configurability is not empirical performance generalization.

### B02 and B03 state

B02/Section 4.3 and B03/Section 4.4 remain `CLOSED / APPROVED / FROZEN / INTEGRATED`. `ARTICLE_MASTER_V012.md` is canonical. The initial B03 DOCX omission was closed before author approval and does not reopen B03.

### B04 V01 state

B04 V01 was executed under Prompt V03 and delivered the section artifact plus cumulative Markdown and DOCX candidates. The independent Managing-AI audit is versioned at `article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md@09ed0ec3a42549522942f5252f0b78713bb94524`. It verified scientific scope, primary-source traceability, EN/ES equivalence, Markdown differential integrity, OOXML integrity, preservation of all 40 inherited comment anchors, and zero tracked changes. Experimental-AI review is not required.

D-063 authorizes only two narrow precision corrections: B04-C01 distinguishes the 2,950-record H100 bank and configured `history_depth=2950` from the score dictionary's materialized lexical matches; B04-C02 makes exact NANDINA-8 documentary matching conditional so Methods does not anticipate Phase-F exact-coverage outcomes. No general rewrite of Section 4.5 is authorized.

### Current external synchronization

B04 consumed and re-verified SRC-03 HEAD `87422102290a4f9a89c51e936cf7274d8e4687d8`, plan blob `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`, and development `main@db0d0ad0d8435921a7838db6720eaea86a263763`. The B04 V02 correction does not alter experimental facts; `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

### Mandatory scientific boundaries

The distinctions among literature gap, project feature, contribution, result, novelty, framework scope, empirical testbed, candidate retrieval, global accuracy, normative association, substantive correctness, auditability, legal correctness, configurability, generalization, and the frozen EXP11A/EXP11B/EXP12 interpretations remain binding. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED`.

### Current gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_NARROW_PRECISION_CORRECTION
NEXT_ACTOR = DRAFTING_AI
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_V01_NARROW_PRECISION_CORRECTION.md@6432e884a632e1884926ee35ffaae3c2b882fb87
BASELINE_SECTION = article/sections/experimental_design/Experimental_Design_B04_V01.md@ade9d022663458d7bbe5aee939e1d7899365a7c8
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md / LOCAL_AUTHOR_CUSTODY
BASELINE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
BASELINE_MD_GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx / LOCAL_AUTHOR_CUSTODY
BASELINE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_DIFFERENTIAL_AUDIT
AUTHOR_APPROVAL_GATE = SUSPENDED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```