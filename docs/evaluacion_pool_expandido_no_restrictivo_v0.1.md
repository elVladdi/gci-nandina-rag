# Evaluacion pool expandido no restrictivo v0.1

## Alcance

La Fase 8B prueba un pool expandido no restrictivo de candidatos NANDINA8. La Fase 8A restrictiva no funciono porque filtrar NANDINA8 por familias HS2/HS4/HS6 recuperadas redujo cobertura exacta en devset frente a buscar directamente NANDINA8 y frente al pool Fase 7A.

Esta fase usa las familias HS2/HS4/HS6 como senales auxiliares de expansion, no como filtro excluyente. El ranking base se conserva en posiciones protegidas y las fuentes auxiliares agregan backfill deduplicado por NANDINA8.

No se uso LLM, Ollama, OpenAI, Text2Trade, requests, HTTP ni APIs remotas. La estrategia se selecciono solo con devset; el evalset se ejecuto una vez con esa estrategia congelada.

## Fuentes

- `BM25_hierarchical_v0.1`.
- `phase7a_pool_hierarchical_80_dual_backfill_20`.
- `BM25_fielded_weighted_v0.1`.
- `BM25_fielded_weighted_expanded_v0.1`.
- Backfill por familias HS2, HS4 y HS6.
- Recuperacion directa NANDINA8 del indice por niveles.

## Seleccion en devset

Estrategia seleccionada:

- `phase7a_plus_all_sources_200`
- `pool_depth = 200`
- `protected_base = 50`
- `HS2 Top-M = 3`
- `HS4 Top-M = 5`
- `HS6 Top-M = 10`

La seleccion maximizo cobertura amplia a Top-200. Esta decision acepto una perdida devset frente al pool 7A a Top-100 para ganar tres rescates a Top-200. Esa tension queda documentada y no se ajusto despues de mirar evalset.

| Metodo | Pool | Final@10 | Final@20 | Final@50 | Final@100 | Final@200 | HS2@100 | HS4@100 | HS6@100 | Rescates@100 | Perdidas@100 | Rescates@200 | Perdidas@200 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| phase7a base | 100 | 0.6154 | 0.6154 | 0.6923 | 0.7692 | NA | 0.9231 | 0.9231 | 0.7692 | 0 | 0 | NA | NA |
| phase7a_plus_all_sources_200 | 200 | 0.6154 | 0.6154 | 0.6923 | 0.6923 | 0.9231 | 0.9231 | 0.9231 | 0.6923 | 0 | 1 | 3 | 1 |

## Evalset congelado

| Metodo | Pool | Final@10 | Final@20 | Final@50 | Final@100 | Final@200 | HS2@100 | HS4@100 | HS6@100 | Rescates@100 | Perdidas@100 | Rescates@200 | Perdidas@200 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| phase7a base | 100 | 0.1067 | 0.1283 | 0.2033 | 0.2667 | NA | 0.5283 | 0.2983 | 0.2717 | 0 | 0 | NA | NA |
| phase7a_plus_all_sources_200 | 200 | 0.1067 | 0.1283 | 0.2033 | 0.2633 | 0.3233 | 0.5533 | 0.3033 | 0.2683 | 4 | 6 | 34 | 0 |

El resultado mejora cobertura amplia si se permite Top-200: `Recall@200` llega a `0.3233`. Frente al pool Fase 7A, `Recall@100` no mejora: queda en `0.2633` contra `0.2667`; a ese corte hay 4 rescates y 6 perdidas por desplazamiento. A Top-200 no se pierden casos que el pool 7A recuperaba y se rescatan 34 casos adicionales.

## Decision

Fase 8B muestra que la expansion no restrictiva agrega cobertura a Top-200, pero no soluciona el cuello de botella a Top-100. El techo sigue lejos de `0.90`: con `Recall@200 = 0.3233`, falta `0.5767` para llegar a `0.90`.

No conviene seguir ampliando solo con recuperacion lexical no restrictiva como linea principal. Conviene pasar a una Fase 9 orientada a evidencia historica y/o clasificador supervisado, manteniendo este pool expandido como fuente auxiliar de alto recall para experimentos posteriores.
