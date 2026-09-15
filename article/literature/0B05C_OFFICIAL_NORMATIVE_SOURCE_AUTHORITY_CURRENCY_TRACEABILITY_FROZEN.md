# 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales / Authority, currency, and traceability of normative/official sources

## Español

### 1. Estado

- Bloque: `0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales`.
- Estado: **`APPROVED / FROZEN`**.
- Reconciliación experimental/editorial: completada.
- Normalización IA de Redacción: completada en `article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`.
- Auditoría científica/editorial final: **`PASS`**.
- Errores materiales: `0`.
- Correcciones menores pendientes: `0`.
- Revisión experimental adicional: `NOT_REQUIRED`.
- Aprobación expresa del autor: recibida el `2026-09-15`.
- Novelty: `NOT_DECLARED`.
- Gap definitivo: `NOT_DEFINED`.
- Manuscrito: `NOT_DRAFTED`.
- `0B-06`: `NOT_STARTED / OPENING_NOT_AUTHORIZED`.

Registros gobernantes:

- `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`;
- `article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md`;
- `article/reviews/0B05C_INTERNAL_REVIEW.md`;
- `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_GOVERNANCE_NORMALIZATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_FINAL_NORMALIZATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_AUTHOR_APPROVAL.md`;
- `article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`.

Este artefacto congela el estado editorial canónico del bloque. No modifica ni sustituye los artefactos experimentales originales.

### 2. Regla documental central

Se congela la separación:

`EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE`.

Una modificación normativa posterior no sustituye retrospectivamente el snapshot usado por el experimento. Del mismo modo, la existencia de una fuente experimental identificable no demuestra por sí sola que el corpus representara toda la normativa vigente en la fecha de ejecución.

### 3. Snapshot experimental preservado

Ref de desarrollo congelado por 0A-02:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

Fuentes normativas de ingesta confirmadas:

- `data/external/Arancel 2022.pdf`;
- `data/processed/corpus/arancel/arancel2022_run_metadata.json`;
- `data/external/CAN Desición 885 - Nanadina Gaceta 4359.pdf`;
- `data/processed/corpus/nandina/run_metadata.json`.

SHA-256 fuente registrados por el pipeline:

- Arancel 2022: `a01a029e1ca29b6debc61d219c17dfc086354e00669246cc24a91ad9f454c7d0`;
- Decisión 885 / Gaceta 4359: `8c4a30fb0328f151089ac4c7857ac447d3dd353de97122a11bde4550d594f0c6`.

Estos valores identifican archivos fuente procesados y no son blob SHA de GitHub.

### 4. Estado oficial auditado y drift confirmado

La auditoría primaria controlada cubrió, dentro del alcance necesario:

- OMA/WCO: HS 2022, GIR y fuentes oficiales relacionadas necesarias para autoridad/vigencia;
- Comunidad Andina: Decisión 885, Decisión 906 y Resolución 2592;
- Perú: DS 404-2021-EF, modificaciones nacionales materialmente auditadas y fuentes SUNAT/gob.pe usadas para orientación o contexto procedimental.

Las conclusiones nacionales quedan limitadas al conjunto de instrumentos efectivamente auditados; no se congela una afirmación universal sobre inexistencia de otras normas pertinentes.

La Decisión 906 modifica la Decisión 885, entró en vigencia el `2023-01-01` e incluye cambios de descripción en subpartidas NANDINA del Capítulo 87, entre ellas `8704.41.10` y `8704.51.10`. Por tanto:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
```

La ausencia de `87044110` y `87045110` entre labels EVAL o candidatos del ranking histórico se congela únicamente como **intersección negativa en esos componentes**. No elimina el drift documental ni autoriza `NO_DRIFT_IDENTIFIED` para el problema global.

### 5. Solapamiento de output confirmado

Se congela el hallazgo:

- archivo: `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`;
- caso: `DA-EVAL-V02-00060`;
- código: `87044110`;
- `candidate_rank = 100`;
- descripción derivada del snapshot Decisión 885.

No se identificó `87045110` en ese mismo output plano Top-100.

Estado:

```text
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25
```

La aparición a rank 100 demuestra solapamiento de output, no cambio automático de Top-k, Recall, MRR, cobertura, integración, HE4 u otra métrica.

### 6. Cadena efectiva de artefactos

Se congela la corrección de inputs efectivos:

- EV-03 ejecutó sobre `data/processed/corpus_rag_v1_index.jsonl`;
- EV-04 ejecutó sobre `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.

Para D1a se preserva el cierre prospectivo:

```text
D1A_TRAINING_EXPOSURE = NO_EFFECTIVE_EXPOSURE_IDENTIFIED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NONE_IDENTIFIED
D1A_MODEL_POLICY = FREEZE_ORIGINAL_D1A_WEIGHTS
D1A_EXECUTION_SPECIFICATION = CLOSED_PROSPECTIVELY
```

### 7. Cierre experimental correctivo congelado

La secuencia histórica se interpreta así:

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

Los estados `NOT_DETERMINED` permanecen como historia de gobernanza, no como estado actual.

Estado final congelado:

```text
EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
0B05C_EXPERIMENTAL_CORRECTIVE_GATE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
```

Este cierre **no** puede resumirse como “cero impacto” ni “sin impacto numérico material”. EV03 presenta cambio agregado cero bajo la sensibilidad; EV04 presenta una disminución no nula muy pequeña restringida a MRR; D1a presenta un cambio positivo no nulo en ranking exacto con efecto HS4 menor y mixto. El efecto conjunto es dependiente del método.

No se infiere significancia estadística, causalidad, relevancia práctica no evaluada ni generalización.

### 8. Correcciones C1–C6 congeladas

- **C1:** incorporado `DA-EVAL-V02-00060 / 87044110 / candidate_rank = 100`.
- **C2:** fijados los inputs efectivos de EV-03 y EV-04.
- **C3:** ausencias parciales se describen como intersecciones negativas, no como `NO_DRIFT_IDENTIFIED`.
- **C4:** conclusiones nacionales limitadas a instrumentos efectivamente auditados.
- **C5:** para DESPA-PG.01 / RS 079-2026/SUNAT se mantiene separada la vigencia general de la disposición específica diferida.
- **C6:** se conserva:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

### 9. Fronteras normativas e interpretativas

Se congelan:

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`.

`DOCUMENT_TRACEABILITY ≠ LEGAL_SUFFICIENCY`.

`NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.

`DOCUMENT_RETRIEVAL ≠ EXPERT_INTERPRETATION ≠ LEGAL_CORRECTNESS`.

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_10_DIGIT`.

La oficialidad, vigencia o trazabilidad de una fuente no demuestra suficiencia jurídica para un caso concreto ni corrección clasificatoria. Recuperar o asociar un fragmento normativo no demuestra corrección normativa sustantiva.

La página institucional/orientativa SUNAT no sustituye un instrumento supranacional. Los textos auxiliares de interpretación no se convierten en normas vinculantes sin soporte oficial expreso.

### 10. Relación con F1–F5

0B-05C no constituye un pressure test de novelty y no modifica los estados provisionales de F1–F5.

- F1: `METHOD_BOUNDARY_RELEVANT` como máximo, por separación entre ranking histórico y autoridad/evidencia normativa.
- F2: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`, salvo frontera explicación ≠ decisión oficial.
- F3: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`.
- F4: `METHOD_BOUNDARY_RELEVANT` para separar fuente oficial/evidencia de corrección jurídica adjudicada.
- F5: `METHOD_BOUNDARY_RELEVANT` para distinguir trazabilidad de fuente de suficiencia/auditabilidad sustantiva.
- G6: permanece eliminado.
- G7: permanece absorbido en F2.

No se declara novelty ni gap definitivo.

### 11. Claims autorizados relacionados

Se preservan C21–C25 de `article/CLAIM_EVIDENCE_MATRIX.md` con sus límites:

- C21: drift/versionado y solapamiento material en Capítulo 87, sin inferir legal correctness ni impacto métrico desde el drift por sí solo;
- C22: EV03 `ZERO_AGGREGATE_CHANGE`;
- C23: EV04 `TINY_NONZERO_MRR_DECREASE_ONLY`;
- C24: D1a `POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT`;
- C25: impacto conjunto `METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A` y `DOWNSTREAM_REEXECUTION = NOT_REQUIRED`.

### 12. Claims prohibidos

0B-05C no autoriza:

- corrección jurídica por mera oficialidad de la fuente;
- corrección normativa sustantiva por mera asociación/retrieval;
- sustitución retrospectiva del snapshot Decisión 885;
- inferir impacto métrico desde drift o solapamiento por sí solos;
- significancia estadística no calculada;
- causalidad de la actualización normativa;
- generalización fuera del diseño de sensibilidad ejecutado;
- presentar el cierre como “sin impacto numérico material”;
- declarar novelty o gap definitivo;
- abrir `0B-06` automáticamente.

### 13. Trazabilidad del freeze

- respuesta normalizada aprobada: `article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`;
- commit de respuesta: `797a1c7b4230cf46c215e521b57701a68ba68734`;
- snapshot editorial consumido por la respuesta: `article/main-manuscript@ec542653cc3f95108c86f4ffeced51c2221e7b6c`;
- SRC-03 consumido por la respuesta: `docs/plan-maestro-temporal-2026-08-31@f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`;
- blob SRC-03 leído: `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`;
- auditoría final: `article/reviews/0B05C_FINAL_NORMALIZATION_EDITORIAL_REVIEW.md` — `PASS`;
- aprobación del autor: `article/reviews/0B05C_AUTHOR_APPROVAL.md`.

### 14. Gate posterior

```text
0B-05C = APPROVED / FROZEN
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = ASSESS_GENUINE_NEED_FOR_0B-06
0C = BLOCKED_UNTIL_PHASE_0B_CLOSED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

El freeze no abre automáticamente 0B-06.

---

## English

### 1. Status

- Block: `0B-05C — Authority, currency, and traceability of normative/official sources`.
- Status: **`APPROVED / FROZEN`**.
- Experimental/editorial reconciliation: completed.
- Writing-AI normalization: completed in `article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`.
- Final scientific/editorial audit: **`PASS`**.
- Material errors: `0`.
- Pending minor corrections: `0`.
- Additional experimental review: `NOT_REQUIRED`.
- Express author approval: received on `2026-09-15`.
- Novelty: `NOT_DECLARED`.
- Final gap: `NOT_DEFINED`.
- Manuscript: `NOT_DRAFTED`.
- `0B-06`: `NOT_STARTED / OPENING_NOT_AUTHORIZED`.

This artifact freezes the canonical editorial state of the block and does not modify or replace the original experimental artifacts.

### 2. Core documentary rule

The following separation is frozen:

`EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE`.

A later normative amendment does not retrospectively replace the snapshot used by the experiment. Likewise, an identifiable experimental source does not by itself establish that the corpus represented all law in force at execution time.

### 3. Preserved experimental snapshot

Frozen 0A-02 development ref:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

Confirmed normative ingestion sources are Arancel 2022, its run metadata, CAN Decision 885/Gazette 4359, and NANDINA run metadata. Recorded source-file SHA-256 values are `a01a029e...454c7d0` and `8c4a30fb...594f0c6` respectively; they are source-file hashes, not GitHub blob SHAs.

### 4. Audited official state and confirmed drift

The controlled primary-source audit covered WCO HS 2022/GIR as needed, Andean Decision 885, Decision 906, Resolution 2592, and the materially audited Peruvian national/procedural sources. National-level conclusions are bounded to the instruments actually audited.

Decision 906 amended Decision 885, became effective on `2023-01-01`, and includes Chapter-87 description changes including `8704.41.10` and `8704.51.10`. Therefore:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
```

Absence of `87044110`/`87045110` from EVAL labels or historical-ranking candidates is frozen only as a negative intersection in those components; it does not remove the global normative drift.

### 5. Confirmed output overlap

Frozen finding:

`DA-EVAL-V02-00060 / 87044110 / candidate_rank = 100`

in `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, under the Decision-885-derived description. `87045110` was not identified in that same flat Top-100 output.

```text
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25
```

Output overlap does not itself establish a change in any metric.

### 6. Effective artifact chain

Frozen effective inputs:

- EV-03: `data/processed/corpus_rag_v1_index.jsonl`;
- EV-04: `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.

For D1a:

```text
D1A_TRAINING_EXPOSURE = NO_EFFECTIVE_EXPOSURE_IDENTIFIED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NONE_IDENTIFIED
D1A_MODEL_POLICY = FREEZE_ORIGINAL_D1A_WEIGHTS
D1A_EXECUTION_SPECIFICATION = CLOSED_PROSPECTIVELY
```

### 7. Frozen corrective experimental closure

Historical sequence:

`initial documentary audit → confirmed drift/scope overlap → metric impact initially NOT_DETERMINED → experimental trigger → pre-execution audit/specification → corrective Attempt06 sensitivity → corrected final interpretation → METHOD_DEPENDENT impact → DOWNSTREAM_REEXECUTION = NOT_REQUIRED`.

Current frozen state:

```text
EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
0B05C_EXPERIMENTAL_CORRECTIVE_GATE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
```

The closure must not be reduced to “zero impact” or “no material numerical impact.” EV03 has zero aggregate change under the sensitivity, EV04 has a tiny nonzero MRR decrease, and D1a has a positive nonzero exact-ranking change with a minor mixed HS4 effect. No uncomputed statistical significance, causality, unevaluated practical relevance, or generalization is inferred.

### 8. Frozen C1–C6 corrections

C1–C6 are incorporated without exception: direct flat overlap; effective EV03/EV04 inputs; negative-intersection wording; bounded national-scope conclusions; DESPA-PG.01 temporal precision; and separation of drift, scope overlap, output overlap, and metric impact.

### 9. Normative and interpretive boundaries

Frozen boundaries:

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`.

`DOCUMENT_TRACEABILITY ≠ LEGAL_SUFFICIENCY`.

`NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.

`DOCUMENT_RETRIEVAL ≠ EXPERT_INTERPRETATION ≠ LEGAL_CORRECTNESS`.

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_10_DIGIT`.

Authority, currency, or traceability does not establish legal sufficiency for a specific case or classification correctness. Retrieval/association of a normative fragment does not establish substantive normative correctness.

### 10. Relationship to F1–F5

0B-05C is not a novelty pressure test and does not change provisional F1–F5 states. F1/F4/F5 are at most method-boundary relevant; F2/F3 are normally not relevant to the gap candidate except for the stated boundaries. G6 remains eliminated and G7 remains merged into F2. No final novelty/gap is declared.

### 11. Related authorized claims

C21–C25 remain authorized only within their recorded limits in `article/CLAIM_EVIDENCE_MATRIX.md`, including the method-dependent final impact and `DOWNSTREAM_REEXECUTION = NOT_REQUIRED`.

### 12. Prohibited claims

0B-05C does not authorize legal correctness from source authority, substantive normative correctness from association/retrieval alone, retrospective replacement of the Decision-885 snapshot, metric impact inferred from drift/overlap alone, uncomputed significance, causality, generalization, reduction of the closure to “no material numerical impact,” final novelty/gap, or automatic opening of `0B-06`.

### 13. Freeze traceability

- approved normalized response: `article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`;
- response commit: `797a1c7b4230cf46c215e521b57701a68ba68734`;
- editorial snapshot consumed by response: `article/main-manuscript@ec542653cc3f95108c86f4ffeced51c2221e7b6c`;
- SRC-03 consumed by response: `docs/plan-maestro-temporal-2026-08-31@f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`;
- SRC-03 blob read: `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`;
- final audit: `article/reviews/0B05C_FINAL_NORMALIZATION_EDITORIAL_REVIEW.md` — `PASS`;
- author approval: `article/reviews/0B05C_AUTHOR_APPROVAL.md`.

### 14. Subsequent gate

```text
0B-05C = APPROVED / FROZEN
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = ASSESS_GENUINE_NEED_FOR_0B-06
0C = BLOCKED_UNTIL_PHASE_0B_CLOSED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

The freeze does not automatically open 0B-06.
