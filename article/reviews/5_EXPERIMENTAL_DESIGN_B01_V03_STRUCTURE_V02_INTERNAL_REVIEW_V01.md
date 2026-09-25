# Experimental Design B01 V03 — Independent internal review under Structure V02

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_V02_INTERNAL_REVIEW_V01
DATE = 2026-09-24
ROLE = IA_GESTORA / LEAD_SCIENTIFIC_EDITOR
GOVERNING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
GOVERNING_STRUCTURE_BLOB = f5270e02e3af1407a2dec2988d6382e433972d3e
PARENT_DECISIONS = D-045 / D-046
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B01_V02_STRUCTURE_V02_REWRITE_RESPONSE_V01.md@829adb40d2e29d96c4b59ca555915e1c81fa307e
SECTION_MD = article/sections/experimental_design/Experimental_Design_B01_V02.md
SECTION_MD_SHA256 = 7e9337fa6e8f0f33c6863c9292cb3f697fbcd7654630656518f6b83c14f75b4b
SECTION_MD_GIT_BLOB = 2f78e3c3f66e797c8328ae6f4b2dddd7c1871e7d
MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
MASTER_CANDIDATE_MD_SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346
MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
MASTER_CANDIDATE_DOCX_SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
B01_SCIENTIFIC_CONTENT = PASS
SECTION_3_FORWARD_REFERENCE_AMENDMENTS = PASS
PUBLICATION_DETAIL_LEVEL = PASS
DOCX_OOXML_INTEGRITY = PASS
DOCX_RENDER_QA = PASS
CUMULATIVE_MASTER_STRUCTURE_V02_ALIGNMENT = FAIL
OVERALL = CONTENT_PASS / STRUCTURAL_CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_3_AND_LATER_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

## 1. Scope of the independent audit

The review independently checked the rewritten B01 against D-045, D-046, Structure V02, the governing experimental sources, the exact returned Markdown and DOCX artifacts, and the versioned Drafting-AI response. A self-declared PASS in the execution response was not treated as approval.

The audit covered: (i) scientific framing and scope; (ii) claim-to-source fidelity; (iii) publication-facing level of technical detail; (iv) the two authorized editorial amendments in Section 3; (v) bilingual semantic consistency; (vi) cumulative-master structural alignment with Structure V02; and (vii) DOCX package/render integrity.

## 2. Scientific and editorial content — PASS

### 2.1 Section 4.1

The revised 4.1 correctly presents the study as an offline experimental evaluation of a concrete instantiation of the Section-3 architecture. It no longer defines the experiment primarily as a non-binding decision-support tool. It correctly states the eight-digit NANDINA/Chapter-87 empirical boundary, SERIE as the analysis unit, DAM as the grouping unit when dependence matters, and the boundary between configurability and empirical performance transfer.

The wording `evaluate/evaluar` is consistent with the approved epistemic strength. The text does not claim operational customs deployment, legal adjudication, or empirical generalization beyond the evaluated setting.

### 2.2 Section 4.2.1 — source and collection

The narrative now begins at the scientific source and actual collection procedure rather than at an intermediate workbook. The statements on SUNAT Aduanet, import for consumption, Maritime Customs Office of Callao, the numbering and collection periods, orange/red channels, recorded cancellation, authorized release, Chapter-87 eligibility, purposive collection, manual copying of series, and procedural screenshots are supported by SRC-02.

The bounded provenance statement is also acceptable: functional reconstruction of relevant processed content is distinguished from binary identity of the complete historical workbook.

### 2.3 Section 4.2.2 — processing and curation

The text distinguishes automated series-level transformation from curation. The stated operations are supported by SRC-02 and frozen processing logic: declaration/series-block parsing, extraction and concatenation of description lines, reproducible series identity, spacing preparation, eight-digit NANDINA/hierarchy derivation, required-field and hierarchy controls, Chapter-87 filtering, critical parse-warning controls, exact duplicate handling, and exclusion of conflicting identifier groups.

The counts 11,320 series / 107 DAM, 4,232 Chapter-87 records before curation, and 4,106 curated records agree with the governing experimental record.

### 2.4 Section 4.2.3 — partition construction and composition

The text correctly states that v0.2 was materialized through explicit whole-DAM assignments and that the recorded seed is provenance metadata rather than the assignment mechanism. It correctly reports zero DAM and reproducible-series-identifier overlap across the three partitions and the frozen composition:

- historical: 2,950 series / 28 DAM / 66 represented codes;
- development: 100 / 6 / 9;
- evaluation: 1,056 / 67 / 42 represented reference codes.

It also correctly avoids presenting the 66 historical codes as the exhaustive Chapter-87 universe and defers detailed duplicate/near-duplicate validity diagnostics to 4.4.

### 2.5 Publication-facing detail level

The principal defect of the prior B01 version has been corrected. The rewritten 4.1–4.2.3 contains no narrative inventory of SHA-256 values, repository paths, physical CSV/workbook names, worksheet names, script names, or other internal artifact identifiers. Scientific provenance, collection, transformation, curation, split construction, and composition govern the narrative instead.

## 3. Controlled Section-3 amendments — PASS

The two backward dependencies registered by D-044/D-045 were amended without reopening the scientific architecture. Section 3.5 now points to the concrete documentary source/version and retrieval conditions in Section 4 while reserving exhaustive technical identities for reproducibility resources. Section 3.7 now describes the reproducibility repository by the resource classes and reconstruction function rather than promising a publication-facing inventory of hashes/paths.

No authority, ordering, or interface rule of the frozen architecture was changed.

## 4. Artifact and DOCX integrity — PASS

Independent local verification of the delivered artifacts produced the exact hashes reported by the Drafting AI:

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346

ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
```

DOCX package comparison against the canonical baseline found only `word/document.xml` changed. `word/comments.xml` remained byte-identical with SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`. The candidate retains 40 comments, 40 comment-range starts, 40 comment-range ends, 40 comment references, and zero tracked insert/delete/move elements.

The complete 40-page rendering was visually inspected. No clipping, overlap, missing glyphs, broken tables, or page-layout failures were found. The blank section-break page is inherited/acceptable. Layout QA therefore passes independently of the editorial findings below.

## 5. Blocking structural finding — cumulative master not aligned to Structure V02

Although the new B01 prose itself follows Structure V02, the cumulative candidate still retains the old V01 skeleton from Section 4.3 onward:

```text
4.3 Documentary corpus
  4.3.1 Source documents and scope
  4.3.2 Corpus preparation
  4.3.3 Versioning and temporal validity
  4.3.4 Retrieval index
4.4 Partitioning and dependence control
4.5 System configuration
4.6 Evaluation framework and research-question mapping
4.7 Candidate-retrieval evaluation
4.8 Documentary-evidence evaluation
4.9 Controlled-explanation evaluation
4.10 Statistical analysis
4.11 Reproducibility resources
```

This conflicts with the author-approved and frozen Structure V02, which requires:

```text
4.3 Documentary corpus and evidence resource
4.4 Partition validity and dependence controls
4.5 Experimental system configuration and execution
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
4.7 Statistical and robustness analysis
4.8 Reproducibility resources
```

This is not a scientific defect in the newly written B01 content and is not attributed to Drafting-AI noncompliance. D-046 simultaneously made Structure V02 governing while prohibiting modification of Section 4.3 and later. Because the canonical V009 still contained the V01 skeleton, strict compliance necessarily preserved a structure that had already been superseded. The conflict was introduced by the Gestora's scope definition and must be corrected through a narrowly authorized structural alignment.

No scientific prose for 4.3–4.8 is authorized by this finding. Only headings, drafting-purpose notes/placeholders, and numbering may be aligned to the already approved Structure V02.

## 6. Additional deterministic residue — Spanish Section-4 placeholder

The Spanish mirror still contains a stale generic placeholder immediately after `4. Diseño experimental` and before `4.1. Entorno y alcance experimental`:

`[Section text to be drafted in a later approved version.]`

Because 4.1 and 4.2 are now populated, this placeholder is obsolete. It must be removed mechanically. The English mirror does not contain an equivalent stale placeholder at this location.

## 7. Verdict and required action

```text
B01_SCIENTIFIC_PROSE = PASS
B01_FACTUAL_TRACEABILITY = PASS
B01_EDITORIAL_FOCUS = PASS
SECTION_3_AMENDMENTS = PASS
DOCX_BINARY_AND_LAYOUT_QA = PASS
MASTER_STRUCTURE_ALIGNMENT = FAIL
STALE_SPANISH_PLACEHOLDER = FAIL
AUTHOR_APPROVAL_GATE = NOT_OPEN
```

The next operation must be a technical/editorial correction only:

1. preserve the approved B01 prose and the two Section-3 amendments byte-for-byte at the text level;
2. align the unfilled Section-4.3+ skeleton in both language mirrors to Structure V02 without drafting scientific prose;
3. remove the stale Spanish Section-4 placeholder before 4.1;
4. preserve all 40 inherited comments and zero tracked changes;
5. return exact cumulative Markdown and DOCX artifacts for differential audit.

After that differential correction passes, B01 can proceed to the author's scientific approval gate. No Section-4.3+ scientific drafting is opened by this review.