# Aprobación del autor 0B-04A / 0B-04A Author Approval

## Español

### Identificación

- Bloque: `0B-04A — Fundamentos de ranking y recuperación de información`.
- Dictamen interno previo: `PASS WITH MINOR CORRECTIONS`.
- Errores materiales detectados: `0`.
- Revisión experimental: `NOT_REQUIRED`.
- Fecha de aprobación expresa del autor: `2026-09-03`.

### Aprobación

El autor aprobó expresamente el bloque 0B-04A y autorizó su cierre y congelamiento en GitHub.

La aprobación comprende la integración de las normalizaciones C1–C8 registradas en:

`article/reviews/0B04A_INTERNAL_REVIEW.md`

En particular, quedan aceptadas como gobernantes para el freeze:

1. BM25 se describe como función lexical de term weighting/scoring/ranking dentro del Probabilistic Relevance Framework; su score no es una probabilidad calibrada de relevancia ni de corrección arancelaria.
2. SBERT se conserva como `SENTENCE_EMBEDDING / SEMANTIC_REPRESENTATION`; habilita semantic search, pero la búsqueda/indexación de candidatos a escala debe especificarse separadamente del encoder.
3. DPR se conserva como `DENSE_BIENCODER_RETRIEVAL / INDEXED_SIMILARITY_SEARCH / CANDIDATE_GENERATION`; FAISS es infraestructura de búsqueda y la búsqueda indexada materializa el Top-k.
4. ColBERT conserva dos modos distintos: `RERANKING` y `FULL_RETRIEVAL`.
5. HNSW se clasifica como `ANN_INDEX_SEARCH / INDEX_ACCELERATION`, no como modelo semántico; la metadata editorial final de la copia suministrada queda `REVIEW_REQUIRED_FOR_FINAL_CITATION`.
6. Nogueira–Cho se conserva como `CROSS_ENCODER_RERANKING` de segunda etapa sobre candidatos BM25; la copia primaria visible es arXiv v5 de 2020 y el `27%` reportado es mejora relativa, no puntos porcentuales.
7. ANN recall, Top-k retrieval accuracy, MRR/MAP, STS Spearman y métricas de clasificación permanecen metodológicamente separadas y no se sintetizan como ranking universal de métodos.
8. Los resultados fundacionales de dense retrieval no reinterpretan D1a: el resultado experimental congelado sigue siendo evidencia únicamente sobre esa implementación exploratoria específica.

### Estado autorizado

```text
0B-04A = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Esta aprobación no autoriza por sí sola la apertura de 0B-04B ni la redacción del manuscrito. 0B-04B debe definirse y abrirse mediante un cambio posterior explícito.

---

## English

### Identification

- Block: `0B-04A — Ranking and information-retrieval foundations`.
- Prior internal verdict: `PASS WITH MINOR CORRECTIONS`.
- Material errors: `0`.
- Experimental review: `NOT_REQUIRED`.
- Express author-approval date: `2026-09-03`.

### Approval

The author expressly approved 0B-04A and authorized its closure and freeze in GitHub.

Approval includes the integration of C1–C8 from `article/reviews/0B04A_INTERNAL_REVIEW.md`: BM25 is lexical ranking within PRF rather than a calibrated relevance/correctness probability; SBERT is semantic representation with candidate search/indexing specified separately; DPR is indexed dense bi-encoder candidate retrieval; ColBERT preserves distinct reranking and full-retrieval modes; HNSW is ANN index/search infrastructure with unresolved final publication metadata in the supplied copy; Nogueira–Cho is second-stage cross-encoder reranking over BM25 candidates; heterogeneous IR/ANN/STS/classification metrics remain non-interchangeable; and foundational dense-retrieval results do not reinterpret the project's frozen D1a result beyond that specific exploratory implementation.

### Authorized state

```text
0B-04A = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

This approval does not by itself open 0B-04B or authorize manuscript drafting. 0B-04B requires a later explicit definition/opening change.
