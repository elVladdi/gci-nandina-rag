# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `AWAITING_AUTHOR_REVIEW` a nivel de `Methods B01`.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**; `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- `0C — Gap, contribución y Research Questions`: **`CLOSED / APPROVED / FROZEN`**.
- `0D-1 — Arquitectura editorial y journal fit`: **`CLOSED / APPROVED / FROZEN`**.
- `0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío`: **`CLOSED / APPROVED / FROZEN`**.
- `PHASE_0 = CLOSED / APPROVED`.
- `PHASE_1 = OPENED`.
- `METHODS_B01 = READY_FOR_AUTHOR_REVIEW`.
- `METHODS_B01_V01_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS`.
- `METHODS_B01_V01_AUTHOR_APPROVAL = REJECTED`.
- `METHODS_B01_V02_INTERNAL_REVIEW = PASS`.
- `METHODS_B01_V02_AUTHOR_APPROVAL = PENDING`.
- `METHODS_B01_REQUIRED_CORRECTIONS = NONE_PENDING`.
- `EDITORIAL_CONTROL_CORRECTION_B01_M04 = CLOSED_BY_IA_GESTORA`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION`.
- `OTHER_METHODS_BLOCKS = NOT_AUTHORIZED_YET`.
- `NEXT_ACTOR = AUTHOR`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para la revisión vigente de B01.

### Target editorial congelado

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
ARTICLE_TYPE_OPERATIVE = Research article
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Gobernanza pre-redacción congelada

```text
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = FROZEN_WITH_OPERATIONAL_CONDITION
WRITING_POLICY_STATUS = FROZEN_FOR_DRAFTING
CLAIM_EVIDENCE_PROTOCOL_STATUS = FROZEN_FOR_DRAFTING
MD_DOCX_WORKFLOW_STATUS = FROZEN_FOR_DRAFTING
WORD_CITATION_COMMENT_PROTOCOL_STATUS = FROZEN_FOR_DRAFTING
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
JOURNAL_CASCADE_STATUS = FROZEN_FOR_DRAFTING
```

Reglas operativas principales:

- La IA de Redacción genera/actualiza el bloque `.md`, el master acumulativo `.md` candidato y el master acumulativo `.docx` candidato.
- El Word interno es bilingüe: `Part I — English manuscript master` + `Part II — Spanish semantic-control mirror`.
- `WORD = PROVISIONAL_APA7_PRESENTATION_LAYER`.
- `MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY`.
- La gestión final con Mendeley corresponde al autor.
- Cada instancia de cita en la parte inglesa del Word lleva comentario anclado con fuente/revista, autor(es), extracto original suficiente, traducción española, justificación de respaldo y límite cuando corresponda.
- Solo una integración aprobada por el autor incrementa `ARTICLE_MASTER_V00N`.
- El primer candidato se inicializa como candidato, no como master aprobado.

### Gate bibliográfico previo a Fase 1 — PASSED

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CANONICAL_ACCESS_MANIFEST = CREATED
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
FILE_LIBRARY_FULLTEXT = 58
OFFICIAL_PRIMARY_WEB_FULLTEXT = 4
PDF_FORMAT_FULLTEXT = 59
AUTHORITATIVE_HTML_FULLTEXT = 3
INACCESSIBLE = 0
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
BIBLIOGRAPHIC_SCIENTIFIC_REASSESSMENT = NOT_PERFORMED
```

El acceso previo no autoriza citar por memoria. Cada cita futura exige recuperar nuevamente el full text, comprobar identidad y pasaje exacto y cumplir `MWDP_V1.0`. Una falla de recuperación activa `ACCESS_RECHECK_REQUIRED`.

### Estado científico preservado

```text
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
GROUP3 = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Se mantienen las fronteras:

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`;
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`;
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`;
- `JOURNAL_FIT ≠ NOVELTY_PROOF`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### Estado del Plan Maestro experimental vivo

Snapshot de rama verificado durante la revisión de B01:

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_LIVE_HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
GROUP3 = NOT_STARTED
```

La afirmación editorial previa de cierres de Grupo 3A/3B era incorrecta y fue corregida. HE2/HE5 y la inferencia final dependiente de Grupo 3 permanecen pendientes. Esta corrección no modifica resultados experimentales; alinea el control editorial con `SRC-03`.

### Estado de Methods B01

Historial de entregas:

- V01: commit `2a0deee3c4b63ae028bbe909d5f44f90a4282086`; revisión interna `PASS_WITH_CORRECTIONS`; aprobación del autor `REJECTED`.
- V02: commit `c9023096344a8949f3ce5f9b49c8cc29379afe4a`; revisión interna `PASS`; aprobación del autor `PENDING`.

Revisiones:

- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V01.md`;
- `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V01.md`;
- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V02.md`.

Resultado vigente:

```text
METHODS_B01_V02_INTERNAL_REVIEW = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
REQUIRED_CORRECTIONS = 0
B01_M01 = CLOSED
B01_M02 = CLOSED
B01_M03 = CLOSED
B01_M04 = CLOSED_BY_IA_GESTORA
B01_M05 = CLOSED
POSITIONING_ORDER = GENERAL_ARCHITECTURE_FIRST / NANDINA_CH87_AS_TESTBED_SECOND
EN_ES_SEMANTIC_EQUIVALENCE = PASS
AUTHOR_APPROVAL_METHODS_B01_V02 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

La V02 presenta primero el **objeto científico general** —arquitectura auditable de apoyo a decisión con desacoplamiento funcional de ranking, evidencia normativa y explicación LLM, Top-3 fijo y sin feedback generativo— y después introduce **NANDINA Capítulo 87 como testbed experimental regulatorio**. No declara novelty final ni generalización empírica.

### Gate vigente

```text
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED
PHASE_1_METHODS_ENTRY_GATE = PASS
METHODS_B01 = READY_FOR_AUTHOR_REVIEW
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION
NEXT_ACTOR = AUTHOR
NEXT_PROMPT = NONE
NEXT_DELIVERY = AUTHOR_DECISION_ON_METHODS_B01_V02
AUTHOR_APPROVAL_METHODS_B01_V02 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### Overall state

- Working branch: `article/main-manuscript`.
- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `CLOSED / APPROVED`; 0B-01 through 0B-06 remain `APPROVED / FROZEN`.
- Phase 0C: `CLOSED / APPROVED / FROZEN`.
- Phase 0D-1: `CLOSED / APPROVED / FROZEN`.
- Phase 0D-2: `CLOSED / APPROVED / FROZEN`.
- `PHASE_0 = CLOSED / APPROVED`.
- `PHASE_1 = OPENED`.
- `METHODS_B01 = READY_FOR_AUTHOR_REVIEW`.
- `METHODS_B01_V01_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS`.
- `METHODS_B01_V01_AUTHOR_APPROVAL = REJECTED`.
- `METHODS_B01_V02_INTERNAL_REVIEW = PASS`.
- `METHODS_B01_V02_AUTHOR_APPROVAL = PENDING`.
- Drafting is not authorized while the author decision is pending; all other Methods blocks remain unauthorized.
- `NEXT_ACTOR = AUTHOR`.

### Frozen journal strategy and governance

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
ARTICLE_TYPE_OPERATIVE = Research article
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
```

### Living experimental state

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_LIVE_HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
GROUP3 = NOT_STARTED
```

### Methods B01 state

V01 at commit `2a0deee3c4b63ae028bbe909d5f44f90a4282086` received internal `PASS_WITH_CORRECTIONS` and was rejected by the author because the opening foregrounded NANDINA/Chapter 87 before making the broader scientific offering visible.

V02 at commit `c9023096344a8949f3ce5f9b49c8cc29379afe4a` received internal `PASS`. It now foregrounds the broader auditable decision-support architecture and introduces NANDINA Chapter 87 only afterward as the controlled regulatory testbed.

```text
METHODS_B01_V02_INTERNAL_REVIEW = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
REQUIRED_CORRECTIONS = 0
B01_M01 = CLOSED
B01_M02 = CLOSED
B01_M03 = CLOSED
B01_M04 = CLOSED_BY_MANAGING_AI
B01_M05 = CLOSED
POSITIONING_ORDER = GENERAL_ARCHITECTURE_FIRST / NANDINA_CH87_AS_TESTBED_SECOND
EN_ES_SEMANTIC_EQUIVALENCE = PASS
AUTHOR_APPROVAL_METHODS_B01_V02 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

### Current gate

```text
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED
PHASE_1_METHODS_ENTRY_GATE = PASS
METHODS_B01 = READY_FOR_AUTHOR_REVIEW
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION
NEXT_ACTOR = AUTHOR
NEXT_PROMPT = NONE
NEXT_DELIVERY = AUTHOR_DECISION_ON_METHODS_B01_V02
AUTHOR_APPROVAL_METHODS_B01_V02 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```
