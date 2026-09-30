# 21 — FAST-F03 Submission Assembly V01

## Role

Act exclusively as **IA de Redacción científica** for GIC-NANDINA.

Execute only the final publication-facing submission assembly described here. Do not act as IA Gestora, IA Experimental, or Author.

No new science is authorized.

## Governing state

Read completely:

- `article/governance/D216_FAST_F02_V03_AUTHOR_APPROVAL_AND_V039_INTEGRATION.md`;
- `article/reviews/21_FAST_F03_SUBMISSION_READINESS_AUDIT_V01.md`;
- `article/governance/D208_FAST_F02_AUTHOR_FIELDS_INTENTIONALLY_BLANK.md`;
- current `article/ARTICLE_STATUS.md`;
- current `article/ARTICLE_WRITING_PLAN.md`;
- `article/STYLE_GUIDE.md`.

Execution requires an authorization decision that binds to this exact prompt Git blob. If authorization identity fails, stop at preflight.

# 1. Exact baselines

## Canonical Markdown

`article/manuscript/ARTICLE_MASTER_V039.md`

```text
EXPECTED_GIT_BLOB =
9a7427365a0bd8a5fc340e27eda5aa98a02a4a1f
EXPECTED_SHA256 =
4367b60f181a4d399ecba4dc205ccb6dcba0d7237effa762753ccb8bb9065074
EXPECTED_SIZE_BYTES = 298710
```

## Canonical cumulative Word

Attach/use the real file:

`ARTICLE_MASTER_CANDIDATE_FAST_F02_V03.docx`

```text
EXPECTED_SHA256 =
2a3a7b6b724728027756fdafd5572e63beab03eaa414bdc4a529bba1bfe989e3
EXPECTED_SIZE_BYTES = 578737
EXPECTED_PAGE_COUNT = 85
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Edit this exact DOCX directly. Do not reconstruct Word from Markdown.

## Approved Supplementary Markdown

`SUPPLEMENTARY_MATERIAL_FAST_F02_V03.md`

```text
EXPECTED_SHA256 =
9c08af66edcae7f39cbf06590105d2e0d0d2a184840c7595fe354078346f934d
EXPECTED_GIT_BLOB =
2eaacc07319d7cb926c5ebb26acf9f40f85f733b
```

## Approved Supplementary Word

`SUPPLEMENTARY_MATERIAL_FAST_F02_V03.docx`

```text
EXPECTED_SHA256 =
f2f4ced99305789c5d194470a6cd1280a825386f1ea06620ef0ff18f2f7616bd
EXPECTED_SIZE_BYTES = 122189
EXPECTED_PAGE_COUNT = 20
EXPECTED_TRACKED_CHANGES = 0
```

If any baseline identity fails, stop before editing.

# 2. Main manuscript — publication-facing extraction

Create a clean English-only submission manuscript from the approved V039.

Remove completely from the submission copy:

1. the `Knowledge-Based Systems target manuscript` working banner;
2. `KBS_ARTICLE_WORKING_STRUCTURE_V02`;
3. `Cumulative editable base for subsequent manuscript versions`;
4. the opening internal metadata table;
5. the editorial-control paragraph;
6. the key-structural-principle drafting note;
7. `Structure at a glance` and its internal table;
8. `PART I — English manuscript master` and its drafting-control note;
9. the drafting instruction below `2. Related work` beginning `Organize by technical function/problem family...`;
10. the drafting instruction below `3. Decision-support architecture` beginning `Describe the general architecture...`;
11. the drafting instruction below `4. Experimental design` beginning `Only here should...`;
12. the complete `PART II — Spanish semantic-control mirror`, from that heading through the end of the internal master.

Do **not** rewrite the remaining English science merely for style.

The final main Markdown must begin directly with the article title structure, not with internal governance metadata.

# 3. Frozen scientific body

Preserve semantically and numerically exactly:

- approved English Title;
- Abstract;
- six Keywords;
- Sections 1–7;
- Data availability;
- Code and reproducibility resources;
- seven main tables;
- four main figures and their approved captions;
- all inferential statements and limitations;
- approved generative-AI declaration;
- 25-reference bibliography identities;
- Supplementary-material statement.

Forbidden:

- new experiment;
- new analysis;
- new metric;
- new CI;
- new p-value;
- new inferential test;
- new hypothesis disposition;
- new literature;
- new reference;
- new scientific claim;
- recomputation;
- scientific paraphrase that changes epistemic force.

# 4. Author-administrative sections

Under D-208, these tasks are **closed and intentionally blank**:

- CRediT authorship contribution statement;
- Funding;
- Declaration of competing interest;
- Acknowledgements.

Keep the headings in the final main manuscript, with empty bodies.

Do not insert any personal data previously present only in governance.

Do not insert `TBD`, `PENDING`, `TO COMPLETE`, explanatory placeholders or comments.

Do not ask the Author for these data.

# 5. Main tables and figures

Final publication-facing inventory:

```text
MAIN_TABLES = 7
MAIN_FIGURES = 4
```

Only the approved English instances remain.

Use the exact four media objects already embedded in the approved V03 DOCX:

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

Extract/reuse the exact embedded PNG bytes for the standalone submission figures. Do not redraw, regenerate, resize, recompress or substitute them.

Deliver:

- `KBS_Figure1_Architecture.png`
- `KBS_Figure2_Explanation_Quality.png`
- `KBS_Figure3_EXP11A_Sensitivity.png`
- `KBS_Figure4_HE2_Evidence.png`

Each delivered SHA-256 must match the corresponding approved identity above.

# 6. Final Word cleanup

Edit the exact V03 DOCX directly.

Required:

- delete the same internal preamble/drafting material removed from Markdown;
- delete the entire Spanish Part II;
- remove all 48 internal comments and all comment anchors/references;
- retain zero tracked changes;
- retain exactly seven publication tables;
- retain exactly four publication figures;
- preserve approved English captions;
- preserve table header-repeat and row-no-split protections where relevant;
- prevent figure/caption separation;
- eliminate blank pages created only by removed internal material;
- retain stable, readable portrait layout unless an existing approved element already requires otherwise.

Do not reconstruct from Markdown.

# 7. Supplementary publication cleanup

Create publication-facing Supplementary from the exact V03 Supplementary baselines.

Required scientific inventory:

```text
TABLES_S1_TO_S7 = PRESENT
FIGURE_S1 = PRESENT
FIGURE_S2 = ABSENT
TABLE_COUNT = 7
DRAWING_COUNT = 1
```

Permitted editorial cleanup:

- title `Supplementary Material — FAST-F02 V03` → `Supplementary Material`;
- remove wording whose only function is to narrate internal FAST/G5/G6 governance transitions, provided the scientific qualification remains unchanged;
- normalize layout after that cleanup.

Do not change any table cell, scientific value, denominator, statistical qualification, figure scientific content or inferential status.

# 8. Cross-reference and integrity audit

Machine-check the final package for:

```text
SECTION_CROSS_REFERENCES = PASS
TABLE_1_TO_7_REFERENCES = PASS
FIGURE_1_TO_4_REFERENCES = PASS
SUPPLEMENTARY_TABLE_S1_TO_S7 = PASS
SUPPLEMENTARY_FIGURE_S1 = PASS

CITATION_REFERENCE_BIJECTION = PASS_25_OF_25
ORPHAN_REFERENCES = 0
UNRESOLVED_CITATIONS = 0

SPANISH_MAIN_TEXT = ABSENT
INTERNAL_WORKING_BANNER = ABSENT
INTERNAL_STRUCTURE_TABLE = ABSENT
DRAFTING_INSTRUCTIONS = ABSENT
FAST_INTERNAL_LABELS_IN_MAIN = ABSENT

COMMENTS = 0
COMMENT_ANCHORS = 0
TRACKED_CHANGES = 0
```

# 9. Render and visual QA

Render the complete final main DOCX and final Supplementary DOCX.

Inspect every page.

Report:

```text
MAIN_PAGE_COUNT = ...
MAIN_FULL_RENDER = PASS / BLOCKED
MAIN_VISUAL_QA = PASS / BLOCKED
MAIN_TABLE_COUNT = 7
MAIN_DRAWING_COUNT = 4

SUPPLEMENTARY_PAGE_COUNT = ...
SUPPLEMENTARY_FULL_RENDER = PASS / BLOCKED
SUPPLEMENTARY_VISUAL_QA = PASS / BLOCKED
SUPPLEMENTARY_TABLE_COUNT = 7
SUPPLEMENTARY_DRAWING_COUNT = 1
```

Blocking visual defects include clipping, overlap, missing figure, separated caption where avoidable, broken table, split row, unreadable wrapping, unexpected blank page, or missing glyph.

# 10. Output files

Version in GitHub:

1. `article/sections/fast/FAST_F03_SUBMISSION_ASSEMBLY_V01.md`
2. `article/manifests/FAST_F03_SUBMISSION_PACKAGE_MANIFEST_V01.md`
3. `article/supplementary/SUPPLEMENTARY_MATERIAL_FAST_F03_V01.md`
4. `article/responses/21_FAST_F03_SUBMISSION_ASSEMBLY_RESPONSE_V01.md`

Deliver as real files:

5. `KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V01.md`
6. `KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V01.docx`
7. `KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V01.md`
8. `KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V01.docx`
9. `KBS_Figure1_Architecture.png`
10. `KBS_Figure2_Explanation_Quality.png`
11. `KBS_Figure3_EXP11A_Sensitivity.png`
12. `KBS_Figure4_HE2_Evidence.png`
13. `KBS_FAST_F03_SUBMISSION_PACKAGE_V01.zip`

The ZIP must contain exactly the real deliverables required for Author review, without render-QA intermediates.

Do not promote a new canonical master.

# 11. Response minimum fields

Report:

```text
SOURCE_COMMIT = ...
SOURCE_BRANCH = article/main-manuscript
PHASE = FAST_FINALIZATION / FAST_F03

PROMPT_IDENTITY = PASS / BLOCKED
AUTHORIZATION_IDENTITY = PASS / BLOCKED
ALL_BASELINE_IDENTITIES = PASS / BLOCKED

INTERNAL_PREAMBLE_REMOVED = PASS / BLOCKED
SPANISH_MIRROR_REMOVED = PASS / BLOCKED
DRAFTING_INSTRUCTIONS_REMOVED = PASS / BLOCKED
COMMENTS_REMOVED = PASS / BLOCKED
TRACKED_CHANGES = 0

MAIN_TABLES = 7
MAIN_FIGURES = 4
SUPPLEMENTARY_TABLES = 7
SUPPLEMENTARY_FIGURES = 1

REFERENCE_BIJECTION = PASS_25_OF_25
SCIENTIFIC_CONTENT_CHANGED = NO
AUTHOR_ADMIN_FIELDS = INTENTIONALLY_BLANK / PASS

MAIN_MD_SHA256 = ...
MAIN_MD_EXPECTED_GIT_BLOB = ...
MAIN_DOCX_SHA256 = ...
MAIN_DOCX_SIZE_BYTES = ...
MAIN_PAGE_COUNT = ...

SUPPLEMENTARY_MD_SHA256 = ...
SUPPLEMENTARY_MD_EXPECTED_GIT_BLOB = ...
SUPPLEMENTARY_DOCX_SHA256 = ...
SUPPLEMENTARY_DOCX_SIZE_BYTES = ...
SUPPLEMENTARY_PAGE_COUNT = ...

FIGURE_1_PNG_SHA256 = ...
FIGURE_2_PNG_SHA256 = ...
FIGURE_3_PNG_SHA256 = ...
FIGURE_4_PNG_SHA256 = ...

PACKAGE_ZIP_SHA256 = ...

NEW_SCIENTIFIC_CONTENT = NO
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO

EXPECTED_EXIT = FAST_F03_COMPLETED_PENDING_GESTORA_AUDIT
```

# 12. Stop condition

Stop exactly at:

`FAST_F03_COMPLETED_PENDING_GESTORA_AUDIT`

Do not perform canonical promotion.

Do not begin Experimental G8-F01.
