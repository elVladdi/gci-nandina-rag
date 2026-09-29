# Internal Review — Prompt 14 / G7-F03 A09+A10 Diagnostic Reranker V01

## Result

```text
REVIEW_RESULT = PASS
PHASE = PRE_FAST_SCIENTIFIC_CORRECTION
BLOCK = G7F03_A09_A10_DIAGNOSTIC_RERANKER

SOURCE_RESPONSE =
article/responses/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_RESPONSE_V01.md@05ed16e4e22c3d34cb37b32c176a947373d9dde4
SOURCE_RESPONSE_GIT_BLOB =
8613240e8c76e798a6803d355b8c1a33dd98bf38

SOURCE_SECTION =
article/sections/pre_fast/Diagnostic_Reranker_A09_A10_V01.md
SOURCE_SECTION_GIT_BLOB =
8a4578a992d20dc8f96ab88f08e95e666d4247c5

AUTHORIZATION = D-197
CANONICAL_INPUT_MASTER = ARTICLE_MASTER_V036

CANDIDATE_MD_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
CANDIDATE_MD_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1

CANDIDATE_DOCX_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
CANDIDATE_DOCX_SIZE_BYTES = 112705
CANDIDATE_DOCX_PAGE_COUNT = 73

GESTORA_DISPOSITION =
PASS_FOR_FOCUSED_EXPERIMENTAL_REAUDIT

AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_F01 = NOT_AUTHORIZED
```

## 1. Response and Git scope

PASS.

The completed response is versioned at commit
`05ed16e4e22c3d34cb37b32c176a947373d9dde4`.
That commit changes only the response file. The section artifact had already been materialized and is present with Git blob
`8a4578a992d20dc8f96ab88f08e95e666d4247c5`.

No canonical master, ARTICLE_STATUS, ARTICLE_WRITING_PLAN, governance decision, or experimental artifact was mutated by Writing AI.

## 2. Candidate Markdown identity and exact differential

PASS.

IA Gestora independently recomputed the uploaded cumulative Markdown:

```text
SIZE_BYTES = 283664
SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1
```

The candidate contains exactly one occurrence of each authorized insertion:

- A09_METHOD_EN;
- A10_RESULT_EN;
- A09_METHOD_ES;
- A10_RESULT_ES.

Removing each inserted paragraph together with its insertion separator restores exactly:

```text
SIZE_BYTES = 279582
SHA256 =
8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8
GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90
```

These are the governed byte identity of ARTICLE_MASTER_V036.

Therefore:

```text
MARKDOWN_OUTSIDE_AUTHORIZED_BLOCKS_BYTE_EQUIVALENT_TO_V036 = PASS
AUTHORIZED_BLOCK_COUNT_MD = 4
UNAUTHORIZED_MARKDOWN_CHANGE = NONE
```

## 3. Scientific audit of A09 — method

PASS.

A09 reports the already executed diagnostic reranker as a separate path and correctly preserves the primary-flow authority boundary.

It is consistent with the frozen Phase-G sources in all material fields:

- closed v0.2 pool;
- nominal depth 100 and effective 63–100;
- `historical_first_80_normative_20`;
- deduplication by first appearance;
- uniform sample without replacement over sorted eligible case IDs;
- seed 0;
- 20 cases;
- 10 closed candidates per reranker input;
- labels used only for evaluation;
- local `qwen2.5:7b-instruct`;
- Ollama / Q4_K_M;
- `temperature=0`;
- JSON;
- no retry / one attempt per input;
- candidate closure 20/20;
- observed 19 reference-in-pool / 1 reference-out-of-pool;
- no pre-specified inferential test;
- no feedback to or replacement of the primary historical ranking/fixed Top-3.

The 19/1 property is correctly described as observed after sampling and not as a selection criterion.

No new experiment or retrospective protocol was introduced.

## 4. Scientific audit of A10 — results

PASS.

A10 accurately reports the frozen diagnostic values:

```text
sample_cases = 20
reference_in_pool = 19
reference_not_in_pool = 1

Top-1 = 0.50 -> 0.50
Top-3 = 0.65 -> 0.65
Top-5 = 0.80 -> 0.80
MRR = 0.6326 -> 0.6326

wins/ties/losses = 0/19/0
candidate_closure = 20/20
paired_inference = NOT RUN
```

The 0/19/0 denominator is correctly restricted to the 19 cases in which the reference code was present in the pool.

The wording remains descriptive. It explicitly does not claim:

- statistical equivalence;
- non-inferiority;
- superiority;
- generalization;
- a population-level null effect.

No p-value, confidence interval, new metric, or new inference was introduced.

## 5. Bilingual equivalence

PASS.

The four English/Spanish blocks preserve the same:

- sample size;
- pool configuration;
- model identity and execution constraints;
- candidate-closure result;
- 19/1 pool status;
- Top-k/MRR values;
- 0/19/0 result;
- inferential limitation;
- no-feedback boundary.

Natural lexical differences do not change scientific meaning.

## 6. Placement and manuscript boundaries

PASS.

The candidate places:

- A09 EN inside §4.5;
- A10 EN at the end of §5.2 before §5.3;
- A09 ES in the equivalent §4.5 location;
- A10 ES at the end of the equivalent §5.2 before §5.3.

No new numbered section is introduced.

Because the exact Markdown restoration to V036 passes, the following are independently proven unchanged in Markdown outside the four insertions:

- Title;
- Abstract;
- Keywords;
- §§1–3;
- all other §4 content;
- all other §5 content;
- Discussion §6;
- Conclusion §7;
- End Matter;
- Figure 1 placeholder;
- drafting notes.

## 7. DOCX identity and OOXML audit

PASS.

IA Gestora independently recomputed the uploaded DOCX identity:

```text
SIZE_BYTES = 112705
SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
ZIP_OOXML_INTEGRITY = PASS
OOXML_PART_COUNT = 14
```

Observed package parts are the expected 14-part package.

Independent structural counts:

```text
COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
```

The four authorized paragraphs each occur exactly once in the DOCX and their visible text is exactly equal to the corresponding Markdown paragraph.

Candidate `word/comments.xml` SHA-256 observed by IA Gestora:

`57bee5d04cc9ed51628a4e10baef0730c0a07b58b9d8c3b436c64657f32821ea`.

The current Gestora environment cannot rematerialize the prior corrected baseline DOCX raw bytes from Project Library, so the response's byte-for-byte baseline comparison of `comments.xml` and all unchanged OOXML parts was not recomputed a second time by Gestora. This is recorded as a provenance limitation, not a blocker, because:

1. the exact candidate package is independently available and structurally valid;
2. all governed comment and anchor counts remain 48;
3. tracked changes remain zero;
4. the only authorized visible text changes are the four paragraphs;
5. the Writing-AI response records its direct byte comparison against the verified exact D-197 baseline;
6. canonical integration remains blocked until Experimental re-audit and Author approval.

```text
BASELINE_NON_DOCUMENT_PARTS_BYTE_COMPARE_BY_GESTORA =
NOT_RECOMPUTED / NON_BLOCKING_PROVENANCE_LIMITATION

DOCX_STRUCTURAL_AUDIT = PASS
```

## 8. Render and visual QA

PASS.

IA Gestora independently rendered the delivered candidate with the canonical DOCX renderer.

```text
FULL_DOCX_PAGE_COUNT = 73
PAGES_REVIEWED = 1-73
FULL_DOCX_RENDER = PASS
FULL_DOCX_VISUAL_QA = PASS

INSERTION_PAGES_REVIEWED_AT_FULL_DETAIL =
20, 25, 56, 61, 62

CLIPPING = NONE_DETECTED
OVERLAP = NONE_DETECTED
MISSING_GLYPHS = NONE_DETECTED
BROKEN_LAYOUT = NONE_DETECTED
HEADER_FOOTER_DEFECTS = NONE_DETECTED
```

The extra page relative to the 72-page V036 baseline is consistent with normal reflow from the four added paragraphs and does not indicate a layout defect.

## 9. Scope controls

PASS.

```text
NEW_EXPERIMENT = NO
NEW_RESULT = NO
NEW_METRIC = NO
NEW_CI = NO
NEW_P_VALUE = NO
NEW_LITERATURE = NO
NEW_CITATION = NO

HE3_REDECIDED = NO
EXP12_REOPENED = NO
DIAGNOSTIC_RERANKER_PRIMARY_FLOW = NO
FINAL_F01_STARTED = NO
```

## 10. Gestora disposition

The A09+A10 correction satisfies Prompt 14 and D-197 for the purpose of the next gate.

```text
GESTORA_REVIEW_RESULT = PASS
MANDATORY_EDITORIAL_CORRECTIONS = NONE
MANDATORY_SCIENTIFIC_CORRECTIONS_BY_GESTORA = NONE

READY_FOR_FOCUSED_EXPERIMENTAL_REAUDIT = YES
READY_FOR_AUTHOR_APPROVAL = NO
READY_FOR_CANONICAL_PROMOTION = NO
FINAL_F01 = NOT_AUTHORIZED
```

The candidate must now return to IA Experimental for the focused G7-F03 re-audit required by D-195/D-197.
