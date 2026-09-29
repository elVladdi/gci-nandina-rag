# Prompt — Pre-FAST scientific correction A09+A10 / Diagnostic LLM reranker V01

## Rol y autorización

Actúa exclusivamente como **IA de Redacción científica** del proyecto GIC-NANDINA.

Ejecuta únicamente la corrección científica estrecha G7F03-A09 + G7F03-A10 autorizada por la decisión viva que apunte expresamente a este prompt y a su Git blob.

No asumas funciones de IA Gestora, IA Experimental ni Autor.

## Objetivo

Corregir una única omisión científica detectada por la auditoría experimental G7-F03:

1. documentar en Experimental Design el protocolo realmente ejecutado del reranker LLM diagnóstico;
2. reportar en Results sus resultados congelados;
3. mantener la ruta diagnóstica estrictamente separada del flujo principal y sin interpretación inferencial.

No revises ni optimices ningún otro contenido del manuscrito.

## Onboarding obligatorio

Lee íntegramente, como mínimo:

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
13. `article/governance/D136_SUBSTANTIVE_EDITORIAL_AUDIT_AND_INTERNAL_TERMINOLOGY_CONTROL.md`
14. `article/governance/D192_AI_DISCLOSURE_V02_SINGULAR_AUTHOR_APPROVAL_AND_V036_INTEGRATION.md`
15. `article/governance/D193_AI_DISCLOSURE_DOCX_PAGE_COUNT_METADATA_CORRECTION.md`
16. `article/governance/D194_PRE_FAST_G7_F03_EXPERIMENTAL_ARTICLE_REVIEW_REQUEST.md`
17. `article/governance/D195_G7_F03_A09_A10_DIAGNOSTIC_RERANKER_CORRECTION_BOUNDARY.md`
18. la revisión interna vigente de este prompt;
19. la autorización viva de ejecución;
20. este prompt completo;
21. `article/manuscript/ARTICLE_MASTER_V036.md`.

Como fuentes científicas primarias obligatorias, lee además en `main`:

22. `docs/writing/group7/g7_f03_article_scientific_review_v0.1.md` desde la rama `writing/g7-f03-article-scientific-review-v01`;
23. `outputs/audits/group7_closure_v0.1.json` desde esa misma rama;
24. `docs/exp04_phase_g_exp06_historical_reranker_audit.md`;
25. `src/configs/diagnostic_llm_reranker_v0.2.json`;
26. `outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/gate_g_pre_llm_freeze_v0.2.md`;
27. `outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_run_metadata_v0.2.json`;
28. `outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_metrics_v0.2.json`;
29. `outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_win_tie_loss_v0.2.json`;
30. `outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/summary.md`.

No uses conversaciones anteriores como fuente de verdad científica.

## Identidades científicas congeladas

```text
G7_F03_REPORT_BLOB =
bc4ad51a8b219adb8cd9a9beab69cdfb5f7f1875

G7_F03_AUDIT_RECORD_BLOB =
ed4f74610ed73ea76427bef2eef2f4319c698441

PHASE_G_AUDIT_BLOB =
4f343cc713b006a5d92414879520ca69b3e2843a

RERANKER_CONFIG_BLOB =
21c7f4840d7ca7cc10a1da14569ad8843d75f3bd

RERANKER_RUN_METADATA_BLOB =
5daba1ed3f44b2d8906d40588dbe2fcec4bf0e4b

RERANKER_METRICS_BLOB =
15800df93cf77f4f2c6e83ac6cb692be013bbeb3

RERANKER_WIN_TIE_LOSS_BLOB =
a4d508070d1ef61abbd09a34a7f0ba76f5013a2a

RERANKER_SUMMARY_BLOB =
2e356497695551c9df61fb36e70d0cd6d2003daa
```

Si cualquiera de estas identidades no coincide, detente en preflight.

## Preflight obligatorio

La response debe registrar:

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = PRE_FAST_SCIENTIFIC_CORRECTION
BLOCK = G7F03_A09_A10_DIAGNOSTIC_RERANKER
PROMPT_IDENTITY = PASS / BLOCKED
EXECUTION_AUTHORIZATION_IDENTITY = PASS / BLOCKED
CANONICAL_MASTER_MD_IDENTITY = PASS / BLOCKED
WORD_BASELINE_IDENTITY = PASS / BLOCKED
G7_F03_REPORT_IDENTITY = PASS / BLOCKED
PHASE_G_SOURCE_IDENTITIES = PASS / BLOCKED
LIVE_GATE_CONSISTENCY = PASS / BLOCKED
EXPERIMENTAL_REVIEW_TRIGGER = PRESENT / REQUIRED_POST_EXECUTION_REAUDIT
BLOCKERS = ...
```

No reconcilies drift científico por inferencia propia.

## Baseline Markdown exacto

Trabaja sobre:

`article/manuscript/ARTICLE_MASTER_V036.md`

```text
EXPECTED_SHA256 =
8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8

EXPECTED_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90
```

## Baseline Word exacto

Trabaja directamente sobre:

`ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx`

```text
EXPECTED_SHA256 =
d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d

EXPECTED_SIZE_BYTES = 111524
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 72
```

No reconstruyas el Word desde Markdown.

Si no tienes acceso a los bytes exactos del DOCX, detente en preflight y versiona una response de bloqueo. No uses el candidato no corregido de 111528 bytes.

## Scope autorizado

Se autorizan exclusivamente cuatro bloques textuales nuevos:

```text
A09_METHOD_EN
A10_RESULT_EN
A09_METHOD_ES
A10_RESULT_ES
```

No se autoriza ningún otro cambio de contenido.

### A09_METHOD_EN

Ubicación: dentro de `## 4.5. Experimental system configuration and execution`, después del párrafo que describe la ejecución principal del LLM de explicación y antes del párrafo final sobre runtimes.

Redacta **un solo párrafo compacto**, aproximadamente 130–190 palabras, que documente el reranker diagnóstico ejecutado.

Debe incluir de forma natural y científicamente delimitada:

- análisis diagnóstico separado del flujo principal;
- pool v0.2 de profundidad nominal 100, tamaño efectivo 63–100;
- estrategia `historical_first_80_normative_20`, con deduplicación por primera aparición;
- selección aleatoria uniforme sin reemplazo de 20 casos elegibles sobre `case_id` ordenados, seed 0;
- 10 candidatos cerrados por caso como entrada al reranker;
- etiquetas de referencia excluidas de la selección/generación y utilizadas solo en evaluación;
- `qwen2.5:7b-instruct`, Ollama local, Q4_K_M, `temperature=0`, respuesta JSON, sin retry, una ejecución por input;
- candidate closure 20/20;
- 19 referencias dentro del pool y 1 fuera, como propiedad observada del conjunto diagnóstico, no como criterio de muestreo;
- ausencia de prueba inferencial preespecificada;
- ruta diagnóstica sin feedback al ranking/Top-3 principal.

No introduzcas hashes, commits, IDs de gate o nombres de archivos en prosa publicable.

### A10_RESULT_EN

Ubicación: al final de `## 5.2. Candidate retrieval performance`, inmediatamente antes de `## 5.3. Documentary evidence retrieval`.

Redacta **un solo párrafo compacto**, aproximadamente 90–140 palabras, identificado verbalmente como análisis diagnóstico separado.

Debe reportar:

- 20 casos;
- 19 con referencia en el pool y 1 sin referencia en el pool;
- Top-1 `0.50 -> 0.50`;
- Top-3 `0.65 -> 0.65`;
- Top-5 `0.80 -> 0.80`;
- MRR `0.6326 -> 0.6326` (o precisión completa si lo prefieres, idéntica antes/después);
- `wins/ties/losses = 0/19/0` calculado solo sobre los 19 casos con referencia en pool;
- candidate closure 20/20;
- no se ejecutó inferencia pareada porque no existía un test inferencial preespecificado.

Interpretación permitida: **no se observaron cambios en esas métricas dentro de esta muestra diagnóstica**.

Interpretaciones prohibidas: equivalencia estadística, no inferioridad, superioridad, mejora, degradación, generalización o efecto nulo poblacional.

### A09_METHOD_ES

Espejo semántico natural de A09_METHOD_EN dentro de `## 4.5. Configuración y ejecución del sistema experimental`, en la posición equivalente.

Conserva exactamente cifras, denominadores, configuración y límites.

### A10_RESULT_ES

Espejo semántico natural de A10_RESULT_EN dentro de `## 5.2. Desempeño de recuperación de candidatos`, inmediatamente antes de `## 5.3. Recuperación de evidencia documental`.

Conserva exactamente cifras, denominadores y límites.

## Contenido que debe permanecer byte-equivalente en Markdown

Fuera de los cuatro bloques autorizados:

```text
TITLE = PRESERVE
ABSTRACT = PRESERVE
KEYWORDS = PRESERVE
SECTIONS_1_TO_3_7 = PRESERVE
SECTION_4_EXCEPT_A09_INSERTION = PRESERVE
SECTION_5_EXCEPT_A10_INSERTION = PRESERVE
DISCUSSION_6_1_TO_6_6 = PRESERVE
CONCLUSION_7 = PRESERVE
END_MATTER = PRESERVE
REFERENCES_PLACEHOLDER = PRESERVE
FIGURE_1_PLACEHOLDER = PRESERVE
DRAFTING_NOTES = PRESERVE
```

No elimines ni reformules las menciones arquitectónicas existentes al reranking diagnóstico en §3.

## Guardrails científicos

Preserva explícitamente:

```text
PRIMARY_FLOW =
HISTORICAL_RANKING -> FIXED_TOP3 -> CANDIDATE_SPECIFIC_DOCUMENTARY_EVIDENCE -> CONTEXT -> LOCAL_LLM_EXPLANATION

DIAGNOSTIC_RERANKER = SEPARATE / NO_FEEDBACK_TO_PRIMARY_FLOW
NORMATIVE_EVIDENCE != PRIMARY_RANKING_AUTHORITY
DIAGNOSTIC_SAMPLE != PRIMARY_BENCHMARK_INFERENCE
ZERO_OBSERVED_DELTA != STATISTICAL_EQUIVALENCE
0_19_0 != INFERENTIAL_PROOF
HE3 = SUPPORTED / DO_NOT_REDECIDE
NO_NEW_EXPERIMENT
NO_NEW_METRIC
NO_NEW_CI
NO_NEW_P_VALUE
EXP12 = DO_NOT_REOPEN
```

No agregues literatura ni citas.

## Artefacto de bloque

Crea:

`article/sections/pre_fast/Diagnostic_Reranker_A09_A10_V01.md`

Debe contener:

1. A09 method EN;
2. A10 result EN;
3. A09 method ES;
4. A10 result ES;
5. una tabla de trazabilidad interna que vincule cada bloque con las fuentes congeladas, sin insertar esa tabla en el manuscrito.

## Masters acumulativos

Crea y entrega como archivos reales:

1. `ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx`

El Markdown debe partir exactamente de V036.

El DOCX debe partir directamente del Word canónico corregido V036 y no reconstruirse desde Markdown.

## DOCX / OOXML

Preserva los 48 comentarios heredados y sus anchors.

```text
EXPECTED_COMMENTS = 48
EXPECTED_COMMENT_RANGE_START = 48
EXPECTED_COMMENT_RANGE_END = 48
EXPECTED_COMMENT_REFERENCE = 48
EXPECTED_TRACKED_CHANGES = 0
```

Ejecuta como mínimo:

- ZIP/OOXML integrity;
- inventario de parts;
- differential audit frente al baseline;
- verificación de que las únicas mutaciones visibles corresponden a A09/A10 EN/ES y al reflow inevitable;
- `word/comments.xml` byte-idéntico;
- conteos de comments y anchors;
- tracked changes;
- render completo;
- QA visual de todas las páginas;
- equivalencia visible MD↔DOCX.

La paginación puede cambiar por reflow; no la fuerces artificialmente a 72.

## Response

Versiona:

`article/responses/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_RESPONSE_V01.md`

Incluye como mínimo:

```text
A09_METHOD_EN = ...
A10_RESULT_EN = ...
A09_METHOD_ES = ...
A10_RESULT_ES = ...

SECTION_ARTIFACT_SHA256 = ...
SECTION_ARTIFACT_GIT_BLOB = ...

MASTER_CANDIDATE_MD_SHA256 = ...
MASTER_CANDIDATE_MD_EXPECTED_GIT_BLOB = ...

CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

AUTHORIZED_BLOCK_COUNT_MD = 4
AUTHORIZED_BLOCK_COUNT_DOCX = 4

MARKDOWN_OUTSIDE_AUTHORIZED_BLOCKS_BYTE_EQUIVALENT_TO_V036 = PASS / BLOCKED
MD_DOCX_VISIBLE_TEXT_EQUIVALENCE = PASS / BLOCKED

COMMENTS = ...
COMMENT_RANGE_START = ...
COMMENT_RANGE_END = ...
COMMENT_REFERENCE = ...
COMMENTS_XML_BYTE_IDENTICAL = PASS / BLOCKED
TRACKED_CHANGES = ...
ZIP_OOXML_INTEGRITY = PASS / BLOCKED
OOXML_CHANGED_PARTS = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = PASS / BLOCKED
FULL_DOCX_VISUAL_QA = PASS / BLOCKED

G7F03_A09_MATERIALIZED = PASS / BLOCKED
G7F03_A10_MATERIALIZED = PASS / BLOCKED
DIAGNOSTIC_ONLY_BOUNDARY_PRESERVED = PASS / BLOCKED
NO_NEW_RESULTS_OR_INFERENCE = PASS / BLOCKED
NO_NEW_LITERATURE_OR_CITATIONS = PASS / BLOCKED
DISCUSSION_CONCLUSION_ABSTRACT_UNCHANGED = PASS / BLOCKED
HE3_NOT_REDECIDED = PASS / BLOCKED
EXP12_NOT_REOPENED = PASS / BLOCKED

POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = YES

EXACT_CUMULATIVE_MD_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
EXACT_CUMULATIVE_DOCX_HANDOFF_TO_AUTHOR = COMPLETED / BLOCKED
```

## Handoff

Versiona en GitHub únicamente:

- `article/sections/pre_fast/Diagnostic_Reranker_A09_A10_V01.md`;
- `article/responses/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_RESPONSE_V01.md`.

Entrega los dos masters acumulativos exactos al Autor como archivos reales.

No promociones todavía ningún nuevo `ARTICLE_MASTER_V0xx.md`.

No modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` ni decisiones de gobernanza.

## Stop condition

Detente en:

`G7F03_A09_A10_V01_COMPLETED_PENDING_GESTORA_AUDIT`

No continúes con FINAL-F01.

```text
AUTHOR_APPROVAL_GATE = NOT_OPEN
EXPERIMENTAL_REAUDIT_GATE = REQUIRED_AFTER_GESTORA_PASS
FINAL_F01 = NOT_AUTHORIZED
FINAL_F02 = NOT_AUTHORIZED
FINAL_F03 = NOT_AUTHORIZED
```
