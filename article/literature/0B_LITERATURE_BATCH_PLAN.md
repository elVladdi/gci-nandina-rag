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

##### 0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero

Estado: **`APPROVED / FROZEN`**.

Artefacto: `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.

##### 0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:

`article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`

Registros:

- `article/reviews/0B03B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`;
- `article/reviews/0B03B_AUTHOR_APPROVAL.md` — aprobación expresa recibida.

Hallazgos gobernantes:

- Los sistemas agentic/regulatorios recientes son heterogéneos: workflows deterministas, consenso multiagente, búsqueda jerárquica/regulatoria, deep-search benchmarks y knowledge-graph-guided classification.
- En varios antecedentes, reglas/normativa/jerarquía participan en la decisión del código; no equivalen a evidencia normativa posterior a un ranking histórico inmutable.
- Wang et al. ya separa una hierarchy path fijada de una fase final de evidence aggregation/rationale. Por ello F2 solo sobrevive en una versión más estricta: **ranking Top-k externo fijado por un componente previo independiente + generador exclusivamente explicativo sin capacidad de introducir/eliminar/sustituir/reordenar códigos ni retroalimentar clasificación**.
- HSCodeComp falsifica G6 amplio como candidato a gap al aportar anotación experta con adjudicación/control. G6 se conserva solo como principio metodológico de calidad del ground truth.
- P01/P04/P06 ya aportan rutas, evidencia, citas o traces; F5 solo sobrevive como evaluación formal, explícita y separada de auditabilidad documental por salida.
- `legally valid path`/path validity/cumplimiento de restricciones codificadas no equivalen a corrección jurídica independiente.
- Claims de leakage sobre benchmarks previos permanecen `SECONDARY_CLAIM_UNVERIFIED` hasta auditoría primaria directa.
- G7 se absorbe en F2 y deja de ser candidato independiente.

Candidatos después de 0B-03B:

- F1/G1: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- F2/G2: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- F3/G3: `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- F4/G4: `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- F5/G5: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- G6: `ELIMINATED AS GAP CANDIDATE`; ground-truth quality remains methodological.
- G7: `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

Ninguno constituye novelty ni gap definitivo.

#### 0B-04 — Fundamentos de Information Retrieval y RAG

Estado: `NOT_STARTED`.

Previsto para BM25, DPR, HNSW, ColBERT, SBERT, RAG, reranking y fundamentos afines únicamente cuando respalden decisiones metodológicas concretas del artículo. Podrá incorporar antecedentes aplicados de embedding/retrieval que hayan quedado fuera de 0B-01/02/03.

La apertura formal de 0B-04 debe definir un lote controlado y un prompt propio antes de su ejecución. No se abre automáticamente por el mero cierre de 0B-03B.

#### 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Estado: `NOT_STARTED`.

Previsto para documentación de datasets, data statements, trazabilidad, reproducibilidad, gestión del conocimiento y fuentes normativas/oficiales requeridas por claims concretos.

#### 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si el corpus heredado revela un vacío bibliográfico real. Toda literatura académica realmente nueva deberá cumplir `article/BIBLIOGRAPHIC_FRAMEWORK.md`, salvo excepción expresa y documentada del autor.

### 4. Gate de cada lote/sub-lote

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

0B-03B ya completó ese gate y está congelado.

Próximo gate potencial:

`definir alcance 0B-04 -> crear prompt controlado -> READY_FOR_DRAFTING -> ejecución por IA de redacción -> revisión interna -> aprobación del autor -> freeze`.

La IA experimental no es revisora bibliográfica obligatoria. Se incorpora únicamente si una interpretación de literatura afecta directamente hechos experimentales, claims experimentales o restricciones metodológicas bajo su autoridad.

### 5. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01: `APPROVED / FROZEN`.
- 0B-02: `APPROVED / FROZEN`.
- 0B-03A: `APPROVED / FROZEN`.
- 0B-03B: `APPROVED / FROZEN`.
- 0B-04, 0B-05 y 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: pendiente hasta 0D.

---

## English

### 1. Purpose

Phase `0B — Critical literature map and taxonomy` is executed through controlled thematic batches. Its purpose is full-PDF reading, precise task identification, and a comparable map for Phase 0C. No Related Work drafting, final novelty claim, or definitive gap is allowed during 0B.

### 2. Corpus and general rules

The consolidated corpus contains 62 distinct works/documents with primary verifiable access `62/62`. Only active-batch PDFs may be analyzed. Read each assigned PDF in full. Do not invent metadata, results, DOI, indexing, or publication status. Third-party claims remain unverified until their primary sources are checked. Missing grouped splits do not prove leakage. `SUPPORTS_CANDIDATE` means only provisional within-batch survival, never novelty evidence.

### 3. Batches

- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**. Canonical artifact: `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.

0B-03B freezes the following governing conclusions: recent agentic/regulatory HS systems already include deterministic workflows, multi-agent consensus, hierarchical/regulation-driven search, deep-search benchmarks, and KG-guided reasoning; rules often participate directly in classification rather than merely supporting a fixed ranking; Wang et al. already separates a fixed path from downstream evidence/rationale; HSCodeComp eliminates broad G6 through expert adjudication/control; traceable paths/citations/traces already exist, narrowing F5 to formal separate auditability evaluation; and G7 is merged into F2.

Provisional candidates after 0B-03B are F1 narrow, F2 further narrowed, F3 with applicability caveat, F4 as methodological distinction, and F5 further narrowed. G6 is eliminated as a gap candidate and G7 is merged into F2. None establishes novelty or a final gap.

- `0B-04`: `NOT_STARTED`.
- `0B-05`: `NOT_STARTED`.
- `0B-06`: `NOT_STARTED`.

0B-04 will cover IR/RAG foundations only where they support concrete methodological decisions. Its formal opening requires a controlled batch definition and its own prompt; closure of 0B-03B does not automatically open it.

### 4. Gate

General gate: `drafting AI -> internal scientific/editorial review against primary PDFs -> correction if needed -> author approval -> freeze`.

0B-03B has completed this gate. The next potential gate is `define 0B-04 scope -> create controlled prompt -> READY_FOR_DRAFTING -> drafting execution -> internal review -> author approval -> freeze`.

Experimental-AI involvement is required only if a literature interpretation changes experimental facts, claims, or restrictions under its authority.

### 5. Current state

Phase 0A is closed/approved. Phase 0B remains open. 0B-01, 0B-02, 0B-03A, and 0B-03B are approved/frozen. 0B-04 through 0B-06 remain not started. 0C is blocked until 0B closes; 0D is blocked until 0C closes; target journal remains pending until 0D.
