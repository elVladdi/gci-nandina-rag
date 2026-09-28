# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.32
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-119
CANONICAL_MASTER = ARTICLE_MASTER_V022
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V022.md
CANONICAL_MASTER_MD_SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
CANONICAL_MASTER_MD_GIT_BLOB = 088eecd537997a3438517f7d206f6d890b0aa064
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B07_V01_AUTHOR_APPROVAL
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B05_SECTION_5_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B06_SECTION_5_6 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B07_SECTION_5_7 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
TARGET_IF_APPROVED = ARTICLE_MASTER_V023
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V022.md` es el master Markdown canónico verificado. Results §5.1–§5.6 están cerrados, aprobados, congelados e integrados.

Results B07 V01 / §5.7 fue ejecutado bajo D-117/D-118 y superó la auditoría independiente de IA Gestora:

`article/reviews/6_RESULTS_B07_SECTION5_7_INTERNAL_REVIEW_V01.md@34d203baf47904e2e16d703c8d5fe6801f3f47ac` — `PASS`.

D-119 abre el gate de aprobación del autor:

`article/governance/D119_RESULTS_B07_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@d9812e89f0515f8d1b6cdc10548330da2d030000`.

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = INTEGRATED
5.5 Sensitivity and robustness analyses   = INTEGRATED
5.6 Inferential results                    = INTEGRATED
5.7 Summary by research question           = GESTORA PASS / PENDING AUTHOR APPROVAL
```

## 3. Objeto exacto de aprobación B07

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.md
SHA256 = d3a54bd263f8f24690fa259eb732e4805515899f0219b6b822b4978e9b985446
GIT_BLOB_EXPECTED = 657c85211323ba60a65d54cccb31edb90c0d18c3

ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.docx
SHA256 = 42803266758c336b83be935c2bd6e2f9d828a4697617d9f8cd0b8bf32da41506
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 60
```

Response y sección:

```text
RESPONSE = article/responses/6_RESULTS_B07_SECTION5_7_RESPONSE_V01.md@a19fa1a8025417d70d26ca6083a4055149528f13
SECTION = article/sections/results/Results_B07_V01.md@0f905016040ef3b14c57114ae453640323c47fc8
SECTION_GIT_BLOB = 30a30ec187613016e8c2cd60ce8c72896d5470d1
```

## 4. Resultado de auditoría

La auditoría confirma que V022→B07 modifica exclusivamente los placeholders inglés y español de §5.7. Cada uno fue sustituido por cuatro párrafos compactos RQ1–RQ4. Todos los resultados, cifras y disposiciones provienen de Results §5.1–§5.6 ya integrados; no se introducen resultados, intervalos, tests, inferencia, causalidad, generalización externa, corrección jurídica, comparación con literatura, novelty, FINAL_GAP, Discussion ni Conclusion nuevos.

El DOCX fue auditado contra el baseline B06: 14/14 partes OOXML preservadas en conjunto, con cambio exclusivo en `word/document.xml`; 40 comentarios, 0 tracked changes y 60 páginas. Los ocho párrafos RQ son textualmente idénticos entre Markdown y Word. El render independiente mostró 54 páginas pixel-identical respecto al baseline y seis páginas nuevas/modificadas sin defectos visuales.

## 5. Regla de promoción si el autor aprueba

La aprobación autorizará únicamente:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V023.md
EXPECTED_SHA256 = d3a54bd263f8f24690fa259eb732e4805515899f0219b6b822b4978e9b985446
EXPECTED_GIT_BLOB = 657c85211323ba60a65d54cccb31edb90c0d18c3
```

V022 seguirá siendo canónico hasta materialización y verificación byte-exacta de V023. El DOCX permanece bajo custodia local del autor. D-035 continúa activo.

Después de integrar B07, Results podrá cerrarse formalmente. Solo entonces IA Gestora podrá decidir y abrir el primer bloque de Discussion; Discussion no queda autorizada por anticipado.

## 6. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_RESULTS_B07_V01
CURRENT_GATE = RESULTS_B07_V01_AUTHOR_APPROVAL
CANONICAL_MASTER_UNTIL_PROMOTION = ARTICLE_MASTER_V022
TARGET_IF_APPROVED = ARTICLE_MASTER_V023
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V022 remains the canonical verified master. Results B07 / Section 5.7 V01 passed the independent Gestora audit and is pending explicit author approval. The audited Markdown candidate has SHA-256 `d3a54bd263f8f24690fa259eb732e4805515899f0219b6b822b4978e9b985446` and expected Git blob `657c85211323ba60a65d54cccb31edb90c0d18c3`; the DOCX candidate has SHA-256 `42803266758c336b83be935c2bd6e2f9d828a4697617d9f8cd0b8bf32da41506`, with 40 comments, zero tracked changes, and 60 pages.

```text
CURRENT_GATE = RESULTS_B07_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
RESULTS_B07 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
TARGET_IF_APPROVED = ARTICLE_MASTER_V023
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```