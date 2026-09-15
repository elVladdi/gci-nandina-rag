# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**.
- `0B-04A`: **`APPROVED / FROZEN`**.
- `0B-04B`: **`APPROVED / FROZEN`**.
- `0B-05A`: **`APPROVED / FROZEN`**.
- `0B-05B`: **`APPROVED / FROZEN`**.
- `0B-05C`: **`APPROVED / FROZEN`**.
- `0B05C_EXPERIMENTAL_CORRECTIVE_GATE`: **`CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION`**.
- `DRAFT_NORMALIZATION`: **`COMPLETED`**.
- `FINAL_NORMALIZATION_REVIEW`: **`PASS`**.
- `AUTHOR_APPROVAL`: **`RECEIVED`**.
- `FREEZE_0B05C`: **`COMPLETED`**.
- `EXPERIMENTAL_REVIEW`: **`NOT_REQUIRED`** para el cierre editorial final.
- `0B-06`: **`NOT_STARTED / OPENING_NOT_AUTHORIZED`**; debe evaluarse en un gate separado si existe una necesidad bibliográfica real.
- `0C — Gap, contribución y Research Questions`: **`BLOCKED`** hasta cerrar formalmente 0B.
- `0D — Arquitectura editorial y journal fit`: **`BLOCKED`** hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- Corpus académico/documental consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth y gobernanza

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

La Fase 0B no modifica el Plan Maestro ni 0A. La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y sobre decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados, gates, claims y reconciliación editorial. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

`START_HERE.md` es vinculante para la taxonomía de estados operativos. `0B-05C` ya superó reconciliación experimental, normalización de redacción, auditoría científica/editorial final y aprobación expresa del autor; por ello su estado formal actual es `APPROVED / FROZEN`.

### Distinciones fundacionales congeladas

0B-04A:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

0B-04B:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

0B-05A:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

0B-05B:

- `data`, `information` y `knowledge` no son sinónimos universales ni etapas lineales necesarias;
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`;
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`;
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`;
- `DOCUMENTED_EXPLICIT_KNOWLEDGE` es solo `OPERACIONALIZACION_DEL_PROYECTO`.

0B-05C:

- `EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE`;
- `SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`;
- `OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`;
- `DOCUMENT_TRACEABILITY ≠ LEGAL_SUFFICIENCY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_10_DIGIT`.

### Candidatos provisionales

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **G6:** `ELIMINATED AS GAP CANDIDATE`.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-05C no cambia estos estados; aporta fronteras metodológicas, evidencia documental oficial y el cierre de una sensibilidad correctiva.

### 0B-05C — cierre formal

Registros gobernantes:

- `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`;
- `article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md`;
- `article/responses/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE_RESPONSE_V01.md`;
- `article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_FINAL_NORMALIZATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_AUTHOR_APPROVAL.md`;
- `article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_FROZEN.md`.

Estado: **`APPROVED / FROZEN`**.

#### Snapshot experimental preservado

Ref de desarrollo congelado por 0A-02:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

Fuentes de ingesta confirmadas:

- `data/external/Arancel 2022.pdf`;
- `data/processed/corpus/arancel/arancel2022_run_metadata.json`;
- `data/external/CAN Desición 885 - Nanadina Gaceta 4359.pdf`;
- `data/processed/corpus/nandina/run_metadata.json`.

SHA-256 fuente:

- Arancel 2022: `a01a029e1ca29b6debc61d219c17dfc086354e00669246cc24a91ad9f454c7d0`;
- Decisión 885/Gaceta 4359: `8c4a30fb0328f151089ac4c7857ac447d3dd353de97122a11bde4550d594f0c6`.

El snapshot original no se sustituye retrospectivamente por Decisión 906 ni por los artefactos correctivos.

#### Resultado documental congelado

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25
```

Hallazgo material: `DA-EVAL-V02-00060 / 87044110 / candidate_rank = 100` en el output BM25 plano bajo descripción derivada del snapshot Decisión 885. No se identificó `87045110` en ese mismo Top-100.

#### Cierre experimental correctivo congelado

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

Los estados históricos `NOT_DETERMINED`, gates preejecución e intentos fail-closed permanecen preservados como historia y no representan el estado actual.

No está autorizado resumir este cierre como “sin impacto numérico material”.

Claims relacionados autorizados en `CLAIM_EVIDENCE_MATRIX.md`: C21–C25.

### Gate vigente

```text
0B-05C = APPROVED / FROZEN
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = ASSESS_GENUINE_NEED_FOR_0B-06
0C = BLOCKED_UNTIL_PHASE_0B_CLOSED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

El freeze de 0B-05C **no abre automáticamente 0B-06**.

### Prohibiciones vigentes

Hasta el siguiente gate editorial no está autorizado:

- modificar Plan Maestro o 0A desde el flujo editorial;
- sustituir retrospectivamente fuentes experimentales;
- modificar resultados experimentales;
- inferir legal correctness desde oficialidad/trazabilidad;
- declarar novelty o gap definitivo;
- abrir 0B-06 sin decisión expresa del gate correspondiente;
- avanzar a 0C, 0D o manuscrito antes de cerrar formalmente 0B.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01 through 0B-05C: **`APPROVED / FROZEN`**.
- `0B05C_EXPERIMENTAL_CORRECTIVE_GATE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION`.
- `DRAFT_NORMALIZATION = COMPLETED`.
- `FINAL_NORMALIZATION_REVIEW = PASS`.
- `AUTHOR_APPROVAL = RECEIVED`.
- `FREEZE_0B05C = COMPLETED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` for final editorial closure.
- 0B-06: **`NOT_STARTED / OPENING_NOT_AUTHORIZED`**; genuine bibliographic need must be assessed under a separate gate.
- 0C/0D remain **`BLOCKED`**.
- Target journal remains pending until 0D.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.

### Governance

Frozen 0A artifacts remain authoritative. The Experimental AI retains exclusive authority over the Master Plan and experimental decisions. The Managing AI / Lead Scientific Editor manages editorial states, gates, claims, and reconciliation. The Writing AI executes only closed versioned prompts.

`0B-05C` has completed experimental reconciliation, Writing-AI normalization, final scientific/editorial audit, and express author approval; its formal state is therefore `APPROVED / FROZEN`.

### Frozen foundational distinctions

0B-04A, 0B-04B, 0B-05A, and 0B-05B preserve their previously frozen distinctions. 0B-05C additionally freezes:

`EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE`.

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`.

`DOCUMENT_TRACEABILITY ≠ LEGAL_SUFFICIENCY`.

`NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_10_DIGIT`.

### Provisional candidates

No candidate constitutes final novelty or gap. F1–F5 preserve their previously frozen provisional states; G6 remains eliminated and G7 remains merged into F2.

### 0B-05C formal closure

Governing records include the historical and final 0B-05C prompts/reviews, the approved Writing-AI response, `article/reviews/0B05C_AUTHOR_APPROVAL.md`, and the canonical frozen artifact `article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_FROZEN.md`.

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

Historical `NOT_DETERMINED` states remain process history only. The closure must not be reduced to “no material numerical impact.” C21–C25 remain authorized within their recorded limits.

### Current gate

```text
0B-05C = APPROVED / FROZEN
0B-06 = NOT_STARTED / OPENING_NOT_AUTHORIZED
NEXT_EDITORIAL_ACTION = ASSESS_GENUINE_NEED_FOR_0B-06
0C = BLOCKED_UNTIL_PHASE_0B_CLOSED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

The 0B-05C freeze does **not** automatically open 0B-06.

Until the next editorial gate, the editorial flow may not modify the Master Plan/0A or experimental results, retrospectively replace experimental sources, infer legal correctness from authority/traceability, declare final novelty/gap, open 0B-06 without an explicit gate decision, or advance to 0C/0D/manuscript drafting before formal Phase-0B closure.
