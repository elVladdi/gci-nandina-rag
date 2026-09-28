# D-114 — Results B06 / Section 5.6 execution authorization

## Español

```text
DECISION = D-114
BLOCK = RESULTS_B06_SECTION_5_6
SECTION = 5.6 INFERENTIAL RESULTS
GROUND_TRUTH = D-113 / SYNCHRONIZED
PROMPT = article/prompts/6_RESULTS_B06_SECTION5_6.md
PROMPT_GIT_BLOB = 263c07e34066ef052062563b7cc4257856acbef7
PROMPT_REVIEW = PASS
EXECUTION = AUTHORIZED_FOR_B06_V01_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
CANONICAL_MASTER = ARTICLE_MASTER_V021
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

Se autoriza a IA de Redacción a ejecutar exclusivamente Results B06 / §5.6 bajo el prompt revisado y el ground truth D-113.

Baselines obligatorios:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V021.md
BASELINE_MD_SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
BASELINE_MD_GIT_BLOB = e76b5b1789de1f82c9623dd6543c38ae639715b0

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
BASELINE_DOCX_SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
PAGE_COUNT_BASELINE = 57
```

La ejecución debe reportar únicamente inferencia congelada HE2_A/HE2_B, disposición HE2 dentro del alcance autorizado y la disposición HE5 inconclusa sin nuevo test. §5.7 y secciones posteriores permanecen cerradas.

La salida esperada es:

```text
article/sections/results/Results_B06_V01.md
ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md
ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
article/responses/6_RESULTS_B06_SECTION5_6_RESPONSE_V01.md
```

La sección y response pequeñas pueden versionarse en GitHub. Los masters acumulativos se entregan como archivos reales conforme MWDP/D-035. Base64 manual, chunking, fragmentación y reensamblado permanecen prohibidos.

### Gate de salida

```text
EXPECTED_EXIT = RESULTS_B06_V01_COMPLETED_PENDING_GESTORA_AUDIT
NEXT_ACTOR = IA_REDACCION
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

Results B06 / Section 5.6 V01 is authorized for Drafting AI execution only. The canonical baseline is V021 and the cumulative Word baseline is the approved B05 DOCX. The execution is limited to frozen HE2_A/HE2_B inferential results and bounded HE2/HE5 dispositions. Section 5.7+, Discussion, and Conclusion remain unauthorized.