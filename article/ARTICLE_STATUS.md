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
- Estado operativo de `0B-05C`: **`EXPERIMENTAL_REVIEW`**.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG`: **`CLOSED — DRIFT_CONFIRMED`**.
- `EXPERIMENTAL_REVIEW`: **`REQUIRED`**.
- `TRIGGER`: **`EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`**.
- `CORRECTIVE_PREEXECUTION_GATE`: **`OPEN`**.
- `CORRECTIVE_NUMERICAL_RERUN`: **`REQUIRED`**.
- `EV03_METRIC_IMPACT`: **`NOT_DETERMINED`**.
- `EV04_METRIC_IMPACT`: **`NOT_DETERMINED`**.
- `EV-05 (identificador editorial del gate) ≡ EXP-04-D1a (identificador experimental canónico)`.
- `D1A_INDEX_EXPOSURE`: **`CONFIRMED`**.
- `D1A_TRAINING_EXPOSURE`: **`NOT_DETERMINED`**.
- `D1A_RETRIEVAL_OUTPUT_OVERLAP`: **`NOT_VERIFIED`**.
- `D1A_METRIC_IMPACT`: **`NOT_DETERMINED`**.
- `D1A_MODEL_POLICY_RULE`: **`PREREGISTERED`**.
- `D1A_EXECUTION_SPECIFICATION`: **`PARTIALLY_PREREGISTERED / NOT_CLOSED`**.
- `D1A_NUMERICAL_EXECUTION`: **`NOT_AUTHORIZED`**.
- `DOWNSTREAM_REEXECUTION`: **`NOT_YET_JUSTIFIED`**.
- `0B-06`: **`BLOCKED`**; aún no iniciado y cerrado por el gate vigente de 0B-05C.
- `0C — Gap, contribución y Research Questions`: **`BLOCKED`** hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: **`BLOCKED`** hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Corpus académico/documental consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth y gobernanza

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

La Fase 0B no modifica el Plan Maestro ni 0A. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro y sobre decisiones experimentales correctivas.

0B-05C puede detectar `SOURCE_VERSION_DRIFT`, pero no puede actualizar el corpus, rerun experimentos, recalcular resultados ni reinterpretar claims congelados desde la rama editorial. La revisión interna confirmó un trigger de afectación experimental y activó revisión de la IA experimental.

`START_HERE.md` es vinculante para la taxonomía de estados operativos. Por ello, los estados correctivos específicos de 0B-05C se registran como flags/subestados y el estado operativo formal del bloque es `EXPERIMENTAL_REVIEW`.

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

0B-05C no está autorizado a cambiar estos estados; solo puede aportar fronteras metodológicas y evidencia documental oficial.

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

El plan de sublotes conserva `READY_FOR_DRAFTING` únicamente como estado histórico de apertura de 0B-05C y remite a este archivo para el estado vigente. El estado operativo actual es `EXPERIMENTAL_REVIEW`.

Prompt de análisis:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

Revisiones gobernantes del gate actual:

- `article/reviews/0B05C_INTERNAL_REVIEW.md`;
- `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_GOVERNANCE_NORMALIZATION_EDITORIAL_REVIEW.md`.

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

#### Fuentes oficiales auditadas

- WCO/OMA: HS Convention cuando fue necesario, HS Nomenclature 2022, GIR 2022, enmiendas complementarias pertinentes y estatus de Explanatory Notes para claims específicos.
- Comunidad Andina: Decisión 885/Gaceta 4359; Decisión 906/Gaceta 5062; Resolución 2592/Gaceta 5761.
- Perú: DS 404-2021-EF/Arancel de Aduanas 2022; modificaciones materialmente pertinentes; SUNAT/gob.pe NANDINA como orientación institucional; DESPA-PG.01 v8 y DESPA-PE.00.03 v4 únicamente para claims de procedencia/contexto administrativo.

#### Resultado de revisión interna

La revisión científica/editorial de 0B-05C emitió:

`0B-05C_INTERNAL_REVIEW = PASS WITH CORRECTIONS`.

Estados confirmados:

- `SOURCE_VERSION_DRIFT = PRESENT`;
- `SCOPE_OVERLAP = CONFIRMED`;
- `RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25`;
- `EXPERIMENTAL_METRIC_IMPACT = NOT_DETERMINED`;
- `EXPERIMENTAL_REVIEW = REQUIRED`;
- `TRIGGER = EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`.

Hallazgo material registrado: `87044110` aparece efectivamente en `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, caso `DA-EVAL-V02-00060`, `candidate_rank = 100`, con la descripción derivada del snapshot Decisión 885. No se identificó `87045110` en ese mismo output plano Top-100.

La revisión interna también dejó registradas las correcciones C1–C6 y mantiene la separación obligatoria:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

#### Revisión editorial del corrective experimental gate

El feedback experimental posterior mantiene abierto el gate y concluye que se requiere una reejecución numérica correctiva acotada. La revisión editorial acepta que el drift y el solapamiento de alcance en Capítulo 87 están confirmados; no se observa afectación de labels EVAL ni del ranking histórico; EV-03 presenta overlap real; y los impactos métricos de EV-03 y EV-04 continúan no determinados. No se justifica reconstrucción completa del benchmark, de los splits ni remapeo de labels, y cualquier sensibilidad debe preservar íntegramente el snapshot original.

Una revisión editorial previa incorporó D1a al gate por su dependencia del corpus normativo plano. Los feedback experimentales posteriores confirman que esa corrección era materialmente válida, pero exigen desagregar la exposición y cerrar la especificación antes de ejecutar. Para trazabilidad:

`EV-05 (identificador editorial del gate) ≡ EXP-04-D1a (identificador experimental canónico)`.

Estado refinado:

```text
0B-05C_OPERATIONAL_STATUS = EXPERIMENTAL_REVIEW
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED
D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_MODEL_POLICY_RULE = PREREGISTERED
D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
CORRECTIVE_NUMERICAL_RERUN = REQUIRED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```

`D1A_INDEX_EXPOSURE = CONFIRMED` no implica por sí sola exposición efectiva del entrenamiento, aparición de `87044110`/`87045110` en rankings D1a ni impacto métrico.

Antes de cualquier rerun, la IA experimental debe verificar exhaustivamente si esos códigos fueron realmente consumidos por el optimizador como targets positivos y/o hard negatives explícitos. La evidencia debe provenir del artefacto de entrenamiento efectivamente consumido y quedar vinculada por hash y/o run metadata; scripts, pools candidatos o mera presencia en corpus no bastan. Una función implícita *in-batch* bajo MNRL no se reclasifica como hard negative explícito.

También debe inspeccionarse el Top-200 congelado completo de D1a. Para cada aparición de `87044110` o `87045110` deben registrarse código, `case_id`, rank y número total de ocurrencias. Esto resuelve `D1A_RETRIEVAL_OUTPUT_OVERLAP`, no `D1A_TRAINING_EXPOSURE` ni `D1A_METRIC_IMPACT`.

La regla de política de pesos ya fue pre-registrada antes de observar métricas. Como recomendación prospectiva adicional, el control primario debe conservar los outputs originales congelados del snapshot Decisión 885; una eventual reejecución del control debe funcionar primero como verificación de reproducibilidad y reproducir el control congelado antes de utilizarse analíticamente. La especificación final continúa bajo autoridad de la IA experimental.

### Gate vigente

```text
0B-05C STATUS = EXPERIMENTAL_REVIEW
D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
-> IA experimental: resolver exhaustivamente D1A_TRAINING_EXPOSURE y D1A_RETRIEVAL_OUTPUT_OVERLAP
-> IA experimental: cerrar prospectivamente política de pesos, brazo control y especificación de ejecución
-> solo después, ejecutar la sensibilidad numérica correctiva acotada cuando corresponda
-> revisión científica/editorial final
-> corrección/normalización de 0B-05C por IA de Redacción, si corresponde
-> aprobación expresa del autor
-> freeze 0B-05C
-> evaluar necesidad de 0B-06
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
- abrir 0B-06, 0C o 0D.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01 through 0B-05B: **`APPROVED / FROZEN`**.
- Active block: **`0B-05C — Authority, currency, and traceability of normative/official sources`**.
- 0B-05C operational status: **`EXPERIMENTAL_REVIEW`**.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = CLOSED — DRIFT_CONFIRMED`.
- `EXPERIMENTAL_REVIEW = REQUIRED`.
- `TRIGGER = EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`.
- `CORRECTIVE_PREEXECUTION_GATE = OPEN`.
- `CORRECTIVE_NUMERICAL_RERUN = REQUIRED`.
- `EV03_METRIC_IMPACT = NOT_DETERMINED`.
- `EV04_METRIC_IMPACT = NOT_DETERMINED`.
- `EV-05 (editorial gate identifier) ≡ EXP-04-D1a (canonical experimental identifier)`.
- `D1A_INDEX_EXPOSURE = CONFIRMED`.
- `D1A_TRAINING_EXPOSURE = NOT_DETERMINED`.
- `D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED`.
- `D1A_METRIC_IMPACT = NOT_DETERMINED`.
- `D1A_MODEL_POLICY_RULE = PREREGISTERED`.
- `D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED`.
- `D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED`.
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`.
- 0B-06: **`BLOCKED`**; not started and closed by the current 0B-05C gate.
- 0C/0D remain **`BLOCKED`**.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governance

Frozen 0A artifacts remain authoritative. 0B-05C may identify source-version drift but cannot update the corpus, rerun experiments, recalculate results, reinterpret frozen claims, or modify the Master Plan from the editorial branch. The experimental AI retains exclusive authority over the Master Plan and experimental corrective decisions.

`START_HERE.md` governs the operational-status taxonomy. Therefore, corrective details for 0B-05C are recorded as flags/substates and the formal operational state of the block is `EXPERIMENTAL_REVIEW`.

### 0B-05C current state

Scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`. The batch plan now preserves `READY_FOR_DRAFTING` only as the historical opening state and defers to this file for the current operational state.

Analysis prompt: `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

Current governing reviews:

- `article/reviews/0B05C_INTERNAL_REVIEW.md`;
- `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_GOVERNANCE_NORMALIZATION_EDITORIAL_REVIEW.md`.

The frozen development snapshot at `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` identifies Arancel 2022 and CAN Decision 885/Gazette 4359 as ingested normative sources, together with their pipeline run metadata and recorded source-file SHA-256 values.

The internal scientific/editorial review returned `0B-05C_INTERNAL_REVIEW = PASS WITH CORRECTIONS`. Confirmed states remain `SOURCE_VERSION_DRIFT = PRESENT`, `SCOPE_OVERLAP = CONFIRMED`, `RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25`, and `EXPERIMENTAL_METRIC_IMPACT = NOT_DETERMINED`. The material flat-BM25 finding remains `DA-EVAL-V02-00060 / 87044110 / candidate_rank = 100` under the Decision-885-derived description.

### Editorial review of the corrective experimental gate

Subsequent experimental feedback keeps the gate open and supports bounded corrective numerical re-execution. Drift and Chapter-87 scope overlap are confirmed; no EVAL-label or historical-ranking impact is observed; EV-03 has a real overlap; and EV-03/EV-04 metric impact remains undetermined. No full benchmark rebuild, split rebuild, or label remap is justified, and the original snapshot must remain preserved.

A prior editorial review brought D1a into the gate because it depends on the flat normative corpus. Subsequent experimental feedback confirms that this was a materially valid correction but requires exposure to be decomposed and the execution specification to be closed before any run. For traceability:

`EV-05 (editorial gate identifier) ≡ EXP-04-D1a (canonical experimental identifier)`.

Refined state:

```text
0B-05C_OPERATIONAL_STATUS = EXPERIMENTAL_REVIEW
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED
D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_MODEL_POLICY_RULE = PREREGISTERED
D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
CORRECTIVE_NUMERICAL_RERUN = REQUIRED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```

`D1A_INDEX_EXPOSURE = CONFIRMED` does not establish effective training exposure, occurrence of `87044110`/`87045110` in D1a rankings, or metric impact.

Before any rerun, the experimental AI must exhaustively determine whether those codes were actually consumed by the optimizer as positive targets and/or explicit hard negatives. Evidence must come from the training artifact actually consumed and be tied to hash and/or run metadata; scripts, candidate pools, or mere corpus occurrence are insufficient. An implicit *in-batch* role under MNRL is not relabeled as an explicit hard negative.

The complete frozen D1a Top-200 must also be inspected. Every occurrence of `87044110` or `87045110` must record code, `case_id`, rank, and total occurrence count. This resolves `D1A_RETRIEVAL_OUTPUT_OVERLAP`, not `D1A_TRAINING_EXPOSURE` or `D1A_METRIC_IMPACT`.

The model-weight decision rule is already preregistered before any sensitivity metrics are observed. As an additional prospective recommendation, the primary control should remain the frozen original outputs from the Decision-885 snapshot; any control rerun should first serve as a reproducibility check and reproduce the frozen control before analytical use. Final experimental specification remains under the experimental AI's authority.

### Current gate

```text
0B-05C STATUS = EXPERIMENTAL_REVIEW
D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
-> experimental AI exhaustively resolves D1A_TRAINING_EXPOSURE and D1A_RETRIEVAL_OUTPUT_OVERLAP
-> experimental AI prospectively closes model-weight, control-arm, and execution policies
-> only then, execute the bounded corrective numerical sensitivity when appropriate
-> final scientific/editorial review
-> writing-AI correction/normalization if required
-> express author approval
-> freeze 0B-05C
-> assess need for 0B-06
```

While 0B-05C remains open, no scientific-editor/writing-AI Master-Plan or 0A changes, retrospective replacement of the original normative snapshot, manuscript drafting, final novelty/gap declarations, 0B-06, 0C, or 0D are authorized.