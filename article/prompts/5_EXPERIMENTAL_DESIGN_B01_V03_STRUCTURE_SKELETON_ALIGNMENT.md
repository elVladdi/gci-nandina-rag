# Experimental Design B01 V03 — Structure V02 skeleton alignment

## 1. Identidad y mandato

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT
ROLE = DRAFTING_AI / TECHNICAL_EDITORIAL_CORRECTION_ONLY
GOVERNING_DECISION = article/governance/D047_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT.md
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_V02_INTERNAL_REVIEW_V01.md
GOVERNING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
GOVERNING_STRUCTURE_GIT_BLOB = f5270e02e3af1407a2dec2988d6382e433972d3e
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
BASELINE_MD_SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
BASELINE_DOCX_SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
EXPECTED_COMMENT_COUNT = 40
EXPECTED_COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
SCIENTIFIC_REWRITE = NOT_AUTHORIZED
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Ejecuta únicamente esta corrección estructural. No reescribas, mejores, resumas ni estilices la prosa científica ya auditada.

## 2. Precedencia y onboarding mínimo

Antes de editar:

1. confirma repo `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`;
2. lee `article/START_HERE.md`;
3. lee `article/ARTICLE_STATUS.md`;
4. lee `article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md`;
5. lee `article/governance/D046_EXPERIMENTAL_DESIGN_B01_REOPENING_UNDER_STRUCTURE_V02.md`;
6. lee `article/governance/D047_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT.md`;
7. lee `article/reviews/5_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_V02_INTERNAL_REVIEW_V01.md`;
8. verifica `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md` y su blob `f5270e02e3af1407a2dec2988d6382e433972d3e`;
9. verifica los dos artefactos baseline adjuntos por SHA-256 antes de modificarlos.

D-047 resuelve de forma estrecha la contradicción de D-046: aunque 4.3+ continúa cerrado para redacción científica, se permite modificar su **esqueleto no redactado** únicamente para hacerlo coincidir con Structure V02.

D-021, D-022, D-023, D-035 y D-047 permanecen vinculantes. No uses Base64 manual, chunking, fragmentación, recomposición, archivos auxiliares, ramas temporales ni múltiples commits como workaround de transferencia.

Si cualquiera de los dos baseline no coincide exactamente con el SHA esperado, detente con:

`B01_V03_STRUCTURE_ALIGNMENT_BASELINE_MISMATCH`

## 3. Objetivo único

Producir una V04 técnicamente corregida mediante **solo dos clases de cambios**:

### A. Alineación mecánica del esqueleto no redactado de Section 4

En Part I y Part II, sustituye el esqueleto legado V01 desde 4.3 hasta el final de Section 4 por la estructura aprobada V02.

La jerarquía final debe ser exactamente:

```text
4.3 Documentary corpus and evidence resource
4.4 Partition validity and dependence controls
4.5 Experimental system configuration and execution
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
4.7 Statistical and robustness analysis
4.8 Reproducibility resources
```

Espejo español:

```text
4.3 Corpus documental y recurso de evidencia
4.4 Validez de particiones y control de dependencia
4.5 Configuración y ejecución experimental
4.6 Marco y protocolos de evaluación
  4.6.1 Evaluación de recuperación de candidatos
  4.6.2 Evaluación de evidencia documental
  4.6.3 Evaluación de explicación controlada
4.7 Análisis estadístico y de robustez
4.8 Recursos de reproducibilidad
```

Usa las notas de función ya aprobadas en `KBS_ARTICLE_WORKING_STRUCTURE_V02.md` como drafting notes internas. No inventes contenido científico para completar ninguna de esas secciones. Los placeholders que indiquen contenido futuro pueden mantenerse de forma coherente con el working master, pero no debe sobrevivir ningún encabezado 4.9, 4.10 o 4.11 ni las antiguas subsecciones 4.3.1–4.3.4.

### B. Eliminar un placeholder residual específico

En Part II, elimina únicamente el placeholder:

`[Section text to be drafted in a later approved version.]`

que aparece entre:

`4. Diseño experimental`

y
`4.1. Entorno y alcance experimental`.

No elimines indiscriminadamente placeholders de secciones que todavía no han sido redactadas.

## 4. Contenido que debe permanecer inalterado

No modifiques el texto científico ya auditado de:

- Introduction;
- Related Work;
- Section 3, incluidas las dos enmiendas de 3.5 y 3.7 ya verificadas;
- 4.1 `Experimental setting and scope` / `Entorno y alcance experimental`;
- 4.2 `Historical data and experimental dataset construction` / `Datos históricos y construcción de los datasets experimentales`;
- 4.2.1 `Source and data collection` / `Fuente y recolección`;
- 4.2.2 `Processing and curation` / `Procesamiento y curación`;
- 4.2.3 `Partition construction and dataset composition` / `Construcción de particiones y composición`;
- Section 5 y posteriores.

No cambies cifras, puntuación, terminología, ortografía, espacios o saltos de párrafo en esa prosa con la excusa de mejorar estilo. Esta ejecución no es una nueva revisión científica.

## 5. Prohibiciones expresas

```text
NEW_SCIENTIFIC_PROSE_4_3_TO_4_8 = PROHIBITED
B01_REWRITE = PROHIBITED
SECTION_3_REWRITE = PROHIBITED
RESULTS_DRAFTING = PROHIBITED
DISCUSSION_DRAFTING = PROHIBITED
NEW_LITERATURE = PROHIBITED
WEB_RESEARCH = PROHIBITED
NEW_CLAIMS = PROHIBITED
ARTICLE_MASTER_V010_PROMOTION = PROHIBITED
AUTHOR_APPROVAL_SELF_GRANT = PROHIBITED
FROZEN_OR_INTEGRATED_SELF_GRANT = PROHIBITED
MANUAL_BASE64 = PROHIBITED
FRAGMENTATION_OR_CHUNKING = PROHIBITED
```

## 6. Entregables

Genera exactamente:

1. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md` — artefacto acumulativo local exacto para handoff al autor;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx` — artefacto acumulativo local exacto para handoff al autor;
3. `article/responses/5_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT_RESPONSE_V01.md` — respuesta pequeña versionada directamente en GitHub.

No es necesario crear una nueva versión de `article/sections/experimental_design/Experimental_Design_B01_V02.md`, porque la prosa científica B01 no debe cambiar en esta ejecución.

## 7. Verificación diferencial obligatoria

Antes de entregar, demuestra en la respuesta GitHub:

- hashes SHA-256 de MD y DOCX de entrada y salida;
- que 3.5/3.7 y 4.1–4.2.3 permanecen textualmente inalterados;
- que la única modificación Markdown fuera del placeholder español corresponde al reemplazo del esqueleto no redactado 4.3+ en Part I/Part II;
- que desaparecieron 4.9, 4.10, 4.11 y 4.3.1–4.3.4;
- que existen 4.6.1, 4.6.2 y 4.6.3 en ambos idiomas;
- que el placeholder residual entre `4. Diseño experimental` y `4.1` ya no existe;
- que no se introdujo prosa científica nueva en 4.3–4.8;
- que Section 5 y posteriores permanecen inalteradas;
- 40 comentarios finales;
- 40 `commentRangeStart`, 40 `commentRangeEnd`, 40 `commentReference`;
- `comments.xml` SHA-256 exactamente `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`;
- cero tracked changes;
- render completo del DOCX y revisión visual de todas las páginas;
- ausencia de clipping, overlap, glifos faltantes o defectos de layout.

Si una modificación distinta de las autorizadas resulta necesaria, detente y no la apliques. Registra:

`B01_V03_STRUCTURE_ALIGNMENT_UNEXPECTED_CHANGE_REQUIRED`

## 8. Handoff D-035

Los dos masters acumulativos son artefactos grandes. Entrégalos como archivos exactos descargables en el chat. No intentes su transferencia directa a GitHub como workaround.

La respuesta pequeña sí debe quedar en GitHub. El chat final debe limitarse a:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/5_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT_RESPONSE_V01.md@<commit_sha>`

más los dos adjuntos exactos:

- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md`
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx`

No declares B01 aprobado, cerrado, congelado o integrado. Después del handoff, detente.