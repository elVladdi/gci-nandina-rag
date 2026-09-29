# D-181 — Keywords B03 V01 audit PASS and author approval gate

## Español

```text
DECISION = D-181
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B03_KEYWORDS_V01

SOURCE_RESPONSE =
article/responses/11_FRONT_MATTER_B03_KEYWORDS_RESPONSE_V01.md@3cf55d18aa03057bd43f3153519ad9736cfc2f07
SOURCE_RESPONSE_GIT_BLOB =
f649553e5a392f94240939a4626f7c8a707f7347

SECTION_ARTIFACT =
article/sections/front_matter/Keywords_B03_V01.md@cdd23a2296ab6b1435d660f7340bcf73a9c340cb
SECTION_ARTIFACT_GIT_BLOB =
fc4a2b98b27e3bf38d962b6fb7da76887d717e47

INTERNAL_REVIEW =
article/reviews/11_FRONT_MATTER_B03_KEYWORDS_INTERNAL_REVIEW_V01.md@62261518ea4aced0bf1d4c17efa7c410daf50377
INTERNAL_REVIEW_GIT_BLOB =
cf20a8f1d134b8df1da4581dcc0db1b8c7f3df27
INTERNAL_REVIEW_RESULT = PASS
MANDATORY_CORRECTIONS = NONE

CANONICAL_MASTER_BEFORE_APPROVAL = ARTICLE_MASTER_V033

KEYWORDS_EN =
Knowledge-based decision support; Tariff classification; Harmonized System; Information retrieval; Documentary evidence; Large language models; Provenance and traceability

KEYWORDS_ES =
Apoyo a la decisión basado en conocimiento; Clasificación arancelaria; Sistema Armonizado; Recuperación de información; Evidencia documental; Modelos de lenguaje grandes; Procedencia y trazabilidad

KEYWORDS_CANDIDATE_MD =
ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V01.md
KEYWORDS_CANDIDATE_MD_SHA256 =
37994390a1be96d6c37bceb6536ea367b0918872b63180e2f5531ba32856f6ca
KEYWORDS_CANDIDATE_MD_EXPECTED_GIT_BLOB =
0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684
KEYWORDS_CANDIDATE_MD_SIZE_BYTES = 277983

KEYWORDS_CANDIDATE_DOCX =
ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V01.docx
KEYWORDS_CANDIDATE_DOCX_SHA256 =
8e31acd688e0e7b52a8f132ed12f342178c75daf9bfe1dbb4d8c44137f317b84
KEYWORDS_CANDIDATE_DOCX_SIZE_BYTES = 110943
KEYWORDS_CANDIDATE_DOCX_COMMENTS = 48
KEYWORDS_CANDIDATE_DOCX_TRACKED_CHANGES = 0
KEYWORDS_CANDIDATE_DOCX_PAGE_COUNT = 71

MARKDOWN_DIFFERENTIAL = PASS / KEYWORDS_EN + KEYWORDS_ES ONLY
DOCX_OOXML_DIFFERENTIAL = PASS / word/document.xml ONLY
COMMENTS_XML_BYTE_IDENTICAL = PASS
COMMENTS_AND_ANCHORS_PRESERVED = PASS
FULL_DOCX_RENDER = PASS
FULL_DOCX_VISUAL_QA = PASS

KBS_EDITORIAL_FIT = PASS
SCIENTIFIC_SCOPE = PASS
CLAIM_CALIBRATION = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS

AUTHOR_APPROVAL_GATE = OPEN
AUTHOR_DECISION = PENDING

CANONICAL_PROMOTION = NOT_AUTHORIZED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V034
TARGET_MASTER_EXPECTED_GIT_BLOB_IF_APPROVED =
0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684

END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisión

IA Gestora acepta el candidato Keywords B03 V01 después de auditoría editorial, científica, Markdown, DOCX/OOXML y visual completa.

No existen correcciones obligatorias.

La selección de siete Keywords / Palabras clave:

- cubre la identidad knowledge-based del sistema;
- identifica el dominio de clasificación arancelaria;
- incorpora vocabulario buscable del Harmonized System;
- representa retrieval, evidencia documental, LLM y provenance/traceability;
- evita reducir el trabajo a NANDINA/Chapter 87/Peru;
- evita términos que exceden la evidencia como auditability, Explainable AI, legal correctness o human validation.

Se abre exclusivamente el gate de aprobación del autor para este candidato exacto.

### Regla de aprobación

Si el autor aprueba explícitamente:

1. el único Markdown elegible para promoción es el candidato con SHA-256 `37994390a1be96d6c37bceb6536ea367b0918872b63180e2f5531ba32856f6ca`;
2. debe materializarse como `article/manuscript/ARTICLE_MASTER_V034.md`;
3. su Git blob debe ser exactamente `0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684`;
4. el Word canónico acumulativo pasa a ser el candidato DOCX exacto con SHA-256 `8e31acd688e0e7b52a8f132ed12f342178c75daf9bfe1dbb4d8c44137f317b84`, bajo custodia local del autor;
5. IA Gestora debe verificar la promoción antes de declarar Keywords cerrado/integrado o abrir End Matter.

No se autoriza promoción automática.

### Gate

```text
CURRENT_GATE = FRONT_MATTER_B03_KEYWORDS_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_EXACT_KEYWORDS_B03_V01_CANDIDATE
AUTHOR_APPROVAL_GATE = OPEN
AUTHOR_DECISION = PENDING

CANONICAL_MASTER = ARTICLE_MASTER_V033
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V034

TITLE = CLOSED / APPROVED / FROZEN / INTEGRATED
ABSTRACT = CLOSED / APPROVED / FROZEN / INTEGRATED
KEYWORDS = COMPLETED / AUDITED_PASS / PENDING_AUTHOR_APPROVAL

END_MATTER_FINALIZATION = NOT_AUTHORIZED
```

---

## English

D-181 records an independent PASS for the exact Keywords B03 V01 cumulative Markdown and DOCX candidates and opens only the explicit author-approval gate.

The seven English/Spanish keywords pass editorial fit, scientific scope, claim calibration, bilingual equivalence, Markdown differential, OOXML integrity, comment/anchor preservation, and full visual QA.

No canonical promotion occurs until explicit author approval. If approved, only the exact candidate Markdown identified above may be promoted as ARTICLE_MASTER_V034 and must match the expected Git blob. End matter remains unauthorized until that promotion is verified.
