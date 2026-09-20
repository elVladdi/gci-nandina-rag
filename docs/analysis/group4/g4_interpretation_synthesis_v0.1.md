# G4-F02 Integrated Interpretation and Limitations v0.1

```text
ARTIFACT_ID = G4_F02_INTERPRETATION_SYNTHESIS_v0.1
STATUS = CANDIDATE_PENDING_EXTERNAL_AUDIT
FICHA = G4-F02
SCIENTIFIC_MAIN = 9f549ebdf940f9d806d5088697394d0c927f9fdc
PROMPT89 = d9494b356cd00fcd97b8b338896df6e88aa279ac
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

This is an analytical governance artifact. It is not article-ready prose, does not add science, and does not contrast the approved evidence with literature.

## 1. Scope and evidence boundary

### G4F02-S001

- Classification: `FINDING`
- Trace: `G3C-014`, `G4F01-0014`, `G3F02-0544`, `G3F02-0545`
- Statement: The empirical boundary is the offline internal Chapter 87 benchmark of 1,056 series, 67 DAM, and 42 NANDINA.
- Qualification: No external validation was performed.
- Forbidden use: Do not assert validity for other chapters, customs administrations, countries, or production settings.

### G4F02-S002

- Classification: `FINDING`
- Trace: `G3C-015`, `G3C-016`, `G3C-017`, `G3C-018`, `G4F01-0015:G4F01-0018`
- Statement: Historical ranking, normative evidence retrieval, and controlled explanation are separate governed functions.
- Qualification: Retrieval performance is not end-to-end RAG accuracy; normative evidence is not a binding legal ruling; an auditable explanation does not validate classification or legal correctness.
- Forbidden use: Do not treat the local LLM as a classifier from scratch or as a replacement for ranking.

## 2. Approved findings

### G4F02-F001

- Classification: `FINDING`
- Trace: `G3C-001:G3C-003`, `G4F01-0001:G4F01-0003`, `G3F03-0001:G3F03-0015`
- Statement: Historical retrieval is superior to corrected flat normative, corrected hierarchical normative, and corrected D1a retrieval for all five primary early-ranking metrics under the frozen HE2_A rules.
- Qualification: The contrasts are noncausal and use cluster-resampling uncertainty within the fixed internal benchmark; D1a refers only to corrected Attempt06.
- Forbidden use: Do not infer global RAG accuracy, legal correctness, causal superiority, or external-population generalization.

### G4F02-F002

- Classification: `FINDING`
- Trace: `G3C-004`, `G4F01-0004`, `G3F03-0016`, `G3F02-0037`, `G3F02-0038`
- Statement: Corrected hierarchical coverage increases from Recall@100 to Recall@200 under the frozen HE2_B primary contrast.
- Qualification: This is one primary contrast; Pool@200 is not a second confirmatory contrast.
- Forbidden use: Do not duplicate Pool@200 as independent evidence.

### G4F02-F003

- Classification: `FINDING`
- Trace: `G3C-005`, `G4F01-0005`, `G3F02-0040:G3F02-0084`
- Statement: The four frozen A_historical_defined Phase E variants show descriptively increasing exact-NANDINA pool coverage at depths 50, 100, and 200.
- Qualification: This pattern is descriptive; no interval, p-value, or inferential contrast was authorized for it.
- Forbidden use: Do not promote Phase E to confirmatory inference.

### G4F02-F004

- Classification: `FINDING`
- Trace: `G3C-006`, `G4F01-0006`, `G3F03-0017:G3F03-0019`
- Statement: Top-50 uncertainty is supplementary and has no role in the HE2 decision.
- Qualification: Top-50 lies outside the five primary Bonferroni metric families.
- Forbidden use: Do not use Top-50 to change `HE2 = SUPPORTED`.

## 3. Historical-bank sensitivity: EXP11A and EXP11B

### G4F02-F005

- Classification: `FINDING`
- Trace: `G3C-007`, `G4F01-0007`, `G3F02-0112:G3F02-0333`, `G2B-L05`
- Statement: EXP11A measures joint bank-size/composition sensitivity across H25, H50, H75, and the frozen H100 reference.
- Qualification: Bank size and natural composition vary together; the design is noncausal.
- Forbidden use: Do not claim an isolated or monotonic causal effect of bank size.

### G4F02-P001

- Classification: `PLAUSIBLE_EXPLANATION`
- Trace: `G3C-007`, `G4F01-0007`
- Statement: Differences observed across EXP11A conditions may be consistent with the combined influence of bank size and natural composition.
- Qualification: `CAUSAL_STATUS = NOT_ESTABLISHED`; the design does not separate those influences.
- Forbidden use: Do not attribute an observed change to size alone.

### G4F02-F006

- Classification: `FINDING`
- Trace: `G3C-008`, `G4F01-0008`, `G3F02-0334:G3F02-0465`, `G2B-L07`, `G2B-L08`
- Statement: EXP11B provides descriptive paired H150/H200 sensitivity for ten accepted seed pairs on the same 1,056-series EVAL set.
- Qualification: The ten seeds do not define a frozen statistical superpopulation, and `10 x 1056` are not independent observations.
- Forbidden use: Do not report inferential generalization beyond the observed H150/H200 conditions.

### G4F02-X001

- Classification: `SPECULATION_NOT_SUPPORTED`
- Trace: `G3C-008`, `G4F01-0008`
- Statement: A seed-superpopulation effect or an independent-case effect for EXP11B is not supported by the frozen design.
- Qualification: `DOWNSTREAM_USE = PROHIBITED_AS_EMPIRICAL_CLAIM`.
- Forbidden use: Do not infer population-level seed behavior from the ten accepted pairs.

## 4. Corrective numerical state: 0B-05C Attempt06

### G4F02-F007

- Classification: `FINDING`
- Trace: `G3C-009`, `G4F01-0009`, `G3F02-0466:G3F02-0527`
- Statement: Attempt06 is the current corrected state: EV03 has zero aggregate change, EV04 has a tiny nonzero MRR decrease only, and D1a has a positive nonzero exact-ranking change with a minor mixed HS4 effect.
- Qualification: `0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A`; Attempts01-05 are superseded for current interpretation.
- Forbidden use: Do not summarize 0B-05C globally as having no numerical impact.

### G4F02-P002

- Classification: `PLAUSIBLE_EXPLANATION`
- Trace: `G3C-009`, `G4F01-0009`
- Statement: The different arm-level responses may be consistent with method-dependent sensitivity to the correction.
- Qualification: `CAUSAL_STATUS = NOT_ESTABLISHED`; this is an interpretation of the approved descriptive pattern, not a newly identified mechanism.
- Forbidden use: Do not claim a causal mechanism for the arm differences.

## 5. Negative / non-estimable evidence: HE5 and EXP12

### G4F02-F008

- Classification: `FINDING`
- Trace: `G3C-010:G3C-014`, `G4F01-0010:G4F01-0014`, `G3F02-0528:G3F02-0548`
- Statement: `HE5 = INCONCLUSIVE` because description quality was not operationalized as a prevalence estimand, hierarchical proximity remains descriptive without a frozen concentration threshold, historical support retains literal `1 DAM`, `2 DAM`, `3-4 DAM`, and `5+ DAM` buckets without an insufficiency threshold, and the empirical scope is internal and offline.
- Qualification: Absence of estimability is neither positive nor negative evidence for HE5.
- Forbidden use: Do not create post-hoc text-quality rules, concentration thresholds, or insufficient-support labels.

### G4F02-F009

- Classification: `FINDING`
- Trace: `G3C-010`, `G4F01-0010`, `G3F02-0548`, `G2B-L10`, `G2B-L11`
- Statement: EXP12 is `CLOSED_WITHOUT_RETRIEVAL`; its frozen planning search did not produce the minimum number of unique feasible conditions, so D-HIGH, D-MID, and D-LOW were not selected and diversity effect is not estimable.
- Qualification: The result is limited to the frozen search, seed, thresholds, coverage, volume, and TVD contract; the forensic diagnostic is non-governing.
- Forbidden use: Do not assert global mathematical infeasibility, characterize unexecuted seeds, reopen the design, or use EXP12 as evidence for or against HE5.

### G4F02-X002

- Classification: `SPECULATION_NOT_SUPPORTED`
- Trace: `G3C-010`, `G4F01-0010`
- Statement: Claims about whether an alternative EXP12 design, seed, or threshold would succeed are not supported by the executed evidence.
- Qualification: `DOWNSTREAM_USE = PROHIBITED_AS_EMPIRICAL_CLAIM`.
- Forbidden use: Do not present hypothetical alternatives as observed results or recommendations.

## 6. Finding / plausible explanation / speculation register

| statement_ids | category | downstream status |
|---|---|---|
| G4F02-S001:S002, G4F02-F001:F009 | FINDING | Permitted only with the stated trace and qualifications |
| G4F02-P001:P002 | PLAUSIBLE_EXPLANATION | Conditional language required; `CAUSAL_STATUS = NOT_ESTABLISHED` |
| G4F02-X001:X002 | SPECULATION_NOT_SUPPORTED | `DOWNSTREAM_USE = PROHIBITED_AS_EMPIRICAL_CLAIM` |

No substantive statement in this synthesis is outside these three categories.

## 7. Reproducibility and traceability limitations from Group2B

### G4F02-F010

- Classification: `FINDING`
- Trace: `G2B-L01:G2B-L11`, canonical Plan state at `2237ddc46bc1c7bfac203753bdcf2c7d4592f83e`
- Statement: Group2B is `CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS`, with zero blocking gaps and 11 distinct nonblocking limitations listed below.
- Qualification: The classification `FINDING` applies to every controlled row in this table; historical candidate-state fields inside the source artifacts do not override the canonical state, and Group2B is not described as perfectly reproducible.
- Forbidden use: Do not promote a nonblocking declared limitation to a blocking gap without new governed evidence.

| limitation_id | controlled limitation | role in G4-F02 |
|---|---|---|
| G2B-L01 | Incomplete historical environment | Qualifies historical reproducibility without invalidating approved results |
| G2B-L02 | Unrecoverable historical EXP04-C runner | Declares an irreversible historical traceability boundary |
| G2B-L03 | Unrecoverable EXP08 v0.1 metadata | Declares an irreversible historical metadata boundary |
| G2B-L04 | Non-byte-exact LLM evaluation | Prevents claims of byte-identical AI evaluation replay |
| G2B-L05 | EXP11A size/composition coupling | Prohibits isolated causal size claims |
| G2B-L06 | User-attested NUEVA_02 acquisition | Qualifies source acquisition provenance |
| G2B-L07 | Local-only EXP11B banks and candidate ranking | Preserves SHA/size-bound local-only status; it does not mean missing or invalid |
| G2B-L08 | Portability runtime not independently rerun by external auditor | Qualifies the external audit scope |
| G2B-L09 | Local-only D1a weights | Preserves hash/size-bound local-only model status |
| G2B-L10 | Failed one-shot EXP12 planning outcome | Records the fail-closed planning boundary |
| G2B-L11 | Non-governing EXP12 forensic diagnostic | Prevents promotion of the diagnostic to a design decision |

## 8. Integrated limitations for downstream writing

### G4F02-F011

- Classification: `FINDING`
- Trace: `G2B-L01:G2B-L11`, `G3C-007:G3C-018`
- Statement: Downstream writing must jointly preserve reproducibility boundaries, noncausal sensitivity scope, Attempt06 currency, EXP12 non-estimability, the internal benchmark boundary, and architectural separation.
- Qualification: Declared limitations constrain claim strength but do not retrospectively invalidate approved evidence.
- Forbidden use: Do not convert `HASH_BOUND_LOCAL_ONLY` to missing, unverified, invalid, or unreproducible; do not convert `DECLARED_NOT_RECOVERABLE` into experimental error.

## 9. Forbidden interpretations / overclaims

### G4F02-X003

- Classification: `SPECULATION_NOT_SUPPORTED`
- Trace: `G3C-001:G3C-018`, `G4F01-0001:G4F01-0018`
- Statement: Causal superiority, external validity, end-to-end RAG accuracy, binding legal correctness, explanation-as-validation, isolated EXP11A size effects, EXP11B superpopulation inference, globally zero 0B-05C impact, global EXP12 infeasibility, and any HE5 decision beyond `INCONCLUSIVE` are unsupported.
- Qualification: `DOWNSTREAM_USE = PROHIBITED_AS_EMPIRICAL_CLAIM`.
- Forbidden use: Do not include any of these propositions as findings.

## 10. Handoff boundary to G4-F03

### G4F02-S003

- Classification: `FINDING`
- Trace: `G4-F03_CONTRACT`
- Statement: G4-F03 remains `PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED`; no literature search, citation comparison, compatibility judgment, or literature-based discussion point was produced here.
- Qualification: Any later literature contrast must use its own prospective authorization and preserve the controlled evidence boundary.
- Forbidden use: Do not treat this artifact as Group4 closure or article prose.
