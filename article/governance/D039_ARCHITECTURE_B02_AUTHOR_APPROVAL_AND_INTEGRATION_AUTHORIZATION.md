# D-039 — Architecture B02 author approval and integration authorization

## Estado

`ACTIVE / BINDING`

## Decisión

El autor aprueba expresamente Architecture B02, correspondiente a Sections 3.5–3.7 del artículo.

La aprobación autoral se emite después de la auditoría independiente registrada en:

`article/reviews/4_ARCHITECTURE_B02_INTERNAL_REVIEW_V01.md@484391d6136e5ed7ad82e77f1d98a21eef0289e8`

La auditoría concluyó:

```text
SCIENTIFIC_CONTENT_REVIEW = PASS
MARKDOWN_SCOPE_AND_PRESERVATION = PASS
DOCX_BINARY_AND_RENDER_QA = PASS
PRIOR_APPROVED_CONTENT_PRESERVATION = PASS
GITHUB_SECTION_DELIVERY = PASS
LARGE_ARTIFACT_HANDOFF = PASS
OVERALL_REVIEW = PASS
AUTHOR_APPROVAL_GATE = OPEN
```

## Artefactos aprobados

```text
SECTION_MD = article/sections/architecture/Architecture_B02_V01.md
SECTION_MD_SHA256 = 9dd820ed1db6ae723d5ddf9be5326da65476ea76f7480a0145c400f6864e6e75
SECTION_MD_GIT_BLOB = 779bf86580db953ed1375ec19c6057a4a6bd0a13

APPROVED_MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.md
APPROVED_MASTER_CANDIDATE_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
EXPECTED_ARTICLE_MASTER_V009_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2

APPROVED_MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
APPROVED_MASTER_CANDIDATE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CITATION_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
```

## Estados concedidos

A partir de esta decisión:

```text
ARCHITECTURE_B02 = AUTHOR_APPROVED / SCIENTIFICALLY_CLOSED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = AUTHOR_APPROVED / SCIENTIFICALLY_CLOSED
ARTICLE_MASTER_V009_PROMOTION = AUTHORIZED
```

La promoción técnica de `ARTICLE_MASTER_V009.md` debe materializar el Markdown aprobado exacto, sin reescritura, normalización ni reconstrucción semántica. Tras la materialización, la IA Gestora debe verificar SHA-256 y Git blob antes de declarar `INTEGRATED` y `CANONICAL`.

El DOCX aprobado pasa a ser el candidato de baseline para el siguiente bloque únicamente después de completar la integración técnica y registrar su identidad canónica bajo la política D-021/D-027/D-035.

## Restricción timeout-safe

D-035 continúa vigente. La aprobación no autoriza Base64 manual, fragmentación, chunking, recomposición ni reintentos de una vía de transferencia grande que ya haya demostrado timeout.

Si el conector disponible para la IA Gestora no admite cargar directamente el archivo local exacto y materializar el master requeriría volver a serializar manualmente el archivo grande por una vía prohibida o previamente fallida, la promoción técnica debe quedar temporalmente en `AUTHORIZED / PENDING_MATERIALIZATION` hasta que el binario textual exacto sea materializado por una vía segura. Ese bloqueo es técnico y no reabre la aprobación científica de B02.

## Siguiente gate

Experimental Design es elegible únicamente después de verificar la materialización de `ARTICLE_MASTER_V009.md` y actualizar el estado editorial correspondiente. La apertura del primer bloque de Experimental Design no requiere una segunda aprobación redundante del autor una vez satisfecho ese gate técnico; la IA Gestora debe continuar automáticamente conforme a la regla de continuidad operativa vigente.

## Estados no concedidos todavía

Esta decisión, por sí sola, no declara:

```text
ARTICLE_MASTER_V009 = CANONICAL
ARCHITECTURE_B02 = INTEGRATED
EXPERIMENTAL_DESIGN = AUTHORIZED
RESULTS = AUTHORIZED
FINAL_GAP = DEFINED
NOVELTY = DECLARED
```
