# FAST-F01 Scientific Presentation V02

## Figure 1

Figure 1. Decision-support architecture and authority boundaries. Historical retrieval determines candidate membership and order, the Top-3 is fixed before downstream processing, documentary evidence is associated without reranking, and the local LLM explains only the received candidates and context.

Figura 1. Arquitectura de apoyo a la decisión y fronteras de autoridad. La recuperación histórica determina la composición y el orden de los candidatos, el Top-3 se fija antes del procesamiento posterior, la evidencia documental se asocia sin reordenar y el LLM local explica únicamente los candidatos y el contexto recibidos.

## Table 1

| Component / split | Role | Size / count | Unit / grouping | Scope / use |
| --- | --- | --- | --- | --- |
| Curated v0.2 benchmark | Union assigned to historical, development and evaluation partitions | 4,106 curated SERIE records | SERIE analysis unit; DAM grouping when dependence is relevant | Offline Chapter-87/NANDINA-8 benchmark; not an operational deployment |
| H100 historical bank | Historical candidate source | 2,950 series; 28 DAM; 66 represented codes | Complete DAM assignment; historical records link descriptions to codes | Determines primary candidate ranking and fixed Top-3 |
| Development set | Development partition | 100 series; 6 DAM; 9 represented codes | Complete DAM assignment | Not the primary evaluation set |
| EVAL set | Primary evaluation partition | 1,056 series; 67 DAM; 42 represented reference codes | SERIE metrics with DAM-cluster inference where relevant | Common benchmark for candidate retrieval and downstream evaluations |
| Decision-885-derived documentary corpus | Candidate-specific documentary evidence resource | Valid eight-digit NANDINA entries with hierarchical context and provenance | Candidate-linked evidence records | Evidence association only; no candidate insertion, substitution, or reranking |

## Table 2

**Table 2. Primary HE2_A early-ranking contrasts.** The confidence interval belongs to the paired Historical-minus-comparator difference; arm-level values have no arm-level CI and no p-values are reported.

| Comparator | Metric | Historical | Comparator | Historical - comparator | 99% CI for paired difference | EVAL_N | DAM_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flat normative BM25 | Top-1 | 0.5095 | 0.0275 | 0.4820 | [0.3294, 0.6313] | 1056 | 67 |
| Flat normative BM25 | Top-3 | 0.6714 | 0.0511 | 0.6203 | [0.4898, 0.7575] | 1056 | 67 |
| Flat normative BM25 | Top-5 | 0.7633 | 0.0616 | 0.7017 | [0.5826, 0.8180] | 1056 | 67 |
| Flat normative BM25 | Top-10 | 0.8911 | 0.0653 | 0.8258 | [0.7372, 0.8961] | 1056 | 67 |
| Flat normative BM25 | MRR@100 | 0.6297 | 0.0423 | 0.5874 | [0.4636, 0.7120] | 1056 | 67 |
| Hierarchical normative BM25 | Top-1 | 0.5095 | 0.0265 | 0.4830 | [0.3304, 0.6308] | 1056 | 67 |
| Hierarchical normative BM25 | Top-3 | 0.6714 | 0.0521 | 0.6193 | [0.4855, 0.7570] | 1056 | 67 |
| Hierarchical normative BM25 | Top-5 | 0.7633 | 0.0625 | 0.7008 | [0.5824, 0.8171] | 1056 | 67 |
| Hierarchical normative BM25 | Top-10 | 0.8911 | 0.0653 | 0.8258 | [0.7366, 0.8949] | 1056 | 67 |
| Hierarchical normative BM25 | MRR@100 | 0.6297 | 0.0420 | 0.5877 | [0.4652, 0.7120] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | Top-1 | 0.5095 | 0.0009 | 0.5085 | [0.3647, 0.6535] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | Top-3 | 0.6714 | 0.0104 | 0.6610 | [0.5413, 0.7816] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | Top-5 | 0.7633 | 0.0511 | 0.7121 | [0.5905, 0.8327] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | Top-10 | 0.8911 | 0.1780 | 0.7131 | [0.5495, 0.8607] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | MRR@100 | 0.6297 | 0.0381 | 0.5916 | [0.4873, 0.7061] | 1056 | 67 |

## Table 3

**Table 3. HE2_B deep-coverage contrast.** Pool@200 is included as context only and is not duplicated as a second confirmatory interpretation.

| Contrast | Recall@100 | Recall@200 | Paired difference | 95% CI | Pool@200 context | EVAL_N | DAM_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchical Recall@200 - Recall@100 | 0.1013 | 0.3040 | 0.2027 | [0.0668, 0.3416] | 0.3040 | 1056 | 67 |

## Figure 2 caption

Figure 2. Primary HE2 evidence in the Chapter 87 offline internal benchmark (1,056 series, 67 DAM, and 42 NANDINA codes). (A) Observed values for Historical and the three corrected Attempt06 comparators for Top-1, Top-3, Top-5, Top-10, and MRR@100; these arm-level values are descriptive and have no authorized arm-level CI. (B) Fifteen paired Historical-minus-comparator differences for the five primary metrics and three comparators, with frozen 99% CIs for each paired difference. (C) The single primary HE2_B corrected-hierarchical contrast, Recall@200 minus Recall@100, with a frozen 95% CI; Recall@100 and Recall@200 are shown only as context and Pool@200 is not duplicated as confirmatory evidence. The contrasts are noncausal, quantify uncertainty within the fixed benchmark, and do not represent overall framework accuracy or external validity.

Figura 2. Evidencia primaria de HE2 en el benchmark interno offline del Capítulo 87 (1.056 series, 67 DAM y 42 códigos NANDINA). (A) Valores observados de Historical y de los tres comparadores corregidos Attempt06 en Top-1, Top-3, Top-5, Top-10 y MRR@100; estos valores por brazo son descriptivos y no tienen CI por brazo autorizado. (B) Quince diferencias pareadas Historical menos comparador para las cinco métricas primarias y los tres comparadores, con CI congelados de 99% para cada diferencia pareada. (C) Único contraste primario HE2_B del retrieval jerárquico corregido, Recall@200 menos Recall@100, con CI congelado de 95%; Recall@100 y Recall@200 se muestran únicamente como contexto y Pool@200 no se duplica como evidencia confirmatoria. Los contrastes son no causales, cuantifican incertidumbre dentro del benchmark fijo y no representan exactitud global del framework ni validez externa.

## Spanish mirror Tables 2–3

**Tabla 2. Contrastes primarios HE2_A de ranking temprano.** El intervalo de confianza corresponde a la diferencia pareada Historical menos comparador; los valores por brazo no tienen CI por brazo y no se reportan p-values.

| Comparador | Métrica | Histórico | Comparador | Histórico - comparador | IC del 99% para la diferencia pareada | EVAL_N | DAM_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BM25 normativo flat | Top-1 | 0.5095 | 0.0275 | 0.4820 | [0.3294, 0.6313] | 1056 | 67 |
| BM25 normativo flat | Top-3 | 0.6714 | 0.0511 | 0.6203 | [0.4898, 0.7575] | 1056 | 67 |
| BM25 normativo flat | Top-5 | 0.7633 | 0.0616 | 0.7017 | [0.5826, 0.8180] | 1056 | 67 |
| BM25 normativo flat | Top-10 | 0.8911 | 0.0653 | 0.8258 | [0.7372, 0.8961] | 1056 | 67 |
| BM25 normativo flat | MRR@100 | 0.6297 | 0.0423 | 0.5874 | [0.4636, 0.7120] | 1056 | 67 |
| BM25 normativo jerárquico | Top-1 | 0.5095 | 0.0265 | 0.4830 | [0.3304, 0.6308] | 1056 | 67 |
| BM25 normativo jerárquico | Top-3 | 0.6714 | 0.0521 | 0.6193 | [0.4855, 0.7570] | 1056 | 67 |
| BM25 normativo jerárquico | Top-5 | 0.7633 | 0.0625 | 0.7008 | [0.5824, 0.8171] | 1056 | 67 |
| BM25 normativo jerárquico | Top-10 | 0.8911 | 0.0653 | 0.8258 | [0.7366, 0.8949] | 1056 | 67 |
| BM25 normativo jerárquico | MRR@100 | 0.6297 | 0.0420 | 0.5877 | [0.4652, 0.7120] | 1056 | 67 |
| MNRL D1a inspirado en Text2Trade | Top-1 | 0.5095 | 0.0009 | 0.5085 | [0.3647, 0.6535] | 1056 | 67 |
| MNRL D1a inspirado en Text2Trade | Top-3 | 0.6714 | 0.0104 | 0.6610 | [0.5413, 0.7816] | 1056 | 67 |
| MNRL D1a inspirado en Text2Trade | Top-5 | 0.7633 | 0.0511 | 0.7121 | [0.5905, 0.8327] | 1056 | 67 |
| MNRL D1a inspirado en Text2Trade | Top-10 | 0.8911 | 0.1780 | 0.7131 | [0.5495, 0.8607] | 1056 | 67 |
| MNRL D1a inspirado en Text2Trade | MRR@100 | 0.6297 | 0.0381 | 0.5916 | [0.4873, 0.7061] | 1056 | 67 |

**Tabla 3. Contraste HE2_B de cobertura profunda.** Pool@200 se incluye solo como contexto y no se duplica como segunda interpretación confirmatoria.

| Contraste | Recall@100 | Recall@200 | Diferencia pareada | IC del 95% | Contexto Pool@200 | EVAL_N | DAM_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Recall jerárquico@200 - Recall@100 | 0.1013 | 0.3040 | 0.2027 | [0.0668, 0.3416] | 0.3040 | 1056 | 67 |
