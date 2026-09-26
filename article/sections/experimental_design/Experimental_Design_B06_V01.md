# Experimental Design B06 V01 — Section 4.7

```text
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
VERSION = V01
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
GOVERNING_DECISION = D-073
GROUND_TRUTH_DECISION = D-072
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V014.md
BASELINE_MASTER_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
BASELINE_MASTER_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
BASELINE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
SRC03_HEAD_READ = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_READ = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_READ = db0d0ad0d8435921a7838db6720eaea86a263763
AUTHORIZED_SCOPE = SECTION_4_7_ONLY
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Part I — English manuscript text

## 4.7. Statistical and robustness analysis

The statistical analysis treated DAM/customs declaration as the primary inferential cluster whenever dependence among series records was relevant. Although SERIE remained the unit of analysis and the unit on which retrieval contributions were defined, multiple series can belong to the same declaration and therefore were not treated as fully independent observations for resampling. The target estimand remained series-weighted: inferential procedures aggregated contributions over the resampled series records rather than replacing them with an unweighted average of declaration-level means.

For the eligible HE2 comparisons, uncertainty was estimated with a paired DAM-cluster bootstrap. In each replicate, DAM clusters were sampled with replacement and every SERIE belonging to each selected declaration was carried into the resample. The same sampled declarations and series records were used for both members of each paired comparison, after which the series-weighted estimand was recomputed. The procedure used 10,000 bootstrap replicates with the frozen seed 20263001 and two-sided percentile confidence intervals. No p-values were used.

For HE2_A, early-ranking performance was analyzed separately for the corrected flat normative, hierarchical normative, and D1a comparator families. The primary metrics were Top-1, Top-3, Top-5, Top-10, and MRR@100. For each metric, the paired per-series contribution was defined as historical retrieval minus the comparator: a difference in binary hit contributions for Top-k metrics and a difference in reciprocal-rank contributions truncated at rank 100 for MRR@100. Each comparator therefore formed a five-metric family. Within each family, 99% marginal percentile confidence intervals implemented a Bonferroni familywise 95% error-control rule. Top-50 was supplementary and was not part of this primary five-metric familywise procedure.

HE2_B addressed deep coverage as a distinct object from early-ranking performance. The corrected hierarchical retrieval family was compared at depths 100 and 200 using the paired per-series contribution `hit_recall_200 - hit_recall_100`. This single contrast used the same paired DAM-cluster bootstrap design, 10,000 replicates, seed 20263001, and one two-sided 95% percentile confidence interval. Because HE2_B contained one inferential contrast, no multiplicity adjustment was applied to that comparison.

Sensitivity and robustness families that were not eligible for inferential claims were retained as descriptive analyses. EXP11A compared H25, H50, and H75 conditions against the frozen H100 reference as a joint sensitivity to historical-bank size and composition; because those two properties changed together, the analysis does not isolate a causal effect of bank size. EXP11B compared paired H150 and H200 banks across the ten frozen paired seeds on the same evaluation set; those repeated case-level rows were not treated as independent observations, and the design does not support inference to a superpopulation of seeds. The final 0B-05C Attempt06 family was treated only as a descriptive corrective sensitivity under its fixed controls, without adding causal or significance claims. Phase-E candidate pools were likewise used only as descriptive coverage inventories and did not replace the primary historical ranking or its inferential comparisons. EXP12 remained not estimable because the frozen diversity conditions did not produce retrieval outputs, and the HE5 evidence families remained descriptive; no post-hoc threshold or new inferential test was introduced for them.

These procedures quantify uncertainty and sensitivity within the fixed offline Chapter-87 benchmark. They do not establish empirical generalization beyond the evaluated setting, legal validity, or performance in operational customs deployment. Candidate-retrieval analysis remains distinct from overall classification accuracy, documentary association remains distinct from substantive normative or legal correctness, and explanation auditability remains distinct from legal correctness. Numerical effects, confidence-interval bounds, hypothesis dispositions, and other observed outcomes are reported only in Results.

## Part II — Spanish semantic-control mirror

## 4.7. Análisis estadístico y de robustez

El análisis estadístico trató a la DAM/declaración aduanera como el cluster inferencial primario cuando la dependencia entre series era relevante. Aunque la SERIE se mantuvo como unidad de análisis y como unidad sobre la que se definieron las contribuciones de recuperación, varias series pueden pertenecer a una misma declaración y, por tanto, no se trataron como observaciones plenamente independientes para el remuestreo. El estimando objetivo se mantuvo ponderado por SERIE: los procedimientos inferenciales agregaron contribuciones sobre las series remuestreadas en lugar de sustituirlas por un promedio no ponderado de medias a nivel de declaración.

Para las comparaciones HE2 elegibles, la incertidumbre se estimó mediante un bootstrap pareado por clusters de DAM. En cada réplica se muestrearon clusters de DAM con reemplazo y se incorporaron al remuestreo todas las SERIE pertenecientes a cada declaración seleccionada. Las mismas declaraciones y series remuestreadas se utilizaron para ambos miembros de cada comparación pareada, tras lo cual se recalculó el estimando ponderado por SERIE. El procedimiento utilizó 10.000 réplicas bootstrap con la semilla congelada 20263001 e intervalos de confianza percentiles bilaterales. No se utilizaron p-values.

Para HE2_A, el desempeño en posiciones tempranas se analizó por separado para las familias comparadoras corregidas normativa plana, normativa jerárquica y D1a. Las métricas primarias fueron Top-1, Top-3, Top-5, Top-10 y MRR@100. Para cada métrica, la contribución pareada por SERIE se definió como recuperación histórica menos el comparador: una diferencia de contribuciones binarias de acierto para las métricas Top-k y una diferencia de contribuciones de rango recíproco truncadas en el rank 100 para MRR@100. Cada comparador constituyó, por tanto, una familia de cinco métricas. Dentro de cada familia, intervalos de confianza percentiles marginales de 99% implementaron una regla de control Bonferroni del error familiar al 95%. Top-50 fue suplementaria y no formó parte de este procedimiento familiar primario de cinco métricas.

HE2_B abordó la cobertura profunda como un objeto distinto del desempeño en posiciones tempranas. La familia de recuperación jerárquica corregida se comparó en profundidades 100 y 200 mediante la contribución pareada por SERIE `hit_recall_200 - hit_recall_100`. Este contraste único utilizó el mismo diseño de bootstrap pareado por clusters de DAM, 10.000 réplicas, semilla 20263001 y un intervalo de confianza percentil bilateral de 95%. Debido a que HE2_B contenía un único contraste inferencial, no se aplicó ajuste por multiplicidad a esa comparación.

Las familias de sensibilidad y robustez que no eran elegibles para claims inferenciales se conservaron como análisis descriptivos. EXP11A comparó las condiciones H25, H50 y H75 con la referencia H100 congelada como sensibilidad conjunta al tamaño y la composición del banco histórico; dado que ambas propiedades cambiaban conjuntamente, el análisis no aísla un efecto causal del tamaño del banco. EXP11B comparó bancos H150 y H200 pareados sobre los diez seeds pareados congelados y el mismo conjunto de evaluación; esas filas repetidas a nivel de caso no se trataron como observaciones independientes y el diseño no sustenta inferencia hacia una superpoblación de seeds. La familia final 0B-05C Attempt06 se trató únicamente como sensibilidad correctiva descriptiva bajo sus controles fijados, sin añadir claims causales ni de significancia. Los pools de candidatos de la Fase E se utilizaron igualmente solo como inventarios descriptivos de cobertura y no sustituyeron el ranking histórico primario ni sus comparaciones inferenciales. EXP12 permaneció no estimable porque las condiciones de diversidad congeladas no produjeron salidas de recuperación, y las familias de evidencia HE5 permanecieron descriptivas; no se introdujo para ellas ningún umbral post hoc ni una nueva prueba inferencial.

Estos procedimientos cuantifican incertidumbre y sensibilidad dentro del benchmark offline fijo del Capítulo 87. No establecen generalización empírica fuera del escenario evaluado, validez jurídica ni desempeño en un despliegue aduanero operativo. El análisis de recuperación de candidatos permanece separado de la accuracy global de clasificación, la asociación documental permanece separada de la corrección normativa o jurídica sustantiva y la auditabilidad de la explicación permanece separada de la corrección jurídica. Los efectos numéricos, los límites de los intervalos de confianza, las decisiones de hipótesis y los demás resultados observados se reportan únicamente en Resultados.
