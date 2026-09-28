# Results B06 V01 — Section 5.6 / Sección 5.6

## Español

### 5.6. Resultados inferenciales

Con el bootstrap pareado por clúster DAM definido en la Sección 4.7, el análisis inferencial mantuvo 1.056 series agrupadas en 67 DAM. Para HE2_A, cada familia de contraste histórico menos comparador incluyó Top-1, Top-3, Top-5, Top-10 y MRR@100, con intervalos de confianza percentiles marginales bilaterales de 99% bajo el control Bonferroni familywise-95% congelado. Los 15 intervalos primarios quedaron completamente por encima de cero; no se calcularon p-values.

Frente a BM25 normativo flat, las diferencias histórico menos comparador fueron Top-1 = 0,482007576, IC 99% [0,329446843; 0,631331820]; Top-3 = 0,620265152 [0,489773908; 0,757505941]; Top-5 = 0,701704545 [0,582607584; 0,817963384]; Top-10 = 0,825757576 [0,737159943; 0,896051128]; y MRR@100 = 0,587410432 [0,463626313; 0,712041394]. Frente a BM25 normativo jerárquico, las diferencias correspondientes fueron 0,482954545 [0,330419446; 0,630822238], 0,619318182 [0,485491905; 0,757028357], 0,700757576 [0,582403679; 0,817063388], 0,825757576 [0,736613432; 0,894902163] y 0,587735966 [0,465199608; 0,712038535]. Frente a D1a corregido, fueron 0,508522727 [0,364702301; 0,653466144], 0,660984848 [0,541305493; 0,781609818], 0,712121212 [0,590534359; 0,832721912], 0,713068182 [0,549548133; 0,860733443] y 0,591620610 [0,487310779; 0,706089907], respectivamente.

El contraste separado HE2_B para la recuperación normativa jerárquica corregida fue Recall@200 - Recall@100 = 0,202651515, con IC 95% [0,066763106; 0,341601308]. Este intervalo también quedó completamente por encima de cero. Como el contraste mide la cobertura exacta adicional al profundizar de 100 a 200 posiciones, y no el desempeño en las primeras posiciones del ranking, se trató por separado de HE2_A.

Dentro del alcance inferencial congelado del benchmark interno de Capítulo 87, las tres familias HE2_A y el contraste primario HE2_B sustentan HE2. Esta disposición se limita a la incertidumbre por remuestreo de clústeres dentro del benchmark fijo y no implica efectos causales, generalización a una población externa, accuracy global del framework ni corrección jurídica. HE5 permaneció inconclusa y no se introdujo para ella un nuevo test inferencial.

## English

### 5.6. Inferential results

Using the paired DAM-cluster bootstrap defined in Section 4.7, the inferential analysis retained 1,056 series nested within 67 DAMs. For HE2_A, each historical-minus-comparator family comprised Top-1, Top-3, Top-5, Top-10, and MRR@100, with two-sided 99% marginal percentile confidence intervals under the frozen Bonferroni familywise-95% control. All 15 primary intervals lay entirely above zero; no p-values were calculated.

Against flat normative BM25, the historical-minus-comparator differences were Top-1 = 0.482007576, 99% CI [0.329446843, 0.631331820]; Top-3 = 0.620265152 [0.489773908, 0.757505941]; Top-5 = 0.701704545 [0.582607584, 0.817963384]; Top-10 = 0.825757576 [0.737159943, 0.896051128]; and MRR@100 = 0.587410432 [0.463626313, 0.712041394]. Against hierarchical normative BM25, the corresponding differences were 0.482954545 [0.330419446, 0.630822238], 0.619318182 [0.485491905, 0.757028357], 0.700757576 [0.582403679, 0.817063388], 0.825757576 [0.736613432, 0.894902163], and 0.587735966 [0.465199608, 0.712038535]. Against corrected D1a, they were 0.508522727 [0.364702301, 0.653466144], 0.660984848 [0.541305493, 0.781609818], 0.712121212 [0.590534359, 0.832721912], 0.713068182 [0.549548133, 0.860733443], and 0.591620610 [0.487310779, 0.706089907], respectively.

The separate HE2_B contrast for corrected hierarchical normative retrieval was Recall@200 - Recall@100 = 0.202651515, with a 95% CI of [0.066763106, 0.341601308]. This interval also lay entirely above zero. Because this contrast measures additional exact coverage between depths 100 and 200 rather than early-ranking performance, it was treated separately from HE2_A.

Within the frozen internal Chapter 87 inferential scope, the three HE2_A families and the primary HE2_B contrast support HE2. This disposition is limited to cluster-resampling uncertainty within the fixed benchmark and does not imply causal effects, external-population generalization, overall framework accuracy, or legal correctness. HE5 remained inconclusive, and no new inferential test was introduced for it.
