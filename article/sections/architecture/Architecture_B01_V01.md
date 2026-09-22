# Architecture B01 — V01

## Part I — English manuscript master

# 3. Decision-support architecture

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

## Part II — Spanish semantic-control mirror

# 3. Arquitectura de apoyo a decisiones

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
