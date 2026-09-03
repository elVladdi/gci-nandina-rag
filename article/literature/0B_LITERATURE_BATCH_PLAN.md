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

Registros:

- Prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.
- Revisión interna: `article/reviews/0B05A_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación: `article/reviews/0B05A_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Corpus congelado: Bender & Friedman, Gebru et al., FAIR Data Pipeline, Pineau et al. y Raji et al.

Distinciones congeladas:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

C1–C7 integradas: Bender & Friedman permanecen como documentación/contextualización y no validación causal; la copia Gebru v8 gobierna el lote y su metadata editorial final queda pendiente; el uso de reproducibility de Gebru/Pineau no se homogeneiza; FAIR Data Pipeline se centra en provenance/lineage y version identification; Pineau conserva su taxonomía operacional específica y lectura no causal; SMACTR conserva cinco etapas y lifecycle auditability se separa de per-output/external/legal auditability; la taxonomía cruzada no se interpreta como escalera de madurez.

Efecto congelado sobre candidatos:

- F1/F2: sin evidencia de novelty.
- F3: fundamento documental sobre relaciones/particiones, sin convertir documentación en control de dependencia.
- F4: `provenance/reproducibility/auditability ≠ substantive/legal correctness`.
- F5: prior art fuerte en provenance, transparency trails e internal audit elimina cualquier formulación amplia de ausencia de trazabilidad/auditabilidad. Solo permanece como candidato estrecho, aún sin novelty, la evaluación formal, explícita y separada de auditabilidad documental por salida.
- G6 permanece eliminado; G7 permanece absorbido en F2.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

Antes de abrirlo se debe:

1. confirmar acceso primario completo a sus fuentes candidatas;
2. fijar el lote final;
3. crear un prompt ejecutable propio;
4. mantener el bloque como fundacional, sin declarar novelty.

Fuentes candidatas heredadas:

- `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`;
- `The Duality of Knowledge.pdf`;
- `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`, si se confirma el PDF primario completo.

Objetivo previsto: delimitar data, information, documented/explicit knowledge y conocimiento tácito/no codificado; evitar una transformación DIKW automática; precisar el uso legítimo de “conocimiento explícito documental” para el corpus normativo; y preservar que retrieval documental no sustituye interpretación/juicio experto.

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

Siguiente gate permitido:

`confirmar fuentes 0B-05B -> definir lote final -> crear prompt ejecutable -> READY_FOR_DRAFTING -> IA de redacción -> revisión interna -> aprobación del autor -> freeze -> evaluar apertura de 0B-05C`.

La IA experimental no es revisora bibliográfica obligatoria; se incorpora solo si una interpretación bibliográfica modifica hechos/claims experimentales o restricciones bajo su autoridad.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, 0B-04B y 0B-05A: `APPROVED / FROZEN`.
- 0B-05B: `NOT_STARTED / ELIGIBLE_FOR_DEFINITION`.
- 0B-05C: `NOT_STARTED / CLOSED_BY_GATE`.
- 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` hasta cerrar 0B.
- 0D: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and rules

Phase `0B — Critical literature map and taxonomy` uses controlled thematic batches with full-PDF and claim-source-scope verification. No manuscript drafting, final novelty, or definitive gap is allowed during 0B. The inherited corpus contains 62 distinct works/documents with primary access `62/62`.

### 2. Closed blocks

0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, 0B-04B, and 0B-05A are **`APPROVED / FROZEN`**. F1–F5 remain provisional; G6 is eliminated and G7 is merged into F2.

### 3. 0B-04 — IR/RAG foundations

Frozen boundaries distinguish representation, candidate generation, ANN/index search, reranking, final ranking, RAG variants, query transformation, passage fusion, evidentiality, provenance, formal auditability, and legal correctness. Additional 0B-04 works remain reserved for directed use.

### 4. 0B-05

#### 0B-05A

Status: **`APPROVED / FROZEN`**.

Governing records are its prompt, internal review, author approval, and canonical artifact `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`. Experimental review was `NOT_REQUIRED`.

Frozen boundaries:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

C1–C7 are integrated. F3 gains documentation foundation only; F4 remains a correctness boundary; F5 is narrowed by strong provenance/transparency/internal-audit prior art to the still-provisional candidate of formal, explicit, separate documentary output-level auditability evaluation. G6/G7 remain closed.

#### 0B-05B

Status: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

Before opening, complete primary access must be confirmed, a final controlled batch must be fixed, and an executable prompt must be created. Candidate inherited sources cover conceptual data/information/knowledge definitions, explicit/tacit knowledge duality, and tacit-knowledge management if the complete primary PDF is confirmed. The block must preserve that document retrieval does not replace expert interpretation or judgment.

#### 0B-05C

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may be defined only after 0B-05B freezes and will be a separate audit of official primary normative sources.

### 5. 0B-06 and gate

0B-06 remains `NOT_STARTED` and opens only if a genuine bibliographic gap remains after 0B-05 and the relevant inherited corpus are exhausted.

Next gate: confirm 0B-05B primary sources -> define final batch -> create executable prompt -> READY_FOR_DRAFTING -> drafting AI -> internal review -> author approval -> freeze -> assess opening 0B-05C.

Experimental-AI review is not a routine bibliographic gate and is triggered only if literature interpretation changes frozen experimental facts/claims or restrictions under its authority.

0C remains blocked until 0B closes; 0D remains blocked until 0C closes; target journal remains pending until 0D.
