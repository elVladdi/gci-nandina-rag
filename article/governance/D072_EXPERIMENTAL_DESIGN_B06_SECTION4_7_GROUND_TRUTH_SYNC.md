# D-072 — Sincronización de ground truth para B06 / Section 4.7 / B06 Section 4.7 ground-truth synchronization

## Español

```text
DECISION_ID = D-072
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-071
BLOCK = EXPERIMENTAL_DESIGN_B06
SECTION = 4.7
SECTION_TITLE = Statistical and robustness analysis
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V014.md
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
SRC03_HEAD_OBSERVED = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_OBSERVED = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
G3_ANALYTICAL_CONTRACT_BLOB = 76862c10fd84fd70588da2d65f96dbe3b40914f6
G3_INFERENTIAL_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
G3_CLAIM_REGISTRY_BLOB = f3f6594277bfeede555f10887bcdb922efd23680
B06_GROUND_TRUTH = SYNCHRONIZED
B06_DRAFTING = NOT_AUTHORIZED_UNTIL_PROMPT_REVIEW_AND_DECISION
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Función de Section 4.7

Section 4.7 debe describir **procedimientos estadísticos, inferenciales, de sensibilidad y robustez**, no sus valores observados ni la disposición final de hipótesis. Debe conservar la separación entre Methods y Results.

La unidad científica primaria permanece en la SERIE. Cuando existe dependencia entre series de una misma DAM/declaración, DAM es la unidad de agrupamiento para el procedimiento de remuestreo. El estimando continúa siendo ponderado por series; no puede sustituirse por una media no ponderada de medias por DAM.

### 2. Procedimiento inferencial autorizado

Para las comparaciones de early-ranking entre recuperación histórica y cada familia comparable corregida —BM25 normativo plano, BM25 normativo jerárquico y D1a inspirado en Text2Trade— el objeto inferencial es la diferencia pareada por serie `historical - comparator` para:

- Top-1;
- Top-3;
- Top-5;
- Top-10;
- MRR@100.

La dependencia se trata mediante bootstrap pareado por clusters DAM:

```text
BOOTSTRAP_CLUSTER = DAM / DECLARATION
BOOTSTRAP_REPLICATES = 10000
BOOTSTRAP_SEED = 20263001
RNG = numpy.random.default_rng / PCG64
NUMBER_OF_DAM_CLUSTERS = 67
PAIRING = SAME_CASES_AND_SAME_RESAMPLED_DAM_MATRIX_ACROSS_STRATEGIES
ESTIMAND = SERIES_WEIGHTED_PAIRED_DIFFERENCE
PRIMARY_INTERVAL = TWO_SIDED_99_PERCENT_PERCENTILE
FAMILYWISE_RULE = BONFERRONI_95_PERCENT_WITHIN_EACH_FIVE_METRIC_STRATEGY_FAMILY
P_VALUES = NONE
```

Cuando una DAM aparece múltiples veces en una réplica bootstrap, todas sus series entran con la misma multiplicidad. El denominador de cada réplica es el número de series resultante de esas multiplicidades.

Top-50 es suplementario y, si se describe metodológicamente, usa intervalo percentil bilateral del 95%; no tiene función en la decisión primaria HE2_A.

### 3. Cobertura profunda

El único contraste inferencial de cobertura profunda congelado es:

`corrected hierarchical Recall@200 - Recall@100`.

Usa el mismo bootstrap pareado por DAM, 10.000 réplicas y seed 20263001, con intervalo percentil bilateral del 95%. No se aplica ajuste de multiplicidad porque existe un único contraste. `Pool@200` no debe duplicarse como segundo contraste confirmatorio.

### 4. Medida de efecto e interpretación

No se introduce retrospectivamente una medida de efecto estandarizada. La medida congelada es la **diferencia absoluta pareada de contribuciones** sobre la métrica correspondiente. No se calculan p-values. Los intervalos describen incertidumbre de remuestreo cluster-aware dentro del benchmark interno fijo de Chapter 87 y no establecen validez para una población externa.

### 5. Sensibilidad y robustez — estatus permitido

Los siguientes análisis pueden describirse únicamente con su estatus metodológico congelado, sin trasladar resultados observados a Methods:

- **Historical-bank sensitivity H25/H50/H75 frente a referencia H100:** `DESCRIPTIVE_SENSITIVITY`; tamaño y composición varían conjuntamente, por lo que no estima un efecto causal aislado del tamaño.
- **H150/H200 sobre diez seeds pareados y el mismo EVAL:** `DESCRIPTIVE_ONLY`; no existe superpoblación congelada de seeds y las 10 × 1.056 filas no son observaciones independientes.
- **Corrective 0B-05C Attempt06:** sensibilidad descriptiva bajo el estado corregido gobernado; intentos superseded quedan excluidos.
- **Phase-E candidate pools:** inventarios descriptivos de cobertura; no son rankings alternativos ni contrastes inferenciales.
- **EXP12 diversity:** `NOT_ESTIMABLE`; no se produjeron condiciones/retrievals seleccionados D-HIGH/D-MID/D-LOW y no debe reabrirse o inventarse un efecto.
- **Ambiguous/incomplete descriptions:** prevalencia no estimable porque `description_quality_operationalized=0`.
- **Hierarchical proximity:** categorías descriptivas `SAME_CHAPTER`, `SAME_HS4`, `SAME_HS6`; no existe umbral congelado de concentración.
- **Historical support:** usar literalmente `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`; no etiquetar post hoc ningún bucket como “insufficient”.

### 6. Fronteras obligatorias

- No reportar point estimates, intervalos observados ni conclusiones de superioridad en 4.7.
- No declarar HE2 `SUPPORTED` ni HE5 `INCONCLUSIVE` en Methods; esas son disposiciones de resultados.
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`.
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`.
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- No p-values.
- No standardized post-hoc effect size.
- No inferencia a población externa.
- No reejecución experimental ni recomputación de métricas durante redacción.

### 7. Estado de fuentes

La IA Gestora re-verificó antes de esta decisión:

- `main = db0d0ad0d8435921a7838db6720eaea86a263763`;
- `SRC-03 = 87422102290a4f9a89c51e936cf7274d8e4687d8`;
- Plan Maestro blob `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`.

No existe drift material respecto del corte usado para B05/B06. La IA de Redacción debe volver a verificar estas identidades al ejecutar B06 y detenerse si un drift posterior altera materialmente 4.7.

---

## English

```text
DECISION_ID = D-072
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-071
BLOCK = EXPERIMENTAL_DESIGN_B06
SECTION = 4.7
SECTION_TITLE = Statistical and robustness analysis
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
SRC03_HEAD_OBSERVED = 87422102290a4f9a89c51e936cf7274d8e4687d8
DEVELOPMENT_MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
B06_GROUND_TRUTH = SYNCHRONIZED
B06_DRAFTING = NOT_AUTHORIZED_UNTIL_PROMPT_REVIEW_AND_DECISION
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Section 4.7 reports statistical, inferential, sensitivity, and robustness procedures without observed result values or final hypothesis dispositions. SERIE remains the primary analysis unit; DAM is the dependence cluster. The estimand remains series-weighted rather than an unweighted mean of DAM-level means.

For each corrected early-ranking comparator, the five primary paired historical-minus-comparator contributions are Top-1, Top-3, Top-5, Top-10, and MRR@100. The frozen procedure uses 10,000 paired DAM-cluster bootstrap replicates, seed 20263001, a common resampled-DAM matrix across strategies, two-sided 99% percentile intervals, and the within-strategy Bonferroni familywise 95% rule. No p-values are calculated. Top-50 is supplementary with a two-sided 95% interval and no primary decision role.

The single deep-coverage inferential contrast is corrected hierarchical `Recall@200 - Recall@100`, evaluated with the same DAM-cluster bootstrap and a two-sided 95% percentile interval without multiplicity adjustment. Pool@200 is not a second confirmatory contrast.

No standardized post-hoc effect measure is introduced; the frozen absolute paired contribution difference is the effect measure. Resampling uncertainty is internal to the fixed Chapter-87 benchmark and does not establish external-population validity.

Sensitivity and robustness families retain their frozen statuses: H25/H50/H75 versus H100 is descriptive joint size/composition sensitivity; H150/H200 across ten paired seeds is descriptive only and does not support seed-superpopulation inference; corrected 0B-05C Attempt06 remains descriptive; Phase-E pools are descriptive coverage inventories; EXP12 diversity is not estimable; ambiguous/incomplete-description prevalence is not estimable; hierarchy categories are descriptive; and historical-support buckets must retain their literal definitions without a post-hoc insufficiency threshold.

Methods must not report observed estimates or confidence intervals, declare final hypothesis dispositions, introduce p-values or standardized post-hoc effect sizes, claim external-population inference, or recompute experimental results during drafting.