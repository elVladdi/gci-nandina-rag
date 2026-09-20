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
ARTICLE_WRITING_PLAN = V2.3
STRUCTURE_APPROVAL_DECISION = D-015
EXPERIMENTAL_RECONCILIATION_DECISION = D-019
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK_B01 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B02 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B03 = APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V003
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V003.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V003.docx
CANONICAL_MASTER_DOCX_SHA256 = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
CANONICAL_CITATION_COMMENTS = 19
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_GATE = RELATED_WORK_B04_V02_CORRECTION
RELATED_WORK_B04_V01 = REVIEWED / MINOR_CORRECTIONS_REQUIRED / NOT_APPROVED
RELATED_WORK_B04_V02 = AUTHORIZED / ACTIVE
AUTHORIZED_SCOPE = SECTION_2.4_CORRECTION_ONLY
RELATED_WORK_B05 = NOT_AUTHORIZED
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

### Related Work aprobado

- `2.1 Automated tariff classification and candidate retrieval` — `APPROVED / FROZEN / INTEGRATED` mediante D-016; 8 comentarios de auditoría.
- `2.2 Knowledge-enhanced retrieval and regulatory reasoning` — `APPROVED / FROZEN / INTEGRATED` mediante D-017; total acumulado 14 comentarios.
- `2.3 LLMs for classification, reasoning, and explanation` — `APPROVED / FROZEN / INTEGRATED` mediante D-018; total acumulado 19 comentarios.

Controles heredados:

- `DIRECT_GENERATIVE_LLM_CLASSIFICATION ≠ FINE_TUNED_TRANSFORMER_CLASSIFIER`;
- `RAG_CLASSIFICATION ≠ RAG_EVIDENCE_SUPPORT ≠ DOCUMENT_QA_RAG`;
- `SEARCH_CONTROL / RERANKING / NEXT_HOP_DECISION ≠ EXPLANATION_ONLY_GENERATION`;
- `RATIONALE / REASONING_TRACE ≠ FAITHFULNESS GUARANTEE`;
- `VISIBLE_CITATION / PROVENANCE ≠ FORMAL_AUDITABILITY ≠ LEGAL_CORRECTNESS`.

### Bloque activo — Related Work B04 V02

B04 V01 fue auditado internamente. No presentó error científico material, pero requiere tres correcciones menores y reconciliación de identidad binaria del DOCX. Por ello no fue aprobado ni integrado.

```text
BLOCK = RELATED_WORK_B04
SECTION = 2.4 Evidence grounding, explainability, and auditability
BLOCK_REVISION = V02
CORRECTIVE_PROMPT = article/prompts/2_RELATED_WORK_B04_V02_CORRECTIONS.md
CORRECTIVE_PROMPT_COMMIT = 6c1e785dc71613e3b6d3425852d7314b21d4c165
DRAFTING = AUTHORIZED
BASELINE_MASTER = ARTICLE_MASTER_V003
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V003.md
BASELINE_DOCX = article/manuscript/ARTICLE_MASTER_V003.docx
BASELINE_DOCX_SHA256 = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
PRIOR_SECTIONS_2_1_TO_2_3 = APPROVED / FROZEN / PRESERVE_EXACTLY
PRIOR_CITATION_COMMENTS = 19 / PRESERVE_EXACTLY
EXPECTED_TOTAL_COMMENTS_AFTER_B04 = 25
SECTIONS_2_5_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

Las correcciones obligatorias V02 son: estrechar la atribución a Lewis et al. (2020) para no presentar provenance support; no atribuir `output-level auditability` a Raji et al. (2020) como constructo establecido; y sustituir el carácter `necessary` por `relevant` en la interpretación de Grainger (2024). El DOCX entregado y el comprometido deben ser binariamente idénticos.

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
C10_C11_RECONCILIATION = COMPLETED_BY_GROUP3_AND_GROUP4 / SEE_CLAIM_EVIDENCE_MATRIX
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
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`;
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.

### Estado experimental vigente

Corte editorial reconciliado por D-019 con el Plan Maestro canónico después del cierre completo de Grupo 4:

```text
EXPERIMENTAL_PLAN_BRANCH = docs/plan-maestro-temporal-2026-08-31
EXPERIMENTAL_PLAN_HEAD = 3ba3557eb10e741b8f49c420850940dee1df08ef
EXPERIMENTAL_PLAN_BLOB = 5ab0af7af5a2c92a1107e820bee1a6bb65026432
EXPERIMENTAL_MAIN_CHECKPOINT = 38e22c19a0eb0d344e7675761a88d7968091eead
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03_EXTERNAL_REAUDIT = PASS
G4_F03_COMPARISON_REGISTRY_COUNT = 11
G4_F03_AUTHORIZED_DISCUSSION_POINT_COUNT = 8
G4_F03_FORBIDDEN_DISCUSSION_POINT_COUNT = 14
GROUP5 = NOT_STARTED
G5_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Grupo 4 cerró el contraste controlado con la literatura y deja elegibles para una futura Discussion únicamente los contrastes expresamente autorizados por G4-F03. No autoriza superioridad numérica entre estudios, SOTA, novelty absoluta, unicidad, generalización empírica, causalidad no identificada ni corrección jurídica. El cierre experimental no abre por sí mismo `Results` ni `Discussion`.

El cierre de Grupo 4 no obliga a reabrir Related Work 2.1–2.3 y tampoco cancela la corrección editorial B04 V02. Grupo 5 permanece no iniciado.

### Gate vigente

```text
CURRENT_GATE = RELATED_WORK_B04_V02_CORRECTION
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_RELATED_WORK_B04_V02_CORRECTIONS_ONLY
NEXT_PROMPT = article/prompts/2_RELATED_WORK_B04_V02_CORRECTIONS.md
MASTER_INTEGRATION = ARTICLE_MASTER_V003 / ACTIVE_BASELINE
B05 = NOT_AUTHORIZED
```

---

## English

Related Work Sections 2.1–2.3 remain `APPROVED / FROZEN / INTEGRATED`; the active cumulative master remains `ARTICLE_MASTER_V003.md/.docx`, SHA-256 `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`, with nineteen inherited citation-audit comments.

The active editorial gate is now `RELATED_WORK_B04_V02_CORRECTION`. B04 V01 was internally reviewed and requires three minor source-scope corrections plus DOCX binary-identity reconciliation. B04 is not yet approved or integrated, and Section 2.5 remains unauthorized.

The article-side experimental snapshot is reconciled with the canonical Master Plan at `3ba3557eb10e741b8f49c420850940dee1df08ef`, blob `5ab0af7af5a2c92a1107e820bee1a6bb65026432`, experimental `main` checkpoint `38e22c19a0eb0d344e7675761a88d7968091eead`. Group 2 is closed with nonblocking limitations; Group 3 is `CLOSED / APPROVED`; `HE2 = SUPPORTED`; `HE5 = INCONCLUSIVE`; Group 4 is `CLOSED / APPROVED`; G4-F01, G4-F02, and G4-F03 are all `CLOSED / APPROVED / INTEGRATED_TO_MAIN`; G4-F03 passed external re-audit. Its literature-contrast registry contains 11 comparison records, 8 authorized discussion points, and 14 forbidden discussion points.

These Group 4 materials become eligible evidence for future Results/Discussion only when the corresponding article gates open. They do not establish cross-study numerical superiority, SOTA, absolute novelty, empirical generalization, unsupported causality, or legal correctness. Group 5 remains `NOT_STARTED`, with G5-F01 `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`.
