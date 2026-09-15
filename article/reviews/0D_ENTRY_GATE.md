# Gate de entrada 0D / 0D Entry Gate

## Español

### 1. Dictamen

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
TARGET_JOURNAL = PENDING_0D
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

Se cumplen las dependencias editoriales de `0D — Arquitectura editorial y journal fit`: 0A, 0B y 0C están cerrados/aprobados, y el posicionamiento científico provisional de 0C está congelado con la alternativa B — arquitectónica-metodológica como contribución central provisional.

La apertura de 0D no declara novelty final, no convierte los gaps candidatos de 0C en ausencia universal de prior art y no autoriza todavía la redacción de secciones del manuscrito.

### 2. Estado científico transferido desde 0C

```text
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
EMPIRICAL_GAP_CANDIDATE = RETAINED_AS_BOUNDED_POSITIONING_COMPONENT
METHODOLOGICAL_GAP_CANDIDATE = RETAINED_FOR_PROVISIONAL_0C_POSITIONING
DECISION_SUPPORT_AUDITABILITY_GAP = NOT_SELECTED_AS_INDEPENDENT_PRIMARY_GAP
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El objeto diferenciador transferido a 0D es el contrato funcional completo evaluado:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Este contrato es una formulación de posicionamiento; no prueba novelty por sí mismo.

### 3. Dependencias y límites experimentales

El snapshot vivo `SRC-03` permanece en:

```text
branch = docs/plan-maestro-temporal-2026-08-31
HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
```

No existe drift nuevo desde el snapshot consumido por 0C.

Se mantienen:

```text
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
```

Por tanto, 0D puede decidir estructura editorial y journal fit sin utilizar EXP-11B como claim del artículo y sin cerrar inferencialmente HE2/HE5.

### 4. Alcance autorizado de 0D

0D debe decidir, de manera trazable y sin redactar el manuscrito:

1. estructura IMRaD definitiva y orden lógico de subsecciones;
2. mapa de tablas y figuras esenciales;
3. matriz de secciones redactables inmediatamente frente a secciones bloqueadas por resultados/gates pendientes;
4. journal fit mediante verificación web actual de scope, tipos de artículo, límites editoriales relevantes, políticas de datos/código/reproducibilidad y artículos recientes relacionados;
5. un target journal principal y al menos dos alternativas justificadas;
6. riesgos de novelty, validez, leakage, dependencia, generalización y overclaiming;
7. recomendación final para el Gate de Fase 0: `PASS`, `PASS_WITH_CORRECTIONS` o `BLOCKED`.

### 5. Targets preliminares que deben evaluarse

Según `ARTICLE_WRITING_PLAN.md`, deben evaluarse como mínimo:

1. Knowledge-Based Systems;
2. Expert Systems with Applications;
3. Information Processing & Management;
4. Decision Support Systems;
5. Government Information Quarterly;
6. Artificial Intelligence and Law, solo si el énfasis jurídico-normativo final lo justifica.

0D puede descartar candidatos por falta de fit. Puede añadir como máximo dos alternativas adicionales si la búsqueda web actual demuestra un ajuste sustancialmente mejor, explicando la razón.

### 6. Reglas de journal fit

La evaluación debe usar preferentemente fuentes oficiales del journal/editorial para:

- aims & scope;
- tipos de artículo;
- requisitos de extensión/estructura cuando existan;
- políticas de datos, código, materiales suplementarios y reproducibilidad;
- política relevante sobre uso/declaración de IA si afecta la preparación del manuscrito;
- costos/APC solo como dato operativo, nunca como criterio científico principal.

Los artículos recientes usados para demostrar fit temático deben verificarse en fuentes primarias y no confundirse con evidencia de novelty.

`JOURNAL_FIT ≠ NOVELTY_PROOF`.

### 7. Prohibiciones

Durante 0D no está autorizado:

- modificar el Plan Maestro experimental;
- modificar resultados experimentales;
- integrar EXP-11B en claims antes de reconciliar C10/C11;
- cerrar HE2/HE5 inferencialmente antes del gate aplicable;
- ejecutar experimentos;
- reabrir 0B como búsqueda bibliográfica de gap;
- utilizar artículos recientes de journal fit para reescribir silenciosamente los freezes de literatura;
- declarar ausencia universal de prior art;
- declarar novelty final por mera diferencia arquitectónica;
- redactar Methods, Related Work, Results, Introduction u otra sección del manuscrito;
- abrir Fase 1 antes de cerrar y aprobar 0D.

### 8. Gate

```text
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
NEXT_ACTOR = IA_DE_REDACCION
EXPERIMENTAL_REVIEW = NOT_REQUIRED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

---

## English

### 1. Verdict

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
TARGET_JOURNAL = PENDING_0D
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

The editorial dependencies for `0D — Editorial architecture and journal fit` are satisfied. Phases 0A, 0B and 0C are closed/approved, and 0C has frozen Alternative B — architectural-methodological — as the provisional central positioning contribution.

Opening 0D does not declare final novelty, convert bounded gap candidates into universal prior-art absence, or authorize manuscript drafting.

### 2. Transferred scientific state

0D inherits the frozen 0C positioning: the methodological-gap candidate is the main provisional positioning basis, the empirical-gap candidate remains bounded support, decision-support/auditability is not an independent primary gap, RQ1/RQ2 are retained, RQ3 remains under HE4 limitations, and RQ4 remains conditional on Group 3. Final gap and novelty remain undeclared.

The differentiating object is the evaluated complete functional contract: externally fixed historical ranking; post-ranking normative evidence without reranking; downstream explanation-only generation; no insertion/deletion/substitution/reordering; no classification feedback; DAM-aware partitioning where dependence exists; and function-specific evaluation. This is positioning, not novelty proof.

### 3. Experimental boundaries

The live `SRC-03` branch remains at HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, unchanged from the 0C snapshot. RQ4 remains conditional on Group 3. EXP-11B article use remains blocked until explicit C10/C11 reconciliation.

### 4. Authorized 0D scope

0D must decide the final IMRaD/subsection architecture, essential tables/figures, immediately draftable versus experimentally blocked sections, current journal fit using web verification, one primary target plus at least two alternatives, the main novelty/validity/leakage/dependence/generalization/overclaiming risks, and the Phase-0 gate verdict (`PASS`, `PASS_WITH_CORRECTIONS`, or `BLOCKED`).

At minimum it must evaluate Knowledge-Based Systems, Expert Systems with Applications, Information Processing & Management, Decision Support Systems, Government Information Quarterly, and Artificial Intelligence and Law when legally justified. Up to two additional candidates may be added only if current evidence shows materially better fit.

Official publisher/journal sources should govern aims/scope, article types, length/structure rules, data/code/reproducibility policies, and relevant AI-disclosure rules. Recent related articles demonstrate topical fit only; they do not prove novelty.

### 5. Prohibitions and gate

0D may not alter experiments, use EXP-11B claims before C10/C11 reconciliation, prematurely close HE2/HE5, reopen the frozen literature map, turn journal-fit literature into silent gap revision, declare universal prior-art absence, infer novelty from architecture alone, draft manuscript sections, or open Phase 1 before 0D closes.

```text
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
NEXT_ACTOR = WRITING_AI
EXPERIMENTAL_REVIEW = NOT_REQUIRED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```
