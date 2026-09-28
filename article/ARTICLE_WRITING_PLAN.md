# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.31
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-118
CANONICAL_MASTER = ARTICLE_MASTER_V022
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V022.md
CANONICAL_MASTER_MD_SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
CANONICAL_MASTER_MD_GIT_BLOB = 088eecd537997a3438517f7d206f6d890b0aa064
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B07_SECTION_5_7_DRAFTING_V01
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B03_SECTION_5_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B04_SECTION_5_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B05_SECTION_5_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B06_SECTION_5_6 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B07_SECTION_5_7 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B07_V01_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V022.md` es el master Markdown canónico verificado. Results §5.1–§5.6 están cerrados, aprobados, congelados e integrados.

La promoción B06 a V022 fue byte-exacta y está registrada en:

`article/governance/D116_RESULTS_B06_AUTHOR_APPROVAL_V022_VERIFICATION_AND_INTEGRATION.md@1f88a9a7121874ea751d8b7e2b5b76e2558c192a`.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
PAGE_COUNT = 58
```

## 2. Estructura vigente de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = INTEGRATED
5.3 Documentary evidence retrieval        = INTEGRATED
5.4 Controlled explanation quality        = INTEGRATED
5.5 Sensitivity and robustness analyses   = INTEGRATED
5.6 Inferential results                    = INTEGRATED
5.7 Summary by research question           = AUTHORIZED B07 V01
```

## 3. Decisión editorial sobre §5.7

La estructura congelada permitía omitir §5.7 si resultaba redundante. D-117 resolvió `RETAIN_AND_DRAFT` porque los cuatro RQ atraviesan seis subsecciones de Results y una síntesis compacta por RQ mejora la legibilidad antes de Discussion.

La sección debe ser estrictamente sintética:

```text
RQ1 = candidate retrieval + inferential HE2 boundary
RQ2 = documentary coverage / traceability / Top-3 invariance
RQ3 = structural preservation + bounded qualitative auditability
RQ4 = benchmark validity / sensitivity / non-estimability / HE5 limits
```

No se permiten resultados nuevos, inferencia nueva, comparación con literatura, causalidad, implicaciones prácticas, novelty, `FINAL_GAP`, Discussion ni Conclusion.

## 4. Contrato activo B07

Boundary:

`article/governance/D117_RESULTS_B07_SECTION5_7_EDITORIAL_NECESSITY_AND_SYNTHESIS_BOUNDARY.md@b22139b265b6f7dfa02e1f00083f1a982eb4c89a`

Prompt:

`article/prompts/6_RESULTS_B07_SECTION5_7.md@d13fb533e7f947a6416ab4ad8067d28a47acf878`

Git blob:

`0387f4a0d5f78e94c771fed3999e9fa940f4a8a2`

Revisión:

`article/reviews/6_RESULTS_B07_SECTION5_7_PROMPT_INTERNAL_REVIEW_V01.md@2d32dcecf55a7bb5e5832727546585c1bd867a5b` — `PASS`.

Autorización:

`article/governance/D118_RESULTS_B07_SECTION5_7_EXECUTION_AUTHORIZATION.md@9ea19f30bb2a3d8251bebe37b9ef0feff13882f4`.

## 5. Baselines y entrega

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V022.md
BASELINE_MASTER_MD_SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
BASELINE_MASTER_MD_GIT_BLOB = 088eecd537997a3438517f7d206f6d890b0aa064

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
BASELINE_DOCX_SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

D-035 continúa activo. El Word debe editarse de forma nativa acumulativa; no reconstruir desde Markdown ni usar Base64 manual, chunking, fragmentación o reensamblado.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B07_SECTION_5_7
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B07_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B07_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B07_SECTION5_7_RESPONSE_V01.md
EXPECTED_EXIT = RESULTS_B07_V01_COMPLETED_PENDING_GESTORA_AUDIT
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V022 is the canonical verified master. Results Sections 5.1–5.6 are integrated. D-117 retained optional Section 5.7 because the research questions cut across the existing Results subsections and a compact RQ-oriented synthesis improves readability. D-118 authorizes only B07 V01 under the reviewed prompt. No new result, inference, claim, literature comparison, implication, novelty statement, Discussion, or Conclusion content is authorized.

```text
CURRENT_GATE = RESULTS_B07_SECTION_5_7_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
RESULTS_B07 = AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```