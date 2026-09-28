# Results B02 V01 — Section 5.2

```text
BLOCK = RESULTS_B02_SECTION_5_2
VERSION = V01
GOVERNING_PROMPT = article/prompts/6_RESULTS_B02_SECTION5_2.md@76045bc1e408298b3e86de11f0598500f7dfa24f
GOVERNING_DECISION = D-093
GROUND_TRUTH_DECISION = D-092
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V017.md
BASELINE_MASTER_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
BASELINE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
AUTHORIZED_SCOPE = SECTION_5_2_ONLY
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Part I — English manuscript text

## 5.2. Candidate retrieval performance

On the common 1,056-series EVAL set, historical BM25 H100 retrieved the reference eight-digit NANDINA code at Top-1 in 538 cases (50.95%), Top-3 in 709 (67.14%), Top-5 in 806 (76.33%), and Top-10 in 941 (89.11%). MRR@100 was 0.6297, and the supplementary Top-50 hit rate was 1,047/1,056 (99.15%).

On the same EVAL set, flat normative BM25 yielded Top-1/3/5/10 hit rates of 2.75%, 5.11%, 6.16%, and 6.53%, with Top-50 of 7.01% and MRR@100 of 0.0423. Hierarchical normative BM25 yielded 2.65%, 5.21%, 6.25%, and 6.53%, with Top-50 of 9.09% and MRR@100 of 0.0420. D1a Text2Trade-inspired MNRL yielded 0.09%, 1.04%, 5.11%, and 17.80%, with Top-50 of 31.34% and MRR@100 of 0.0381.

For the corrected hierarchical normative comparator, exact Recall@100 was 107/1,056 (10.13%), while exact Recall@200 was 321/1,056 (30.40%); Pool@200 was likewise 321/1,056 (30.40%). These deeper-coverage values are reported descriptively and separately from the early-ranking metrics.

Across the listed early-ranking metrics and supplementary Top-50, historical BM25 H100 had the highest observed values among the four evaluated families on this fixed EVAL set. The three non-historical methods were evaluation comparators and did not replace the historical ranking as the candidate source in the primary framework; inferential contrasts are reserved for Section 5.6.

## Part II — Spanish semantic-control mirror

## 5.2. Desempeño de recuperación de candidatos

En el conjunto EVAL común de 1.056 series, BM25 histórico H100 recuperó el código NANDINA de referencia de ocho dígitos en Top-1 para 538 casos (50,95%), Top-3 para 709 (67,14%), Top-5 para 806 (76,33%) y Top-10 para 941 (89,11%). El MRR@100 fue 0,6297 y la tasa suplementaria Top-50 fue 1.047/1.056 (99,15%).

En el mismo conjunto EVAL, BM25 normativo flat obtuvo tasas Top-1/3/5/10 de 2,75%, 5,11%, 6,16% y 6,53%, con Top-50 de 7,01% y MRR@100 de 0,0423. BM25 normativo jerárquico obtuvo 2,65%, 5,21%, 6,25% y 6,53%, con Top-50 de 9,09% y MRR@100 de 0,0420. D1a Text2Trade-inspired MNRL obtuvo 0,09%, 1,04%, 5,11% y 17,80%, con Top-50 de 31,34% y MRR@100 de 0,0381.

Para el comparador normativo jerárquico corregido, Exact Recall@100 fue 107/1.056 (10,13%), mientras que Exact Recall@200 fue 321/1.056 (30,40%); Pool@200 fue igualmente 321/1.056 (30,40%). Estos valores de cobertura a mayor profundidad se reportan de forma descriptiva y separada de las métricas de early ranking.

En las métricas de early ranking listadas y el Top-50 suplementario, BM25 histórico H100 presentó los mayores valores observados entre las cuatro familias evaluadas en este conjunto EVAL fijo. Los tres métodos no históricos fueron comparadores de evaluación y no sustituyeron al ranking histórico como fuente de candidatos del framework primario; los contrastes inferenciales se reservan para la Section 5.6.
