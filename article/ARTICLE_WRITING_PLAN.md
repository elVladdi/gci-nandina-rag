# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.17
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-093
CANONICAL_MASTER = ARTICLE_MASTER_V017
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V017.md
CANONICAL_MASTER_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
CANONICAL_MASTER_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B02_SECTION_5_2_DRAFTING_V01
RESULTS_B01_SECTION_5_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B02_SECTION_5_2 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B02_V01_ONLY
RESULTS_B03_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V017.md` es el master Markdown canónico verificado. La promoción B01 fue byte-exacta y está registrada en D-091.

El Word acumulativo canónico es `ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx`, SHA-256 `f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f`, bajo custodia local del autor, con 40 comentarios preservados y 0 tracked changes.

Experimental Design y Results B01 / §5.1 están cerrados, aprobados, congelados e integrados.

## 2. Estructura congelada de Results

```text
5.1 Data and partition checks             = INTEGRATED
5.2 Candidate retrieval performance       = OPEN / AUTHORIZED B02 V01
5.3 Documentary evidence retrieval        = NOT AUTHORIZED
5.4 Controlled explanation quality        = NOT AUTHORIZED
5.5 Sensitivity and robustness analyses   = NOT AUTHORIZED
5.6 Inferential results                    = NOT AUTHORIZED
5.7 Summary by research question           = NOT AUTHORIZED
```

## 3. Results B02 / Section 5.2

Ground truth:

`article/governance/D092_RESULTS_B02_GROUND_TRUTH_SYNC_AND_SECTION5_2_BOUNDARY.md@494ada68bf314357381d42bb9bdcbb4c58719cc6`

Snapshot experimental congelado:

`db0d0ad0d8435921a7838db6720eaea86a263763`

Fuentes métricas congeladas:

```text
Historical BM25 H100
outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json
GIT_BLOB = a43893eca3dd756a1ff11935a9cf55afb728e8f4

Flat normative BM25
outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5/normative_flat_metrics.json
GIT_BLOB = 922ecbee8316ee36cd8a53d3ac52f79fac4cd3ed

Hierarchical normative BM25
outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_metrics.json
GIT_BLOB = 780a005130d1ad68867b290b832c394f8f488a23

D1a Text2Trade-inspired MNRL
outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_metrics.json
GIT_BLOB = 73e062b927d059a9f4e52caab7b785eafb6f2e01
```

B02 reportará exclusivamente desempeño descriptivo sobre EVAL=1,056: Top-1/3/5/10, MRR@100, Top-50 suplementario y deep coverage jerárquico Recall@100/Recall@200/Pool@200. Los comparadores no sustituyen el ranking histórico del flujo primario.

Inferencia, CI, `HE2 = SUPPORTED`, Phase-E pools, sensibilidades, evidencia documental, explicación, literatura y Discussion permanecen fuera de B02.

## 4. Contrato activo

Prompt:

`article/prompts/6_RESULTS_B02_SECTION5_2.md@76045bc1e408298b3e86de11f0598500f7dfa24f`

Git blob:

`0fd0aa40419b248e5983f0cb445c187e92a4bc13`

Revisión:

`article/reviews/6_RESULTS_B02_SECTION5_2_PROMPT_INTERNAL_REVIEW_V01.md@f0ed6c555275afff6e094d1b91ecef56e642b476` — `PASS`.

Autorización:

`article/governance/D093_RESULTS_B02_SECTION5_2_EXECUTION_AUTHORIZATION.md@d5860fca630a426df0ecf69198d109085742a80d`.

## 5. Baselines y entrega

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V017.md
BASELINE_MASTER_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
BASELINE_MASTER_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
BASELINE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

D-035 continúa activo: Base64 manual, chunking, fragmentación y reensamblado están prohibidos. El DOCX no se reconstruye desde Markdown y los candidatos acumulativos deben entregarse como archivos reales.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B02_SECTION_5_2
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B02_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B02_SECTION5_2_RESPONSE_V01.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V017 is the canonical verified Markdown master; the B01 V01 DOCX is the canonical cumulative Word baseline. Results B01 is integrated. Results B02 / §5.2 is the only open drafting block under D-092/D-093 and the exact prompt `article/prompts/6_RESULTS_B02_SECTION5_2.md@76045bc1e408298b3e86de11f0598500f7dfa24f`.

```text
CURRENT_GATE = RESULTS_B02_SECTION_5_2_DRAFTING_V01
NEXT_ACTOR = DRAFTING_AI
RESULTS_B02 = AUTHORIZED
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```