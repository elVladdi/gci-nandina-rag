# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- `Fase 0`: **`CLOSED / APPROVED`**.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**; `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- `0C — Gap, contribución y Research Questions`: **`CLOSED / APPROVED / FROZEN`**.
- `0D — Arquitectura editorial, journal fit y gobernanza pre-redacción`: **`CLOSED / APPROVED / FROZEN`**.
- `0D-1 — Arquitectura editorial y journal fit`: **`CLOSED / APPROVED / FROZEN`**.
- `0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío`: **`CLOSED / APPROVED / FROZEN`**.
- `0D_V02_INTERNAL_REVIEW = PASS`.
- `0D2_V02_INTERNAL_REVIEW = PASS`.
- `0D_AUTHOR_APPROVAL = RECEIVED`.
- `BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS`.
- `MASTER_WRITING_AND_DELIVERY_PROTOCOL = MWDP_V1.0 / FROZEN`.
- `TARGET_JOURNAL = Knowledge-Based Systems`.
- `PLAN_B = Expert Systems with Applications`.
- `PLAN_C = Information Processing & Management`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `PHASE_1 = ELIGIBLE_FOR_OPENING / NEXT`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_UNTIL_PHASE_1_BLOCK_PROMPT`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para el gate editorial vigente.

### Artefactos canónicos de cierre de Fase 0

- Aprobación del autor de 0D: `article/reviews/0D_AUTHOR_APPROVAL.md`.
- Freeze canónico de 0D: `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`.
- Protocolo maestro acumulativo: `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — `MWDP_V1.0 / FROZEN`.
- Auditoría de acceso bibliográfico: `article/reviews/0D2_BIBLIOGRAPHIC_FULLTEXT_ACCESS_AUDIT.md`.
- Cierre formal de Fase 0: `article/reviews/0_PHASE_CLOSURE.md`.

### Gobernanza pre-redacción congelada

```text
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = FROZEN
WRITING_POLICY_STATUS = FROZEN
CLAIM_EVIDENCE_PROTOCOL_STATUS = FROZEN
MD_DOCX_WORKFLOW_STATUS = FROZEN
WORD_CITATION_COMMENT_PROTOCOL_STATUS = FROZEN
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
JOURNAL_CASCADE_STATUS = FROZEN
```

Reglas operativas principales:

- La IA de Redacción genera y actualiza el bloque `.md`, el master acumulativo `.md` candidato y el master acumulativo `.docx` candidato.
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` debe leerse y cumplirse íntegramente en cada bloque de Fase 1 en adelante.
- El Word interno es bilingüe: `Part I — English manuscript master` + `Part II — Spanish semantic-control mirror`.
- `WORD = PROVISIONAL_APA7_PRESENTATION_LAYER`.
- `MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY`.
- La gestión final con Mendeley corresponde al autor.
- Cada instancia de cita en la parte inglesa del Word lleva comentario anclado con fuente/revista, autor(es), extracto original suficiente, traducción española, justificación de respaldo y límite cuando corresponda.
- El siguiente bloque parte del último master aprobado; no se reconstruye silenciosamente desde cero.
- Se distinguen `BLOCK_REVISION`, `MASTER_CANDIDATE_REVISION` y `MASTER_INTEGRATION`; solo una integración aprobada hace avanzar el master canónico.
- Los requisitos KBS todavía no verificables desde fuente primaria accesible se gestionan mediante master neutral/reversible y deben revalidarse antes del paquete final de submission.

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

No se interpreta como existencia de 62 PDF locales. El `PASS` no autoriza citar por memoria: cada uso futuro debe recuperar nuevamente el full text y verificar el pasaje exacto. Si una fuente deja de recuperarse en una sesión futura, se usa `ACCESS_RECHECK_REQUIRED`.

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
PHASE_0 = CLOSED / APPROVED
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED / FROZEN
PHASE_0D = CLOSED / APPROVED / FROZEN
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
MASTER_WRITING_AND_DELIVERY_PROTOCOL = MWDP_V1.0 / FROZEN
TARGET_JOURNAL = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
PHASE_1 = ELIGIBLE_FOR_OPENING / NEXT
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = OPEN_PHASE_1_METHODS_ENTRY_GATE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_UNTIL_PHASE_1_BLOCK_PROMPT
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### Overall state

- Working branch: `article/main-manuscript`.
- `Phase 0 = CLOSED / APPROVED`.
- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `CLOSED / APPROVED`; blocks 0B-01 through 0B-06 remain `APPROVED / FROZEN`.
- Phase 0C: `CLOSED / APPROVED / FROZEN`.
- Phase 0D: `CLOSED / APPROVED / FROZEN`.
- `0D1 = CLOSED / APPROVED / FROZEN`.
- `0D2 = CLOSED / APPROVED / FROZEN`.
- `0D_V02_INTERNAL_REVIEW = PASS`.
- `0D2_V02_INTERNAL_REVIEW = PASS`.
- `0D_AUTHOR_APPROVAL = RECEIVED`.
- `BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS`.
- `MASTER_WRITING_AND_DELIVERY_PROTOCOL = MWDP_V1.0 / FROZEN`.
- `TARGET_JOURNAL = Knowledge-Based Systems`.
- `PLAN_B = Expert Systems with Applications`.
- `PLAN_C = Information Processing & Management`.
- `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`.
- `PHASE_1 = ELIGIBLE_FOR_OPENING / NEXT`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_UNTIL_PHASE_1_BLOCK_PROMPT`.

### Canonical Phase-0 closure artifacts

The author approval, canonical 0D freeze, frozen `MWDP_V1.0`, bibliographic full-text access audit, and formal Phase-0 closure are respectively recorded in `article/reviews/0D_AUTHOR_APPROVAL.md`, `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`, `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`, `article/reviews/0D2_BIBLIOGRAPHIC_FULLTEXT_ACCESS_AUDIT.md`, and `article/reviews/0_PHASE_CLOSURE.md`.

### Frozen pre-drafting governance

```text
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = FROZEN
WRITING_POLICY_STATUS = FROZEN
CLAIM_EVIDENCE_PROTOCOL_STATUS = FROZEN
MD_DOCX_WORKFLOW_STATUS = FROZEN
WORD_CITATION_COMMENT_PROTOCOL_STATUS = FROZEN
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
JOURNAL_CASCADE_STATUS = FROZEN
```

The Writing AI owns block Markdown and cumulative candidate Markdown/Word generation and update. `MWDP_V1.0` must be read and fully followed in every Phase-1-or-later block. The internal Word master is bilingual; Word alone carries provisional APA-7 presentation; Markdown remains the source-traceability layer; final Mendeley management belongs to the author; each English Word citation carries the mandatory anchored audit comment; approved-master integrity is preserved; and block/candidate/integration revisions remain distinct.

### Bibliographic gate — PASSED

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

This does not mean 62 local PDFs exist, nor does `PASS` authorize citation from memory. Every future citation must re-retrieve the relevant full text and verify the exact supporting passage. Future retrieval failure triggers `ACCESS_RECHECK_REQUIRED`.

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
PHASE_0 = CLOSED / APPROVED
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED / FROZEN
PHASE_0D = CLOSED / APPROVED / FROZEN
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
MASTER_WRITING_AND_DELIVERY_PROTOCOL = MWDP_V1.0 / FROZEN
TARGET_JOURNAL = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
PHASE_1 = ELIGIBLE_FOR_OPENING / NEXT
NEXT_ACTOR = MANAGING_AI
NEXT_ACTION = OPEN_PHASE_1_METHODS_ENTRY_GATE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED_UNTIL_PHASE_1_BLOCK_PROMPT
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```
