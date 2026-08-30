# EXP-04 Fase E: candidate pools normativos v0.2

## Ejecución reproducible

- Experimento: `exp04_phase_e_normative_candidate_pools_v0.2` (`EXP-04-E`).
- Evalset: `data/processed/data_aduanas_evalset_clase87_v0.2.csv`, SHA-256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`, 1,056 casos.
- Runner: `python -B -m src.experiments.evaluate_normative_candidate_pools_data_aduanas_v02`.
- Commit de ejecución: `36373e4f637c5f904948ffd48c8540f03e750f1e` en `codex/exp04-rerun-v02`.
- Compatibilidad A/B/C/D1a/E: `compatible = true`, mismos `case_id` y mismas etiquetas. D0 permanece excluido como `INVALID AS FINAL COMPARATOR - LEGACY VECTOR INDEX NOT REPRODUCIBLE`.
- El mayor artefacto es `candidate_pool_results.csv` con 20.34 MiB; no hubo outputs mayores de 25 MiB ni de 50 MiB.

## Definiciones congeladas

El inventario y la evidencia preexistente están en `docs/exp04_phase_e_candidate_pool_inventory.md`. `dual` combina dos índices BM25 normativos de ablation: precisión `C_hs6_leaf.pkl` (HS6 + hoja NANDINA-8) y recall `D_4d_hs6_leaf.pkl` (HS4 + HS6 + hoja NANDINA-8). No mezcla BM25 plano y jerárquico, no pondera scores y no usa etiquetas.

`dual protegido` conserva primero cinco candidatos únicos de precisión, agrega candidatos nuevos de recall y termina con candidatos nuevos de precisión. Cada pool conserva el primer código NANDINA-8 que aparece; cualquier repetición se descarta.

Los pools usan exclusivamente jerárquico y dual. Histórico, plano y D1a se mantienen en la tabla de rankings y trazabilidad, no en la composición de pool. La variante 70/30 es `B — histórico pero no formalmente congelado para v0.2`; se reporta descriptivamente, sin selección confirmatoria.

La unión `diagnostic_union_hierarchical_dual` es **DIAGNOSTIC ORACLE-LIKE UNION / COVERAGE CEILING**: construye la unión de ambos Top-N sin consultar la etiqueta. No es ranking y no reporta Top-k ni MRR.

## Tabla de rankings

| Estrategia | Top-1 | Top-3 | Top-5 | Top-10 | Top-50 | Recall@100 | MRR@100 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Histórico BM25 | 0.509470 | 0.671402 | 0.763258 | 0.891098 | 0.991477 | 0.991477 | 0.629708 |
| Normativo plano | 0.027462 | 0.051136 | 0.061553 | 0.065341 | 0.070076 | 0.071023 | 0.042297 |
| Normativo jerárquico | 0.026515 | 0.052083 | 0.062500 | 0.065341 | 0.090909 | 0.101326 | 0.041981 |
| D1a Text2Trade-inspired MNRL | 0.000000 | 0.003788 | 0.034091 | 0.156250 | 0.305871 | 0.345644 | 0.032424 |
| Dual protegido | 0.021780 | 0.041667 | 0.052083 | 0.064394 | 0.091856 | 0.100379 | 0.037003 |

## Candidate pools

| Pool | N | Tamaño efectivo medio | Recall/Pool | HS6 | HS4 | Chapter |
|---|---:|---:|---:|---:|---:|---:|
| Jerárquico | 100 | 99.761 | 107/1056 (0.101326) | 0.111742 | 0.250000 | 0.509470 |
| Dual protegido | 100 | 99.451 | 106/1056 (0.100379) | 0.114583 | 0.256629 | 0.547348 |
| Jerárquico 80 + dual 20 | 100 | 99.761 | 107/1056 (0.101326) | 0.111742 | 0.250000 | 0.509470 |
| Jerárquico 70 + dual 30 (descriptivo B) | 100 | 99.761 | 108/1056 (0.102273) | 0.112689 | 0.250947 | 0.509470 |
| Jerárquico | 200 | 192.105 | 321/1056 (0.303977) | 0.343750 | 0.500947 | 0.767045 |
| Dual protegido | 200 | 191.122 | 281/1056 (0.266098) | 0.321970 | 0.485795 | 0.783144 |
| Jerárquico 80 + dual 20 | 200 | 192.105 | 321/1056 (0.303977) | 0.343750 | 0.500947 | 0.767045 |
| Jerárquico 70 + dual 30 (descriptivo B) | 200 | 192.105 | 321/1056 (0.303977) | 0.343750 | 0.500947 | 0.767045 |

La unión diagnóstica cubre 113/1056 (0.107008) a profundidad de fuentes 100 con tamaño efectivo medio 112.722, y 322/1056 (0.304924) a 200 con tamaño efectivo medio 217.770. Esa diferencia de cardinalidad impide compararla como pool de igual tamaño o como sistema final.

## Complementariedad y backfill

Entre jerárquico y dual: a 100 recuperan ambos 100 casos, solo jerárquico 7, solo dual 6 y ninguno 943; a 200: ambos 280, solo jerárquico 41, solo dual 1 y ninguno 734. La unión de diagnóstico suma precisamente esos casos, no una señal de ranking.

A 100, el backfill 80/20 no añade recuperaciones y el 70/30 añade 1 caso (0.93% relativo frente a 107), pero este último no es confirmatorio para v0.2. A 200, 80/20 y 70/30 no añaden casos sobre el jerárquico. `hierarchical_first_100` añade un caso a 200, pero pierde 42 por desplazar candidatos jerárquicos 101--200; por ello no representa una ampliación neta.

La tabla `candidate_pool_unrecovered_cases.csv` contiene los 734 casos que la unión normativa no recupera a 200, con flags históricos reutilizados solo para diagnóstico; no intervienen en la construcción de los pools.

## Dictamen OE2 / HE2

- **HE2-A — ranking temprano: SUPPORTED.** Histórico BM25 supera a todos los comparadores normativos y a D1a en Top-k y MRR@100: 0.629708 frente al máximo no histórico de 0.042297.
- **HE2-B — cobertura profunda: PARTIALLY SUPPORTED.** El ranking jerárquico alcanza 321/1056 a 200 frente a 107/1056 a 100, pero los candidate pools entregables no superan de manera material al jerárquico a igual tamaño: el mejor cambio confirmatorio a 200 es 0. La unión diagnóstica llega a 322/1056, pero tiene media de 217.770 candidatos y no es una configuración entregable.
- **HE2 global: PARTIALLY SUPPORTED.** El contraste temprano favorece con claridad al histórico; la recuperación normativa profunda existe, pero la evidencia no confirma una ganancia operacional de los pools híbridos sobre el jerárquico de igual cardinalidad.

Este dictamen cierra experimentalmente OE2/HE2 sin iniciar OE3/HE3, Fase F, integración histórico-normativa ni reranking.
