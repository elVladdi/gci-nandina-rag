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
- `0D_DRAFTING_ANALYSIS = COMPLETED`.
- `0D_INTERNAL_REVIEW = PASS_WITH_MINOR_CORRECTIONS`.
- `0D_V02_INTERNAL_REVIEW = PASS`.
- `0D_M01 = CLOSED`.
- `0D = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- `PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems`.
- `ALTERNATIVE_TARGET_1 = Expert Systems with Applications`.
- `ALTERNATIVE_TARGET_2 = Information Processing & Management`.
- `PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS`.
- `TARGET_JOURNAL = PENDING_AUTHOR_APPROVAL`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = PENDING`.
- `FREEZE_0D = NOT_AUTHORIZED_YET`.
- `PHASE_1 = BLOCKED_UNTIL_0D_AND_PHASE_0_CLOSE`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED_FOR_GAP`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para el gate editorial actual.
- Corpus heredado consolidado: `62` obras/documentos con acceso primario verificable `62/62`.
- Registro de nueva literatura: `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.

### Gobernanza vigente

Gobiernan:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- freezes `0B-01` a `0B-06`;
- `article/reviews/0B_PHASE_CLOSURE.md`;
- `article/reviews/0C_ENTRY_GATE.md`;
- `article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`;
- `article/reviews/0C_INTERNAL_REVIEW.md`;
- `article/reviews/0C_AUTHOR_APPROVAL.md`;
- `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
- `article/reviews/0C_PHASE_CLOSURE.md`;
- `article/reviews/0D_ENTRY_GATE.md`;
- `article/prompts/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT.md`;
- `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V01.md`;
- `article/reviews/0D_INTERNAL_REVIEW.md`;
- `article/prompts/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_REVISION_V02.md`;
- `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`;
- `article/reviews/0D_V02_INTERNAL_REVIEW.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/DECISIONS.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/STYLE_GUIDE.md`.

La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados editoriales, gates, claims y admisión bibliográfica. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

### Snapshot experimental consumido por 0D

`SRC-03` fue consultado en modo solo lectura:

```text
branch = docs/plan-maestro-temporal-2026-08-31
HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
GROUP3 = NEXT / NOT_STARTED
```

No se introdujo interpretación experimental nueva en 0D.

### Posicionamiento 0C congelado transferido a 0D

La contribución central provisional continúa siendo la alternativa B — arquitectónica-metodológica. El objeto diferenciador es el contrato funcional completo evaluado:

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

### Research Questions

```text
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
```

RQ4 no puede cerrarse inferencialmente antes de Grupo 3.

### Resultado 0D y journal fit

La V02 corrigió la única observación terminológica de V01. `0D_M01 = CLOSED`.

La recomendación editorial que pasa al autor es:

```text
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
```

La selección todavía no es definitiva. Requiere aprobación expresa del autor durante el freeze de 0D.

La arquitectura editorial candidata acepta como redactables tras el cierre de Fase 0, entre otros:

- Methods 3.1, 3.3–3.6: `DRAFTABLE_NOW`;
- Methods 3.2, 3.7–3.9: `DRAFTABLE_WITH_FROZEN_LIMITATIONS`;
- Related Work 2.1–2.4: `DRAFTABLE_NOW`;
- Related Work 2.5: `DRAFTABLE_WITH_FROZEN_LIMITATIONS`;
- Results 4.1–4.2: `DRAFTABLE_NOW`;
- Results 4.3–4.5: `DRAFTABLE_WITH_FROZEN_LIMITATIONS`.

Se mantienen bloqueados:

- Results 4.6: `BLOCKED_BY_GROUP3`;
- Results 4.7/EXP-11B: `BLOCKED_BY_C10_C11_RECONCILIATION`;
- Discussion final y Conclusions: `BLOCKED_BY_FINAL_RESULTS`;
- Abstract y Title definitivo: `DEFER_TO_LATE_STAGE`.

### Desfase editorial EXP-11B y dependencias posteriores

```text
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
```

Estas condiciones no bloquean el cierre de 0D ni el inicio posterior de bloques redactables, pero sí restringen el contenido final del manuscrito.

### Gate de Fase 0 recomendado

```text
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
```

Las condiciones que permanecerían abiertas después del cierre de Fase 0 son:

1. reconciliar C10/C11 antes de utilizar EXP-11B;
2. cerrar Grupo 3 antes del cierre inferencial final de RQ4/HE2/HE5;
3. preservar `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` hasta el gate posterior aplicable;
4. revalidar la guía exacta del target final antes de submission.

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

### Gate vigente

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
NEXT_ACTOR = AUTHOR
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
TARGET_JOURNAL = PENDING_AUTHOR_APPROVAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = PENDING
FREEZE_0D = NOT_AUTHORIZED_YET
PHASE_1 = BLOCKED_UNTIL_0D_AND_PHASE_0_CLOSE
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
- Active phase: **`0D — Editorial architecture and journal fit`**.
- `0D_DRAFTING_ANALYSIS = COMPLETED`.
- `0D_V02_INTERNAL_REVIEW = PASS`.
- `0D_M01 = CLOSED`.
- `0D = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- `PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems`.
- `ALTERNATIVE_TARGET_1 = Expert Systems with Applications`.
- `ALTERNATIVE_TARGET_2 = Information Processing & Management`.
- `PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS`.
- `TARGET_JOURNAL = PENDING_AUTHOR_APPROVAL`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = PENDING`.
- `FREEZE_0D = NOT_AUTHORIZED_YET`.
- `PHASE_1 = BLOCKED_UNTIL_0D_AND_PHASE_0_CLOSE`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` for the current editorial gate.

### Governance and experimental state

Frozen 0A/0B/0C artifacts, the 0D entry gate, 0D V01/V02 responses, internal reviews, Master Writing Plan, Decisions, Source Registry, Claim–Evidence Matrix, and Style Guide govern the current state. The Experimental AI retains exclusive authority over the Master Plan and experimental decisions.

The read-only `SRC-03` snapshot remains branch `docs/plan-maestro-temporal-2026-08-31`, HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`. Group 3 remains `NEXT / NOT_STARTED`; EXP-11B is experimentally closed but remains blocked from article claims until C10/C11 reconciliation.

### Frozen positioning and RQs

Alternative B — architectural-methodological — remains the frozen provisional central positioning contribution. The differentiating object is the evaluated complete functional contract: externally fixed historical ranking; post-ranking normative evidence without reranking; downstream explanation-only generation; no insertion/deletion/substitution/reordering; no classification feedback; DAM-aware partitioning where dependence exists; and function-specific evaluation.

RQ1/RQ2 are retained; RQ3 remains under HE4 limitations; RQ4 remains conditional on Group 3. Final gap and novelty remain undeclared.

### 0D result and journal recommendation

V02 resolves the sole terminology correction from V01. `0D_M01 = CLOSED`.

The recommendation submitted to the author is:

```text
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
```

This remains a recommendation pending author approval, not a final journal selection.

After formal Phase-0 closure, Methods, Related Work, and the already frozen Results blocks identified by 0D may open according to D-003, while Group-3-dependent final inference, unreconciled EXP-11B, final Discussion/Conclusions, Abstract, and final Title remain blocked or deferred.

### Phase-0 gate recommendation

```text
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
```

The remaining conditions are downstream constraints, not V02 defects: C10/C11 reconciliation before EXP-11B article use; Group-3 closure before final RQ4/HE2/HE5 inference; final gap/novelty remain undeclared; and exact target-journal author-guide requirements must be revalidated before submission.

### Current gate

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
NEXT_ACTOR = AUTHOR
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
TARGET_JOURNAL = PENDING_AUTHOR_APPROVAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = PENDING
FREEZE_0D = NOT_AUTHORIZED_YET
PHASE_1 = BLOCKED_UNTIL_0D_AND_PHASE_0_CLOSE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```