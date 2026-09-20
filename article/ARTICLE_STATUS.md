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
RELATED_WORK_B02_REVIEW = PASS
RELATED_WORK_B02_AUTHOR_APPROVAL = RECEIVED / EFFECTIVE
CANONICAL_MASTER = ARTICLE_MASTER_V002
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V002.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V002.docx
CANONICAL_MASTER_DOCX_SHA256 = ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e
CANONICAL_CITATION_COMMENTS = 14
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_GATE = RELATED_WORK_B03_DRAFTING
RELATED_WORK_B03 = AUTHORIZED
AUTHORIZED_SCOPE = SECTION_2.3_ONLY
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

### Cierre de Related Work B02

La entrega `5e58b5a45b1dcc50a4a324f38e5cc0c9746ef3dc` fue auditada independientemente por la IA Gestora, incluyendo verificación claim–cita–fuente contra los seis full texts primarios y comprobación de los comentarios Word.

```text
B02_SECTION = 2.2 Knowledge-enhanced retrieval and regulatory reasoning
B02_INTERNAL_REVIEW = PASS
B02_SCIENTIFIC_CONTENT = PASS
B02_SOURCE_SUPPORT = PASS
B02_COMMENT_SOURCE_ALIGNMENT = PASS
B02_KBS_EDITORIAL_FIT = PASS
B02_EN_ES_EQUIVALENCE = PASS
B02_NEW_CITATION_COMMENT_COVERAGE = 6/6 / PASS
B02_PRIOR_COMMENTS_PRESERVED = 8/8 / PASS
B02_TOTAL_COMMENTS = 14
B02_DOCX_INTEGRITY = PASS
B02_DOCX_RENDER = PASS / 19_OF_19_PAGES
B02_MATERIAL_CORRECTIONS = 0
B02_EXPERIMENTAL_REVIEW = NOT_REQUIRED
B02_AUTHOR_APPROVAL = RECEIVED / EFFECTIVE
B02_STATUS = APPROVED / FROZEN / INTEGRATED
```

La integración canónica posterior a B02 es `ARTICLE_MASTER_V002`. El DOCX canónico es binariamente equivalente al candidato B02 aprobado, conserva los catorce comentarios de auditoría y tiene SHA-256 `ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e`.

Controles no bloqueantes heredados de B02:

- Wang et al. (2026), `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification`, se conserva como **preprint** mientras no se verifique una versión editorial final;
- evidencia visible, citas, reasoning traces, path validity o rationale no equivalen automáticamente a auditabilidad formal ni corrección jurídica;
- la posición funcional del LLM en el pipeline debe distinguirse de su mera denominación como “LLM”.

### Bloque activo — Related Work B03

```text
BLOCK = RELATED_WORK_B03
SECTION = 2.3 LLMs for classification, reasoning, and explanation
BLOCK_REVISION = V01
DRAFTING = AUTHORIZED
BASELINE_MASTER = ARTICLE_MASTER_V002
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V002.md
BASELINE_DOCX = article/manuscript/ARTICLE_MASTER_V002.docx
BASELINE_DOCX_SHA256 = ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e
PRIOR_SECTIONS_2_1_2_2 = APPROVED / FROZEN / PRESERVE_EXACTLY
PRIOR_CITATION_COMMENTS = 14 / PRESERVE_EXACTLY
SECTIONS_2_4_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_UNLESS_NEW_TRIGGER_APPEARS
```

B03 debe distinguir por función operativa: clasificación generativa directa, transformer classifier fine-tuned, LLM que decide/controla búsqueda o reranking, lector/razonador condicionado por retrieval y generador de explicación/rationale. No puede describir todavía la arquitectura del presente estudio ni declarar gap final o novelty universal.

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
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
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
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### Estado experimental preservado

La integración de B02 no modifica el Plan Maestro experimental. Related Work B03 no consume resultados experimentales propios; cualquier trigger nuevo deberá declararse antes de usar información experimental no cerrada.

### Gate vigente

```text
CURRENT_GATE = RELATED_WORK_B03_DRAFTING
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_RELATED_WORK_B03_SECTION_2.3_ONLY
NEXT_PROMPT = article/prompts/2_RELATED_WORK_B03_LLM_CLASSIFICATION_REASONING_EXPLANATION.md
MASTER_INTEGRATION = ARTICLE_MASTER_V002 / ACTIVE_BASELINE
```

---

## English

Related Work B01 / Section 2.1 and Related Work B02 / Section 2.2 are `APPROVED / FROZEN / INTEGRATED`. B02 passed independent scientific, primary-source, citation-comment, editorial, bilingual, OOXML, and 19-page render review. The author had approved B02 subject to that audit; the PASS makes the approval effective.

The active cumulative master is `article/manuscript/ARTICLE_MASTER_V002.md/.docx`; its DOCX SHA-256 is `ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e` and it retains fourteen English citation-audit comments.

The current gate is `RELATED_WORK_B03_DRAFTING`. Only Section 2.3, `LLMs for classification, reasoning, and explanation`, is authorized. B03 must preserve approved Sections 2.1–2.2 and all fourteen comments unchanged, start from the canonical V002 DOCX, and stop before Section 2.4. Present-study architecture, experimental testbed/results, final gap, and universal novelty remain unauthorized.