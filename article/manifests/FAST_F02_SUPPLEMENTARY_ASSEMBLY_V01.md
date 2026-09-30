# FAST-F02 Supplementary Assembly Manifest V01

## Status

```text
PHASE = FAST_FINALIZATION / FAST_F02
PURPOSE = GOVERNED_SUPPLEMENTARY_ASSEMBLY
CANONICAL_ARTICLE_BASELINE = ARTICLE_MASTER_V038
SCIENTIFIC_RECOMPUTATION = FORBIDDEN
NEW_INFERENCE = FORBIDDEN
```

## 1. Governing disposition

Experimental G7-F03 and the subsequent focused re-audit disposed the following scientific presentations to Supplementary / Appendix:

- G5-SECONDARY-01
- G5-SECONDARY-02
- G5-APPENDIX-01
- G5-APPENDIX-02
- G5-APPENDIX-03
- G5-APPENDIX-04
- G5-APPENDIX-05
- G6-FIG-02
- G6-FIG-03

The two G5 main tables and G6-FIG-01 have already been integrated into the main body by FAST-F01 and must not be duplicated here.

## 2. Canonical supplementary tables

| Supplement ID | Role | Canonical CSV | Git blob | Governing qualification |
|---|---|---|---|---|
| G5-SECONDARY-01 | Phase E descriptive coverage | `outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv` | `fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61` | descriptive only; no CI; no confirmatory role |
| G5-SECONDARY-02 | HE5 descriptive components | `outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv` | `727076a0d09735a87f45f6522d2a0ecead2cee17` | HE5 remains INCONCLUSIVE; no post-hoc concentration threshold |
| G5-APPENDIX-01 | Top-50 supplementary uncertainty | `outputs/results/group5/tables/g5_appendix_01_top50_supplementary.csv` | `c2ded734af9ea340d715483b6e8cc00a7536dfea` | supplementary only; no HE2 decision role |
| G5-APPENDIX-02 | EXP11A size-composition sensitivity | `outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv` | `cf3aedab5935d6af9b3ac7be7b51b954fcb9c403` | descriptive/noncausal; size and composition vary jointly |
| G5-APPENDIX-03 | EXP11B H150/H200 sensitivity | `outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv` | `76c8c6c588c7e809c6be64f7192f497c491fb692` | ten observed paired seeds; no seed-superpopulation inference |
| G5-APPENDIX-04 | 0B-05C Attempt06 corrective sensitivity | `outputs/results/group5/tables/g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv` | `490ef570fa1674e2eecad7f0a3cdf34ba96204db` | corrected Attempt06 only; method-dependent; descriptive |
| G5-APPENDIX-05 | Phase E diagnostic-union ceiling | `outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv` | `f43cce08d1d7bc3cef64698dbebf14eae4b26ed5` | diagnostic ceiling only; not production/confirmatory performance |

Governing registry:

`outputs/results/group5/g5_table_registry_v0.1.json`

Git blob:

`4fe9318d52fad093066ff9f42d524fc95e436245`

## 3. Canonical supplementary figures

### G6-FIG-02 — Phase E descriptive coverage

```text
SVG =
figures/group6/g6_fig_02_phase_e.svg
GIT_BLOB =
ec164ea41ab8605edf198c03785db63c442c1b64

PNG =
figures/group6/g6_fig_02_phase_e.png
GIT_BLOB =
7917314c8fc54dd96dd9ddfb28c9927c9a577c76

SOURCE_TABLE =
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
SOURCE_TABLE_GIT_BLOB =
fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61

ROLE =
DESCRIPTIVE_SUPPLEMENTARY
```

Required interpretation:

- four formal `A_historical_defined` variants plus 70/30 as context;
- no CI;
- no p-values;
- no inferential ranking between variants;
- diagnostic union excluded from ordinary performance.

### G6-FIG-03 — EXP11A joint size-composition sensitivity

```text
SVG =
figures/group6/g6_fig_03_exp11a.svg
GIT_BLOB =
1b2aca9aa9c2582cf0b7e16850cd5b22387cc771

PNG =
figures/group6/g6_fig_03_exp11a.png
GIT_BLOB =
eaf59497ee49ab36d34d23e42cf002111bc9fe3e

SOURCE_TABLE =
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
SOURCE_TABLE_GIT_BLOB =
cf3aedab5935d6af9b3ac7be7b51b954fcb9c403

ROLE =
DESCRIPTIVE_SENSITIVITY / NONCAUSAL
```

Required interpretation:

- 31 observed runs;
- H25 / H50-D1 / H50-D2 / H75 / H100 reference;
- H100 is one frozen reference, not a replicate distribution;
- no CI, p-values, regression, smoothing, or new summary statistic;
- no isolated or monotonic causal size-effect interpretation.

Governing caption registry:

`docs/figures/group6/g6_caption_registry_v0.1.md`

Git blob:

`0dcb43cfa56dfce2e6955f960184069beb36ba76`

## 4. Assembly design

FAST-F02 should create **one compact Supplementary Material package** with this order:

```text
Supplementary Methods / reading note (minimal)
S1 — Phase E descriptive coverage table
S2 — HE5 descriptive components table
S3 — Top-50 supplementary uncertainty
S4 — EXP11A joint size-composition sensitivity table
S5 — EXP11B H150/H200 paired sensitivity
S6 — 0B-05C Attempt06 corrective sensitivity
S7 — Phase E diagnostic-union ceiling
Figure S1 — G6-FIG-02
Figure S2 — G6-FIG-03
```

The ordering is editorial only and does not change scientific priority.

## 5. Formatting policy

For publication-facing supplementary display:

- retain all canonical rows;
- preserve exact denominators and inferential/descriptive roles;
- ordinary display rounding may follow the main-manuscript FAST-F01 convention when necessary for readability, while exact source values remain in the traceability record;
- do not derive any new statistic;
- do not alter G6 figure content;
- captions may be translated to English publication-facing wording and mirrored in Spanish only for the internal bilingual master.

## 6. Article-side Supplementary statement

The article's End Matter may state that supplementary material accompanies the article only after the package is actually materialized.

Do not leave a meaningless `None` placeholder once the package exists.

## 7. Gate

```text
SUPPLEMENTARY_SOURCE_INVENTORY = COMPLETE
SUPPLEMENTARY_ASSEMBLY = READY_FOR_WRITING_AI
SCIENTIFIC_REAUDIT_REQUIRED = NO_BY_DEFAULT
FAST_F02_WRITING_EXECUTION = NOT_YET_AUTHORIZED
```
