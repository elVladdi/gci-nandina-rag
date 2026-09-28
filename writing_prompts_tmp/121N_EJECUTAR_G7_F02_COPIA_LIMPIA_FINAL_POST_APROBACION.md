# PROMPT121N — G7-F02: COPIA LIMPIA FINAL POST-APROBACIÓN DE REVIEW V03 M

## 0. Actor, gate y propósito

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. Este bloque es una **consolidación editorial mecánica post-aprobación**; no es un nuevo bloque científico.

Lee íntegramente antes de editar:

```text
writing_prompts_tmp/121M_AUDITORIA_EXTERNA_PASS.md
commit = 5f82a51ed624b4ae2adab2ab14d90cda08c6272d

writing_prompts_tmp/121M_AUTOR_APROBACION_REVIEW_V03_M.md
commit = 49f32db42404255ea50e424ca4ff4635d32a539f

writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
commit = 583138f94646b1e84de1c28f32342e59f82988a3

writing_prompts_tmp/121M_RESPUESTA_G7_F02_V03_BLOQUE_M_CIERRE_CONCLUSIONES_Y_CORRECCIONES_EDITORIALES.md
commit = 48c936dfb2d0cfdc95b6393dfa9e8c58d3902745
```

Gate vinculante:

```text
PROMPT121M_EXTERNAL_AUDIT = PASS
AUTHOR_ACCEPTANCE_REVIEW_V03_M = APPROVED
A001_A082_AUTHOR_ACCEPTED = true
CLEAN_COPY_PREPARATION_AUTHORIZED = true
G7_F03_AUTHORIZED = false
```

Objetivo exclusivo: transformar la copia de revisión M ya aprobada en una **copia limpia final de G7-F02**, aceptando mecánicamente los cambios visibles ya aprobados, materializando las decisiones gráficas aprobadas y eliminando exclusivamente la infraestructura de revisión.

**No generes nueva ciencia. No reescribas contenido por estilo. No ejecutes G7-F03. No inicies el artículo.**

---

# 1. Entradas exactas y precondición

Trabaja exclusivamente sobre:

```text
Molleapasa_gv_G7F02_REVIEW_V03_M.docx
SHA256 = 5a89b3069f3d10fa9322c01e636e8d2806b6cdc212ef2917efc84d4016ce19da
SIZE = 4689972

g7_thesis_claim_traceability_v0.3_M.csv
SHA256 = 5596ea01f1a2b98373de151176f0799f54d5a1e859f60e30c3ecc26eaad32dec
SIZE = 127824
ROWS = 136
```

Antes de editar, verifica hashes, tamaños y filas. Si cualquiera no coincide, devuelve:

```text
PROMPT121N_EXECUTION = STOPPED_PRECONDITION
```

y no modifiques nada.

Estado estructural heredado obligatorio de M:

```text
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
COMMENT_COUNT = 222
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
TRACE_ROWS = 136
A001_A082_EXTERNALLY_AUDITED = true
```

No reconstruyas el documento desde baseline, K, L, L-R1 ni versiones anteriores.

---

# 2. Regla central de aceptación de cambios textuales

REVIEW V03 utiliza esta convención:

```text
LEGACY_REPLACED = amarillo + tachado + visible
ACTIVE_APPROVED = amarillo + no tachado + visible
UNCHANGED = normal
```

La copia limpia debe **aceptar** los cambios ya aprobados, no reescribirlos.

Para toda modificación textual A001–A082:

1. elimina físicamente únicamente el contenido legacy marcado como **amarillo + tachado**;
2. conserva exactamente el contenido activo aprobado marcado como **amarillo + no tachado**;
3. retira el resaltado amarillo del contenido activo conservado;
4. conserva sin cambio el contenido que ya estaba normal;
5. no alteres palabras, cifras, puntuación, referencias bibliográficas, estilos semánticos o estructura más allá de lo imprescindible para retirar el marcado de revisión;
6. no uses `w:del` ni `w:ins` para efectuar la limpieza.

Resultado obligatorio:

```text
REVIEW_LEGACY_VISIBLE_TEXT_REMAINING = 0
REVIEW_YELLOW_HIGHLIGHT_REMAINING = 0
REVIEW_STRIKETHROUGH_REMAINING = 0
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
```

No conviertas esta limpieza en una nueva ronda de edición científica o estilística.

---

# 3. Comentarios Word — eliminación completa post-aprobación

Los 222 comentarios de M forman parte de la infraestructura de revisión y ya cumplieron su función de trazabilidad durante la aprobación.

En la copia limpia:

- elimina los 222 comentarios Word;
- elimina todos los `commentRangeStart`, `commentRangeEnd` y `commentReference` del documento;
- elimina o limpia correctamente las partes OOXML de comentarios y sus relaciones cuando ya no sean necesarias;
- no dejes comentarios huérfanos, rangos huérfanos ni relaciones rotas;
- no cambies contenido visible al retirar comentarios.

Resultado obligatorio:

```text
COMMENT_COUNT = 0
COMMENT_RANGE_START_COUNT = 0
COMMENT_RANGE_END_COUNT = 0
COMMENT_REFERENCE_COUNT = 0
ORPHAN_COMMENT_RELATIONSHIPS = 0
```

El CSV de trazabilidad conserva los `comment_id` históricos de REVIEW V03 como evidencia de auditoría. Esos IDs **no se reinterpretan como comentarios vivos de la copia limpia**.

---

# 4. Decisiones gráficas post-aprobación

La aprobación autoral materializa ahora las decisiones gráficas que durante REVIEW V03 permanecieron deliberadamente como propuestas visibles.

## 4.1 Figuras 1–3

Conserva sin cambios científicos ni gráficos las Figuras 1–3 y sus binarios vigentes.

Binarios esperados heredados de M:

```text
Figura 1 -> SHA256 5d7ff24f003d29d24e0d353afc9e128abf6cd5b11b6580c110e16bd8c9ef565f
Figura 2 -> SHA256 6b63f7362cc2bfa001efa14e7ffe9508a4af71250d1fc95de3dddfc9a4615f37
Figura 3 -> SHA256 fb8e7238a140f75dae6e77724aa3d087d136c3f33cb9d389223cde722b034ddc
```

## 4.2 Figuras 4–6 — aceptar los reemplazos aprobados

En M, cada una conserva el gráfico legacy y, después del marcador `PROPUESTA DE REEMPLAZO DEL ELEMENTO GRÁFICO ANTERIOR — NO ES NUMERACIÓN FINAL`, incorpora un gráfico nuevo aprobado.

Para la copia limpia:

- elimina el gráfico legacy de la Figura 4 y conserva como Figura 4 el gráfico de reemplazo aprobado;
- elimina el gráfico legacy de la Figura 5 y conserva como Figura 5 el gráfico de reemplazo aprobado;
- elimina el gráfico legacy de la Figura 6 y conserva como Figura 6 el gráfico de reemplazo aprobado;
- elimina todos los párrafos `PROPUESTA DE REEMPLAZO...`;
- elimina los captions/títulos legacy sustituidos;
- conserva exactamente la redacción científica aprobada asociada a cada reemplazo, sin resumirla ni reinterpretarla;
- conserva un único campo `SEQ Figura` por figura final;
- evita cualquier duplicación de número o caption.

Binarios finales aprobados:

```text
Figura 4 final -> SHA256 5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e
Figura 5 final -> SHA256 aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0
Figura 6 final -> SHA256 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
```

Los binarios legacy de las antiguas Figuras 4–6 no deben quedar referenciados ni almacenados como medios huérfanos:

```text
legacy Figura 4 -> 949eabafb33fbaa0328e72e354cc2da17f39573af1c202f838e9ee11c36a54ae
legacy Figura 5 -> df0ecf10294d7b646f5b9bd1fa5cf52f98446ea3388a5c671a0911514561ad16
legacy Figura 6 -> aff335a5edc4563f091ea945a484e870264df983472d7cec9d66d9cbee58b65a
```

### Estructura final de caption para Figuras 4–6

Mantén la convención nativa del documento:

1. párrafo de número `Figura N` con campo `SEQ Figura`;
2. título científico;
3. gráfico aprobado;
4. nota/caption explicativa cuando corresponda.

La redacción aprobada actualmente aparece en M en el párrafo posterior al gráfico de reemplazo con prefijo literal `Figura N.`. Para consolidarla sin inventar texto:

- elimina únicamente el prefijo redundante `Figura N.` de ese párrafo;
- usa su **primer enunciado completo** como título científico;
- conserva el resto del texto, sin cambiar palabras ni cifras, como nota explicativa inmediatamente posterior al gráfico; puede añadirse únicamente el prefijo editorial `Nota.` para ajustarse a la convención nativa;
- no acortes, parafrasees ni amplíes esa redacción.

## 4.3 Figuras 7–10 de REVIEW V03 — supresión aprobada

Elimina completamente los cuatro bloques gráficos legacy aprobados para supresión:

```text
REVIEW Figura 7 -> suprimir
REVIEW Figura 8 -> suprimir
REVIEW Figura 9 -> suprimir
REVIEW Figura 10 -> suprimir
```

Para cada una elimina:

- párrafo `Figura N` y su campo `SEQ Figura`;
- título/caption asociado;
- dibujo/imagen;
- párrafo `PROPUESTA DE SUPRESIÓN DEL ELEMENTO GRÁFICO ANTERIOR — SE CONSERVA PARA REVISIÓN / NO ES NUMERACIÓN FINAL`;
- relaciones y medios que queden sin uso.

Binarios que deben desaparecer del paquete final si no tienen ninguna otra referencia:

```text
Figura 7 legacy  -> SHA256 7a8862f4f1b338716c2c5446377f8e5e0a7595a4c555d83828918d67f2794cfe
Figura 8 legacy  -> SHA256 64d0417b553638dd85ac155f4ccfbc2de45412e61c5a4abf4c93316710cc6695
Figura 9 legacy  -> SHA256 287950c94a214c49c408be67f4e512b6b99e66b2e97ab5edfcefbbbaba074c66
Figura 10 legacy -> SHA256 cc9b791b0fbf76186582cf45ff7f34ac0a7c7724e0e2bec9375458d6def556e9
```

No sustituyas estas cuatro figuras por gráficos nuevos.

## 4.4 Renumeración final de las Figuras 11–12 retenidas

Las Figuras 11 y 12 de REVIEW V03 permanecen científicamente vigentes y fueron conservadas durante la revisión únicamente para evitar renumeración anticipada.

Después de suprimir REVIEW Figuras 7–10:

```text
REVIEW Figura 11 -> FINAL Figura 7
REVIEW Figura 12 -> FINAL Figura 8
```

Conserva sus binarios exactamente:

```text
FINAL Figura 7 (antes 11) -> SHA256 3039a4f1b34ef57e4455da84e4e9f50d0f3cebeb8501c3bf1bb7205bf85c9824
FINAL Figura 8 (antes 12) -> SHA256 46f26b333ade25ebd5fd65e4c5e6581bf240a03bd072b14f3c02ef832b0d2dff
```

Actualiza campos `SEQ Figura`, resultados visibles, bookmarks/cross-references si existieran y la Lista de Figuras. No cambies el contenido científico de sus títulos ni imágenes.

## 4.5 Estado final esperado de figuras y medios

Después de consolidar:

```text
FINAL_FIGURE_COUNT = 8
SEQ_FIGURA_COUNT = 8
FINAL_FIGURE_VISIBLE_SEQUENCE = 1..8
MEDIA_FILE_COUNT = 9
```

Los nueve medios finales deben corresponder únicamente a:

1. el emblema/imagen institucional existente;
2. Figura 1;
3. Figura 2;
4. Figura 3;
5. reemplazo aprobado de Figura 4;
6. reemplazo aprobado de Figura 5;
7. reemplazo aprobado de Figura 6;
8. antigua Figura 11 renumerada a Figura 7;
9. antigua Figura 12 renumerada a Figura 8.

No dejes medios huérfanos ni relaciones gráficas no utilizadas.

---

# 5. Tablas y referencias cruzadas

Las 24 tablas corporales ya fueron aprobadas y auditadas.

No modifiques contenido científico, estructura, propiedades o numeración de ninguna tabla.

Resultado obligatorio:

```text
TABLE_OBJECT_COUNT = 24
TABLE_VISIBLE_SEQUENCE = 1..24
TABLES_1_TO_24_PRESERVED = true
```

Al aceptar el marcado de revisión, deben quedar únicamente las referencias tabulares activas aprobadas. Verifica expresamente que no sobrevivan concatenaciones legacy/activas como:

```text
Tabla 4 Tabla 3
Tabla 8 Tabla 7
Tabla 9 Tabla 8
Tabla 10 Tabla 9
Tabla 13 Tabla 12
Tabla 21 Tabla 20
Tabla 24 Tabla 23
```

La Lista de Tablas final debe mostrar una sola secuencia limpia `Tabla 1`–`Tabla 24`, sin texto tachado, sin `Tabla 25` y con páginas finales correctas.

---

# 6. Índice general, Lista de Tablas y Lista de Figuras

REVIEW V03 preservó deliberadamente campos y paginación para comparabilidad humana. La copia limpia ya no tiene esa restricción.

Después de consolidar todo el contenido:

1. actualiza los campos automáticos del documento de manera controlada;
2. actualiza el Índice general para que los números de página correspondan al documento limpio;
3. actualiza la Lista de Tablas para que conserve 24 entradas, Tabla 1–24, con páginas finales reales;
4. actualiza la Lista de Figuras para que contenga exactamente 8 entradas, Figura 1–8, con páginas finales reales;
5. conserva estilos, tabulaciones, líderes, jerarquía y tipografía nativos;
6. no introduzcas entradas nuevas ajenas a los headings/captions existentes;
7. no alteres títulos de secciones ni captions científicos fuera de la renumeración de figuras autorizada.

Si el software no materializa de forma confiable los resultados de los campos, calcula las páginas desde una renderización final y reconcilia únicamente los resultados visibles, preservando las instrucciones de campo cuando sea técnicamente posible.

Verifica:

```text
TOC_PAGE_NUMBERS_MATCH_FINAL_RENDER = true
LIST_OF_TABLES_COUNT = 24
LIST_OF_TABLES_SEQUENCE = 1..24
LIST_OF_TABLES_PAGES_MATCH_FINAL_RENDER = true
LIST_OF_FIGURES_COUNT = 8
LIST_OF_FIGURES_SEQUENCE = 1..8
LIST_OF_FIGURES_PAGES_MATCH_FINAL_RENDER = true
```

---

# 7. Trazabilidad final

No existe una acción científica nueva después de A082. La consolidación limpia no debe fabricar A083 ni modificar la historia de A001–A082.

Genera:

```text
g7_thesis_claim_traceability_v0.3_FINAL.csv
```

como **copia byte-idéntica** del CSV M:

```text
EXPECTED_SHA256 = 5596ea01f1a2b98373de151176f0799f54d5a1e859f60e30c3ecc26eaad32dec
EXPECTED_SIZE = 127824
ROWS = 136
TRACE_CSV_BYTE_IDENTICAL_TO_M = true
NEW_TRACE_ROWS_ADDED = 0
```

Los `comment_id` de este CSV son identificadores históricos de la revisión y permanecen para trazabilidad. No requieren comentarios vivos en la copia limpia.

La ejecución de 121N se documentará en su respuesta oficial, no mediante una nueva fila Axxx.

---

# 8. Prohibiciones científicas y editoriales

Durante 121N está prohibido:

- introducir ciencia nueva;
- recalcular métricas;
- ejecutar experimentos;
- abrir o reabrir EXP12;
- buscar en la web;
- añadir, eliminar o sustituir referencias bibliográficas;
- cambiar disposiciones de HG/HE1–HE5;
- corregir de oficio redacción no marcada como cambio aprobado;
- normalizar estilo por preferencia personal;
- modificar Recomendaciones;
- modificar problema, objetivos o hipótesis aprobadas;
- reabrir A001–A082;
- ejecutar G7-F03;
- iniciar artículo, resumen extendido u otro producto posterior.

Guardrails científicos que deben permanecer intactos:

```text
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE
HG = NO_FORMAL_DISPOSITION_FOUND

HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_OR_LEGAL_CORRECTNESS
EXP11A != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B != SEED_SUPERPOPULATION_INFERENCE
ATTEMPT06 != GLOBAL_ZERO_IMPACT
```

---

# 9. Controles OOXML y de integridad

La copia limpia debe abrir sin reparación ni advertencias.

Verifica al menos:

```text
DOCX_ZIP_INTEGRITY = PASS
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 8
MEDIA_FILE_COUNT = 9
COMMENT_COUNT = 0
COMMENT_RANGE_START_COUNT = 0
COMMENT_RANGE_END_COUNT = 0
COMMENT_REFERENCE_COUNT = 0
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
REVIEW_YELLOW_HIGHLIGHT_REMAINING = 0
REVIEW_STRIKETHROUGH_REMAINING = 0
PROPOSAL_MARKER_PARAGRAPH_COUNT = 0
UNUSED_MEDIA_RELATIONSHIPS = 0
BROKEN_INTERNAL_RELATIONSHIPS = 0
```

Busca y exige ausencia de estas cadenas de gobernanza/revisión en texto visible:

```text
PROPUESTA DE REEMPLAZO
PROPUESTA DE SUPRESIÓN
NO ES NUMERACIÓN FINAL
SE CONSERVA PARA REVISIÓN
A001
A082
PROMPT121
REVISION_REQUIRED
PENDING_EXTERNAL_AUDIT
```

No elimines términos científicos legítimos solo por coincidencias parciales; esta búsqueda se utiliza como control de fugas de gobernanza/revisión.

---

# 10. QA visual final integral

Renderiza **todo el DOCX limpio**, no solo páginas afectadas.

Inspecciona todas las páginas mediante hojas de contacto y, a resolución de página, como mínimo:

1. portada e índice general;
2. Lista de Tablas;
3. Lista de Figuras;
4. todas las Figuras 1–8;
5. zonas donde antes estaban las REVIEW Figuras 7–10 para verificar que no queden huecos, captions huérfanos o saltos extraños;
6. todas las Tablas 1–24;
7. 4.1–4.3;
8. Conclusiones;
9. Recomendaciones;
10. transición hacia Referencias bibliográficas;
11. últimas páginas del documento.

Criterios obligatorios:

```text
NO_CLIPPING = true
NO_OVERFLOW = true
NO_OVERLAP = true
NO_ORPHAN_CAPTIONS = true
NO_ORPHAN_NOTES = true
NO_BLANK_PAGES_INTRODUCED_BY_CLEANUP = true
FIGURES_LEGIBLE = true
TABLES_LEGIBLE = true
PAGINATION_COHERENT = true
TOC_AND_LISTS_COHERENT = true
LOCAL_VISUAL_REVIEW = PASS
```

No declares COMPLETE si existe un defecto visual material.

---

# 11. Salidas obligatorias

No sobrescribas M.

Genera exclusivamente como artefactos finales de este bloque:

```text
Molleapasa_gv_G7F02_FINAL_CLEAN.docx
g7_thesis_claim_traceability_v0.3_FINAL.csv
```

Calcula SHA-256 y tamaño del DOCX final. Para el CSV final confirma el hash byte-idéntico esperado.

Publica respuesta oficial en:

```text
writing_prompts_tmp/121N_RESPUESTA_G7_F02_COPIA_LIMPIA_FINAL_POST_APROBACION.md
```

La respuesta debe reportar como mínimo:

```text
PROMPT121N_EXECUTION = COMPLETE | REVISION_REQUIRED | STOPPED_PRECONDITION
AUTHOR_ACCEPTANCE_VERIFIED = true|false
SOURCE_M_IDENTITY_MATCH = true|false
LEGACY_REVIEW_TEXT_REMOVED = true|false
ACTIVE_APPROVED_TEXT_PRESERVED = true|false
REVIEW_YELLOW_HIGHLIGHT_REMAINING = <int>
REVIEW_STRIKETHROUGH_REMAINING = <int>
COMMENT_COUNT = <int>
COMMENT_RANGE_START_COUNT = <int>
COMMENT_RANGE_END_COUNT = <int>
COMMENT_REFERENCE_COUNT = <int>
FIGURE_4_REPLACEMENT_MATERIALIZED = true|false
FIGURE_5_REPLACEMENT_MATERIALIZED = true|false
FIGURE_6_REPLACEMENT_MATERIALIZED = true|false
FIGURE_7_TO_10_REVIEW_SUPPRESSED = true|false
OLD_FIGURE_11_RENUMBERED_TO_7 = true|false
OLD_FIGURE_12_RENUMBERED_TO_8 = true|false
FINAL_FIGURE_COUNT = 8
SEQ_FIGURA_COUNT = 8
MEDIA_FILE_COUNT = 9
TABLE_OBJECT_COUNT = 24
LIST_OF_TABLES_SEQUENCE = 1..24 | FAIL
LIST_OF_FIGURES_SEQUENCE = 1..8 | FAIL
TOC_PAGE_NUMBERS_MATCH_FINAL_RENDER = true|false
LIST_OF_TABLES_PAGES_MATCH_FINAL_RENDER = true|false
LIST_OF_FIGURES_PAGES_MATCH_FINAL_RENDER = true|false
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
PROPOSAL_MARKER_PARAGRAPH_COUNT = 0
NEW_REFERENCES = 0
NEW_SCIENCE = 0
TRACE_CSV_BYTE_IDENTICAL_TO_M = true|false
TRACE_CSV_ROWS = 136
G7_F03_EXECUTED = false
LOCAL_VISUAL_REVIEW = PASS|FAIL
FINAL_RENDER_PAGE_COUNT = <int>
DOCX_FINAL_SHA256 = <hash>
DOCX_FINAL_SIZE = <bytes>
CSV_FINAL_SHA256 = 5596ea01f1a2b98373de151176f0799f54d5a1e859f60e30c3ecc26eaad32dec
CSV_FINAL_SIZE = 127824
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

---

# 12. Parada obligatoria

Al finalizar, detente para auditoría externa.

No declares G7-F02 cerrado por tu cuenta.
No autorices G7-F03.
No ejecutes ningún bloque posterior.

Estado esperado al terminar correctamente:

```text
PROMPT121N_EXECUTION = COMPLETE
G7_F02_CLEAN_COPY = GENERATED / PENDING_EXTERNAL_AUDIT
G7_F02 = ACTIVE / AUTHOR_ACCEPTED / PENDING_CLEAN_COPY_EXTERNAL_AUDIT / NOT_YET_CLOSED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```
