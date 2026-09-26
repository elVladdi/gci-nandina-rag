# Experimental Design B04 V01 — narrow precision correction

## Español

### 1. Identidad

```text
BLOCK = EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION
GOVERNING_DECISION = article/governance/D063_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION.md@ce42b76a8c8da69924cd205dbcb132e479d0d6ea
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md@09ed0ec3a42549522942f5252f0b78713bb94524
BASELINE_SECTION = article/sections/experimental_design/Experimental_Design_B04_V01.md@ade9d022663458d7bbe5aee939e1d7899365a7c8
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
BASELINE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
BASELINE_MD_GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx
BASELINE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
SCIENTIFIC_SCOPE_4_5 = VERIFIED / PASS / DO_NOT_REWRITE
AUTHORIZED_CORRECTION_COUNT = 2 ITEMS / 4 EN-ES REPLACEMENTS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Ejecuta exclusivamente esta corrección. No avances.

### 2. Rol

Actúa solo como **IA de Redacción**. Este es un microgate correctivo diferencial, no un nuevo bloque de redacción científica.

No reabras experimentos, claims, bibliografía, arquitectura, B02/B03, 4.6–4.8 ni Results. No modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, decisiones, reviews, SRC-03, Plan Maestro, `main` ni artefactos experimentales.

### 3. Onboarding mínimo obligatorio

Lee antes de editar:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
5. `article/governance/D063_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION.md`;
6. `article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md`;
7. este prompt completo.

Verifica los dos baselines entregados por el autor antes de editar. Deben coincidir exactamente con los SHA-256 indicados arriba. Si falta uno o no coincide, detente con:

`B04_NARROW_CORRECTION_BASELINE_MISMATCH`

No reconstruyas el DOCX desde Markdown y no regreses al DOCX B03.

### 4. Únicas modificaciones autorizadas

#### B04-C01 — precisión de profundidad histórica

Reemplaza exactamente en inglés:

```text
For each evaluation query, the implementation scored the historical records, considered the full H100 depth of 2,950 records, and retained up to 100 unique code candidates.
```

por:

```text
For each evaluation query, the implementation scored the historical matches using the 2,950-record H100 bank, set the historical ranking depth to 2,950, and retained up to 100 unique code candidates.
```

Reemplaza exactamente en español:

```text
Para cada consulta de evaluación, la implementación puntuó los registros históricos, consideró la profundidad completa de H100 de 2.950 registros y retuvo hasta 100 candidatos de código únicos.
```

por:

```text
Para cada consulta de evaluación, la implementación puntuó las coincidencias históricas usando el banco H100 de 2.950 registros, fijó la profundidad del ranking histórico en 2.950 y retuvo hasta 100 candidatos de código únicos.
```

#### B04-C02 — regla de match documental sin anticipar outcome

Reemplaza exactamente en inglés:

```text
The matched eight-digit record supplied exact candidate-level evidence, while section, chapter, heading, and six-digit parent information remained explicit hierarchical context.
```

por:

```text
When an exact eight-digit match was available, that record supplied candidate-level evidence, while section, chapter, heading, and six-digit parent information remained explicit hierarchical context.
```

Reemplaza exactamente en español:

```text
El registro coincidente de ocho dígitos aportó la evidencia exacta a nivel de candidato, mientras que la información de sección, capítulo, partida y subpartida de seis dígitos permaneció como contexto jerárquico explícito.
```

por:

```text
Cuando existía una coincidencia exacta de ocho dígitos, ese registro aportaba evidencia a nivel de candidato, mientras que la información de sección, capítulo, partida y subpartida de seis dígitos permanecía como contexto jerárquico explícito.
```

### 5. Contenido congelado

Todo lo demás debe permanecer sin cambios de contenido.

En particular:

- no reformules ninguna otra oración de 4.5;
- no cambies Sections 1–4.4;
- no cambies placeholders/instrucciones de 4.6–4.8;
- no cambies Results, Discussion, Conclusion ni end matter;
- no agregues o elimines citas/referencias;
- no agregues métricas, resultados, inferencias, claims de novelty o FINAL_GAP;
- no cambies parámetros experimentales;
- no cambies las 40 anotaciones de citas heredadas.

Si detectas que uno de los textos fuente exactos no aparece una vez y solo una vez en cada artefacto pertinente, detente con:

`B04_NARROW_CORRECTION_SOURCE_TEXT_MISMATCH`

Si aparece cualquier mutación no autorizada, detente con:

`B04_NARROW_CORRECTION_OUT_OF_SCOPE_MUTATION`

### 6. Entregables

#### A. Section artifact corregido

Crea y versiona:

`article/sections/experimental_design/Experimental_Design_B04_V02.md`

Debe ser idéntico en contenido científico a B04 V01 excepto por B04-C01 y B04-C02 EN/ES. Actualiza únicamente el encabezado de trazabilidad necesario para identificar V02 y este microgate.

#### B. Master Markdown candidato V02

Partiendo exclusivamente de `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md`, genera:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md`

Solo se autorizan las cuatro sustituciones literales anteriores. Entrega el archivo exacto al autor y reporta SHA-256 y Git blob calculado desde sus bytes.

#### C. DOCX acumulativo candidato V02

Edita directamente el B04 V01 exacto y genera:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx`

No lo reconstruyas.

Checks obligatorios:

```text
BASELINE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611 / PASS
COMMENTS = 40 / PRESERVE
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
DOCX_RECONSTRUCTED_FROM_MD = NO
ZIP_OOXML_INTEGRITY = PASS
XML_RELS_PARSE = PASS
RENDER_ALL_PAGES = REQUIRED
VISUAL_INSPECTION_ALL_PAGES = REQUIRED
```

El DOCX debe entregarse efectivamente al autor como archivo descargable conforme a D-027/D-035.

#### D. Response versionada

Crea:

`article/responses/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_RESPONSE_V01.md`

Debe ser bilingüe y registrar:

- hashes baseline verificados;
- conteo exacto de reemplazos B04-C01/B04-C02 por idioma y artefacto;
- SHA-256/Git blob del MD V02;
- SHA-256 del DOCX V02;
- QA OOXML/comentarios/tracked changes/render;
- confirmación de que no hubo cambios fuera de los dos ítems autorizados.

### 7. Gate de salida

Finaliza con:

```text
EXECUTION_COMPLETED_PENDING_GESTORA_DIFFERENTIAL_AUDIT
AUTHOR_APPROVAL_GATE = SUSPENDED
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

En chat responde únicamente con la ruta@commit de la response y los enlaces/adjuntos exactos de los candidatos MD y DOCX V02. No repitas el informe sustantivo.

---

## English

### 1. Identity

```text
BLOCK = EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION
GOVERNING_DECISION = article/governance/D063_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION.md@ce42b76a8c8da69924cd205dbcb132e479d0d6ea
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_INTERNAL_REVIEW_V01.md@09ed0ec3a42549522942f5252f0b78713bb94524
BASELINE_SECTION = article/sections/experimental_design/Experimental_Design_B04_V01.md@ade9d022663458d7bbe5aee939e1d7899365a7c8
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
BASELINE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
BASELINE_MD_GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx
BASELINE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
SCIENTIFIC_SCOPE_4_5 = VERIFIED / PASS / DO_NOT_REWRITE
AUTHORIZED_CORRECTION_COUNT = 2 ITEMS / 4 EN-ES REPLACEMENTS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Execute only this differential correction. Do not advance.

### 2. Role

Act only as the **Drafting AI**. This is a narrow corrective microgate, not a new scientific drafting block. Do not reopen experiments, claims, bibliography, architecture, B02/B03, Sections 4.6–4.8, or Results. Do not modify governance/status files, SRC-03, the experimental Master Plan, `main`, or experimental artifacts.

### 3. Mandatory onboarding

Read the current `START_HERE`, `ARTICLE_STATUS`, `ARTICLE_WRITING_PLAN`, MWDP v1.0, D-063, the governing B04 internal review, and this prompt. Verify both author-supplied baselines before editing. If either file is absent or its SHA-256 differs, stop with `B04_NARROW_CORRECTION_BASELINE_MISMATCH`. Do not reconstruct Word from Markdown and do not return to the B03 DOCX.

### 4. Authorized edits

Apply exactly the four EN/ES literal replacements frozen in the Spanish section above: B04-C01 (historical-depth precision) and B04-C02 (conditional exact documentary match). No paraphrase or additional cleanup is authorized.

### 5. Frozen content

All other scientific and cumulative-master content is frozen. No other Section-4.5 sentence, Sections 1–4.4, Sections 4.6+, Results, references, metrics, claims, parameters, or inherited citation comments may change. Any source-text mismatch or out-of-scope mutation is a blocking condition.

### 6. Deliverables

Produce:

1. `article/sections/experimental_design/Experimental_Design_B04_V02.md` — versioned in GitHub;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md` — exact cumulative Markdown candidate handed to the author;
3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx` — edited directly from the exact B04 V01 DOCX and handed to the author;
4. `article/responses/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_RESPONSE_V01.md` — bilingual versioned response.

Verify and record exact replacement counts, hashes, Git blob for Markdown, OOXML integrity, all 40 comment anchors, zero tracked changes, full rendering, all-page visual inspection, and no out-of-scope content mutations.

### 7. Exit gate

```text
EXECUTION_COMPLETED_PENDING_GESTORA_DIFFERENTIAL_AUDIT
AUTHOR_APPROVAL_GATE = SUSPENDED
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

In chat return only the versioned-response path@commit and downloadable exact MD/DOCX V02 artifacts.