# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**; `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- `0C — Gap, contribución y Research Questions`: **`CLOSED / APPROVED / FROZEN`**.
- `0D-1 — Arquitectura editorial y journal fit`: **`INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`**.
- `0D_V02_INTERNAL_REVIEW = PASS`; `0D_M01 = CLOSED`.
- `0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío`: **`INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`**.
- `0D2_V02_INTERNAL_REVIEW = PASS`.
- `0D2_M01 = CLOSED`.
- `0D2_M02 = CLOSED_BY_AUTHOR_DECISION`.
- `0D2_M03 = CLOSED`.
- `0D2_M04 = CLOSED`.
- `PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems`.
- `ALTERNATIVE_TARGET_1 = Expert Systems with Applications`.
- `ALTERNATIVE_TARGET_2 = Information Processing & Management`.
- `TARGET_JOURNAL = PENDING_0D_FREEZE_AND_AUTHOR_APPROVAL`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = NOT_REQUESTED_YET`.
- `FREEZE_0D = NOT_AUTHORIZED_YET`.
- `PHASE_1 = BLOCKED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para el gate editorial vigente.

### Resultado 0D-2 V02

La V02 corrige íntegramente las cuatro observaciones de V01. Gobierna la revisión:

- `article/reviews/0D2_V02_INTERNAL_REVIEW.md`.

Estados principales:

```text
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
JOURNAL_CASCADE_STATUS = CLOSED_FOR_DRAFTING
```

Se mantiene la política de Word neutral y reversible mientras el Guide for Authors específico de KBS no permita cerrar plantilla, límite exacto, free-format, headings obligatorios o estilo bibliográfico final mediante fuente primaria accesible. Estos puntos se conservan como condiciones operativas y deben revalidarse antes del paquete final de submission.

### Gobernanza de manuscrito pre-redacción

- La **IA de Redacción** genera y actualiza cada bloque `.md`, el master acumulativo `.md` candidato y el master acumulativo `.docx` candidato.
- El Word interno será bilingüe: **Part I — English manuscript master** + **Part II — Spanish semantic-control mirror**.
- `WORD = PROVISIONAL_APA7_PRESENTATION_LAYER`.
- `MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY`.
- La gestión final con Mendeley corresponde al autor.
- Cada instancia de cita en la parte inglesa del Word debe llevar comentario anclado con fuente/revista, autor(es), extracto original suficiente, traducción española, justificación de respaldo y límite cuando corresponda.
- El siguiente bloque siempre parte del último master aprobado; no se reconstruye silenciosamente desde cero.
- Se distinguen `BLOCK_REVISION`, `MASTER_CANDIDATE_REVISION` y `MASTER_INTEGRATION`; solo una integración aprobada hace avanzar el master canónico.

### Gate bibliográfico previo a Fase 1

A solicitud posterior del autor, antes de abrir Fase 1 debe comprobarse la disponibilidad efectiva del corpus bibliográfico consolidado de `62` fuentes. Esta condición no reabre 0B ni invalida 0D-2 V02; garantiza que el protocolo claim–cita–fuente pueda ejecutarse durante la redacción.

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
BIBLIOGRAPHIC_FULLTEXT_ACCESS_AUDIT = REQUIRED
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PENDING
```

La auditoría debe comprobar, por referencia:

```text
reference_identity_verified
full_text_or_pdf_accessible
source_text_searchable_or_inspectable
stable_source_identifier_available
citation_comment_support_possible
```

No implica reanalizar científicamente los 62 trabajos ni reabrir novelty; solo verificar acceso efectivo y reutilizable al texto fuente.

### Estado científico preservado

```text
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
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

### Gate vigente

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2_V02_INTERNAL_REVIEW = PASS
0D2_M01 = CLOSED
0D2_M02 = CLOSED_BY_AUTHOR_DECISION
0D2_M03 = CLOSED
0D2_M04 = CLOSED
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PENDING
NEXT_ACTOR = IA_GESTORA
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED_YET
FREEZE_0D = NOT_AUTHORIZED_YET
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `CLOSED / APPROVED`; 0B-01 through 0B-06 are `APPROVED / FROZEN`.
- Phase 0C: `CLOSED / APPROVED / FROZEN`.
- `0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`.
- `0D2 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`.
- `0D2_V02_INTERNAL_REVIEW = PASS`.
- `0D2_M01 = CLOSED`; `0D2_M02 = CLOSED_BY_AUTHOR_DECISION`; `0D2_M03 = CLOSED`; `0D2_M04 = CLOSED`.
- Primary target recommendation remains Knowledge-Based Systems; alternatives remain Expert Systems with Applications and Information Processing & Management.
- `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = NOT_REQUESTED_YET`.
- `FREEZE_0D = NOT_AUTHORIZED_YET`.
- `PHASE_1 = BLOCKED`; `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.

### 0D-2 V02 result

V02 fully resolves the four V01 observations. Current pre-drafting governance is:

```text
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
JOURNAL_CASCADE_STATUS = CLOSED_FOR_DRAFTING
```

The Writing AI owns manuscript artifact generation/update. The internal Word master is bilingual; Word alone carries provisional APA-7 presentation; Markdown is the source-traceability layer; final Mendeley management belongs to the author; every English Word citation carries the required anchored audit comment; and block revision, candidate-master revision, and approved master integration use distinct counters.

### Pre-Phase-1 bibliographic access gate

Following the author's subsequent request, effective access to the consolidated 62-source bibliographic corpus must be checked before Phase 1 opens. This is not a V02 defect and does not reopen Phase 0B; it ensures future claim–citation–source audit comments can be grounded in re-inspectable source text.

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
BIBLIOGRAPHIC_FULLTEXT_ACCESS_AUDIT = REQUIRED
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PENDING
```

For each reference, the audit must verify identity, full-text/PDF access, inspectable/searchable source text, a stable source identifier, and the feasibility of citation-comment support.

### Current gate

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2_V02_INTERNAL_REVIEW = PASS
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PENDING
NEXT_ACTOR = MANAGING_AI
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED_YET
FREEZE_0D = NOT_AUTHORIZED_YET
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```
