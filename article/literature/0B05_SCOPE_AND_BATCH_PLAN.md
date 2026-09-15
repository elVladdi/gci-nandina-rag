# 0B-05 — Datos, procedencia, reproducibilidad, conocimiento y fuentes normativas / Data, provenance, reproducibility, knowledge, and normative sources

## Español

### 1. Propósito

`0B-05` completa el mapa de Fase 0B en tres dimensiones que no deben confundirse:

1. documentación/gobernanza de datos;
2. procedencia, trazabilidad, reproducibilidad y auditoría del ciclo de vida;
3. fundamentos de información/conocimiento y autoridad, vigencia y trazabilidad de fuentes normativas/oficiales.

El bloque no declara novelty. Su función es fijar fronteras científicas para describir banco histórico, corpus normativo, versionamiento, provenance, reproducibilidad, conocimiento explícito documental y autoridad normativa sin convertir documentación en correctness ni retrieval en juicio jurídico.

### 2. Sub-lotes

#### 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:

`article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

Fronteras congeladas:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

F3 recibe fundamento documental, no prueba de independencia; F4 conserva la frontera correctness; F5 queda restringido al candidato estrecho de evaluación formal, explícita y separada de auditabilidad documental por salida. G6 sigue eliminado y G7 absorbido en F2.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`APPROVED / FROZEN`**.

Registros:

- Prompt: `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.
- Revisión interna: `article/reviews/0B05B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación: `article/reviews/0B05B_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Lote congelado: Zins; Hildreth & Kimble; Al-Hawamdeh.

Fronteras congeladas:

- `data`, `information` y `knowledge` no son sinónimos universales ni etapas lineales necesarias; sus definiciones/relaciones dependen del marco conceptual;
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`;
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`;
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

`DOCUMENTED_EXPLICIT_KNOWLEDGE` queda autorizado solo como `OPERACIONALIZACION_DEL_PROYECTO`. C1–C8 están integradas. La autoridad, vigencia, jerarquía y suficiencia jurídica de fuentes oficiales se reservan a 0B-05C.

Impacto metodológico: F1/F2/F4/F5 solo `METHOD_BOUNDARY_RELEVANT`; F3 `NOT_RELEVANT_TO_GAP_CANDIDATE`; ningún estado provisional cambia.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado inicial del sublote: **`READY_FOR_DRAFTING`**.

Estado operativo vigente: **`REVISION_REQUIRED`**. La revisión experimental correctiva ya está cerrada; el bloque requiere ahora normalización editorial del entregable previo antes de auditoría final, aprobación del autor y freeze. `ARTICLE_STATUS.md` es la fuente de verdad para el subestado actual, bloqueos y siguiente gate.

Prompt histórico de análisis:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

Prompt vigente de normalización posterior al cierre experimental:

`article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md`.

Revisión editorial que gobierna esta transición:

`article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`.

##### 2.1 Naturaleza del bloque

0B-05C es una auditoría de **fuentes primarias oficiales**, no un lote de literatura académica. Su eje gobernante es separar:

`EXPERIMENTAL_SOURCE_SNAPSHOT`

versus

`CURRENT_OFFICIAL_SOURCE_STATE`.

Una modificación normativa posterior no reemplaza retroactivamente la fuente usada por el experimento; a la vez, una fuente experimental identificable no prueba por sí sola que el corpus representara toda la normativa vigente en la fecha de ejecución.

##### 2.2 Snapshot experimental confirmado para auditar

Ref de desarrollo congelado por 0A-02:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

Fuentes efectivamente procesadas documentadas en GitHub:

1. `data/external/Arancel 2022.pdf`;
2. `data/processed/corpus/arancel/arancel2022_run_metadata.json`;
3. `data/external/CAN Desición 885 - Nanadina Gaceta 4359.pdf`;
4. `data/processed/corpus/nandina/run_metadata.json`.

SHA-256 de fuente registrados por los metadatos del pipeline:

- `Arancel 2022.pdf`: `a01a029e1ca29b6debc61d219c17dfc086354e00669246cc24a91ad9f454c7d0`;
- `CAN Desición 885 - Nanadina Gaceta 4359.pdf`: `8c4a30fb0328f151089ac4c7857ac447d3dd353de97122a11bde4550d594f0c6`.

Estos son hashes de los archivos fuente procesados, no blob SHA de GitHub.

##### 2.3 Conjunto oficial primario controlado

La auditoría cubrió, como mínimo:

**WCO/OMA — nivel HS**

- Convenio Internacional del Sistema Armonizado, en lo necesario para definir qué integra el HS y el papel de GIR/notas;
- HS Nomenclature 2022 edition;
- General Rules for the Interpretation of the Harmonized System — edición 2022;
- enmiendas complementarias de HS 2022 cuando fueron necesarias para determinar vigencia;
- estatus de Explanatory Notes solo para claims que lo requirieron.

**Comunidad Andina — nivel NANDINA**

- Decisión 885 — Gaceta Oficial 4359;
- Decisión 906 — Gaceta Oficial 5062;
- Resolución 2592 — Gaceta Oficial 5761, `2026-05-18`, Notas Explicativas Complementarias de la NANDINA;
- solo otros instrumentos oficiales estrictamente necesarios para establecer vigencia/impacto de Capítulo 87.

**Perú — nivel nacional/procedimental**

- Decreto Supremo N.° 404-2021-EF — Arancel de Aduanas 2022;
- modificaciones posteriores del Arancel de Aduanas 2022 materialmente necesarias para determinar afectación de Capítulo 87;
- SUNAT/gob.pe `Nomenclatura común Nandina` como orientación institucional, no sustituto de la norma comunitaria;
- `DESPA-PG.01 — Importación para el consumo (versión 8)` solo para claims de procedencia/contexto de DAM;
- `DESPA-PE.00.03 — Reconocimiento físico - extracción y análisis de muestras (versión 4)` solo para claims de reconocimiento físico/muestras.

Las fuentes estadísticas/anuarios quedan fuera del núcleo salvo necesidad documental explícita.

##### 2.4 Hallazgo documental y cierre experimental posterior

La auditoría confirmó que **Decisión 906** modifica la Decisión 885, entró en vigencia el `2023-01-01` e incluye modificaciones de descripción en subpartidas del **Capítulo 87**, entre ellas `8704.41.10` y `8704.51.10`.

También se confirmó que las 42 etiquetas de referencia EVAL v0.2 listadas en `historical_support_by_code_v0.2.csv` no incluyen esos dos códigos. Esa ausencia no permitía concluir impacto cero y activó correctamente la revisión experimental.

El estado histórico de apertura fue:

`PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`.

Posteriormente se confirmó:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25
```

La sensibilidad correctiva final cerró el impacto experimental de forma diferenciada por método:

```text
EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
```

Estos estados no sustituyen retrospectivamente el snapshot experimental original. Describen exclusivamente la sensibilidad correctiva auditada.

La Resolución 2592 de 2026 se identificó como notas complementarias para capítulos 1–22; su presencia en el estado oficial actual no implica por sí misma afectación directa del Capítulo 87.

##### 2.5 Distinciones obligatorias

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_SUBHEADING-10`

`INSTITUTIONAL_ORIENTATION_PAGE ≠ SUPRANATIONAL_LEGAL_INSTRUMENT`

`TEXT_AUXILIARY_FOR_INTERPRETATION ≠ BINDING_NORM`, salvo soporte oficial expreso sobre su estatus.

##### 2.6 Relación con F1–F5

0B-05C no es un pressure test de novelty:

- F1: como máximo `METHOD_BOUNDARY_RELEVANT`;
- F2: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`, salvo frontera explanation ≠ official decision;
- F3: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`;
- F4: `METHOD_BOUNDARY_RELEVANT`;
- F5: `METHOD_BOUNDARY_RELEVANT`.

G6 permanece eliminado; G7 absorbido en F2.

### 3. Relación con freezes previos y trigger experimental

0B-05C no reabre 0A ni los resultados experimentales congelados. La auditoría documental detectó drift y activó un gate experimental que ya fue completado. La rama editorial no modifica el corpus, no reejecuta experimentos, no recalcula resultados y no modifica el Plan Maestro.

Para la normalización editorial actual:

`EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

Una nueva revisión experimental solo se reabriría si la normalización introdujera una contradicción científica nueva con la fuente experimental canónica.

### 4. Gate

Completados:

`0B-05A -> APPROVED / FROZEN`

`0B-05B -> APPROVED / FROZEN`

Flujo histórico de 0B-05C:

`READY_FOR_DRAFTING -> análisis documental -> revisión interna -> EXPERIMENTAL_REVIEW -> auditoría/pre-registro -> sensibilidad correctiva -> cierre experimental`.

Gate operativo vigente:

`0B-05C STATUS = REVISION_REQUIRED -> IA de Redacción normaliza el entregable mediante prompt versionado -> auditoría científica/editorial final -> [revisión experimental solo si aparece contradicción nueva] -> aprobación expresa del autor -> freeze 0B-05C -> evaluar necesidad real de 0B-06`.

Mientras 0B-05C continúe abierto:

- no se redacta el manuscrito;
- no se declara novelty/gap definitivo;
- no se modifica 0A ni el Plan Maestro;
- no se actualiza el corpus ni se rerun experimentos desde la rama editorial;
- `0B-06` permanece `NOT_STARTED` y su apertura no está autorizada;
- 0C permanece bloqueado.

---

## English

### 1. Purpose

`0B-05` completes Phase 0B across data documentation/governance; provenance/reproducibility/lifecycle audit; and information/knowledge foundations plus official normative-source authority, currency, and traceability. It does not establish novelty.

### 2. Sub-batches

#### 0B-05A

Status: **`APPROVED / FROZEN`**. Frozen distinctions separate documentation, identity/versioning, provenance, reproducibility, replication, generalization, lifecycle audit, output-level auditability, and substantive/legal correctness.

#### 0B-05B

Status: **`APPROVED / FROZEN`**. Frozen boundaries reject universal DIKW sequencing, distinguish documented knowledge from total expertise, document retrieval from expert/legal interpretation, and LLM explanation from expert knowledge/official classification. `DOCUMENTED_EXPLICIT_KNOWLEDGE` is project operationalization only.

#### 0B-05C — Authority, currency, and traceability of normative/official sources

Initial sub-batch status: **`READY_FOR_DRAFTING`**.

Current operational status: **`REVISION_REQUIRED`**. The corrective experimental review is closed; the block now requires editorial normalization of the prior deliverable before final audit, author approval, and freeze. `ARTICLE_STATUS.md` is the source of truth for the current substate, blockers, and next gate.

Historical analysis prompt:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

Current post-experimental-closure normalization prompt:

`article/prompts/0B05C_FINAL_NORMALIZATION_AFTER_EXPERIMENTAL_CLOSURE.md`.

Editorial review governing this transition:

`article/reviews/0B05C_FINAL_EXPERIMENTAL_RECONCILIATION_EDITORIAL_REVIEW.md`.

0B-05C is a primary official-source audit, not an academic-literature batch. It separates the exact experimental normative-source snapshot at development ref `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` from the current official-source state.

The frozen experimental source snapshot includes `Arancel 2022.pdf` and the CAN Decision 885/Gazette 4359 PDF, with recorded source-file SHA-256 values `a01a029e...454c7d0` and `8c4a30fb...594f0c6`, respectively, plus their run metadata and processed artifacts.

The controlled official set covers WCO HS 2022/GIR/necessary amendments; Andean Decision 885, Decision 906, Resolution 2592 and only other Chapter-87-relevant official instruments; Peru DS 404-2021-EF and material tariff modifications; the SUNAT NANDINA orientation page; and DESPA-PG.01 v8 / DESPA-PE.00.03 v4 only for administrative-data provenance claims.

The official-source audit confirmed that Decision 906, effective 2023-01-01, modifies Decision 885 and includes Chapter-87 description changes for `8704.41.10` and `8704.51.10`. The two codes are not among the 42 frozen EVAL reference labels, but that negative intersection did not justify zero-impact inference and correctly triggered experimental review.

The historical opening state was `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`. The subsequent audit and experimental closure established:

```text
SOURCE_VERSION_DRIFT = PRESENT
SCOPE_OVERLAP = CONFIRMED
RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25

EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
```

These states do not retrospectively replace the original experimental snapshot. They describe only the audited corrective sensitivity.

Resolution 2592 (2026) was identified as complementary explanatory notes for Chapters 1–22, so its current existence does not itself establish direct Chapter-87 impact.

Mandatory boundaries:

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_SUBHEADING-10`

`INSTITUTIONAL_ORIENTATION_PAGE ≠ SUPRANATIONAL_LEGAL_INSTRUMENT`.

### 3. Prior freezes and experimental trigger

0B-05C does not reopen frozen experimental facts. The official-source audit detected drift and triggered an experimental gate that has now been completed. The editorial branch does not modify the corpus, rerun experiments, recalculate results, or modify 0A/Master Plan.

For the current editorial normalization:

`EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

A new experimental review is required only if the normalization introduces a new scientific contradiction with the canonical experimental source.

### 4. Gate

Historical 0B-05C flow:

`READY_FOR_DRAFTING -> documentary analysis -> internal review -> EXPERIMENTAL_REVIEW -> audit/preregistration -> corrective sensitivity -> experimental closure`.

Current operational gate:

`0B-05C STATUS = REVISION_REQUIRED -> Writing AI normalizes the deliverable through the versioned prompt -> final scientific/editorial audit -> [experimental review only if a new contradiction appears] -> express author approval -> freeze 0B-05C -> assess genuine need for 0B-06`.

While 0B-05C remains open, manuscript drafting and final novelty/gap declaration remain unauthorized; editorial-branch 0A/Master-Plan modification and corpus update/rerun remain prohibited; `0B-06` remains `NOT_STARTED` with opening unauthorized; and 0C remains blocked.