# Experimental Design B01 V03 — Structure V02 skeleton alignment response

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT
GOVERNING_DECISION = D-047
GOVERNING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
GOVERNING_STRUCTURE_GIT_BLOB_CHECK = f5270e02e3af1407a2dec2988d6382e433972d3e / PASS
BASELINE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
BASELINE_MD_SHA256_CHECK = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346 / PASS
BASELINE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
BASELINE_DOCX_SHA256_CHECK = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7 / PASS
OUTPUT_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md
OUTPUT_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
OUTPUT_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx
OUTPUT_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
SECTION_3_5_AND_3_7_TEXT_UNCHANGED = PASS
SECTION_4_1_TO_4_2_3_TEXT_UNCHANGED = PASS
SECTION_4_3_TO_4_8_CHANGE_CLASS = STRUCTURE_V02_SKELETON_ONLY / PASS
SPANISH_PRE_4_3_NONSTRUCTURAL_CHANGE = ONE_AUTHORIZED_STALE_PLACEHOLDER_DELETION_ONLY / PASS
OLD_4_9_4_10_4_11_REMOVED = PASS
OLD_4_3_1_TO_4_3_4_REMOVED = PASS
NEW_4_6_1_TO_4_6_3_PRESENT_ENGLISH = PASS
NEW_4_6_1_TO_4_6_3_PRESENT_SPANISH = PASS
STALE_SPANISH_SECTION4_PLACEHOLDER_REMOVED = PASS
NEW_SCIENTIFIC_PROSE_4_3_TO_4_8 = NO
SECTION_5_AND_LATER_TEXT_UNCHANGED = PASS
DOCX_CHANGED_PACKAGE_PARTS = word/document.xml ONLY
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
COMMENT_RANGE_START_COUNT = 40
COMMENT_RANGE_END_COUNT = 40
COMMENT_REFERENCE_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / PASS
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 39
CLIPPING = NONE_OBSERVED
OVERLAP = NONE_OBSERVED
MISSING_GLYPHS = NONE_OBSERVED
LAYOUT_DEFECTS = NONE_OBSERVED
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_STARTED / NOT_AUTHORIZED
RESULTS = NOT_STARTED / NOT_AUTHORIZED
AUTHOR_APPROVAL_SELF_GRANT = NO
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
TERMINAL_STATE = DELIVERED_FOR_DIFFERENTIAL_AUDIT
```

### Verificación diferencial

La comparación del master Markdown V03 con V04 confirmó que el contenido anterior a 4.3 permanece idéntico en la Parte I y que la única diferencia anterior a 4.3 en la Parte II es la eliminación expresamente autorizada del placeholder residual situado entre `4. Diseño experimental` y `4.1. Entorno y alcance experimental`. La comparación textual del DOCX confirma igualmente que las dos enmiendas ya auditadas de 3.5/3.7 y la prosa de 4.1–4.2.3 no cambiaron.

Desde 4.3 hasta el final de Section 4, el único cambio es el reemplazo mecánico del esqueleto V01 no redactado por el esqueleto y las notas de función de Structure V02. No se añadió prosa científica nueva. Desaparecieron 4.9, 4.10, 4.11 y 4.3.1–4.3.4, y quedaron incorporadas 4.6.1, 4.6.2 y 4.6.3 en ambos idiomas. Section 5 y todo el contenido posterior permanecen textualmente inalterados.

La comprobación OOXML confirmó que el conjunto de partes del paquete se conserva y que únicamente `word/document.xml` cambió. `word/comments.xml` conserva exactamente su identidad esperada, con 40 comentarios, 40 inicios de rango, 40 finales de rango y 40 referencias; no existen cambios controlados. El DOCX completo se renderizó en 39 páginas y todas fueron inspeccionadas visualmente sin observar clipping, solapamientos, glifos faltantes ni defectos de layout.

No se promovió `ARTICLE_MASTER_V010`, no se abrió la redacción científica de 4.3–4.8 y no se concede aprobación, cierre, congelamiento ni integración de B01.

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT
GOVERNING_DECISION = D-047
GOVERNING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
GOVERNING_STRUCTURE_GIT_BLOB_CHECK = f5270e02e3af1407a2dec2988d6382e433972d3e / PASS
BASELINE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
BASELINE_MD_SHA256_CHECK = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346 / PASS
BASELINE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
BASELINE_DOCX_SHA256_CHECK = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7 / PASS
OUTPUT_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md
OUTPUT_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
OUTPUT_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx
OUTPUT_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
SECTION_3_5_AND_3_7_TEXT_UNCHANGED = PASS
SECTION_4_1_TO_4_2_3_TEXT_UNCHANGED = PASS
SECTION_4_3_TO_4_8_CHANGE_CLASS = STRUCTURE_V02_SKELETON_ONLY / PASS
SPANISH_PRE_4_3_NONSTRUCTURAL_CHANGE = ONE_AUTHORIZED_STALE_PLACEHOLDER_DELETION_ONLY / PASS
OLD_4_9_4_10_4_11_REMOVED = PASS
OLD_4_3_1_TO_4_3_4_REMOVED = PASS
NEW_4_6_1_TO_4_6_3_PRESENT_ENGLISH = PASS
NEW_4_6_1_TO_4_6_3_PRESENT_SPANISH = PASS
STALE_SPANISH_SECTION4_PLACEHOLDER_REMOVED = PASS
NEW_SCIENTIFIC_PROSE_4_3_TO_4_8 = NO
SECTION_5_AND_LATER_TEXT_UNCHANGED = PASS
DOCX_CHANGED_PACKAGE_PARTS = word/document.xml ONLY
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
COMMENT_RANGE_START_COUNT = 40
COMMENT_RANGE_END_COUNT = 40
COMMENT_REFERENCE_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / PASS
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 39
CLIPPING = NONE_OBSERVED
OVERLAP = NONE_OBSERVED
MISSING_GLYPHS = NONE_OBSERVED
LAYOUT_DEFECTS = NONE_OBSERVED
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_STARTED / NOT_AUTHORIZED
RESULTS = NOT_STARTED / NOT_AUTHORIZED
AUTHOR_APPROVAL_SELF_GRANT = NO
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
TERMINAL_STATE = DELIVERED_FOR_DIFFERENTIAL_AUDIT
```

### Differential verification

The V03-to-V04 Markdown comparison confirmed that Part I remains identical before Section 4.3 and that the only Part-II difference before Section 4.3 is the expressly authorized deletion of the stale placeholder between `4. Diseño experimental` and `4.1. Entorno y alcance experimental`. DOCX text comparison likewise confirms that the already audited 3.5/3.7 amendments and the 4.1–4.2.3 scientific prose remain unchanged.

From Section 4.3 through the end of Section 4, the only change is the mechanical replacement of the unfilled V01 skeleton with the Structure-V02 skeleton and its approved drafting-purpose notes. No new scientific prose was introduced. Sections 4.9, 4.10, 4.11 and 4.3.1–4.3.4 were removed, while 4.6.1, 4.6.2 and 4.6.3 are present in both language mirrors. Section 5 and all later content remain textually unchanged.

OOXML verification confirmed that the package-part set is preserved and only `word/document.xml` changed. `word/comments.xml` retains the exact expected identity, with 40 comments, 40 range starts, 40 range ends and 40 references; there are no tracked changes. The complete DOCX was rendered to 39 pages, and every page was visually inspected with no observed clipping, overlap, missing glyphs, or layout defects.

`ARTICLE_MASTER_V010` was not promoted, scientific drafting of Sections 4.3–4.8 was not opened, and no B01 approval, closure, freezing, or integration is granted by this execution.