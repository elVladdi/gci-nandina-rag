# 0C — Posicionamiento científico congelado / Frozen Scientific Positioning

## Español

### 1. Estado

```text
0C = APPROVED / FROZEN
0C_INTERNAL_REVIEW = PASS
0C_AUTHOR_APPROVAL = RECEIVED
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
EXPERIMENTAL_REVIEW = NOT_REQUIRED
0D = NOT_STARTED / OPENING_NOT_AUTHORIZED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

Este artefacto congela el resultado editorial de 0C. No declara novelty final ni transforma el posicionamiento candidato en una afirmación de ausencia universal de prior art.

### 2. Fuentes gobernantes

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- freezes de `0B-01` a `0B-06`;
- `article/reviews/0B_PHASE_CLOSURE.md`;
- `article/reviews/0C_ENTRY_GATE.md`;
- `article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md`;
- `article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`;
- `article/reviews/0C_INTERNAL_REVIEW.md`;
- `article/reviews/0C_AUTHOR_APPROVAL.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `SRC-03` en modo solo lectura.

### 3. Estado bibliográfico heredado de 0B

Se conserva sin reinterpretación:

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

Consecuencias:

- F1 y F3 no prueban inexistencia universal ni novelty;
- F2 solo sobrevive bajo aislamiento estricto entre ranking upstream y explicación downstream;
- F4 permanece como frontera metodológica;
- F5 general queda descartado como gap independiente;
- el componente de auditabilidad solo puede usarse de forma contextual y acotada.

### 4. Contribución central provisional congelada

Se adopta para posicionamiento editorial la alternativa B — arquitectónica-metodológica:

> El artículo puede contribuir mediante la formalización y evaluación de un contrato arquitectónico-metodológico en el que la recuperación histórica fija el ranking de candidatos, la recuperación normativa solo documenta esos candidatos y un LLM local downstream explica un Top-3 inmutable sin capacidad de insertar, eliminar, sustituir, reordenar ni retroalimentar la clasificación. La evaluación acompaña ese contrato con particiones agrupadas por DAM cuando existe dependencia y métricas separadas para ranking, evidencia y explicación/auditabilidad.

El objeto diferenciador no es la mera existencia de los componentes, sino el **contrato funcional completo evaluado**:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Esta formulación es provisional de posicionamiento. No implica que cada componente sea nuevo ni constituye una declaración final de novelty.

### 5. Familias de gap para consumo posterior

```text
EMPIRICAL_GAP_CANDIDATE = RETAINED_AS_BOUNDED_POSITIONING_COMPONENT
METHODOLOGICAL_GAP_CANDIDATE = RETAINED_FOR_PROVISIONAL_0C_POSITIONING
DECISION_SUPPORT_AUDITABILITY_GAP = NOT_SELECTED_AS_INDEPENDENT_PRIMARY_GAP
FINAL_GAP = NOT_DEFINED
```

El gap metodológico candidato es la base principal del posicionamiento provisional. El gap empírico se conserva como componente acotado. El gap de apoyo a decisiones/auditabilidad no se adopta como gap primario independiente debido al prior art directo identificado en 0B-06.

### 6. Research Questions retenidas

- **RQ1 — RETAINED:** ¿Qué desempeño de recuperación de candidatos alcanza la recuperación histórica en el benchmark v0.2 cuando las particiones se mantienen disjuntas por DAM?
- **RQ2 — RETAINED:** ¿En qué medida puede asociarse evidencia normativa identificable a cada candidato de un Top-3 histórico fijo sin alterar su orden?
- **RQ3 — RETAINED_WITH_HE4_LIMITATIONS:** ¿En qué medida un LLM local restringido a un Top-3 inmutable conserva candidatos y orden y produce explicaciones estructuradas con evidencia identificable bajo el protocolo HE4?
- **RQ4 — RETAINED_CONDITIONAL_ON_GROUP3:** ¿Qué límites de validez introducen la dependencia intra-DAM, los near-duplicates residuales, la composición del banco histórico y el drift normativo en la interpretación de los resultados del piloto?

RQ4 no puede cerrarse inferencialmente antes de Grupo 3. RQ3 queda limitada por la muestra HE4, el evaluador IA y el mismatch prompt–schema ya congelado.

### 7. Mapeo OE/HE congelado para alcance del artículo

- OE1, HE1: `IN_PAPER` dentro de sus límites de reproducibilidad/provenance.
- OE2: `IN_PAPER`; HE2: `CONDITIONAL` hasta el gate inferencial aplicable.
- OE3: `IN_PAPER`; HE3: `CONDITIONAL` por el carácter limitado del reranker diagnóstico.
- OE4, HE4: `IN_PAPER` con las limitaciones HE4 congeladas.
- OE5: `IN_PAPER`; HE5: `CONDITIONAL` hasta Grupo 3.

`IN_PAPER` significa pertinencia temática y evidencia suficiente para consideración editorial posterior; no equivale a confirmación inferencial automática de una hipótesis.

### 8. Desfase EXP-11B

El Plan Maestro vivo registra EXP-11B retrieval como cerrado/aprobado/integrado, mientras C10/C11 permanecen en `CLAIM_EVIDENCE_MATRIX.md` como `PROHIBITED` con redacción histórica referida a retrieval pendiente.

```text
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
```

0C no modifica C10/C11 y no utiliza la dirección H150/H200 para sostener la contribución provisional, los gaps candidatos ni las RQs.

### 9. Fronteras obligatorias

Continúan vigentes:

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`;
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`;
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### 10. Prohibiciones tras el freeze

El freeze de 0C no autoriza:

- declarar novelty final;
- afirmar ausencia universal de prior art;
- usar F5 general como gap;
- usar EXP-11B como claim del artículo antes de reconciliar C10/C11;
- cerrar HE2 o HE5 antes del gate inferencial correspondiente;
- abrir 0D automáticamente;
- seleccionar revista;
- redactar el manuscrito.

### 11. Próximo gate

```text
0C = APPROVED / FROZEN
0D = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = DEFINE_0D_SCOPE_AND_ENTRY_GATE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### 1. Status

```text
0C = APPROVED / FROZEN
0C_INTERNAL_REVIEW = PASS
0C_AUTHOR_APPROVAL = RECEIVED
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
EXPERIMENTAL_REVIEW = NOT_REQUIRED
0D = NOT_STARTED / OPENING_NOT_AUTHORIZED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

This artifact freezes the editorial outcome of 0C. It does not declare final novelty or turn bounded positioning into a universal prior-art absence claim.

### 2. Frozen provisional central contribution

Alternative B — architectural-methodological — is adopted for provisional editorial positioning. The article may contribute by formalizing and evaluating a functional contract in which historical retrieval fixes the candidate ranking, normative retrieval only documents those candidates, and a downstream local LLM explains an immutable Top-3 without inserting, deleting, substituting, reordering, or feeding back into classification. Evaluation pairs this contract with DAM-aware partitioning where dependence exists and function-specific metrics.

The differentiating object is the evaluated complete contract, not the mere existence or novelty of its individual components.

### 3. Gap families and RQs

The methodological-gap candidate is retained as the main provisional positioning basis; the empirical-gap candidate remains a bounded supporting component; decision-support/auditability is not selected as an independent primary gap. `FINAL_GAP = NOT_DEFINED`.

RQ1 and RQ2 are retained; RQ3 is retained under HE4 limitations; RQ4 remains conditional on Group 3.

### 4. OE/HE scope

OE1–OE5 remain eligible for the paper within their documented boundaries. HE2, HE3 and HE5 remain conditional as specified by the internal review; HE4 remains bounded by the executed HE4 protocol. `IN_PAPER` does not mean inferential confirmation.

### 5. EXP-11B governance lag

The live Master Plan records EXP-11B retrieval as closed/approved/integrated while C10/C11 remain prohibited in the editorial Claim–Evidence Matrix under historical pending-retrieval wording. 0C does not alter C10/C11 or use H150/H200 direction as positioning support. Explicit C10/C11 reconciliation is required before any article use of EXP-11B results.

### 6. Mandatory boundaries

The frozen positioning preserves the distinctions between literature gap, project feature, scientific contribution, experimental result and novelty claim; bounded search absence and universal absence; architectural difference and novelty; candidate retrieval and overall system accuracy; normative association and legal correctness; auditability and legal correctness; configurability and empirical generalization.

### 7. Next gate

```text
0C = APPROVED / FROZEN
0D = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = DEFINE_0D_SCOPE_AND_ENTRY_GATE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```