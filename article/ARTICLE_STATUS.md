# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
PHASE_0 = CLOSED / APPROVED
PHASE_1 = OPENED / RESTRUCTURED_BY_D014
KBS_EMPIRICAL_WRITING_GUIDE = KBS_EWG_34_V01 / AUTHOR_APPROVED / ACTIVE / BINDING
ARTICLE_WRITING_PLAN = V2.2
STRUCTURE_APPROVAL_DECISION = D-015
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK_B01 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B02 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B03 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B03_REVIEW = PASS
RELATED_WORK_B03_AUTHOR_APPROVAL = RECEIVED / EFFECTIVE
CANONICAL_MASTER = ARTICLE_MASTER_V003
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V003.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V003.docx
CANONICAL_MASTER_DOCX_SHA256 = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
CANONICAL_CITATION_COMMENTS = 19
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_GATE = RELATED_WORK_B04_DRAFTING
RELATED_WORK_B04 = AUTHORIZED
AUTHORIZED_SCOPE = SECTION_2.4_ONLY
NEXT_ACTOR = DRAFTING_AI
METHODS_B01_V05 = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
```

### Estructura aprobada y orden activo

La estructura congelada por D-015 permanece:

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

Orden de redacción activo:

`Related Work → Introduction provisional → Decision-support architecture → Experimental design → Results autorizados → figures/tables → integración de resultados pendientes → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → adaptación final KBS`.

### Related Work B01

`Related Work B01 / Section 2.1` permanece `APPROVED / FROZEN / INTEGRATED` mediante D-016. Su integración canónica inicial fue `ARTICLE_MASTER_V001`; conserva ocho comentarios de auditoría de citas.

Controles heredados: `has most often been framed` es síntesis cualitativa y no una frecuencia estadística; las métricas Top-k deben nombrarse con precisión y no sustituir medidas sensibles al orden como MRR.

### Related Work B02

`Related Work B02 / Section 2.2` permanece `APPROVED / FROZEN / INTEGRATED` mediante D-017. Su integración canónica inicial fue `ARTICLE_MASTER_V002` y elevó el total acumulado a catorce comentarios de auditoría de citas.

Controles heredados de B02:

- Wang et al. (2026), `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification`, se conserva como **preprint** mientras no se verifique una versión editorial final;
- evidencia visible, citas, reasoning traces, path validity o rationale no equivalen automáticamente a auditabilidad formal ni corrección jurídica;
- la posición funcional del LLM en el pipeline debe distinguirse de su mera denominación como “LLM”.

### Cierre de Related Work B03

La entrega semántica `17802e2c10de072524acf3655d6ee8ad0b0aa892` fue auditada independientemente por la IA Gestora y aprobada expresamente por el autor. La comparación hasta el HEAD previo a la integración confirmó que los commits posteriores no modificaron los cuatro artefactos B03.

```text
B03_SECTION = 2.3 LLMs for classification, reasoning, and explanation
B03_INTERNAL_REVIEW = PASS
B03_SCIENTIFIC_CONTENT = PASS
B03_SOURCE_SUPPORT = PASS
B03_COMMENT_SOURCE_ALIGNMENT = PASS
B03_KBS_EDITORIAL_FIT = PASS
B03_EN_ES_EQUIVALENCE = PASS
B03_NEW_CITATION_COMMENT_COVERAGE = 5/5 / PASS
B03_PRIOR_COMMENTS_PRESERVED = 14/14 / PASS
B03_TOTAL_COMMENTS = 19
B03_DOCX_INTEGRITY = PASS
B03_DOCX_TRACKED_CHANGES = 0
B03_DOCX_RENDER = PASS / 21_OF_21_PAGES
B03_MATERIAL_CORRECTIONS = 0
B03_EXPERIMENTAL_REVIEW = NOT_REQUIRED
B03_AUTHOR_APPROVAL = RECEIVED / EFFECTIVE
B03_STATUS = APPROVED / FROZEN / INTEGRATED
```

La integración canónica posterior a B03 es `ARTICLE_MASTER_V003`. El DOCX canónico es binariamente equivalente al candidato B03 aprobado, conserva los diecinueve comentarios de auditoría y tiene SHA-256 `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`.

Controles heredados de B03:

- `DIRECT_GENERATIVE_LLM_CLASSIFICATION ≠ FINE_TUNED_TRANSFORMER_CLASSIFIER`;
- `RAG_CLASSIFICATION ≠ RAG_EVIDENCE_SUPPORT ≠ DOCUMENT_QA_RAG`;
- `SEARCH_CONTROL / RERANKING / NEXT_HOP_DECISION ≠ EXPLANATION_ONLY_GENERATION`;
- `RATIONALE / REASONING_TRACE ≠ FAITHFULNESS GUARANTEE`;
- `VISIBLE_CITATION / PROVENANCE ≠ FORMAL_AUDITABILITY ≠ LEGAL_CORRECTNESS`.

### Bloque activo — Related Work B04

```text
BLOCK = RELATED_WORK_B04
SECTION = 2.4 Evidence grounding, explainability, and auditability
BLOCK_REVISION = V01
DRAFTING = AUTHORIZED
BASELINE_MASTER = ARTICLE_MASTER_V003
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V003.md
BASELINE_DOCX = article/manuscript/ARTICLE_MASTER_V003.docx
BASELINE_DOCX_SHA256 = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
PRIOR_SECTIONS_2_1_TO_2_3 = APPROVED / FROZEN / PRESERVE_EXACTLY
PRIOR_CITATION_COMMENTS = 19 / PRESERVE_EXACTLY
SECTIONS_2_5_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_UNLESS_NEW_TRIGGER_APPEARS
```

B04 debe sintetizar evidence grounding, explainability, provenance/traceability y auditability sin colapsar propiedades distintas. Debe separar evidencia visible de soporte real del claim, explanation/rationale de faithfulness, provenance de correctness, lifecycle audit de output-level auditability y autoridad/actualidad documental de corrección sustantiva o jurídica. No puede describir todavía la arquitectura del presente estudio, HE4, el testbed ni resultados propios. Debe cerrar preparando 2.5 sobre reproducibilidad y evaluación.

### Gobernanza editorial vigente

```text
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
SPCCR_VERSION = 1.0
SPCCR_STATUS = AUTHOR_APPROVED / ACTIVE
KBS_EMPIRICAL_WRITING_GUIDE = KBS_EWG_34_V01
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
PUBLICATION_ROUTE_TARGET_A = SUBSCRIPTION
PAID_OPEN_ACCESS = NOT_SELECTED
APC_PAYMENT_PLANNED = NO
```

### Estado científico preservado

```text
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED / GROUP3_CONDITION_RESOLVED
GROUP3_HYPOTHESIS_DISPOSITION = HE2_SUPPORTED / HE5_INCONCLUSIVE
C10_C11_RECONCILIATION = COMPLETED_BY_GROUP3_AND_G4_F01 / SEE_CLAIM_EVIDENCE_MATRIX
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Fronteras obligatorias:

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`;
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`;
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`;
- `JOURNAL_FIT ≠ NOVELTY_PROOF`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`;
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`;
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.

### Estado experimental preservado

Corte editorial sincronizado con `SRC-03` después del cierre de Grupo 3 y la integración de G4-F01:

```text
EXPERIMENTAL_PLAN_BRANCH = docs/plan-maestro-temporal-2026-08-31
EXPERIMENTAL_PLAN_HEAD = 2237ddc46bc1c7bfac203753bdcf2c7d4592f83e
EXPERIMENTAL_MAIN_CHECKPOINT = 9f549ebdf940f9d806d5088697394d0c927f9fdc
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = IN_PROGRESS
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F03 = NOT_AUTHORIZED
```

Este corte no obliga a reabrir Related Work B01–B03: esas subsecciones no consumen resultados propios del estudio. Sí gobierna la futura redacción de `Experimental design`, `Results` y `Discussion`. Los resultados de Grupo 3 y la matriz controlada de G4-F01 pueden utilizarse únicamente dentro de su alcance aprobado y cuando el gate editorial correspondiente esté abierto. G4-F02 y G4-F03 no pueden consumirse como evidencia cerrada mientras el Plan Maestro no registre el estado requerido.

### Gate vigente

```text
CURRENT_GATE = RELATED_WORK_B04_DRAFTING
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_RELATED_WORK_B04_SECTION_2.4_ONLY
NEXT_PROMPT = article/prompts/2_RELATED_WORK_B04_EVIDENCE_GROUNDING_EXPLAINABILITY_AUDITABILITY.md
MASTER_INTEGRATION = ARTICLE_MASTER_V003 / ACTIVE_BASELINE
```

---

## English

Related Work B01 / Section 2.1, B02 / Section 2.2, and B03 / Section 2.3 are `APPROVED / FROZEN / INTEGRATED`. B03 passed independent scientific, primary-source, citation-comment, editorial, bilingual, OOXML, zero-tracked-change, and 21-page render review. The author's approval is effective.

The active cumulative master is `article/manuscript/ARTICLE_MASTER_V003.md/.docx`; its DOCX SHA-256 is `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7` and it retains nineteen English citation-audit comments.

The article-side experimental snapshot remains reconciled with the canonical Master Plan after Group 3 closure and G4-F01 integration: Group 2 is `CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS`; Group 3 is `CLOSED / APPROVED`; `HE2 = SUPPORTED`; `HE5 = INCONCLUSIVE`; Group 4 is `IN_PROGRESS`; G4-F01 is `CLOSED / APPROVED / INTEGRATED_TO_MAIN`; G4-F02 is `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`; and G4-F03 is `NOT_AUTHORIZED`.

The current gate is `RELATED_WORK_B04_DRAFTING`. Only Section 2.4, `Evidence grounding, explainability, and auditability`, is authorized. B04 must preserve approved Sections 2.1–2.3 and all nineteen comments unchanged, start from the canonical V003 DOCX, distinguish grounding/explanation/provenance/auditability/legal correctness carefully, and stop before Section 2.5. Present-study architecture, experimental testbed/results, final gap, and novelty remain unauthorized.