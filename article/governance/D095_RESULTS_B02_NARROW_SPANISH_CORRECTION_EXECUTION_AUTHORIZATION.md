# D-095 — Autorización de corrección estrecha de Results B02 / Spanish mirror

## Español

```text
DECISION_ID = D-095
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-094
PHASE = RESULTS
BLOCK = RESULTS_B02_SECTION_5_2
CORRECTION_PROMPT = article/prompts/6_RESULTS_B02_V01_NARROW_SPANISH_NATURALNESS_CORRECTION.md@f8286d6b9ccd797057f47f6b200f7b20adec3359
CORRECTION_PROMPT_GIT_BLOB = e2477447f6eb6eb46a3a82270158109d7e5c87f1
PROMPT_REVIEW = article/reviews/6_RESULTS_B02_NARROW_SPANISH_CORRECTION_PROMPT_REVIEW_V01.md@36b6787d06af7afbcc0615bdf6ccc624a1760009
PROMPT_REVIEW_RESULT = PASS
RESULTS_B02_V02 = AUTHORIZED_FOR_NARROW_CORRECTION_ONLY
AUTHOR_APPROVAL_GATE = CLOSED
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Autorización

Se autoriza a IA de Redacción a ejecutar exclusivamente el prompt correctivo indicado arriba y producir Results B02 V02.

La autorización se limita a las tres sustituciones de naturalidad congeladas por D-094 dentro del espejo español de §5.2. El contenido científico y numérico de B02 V01 queda congelado durante esta corrección.

## 2. Baselines exactos

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.md
BASELINE_MD_SHA256 = 87b85f095e0cef6d6f9b12e70223596b563014a38bcacfa37c4e0448a66dad6c
BASELINE_MD_GIT_BLOB_EXPECTED_FROM_BYTES = 804ae5709f08e878202f48465d4671bf70dc15c7

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.docx
BASELINE_DOCX_SHA256 = c267f7da5415161b812aed10cef66929b6b6cd2be51ecb2196d43c2e1180ce6f
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

## 3. Gate

```text
CURRENT_GATE = RESULTS_B02_V02_NARROW_CORRECTION_EXECUTION
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_CORRECTION_PROMPT
EXPECTED_RESPONSE = article/responses/6_RESULTS_B02_SECTION5_2_RESPONSE_V02.md
EXPECTED_SECTION = article/sections/results/Results_B02_V02.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
RESULTS_B03_PLUS = NOT_AUTHORIZED
```

Tras recibir V02, IA Gestora deberá auditar diferencialmente la corrección. Solo un `PASS` posterior podrá abrir el gate de aprobación autoral de B02.

---

## English

D-095 authorizes only the narrow Spanish-mirror correction defined by the exact reviewed prompt. No scientific, numerical, English-text, or later-section changes are authorized. Results B03+ remain closed.