# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.28
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-111
CANONICAL_MASTER = ARTICLE_MASTER_V020
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V020.md
CANONICAL_MASTER_MD_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
CANONICAL_MASTER_MD_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B05_V01_AUTHOR_APPROVAL
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B05_SECTION_5_5 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
RESULTS_B06_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = OPEN
TARGET_IF_APPROVED = ARTICLE_MASTER_V021
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V020.md` continúa siendo el master canónico verificado. Results §5.1–§5.4 están cerrados, aprobados, congelados e integrados.

Results B05 / §5.5 V01 fue ejecutado bajo D-109/D-110 y superó la auditoría independiente de IA Gestora. La revisión formal es:

`article/reviews/6_RESULTS_B05_SECTION5_5_INTERNAL_REVIEW_V01.md@ccac96ffee0c6a06c6dd8ccc56e07e646fd81d7a` — `PASS`.

D-111 abre el gate de aprobación del autor:

`article/governance/D111_RESULTS_B05_V01_AUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@49b9b682f27d3b4ab1eba29abb7dd9e567a832f6`.

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = INTEGRATED
5.5 Sensitivity and robustness analyses   = GESTORA PASS / PENDING AUTHOR APPROVAL
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Objeto exacto de aprobación B05

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.md
SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
GIT_BLOB_EXPECTED = e76b5b1789de1f82c9623dd6543c38ae639715b0

ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 57
```

Respuesta y sección:

```text
RESPONSE = article/responses/6_RESULTS_B05_SECTION5_5_RESPONSE_V01.md@53419aca4b7805733a3c804512eb757764c2acae
SECTION = article/sections/results/Results_B05_V01.md@bebe259868921a4f04539418b5f4a934d92ee44d
SECTION_GIT_BLOB = 28a230219a60f84951e8c3dd658c451809e6f9ad
```

## 4. Resultado de la auditoría

El diff Markdown frente a V020 modifica exclusivamente los placeholders EN/ES de §5.5. Las cifras EXP11A, EXP11B, 0B-05C y HE5 coinciden con las fuentes congeladas; no se filtró contenido inferencial HE2 de §5.6. EXP11A conserva la lectura conjunta tamaño/composición, EXP11B permanece descriptivo sin superpoblación de seeds, la sensibilidad 0B-05C se reporta como dependiente del método y HE5 permanece `INCONCLUSIVE` con EXP12 y descripción-quality no estimables.

En Word, solo cambió `word/document.xml`; comentarios, relaciones, estilos y demás partes OOXML permanecen byte-identical. Se preservan 40 comentarios y 0 tracked changes. El documento renderizado tiene 57 páginas sin clipping, superposición ni truncamiento. La equivalencia Markdown↔DOCX y EN↔ES es `PASS`.

## 5. Regla de promoción si el autor aprueba

La aprobación autorizará únicamente:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V021.md
EXPECTED_SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
EXPECTED_GIT_BLOB = e76b5b1789de1f82c9623dd6543c38ae639715b0
```

V020 seguirá siendo canónico hasta la materialización y verificación byte-exacta de V021. D-035 continúa activo: no se permite Base64 manual, chunking, fragmentación o reensamblado como workaround. El DOCX permanece bajo custodia local del autor.

## 6. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_RESULTS_B05_V01
CURRENT_GATE = RESULTS_B05_V01_AUTHOR_APPROVAL
CANONICAL_MASTER_UNTIL_PROMOTION = ARTICLE_MASTER_V020
TARGET_IF_APPROVED = ARTICLE_MASTER_V021
RESULTS_B06_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V020 remains the canonical verified master. Results B05 / Section 5.5 V01 passed the independent Gestora audit and is pending explicit author approval. The audited Markdown candidate has SHA-256 `a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06` and expected Git blob `e76b5b1789de1f82c9623dd6543c38ae639715b0`; the DOCX candidate has SHA-256 `3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70`, with 40 preserved comments and zero tracked changes.

```text
CURRENT_GATE = RESULTS_B05_V01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
RESULTS_B05 = GESTORA_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
TARGET_IF_APPROVED = ARTICLE_MASTER_V021
RESULTS_B06_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
