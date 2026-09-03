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
- Se distinguen `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`.
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

#### 0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt ejecutado:

`article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`

Revisión interna:

`article/reviews/0B02_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**.

PDF analizados:

1. `Classification of Goods Using Text Descriptions With Sentences Retrieval.pdf`
2. `Text2Trade. A semantic search system whith Monte Carlo Droput Uncertainty Quantification For HS Code Retrieval..pdf`
3. `Explainable Product Classification for Customs.pdf`
4. `Application of machine learning for assessment of HS code correctness.pdf`
5. `Customs Tariff Classification and the Use of Assistive Technologies.pdf`
6. `Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities.pdf`

Hallazgos gobernantes de revisión:

- P01: la sentence retrieval del manual participa en la predicción HS6; test temporal efectivo 1,652, validación 1,835; HS6 Top-3 0.955 sin sentencias vs 0.937 con sentencias.
- P02 Text2Trade: `REVIEW_REQUIRED` por metadata; code retrieval con MNRL/MCD; sector analysis no constituye validación externa independiente.
- P03: candidate prediction + posterior HS-manual evidence retrieval constituye antecedente directo; el total 226,703 frente al split explícito 211,435 deja 15,268 registros sin disposición explícita; helpfulness cuerpo = 65.7 % (4–5), no 85 %; no hay medición causal de ahorro de tiempo.
- P04: correctness assessment presupone que las labels históricas son correctas; ≈84.23 % de scores 3–4 no equivale a detección adjudicada de misclasificación.
- P05: auditability/authoritative sources/file note aparecen explícitamente como requisitos prácticos; no es benchmark predictivo cuantitativo.
- P06: tarea formal de HS-code prediction/link completion; Recall impreso `TP/(TP+TN)` requiere caveat; CV por triples no demuestra independencia por mercancía/declaración ni leakage.

Estado provisional de candidatos tras 0B-02:

- F1: `CANDIDATE_GAP_ONLY — NARROWED`.
- F2: `CANDIDATE_GAP_ONLY — NARROWED`.
- F3: `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
- F4: `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION`.
- F5: `CANDIDATE_GAP_ONLY — NARROWED`.
- G6: `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM`.

Gate pendiente:

`aprobación expresa del autor -> integración de correcciones -> freeze 0B-02 -> apertura 0B-03`.

No es necesaria una nueva ejecución completa de la IA de redacción ni revisión de la IA experimental.

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
- Estado 0B-02: `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
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
- Third-party statements cited inside papers do not become independently verified manuscript facts without checking their primary sources.
- Distinguish `REPORTED_BY_AUTHORS`, `CRITICAL_INFERENCE`, `NOT_VERIFIABLE_IN_PDF`, and `SECONDARY_CLAIM_UNVERIFIED`.
- Do not conflate classification, candidate retrieval, evidence retrieval, validation, explanation, or auditability.
- Missing group splitting does not prove leakage.
- Inherited references remain eligible regardless of age or publication type; the 2022–2026/Q1-Q2 rule applies to genuinely new academic literature under `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 3. Batches

#### 0B-01 — Direct HS classification and supervised learning

Status: **`APPROVED / FROZEN`**.

Canonical artifact: `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.

Review and approval: `article/reviews/0B01_INTERNAL_REVIEW.md` (`PASS WITH MINOR CORRECTIONS`) and `article/reviews/0B01_AUTHOR_APPROVAL.md` (express approval received).

#### 0B-02 — Retrieval, validation, knowledge, and customs auditability

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Executed prompt: `article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`.

Internal review: `article/reviews/0B02_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**.

The six analyzed PDFs are the same six listed in the Spanish section.

Governing review findings:

- P01: HS-manual sentence retrieval participates in HS6 prediction; effective temporal test 1,652, validation 1,835; HS6 Top-3 0.955 without sentences versus 0.937 with sentences.
- P02 Text2Trade: metadata remains `REVIEW_REQUIRED`; it is code retrieval with MNRL/MCD; sector analysis is not independent external validation.
- P03: candidate prediction followed by HS-manual evidence retrieval is direct prior art; 226,703 total records versus 211,435 explicitly allocated leaves 15,268 records with no explicit disposition; body helpfulness = 65.7% scoring 4–5 rather than 85%; no causal time-saving measurement.
- P04: correctness assessment assumes historical labels are correct; ≈84.23% scores 3–4 is not independently adjudicated misclassification detection.
- P05: auditability, authoritative sources, and a retained file note are explicit practical requirements; the study is not a quantitative predictive benchmark.
- P06: formal task is HS-code prediction/link completion; printed Recall=`TP/(TP+TN)` requires a metric caveat; triple-level CV does not establish commodity/declaration independence or leakage.

Provisional candidate status after 0B-02:

- F1: `CANDIDATE_GAP_ONLY — NARROWED`.
- F2: `CANDIDATE_GAP_ONLY — NARROWED`.
- F3: `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
- F4: `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION`.
- F5: `CANDIDATE_GAP_ONLY — NARROWED`.
- G6: `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM`.

Pending gate: `express author approval -> integrate corrections -> freeze 0B-02 -> open 0B-03`.

A full drafting-AI rerun and experimental-AI review are not required.

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
- 0B-02 status: `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- 0B-03 and later: `NOT_STARTED`.
- 0C: `BLOCKED` until 0B closes.
- 0D: `BLOCKED` until 0C closes.
- Target journal: pending until 0D.
