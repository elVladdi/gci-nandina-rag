# 0B-04 — Alcance y plan de lotes de fundamentos IR/RAG / IR-RAG foundations scope and batch plan

## Español

### 1. Propósito

`0B-04 — Fundamentos de Information Retrieval y RAG` no es una revisión general de IR ni una búsqueda de novelty. Su función es establecer el fundamento metodológico mínimo y suficiente para describir con precisión las decisiones del artículo relacionadas con:

- ranking léxico BM25;
- representación semántica y dense retrieval;
- late interaction;
- reranking;
- búsqueda ANN/indexación;
- retrieval-augmented generation;
- query transformation/expansion cuando sea metodológicamente pertinente;
- grounding/evidentiality de generación.

El bloque debe impedir confusiones frecuentes como `embedding = retriever`, `HNSW = semantic model`, `reranker = candidate generator`, `RAG = cualquier uso de documentos`, o `retrieval metric = classification accuracy`.

### 2. Criterio de selección

El corpus heredado contiene más trabajos de IR/RAG de los necesarios para el artículo. 0B-04 no analizará automáticamente todos. Solo se incorporan aquellos que respaldan una decisión metodológica concreta o una distinción necesaria para interpretar el sistema experimental.

Por volumen y para conservar lectura íntegra/auditoría primaria, 0B-04 se divide en dos sub-lotes principales.

### 3. 0B-04A — Fundamentos de ranking y recuperación

Estado: **`READY_FOR_DRAFTING`**.

Prompt:
`article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`

PDF asignados:

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Objetivo: reconstruir con exactitud la función de cada componente en el pipeline y distinguir `representation`, `candidate generation`, `ANN/index search`, `reranking` y `final ranking`.

Preguntas gobernantes:

- ¿Qué fundamento respalda BM25 y qué no demuestra?
- ¿Qué distingue sentence embeddings, dense bi-encoders, late interaction y cross-encoder reranking?
- ¿Qué hace HNSW y qué no hace?
- ¿Qué candidatos presupone un reranker?
- ¿Qué métricas y resultados son comparables solo dentro de cada paper/benchmark?
- ¿Qué fundamentos son pertinentes al sistema actual y cuáles solo sirven de contraste?

### 4. 0B-04B — Fundamentos de RAG, query transformation y grounding

Estado: `NOT_STARTED`.

Se abrirá únicamente después del cierre de 0B-04A.

Lote previsto, sujeto a confirmación final antes de abrirlo:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM: Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering.pdf`
4. `Query2doc.pdf`
5. `Query Rewriting for Retrieval-Augmented LLMs.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

Objetivo previsto: distinguir retrieval usado para condicionar generación, retrieval-augmented pretraining, fusion/aggregation de pasajes, query rewriting/expansion y mecanismos de grounding/evidentiality. Este sub-lote deberá analizar de forma explícita por qué el RAG fundacional no equivale automáticamente al contrato del proyecto `Top-k histórico fijo -> evidencia normativa -> LLM explicativo no reordenador`.

No se crea todavía el prompt ejecutable de 0B-04B para evitar abrirlo antes del gate.

### 5. Trabajos IR/product-processing reservados

Los siguientes trabajos del corpus permanecen disponibles, pero no se incluyen automáticamente en 0B-04A/04B:

- `SimCSE.pdf`;
- `Query Expansion by Prompting Large Language Models.pdf`;
- `ExtractGPT.pdf`;
- `Product Information Extraction using ChatGPT.pdf`;
- `Using LLMs for the Extraction and Normalization of Product Attribute Values.pdf`.

Estado operativo: `RESERVED_FOR_DIRECTED_USE`.

Podrán incorporarse posteriormente solo si una decisión metodológica concreta sobre normalización, atributos, query expansion o representación requiere evidencia adicional. No se abre un 0B-04C por defecto.

### 6. Relación con los candidatos de gap

0B-04 es principalmente metodológico. Los papers fundacionales no deben usarse para afirmar ausencia de una arquitectura aduanera específica.

Después de 0B-03B continúan provisionalmente:

- F1: ranking histórico fijado por precedentes + normativa posterior no reordenadora;
- F2: generador exclusivamente explicativo sobre Top-k externo e inmutable, sin feedback clasificatorio;
- F3: control de dependencia por unidad/grupo cuando aplica;
- F4: rendimiento predictivo/retrieval/path validity/evidence grounding ≠ corrección sustantiva adjudicada;
- F5: evaluación formal y separada de auditabilidad documental por salida.

G6 permanece eliminado como gap candidate y G7 absorbido en F2.

En 0B-04A los papers se relacionarán con F1–F5 mediante etiquetas metodológicas, no mediante supuesta evidencia de novelty.

### 7. Gate

`0B-04A READY_FOR_DRAFTING -> IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze -> definir/abrir 0B-04B`.

No se abre 0B-04B hasta cerrar 0B-04A.

La IA experimental solo interviene si una interpretación bibliográfica amenaza o modifica un hecho/claim experimental congelado o una restricción metodológica bajo su autoridad.

### 8. Prohibiciones

Durante 0B-04:

- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva salvo apertura posterior explícita de 0B-06;
- no comparar métricas entre benchmarks heterogéneos como superioridad global;
- no modificar el Plan Maestro ni 0A;
- no reabrir G6/G7;
- no convertir referencias fundacionales en evidencia de ausencia de prior art aduanero.

---

## English

### 1. Purpose

`0B-04 — Information Retrieval and RAG foundations` is not a general IR review or a novelty-search stage. It provides the minimum sufficient methodological basis for lexical BM25 ranking, dense representation/retrieval, late interaction, reranking, ANN indexing/search, RAG, query transformation when relevant, and generation grounding/evidentiality.

Its purpose includes preventing category errors such as `embedding = retriever`, `HNSW = semantic model`, `reranker = candidate generator`, `RAG = any use of documents`, or `retrieval metric = classification accuracy`.

### 2. Controlled selection

The inherited corpus contains more IR/RAG works than the article needs. 0B-04 will analyze only papers that support a concrete methodological decision or a necessary conceptual distinction.

### 3. 0B-04A — Ranking and retrieval foundations

Status: **`READY_FOR_DRAFTING`**.

Prompt: `article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.

The six assigned PDFs are the BM25, Sentence-BERT, DPR, ColBERT, HNSW, and BERT reranking works listed in the Spanish section.

The governing objective is to distinguish representation, candidate generation, ANN/index search, reranking, and final ranking and to establish what each paper can and cannot justify for the present article.

### 4. 0B-04B — RAG, query transformation, and grounding foundations

Status: `NOT_STARTED`.

It will open only after 0B-04A is frozen. The planned six-paper set includes RAG, REALM, Fusion-in-Decoder/passage retrieval with generative models, Query2doc, query rewriting for RAG, and evidentiality-guided generation. The executable prompt is intentionally not created yet.

### 5. Reserved works

SimCSE, query expansion, ExtractGPT, product-information extraction with ChatGPT, and LLM-based product-attribute extraction/normalization remain `RESERVED_FOR_DIRECTED_USE`. They may be analyzed later only if a concrete methodological need emerges; no 0B-04C opens by default.

### 6. Gap-candidate governance

0B-04 is primarily methodological. Foundational IR papers must not be treated as evidence that a customs-specific architecture is absent from prior art. F1–F5 remain provisional after 0B-03B; G6 remains eliminated and G7 remains merged into F2.

### 7. Gate

`0B-04A READY_FOR_DRAFTING -> drafting AI -> internal primary-PDF review -> correction if needed -> author approval -> freeze -> define/open 0B-04B`.

0B-04B cannot open before 0B-04A closes. Experimental-AI review is required only if literature interpretation changes frozen experimental facts/claims or methodological restrictions under its authority.

### 8. Prohibitions

No manuscript drafting, final novelty/gap claims, new literature search, cross-benchmark global superiority claims, Master-Plan/0A modification, reopening G6/G7, or using foundational-method papers as proof of missing customs prior art.