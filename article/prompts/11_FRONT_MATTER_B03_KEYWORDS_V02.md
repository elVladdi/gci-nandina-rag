# Prompt — Front matter B03 / Final Keywords V02

## Rol y autorización

Actúa exclusivamente como **IA de Redacción científica** del proyecto GIC-NANDINA.

Ejecuta solo este bloque y solo bajo la autorización viva que apunte expresamente a este prompt V02 y a su Git blob.

No asumas funciones de IA Gestora, IA Experimental ni Autor.

## Objetivo

Materializar exactamente la corrección de Keywords / Palabras clave fijada por D-184 para cumplir el máximo vigente de seis keywords antes de la sumisión a *Knowledge-Based Systems*.

No generes alternativas.

## Onboarding obligatorio

Lee íntegramente, como mínimo:

1. `article/START_HERE.md`
2. `article/ARTICLE_STATUS.md`
3. `article/ARTICLE_WRITING_PLAN.md`
4. `article/STYLE_GUIDE.md`
5. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`
6. `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`
7. `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`
8. `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`
9. `article/governance/D183_KEYWORDS_B03_V01_AUTHOR_APPROVAL_VERIFICATION_AND_V034_INTEGRATION.md`
10. `article/reviews/11_FRONT_MATTER_B03_KEYWORDS_KBS_SUBMISSION_COMPLIANCE_REVIEW_V01.md`
11. `article/governance/D184_KEYWORDS_B03_V01_KBS_COMPLIANCE_REOPEN_AND_V02_REQUIREMENT.md`
12. la revisión interna vigente de este prompt;
13. la autorización viva de ejecución;
14. este prompt completo;
15. `article/manuscript/ARTICLE_MASTER_V034.md`.

Si la gobernanza viva contradice estas identidades, detente en preflight.

## Preflight

Registra en la response:

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = FRONT_MATTER / KEYWORDS
PROMPT_IDENTITY = PASS / BLOCKED
EXECUTION_AUTHORIZATION_IDENTITY = PASS / BLOCKED
CANONICAL_MASTER_IDENTITY = PASS / BLOCKED
WORD_BASELINE_IDENTITY = PASS / BLOCKED
LIVE_GATE_CONSISTENCY = PASS / BLOCKED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
BLOCKERS = ...
```

No reconcilies drift por inferencia propia.

## Baseline Markdown exacto

```text
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V034.md
EXPECTED_SHA256 = 37994390a1be96d6c37bceb6536ea367b0918872b63180e2f5531ba32856f6ca
EXPECTED_GIT_BLOB = 0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684
```

## Baseline Word exacto

Trabaja directamente sobre:

`ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V01.docx`

```text
EXPECTED_SHA256 = 8e31acd688e0e7b52a8f132ed12f342178c75daf9bfe1dbb4d8c44137f317b84
EXPECTED_SIZE_BYTES = 110943
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 71
```

No reconstruyas el Word desde Markdown.

Si no tienes acceso a los bytes exactos del DOCX, detente en preflight.

## Texto exacto a materializar

### English Keywords

Materializa exactamente, en una única línea y en este orden:

```text
Knowledge-based decision support; Tariff classification; Harmonized System; Information retrieval; Large language model; Provenance
```

### Palabras clave

Materializa exactamente, en una única línea y en este orden:

```text
Apoyo a la decisión basado en conocimiento; Clasificación arancelaria; Sistema Armonizado; Recuperación de información; Modelo de lenguaje grande; Procedencia
```

Estos textos están fijados por D-184.

No reformules, sustituyas, añadas, elimines ni reordenes términos.

## Razón de la revisión

B03 V01 fue aprobado por el autor y promovido como V034, pero una auditoría de compliance posterior detectó que la guía vigente de Elsevier limita la lista a un máximo de seis keywords.

V02 corrige únicamente ese requisito de sumisión y dos detalles asociados:

- `Large language models` → `Large language model`;
- `Provenance and traceability` → `Provenance`;
- `Documentary evidence` se elimina solo de la lista de Keywords y permanece explícito en el Title y cuerpo del manuscrito.

No reabras ninguna decisión científica.

## Scope diferencial autorizado

Solo sustituye:

- la línea final dentro de `## Keywords`;
- la línea final dentro de `## Palabras clave`.

```text
AUTHORIZED_CHANGED_BLOCKS = KEYWORDS_EN + KEYWORDS_ES ONLY
TITLE_EN_ES = PRESERVE_FROZEN
ABSTRACT_EN_ES = PRESERVE_FROZEN
SECTIONS_1_TO_7 = PRESERVE
END_MATTER = PRESERVE_PLACEHOLDERS
```

Cualquier mutación fuera de las dos líneas autorizadas implica `BLOCKED_OUT_OF_SCOPE_MUTATION`.

## Frontera científica vinculante

Preserva:

- `Knowledge-based decision support` como caracterización del sistema completo;
- `Harmonized System` como vocabulario del dominio general;
- `Information retrieval` como familia técnica, sin lock-in a BM25;
- `Large language model` como familia de la etapa explicativa, no autoridad clasificatoria;
- `Provenance` como propiedad de lineage/origin, no correctness.

No introducir:

- Documentary evidence como keyword V02;
- Auditability;
- RAG;
- BM25;
- NANDINA;
- Chapter 87;
- Peru;
- Explainable AI;
- novelty / first / SOTA / superiority;
- legal correctness;
- human validation;
- generalization;
- deployment readiness.

## DOCX / OOXML

Preserva:

```text
OOXML_PART_COUNT = 14
COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
TRACKED_CHANGES = 0
```

`word/comments.xml` debe permanecer byte-idéntico.

La única parte OOXML esperable con cambio sustantivo es `word/document.xml`.

Ejecuta:

- ZIP/OOXML integrity check;
- comparación diferencial contra baseline;
- render completo;
- QA visual de todas las páginas;
- equivalencia visible Markdown ↔ DOCX.

## Entregables

1. `article/sections/front_matter/Keywords_B03_V02.md`
2. `ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V02.md`
3. `ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V02.docx`
4. `article/responses/11_FRONT_MATTER_B03_KEYWORDS_RESPONSE_V02.md`

El artefacto de sección debe contener únicamente las Keywords EN/ES exactas y una nota breve de que fueron fijadas por D-184.

## Handoff D-035

Versiona en GitHub solo:

- `article/sections/front_matter/Keywords_B03_V02.md`;
- `article/responses/11_FRONT_MATTER_B03_KEYWORDS_RESPONSE_V02.md`.

Entrega los masters acumulativos MD/DOCX como archivos reales al autor.

```text
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
CUMULATIVE_MD_REAL_FILE_HANDOFF_TO_AUTHOR = REQUIRED
CUMULATIVE_DOCX_REAL_FILE_HANDOFF_TO_AUTHOR = REQUIRED
```

No uses Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes.

## Response técnica mínima

Incluye:

```text
KEYWORDS_EN = ...
KEYWORDS_ES = ...
KEYWORD_COUNT_EN = 6
KEYWORD_COUNT_ES = 6

SECTION_ARTIFACT_SHA256 = ...
SECTION_ARTIFACT_GIT_BLOB = ...

MASTER_CANDIDATE_MD_SHA256 = ...
MASTER_CANDIDATE_MD_EXPECTED_GIT_BLOB = ...

CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

MARKDOWN_OUTSIDE_AUTHORIZED_BLOCKS_BYTE_EQUIVALENT_TO_V034 = PASS / BLOCKED
MD_DOCX_VISIBLE_TEXT_EQUIVALENCE = PASS / BLOCKED
COMMENTS_AND_ANCHORS_PRESERVED = PASS / BLOCKED
COMMENTS_XML_BYTE_IDENTICAL = PASS / BLOCKED
TRACKED_CHANGES = ...
ZIP_OOXML_INTEGRITY = PASS / BLOCKED
OOXML_CHANGED_PARTS = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = PASS / BLOCKED
FULL_DOCX_VISUAL_QA = PASS / BLOCKED

NO_NEW_RESULTS_OR_INFERENCE = PASS / BLOCKED
NO_NEW_LITERATURE_OR_CITATIONS = PASS / BLOCKED
D184_EXACT_KEYWORDS_MATERIALIZATION = PASS / BLOCKED
TITLE_AND_ABSTRACT_FROZEN = PASS / BLOCKED
END_MATTER_UNCHANGED = PASS / BLOCKED

EXACT_CUMULATIVE_MD_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
EXACT_CUMULATIVE_DOCX_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
```

## Stop condition

Antes del mensaje terminal, la response sustantiva debe estar versionada en GitHub.

Después de adjuntar los dos masters acumulativos exactos, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/11_FRONT_MATTER_B03_KEYWORDS_RESPONSE_V02.md@<commit_sha>`

Detente en:

`FRONT_MATTER_B03_KEYWORDS_V02_COMPLETED_PENDING_GESTORA_AUDIT`

No ejecutes End Matter.

```text
EXPECTED_EXIT = FRONT_MATTER_B03_KEYWORDS_V02_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```
