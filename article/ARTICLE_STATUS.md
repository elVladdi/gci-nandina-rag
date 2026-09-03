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
- Estado de `0B-04A`: **`READY_FOR_DRAFTING`**.
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

### 0B-04 — apertura formal

Alcance controlado:

`article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`

0B-04 se divide en `0B-04A` y `0B-04B` para conservar lectura completa, distinciones metodológicas y auditoría primaria.

#### 0B-04A — activo

Prompt:

`article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`

PDF asignados:

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Objetivo gobernante:

`QUERY/DOCUMENT REPRESENTATION -> CANDIDATE GENERATION -> ANN/INDEX SEARCH -> RERANKING -> FINAL RANKING`

El bloque debe distinguir con precisión BM25, sentence embeddings, dense bi-encoders, late interaction, cross-encoder reranking y ANN/HNSW. No está autorizado derivar superioridad global de un método, mezclar benchmarks heterogéneos ni usar papers fundacionales como evidencia de ausencia de prior art aduanero.

F1–F5 se evaluarán con etiquetas de **relevancia metodológica**, no como pressure test de novelty. G6/G7 no se reabren.

#### 0B-04B — previsto, no abierto

Estado: `NOT_STARTED`.

Se abrirá solo después de cerrar 0B-04A. El alcance previsto cubre RAG fundacional, REALM, passage retrieval + generation, Query2doc, query rewriting y evidentiality/grounding. No existe todavía prompt ejecutable.

### Gate vigente

```text
0B-04A READY_FOR_DRAFTING
-> IA de redacción
-> revisión científica/editorial interna contra los seis PDF primarios
-> corrección si aplica
-> aprobación expresa del autor
-> freeze 0B-04A
-> definir/abrir 0B-04B
```

La IA experimental solo se incorpora si una interpretación bibliográfica afecta directamente hechos/claims experimentales o restricciones metodológicas bajo su autoridad.

### Prohibiciones vigentes

Durante 0B-04A no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad general de métodos;
- usar otros PDF del corpus;
- buscar literatura nueva;
- modificar 0A o el Plan Maestro;
- reabrir G6/G7;
- abrir 0B-04B, 0B-05, 0B-06 o 0C antes del gate correspondiente.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**; 0A-01 and 0A-02 are **`APPROVED / FROZEN`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, and 0B-03B are **`APPROVED / FROZEN`**.
- Active block: **`0B-04A — Ranking and information-retrieval foundations`**.
- 0B-04A status: **`READY_FOR_DRAFTING`**.
- 0B-04B, 0B-05, and 0B-06: `NOT_STARTED`.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D.
- Manuscript drafting has not started.

### Governing ground truth

Frozen 0A documentary and experimental artifacts remain authoritative. Literature review cannot modify the Master Plan; exclusive Master-Plan authority remains with the experimental workflow.

### Provisional candidates after 0B-03B

F1–F5 remain provisional in narrowed/methodological forms; G6 is eliminated as a gap candidate and G7 is merged into F2. None establishes novelty or a final gap.

### 0B-04 formal opening

Controlled scope: `article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

0B-04 is split into 0B-04A and 0B-04B. The active 0B-04A prompt is `article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md` and covers only the six BM25/SBERT/DPR/ColBERT/HNSW/BERT-reranking papers listed in the Spanish section.

Its governing pipeline is `QUERY/DOCUMENT REPRESENTATION -> CANDIDATE GENERATION -> ANN/INDEX SEARCH -> RERANKING -> FINAL RANKING`. The block must distinguish retrieval representations, indexing/search, and reranking and must not infer global method superiority or missing customs prior art from heterogeneous foundational benchmarks.

0B-04B remains `NOT_STARTED` and will cover RAG/query transformation/grounding only after 0B-04A is frozen.

### Gate

`0B-04A READY_FOR_DRAFTING -> drafting AI -> internal primary-PDF review -> correction if needed -> express author approval -> freeze -> define/open 0B-04B`.

Experimental-AI review is required only if a literature interpretation affects frozen experimental facts/claims or methodological restrictions under its authority.