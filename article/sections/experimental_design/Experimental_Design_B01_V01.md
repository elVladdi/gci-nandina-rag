# PART I — English manuscript master

## 4.1. Evaluation setting

The empirical evaluation was conducted offline as a non-binding decision-support pilot for NANDINA subheading recommendation within Chapter 87. Each SERIE constitutes one analysis unit. Because several series can belong to the same DAM/customs declaration and may therefore share declaration-level information, DAM is treated as the grouping unit whenever dependence is relevant. The v0.2 data partition used in this study was materialized by DAM, with no DAM shared across the historical, development, and evaluation partitions. Detailed dependence, duplicate, and near-duplicate diagnostics are reported separately in Section 4.4.

This setting evaluates the implemented procedure under a bounded customs-classification scenario rather than an operational deployment or legal adjudication process. The study does not treat the generated recommendations as legally binding customs classifications. Chapter 87 defines the empirical scope of this evaluation; it does not redefine the more general interface requirements stated in Section 3, and no empirical generalization beyond the evaluated setting is inferred from this design.

## 4.2. Historical data

The historical-data component was instantiated from a versioned pipeline that converted series-level customs records into a curated Chapter-87 pool and then materialized fixed historical, development, and evaluation datasets. The following subsections distinguish source provenance, represented code space, curation operations, and the frozen identities of the datasets used in the experiment.

### 4.2.1. Data source and selection

The reconstruction of the historical-data pipeline used the workbook `data/Series - Descripciones.xlsx` as the available source file. The current copy has SHA-256 `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`. The series parser opens the workbook in read-only, data-only mode and, when no worksheet is specified, processes the first worksheet. The historical run therefore processed `Hoja2`, which was worksheet index 0 in the relevant workbook ordering. The parser identifies DAM blocks and their associated series-detail tables, preserves the source labels, constructs the business key `id_unico` from `DECLARACION` and `SERIE`, and records source and row-level traceability fields.

The available workbook is sufficient to reproduce the parser-processed content relevant to the frozen datasets, but it is not byte-identical to the complete historical workbook. Historical metadata records a different source SHA-256 from the current workbook. Accordingly, the provenance claim is limited to functional reproduction of the processed content and the derived datasets, not binary identity of the original workbook. The reconstructed intermediate contains 11,320 series from 107 DAM. Restricting the records to Chapter 87 yields 4,232 rows before curation and 4,106 curated records used as the source pool for the frozen v0.2 partition.

### 4.2.2. Target class space

The empirical code space is limited to eight-digit NANDINA codes whose derived class field is `87`. This scope was applied to the curated series records before the v0.2 partition was materialized. The resulting historical bank H100 contains 66 represented codes, the development set contains 9 represented codes, and the evaluation set contains 42 represented reference codes.

These counts describe the codes present in the three frozen datasets; they do not claim to enumerate every possible Chapter-87 code. In particular, the 66 codes in H100 are the codes represented in the historical bank used by this instantiation, and the 42 evaluation codes are the reference labels represented among the evaluation series. The unit evaluated remains the SERIE record, while DAM is retained as the grouping variable for partition construction and later analyses that require dependence control.

### 4.2.3. Preparation and curation

The source workbook is first parsed into a flat series-level table. The parser cleans cell text by trimming surrounding whitespace, replacing non-breaking spaces, and collapsing repeated whitespace; it preserves the visible NANDINA value and derives the corresponding class, four-digit heading, six-digit subheading, and eight-digit NANDINA fields from its digits. Merchandise-description lines are retained and concatenated into a series-level description field, while technical columns preserve the source file, worksheet, DAM block, series row range, and parser warnings.

Curation then selects records whose derived class equals `87` and applies explicit quality rules. A record is excluded when required fields are missing, the NANDINA field is not an eight-digit code, the derived class/heading/subheading hierarchy is inconsistent with that code, or a critical parser warning affects `DECLARACION`, `SERIE`, or `NANDINA`. Records that pass these checks are grouped by `id_unico`. If repeated rows for the same `id_unico` have identical non-technical content, the first stable occurrence is retained and the excess rows are excluded; if the repeated rows conflict, the entire `id_unico` group is excluded. These operations produced 4,106 curated Chapter-87 records.

Version v0.2 was then materialized from the curated source pool using the frozen `T5-safe-159` configuration. Partition membership is defined by explicit DAM lists rather than by a new random draw or model-performance criterion. Although `seed = 2026` is retained in the configuration for provenance, it is not the mechanism that assigns v0.2 records. All 4,106 curated records are assigned once, with zero DAM overlap and zero `id_unico` overlap across the historical, development, and evaluation partitions. More detailed cross-partition duplicate and near-duplicate analyses are deferred to Section 4.4.

### 4.2.4. Versioned datasets used in the experiment

The historical bank used in the experiment is `data/processed/data_aduanas_historico_clase87_v0.2.csv`. It contains 2,950 series from 28 DAM and 66 represented codes; its SHA-256 is `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.

The development dataset is `data/processed/data_aduanas_devset_clase87_v0.2.csv`. It contains 100 series from 6 DAM and 9 represented codes; its SHA-256 is `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`.

The evaluation dataset is `data/processed/data_aduanas_evalset_clase87_v0.2.csv`. It contains 1,056 series from 67 DAM and 42 represented reference codes; its SHA-256 is `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`. The split metadata records historical support for all 1,056 evaluation cases without using retrieval or model-performance metrics to choose the v0.2 assignment.

The three v0.2 CSV files were reproduced byte for byte during the forensic reconstruction of the processing chain. This supports the identity of the processed datasets used in the experiment while preserving the separate limitation that the complete original workbook cannot be claimed to be byte-identical to the currently available workbook.

# PART II — Spanish semantic-control mirror

## 4.1. Entorno de evaluación

La evaluación empírica se realizó offline como un piloto no vinculante de apoyo a decisiones para la recomendación de subpartidas NANDINA dentro del Capítulo 87. Cada SERIE constituye una unidad de análisis. Como varias series pueden pertenecer a una misma DAM/declaración aduanera y, por ello, compartir información a nivel de declaración, la DAM se trata como unidad de agrupamiento cuando la dependencia es relevante. La partición v0.2 utilizada en este estudio se materializó por DAM, sin compartir una misma DAM entre los conjuntos histórico, de desarrollo y de evaluación. Los diagnósticos detallados de dependencia, duplicados y near-duplicates se presentan por separado en la Sección 4.4.

Este escenario evalúa el procedimiento implementado dentro de un contexto aduanero acotado y no como un despliegue operativo ni como un proceso de adjudicación jurídica. El estudio no trata las recomendaciones generadas como clasificaciones aduaneras jurídicamente vinculantes. El Capítulo 87 delimita el alcance empírico de esta evaluación; no redefine los requisitos generales de interfaz establecidos en la Sección 3 ni permite inferir generalización empírica fuera del escenario evaluado.

## 4.2. Datos históricos

El componente de datos históricos se instanció mediante un pipeline versionado que transformó registros aduaneros a nivel de serie en un conjunto curado del Capítulo 87 y, posteriormente, materializó datasets fijos para histórico, desarrollo y evaluación. Las subsecciones siguientes separan la procedencia de la fuente, el espacio de códigos representado, las operaciones de curación y las identidades congeladas de los datasets utilizados en el experimento.

### 4.2.1. Fuente y selección de datos

La reconstrucción del pipeline de datos históricos utilizó como archivo fuente disponible el workbook `data/Series - Descripciones.xlsx`. La copia actual tiene SHA-256 `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`. El parser de series abre el workbook en modo de solo lectura y con valores calculados y, cuando no se especifica una hoja, procesa la primera worksheet. Por ello, la ejecución histórica procesó `Hoja2`, que ocupaba el índice 0 en el orden de hojas pertinente. El parser identifica bloques DAM y sus tablas de detalle de series, conserva las etiquetas de la fuente, construye la clave de negocio `id_unico` a partir de `DECLARACION` y `SERIE` y registra campos de trazabilidad de archivo y filas de origen.

El workbook disponible permite reproducir funcionalmente el contenido procesado por el parser que es pertinente para los datasets congelados, pero no es byte-identificable con el workbook histórico completo. La metadata histórica registra un SHA-256 de fuente distinto al de la copia actual. En consecuencia, la afirmación de procedencia se limita a la reproducción funcional del contenido procesado y de los datasets derivados, no a la identidad binaria de la fuente original. El intermedio reconstruido contiene 11,320 series de 107 DAM. Al restringir los registros al Capítulo 87 se obtienen 4,232 filas antes de la curación y 4,106 registros curados que constituyen el pool de origen de la partición v0.2 congelada.

### 4.2.2. Espacio de clases objetivo

El espacio empírico de códigos se limita a códigos NANDINA de ocho dígitos cuyo campo de clase derivado es `87`. Este alcance se aplicó a los registros de series curados antes de materializar la partición v0.2. El banco histórico H100 resultante contiene 66 códigos representados, el conjunto de desarrollo contiene 9 códigos representados y el conjunto de evaluación contiene 42 códigos de referencia representados.

Estas cantidades describen los códigos presentes en los tres datasets congelados; no constituyen una enumeración exhaustiva de todos los códigos posibles del Capítulo 87. En particular, los 66 códigos de H100 son los códigos representados en el banco histórico utilizado por esta instanciación, mientras que los 42 códigos de evaluación corresponden a las etiquetas de referencia representadas entre las series de evaluación. La unidad evaluada sigue siendo la SERIE y la DAM se conserva como variable de agrupamiento para construir las particiones y para los análisis posteriores que requieran controlar dependencia.

### 4.2.3. Preparación y curación

El workbook fuente se transforma primero en una tabla plana a nivel de serie. El parser limpia el texto de las celdas eliminando espacios periféricos, sustituyendo espacios no separables y colapsando espacios repetidos; conserva el valor NANDINA visible y deriva a partir de sus dígitos la clase, la partida de cuatro dígitos, la subpartida de seis dígitos y el código NANDINA de ocho dígitos. Las líneas de descripción de mercancías se conservan y concatenan en un campo de descripción a nivel de serie, mientras que las columnas técnicas registran el archivo y la hoja de origen, el bloque DAM, el rango de filas de la serie y las advertencias del parser.

La curación selecciona después los registros cuya clase derivada es `87` y aplica reglas de calidad explícitas. Un registro se excluye cuando faltan campos obligatorios, el campo NANDINA no contiene un código de ocho dígitos, la jerarquía derivada de clase/partida/subpartida no es consistente con ese código o existe una advertencia crítica del parser que afecta `DECLARACION`, `SERIE` o `NANDINA`. Los registros que superan estos controles se agrupan por `id_unico`. Si las filas repetidas de un mismo `id_unico` tienen contenido no técnico idéntico, se conserva la primera aparición estable y se excluyen las restantes; si las filas repetidas presentan conflicto, se excluye todo el grupo `id_unico`. Estas operaciones produjeron 4,106 registros curados del Capítulo 87.

La versión v0.2 se materializó a continuación a partir del pool curado mediante la configuración congelada `T5-safe-159`. La pertenencia a cada partición está definida por listas explícitas de DAM y no por un nuevo sorteo aleatorio ni por un criterio basado en desempeño del modelo. Aunque `seed = 2026` se conserva en la configuración por razones de procedencia, no es el mecanismo que asigna los registros de v0.2. Los 4,106 registros curados quedan asignados una sola vez, con cero solapamiento de DAM y cero solapamiento de `id_unico` entre histórico, desarrollo y evaluación. Los análisis más detallados de duplicados y near-duplicates entre particiones se difieren a la Sección 4.4.

### 4.2.4. Datasets versionados utilizados en el experimento

El banco histórico utilizado en el experimento es `data/processed/data_aduanas_historico_clase87_v0.2.csv`. Contiene 2,950 series de 28 DAM y 66 códigos representados; su SHA-256 es `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.

El dataset de desarrollo es `data/processed/data_aduanas_devset_clase87_v0.2.csv`. Contiene 100 series de 6 DAM y 9 códigos representados; su SHA-256 es `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`.

El dataset de evaluación es `data/processed/data_aduanas_evalset_clase87_v0.2.csv`. Contiene 1,056 series de 67 DAM y 42 códigos de referencia representados; su SHA-256 es `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`. La metadata de la partición registra soporte histórico para los 1,056 casos de evaluación sin utilizar métricas de recuperación o de desempeño del modelo para seleccionar la asignación v0.2.

Los tres CSV v0.2 fueron reproducidos byte a byte durante la reconstrucción forense de la cadena de procesamiento. Esto respalda la identidad de los datasets procesados utilizados en el experimento y mantiene, al mismo tiempo, la limitación separada de que no puede afirmarse identidad binaria entre el workbook histórico completo y el workbook actualmente disponible.
