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
ARTICLE_WRITING_PLAN = V2.1
STRUCTURE_RESET_DECISION = D-014
STRUCTURE_APPROVAL_DECISION = D-015
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
WORD_BASELINE = KBS_ARTICLE_WORKING_STRUCTURE_V01.docx
WORD_BASELINE_SHA256 = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
METHODS_B01_V05 = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
CURRENT_DRAFTING_PHASE = RELATED_WORK
RELATED_WORK_B01 = AUTHORIZED
AUTHORIZED_SCOPE = SECTION_2.1_ONLY
NEXT_ACTOR = DRAFTING_AI
```

### Fases previas

- `0A — Ground truth documental y experimental`: **CLOSED / APPROVED**.
- `0B — Mapa crítico de literatura y taxonomía`: **CLOSED / APPROVED / FROZEN**.
- `0C — Posicionamiento científico y Research Questions`: **CLOSED / APPROVED / FROZEN**.
- `0D-1 / 0D-2`: **CLOSED / APPROVED / FROZEN**; su arquitectura de secciones/orden de redacción fue supersedida controladamente por D-014.
- `KBS_EWG_34_V01`: **AUTHOR_APPROVED / ACTIVE / BINDING**.
- `KBS_ARTICLE_WORKING_STRUCTURE_V01`: **AUTHOR_APPROVED / FROZEN_FOR_DRAFTING** mediante D-015.

D-014/D-015 no modifican alcance científico, RQs, Claim–Evidence Matrix, diseño experimental ni gobernanza del Plan Maestro.

### Methods B01 legado

```text
METHODS_B01_V05_INTERNAL_REVIEW = PASS / HISTORICAL
METHODS_B01_V05_AUTHOR_APPROVAL = NOT_GRANTED
METHODS_B01_V05_STATUS = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
MASTER_INTEGRATION_OF_V05 = PROHIBITED
```

La V05 no se corregirá ni reutilizará automáticamente. La nueva arquitectura separa problema/posicionamiento, arquitectura general e instanciación experimental.

### Estructura aprobada

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

`Limitations` permanece integrada como `6.6 Limitations` salvo futura enmienda explícita.

### Orden de redacción activo

`Related Work → Introduction provisional → Decision-support architecture → Experimental design → Results autorizados → figures/tables → integración de resultados pendientes → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → adaptación final KBS`.

El antiguo orden `Methods → Related Work → ... → Introduction` permanece `SUPERSEDED`.

### Bloque activo

```text
CURRENT_GATE = RELATED_WORK_B01_DRAFTING
BLOCK = RELATED_WORK_B01
SECTION = 2.1 Automated tariff classification and candidate retrieval
BLOCK_REVISION = V01
DRAFTING = AUTHORIZED
SECTIONS_2_2_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_UNLESS_NEW_TRIGGER_APPEARS
```

El bloque debe redactarse dentro de la base acumulativa aprobada. Si la IA de Redacción no puede acceder al Word exacto con SHA-256 registrado, debe detenerse con `BASELINE_DOCX_ACCESS_REQUIRED`; no puede reconstruirlo silenciosamente.

### Gobernanza editorial

```text
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
SPCCR_VERSION = 1.0
SPCCR_STATUS = AUTHOR_APPROVED / ACTIVE
KBS_EMPIRICAL_WRITING_GUIDE = KBS_EWG_34_V01
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
PUBLICATION_ROUTE_TARGET_A = SUBSCRIPTION
PAID_OPEN_ACCESS = NOT_SELECTED
APC_PAYMENT_PLANNED = NO
```

La guía KBS-34 gobierna prosa, organización retórica, densidad, visibilidad de contribución y presentación metodológica. Los 34 artículos son evidencia editorial y no fuentes científicas automáticas.

### Estado científico preservado

```text
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Fronteras obligatorias:

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`;
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`;
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`;
- `JOURNAL_FIT ≠ NOVELTY_PROOF`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### Fuentes y Plan Maestro experimental

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
KBS_EDITORIAL_CORPUS_SIZE = 34
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_LIVE_HEAD_LAST_CHECKED = 96cccb9a61f42ab97b1eba607524e33f992740f6
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Related Work B01 no depende de nuevos resultados experimentales; cualquier trigger nuevo debe reportarse antes de usarlo.

### Gate vigente

```text
CURRENT_GATE = RELATED_WORK_B01_DRAFTING
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_RELATED_WORK_B01_SECTION_2_1_ONLY
MASTER_INTEGRATION = NOT_AUTHORIZED
```

---

## English

### Overall state

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED / RESTRUCTURED_BY_D014
ARTICLE_WRITING_PLAN = V2.1
STRUCTURE_APPROVAL_DECISION = D-015
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
WORD_BASELINE = KBS_ARTICLE_WORKING_STRUCTURE_V01.docx
WORD_BASELINE_SHA256 = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
METHODS_B01_V05 = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
CURRENT_DRAFTING_PHASE = RELATED_WORK
RELATED_WORK_B01 = AUTHORIZED
AUTHORIZED_SCOPE = SECTION_2.1_ONLY
NEXT_ACTOR = DRAFTING_AI
```

The author has approved and frozen the complete KBS article structure for drafting. D-014/D-015 alter editorial structure and drafting sequence only; scientific scope, RQs, claims, experimental design, and experimental governance remain unchanged.

The active sequence is `Related Work → provisional Introduction → Decision-support architecture → Experimental design → authorized Results → figures/tables → pending-result integration → final Results → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → final KBS adaptation`.

Only `Related Work B01 — Section 2.1 Automated tariff classification and candidate retrieval` is authorized. All other manuscript sections remain blocked until this gate is reviewed.

The exact cumulative Word baseline is `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx`, SHA-256 `0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5`. Silent reconstruction is prohibited; missing access requires `BASELINE_DOCX_ACCESS_REQUIRED`.

### Current gate

```text
CURRENT_GATE = RELATED_WORK_B01_DRAFTING
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_RELATED_WORK_B01_SECTION_2_1_ONLY
MASTER_INTEGRATION = NOT_AUTHORIZED
```