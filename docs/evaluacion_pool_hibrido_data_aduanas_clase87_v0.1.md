# Evaluacion pool hibrido data_aduanas clase 87 v0.1

## Objetivo

Esta actualizacion de Fase 9B construye y evalua un pool hibrido historico + normativo sobre `data_aduanas` clase 87. Parte de la Fase 9A actualizada, que recupera contra un historico real separado, y del pool normativo de Fase 7A actualizada.

La pregunta metodologica es si el bloque normativo mejora el pool historico real sin fuga por `id_unico`, sin usar la etiqueta esperada para decidir reglas y sin degradar el ranking temprano.

## Diferencia con Fase 9B historica

La Fase 9B historica usaba el evalset viejo de 600 casos y combinaba el leave-one-out historico con Fase 7A/Fase 8B antiguas. Esa evidencia se conserva como antecedente.

Esta actualizacion usa particiones separadas de `data_aduanas` clase 87:

- Historico real: `data/processed/data_aduanas_historico_clase87_v0.1.csv`, 3,000 filas.
- Evalset: `data/processed/data_aduanas_evalset_clase87_v0.1.csv`, 1,006 filas.
- Historico 9A: `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/`.
- Normativo 7A: `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/`.

La validacion confirma `id_unico_overlap_count = 0`. No hay self-match entre historico y evalset.

## Fuentes

| Fuente | Estrategia usada | Rol |
| --- | --- | --- |
| Historico real Fase 9A | `historical_bm25_data_aduanas_clase87` | Ranking principal. |
| Normativo Fase 7A | `hierarchical_70_dual_backfill_30` | Backfill y trazabilidad normativa. |

Se eligio `hierarchical_70_dual_backfill_30` como fuente normativa porque fue el mejor pool operativo normativo a Top-100 sobre clase 87 (`0.3489`). A Top-200 empata con `hierarchical_80_dual_backfill_20` (`0.6292`).

## Estrategias evaluadas

| Estrategia | Regla |
| --- | --- |
| `historical_only` | Solo candidatos historicos. |
| `historical_first_90_normative_10` | Primer bloque Top-100 con 90 historicos y 10 normativos; luego remanentes. |
| `historical_first_80_normative_20` | Primer bloque Top-100 con 80 historicos y 20 normativos; luego remanentes. |
| `historical_first_70_normative_30` | Primer bloque Top-100 con 70 historicos y 30 normativos; luego remanentes. |
| `historical_first_50_normative_50` | Primer bloque Top-100 con 50 historicos y 50 normativos; luego remanentes. |
| `historical_with_normative_backfill_if_low_support` | Si el Top-1 historico observado tiene soporte historico menor que 10, adelanta backfill 70/30; si no, historico primero y normativo despues. |
| `historical_with_normative_backfill_if_missing_code` | Si no hay candidatos historicos observados, usa normativo; si hay, conserva historico primero y agrega normativo despues. |
| `normative_only_reference` | Referencia normativa pura con `hierarchical_70_dual_backfill_30`. |

Las reglas de bajo soporte y codigo faltante usan solo senales observables del ranking o del banco historico. No usan la NANDINA esperada para decidir.

## Metricas globales

| Estrategia | Top-1 | Top-10 | Top-20 | Top-50 | Top-100 | Top-200 | MRR | Fuera Top-100 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `historical_only` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 | 0 |
| `historical_first_90_normative_10` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 | 0 |
| `historical_first_80_normative_20` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 | 0 |
| `historical_first_70_normative_30` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 | 0 |
| `historical_first_50_normative_50` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 | 0 |
| `historical_with_normative_backfill_if_low_support` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 | 0 |
| `historical_with_normative_backfill_if_missing_code` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 | 0 |
| `normative_only_reference` | 0.0249 | 0.0497 | 0.0517 | 0.0626 | 0.3489 | 0.6292 | 0.0407 | 655 |

Ningun hibrido mejora Top-100 frente a `historical_only` porque el historico corregido ya alcanza cobertura completa a Top-100. Todos los hibridos operativos mantienen Top-1, Top-10, Top-20, Top-50, Top-100, Top-200 y MRR. El backfill normativo queda como respaldo/trazabilidad posterior, no como fuente de rescate en esta corrida.

## Metricas jerarquicas

Para la estrategia recomendada `historical_with_normative_backfill_if_missing_code`:

| Nivel | @10 | @50 | @100 | @200 |
| --- | ---: | ---: | ---: | ---: |
| Partida | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Sub Partida | 0.9920 | 1.0000 | 1.0000 | 1.0000 |
| Clase | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

## Soporte historico

Para la estrategia recomendada:

| Bucket soporte historico | Casos | Top-1 | Top-10 | Top-100 | Top-200 | MRR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 1 | 5 | 0.8000 | 0.8000 | 1.0000 | 1.0000 | 0.8077 |
| 2-4 | 7 | 0.2857 | 0.8571 | 1.0000 | 1.0000 | 0.4813 |
| 5-9 | 32 | 0.8125 | 0.9688 | 1.0000 | 1.0000 | 0.8783 |
| 10+ | 962 | 0.8690 | 0.9823 | 1.0000 | 1.0000 | 0.9108 |

Todas las NANDINAS esperadas del evalset estan presentes en el historico. Por eso esta corrida no mide todavia el valor real del backfill normativo para codigos completamente ausentes; esa condicion requiere validacion futura con particiones temporales o historicos ampliados.

## Casos de bajo soporte y fallos historicos

La Fase 9A corregida no deja casos fuera de Top-100. Las NANDINAS de bajo soporte historico se mantienen como watchlist metodologica, pero no generan fallos de cobertura en esta corrida.

## Contribucion por fuente

Para la estrategia recomendada, entre los aciertos Top-100:

| Fuente del codigo esperado | Casos |
| --- | ---: |
| Historico solo | 373 |
| Historico y normativo | 633 |
| Normativo solo | 0 |

El normativo no rescata casos adicionales a Top-100, pero aporta presencia concurrente para 633 aciertos y evidencia normativa asociada para trazabilidad. En el output normativo hubo 5 casos sin candidatos para la estrategia `hierarchical_70_dual_backfill_30`; el historico cubre esos casos.

## Comparacion contra referencias

| Referencia | Top-1 | Top-10 | Top-100 | Top-200 | MRR |
| --- | ---: | ---: | ---: | ---: | ---: |
| Historico solo Fase 9A | 0.8628 | 0.9801 | 1.0000 | 1.0000 | 0.9062 |
| Normativo solo Fase 7A | 0.0249 | 0.0497 | 0.3489 | 0.6292 | 0.0407 |
| Hibrido recomendado | 0.8628 | 0.9801 | 1.0000 | 1.0000 | 0.9062 |

No hay ganancia de cobertura exacta del hibrido frente al historico en esta corrida corregida, porque el historico ya cubre Top-100 y Top-200. A profundidades relevantes para un re-ranker corto o LLM posterior (`10`, `20`, `50`), el historico real domina y el normativo no cambia el resultado.

## Decision

La configuracion recomendada es `historical_with_normative_backfill_if_missing_code`.

Motivo: conserva el ranking historico como orden operativo principal, no degrada Top-1, Top-10, Top-20, Top-50, Top-100 ni MRR, y agrega backfill normativo posterior para trazabilidad y robustez futura. En clase 87, el historico solo ya debe mantenerse como ranking principal; el normativo debe entrar como respaldo/trazabilidad, no como fuente que desplace candidatos historicos tempranos.

Para una futura fase LLM+RAG de explicacion, la recomendacion es alimentar el re-ranker o justificador con un pool corto dominado por historico. Si se usan pocos candidatos (`10`, `20` o `50`), el ranking debe permanecer historico. La evidencia normativa puede adjuntarse como contexto explicativo de los codigos ya recuperados o como backfill posterior cuando el historico no tenga candidatos.

## Outputs

Outputs regenerables e ignorados por Git:

```text
outputs/evaluation/hybrid_pool_data_aduanas_clase87_v0.1/
```

Archivos generados:

- `hybrid_pool.csv`
- `hybrid_case_summary.csv`
- `hybrid_metrics.json`
- `hybrid_summary.md`
- `hybrid_source_contribution.csv`
- `hybrid_rescue_loss_cases.csv`
- `hybrid_low_support_cases.csv`

## Politica de ejecucion

No se uso LLM, Ollama, Text2Trade, Dense, OpenAI ni APIs remotas. No se modificaron los splits clase 87, el evalset historico v0.1, el devset historico ni el Excel fuente.
