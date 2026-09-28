# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.45
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-143
CANONICAL_MASTER = ARTICLE_MASTER_V027
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V027.md
CANONICAL_MASTER_MD_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
CANONICAL_MASTER_MD_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0
CANONICAL_DOCX_PAGE_COUNT = 66
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B03_SECTION_6_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B04_SECTION_6_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B05_SECTION_6_5 = V01_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
DISCUSSION_B05_EXECUTION_RESPONSE = article/responses/7_DISCUSSION_B05_SECTION6_5_RESPONSE_V01.md@c8568c6e2a97e166e3d80e1d705a04bc48e6d60a
DISCUSSION_B05_BLOCK = article/sections/discussion/Discussion_B05_V01.md@ec6bec9020ff51fe3c821e2607b86859fe38bf1e
DISCUSSION_B05_INTERNAL_REVIEW = article/reviews/7_DISCUSSION_B05_SECTION6_5_INTERNAL_REVIEW_V01.md@e32e569d842e07ec79b27ab6e762cf7e92fc90b1
DISCUSSION_B05_INTERNAL_REVIEW_RESULT = PASS
DISCUSSION_B05_AUTHOR_GATE = D-143
B05_V01_CANDIDATE_MD_SHA256 = c154257a2c203e580372dd404df875ef808c325947ce580171e2e306961e568e
B05_V01_CANDIDATE_MD_GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
B05_V01_CANDIDATE_DOCX_SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
B05_V01_CANDIDATE_DOCX_COMMENTS = 48
B05_V01_CANDIDATE_DOCX_TRACKED_CHANGES = 0
B05_V01_CANDIDATE_DOCX_PAGE_COUNT = 67
PLANNED_PROMOTION_IF_APPROVED = article/manuscript/ARTICLE_MASTER_V028.md
PLANNED_PROMOTION_EXPECTED_SHA256 = c154257a2c203e580372dd404df875ef808c325947ce580171e2e306961e568e
PLANNED_PROMOTION_EXPECTED_GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
CURRENT_GATE = DISCUSSION_B05_V01_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
NEXT_ACTOR = AUTHOR
LEGACY_EDITORIAL_DEBT = DISCUSSION_B02_INTERNAL_TERMINOLOGY_HYGIENE
DISCUSSION_B06 = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V027.md` permanece como master Markdown canónico. Results §5.1–§5.7 y Discussion §6.1–§6.4 están cerrados, aprobados, congelados e integrados.

El Word acumulativo canónico permanece, hasta aprobación de B05:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx
SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 66
```

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = INTEGRATED / LEGACY EDITORIAL DEBT LOGGED
6.3 Comparison with prior work                             = INTEGRATED
6.4 Implications for auditable decision support            = INTEGRATED
6.5 Configurability and transfer conditions                = V01 AUDITED / PASS / PENDING AUTHOR APPROVAL
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Auditoría B05 V01

IA Redacción ejecutó §6.5 bajo D-141/D-142. IA Gestora reaudita el bloque bajo MWDP, SPCCR, KBS_EWG_34_V01 y D-136 y emite `PASS` sin correcciones obligatorias.

La revisión sustantiva confirma que la sección:

- trata configurabilidad como reinstanciación condicional, no como generalización empírica;
- preserva la autoridad de componentes y las interfaces necesarias;
- no transfiere resultados Chapter 87 ni métricas a otras instancias;
- separa compatibilidad documental de vigencia, autoridad y corrección jurídica;
- distingue reproducción de referencia de replicación externa;
- no introduce nueva literatura, citas, resultados, inferencias ni claims prohibidos;
- evita terminología interna de gobernanza/QA en §6.5 y mantiene prosa concreta y reader-facing;
- conserva equivalencia semántica EN/ES.

La revisión técnica confirma:

```text
CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.md
SHA256 = c154257a2c203e580372dd404df875ef808c325947ce580171e2e306961e568e
GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69

CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx
SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 67

MARKDOWN_CHANGED_HUNKS = 2 / SECTION_6_5_EN_ES_ONLY
OOXML_CHANGED_PARTS = word/document.xml ONLY
MD_DOCX_SECTION_6_5_EQUIVALENCE = PASS / EXACT_TEXT
FULL_DOCX_RENDER = PASS
```

Review:

`article/reviews/7_DISCUSSION_B05_SECTION6_5_INTERNAL_REVIEW_V01.md@e32e569d842e07ec79b27ab6e762cf7e92fc90b1`.

D-143 abre el gate autoral. V027 permanece canónico hasta aprobación expresa y verificación byte-exact de una eventual V028.

## 4. Promoción prevista si el autor aprueba

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.md
TARGET = article/manuscript/ARTICLE_MASTER_V028.md
EXPECTED_SHA256 = c154257a2c203e580372dd404df875ef808c325947ce580171e2e306961e568e
EXPECTED_GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
EXPECTED_CANONICAL_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx
EXPECTED_CANONICAL_DOCX_SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
```

## 5. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_DISCUSSION_B05_V01
CURRENT_GATE = DISCUSSION_B05_V01_AUTHOR_APPROVAL
CANONICAL_MASTER = ARTICLE_MASTER_V027
DISCUSSION_B06 = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

La deuda editorial heredada de §6.2 permanece fuera del scope de B05 y sigue pendiente de un gate transversal controlado antes del freeze final.

---

# English

V027 remains canonical. Results §5.1–§5.7 and Discussion §6.1–§6.4 are integrated. Discussion B05 V01 passed substantive-editorial and technical audit and is pending explicit author approval.

```text
PLAN_VERSION = V3.45
DISCUSSION_B05 = V01_AUDITED / PASS / PENDING_AUTHOR_APPROVAL
CURRENT_GATE = DISCUSSION_B05_V01_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
NEXT_ACTOR = AUTHOR
DISCUSSION_B06 = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

If the author approves B05 V01, the planned promotion target is `article/manuscript/ARTICLE_MASTER_V028.md` with Git blob `a261d0909cf64cb5554bf4e40d68cbcaf11aaf69`. Promotion remains a separate verification step.