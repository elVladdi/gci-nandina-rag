# Evaluacion BM25 dual backfill devset v0.1

## Objetivo

Evaluar una recuperacion dual defensiva para NANDINA: un indice de precision HS6+NANDINA8 como ranking base y un indice de recall 4D+HS6+NANDINA8 usado como backfill controlado. Esta fase usa solo devset; no se ejecuto evalset, LLM ni Text2Trade.

## Motivacion

La ablation 6B-2 mostro que `C_hs6_leaf` mejora Top-1/MRR y protege precision, mientras que las variantes con 4D mejoran recall pero degradan algunos casos. La fusion dual separa esas funciones para que el indice amplio agregue candidatos sin desplazar agresivamente el ranking de precision.

## Indices usados

- Precision: `C_hs6_leaf`, campo `texto_index_variant`, corpus de HS6 + NANDINA8.
- Recall: `D_4d_hs6_leaf`, campo `texto_index_variant`, corpus de 4D + HS6 + NANDINA8.
- Referencias: BM25 plano actual y BM25 jerarquico v0.1.

## Estrategias

- `precision_then_backfill_k10`: conserva Top-10 de precision y agrega candidatos nuevos de recall despues.
- `protected_top_5_backfill`: protege Top-5 de precision, luego permite backfill amplio.
- `protected_top_10_backfill`: protege Top-10 de precision, luego permite backfill amplio.
- `oracle_backfill_if_precision_misses_top10`: diagnostico con etiqueta esperada; aplica backfill si la respuesta no aparece en Top-10 de precision.
- `oracle_backfill_if_precision_misses_top50`: diagnostico con etiqueta esperada; aplica backfill si la respuesta no aparece en Top-50 de precision.

## Metricas comparativas

| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4 | HS2 | NF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25_flat_current | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4370 | 0.6154 | 0.6154 | 0.8462 | 0.8462 | 5 |
| C_hs6_leaf | 0.4615 | 0.4615 | 0.4615 | 0.5385 | 0.4754 | 0.6154 | 0.6154 | 0.7692 | 0.7692 | 5 |
| BM25_hierarchical_v0.1 | 0.3846 | 0.5385 | 0.6154 | 0.6154 | 0.4701 | 0.6923 | 0.6923 | 0.7692 | 0.7692 | 4 |
| precision_then_backfill_k10 | 0.4615 | 0.4615 | 0.4615 | 0.5385 | 0.4855 | 0.6923 | 0.7692 | 0.7692 | 0.7692 | 3 |
| protected_top_5_backfill | 0.4615 | 0.4615 | 0.4615 | 0.6923 | 0.4991 | 0.6923 | 0.7692 | 0.9231 | 0.9231 | 3 |
| protected_top_10_backfill | 0.4615 | 0.4615 | 0.4615 | 0.5385 | 0.4855 | 0.6923 | 0.7692 | 0.7692 | 0.7692 | 3 |
| oracle_backfill_if_precision_misses_top10 | 0.4615 | 0.4615 | 0.4615 | 0.5385 | 0.4855 | 0.6923 | 0.7692 | 0.7692 | 0.7692 | 3 |
| oracle_backfill_if_precision_misses_top50 | 0.4615 | 0.4615 | 0.4615 | 0.5385 | 0.4833 | 0.6923 | 0.7692 | 0.7692 | 0.7692 | 3 |

## Casos criticos

| Codigo | Fuente | BM25_flat_current | C_hs6_leaf | BM25_hierarchical_v0.1 | precision_then_backfill_k10 | protected_top_5_backfill | protected_top_10_backfill | oracle_backfill_if_precision_misses_top10 | oracle_backfill_if_precision_misses_top50 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 39012000 | devset | 1 | 1 | 36 | 1 | 1 | 1 | 1 | 1 |
| 02013000 | devset | 8 | 8 | 1 | 8 | 6 | 8 | 8 | 8 |
| 85414100 | devset | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 |
| 95030010 | devset | 18 | 18 | 3 | 12 | 7 | 12 | 12 | 18 |
| 28151100 | devset | 0 | 0 | 4 | 11 | 6 | 11 | 11 | 11 |
| 83022000 | smoke | 1 | 1 | 5 | 1 | 1 | 1 | 1 | 1 |

## Smoke tests

- `soda caustica solida` espera 28151100; ver `dual_backfill_smoke_tests.json` para ranks y Top-10 por metodo.
- `ruedas` espera 83022000; ver `dual_backfill_smoke_tests.json` para ranks y Top-10 por metodo.

## Decision metodologica

Estrategia mejor clasificada: `protected_top_5_backfill`.
Clasificacion: B. Candidato exploratorio.
`protected_top_5_backfill` es candidato exploratorio: mejora recall o balance, pero conserva degradaciones menores; conviene iterar antes de evalset.

## Alcance

Esta fase solo usa devset. No se leyo ni ejecuto el evalset final. Tampoco se ejecuto LLM, Text2Trade ni Excel fuente.
