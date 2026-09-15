# 0B-05 — Datos, procedencia, reproducibilidad, conocimiento y fuentes normativas / Data, provenance, reproducibility, knowledge, and normative sources

## Español

### 1. Propósito

`0B-05` completa el mapa de Fase 0B en tres dimensiones diferenciadas:

1. documentación/gobernanza de datos;
2. procedencia, trazabilidad, reproducibilidad y auditoría del ciclo de vida;
3. fundamentos de información/conocimiento y autoridad, vigencia y trazabilidad de fuentes normativas/oficiales.

El bloque no declara novelty. Su función es fijar fronteras científicas para describir banco histórico, corpus normativo, versionamiento, provenance, reproducibilidad, conocimiento explícito documental y autoridad normativa sin convertir documentación en correctness ni retrieval en juicio jurídico.

### 2. Sublotes

#### 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:

`article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

Fronteras congeladas:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:

`article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.

Fronteras congeladas:

- `data`, `information` y `knowledge` no son sinónimos universales ni etapas lineales necesarias;
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`;
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`;
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`;
- `DOCUMENTED_EXPLICIT_KNOWLEDGE` es solo `OPERACIONALIZACION_DEL_PROYECTO`.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:

`article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_FROZEN.md`.

Registros de cierre:

- prompt histórico: `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`;
- prompt de normalización final: `article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md`;
- respuesta aprobada de IA de Redacción: `article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`;
- reconciliación editorial del cierre experimental: `article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`;
- auditoría final de normalización: `article/reviews/0B05C_FINAL_NORMALIZATION_EDITORIAL_REVIEW.md` — `PASS`;
- aprobación del autor: `article/reviews/0B05C_AUTHOR_APPROVAL.md`.

#### 2.1 Naturaleza y regla documental

0B-05C es una auditoría de fuentes primarias oficiales, no un lote de literatura académica. Se congela:

`EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE`.

Una modificación normativa posterior no reemplaza retroactivamente la fuente usada por el experimento; una fuente experimental identificable tampoco prueba por sí sola que el corpus representara toda la normativa vigente en la fecha de ejecución.

#### 2.2 Snapshot experimental preservado

Ref de desarrollo congelado por 0A-02:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

Fuentes confirmadas:

1. `data/external/Arancel 2022.pdf`;
2. `data/processed/corpus/arancel/arancel2022_run_metadata.json`;
3. `data/external/CAN Desición 885 - Nanadina Gaceta 4359.pdf`;
4. `data/processed/corpus/nandina/run_metadata.json`.

SHA-256 de fuente:

- Arancel 2022: `a01a029e1ca29b6debc61d219c17dfc086354e00669246cc24a91ad9f454c7d0`;
- Decisión 885/Gaceta 4359: `8c4a30fb0328f151089ac4c7857ac447d3dd353de97122a11bde4550d594f0c6`.

El snapshot original no se sustituye retrospectivamente por Decisión 906 ni por los artefactos de sensibilidad correctiva.

#### 2.3 Estado documental congelado

La auditoría oficial confirmó que Decisión 906 modifica Decisión 885, entró en vigencia el `2023-01-01` e incluye cambios de descripción en subpartidas de Capítulo 87, entre ellas `8704.41.10` y `8704.51.10`.

Estado congelado:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25
```

Hallazgo material: `DA-EVAL-V02-00060 / 87044110 / candidate_rank = 100` en el output BM25 plano. La ausencia de `87044110`/`87045110` entre labels EVAL o candidatos históricos es únicamente una intersección negativa en esos componentes.

#### 2.4 Cierre experimental correctivo congelado

Inputs efectivos:

- EV-03: `data/processed/corpus_rag_v1_index.jsonl`;
- EV-04: `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.

D1a:

```text
D1A_TRAINING_EXPOSURE = NO_EFFECTIVE_EXPOSURE_IDENTIFIED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NONE_IDENTIFIED
D1A_MODEL_POLICY = FREEZE_ORIGINAL_D1A_WEIGHTS
D1A_EXECUTION_SPECIFICATION = CLOSED_PROSPECTIVELY
```

Impacto final:

```text
EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
0B05C_EXPERIMENTAL_CORRECTIVE_GATE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
```

Los estados históricos `NOT_DETERMINED` se preservan como historia, no como estado actual. El cierre no debe resumirse como “sin impacto numérico material”.

#### 2.5 Distinciones congeladas

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`.

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

`DOCUMENT_TRACEABILITY ≠ LEGAL_SUFFICIENCY`.

`NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_SUBHEADING-10`.

`INSTITUTIONAL_ORIENTATION_PAGE ≠ SUPRANATIONAL_LEGAL_INSTRUMENT`.

#### 2.6 Relación con F1–F5

0B-05C no es un pressure test de novelty y no cambia estados provisionales:

- F1: como máximo `METHOD_BOUNDARY_RELEVANT`;
- F2: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`, salvo explanation ≠ official decision;
- F3: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`;
- F4: `METHOD_BOUNDARY_RELEVANT`;
- F5: `METHOD_BOUNDARY_RELEVANT`;
- G6 permanece eliminado;
- G7 permanece absorbido en F2.

### 3. Estado de 0B-05

```text
0B-05A = APPROVED / FROZEN
0B-05B = APPROVED / FROZEN
0B-05C = APPROVED / FROZEN
```

El cierre de 0B-05C no abre automáticamente 0B-06.

### 4. Gate posterior

```text
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = ASSESS_GENUINE_NEED_FOR_0B-06
0C = BLOCKED_UNTIL_PHASE_0B_CLOSED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

Debe realizarse un gate separado para decidir si 0B-06 es necesario, omitible o requiere redefinición. Hasta esa decisión no se abre 0B-06 ni se declara cerrada la Fase 0B.

---

## English

### 1. Purpose

`0B-05` completes Phase 0B across data documentation/governance, provenance/reproducibility/lifecycle audit, and information/knowledge foundations plus official normative-source authority, currency, and traceability. It does not establish novelty.

### 2. Sub-batches

- `0B-05A = APPROVED / FROZEN`; canonical artifact: `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.
- `0B-05B = APPROVED / FROZEN`; canonical artifact: `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.
- `0B-05C = APPROVED / FROZEN`; canonical artifact: `article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_FROZEN.md`.

0B-05C is a primary official-source audit, not an academic-literature batch. It freezes the separation `EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE` and preserves the original Decision-885-based experimental snapshot rather than retrospectively replacing it.

Frozen documentary state:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25
```

Frozen corrective experimental closure:

```text
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

The closure must not be reduced to “no material numerical impact.” The block freezes the boundaries separating source authority, legal sufficiency, classification correctness, version drift, scope/output overlap, metric impact, and HS/NANDINA/national levels.

0B-05C does not alter provisional F1–F5 states, does not reopen G6, and does not restore G7 as an independent candidate.

### 3. 0B-05 status

```text
0B-05A = APPROVED / FROZEN
0B-05B = APPROVED / FROZEN
0B-05C = APPROVED / FROZEN
```

The 0B-05C closure does not automatically open 0B-06.

### 4. Subsequent gate

```text
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = ASSESS_GENUINE_NEED_FOR_0B-06
0C = BLOCKED_UNTIL_PHASE_0B_CLOSED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

A separate gate must decide whether 0B-06 is necessary, omittable, or requires redefinition. Until then, 0B-06 remains unopened and Phase 0B is not yet declared closed.
