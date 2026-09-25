# G7-F01 — Writing source freeze v0.1

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G7-F01
group = 7
main_source_commit = e93b44164a9619dad1f527a3b2d4479265858e39
fichas_base = bed229d81b2ce3258e1ac3c9efc171458e2891aa
plan_base = cc9a47986dfbae138738ad9945f0c0b1859b9f4f
group6 = CLOSED / APPROVED
group7 = IN_PROGRESS / NOT_CLOSED
g7_f02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
g7_f03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
external_audit = PENDING
```

This is a source and writing-action contract, not thesis or article prose. The companion JSON is the machine-readable registry: it lists each scientific source with its exact `main` blob and role, all eight article-control blobs, each hypothesis binding, and the full per-topic writing matrices. No result or hypothesis is recalculated here.

## Source precedence

1. Approved project formulations govern the wording of problem, objectives and hypotheses. The current thesis is a correction baseline, not scientific ground truth.
2. The current Plan and frozen experimental artifacts govern methods, status and results. G3 supersedes Group1's historical HE2/HE5 labels. G3 inference and G5 canonical tables govern any number presented; G4 governs claim strength and literature contrast; G6 governs figures and captions.
3. The Group1 EXP-04 hypothesis registry governs HE3 and HE4, with F/G and J/K as component evidence. Group1 explicitly reports no consolidated OE1/HE1 assessment. No terminal aggregate HG disposition was located.
4. `article/ARTICLE_STATUS.md` and the other article controls govern editorial permissions, never scientific truth. G7-F01 does not override them.
5. PREF003 (`27d1ed8a54bc661485a6f38ac77a3d9ef0775e58`) and PREF004 (`693d43a0c7f87627de744a016f07c736a3160b1c`) are non-governing location/traceability aids. Their conclusions were checked against the versioned primary sources in the JSON.

The source registry freezes 33 scientific paths at `main=e93b44164a9619dad1f527a3b2d4479265858e39`: eight G3, five G4, four G5, four G6, and twelve Group1/Group2 and hypothesis-component sources. All 33 paths resolved to the recorded Git blobs. Group6's closure records three figures and three captions, with G6-F01/F02/F03 and Group6 closed, approved, integrated. G3's current fixed evaluation is 1,056 series / 67 DAM / 42 NANDINA in an offline internal Chapter-87 benchmark. The unit of analysis is SERIE and DAM/declaration is the dependence group when applicable. No p-values were calculated.

## Thesis identity

The versioned manifest `preflight_tmp/THESIS_CURRENT_MASTER_MANIFEST_2026-09-22.md` has blob `42b89b512b8db818238bfd0da22a7c75c207d9f1`. It identifies the author-confirmed correction baseline `Molleapasa_gv(5).docx`, canonically `/Tesis San Marcos/tesis_vigente/Molleapasa_gv_vigente_2026-09-22.docx`, Library id `libfile_a4565dde90148191898d246f47c287e7`, SHA-256 `08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed`, 4,360,620 bytes and 129 parsed pages. `Molleapasa_gv(4).docx` is historical, not current. This is `CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED` and `THESIS_CORRECTION_BASELINE=true`, not a scientific ground truth or final approved thesis. The G7-F01 executor did not have the binary bytes and did not recalculate the SHA. Exact byte-hash recheck is required before any G7-F02 edit; an author-confirmed later master would require a new explicit identity freeze.

## Hypotheses

| Hypothesis | Frozen disposition | Governing evidence and writing boundary |
|---|---|---|
| HG | `NO_FORMAL_DISPOSITION_FOUND` | No terminal aggregate HG decision found. Describe component evidence separately; do not assert supported/rejected or derive HG from HE1–HE5. |
| HE1 | `NO_FORMAL_DISPOSITION_FOUND` | Group1 manifest explicitly says `NOT_FABRICATED_NO_CONSOLIDATED_ASSESSMENT_FOUND`. G2A/G2B reproducibility is evidence with limitations, not a HE1 decision. |
| HE2 | `SUPPORTED` | G3-F04 governs: 15 primary HE2_A paired DAM-cluster contrasts with frozen 99% CI and one HE2_B primary 95% CI. Phase E is descriptive only. |
| HE3 | `SUPPORTED` | Group1 registry plus F/G: historical ranking invariant in 1,056/1,056 cases; LLM reranker is diagnostic, not the main pipeline. |
| HE4 | `PARTIALLY_SUPPORTED` | Group1 registry plus J/K: structural Top-3/traceability 50/50, qualitative auditable 28/50. Preserve `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` and `EVALUATOR_MODALITY_DEVIATION`; no legal-correctness inference. |
| HE5 | `INCONCLUSIVE` | G3-F04 governs. Description quality was not operationalized; hierarchy and support remain descriptive. EXP12 has no estimable diversity effect. |

The approved literal hypothesis formulations must not be silently rewritten. A disposition update in future thesis writing is distinct from changing a formulation. The Group1 HE2/HE5 labels are historical and superseded by G3.

## Thesis writing contract for future G7-F02

The JSON provides the required eight columns for each of these 28 rows: `thesis_section_or_topic`, `baseline_state`, `writing_action`, `scientific_governing_source`, `claim_or_metric_rule`, `must_preserve`, `must_replace_or_remove`, and `blocking_if_source_missing`. This summary is an index, not permission to draft now.

| Topic | Future action | Governing source / decisive boundary |
|---|---|---|
| Problem and objectives | `KEEP_WITH_TERMINOLOGY_REVIEW` | Approved wording; G4 bounded scope |
| HG and HE1 | `VERIFY_BEFORE_WRITING` | No formal terminal disposition |
| HE2 and HE5 | `UPDATE_REQUIRED` | G3 `SUPPORTED` / `INCONCLUSIVE` |
| HE3 and HE4 | `UPDATE_REQUIRED` | Group1 `SUPPORTED` / `PARTIALLY_SUPPORTED` |
| Variables and operationalization | `UPDATE_REQUIRED` | G3 metric populations and DAM dependence |
| Design and analysis unit | `REWRITE_REQUIRED` | SERIE, DAM cluster, fixed internal benchmark |
| Population/sample/split | `REWRITE_REQUIRED` | H100 2950/28; DEV 100/6; EVAL 1056/67/42; DAM-disjoint v0.2 |
| Collection/normalization | `UPDATE_REQUIRED` | Source acquisition and current curation, not legacy files as final state |
| Documentary/normative corpus | `VERIFY_BEFORE_WRITING` | Group1 corpus and 0B-05C; revalidate counts |
| Historical retrieval | `REWRITE_REQUIRED` | G5 tables; candidate retrieval, not global RAG accuracy |
| Normative retrieval | `REWRITE_REQUIRED` | Corrected Attempt06 comparators; G5/G3 |
| Historical-normative integration | `UPDATE_REQUIRED` | F preserves historical rank; fixed Top-3 |
| Diagnostic reranker | `UPDATE_REQUIRED` | G is diagnostic; no main-flow reranking |
| Auditable explanation | `REWRITE_REQUIRED` | HE4 J/K and both limitations |
| Metrics and inference | `REWRITE_REQUIRED` | 15 paired 99% CIs + one 95% CI; no arm CI/p-values |
| HE5 and limitations | `REWRITE_REQUIRED` | Description not estimable; hierarchy/support descriptive |
| EXP11A | `NEW_TEXT_ALLOWED` | Joint size-composition sensitivity, noncausal |
| EXP11B | `NEW_TEXT_ALLOWED` | Ten observed seed pairs; descriptive only |
| EXP12 | `UPDATE_REQUIRED` | Closed without retrieval; diversity effect not estimable |
| Results | `REWRITE_REQUIRED` | Nine G5 canonical tables; no superseded figures |
| Hypothesis contrast | `REWRITE_REQUIRED` | No new decision; HG/HE1 formal absence explicit |
| Discussion | `REWRITE_REQUIRED` | G4 interpretation, limits and literature contrast |
| Reproducibility | `UPDATE_REQUIRED` | G2A/G2B with declared limitations |
| Conclusions | `REWRITE_REQUIRED` | Frozen claim-evidence chain; no invented HG/HE1 decision |
| Recommendations | `KEEP_WITH_TERMINOLOGY_REVIEW` | Future work, not completed generalization |
| Figures and tables | `UPDATE_REQUIRED` | G5 nine tables; G6 three figures/captions |
| Thesis bibliography | `VERIFY_BEFORE_WRITING` | Existing references are a baseline, not scientific ground truth |
| Institutional structure/format | `IMMUTABLE` | Preserve current layout absent official/author rule |

The frozen Word is older than the later group closures. PREF003 locates legacy 3,000/100/1,006 partition values, outdated retrieval figures, and the obsolete statement that no inference/CI occurred. These are future correction targets only. The current source values and estimands must be confirmed from the listed primary artifacts when editing; do not merely replace numbers from this index.

## Article onboarding and future G7-F03 contract

At `origin/article/main-manuscript=2aad97aaceec0af6be0edb9ba0dd29170ad35baf`, all eight onboarding controls were read in the required order; their path, blob and role are frozen in JSON. `ARTICLE_STATUS.md` governs the live state: phase `EXPERIMENTAL DESIGN`, gate `EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT`, canonical master `ARTICLE_MASTER_V009`. Only narrow B01 technical/editorial skeleton alignment and stale Spanish placeholder removal are authorized there. B01 prose rewrite and scientific drafting of Section 4.3+ are not. Results, Discussion, Conclusion, Abstract, final title and novelty are not opened by G7-F01.

The article contract has 12 block rows in JSON. Related Work, Introduction B01 and Architecture 3.1–3.7 are closed/frozen/integrated and `IMMUTABLE` absent an explicit editorial reopening. B01 is `VERIFY` under D-047. Section 4.3–4.8 science, Results, Discussion, Conclusion, Abstract, final title/keywords and novelty/gap are `NOT_AUTHORIZED`. Future approved GitHub article text must have Spanish-English semantic equivalence. Any G7-F03 action must first compare the then-current article head with the frozen SHA and reconcile material scientific drift; a SHA change alone is not a contradiction.

Preserve the architecture: historical ranking → fixed Top-3 → candidate-specific normative evidence → context → local LLM explanation. Normative retrieval does not rerank; diagnostic LLM reranking is separate. Article control files do not replace the primary experimental sources. Existing article bibliography is governed by its `SOURCE_REGISTRY.md`; the thesis references are a baseline only; G4 literature contrast controls scientific comparisons. No new reference is introduced here.

## Institutional rules and permanent guardrails

No expressly current, versioned UNMSM thesis-format rule was located in the repository. Preserve the current thesis structure and format unless an author-provided or official source supplies a different rule; do not invent one. This does not block scientific source freezing but blocks format changes justified as a new institutional requirement.

```text
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_OR_LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
EXP11A != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B != SEED_SUPERPOPULATION_INFERENCE
ATTEMPT06 != GLOBAL_ZERO_IMPACT
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN
```

Open source gaps are explicit in JSON: HG and HE1 formal dispositions, thesis binary recheck before G7-F02, exact approved-project/Annex bytes for literal/method edits, explicit UNMSM format rule, and article drift check before G7-F03. None is silently filled. G7-F01 awaits independent external audit; no thesis/article modification or downstream activation is authorized by this candidate.
