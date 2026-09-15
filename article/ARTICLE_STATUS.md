# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**; `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- `0C — Gap, contribución y Research Questions`: **`CLOSED / APPROVED / FROZEN`**.
- `0D-1 — Arquitectura editorial y journal fit`: **`INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`**.
- `0D_V02_INTERNAL_REVIEW = PASS`.
- `0D_M01 = CLOSED`.
- `0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío`: **`REVISION_REQUIRED`**.
- `0D2_V01 = COMPLETED_PENDING_EDITORIAL_REVIEW` en commit `2199c58c71b5703a174c3a7b2fa57018a1700136`.
- `0D2_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS`.
- `0D2_M01 = OPEN`.
- `0D2_M02 = OPEN`.
- `0D2_M03 = OPEN`.
- `0D2_M04 = OPEN`.
- `PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems`.
- `ALTERNATIVE_TARGET_1 = Expert Systems with Applications`.
- `ALTERNATIVE_TARGET_2 = Information Processing & Management`.
- `TARGET_JOURNAL = PENDING_0D2_AND_AUTHOR_APPROVAL`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = NOT_REQUESTED`.
- `FREEZE_0D = NOT_AUTHORIZED`.
- `PHASE_1 = BLOCKED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para este gate editorial.

### Posicionamiento científico preservado

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

El contrato funcional sigue siendo:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Se mantienen las fronteras obligatorias:

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`;
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`;
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`;
- `JOURNAL_FIT ≠ NOVELTY_PROOF`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### Resultado de revisión 0D-2 V01

La V01 pasa científicamente, pero requiere cuatro correcciones editoriales/operativas antes del freeze:

1. **0D2-M01 — requisitos KBS potencialmente reescribientes:** separar requisitos verificados por fuente primaria, no verificados pero capaces de producir reescritura y diferibles sin riesgo; no tratar como no bloqueante aquello que pueda afectar longitud, formato inicial o arquitectura sin una política conservadora explícita que neutralice el riesgo.
2. **0D2-M02 — layout lingüístico del Word:** la propuesta de Word bilingüe EN+ES no fue aprobada expresamente por el autor. Debe presentarse como decisión pendiente frente a la alternativa Word maestro solo en inglés con control bilingüe en `.md`/gobernanza.
3. **0D2-M03 — APA 7:** APA 7 provisional es exclusivamente una capa de presentación del Word. Markdown debe ser capa de trazabilidad de fuentes/citas, no una segunda autoridad de formato APA 7.
4. **0D2-M04 — versionado:** separar revisión del bloque, revisión del master candidato e integración aprobada del master.

Gobiernan para esta corrección:

- `article/reviews/0D2_INTERNAL_REVIEW.md`;
- `article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_REVISION_V02.md`.

### Estado experimental relevante

El snapshot experimental permanece en solo lectura:

```text
SRC-03 branch = docs/plan-maestro-temporal-2026-08-31
SRC-03 HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
SRC-03 blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
GROUP3 = NEXT / NOT_STARTED
```

0D-2 no modifica ni reconcilia estados experimentales.

### Gate vigente

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2 = REVISION_REQUIRED
0D2_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS
0D2_M01 = OPEN
0D2_M02 = OPEN
0D2_M03 = OPEN
0D2_M04 = OPEN
NEXT_ACTOR = IA_DE_REDACCION
PROMPT = article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_REVISION_V02.md
EXPECTED_RESPONSE = article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V02.md
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `CLOSED / APPROVED`; 0B-01 through 0B-06 are `APPROVED / FROZEN`.
- Phase 0C: `CLOSED / APPROVED / FROZEN`.
- `0D-1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`.
- `0D_V02_INTERNAL_REVIEW = PASS`; `0D_M01 = CLOSED`.
- `0D-2 = REVISION_REQUIRED`.
- `0D2_V01 = COMPLETED_PENDING_EDITORIAL_REVIEW` at commit `2199c58c71b5703a174c3a7b2fa57018a1700136`.
- `0D2_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS`.
- `0D2_M01` through `0D2_M04` are `OPEN`.
- Primary target recommendation remains Knowledge-Based Systems; alternatives remain Expert Systems with Applications and Information Processing & Management.
- `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = NOT_REQUESTED`.
- `FREEZE_0D = NOT_AUTHORIZED`.
- `PHASE_1 = BLOCKED`; `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` for this editorial gate.

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

The functional contract and all frozen claim boundaries remain unchanged.

### 0D-2 V01 review result

V01 passes scientifically but requires four editorial/operational corrections before freeze:

1. **0D2-M01:** distinguish primary-verified KBS requirements, unverified but rewrite-relevant requirements, and safely deferable requirements; any item capable of affecting length, initial format, or architecture must either be neutralized by an explicit conservative drafting policy or remain blocking.
2. **0D2-M02:** bilingual EN+ES Word layout was not explicitly approved by the author and must remain a pending decision against an English-only Word master with bilingual control in Markdown/governance.
3. **0D2-M03:** provisional APA 7 is a Word-only presentation layer; Markdown is a source/citation traceability layer, not a second APA-7 formatting authority.
4. **0D2-M04:** separate block revision, candidate-master revision, and approved master integration version counters.

The correction is governed by:

- `article/reviews/0D2_INTERNAL_REVIEW.md`;
- `article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_REVISION_V02.md`.

### Current gate

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2 = REVISION_REQUIRED
0D2_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS
0D2_M01 = OPEN
0D2_M02 = OPEN
0D2_M03 = OPEN
0D2_M04 = OPEN
NEXT_ACTOR = WRITING_AI
PROMPT = article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_REVISION_V02.md
EXPECTED_RESPONSE = article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V02.md
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```
