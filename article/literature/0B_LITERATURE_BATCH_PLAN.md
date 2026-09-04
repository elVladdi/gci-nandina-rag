# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito y reglas generales

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta mediante lotes temáticos controlados. Su finalidad es leer y auditar fuentes primarias completas, identificar qué problema resuelve o qué autoridad documental aporta realmente cada fuente y construir un mapa comparable para 0C. Durante 0B no se redacta el manuscrito ni se declara novelty o gap definitivo.

Reglas gobernantes:

- corpus académico/documental consolidado: `62` obras/documentos distintos, acceso primario verificable `62/62`;
- lectura/auditoría claim-source-scope obligatoria;
- no inventar metadata, DOI, resultados, vigencia, jerarquía o estado editorial/normativo;
- una afirmación secundaria no se convierte en hecho independiente sin verificar su fuente primaria;
- no equiparar classification, candidate retrieval, evidence retrieval, reranking, explanation, provenance, reproducibility, auditability ni correctness;
- no imponer DIKW universal ni transformar automáticamente data→information→knowledge;
- `SUPPORTS_CANDIDATE` nunca significa novelty;
- literatura académica nueva se rige por `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
- fuentes normativas/institucionales primarias constituyen una capa separada y se auditan por autoridad, identidad, vigencia, alcance y función documental.

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

### 3. Fundamentos ya congelados

0B-04A:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

0B-04B:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

0B-05A:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

0B-05B:

- data/information/knowledge no son sinónimos universales ni etapas lineales necesarias;
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`;
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`;
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`;
- `DOCUMENTED_EXPLICIT_KNOWLEDGE` = `OPERACIONALIZACION_DEL_PROYECTO` únicamente.

### 4. 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`READY_FOR_DRAFTING`**.

Alcance formal:

`article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Prompt activo:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

#### 4.1 Objeto

0B-05C no es literatura académica: audita la capa de fuente primaria oficial y compara:

`EXPERIMENTAL_SOURCE_SNAPSHOT`

con

`CURRENT_OFFICIAL_SOURCE_STATE`.

El bloque debe verificar autoridad emisora, instrumento exacto, fecha, vigencia, alcance, función documental, modificaciones/derogaciones, identificador oficial y relación con el corpus experimental.

#### 4.2 Snapshot experimental gobernante

Ref de desarrollo congelado por 0A-02:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

Fuentes a rastrear:

- `data/external/Arancel 2022.pdf` + `arancel2022_run_metadata.json`;
- `data/external/CAN Desición 885 - Nanadina Gaceta 4359.pdf` + `data/processed/corpus/nandina/run_metadata.json`;
- artefactos procesados derivados cuando sean necesarios para comprobar alcance.

SHA-256 registrados:

- Arancel 2022: `a01a029e1ca29b6debc61d219c17dfc086354e00669246cc24a91ad9f454c7d0`;
- Decisión 885/Gaceta 4359: `8c4a30fb0328f151089ac4c7857ac447d3dd353de97122a11bde4550d594f0c6`.

#### 4.3 Fuentes oficiales controladas

Mínimo:

- **WCO/OMA:** Convenio HS en lo necesario; HS Nomenclature 2022; GIR 2022; enmiendas complementarias relevantes; estatus de Explanatory Notes solo si el claim lo exige.
- **Comunidad Andina:** Decisión 885/Gaceta 4359; Decisión 906/Gaceta 5062; Resolución 2592/Gaceta 5761; otros instrumentos solo si son necesarios para determinar vigencia/Capítulo 87.
- **Perú:** DS 404-2021-EF/Arancel de Aduanas 2022; modificaciones posteriores materialmente pertinentes; página SUNAT/gob.pe NANDINA como orientación institucional; DESPA-PG.01 v8 y DESPA-PE.00.03 v4 únicamente para claims de procedencia/contexto administrativo de DAM/reconocimiento físico.

La auditoría requiere web actual, pero la evidencia final solo puede provenir de dominios oficiales WCO/OMA, Comunidad Andina, SUNAT, gob.pe, MEF o El Peruano.

#### 4.4 Drift preliminar abierto

La definición del lote verificó en fuente oficial que la **Decisión 906**, vigente desde `2023-01-01`, modifica la Decisión 885 e incluye cambios de Capítulo 87, entre ellos `8704.41.10` y `8704.51.10`.

Las 42 etiquetas EVAL v0.2 del artefacto `historical_support_by_code_v0.2.csv` no incluyen esos dos códigos. Esto no demuestra impacto experimental nulo porque podrían aparecer como candidatos, códigos históricos o evidencia.

Estado de apertura:

`PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`.

El bloque debe distinguir estrictamente:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

Si se confirma o queda razonablemente abierta afectación material de componentes congelados, el entregable debe marcar `EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`; no debe alterar experimentos, 0A, claims congelados ni Plan Maestro.

La Resolución 2592 de 2026 se identificó preliminarmente como Notas Explicativas Complementarias para capítulos 1–22; no se presume afectación de Capítulo 87.

#### 4.5 Fronteras obligatorias

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_SUBHEADING-10`

`INSTITUTIONAL_ORIENTATION_PAGE ≠ SUPRANATIONAL_LEGAL_INSTRUMENT`

`TEXT_AUXILIARY_FOR_INTERPRETATION ≠ BINDING_NORM`, salvo soporte oficial expreso.

0B-05C no modifica F1–F5: solo puede aportar relevancia metodológica de frontera. G6/G7 permanecen cerrados.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: `NOT_STARTED / CLOSED_BY_GATE`.

0B-06 solo se evaluará después del freeze de 0B-05C y únicamente si persiste una necesidad bibliográfica real bajo `article/BIBLIOGRAPHIC_FRAMEWORK.md`. No es obligatorio.

### 6. Gate

Gate activo:

`0B-05C READY_FOR_DRAFTING -> IA de análisis -> auditoría primaria oficial -> revisión científica/editorial -> [IA experimental si trigger confirmado] -> corrección/normalización si aplica -> aprobación expresa del autor -> freeze -> evaluar necesidad real de 0B-06`.

La IA experimental conserva autoridad exclusiva sobre el Plan Maestro y decisiones experimentales correctivas.

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01 a 0B-05B: `APPROVED / FROZEN`.
- Bloque activo: `0B-05C`.
- 0B-05C: `READY_FOR_DRAFTING`.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`.
- 0B-06: `NOT_STARTED / CLOSED_BY_GATE`.
- 0C: `BLOCKED`.
- 0D: `BLOCKED`.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and rules

Phase 0B uses controlled primary-source batches and does not draft the manuscript or declare final novelty/gap. Academic literature and official normative/institutional sources remain separate evidence layers.

### 2. Closed blocks

0B-01 through 0B-05B are **`APPROVED / FROZEN`**. F1–F5 remain provisional; G6 is eliminated and G7 is merged into F2.

### 3. Frozen foundations

Prior freezes distinguish retrieval/reranking/generation; RAG/query transformation/evidentiality/provenance/legal correctness; dataset documentation/versioning/provenance/reproducibility/replication/generalization; and documented knowledge vs complete expertise/legal judgment.

### 4. 0B-05C — Authority, currency, and traceability of normative/official sources

Status: **`READY_FOR_DRAFTING`**.

Scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Active prompt: `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

This is a primary official-source audit comparing the frozen `EXPERIMENTAL_SOURCE_SNAPSHOT` with `CURRENT_OFFICIAL_SOURCE_STATE`.

The experimental snapshot at development ref `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` includes Arancel 2022 and CAN Decision 885/Gazette 4359 with their pipeline metadata and processed artifacts.

The controlled current-official set covers WCO HS 2022/GIR/needed amendments; Andean Decision 885, Decision 906 and Resolution 2592 plus only additional Chapter-87-relevant official instruments; Peru DS 404-2021-EF and materially relevant tariff amendments; and SUNAT sources only for the specific institutional/administrative claims they support.

Current web verification is mandatory and final evidence is restricted to official WCO, Andean Community, SUNAT, gob.pe, MEF or El Peruano sources.

A preliminary definition-stage flag is open: Decision 906, effective 2023-01-01, modifies Decision 885 and includes Chapter-87 changes such as 8704.41.10 and 8704.51.10. Those codes are not among the frozen 42 EVAL reference labels, but zero impact cannot be inferred because candidate/historical/evidence overlap remains to be tested.

`PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`.

Mandatory distinction:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

If material overlap is confirmed or reasonably remains open, the deliverable must return `EXPERIMENTAL_IMPACT_REVIEW_REQUIRED` without changing experiments, 0A, claims, or Master Plan.

Resolution 2592 was preliminarily identified as complementary explanatory notes for Chapters 1–22 and therefore does not by itself establish Chapter-87 impact.

### 5. 0B-06

Status: `NOT_STARTED / CLOSED_BY_GATE`. It is assessed only after 0B-05C freezes and only if a genuine bibliographic need remains.

### 6. Gate

`0B-05C READY_FOR_DRAFTING -> official-source analysis -> internal scientific/editorial review -> [experimental AI if triggered] -> correction/normalization if needed -> express author approval -> freeze -> assess genuine need for 0B-06`.

The experimental AI retains exclusive authority over the Master Plan and experimental corrective decisions.

### 7. Current state

Phase 0B is open; 0B-01 through 0B-05B are frozen; 0B-05C is the active `READY_FOR_DRAFTING` block; the preliminary drift flag is open for audit; 0B-06 and 0C remain gated; target journal remains pending until 0D.
