# Architecture B01 — Timeout-safe correction and exact artifact handoff

## 1. Identidad y objetivo único

```text
BLOCK = ARCHITECTURE_B01_TIMEOUT_SAFE_RECOVERY
PARENT_BLOCK = ARCHITECTURE_B01
GOVERNING_REVIEW = article/reviews/4_ARCHITECTURE_B01_INTERNAL_REVIEW_V01.md@c222fc9c887cef8808612e357266ccb609d66ba8
GOVERNING_DECISION = article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md@b5db5c0e9178c2a758c6572f2b6ec742b0da3563
SUPERSEDES_FOR_EXECUTION = article/prompts/4_ARCHITECTURE_B01_CORRECT_PLACEHOLDER_AND_COMPLETE_DELIVERY.md@6000972317488b5a0bb90a0ddc5fddb00a8e1731
SOURCE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.docx
SOURCE_CANDIDATE_DOCX_SHA256 = 485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53
SCIENTIFIC_REDRAFT = PROHIBITED
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
DIRECT_LARGE_MARKDOWN_GITHUB_TRANSFER = PROHIBITED_FOR_THIS_EXECUTION
MANUAL_BASE64 = PROHIBITED
FRAGMENTATION_OR_CHUNKING = PROHIBITED
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
ARTICLE_MASTER_V008 = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Ejecuta exclusivamente la corrección estructural menor de Architecture B01 y el handoff exacto de sus artefactos. **No intentes nuevamente transferir a GitHub los Markdown científicos grandes.** Ese intento ya produjo timeout y el mecanismo queda sustituido por D-035.

## 2. Input obligatorio

Trabaja exclusivamente sobre:

`ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.docx`

SHA-256 esperado:

`485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53`

Si no coincide, detente. No reconstruyas el DOCX.

## 3. Única corrección autorizada

En Part II elimina únicamente la línea genérica:

`[Section text to be drafted in a later approved version.]`

situada entre la nota interna de `3. Arquitectura de apoyo a decisiones` y `3.1. Vista general y flujo de información`.

No modifiques ninguna palabra de 3.1–3.4. No elimines el placeholder de Figure 1 ni los placeholders/instrucciones de 3.5–3.7 o posteriores. No agregues citas.

## 4. Artefactos locales finales

Genera/verifica exactamente:

1. `Architecture_B01_V01.md`
   - 3.1–3.4 auditadas, Part I English + Part II Spanish.
   - Sin reescritura científica.

2. `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md`
   - Master acumulativo candidato basado en `ARTICLE_MASTER_V007.md` e incorporando B01 y únicamente la eliminación autorizada del placeholder.
   - No constituye promoción de V008.

3. `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`
   - Derivado exclusivamente del DOCX V01 exacto mediante la corrección única autorizada.

Calcula SHA-256 de los tres archivos finales.

## 5. QA mínimo y suficiente

Para el DOCX V02 verifica:

- integridad OOXML;
- 40 comentarios y anclajes preservados;
- `word/comments.xml` SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`;
- 0 tracked changes;
- V01→V02: única modificación textual = eliminación del placeholder autorizado;
- render completo e inspección visual de todas las páginas.

No reabras revisión científica, bibliográfica o experimental.

## 6. Handoff timeout-safe obligatorio

Conforme a D-035:

- **NO** pegues el contenido completo de los Markdown en llamadas del conector GitHub;
- **NO** uses Base64 manual;
- **NO** fragmentes/chunkees los archivos;
- **NO** hagas reintentos de transferencia del master grande;
- **NO** crees blobs de prueba, archivos auxiliares, ramas temporales ni commits parciales de los Markdown científicos.

Entrega al autor como **archivos adjuntos descargables**, sin alterar bytes:

- `Architecture_B01_V01.md`;
- `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md`;
- `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`.

El autor trasladará esos tres archivos a la IA Gestora. La IA Gestora verificará los SHA-256 y completará la materialización GitHub de los Markdown.

## 7. Único archivo a versionar directamente en GitHub

Crea únicamente:

`article/responses/4_ARCHITECTURE_B01_TIMEOUT_SAFE_HANDOFF_RESPONSE_V01.md`

La respuesta debe ser breve y registrar:

```text
BLOCK = ARCHITECTURE_B01_TIMEOUT_SAFE_RECOVERY
SOURCE_CANDIDATE_DOCX_SHA256 = 485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53 / PASS
AUTHORIZED_TEXTUAL_CORRECTION_COUNT = 1
STALE_SPANISH_SECTION3_PLACEHOLDER_REMOVED = PASS
B01_SCIENTIFIC_PROSE_CHANGED = NO
INTRODUCTION_MODIFIED = NO
RELATED_WORK_MODIFIED = NO
SECTIONS_3_5_TO_3_7_MODIFIED = NO
LATER_SECTIONS_MODIFIED = NO
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = <actual>
SECTION_MD_FILENAME = Architecture_B01_V01.md
SECTION_MD_SHA256 = <actual>
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md
MASTER_CANDIDATE_MD_SHA256 = <actual>
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx
CANDIDATE_DOCX_SHA256 = <actual>
DIRECT_LARGE_MARKDOWN_GITHUB_TRANSFER = NOT_ATTEMPTED / D035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
EXACT_ARTIFACT_HANDOFF_TO_AUTHOR = PREPARED
GITHUB_SCIENTIFIC_MARKDOWN_MATERIALIZATION = DEFERRED_TO_IA_GESTORA
ARTICLE_MASTER_V008 = NOT_PROMOTED
ARCHITECTURE_B02 = NOT_STARTED
EXPERIMENTAL_DESIGN = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No modifiques ningún otro archivo GitHub.

## 8. Respuesta final en chat

Responde únicamente con:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/4_ARCHITECTURE_B01_TIMEOUT_SAFE_HANDOFF_RESPONSE_V01.md@<commit_sha>`

más los **tres archivos descargables** indicados en la sección 6.

No incluyas explicación sustantiva, hashes ni QA en el texto del chat; esos datos quedan en la respuesta versionada.
