# D-192 — AI disclosure V02 author-singular correction approved and integrated as V036

## Español

```text
DECISION = D-192
PHASE = END_MATTER / AI_DISCLOSURE_FINALIZATION
BLOCK = END_MATTER_B02_GENERATIVE_AI_DECLARATION_V02

SOURCE_RESPONSE =
article/responses/12_END_MATTER_B02_GENERATIVE_AI_DECLARATION_RESPONSE_V02.md@4a5b4a4d7ceb5bebdc142e144e226313820cbd2e
SOURCE_RESPONSE_GIT_BLOB =
e8719e3a7ff3cd6048ad3355d54ad374c845d737

GESTORA_REVIEW =
article/reviews/12_END_MATTER_B02_GENERATIVE_AI_DECLARATION_INTERNAL_REVIEW_V02_C01.md@f5d77b0f9b323df0635ed707f903c167257ab3f5
GESTORA_REVIEW_GIT_BLOB =
46664f0e168549e8c2bdc87859efd919657d9959
GESTORA_REVIEW_RESULT = PASS

CORRECTED_SECTION =
article/sections/end_matter/Generative_AI_Declaration_V02_C01.md@3e96ff538c7b71519ade28afbec2d42524809535
CORRECTED_SECTION_GIT_BLOB =
e816396f01475fbbf1257247282ce6154f173906

AUTHOR_CORRECTION =
PLURAL_AUTHOR_REFERENCES -> SINGULAR_AUTHOR_REFERENCES
AUTHOR_CORRECTION_APPLIED = YES
AUTHOR_CONDITIONAL_APPROVAL = SATISFIED
AUTHOR_APPROVAL_GATE = CLOSED / APPROVED

CORRECTED_CANDIDATE_MD =
ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.md
CORRECTED_CANDIDATE_MD_SHA256 =
8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8
CORRECTED_CANDIDATE_MD_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90

CORRECTED_CANDIDATE_DOCX =
ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx
CORRECTED_CANDIDATE_DOCX_SHA256 =
d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d
CORRECTED_CANDIDATE_DOCX_SIZE_BYTES = 111524
CORRECTED_CANDIDATE_DOCX_COMMENTS = 48
CORRECTED_CANDIDATE_DOCX_TRACKED_CHANGES = 0
CORRECTED_CANDIDATE_DOCX_PAGE_COUNT = 72

PROMOTED_MASTER =
article/manuscript/ARTICLE_MASTER_V036.md
PROMOTION_COMMIT =
31875672f2f62b7a1259cd6684f8bb97a0c091be
PROMOTED_MASTER_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90
EXPECTED_PROMOTED_MASTER_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90
PROMOTION_VERIFICATION = PASS / BYTE_EXACT_BY_GIT_BLOB_IDENTITY

CANONICAL_MASTER = ARTICLE_MASTER_V036
CANONICAL_MASTER_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90
CANONICAL_MASTER_SHA256 =
8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8

CANONICAL_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 =
d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d

AI_DISCLOSURE_STATUS =
CLOSED / APPROVED / FROZEN / INTEGRATED

GESTORA_TASK_STATUS = FINALIZED
OTHER_END_MATTER = AUTHOR_OWNED
FINAL_SUBMISSION_ASSEMBLY = AUTHOR_OWNED
SUBMISSION_READY = NOT_ASSERTED
```

## 1. Auditoría de IA de Redacción

IA Gestora auditó la respuesta y los dos masters acumulativos entregados por IA de Redacción.

La ejecución V02 cumplió D-190/D-191 y materializó únicamente las cuatro inserciones autorizadas.

La única observación posterior fue declarativa y autoral: el manuscrito tiene un solo autor.

## 2. Corrección singular autorizada directamente por el Autor

El Autor instruyó expresamente que IA Gestora realizara directamente la corrección de número autoral y declaró que, con esa corrección, el candidato quedaba aprobado.

Se corrigieron exclusivamente los cuatro párrafos gobernados:

- Methods EN;
- final declaration EN;
- Methods ES;
- final declaration ES.

No se alteró el alcance sustantivo del uso de IA.

## 3. Auditoría técnica de la corrección

```text
MARKDOWN_CHANGED_LINES = 4
MARKDOWN_OTHER_CHANGES = 0

DOCX_CHANGED_PARAGRAPHS = 4
DOCX_OTHER_PARAGRAPH_CHANGES = 0

OOXML_PART_COUNT = 14
OOXML_CHANGED_PARTS = word/document.xml ONLY
COMMENTS_XML_BYTE_IDENTICAL = PASS
COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
TRACKED_CHANGES = 0

FULL_DOCX_PAGE_COUNT = 72
FULL_DOCX_RENDER = PASS
FULL_DOCX_VISUAL_QA = PASS
PAGES_REVIEWED = 1-72
AI_DISCLOSURE_PAGES_REVIEWED_AT_FULL_DETAIL = 24, 35, 60, 72
```

## 4. Texto final

### Methods EN

```text
OpenAI Codex was used as an AI-assisted software-development tool to support software implementation and code refinement. The author reviewed and edited the Codex-assisted code as needed and retained responsibility for the final research software and its use in the reported study.
```

### Final declaration EN

```text
During the preparation of this work, the author used ChatGPT (OpenAI) to support manuscript drafting and language refinement, and Codex (OpenAI) to support software implementation and code refinement. The author reviewed and edited the AI-assisted outputs as needed and takes full responsibility for the content of the publication and the final research software.
```

### Methods ES

```text
OpenAI Codex se utilizó como herramienta de desarrollo de software asistida por IA para apoyar la implementación de software y el refinamiento de código. El autor revisó y editó el código asistido por Codex según fue necesario y conservó la responsabilidad sobre el software de investigación final y su uso en el estudio reportado.
```

### Declaración final ES

```text
Durante la preparación de este trabajo, el autor utilizó ChatGPT (OpenAI) como apoyo para la redacción del manuscrito y el refinamiento del lenguaje, y Codex (OpenAI) como apoyo para la implementación de software y el refinamiento de código. El autor revisó y editó las salidas asistidas por IA según fue necesario y asume plena responsabilidad por el contenido de la publicación y por el software de investigación final.
```

## 5. Integración canónica

El candidato corregido y aprobado fue materializado como:

`article/manuscript/ARTICLE_MASTER_V036.md`

La verificación observada:

```text
V036_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90

EXPECTED =
c9dcbcc376cdb121d30dc2408756a6c95b569a90

RESULT = PASS
```

## 6. Cierre

Por instrucción previa del Autor, los componentes restantes del End Matter y el ensamblaje final de sumisión quedan bajo responsabilidad directa del Autor.

IA Gestora no continuará sobre esos componentes.

```text
CURRENT_DRAFTING_PHASE = AUTHOR_FINALIZATION
CURRENT_GATE = AUTHOR_OWNED_FINAL_ASSEMBLY
NEXT_ACTOR = AUTHOR
NEXT_ACTION = COMPLETE_REMAINING_END_MATTER_AND_SUBMISSION_ASSEMBLY

GESTORA_TASK_STATUS = FINALIZED
AUTHOR_APPROVAL_GATE = CLOSED / APPROVED

CANONICAL_MASTER = ARTICLE_MASTER_V036
AI_DISCLOSURE_STATUS = CLOSED / APPROVED / FROZEN / INTEGRATED
OTHER_END_MATTER = AUTHOR_OWNED
FINAL_SUBMISSION_ASSEMBLY = AUTHOR_OWNED

SUBMISSION_READY = NOT_ASSERTED
```

---

## English

D-192 records the independent audit of the Writing-AI V02 response, the author's explicit singular-author correction, the author's conditional approval after that correction, and byte-exact canonical integration as ARTICLE_MASTER_V036.

Only four governed AI-disclosure paragraphs were changed from plural to singular author language, with the grammatical agreement required by that correction. The Markdown and DOCX passed differential, OOXML, comment/anchor, tracked-change, render, and full visual QA.

V036 is now canonical. The AI disclosure is closed, approved, frozen, and integrated.

All remaining End Matter and final submission assembly are author-owned. The Managing-AI task is finalized.
