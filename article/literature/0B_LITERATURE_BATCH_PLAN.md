# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito y reglas generales

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta mediante lotes temáticos controlados. Su finalidad es leer PDF completos, identificar qué problema resuelve realmente cada trabajo y construir un mapa comparable para 0C. Durante 0B no se redacta el manuscrito ni se declara novelty o gap definitivo.

Reglas gobernantes:

- corpus consolidado: `62` obras/documentos distintos, con acceso primario verificable `62/62`;
- solo se analizan los PDF del lote activo;
- lectura íntegra obligatoria;
- no inventar metadata, DOI, resultados, indexación o estado editorial;
- distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`;
- una afirmación secundaria no se convierte en hecho independiente sin verificar su fuente primaria;
- ausencia de group split documentado no demuestra leakage;
- no equiparar classification, candidate retrieval, evidence retrieval, reranking, explanation, auditability ni correctness;
- `SUPPORTS_CANDIDATE` significa solo supervivencia provisional, nunca novelty;
- las referencias heredadas conservan elegibilidad aunque sean antiguas/proceedings/preprints; nuevas referencias académicas se rigen por `article/BIBLIOGRAPHIC_FRAMEWORK.md`.

### 2. Bloques cerrados

- `0B-01`: **`APPROVED / FROZEN`** — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02`: **`APPROVED / FROZEN`** — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A`: **`APPROVED / FROZEN`** — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B`: **`APPROVED / FROZEN`** — `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.
- `0B-04A`: **`APPROVED / FROZEN`** — `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.
- `0B-04B`: **`APPROVED / FROZEN`** — `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.

Después de 0B-03B permanecen provisionalmente F1–F5 en formas estrechas/metodológicas; G6 está eliminado como candidato a gap y G7 absorbido en F2. Ninguno constituye novelty ni gap definitivo. Los lotes fundacionales 0B-04A/04B no modifican esos estados.

### 3. 0B-04 — Fundamentos de Information Retrieval y RAG

Alcance formal:
`article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-04A

Estado: **`APPROVED / FROZEN`**.

Registros: prompt 0B04A, revisión interna, aprobación del autor y artefacto canónico `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.

Distinción congelada:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

#### 0B-04B

Estado: **`APPROVED / FROZEN`**.

Registros:

- Prompt: `article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.
- Revisión interna: `article/reviews/0B04B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación: `article/reviews/0B04B_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Lote congelado: Lewis et al. RAG, REALM, Fusion-in-Decoder, Query2doc, Query Rewriting for Retrieval-Augmented Large Language Models y Evidentiality-guided Generation.

Distinciones congeladas:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

C1–C13 quedan integradas: gobernar Lewis por Tabla-4 `11.7%` frente al `17%` narrativo; no describir RAG-Token como retrieval nuevo por token; preservar REALM como retrieval-augmented pretraining/span-based Open-QA; separar FiD fusion/attribution; tratar Query2doc/query rewriting como transformaciones upstream; preservar OOD mixto, false-claim risk y latencia específica; gobernar Asai por cinco datasets y limitar `95%/96%` a validación de labels; separar provenance/grounding/evidentiality/auditability/legal correctness; no transferir benchmarks a HS/NANDINA.

Contrato del piloto usado solo como frontera comparativa:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

#### Trabajos reservados

Permanecen `RESERVED_FOR_DIRECTED_USE`: SimCSE, `Query Expansion by Prompting Large Language Models`, ExtractGPT, product-information extraction with ChatGPT y LLM product-attribute extraction/normalization. No se abre 0B-04C por defecto.

### 4. 0B-05 — Datos, documentación, procedencia, reproducibilidad, conocimiento y normativa

Alcance formal:
`article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Por heterogeneidad conceptual, 0B-05 se ejecutará en tres sub-lotes controlados y solo uno podrá estar abierto a la vez.

#### 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail

Estado: **`READY_FOR_DRAFTING`**.

Prompt activo:
`article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

Lote final:

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

La identidad científica del tercer archivo es **FAIR Data Pipeline: provenance-driven data management for traceable scientific workflows**; el nombre físico se conserva para localizar la copia suministrada.

Cadena metodológica gobernante:

`DATA/DOCUMENTATION -> VERSION/IDENTITY -> PROVENANCE/LINEAGE -> REPRODUCIBLE WORKFLOW -> AUDIT TRAIL`

sin inferir:

`CORRECTNESS -> LEGAL VALIDITY -> GENERALIZATION`.

Controles obligatorios:

- dataset documentation ≠ dataset quality/adequacy;
- dataset description ≠ dataset identity/version;
- versioning ≠ reproducibility;
- provenance/lineage ≠ correctness;
- code/data availability ≠ automatic reproducibility;
- reproducibility ≠ external replication/generalization;
- lifecycle/internal audit ≠ output-level formal auditability evaluation;
- transparency trail ≠ legal correctness.

En relación con F1–F5, 0B-05A es metodológico y de gobernanza, no un pressure test de prior art aduanero. F1/F2 son normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`; F3 puede recibir fundamento metodológico sobre documentación de composición/curación/particiones sin inferir leakage; F4 puede recibir frontera metodológica entre provenance/reproducibility y correctness; F5 puede recibir frontera metodológica entre lifecycle audit trail y evaluación formal de auditabilidad por salida. G6 permanece eliminado y G7 absorbido en F2.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse/abrirse después del freeze de 0B-05A. Fuentes candidatas heredadas, sujetas a confirmación primaria antes de apertura:

- `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`;
- `The Duality of Knowledge.pdf`;
- Al-Hawamdeh, únicamente si se confirma acceso al PDF primario completo.

Objetivo previsto: delimitar data, information, documented/explicit knowledge y conocimiento tácito/no codificado, sin convertir retrieval documental en sustituto del conocimiento experto.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse después del freeze de 0B-05B y de verificar qué fuentes oficiales primarias del corpus vigente requieren auditoría documental adicional. Será una auditoría separada de fuentes oficiales, no un lote de literatura académica. Se revisarán autoridad emisora, versión, vigencia, fecha, jerarquía documental, identificador/enlace estable y función evidencial. WCO/OMA, Comunidad Andina y SUNAT se tratarán como fuentes primarias oficiales y no como artículos científicos.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED`.

Solo se abrirá si, después de completar el corpus heredado relevante y cerrar 0B-05, persiste un vacío bibliográfico real y bajo las reglas de `article/BIBLIOGRAPHIC_FRAMEWORK.md`. 0B-06 no es obligatorio.

### 6. Gate

Gate general:

`IA de redacción -> revisión científica/editorial interna contra PDF primarios -> corrección si aplica -> aprobación del autor -> freeze`.

0B-04A y 0B-04B completaron el gate.

Gate activo:

`0B-05A READY_FOR_DRAFTING -> IA de redacción -> revisión interna contra los cinco PDF primarios -> aprobación del autor -> freeze -> definir/abrir 0B-05B`.

0B-05B y 0B-05C permanecen cerrados hasta sus gates respectivos. La IA experimental no es revisora bibliográfica obligatoria y se incorpora solo si una interpretación bibliográfica modifica hechos/claims experimentales o restricciones bajo su autoridad.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A y 0B-04B: `APPROVED / FROZEN`.
- Bloque activo: `0B-05A`.
- 0B-05A: `READY_FOR_DRAFTING`.
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

0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, and 0B-04B are **`APPROVED / FROZEN`**. F1–F5 remain provisional after the customs-prior-art batches; G6 is eliminated as a gap candidate and G7 is merged into F2. The foundational 0B-04 batches do not change those states.

### 3. 0B-04 — IR/RAG foundations

0B-04A is approved/frozen and established the distinction between representation, candidate generation, ANN/index search, reranking, and final ranking.

0B-04B is approved/frozen. Its frozen distinctions separate retrieval-augmented generation, retrieval-augmented pretraining, retrieve-then-generate, query expansion, query rewriting, passage fusion, and evidentiality-guided generation; and separately distinguish retrieved passages, evidence attribution, evidentiality, grounding guarantees, provenance verification, formal auditability, and legal correctness.

The pilot remains only a comparison boundary: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

Reserved IR/product-processing works remain `RESERVED_FOR_DIRECTED_USE`; no 0B-04C opens by default.

### 4. 0B-05 — Data, documentation, provenance, reproducibility, knowledge, and normative sources

Formal scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

0B-05 is divided into three controlled sub-batches.

#### 0B-05A — Data documentation, provenance, reproducibility, and audit trail

Status: **`READY_FOR_DRAFTING`**.

Active prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

The final inherited set contains Bender & Friedman data statements, Gebru et al. datasheets, the supplied FAIR Data Pipeline paper, Pineau et al. reproducibility report, and Raji et al. end-to-end internal algorithmic auditing framework.

The governing chain is:

`DATA/DOCUMENTATION -> VERSION/IDENTITY -> PROVENANCE/LINEAGE -> REPRODUCIBLE WORKFLOW -> AUDIT TRAIL`

and explicitly not:

`CORRECTNESS -> LEGAL VALIDITY -> GENERALIZATION`.

Required boundaries include documentation vs dataset adequacy, description vs identity/version, versioning vs reproducibility, provenance vs correctness, code/data availability vs automatic reproducibility, reproducibility vs external replication/generalization, lifecycle/internal audit vs formal output-level auditability, and transparency trail vs legal correctness.

F1/F2 are normally not relevant in this sub-batch; F3/F4/F5 may receive methodological foundation/boundary labels only, never novelty evidence. G6 remains eliminated and G7 remains merged into F2.

#### 0B-05B — Information, documented explicit knowledge, and limits of codified knowledge

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may open only after 0B-05A is frozen. Candidate inherited primary sources are Zins, Hildreth & Kimble, and Al-Hawamdeh only if complete primary-PDF access is confirmed.

#### 0B-05C — Authority, currency, and traceability of normative/official sources

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It will be a separate primary-official-source audit after 0B-05B, covering issuing authority, version, currency, documentary hierarchy, stable identifiers, and evidentiary role for WCO, Andean Community, SUNAT, and other relevant official sources. These are official primary sources, not academic articles.

### 5. 0B-06 and gate

0B-06 remains `NOT_STARTED` and will open only if a genuine bibliographic gap remains after the relevant inherited corpus and 0B-05 are completed. It is not mandatory.

Active gate:

`0B-05A READY_FOR_DRAFTING -> drafting AI -> internal review against the five primary PDFs -> express author approval -> freeze -> define/open 0B-05B`.

0B-05B and 0B-05C remain closed by their gates. Experimental-AI review is only triggered if a literature interpretation affects frozen experimental facts/claims or restrictions under its authority.

### 6. Current status

Phase 0A is closed/approved. Phase 0B is open. 0B-01 through 0B-04B are approved/frozen. 0B-05A is the active block and is ready for drafting; 0B-05B/05C are closed by gate; 0B-06 is not started; 0C and 0D remain blocked; target journal remains pending until 0D.
