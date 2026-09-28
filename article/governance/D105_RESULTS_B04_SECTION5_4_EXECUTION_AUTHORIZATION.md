# D-105 — Results B04 / Section 5.4 execution authorization

## Español

```text
DECISION = D-105
BLOCK = RESULTS_B04_SECTION_5_4
SECTION = 5.4 CONTROLLED EXPLANATION QUALITY
GROUND_TRUTH = D-104 / SYNCHRONIZED
CLAIM_MATRIX_C35_C41 = REGISTERED / AUTHORIZED
PROMPT_REVIEW = PASS
EXECUTION = AUTHORIZED_FOR_B04_V01_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Autoridad de ejecución

Se autoriza a la IA de Redacción a ejecutar exclusivamente:

```text
PROMPT = article/prompts/6_RESULTS_B04_SECTION5_4.md
PROMPT_COMMIT = 290d8668f138839cfce11752fc1010e778ddee31
PROMPT_GIT_BLOB = 98161fb0e606205cc6c429c81765c59b5ade3a23
```

La revisión interna vinculante es:

```text
PROMPT_REVIEW = article/reviews/6_RESULTS_B04_SECTION5_4_PROMPT_INTERNAL_REVIEW_V01.md
PROMPT_REVIEW_COMMIT = d4c90480c136a9d3d778ddc125e577d86beaa8aa
PROMPT_REVIEW_RESULT = PASS
```

### 2. Baselines exactos

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V019.md
BASELINE_MASTER_MD_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
BASELINE_MASTER_MD_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
BASELINE_DOCX_SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

### 3. Alcance científico autorizado

B04 V01 puede reportar únicamente los resultados de RQ3 fijados en D-104 y C35–C41:

- controles automáticos/estructurales sobre 50 casos / 150 slots;
- preservación del Top-3, rank, referencias y trazabilidad;
- ausencia de una regla per-case `automatic_validation_pass` válida para reconstrucción retrospectiva;
- `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` que explica el 0/50 de schema compliance;
- evaluación cualitativa 28/50 auditable, distribución total y ocho dimensiones;
- warning-control descriptivo 41/50;
- modalidad real `AI_EXPERT_ROLE`/LLM-as-judge, no humana;
- síntesis funcional y delimitada del resultado conjunto.

### 4. Límites vinculantes

```text
C13 = PROHIBITED
C14 = CONDITIONAL_ONLY
HUMAN_EXPERT_VALIDATION = PROHIBITED
LEGAL_CORRECTNESS = PROHIBITED
SUBSTANTIVE_NORMATIVE_CORRECTNESS = PROHIBITED
OVERALL_CLASSIFICATION_ACCURACY = PROHIBITED
CAUSAL_FAITHFULNESS = PROHIBITED
EMPIRICAL_GENERALIZATION_BEYOND_CHAPTER87 = PROHIBITED
RETROSPECTIVE_AUTOMATIC_PASS_RATE = PROHIBITED
INFERENCE_OR_SIGNIFICANCE_FOR_B04 = PROHIBITED
```

B04 debe mostrar las debilidades observadas junto con las fortalezas y preservar las dos limitaciones metodológicas centrales: mismatch prompt-schema y desviación de modalidad del evaluador.

### 5. Alcance diferencial

```text
SECTIONS_1_TO_5_3 = FROZEN / PRESERVE
SECTION_5_4 = AUTHORIZED_FOR_DRAFTING_V01
SECTIONS_5_5_PLUS = NOT_AUTHORIZED / PRESERVE_PLACEHOLDERS
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
END_MATTER = PRESERVE
```

D-035 permanece obligatorio.

### 6. Gate vigente

```text
CURRENT_GATE = RESULTS_B04_SECTION_5_4_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B04_PROMPT
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B04_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B04_SECTION5_4_RESPONSE_V01.md
EXPECTED_EXIT = RESULTS_B04_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B05_PLUS = NOT_AUTHORIZED
```

---

## English

Results B04 / Section 5.4 V01 is authorized for drafting under the exact prompt `article/prompts/6_RESULTS_B04_SECTION5_4.md@290d8668f138839cfce11752fc1010e778ddee31`. V019 and the approved B03 DOCX are the exact cumulative baselines. Drafting is limited to controlled-explanation quality under frozen C35–C41 evidence and the D-104 boundaries. Results B05+, Discussion, and Conclusion remain unauthorized.