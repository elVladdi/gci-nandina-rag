# 121N — Auditoría externa — PASS

## Dictamen

```text
PROMPT121N_EXTERNAL_AUDIT = PASS
G7_F02_CLEAN_COPY_EXTERNAL_AUDIT = PASS
G7_F02 = CLOSED / APPROVED / INTEGRATED
G7_F03_AUTHORIZED = true
GROUP7_CLOSED = false
```

## Identidad de artefactos auditados

```text
Molleapasa_gv_G7F02_FINAL_CLEAN.docx
SHA256 = e734e1b93e82e732d7db99eec9fd22334e67f9621dacfedc4a559ab90f785a85
SIZE = 3909601

g7_thesis_claim_traceability_v0.3_FINAL.csv
SHA256 = 5596ea01f1a2b98373de151176f0799f54d5a1e859f60e30c3ecc26eaad32dec
SIZE = 127824
ROWS = 136
```

El CSV final conserva exactamente la identidad previamente congelada para M y no contiene filas nuevas posteriores a las 136 ya auditadas.

## Auditoría OOXML y de limpieza

Se inspeccionó directamente el paquete DOCX final.

```text
DOCX_ZIP_INTEGRITY = PASS
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 8
MEDIA_FILE_COUNT = 9
COMMENT_PARTS_PRESENT = 0
COMMENT_RANGE_START_COUNT = 0
COMMENT_RANGE_END_COUNT = 0
COMMENT_REFERENCE_COUNT = 0
REVIEW_YELLOW_HIGHLIGHT_REMAINING = 0
REVIEW_STRIKETHROUGH_REMAINING = 0
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
PROPOSAL_MARKER_PARAGRAPH_COUNT = 0
FINAL_FIGURE_VISIBLE_SEQUENCE = 1..8
TABLE_VISIBLE_SEQUENCE = 1..24
```

No se detectaron concatenaciones legacy/activas de referencias tabulares ni marcadores de propuesta de reemplazo/supresión.

## Figuras finales

Los nueve medios del paquete corresponden al medio institucional y a las ocho figuras finales. Los hashes de los ocho binarios científicos coinciden con el contrato 121N:

```text
Figura 1 = 5d7ff24f003d29d24e0d353afc9e128abf6cd5b11b6580c110e16bd8c9ef565f
Figura 2 = 6b63f7362cc2bfa001efa14e7ffe9508a4af71250d1fc95de3dddfc9a4615f37
Figura 3 = fb8e7238a140f75dae6e77724aa3d087d136c3f33cb9d389223cde722b034ddc
Figura 4 = 5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e
Figura 5 = aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0
Figura 6 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
Figura 7 = 3039a4f1b34ef57e4455da84e4e9f50d0f3cebeb8501c3bf1bb7205bf85c9824
Figura 8 = 46f26b333ade25ebd5fd65e4c5e6581bf240a03bd072b14f3c02ef832b0d2dff
```

Los reemplazos aprobados de Figuras 4–6 están materializados, las REVIEW Figuras 7–10 ya no están presentes y las antiguas Figuras 11–12 quedaron consolidadas como Figuras 7–8.

## Índice, listas y paginación

Se realizó render independiente del DOCX final con 140 páginas.

La Lista de Tablas contiene 24 entradas y las páginas extraídas del render coinciden exactamente con los 24 captions corporales:

```text
1=50; 2=52; 3=58; 4=65; 5=67; 6=70; 7=76; 8=82; 9=90; 10=92; 11=93; 12=96;
13=97; 14=100; 15=101; 16=104; 17=106; 18=108; 19=110; 20=111; 21=119; 22=122; 23=126; 24=130
```

La Lista de Figuras contiene 8 entradas y coincide exactamente con el render:

```text
1=38; 2=62; 3=95; 4=98; 5=99; 6=102; 7=123; 8=129
```

Los encabezados principales auditados también coinciden con el índice: Capítulo 1 p.8; Capítulo 2 p.17; Capítulo 3 p.48; Capítulo 4 p.92; 4.2 p.112; 4.3 p.120; Conclusiones p.133; Recomendaciones p.136; Referencias bibliográficas p.137.

## QA visual externo

Se renderizaron las 140 páginas y se revisaron mediante hojas de contacto de cobertura completa, con inspección específica de preliminares, tablas extensas, Figuras 1–8, resultados, discusión, Conclusiones, Recomendaciones y Referencias.

```text
EXTERNAL_RENDER_PAGE_COUNT = 140
NO_CLIPPING = true
NO_OVERFLOW = true
NO_OVERLAP = true
NO_BLANK_PAGES_INTRODUCED = true
FIGURES_LEGIBLE = true
TABLES_LEGIBLE = true
PAGINATION_COHERENT = true
TOC_AND_LISTS_COHERENT = true
EXTERNAL_VISUAL_QA = PASS
```

## Cierre

La copia limpia final cumple el contrato post-aprobación. No se requiere R1.

```text
121N_CLOSED_FOR_DOWNSTREAM = true
G7_F02_REVIEW_AND_CLEAN_COPY = COMPLETE
G7_F02_EXTERNAL_AUDIT = PASS
G7_F02 = CLOSED / APPROVED / INTEGRATED
G7_F03_AUTHORIZED = true
G7_F03_EXECUTED = false
```
