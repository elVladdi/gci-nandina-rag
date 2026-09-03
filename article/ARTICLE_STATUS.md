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
- Bloque activo: **`0B-04A — Fundamentos de ranking y recuperación de información`**.
- Estado de `0B-04A`: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Dictamen interno: **`PASS WITH MINOR CORRECTIONS`**.
- Errores materiales: `0`.
- Revisión experimental: `NOT_REQUIRED`.
- Freeze de 0B-04A: `NOT_YET_AUTHORIZED`.
- `0B-04B`: `NOT_STARTED`.
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

### Candidatos provisionales después de 0B-03B

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **G6:** `ELIMINATED AS GAP CANDIDATE`; queda solo como principio de calidad del ground truth.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-04A no cambia estos estados; es un bloque fundacional que normaliza vocabulario y función de componentes IR.

### 0B-04A — revisión interna completada

Prompt ejecutado:

`article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`

Revisión interna:

`article/reviews/0B04A_INTERNAL_REVIEW.md`

Estado formal:

```text
0B-04A = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE = NOT_YET_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Los seis PDF asignados fueron verificados como fuentes primarias:

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Hallazgos gobernantes para el eventual freeze:

1. BM25 = lexical term-weighting/scoring/ranking dentro del PRF; su score no es una probabilidad calibrada de relevancia o corrección arancelaria.
2. SBERT = representación semántica independiente que habilita semantic search; un pipeline a escala debe especificar por separado candidate search/indexing.
3. DPR = dense bi-encoder retrieval con indexed similarity search; FAISS es infraestructura de búsqueda y la búsqueda indexada materializa el Top-k.
4. ColBERT debe conservar dos modos distintos: reranking y full/end-to-end retrieval.
5. HNSW = ANN/index search sobre representaciones preexistentes; no semantic model. La metadata editorial final de la copia suministrada queda `REVIEW_REQUIRED_FOR_FINAL_CITATION`.
6. Nogueira–Cho = cross-encoder reranking de segunda etapa sobre BM25 Top-1000; la copia primaria disponible es arXiv v5 del 14-Apr-2020 y el `27%` del abstract es mejora relativa, no puntos porcentuales.
7. ANN recall, Top-k retrieval accuracy, MRR/MAP, STS Spearman y classification metrics no son intercambiables.
8. Los resultados fundacionales de dense retrieval no reinterpretan el D1a experimental: D1a sigue describiendo únicamente esa implementación exploratoria específica.

Taxonomía metodológica resultante:

- BM25: `SPARSE_LEXICAL_RETRIEVAL / CANDIDATE_GENERATION / RANKING`.
- SBERT: `SENTENCE_EMBEDDING / SEMANTIC_REPRESENTATION`.
- DPR: `DENSE_BIENCODER_RETRIEVAL / INDEXED_SIMILARITY_SEARCH / CANDIDATE_GENERATION`.
- ColBERT: `LATE_INTERACTION_RETRIEVAL`, con `RERANKING` y `FULL_RETRIEVAL`.
- HNSW: `ANN_INDEX_SEARCH / INDEX_ACCELERATION`.
- BERT passage reranker: `CROSS_ENCODER_RERANKING`.

### Gate vigente

```text
0B-04A revisión interna [COMPLETADA]
-> aprobación expresa del autor [PENDIENTE]
-> integrar C1–C8 y crear freeze canónico
-> definir/abrir 0B-04B
```

No se requiere nueva ejecución completa por la IA de redacción. No se requiere revisión de la IA experimental porque no se modifica ningún hecho/claim experimental congelado ni el Plan Maestro.

Hasta aprobación expresa del autor no está autorizado:

- congelar 0B-04A;
- crear/abrir el prompt ejecutable de 0B-04B;
- abrir 0B-05/0B-06/0C;
- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad global de métodos;
- modificar 0A o el Plan Maestro.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A is **`CLOSED / APPROVED`**; 0A-01 and 0A-02 are frozen.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, and 0B-03B are **`APPROVED / FROZEN`**.
- Active block: **`0B-04A — Ranking and information-retrieval foundations`**.
- 0B-04A status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**; material errors `0`.
- Experimental review: `NOT_REQUIRED`.
- Freeze: `NOT_YET_AUTHORIZED`.
- 0B-04B, 0B-05, and 0B-06 remain `NOT_STARTED`.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D.
- Manuscript drafting has not started.

### 0B-04A internal review

The six assigned primary PDFs were independently verified. Review record: `article/reviews/0B04A_INTERNAL_REVIEW.md`.

The governing methodological conclusions are: BM25 is lexical scoring/ranking within the probabilistic relevance framework rather than a calibrated correctness probability; SBERT provides independently computable semantic representations but scalable candidate search/indexing must be specified separately; DPR is dense bi-encoder indexed retrieval; ColBERT has distinct reranking and full-retrieval modes; HNSW is ANN/index-search infrastructure rather than a semantic model; and Nogueira–Cho implement second-stage cross-encoder reranking over BM25 candidates.

HNSW's supplied manuscript has unresolved final publication metadata and is `REVIEW_REQUIRED_FOR_FINAL_CITATION` for those fields. ANN recall, retrieval Top-k accuracy, MRR/MAP, STS Spearman, and classification metrics remain non-interchangeable. Foundational dense-retrieval results do not reinterpret the project's frozen D1a result, which remains specific to that exploratory implementation.

0B-04A does not change F1–F5's provisional post-0B-03B status; it constrains terminology and method interpretation. G6 remains eliminated and G7 remains merged into F2.

### Gate

`internal review complete -> express author approval -> integrate C1-C8 -> canonical freeze -> define/open 0B-04B`.

No drafting-AI rerun or experimental-AI review is required. Until express author approval, 0B-04A cannot be frozen and 0B-04B/later phases remain closed.
