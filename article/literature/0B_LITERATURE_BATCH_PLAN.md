# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito y reglas generales

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta mediante lotes temáticos controlados. Su finalidad es leer PDF completos, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable para 0C. Durante 0B no se redacta el manuscrito ni se declara novelty o gap definitivo.

Reglas gobernantes:

- corpus consolidado: `62` obras/documentos distintos, con acceso primario verificable `62/62`;
- solo se analizan los PDF del lote activo;
- lectura íntegra y auditoría claim-source-scope obligatorias;
- no inventar metadata, DOI, resultados, indexación o estado editorial;
- distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`;
- una afirmación secundaria no se convierte en hecho independiente sin verificar su fuente primaria;
- ausencia de group split documentado no demuestra leakage;
- no equiparar classification, candidate retrieval, evidence retrieval, reranking, explanation, provenance, reproducibility, auditability ni correctness;
- `SUPPORTS_CANDIDATE` significa solo supervivencia provisional, nunca novelty;
- las referencias heredadas conservan elegibilidad aunque sean antiguas/proceedings/preprints; nuevas referencias académicas se rigen por `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 2. Bloques cerrados

- `0B-01`: **`APPROVED / FROZEN`** — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02`: **`APPROVED / FROZEN`** — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A`: **`APPROVED / FROZEN`** — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B`: **`APPROVED / FROZEN`** — `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.
- `0B-04A`: **`APPROVED / FROZEN`** — `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.
- `0B-04B`: **`APPROVED / FROZEN`** — `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.

Después de 0B-03B permanecen provisionalmente F1–F5 en formas estrechas/metodológicas; G6 está eliminado como candidato a gap y G7 absorbido en F2. Ninguno constituye novelty ni gap definitivo. Los lotes fundacionales posteriores no modifican ese status salvo decisión explícita en un freeze.

### 3. 0B-04 — Fundamentos de Information Retrieval y RAG

Alcance formal: `article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-04A

Estado: **`APPROVED / FROZEN`**.

Distinción congelada:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

#### 0B-04B

Estado: **`APPROVED / FROZEN`**.

Distinciones congeladas:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Los resultados fundacionales no reinterpretan el resultado D1a fuera de la implementación densa exploratoria específica del proyecto.

Trabajos adicionales de 0B-04 permanecen `RESERVED_FOR_DIRECTED_USE`; no se abre 0B-04C por defecto.

### 4. 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Alcance formal: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

0B-05 se divide en tres sub-lotes controlados y solo uno puede estar abierto a la vez.

#### 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

Revisión interna: `article/reviews/0B05A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

Lote final:

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

La identidad científica del tercer archivo es **FAIR Data Pipeline: provenance-driven data management for traceable scientific workflows**.

Fronteras aceptadas por la revisión:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

Correcciones C1–C7 que deberán incorporarse al freeze:

- Bender & Friedman: propuesta documental, dos casos post hoc y value scenarios no predictivos; no causalizar beneficios.
- Gebru: copia analizada = arXiv v8; metadata editorial final queda `REVIEW_REQUIRED_FOR_FINAL_CITATION`, sin reconstrucción silenciosa; no homogeneizar su uso de reproducibility con Pineau.
- FAIR Data Pipeline: provenance/lineage y versiones son el núcleo; full reproducibility no es core requirement; identifiers/versioning no garantizan correctness.
- Pineau: preservar `reproducible ≠ replicable ≠ robust ≠ generalisable` como convención del paper; no causalizar asociaciones ni presentar code/data availability como garantía automática.
- Raji: SMACTR tiene cinco etapas; Post-Audit no constituye una sexta etapa; transparency trail/ADHF = lifecycle auditability, no formal per-output auditability, external independent audit ni legal correctness.
- La taxonomía cruzada es una frontera metodológica, no una secuencia lineal de madurez o implicación.

Efecto provisional sobre candidatos:

- F1/F2: sin evidencia de novelty.
- F3: fundamento documental sobre composición/relaciones/particiones; documentar no equivale a controlar dependencia.
- F4: frontera metodológica `provenance/reproducibility/auditability ≠ substantive/legal correctness`.
- F5: prior art fuerte en provenance, transparency trails e internal audit elimina cualquier formulación amplia de ausencia de trazabilidad/auditabilidad. Solo permanece como candidato estrecho la evaluación formal, explícita y separada de auditabilidad documental por salida, aún sin novelty.
- G6 permanece eliminado; G7 permanece absorbido en F2.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse/abrirse después del freeze de 0B-05A. Fuentes candidatas heredadas, sujetas a confirmación primaria antes de apertura:

- `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`;
- `The Duality of Knowledge.pdf`;
- Al-Hawamdeh únicamente si se confirma acceso al PDF primario completo.

Objetivo previsto: delimitar data, information, documented/explicit knowledge y conocimiento tácito/no codificado, sin convertir retrieval documental en sustituto del conocimiento experto.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse después del freeze de 0B-05B. Será una auditoría separada de fuentes oficiales primarias, no un lote de literatura académica. Revisará autoridad emisora, versión, vigencia, fecha, jerarquía documental, identificador/enlace estable y función evidencial para WCO/OMA, Comunidad Andina, SUNAT y otras fuentes pertinentes.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si, después de completar el corpus heredado relevante y cerrar 0B-05, persiste un vacío bibliográfico real bajo `article/BIBLIOGRAPHIC_FRAMEWORK.md`. 0B-06 no es obligatorio.

### 6. Gate

Gate general:

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

0B-01 a 0B-04B completaron el gate.

Gate activo:

`0B-05A INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> aprobación expresa del autor -> integrar C1–C7 -> freeze -> definir/abrir 0B-05B`.

No se requiere retorno a la IA de redacción porque `MATERIAL_ERRORS = 0`. La IA experimental no es revisora bibliográfica obligatoria y en 0B-05A no se activó porque ningún hecho/claim experimental congelado fue modificado.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A y 0B-04B: `APPROVED / FROZEN`.
- Bloque activo: `0B-05A`.
- 0B-05A: `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- 0B-05B: `NOT_STARTED / CLOSED_BY_GATE`.
- 0B-05C: `NOT_STARTED / CLOSED_BY_GATE`.
- 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and rules

Phase `0B — Critical literature map and taxonomy` uses controlled thematic batches with full-PDF and claim-level verification. No manuscript drafting, final novelty, or definitive gap is allowed during 0B. The inherited corpus contains 62 distinct works/documents with primary access `62/62`.

### 2. Closed blocks

0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, and 0B-04B are **`APPROVED / FROZEN`**. F1–F5 remain provisional; G6 is eliminated and G7 is merged into F2.

### 3. 0B-04 — IR/RAG foundations

0B-04A freezes the distinction between representation, candidate generation, ANN/index search, reranking, and final ranking.

0B-04B freezes the distinctions among RAG, retrieval-augmented pretraining, retrieve-then-generate, query expansion, query rewriting, passage fusion, and evidentiality-guided generation; and separately between retrieved passages, evidence attribution, evidentiality, grounding guarantees, provenance verification, formal auditability, and legal correctness.

These foundational results do not reinterpret the project's D1a result beyond its specific exploratory dense implementation.

### 4. 0B-05 — Data, documentation, provenance, reproducibility, knowledge, and normative sources

Formal scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-05A — Data documentation, provenance, reproducibility, and audit trail

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

Internal review: `article/reviews/0B05A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

The review accepts the boundaries:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

C1–C7 require the freeze to keep Bender & Friedman as documentation rather than causal validation; preserve the analyzed Gebru copy as arXiv v8 and final-citation metadata as pending, while keeping its reproducibility terminology distinct from Pineau; keep FAIR Data Pipeline centered on provenance/lineage because full reproducibility is explicitly not a core requirement; preserve Pineau's 2×2 terminology and non-causal interpretation; keep SMACTR at five stages and separate lifecycle audit from per-output/external/legal auditability; and treat the cross-paper taxonomy as boundaries rather than a linear implication ladder.

F1/F2 receive no novelty evidence. F3 gains documentation foundation only. F4 gains a correctness boundary. F5 is further narrowed by strong prior art on provenance, transparency trails, and internal audit: only the narrow candidate of formal, explicit, separate documentary auditability evaluation at output level remains, still without novelty status. G6/G7 remain closed as previously frozen.

#### 0B-05B

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may open only after 0B-05A is frozen. Candidate inherited sources remain Zins, Hildreth & Kimble, and Al-Hawamdeh only if complete primary-PDF access is confirmed.

#### 0B-05C

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It will be a separate primary-official-source audit after 0B-05B, covering authority, version, currency, documentary hierarchy, stable identifiers, and evidentiary role.

### 5. 0B-06 and gate

0B-06 remains `NOT_STARTED` and will open only if a genuine bibliographic gap remains after the inherited corpus and 0B-05 are completed.

Active gate:

`0B-05A INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> express author approval -> integrate C1–C7 -> freeze -> define/open 0B-05B`.

No return to the drafting AI is required because `MATERIAL_ERRORS = 0`; experimental-AI review was not triggered.

### 6. Current state

0B-01 through 0B-04B are frozen. 0B-05A awaits author approval. 0B-05B/05C remain closed by gate; 0B-06 is not started; 0C and 0D remain blocked. Target journal remains pending until 0D.
