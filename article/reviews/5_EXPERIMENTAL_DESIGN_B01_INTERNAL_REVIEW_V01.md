# Experimental Design B01 — Internal review V01

## Español

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_B01_INTERNAL_REVIEW_V01
BLOCK = EXPERIMENTAL_DESIGN_B01
REVIEWER = IA_GESTORA
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B01_RESPONSE_V01.md@18cb9d9173ebc140baeb7e77ae3e70ea373c9a4e
GOVERNING_DECISION = article/governance/D041_EXPERIMENTAL_DESIGN_B01_OPENING.md
CANONICAL_BASELINE_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_BASELINE_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
SECTION_MD_SHA256 = fe80017f26010c4125b3abaec41ce066d91b63e1ff5ca54fa98baea0bea90e78
SECTION_MD_GIT_BLOB = b876bef94d75c0c8c676f5a4fa3276cbb22fbd28
MASTER_CANDIDATE_MD_SHA256 = 6e443353c362410ffe70c880b49647a12b1a88d3ec72a12675cce5e086435754
CANDIDATE_DOCX_SHA256 = 4089ca75267ed05d1406b9bf2c1f895300f4da77ccb3e0559b2ef43ad49f3e5c
SCIENTIFIC_CONTENT_REVIEW = PASS
CLAIM_EVIDENCE_REVIEW = PASS
AUTHORIZED_SCOPE_REVIEW = PASS
PRIOR_APPROVED_CONTENT_PRESERVATION = PASS
SECTION_4_3_AND_LATER_PRESERVATION = PASS
RESULTS_LEAKAGE = NONE
NEW_LITERATURE = NONE
PART_I_PART_II_SCIENTIFIC_EQUIVALENCE = PASS
OOXML_QA = PASS
DOCX_COMMENT_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
TRACKED_CHANGES = 0
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 41
STRUCTURAL_PLACEHOLDER_REVIEW = FAIL_ONE_MINOR
OVERALL_REVIEW = PASS_WITH_ONE_MINOR_CORRECTION
AUTHOR_APPROVAL_GATE = NOT_OPEN
ARTICLE_MASTER_V010 = NOT_PROMOTED
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Dictamen científico

El contenido redactado para 4.1 y 4.2.1–4.2.4 es científicamente aceptable dentro del alcance autorizado. La auditoría independiente confirmó que los hechos principales son trazables a las fuentes experimentales gobernantes: SERIE como unidad de análisis, DAM/DECLARACION como agrupamiento cuando existe dependencia, alcance empírico en Capítulo 87, composición e identidades SHA-256 de H100/DEV/EVAL, estrategia `T5-safe-159`, asignación v0.2 mediante listas explícitas de DAM, ausencia de solapamiento DAM/`id_unico`, procedencia limitada del workbook disponible, comportamiento del parser, conteos 11,320/107, 4,232 y 4,106, reglas de curación y reproducción byte-exacta de los tres CSV v0.2.

No se detectaron métricas de desempeño, resultados de hipótesis, claims de corrección jurídica, generalización empírica, novelty o contenido de Results. La separación entre códigos representados y universo completo de Capítulo 87 se mantiene correctamente.

### 2. Verificación de artefactos

La entrega local coincide con los hashes reportados por la IA de Redacción. El archivo de sección versionado en GitHub es reconstruible exactamente desde el master candidato: SHA-256 `fe80017f26010c4125b3abaec41ce066d91b63e1ff5ca54fa98baea0bea90e78` y Git blob `b876bef94d75c0c8c676f5a4fa3276cbb22fbd28`.

El DOCX candidato parte del baseline exacto. Conserva 40 comentarios, el `comments.xml` heredado byte a byte, cero tracked changes y modifica únicamente `word/document.xml`. La comparación de párrafos baseline→candidato no detectó cambios fuera del bloque B01. El render completo produjo 41 páginas; todas fueron inspeccionadas y no presentan clipping, solapamientos, pérdida de glifos ni roturas de layout.

### 3. Única corrección obligatoria

El master acumulativo Markdown y el DOCX conservan un placeholder genérico obsoleto exclusivamente en la Parte II, inmediatamente después de:

`4. Diseño experimental`

`A partir de aquí se introduce la instanciación empírica concreta.`

y antes de:

`4.1. Entorno de evaluación`

La línea residual es:

`[Section text to be drafted in a later approved version.]`

La Parte I no contiene el placeholder equivalente y 4.1–4.2 ya fueron redactadas. Por tanto, mantener esa línea contradice el estado real de Section 4 y rompe la simetría estructural del master bilingüe. Es un defecto editorial/estructural menor, no un defecto científico del texto B01.

La corrección debe eliminar **solo esa línea**. No se autoriza reescritura científica, cambios en `Experimental_Design_B01_V01.md`, modificación de 4.1–4.2.4, modificación de 4.3 o posteriores, promoción de V010 ni apertura de B02.

### 4. Gate

Experimental Design B01 queda `SCIENTIFIC_CONTENT = PASS`, pero el gate de aprobación autoral permanece cerrado hasta recibir y auditar el master acumulativo corregido. Tras la corrección técnica única, la IA Gestora realizará una verificación diferencial acotada y, si pasa, abrirá el gate de aprobación del autor.

---

## English

```text
SCIENTIFIC_CONTENT_REVIEW = PASS
CLAIM_EVIDENCE_REVIEW = PASS
AUTHORIZED_SCOPE_REVIEW = PASS
PRIOR_APPROVED_CONTENT_PRESERVATION = PASS
SECTION_4_3_AND_LATER_PRESERVATION = PASS
DOCX_BINARY_AND_RENDER_QA = PASS
STRUCTURAL_PLACEHOLDER_REVIEW = FAIL_ONE_MINOR
OVERALL_REVIEW = PASS_WITH_ONE_MINOR_CORRECTION
AUTHOR_APPROVAL_GATE = NOT_OPEN
```

### 1. Scientific assessment

The drafted content for Sections 4.1 and 4.2.1–4.2.4 is scientifically acceptable within the authorized scope. Independent review confirmed the principal dataset, provenance, parser, curation, split, count, and hash statements against the governing experimental sources. No performance results, hypothesis outcomes, legal-correctness claims, empirical-generalization claims, novelty claims, or Results prose were introduced.

### 2. Artifact verification

The handed-off cumulative Markdown and DOCX match the SHA-256 identities reported in the execution response. The GitHub section artifact is exactly reconstructible from the cumulative candidate and matches both the reported SHA-256 and Git blob. The DOCX preserves all 40 citation comments, the inherited `comments.xml`, and zero tracked changes. Its complete 41-page rendering passed visual inspection.

### 3. Single mandatory correction

The cumulative Markdown and DOCX retain one stale generic drafting placeholder in Part II between the Spanish Section-4 introductory note and `4.1. Entorno de evaluación`:

`[Section text to be drafted in a later approved version.]`

No equivalent placeholder remains in Part I, and Sections 4.1–4.2 are now drafted. This is a minor structural/editorial defect rather than a scientific defect. The correction is limited to deleting that one line. No scientific redrafting, section-file revision, change to Section 4.3 or later, V010 promotion, or B02 opening is authorized.

### 4. Gate

Experimental Design B01 scientific content passes, but the author-approval gate remains closed until the corrected cumulative master is received and differentially verified by the Managing AI.