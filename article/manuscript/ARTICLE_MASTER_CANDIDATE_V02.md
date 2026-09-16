# ARTICLE MASTER CANDIDATE V02

## Part I — English manuscript master

### 3. Methods

#### 3.1 Design, scope, and units

The study evaluated an auditable decision-support architecture in which candidate ranking, normative-evidence retrieval, and downstream explanation were assigned distinct functions. Historical retrieval generated and ranked candidate subheadings, producing a historical Top-k from which a fixed Top-3 was selected. Normative retrieval then supplied documentary evidence for those already fixed candidates without replacing or reordering the historical ranking. A local LLM operated only after retrieval to generate controlled explanations of the fixed Top-3; it did not classify from scratch, insert external candidate codes, delete or substitute retrieved candidates, change their order, or feed generated content back into candidate selection.

This architecture was examined through an applied, offline experimental pilot using NANDINA Chapter 87 as a controlled regulatory testbed. The system was non-binding decision support rather than an autonomous customs-classification authority, and expert review remained outside the automated workflow. The empirical evaluation was restricted to Chapter 87 within the administrative, documentary, temporal, and experimental setting defined for the study; it does not establish empirical generalization beyond that scope.

The unit of observation and analysis was the series record within a Declaración Aduanera de Mercancías (DAM; customs declaration). Because multiple series records may belong to the same DAM, the DAM served as the grouping unit whenever dependence was methodologically relevant. The query unit was the series record represented by its normalized commercial description. The corresponding output objects were the historical Top-k ranking and the fixed historical Top-3 used for downstream normative-evidence retrieval and explanation. These definitions distinguish the analytical unit, dependence structure, query representation, and output object.

## Part II — Spanish semantic-control mirror

### 3. Métodos

#### 3.1 Diseño, alcance y unidades

El estudio evaluó una arquitectura auditable de apoyo a decisión en la que el ranking de candidatos, la recuperación de evidencia normativa y la explicación posterior se asignaron a funciones diferenciadas. La recuperación histórica generó y ordenó las subpartidas candidatas, produciendo un ranking histórico Top-k del cual se seleccionó un Top-3 fijo. La recuperación normativa aportó después evidencia documental para esos candidatos ya fijados sin sustituir ni reordenar el ranking histórico. Un LLM local operó únicamente después de la recuperación para generar explicaciones controladas del Top-3 fijo; no clasificó desde cero, no insertó códigos candidatos externos, no eliminó ni sustituyó candidatos recuperados, no cambió su orden ni retroalimentó la selección de candidatos con contenido generado.

Esta arquitectura se examinó mediante un piloto experimental aplicado y offline, utilizando el Capítulo 87 de NANDINA como un entorno de prueba regulatorio controlado. El sistema funcionó como apoyo a la decisión no vinculante y no como una autoridad autónoma de clasificación aduanera, y la revisión experta permaneció fuera del flujo automatizado. La evaluación empírica se restringió al Capítulo 87 dentro del entorno administrativo, documental, temporal y experimental definido para el estudio; no establece generalización empírica más allá de ese alcance.

La unidad de observación y análisis fue la serie de una Declaración Aduanera de Mercancías (DAM). Dado que varias series pueden pertenecer a una misma DAM, la DAM se utilizó como unidad de agrupamiento cuando la dependencia era metodológicamente relevante. La unidad de consulta fue la serie representada por su descripción comercial normalizada. Los objetos de salida correspondientes fueron el ranking histórico Top-k y el Top-3 histórico fijo utilizado para la recuperación posterior de evidencia normativa y la explicación. Estas definiciones distinguen la unidad analítica, la estructura de dependencia, la representación de consulta y el objeto de salida.
