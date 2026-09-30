# 18 — FAST-F02 End Matter, References & Supplementary Integrity V01

## Scope

FAST-F02 finalizes content-bearing End Matter, references, and supplementary material using ARTICLE_MASTER_V038 as the manuscript baseline.

Markdown baseline:
- path: article/manuscript/ARTICLE_MASTER_V038.md
- SHA-256: 6201a9a47f86630f5f275ca7a6d9a01c2c642140a7f803cb390d26848721572e
- Git blob: b508aeccb7dab93a8b4cf25b185aa429dbe5577f

Word baseline:
- file: ARTICLE_MASTER_CANDIDATE_FAST_F01_V02.docx
- SHA-256: 7506189f32af5c9e99cb3bc87530b9ffd2ca09e3348f886c2b6c194080a21fe8
- size: 351420 bytes
- comments: 48
- tracked changes: 0
- baseline page count: 79

The Word candidate must derive directly from the exact Word baseline.

## Governing inputs

- article/governance/D206_FAST_F02_END_MATTER_REFERENCES_SUPPLEMENTARY_BOUNDARY.md
- article/governance/D208_FAST_F02_AUTHOR_FIELDS_INTENTIONALLY_BLANK.md
- article/reviews/18_FAST_F02_GESTORA_AUTONOMOUS_AUDIT_V01.md
- article/manifests/FAST_F02_SUPPLEMENTARY_ASSEMBLY_V01.md
- article/forms/FAST_F02_AUTHOR_FIELDS_DEFERRAL_V01.md
- article/STYLE_GUIDE.md

## Author-administrative fields

The following manuscript fields are intentionally blank for this workflow: author metadata not already present, corresponding-author designation, CRediT, Funding, competing interests, and Acknowledgements.

Existing drafting placeholders in CRediT, Funding, competing interests, and Acknowledgements are removed while their headings remain. No previously supplied author facts are inserted. Blank status is final for FAST-F02 and is not a blocker.

The already approved generative-AI declaration remains unchanged.

## Content-bearing End Matter

Data availability must state that administrative/reference inputs used in the governed study are not represented as publicly redistributable. Public code, configuration contracts, documentation, and reproducibility resources are available in the public repository elVladdi/gci-nandina-rag-reproducibility, audited at commit 254831cd955103faa2517065a7eed7fb340bbccc. Exact reference-study reproduction may require restricted or non-redistributed inputs.

Code and reproducibility wording must describe the documented reference/custom/synthetic modes, data/provenance contracts, experiment protocol, taxonomy/normative-corpus configuration, reproducibility guidance, and compatible user-supplied data. It must not describe the audited public snapshot as a complete one-command fresh-clone end-to-end reproduction of the full reference study or claim deployment readiness.

## References

The final working bibliography contains exactly the 25 cited works recorded in article/reviews/18_FAST_F02_GESTORA_AUTONOMOUS_AUDIT_V01.md. No additional reference is added.

Existing author-year in-text citations are preserved. A consistent author-year bibliography is used for this working master. Verified DOI or persistent identifiers are included where available. Lee et al. Explainable Product Classification for Customs retains the audited 2023 arXiv identity rather than silently changing the in-text year to 2024.

Required checks:
- 25 unique English-body cited works
- 25 English reference entries
- 0 unresolved citations
- 0 orphan references
- 0 duplicate reference identities
- Spanish mirror uses the same bibliography

## Supplementary Material

The package contains exactly:
- Tables S1-S7 corresponding to G5-SECONDARY-01, G5-SECONDARY-02, and G5-APPENDIX-01 through G5-APPENDIX-05
- Figure S1 = G6-FIG-02
- Figure S2 = G6-FIG-03

All canonical paths, blobs, roles, and interpretation constraints are those frozen in article/manifests/FAST_F02_SUPPLEMENTARY_ASSEMBLY_V01.md.

No new metric, CI, p-value, experiment, hypothesis disposition, or scientific recomputation is permitted.

The main manuscript Supplementary material section states only that Supplementary Material accompanies the article and contains Tables S1-S7 and Figures S1-S2; the full supplement is not duplicated in the main article.

## Main-manuscript edit boundary

Only these EN/ES blocks may change:
- Data availability
- Code and reproducibility resources
- CRediT body to blank
- Funding body to blank
- competing-interest body to blank
- Acknowledgements body to blank
- References
- Supplementary material statement

Title, Abstract, Keywords, Sections 1-7, Tables 1-3, Figures 1-2, A09/A10, Discussion, Conclusion, and the generative-AI declaration remain unchanged. No author metadata is added to the title page.

## Required outputs

Version:
- article/sections/fast/FAST_F02_End_Matter_References_V01.md
- article/supplementary/SUPPLEMENTARY_MATERIAL_FAST_F02_V01.md
- article/manifests/FAST_F02_REFERENCE_BIJECTION_V01.md
- article/responses/18_FAST_F02_END_MATTER_REFERENCES_SUPPLEMENTARY_RESPONSE_V01.md

Deliver as real files:
- ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.md
- ARTICLE_MASTER_CANDIDATE_FAST_F02_V01.docx
- SUPPLEMENTARY_MATERIAL_FAST_F02_V01.md
- SUPPLEMENTARY_MATERIAL_FAST_F02_V01.docx

No canonical promotion occurs during execution.

## QA

Manuscript QA must demonstrate that changes are confined to the authorized End Matter blocks. Blank administrative headings remain, placeholders are removed, and no author facts are inserted.

DOCX QA includes ZIP/OOXML integrity, 48 comments and anchors, zero tracked changes, comments.xml preservation, relationship/media inventory, full render, all-page visual QA, detailed End Matter-page QA, and Markdown/DOCX visible-text equivalence for changed blocks.

Supplementary QA includes MD/DOCX equivalence, source identity for S1-S7, and Figure S1/S2 content identity against the approved G6 assets.

## Completion state

The response reports all baseline identities, End Matter status, reference bijection results, supplementary inventory results, DOCX/OOXML checks, full render/visual QA, output hashes, and whether any Experimental re-audit is required.

Expected completion state:
FAST_F02_COMPLETED_PENDING_GESTORA_AUDIT

FAST-F03 and Experimental G8-F01 remain outside this scope.
