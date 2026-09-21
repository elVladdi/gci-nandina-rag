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
ARTICLE_WRITING_PLAN = V2.4
STRUCTURE_APPROVAL_DECISION = D-015
EXPERIMENTAL_RECONCILIATION_DECISION = D-019
LATEST_EDITORIAL_DECISION = D-020
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK_B01 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B02 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B03 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B04 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B04_V02 = APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V004
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V004.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V004.docx
CANONICAL_MASTER_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
CANONICAL_MASTER_DOCX_GIT_BLOB = 64519f62da55bd92acbc7c62c30f97a23b529efc
CANONICAL_CITATION_COMMENTS = 25
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_GATE = RELATED_WORK_B05
AUTHORIZED_SCOPE = SECTION_2.5_ONLY
RELATED_WORK_B05 = AUTHORIZED / ACTIVE
RELATED_WORK_B06 = NOT_AUTHORIZED
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
- `2.4 Evidence grounding, explainability, and auditability` — `APPROVED / FROZEN / INTEGRATED` mediante D-020; total acumulado 25 comentarios.

Controles heredados:

- `DIRECT_GENERATIVE_LLM_CLASSIFICATION ≠ FINE_TUNED_TRANSFORMER_CLASSIFIER`;
- `RAG_CLASSIFICATION ≠ RAG_EVIDENCE_SUPPORT ≠ DOCUMENT_QA_RAG`;
- `SEARCH_CONTROL / RERANKING / NEXT_HOP_DECISION ≠ EXPLANATION_ONLY_GENERATION`;
- `RATIONALE / REASONING_TRACE ≠ FAITHFULNESS GUARANTEE`;
- `VISIBLE_CITATION / PROVENANCE ≠ FORMAL_AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `PROVENANCE / LINEAGE ≠ SUBSTANTIVE_CORRECTNESS`;
- `LIFECYCLE_AUDIT ≠ REVIEW_OF_AN_INDIVIDUAL_OUTPUT`;
- `OFFICIAL_SOURCE / DOCUMENT_AUTHORITY ≠ CORRECT_LEGAL_INTERPRETATION`.

### Cierre B04 V02

```text
BLOCK = RELATED_WORK_B04
BLOCK_REVISION = V02
SECTION = 2.4 Evidence grounding, explainability, and auditability
DELIVERY_COMMIT = 119d6f9b46320d4970c7c46e421d66649269885f
AUTHOR_APPROVAL = RECEIVED
INTERNAL_REVIEW = PASS
SOURCE_SUPPORT = PASS / 6_OF_6
C1_LEWIS_CORRECTION = PASS
C2_RAJI_CORRECTION = PASS
C3_GRAINGER_CORRECTION = PASS
PRIOR_CITATION_COMMENTS_PRESERVED = 19/19
B04_CITATION_COMMENT_COVERAGE = 6/6
TOTAL_CITATION_COMMENT_COUNT = 25
DOCX_OOXML_INTEGRITY = PASS
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS / 23_OF_23_PAGES
DOCX_BINARY_IDENTITY = PASS
APPROVED_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
APPROVED_DOCX_GIT_BLOB = 64519f62da55bd92acbc7c62c30f97a23b529efc
NET_B04_V02_FILE_SCOPE = PASS / EXACTLY_4_AUTHORIZED_FILES
SINGLE_COMMIT_DISCIPLINE = FAIL / NONBLOCKING_PROCESS_DEVIATION
HISTORY_REWRITE = NOT_PERFORMED
```

La desviación de historial queda documentada en D-020. Los commits accidentales no alteran el árbol final ni el contenido científico. No se realizó force-push ni reescritura destructiva. El candidato B04 V02 aprobado fue promovido byte-for-byte a `ARTICLE_MASTER_V004`.

### Bloque activo — Related Work B05

```text
BLOCK = RELATED_WORK_B05
SECTION = 2.5 Reproducibility and evaluation in knowledge-based decision support
PROMPT = article/prompts/2_RELATED_WORK_B05_REPRODUCIBILITY_EVALUATION.md
DRAFTING = AUTHORIZED
BASELINE_MASTER = ARTICLE_MASTER_V004
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V004.md
BASELINE_DOCX = article/manuscript/ARTICLE_MASTER_V004.docx
BASELINE_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
PRIOR_SECTIONS_2_1_TO_2_4 = APPROVED / FROZEN / PRESERVE_EXACTLY
PRIOR_CITATION_COMMENTS = 25 / PRESERVE_EXACTLY
SECTION_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

B05 sintetizará literatura sobre documentación de datos, identidad/versionado, provenance/lineage, reproducibilidad y evaluación alineada con función/salida. No describirá todavía la arquitectura, testbed, resultados, FINAL_GAP ni novelty del presente estudio.

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

Grupo 4 deja elegibles para futura Discussion únicamente los contrastes autorizados por G4-F03. No autoriza superioridad numérica entre estudios, SOTA, novelty absoluta, unicidad, generalización empírica, causalidad no identificada ni corrección jurídica. El cierre experimental no abre por sí mismo Results ni Discussion. Grupo 5 permanece no iniciado.

### Gate vigente

```text
CURRENT_GATE = RELATED_WORK_B05
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_RELATED_WORK_B05_ONLY
NEXT_PROMPT = article/prompts/2_RELATED_WORK_B05_REPRODUCIBILITY_EVALUATION.md
MASTER_INTEGRATION = ARTICLE_MASTER_V004 / ACTIVE_BASELINE
B06 = NOT_AUTHORIZED
```

---

## English

Related Work Sections 2.1–2.4 are `APPROVED / FROZEN / INTEGRATED`. The canonical cumulative master is now `ARTICLE_MASTER_V004.md/.docx`, SHA-256 `e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162`, with twenty-five citation-audit comments.

B04 V02 passed independent source audit and author approval. Its approved DOCX is byte-identical to Git blob `64519f62da55bd92acbc7c62c30f97a23b529efc`. The accidental connector/probe commits are retained transparently as nonblocking process deviations; the final tree is normalized and no history rewrite was performed.

The active editorial gate is `RELATED_WORK_B05`, Section 2.5 only. It must use V004 as the exact cumulative baseline and preserve Sections 2.1–2.4 plus all twenty-five inherited comments. Section 2.6 and all later manuscript sections remain unauthorized.

The experimental snapshot remains the D-019 reconciliation after complete Group 4 closure: Group 3 is closed, `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE`, Group 4 is closed/approved, and G4-F01–F03 are integrated. Group 5 remains not started. Those experimental facts do not authorize Results/Discussion at the present gate.