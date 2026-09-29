# Prompt — Front matter B03 / Final Keywords V01

## Rol y autorización

Actúa exclusivamente como **IA de Redacción científica** del proyecto GIC-NANDINA.

Ejecuta solo este bloque y solo bajo la autorización viva que apunte expresamente a este prompt V01 y a su Git blob.

No asumas funciones de IA Gestora, IA Experimental ni Autor.

## Objetivo

Materializar exactamente las Keywords / Palabras clave fijadas por D-178 después de la integración verificada de Title B02 V03 en V033.

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
9. `article/governance/D177_TITLE_B02_V03_AUTHOR_APPROVAL_VERIFICATION_AND_V033_INTEGRATION.md`
10. `article/governance/D178_FRONT_MATTER_KEYWORDS_INTERPRETIVE_BOUNDARY.md`
11. la revisión interna vigente de este prompt;
12. la autorización viva de ejecución;
13. este prompt completo;
14. `article/manuscript/ARTICLE_MASTER_V033.md`.

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
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V033.md
EXPECTED_SHA256 = bf90c8b10891d401aa34f7553248f30578c1e4b98bef0bcbf32ec1da4446c9f1
EXPECTED_GIT_BLOB = 9b87c71290126f5223c6e4a252f95b5d64f71f49
```

## Baseline Word exacto

Trabaja directamente sobre:

`ARTICLE_MASTER_CANDIDATE_TITLE_B02_V03.docx`

```text
EXPECTED_SHA256 = 1451c7c2d9a013603c749a7ad0730ea450f76700ff853b6d96d9d1f865882ed1
EXPECTED_SIZE_BYTES = 110921
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 71
```

No uses como baseline ningún Word anterior a Title B02 V03.

No reconstruyas el Word desde Markdown.

Si no tienes acceso a los bytes exactos del DOCX, detente en preflight.

## Texto exacto a materializar

### English Keywords

Materializa exactamente, en una única línea de Keywords y en este orden:

```text
Knowledge-based decision support; Tariff classification; Harmonized System; Information retrieval; Documentary evidence; Large language models; Provenance and traceability
```

### Palabras clave

Materializa exactamente, en una única línea y en este orden:

```text
Apoyo a la decisión basado en conocimiento; Clasificación arancelaria; Sistema Armonizado; Recuperación de información; Evidencia documental; Modelos de lenguaje grandes; Procedencia y trazabilidad
```

Estos textos están fijados por D-178.

No reformules, sustituyas, añadas, elimines ni reordenes términos.

## Scope diferencial autorizado

Solo sustituye:

- el placeholder/instrucciones dentro de `## Keywords`;
- el placeholder/instrucciones dentro de `## Palabras clave`.

```text
AUTHORIZED_CHANGED_BLOCKS = KEYWORDS_EN + KEYWORDS_ES ONLY
TITLE_EN_ES = PRESERVE_FROZEN
ABSTRACT_EN_ES = PRESERVE_FROZEN
SECTIONS_1_TO_7 = PRESERVE
END_MATTER = PRESERVE
```

Cualquier mutación fuera de las dos zonas autorizadas implica `BLOCKED_OUT_OF_SCOPE_MUTATION`.

## Frontera científica vinculante

Preserva estas interpretaciones:

- `Knowledge-based decision support` caracteriza el sistema completo, no un expert system simbólico clásico.
- `Harmonized System` funciona como vocabulario de dominio general y no convierte NANDINA/Chapter 87 en alcance conceptual.
- `Information retrieval` cubre la familia técnica sin fijar la arquitectura a BM25.
- `Documentary evidence` identifica la función downstream de asociación de evidencia.
- `Large language models` identifica la familia de la etapa explicativa; no otorga autoridad clasificatoria al LLM.
- `Provenance and traceability` no equivale a legal correctness, human validation o formal auditability.

No introducir:

- Auditability como keyword;
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
- QA visual;
- equivalencia visible Markdown ↔ DOCX.

## Entregables

1. `article/sections/front_matter/Keywords_B03_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V01.docx`
4. `article/responses/11_FRONT_MATTER_B03_KEYWORDS_RESPONSE_V01.md`

El artefacto de sección debe contener únicamente las Keywords EN/ES exactas y una nota breve de que fueron fijadas por D-178.

## Handoff D-035

Versiona en GitHub solo:

- `article/sections/front_matter/Keywords_B03_V01.md`;
- `article/responses/11_FRONT_MATTER_B03_KEYWORDS_RESPONSE_V01.md`.

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
KEYWORD_COUNT_EN = 7
KEYWORD_COUNT_ES = 7

SECTION_ARTIFACT_SHA256 = ...
SECTION_ARTIFACT_GIT_BLOB = ...

MASTER_CANDIDATE_MD_SHA256 = ...
MASTER_CANDIDATE_MD_EXPECTED_GIT_BLOB = ...

CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

MARKDOWN_OUTSIDE_AUTHORIZED_BLOCKS_BYTE_EQUIVALENT_TO_V033 = PASS / BLOCKED
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
D178_EXACT_KEYWORDS_MATERIALIZATION = PASS / BLOCKED
TITLE_AND_ABSTRACT_FROZEN = PASS / BLOCKED

EXACT_CUMULATIVE_MD_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
EXACT_CUMULATIVE_DOCX_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
```

## Stop condition

Antes del mensaje terminal, la response sustantiva debe estar versionada en GitHub.

Después de adjuntar los dos masters acumulativos exactos, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/11_FRONT_MATTER_B03_KEYWORDS_RESPONSE_V01.md@<commit_sha>`

Detente en:

`FRONT_MATTER_B03_KEYWORDS_V01_COMPLETED_PENDING_GESTORA_AUDIT`

No ejecutes end matter.

```text
EXPECTED_EXIT = FRONT_MATTER_B03_KEYWORDS_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```
