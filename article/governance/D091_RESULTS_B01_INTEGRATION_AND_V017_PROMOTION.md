# D-091 — Integración de Results B01 y promoción de V017 / Results B01 integration and V017 promotion

## Español

```text
DECISION_ID = D-091
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-090
PHASE = RESULTS
BLOCK = RESULTS_B01_SECTION_5_1
ARTICLE_MASTER_V017 = CANONICAL / VERIFIED
RESULTS_B01_STATE = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_PLUS = NOT_AUTHORIZED_BY_THIS_DECISION
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Verificación de la promoción

IA Gestora verificó directamente en GitHub la materialización del target autorizado por D-090:

```text
TARGET = article/manuscript/ARTICLE_MASTER_V017.md
OBSERVED_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
EXPECTED_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
VERDICT = PASS / BYTE_EXACT
```

La identidad Git blob observada coincide exactamente con el blob congelado del candidato aprobado `ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md`. Por identidad byte-exacta se conserva el SHA-256 aprobado:

```text
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V017.md
CANONICAL_MASTER_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
CANONICAL_MASTER_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
```

## 2. Word acumulativo canónico

Tras la promoción verificada, el Word acumulativo aprobado de B01 pasa a ser el baseline Word canónico bajo custodia local del autor:

```text
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

No se reconstruye el DOCX desde Markdown.

## 3. Cierre de B01

Results B01 / Section 5.1 queda definitivamente cerrado, aprobado, congelado e integrado. La sección reporta únicamente composición del benchmark, controles cross-partition, soporte histórico nominal y similitud textual residual conforme al ground truth D-087.

## 4. Gate

```text
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V017
CURRENT_DRAFTING_PHASE = RESULTS
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = SYNCHRONIZE_RESULTS_B02_GROUND_TRUTH_AND_PREPARE_SEPARATE_GATE
RESULTS_B02_PLUS = NOT_AUTHORIZED_UNTIL_SEPARATE_DECISION
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

The byte-exact promotion authorized by D-090 was independently verified. `article/manuscript/ARTICLE_MASTER_V017.md` has Git blob `35edb134f3d060bad4257d314cf415d9ecf17b6c`, exactly matching the approved B01 cumulative candidate. V017 is therefore canonical, and Results B01 / Section 5.1 is closed, approved, frozen, and integrated. The canonical cumulative DOCX is `ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx`, SHA-256 `f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f`, under local author custody. B02 requires a separate ground-truth and authorization gate.