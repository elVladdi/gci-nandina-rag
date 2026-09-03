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
- `SUPPORTS_CANDIDATE` en lotes de prior art significa solo supervivencia provisional, nunca novelty;
- las referencias heredadas conservan elegibilidad aunque sean antiguas/proceedings/preprints; nuevas referencias académicas se rigen por `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 2. Bloques ya cerrados

- `0B-01 — Clasificación HS directa y aprendizaje supervisado`: **`APPROVED / FROZEN`**.
  - Artefacto: `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera`: **`APPROVED / FROZEN`**.
  - Artefacto: `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero`: **`APPROVED / FROZEN`**.
  - Artefacto: `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio`: **`APPROVED / FROZEN`**.
  - Artefacto: `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.

Después de 0B-03B quedan provisionalmente:

- F1: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`;
- F2: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`;
- F3: `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`;
- F4: `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`;
- F5: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`;
- G6: `ELIMINATED AS GAP CANDIDATE`;
- G7: `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

Ninguno constituye novelty ni gap definitivo.

### 3. 0B-04 — Fundamentos de Information Retrieval y RAG

Alcance formal:
`article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

Por volumen y heterogeneidad, 0B-04 se divide en dos sub-lotes principales. No todos los trabajos IR/RAG del corpus se analizan automáticamente: solo aquellos que respaldan decisiones metodológicas concretas.

#### 0B-04A — Fundamentos de ranking y recuperación de información

Estado: **`READY_FOR_DRAFTING`**.

Prompt activo:
`article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.

PDF asignados:

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Objetivo: distinguir rigurosamente:

`QUERY/DOCUMENT REPRESENTATION -> CANDIDATE GENERATION -> ANN/INDEX SEARCH -> RERANKING -> FINAL RANKING`.

Controles obligatorios:

- BM25 se analiza desde su marco probabilístico, sin convertirlo en una afirmación de superioridad general;
- `SENTENCE_EMBEDDING` ≠ sistema completo de retrieval;
- `DENSE_BIENCODER_RETRIEVAL` ≠ `LATE_INTERACTION_RETRIEVAL`;
- `CROSS_ENCODER_RERANKING` presupone candidatos previos cuando el paper así lo define;
- HNSW = `ANN_INDEX_SEARCH`, no modelo semántico;
- resultados de benchmarks heterogéneos no se convierten en comparación global de métodos;
- métricas de retrieval no equivalen a classification accuracy;
- este lote es fundacional: F1–F5 se relacionan mediante etiquetas metodológicas, no mediante supuesta evidencia de novelty.

Los demás 56 documentos permanecen fuera de alcance de 0B-04A.

#### 0B-04B — Fundamentos de RAG, query transformation y grounding

Estado: `NOT_STARTED`.

Se abrirá solo después de cerrar 0B-04A. Lote previsto, sujeto a confirmación antes de apertura:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM: Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering.pdf`
4. `Query2doc.pdf`
5. `Query Rewriting for Retrieval-Augmented LLMs.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

No existe todavía prompt ejecutable para 0B-04B.

#### Trabajos reservados para uso dirigido

Estado `RESERVED_FOR_DIRECTED_USE`:

- `SimCSE.pdf`;
- `Query Expansion by Prompting Large Language Models.pdf`;
- `ExtractGPT.pdf`;
- `Product Information Extraction using ChatGPT.pdf`;
- `Using LLMs for the Extraction and Normalization of Product Attribute Values.pdf`.

Solo se abrirán si una necesidad metodológica concreta los hace necesarios. No existe 0B-04C por defecto.

### 4. 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Estado: `NOT_STARTED`.

Previsto para documentación de datasets, data statements, trazabilidad, reproducibilidad, gestión del conocimiento y fuentes normativas/oficiales necesarias para claims concretos.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si, después de completar el corpus heredado relevante, persiste un vacío bibliográfico real. Toda nueva literatura académica deberá cumplir `article/BIBLIOGRAPHIC_FRAMEWORK.md`, salvo excepción expresa del autor.

### 6. Gate

Gate general:

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

Gate activo:

`0B-04A READY_FOR_DRAFTING -> IA de redacción -> revisión interna -> aprobación del autor -> freeze -> definir/abrir 0B-04B`.

La IA experimental no es revisora bibliográfica obligatoria. Se incorpora únicamente si una interpretación bibliográfica afecta directamente hechos/claims experimentales o restricciones metodológicas bajo su autoridad.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A y 0B-03B: `APPROVED / FROZEN`.
- Bloque activo: `0B-04A`.
- 0B-04A: `READY_FOR_DRAFTING`.
- 0B-04B: `NOT_STARTED`.
- 0B-05/0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and governing rules

Phase `0B — Critical literature map and taxonomy` is executed through controlled thematic batches. Full-PDF reading and claim-level provenance are mandatory. No manuscript drafting, final novelty, or definitive gap is allowed during 0B. The consolidated corpus contains 62 distinct works/documents with primary access `62/62`.

### 2. Closed blocks

0B-01, 0B-02, 0B-03A, and 0B-03B are **`APPROVED / FROZEN`** with their canonical literature artifacts. After 0B-03B, F1–F5 remain provisional in narrowed forms, G6 is eliminated as a gap candidate, and G7 is merged into F2. None establishes novelty or a final gap.

### 3. 0B-04 — Information Retrieval and RAG foundations

Formal scope: `article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

0B-04 is split into controlled sub-batches and does not automatically analyze every IR/RAG paper in the inherited corpus.

#### 0B-04A — Ranking and retrieval foundations

Status: **`READY_FOR_DRAFTING`**.

Active prompt: `article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.

Assigned papers are the BM25, Sentence-BERT, DPR, ColBERT, HNSW, and BERT reranking works listed in the Spanish section.

The governing objective is to distinguish query/document representation, candidate generation, ANN/index search, reranking, and final ranking. HNSW is treated as ANN/index search rather than a semantic model; sentence embeddings are not automatically complete retrievers; cross-encoder reranking must be distinguished from candidate generation; and heterogeneous benchmark scores must not be synthesized as global method superiority.

Because 0B-04A is foundational, F1–F5 are mapped through methodological relevance rather than used to infer missing customs prior art.

#### 0B-04B — RAG, query transformation, and grounding foundations

Status: `NOT_STARTED`; it opens only after 0B-04A closes. The planned six-paper set includes RAG, REALM, passage-retrieval/generative QA, Query2doc, query rewriting for RAG, and evidentiality-guided generation. No executable 0B-04B prompt exists yet.

Five additional IR/product-processing works remain `RESERVED_FOR_DIRECTED_USE` and will be analyzed only if a concrete methodological need arises.

### 4. Later blocks

0B-05 and 0B-06 remain `NOT_STARTED`. 0B-06 opens only if a genuine bibliographic gap remains after relevant inherited literature is exhausted.

### 5. Gate and current state

Active gate: `0B-04A READY_FOR_DRAFTING -> drafting AI -> internal primary-PDF review -> author approval -> freeze -> define/open 0B-04B`.

Experimental-AI review is required only if literature interpretation changes frozen experimental facts/claims or methodological restrictions under its authority.

Current state: Phase 0B is open; 0B-04A is the active block; 0C remains blocked until 0B closes; 0D remains blocked until 0C closes; target journal remains pending until 0D.