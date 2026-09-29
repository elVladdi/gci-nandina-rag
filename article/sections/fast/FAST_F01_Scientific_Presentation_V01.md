# FAST-F01 Scientific Presentation V01

## Figure 1

Figure 1. Decision-support architecture and authority boundaries. Historical retrieval determines candidate membership and order, the Top-3 is fixed before downstream processing, documentary evidence is associated without reranking, and the local LLM explains only the received candidates and context. The diagnostic reranker is shown only as a separate lateral analysis with no feedback to the primary ranking.

Figura 1. Arquitectura de apoyo a la decisión y fronteras de autoridad. La recuperación histórica determina la composición y el orden de los candidatos, el Top-3 se fija antes del procesamiento posterior, la evidencia documental se asocia sin reordenar y el LLM local explica únicamente los candidatos y el contexto recibidos. El reranker diagnóstico se muestra solo como un análisis lateral separado, sin retroalimentación al ranking primario.

## Table 1

| Component / split | Role | Size / count | Unit / grouping | Scope / use |
| --- | --- | --- | --- | --- |
| Curated v0.2 benchmark | Union assigned to historical, development and evaluation partitions | 4,106 curated SERIE records | SERIE analysis unit; DAM grouping when dependence is relevant | Offline Chapter-87/NANDINA-8 benchmark; not an operational deployment |
| H100 historical bank | Historical candidate source | 2,950 series; 28 DAM; 66 represented codes | Complete DAM assignment; historical records link descriptions to codes | Determines primary candidate ranking and fixed Top-3 |
| Development set | Development partition | 100 series; 6 DAM; 9 represented codes | Complete DAM assignment | Not the primary evaluation set |
| EVAL set | Primary evaluation partition | 1,056 series; 67 DAM; 42 represented reference codes | SERIE metrics with DAM-cluster inference where relevant | Common benchmark for candidate retrieval and downstream evaluations |
| Decision-885-derived documentary corpus | Candidate-specific documentary evidence resource | Valid eight-digit NANDINA entries with hierarchical context and provenance | Candidate-linked evidence records | Evidence association only; no candidate insertion, substitution, or reranking |

## Table 2

| Comparator | Metric | Historical | Comparator | Historical - comparator | 99% CI for paired difference | EVAL_N | DAM_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flat normative BM25 | Top-1 | 0.509469696969697 | 0.027462121212121212 | 0.48200757575757575 | [0.3294468432754924, 0.6313318202387002] | 1056 | 67 |
| Flat normative BM25 | Top-3 | 0.6714015151515151 | 0.05113636363636364 | 0.6202651515151515 | [0.4897739082938048, 0.7575059408229955] | 1056 | 67 |
| Flat normative BM25 | Top-5 | 0.7632575757575758 | 0.061553030303030304 | 0.7017045454545454 | [0.5826075839920948, 0.8179633837631779] | 1056 | 67 |
| Flat normative BM25 | Top-10 | 0.8910984848484849 | 0.06534090909090909 | 0.8257575757575758 | [0.7371599425592884, 0.8960511280511279] | 1056 | 67 |
| Flat normative BM25 | MRR@100 | 0.6297077493524843 | 0.04229731726741296 | 0.5874104320850713 | [0.4636263128057276, 0.7120413939150084] | 1056 | 67 |
| Hierarchical normative BM25 | Top-1 | 0.509469696969697 | 0.026515151515151516 | 0.48295454545454547 | [0.3304194457866509, 0.6308222377115758] | 1056 | 67 |
| Hierarchical normative BM25 | Top-3 | 0.6714015151515151 | 0.052083333333333336 | 0.6193181818181818 | [0.48549190547352417, 0.7570283570093408] | 1056 | 67 |
| Hierarchical normative BM25 | Top-5 | 0.7632575757575758 | 0.0625 | 0.7007575757575758 | [0.582403679370273, 0.8170633881854532] | 1056 | 67 |
| Hierarchical normative BM25 | Top-10 | 0.8910984848484849 | 0.06534090909090909 | 0.8257575757575758 | [0.7366134318353867, 0.8949021633933183] | 1056 | 67 |
| Hierarchical normative BM25 | MRR@100 | 0.6297077493524843 | 0.041971783226435376 | 0.5877359661260488 | [0.46519960807980876, 0.7120385347859284] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | Top-1 | 0.509469696969697 | 0.000946969696969697 | 0.5085227272727273 | [0.36470230112770496, 0.6534661440827626] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | Top-3 | 0.6714015151515151 | 0.010416666666666666 | 0.6609848484848485 | [0.5413054932182491, 0.7816098181559374] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | Top-5 | 0.7632575757575758 | 0.05113636363636364 | 0.7121212121212122 | [0.590534358995813, 0.832721912225224] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | Top-10 | 0.8910984848484849 | 0.17803030303030304 | 0.7130681818181818 | [0.5495481330386991, 0.8607334430830679] | 1056 | 67 |
| D1a Text2Trade-inspired MNRL | MRR@100 | 0.6297077493524843 | 0.038087139731859634 | 0.5916206096206248 | [0.48731077928400757, 0.7060899067492691] | 1056 | 67 |

## Table 3

| Contrast | Recall@100 | Recall@200 | Paired difference | 95% CI | Pool@200 context | EVAL_N | DAM_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchical Recall@200 - Recall@100 | 0.10132575757575757 | 0.3039772727272727 | 0.20265151515151514 | [0.06676310583580614, 0.34160130792395144] | 0.3039772727272727 | 1056 | 67 |

## Figure 2 caption

Figure 2. Primary HE2 evidence in the Chapter 87 offline internal benchmark (1,056 series, 67 DAM, and 42 NANDINA codes). (A) Observed values for Historical and the three corrected Attempt06 comparators for Top-1, Top-3, Top-5, Top-10, and MRR@100; these arm-level values are descriptive and have no authorized arm-level CI. (B) Fifteen paired Historical-minus-comparator differences for the five primary metrics and three comparators, with frozen 99% CIs for each paired difference. (C) The single primary HE2_B corrected-hierarchical contrast, Recall@200 minus Recall@100, with a frozen 95% CI; Recall@100 and Recall@200 are shown only as context and Pool@200 is not duplicated as confirmatory evidence. The contrasts are noncausal, quantify uncertainty within the fixed benchmark, and do not represent overall framework accuracy or external validity.

Figura 2. Evidencia primaria de HE2 en el benchmark interno offline del Capítulo 87 (1.056 series, 67 DAM y 42 códigos NANDINA). (A) Valores observados de Historical y de los tres comparadores corregidos Attempt06 en Top-1, Top-3, Top-5, Top-10 y MRR@100; estos valores por brazo son descriptivos y no tienen CI por brazo autorizado. (B) Quince diferencias pareadas Historical menos comparador para las cinco métricas primarias y los tres comparadores, con CI congelados de 99% para cada diferencia pareada. (C) Único contraste primario HE2_B del retrieval jerárquico corregido, Recall@200 menos Recall@100, con CI congelado de 95%; Recall@100 y Recall@200 se muestran únicamente como contexto y Pool@200 no se duplica como evidencia confirmatoria. Los contrastes son no causales, cuantifican incertidumbre dentro del benchmark fijo y no representan exactitud global del framework ni validez externa.
