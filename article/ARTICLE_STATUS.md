# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `READY_FOR_AUTHOR_REVIEW` a nivel de `Methods B01`.
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
- `METHODS_B01_V02_AUTHOR_APPROVAL = REJECTED`.
- `METHODS_B01_V03_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS`.
- `METHODS_B01_V03_SCIENTIFIC_CONTENT_REVIEW = PASS`.
- `METHODS_B01_V03_AUTHOR_APPROVAL = NOT_REQUESTED`.
- `METHODS_B01_V05_INTERNAL_REVIEW = PASS`.
- `METHODS_B01_V05_KBS_EDITORIAL_FIT = PASS`.
- `METHODS_B01_V05_AUTHOR_APPROVAL = PENDING`.
- `METHODS_B01_REQUIRED_CORRECTIONS = NONE_PENDING`.
- `V04_STATUS = NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION`.
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
PUBLICATION_ROUTE_TARGET_A = SUBSCRIPTION
PAID_OPEN_ACCESS = NOT_SELECTED
APC_PAYMENT_PLANNED = NO
```

La decisión de publicación para KBS se conserva en `article/governance/D012_KBS_PUBLICATION_MODEL_DECISION.md`.

### Gobernanza de redacción y estándar KBS

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
SPCCR_VERSION = 1.0
SPCCR_STATUS = AUTHOR_APPROVED / ACTIVE
KBS_EMPIRICAL_WRITING_GUIDE = KBS_EWG_34_V01
KBS_EMPIRICAL_WRITING_GUIDE_STATUS = AUTHOR_APPROVED / ACTIVE / BINDING
KBS_EMPIRICAL_WRITING_GUIDE_DECISION = D-013
KBS_EMPIRICAL_CORPUS_SIZE = 34
```

Reglas operativas principales:

- La IA de Redacción genera/actualiza el bloque `.md`, el master acumulativo `.md` candidato y el master acumulativo `.docx` candidato.
- El Word interno es bilingüe: `Part I — English manuscript master` + `Part II — Spanish semantic-control mirror`.
- `WORD = PROVISIONAL_APA7_PRESENTATION_LAYER`.
- `MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY`.
- La gestión final con Mendeley corresponde al autor.
- Cada instancia de cita en la parte inglesa del Word lleva comentario anclado con fuente/revista, autor(es), extracto original suficiente, traducción española, justificación de respaldo y límite cuando corresponda.
- Solo una integración aprobada por el autor incrementa `ARTICLE_MASTER_V00N`.
- Desde B01 V03 rige `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`.
- Desde D-013, `KBS_EWG_34_V01` es la referencia editorial principal para prosa, organización retórica, densidad, explicitación de contribución y presentación metodológica mientras KBS permanezca como `TARGET_A`.
- La guía KBS-34 no amplía claims ni sustituye MWDP, Claim–Evidence Matrix o Plan Maestro para evidencia, alcance, causalidad, resultados, inferencia o generalización.

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

El corpus editorial KBS-34 es independiente del corpus científico bibliográfico de 62 fuentes. Los 34 artículos KBS sirven como evidencia editorial y no se convierten automáticamente en fuentes científicas del manuscrito.

El acceso previo no autoriza citar por memoria. Cada cita futura exige recuperar nuevamente el full text, comprobar identidad y pasaje exacto y cumplir `MWDP_V1.0`. Una falla de recuperación activa `ACCESS_RECHECK_REQUIRED`.

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

Snapshot verificado durante la revisión interna de B01 V05:

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

Este avance experimental no modifica por sí solo Methods B01. V05 no consume resultados, métricas ni inferencias de Grupo 3. Cualquier uso posterior de nuevos resultados experimentales deberá seguir el gate correspondiente y consultar nuevamente el Plan Maestro vivo.

### Estado de Methods B01

Historial de entregas:

- V01: commit `2a0deee3c4b63ae028bbe909d5f44f90a4282086`; revisión interna `PASS_WITH_CORRECTIONS`; aprobación del autor `REJECTED`.
- V02: commit `c9023096344a8949f3ce5f9b49c8cc29379afe4a`; revisión interna `PASS`; aprobación del autor `REJECTED`.
- V03: commit `5a3d78c0eedf6d14b79e5a9470c8f8c90a2dc2b1`; contenido científico `PASS`; revisión interna global `PASS_WITH_CORRECTIONS`; posteriormente reauditable editorialmente bajo KBS-34.
- V04: `NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION`; estaba limitada a reparar el DOCX V03 y quedó sustituida por D-013 antes de ejecutarse.
- V05: commit `1e5c6fe2fc89b9f819b0555478bcca179c3a1bc3`; revisión interna `PASS`; `KBS_EDITORIAL_FIT = PASS`; lista para revisión del autor.

Revisiones relevantes:

- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V01.md`;
- `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V01.md`;
- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V02.md`;
- `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V02.md`;
- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V03.md`;
- `article/reviews/1_METHODS_B01_KBS_EDITORIAL_REAUDIT_V03.md`;
- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V05.md`.

Resultado vigente:

```text
METHODS_B01_V05_INTERNAL_REVIEW = PASS
SCIENTIFIC_CONTENT_REVIEW = PASS / PREVIOUS_PASS_RETAINED
KBS_EDITORIAL_FIT = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
B01_M01 = CLOSED
B01_M02 = CLOSED
B01_M03 = CLOSED
B01_M04 = CLOSED_BY_IA_GESTORA
B01_M05 = CLOSED
B01_M06 = CLOSED
B01_M07 = CLOSED
B01_M08 = CLOSED
B01_M09 = CLOSED
B01_M10 = CLOSED
B01_M11 = CLOSED
B01_M12 = CLOSED
B01_M13 = CLOSED
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
GENERAL_METHOD_FIRST = PASS
NANDINA_AS_TESTBED_SECOND = PASS
INPUT_OPERATION_OUTPUT_CLARITY = PASS
ABSTRACTION_DENSITY = LOW_TO_MODERATE
CONTRACT_LANGUAGE_OVERLOAD = ABSENT
CONFIGURABILITY_PRECONDITIONS = EXPLICIT_BOUNDED
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
DOCX_SHA256 = 77c8cb0121f50ff51507c59d32f4a66f32e198143777285a4d5b7cb62013ba76
DOCX_ZIP_INTEGRITY = PASS
DOCX_DOCUMENT_XML = PRESENT
DOCX_COMMENTS = 0
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS
MD_DOCX_VISIBLE_TEXT_EQUIVALENCE = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
AUTHOR_REVIEW_READY = YES
AUTHOR_APPROVAL_METHODS_B01_V05 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

V05 presenta el método antes del testbed, describe explícitamente entrada–operación–salida, conserva el Top-3 fijo antes de la recuperación normativa, mantiene al LLM fuera del ranking y formula la configurabilidad con precondiciones de recursos e interfaces. La evidencia empírica queda delimitada al piloto offline de NANDINA Chapter 87 y a las versiones de datos, corpus y configuración utilizadas en dicho piloto.

### Gate vigente

```text
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED
PHASE_1_METHODS_ENTRY_GATE = PASS
METHODS_B01 = READY_FOR_AUTHOR_REVIEW
METHODS_B01_V05_INTERNAL_REVIEW = PASS
NEXT_ACTOR = AUTHOR
AUTHOR_APPROVAL_METHODS_B01_V05 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

No existe autorización para integrar V05 como master canónico, congelar B01 ni abrir B02 hasta recibir decisión expresa del autor.

---

## English

### Overall state

- Working branch: `article/main-manuscript`.
- Global state: `READY_FOR_AUTHOR_REVIEW` at `Methods B01`.
- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `CLOSED / APPROVED`; 0B-01 through 0B-06 remain `APPROVED / FROZEN`.
- Phase 0C: `CLOSED / APPROVED / FROZEN`.
- Phase 0D-1: `CLOSED / APPROVED / FROZEN`.
- Phase 0D-2: `CLOSED / APPROVED / FROZEN`.
- `PHASE_0 = CLOSED / APPROVED`.
- `PHASE_1 = OPENED`.
- `METHODS_B01 = READY_FOR_AUTHOR_REVIEW`.
- `METHODS_B01_V05_INTERNAL_REVIEW = PASS`.
- `METHODS_B01_V05_KBS_EDITORIAL_FIT = PASS`.
- `METHODS_B01_V05_AUTHOR_APPROVAL = PENDING`.
- `METHODS_B01_REQUIRED_CORRECTIONS = NONE_PENDING`.
- `V04_STATUS = NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION`.
- `OTHER_METHODS_BLOCKS = NOT_AUTHORIZED_YET`.
- `NEXT_ACTOR = AUTHOR`.

### Frozen journal strategy and writing governance

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
ARTICLE_TYPE_OPERATIVE = Research article
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
PUBLICATION_ROUTE_TARGET_A = SUBSCRIPTION
PAID_OPEN_ACCESS = NOT_SELECTED
APC_PAYMENT_PLANNED = NO
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
SPCCR_VERSION = 1.0
SPCCR_STATUS = AUTHOR_APPROVED / ACTIVE
KBS_EMPIRICAL_WRITING_GUIDE = KBS_EWG_34_V01
KBS_EMPIRICAL_WRITING_GUIDE_STATUS = AUTHOR_APPROVED / ACTIVE / BINDING
KBS_EMPIRICAL_WRITING_GUIDE_DECISION = D-013
KBS_EMPIRICAL_CORPUS_SIZE = 34
```

The KBS-34 guide is the primary editorial reference for prose, rhetorical organization, density, contribution visibility, and methodological presentation while KBS remains Target A. It cannot expand scientific claims or supersede MWDP, the Claim–Evidence Matrix, or the experimental Master Plan for evidence, scope, causal statements, results, inference, or generalization.

### Bibliographic gate

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
```

The KBS-34 editorial corpus is separate from the 62-source scientific bibliographic corpus. The KBS papers do not automatically become scientific sources for the manuscript.

### Preserved scientific state

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

The boundaries `candidate retrieval ≠ overall classification accuracy`, `normative association ≠ substantive normative correctness`, `auditability ≠ legal correctness`, and `configurability ≠ empirical generalization` remain mandatory.

### Living experimental state

Snapshot verified during the V05 internal review:

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

V05 consumes no Group 3 result, metric, or inference, so the current experimental progress does not trigger an experimental review for Methods 3.1.

### Methods B01 state

- V01: internal `PASS_WITH_CORRECTIONS`; author rejected.
- V02: internal `PASS`; author rejected.
- V03: scientific content `PASS`, global internal `PASS_WITH_CORRECTIONS`; later subjected to KBS-34 editorial reaudit.
- V04: `NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION`.
- V05: delivery commit `1e5c6fe2fc89b9f819b0555478bcca179c3a1bc3`; internal review `PASS`; `KBS_EDITORIAL_FIT = PASS`; ready for author review.

```text
METHODS_B01_V05_INTERNAL_REVIEW = PASS
SCIENTIFIC_CONTENT_REVIEW = PASS / PREVIOUS_PASS_RETAINED
KBS_EDITORIAL_FIT = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
B01_M09 = CLOSED
B01_M10 = CLOSED
B01_M11 = CLOSED
B01_M12 = CLOSED
B01_M13 = CLOSED
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
GENERAL_METHOD_FIRST = PASS
NANDINA_AS_TESTBED_SECOND = PASS
INPUT_OPERATION_OUTPUT_CLARITY = PASS
ABSTRACTION_DENSITY = LOW_TO_MODERATE
CONTRACT_LANGUAGE_OVERLOAD = ABSENT
CONFIGURABILITY_PRECONDITIONS = EXPLICIT_BOUNDED
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
DOCX_SHA256 = 77c8cb0121f50ff51507c59d32f4a66f32e198143777285a4d5b7cb62013ba76
DOCX_ZIP_INTEGRITY = PASS
DOCX_DOCUMENT_XML = PRESENT
DOCX_COMMENTS = 0
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS
MD_DOCX_VISIBLE_TEXT_EQUIVALENCE = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
AUTHOR_REVIEW_READY = YES
AUTHOR_APPROVAL_METHODS_B01_V05 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

### Current gate

```text
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED
PHASE_1_METHODS_ENTRY_GATE = PASS
METHODS_B01 = READY_FOR_AUTHOR_REVIEW
METHODS_B01_V05_INTERNAL_REVIEW = PASS
NEXT_ACTOR = AUTHOR
AUTHOR_APPROVAL_METHODS_B01_V05 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

There is no authorization to integrate V05 into the canonical master, freeze B01, or open B02 until an explicit author decision is received.