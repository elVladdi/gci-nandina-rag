# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito y reglas generales

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta mediante lotes temáticos controlados. Su finalidad es leer PDF completos, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable para 0C. Durante 0B no se redacta el manuscrito ni se declara novelty o gap definitivo.

Reglas gobernantes:

- corpus consolidado: `62` obras/documentos distintos, con acceso primario verificable `62/62`;
- solo se analizan los PDF del lote activo;
- lectura íntegra y auditoría claim-source-scope obligatorias;
- no inventar metadata, DOI, resultados, indexación o estado editorial;
- distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `OPERACIONALIZACION_DEL_PROYECTO` cuando aplique, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`;
- una afirmación secundaria no se convierte en hecho independiente sin verificar su fuente primaria;
- ausencia de group split documentado no demuestra leakage;
- no equiparar classification, candidate retrieval, evidence retrieval, reranking, explanation, provenance, reproducibility, auditability ni correctness;
- no imponer una pirámide DIKW o una transformación data→information→knowledge como universal si las fuentes no la sostienen;
- `SUPPORTS_CANDIDATE` significa solo supervivencia provisional, nunca novelty;
- las referencias heredadas conservan elegibilidad aunque sean antiguas/proceedings/preprints; nuevas referencias académicas se rigen por `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 2. Bloques cerrados

- `0B-01`: **`APPROVED / FROZEN`** — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02`: **`APPROVED / FROZEN`** — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A`: **`APPROVED / FROZEN`** — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B`: **`APPROVED / FROZEN`** — `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.
- `0B-04A`: **`APPROVED / FROZEN`** — `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.
- `0B-04B`: **`APPROVED / FROZEN`** — `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.
- `0B-05A`: **`APPROVED / FROZEN`** — `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

Después de los lotes de prior art aduanero permanecen provisionalmente F1–F5 en formas estrechas/metodológicas; G6 está eliminado como candidato a gap y G7 absorbido en F2. Ninguno constituye novelty ni gap definitivo.

### 3. 0B-04 — Fundamentos de Information Retrieval y RAG

0B-04A y 0B-04B están `APPROVED / FROZEN`.

Distinciones gobernantes:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Trabajos adicionales de 0B-04 permanecen `RESERVED_FOR_DIRECTED_USE`; no se abre 0B-04C por defecto.

### 4. 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Alcance formal: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail

Estado: **`APPROVED / FROZEN`**.

Registros gobernantes: prompt 0B05A, revisión interna, aprobación del autor y artefacto canónico `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`. Revisión experimental: `NOT_REQUIRED`.

Distinciones congeladas:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

Efecto congelado sobre candidatos:

- F1/F2: sin evidencia de novelty.
- F3: fundamento documental sobre relaciones/particiones, sin convertir documentación en control de dependencia.
- F4: `provenance/reproducibility/auditability ≠ substantive/legal correctness`.
- F5: prior art fuerte en provenance, transparency trails e internal audit elimina formulaciones amplias de ausencia de trazabilidad/auditabilidad; solo permanece como candidato estrecho la evaluación formal, explícita y separada de auditabilidad documental por salida.
- G6 permanece eliminado; G7 permanece absorbido en F2.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Registros:

- Prompt: `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.
- Revisión interna: `article/reviews/0B05B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Revisión experimental: `NOT_REQUIRED`.
- Aprobación del autor: `PENDING`.

Lote final controlado:

1. `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`
2. `The Duality of Knowledge.pdf`
3. `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`

La revisión interna contra los tres PDF primarios confirmó la diversidad conceptual del lote y que no procede seleccionar una secuencia DIKW universal. La notación `DATA ≠ INFORMATION ≠ KNOWLEDGE` solo puede utilizarse como abreviatura de no equivalencia automática/no sinonimia universal, no como disyunción ontológica rígida, porque Zins admite concepciones en las que `information` es un tipo de `knowledge`.

Normalizaciones obligatorias para el freeze:

- Zins: `44 panel contributors + researcher = 45 scholars`, aproximadamente 130 definiciones; distinguir posiciones de participantes, síntesis de Zins y posición propia de Zins.
- Hildreth & Kimble: `duality`, no dicotomía rígida; hard/soft coexisten en proporciones variables y la frontera es contextual.
- Al-Hawamdeh: externalized/explicit knowledge como `information` es posición del autor, no consenso universal; `implicit/know-how` se conserva distinto de `tacit` estricto.
- `DOCUMENTED_EXPLICIT_KNOWLEDGE`: solo `OPERACIONALIZACION_DEL_PROYECTO`.
- Claims anidados de otros autores permanecen `SECONDARY_CLAIM_UNVERIFIED` si se usan como afirmaciones independientes.
- La autoridad/vigencia/jerarquía/suficiencia jurídica de las fuentes normativas no es verificada por P01–P03; esa auditoría primaria corresponde a 0B-05C.

Fronteras aceptadas para el eventual freeze:

`DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`

`LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

Estas son fronteras metodológicas, no una ontología universal ni una cadena de implicación.

Relación resultante con F1–F5: F1/F2/F4/F5 reciben solo `METHOD_BOUNDARY_RELEVANT`; F3 es `NOT_RELEVANT_TO_GAP_CANDIDATE`. Los estados provisionales F1–F5 no cambian. 0B-05B no es un pressure test de novelty. G6/G7 no se reabren.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse después del freeze de 0B-05B. Será una auditoría separada de fuentes oficiales primarias —WCO/OMA, Comunidad Andina, SUNAT y otras pertinentes— según autoridad emisora, versión, vigencia, fecha, jerarquía documental, identificador/enlace estable y función evidencial.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si, después de cerrar 0B-05 y agotar el corpus heredado relevante, persiste un vacío bibliográfico real bajo `article/BIBLIOGRAPHIC_FRAMEWORK.md`. 0B-06 no es obligatorio.

### 6. Gate

Gate general:

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

0B-01 a 0B-05A completaron el gate correspondiente.

Gate activo:

`0B-05B INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> aprobación expresa del autor -> incorporar C1–C8 al artefacto canónico -> freeze -> evaluar definición/apertura de 0B-05C`.

La IA experimental no es revisora bibliográfica obligatoria; se incorpora solo si una interpretación bibliográfica modifica o amenaza hechos/claims experimentales o restricciones bajo su autoridad.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, 0B-04B y 0B-05A: `APPROVED / FROZEN`.
- Bloque activo: `0B-05B`.
- 0B-05B: `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- 0B-05C: `NOT_STARTED / CLOSED_BY_GATE`.
- 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and rules

Phase `0B — Critical literature map and taxonomy` uses controlled thematic batches with full-PDF and claim-source-scope verification. No manuscript drafting, final novelty, or definitive gap is allowed during 0B. The inherited corpus contains 62 distinct works/documents with primary access `62/62`.

Governing rules include strict separation of retrieval/classification/explanation/provenance/auditability/correctness concepts, source-level provenance labels, and rejection of a universal DIKW transformation unless the primary sources support it.

### 2. Closed blocks

0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, 0B-04B, and 0B-05A are **`APPROVED / FROZEN`**. F1–F5 remain provisional; G6 is eliminated and G7 is merged into F2.

### 3. 0B-04 — IR/RAG foundations

Frozen boundaries distinguish representation, candidate generation, ANN/index search, reranking, final ranking, RAG variants, query transformation, passage fusion, evidentiality, provenance, formal auditability, and legal correctness. Additional 0B-04 works remain reserved for directed use.

### 4. 0B-05

#### 0B-05A

Status: **`APPROVED / FROZEN`**.

Frozen boundaries distinguish dataset documentation, identity/versioning, data/workflow provenance, reproducibility, replication, generalization, transparency trails, lifecycle audit, output-level auditability, and substantive/legal correctness. F5 remains only as the narrow provisional candidate of formal, explicit, separate documentary auditability evaluation at output level.

#### 0B-05B — Information, documented explicit knowledge, and limits of codified knowledge

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Records: active prompt `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`; internal review `article/reviews/0B05B_INTERNAL_REVIEW.md` with `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`; experimental review `NOT_REQUIRED`; author approval `PENDING`.

The primary-source review confirms conceptual diversity and rejects a universal DIKW ontology. `DATA ≠ INFORMATION ≠ KNOWLEDGE` may be used only as shorthand for non-automatic equivalence/non-universal synonymy, not as rigid ontological disjunction, because Zins allows conceptions in which information is a type of knowledge.

Mandatory freeze normalizations preserve Zins attribution/counting, Hildreth & Kimble's duality rather than rigid dichotomy, Al-Hawamdeh's externalized-knowledge-to-information mapping as his own conceptual position, implicit/know-how as distinct from strict tacit knowledge, `DOCUMENTED_EXPLICIT_KNOWLEDGE` as `PROJECT_OPERATIONALIZATION` only, and nested-source claims as secondary unless independently verified. Authority/currency/hierarchy/legal sufficiency of official normative sources is deferred to 0B-05C.

Accepted methodological boundaries for the eventual freeze are:

`DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`

`LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

F1/F2/F4/F5 receive methodological boundary relevance only; F3 is not relevant to the gap candidate in this batch. No provisional gap-candidate state changes. G6/G7 remain closed.

#### 0B-05C

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may be defined only after 0B-05B freezes and will be a separate audit of official primary normative sources.

### 5. 0B-06 and gate

0B-06 remains `NOT_STARTED` and opens only if a genuine bibliographic gap remains after 0B-05 and the relevant inherited corpus are exhausted.

Active gate:

`0B-05B INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> express author approval -> incorporate C1–C8 into the canonical artifact -> freeze -> assess definition/opening of 0B-05C`.

Experimental-AI review is not routine and is triggered only if literature interpretation changes or threatens frozen experimental facts/claims or restrictions under its authority.

0C remains blocked until 0B closes; 0D remains blocked until 0C closes; target journal remains pending until 0D.
