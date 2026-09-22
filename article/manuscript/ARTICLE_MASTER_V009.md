**Knowledge-Based Systems target manuscript**

**KBS_ARTICLE_WORKING_STRUCTURE_V01**

*Cumulative editable base for subsequent manuscript versions*

| **Target journal**          | Knowledge-Based Systems                                                              |
|-----------------------------|--------------------------------------------------------------------------------------|
| **Article type**            | Research article                                                                     |
| **Editorial basis**         | KBS empirical writing guide based on 34 recent Open Access articles                  |
| **Current purpose**         | Freeze and edit the complete article structure before further section drafting       |
| **Scientific prose status** | No manuscript prose is approved by this structure file                               |
| **Version policy**          | Future deliveries must preserve and progressively complete this cumulative structure |

Editorial control: this file is a structural working base, not a
completed manuscript. Gray italic notes are drafting instructions and
must be removed from the submission version.

Key structural principle: the reader first encounters the scientific
problem and positioning, then the general decision-support architecture,
and only afterwards the specific experimental instantiation. The
experimental testbed must not define the conceptual scope of the
architecture.

# Structure at a glance

| **Section**                       | **Primary function**                                                                                                                               |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Front matter                      | Title; Abstract; Keywords                                                                                                                          |
| 1\. Introduction                  | Problem → limitation → proposal → contribution → evaluation context → RQs → roadmap                                                                |
| 2\. Related work                  | Prior approaches organized by function, ending in explicit positioning                                                                             |
| 3\. Decision-support architecture | General architecture and information flow, without opening from the experimental testbed                                                           |
| 4\. Experimental design           | Specific empirical instantiation, datasets, corpus, partitioning, configuration, evaluation and reproducibility                                    |
| 5\. Results                       | Results organized by function and research question                                                                                                |
| 6\. Discussion                    | Interpretation, comparison, implications, transfer conditions and limitations                                                                      |
| 7\. Conclusion                    | Contribution, evidence, scope and implication                                                                                                      |
| End matter                        | Data availability; reproducibility resources; CRediT; funding; competing interests; acknowledgements; references; supplementary material if needed |

# PART I — English manuscript master

The English part is the publication-facing master. Drafting notes below
define the intended function of each section; they are not manuscript
prose.

## Title

Define at the end. It should foreground the scientific/architectural
contribution; the customs domain may appear as an application or testbed
only if it improves precision.

\[Final title to be written after the manuscript is complete.\]

## Abstract

Recommended rhetorical order: concrete problem → limitation → proposed
architecture → evaluation → main findings → bounded implication. Target
approximately 200–250 words unless final content requires otherwise.

\[Section text to be drafted in a later approved version.\]

## Keywords

Select after the final title and abstract. Keywords should represent
both the contribution and the application domain without reducing the
work to the testbed.

\[5–7 final keywords.\]

# 1. Introduction

Tariff classification decision support starts from a concrete information problem: a commercial description must be mapped to a code within a hierarchical nomenclature while the reviewer may also need documentary material that explains why a candidate is relevant. Automated systems address different parts of this problem. Some models select a code directly, some produce ranked candidates, some retrieve regulatory or manual text, and others generate a rationale or trace. These functions are related, but they do not have the same output or the same authority over the final recommendation. For an auditable decision-support workflow, it therefore matters not only which techniques are used, but also which stage is allowed to determine the candidate set, which stage only documents it, and which stage only explains an already fixed result.

Prior work shows several ways in which these functions can be coupled. Lee et al. (2021) predict a heading, retrieve key sentences from the HS manual, and then use the product description together with those sentences to predict the subheading; the retrieved material therefore participates in the later classification decision. Lee et al. (2023) separate the sequence differently: their system predicts classification candidates before retrieving evidence about each candidate from the HS manual, demonstrating that candidate prediction followed by documentary support is already established in customs decision support. Regulation-driven search can give retrieved evidence still greater influence: Wang et al. (2026) build evidence-enriched candidate packages and use a decision model to select each next hop in a regulatory hierarchy before aggregating evidence for the final rationale. In legal AI, Chen and Tanaka-Ishii (2026) retrieve legal sources and examples, compile them into an executable representation, and refine that representation as part of the process that produces the label. These studies provide close and partial precedents for combining retrieval, evidence, and explanation; the limitation addressed here is therefore not an absence of such components.

The remaining methodological problem concerns operational and evaluative separation. When several downstream stages can alter the same candidate set, a reviewer cannot easily determine whether a candidate was selected by the historical evidence, by the regulatory material, or by the language model. The same coupling also complicates evaluation: a candidate-ranking metric measures a different object from documentary association, and neither one measures the structure or traceability of a generated explanation. If these outputs are reported as if they described one undifferentiated system decision, it becomes difficult to attribute an observed outcome to the component that actually produced it. In a regulated setting, this distinction is also important for human review: attaching an official or relevant passage to a candidate does not establish substantive legal correctness, and producing a structured explanation does not turn the language model into the classifier that selected the code.

This study examines a decision-support architecture that makes those boundaries explicit. A historical retrieval stage receives the normalized commercial description, generates candidate codes from a labeled historical bank, and fixes their ranking. The top three candidates become a fixed Top-3 before normative retrieval begins. A separate normative-retrieval stage then associates documentary evidence with each of those candidates without inserting, deleting, substituting, or reordering codes. Finally, a downstream local LLM receives the fixed candidates and their retrieved documentary context to produce a controlled explanation; it has no authority to modify the candidates or feed information back into classification. The architecture therefore treats candidate ranking, documentary association, and explanation as distinct outputs that can be inspected and evaluated separately.

The article makes three bounded contributions. First, it specifies a procedure that assigns a concrete role to each component. Historical retrieval generates and ranks candidates and fixes the Top-3; normative retrieval then associates evidence with those fixed candidates without changing their membership or order; and the local LLM generates only the explanation of that fixed Top-3. Second, it evaluates candidate retrieval, documentary association, and controlled explanation as distinct outputs, while preserving DAM-level grouping when shared declaration structure creates dependence. Third, it documents the interfaces and reproducibility resources needed to re-instantiate the procedure with a different labeled historical bank, target class space, or compatible documentary corpus. This third contribution concerns reproducibility and re-instantiation of the procedure; it does not imply that performance observed in one empirical setting will transfer to another.

The empirical evaluation uses an offline customs-classification testbed for NANDINA subheading recommendation within the delimited Class/Chapter 87 setting. The commercial description of a SERIE is used as the query representation after normalization; SERIE is the analysis unit, and DAM/customs declaration is the grouping unit where dependence must be controlled. The implementation combines a labeled historical bank, a normative/documentary corpus, historical candidate retrieval, candidate-specific normative retrieval, and a local LLM restricted to explanation of the fixed Top-3. The testbed is non-binding and supports analysis of the architecture rather than defining its conceptual scope. The same procedure can be re-instantiated with other data, class spaces, and documentary corpora when the required interfaces and provenance controls are satisfied, but such configurability is not evidence of empirical generalization beyond the evaluated setting.

The evaluation is guided by four research questions:

- **RQ1.** What candidate-retrieval performance does historical retrieval achieve under partitions that are disjoint by DAM/customs declaration?
- **RQ2.** To what extent can identifiable normative evidence be associated with each candidate in a fixed historical Top-3 without altering candidate order?
- **RQ3.** To what extent can a local LLM restricted to the fixed Top-3 preserve the candidates and their order while producing structured explanations linked to identifiable evidence?
- **RQ4.** What validity limits do intra-DAM dependence, residual near-duplicates, historical-bank composition, and normative drift introduce when interpreting the results of the offline pilot?

The remainder of the article is organized as follows. Section 2 reviews automated tariff classification, knowledge-enhanced retrieval, LLM roles, evidence grounding, auditability, reproducibility, and the positioning of this study. Section 3 describes the decision-support architecture and its information flow. Section 4 presents the experimental design, data and documentary resources, partitioning, system configuration, evaluation protocols, and reproducibility resources. Section 5 reports results by system function and research question, Section 6 discusses their implications and limitations, and Section 7 concludes the article within the evaluated scope.

# 2. Related work

Organize by technical function/problem family rather than
author-by-author chronology. Each subsection should end with a synthesis
relevant to the positioning of this study.

## 2.1. Automated tariff classification and candidate retrieval

Automated tariff coding has most often been framed as a text-to-code
prediction problem: a model receives a product or declaration
description and returns one or more HS labels. Early work treated this
as supervised text categorization, with models trained on historical
declarations and evaluated at a defined level of the tariff hierarchy.
Ding et al. used a Background Net classifier to map goods-declaration
text to HS categories, illustrating a conventional direct-classification
formulation (Ding et al., 2015). CNN-based work later showed that short
descriptions could be classified separately at HS2 and HS4, while also
exposing the increased class cardinality at finer levels (Luppes, 2019).
At larger scale, Ruder compared conventional machine-learning and neural
classifiers on more than one million cargo descriptions spanning
thousands of HS6 classes (Ruder, 2020). These studies share a supervised
prediction objective, but their target levels, label spaces, datasets,
and evaluation measures differ; reported percentages therefore should
not be read as directly comparable measures of tariff-classification
performance.

Subsequent work has changed the representation of trade text without
necessarily changing that prediction objective. Anggoro et al., for
example, fine-tuned Sentence-BERT with Multiple Negative Ranking loss to
obtain transaction embeddings and then used those fixed-length
representations as inputs to SVM and Random Forest classifiers for
HS-code prediction (Anggoro et al., 2025). Other approaches exploit the
hierarchy more explicitly. Lee et al. first predict a four-digit
heading, retrieve relevant sentences from the HS manual, and then
predict the six-digit subheading from the product description together
with the retrieved sentences (Lee et al., 2021). This staged design
differs from treating HS2, HS4, or HS6 as independent flat
classification targets because information produced between levels can
participate in the later decision.

A second family formulates the problem as retrieval or ranking rather
than as a single-label decision. Stassin et al. compared supervised
neural models with semantic-similarity methods over HS6, HS8, and HS10
and evaluated whether relevant codes appeared near the top of a ranked
output (Stassin et al., 2023). Pain likewise used semantic textual
similarity to generate ranked commodity recommendations and evaluated
whether the expected commodity code appeared among the top-k suggestions
(Pain, 2021). In this formulation, the model's immediate output is a
candidate list that can support a subsequent human or automated
decision. This distinction is operationally important: Top-k retrieval
measures the presence and ordering of candidates, whereas classification
accuracy evaluates a selected label. The two objectives can coexist in
tariff-assistance systems, but their metrics and denominators should not
be treated as interchangeable.

A third task begins from a code that has already been assigned and asks
whether that assignment is coherent or plausible. Spichakova and Haav
combine textual similarity with similarity derived from the HS taxonomy
to assess assigned-code correctness and to provide alternative
predictions or recommendations (Spichakova & Haav, 2020). Such
validation or correction is not equivalent to generating candidates from
an uncoded description, because the existing code is part of the object
being assessed and the evaluation depends on assumptions about the
historical labels used as reference.

Taken together, this literature spans direct classification, staged
hierarchical prediction, candidate retrieval/ranking, and
post-assignment validation. The boundaries between these tasks matter
because the same technologies—embeddings, neural encoders, similarity
functions, or historical records—can support different outputs and
evaluation criteria. They also clarify the point at which external
documentary knowledge enters a system: in some designs it participates
in the classification decision itself, while in others retrieval is used
to expose supporting material around candidate codes. That functional
distinction motivates the next subsection on knowledge-enhanced
retrieval and regulatory reasoning.

## 2.2. Knowledge-enhanced retrieval and regulatory reasoning

External knowledge enters tariff and regulatory systems in materially
different ways. In some models, domain structure is part of the
predictor itself rather than a document retrieved after a candidate has
been produced. Qi et al. transform declaration elements into semantic
and attribute associations, construct a knowledge graph, and train a
graph-attention model so that HS-code prediction is formulated as link
completion on that graph (Qi et al., 2025). Here, structured knowledge
affects the representation and inference that produce the code. This
role differs from documentary retrieval whose output is shown as
supporting material, and it also differs from validating an already
assigned code. The distinction is important because a knowledge graph, a
taxonomy, and a retrieved passage may all be described as “external
knowledge” while intervening at different points in the decision
process.

Document retrieval can also participate directly in classification. Lee
et al. first predict a four-digit heading, retrieve key sentences from
the corresponding HS manual, and then use the product description
together with those sentences to predict the six-digit subheading (Lee
et al., 2021). The retrieved sentences therefore become inputs to the
later prediction rather than merely an explanation displayed after
classification. A related customs decision-support design separates
these roles differently: it first predicts candidate classifications and
then retrieves evidence about each candidate from the HS manual,
returning candidate codes together with relevant supporting sentences
for officers to inspect (Lee et al., 2023). These examples show why code
retrieval, sentence retrieval, precedent retrieval, and evidence
retrieval should not be collapsed into a single function. The object
retrieved and the point at which retrieval occurs determine whether it
generates candidates, changes a prediction, or supports review of an
existing suggestion.

Regulation-driven search makes this coupling even more explicit. In
constraint-aware hierarchical search, regulatory documents are organized
as a searchable tree; at each level, the system retrieves plausible
child nodes and supporting evidence, constructs a candidate package, and
uses a decision model to select the next hop or stop (Wang et al.,
2026). Once the path is fixed, evidence from visited nodes is aggregated
for verification and rationale generation. Regulatory material in this
setting is thus part of the traversal that determines the classification
path, not simply a citation layer attached to an independently selected
label. The same functional reading is necessary for other agentic or
rule-constrained systems: hierarchy, exclusions, redirects, and
retrieved rules may restrict or alter the search trajectory. A
hierarchy-consistent path or a rationale supported by retrieved material
can make the decision process inspectable, but neither property by
itself establishes independently adjudicated legal correctness or a
formal auditability score.

General retrieval-augmented generation provides a broader pattern for
coupling external text with generation. Lewis et al. combine a neural
retriever over a non-parametric document index with a
sequence-to-sequence generator; retrieved documents are supplied as
additional context when the target sequence is generated (Lewis et al.,
2020). In that formulation, retrieval and generation are components of
one probabilistic model, and the generated output remains conditioned on
both the input and retrieved passages. RAG should therefore not be used
as a synonym for every system that happens to retrieve documents:
retrieve-then-generate, retrieval used inside classification, and
evidence retrieval for human inspection assign different functions to
the retrieved material. Likewise, an inspectable passage is not
automatically a complete attribution of every generated claim, nor does
retrieval alone guarantee that the output is grounded in the governing
source.

Query transformation illustrates another boundary. Ma et al. place a
rewriter before retrieval: the system rewrites the input into a search
query, retrieves documents, and then passes those documents to a
black-box reader; their trainable variant optimizes the rewriter using
reader feedback (Ma et al., 2023). Because rewriting changes what the
retriever searches for, it can change the downstream context and answer.
The rewritten query is therefore a control input to retrieval, not
evidence for the final claim. More generally, query rewriting, document
retrieval, passage selection, and generation are separable operations
even when an implementation trains or executes them jointly.

Across these approaches, the scientifically useful question is not
simply whether a system “uses knowledge,” but what that knowledge does.
It may be encoded as structure that participates in prediction,
retrieved as context that changes a later decision, used as rules or
constraints during hierarchical search, or presented as supporting
material for human review. These roles imply different outputs and
different evaluation targets, and visible citations or reasoning traces
should not be treated as substitutes for source-to-claim verification or
substantive correctness. This functional separation also clarifies the
next issue: once retrieval and regulatory context are available, an LLM
may still serve very different roles—as classifier, search controller,
reader/reasoner, or explanation generator. Those roles are examined in
the next subsection.

## 2.3. LLMs for classification, reasoning, and explanation

The label “LLM” covers systems that assign very different authority to
the language model. Some models directly choose a tariff code from a
product description, others are fine-tuned encoders that output a class
from a fixed label space, and retrieval-augmented or agentic systems may
let the model control search, compare candidates, or produce a rationale
after earlier decisions have already constrained the outcome. The
relevant distinction is therefore not model size or branding, but which
decision the model is allowed to make and which upstream outputs it can
change.

Direct generative classification gives the model broad authority over
the predicted code. Marra de Artiñano et al. query GPT-3.5 through
direct API prompts so that products are categorized individually,
without training GPT-3.5 on the customs datasets used to fit the
conventional machine-learning baselines (Marra de Artiñano et al.,
2023). Here the model itself maps the description to the tariff label.
That setup should be distinguished from studies that use the term “large
language model” for supervised transformer encoders. Koch and Power
fine-tune transformer models on labeled shipping-manifest descriptions
for HS-code classification; their experimental comparison includes BERT-
and RoBERTa-family models trained for the same classification task (Koch
& Power, 2025). In such a system, the transformer supplies contextual
representations inside a supervised classifier rather than freely
generating a code through prompting. Direct generative classification
and fine-tuned transformer classification therefore place different
constraints on the model even when both are described as LLM-based.

Retrieval augmentation changes the role again when retrieved material
becomes context for the model that determines the code. Kim et al.
propose THE-RAG, a two-stage framework that combines dense retrieval,
BM25, and reranking and evaluates how retrieval preprocessing and the
language model’s sentence-comprehension capability affect HS-code
classification quality (Kim et al., 2025). In this configuration, the
LLM acts as a retrieval-conditioned reader and decision maker: the
retrieved context informs the final classification rather than merely
documenting a code selected elsewhere. This differs from documentary QA
RAG, where the generated object is an answer to a question, and from
evidence-support retrieval, where retrieved passages can be exposed
around candidates without giving the generator authority to alter
candidate selection.

Agentic designs can expand the model’s authority beyond reading
retrieved passages. In a 2026 preprint, Nguyen et al. combine
multi-agent information retrieval, semantic search over official tariff
documents, evidence-grounded reasoning, consensus validation,
element-wise voting, confidence estimation, and human-in-the-loop
escalation for Canadian 10-digit classification (Nguyen et al., 2026).
In such a workflow, model outputs and retrieved evidence participate in
the classification procedure itself. Consensus or self-consistency can
stabilize that procedure or express agreement among
repeated/model-specific outputs, but agreement is not independent ground
truth. Likewise, confidence-based escalation changes how uncertain cases
are handled; it does not by itself establish that the selected code is
substantively or legally correct.

A different separation appears when the model participates in search
first and generates a rationale only after the decision path has been
fixed. In another 2026 preprint, Wang et al. propose constraint-aware
hierarchical search in which an LLM helps choose each next hop from
locally retrieved child nodes and supporting regulatory evidence. After
the hierarchy path is fixed, evidence from visited nodes is aggregated
for final verification and rationale generation (Wang et al., 2026). The
downstream rationale stage therefore follows a fixed path, but the same
overall system used an LLM and regulatory evidence to construct that
path. This is functionally different from treating search control,
reranking, or next-hop selection as explanation-only generation. It also
illustrates why a rationale or reasoning trace should not be assumed to
faithfully expose the causal basis of the preceding decision merely
because it is produced after that decision.

Across these configurations, LLM authority ranges from selecting the
code directly, to operating inside a supervised classifier, to reading
retrieved context while retaining decision authority, to steering search
or consensus, and finally to generating explanatory text after upstream
decisions have constrained the available output. These roles lead to
different failure modes and different evaluation needs. Classification
performance cannot establish whether a rationale is faithful; a visible
reasoning trace does not by itself demonstrate source-to-claim support;
and citations or provenance metadata do not establish formal
auditability or legal correctness. These distinctions motivate the next
subsection, which examines how grounding, explainability, and
auditability should be evaluated once an LLM-generated output is
attached to retrieved evidence or an explicit decision trace.

## 2.4. Evidence grounding, explainability, and auditability

Grounding should be assessed as a relationship between an output and
evidence, not as the mere presence of retrieved text.
Retrieval-augmented generation allows the generator to condition on
non-parametric memory and can improve access to updatable external
knowledge and make retrieved passages inspectable for verification
(Lewis et al., 2020). Yet the generator still combines the input,
retrieved passages, and its parametric model; retrieval alone does not
show that each statement in the output is supported by a source.

Asai et al. make this distinction explicit: passages can contain an
answer string and still lack evidence, so their evidentiality model
predicts whether a passage supports the gold output rather than treating
retrieval or lexical overlap as support (Asai et al., 2022). Grounding
therefore requires an evaluated support relation between a claim and the
material offered as evidence.

Explainability addresses a different question: what information is
exposed to help a person understand or review a recommendation. In
customs decision support, Lee et al. first predict candidate
classifications and then retrieve relevant sentences from the HS manual,
presenting candidate codes together with those sentences as explainable
evidence (Lee et al., 2023). This design makes documentary support
visible to the reviewer, but visibility and interpretability do not by
themselves establish that every explanatory statement is entailed by the
cited passage. The same boundary applies to rationales and reasoning
traces more broadly. A rationale can organize information around a
decision and still require a separate faithfulness test if it is
intended to represent the basis on which that decision was actually
reached.

Provenance and traceability answer another question: where an output
came from and which objects or operations contributed to it. The FAIR
Data Pipeline, for example, records data and metadata as analyses
consume and produce research objects and can trace scientific outputs
back through modelling or analysis code to primary data (Mitchell et
al., 2022). Such lineage can make dependencies, versions, and
transformations inspectable. It does not, however, establish that the
source data, transformation, interpretation, or final output is
substantively correct. Traceability is therefore evidence about the
production path of an artifact, not a correctness verdict on the
artifact itself.

Auditability can also refer to different scopes. Raji et al. propose an
internal algorithmic-audit framework applied throughout the
organizational development lifecycle, with each audit stage producing
documents that collectively form an audit report (Raji et al., 2020).
This kind of lifecycle audit reconstructs design decisions, risks,
testing activities, and organizational accountability over time. At the
level of an individual output, a distinct review question is whether
that output can be examined against explicit criteria using its
associated evidence and trace. A lifecycle record may support such
review, but it is not equivalent to a case-level review, just as a
case-level evidence package does not reconstruct the full development
lifecycle.

Regulatory systems add source authority and currency as further
dimensions. Grainger's illustrative criteria for electronic tariff tools
include the ability to incorporate tariff updates, cross-reference
authoritative guidance, apply classification rules, and provide a
statement explaining the recommendation (Grainger, 2024). These
capabilities matter because an explanation built from an obsolete or
non-authoritative document may be traceable while still being unsuitable
for the current decision context. Conversely, citing an official and
current source establishes neither that the relevant provision was
selected nor that it was interpreted correctly for a particular case.
Documentary authority and currency are therefore relevant dimensions to
examine in regulated decision support, but they remain distinct from
substantive or legal correctness.

Taken together, grounding, explanation, provenance, lifecycle auditing,
review at the level of individual outputs, and source authority answer
different verification questions. They should not be arranged as a
maturity ladder in which one property guarantees the next. A system may
expose sources without demonstrating claim support, preserve lineage
without proving correctness, or maintain an audit trail without
validating each output. Conversely, a well-supported individual output
does not establish reproducibility of the wider system or dataset. Once
these constructs are separated, evaluation can assign each one an
appropriate protocol and metric; the next subsection therefore turns to
reproducibility and evaluation in knowledge-based decision support.

## 2.5. Reproducibility and evaluation in knowledge-based decision support

Once grounding, explanation, provenance, and audit scope are separated, reproducible assessment requires the experimental objects behind a reported result to be inspectable as well. Dataset documentation is one part of that requirement. Bender and Friedman define a data statement as a characterization that supplies context for judging how experimental results may generalize, how software may be deployed, and which biases may be reflected in systems built from the data (Bender & Friedman, 2018). Gebru et al. broaden this documentation across the dataset lifecycle by organizing datasheets around motivation, composition, collection, preprocessing and labeling, uses, distribution, and maintenance (Gebru et al., 2021). Such records make assumptions and dataset context visible, but documentation is not a certificate of dataset quality, representativeness, independence, or freedom from leakage. Those properties require separate evidence and, where relevant, explicit controls.

Dataset documentation also needs to distinguish descriptive metadata from technical identity. A datasheet can record relationships between instances and recommended data splits, which helps a reader reconstruct how a dataset was intended to be used, but recording a split does not itself enforce dependence control or prove that partitions are independent (Gebru et al., 2021). Reproducible computation additionally benefits from identifying the concrete versions of data, processing code, parameters, and other research objects used in a run. The FAIR Data Pipeline illustrates this stronger lineage relation: it annotates data as analyses consume them and can trace scientific outputs back through analytical or modelling code to primary data (Mitchell et al., 2022). Provenance therefore answers which objects and transformations contributed to an output. It does not establish that those inputs, transformations, or outputs are substantively correct, and a provenance chain alone is not equivalent to full reproducibility.

Reproducibility itself also needs a declared convention. Pineau et al. explicitly distinguish several related concepts: under the terminology adopted in their study, reproducible work repeats an experiment with the same data and analytical tools; replicable work changes the data while retaining the tools; robust work keeps the data but changes the analysis; and generalisable work changes both data and analytical tools while reaching the same conclusions (Pineau et al., 2021). These labels should not be treated as universal nomenclature, but the separation is methodologically useful. Reproducing a reported result under closely matched conditions does not by itself show robustness to another implementation, replication on different data, or generalization beyond the evaluated setting. Likewise, making code and data available may facilitate reproduction without guaranteeing that another researcher will reproduce the result successfully.

Traceability across a development process serves yet another function. Raji et al. describe an internal algorithmic-audit framework applied throughout the organizational development lifecycle, in which each audit stage produces documents that collectively form an audit report (Raji et al., 2020). Such artifacts can preserve design decisions, tests, risks, and accountability information that a final performance number cannot recover. Their scope, however, is lifecycle-oriented. A documented internal audit trail does not automatically constitute a formal review of every individual output, and it does not establish substantive or legal correctness.

These distinctions have a direct consequence for evaluation design: the metric must correspond to the function and output being assessed. Pineau et al. identify under-specification of reported metrics, improper statistical analysis, and over-claiming beyond the presented evidence among recurring obstacles to reproducible machine-learning research (Pineau et al., 2021). In multi-stage knowledge-based systems, this problem is amplified because retrieval, ranking, evidence selection, classification, and explanation can produce different objects. A retrieval metric describes a ranked set under a particular relevance definition; a classification metric describes selected labels; an evidence measure concerns retrieved support; and an explanation measure concerns properties of generated or presented rationales. Correctly specifying a metric is therefore necessary but not sufficient for comparison: aligned metrics do not make different tasks, datasets, relevance judgments, or output semantics equivalent.

Reproducible evaluation consequently depends on a chain of explicit relationships rather than on a single headline score: the dataset and its intended use are documented; the concrete experimental objects and versions are identifiable; the production path of outputs is traceable; the reproducibility claim states which conditions are being held fixed or changed; and each metric is interpreted only for the function it actually measures. These controls improve the inspectability of evidence without converting documentation into quality certification, lineage into correctness, reproducibility into generalization, or metric alignment into task equivalence. With those evaluation boundaries established, the remaining literature can be compared in terms of how these functions are combined or kept separate, which is the purpose of the following subsection.

## 2.6. Positioning of this study

The reviewed literature assigns materially different decision authority to classification, retrieval, regulatory evidence, and generation. In one staged customs-classification design, a model first predicts a four-digit heading, retrieves key sentences from the corresponding HS manual, and then predicts the six-digit subheading from the product description together with those retrieved sentences (Lee et al., 2021). Retrieval in that pipeline is therefore not merely an explanatory layer after the decision: the retrieved material becomes an input to the later prediction. This distinction matters for positioning because systems that use similar components can still implement different decision processes depending on when evidence enters and whether it can affect the selected label.

A closer customs precedent separates candidate prediction from documentary support more explicitly. Lee et al. (2023) describe a model that predicts subheading candidates and then retrieves relevant HS-manual sentences as supporting evidence for those candidates. Their output consequently combines candidate codes with inspectable documentary material, showing that candidate prediction plus evidence retrieval is already established prior art and cannot, by itself, distinguish the present study. The remaining distinction concerns authority and sequencing: whether the candidate ranking is fixed independently before documentary retrieval, whether later components are allowed to modify that ranking, and whether generation is part of classification or is restricted to explaining an upstream result.

Regulation-driven and legal-AI systems illustrate stronger coupling between evidence, search, and decision making. Wang et al. (2026) retrieve plausible child nodes and supporting evidence at each level of a regulatory hierarchy, then use a decision model to select the next hop; only after the path is fixed is evidence aggregated for final verification and rationale generation. Chen and Tanaka-Ishii (2026) provide a different audit-oriented example: retrieved legal sources and examples are compiled into an executable representation whose refinement remains part of the process that produces the final label, and the model may revise the program or issue an additional retrieval query. These approaches make decision paths and source support more inspectable, but they also show that explanation-oriented artifacts can remain coupled to the mechanism that constructs the decision itself.

Against this prior art, the present study is positioned through the complete separation of component authority rather than through the isolated presence of historical retrieval, documentary evidence, or an LLM. An external historical-retrieval stage fixes the candidate ranking and a fixed Top-3 before normative documents are retrieved. Normative retrieval is then restricted to attaching evidence to those already fixed candidates; it does not insert, delete, substitute, or reorder them. A downstream local LLM receives the fixed candidates and their documentary context only to produce an explanation, without authority to change the candidate set, alter its order, or feed information back into classification. This functional contract describes the design being studied; it is not, by itself, a claim that the individual components or their combination are novel.

The evaluation logic follows the same separation. Candidate ranking, documentary association, and explanation are treated as different outputs and are evaluated with measures appropriate to their respective functions, while grouping is preserved where shared declaration-level structure creates dependence. This prevents a retrieval metric from being read as overall classification accuracy, documentary association from being treated as substantive normative correctness, or explanation traceability from being treated as legal correctness. It also separates reproducibility of the evaluated procedure from empirical generalization beyond the studied setting. The resulting position is therefore deliberately bounded: the study examines a decision-support architecture in which ranking, evidence, and explanation have explicit non-overlapping authority, and the empirical sections that follow will evaluate those functions without using Related Work to pre-empt their results.

# 3. Decision-support architecture

Describe the general architecture before the empirical instantiation. Do
not open this section by defining NANDINA, Chapter 87, the Peruvian
corpus, H100, or the experimental sample.

## 3.1. Overview and information flow

The architecture separates candidate formation from the stages that document and explain those candidates. A commercial description enters the pipeline and is transformed into a normalized textual query. Historical retrieval uses that query to search a labeled collection of prior records and produces an ordered set of candidate codes. The candidate ranking is therefore determined before any normative document is retrieved and before any generative model is invoked. Once the first three unique codes have been selected, they become the fixed Top-3 that is passed to all downstream processing.

[Figure 1 placeholder — overall architecture and information flow.]

The downstream stages operate on this fixed candidate set rather than on an open class space. Candidate-specific normative retrieval attaches documentary material to each candidate, and context construction combines the query, candidate identities, historical support, and retrieved documentary evidence for subsequent explanation. The local LLM receives that assembled context only after the Top-3 has been fixed. Its output is explanatory text; it does not select a different code, alter candidate membership, or change candidate order. A separate diagnostic reranking path may be evaluated outside the primary flow, but it does not feed back into the ranking used by the architecture.

This sequencing yields three functionally distinct outputs. Historical retrieval produces the candidate ranking and its links to historical precedents. The documentary stage produces candidate–evidence associations. The generative stage produces an explanation of the already fixed candidates using the supplied context. Keeping these outputs separate preserves attribution: a code appears in the Top-3 because of historical retrieval, not because a normative passage or the language model promoted it later. It also allows each output to be evaluated according to the function that produced it rather than treating the pipeline as one undifferentiated classifier.

## 3.2. Query representation and normalization

The retrieval interface receives a textual representation derived from the commercial description. Normalization converts the source description into a deterministic query representation so that the same input, under the same configured preprocessing procedure, yields the same text presented to historical retrieval. This transformation prepares text for matching; it does not consult normative documents, introduce candidate codes, or use a language model to reinterpret the merchandise before candidate retrieval.

At the architecture level, the requirement is reproducibility of this query interface rather than a particular cleaning recipe. The system must preserve the relationship between the source description and the normalized query and must apply the configured transformation consistently to the historical collection and to incoming queries where the retrieval method requires comparable representations. Exact operations such as character normalization, tokenization, field concatenation, or other implementation choices belong to the experimental instantiation and are specified with the retrieval configuration rather than treated as universal properties of the architecture.

The normalized query is therefore the handoff between input preparation and candidate generation. From this point onward, historical retrieval is responsible for determining which labeled precedents are most similar under the configured scoring function. No downstream evidence or explanation stage can modify the query retrospectively in order to change the primary candidate ranking.

## 3.3. Historical candidate retrieval and ranking

Historical candidate retrieval operates over a collection of prior records that pair commercial descriptions with assigned codes. For each normalized query, the retriever computes a score between the query and historical records and orders the records from highest to lowest score. The experimental instantiation uses BM25 for this operation, but the architecture requires only a retrieval function that returns an ordered record-level result with reproducible scores and traceable source records; it does not require BM25 for every possible re-instantiation.

The record-level ranking retains the historical precedent behind each hit. Candidate construction then traverses that ordered list and maps records to their associated codes. If several retrieved records share the same code, only the first occurrence contributes a new code candidate. Because that first occurrence is the highest-ranked record for that code, it is retained as the primary historical precedent associated with the candidate. Subsequent records with the same code do not occupy additional candidate positions. The code-level ranking thus contains unique candidates while preserving a direct link from each candidate to the historical record that caused it to enter the ranking.

This procedure produces a Top-k ranking of unique code candidates whose order is inherited from the ranked historical records. Retrieval scores express match strength under the configured retrieval function; they are not probabilities of legal correctness and do not interpret the governing nomenclature. Normative documents do not participate in this ranking stage. Their later role is to provide identifiable documentary evidence for candidates that have already been produced by historical retrieval. The separation ensures that candidate generation remains attributable to the historical collection and its retrieval function.

## 3.4. Fixed candidate set

The fixed candidate set is obtained by taking the first three unique codes in the historical code-level ranking. These three codes, together with their rank positions and links to the supporting historical precedents, form the fixed Top-3 passed downstream. The boundary is procedural: after the Top-3 is formed, its membership and order remain unchanged in the primary flow.

Subsequent stages enrich rather than revise that set. Documentary retrieval can associate evidence with each of the three candidates, context construction can organize those materials, and the local LLM can generate a structured explanation of the alternatives. None of those operations changes which codes occupy ranks one through three. Any diagnostic reranking experiment is kept outside this primary path and cannot replace the fixed Top-3 used for downstream explanation.

Fixing the candidates at this point also defines the scope of evaluation. Candidate-retrieval measures assess the historical stage that produced the ranking, whereas documentary-association and explanation measures assess outputs created after the ranking has been fixed. A downstream stage therefore cannot improve or degrade the primary ranking by changing candidate membership or order. This boundary makes the origin of each output explicit without implying that a retrieved candidate is substantively or legally correct.

## 3.5. Candidate-specific documentary retrieval

The fixed Top-3 produced in Section 3.4 is the only candidate input to the documentary stage. The class space is not reopened at this point. Documentary retrieval is performed for each fixed candidate, or through an equivalent procedure that preserves the identity of the candidate associated with every retrieved item. Its output is therefore not a new ranking, but a set of candidate–evidence associations that can be inspected independently for ranks one, two, and three.

The retriever searches a documentary or normative corpus that is compatible with the instantiated code space and identified by version for that instantiation. Each retrieved item must remain linked to the candidate that triggered or received it and to an identifiable source, such as a document or fragment identifier together with the provenance needed to locate that source again. The architecture requires those links, but it does not prescribe a particular corpus, segmentation scheme, index, query strategy, or documentary top-N. Those implementation choices belong to the empirical instantiation.

This stage enriches the fixed candidates without changing them. It does not insert, remove, substitute, or reorder codes, and it does not recalculate the historical ranking. If documentary support is unavailable for a candidate, that absence does not authorize the stage to replace the candidate with another code. Conversely, retrieving an identifiable or formally authoritative passage does not by itself establish that the passage is pertinent, sufficient, or that the candidate is substantively or legally correct. The concrete source documents, temporal version, corpus preparation, retrieval index, parameters, and hashes used in the evaluation are specified in Section 4.

## 3.6. Evidence-context construction and controlled explanation

Context construction receives the normalized description or query, the fixed Top-3 with its unchanged rank positions, the available historical precedent associated with each candidate, and the documentary evidence retrieved for that candidate. It organizes these elements so that the evidence supplied for one alternative remains distinguishable from the evidence supplied for the other alternatives. The resulting context is the input package for explanation; it is not another candidate-selection stage.

The context records identifiers and provenance sufficient to reconstruct which evidence was supplied to the generator. At the architectural level, this means preserving the relation among the query, candidate code, fixed rank, historical support, documentary source or fragment, and the versioned resource from which that evidence was obtained. The exact serialization of those fields is implementation-specific, but the links must remain recoverable so that a reviewer can trace an explanatory statement back to the material supplied to the model.

The local LLM receives this assembled context only after the historical ranking and fixed Top-3 have been established. In the primary flow, it produces a controlled explanation of the three received alternatives. It must preserve candidate membership and order, must not introduce external codes or substitute candidates, and cannot feed information back into candidate generation or ranking. Any experiment in which an LLM reorders candidates is a separate diagnostic path and does not replace the fixed Top-3 used by the explanatory flow.

A structured and traceable explanation makes the relation between the generated text and its supplied evidence inspectable, but it does not establish substantive or legal correctness and does not demonstrate that the generated rationale is a faithful causal account of how the upstream ranking was produced. The exact model, version, prompt text, generation parameters, output schema, validators, and execution environment are properties of the experimental instantiation and are reported in Section 4.

## 3.7. Configurability and interface requirements

The procedure can be re-instantiated with a different labeled historical bank, a different target code space, and a different compatible documentary corpus. Replacing those resources is possible only when the interfaces required by the workflow are preserved. The commercial input must be representable as a reproducible normalized query; historical records must remain linkable to assigned codes and their provenance; and the historical retriever must return an ordered, traceable record-level result from which unique code candidates can be constructed and the Top-3 fixed before any downstream evidence or generation stage is invoked.

The documentary retriever must provide evidence that can be linked to individual fixed candidates through recoverable identifiers. Context construction must then preserve, for each candidate, its code and fixed position together with the available historical support, documentary evidence, and provenance. The generator must receive that fixed candidate set and its context while remaining restricted to explanation. A replacement model or prompting strategy is compatible with the architecture only if it cannot alter the upstream candidate set or order in the primary flow.

To reconstruct an execution, the resources that materially affect it must be identifiable and versioned when applicable. These include the historical data, documentary corpus, processing and retrieval code, configurations, model and prompt definitions, and other resources required to repeat or compare the run. The reproducibility repository supports this task by preserving and, where redistribution is permitted, distributing versioned configurations, scripts, manifests, hashes, instructions, and redistributable data or documentary resources. Section 4.11 records the concrete artifact inventory, identities, access conditions, and redistribution restrictions for the evaluated instantiation, while Section 4.3 documents the documentary corpus that feeds the explanation context, including its preparation, temporal validity, and retrieval index.

Under this separation, reproduction of the reference study concerns reconstructing the identified evaluated instantiation as closely as the available artifacts permit, whereas an external replication may supply independent data or replacement resources while retaining the same functional interfaces. Neither technical re-instantiation nor interface compatibility implies that the performance observed in one setting will transfer to another. Configurability is therefore a property of the procedure, not evidence of empirical generalization.

# 4. Experimental design

Only here should the manuscript move from the general architecture to
the specific empirical instantiation used to evaluate it.

## 4.1. Evaluation setting

Introduce the offline evaluation setting and the
regulatory/classification testbed. This is the appropriate place to
delimit NANDINA, the selected class/chapter and the non-binding
decision-support scope.

\[Section text to be drafted in a later approved version.\]

## 4.2. Historical data

### 4.2.1. Data source and selection

Document provenance and selection rules for the historical records used
in the experiment.

\[Section text to be drafted in a later approved version.\]

### 4.2.2. Target class space

Define the class/code universe actually represented in the evaluation.

\[Section text to be drafted in a later approved version.\]

### 4.2.3. Preparation and curation

Describe cleaning, normalization, inclusion/exclusion and curation
procedures.

\[Section text to be drafted in a later approved version.\]

### 4.2.4. Versioned datasets used in the experiment

Identify the frozen/versioned historical, development and evaluation
datasets used, including hashes or repository references where
appropriate.

\[Section text to be drafted in a later approved version.\]

## 4.3. Documentary corpus

### 4.3.1. Source documents and scope

Identify the documentary/normative sources that provide evidence to the
downstream retrieval stage.

\[Section text to be drafted in a later approved version.\]

### 4.3.2. Corpus preparation

Explain extraction, cleaning, segmentation/chunking and representation.

\[Section text to be drafted in a later approved version.\]

### 4.3.3. Versioning and temporal validity

Record the version/date boundary used for the experiment and how
normative drift is controlled or bounded.

\[Section text to be drafted in a later approved version.\]

### 4.3.4. Retrieval index

Describe how the corpus is indexed and queried for candidate-specific
evidence.

\[Section text to be drafted in a later approved version.\]

## 4.4. Partitioning and dependence control

Describe series-level observation, DAM-level grouping where dependence
exists, split construction, leakage controls, duplicates and
near-duplicate diagnostics.

\[Section text to be drafted in a later approved version.\]

## 4.5. System configuration

Report retrieval parameters, Top-k/Top-3 configuration, documentary
retrieval configuration, local LLM and inference settings, plus
software/hardware details that materially affect reproducibility.

\[Section text to be drafted in a later approved version.\]

## 4.6. Evaluation framework and research-question mapping

Map each RQ to system function, output, metric and permitted
interpretation. This is the main safeguard against conflating candidate
retrieval, documentary association and explanation quality.

\[Table placeholder — RQ → function → output → metric → permitted
interpretation.\]

\[Section text to be drafted in a later approved version.\]

## 4.7. Candidate-retrieval evaluation

Define Top-k/MRR and any other authorized retrieval metrics; specify the
evaluation unit and comparison logic.

\[Section text to be drafted in a later approved version.\]

## 4.8. Documentary-evidence evaluation

Define coverage/association/traceability criteria without treating
documentary association as substantive legal correctness.

\[Section text to be drafted in a later approved version.\]

## 4.9. Controlled-explanation evaluation

Describe the approved explanation/auditability rubric, dimensions,
scoring procedure and known limits.

\[Section text to be drafted in a later approved version.\]

## 4.10. Statistical analysis

Insert only the inferential design and tests that are finally authorized
by the experimental master plan. Do not anticipate pending Group 3
conclusions.

\[Section text to be drafted in a later approved version.\]

## 4.11. Reproducibility resources

Identify the public reproducibility repository and what it contains:
versioned data that can be redistributed, configurations, scripts,
manifests, hashes, instructions and declared non-redistributable or
unrecoverable items.

\[Section text to be drafted in a later approved version.\]

# 5. Results

Organize results by function/RQ, not by internal experiment codes or
execution chronology.

## 5.1. Data and partition checks

Report the controls that establish the validity of the benchmark and
partitions used for analysis.

\[Section text to be drafted in a later approved version.\]

## 5.2. Candidate retrieval performance

Primary RQ1 evidence: report authorized retrieval metrics and
comparisons. Do not label this as overall system accuracy.

\[Section text to be drafted in a later approved version.\]

## 5.3. Documentary evidence retrieval

Primary RQ2 evidence: report coverage, association, traceability and
preservation of candidate ranking as supported by the final evidence.

\[Section text to be drafted in a later approved version.\]

## 5.4. Controlled explanation quality

Primary RQ3 evidence: report the approved explanation/auditability
evaluation and its limits.

\[Section text to be drafted in a later approved version.\]

## 5.5. Sensitivity and robustness analyses

Include only sensitivity analyses that survive final experimental
reconciliation. Internal experiment IDs should be translated into
scientific headings.

\[Section text to be drafted in a later approved version.\]

## 5.6. Inferential results

Primary RQ4 evidence. Populate only after the relevant Group 3 analyses
are closed and authorized for article use.

\[Section text to be drafted in a later approved version.\]

## 5.7. Summary by research question

Optional compact synthesis if it improves readability. Use evidence,
main finding and permitted interpretation; omit if redundant with the
preceding subsections.

\[Section text to be drafted in a later approved version.\]

# 6. Discussion

Interpret results rather than repeat them. Keep limitations close to the
claims they qualify and consolidate them in the final subsection.

## 6.1. Separating candidate ranking from documentary evidence

\[Section text to be drafted in a later approved version.\]

## 6.2. Controlled use of the LLM for explanation

\[Section text to be drafted in a later approved version.\]

## 6.3. Comparison with prior work

\[Section text to be drafted in a later approved version.\]

## 6.4. Implications for auditable decision support

\[Section text to be drafted in a later approved version.\]

## 6.5. Configurability and transfer conditions

Explain what may be reconfigured and under which preconditions, while
preserving the distinction between architecture configurability and
empirical generalization.

\[Section text to be drafted in a later approved version.\]

## 6.6. Limitations

Consolidate benchmark/data limits, documentary-corpus and
normative-drift limits, explanation-evaluation limits, legal-validity
boundaries, external validity and reproducibility constraints.

\[Section text to be drafted in a later approved version.\]

# 7. Conclusion

Close on contribution → main evidence → scope → implication. Do not
introduce new results or new claims of external generalization.

\[Section text to be drafted in a later approved version.\]

# Data availability

Formal availability statement; should point to the public
reproducibility resources and clearly distinguish public, restricted and
non-redistributable materials.

\[Section text to be drafted in a later approved version.\]

# Code and reproducibility resources

Use as a separate statement only if retained in the final KBS submission
format; otherwise integrate with Data availability.

\[Section text to be drafted in a later approved version.\]

# CRediT authorship contribution statement

\[Section text to be drafted in a later approved version.\]

# Funding

\[Section text to be drafted in a later approved version.\]

# Declaration of competing interest

\[Section text to be drafted in a later approved version.\]

# Acknowledgements

\[Include only if applicable.\]

# References

\[Final reference list managed at submission stage according to the
current KBS requirements.\]

# Supplementary material

Include only if needed for extensive rubrics, configurations, tables or
supporting artifacts that should not remain in the main text.

\[Optional.\]

# PART II — Spanish semantic-control mirror

Esta parte replica la estructura de la Parte I para control semántico
interno. No sustituye al manuscrito inglés de publicación.

## Título

Se definirá al final. Debe priorizar la contribución
científica/arquitectónica; el dominio aduanero puede aparecer como
aplicación o testbed solo si mejora la precisión.

\[Título final por redactar cuando el manuscrito esté completo.\]

## Resumen

Secuencia recomendada: problema concreto → limitación → arquitectura
propuesta → evaluación → hallazgos principales → implicación delimitada.

\[Section text to be drafted in a later approved version.\]

## Palabras clave

\[5–7 palabras clave finales.\]

# 1. Introducción

El apoyo a la decisión en clasificación arancelaria parte de un problema concreto de información: una descripción comercial debe vincularse con un código dentro de una nomenclatura jerárquica y, al mismo tiempo, quien revisa la recomendación puede necesitar material documental que explique por qué un candidato es pertinente. Los sistemas automáticos atienden partes distintas de este problema. Algunos modelos seleccionan un código directamente, otros producen candidatos ordenados, otros recuperan texto regulatorio o del manual y otros generan una justificación o una traza. Estas funciones están relacionadas, pero no producen la misma salida ni tienen la misma autoridad sobre la recomendación final. En un flujo de apoyo a decisiones auditable, por tanto, importa no solo qué técnicas se utilizan, sino también qué etapa puede determinar el conjunto de candidatos, qué etapa únicamente lo documenta y qué etapa solo explica un resultado ya fijado.

Los antecedentes muestran distintas formas de acoplar estas funciones. Lee et al. (2021) predicen un heading, recuperan oraciones clave del manual HS y luego utilizan la descripción del producto junto con esas oraciones para predecir la subpartida; por ello, el material recuperado participa en la decisión de clasificación posterior. Lee et al. (2023) separan la secuencia de otra manera: su sistema predice candidatos de clasificación antes de recuperar del manual HS evidencia sobre cada candidato, lo que demuestra que la predicción de candidatos seguida de soporte documental ya existe en el apoyo a decisiones aduaneras. La búsqueda guiada por regulación puede otorgar todavía mayor influencia a la evidencia recuperada: Wang et al. (2026) construyen paquetes de candidatos enriquecidos con evidencia y utilizan un modelo de decisión para seleccionar cada siguiente salto dentro de una jerarquía regulatoria antes de agregar la evidencia para la justificación final. En IA jurídica, Chen y Tanaka-Ishii (2026) recuperan fuentes legales y ejemplos, los compilan en una representación ejecutable y refinan esa representación como parte del proceso que produce la etiqueta. Estos trabajos constituyen antecedentes cercanos y parciales de la combinación entre recuperación, evidencia y explicación; la limitación abordada aquí no consiste, por tanto, en afirmar la ausencia de esos componentes.

El problema metodológico restante se refiere a la separación operacional y evaluativa. Cuando varias etapas posteriores pueden modificar el mismo conjunto de candidatos, quien revisa la salida no puede determinar con facilidad si un candidato fue seleccionado por la evidencia histórica, por el material regulatorio o por el modelo de lenguaje. Ese acoplamiento también dificulta la evaluación: una métrica de ranking de candidatos mide un objeto distinto de la asociación documental, y ninguna de las dos mide la estructura o trazabilidad de una explicación generada. Si estas salidas se reportan como si describieran una única decisión indiferenciada del sistema, resulta difícil atribuir un resultado observado al componente que realmente lo produjo. En un contexto regulado, esta distinción también es relevante para la revisión humana: asociar a un candidato un pasaje oficial o pertinente no establece corrección jurídica sustantiva, y producir una explicación estructurada no convierte al modelo de lenguaje en el clasificador que seleccionó el código.

Este estudio examina una arquitectura de apoyo a decisiones que hace explícitas esas fronteras. Una etapa de recuperación histórica recibe la descripción comercial normalizada, genera códigos candidatos desde un banco histórico etiquetado y fija su ranking. Los tres candidatos mejor posicionados forman un Top-3 fijo antes de que comience la recuperación normativa. Una etapa separada de recuperación normativa asocia después evidencia documental con cada uno de esos candidatos sin insertar, eliminar, sustituir ni reordenar códigos. Finalmente, un LLM local downstream recibe los candidatos fijados y su contexto documental recuperado para producir una explicación controlada; no tiene autoridad para modificar los candidatos ni retroalimentar la clasificación. La arquitectura trata, por ello, el ranking de candidatos, la asociación documental y la explicación como salidas distintas que pueden inspeccionarse y evaluarse por separado.

El artículo plantea tres contribuciones acotadas. Primero, especifica un procedimiento que asigna una función concreta a cada componente. La recuperación histórica genera y ordena candidatos y fija el Top-3; la recuperación normativa asocia después evidencia con esos candidatos ya fijados sin cambiar su composición ni su orden; y el LLM local genera únicamente la explicación de ese Top-3 fijo. Segundo, evalúa la recuperación de candidatos, la asociación documental y la explicación controlada como salidas distintas, preservando el agrupamiento a nivel de DAM cuando la estructura compartida de una declaración introduce dependencia. Tercero, documenta las interfaces y los recursos de reproducibilidad necesarios para reinstanciar el procedimiento con otro banco histórico etiquetado, otro espacio de clases objetivo o un corpus documental compatible. Esta tercera contribución se refiere a la reproducibilidad y reinstanciación del procedimiento; no implica que el desempeño observado en un escenario empírico se transfiera a otro.

La evaluación empírica utiliza un testbed aduanero offline para la recomendación de subpartidas NANDINA dentro del alcance delimitado de la Clase/Capítulo 87. La descripción comercial de una SERIE se utiliza como consulta después de la normalización; la SERIE es la unidad de análisis y la DAM/declaración aduanera es la unidad de agrupamiento cuando debe controlarse dependencia. La implementación combina un banco histórico etiquetado, un corpus normativo/documental, recuperación histórica de candidatos, recuperación normativa específica por candidato y un LLM local restringido a explicar el Top-3 fijo. El testbed es no vinculante y sirve para analizar la arquitectura, no para definir su alcance conceptual. El mismo procedimiento puede reinstanciarse con otros datos, espacios de clases y corpus documentales cuando se satisfacen las interfaces y controles de procedencia requeridos, pero esa configurabilidad no constituye evidencia de generalización empírica fuera del escenario evaluado.

La evaluación se guía por cuatro preguntas de investigación:

- **RQ1.** ¿Qué desempeño de recuperación de candidatos alcanza la recuperación histórica bajo particiones disjuntas por DAM/declaración aduanera?
- **RQ2.** ¿En qué medida puede asociarse evidencia normativa identificable a cada candidato de un Top-3 histórico fijo sin alterar el orden de los candidatos?
- **RQ3.** ¿En qué medida un LLM local restringido al Top-3 fijo puede preservar los candidatos y su orden y, al mismo tiempo, producir explicaciones estructuradas vinculadas con evidencia identificable?
- **RQ4.** ¿Qué límites de validez introducen la dependencia intra-DAM, los near-duplicates residuales, la composición del banco histórico y el drift normativo al interpretar los resultados del piloto offline?

El resto del artículo se organiza del siguiente modo. La Sección 2 revisa clasificación arancelaria automatizada, recuperación enriquecida con conocimiento, funciones de los LLM, fundamentación en evidencia, auditabilidad, reproducibilidad y el posicionamiento del estudio. La Sección 3 describe la arquitectura de apoyo a decisiones y su flujo de información. La Sección 4 presenta el diseño experimental, los recursos de datos y documentos, el particionamiento, la configuración del sistema, los protocolos de evaluación y los recursos de reproducibilidad. La Sección 5 reporta los resultados por función del sistema y pregunta de investigación, la Sección 6 discute sus implicaciones y limitaciones y la Sección 7 cierra el artículo dentro del alcance evaluado.

# 2. Trabajos relacionados

Organizar por función técnica y cerrar cada subsección con una síntesis
útil para el posicionamiento.

\[Section text to be drafted in a later approved version.\]

## 2.1. Clasificación arancelaria automatizada y recuperación de candidatos

La clasificación arancelaria automatizada se ha formulado con frecuencia
como un problema de predicción de texto a código: un modelo recibe la
descripción de un producto o una declaración y devuelve una o más
etiquetas HS. Los primeros trabajos abordaron esta tarea como
categorización supervisada de texto, con modelos entrenados sobre
declaraciones históricas y evaluados en un nivel definido de la
jerarquía arancelaria. Ding et al. emplearon un clasificador Background
Net para asignar el texto de declaraciones de mercancías a categorías
HS, lo que ejemplifica una formulación convencional de clasificación
directa (Ding et al., 2015). Trabajos posteriores con CNN mostraron que
las descripciones cortas podían clasificarse por separado en HS2 y HS4,
y también hicieron visible el aumento de cardinalidad de clases en
niveles más finos (Luppes, 2019). A mayor escala, Ruder comparó
clasificadores de aprendizaje automático convencional y redes neuronales
sobre más de un millón de descripciones de carga distribuidas entre
miles de clases HS6 (Ruder, 2020). Estos estudios comparten un objetivo
de predicción supervisada, pero difieren en nivel objetivo, espacio de
etiquetas, datasets y medidas de evaluación; por ello, sus porcentajes
reportados no deben interpretarse como medidas directamente comparables
del desempeño de clasificación arancelaria.

Trabajos posteriores han modificado la representación del texto
comercial sin cambiar necesariamente ese objetivo de predicción. Anggoro
et al., por ejemplo, ajustaron Sentence-BERT con Multiple Negative
Ranking loss para obtener embeddings de transacciones y utilizaron
después esas representaciones de longitud fija como entradas de
clasificadores SVM y Random Forest para predecir códigos HS (Anggoro et
al., 2025). Otros enfoques explotan de manera más explícita la
jerarquía. Lee et al. predicen primero un heading de cuatro dígitos,
recuperan oraciones pertinentes del manual HS y posteriormente predicen
la subpartida de seis dígitos a partir de la descripción del producto
junto con las oraciones recuperadas (Lee et al., 2021). Este diseño por
etapas difiere de tratar HS2, HS4 o HS6 como objetivos planos
independientes, porque la información producida entre niveles puede
participar en la decisión posterior.

Una segunda familia formula el problema como recuperación o ranking, en
lugar de una decisión de etiqueta única. Stassin et al. compararon
modelos neuronales supervisados con métodos de similitud semántica en
HS6, HS8 y HS10 y evaluaron si los códigos pertinentes aparecían en las
primeras posiciones de una salida ordenada (Stassin et al., 2023). Pain
también empleó similitud textual semántica para generar recomendaciones
ordenadas de mercancías y evaluó si el código esperado aparecía entre
las sugerencias Top-k (Pain, 2021). En esta formulación, la salida
inmediata del modelo es una lista de candidatos que puede apoyar una
decisión humana o automatizada posterior. Esta distinción es importante
en términos operativos: las métricas Top-k de recuperación evalúan la
presencia y el orden de candidatos, mientras que la accuracy de
clasificación evalúa una etiqueta seleccionada. Ambos objetivos pueden
coexistir en sistemas de asistencia arancelaria, pero sus métricas y
denominadores no deben tratarse como intercambiables.

Una tercera tarea parte de un código ya asignado y pregunta si esa
asignación es coherente o plausible. Spichakova y Haav combinan
similitud textual con similitud derivada de la taxonomía HS para evaluar
la corrección del código asignado y proporcionar predicciones o
recomendaciones alternativas (Spichakova & Haav, 2020). Esta validación
o corrección no equivale a generar candidatos desde una descripción sin
código, porque el código existente forma parte del objeto evaluado y la
evaluación depende de supuestos sobre las etiquetas históricas
utilizadas como referencia.

En conjunto, esta literatura abarca clasificación directa, predicción
jerárquica por etapas, recuperación/ranking de candidatos y validación
posterior a la asignación. Las fronteras entre estas tareas son
relevantes porque las mismas tecnologías —embeddings, codificadores
neuronales, funciones de similitud o registros históricos— pueden
sostener salidas y criterios de evaluación diferentes. También permiten
precisar el punto en que el conocimiento documental externo entra al
sistema: en algunos diseños participa en la propia decisión de
clasificación, mientras que en otros la recuperación se utiliza para
exponer material de respaldo alrededor de códigos candidatos. Esta
diferencia funcional prepara la siguiente subsección sobre recuperación
enriquecida con conocimiento y razonamiento regulatorio.

## 2.2. Recuperación enriquecida con conocimiento y razonamiento regulatorio

El conocimiento externo interviene en los sistemas arancelarios y
regulatorios de formas materialmente distintas. En algunos modelos, la
estructura del dominio forma parte del propio predictor, en lugar de ser
un documento recuperado después de producir un candidato. Qi et al.
transforman los elementos de la declaración en asociaciones semánticas y
de atributos, construyen un grafo de conocimiento y entrenan un modelo
de atención sobre grafos para formular la predicción del código HS como
una tarea de completado de enlaces en ese grafo (Qi et al., 2025). En
este caso, el conocimiento estructurado influye en la representación y
en la inferencia que producen el código. Esta función difiere de la
recuperación documental cuyo resultado se muestra como material de
respaldo, y también de la validación de un código ya asignado. La
distinción es importante porque un grafo de conocimiento, una taxonomía
y un pasaje recuperado pueden describirse como «conocimiento externo»
aunque intervengan en puntos diferentes del proceso de decisión.

La recuperación documental también puede participar directamente en la
clasificación. Lee et al. predicen primero un heading de cuatro dígitos,
recuperan oraciones clave del manual HS correspondiente y luego utilizan
la descripción del producto junto con esas oraciones para predecir la
subpartida de seis dígitos (Lee et al., 2021). Por tanto, las oraciones
recuperadas se convierten en entradas de la predicción posterior y no
únicamente en una explicación mostrada después de clasificar. Un diseño
relacionado de apoyo a decisiones aduaneras separa esas funciones de
otra manera: primero predice clasificaciones candidatas y después
recupera del manual HS evidencia sobre cada candidato, devolviendo
códigos candidatos junto con oraciones de respaldo pertinentes para que
los funcionarios las inspeccionen (Lee et al., 2023). Estos ejemplos
muestran por qué la recuperación de códigos, de oraciones, de
precedentes y de evidencia no debe reducirse a una única función. El
objeto recuperado y el momento en que ocurre la recuperación determinan
si esta genera candidatos, modifica una predicción o respalda la
revisión de una sugerencia existente.

La búsqueda guiada por regulación hace aún más explícito este
acoplamiento. En la búsqueda jerárquica consciente de restricciones, los
documentos regulatorios se organizan como un árbol consultable; en cada
nivel, el sistema recupera nodos hijos plausibles y evidencia de
respaldo, construye un paquete de candidatos y utiliza un modelo de
decisión para seleccionar el siguiente salto o detenerse (Wang et al.,
2026). Una vez fijada la ruta, la evidencia de los nodos visitados se
agrega para la verificación y la generación de la justificación. En este
contexto, el material regulatorio forma parte del recorrido que
determina la ruta de clasificación y no es simplemente una capa de citas
añadida a una etiqueta seleccionada de manera independiente. La misma
lectura funcional es necesaria en otros sistemas agénticos o
restringidos por reglas: la jerarquía, las exclusiones, las
redirecciones y las reglas recuperadas pueden restringir o modificar la
trayectoria de búsqueda. Una ruta consistente con la jerarquía o una
justificación respaldada por material recuperado puede hacer
inspeccionable el proceso de decisión, pero ninguna de esas propiedades
establece por sí sola una corrección jurídica adjudicada de manera
independiente ni una puntuación formal de auditabilidad.

La generación aumentada por recuperación ofrece un patrón más general
para acoplar texto externo con generación. Lewis et al. combinan un
recuperador neuronal sobre un índice documental no paramétrico con un
generador sequence-to-sequence; los documentos recuperados se
proporcionan como contexto adicional cuando se genera la secuencia
objetivo (Lewis et al., 2020). En esa formulación, recuperación y
generación son componentes de un único modelo probabilístico, y la
salida generada permanece condicionada tanto por la entrada como por los
pasajes recuperados. Por ello, RAG no debe utilizarse como sinónimo de
todo sistema que recupere documentos: retrieve-then-generate, la
recuperación usada dentro de una clasificación y la recuperación de
evidencia para inspección humana asignan funciones diferentes al
material recuperado. Del mismo modo, un pasaje inspeccionable no
constituye automáticamente una atribución completa de cada afirmación
generada, ni la recuperación por sí sola garantiza que la salida esté
fundamentada en la fuente gobernante.

La transformación de la consulta ilustra otra frontera. Ma et al. sitúan
un reescritor antes de la recuperación: el sistema reescribe la entrada
como una consulta de búsqueda, recupera documentos y posteriormente
entrega esos documentos a un lector de caja negra; en su variante
entrenable, el reescritor se optimiza mediante retroalimentación del
lector (Ma et al., 2023). Dado que la reescritura cambia aquello que el
recuperador busca, puede cambiar el contexto posterior y la respuesta.
La consulta reescrita es, por tanto, una entrada de control para la
recuperación y no evidencia de la afirmación final. En términos más
generales, la reescritura de consultas, la recuperación documental, la
selección de pasajes y la generación son operaciones separables incluso
cuando una implementación las entrena o ejecuta conjuntamente.

En conjunto, la pregunta científicamente útil no es simplemente si un
sistema «usa conocimiento», sino qué hace ese conocimiento. Puede estar
codificado como estructura que participa en la predicción, recuperarse
como contexto que modifica una decisión posterior, utilizarse como
reglas o restricciones durante una búsqueda jerárquica o presentarse
como material de respaldo para revisión humana. Estas funciones implican
salidas y objetivos de evaluación distintos, y las citas visibles o las
trazas de razonamiento no deben tratarse como sustitutos de la
verificación fuente-afirmación ni de la corrección sustantiva. Esta
separación funcional también aclara el siguiente problema: una vez
disponibles la recuperación y el contexto regulatorio, un LLM todavía
puede desempeñar funciones muy diferentes, como clasificador,
controlador de búsqueda, lector/razonador o generador de explicaciones.
Esas funciones se examinan en la siguiente subsección.

## 2.3. LLM para clasificación, razonamiento y explicación

La etiqueta «LLM» abarca sistemas que otorgan al modelo de lenguaje
grados de autoridad muy distintos. Algunos modelos seleccionan
directamente un código arancelario a partir de la descripción de un
producto; otros son codificadores ajustados que devuelven una clase
dentro de un espacio fijo de etiquetas; y los sistemas aumentados por
recuperación o agénticos pueden permitir que el modelo controle la
búsqueda, compare candidatos o produzca una justificación después de que
decisiones anteriores ya hayan restringido el resultado. Por ello, la
distinción relevante no es el tamaño ni la denominación del modelo, sino
qué decisión se le permite tomar y qué salidas previas puede modificar.

La clasificación generativa directa concede al modelo una amplia
autoridad sobre el código predicho. Marra de Artiñano et al. consultan
GPT-3.5 mediante prompts directos a través de la API para categorizar
los productos individualmente, sin entrenar GPT-3.5 con los datasets
aduaneros utilizados para ajustar los baselines de aprendizaje
automático convencional (Marra de Artiñano et al., 2023). En este caso,
el propio modelo transforma la descripción en la etiqueta arancelaria.
Esta configuración debe distinguirse de los estudios que utilizan la
expresión «large language model» para referirse a codificadores
transformer supervisados. Koch y Power ajustan modelos transformer con
descripciones etiquetadas de manifiestos de carga para clasificar
códigos HS; su comparación experimental incluye modelos de las familias
BERT y RoBERTa entrenados para la misma tarea de clasificación (Koch &
Power, 2025). En estos sistemas, el transformer aporta representaciones
contextuales dentro de un clasificador supervisado, en lugar de generar
libremente un código mediante prompting. Por tanto, la clasificación
generativa directa y la clasificación con transformers ajustados imponen
restricciones diferentes al modelo, aunque ambas se describan como
basadas en LLM.

La recuperación cambia nuevamente la función del modelo cuando el
material recuperado se convierte en contexto para el LLM que determina
el código. Kim et al. proponen THE-RAG, un framework de dos etapas que
combina recuperación densa, BM25 y reranking, y evalúa cómo el
preprocesamiento para recuperación y la capacidad de comprensión de
oraciones del modelo de lenguaje afectan la calidad de la clasificación
HS (Kim et al., 2025). En esta configuración, el LLM funciona como
lector condicionado por recuperación y como decisor: el contexto
recuperado interviene en la clasificación final, en lugar de limitarse a
documentar un código seleccionado en otra etapa. Esta función difiere
del RAG para QA documental, donde el objeto generado es la respuesta a
una pregunta, y de la recuperación de evidencia de apoyo, en la que los
pasajes pueden mostrarse alrededor de candidatos sin otorgar al
generador autoridad para alterar su selección.

Los diseños agénticos pueden ampliar la autoridad del modelo más allá de
la lectura de pasajes recuperados. En un preprint de 2026, Nguyen et al.
combinan recuperación multiagente de información, búsqueda semántica
sobre documentos arancelarios oficiales, razonamiento respaldado por
evidencia, validación por consenso, votación elemento por elemento,
estimación de confianza y escalamiento human-in-the-loop para
clasificación canadiense a diez dígitos (Nguyen et al., 2026). En un
flujo de este tipo, las salidas de los modelos y la evidencia recuperada
participan en el propio procedimiento de clasificación. El consenso o la
autoconsistencia pueden estabilizar ese procedimiento o expresar acuerdo
entre ejecuciones o modelos, pero el acuerdo no constituye ground truth
independiente. Del mismo modo, el escalamiento basado en confianza
modifica el tratamiento de los casos inciertos, pero no establece por sí
mismo que el código seleccionado sea sustantiva o jurídicamente
correcto.

Otra separación aparece cuando el modelo participa primero en la
búsqueda y genera una justificación solo después de que la ruta de
decisión ha quedado fijada. En otro preprint de 2026, Wang et al.
proponen una búsqueda jerárquica consciente de restricciones en la que
un LLM ayuda a elegir cada siguiente salto entre nodos hijos recuperados
localmente y evidencia regulatoria de respaldo. Una vez fijada la ruta
jerárquica, la evidencia de los nodos visitados se agrega para la
verificación final y la generación de la justificación (Wang et al.,
2026). Por tanto, la etapa posterior de justificación ocurre después de
una ruta fija, pero el mismo sistema general utilizó un LLM y evidencia
regulatoria para construir esa ruta. Esto es funcionalmente distinto de
tratar el control de búsqueda, el reranking o la selección del siguiente
salto como generación exclusivamente explicativa. También muestra por
qué una justificación o una traza de razonamiento no debe asumirse como
una representación fiel de la base causal de la decisión precedente
únicamente porque se produzca después de ella.

En estas configuraciones, la autoridad del LLM abarca desde seleccionar
directamente el código, operar dentro de un clasificador supervisado,
leer contexto recuperado conservando autoridad decisoria y dirigir
búsqueda o consenso, hasta generar texto explicativo después de que
decisiones previas hayan restringido la salida disponible. Estas
funciones implican modos de fallo y necesidades de evaluación
diferentes. El desempeño de clasificación no permite establecer la
fidelidad de una justificación; una traza de razonamiento visible no
demuestra por sí sola respaldo fuente-afirmación; y las citas o los
metadatos de procedencia no establecen auditabilidad formal ni
corrección jurídica. Estas distinciones preparan la siguiente
subsección, que examina cómo deben evaluarse la fundamentación en
evidencia, la explicabilidad y la auditabilidad cuando una salida
generada por un LLM se vincula con evidencia recuperada o con una traza
explícita de decisión.

## 2.4. Fundamentación en evidencia, explicabilidad y auditabilidad

La fundamentación en evidencia debe evaluarse como una relación entre
una salida y la evidencia, y no como la mera presencia de texto
recuperado. La generación aumentada por recuperación permite que el
generador se condicione por memoria no paramétrica y puede mejorar el
acceso a conocimiento externo actualizable y hacer inspeccionables los
pasajes recuperados para su verificación (Lewis et al., 2020). Sin
embargo, el generador sigue combinando la entrada, los pasajes
recuperados y su modelo paramétrico; la recuperación por sí sola no
demuestra que cada afirmación de la salida esté respaldada por una
fuente.

Asai et al. hacen explícita esta distinción: un pasaje puede contener la
cadena de una respuesta y aun así carecer de evidencia, por lo que su
modelo de evidencialidad predice si el pasaje respalda la salida de
referencia en lugar de tratar la recuperación o el solapamiento léxico
como respaldo (Asai et al., 2022). Por tanto, el grounding exige evaluar
la relación de soporte entre una afirmación y el material presentado
como evidencia.

La explicabilidad responde a otra pregunta: qué información se expone
para ayudar a una persona a comprender o revisar una recomendación. En
apoyo a decisiones aduaneras, Lee et al. primero predicen
clasificaciones candidatas y después recuperan oraciones pertinentes del
manual HS, presentando los códigos candidatos junto con esas oraciones
como evidencia explicativa (Lee et al., 2023). Este diseño hace visible
el respaldo documental para quien revisa la recomendación, pero la
visibilidad y la interpretabilidad no establecen por sí solas que cada
afirmación explicativa esté implicada por el pasaje citado. La misma
frontera se aplica de forma más general a las justificaciones y trazas
de razonamiento. Una justificación puede organizar información alrededor
de una decisión y, aun así, requerir una prueba separada de fidelidad si
se pretende que represente la base sobre la cual se llegó realmente a
esa decisión.

La procedencia y la trazabilidad responden a otra pregunta: de dónde
provino una salida y qué objetos u operaciones contribuyeron a
producirla. FAIR Data Pipeline, por ejemplo, registra datos y metadatos
a medida que los análisis consumen y producen objetos de investigación y
puede rastrear salidas científicas a través del código de modelado o
análisis hasta los datos primarios (Mitchell et al., 2022). Ese lineage
puede hacer inspeccionables las dependencias, versiones y
transformaciones. Sin embargo, no establece que los datos fuente, la
transformación, la interpretación o la salida final sean sustantivamente
correctos. La trazabilidad constituye, por tanto, evidencia sobre la
ruta de producción de un artefacto y no un dictamen de corrección sobre
el propio artefacto.

La auditabilidad también puede referirse a alcances distintos. Raji et
al. proponen un framework de auditoría algorítmica interna aplicado
durante todo el ciclo de desarrollo organizacional, donde cada etapa de
la auditoría produce documentos que, en conjunto, forman un informe de
auditoría (Raji et al., 2020). Este tipo de auditoría del ciclo de vida
reconstruye decisiones de diseño, riesgos, actividades de prueba y
responsabilidad organizacional a lo largo del tiempo. A nivel de una
salida individual, una cuestión de revisión distinta es si esa salida
puede examinarse contra criterios explícitos utilizando la evidencia y
la traza asociadas. Un registro del ciclo de vida puede apoyar esa
revisión, pero no equivale a una revisión caso por caso, del mismo modo
que un paquete de evidencia por caso no reconstruye todo el ciclo de
desarrollo.

Los sistemas regulatorios añaden la autoridad y vigencia de las fuentes
como dimensiones adicionales. Los criterios ilustrativos de Grainger
para herramientas arancelarias electrónicas incluyen la capacidad de
incorporar actualizaciones arancelarias, remitir a guías autoritativas,
aplicar reglas de clasificación y proporcionar una declaración que
explique la recomendación (Grainger, 2024). Estas capacidades son
relevantes porque una explicación construida con un documento obsoleto o
no autoritativo puede ser trazable y, aun así, resultar inadecuada para
el contexto decisorio vigente. A la inversa, citar una fuente oficial y
actual no establece que se haya seleccionado la disposición pertinente
ni que esta se haya interpretado correctamente para un caso concreto. La
autoridad y vigencia documental son, por tanto, dimensiones relevantes
que deben examinarse en apoyo a decisiones reguladas, pero permanecen
separadas de la corrección sustantiva o jurídica.

En conjunto, grounding, explicación, procedencia, auditoría del ciclo de
vida, revisión a nivel de salidas individuales y autoridad de las
fuentes responden a preguntas de verificación diferentes. No deben
ordenarse como una escalera de madurez en la que una propiedad garantice
la siguiente. Un sistema puede mostrar fuentes sin demostrar respaldo de
afirmaciones, conservar lineage sin probar corrección o mantener un
audit trail sin validar cada salida. A la inversa, una salida individual
bien respaldada no establece la reproducibilidad del sistema o del
dataset en su conjunto. Una vez separados estos constructos, la
evaluación puede asignar a cada uno un protocolo y una métrica
apropiados; la siguiente subsección aborda, por ello, la
reproducibilidad y la evaluación en sistemas de apoyo a decisiones
basados en conocimiento.

## 2.5. Reproducibilidad y evaluación en apoyo a decisiones basado en conocimiento

Una vez separadas la fundamentación, la explicación, la procedencia y el alcance de la auditoría, una evaluación reproducible exige también que sean inspeccionables los objetos experimentales que sustentan un resultado reportado. La documentación del dataset constituye una parte de ese requisito. Bender y Friedman definen un data statement como una caracterización que aporta contexto para juzgar cómo podrían generalizarse los resultados experimentales, cómo podría desplegarse el software y qué sesgos podrían reflejarse en los sistemas construidos a partir de los datos (Bender & Friedman, 2018). Gebru et al. amplían esta documentación a lo largo del ciclo de vida del dataset al organizar los datasheets en torno a motivación, composición, recopilación, preprocesamiento y etiquetado, usos, distribución y mantenimiento (Gebru et al., 2021). Estos registros hacen visibles los supuestos y el contexto del dataset, pero la documentación no constituye una certificación de calidad, representatividad, independencia ni ausencia de leakage. Esas propiedades requieren evidencia separada y, cuando corresponda, controles explícitos.

La documentación del dataset también debe distinguir los metadatos descriptivos de la identidad técnica. Un datasheet puede registrar relaciones entre instancias y particiones de datos recomendadas, lo que ayuda a reconstruir cómo se pretendía utilizar un dataset, pero registrar una partición no ejecuta por sí mismo control de dependencia ni demuestra que las particiones sean independientes (Gebru et al., 2021). La computación reproducible se beneficia además de identificar las versiones concretas de los datos, el código de procesamiento, los parámetros y otros objetos de investigación utilizados en una ejecución. FAIR Data Pipeline ilustra esta relación de lineage más fuerte: anota los datos a medida que los análisis los consumen y puede rastrear las salidas científicas, a través del código analítico o de modelado, hasta los datos primarios (Mitchell et al., 2022). La procedencia responde, por tanto, qué objetos y transformaciones contribuyeron a una salida. No establece que esas entradas, transformaciones o salidas sean sustantivamente correctas, y una cadena de procedencia por sí sola no equivale a reproducibilidad completa.

La reproducibilidad también requiere declarar una convención terminológica. Pineau et al. distinguen explícitamente varios conceptos relacionados: bajo la terminología adoptada en su estudio, el trabajo reproducible repite un experimento con los mismos datos y herramientas analíticas; el trabajo replicable cambia los datos y mantiene las herramientas; el trabajo robusto conserva los datos pero cambia el análisis; y el trabajo generalizable cambia tanto los datos como las herramientas analíticas y alcanza las mismas conclusiones (Pineau et al., 2021). Estas etiquetas no deben tratarse como nomenclatura universal, pero la separación resulta metodológicamente útil. Reproducir un resultado reportado bajo condiciones estrechamente equivalentes no demuestra por sí mismo robustez frente a otra implementación, replicación con datos distintos ni generalización fuera del escenario evaluado. Del mismo modo, hacer disponibles el código y los datos puede facilitar la reproducción sin garantizar que otro investigador consiga reproducir el resultado.

La trazabilidad a lo largo del proceso de desarrollo cumple otra función. Raji et al. describen un framework de auditoría algorítmica interna aplicado durante el ciclo de desarrollo organizacional, en el que cada etapa de la auditoría produce documentos que, en conjunto, forman un informe de auditoría (Raji et al., 2020). Estos artefactos pueden conservar decisiones de diseño, pruebas, riesgos e información de responsabilidad que una cifra final de desempeño no permite reconstruir. Sin embargo, su alcance está orientado al ciclo de vida. Un audit trail interno documentado no constituye automáticamente una revisión formal de cada salida individual ni establece corrección sustantiva o jurídica.

Estas distinciones tienen una consecuencia directa para el diseño de evaluación: la métrica debe corresponder a la función y a la salida que se evalúan. Pineau et al. identifican la especificación insuficiente de las métricas reportadas, el uso inadecuado del análisis estadístico y el overclaiming más allá de la evidencia presentada entre los obstáculos recurrentes para la investigación reproducible en aprendizaje automático (Pineau et al., 2021). En sistemas basados en conocimiento con varias etapas, este problema se amplifica porque la recuperación, el ranking, la selección de evidencia, la clasificación y la explicación pueden producir objetos diferentes. Una métrica de recuperación describe un conjunto ordenado bajo una definición concreta de relevancia; una métrica de clasificación describe etiquetas seleccionadas; una medida de evidencia se refiere al respaldo recuperado; y una medida de explicación se refiere a propiedades de las justificaciones generadas o presentadas. Especificar correctamente una métrica es, por tanto, necesario pero no suficiente para comparar: métricas alineadas no vuelven equivalentes tareas, datasets, juicios de relevancia ni semánticas de salida diferentes.

En consecuencia, la evaluación reproducible depende de una cadena de relaciones explícitas y no de un único indicador principal: se documentan el dataset y su uso previsto; se identifican los objetos y versiones concretos del experimento; se puede rastrear la ruta de producción de las salidas; el claim de reproducibilidad declara qué condiciones se mantienen o cambian; y cada métrica se interpreta únicamente para la función que realmente mide. Estos controles mejoran la inspeccionabilidad de la evidencia sin convertir documentación en certificación de calidad, lineage en corrección, reproducibilidad en generalización ni alineación de métricas en equivalencia de tareas. Establecidos estos límites de evaluación, la literatura restante puede compararse en función de cómo combina o mantiene separadas estas funciones, que es el propósito de la subsección siguiente.

## 2.6. Posicionamiento del estudio

La literatura revisada asigna niveles de autoridad materialmente distintos a la clasificación, la recuperación, la evidencia regulatoria y la generación. En un diseño aduanero por etapas, un modelo predice primero un heading de cuatro dígitos, recupera oraciones clave del manual HS correspondiente y luego predice la subpartida de seis dígitos a partir de la descripción del producto junto con esas oraciones recuperadas (Lee et al., 2021). Por tanto, la recuperación en ese pipeline no funciona únicamente como una capa explicativa posterior a la decisión: el material recuperado se convierte en una entrada de la predicción posterior. Esta distinción es relevante para el posicionamiento porque sistemas que emplean componentes similares pueden implementar procesos de decisión diferentes según el momento en que entra la evidencia y si esta puede afectar la etiqueta seleccionada.

Un antecedente aduanero más cercano separa de forma más explícita la predicción de candidatos del soporte documental. Lee et al. (2023) describen un modelo que predice candidatos de subpartida y posteriormente recupera del manual HS oraciones pertinentes como evidencia de respaldo para esos candidatos. Su salida combina, en consecuencia, códigos candidatos con material documental inspeccionable, lo que muestra que la predicción de candidatos acompañada de recuperación de evidencia ya constituye prior art y no puede, por sí sola, diferenciar el presente estudio. La distinción restante se refiere a la autoridad y a la secuencia: si el ranking de candidatos queda fijado de manera independiente antes de la recuperación documental, si los componentes posteriores pueden modificar ese ranking y si la generación forma parte de la clasificación o se restringe a explicar un resultado producido upstream.

Los sistemas regulatorios y de IA jurídica muestran un acoplamiento mayor entre evidencia, búsqueda y toma de decisiones. Wang et al. (2026) recuperan nodos hijos plausibles y evidencia de respaldo en cada nivel de una jerarquía regulatoria, y luego emplean un modelo de decisión para seleccionar el siguiente salto; solo después de fijar la ruta se agrega la evidencia para la verificación final y la generación de la justificación. Chen y Tanaka-Ishii (2026) ofrecen otro ejemplo orientado a auditoría: las fuentes jurídicas y los ejemplos recuperados se compilan en una representación ejecutable cuyo refinamiento continúa formando parte del proceso que produce la etiqueta final, y el modelo puede revisar el programa o emitir una consulta de recuperación adicional. Estos enfoques hacen más inspeccionables las rutas de decisión y el respaldo de fuentes, pero también muestran que los artefactos orientados a explicación pueden seguir acoplados al mecanismo que construye la decisión.

Frente a este prior art, el presente estudio se posiciona por la separación completa de la autoridad de sus componentes, no por la presencia aislada de recuperación histórica, evidencia documental o un LLM. Una etapa externa de recuperación histórica fija el ranking de candidatos y un Top-3 fijo antes de recuperar documentos normativos. La recuperación normativa queda entonces restringida a asociar evidencia con esos candidatos ya fijados; no puede insertar, eliminar, sustituir ni reordenarlos. Un LLM local downstream recibe únicamente los candidatos fijados y su contexto documental para producir una explicación, sin autoridad para modificar el conjunto de candidatos, alterar su orden ni retroalimentar la clasificación. Este contrato funcional describe el diseño objeto de estudio; no constituye, por sí mismo, una afirmación de que los componentes individuales o su combinación sean novedosos.

La lógica de evaluación mantiene la misma separación. El ranking de candidatos, la asociación documental y la explicación se tratan como salidas diferentes y se evalúan mediante medidas apropiadas para sus respectivas funciones, mientras se conserva el agrupamiento cuando una estructura compartida a nivel de declaración genera dependencia. Esto evita interpretar una métrica de recuperación como accuracy global de clasificación, tratar la asociación documental como corrección normativa sustantiva o equiparar la trazabilidad de una explicación con corrección jurídica. También separa la reproducibilidad del procedimiento evaluado de la generalización empírica más allá del escenario estudiado. El posicionamiento resultante es, por ello, deliberadamente acotado: el estudio examina una arquitectura de apoyo a decisiones en la que ranking, evidencia y explicación tienen autoridades explícitas y no superpuestas, y las secciones empíricas posteriores evaluarán esas funciones sin utilizar Related Work para anticipar sus resultados.

# 3. Arquitectura de apoyo a decisiones

Describir primero la arquitectura general. No abrir esta sección con
NANDINA, Capítulo 87, corpus peruano, H100 ni tamaños del experimento.

## 3.1. Vista general y flujo de información

La arquitectura separa la formación de candidatos de las etapas que documentan y explican esos candidatos. Una descripción comercial ingresa al flujo y se transforma en una consulta textual normalizada. La recuperación histórica utiliza esa consulta para buscar en una colección etiquetada de registros previos y produce un conjunto ordenado de códigos candidatos. Por tanto, el ranking de candidatos queda determinado antes de recuperar cualquier documento normativo y antes de invocar cualquier modelo generativo. Una vez seleccionados los tres primeros códigos únicos, estos forman el Top-3 fijo que se entrega a todo el procesamiento posterior.

[Figure 1 placeholder — overall architecture and information flow.]

Las etapas posteriores operan sobre ese conjunto fijo de candidatos y no sobre un espacio abierto de clases. La recuperación normativa específica por candidato asocia material documental con cada alternativa, y la construcción de contexto combina la consulta, la identidad de los candidatos, el respaldo histórico y la evidencia documental recuperada para la explicación posterior. El LLM local recibe ese contexto ensamblado únicamente después de que el Top-3 ha quedado fijado. Su salida es texto explicativo; no selecciona otro código, no modifica la composición del conjunto ni cambia el orden de los candidatos. Puede evaluarse una ruta separada de reordenamiento diagnóstico fuera del flujo principal, pero esta no retroalimenta el ranking utilizado por la arquitectura.

Esta secuencia produce tres salidas funcionalmente distintas. La recuperación histórica produce el ranking de candidatos y sus vínculos con precedentes históricos. La etapa documental produce asociaciones candidato–evidencia. La etapa generativa produce una explicación de los candidatos ya fijados utilizando el contexto suministrado. Mantener separadas estas salidas preserva la atribución: un código aparece en el Top-3 por la recuperación histórica, no porque un pasaje normativo o el modelo de lenguaje lo haya promovido posteriormente. También permite evaluar cada salida según la función que la produjo, en lugar de tratar el flujo como un único clasificador indiferenciado.

## 3.2. Representación y normalización de la consulta

La interfaz de recuperación recibe una representación textual derivada de la descripción comercial. La normalización convierte la descripción de origen en una representación determinista de consulta, de modo que una misma entrada, bajo el mismo procedimiento de preprocesamiento configurado, produce el mismo texto que se entrega a la recuperación histórica. Esta transformación prepara el texto para la comparación; no consulta documentos normativos, no introduce códigos candidatos ni utiliza un modelo de lenguaje para reinterpretar la mercancía antes de recuperar candidatos.

A nivel arquitectónico, el requisito es la reproducibilidad de esta interfaz de consulta y no una receta particular de limpieza. El sistema debe conservar la relación entre la descripción de origen y la consulta normalizada y aplicar de manera consistente la transformación configurada a la colección histórica y a las consultas entrantes cuando el método de recuperación requiera representaciones comparables. Las operaciones exactas de normalización de caracteres, tokenización, concatenación de campos u otras decisiones de implementación pertenecen a la instanciación experimental y se especifican junto con la configuración de recuperación, en lugar de tratarse como propiedades universales de la arquitectura.

La consulta normalizada constituye, por tanto, el punto de transferencia entre la preparación de la entrada y la generación de candidatos. A partir de este punto, la recuperación histórica es responsable de determinar qué precedentes etiquetados presentan mayor correspondencia según la función de puntuación configurada. Ninguna etapa posterior de evidencia o explicación puede modificar retrospectivamente la consulta para cambiar el ranking principal de candidatos.

## 3.3. Recuperación histórica y ranking de candidatos

La recuperación histórica de candidatos opera sobre una colección de registros previos que vinculan descripciones comerciales con códigos asignados. Para cada consulta normalizada, el recuperador calcula una puntuación entre la consulta y los registros históricos y ordena los registros de mayor a menor puntuación. La instanciación experimental utiliza BM25 para esta operación, pero la arquitectura solo exige una función de recuperación que devuelva un resultado ordenado a nivel de registro, con puntuaciones reproducibles y registros fuente trazables; no exige BM25 para toda posible reinstanciación.

El ranking a nivel de registro conserva el precedente histórico que sustenta cada resultado. La construcción de candidatos recorre después esa lista ordenada y vincula los registros con sus códigos asociados. Cuando varios registros recuperados comparten el mismo código, solo la primera aparición incorpora un nuevo candidato. Como esa primera aparición corresponde al registro mejor posicionado para ese código, se conserva como precedente histórico principal asociado al candidato. Los registros posteriores con el mismo código no ocupan posiciones adicionales de candidato. De este modo, el ranking a nivel de código contiene candidatos únicos y mantiene un vínculo directo entre cada candidato y el registro histórico que hizo que ingresara al ranking.

El procedimiento produce un ranking Top-k de códigos candidatos únicos cuyo orden se hereda de los registros históricos ordenados. Las puntuaciones de recuperación expresan la fuerza de correspondencia bajo la función configurada; no son probabilidades de corrección jurídica ni interpretan la nomenclatura aplicable. Los documentos normativos no participan en esta etapa de ranking. Su función posterior consiste en aportar evidencia documental identificable para candidatos que ya fueron producidos por la recuperación histórica. Esta separación permite atribuir la generación de candidatos a la colección histórica y a su función de recuperación.

## 3.4. Conjunto fijo de candidatos

El conjunto fijo de candidatos se obtiene tomando los tres primeros códigos únicos del ranking histórico a nivel de código. Esos tres códigos, junto con sus posiciones y sus vínculos con los precedentes históricos de respaldo, forman el Top-3 fijo que se entrega a las etapas posteriores. La frontera es procedimental: después de formar el Top-3, su composición y su orden permanecen sin cambios en el flujo principal.

Las etapas posteriores enriquecen ese conjunto, pero no lo revisan. La recuperación documental puede asociar evidencia con cada uno de los tres candidatos, la construcción de contexto puede organizar esos materiales y el LLM local puede generar una explicación estructurada de las alternativas. Ninguna de esas operaciones cambia qué códigos ocupan las posiciones uno, dos y tres. Cualquier experimento diagnóstico de reordenamiento se mantiene fuera de esta ruta principal y no puede sustituir el Top-3 fijo utilizado para la explicación posterior.

Fijar los candidatos en este punto también delimita el alcance de la evaluación. Las medidas de recuperación de candidatos evalúan la etapa histórica que produjo el ranking, mientras que las medidas de asociación documental y de explicación evalúan salidas creadas después de fijar el ranking. Por ello, una etapa posterior no puede mejorar ni degradar el ranking principal modificando la composición o el orden de los candidatos. Esta frontera hace explícito el origen de cada salida sin implicar que un candidato recuperado sea sustantiva o jurídicamente correcto.

## 3.5. Recuperación documental específica por candidato

El Top-3 fijo producido en la Sección 3.4 es la única entrada de candidatos a la etapa documental. En este punto no se reabre el espacio de clases. La recuperación documental se ejecuta para cada candidato fijo, o mediante un procedimiento equivalente que conserve la identidad del candidato asociado con cada elemento recuperado. Su salida no es, por tanto, un nuevo ranking, sino un conjunto de asociaciones candidato–evidencia que pueden inspeccionarse por separado para las posiciones uno, dos y tres.

El recuperador consulta un corpus documental o normativo compatible con el espacio de códigos de la instanciación y cuya versión queda identificada para esa instanciación. Cada elemento recuperado debe permanecer vinculado con el candidato que originó o recibió la evidencia y con una fuente identificable, como un documento o fragmento, junto con la procedencia necesaria para localizar nuevamente esa fuente. La arquitectura exige conservar esos vínculos, pero no prescribe un corpus, una estrategia de segmentación, un índice, una estrategia de consulta ni un Top-N documental específicos. Esas decisiones pertenecen a la instanciación empírica.

Esta etapa enriquece a los candidatos fijos sin modificarlos. No inserta, elimina, sustituye ni reordena códigos y no recalcula el ranking histórico. Si un candidato no dispone de respaldo documental, esa ausencia no autoriza a sustituirlo por otro código. Del mismo modo, recuperar un pasaje identificable o formalmente autoritativo no demuestra por sí solo que ese pasaje sea pertinente o suficiente ni que el candidato sea sustantiva o jurídicamente correcto. Los documentos fuente concretos, su versión temporal, la preparación del corpus, el índice de recuperación, los parámetros y los hashes utilizados en la evaluación se especifican en la Sección 4.

## 3.6. Construcción de contexto y explicación controlada

La construcción de contexto recibe la descripción o consulta normalizada, el Top-3 fijo con sus posiciones sin cambios, el precedente histórico disponible para cada candidato y la evidencia documental recuperada para ese candidato. Estos elementos se organizan de modo que la evidencia suministrada para una alternativa permanezca diferenciada de la evidencia suministrada para las demás. El contexto resultante constituye el paquete de entrada para la explicación; no es una nueva etapa de selección de candidatos.

El contexto registra los identificadores y la procedencia necesarios para reconstruir qué evidencia fue suministrada al generador. A nivel arquitectónico, esto exige mantener la relación entre consulta, código candidato, posición fija, respaldo histórico, documento o fragmento documental y recurso versionado del que se obtuvo la evidencia. La serialización exacta de estos campos depende de la implementación, pero los vínculos deben poder recuperarse para que quien revise la salida pueda rastrear una afirmación explicativa hasta el material suministrado al modelo.

El LLM local recibe este contexto ensamblado únicamente después de que se han establecido el ranking histórico y el Top-3 fijo. En el flujo principal, produce una explicación controlada de las tres alternativas recibidas. Debe conservar los candidatos y su orden, no puede incorporar códigos externos ni sustituir candidatos y no puede retroalimentar la generación o el ranking de candidatos. Cualquier experimento en el que un LLM reordene candidatos constituye una ruta diagnóstica separada y no reemplaza el Top-3 fijo utilizado por el flujo explicativo.

Una explicación estructurada y trazable permite inspeccionar la relación entre el texto generado y la evidencia suministrada, pero no establece corrección sustantiva o jurídica ni demuestra que la justificación generada sea una representación causalmente fiel de cómo se produjo el ranking previo. El modelo exacto, su versión, el texto del prompt, los parámetros de generación, el esquema de salida, los validadores y el entorno de ejecución son propiedades de la instanciación experimental y se reportan en la Sección 4.

## 3.7. Configurabilidad y requisitos de interfaz

El procedimiento puede reinstanciarse con otro banco histórico etiquetado, otro espacio de códigos objetivo y otro corpus documental compatible. La sustitución de estos recursos solo es posible si se conservan las interfaces que requiere el flujo. La entrada comercial debe poder representarse mediante una consulta normalizada reproducible; los registros históricos deben permanecer vinculados con los códigos asignados y su procedencia; y el recuperador histórico debe devolver un resultado ordenado y trazable a nivel de registro, a partir del cual puedan construirse candidatos únicos y fijarse el Top-3 antes de invocar cualquier etapa posterior de evidencia o generación.

El recuperador documental debe producir evidencia que pueda vincularse con candidatos fijos individuales mediante identificadores recuperables. La construcción de contexto debe conservar después, para cada candidato, su código y posición fija junto con el respaldo histórico disponible, la evidencia documental y su procedencia. El generador debe recibir ese conjunto fijo de candidatos y su contexto y permanecer restringido a la explicación. Un modelo o una estrategia de prompting alternativos son compatibles con la arquitectura únicamente si no pueden modificar el conjunto ni el orden de candidatos definidos previamente en el flujo principal.

Para reconstruir una ejecución, los recursos que la afectan materialmente deben poder identificarse y versionarse cuando corresponda. Entre ellos se encuentran los datos históricos, el corpus documental, el código de procesamiento y recuperación, las configuraciones, las definiciones del modelo y del prompt y los demás recursos necesarios para repetir o comparar la corrida. El repositorio de reproducibilidad apoya esta tarea al conservar y, cuando la redistribución está permitida, distribuir configuraciones, scripts, manifiestos, hashes, instrucciones y datos o recursos documentales redistribuibles. La Sección 4.11 registra el inventario concreto de artefactos, sus identidades, condiciones de acceso y restricciones de redistribución de la instanciación evaluada, mientras que la Sección 4.3 documenta el corpus documental que alimenta el contexto de explicación, incluida su preparación, vigencia temporal e índice de recuperación.

Bajo esta separación, la reproducción del estudio de referencia busca reconstruir la instanciación evaluada identificada en la medida en que lo permitan los artefactos disponibles, mientras que una replicación externa puede utilizar datos independientes o recursos sustitutos conservando las mismas interfaces funcionales. Ni la reinstanciación técnica ni la compatibilidad de interfaces implican que el desempeño observado en un escenario se transfiera a otro. La configurabilidad es, por tanto, una propiedad del procedimiento y no evidencia de generalización empírica.

# 4. Diseño experimental

A partir de aquí se introduce la instanciación empírica concreta.

\[Section text to be drafted in a later approved version.\]

## 4.1. Entorno de evaluación

Aquí se delimita el testbed regulatorio, el alcance offline y el apoyo a
decisiones no vinculante.

\[Section text to be drafted in a later approved version.\]

## 4.2. Datos históricos

\[Section text to be drafted in a later approved version.\]

### 4.2.1. Fuente y selección de datos

\[Section text to be drafted in a later approved version.\]

### 4.2.2. Espacio de clases objetivo

\[Section text to be drafted in a later approved version.\]

### 4.2.3. Preparación y curación

\[Section text to be drafted in a later approved version.\]

### 4.2.4. Datasets versionados utilizados en el experimento

\[Section text to be drafted in a later approved version.\]

## 4.3. Corpus documental

\[Section text to be drafted in a later approved version.\]

### 4.3.1. Documentos fuente y alcance

\[Section text to be drafted in a later approved version.\]

### 4.3.2. Preparación del corpus

\[Section text to be drafted in a later approved version.\]

### 4.3.3. Versionado y validez temporal

\[Section text to be drafted in a later approved version.\]

### 4.3.4. Índice de recuperación

\[Section text to be drafted in a later approved version.\]

## 4.4. Particionamiento y control de dependencia

Serie como unidad de observación; DAM como agrupamiento cuando exista
dependencia; controles de leakage, duplicados y near-duplicates.

\[Section text to be drafted in a later approved version.\]

## 4.5. Configuración del sistema

\[Section text to be drafted in a later approved version.\]

## 4.6. Marco de evaluación y correspondencia con las preguntas de investigación

Mapear RQ → función → output → métrica → interpretación permitida.

\[Section text to be drafted in a later approved version.\]

## 4.7. Evaluación de recuperación de candidatos

\[Section text to be drafted in a later approved version.\]

## 4.8. Evaluación de recuperación de evidencia documental

\[Section text to be drafted in a later approved version.\]

## 4.9. Evaluación de explicaciones controladas

\[Section text to be drafted in a later approved version.\]

## 4.10. Análisis estadístico

Incorporar solo análisis cerrados y autorizados por el Plan Maestro
experimental.

\[Section text to be drafted in a later approved version.\]

## 4.11. Recursos de reproducibilidad

Identificar explícitamente el repositorio público y el alcance de sus
artefactos.

\[Section text to be drafted in a later approved version.\]

# 5. Resultados

Organizar por función/RQ, no por códigos internos de experimentos.

\[Section text to be drafted in a later approved version.\]

## 5.1. Controles de datos y particiones

\[Section text to be drafted in a later approved version.\]

## 5.2. Desempeño de recuperación de candidatos

No denominarlo accuracy global del sistema.

\[Section text to be drafted in a later approved version.\]

## 5.3. Recuperación de evidencia documental

\[Section text to be drafted in a later approved version.\]

## 5.4. Calidad de la explicación controlada

\[Section text to be drafted in a later approved version.\]

## 5.5. Análisis de sensibilidad y robustez

\[Section text to be drafted in a later approved version.\]

## 5.6. Resultados inferenciales

Completar solo cuando los análisis pertinentes de Grupo 3 estén cerrados
y autorizados.

\[Section text to be drafted in a later approved version.\]

## 5.7. Síntesis por pregunta de investigación

Opcional; conservar solo si mejora la lectura.

\[Section text to be drafted in a later approved version.\]

# 6. Discusión

Interpretar, comparar y delimitar; no repetir Resultados.

\[Section text to be drafted in a later approved version.\]

## 6.1. Separación entre ranking de candidatos y evidencia documental

\[Section text to be drafted in a later approved version.\]

## 6.2. Uso controlado del LLM para explicación

\[Section text to be drafted in a later approved version.\]

## 6.3. Comparación con trabajos previos

\[Section text to be drafted in a later approved version.\]

## 6.4. Implicaciones para apoyo a decisiones auditable

\[Section text to be drafted in a later approved version.\]

## 6.5. Configurabilidad y condiciones de transferencia

\[Section text to be drafted in a later approved version.\]

## 6.6. Limitaciones

Consolidar límites de datos, corpus, drift normativo, evaluación de
explicaciones, validez jurídica, validez externa y reproducibilidad.

\[Section text to be drafted in a later approved version.\]

# 7. Conclusión

Cerrar con aporte → evidencia principal → alcance → implicación.

\[Section text to be drafted in a later approved version.\]

# Disponibilidad de datos

\[Section text to be drafted in a later approved version.\]

# Código y recursos de reproducibilidad

\[Section text to be drafted in a later approved version.\]

# Declaración CRediT de contribución de autoría

\[Section text to be drafted in a later approved version.\]

# Financiamiento

\[Section text to be drafted in a later approved version.\]

# Declaración de conflictos de interés

\[Section text to be drafted in a later approved version.\]

# Agradecimientos

\[Section text to be drafted in a later approved version.\]

# Referencias

\[Section text to be drafted in a later approved version.\]

# Material suplementario

Opcional.

\[Section text to be drafted in a later approved version.\]
