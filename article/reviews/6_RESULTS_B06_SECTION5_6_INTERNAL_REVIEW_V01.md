# Internal Review — Results B06 / Section 5.6 — V01

## Verdict

```text
VERDICT = PASS
BLOCK = RESULTS_B06_SECTION_5_6
VERSION = V01
SCIENTIFIC_CONTENT = PASS
NUMERICAL_FIDELITY = PASS
CLAIM_BOUNDARIES = PASS
SCOPE_ONLY_DIFF = PASS
EN_ES_EQUIVALENCE = PASS
MD_DOCX_EQUIVALENCE = PASS
OOXML_INTEGRITY = PASS
FULL_RENDER = PASS
D035 = PASS
AUTHOR_APPROVAL_GATE = MAY_OPEN
```

## Audited objects

```text
RESPONSE = article/responses/6_RESULTS_B06_SECTION5_6_RESPONSE_V01.md@e7e9ab0efb137243471bd0dc1feb4363b9b1c7d7
SECTION = article/sections/results/Results_B06_V01.md@cbb5cafdf3c9725c0d0caefa565ba694ead93349
SECTION_GIT_BLOB = 092e8f9af2cd96ac7d6ad41f193bd7486ec40938

CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.md
CANDIDATE_MD_SHA256 = 56ab09837fedeb8206908f6966cb606d61b42ad443296eb82b4ea32c1f747795
CANDIDATE_MD_GIT_BLOB_EXPECTED = 088eecd537997a3438517f7d206f6d890b0aa064

CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B06_V01.docx
CANDIDATE_DOCX_SHA256 = 46ec068687465215ecc32632b29b265f4376e3d481a3a0e8b06cf0f90cfe8c79
CANDIDATE_DOCX_PAGE_COUNT = 58
COMMENTS = 40
TRACKED_CHANGES = 0
```

## 1. Baseline and differential integrity

The local B05 baseline matched its frozen identity:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.md
SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
GIT_BLOB = e76b5b1789de1f82c9623dd6543c38ae639715b0

ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
```

The B06 Markdown candidate differs from B05 only by replacing the English and Spanish Section 5.6 placeholders. Replacing those two B06 sections with the frozen B05 placeholders reconstructs the B05 Markdown byte-for-byte and reproduces SHA-256 `a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06`.

Therefore:

```text
SECTION_5_6_ONLY_DIFF = PASS
SECTIONS_1_TO_5_5_PRESERVED = PASS
SECTION_5_7_PRESERVED = PASS
DISCUSSION_PRESERVED = PASS
CONCLUSION_PRESERVED = PASS
END_MATTER_PRESERVED = PASS
```

## 2. Scientific and numerical audit

The manuscript values were checked against the frozen `main@db0d0ad0d8435921a7838db6720eaea86a263763` Group-3 inferential artifacts and D-113/D-114.

HE2_A correctly reports three paired `historical - comparator` families for Top-1, Top-3, Top-5, Top-10, and MRR@100. The fifteen point estimates and 99% marginal percentile confidence intervals match the frozen inferential registry to the reported precision. All fifteen lower confidence limits are greater than zero.

The separate HE2_B contrast is correctly transcribed as:

```text
Recall@200 - Recall@100 = 0.202651515
95% CI = [0.066763106, 0.341601308]
```

The section correctly preserves the inferential design already defined in §4.7: 1,056 SERIE nested within 67 DAM, paired DAM-cluster bootstrap, series-weighted estimand, 10,000 bootstrap replicates, frozen seed 20263001, and no p-values. It does not recompute or introduce new tests, intervals, standardized effects, or Phase-E inference.

The hypothesis dispositions are correctly bounded:

```text
HE2 = SUPPORTED / FROZEN INTERNAL INFERENTIAL SCOPE ONLY
HE5 = INCONCLUSIVE / NO NEW INFERENTIAL TEST
```

No causal effect, external-population generalization, overall framework accuracy, or legal correctness claim is introduced. C28 and C29 are used within their authorized boundaries.

## 3. Bilingual equivalence

The English publication-facing text and Spanish semantic-control mirror contain the same four substantive paragraphs, the same 15 HE2_A estimates and confidence intervals, the same HE2_B estimate and interval, and the same bounded HE2/HE5 interpretation. Decimal punctuation is localized but values are equivalent.

```text
EN_ES_SEMANTIC_EQUIVALENCE = PASS
EN_ES_NUMERICAL_EQUIVALENCE = PASS
```

## 4. Markdown ↔ DOCX equivalence and OOXML audit

The four English and four Spanish §5.6 body paragraphs in the DOCX match the Markdown paragraphs exactly after extraction. The B05 and B06 DOCX packages contain the same 14 OOXML parts. The only changed package member is:

```text
word/document.xml
```

The following inherited package members are byte-identical, including `word/comments.xml`, `word/_rels/document.xml.rels`, `[Content_Types].xml`, `word/styles.xml`, `word/settings.xml`, `word/numbering.xml`, and `word/fontTable.xml`.

Structural counts in the B06 DOCX are:

```text
COMMENTS = 40
COMMENT_RANGE_STARTS = 40
COMMENT_RANGE_ENDS = 40
COMMENT_REFERENCES = 40
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
```

Thus the inherited comments and no-tracked-changes state are preserved.

## 5. Rendering and visual QA

The candidate DOCX was independently rendered with the canonical DOCX renderer and produced 58 pages. Against the previously audited 57-page B05 baseline, 52 corresponding pages were pixel-identical. The only changed corresponding pages were 27–29 and 56–57; page 58 is newly created by pagination. Pages 27–29 and 56–58 were visually inspected and contain no clipping, overlap, broken layout, missing glyphs, or malformed headings. The apparent pagination movement is consistent with insertion of the English and Spanish §5.6 prose.

```text
FULL_RENDER = PASS / 58 PAGES
VISUAL_QA = PASS
```

## 6. D-035 and GitHub scope

The two drafting commits version only the small Section 5.6 artifact and the execution response. No cumulative master or DOCX was versioned by the drafting execution. The received cumulative candidates were delivered as real files. No manual Base64, chunking, fragmentation, reassembly, or Word reconstruction from Markdown was used as a handoff workaround.

```text
D035_TIMEOUT_SAFE_HANDOFF = PASS
```

## Final assessment

B06 V01 is scientifically faithful to the frozen inferential evidence, stays within the authorized claims and manuscript boundary, preserves the cumulative masters correctly, and introduces no mandatory correction.

```text
FINAL_VERDICT = PASS
NEXT_GATE = AUTHOR_APPROVAL_FOR_EXACT_B06_V01_CANDIDATES
RESULTS_B07_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```