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

### 4. 0B-04B — Fundamentos de RAG, transformación de consultas y grounding

Estado: **`READY_FOR_DRAFTING`**.

Prompt activo:
`article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.

Lote final confirmado:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM-Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging passage retrieval with generative models for open domain question answering.pdf`
4. `Query2doc-Query Expansion whit Large Lenguage Models.pdf`
5. `Query Rewriting for Retrieval-Augmented Large Language Models.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

Los seis están dentro del corpus heredado y fueron localizados por identidad científica; duplicados o pequeñas variaciones ortográficas de nombre no alteran la identidad de la obra.

Objetivo gobernante:

`QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`

El sub-lote debe distinguir:

- `RETRIEVAL_AUGMENTED_GENERATION` de `RETRIEVAL_AUGMENTED_PRETRAINING`;
- retrieve-then-generate de query expansion/query rewriting;
- retrieval que determina el contexto disponible al generador de evidencia normativa posterior a un ranking histórico ya fijado;
- passage fusion de evidence attribution;
- inspectable retrieval/provenance de evaluación formal de auditabilidad;
- evidentiality/grounding de corrección sustantiva o jurídica.

Comparación obligatoria con el contrato del piloto:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

0B-04B sigue siendo **fundacional**. Para F1–F5 solo se usarán etiquetas de relevancia metodológica; no se utilizarán estos papers para declarar ausencia de prior art aduanero. G6 permanece eliminado y G7 absorbido en F2.

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

G6 permanece eliminado y G7 absorbido en F2. 0B-04A no modificó estos estados; 0B-04B deberá mantener el mismo control y aportar únicamente fundamentos/contrastes metodológicos.

### 7. Gate

0B-04A completó el gate:

`IA de redacción -> revisión interna -> aprobación expresa del autor -> freeze`.

Gate activo:

`0B-04B READY_FOR_DRAFTING -> IA de redacción -> revisión científica/editorial interna contra los seis PDF primarios -> corrección si aplica -> aprobación expresa del autor -> freeze -> evaluar apertura de 0B-05`.

No se abre 0B-05 antes de cerrar 0B-04B.

La IA experimental solo interviene si una interpretación bibliográfica modifica o amenaza un hecho/claim experimental congelado o una restricción bajo su autoridad.

### 8. Prohibiciones vigentes

Mientras 0B permanezca abierto:

- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva salvo apertura explícita de 0B-06;
- no comparar benchmarks heterogéneos como superioridad global;
- no modificar Plan Maestro ni 0A;
- no reabrir G6/G7;
- no reinterpretar resultados experimentales congelados fuera de su alcance;
- no avanzar a 0B-05, 0B-06 o 0C antes del gate correspondiente.

---

## English

### 1. Purpose

`0B-04 — Information Retrieval and RAG foundations` provides the minimum sufficient methodological basis for lexical BM25 ranking, semantic/dense representation and retrieval, late interaction, reranking, ANN indexing/search, RAG, query transformation, and grounding/evidentiality. It is not a general IR review or novelty-search stage.

### 2. Controlled selection

Only inherited works that support a concrete methodological decision or a necessary conceptual distinction are included. 0B-04 is divided into two controlled sub-batches.

### 3. 0B-04A — Ranking and retrieval foundations

Status: **`APPROVED / FROZEN`**. Its prompt, internal review, author approval, and canonical artifact are frozen. The governing map distinguishes lexical ranking, semantic representation, indexed dense retrieval, late interaction, ANN/index search, and second-stage cross-encoder reranking. Foundational dense-retrieval results do not reinterpret the project's frozen D1a result.

### 4. 0B-04B — RAG, query transformation, and grounding foundations

Status: **`READY_FOR_DRAFTING`**.

Active prompt:
`article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.

The final six-paper batch is the Lewis et al. RAG paper, REALM, Fusion-in-Decoder, Query2doc, Query Rewriting for Retrieval-Augmented Large Language Models, and Evidentiality-guided Generation listed in the Spanish section.

The governing pipeline is:

`QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

The block must distinguish retrieval-augmented generation from retrieval-augmented pretraining, retrieve-then-generate from query rewriting/expansion, passage fusion from evidence attribution, inspectable retrieval/provenance from formal auditability, and evidentiality/grounding from substantive or legal correctness.

The present pilot remains a distinct contract to be used only as a comparison boundary: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

0B-04B is foundational. F1–F5 may only receive methodological relevance labels; these papers are not proof of missing customs prior art. G6 remains eliminated and G7 remains merged into F2.

### 5. Reserved works

SimCSE, Query Expansion by Prompting Large Language Models, ExtractGPT, product-information extraction with ChatGPT, and LLM-based product-attribute extraction/normalization remain `RESERVED_FOR_DIRECTED_USE`. No 0B-04C opens by default.

### 6. Gate

The active gate is:

`0B-04B READY_FOR_DRAFTING -> drafting AI -> internal scientific/editorial review against the six primary PDFs -> correction if needed -> express author approval -> freeze -> assess opening 0B-05`.

0B-05 cannot open before 0B-04B closes. Experimental-AI review is required only if literature interpretation changes or threatens frozen experimental facts/claims or restrictions under its authority.

### 7. Prohibitions

No manuscript drafting, final novelty/gap claims, new-literature search outside an explicitly opened 0B-06, cross-benchmark universal superiority claims, Master-Plan/0A modification, reopening G6/G7, reinterpretation of frozen experiments beyond scope, or advancing to 0B-05/0B-06/0C before the corresponding gate.