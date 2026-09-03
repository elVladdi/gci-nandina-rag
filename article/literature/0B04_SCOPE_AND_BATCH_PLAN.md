# 0B-04 — Alcance y plan de lotes de fundamentos IR/RAG / IR-RAG foundations scope and batch plan

## Español

### 1. Propósito

`0B-04 — Fundamentos de Information Retrieval y RAG` establece el fundamento metodológico mínimo para describir ranking léxico BM25, representación semántica/dense retrieval, late interaction, reranking, ANN/indexación, RAG, query transformation y grounding/evidentiality. No es una revisión general de IR ni una búsqueda de novelty.

El bloque impide errores de categoría como `embedding = retriever`, `HNSW = semantic model`, `reranker = candidate generator`, `RAG = cualquier uso de documentos` o `retrieval metric = classification accuracy`.

### 2. 0B-04A — Fundamentos de ranking y recuperación

Estado: **`APPROVED / FROZEN`**.

Registros:

- Prompt: `article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.
- Revisión: `article/reviews/0B04A_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`.
- Aprobación: `article/reviews/0B04A_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

Distinción congelada:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

Hallazgos gobernantes: BM25 = lexical ranking; SBERT = semantic representation con búsqueda/indexación especificada separadamente; DPR = indexed dense bi-encoder retrieval; ColBERT = late interaction con modos reranking/full retrieval; HNSW = ANN index/search; Nogueira–Cho = second-stage cross-encoder reranking. Las métricas ANN/IR/STS/clasificación no son intercambiables y los fundamentos dense no reinterpretan D1a fuera de su implementación exploratoria específica.

### 3. 0B-04B — Fundamentos de RAG, transformación de consultas y grounding

Estado: **`APPROVED / FROZEN`**.

Registros:

- Prompt: `article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.
- Revisión interna: `article/reviews/0B04B_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`.
- Aprobación: `article/reviews/0B04B_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Lote congelado:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM-Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging passage retrieval with generative models for open domain question answering.pdf`
4. `Query2doc-Query Expansion whit Large Lenguage Models.pdf`
5. `Query Rewriting for Retrieval-Augmented Large Language Models.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

Pipeline general de contraste:

`QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

Distinciones congeladas:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Normalizaciones C1–C13 integradas:

- Lewis et al.: gobierna `11.7%` de Tabla 4 frente al `17%` narrativo; la evaluación humana de 452 pares no es una tasa universal de hallucination.
- RAG-Token no ejecuta un nuevo retrieval por token; RAG es retrieval-conditioned generation, no hard grounding.
- REALM = retrieval-augmented pretraining/retrieve-then-predict; Open-QA span-based.
- FiD: passage fusion ≠ evidence attribution.
- Query2doc = query expansion upstream; pseudo-documento ≠ evidencia, OOD mixto y riesgo de false claims.
- Query2doc: deltas no se reinterpretan automáticamente como porcentajes relativos; latencia específica de configuración.
- Rewrite-Retrieve-Read = query rewriting/retriever-reader interaction; la query puede cambiar retrieval y downstream output.
- Asai et al.: evidentiality task-relative y labels parcialmente dependientes del generador base; cinco datasets pese al caption `six datasets`; `95%/96%` = validación de labels bajo su protocolo, no auditability/legal correctness.
- provenance, grounding, evidentiality y formal auditability permanecen separados.
- resultados de benchmarks no se transfieren como métricas HS/NANDINA.
- F1–F5 no cambian de estado por este lote; G6 permanece eliminado y G7 absorbido en F2.

Contrato del piloto usado solo como frontera comparativa:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

### 4. Trabajos reservados

Permanecen `RESERVED_FOR_DIRECTED_USE`:

- `SimCSE.pdf`;
- `Query Expansion by Prompting Large Language Models.pdf`;
- `ExtractGPT.pdf`;
- `Product Information Extraction using ChatGPT.pdf`;
- `Using LLMs for the Extraction and Normalization of Product Attribute Values.pdf`.

No se abre un 0B-04C por defecto.

### 5. Relación con candidatos de gap

0B-04 es metodológico y no prueba ausencia de prior art aduanero.

Después de los lotes aduaneros permanecen provisionalmente:

- F1: ranking histórico fijado por precedentes + normativa posterior no reordenadora;
- F2: generador exclusivamente explicativo sobre Top-k externo e inmutable, sin feedback clasificatorio;
- F3: control de dependencia por unidad/grupo cuando aplica;
- F4: retrieval/predictive/path/evidence metrics ≠ corrección sustantiva adjudicada;
- F5: evaluación formal y separada de auditabilidad documental por salida.

G6 permanece eliminado y G7 absorbido en F2.

### 6. Gate siguiente

0B-04A y 0B-04B completaron el gate normal:

`IA de redacción -> revisión interna -> aprobación expresa del autor -> freeze`.

0B-05 queda **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**. Su alcance/lote/prompt deben definirse mediante un cambio posterior explícito antes de cualquier ejecución.

La IA experimental no fue requerida en 0B-04 porque ningún hallazgo bibliográfico modificó hechos/claims experimentales congelados ni restricciones bajo su autoridad.

### 7. Prohibiciones vigentes

Mientras 0B permanezca abierto:

- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva salvo apertura explícita de 0B-06;
- no comparar benchmarks heterogéneos como superioridad global;
- no modificar Plan Maestro ni 0A;
- no reabrir G6/G7;
- no reinterpretar resultados experimentales congelados fuera de su alcance;
- no ejecutar 0B-05 hasta su apertura explícita.

---

## English

### 1. Purpose

`0B-04 — Information Retrieval and RAG foundations` establishes the minimum methodological basis for lexical BM25 ranking, semantic/dense representation and retrieval, late interaction, reranking, ANN indexing/search, RAG, query transformation, and grounding/evidentiality. It is not a general IR review or novelty-search stage.

### 2. 0B-04A — Ranking and retrieval foundations

Status: **`APPROVED / FROZEN`**. Its prompt, internal review, author approval, and canonical freeze are versioned. The frozen distinction is `QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`. Foundational dense-retrieval results do not reinterpret the project's D1a result beyond that specific exploratory implementation.

### 3. 0B-04B — RAG, query transformation, and grounding foundations

Status: **`APPROVED / FROZEN`**.

Governing records are the executable prompt, internal review, author approval, and canonical artifact `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.

The frozen batch contains the Lewis et al. RAG paper, REALM, Fusion-in-Decoder, Query2doc, Query Rewriting for Retrieval-Augmented Large Language Models, and Evidentiality-guided Generation.

General comparison pipeline: `QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

Frozen distinctions:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

C1–C13 are integrated: Lewis's Table-4 `11.7%` governs the narrative `17%` discrepancy; RAG-Token does not retrieve anew per token; REALM remains retrieval-augmented pretraining/span-based Open-QA; FiD fusion is not attribution; Query2doc/query rewriting are upstream transformations; pseudo-document risks, mixed OOD outcomes, and configuration-specific latency are preserved; Asai et al. is governed by five datasets and the limited `95%/96%` label-validation protocol; provenance/grounding/evidentiality/formal auditability remain distinct; and benchmark results do not transfer as HS/NANDINA metrics.

The pilot remains only a comparison boundary: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

### 4. Reserved works and gap governance

SimCSE, query expansion by prompting LLMs, ExtractGPT, product-information extraction, and product-attribute extraction/normalization remain `RESERVED_FOR_DIRECTED_USE`; no 0B-04C opens by default.

0B-04 is methodological and does not change F1–F5's customs-prior-art status. G6 remains eliminated and G7 remains merged into F2.

### 5. Next gate

0B-04A and 0B-04B completed the normal drafting/review/author-approval/freeze gate. 0B-05 is now **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`** and requires a later explicit scope/batch/prompt definition before execution.

Experimental-AI review was not required because no frozen experimental fact/claim or restriction was changed.

No manuscript drafting, final novelty/gap claims, new-literature search outside an explicitly opened 0B-06, Master-Plan/0A modification, reopening G6/G7, or 0B-05 execution before explicit opening is authorized while 0B remains open.
