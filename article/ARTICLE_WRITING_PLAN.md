# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.24
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-105
CANONICAL_MASTER = ARTICLE_MASTER_V019
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V019.md
CANONICAL_MASTER_MD_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
CANONICAL_MASTER_MD_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B04_SECTION_5_4_DRAFTING_V01
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B04_SECTION_5_4 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B04_V01_ONLY
RESULTS_B05_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V019.md` es el master Markdown canónico verificado. B03 V01 fue promovido byte-exactamente y su integración está registrada en D-103.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 54
```

Experimental Design y Results §5.1–§5.3 están cerrados, aprobados, congelados e integrados.

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = OPEN / AUTHORIZED B04 V01
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Results B04 / Section 5.4

Ground truth:

`article/governance/D104_RESULTS_B04_GROUND_TRUTH_SYNC_AND_SECTION5_4_BOUNDARY.md@31c4570d4172fa7c5deb4f7dcfc62a20148b8c84`

Snapshot experimental:

`main@db0d0ad0d8435921a7838db6720eaea86a263763`

El contrato B04 separa dos capas: controles automáticos/estructurales y evaluación cualitativa. Los 50 casos preservan Top-3/order y trazabilidad; las referencias y consistencia de rank son válidas en los 150 candidate slots. No se autoriza una tasa retrospectiva `automatic_validation_pass`. El 0/50 de schema compliance se interpreta exclusivamente bajo el `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` congelado.

La capa cualitativa registra:

```text
AUDITABLE = 28/50 = 56.0%
NON_AUDITABLE = 22/50 = 44.0%
TOTAL_MEAN = 11.72/16
TOTAL_MEDIAN = 12/16
TOTAL_RANGE = 6–15
HARD_VIOLATIONS = 0
EVALUATOR_MODALITY = AI_EXPERT_ROLE / LLM-AS-JUDGE
HUMAN_SCORING = FALSE
```

Los claims C35-C41 fueron incorporados a `article/CLAIM_EVIDENCE_MATRIX.md@fd1af9e0fa27db5f7bb7a2413db800bd0dba9d8b` como `AUTHORIZED` con límites explícitos. C13 permanece `PROHIBITED`; C14 permanece `CONDITIONAL` como claim paraguas.

## 4. Contrato activo

Prompt:

`article/prompts/6_RESULTS_B04_SECTION5_4.md@290d8668f138839cfce11752fc1010e778ddee31`

Git blob:

`98161fb0e606205cc6c429c81765c59b5ade3a23`

Revisión:

`article/reviews/6_RESULTS_B04_SECTION5_4_PROMPT_INTERNAL_REVIEW_V01.md@d4c90480c136a9d3d778ddc125e577d86beaa8aa` — `PASS`.

Autorización:

`article/governance/D105_RESULTS_B04_SECTION5_4_EXECUTION_AUTHORIZATION.md@2b6fc7c117074e69dfdde4b5bc36b9251966281c`.

## 5. Baselines y entrega

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V019.md
BASELINE_MASTER_MD_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
BASELINE_MASTER_MD_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
BASELINE_DOCX_SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

D-035 continúa activo: Base64 manual, chunking, fragmentación y reensamblado están prohibidos. El DOCX no se reconstruye desde Markdown y los candidatos acumulativos deben entregarse como archivos reales.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B04_SECTION_5_4
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B04_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B04_SECTION5_4_RESPONSE_V01.md
EXPECTED_EXIT = RESULTS_B04_V01_COMPLETED_PENDING_GESTORA_AUDIT
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V019 is the canonical verified Markdown master and the approved B03 DOCX is the canonical cumulative Word baseline. Results §5.1–§5.3 are integrated. Results B04 / §5.4 is the only open drafting block under D-104/D-105 and the exact prompt `article/prompts/6_RESULTS_B04_SECTION5_4.md@290d8668f138839cfce11752fc1010e778ddee31`.

```text
CURRENT_GATE = RESULTS_B04_SECTION_5_4_DRAFTING_V01
NEXT_ACTOR = DRAFTING_AI
RESULTS_B04 = AUTHORIZED
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```