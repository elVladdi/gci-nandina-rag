# Internal Review — Prompt 20 / FAST-F02 V03 Presentation-Consistency Correction V01

## Result

```text
REVIEW_RESULT = PASS
PHASE = FAST_FINALIZATION / FAST_F02_V03_PRESENTATION_CONSISTENCY

PROMPT =
article/prompts/20_FAST_F02_V03_PRESENTATION_CONSISTENCY_CORRECTION_V01.md
PROMPT_GIT_BLOB =
f544ce7f00109ce6628e87672a2cd2c129be4053

SOURCE_REVIEW =
article/reviews/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_INTERNAL_REVIEW_V01.md
SOURCE_REVIEW_GIT_BLOB =
a7d03575854aa5e528b7118233621e32ca07c40c

SCIENTIFIC_RECOMPUTATION = NONE
NEW_INFERENCE = NONE
NEW_LITERATURE = NONE
EXPERIMENTAL_REAUDIT_REQUIRED = NO
READY_FOR_EXECUTION_AUTHORIZATION = YES
```

## Scope

PASS.

The prompt fixes only the four blocking presentation/traceability defects found in FAST-F02 V02:

- missing Spanish Figure 2 and Figure 3 image instances;
- stale Supplementary DOCX reading note;
- Figure 2 PNG handoff hash mismatch;
- Figure 2 SVG/PNG presentation inconsistency.

It also corrects the Managing-AI drawing-count contract from 6 to 8 scientific drawing instances for the bilingual internal master.

## Baselines

PASS.

The prompt binds to the exact V02 main MD/DOCX and Supplementary MD/DOCX hashes delivered under response 19.

## Scientific freeze

PASS.

No table value, inferential result, claim, reference, End Matter science, hypothesis disposition or Supplementary scientific source may change.

## Figure 2 canonicalization

PASS.

The prompt requires one canonical visual source for SVG and PNG, preserving exactly the eight frozen qualitative means, and requires the exact same PNG bytes in English and Spanish DOCX instances.

## Word QA

PASS.

The prompt preserves 48 comments and zero tracked changes, corrects table-row splitting and figure-caption separation, and requires complete rendering and visual inspection.

## Final disposition

```text
PROMPT_INTERNAL_REVIEW_RESULT = PASS
READY_FOR_FAST_F02_V03_EXECUTION_AUTHORIZATION = YES
```
