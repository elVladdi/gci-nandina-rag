# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito y reglas generales

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta mediante lotes temáticos controlados. Su finalidad es leer PDF completos, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable para 0C. Durante 0B no se redacta el manuscrito ni se declara novelty o gap definitivo.

Reglas gobernantes:

- corpus consolidado: `62` obras/documentos distintos, con acceso primario verificable `62/62`;
- solo se analizan los PDF del lote activo;
- lectura íntegra obligatoria;
- no inventar metadata, DOI, resultados, indexación o estado editorial;
- distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`;
- una afirmación secundaria no se convierte en hecho independiente sin verificar su fuente primaria;
- ausencia de group split documentado no demuestra leakage;
- no equiparar classification, candidate retrieval, evidence retrieval, reranking, explanation, auditability ni correctness;
- `SUPPORTS_CANDIDATE` significa solo supervivencia provisional dentro del lote, nunca novelty;
- las referencias heredadas conservan elegibilidad aunque sean antiguas/proceedings/preprints; nuevas referencias académicas se rigen por `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 2. Bloques cerrados

- `0B-01`: **`APPROVED / FROZEN`** — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02`: **`APPROVED / FROZEN`** — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A`: **`APPROVED / FROZEN`** — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B`: **`APPROVED / FROZEN`** — `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.

Después de 0B-03B permanecen provisionalmente F1–F5 en formas estrechas/metodológicas; G6 está eliminado como candidato a gap y G7 absorbido en F2. Ninguno constituye novelty ni gap definitivo.

### 3. 0B-04 — Fundamentos de Information Retrieval y RAG

Alcance formal:
`article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-04A — Fundamentos de ranking y recuperación de información

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt ejecutado:
`article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.

Revisión interna:
`article/reviews/0B04A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`.

PDF analizados:

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Hallazgos gobernantes tras auditoría primaria:

- BM25 = `SPARSE_LEXICAL_RETRIEVAL / CANDIDATE_GENERATION / RANKING`; score de ranking, no probabilidad calibrada de correctness.
- SBERT = `SENTENCE_EMBEDDING / SEMANTIC_REPRESENTATION`; habilita semantic search, pero candidate search/indexing debe especificarse separadamente.
- DPR = `DENSE_BIENCODER_RETRIEVAL / INDEXED_SIMILARITY_SEARCH / CANDIDATE_GENERATION`; FAISS es infraestructura de búsqueda.
- ColBERT = `LATE_INTERACTION_RETRIEVAL` con modos distintos de `RERANKING` y `FULL_RETRIEVAL`.
- HNSW = `ANN_INDEX_SEARCH / INDEX_ACCELERATION`, no modelo semántico; metadata editorial final `REVIEW_REQUIRED_FOR_FINAL_CITATION` en la copia suministrada.
- Nogueira–Cho = `CROSS_ENCODER_RERANKING` de segunda etapa sobre BM25 Top-1000; la copia primaria es arXiv v5 del 14-Apr-2020.
- ANN recall, Top-k retrieval accuracy, MRR/MAP, STS Spearman y classification metrics no se mezclan ni ordenan globalmente.
- Los resultados fundacionales de dense retrieval no reinterpretan el D1a experimental, que permanece específico de la implementación exploratoria congelada.

Correcciones C1–C8 están registradas y pueden integrarse editorialmente después de aprobación del autor. No se requiere rerun de la IA de redacción ni revisión experimental.

#### 0B-04B — Fundamentos de RAG, query transformation y grounding

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Se abrirá solo después de aprobación y freeze de 0B-04A. El lote previsto sigue sujeto a confirmación final y no existe prompt ejecutable todavía.

#### Trabajos reservados para uso dirigido

Permanecen `RESERVED_FOR_DIRECTED_USE`: SimCSE, query expansion by prompting LLMs, ExtractGPT, product-information extraction with ChatGPT y LLM product-attribute extraction/normalization. No se abre 0B-04C por defecto.

### 4. 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Estado: `NOT_STARTED`.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`. Solo se abrirá si, después del corpus heredado relevante, persiste un vacío bibliográfico real y bajo las reglas de `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 6. Gate

Gate general:

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

Gate activo:

`0B-04A INTERNAL_REVIEW_COMPLETE -> aprobación expresa del autor -> integrar C1–C8 -> freeze -> definir/abrir 0B-04B`.

La IA experimental no es revisora bibliográfica obligatoria. Se incorpora solo si una interpretación bibliográfica modifica hechos/claims experimentales o restricciones bajo su autoridad.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A y 0B-03B: `APPROVED / FROZEN`.
- Bloque activo: `0B-04A`.
- 0B-04A: `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- 0B-04B: `NOT_STARTED / CLOSED_BY_GATE`.
- 0B-05/0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and rules

Phase `0B — Critical literature map and taxonomy` uses controlled thematic batches with full-PDF and claim-level verification. No manuscript drafting, final novelty, or definitive gap is allowed during 0B. The inherited corpus contains 62 distinct works/documents with primary access `62/62`.

### 2. Closed blocks

0B-01, 0B-02, 0B-03A, and 0B-03B are **`APPROVED / FROZEN`**. F1–F5 remain provisional after 0B-03B; G6 is eliminated as a gap candidate and G7 is merged into F2.

### 3. 0B-04 — IR/RAG foundations

#### 0B-04A

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Internal review: `article/reviews/0B04A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, no material errors.

Primary verification establishes the governing taxonomy: BM25 = sparse lexical retrieval/ranking; SBERT = sentence embedding/semantic representation with search/indexing specified separately; DPR = dense bi-encoder indexed retrieval; ColBERT = late-interaction retrieval with reranking and full-retrieval modes; HNSW = ANN index/search acceleration with unresolved final publication metadata in the supplied manuscript; and Nogueira–Cho = second-stage cross-encoder reranking over BM25 candidates. Heterogeneous IR/ANN/STS/classification metrics are non-interchangeable, and foundational dense-retrieval results do not reinterpret the project's frozen D1a result.

C1–C8 may be integrated after express author approval. No drafting-AI rerun or experimental-AI review is required.

#### 0B-04B

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It opens only after 0B-04A author approval and freeze. No executable prompt exists yet.

Reserved IR/product-processing works remain `RESERVED_FOR_DIRECTED_USE` and no 0B-04C opens by default.

### 4. Later blocks and gate

0B-05 and 0B-06 remain not started. The active gate is `0B-04A INTERNAL_REVIEW_COMPLETE -> express author approval -> integrate C1-C8 -> freeze -> define/open 0B-04B`.

0C remains blocked until 0B closes; 0D remains blocked until 0C closes; target journal remains pending until 0D.
