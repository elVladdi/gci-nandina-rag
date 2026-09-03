# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecutará por lotes temáticos controlados. El objetivo no es redactar Related Work ni declarar novelty, sino leer los PDF completos del corpus disponible, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable que permita posteriormente definir el gap en 0C.

La literatura heredada conserva elegibilidad aunque incluya proceedings, tesis, preprints o trabajos anteriores a 2022. Las restricciones 2022–2026/Q1-Q2 aplican únicamente a literatura académica **nueva** incorporada después de detectar un vacío bibliográfico real.

### 2. Corpus PDF disponible para 0B

El autor ha informado y verificado que la IA de redacción dispone actualmente de un corpus consolidado de **62 obras/documentos distintos en PDF**, después de descontar copias repetidas y sufijos automáticos de adjunto.

El inventario informado se distribuye en tres familias amplias:

- clasificación HS, aduanas y clasificación de productos;
- recuperación de información, RAG y procesamiento de producto;
- metodología, reproducibilidad, conocimiento y normativa.

En el corte informado por el autor, `37/62` obras ya tienen entrada en el índice bibliográfico versionado de GitHub y `25/62` todavía no poseen entrada en ese índice. La ausencia de entrada en GitHub **no implica exclusión ni invalidez**: indica únicamente que su metadata/función bibliográfica todavía debe gobernarse y, cuando corresponda, registrarse mediante el flujo de 0B.

La disponibilidad de los 62 PDF **no autoriza analizarlos todos simultáneamente**. 0B mantiene lotes temáticos controlados para preservar trazabilidad, comparabilidad y calidad de lectura. Un PDF disponible pero no asignado al lote activo permanece `OUT_OF_SCOPE_FOR_CURRENT_BATCH` hasta que se abra el lote que le corresponda.

Los documentos adicionales podrán utilizarse en lotes posteriores cuando sean pertinentes. Su disponibilidad para lectura no equivale automáticamente a autorización de cita final: las referencias que no sean claramente heredadas del proyecto/tesis deberán cumplir la gobernanza de admisión definida en `article/BIBLIOGRAPHIC_FRAMEWORK.md` antes de incorporarse al manuscrito.

No es necesario volver a cargar un PDF si la IA de redacción ya puede acceder íntegramente a él en su conversación/sesión. Si un archivo deja de estar accesible o no puede leerse completo, deberá solicitarse únicamente ese archivo.

### 3. Reglas generales

- Cada PDF debe leerse íntegramente antes de clasificarlo como revisado.
- No se inferirán resultados, metadatos o diseños que el PDF no soporte.
- No se hará búsqueda abierta de literatura nueva durante los primeros lotes del corpus proporcionado por el autor.
- Los metadatos dudosos se marcarán `REVIEW_REQUIRED`.
- No se redactarán secciones del artículo durante 0B.
- No se declarará novelty ni gap definitivo antes de 0C.
- Cada trabajo se mapeará contra: problema, tarea, dataset/corpus, nivel HS, input, método, validación, métricas, jerarquía, evidencia normativa, explicabilidad, auditabilidad, precedentes históricos, LLM, limitaciones y diferencia con el presente trabajo.
- La existencia de otros PDF visibles en la conversación de la IA de redacción no permite usarlos para completar silenciosamente un lote: solo se analizan los documentos expresamente asignados al bloque activo.

### 4. Lotes previstos

#### 0B-01 — Clasificación HS directa y aprendizaje supervisado

Primer lote activo. Núcleo histórico de trabajos que tratan la asignación/clasificación de códigos HS mediante ML/DL/transfer learning/representaciones de texto.

PDF asignados al lote:

1. `Best approaches for HS code prediction.pdf`
2. `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
3. `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
4. `Automatic Tariff Classification System using Deep Learning.pdf`
5. `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
6. `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
7. `Application of machine learning for automated HS-6 code assignment.pdf`
8. `Auto-Categorization of HS Code Using Background Net Approach.pdf`

Estos ocho forman el alcance analítico de 0B-01 aunque la IA de redacción tenga acceso simultáneo a los demás PDF del corpus de 62.

#### 0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera

Previsto para el segundo lote. Incluirá, entre otros, trabajos sobre sentence retrieval, Text2Trade, explainable product classification, assessment/correction of HS-code correctness, assistive technologies y conocimiento estructurado. La selección concreta se hará a partir del corpus de 62 ya disponible y podrá ampliarse o dividirse si el volumen compromete una lectura completa y comparable.

#### 0B-03 — LLM, multimodalidad y agentes/razonamiento jerárquico

Previsto para el tercer lote. Incluirá trabajos disponibles centrados en LLM para clasificación/compliance, RAG aduanero, agentes, multimodalidad y benchmarks/razonamiento jerárquico. La admisibilidad final de trabajos no heredados se resolverá conforme a `BIBLIOGRAPHIC_FRAMEWORK.md`.

#### 0B-04 — Fundamentos de Information Retrieval y RAG

Previsto para BM25, DPR, HNSW, ColBERT, SBERT, RAG y otros fundamentos disponibles, únicamente en la medida en que respalden decisiones metodológicas concretas del artículo.

#### 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Previsto para referencias fundacionales/metodológicas y fuentes oficiales sobre documentación de datasets, data statements, trazabilidad, reproducibilidad, gestión del conocimiento y reglas/normativa aduanera cuando resulten necesarias para claims concretos.

#### 0B-06 — Búsqueda dirigida de literatura nueva

Solo se abrirá si el corpus proporcionado por el autor revela vacíos concretos. Toda referencia académica realmente nueva deberá cumplir `article/BIBLIOGRAPHIC_FRAMEWORK.md`: ventana 2022–2026, journal peer-reviewed, Q1 preferido/Q2 excepcionalmente justificado, PDF completo legítimo, DOI/identificador estable y relevancia directa, salvo autorización expresa del autor para una excepción documentada.

### 5. Gate de cada lote

Cada lote sigue la secuencia:

`IA de redacción -> revisión científica/editorial interna -> corrección si aplica -> aprobación del autor`.

La IA experimental no es revisora obligatoria de literatura; solo se solicitará su intervención si una interpretación bibliográfica afecta directamente un hecho experimental, un claim experimental o una restricción metodológica bajo su autoridad.

### 6. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- Corpus PDF conocido disponible para la IA de redacción: `62` obras/documentos distintos.
- Bloque activo: `0B-01`.
- Estado 0B-01: `READY_FOR_DRAFTING`.
- Alcance de 0B-01: únicamente los ocho PDF asignados en §4.
- 0C y posteriores: bloqueados.
- Target journal: pendiente hasta 0D.

---

## English

### 1. Purpose

Phase `0B — Critical literature map and taxonomy` will be executed through controlled thematic batches. The goal is not to draft Related Work or declare novelty, but to read complete PDFs from the available corpus, identify the actual problem solved by each work, and build a comparable map that can later support gap definition in 0C.

Inherited literature remains eligible even when it includes proceedings, theses, preprints, or works published before 2022. The 2022–2026/Q1-Q2 restrictions apply only to **new** academic literature added after a genuine bibliographic gap has been identified.

### 2. PDF corpus available for 0B

The author has reported and verified that the drafting AI currently has access to a consolidated corpus of **62 distinct works/documents in PDF**, after removing duplicate uploads and automatic attachment suffixes.

The reported inventory spans three broad families:

- HS classification, customs, and product classification;
- information retrieval, RAG, and product processing;
- methodology, reproducibility, knowledge, and normative sources.

At the author-reported cutoff, `37/62` works already have an entry in the versioned GitHub bibliographic index and `25/62` do not yet have such an entry. Missing GitHub indexing **does not imply exclusion or invalidity**; it only means that metadata/bibliographic function still needs to be governed and, when appropriate, registered through the 0B workflow.

Availability of all 62 PDFs **does not authorize analyzing them all at once**. Phase 0B retains controlled thematic batches to preserve traceability, comparability, and full-reading quality. A PDF that is available but not assigned to the active batch remains `OUT_OF_SCOPE_FOR_CURRENT_BATCH` until its batch is opened.

Additional documents may be used in later batches when relevant. Read availability does not automatically authorize final citation: references that are not clearly inherited from the project/thesis must satisfy the admission governance in `article/BIBLIOGRAPHIC_FRAMEWORK.md` before manuscript use.

A PDF need not be uploaded again if the drafting AI can already access it in full in its current conversation/session. If access is lost or a file cannot be read completely, only that specific file should be requested.

### 3. General rules

- Each PDF must be read in full before being classified as reviewed.
- Results, metadata, or designs not supported by the PDF must not be inferred.
- No open-ended search for new literature will be performed during the initial author-provided corpus batches.
- Uncertain metadata must be marked `REVIEW_REQUIRED`.
- No manuscript sections will be drafted during 0B.
- No novelty or definitive gap will be declared before 0C.
- Each work will be mapped against: problem, task, dataset/corpus, HS level, input, method, validation, metrics, hierarchy, normative evidence, explainability, auditability, historical precedents, LLM use, limitations, and difference from the present work.
- Visibility of other PDFs in the drafting-AI conversation does not allow them to be used to silently fill gaps in the current batch: only documents explicitly assigned to the active block may be analyzed.

### 4. Planned batches

#### 0B-01 — Direct HS classification and supervised learning

First active batch. Historical core of works addressing HS-code assignment/classification through ML/DL/transfer learning/text representations.

Assigned PDFs:

1. `Best approaches for HS code prediction.pdf`
2. `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
3. `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
4. `Automatic Tariff Classification System using Deep Learning.pdf`
5. `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
6. `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
7. `Application of machine learning for automated HS-6 code assignment.pdf`
8. `Auto-Categorization of HS Code Using Background Net Approach.pdf`

These eight define the analytical scope of 0B-01 even if the drafting AI can simultaneously access the remaining PDFs in the 62-document corpus.

#### 0B-02 — Retrieval, validation, knowledge, and customs auditability

Planned as the second batch. It will include sentence retrieval, Text2Trade, explainable product classification, HS-code correctness assessment/correction, assistive technologies, and structured-knowledge work. The concrete selection will be drawn from the already available 62-document corpus and may be split further if volume would compromise full and comparable reading.

#### 0B-03 — LLMs, multimodality, and agents/hierarchical reasoning

Planned as the third batch. It will include available work on LLM-based classification/compliance, customs RAG, agents, multimodality, and hierarchical-search/reasoning benchmarks. Final admissibility of non-inherited works will be governed by `BIBLIOGRAPHIC_FRAMEWORK.md`.

#### 0B-04 — Information Retrieval and RAG foundations

Planned for BM25, DPR, HNSW, ColBERT, SBERT, RAG, and other available foundations only insofar as they support concrete methodological decisions in the article.

#### 0B-05 — Data, documentation, provenance, reproducibility, knowledge, and normative sources

Planned for foundational/methodological references and official sources on dataset documentation, data statements, traceability, reproducibility, knowledge management, and customs rules/normative material when required for concrete claims.

#### 0B-06 — Directed search for new literature

This will open only if the author-provided corpus reveals concrete gaps. Every genuinely new academic reference must satisfy `article/BIBLIOGRAPHIC_FRAMEWORK.md`: 2022–2026 window, peer-reviewed journal, Q1 preferred/Q2 exceptionally justified, legitimate full PDF, DOI/stable identifier, and direct relevance, unless the author expressly approves a documented exception.

### 5. Gate for each batch

Each batch follows:

`drafting AI -> internal scientific/editorial review -> correction if needed -> author approval`.

The experimental AI is not a mandatory literature reviewer; it will only be involved when a bibliographic interpretation directly affects an experimental fact, experimental claim, or methodological restriction under its authority.

### 6. Current state

- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `OPEN`.
- Known PDF corpus available to the drafting AI: `62` distinct works/documents.
- Active block: `0B-01`.
- 0B-01 status: `READY_FOR_DRAFTING`.
- 0B-01 scope: only the eight PDFs assigned in §4.
- 0C and later phases: blocked.
- Target journal: pending until 0D.
