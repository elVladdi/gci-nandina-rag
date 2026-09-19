# Guía empírica de redacción para Knowledge-Based Systems basada en 34 artículos recientes / Empirical Writing Guide for Knowledge-Based Systems Based on 34 Recent Articles

## Español

### 1. Estado y alcance

```text
GUIDE_ID = KBS_EWG_34_V01
EVIDENCE_BASE = 34 artículos Open Access de Knowledge-Based Systems
PUBLICATION_YEAR = 2026
VOLUMES = 341–352
RESEARCH_ARTICLES = 33
SURVEY_ARTICLES = 1
CORPUS_DUPLICATES = 0
UNIQUE_DOI = 34/34
STATUS = DRAFT / AWAITING_AUTHOR_REVIEW
BINDING_STATUS = NOT_YET_BINDING
OFFICIAL_JOURNAL_CRITERIA = NOT_INFERRED_FROM_PUBLISHED_ARTICLES
```

Esta guía reconstruye **convenciones editoriales observadas en artículos efectivamente publicados** en *Knowledge-Based Systems* (KBS). No debe interpretarse como una lista de criterios oficiales de aceptación de Elsevier/KBS. El corpus permite inferir cómo se formula, organiza y presenta investigación que superó el proceso editorial de la revista; los requisitos oficiales de envío deben verificarse por separado en la fuente oficial vigente.

La codificación completa del corpus se conserva en `article/literature/KBS_34_ARTICLE_EDITORIAL_PATTERN_MATRIX.md`.

### 2. Hallazgos cuantitativos del corpus

| Rasgo observado | Resultado empírico | Implicación de redacción |
|---|---:|---|
| Longitud del artículo | mediana 15 páginas; rango 8–32 | KBS admite artículos compactos y extensos; la densidad depende de la complejidad metodológica, no de una plantilla fija. |
| Longitud del título | media 10.6 palabras; rango 7–14 | El título debe ser específico y técnico, sin convertirse en una oración larga. |
| Títulos con dos partes separadas por `:` | 17/34 | Es común `nombre/método: función o dominio`, pero no obligatorio. |
| Longitud del abstract | mediana 220.5 palabras; rango 134–393 | Un abstract alrededor de 200–250 palabras es consistente con el centro del corpus. |
| Abstract con lenguaje explícito de problema/limitación | 30/34 | El abstract normalmente establece primero qué falla o qué falta. |
| Abstract con propuesta explícita | 29/34 | La solución se introduce directamente con verbos como *propose*, *introduce*, *present* o *design*. |
| Abstract con evaluación/validación | 32/34 | No basta describir el método: se dice cómo fue evaluado. |
| Abstract con movimiento explícito de resultados | 31/34 | El abstract comunica evidencia, no solo intención. |
| Artículos de investigación con resultados cuantitativos concretos en el abstract | 17/33 | Las cifras son frecuentes cuando son decisivas, pero no deben añadirse por obligación. |
| Longitud aproximada de Introduction | mediana 946 palabras; rango 523–1852 | La Introduction suele ser sustantiva, pero avanza por una secuencia argumental clara. |
| Artículos de investigación con contribución explícita | 33/33 | La contribución no debe quedar implícita. |
| Contribución explicitada dentro de la Introduction | 32/33 | El lector normalmente conoce el aporte antes de entrar al cuerpo metodológico. |
| Introduction con primera persona activa (*we propose*, *we introduce*, etc.) | 27/34 | La voz activa es normal en KBS; no existe necesidad de ocultar al agente mediante nominalizaciones. |
| Introduction con párrafo de organización del artículo | 25/34 | El roadmap sigue siendo una convención frecuente. |
| Investigación con sección superior diferenciada de literatura/background/contexto | 31/33 | Related Work separado es la opción dominante, aunque puede adoptar otros nombres. |
| Trabajos con análisis de ablation | 15/34 | Es frecuente cuando el aporte posee módulos cuya contribución puede aislarse. |
| Trabajos con evidencia cualitativa explícita | 17/34 | La evaluación visual/casos complementa métricas cuando aporta información distinta. |
| Trabajos que incluyen significancia estadística o pruebas equivalentes | 14/34 | La inferencia estadística aparece cuando responde a la naturaleza del claim; no es decorativa. |
| Artículos con discusión identificable como sección/subsección interpretativa | 17/33 aprox. | Discussion independiente no es obligatoria; puede integrarse con Results. |
| Artículos de investigación con limitaciones propias en una sección/subsección identificable | 10/33 | Una sección exclusiva no es universal, pero las fronteras del claim aparecen a lo largo del manuscrito. |
| `Data availability` | 33/34 | Debe prepararse una declaración formal de disponibilidad de datos. |
| `CRediT authorship contribution statement` | 34/34 | Forma parte del end matter observado. |
| `Declaration of competing interest` | 34/34 | Forma parte del end matter observado. |
| Investigación con enlace explícito a código/datos/repositorio/proyecto reproducible | ~20/33 | La apertura de artefactos es común, especialmente en frameworks, benchmarks y sistemas computacionales. |

Los conteos describen este corpus específico y no son umbrales editoriales.

### 3. Patrón editorial dominante

El patrón más estable no es una plantilla rígida de secciones, sino una **cadena de argumentación**:

`problema concreto → limitación verificable de enfoques actuales → consecuencia de esa limitación → propuesta concreta → mecanismo que resuelve la limitación → evaluación alineada con el claim → resultado principal → alcance y límites`

Los artículos de mayor utilidad como referencia para nuestro trabajo no presentan la arquitectura como una colección de conceptos. Explican **qué objeto entra, qué componente actúa, qué transforma, qué conserva, qué produce y cómo se comprueba**. Esta observación es especialmente relevante para evitar que el manuscrito adopte tono de documento de gobernanza, especificación contractual o tesis excesivamente abstracta.

### 4. Título

#### Qué se observa

Los títulos suelen combinar tres elementos: **objeto/método**, **operación o propiedad distintiva** y, cuando aporta información, **tarea o dominio**. Nueve trabajos usan un nombre propio del método como entrada (`Causal-Nest`, `CodeEnhancer`, `DynaMind`, `EfficientMedFormer`, `HuddsTrafficFL`, etc.); otros describen directamente la operación técnica.

#### Regla para nuestro artículo

El título definitivo debe escribirse al final. Debe hacer visible la naturaleza del aporte sin reducirlo a “NANDINA Chapter 87” ni presentarlo genéricamente como “RAG for HS classification”. El dominio puede aparecer como testbed/aplicación si mejora la precisión, pero no debe desplazar al aporte arquitectónico-metodológico.

#### Evitar

- títulos promocionales o con demasiados adjetivos;
- títulos que describen únicamente la tecnología usada (`LLM + RAG + BM25`) sin expresar la función científica;
- títulos que hacen pasar el testbed por el alcance conceptual completo;
- títulos que prometen generalización no demostrada.

### 5. Abstract

#### Secuencia recomendada

El corpus favorece una secuencia de cinco movimientos:

1. **Problema y contexto inmediato.** Una o dos frases; no una historia extensa del dominio.
2. **Limitación concreta.** Qué no resuelven adecuadamente los enfoques existentes y por qué importa.
3. **Propuesta.** Qué se propone y cuál es el mecanismo central.
4. **Evaluación y evidencia.** Dataset/testbed, comparación o diseño experimental y resultados principales.
5. **Interpretación delimitada.** Qué demuestra la evidencia y hasta dónde llega.

#### Aplicación a nuestro artículo

El abstract final debe poder entenderse sin conocer NANDINA previamente. Debe distinguir con claridad:

- ranking histórico de candidatos;
- Top-3 fijo;
- recuperación normativa posterior sin reranking;
- LLM únicamente para explicación;
- evaluación por función;
- NANDINA Chapter 87 como testbed empírico.

Cuando Grupo 3 y los resultados finales estén cerrados, el abstract deberá incorporar únicamente las cifras que materialmente demuestren los claims centrales. No se deben llenar el abstract de métricas secundarias.

### 6. Introduction

#### Patrón observado

La Introduction de KBS no funciona como marco conceptual genérico. Normalmente avanza de lo general a una **fricción técnica precisa** y termina haciendo visible el aporte. La secuencia dominante es:

`relevancia del problema → enfoques existentes → limitación específica → por qué la limitación importa → propuesta → delimitación → contribuciones → roadmap`

La contribución es explícita en los 33 artículos de investigación del corpus. La práctica dominante es presentarla mediante una lista breve de contribuciones diferenciables o mediante un párrafo compacto equivalente.

#### Regla para nuestro artículo

La Introduction debe hacer que un lector pueda responder, antes de Methods:

1. ¿Qué problema de decisión/clasificación asistida se intenta resolver?
2. ¿Qué mezclan o dejan insuficientemente separados los enfoques existentes?
3. ¿Qué contrato funcional propone este trabajo?
4. ¿Qué se evalúa realmente y qué no se afirma?
5. ¿Por qué la separación ranking → evidencia → explicación es científicamente relevante?
6. ¿Qué parte es general/configurable y qué parte solo ha sido probada en NANDINA Chapter 87?

No se debe comenzar enumerando componentes internos del repositorio ni describiendo el piloto como si fuera el aporte principal.

### 7. Related Work

#### Patrón observado

La sección separada de literatura/background/contexto aparece en 31 de los 33 research articles. La organización predominante es **por familias de enfoques o problemas**, no por secuencia de autores. Las mejores secciones del corpus hacen tres cosas:

- describen qué resuelve cada familia;
- identifican la limitación pertinente para el problema actual;
- terminan posicionando la propuesta respecto de esas familias.

#### Regla para nuestro artículo

La organización prevista por HS classification/candidate retrieval, RAG/regulatory reasoning, explainability/auditability y validity/reproducibility es compatible con la práctica observada. Cada subsección debe terminar en una síntesis comparativa útil para el posicionamiento; no debe convertirse en una bibliografía comentada.

`Gap` y `novelty` no deben declararse por repetición. El gap final debe emerger de comparaciones específicas entre funciones y evidencia disponible.

### 8. Methods: qué espera el lector

#### 8.1. Concreción antes que abstracción

Los artículos del corpus describen el método mediante entidades y operaciones identificables. La redacción típica utiliza relaciones del tipo:

`input → operación → condición → output`

La voz activa es frecuente. Expresiones como *we propose*, *we use*, *the module receives*, *the algorithm selects* y *the model outputs* son normales. Esto contradice cualquier regla que obligue a esconder la acción detrás de cadenas nominales.

#### 8.2. Arquitectura primero, detalles después

En frameworks y sistemas complejos suele aparecer temprano una vista de conjunto, diagrama o explicación de flujo. La figura arquitectónica no sustituye al texto: el texto debe seguir el mismo orden operacional de la figura.

Para nuestro artículo, Methods debe permitir seguir literalmente:

`descripción comercial → normalización → recuperación histórica → Top-k → Top-3 fijo → recuperación normativa para esos candidatos → construcción de contexto → LLM local → explicación`

#### 8.3. Datos y corpus como objetos metodológicos

El dataset histórico y el corpus normativo no pueden aparecer como detalles secundarios. Deben documentarse como **dos fuentes con funciones diferentes**:

- banco histórico etiquetado → ranking de candidatos;
- corpus documental/normativo → evidencia posterior para candidatos ya fijados.

La guía exige explicar procedencia, selección, preparación, versión, cobertura y función de cada uno, sin llamar “training data” al corpus documental si no cumple esa función.

#### 8.4. Configurabilidad con límites

Los artículos más próximos a nuestra situación distinguen cuidadosamente entre una arquitectura general y una prueba empírica delimitada. Para nuestro manuscrito:

- puede afirmarse que el método está diseñado para instanciarse con otro banco histórico, universo de clases y corpus documental compatible;
- deben declararse las interfaces/precondiciones necesarias;
- no puede inferirse que el rendimiento observado en Chapter 87 se transfiere a esas nuevas instancias.

`configurability / replicability ≠ empirical generalization` permanece como frontera obligatoria.

#### 8.5. Implementación y reproducibilidad

Los artículos de frameworks y benchmarks suelen separar la descripción conceptual de configuraciones, software, datasets y artefactos. Nuestro Methods 3.9 debe identificar explícitamente el repositorio de reproducibilidad y explicar qué permite reproducir/configurar.

La declaración final `Data availability` no sustituye esta explicación metodológica.

### 9. Results

#### Patrón observado

KBS favorece resultados organizados alrededor de **comparaciones verificables**, no una narración cronológica del experimento. El uso de baselines/comparadores aparece en prácticamente todo el corpus experimental. Ablation, sensibilidad, evidencia cualitativa, eficiencia computacional y pruebas estadísticas se incorporan cuando responden a un claim concreto.

#### Regla para nuestro artículo

Results debe mantener la evaluación funcional:

1. controles de benchmark y partición;
2. recuperación histórica / RQ1;
3. recuperación normativa e integración / RQ2;
4. explicación controlada / RQ3;
5. sensibilidad y validez documental;
6. inferencia / RQ4 solo cuando Grupo 3 esté cerrado;
7. EXP-11B solo tras reconciliación C10/C11.

Cada subsección debe responder:

`pregunta → métrica → comparación → resultado → interpretación permitida`

No utilizar “accuracy del sistema RAG” cuando la métrica evalúa candidate retrieval. No convertir asociación normativa en corrección jurídica y no convertir auditabilidad en legal correctness.

### 10. Discussion y Limitations

#### Patrón observado

KBS no impone una única forma: varios trabajos tienen Discussion independiente, otros la integran en Results y otros combinan Discussion/Conclusion. Lo estable es la función interpretativa.

La limitación tampoco se posterga necesariamente hasta una sección final. Los artículos técnicamente más cuidadosos introducen límites cerca del claim al que afectan y después los consolidan al final.

#### Regla para nuestro artículo

La Discussion debe explicar:

- qué significa separar ranking, evidencia y explicación;
- qué se gana en auditabilidad y control del pipeline;
- qué se puede comparar con literatura previa;
- qué no demuestra el piloto;
- bajo qué condiciones la arquitectura puede reconfigurarse.

Limitations debe ser técnica, no defensiva. Debe cubrir benchmark/datos, HE4/auditabilidad, drift normativo, corpus, reproducibilidad y validez externa según corresponda al estado final de la evidencia.

### 11. Conclusion

La Conclusion debe cerrar cuatro elementos: **aporte**, **evidencia principal**, **alcance** e **implicación**. No debe introducir una nueva promesa de generalización ni repetir de manera mecánica todas las métricas.

El trabajo futuro es frecuente en el corpus, pero debe derivarse de limitaciones reales, no servir para compensar evidencia faltante.

### 12. Reproducibilidad y end matter

La presencia de `Data availability` en 33/34 artículos y de CRediT/competing-interest en 34/34 hace necesario reservar desde ahora el cierre editorial correspondiente.

Para nuestro artículo deben existir, como mínimo:

- identificación formal del repositorio `gci-nandina-rag-reproducibility`;
- alcance de lo que contiene y de lo que no contiene;
- versión/commit o release estable al momento de submission;
- instrucciones suficientes para reconstruir el flujo experimental permitido;
- relación entre dataset histórico, corpus normativo, configuración y resultados;
- `Data availability` final coherente con el repositorio y con cualquier restricción de datos.

### 13. Estilo de frase y párrafo

#### Hacer

- preferir sujeto/agente + verbo + objeto;
- nombrar el componente que ejecuta cada acción;
- explicar causalidad mecánica solo cuando el diseño la respalda;
- usar conectores contrastivos para mostrar la lógica (`however`, `therefore`, `to address this limitation`) y no como relleno;
- reservar una oración para una relación principal cuando la frase empieza a acumular funciones;
- poner cifras junto al claim que prueban;
- presentar primero la diferencia funcional y después la terminología interna;
- mantener los límites de alcance próximos a afirmaciones de transferibilidad, generalización o validez.

#### Evitar

- cadenas de sustantivos abstractos del tipo “functional separation of candidate-evidence integration and downstream explanation” sin explicar qué componente hace qué;
- prosa que parezca un contrato de software o un documento de gobernanza;
- párrafos que enumeran restricciones antes de explicar el proceso;
- convertir cada detalle metodológico en una “contribución”;
- anunciar `novel`, `robust`, `superior`, `effective` o `generalizable` sin evidencia inmediatamente trazable;
- prohibir mecánicamente esas palabras: el corpus KBS sí las usa cuando están sustentadas;
- repetir en Discussion los mismos números de Results sin interpretarlos;
- usar el dominio NANDINA como sustituto de la pregunta científica.

### 14. Patrón de claims: nivel de fuerza

El corpus muestra que KBS admite lenguaje fuerte, pero los mejores ejemplos acoplan fuerza verbal y evidencia. La regla para el manuscrito será:

- **diseño:** `is designed to`, `supports`, `allows`, `preserves`;
- **observación experimental:** `achieved`, `reduced`, `retrieved`, `maintained`;
- **comparación:** `outperformed` solo con comparador y métrica explícitos;
- **inferencia:** `suggests`, `indicates`, `is consistent with` cuando la evidencia no prueba causalidad/generalización;
- **frontera:** `does not establish`, `is limited to`, `was evaluated only on` para evitar extrapolación.

No utilizar un verbo de resultado para una propiedad meramente configuracional.

### 15. Artículos de referencia prioritaria para nuestro manuscrito

No todos los 34 artículos tienen la misma utilidad estilística para nuestro trabajo. Se priorizan los siguientes como **modelos editoriales funcionales**, sin convertirlos en fuentes científicas de nuestros claims:

1. **AIMNER** — excelente separación entre framework general, aplicación única y transferencia no demostrada.
2. **From entity-centric to goal-oriented graphs** — muy próximo por RAG/knowledge retrieval y por su delimitación explícita del testbed frente al alcance conceptual.
3. **Automating data-driven modeling... using LLM agents** — distingue su contribución de frameworks genéricos y concreta un workflow end-to-end.
4. **Agentic LLM for anonymizing healthcare data...** — arquitectura modular y evaluación de funciones diferenciadas.
5. **Metric-privacy-inspired noise calibration...** — ejemplar para declarar que una idea se usa como principio de diseño sin elevarla a garantía formal.
6. **On the impact of pretraining data ordering...** — modelo de lenguaje inferencial prudente y diseño controlado.
7. **Operational fairness diagnostics...** — metodología general seguida de instanciación y evaluación en un dominio.
8. **HuddsTrafficFL** — benchmark/reproducibilidad, disponibilidad de artefactos y evaluación comparativa.
9. **Rule-based semantic hypergraph parsing...** — conocimiento estructurado, reglas explícitas y posicionamiento comparativo.

### 16. Aplicación obligatoria propuesta al manuscrito actual

Una vez aprobada por el autor, esta guía debería convertirse en control acumulativo de la IA de Redacción. Antes de aprobar cualquier bloque deberá auditarse, además del contenido científico:

```text
KBS_PROBLEM_TO_CONTRIBUTION_FLOW = PASS
KBS_CONCRETE_AGENT_ACTION_OBJECT_PROSE = PASS
KBS_SECTION_FUNCTION = PASS
KBS_CLAIM_STRENGTH_EVIDENCE_MATCH = PASS
KBS_GENERAL_METHOD_TESTBED_BOUNDARY = PASS
KBS_REPRODUCIBILITY_VISIBILITY = PASS
KBS_NO_GOVERNANCE_PROSE_LEAKAGE = PASS
```

La V03/V04 de Methods B01 deberá ser reexaminada contra esta guía antes de aprobación de autor. El `PASS` científico previo no debe considerarse automáticamente un `PASS` editorial KBS.

---

## English

### 1. Status and scope

```text
GUIDE_ID = KBS_EWG_34_V01
EVIDENCE_BASE = 34 recent Open Access Knowledge-Based Systems articles
PUBLICATION_YEAR = 2026
VOLUMES = 341–352
RESEARCH_ARTICLES = 33
SURVEY_ARTICLES = 1
CORPUS_DUPLICATES = 0
UNIQUE_DOI = 34/34
STATUS = DRAFT / AWAITING_AUTHOR_REVIEW
BINDING_STATUS = NOT_YET_BINDING
OFFICIAL_JOURNAL_CRITERIA = NOT_INFERRED_FROM_PUBLISHED_ARTICLES
```

This guide reconstructs **editorial conventions observed in articles actually published** in *Knowledge-Based Systems* (KBS). It is not a list of official Elsevier/KBS acceptance criteria. The corpus shows how research that passed the journal's editorial process is formulated, organized, and presented; official submission requirements must be checked separately against the current primary journal source.

The complete corpus coding is stored in `article/literature/KBS_34_ARTICLE_EDITORIAL_PATTERN_MATRIX.md`.

### 2. Quantitative corpus findings

| Observed feature | Empirical result | Writing implication |
|---|---:|---|
| Article length | median 15 pages; range 8–32 | KBS accommodates compact and extensive papers; density follows methodological complexity rather than a fixed template. |
| Title length | mean 10.6 words; range 7–14 | Titles are specific and technical without becoming long sentences. |
| Two-part titles separated by `:` | 17/34 | `method/name: function or domain` is common but optional. |
| Abstract length | median 220.5 words; range 134–393 | Roughly 200–250 words lies near the center of the observed corpus. |
| Abstracts with explicit problem/limitation language | 30/34 | Abstracts usually establish what is missing or failing before the solution. |
| Abstracts with an explicit proposal move | 29/34 | Solutions are introduced directly through verbs such as *propose*, *introduce*, *present*, or *design*. |
| Abstracts with evaluation/validation | 32/34 | Describing the method alone is insufficient; evaluation is normally stated. |
| Abstracts with an explicit results move | 31/34 | Abstracts communicate evidence, not merely intent. |
| Research articles reporting concrete quantitative results in the abstract | 17/33 | Numbers are frequent when decisive, but they are not mechanically required. |
| Approximate Introduction length | median 946 words; range 523–1852 | Introductions are substantive but follow a clear argumentative sequence. |
| Research articles with explicit contribution statements | 33/33 | Contribution is not left implicit. |
| Contribution made explicit within the Introduction | 32/33 | Readers normally know the contribution before entering the methodological body. |
| Introductions using active first person (*we propose*, *we introduce*, etc.) | 27/34 | Active voice is normal in KBS; agents need not be hidden behind nominalizations. |
| Introductions with a paper roadmap | 25/34 | A structural roadmap remains a frequent convention. |
| Research papers with a distinct top-level literature/background/context section | 31/33 | A separate Related Work-type section is dominant, though labels vary. |
| Papers with ablation analysis | 15/34 | Common when the contribution contains modules whose effects can be isolated. |
| Papers with explicit qualitative evidence | 17/34 | Visual/case evidence complements metrics when it adds distinct information. |
| Papers including statistical significance or equivalent testing | 14/34 | Statistical inference is used when it follows from the claim, not as decoration. |
| Research articles with an identifiable interpretive Discussion section/subsection | approx. 17/33 | A standalone Discussion is not mandatory; interpretation may be integrated with Results. |
| Research articles with a dedicated author-limitation section/subsection | 10/33 | A dedicated section is not universal, but claim boundaries appear throughout the manuscript. |
| `Data availability` | 33/34 | A formal data-availability statement should be prepared. |
| `CRediT authorship contribution statement` | 34/34 | This is part of the observed end matter. |
| `Declaration of competing interest` | 34/34 | This is part of the observed end matter. |
| Research with an explicit code/data/repository/reproducible-project link | ~20/33 | Artifact openness is common, especially for frameworks, benchmarks, and computational systems. |

These counts describe this corpus and are not editorial thresholds.

### 3. Dominant editorial pattern

The most stable pattern is not a rigid section template but an **argument chain**:

`concrete problem → verifiable limitation of current approaches → consequence of that limitation → concrete proposal → mechanism addressing the limitation → claim-aligned evaluation → main result → scope and boundaries`

The most useful papers for our work do not present an architecture as a collection of concepts. They explain **what enters, which component acts, what it transforms, what it preserves, what it outputs, and how this is tested**. This is particularly important for preventing the manuscript from sounding like governance documentation, a software contract, or an overly abstract thesis.

### 4. Title

Observed titles typically combine **method/object**, a **distinctive operation/property**, and, when informative, the **task/domain**. Named methods are common but not required.

For our paper, the final title should be written late. It must expose the architectural-methodological contribution without reducing the paper to “NANDINA Chapter 87” or generic “RAG for HS classification.” The testbed may appear when it improves precision, but it must not replace the scientific object.

Avoid promotional adjectives, technology inventories, testbed-as-scope framing, and unsupported generalization.

### 5. Abstract

The recommended five-move sequence is:

1. Immediate problem and context.
2. Concrete limitation.
3. Proposal and central mechanism.
4. Evaluation and evidence.
5. Bounded interpretation.

Our final abstract must clearly separate historical candidate ranking, fixed Top-3 selection, post-ranking normative retrieval without reranking, LLM explanation only, function-specific evaluation, and NANDINA Chapter 87 as the empirical testbed. Once Group 3 and final results are closed, only figures that materially support the central claims should be included.

### 6. Introduction

The dominant sequence is:

`problem relevance → current approaches → specific limitation → why it matters → proposal → boundary → contributions → roadmap`

All 33 research papers make their contribution explicit. Our Introduction must allow a reader to identify the decision-support problem, the limitation in prior functional arrangements, the proposed functional contract, the empirical scope, the scientific value of separating ranking/evidence/explanation, and the distinction between configurability and demonstrated transfer.

### 7. Related Work

A distinct literature/background/context section appears in 31/33 research articles. Strong sections are organized by method/problem families, identify the limitation relevant to the present work, and end with comparative positioning rather than an author-by-author catalogue.

Our planned task-based structure is compatible with this pattern. `Gap` and `novelty` must emerge from specific comparisons rather than repeated labels.

### 8. Methods

KBS papers favor identifiable entities and operations. A useful sentence pattern is `input → operation → condition → output`. Active voice is common and should be preferred over stacked nominalizations when it improves precision.

Complex systems usually establish an overview before implementation details. Our Methods should follow the same operational order as the architecture figure: commercial description → normalization → historical retrieval → Top-k → fixed Top-3 → candidate-specific normative evidence → context construction → local LLM → explanation.

Historical data and the normative corpus must be documented as different methodological objects with different roles. Configurability may be described as a design property, but empirical performance outside the evaluated Chapter 87 instance must not be inferred.

Implementation and reproducibility details should be separated from the conceptual contract. Methods 3.9 should explicitly identify the reproducibility repository and what it allows readers to reproduce or reconfigure.

### 9. Results

KBS results are organized around verifiable comparisons rather than chronological experiment narration. Baselines/comparators dominate the experimental corpus; ablation, sensitivity, qualitative evidence, computational efficiency, and statistical tests are included when they directly test a claim.

Our Results should preserve function-specific evaluation and use the pattern `question → metric → comparison → result → permitted interpretation`. Candidate retrieval must not be called overall system accuracy; normative association is not substantive legal correctness; auditability is not legal correctness.

### 10. Discussion and Limitations

KBS permits standalone, combined, or integrated Discussion structures. What matters is interpretation. Claim limitations often appear near the affected claim and are consolidated later.

Our Discussion should interpret the ranking/evidence/explanation separation, auditability/control implications, literature comparison, non-demonstrated aspects of the pilot, and conditions for reconfiguration. Limitations should be technical rather than defensive.

### 11. Conclusion

The Conclusion should close contribution, main evidence, scope, and implication without introducing new generalization claims. Future work is common but should follow from real limitations rather than compensate for missing evidence.

### 12. Reproducibility and end matter

The observed prevalence of `Data availability`, CRediT, and competing-interest declarations means these components should be reserved now. Our paper should formally identify `gci-nandina-rag-reproducibility`, its scope, a stable release/commit at submission, reproducible/configurable interfaces, and the relationship among historical data, normative corpus, configuration, and outputs.

### 13. Sentence and paragraph style

Prefer explicit agent–action–object relations, concrete component names, evidence-localized numbers, and scope boundaries near transfer/generalization claims. Avoid stacked abstractions, governance-contract prose, restriction lists before process explanation, and unsupported adjectives.

The corpus does use terms such as *novel*, *robust*, *superior*, and *effective*. They should therefore not be banned mechanically; they must be evidence-anchored and epistemically appropriate.

### 14. Claim strength

Use design verbs for design properties, result verbs for observations, comparative verbs only with explicit metrics/comparators, inferential verbs for bounded interpretation, and boundary verbs for scope restrictions. A configurability property must never be phrased as an empirical performance result.

### 15. Priority reference papers for our manuscript

The most useful editorial exemplars for our problem are AIMNER; *From entity-centric to goal-oriented graphs*; *Automating data-driven modeling... using LLM agents*; *Agentic LLM for anonymizing healthcare data...*; *Metric-privacy-inspired noise calibration...*; *On the impact of pretraining data ordering...*; *Operational fairness diagnostics...*; HuddsTrafficFL; and *Rule-based semantic hypergraph parsing...*.

### 16. Proposed binding application

Once approved by the author, the guide should become a cumulative drafting control using the following gates:

```text
KBS_PROBLEM_TO_CONTRIBUTION_FLOW = PASS
KBS_CONCRETE_AGENT_ACTION_OBJECT_PROSE = PASS
KBS_SECTION_FUNCTION = PASS
KBS_CLAIM_STRENGTH_EVIDENCE_MATCH = PASS
KBS_GENERAL_METHOD_TESTBED_BOUNDARY = PASS
KBS_REPRODUCIBILITY_VISIBILITY = PASS
KBS_NO_GOVERNANCE_PROSE_LEAKAGE = PASS
```

Methods B01 V03/V04 should be re-audited against this guide before author approval. A previous scientific-content `PASS` does not automatically constitute a KBS editorial-quality `PASS`.
