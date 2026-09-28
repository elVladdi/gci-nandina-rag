# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.30
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-115
CANONICAL_MASTER = ARTICLE_MASTER_V021
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V021.md
CANONICAL_MASTER_MD_SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
CANONICAL_MASTER_MD_GIT_BLOB = e76b5b1789de1f82c9623dd6543c38ae639715b0
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B06_V01_AUTHOR_APPROVAL
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B05_SECTION_5_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B06_SECTION_5_6 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
RESULTS_B07_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = OPEN
TARGET_IF_APPROVED = ARTICLE_MASTER_V022
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V021.md` es el master Markdown canónico verificado. Results §5.1–§5.5 están cerrados, aprobados, congelados e integrados.

Results B06 V01 / §5.6 fue ejecutado bajo D-113/D-114 y superó la auditoría independiente de IA Gestora:

`article/reviews/6_RESULTS_B06_SECTION5_6_INTERNAL_REVIEW_V01.md@5dd4f0b4632b81acb3c713a2c22732582675cd53` — `PASS`.

D-115 abre el gate de aprobación del autor:

`article/governance/D115_RESULTS_B06_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@deeeb80f57d9fef093730df42a04b050da915c2a`.

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = INTEGRATED
5.5 Sensitivity and robustness analyses   = INTEGRATED
5.6 Inferential results                    = GESTORA PASS / PENDING AUTHOR APPROVAL
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Objeto exacto de aprobación B06

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md
SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
GIT_BLOB_EXPECTED = 088eecd537997a3438517f7d206f6d890b0aa064

ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 58
```

Respuesta y sección:

```text
RESPONSE = article/responses/6_RESULTS_B06_SECTION5_6_RESPONSE_V01.md@e7e9ab0efb137243471bd0dc1feb4363b9b1c7d7
SECTION = article/sections/results/Results_B06_V01.md@cbb5cafdf3c9725c0d0caefa565ba694ead93349
SECTION_GIT_BLOB = 092e8f9af2cd96ac7d6ad41f193bd7486ec40938
```

## 4. Resultado de la auditoría

La auditoría confirmó que V021→B06 modifica exclusivamente los placeholders ingleses y españoles de §5.6. Los 15 contrastes primarios HE2_A y el contraste HE2_B coinciden con los artefactos inferenciales congelados y con D-113. Los 15 intervalos primarios permanecen completamente por encima de cero; HE2_B usa el contraste `Recall@200 - Recall@100 = 0.202651515`, 95% CI `[0.066763106, 0.341601308]`.

El bloque conserva `HE2 = SUPPORTED` exclusivamente dentro del alcance inferencial interno congelado y `HE5 = INCONCLUSIVE`. No introduce p-values, nuevas pruebas o intervalos, causalidad, generalización externa, accuracy global del framework ni corrección jurídica.

El DOCX fue auditado contra el baseline B05: 14/14 partes OOXML idénticas en conjunto, con cambio exclusivo en `word/document.xml`; 40 comentarios, 0 tracked changes y 58 páginas renderizadas sin defectos. Markdown↔DOCX y EN↔ES son `PASS`.

## 5. Regla de promoción si el autor aprueba

La aprobación autorizará únicamente:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V022.md
EXPECTED_SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
EXPECTED_GIT_BLOB = 088eecd537997a3438517f7d206f6d890b0aa064
```

V021 seguirá siendo canónico hasta la materialización y verificación byte-exacta de V022. El DOCX permanece bajo custodia local del autor. D-035 continúa activo.

Después de integrar B06, IA Gestora evaluará expresamente si §5.7 mejora la legibilidad o resulta redundante. La estructura congelada define §5.7 como opcional; no debe redactarse automáticamente antes de esa decisión.

## 6. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_RESULTS_B06_V01
CURRENT_GATE = RESULTS_B06_V01_AUTHOR_APPROVAL
CANONICAL_MASTER_UNTIL_PROMOTION = ARTICLE_MASTER_V021
TARGET_IF_APPROVED = ARTICLE_MASTER_V022
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V021 remains the canonical verified master. Results B06 / Section 5.6 V01 passed the independent Gestora audit and is pending explicit author approval. The audited Markdown candidate has SHA-256 `56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795` and expected Git blob `088eecd537997a3438517f7d206f6d890b0aa064`; the DOCX candidate has SHA-256 `46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79`, with 40 comments, zero tracked changes, and 58 pages.

```text
CURRENT_GATE = RESULTS_B06_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
RESULTS_B06 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
TARGET_IF_APPROVED = ARTICLE_MASTER_V022
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```