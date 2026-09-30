# Internal Review — FAST-F02 End Matter, References & Supplementary V01

## Result

```text
REVIEW_RESULT = PASS_WITH_NONBLOCKING_TRACEABILITY_DEVIATION
PHASE = FAST_FINALIZATION / FAST_F02

SOURCE_RESPONSE =
article/responses/18_FAST_F02_END_MATTER_REFERENCES_SUPPLEMENTARY_RESPONSE_V01.md@5be478363425f1a5a478fac365d2916b920e337f
SOURCE_RESPONSE_GIT_BLOB =
ee764b0b829b0bd6edb392af1d9711d0fc32c6d8

AUTHORIZATION = D-209
PROMPT_GIT_BLOB =
5a38905b03e0d44d1b3125f866996fc03b92aa79

CANDIDATE_MD_SHA256 =
c6909699b9b7272d12cbe57f02d5897b78c8a489c9105bdf69e23e4462e90dd4
CANDIDATE_MD_GIT_BLOB =
4c891641a86d0622cdc9fb7b2afee6f4691ee320
CANDIDATE_MD_SIZE_BYTES = 305240

CANDIDATE_DOCX_SHA256 =
bd584ce9817ce8d251cbe43a6e737612039a5ba82c932f1637839d66466e9e31
CANDIDATE_DOCX_SIZE_BYTES = 356835
CANDIDATE_DOCX_PAGE_COUNT = 81

SUPPLEMENTARY_MD_SHA256 =
fd2ff32090f2262787a0f661bf67300bca158733b24edae0a37ac90dffd0a89f
SUPPLEMENTARY_MD_GIT_BLOB =
d10207e99ca76c1b501f57c9cf2b620e54c03a3f
SUPPLEMENTARY_MD_SIZE_BYTES = 43533

SUPPLEMENTARY_DOCX_SHA256 =
ad6b7f5cbfa695ab61eb4f9b5469f061eb804074c5bfb8c735bdef81d700cc9e
SUPPLEMENTARY_DOCX_SIZE_BYTES = 222424
SUPPLEMENTARY_DOCX_PAGE_COUNT = 21

CONTENT_AUDIT = PASS
REFERENCE_INTEGRITY_AUDIT = PASS
SUPPLEMENTARY_SOURCE_IDENTITY = PASS
OOXML_STRUCTURAL_AUDIT = PASS
VISUAL_QA = PASS
EXPERIMENTAL_REAUDIT_REQUIRED = NO

FAST_F02 = PASS_PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = READY_TO_OPEN
FAST_F03 = NOT_AUTHORIZED
```

## 1. Input/output identity

PASS.

IA Gestora independently verified the real files delivered by Writing AI:

```text
ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.md
SIZE = 305240
SHA256 =
c6909699b9b7272d12cbe57f02d5897b78c8a489c9105bdf69e23e4462e90dd4
GIT_BLOB =
4c891641a86d0622cdc9fb7b2afee6f4691ee320

ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.docx
SIZE = 356835
SHA256 =
bd584ce9817ce8d251cbe43a6e737612039a5ba82c932f1637839d66466e9e31

SUPPLEMENTARY_MATERIAL_FAST_F02_V01.md
SIZE = 43533
SHA256 =
fd2ff32090f2262787a0f661bf67300bca158733b24edae0a37ac90dffd0a89f
GIT_BLOB =
d10207e99ca76c1b501f57c9cf2b620e54c03a3f

SUPPLEMENTARY_MATERIAL_FAST_F02_V01.docx
SIZE = 222424
SHA256 =
ad6b7f5cbfa695ab61eb4f9b5469f061eb804074c5bfb8c735bdef81d700cc9e
```

The cumulative Markdown Git blob computed independently matches the response.

## 2. Manuscript scope audit

PASS.

A top-level section differential against ARTICLE_MASTER_V038 shows no change outside the FAST-F02 authorized End Matter blocks.

Changed only:

- Data availability EN/ES;
- Code and reproducibility resources EN/ES;
- CRediT body -> empty EN/ES;
- Funding body -> empty EN/ES;
- competing-interest body -> empty EN/ES;
- Acknowledgements body -> empty EN/ES;
- References EN/ES;
- Supplementary material statement EN/ES.

All other top-level manuscript sections are byte-equivalent.

The generative-AI disclosure sections are byte-identical at Markdown level in EN and ES.

No previously supplied author facts were inserted.

## 3. Data availability and reproducibility

PASS.

The finalized wording preserves the D-206/D-207 boundary:

- administrative/reference inputs are not represented as publicly redistributable;
- the public reproducibility repository is named and pinned to audited commit 254831cd955103faa2517065a7eed7fb340bbccc;
- exact reference-study reproduction may require restricted/non-redistributed inputs;
- the public snapshot is not claimed to be a complete one-command fresh-clone end-to-end reproduction;
- repository availability is not treated as deployment readiness.

## 4. Author-administrative fields

PASS.

The headings remain and their bodies are empty:

- CRediT;
- Funding;
- Declaration of competing interest;
- Acknowledgements;

and the Spanish mirrors.

No name, affiliation, ORCID, email, funding fact, conflict declaration, acknowledgement, or corresponding-author designation was inserted.

This satisfies D-208.

## 5. Reference integrity

PASS.

IA Gestora independently checked the candidate manuscript and reference manifest:

```text
UNIQUE_ENGLISH_BODY_CITED_WORKS = 25
REFERENCE_ENTRIES_EN = 25
REFERENCE_ENTRIES_ES = 25
UNRESOLVED_CITATIONS = 0
ORPHAN_REFERENCES = 0
DUPLICATE_REFERENCE_IDENTITIES = 0
EN_ES_REFERENCE_LIST_TEXT_IDENTITY = PASS
LEE_2023_PREPRINT_IDENTITY = PRESERVED
```

The candidate uses exactly the governed 25-work corpus.

Publisher-specific reference-style normalization remains a FAST-F03 mechanical concern and does not alter source identity.

## 6. Supplementary source identity

PASS.

IA Gestora independently compared each Supplementary Markdown table against its canonical CSV source.

```text
S1 = 15/15 rows exact
S2 = 15/15 rows exact
S3 = 3/3 rows exact
S4 = 37/37 rows exact
S5 = 22/22 rows exact
S6 = 62/62 rows exact
S7 = 3/3 rows exact
```

All cells match the canonical CSV strings exactly.

The Supplementary DOCX contains exactly seven tables with the same data-row counts:

```text
S1 = 15
S2 = 15
S3 = 3
S4 = 37
S5 = 22
S6 = 62
S7 = 3
```

It also contains exactly two drawings corresponding to Figures S1-S2.

The scientific restrictions remain explicit: descriptive/noncausal roles, HE5 inconclusive, no seed-superpopulation inference, diagnostic ceiling not production performance, and no new statistic/inference.

## 7. Main DOCX / OOXML audit

PASS.

Independent inspection against the exact V038 DOCX baseline:

```text
ZIP_OOXML_INTEGRITY = PASS
OOXML_PART_COUNT = 16
OOXML_PART_NAMES_IDENTICAL_TO_V038 = PASS

CHANGED_PARTS_VS_V038 =
word/document.xml ONLY

COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48

COMMENTS_XML_SHA256 =
57bee5d04cc9ed51628a4e10baef0730c0a07b58b9d8c3b436c64657f32821ea

COMMENTS_XML_BYTE_IDENTICAL_TO_V038 = PASS
COMMENT_RANGE_START_ID_SEQUENCE_IDENTICAL = PASS

TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
TABLES = 8
DRAWINGS = 4
```

The inherited media and relationships are unchanged.

## 8. Supplementary DOCX structure

PASS.

```text
ZIP_OOXML_INTEGRITY = PASS
OOXML_PART_COUNT = 19
TABLES = 7
DRAWINGS = 2
TRACKED_CHANGES = 0

EMBEDDED_FIGURE_S1_SHA256 =
3b4e4411674347ec09250278d53738b75ae37cc30a9b2b29e4449266b37597af
DIMENSIONS = 1800x1012

EMBEDDED_FIGURE_S2_SHA256 =
d664e26c36e107cbf64c846ba2b6244f4e40df3048db99fa30ca46c4cba4def0
DIMENSIONS = 1800x1200
```

These are presentation renders; byte identity to the canonical PNG assets was not required by Prompt 18. Scientific identity is supported by the frozen table values, governed caption contracts and visual content.

## 9. Independent render / visual QA

PASS.

IA Gestora independently rendered:

```text
MAIN DOCX = 81 pages
SUPPLEMENTARY DOCX = 21 pages
TOTAL = 102 pages
```

The full documents were reviewed for clipping, missing glyphs, broken images, overlap and broken page flow.

Detailed checks included the End Matter and reference pages in both languages and all Supplementary tables/figures.

No blocking visual defect was found.

## 10. Nonblocking traceability deviation

Prompt 18 requested versioning of:

`article/sections/fast/FAST_F02_End_Matter_References_V01.md`

This file is absent at response commit 5be478363425f1a5a478fac365d2916b920e337f.

Classification:

```text
FASTF02-T01 =
NONBLOCKING_GOVERNANCE_TRACEABILITY_DEVIATION

SCIENTIFIC_CONTENT_MISSING = NO
CUMULATIVE_MANUSCRIPT_MISSING = NO
SUPPLEMENTARY_PACKAGE_MISSING = NO
REFERENCE_MANIFEST_MISSING = NO
DOCX_DELIVERABLE_MISSING = NO
REEXECUTION_REQUIRED = NO
```

Managing AI waives this redundant derived-section artifact for FAST-F02 closure because the exact cumulative candidate, response, reference-bijection manifest, Supplementary source package and four real handoff files are present and independently auditable.

No Writing-AI correction cycle is opened for this file alone.

## 11. Disposition

```text
FAST_F02_EXECUTION = PASS_WITH_NONBLOCKING_TRACEABILITY_DEVIATION
FAST_F02_CONTENT = PASS
FAST_F02_REFERENCE_INTEGRITY = PASS
FAST_F02_SUPPLEMENTARY = PASS
FAST_F02_DOCX_QA = PASS

READY_FOR_AUTHOR_APPROVAL = YES
READY_FOR_CANONICAL_PROMOTION = NO

NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_FAST_F02_V01

FAST_F03 = NOT_AUTHORIZED
EXPERIMENTAL_G8_F01 = NOT_AUTHORIZED_BY_THIS_REVIEW
```
