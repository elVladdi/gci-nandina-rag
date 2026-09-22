# D-041 — Experimental Design B01 opening

## Español

```text
DECISION_ID = D-041
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-040
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = AUTHORIZED / ACTIVE
AUTHORIZED_SCOPE = SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Objetivo del bloque

Se abre el primer bloque atómico de Section 4 — Experimental design. Su función es trasladar al lector desde la arquitectura general ya cerrada hacia la instanciación empírica concreta, sin repetir Section 3 ni anticipar resultados.

B01 comprende exclusivamente:

- `4.1 Evaluation setting` / `Escenario de evaluación`;
- `4.2 Historical data` / `Datos históricos`;
- `4.2.1 Data source and selection` / `Fuente de datos y selección`;
- `4.2.2 Target class space` / `Espacio de clases objetivo`;
- `4.2.3 Preparation and curation` / `Preparación y curación`;
- `4.2.4 Versioned datasets used in the experiment` / `Datasets versionados utilizados en el experimento`.

No se autoriza 4.3 ni subsecciones posteriores.

## 2. Ground truth experimental autorizado

La fuente viva gobernante `SRC-03` fue verificada en modo de solo lectura:

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_HEAD = b74b96d0163807007e4579d86450dd235125b30f
SRC03_PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
SRC03_BLOB = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
DEVELOPMENT_MAIN_CHECKPOINT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

El benchmark v0.2 congelado registra:

```text
ANALYSIS_UNIT = SERIE
GROUPING_UNIT_WHEN_DEPENDENCE_IS_RELEVANT = DAM / DECLARACION
EMPIRICAL_SCOPE = NANDINA CHAPTER 87
H100 = 2950 SERIES / 28 DAM / 66 REPRESENTED CODES
DEV = 100 SERIES / 6 DAM / 9 REPRESENTED CODES
EVAL = 1056 SERIES / 67 DAM / 42 REPRESENTED REFERENCE CODES
H100_SHA256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
DEV_SHA256 = 434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00
EVAL_SHA256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

Fuente técnica primaria para la identidad de las particiones:

`data/processed/data_aduanas_splits_clase87_v0.2_metadata.json@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`

Git blob verificado en el mismo contenido: `bcb02c9c3493235a6f80991158c5b24fa7c04510`.

La configuración congelada es:

`src/configs/data_aduanas_split_clase87_v0.2.json@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`

Git blob: `059eb81677dad92d6f9241f0b8cbbff9bba332cd`.

La estrategia v0.2 es `T5-safe-159`. El campo `seed = 2026` permanece como atributo de configuración/procedencia; la asignación v0.2 se materializa mediante listas explícitas de DAM y no mediante aleatoriedad ni selección basada en métricas del modelo.

La metadata confirma asignación completa de 4,106 registros curados, cero solapamiento de DAM y `id_unico` entre histórico/desarrollo/evaluación, y soporte histórico nominal para 1,056/1,056 casos de evaluación. El detalle de independencia, duplicados y near-duplicates pertenece principalmente a 4.4 y no debe sobrecargar B01.

## 3. Procedencia y límite forense

La trazabilidad histórica del origen debe redactarse con especial cautela.

El Plan Maestro registra que el workbook actual `data/Series - Descripciones.xlsx` reproduce funcionalmente el contenido procesado por el parser para la reconstrucción histórica pertinente, pero el workbook histórico completo no es byte-identificable con el workbook actual. La metadata histórica registraba un SHA distinto del workbook actual. El pipeline histórico fue clasificado conservadoramente como `PIPELINE_PARTIALLY_RECONSTRUCTED`.

Por tanto, B01 puede describir la procedencia verificable, el parser, la hoja procesada y los datasets derivados congelados, pero no puede afirmar identidad binaria del workbook histórico original. Debe distinguirse explícitamente equivalencia funcional del contenido procesado de identidad binaria de la fuente original.

Hechos documentados:

- workbook actual: `data/Series - Descripciones.xlsx`;
- SHA actual: `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`;
- hoja procesada históricamente: `Hoja2`, índice 0, por selección de la primera hoja cuando no se proporcionaba `--sheet`;
- intermedio reproducido: 107 DAM / 11,320 series;
- Chapter 87: 4,232 filas antes de curación y 4,106 registros curados;
- los tres datasets v0.2 se reprodujeron byte a byte.

No debe trasladarse al manuscrito la historia operativa de gates o auditorías; solo los hechos metodológicos relevantes y sus límites.

## 4. Claims y fronteras

Claims especialmente relevantes:

- C06 `AUTHORIZED`: v0.2 evita solapamiento de DAM entre histórico, desarrollo y evaluación;
- C07 `AUTHORIZED`: la dependencia intra-DAM debe respetarse cuando la inferencia requiera independencia;
- C19 `AUTHORIZED`: el solapamiento del split v0.1 puede utilizarse únicamente como snapshot histórico cuando sea metodológicamente necesario;
- C20 `REVIEW_REQUIRED`: `48/59 DAM` no puede utilizarse como cifra congelada;
- C21 `AUTHORIZED`: el drift documental/normativo puede tratarse posteriormente dentro de sus límites; no debe introducirse en B01 salvo necesidad directa y no autoriza inferencia de legal correctness o impacto métrico.

B01 no debe introducir resultados de candidate retrieval, resultados de hipótesis, HE2/HE5, EXP11A/EXP11B/EXP12, ni cifras de desempeño. Tampoco debe presentar los 66 códigos históricos como el universo completo de Chapter 87: son códigos representados en el banco histórico H100 de esta instanciación. Los 42 códigos de EVAL son etiquetas de referencia representadas en ese conjunto de evaluación.

El sistema se describe como piloto offline de apoyo no vinculante. No produce una clasificación aduanera jurídicamente vinculante.

## 5. Relación con artefactos heredados

`article/sections/methods/Methods_B01_V05.md` puede consultarse únicamente como artefacto legado de formulaciones previamente auditadas. No es el master canónico y no puede copiarse como estructura de Section 4. Sus párrafos de configurabilidad ya quedaron absorbidos por Section 3.7 y no deben duplicarse.

Cualquier discrepancia entre ese legado y las fuentes experimentales primarias se resuelve a favor de `SRC-03` y de los artefactos congelados del repositorio de desarrollo.

## 6. Compatibilidad de gobernanza y transferencia

Antes de abrir este bloque se verificó compatibilidad con D-021, D-022, D-023, D-035, D-039 y D-040.

Para B01 se reutiliza el patrón timeout-safe ya probado:

1. el archivo de sección, relativamente pequeño, puede versionarse directamente en GitHub;
2. la respuesta operacional pequeña se versiona en GitHub;
3. el master Markdown acumulativo candidato grande se entrega al autor como archivo exacto descargable con SHA-256;
4. el DOCX acumulativo candidato se entrega al autor como archivo exacto descargable con SHA-256;
5. no se intenta transferir el master acumulativo grande por la vía directa que ya produjo timeout;
6. no se usa Base64 manual, fragmentación, chunking, recomposición, archivos auxiliares ni múltiples commits como workaround;
7. la codificación interna automática del conector no se considera Base64 manual.

## 7. Gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = DRAFT_SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
EXPERIMENTAL_DESIGN_B01 = AUTHORIZED
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-041
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-040
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = AUTHORIZED / ACTIVE
AUTHORIZED_SCOPE = SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Block objective

The first atomic Section-4 block is opened. It moves the reader from the closed general architecture to the concrete empirical instantiation without repeating Section 3 or anticipating Results.

B01 covers only Section 4.1 and Sections 4.2.1–4.2.4: evaluation setting; historical-data source and selection; represented target-code space; preparation/curation; and the versioned datasets used in the experiment. Section 4.3 and all later subsections remain unauthorized.

### 2. Authorized experimental ground truth

The governing living source `SRC-03` was verified read-only at `docs/plan-maestro-temporal-2026-08-31@b74b96d0163807007e4579d86450dd235125b30f`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`, blob `7b63fdb14b75eace173ac3c94775d39ed7ed7a57`. The development checkpoint currently relevant to the article is `main@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`.

The frozen v0.2 benchmark uses SERIE as the analysis unit and DAM/declaration as the grouping unit when dependence matters. Its empirical scope is NANDINA Chapter 87. H100 contains 2,950 series from 28 DAM and 66 represented codes; DEV contains 100 series from 6 DAM and 9 represented codes; EVAL contains 1,056 series from 67 DAM and 42 represented reference codes. The approved SHA-256 values are those listed in the Spanish control version above.

The canonical split metadata and configuration are `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json` (blob `bcb02c9c3493235a6f80991158c5b24fa7c04510`) and `src/configs/data_aduanas_split_clase87_v0.2.json` (blob `059eb81677dad92d6f9241f0b8cbbff9bba332cd`) at the development checkpoint. Strategy `T5-safe-159` materializes v0.2 through explicit DAM lists. `seed=2026` remains configuration/provenance metadata rather than the mechanism that assigns v0.2 partitions.

The metadata confirms complete assignment of 4,106 curated records, zero DAM and `id_unico` overlap across historical/development/evaluation partitions, and nominal historical support for all 1,056 evaluation records. Duplicate and near-duplicate diagnostics belong primarily to Section 4.4 rather than B01.

### 3. Provenance and forensic boundary

The current workbook `data/Series - Descripciones.xlsx` functionally reproduces the parser-processed content relevant to the historical reconstruction, but the full historical workbook is not byte-identifiable with the current workbook. The historical pipeline is conservatively classified as partially reconstructed. B01 may report verifiable provenance, parser behavior, the historically processed worksheet, and frozen derived datasets, but it must not claim binary identity of the original historical workbook. Functional equivalence of processed content and binary identity of the original source must remain distinct.

Documented facts include the current workbook SHA, historical processing of `Hoja2` as worksheet index 0 when no `--sheet` was supplied, a reproduced intermediate of 107 DAM / 11,320 series, 4,232 Chapter-87 rows before curation, 4,106 curated records, and byte-exact reproduction of the three v0.2 datasets. Internal gate/audit chronology must not be transferred to publishable prose.

### 4. Claims and boundaries

C06 and C07 are authorized. C19 may be used only as a historical v0.1 snapshot if methodologically needed. C20 remains review-required and its `48/59 DAM` figure must not be used as frozen evidence. C21 remains bounded to documentary/normative drift and does not authorize legal-correctness or metric-impact inference.

B01 must not introduce retrieval-performance values, hypothesis outcomes, HE2/HE5, EXP11A/EXP11B/EXP12 results, or any Results prose. The 66 H100 codes are represented codes in this empirical historical bank, not a claim that they exhaust the entire Chapter-87 nomenclature. The 42 EVAL codes are represented reference labels in the evaluation set. The system is an offline, non-binding decision-support pilot and does not issue legally binding customs classifications.

### 5. Legacy artifact

`article/sections/methods/Methods_B01_V05.md` is a legacy audited wording artifact only. It is not the canonical manuscript structure. Its configurability paragraphs are already represented in Section 3.7 and must not be duplicated in Section 4. Primary experimental sources take precedence over the legacy file.

### 6. Governance and transfer compatibility

D-021, D-022, D-023, D-035, D-039, and D-040 were checked before opening B01. The proven timeout-safe pattern is reused: the small section artifact and small operational response may be committed directly; the large cumulative Markdown candidate and DOCX candidate are delivered to the author as exact downloadable files with hashes. The previously failing large direct-transfer path must not be retried. Manual Base64, fragmentation/chunking, recomposition, auxiliary-file, or multi-commit workarounds remain prohibited. Automatic connector encoding is permitted.

### 7. Gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = DRAFT_SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
EXPERIMENTAL_DESIGN_B01 = AUTHORIZED
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
