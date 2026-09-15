# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**.
- `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- `0C — Gap, contribución y Research Questions`: **`CLOSED / APPROVED`**.
- `0C`: **`APPROVED / FROZEN`**.
- `0C_INTERNAL_REVIEW = PASS`.
- `0C_AUTHOR_APPROVAL = RECEIVED`.
- `0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL`.
- `RQ1 = RETAINED`.
- `RQ2 = RETAINED`.
- `RQ3 = RETAINED_WITH_HE4_LIMITATIONS`.
- `RQ4 = RETAINED_CONDITIONAL_ON_GROUP3`.
- `0D — Arquitectura editorial y journal fit`: **`NOT_STARTED / OPENING_NOT_AUTHORIZED`**.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para el cierre de 0C.
- Corpus heredado consolidado: `62` obras/documentos con acceso primario verificable `62/62`.
- Registro de nueva literatura: `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.

### Gobernanza vigente

Gobiernan:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- freezes `0B-01` a `0B-06`;
- `article/reviews/0B_PHASE_CLOSURE.md`;
- `article/reviews/0C_ENTRY_GATE.md`;
- `article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md`;
- `article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`;
- `article/reviews/0C_INTERNAL_REVIEW.md`;
- `article/reviews/0C_AUTHOR_APPROVAL.md`;
- `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
- `article/reviews/0C_PHASE_CLOSURE.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/DECISIONS.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/STYLE_GUIDE.md`.

La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados editoriales, gates, claims y admisión bibliográfica. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

### Snapshot experimental consumido por 0C

`SRC-03` fue consultado en modo solo lectura:

```text
branch = docs/plan-maestro-temporal-2026-08-31
HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
```

El estado vivo registra EXP-11B retrieval cerrado/aprobado/integrado, EXP-12 cerrado sin retrieval bajo el diseño congelado y Grupo 3 como siguiente bloque de métricas/inferencia todavía no ejecutado. 0C no modifica ese estado.

### Posicionamiento 0C congelado

La contribución central provisional adoptada es la alternativa B — arquitectónica-metodológica. El objeto diferenciador es el contrato funcional completo evaluado, no la mera existencia de sus componentes:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Estado de las familias de gap:

```text
EMPIRICAL_GAP_CANDIDATE = RETAINED_AS_BOUNDED_POSITIONING_COMPONENT
METHODOLOGICAL_GAP_CANDIDATE = RETAINED_FOR_PROVISIONAL_0C_POSITIONING
DECISION_SUPPORT_AUDITABILITY_GAP = NOT_SELECTED_AS_INDEPENDENT_PRIMARY_GAP
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No se autoriza afirmar que cada componente sea novedoso ni que exista ausencia universal de prior art.

### Research Questions congeladas para 0D

```text
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
```

RQ4 no puede cerrarse inferencialmente antes de Grupo 3. RQ3 conserva las limitaciones HE4 ya congeladas.

### Estado bibliográfico heredado de 0B

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F4 = METHODOLOGICAL_BOUNDARY_NOT_INDEPENDENT_NOVELTY
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
G6 = ELIMINATED_AS_GAP_CANDIDATE
G7 = MERGED_INTO_F2
```

N01 permanece `APPROVED_NEW`; N02 `REVIEW_REQUIRED / NOT_ADMITTED_YET`; N03 y N04 `REJECT`.

### Desfase editorial EXP-11B

```text
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
```

`SRC-03` registra EXP-11B retrieval como cerrado/aprobado/integrado, mientras C10/C11 continúan `PROHIBITED` en `CLAIM_EVIDENCE_MATRIX.md` con redacción histórica referida a retrieval pendiente. La aprobación del autor ordena no integrar EXP-11B en claims del artículo hasta reconciliar explícitamente C10/C11.

### Fronteras obligatorias

Se mantienen:

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`;
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`;
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### Prohibiciones vigentes tras el freeze

No está autorizado:

- declarar novelty final;
- convertir los gaps candidatos en ausencia universal;
- restaurar F5 general como gap;
- integrar EXP-11B como claim antes de reconciliar C10/C11;
- cerrar HE2 o HE5 antes del gate inferencial aplicable;
- equiparar auditabilidad/source support/trazabilidad con legal correctness;
- abrir 0D sin un gate de entrada separado;
- seleccionar revista antes de 0D;
- redactar secciones del manuscrito antes del cierre de Fase 0.

### Gate vigente

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = DEFINE_0D_SCOPE_AND_ENTRY_GATE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Phase 0B: **`CLOSED / APPROVED`**; 0B-01 through 0B-06 are `APPROVED / FROZEN`.
- Phase 0C: **`CLOSED / APPROVED`** and `APPROVED / FROZEN`.
- `0C_INTERNAL_REVIEW = PASS`.
- `0C_AUTHOR_APPROVAL = RECEIVED`.
- `0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL`.
- RQ1/RQ2 retained; RQ3 retained under HE4 limitations; RQ4 retained conditional on Group 3.
- Phase 0D: **`NOT_STARTED / OPENING_NOT_AUTHORIZED`**.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` for 0C closure.

### Frozen 0C positioning

Alternative B — architectural-methodological — is the frozen provisional central positioning contribution. The differentiating object is the evaluated complete functional contract: externally fixed historical ranking; post-ranking normative evidence without reranking; downstream explanation-only generation; no insertion/deletion/substitution/reordering; no classification feedback; DAM-aware partitioning where dependence exists; and function-specific evaluation.

The methodological-gap candidate is retained as the primary provisional positioning basis; the empirical-gap candidate remains a bounded supporting component; decision-support/auditability is not selected as an independent primary gap. Final gap and novelty remain undeclared.

### RQs

RQ1 and RQ2 are retained; RQ3 remains under HE4 limitations; RQ4 remains conditional on Group 3.

### EXP-11B governance lag

```text
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
```

Current `SRC-03` records EXP-11B retrieval as closed/approved/integrated, while C10/C11 remain prohibited under historical pending-retrieval wording in the Claim–Evidence Matrix. EXP-11B may not be used as an article claim until explicit C10/C11 reconciliation.

### Current gate

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = DEFINE_0D_SCOPE_AND_ENTRY_GATE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

0D must be opened through a separate entry gate. The current state does not authorize journal selection or manuscript drafting.