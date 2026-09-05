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

Estado operativo vigente: **`EXPERIMENTAL_REVIEW`**. `ARTICLE_STATUS.md` es la fuente de verdad para el subestado correctivo, bloqueos y siguiente gate. El estado inicial anterior se conserva solo como registro histórico de apertura del sublote; fue superado operacionalmente por el trigger experimental confirmado durante la auditoría.

Prompt activo:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

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

La auditoría debe cubrir, como mínimo:

**WCO/OMA — nivel HS**

- Convenio Internacional del Sistema Armonizado, en lo necesario para definir qué integra el HS y el papel de GIR/notas;
- HS Nomenclature 2022 edition;
- General Rules for the Interpretation of the Harmonized System — edición 2022;
- enmiendas complementarias de HS 2022 cuando sean necesarias para determinar vigencia;
- estatus de Explanatory Notes solo para claims que lo requieran.

**Comunidad Andina — nivel NANDINA**

- Decisión 885 — Gaceta Oficial 4359;
- Decisión 906 — Gaceta Oficial 5062;
- Resolución 2592 — Gaceta Oficial 5761, `2026-05-18`, Notas Explicativas Complementarias de la NANDINA;
- solo otros instrumentos oficiales estrictamente necesarios para establecer vigencia/impacto de Capítulo 87.

**Perú — nivel nacional/procedimental**

- Decreto Supremo N.° 404-2021-EF — Arancel de Aduanas 2022;
- modificaciones posteriores del Arancel de Aduanas 2022 cuando sean materialmente necesarias para determinar afectación de Capítulo 87;
- SUNAT/gob.pe `Nomenclatura común Nandina` como orientación institucional, no sustituto de la norma comunitaria;
- `DESPA-PG.01 — Importación para el consumo (versión 8)` solo para claims de procedencia/contexto de DAM;
- `DESPA-PE.00.03 — Reconocimiento físico - extracción y análisis de muestras (versión 4)` solo para claims de reconocimiento físico/muestras.

Las fuentes estadísticas/anuarios quedan fuera del núcleo salvo necesidad documental explícita.

##### 2.4 Web oficial autorizada

A diferencia de 0B-01–0B-05B, 0B-05C **requiere consulta web actual**. La evidencia final debe proceder de fuentes oficiales:

- `wcoomd.org` / infraestructura oficial WCO;
- `comunidadandina.org`;
- `sunat.gob.pe`;
- `gob.pe`;
- `mef.gob.pe`;
- `elperuano.pe`.

Buscadores pueden utilizarse solo para descubrimiento. Agregadores, blogs, bases jurídicas de terceros y papers no son autoridad final de este bloque.

##### 2.5 Hallazgo preliminar que debe auditarse, no asumirse como impacto

Durante la definición del lote se verificó en fuente oficial que **Decisión 906** modifica la Decisión 885, entró en vigencia el `2023-01-01` e incluye modificaciones de descripción en subpartidas del **Capítulo 87**, entre ellas `8704.41.10` y `8704.51.10`.

También se verificó que las 42 etiquetas de referencia EVAL v0.2 listadas en `historical_support_by_code_v0.2.csv` no incluyen esos dos códigos. Esto **no permite concluir impacto cero**, porque los códigos podrían aparecer como candidatos, en el banco histórico o en evidencia normativa.

Por tanto, al abrir 0B-05C se registró inicialmente:

`PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`

Ese valor describe el estado histórico de apertura del sublote. El resultado vigente de la auditoría y del trigger experimental se mantiene exclusivamente en `ARTICLE_STATUS.md`; este plan no debe utilizarse como fuente de verdad para inferir que el flag continúa abierto.

No se modifica ningún resultado experimental ni 0A. El entregable debe comprobar el solapamiento concreto y, si corresponde, devolver `EXPERIMENTAL_IMPACT_REVIEW_REQUIRED` para que la IA experimental determine materialidad y acciones.

La Resolución 2592 de 2026 se identificó preliminarmente como notas complementarias para capítulos 1–22; su presencia en el estado oficial actual no implica por sí misma afectación directa del Capítulo 87.

##### 2.6 Distinciones obligatorias

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_SUBHEADING-10`

`INSTITUTIONAL_ORIENTATION_PAGE ≠ SUPRANATIONAL_LEGAL_INSTRUMENT`

`TEXT_AUXILIARY_FOR_INTERPRETATION ≠ BINDING_NORM`, salvo soporte oficial expreso sobre su estatus.

##### 2.7 Relación con F1–F5

0B-05C no es un pressure test de novelty:

- F1: como máximo `METHOD_BOUNDARY_RELEVANT`;
- F2: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`, salvo frontera explanation ≠ official decision;
- F3: normalmente `NOT_RELEVANT_TO_GAP_CANDIDATE`;
- F4: `METHOD_BOUNDARY_RELEVANT`;
- F5: `METHOD_BOUNDARY_RELEVANT`.

G6 permanece eliminado; G7 absorbido en F2.

### 3. Relación con freezes previos y trigger experimental

0B-05C no reabre 0A ni los resultados experimentales congelados. La auditoría documental puede detectar drift; no puede resolverlo mediante modificación del corpus, rerun, recalculo o reinterpretación de resultados.

La IA experimental se vuelve obligatoria **solo si** el análisis confirma o deja razonablemente abierto un solapamiento material entre drift normativo y componentes experimentales congelados. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro y sobre cualquier decisión experimental correctiva.

### 4. Gate

Completados:

`0B-05A -> APPROVED / FROZEN`

`0B-05B -> APPROVED / FROZEN`

Flujo inicial registrado al abrir 0B-05C:

`0B-05C READY_FOR_DRAFTING -> IA de análisis -> auditoría de fuentes oficiales -> revisión científica/editorial interna -> [IA experimental si trigger confirmado] -> corrección/normalización si aplica -> aprobación expresa del autor -> freeze -> evaluar necesidad real de 0B-06`.

Gate operativo vigente:

`0B-05C STATUS = EXPERIMENTAL_REVIEW -> IA experimental resuelve la exposición efectiva y especificación pre-ejecución D1a -> sensibilidad correctiva acotada cuando quede autorizada -> revisión científica/editorial final -> corrección/normalización si corresponde -> aprobación expresa del autor -> freeze -> evaluar necesidad real de 0B-06`.

Los flags y bloqueos concretos deben consultarse en `ARTICLE_STATUS.md`.

Mientras 0B-05C esté abierto:

- no se redacta el manuscrito;
- no se declara novelty/gap definitivo;
- no se modifica 0A ni el Plan Maestro;
- no se actualiza el corpus ni se rerun experimentos desde la rama editorial;
- no se abre 0B-06 ni 0C.

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

Current operational status: **`EXPERIMENTAL_REVIEW`**. `ARTICLE_STATUS.md` is the source of truth for the corrective substate, blockers, and next gate. The former initial state is preserved only as the historical opening state of the sub-batch; it was operationally superseded by the experimental trigger confirmed during the audit.

Active prompt:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

0B-05C is a primary official-source audit, not an academic-literature batch. It separates the exact experimental normative-source snapshot at development ref `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` from the current official-source state.

The frozen experimental source snapshot includes `Arancel 2022.pdf` and the CAN Decision 885/Gazette 4359 PDF, with recorded source-file SHA-256 values `a01a029e...454c7d0` and `8c4a30fb...594f0c6`, respectively, plus their run metadata and processed artifacts.

The controlled official set covers WCO HS 2022/GIR/necessary amendments; Andean Decision 885, Decision 906, Resolution 2592 and only other Chapter-87-relevant official instruments; Peru DS 404-2021-EF and material tariff modifications; the SUNAT NANDINA orientation page; and DESPA-PG.01 v8 / DESPA-PE.00.03 v4 only for administrative-data provenance claims.

Current web verification is required, but final evidence must come from official WCO, Andean Community, SUNAT, gob.pe, MEF or El Peruano sources.

The definition-stage finding was initially recorded as `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`: Decision 906, effective 2023-01-01, modifies Decision 885 and contains Chapter-87 modifications including 8704.41.10 and 8704.51.10. Those codes are not among the 42 EVAL reference labels in the frozen support-by-code table, but zero experimental impact cannot be inferred because they may occur as candidates, historical labels, or evidence. That flag represents the historical opening state only; the current audit outcome and experimental trigger are governed by `ARTICLE_STATUS.md`.

Resolution 2592 (2026) was preliminarily identified as complementary explanatory notes for Chapters 1–22, so its current existence does not itself establish direct Chapter-87 impact.

Mandatory boundaries:

`OFFICIAL_SOURCE ≠ LEGALLY_SUFFICIENT_FOR_CASE ≠ CORRECT_CLASSIFICATION`

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`

`HS-6 ≠ NANDINA-8 ≠ PERU_NATIONAL_SUBHEADING-10`

`INSTITUTIONAL_ORIENTATION_PAGE ≠ SUPRANATIONAL_LEGAL_INSTRUMENT`.

### 3. Prior freezes and experimental trigger

0B-05C does not reopen frozen experimental facts. It may detect source drift but cannot update the corpus, rerun experiments, recalculate results, or modify 0A/Master Plan from the editorial branch.

Experimental-AI review becomes required only if the official-source audit confirms or reasonably leaves open a material overlap between normative drift and frozen experimental components. The experimental AI retains exclusive authority over the Master Plan and experimental corrective decisions.

### 4. Gate

Initial flow recorded when 0B-05C was opened:

`0B-05C READY_FOR_DRAFTING -> official-source analysis AI -> official-source audit -> internal review -> [experimental AI if triggered] -> correction/normalization if needed -> express author approval -> freeze -> assess genuine need for 0B-06`.

Current operational gate:

`0B-05C STATUS = EXPERIMENTAL_REVIEW -> experimental AI resolves effective D1a exposure and pre-execution specification -> bounded corrective sensitivity when authorized -> final scientific/editorial review -> correction/normalization if needed -> express author approval -> freeze -> assess genuine need for 0B-06`.

Concrete flags and blockers must be read from `ARTICLE_STATUS.md`.

No manuscript drafting, final novelty/gap declaration, editorial-branch 0A/Master-Plan modification, editorial-branch corpus update/rerun, 0B-06, or 0C is authorized while 0B-05C remains open.