# 22 — FAST-F03 V02 Residual Drafting-Note Cleanup V01

## Role

Act exclusively as **IA de Redacción científica** for GIC-NANDINA.

Execute only the narrow FAST-F03 V02 publication-cleanup correction defined here.

Do not act as IA Gestora, IA Experimental, or Author.

No new science is authorized.

## Governing state

Read completely:

- `article/responses/21_FAST_F03_SUBMISSION_ASSEMBLY_RESPONSE_V01.md@7b17c02a6ae9a92a70390b94904dc70f85a4d695`;
- `article/reviews/21_FAST_F03_SUBMISSION_ASSEMBLY_INTERNAL_REVIEW_V01.md`;
- `article/governance/D216_FAST_F02_V03_AUTHOR_APPROVAL_AND_V039_INTEGRATION.md`;
- `article/governance/D208_FAST_F02_AUTHOR_FIELDS_INTENTIONALLY_BLANK.md`;
- current `article/ARTICLE_STATUS.md`;
- current `article/ARTICLE_WRITING_PLAN.md`.

Execution requires an authorization decision that binds to this exact prompt Git blob.

# 1. Exact correction baselines

Use the real files supplied by the Author/Gestora:

## Main Markdown V01

`KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V01.md`

```text
EXPECTED_SHA256 =
ffe6cbe06b0e0f7f17c2ba8e6e839205588a88ff87b8706f55cf647d16c9363a
EXPECTED_GIT_BLOB =
ea6ebe9d987bce108538a8bed14b6c45f02721ea
EXPECTED_SIZE_BYTES = 139139
```

## Main Word V01

`KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V01.docx`

```text
EXPECTED_SHA256 =
f579adca3b5c66394478ecc93f761d3271b090021c9df063ab41b581fb504b58
EXPECTED_SIZE_BYTES = 510287
EXPECTED_PAGE_COUNT = 40
EXPECTED_TABLES = 7
EXPECTED_DRAWINGS = 4
EXPECTED_COMMENTS = 0
EXPECTED_TRACKED_CHANGES = 0
```

Edit this exact DOCX directly. Do not reconstruct it from Markdown.

## Supplementary V01 — frozen carry-forward

`KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V01.md`

```text
EXPECTED_SHA256 =
c628bbb7c509aa5019c003bf686ab8932fb3b2e7be5af17f9b3ef84369259eb3
EXPECTED_GIT_BLOB =
e224162dec7f7c3f09da66ceab50ac7160a32066
```

`KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V01.docx`

```text
EXPECTED_SHA256 =
ab62250d63568c9e12492840295bff88f2991a8ca36810090459a5be1be9c5dd
EXPECTED_SIZE_BYTES = 121843
EXPECTED_PAGE_COUNT = 20
EXPECTED_TABLES = 7
EXPECTED_DRAWINGS = 1
EXPECTED_TRACKED_CHANGES = 0
```

The Supplementary scientific content is already PASS and must not be edited.

If any baseline identity fails, stop before editing.

# 2. Sole manuscript correction

Delete **exactly these eight internal drafting-control paragraphs** from both the main Markdown and the main DOCX:

1. `Organize results by function/RQ, not by internal experiment codes or execution chronology.`

2. `Report the controls that establish the validity of the benchmark and partitions used for analysis.`

3. `Primary RQ1 evidence: report authorized retrieval metrics and comparisons. Do not label this as overall system accuracy.`

4. `Primary RQ2 evidence: report coverage, association, traceability and preservation of candidate ranking as supported by the final evidence.`

5. `Primary RQ3 evidence: report the approved explanation/auditability evaluation and its limits.`

6. `Include only sensitivity analyses that survive final experimental reconciliation. Internal experiment IDs should be translated into scientific headings.`

7. `Optional compact synthesis if it improves readability. Use evidence, main finding and permitted interpretation; omit if redundant with the preceding subsections.`

8. `Interpret results rather than repeat them. Keep limitations close to the claims they qualify and consolidate them in the final subsection.`

These paragraphs are editorial drafting instructions, not scientific prose.

Do not rewrite, merge, reflow, paraphrase or otherwise edit the surrounding scientific paragraphs.

Whitespace/pagination may change naturally after deletion.

# 3. Absolute scientific freeze

Other than deletion of the eight exact paragraphs above, the main scientific content must remain byte-text equivalent at paragraph/table-cell level.

Preserve exactly:

- Title;
- Abstract;
- Keywords;
- Sections 1–7 scientific prose;
- all seven main tables and every cell;
- all four main figures and captions;
- all numerical results and denominators;
- all inferential statements and limitations;
- Data availability;
- Code and reproducibility resources;
- intentionally blank CRediT/Funding/competing-interest/Acknowledgements bodies;
- AI disclosure;
- all 25 bibliography entries and identities;
- Supplementary-material statement.

Forbidden:

- new experiment or analysis;
- new metric, CI, p-value or test;
- new literature/reference;
- scientific rewriting;
- reference normalization beyond what is already present;
- layout-driven deletion of scientific content.

# 4. Word constraints

The V02 main DOCX must be a direct edit of the exact V01 DOCX.

Required final state:

```text
MAIN_TABLES = 7
MAIN_DRAWINGS = 4
COMMENTS = 0
COMMENT_ANCHORS = 0
TRACKED_CHANGES = 0
RESIDUAL_DRAFTING_PARAGRAPHS = 0
```

Retain repeating table headers and row-no-split protection.

Retain the four exact embedded approved media:

```text
FIGURE_1_SHA256 =
d43b3695af795b14174ccaddfb29bff3e6f976f5234fef16fdda5eafc4a880f7
FIGURE_2_SHA256 =
35ecca4cd49a98e72bf73b323f0797c8e2fb70cfba1d8b04dec09d7a64cbb673
FIGURE_3_SHA256 =
d664e26c36e107cbf64c846ba2b6244f4e40df3048db99fa30ca46c4cba4def0
FIGURE_4_SHA256 =
9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11
```

# 5. Supplementary carry-forward

Do not edit Supplementary content.

Deliver V02-named copies that are byte-identical to V01:

- `KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V02.md`;
- `KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V02.docx`.

Their SHA-256 values must remain exactly:

```text
SUPPLEMENTARY_MD_SHA256 =
c628bbb7c509aa5019c003bf686ab8932fb3b2e7be5af17f9b3ef84369259eb3

SUPPLEMENTARY_DOCX_SHA256 =
ab62250d63568c9e12492840295bff88f2991a8ca36810090459a5be1be9c5dd
```

# 6. Standalone figures and ZIP integrity

Extract/reuse the exact four approved PNG binaries from the corrected main DOCX.

Deliver:

- `KBS_Figure1_Architecture.png`;
- `KBS_Figure2_Explanation_Quality.png`;
- `KBS_Figure3_EXP11A_Sensitivity.png`;
- `KBS_Figure4_HE2_Evidence.png`.

Do not depend on inline image transport for binary verification.

Create and deliver as a **real binary file**:

`KBS_FAST_F03_SUBMISSION_PACKAGE_V02.zip`

The ZIP must contain exactly:

```text
KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V02.md
KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V02.docx
KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V02.md
KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V02.docx
KBS_Figure1_Architecture.png
KBS_Figure2_Explanation_Quality.png
KBS_Figure3_EXP11A_Sensitivity.png
KBS_Figure4_HE2_Evidence.png
```

The Gestora will verify standalone figure bytes from the ZIP because direct image attachments can be transformed by the chat transport layer.

# 7. Machine checks

The final main files must contain none of the eight exact drafting instructions.

Also verify:

```text
SPANISH_MAIN_TEXT = ABSENT
INTERNAL_WORKING_BANNER = ABSENT
INTERNAL_STRUCTURE_TABLE = ABSENT
DRAFTING_INSTRUCTIONS = ABSENT
FAST_INTERNAL_LABELS_IN_MAIN = ABSENT

SECTION_CROSS_REFERENCES = PASS
TABLE_1_TO_7_REFERENCES = PASS
FIGURE_1_TO_4_REFERENCES = PASS
REFERENCE_BIJECTION = PASS_25_OF_25

MAIN_TABLES = 7
MAIN_FIGURES = 4
COMMENTS = 0
COMMENT_ANCHORS = 0
TRACKED_CHANGES = 0

SUPPLEMENTARY_TABLES = 7
SUPPLEMENTARY_FIGURES = 1
SUPPLEMENTARY_SCIENTIFIC_CONTENT_CHANGED = NO
```

# 8. Render and visual QA

Render the complete corrected main DOCX and the unchanged Supplementary DOCX.

Inspect every page.

The prior R01 drafting-note paragraphs must no longer be visible.

Report page counts and any layout changes caused solely by their deletion.

Blocking defects: clipping, overlap, broken table, split row, missing figure, avoidable caption separation, unreadable wrapping, unexpected blank page, missing glyph, or any residual drafting instruction.

# 9. Versioned outputs

Version in GitHub:

1. `article/sections/fast/FAST_F03_SUBMISSION_ASSEMBLY_V02.md`
2. `article/manifests/FAST_F03_SUBMISSION_PACKAGE_MANIFEST_V02.md`
3. `article/responses/22_FAST_F03_V02_DRAFTING_NOTE_CLEANUP_RESPONSE_V01.md`

The already versioned Supplementary source remains authoritative and need not be rewritten in Git because its V02 delivered copies are required to be byte-identical to V01.

Deliver real files:

4. `KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V02.md`
5. `KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V02.docx`
6. `KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V02.md`
7. `KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V02.docx`
8. the four exact standalone PNGs;
9. `KBS_FAST_F03_SUBMISSION_PACKAGE_V02.zip`.

Do not promote a canonical master.

# 10. Response minimum fields

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = FAST_FINALIZATION / FAST_F03_V02_CORRECTIVE

PROMPT_IDENTITY = PASS / BLOCKED
AUTHORIZATION_IDENTITY = PASS / BLOCKED
ALL_BASELINE_IDENTITIES = PASS / BLOCKED

DELETED_DRAFTING_PARAGRAPHS = 8
RESIDUAL_DRAFTING_PARAGRAPHS = 0
SCIENTIFIC_CONTENT_CHANGED = NO

MAIN_TABLES = 7
MAIN_FIGURES = 4
COMMENTS = 0
TRACKED_CHANGES = 0
REFERENCE_BIJECTION = PASS_25_OF_25

MAIN_MD_SHA256 = ...
MAIN_MD_EXPECTED_GIT_BLOB = ...
MAIN_DOCX_SHA256 = ...
MAIN_DOCX_SIZE_BYTES = ...
MAIN_PAGE_COUNT = ...

SUPPLEMENTARY_MD_SHA256 =
c628bbb7c509aa5019c003bf686ab8932fb3b2e7be5af17f9b3ef84369259eb3
SUPPLEMENTARY_DOCX_SHA256 =
ab62250d63568c9e12492840295bff88f2991a8ca36810090459a5be1be9c5dd

FIGURE_1_PNG_SHA256 = ...
FIGURE_2_PNG_SHA256 = ...
FIGURE_3_PNG_SHA256 = ...
FIGURE_4_PNG_SHA256 = ...

PACKAGE_ZIP_SHA256 = ...
PACKAGE_ZIP_ENTRY_COUNT = 8

NEW_SCIENTIFIC_CONTENT = NO
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO
EXPECTED_EXIT = FAST_F03_V02_COMPLETED_PENDING_GESTORA_AUDIT
```

# 11. Stop condition

Stop exactly at:

`FAST_F03_V02_COMPLETED_PENDING_GESTORA_AUDIT`

Do not perform canonical promotion.

Do not begin Experimental G8-F01.
