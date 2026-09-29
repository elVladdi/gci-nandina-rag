# 15 — G7-F03 focused Experimental re-audit after A09+A10 correction V01

## Nature of this request

This is a cross-role scientific re-audit request from **IA Gestora del Artículo** to **IA Experimental**.

It does not authorize IA Experimental to modify the article branch.

The purpose is to resolve the exact follow-up gate required by the prior G7-F03 verdict:

```text
G7_F03 =
REVISION_REQUIRED / EXECUTED / NOT_APPROVED

BLOCKING_FINDINGS =
G7F03-A09 + G7F03-A10
```

IA de Redacción has now materialized those two corrections in English and Spanish. IA Gestora independently audited the candidate and returned PASS for focused Experimental re-audit.

## Article-side identities

Repository:

`elVladdi/gci-nandina-rag`

Editorial branch:

`article/main-manuscript`

Canonical pre-correction baseline:

`article/manuscript/ARTICLE_MASTER_V036.md`

```text
V036_GIT_BLOB =
c9dcbcc376cdb121d30dc2408756a6c95b569a90

V036_SHA256 =
8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8
```

Correction prompt:

`article/prompts/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_V01.md`

Git blob:

`8e1f046a541aecf066ecafcc12b7648db09905bc`

Writing-AI completed response:

`article/responses/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_RESPONSE_V01.md@05ed16e4e22c3d34cb37b32c176a947373d9dde4`

Response Git blob:

`8613240e8c76e798a6803d355b8c1a33dd98bf38`

Correction section artifact:

`article/sections/pre_fast/Diagnostic_Reranker_A09_A10_V01.md`

Git blob:

`8a4578a992d20dc8f96ab88f08e95e666d4247c5`

Gestora audit:

`article/reviews/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_INTERNAL_REVIEW_V01.md@f9f5ffdbed54fbfbe7618bc823fd7885a11e5f5d`

Gestora-audit Git blob:

`e08df7d8d1e00c56da6acc48907679af5e3b1682`

Cumulative candidate identity audited by Gestora:

```text
ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.md
SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
EXPECTED_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1

ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx
SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
SIZE_BYTES = 112705
PAGE_COUNT = 73
```

The cumulative candidate files themselves are not promoted as canonical and were not versioned as manuscript masters. For scientific re-audit, the exact delta is fully materialized in the versioned section artifact above, and Gestora independently verified that removing exactly the four bilingual A09/A10 insertion paragraphs restores V036 byte-for-byte.

## Original G7-F03 sources

Re-read your own governing G7-F03 report and audit record from:

Branch:

`writing/g7-f03-article-scientific-review-v01`

Report:

`docs/writing/group7/g7_f03_article_scientific_review_v0.1.md`

Git blob:

`bc4ad51a8b219adb8cd9a9beab69cdfb5f7f1875`

Audit record:

`outputs/audits/group7_closure_v0.1.json`

Git blob:

`ed4f74610ed73ea76427bef2eef2f4319c698441`

Retain your own current Plan Maestro as governing authority.

## Scope of focused re-audit

Re-audit only the two prior blocking findings and any direct contradiction they could create with the already-passed scientific core.

### G7F03-A09 — method correction

Confirm whether the versioned A09 paragraphs now adequately document the executed diagnostic reranker protocol, including:

- diagnostic path separate from the primary fixed-Top-3 workflow;
- closed v0.2 pool;
- nominal depth 100 / effective 63–100;
- `historical_first_80_normative_20`;
- deduplication by first appearance;
- uniform random sampling without replacement over sorted eligible case IDs;
- seed 0;
- 20 sampled cases;
- 10 closed candidates per reranker input;
- labels excluded from selection/generation and used only for evaluation;
- local `qwen2.5:7b-instruct`;
- Ollama / Q4_K_M;
- `temperature=0`;
- JSON response;
- no retry / one attempt per input;
- candidate closure 20/20;
- observed 19 reference-in-pool / 1 reference-out-of-pool;
- no prespecified inferential test;
- no feedback to or replacement of the primary historical ranking/fixed Top-3.

### G7F03-A10 — result correction

Confirm whether the versioned A10 paragraphs now accurately report:

```text
sample_cases = 20
reference_in_pool = 19
reference_not_in_pool = 1

Top-1 = 0.50 -> 0.50
Top-3 = 0.65 -> 0.65
Top-5 = 0.80 -> 0.80
MRR = 0.6326 -> 0.6326

wins/ties/losses = 0/19/0
candidate_closure = 20/20
paired_inference = NOT RUN / NO PRE-SPECIFIED TEST
```

Confirm that the wording does not assert:

- improvement;
- degradation;
- statistical equivalence;
- non-inferiority;
- superiority;
- generalization;
- population-level null effect.

## Direct-contradiction check

Because the prior G7-F03 audit passed the rest of the scientific core, do not re-open the whole article unless one of the four inserted paragraphs directly contradicts a previously passed statement.

Check only whether A09/A10 create a direct contradiction with:

- primary flow authority;
- fixed Top-3;
- documentary-evidence role;
- HE3 disposition;
- EXP12 closure;
- inferential boundaries;
- benchmark scope.

Do not reinterpret unrelated sections.

## Required disposition

Return the formal status governed by your current Experimental Plan.

The expected scientific question is:

```text
HAVE_G7F03_A09_AND_A10_BEEN_SATISFIED_WITHOUT_NEW_SCIENTIFIC_CONTRADICTION?
```

If YES, state explicitly whether this closes:

```text
G7-F03 = CLOSED / APPROVED
GROUP7 = CLOSED / APPROVED
G8-F01 = ELIGIBLE
```

or the exact equivalent statuses required by your Plan.

If NO, identify the exact remaining defect and bind it to a frozen source. Do not create new scope.

## FAST-finalization constraint carry-forward

Also confirm whether your previous scientific disposition for final presentation remains valid:

### Main body

- G5-MAIN-01
- G5-MAIN-02
- G6-FIG-01

### Supplementary / Appendix

- G5-SECONDARY-01
- G5-SECONDARY-02
- G5-APPENDIX-01
- G5-APPENDIX-02
- G5-APPENDIX-03
- G5-APPENDIX-04
- G5-APPENDIX-05
- G6-FIG-02
- G6-FIG-03

And confirm whether the architecture Figure 1 remains scientifically permissible as an editorial figure provided any diagnostic reranker is depicted only as a separate lateral route with no feedback to the primary flow.

Do not design or generate tables/figures in this re-audit.

## Prohibitions

- Do not modify `article/main-manuscript`.
- Do not rewrite A09/A10 unless a scientific defect remains.
- Do not create a new experiment.
- Do not recompute metrics.
- Do not create a new CI or p-value.
- Do not re-open EXP12.
- Do not re-decide HE3 unless the correction directly contradicts its frozen evidence.
- Do not start G8-F01 unless your own Plan says G7-F03 and Group 7 are formally closed.
- Do not authorize FINAL-F01 on behalf of IA Gestora or the Author.

## Deliverable

Materialize/version the focused re-audit according to your current Experimental Plan and provide:

1. formal G7-F03 status;
2. A09 verdict;
3. A10 verdict;
4. direct-contradiction verdict;
5. Group 7 closure status;
6. G8-F01 eligibility status;
7. confirmation or revision of the G5/G6 table/figure disposition;
8. any exact remaining condition, if one exists.

## Stop condition

Stop after the focused G7-F03 re-audit.

Return control to:

`IA_GESTORA_DEL_ARTICULO`

Do not proceed into G8-F01 or article finalization.
