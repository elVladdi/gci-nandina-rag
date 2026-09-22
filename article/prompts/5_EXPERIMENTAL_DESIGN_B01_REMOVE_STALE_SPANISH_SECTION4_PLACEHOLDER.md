# Experimental Design B01 — Corrección técnica única del placeholder residual

## Español

### 1. Identidad

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_CORRECTION
PARENT_BLOCK = EXPERIMENTAL_DESIGN_B01
GOVERNING_DECISION = article/governance/D041_EXPERIMENTAL_DESIGN_B01_OPENING.md
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_INTERNAL_REVIEW_V01.md@d1e78932cbc2eebc0b0594a418661e6a599ee567
SOURCE_SECTION_MD = article/sections/experimental_design/Experimental_Design_B01_V01.md
SOURCE_SECTION_MD_SHA256 = fe80017f26010c4125b3abaec41ce066d91b63e1ff5ca54fa98baea0bea90e78
SOURCE_SECTION_MD_GIT_BLOB = b876bef94d75c0c8c676f5a4fa3276cbb22fbd28
SOURCE_MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.md
SOURCE_MASTER_CANDIDATE_MD_SHA256 = 6e443353c362410ffe70c880b49647a12b1a88d3ec72a12675cce5e086435754
SOURCE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.docx
SOURCE_CANDIDATE_DOCX_SHA256 = 4089ca75267ed05d1406b9bf2c1f895300f4da77ccb3e0559b2ef43ad49f3e5c
INHERITED_COMMENT_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
SCIENTIFIC_REDRAFT = PROHIBITED
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN_B02 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Ejecuta exclusivamente esta corrección técnica. No avances a ningún bloque posterior.

### 2. Control de precedencia de gobernanza

Esta instrucción respeta y no sustituye D-021, D-022, D-023, D-027, D-035 y D-041.

En particular:

- conserva el DOCX acumulativo exacto y sus comentarios;
- la respuesta operacional pequeña se versiona en GitHub;
- los artefactos acumulativos grandes se entregan al autor como adjuntos exactos;
- no se usa Base64 manual, fragmentación, chunking, recomposición, archivos auxiliares, ramas temporales ni reintentos de una vía grande que ya produjo timeout;
- la codificación interna automática de una API/conector no constituye Base64 manual;
- no se reabre la revisión científica que ya obtuvo `PASS` en la auditoría de la IA Gestora.

Si cualquier instrucción posterior parece exigir una operación incompatible con estas decisiones, detente con `EXPDES_B01_CORRECTION_GOVERNANCE_CONFLICT`.

### 3. Entradas exactas obligatorias

Debes recibir del autor y verificar antes de modificar:

1. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.md`
   - SHA-256 obligatorio: `6e443353c362410ffe70c880b49647a12b1a88d3ec72a12675cce5e086435754`.
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.docx`
   - SHA-256 obligatorio: `4089ca75267ed05d1406b9bf2c1f895300f4da77ccb3e0559b2ef43ad49f3e5c`.

Si falta cualquiera de los dos archivos o algún hash no coincide, detente con:

`EXPDES_B01_CORRECTION_SOURCE_MISMATCH`.

No reconstruyas ninguno desde GitHub, desde el otro formato ni desde `ARTICLE_MASTER_V009.md`.

### 4. Corrección única autorizada

En **Part II — Spanish semantic-control mirror**, localiza esta secuencia exacta:

```text
# 4. Diseño experimental

A partir de aquí se introduce la instanciación empírica concreta.

[Section text to be drafted in a later approved version.]

## 4.1. Entorno de evaluación
```

Elimina **únicamente** la línea:

```text
[Section text to be drafted in a later approved version.]
```

que aparece entre la nota introductoria de `4. Diseño experimental` y `4.1. Entorno de evaluación`.

Después de la corrección, debe quedar:

```text
# 4. Diseño experimental

A partir de aquí se introduce la instanciación empírica concreta.

## 4.1. Entorno de evaluación
```

No elimines ningún placeholder de 4.3 o subsecciones posteriores. No elimines instrucciones estructurales fuera de esta ubicación.

### 5. Contenido que debe permanecer byte/semánticamente inalterado

No modifiques:

- `article/sections/experimental_design/Experimental_Design_B01_V01.md`;
- Introduction;
- Related Work;
- Section 3.1–3.7;
- la prosa inglesa de 4.1–4.2.4;
- la prosa española de 4.1–4.2.4;
- ningún número, ruta, hash, nombre de dataset, término o afirmación científica;
- Section 4.3 y posteriores;
- Results, Discussion, Conclusion o front matter;
- comentarios heredados.

La corrección no autoriza mejorar estilo, terminología, traducción, cifras ni redacción. Cualquier cambio distinto de la eliminación exacta indicada es un fallo.

### 6. Artefactos finales

Genera localmente:

1. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md`
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx`

No crees `Experimental_Design_B01_V02.md`: el archivo de sección V01 permanece científicamente válido y no cambia.

Versiona directamente en GitHub **solo**:

`article/responses/5_EXPERIMENTAL_DESIGN_B01_CORRECTION_RESPONSE_V01.md`

No transfieras el master Markdown acumulativo grande a GitHub en esta ejecución.

### 7. QA obligatorio

#### Markdown

Verifica diferencialmente V01→V02:

- exactamente una eliminación textual;
- la eliminación es el placeholder español autorizado;
- ninguna otra línea cambia;
- 4.3 y posteriores permanecen exactos.

Calcula SHA-256 del V02 final.

#### DOCX / OOXML

Verifica:

- OOXML íntegro;
- 40 comentarios finales;
- `word/comments.xml` SHA-256 exactamente `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`;
- 0 tracked changes;
- comparación V01→V02: únicamente desaparece el placeholder español autorizado;
- ningún texto científico de B01 cambia.

Renderiza el DOCX completo y revisa visualmente **todas** las páginas. Registra el número real de páginas. No declares `FULL_RENDER_QA = PASS` sin inspección completa.

### 8. Handoff timeout-safe

Entrega al autor como archivos descargables exactos:

- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md`;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx`.

Calcula y registra SHA-256 de ambos.

No pegues su contenido en chat. No uses Base64 manual ni fragmentación.

### 9. Respuesta operacional requerida

La respuesta versionada debe registrar como mínimo:

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
RENDERED_PAGE_COUNT = <actual>
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md
MASTER_CANDIDATE_MD_SHA256 = <actual>
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx
CANDIDATE_DOCX_SHA256 = <actual>
DIRECT_LARGE_MASTER_GITHUB_TRANSFER = NOT_ATTEMPTED / D035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
EXPERIMENTAL_DESIGN_B02 = NOT_STARTED
RESULTS = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 10. Estados que no puedes autoasignar

No declares `APPROVED`, `FROZEN`, `INTEGRATED` ni `CANONICAL`. La IA Gestora verificará los artefactos corregidos y decidirá si abre el gate de aprobación autoral.

### 11. Mensaje terminal en chat

Conforme a D-022, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/5_EXPERIMENTAL_DESIGN_B01_CORRECTION_RESPONSE_V01.md@<commit_sha>`

y adjunta los dos artefactos V02 exactos como archivos descargables. No repitas hashes, QA ni hallazgos en chat.

---

## English

Execute only the single technical correction authorized by the Managing-AI review. Use the exact handed-off V01 cumulative Markdown and DOCX identified above. Delete only the stale generic Spanish Section-4 placeholder located between the Spanish Section-4 introductory note and `4.1. Entorno de evaluación`.

Do not revise scientific prose, the GitHub section artifact, Sections 4.1–4.2.4, Section 4.3 or later content, prior approved sections, results, terminology, figures, numbers, paths, or hashes. Preserve all 40 comments, the exact inherited `comments.xml`, and zero tracked changes.

Produce `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md` and `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx`, perform an exact one-deletion differential check, complete OOXML QA and full-page visual rendering review, and hand both exact artifacts to the author under D-035. Version only the small operational response in GitHub. Do not promote V010 or start Experimental Design B02.