# Related Work B04 V02 — Technical Closure Prompt

## Scope

Execute exclusively the technical closure of `Related Work B04 V02 / Section 2.4` after scientific review and explicit author approval.

Do not draft new scientific content. Do not advance to B05 / Section 2.5.

Read first and comply with:

- `article/START_HERE.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/prompts/2_RELATED_WORK_B04_V02_CORRECTIONS.md`.

## Governing state

The B04 V02 content has already passed independent Managing-AI review and received explicit author approval.

```text
RELATED_WORK_B04_V02_CONTENT = PASS
AUTHOR_APPROVAL = RECEIVED
SOURCE_SUPPORT = PASS / 6_OF_6
C1_LEWIS = PASS
C2_RAJI = PASS
C3_GRAINGER = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
PRIOR_CITATION_COMMENTS = 19/19
B04_CITATION_COMMENTS = 6/6
TOTAL_CITATION_COMMENTS = 25
DOCX_RENDER = PASS / 23_OF_23_PAGES
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

The only remaining task is to close binary artifact identity and create the semantic delivery commit.

## Live-branch control

Before writing, verify the live HEAD of `article/main-manuscript`.

The Managing AI last verified:

`4544cc79e430d61c2e2d112d03d42f8659c2ec91`

If HEAD has changed, inspect the intervening commits first. Do not force-update the branch, discard concurrent work, or overwrite unrelated changes.

## Exact DOCX artifact

Use exactly the already finalized B04 V02 DOCX delivered to the author:

`article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V02.docx`

Required SHA-256:

`e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162`

Do not regenerate, resave, normalize, reconstruct, or otherwise modify this DOCX. Do not alter comments, OOXML metadata, relationships, ZIP package order, or any byte.

## Required semantic commit

Create one semantic commit containing exactly these four deliverables:

1. `article/sections/related_work/RelatedWork_B04_V02.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V02.md`
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V02.docx`
4. `article/responses/2_RELATED_WORK_B04_RESPONSE_V02.md`

Do not include any fifth file.

The DOCX must be committed through a binary-safe mechanism that preserves the original bytes. Do not commit a base64 representation as the file contents and do not convert the DOCX to text.

## Hard artifact-identity gate

After the commit, verify the committed DOCX independently.

The response must report:

```text
DELIVERED_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
COMMITTED_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
ARTIFACT_IDENTITY_MATCH = PASS
```

If this identity cannot be established, do not report completion and do not create a partial commit.

## Response V02 required controls

`article/responses/2_RELATED_WORK_B04_RESPONSE_V02.md` must record at least:

```text
BLOCK = RELATED_WORK_B04
BLOCK_REVISION = V02
SECTION = 2.4
BASELINE_DOCX_SHA256_EXPECTED = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
BASELINE_DOCX_SHA256_VERIFIED = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7 / PASS
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
DOCX_RENDER = PASS / 23_OF_23_PAGES
MD_DOCX_EQUIVALENCE = PASS
DELIVERED_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
COMMITTED_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
ARTIFACT_IDENTITY_MATCH = PASS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = COMPLETED / READY_FOR_INTEGRATION
```

## Prohibited modifications

Do not modify:

- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- any governance file;
- `ARTICLE_MASTER_V003.md/.docx`;
- any experimental file;
- any previously approved Related Work section.

Do not promote `ARTICLE_MASTER_V004`.

## Stopping condition

After the single semantic commit, stop.

Return only:

- semantic commit SHA;
- resulting branch HEAD;
- the four committed paths;
- committed DOCX SHA-256;
- `ARTIFACT_IDENTITY_MATCH`;
- confirmation `RELATED_WORK_B05 = NOT_AUTHORIZED`.

Canonical promotion, B04 freeze/integration, and B05 authorization remain exclusive to the Managing AI after commit verification.
