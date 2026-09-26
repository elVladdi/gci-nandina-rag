# Revisión diferencial — Experimental Design B04 / narrow precision correction — V01

## Español

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01
ROLE = IA_GESTORA
DATE = 2026-09-26
GOVERNING_DECISION = D-063
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_V01_NARROW_PRECISION_CORRECTION.md@6432e884a632e1884926ee35ffaae3c2b882fb87
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_RESPONSE_V01.md@bc93692cd78e59778392b218d418c767a015466f
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
BASELINE_MASTER_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
BASELINE_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx
CANDIDATE_MASTER_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md
CANDIDATE_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx
REVIEW_SCOPE = DIFFERENTIAL_ONLY / B04-C01 + B04-C02
EXPERIMENTAL_REVIEW = NOT_REQUIRED
RESULT = PASS
AUTHOR_APPROVAL_GATE = MAY_REOPEN
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

### 1. Identidad de artefactos

La IA Gestora verificó directamente los binarios/bytes entregados por el autor:

```text
BASELINE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad / PASS
BASELINE_MD_GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676 / PASS
BASELINE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611 / PASS
CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43 / PASS
CANDIDATE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62 / PASS
CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f / PASS
```

Los hashes del candidato coinciden exactamente con los reportados por la IA de Redacción.

### 2. Auditoría diferencial del Markdown

Se verificaron las cuatro sustituciones literales autorizadas por D-063:

- B04-C01 EN: 1 reemplazo;
- B04-C01 ES: 1 reemplazo;
- B04-C02 EN: 1 reemplazo;
- B04-C02 ES: 1 reemplazo.

En el candidato V02, cada texto nuevo aparece exactamente una vez y cada texto fuente V01 aparece cero veces. Al invertir únicamente esas cuatro sustituciones sobre los bytes de V02, el archivo resultante es byte-idéntico al baseline B04 V01.

```text
MASTER_MD_DIFFERENTIAL = PASS
UNAUTHORIZED_MD_MUTATION = NONE
```

El section artifact V02 versionado en GitHub contiene exactamente las dos precisiones aprobadas en ambos idiomas y no reabre el resto de Section 4.5.

### 3. Auditoría diferencial del DOCX

Se inspeccionó directamente el paquete OOXML de B04 V01 y B04 V02.

```text
ZIP_OOXML_INTEGRITY = PASS
PACKAGE_ENTRY_SET = IDENTICAL / 14 ENTRIES
XML_AND_RELS_PARSE = 14/14 PASS
CHANGED_PACKAGE_ENTRIES = [word/document.xml]
UNCHANGED_PACKAGE_ENTRIES = ALL_OTHERS / BYTE_IDENTICAL
TRACKED_CHANGES = 0
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / PRESERVED
```

Al invertir solo B04-C01 y B04-C02 EN/ES dentro de `word/document.xml`, el XML resultante reproduce exactamente el `word/document.xml` del baseline V01. Por tanto, no existe mutación de contenido DOCX fuera de las cuatro sustituciones autorizadas.

### 4. Render y presentación

El DOCX V02 fue renderizado nuevamente por la IA Gestora.

```text
BASELINE_RENDER_PAGE_COUNT = 44
CANDIDATE_RENDER_PAGE_COUNT = 45
PAGE_COUNT_CHANGE = AUTHORIZED_TEXT_REFLOW
VISUAL_DIFFERENTIAL_QA = PASS
```

La página adicional deriva del reflujo acumulativo producido por la mayor longitud de las sustituciones autorizadas; no corresponde a contenido nuevo. Se verificaron las páginas afectadas por las correcciones y el reflujo, incluidos los bloques EN de Section 4.5 y ES de Section 4.5, así como el cierre del documento. No se observaron clipping, solapamientos, encabezados/pies desplazados ni pérdida de contenido.

### 5. Contenido científico y equivalencia bilingüe

Las correcciones ejecutan exactamente el alcance de D-063:

- B04-C01 evita equiparar `history_depth=2950` con una afirmación más fuerte sobre materialización de score para todos los registros;
- B04-C02 formula el match NANDINA-8 de forma condicional y evita anticipar en Methods el outcome observado de cobertura exacta.

La versión inglesa y el espejo español conservan equivalencia semántica. No se añadieron métricas de Results, inferencias, claims de corrección jurídica, generalización, `FINAL_GAP` ni novelty.

```text
SCIENTIFIC_SCOPE_4_5 = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
RESULTS_LEAKAGE = NONE
NEW_SCIENTIFIC_CLAIMS = NONE
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

### 6. Dictamen

```text
B04_V02_DIFFERENTIAL_AUDIT = PASS
CORRECTION_REQUIRED = NO
AUTHOR_APPROVAL_GATE = REOPEN_ELIGIBLE
CANONICAL_MASTER_REMAINS = ARTICLE_MASTER_V012 UNTIL EXPRESS AUTHOR APPROVAL
B05 = NOT_AUTHORIZED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

No corresponde una nueva corrección ni una revisión experimental. El siguiente gate es exclusivamente la aprobación expresa del autor de B04 V02. Solo después de esa aprobación la IA Gestora podrá integrar/promover el candidato y evaluar la apertura de B05/Section 4.6.

---

## English

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01
ROLE = MANAGING_AI
DATE = 2026-09-26
GOVERNING_DECISION = D-063
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_V01_NARROW_PRECISION_CORRECTION.md@6432e884a632e1884926ee35ffaae3c2b882fb87
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_RESPONSE_V01.md@bc93692cd78e59778392b218d418c767a015466f
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
REVIEW_SCOPE = DIFFERENTIAL_ONLY / B04-C01 + B04-C02
EXPERIMENTAL_REVIEW = NOT_REQUIRED
RESULT = PASS
AUTHOR_APPROVAL_GATE = MAY_REOPEN
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

The Managing AI independently verified the exact baseline and candidate hashes. The V02 Markdown differs from V01 only through the four authorized EN/ES literal replacements; reversing those replacements restores the V01 bytes exactly. The V02 DOCX preserves the same 14-package-entry set, all package members except `word/document.xml` are byte-identical, all XML/relationship parts parse successfully, all 40 inherited comment anchors and the unchanged `comments.xml` are preserved, and tracked changes remain zero. Reversing the four authorized replacements in `word/document.xml` reproduces the V01 XML exactly.

The candidate renders to 45 pages versus 44 for V01. This is a layout reflow consequence of the longer authorized wording, not additional scientific content. Visual differential inspection of the corrected Section 4.5 blocks, downstream reflow, and document ending found no clipping, overlap, missing content, or header/footer defects.

B04-C01 and B04-C02 now implement the intended precision boundaries without adding Results, inference, legal-correctness claims, empirical-generalization claims, `FINAL_GAP`, or novelty. English and Spanish remain semantically equivalent. No experimental-review trigger is present.

```text
B04_V02_DIFFERENTIAL_AUDIT = PASS
CORRECTION_REQUIRED = NO
AUTHOR_APPROVAL_GATE = REOPEN_ELIGIBLE
CANONICAL_MASTER_REMAINS = ARTICLE_MASTER_V012 UNTIL EXPRESS AUTHOR APPROVAL
B05 = NOT_AUTHORIZED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
