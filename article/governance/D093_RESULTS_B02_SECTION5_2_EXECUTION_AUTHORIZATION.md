# D-093 — Autorización de ejecución Results B02 / Section 5.2

## Español

```text
DECISION_ID = D-093
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-092
PHASE = RESULTS
BLOCK = RESULTS_B02_SECTION_5_2
PROMPT = article/prompts/6_RESULTS_B02_SECTION5_2.md@76045bc1e408298b3e86de11f0598500f7dfa24f
PROMPT_GIT_BLOB = 0fd0aa40419b248e5983f0cb445c187e92a4bc13
PROMPT_REVIEW = article/reviews/6_RESULTS_B02_SECTION5_2_PROMPT_INTERNAL_REVIEW_V01.md@f0ed6c555275afff6e094d1b91ecef56e642b476
PROMPT_REVIEW_RESULT = PASS
RESULTS_B02 = AUTHORIZED_FOR_DRAFTING_UNDER_PROMPT_ONLY
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Autorización

Se autoriza a IA de Redacción a ejecutar exclusivamente Results B02 / Section 5.2 — Candidate retrieval performance conforme al prompt exacto indicado arriba.

La autorización queda limitada al ground truth descriptivo congelado por D-092. No puede ampliarse a inferencia, HE2 disposition, sensibilidades, documentary evidence, controlled explanation, Discussion ni secciones posteriores.

## 2. Baselines obligatorios

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V017.md
BASELINE_MASTER_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
BASELINE_MASTER_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
BASELINE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

## 3. Salida esperada

```text
SECTION_ARTIFACT = article/sections/results/Results_B02_V01.md
CUMULATIVE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.md
CUMULATIVE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.docx
RESPONSE = article/responses/6_RESULTS_B02_SECTION5_2_RESPONSE_V01.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
```

D-035 continúa vinculante. Los candidatos acumulativos deben entregarse como archivos reales; Base64 manual, chunking, fragmentación, reensamblado y reconstrucción DOCX desde Markdown están prohibidos.

## 4. Gate

```text
CURRENT_GATE = RESULTS_B02_SECTION_5_2_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B02_PROMPT
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

D-093 authorizes only Results B02 / Section 5.2 under `article/prompts/6_RESULTS_B02_SECTION5_2.md@76045bc1e408298b3e86de11f0598500f7dfa24f`. The exact V017 Markdown and B01 V01 DOCX baselines are mandatory. No inferential result, HE2 disposition, sensitivity result, later Results subsection or later manuscript section is authorized. D-035 remains binding.