# G3-F01 Analytical Contract v0.1

## Status and binding

This document freezes the prospective analytical contract for G3-F01. It is a
contract of hypotheses, evidence families, source bindings, estimands, and
procedures. It contains no new scientific calculation and does not decide HE2
or HE5.

```text
prompt = PROMPT76
prompt_source_commit = 409dd7b7302bce1d41cc69e24b9debe3db05982e
scientific_main_commit = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
canonical_plan_commit = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
article_commit = 254b1e6df736fa9938ac86a515d65b36f4d361c5
fichas_snapshot_commit = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
ficha_path = docs/fichas/grupos_3_8/grupo_3/G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
ficha_blob = 4208e70a464e2a645644e9f9c5289cd7333afe48
```

The source transcription used for the literal hypotheses is:

```text
SRC01_ORIGINAL = Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf
SRC01_ACCESS_MODE = AUTHOR_APPROVED_FROZEN_TRANSCRIPTION_IN_GITHUB
SRC01_DIRECT_PDF_BYTES_READ_BY_CODEX = false
SRC01_TRANSCRIPTION_STATUS = APPROVED / FROZEN / INDEPENDENTLY_VERIFIED_BY_IA_EXPERIMENTAL
```

The exact frozen statements are:

```text
HE2 = La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.

HE5 = Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.
```

The accented forms in the approved transcription are preserved in the JSON
binding as UTF-8 exact text. The statements remain undecided in this contract.

## Hypothesis decomposition

HE2 is decomposed into two non-interchangeable propositions:

- HE2_A: historical early-ranking superiority against normative retrieval.
- HE2_B: deeper documentary coverage from normative hierarchical and expanded-candidate variants.

Early ranking is evaluated with the common benchmark and aligned Top-k/MRR
definitions. Deep coverage is evaluated with deeper recall or coverage
positions. A deeper coverage increase is not evidence of early-ranking
superiority.

HE5 is decomposed into five components:

- ambiguous or incomplete descriptions;
- hierarchically proximate subheadings;
- insufficient historical precedents;
- internal-evaluation validity limits;
- explanation and evidence-auditability limits.

## Evidence-family contract

The authoritative machine-readable matrix is
`outputs/analysis/group3/g3_analytical_contract_v0.1.json`. Its 13 families
use only the terminal labels `ELIGIBLE`, `DESCRIPTIVE_ONLY`,
`NOT_ESTIMABLE`, and `NOT_APPLICABLE`.

### Primary sources and scope

The primary bindings are the frozen Group 1 and Group 2B artifacts in
`main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f`. Compatibility artifacts
must match the benchmark v0.2 EVAL identity; the superseded 3,000/1,006 split
is excluded. The following scope rules are binding:

- EXP11A is sensitivity only. Its H25/H50/H75/H100 conditions are independent
  complete-DAM conditions with size and composition coupled. H50 D1/D2 are
  paired strata. No isolated causal historical-bank-size effect is authorized.
- EXP11B is H150/H200 historical-size sensitivity. The ten approved H150 and
  ten approved H200 runs are paired by seed; the common seed set must be
  identified before any future comparison. No isolated causal size claim is
  authorized.
- 0B-05C uses only the corrected Attempt06 outputs. Superseded attempts and
  uncorrected outputs are not current evidence.
- EXP12 is closed at its original design disposition. Retrieval was not
  executed, D-HIGH/D-MID/D-LOW were not selected, and a diversity effect is
  not estimable.
- HE5 evidence with a diagnostic sample or a qualitative sample is not
  extrapolated to the complete evaluation population.

## Prospective procedures

For eligible families, the primary unit and estimand are fixed before looking
at any future result. Paired comparisons use the same case identifiers and
aligned metric definitions. Dependence within a DAM is handled by aggregating
case-level contributions within DAM before uncertainty estimation; series from
the same DAM are never treated as independent clusters.

The default future uncertainty procedure for an eligible paired family is a
two-sided DAM-cluster bootstrap with 10,000 resamples, fixed seed 20263001,
percentile 95% interval, and the pre-specified estimand stated by the family.
Where a family declares no inferential target, the output is descriptive only
and no interval is produced. Multiplicity is controlled separately within the
HE2 family by Holm adjustment across its pre-specified primary metric tests;
HE5 component descriptions are not converted into a multiple-testing claim.
No p-value, interval, effect size, or test is calculated by Prompt76.

## Frozen limitations

The contract does not select procedures based on an observed result, does not
change thresholds, seeds, populations, exclusions, tokenization, retrieval,
or ranking definitions, and does not reopen EXP12. HE2 and HE5 remain
undecided. G3-F02 remains unstarted.

## Audit state

```text
INFERENTIAL_CALCULATION_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
SCIENTIFIC_EXPERIMENT_REEXECUTED = false
EXP12_REOPENED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
EXTERNAL_AUDIT_REQUIRED = true
```
