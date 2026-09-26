# Experimental Design B02 V02 — Independent differential review of narrow coherence correction

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B02_V02_NARROW_COHERENCE_CORRECTION_INTERNAL_REVIEW_V01
DATE = 2026-09-26
ROLE = IA_GESTORA / LEAD_SCIENTIFIC_EDITOR
GOVERNING_DECISION = D-053
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B02_V01_NARROW_COHERENCE_CORRECTION.md@d6bbe9de0d08547d778afdfd7cc828b68690da41
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B02_NARROW_COHERENCE_CORRECTION_RESPONSE_V01.md@2ce55f097420ddc90f3a0583d1168483c50b022a
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.md
BASELINE_MD_SHA256 = 22f5a6e1168e08ef6281488024a4ac5e4f6742ee90a96d8f31e5453c592bf592
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.docx
BASELINE_DOCX_SHA256 = 40d492911b2163a4c6a837f292f3056aa49bcbf69ce9dc3caf50aa80f021ae1e
OUTPUT_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.md
OUTPUT_MD_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
OUTPUT_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx
OUTPUT_DOCX_SHA256 = d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf
AUTHORIZED_LOGICAL_REPLACEMENTS_MD = 5 / VERIFIED
AUTHORIZED_TEXT_OCCURRENCES_DOCX = 6 / VERIFIED
SECTION_4_3_SCIENTIFIC_CONTENT = VERIFIED / PASS / PRESERVED
AUTHORIZED_SCOPE_ONLY = PASS
DOCX_OOXML_INTEGRITY = PASS
DOCX_RENDER_QA = PASS
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OVERALL = PASS
AUTHOR_APPROVAL_GATE = OPEN
CANONICAL_MASTER = ARTICLE_MASTER_V010 / UNCHANGED
B02_V02 = VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Alcance de la auditoría

La IA Gestora realizó una auditoría diferencial independiente entre los artefactos B02 V01 y B02 V02. El objetivo fue comprobar exclusivamente que la corrección ordenada por D-053 se ejecutara sin reabrir ni modificar el contenido científico de Section 4.3 y sin introducir cambios fuera de alcance.

Los hashes de los cuatro binarios/textos involucrados fueron calculados independientemente y coinciden exactamente con los valores gobernantes y reportados por la IA de Redacción.

## 2. Markdown V01 → V02 — PASS

La comparación textual independiente identifica exactamente cinco cambios lógicos autorizados:

1. `KBS_ARTICLE_WORKING_STRUCTURE_V01` → `KBS_ARTICLE_WORKING_STRUCTURE_V02`;
2. reemplazo C02a en Introduction — Part I, separando `Peruvian administrative context` de `Andean documentary resource`;
3. reemplazo C02c en la nota interna de Section 3 — Part I;
4. reemplazo C02b en Introduction — Part II, separando `contexto administrativo peruano` de `recurso documental andino`;
5. reemplazo C02c en la nota interna de Section 3 — Part II.

No se identificó ningún cambio científico adicional.

En la nota interna inglesa de Section 3, el baseline Markdown dividía `the Peruvian corpus` mediante un salto de línea físico (`the Peruvian` / `corpus`). La sustitución autorizada quedó en una sola línea en V02. Esta normalización de hard-wrap está contenida íntegramente dentro del mismo segmento C02c autorizado, no cambia su semántica ni afecta prosa científica; no se considera una mutación fuera de alcance.

Section 4.3, Sections 4.1–4.2.3, Related Work, el resto de Introduction/Architecture, los placeholders 4.4–4.8 y Sections 5–7 permanecen preservados fuera de los cinco reemplazos autorizados.

## 3. DOCX V01 → V02 — PASS

La comparación OOXML independiente confirma:

```text
OOXML_PART_COUNT_V01 = 14
OOXML_PART_COUNT_V02 = 14
OOXML_PART_SET = IDENTICAL
CHANGED_PARTS = word/document.xml / word/footer1.xml ONLY
ALL_OTHER_PARTS = BYTE_IDENTICAL
COMMENTS_XML = BYTE_IDENTICAL
COMMENTS = 40
COMMENT_IDS = 0..39
TRACKED_CHANGES = 0
```

Al comparar los párrafos de `word/document.xml`, aparecen exactamente cinco modificaciones textuales, correspondientes uno a uno a C01, C02a, C02b y los dos C02c. En `word/footer1.xml` aparece únicamente la segunda ocurrencia de C01. Por tanto:

```text
AUTHORIZED_TEXT_OCCURRENCES_DOCX = 6 / EXACT
UNEXPECTED_DOCX_TEXT_MUTATIONS = 0
```

La estructura XML y los atributos de las dos partes modificadas permanecen iguales al ignorar únicamente los nodos de texto; la modificación es textual y no estructural.

## 4. Preservación de B02 / Section 4.3 — PASS

La Section 4.3 inglesa y su espejo español permanecen textualmente sin cambios respecto de B02 V01. Se conserva el contenido científico previamente verificado:

- recurso jerárquico NANDINA derivado de Decision 885;
- asociación documental por lookup exacto del código NANDINA-8 de cada candidato ya fijado;
- ausencia de query-based normative retrieval en la ruta primaria;
- ausencia de score fusion, reranking, inserción o sustitución de candidatos;
- contexto parental sin promoción automática a evidencia exacta de ocho dígitos;
- Top-3 inmutable downstream;
- divulgación de la frontera temporal/versionado frente a Decision 906 sin convertirla en un claim de invalidez general de Chapter 87.

No se añadieron resultados, métricas, referencias, novelty claims ni FINAL_GAP.

## 5. Render y control visual — PASS

El DOCX V02 fue renderizado independientemente por la IA Gestora en 41 páginas. Las 41 páginas fueron inspeccionadas visualmente, incluida la portada, ambas Introduction, las notas internas de Section 3, Section 4.3 en inglés y español, los placeholders posteriores y el cierre del documento.

No se observaron:

- clipping o texto fuera de página;
- solapamientos;
- glifos faltantes;
- headings desplazados o duplicados;
- páginas corruptas;
- alteraciones visibles de maquetación atribuibles a la corrección.

El footer muestra consistentemente `KBS_ARTICLE_WORKING_STRUCTURE_V02`.

## 6. Dictamen

```text
B02_V02_NARROW_COHERENCE_CORRECTION = PASS
B02_SECTION_4_3_SCIENTIFIC_CONTENT = VERIFIED / PASS / PRESERVED
B02_PUBLICATION_FIT = PASS
B02_DOCX_QA = PASS
B02_V02 = VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
ARTICLE_MASTER_V010 = REMAINS_CANONICAL
ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02 = NOT_YET_CANONICAL
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

D-053 queda técnicamente satisfecho. Esta auditoría abre el gate de aprobación autoral, pero no concede aprobación, cierre, congelamiento ni integración. El autor debe decidir expresamente sobre `ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02` antes de cualquier promoción canónica o apertura de Section 4.4.