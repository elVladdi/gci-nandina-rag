# Prompt cerrado 0B-05C — Normalización final posterior al cierre experimental / Closed prompt 0B-05C — Final normalization after experimental closure

## Español

### Rol

Actúa exclusivamente como **IA de Redacción** del artículo científico principal del proyecto Tesis San Marcos.

Tu tarea es realizar una **normalización correctiva acotada** del entregable `0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales` después del cierre experimental correctivo.

No eres la IA Experimental ni la IA Gestora. No decides nuevos experimentos, no recalculas métricas, no modificas el Plan Maestro y no avanzas a ningún bloque posterior.

### Rama y repositorio

Repositorio: `elVladdi/gci-nandina-rag`  
Rama: `article/main-manuscript`

Trabaja únicamente sobre el estado vigente de esa rama al momento de ejecutar este prompt.

### Onboarding obligatorio

Antes de escribir, lee íntegramente y en este orden:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/DECISIONS.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/STYLE_GUIDE.md`;
9. `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`;
10. `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`;
11. `article/reviews/0B05C_INTERNAL_REVIEW.md`;
12. `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`;
13. `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`;
14. `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md`;
15. `article/reviews/0B05C_D1A_GOVERNANCE_NORMALIZATION_EDITORIAL_REVIEW.md`;
16. `article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`;
17. `SRC-03`, solo lectura: rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

La revisión final `0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md` gobierna la transición actual. Los reviews anteriores conservan validez histórica para documentar cómo evolucionó el gate.

### Estado de entrada obligatorio

Debes partir de:

```text
0B-05C_OPERATIONAL_STATUS = REVISION_REQUIRED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

### Estado experimental final que debes reproducir exactamente

No reinterpretar, resumir favorablemente ni sustituir estas etiquetas:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25

D1A_TRAINING_EXPOSURE = NO_EFFECTIVE_EXPOSURE_IDENTIFIED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NONE_IDENTIFIED
D1A_MODEL_POLICY = FREEZE_ORIGINAL_D1A_WEIGHTS
D1A_EXECUTION_SPECIFICATION = CLOSED_PROSPECTIVELY

EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED

0B05C_EXPERIMENTAL_CORRECTIVE_GATE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
```

Si SRC-03 contiene estados históricos previos que luego fueron corregidos o superseded dentro del propio historial experimental, utiliza exclusivamente la interpretación final vigente registrada por el cierre correctivo y por la revisión editorial final. No recuperes como vigente una interpretación histórica rechazada.

### Correcciones obligatorias C1–C6

Debes incorporar exactamente estas correcciones ya auditadas:

1. **C1 — overlap plano:** registrar que `87044110` aparece en `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, caso `DA-EVAL-V02-00060`, `candidate_rank = 100`.
2. **C2 — inputs efectivos:** EV-03 ejecutó sobre `data/processed/corpus_rag_v1_index.jsonl`; EV-04 sobre `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.
3. **C3 — intersecciones negativas:** la ausencia de `87044110`/`87045110` en labels EVAL o candidatos históricos no debe denominarse `NO_DRIFT_IDENTIFIED`; descríbela únicamente como ausencia/intersección negativa en esos componentes.
4. **C4 — instrumentos nacionales:** limita cualquier conclusión al conjunto de instrumentos nacionales efectivamente auditados. No declares universalmente que no existen otras normas pertinentes.
5. **C5 — DESPA-PG.01:** conserva la precisión temporal de RS 079-2026/SUNAT; no fusiones la vigencia general con la disposición específica diferida.
6. **C6 — separación conceptual:** conserva siempre:

```text
SOURCE_VERSION_DRIFT
≠ SCOPE_OVERLAP
≠ RETRIEVAL_OUTPUT_OVERLAP
≠ EXPERIMENTAL_METRIC_IMPACT
```

### Cronología obligatoria

El artefacto normalizado debe distinguir claramente:

```text
auditoría documental inicial
→ drift y scope overlap confirmados
→ impacto métrico inicialmente NOT_DETERMINED
→ trigger experimental
→ auditoría y especificación pre-ejecución
→ sensibilidad correctiva Attempt06
→ interpretación final corregida
→ impacto METHOD_DEPENDENT
→ DOWNSTREAM_REEXECUTION = NOT_REQUIRED
```

`NOT_DETERMINED` puede conservarse solo cuando se identifique explícitamente como estado histórico previo a la ejecución correctiva. No puede aparecer como estado actual de 0B-05C.

### Regla sobre métricas y cifras

No recalcules ninguna cifra.

Puedes transcribir cifras/deltas de Attempt06 únicamente si están explícitamente documentadas en SRC-03 o en artefactos experimentales ya integrados y si son necesarias para explicar el resultado. No derives valores nuevos ni realices inferencia estadística.

Está prohibido afirmar:

- significancia estadística no calculada;
- causalidad;
- relevancia práctica no evaluada;
- generalización fuera del diseño ejecutado;
- legal correctness;
- que la actualización normativa “mejoró el sistema” en términos generales;
- que 0B-05C tuvo “cero impacto” o “ningún impacto material”.

### Fronteras normativas obligatorias

Mantén:

```text
OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION
DOCUMENT_TRACEABILITY ≠ LEGAL_SUFFICIENCY
NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS
DOCUMENT_RETRIEVAL ≠ EXPERT_INTERPRETATION ≠ LEGAL_CORRECTNESS
HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_10_DIGIT
```

No sustituir retrospectivamente el snapshot Decisión 885 originalmente utilizado por el experimento. La sensibilidad correctiva debe describirse como análisis posterior, no como reescritura del experimento original.

### Alcance negativo

No hagas ninguna de estas acciones:

- no realices búsqueda web nueva;
- no abras ni ejecutes 0B-06;
- no abras 0C ni 0D;
- no redactes ninguna sección del manuscrito;
- no declares novelty o gap definitivo;
- no modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md` ni ningún review;
- no modifiques el Plan Maestro;
- no modifiques `main`;
- no ejecutes experimentos;
- no recalcules resultados;
- no integres resultados de EXP11B, EXP12, Grupo 2B o Grupo 3 en esta normalización;
- no uses resultados inexistentes de Grupo 3;
- no declares 0B-05C `APPROVED` ni `FROZEN`;
- no solicites aprobación del autor.

### Artefacto de respuesta obligatorio en GitHub

Debes crear **un único archivo de respuesta** en:

`article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_NORMALIZED.md`

No modifiques ningún otro archivo.

Como la respuesta quedará versionada dentro del entorno del artículo, debe contener:

1. versión completa en español;
2. versión completa en inglés con equivalencia semántica claim por claim;
3. una sección final de trazabilidad con:
   - archivos gobernantes leídos;
   - snapshot de SRC-03 consumido;
   - lista de correcciones C1–C6 incorporadas;
   - lista de estados experimentales finales reproducidos;
4. una tabla `CAMBIO | MOTIVO | FUENTE GOBERNANTE` y su equivalente inglés;
5. el siguiente cierre operativo exacto:

```text
0B-05C_DRAFTING_NORMALIZATION = COMPLETED_PENDING_EDITORIAL_REVIEW
0B-05C_OPERATIONAL_STATUS = REVISION_REQUIRED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE = NOT_PERFORMED
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

### Commit

Versiona únicamente ese archivo de respuesta en `article/main-manuscript` con un mensaje semántico equivalente a:

`article: normalize 0B-05C after experimental closure`

En tu respuesta al usuario, informa únicamente:

- commit SHA;
- ruta del archivo creado;
- estado `COMPLETED_PENDING_EDITORIAL_REVIEW`.

No pegues de nuevo el contenido completo en el chat.

Detente después de ese commit.

---

## English

### Role

Act exclusively as the **Writing AI** for the main scientific article of the Tesis San Marcos project.

Your task is to perform a **bounded corrective normalization** of the `0B-05C — Authority, currency, and traceability of normative/official sources` deliverable after the corrective experimental closure.

You are neither the Experimental AI nor the Managing AI. You do not decide new experiments, recalculate metrics, modify the Master Plan, or advance to later blocks.

### Repository and branch

Repository: `elVladdi/gci-nandina-rag`  
Branch: `article/main-manuscript`

Work only from the current state of that branch when executing this prompt.

### Mandatory onboarding

Before writing, read in full and in this order:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/DECISIONS.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/STYLE_GUIDE.md`;
9. `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`;
10. `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`;
11. `article/reviews/0B05C_INTERNAL_REVIEW.md`;
12. `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`;
13. `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`;
14. `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md`;
15. `article/reviews/0B05C_D1A_GOVERNANCE_NORMALIZATION_EDITORIAL_REVIEW.md`;
16. `article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`;
17. `SRC-03`, read-only: branch `docs/plan-maestro-temporal-2026-08-31`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

The final `0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md` governs the current transition. Earlier reviews remain historically valid evidence of how the gate evolved.

### Mandatory input state

Start from:

```text
0B-05C_OPERATIONAL_STATUS = REVISION_REQUIRED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

### Final experimental state to reproduce exactly

Do not reinterpret, favorably summarize, or replace these labels:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25

D1A_TRAINING_EXPOSURE = NO_EFFECTIVE_EXPOSURE_IDENTIFIED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NONE_IDENTIFIED
D1A_MODEL_POLICY = FREEZE_ORIGINAL_D1A_WEIGHTS
D1A_EXECUTION_SPECIFICATION = CLOSED_PROSPECTIVELY

EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED

0B05C_EXPERIMENTAL_CORRECTIVE_GATE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
```

If SRC-03 contains earlier historical states that were later corrected or superseded within the experimental history itself, use only the current final interpretation recorded by the corrective closure and the final editorial reconciliation. Do not restore a rejected historical interpretation as current.

### Mandatory C1–C6 corrections

Incorporate exactly these already-audited corrections:

1. **C1 — flat overlap:** record that `87044110` appears in `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, case `DA-EVAL-V02-00060`, `candidate_rank = 100`.
2. **C2 — effective inputs:** EV-03 ran on `data/processed/corpus_rag_v1_index.jsonl`; EV-04 on `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.
3. **C3 — negative intersections:** absence of `87044110`/`87045110` from EVAL labels or historical candidates must not be called `NO_DRIFT_IDENTIFIED`; describe it only as absence/negative intersection in those components.
4. **C4 — national instruments:** bound any conclusion to the set of national instruments actually audited. Do not universally claim that no other relevant rules exist.
5. **C5 — DESPA-PG.01:** preserve the temporal precision of RS 079-2026/SUNAT; do not merge general effectiveness with the specifically deferred provision.
6. **C6 — conceptual separation:** always preserve:

```text
SOURCE_VERSION_DRIFT
≠ SCOPE_OVERLAP
≠ RETRIEVAL_OUTPUT_OVERLAP
≠ EXPERIMENTAL_METRIC_IMPACT
```

### Mandatory chronology

The normalized artifact must clearly distinguish:

```text
initial documentary audit
→ confirmed drift and scope overlap
→ metric impact initially NOT_DETERMINED
→ experimental trigger
→ pre-execution audit and specification
→ corrective Attempt06 sensitivity
→ corrected final interpretation
→ METHOD_DEPENDENT impact
→ DOWNSTREAM_REEXECUTION = NOT_REQUIRED
```

`NOT_DETERMINED` may remain only when explicitly identified as a historical pre-execution state. It must not appear as the current 0B-05C state.

### Metrics and figures rule

Do not recalculate any figure.

You may transcribe Attempt06 figures/deltas only when explicitly documented in SRC-03 or already-integrated experimental artifacts and when necessary to explain the result. Do not derive new values or perform statistical inference.

Do not claim uncomputed statistical significance, causality, unevaluated practical relevance, generalization beyond the executed design, legal correctness, that the normative update generally “improved the system,” or that 0B-05C had “zero impact” or “no material impact.”

### Mandatory normative boundaries

Preserve:

```text
OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION
DOCUMENT_TRACEABILITY ≠ LEGAL_SUFFICIENCY
NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS
DOCUMENT_RETRIEVAL ≠ EXPERT_INTERPRETATION ≠ LEGAL_CORRECTNESS
HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_10_DIGIT
```

Do not retrospectively replace the Decision-885 snapshot originally used by the experiment. Describe the corrective sensitivity as a subsequent analysis, not as a rewrite of the original experiment.

### Negative scope

Do not perform new web research; do not open or execute 0B-06, 0C, or 0D; do not draft any manuscript section; do not declare final novelty or gap; do not modify `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, or any review; do not modify the Master Plan or `main`; do not run experiments or recalculate results; do not integrate EXP11B, EXP12, Group 2B, or Group 3 results into this normalization; do not use nonexistent Group 3 results; do not declare 0B-05C `APPROVED` or `FROZEN`; and do not request author approval.

### Mandatory GitHub response artifact

Create **exactly one response file** at:

`article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_NORMALIZED.md`

Do not modify any other file.

Because the response is versioned inside the article environment, it must contain a complete Spanish version and a complete English version with claim-by-claim semantic equivalence; a final traceability section listing governing files read, the SRC-03 snapshot consumed, C1–C6 corrections incorporated, and final experimental states reproduced; a `CHANGE | RATIONALE | GOVERNING SOURCE` table and Spanish equivalent; and exactly this operational closure:

```text
0B-05C_DRAFTING_NORMALIZATION = COMPLETED_PENDING_EDITORIAL_REVIEW
0B-05C_OPERATIONAL_STATUS = REVISION_REQUIRED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE = NOT_PERFORMED
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

### Commit

Version only that response file on `article/main-manuscript` with a semantic commit message equivalent to:

`article: normalize 0B-05C after experimental closure`

In your user-facing response, report only the commit SHA, created file path, and `COMPLETED_PENDING_EDITORIAL_REVIEW` state. Do not paste the full artifact back into chat.

Stop after that commit.