# 17 — FAST-F01 Corrective Presentation V01

## Role

Act exclusively as **IA de Redacción científica** for GIC-NANDINA.

This is a narrow corrective execution inside FAST-F01. Do not act as IA Gestora, IA Experimental, or Author.

## Governing context

Read completely:

- `article/governance/D200_G7_F03_A09_A10_AUTHOR_APPROVAL_AND_V037_INTEGRATION.md`;
- `article/governance/D201_FAST_FINALIZATION_MODE_AND_FAST_F01_BOUNDARY.md`;
- `article/governance/D202_FAST_F01_SCIENTIFIC_PRESENTATION_EXECUTION_AUTHORIZATION.md`;
- `article/prompts/16_FAST_F01_SCIENTIFIC_PRESENTATION_V01.md`;
- `article/responses/16_FAST_F01_SCIENTIFIC_PRESENTATION_RESPONSE_V01.md@b4b0d668dfac40f93db40aef3b710c7028345960`;
- `article/reviews/16_FAST_F01_SCIENTIFIC_PRESENTATION_INTERNAL_REVIEW_V01.md`;
- current `article/ARTICLE_STATUS.md`;
- current `article/ARTICLE_WRITING_PLAN.md`.

Execute only the corrections explicitly authorized below.

## Exact correction inputs

### Cumulative Markdown candidate V01

Real file:

`ARTICLE_MASTER_CANDIDATE_FAST_F01_V01.md`

Expected identity:

```text
SIZE_BYTES = 295839
SHA256 =
d106eba471d2653b38d10d52854a8bc274d8e9b4f21e6084e60b612766512183
GIT_BLOB_IF_MATERIALIZED =
bfd02b2387605968ec6b2165c81f7a8be407cb97
```

### Cumulative DOCX candidate V01

Real file:

`ARTICLE_MASTER_CANDIDATE_FAST_F01_V01.docx`

Expected identity:

```text
SIZE_BYTES = 356904
SHA256 =
69c417198bd841f8947f422968a415b87b1e2a1a43753c339df729330e784199
PAGE_COUNT = 79
COMMENTS = 48
TRACKED_CHANGES = 0
```

Do not reconstruct the DOCX from Markdown. Edit the exact V01 DOCX directly.

If either exact cumulative candidate is unavailable or does not match, stop at preflight.

## Scientific invariants

The FAST-F01 scientific content already passed Gestora audit.

Do not change:

- any scientific claim;
- any numerator/denominator;
- any source value;
- any hypothesis disposition;
- any inferential method;
- any paragraph outside the exact correction zones;
- Figure 2 scientific content;
- A09/A10 diagnostic reranker Methods/Results prose.

```text
NO_NEW_EXPERIMENT = YES
NO_NEW_METRIC = YES
NO_NEW_CI = YES
NO_NEW_P_VALUE = YES
NO_NEW_LITERATURE = YES
NO_NEW_CITATION = YES
NO_NEW_HYPOTHESIS_DISPOSITION = YES
EXPERIMENTAL_REAUDIT_REQUIRED = NO
```

## Correction R01 — Figure 1

The current Figure 1 contains a red dashed curved arrow that visually bypasses the fixed Top-3 and terminates at documentary evidence while the diagnostic reranker box is disconnected.

Replace Figure 1 with a simpler primary-architecture-only schematic.

### Required Figure 1 content

Show only:

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

Required authority annotations:

- historical retrieval / unique candidate construction determine membership and order;
- fixed Top-3 is the authority boundary;
- documentary evidence is evidence-only and cannot rerank or replace candidates;
- LLM role is explanation-only;
- downstream stages enrich/explain but do not alter ranking.

### Prohibited Figure 1 content

Do not show:

- diagnostic reranker;
- red dashed route;
- alternative candidate path;
- feedback arrow;
- bypass around fixed Top-3;
- diagnostic pool;
- reranker metrics.

The diagnostic reranker remains documented only in A09/A10 prose.

Update the Figure 1 caption in EN/ES by removing only the sentence that says the diagnostic reranker is shown.

Create/version:

`article/figures/FAST_F01_Figure1_Architecture_V02.svg`

and deliver:

`FAST_F01_Figure1_Architecture_V02.png`.

## Correction R02 — publication-ready Tables 1–3 in DOCX

Do not alter the underlying frozen numbers.

### Display precision authorization

For publication-facing display only, format:

- proportions;
- Recall values;
- Pool@200;
- paired differences;
- CI lower/upper bounds

to **4 decimal places**.

Example:

```text
0.509469696969697 -> 0.5095
0.3294468432754924 -> 0.3294
```

This is display formatting, not recomputation.

Keep:

- EVAL_N and DAM_N as integers;
- Top-k / MRR / Recall labels unchanged;
- all 15 HE2_A rows;
- the single HE2_B row;
- the same row ordering;
- the same three-table main-body count.

The response must include a machine-auditable mapping proving that every displayed 4-decimal value is the ordinary rounding of its exact frozen source value.

### DOCX layout requirements

- Do not allow a table row to split across pages.
- Repeat header rows on every continuation page.
- Effective table text must be approximately 8.5–9 pt or larger.
- Do not wrap numeric strings at arbitrary digit positions.
- Keep captions with the table start where feasible.
- If necessary, use a temporary landscape section for Tables 2–3 only, then return to portrait.
- Do not split Table 2 into multiple scientific tables.
- Do not create Table 4.

Table 1 may remain portrait if clean.

## Correction R03 — Spanish mirror labels

In the Spanish §5.2 Tables 2 and 3, translate presentation labels naturally.

Use:

### Tabla 2 headers

```text
Comparador
Métrica
Histórico
Comparador
Histórico - comparador
IC del 99% para la diferencia pareada
EVAL_N
DAM_N
```

Recommended comparator display labels:

```text
BM25 normativo flat
BM25 normativo jerárquico
MNRL D1a inspirado en Text2Trade
```

### Tabla 3 headers

```text
Contraste
Recall@100
Recall@200
Diferencia pareada
IC del 95%
Contexto Pool@200
EVAL_N
DAM_N
```

Preserve metric tokens where conventional.

## Correction R04 — Table 1 structural synchronization

The Markdown V01 places Table 1 at the end of §4.4 before the §4.5 heading.

Make this exact order true in both cumulative outputs:

```text
final paragraph of §4.4
Table 1 caption
Table 1
§4.5 heading
first §4.5 prose paragraph
```

Apply this in EN and ES.

Do not change the Table 1 scientific content except layout.

## Figure 2 freeze

Figure 2 must remain content-identical to the approved render already embedded in V01.

Expected embedded PNG SHA-256:

`9b7efbbdb4c2bb5e0829739717f544e752c0d4a188edcab399cd1da12f7f4e11`

Do not regenerate Figure 2 if doing so changes its bytes.

If a standalone Figure 2 is delivered, it must be the exact embedded PNG bytes.

## Comments / tracked changes

Preserve:

```text
COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
COMMENTS_XML_SHA256 =
57bee5d04cc9ed51628a4e10baef0730c0a07b58b9d8c3b436c64657f32821ea
TRACKED_CHANGES = 0
```

No comment may be removed or silently re-anchored outside an edited zone.

## Required output artifacts

Version:

1. `article/sections/fast/FAST_F01_Scientific_Presentation_V02.md`;
2. `article/figures/FAST_F01_Figure1_Architecture_V02.svg`;
3. `article/responses/17_FAST_F01_CORRECTIVE_PRESENTATION_RESPONSE_V01.md`.

Deliver as real files:

4. `ARTICLE_MASTER_CANDIDATE_FAST_F01_V02.md`;
5. `ARTICLE_MASTER_CANDIDATE_FAST_F01_V02.docx`;
6. `FAST_F01_Figure1_Architecture_V02.png`;
7. exact `G6_FIG_01_HE2_APPROVED_RENDER.png` if requested by the handoff.

Do not promote a canonical master.

## Required audits

### Markdown

Prove that, relative to candidate V01, changes are restricted to:

- Figure 1 image filename/caption;
- Table 1 placement synchronization if required;
- Table 2/3 display precision;
- Spanish Table 2/3 presentation labels.

No other Markdown change is authorized.

### DOCX / OOXML

Run and report:

- ZIP integrity;
- OOXML part inventory;
- comments / anchors;
- comments.xml byte identity;
- tracked changes;
- image relationship inventory;
- exact Figure 2 embedded PNG identity;
- full render;
- visual QA of every page;
- full-detail QA of every page containing Tables 1–3 or Figures 1–2;
- header repetition on any multipage table;
- row-split prevention;
- minimum effective table font;
- Markdown/DOCX visible-text and structural-order equivalence in changed zones.

## Response minimum fields

```text
SOURCE_COMMIT = ...
PHASE = FAST_FINALIZATION / FAST_F01_CORRECTION

PROMPT_IDENTITY = PASS / BLOCKED
AUTHORIZATION_IDENTITY = PASS / BLOCKED
INPUT_MD_IDENTITY = PASS / BLOCKED
INPUT_DOCX_IDENTITY = PASS / BLOCKED

R01_FIGURE1 = CORRECTED / BLOCKED
R02_TABLE_LAYOUT = CORRECTED / BLOCKED
R02_DISPLAY_PRECISION = PASS / BLOCKED
R03_SPANISH_LABELS = CORRECTED / BLOCKED
R04_MD_DOCX_TABLE1_POSITION = PASS / BLOCKED

MAIN_BODY_TABLE_COUNT = 3
MAIN_BODY_FIGURE_COUNT = 2

FIGURE2_EMBEDDED_SHA256 = ...
FIGURE2_IDENTITY = PASS / BLOCKED

COMMENTS = ...
COMMENT_RANGE_START = ...
COMMENT_RANGE_END = ...
COMMENT_REFERENCE = ...
COMMENTS_XML_BYTE_IDENTICAL = PASS / BLOCKED
TRACKED_CHANGES = ...
ZIP_OOXML_INTEGRITY = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = ...
FULL_DOCX_VISUAL_QA = ...

CANDIDATE_MD_SHA256 = ...
CANDIDATE_MD_EXPECTED_GIT_BLOB = ...
CANDIDATE_DOCX_SHA256 = ...
CANDIDATE_DOCX_SIZE_BYTES = ...

NEW_SCIENTIFIC_CONTENT = NO / BLOCKED
POST_EXECUTION_EXPERIMENTAL_REAUDIT_REQUIRED = NO

EXPECTED_EXIT = FAST_F01_CORRECTION_COMPLETED_PENDING_GESTORA_AUDIT
```

## Stop condition

Stop exactly at:

`FAST_F01_CORRECTION_COMPLETED_PENDING_GESTORA_AUDIT`

Do not begin FAST-F02, FAST-F03, or Experimental G8-F01.
