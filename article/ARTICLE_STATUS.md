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
- `0B-04A — Fundamentos de ranking y recuperación de información`: **`APPROVED / FROZEN`**.
- `0B-04B`: **`NOT_STARTED / CLOSED_BY_GATE`**.
- `0B-05`: `NOT_STARTED`.
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

### Candidatos provisionales después de 0B-03B

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **G6:** `ELIMINATED AS GAP CANDIDATE`; queda solo como principio de calidad del ground truth.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-04A no modifica estos estados; es un bloque fundacional que normaliza vocabulario y función de componentes IR.

### 0B-04A — cierre formal

```text
0B-04A = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = RECEIVED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Registros:

- Prompt: `article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.
- Revisión interna: `article/reviews/0B04A_INTERNAL_REVIEW.md`.
- Aprobación del autor: `article/reviews/0B04A_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

Hallazgos gobernantes congelados:

1. BM25 = lexical term-weighting/scoring/ranking dentro del Probabilistic Relevance Framework; su score no es probabilidad calibrada de relevancia/corrección.
2. SBERT = `SENTENCE_EMBEDDING / SEMANTIC_REPRESENTATION`; habilita semantic search, pero candidate search/indexing a escala se especifica separadamente.
3. DPR = `DENSE_BIENCODER_RETRIEVAL / INDEXED_SIMILARITY_SEARCH / CANDIDATE_GENERATION`; FAISS es infraestructura de búsqueda y la búsqueda indexada materializa el Top-k.
4. ColBERT conserva dos modos: `RERANKING` y `FULL_RETRIEVAL`.
5. HNSW = `ANN_INDEX_SEARCH / INDEX_ACCELERATION`, no modelo semántico; metadata editorial final de la copia suministrada = `REVIEW_REQUIRED_FOR_FINAL_CITATION`.
6. Nogueira–Cho = `CROSS_ENCODER_RERANKING` de segunda etapa sobre BM25 Top-1000; la copia visible es arXiv v5 de 2020 y el `27%` reportado es mejora relativa.
7. ANN recall, Top-k retrieval accuracy, MRR/MAP, STS Spearman y classification metrics no son intercambiables.
8. DPR/ColBERT/SBERT fundacionales no reinterpretan D1a: D1a permanece evidencia solo sobre la implementación densa exploratoria congelada.

Distinción metodológica central congelada:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

Las funciones pueden estar operacionalmente acopladas, pero no son sinónimos.

### Gate siguiente

`0B-04B — Fundamentos de RAG, query transformation y grounding` permanece **`NOT_STARTED / CLOSED_BY_GATE`**.

El freeze de 0B-04A **no** abre 0B-04B automáticamente. Su lote y prompt ejecutable deberán confirmarse y abrirse en un cambio posterior explícito.

Mientras 0B permanezca abierto no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad global de métodos;
- abrir 0C;
- modificar 0A o el Plan Maestro;
- reabrir G6/G7;
- convertir claims secundarios en hechos sin verificar la fuente primaria.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A is **`CLOSED / APPROVED`**; 0A-01 and 0A-02 are frozen.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, 0B-03B, and 0B-04A are **`APPROVED / FROZEN`**.
- 0B-04B is **`NOT_STARTED / CLOSED_BY_GATE`**; 0B-05 and 0B-06 are not started.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D.
- Manuscript drafting has not started.

### Governing ground truth

Frozen 0A documentary and experimental artifacts remain authoritative. Literature review cannot modify the Master Plan; exclusive Master-Plan authority remains with the experimental workflow.

### 0B-04A formal closure

```text
0B-04A = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = RECEIVED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Canonical artifact: `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`; review and author-approval records are stored under `article/reviews/`.

The frozen methodological map is: BM25 = sparse lexical retrieval/ranking; SBERT = semantic sentence representation with scalable candidate search/indexing specified separately; DPR = indexed dense bi-encoder retrieval; ColBERT = late-interaction retrieval with reranking and full-retrieval modes; HNSW = ANN index/search acceleration rather than a semantic model; and Nogueira–Cho = second-stage cross-encoder reranking over BM25 candidates. Heterogeneous ANN/IR/STS/classification metrics remain non-interchangeable, and foundational dense-retrieval results do not reinterpret the project's frozen D1a result beyond that specific exploratory implementation.

The governing functional distinction is `QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`, while recognizing that functions can be operationally coupled.

0B-04A does not alter F1–F5's post-0B-03B status; G6 remains eliminated and G7 remains merged into F2.

### Next gate

0B-04B remains `NOT_STARTED / CLOSED_BY_GATE`. The 0B-04A freeze does not open it automatically; its final batch and executable prompt require a later explicit definition/opening change. Manuscript drafting, final novelty/gap claims, 0C opening, and Master-Plan modification remain prohibited while 0B is open.
