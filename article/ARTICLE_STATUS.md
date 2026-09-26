# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.3
LATEST_EDITORIAL_DECISION = D-054
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
CANONICAL_MASTER = ARTICLE_MASTER_V010
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V010.md
CANONICAL_MASTER_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
APPROVED_B02_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.md
APPROVED_B02_CANDIDATE_MD_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
APPROVED_B02_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_B02_CANDIDATE_DOCX_SHA256 = d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_V011_CANONICAL_INTEGRATION
SECTION_4_3 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
B02_AUTHOR_APPROVAL_GATE = SATISFIED
ARTICLE_MASTER_V011 = AUTHORIZED / NOT_YET_MATERIALIZED
SECTION_4_4 = ELIGIBLE_AFTER_V011_INTEGRATION / NOT_AUTHORIZED
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Jerarquía científica gobernante

El objeto general continúa siendo un **framework configurable para apoyo auditable a la clasificación arancelaria**. La arquitectura de Section 3 es su núcleo técnico:

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

El ranking histórico genera y ordena candidatos. El Top-3 queda fijado antes de la etapa documental. La evidencia documental no altera composición ni orden de candidatos, y el LLM opera downstream para explicación controlada. La arquitectura apoya una decisión; no adjudica autónomamente una clasificación jurídica final.

NANDINA de ocho dígitos, Chapter 87 y el contexto administrativo peruano constituyen la instanciación empírica evaluada, no el alcance conceptual completo del framework. La configurabilidad para otros bancos históricos, espacios de clases, profundidades arancelarias o corpus compatibles no equivale a generalización de desempeño.

### B01 integrado

D-050 verificó la materialización exacta de `ARTICLE_MASTER_V010.md` y cerró Experimental Design B01. Quedaron integrados y congelados:

- los ajustes editoriales controlados en 3.5 y 3.7;
- 4.1 `Experimental setting and scope`;
- 4.2 y 4.2.1–4.2.3;
- el posicionamiento transversal framework vs. instanciación experimental.

### Sincronización externa D-052

La IA Gestora volvió a consultar el `SRC-03` vivo y registró el siguiente corte:

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

Consecuencias editoriales:

- Grupo 6 ya produjo y aprobó tres figuras experimentales y tres captions; quedan pendientes solo de integración editorial cuando se abra Results o el material secundario correspondiente.
- Estas figuras no sustituyen `Figure 1` de Section 3.1, que corresponde a la arquitectura general.
- El cierre de Grupo 6 no abre Results.
- G7-F01 y G7-F02 son dependencias externas administradas por la IA Experimental y no modifican automáticamente el artículo.
- No se reabre contenido científico previamente aprobado.

### Cierre autoral B02 V02 — D-054

La entrega `ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02` superó la auditoría diferencial independiente y fue aprobada expresamente por el autor.

```text
B02_SECTION_4_3_SCIENTIFIC_CONTENT = VERIFIED / PASS / PRESERVED
B02_V02_NARROW_COHERENCE_CORRECTION = PASS
B02_DOCX_QA = PASS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
ARTICLE_MASTER_V011 = AUTHORIZED / NOT_YET_MATERIALIZED
```

Quedan congelados para integración Section 4.3 y las correcciones estrechas autorizadas por D-053. La aprobación no abre Section 4.4 ni posteriores. La promoción canónica exige materializar y verificar el Markdown exacto aprobado como `article/manuscript/ARTICLE_MASTER_V011.md`.

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
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_V011_CANONICAL_INTEGRATION
NEXT_ACTOR = IA_GESTORA / TECHNICAL_INTEGRATION_ONLY
APPROVED_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.md
APPROVED_MD_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
TARGET_CANONICAL_MD = article/manuscript/ARTICLE_MASTER_V011.md
APPROVED_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_DOCX_SHA256 = d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf
SECTION_4_4 = ELIGIBLE_AFTER_INTEGRATION / NOT_AUTHORIZED
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_WRITING_PLAN = V3.3
LATEST_EDITORIAL_DECISION = D-054
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
CANONICAL_MASTER = ARTICLE_MASTER_V010
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_V011_CANONICAL_INTEGRATION
SECTION_4_3 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
B02_AUTHOR_APPROVAL_GATE = SATISFIED
ARTICLE_MASTER_V011 = AUTHORIZED / NOT_YET_MATERIALIZED
SECTION_4_4 = ELIGIBLE_AFTER_V011_INTEGRATION / NOT_AUTHORIZED
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
EXPERIMENTAL_FIGURES_GROUP6 = CLOSED / APPROVED / EDITORIAL_INTEGRATION_DEFERRED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

`ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02` passed independent differential review and was expressly approved by the author. Section 4.3 and the narrow D-053 coherence corrections are frozen for integration. Canonical promotion requires exact materialization and verification of the approved Markdown as `article/manuscript/ARTICLE_MASTER_V011.md`. Section 4.4 and all later scientific blocks remain unauthorized until that integration gate is satisfied.