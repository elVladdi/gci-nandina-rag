# 20 — FAST-F02 V03 Presentation-Consistency Correction V01

## Role

Act exclusively as **IA de Redacción científica** for GIC-NANDINA.

Execute only the narrow FAST-F02 V03 presentation-consistency correction authorized by the live governance decision.

Do not act as IA Gestora, IA Experimental, or Author.

No new science is authorized.

## Governing documents

Read completely:

- `article/governance/D213_FAST_F02_V02_AUDIT_FAILURE_V03_CORRECTION_REQUIRED.md`;
- `article/reviews/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_INTERNAL_REVIEW_V01.md`;
- `article/prompts/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_V01.md`;
- `article/governance/D208_FAST_F02_AUTHOR_FIELDS_INTENTIONALLY_BLANK.md`;
- current `article/ARTICLE_STATUS.md`;
- current `article/ARTICLE_WRITING_PLAN.md`;
- `article/STYLE_GUIDE.md`.

Execution authorization must bind explicitly to this prompt and its exact Git blob. Otherwise stop at preflight.

# 1. Exact V02 corrective baselines

## Main Markdown

`ARTICLE_MASTER_CANDIDATE_FAST_F02_V02.md`

```text
EXPECTED_SHA256 =
351fbd5a981f3c430b8debfa5fa360c4e079301e7591c653908a8061cffb28ef
EXPECTED_GIT_BLOB =
7ac057a2d0b92322757c3da2b9fc36fa8b66db4c
EXPECTED_SIZE_BYTES = 298483
```

## Main DOCX

`ARTICLE_MASTER_CANDIDATE_FAST_F02_V02.docx`

```text
EXPECTED_SHA256 =
489f0f1df62fa0d661efd601b8155a4416db7a95a6cb45636552c3bb7b6d8524
EXPECTED_SIZE_BYTES = 605152
EXPECTED_PAGE_COUNT = 82
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Edit this exact DOCX directly. Do not reconstruct it from Markdown.

## Supplementary Markdown

`SUPPLEMENTARY_MATERIAL_FAST_F02_V02.md`

```text
EXPECTED_SHA256 =
f9e5eaedf7a0e6ee797681612118e8bda8fb42c5d613ad50644b204bebbd023b
EXPECTED_GIT_BLOB =
da7125d1ca7f89b7009ed05f8a8d088a6a0235af
```

## Supplementary DOCX

`SUPPLEMENTARY_MATERIAL_FAST_F02_V02.docx`

```text
EXPECTED_SHA256 =
0a84da58dd1b55e2824dd28b9105a17ae050dfcc8245c26a5e0c71c8255a909c
EXPECTED_SIZE_BYTES = 122133
EXPECTED_PAGE_COUNT = 20
EXPECTED_TRACKED_CHANGES = 0
```

If any baseline fails identity verification, stop at preflight.

# 2. Correction A — restore complete Spanish figure mirror

FAST-F02 V02 contains all four main figures in the English publication-facing master, but the Spanish semantic-control mirror contains image objects only for Figures 1 and 4.

Insert the **same Figure 2 and Figure 3 scientific images** into Part II, immediately before their already existing Spanish captions, preserving the exact same scientific content used in Part I.

Required final Markdown image-reference inventory:

```text
EN Figure 1 = PRESENT
EN Figure 2 = PRESENT
EN Figure 3 = PRESENT
EN Figure 4 = PRESENT

ES Figura 1 = PRESENT
ES Figura 2 = PRESENT
ES Figura 3 = PRESENT
ES Figura 4 = PRESENT

TOTAL_MAIN_MD_IMAGE_REFERENCES = 8
```

Required final DOCX drawing contract:

```text
SCIENTIFIC_FIGURE_IDENTITIES = 4
EN_DRAWING_INSTANCES = 4
ES_DRAWING_INSTANCES = 4
TOTAL_SCIENTIFIC_DRAWING_INSTANCES = 8
UNIQUE_SCIENTIFIC_MEDIA_ASSETS = 4
```

Reuse the same media asset for the English and Spanish instance of each scientific figure. Do not create a scientifically different Spanish rendering.

This corrects the drawing-count inconsistency in Prompt 19. The old expected count of 6 is superseded by D-213.

# 3. Correction B — Supplementary V03 visible-text consistency

The V02 Supplementary Markdown is scientifically correct and must remain semantically unchanged.

The V02 Supplementary DOCX page-1 reading note is stale.

Replace:

`Figures S1–S2 preserve the approved G6 scientific content.`

with wording semantically identical to the V02 Markdown reading note:

```text
Figure S1 preserves the approved G6-FIG-02 scientific content.
Former Figure S2 / G6-FIG-03 has been removed from the Supplementary package
because the same approved scientific figure is promoted to main Figure 3.
```

Required final Supplementary inventory:

```text
TABLES_S1_TO_S7 = PRESENT / UNCHANGED
FIGURE_S1 = PRESENT
FIGURE_S2 = ABSENT
DRAWING_COUNT = 1
UNUSED_FIGURE_S2_MEDIA = NONE
```

No Supplementary table value may change.

# 4. Correction C — canonicalize Figure 2 artifact identity

FAST-F02 V02 has one scientific Figure 2 dataset but two presentation variants:

- the versioned SVG;
- the PNG embedded in the main DOCX.

Create a single canonical Figure 2 V02 visual and derive both formats from the same plotting/rendering source.

Use the current **main-DOCX embedded Figure 2 visual appearance** as the presentation target because it already passed readability inspection and contains the correct eight frozen means.

Frozen values, exactly:

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

Required canonical files:

`article/figures/FAST_F02_Figure2_Explanation_Quality_V02.svg`

and real handoff file:

`FAST_F02_Figure2_Explanation_Quality_V02.png`

Requirements:

- same title, axes, labels, bar order, grayscale/print-safe design and value labels in SVG and PNG;
- x-axis fixed 0–2;
- no subtitle in one format unless the same subtitle appears in the other;
- no CI;
- no p-values;
- no significance marks;
- no invented threshold;
- no change to the eight means;
- rasterize/export PNG from the same canonical figure source used for SVG.

Update the English and Spanish manuscript instances of Figure 2 to use the new canonical V02 PNG.

The exact same PNG bytes must be embedded for both language instances.

Report the final PNG SHA-256 and the SVG Git blob.

The real PNG delivered to the Author must match the reported SHA exactly.

# 5. Correction D — narrow visual-layout QA

Do not change scientific wording or values.

Apply only these layout corrections:

1. Keep each Figure 2 image and its caption together on the same page if feasible.
2. Keep each Figure 3 image and caption together on the same page if feasible.
3. Prevent individual table rows from splitting across pages for Tables 2–7 in both languages.
4. Repeat table header rows when a table continues to another page.
5. Adjust Table 7 column widths/typography so Design-note text does not break words unnaturally in English or Spanish.

No landscape conversion is required unless it is the only way to preserve readability; prefer conservative portrait-layout correction.

# 6. Freeze everything else

The following are frozen and must not change semantically:

- all seven main table identities and numerical values;
- Figure 1 scientific content;
- Figure 3 scientific content;
- Figure 4 scientific content;
- Results interpretations already approved by the V02 content audit;
- Abstract, Introduction, Related Work, Architecture, Methods, Discussion and Conclusion;
- Data availability;
- Code and reproducibility resources;
- 25-reference bibliography;
- Supplementary Tables S1–S7;
- Supplementary Figure S1;
- AI disclosure;
- author-administrative fields remain blank.

No new claim, analysis, experiment, statistic, literature or inference.

# 7. Output versions

Create/version:

1. `article/sections/fast/FAST_F02_V03_PRESENTATION_CONSISTENCY_CORRECTION_V01.md`
2. `article/figures/FAST_F02_Figure2_Explanation_Quality_V02.svg`
3. `article/manifests/FAST_F02_TABLE_FIGURE_INVENTORY_V03.md`
4. `article/supplementary/SUPPLEMENTARY_MATERIAL_FAST_F02_V03.md`
5. `article/responses/20_FAST_F02_V03_PRESENTATION_CONSISTENCY_CORRECTION_RESPONSE_V01.md`

Deliver as real files:

6. `ARTICLE_MASTER_CANDIDATE_FAST_F02_V03.md`
7. `ARTICLE_MASTER_CANDIDATE_FAST_F02_V03.docx`
8. `SUPPLEMENTARY_MATERIAL_FAST_F02_V03.md`
9. `SUPPLEMENTARY_MATERIAL_FAST_F02_V03.docx`
10. `FAST_F02_Figure2_Explanation_Quality_V02.png`

If feasible, also deliver the SVG as a real file.

Do not promote a canonical master.

# 8. Main Markdown acceptance contract

Prove:

```text
MAIN_TABLE_IDENTITIES = 7
MAIN_FIGURE_IDENTITIES = 4

EN_IMAGE_REFERENCES = 4
ES_IMAGE_REFERENCES = 4
TOTAL_IMAGE_REFERENCES = 8

FIGURE_2_EN_ES_PATH_IDENTITY = PASS
FIGURE_3_EN_ES_PATH_IDENTITY = PASS

SCIENTIFIC_VALUES_CHANGED = NO
PROSE_SCIENTIFIC_MEANING_CHANGED = NO
```

# 9. DOCX / OOXML acceptance contract

Main DOCX:

```text
ZIP_OOXML_INTEGRITY = PASS
COMMENTS = 48
COMMENTS_XML_BYTE_IDENTICAL_TO_V02 = PASS
COMMENT_ANCHORS_IDENTICAL = PASS
TRACKED_CHANGES = 0

SCIENTIFIC_DRAWING_INSTANCES = 8
UNIQUE_SCIENTIFIC_MEDIA_ASSETS = 4

FIGURE_2_EN_MEDIA_SHA256 = <same>
FIGURE_2_ES_MEDIA_SHA256 = <same>
FIGURE_3_EN_MEDIA_SHA256 = <same>
FIGURE_3_ES_MEDIA_SHA256 = <same>
```

Supplementary DOCX:

```text
TABLE_COUNT = 7
DRAWING_COUNT = 1
TRACKED_CHANGES = 0
VISIBLE_READING_NOTE = CORRECT_V03
FIGURE_S2_TEXTUAL_CLAIM = ABSENT
FIGURE_S2_MEDIA = ABSENT
```

# 10. Render / visual QA

Render the complete main and Supplementary DOCX.

Inspect every page.

At minimum report:

```text
MAIN_PAGE_COUNT = ...
MAIN_FULL_RENDER = PASS / BLOCKED
MAIN_VISUAL_QA = PASS / BLOCKED

SPANISH_FIGURE_2_VISIBLE = PASS / BLOCKED
SPANISH_FIGURE_3_VISIBLE = PASS / BLOCKED
FIGURE_2_CAPTION_KEEP = PASS / BLOCKED
FIGURE_3_CAPTION_KEEP = PASS / BLOCKED
TABLE_ROW_SPLIT_QA = PASS / BLOCKED
TABLE_7_WORD_WRAP_QA = PASS / BLOCKED

SUPPLEMENTARY_PAGE_COUNT = ...
SUPPLEMENTARY_FULL_RENDER = PASS / BLOCKED
SUPPLEMENTARY_VISUAL_QA = PASS / BLOCKED
SUPPLEMENTARY_READING_NOTE_QA = PASS / BLOCKED
```

# 11. Response minimum fields

Report:

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = FAST_FINALIZATION / FAST_F02_V03_PRESENTATION_CONSISTENCY

PROMPT_IDENTITY = PASS / BLOCKED
AUTHORIZATION_IDENTITY = PASS / BLOCKED
ALL_BASELINE_IDENTITIES = PASS / BLOCKED

R01_SPANISH_FIGURE_MIRROR = PASS / BLOCKED
R02_SUPPLEMENTARY_READING_NOTE = PASS / BLOCKED
R03_FIGURE2_PNG_HANDOFF_IDENTITY = PASS / BLOCKED
R04_FIGURE2_SVG_PNG_CANONICALIZATION = PASS / BLOCKED

MAIN_TABLE_IDENTITIES = 7
MAIN_FIGURE_IDENTITIES = 4
MAIN_DRAWING_INSTANCES = ...
MAIN_UNIQUE_MEDIA_ASSETS = ...

SUPPLEMENTARY_TABLES = 7
SUPPLEMENTARY_DRAWINGS = 1

COMMENTS = ...
TRACKED_CHANGES = ...

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

NEW_SCIENTIFIC_CONTENT = NO
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO

EXPECTED_EXIT = FAST_F02_V03_COMPLETED_PENDING_GESTORA_AUDIT
```

# 12. Stop condition

Stop exactly at:

`FAST_F02_V03_COMPLETED_PENDING_GESTORA_AUDIT`

Do not begin FAST-F03 or Experimental G8-F01.
