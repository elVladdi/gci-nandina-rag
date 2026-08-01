# Evaluacion BM25 jerarquico/dual data_aduanas clase 87 v0.1

## Objetivo

Reevaluar, de forma acotada, las variantes normativas previamente definidas en Fase 6B/6C sobre el nuevo evalset `data_aduanas` Clase = 87. Esta corrida no rehace la busqueda de variantes ni ajusta reglas mirando el evalset.

## Por que no se rehace toda Fase 6B/6C

Fase 6B/6C historica conserva su rol exploratorio sobre devset/evalset anterior. En esta actualizacion solo se valida si los recuperadores normativos ya congelados siguen aportando como trazabilidad o respaldo sobre descripciones comerciales clase 87.

## Variantes evaluadas

- `BM25_flat_current`: data/processed/indexes/bm25_nandina8.pkl.
- `BM25_hierarchical_v0.1`: data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl.
- `BM25_dual_protected_top_5_backfill`: data/processed/indexes/bm25_ablation_nandina_v0.1/C_hs6_leaf.pkl + data/processed/indexes/bm25_ablation_nandina_v0.1/D_4d_hs6_leaf.pkl.
- Variantes no evaluadas: A/B/E/F/G no se reejecutan porque esta actualizacion solo valida variantes normativas previamente utiles.

## Evalset

- Archivo: `data/processed/data_aduanas_evalset_clase87_v0.1.csv`.
- Filas evaluadas por metodo: 1006.
- Columna de consulta: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta esperada: `NANDINA`.

## Metricas

| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | Partida@10 | Partida@50 | Partida@100 | Sub Partida@10 | Sub Partida@50 | Sub Partida@100 | Clase@10 | Clase@50 | Clase@100 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| BM25_flat_current | 0.0229 | 0.0338 | 0.0398 | 0.0467 | 0.0312 | 0.0616 | 0.0626 | 0.0755 | 0.1183 | 0.1252 | 0.0537 | 0.0716 | 0.0755 | 0.6829 | 0.8797 | 0.8887 |
| BM25_hierarchical_v0.1 | 0.0249 | 0.0398 | 0.0487 | 0.0497 | 0.0385 | 0.0626 | 0.3449 | 0.0755 | 0.4751 | 0.5865 | 0.0537 | 0.0716 | 0.5209 | 0.1849 | 0.6799 | 0.7386 |
| BM25_dual_protected_top_5_backfill | 0.0239 | 0.0368 | 0.0437 | 0.0487 | 0.0340 | 0.0716 | 0.1948 | 0.0795 | 0.1262 | 0.5905 | 0.0537 | 0.0795 | 0.3708 | 0.1779 | 0.6998 | 0.7753 |

## Comparacion con BM25 plano Fase 4 actualizada

La referencia Fase 4 clase 87 reporto Top-10 = 0.0467, MRR = 0.0312, Recall@100 = 0.0626, Partida@100 = 0.1252, Sub Partida@100 = 0.0755 y Clase@100 = 0.8887. La corrida actual recalcula `BM25_flat_current` con el mismo evalset e indice plano para dejar una comparacion por metodo en el mismo archivo.

## Lectura metodologica

La familia normativa mantiene alta senal de Clase@100, pero sigue lejos de resolver exactitud NANDINA8 sobre descripciones comerciales clase 87. La comparacion confirma que estas variantes son utiles como trazabilidad y respaldo, no como recuperador principal cuando exista evidencia historica.

## Decision

`BM25_hierarchical_v0.1` se conserva como recuperador normativo auxiliar de trazabilidad. `BM25_dual_protected_top_5_backfill` se conserva solo como fuente auxiliar de cobertura profunda. No se promueven como ranking principal para clase 87.

## Advertencia de comparabilidad

Estas metricas no sustituyen ni corrigen las cifras historicas de Fase 6B/6C: cambian fuente, distribucion y alcance del evalset. La comparacion valida solo el uso auxiliar de variantes normativas sobre `data_aduanas` clase 87.

## Controles

- No se ejecuto LLM.
- No se ejecuto Ollama.
- No se ejecuto Text2Trade.
- No se usaron APIs remotas.
- No se modificaron evalset historico, devset historico ni splits clase 87.
