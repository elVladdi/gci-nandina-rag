# Experimental Design B01 V04 — Independent differential review

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B01_V04_STRUCTURE_ALIGNMENT_INTERNAL_REVIEW_V01
DATE = 2026-09-25
ROLE = IA_GESTORA / LEAD_SCIENTIFIC_EDITOR
GOVERNING_DECISION = D-047
GOVERNING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT_RESPONSE_V01.md@92a46b78a0cb192dba2a5cff826990baed17db99
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
BASELINE_MD_SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
BASELINE_DOCX_SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
OUTPUT_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md
OUTPUT_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
OUTPUT_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx
OUTPUT_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
DIFFERENTIAL_SCOPE = PASS
B01_SCIENTIFIC_PROSE_PRESERVATION = PASS
SECTION_3_5_AND_3_7_PRESERVATION = PASS
STRUCTURE_V02_ALIGNMENT = PASS
STALE_SPANISH_PLACEHOLDER_REMOVAL = PASS
SECTION_5_AND_LATER_PRESERVATION = PASS
NEW_SCIENTIFIC_PROSE_4_3_TO_4_8 = NONE
DOCX_OOXML_INTEGRITY = PASS
DOCX_RENDER_QA = PASS
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OVERALL = PASS
AUTHOR_APPROVAL_GATE = OPEN
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Objeto de la auditoría

La revisión fue diferencial y se limitó a verificar el cumplimiento exacto de D-047. No se reabrió la revisión científica de 4.1–4.2.3 ni de las dos enmiendas editoriales de 3.5/3.7, que ya habían obtenido PASS en la auditoría V03.

## 2. Identidad de artefactos — PASS

Los hashes calculados independientemente sobre los archivos entregados coinciden exactamente con la respuesta de la IA de Redacción:

- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md`: `0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8`.
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx`: `bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d`.

Los baseline V03 disponibles también coinciden con sus hashes gobernantes.

## 3. Comparación Markdown V03 → V04 — PASS

La comparación unificada confirma únicamente las dos clases de cambio autorizadas por D-047:

1. reemplazo mecánico del esqueleto no redactado de Section 4 desde 4.3 por la Structure V02 aprobada, en ambos idiomas;
2. eliminación del placeholder español residual situado entre `4. Diseño experimental` y `4.1. Entorno y alcance experimental`.

No se detectaron modificaciones en la prosa científica auditada de 4.1–4.2.3 ni en las enmiendas de 3.5/3.7. Tampoco se modificó Section 5 ni contenido posterior.

La estructura final contiene 4.3–4.8 según Structure V02, incluidas 4.6.1–4.6.3 en ambos idiomas. Desaparecieron 4.9, 4.10, 4.11 y 4.3.1–4.3.4. No se añadió prosa científica nueva en 4.3–4.8; solo se incorporaron las notas de función ya aprobadas y placeholders correspondientes.

## 4. OOXML y comentarios — PASS

La comparación de paquetes DOCX confirma que ambos paquetes contienen las mismas 14 partes y que únicamente `word/document.xml` cambió. `word/comments.xml` permanece byte-identical con SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`.

El V04 conserva:

- 40 comentarios;
- 40 `commentRangeStart`;
- 40 `commentRangeEnd`;
- 40 `commentReference`;
- 0 `w:ins`;
- 0 `w:del`;
- 0 `w:moveFrom`;
- 0 `w:moveTo`.

La integridad ZIP/OOXML es correcta.

## 5. Render completo — PASS

El DOCX V04 fue renderizado independientemente mediante el flujo canónico de QA. Se obtuvieron 39 páginas y se inspeccionaron visualmente todas. No se observaron clipping, solapamientos, glifos faltantes, tablas rotas, encabezados/pies desplazados ni defectos de maquetación. La reducción de 40 a 39 páginas respecto del V03 es coherente con la compactación del esqueleto 4.3+ y la eliminación del placeholder residual.

## 6. Dictamen

```text
B01_V04_DIFFERENTIAL_REVIEW = PASS
B01_SCIENTIFIC_CONTENT = VERIFIED / PASS
B01_EDITORIAL_FOCUS = VERIFIED / PASS
CUMULATIVE_MASTER_STRUCTURE_V02_ALIGNMENT = PASS
STALE_SPANISH_SECTION4_PLACEHOLDER = RESOLVED
DOCX_QA = PASS
EXPERIMENTAL_DESIGN_B01 = VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
```

La corrección estructural requerida por D-047 queda cerrada técnicamente. Esta auditoría no concede aprobación autoral, cierre, congelamiento ni integración. `ARTICLE_MASTER_V009` continúa como master canónico y `ARTICLE_MASTER_V010` no debe promoverse hasta una aprobación explícita del autor y el posterior gate de integración.

Section 4.3–4.8 permanece cerrada para redacción científica hasta que B01 sea aprobado por el autor y formalmente cerrado/integrado.