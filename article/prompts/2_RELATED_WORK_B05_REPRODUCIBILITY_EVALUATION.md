# Related Work B05 — Section 2.5 Reproducibility and evaluation in knowledge-based decision support

## Role and authorization

Execute exclusively `Related Work B05 / Section 2.5 — Reproducibility and evaluation in knowledge-based decision support`.

This block is authorized only after approval and integration of B04 V02 under D-020. Do not draft Section 2.6 or any later manuscript section.

Read first and comply with:

- `article/START_HERE.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
- `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md`;
- `article/governance/D020_RELATED_WORK_B04_APPROVAL_INTEGRATION_AND_B05_START.md`;
- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
- `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`.

The KBS-34 editorial corpus governs rhetorical/editorial style only. Do not use it as scientific evidence unless a paper is independently part of the scientific bibliography and is re-verified as such.

## Frozen cumulative baseline

Use exclusively:

- `article/manuscript/ARTICLE_MASTER_V004.md`
- `article/manuscript/ARTICLE_MASTER_V004.docx`
- required DOCX SHA-256: `e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162`

If the exact baseline DOCX is inaccessible or its SHA-256 differs, stop with:

`BASELINE_DOCX_ACCESS_REQUIRED = YES`

Do not reconstruct the master and do not substitute another DOCX.

Preserve exactly:

- Sections 2.1–2.4;
- all 25 inherited citation-audit comments and their anchors/content;
- all structure and drafting notes outside Section 2.5, except removal of the placeholder/note belonging specifically to Section 2.5 when the new text is inserted.

## Authorized scientific function of Section 2.5

Draft a compact functional synthesis explaining why reproducible and auditable knowledge-based decision support requires more than reporting a final metric. The subsection should connect, only where the literature supports it:

1. dataset documentation and contextualization;
2. dataset identity, versioning, and split documentation;
3. provenance/lineage linking outputs to data, software/configuration, and transformations;
4. reproducibility as distinct from replication, robustness, and generalization;
5. evaluation design aligned with the function and output actually being assessed;
6. the need to preserve task-specific interpretation of metrics rather than treating heterogeneous metrics as interchangeable.

The prose must remain literature synthesis. Do not describe the present study's implementation or results.

Use a KBS-compatible narrative flow rather than a paper-by-paper catalogue. Prefer concrete entities and relations: what is documented, versioned, traced, reproduced, evaluated, and what each artifact or metric can and cannot establish.

A reasonable target is approximately 650–850 English words unless scientific economy supports a shorter section. Do not add material merely to reach a target length.

## Governing literature

Consult first the frozen maps:

- `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`;
- `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md` only where its conceptual boundaries are directly relevant;
- relevant retrieval/evaluation foundations already frozen under 0B-04A/0B-04B and earlier Related Work blocks when needed to support task–metric distinctions.

Likely core primary works from 0B-05A include, when genuinely needed:

- Bender & Friedman — data statements;
- Gebru et al. — Datasheets for Datasets;
- Mitchell et al. — FAIR Data Pipeline / provenance and lineage;
- Pineau et al. — reproducibility, replication, robustness, and generalization conventions;
- Raji et al. — internal lifecycle auditing / transparency trail.

This list is not a citation quota. Cite only sources necessary for the claims actually written.

For every citation used in the manuscript, re-retrieve and inspect the primary full text before finalizing the claim. Do not cite from frozen summaries, memory, abstracts, secondary citations, or prior comments alone. If a required full text cannot be re-accessed, report `ACCESS_RECHECK_REQUIRED` and do not use the unsupported claim.

## Mandatory scientific boundaries

Preserve at least these distinctions:

- `DATASET_DOCUMENTATION ≠ DATASET_QUALITY_CERTIFICATION`;
- `DATASET_DOCUMENTATION ≠ DEPENDENCE_CONTROL / LEAKAGE_PREVENTION`;
- `DATASET_IDENTITY / VERSIONING ≠ REPRODUCIBILITY`;
- `PROVENANCE / LINEAGE ≠ SUBSTANTIVE_CORRECTNESS`;
- `PROVENANCE ≠ FULL_REPRODUCIBILITY`;
- `REPRODUCIBILITY ≠ REPLICATION ≠ ROBUSTNESS ≠ GENERALIZATION`;
- `CODE / DATA AVAILABILITY ≠ GUARANTEED_REPRODUCTION`;
- `INTERNAL_LIFECYCLE_AUDIT ≠ FORMAL_REVIEW_OF_EACH_OUTPUT`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `CODE_RETRIEVAL ≠ PASSAGE_RETRIEVAL ≠ EVIDENCE_RETRIEVAL ≠ CLASSIFICATION`;
- `EVIDENCE_RETRIEVAL ≠ SUBSTANTIVE_EVIDENCE_CORRECTNESS`;
- `VISIBLE_CITATION / PROVENANCE / REPRODUCIBILITY ≠ LEGAL_CORRECTNESS`;
- `METRIC_ALIGNMENT ≠ TASK_EQUIVALENCE`.

When using Pineau et al., present their terminology as the operational convention adopted in that paper, not as universal nomenclature.

When using Bender & Friedman or Gebru et al., do not imply that data statements/datasheets eliminate bias, prove representativeness, prove split independence, or guarantee generalization.

When using Mitchell et al., do not equate traceable lineage with correctness or full reproducibility.

When using Raji et al., do not present lifecycle audit artifacts as formal per-output auditability or legal compliance.

## Prohibited content

Do not introduce or discuss as present-study material:

- the present architecture or its specific components;
- fixed Top-3 implementation details;
- NANDINA as empirical testbed;
- Chapter/Class 87;
- DAM or series-level partition details;
- H100/H150/H200;
- HE2, HE4, HE5;
- EXP11A, EXP11B, EXP12;
- own metrics or results;
- Group 3/4 results;
- the Group 4 comparison registry;
- FINAL_GAP;
- novelty, first-of-kind, uniqueness, SOTA, or superiority claims.

Do not convert Section 2.5 into the study's reproducibility-resources subsection. The present study's concrete repository, scripts, manifests, hashes, data releases, and configurations belong later in Experimental design / reproducibility resources.

Section 2.5 may end with a short transition toward Section 2.6 Positioning of this study, but must not perform that positioning or draft Section 2.6.

## Citation-comment requirements

Every English citation instance newly introduced in 2.5 must have an anchored Word comment containing at minimum:

- source identity and publication venue/version when supported by the inspected full text;
- authors;
- exact supporting passage from the primary source;
- Spanish translation of that passage;
- explanation of why it supports the manuscript claim;
- scope limitation where applicable.

The 25 inherited comments must remain exactly preserved.

Report:

- `PRIOR_CITATION_COMMENTS_PRESERVED = 25/25`;
- `B05_CITATION_COMMENT_COVERAGE = <N>/<N>`;
- `TOTAL_CITATION_COMMENT_COUNT = 25 + N`.

Do not add a citation merely to increase the count.

## Bilingual and prose controls

Part I remains the publication-facing English manuscript. Part II remains the Spanish semantic-control mirror.

The Spanish mirror must preserve scientific scope, qualifications, negations, distinctions, citations, and transitions of the English text; it need not reproduce awkward English syntax literally.

Apply SPCCR: avoid stacked abstractions and governance/specification prose. Prefer explicit subject–action–object relations and readable scientific transitions.

Section 2.5 should follow naturally from 2.4: after separating grounding, explanation, provenance and audit scopes, it should explain how documentation, traceability and evaluation design support reproducible assessment without collapsing those properties into correctness.

## Required outputs

Generate exactly these four B05 V01 deliverables:

1. `article/sections/related_work/RelatedWork_B05_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B05_V01.md`
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx`
4. `article/responses/2_RELATED_WORK_B05_RESPONSE_V01.md`

The candidate master must derive from the exact V004 cumulative baseline.

## QA and execution report

Before delivery, verify and report at minimum:

```text
BLOCK = RELATED_WORK_B05
BLOCK_REVISION = V01
SECTION = 2.5 Reproducibility and evaluation in knowledge-based decision support
BASELINE_MASTER = ARTICLE_MASTER_V004
BASELINE_DOCX_SHA256_EXPECTED = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
BASELINE_DOCX_SHA256_VERIFIED = <hash> / PASS
FULLTEXTS_RETRIEVED = [<sources actually cited>]
ACCESS_RECHECK_REQUIRED = <NONE or list>
PRIOR_2_1_TEXT_PRESERVED = PASS
PRIOR_2_2_TEXT_PRESERVED = PASS
PRIOR_2_3_TEXT_PRESERVED = PASS
PRIOR_2_4_TEXT_PRESERVED = PASS
PRIOR_CITATION_COMMENTS_PRESERVED = 25/25
B05_CITATION_COMMENT_COVERAGE = <N>/<N>
TOTAL_CITATION_COMMENT_COUNT = <25+N>
EN_ES_SEMANTIC_EQUIVALENCE = PASS
KBS_PROSE_QA = PASS
B05_B06_BOUNDARY = PASS
DOCX_OOXML_INTEGRITY = PASS
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS / <N>_OF_<N>_PAGES
MD_DOCX_EQUIVALENCE = PASS
DELIVERED_DOCX_SHA256 = <sha256>
COMMITTED_DOCX_SHA256 = <sha256>
ARTIFACT_IDENTITY_MATCH = PASS
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
RELATED_WORK_B06 = NOT_AUTHORIZED
```

The DOCX delivered to the author must be exactly the same binary as the DOCX committed to GitHub. Do not regenerate or resave it after computing the committed/delivered hash.

## Commit discipline and stopping condition

Before writing, inspect the live `article/main-manuscript` HEAD. Do not overwrite concurrent work.

Create one semantic commit containing only the four authorized B05 V01 deliverables. Do not modify governance, canonical masters, prior sections, experimental files, ARTICLE_STATUS, ARTICLE_WRITING_PLAN, SOURCE_REGISTRY, or CLAIM_EVIDENCE_MATRIX.

After the commit and delivery, stop.

`RELATED_WORK_B06 / SECTION_2.6 = NOT_AUTHORIZED`.