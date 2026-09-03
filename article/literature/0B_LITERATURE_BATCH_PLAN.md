# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta por lotes temáticos controlados. Su finalidad es leer los PDF completos del corpus disponible, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable para 0C. Durante 0B no se redacta Related Work ni se declara novelty o gap definitivo.

### 2. Corpus y reglas generales

- Corpus PDF consolidado disponible: `62` obras/documentos distintos.
- La disponibilidad de un PDF no autoriza analizarlo fuera del lote activo.
- Cada PDF debe leerse íntegramente.
- No se inventan metadatos, resultados, diseños ni DOI.
- Metadata dudosa: `REVIEW_REQUIRED`.
- Una afirmación que un paper atribuya a un tercero no se convierte en hecho independiente del manuscrito sin verificar la fuente primaria correspondiente.
- Se distinguen `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y, desde 0B-02, `SECONDARY_CLAIM_UNVERIFIED`.
- No se equiparan clasificación, candidate retrieval, evidence retrieval, validación, explicación ni auditabilidad.
- La ausencia de group split documentado no demuestra leakage.
- Las referencias heredadas conservan elegibilidad aunque sean antiguas, proceedings o tesis. Las reglas 2022–2026/Q1-Q2 aplican a literatura académica nueva conforme a `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 3. Lotes

#### 0B-01 — Clasificación HS directa y aprendizaje supervisado

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:

`article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`

Revisión y aprobación:

- `article/reviews/0B01_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`;
- `article/reviews/0B01_AUTHOR_APPROVAL.md` — aprobación expresa recibida.

PDF analizados:

1. `Best approaches for HS code prediction.pdf`
2. `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
3. `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
4. `Automatic Tariff Classification System using Deep Learning.pdf`
5. `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
6. `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
7. `Application of machine learning for automated HS-6 code assignment.pdf`
8. `Auto-Categorization of HS Code Using Background Net Approach.pdf`

F1–F5 permanecen `CANDIDATE_GAP_ONLY` y pueden ser falsados o reformulados por lotes posteriores.

#### 0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera

Estado: **`READY_FOR_DRAFTING`**.

Prompt activo:

`article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`

PDF asignados:

1. `Classification of Goods Using Text Descriptions With Sentences Retrieval.pdf`
2. `Text2Trade. A semantic search system whith Monte Carlo Droput Uncertainty Quantification For HS Code Retrieval..pdf`
3. `Explainable Product Classification for Customs.pdf`
4. `Application of machine learning for assessment of HS code correctness.pdf`
5. `Customs Tariff Classification and the Use of Assistive Technologies.pdf`
6. `Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities.pdf`

Objetivos específicos del lote:

- distinguir code retrieval, sentence retrieval, validation/correction, structured knowledge, explainability y auditability;
- determinar el papel exacto de descripciones HS/WCO/normativa en cada trabajo;
- separar conocimiento usado para decidir el código de evidencia documental posterior al ranking;
- auditar incertidumbre, rejection, human support, traceability y controles de dependencia;
- someter F1–F5 a `SUPPORTS_CANDIDATE`, `WEAKENS_CANDIDATE`, `FALSIFIES_CANDIDATE`, `NOT_RELEVANT` o `UNRESOLVED`;
- registrar claims secundarios como `SECONDARY_CLAIM_UNVERIFIED` hasta comprobar fuente primaria.

#### 0B-03 — LLM, multimodalidad y agentes/razonamiento jerárquico

Estado: `NOT_STARTED`.

Incluirá trabajos del corpus sobre LLM para clasificación/compliance, RAG aduanero, agentes, multimodalidad y benchmarks de razonamiento/búsqueda jerárquica.

#### 0B-04 — Fundamentos de Information Retrieval y RAG

Estado: `NOT_STARTED`.

Previsto para BM25, DPR, HNSW, ColBERT, SBERT, RAG y fundamentos afines únicamente cuando respalden decisiones metodológicas concretas.

#### 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Estado: `NOT_STARTED`.

Previsto para documentación de datasets, data statements, trazabilidad, reproducibilidad, gestión del conocimiento y fuentes normativas/oficiales necesarias para claims concretos.

#### 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si los lotes del corpus proporcionado revelan un vacío bibliográfico real. Toda nueva literatura académica deberá cumplir `article/BIBLIOGRAPHIC_FRAMEWORK.md`, salvo excepción expresa y documentada del autor.

### 4. Gate de cada lote

`IA de redacción -> revisión científica/editorial interna -> corrección si aplica -> aprobación del autor -> freeze`

La IA experimental no es revisora bibliográfica obligatoria. Se solicita únicamente si una interpretación de literatura afecta directamente hechos experimentales, claims experimentales o restricciones metodológicas bajo su autoridad.

### 5. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01: `APPROVED / FROZEN`.
- Bloque activo: `0B-02`.
- Estado 0B-02: `READY_FOR_DRAFTING`.
- 0B-03 y posteriores: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: pendiente hasta 0D.

---

## English

### 1. Purpose

Phase `0B — Critical literature map and taxonomy` is executed through controlled thematic batches. Its purpose is to read complete PDFs, determine what problem each work actually solves, and build a comparable map for 0C. No Related Work drafting, final novelty claim, or definitive gap is allowed during 0B.

### 2. Corpus and general rules

- Consolidated PDF corpus: `62` distinct works/documents.
- PDF availability does not authorize analysis outside the active batch.
- Every assigned PDF must be read in full.
- Metadata, results, designs, and DOI must not be invented.
- Uncertain metadata: `REVIEW_REQUIRED`.
- A statement that a paper attributes to a third party does not become an independent manuscript fact without checking the corresponding primary source.
- Distinguish `REPORTED_BY_AUTHORS`, `CRITICAL_INFERENCE`, `NOT_VERIFIABLE_IN_PDF`, and from 0B-02 onward `SECONDARY_CLAIM_UNVERIFIED`.
- Do not conflate classification, candidate retrieval, evidence retrieval, validation, explanation, or auditability.
- Missing group splitting does not prove leakage.
- Inherited references remain eligible regardless of age or publication type; the 2022–2026/Q1-Q2 rule applies to genuinely new academic literature under `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 3. Batches

#### 0B-01 — Direct HS classification and supervised learning

Status: **`APPROVED / FROZEN`**.

Canonical artifact: `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.

Review and approval:

- `article/reviews/0B01_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`;
- `article/reviews/0B01_AUTHOR_APPROVAL.md` — express author approval received.

The eight analyzed PDFs are the same eight listed in the Spanish section. F1–F5 remain `CANDIDATE_GAP_ONLY` and may be falsified or reformulated by later batches.

#### 0B-02 — Retrieval, validation, knowledge, and customs auditability

Status: **`READY_FOR_DRAFTING`**.

Active prompt: `article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`.

Assigned PDFs are the six works listed in the Spanish section: sentence retrieval, Text2Trade, explainable customs classification, HS-code correctness assessment, assistive technologies, and KBGAT/attribute knowledge.

The batch must distinguish retrieval types, validation/correction, structured knowledge, explainability, auditability, the exact role of HS/WCO/normative material, human support, uncertainty, traceability, and dependency controls. It must pressure-test F1–F5 and keep third-party claims as `SECONDARY_CLAIM_UNVERIFIED` until primary verification.

#### 0B-03 — LLMs, multimodality, and agents/hierarchical reasoning

Status: `NOT_STARTED`.

#### 0B-04 — Information Retrieval and RAG foundations

Status: `NOT_STARTED`.

#### 0B-05 — Data, documentation, provenance, reproducibility, knowledge, and normative sources

Status: `NOT_STARTED`.

#### 0B-06 — Directed search for new literature

Status: `NOT_STARTED`. Open only if the author-provided corpus reveals a real bibliographic gap.

### 4. Batch gate

`drafting AI -> internal scientific/editorial review -> correction if needed -> author approval -> freeze`

The experimental AI is not a mandatory literature reviewer; it is involved only when literature interpretation directly affects experimental facts, experimental claims, or methodological restrictions under its authority.

### 5. Current state

- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `OPEN`.
- 0B-01: `APPROVED / FROZEN`.
- Active block: `0B-02`.
- 0B-02 status: `READY_FOR_DRAFTING`.
- 0B-03 and later: `NOT_STARTED`.
- 0C: `BLOCKED` until 0B is closed.
- 0D: `BLOCKED` until 0C is closed.
- Target journal: pending until 0D.