# D-088 — Autorización de ejecución Results B01 / Section 5.1

## Español

```text
DECISION_ID = D-088
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-087
PHASE = RESULTS
BLOCK = RESULTS_B01_SECTION_5_1
PROMPT = article/prompts/6_RESULTS_B01_SECTION5_1.md@cc75fb9b732de6b9162cf90b8eacb8462372405e
PROMPT_GIT_BLOB = a0f4005e8c406574d39b5540dfbf676f3d4acc0d
PROMPT_REVIEW = article/reviews/6_RESULTS_B01_SECTION5_1_PROMPT_INTERNAL_REVIEW_V01.md@275c6e14d7d3eab0ada488e829dcd07f8b1254df
PROMPT_REVIEW_RESULT = PASS
RESULTS_B01 = AUTHORIZED_FOR_DRAFTING_UNDER_PROMPT_ONLY
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Autorización

Se autoriza a IA de Redacción a ejecutar exclusivamente Results B01 / Section 5.1 — Data and partition checks conforme al prompt exacto indicado arriba.

La autorización queda limitada al ground truth congelado por D-087. No puede ampliarse por inferencia a candidate-retrieval performance, documentary evidence, controlled explanation, sensibilidad, inferencia, disposiciones HE2/HE5, Discussion ni secciones posteriores.

## 2. Baselines obligatorios

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V016.md
BASELINE_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
BASELINE_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
BASELINE_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

## 3. Salida esperada

```text
SECTION_ARTIFACT = article/sections/results/Results_B01_V01.md
CUMULATIVE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md
CUMULATIVE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
RESPONSE = article/responses/6_RESULTS_B01_SECTION5_1_RESPONSE_V01.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
```

D-035 continúa vinculante. Los candidatos acumulativos deben entregarse como archivos reales; Base64 manual, chunking, fragmentación, reensamblado y reconstrucción DOCX desde Markdown están prohibidos.

## 4. Gate

```text
CURRENT_GATE = RESULTS_B01_SECTION_5_1_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B01_PROMPT
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

D-088 authorizes only Results B01 / Section 5.1 under `article/prompts/6_RESULTS_B01_SECTION5_1.md@cc75fb9b732de6b9162cf90b8eacb8462372405e`. The exact V016 Markdown and B07 V02 DOCX baselines are mandatory. No other Results subsection or later article section is authorized. D-035 timeout-safe handoff remains binding.