# Evaluacion recuperacion jerarquica BM25 devset v0.1

## Alcance

La Fase 8A evalua si conviene pasar de recuperacion directa NANDINA8 a una recuperacion jerarquica por familias arancelarias `HS2/HS4/HS6 -> NANDINA8` para elevar el techo de candidatos del futuro flujo LLM+RAG.

El cuello de botella observado en fases previas era un `Recall@100` bajo del pool de candidatos. La hipotesis de esta fase fue que restringir la busqueda NANDINA8 a familias arancelarias recuperadas previamente podia mejorar cobertura amplia frente a buscar directamente en NANDINA8.

Esta fase no uso LLM, Ollama, OpenAI, Text2Trade, requests, HTTP ni APIs remotas. El evalset no se uso para seleccionar estrategia; solo se genero un diagnostico de techo, separado de la decision devset.

## Artefactos

Scripts versionables:

- `src/analysis/diagnose_hierarchical_retrieval_ceiling.py`
- `src/corpus/build_hierarchical_level_corpora.py`
- `src/experiments/build_bm25_level_indexes.py`
- `src/experiments/evaluate_hierarchical_bm25_devset.py`

Artefactos regenerables e ignorados:

- `data/processed/corpus_levels/`
- `data/processed/indexes/bm25_levels/`
- `outputs/analysis/hierarchical_retrieval_ceiling_v0.1/`
- `outputs/evaluation/hierarchical_bm25_devset_v0.1/`

## Diagnostico de techo

| Dataset | Metodo | NANDINA8@100 | HS6@100 | HS4@100 | HS2@100 |
|---|---|---:|---:|---:|---:|
| devset | BM25_hierarchical_v0.1 | 0.6923 | 0.6923 | 0.9231 | 0.9231 |
| devset | phase7a_pool_hierarchical_80_dual_backfill_20 | 0.7692 | 0.7692 | 0.9231 | 0.9231 |
| evalset | BM25_hierarchical_v0.1 | 0.2500 | 0.2550 | 0.2850 | 0.4983 |
| evalset | phase7a_pool_hierarchical_80_dual_backfill_20 | 0.2667 | 0.2717 | 0.2983 | 0.5283 |

La brecha entre `HS2@100` y `NANDINA8@100` muestra que hay cobertura familiar parcial: muchos casos llegan al capitulo correcto, pero no a la subpartida exacta dentro del Top-100. Esta brecha justifica investigar recuperacion jerarquica, pero no garantiza que filtrar por familias mejore el ranking final.

## Resultados devset

Se probaron 102 configuraciones sobre el devset:

- `direct_nandina8`
- `hs4_then_nandina8`
- `hs6_then_nandina8`
- `hs4_hs6_union_then_nandina8`
- `hs2_hs4_hs6_union_then_nandina8`

Valores probados:

- HS2 Top-M: `3`, `5`
- HS4 Top-M: `5`, `10`, `20`
- HS6 Top-M: `10`, `20`, `50`
- NANDINA8 final: `Top-10`, `Top-50`, `Top-100`

| Estrategia | HS2 M | HS4 M | HS6 M | Final N | Top-10 | Recall@50 | Recall@100 | HS4@100 | HS2@100 | MRR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| direct_nandina8 | 0 | 0 | 0 | 100 | 0.6154 | 0.6923 | 0.6923 | 0.9231 | 0.9231 | 0.4698 |
| hs2_hs4_hs6_union_then_nandina8 | 3 | 10 | 10 | 100 | 0.5385 | 0.5385 | 0.6154 | 0.7692 | 0.7692 | 0.3918 |
| hs4_hs6_union_then_nandina8 | 0 | 10 | 10 | 100 | 0.5385 | 0.5385 | 0.6154 | 0.7692 | 0.7692 | 0.3918 |

La mejor configuracion por devset fue `direct_nandina8` con `final_top_n=50` por desempate conservador; `direct_nandina8 Top-100` conserva el mismo `Recall@100 = 0.6923` y mayor cobertura familiar a Top-100. Ninguna estrategia jerarquica probo mejora de `Recall@100` frente al directo NANDINA8 ni frente al pool Fase 7A `hierarchical_80_dual_backfill_20`, que ya tenia `final_pool@100 = 0.7692` en devset.

## Decision

No se selecciona una estrategia jerarquica HS2/HS4/HS6 para Fase 8B. El prototipo confirma que existe techo familiar, especialmente a HS2, pero el filtrado jerarquico probado reduce o empata la cobertura exacta en devset.

La recomendacion es no ejecutar evalset como validacion de estrategia jerarquica entregable en esta forma. Una eventual Fase 8B deberia redisenarse antes, por ejemplo como diagnostico de reordenamiento intra-familia o como expansion no restrictiva del pool, manteniendo la regla de seleccionar cualquier nueva estrategia solo con devset antes de tocar evalset.
