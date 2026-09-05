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
- Estado de `0B-05C`: **`CORRECTIVE_EXPERIMENTAL_REVIEWED / CORRECTIVE_NUMERICAL_RERUN_REQUIRED`**.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG`: **`CLOSED — DRIFT_CONFIRMED`**.
- `EXPERIMENTAL_REVIEW`: **`REQUIRED`**.
- `TRIGGER`: **`EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`**.
- `CORRECTIVE_GATE_SCOPING`: **`INCOMPLETE`**.
- `EV03_METRIC_IMPACT`: **`NOT_DETERMINED`**.
- `EV04_METRIC_IMPACT`: **`NOT_DETERMINED`**.
- `EV05_D1A_STATUS`: **`REQUIRES_EXPLICIT_INCLUSION_OR_EXCLUSION_JUSTIFICATION`**.
- `DOWNSTREAM_REEXECUTION`: **`CONDITIONAL_ON_PROPAGATION`**.
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
- `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`.

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

El feedback experimental posterior mantiene abierto el gate y concluye que se requiere una reejecución numérica correctiva acotada. La revisión editorial acepta que:

- el drift y el solapamiento de alcance en Capítulo 87 están confirmados;
- no se observa afectación de labels EVAL ni del ranking histórico por este hallazgo;
- EV-03 presenta overlap real y `EV03_METRIC_IMPACT = NOT_DETERMINED`;
- `EV04_METRIC_IMPACT = NOT_DETERMINED`;
- no se justifica reconstrucción completa del benchmark, de los splits ni remapeo de labels;
- cualquier sensibilidad debe preservar íntegramente el snapshot original;
- downstream solo debe reabrirse ante propagación demostrada.

Corrección material pendiente: el feedback actual acota la reejecución a EV-03/EV-04, pero una revisión experimental previa había identificado EV-05/D1a como potencialmente expuesto por dependencia directa de `corpus_rag_v1_index.jsonl`. El feedback actual no documenta por qué D1a deja de formar parte de ese alcance. Por ello, antes del cierre, la IA experimental debe **incluir EV-05/D1a en la sensibilidad correctiva o excluirlo explícitamente con evidencia trazable suficiente**. Esto no implica un rerun automático de D1a.

Dictamen:

```text
0B05C_CORRECTIVE_EXPERIMENTAL_REVIEW = PASS_WITH_MATERIAL_CORRECTION
CORRECTIVE_GATE_SCOPING = INCOMPLETE
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED
EV05_D1A_STATUS = REQUIRES_EXPLICIT_INCLUSION_OR_EXCLUSION_JUSTIFICATION
DOWNSTREAM_REEXECUTION = CONDITIONAL_ON_PROPAGATION
CORRECTIVE_NUMERICAL_RERUN = REQUIRED
0B05C_CLOSURE = NOT_AUTHORIZED
```

### Gate vigente

```text
0B-05C = CORRECTIVE_EXPERIMENTAL_REVIEWED / CORRECTIVE_NUMERICAL_RERUN_REQUIRED
-> IA experimental: completar comprobación numérica correctiva y resolver explícitamente EV-05/D1a
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
- 0B-05C: **`CORRECTIVE_EXPERIMENTAL_REVIEWED / CORRECTIVE_NUMERICAL_RERUN_REQUIRED`**.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = CLOSED — DRIFT_CONFIRMED`.
- `EXPERIMENTAL_REVIEW = REQUIRED`.
- `TRIGGER = EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`.
- `CORRECTIVE_GATE_SCOPING = INCOMPLETE`.
- `EV03_METRIC_IMPACT = NOT_DETERMINED`.
- `EV04_METRIC_IMPACT = NOT_DETERMINED`.
- `EV05_D1A_STATUS = REQUIRES_EXPLICIT_INCLUSION_OR_EXCLUSION_JUSTIFICATION`.
- `DOWNSTREAM_REEXECUTION = CONDITIONAL_ON_PROPAGATION`.
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
- `article/reviews/0B05C_CORRECTIVE_EXPERIMENTAL_FEEDBACK_EDITORIAL_REVIEW.md`.

The frozen development snapshot at `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` identifies Arancel 2022 and CAN Decision 885/Gazette 4359 as ingested normative sources, together with their pipeline run metadata and recorded source-file SHA-256 values.

The internal scientific/editorial review returned:

`0B-05C_INTERNAL_REVIEW = PASS WITH CORRECTIONS`.

Confirmed states:

- `SOURCE_VERSION_DRIFT = PRESENT`;
- `SCOPE_OVERLAP = CONFIRMED`;
- `RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25`;
- `EXPERIMENTAL_METRIC_IMPACT = NOT_DETERMINED`;
- `EXPERIMENTAL_REVIEW = REQUIRED`;
- `TRIGGER = EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`.

The recorded material finding is that `87044110` appears in `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, case `DA-EVAL-V02-00060`, `candidate_rank = 100`, using the description derived from the Decision 885 snapshot. `87045110` was not identified in that same flat Top-100 output.

Corrections C1–C6 are recorded in `article/reviews/0B05C_INTERNAL_REVIEW.md`. The following separation remains mandatory:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

### Editorial review of the corrective experimental gate

Subsequent experimental feedback keeps the gate open and concludes that bounded corrective numerical re-execution is required. The editorial review accepts that:

- drift and Chapter-87 scope overlap are confirmed;
- no EVAL-label or historical-ranking impact is observed from this finding;
- EV-03 has a real overlap and `EV03_METRIC_IMPACT = NOT_DETERMINED`;
- `EV04_METRIC_IMPACT = NOT_DETERMINED`;
- no full benchmark rebuild, split rebuild, or label remap is justified;
- any sensitivity analysis must fully preserve the original snapshot;
- downstream components should be reopened only upon demonstrated propagation.

Material correction pending: the current feedback limits re-execution to EV-03/EV-04, but an earlier experimental review had identified EV-05/D1a as potentially exposed through a direct dependency on `corpus_rag_v1_index.jsonl`. The current feedback does not document why D1a is removed from that scope. Therefore, before closure, the experimental AI must **include EV-05/D1a in the corrective sensitivity analysis or explicitly exclude it with sufficient traceable evidence**. This does not imply an automatic D1a rerun.

Verdict:

```text
0B05C_CORRECTIVE_EXPERIMENTAL_REVIEW = PASS_WITH_MATERIAL_CORRECTION
CORRECTIVE_GATE_SCOPING = INCOMPLETE
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED
EV05_D1A_STATUS = REQUIRES_EXPLICIT_INCLUSION_OR_EXCLUSION_JUSTIFICATION
DOWNSTREAM_REEXECUTION = CONDITIONAL_ON_PROPAGATION
CORRECTIVE_NUMERICAL_RERUN = REQUIRED
0B05C_CLOSURE = NOT_AUTHORIZED
```

### Current gate

`0B-05C CORRECTIVE_EXPERIMENTAL_REVIEWED / CORRECTIVE_NUMERICAL_RERUN_REQUIRED -> experimental AI completes the corrective numerical check and explicitly resolves EV-05/D1a -> final scientific/editorial review -> writing-AI correction/normalization if required -> express author approval -> freeze -> assess 0B-06 need`.

While 0B-05C remains open, no scientific-editor/writing-AI Master-Plan or 0A changes, retrospective replacement of the original normative snapshot, manuscript drafting, final novelty/gap declarations, 0B-06, 0C, or 0D are authorized.
