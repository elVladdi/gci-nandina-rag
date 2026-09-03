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
- `SUPPORTS_CANDIDATE` significa solo supervivencia provisional, nunca novelty;
- las referencias heredadas conservan elegibilidad aunque sean antiguas/proceedings/preprints; nuevas referencias académicas se rigen por `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 2. Bloques cerrados

- `0B-01`: **`APPROVED / FROZEN`** — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02`: **`APPROVED / FROZEN`** — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A`: **`APPROVED / FROZEN`** — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B`: **`APPROVED / FROZEN`** — `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.
- `0B-04A`: **`APPROVED / FROZEN`** — `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.
- `0B-04B`: **`APPROVED / FROZEN`** — `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.

Después de 0B-03B permanecen provisionalmente F1–F5 en formas estrechas/metodológicas; G6 está eliminado como candidato a gap y G7 absorbido en F2. Ninguno constituye novelty ni gap definitivo. Los lotes fundacionales 0B-04A/04B no modifican esos estados.

### 3. 0B-04 — Fundamentos de Information Retrieval y RAG

Alcance formal:
`article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-04A

Estado: **`APPROVED / FROZEN`**.

Registros: prompt 0B04A, revisión interna, aprobación del autor y artefacto canónico `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

Distinción congelada:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

#### 0B-04B

Estado: **`APPROVED / FROZEN`**.

Registros:

- Prompt: `article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.
- Revisión interna: `article/reviews/0B04B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación: `article/reviews/0B04B_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Lote congelado: Lewis et al. RAG, REALM, Fusion-in-Decoder, Query2doc, Query Rewriting for Retrieval-Augmented Large Language Models y Evidentiality-guided Generation.

Distinciones congeladas:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

C1–C13 quedan integradas: gobernar Lewis por Tabla-4 `11.7%` frente al `17%` narrativo; no describir RAG-Token como retrieval nuevo por token; preservar REALM como retrieval-augmented pretraining/span-based Open-QA; separar FiD fusion/attribution; tratar Query2doc/query rewriting como transformaciones upstream; preservar OOD mixto, false-claim risk y latencia específica; gobernar Asai por cinco datasets y limitar `95%/96%` a validación de labels; separar provenance/grounding/evidentiality/auditability/legal correctness; no transferir benchmarks a HS/NANDINA.

Contrato del piloto usado solo como frontera comparativa:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

#### Trabajos reservados

Permanecen `RESERVED_FOR_DIRECTED_USE`: SimCSE, `Query Expansion by Prompting Large Language Models`, ExtractGPT, product-information extraction with ChatGPT y LLM product-attribute extraction/normalization. No se abre 0B-04C por defecto.

### 4. 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Estado: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

0B-04B ya está congelado. 0B-05 puede definirse y abrirse mediante un cambio posterior explícito. Antes de ejecutarlo deben fijarse su alcance, lote y prompt.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si, después de completar el corpus heredado relevante, persiste un vacío bibliográfico real y bajo las reglas de `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 6. Gate

Gate general:

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

0B-04A y 0B-04B completaron el gate.

Siguiente gate potencial:

`definir lote final 0B-05 -> crear prompt ejecutable -> READY_FOR_DRAFTING -> IA de redacción -> revisión interna -> aprobación del autor -> freeze -> evaluar necesidad real de 0B-06`.

La IA experimental no es revisora bibliográfica obligatoria. Se incorpora solo si una interpretación bibliográfica modifica hechos/claims experimentales o restricciones bajo su autoridad.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A y 0B-04B: `APPROVED / FROZEN`.
- 0B-05: `NOT_STARTED / ELIGIBLE_FOR_DEFINITION`.
- 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and rules

Phase `0B — Critical literature map and taxonomy` uses controlled thematic batches with full-PDF and claim-level verification. No manuscript drafting, final novelty, or definitive gap is allowed during 0B. The inherited corpus contains 62 distinct works/documents with primary access `62/62`.

### 2. Closed blocks

0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, and 0B-04B are **`APPROVED / FROZEN`**. F1–F5 remain provisional after the customs-prior-art batches; G6 is eliminated as a gap candidate and G7 is merged into F2. The foundational 0B-04 batches do not change those states.

### 3. 0B-04 — IR/RAG foundations

0B-04A is approved/frozen and established the distinction between representation, candidate generation, ANN/index search, reranking, and final ranking.

0B-04B is approved/frozen. Governing records are its prompt, internal review, author approval, and canonical frozen artifact. The six-paper batch covers RAG, REALM, Fusion-in-Decoder, Query2doc, query rewriting, and evidentiality-guided generation.

Frozen distinctions:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Integrated C1–C13 preserve the Lewis `11.7%` table value over the narrative `17%`, reject per-token re-retrieval wording for RAG-Token, preserve REALM as retrieval-augmented pretraining/span-based Open-QA, separate FiD fusion from attribution, treat Query2doc/query rewriting as upstream transformations, preserve mixed OOD and pseudo-document risks, govern Asai by five datasets and its limited `95%/96%` label-validation protocol, keep provenance/grounding/evidentiality/auditability/legal correctness separate, and prevent transfer of benchmark scores as HS/NANDINA metrics.

The pilot remains only a comparison boundary: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

Reserved IR/product-processing works remain `RESERVED_FOR_DIRECTED_USE`; no 0B-04C opens by default.

### 4. 0B-05 and later gate

0B-05 is now **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**. It may be explicitly defined/opened after the 0B-04B freeze, but its scope, batch, and executable prompt must be fixed before execution.

0B-06 remains `NOT_STARTED` and opens only if a genuine bibliographic gap remains after the relevant inherited corpus is exhausted.

Next potential gate: define final 0B-05 batch -> create executable prompt -> READY_FOR_DRAFTING -> drafting AI -> internal review -> author approval -> freeze -> assess whether 0B-06 is actually needed.

0C remains blocked until 0B closes; 0D remains blocked until 0C closes; target journal remains pending until 0D.
