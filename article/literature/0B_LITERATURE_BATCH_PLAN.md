# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta por lotes temáticos controlados. Su finalidad es leer PDF completos, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable para 0C. Durante 0B no se redacta Related Work ni se declara novelty o gap definitivo.

### 2. Corpus y reglas generales

- Corpus consolidado: `62` obras/documentos distintos, con acceso primario verificable `62/62`.
- Un PDF disponible fuera del lote activo permanece fuera de alcance.
- Cada PDF debe leerse íntegramente.
- No se inventan metadatos, resultados, diseños, DOI ni estados editoriales.
- Metadata dudosa: `REVIEW_REQUIRED`.
- Distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`.
- Un claim que un paper atribuya a un tercero no se convierte en hecho independiente del manuscrito sin verificar la fuente primaria.
- No equiparar clasificación, candidate retrieval, evidence retrieval, validation, explanation, auditability ni correctness.
- Ausencia de group split documentado no demuestra leakage.
- Las referencias heredadas conservan elegibilidad aunque sean antiguas, proceedings, working papers, tesis o preprints. Las reglas 2022–2026/Q1-Q2 aplican a literatura académica nueva conforme a `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 3. Lotes

#### 0B-01 — Clasificación HS directa y aprendizaje supervisado

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:
`article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`

Registros:
- `article/reviews/0B01_INTERNAL_REVIEW.md`;
- `article/reviews/0B01_AUTHOR_APPROVAL.md`.

#### 0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:
`article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`

Registros:
- `article/reviews/0B02_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`;
- `article/reviews/0B02_AUTHOR_APPROVAL.md` — aprobación expresa recibida.

Hallazgos gobernantes:
- P01: sentence retrieval del manual participa en predicción HS6; test efectivo 1,652; Top-3 0.955 sin sentencias vs 0.937 con sentencias.
- P02/Text2Trade: `REVIEW_REQUIRED`; sector analysis no es validación externa independiente.
- P03: candidate prediction + evidence retrieval del manual HS es antecedente directo; 15,268 registros quedan sin disposición explícita; helpfulness operativo 65.7%, no 85%; claims de tiempo/esfuerzo son perceptuales.
- P04: correctness assessment presupone labels históricos correctos; ≈84.23% no es detección adjudicada de misclasificación real.
- P05: authoritative sources, file note y auditability aparecen explícitamente; no es benchmark predictivo.
- P06: Recall impreso `TP/(TP+TN)` exige caveat; CV por triples no demuestra independencia por mercancía/declaración ni leakage.

Candidatos tras 0B-02:
- F1: `CANDIDATE_GAP_ONLY — NARROWED`.
- F2: `CANDIDATE_GAP_ONLY — NARROWED`.
- F3: `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
- F4: `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION`.
- F5: `CANDIDATE_GAP_ONLY — NARROWED`.
- G6: `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM`.

#### 0B-03 — LLM, multimodalidad y agentes/razonamiento jerárquico

Por volumen y para preservar lectura completa y auditoría independiente, 0B-03 se divide en dos sub-bloques controlados.

##### 0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt ejecutado:
`article/prompts/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS.md`

Revisión interna:
`article/reviews/0B03A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**.

Revisión experimental: `NOT_REQUIRED`.

PDF analizados:

1. `Automatic product classification in international trade Machine learning and large language models.pdf`
2. `Automating Harmonized System (HS) Code Classification from Unstructured Shipping Manifests using Large Language Models.pdf`
3. `Development of an Automated HS Code Classification System Using LLM Based on an Optimized RAG Framework.pdf`
4. `ICCA-RAG Intelligent Customs Clearance Assistant Using RAG.pdf`
5. `LLM-based robust product classification in commerce and compliance.pdf`
6. `Multimodal approach for Harmonized System code prediction.pdf`

Hallazgos gobernantes tras revisión primaria:

- THE-RAG constituye antecedente directo de `RAG_CLASSIFICATION` en HS; el LLM participa en la decisión final y RAG no mejora universalmente todas las configuraciones.
- ICCA-RAG es `customs-document QA/RAG`, no benchmark de clasificación HS. Su metadata/backtracking aporta procedencia técnica, pero no demuestra auditabilidad formal por candidato ni corrección jurídica.
- Koch & Power debe distinguirse como `FINE_TUNED_TRANSFORMER_CLASSIFIER`, aunque los autores usen la etiqueta LLM.
- Gholamian et al. estudia Icecat/WDC-222, no HS; su utilidad es supporting para robustez, perturbaciones e ICL.
- Amel et al. demuestra que el efecto multimodal depende del baseline: +8.2 pp contra `D-only`, pero solo +0.6 pp frente al mejor texto enriquecido en Top-1.

Correcciones editoriales obligatorias para el futuro freeze:

1. separar `gemini_1.5_flash` de `gemini_1.5_flash_8b` en THE-RAG;
2. normalizar la taxonomía de Koch & Power;
3. calificar la función de evidencia de ICCA-RAG como contexto de QA y no evidencia post-ranking de candidatos fijos;
4. no generalizar el estudio humano de Gholamian a beneficio humano de clasificación HS;
5. interpretar `SUPPORTS_CANDIDATE` como contraste provisional del lote, no como evidencia de novelty;
6. mantener siempre el baseline exacto de los efectos multimodales.

Candidatos tras revisión 0B-03A:
- F1/G1: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- F2/G2: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- F3/G3: `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH; METHODOLOGICAL`.
- F4/G4: `CANDIDATE_GAP_ONLY — SURVIVES AS METHODOLOGICAL DISTINCTION`.
- F5/G5: `CANDIDATE_GAP_ONLY — FURTHER NARROWED BY ICCA-RAG`.
- G6: `CANDIDATE_GAP_ONLY — SURVIVES; METHODOLOGICAL`.
- G7: `CANDIDATE_GAP_ONLY — NEW/PROVISIONAL; PRESSURE TEST REQUIRED IN 0B-03B`.

No se requiere rerun de la IA de redacción. La aprobación expresa del autor es el único gate pendiente antes de integrar las correcciones y congelar 0B-03A.

##### 0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio

Estado: `NOT_STARTED`.

Se abrirá solo después de aprobar y congelar 0B-03A. Lote previsto:

1. `A Deterministic Agentic Workflow for HS Tariff Classification.pdf`
2. `ATLAS-Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification.pdf`
3. `Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification.pdf`
4. `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification.pdf`
5. `HSCodeComp- A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application.pdf`
6. `HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification.pdf`

El nombre exacto del archivo puede variar por sufijo automático; la identidad científica se determina por el contenido.

#### 0B-04 — Fundamentos de Information Retrieval y RAG

Estado: `NOT_STARTED`.

Previsto para BM25, DPR, HNSW, ColBERT, SBERT, RAG, reranking y otros fundamentos únicamente cuando respalden decisiones metodológicas concretas del artículo. También puede incorporar antecedentes aplicados de embedding/retrieval que hayan quedado fuera de 0B-01/02/03.

#### 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Estado: `NOT_STARTED`.

Previsto para documentación de datasets, data statements, trazabilidad, reproducibilidad, gestión de conocimiento y fuentes normativas/oficiales requeridas por claims concretos.

#### 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si los lotes del corpus heredado revelan un vacío bibliográfico real. Toda literatura académica realmente nueva deberá cumplir `article/BIBLIOGRAPHIC_FRAMEWORK.md`, salvo excepción expresa y documentada del autor.

### 4. Gate de cada lote/sub-lote

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

Para 0B-03A, la revisión interna ya terminó. Gate vigente:

`AUTHOR_APPROVAL_PENDING -> aprobación expresa -> integrar C1–C6 -> freeze -> abrir 0B-03B`.

La IA experimental no es revisora bibliográfica obligatoria. Se solicita únicamente si una interpretación bibliográfica afecta directamente hechos experimentales, claims experimentales o restricciones metodológicas bajo su autoridad.

### 5. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01: `APPROVED / FROZEN`.
- 0B-02: `APPROVED / FROZEN`.
- Bloque activo: `0B-03A`.
- 0B-03A: `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- 0B-03B y posteriores: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: pendiente hasta 0D.

---

## English

### 1. Purpose

Phase `0B — Critical literature map and taxonomy` is executed through controlled thematic batches. The purpose is full-PDF reading, precise task identification, and a comparable map for Phase 0C. No Related Work drafting, final novelty claim, or definitive gap is allowed during 0B.

### 2. Corpus and general rules

- Consolidated corpus: 62 distinct works/documents with primary verifiable access `62/62`.
- A visible PDF outside the active batch remains out of scope.
- Read every assigned PDF in full.
- Do not invent metadata, results, designs, DOI, or publication status.
- Uncertain metadata: `REVIEW_REQUIRED`.
- Distinguish `REPORTED_BY_AUTHORS`, `CRITICAL_INFERENCE`, `NOT_VERIFIABLE_IN_PDF`, and `SECONDARY_CLAIM_UNVERIFIED`.
- Third-party claims cited by papers do not become independent manuscript facts without primary-source verification.
- Do not conflate classification, candidate retrieval, evidence retrieval, validation, explanation, auditability, or correctness.
- Missing grouped splits do not prove leakage.
- Inherited references remain eligible regardless of age/publication type; 2022–2026/Q1-Q2 rules apply to genuinely new academic literature under the bibliographic framework.

### 3. Batches

#### 0B-01
Status: **`APPROVED / FROZEN`**. Canonical artifact: `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.

#### 0B-02
Status: **`APPROVED / FROZEN`**. Canonical artifact: `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`. Internal review passed with minor corrections and express author approval was received.

#### 0B-03A — LLM, RAG, and multimodality in customs classification/compliance

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Internal review: `article/reviews/0B03A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**.

Experimental review: `NOT_REQUIRED`.

The six assigned PDFs were analyzed. Governing findings after primary verification: THE-RAG is direct prior art for RAG-based HS classification and its LLM participates in code determination; ICCA-RAG is customs-document QA rather than an HS-classification benchmark; Koch & Power operationally use fine-tuned transformer encoders as closed-label classifiers; Gholamian et al. do not evaluate HS codes; and Amel et al.'s multimodal effect is baseline-dependent.

Required freeze corrections: preserve exact THE-RAG model identity; normalize Koch & Power's operational taxonomy; qualify ICCA-RAG's evidence role; narrow interpretation of Gholamian's human experiment; define pressure-test labels as provisional contrast rather than novelty evidence; and always state the exact multimodal baseline.

Candidate status remains provisional: F1/F2 survive only narrowly; F3/G6 remain methodological; F4 remains a methodological distinction; F5 is further narrowed by ICCA-RAG; and G7 is new/provisional and must be pressure-tested in 0B-03B. All remain `CANDIDATE_GAP_ONLY`.

No drafting-AI rerun is required. Express author approval is the only pending gate before editorially integrating C1–C6 and creating the canonical freeze.

#### 0B-03B — Agents, benchmarks, and hierarchical/regulatory reasoning
Status: `NOT_STARTED`; it opens only after 0B-03A is approved and frozen.

#### 0B-04 — Information Retrieval and RAG foundations
Status: `NOT_STARTED`.

#### 0B-05 — Data, documentation, provenance, reproducibility, knowledge, and normative sources
Status: `NOT_STARTED`.

#### 0B-06 — Directed search for new literature
Status: `NOT_STARTED`. Open only if the inherited corpus reveals a real bibliographic gap.

### 4. Gate

General gate: `drafting AI -> internal scientific/editorial review against primary PDFs -> correction if needed -> author approval -> freeze`.

Current 0B-03A gate: `AUTHOR_APPROVAL_PENDING -> express approval -> integrate C1–C6 -> freeze -> open 0B-03B`.

The experimental AI is involved only when a literature interpretation directly affects experimental facts, claims, or restrictions under its authority.

### 5. Current state

- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `OPEN`.
- 0B-01: `APPROVED / FROZEN`.
- 0B-02: `APPROVED / FROZEN`.
- Active block: `0B-03A`.
- 0B-03A: `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- 0B-03B and later: `NOT_STARTED`.
- 0C: `BLOCKED` until 0B closes.
- 0D: `BLOCKED` until 0C closes.
- Target journal: pending until 0D.
