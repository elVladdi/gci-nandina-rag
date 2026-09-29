# D-188 — End Matter source-completeness audit and author-declaration boundary

## Español

```text
DECISION = D-188
PHASE = END_MATTER
SCOPE = SOURCE_COMPLETENESS + SUBMISSION_DECLARATIONS + FINAL_ASSEMBLY_BOUNDARY

CANONICAL_MASTER = ARTICLE_MASTER_V035
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V035.md
CANONICAL_MASTER_MD_SHA256 =
23a92e46f1fe3d7edfcf9210e1d90a133c17abf6b85e62ad3906171dc48589ac
CANONICAL_MASTER_MD_GIT_BLOB =
ddf3abb1826f93d5d82c0a135c0c2ae6b389e7fd

CANONICAL_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 =
de3c60c59bd71e5c5b101c7281a675b68faaf8275af64d7403f1ff51fa60905b
CANONICAL_MASTER_DOCX_SIZE_BYTES = 110919
CANONICAL_MASTER_DOCX_COMMENTS = 48
CANONICAL_MASTER_DOCX_TRACKED_CHANGES = 0
CANONICAL_MASTER_DOCX_PAGE_COUNT = 71

FRONT_MATTER_FINALIZATION = CLOSED / APPROVED / FROZEN / INTEGRATED

END_MATTER_B01_DATA_AND_REPRODUCIBILITY = SOURCE_READY
END_MATTER_B02_AUTHOR_DECLARATIONS = BLOCKED_AUTHOR_INPUT
END_MATTER_B03_REFERENCES = GESTORA_AUDIT_REQUIRED
END_MATTER_B04_SUPPLEMENTARY = EDITORIAL_DETERMINATION_REQUIRED

FINAL_GAP = SUBMISSION_ASSEMBLY_REQUIRED
```

## 1. Current target-journal requirements rechecked

The current Elsevier author guidance linked from the target-journal environment was rechecked on 2026-09-29.

Relevant submission controls include:

- a definitive author list before original submission;
- author-contribution disclosure using CRediT roles is encouraged;
- funding sources and sponsor role must be identified when applicable;
- competing interests must be explicitly disclosed by the authors;
- acknowledgements belong in a separate section before references when applicable;
- reference formatting is flexible at initial submission if consistent and bibliographically complete; DOI is encouraged where available;
- research-data availability should be stated according to the journal/submission data-policy workflow;
- substantive use of generative AI or AI-assisted technologies in manuscript preparation requires a separate disclosure immediately before the references; basic spelling/grammar-only use is exempt.

The final manuscript must therefore contain or be accompanied by the declarations required by the actual submission record.

## 2. B01 — Data availability and reproducibility resources

### Evidence available

The manuscript already states that the public reproducibility repository is intended as the clean scientific package for reference reproduction and external replication, but that the audited public snapshot is incomplete for one-command end-to-end reference reproduction from a fresh clone.

The current public reproducibility repository was independently rechecked:

```text
REPOSITORY =
https://github.com/elVladdi/gci-nandina-rag-reproducibility

AUDITED_HEAD =
254831cd955103faa2517065a7eed7fb340bbccc

README_GIT_BLOB =
eb31035160d88fbe5634ca8df414c4ed741bd624
```

Its README documents:

- reference, custom, and synthetic modes;
- configurable data and tariff hierarchy;
- normative-corpus compatibility requirements;
- group-independence and provenance controls;
- target interfaces for validation, experiment execution, and reference reproduction;
- that target commands are being implemented progressively.

The canonical manuscript further records that administrative reference CSVs are not assumed to be publicly redistributable and that restricted/non-redistributed inputs remain outside the public package.

### Disposition

```text
DATA_AVAILABILITY = DRAFTABLE_WITH_EXISTING_EVIDENCE
CODE_REPRODUCIBILITY_RESOURCES = DRAFTABLE_WITH_EXISTING_EVIDENCE
PUBLIC_REFERENCE_REPRODUCTION_COMPLETE = NO
ADMINISTRATIVE_REFERENCE_DATA_PUBLIC_REDISTRIBUTION = NOT_ESTABLISHED
CLAIM_OF_ONE_COMMAND_FRESH_CLONE_REPRODUCTION = PROHIBITED
```

No author invention is required for B01, but the final statement must not imply availability of restricted data or a reproducibility capability not currently materialized.

## 3. B02 — Human-author declarations

The repository and manuscript do not provide a governed basis for inventing the following declarations.

### 3.1. Final author list and submission metadata

Required from the author:

- complete author names in final publication order;
- affiliation(s) for each author;
- corresponding author;
- corresponding email;
- ORCID(s), if intended for submission.

The current manuscript master does not contain a final author/title-page metadata block.

### 3.2. CRediT

Required from the author:

- exact CRediT roles for each human author.

Permitted role vocabulary follows the Elsevier CRediT taxonomy, including:

`Conceptualization; Data curation; Formal analysis; Funding acquisition; Investigation; Methodology; Project administration; Resources; Software; Supervision; Validation; Visualization; Writing – original draft; Writing – review & editing.`

No role may be inferred from commits, account names, chat participation, or project history.

### 3.3. Funding

Required from the author:

Either:

```text
NO_SPECIFIC_GRANT = CONFIRMED
```

or, for every source:

```text
FUNDER_NAME = ...
GRANT_AWARD_NUMBER = ...
GRANT_RECIPIENT = ...
SPONSOR_ROLE = ...
```

No funding status may be inferred from silence.

### 3.4. Declaration of competing interest

Required from the author on behalf of all human authors:

Either an explicit declaration of no competing interests, or the exact relationships/interests that must be disclosed.

No conflict status may be inferred.

### 3.5. Acknowledgements

Required from the author:

Either:

```text
ACKNOWLEDGEMENTS = NONE
```

or the exact people/institutions to acknowledge and confirmation that naming them is authorized where needed.

### 3.6. Generative-AI manuscript-preparation declaration

This project has used generative-AI assistance substantively in manuscript drafting/editorial revision, not merely spelling or punctuation.

Elsevier's current policy therefore requires a manuscript-preparation AI declaration before the references.

Required from the author:

- exact AI tool/service name(s) to disclose;
- purpose(s) of use;
- confirmation that the authors reviewed/edited the AI-assisted content and accept full responsibility for the final article.

This declaration is separate from the experimental use of the local `qwen2.5:7b-instruct` model, which is already reported as part of the research Methods.

```text
AI_MANUSCRIPT_PREPARATION_DECLARATION = REQUIRED
AI_TOOL_LIST = AUTHOR_CONFIRMATION_REQUIRED
AUTHOR_OVERSIGHT_CONFIRMATION = REQUIRED
```

## 4. B03 — References

The current manuscript contains a References placeholder rather than the final bibliographic list.

The current Elsevier guidance does not impose strict reference formatting at initial submission, but it requires consistent references with the necessary bibliographic elements and encourages DOI inclusion where applicable.

Accordingly:

```text
REFERENCES_FINALIZATION = REQUIRED
REFERENCE_STYLE_AT_INITIAL_SUBMISSION = CONSISTENT_STYLE_SUFFICIENT
BIBLIOGRAPHIC_COMPLETENESS_AUDIT = REQUIRED
CITATION_TO_REFERENCE_BIJECTION_AUDIT = REQUIRED
DOI_METADATA_RECHECK = REQUIRED_WHERE_APPLICABLE
```

This work is editorial/bibliographic and can proceed after the author-declaration packet is fixed so that one final End Matter candidate can be assembled.

## 5. B04 — Supplementary material

No separate Supplementary Material claim is authorized yet.

The decision will be made after:

- reference finalization;
- reproducibility-package recheck;
- figure/table inventory;
- rubric/configuration inventory.

If no material needs a separate supplementary file, the placeholder should be removed rather than replaced by a meaningless "None" section unless the submission system specifically requests it.

## 6. Final submission-assembly gap discovered

V035 remains a governed cumulative manuscript, not yet a submission-clean file.

The manuscript itself explicitly states that drafting notes must be removed before submission. The current master still contains internal drafting instructions, including section-level editorial notes.

It also still contains:

`[Figure 1 placeholder — overall architecture and information flow.]`

Therefore:

```text
FINAL_GAP = SUBMISSION_ASSEMBLY_REQUIRED
INTERNAL_DRAFTING_NOTES_REMAIN = YES
FIGURE_1_PLACEHOLDER_REMAINS = YES
FINAL_REFERENCE_LIST_REMAINS = YES
FINAL_AUTHOR_METADATA_REMAINS = YES

SUBMISSION_READY = NO
```

This does not reopen already approved scientific prose. A later final-assembly block must remove internal scaffolding and resolve all submission artifacts without changing frozen scientific claims unless a separately governed correction is required.

## 7. Gate

```text
CURRENT_DRAFTING_PHASE = END_MATTER
CURRENT_GATE = END_MATTER_AUTHOR_DECLARATIONS_REQUIRED
NEXT_ACTOR = AUTHOR
NEXT_ACTION = PROVIDE_END_MATTER_DECLARATIVE_INPUTS

CANONICAL_MASTER = ARTICLE_MASTER_V035
CANONICAL_MASTER_GIT_BLOB =
ddf3abb1826f93d5d82c0a135c0c2ae6b389e7fd

END_MATTER_B01_DATA_AND_REPRODUCIBILITY = READY
END_MATTER_B02_AUTHOR_DECLARATIONS = BLOCKED_AUTHOR_INPUT
END_MATTER_B03_REFERENCES = PENDING_GESTORA_AUDIT
END_MATTER_B04_SUPPLEMENTARY = PENDING_EDITORIAL_DETERMINATION

AUTHOR_APPROVAL_GATE = NOT_OPEN
SUBMISSION_READY = NO
```

---

## English

D-188 audits End Matter source completeness after definitive Front Matter integration.

Data availability and reproducibility-resource statements can be drafted from existing project evidence, but the Managing AI must preserve the documented limitations of the current public package and must not claim public redistribution of administrative reference data.

Human-author declarations cannot be inferred. The author must provide the final author list/affiliations, CRediT roles, funding status/details, competing-interest statement, acknowledgements status/content, and the exact generative-AI manuscript-preparation disclosure inputs.

The reference list still requires a complete citation-to-reference and metadata audit. Supplementary material remains an editorial determination.

A separate final submission-assembly gap is also recorded because the governed master still contains internal drafting instructions, a Figure 1 placeholder, no final author metadata block, and no final reference list. These items must be resolved after End Matter without reopening frozen scientific prose by default.
