# 19 — FAST-F02 Global Full-Body Table/Figure Editorial Audit V01

## Result

```text
AUDIT_RESULT = REVISION_REQUIRED
PHASE = FAST_FINALIZATION / FAST_F02_CORRECTIVE_PRESENTATION

AUTHOR_DECISION = FAST_F02_V01_APPROVAL_SUPERSEDED_BEFORE_INTEGRATION
GOVERNANCE = D-211

AUDITED_BASELINE_MD =
ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.md
AUDITED_BASELINE_MD_SHA256 =
c6909699b9b7272d12cbe57f02d5897b78c8a489c9105bdf69e23e4462e90dd4
AUDITED_BASELINE_MD_GIT_BLOB =
4c891641a86d0622cdc9fb7b2afee6f4691ee320

AUDITED_BASELINE_DOCX =
ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.docx
AUDITED_BASELINE_DOCX_SHA256 =
bd584ce9817ce8d251cbe43a6e737612039a5ba82c932f1637839d66466e9e31
AUDITED_BASELINE_DOCX_SIZE_BYTES = 356835
AUDITED_BASELINE_DOCX_PAGE_COUNT = 81

CURRENT_MAIN_TABLES = 3
CURRENT_MAIN_FIGURES = 2

RECOMMENDED_MAIN_TABLES_AFTER_CORRECTION = 7
RECOMMENDED_MAIN_FIGURES_AFTER_CORRECTION = 4

NEW_OR_RESTRUCTURED_MAIN_TABLE_ACTIONS = 4
NEW_OR_PROMOTED_MAIN_FIGURE_ACTIONS = 2

NEW_SCIENTIFIC_ANALYSIS = NO
NEW_INFERENCE = NO
EXPERIMENTAL_REAUDIT_REQUIRED = NO_BY_DEFAULT
```

## 1. Audit question

This audit was run over the complete English publication-facing body, not only the objects selected in FAST-F01.

The decision rule was not a numerical quota. A table or figure is justified only when it:

1. materially reduces cognitive load;
2. makes a comparison or pattern substantially easier to inspect;
3. does not duplicate another object without added function;
4. does not inflate the prominence of diagnostic or secondary material;
5. can be produced entirely from already frozen evidence without new scientific calculation or inference.

The Spanish semantic-control mirror must follow the same editorial structure after correction.

## 2. Overall finding

FAST-F01's three-table/two-figure selection was scientifically valid but editorially incomplete as a global presentation audit.

The current FAST-F02 V01 manuscript still contains several number-dense passages in Results whose primary function is comparison rather than interpretation. Some should become tables; others should be shortened because an existing main or supplementary table/figure already carries the numbers.

The audit does **not** recommend converting every quantitative paragraph into a visual object.

## 3. Main-table decisions

### T1 — Existing Table 1: retain

**Experimental benchmark and evaluation overview** remains useful and nonredundant.

Dataset composition repeated later in Sections 4.2.3 and 5.1 should be concise and should point back to Table 1 rather than create another dataset-composition table.

```text
ACTION = RETAIN
TABLE_AFTER_CORRECTION = Table 1
NEW_OBJECT = NO
```

### T2 — Add observed candidate-retrieval performance table

Current number-dense blocks:

- Section 5.2, historical H100 observed metrics;
- Section 5.2, flat/hierarchical/D1a observed metrics.

These values are currently split between prose and the descriptive columns embedded inside the inferential Table 2.

Create a compact descriptive table with methods as rows:

```text
Rows:
Historical BM25 H100
Flat normative BM25
Hierarchical normative BM25
Corrected D1a Text2Trade-inspired MNRL

Columns:
Top-1
Top-3
Top-5
Top-10
Top-50
MRR@100
```

Use the already reported/frozen observed values only.

The surrounding prose should retain only the main interpretation and one or two anchor values, not repeat the full row vectors.

```text
ACTION = CREATE
TABLE_AFTER_CORRECTION = Table 2
SCIENTIFIC_ROLE = DESCRIPTIVE_RQ1
```

### T3 — Restructure current HE2_A table into an inferential contrast matrix

The current Table 2 contains observed arm values and paired differences/CIs, while Section 5.6 repeats the entire set of 15 differences and confidence intervals in prose.

After T2 carries observed values, convert the current inferential content to a compact matrix:

```text
Rows:
Top-1
Top-3
Top-5
Top-10
MRR@100

Columns:
Flat BM25: Historical - comparator [99% CI]
Hierarchical BM25: Historical - comparator [99% CI]
Corrected D1a: Historical - comparator [99% CI]
```

Use exactly:
`outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv`
Git blob:
`cb68583ee2260e4455796bac99ad90995ca7ef92`

Section 5.6 must no longer spell out all 15 numeric CI triplets. It should state the inferential result and refer to Table 3 and Figure 2.

```text
ACTION = RESTRUCTURE_EXISTING_TABLE
CURRENT_TABLE = Table 2
TABLE_AFTER_CORRECTION = Table 3
SCIENTIFIC_ROLE = PRIMARY_INFERENTIAL_HE2_A
```

### T4 — Existing HE2_B deep-coverage table: retain and renumber

Current Table 3 remains scientifically and editorially appropriate.

Source:
`outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv`
Git blob:
`359e4e19b5ef1d44983c03039162209293b2a44c`

```text
ACTION = RETAIN_AND_RENUMBER
CURRENT_TABLE = Table 3
TABLE_AFTER_CORRECTION = Table 4
```

### T5 — Add documentary-association and ranking-invariance summary table

Section 5.3 currently carries a dense sequence of exact-association, HS6/HS4/chapter parent-context, historical-precedent, traceability and rank-invariance counts.

Create one compact table with rows for the distinct documentary/structural controls and columns for numerator/denominator, percentage and permitted interpretation.

Use the frozen Phase-F evidence only.

Governing source:
`docs/exp04_phase_f_historical_normative_integration_v02_results.md`
Git blob:
`01a4573d34c029efb0b055c7b90202842e914549`

Required distinctions:

- exact NANDINA-8 evidence;
- HS6 parent context;
- HS4 parent context;
- chapter parent context;
- historical-precedent coverage;
- complete traceability;
- case-level Top-3 membership/order invariance.

Do not present parent-context coverage as exact evidence and do not imply legal correctness.

```text
ACTION = CREATE
TABLE_AFTER_CORRECTION = Table 5
SCIENTIFIC_ROLE = RQ2_DOCUMENTARY_ASSOCIATION_AND_INVARIANCE
```

### T6 — Add controlled-explanation evaluation summary table

Section 5.4 currently reports multiple structural checks, schema compatibility, auditability, hard violations and warning-control outcomes in prose.

Create a compact aggregate table covering:

- Top-3 membership/order preserved;
- candidate-slot code/history/normative/rank consistency;
- schema compliance result and its prompt-schema mismatch qualification;
- auditable cases;
- non-auditable cases;
- hard violations;
- generic-normative-warning control present/missing and its descriptive subgroup result.

Do **not** place all eight qualitative dimension means in this table; those belong in Figure 3.

Governing frozen sources:

`outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_metrics_v0.2.json`
Git blob:
`843e1edd17a023f6c3d6f0b5235dd3fba86369c1`

`outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_warning_comparison_v0.2.csv`
Git blob:
`1cab0e8e7398a7299086fec7ad1ec28b2f706f2d`

```text
ACTION = CREATE
TABLE_AFTER_CORRECTION = Table 6
SCIENTIFIC_ROLE = RQ3_STRUCTURAL_AND_QUALITATIVE_SUMMARY
```

### T7 — Add historical-bank sensitivity summary table

The H25/H50/H75/H100 and H150/H200 passages in Section 5.5 are too number-dense for prose.

Create a summary table with:

```text
Condition
Observed runs
Top-1
Top-3
Top-5
Top-10
Top-50
MRR@100
Design note
```

Rows:

- H25
- H50
- H75
- H100 frozen reference
- H150
- H200

For H25/H50/H75, the prose may retain the already frozen Top-3 and MRR ranges if scientifically useful, but the full vectors must move to the table. Do not invent intervals.

Sources:

`outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv`
Git blob:
`cf3aedab5935d6af9b3ac7be7b51b954fcb9c403`

`outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv`
Git blob:
`76c8c6c588c7e809c6be64f7192f497c491fb692`

The table must make clear that H25/H50/H75/H100 and H150/H200 belong to related but not identical sensitivity designs and that no causal/monotonic size effect is identified.

```text
ACTION = CREATE
TABLE_AFTER_CORRECTION = Table 7
SCIENTIFIC_ROLE = DESCRIPTIVE_SENSITIVITY
```

## 4. Main-figure decisions

### F1 — Existing architecture figure: retain

```text
ACTION = RETAIN
FIGURE_AFTER_CORRECTION = Figure 1
```

### F2 — Existing primary HE2 figure: retain

The current Figure 2 remains the primary inferential visualization and complements exact-value Tables 2–4.

```text
ACTION = RETAIN
FIGURE_AFTER_CORRECTION = Figure 2
```

### F3 — Add qualitative explanation-dimension profile

The eight frozen qualitative dimensions are a pattern, not merely a list of values. Their profile is materially easier to inspect visually.

Create a simple horizontal bar chart with a fixed 0–2 axis and exactly these eight mean scores:

- traceability = 2.00;
- verifiability = 0.54;
- historical–normative evidence separation = 1.04;
- conclusion prudence = 1.78;
- fixed-Top-3 consistency = 1.96;
- detection of generic normative evidence = 1.68;
- candidate comparison = 1.46;
- utility for human audit = 1.26.

Canonical source:

`outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_dimension_metrics_v0.2.csv`
Git blob:
`c119cc8d05148ad893d7c7687b9f4495c24fc49b`

The caption must state:

- 50-case frozen qualitative sample;
- 0–2 rubric scale;
- AI_EXPERT_ROLE / LLM-as-judge, not human scoring;
- descriptive profile only;
- no CI, p-values or human-validation interpretation.

```text
ACTION = CREATE
FIGURE_AFTER_CORRECTION = Figure 3
SCIENTIFIC_ROLE = RQ3_DESCRIPTIVE_QUALITATIVE_PROFILE
```

### F4 — Promote the approved EXP11A sensitivity figure to the main body

The run-level variation across H25/H50-D1/H50-D2/H75/H100 is a genuinely graphical pattern and is central to the interpretation of the joint size/composition sensitivity.

Reuse the already approved G6-FIG-03 exactly in scientific content:

`figures/group6/g6_fig_03_exp11a.svg`
Git blob:
`1b2aca9aa9c2582cf0b7e16850cd5b22387cc771`

Approved PNG:
`figures/group6/g6_fig_03_exp11a.png`
Git blob:
`eaf59497ee49ab36d34d23e42cf002111bc9fe3e`

Source table:
`outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv`
Git blob:
`cf3aedab5935d6af9b3ac7be7b51b954fcb9c403`

Reuse the governed scientific caption contract from:
`docs/figures/group6/g6_caption_registry_v0.1.md`
Git blob:
`0dcb43cfa56dfce2e6955f960184069beb36ba76`

Its role remains descriptive/noncausal. Promotion is editorial placement only.

To avoid duplication, remove this same figure from the Supplementary package. G6-FIG-02 remains Supplementary Figure S1.

```text
ACTION = PROMOTE_EXISTING_APPROVED_FIGURE
CURRENT_LOCATION = SUPPLEMENTARY_FIGURE_S2
FIGURE_AFTER_CORRECTION = Figure 4
SCIENTIFIC_CONTENT_CHANGE = NO
```

## 5. Dense passages that should NOT create additional main objects

### 5.1 Partition composition and residual similarity

The partition sizes are already covered by Table 1. Keep residual exact/near-duplicate diagnostics in concise prose; three Jaccard thresholds do not justify another main table or figure.

```text
NEW_TABLE = NO
NEW_FIGURE = NO
```

### 5.2 Diagnostic LLM reranker

The 20-case reranker analysis is explicitly diagnostic and noninferential. A dedicated main table/figure would give it disproportionate visual prominence.

Retain a short prose summary.

```text
NEW_TABLE = NO
NEW_FIGURE = NO
```

### 5.3 Corrective normative-resource sensitivity

The long before/after metric vector in Section 5.5 should be sharply shortened and point to Supplementary Table S6.

Do not create a new main table.

```text
MAIN_PROSE = COMPACT
DETAIL = SUPPLEMENTARY_TABLE_S6
```

### 5.4 Error hierarchy and historical-support strata

The detailed counts and rates are already frozen in Supplementary Table S2.

Main prose should retain only the scientifically useful synthesis and cite Table S2.

```text
MAIN_PROSE = COMPACT
DETAIL = SUPPLEMENTARY_TABLE_S2
```

### 5.5 Full HE2_A interval vector

Do not create another table beyond the restructured Table 3. Remove the prose duplication and refer to Table 3/Figure 2.

```text
MAIN_PROSE = INTERPRETATION_ONLY
DETAIL = TABLE_3 + FIGURE_2
```

### 5.6 Methods/configuration numerics

BM25/LLM/runtime parameters remain in prose because they are procedural specifications rather than comparative result vectors. A separate configuration table is not required for this manuscript.

```text
NEW_TABLE = NO
NEW_FIGURE = NO
```

## 6. Anti-redundancy rule

After correction:

- tables carry exact comparison values;
- figures carry patterns/profiles;
- prose carries interpretation, scope and key anchor values;
- the same full numeric vector must not appear both in prose and a table;
- a main figure must not be duplicated as an identical Supplementary figure.

## 7. Supplementary consequences

After Figure S2 / G6-FIG-03 is promoted to main Figure 4:

```text
SUPPLEMENTARY_TABLES = S1-S7 / UNCHANGED
SUPPLEMENTARY_FIGURES = Figure S1 ONLY
REMOVED_FROM_SUPPLEMENTARY = former Figure S2 / G6-FIG-03
PROMOTED_TO_MAIN = Figure 4
```

Update the main End Matter statement and Supplementary reading note accordingly.

No supplementary scientific table is deleted.

## 8. Expected main-body presentation after correction

```text
MAIN_TABLES = 7
Table 1 = Experimental benchmark and evaluation overview
Table 2 = Observed candidate-retrieval performance by method
Table 3 = HE2_A paired Historical-minus-comparator differences with 99% CI
Table 4 = HE2_B deep-coverage contrast
Table 5 = Documentary-association and ranking-invariance summary
Table 6 = Controlled-explanation evaluation summary
Table 7 = Historical-bank sensitivity summary

MAIN_FIGURES = 4
Figure 1 = Architecture and authority boundaries
Figure 2 = Primary HE2 evidence
Figure 3 = Qualitative explanation-dimension profile
Figure 4 = EXP11A joint size-composition sensitivity
```

This is a recommendation derived from the full-body audit, not a preset quota.

## 9. Scientific boundary

```text
NEW_EXPERIMENT = FORBIDDEN
NEW_METRIC = FORBIDDEN
NEW_INFERENTIAL_TEST = FORBIDDEN
NEW_CI = FORBIDDEN
NEW_P_VALUE = FORBIDDEN
NEW_HYPOTHESIS_DISPOSITION = FORBIDDEN
NEW_LITERATURE = FORBIDDEN

ALLOWED =
EDITORIAL_REPRESENTATION /
RELOCATION_OF_ALREADY_APPROVED_FIGURE /
EXACT_TRANSCRIPTION_OF_FROZEN_VALUES /
ROUNDING_CONSISTENT_WITH_EXISTING_MAIN_TABLE_POLICY /
PROSE_DEDUPLICATION
```

## 10. Disposition

```text
GLOBAL_TABLE_FIGURE_AUDIT = COMPLETE
FAST_F02_V01 = REVISION_REQUIRED
CORRECTIVE_WRITING_PROMPT = REQUIRED
AUTHOR_APPROVAL_GATE = CLOSED
CANONICAL_MASTER = ARTICLE_MASTER_V038
FAST_F03 = NOT_AUTHORIZED
```
