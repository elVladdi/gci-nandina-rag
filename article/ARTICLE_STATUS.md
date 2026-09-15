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
- `0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL`.
- `RQ1 = RETAINED`.
- `RQ2 = RETAINED`.
- `RQ3 = RETAINED_WITH_HE4_LIMITATIONS`.
- `RQ4 = RETAINED_CONDITIONAL_ON_GROUP3`.
- Fase activa: **`0D — Arquitectura editorial y journal fit`**.
- `0D_ENTRY_GATE = PASS / OPENED`.
- `0D = READY_FOR_DRAFTING`.
- Target journal: `PENDING_0D`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED_FOR_GAP`; búsqueda web actual sí autorizada exclusivamente para journal fit y requisitos editoriales de 0D.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para la apertura de 0D.
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
- `article/reviews/0D_ENTRY_GATE.md`;
- `article/prompts/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/DECISIONS.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/STYLE_GUIDE.md`.

La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados editoriales, gates, claims y admisión bibliográfica. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

### Snapshot experimental para apertura de 0D

`SRC-03` fue verificado en modo solo lectura:

```text
branch = docs/plan-maestro-temporal-2026-08-31
HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
```

No existe cambio desde el snapshot consumido por 0C. El estado vivo registra EXP-11B retrieval cerrado/aprobado/integrado, EXP-12 cerrado sin retrieval bajo el diseño congelado y Grupo 3 como siguiente bloque de métricas/inferencia todavía no ejecutado. 0D no puede modificar ni reinterpretar ese estado por cuenta propia.

### Posicionamiento 0C congelado transferido a 0D

La contribución central provisional adoptada es la alternativa B — arquitectónica-metodológica. El objeto diferenciador es el contrato funcional completo evaluado:

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

### Research Questions transferidas a 0D

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

La búsqueda web de 0D se limita a journal fit y requisitos editoriales actuales. Los artículos encontrados para este fin no se incorporan automáticamente al corpus congelado de 0B ni prueban novelty.

### Desfase editorial EXP-11B

```text
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
```

`SRC-03` registra EXP-11B retrieval como cerrado/aprobado/integrado, mientras C10/C11 continúan `PROHIBITED` en `CLAIM_EVIDENCE_MATRIX.md` con redacción histórica referida a retrieval pendiente. 0D no está autorizado a reconciliar ese desfase por inferencia ni a usar H150/H200 como claims del artículo.

### Alcance operativo de 0D

0D debe producir, sin redactar manuscrito:

1. arquitectura IMRaD definitiva candidata y orden lógico de subsecciones;
2. mapa de tablas y figuras esenciales;
3. matriz de secciones redactables inmediatamente y secciones bloqueadas;
4. screening actualizado de journal fit;
5. deep dive del Top-3 de journals;
6. propuesta de `PRIMARY_TARGET` y dos alternativas;
7. evaluación de riesgos científicos/editoriales;
8. recomendación de Gate de Fase 0: `PASS`, `PASS_WITH_CORRECTIONS` o `BLOCKED`.

Prompt gobernante:

`article/prompts/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT.md`.

Artefacto esperado:

`article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V01.md`.

### Fronteras obligatorias

Se mantienen:

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`;
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`;
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`;
- `JOURNAL_FIT ≠ NOVELTY_PROOF`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### Prohibiciones vigentes durante 0D

No está autorizado:

- declarar novelty final;
- convertir los gaps candidatos en ausencia universal;
- restaurar F5 general como gap;
- integrar EXP-11B como claim antes de reconciliar C10/C11;
- cerrar HE2 o HE5 antes del gate inferencial aplicable;
- equiparar auditabilidad/source support/trazabilidad con legal correctness;
- reabrir 0B mediante la búsqueda de journal fit;
- modificar Plan Maestro o resultados experimentales;
- seleccionar definitivamente revista sin auditoría editorial y aprobación del autor;
- redactar secciones del manuscrito antes del cierre de Fase 0.

### Gate vigente

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
NEXT_ACTOR = IA_DE_REDACCION
PROMPT = article/prompts/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT.md
EXPECTED_RESPONSE = article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V01.md
TARGET_JOURNAL = PENDING_0D
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Phase 0B: **`CLOSED / APPROVED`**; 0B-01 through 0B-06 are `APPROVED / FROZEN`.
- Phase 0C: **`CLOSED / APPROVED`** and `APPROVED / FROZEN`.
- Active phase: **`0D — Editorial architecture and journal fit`**.
- `0D_ENTRY_GATE = PASS / OPENED`.
- `0D = READY_FOR_DRAFTING`.
- `TARGET_JOURNAL = PENDING_0D`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- Gap-literature search remains closed; current web research is authorized only for 0D journal fit and current editorial requirements.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` at 0D entry.

### Governance and experimental state

Frozen 0A/0B/0C artifacts, the 0D entry gate, Master Writing Plan, Decisions, Source Registry, Claim–Evidence Matrix, and Style Guide govern 0D. The Experimental AI retains exclusive authority over the Master Plan and experimental decisions.

The read-only `SRC-03` snapshot remains branch `docs/plan-maestro-temporal-2026-08-31`, HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`, unchanged from 0C.

### Frozen 0C positioning transferred to 0D

Alternative B — architectural-methodological — is the frozen provisional central positioning contribution. The differentiating object is the evaluated complete functional contract: externally fixed historical ranking; post-ranking normative evidence without reranking; downstream explanation-only generation; no insertion/deletion/substitution/reordering; no classification feedback; DAM-aware partitioning where dependence exists; and function-specific evaluation.

The methodological-gap candidate remains the primary provisional positioning basis; the empirical-gap candidate is bounded support; decision-support/auditability is not an independent primary gap. Final gap and novelty remain undeclared.

RQ1/RQ2 are retained; RQ3 is retained under HE4 limitations; RQ4 remains conditional on Group 3.

### EXP-11B governance lag

```text
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
```

0D may not reconcile this lag by inference or use H150/H200 as article claims.

### Authorized 0D scope

0D must produce the candidate final IMRaD/subsection architecture, essential table/figure map, draftability matrix, current journal-fit screening, top-three journal deep dive, one primary and two alternative targets, scientific/editorial risk assessment, and a Phase-0 gate recommendation (`PASS`, `PASS_WITH_CORRECTIONS`, or `BLOCKED`).

Governing prompt:

`article/prompts/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT.md`.

Expected artifact:

`article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V01.md`.

### Mandatory boundaries

0D preserves the distinctions among literature gap, project feature, scientific contribution, experimental result and novelty claim; bounded and universal absence; architectural difference and novelty; journal fit and novelty proof; candidate retrieval and overall accuracy; normative association and legal correctness; auditability and legal correctness; configurability and empirical generalization.

### Current gate

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
NEXT_ACTOR = WRITING_AI
PROMPT = article/prompts/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT.md
EXPECTED_RESPONSE = article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V01.md
TARGET_JOURNAL = PENDING_0D
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```
