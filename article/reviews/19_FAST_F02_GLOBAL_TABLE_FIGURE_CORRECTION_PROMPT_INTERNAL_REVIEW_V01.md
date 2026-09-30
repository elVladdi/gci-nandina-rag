# Internal Review — Prompt 19 / FAST-F02 Global Table-Figure Correction V01

## Result

```text
REVIEW_RESULT = PASS
PHASE = FAST_FINALIZATION / FAST_F02_CORRECTIVE_PRESENTATION

PROMPT =
article/prompts/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_V01.md
PROMPT_GIT_BLOB =
19f205ed87f7ce67ba6fe22e3d93c6fea3907ef7

GOVERNANCE = D-211
GLOBAL_EDITORIAL_AUDIT =
article/reviews/19_FAST_F02_GLOBAL_TABLE_FIGURE_EDITORIAL_AUDIT_V01.md
GLOBAL_EDITORIAL_AUDIT_GIT_BLOB =
f622b55336f5549472f8e26aeceba71aed2af009

SCIENTIFIC_RECOMPUTATION = NONE
NEW_INFERENCE = NONE
NEW_LITERATURE = NONE
EXPERIMENTAL_REAUDIT_REQUIRED = NO_BY_DEFAULT
READY_FOR_EXECUTION_AUTHORIZATION = YES
```

## 1. Scope

PASS.

The prompt corrects only scientific presentation: table structure, figure placement/creation from frozen values, prose deduplication, numbering and cross-references.

It does not reopen experimental results, hypotheses, literature, End Matter scientific boundaries, author fields, or the 25-reference corpus.

## 2. Baselines

PASS.

The prompt binds to the exact four FAST-F02 V01 handoff files:

- main MD SHA-256 `c6909699...`;
- main DOCX SHA-256 `bd584ce9...`;
- Supplementary MD SHA-256 `fd2ff320...`;
- Supplementary DOCX SHA-256 `ad6b7f5c...`.

The cumulative DOCX must be edited directly rather than reconstructed.

## 3. Table plan

PASS.

Seven main tables are justified by function rather than quota:

- one benchmark overview;
- one descriptive candidate-performance table;
- one HE2_A inferential contrast matrix;
- one HE2_B table;
- one documentary-association/invariance table;
- one explanation-evaluation summary;
- one historical-bank sensitivity summary.

Dense blocks already covered by Supplementary S2/S6 are explicitly not promoted into redundant main tables.

## 4. Figure plan

PASS.

Four main figures are justified:

- architecture;
- qualitative explanation-dimension profile;
- approved EXP11A run-level sensitivity figure promoted from Supplementary;
- primary HE2 evidence.

The new qualitative profile uses exactly eight frozen means from the canonical dimension-metrics CSV; no new statistic is created.

G6-FIG-03 is relocated without scientific alteration. It is removed from Supplementary to prevent exact duplication.

## 5. Anti-redundancy

PASS.

The prompt explicitly separates:

```text
TABLE = EXACT COMPARISON VALUES
FIGURE = PATTERN / PROFILE
PROSE = INTERPRETATION / LIMITS / FEW ANCHOR VALUES
```

It requires removal of the full HE2_A interval vector from prose and compaction of corrective-sensitivity/error-support passages toward existing Supplementary tables.

## 6. Scientific controls

PASS.

Forbidden:

- new experiment;
- new metric;
- new CI;
- new p-value;
- new inferential test;
- new hypothesis disposition;
- new literature/reference;
- new scientific claim.

No Experimental re-audit is required by default because every numerical object is an exact representation or relocation of frozen evidence.

## 7. Word/visual QA

PASS.

The prompt requires preservation of 48 comments, zero tracked changes, OOXML integrity, complete rendering and visual QA, MD/DOCX equivalence, exact table/figure counts, and detailed inspection of all visual objects.

## Final disposition

```text
PROMPT_INTERNAL_REVIEW_RESULT = PASS
READY_FOR_FAST_F02_V02_CORRECTIVE_EXECUTION_AUTHORIZATION = YES
```
