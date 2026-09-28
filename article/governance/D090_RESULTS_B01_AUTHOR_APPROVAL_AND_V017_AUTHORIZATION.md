# D-090 — Aprobación autoral de Results B01 y autorización de V017 / Results B01 author approval and V017 authorization

## Español

```text
DECISION_ID = D-090
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-089
PHASE = RESULTS
BLOCK = RESULTS_B01_SECTION_5_1
CANDIDATE_REVISION = V01
AUTHOR_DECISION = APPROVED
RESULTS_B01_STATE = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_5_1 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V017
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión autoral

El autor aprobó explícitamente Results B01 V01 / Section 5.1 después del `PASS` de IA Gestora registrado en D-089. Se cierra el gate autoral de B01.

La aprobación autoriza exclusivamente la promoción byte-exacta del candidato Markdown aprobado a `article/manuscript/ARTICLE_MASTER_V017.md`. No autoriza por sí sola Results B02 ni ninguna sección posterior.

## 2. Identidades congeladas del candidato aprobado

IA Gestora re-verificó localmente los dos archivos entregados antes de registrar esta decisión:

```text
SOURCE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md
SOURCE_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
SOURCE_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c

SOURCE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
SOURCE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

## 3. Promoción autorizada

```text
PROMOTION_SOURCE = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md
PROMOTION_TARGET = article/manuscript/ARTICLE_MASTER_V017.md
EXPECTED_TARGET_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
EXPECTED_TARGET_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
PROMOTION_MODE = BYTE_EXACT
```

Hasta que el target se materialice en GitHub y IA Gestora verifique la identidad exacta del Git blob, `ARTICLE_MASTER_V016` continúa siendo el master canónico.

El DOCX aprobado permanece bajo custodia local del autor y será el Word acumulativo canónico únicamente después de que la promoción V017 sea verificada. No debe reconstruirse desde Markdown.

## 4. Gate

```text
CURRENT_GATE = RESULTS_B01_V017_PROMOTION_PENDING
NEXT_ACTOR = AUTHOR_FOR_BYTE_EXACT_MATERIALIZATION
NEXT_ACTION = MATERIALIZE_EXACT_APPROVED_MD_AS_ARTICLE_MASTER_V017
ARTICLE_MASTER_V016 = CANONICAL_UNTIL_VERIFICATION
ARTICLE_MASTER_V017 = AUTHORIZED / PENDING_MATERIALIZATION_AND_VERIFICATION
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

Tras verificación byte-exacta, IA Gestora deberá registrar la integración de B01, declarar V017 canónico y continuar directamente con el ground-truth gate de Results B02; no deberá detener el flujo salvo que aparezca un bloqueo real.

---

## English

The author explicitly approved Results B01 V01 / Section 5.1 after the Managing-AI PASS in D-089. D-090 freezes the approved cumulative candidate identities and authorizes only byte-exact promotion of `ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md` to `article/manuscript/ARTICLE_MASTER_V017.md` with expected Git blob `35edb134f3d060bad4257d314cf415d9ecf17b6c` and SHA-256 `6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318`. V016 remains canonical until that promotion is materialized and independently verified. Results B02 and later sections remain unauthorized.