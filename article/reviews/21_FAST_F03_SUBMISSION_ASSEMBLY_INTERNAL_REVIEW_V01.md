# Internal Review — FAST-F03 Submission Assembly V01

## Result

```text
REVIEW_RESULT = FAIL_CORRECTION_REQUIRED
PHASE = FAST_FINALIZATION / FAST_F03

SOURCE_RESPONSE =
article/responses/21_FAST_F03_SUBMISSION_ASSEMBLY_RESPONSE_V01.md@7b17c02a6ae9a92a70390b94904dc70f85a4d695
SOURCE_RESPONSE_GIT_BLOB =
4b1c15a23ea4f0458e914dec7e53075a3bb40e53

AUTHORIZATION = D-217
PROMPT =
article/prompts/21_FAST_F03_SUBMISSION_ASSEMBLY_V01.md
PROMPT_GIT_BLOB =
ee9d439eab270e8991e8c1ef14a1d8e2ca0bf661

MAIN_MD_SHA256 =
ffe6cbe06b0e0f7f17c2ba8e6e839205588a88ff87b8706f55cf647d16c9363a
MAIN_MD_GIT_BLOB =
ea6ebe9d987bce108538a8bed14b6c45f02721ea

MAIN_DOCX_SHA256 =
f579adca3b5c66394478ecc93f761d3271b090021c9df063ab41b581fb504b58
MAIN_DOCX_SIZE_BYTES = 510287
MAIN_DOCX_PAGE_COUNT = 40

SUPPLEMENTARY_MD_SHA256 =
c628bbb7c509aa5019c003bf686ab8932fb3b2e7be5af17f9b3ef84369259eb3
SUPPLEMENTARY_MD_GIT_BLOB =
e224162dec7f7c3f09da66ceab50ac7160a32066

SUPPLEMENTARY_DOCX_SHA256 =
ab62250d63568c9e12492840295bff88f2991a8ca36810090459a5be1be9c5dd
SUPPLEMENTARY_DOCX_SIZE_BYTES = 121843
SUPPLEMENTARY_DOCX_PAGE_COUNT = 20

SCIENTIFIC_CONTENT = PASS
ENGLISH_ONLY_EXTRACTION = PASS
TABLE_FIGURE_INVENTORY = PASS
COMMENTS_REMOVED = PASS
TRACKED_CHANGES = PASS
SUPPLEMENTARY = PASS
REFERENCE_CORPUS = PRESERVED

DRAFTING_INSTRUCTIONS_ABSENT = FAIL
PUBLICATION_FACING_CLEANLINESS = FAIL
PACKAGE_ZIP_BINARY_AUDIT = NOT_VERIFIABLE_FROM_HANDOFF
STANDALONE_FIGURE_BINARY_HANDOFF = PARTIAL_TRANSPORT_MISMATCH

NEW_SCIENTIFIC_CONTENT = NO
EXPERIMENTAL_REAUDIT_REQUIRED = NO
AUTHOR_APPROVAL_GATE = NOT_OPEN
```

## 1. Identity and scientific-freeze audit

PASS.

The four real manuscript/Supplementary files supplied to the Gestora match the exact SHA-256 identities declared in Response 21.

The main Markdown computes to Git blob `ea6ebe9d987bce108538a8bed14b6c45f02721ea`, and the Supplementary Markdown computes to Git blob `e224162dec7f7c3f09da66ceab50ac7160a32066`.

A block-level comparison of the final main DOCX against the approved FAST-F02 V03 DOCX confirms that the retained scientific English body is text-identical. The V01 final DOCX is exactly the English scientific sequence from the approved baseline after removal of the preamble, PART I control wrapper, the three Prompt-21-enumerated drafting paragraphs, Spanish Part II, comments and internal footer.

The final Markdown is likewise identical to the approved English master after the authorized removals, whitespace normalization and submission-facing figure-path renaming.

Therefore no scientific claim, value, table cell, reference identity or inference was changed by FAST-F03 V01.

## 2. Blocking defect R01 — residual drafting instructions

FAIL.

Response 21 declares:

`DRAFTING_INSTRUCTIONS = ABSENT`

but the publication-facing main Markdown and DOCX still contain **eight internal drafting-control paragraphs**:

1. `Organize results by function/RQ, not by internal experiment codes or execution chronology.`
2. `Report the controls that establish the validity of the benchmark and partitions used for analysis.`
3. `Primary RQ1 evidence: report authorized retrieval metrics and comparisons. Do not label this as overall system accuracy.`
4. `Primary RQ2 evidence: report coverage, association, traceability and preservation of candidate ranking as supported by the final evidence.`
5. `Primary RQ3 evidence: report the approved explanation/auditability evaluation and its limits.`
6. `Include only sensitivity analyses that survive final experimental reconciliation. Internal experiment IDs should be translated into scientific headings.`
7. `Optional compact synthesis if it improves readability. Use evidence, main finding and permitted interpretation; omit if redundant with the preceding subsections.`
8. `Interpret results rather than repeat them. Keep limitations close to the claims they qualify and consolidate them in the final subsection.`

These are visibly present in the rendered publication-facing Word file, including within Results and Discussion.

They are not scientific prose and are safe to delete byte-boundedly without experimental or scientific re-audit.

Root cause: Prompt 21 explicitly enumerated the older drafting notes under Sections 2, 3 and 4, but its global invariant `DRAFTING_INSTRUCTIONS = ABSENT` was not operationalized against the additional internal instructions already present in Results/Discussion.

## 3. Main DOCX structural audit

Apart from R01, PASS.

```text
ZIP_OOXML_INTEGRITY = PASS
TABLES = 7
DRAWINGS = 4
UNIQUE_MEDIA_ASSETS = 4
COMMENTS_XML = ABSENT
COMMENT_RANGE_START = 0
COMMENT_RANGE_END = 0
COMMENT_REFERENCE = 0
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
```

All seven main tables retain repeating header rows and row-no-split protection.

The four embedded media objects are the exact approved binaries:

```text
FIGURE_1_EMBEDDED_SHA256 =
d43b3695af795b14174ccaddfb29bff3e6f976f5234fef16fdda5eafc4a880f7
FIGURE_2_EMBEDDED_SHA256 =
35ecca4cd49a98e72bf73b323f0797c8e2fb70cfba1d8b04dec09d7a64cbb673
FIGURE_3_EMBEDDED_SHA256 =
d664e26c36e107cbf64c846ba2b6244f4e40df3048db99fa30ca46c4cba4def0
FIGURE_4_EMBEDDED_SHA256 =
9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11
```

## 4. Supplementary audit

PASS.

The Supplementary Markdown differs from the approved FAST-F02 V03 source only by:

- changing the title to `Supplementary Material`;
- removing the internal governance-transition reading note.

All seven Word table XML objects are byte-identical to the approved V03 Supplementary baseline.

```text
SUPPLEMENTARY_TABLES = 7
SUPPLEMENTARY_DRAWINGS = 1
SUPPLEMENTARY_FIGURE_S2 = ABSENT
TRACKED_CHANGES = 0
```

No Supplementary scientific correction is required.

## 5. Visual QA

The Gestora independently rendered the real files supplied in the handoff:

```text
MAIN_FULL_RENDER = PASS / 40 PAGES
SUPPLEMENTARY_FULL_RENDER = PASS / 20 PAGES
```

All pages were inspected.

No clipping, overlap, missing scientific figure, broken table, split-row defect or missing glyph was identified.

However, publication-facing visual QA is **FAIL** because the eight drafting-control paragraphs remain visibly printed in the main manuscript. This is a content-cleanliness blocker, not a layout defect.

## 6. Standalone figure transport audit

The directly supplied standalone Figure 1 and Figure 3 files match their governed hashes exactly.

The directly supplied Figure 2 and Figure 4 image attachments do not preserve the governed binary identities:

```text
DIRECT_FIGURE_2_SHA256 =
081728ba44eb4c0787c8cfe4c6ee5bd4a750861b025cd0c88a680e2ee292dd9c
EXPECTED_FIGURE_2_SHA256 =
35ecca4cd49a98e72bf73b323f0797c8e2fb70cfba1d8b04dec09d7a64cbb673

DIRECT_FIGURE_4_SHA256 =
73b9df5b6a6c7f3240385c2f1c7a93692925b5be9f92bf87f691b903a38db66e
EXPECTED_FIGURE_4_SHA256 =
9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11
```

The correct Figure 2 and Figure 4 binaries are nevertheless embedded byte-exact in the audited main DOCX. This is consistent with image-attachment transport transformation and does not indicate a scientific figure change.

For V02, binary verification of standalone figures must be performed from the actual ZIP package, not from potentially transcoded inline image attachments.

## 7. ZIP audit

The handoff message references `KBS_FAST_F03_SUBMISSION_PACKAGE_V01.zip`, but that ZIP was not available among the real files supplied to the Gestora in this handoff.

Therefore its reported SHA-256 and entry identities cannot be independently verified.

V02 must provide the ZIP as a real binary file. The Gestora will audit the standalone figure bytes from the ZIP.

## 8. Disposition

```text
FAST_F03_V01_GESTORA_REVIEW = FAIL_CORRECTION_REQUIRED
SCIENTIFIC_CONTENT = PASS / FROZEN
SUPPLEMENTARY = PASS / NO_CHANGE_REQUIRED
CORRECTIVE_SCOPE = DELETE_8_RESIDUAL_DRAFTING_PARAGRAPHS + REPACKAGE
NEW_SCIENCE = NO
EXPERIMENTAL_REAUDIT_REQUIRED = NO
AUTHOR_APPROVAL_GATE = NOT_OPEN
```
