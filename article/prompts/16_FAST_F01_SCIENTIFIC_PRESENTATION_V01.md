# 16 — FAST-F01 Scientific Presentation & Visual Structuring V01

## Role

Act exclusively as **IA de Redacción científica** for GIC-NANDINA.

Execute only FAST-F01. Do not act as IA Gestora, IA Experimental, or Author.

## Goal

Improve the scientific readability of ARTICLE_MASTER_V037 by converting selected dense numerical presentation into a restrained set of tables and figures, while preserving all scientific claims, denominators, inferential boundaries, and conclusions.

This is a presentation/editing task, not a new scientific-analysis task.

## Governing decisions and reviews

Read completely:

- `article/governance/D200_G7_F03_A09_A10_AUTHOR_APPROVAL_AND_V037_INTEGRATION.md`;
- `article/governance/D201_FAST_FINALIZATION_MODE_AND_FAST_F01_BOUNDARY.md`;
- `article/reviews/16_FAST_F01_KBS34_TABLE_FIGURE_EDITORIAL_REVIEW_V01.md`;
- current `article/ARTICLE_STATUS.md`;
- current `article/ARTICLE_WRITING_PLAN.md`;
- `article/STYLE_GUIDE.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
- `article/manuscript/ARTICLE_MASTER_V037.md`.

The execution authorization must bind explicitly to this prompt and its Git blob. If it does not, stop in preflight.

## Exact baseline Markdown

`article/manuscript/ARTICLE_MASTER_V037.md`

```text
EXPECTED_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919

EXPECTED_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1
```

## Exact baseline Word

`ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx`

```text
EXPECTED_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c

EXPECTED_SIZE_BYTES = 112705
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
BASELINE_PAGE_COUNT = 73
```

The DOCX must be edited directly from this exact binary. Do not reconstruct the Word from Markdown.

If the exact DOCX bytes are unavailable in the execution context, stop at preflight.

## Frozen scientific presentation sources

Use the following sources as authoritative.

### G5-MAIN-01

`outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv`

Git blob:

`cb68583ee2260e4455796bac99ad90995ca7ef92`

### G5-MAIN-02

`outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv`

Git blob:

`359e4e19b5ef1d44983c03039162209293b2a44c`

### G5 canonical table contract

`docs/results/group5/g5_canonical_tables_v0.1.md`

Git blob:

`9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d`

### G6-FIG-01

`figures/group6/g6_fig_01_he2.svg`

Git blob:

`f57511c1ddbed5d2177e7cf7b5c9a4a180a3c7e3`

Caption registry:

`docs/figures/group6/g6_caption_registry_v0.1.md`

Git blob:

`0dcb43cfa56dfce2e6955f960184069beb36ba76`

Do not recompute, redesign, reorder, simplify, or reinterpret the scientific content of G5-MAIN-01, G5-MAIN-02, or G6-FIG-01.

## Required main-body visual inventory

Exactly:

```text
TABLES = 3
FIGURES = 2
```

No additional main-body table or figure is authorized.

### Table 1 — Experimental benchmark and evaluation overview

Create one compact editorial summary table using **only facts already stated in V037**.

Purpose: make the benchmark, data roles, evaluation unit, dependence unit, and major scope constraints inspectable without forcing the reader through several dense paragraphs.

Allowed fields may include, where explicitly supported by V037:

- component / split / bank;
- role;
- size/count;
- primary unit;
- dependence/grouping;
- scope/use.

Do not calculate a new percentage, ratio, aggregate, statistic, or derived quantity.

Do not add a number that is absent from V037.

Place the table in Experimental Design at the most natural point before detailed system execution; do not create a new numbered section solely for the table.

Create publication-facing English and natural Spanish mirror captions/tables.

### Table 2 — Primary HE2_A early-ranking contrasts

Materialize G5-MAIN-01 into publication-ready table form.

Requirements:

- use only the canonical 15 rows;
- preserve all historical arm values, comparator arm values, paired differences, frozen 99% CI bounds, EVAL_N=1056, DAM_N=67;
- make clear that the CI belongs to the paired Historical-minus-comparator difference, not either arm;
- Top-50 must not be introduced into this table;
- no arm-level CI;
- no p-values;
- no causal language;
- no favorability-based reordering.

Place in §5.2.

The prose in §5.2 may be shortened locally so that it states the main observed pattern and interpretation rather than re-listing every table value.

### Table 3 — HE2_B deep coverage

Materialize G5-MAIN-02 into publication-ready table form.

Requirements:

- Recall@100;
- Recall@200;
- paired difference;
- frozen CI;
- Pool@200 as context only;
- EVAL_N=1056;
- DAM_N=67;
- no second confirmatory interpretation of Pool@200.

Place in §5.2 after Table 2 or at the end of the deep-coverage paragraph.

### Figure 1 — Decision-support architecture

Create an editorial schematic from the already approved architecture in §3.

Required primary flow:

```text
Commercial description / input
-> Query normalization
-> Historical retrieval and ranking
-> Unique candidate construction
-> FIXED TOP-3
-> Candidate-specific documentary evidence
-> Context assembly
-> Local LLM explanation
```

The diagram must communicate authority boundaries:

- historical retrieval determines candidate membership/order;
- documentary evidence attaches evidence but does not rerank;
- the LLM explains received candidates/context and cannot alter ranking.

If the diagnostic reranker is shown, it must appear only as a clearly labeled **diagnostic lateral route**, with no arrow that returns to or changes the primary ranking/fixed Top-3.

Do not show the diagnostic reranker as a production component.

Create:

- editable SVG;
- PNG rendering for delivery;
- English publication-facing labels;
- optional Spanish mirror figure only if needed for the internal bilingual master; otherwise use one language-neutral figure with bilingual captions.

Place as Figure 1 in §3 near the overall architecture description.

### Figure 2 — G6-FIG-01

Use the approved G6-FIG-01 visual content exactly.

The scientific figure itself must not be redrawn or altered.

You may convert the approved SVG to PNG only as a rendering operation without changing content.

Place in Results where it supports the inferential HE2 evidence, preferably §5.6.

Use an English publication-facing caption that is a faithful semantic translation of the approved caption registry, and a natural Spanish mirror caption.

Preserve:

- Panel A arm-level values with no arm-level CI;
- Panel B 15 paired Historical-minus-comparator differences with frozen 99% CIs;
- Panel C single HE2_B Recall@200-minus-Recall@100 contrast with frozen 95% CI;
- no p-values;
- noncausal internal-benchmark interpretation.

## Prose compression rules

You may edit prose only where necessary to avoid direct duplication created by Tables 1–3 and Figures 1–2.

Allowed local compression zones:

- the Experimental Design paragraphs immediately surrounding Table 1;
- §5.2 immediately surrounding Tables 2–3;
- §5.6 immediately surrounding Figure 2;
- §3 immediately surrounding Figure 1.

Outside those zones, preserve content.

Do not modify:

- Title;
- Abstract;
- Keywords;
- Related Work;
- A09/A10 diagnostic reranker text except cross-reference wording if strictly needed;
- Discussion §6;
- Conclusion §7;
- AI disclosure;
- other End Matter;
- References placeholder;
- supplementary material content;
- drafting-note cleanup outside the insertion zones.

## Scientific guardrails

```text
NO_NEW_EXPERIMENT = YES
NO_NEW_METRIC = YES
NO_NEW_CI = YES
NO_NEW_P_VALUE = YES
NO_NEW_LITERATURE = YES
NO_NEW_CITATION = YES
NO_NEW_HYPOTHESIS_DISPOSITION = YES

HE2 = PRESERVE
HE3 = PRESERVE
HE5 = INCONCLUSIVE / PRESERVE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / PRESERVE

PRIMARY_FLOW =
HISTORICAL_RANKING -> FIXED_TOP3 -> DOCUMENTARY_EVIDENCE -> CONTEXT -> LOCAL_LLM_EXPLANATION

DIAGNOSTIC_RERANKER =
SEPARATE / DIAGNOSTIC_ONLY / NO_FEEDBACK
```

## Supplementary carry-forward

Do not integrate these into the main body in FAST-F01:

- G5-SECONDARY-01;
- G5-SECONDARY-02;
- G5-APPENDIX-01;
- G5-APPENDIX-02;
- G5-APPENDIX-03;
- G5-APPENDIX-04;
- G5-APPENDIX-05;
- G6-FIG-02;
- G6-FIG-03.

Create only an internal carry-forward manifest for FAST-F02 listing their governed paths and dispositions.

## Required artifacts

Create/version:

1. `article/sections/fast/FAST_F01_Scientific_Presentation_V01.md`
2. `article/figures/FAST_F01_Figure1_Architecture_V01.svg`
3. `article/manifests/FAST_F01_SUPPLEMENTARY_CARRY_FORWARD_V01.md`
4. `article/responses/16_FAST_F01_SCIENTIFIC_PRESENTATION_RESPONSE_V01.md`

Deliver as real files:

5. `ARTICLE_MASTER_CANDIDATE_FAST_F01_V01.md`
6. `ARTICLE_MASTER_CANDIDATE_FAST_F01_V01.docx`
7. `FAST_F01_Figure1_Architecture_V01.png`
8. approved G6-FIG-01 rendered PNG used in the candidate, if needed for reproducible handoff.

Do not promote a new canonical master.

## Markdown audit contract

The response must identify:

- exact changed regions;
- exact table insertion locations;
- exact figure insertion locations;
- prose lines/paragraphs removed or shortened because of duplication;
- proof that all edits outside authorized FAST-F01 zones are unchanged.

## DOCX / OOXML contract

Preserve all inherited comments and anchors unless a comment anchor lies inside a directly edited paragraph; if any anchor would move, preserve its semantic span and report it.

At minimum:

```text
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Run:

- ZIP/OOXML integrity;
- part inventory;
- comments and anchors;
- tracked changes;
- image relationship inventory;
- full render;
- visual QA of every page;
- full-detail QA of every page containing a new table or figure;
- visible-text equivalence between Markdown and DOCX for all changed prose/table captions;
- figure-caption identity;
- check that Table 2/3 values match the canonical G5 CSVs exactly;
- check that Figure 2 is content-identical to approved G6-FIG-01.

Page count may change by reflow.

## Response minimum fields

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = FAST_FINALIZATION / FAST_F01

PROMPT_IDENTITY = PASS / BLOCKED
AUTHORIZATION_IDENTITY = PASS / BLOCKED
BASELINE_MD_IDENTITY = PASS / BLOCKED
BASELINE_DOCX_IDENTITY = PASS / BLOCKED
G5_MAIN_01_IDENTITY = PASS / BLOCKED
G5_MAIN_02_IDENTITY = PASS / BLOCKED
G6_FIG_01_IDENTITY = PASS / BLOCKED

TABLE_1 = MATERIALIZED / BLOCKED
TABLE_2_G5_MAIN_01 = MATERIALIZED / BLOCKED
TABLE_3_G5_MAIN_02 = MATERIALIZED / BLOCKED
FIGURE_1_ARCHITECTURE = MATERIALIZED / BLOCKED
FIGURE_2_G6_FIG_01 = MATERIALIZED / BLOCKED

MAIN_BODY_TABLE_COUNT = ...
MAIN_BODY_FIGURE_COUNT = ...

NEW_SCIENTIFIC_CONTENT = NO / BLOCKED
NEW_METRIC_OR_INFERENCE = NO / BLOCKED
G5_VALUES_EXACT = PASS / BLOCKED
G6_FIGURE_CONTENT_IDENTITY = PASS / BLOCKED
DIAGNOSTIC_RERANKER_BOUNDARY = PASS / BLOCKED

COMMENTS = ...
TRACKED_CHANGES = ...
ZIP_OOXML_INTEGRITY = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = ...
FULL_DOCX_VISUAL_QA = ...

CANDIDATE_MD_SHA256 = ...
CANDIDATE_MD_EXPECTED_GIT_BLOB = ...
CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO / YES + REASON
EXPECTED_EXIT = FAST_F01_COMPLETED_PENDING_GESTORA_AUDIT
```

## Stop condition

Stop at:

`FAST_F01_COMPLETED_PENDING_GESTORA_AUDIT`

Do not begin FAST-F02, FAST-F03, or Experimental G8-F01.
