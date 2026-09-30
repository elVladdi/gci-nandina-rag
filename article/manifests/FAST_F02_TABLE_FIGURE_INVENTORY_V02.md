# FAST-F02 Table/Figure Inventory V02

## Status

```text
PHASE = FAST_FINALIZATION / FAST_F02_CORRECTIVE_PRESENTATION
SOURCE_COMMIT = 584cf533ff8a01c26794e5811b2b20e23438c192
AUTHORIZATION = D-212
PROMPT_GIT_BLOB = 19f205ed87f7ce67ba6fe22e3d93c6fea3907ef7

MAIN_TABLE_COUNT = 7
MAIN_FIGURE_COUNT = 4
SUPPLEMENTARY_TABLE_COUNT = 7
SUPPLEMENTARY_FIGURE_COUNT = 1

NEW_SCIENTIFIC_CONTENT = NO
```

## Main publication table inventory

| Table | Disposition | Scientific role | Frozen source / identity |
|---|---|---|---|
| Table 1 | Retained unchanged | Experimental benchmark and evaluation overview | FAST-F02 V01 / FAST-F01 V02 inherited |
| Table 2 | Created | Observed candidate-retrieval performance | Exact frozen observed values fixed by Prompt 19 |
| Table 3 | Restructured | HE2_A paired Historical-minus-comparator contrasts | `outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv` @ `cb68583ee2260e4455796bac99ad90995ca7ef92` |
| Table 4 | Retained and renumbered | HE2_B deep-coverage contrast | `outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv` @ `359e4e19b5ef1d44983c03039162209293b2a44c` |
| Table 5 | Created | Documentary association and ranking invariance | `docs/exp04_phase_f_historical_normative_integration_v02_results.md` @ `01a4573d34c029efb0b055c7b90202842e914549` |
| Table 6 | Created | Controlled-explanation evaluation summary | metrics @ `843e1edd17a023f6c3d6f0b5235dd3fba86369c1`; warning comparison @ `1cab0e8e7398a7299086fec7ad1ec28b2f706f2d` |
| Table 7 | Created | Historical-bank sensitivity summary | EXP11A @ `cf3aedab5935d6af9b3ac7be7b51b954fcb9c403`; EXP11B @ `76c8c6c588c7e809c6be64f7192f497c491fb692` |

## Main publication figure inventory

| Figure | Disposition | Scientific role | Frozen source / identity |
|---|---|---|---|
| Figure 1 | Retained unchanged | Architecture and authority boundaries | Inherited FAST-F02 V01 image; byte-preserved media |
| Figure 2 | Created from frozen means | Descriptive qualitative explanation profile | `he4_qualitative_dimension_metrics_v0.2.csv` @ `c119cc8d05148ad893d7c7687b9f4495c24fc49b` |
| Figure 3 | Promoted from Supplementary | EXP11A joint size-composition sensitivity | G6-FIG-03 SVG @ `1b2aca9aa9c2582cf0b7e16850cd5b22387cc771`; exact inherited FAST-F02 V01 Supplementary presentation render reused |
| Figure 4 | Retained and renumbered | Primary HE2 evidence | Existing G6-FIG-01 scientific image byte-preserved |

Figure 2 frozen means:

```text
Traceability = 2.00
Verifiability = 0.54
Historical-normative evidence separation = 1.04
Conclusion prudence = 1.78
Fixed-Top-3 consistency = 1.96
Detection of generic normative evidence = 1.68
Candidate comparison = 1.46
Utility for human audit = 1.26
```

## Supplementary inventory

```text
TABLES S1-S7 = UNCHANGED
FIGURE S1 = G6-FIG-02 / UNCHANGED
FORMER FIGURE S2 = REMOVED_FROM_SUPPLEMENTARY / PROMOTED_TO_MAIN_FIGURE_3
```

All seven Supplementary tables retain their complete canonical row sets. The V02 Supplementary DOCX contains seven native tables and one drawing. The unused OOXML relationship/media object for former Figure S2 was removed after promotion, so the Supplementary package does not retain a hidden duplicate.

## Presentation compaction

```text
FULL_NUMERIC_VECTOR_DUPLICATION_IN_PROSE = NONE
SECTION_5_2 = TABLES_2_TO_4 + CONCISE_INTERPRETATION
SECTION_5_3 = TABLE_5 + CONCISE_INTERPRETATION
SECTION_5_4 = TABLE_6 + FIGURE_2 + CONCISE_INTERPRETATION
SECTION_5_5 = TABLE_7 + FIGURE_3 + SUPPLEMENTARY_S2_S6_POINTERS
SECTION_5_6 = INFERENTIAL_SYNTHESIS + FIGURE_4
```

No additional visual object was introduced in Sections 5.7, Discussion, or Conclusion.

## Materialized output identities

```text
CORRECTION_SECTION_GIT_BLOB = e189efd6a51bd652c10ffeea078f8a15ef615f5f
FIGURE_2_SVG_GIT_BLOB = 293298c3f1b9f987ef5f7c07c90bbfebdca5eb50
SUPPLEMENTARY_V02_MD_GIT_BLOB = da7125d1ca7f89b7009ed05f8a8d088a6a0235af

CANDIDATE_MD_SHA256 = 351fbd5a981f3c430b8debfa5fa360c4e079301e7591c653908a8061cffb28ef
CANDIDATE_MD_EXPECTED_GIT_BLOB = 7ac057a2d0b92322757c3da2b9fc36fa8b66db4c
CANDIDATE_DOCX_SHA256 = 489f0f1df62fa0d661efd601b8155a4416db7a95a6cb45636552c3bb7b6d8524
CANDIDATE_DOCX_SIZE_BYTES = 605152

SUPPLEMENTARY_MD_SHA256 = f9e5eaedf7a0e6ee797681612118e8bda8fb42c5d613ad50644b204bebbd023b
SUPPLEMENTARY_MD_GIT_BLOB = da7125d1ca7f89b7009ed05f8a8d088a6a0235af
SUPPLEMENTARY_DOCX_SHA256 = 0a84da58dd1b55e2824dd28b9105a17ae050dfcc8245c26a5e0c71c8255a909c
SUPPLEMENTARY_DOCX_SIZE_BYTES = 122133

FIGURE_2_PNG_SHA256 = a47669390563206cb20ac2adac3622271008fba4fb06ded9be703da53c6b4b77
FIGURE_2_SVG_SHA256 = 79d4ed3ed3234ba5452fee1bf18f3ff1e75085c8f69ebd6ccb195f9f8e785940
```

## Word structural inventory

The cumulative Word is the bilingual internal master. Therefore its raw OOXML table count is not the same concept as the seven publication table identities.

```text
MAIN_PUBLICATION_TABLE_IDENTITIES = 7
MAIN_DOCX_RAW_TABLE_ELEMENTS = 16
MAIN_DOCX_PUBLICATION_TABLE_INSTANCES_EN_ES = 14
MAIN_DOCX_INHERITED_INTERNAL_TABLE_ELEMENTS = 2

MAIN_DOCX_DRAWING_COUNT = 6
MAIN_PUBLICATION_FIGURE_IDENTITIES = 4

COMMENTS = 48
TRACKED_CHANGES = 0
COMMENTS_XML_BYTE_IDENTICAL_TO_FAST_F02_V01 = PASS

SUPPLEMENTARY_DOCX_TABLE_COUNT = 7
SUPPLEMENTARY_DOCX_DRAWING_COUNT = 1
SUPPLEMENTARY_TRACKED_CHANGES = 0
```

The six main-document drawings comprise the inherited bilingual architecture and HE2 placements plus the new Figure 2 and promoted Figure 3 presentation placements; publication-facing figure identity remains exactly four.

## Scientific boundary

```text
NEW_EXPERIMENT = NO
NEW_METRIC = NO
NEW_CI = NO
NEW_P_VALUE = NO
NEW_INFERENTIAL_TEST = NO
NEW_HYPOTHESIS_DISPOSITION = NO
NEW_LITERATURE = NO
NEW_REFERENCE = NO
NEW_CLAIM = NO
```
