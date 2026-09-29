# D-198 — Gestora PASS de A09+A10 y apertura de reauditoría experimental focalizada G7-F03

## Español

```text
DECISION = D-198
PHASE = PRE_FAST_SCIENTIFIC_CORRECTION
PREVIOUS_DECISION = D-197

SOURCE_RESPONSE =
article/responses/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_RESPONSE_V01.md@05ed16e4e22c3d34cb37b32c176a947373d9dde4
SOURCE_RESPONSE_GIT_BLOB =
8613240e8c76e798a6803d355b8c1a33dd98bf38

GESTORA_REVIEW =
article/reviews/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_INTERNAL_REVIEW_V01.md@f9f5ffdbed54fbfbe7618bc823fd7885a11e5f5d
GESTORA_REVIEW_GIT_BLOB =
e08df7d8d1e00c56da6acc48907679af5e3b1682
GESTORA_REVIEW_RESULT = PASS

SECTION_ARTIFACT =
article/sections/pre_fast/Diagnostic_Reranker_A09_A10_V01.md
SECTION_ARTIFACT_GIT_BLOB =
8a4578a992d20dc8f96ab88f08e95e666d4247c5

CANDIDATE_MD_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
CANDIDATE_MD_EXPECTED_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1

CANDIDATE_DOCX_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
CANDIDATE_DOCX_SIZE_BYTES = 112705
CANDIDATE_DOCX_PAGE_COUNT = 73

EXPERIMENTAL_REAUDIT_REQUEST =
article/prompts/15_G7_F03_A09_A10_FOCUSED_EXPERIMENTAL_REAUDIT_V01.md@b94d68f3d41c163f5f6cb11fdadbc168622f5f35
EXPERIMENTAL_REAUDIT_REQUEST_GIT_BLOB =
249c632058d6773741e2ade3254bca1ef42ae8ef

NEXT_ACTOR = IA_EXPERIMENTAL
NEXT_ACTION = EXECUTE_FOCUSED_G7_F03_A09_A10_REAUDIT

AUTHOR_APPROVAL_GATE = NOT_OPEN
CANONICAL_PROMOTION = NOT_AUTHORIZED
FINAL_F01 = NOT_AUTHORIZED
```

## 1. Auditoría de IA Gestora

IA Gestora auditó de forma independiente la response completada de Prompt 14 y los dos candidatos acumulativos entregados por IA de Redacción.

El Markdown candidato tiene identidad exacta:

```text
SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1
```

Al eliminar exactamente los cuatro párrafos autorizados A09/A10 EN/ES y sus separadores de inserción se restaura byte por byte ARTICLE_MASTER_V036:

```text
RESTORED_SIZE_BYTES = 279582
RESTORED_SHA256 =
8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8
RESTORED_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90
```

Por tanto, no existe cambio Markdown fuera de los cuatro bloques autorizados.

## 2. Auditoría científica Gestora

A09 reproduce correctamente el protocolo diagnóstico ya congelado.

A10 reproduce correctamente los resultados congelados:

```text
Top-1 = 0.50 -> 0.50
Top-3 = 0.65 -> 0.65
Top-5 = 0.80 -> 0.80
MRR = 0.6326 -> 0.6326
wins/ties/losses = 0/19/0
candidate_closure = 20/20
paired_inference = NOT RUN
```

La redacción evita afirmar equivalencia estadística, no inferioridad, superioridad, generalización o efecto nulo poblacional.

La ruta diagnóstica permanece separada del flujo primario y sin feedback al fixed Top-3.

## 3. Auditoría DOCX / OOXML

IA Gestora verificó independientemente el candidato entregado:

```text
SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
SIZE_BYTES = 112705
ZIP_OOXML_INTEGRITY = PASS
OOXML_PART_COUNT = 14

COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0

FULL_DOCX_PAGE_COUNT = 73
FULL_DOCX_RENDER = PASS
FULL_DOCX_VISUAL_QA = PASS
PAGES_REVIEWED = 1-73
```

Los cuatro bloques autorizados aparecen una sola vez y el texto visible de cada bloque coincide exactamente entre Markdown y DOCX.

El actual entorno de IA Gestora no permite rematerializar los bytes raw del Word baseline V036 desde Project Library, por lo que no se recomputó una segunda comparación byte-a-byte de cada part no modificado contra el baseline. Esta limitación de procedencia no bloquea la reauditoría científica: la response de Redacción registra su comparación directa contra el baseline exacto, el candidato conserva los 48 comentarios/anchors, cero tracked changes, package integrity y render completo, y ninguna integración canónica está todavía autorizada.

## 4. Resultado del gate Gestora

```text
GESTORA_REVIEW_RESULT = PASS
G7F03_A09_MATERIALIZED = PASS
G7F03_A10_MATERIALIZED = PASS
UNAUTHORIZED_MARKDOWN_CHANGE = NONE
SCIENTIFIC_OVERCLAIM = NONE
MANDATORY_CORRECTIONS = NONE

READY_FOR_FOCUSED_EXPERIMENTAL_REAUDIT = YES
READY_FOR_AUTHOR_APPROVAL = NO
READY_FOR_CANONICAL_PROMOTION = NO
```

## 5. Reauditoría Experimental obligatoria

Conforme a D-195/D-197 y al dictamen original de G7-F03, el candidato debe volver a IA Experimental antes de cualquier gate autoral.

D-198 emite la solicitud versionada:

`article/prompts/15_G7_F03_A09_A10_FOCUSED_EXPERIMENTAL_REAUDIT_V01.md`

Git blob:

`249c632058d6773741e2ade3254bca1ef42ae8ef`.

La reauditoría está restringida a comprobar:

- satisfacción de G7F03-A09;
- satisfacción de G7F03-A10;
- ausencia de contradicción científica directa con el núcleo previamente aprobado;
- cierre formal de G7-F03 / Group 7 conforme al Plan Experimental;
- mantenimiento o revisión de la disposición científica de tablas/figuras G5/G6.

## 6. Gate vigente

```text
CURRENT_DRAFTING_PHASE = PRE_FAST_SCIENTIFIC_CORRECTION
CURRENT_GATE = G7_F03_FOCUSED_EXPERIMENTAL_REAUDIT_PENDING
NEXT_ACTOR = IA_EXPERIMENTAL
NEXT_ACTION = EXECUTE_PROMPT_15_FOCUSED_REAUDIT

AUTHOR_APPROVAL_GATE = NOT_OPEN
CANONICAL_MASTER = ARTICLE_MASTER_V036
CANDIDATE_STATUS = GESTORA_PASS / PENDING_EXPERIMENTAL_REAUDIT
FAST_FINALIZATION_MODE = NOT_AUTHORIZED
FINAL_F01 = NOT_AUTHORIZED
```

If IA Experimental returns PASS and formally closes G7-F03, IA Gestora will then open the Author approval gate for the A09+A10 correction. Only after Author approval and canonical integration may FINAL-F01 begin.

---

## English

D-198 records Managing-AI PASS for the narrowly scoped A09+A10 correction and opens the mandatory focused Experimental-AI re-audit.

The candidate Markdown is independently proven to differ from V036 only by the four authorized bilingual A09/A10 paragraphs. The DOCX identity, OOXML integrity, comment/anchor counts, absence of tracked changes, 73-page render, and full visual QA pass.

No author-approval gate or canonical promotion is opened. Experimental AI must now determine whether G7F03-A09 and G7F03-A10 are satisfied and whether G7-F03 / Group 7 can close under the Experimental Master Plan.
