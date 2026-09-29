# Editorial review — Front matter B02 / KBS identity signal and Title V03 requirement

## Español

```text
REVIEW_TYPE = TARGET_JOURNAL_IDENTITY_AND_TITLE_TO_SCOPE_AUDIT
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE
TARGET_JOURNAL = Knowledge-Based Systems
CORPUS = 34 AUTHOR-SUPPLIED ACCEPTED KBS ARTICLES

CURRENT_TITLE_V02 =
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support

CURRENT_TITLE_V02_TECHNICAL_AUDIT = PASS
CURRENT_TITLE_V02_KBS_CORPUS_OPERATIONAL_FIT = PASS
CURRENT_TITLE_V02_AUTHOR_DECISION = NOT_YET_GIVEN

EDITORIAL_QUESTION =
DOES_THE_TITLE_MAKE_THE_ARTICLE'S_KBS_RELEVANT_COMPUTATIONAL_OR_KNOWLEDGE_OBJECT_RECOGNIZABLE_AT_FIRST_READ?

VERDICT = REVISE_TITLE_TO_V03
```

### 1. Hallazgo del corpus

La revisión del corpus completo confirma que los títulos aceptados en *Knowledge-Based Systems* no están obligados a contener literalmente `AI`, `knowledge`, `machine learning` o `knowledge-based`.

Existen artículos aceptados cuyo título no usa esas palabras, por ejemplo:

- `Rule-based semantic hypergraph parsing from textual annotations`;
- `Selecting test problems from benchmark suites in constrained multiobjective optimisation`;
- `Factorized stochastic transport for composite degradation image restoration`.

Sin embargo, esos títulos siguen haciendo inmediatamente reconocible un objeto computacional, algorítmico, de representación, inferencia, optimización o aprendizaje que justifica la contribución dentro del ámbito de KBS.

En otros artículos el vínculo es explícito:

- `From entity-centric to goal-oriented graphs: Enhancing LLM knowledge retrieval in Minecraft`;
- `Operational fairness diagnostics for AI-based detection systems: Metrics and methodology`;
- `A knowledge-aware graph-based framework ...`;
- `Causal-Nest: A framework for automated causal discovery and inference`;
- títulos que explicitan LLMs, federated learning, transformers, neural networks, reinforcement learning, semantic graphs, learned indexes o artificial intelligence.

La regla editorial empírica observada no es "mencionar AI/knowledge", sino:

```text
THE_TITLE_SHOULD_MAKE_THE_KBS_RELEVANT_SCIENTIFIC_OBJECT_OR_MECHANISM
RECOGNIZABLE_BEFORE_THE_ABSTRACT
```

### 2. Reevaluación de V02

V02 comunica correctamente:

- el dominio: tariff classification decision support;
- la operación: separar candidate ranking, documentary evidence y explanation.

Pero, en una lectura sin contexto, no identifica con suficiente fuerza:

- que la contribución es una **arquitectura computacional**;
- que el sistema es **knowledge-based** en un sentido sustantivo y no meramente administrativo/documental.

El título podría ser leído, antes del Abstract, como diseño de procesos, gobernanza documental o metodología organizacional de apoyo a decisiones.

Por tanto:

```text
V02_TITLE_TO_ARTICLE_FIDELITY = PASS
V02_METHOD_OPERATION_VISIBILITY = PASS
V02_TASK_DOMAIN_VISIBILITY = PASS
V02_CONTRIBUTION_TYPE_VISIBILITY = PARTIAL
V02_KBS_IDENTITY_SIGNAL_AT_FIRST_READ = PARTIAL
```

### 3. ¿Es científicamente defendible "knowledge-based"?

Sí, con una frontera precisa.

No se adopta `knowledge-based` por coincidencia nominal con la revista.

El manuscrito ya utiliza de forma sustantiva:

- `knowledge-based decision support`;
- `multi-stage knowledge-based systems`;
- `knowledge-enhanced retrieval and regulatory reasoning`;
- la distinción entre conocimiento que participa en predicción, conocimiento recuperado como contexto, reglas/constraints y conocimiento presentado para revisión.

La arquitectura estudiada integra objetos de conocimiento identificables:

1. un banco histórico etiquetado con precedentes trazables;
2. un corpus documental/normativo versionado y candidate-specific;
3. relaciones explícitas candidate–evidence–provenance;
4. un contexto de explicación construido a partir de candidatos ya fijados y evidencia identificable;
5. un LLM local restringido a explicación sobre ese contexto, sin autoridad de ranking.

El artículo no presenta una única `knowledge base` simbólica clásica ni afirma razonamiento jurídico formal. Por ello, `knowledge-based` debe modificar el **decision-support architecture** completo y no implicar que el ranking histórico esté gobernado por el corpus normativo.

```text
KNOWLEDGE_BASED_AS_SYSTEM_LEVEL_CHARACTERIZATION = SUPPORTED
KNOWLEDGE_BASED_AS_CLAIM_OF_SYMBOLIC_EXPERT_SYSTEM = NOT_CLAIMED
KNOWLEDGE_BASED_AS_NORMATIVE_RANKING_AUTHORITY = NOT_CLAIMED
```

### 4. Formulación V03 recomendada

```text
TITLE_EN_V03 =
Knowledge-Based Decision-Support Architecture for Tariff Classification: Separating Candidate Ranking, Documentary Evidence, and Explanation

TITLE_ES_V03 =
Arquitectura basada en conocimiento para el apoyo a la decisión en clasificación arancelaria: separación del ranking de candidatos, la evidencia documental y la explicación
```

### 5. Razones editoriales

V03 hace visibles, en una sola lectura:

```text
CONTRIBUTION_TYPE = ARCHITECTURE
KBS_SCIENTIFIC_IDENTITY = KNOWLEDGE-BASED DECISION SUPPORT
APPLICATION_DOMAIN = TARIFF CLASSIFICATION
DISTINCTIVE_OPERATION =
SEPARATING CANDIDATE RANKING + DOCUMENTARY EVIDENCE + EXPLANATION
```

La primera parte responde "qué es la contribución y en qué dominio".

La segunda parte responde "qué propiedad metodológica concreta la distingue".

El uso del colon sigue un patrón frecuente en el corpus KBS para separar objeto/contribución de mecanismo o propósito.

### 6. Control de sobreinterpretación

V03 no debe leerse como claim de:

- expert system clásico;
- knowledge graph obligatorio;
- rule-based legal inference;
- normative knowledge determining candidate ranking;
- legal correctness;
- overall classification accuracy;
- human validation;
- autonomous classification;
- novelty/first/SOTA;
- external generalization;
- deployment readiness.

El cuerpo conserva la definición operacional real: historical retrieval fija candidatos; documentary evidence se asocia después; el LLM explica sin cambiar el ranking.

### 7. Dictamen

```text
TITLE_B02_V02_TECHNICAL_VALIDITY = RETAINED_PASS
TITLE_B02_V02_FINAL_EDITORIAL_APPROVAL = WITHDRAW
D172_AUTHOR_GATE = WITHDRAW_BEFORE_AUTHOR_APPROVAL

TITLE_B02_V03_REQUIRED = YES

TARGET_TITLE_EN_V03 =
Knowledge-Based Decision-Support Architecture for Tariff Classification: Separating Candidate Ranking, Documentary Evidence, and Explanation

TARGET_TITLE_ES_V03 =
Arquitectura basada en conocimiento para el apoyo a la decisión en clasificación arancelaria: separación del ranking de candidatos, la evidencia documental y la explicación

CANONICAL_MASTER_REMAINS = ARTICLE_MASTER_V032
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```

---

## English

The full 34-paper accepted-KBS corpus does not impose literal use of "AI" or "knowledge" in titles. It does, however, show a strong editorial pattern: before the Abstract, the title normally makes the KBS-relevant computational, inferential, representational, learning, or knowledge object recognizable.

Title V02 remains scientifically faithful and technically valid, but its first-read KBS identity and contribution type are only partial. The manuscript itself substantively uses "knowledge-based decision support" and "multi-stage knowledge-based systems", and its architecture integrates traceable historical precedents, candidate-specific documentary knowledge, provenance, and constrained LLM explanation.

Accordingly, "knowledge-based" is supported as a system-level characterization, not as a claim that the normative corpus determines ranking or that the framework is a classical symbolic expert system.

The recommended V03 title is:

Knowledge-Based Decision-Support Architecture for Tariff Classification: Separating Candidate Ranking, Documentary Evidence, and Explanation

The D-172 author gate should be withdrawn before approval; V032 remains canonical; Keywords and end matter remain unauthorized.
