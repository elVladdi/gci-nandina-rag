# Internal review — Front matter B02 / Final Title V02

## Español

```text
REVIEW_TYPE = INDEPENDENT_SUBSTANTIVE_AND_TECHNICAL_AUDIT
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE_V02

SOURCE_RESPONSE = article/responses/10_FRONT_MATTER_B02_TITLE_RESPONSE_V02.md@9f9c7ae68bdbe2746cfd545faa91f5629dc09a7e
SOURCE_RESPONSE_GIT_BLOB = 11e6a9d78962f620e0b1fcb6af0d5bc1ce938f93

SECTION_ARTIFACT = article/sections/front_matter/Title_B02_V02.md@f9ed61b8fd95569d03dc576cb1450367c482f65e
SECTION_ARTIFACT_GIT_BLOB = da06dc42f00e88758f9e3674de4232f908dbeb78

PROMPT = article/prompts/10_FRONT_MATTER_B02_TITLE_V02.md
PROMPT_GIT_BLOB = 8a86f760bf7353222e5610312b11525ec5793385
AUTHORIZATION = D-171
EDITORIAL_DECISION = D-170

CANONICAL_INPUT_MASTER = ARTICLE_MASTER_V032

VERDICT = PASS
MANDATORY_CORRECTIONS = NONE
AUTHOR_APPROVAL_GATE_READY = YES
```

### 1. Título auditado

```text
TITLE_EN =
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support

TITLE_ES =
Separación del ranking de candidatos, la evidencia documental y la explicación en el apoyo a la decisión de clasificación arancelaria
```

La ejecución materializa exactamente los textos fijados por D-170, sin alternativas ni reformulación.

Editorialmente, el título expone directamente la operación metodológica que estructura el artículo completo: ranking de candidatos, evidencia documental y explicación como funciones separadas dentro de un flujo de apoyo a la decisión para clasificación arancelaria.

No convierte NANDINA/Capítulo 87 en el alcance conceptual del trabajo y no introduce `auditable` como claim principal del título.

### 2. Identidad de archivos entregados

```text
MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_TITLE_B02_V02.md
OBSERVED_SIZE_BYTES = 277760
OBSERVED_SHA256 = ad604203c72d5cdb520c59879ade0cfcb7fd60f05c18f778f9546ec5843e364a
OBSERVED_EXPECTED_GIT_BLOB = b4e25a990e659b87a4f48f35b2dce343bef91b5e
RESPONSE_DECLARED_SHA256 = MATCH
RESPONSE_DECLARED_GIT_BLOB = MATCH

MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_TITLE_B02_V02.docx
OBSERVED_SIZE_BYTES = 110896
OBSERVED_SHA256 = 6690f5e39b3c7a907b075be3a4367ffe858fb6d1dbe4c74632b647463252deeb
RESPONSE_DECLARED_SIZE = MATCH
RESPONSE_DECLARED_SHA256 = MATCH
```

### 3. Auditoría diferencial Markdown

IA Gestora realizó una reconstrucción reversible independiente.

Al restaurar exclusivamente los bloques `## Title` y `## Título` con los placeholders exactos de V032, el archivo reconstruido devuelve:

```text
RECONSTRUCTED_V032_SHA256 = 0fcf9c2676add5128f86efc50788335bc435077bedbd7a8aedbf73f8f1549f64
EXPECTED_V032_SHA256 = 0fcf9c2676add5128f86efc50788335bc435077bedbd7a8aedbf73f8f1549f64

RECONSTRUCTED_V032_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f
EXPECTED_V032_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f

MARKDOWN_OUTSIDE_AUTHORIZED_BLOCKS = EXACT / PASS
```

Por tanto, Abstract/Resumen, Keywords/Palabras clave placeholders, Sections 1–7 y end matter permanecen byte-exactamente equivalentes a V032.

### 4. Auditoría DOCX / OOXML

Baseline:

`ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V02.docx`

Candidato:

`ARTICLE_MASTER_CANDIDATE_TITLE_B02_V02.docx`

Resultado independiente:

```text
BASELINE_SHA256 = 4709944a4653dac813b5ebe68b1b14a13c9b87ceddadd315308e975289335156
CANDIDATE_SHA256 = 6690f5e39b3c7a907b075be3a4367ffe858fb6d1dbe4c74632b647463252deeb

BASELINE_OOXML_PARTS = 14
CANDIDATE_OOXML_PARTS = 14
OOXML_PART_LIST_IDENTICAL = PASS

OOXML_CHANGED_PARTS =
- word/document.xml

ALL_OTHER_OOXML_PARTS_BYTE_IDENTICAL = PASS
COMMENTS_XML_BYTE_IDENTICAL = PASS

BASELINE_COMMENTS = 48
CANDIDATE_COMMENTS = 48

BASELINE_COMMENT_RANGE_START = 48
CANDIDATE_COMMENT_RANGE_START = 48
BASELINE_COMMENT_RANGE_END = 48
CANDIDATE_COMMENT_RANGE_END = 48
BASELINE_COMMENT_REFERENCE = 48
CANDIDATE_COMMENT_REFERENCE = 48

TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
ZIP_OOXML_INTEGRITY = PASS
```

La comparación de párrafos en `word/document.xml` detectó exactamente dos reemplazos:

1. las dos líneas/instrucciones del Title inglés por el título V02 exacto;
2. las dos líneas/instrucciones del Título español por el título V02 exacto.

No se detectó ninguna otra mutación de párrafo.

### 5. Render y QA visual

Baseline y candidato fueron renderizados independientemente con el mismo renderer.

```text
BASELINE_PAGE_COUNT = 71
CANDIDATE_PAGE_COUNT = 71

PIXEL_CHANGED_PAGE_RANGE = 3-38
PIXEL_IDENTICAL_PAGES =
- 1-2
- 39-71

PIXEL_IDENTICAL_PAGE_COUNT = 35
PIXEL_CHANGED_PAGE_COUNT = 36
```

La diferencia visual en páginas 3–38 se debe al reflujo de paginación causado por la mayor altura del nuevo título inglés y su espejo español, no a mutaciones sustantivas adicionales del DOCX.

IA Gestora inspeccionó las páginas modificadas/refluidas y verificó:

```text
TITLE_PAGE_EN = PASS
TITLE_PAGE_ES = PASS
CLIPPING = NONE_DETECTED
OVERLAP = NONE_DETECTED
MISSING_GLYPHS = NONE_DETECTED
BROKEN_LAYOUT = NONE_DETECTED
HEADER_FOOTER_DEFECTS = NONE_DETECTED
FULL_DOCX_PAGE_COUNT = 71
FULL_DOCX_VISUAL_QA = PASS
```

Las 35 páginas pixel-idénticas al baseline mantienen el layout ya auditado.

### 6. Auditoría editorial KBS y científica

El título V02 cumple la directiva derivada del corpus completo de 34 artículos aceptados de *Knowledge-Based Systems*.

```text
TITLE_TO_FULL_ARTICLE_FIDELITY = PASS
SCIENTIFIC_OBJECT_VISIBILITY = PASS
DISTINCTIVE_METHOD_OPERATION_VISIBILITY = PASS
TASK_DOMAIN_PRECISION = PASS
KBS_CORPUS_EDITORIAL_FIT = PASS
CLAIM_CALIBRATION = PASS
TESTBED_SCOPE_HYGIENE = PASS
ANTI_OVERCLAIMING = PASS
NO_INTERNAL_TERMINOLOGY = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
```

La formulación coincide con el artículo completo:

- Abstract: separa ranking, asociación documental y explicación;
- Introduction: define el problema como separación operacional y evaluativa;
- Related Work §2.6: posiciona el trabajo por autoridad no superpuesta entre ranking, evidencia y explicación;
- Architecture §3: implementa esas tres funciones;
- Methods/Results: las evalúa como objetos separados;
- Discussion/Conclusion: identifica esa separación como implicación metodológica principal.

No introduce resultados nuevos, inferencia nueva, literatura nueva ni claims no gobernados.

### 7. Veredicto

```text
PROMPT_COMPLIANCE = PASS
D170_EXACT_MATERIALIZATION = PASS
KBS_CORPUS_EDITORIAL_FIT = PASS
SCIENTIFIC_FIDELITY = PASS
MARKDOWN_DIFFERENTIAL = PASS / EXACT
DOCX_OOXML_DIFFERENTIAL = PASS
COMMENTS_AND_ANCHORS = PASS
FULL_RENDER = PASS
VISUAL_QA = PASS
MANDATORY_CORRECTIONS = NONE
VERDICT = PASS
AUTHOR_APPROVAL_GATE_READY = YES
```

El candidato exacto puede pasar a aprobación explícita del autor.

No se autoriza todavía promoción canónica, Keywords ni end matter.

---

## English

Final Title B02 V02 passes independent Managing-AI editorial, scientific, Markdown, DOCX/OOXML, and visual audit.

The exact D-170 title pair was materialized without alternatives. Reversing only the authorized Title/Título blocks reconstructs canonical V032 exactly by SHA-256 and Git blob. The Word package preserves all 14 OOXML parts, changes only word/document.xml, preserves byte-identical comments.xml, all 48 comment anchors, and zero tracked changes.

The longer V02 title causes expected pagination reflow from pages 3 through 38, while pages 1-2 and 39-71 remain pixel-identical to the approved baseline. All changed/reflowed pages pass visual QA.

The title now matches the editorial pattern inferred from the full 34-article accepted KBS corpus: it exposes the concrete methodological operation that structures the entire paper—separating candidate ranking, documentary evidence, and explanation—while retaining tariff-classification decision support as the task context and avoiding unsupported headline claims.

No mandatory corrections remain. The exact candidate is ready only for explicit author approval. Canonical promotion, Keywords, and end matter remain unauthorized.
