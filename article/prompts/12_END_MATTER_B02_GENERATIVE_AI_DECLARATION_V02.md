# Prompt — End Matter B02 / Generative-AI disclosure V02

## Rol y autorización

Actúa exclusivamente como **IA de Redacción científica** del proyecto GIC-NANDINA.

Ejecuta solo este bloque y solo bajo la autorización viva que apunte expresamente a este prompt V02 y a su Git blob.

No asumas funciones de IA Gestora, IA Experimental ni Autor.

## Objetivo

Materializar exactamente la corrección de transparencia sobre uso de IA fijada por D-190:

1. declarar en Methods el uso de Codex (OpenAI) como apoyo en implementación/refinamiento de código;
2. incorporar antes de References/Referencias la declaración final que identifica ChatGPT y Codex, sus finalidades y la responsabilidad humana.

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
9. `article/governance/D187_KEYWORDS_B03_V02_AUTHOR_APPROVAL_VERSION_REPAIR_AND_V035_INTEGRATION.md`
10. `article/governance/D188_END_MATTER_SOURCE_COMPLETENESS_AND_AUTHOR_DECLARATION_BOUNDARY.md`
11. `article/governance/D189_GENERATIVE_AI_DECLARATION_AND_GESTORA_TASK_CLOSURE.md`
12. `article/governance/D190_REOPEN_AI_DISCLOSURE_FOR_CODEX_AND_REDACCION_FLOW.md`
13. la revisión interna vigente de este prompt;
14. la autorización viva de ejecución;
15. este prompt completo;
16. `article/manuscript/ARTICLE_MASTER_V035.md`.

Si la gobernanza viva contradice estas identidades, detente en preflight.

## Preflight obligatorio

Registra en la response:

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = END_MATTER / AI_DISCLOSURE_CORRECTION
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
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V035.md
EXPECTED_SHA256 = 23a92e46f1fe3d7edfcf9210e1d90a133c17abf6b85e62ad3906171dc48589ac
EXPECTED_GIT_BLOB = ddf3abb1826f93d5d82c0a135c0c2ae6b389e7fd
```

## Baseline Word exacto

Trabaja directamente sobre:

`ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V02.docx`

```text
EXPECTED_SHA256 = de3c60c59bd71e5c5b101c7281a675b68faaf8275af64d7403f1ff51fa60905b
EXPECTED_SIZE_BYTES = 110919
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 71
```

No reconstruyas el Word desde Markdown.

Si no tienes acceso a los bytes exactos del DOCX, detente en preflight.

## Inserción 1 — Methods / Codex

### English

Ubicación exacta: al final de `## 4.8. Reproducibility resources`, inmediatamente antes de `# 5. Results`.

Inserta exactamente:

```text
OpenAI Codex was used as an AI-assisted software-development tool to support software implementation and code refinement. The authors reviewed and edited the Codex-assisted code as needed and retained responsibility for the final research software and its use in the reported study.
```

### Español

Ubicación exacta: al final de `## 4.8. Recursos de reproducibilidad`, inmediatamente antes de `# 5. Resultados`.

Inserta exactamente:

```text
OpenAI Codex se utilizó como herramienta de desarrollo de software asistida por IA para apoyar la implementación de software y el refinamiento de código. Los autores revisaron y editaron el código asistido por Codex según fue necesario y conservaron la responsabilidad sobre el software de investigación final y su uso en el estudio reportado.
```

## Inserción 2 — Declaración final de IA

### English

Ubicación exacta: inmediatamente antes de `# References`.

Inserta exactamente:

```text
# Declaration of generative AI and AI-assisted technologies in the manuscript preparation and research process

During the preparation of this work, the authors used ChatGPT (OpenAI) to support manuscript drafting and language refinement, and Codex (OpenAI) to support software implementation and code refinement. The authors reviewed and edited the AI-assisted outputs as needed and take full responsibility for the content of the publication and the final research software.
```

### Español

Ubicación exacta: inmediatamente antes de `# Referencias`.

Inserta exactamente:

```text
# Declaración sobre el uso de IA generativa y tecnologías asistidas por IA en la preparación del manuscrito y el proceso de investigación

Durante la preparación de este trabajo, los autores utilizaron ChatGPT (OpenAI) como apoyo para la redacción del manuscrito y el refinamiento del lenguaje, y Codex (OpenAI) como apoyo para la implementación de software y el refinamiento de código. Los autores revisaron y editaron las salidas asistidas por IA según fue necesario y asumen plena responsabilidad por el contenido de la publicación y por el software de investigación final.
```

## Interpretación vinculante

Preserva exactamente estas fronteras:

- ChatGPT = apoyo en redacción del manuscrito y refinamiento del lenguaje;
- Codex = apoyo en implementación de software y refinamiento de código;
- autores humanos = revisión/edición de las salidas y responsabilidad final;
- Codex NO = autoridad sobre diseño experimental;
- Codex NO = autoridad sobre resultados, métricas, inferencia, interpretación o conclusiones;
- ChatGPT/Codex NO = autores;
- ChatGPT/Codex NO = validadores científicos;
- el uso experimental del LLM local `qwen2.5:7b-instruct` permanece una cuestión metodológica separada y no debe confundirse con esta declaración.

No añadas nombres de modelos, versiones, fechas, prompts, proveedores, herramientas o funciones que no estén fijados arriba.

## Scope diferencial autorizado

Se autorizan exclusivamente cuatro inserciones:

```text
1. METHODS_CODEX_EN
2. METHODS_CODEX_ES
3. AI_DECLARATION_EN
4. AI_DECLARATION_ES
```

Todo el contenido preexistente de V035 debe preservarse.

No se autoriza completar, corregir o eliminar:

- Title/Título;
- Abstract/Resumen;
- Keywords/Palabras clave;
- Sections 1–7, salvo las dos inserciones Codex en §4.8;
- Data availability;
- Code and reproducibility resources del End Matter;
- CRediT;
- Funding;
- Declaration of competing interest;
- Acknowledgements;
- References;
- Supplementary material;
- Figure 1 placeholder;
- drafting notes;
- author metadata.

Cualquier mutación fuera de las cuatro inserciones autorizadas implica `BLOCKED_OUT_OF_SCOPE_MUTATION`.

## DOCX / OOXML

Preserva:

```text
BASELINE_OOXML_PART_COUNT = 14
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
- comprobación de que existen exactamente las cuatro inserciones autorizadas;
- render completo;
- QA visual de todas las páginas;
- equivalencia visible Markdown ↔ DOCX.

## Artefacto de sección

Crea:

`article/sections/end_matter/Generative_AI_Declaration_V02.md`

Debe contener:

1. `Methods disclosure EN`;
2. `Methods disclosure ES`;
3. `Final declaration EN`;
4. `Final declaration ES`;
5. una nota breve de que los cuatro textos fueron fijados por D-190.

No modifiques ni borres el histórico:

`article/sections/end_matter/Generative_AI_Declaration_V01.md`.

## Masters acumulativos

Crea y entrega como archivos reales:

1. `ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02.md`
2. `ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02.docx`

Estos deben partir exactamente de V035 y del Word baseline B03 V02.

## Response

Versiona:

`article/responses/12_END_MATTER_B02_GENERATIVE_AI_DECLARATION_RESPONSE_V02.md`

Incluye como mínimo:

```text
METHODS_CODEX_EN = ...
METHODS_CODEX_ES = ...
AI_DECLARATION_EN = ...
AI_DECLARATION_ES = ...

SECTION_ARTIFACT_SHA256 = ...
SECTION_ARTIFACT_GIT_BLOB = ...

MASTER_CANDIDATE_MD_SHA256 = ...
MASTER_CANDIDATE_MD_EXPECTED_GIT_BLOB = ...

CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

AUTHORIZED_INSERTION_COUNT_MD = 4
AUTHORIZED_INSERTION_COUNT_DOCX = 4

MARKDOWN_OUTSIDE_AUTHORIZED_INSERTIONS_BYTE_EQUIVALENT_TO_V035 = PASS / BLOCKED
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
D190_EXACT_DISCLOSURE_MATERIALIZATION = PASS / BLOCKED
AUTHOR_OWNED_END_MATTER_UNCHANGED = PASS / BLOCKED

EXACT_CUMULATIVE_MD_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
EXACT_CUMULATIVE_DOCX_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
```

## Handoff D-035

Versiona en GitHub únicamente:

- `article/sections/end_matter/Generative_AI_Declaration_V02.md`;
- `article/responses/12_END_MATTER_B02_GENERATIVE_AI_DECLARATION_RESPONSE_V02.md`.

Entrega los dos masters acumulativos como archivos reales al autor.

No intentes materializar los masters acumulativos grandes en GitHub.

No uses Base64 manual, chunking, fragmentación o reensamblado.

## Stop condition

Antes del mensaje terminal, la response sustantiva debe estar versionada en GitHub.

Después de adjuntar los dos masters acumulativos exactos, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/12_END_MATTER_B02_GENERATIVE_AI_DECLARATION_RESPONSE_V02.md@<commit_sha>`

Detente en:

`END_MATTER_B02_GENERATIVE_AI_DECLARATION_V02_COMPLETED_PENDING_GESTORA_AUDIT`

No completes ningún otro End Matter.

```text
EXPECTED_EXIT =
END_MATTER_B02_GENERATIVE_AI_DECLARATION_V02_COMPLETED_PENDING_GESTORA_AUDIT

AUTHOR_APPROVAL_GATE = NOT_OPEN
OTHER_END_MATTER = AUTHOR_OWNED / DO_NOT_EDIT
```
