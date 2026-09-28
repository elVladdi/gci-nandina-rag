# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.37
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-130
CANONICAL_MASTER = ARTICLE_MASTER_V025
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V025.md
CANONICAL_MASTER_MD_SHA256 = a805cd220904fb4972d0db59764425aff87a49c8ec1cd34936e85913778feee5
CANONICAL_MASTER_MD_GIT_BLOB = 829a6f5df87cf91dcafe89c48c1afd48ddbd2faf
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cc8f765bc197acbb210ebcb01da104ebd282481013d549ca51c8cf80268786c7
CANONICAL_CITATION_COMMENTS = 44
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B03_SECTION_6_3 = OPEN / AUTHORIZED_FOR_DRAFTING
CURRENT_GATE = DISCUSSION_B03_SECTION_6_3_DRAFTING_V01
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B04_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V025.md` es el master Markdown canónico verificado. Results §5.1–§5.7 y Discussion §6.1–§6.2 están cerrados, aprobados, congelados e integrados.

La promoción B02 a V025 fue byte-exacta y está registrada en:

`article/governance/D128_DISCUSSION_B02_AUTHOR_APPROVAL_V025_VERIFICATION_AND_INTEGRATION.md@a91377adb3b09027a1b0f894ff1875091bc96536`.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx
SHA256 = cc8f765bc197acbb210ebcb01da104ebd282481013d549ca51c8cf80268786c7
COMMENTS = 44
TRACKED_CHANGES = 0
PAGE_COUNT = 62
```

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = INTEGRATED
6.3 Comparison with prior work                             = AUTHORIZED B03 V01
6.4 Implications for auditable decision support            = NOT AUTHORIZED
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Discussion B03 / Section 6.3

Boundary:

`article/governance/D129_DISCUSSION_B03_SECTION6_3_INTERPRETIVE_BOUNDARY_AND_LITERATURE_TRACE.md@03222ca5666de2a408bd3131e22c1bd56e85dd36`

Prompt:

`article/prompts/7_DISCUSSION_B03_SECTION6_3.md@2203f81bfb3020219aac9c32e4605b357fa8cf81`

Git blob:

`c30bf7bca82e66b3fd8cd26d8463b686a681a37f`

Revisión:

`article/reviews/7_DISCUSSION_B03_SECTION6_3_PROMPT_INTERNAL_REVIEW_V01.md@03fac8bded59a495c5c1d72d126aded0fab15bff` — `PASS`.

Autorización:

`article/governance/D130_DISCUSSION_B03_SECTION6_3_EXECUTION_AUTHORIZATION.md@156521548817b30dec11171926876f16477db358`.

## 4. Contrato científico B03

§6.3 compara prior work por autoridad y secuenciación de componentes, no por porcentajes de desempeño. Las fuentes autorizadas son Lee et al. (2021), Lee et al. (2023), Marra de Artiñano et al. (2023) y Kim et al. (2025).

Lee et al. (2023) debe reconocerse como prior art cercano de candidate prediction seguida de evidence retrieval. El presente estudio puede posicionarse por el contrato operativo explícito: historical retrieval fija el Top-3 antes de documentary evidence; las etapas downstream no pueden modificar membership ni orden; y candidate retrieval, documentary association y controlled explanation se evalúan como objetos separados.

Ese posicionamiento no autoriza novelty, first-ever, state-of-the-art, superioridad global, causalidad, cross-study numerical superiority, legal correctness ni external generalization.

## 5. Política Word y citas

El baseline Word tiene 44 comentarios. B03 debe introducir exactamente cuatro nuevas citas en la Parte I inglesa —una para cada fuente autorizada— y cuatro nuevos comentarios de fuente. El candidato esperado debe contener:

```text
COMMENTS = 48
TRACKED_CHANGES = 0
```

Los 44 comentarios heredados deben preservarse sin modificación. D-035 continúa activo y Word no debe reconstruirse desde Markdown.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_DISCUSSION_B03_SECTION_6_3
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V025.md
BASELINE_MASTER_MD_SHA256 = a805cd220904fb4972d0db59764425aff87a49c8ec1cd34936e85913778feee5
BASELINE_MASTER_MD_GIT_BLOB = 829a6f5df87cf91dcafe89c48c1afd48ddbd2faf
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx
BASELINE_DOCX_SHA256 = cc8f765bc197acbb210ebcb01da104ebd282481013d549ca51c8cf80268786c7
EXPECTED_COMMENTS = 48
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx
EXPECTED_SECTION = article/sections/discussion/Discussion_B03_V01.md
EXPECTED_RESPONSE = article/responses/7_DISCUSSION_B03_SECTION6_3_RESPONSE_V01.md
EXPECTED_EXIT = DISCUSSION_B03_V01_COMPLETED_PENDING_GESTORA_AUDIT
DISCUSSION_B04_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V025 is canonical and verified. Discussion Sections 6.1–6.2 are integrated. Discussion B03 / Section 6.3 is the only open drafting block. It must compare prior work only by component authority and sequencing, using Lee et al. (2021), Lee et al. (2023), Marra de Artiñano et al. (2023), and Kim et al. (2025). Candidate prediction plus evidence retrieval must be acknowledged as prior art. Exactly four new English citation comments are authorized, taking the cumulative Word total from 44 to 48. No Section 6.4+, Conclusion, novelty, first-ever, state-of-the-art, cross-study numerical superiority, legal-correctness, or external-generalization claim is authorized.

```text
CURRENT_GATE = DISCUSSION_B03_SECTION_6_3_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
DISCUSSION_B03 = AUTHORIZED
DISCUSSION_B04_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```