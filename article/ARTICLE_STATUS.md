# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `DRAFTING` a nivel de Fase 1, limitado al bloque autorizado.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**; `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- `0C — Gap, contribución y Research Questions`: **`CLOSED / APPROVED / FROZEN`**.
- `0D-1 — Arquitectura editorial y journal fit`: **`CLOSED / APPROVED / FROZEN`**.
- `0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío`: **`CLOSED / APPROVED / FROZEN`**.
- `PHASE_0 = CLOSED / APPROVED`.
- `PHASE_1 = OPENED`.
- `METHODS_B01 = READY_FOR_DRAFTING`.
- `METHODS_B01_TITLE = Design, scope, and units`.
- `MANUSCRIPT_DRAFTING = AUTHORIZED_FOR_METHODS_B01_ONLY`.
- `OTHER_METHODS_BLOCKS = NOT_AUTHORIZED_YET`.
- `NEXT_ACTOR = DRAFTING_AI`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para el gate de entrada de B01.

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
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3_UNTIL_EXPLICIT_ARTICLE_RECONCILIATION
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

Snapshot de rama verificado al abrir Fase 1:

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_LIVE_HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
```

El Plan Maestro vivo registra cierres de Grupo 3A/3B posteriores a algunos artefactos editoriales históricos. Esa diferencia **no se reconcilia silenciosamente** con RQ4 ni con la matriz de claims. Requiere un gate editorial específico antes de usar esos resultados o inferencias en el artículo. No bloquea B01 porque B01 contiene únicamente diseño, alcance y unidades.

### Gate vigente

```text
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED
PHASE_1_METHODS_ENTRY_GATE = PASS
METHODS_B01 = READY_FOR_DRAFTING
METHODS_B01_PROMPT = article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS.md
MANUSCRIPT_DRAFTING = AUTHORIZED_FOR_METHODS_B01_ONLY
NEXT_ACTOR = DRAFTING_AI
NEXT_DELIVERY = Methods_B01_V01 + initial cumulative master candidate
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
- `METHODS_B01 = READY_FOR_DRAFTING`.
- `MANUSCRIPT_DRAFTING = AUTHORIZED_FOR_METHODS_B01_ONLY`.
- All other Methods blocks remain unauthorized.
- `NEXT_ACTOR = DRAFTING_AI`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` for the B01 entry gate.

### Frozen journal strategy

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
ARTICLE_TYPE_OPERATIVE = Research article
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Frozen pre-drafting governance

```text
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
WORD_CITATION_COMMENT_PROTOCOL_STATUS = FROZEN_FOR_DRAFTING
JOURNAL_CASCADE_STATUS = FROZEN_FOR_DRAFTING
```

The Writing AI owns generation/update of the block and cumulative candidate Markdown/Word masters. The internal Word master is bilingual. Word is the provisional APA-7 presentation layer; Markdown is the source-traceability layer; final Mendeley management belongs to the author. Every English citation requires its exact anchored audit comment. Only author-approved integration increments `ARTICLE_MASTER_V00N`.

### Pre-Phase-1 bibliographic gate

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
INACCESSIBLE = 0
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
BIBLIOGRAPHIC_SCIENTIFIC_REASSESSMENT = NOT_PERFORMED
```

Prior access never authorizes citation from memory. Every future citation must re-retrieve and verify the actual full text and exact supporting passage under MWDP_V1.0; retrieval failure triggers `ACCESS_RECHECK_REQUIRED`.

### Preserved scientific state

```text
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3_UNTIL_EXPLICIT_ARTICLE_RECONCILIATION
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The living experimental Master Plan was rechecked at `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`. It records later Group-3A/3B closures than some historical editorial artifacts. This is not silently reconciled into RQ4 or article claims; a dedicated editorial gate is required before those results/inferences are used. This does not block B01.

### Current gate

```text
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED
PHASE_1_METHODS_ENTRY_GATE = PASS
METHODS_B01 = READY_FOR_DRAFTING
METHODS_B01_PROMPT = article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS.md
MANUSCRIPT_DRAFTING = AUTHORIZED_FOR_METHODS_B01_ONLY
NEXT_ACTOR = DRAFTING_AI
NEXT_DELIVERY = Methods_B01_V01 + initial cumulative master candidate
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```
