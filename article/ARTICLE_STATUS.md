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
- Estado de `0B-05C`: **`CORRECTIVE_PREEXECUTION_SPECIFICATION_PENDING / CORRECTIVE_NUMERICAL_RERUN_REQUIRED`**.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG`: **`CLOSED — DRIFT_CONFIRMED`**.
- `EXPERIMENTAL_REVIEW`: **`REQUIRED`**.
- `TRIGGER`: **`EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`**.
- `EV03_METRIC_IMPACT`: **`NOT_DETERMINED`**.
- `EV04_METRIC_IMPACT`: **`NOT_DETERMINED`**.
- `EV-05 (identificador editorial del gate) ≡ EXP-04-D1a (identificador experimental canónico)`.
- `D1A_INDEX_EXPOSURE`: **`CONFIRMED`**.
- `D1A_TRAINING_EXPOSURE`: **`NOT_DETERMINED`**.
- `D1A_RETRIEVAL_OUTPUT_OVERLAP`: **`NOT_VERIFIED`**.
- `D1A_METRIC_IMPACT`: **`NOT_DETERMINED`**.
- `D1A_EXECUTION_SPECIFICATION`: **`PENDING`**.
- `DOWNSTREAM_REEXECUTION`: **`NOT_YET_JUSTIFIED`**.
- `0B-06`: **`NOT_STARTED / CLOSED_BY_GATE`**.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta cerrar 0C.
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

0B-05C puede detectar `SOURCE_VERSION_DRIFT`, pero no puede actualizar el corpus, rerun experimentos, recalcular resultados ni reinterpretar claims congelados. La revisión interna confirmó un trigger de afectación experimental y activó revisión de la IA experimental.

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

Prompt de análisis:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

Revisiones gobernantes del gate actual:

- `article/reviews/0B05C_INTERNAL_REVIEW.md`;
- `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`.

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

Una revisión editorial previa incorporó D1a al gate por su dependencia del corpus normativo plano. El segundo feedback experimental confirma que esa corrección era materialmente válida, pero exige desagregar la exposición antes de ejecutar. Para trazabilidad:

`EV-05 (identificador editorial del gate) ≡ EXP-04-D1a (identificador experimental canónico)`.

Estado refinado:

```text
0B05C_CORRECTIVE_EXPERIMENTAL_REVIEW = SUBSTANTIVELY_APPROVED_WITH_EXECUTION_SPECIFICATION_PENDING
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED
D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_EXECUTION_SPECIFICATION = PENDING
CORRECTIVE_NUMERICAL_RERUN = REQUIRED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```

`D1A_INDEX_EXPOSURE = CONFIRMED` no implica por sí sola exposición efectiva del entrenamiento, aparición de `87044110`/`87045110` en rankings D1a ni impacto métrico. Antes de cualquier rerun, la IA experimental debe verificar si esos códigos participaron como positivos y/o hard negatives del fine-tuning y si aparecen en `d1a_ranked_codes_top200.jsonl`. Con esa evidencia debe fijar prospectivamente si la sensibilidad D1a usa pesos congelados y reconstrucción del índice solamente, o si existe fundamento trazable para incluir reentrenamiento controlado.

### Gate vigente

```text
0B-05C = CORRECTIVE_PREEXECUTION_SPECIFICATION_PENDING / CORRECTIVE_NUMERICAL_RERUN_REQUIRED
-> IA experimental: auditar exposición de entrenamiento/output de EXP-04-D1a y fijar la especificación pre-ejecución
-> IA experimental: ejecutar después la sensibilidad numérica correctiva acotada según esa especificación
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
- 0B-05C: **`CORRECTIVE_PREEXECUTION_SPECIFICATION_PENDING / CORRECTIVE_NUMERICAL_RERUN_REQUIRED`**.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = CLOSED — DRIFT_CONFIRMED`.
- `EXPERIMENTAL_REVIEW = REQUIRED`.
- `TRIGGER = EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`.
- `EV03_METRIC_IMPACT = NOT_DETERMINED`.
- `EV04_METRIC_IMPACT = NOT_DETERMINED`.
- `EV-05 (editorial gate identifier) ≡ EXP-04-D1a (canonical experimental identifier)`.
- `D1A_INDEX_EXPOSURE = CONFIRMED`.
- `D1A_TRAINING_EXPOSURE = NOT_DETERMINED`.
- `D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED`.
- `D1A_METRIC_IMPACT = NOT_DETERMINED`.
- `D1A_EXECUTION_SPECIFICATION = PENDING`.
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`.
- 0B-06: `NOT_STARTED / CLOSED_BY_GATE`.
- 0C/0D remain blocked.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governance

Frozen 0A artifacts remain authoritative. 0B-05C may identify source-version drift but cannot update the corpus, rerun experiments, recalculate results, reinterpret frozen claims, or modify the Master Plan. The experimental AI retains exclusive authority over the Master Plan and experimental corrective decisions.

### 0B-05C current state

Scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Analysis prompt: `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

Current gate reviews:

- `article/reviews/0B05C_INTERNAL_REVIEW.md`;
- `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`;
- `article/reviews/0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`.

The frozen development snapshot at `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` identifies Arancel 2022 and CAN Decision 885/Gazette 4359 as ingested normative sources, together with their pipeline run metadata and recorded source-file SHA-256 values.

The internal scientific/editorial review returned `0B-05C_INTERNAL_REVIEW = PASS WITH CORRECTIONS`. Confirmed states remain `SOURCE_VERSION_DRIFT = PRESENT`, `SCOPE_OVERLAP = CONFIRMED`, `RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25`, and `EXPERIMENTAL_METRIC_IMPACT = NOT_DETERMINED`. The material flat-BM25 finding remains `DA-EVAL-V02-00060 / 87044110 / candidate_rank = 100` under the Decision-885-derived description.

### Editorial review of the corrective experimental gate

Subsequent experimental feedback keeps the gate open and supports bounded corrective numerical re-execution. Drift and Chapter-87 scope overlap are confirmed; no EVAL-label or historical-ranking impact is observed; EV-03 has a real overlap; and EV-03/EV-04 metric impact remains undetermined. No full benchmark rebuild, split rebuild, or label remap is justified, and the original snapshot must remain preserved.

A prior editorial review brought D1a into the gate because it depends on the flat normative corpus. The second experimental feedback confirms that this was a materially valid correction but requires exposure to be decomposed before execution. For traceability:

`EV-05 (editorial gate identifier) ≡ EXP-04-D1a (canonical experimental identifier)`.

Refined state:

```text
0B05C_CORRECTIVE_EXPERIMENTAL_REVIEW = SUBSTANTIVELY_APPROVED_WITH_EXECUTION_SPECIFICATION_PENDING
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED
D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_EXECUTION_SPECIFICATION = PENDING
CORRECTIVE_NUMERICAL_RERUN = REQUIRED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```

`D1A_INDEX_EXPOSURE = CONFIRMED` does not by itself establish effective training exposure, occurrence of `87044110`/`87045110` in D1a rankings, or metric impact. Before any rerun, the experimental AI must determine whether those codes actually participated as fine-tuning positives and/or hard negatives and whether they occur in `d1a_ranked_codes_top200.jsonl`. That evidence must prospectively fix whether the D1a sensitivity uses frozen weights with index reconstruction only or whether a traceable basis exists to include controlled retraining.

### Current gate

`0B-05C CORRECTIVE_PREEXECUTION_SPECIFICATION_PENDING / CORRECTIVE_NUMERICAL_RERUN_REQUIRED -> experimental AI audits EXP-04-D1a training/output exposure and fixes the pre-execution specification -> experimental AI then executes the bounded corrective numerical sensitivity under that specification -> final scientific/editorial review -> writing-AI correction/normalization if required -> express author approval -> freeze -> assess 0B-06 need`.

While 0B-05C remains open, no scientific-editor/writing-AI Master-Plan or 0A changes, retrospective replacement of the original normative snapshot, manuscript drafting, final novelty/gap declarations, 0B-06, 0C, or 0D are authorized.