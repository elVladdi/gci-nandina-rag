# Evaluacion pool hibrido historico normativo v0.1

## Objetivo de Fase 9B

Fase 9B construye y evalua pools hibridos de candidatos NANDINA8 combinando recuperacion historica sobre descripciones comerciales con fuentes normativas/lexicales ya generadas en Fase 7A y Fase 8B. La meta es conservar la fuerza de Fase 9A cuando existe precedente historico y medir si las fuentes normativas rescatan casos singleton o aportan trazabilidad sin degradar el ranking.

## Por que despues de Fase 9A

Fase 9A mostro que `historical_bm25_description` alcanza `Top-1 = 0.7967`, `Top-10 = 0.8750`, `Recall@100 = 0.9100` y `MRR = 0.8305`. Ese resultado depende del soporte historico interno: 546 casos tienen precedente de la misma NANDINA8 y 54 casos son singleton. El hibrido se justifica porque el historico puro no puede recuperar una NANDINA8 singleton desde otro caso con la misma etiqueta.

## Fuentes

- Historico: `outputs/evaluation/historical_examples_leave_one_out_v0.1/historical_results.csv` y `historical_case_summary.csv`.
- Fase 7A: `outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool.csv` y `candidate_pool_case_summary.csv`, usando `hierarchical_80_dual_backfill_20`.
- Fase 8B: `outputs/evaluation/nonrestrictive_expanded_pool_evalset_v0.1/expanded_pool.csv` y `expanded_pool_case_summary.csv`, usando `phase7a_plus_all_sources_200`.
- Evalset: `data/processed/evalset_v0.1.csv`.

El BM25 normativo jerarquico queda incorporado a traves de Fase 7A y Fase 8B; no fue necesario generar una fuente adicional de candidatos.

## Estrategias evaluadas

| Estrategia | Tipo | Descripcion |
| --- | --- | --- |
| `historical_first_95_normative_5` | Operativa | Protege 95 candidatos historicos y completa con fuentes normativas. |
| `historical_first_80_normative_20` | Operativa | Protege 80 candidatos historicos y completa con fuentes normativas. |
| `historical_first_50_normative_50` | Operativa | Protege 50 candidatos historicos y completa con fuentes normativas. |
| `historical_plus_normative_rrf` | Operativa | Fusiona historico, Fase 7A y Fase 8B con reciprocal rank fusion. |
| `oracle_historical_if_label_supported_else_normative` | Oraculo diagnostico | Usa soporte de la NANDINA esperada para decidir historico vs normativo; no es regla operativa para casos futuros. |

## Tabla comparativa

| Enfoque | @1 | @10 | @100 | MRR | Singleton rescatados vs 9A | Perdidas vs 9A | Tipo |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Fase 7A | 0.0283 | 0.1067 | 0.2667 | 0.0526 | 8 | 394 | Baseline normativo |
| Fase 8B | 0.0283 | 0.1067 | 0.2633 | 0.0526 | 10 | 398 | Baseline normativo |
| Fase 9A historico puro | 0.7967 | 0.8750 | 0.9100 | 0.8305 | 0 | 0 | Baseline historico |
| `historical_first_95_normative_5` | 0.7967 | 0.8750 | 0.9133 | 0.8305 | 3 | 1 | Operativa |
| `historical_first_80_normative_20` | 0.7967 | 0.8750 | 0.9167 | 0.8306 | 5 | 1 | Operativa seleccionada |
| `historical_first_50_normative_50` | 0.7967 | 0.8750 | 0.9150 | 0.8306 | 8 | 5 | Operativa |
| `historical_plus_normative_rrf` | 0.1367 | 0.2533 | 0.8917 | 0.1762 | 8 | 19 | Operativa, descartada |
| `oracle_historical_if_label_supported_else_normative` | 0.8000 | 0.8833 | 0.9250 | 0.8350 | 10 | 1 | Oraculo diagnostico |

## Correccion metodologica

La estrategia `oracle_historical_if_label_supported_else_normative` no se selecciona como pool oficial porque usa el soporte de la NANDINA esperada (`support_counts[expected]`) para decidir si debe dominar el historico o el bloque normativo. Esa informacion no existe en un caso nuevo. Por eso queda documentada solo como techo diagnostico exploratorio.

La mejor estrategia operativa es `historical_first_80_normative_20`: no necesita conocer la etiqueta esperada, conserva Top-1/Top-10 del historico puro, mejora `Recall@100` de `0.9100` a `0.9167`, rescata 5 singleton y pierde 1 caso frente a Fase 9A.

## Metricas por soporte historico

Para la estrategia operativa seleccionada `historical_first_80_normative_20`:

| Soporte | Casos | @100 | MRR |
| --- | ---: | ---: | ---: |
| singleton | 54 | 0.0926 | 0.0011 |
| 2-4 | 116 | 0.9914 | 0.8576 |
| 5-9 | 82 | 1.0000 | 0.8706 |
| 10+ | 348 | 1.0000 | 0.9408 |

Por tipo de caso:

| Tipo | Casos | @100 | MRR |
| --- | ---: | ---: | ---: |
| Con precedente historico | 546 | 0.9982 | 0.9126 |
| Singleton | 54 | 0.0926 | 0.0011 |

## Analisis de singleton

Fase 9A no recupera singleton por definicion operativa: no existe otro caso con la misma NANDINA8 dentro del banco historico. `historical_first_80_normative_20` rescata 5 de 54 singleton en Top-100 usando fuentes normativas/lexicales, elevando el desempeno singleton a `Recall@100 = 0.0926`. El costo es una perdida frente a Fase 9A en un caso con precedente.

El oraculo diagnostico rescata 10 singleton y llega a `Recall@100 = 0.9250`, pero no es defendible como estrategia operativa porque decide usando la etiqueta esperada. Sirve para mostrar que una politica adaptativa podria mejorar si se disena un criterio observable de confianza historica sin mirar la NANDINA correcta.

## Decision metodologica

La estrategia candidata operativa para Fase 9B es `historical_first_80_normative_20`. El historico queda como fuente dominante y el bloque normativo opera como backfill y soporte de trazabilidad. El oraculo `oracle_historical_if_label_supported_else_normative` queda excluido de la decision operativa y se conserva solo como limite superior diagnostico.

La siguiente fase no debe formalizar una regla basada en soporte de la etiqueta esperada. Debe convertir `historical_first_80_normative_20` en pool oficial auditable o disenar una variante adaptativa basada en senales observables, por ejemplo confianza del ranking historico, margen entre scores, diversidad de NANDINAS historicas o acuerdo historico-normativo.

## Outputs regenerables

La corrida genero outputs ignorados por Git en `outputs/evaluation/hybrid_historical_normative_pool_v0.1/`:

- `hybrid_pool.csv`
- `hybrid_case_summary.csv`
- `hybrid_metrics.json`
- `hybrid_summary.md`
- `hybrid_rescue_cases.csv`
- `hybrid_loss_cases.csv`
- `hybrid_singleton_cases.csv`
- `hybrid_source_contribution.csv`

## Politica de ejecucion

No se uso LLM, Ollama, OpenAI ni APIs remotas. La fase se ejecuto con codigo local deterministico sobre artefactos locales del repositorio.
