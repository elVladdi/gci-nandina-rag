# EXP-04 Fase E: inventario y congelamiento de candidate pools v0.2

## Hallazgo histórico

La implementación anterior relevante es `src/experiments/build_candidate_pool_data_aduanas.py`, introducida en `8c8ea112` (2026-07-30) y actualizada en `9dbd817` (2026-08-01). Trabaja únicamente con fuentes normativas y define cinco pools operativos a profundidades 10, 20, 50, 100 y 200:

| Variante | Definición histórica | Tipo |
|---|---|---|
| `hierarchical_only` | ranking BM25 jerárquico, deduplicado por primera aparición | candidate pool de fuente única |
| `dual_only` | ranking dual protegido | candidate pool de fuente única |
| `hierarchical_first_100` | 100 posiciones jerárquicas antes de cualquier dual | candidate pool híbrido |
| `hierarchical_80_dual_backfill_20` | 80 jerárquicas y 20 duales dentro de las primeras 100 posiciones | candidate pool híbrido |
| `hierarchical_70_dual_backfill_30` | 70 jerárquicas y 30 duales dentro de las primeras 100 posiciones | candidate pool híbrido |

Después de la primera centena, el código histórico completa con dual remanente y después jerárquico remanente, siempre con deduplicación por primera aparición. A profundidad menor que 100, la misma regla escala el bloque inicial: por ejemplo, 80/20 produce 40 jerárquicos y 10 duales a profundidad 50.

## Dual y dual protegido

`dual` no significa una mezcla plano/jerárquico ni una ponderación de scores. Usa dos índices BM25 normativos de ablation:

- precisión: `C_hs6_leaf.pkl`, representación HS-6 + hoja NANDINA-8;
- recall: `D_4d_hs6_leaf.pkl`, representación HS-4 + HS-6 + hoja NANDINA-8.

`protected_top_5_backfill` agrega, en orden: Top-5 del índice de precisión, candidatos nuevos del índice de recall y candidatos nuevos restantes de precisión. Se deduplica por código NANDINA-8 y luego se trunca a la profundidad solicitada. No usa pesos ni la etiqueta esperada. "Protegido" describe la preservación de las primeras cinco posiciones de precisión frente al backfill amplio.

## Unión diagnóstica

La implementación histórica llama `union_oracle` a la unión de los candidatos jerárquicos y duales en cada profundidad. No usa la etiqueta para construir candidatos, por lo que aquí se etiqueta con precisión como **DIAGNOSTIC ORACLE-LIKE UNION / COVERAGE CEILING**: es un conjunto no ordenado para medir cobertura, no un ranking entregable y no genera Top-k ni MRR.

## Preespecificación 70/30

`hierarchical_70_dual_backfill_30` está presente como código y output histórico desde Fase 7A, por lo que no es una variante inventada para v0.2. Sin embargo, no existe una configuración v0.2 independiente que la congele antes de la campaña, y la documentación v0.1 la llamó "mejor" tras métricas de eval v0.1. Se clasifica **B: histórico pero no formalmente congelado para v0.2**. Se evaluará descriptivamente, sin seleccionarla como configuración confirmatoria de HE2.

## Fuentes admitidas y exclusiones

Fase E v0.2 reutiliza el ranking jerárquico v0.2 como fuente primaria y reconstruye el dual protegido con los dos índices históricos congelados, aplicados al evalset v0.2. BM25 plano v0.2, histórico y D1a permanecen en la tabla de rankings y el reporte de compatibilidad, pero no entran en la composición de pools: la definición histórica de Fase 7A no los incluía. D0 queda excluido de toda comparación confirmatoria.

Las profundidades 50, 100 y 200 ya estaban contempladas históricamente. La métrica central será presencia exacta en el conjunto (PoolRecall), con cobertura HS6, HS4 y capítulo; no habrá MRR para pools ni para la unión diagnóstica.
