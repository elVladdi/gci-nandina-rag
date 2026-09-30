# Response — FAST-F03 Submission Assembly V01 — COMPLETED PENDING GESTORA AUDIT

## Español

```text
SOURCE_COMMIT = 4a5d29a7a9054076de5b1a6e670fa4b33322f823
SOURCE_BRANCH = article/main-manuscript
PHASE = FAST_FINALIZATION / FAST_F03

PROMPT_IDENTITY = PASS
AUTHORIZATION_IDENTITY = PASS
ALL_BASELINE_IDENTITIES = PASS

INTERNAL_PREAMBLE_REMOVED = PASS
SPANISH_MIRROR_REMOVED = PASS
DRAFTING_INSTRUCTIONS_REMOVED = PASS
INTERNAL_WORKING_FOOTER_REMOVED = PASS
COMMENTS_REMOVED = PASS
TRACKED_CHANGES = 0

MAIN_TABLES = 7
MAIN_FIGURES = 4
SUPPLEMENTARY_TABLES = 7
SUPPLEMENTARY_FIGURES = 1

REFERENCE_BIJECTION = PASS_25_OF_25
SCIENTIFIC_CONTENT_CHANGED = NO
AUTHOR_ADMIN_FIELDS = INTENTIONALLY_BLANK / PASS

NEW_SCIENTIFIC_CONTENT = NO
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO

EXPECTED_EXIT = FAST_F03_COMPLETED_PENDING_GESTORA_AUDIT
```

### Preflight

```text
PROMPT =
article/prompts/21_FAST_F03_SUBMISSION_ASSEMBLY_V01.md
OBSERVED_PROMPT_GIT_BLOB =
ee9d439eab270e8991e8c1ef14a1d8e2ca0bf661
EXPECTED_PROMPT_GIT_BLOB =
ee9d439eab270e8991e8c1ef14a1d8e2ca0bf661

AUTHORIZATION = D-217
D217_GIT_BLOB =
132b2acdbbe1b2c17fa479100b464c7a25f50b7b
AUTHORIZATION_IDENTITY = PASS

CANONICAL_MD = article/manuscript/ARTICLE_MASTER_V039.md
CANONICAL_MD_GIT_BLOB =
9a7427365a0bd8a5fc340e27eda5aa98a02a4a1f
CANONICAL_MD_SHA256 =
4367b60f181a4d399ecba4dc205ccb6dcba0d7237effa762753ccb8bb9065074

INPUT_MAIN_DOCX_SHA256 =
2a3a7b6b724728027756fdafd5572e63beab03eaa414bdc4a529bba1bfe989e3
INPUT_MAIN_DOCX_SIZE_BYTES = 578737
INPUT_MAIN_DOCX_PAGE_COUNT = 85
INPUT_MAIN_DOCX_COMMENTS = 48
INPUT_MAIN_DOCX_TRACKED_CHANGES = 0

INPUT_SUPPLEMENTARY_MD_SHA256 =
9c08af66edcae7f39cbf06590105d2e0d0d2a184840c7595fe354078346f934d
INPUT_SUPPLEMENTARY_MD_GIT_BLOB =
2eaacc07319d7cb926c5ebb26acf9f40f85f733b

INPUT_SUPPLEMENTARY_DOCX_SHA256 =
f2f4ced99305789c5d194470a6cd1280a825386f1ea06620ef0ff18f2f7616bd
INPUT_SUPPLEMENTARY_DOCX_SIZE_BYTES = 122189
INPUT_SUPPLEMENTARY_DOCX_PAGE_COUNT = 20

ALL_BASELINE_IDENTITIES = PASS
```

### Main manuscript extraction

The publication-facing copy was extracted mechanically from the approved English Part I. No scientific paragraph was stylistically rewritten.

Removed:

- internal working banner and working-structure identifier;
- internal metadata/structure tables and editorial-control material;
- PART I wrapper and its drafting-control note;
- the three identified drafting instructions under Sections 2, 3 and 4;
- complete Spanish semantic-control Part II;
- internal working-base footer;
- all 48 Word comments and all comment range/reference anchors.

Preserved:

- approved English Title, Abstract and six Keywords;
- Sections 1–7;
- seven tables and four figures;
- approved figure captions;
- Data availability;
- Code and reproducibility resources;
- intentionally blank CRediT/Funding/competing-interest/Acknowledgements bodies;
- approved generative-AI declaration;
- 25-reference bibliography;
- Supplementary-material statement.

```text
SECTION_CROSS_REFERENCES = PASS
TABLE_1_TO_7_REFERENCES = PASS
FIGURE_1_TO_4_REFERENCES = PASS
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

### Main output identities

```text
MAIN_MD =
KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V01.md
MAIN_MD_SHA256 =
ffe6cbe06b0e0f7f17c2ba8e6e839205588a88ff87b8706f55cf647d16c9363a
MAIN_MD_EXPECTED_GIT_BLOB =
ea6ebe9d987bce108538a8bed14b6c45f02721ea
MAIN_MD_SIZE_BYTES = 139139

MAIN_DOCX =
KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V01.docx
MAIN_DOCX_SHA256 =
f579adca3b5c66394478ecc93f761d3271b090021c9df063ab41b581fb504b58
MAIN_DOCX_SIZE_BYTES = 510287
MAIN_PAGE_COUNT = 40

MAIN_DOCX_TABLE_COUNT = 7
MAIN_DOCX_DRAWING_COUNT = 4
MAIN_DOCX_UNIQUE_MEDIA_ASSETS = 4
ZIP_OOXML_INTEGRITY = PASS
```

The main Word was edited directly from the exact approved V03 DOCX and was not reconstructed from Markdown.

### Approved standalone figures

The four standalone PNGs were extracted byte-for-byte from the approved V03 Word package; no redraw, resize, recompression or substitution was performed.

```text
FIGURE_1_PNG_SHA256 =
d43b3695af795b14174ccaddfb29bff3e6f976f5234fef16fdda5eafc4a880f7

FIGURE_2_PNG_SHA256 =
35ecca4cd49a98e72bf73b323f0797c8e2fb70cfba1d8b04dec09d7a64cbb673

FIGURE_3_PNG_SHA256 =
d664e26c36e107cbf64c846ba2b6244f4e40df3048db99fa30ca46c4cba4def0

FIGURE_4_PNG_SHA256 =
9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11
```

### Supplementary publication cleanup

The Supplementary was derived from the exact approved V03 baselines.

Editorial-only changes:

- title changed from `Supplementary Material — FAST-F02 V03` to `Supplementary Material`;
- governance-transition reading note removed.

Scientific tables and figure content were not modified.

```text
SUPPLEMENTARY_TABLE_S1_TO_S7 = PASS
SUPPLEMENTARY_FIGURE_S1 = PASS
SUPPLEMENTARY_FIGURE_S2 = ABSENT
SUPPLEMENTARY_TABLE_XML_IDENTITY_TO_V03_BASELINE = PASS

SUPPLEMENTARY_MD =
KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V01.md
SUPPLEMENTARY_MD_SHA256 =
c628bbb7c509aa5019c003bf686ab8932fb3b2e7be5af17f9b3ef84369259eb3
SUPPLEMENTARY_MD_EXPECTED_GIT_BLOB =
e224162dec7f7c3f09da66ceab50ac7160a32066

SUPPLEMENTARY_DOCX =
KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V01.docx
SUPPLEMENTARY_DOCX_SHA256 =
ab62250d63568c9e12492840295bff88f2991a8ca36810090459a5be1be9c5dd
SUPPLEMENTARY_DOCX_SIZE_BYTES = 121843
SUPPLEMENTARY_PAGE_COUNT = 20

SUPPLEMENTARY_DOCX_TABLE_COUNT = 7
SUPPLEMENTARY_DOCX_DRAWING_COUNT = 1
SUPPLEMENTARY_TRACKED_CHANGES = 0
```

### Render and visual QA

```text
MAIN_PAGE_COUNT = 40
MAIN_FULL_RENDER = PASS
MAIN_VISUAL_QA = PASS / ALL 40 PAGES REVIEWED
MAIN_TABLE_COUNT = 7
MAIN_DRAWING_COUNT = 4

SUPPLEMENTARY_PAGE_COUNT = 20
SUPPLEMENTARY_FULL_RENDER = PASS
SUPPLEMENTARY_VISUAL_QA = PASS / ALL 20 PAGES REVIEWED
SUPPLEMENTARY_TABLE_COUNT = 7
SUPPLEMENTARY_DRAWING_COUNT = 1

VISUAL_QA_BLOCKING_DEFECTS = NONE
```

All final pages were visually inspected. No blocking clipping, overlap, missing figure, avoidable figure/caption separation, broken table, split row, unreadable wrapping, unexpected blank page, or missing glyph was observed.

### Versioned artifacts

```text
ASSEMBLY_SECTION =
article/sections/fast/FAST_F03_SUBMISSION_ASSEMBLY_V01.md
ASSEMBLY_SECTION_GIT_BLOB =
32fbb3320f31e7db8ff060d9851495af7fba758b

PACKAGE_MANIFEST =
article/manifests/FAST_F03_SUBMISSION_PACKAGE_MANIFEST_V01.md
PACKAGE_MANIFEST_GIT_BLOB =
0bb509e958c28f3bb5739a89c458f9b89e6d3707

SUPPLEMENTARY_VERSIONED =
article/supplementary/SUPPLEMENTARY_MATERIAL_FAST_F03_V01.md
SUPPLEMENTARY_VERSIONED_GIT_BLOB =
e224162dec7f7c3f09da66ceab50ac7160a32066
```

### ZIP package

```text
PACKAGE_ZIP =
KBS_FAST_F03_SUBMISSION_PACKAGE_V01.zip
PACKAGE_ZIP_SHA256 =
31a5fab3eb5b6ce2137bdb206f2cb751eed2ec0ee78f45886eca0fd6381d42c9
PACKAGE_ZIP_SIZE_BYTES = 1133440
PACKAGE_ZIP_ENTRY_COUNT = 8
```

ZIP contents exactly:

```text
KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V01.md
KBS_SUBMISSION_MANUSCRIPT_FAST_F03_V01.docx
KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V01.md
KBS_SUPPLEMENTARY_MATERIAL_FAST_F03_V01.docx
KBS_Figure1_Architecture.png
KBS_Figure2_Explanation_Quality.png
KBS_Figure3_EXP11A_Sensitivity.png
KBS_Figure4_HE2_Evidence.png
```

No render-QA intermediates are included.

### Disposition

```text
SCIENTIFIC_CONTENT_CHANGED = NO
NEW_SCIENTIFIC_CONTENT = NO
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO

EXPECTED_EXIT = FAST_F03_COMPLETED_PENDING_GESTORA_AUDIT
NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
CANONICAL_PROMOTION = NOT_AUTHORIZED
EXPERIMENTAL_G8_F01 = NOT_AUTHORIZED
```

No canonical promotion was performed and Experimental G8-F01 was not started.

---

## English

FAST-F03 V01 was executed exclusively under D-217 from the Author-approved V039 and the exact approved FAST-F02 V03 Word/Supplementary baselines.

The final main manuscript is English-only and publication-facing. Internal working metadata, structure material, drafting instructions, the Spanish semantic-control mirror, the internal footer, all 48 comments and all comment anchors were removed. The approved scientific body, seven tables, four figures, End Matter, generative-AI declaration and 25-reference corpus were preserved.

The final main DOCX contains seven tables, four drawings, zero comments, zero comment anchors and zero tracked changes, and renders to 40 pages. The publication-facing Supplementary contains seven tables, Figure S1 only, zero tracked changes, and renders to 20 pages. All 60 final pages were visually inspected without blocking defects.

The four standalone submission figures are byte-exact extractions of the approved embedded V03 media and match the governed SHA-256 identities.

The ZIP contains exactly the eight requested Author-review deliverables and no QA intermediates.

Execution stops at `FAST_F03_COMPLETED_PENDING_GESTORA_AUDIT`. No canonical promotion was performed and Experimental G8-F01 was not started.
