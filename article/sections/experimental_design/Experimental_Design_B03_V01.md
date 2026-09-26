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

The current benchmark uses declaration-level separation because the historical v0.1 split did not constrain records from the same DAM/customs declaration to a single partition. That historical snapshot selected individual series records by proportional NANDINA stratification with seed 2026; consequently, series belonging to one declaration could be distributed across historical, development, and evaluation data. Because a DAM may contain multiple series that share declaration-level context and can also contain similar merchandise descriptions or tariff codes, such cross-partition sharing did not rule out dependence between records and left a potential leakage path. This limitation motivated the declaration-grouped redesign; v0.1 is retained only as a historical snapshot and does not govern the reported benchmark.

In v0.2, the curated union was repartitioned by explicit DAM assignments. Each DAM was assigned in full to exactly one of the historical, development, or evaluation partitions, yielding H100 with 2,950 series from 28 DAMs and 66 represented codes, DEV with 100 series from 6 DAMs, and EVAL with 1,056 series from 67 DAMs and 42 represented codes. The resulting pairwise DAM overlap is zero. The configuration also checks zero cross-partition overlap of `id_unico`, full assignment of the curated records, and nominal historical support for the evaluation codes. These are distinct controls: the `seed=2026` field is retained for configuration provenance, whereas the v0.2 membership is materialized from explicit DAM lists rather than randomized by that seed.

SERIE remains the analysis unit, while DAM is the grouping unit whenever dependence among series is methodologically relevant. Assigning whole declarations to one partition prevents the same DAM from contributing records to both the historical bank and the evaluation set, but it does not make series within a DAM independent observations. Accordingly, the 1,056 evaluation series must not be interpreted automatically as 1,056 independent units for inferential procedures that require independence; such analyses must preserve the DAM grouping or otherwise justify how within-DAM dependence is handled.

Textual duplication was assessed separately from declaration grouping. Exact cross-partition matches were defined on normalized merchandise descriptions, while near-duplicate diagnostics compared historical and evaluation descriptions with token-set Jaccard similarity at thresholds 0.90, 0.95, and 0.98. These thresholds were diagnostic checks and did not determine v0.2 partition membership or automatically exclude records. Likewise, the earlier curation of repeated or conflicting records keyed by `id_unico` addresses record identity, not declaration-level dependence. Therefore, zero DAM overlap, zero `id_unico` overlap, exact-description checks, and near-duplicate diagnostics should not be treated as interchangeable guarantees.

These controls establish declaration-disjoint partitions for the evaluated Chapter-87 testbed and make residual similarity observable, but they do not establish i.i.d. sampling or eliminate every possible source of dependence or lexical similarity across different declarations. Subsequent performance summaries and inferential analyses must therefore be interpreted within this partition design, with DAM-level grouping respected whenever independence assumptions are relevant.

## Part II — Spanish semantic-control mirror

### 4.4. Validez de particiones y control de dependencia

El benchmark vigente utiliza separación a nivel de declaración porque el split histórico v0.1 no restringía los registros de una misma DAM/declaración aduanera a una sola partición. Ese snapshot histórico seleccionaba series individuales mediante estratificación proporcional por NANDINA con seed 2026; en consecuencia, series pertenecientes a una misma declaración podían distribuirse entre los conjuntos histórico, desarrollo y evaluación. Debido a que una DAM puede contener varias series que comparten contexto a nivel de declaración y también pueden presentar descripciones de mercancías o códigos arancelarios similares, ese posible reparto entre particiones no descartaba dependencia entre registros y dejaba una vía potencial de leakage. Esta limitación motivó el rediseño agrupado por declaración; v0.1 se conserva únicamente como snapshot histórico y no gobierna el benchmark reportado.

En v0.2, la unión curada se volvió a particionar mediante asignaciones explícitas de DAM. Cada DAM se asignó íntegramente a una sola de las particiones histórica, desarrollo o evaluación, obteniéndose H100 con 2.950 series de 28 DAM y 66 códigos representados, DEV con 100 series de 6 DAM y EVAL con 1.056 series de 67 DAM y 42 códigos representados. El solapamiento de DAM resultante es cero para cada par de particiones. La configuración también comprueba ausencia de solapamiento de `id_unico` entre particiones, asignación completa de los registros curados y soporte histórico nominal para los códigos de evaluación. Estos son controles distintos: el campo `seed=2026` se conserva como procedencia de configuración, mientras que la pertenencia a v0.2 se materializa a partir de listas explícitas de DAM y no se aleatoriza mediante ese seed.

SERIE se mantiene como unidad de análisis, mientras que DAM es la unidad de agrupamiento cuando la dependencia entre series es metodológicamente relevante. Asignar declaraciones completas a una sola partición evita que una misma DAM aporte registros tanto al banco histórico como al conjunto de evaluación, pero no convierte a las series de una DAM en observaciones independientes. Por ello, las 1.056 series de evaluación no deben interpretarse automáticamente como 1.056 unidades independientes en procedimientos inferenciales que requieran independencia; dichos análisis deben preservar el agrupamiento por DAM o justificar de otro modo cómo se trata la dependencia intra-DAM.

La duplicación textual se evaluó por separado del agrupamiento por declaración. Las coincidencias exactas entre particiones se definieron sobre descripciones de mercancías normalizadas, mientras que los diagnósticos de near-duplicates compararon descripciones históricas y de evaluación mediante similitud Jaccard sobre conjuntos de tokens con umbrales 0,90, 0,95 y 0,98. Estos umbrales fueron controles diagnósticos y no determinaron la pertenencia a las particiones v0.2 ni excluyeron registros automáticamente. Del mismo modo, la curación previa de registros repetidos o conflictivos basada en `id_unico` aborda identidad de registros, no dependencia a nivel de declaración. Por tanto, ausencia de solapamiento de DAM, ausencia de solapamiento de `id_unico`, controles de descripciones exactas y diagnósticos de near-duplicates no deben tratarse como garantías intercambiables.

Estos controles establecen particiones disjuntas por declaración para el testbed evaluado del Capítulo 87 y hacen observable la similitud residual, pero no establecen un muestreo i.i.d. ni eliminan toda posible fuente de dependencia o similitud léxica entre declaraciones distintas. En consecuencia, los resúmenes posteriores de desempeño y los análisis inferenciales deben interpretarse dentro de este diseño de partición, respetando el agrupamiento por DAM cuando los supuestos de independencia sean relevantes.
