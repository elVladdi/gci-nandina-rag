# 0B-04 — Alcance y plan de lotes de fundamentos IR/RAG / IR-RAG foundations scope and batch plan

## Español

### 1. Propósito

`0B-04 — Fundamentos de Information Retrieval y RAG` no es una revisión general de IR ni una búsqueda de novelty. Su función es establecer el fundamento metodológico mínimo y suficiente para describir con precisión las decisiones del artículo relacionadas con ranking léxico BM25, representación semántica/dense retrieval, late interaction, reranking, ANN/indexación, RAG, query transformation y grounding/evidentiality.

El bloque debe impedir errores de categoría como `embedding = retriever`, `HNSW = semantic model`, `reranker = candidate generator`, `RAG = cualquier uso de documentos`, o `retrieval metric = classification accuracy`.

### 2. Criterio de selección

El corpus heredado contiene más trabajos IR/RAG de los necesarios. Solo se incorporan aquellos que respaldan una decisión metodológica concreta o una distinción necesaria para interpretar el sistema experimental. Por volumen y heterogeneidad, 0B-04 se divide en dos sub-lotes principales.

### 3. 0B-04A — Fundamentos de ranking y recuperación

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt ejecutado:
`article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.

Revisión interna:
`article/reviews/0B04A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`.

Revisión experimental: `NOT_REQUIRED`.

PDF analizados:

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Hallazgos gobernantes tras revisión primaria:

- BM25 es lexical term-weighting/scoring/ranking dentro del Probabilistic Relevance Framework; su score no es probabilidad calibrada de corrección.
- SBERT produce representaciones semánticas independientes y habilita semantic search, pero el candidate search/indexing a escala debe especificarse separadamente del encoder.
- DPR constituye dense bi-encoder retrieval; FAISS es infraestructura de similarity/index search y la búsqueda indexada materializa el Top-k.
- ColBERT tiene dos modos metodológicamente distintos: `re-ranking` y `full/end-to-end retrieval`.
- HNSW es `ANN_INDEX_SEARCH / INDEX_ACCELERATION`, no modelo semántico; la metadata editorial final de la copia suministrada queda `REVIEW_REQUIRED_FOR_FINAL_CITATION`.
- Nogueira–Cho es `CROSS_ENCODER_RERANKING`: BM25 genera Top-1000 y BERT reordena. La copia primaria visible es arXiv v5, 14-Apr-2020; el `27%` del abstract es mejora relativa.
- ANN recall, Top-k retrieval accuracy, MRR/MAP, STS Spearman y classification metrics no son métricas intercambiables.
- Los resultados fundacionales de dense retrieval no reinterpretan el D1a experimental; D1a sigue siendo específico de la implementación exploratoria congelada.

Correcciones C1–C8 para el eventual freeze están registradas en la revisión interna. No se requiere rerun de la IA de redacción.

### 4. 0B-04B — Fundamentos de RAG, query transformation y grounding

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá abrirse después de aprobación y freeze de 0B-04A.

Lote previsto, sujeto a confirmación final antes de abrirlo:

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

Gate vigente:

`0B-04A INTERNAL_REVIEW_COMPLETE -> aprobación expresa del autor -> integrar C1–C8 -> freeze -> definir/abrir 0B-04B`.

No se abre 0B-04B hasta cerrar 0B-04A. La IA experimental solo interviene si una interpretación bibliográfica modifica o amenaza un hecho/claim experimental congelado o una restricción bajo su autoridad; no ocurrió en la revisión 0B-04A.

### 8. Prohibiciones

Hasta cerrar 0B-04A:

- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva;
- no comparar benchmarks heterogéneos como superioridad global;
- no modificar Plan Maestro ni 0A;
- no reabrir G6/G7;
- no crear/ejecutar 0B-04B;
- no usar literatura fundacional para reinterpretar resultados experimentales congelados fuera de su alcance.

---

## English

### 1. Purpose

`0B-04 — Information Retrieval and RAG foundations` provides the minimum sufficient methodological basis for lexical BM25 ranking, semantic/dense representation and retrieval, late interaction, reranking, ANN indexing/search, RAG, query transformation, and grounding/evidentiality. It is not a general IR review or novelty-search stage.

### 2. 0B-04A — Ranking and retrieval foundations

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Internal review: `article/reviews/0B04A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, no material errors. Experimental review is not required.

Primary verification confirms: BM25 is lexical ranking within PRF rather than a calibrated correctness probability; SBERT supplies semantic representation while scalable candidate search/indexing must be specified separately; DPR is indexed dense bi-encoder retrieval; ColBERT has distinct reranking and full-retrieval modes; HNSW is ANN/index-search infrastructure and its supplied manuscript has unresolved final publication metadata; Nogueira–Cho is second-stage cross-encoder reranking over BM25 candidates; heterogeneous IR/ANN/STS/classification metrics are not interchangeable; and foundational dense-retrieval results do not reinterpret the project's frozen D1a result.

C1–C8 are recorded in the internal review. No drafting-AI rerun is required.

### 3. 0B-04B — RAG/query transformation/grounding foundations

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may open only after author approval and freeze of 0B-04A. The planned six-paper set remains provisional and no executable prompt has been created.

### 4. Reserved works

SimCSE, query expansion, ExtractGPT, product-information extraction, and product-attribute extraction/normalization remain `RESERVED_FOR_DIRECTED_USE` and will be analyzed only if a concrete methodological need emerges.

### 5. Gap-candidate governance

0B-04A does not alter the post-0B-03B status of F1–F5. It only constrains terminology and methodological interpretation. G6 remains eliminated and G7 remains merged into F2.

### 6. Gate

`0B-04A INTERNAL_REVIEW_COMPLETE -> express author approval -> integrate C1-C8 -> freeze -> define/open 0B-04B`.

Until then, 0B-04B and later phases remain closed. Experimental-AI review was not required because no frozen experimental fact/claim or Master-Plan rule was modified.
