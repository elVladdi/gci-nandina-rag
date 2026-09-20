# ARTICLE MASTER CANDIDATE V05

## Part I — English manuscript master

### 3. Methods

#### 3.1 Design, scope, and units

The method takes a normalized merchandise description as the query for historical retrieval. That stage searches a labeled historical bank, produces a Top-k ranking of candidate subheadings, and fixes the historical Top-3 before normative evidence is retrieved. Normative retrieval then searches a documentary corpus for evidence linked to those fixed candidates and attaches that evidence without changing their order. The local LLM receives the fixed Top-3 and the retrieved evidence and generates a controlled explanation; its output is not fed back into candidate selection or ranking. This sequence defines the functional contract evaluated in the study, with ranking, evidence retrieval, and explanation treated as distinct functions.

A new instance requires a labeled historical dataset aligned with a target class universe that is explicitly defined for the task. It also requires a documentary or normative corpus whose candidate identifiers and content are compatible with the retrieval mechanism, together with representation and identifier interfaces that connect these resources consistently to the pipeline. These prerequisites allow the resources to change while the order of functions remains fixed. Configurability and replicability are design properties; they do not imply automatic interoperability or transfer of empirical performance to other datasets, class systems, chapters, tariff levels, jurisdictions, or corpora. The construction and versioning of these resources are described in later Methods subsections.

In this article, we evaluated one instance as an applied, offline pilot using NANDINA Chapter 87 and the specific versions of the historical data, documentary corpus, and configuration prepared for that pilot. The system provided non-binding decision support, while expert review remained outside the automated workflow. Accordingly, the empirical evidence reported in this article applies to this Chapter-87 pilot and those versioned resources; it does not establish performance for other instances.

The unit of observation and analysis was the series record within a Declaración Aduanera de Mercancías (DAM; customs declaration). When dependence among records from the same declaration was methodologically relevant, the DAM served as the grouping unit. Each query was a series record represented by its normalized commercial description. Historical retrieval returned the Top-k ranking and fixed historical Top-3 carried forward to normative-evidence retrieval and explanation.

## Part II — Spanish semantic-control mirror

### 3. Métodos

#### 3.1 Diseño, alcance y unidades

El método recibe una descripción comercial normalizada como consulta para la recuperación histórica. Esta etapa consulta un banco histórico etiquetado, produce un ranking Top-k de subpartidas candidatas y fija el Top-3 histórico antes de recuperar evidencia normativa. Luego, la recuperación normativa consulta un corpus documental para obtener evidencia vinculada con esos candidatos ya fijados y la asocia sin cambiar su orden. El LLM local recibe el Top-3 fijo y la evidencia recuperada y genera una explicación controlada; su salida no retroalimenta la selección ni el ranking de candidatos. Esta secuencia define el contrato funcional evaluado en el estudio, en el que el ranking, la recuperación de evidencia y la explicación se tratan como funciones diferenciadas.

Una nueva instancia requiere un dataset o banco histórico etiquetado y alineado con un universo de clases objetivo definido explícitamente para la tarea. También requiere un corpus documental o normativo cuyos identificadores de candidatos y contenido sean compatibles con el mecanismo de recuperación, además de interfaces de representación e identificación que conecten esos recursos de manera coherente con el pipeline. Estas precondiciones permiten cambiar los recursos manteniendo fijo el orden de las funciones. La configurabilidad y la replicabilidad son propiedades de diseño; no implican interoperabilidad automática ni transferencia del desempeño empírico a otros datasets, sistemas de clases, capítulos, niveles arancelarios, jurisdicciones o corpus. La construcción y el versionamiento de estos recursos se describen en subsecciones posteriores de Methods.

En este artículo, evaluamos una instancia mediante un piloto experimental aplicado y offline que utiliza el Capítulo 87 de NANDINA y las versiones específicas de los datos históricos, el corpus documental y la configuración preparadas para ese piloto. El sistema proporcionó apoyo a la decisión no vinculante, mientras que la revisión experta permaneció fuera del flujo automatizado. En consecuencia, la evidencia empírica presentada en este artículo corresponde a este piloto del Capítulo 87 y a esos recursos versionados; no establece desempeño para otras instancias.

La unidad de observación y análisis fue la serie de una Declaración Aduanera de Mercancías (DAM). Cuando la dependencia entre registros de una misma declaración fue metodológicamente relevante, la DAM se utilizó como unidad de agrupamiento. Cada consulta correspondió a una serie representada por su descripción comercial normalizada. La recuperación histórica devolvió el ranking Top-k y el Top-3 histórico fijo que continuó hacia la recuperación de evidencia normativa y la explicación.
