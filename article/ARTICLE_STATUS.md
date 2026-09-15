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
- Bloque activo: **`0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales`**.
- Estado operativo de `0B-05C`: **`REVISION_REQUIRED`**.
- `EXPERIMENTAL_REVIEW`: **`NOT_REQUIRED_FOR_CURRENT_NORMALIZATION`**.
- `0B05C_EXPERIMENTAL_CORRECTIVE_GATE`: **`CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION`**.
- `DRAFT_NORMALIZATION`: **`REQUIRED`**.
- `AUTHOR_APPROVAL`: **`NOT_REQUESTED`**.
- `FREEZE_0B05C`: **`NOT_AUTHORIZED`**.
- `0B-06`: **`NOT_STARTED`**; su apertura no está autorizada hasta cerrar/freeze 0B-05C y evaluar necesidad bibliográfica real.
- `0C — Gap, contribución y Research Questions`: **`BLOCKED`** hasta cerrar 0B.
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

La Fase 0B no modifica el Plan Maestro ni 0A. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro y sobre decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados, gates, claims y reconciliación editorial. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

`START_HERE.md` es vinculante para la taxonomía de estados operativos. El estado formal actual de 0B-05C es `REVISION_REQUIRED`; los estados experimentales correctivos se registran como evidencia/subestados y no sustituyen el estado editorial formal.

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

### Candidatos provisionales

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`; solo permanece el candidato estrecho de evaluación formal, explícita y separada de auditabilidad documental por salida.
- **G6:** `ELIMINATED AS GAP CANDIDATE`.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-05C no cambia estos estados; aporta fronteras metodológicas, evidencia documental oficial y la reconciliación de una sensibilidad correctiva.

### 0B-05B — cierre formal

Registros gobernantes:

- `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`;
- `article/reviews/0B05B_INTERNAL_REVIEW.md`;
- `article/reviews/0B05B_AUTHOR_APPROVAL.md`;
- `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.

Estado: **`APPROVED / FROZEN`**; `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

### 0B-05C — estado vigente

Alcance:

`article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Prompt histórico de análisis:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

Prompt vigente para la IA de Redacción:

`article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md`.

Revisiones gobernantes de la cadena 0B-05C:

- `article/reviews/0B05C_INTERNAL_REVIEW.md`;
- `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_GOVERNANCE_NORMALIZATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`.

#### Snapshot experimental que debe preservarse

Ref de desarrollo congelado por 0A-02:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

Fuentes normativas de ingesta confirmadas:

- `data/external/Arancel 2022.pdf`;
- `data/processed/corpus/arancel/arancel2022_run_metadata.json`;
- `data/external/CAN Desición 885 - Nanadina Gaceta 4359.pdf`;
- `data/processed/corpus/nandina/run_metadata.json`.

SHA-256 fuente registrados:

- Arancel 2022: `a01a029e1ca29b6debc61d219c17dfc086354e00669246cc24a91ad9f454c7d0`;
- Decisión 885/Gaceta 4359: `8c4a30fb0328f151089ac4c7857ac447d3dd353de97122a11bde4550d594f0c6`.

El snapshot original no se sustituye retrospectivamente por Decisión 906 ni por los artefactos de sensibilidad correctiva.

#### Resultado documental confirmado

- `SOURCE_VERSION_DRIFT = PRESENT`;
- `SCOPE_OVERLAP = CONFIRMED`;
- `RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25`.

Hallazgo material conservado: `87044110` aparece en `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, caso `DA-EVAL-V02-00060`, `candidate_rank = 100`, con descripción derivada del snapshot Decisión 885. No se identificó `87045110` en ese output plano Top-100.

La ausencia de `87044110`/`87045110` entre labels EVAL o candidatos históricos es una intersección negativa en esos componentes, no `NO_DRIFT_IDENTIFIED` para el problema normativo global.

Debe mantenerse:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

#### Cierre experimental correctivo

El gate experimental posterior resolvió las incógnitas preejecución y cerró la sensibilidad correctiva. Estado vigente:

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

Los estados históricos `NOT_DETERMINED`, las autorizaciones preejecución y los intentos fail-closed continúan preservados en sus artefactos, pero ya no son el estado actual.

No está autorizado resumir este cierre como “sin impacto numérico material”: EV04 y D1a presentan cambios no nulos y el efecto final es dependiente del método.

Claims reconciliados en `CLAIM_EVIDENCE_MATRIX.md`: C21–C25.

### Gate vigente

```text
0B-05C STATUS = REVISION_REQUIRED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION
-> IA de Redacción: ejecutar exclusivamente article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md
-> crear únicamente el artefacto normalizado indicado por ese prompt
-> IA Gestora / Editor Científico Principal: auditoría científica/editorial final
-> revisión experimental solo si aparece una contradicción científica nueva
-> aprobación expresa del autor
-> freeze 0B-05C
-> evaluar necesidad real de 0B-06
```

### Prohibiciones vigentes

Mientras 0B-05C permanezca abierto no está autorizado:

- que el editor científico o la IA de Redacción modifiquen el Plan Maestro o 0A;
- sustituir retrospectivamente las fuentes usadas por el experimento;
- modificar/actualizar el snapshot normativo original;
- inferir legal correctness desde oficialidad o trazabilidad;
- confundir HS-6, NANDINA-8 y subpartida nacional de 10 dígitos;
- redactar el manuscrito;
- declarar novelty/gap definitivo;
- abrir 0B-06;
- avanzar a 0C o 0D.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01 through 0B-05B: **`APPROVED / FROZEN`**.
- Active block: **`0B-05C — Authority, currency, and traceability of normative/official sources`**.
- 0B-05C operational status: **`REVISION_REQUIRED`**.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION`.
- `0B05C_EXPERIMENTAL_CORRECTIVE_GATE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION`.
- `DRAFT_NORMALIZATION = REQUIRED`.
- `AUTHOR_APPROVAL = NOT_REQUESTED`.
- `FREEZE_0B05C = NOT_AUTHORIZED`.
- 0B-06: **`NOT_STARTED`**; opening is not authorized until 0B-05C is closed/frozen and a genuine bibliographic need is assessed.
- 0C/0D remain **`BLOCKED`**.
- Target journal remains pending until 0D; manuscript drafting has not started.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.

### Governance

Frozen 0A artifacts remain authoritative. The experimental AI retains exclusive authority over the Master Plan and experimental decisions. The Managing AI / Lead Scientific Editor manages editorial states, gates, claims, and reconciliation. The Writing AI executes only closed versioned prompts.

`START_HERE.md` governs the operational-status taxonomy. The current formal state of 0B-05C is `REVISION_REQUIRED`; corrective experimental states are evidence/substates and do not replace the formal editorial state.

### Frozen foundational distinctions

0B-04A:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

0B-04B:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

0B-05A:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

0B-05B preserves the distinctions among data/information/knowledge, documented knowledge and total expertise, document retrieval and expert/legal interpretation, and LLM explanation and official classification. `DOCUMENTED_EXPLICIT_KNOWLEDGE` remains project operationalization only.

### Provisional candidates

No candidate constitutes final novelty or gap. F1–F5 preserve their previously frozen provisional states; G6 remains eliminated and G7 remains merged into F2.

### 0B-05C current state

Scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Historical analysis prompt: `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

Current Writing-AI prompt: `article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md`.

Governing review chain includes the previous 0B-05C internal/D1a reviews and `article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`.

The original frozen development snapshot remains `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`, with Arancel 2022 and CAN Decision 885/Gazette 4359 as ingested normative sources and their recorded source-file SHA-256 values. The original snapshot is not retrospectively replaced by Decision 906 or the corrective-sensitivity artifacts.

Confirmed documentary state:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25
```

The material flat-BM25 finding remains `DA-EVAL-V02-00060 / 87044110 / candidate_rank = 100` under the Decision-885-derived description. Absence of `87044110`/`87045110` from EVAL labels or historical candidates is a negative intersection in those components, not global `NO_DRIFT_IDENTIFIED`.

Mandatory separation:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

The subsequent experimental gate resolved the pre-execution uncertainties and closed the corrective sensitivity. Current state:

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

Historical `NOT_DETERMINED` states, pre-execution authorizations, and fail-closed attempts remain preserved in their artifacts but are no longer current.

This closure must not be summarized as “no material numerical impact”: EV04 and D1a contain nonzero changes and the final effect is method-dependent.

Reconciled claims in `CLAIM_EVIDENCE_MATRIX.md`: C21–C25.

### Current gate

```text
0B-05C STATUS = REVISION_REQUIRED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_FOR_CURRENT_NORMALIZATION
-> Writing AI executes only article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md
-> creates only the normalized artifact specified by that prompt
-> Managing AI / Lead Scientific Editor performs final scientific/editorial audit
-> experimental review only if a new scientific contradiction appears
-> express author approval
-> freeze 0B-05C
-> assess genuine need for 0B-06
```

While 0B-05C remains open, Master-Plan/0A modification from the editorial flow, retrospective source replacement, manuscript drafting, final novelty/gap declarations, opening 0B-06, 0C, and 0D remain unauthorized.