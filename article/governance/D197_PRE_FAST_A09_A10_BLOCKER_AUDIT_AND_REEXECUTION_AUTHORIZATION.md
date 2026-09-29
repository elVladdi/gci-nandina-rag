# D-197 — Reejecución de Prompt 14 tras blocker válido de baseline DOCX

## Español

```text
DECISION = D-197
PHASE = PRE_FAST_SCIENTIFIC_CORRECTION
PREVIOUS_DECISION = D-196

BLOCKED_RESPONSE =
article/responses/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_RESPONSE_V01.md@55637db5ff0a2a2871097f40ba69a65fb4ef9219
BLOCKED_RESPONSE_GIT_BLOB =
2c6f57b24df4d08b8a59af864c969f0ccb731f66

BLOCKER_AUDIT =
article/reviews/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_RESPONSE_BLOCKER_AUDIT_V01.md@7e62e6a61a797787cd99bac6797ee91cddfef649
BLOCKER_AUDIT_GIT_BLOB =
ac09009830b9d60e75ea09fa2342ed6e9a93ccf5
BLOCKER_AUDIT_RESULT =
PASS_BLOCKED_PREEXECUTION_COMPLIANT

REEXECUTION_PROMPT =
article/prompts/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_V01.md
REEXECUTION_PROMPT_GIT_BLOB =
8e1f046a541aecf066ecafcc12b7648db09905bc

INPUT_MASTER_MD =
article/manuscript/ARTICLE_MASTER_V036.md
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

REEXECUTION_CONDITION =
EXACT_CORRECTED_DOCX_MUST_BE_ATTACHED_AS_REAL_FILE_IN_WRITING_AI_CONTEXT

AUTHORIZED_ACTOR = IA_DE_REDACCION_CIENTIFICA
AUTHORIZED_BLOCK = G7F03_A09_A10_DIAGNOSTIC_RERANKER_V01
POST_EXECUTION_EXPERIMENTAL_REAUDIT = REQUIRED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_F01 = NOT_AUTHORIZED
```

## 1. Disposición del intento D-196

El intento autorizado por D-196 es válido como ejecución bloqueada en preflight.

No se considera una ejecución defectuosa ni una entrega científica incompleta: el prompt exigía detenerse si no estaban disponibles los bytes exactos del Word corregido.

La response bloqueada y su auditoría quedan retenidas como trazabilidad histórica.

## 2. Naturaleza del blocker

El blocker es exclusivamente de acceso al binario Word.

No existe:

- cambio de scope;
- nueva discrepancia científica;
- defecto del Prompt 14;
- defecto de las fuentes Phase-G;
- necesidad de modificar A09/A10;
- necesidad de nuevo experimento.

Por tanto, no se crea Prompt 14 V02.

## 3. Condición obligatoria de reejecución

El Autor debe suministrar directamente en la conversación/contexto de IA de Redacción el archivo real:

`ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx`

IA de Redacción debe verificar sobre los bytes montados:

```text
SHA256 =
d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d

SIZE_BYTES = 111524
```

y continuar solo si esa identidad coincide.

La presencia del archivo por nombre o metadata en Project Library no sustituye este requisito.

## 4. Autorización de reejecución

D-197 autoriza reejecutar íntegramente el mismo Prompt 14 V01, Git blob
`8e1f046a541aecf066ecafcc12b7648db09905bc`,
sin ampliar ni reinterpretar su alcance.

La IA de Redacción debe crear una nueva versión de la misma response path conforme a la política de Git vigente o actualizarla mediante un nuevo commit, preservando el histórico Git del intento bloqueado.

## 5. Stop condition

Se mantiene sin cambios:

`G7F03_A09_A10_V01_COMPLETED_PENDING_GESTORA_AUDIT`

Después de una ejecución completa:

```text
NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
POST_GESTORA_PASS_ACTOR = IA_EXPERIMENTAL
EXPERIMENTAL_REAUDIT = MANDATORY
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_F01 = NOT_AUTHORIZED
```

---

## English

D-197 authorizes re-execution of the unchanged Prompt 14 V01 after the D-196 attempt correctly stopped at preflight because the exact corrected Word baseline was not available as raw bytes.

The blocker is access-only. Re-execution is authorized only when the exact 111524-byte corrected DOCX is supplied as a real attachment in the Writing-AI execution context and independently matches the governed SHA-256. No prompt revision, scientific scope expansion, new experiment, or FAST-finalization task is authorized.
