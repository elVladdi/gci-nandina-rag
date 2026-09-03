# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0A-01`: **`APPROVED / FROZEN`**.
- `0A-02`: **`APPROVED / FROZEN`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**.
- `0B-04A`: **`APPROVED / FROZEN`**.
- `0B-04B`: **`APPROVED / FROZEN`**.
- `0B-05`: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.
- `0B-06`: `NOT_STARTED`.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Corpus consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth gobernante

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

La revisión bibliográfica no modifica el Plan Maestro ni el ground truth 0A. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro.

### Bloques 0B cerrados

- `0B-01 = APPROVED / FROZEN` — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02 = APPROVED / FROZEN` — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A = APPROVED / FROZEN` — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B = APPROVED / FROZEN` — `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.
- `0B-04A = APPROVED / FROZEN` — `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.
- `0B-04B = APPROVED / FROZEN` — `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.

### Candidatos provisionales

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **G6:** `ELIMINATED AS GAP CANDIDATE`; queda solo como principio de calidad del ground truth.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-04A y 0B-04B son fundacionales y no modifican estos estados; solo fijan vocabulario y fronteras metodológicas.

### 0B-04 — cierre formal

#### 0B-04A

```text
0B-04A = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

Artefacto canónico:
`article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

Distinción congelada:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

#### 0B-04B

```text
0B-04B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Registros:

- Prompt: `article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.
- Revisión interna: `article/reviews/0B04B_INTERNAL_REVIEW.md`.
- Aprobación del autor: `article/reviews/0B04B_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.

Distinciones congeladas:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Normalizaciones C1–C13 integradas: discrepancia Lewis `17%`/Tabla-4 `11.7%`; RAG-Token sin nuevo retrieval por token; REALM como retrieval-augmented pretraining/span-based Open-QA; FiD fusion sin attribution; Query2doc/query rewriting como transformaciones upstream; resultados OOD y false-claim risk preservados; Asai et al. gobernado por cinco datasets y chequeo humano `95%/96%` limitado a validación de labels; provenance/grounding/evidentiality/auditability/legal correctness permanecen separados; benchmarks no se transfieren como métricas HS/NANDINA.

Contrato del piloto usado únicamente como frontera comparativa:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

### Gate siguiente

`0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa` queda **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

El freeze de 0B-04B no abre automáticamente 0B-05. Corresponde definir su alcance, lote y prompt mediante un cambio posterior explícito.

Mientras 0B permanezca abierto no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty o gap definitivo;
- abrir 0C;
- modificar 0A o el Plan Maestro;
- reabrir G6/G7;
- buscar literatura nueva salvo apertura explícita de 0B-06;
- convertir claims secundarios en hechos sin verificar la fuente primaria.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A is **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, and 0B-04B are **`APPROVED / FROZEN`**.
- 0B-05 is **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**; 0B-06 is not started.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governing ground truth

Frozen 0A documentary and experimental artifacts remain authoritative. Literature review cannot modify the Master Plan; exclusive Master-Plan authority remains with the experimental workflow.

### Provisional candidates

F1–F5 remain provisional in narrowed/methodological forms; G6 remains eliminated and G7 remains merged into F2. 0B-04A/0B-04B are foundational and do not change those literature statuses.

### 0B-04 closure

0B-04A is approved/frozen and established `QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

0B-04B is now approved/frozen. Governing records are the prompt, internal review, author approval, and canonical artifact `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.

Frozen distinctions:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

C1–C13 are integrated, including the Lewis `17%`/Table-4 `11.7%` discrepancy, no per-token retrieval in RAG-Token, REALM's retrieval-augmented-pretraining/span-based Open-QA characterization, the FiD fusion/attribution distinction, upstream Query2doc/query rewriting causality, preservation of mixed OOD and false-pseudo-document risks, Asai's five-dataset ground truth and limited `95%/96%` label-validation protocol, and strict separation of provenance/grounding/evidentiality/auditability/legal correctness. Benchmark results do not transfer as HS/NANDINA metrics.

The pilot contract remains only a comparison boundary: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

### Next gate

0B-05 is now `NOT_STARTED / ELIGIBLE_FOR_DEFINITION`. The 0B-04B freeze does not automatically open it; its scope, batch, and executable prompt require a later explicit definition/opening change.

Manuscript drafting, final novelty/gap claims, 0C opening, Master-Plan modification, reopening G6/G7, and new-literature search outside an explicitly opened 0B-06 remain prohibited while 0B is open.
