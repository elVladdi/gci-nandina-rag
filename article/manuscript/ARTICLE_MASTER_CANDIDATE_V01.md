# ARTICLE MASTER CANDIDATE V01

## Part I — English manuscript master

### 3. Methods

#### 3.1 Design, scope, and units

The study was designed as an applied, offline experimental pilot for auditable recommendation of NANDINA subheadings from customs merchandise descriptions. Its empirical scope was restricted to Chapter 87, under the administrative, documentary, temporal, and experimental conditions defined by the governing study artifacts. The system was conceived as non-binding decision support rather than an autonomous customs-classification authority; expert review remained outside the automated workflow.

Functional responsibilities were separated by design. Historical retrieval generated and ranked candidate subheadings, producing the historical Top-k from which a fixed Top-3 was selected. Normative retrieval then supplied documentary evidence for those already fixed candidates and was not allowed to replace or reorder the historical ranking. The local LLM operated only downstream of retrieval to produce a controlled explanation of the fixed Top-3. It did not classify from scratch, introduce external candidate codes, delete or substitute retrieved candidates, change their order, or feed generated content back into the classification process.

The unit of observation and analysis was the series record within a customs declaration (DAM). Because multiple series records may belong to the same declaration, DAM was treated as the grouping unit whenever dependence was methodologically relevant. The query unit was the series record represented by its normalized commercial description. The system output was the historical Top-k ranking and, for downstream evidence retrieval and explanation, the fixed historical Top-3. These definitions separate the analytical unit, dependence structure, query representation, and output object. The architecture may be configurable beyond the evaluated setting, but such configurability is a design property and does not constitute empirical generalization beyond the Chapter 87 scope examined here.

## Part II — Spanish semantic-control mirror

### 3. Métodos

#### 3.1 Diseño, alcance y unidades

El estudio se diseñó como un piloto experimental aplicado y offline para apoyar la recomendación auditable de subpartidas NANDINA a partir de descripciones comerciales aduaneras. Su alcance empírico se restringió al Capítulo 87, dentro de las condiciones administrativas, documentales, temporales y experimentales definidas por los artefactos gobernantes del estudio. El sistema se concibió como apoyo a la decisión no vinculante y no como una autoridad autónoma de clasificación aduanera; la revisión experta permaneció fuera del flujo automatizado.

Las responsabilidades funcionales se separaron por diseño. La recuperación histórica generó y ordenó las subpartidas candidatas, produciendo el ranking histórico Top-k del que se seleccionó un Top-3 fijo. La recuperación normativa aportó después evidencia documental para esos candidatos ya fijados y no podía sustituir ni reordenar el ranking histórico. El LLM local operó únicamente después de la recuperación para producir una explicación controlada del Top-3 fijo. No clasificó desde cero, no incorporó códigos candidatos externos, no eliminó ni sustituyó candidatos recuperados, no cambió su orden ni retroalimentó el proceso de clasificación con contenido generado.

La unidad de observación y análisis fue la serie de una Declaración Aduanera de Mercancías (DAM). Dado que varias series pueden pertenecer a una misma declaración, la DAM se trató como unidad de agrupamiento cuando la dependencia era metodológicamente relevante. La unidad de consulta fue la serie representada por su descripción comercial normalizada. La salida del sistema fue el ranking histórico Top-k y, para la recuperación posterior de evidencia y la explicación, el Top-3 histórico fijo. Estas definiciones separan la unidad analítica, la estructura de dependencia, la representación de consulta y el objeto de salida. La arquitectura puede ser configurable fuera del entorno evaluado, pero esa configurabilidad es una propiedad de diseño y no constituye generalización empírica más allá del alcance del Capítulo 87 examinado aquí.
