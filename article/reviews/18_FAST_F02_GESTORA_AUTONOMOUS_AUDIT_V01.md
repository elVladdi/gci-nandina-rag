# FAST-F02 Gestora Autonomous Audit V01

## Result

```text
AUDIT_RESULT = PASS_WITH_AUTHOR_FACTS_PENDING
PHASE = FAST_FINALIZATION / FAST_F02
CANONICAL_MASTER = ARTICLE_MASTER_V038
CANONICAL_MASTER_GIT_BLOB = b508aeccb7dab93a8b4cf25b185aa429dbe5577f

DATA_AVAILABILITY = READY_FOR_WRITING_AI
REPRODUCIBILITY_RESOURCES = READY_FOR_WRITING_AI
REFERENCE_INVENTORY = COMPLETE / 25 UNIQUE CITED WORKS
REFERENCE_METADATA_AUDIT = READY_WITH_ONE_EDITORIAL_YEAR_NORMALIZATION
SUPPLEMENTARY_SOURCE_INVENTORY = COMPLETE
SUPPLEMENTARY_ASSEMBLY = READY_FOR_WRITING_AI

AUTHOR_FACTS = PARTIAL / 5 DECLARATIONS PENDING
FAST_F02_WRITING_EXECUTION = BLOCKED_ONLY_BY_AUTHOR_FACTS
EXPERIMENTAL_REAUDIT_REQUIRED = NO_BY_DEFAULT
```

## 1. Scope

This audit executes the Managing-AI lane authorized by D-206 while the Author lane proceeds in parallel.

It does not modify ARTICLE_MASTER_V038 and does not authorize Writing-AI execution.

## 2. Data availability and reproducibility audit

### Public repository verified

Repository:

`elVladdi/gci-nandina-rag-reproducibility`

Audited head:

`254831cd955103faa2517065a7eed7fb340bbccc`

README Git blob:

`eb31035160d88fbe5634ca8df414c4ed741bd624`

The repository currently documents:

- reference, custom and synthetic usage modes;
- configurable tariff hierarchy and jurisdiction;
- configurable normative corpus;
- group-independence controls;
- dataset/data-provenance contracts;
- target interfaces for validation, experiment execution and reference reproduction;
- documentation for data contracts, provenance, experiment protocol, reproducibility, taxonomy/normative corpus and custom data.

Relevant documentation identities observed:

```text
docs/DATA_CONTRACT.md =
4611667ced7f596089822b749800555be21e7fb8

docs/DATA_PROVENANCE.md =
e7fac0b48c9fc53c2e09f99807d8be7609277ac6

docs/EXPECTED_RESULTS.md =
361686e6c6d300a8c8732819a1db4c58b278d839

docs/EXPERIMENT_PROTOCOL.md =
3782e98bd6423ce3a7cfe7a4cd5d620e2573ccaa

docs/REPRODUCIBILITY.md =
839b4245fcf4497ebf6ced28dd8771e3b29601c4

docs/TAXONOMY_AND_NORMATIVE_CORPUS.md =
9512b1583c5a78cc0cd2d356a60f30d3ddfc41ed

docs/USING_YOUR_OWN_DATA.md =
e852ab22c47164689699b8be8d338763c5f23f44
```

### Important limitation rechecked

The repository README explicitly describes its quick-start commands as a **target interface** to be implemented progressively.

At the audited head, the root `scripts/` directory contains only `scripts/README.md`; therefore a publication-facing statement must not claim that one-command fresh-clone end-to-end reference reproduction is currently complete.

The administrative/reference inputs used by the governed experiment are not established as publicly redistributable.

### Approved wording boundary

FAST-F02 may draft a concise statement with the following meaning:

```text
DATA_AVAILABILITY =
The administrative/reference data used in the study are not represented as
publicly redistributable. Public code, configuration contracts,
documentation and reproducibility resources are provided through the
project's reproducibility repository. Reproduction of the exact reference
study may require access to restricted/non-redistributed inputs.

CODE_AND_REPRODUCIBILITY =
The public repository documents the experimental protocol, configurable
data and taxonomy contracts, provenance requirements and reference/custom/
synthetic modes. The current public snapshot supports inspection and
progressive reproduction/replication workflows but must not be described as
a complete one-command fresh-clone reproduction of the full reference study.
```

Writing AI may polish this wording but may not strengthen the availability/reproducibility claim.

## 3. Citation inventory

A full scan of the English publication-facing body of V038 identifies **25 unique cited works**:

1. Ding et al. (2015)
2. Luppes (2019)
3. Ruder (2020)
4. Anggoro et al. (2025)
5. Lee et al. (2021)
6. Stassin et al. (2023)
7. Pain (2021)
8. Spichakova & Haav (2020)
9. Qi et al. (2025)
10. Lee et al. (2023)
11. Wang et al. (2026)
12. Lewis et al. (2020)
13. Ma et al. (2023)
14. Koch & Power (2025)
15. Marra de Artiñano et al. (2023)
16. Kim et al. (2025)
17. Nguyen et al. (2026)
18. Asai et al. (2022)
19. Bender & Friedman (2018)
20. Gebru et al. (2021)
21. Mitchell et al. (2022)
22. Pineau et al. (2021)
23. Raji et al. (2020)
24. Grainger (2024)
25. Chen & Tanaka-Ishii (2026)

No additional author-year citation was found in the English body.

## 4. Reference metadata audit

The final reference list may use a consistent author-year style for initial submission. Metadata were reconciled against the frozen literature corpus and current authoritative/publication records.

### 4.1 Ready references with stable DOI or canonical publication identity

```text
Ding, L.; Fan, Z.; Chen, D. (2015).
Auto-Categorization of HS Code Using Background Net Approach.
Procedia Computer Science 60, 1462-1471.
DOI 10.1016/j.procs.2015.08.224.

Anggoro, A.W.; Corcoran, P.; De Widt, D.; Li, Y. (2025).
Harmonized system code classification using supervised contrastive learning
with sentence BERT and multiple negative ranking loss.
Data Technologies and Applications 59(2), 276-301.
DOI 10.1108/DTA-01-2024-0052.

Stassin, S.; Amel, O.; Mahmoudi, S.A.; Siebert, X. (2023).
Similarity versus Supervision: Best Approaches for HS Code Prediction.
ESANN 2023.
DOI 10.14428/esann/2023.ES2023-163.

Spichakova, M.; Haav, H.-M. (2020).
Application of Machine Learning for Assessment of HS Code Correctness.
Baltic Journal of Modern Computing 8(4), 698-718.
DOI 10.22364/bjmc.2020.8.4.13.

Qi, L.; Zhang, Q.; Lin, X.; Zhang, J.; Liao, M. (2025).
Attribute knowledge and KBGAT for predicting the accuracy of the harmonized
system code for classifying import and export commodities.
Scientific Reports 15, 43504.
DOI 10.1038/s41598-025-16580-7.

Koch, T.; Power, K. (2025).
Automating Harmonized System (HS) Code Classification from Unstructured
Shipping Manifests using Large Language Models.
2025 IEEE High Performance Extreme Computing Conference (HPEC), 1-5.
DOI 10.1109/HPEC67600.2025.11196693.

Ma, X.; Gong, Y.; He, P.; Zhao, H.; Duan, N. (2023).
Query Rewriting in Retrieval-Augmented Large Language Models.
Proceedings of EMNLP 2023, 5303-5315.
DOI 10.18653/v1/2023.emnlp-main.322.

Kim, H.; Kim, G.; Choi, K. (2025).
Development of an Automated HS Code Classification System Using LLM Based on
an Optimized RAG Framework.
The Journal of Information Systems 34(3), 167-189.
DOI 10.5859/KAIS.2025.34.3.167.

Asai, A.; Gardner, M.; Hajishirzi, H. (2022).
Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.
NAACL 2022, 2226-2243.
DOI 10.18653/v1/2022.naacl-main.162.

Bender, E.M.; Friedman, B. (2018).
Data Statements for Natural Language Processing: Toward Mitigating System
Bias and Enabling Better Science.
Transactions of the Association for Computational Linguistics 6, 587-604.
DOI 10.1162/tacl_a_00041.

Gebru, T.; Morgenstern, J.; Vecchione, B.; Vaughan, J.W.; Wallach, H.;
Daumé III, H.; Crawford, K. (2021).
Datasheets for Datasets.
Communications of the ACM 64(12), 86-92.
DOI 10.1145/3458723.

Mitchell, S.N. et al. (2022).
FAIR data pipeline: provenance-driven data management for traceable
scientific workflows.
Philosophical Transactions of the Royal Society A 380(2233), 20210300.
DOI 10.1098/rsta.2021.0300.

Raji, I.D. et al. (2020).
Closing the AI accountability gap: defining an end-to-end framework for
internal algorithmic auditing.
Proceedings of FAT* 2020, 33-44.
DOI 10.1145/3351095.3372873.

Grainger, A. (2024).
Customs Tariff Classification and the Use of Assistive Technologies.
World Customs Journal 18(1), 3-32.
DOI 10.55596/001c.116525.

Chen, H.; Tanaka-Ishii, K. (2026).
Executable explanation traces for legal LLM predictions via
retrieval-augmented codification.
Frontiers in Artificial Intelligence 9, 1905145.
DOI 10.3389/frai.2026.1905145.
```

### 4.2 Ready thesis / repository records

```text
Luppes, J. (2019).
Classifying Short Text for the Harmonized System with Convolutional Neural
Networks.
Master's thesis, Radboud University.

Ruder, D. (2020).
Application of Machine Learning for Automated HS-6 Code Assignment.
Master's thesis, Tallinn University of Technology.

Pain, K. (2021).
Harmonized System Code Classification Using Transfer Learning with
Pre-Trained Weights.
Master of Computer Science thesis, Dalhousie University.
Repository handle: 10222/80672.
```

### 4.3 Ready preprint / working-paper identities that preserve the cited year

```text
Lee, E. et al. (2021).
Classification of Goods Using Text Descriptions With Sentences Retrieval.
arXiv:2111.01663.
DOI-form identifier may be rendered as 10.48550/arXiv.2111.01663 if desired.

Lee, E.; Kim, S.; Kim, S.; Jung, S.; Kim, H.; Cha, M. (2023).
Explainable Product Classification for Customs.
arXiv:2311.10922.
DOI-form identifier: 10.48550/arXiv.2311.10922.

Marra de Artiñano, I.; Riottini Depetris, F.; Volpe Martincus, C. (2023).
Automatic Product Classification in International Trade:
Machine Learning and Large Language Models.
Inter-American Development Bank working paper.
DOI 10.18235/0005012.

Wang, S.; Tan, W.; Chen, L. (2026).
Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained
Classification.
arXiv:2607.10588.

Nguyen, T.T.H.; Nguyen, K.V.Q.; Cao, H.-L.; Duong, T.; Ho, P.; Pham, V.;
Nguyen, L.; Cao, H. (2026).
Consensus-based Agentic Large Language Model Framework for Harmonized Tariff
Schedule Code Classification.
arXiv:2606.16987.
```

For Marra de Artiñano et al., a later journal version exists, but it materially updates the evaluated LLM set and publication year. The 2023 working-paper identity should therefore be retained for the claims currently attributed to the 2023 source unless the manuscript claim is separately re-audited against the journal version.

### 4.4 General-method references without mandatory DOI

```text
Lewis, P. et al. (2020).
Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
Advances in Neural Information Processing Systems 33.

Pineau, J.; Vincent-Lamarre, P.; Sinha, K.; Larivière, V.; Beygelzimer, A.;
d'Alché-Buc, F.; Fox, E.; Larochelle, H. (2021).
Improving Reproducibility in Machine Learning Research
(A Report from the NeurIPS 2019 Reproducibility Program).
Journal of Machine Learning Research 22(164), 1-20.
```

## 5. Lee et al. publication-year decision

The manuscript currently cites **Lee et al. (2023)** for `Explainable Product Classification for Customs`.

Two valid identities exist:

```text
PREPRINT =
CoRR / arXiv:2311.10922 (2023)

FINAL_JOURNAL =
ACM Transactions on Intelligent Systems and Technology
15(2), Article 25, 1-24 (2024)
DOI 10.1145/3635158
```

The scientific content used by V038 is already bound to the analyzed preprint lineage. To avoid an unnecessary claim-level re-audit, FAST-F02 may preserve the **2023 preprint citation** exactly.

Recommended FAST-F02 choice:

```text
LEE_EXPLAINABLE_CUSTOMS_REFERENCE =
PRESERVE_2023_PREPRINT_IDENTITY
```

No in-text year change is required.

## 6. Citation-to-reference bijection disposition

```text
UNIQUE_ENGLISH_BODY_CITATIONS = 25
TARGET_REFERENCE_ENTRIES = 25
ORPHAN_REFERENCE_ENTRIES_ALLOWED = 0
UNRESOLVED_CITED_WORKS = 0
REFERENCE_LIST_ASSEMBLY = READY_FOR_WRITING_AI
```

Writing AI must still run a final machine check after inserting the list, because formatting can introduce omissions or duplicates.

## 7. Supplementary audit

The exact supplementary inventory is frozen separately in:

`article/manifests/FAST_F02_SUPPLEMENTARY_ASSEMBLY_V01.md`

The inventory contains seven canonical G5 supplementary tables and two approved G6 supplementary figures, with exact Git blob identities and interpretive constraints.

```text
SUPPLEMENTARY_SOURCE_INVENTORY = COMPLETE
SUPPLEMENTARY_PACKAGE = READY_FOR_WRITING_AI
NEW_SCIENTIFIC_CALCULATION = NOT_REQUIRED
```

## 8. Author facts received

Recorded in:

`article/forms/FAST_F02_AUTHOR_INPUT_PACKET_FILLED_V01.md`

Received:

```text
AUTHOR_FULL_NAME = Vladimir Molleapasa Gutierrez
AFFILIATION = Universidad Nacional Mayor de San Marcos
ORCID = 0009-0000-1086-7255
EMAIL = vladimir.molleapasa@unmsm.edu.pe
FUNDING = SELF_FUNDED / NO_SPECIFIC_GRANT_STATED
```

Universidad Nacional Mayor de San Marcos is treated as affiliation only, not as a funding body.

## 9. Remaining blockers

Only five factual declarations remain author-owned:

```text
B1_CORRESPONDING_AUTHOR_CONFIRMATION
B2_CREDIT_ROLES
B3_COMPETING_INTERESTS
B4_ACKNOWLEDGEMENTS
B5_AI_DISCLOSURE_CURRENT_TEXT_CONFIRMATION
```

No further Gestora literature, reference, reproducibility or supplementary research is required before Prompt 18 can be prepared.

## 10. Stop condition

```text
GESTORA_LANE_B = COMPLETE
FAST_F02_AUTHOR_INPUT = PARTIAL
FAST_F02_PROMPT = NOT_YET_AUTHORIZED

NEXT_ACTOR = AUTHOR
NEXT_ACTION = PROVIDE_B1_TO_B5_ONLY
EXPECTED_NEXT_AFTER_AUTHOR_INPUT =
GESTORA_VERSIONS_AND_AUDITS_SINGLE_FAST_F02_WRITING_PROMPT
```
