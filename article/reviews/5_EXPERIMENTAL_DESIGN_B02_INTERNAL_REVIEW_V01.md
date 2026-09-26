# Internal review — Experimental Design B02 V01

```text
REVIEW = 5_EXPERIMENTAL_DESIGN_B02_INTERNAL_REVIEW_V01
DATE = 2026-09-25
BLOCK = EXPERIMENTAL_DESIGN_B02_SECTION_4_3
RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B02_RESPONSE_V01.md@83d9df1bc2e9410ba9a6cacb606d348c6c25f1f8
SECTION = article/sections/experimental_design/Experimental_Design_B02_V01.md
MASTER_CANDIDATE_MD_SHA256 = 22f5a6e1168e08ef6281488024a4ac5e4f6742ee90a96d8f31e5453c592bf592
MASTER_CANDIDATE_DOCX_SHA256 = 40d492911b2163a4c6a837f292f3056aa49bcbf69ce9dc3caf50aa80f021ae1e
SCIENTIFIC_CONTENT = PASS
SECTION_4_3_SCOPE = PASS
DOCX_INTEGRITY = PASS
OVERALL = PASS_WITH_TWO_NARROW_COHERENCE_CORRECTIONS
AUTHOR_APPROVAL_GATE = NOT_YET_OPEN
```

## 1. Scientific audit

Section 4.3 is supported by the governing experimental sources and respects D-051.

Verified independently:

- the primary documentary resource is the hierarchical NANDINA corpus derived from Decision 885;
- the primary association operation is exact lookup by the already fixed candidate NANDINA-8 code;
- no query-based normative retrieval over the commercial description is used in this primary path;
- no historical/documentary score fusion, documentary reranking, candidate insertion, substitution, or fallback to another code is performed;
- hierarchical parent fields are context and are not promoted to exact eight-digit evidence;
- the documentary record/context is passed downstream while Top-3 membership and order remain fixed;
- Decision 906 modifies Decision 885 and entered into force before the 2026 administrative cases; the manuscript correctly discloses that the primary experiment retained the Decision-885-derived frozen resource without converting this into a blanket claim of Chapter-87 invalidity.

The prose is appropriately compact for Methods and avoids repository paths, hashes, filenames, internal experiment labels and performance leakage.

English and Spanish versions are semantically aligned.

## 2. Differential scope audit

The cumulative Markdown differs from the approved B01 V05 baseline only in the English and Spanish Section 4.3 blocks. Sections 4.4–4.8 and Results remain undrafted.

The uploaded artifacts match the declared hashes.

DOCX independent checks:

```text
OOXML_PART_COUNT = 14
OOXML_PART_SET_VS_BASELINE = IDENTICAL
CHANGED_PARTS = word/document.xml ONLY
COMMENTS = 40 / PRESERVED
COMMENTS_XML = BYTE_IDENTICAL_TO_BASELINE
TRACKED_CHANGES = 0
RENDERED_PAGE_COUNT = 41
RENDER_QA = PASS
```

## 3. Required narrow correction C01 — Structure V02 label

D-052 explicitly deferred the residual master label correction to the next cumulative candidate:

```text
NEXT_CUMULATIVE_CANDIDATE_STRUCTURE_LABEL = KBS_ARTICLE_WORKING_STRUCTURE_V02
```

The B02 candidate still displays `KBS_ARTICLE_WORKING_STRUCTURE_V01` in the cumulative master. This is an administrative/editorial consistency defect, not a scientific defect in Section 4.3.

Required action: replace the legacy visible/internal master structure label with `KBS_ARTICLE_WORKING_STRUCTURE_V02` wherever that master label is used, without altering scientific prose or formatting beyond what the label replacement necessarily changes.

## 4. Required narrow correction C02 — Andean documentary authority vs. Peruvian context

B02 correctly establishes that the primary documentary resource derives from Decision 885 of the Commission of the Andean Community. The already frozen Introduction still contains the phrase `the Peruvian administrative and documentary context defined in Methods`, and its Spanish mirror says `contexto administrativo y documental peruano`. The Section-3 drafting note also retains `the Peruvian corpus` / `corpus peruano`.

Those formulations can now be read as attributing the documentary resource itself to a Peruvian national corpus, which conflicts with the authority distinction fixed by D-051. This inconsistency predates B02 and is not a drafting failure of Section 4.3.

Required action is narrowly limited to four coherence edits:

1. English Introduction: distinguish the **Peruvian administrative context** from the **Andean documentary resource**.
2. Spanish Introduction: same semantic distinction.
3. English Section-3 drafting note: replace `the Peruvian corpus` with a neutral reference to the documentary resource used in the experiment.
4. Spanish Section-3 drafting note: same correction.

Do not otherwise reopen Introduction, Architecture, B01 or Section 4.3.

## 5. Verdict

```text
B02_SECTION_4_3_SCIENTIFIC_CONTENT = VERIFIED / PASS
B02_SECTION_4_3_PUBLICATION_FIT = PASS
B02_DOCX = PASS
B02_GLOBAL_CANDIDATE = CORRECTION_REQUIRED_BEFORE_AUTHOR_APPROVAL
CORRECTION_SCOPE = C01 + C02 ONLY
SECTION_4_4_PLUS = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
