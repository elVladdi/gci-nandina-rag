# Internal Review — FAST-F01 Scientific Presentation V01

## Result

```text
REVIEW_RESULT = REVISION_REQUIRED
PHASE = FAST_FINALIZATION / FAST_F01

SOURCE_RESPONSE =
article/responses/16_FAST_F01_SCIENTIFIC_PRESENTATION_RESPONSE_V01.md@b4b0d668dfac40f93db40aef3b710c7028345960
SOURCE_RESPONSE_GIT_BLOB =
2eec6a1234b5011dad42101f5db93a476ea701c8

AUTHORIZATION = D-202
CANONICAL_INPUT_MASTER = ARTICLE_MASTER_V037

CANDIDATE_MD_SHA256 =
d106eba471d2653b38d10d52854a8bc274d8e9b4f21e6084e60b612766512183
CANDIDATE_MD_GIT_BLOB =
bfd02b2387605968ec6b2165c81f7a8be407cb97

CANDIDATE_DOCX_SHA256 =
69c417198bd841f8947f422968a415b87b1e2a1a43753c339df729330e784199
CANDIDATE_DOCX_SIZE_BYTES = 356904
CANDIDATE_DOCX_PAGE_COUNT = 79

SCIENTIFIC_CONTENT_AUDIT = PASS
EDITORIAL_PRESENTATION_AUDIT = REVISION_REQUIRED
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO

AUTHOR_APPROVAL_GATE = NOT_OPEN
CANONICAL_PROMOTION = NOT_AUTHORIZED
FAST_F02 = NOT_AUTHORIZED
FAST_F03 = NOT_AUTHORIZED
```

## 1. Scope and identity

PASS.

IA Gestora independently verified the real files delivered by Writing AI:

```text
ARTICLE_MASTER_CANDIDATE_FAST_F01_V01.md
SIZE_BYTES = 295839
SHA256 =
d106eba471d2653b38d10d52854a8bc274d8e9b4f21e6084e60b612766512183
GIT_BLOB =
bfd02b2387605968ec6b2165c81f7a8be407cb97

ARTICLE_MASTER_CANDIDATE_FAST_F01_V01.docx
SIZE_BYTES = 356904
SHA256 =
69c417198bd841f8947f422968a415b87b1e2a1a43753c339df729330e784199
```

The Markdown differs from V037 only in the authorized FAST-F01 zones:

- Figure 1 placeholder replacement, EN/ES;
- Table 1 insertion, EN/ES;
- Tables 2–3 insertion, EN/ES;
- Figure 2 insertion, EN/ES;
- whitespace associated with those insertions.

No unauthorized scientific rewrite was detected.

## 2. Scientific content

PASS.

The candidate preserves the frozen scientific content.

### Tables 2 and 3

The 15 HE2_A rows and the single HE2_B row are numerically consistent with the governed G5 sources.

No new metric, CI, p-value, experiment, or hypothesis disposition was introduced.

### Figure 2

The DOCX embeds a PNG with SHA-256:

`9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11`

which matches the identity reported by Writing AI for the approved G6-FIG-01 render.

The scientific panel structure and inferential semantics remain preserved.

### Diagnostic reranker text

The A09/A10 prose remains unchanged.

Therefore:

```text
NEW_SCIENTIFIC_CONTENT = NO
NEW_METRIC_OR_INFERENCE = NO
HE2 = PRESERVED
HE3 = PRESERVED
HE5 = INCONCLUSIVE / PRESERVED
EXP12 = CLOSED_WITHOUT_RETRIEVAL / PRESERVED
EXPERIMENTAL_REAUDIT_REQUIRED = NO
```

## 3. DOCX / OOXML structural audit

PASS structurally.

IA Gestora independently observed:

```text
ZIP_OOXML_INTEGRITY = PASS
OOXML_PART_COUNT = 16

COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
COMMENTS_XML_SHA256 =
57bee5d04cc9ed51628a4e10baef0730c0a07b58b9d8c3b436c64657f32821ea
COMMENTS_XML_BYTE_IDENTICAL_TO_V037_BASELINE = PASS

TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0

TABLES_IN_DOCUMENT_XML = 8
DRAWINGS_IN_DOCUMENT_XML = 4

MEDIA_IMAGE_1_SHA256 =
f98c46131df41abfc6f7671ef62563f5803b5790539d51b6ea47207370c61fd1

MEDIA_IMAGE_2_SHA256 =
9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11
```

The only pre-existing OOXML parts modified are:

- `[Content_Types].xml`;
- `word/_rels/document.xml.rels`;
- `word/document.xml`.

Two media files were added. No baseline part was removed.

## 4. Independent render audit

The exact candidate DOCX was independently rendered by IA Gestora to 79 pages.

No clipping, missing glyphs, corrupted images, or broken OOXML was detected.

However, visual correctness is **not sufficient for PASS** because several publication-facing presentation defects remain.

## 5. Finding FASTF01-R01 — Figure 1 authority path is visually ambiguous

**Severity: MAJOR / BLOCKING FAST-F01 PASS**

The main black flow is correct:

```text
Commercial description
-> Query normalization
-> Historical retrieval and ranking
-> Unique candidate construction
-> FIXED TOP-3
-> Candidate-specific documentary evidence
-> Context assembly
-> LLM explains
```

But the red dashed path in the delivered Figure 1 begins below `Unique candidate construction` and terminates with an arrowhead below `Candidate-specific documentary evidence`.

The separate box labeled `Diagnostic reranker only` is visually disconnected from that curved path.

This creates an unintended visual reading in which a red diagnostic/bypass route can appear to flow from candidate construction directly into documentary evidence while bypassing the fixed Top-3.

That is inconsistent with the purpose of Figure 1 and with D-201/D-202, which require the primary authority boundary to be visually unambiguous.

### Required correction

Use the simplest safe representation:

```text
REMOVE THE DIAGNOSTIC RERANKER FROM FIGURE 1
```

and remove the corresponding sentence from the Figure 1 caption.

The diagnostic reranker remains fully documented in Methods/Results A09/A10 and does not need to appear in the architecture figure.

Do not add a replacement diagnostic arrow, pool, or alternative pathway.

The corrected Figure 1 must show only the primary architecture and its authority annotations.

## 6. Finding FASTF01-R02 — Tables are not yet publication-ready in DOCX

**Severity: MAJOR / BLOCKING FAST-F01 PASS**

The Word render shows avoidable readability defects:

- Table 1 splits its final row across pages 19–20.
- Table 2 begins at the bottom of page 25 with only its first row and continues on page 26.
- The continuation of Table 2 does not repeat the header row.
- Several long numeric values and CI bounds wrap at arbitrary digit positions.
- Table 2/3 effective text size is materially smaller than surrounding manuscript text.
- The resulting layout is technically legible but not publication-ready.

This contradicts the FAST-F01 objective of improving readability.

### Required correction

Without changing scientific values:

1. use compact publication display precision:
   - proportions, paired differences, Recall values, Pool@200 and CI bounds: **4 decimal places**;
   - `EVAL_N` and `DAM_N`: integers;
2. retain the exact frozen source values in the audit/traceability record, but use the rounded display form in the publication-facing table;
3. keep each table row intact across page breaks;
4. repeat header rows on continuation pages;
5. use a minimum effective table font of approximately 8.5–9 pt;
6. if Table 2 still cannot be rendered cleanly in portrait, place only the page(s) containing Table 2/3 in a temporary landscape section, then return to portrait;
7. do not split Table 2 into multiple scientific tables and do not alter the authorized count of three main-body tables.

This is an editorial formatting change only and does not require Experimental re-audit.

## 7. Finding FASTF01-R03 — Spanish mirror table labels are not natural Spanish

**Severity: MINOR / REQUIRED**

The Spanish §5.2 table captions are Spanish, but Tables 2 and 3 retain English column labels such as:

- `Comparator`;
- `Metric`;
- `Historical - comparator`;
- `99% CI for paired difference`;
- `Contrast`;
- `Paired difference`;
- `Pool@200 context`.

For the bilingual internal master, translate these presentation labels naturally into Spanish while preserving conventional metric tokens such as Top-1, Top-3, MRR@100, Recall@100, Recall@200, EVAL_N, DAM_N and Pool@200.

No value may change except the authorized display rounding in FASTF01-R02.

## 8. Finding FASTF01-R04 — Markdown/DOCX Table 1 structural position mismatch

**Severity: MINOR / REQUIRED**

In the candidate Markdown, Table 1 appears at the end of §4.4 immediately before the §4.5 heading.

In the rendered DOCX, §4.5 appears first and Table 1 appears immediately below that heading.

The two cumulative candidates should represent the same manuscript structure.

### Required correction

Use the Markdown placement as canonical for this correction:

```text
END OF §4.4
TABLE 1
§4.5 HEADING
DETAILED SYSTEM EXECUTION
```

Move Table 1 in DOCX to match. Preserve all surrounding prose byte-equivalently except for the table insertion boundary.

## 9. Standalone Figure 2 handoff note

The standalone Figure 2 PNG attached in the Gestora chat is not byte-identical to the reported PNG:

```text
ATTACHED_PNG_SHA256 =
73b9df5b6a6c7f3240385c2f1c7a93692925b5be9f92bf87f691b903a38db66e
ATTACHED_DIMENSIONS = 1572 x 2048

DOCX_EMBEDDED_APPROVED_RENDER_SHA256 =
9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11
DOCX_EMBEDDED_DIMENSIONS = 1573 x 2049
```

This is **non-blocking** because the DOCX embeds the exact governed render and the canonical G6 source remains versioned. The corrective delivery should nevertheless return the exact standalone PNG used in the DOCX if the handoff contract requests it.

## 10. Gestora disposition

```text
SCIENTIFIC_AUDIT = PASS
OOXML_STRUCTURAL_AUDIT = PASS
VISUAL_PRESENTATION_AUDIT = REVISION_REQUIRED

BLOCKING_FINDINGS =
FASTF01-R01
FASTF01-R02

REQUIRED_MINOR_FINDINGS =
FASTF01-R03
FASTF01-R04

NEW_SCIENTIFIC_ANALYSIS_REQUIRED = NO
EXPERIMENTAL_REAUDIT_REQUIRED = NO

READY_FOR_AUTHOR_APPROVAL = NO
READY_FOR_CANONICAL_PROMOTION = NO
FAST_F02 = NOT_AUTHORIZED
FAST_F03 = NOT_AUTHORIZED

NEXT_ACTOR = IA_DE_REDACCION_CIENTIFICA
NEXT_ACTION = EXECUTE_NARROW_FAST_F01_CORRECTION
```
