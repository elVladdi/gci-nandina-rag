# Prompt — Front matter B02 / Final Title V01

## Rol

Actúa exclusivamente como **IA de Redacción científica** del proyecto GIC-NANDINA.

Ejecuta únicamente este bloque. No asumas funciones de IA Gestora, IA Experimental ni Autor.

## Objetivo

Redactar el **Title final en inglés** y su **Título español semánticamente equivalente** sobre el master canónico V032, sin modificar ningún otro contenido del manuscrito.

El título debe representar el objeto arquitectónico-metodológico ya integrado y no convertir el testbed NANDINA/Capítulo 87 en el alcance conceptual del trabajo.

## Onboarding obligatorio

Antes de redactar, lee íntegramente y en este orden:

1. `article/START_HERE.md`
2. `article/README.md`
3. `article/ARTICLE_STATUS.md`
4. `article/ARTICLE_WRITING_PLAN.md`
5. `article/DECISIONS.md`
6. `article/SOURCE_REGISTRY.md`
7. `article/CLAIM_EVIDENCE_MATRIX.md`
8. `article/STYLE_GUIDE.md`
9. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`
10. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`
11. `article/governance/D013_KBS_EMPIRICAL_WRITING_GUIDE_APPROVAL.md`
12. `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md`
13. `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`
14. `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`
15. `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`
16. `article/governance/D136_SUBSTANTIVE_EDITORIAL_AUDIT_AND_INTERNAL_TERMINOLOGY_CONTROL.md`
17. `article/governance/D159_CONCLUSION_B01_AUTHOR_APPROVAL_V031_VERIFICATION_AND_INTEGRATION.md`
18. `article/governance/D160_FRONT_MATTER_ABSTRACT_INTERPRETIVE_BOUNDARY.md`
19. `article/governance/D165_ABSTRACT_B01_AUTHOR_APPROVAL_V032_VERIFICATION_AND_INTEGRATION.md`
20. `article/governance/D166_FRONT_MATTER_TITLE_INTERPRETIVE_BOUNDARY.md`
21. la revisión interna vigente de este prompt;
22. la autorización de ejecución vigente;
23. este prompt completo;
24. `article/manuscript/ARTICLE_MASTER_V032.md`.

No alteres el orden.

## Preflight obligatorio

Antes de editar, verifica que el prompt observado sea exactamente este V01 y que la autorización viva apunte expresamente a su path y Git blob.

La response debe registrar:

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
FASE_ACTIVA = FRONT_MATTER / TITLE
ESTADO_DEL_BLOQUE_ASIGNADO = ...
REDACCIÓN_AUTORIZADA = ...
DECISIONES_CONGELADAS_RELEVANTES = ...
CLAIMS_AUTORIZADOS_RELEVANTES = ...
CLAIMS_PROHIBIDOS_O_PENDIENTES_RELEVANTES = ...
FUENTES_EXTERNAS_QUE_DEBEN_VERIFICARSE = NONE
BLOQUEOS_O_CONTRADICCIONES_DETECTADOS = ...
PROMPT_IDENTITY = PASS / BLOCKED
EXECUTION_AUTHORIZATION_IDENTITY = PASS / BLOCKED
```

Si prompt, autorización, master canónico o Word baseline no coinciden con las identidades gobernadas, detente. No reconcilies drift por inferencia propia.

## Baseline Markdown exacto

```text
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
EXPECTED_SHA256 = 0fcf9c2676add5128f86efc50788335bc435077bedbd7a8aedbf73f8f1549f64
EXPECTED_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f
```

## Baseline Word exacto

Trabaja directamente sobre el archivo acumulativo real:

`ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V02.docx`

Identidad esperada:

```text
EXPECTED_SHA256 = 4709944a4653dac813b5ebe68b1b14a13c9b87ceddadd315308e975289335156
EXPECTED_SIZE_BYTES = 111028
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 71
```

No reconstruyas el Word desde Markdown.

Si los bytes exactos del DOCX no están disponibles en tu entorno, detente con blocker pre-execution.

## Scope diferencial autorizado

Solo puedes sustituir:

- el placeholder/instrucciones dentro de `## Title` en la Parte I inglesa;
- el placeholder/instrucciones dentro de `## Título` en la Parte II española.

```text
AUTHORIZED_CHANGED_BLOCKS = TITLE_EN + TITLE_ES ONLY
ABSTRACT_EN_ES = PRESERVE_FROZEN
KEYWORDS_EN_ES = PRESERVE_PLACEHOLDER
SECTIONS_1_TO_7 = BYTE/TEXT_PRESERVE
END_MATTER_EN_ES = BYTE/TEXT_PRESERVE
TABLES_CAPTIONS_REFERENCES = PRESERVE
```

Cualquier cambio fuera de esas dos zonas implica `BLOCKED_OUT_OF_SCOPE_MUTATION`.

## Función científica del título

Aplica estrictamente D-166.

El título debe hacer visible prioritariamente:

1. el objeto arquitectónico/metodológico;
2. la separación explícita de autoridad decisoria entre ranking de candidatos, asociación documental y explicación controlada;
3. el dominio de apoyo a la clasificación arancelaria cuando ayude a identificar la tarea.

No necesitas enumerar los tres componentes si una formulación más compacta expresa correctamente la propiedad central.

## Estrategia de redacción

Antes de materializar el master, considera internamente varias formulaciones plausibles y selecciona **una sola** como título final del candidato.

No escribas una lista de alternativas en el manuscrito ni en el artefacto de sección.

La opción seleccionada debe optimizar conjuntamente:

```text
SCIENTIFIC_OBJECT_VISIBILITY
ARCHITECTURAL_CONTRIBUTION_VISIBILITY
AUTHORITY_BOUNDARY_FIDELITY
TASK_DOMAIN_PRECISION
TESTBED_SCOPE_HYGIENE
ANTI_OVERCLAIMING
KBS_TITLE_CONCISION
READER_FACING_NATURALNESS
```

## Guía de longitud y forma

El empirical guide de 34 artículos KBS observó:

```text
MEAN = 10.6 English words
RANGE = 7-14 English words
COLON_TWO_PART = 17/34
```

Usa 7–14 palabras como objetivo editorial preferido, no como regla rígida.

Si la mejor formulación sale de ese rango, justifica brevemente en la response por qué mejora precisión.

Puede utilizarse `:` si una estructura en dos partes mejora legibilidad.

No terminar el título con punto.

## Terminología preferida

Puedes usar, si son naturales y necesarios:

- auditable decision support;
- tariff classification;
- decision authority;
- authority separation;
- candidate ranking;
- documentary evidence;
- controlled explanation;
- provenance;
- configurable framework.

No fuerces todas estas expresiones en un único título.

## Terminología/framing a evitar

No usar como framing principal:

- `RAG for HS classification`;
- `LLM + RAG + BM25`;
- `NANDINA Chapter 87`;
- H100, EVAL, SERIE, DAM;
- Decision 885/906;
- porcentajes, métricas, nombres de experimentos/fases;
- inventarios de tecnologías.

## Claims prohibidos

No introducir ni insinuar:

```text
NOVEL
NOVELTY
FIRST
STATE-OF-THE-ART
SOTA
SUPERIOR
SUPERIORITY
ACCURATE
HIGH-ACCURACY
LEGAL CORRECTNESS
HUMAN VALIDATION
GENERALIZABLE
GENERALIZATION
DEPLOYMENT READY
PRODUCTION READY
AUTONOMOUS CLASSIFICATION
END-TO-END CLASSIFIER
```

`FINAL_GAP = NOT_DEFINED`

`NOVELTY = NOT_DECLARED`

## Fronteras científicas

El título debe ser compatible con:

```text
historical retrieval = candidate generation/ranking authority
fixed Top-3 = fixed before documentary association and generation
documentary association = evidence attachment / no reranking
local LLM = controlled explanation only
auditability = inspectability/traceability, not legal correctness
configurability != empirical generalization
```

No sugieras que el LLM clasifica o que el documento normativo decide el ranking.

## Testbed

Preferencia: usar `tariff classification` como dominio de tarea si mejora precisión.

No incluir NANDINA/Chapter 87 salvo que sea editorialmente indispensable. Si se incluye, debe quedar inequívocamente como contexto/testbed y no como alcance conceptual completo.

## Espejo español

El título español debe ser natural, conciso y semánticamente equivalente.

Debe preservar exactamente:

- objeto científico;
- alcance;
- fuerza epistémica;
- ausencia de claims promocionales.

No es necesario calcar la sintaxis inglesa.

## Word / OOXML

Edita directamente el Word acumulativo exacto.

Preserva:

- las 14 partes OOXML;
- los 48 comentarios;
- `commentRangeStart = 48`;
- `commentRangeEnd = 48`;
- `commentReference = 48`;
- texto anclado de los comentarios;
- `tracked changes = 0`.

`word/comments.xml` debe permanecer byte-identical salvo impedimento técnico verificable. Cualquier diferencia no esperada debe bloquear la entrega.

Espera que el cambio sustantivo se concentre en `word/document.xml`.

Realiza ZIP/OOXML integrity check, render completo y QA visual.

## Entregables

1. `article/sections/front_matter/Title_B02_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_TITLE_B02_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_TITLE_B02_V01.docx`
4. `article/responses/10_FRONT_MATTER_B02_TITLE_RESPONSE_V01.md`

El artefacto pequeño debe contener únicamente:

- Title final EN;
- Título final ES;
- word count del título inglés;
- nota breve de por qué la formulación representa el objeto científico sin sobreclaiming.

No incluyas alternativas descartadas.

## D-035 — materialización y handoff

Versiona en GitHub solo:

- `article/sections/front_matter/Title_B02_V01.md`;
- `article/responses/10_FRONT_MATTER_B02_TITLE_RESPONSE_V01.md`.

No intentes materializar directamente en GitHub los masters acumulativos MD/DOCX durante la ejecución.

```text
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
SECTION_ARTIFACT_GITHUB_VERSIONING = REQUIRED
RESPONSE_GITHUB_VERSIONING = REQUIRED
CUMULATIVE_MD_REAL_FILE_HANDOFF_TO_AUTHOR = REQUIRED
CUMULATIVE_DOCX_REAL_FILE_HANDOFF_TO_AUTHOR = REQUIRED
```

Entrega MD y DOCX acumulativos como archivos reales exactos.

No uses Base64 manual, chunking, fragmentación, reensamblado, archivos auxiliares, ramas ad hoc, commits parciales ni workarounds equivalentes.

## Response técnica obligatoria

Incluye como mínimo:

```text
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
PROMPT_IDENTITY = PASS / BLOCKED
EXECUTION_AUTHORIZATION_IDENTITY = PASS / BLOCKED

TITLE_EN = ...
TITLE_EN_WORD_COUNT = ...
TITLE_ES = ...

SECTION_ARTIFACT_SHA256 = ...
SECTION_ARTIFACT_GIT_BLOB = ...

MASTER_CANDIDATE_MD_SHA256 = ...
MASTER_CANDIDATE_MD_EXPECTED_GIT_BLOB = ...

CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

AUTHORIZED_CHANGED_BLOCKS = TITLE_EN + TITLE_ES ONLY
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
ANTI_OVERCLAIMING = PASS / BLOCKED
TESTBED_SCOPE_HYGIENE = PASS / BLOCKED
EN_ES_SEMANTIC_EQUIVALENCE = PASS / BLOCKED

D035_TIMEOUT_SAFE_HANDOFF = PASS / BLOCKED
EXACT_CUMULATIVE_MD_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
EXACT_CUMULATIVE_DOCX_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
```

Si aparece drift científico o necesidad de claim no gobernado:

`EXPERIMENTAL_REVIEW_TRIGGER = PRESENT`

y detente. No resuelvas la discrepancia por inferencia.

## Stop condition

Antes del mensaje terminal, la response sustantiva debe estar versionada en GitHub.

En el chat, después de adjuntar los masters acumulativos exactos, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/10_FRONT_MATTER_B02_TITLE_RESPONSE_V01.md@<commit_sha>`

Detente en:

`FRONT_MATTER_B02_TITLE_V01_COMPLETED_PENDING_GESTORA_AUDIT`

No ejecutes Keywords ni end matter.

## Expected exit

```text
EXPECTED_EXIT = FRONT_MATTER_B02_TITLE_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
