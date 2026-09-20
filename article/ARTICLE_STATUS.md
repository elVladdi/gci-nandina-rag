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
ARTICLE_WRITING_PLAN = V2.0
STRUCTURE_DECISION = D-014
WORKING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
WORKING_STRUCTURE_STATUS = WORKING / AUTHOR_EDITABLE / NOT_YET_FROZEN
METHODS_B01_V05 = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
NEW_MANUSCRIPT_SECTION_DRAFTING = NOT_AUTHORIZED_PENDING_STRUCTURE_APPROVAL
NEXT_ACTOR = AUTHOR
NEXT_ACTION = REVIEW_AND_EDIT_WORKING_STRUCTURE_V01
```

### Fases previas

- `0A — Ground truth documental y experimental`: **CLOSED / APPROVED**.
- `0B — Mapa crítico de literatura y taxonomía`: **CLOSED / APPROVED / FROZEN**.
- `0C — Posicionamiento científico y Research Questions`: **CLOSED / APPROVED / FROZEN**.
- `0D-1 / 0D-2`: **CLOSED / APPROVED / FROZEN**; D-014 supersede de forma controlada únicamente la arquitectura de secciones y el orden de redacción heredados de 0D.

D-014 **no modifica** el alcance científico, las RQ, la Claim–Evidence Matrix, el diseño experimental ni la gobernanza del Plan Maestro experimental.

### Decisión del autor sobre Methods B01 V05

El autor **no aprueba V05**. La revisión interna previa (`PASS`) queda como antecedente técnico, pero no tiene efecto de aprobación editorial del autor.

Motivos registrados:

- fluidez insuficiente;
- persistencia de abstracciones;
- apertura mediante una formulación que sugiere prematuramente el desarrollo de “the method”;
- introducción demasiado temprana del alcance experimental específico;
- NANDINA / Chapter-Class 87 / corpus concreto aparecen antes de que el lector comprenda adecuadamente el problema, el posicionamiento y la arquitectura general.

Por tanto:

```text
METHODS_B01_V05_INTERNAL_REVIEW = PASS / HISTORICAL
METHODS_B01_V05_AUTHOR_APPROVAL = NOT_GRANTED
METHODS_B01_V05_STATUS = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
MASTER_INTEGRATION_OF_V05 = PROHIBITED
```

No se corregirá V05 todavía. Primero debe cerrarse la estructura completa del artículo.

### Reset estructural D-014

A partir de D-014, el artículo separa explícitamente:

1. problema y posicionamiento científico;
2. arquitectura general de apoyo a decisiones;
3. instanciación experimental específica.

Arquitectura de trabajo:

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

`Limitations` queda provisionalmente integrada como `6.6 Limitations`.

La estructura detallada está en `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`. El Word editable `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx` es la base acumulativa para las versiones posteriores; la estructura aún no está congelada y puede ser editada por el autor.

### Nuevo orden de redacción

Tras aprobación explícita de la estructura:

`Related Work → Introduction provisional → Decision-support architecture → Experimental design → Results disponibles/autorizados → figuras/tablas → integración de resultados pendientes → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → adaptación final KBS`.

El antiguo orden `Methods → Related Work → ... → Introduction` queda `SUPERSEDED`.

### Gobernanza y estándar editorial

```text
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
SPCCR_VERSION = 1.0
SPCCR_STATUS = AUTHOR_APPROVED / ACTIVE
KBS_EMPIRICAL_WRITING_GUIDE = KBS_EWG_34_V01
KBS_EMPIRICAL_WRITING_GUIDE_STATUS = AUTHOR_APPROVED / ACTIVE / BINDING
KBS_EMPIRICAL_WRITING_GUIDE_DECISION = D-013
KBS_EMPIRICAL_CORPUS_SIZE = 34
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
PUBLICATION_ROUTE_TARGET_A = SUBSCRIPTION
PAID_OPEN_ACCESS = NOT_SELECTED
APC_PAYMENT_PLANNED = NO
```

La guía KBS-34 gobierna prosa, organización retórica, densidad, visibilidad de la contribución y presentación metodológica. No amplía claims ni reemplaza MWDP, Claim–Evidence Matrix o Plan Maestro en asuntos de evidencia, resultados, inferencia, causalidad o generalización.

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

### Gate bibliográfico

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
KBS_EDITORIAL_CORPUS_SIZE = 34
```

Los 34 artículos KBS son evidencia editorial, no fuentes científicas automáticas del manuscrito.

### Estado del Plan Maestro experimental vivo

Último snapshot consultado en este proceso:

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_LIVE_HEAD = 96cccb9a61f42ab97b1eba607524e33f992740f6
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
NEXT_ELIGIBLE_FICHA = G3-F04
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
```

La reestructuración editorial no modifica estos estados experimentales.

### Historial resumido de Methods B01

- V01: autor `REJECTED`.
- V02: autor `REJECTED`.
- V03: contenido científico `PASS`; entrega global requirió corrección y reauditoría editorial posterior.
- V04: `NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION`.
- V05: revisión interna `PASS`, pero autor `NOT APPROVED`; queda en `HOLD` por problemas de fluidez, abstracción y ubicación narrativa del alcance experimental.

### Gate vigente

```text
CURRENT_GATE = ARTICLE_STRUCTURE_REVIEW
WORKING_STRUCTURE_STATUS = WORKING / AUTHOR_EDITABLE / NOT_YET_FROZEN
NEXT_ACTOR = AUTHOR
NEXT_ACTION = REVIEW_AND_EDIT_WORKING_STRUCTURE_V01
NEW_SECTION_DRAFTING = NOT_AUTHORIZED
METHODS_B01_V06 = NOT_AUTHORIZED
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
KBS_EMPIRICAL_WRITING_GUIDE = KBS_EWG_34_V01 / AUTHOR_APPROVED / ACTIVE / BINDING
ARTICLE_WRITING_PLAN = V2.0
STRUCTURE_DECISION = D-014
WORKING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
WORKING_STRUCTURE_STATUS = WORKING / AUTHOR_EDITABLE / NOT_YET_FROZEN
METHODS_B01_V05 = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
NEW_MANUSCRIPT_SECTION_DRAFTING = NOT_AUTHORIZED_PENDING_STRUCTURE_APPROVAL
NEXT_ACTOR = AUTHOR
```

### Author decision on Methods B01 V05

V05 is not approved. The previous internal PASS remains a technical historical record only. The author identified limited fluency, remaining abstraction, premature framing as “the method,” and premature introduction of the specific experimental scope before the reader has understood the problem, scientific positioning, and general architecture.

No V06 correction is authorized yet. The complete article structure must be reviewed first.

### D-014 structural reset

The working article architecture is now:

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion
7. Conclusion
8. KBS end matter.

The detailed structure is versioned in `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`. The editable Word with the same structure is the cumulative working base for future versions and remains author-editable until explicitly frozen.

After structure approval, drafting proceeds as:

`Related Work → provisional Introduction → Decision-support architecture → Experimental design → authorized Results → figures/tables → pending-result integration → final Results → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → final KBS adaptation`.

The former Methods-first sequence is superseded.

### Preserved scientific and experimental boundaries

D-014 changes editorial structure and drafting order only. Scientific scope, RQs, Claim–Evidence rules, experimental design and the experimental Master Plan remain unchanged. Candidate retrieval is not overall system accuracy; documentary association is not legal correctness; auditability is not legal correctness; configurability is not empirical generalization.

### Current gate

```text
CURRENT_GATE = ARTICLE_STRUCTURE_REVIEW
WORKING_STRUCTURE_STATUS = WORKING / AUTHOR_EDITABLE / NOT_YET_FROZEN
NEXT_ACTOR = AUTHOR
NEW_SECTION_DRAFTING = NOT_AUTHORIZED
METHODS_B01_V06 = NOT_AUTHORIZED
MASTER_INTEGRATION = NOT_AUTHORIZED
```
