# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.9
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-081
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V015.md
CANONICAL_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = B07_V01_AUTHOR_APPROVAL
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B05 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B06 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B07 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
SECTION_4_8 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN_FOR_B07_V01_ONLY
B07_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Política acumulativa

`ARTICLE_MASTER_V015.md` continúa como master Markdown canónico verificado mientras B07 V01 se encuentra ante el autor. El Word acumulativo canónico sigue siendo `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx` hasta una eventual aprobación e integración de B07.

MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035 y las decisiones editoriales activas permanecen vinculantes. Un `PASS` de IA Gestora no equivale a aprobación del autor ni a integración.

## 2. Estado de construcción de Experimental Design

| Bloque | Estado |
|---|---|
| B01 / 4.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B02 / 4.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B03 / 4.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B04 / 4.5 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B05 / 4.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B06 / 4.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| ARTICLE_MASTER_V015 | CANONICAL / VERIFIED |
| B07 / 4.8 | DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 3. B07 / Section 4.8 — entrega auditada

Response de ejecución:

`article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V01.md@c897204c1df5b591ff2c7742c53caa24baaf3b92`

Artefacto de sección:

`article/sections/experimental_design/Experimental_Design_B07_V01.md@c3cc9971f7d2aaebd629b07cad235e8efa3ee526`

Auditoría Gestora:

`article/reviews/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_INTERNAL_REVIEW_V01.md@2cb6473345077ed66f453e5963d2d08146ce59cc` — `PASS`.

Decisión vigente:

`article/governance/D081_EXPERIMENTAL_DESIGN_B07_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@6bdff70a4371ff0556eb1c492ffb43670ae22a30`.

### 3.1 Candidatos exactos sometidos al autor

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md
SHA256 = a2a7e5527bf69cebab1e6ab3d36a95dd16b5ceac34862038f7fff4ef38d3db12
GIT_BLOB = 0d8a4ad3dd03c5b69feeec6a5710d296a5a76662

ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx
SHA256 = dc51307ed3ca6918dd1c43de67d366e82121a5f5ed047ccf542d4f400b0abf6c
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_RENDER = PASS / 51 OF 51 PAGES
VISUAL_QA = PASS
```

### 3.2 Resultado científico/editorial

B07 V01 conserva el estado real del repositorio público auditado: documentación, contratos y configuración de ejemplo materializados, pero sin una release computacional completa de referencia. Mantiene las fronteras C15/C16/C17 y distingue recursos materializados, planificados y restringidos.

No introduce Results ni afirmaciones de reproducción one-command/fresh-clone, disponibilidad pública de datos administrativos, generalización empírica o corrección jurídica.

### 3.3 Timeout-safe handoff

El autor informó que una primera ejecución cayó en timeout. Para la segunda ejecución, D-035 quedó activado y la auditoría concluyó `PASS`: el master Markdown grande no se materializó directamente en GitHub, el DOCX tampoco se subió al repositorio, no se observaron artefactos de chunking/Base64/reensamblado y los candidatos exactos fueron entregados como archivos reales con hashes coincidentes.

## 4. Gate autoral

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_B07_V01_OR_REQUEST_CHANGES
AUTHOR_APPROVAL_GATE = OPEN_FOR_B07_V01_ONLY
B07_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
```

Una eventual aprobación de B07 cerrará el contenido de Section 4 — Experimental design, pero no abrirá automáticamente Results. La promoción V016 deberá materializarse y verificarse byte-exactamente antes de cualquier gate posterior.

---

# English

## 1. Current cumulative state

`ARTICLE_MASTER_V015.md` remains the verified canonical Markdown master. B01–B06 are closed, approved, frozen, and integrated. B07 V01 has passed the independent Managing-AI audit and is pending explicit author approval.

## 2. Exact B07 candidates

```text
B07_MD_SHA256 = a2a7e5527bf69cebab1e6ab3d36a95dd16b5ceac34862038f7fff4ef38d3db12
B07_MD_GIT_BLOB = 0d8a4ad3dd03c5b69feeec6a5710d296a5a76662
B07_DOCX_SHA256 = dc51307ed3ca6918dd1c43de67d366e82121a5f5ed047ccf542d4f400b0abf6c
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_RENDER = PASS / 51 OF 51 PAGES
```

The Section 4.8 text accurately preserves the public-repository state and the boundaries between materialized, planned, and restricted resources, as well as between reference reproduction and external replication. It does not claim empirical generalization or complete fresh-clone reproduction.

The author-reported prior timeout activated D-035. The second execution followed the timeout-safe delivery path and the exact MD/DOCX candidates were received and verified.

## 3. Gate

```text
CURRENT_GATE = B07_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
B07_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
