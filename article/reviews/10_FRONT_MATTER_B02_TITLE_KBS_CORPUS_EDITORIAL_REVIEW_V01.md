# Editorial review — Front matter B02 / Title against accepted KBS corpus V01

## Español

```text
REVIEW_TYPE = TARGET_JOURNAL_CORPUS_EDITORIAL_AUDIT
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE
TARGET_JOURNAL = Knowledge-Based Systems
AUTHOR_SUPPLIED_ACCEPTED_ARTICLE_CORPUS = 34 PDF ARTICLES
CORPUS_STATUS = COMPLETE_FOR_THIS_EDITORIAL_AUDIT

TITLE_V01 =
Auditable Decision Support for Tariff Classification with Explicit Authority Separation

TITLE_V01_SOURCE =
article/sections/front_matter/Title_B02_V01.md@a50fff633f983fbfa0c9dfa0dd16684d113e8c02

CANONICAL_MASTER = ARTICLE_MASTER_V032
CANONICAL_MASTER_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f

PREVIOUS_TECHNICAL_SCIENTIFIC_REVIEW =
article/reviews/10_FRONT_MATTER_B02_TITLE_INTERNAL_REVIEW_V01.md@7c216c998ccaeeb9dcaeb1321c86348a55577292

PREVIOUS_AUTHOR_APPROVAL_GATE = D-169
AUTHOR_DECISION_ON_V01 = NOT_YET_GIVEN

EDITORIAL_VERDICT = REVISE_TITLE
SCIENTIFIC_FIDELITY = PASS
TARGET_JOURNAL_EDITORIAL_FIT = PARTIAL
CLAIM_CALIBRATION = PARTIAL
MANDATORY_EDITORIAL_REVISION = YES
```

### 1. Alcance y método de la auditoría editorial

Esta auditoría no usa longitud del título como criterio principal.

Se revisó el corpus completo de 34 artículos aceptados en *Knowledge-Based Systems* suministrado por el autor. Para cada artículo, la lectura editorial relacionó:

1. el título;
2. la promesa científica visible en el Abstract;
3. el problema y la contribución definidos en la Introducción;
4. la formulación de la contribución y los límites en la Conclusión.

El objetivo fue inferir el patrón editorial efectivo de la revista: qué función cumple el título respecto del artículo completo y qué clase de promesa científica tiende a ser aceptada.

### 2. Patrón editorial observado en el corpus KBS

La regularidad principal no es una fórmula sintáctica única ni un número de palabras.

Los títulos aceptados tienden a cumplir una relación fuerte entre:

```text
SCIENTIFIC_OBJECT
+
DISTINCTIVE_METHOD_OR_TRANSFORMATION
+
TASK_OR_APPLICATION_CONTEXT_WHEN_NEEDED
```

El título suele permitir que un lector externo anticipe qué objeto científico se estudia o propone y cuál es la operación, arquitectura, mecanismo, metodología o contraste que estructura el artículo.

El corpus admite diferentes estilos:

- títulos descriptivos directos;
- títulos método + tarea;
- títulos de transformación conceptual;
- títulos con nombre de sistema;
- títulos de dos partes con colon;
- títulos ocasionalmente retóricos.

Sin embargo, incluso cuando existe un nombre de sistema o un gancho retórico, la segunda parte o el resto del título ancla inmediatamente el trabajo al mecanismo y a la tarea efectivamente desarrollados.

### 3. Ejemplos representativos del patrón

Ejemplos observados en el corpus aceptado:

```text
Rule-based semantic hypergraph parsing from textual annotations
```

El título nombra directamente la transformación que el artículo implementa y evalúa.

```text
Selecting test problems from benchmark suites in constrained multiobjective optimisation
```

El título expresa la operación metodológica central y el dominio donde se aplica.

```text
Operational fairness diagnostics for AI-based detection systems: Metrics and methodology
```

El objeto científico y el tipo de contribución quedan explícitos; el artículo desarrolla precisamente esas métricas y metodología.

```text
From entity-centric to goal-oriented graphs: Enhancing LLM knowledge retrieval in Minecraft
```

El título comunica una transformación conceptual concreta y la tarea que pretende mejorar.

```text
Seeing the unseen: Cognitive Visual Imagination for camouflaged object detection
```

El gancho retórico no sustituye el contenido científico: queda seguido inmediatamente por el mecanismo y la tarea.

Otros títulos del corpus refuerzan la misma relación título-artículo mediante nombres de métodos, frameworks o sistemas seguidos de su función real, por ejemplo FireSegUNet, EfficientMedFormer, HuddsTrafficFL, PPO-CIS, CodeEnhancer, DynaMind, Causal-Nest y otros.

### 4. Regla de claim editorial observada

El corpus también muestra que KBS admite títulos fuertes cuando la propiedad destacada queda respaldada por la evaluación central del artículo.

Por tanto, un término prominente en el título debe responder a una de estas condiciones:

```text
A) es el objeto metodológico principal realmente desarrollado; o
B) es una propiedad central directamente evaluada y suficientemente respaldada.
```

Un término correcto pero secundario, ambiguo para un lector externo o respaldado solo parcialmente no debería ocupar la posición conceptual principal del título.

### 5. Auditoría de Title B02 V01

Título V01:

```text
Auditable Decision Support for Tariff Classification with Explicit Authority Separation
```

#### 5.1. Aspectos que pasan

```text
TARIFF_CLASSIFICATION_DOMAIN = PASS
DECISION_SUPPORT_FRAMING = PASS
NO_AUTONOMOUS_CLASSIFIER_OVERCLAIM = PASS
NO_NANDINA_TESTBED_REDUCTION = PASS
NO_NOVELTY_OR_SOTA_CLAIM = PASS
SCIENTIFIC_COMPATIBILITY_WITH_MANUSCRIPT = PASS
```

El título es científicamente defendible y no contradice el manuscrito.

#### 5.2. Problema editorial 1 — "Explicit Authority Separation"

`Explicit Authority Separation` es correcto dentro de la terminología interna del artículo, pero es demasiado abstracto como descriptor principal para un lector que aún no conoce el sistema.

El artículo no estudia una noción genérica de autoridad. Su operación metodológica concreta es:

```text
candidate ranking
-> fixed candidates
-> documentary evidence association without reranking
-> controlled explanation without ranking authority
```

El manuscrito define esta separación en Abstract, Introduction, Positioning, Architecture y Conclusion.

El título V01 obliga al lector a descubrir después qué significa `authority`; los títulos aceptados del corpus tienden a hacer visible con mayor concreción el objeto o transformación científica.

#### 5.3. Problema editorial 2 — prominencia de "Auditable"

`Auditable` es compatible con el framing del trabajo, pero su posición inicial lo convierte en una promesa editorial principal.

La evidencia del artículo es desigual respecto de esa palabra:

- la preservación de ranking y la procedencia estructural están fuertemente verificadas;
- la asociación documental es completa dentro del corpus congelado;
- la evaluación cualitativa de auditability cubre 50 casos;
- 28/50 (56.0%) cumplen el criterio cualitativo gobernado;
- el evaluador fue LLM-as-judge, no expertos humanos;
- el manuscrito declara expresamente que trazabilidad no equivale a verificabilidad, corrección legal ni validación humana.

Por tanto:

```text
AUDITABLE = DEFENSIBLE_AS_A_BOUNDED_PROPERTY
AUDITABLE_AS_PRIMARY_TITLE_PROMISE = EDITORIALLY_TOO_PROMINENT
```

La propiedad más estable y centralmente demostrada por el artículo es la **separación funcional y evaluativa** de ranking, evidencia y explicación.

### 6. Relación con el artículo completo

El Abstract formula exactamente tres funciones separadas:

- historical retrieval ranks and fixes the Top-3;
- documentary association attaches evidence without modifying membership/order;
- the local LLM explains without ranking authority.

La Introduction posiciona el problema como separación operacional y evaluativa.

Related Work §2.6 declara que el estudio se posiciona por la separación completa de autoridad entre esos componentes, no por la presencia aislada de retrieval, evidence o LLM.

La Architecture materializa esas interfaces.

Methods y Results evalúan las funciones por separado.

La Conclusion declara como principal implicación metodológica mantener separadas la autoridad de ranking, la asociación documental y la generación, preservando procedencia.

Por ello, el título editorialmente más fiel debe hacer visible esa operación concreta.

### 7. Título editorial recomendado

```text
TITLE_EN_V02 =
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support

TITLE_ES_V02 =
Separación del ranking de candidatos, la evidencia documental y la explicación en el apoyo a la decisión de clasificación arancelaria
```

### 8. Razones de la recomendación

El V02 propuesto:

- nombra las tres funciones que estructuran todo el artículo;
- convierte el concepto abstracto de authority separation en una operación legible;
- conserva `Tariff Classification Decision Support` como dominio y framing;
- no reduce el trabajo al testbed NANDINA/Chapter 87;
- no depende de un claim de auditability más fuerte que la evaluación disponible;
- no introduce novelty, superiority, legal correctness, human validation ni deployment readiness;
- alinea título, Abstract, Introduction, Positioning, Architecture, Methods, Results, Discussion y Conclusion.

### 9. Dictamen

```text
TITLE_B02_V01_TECHNICAL_AUDIT = REMAINS_PASS
TITLE_B02_V01_SCIENTIFIC_FIDELITY = PASS
TITLE_B02_V01_KBS_CORPUS_EDITORIAL_FIT = PARTIAL
TITLE_B02_V01_CLAIM_CALIBRATION = PARTIAL

EDITORIAL_VERDICT = REVISE_TITLE
AUTHOR_APPROVAL_GATE_V01 = SHOULD_BE_WITHDRAWN_BEFORE_APPROVAL

TITLE_B02_V02_REQUIRED = YES
TARGET_TITLE_EN_V02 =
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support
```

La revisión no invalida el trabajo técnico de V01; invalida únicamente su suficiencia editorial final para la revista objetivo.

Keywords y end matter permanecen fuera de scope.

---

## English

A full editorial audit was performed against the 34 author-supplied accepted *Knowledge-Based Systems* articles. The main observed pattern is not title length but title-to-paper fidelity: accepted titles usually expose the scientific object together with the distinctive method, transformation, architecture, or task relation that structures the full paper.

Title B02 V01 remains scientifically defensible, but its journal-fit is only partial. "Explicit Authority Separation" is accurate yet abstract for a reader who has not read the manuscript, while "Auditable" is given primary prominence despite the paper's qualitative auditability assessment being limited to 50 LLM-as-judge cases with 28/50 meeting the governed criterion.

The manuscript's most stable and pervasive methodological object is the explicit separation of candidate ranking, documentary evidence association, and controlled explanation. The recommended V02 title therefore makes those functions directly visible:

"Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support."

The V01 author-approval gate should be withdrawn before approval, V032 must remain canonical, and a Title B02 V02 candidate should be produced. Keywords and end matter remain unauthorized.
