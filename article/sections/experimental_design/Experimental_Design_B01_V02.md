# Experimental Design B01 V02 — Structure V02 rewrite

## Controlled Section 3 forward-reference amendments

### Part I — English

- **Section 3.5:** The concrete source documents, temporal version, corpus preparation, retrieval index, and retrieval conditions used in the evaluation are specified in Section 4, while exhaustive technical identities are retained in the reproducibility resources.
- **Section 3.7:** Section 4.8 describes the reproducibility resources and the access or redistribution conditions needed to reconstruct the evaluated instantiation, while Section 4.3 documents the documentary corpus that feeds the explanation context, including its preparation, temporal validity, and retrieval representation.

### Part II — Spanish semantic-control mirror

- **Sección 3.5:** Los documentos fuente concretos, su versión temporal, la preparación del corpus, el índice de recuperación y las condiciones de recuperación utilizadas en la evaluación se especifican en la Sección 4, mientras que las identidades técnicas exhaustivas se conservan en los recursos de reproducibilidad.
- **Sección 3.7:** La Sección 4.8 describe los recursos de reproducibilidad y las condiciones de acceso o redistribución necesarias para reconstruir la instanciación evaluada, mientras que la Sección 4.3 documenta el corpus documental que alimenta el contexto de explicación, incluida su preparación, vigencia temporal y representación para recuperación.

# PART I — English manuscript master

## 4.1. Experimental setting and scope

The experiment evaluated, offline, a concrete instantiation of the Section 3 architecture using commercial descriptions and administrative reference labels at the eight-digit NANDINA level within Chapter 87. Each SERIE record was the analysis unit. Because multiple series can belong to the same DAM/customs declaration and may share declaration-level structure, DAM was retained as the grouping unit whenever that dependence was methodologically relevant to partitioning or inference. The evaluation used fixed datasets and controlled computational procedures; it did not constitute an operational customs deployment or an adjudication of legal classification.

Chapter 87 and the eight-digit NANDINA level delimit this empirical instantiation only. The interfaces defined in Section 3 can be re-instantiated with other historical banks, target class spaces, tariff depths, or compatible documentary corpora when their stated requirements are satisfied. Such configurability is a design property and does not imply that performance observed in the present setting transfers to another setting.

## 4.2. Historical data and experimental dataset construction

The historical data were constructed through four distinct operations: collection from the administrative source, automated transformation into series-level records, curation, and DAM-grouped partition construction. Keeping these operations separate distinguishes the provenance of the administrative records from the processed representation used in the experiment.

### 4.2.1. Source and data collection

Commercial cases were collected through the SUNAT Aduanet portal for the import-for-consumption regime at the Maritime Customs Office of Callao (code 118). Eligible DAMs were declarations numbered between 2 January and 30 March 2026, collected between 11 and 20 April 2026, assigned to orange or red control channels, with a recorded cancellation date and authorized release, and containing at least one tariff item in Chapter 87. The collection was purposive rather than probability-based and applied these administrative, temporal, topical, and data-availability criteria.

After an eligible DAM was identified, the declaration was opened in Aduanet and its series entries were manually copied into an intermediate collection register. For each series, the study retained the information needed to link the analysis unit to its source declaration and administrative reference label: the declaration identifier, series number, commercial description, and recorded eight-digit NANDINA code. Consultation screenshots were retained as evidence of the collection procedure and were not used as an additional label source. The processed content required for the experiment could later be functionally reconstructed from the available collection material; however, no claim is made that the currently available complete workbook is byte-identical to the historical original.

### 4.2.2. Processing and curation

The collected records were transformed in Python into a tabular representation with one row per SERIE. Processing identified declaration and series blocks, extracted the fields associated with each series, preserved the available merchandise-description lines, concatenated them into the commercial-description representation, and generated a reproducible series identifier from declaration and series information. Text preparation standardized spacing, while the tariff-code field was converted into its eight-digit NANDINA representation and corresponding hierarchy fields for consistency checks.

Quality controls required the fields needed to identify the series and its reference code, a non-empty commercial description, a valid eight-digit NANDINA code, hierarchy consistency, Chapter 87 membership, and absence of critical parsing warnings affecting the declaration, series, or tariff code. Repeated records sharing a series identifier were handled according to their content: identical non-technical duplicates were collapsed to one stable record, whereas conflicting records for the same identifier were excluded as a group. The reconstructed intermediate contained 11,320 series from 107 DAMs. Chapter 87 filtering yielded 4,232 records before curation and 4,106 curated records for construction of the version 0.2 benchmark.

### 4.2.3. Partition construction and dataset composition

The 4,106 curated records were assigned to a historical bank, a development set, and an evaluation set. Version 0.2 was materialized through explicit assignments of complete DAMs to the three partitions; the recorded random seed is provenance metadata and was not the mechanism used to allocate version 0.2 records. DAM therefore served as the grouping unit for partition construction. The final partitions had no DAM overlap and no overlap in the reproducible series identifiers across partitions.

The historical bank contains 2,950 series from 28 DAMs and 66 represented codes. The development set contains 100 series from 6 DAMs and 9 represented codes. The evaluation set contains 1,056 series from 67 DAMs and 42 represented reference codes. These counts characterize the labels present in each partition; in particular, the 66 codes represented in the historical bank are not asserted to exhaust Chapter 87. Detailed diagnostics of residual exact or near-duplicate descriptions and other partition-validity conditions are reserved for Section 4.4.

# PART II — Spanish semantic-control mirror

## 4.1. Entorno y alcance experimental

El experimento evaluó, de manera offline, una instanciación concreta de la arquitectura de la Sección 3 utilizando descripciones comerciales y etiquetas administrativas de referencia en el nivel NANDINA de ocho dígitos dentro del Capítulo 87. Cada registro de SERIE constituyó la unidad de análisis. Como varias series pueden pertenecer a una misma DAM/declaración aduanera y compartir estructura a nivel de declaración, la DAM se conservó como unidad de agrupamiento cuando esa dependencia resultaba metodológicamente relevante para el particionamiento o la inferencia. La evaluación utilizó datasets fijos y procedimientos computacionales controlados; no constituyó un despliegue operativo aduanero ni una adjudicación de la clasificación jurídica.

El Capítulo 87 y el nivel NANDINA de ocho dígitos delimitan únicamente esta instanciación empírica. Las interfaces definidas en la Sección 3 pueden reinstanciarse con otros bancos históricos, espacios de clases objetivo, profundidades arancelarias o corpus documentales compatibles cuando se satisfacen sus requisitos declarados. Esa configurabilidad es una propiedad de diseño y no implica que el desempeño observado en el escenario actual se transfiera a otro escenario.

## 4.2. Datos históricos y construcción de los datasets experimentales

Los datos históricos se construyeron mediante cuatro operaciones diferenciadas: recolección desde la fuente administrativa, transformación automatizada en registros a nivel de serie, curación y construcción de particiones agrupadas por DAM. Mantener separadas estas operaciones permite distinguir la procedencia de los registros administrativos de la representación procesada utilizada en el experimento.

### 4.2.1. Fuente y recolección

Los casos comerciales se recolectaron mediante el portal Aduanet de SUNAT para el régimen de importación para el consumo en la Aduana Marítima del Callao (código 118). Las DAM elegibles fueron declaraciones numeradas entre el 2 de enero y el 30 de marzo de 2026, recolectadas entre el 11 y el 20 de abril de 2026, asignadas a canal naranja o rojo, con fecha de cancelación registrada y levante autorizado, y con al menos una partida del Capítulo 87. La recolección fue intencional y no probabilística, y aplicó estos criterios administrativos, temporales, temáticos y de disponibilidad de datos.

Una vez identificada una DAM elegible, se ingresó a la declaración en Aduanet y sus series se copiaron manualmente en un registro intermedio de recolección. Para cada serie se conservaron los datos necesarios para vincular la unidad de análisis con su declaración de origen y su etiqueta administrativa de referencia: identificador de la declaración, número de serie, descripción comercial y código NANDINA de ocho dígitos registrado. Las capturas de consulta se conservaron como evidencia del procedimiento de recolección y no se utilizaron como una fuente adicional de etiquetas. El contenido procesado necesario para el experimento pudo reconstruirse funcionalmente a partir del material de recolección disponible; sin embargo, no se afirma que el workbook completo disponible actualmente sea byte a byte idéntico al original histórico.

### 4.2.2. Procesamiento y curación

Los registros recolectados se transformaron en Python en una representación tabular con una fila por SERIE. El procesamiento identificó bloques de declaración y serie, extrajo los campos asociados con cada serie, conservó las líneas disponibles de descripción de mercancías, las concatenó en la representación de la descripción comercial y generó un identificador reproducible de serie a partir de la información de declaración y serie. La preparación textual estandarizó el espaciado, mientras que el campo de código arancelario se transformó en su representación NANDINA de ocho dígitos y en los campos jerárquicos correspondientes para efectuar controles de consistencia.

Los controles de calidad exigieron los campos necesarios para identificar la serie y su código de referencia, una descripción comercial no vacía, un código NANDINA válido de ocho dígitos, coherencia jerárquica, pertenencia al Capítulo 87 y ausencia de advertencias críticas de parseo que afectaran la declaración, la serie o el código arancelario. Los registros repetidos que compartían un identificador de serie se trataron según su contenido: los duplicados con contenido no técnico idéntico se redujeron a un único registro estable, mientras que los registros conflictivos de un mismo identificador se excluyeron como grupo. El intermedio reconstruido contenía 11,320 series procedentes de 107 DAM. El filtrado al Capítulo 87 produjo 4,232 registros antes de la curación y 4,106 registros curados para construir el benchmark versión 0.2.

### 4.2.3. Construcción de particiones y composición

Los 4,106 registros curados se asignaron a un banco histórico, un conjunto de desarrollo y un conjunto de evaluación. La versión 0.2 se materializó mediante asignaciones explícitas de DAM completas a las tres particiones; la semilla aleatoria registrada constituye metadato de procedencia y no fue el mecanismo utilizado para asignar los registros de la versión 0.2. Por ello, la DAM funcionó como unidad de agrupamiento para construir las particiones. Las particiones finales no presentan solapamiento de DAM ni solapamiento de los identificadores reproducibles de serie entre conjuntos.

El banco histórico contiene 2,950 series de 28 DAM y 66 códigos representados. El conjunto de desarrollo contiene 100 series de 6 DAM y 9 códigos representados. El conjunto de evaluación contiene 1,056 series de 67 DAM y 42 códigos de referencia representados. Estos conteos caracterizan las etiquetas presentes en cada partición; en particular, no se afirma que los 66 códigos representados en el banco histórico agoten el Capítulo 87. Los diagnósticos detallados de descripciones duplicadas exactas o cercanas y otras condiciones de validez de las particiones se reservan para la Sección 4.4.
