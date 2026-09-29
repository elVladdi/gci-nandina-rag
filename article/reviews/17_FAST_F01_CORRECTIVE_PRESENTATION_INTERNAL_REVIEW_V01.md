# Internal Review — FAST-F01 Corrective Presentation V01

## Result

```text
REVIEW_RESULT = PASS
PHASE = FAST_FINALIZATION / FAST_F01_CORRECTION

SOURCE_RESPONSE =
article/responses/17_FAST_F01_CORRECTIVE_PRESENTATION_RESPONSE_V01.md@6ddf5c063efeb84ba3afd75960139371d8abeaa2
SOURCE_RESPONSE_GIT_BLOB =
da15118e2807e003e3cc67612404089fbd9d6d10

AUTHORIZATION = D-203
SOURCE_COMMIT_DECLARED_BY_WRITING_AI =
cbcc2ade43adc18d7329dc929f86648096d9f785

CANDIDATE_MD_SHA256 =
6201a9a47f86630f5f275ca7a6d9a01c2c642140a7f803cb390d26848721572e
CANDIDATE_MD_GIT_BLOB =
b508aeccb7dab93a8b4cf25b185aa429dbe5577f
CANDIDATE_MD_SIZE_BYTES = 293668

CANDIDATE_DOCX_SHA256 =
7506189f32af5c9e99cb3bc87530b9ffd2ca09e3348f886c2b6c194080a21fe8
CANDIDATE_DOCX_SIZE_BYTES = 351420
CANDIDATE_DOCX_PAGE_COUNT = 79

FIGURE1_PNG_SHA256 =
d43b3695af795b14174ccaddfb29bff3e6f976f5234fef16fdda5eafc4a880f7
FIGURE1_PNG_DIMENSIONS = 1800 x 720

SCIENTIFIC_CONTENT_AUDIT = PASS
EDITORIAL_PRESENTATION_AUDIT = PASS
OOXML_STRUCTURAL_AUDIT = PASS
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO

FAST_F01 = PASS_PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = READY_TO_OPEN
CANONICAL_PROMOTION = NOT_YET_AUTHORIZED
FAST_F02 = NOT_AUTHORIZED
FAST_F03 = NOT_AUTHORIZED
```

## 1. Identity audit

PASS.

IA Gestora independently verified the three real files returned by Writing AI:

```text
ARTICLE_MASTER_CANDIDATE_FAST_F01_V02.md
SIZE_BYTES = 293668
SHA256 =
6201a9a47f86630f5f275ca7a6d9a01c2c642140a7f803cb390d26848721572e
GIT_BLOB =
b508aeccb7dab93a8b4cf25b185aa429dbe5577f

ARTICLE_MASTER_CANDIDATE_FAST_F01_V02.docx
SIZE_BYTES = 351420
SHA256 =
7506189f32af5c9e99cb3bc87530b9ffd2ca09e3348f886c2b6c194080a21fe8

FAST_F01_Figure1_Architecture_V02.png
SIZE_BYTES = 84070
SHA256 =
d43b3695af795b14174ccaddfb29bff3e6f976f5234fef16fdda5eafc4a880f7
DIMENSIONS = 1800 x 720
```

The identities exactly match the finalized Prompt-17 response.

## 2. R01 — Figure 1

PASS.

The corrected Figure 1 now contains only the primary authority path:

```text
Commercial description
-> Query normalization
-> Historical retrieval and ranking
-> Unique candidate construction
-> FIXED TOP-3
-> Candidate-specific documentary evidence
-> Context assembly
-> Local LLM explanation
```

The diagnostic reranker, red dashed route, bypass, feedback path and diagnostic pool are absent.

The figure explicitly marks the fixed Top-3 as the authority boundary and states that documentary evidence is evidence-only and that the LLM is explanation-only.

The EN/ES Figure-1 captions remove only the sentence that previously stated that the diagnostic reranker was shown.

The A09/A10 diagnostic-reranker prose remains present outside the figure and is not reopened.

```text
R01_FIGURE1 = PASS
```

## 3. R02 — Tables 1–3 and display precision

PASS.

### Numeric display

All 15 HE2_A rows and the single HE2_B row are present.

The publication-facing values use four-decimal display precision.

IA Gestora checked the exact-to-display map supplied in the response against the V01 frozen values. The displayed values are ordinary decimal rounding of the exact governed source values.

No scientific value, numerator/denominator, inferential object, CI level or hypothesis disposition was changed.

### DOCX table behavior

Independent OOXML inspection shows the corrected FAST tables have repeating header rows and non-splitting rows.

For the six EN/ES FAST tables:

```text
EN Table 1: header rows = 1; cantSplit rows = 6; min explicit font = 9.0 pt
EN Table 2: header rows = 1; cantSplit rows = 16; min explicit font = 8.5 pt
EN Table 3: header rows = 1; cantSplit rows = 2; min explicit font = 8.5 pt

ES Table 1: header rows = 1; cantSplit rows = 6; min explicit font = 9.0 pt
ES Table 2: header rows = 1; cantSplit rows = 16; min explicit font = 8.5 pt
ES Table 3: header rows = 1; cantSplit rows = 2; min explicit font = 8.5 pt
```

Table 1 spans two pages in EN and ES, but no data row is split and the header repeats on the continuation page.

Table 2/3 are readable without arbitrary digit wrapping. No landscape section was required.

```text
R02_TABLE_LAYOUT = PASS
R02_DISPLAY_PRECISION = PASS
```

## 4. R03 — Spanish presentation labels

PASS.

The Spanish mirror uses the authorized labels, including:

- Comparador;
- Métrica;
- Histórico;
- Histórico - comparador;
- IC del 99% para la diferencia pareada;
- Contraste;
- Diferencia pareada;
- IC del 95%;
- Contexto Pool@200.

The comparator presentation labels are localized while metric tokens are preserved.

```text
R03_SPANISH_LABELS = PASS
```

## 5. R04 — Table 1 structural synchronization

PASS.

In both EN and ES the rendered DOCX now follows:

```text
final §4.4 paragraph
-> Table 1 caption
-> Table 1
-> §4.5 heading
-> first §4.5 prose paragraph
```

This matches the cumulative Markdown candidate.

```text
R04_MD_DOCX_TABLE1_POSITION = PASS
```

## 6. Markdown scope audit

PASS.

The V01 -> V02 Markdown diff is restricted to:

- Figure-1 image filename V01 -> V02;
- deletion of the diagnostic-reranker sentence from the EN/ES Figure-1 caption;
- four-decimal display precision in Tables 2–3 EN/ES;
- authorized Spanish Table-2/3 labels and comparator display labels.

No unrelated manuscript prose changed.

## 7. DOCX / OOXML audit

PASS.

Independent checks:

```text
ZIP_OOXML_INTEGRITY = PASS
OOXML_PART_COUNT = 16
OOXML_PART_NAMES_IDENTICAL_TO_V01 = PASS
OOXML_CHANGED_PARTS_VS_V01 =
word/document.xml;
word/media/image1.png

TABLES_IN_DOCUMENT_XML = 8
DRAWINGS_IN_DOCUMENT_XML = 4

TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0

COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48

COMMENTS_XML_SHA256 =
57bee5d04cc9ed51628a4e10baef0730c0a07b58b9d8c3b436c64657f32821ea
COMMENTS_XML_BYTE_IDENTICAL_TO_V01 = PASS

IMAGE1_SHA256 =
d43b3695af795b14174ccaddfb29bff3e6f976f5234fef16fdda5eafc4a880f7

FIGURE2_EMBEDDED_SHA256 =
9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11
FIGURE2_IDENTITY = PASS
```

Only `word/document.xml` and the corrected Figure-1 media bytes changed relative to the exact V01 DOCX. Figure 2 remains byte-exact.

## 8. Independent render and visual audit

PASS.

IA Gestora independently rendered the exact submitted V02 DOCX to 79 pages.

All 79 pages were reviewed for gross layout defects, clipping, overlap, missing glyphs and broken objects. The edited pages were additionally inspected at full detail:

```text
Figure 1 EN = p13
Table 1 EN = p19-p20
Tables 2-3 EN = p26
Figure 2 EN = p30

Figure 1 ES = p51
Table 1 ES = p58-p59
Tables 2-3 ES = p65-p66
Figure 2 ES = p70
```

No blocking visual defect was found.

## 9. Scientific controls

PASS.

```text
NEW_SCIENTIFIC_CONTENT = NO
NEW_EXPERIMENT = NO
NEW_METRIC = NO
NEW_CI = NO
NEW_P_VALUE = NO
NEW_LITERATURE = NO
NEW_CITATION = NO
NEW_HYPOTHESIS_DISPOSITION = NO

HE2 = PRESERVED
HE3 = PRESERVED
HE5 = INCONCLUSIVE / PRESERVED
EXP12 = CLOSED_WITHOUT_RETRIEVAL / PRESERVED

EXPERIMENTAL_REAUDIT_REQUIRED = NO
```

## 10. Gestora disposition

```text
FAST_F01_CORRECTIVE_EXECUTION = PASS
FASTF01-R01 = CLOSED
FASTF01-R02 = CLOSED
FASTF01-R03 = CLOSED
FASTF01-R04 = CLOSED

FAST_F01 = PASS_PENDING_AUTHOR_APPROVAL

READY_FOR_AUTHOR_APPROVAL = YES
READY_FOR_CANONICAL_PROMOTION = NO

NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_FAST_F01_V02

FAST_F02 = NOT_AUTHORIZED
FAST_F03 = NOT_AUTHORIZED
EXPERIMENTAL_G8_F01 = NOT_AUTHORIZED
```
