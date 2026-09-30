# 19 — FAST-F02 Global Table/Figure Correction V01

## Role

Act exclusively as **IA de Redacción científica** for GIC-NANDINA.

Execute only the corrective presentation cycle authorized for FAST-F02. Do not act as IA Gestora, IA Experimental, or Author.

The purpose is to correct the publication-facing presentation of the already approved scientific content by completing a **global full-body table/figure correction**. No new science is authorized.

## Governing documents

Read completely:

- `article/governance/D211_FAST_F02_APPROVAL_SUPERSEDED_GLOBAL_TABLE_FIGURE_AUDIT.md`;
- `article/reviews/19_FAST_F02_GLOBAL_TABLE_FIGURE_EDITORIAL_AUDIT_V01.md`;
- `article/governance/D208_FAST_F02_AUTHOR_FIELDS_INTENTIONALLY_BLANK.md`;
- `article/reviews/18_FAST_F02_END_MATTER_REFERENCES_SUPPLEMENTARY_INTERNAL_REVIEW_V01.md`;
- `article/manifests/FAST_F02_SUPPLEMENTARY_ASSEMBLY_V01.md`;
- `docs/figures/group6/g6_caption_registry_v0.1.md` from the main scientific branch/source;
- current `article/ARTICLE_STATUS.md`;
- current `article/ARTICLE_WRITING_PLAN.md`;
- `article/STYLE_GUIDE.md`.

Execution authorization must bind explicitly to this prompt and its exact Git blob. If it does not, stop at preflight.

# 1. Exact corrective baselines

## 1.1 Main manuscript Markdown baseline

`ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.md`

```text
EXPECTED_SHA256 =
c6909699b9b7272d12cbe57f02d5897b78c8a489c9105bdf69e23e4462e90dd4

EXPECTED_GIT_BLOB =
4c891641a86d0622cdc9fb7b2afee6f4691ee320

EXPECTED_SIZE_BYTES = 305240
```

## 1.2 Main manuscript Word baseline

`ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.docx`

```text
EXPECTED_SHA256 =
bd584ce9817ce8d251cbe43a6e737612039a5ba82c932f1637839d66466e9e31

EXPECTED_SIZE_BYTES = 356835
EXPECTED_PAGE_COUNT = 81
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Edit this exact DOCX directly. Do not reconstruct the cumulative Word manuscript from Markdown.

## 1.3 Supplementary Markdown baseline

`SUPPLEMENTARY_MATERIAL_FAST_F02_V01.md`

```text
EXPECTED_SHA256 =
fd2ff32090f2262787a0f661bf67300bca158733b24edae0a37ac90dffd0a89f

EXPECTED_GIT_BLOB =
d10207e99ca76c1b501f57c9cf2b620e54c03a3f

EXPECTED_SIZE_BYTES = 43533
```

## 1.4 Supplementary Word baseline

`SUPPLEMENTARY_MATERIAL_FAST_F02_V01.docx`

```text
EXPECTED_SHA256 =
ad6b7f5cbfa695ab61eb4f9b5469f061eb804074c5bfb8c735bdef81d700cc9e

EXPECTED_SIZE_BYTES = 222424
EXPECTED_PAGE_COUNT = 21
EXPECTED_TRACKED_CHANGES = 0
```

If any exact baseline is unavailable or fails identity verification, stop at preflight.

# 2. Core editorial rule

This is not a quota-driven table/figure exercise.

You must implement exactly the audited presentation plan because it was produced from a full-body editorial review:

```text
MAIN_TABLES_AFTER_CORRECTION = 7
MAIN_FIGURES_AFTER_CORRECTION = 4

SUPPLEMENTARY_TABLES_AFTER_CORRECTION = 7
SUPPLEMENTARY_FIGURES_AFTER_CORRECTION = 1
```

Do not add any additional table or figure beyond this audited set.

The anti-redundancy rule is binding:

- exact comparison vectors belong in tables;
- patterns/profiles belong in figures;
- prose carries interpretation, limits, and only a small number of anchor values;
- do not repeat a full table row/vector in prose;
- do not duplicate an identical main figure in Supplementary.

# 3. Main tables — exact required structure

## Table 1 — retain

Retain the existing:

**Experimental benchmark and evaluation overview**

Scientific content unchanged.

## Table 2 — create: observed candidate-retrieval performance by method

Create in Section 5.2 a compact descriptive table with exactly these rows:

1. Historical BM25 H100
2. Flat normative BM25
3. Hierarchical normative BM25
4. Corrected D1a Text2Trade-inspired MNRL

Columns:

- Method
- Top-1
- Top-3
- Top-5
- Top-10
- Top-50
- MRR@100

Use only the frozen values already present in FAST-F02 V01 and governed sources.

Required displayed values, rounded consistently with the current main-manuscript convention:

```text
Historical BM25 H100
Top-1 = 0.5095
Top-3 = 0.6714
Top-5 = 0.7633
Top-10 = 0.8911
Top-50 = 0.9915
MRR@100 = 0.6297

Flat normative BM25
Top-1 = 0.0275
Top-3 = 0.0511
Top-5 = 0.0616
Top-10 = 0.0653
Top-50 = 0.0701
MRR@100 = 0.0423

Hierarchical normative BM25
Top-1 = 0.0265
Top-3 = 0.0521
Top-5 = 0.0625
Top-10 = 0.0653
Top-50 = 0.0909
MRR@100 = 0.0420

Corrected D1a Text2Trade-inspired MNRL
Top-1 = 0.0009
Top-3 = 0.0104
Top-5 = 0.0511
Top-10 = 0.1780
Top-50 = 0.3134
MRR@100 = 0.0381
```

Do not attach CI to these arm-level observed values.

The detailed Top-50 inferential uncertainty remains Supplementary Table S3 and has no HE2 decision role.

## Table 3 — restructure current HE2_A table

Replace the current 15-row Table 2 with a compact inferential contrast matrix.

Rows:

- Top-1
- Top-3
- Top-5
- Top-10
- MRR@100

Columns:

- Metric
- Flat normative BM25: Historical − comparator [99% CI]
- Hierarchical normative BM25: Historical − comparator [99% CI]
- Corrected D1a: Historical − comparator [99% CI]

Use exactly:

`outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv`

Git blob:

`cb68583ee2260e4455796bac99ad90995ca7ef92`

Do not recompute any estimate or CI.

Each data cell may use a compact representation such as:

`0.4820 [0.3294, 0.6313]`

provided all values retain the existing approved rounding policy.

The caption must state:

- paired Historical-minus-comparator differences;
- 99% marginal percentile CI;
- frozen Bonferroni familywise-95% control;
- no p-values;
- no causal or external-validity interpretation.

## Table 4 — retain current HE2_B table

Retain the current HE2_B deep-coverage table and renumber it mechanically from current Table 3 to Table 4.

Use source:

`outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv`

Git blob:

`359e4e19b5ef1d44983c03039162209293b2a44c`

Scientific content unchanged.

## Table 5 — create: documentary association and ranking invariance

Create in Section 5.3.

Use the frozen Phase-F source:

`docs/exp04_phase_f_historical_normative_integration_v02_results.md`

Git blob:

`01a4573d34c029efb0b055c7b90202842e914549`

Recommended columns:

- Control / evidence level
- Numerator / denominator
- Rate
- Interpretation

Required rows:

```text
Exact NANDINA-8 evidence
3168/3168
1.0000
Exact candidate-level documentary association

HS6 parent context
2168/3168
0.6843
Hierarchical parent context only

HS4 parent context
3168/3168
1.0000
Hierarchical parent context only

Chapter parent context
3168/3168
1.0000
Hierarchical parent context only

Historical-precedent coverage
3168/3168
1.0000
Candidate-linked historical precedent retained

Complete candidate-level traceability
3168/3168
1.0000
Candidate/precedent/document links reconstructible

Top-3 membership and order preserved
1056/1056
1.0000
Case-level ranking invariance after documentary association
```

Do not state or imply that HS6/HS4/chapter parent context is exact NANDINA-8 evidence.

Do not imply legal correctness.

## Table 6 — create: controlled-explanation evaluation summary

Create in Section 5.4.

Use frozen sources only:

`outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_metrics_v0.2.json`

Git blob:

`843e1edd17a023f6c3d6f0b5235dd3fba86369c1`

and

`outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_warning_comparison_v0.2.csv`

Git blob:

`1cab0e8e7398a7299086fec7ad1ec28b2f706f2d`

The table must summarize, without creating new measures:

- Top-3 membership/order preserved: 50/50;
- candidate code / historical reference / normative reference / rank consistency: 150/150 slots;
- schema compliance: 0/50, qualified explicitly as prompt-schema specification mismatch caused by required `advertencias_globales`;
- auditable cases: 28/50 (56.0%);
- non-auditable cases: 22/50 (44.0%);
- hard violations: 0/50;
- generic-normative-warning present: 41/50;
- generic-normative-warning missing: 9/50;
- missing-warning subgroup: 1/9 auditable, mean total score 9.67;
- other cases: 27/41 auditable, mean total score 12.17.

The warning subgroup comparison must remain explicitly descriptive/noncausal.

Do not place the eight dimension means in Table 6; they belong in Figure 2.

## Table 7 — create: historical-bank sensitivity summary

Create in Section 5.5.

Sources:

`outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv`
Git blob:
`cf3aedab5935d6af9b3ac7be7b51b954fcb9c403`

`outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv`
Git blob:
`76c8c6c588c7e809c6be64f7192f497c491fb692`

Rows:

- H25
- H50
- H75
- H100 frozen reference
- H150
- H200

Columns:

- Condition
- Observed runs
- Top-1
- Top-3
- Top-5
- Top-10
- Top-50
- MRR@100
- Design note

Use exactly the frozen condition summaries.

For H25/H50/H75/H100:

```text
H25 / n=10
0.493371 / 0.645170 / 0.737405 / 0.843277 / 0.973106 / 0.603787

H50 / n=10
0.428598 / 0.597917 / 0.680303 / 0.776042 / 0.930492 / 0.542492

H75 / n=10
0.298295 / 0.463352 / 0.548769 / 0.653883 / 0.837121 / 0.414030

H100 / n=1 frozen reference
0.509470 / 0.671402 / 0.763258 / 0.891098 / 0.991477 / 0.629708
```

For H150/H200 use the frozen condition summaries from the canonical S5 source:

```text
H150 / 10 observed seed pairs
Top-1 = 0.512689
Top-3 = 0.689962
Top-5 = 0.783333
Top-10 = 0.891572
Top-50 = 0.989583
MRR@100 = 0.633268

H200 / 10 observed seed pairs
Top-1 = 0.514110
Top-3 = 0.689489
Top-5 = 0.782008
Top-10 = 0.895265
Top-50 = 0.985227
MRR@100 = 0.633310
```

Design-note cells must preserve:

- H25/H50/H75: joint size-composition sensitivity;
- H100: one frozen reference, not a replicate distribution;
- H150/H200: paired observed seed constructions, no seed-superpopulation inference.

Do not combine these designs into a causal size trend.

# 4. Main figures — exact required structure and order

Because the new figures occur before the current primary HE2 figure, figure numbering changes mechanically.

## Figure 1 — retain architecture

Retain current Figure 1 unchanged.

## Figure 2 — create: qualitative explanation-dimension profile

Create in Section 5.4 immediately after the paragraph/table introducing the qualitative profile.

Source:

`outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_dimension_metrics_v0.2.csv`

Git blob:

`c119cc8d05148ad893d7c7687b9f4495c24fc49b`

Create a publication-ready **horizontal bar chart**.

Exactly eight bars, no extra statistic:

```text
Traceability = 2.00
Verifiability = 0.54
Historical-normative evidence separation = 1.04
Conclusion prudence = 1.78
Fixed-Top-3 consistency = 1.96
Detection of generic normative evidence = 1.68
Candidate comparison = 1.46
Utility for human audit = 1.26
```

Requirements:

- x-axis fixed at 0 to 2;
- one bar per dimension;
- readable publication-facing English labels;
- value labels may be printed at bar ends;
- no CI;
- no p-values;
- no significance marks;
- no invented threshold line;
- no ranking language such as “best/worst” in the caption;
- no decorative 3D;
- accessible grayscale/print-safe design;
- vector SVG plus high-resolution PNG.

Caption must state:

- frozen 50-case qualitative sample;
- 0–2 rubric;
- evaluator = `independent_ai_reviewer_01`, `AI_EXPERT_ROLE`;
- LLM-as-judge, not human scoring;
- descriptive profile;
- does not establish human validation, legal correctness, or causal faithfulness.

Version the new figure as:

`article/figures/FAST_F02_Figure2_Explanation_Quality_V01.svg`

and deliver/export:

`FAST_F02_Figure2_Explanation_Quality_V01.png`

## Figure 3 — promote exact approved EXP11A figure

Place in Section 5.5.

Reuse the already approved scientific figure:

`figures/group6/g6_fig_03_exp11a.svg`
Git blob:
`1b2aca9aa9c2582cf0b7e16850cd5b22387cc771`

Approved PNG:
`figures/group6/g6_fig_03_exp11a.png`
Git blob:
`eaf59497ee49ab36d34d23e42cf002111bc9fe3e`

Do not redraw or alter scientific content.

This is an editorial promotion from Supplementary to main body.

Use the governed caption semantics from:

`docs/figures/group6/g6_caption_registry_v0.1.md`

Git blob:
`0dcb43cfa56dfce2e6955f960184069beb36ba76`

The caption must preserve:

- 31 observed runs;
- H25 n=10;
- H50-D1 n=5;
- H50-D2 n=5;
- H75 n=10;
- H100 n=1 frozen reference;
- six panels Top1/Top3/Top5/Top10/Top50/MRR;
- descriptive/noncausal;
- size and composition vary jointly;
- no CI, p-values, regression, smoothing or isolated monotonic size-effect interpretation.

## Figure 4 — retain current primary HE2 figure and renumber

The current Figure 2 / G6-FIG-01 becomes Figure 4 because it appears after Figures 2–3.

Scientific content and underlying image are unchanged.

Update caption numbering and all in-text cross-references mechanically.

# 5. Prose correction — remove numeric overload without deleting interpretation

## Section 5.2

After Tables 2–4:

- retain a concise lead sentence for historical performance;
- retain the interpretation that historical H100 had the highest observed values among the four evaluated retrieval families on the fixed EVAL set;
- do not repeat the complete four-method metric vectors in prose;
- deep-coverage prose may keep Recall@100/Recall@200 anchor values if useful but must not duplicate a full table.

## Section 5.3

After Table 5:

- reduce the current coverage paragraphs;
- keep the distinction between exact NANDINA-8 association and parent context;
- keep the ranking-invariance interpretation;
- keep the legal/substantive-correctness limitation;
- do not repeat every numerator/denominator already in Table 5.

## Section 5.4

After Table 6 and Figure 2:

- keep the central finding that 28/50 cases met the frozen auditability criterion;
- keep the key interpretation that traceability was stronger than verifiability/evidence separation;
- do not repeat all eight dimension means in prose;
- keep the prompt-schema mismatch explanation;
- keep LLM-as-judge limitation;
- keep warning-subgroup comparison descriptive/noncausal without repeating all table cells.

## Section 5.5

Replace the dense H25/H50/H75/H100 and H150/H200 vectors with:

- a concise interpretation;
- Table 7;
- Figure 3 for EXP11A run-level pattern.

The already reported frozen H25/H50/H75 Top-3 and MRR ranges may remain if they materially support variability interpretation, but do not retain the full metric vectors in prose.

For the corrective normative-resource sensitivity:

- sharply shorten the long before/after vector;
- preserve the central result: flat family zero aggregate change; hierarchical family tiny MRR decrease only; D1a non-zero changes with mixed minor hierarchy effect;
- refer to Supplementary Table S6 for exact values;
- no new main table.

For error hierarchy and support strata:

- retain only concise interpretation;
- refer to Supplementary Table S2;
- no new main table.

## Section 5.6

Delete the prose enumeration of all 15 HE2_A differences and confidence intervals.

Replace with concise inferential synthesis:

- all 15 primary 99% intervals lay entirely above zero;
- no p-values;
- refer to Table 3 and Figure 4.

Retain the separate HE2_B contrast interpretation and its bounded scope.

## Section 5.7, Discussion and Conclusion

Do not add new visual objects.

Preserve the existing scientific synthesis.

Only make minimal wording/cross-reference edits needed to avoid newly created duplication or to refer to the corrected table/figure numbering.

# 6. Partition/methods paragraphs deliberately kept as prose

Do not create additional tables/figures for:

- Section 4.2.3 partition composition;
- Section 4.4 partition validity controls;
- Section 4.5 BM25/LLM/runtime configuration;
- Section 5.1 residual exact/near-duplicate diagnostics;
- Section 5.2 diagnostic 20-case LLM reranker analysis.

Reason: Table 1 already carries benchmark composition, while the remaining items are methodological or diagnostic and do not justify additional main visual prominence.

# 7. Supplementary correction

Promote current Supplementary Figure S2 / G6-FIG-03 to main Figure 3.

Therefore Supplementary V02 must contain:

```text
Tables S1-S7 = UNCHANGED
Figure S1 = G6-FIG-02 / UNCHANGED
Former Figure S2 = REMOVED_FROM_SUPPLEMENTARY / PROMOTED_TO_MAIN_FIGURE_3
```

Do not delete any Supplementary table.

Update:

- Supplementary reading note;
- Supplementary figure count;
- main End Matter Supplementary statement.

The main manuscript End Matter statement becomes semantically equivalent to:

“Supplementary Material accompanies this article and contains Tables S1–S7 and Figure S1.”

The Spanish mirror must be semantically equivalent.

# 8. Spanish semantic-control mirror

Apply the same editorial structure to Part II:

- same seven table objects;
- same four main figures;
- same table/figure order;
- semantically equivalent captions and interpretation;
- no divergence in numeric values;
- no additional Spanish-only visual object.

Do not translate bibliography identities.

# 9. Author-administrative and End Matter freeze

Preserve FAST-F02 V01 End Matter content.

These fields remain blank:

- CRediT;
- Funding;
- Declaration of competing interest;
- Acknowledgements;

and Spanish mirrors.

Do not insert any author facts.

Preserve the approved generative-AI declaration unchanged.

Preserve Data availability, Code and reproducibility resources, and the 25-reference bibliography unchanged except for unavoidable cross-reference/layout mechanics.

# 10. Scientific prohibitions

```text
NEW_EXPERIMENT = FORBIDDEN
NEW_METRIC = FORBIDDEN
NEW_CI = FORBIDDEN
NEW_P_VALUE = FORBIDDEN
NEW_INFERENTIAL_TEST = FORBIDDEN
NEW_HYPOTHESIS_DISPOSITION = FORBIDDEN
NEW_LITERATURE = FORBIDDEN
NEW_REFERENCE = FORBIDDEN
NEW_CLAIM = FORBIDDEN
```

Allowed operations:

```text
EXACT_TRANSCRIPTION_OF_FROZEN_VALUES
TABLE_RESTRUCTURING
FIGURE_CREATION_FROM_FROZEN_DIMENSION_MEANS
PROMOTION_OF_ALREADY_APPROVED_G6_FIG_03
PROSE_DEDUPLICATION
CAPTION_EDITING_WITHIN_GOVERNED_SEMANTICS
MECHANICAL_RENUMBERING_AND_CROSS_REFERENCES
PUBLICATION_DISPLAY_ROUNDING
```

# 11. Required versioned artifacts

Create/version:

1. `article/sections/fast/FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_V01.md`
2. `article/manifests/FAST_F02_TABLE_FIGURE_INVENTORY_V02.md`
3. `article/figures/FAST_F02_Figure2_Explanation_Quality_V01.svg`
4. `article/supplementary/SUPPLEMENTARY_MATERIAL_FAST_F02_V02.md`
5. `article/responses/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_RESPONSE_V01.md`

Deliver as real files:

6. `ARTICLE_MASTER_CANDIDATE_FAST_F02_V02.md`
7. `ARTICLE_MASTER_CANDIDATE_FAST_F02_V02.docx`
8. `SUPPLEMENTARY_MATERIAL_FAST_F02_V02.md`
9. `SUPPLEMENTARY_MATERIAL_FAST_F02_V02.docx`
10. `FAST_F02_Figure2_Explanation_Quality_V01.png`

If feasible, also deliver the SVG as a real handoff file.

Do not promote a canonical master.

# 12. Markdown audit contract

Prove:

```text
MAIN_TABLE_COUNT = 7
MAIN_FIGURE_COUNT = 4
SUPPLEMENTARY_TABLE_COUNT = 7
SUPPLEMENTARY_FIGURE_COUNT = 1

TABLE_1 = RETAINED
TABLE_2 = OBSERVED_RETRIEVAL_PERFORMANCE
TABLE_3 = HE2_A_PAIRED_CONTRASTS
TABLE_4 = HE2_B_DEEP_COVERAGE
TABLE_5 = DOCUMENTARY_ASSOCIATION_AND_INVARIANCE
TABLE_6 = CONTROLLED_EXPLANATION_SUMMARY
TABLE_7 = HISTORICAL_BANK_SENSITIVITY

FIGURE_1 = ARCHITECTURE
FIGURE_2 = EXPLANATION_DIMENSION_PROFILE
FIGURE_3 = EXP11A_PROMOTED_FROM_SUPPLEMENTARY
FIGURE_4 = PRIMARY_HE2_EVIDENCE

FULL_NUMERIC_VECTOR_DUPLICATION_IN_PROSE = NONE
NEW_SCIENTIFIC_CONTENT = NO
```

Prove that scientific prose outside the explicitly permitted presentation-compaction blocks is unchanged except for table/figure numbering and cross-reference mechanics.

# 13. DOCX / OOXML contract

The cumulative V02 Word must be edited directly from the exact V01 Word baseline.

Preserve:

```text
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Run:

- ZIP/OOXML integrity;
- OOXML part inventory;
- comments and anchors;
- comments.xml byte identity against FAST-F02 V01 baseline;
- tracked changes;
- relationship/media inventory;
- table count;
- drawing count;
- full render;
- visual QA of every page;
- detailed QA of all pages containing Tables 1–7 and Figures 1–4;
- full-detail QA of End Matter;
- Markdown/DOCX visible-text equivalence for all changed blocks.

Required expected main DOCX structural counts after correction:

```text
MAIN_TABLES = 7
MAIN_DRAWINGS = 6
```

Explanation:

- four publication figures;
- inherited non-figure drawings/media may remain;
- report exact drawing inventory rather than assuming every drawing is a scientific figure.

For the Supplementary DOCX:

- seven tables;
- one scientific figure;
- zero tracked changes;
- source-value identity for Tables S1–S7;
- no former Figure S2 duplicate;
- full render and visual QA.

# 14. Figure QA

## New Figure 2

Prove data identity against:

`he4_qualitative_dimension_metrics_v0.2.csv@c119cc8d05148ad893d7c7687b9f4495c24fc49b`

Verify all eight means exactly.

## Promoted Figure 3

Prove the main-document embedded scientific image/content derives from the approved G6-FIG-03 asset without scientific alteration.

Do not redraw it from scratch if the approved asset can be embedded directly.

## Figure 4

Prove current HE2 figure scientific content is unchanged aside from mechanical numbering/caption reference.

# 15. Response minimum fields

Report at least:

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = FAST_FINALIZATION / FAST_F02_CORRECTIVE_PRESENTATION

PROMPT_IDENTITY = PASS / BLOCKED
AUTHORIZATION_IDENTITY = PASS / BLOCKED

BASELINE_MAIN_MD_IDENTITY = PASS / BLOCKED
BASELINE_MAIN_DOCX_IDENTITY = PASS / BLOCKED
BASELINE_SUPPLEMENTARY_MD_IDENTITY = PASS / BLOCKED
BASELINE_SUPPLEMENTARY_DOCX_IDENTITY = PASS / BLOCKED

MAIN_TABLE_COUNT = ...
MAIN_FIGURE_COUNT = ...
SUPPLEMENTARY_TABLE_COUNT = ...
SUPPLEMENTARY_FIGURE_COUNT = ...

TABLE_2_SOURCE_IDENTITY = PASS / BLOCKED
TABLE_3_SOURCE_IDENTITY = PASS / BLOCKED
TABLE_4_SOURCE_IDENTITY = PASS / BLOCKED
TABLE_5_SOURCE_IDENTITY = PASS / BLOCKED
TABLE_6_SOURCE_IDENTITY = PASS / BLOCKED
TABLE_7_SOURCE_IDENTITY = PASS / BLOCKED

FIGURE_2_SOURCE_IDENTITY = PASS / BLOCKED
FIGURE_3_PROMOTION_IDENTITY = PASS / BLOCKED
FIGURE_4_CONTENT_PRESERVED = PASS / BLOCKED

PROSE_NUMERIC_DEDUPLICATION = PASS / BLOCKED
SCIENTIFIC_SCOPE_PRESERVED = PASS / BLOCKED
NEW_SCIENTIFIC_CONTENT = NO / BLOCKED

AUTHOR_ADMINISTRATIVE_FIELDS = BLANK / PASS
AI_DISCLOSURE_PRESERVED = PASS / BLOCKED
REFERENCE_BIJECTION = PASS_25_OF_25 / BLOCKED

COMMENTS = ...
COMMENTS_XML_BYTE_IDENTICAL = PASS / BLOCKED
TRACKED_CHANGES = ...
ZIP_OOXML_INTEGRITY = ...
MAIN_DOCX_TABLE_COUNT = ...
MAIN_DOCX_DRAWING_COUNT = ...
FULL_MAIN_DOCX_PAGE_COUNT = ...
FULL_MAIN_DOCX_RENDER = ...
FULL_MAIN_DOCX_VISUAL_QA = ...

SUPPLEMENTARY_DOCX_TABLE_COUNT = ...
SUPPLEMENTARY_DOCX_DRAWING_COUNT = ...
FULL_SUPPLEMENTARY_DOCX_PAGE_COUNT = ...
FULL_SUPPLEMENTARY_DOCX_RENDER = ...
FULL_SUPPLEMENTARY_DOCX_VISUAL_QA = ...

CANDIDATE_MD_SHA256 = ...
CANDIDATE_MD_EXPECTED_GIT_BLOB = ...
CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

SUPPLEMENTARY_MD_SHA256 = ...
SUPPLEMENTARY_MD_EXPECTED_GIT_BLOB = ...
SUPPLEMENTARY_DOCX_SHA256 = ...
SUPPLEMENTARY_DOCX_SIZE_BYTES = ...

FIGURE_2_PNG_SHA256 = ...
FIGURE_2_SVG_GIT_BLOB = ...

POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO / YES + REASON
EXPECTED_EXIT = FAST_F02_V02_COMPLETED_PENDING_GESTORA_AUDIT
```

# 16. Stop condition

Stop exactly at:

`FAST_F02_V02_COMPLETED_PENDING_GESTORA_AUDIT`

Do not begin FAST-F03 or Experimental G8-F01.
