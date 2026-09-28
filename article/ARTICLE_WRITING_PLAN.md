# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.40
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-135
CANONICAL_MASTER = ARTICLE_MASTER_V026
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V026.md
CANONICAL_MASTER_MD_SHA256 = 76107b20419329ef7a5c6643fec892fbdc0e0779c1ab58f6de41bc36711f4156
CANONICAL_MASTER_MD_GIT_BLOB = f6a63be554317e62103aa96c1091f4039249e5ee
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
CANONICAL_CITATION_COMMENTS = 48
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B03_SECTION_6_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B04_SECTION_6_4 = AUTHORIZED_FOR_EXECUTION_USING_PROMPT_V02
CURRENT_GATE = DISCUSSION_B04_V01_DRAFTING
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_ACTOR = IA_REDACCION
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V026.md` es el master Markdown canónico verificado tras promoción byte-exacta del candidato Discussion B03 V01 aprobado por el autor. Results §5.1–§5.7 y Discussion §6.1–§6.3 están cerrados, aprobados, congelados e integrados.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx
SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 64
```

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = INTEGRATED
6.3 Comparison with prior work                             = INTEGRATED
6.4 Implications for auditable decision support            = AUTHORIZED FOR EXECUTION / PROMPT V02
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Cierre e integración B03

`article/governance/D132_DISCUSSION_B03_AUTHOR_APPROVAL_V026_VERIFICATION_AND_INTEGRATION.md@3d56571e267f0f58673f32391b9f8cf7420e8c39`

```text
V026_PROMOTION = PASS / BYTE_EXACT
V026_GIT_BLOB = f6a63be554317e62103aa96c1091f4039249e5ee
V026_SHA256 = 76107b20419329ef7a5c6643fec892fbdc0e0779c1ab58f6de41bc36711f4156
DISCUSSION_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
```

## 4. Trazabilidad B04 vigente

Boundary científico:
`article/governance/D133_DISCUSSION_B04_SECTION6_4_INTERPRETIVE_BOUNDARY_AND_AUDITABILITY_TRACE.md@be5a3df880d6fea49e18e64d6080d3485a5850de`

Prompt V01:
`article/prompts/7_DISCUSSION_B04_SECTION6_4.md@982375ae4b6660bd05d962b7ed681d59354e39c0` — `SUPERSEDED FOR EXECUTION`.

Prompt activo V02:
`article/prompts/7_DISCUSSION_B04_SECTION6_4_V02.md@9d84059e8620219cd83c3b3dad91c4af900d447e`

Prompt V02 Git blob:
`dcc3b40d29e1f6913cce96bee43403f3ab03e1d0`

Prompt review V02:
`article/reviews/7_DISCUSSION_B04_SECTION6_4_PROMPT_INTERNAL_REVIEW_V02.md@7716a4916662e8116ac84c7626e38caa7e7d66d9` — `PASS`.

Execution reauthorization:
`article/governance/D135_DISCUSSION_B04_PROMPT_V02_PROTOCOL_COMPLIANCE_AND_EXECUTION_REAUTHORIZATION.md@b5ef45237d7909b948edd3442d5da2ca14a335e2`.

D-135 no modifica el scope científico de B04. Corrige la cobertura operacional del prompt para que haga explícitos `START_HERE`, `MWDP_V1.0`, `SPCCR_V1.0`, D-022, D-027 y D-035, junto con el preflight y checklist obligatorio de entrega.

## 5. Contrato científico B04

§6.4 interpretará las implicaciones del contrato explícito de autoridad para apoyo a decisiones auditable. Historical retrieval genera y ordena candidatos; el Top-3 se fija antes de documentary association; documentary evidence no puede modificar membership u orden; el LLM es downstream explanation-only.

Ground truth congelado para la sección:

- RQ2: 3,168/3,168 candidate slots con asociación documental exacta NANDINA-8; 1,056/1,056 casos con preservación del Top-3 y su orden.
- RQ3 structural: 50/50 casos preservaron fixed Top-3/order y controles estructurales; 150/150 slots preservaron código, referencia histórica, referencia normativa y rank consistency.
- RQ3 qualitative: 28/50 = 56.0% cumplieron el criterio congelado de auditabilidad.
- Traceability = 2.00/2; mean verifiability = 0.54/2; mean historical–normative separation = 1.04/2.
- Schema compliance = 0/50 únicamente por `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` relativo a `advertencias_globales`.
- Qualitative evaluator = LLM-as-judge (`AI_EXPERT_ROLE`), no human validation.

La interpretación autorizada es que autoridad no solapada y provenance por candidato permiten inspeccionar outputs y fallos por etapa, pero trazabilidad estructural no es suficiente para demostrar verificabilidad, calidad de explicación, validación humana ni corrección jurídica. La coherencia versionada entre prompt y schema puede discutirse como requisito técnico de validación de interfaces.

No se autoriza nueva literatura, nuevas citas, novelty, first-ever, state-of-the-art, superioridad global, safety, reducción de alucinaciones, causalidad, overall classification accuracy, substantive normative correctness, legal correctness, deployment readiness ni external generalization.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_DISCUSSION_B04_V01_ONLY_USING_PROMPT_V02
PROMPT = article/prompts/7_DISCUSSION_B04_SECTION6_4_V02.md
PROMPT_GIT_BLOB = dcc3b40d29e1f6913cce96bee43403f3ab03e1d0
AUTHORIZATION = D-135
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V026.md
BASELINE_MD_SHA256 = 76107b20419329ef7a5c6643fec892fbdc0e0779c1ab58f6de41bc36711f4156
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx
BASELINE_DOCX_SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
BASELINE_COMMENTS = 48
EXPECTED_COMMENTS_AFTER_B04 = 48
EXPECTED_EXIT = DISCUSSION_B04_V01_COMPLETED_PENDING_GESTORA_AUDIT
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V026 is the verified canonical Markdown master. Results Sections 5.1–5.7 and Discussion Sections 6.1–6.3 are integrated. Discussion B04 / Section 6.4 remains scientifically bounded by D-133 and is authorized for execution only through the protocol-complete V02 prompt reauthorized by D-135.

V02 explicitly restores the cumulative operational requirements: repository onboarding, MWDP delivery checklist, SPCCR prose QA, repository-first execution response, exact DOCX author handoff, and timeout-safe cumulative-artifact transfer. The scientific scope is unchanged.

```text
PLAN_VERSION = V3.40
CURRENT_GATE = DISCUSSION_B04_V01_DRAFTING
NEXT_ACTOR = IA_REDACCION
ACTIVE_PROMPT = article/prompts/7_DISCUSSION_B04_SECTION6_4_V02.md
DISCUSSION_B04 = AUTHORIZED_FOR_EXECUTION
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```