# 0B-04A — Fundamentos de ranking y recuperación de información / Ranking and information-retrieval foundations

## Español

### 1. Estado

- Bloque: `0B-04A — Fundamentos de ranking y recuperación de información`.
- Estado: **`APPROVED / FROZEN`**.
- Entrega inicial: análisis metodológico A–K de seis PDF primarios por la IA de redacción.
- Revisión científica/editorial interna: **`PASS WITH MINOR CORRECTIONS`**.
- Errores materiales detectados: `0`.
- Aprobación expresa del autor: recibida el `2026-09-03`.
- Revisión experimental: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Gap definitivo: `NOT_DEFINED`.
- Manuscrito: `NOT_DRAFTED`.

Registros gobernantes:

- `article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`;
- `article/reviews/0B04A_INTERNAL_REVIEW.md`;
- `article/reviews/0B04A_AUTHOR_APPROVAL.md`.

Este artefacto congela el mapa metodológico canónico de 0B-04A. Las etiquetas `KEEP_CORE_METHOD` y `KEEP_SUPPORTING_METHOD` expresan función en el mapa metodológico y no obligación de cita final.

### 2. Corpus congelado

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Los seis se trataron como fuentes primarias del sub-lote. Todos los demás documentos del corpus quedaron fuera de alcance de 0B-04A.

### 3. Regla metodológica central

La separación gobernante es:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

Estas categorías pueden estar operacionalmente acopladas en una implementación concreta, pero no son sinónimos ni deben asignarse automáticamente a un único algoritmo por etapa.

### 4. Hallazgos canónicos por trabajo

#### P01 — Robertson & Zaragoza: BM25

- Función: `KEEP_CORE_METHOD`.
- Taxonomía: `SPARSE_LEXICAL_RETRIEVAL / CANDIDATE_GENERATION / RANKING`.
- BM25 se sitúa dentro del Probabilistic Relevance Framework como función de term weighting/document scoring.
- Su scoring incorpora rareza de términos/IDF, saturación de term frequency y normalización por longitud documental.
- El score operativo no debe interpretarse como probabilidad calibrada de relevancia ni, menos aún, como probabilidad de corrección NANDINA.
- La monografía no constituye evidencia experimental de superioridad universal de BM25 frente a otros paradigmas.

#### P02 — Reimers & Gurevych: Sentence-BERT

- Función: `KEEP_CORE_METHOD`.
- Taxonomía: `SENTENCE_EMBEDDING / SEMANTIC_REPRESENTATION`.
- SBERT produce embeddings independientes mediante arquitectura siamese/triplet y habilita comparación eficiente por similitud.
- Los autores lo sitúan como habilitador de semantic search/information retrieval; por tanto, no debe negarse categóricamente su función para retrieval.
- Un pipeline de recuperación a escala debe especificar por separado cómo realiza candidate search/indexing —exact search o ANN, por ejemplo—; esa infraestructura no forma parte del encoder SBERT por sí sola.
- Si se citan `77.03/79.23`, corresponden a `SBERT-NLI-base/large` sin STS-specific fine-tuning en STS Benchmark y no deben mezclarse con configuraciones posteriormente afinadas sobre STSb.

#### P03 — Karpukhin et al.: DPR

- Función: `KEEP_CORE_METHOD`.
- Taxonomía: `DENSE_BIENCODER_RETRIEVAL / INDEXED_SIMILARITY_SEARCH / CANDIDATE_GENERATION`.
- DPR representa query y passage con encoders separados, precalcula el corpus y recupera Top-k mediante similitud densa indexada.
- FAISS es infraestructura de index/search; no es el modelo semántico DPR.
- La búsqueda indexada por producto interno es el mecanismo operacional que materializa el Top-k; `index search` y `candidate generation` no deben dibujarse necesariamente como algoritmos independientes en serie.
- El contraste Natural Questions `78.4%` Top-20 DPR vs `59.1%` BM25 queda restringido a ese benchmark/configuración.
- SQuAD funciona como contraejemplo interno a cualquier claim de superioridad universal de dense retrieval sobre BM25.
- Resultados de open-domain QA no se transfieren directamente a HS/NANDINA.

#### P04 — Khattab & Zaharia: ColBERT

- Función: `KEEP_CORE_METHOD`.
- Taxonomía: `LATE_INTERACTION_RETRIEVAL`, con modos `RERANKING` y `FULL_RETRIEVAL`.
- Mantiene múltiples embeddings contextualizados por query/documento y aplica interacción tardía basada en MaxSim.
- `ColBERT (re-rank)` opera sobre candidatos previos.
- `ColBERT (full/end-to-end retrieval)` realiza candidate filtering desde la colección y después aplica late-interaction scoring.
- No debe reducirse a una sola identidad operacional.
- Los valores TREC-CAR `MAP 31.3 / MRR@10 44.3` para `BM25 + ColBERT` permanecen específicos del benchmark.
- Que full retrieval pueda recuperar documentos ausentes del candidate set upstream es un hallazgo arquitectónico; no demuestra superioridad universal de full retrieval.

#### P05 — Malkov & Yashunin: HNSW

- Función: `KEEP_SUPPORTING_METHOD`.
- Taxonomía: `ANN_INDEX_SEARCH / INDEX_ACCELERATION`.
- HNSW realiza approximate nearest-neighbor search sobre una representación y función de distancia preexistentes.
- No genera embeddings, no aprende semántica y no determina por sí mismo relevancia o correctness.
- ANN recall se refiere a recuperación de true nearest neighbors y no equivale automáticamente a Recall@k de documentos relevantes en IR.
- La copia suministrada conserva metadata editorial de manuscrito enviado a IEEE; título/autores/método son verificables, pero journal final, volumen, número, páginas y versión definitiva quedan `REVIEW_REQUIRED_FOR_FINAL_CITATION`.

#### P06 — Nogueira & Cho: Passage Re-Ranking with BERT

- Función: `KEEP_CORE_METHOD`.
- Taxonomía: `CROSS_ENCODER_RERANKING`.
- El pipeline evaluado es `BM25 -> Top-1000 candidates -> BERT rescoring/reranking -> final list`.
- BERT reranking es explícitamente segunda etapa y no candidate generation desde el corpus completo.
- Un reranker no puede recuperar un documento que el first-stage retriever no entregó.
- La copia primaria visible es `arXiv:1901.04085v5`, `14 Apr 2020`; no se reconstruye silenciosamente otra metadata editorial.
- El `27%` del abstract es mejora relativa de MRR@10, no `+27` puntos porcentuales.

### 5. Taxonomía congelada

- BM25: `SPARSE_LEXICAL_RETRIEVAL / CANDIDATE_GENERATION / RANKING`.
- SBERT: `SENTENCE_EMBEDDING / SEMANTIC_REPRESENTATION`.
- DPR: `DENSE_BIENCODER_RETRIEVAL / INDEXED_SIMILARITY_SEARCH / CANDIDATE_GENERATION`.
- ColBERT: `LATE_INTERACTION_RETRIEVAL / RERANKING / FULL_RETRIEVAL` según modo.
- HNSW: `ANN_INDEX_SEARCH / INDEX_ACCELERATION`.
- BERT Passage Re-Ranking: `CROSS_ENCODER_RERANKING`.

### 6. Reglas canónicas de métricas

Las siguientes familias no son intercambiables:

- HNSW ANN recall = recuperación de true nearest neighbors;
- DPR Top-k retrieval accuracy = presencia de passage con answer span dentro del Top-k;
- MRR/MAP = métricas de ranking bajo relevance judgments específicos;
- STS Spearman = correlación de similitud semántica;
- classification accuracy/F1 = métricas de clasificación.

No se sintetizan en un ranking global de BM25, SBERT, DPR, ColBERT, HNSW y BERT reranking. Tampoco se comparan resultados de STS, ANN, MS MARCO, TREC-CAR u open-domain QA como si pertenecieran a un único benchmark.

### 7. Claims metodológicos permitidos

Dentro de su alcance, 0B-04A permite sostener metodológicamente que:

1. BM25 es un mecanismo lexical de scoring/ranking con saturación de term frequency, IDF y normalización por longitud.
2. SBERT permite representaciones semánticas independientes y comparables por similitud, pero retrieval a escala exige especificar candidate search/indexing.
3. DPR es dense bi-encoder candidate retrieval con similarity search indexada.
4. ColBERT implementa late interaction y puede funcionar como reranker o como full retriever.
5. HNSW es una estructura ANN/index search y no un modelo semántico.
6. Un cross-encoder reranker puede modificar el orden de candidatos previos, pero no recuperar elementos ausentes del first stage.
7. Candidate generation, reranking y explanation deben permanecer conceptualmente separados.
8. Retrieval/ranking effectiveness no equivale a correctness arancelaria o jurídica.

### 8. Claims prohibidos por este freeze

No autoriza afirmar:

- `BM25 > dense retrieval` en general;
- `dense retrieval > BM25` en general;
- SBERT = índice ANN o sistema completo de retrieval por sí solo;
- HNSW genera/ mejora semántica de los embeddings;
- ANN recall = IR Recall@k;
- BERT reranking recupera desde todo el corpus;
- ColBERT es únicamente reranker o únicamente first-stage retriever;
- resultados heterogéneos forman un ranking universal de métodos;
- mejoras de MRR/MAP/Top-k retrieval demuestran mayor corrección HS/NANDINA;
- resultados de Wikipedia/MS MARCO/STS/ANN se transfieren directamente a NANDINA;
- los fundamentos IR prueban ausencia de prior art aduanero.

### 9. Protección del resultado experimental D1a

Los resultados fundacionales de DPR, ColBERT y SBERT no reinterpretan el resultado experimental D1a congelado del proyecto. D1a sigue describiendo únicamente **esa implementación densa exploratoria específica**. No se infiere superioridad/inferioridad general de dense retrieval ni se usa 0B-04A para refutar o reivindicar la familia metodológica.

Esta regla no modifica el ground truth experimental y, por tanto, no requirió revisión de la IA experimental.

### 10. Relación con F1–F5

0B-04A es fundacional y no constituye un pressure test de prior art aduanero. No cambia los estados heredados de F1–F5 después de 0B-03B.

- F1: se refuerza la precisión terminológica de `candidate generation/ranking` frente a evidence retrieval posterior.
- F2: `reranking`, que altera orden, queda separado de `explanation`, que en el piloto no puede alterarlo.
- F4: retrieval/ranking metrics permanecen separadas de substantive/legal correctness.
- F3/F5: sin evidencia fundacional directa adicional.
- G6: continúa eliminado como gap candidate.
- G7: continúa absorbido en F2.

### 11. Gate posterior

0B-04A queda cerrado. `0B-04B` permanece `NOT_STARTED / CLOSED_BY_GATE` hasta que exista una definición y apertura explícitas posteriores. Este freeze no autoriza automáticamente 0B-04B, 0B-05, 0B-06, 0C ni redacción del manuscrito.

---

## English

### 1. Status

- Block: `0B-04A — Ranking and information-retrieval foundations`.
- Status: **`APPROVED / FROZEN`**.
- Initial deliverable: A–K methodological analysis of six primary PDFs by the drafting AI.
- Internal scientific/editorial review: **`PASS WITH MINOR CORRECTIONS`**.
- Material errors: `0`.
- Express author approval received: `2026-09-03`.
- Experimental review: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Final gap: `NOT_DEFINED`.
- Manuscript: `NOT_DRAFTED`.

Governing records are the 0B-04A prompt, internal review, and author-approval files. This artifact freezes the canonical methodological map; method-role labels do not mandate final manuscript citation.

### 2. Frozen corpus

The six primary works are the BM25, Sentence-BERT, DPR, ColBERT, HNSW, and BERT passage-reranking PDFs assigned in the prompt. All other inherited documents were outside the 0B-04A scope.

### 3. Governing distinction

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

These functions may be operationally coupled, but they are not synonyms or necessarily separate one-to-one algorithms.

### 4. Canonical method map

- Robertson & Zaragoza: BM25 = sparse lexical term weighting/scoring/ranking within PRF; its score is not a calibrated probability of relevance or tariff correctness, and the monograph does not establish universal superiority.
- Reimers & Gurevych: SBERT = sentence embedding/semantic representation enabling semantic search; scalable candidate search/indexing must be specified separately from the encoder. `77.03/79.23`, if used, refer to SBERT-NLI base/large without STS-specific fine-tuning.
- Karpukhin et al.: DPR = dense bi-encoder indexed retrieval; FAISS is search/index infrastructure, and indexed inner-product search materializes Top-k candidates. The NQ `78.4 vs 59.1` comparison is benchmark-specific and SQuAD is an internal counterexample to universal dense superiority.
- Khattab & Zaharia: ColBERT = late-interaction retrieval with distinct reranking and full/end-to-end retrieval modes. Benchmark values remain benchmark-specific.
- Malkov & Yashunin: HNSW = ANN index/search acceleration over existing representations; it does not create semantic representations or determine relevance. Final publication metadata in the supplied manuscript remains `REVIEW_REQUIRED_FOR_FINAL_CITATION`.
- Nogueira & Cho: BERT passage reranking = second-stage cross-encoder reranking over BM25 Top-1000 candidates. The supplied primary copy is arXiv v5 dated 14 Apr 2020; its `27%` abstract figure is a relative MRR@10 improvement.

### 5. Metrics and prohibited synthesis

ANN recall, Top-k retrieval accuracy, MRR/MAP, STS Spearman, and classification accuracy/F1 are methodologically distinct. Results from STS, ANN, MS MARCO, TREC-CAR, or open-domain QA must not be combined into a universal ranking of BM25/SBERT/DPR/ColBERT/HNSW/BERT reranking.

### 6. D1a protection

Foundational DPR/ColBERT/SBERT results do not reinterpret the project's frozen D1a result. D1a remains evidence only about that specific exploratory dense implementation, not about dense retrieval as a general family. This clarification does not modify experimental ground truth and did not require experimental-AI review.

### 7. Gap-candidate effect and next gate

0B-04A is foundational rather than customs-prior-art analysis. It does not change F1–F5's post-0B-03B status; it only constrains terminology: candidate generation versus evidence retrieval, reranking versus explanation, and retrieval metrics versus substantive/legal correctness. G6 remains eliminated and G7 remains merged into F2.

0B-04A is closed. `0B-04B` remains `NOT_STARTED / CLOSED_BY_GATE` until a later explicit definition and opening. This freeze does not authorize later literature blocks, 0C, or manuscript drafting.
