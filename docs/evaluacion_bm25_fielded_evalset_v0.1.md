# Evaluacion BM25 fielded evalset v0.1

## Alcance

Esta fase valida en el evalset final la variante congelada `BM25_fielded_weighted_expanded_v0.1`, seleccionada previamente usando solo devset en Fase 7A-3. El diccionario `src/corpus/controlled_lexical_expansions_v0.1.json` y los pesos del corpus fielded quedaron congelados antes de mirar el evalset.

El evalset se ejecuto una sola vez en esta fase. Cualquier mejora o caida se interpreta como validacion externa preliminar, no como ajuste posterior.

## Controles

- La expansion controlada se aplica al corpus, no a la consulta.
- La expansion controlada no usa codigos como terminos buscables.
- No se uso LLM, Text2Trade, Ollama, OpenAI ni APIs remotas.
- No se modifico devset, evalset ni Excel fuente.
- El pool Fase 7A se reporta separado como pool auxiliar, no como ranking BM25 puro.

## Metricas comparativas

| Metodo | Tipo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4@10 | HS2@10 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25_flat_current | ranking BM25 | 0.0050 | 0.0433 | 0.0483 | 0.0517 | 0.0290 | 0.1450 | 0.1633 | 0.1933 | 0.3800 |
| BM25_hierarchical_v0.1 | ranking BM25 | 0.0283 | 0.0583 | 0.0883 | 0.1067 | 0.0524 | 0.2033 | 0.2500 | 0.1533 | 0.2433 |
| BM25_fielded_weighted_v0.1 | ranking BM25 | 0.0283 | 0.0350 | 0.0400 | 0.0683 | 0.0416 | 0.1750 | 0.2617 | 0.1783 | 0.2783 |
| BM25_fielded_weighted_expanded_v0.1 | ranking BM25 | 0.0283 | 0.0350 | 0.0400 | 0.0683 | 0.0416 | 0.1750 | 0.2617 | 0.1967 | 0.3000 |
| phase7a_pool_hierarchical_80_dual_backfill_20 | pool auxiliar | 0.0283 | 0.0583 | 0.0883 | 0.1067 | 0.0526 | 0.2033 | 0.2667 | 0.1533 | 0.2433 |

## Comparacion contra BM25_hierarchical_v0.1

| Metodo | Ganados | Perdidos | Sin cambio | Nuevos recuperados | Perdidos exactos | Casos peor rank |
|---|---:|---:|---:|---:|---:|---:|
| BM25_flat_current | 35 | 128 | 437 | 18 | 70 | 128 |
| BM25_fielded_weighted_v0.1 | 49 | 89 | 462 | 13 | 6 | 89 |
| BM25_fielded_weighted_expanded_v0.1 | 49 | 89 | 462 | 13 | 6 | 89 |
| phase7a_pool_hierarchical_80_dual_backfill_20 | 15 | 3 | 582 | 13 | 3 | 3 |

## Interpretacion

`BM25_fielded_weighted_expanded_v0.1` no mejora el ranking temprano frente a `BM25_hierarchical_v0.1`: Top-10 cae de 0.1067 a 0.0683 y MRR cae de 0.0524 a 0.0416. Si se separa ranking de cobertura amplia, la unica mejora principal esta en Recall@100, que sube de 0.2500 a 0.2617.

La mejora observada en devset no generaliza como nuevo ranking base. En evalset, la variante expanded queda como evidencia de cobertura amplia marginal, pero con costo de ranking temprano.

## Casos criticos

La tabla completa esta en `outputs/evaluation/bm25_fielded_evalset_v0.1/fielded_evalset_critical_cases.csv`. En el Markdown se omiten descripciones crudas para no propagar problemas de codificacion del origen SUNAT.

| Grupo observado | Lectura |
|---|---|
| LED/iluminacion | Algunos casos pasan de no recuperados a ranks dentro de Top-100, pero no estabilizan Top-10. |
| Polietileno/plasticos | La expansion mejora familias HS4/HS2 en algunos registros, pero tambien atrae ruido de plasticos no equivalentes. |
| Laptop/computadora portatil | No hay evidencia suficiente para promover expanded como ranking base en evalset. |
| Soda caustica/SSD/patinete | No aparecen como casos exactos fuertes en el evalset final con el mismo patron controlado del devset. |

## Decision metodologica

`BM25_fielded_weighted_expanded_v0.1` no queda como nuevo ranking base. El ranking base debe seguir siendo `BM25_hierarchical_v0.1` por mejor Top-10 y MRR en evalset.

La variante expanded puede considerarse como experimento de cobertura o fuente auxiliar para pool, pero no como sustituto directo del ranking principal. Para pool auxiliar, el baseline mas estable sigue siendo `phase7a_pool_hierarchical_80_dual_backfill_20`, que conserva Top-10/MRR del jerarquico y mejora Recall@100 a 0.2667.

## Limitaciones

- Validacion externa preliminar: no habilita ajuste posterior del diccionario ni de pesos con base en evalset.
- La expansion controlada puede beneficiar familias lexicales cubiertas y no necesariamente generaliza a todos los capitulos.
- Las metricas miden recuperacion y ranking documental, no clasificacion oficial ni validacion legal.
