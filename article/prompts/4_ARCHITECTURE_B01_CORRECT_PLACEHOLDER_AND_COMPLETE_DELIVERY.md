# Architecture B01 — Minor structural correction and completion of GitHub delivery

## Español

### 1. Identidad y objetivo único

```text
BLOCK = ARCHITECTURE_B01_CORRECTION_AND_DELIVERY
PARENT_BLOCK = ARCHITECTURE_B01
STATUS_AT_ENTRY = PASS_WITH_CORRECTIONS / DELIVERY_BLOCKED
GOVERNING_REVIEW = article/reviews/4_ARCHITECTURE_B01_INTERNAL_REVIEW_V01.md@c222fc9c887cef8808612e357266ccb609d66ba8
PRIOR_RESPONSE = article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md@688b83bf352ceb89ac41ca4147162e4afb0a640c
SOURCE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.docx
SOURCE_CANDIDATE_DOCX_SHA256 = 485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53
EXPECTED_INHERITED_COMMENTS = 40
SCIENTIFIC_REDRAFT = PROHIBITED
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
ARTICLE_MASTER_V008 = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Ejecuta **exclusivamente** la corrección estructural menor y la entrega GitHub incompleta de Architecture B01. No reabras el contenido científico de 3.1–3.4 y no avances a ningún bloque posterior.

### 2. Rol

Actúa como **IA de Redacción científica en modo de corrección/entrega controlada**. No actúes como IA Gestora ni Experimental. No cambies decisiones, gates, claims, el Plan Maestro experimental, `ARTICLE_STATUS`, `ARTICLE_WRITING_PLAN` ni governance.

Esta ejecución no es una segunda redacción de B01. El contenido científico de 3.1–3.4 ya fue auditado como sustancialmente correcto. Tu trabajo consiste únicamente en:

1. eliminar un placeholder estructural obsoleto en Part II;
2. regenerar el binario candidato con esa única corrección;
3. completar la entrega exacta de los dos Markdown científicos que no se versionaron en V01;
4. registrar la operación en una respuesta V02.

### 3. Input binario obligatorio

Trabaja exclusivamente sobre el DOCX candidato entregado al autor:

`ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.docx`

SHA-256 obligatorio:

`485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53`

El autor debe proporcionarte ese binario exacto. Verifica el hash antes de cualquier edición.

Si el archivo no está disponible o el SHA-256 no coincide, detente con:

`ARCHITECTURE_B01_CORRECTION_SOURCE_MISMATCH`

No reconstruyas el DOCX desde Markdown, desde `ARTICLE_MASTER_V007.md`, desde la respuesta V01 ni desde memoria.

### 4. Corrección única autorizada en el DOCX

En **Part II — Spanish semantic-control mirror**, localiza exactamente esta secuencia:

```text
3. Arquitectura de apoyo a decisiones
Describir primero la arquitectura general. No abrir esta sección con NANDINA, Capítulo 87, corpus peruano, H100 ni tamaños del experimento.
[Section text to be drafted in a later approved version.]
3.1. Vista general y flujo de información
```

Elimina **únicamente** la línea:

`[Section text to be drafted in a later approved version.]`

que se encuentra entre la nota interna de Section 3 y `3.1. Vista general y flujo de información`.

No elimines:

- la nota interna bajo `3. Arquitectura de apoyo a decisiones`;
- el placeholder de Figure 1;
- los placeholders o instrucciones de 3.5, 3.6 y 3.7;
- ningún placeholder de secciones posteriores.

No alteres una sola palabra de los párrafos científicos de 3.1–3.4 en inglés o español.

No introduzcas citas nuevas.

### 5. Contenido científico que debe permanecer exactamente estable

Conserva sin reescritura:

- 3.1: query normalizada → recuperación histórica → ranking → Top-3 fijo antes de downstream;
- 3.2: interfaz de consulta reproducible separada de detalles de instanciación experimental;
- 3.3: ranking de registros históricos, deduplicación por código, retención del precedente mejor posicionado y ranking Top-k de códigos únicos; BM25 solo como instanciación experimental;
- 3.4: tres primeros códigos únicos = Top-3 fijo; membresía y orden inmutables en el flujo principal; etapas downstream solo enriquecen/explican;
- reranking LLM diagnóstico fuera del flujo principal;
- ausencia de resultados, métricas, H100, tamaños de dataset, novelty o legal correctness.

No conviertas esta ejecución en una oportunidad de mejora estilística adicional.

### 6. Preservación del DOCX

El DOCX corregido debe conservar:

- todo Introduction aprobado;
- Related Work 2.1–2.6 aprobado;
- los 40 comentarios heredados y sus anclajes;
- `word/comments.xml` byte-identical al candidato V01, con SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`;
- 0 tracked changes;
- 3.5–3.7 y todas las secciones posteriores sin modificaciones;
- Figure 1 solo como placeholder; no generar figura.

Guarda el nuevo binario como:

`ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`

Calcula y registra su nuevo SHA-256.

Antes del handoff:

1. verifica integridad OOXML;
2. verifica comentarios/anclajes;
3. verifica 0 tracked changes;
4. compara el DOCX V01 y V02 y confirma que la única modificación textual sea la eliminación autorizada;
5. renderiza el documento completo;
6. inspecciona visualmente todas las páginas;
7. entrega efectivamente el DOCX V02 al autor conforme a D-027.

### 7. Artefactos Markdown a versionar

La entrega científica V01 no llegó a GitHub. En esta ejecución debes crear y versionar:

1. `article/sections/architecture/Architecture_B01_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md`
3. `article/responses/4_ARCHITECTURE_B01_RESPONSE_V02.md`

#### 7.1. Architecture_B01_V01.md

Debe contener únicamente la versión científica auditada de Architecture B01 — 3.1–3.4 — en Part I English y Part II Spanish semantic-control mirror, sin reescritura respecto del DOCX corregido.

No incluyas Results, métricas ni texto de 3.5–3.7.

#### 7.2. ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md

Debe ser el master acumulativo candidato, basado en el contenido canónico de `ARTICLE_MASTER_V007.md` blob `436e0522db0ac348efaed86f4e53a7e6db372471`, incorporando exclusivamente B01 y la eliminación del placeholder español autorizada por esta corrección.

Debe preservar exactamente Introduction, Related Work y todo contenido posterior no autorizado.

El nombre V02 corresponde a la corrección estructural del candidato; **no** promueve `ARTICLE_MASTER_V008`.

### 8. Transferencia exacta a GitHub — aclaración operativa

El bloqueo de V01 no debe repetirse por una interpretación excesivamente restrictiva del conector.

El procedimiento autorizado es:

1. genera el Markdown UTF-8 local final;
2. calcula su SHA-256 local;
3. lee su contenido textual completo desde el archivo local verificado;
4. transfiere ese contenido **literalmente** mediante el campo de contenido textual de la operación GitHub correspondiente;
5. vuelve a leer desde GitHub el archivo versionado;
6. verifica igualdad textual exacta con el archivo local y registra el blob Git resultante.

La transferencia literal de un archivo local verificado al campo textual del conector **no constituye reconstrucción científica manual**, porque no se está reescribiendo, resumiendo ni reinterpretando su contenido.

Si el contenido excede una limitación real de la herramienta, no sustituyas el archivo por fragmentos incompletos ni placeholders. Registra el error concreto. Sin embargo, no declares un bloqueo únicamente porque la API recibe texto: precisamente esa es la vía autorizada de transferencia.

### 9. Commit permitido

El commit de esta ejecución debe añadir/modificar **únicamente**:

- `article/sections/architecture/Architecture_B01_V01.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md`;
- `article/responses/4_ARCHITECTURE_B01_RESPONSE_V02.md`.

No modifiques:

- `ARTICLE_STATUS.md`;
- `ARTICLE_WRITING_PLAN.md`;
- `DECISIONS.md`;
- `SOURCE_REGISTRY.md`;
- `CLAIM_EVIDENCE_MATRIX.md`;
- governance;
- `ARTICLE_MASTER_V007.md`;
- prompts anteriores;
- Results/Discussion;
- archivos experimentales.

No subas el DOCX a GitHub.

### 10. QA obligatorio de la respuesta V02

La respuesta debe registrar como mínimo:

```text
BLOCK = ARCHITECTURE_B01_CORRECTION_AND_DELIVERY
SOURCE_CANDIDATE_DOCX_SHA256 = 485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53 / PASS
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
STALE_SPANISH_SECTION3_PLACEHOLDER_REMOVED = PASS
B01_SCIENTIFIC_PROSE_CHANGED = NO
INTRODUCTION_MODIFIED = NO
RELATED_WORK_MODIFIED = NO
SECTIONS_3_5_TO_3_7_MODIFIED = NO
LATER_SECTIONS_MODIFIED = NO
NEW_BIBLIOGRAPHIC_CITATIONS = 0
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = <actual>
SECTION_MD_PATH = article/sections/architecture/Architecture_B01_V01.md
SECTION_MD_SHA256 = <actual>
SECTION_MD_GITHUB_BLOB = <actual>
MASTER_CANDIDATE_MD_PATH = article/manuscript/ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md
MASTER_CANDIDATE_MD_SHA256 = <actual>
MASTER_CANDIDATE_MD_GITHUB_BLOB = <actual>
LOCAL_TO_GITHUB_TEXT_EQUALITY = PASS
CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx
CANDIDATE_DOCX_SHA256 = <actual>
AUTHOR_HANDOFF_DOCX = COMPLETED
GITHUB_SEMANTIC_DELIVERY = COMPLETE
ARTICLE_MASTER_V008 = NOT_PROMOTED
ARCHITECTURE_B02 = NOT_STARTED
EXPERIMENTAL_DESIGN = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No declares `APPROVED`, `FROZEN`, `INTEGRATED` ni abras el siguiente gate. Esos estados corresponden a la auditoría posterior de la IA Gestora y a la aprobación expresa del autor.

### 11. Respuesta en chat

Después de completar el commit y el handoff efectivo del DOCX, responde en chat únicamente con:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/4_ARCHITECTURE_B01_RESPONSE_V02.md@<commit_sha>`

y el archivo descargable `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`.

---

## English

### 1. Single objective

Execute only the controlled minor structural correction and complete the missing GitHub delivery for Architecture B01. Do not redraft Sections 3.1–3.4 and do not advance to later blocks.

```text
PARENT_BLOCK = ARCHITECTURE_B01
GOVERNING_REVIEW = article/reviews/4_ARCHITECTURE_B01_INTERNAL_REVIEW_V01.md@c222fc9c887cef8808612e357266ccb609d66ba8
SOURCE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.docx
SOURCE_CANDIDATE_DOCX_SHA256 = 485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53
SCIENTIFIC_REDRAFT = PROHIBITED
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
ARTICLE_MASTER_V008 = NOT_AUTHORIZED
```

Use only the exact V01 candidate DOCX supplied by the author. Stop on hash mismatch; do not reconstruct the DOCX from Markdown.

### 2. Authorized correction

In Part II, remove only the stale generic line:

`[Section text to be drafted in a later approved version.]`

located between the Section 3 internal drafting note and `3.1. Vista general y flujo de información`.

Keep the Section 3 note, Figure 1 placeholder, Sections 3.5–3.7 placeholders, later placeholders, all scientific B01 prose, and all prior approved content unchanged.

### 3. DOCX QA and handoff

Create `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`; preserve all 40 comments and byte-identical `comments.xml`, keep zero tracked changes, verify that the V01→V02 textual delta contains only the authorized deletion, render the full document, inspect every page, calculate the new SHA-256, and hand the exact binary to the author under D-027.

### 4. Required GitHub artifacts

Version exactly:

- `article/sections/architecture/Architecture_B01_V01.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md`;
- `article/responses/4_ARCHITECTURE_B01_RESPONSE_V02.md`.

The section Markdown preserves the already audited B01 scientific prose. The cumulative V02 Markdown is based on canonical `ARTICLE_MASTER_V007.md` blob `436e0522db0ac348efaed86f4e53a7e6db372471` and incorporates only B01 plus the authorized Spanish placeholder deletion. V02 is a candidate version and does not promote V008.

### 5. Exact textual transfer

Generating a verified local UTF-8 Markdown file, reading its complete contents, passing those contents literally through the GitHub connector's text-content field, and verifying exact equality after fetching the committed file is an authorized transfer procedure. It is not a scientific rewrite or unsafe reconstruction.

Do not commit partial files, fragments, or placeholders. Record the local SHA-256 and resulting Git blob for each Markdown artifact and verify local-to-GitHub text equality.

### 6. Scope and state

Do not modify status, writing plan, decisions, governance, claims, source registry, canonical V007, experimental files, Results, or Discussion. Do not start B02 or Experimental design. Do not self-declare approval, freeze, integration, final gap, or novelty.

After successful commit and DOCX handoff, the chat response must contain only the V02 response pointer and the downloadable corrected DOCX.