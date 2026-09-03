# 0B-04 — Alcance y plan de lotes de fundamentos IR/RAG / IR-RAG foundations scope and batch plan

## Español

### 1. Propósito

`0B-04 — Fundamentos de Information Retrieval y RAG` no es una revisión general de IR ni una búsqueda de novelty. Su función es establecer el fundamento metodológico mínimo y suficiente para describir con precisión las decisiones del artículo relacionadas con ranking léxico BM25, representación semántica/dense retrieval, late interaction, reranking, ANN/indexación, RAG, query transformation y grounding/evidentiality.

El bloque debe impedir errores de categoría como `embedding = retriever`, `HNSW = semantic model`, `reranker = candidate generator`, `RAG = cualquier uso de documentos`, o `retrieval metric = classification accuracy`.

### 2. Criterio de selección

El corpus heredado contiene más trabajos IR/RAG de los necesarios. Solo se incorporan aquellos que respaldan una decisión metodológica concreta o una distinción necesaria para interpretar el sistema experimental. Por volumen y heterogeneidad, 0B-04 se divide en dos sub-lotes principales.

### 3. 0B-04A — Fundamentos de ranking y recuperación

Estado: **`APPROVED / FROZEN`**.

Prompt ejecutado:
`article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.

Revisión interna:
`article/reviews/0B04A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`.

Aprobación del autor:
`article/reviews/0B04A_AUTHOR_APPROVAL.md` — aprobación expresa recibida el `2026-09-03`.

Artefacto canónico:
`article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

Revisión experimental: `NOT_REQUIRED`.

PDF analizados:

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Hallazgos congelados:

- BM25 = lexical term-weighting/scoring/ranking dentro del Probabilistic Relevance Framework; su score no es probabilidad calibrada de corrección.
- SBERT = `SENTENCE_EMBEDDING / SEMANTIC_REPRESENTATION`; habilita semantic search, pero candidate search/indexing a escala se especifica separadamente del encoder.
- DPR = `DENSE_BIENCODER_RETRIEVAL / INDEXED_SIMILARITY_SEARCH / CANDIDATE_GENERATION`; FAISS es infraestructura de búsqueda y la búsqueda indexada materializa el Top-k.
- ColBERT conserva dos modos metodológicamente distintos: `RERANKING` y `FULL_RETRIEVAL`.
- HNSW = `ANN_INDEX_SEARCH / INDEX_ACCELERATION`, no modelo semántico; la metadata editorial final de la copia suministrada queda `REVIEW_REQUIRED_FOR_FINAL_CITATION`.
- Nogueira–Cho = `CROSS_ENCODER_RERANKING` de segunda etapa sobre BM25 Top-1000; la copia primaria visible es arXiv v5 de 2020 y el `27%` del abstract es mejora relativa.
- ANN recall, Top-k retrieval accuracy, MRR/MAP, STS Spearman y classification metrics no son intercambiables.
- Los resultados fundacionales de DPR/ColBERT/SBERT no reinterpretan el D1a experimental; D1a sigue siendo específico de la implementación densa exploratoria congelada.

Distinción central congelada:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

Las funciones pueden estar operacionalmente acopladas; no implican una correspondencia uno-a-uno con algoritmos independientes.

### 4. 0B-04B — Fundamentos de RAG, query transformation y grounding

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

0B-04A ya está congelado, por lo que 0B-04B queda **elegible para definición posterior**, pero no está abierto automáticamente. Su lote definitivo y prompt ejecutable requieren un cambio explícito posterior.

Lote previsto, sujeto a confirmación antes de apertura:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM: Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering.pdf`
4. `Query2doc.pdf`
5. `Query Rewriting for Retrieval-Augmented LLMs.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

Objetivo previsto: distinguir retrieval usado para condicionar generación, retrieval-augmented pretraining, fusión/agregación de pasajes, query rewriting/expansion y mecanismos de grounding/evidentiality. Debe analizar por qué RAG fundacional no equivale automáticamente al contrato `Top-k histórico fijo -> evidencia normativa -> LLM explicativo no reordenador`.

No existe todavía prompt ejecutable de 0B-04B.

### 5. Trabajos reservados

Permanecen `RESERVED_FOR_DIRECTED_USE`:

- `SimCSE.pdf`;
- `Query Expansion by Prompting Large Language Models.pdf`;
- `ExtractGPT.pdf`;
- `Product Information Extraction using ChatGPT.pdf`;
- `Using LLMs for the Extraction and Normalization of Product Attribute Values.pdf`.

Solo se incorporarán si una necesidad metodológica concreta sobre normalización, atributos, query expansion o representación lo exige. No se abre un 0B-04C por defecto.

### 6. Relación con candidatos de gap

0B-04 es principalmente metodológico. Los papers fundacionales no son evidencia de ausencia de una arquitectura aduanera específica.

Después de 0B-03B permanecen:

- F1: ranking histórico fijado por precedentes + normativa posterior no reordenadora;
- F2: generador exclusivamente explicativo sobre Top-k externo e inmutable, sin feedback clasificatorio;
- F3: control de dependencia por unidad/grupo cuando aplica;
- F4: rendimiento predictive/retrieval/path validity/evidence grounding ≠ corrección sustantiva adjudicada;
- F5: evaluación formal y separada de auditabilidad documental por salida.

G6 permanece eliminado y G7 absorbido en F2. 0B-04A no modifica estos estados; aporta vocabulario y distinciones metodológicas.

### 7. Gate

0B-04A completó el gate:

`IA de redacción -> revisión interna -> aprobación expresa del autor -> freeze`.

Siguiente gate potencial:

`definir lote final 0B-04B -> crear prompt ejecutable -> READY_FOR_DRAFTING -> IA de redacción -> revisión interna -> aprobación del autor -> freeze`.

La IA experimental solo interviene si una interpretación bibliográfica modifica o amenaza un hecho/claim experimental congelado o una restricción bajo su autoridad.

### 8. Prohibiciones vigentes

Mientras 0B permanezca abierto:

- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva salvo apertura explícita de 0B-06;
- no comparar benchmarks heterogéneos como superioridad global;
- no modificar Plan Maestro ni 0A;
- no reabrir G6/G7;
- no ejecutar 0B-04B hasta su apertura explícita;
- no usar literatura fundacional para reinterpretar resultados experimentales congelados fuera de su alcance.

---

## English

### 1. Purpose

`0B-04 — Information Retrieval and RAG foundations` provides the minimum sufficient methodological basis for lexical BM25 ranking, semantic/dense representation and retrieval, late interaction, reranking, ANN indexing/search, RAG, query transformation, and grounding/evidentiality. It is not a general IR review or novelty-search stage.

### 2. 0B-04A — Ranking and retrieval foundations

Status: **`APPROVED / FROZEN`**.

The governing records are the 0B-04A prompt, internal review, author approval, and canonical frozen artifact `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

The frozen method map is: BM25 = lexical ranking within PRF rather than a calibrated correctness probability; SBERT = sentence embedding/semantic representation with candidate search/indexing specified separately; DPR = indexed dense bi-encoder retrieval; ColBERT = late-interaction retrieval with reranking and full-retrieval modes; HNSW = ANN index/search infrastructure with unresolved final publication metadata in the supplied copy; and Nogueira–Cho = second-stage cross-encoder reranking over BM25 candidates. Heterogeneous IR/ANN/STS/classification metrics remain non-interchangeable, and foundational dense-retrieval results do not reinterpret the project's frozen D1a result.

The central distinction is `QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`, while recognizing that functions can be operationally coupled.

### 3. 0B-04B — RAG/query transformation/grounding foundations

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. Because 0B-04A is now frozen, 0B-04B is eligible for a later explicit definition, but it has not been opened automatically. The planned six-paper set remains provisional and no executable prompt exists yet.

### 4. Reserved works

SimCSE, query expansion, ExtractGPT, product-information extraction, and product-attribute extraction/normalization remain `RESERVED_FOR_DIRECTED_USE`.

### 5. Gap-candidate governance

0B-04A does not alter the post-0B-03B status of F1–F5. It constrains terminology and method interpretation only. G6 remains eliminated and G7 remains merged into F2.

### 6. Gate

0B-04A completed the normal gate: drafting AI -> internal review -> express author approval -> freeze. The next potential gate is: define the final 0B-04B batch -> create executable prompt -> READY_FOR_DRAFTING -> drafting AI -> internal review -> author approval -> freeze.

No manuscript drafting, final novelty/gap claims, new-literature search outside an explicitly opened 0B-06, Master-Plan modification, or 0B-04B execution is authorized until the corresponding gate is opened.
