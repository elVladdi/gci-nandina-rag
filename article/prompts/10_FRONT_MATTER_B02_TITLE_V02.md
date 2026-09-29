# Prompt — Front matter B02 / Final Title V02

## Rol y autorización

Actúa exclusivamente como **IA de Redacción científica** del proyecto GIC-NANDINA.

Ejecuta solo este bloque y solo bajo la autorización viva que apunte expresamente a este prompt V02 y a su Git blob.

No asumas funciones de IA Gestora, IA Experimental ni Autor.

## Objetivo

Materializar exactamente la revisión editorial del Title/Título fijada por D-170 después de la auditoría del corpus completo de 34 artículos aceptados de *Knowledge-Based Systems*.

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
9. `article/governance/D165_ABSTRACT_B01_AUTHOR_APPROVAL_V032_VERIFICATION_AND_INTEGRATION.md`
10. `article/governance/D166_FRONT_MATTER_TITLE_INTERPRETIVE_BOUNDARY.md`
11. `article/reviews/10_FRONT_MATTER_B02_TITLE_KBS_CORPUS_EDITORIAL_REVIEW_V01.md`
12. `article/governance/D170_TITLE_B02_V01_KBS_CORPUS_EDITORIAL_REAUDIT_AND_V02_REQUIREMENT.md`
13. la revisión interna vigente de este prompt;
14. la autorización viva de ejecución;
15. este prompt completo;
16. `article/manuscript/ARTICLE_MASTER_V032.md`.

Si la gobernanza viva contradice estas identidades, detente en preflight.

## Preflight

Registra en la response:

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = FRONT_MATTER / TITLE
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
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
EXPECTED_SHA256 = 0fcf9c2676add5128f86efc50788335bc435077bedbd7a8aedbf73f8f1549f64
EXPECTED_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f
```

## Baseline Word exacto

Trabaja directamente sobre:

`ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V02.docx`

```text
EXPECTED_SHA256 = 4709944a4653dac813b5ebe68b1b14a13c9b87ceddadd315308e975289335156
EXPECTED_SIZE_BYTES = 111028
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 71
```

No uses como baseline `ARTICLE_MASTER_CANDIDATE_TITLE_B02_V01.docx`, porque V01 nunca fue aprobado ni promovido.

No reconstruyas el Word desde Markdown.

Si no tienes acceso a los bytes exactos del DOCX, detente en preflight.

## Texto exacto a materializar

### English

```text
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support
```

### Español

```text
Separación del ranking de candidatos, la evidencia documental y la explicación en el apoyo a la decisión de clasificación arancelaria
```

Estos textos están fijados por D-170.

No reformules, acortes, amplíes ni propongas variantes.

## Scope diferencial autorizado

Solo sustituye:

- el placeholder/instrucciones dentro de `## Title`;
- el placeholder/instrucciones dentro de `## Título`.

```text
AUTHORIZED_CHANGED_BLOCKS = TITLE_EN + TITLE_ES ONLY
ABSTRACT_EN_ES = PRESERVE_FROZEN
KEYWORDS_EN_ES = PRESERVE_PLACEHOLDER
SECTIONS_1_TO_7 = PRESERVE
END_MATTER = PRESERVE
```

Cualquier mutación fuera de las dos zonas autorizadas implica `BLOCKED_OUT_OF_SCOPE_MUTATION`.

## Racional editorial vinculante

La revisión V02 responde a la auditoría del corpus KBS:

- el título debe exponer la operación metodológica concreta del artículo;
- candidate ranking, documentary evidence y explanation son las tres funciones que estructuran Abstract, Introduction, Positioning, Architecture, Methods, Results, Discussion y Conclusion;
- `Auditable` no debe ocupar la promesa primaria del título;
- `Authority Separation` no debe quedar como abstracción no explicada;
- NANDINA/Chapter 87 sigue siendo testbed y no alcance conceptual;
- no introducir novelty, first/SOTA, superiority, legal correctness, human validation, generalization o deployment readiness.

No necesitas volver a decidir estos puntos; solo preservarlos al materializar el texto fijado.

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
- QA visual;
- equivalencia visible Markdown ↔ DOCX.

## Entregables

1. `article/sections/front_matter/Title_B02_V02.md`
2. `ARTICLE_MASTER_CANDIDATE_TITLE_B02_V02.md`
3. `ARTICLE_MASTER_CANDIDATE_TITLE_B02_V02.docx`
4. `article/responses/10_FRONT_MATTER_B02_TITLE_RESPONSE_V02.md`

El artefacto de sección debe contener únicamente los títulos EN/ES exactos y una nota breve de que fueron fijados por D-170.

## Handoff D-035

Versiona en GitHub solo:

- `article/sections/front_matter/Title_B02_V02.md`;
- `article/responses/10_FRONT_MATTER_B02_TITLE_RESPONSE_V02.md`.

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
TITLE_EN = ...
TITLE_ES = ...

SECTION_ARTIFACT_SHA256 = ...
SECTION_ARTIFACT_GIT_BLOB = ...

MASTER_CANDIDATE_MD_SHA256 = ...
MASTER_CANDIDATE_MD_EXPECTED_GIT_BLOB = ...

CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

MARKDOWN_OUTSIDE_AUTHORIZED_BLOCKS_BYTE_EQUIVALENT_TO_V032 = PASS / BLOCKED
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
KBS_CORPUS_EDITORIAL_DIRECTIVE_PRESERVED = PASS / BLOCKED

EXACT_CUMULATIVE_MD_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
EXACT_CUMULATIVE_DOCX_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
```

## Stop condition

Antes del mensaje terminal, la response sustantiva debe estar versionada en GitHub.

Después de adjuntar los dos masters acumulativos exactos, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/10_FRONT_MATTER_B02_TITLE_RESPONSE_V02.md@<commit_sha>`

Detente en:

`FRONT_MATTER_B02_TITLE_V02_COMPLETED_PENDING_GESTORA_AUDIT`

No ejecutes Keywords ni end matter.

```text
EXPECTED_EXIT = FRONT_MATTER_B02_TITLE_V02_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```
