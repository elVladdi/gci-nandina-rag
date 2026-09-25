# G6-F03 — Caption Registry v0.1

status: APPROVED
main_source_commit: 3390878a62ce32ba0e6f4fce69a394c903f5ff11
figure_count: 3
caption_count: 3

## G6-FIG-01

figure_id: G6-FIG-01
working_title: Evidencia primaria de HE2: ranking temprano y cobertura profunda
scientific_role: PRIMARY_INFERENTIAL
destination: MAIN

final_caption: **Evidencia primaria de HE2 en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** (A) Valores observados de Historical y de los tres comparadores corregidos Attempt06 en Top-1, Top-3, Top-5, Top-10 y MRR@100; estos valores por brazo son descriptivos y no tienen CI por brazo autorizado. (B) Quince diferencias pareadas `Historical − comparator` correspondientes a las cinco métricas primarias y los tres comparadores, con CI congelados de 99% sobre cada diferencia pareada. (C) Único contraste primario HE2_B del retrieval jerárquico corregido, `Recall@200 − Recall@100`, con CI congelado de 95%; Recall@100 y Recall@200 se muestran únicamente como contexto y Pool@200 no se duplica como evidencia confirmatoria. Los contrastes son no causales, cuantifican incertidumbre dentro del benchmark fijo y no representan exactitud global del framework RAG ni validez externa.

population_and_denominator: 1,056 series / 67 DAM / 42 NANDINA; benchmark interno offline, Capítulo 87.
metric_or_evidence_family: HE2_A primary early-ranking metrics (Top-1, Top-3, Top-5, Top-10, MRR@100) + HE2_B corrected hierarchical deep-coverage contrast.
uncertainty_statement: Panel A has no authorized arm-level CI; Panel B uses frozen 99% CI only on the 15 paired Historical-minus-comparator differences; Panel C uses one frozen 95% CI on Recall@200-minus-Recall@100; no p-values.
scope_limitation: Noncausal contrasts and cluster-resampling uncertainty inside the fixed internal benchmark; no external validation.
forbidden_interpretation: Do not infer global RAG accuracy, causal superiority, arm-level uncertainty, external-population validity, or duplicate Pool@200 as confirmatory evidence.
source_table_paths:
  - outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
  - outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
figure_svg_path: figures/group6/g6_fig_01_he2.svg
figure_png_path: figures/group6/g6_fig_01_he2.png
accessibility_checks:
  - all nonempty text >= 8 pt effective at native vector/raster size
  - axis/tick text approximately 9 pt effective
  - redundant circle/square/triangle/diamond encoding
  - visible zero references in contrast panels
  - no material clipping or label overlap detected
  - no internal workflow ID displayed as publication title
status: APPROVED

## G6-FIG-02

figure_id: G6-FIG-02
working_title: Cobertura exacta NANDINA de Phase E según profundidad y variante
scientific_role: DESCRIPTIVE_SUPPLEMENTARY
destination: SECONDARY

final_caption: **Cobertura exacta NANDINA de Phase E según profundidad y variante en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** Se muestran 15 proporciones descriptivas de cobertura exacta NANDINA: cinco variantes en cada profundidad de recuperación 50, 100 y 200. `hierarchical_only`, `dual_only`, `hierarchical_first_100` y `hierarchical_80_dual_backfill_20` son las cuatro variantes formales `A_historical_defined` asociadas al claim descriptivo G3C-005; `hierarchical_70_dual_backfill_30` se incluye únicamente como contexto descriptivo adicional y no fue seleccionada por favorabilidad ni constituye evidencia confirmatoria. No se presentan CI, p-values, tendencias ajustadas ni contrastes inferenciales. `diagnostic_union_hierarchical_dual` se excluye del rendimiento ordinario porque representa un techo diagnóstico. La figura no modifica la evidencia confirmatoria ni la disposición de HE2.

population_and_denominator: 1,056 series / 67 DAM / 42 NANDINA; benchmark interno offline, Capítulo 87.
metric_or_evidence_family: Phase E exact-NANDINA descriptive coverage at depths 50, 100 and 200.
uncertainty_statement: DESCRIPTIVE_NO_CI_AUTHORIZED; no p-values or inferential contrasts.
scope_limitation: Four formal A_historical_defined variants plus hierarchical_70_dual_backfill_30 as context only; diagnostic union excluded from ordinary performance.
forbidden_interpretation: Do not promote Phase E to confirmatory evidence, infer significance between variants, rank variants by favorability, or use the diagnostic union as ordinary performance.
source_table_paths:
  - outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
figure_svg_path: figures/group6/g6_fig_02_phase_e.svg
figure_png_path: figures/group6/g6_fig_02_phase_e.png
accessibility_checks:
  - both axis titles >= 10 pt effective
  - ticks and nominal legend entries >= 9 pt effective
  - five distinct marker shapes; color not sole required encoding
  - 70/30 contextual variant retains equal visual weight
  - y-axis baseline at zero and range [0,0.35]
  - no material clipping or label overlap detected
  - no internal workflow ID displayed as publication title
status: APPROVED

## G6-FIG-03

figure_id: G6-FIG-03
working_title: Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A)
scientific_role: DESCRIPTIVE_SENSITIVITY / NONCAUSAL
destination: APPENDIX

final_caption: **Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A) en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** Los seis paneles muestran Top1, Top3, Top5, Top10, Top50 y MRR para 31 corridas observadas distribuidas como H25 (`n=10`), H50-D1 (`n=5`), H50-D2 (`n=5`), H75 (`n=10`) y la referencia congelada H100 (`n=1`). D1 y D2 son composiciones diferenciadas dentro de H50; H25, H75 y H100 conservan asimismo sus composiciones observadas. Cada punto representa una corrida individual y H100 se muestra como una única referencia, no como una distribución de réplicas. EXP11A es una sensibilidad descriptiva y no causal en la que tamaño y composición varían conjuntamente; por ello, las diferencias entre condiciones no identifican un efecto causal aislado ni monotónico del tamaño. No se muestran CI, p-values, regresiones, suavizados ni summaries congelados como marks de la figura.

population_and_denominator: EVAL fijo de 1,056 series / 67 DAM / 42 NANDINA; 31 bancos/corridas observados con inventario 10/5/5/10/1 por condición.
metric_or_evidence_family: EXP11A joint size-composition sensitivity; Top1, Top3, Top5, Top10, Top50 and MRR.
uncertainty_statement: DESCRIPTIVE_NO_CI_AUTHORIZED; no p-values, regressions, smoothing or summary marks.
scope_limitation: Bank size and natural composition vary jointly; H100 is one frozen reference; H50-D1 and H50-D2 are distinct observed compositions.
forbidden_interpretation: Do not infer an isolated or monotonic causal size effect, treat H100 n=1 as a replicate distribution, or convert frozen condition summaries into uncertainty intervals.
source_table_paths:
  - outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
  - outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv
  - outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv
figure_svg_path: figures/group6/g6_fig_03_exp11a.svg
figure_png_path: figures/group6/g6_fig_03_exp11a.png
accessibility_checks:
  - minimum effective font >= 8.5 pt
  - all six panel titles = 9.6 pt effective
  - category labels horizontal in frozen non-favorability order
  - deterministic horizontal jitter only; no vertical jitter
  - individual observations remain discernible
  - H100 additionally encoded by solid diamond
  - no material clipping or label overlap detected
  - no internal workflow ID displayed as publication title
status: APPROVED
