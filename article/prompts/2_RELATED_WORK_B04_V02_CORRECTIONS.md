# Related Work B04 — V02 Corrective Prompt

## Role and governing state

Execute exclusively the corrective revision of `Related Work B04 / Section 2.4 — Evidence grounding, explainability, and auditability`.

This is a controlled correction of B04 V01 after Managing-AI internal review. It is **not** authorization to draft Section 2.5 or any later manuscript section.

Read first and comply with:

- `article/START_HERE.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
- `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md`;
- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- the approved structure in `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`.

## Frozen baseline

Use exclusively the current canonical cumulative master:

- `article/manuscript/ARTICLE_MASTER_V003.docx`
- required SHA-256: `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`

If the exact baseline DOCX is not accessible or its SHA-256 does not match, stop with:

`BASELINE_DOCX_ACCESS_REQUIRED = YES`

Do not reconstruct the master and do not use any other DOCX as substitute.

Preserve exactly:

- Sections 2.1, 2.2 and 2.3;
- all 19 pre-existing citation-audit comments;
- the approved structure outside Section 2.4.

## Source text to correct

Use B04 V01 only as the source of the Section 2.4 draft to be corrected:

- `article/sections/related_work/RelatedWork_B04_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V01.md`

Do not broaden the subsection. Keep the same six scientific sources and the same six citation instances unless a strictly grammatical relocation is necessary.

## Mandatory corrections

Apply exactly the following three substantive corrections in both English and the Spanish semantic-control mirror.

### C1 — Lewis et al. (2020): narrow the provenance wording

The V01 wording `provide limited provenance support` is too strong for Lewis et al. (2020). The source supports updatable external/non-parametric knowledge and inspection of retrieved knowledge, while provenance remains an open issue.

Replace the relevant English wording with:

`can improve access to updatable external knowledge and make retrieved passages inspectable for verification.`

Use a semantically equivalent Spanish formulation:

`puede mejorar el acceso a conocimiento externo actualizable y hacer inspeccionables los pasajes recuperados para su verificación.`

Do not attribute provenance support to Lewis et al. (2020).

### C2 — Raji et al. (2020): do not attribute “output-level auditability” as an established construct

Raji et al. (2020) supports internal algorithmic auditing across the organizational/development lifecycle. Do not present `output-level auditability` as a construct defined by that source.

Replace the definitional sentence with:

`At the level of an individual output, a distinct review question is whether that output can be examined against explicit criteria using its associated evidence and trace.`

Use the semantically equivalent Spanish formulation:

`A nivel de una salida individual, una cuestión de revisión distinta es si esa salida puede examinarse contra criterios explícitos utilizando la evidencia y la traza asociadas.`

In the synthesis paragraph, use wording such as `review at the level of individual outputs` rather than presenting `output-level auditability` as a literature-established taxonomy.

### C3 — Grainger (2024): narrow “necessary” to “relevant”

The source presents illustrative criteria/capabilities for electronic tariff tools; it does not establish those properties as universally necessary.

Replace:

`Documentary authority and currency are therefore necessary properties to examine...`

with:

`Documentary authority and currency are therefore relevant dimensions to examine...`

Apply the same semantic narrowing in Spanish.

## Citation and comment controls

Re-verify the six B04 citation instances against the primary full texts before finalizing V02.

Every B04 English citation must retain an anchored Word comment containing, at minimum:

- source / journal or publication venue;
- authors;
- exact supporting passage from the primary source;
- Spanish translation of that passage;
- why the passage supports the manuscript claim;
- scope limitation where applicable.

Expected comment counts:

- inherited comments: `19/19`;
- B04 comments: `6/6`;
- total comments: `25`.

Do not add citations or sources merely to compensate for the three corrections.

## Scientific boundaries

Do not introduce:

- present-study results;
- HE4;
- FINAL_GAP;
- novelty claims;
- present-study architecture;
- fixed Top-3 details of the present study;
- NANDINA as the empirical testbed;
- Chapter 87;
- H100;
- DAM;
- claims from pending or unauthorized experimental work.

Preserve these distinctions:

- `VISIBLE EVIDENCE / CITATION ≠ CLAIM SUPPORT`;
- `RATIONALE / REASONING TRACE ≠ FAITHFULNESS GUARANTEE`;
- `PROVENANCE / LINEAGE ≠ SUBSTANTIVE CORRECTNESS`;
- `LIFECYCLE AUDIT ≠ REVIEW OF AN INDIVIDUAL OUTPUT`;
- `OFFICIAL SOURCE / DOCUMENT AUTHORITY ≠ CORRECT LEGAL INTERPRETATION`;
- `DOCUMENT CURRENCY / TRACEABILITY ≠ LEGAL VALIDITY OF THE MODEL OUTPUT`.

Section 2.4 may end by preparing the transition to reproducibility/evaluation, but it must not draft Section 2.5.

## Artifact identity correction

B04 V01 had a traceability discrepancy between the DOCX SHA-256 declared in the repository execution report and the separately delivered DOCX binary. V02 must close this issue.

The DOCX delivered to the author must be **exactly the same binary** as the DOCX committed to GitHub.

The execution report must explicitly include:

```text
DELIVERED_DOCX_SHA256 = <sha256>
COMMITTED_DOCX_SHA256 = <sha256>
ARTIFACT_IDENTITY_MATCH = PASS
```

Both hashes must be identical.

Do not regenerate, resave or otherwise modify the DOCX after computing the hash of the binary that will be committed and delivered.

## Required outputs

Generate exactly these four authorized deliverables:

1. `article/sections/related_work/RelatedWork_B04_V02.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V02.md`
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V02.docx`
4. `article/responses/2_RELATED_WORK_B04_RESPONSE_V02.md`

The cumulative DOCX must derive from the exact `ARTICLE_MASTER_V003.docx` baseline and contain only the corrected Section 2.4 addition plus the preserved prior content/comments.

## QA requirements

Before delivery, verify and report:

```text
BLOCK = RELATED_WORK_B04
BLOCK_REVISION = V02
SECTION = 2.4
BASELINE_DOCX_SHA256_EXPECTED = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
BASELINE_DOCX_SHA256_VERIFIED = <hash> / PASS
C1_LEWIS_CORRECTION = PASS
C2_RAJI_CORRECTION = PASS
C3_GRAINGER_CORRECTION = PASS
PRIOR_2_1_TEXT_PRESERVED = PASS
PRIOR_2_2_TEXT_PRESERVED = PASS
PRIOR_2_3_TEXT_PRESERVED = PASS
PRIOR_CITATION_COMMENTS_PRESERVED = 19/19
B04_CITATION_COMMENT_COVERAGE = 6/6
TOTAL_CITATION_COMMENT_COUNT = 25
EN_ES_SEMANTIC_EQUIVALENCE = PASS
DOCX_OOXML_INTEGRITY = PASS
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS / <N>_OF_<N>_PAGES
MD_DOCX_EQUIVALENCE = PASS
DELIVERED_DOCX_SHA256 = <sha256>
COMMITTED_DOCX_SHA256 = <sha256>
ARTIFACT_IDENTITY_MATCH = PASS
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```

If any required control fails, do not report completion.

## Commit discipline and stopping condition

Create a single semantic commit containing only the four authorized V02 deliverables.

Do not modify governance files, canonical masters, prior approved sections, experimental files, or any unrelated artifact.

After the commit and delivery, stop.

`RELATED_WORK_B05 / SECTION_2.5 = NOT_AUTHORIZED`.
