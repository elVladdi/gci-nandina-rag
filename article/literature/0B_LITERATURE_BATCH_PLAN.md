# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecutará por lotes temáticos controlados. El objetivo no es redactar Related Work ni declarar novelty, sino leer los PDF completos del corpus heredado, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable que permita posteriormente definir el gap en 0C.

La literatura heredada conserva elegibilidad aunque incluya proceedings, tesis, preprints o trabajos anteriores a 2022. Las restricciones 2022–2026/Q1-Q2 aplican únicamente a literatura académica **nueva** incorporada después de detectar un vacío bibliográfico real.

### 2. Reglas generales

- Cada PDF debe leerse íntegramente antes de clasificarlo como revisado.
- No se inferirán resultados, metadatos o diseños que el PDF no soporte.
- No se hará búsqueda abierta de literatura nueva durante los primeros lotes heredados.
- Los metadatos dudosos se marcarán `REVIEW_REQUIRED`.
- No se redactarán secciones del artículo durante 0B.
- No se declarará novelty ni gap definitivo antes de 0C.
- Cada trabajo se mapeará contra: problema, tarea, dataset/corpus, nivel HS, input, método, validación, métricas, jerarquía, evidencia normativa, explicabilidad, auditabilidad, precedentes históricos, LLM, limitaciones y diferencia con el presente trabajo.

### 3. Lotes previstos

#### 0B-01 — Clasificación HS directa y aprendizaje supervisado

Primer lote activo. Núcleo histórico de trabajos que tratan la asignación/clasificación de códigos HS mediante ML/DL/transfer learning/representaciones de texto.

PDF requeridos:

1. `Best approaches for HS code prediction.pdf`
2. `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
3. `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
4. `Automatic Tariff Classification System using Deep Learning.pdf`
5. `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
6. `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
7. `Application of machine learning for automated HS-6 code assignment.pdf`
8. `Auto-Categorization of HS Code Using Background Net Approach.pdf`

#### 0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera

Previsto para el segundo lote. Incluirá, entre otros, trabajos sobre sentence retrieval, Text2Trade, explainable product classification, assessment/correction of HS-code correctness, assistive technologies y conocimiento estructurado.

#### 0B-03 — LLM, multimodalidad y agentes/razonamiento jerárquico

Previsto para el tercer lote. Incluirá trabajos heredados centrados en LLM para clasificación/compliance, multimodalidad y benchmarks/agentes de búsqueda jerárquica.

#### 0B-04 — Fundamentos de Information Retrieval

Previsto para DPR, HNSW y ColBERT, únicamente en la medida en que respalden decisiones metodológicas concretas del artículo.

#### 0B-05 — Datos, documentación, procedencia y reproducibilidad

Previsto para referencias fundacionales/metodológicas sobre documentación de datasets, data statements, trazabilidad y reproducibilidad que resulten necesarias para claims concretos.

#### 0B-06 — Búsqueda dirigida de literatura nueva

Solo se abrirá si los lotes heredados revelan vacíos concretos. Toda nueva referencia deberá cumplir `article/BIBLIOGRAPHIC_FRAMEWORK.md`: ventana 2022–2026, journal peer-reviewed, Q1 preferido/Q2 excepcionalmente justificado, PDF completo legítimo, DOI/identificador estable y relevancia directa.

### 4. Gate de cada lote

Cada lote sigue la secuencia:

`IA de redacción -> revisión científica/editorial interna -> corrección si aplica -> aprobación del autor`.

La IA experimental no es revisora obligatoria de literatura; solo se solicitará su intervención si una interpretación bibliográfica afecta directamente un hecho experimental, un claim experimental o una restricción metodológica bajo su autoridad.

### 5. Estado inicial

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- Bloque activo: `0B-01`.
- Estado 0B-01: `READY_FOR_DRAFTING`.
- 0C y posteriores: bloqueados.
- Target journal: pendiente hasta 0D.

---

## English

### 1. Purpose

Phase `0B — Critical literature map and taxonomy` will be executed through controlled thematic batches. The goal is not to draft Related Work or declare novelty, but to read the complete PDFs in the inherited corpus, identify the actual problem solved by each work, and build a comparable map that can later support gap definition in 0C.

Inherited literature remains eligible even when it includes proceedings, theses, preprints, or works published before 2022. The 2022–2026/Q1-Q2 restrictions apply only to **new** academic literature added after a genuine bibliographic gap has been identified.

### 2. General rules

- Each PDF must be read in full before being classified as reviewed.
- Results, metadata, or designs not supported by the PDF must not be inferred.
- No open-ended search for new literature will be performed during the initial inherited-corpus batches.
- Uncertain metadata must be marked `REVIEW_REQUIRED`.
- No manuscript sections will be drafted during 0B.
- No novelty or definitive gap will be declared before 0C.
- Each work will be mapped against: problem, task, dataset/corpus, HS level, input, method, validation, metrics, hierarchy, normative evidence, explainability, auditability, historical precedents, LLM use, limitations, and difference from the present work.

### 3. Planned batches

#### 0B-01 — Direct HS classification and supervised learning

First active batch. Historical core of works addressing HS-code assignment/classification through ML/DL/transfer learning/text representations.

Required PDFs:

1. `Best approaches for HS code prediction.pdf`
2. `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
3. `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
4. `Automatic Tariff Classification System using Deep Learning.pdf`
5. `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
6. `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
7. `Application of machine learning for automated HS-6 code assignment.pdf`
8. `Auto-Categorization of HS Code Using Background Net Approach.pdf`

#### 0B-02 — Retrieval, validation, knowledge, and customs auditability

Planned as the second batch. It will include sentence-retrieval work, Text2Trade, explainable product classification, HS-code correctness assessment/correction, assistive technologies, and structured-knowledge approaches.

#### 0B-03 — LLMs, multimodality, and agents/hierarchical reasoning

Planned as the third batch. It will include inherited work focused on LLM-based classification/compliance, multimodal approaches, and hierarchical-search/agent benchmarks.

#### 0B-04 — Information Retrieval foundations

Planned for DPR, HNSW, and ColBERT, only insofar as they support concrete methodological decisions in the article.

#### 0B-05 — Data, documentation, provenance, and reproducibility

Planned for foundational/methodological references on dataset documentation, data statements, traceability, and reproducibility when required for concrete claims.

#### 0B-06 — Directed search for new literature

This will open only if inherited-corpus batches reveal concrete gaps. Every new reference must satisfy `article/BIBLIOGRAPHIC_FRAMEWORK.md`: 2022–2026 window, peer-reviewed journal, Q1 preferred/Q2 exceptionally justified, legitimate full PDF, DOI/stable identifier, and direct relevance.

### 4. Gate for each batch

Each batch follows:

`drafting AI -> internal scientific/editorial review -> correction if needed -> author approval`.

The experimental AI is not a mandatory literature reviewer; it will only be involved when a bibliographic interpretation directly affects an experimental fact, experimental claim, or methodological restriction under its authority.

### 5. Initial state

- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `OPEN`.
- Active block: `0B-01`.
- 0B-01 status: `READY_FOR_DRAFTING`.
- 0C and later phases: blocked.
- Target journal: pending until 0D.
