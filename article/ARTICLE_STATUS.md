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
- Bloque activo: **`0B-06 — Búsqueda dirigida de literatura nueva para falsación de candidatos`**.
- `0B-06`: **`READY_FOR_DRAFTING`**.
- `0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT`: **`REQUIRED`**.
- `0B06_SCOPE`: **`DIRECTED_FALSIFICATION_SEARCH_ONLY`**.
- `OPEN_ENDED_LITERATURE_EXPANSION`: **`NOT_AUTHORIZED`**.
- `EXPERIMENTAL_REVIEW`: **`NOT_REQUIRED`** para este gate bibliográfico.
- `0C — Gap, contribución y Research Questions`: **`BLOCKED`** hasta cerrar formalmente 0B.
- `0D — Arquitectura editorial y journal fit`: **`BLOCKED`** hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- Corpus académico/documental heredado consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth y gobernanza

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

La Fase 0B no modifica el Plan Maestro ni 0A. La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y sobre decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados, gates, claims, admisión bibliográfica y reconciliación editorial. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

`START_HERE.md` es vinculante para la taxonomía de estados operativos.

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

### Candidatos provisionales antes de 0B-06

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **G6:** `ELIMINATED AS GAP CANDIDATE`.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

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

Estado documental congelado:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25
```

Cierre experimental correctivo congelado:

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

Claims relacionados autorizados en `CLAIM_EVIDENCE_MATRIX.md`: C21–C25.

### 0B-06 — gate de necesidad y apertura

Revisión gobernante:

`article/reviews/0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT.md`.

El gate concluyó que sí existe una necesidad bibliográfica **estrecha y concreta**, no una insuficiencia general del corpus. Antes de 0C deben someterse a un último pressure test contemporáneo y falsacionista:

- **F1:** ranking histórico/precedentes fijado antes de evidence retrieval normativo no-reranking;
- **F2:** LLM/generador exclusivamente explicativo sobre Top-k externo e inmutable;
- **F3:** secundariamente, grouped split/dependencia/leakage control comparable;
- **F5:** evaluación formal, separada y per-output/case-level de auditabilidad documental.

F4 no requiere búsqueda dedicada porque queda como frontera metodológica, no como novelty candidata independiente.

Prompt gobernante:

`article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md`.

Artefacto de respuesta esperado:

`article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`.

Las nuevas referencias no pueden pasar directamente al manuscrito ni a `APPROVED_NEW`; primero requieren auditoría de la IA Gestora / Editor Científico Principal.

### Gate vigente

```text
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
NEXT_ACTOR = IA_DE_REDACCION
PROMPT = article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md
EXPECTED_RESPONSE = article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md
0C = BLOCKED_UNTIL_PHASE_0B_CLOSED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

### Prohibiciones vigentes

Durante 0B-06 no está autorizado:

- modificar Plan Maestro o 0A desde el flujo editorial;
- sustituir retrospectivamente fuentes experimentales;
- modificar resultados experimentales;
- declarar novelty o gap definitivo;
- hacer una búsqueda abierta/general de literatura;
- reabrir G6 o G7;
- tratar F4 como novelty independiente;
- insertar referencias nuevas directamente en el manuscrito;
- avanzar a 0C, 0D o manuscrito antes de cerrar formalmente 0B.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- `0B-01` through `0B-05C`: **`APPROVED / FROZEN`**.
- Active block: **`0B-06 — Directed new-literature search to falsify candidates`**.
- `0B-06 = READY_FOR_DRAFTING`.
- `0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT = REQUIRED`.
- `0B06_SCOPE = DIRECTED_FALSIFICATION_SEARCH_ONLY`.
- `OPEN_ENDED_LITERATURE_EXPANSION = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` for this bibliographic gate.
- 0C and 0D remain **`BLOCKED`**.
- Target journal remains pending until 0D.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- Inherited academic/documentary corpus: `62` distinct works/documents with verifiable primary access `62/62`.

### Governance

Frozen 0A artifacts remain authoritative. The Experimental AI retains exclusive authority over the Master Plan and experimental decisions. The Managing AI / Lead Scientific Editor manages editorial states, gates, claims, bibliographic admission, and reconciliation. The Writing AI executes only closed versioned prompts.

### Frozen foundational distinctions

0B-04A, 0B-04B, 0B-05A, 0B-05B, and 0B-05C preserve their frozen methodological/documentary boundaries, including the separation among candidate generation, reranking, explanation, provenance/auditability, substantive/legal correctness, documented knowledge, and current official versus original experimental normative state.

### Provisional candidates before 0B-06

No candidate is final novelty or a definitive gap. F1 survives narrowly; F2 and F5 are further narrowed; F3 remains with an applicability caveat; F4 is retained only as a methodological distinction; G6 is eliminated and G7 is merged into F2.

### 0B-05C formal closure

0B-05C is `APPROVED / FROZEN`. Its documentary and corrective experimental states remain exactly as recorded in its frozen artifact and C21–C25 remain authorized within their limits.

### 0B-06 need gate and opening

Governing review:

`article/reviews/0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT.md`.

The gate found a **narrow, concrete** bibliographic need rather than broad inadequacy of the inherited corpus. Before 0C, one final contemporary falsification-oriented pressure test is required for F1, F2, F5 and secondarily F3. F4 requires no dedicated search because it remains a methodological boundary rather than an independent novelty candidate.

Governing prompt:

`article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md`.

Expected response artifact:

`article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`.

New references cannot be inserted into the manuscript or promoted directly to `APPROVED_NEW`; Managing-AI review is required first.

### Current gate

```text
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
NEXT_ACTOR = WRITING_AI
PROMPT = article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md
EXPECTED_RESPONSE = article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md
0C = BLOCKED_UNTIL_PHASE_0B_CLOSED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

During 0B-06, the editorial flow may not modify the Master Plan/0A or experimental results, declare final novelty/gap, run an open-ended literature search, reopen G6/G7, treat F4 as independent novelty, insert new references directly into the manuscript, or advance to 0C/0D/manuscript drafting before Phase 0B formally closes.