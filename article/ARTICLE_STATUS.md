# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED / RESTRUCTURED_BY_D014
KBS_EMPIRICAL_WRITING_GUIDE = KBS_EWG_34_V01 / AUTHOR_APPROVED / ACTIVE / BINDING
ARTICLE_WRITING_PLAN = V2.8
STRUCTURE_APPROVAL_DECISION = D-015
RELATED_WORK_CLOSURE_DECISION = D-025
EXPERIMENTAL_RECONCILIATION_DECISION = D-030
INTRODUCTION_APPROVAL_DECISION = D-031
INTRODUCTION_INTEGRATION_DECISION = D-033
G6_G7_RECONCILIATION_DECISION = D-034
DOCX_CUSTODY_DECISION = D-021 / D-027 / D-029 / D-033
GITHUB_ONLY_RESPONSE_DECISION = D-022
TECHNICAL_CLOSURE_MODE_DECISION = D-023
LATEST_EDITORIAL_DECISION = D-034
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01_V02 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V007
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
CANONICAL_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
CANONICAL_MASTER_DOCX = LOCAL_AUTHOR_CUSTODY / D033
CANONICAL_MASTER_DOCX_SOURCE_FILENAME = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx
CANONICAL_MASTER_DOCX_REPOSITORY_UPLOAD = DEFERRED_BY_D021
CANONICAL_MASTER_DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = DECISION_SUPPORT ARCHITECTURE
CURRENT_GATE = ARCHITECTURE_B01
AUTHORIZED_SCOPE = SECTIONS_3_1_TO_3_4_ONLY
DECISION_SUPPORT_ARCHITECTURE = AUTHORIZED / ACTIVE
ARCHITECTURE_B01 = AUTHORIZED / DRAFTING_PENDING
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Estructura aprobada

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

### Secciones cerradas

- Related Work 2.1–2.6: `APPROVED / FROZEN / INTEGRATED`.
- Introduction B01 V02: `APPROVED / FROZEN / INTEGRATED` mediante D-033.
- Master canónico actual: `ARTICLE_MASTER_V007.md`.

La Introduction aprobada fija el problema, la limitación operacional/evaluativa, la arquitectura de alto nivel, las tres contribuciones acotadas, el testbed como instanciación y RQ1–RQ4. No declara novelty absoluta, ausencia universal, SOTA, generalización empírica ni corrección jurídica.

### Fronteras científicas obligatorias

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`.
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`.
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`.
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`.
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.

### Estado experimental consumible

```text
EXPERIMENTAL_PLAN_BRANCH = docs/plan-maestro-temporal-2026-08-31
EXPERIMENTAL_PLAN_HEAD = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
EXPERIMENTAL_PLAN_BLOB = 9b388fe8cc19fce86ec3c15853e73899cb3e5666
EXPERIMENTAL_MAIN_CHECKPOINT = ca065618d5df0019f76ef5a971e858d91c263e1f
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F03_EXTERNAL_REAUDIT = PASS
G4_F03_COMPARISON_REGISTRY_COUNT = 11
G4_F03_AUTHORIZED_DISCUSSION_POINT_COUNT = 8
G4_F03_FORBIDDEN_DISCUSSION_POINT_COUNT = 14
GROUP5 = CLOSED / APPROVED
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5_CANONICAL_TABLE_COUNT = 9
GROUP6 = NOT_STARTED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7 = PROSPECTIVE / NOT_ACTIVATED
GROUP8 = PROSPECTIVE / NOT_ACTIVATED
```

### Reconciliación G6/G7 — D-034

La revisión directa de las fichas G6/G7 y el dictamen metodológico de la IA Experimental son concordantes: el cierre de Grupo 6 es precondición para **activar formalmente Grupo 7**, no para redactar progresivamente Architecture o Experimental design bajo la gobernanza del artículo.

```text
GROUP6_CLOSE_REQUIRED_FOR_FORMAL_G7_ACTIVATION = YES
GROUP6_CLOSE_REQUIRED_FOR_ARCHITECTURE_DRAFTING = NO
GROUP6_CLOSE_REQUIRED_FOR_EXPERIMENTAL_DESIGN_DRAFTING = NO
FORMAL_G7_ACTIVATION_BEFORE_GROUP6_CLOSE = NOT_PERMITTED
G7_F03_ROLE = SYNCHRONIZATION_AND_TRANSVERSAL_CLOSURE
G7_F03_ROLE_IS_ARTICLE_INCEPTION = false
GROUP7_CLOSE_REQUIRED_BEFORE_GROUP8 = YES
SCIENTIFIC_FINAL_FREEZE_REQUIRES_GROUP8 = true
```

La selección/numeración final de figuras, captions, referencias cruzadas y pasajes finales de Results/Discussion dependientes de esas figuras permanecen provisionales hasta Grupo 6. D-034 no autoriza G6, G7 ni G8.

### Bloque activo — Architecture B01

```text
BLOCK = ARCHITECTURE_B01
SECTION = 3.1–3.4
DRAFTING = AUTHORIZED
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
BASELINE_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx
BASELINE_DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
PRIOR_INTRODUCTION_AND_RELATED_WORK = APPROVED / FROZEN / PRESERVE_EXACTLY
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

B01 debe redactar exclusivamente:

- 3.1 vista general y flujo de información;
- 3.2 representación y normalización de consulta;
- 3.3 recuperación histórica y ranking de candidatos;
- 3.4 conjunto fijo de candidatos.

Debe describir la arquitectura general antes del testbed. No debe abrir con NANDINA, Clase/Capítulo 87, H100, tamaños de datasets o resultados. Debe preservar la separación `historical ranking → fixed Top-3 → downstream stages` y dejar la recuperación normativa, construcción de contexto, LLM y configurabilidad detallada para el bloque posterior.

### Gate vigente

```text
CURRENT_GATE = ARCHITECTURE_B01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ARCHITECTURE_B01_ONLY
MASTER_INTEGRATION = ARTICLE_MASTER_V007 / ACTIVE_BASELINE
ARCHITECTURE_B01 = AUTHORIZED
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FIGURES = NOT_AUTHORIZED
GROUP6 = NOT_STARTED / NOT_AUTHORIZED_BY_ARTICLE
GROUP7 = NOT_ACTIVATED
GROUP8 = NOT_ACTIVATED
```

---

## English

### General state

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_WRITING_PLAN = V2.8
LATEST_EDITORIAL_DECISION = D-034
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01_V02 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V007
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
CANONICAL_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = DECISION SUPPORT ARCHITECTURE
CURRENT_GATE = ARCHITECTURE_B01
AUTHORIZED_SCOPE = SECTIONS_3_1_TO_3_4_ONLY
DECISION_SUPPORT_ARCHITECTURE = AUTHORIZED / ACTIVE
ARCHITECTURE_B01 = AUTHORIZED / DRAFTING_PENDING
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Related Work 2.1–2.6 and Introduction B01 V02 are closed, approved, frozen, and integrated. `ARTICLE_MASTER_V007` is the canonical cumulative master. The approved Introduction preserves the bounded functional separation and does not declare absolute novelty, universal prior-art absence, SOTA, empirical generalization, or legal correctness.

The consumable experimental cutoff remains Master Plan HEAD `98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e`, blob `9b388fe8cc19fce86ec3c15853e73899cb3e5666`, and experimental `main@ca065618d5df0019f76ef5a971e858d91c263e1f`. Groups 3–5 are closed/approved; `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE`; Group 6 remains not started and G6-F01 is only eligible/unauthorized/unexecuted.

D-034 reconciles G6/G7 with the article workflow. Group 6 closure is required for formal Group 7 activation, but not for Architecture or later Experimental-design drafting under their own editorial gates. G7-F03 is synchronization/transversal closure rather than article inception; Group 8 is required for final scientific-freeze readiness. Final figures/captions/cross-references and figure-dependent final Results/Discussion prose remain provisional until Group 6 closes. D-034 does not authorize G6, G7, or G8.

Architecture B01 is the only active drafting block. It covers Sections 3.1–3.4: overview/information flow, query representation/normalization, historical candidate retrieval/ranking, and fixed candidate set. It must describe the general architecture before the empirical testbed and must preserve all approved Introduction/Related Work text and all 40 inherited citation comments. Architecture B02, Experimental design, Results, Discussion, and figures remain unauthorized.

```text
CURRENT_GATE = ARCHITECTURE_B01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ARCHITECTURE_B01_ONLY
MASTER_INTEGRATION = ARTICLE_MASTER_V007 / ACTIVE_BASELINE
```