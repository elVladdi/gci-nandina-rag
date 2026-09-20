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
ARTICLE_WRITING_PLAN = V2.1
STRUCTURE_APPROVAL_DECISION = D-015
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK_B01 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK_B01_REVIEW = PASS
RELATED_WORK_B01_AUTHOR_APPROVAL = RECEIVED / EFFECTIVE
CANONICAL_MASTER = ARTICLE_MASTER_V001
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V001.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V001.docx
CANONICAL_MASTER_DOCX_SHA256 = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_GATE = RELATED_WORK_B02_DRAFTING
RELATED_WORK_B02 = AUTHORIZED
AUTHORIZED_SCOPE = SECTION_2.2_ONLY
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

### Cierre de Related Work B01

La entrega `9a3acddeee01bd3c78f1b06306b8619a9ad5ccd6` fue auditada independientemente por la IA Gestora.

```text
B01_SECTION = 2.1 Automated tariff classification and candidate retrieval
B01_INTERNAL_REVIEW = PASS
B01_SCIENTIFIC_CONTENT = PASS
B01_SOURCE_SUPPORT = PASS
B01_KBS_EDITORIAL_FIT = PASS
B01_EN_ES_EQUIVALENCE = PASS
B01_CITATION_COMMENT_COVERAGE = 8/8 / PASS
B01_DOCX_INTEGRITY = PASS
B01_DOCX_RENDER = PASS / 16_OF_16_PAGES
B01_MATERIAL_CORRECTIONS = 0
B01_EXPERIMENTAL_REVIEW = NOT_REQUIRED
B01_AUTHOR_APPROVAL = RECEIVED / EFFECTIVE
B01_STATUS = APPROVED / FROZEN / INTEGRATED
```

La primera integración canónica bajo la estructura D-015 es `ARTICLE_MASTER_V001`. El DOCX canónico es binariamente equivalente al candidato B01 aprobado y conserva los ocho comentarios de auditoría de citas.

Dos controles no bloqueantes se mantienen para etapas posteriores: `has most often been framed` es una síntesis cualitativa, no una frecuencia estadística; y las métricas Top-k deberán nombrarse con precisión sin sustituir métricas sensibles al orden como MRR.

El cover interno conserva etiquetas heredadas del bootstrap estructural. Es un asunto de formato no científico y no bloquea la redacción; cualquier normalización futura deberá ser controlada y preservar contenido, comentarios y trazabilidad.

### Bloque activo — Related Work B02

```text
BLOCK = RELATED_WORK_B02
SECTION = 2.2 Knowledge-enhanced retrieval and regulatory reasoning
BLOCK_REVISION = V01
DRAFTING = AUTHORIZED
BASELINE_MASTER = ARTICLE_MASTER_V001
BASELINE_DOCX_SHA256 = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
SECTIONS_2_3_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_UNLESS_NEW_TRIGGER_APPEARS
```

B02 deberá preservar 2.1 sin cambios y sintetizar la literatura según la función del conocimiento externo: conocimiento que participa en clasificación/selección, retrieval de documentos o pasajes para contexto, uso de reglas/jerarquías/agentes para razonamiento y evidencia/documentación usada como soporte. No puede describir todavía la arquitectura del presente estudio ni declarar gap final o novelty universal.

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

La integración de B01 no modifica el Plan Maestro experimental. El último estado registrado para el proceso editorial permanece con Grupo 3 en curso y RQ4 condicionada a su cierre aplicable. Related Work B02 no requiere resultados experimentales propios.

### Gate vigente

```text
CURRENT_GATE = RELATED_WORK_B02_DRAFTING
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_RELATED_WORK_B02_SECTION_2.2_ONLY
NEXT_PROMPT = article/prompts/2_RELATED_WORK_B02_KNOWLEDGE_ENHANCED_RETRIEVAL_REGULATORY_REASONING.md
MASTER_INTEGRATION = ARTICLE_MASTER_V001 / ACTIVE_BASELINE
```

---

## English

Related Work B01 / Section 2.1 has passed independent scientific, source, editorial, bilingual, citation-comment, OOXML, and render review. The author had approved V01 subject to that audit; the PASS makes the approval effective. B01 is now `APPROVED / FROZEN / INTEGRATED`.

The canonical cumulative baseline is `article/manuscript/ARTICLE_MASTER_V001.md/.docx`; the canonical DOCX SHA-256 is `08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5` and retains all eight English citation-audit comments.

The current gate is `RELATED_WORK_B02_DRAFTING`. Only Section 2.2, `Knowledge-enhanced retrieval and regulatory reasoning`, is authorized. B02 must preserve approved 2.1 unchanged, start from the canonical V001 DOCX, and stop before Section 2.3. Present-study architecture, experimental testbed/results, final gap, and universal novelty remain unauthorized.