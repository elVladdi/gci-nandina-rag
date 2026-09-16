# Methods B01 — Revisión interna V02 / Internal Review V02

## Español

### 1. Objeto y trazabilidad

Se auditó exclusivamente la entrega `Methods B01 — Design, scope, and units` V02 del commit `c9023096344a8949f3ce5f9b49c8cc29379afe4a`, contra:

- `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS_REVISION_V02.md`;
- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V01.md`;
- `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V01.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`);
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/ARTICLE_STATUS.md`;
- el `SRC-03` vivo.

El HEAD de `article/main-manuscript` al iniciar esta auditoría era exactamente `c9023096344a8949f3ce5f9b49c8cc29379afe4a`, descendiente directo de `ae4cf9b7876759234bfbeff4560dcdb4a2644de2`. La comparación entre ambos commits confirma un único commit y únicamente los cuatro artefactos V02 autorizados:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V02.md`;
2. `article/sections/methods/Methods_B01_V02.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.docx`.

No se sobrescribieron los artefactos V01, no se creó `ARTICLE_MASTER_V001.*` y no se abrió B02.

### 2. Auditoría de las correcciones obligatorias

#### B01-M01 — Lenguaje de gobernanza interna

**PASS.** Se eliminaron `governing study artifacts` / `artefactos gobernantes del estudio`. La delimitación se expresa ahora en lenguaje científico autosuficiente orientado al lector.

#### B01-M02 — Definición de DAM

**PASS.** La primera aparición inglesa usa `Declaración Aduanera de Mercancías (DAM; customs declaration)` y el espejo español conserva `Declaración Aduanera de Mercancías (DAM)`.

#### B01-M03 — Configurabilidad fuera del entorno evaluado

**PASS.** Se eliminó el claim positivo de configurabilidad. La V02 conserva únicamente la frontera válida: la evaluación no establece generalización empírica fuera del alcance de Capítulo 87. No se introdujo C15.

#### B01-M05 — Posicionamiento solicitado por el autor

**PASS.** La V02 invierte correctamente el orden conceptual que motivó el rechazo de V01:

```text
arquitectura auditable general
→ separación ranking histórico / evidencia normativa / explicación LLM
→ Top-3 fijo y ausencia de feedback generativo
→ evaluación mediante testbed regulatorio
→ NANDINA Capítulo 87
```

El primer párrafo presenta el objeto científico general y sus restricciones funcionales. NANDINA Capítulo 87 aparece recién en el segundo párrafo como `controlled regulatory testbed`. Por tanto, la primera lectura ya no presenta el trabajo como un experimento NANDINA/Clase 87 antes de comunicar la oferta científica general.

No se añadió novelty final, superioridad, ausencia universal de prior art ni generalización empírica.

### 3. Auditoría claim–evidence y alcance

Los claims utilizados son compatibles con el conjunto autorizado para B01:

```text
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
```

- C01: la recuperación histórica genera y ordena candidatos — **PASS**.
- C02: la recuperación normativa aporta evidencia documental sin reemplazar/reordenar el ranking — **PASS**.
- C03: el LLM local explica el Top-3 previamente recuperado y no clasifica desde cero — **PASS**.
- C07: DAM se usa como unidad de agrupamiento cuando la dependencia es metodológicamente relevante — **PASS**.

La formulación adicional de no insertar, eliminar, sustituir, reordenar ni retroalimentar la selección conserva el contrato funcional congelado de `MWDP-F01` y no introduce un resultado experimental nuevo.

Controles de alcance:

```text
NO_RESULTS_OR_METRICS = PASS
NO_GROUP3_RESULTS = PASS
NO_EXP11B_USE = PASS
NO_CAUSAL_LANGUAGE = PASS
NO_FINAL_GAP = PASS
NO_NOVELTY_CLAIM = PASS
NO_EXTERNAL_LITERATURE = PASS
CITATION_COMMENT_COVERAGE = 0/0 / PASS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

El `SRC-03` vivo permanece en `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`; no existe un cambio experimental que active revisión por IA Experimental para este bloque.

### 4. Equivalencia bilingüe

**PASS.** Se verificó correspondencia semántica EN–ES en:

- objeto científico y orden de framing;
- separación de funciones;
- invariancia del Top-3 frente al LLM;
- naturaleza no vinculante del sistema;
- posición de la revisión experta;
- alcance empírico del testbed;
- unidades de observación/análisis, agrupamiento y consulta;
- objetos de salida y límite de generalización.

No se detectó aumento o reducción material de fuerza epistémica entre ambos idiomas.

### 5. Verificación independiente del master candidato y Word

`ARTICLE_MASTER_CANDIDATE_V02.md` reproduce exactamente el contenido científico de `Methods_B01_V02.md`, con la jerarquía acumulativa `3. Methods → 3.1 Design, scope, and units` y su espejo español.

El `.docx` fue recuperado del blob GitHub `88f92f47f2a3795cf7bc1648e08bc238ca3b8cc0` y auditado independientemente:

```text
DOCX_SIZE_BYTES = 3786
DOCX_SHA256 = 248eaf3f81347eabb9f6d8a86cfbd4127d68596f2508e15e858d07352009bdba
DOCX_OOXML_VALID = PASS
DOCX_PAGE_COUNT = 2
DOCX_MD_TEXT_EQUIVALENCE = PASS
DOCX_NONEMPTY_PARAGRAPHS = 13/13 exact match
DOCX_COMMENTS = NONE
DOCX_TRACKED_CHANGES = NONE
DOCX_FIELDS = NONE
DOCX_CUSTOMXML = NONE
DOCX_VISUAL_QA = PASS
```

La página 1 contiene exclusivamente `Part I — English manuscript master`; la página 2 contiene `Part II — Spanish semantic-control mirror`. No se observaron recortes, solapamientos, texto ilegible ni anomalías de layout. La ausencia de comentarios es correcta porque el bloque contiene cero citas.

El conteo independiente del texto principal inglés confirma:

```text
ENGLISH_MAIN_TEXT_WORD_COUNT = 253
```

### 6. Dictamen interno

```text
METHODS_B01_V02_INTERNAL_REVIEW = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
REQUIRED_CORRECTIONS = 0
B01_M01 = CLOSED
B01_M02 = CLOSED
B01_M03 = CLOSED
B01_M05 = CLOSED
POSITIONING_ORDER = GENERAL_ARCHITECTURE_FIRST / NANDINA_CH87_AS_TESTBED_SECOND
EN_ES_SEMANTIC_EQUIVALENCE = PASS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
METHODS_B01 = READY_FOR_AUTHOR_REVIEW
AUTHOR_APPROVAL_METHODS_B01_V02 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

Este `PASS` interno **no equivale a aprobación, freeze ni integración**. Conforme a `MWDP-B07`, la decisión siguiente corresponde exclusivamente al autor.

---

## English

### 1. Scope and traceability

This review covers only `Methods B01 — Design, scope, and units` V02 at commit `c9023096344a8949f3ce5f9b49c8cc29379afe4a`, checked against the V02 revision prompt, both V01 reviews, `MWDP_V1.0`, the claim–evidence matrix, current editorial status, and living `SRC-03`.

The delivery is a single commit directly descended from `ae4cf9b7876759234bfbeff4560dcdb4a2644de2` and adds only the four authorized V02 artifacts. V01 was preserved, no canonical `ARTICLE_MASTER_V001.*` was created, and B02 was not opened.

### 2. Mandatory corrections

- **B01-M01 — PASS:** internal governance wording was removed.
- **B01-M02 — PASS:** DAM is correctly defined at first English occurrence.
- **B01-M03 — PASS:** the positive configurability claim was removed and no C15 claim was added.
- **B01-M05 — PASS:** the broader auditable decision-support architecture is foregrounded before NANDINA Chapter 87 is introduced as the controlled regulatory testbed. No final novelty, superiority, prior-art-absence, or empirical-generalization claim was introduced.

### 3. Claim and scope audit

`C01`, `C02`, `C03`, and `C07` are used within their authorized Methods scope. No conditional/prohibited claim, result, Group-3 inference, EXP-11B result, causal language, external literature, final gap, or novelty claim appears. Citation-comment coverage is correctly `0/0`. `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

### 4. Bilingual and Word QA

EN–ES semantic equivalence is `PASS`. The Markdown master and standalone B01 block are scientifically identical. The DOCX blob `88f92f47f2a3795cf7bc1648e08bc238ca3b8cc0` is a valid two-page OOXML document; its 13 non-empty paragraphs exactly reproduce the Markdown master, it contains no comments, fields, tracked changes, or custom XML, and visual rendering shows no clipping, overlap, or layout defect. Independent English main-text count is 253 words.

### 5. Verdict

```text
METHODS_B01_V02_INTERNAL_REVIEW = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
REQUIRED_CORRECTIONS = 0
B01_M01 = CLOSED
B01_M02 = CLOSED
B01_M03 = CLOSED
B01_M05 = CLOSED
POSITIONING_ORDER = GENERAL_ARCHITECTURE_FIRST / NANDINA_CH87_AS_TESTBED_SECOND
EN_ES_SEMANTIC_EQUIVALENCE = PASS
EXPERIMENTAL_REVIEW = NOT_REQUIRED
METHODS_B01 = READY_FOR_AUTHOR_REVIEW
AUTHOR_APPROVAL_METHODS_B01_V02 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

Internal `PASS` does not authorize approval, freeze, canonical master integration, or B02. The next decision belongs to the author under `MWDP-B07`.
