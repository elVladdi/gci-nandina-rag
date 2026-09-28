# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.27
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-110
CANONICAL_MASTER = ARTICLE_MASTER_V020
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V020.md
CANONICAL_MASTER_MD_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
CANONICAL_MASTER_MD_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B05_SECTION_5_5_DRAFTING_V01
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B05_SECTION_5_5 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B05_V01_ONLY
RESULTS_B06_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V020.md` es el master Markdown canónico verificado. Results §5.1–§5.4 están cerrados, aprobados, congelados e integrados.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 54
```

B04 fue promovido byte-exactamente a V020 y su integración está registrada en D-108.

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = INTEGRATED
5.5 Sensitivity and robustness analyses   = OPEN / AUTHORIZED B05 V01
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Results B05 / Section 5.5

Ground truth:

`article/governance/D109_RESULTS_B05_GROUND_TRUTH_SYNC_AND_SECTION5_5_BOUNDARY.md@8709d3fa886e720888ea8a1fd5385ecfc0dc59a3`

Snapshot experimental:

`main@db0d0ad0d8435921a7838db6720eaea86a263763`

El contrato B05 congela cuatro familias descriptivas:

1. sensibilidad conjunta tamaño/composición de banco histórico H25/H50/H75 con H100 como referencia;
2. sensibilidad pareada H150/H200 en diez seeds, todos sobre el mismo EVAL de 1,056 series;
3. sensibilidad correctiva final 0B-05C Attempt06, cuya respuesta es dependiente del método;
4. resultados descriptivos y no-estimabilidad HE5.

EXP11A no identifica un efecto causal aislado del tamaño. EXP11B no autoriza inferencia a superpoblación de seeds ni trata las filas repetidas del mismo EVAL como independientes. EXP12 diversity y la prevalencia de descripciones ambiguas/incompletas siguen `NOT_ESTIMABLE`. HE5 permanece `INCONCLUSIVE`.

Los intervalos inferenciales, bootstrap por DAM y disposición HE2 se reservan para §5.6.

## 4. Contrato activo

Prompt:

`article/prompts/6_RESULTS_B05_SECTION5_5.md@b6a0973bd2e9337d7c79132ca73cd9c05d8ba7da`

Git blob:

`d2dd98fb21982078b7d92539f6cc630c342647e7`

Revisión:

`article/reviews/6_RESULTS_B05_SECTION5_5_PROMPT_INTERNAL_REVIEW_V01.md@edac2f1276c4c42dd7a9000820e4a4ed18a2c0ed` — `PASS`.

Autorización:

`article/governance/D110_RESULTS_B05_SECTION5_5_EXECUTION_AUTHORIZATION.md@6442eb48dedd1af796852407f89ddddfd30db782`.

## 5. Baselines y entrega

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V020.md
BASELINE_MASTER_MD_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
BASELINE_MASTER_MD_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
BASELINE_DOCX_SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

D-035 continúa activo: Base64 manual, chunking, fragmentación y reensamblado están prohibidos. El DOCX no se reconstruye desde Markdown y los candidatos acumulativos deben entregarse como archivos reales.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B05_SECTION_5_5
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B05_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B05_SECTION5_5_RESPONSE_V01.md
EXPECTED_EXIT = RESULTS_B05_V01_COMPLETED_PENDING_GESTORA_AUDIT
RESULTS_B06_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V020 is the canonical verified Markdown master and the approved B04 DOCX is the canonical cumulative Word baseline. Results §5.1–§5.4 are integrated. Results B05 / §5.5 is the only open drafting block under D-109/D-110 and the exact prompt `article/prompts/6_RESULTS_B05_SECTION5_5.md@b6a0973bd2e9337d7c79132ca73cd9c05d8ba7da`.

```text
CURRENT_GATE = RESULTS_B05_SECTION_5_5_DRAFTING_V01
NEXT_ACTOR = DRAFTING_AI
RESULTS_B05 = AUTHORIZED
RESULTS_B06_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```