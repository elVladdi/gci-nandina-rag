# D-196 — Autorización de ejecución de corrección pre-FAST G7-F03 A09+A10 V01

## Español

```text
DECISION = D-196
PHASE = PRE_FAST_SCIENTIFIC_CORRECTION
PREVIOUS_DECISION = D-195

AUTHORIZED_ACTOR = IA_DE_REDACCION_CIENTIFICA
AUTHORIZED_BLOCK = G7F03_A09_A10_DIAGNOSTIC_RERANKER_V01

PROMPT =
article/prompts/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_V01.md@7b0fa6283a6997785367f16f9d3508e36c07474a
PROMPT_GIT_BLOB =
8e1f046a541aecf066ecafcc12b7648db09905bc

PROMPT_INTERNAL_REVIEW =
article/reviews/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_PROMPT_INTERNAL_REVIEW_V01.md@635623340a9c66859ed34d854f057943699398c7
PROMPT_INTERNAL_REVIEW_GIT_BLOB =
2cb1d0b1028d7cfa4c4169d4570c8c5d363d486b
PROMPT_INTERNAL_REVIEW_RESULT = PASS

INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V036.md
INPUT_MASTER_MD_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90
INPUT_MASTER_MD_SHA256 =
8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8

INPUT_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx
INPUT_MASTER_DOCX_SHA256 =
d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d
INPUT_MASTER_DOCX_SIZE_BYTES = 111524
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
BASELINE_PAGE_COUNT = 72

AUTHORIZED_CHANGE_COUNT = 4
AUTHORIZED_CHANGES =
A09_METHOD_EN + A10_RESULT_EN + A09_METHOD_ES + A10_RESULT_ES

POST_EXECUTION_EXPERIMENTAL_REAUDIT = REQUIRED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_F01 = NOT_AUTHORIZED
```

## 1. Autorización

D-196 autoriza a IA de Redacción científica a ejecutar exclusivamente el prompt V01 identificado arriba.

La autorización existe para reparar los hallazgos mayores G7F03-A09 y G7F03-A10 detectados por IA Experimental. No autoriza una revisión general del artículo.

## 2. Baselines vinculantes

La ejecución debe partir exactamente de V036 y del Word corregido vigente.

Si el Markdown, el DOCX, el prompt o la autorización no coinciden exactamente con las identidades registradas, IA de Redacción debe detenerse en preflight y versionar el bloqueo.

En particular, queda prohibido utilizar como baseline el candidato Word anterior de 111528 bytes.

## 3. Scope

Solo pueden incorporarse:

1. método diagnóstico EN;
2. resultado diagnóstico EN;
3. método diagnóstico ES;
4. resultado diagnóstico ES.

Todo el contenido restante debe preservarse conforme al contrato diferencial del prompt.

## 4. Estado posterior esperado

La ejecución no puede promover un nuevo master canónico ni abrir FINAL-F01.

Salida esperada:

```text
EXPECTED_EXIT =
G7F03_A09_A10_V01_COMPLETED_PENDING_GESTORA_AUDIT

NEXT_ACTOR_AFTER_EXECUTION = IA_GESTORA_DEL_ARTICULO
POST_GESTORA_PASS_ACTOR = IA_EXPERIMENTAL
EXPERIMENTAL_REAUDIT = MANDATORY
AUTHOR_APPROVAL_GATE = NOT_OPEN
```

Solo después de un PASS de IA Gestora y un PASS de reauditoría focalizada de IA Experimental podrá abrirse el gate de aprobación del Autor para la corrección.

---

## English

D-196 authorizes Writing AI to execute only Prompt 14 V01 against the exact V036 Markdown and corrected V036 DOCX baselines.

The only authorized manuscript changes are the four bilingual A09/A10 insertions documenting the already executed diagnostic LLM reranker method and frozen diagnostic results.

No master promotion, FAST finalization work, new experiment, new metric, new inference, or author-approval gate is authorized. The corrected candidate must first pass Managing-AI audit and then a focused Experimental-AI re-audit.
