# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.29
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-114
CANONICAL_MASTER = ARTICLE_MASTER_V021
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V021.md
CANONICAL_MASTER_MD_SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
CANONICAL_MASTER_MD_GIT_BLOB = e76b5b1789de1f82c9623dd6543c38ae639715b0
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B06_SECTION_5_6_DRAFTING_V01
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B05_SECTION_5_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B06_SECTION_5_6 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B06_V01_ONLY
RESULTS_B07_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V021.md` es el master Markdown canónico verificado. Results §5.1–§5.5 están cerrados, aprobados, congelados e integrados.

La promoción B05 a V021 fue byte-exacta y está registrada en:

`article/governance/D112_RESULTS_B05_AUTHOR_APPROVAL_V021_VERIFICATION_AND_INTEGRATION.md@54884ec91f3179ce9a35d87da58d2bee1970bd74`.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 57
```

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = INTEGRATED
5.5 Sensitivity and robustness analyses   = INTEGRATED
5.6 Inferential results                    = OPEN / AUTHORIZED B06 V01
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Results B06 / Section 5.6

Ground truth:

`article/governance/D113_RESULTS_B06_GROUND_TRUTH_SYNC_AND_SECTION5_6_BOUNDARY.md@ea170f8bb6c145c44706b42f8dd32f7d6e336ace`

Snapshot experimental:

`main@db0d0ad0d8435921a7838db6720eaea86a263763`

Fuentes principales:

```text
outputs/analysis/group3/g3_inferential_results_v0.1.csv
GIT_BLOB = cf3d8d85e099a300330da0214836e70af7a02253

docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
GIT_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
```

El bloque congela:

1. HE2_A: tres familias `historical - comparator`, cinco métricas primarias cada una, con 99% marginal percentile CI bajo control Bonferroni familywise-95%; los 15 límites inferiores son > 0.
2. HE2_B: `Recall@200 - Recall@100 = 0.202651515`, 95% CI `[0.066763106, 0.341601308]`.
3. Top-50 como suplementario sin rol decisional.
4. Phase E como evidencia descriptiva, no inferencial.
5. C28: `HE2 = SUPPORTED` únicamente dentro del alcance inferencial congelado.
6. C29: `HE5 = INCONCLUSIVE`; no se añade un test inferencial nuevo.

No se autorizan p-values, nueva inferencia, causalidad, generalización externa, accuracy global del framework ni validez jurídica.

## 4. Contrato activo

Prompt:

`article/prompts/6_RESULTS_B06_SECTION5_6.md@8fead6a8fca5361e7632faf566d5d86f909ed740`

Git blob:

`263c07e34066ef052062563b7cc4257856acbef7`

Revisión:

`article/reviews/6_RESULTS_B06_SECTION5_6_PROMPT_INTERNAL_REVIEW_V01.md@a8b222604cb1a86c14684bb99b17c5af93c0be73` — `PASS`.

Autorización:

`article/governance/D114_RESULTS_B06_SECTION5_6_EXECUTION_AUTHORIZATION.md@9186a395762dede09935e973981064b84f7458e8`.

## 5. Baselines y entrega

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V021.md
BASELINE_MASTER_MD_SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
BASELINE_MASTER_MD_GIT_BLOB = e76b5b1789de1f82c9623dd6543c38ae639715b0

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
BASELINE_DOCX_SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

D-035 continúa activo. El DOCX debe editarse de forma nativa acumulativa; no reconstruir desde Markdown ni usar Base64 manual, chunking, fragmentación o reensamblado.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B06_SECTION_5_6
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B06_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B06_SECTION5_6_RESPONSE_V01.md
EXPECTED_EXIT = RESULTS_B06_V01_COMPLETED_PENDING_GESTORA_AUDIT
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V021 is the canonical verified master. Results Sections 5.1–5.5 are integrated. Results B06 / Section 5.6 is the only open drafting block under D-113/D-114. It is limited to frozen HE2_A/HE2_B inference and bounded HE2/HE5 dispositions; no new inference or downstream drafting is authorized.

```text
CURRENT_GATE = RESULTS_B06_SECTION_5_6_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
RESULTS_B06 = AUTHORIZED
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```