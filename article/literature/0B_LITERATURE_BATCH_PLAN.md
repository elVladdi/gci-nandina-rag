# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta por lotes temáticos controlados. Su finalidad es leer PDF completos, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable para 0C. Durante 0B no se redacta Related Work ni se declara novelty o gap definitivo.

### 2. Corpus y reglas generales

- Corpus consolidado: `62` obras/documentos distintos, con acceso primario verificable `62/62`.
- Un PDF disponible fuera del lote activo permanece fuera de alcance.
- Cada PDF asignado debe leerse íntegramente.
- No se inventan metadatos, resultados, diseños, DOI, indexación ni estados editoriales.
- Metadata dudosa: `REVIEW_REQUIRED`.
- Distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`.
- Un claim que un paper atribuya a un tercero no se convierte en hecho independiente del manuscrito sin verificar la fuente primaria.
- No equiparar clasificación, candidate retrieval, evidence retrieval, validation, explanation, auditability ni correctness.
- Ausencia de group split documentado no demuestra leakage.
- `SUPPORTS_CANDIDATE` significa solo contraste compatible con supervivencia provisional dentro del lote; no evidencia de novelty.
- Las referencias heredadas conservan elegibilidad aunque sean antiguas o de distinto tipo documental. Para literatura académica nueva rige `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 3. Lotes

#### 0B-01 — Clasificación HS directa y aprendizaje supervisado

Estado: **`APPROVED / FROZEN`**.

Artefacto: `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.

#### 0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera

Estado: **`APPROVED / FROZEN`**.

Artefacto: `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.

#### 0B-03 — LLM, multimodalidad y agentes/razonamiento jerárquico

0B-03 se divide en dos sub-bloques para preservar lectura completa y auditoría independiente.

##### 0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:
`article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.

Registros:

- `article/reviews/0B03A_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`;
- `article/reviews/0B03A_AUTHOR_APPROVAL.md` — aprobación expresa recibida.

Hallazgos gobernantes:

- THE-RAG confirma que `RAG + LLM + HS classification` ya tiene antecedente directo y que RAG no mejora universalmente toda configuración.
- `gemini_1.5_flash` y `gemini_1.5_flash_8b` deben permanecer diferenciados.
- Koch & Power se clasifica operacionalmente como `FINE_TUNED_TRANSFORMER_CLASSIFIER`.
- ICCA-RAG es QA documental aduanero; document/section metadata y backtracking aportan procedencia técnica, no auditabilidad formal por candidato ni legal correctness.
- Gholamian et al. usa taxonomías Icecat/WDC-222, no HS; su papel es supporting para robustez/ICL.
- Amel et al.: +8.2 pp frente a D-only y +0.6 pp frente al mejor texto enriquecido; toda ganancia multimodal debe declarar baseline.

Candidatos tras 0B-03A, todos `CANDIDATE_GAP_ONLY`:

- F1/G1: `SURVIVES IN NARROW FORM`.
- F2/G2: `SURVIVES IN NARROW FORM`.
- F3/G3: `SURVIVES THIS BATCH; METHODOLOGICAL`.
- F4/G4: `SURVIVES AS METHODOLOGICAL DISTINCTION`.
- F5/G5: `FURTHER NARROWED BY ICCA-RAG`.
- G6: `SURVIVES; METHODOLOGICAL`.
- G7: `NEW/PROVISIONAL; PRESSURE TEST REQUIRED IN 0B-03B`.

##### 0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio

Estado: **`READY_FOR_DRAFTING`**.

Prompt activo:
`article/prompts/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING.md`.

PDF asignados:

1. `A Deterministic Agentic Workflow for HS Tariff Classification.pdf`
2. `ATLAS-Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification.pdf`
3. `Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification.pdf`
4. `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification.pdf`
5. `HSCodeComp- A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application.pdf`
6. `HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification.pdf`

Objetivos específicos:

- distinguir clasificación agentic, consensus, workflows deterministas, deep/hierarchical search, regulation-driven search y KG-guided reasoning;
- determinar si reglas/GIR/notas legales participan en la decisión del código o solo en evidencia posterior;
- identificar quién decide el código final;
- comprobar si existe Top-k previo fijado, si los agentes pueden introducir códigos externos o modificar el orden;
- auditar validation/guardrails/abstention/invalid-code filtering;
- distinguir reasoning trace/citations de auditabilidad formal;
- evaluar ground truth y adjudicación experta;
- revisar controles de dependencia sin inferir leakage por ausencia de group split;
- pressure-test F1–F5/G6/G7, especialmente G7;
- mantener separadas función científica y admisibilidad bibliográfica final.

Los otros 56 PDF permanecen `OUT_OF_SCOPE_FOR_0B03B`.

#### 0B-04 — Fundamentos de Information Retrieval y RAG

Estado: `NOT_STARTED`.

Previsto para BM25, DPR, HNSW, ColBERT, SBERT, RAG, reranking y fundamentos afines únicamente cuando respalden decisiones metodológicas concretas del artículo. Podrá incorporar antecedentes aplicados de embedding/retrieval que hayan quedado fuera de 0B-01/02/03.

#### 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Estado: `NOT_STARTED`.

Previsto para documentación de datasets, data statements, trazabilidad, reproducibilidad, gestión del conocimiento y fuentes normativas/oficiales requeridas por claims concretos.

#### 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si el corpus heredado revela un vacío bibliográfico real. Toda literatura académica realmente nueva deberá cumplir `article/BIBLIOGRAPHIC_FRAMEWORK.md`, salvo excepción expresa y documentada del autor.

### 4. Gate de cada lote/sub-lote

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

Gate vigente de 0B-03B:

`READY_FOR_DRAFTING -> entrega A–K -> revisión interna -> corrección si aplica -> aprobación del autor -> freeze -> evaluar apertura de 0B-04`.

La IA experimental no es revisora bibliográfica obligatoria. Se incorpora únicamente si una interpretación de literatura afecta directamente hechos experimentales, claims experimentales o restricciones metodológicas bajo su autoridad.

### 5. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01: `APPROVED / FROZEN`.
- 0B-02: `APPROVED / FROZEN`.
- 0B-03A: `APPROVED / FROZEN`.
- Bloque activo: `0B-03B`.
- 0B-03B: `READY_FOR_DRAFTING`.
- 0B-04 y posteriores: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: pendiente hasta 0D.

---

## English

### 1. Purpose

Phase `0B — Critical literature map and taxonomy` is executed through controlled thematic batches. Its purpose is full-PDF reading, precise task identification, and a comparable map for Phase 0C. No Related Work drafting, final novelty claim, or definitive gap is allowed during 0B.

### 2. Corpus and general rules

The consolidated corpus contains 62 distinct works/documents with primary verifiable access `62/62`. Only active-batch PDFs may be analyzed. Read every assigned PDF in full. Do not invent metadata, results, DOI, indexing, or publication status. Keep third-party claims unverified until their primary sources are checked. Missing grouped splits do not prove leakage. `SUPPORTS_CANDIDATE` means only provisional within-batch survival, never novelty evidence.

### 3. Batches

- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**. Canonical artifact: `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B`: **`READY_FOR_DRAFTING`**. Active prompt: `article/prompts/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING.md`.

0B-03B covers the six agentic/benchmark/hierarchical-regulatory papers listed in the Spanish section. It must distinguish agentic classification, consensus, deterministic workflows, hierarchical/regulation-driven search, KG-guided reasoning, rule use for code determination versus post-ranking evidence, candidate fixation/new-code capability/order changes, validation/guardrails, ground-truth quality, and formal auditability. It must pressure-test F1–F5/G6/G7 without novelty claims and separately report scientific function versus provisional bibliographic admissibility.

- `0B-04`: `NOT_STARTED`.
- `0B-05`: `NOT_STARTED`.
- `0B-06`: `NOT_STARTED`.

### 4. Gate

General gate: `drafting AI -> internal scientific/editorial review against primary PDFs -> correction if needed -> author approval -> freeze`.

Current 0B-03B gate: `READY_FOR_DRAFTING -> A–K deliverable -> internal review -> correction if needed -> author approval -> freeze -> assess opening 0B-04`.

Experimental-AI involvement is required only if a literature interpretation changes experimental facts, claims, or restrictions under its authority.

### 5. Current state

Phase 0A is closed/approved. Phase 0B is open. 0B-01, 0B-02, and 0B-03A are approved/frozen. The active block is 0B-03B (`READY_FOR_DRAFTING`). 0B-04 and later remain not started. 0C is blocked until 0B closes; 0D is blocked until 0C closes; target journal remains pending until 0D.
