# Revisión interna — Experimental Design B03 / Section 4.4 — V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B03_SECTION_4_4
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
REVIEW_VERSION = V01
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4_RESPONSE_V01.md@b9d3b6eabda35e4825fcaa699a75768af6db3c4e
SECTION = article/sections/experimental_design/Experimental_Design_B03_V01.md@bbcc050df7394e1c4cd91d43f1e2e83d1ef483e2
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V011.md
BASELINE_MASTER_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
B03_MASTER_CANDIDATE_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
SCIENTIFIC_CONTENT = PASS
CLAIM_EVIDENCE_AUDIT = PASS
DIFFERENTIAL_MD_AUDIT = PASS
BILINGUAL_EQUIVALENCE = PASS
SCOPE_CONTROL = PASS
DOCX_CONTINUITY = FAIL / MISSING_REQUIRED_CANDIDATE
OVERALL = PASS_WITH_BLOCKING_TECHNICAL_CORRECTION
AUTHOR_APPROVAL_GATE = NOT_OPEN
B04 = NOT_AUTHORIZED
```

### 1. Auditoría independiente

La IA Gestora no adopta como prueba los `PASS` declarados por la IA de Redacción. Se contrastó directamente la prosa de 4.4 contra el prompt gobernante, D-055, D-056, el ground truth experimental congelado y los artefactos primarios de v0.1/v0.2 en `main`.

La afirmación de que v0.1 operaba a nivel de fila/serie mediante muestreo estratificado proporcional por NANDINA con `seed=2026`, sin imponer agrupamiento por DAM, es consistente con `src/evaluation/build_data_aduanas_splits.py` y la metadata v0.1. La formulación usa correctamente un riesgo potencial de dependencia/leakage y no convierte el hallazgo histórico en una afirmación causal o en un resultado del benchmark vigente.

La descripción de v0.2 también es consistente con la evidencia primaria: asignaciones explícitas de DAM, `SERIE` como unidad de análisis, `DECLARACION`/DAM como unidad de agrupamiento, H100=2,950/28/66, DEV=100/6/9, EVAL=1,056/67/42, asignación completa, solapamiento DAM=0, solapamiento `id_unico`=0 y soporte histórico nominal de 1,056/1,056 series y 42/42 códigos de evaluación.

La sección mantiene correctamente separados cuatro controles que no son equivalentes: disjunción por DAM, unicidad de `id_unico`, coincidencias textuales exactas y diagnósticos de near-duplicates. Los umbrales Jaccard 0.90/0.95/0.98 se presentan como diagnósticos y no como filtros de exclusión. La omisión de las cantidades 35/55/44/37 no constituye defecto de Methods: el prompt exigía no adelantar resultados de Section 5 y 4.4 conserva el mecanismo y el alcance metodológico sin convertir esos diagnósticos en resultados narrativos.

La frontera inferencial también es correcta: cero DAM compartidas entre particiones no implica independencia de las series dentro de una DAM; las 1,056 series de EVAL no se presentan como 1,056 observaciones inferenciales independientes; no se declara i.i.d., eliminación total de leakage ni generalización fuera del testbed.

### 2. Control diferencial del master Markdown

Se verificó el artefacto exacto entregado por el autor `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.md`:

- SHA-256 = `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`;
- Git blob esperado = `dfea73f5f462fc65cf98347f796deadc6da58455`.

Comparado contra el baseline exacto aprobado/materializado de B02/V011, el diferencial está restringido a los dos placeholders de Section 4.4 —inglés y español— sustituidos por la prosa B03. No se detectaron cambios en Sections 1–4.3, 4.5+, Results ni en el resto del master.

### 3. Defecto técnico bloqueante: continuidad DOCX

La entrega B03 declaró `DOCX_CANDIDATE = NOT_REQUIRED_BY_THIS_PROMPT / NOT_GENERATED`. Esa interpretación es incompatible con D-021 y con D-055.

D-021 establece que el DOCX acumulativo sigue siendo necesario, que su SHA-256 es obligatorio, que el siguiente bloque que continúe sobre Word debe usar el binario local exacto aprobado y que está prohibido reconstruirlo desde Markdown. D-055 fija como baseline Word canónico bajo custodia local:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx`

SHA-256:

`d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf`

Por tanto, el contenido científico de B03 no requiere reescritura, pero B03 no puede pasar a aprobación autoral mientras falte el candidato DOCX acumulativo derivado del Word exacto B02 V02, con preservación de comentarios/anclajes/formato y QA correspondiente.

### 4. Dictamen

`PASS_WITH_BLOCKING_TECHNICAL_CORRECTION`.

No se autoriza reescribir 4.4. La única corrección autorizada es completar la continuidad DOCX y la trazabilidad asociada. B04/4.5 permanece cerrado.

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B03_SECTION_4_4
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
REVIEW_VERSION = V01
SCIENTIFIC_CONTENT = PASS
CLAIM_EVIDENCE_AUDIT = PASS
DIFFERENTIAL_MD_AUDIT = PASS
BILINGUAL_EQUIVALENCE = PASS
SCOPE_CONTROL = PASS
DOCX_CONTINUITY = FAIL / MISSING_REQUIRED_CANDIDATE
OVERALL = PASS_WITH_BLOCKING_TECHNICAL_CORRECTION
AUTHOR_APPROVAL_GATE = NOT_OPEN
B04 = NOT_AUTHORIZED
```

The Managing AI independently checked Section 4.4 against the governing prompt, D-055, D-056, the frozen experimental ground truth, and primary v0.1/v0.2 artifacts. The scientific content passes: the historical row-level v0.1 split, explicit DAM assignments in v0.2, partition counts, zero DAM and `id_unico` overlap, nominal historical support, separation of exact/near-duplicate diagnostics from DAM grouping, and the non-i.i.d. limitation are represented within their authorized scope.

The exact B03 Markdown candidate has SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78` and expected Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`. Its differential against the exact B02/V011 baseline is restricted to replacing the English and Spanish Section 4.4 placeholders.

The blocking defect is DOCX continuity. D-021 makes the cumulative DOCX necessary even when repository upload is deferred, and D-055 freezes `ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx` (SHA-256 `d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf`) as the exact local Word baseline. B03 therefore requires a cumulative DOCX candidate derived from that exact binary, not reconstructed from Markdown. No scientific rewrite of Section 4.4 is authorized. The author-approval gate remains closed and B04 remains unauthorized.