# Prompt cerrado 0B-05C — Normalización final posterior al cierre experimental / Closed prompt 0B-05C — Final normalization after experimental closure

## Español

### Rol y alcance

Actúa exclusivamente como **IA de Redacción** del artículo científico principal del proyecto Tesis San Marcos.

Ejecuta una **normalización correctiva acotada** de `0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales` después del cierre experimental correctivo.

No eres la IA Experimental ni la IA Gestora. No decides nuevos experimentos, no recalculas métricas, no modificas el Plan Maestro y no avanzas a ningún bloque posterior.

Repositorio: `elVladdi/gci-nandina-rag`  
Rama: `article/main-manuscript`

### Onboarding obligatorio

Lee íntegramente, en este orden:

1. `article/START_HERE.md`
2. `article/README.md`
3. `article/ARTICLE_STATUS.md`
4. `article/ARTICLE_WRITING_PLAN.md`
5. `article/DECISIONS.md`
6. `article/SOURCE_REGISTRY.md`
7. `article/CLAIM_EVIDENCE_MATRIX.md`
8. `article/STYLE_GUIDE.md`
9. `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`
10. `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`
11. `article/reviews/0B05C_INTERNAL_REVIEW.md`
12. `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`
13. `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`
14. `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md`
15. `article/reviews/0B05C_D1A_GOVERNANCE_NORMALIZATION_EDITORIAL_REVIEW.md`
16. `article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`
17. SRC-03 en modo solo lectura: rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

La revisión final de reconciliación gobierna la transición actual. Los reviews anteriores son evidencia histórica del gate.

### Estado de entrada

```text
0B-05C_OPERATIONAL_STATUS = REVISION_REQUIRED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

### Estado experimental final obligatorio

Reproduce exactamente:

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

No restaures como vigente ninguna interpretación histórica posteriormente rechazada o corregida.

### Correcciones obligatorias C1–C6

1. Registrar el overlap plano de `87044110` en `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, caso `DA-EVAL-V02-00060`, `candidate_rank = 100`.
2. Precisar inputs efectivos: EV-03 → `data/processed/corpus_rag_v1_index.jsonl`; EV-04 → `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.
3. La ausencia de `87044110`/`87045110` en labels EVAL o candidatos históricos es una intersección negativa, no `NO_DRIFT_IDENTIFIED`.
4. Limitar conclusiones nacionales a los instrumentos efectivamente auditados.
5. Conservar la precisión temporal de RS 079-2026/SUNAT para DESPA-PG.01.
6. Mantener:

```text
SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT
```

### Cronología obligatoria

```text
auditoría documental inicial
→ drift y scope overlap confirmados
→ impacto métrico inicialmente NOT_DETERMINED
→ trigger experimental
→ auditoría/especificación pre-ejecución
→ sensibilidad correctiva Attempt06
→ interpretación final corregida
→ impacto METHOD_DEPENDENT
→ DOWNSTREAM_REEXECUTION = NOT_REQUIRED
```

`NOT_DETERMINED` solo puede aparecer como estado histórico previo, nunca como estado actual.

### Límites científicos

No recalcules cifras. Solo puedes transcribir cifras/deltas ya documentados si son necesarios. No declares significancia estadística no calculada, causalidad, relevancia práctica no evaluada, generalización, legal correctness, mejora global del sistema, ni que 0B-05C tuvo “cero impacto” o “ningún impacto material”.

Mantén:

```text
OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION
DOCUMENT_TRACEABILITY ≠ LEGAL_SUFFICIENCY
NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS
DOCUMENT_RETRIEVAL ≠ EXPERT_INTERPRETATION ≠ LEGAL_CORRECTNESS
HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_10_DIGIT
```

No sustituyas retrospectivamente el snapshot Decisión 885. La sensibilidad correctiva es un análisis posterior.

### Prohibiciones

No realices búsqueda web nueva; no abras 0B-06, 0C o 0D; no redactes el manuscrito; no declares novelty/gap definitivo; no modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md` ni reviews; no modifiques Plan Maestro ni `main`; no ejecutes experimentos; no recalcules resultados; no integres EXP11B, EXP12, Grupo 2B o Grupo 3; no uses resultados inexistentes de Grupo 3; no declares 0B-05C `APPROVED`/`FROZEN`; no solicites aprobación del autor.

### Respuesta obligatoria en GitHub — precisión de staging

Tu entrega es un **artefacto de trabajo pendiente de auditoría**, no un artefacto canónico/frozen de `article/literature/`.

Debes crear **exactamente un único archivo** en:

`article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`

Reglas:

- `article/responses/` es el área de staging de entregas de la IA de Redacción pendientes de revisión por la IA Gestora/Editor Científico Principal;
- no escribas esta entrega en `article/literature/`, `article/reviews/` ni `article/prompts/`;
- `V01` identifica esta primera ronda y debe preservarse como registro histórico;
- no sobrescribas una respuesta existente;
- si `..._RESPONSE_V01.md` ya existe, detente y reporta el conflicto; no generes `V02` sin instrucción expresa;
- si `article/responses/` no existe, créalo implícitamente al crear el archivo; no crees `.gitkeep` ni archivos auxiliares;
- no modifiques ningún otro archivo.

La respuesta debe contener:

1. versión completa en español;
2. versión completa en inglés semánticamente equivalente claim por claim;
3. trazabilidad: archivos gobernantes leídos, snapshot SRC-03, C1–C6 incorporadas y estados experimentales finales reproducidos;
4. tabla `CAMBIO | MOTIVO | FUENTE GOBERNANTE` y equivalente inglés;
5. cierre exacto:

```text
0B-05C_DRAFTING_NORMALIZATION = COMPLETED_PENDING_EDITORIAL_REVIEW
0B-05C_OPERATIONAL_STATUS = REVISION_REQUIRED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE = NOT_PERFORMED
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

### Commit y respuesta al usuario

Versiona únicamente ese archivo en `article/main-manuscript` con mensaje equivalente a:

`article: add 0B-05C drafting normalization response v01`

Después informa al usuario únicamente:

- commit SHA;
- ruta del archivo creado;
- `COMPLETED_PENDING_EDITORIAL_REVIEW`.

No pegues el contenido completo en el chat. Detente después del commit.

---

## English

### Role and scope

Act exclusively as the **Writing AI** for the main scientific article of the Tesis San Marcos project. Perform only the bounded corrective normalization of 0B-05C after the corrective experimental closure. You are neither the Experimental AI nor the Managing AI.

Repository: `elVladdi/gci-nandina-rag`  
Branch: `article/main-manuscript`

Read the same 17 governing sources listed in the Spanish section, including SRC-03 in read-only mode. The final reconciliation review governs the current transition; earlier reviews remain historical evidence.

Start from the exact operational state and reproduce exactly the final experimental labels stated in the Spanish section. Incorporate C1–C6 exactly, preserve the documented chronology, and keep `NOT_DETERMINED` only as a historical pre-execution state.

Do not recalculate figures or claim uncomputed significance, causality, unevaluated practical relevance, generalization, legal correctness, global system improvement, “zero impact,” or “no material impact.” Preserve all normative boundaries stated above and do not retrospectively replace the Decision-885 snapshot.

Do not perform new web research; do not open 0B-06, 0C, or 0D; do not draft the manuscript; do not modify governance files, reviews, the Master Plan, or `main`; do not run experiments or recalculate results; do not integrate EXP11B, EXP12, Group 2B, or Group 3; do not declare 0B-05C approved/frozen; and do not request author approval.

### Mandatory GitHub response artifact — staging rule

Your delivery is a **working artifact pending audit**, not a canonical/frozen `article/literature/` artifact.

Create **exactly one file** at:

`article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`

Rules:

- `article/responses/` is the staging area for Writing-AI deliveries pending Managing-AI/Lead-Editor review;
- do not write this delivery under `article/literature/`, `article/reviews/`, or `article/prompts/`;
- preserve `V01` as the historical record of this first round;
- never overwrite an existing response;
- if `..._RESPONSE_V01.md` already exists, stop and report the conflict; do not create `V02` without explicit instruction;
- if `article/responses/` does not exist, create it implicitly by creating this file; do not create `.gitkeep` or auxiliary files;
- modify no other repository file.

The response file must contain a full Spanish version and a semantically equivalent full English version, traceability, the change/rationale/governing-source table, and the exact operational closure defined above.

Commit only that response file with a semantic message equivalent to:

`article: add 0B-05C drafting normalization response v01`

Then report only the commit SHA, created path, and `COMPLETED_PENDING_EDITORIAL_REVIEW`. Do not paste the full content in chat. Stop after that commit.