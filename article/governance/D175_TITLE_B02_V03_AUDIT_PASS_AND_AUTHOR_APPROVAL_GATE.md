# D-175 — Title B02 V03 audit PASS and author approval gate

## Español

```text
DECISION = D-175
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE_V03

SOURCE_RESPONSE = article/responses/10_FRONT_MATTER_B02_TITLE_RESPONSE_V03.md@9cb2bf091138959ec27da4b6204e0506cd332d93
SOURCE_RESPONSE_GIT_BLOB = c2eed28f7a6ea9961c30eaa950b19cfc79b129d7

SECTION_ARTIFACT = article/sections/front_matter/Title_B02_V03.md@37b733114c7b43008323acdcab790775d09a78f5
SECTION_ARTIFACT_GIT_BLOB = 9b3fedd395664537d846dee3dd36061b8e4b9755

INTERNAL_REVIEW = article/reviews/10_FRONT_MATTER_B02_TITLE_INTERNAL_REVIEW_V03.md@7a0b0ffe8d6e3b905abb72642d41414ffcffd337
INTERNAL_REVIEW_GIT_BLOB = 672edc20d6eb9c0300485a3721315cba0b3bcdfd
INTERNAL_REVIEW_RESULT = PASS
MANDATORY_CORRECTIONS = NONE

CANONICAL_MASTER_BEFORE_APPROVAL = ARTICLE_MASTER_V032

TITLE_EN =
Knowledge-Based Decision-Support Architecture for Tariff Classification: Separating Candidate Ranking, Documentary Evidence, and Explanation

TITLE_ES =
Arquitectura basada en conocimiento para el apoyo a la decisión en clasificación arancelaria: separación del ranking de candidatos, la evidencia documental y la explicación

TITLE_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_TITLE_B02_V03.md
TITLE_CANDIDATE_MD_SHA256 = bf90c8b10891d401aa34f7553248f30578c1e4b98bef0bcbf32ec1da4446c9f1
TITLE_CANDIDATE_MD_EXPECTED_GIT_BLOB = 9b87c71290126f5223c6e4a252f95b5d64f71f49
TITLE_CANDIDATE_MD_SIZE_BYTES = 277830

TITLE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_TITLE_B02_V03.docx
TITLE_CANDIDATE_DOCX_SHA256 = 1451c7c2d9a013603c749a7ad0730ea450f76700ff853b6d96d9d1f865882ed1
TITLE_CANDIDATE_DOCX_SIZE_BYTES = 110921
TITLE_CANDIDATE_DOCX_COMMENTS = 48
TITLE_CANDIDATE_DOCX_TRACKED_CHANGES = 0
TITLE_CANDIDATE_DOCX_PAGE_COUNT = 71

MARKDOWN_DIFFERENTIAL = PASS / TITLE_EN + TITLE_ES ONLY
DOCX_OOXML_DIFFERENTIAL = PASS / word/document.xml ONLY
COMMENTS_XML_BYTE_IDENTICAL = PASS
COMMENTS_AND_ANCHORS_PRESERVED = PASS
FULL_DOCX_RENDER = PASS
FULL_DOCX_VISUAL_QA = PASS

KBS_CORPUS_EDITORIAL_FIT = PASS
KBS_FIRST_READ_IDENTITY = PASS
SCIENTIFIC_EDITORIAL_AUDIT = PASS

AUTHOR_APPROVAL_GATE = OPEN
AUTHOR_DECISION = PENDING

CANONICAL_PROMOTION = NOT_AUTHORIZED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V033
TARGET_MASTER_EXPECTED_GIT_BLOB_IF_APPROVED = 9b87c71290126f5223c6e4a252f95b5d64f71f49

KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisión

IA Gestora acepta el candidato Title B02 V03 después de auditoría editorial KBS, científica, Markdown, DOCX/OOXML y visual completa.

No existen correcciones obligatorias.

V03 resuelve las dos debilidades editoriales sucesivamente identificadas en V01/V02:

1. sustituye la formulación abstracta `Auditable / Authority Separation` por la operación metodológica concreta;
2. hace reconocible desde la primera lectura el tipo de contribución y su identidad científica KBS mediante `Knowledge-Based Decision-Support Architecture`.

El título mantiene explícito el dominio `Tariff Classification` y la operación distintiva:

```text
candidate ranking
+
documentary evidence
+
explanation
```

La auditoría técnica confirma que solo Title/Título cambiaron respecto de V032. El DOCX conserva 14 partes OOXML, 48 comentarios y anclajes, cero tracked changes y 71 páginas.

Se abre exclusivamente el gate de aprobación del autor para este candidato exacto.

### Regla de aprobación

Si el autor aprueba explícitamente:

1. el único Markdown elegible para promoción es el candidato con SHA-256 `bf90c8b10891d401aa34f7553248f30578c1e4b98bef0bcbf32ec1da4446c9f1`;
2. debe materializarse como `article/manuscript/ARTICLE_MASTER_V033.md`;
3. su Git blob debe ser exactamente `9b87c71290126f5223c6e4a252f95b5d64f71f49`;
4. el Word canónico acumulativo pasa a ser el candidato DOCX exacto con SHA-256 `1451c7c2d9a013603c749a7ad0730ea450f76700ff853b6d96d9d1f865882ed1`, bajo custodia local del autor;
5. IA Gestora debe verificar la promoción antes de declarar Title/Título cerrado/integrado o abrir Keywords.

No se autoriza promoción automática.

### Gate

```text
CURRENT_GATE = FRONT_MATTER_B02_TITLE_V03_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_EXACT_TITLE_B02_V03_CANDIDATE
AUTHOR_APPROVAL_GATE = OPEN
AUTHOR_DECISION = PENDING

CANONICAL_MASTER = ARTICLE_MASTER_V032
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V033

KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```

---

## English

D-175 records an independent PASS for the exact Final Title B02 V03 cumulative Markdown and DOCX candidates and opens only the explicit author-approval gate.

V03 is the first title candidate that passes all three editorial layers applied in sequence: title-to-paper fidelity, accepted-KBS-corpus fit, and first-read KBS scientific identity.

The title identifies the contribution as a knowledge-based decision-support architecture, the application task as tariff classification, and the concrete methodological operation as separation of candidate ranking, documentary evidence, and explanation.

No canonical promotion occurs until explicit author approval. If approved, only the exact candidate Markdown identified above may be promoted as ARTICLE_MASTER_V033 and must match the expected Git blob. Keywords and end matter remain unauthorized.
