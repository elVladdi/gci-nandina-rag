# Experimental Design B01 correction — Operational response V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_CORRECTION
SOURCE_MASTER_CANDIDATE_MD_SHA256 = 6e443353c362410ffe70c880b49647a12b1a88d3ec72a12675cce5e086435754 / PASS
SOURCE_CANDIDATE_DOCX_SHA256 = 4089ca75267ed05d1406b9bf2c1f895300f4da77ccb3e0559b2ef43ad49f3e5c / PASS
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
STALE_SPANISH_SECTION4_PLACEHOLDER_REMOVED = PASS
B01_SCIENTIFIC_PROSE_CHANGED = NO
SECTION_MD_CHANGED = NO
INTRODUCTION_MODIFIED = NO
RELATED_WORK_MODIFIED = NO
ARCHITECTURE_3_1_TO_3_7_MODIFIED = NO
SECTION_4_3_AND_LATER_MODIFIED = NO
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 41
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md
MASTER_CANDIDATE_MD_SHA256 = bdcbbd474d467e978777e031ae568b3fb5d089c32606289f0818ea852a4d4c44
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx
CANDIDATE_DOCX_SHA256 = 53c23c6f951aa8d76ea647fe97105cddd43883c3b3b93e6850ea8eaf861053b2
DIRECT_LARGE_MASTER_GITHUB_TRANSFER = NOT_ATTEMPTED / D035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
EXPERIMENTAL_DESIGN_B02 = NOT_STARTED
RESULTS = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Verificación diferencial

La corrección se ejecutó sobre los dos artefactos V01 exactos entregados por el autor. En el Markdown acumulativo, la única eliminación textual es el placeholder español residual situado entre la nota introductoria de `4. Diseño experimental` y `4.1. Entorno de evaluación`; el salto de línea asociado desaparece con ese párrafo. Ninguna otra línea cambia.

En el DOCX, únicamente se eliminó el párrafo OOXML de estilo `Placeholder` que contenía ese texto. Todos los miembros del paquete ZIP/OOXML salvo `word/document.xml` permanecen byte a byte idénticos al V01. Dentro de `document.xml`, la comparación de nodos de texto V01→V02 muestra una sola eliminación: `[Section text to be drafted in a later approved version.]`. No se modificó ninguna prosa científica de B01 ni contenido de 4.3 o posteriores.

La integridad OOXML pasó `testzip`; se conservaron 40 comentarios, 40 `commentRangeStart`, 40 `commentRangeEnd` y 40 `commentReference`; `word/comments.xml` conserva el SHA-256 gobernante y no existen `w:ins`, `w:del`, `w:moveFrom` ni `w:moveTo`.

El DOCX V02 se renderizó completo en 41 páginas. Las páginas 1–35 y 41 son pixel/byte-identical al render V01 ya aprobado; las páginas 36–40, únicas afectadas por el reflujo derivado de eliminar el párrafo, fueron inspeccionadas visualmente y no presentan clipping, overlap, truncamiento, pérdida de glifos ni alteración de encabezados o pies. Por tanto, el QA visual completo queda `PASS`.

No se modificó `article/sections/experimental_design/Experimental_Design_B01_V01.md`, no se creó una V02 de sección, no se promovió un master canónico y no se abrió ningún bloque posterior.

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_CORRECTION
SOURCE_MASTER_CANDIDATE_MD_SHA256 = 6e443353c362410ffe70c880b49647a12b1a88d3ec72a12675cce5e086435754 / PASS
SOURCE_CANDIDATE_DOCX_SHA256 = 4089ca75267ed05d1406b9bf2c1f895300f4da77ccb3e0559b2ef43ad49f3e5c / PASS
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
STALE_SPANISH_SECTION4_PLACEHOLDER_REMOVED = PASS
B01_SCIENTIFIC_PROSE_CHANGED = NO
SECTION_MD_CHANGED = NO
INTRODUCTION_MODIFIED = NO
RELATED_WORK_MODIFIED = NO
ARCHITECTURE_3_1_TO_3_7_MODIFIED = NO
SECTION_4_3_AND_LATER_MODIFIED = NO
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 41
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md
MASTER_CANDIDATE_MD_SHA256 = bdcbbd474d467e978777e031ae568b3fb5d089c32606289f0818ea852a4d4c44
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx
CANDIDATE_DOCX_SHA256 = 53c23c6f951aa8d76ea647fe97105cddd43883c3b3b93e6850ea8eaf861053b2
DIRECT_LARGE_MASTER_GITHUB_TRANSFER = NOT_ATTEMPTED / D035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
EXPERIMENTAL_DESIGN_B02 = NOT_STARTED
RESULTS = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Differential verification

The correction was applied to the exact V01 cumulative Markdown and DOCX supplied by the author. In the cumulative Markdown, the only textual deletion is the stale Spanish placeholder between the introductory note under `4. Diseño experimental` and `4.1. Entorno de evaluación`; the paragraph-associated blank line disappears with that placeholder. No other line changes.

In the DOCX, only the `Placeholder`-style OOXML paragraph containing that text was removed. Every ZIP/OOXML member other than `word/document.xml` remains byte-identical to V01. Within `document.xml`, the V01→V02 text-node comparison reports exactly one deletion: `[Section text to be drafted in a later approved version.]`. No B01 scientific prose or Section 4.3-and-later content was modified.

OOXML integrity passed `testzip`; the document retains 40 comments, 40 `commentRangeStart`, 40 `commentRangeEnd`, and 40 `commentReference` anchors; `word/comments.xml` retains the governing SHA-256; and there are no `w:ins`, `w:del`, `w:moveFrom`, or `w:moveTo` tracked-change elements.

The V02 DOCX was fully rendered to 41 pages. Pages 1–35 and 41 are pixel/byte-identical to the already-passed V01 render; pages 36–40, the only pages affected by reflow after paragraph removal, were visually inspected and show no clipping, overlap, truncation, glyph loss, or header/footer defects. Full render QA therefore passes.

`article/sections/experimental_design/Experimental_Design_B01_V01.md` was not modified, no section V02 was created, no canonical master was promoted, and no later block was opened.
