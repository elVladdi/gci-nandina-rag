# Experimental Design B01 V04 — Transversal positioning review

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B01_V04_TRANSVERSAL_POSITIONING_REVIEW_V01
DATE = 2026-09-25
ROLE = IA_GESTORA / LEAD_SCIENTIFIC_EDITOR
INPUT = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04
INPUT_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
INPUT_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
AUTHOR_INTENT_CLARIFICATION = FRAMEWORK_LEVEL_CONTRIBUTION / EXPERIMENTAL_TESTBED_IS_ONLY_ONE_INSTANTIATION
B01_SCIENTIFIC_FACTS = PRESERVED
B01_STRUCTURAL_ALIGNMENT = PRESERVED
TRANSVERSAL_POSITIONING = REVISION_REQUIRED
AUTHOR_APPROVAL_GATE = SUSPEND_PENDING_POSITIONING_CORRECTION
SECTION_4_3_TO_4_8_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

## 1. Editorial object of the review

This review does not reopen the factual or methodological audit of Sections 4.1–4.2.3, which already passed. It evaluates whether the cumulative manuscript communicates the intended scientific hierarchy consistently:

1. the contribution is a configurable framework for auditable tariff-classification decision support;
2. the framework supports classification by generating/ranking candidate codes, associating documentary evidence, and producing controlled explanations whose provenance can be inspected;
3. the eight-digit NANDINA / Chapter-87 / Peruvian setting is the empirical instantiation used to evaluate the framework, not the conceptual scope of the framework;
4. re-instantiation in other class spaces, tariff depths, historical datasets, or compatible documentary corpora is a design/configurability property and is not evidence of empirical performance transfer.

The framework must not be described as autonomously adjudicating a legally final tariff code. Its primary evaluated classification output is a ranked candidate set, specifically the fixed Top-3 in the reference instantiation.

## 2. What already communicates the intended idea correctly — PASS

### 2.1 General-before-specific architecture

The manuscript explicitly requires the general decision-support architecture to precede the empirical instantiation and states that the testbed must not define the conceptual scope. Section 3 follows that rule and does not begin from NANDINA, Chapter 87, H100, or the Peruvian corpus.

### 2.2 Functional separation

The Introduction, Related Work positioning, and Section 3 consistently preserve the core contract:

`historical retrieval → fixed ranking / Top-3 → documentary evidence → controlled explanation`.

The downstream documentary and generative stages cannot insert, remove, substitute, or reorder candidates in the primary flow. This supports the intended audit/traceability logic because the origin of each candidate remains attributable to historical retrieval while documentary evidence and explanation remain separately inspectable.

### 2.3 Experimental boundary

Section 4.1 is correctly framed. It says that the experiment evaluates one concrete offline instantiation at eight-digit NANDINA within Chapter 87 and immediately states that this scope delimits only the empirical instantiation. It also states that the interfaces can be re-instantiated with other historical banks, class spaces, tariff depths, or compatible documentary corpora.

### 2.4 Configurability versus generalization

Sections 3.7 and 4.1 correctly distinguish re-instantiation/configurability from empirical generalization. This boundary must remain frozen.

## 3. Main conceptual weakness — framework hierarchy is not yet dominant enough

The current manuscript usually names the contribution as a `decision-support architecture` or a `procedure`. Those descriptions are scientifically compatible with the work, but they are narrower than the intended article-level object. The word `framework` is not used to identify the present contribution in the publication-facing prose; its occurrences mainly describe prior work or the evaluation framework.

As a result, a reader can correctly understand the component architecture but still perceive the paper mainly as a candidate-retrieval-plus-explanation architecture rather than as a broader framework for auditable tariff-classification decision support that includes:

- candidate generation/ranking;
- fixed-candidate control;
- documentary evidence association;
- controlled explanation;
- traceability/audit-oriented inspection;
- evaluation boundaries;
- reproducibility/re-instantiation interfaces.

The architecture remains the technical core of the framework; the correction must not replace or weaken the architecture concept.

## 4. Specific residues requiring correction

### F1 — Introduction should define the article-level object as a framework

The paragraph beginning `This study examines a decision-support architecture...` correctly describes the architecture but should establish the article-level object as a framework whose core architecture enforces the separation of ranking, evidence, and explanation.

Required semantic outcome:

`FRAMEWORK = architecture + controlled information flow + evaluation boundaries + reproducibility/re-instantiation interfaces`.

Do not claim novelty merely from using the term framework.

### F2 — Auditability/inspectability should be explicit in the contribution statement

The opening paragraph mentions an auditable decision-support workflow, and later sections discuss auditability. However, the three-contribution paragraph does not make sufficiently explicit that the purpose of preserving component authority and provenance is to make each recommendation inspectable for review/audit.

The correction should state, without overclaiming, that the framework preserves a traceable relation among commercial description/query, historical precedent, fixed candidate, documentary evidence, and generated explanation. This supports case-level inspection/audit; it does not establish legal correctness or a formal auditability score.

### F3 — Experimental paragraph should subordinate NANDINA/Chapter 87/Peru more clearly

The current paragraph starts from an `offline customs-classification testbed for NANDINA subheading recommendation`. Although it later says the testbed does not define conceptual scope, the rhetorical order still gives the empirical domain more prominence than necessary.

Preferred rhetorical hierarchy:

`To evaluate the framework, we instantiate it in ... eight-digit NANDINA / Chapter 87 / Peruvian documentary-administrative context.`

The empirical domain must be presented as the evaluation setting, not as the product being contributed.

### F4 — Remove the residual `non-binding testbed` formulation from the Introduction

`The testbed is non-binding` is not the clearest scientific statement of the boundary and had already been identified as rhetorically weak. The relevant limitation is already expressed more precisely in Section 4.1: the experiment is not an operational customs deployment or a legal adjudication.

The Introduction should use that scientific boundary rather than `non-binding` as the primary qualifier.

### F5 — Classification terminology must remain precise

The framework can legitimately be positioned as supporting tariff classification, but the manuscript must not imply that the evaluated primary flow autonomously selects or legally adjudicates one final code. In the reference experiment, historical retrieval generates/ranks candidate codes and fixes a Top-3; later stages document and explain those candidates.

Therefore:

`TARIFF_CLASSIFICATION_SUPPORT = AUTHORIZED`

`RANKED_CANDIDATE_RECOMMENDATION = AUTHORIZED`

`AUTONOMOUS_FINAL_LEGAL_CLASSIFICATION = PROHIBITED`

`CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY` remains binding.

### F6 — Extensibility should be expressed as re-instantiation, not performance transfer

The manuscript already supports re-instantiation with other datasets, target class spaces, tariff depths, and compatible documentary corpora. Future wording may make examples clearer (e.g., different tariff depths, broader/different chapter spaces, or jurisdiction-specific documentary corpora), but must retain the existing boundary:

`CONFIGURABILITY / RE-INSTANTIATION ≠ EMPIRICAL GENERALIZATION`.

No claim that the observed Chapter-87 performance transfers to another chapter, tariff depth, country, or corpus is permitted.

## 5. Scope of required correction

This is a narrow transversal positioning correction, not a new scientific rewrite.

Priority correction targets:

1. Introduction paragraph that defines the proposed object;
2. Introduction contribution paragraph;
3. Introduction empirical-evaluation paragraph;
4. corresponding Spanish semantic-control mirror;
5. one terminology reinforcement in Section 3.7 if needed to make clear that the architecture is the technical core of the wider framework.

Sections 4.1–4.2.3 do not require factual rewriting. Their empirical-scope language is already correct.

Related Work 2.6 is substantively compatible and should not be rewritten unless a minimal terminology adjustment is strictly necessary for consistency.

## 6. Verdict

```text
CORE_SCIENTIFIC_IDEA = PRESENT
FRAMEWORK_GENERALITY = PRESENT_BUT_NOT_DOMINANT_ENOUGH
EXPERIMENTAL_TESTBED_BOUNDARY = PASS
CONFIGURABILITY_BOUNDARY = PASS
AUDITABILITY_PURPOSE = PRESENT_BUT_UNDEREMPHASIZED_IN_CONTRIBUTION
CLASSIFICATION_SEMANTICS = REQUIRE_PRECISION
B01_FACTUAL_CONTENT = PASS / DO_NOT_REOPEN
B01_STRUCTURE = PASS / DO_NOT_REOPEN
TRANSVERSAL_POSITIONING = REVISION_REQUIRED
AUTHOR_APPROVAL_GATE = SUSPEND_PENDING_CONTROLLED_CORRECTION
```

The correction should strengthen the hierarchy `general auditable classification-support framework → core architecture → specific NANDINA/Chapter-87/Peruvian experimental instantiation`, without changing the frozen empirical facts, performance scope, or legal-correctness boundaries.