# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito y reglas generales

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta mediante lotes temáticos controlados. Su finalidad es leer fuentes primarias completas, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable para 0C. Durante 0B no se redacta el manuscrito ni se declara novelty o gap definitivo.

Reglas gobernantes:

- corpus consolidado: `62` obras/documentos distintos, acceso primario verificable `62/62`;
- lectura íntegra y auditoría claim-source-scope obligatorias;
- no inventar metadata, DOI, resultados, indexación o estado editorial;
- distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `OPERACIONALIZACION_DEL_PROYECTO`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED` cuando corresponda;
- una afirmación secundaria no se convierte en hecho independiente sin verificar su fuente primaria;
- no equiparar classification, candidate retrieval, evidence retrieval, reranking, explanation, provenance, reproducibility, auditability ni correctness;
- no imponer DIKW universal ni transformar automáticamente data→information→knowledge;
- `SUPPORTS_CANDIDATE` nunca significa novelty;
- fuentes heredadas conservan elegibilidad; literatura académica nueva se rige por `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 2. Bloques cerrados

- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**.
- `0B-04A`: **`APPROVED / FROZEN`**.
- `0B-04B`: **`APPROVED / FROZEN`**.
- `0B-05A`: **`APPROVED / FROZEN`**.
- `0B-05B`: **`APPROVED / FROZEN`**.

F1–F5 permanecen provisionales; G6 está eliminado y G7 absorbido en F2. Ninguno constituye novelty ni gap definitivo.

### 3. 0B-04 — Fundamentos de IR y RAG

0B-04A y 0B-04B están congelados.

Fronteras gobernantes:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Trabajos adicionales de 0B-04 permanecen `RESERVED_FOR_DIRECTED_USE`; no se abre 0B-04C por defecto.

### 4. 0B-05 — Datos, procedencia, reproducibilidad, conocimiento y normativa

Alcance formal: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-05A

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:

`article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

Fronteras congeladas:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

F5 permanece únicamente como candidato estrecho de evaluación formal, explícita y separada de auditabilidad documental por salida.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`APPROVED / FROZEN`**.

Registros gobernantes:

- Prompt: `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.
- Revisión: `article/reviews/0B05B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación: `article/reviews/0B05B_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Corpus congelado: Zins; Hildreth & Kimble; Al-Hawamdeh.

Fronteras congeladas:

- data, information y knowledge no son sinónimos universales ni etapas lineales necesarias; sus relaciones dependen del marco conceptual;
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`;
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`;
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

`DOCUMENTED_EXPLICIT_KNOWLEDGE` es únicamente `OPERACIONALIZACION_DEL_PROYECTO`.

C1–C8 integradas: interpretación no rígida de D-I-K; contabilidad/atribución de Zins normalizada; duality de Hildreth & Kimble; control de fuentes anidadas; posición de Al-Hawamdeh no tratada como consenso; implicit/know-how separado de tacit estricto; conocimiento explícito documental restringido a operacionalización del proyecto; autoridad/vigencia/jerarquía de fuentes oficiales reservadas a 0B-05C.

Impacto metodológico: F1/F2/F4/F5 reciben solo `METHOD_BOUNDARY_RELEVANT`; F3 es `NOT_RELEVANT_TO_GAP_CANDIDATE`. No cambia ningún estado provisional de F1–F5. G6/G7 permanecen cerrados.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

No está activo todavía.

Antes de abrirlo se requiere:

1. identificar el conjunto exacto de fuentes oficiales primarias relevantes;
2. definir criterios de autoridad emisora, instrumento/documento exacto, versión/edición, fecha, vigencia, alcance, jerarquía documental, identificador/enlace estable y función evidencial;
3. separar `fuente oficial/autoritativa` de `evidencia suficiente para un caso` y de `corrección jurídica`;
4. crear un prompt ejecutable propio;
5. mantener las fuentes oficiales separadas de la literatura académica.

WCO/OMA, Comunidad Andina, SUNAT y otras fuentes solo entrarán si su presencia/función está sustentada por la documentación gobernante del proyecto. No se inventará ni completará una lista desde memoria.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

0B-06 solo se abrirá si, después de cerrar 0B-05 y agotar el corpus heredado pertinente, persiste una necesidad bibliográfica real bajo `article/BIBLIOGRAPHIC_FRAMEWORK.md`. No es obligatorio.

### 6. Gate

Gate general:

`IA de redacción/análisis -> revisión científica/editorial contra fuentes primarias -> corrección si aplica -> aprobación del autor -> freeze`.

0B-01 a 0B-05B completaron su gate.

Siguiente gate permitido:

`definir 0B-05C -> fijar fuentes oficiales -> crear prompt ejecutable -> READY_FOR_DRAFTING -> auditoría de fuentes oficiales -> revisión interna -> aprobación del autor -> freeze -> evaluar necesidad real de 0B-06`.

La IA experimental no es revisora bibliográfica rutinaria; se incorpora solo si una interpretación afecta hechos/claims experimentales o restricciones bajo su autoridad. El Plan Maestro sigue bajo autoridad exclusiva de la IA experimental.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, 0B-04B, 0B-05A y 0B-05B: `APPROVED / FROZEN`.
- 0B-05C: `NOT_STARTED / ELIGIBLE_FOR_DEFINITION`.
- 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and rules

Phase `0B — Critical literature map and taxonomy` uses controlled thematic batches with full primary-source and claim-source-scope verification. No manuscript drafting, final novelty, or definitive gap is allowed during 0B.

The consolidated corpus contains 62 distinct works/documents with primary access `62/62`. Governing rules preserve source provenance labels, prevent unsupported metadata/results, reject universal DIKW assumptions, and keep classification/retrieval/explanation/provenance/auditability/correctness concepts distinct.

### 2. Closed blocks

0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, 0B-04B, 0B-05A, and 0B-05B are **`APPROVED / FROZEN`**. F1–F5 remain provisional; G6 is eliminated and G7 is merged into F2.

### 3. 0B-04

Frozen boundaries distinguish query/document representation, candidate generation, ANN/index search, reranking, final ranking, RAG variants, query transformation, passage fusion, evidentiality, provenance, formal auditability, and legal correctness.

### 4. 0B-05

#### 0B-05A

Status: **`APPROVED / FROZEN`**.

Canonical artifact: `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

Frozen boundaries distinguish dataset documentation, identity/versioning, data/workflow provenance, reproducibility, replication, generalization, transparency trails, lifecycle audit, output-level auditability, and substantive/legal correctness.

#### 0B-05B

Status: **`APPROVED / FROZEN`**.

Governing records:

- `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`;
- `article/reviews/0B05B_INTERNAL_REVIEW.md`;
- `article/reviews/0B05B_AUTHOR_APPROVAL.md`;
- `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.

Frozen corpus: Zins; Hildreth & Kimble; Al-Hawamdeh.

Frozen boundaries state that data/information/knowledge are not universal synonyms or necessary linear stages; documented/explicit knowledge is not total expert knowledge; document retrieval is not expert interpretation/legal correctness; and LLM-generated explanation is not expert knowledge/official classification.

`DOCUMENTED_EXPLICIT_KNOWLEDGE` is project operationalization only. C1–C8 are integrated, including non-rigid D-I-K interpretation, normalized Zins attribution/counting, Hildreth & Kimble duality, nested-source control, author-specific treatment of Al-Hawamdeh, preservation of implicit/know-how vs strict tacit knowledge, and reservation of official-source authority/currency/hierarchy for 0B-05C.

F1/F2/F4/F5 receive methodological boundary relevance only; F3 is not relevant to the gap candidate in this batch. No provisional candidate state changes.

#### 0B-05C

Status: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

It is not active yet. Before opening, the workflow must identify the exact official primary-source set, define checks for issuing authority, exact instrument identity, version/edition/date, applicable currency, scope, documentary hierarchy, stable identifiers/links, and evidentiary role, and create a dedicated executable prompt.

Official/authoritative status must remain distinct from evidentiary sufficiency for a case and from legal correctness. WCO/OMA, Andean Community, SUNAT, and other sources enter only when supported by governing project documentation; the list will not be completed from memory.

### 5. 0B-06

Status: `NOT_STARTED`. It opens only if a genuine bibliographic need remains after 0B-05 and the relevant inherited corpus are exhausted.

### 6. Gate

0B-01 through 0B-05B have completed their gates.

Next allowed gate:

`define 0B-05C -> fix official source set -> create executable prompt -> READY_FOR_DRAFTING -> official-source audit -> internal review -> author approval -> freeze -> assess genuine need for 0B-06`.

Experimental-AI review is not routine; the experimental AI retains exclusive authority over the Master Plan and is invoked only when literature interpretation affects frozen experimental facts/claims or restrictions under its authority.

### 7. Current state

- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `OPEN`.
- 0B-01 through 0B-05B: `APPROVED / FROZEN`.
- 0B-05C: `NOT_STARTED / ELIGIBLE_FOR_DEFINITION`.
- 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` until 0B closes.
- 0D: `BLOCKED` until 0C closes.
- Target journal: `PENDING — to be decided in Phase 0D`.
