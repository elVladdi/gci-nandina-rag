# D-110 — Results B05 / Section 5.5 execution authorization

## Español

```text
DECISION = D-110
BLOCK = RESULTS_B05_SECTION_5_5
SECTION = 5.5 SENSITIVITY AND ROBUSTNESS ANALYSES
GROUND_TRUTH = D-109 / SYNCHRONIZED
PROMPT_REVIEW = PASS
EXECUTION = AUTHORIZED_FOR_B05_V01_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B06_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Autoridad de ejecución

Se autoriza a IA de Redacción a ejecutar exclusivamente:

```text
PROMPT = article/prompts/6_RESULTS_B05_SECTION5_5.md
PROMPT_COMMIT = b6a0973bd2e9337d7c79132ca73cd9c05d8ba7da
PROMPT_GIT_BLOB = d2dd98fb21982078b7d92539f6cc630c342647e7
```

La revisión interna vinculante es:

```text
PROMPT_REVIEW = article/reviews/6_RESULTS_B05_SECTION5_5_PROMPT_INTERNAL_REVIEW_V01.md
PROMPT_REVIEW_COMMIT = edac2f1276c4c42dd7a9000820e4a4ed18a2c0ed
PROMPT_REVIEW_GIT_BLOB = fb40eda4fa6dae19a261c93337f57583f85dc0fc
PROMPT_REVIEW_RESULT = PASS
```

### 2. Baselines exactos

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V020.md
BASELINE_MASTER_MD_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
BASELINE_MASTER_MD_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
BASELINE_DOCX_SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
PAGE_COUNT = 54
```

### 3. Alcance científico autorizado

B05 V01 puede reportar exclusivamente los resultados de sensibilidad/robustez delimitados en D-109 y en los claims `C08`, `C22`–`C27` y `C29`:

- sensibilidad conjunta tamaño/composición H25/H50/H75 con H100 como referencia congelada;
- sensibilidad descriptiva H150/H200 sobre diez seeds pareados en el mismo EVAL;
- sensibilidad correctiva final 0B-05C Attempt06 con respuesta dependiente del método;
- distribución descriptiva HE5 por proximidad jerárquica y buckets literales de soporte;
- no-estimabilidad de diversidad histórica EXP12 y prevalencia de descripciones ambiguas/incompletas;
- disposición HE5 únicamente como `INCONCLUSIVE` bajo sus límites.

### 4. Límites vinculantes

```text
ISOLATED_CAUSAL_BANK_SIZE_EFFECT = PROHIBITED
GENERAL_H150_H200_IMPROVEMENT_OR_DEGRADATION_CLAIM = PROHIBITED
SEED_SUPERPOPULATION_INFERENCE = PROHIBITED
INFERENTIAL_CI_OR_PVALUES_IN_B05 = PROHIBITED
HE2_DISPOSITION_IN_B05 = PROHIBITED
GLOBAL_ZERO_IMPACT_OF_0B05C = PROHIBITED
LEGAL_CORRECTNESS = PROHIBITED
OVERALL_CLASSIFICATION_ACCURACY = PROHIBITED
EMPIRICAL_GENERALIZATION_BEYOND_CHAPTER87 = PROHIBITED
NOVELTY_OR_SOTA = PROHIBITED
```

§5.6 conserva en exclusiva los resultados inferenciales HE2 y sus intervalos.

### 5. Alcance diferencial

```text
SECTIONS_1_TO_5_4 = FROZEN / PRESERVE
SECTION_5_5 = AUTHORIZED_FOR_DRAFTING_V01
SECTIONS_5_6_PLUS = NOT_AUTHORIZED / PRESERVE_PLACEHOLDERS
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
END_MATTER = PRESERVE
```

D-035 permanece obligatorio.

### 6. Gate vigente

```text
CURRENT_GATE = RESULTS_B05_SECTION_5_5_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B05_PROMPT
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B05_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B05_SECTION5_5_RESPONSE_V01.md
EXPECTED_EXIT = RESULTS_B05_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B06_PLUS = NOT_AUTHORIZED
```

---

## English

Results B05 / Section 5.5 V01 is authorized for drafting under the exact prompt `article/prompts/6_RESULTS_B05_SECTION5_5.md@b6a0973bd2e9337d7c79132ca73cd9c05d8ba7da`. V020 and the approved B04 DOCX are the exact cumulative baselines. Drafting is limited to the reconciled descriptive sensitivity and robustness evidence in D-109. Section 5.6 inferential HE2 results, Results B06+, Discussion, and Conclusion remain unauthorized.