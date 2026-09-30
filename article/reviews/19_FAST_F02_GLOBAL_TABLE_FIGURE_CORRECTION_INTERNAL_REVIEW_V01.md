# Internal Review — FAST-F02 V02 Global Table/Figure Correction

## Result

```text
REVIEW_RESULT = FAIL_CORRECTION_REQUIRED
PHASE = FAST_FINALIZATION / FAST_F02_CORRECTIVE_PRESENTATION

SOURCE_RESPONSE =
article/responses/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_RESPONSE_V01.md@f2adee6a77ec925f9d2fa413488654e9735ec421
SOURCE_RESPONSE_GIT_BLOB =
17797b884a945b99c9133999f4e631a28f743651

AUTHORIZATION = D-212
PROMPT_GIT_BLOB =
19f205ed87f7ce67ba6fe22e3d93c6fea3907ef7

CANDIDATE_MD_SHA256 =
351fbd5a981f3c430b8debfa5fa360c4e079301e7591c653908a8061cffb28ef
CANDIDATE_MD_GIT_BLOB =
7ac057a2d0b92322757c3da2b9fc36fa8b66db4c

CANDIDATE_DOCX_SHA256 =
489f0f1df62fa0d661efd601b8155a4416db7a95a6cb45636552c3bb7b6d8524
CANDIDATE_DOCX_SIZE_BYTES = 605152
CANDIDATE_DOCX_PAGE_COUNT = 82

SUPPLEMENTARY_MD_SHA256 =
f9e5eaedf7a0e6ee797681612118e8bda8fb42c5d613ad50644b204bebbd023b
SUPPLEMENTARY_MD_GIT_BLOB =
da7125d1ca7f89b7009ed05f8a8d088a6a0235af

SUPPLEMENTARY_DOCX_SHA256 =
0a84da58dd1b55e2824dd28b9105a17ae050dfcc8245c26a5e0c71c8255a909c
SUPPLEMENTARY_DOCX_SIZE_BYTES = 122133
SUPPLEMENTARY_DOCX_PAGE_COUNT = 20

CONTENT_TABLE_AUDIT = PASS
SCIENTIFIC_SCOPE_AUDIT = PASS
REFERENCE_INTEGRITY = PASS
NEW_SCIENCE = NO
EXPERIMENTAL_REAUDIT_REQUIRED = NO

PRESENTATION_CONSISTENCY = FAIL
BILINGUAL_FIGURE_MIRROR = FAIL
SUPPLEMENTARY_MD_DOCX_EQUIVALENCE = FAIL
FIGURE_2_ARTIFACT_IDENTITY = FAIL
VISUAL_QA = FAIL_MINOR_LAYOUT_PLUS_BLOCKING_CONSISTENCY

FAST_F02 = NOT_APPROVED
AUTHOR_APPROVAL_GATE = CLOSED
CANONICAL_PROMOTION = NOT_AUTHORIZED
```

## 1. What passed

The four primary FAST-F02 V02 handoff files match the identities reported by Writing AI:

```text
MAIN_MD = PASS
MAIN_DOCX = PASS
SUPPLEMENTARY_MD = PASS
SUPPLEMENTARY_DOCX = PASS
```

The main Markdown changes are confined to the authorized English/Spanish Results presentation blocks and the two Supplementary-material statements. All other top-level scientific sections are byte-identical to FAST-F02 V01.

The seven main table identities are present in English and Spanish. The numerical values in Tables 2–7 match the frozen sources required by Prompt 19.

The English publication-facing Results implementation is substantively correct:

- Table 2 carries the four-method observed retrieval vectors;
- Table 3 carries the 15 HE2_A paired contrasts and frozen 99% CIs;
- Table 4 preserves HE2_B;
- Table 5 carries documentary association/invariance;
- Table 6 carries the controlled-explanation summary;
- Table 7 carries the historical-bank sensitivity summaries;
- English Figures 1–4 are present;
- the long HE2_A numeric vector was removed from prose;
- corrective-sensitivity and error/support detail are delegated to Supplementary S6/S2.

No new experiment, metric, CI, p-value, hypothesis disposition, literature or scientific claim was introduced.

The main DOCX also passes structural integrity:

```text
ZIP_OOXML = PASS
COMMENTS = 48
COMMENTS_XML_BYTE_IDENTICAL_TO_V01 = PASS
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
TRACKED_CHANGES = 0
UNIQUE_MEDIA_PARTS = 4
RAW_DRAWING_INSTANCES = 6
RAW_TABLE_ELEMENTS = 16
```

## 2. Blocking finding R01 — Spanish mirror is missing Figure 2 and Figure 3 image objects

Prompt 19 Section 8 required the Spanish semantic-control mirror to have:

```text
same seven table objects;
same four main figures;
same table/figure order;
semantically equivalent captions and interpretation.
```

The delivered V02 Markdown contains Spanish image references for Figure 1 and Figure 4 only.

It contains captions for Spanish Figure 2 and Figure 3, but **no image references** for those two figures.

The DOCX reproduces the same defect:

- page 69 contains the Spanish Figure 2 caption but no Figure 2 image;
- page 70 contains the Spanish Figure 3 caption but no Figure 3 image;
- Spanish Figure 4 is correctly present on page 71 with its caption on page 72.

This explains the raw drawing count of 6:

```text
Figure 1 EN + ES = 2 drawing instances
Figure 2 EN only = 1
Figure 3 EN only = 1
Figure 4 EN + ES = 2
TOTAL = 6
```

The correct bilingual internal-master count is:

```text
4 scientific figures × 2 language instances = 8 drawing instances
4 unique scientific media assets
```

### Managing-AI prompt defect

Prompt 19 itself contained an internal inconsistency: it required the same four figures in the Spanish mirror but separately stated an expected main-DOCX drawing count of 6.

That drawing-count contract was under-specified/incorrect for the bilingual master and contributed to this defect.

Classification:

```text
FASTF02V02-R01 = BLOCKING
ROOT_CAUSE = PROMPT_CONTRACT_INCONSISTENCY + EXECUTION_OMISSION
SCIENTIFIC_RECOMPUTATION = NOT_REQUIRED
```

## 3. Blocking finding R02 — Supplementary V02 DOCX reading note contradicts V02 content

The Supplementary V02 Markdown is correct: it states that Tables S1–S7 are retained, Figure S1 remains, and former Figure S2 / G6-FIG-03 was promoted to main Figure 3.

The real Supplementary V02 DOCX has seven tables and one drawing, and the former S2 media was removed. However, its visible page-1 reading note still says:

```text
Figures S1–S2 preserve the approved G6 scientific content.
```

This is false for V02 and contradicts both the Markdown and the actual DOCX contents.

Therefore Writing AI's claim of visible-text equivalence is not valid.

Classification:

```text
FASTF02V02-R02 = BLOCKING
TYPE = MD_DOCX_VISIBLE_TEXT_MISMATCH
SCIENTIFIC_CONTENT_CHANGE = NO
```

## 4. Blocking finding R03 — Figure 2 PNG handoff identity does not match the response

The response records:

```text
FIGURE_2_PNG_SHA256 =
a47669390563206cb20ac2adac3622271008fba4fb06ded9be703da53c6b4b77
```

The Figure 2 PNG embedded in the main DOCX matches that SHA and has dimensions 3116×1918.

The PNG supplied in the current handoff has:

```text
SHA256 =
ab36a372a459c8621c1dc38a4530caf2f62af4d9021289e0c87b4bf412a9fb41
DIMENSIONS = 2047×1260
```

The plotted scientific values are visually equivalent, but the exact binary identity is not.

Because Prompt 19 required a real PNG deliverable and the response asserted an exact SHA, the handoff is not traceability-clean.

Classification:

```text
FASTF02V02-R03 = BLOCKING_HANDOFF_IDENTITY
SCIENTIFIC_DIFFERENCE = NONE_DETECTED
```

## 5. Blocking finding R04 — Figure 2 SVG and PNG are different presentation variants

The versioned SVG at:

`article/figures/FAST_F02_Figure2_Explanation_Quality_V01.svg`

Git blob:

`293298c3f1b9f987ef5f7c07c90bbfebdca5eb50`

is not the same presentation rendering as the PNG embedded in the manuscript.

The SVG contains, among other differences:

- a subtitle: “Frozen 50-case sample · descriptive means on the 0–2 rubric”;
- different bar geometry and label placement;
- different value-label placement.

The main-DOCX PNG uses the Matplotlib-style layout visible in the delivered manuscript.

Both encode the same eight frozen means, but Prompt 19 requested SVG + high-resolution PNG as representations of the same new publication figure.

For publication traceability, one canonical Figure 2 visual must generate both formats.

Classification:

```text
FASTF02V02-R04 = BLOCKING_PRESENTATION_IDENTITY
NEW_SCIENCE_REQUIRED = NO
```

## 6. Visual-layout findings to correct in the same cycle

These do not independently reopen science, but should be corrected while FAST-F02 remains open.

### V01 — English Figure 2 separated from its caption

The Figure 2 image is on main-DOCX page 28 while its caption starts on page 29.

Keep the image and caption together if feasible.

### V02 — Spanish Table 6 row splits across pages

The Spanish “Cumplimiento del esquema” row begins at the bottom of page 68 and its interpretation cell continues alone at the top of page 69.

Prevent table rows from splitting across pages and repeat header rows where a table continues.

### V03 — Table 7 narrow Design-note column

English and Spanish Table 7 produce undesirable mid-word wrapping in the Design note column (e.g. seed-superpopulation / superpoblación fragments).

Adjust widths or typography without changing text or values.

## 7. Supplementary structural status

Except for R02, the Supplementary relocation is correct:

```text
TABLES = 7
DRAWINGS = 1
TRACKED_CHANGES = 0
FORMER_FIGURE_S2_VISIBLE = NO
FORMER_FIGURE_S2_MEDIA = NO
FIGURE_S1 = PRESENT
```

The Supplementary Markdown correctly documents that only Figure S1 remains.

## 8. Required correction scope

A narrow FAST-F02 V03 presentation-consistency correction is sufficient.

Required actions:

1. insert Figure 2 and Figure 3 image objects/references into the Spanish mirror at the locations of their existing captions;
2. ensure the bilingual DOCX contains 8 scientific drawing instances and 4 unique scientific media assets;
3. correct the Supplementary DOCX reading note to match Supplementary Markdown V02;
4. canonicalize Figure 2 so SVG, PNG and both English/Spanish DOCX instances represent one presentation variant;
5. deliver the exact canonical PNG bytes and report their SHA;
6. keep figure and caption together where feasible;
7. prevent table-row splits and improve Table 7 wrapping;
8. preserve all science, values, tables, captions' scientific semantics, End Matter, references and comments.

## 9. Disposition

```text
FAST_F02_V02 = FAIL_CORRECTION_REQUIRED
FAST_F02_V03 = REQUIRED
AUTHOR_APPROVAL_GATE = CLOSED
CANONICAL_MASTER = ARTICLE_MASTER_V038
EXPERIMENTAL_REAUDIT_REQUIRED = NO

NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
NEXT_ACTION = PREPARE_AND_AUTHORIZE_NARROW_V03_CORRECTION
FAST_F03 = NOT_AUTHORIZED
```
