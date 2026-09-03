# Revisión interna 0B-04A / 0B-04A Internal Review

## Español

### 1. Identificación

- Bloque: `0B-04A — Fundamentos de ranking y recuperación de información`.
- Tipo de revisión: científica/editorial interna con verificación de claims contra los seis PDF primarios asignados.
- Entrega revisada: análisis A–K producido por la IA de redacción.
- Estado previo: `READY_FOR_DRAFTING`.
- Dictamen interno: **`PASS WITH MINOR CORRECTIONS`**.
- Errores materiales detectados: **`0`**.
- Revisión experimental: **`NOT_REQUIRED`**.
- Aprobación del autor: **`PENDING`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-04B: **`NOT_STARTED`**.

### 2. Resultado general

La entrega cumple el objetivo de 0B-04A y reconstruye correctamente la separación funcional entre representación, recuperación de candidatos, búsqueda/indexación ANN, reranking y ranking final. Los seis trabajos se analizaron como fuentes primarias del lote y no se utilizaron para declarar novelty, gap definitivo ni superioridad universal entre paradigmas.

La verificación independiente confirma los hallazgos principales:

- Robertson y Zaragoza presentan BM25 dentro del Probabilistic Relevance Framework como función de term weighting/document scoring; el propio documento declara que no es principalmente un survey experimental.
- Sentence-BERT produce embeddings independientes mediante arquitectura siamese/triplet y permite comparación eficiente por similitud, pero el índice/búsqueda a escala debe distinguirse del encoder.
- DPR es un dense bi-encoder retriever que precalcula pasajes, usa búsqueda indexada por producto interno y materializa un Top-k de candidatos; sus resultados frente a BM25 pertenecen a open-domain QA y no se trasladan automáticamente a HS/NANDINA.
- ColBERT implementa late interaction y tiene dos modos distintos: reranking de candidatos previos y end-to-end/full retrieval mediante vector-similarity candidate filtering seguido de scoring ColBERT.
- HNSW es una estructura de approximate nearest-neighbor search sobre una representación y función de distancia preexistentes; no crea embeddings ni define por sí mismo relevancia semántica.
- Nogueira y Cho implementan explícitamente la segunda etapa de un pipeline: BM25 genera candidatos y BERT reordena ese conjunto; un reranker no puede recuperar un elemento ausente del first stage.

### 3. Correcciones y normalizaciones obligatorias para el freeze

#### C1 — BM25: score de ranking ≠ probabilidad calibrada

Aunque BM25 se deriva dentro de un marco probabilístico de relevancia, su score operativo debe describirse como función de ranking/term weighting rank-equivalent, no como una probabilidad calibrada de relevancia y mucho menos como probabilidad de corrección NANDINA. Mantener IDF, saturación de term frequency y normalización por longitud como componentes del scoring, sin convertir la monografía en evidencia experimental de superioridad universal.

#### C2 — Sentence-BERT: evitar una negación excesiva de su función de retrieval

La taxonomía `SENTENCE_EMBEDDING` es correcta, pero el freeze no debe afirmar categóricamente que SBERT “no es retrieval”: los autores señalan explícitamente que sus embeddings habilitan semantic search/information retrieval. La formulación precisa es:

> SBERT aporta la representación independiente y una función de similitud; un pipeline de recuperación a escala todavía debe especificar cómo busca/selecciona candidatos —por ejemplo, exact search o un índice ANN—, y esa infraestructura no forma parte del encoder SBERT por sí sola.

Si se conservan `77.03/79.23`, deben identificarse como resultados de `SBERT-NLI-base/large` **sin entrenamiento STS específico** en STS Benchmark, para no mezclarlos con las configuraciones posteriormente fine-tuned sobre STSb.

#### C3 — DPR: index search y candidate generation están operacionalmente acoplados

DPR debe conservarse como `DENSE_BIENCODER_RETRIEVAL`. FAISS es infraestructura de similarity/index search, no el modelo de representación. En inferencia, la búsqueda indexada por inner product es precisamente el mecanismo que materializa el Top-k de candidatos; por ello el diagrama conceptual no debe sugerir que `ANN/index search` y `candidate generation` son siempre dos algoritmos independientes y estrictamente secuenciales.

Los resultados Natural Questions `78.4%` Top-20 para DPR frente a `59.1%` para el BM25 de los autores quedan restringidos a ese benchmark/configuración. SQuAD es un contraejemplo interno al supuesto de superioridad densa universal.

#### C4 — ColBERT: preservar siempre los dos modos

No reducir ColBERT a `reranker` ni a `first-stage dense retriever`. En el paper:

- `ColBERT (re-rank)` opera sobre candidatos previos;
- `ColBERT (full/end-to-end retrieval)` usa vector-similarity candidate filtering desde la colección y luego aplica late-interaction scoring.

Los valores TREC-CAR `MAP 31.3` y `MRR@10 44.3` para `BM25 + ColBERT` están verificados en la tabla del PDF, pero permanecen específicos de ese benchmark. El hallazgo arquitectónico importante es que full retrieval puede recuperar documentos ausentes del Top-1000 upstream; ello no implica superioridad universal de full retrieval.

#### C5 — HNSW: contenido metodológico válido, metadata final pendiente

El contenido técnico del PDF permite mantener `KEEP_SUPPORTING_METHOD`. Sin embargo, la copia disponible se identifica como manuscrito enviado a IEEE (`IEEE TRANSACTIONS ON JOURNAL NAME, MANUSCRIPT ID` / submitted for possible publication). Por tanto:

- título, autores y método: verificables;
- metadata editorial definitiva (journal final, volumen, número, páginas y versión de publicación): **`REVIEW_REQUIRED_FOR_FINAL_CITATION`**.

No completar esos campos desde memoria, referencias secundarias o conocimiento externo durante este freeze.

#### C6 — Nogueira y Cho: versionado bibliográfico y función de segunda etapa

La copia primaria disponible es `arXiv:1901.04085v5`, fechada `14 Apr 2020`. No se debe reconstruir silenciosamente una metadata editorial distinta. La función metodológica queda congelada como `CROSS_ENCODER_RERANKING`: BM25 entrega Top-1000 y BERT modifica el orden. El `27%` del abstract es mejora **relativa** de MRR@10 respecto del estado previo reportado, no `+27` puntos porcentuales.

#### C7 — Métricas heterogéneas: separación obligatoria

Mantener explícitamente que:

- HNSW ANN recall = recuperación de true nearest neighbors;
- DPR Top-k retrieval accuracy = proporción de queries cuyo Top-k contiene un passage con answer span;
- MRR/MAP = métricas de ranking bajo sus respectivos relevance judgments;
- STS Spearman = correlación de similitud semántica;
- classification accuracy/F1 = otra familia de evaluación.

No se sintetizan estas métricas en una tabla de “mejor método” ni se convierten unas en otras.

#### C8 — Protección del claim experimental dense D1a

Los resultados fundacionales de DPR, ColBERT o SBERT **no reinterpretan** el resultado experimental D1a del proyecto. El ground truth experimental congelado continúa autorizando únicamente una lectura sobre **esa implementación densa exploratoria específica**. No puede inferirse que dense retrieval sea superior/inferior en general ni que el desempeño D1a pruebe o refute la familia metodológica.

Esta normalización no modifica el ground truth experimental; por ello no activa revisión de la IA experimental.

### 4. Taxonomía metodológica gobernante

La entrega aporta una separación útil, con una precisión adicional: `ANN/index search` es infraestructura de búsqueda y puede ser el mecanismo operacional que materializa los candidatos, por lo que las etapas no siempre corresponden uno-a-uno con algoritmos independientes.

Taxonomía congelable:

- BM25: `SPARSE_LEXICAL_RETRIEVAL / CANDIDATE_GENERATION / RANKING`.
- SBERT: `SENTENCE_EMBEDDING / SEMANTIC_REPRESENTATION`; candidate search/index debe especificarse separadamente cuando aplique.
- DPR: `DENSE_BIENCODER_RETRIEVAL / INDEXED_SIMILARITY_SEARCH / CANDIDATE_GENERATION`.
- ColBERT: `LATE_INTERACTION_RETRIEVAL`, con modos `RERANKING` y `FULL_RETRIEVAL`.
- HNSW: `ANN_INDEX_SEARCH / INDEX_ACCELERATION`, no semantic representation.
- BERT passage reranker: `CROSS_ENCODER_RERANKING`, presupone first-stage candidates en el diseño evaluado.

### 5. Efecto sobre F1–F5

0B-04A es un lote fundacional y **no constituye un pressure test de prior art aduanero**. No cambia el estado bibliográfico de F1–F5 establecido tras 0B-03B. Su efecto es terminológico/metodológico:

- F1 debe usar correctamente `candidate generation/ranking` y distinguirlo de evidence retrieval posterior;
- F2 debe distinguir `reranking`, que modifica el orden, de explanation, que en el piloto no puede modificarlo;
- F4 debe mantener retrieval/ranking metrics separadas de substantive/legal correctness;
- F3 y F5 no reciben evidencia fundacional directa de este lote.

G6 permanece eliminado y G7 permanece absorbido en F2.

### 6. Función bibliográfica provisional

- Robertson & Zaragoza — `KEEP_CORE_METHOD`.
- Reimers & Gurevych — `KEEP_CORE_METHOD`.
- Karpukhin et al. — `KEEP_CORE_METHOD`.
- Khattab & Zaharia — `KEEP_CORE_METHOD`.
- Malkov & Yashunin — `KEEP_SUPPORTING_METHOD` + `REVIEW_REQUIRED_FOR_FINAL_CITATION` para metadata editorial final.
- Nogueira & Cho — `KEEP_CORE_METHOD`; usar la versión primaria visible y no inferir una publicación distinta.

Estas etiquetas expresan función dentro del mapa metodológico y no obligación de cita final.

### 7. Dictamen y gate

**`0B-04A INTERNAL REVIEW = PASS WITH MINOR CORRECTIONS`**.

No se requiere una nueva ejecución completa por la IA de redacción. C1–C8 son normalizaciones deterministas de alcance, taxonomía, versionado y protección contra comparaciones inválidas que pueden integrarse editorialmente después de aprobación expresa del autor.

No se requiere revisión de la IA experimental porque no se modifica ningún hecho/claim experimental congelado ni el Plan Maestro.

Siguiente estado permitido:

`AUTHOR_APPROVAL_PENDING`.

Hasta aprobación expresa del autor:

- no congelar 0B-04A;
- no crear/abrir el prompt ejecutable de 0B-04B;
- no abrir 0B-05/0B-06;
- no abrir 0C;
- no redactar secciones del manuscrito.

---

## English

### 1. Identification

- Block: `0B-04A — Ranking and information-retrieval foundations`.
- Review type: internal scientific/editorial review with claim-level verification against the six assigned primary PDFs.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**.
- Material errors: **`0`**.
- Experimental review: **`NOT_REQUIRED`**.
- Author approval: **`PENDING`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-04B: **`NOT_STARTED`**.

### 2. Overall assessment

The deliverable correctly separates representation, candidate retrieval, ANN/index search, reranking, and final ranking. Primary-source verification confirms the central methodological map: BM25 is lexical ranking within the probabilistic relevance framework; SBERT produces independently computable sentence embeddings; DPR is indexed dense bi-encoder retrieval; ColBERT supports both reranking and full retrieval through late interaction; HNSW is ANN search infrastructure rather than a semantic representation model; and Nogueira–Cho implement an explicit second-stage BERT reranker over BM25 candidates.

### 3. Required corrections for freeze

**C1 — BM25.** Treat BM25 as a rank-scoring/term-weighting function derived in a probabilistic framework, not as a calibrated probability of relevance or tariff correctness. The monograph is not evidence of universal superiority.

**C2 — SBERT.** Do not state categorically that SBERT “is not retrieval.” The authors explicitly position its independent embeddings as enabling semantic search/IR. The precise distinction is that SBERT provides representation/similarity, while scalable candidate search/indexing must still be specified separately. If `77.03/79.23` are retained, label them as SBERT-NLI base/large without STS-specific fine-tuning on the STS Benchmark.

**C3 — DPR.** FAISS is index/search infrastructure rather than the semantic representation. Indexed inner-product search operationally materializes the candidate Top-k, so index search and candidate generation are not necessarily two independent algorithms. Restrict the NQ `78.4 vs 59.1` comparison to the evaluated setting; SQuAD is an internal counterexample to universal dense superiority.

**C4 — ColBERT.** Preserve both modes: reranking of upstream candidates and full/end-to-end retrieval through vector-similarity candidate filtering followed by late-interaction scoring. Verified TREC-CAR `MAP 31.3 / MRR@10 44.3` remains benchmark-specific.

**C5 — HNSW.** Scientific role remains `KEEP_SUPPORTING_METHOD`, but the supplied PDF is a submitted IEEE manuscript with placeholder journal metadata. Final journal/volume/issue/pages remain `REVIEW_REQUIRED_FOR_FINAL_CITATION` and must not be reconstructed from memory or secondary sources.

**C6 — Nogueira & Cho.** The supplied primary copy is arXiv v5 dated 14 Apr 2020. Preserve that version status unless later verified from a primary publication source. Its role is second-stage cross-encoder reranking over BM25 Top-1000; the abstract's `27%` is a relative MRR@10 improvement, not percentage points.

**C7 — Metrics.** ANN recall, Top-k retrieval accuracy, MRR/MAP, STS Spearman, and classification accuracy/F1 are distinct metrics and must not be synthesized into a universal method ranking.

**C8 — Experimental D1a protection.** Foundational DPR/ColBERT/SBERT results do not reinterpret the project's frozen D1a result. D1a remains evidence only about that specific exploratory dense implementation, not dense retrieval as a family. This clarification does not change experimental ground truth and therefore does not require experimental-AI review.

### 4. Method taxonomy

The governing taxonomy may freeze as: BM25 = sparse lexical retrieval/ranking; SBERT = sentence embedding/semantic representation; DPR = dense bi-encoder indexed retrieval; ColBERT = late-interaction retrieval with reranking and full-retrieval modes; HNSW = ANN index/search acceleration; BERT passage reranker = cross-encoder reranking over a first-stage candidate set.

### 5. Effect on gap candidates

0B-04A is foundational rather than customs-prior-art analysis. It does not change F1–F5's post-0B-03B status. It only constrains terminology: candidate generation must be separated from downstream evidence retrieval; reranking from explanation; and retrieval/ranking metrics from substantive/legal correctness. G6 remains eliminated and G7 remains merged into F2.

### 6. Gate

**`0B-04A INTERNAL REVIEW = PASS WITH MINOR CORRECTIONS`**. No complete drafting-AI rerun or experimental-AI review is required. After express author approval, C1–C8 may be integrated into the canonical freeze. Until then, 0B-04B remains closed and no later literature/manuscript phase may open.
