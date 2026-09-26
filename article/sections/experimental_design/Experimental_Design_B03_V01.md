# Experimental Design B03 V01 — Section 4.4

```text
BLOCK = EXPERIMENTAL_DESIGN_B03_SECTION_4_4
VERSION = V01
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V011.md
BASELINE_MASTER_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
BASELINE_MASTER_GIT_BLOB = c2aee16c219ed33c16e8e647fbd56f4dacc2cd61
SRC03_HEAD_READ = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_BLOB_READ = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_READ = db0d0ad0d8435921a7838db6720eaea86a263763
AUTHORIZED_SCOPE = SECTION_4_4_ONLY
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Part I — English manuscript text

### 4.4. Partition validity and dependence controls

The current benchmark uses declaration-level separation because the historical v0.1 split did not constrain records from the same DAM/customs declaration to a single partition. That historical snapshot selected individual series records by proportional stratification on NANDINA code with seed 2026; consequently, series belonging to one declaration could be distributed across historical, development, and evaluation data. Because a DAM may contain multiple series that share declaration-level context and may also contain similar merchandise descriptions or tariff codes, such cross-partition sharing left a potential dependence and leakage path. This limitation motivated the declaration-grouped redesign; v0.1 is retained only as a historical snapshot and does not govern the current benchmark.

In v0.2, the curated union was repartitioned through explicit DAM assignments. Each DAM was assigned in full to exactly one of the historical, development, or evaluation partitions, yielding H100 with 2,950 series from 28 DAMs and 66 represented codes, DEV with 100 series from 6 DAMs and 9 represented codes, and EVAL with 1,056 series from 67 DAMs and 42 represented codes. The resulting pairwise DAM overlap is zero. The split configuration also requires zero cross-partition overlap of `id_unico` and full assignment of the curated Chapter-87 records. These are distinct controls: the `seed=2026` field is retained as configuration provenance, whereas v0.2 membership is materialized from explicit DAM lists rather than randomized by that seed.

A separate historical-support condition requires each evaluation series to have its reference eight-digit NANDINA code represented in the historical partition. The frozen v0.2 audit records this condition for all 1,056 evaluation series and all 42 represented evaluation codes. This establishes that the reference class of each evaluated series is present in the historical bank; it does not imply that historical retrieval places that reference code at any particular rank and is not a candidate-retrieval performance result.

Textual duplication was assessed separately from declaration grouping. Exact cross-partition matches were defined on normalized merchandise descriptions, while near-duplicate diagnostics compared historical and evaluation descriptions with token-set Jaccard similarity at thresholds 0.90, 0.95, and 0.98. These thresholds were diagnostic checks: they did not determine v0.2 partition membership and were not automatic exclusion filters. Likewise, the earlier treatment of repeated or conflicting records keyed by `id_unico` addresses record identity rather than declaration-level dependence. Zero DAM overlap, zero `id_unico` overlap, exact-description checks, and near-duplicate diagnostics therefore represent different validity controls and should not be treated as interchangeable guarantees.

SERIE remains the analysis unit, while DAM is the grouping unit whenever dependence among series is methodologically relevant. Assigning whole declarations to one partition prevents the same DAM from contributing records to both the historical bank and the evaluation set, but it does not make series within a DAM statistically independent. The 1,056 evaluation series must therefore not be interpreted automatically as 1,056 independent inferential observations. The partition controls make cross-partition declaration sharing and residual textual similarity observable within the evaluated Chapter-87 setting, but they do not establish i.i.d. sampling or eliminate every possible source of dependence or lexical similarity across different declarations. Statistical units, assumptions, and inferential procedures are reserved for Section 4.7.

## Part II — Spanish semantic-control mirror

### 4.4. Validez de las particiones y controles de dependencia

El benchmark vigente utiliza separación a nivel de declaración porque el split histórico v0.1 no restringía los registros de una misma DAM/declaración aduanera a una sola partición. Ese snapshot histórico seleccionaba series individuales mediante estratificación proporcional por código NANDINA con seed 2026; en consecuencia, series pertenecientes a una misma declaración podían distribuirse entre los conjuntos histórico, desarrollo y evaluación. Debido a que una DAM puede contener varias series que comparten contexto a nivel de declaración y también puede contener descripciones de mercancías o códigos arancelarios similares, ese reparto entre particiones dejaba una vía potencial de dependencia y leakage. Esta limitación motivó el rediseño agrupado por declaración; v0.1 se conserva únicamente como snapshot histórico y no gobierna el benchmark vigente.

En v0.2, la unión curada se volvió a particionar mediante asignaciones explícitas de DAM. Cada DAM se asignó íntegramente a una sola de las particiones histórica, desarrollo o evaluación, obteniéndose H100 con 2.950 series de 28 DAM y 66 códigos representados, DEV con 100 series de 6 DAM y 9 códigos representados, y EVAL con 1.056 series de 67 DAM y 42 códigos representados. El solapamiento de DAM resultante es cero para cada par de particiones. La configuración del split también exige ausencia de solapamiento de `id_unico` entre particiones y asignación completa de los registros curados del Capítulo 87. Estos son controles distintos: el campo `seed=2026` se conserva como procedencia de configuración, mientras que la pertenencia a v0.2 se materializa a partir de listas explícitas de DAM y no se aleatoriza mediante ese seed.

Una condición separada de soporte histórico exige que cada serie de evaluación tenga su código NANDINA de referencia de ocho dígitos representado en la partición histórica. La auditoría congelada v0.2 registra esta condición para las 1.056 series de evaluación y los 42 códigos representados en evaluación. Esto establece que la clase de referencia de cada serie evaluada está presente en el banco histórico; no implica que la recuperación histórica sitúe ese código de referencia en una posición determinada y no constituye un resultado de desempeño de recuperación de candidatos.

La duplicación textual se evaluó por separado del agrupamiento por declaración. Las coincidencias exactas entre particiones se definieron sobre descripciones de mercancías normalizadas, mientras que los diagnósticos de near-duplicates compararon descripciones históricas y de evaluación mediante similitud Jaccard sobre conjuntos de tokens con umbrales 0,90, 0,95 y 0,98. Estos umbrales fueron controles diagnósticos: no determinaron la pertenencia a las particiones v0.2 ni funcionaron como filtros automáticos de exclusión. Del mismo modo, el tratamiento previo de registros repetidos o conflictivos basado en `id_unico` aborda identidad de registros y no dependencia a nivel de declaración. Por tanto, ausencia de solapamiento de DAM, ausencia de solapamiento de `id_unico`, controles de descripciones exactas y diagnósticos de near-duplicates representan controles de validez distintos y no deben tratarse como garantías intercambiables.

SERIE se mantiene como unidad de análisis, mientras que DAM es la unidad de agrupamiento cuando la dependencia entre series es metodológicamente relevante. Asignar declaraciones completas a una sola partición evita que una misma DAM aporte registros tanto al banco histórico como al conjunto de evaluación, pero no convierte a las series de una DAM en observaciones estadísticamente independientes. Por ello, las 1.056 series de evaluación no deben interpretarse automáticamente como 1.056 observaciones inferenciales independientes. Los controles de partición hacen observable el reparto de declaraciones entre particiones y la similitud textual residual dentro del escenario evaluado del Capítulo 87, pero no establecen un muestreo i.i.d. ni eliminan toda posible fuente de dependencia o similitud léxica entre declaraciones diferentes. Las unidades estadísticas, los supuestos y los procedimientos inferenciales se reservan para la Sección 4.7.
