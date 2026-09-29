# D-206 — FAST-F02 boundary: End Matter, references and supplementary integrity

## Español

```text
DECISION = D-206
PHASE = FAST_FINALIZATION / FAST_F02
PREVIOUS_DECISION = D-205

CANONICAL_MASTER = ARTICLE_MASTER_V038
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V038.md
CANONICAL_MASTER_MD_GIT_BLOB =
b508aeccb7dab93a8b4cf25b185aa429dbe5577f
CANONICAL_MASTER_MD_SHA256 =
6201a9a47f86630f5f275ca7a6d9a01c2c642140a7f803cb390d26848721572e

CANONICAL_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_FAST_F01_V02.docx
CANONICAL_MASTER_DOCX_SHA256 =
7506189f32af5c9e99cb3bc87530b9ffd2ca09e3348f886c2b6c194080a21fe8
CANONICAL_MASTER_DOCX_SIZE_BYTES = 351420
CANONICAL_MASTER_DOCX_PAGE_COUNT = 79
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0

FAST_F01 = CLOSED / APPROVED / INTEGRATED
FAST_F02 = ACTIVE / BOUNDARY_DEFINED
FAST_F03 = NOT_AUTHORIZED

AUTHOR_INPUT_FORM =
article/forms/FAST_F02_AUTHOR_INPUT_PACKET_V01.md@3199985dbb52a907b80146ab413bda9023960a47
AUTHOR_INPUT_FORM_GIT_BLOB =
d186b2c03decc524fca941a0bff834a9a7160370
```

## 1. Objective

FAST-F02 must close the remaining End Matter and supporting-material integrity in one consolidated cycle, without reopening approved scientific prose.

It combines:

- author/title-page metadata;
- CRediT;
- funding;
- competing interests;
- acknowledgements;
- Data availability;
- code/reproducibility resources;
- reference-list integrity;
- supplementary material assembly;
- preservation of the already approved generative-AI declaration.

## 2. Parallel execution strategy

To minimize delay, FAST-F02 is split operationally into two parallel lanes.

### Lane A — Author factual packet

The Author supplies only facts that cannot be inferred:

- final author names and order;
- affiliations;
- corresponding author and email;
- ORCID(s), if used;
- CRediT roles;
- funding status/details;
- competing-interest status/details;
- acknowledgements;
- confirmation or exact correction of the current AI disclosure.

No AI role may infer these facts from project history.

### Lane B — Gestora autonomous audit

IA Gestora may proceed without waiting for Lane A on:

- Data availability wording from governed evidence;
- code/reproducibility wording;
- citation-to-reference inventory;
- reference completeness and DOI/metadata checks where possible;
- supplementary-material assembly from the already disposed G5/G6 artifacts;
- removal plan for End Matter placeholders.

## 3. Data availability / reproducibility constraints

D-188 remains binding.

Allowed:

- point to the public reproducibility repository;
- distinguish public, restricted and non-redistributable materials;
- state configurable/reference/custom/synthetic modes only to the extent currently documented;
- describe the public package as a reproducibility resource with its known limits.

Prohibited:

- claiming that restricted administrative reference data are publicly redistributable;
- claiming one-command fresh-clone end-to-end reproduction if not actually materialized;
- implying deployment readiness from repository availability.

## 4. Reference integrity

FAST-F02 must produce a final bibliographic list and audit:

```text
CITATION_TO_REFERENCE_BIJECTION = REQUIRED
BIBLIOGRAPHIC_COMPLETENESS = REQUIRED
CONSISTENT_REFERENCE_STYLE = REQUIRED
DOI_METADATA_CHECK = REQUIRED_WHERE_APPLICABLE
UNRESOLVED_REFERENCE = BLOCKER
```

No source may be invented.

## 5. Supplementary material

Carry forward the Experimental-AI disposition unchanged.

### Supplementary / Appendix

- G5-SECONDARY-01;
- G5-SECONDARY-02;
- G5-APPENDIX-01;
- G5-APPENDIX-02;
- G5-APPENDIX-03;
- G5-APPENDIX-04;
- G5-APPENDIX-05;
- G6-FIG-02;
- G6-FIG-03.

These may be assembled editorially but their scientific content may not be recomputed or altered.

FAST-F02 should create one compact supplementary package rather than multiple redundant files where practical.

## 6. Generative-AI declaration

The already approved declaration remains frozen unless the Author explicitly requests a factual correction.

Current disclosure:

- ChatGPT (OpenAI): manuscript drafting and language refinement;
- Codex (OpenAI): software implementation and code refinement;
- Author reviewed/edited AI-assisted outputs and accepts responsibility.

No new wording change is authorized by D-206 unless the Author marks `CHANGE_REQUIRED`.

## 7. Efficiency rule

FAST-F02 must aim for a single Writing-AI cycle after the factual author packet and Gestora audit are complete.

Do not open separate author gates for CRediT, funding, conflicts, acknowledgements, references or supplementary material unless a genuine factual blocker appears.

## 8. Current gate

```text
CURRENT_DRAFTING_PHASE = FAST_FINALIZATION / FAST_F02
CURRENT_GATE = FAST_F02_AUTHOR_INPUT_AND_GESTORA_AUDIT_PARALLEL

NEXT_ACTOR_A = AUTHOR
NEXT_ACTION_A = COMPLETE_FAST_F02_AUTHOR_INPUT_PACKET

NEXT_ACTOR_B = IA_GESTORA_DEL_ARTICULO
NEXT_ACTION_B = AUDIT_REFERENCES_DATA_AVAILABILITY_AND_SUPPLEMENTARY

FAST_F02_WRITING_EXECUTION = NOT_AUTHORIZED_YET
AUTHOR_APPROVAL_GATE = NOT_OPEN
FAST_F03 = NOT_AUTHORIZED
EXPERIMENTAL_G8_F01 = NOT_AUTHORIZED_BY_THIS_DECISION
```

---

## English

D-206 defines FAST-F02 as one consolidated End Matter, references, and supplementary-material cycle.

Author-only factual declarations and Managing-AI autonomous editorial audits may proceed in parallel. No Writing-AI execution is authorized until both lanes are complete enough to generate one bounded FAST-F02 prompt.
