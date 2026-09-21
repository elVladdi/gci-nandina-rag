# Related Work B05 V01 — technical closure after scientific and author approval

## Authorization

Execute exclusively the technical closure of `RELATED_WORK_B05 / Section 2.5`.

Scientific drafting and QA are already complete. The IA Gestora independently audited B05 V01 and returned `PASS`; the author has explicitly approved B05 V01.

Do **not** revise scientific prose. Do **not** advance to B06 / Section 2.6. Do **not** integrate a canonical master. Integration and B06 authorization remain the responsibility of the IA Gestora after verification of this commit.

Read first `article/START_HERE.md` and the applicable governance documents.

## Live-branch gate

Before writing, inspect the live `article/main-manuscript` HEAD.

The parent expected immediately before execution is the commit that introduces this technical-closure prompt. If the branch has changed after that commit, inspect the new commits and stop if any concurrent manuscript work conflicts with this closure. Never force-update the branch.

## Frozen B05 V01 artifacts

Use the exact local artifacts already generated and delivered to the author. Do not regenerate, normalize, re-export, or resave the manuscript artifacts.

Required repository paths and exact identities:

1. `article/sections/related_work/RelatedWork_B05_V01.md`
   - SHA-256: `1093cacb99de062f687786cb29f06ae96fdc2b16160d29287df797ed339a0495`
   - expected Git blob: `7f0c67fd3a3449a92e23e27a371660793622013e`

2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B05_V01.md`
   - SHA-256: `56c1e03af0d803777818a973462e4e70c849266b56f5cb11f396cc915fc22efe`
   - expected Git blob: `25782b8b2305b546f2f5ff69514893d045e50762`

3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx`
   - SHA-256: `042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`
   - expected Git blob / `git hash-object`: `064dc9fb69a26c831f44b4e3bd1d7a5c47b1113d`

4. `article/responses/2_RELATED_WORK_B05_RESPONSE_V01.md`
   - start from the exact local execution report already delivered;
   - make **only** the execution-status replacements defined below;
   - no scientific prose or QA result may be changed.

## Required finalization of the response report

In both the Spanish and English status blocks, make exactly these replacements:

- after `BLOCK_REVISION = V01`, insert:
  - `INTERNAL_REVIEW = PASS`
  - `AUTHOR_APPROVAL = RECEIVED`

- replace:
  - `COMMITTED_DOCX_SHA256 = NOT_AVAILABLE / SEMANTIC_COMMIT_NOT_CREATED`
  with
  - `COMMITTED_DOCX_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`

- replace:
  - `ARTIFACT_IDENTITY_MATCH = NOT_EVALUABLE / SEMANTIC_COMMIT_NOT_CREATED`
  with
  - `ARTIFACT_IDENTITY_MATCH = PASS`

- replace:
  - `DELIVERY_STATE = DRAFT_COMPLETE / SEMANTIC_COMMIT_BLOCKED`
  with
  - `DELIVERY_STATE = COMPLETED / READY_FOR_INTEGRATION`

After these exact changes, the finalized response report must have:

- SHA-256: `b74e1f92bcceb6817aea582f605857291dd3486cdf3e720037396cea86d9d36a`
- expected Git blob: `c06a045fb36a0e6fc777d4b0f13a5f9378b52075`

If either identity differs, stop and report the mismatch. Do not improvise edits.

## Binary-safe Git procedure

The DOCX must be committed byte-for-byte identical to the approved local binary.

Use a low-level Git-object workflow. If `create_blob` is available, base64-encode the **raw DOCX bytes** locally and create the blob with `encoding=base64`. The SHA returned by GitHub must be exactly:

`064dc9fb69a26c831f44b4e3bd1d7a5c47b1113d`

For each Markdown artifact, create a Git blob from its exact UTF-8 bytes and verify the expected blob SHA above.

Then:

1. obtain the current base tree from the live HEAD;
2. create one new tree based on that tree, adding exactly the four authorized B05 paths;
3. create **one semantic commit** with the live HEAD as its single parent;
4. move `article/main-manuscript` to that commit using a normal fast-forward update (`force=false`).

Do not use the Contents API to create sequential commits on `article/main-manuscript`.
Do not create placeholders, `__noop__`, temporary files, test files, or auxiliary commits on `article/main-manuscript`.
Do not use force push or history rewriting.

If your connector cannot perform the exact binary-safe blob creation, stop **before any branch write** and report `BINARY_BLOB_CREATION_UNAVAILABLE = YES`.

## Hard file-scope gate

The semantic commit must add exactly these four paths and no others:

- `article/sections/related_work/RelatedWork_B05_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B05_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx`
- `article/responses/2_RELATED_WORK_B05_RESPONSE_V01.md`

Do not modify:

- `ARTICLE_MASTER_V004.md/.docx`;
- `ARTICLE_STATUS.md`;
- `ARTICLE_WRITING_PLAN.md`;
- `SOURCE_REGISTRY.md`;
- `CLAIM_EVIDENCE_MATRIX.md`;
- any governance file;
- any prior Related Work section;
- any experimental file.

## Verification before stopping

After the branch update, verify:

```text
BLOCK = RELATED_WORK_B05
BLOCK_REVISION = V01
INTERNAL_REVIEW = PASS
AUTHOR_APPROVAL = RECEIVED
SEMANTIC_COMMIT = CREATED
SEMANTIC_COMMIT_FILE_SCOPE = PASS / EXACTLY_4_FILES
DELIVERED_DOCX_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a
COMMITTED_DOCX_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a
COMMITTED_DOCX_GIT_BLOB = 064dc9fb69a26c831f44b4e3bd1d7a5c47b1113d
ARTIFACT_IDENTITY_MATCH = PASS
RELATED_WORK_B06 = NOT_AUTHORIZED
```

## Response in chat

Return only:

- semantic commit SHA;
- resulting branch HEAD;
- the four committed paths;
- committed DOCX SHA-256;
- committed DOCX Git blob;
- `ARTIFACT_IDENTITY_MATCH`;
- `SEMANTIC_COMMIT_FILE_SCOPE`;
- confirmation `RELATED_WORK_B06 = NOT_AUTHORIZED`.

Then stop.
