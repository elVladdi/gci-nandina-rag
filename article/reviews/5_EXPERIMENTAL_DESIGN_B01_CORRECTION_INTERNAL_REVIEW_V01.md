# Experimental Design B01 correction — Internal review V01

## Español

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_B01_CORRECTION_INTERNAL_REVIEW_V01
BLOCK = EXPERIMENTAL_DESIGN_B01_CORRECTION
REVIEWER = IA_GESTORA
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B01_CORRECTION_RESPONSE_V01.md@3e14e8f27512a0d3fabda17933893e9efd363608
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_INTERNAL_REVIEW_V01.md@d1e78932cbc2eebc0b0594a418661e6a599ee567
SOURCE_MASTER_CANDIDATE_MD_SHA256 = 6e443353c362410ffe70c880b49647a12b1a88d3ec72a12675cce5e086435754
SOURCE_CANDIDATE_DOCX_SHA256 = 4089ca75267ed05d1406b9bf2c1f895300f4da77ccb3e0559b2ef43ad49f3e5c
CORRECTED_MASTER_CANDIDATE_MD_SHA256 = bdcbbd474d467e978777e031ae568b3fb5d089c32606289f0818ea852a4d4c44
CORRECTED_CANDIDATE_DOCX_SHA256 = 53c23c6f951aa8d76ea647fe97105cddd43883c3b3b93e6850ea8eaf861053b2
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
STALE_SPANISH_SECTION4_PLACEHOLDER_REMOVED = PASS
UNAUTHORIZED_TEXTUAL_CHANGE = NONE
B01_SCIENTIFIC_PROSE_CHANGED = NO
SECTION_MD_CHANGED = NO
SECTION_4_3_AND_LATER_MODIFIED = NO
ZIP_OOXML_MEMBER_DIFF = word/document.xml ONLY
DOCX_COMMENT_COUNT = 40
COMMENT_RANGE_START_COUNT = 40
COMMENT_RANGE_END_COUNT = 40
COMMENT_REFERENCE_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
TRACKED_CHANGES = 0
OOXML_QA = PASS
RENDERED_PAGE_COUNT = 41
PIXEL_IDENTICAL_PAGES = 1-35,41
REFLOWED_PAGES_VISUALLY_INSPECTED = 36-40
FULL_RENDER_QA = PASS
DIFFERENTIAL_REVIEW = PASS
OVERALL_REVIEW = PASS
AUTHOR_APPROVAL_GATE = OPEN
ARTICLE_MASTER_V010 = NOT_PROMOTED
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Verificación diferencial independiente

La IA Gestora verificó directamente los artefactos V01 y V02. En el Markdown acumulativo, el diff contiene una sola eliminación textual: el placeholder español residual `[Section text to be drafted in a later approved version.]` situado entre la nota introductoria de `4. Diseño experimental` y `4.1. Entorno de evaluación`. No existe ninguna otra diferencia textual.

En el DOCX, los nombres de miembros ZIP/OOXML son idénticos y el único miembro cuyo hash cambia es `word/document.xml`. La comparación de párrafos OOXML identifica exactamente una operación `delete`, correspondiente al mismo placeholder. `word/comments.xml` permanece byte a byte idéntico con SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`.

La integridad del paquete pasa `testzip`; se conservan 40 comentarios, 40 `commentRangeStart`, 40 `commentRangeEnd` y 40 `commentReference`, con cero `w:ins`, `w:del`, `w:moveFrom` y `w:moveTo`.

### 2. QA visual

Ambas versiones se renderizaron independientemente a 41 páginas. Las páginas 1–35 y 41 son pixel-identical V01→V02. Las páginas 36–40 son las únicas afectadas por el reflujo esperado y fueron inspeccionadas visualmente; no presentan clipping, overlap, truncamiento, pérdida de glifos ni defectos de encabezado o pie. El render V02 completo es aceptable.

### 3. Dictamen

La corrección obligatoria quedó resuelta sin modificar la prosa científica de B01 ni contenido de 4.3 o posteriores. Se mantiene el `PASS` científico del review padre y se elimina el único defecto estructural que impedía abrir el gate autoral.

Por tanto:

```text
EXPERIMENTAL_DESIGN_B01 = VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
```

No se promueve `ARTICLE_MASTER_V010` ni se abre Experimental Design B02 hasta decisión explícita del autor.

---

## English

The independent differential review confirms that V01→V02 removes exactly one stale Spanish Section-4 placeholder and introduces no other textual or scientific change. Only `word/document.xml` changes in the DOCX package; comments and anchors are preserved exactly, tracked changes remain zero, and the complete 41-page render passes visual QA. Experimental Design B01 is therefore `VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL`; V010 promotion and B02 remain blocked pending explicit author approval.
