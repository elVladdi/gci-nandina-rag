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
- `0B-04A`: **`APPROVED / FROZEN`** — `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

Después de 0B-03B permanecen provisionalmente F1–F5 en formas estrechas/metodológicas; G6 está eliminado como candidato a gap y G7 absorbido en F2. Ninguno constituye novelty ni gap definitivo. 0B-04A y la revisión interna de 0B-04B no modifican esos estados.

### 3. 0B-04 — Fundamentos de Information Retrieval y RAG

Alcance formal:
`article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-04A — Fundamentos de ranking y recuperación de información

Estado: **`APPROVED / FROZEN`**.

Prompt:
`article/prompts/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS.md`.

Revisión:
`article/reviews/0B04A_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`.

Aprobación:
`article/reviews/0B04A_AUTHOR_APPROVAL.md`.

Artefacto canónico:
`article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

Distinción metodológica congelada:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

#### 0B-04B — Fundamentos de RAG, transformación de consultas y grounding

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt ejecutado:
`article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.

Revisión interna:
`article/reviews/0B04B_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, revisión experimental `NOT_REQUIRED`.

Lote verificado:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM-Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging passage retrieval with generative models for open domain question answering.pdf`
4. `Query2doc-Query Expansion whit Large Lenguage Models.pdf`
5. `Query Rewriting for Retrieval-Augmented Large Language Models.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

Objetivo metodológico:

`QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

La revisión independiente confirma:

- `RETRIEVAL_AUGMENTED_GENERATION` ≠ `RETRIEVAL_AUGMENTED_PRETRAINING`;
- retrieve-then-generate ≠ query expansion/query rewriting;
- query transformation puede cambiar retrieval y ranking; no es explanation posterior;
- generation conditioned on retrieval ≠ explainer sobre Top-k externo e inmutable;
- passage fusion ≠ evidence attribution;
- provenance/inspectable passages ≠ formal auditability;
- evidentiality/grounding ≠ substantive/legal correctness;
- resultados de QA/fact verification/dialogue/IR no equivalen a accuracy o correctness HS/NANDINA;
- estos papers fundacionales no prueban ausencia de prior art aduanero.

Distinción congelable después de aprobación del autor:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

El review interno fija C1–C13 como normalizaciones obligatorias para el eventual freeze, incluyendo las inconsistencias RAG `17%`/`11.7%` y Asai `five datasets`/caption `six datasets`, la lectura limitada del chequeo humano `95%/96%`, la separación FiD fusion/attribution, la naturaleza upstream de Query2doc/query rewriting y los límites de transferencia de todos los benchmarks.

Contrato del piloto usado como frontera comparativa:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

F1–F5 reciben solo precisión metodológica. G6 permanece eliminado y G7 absorbido en F2.

#### Trabajos reservados para uso dirigido

Permanecen `RESERVED_FOR_DIRECTED_USE`: SimCSE, `Query Expansion by Prompting Large Language Models`, ExtractGPT, product-information extraction with ChatGPT y LLM product-attribute extraction/normalization. No se abre 0B-04C por defecto.

### 4. 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse/abrirse después del freeze de 0B-04B.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si, después de completar el corpus heredado relevante, persiste un vacío bibliográfico real y bajo las reglas de `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 6. Gate

Gate general:

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

Gate activo:

`0B-04B INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> aprobación expresa del autor -> integrar C1–C13 -> freeze -> evaluar apertura de 0B-05`.

La IA experimental no es revisora bibliográfica obligatoria y no fue requerida en 0B-04B porque ninguna interpretación modificó hechos/claims experimentales o restricciones bajo su autoridad.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A, 0B-03B y 0B-04A: `APPROVED / FROZEN`.
- Bloque activo: `0B-04B`.
- 0B-04B: `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- 0B-05: `NOT_STARTED / CLOSED_BY_GATE`.
- 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and rules

Phase `0B — Critical literature map and taxonomy` uses controlled thematic batches with full-PDF and claim-level verification. No manuscript drafting, final novelty, or definitive gap is allowed during 0B. The inherited corpus contains 62 distinct works/documents with primary access `62/62`.

### 2. Closed blocks

0B-01, 0B-02, 0B-03A, 0B-03B, and 0B-04A are **`APPROVED / FROZEN`**. F1–F5 remain provisional after 0B-03B; G6 is eliminated as a gap candidate and G7 is merged into F2. Neither 0B-04A nor the 0B-04B internal review changes those states.

### 3. 0B-04 — IR/RAG foundations

0B-04A is approved/frozen and established the distinction between representation, candidate generation, ANN/index search, reranking, and final ranking.

#### 0B-04B

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Executed prompt: `article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.

Internal review: `article/reviews/0B04B_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, experimental review `NOT_REQUIRED`.

The six assigned primary PDFs were independently verified. The governing pipeline remains `QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

The review confirms that retrieval-augmented generation, retrieval-augmented pretraining, retrieve-then-generate, query expansion, query rewriting, passage fusion, and evidentiality-guided generation are distinct functions; provenance/inspectable passages are not formal auditability; and evidentiality/grounding are not substantive or legal correctness.

Freeze-eligible distinctions after author approval:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

C1–C13 in the internal review govern the eventual freeze, including the RAG `17%`/`11.7%` discrepancy, Asai's five datasets despite a `six datasets` caption, the limited `95%/96%` human-label check, the FiD fusion/attribution distinction, Query2doc/query-rewriting upstream causality, and all benchmark-transfer limits.

The current pilot remains a comparison boundary: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

F1–F5 receive only methodological precision; G6 remains eliminated and G7 remains merged into F2.

### 4. Later blocks and gate

0B-05 is `NOT_STARTED / CLOSED_BY_GATE` and may open only after 0B-04B is frozen. 0B-06 remains not started and will open only if a genuine bibliographic gap remains after inherited literature is exhausted.

Active gate: `0B-04B INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> express author approval -> integrate C1–C13 -> freeze -> assess opening 0B-05`.

Experimental-AI review was not required because no frozen experimental fact/claim or restriction was affected.

0C remains blocked until 0B closes; 0D remains blocked until 0C closes; target journal remains pending until 0D.