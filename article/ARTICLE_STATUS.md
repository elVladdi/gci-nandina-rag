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
- `AUTHOR_APPROVAL = PENDING_REQUEST`.
- `FREEZE_0D = NOT_AUTHORIZED_YET`.
- `PHASE_1 = BLOCKED_PENDING_AUTHOR_APPROVAL_AND_0D_FREEZE`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para el gate editorial vigente.

### Gobernanza pre-redacción cerrada en 0D-2

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

Reglas operativas principales:

- La IA de Redacción genera y actualiza el bloque `.md`, el master acumulativo `.md` candidato y el master acumulativo `.docx` candidato.
- El Word interno es bilingüe: `Part I — English manuscript master` + `Part II — Spanish semantic-control mirror`.
- `WORD = PROVISIONAL_APA7_PRESENTATION_LAYER`.
- `MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY`.
- La gestión final con Mendeley corresponde al autor.
- Cada instancia de cita en la parte inglesa del Word lleva comentario anclado con fuente/revista, autor(es), extracto original suficiente, traducción española, justificación de respaldo y límite cuando corresponda.
- El siguiente bloque parte del último master aprobado; no se reconstruye silenciosamente desde cero.
- Se distinguen `BLOCK_REVISION`, `MASTER_CANDIDATE_REVISION` y `MASTER_INTEGRATION`; solo una integración aprobada hace avanzar el master canónico.
- Los requisitos KBS aún no confirmados desde el Guide for Authors se neutralizan mediante un master Word neutral/reversible y disciplina de extensión conservadora, y deben revalidarse antes del paquete final de submission.

### Gate bibliográfico previo a Fase 1 — PASSED

La auditoría técnica está registrada en:

`article/reviews/0D2_BIBLIOGRAPHIC_FULLTEXT_ACCESS_AUDIT.md`

Resultado exacto:

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

Aclaración: no existen necesariamente `62 PDF locales`. Hay 58 full-text recuperables directamente mediante File Library, el PDF oficial WCO de las General Rules y tres fuentes full-text HTML autoritativas (dos procedimientos SUNAT y Al-Hawamdeh en Information Research). Las 62 fuentes son actualmente reinspeccionables a texto completo para auditoría claim–cita–fuente.

El `PASS` de acceso no autoriza citar por memoria. Cada uso futuro debe recuperar nuevamente la fuente full-text y comprobar el pasaje exacto antes de redactar el claim y el comentario de Word. Si una sesión futura no logra recuperar una fuente, se declara `ACCESS_RECHECK_REQUIRED`.

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
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
NEXT_ACTOR = AUTHOR_THEN_IA_GESTORA
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = PENDING_REQUEST
FREEZE_0D = NOT_AUTHORIZED_YET
PHASE_1 = BLOCKED_PENDING_AUTHOR_APPROVAL_AND_0D_FREEZE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### Overall state

- Working branch: `article/main-manuscript`.
- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `CLOSED / APPROVED`; blocks 0B-01 through 0B-06 remain `APPROVED / FROZEN`.
- Phase 0C: `CLOSED / APPROVED / FROZEN`.
- `0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`.
- `0D2 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`.
- `0D2_V02_INTERNAL_REVIEW = PASS`; M01–M04 are closed.
- Primary target recommendation remains Knowledge-Based Systems; Plan B remains Expert Systems with Applications; Plan C remains Information Processing & Management.
- `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = PENDING_REQUEST`.
- `FREEZE_0D = NOT_AUTHORIZED_YET`.
- `PHASE_1 = BLOCKED_PENDING_AUTHOR_APPROVAL_AND_0D_FREEZE`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.

### Closed pre-drafting governance

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

The Writing AI owns generation/update of block Markdown and cumulative candidate Markdown/Word masters. The internal Word master is bilingual. Word alone is the provisional APA-7 presentation layer; Markdown is the source-traceability layer; final Mendeley management belongs to the author. Each English Word citation carries the required anchored audit comment. Approved-master integrity and separate block/candidate/integration revision counters remain mandatory.

### Pre-Phase-1 bibliographic gate — PASSED

The technical audit is recorded in `article/reviews/0D2_BIBLIOGRAPHIC_FULLTEXT_ACCESS_AUDIT.md`.

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

This is not a claim that 62 local PDFs exist. Fifty-eight full-text files are directly retrievable through File Library; WCO REF-053 is available as the official primary PDF; and three sources are authoritative complete HTML sources. All 62 are currently reinspectable at full-text level. Every future citation must nevertheless re-retrieve the actual full text and verify the exact supporting passage; a future retrieval failure triggers `ACCESS_RECHECK_REQUIRED`.

### Preserved scientific state

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

### Current gate

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2_V02_INTERNAL_REVIEW = PASS
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
NEXT_ACTOR = AUTHOR_THEN_MANAGING_AI
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = PENDING_REQUEST
FREEZE_0D = NOT_AUTHORIZED_YET
PHASE_1 = BLOCKED_PENDING_AUTHOR_APPROVAL_AND_0D_FREEZE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```
