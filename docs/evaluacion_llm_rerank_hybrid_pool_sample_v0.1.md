# Evaluacion LLM rerank hybrid pool sample v0.1

## Objetivo

Fase 9C-A ejecuta una prueba diagnostica minima de LLM como re-ranker cerrado sobre el pool hibrido operativo de Fase 9B. La hipotesis es que el modelo puede reordenar una lista corta de candidatos sin inventar codigos y sin degradar fuertemente el ranking original.

Esta fase solo mide ranking, adherencia JSON y violaciones de pool. No evalua auditabilidad ni explicaciones largas.

## Modelo usado

- Modelo: `qwen2.5:7b-instruct`.
- Motor: Ollama local disponible en `127.0.0.1:11434`.
- Temperatura: 0.
- APIs remotas: no usadas.
- OpenAI: no usado.

## Pool y muestra

- Pool usado: `historical_first_80_normative_20`.
- Candidate limit enviado al LLM: 10.
- Oraculo: no usado. Las filas con `oracle` en el nombre de estrategia fueron omitidas.
- Casos evaluados: 20.

Composicion deterministica de muestra:

| Categoria objetivo | Casos | Nota |
| --- | ---: | --- |
| rank 1 | 5 | Categoria exacta. |
| rank 2-10 | 5 | Categoria exacta. |
| rank 11-100 | 5 | Categoria exacta; la correcta no esta dentro del Top-10 enviado. |
| singleton | 5 | Categoria exacta. |

## Metricas original vs LLM

| Ranking | Top-1 | Top-3 | Top-5 | Top-10 | MRR |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original enviado | 0.2500 | 0.4500 | 0.5000 | 0.5000 | 0.3542 |
| LLM | 0.2000 | 0.4500 | 0.4500 | 0.5000 | 0.3083 |

## Adherencia y violaciones

| Indicador | Valor |
| --- | ---: |
| JSON valido | 20/20 |
| Tasa JSON valido | 1.0000 |
| Casos con codigos fuera del pool | 0 |
| Codigos fuera del pool total | 0 |
| Rank 1 fuera del pool | 0 |
| Casos con duplicados | 0 |
| Rankings incompletos | 13 |

Los rankings incompletos significan que el modelo devolvio menos de 10 candidatos validos y unicos en 13 casos, aunque no invento codigos ni saco el rank 1 fuera del pool.

## Ganados, perdidos y sin cambio

| Resultado | Casos |
| --- | ---: |
| Ganados | 0 |
| Perdidos | 4 |
| Sin cambio | 16 |
| Top-1 correcto degradado | 1 |
| LLM sube la NANDINA correcta | 0 |

El LLM degrado un caso originalmente correcto en Top-1 y empeoro el rank de tres casos adicionales. No subio la NANDINA correcta en ningun caso.

## Decision

No escalar a 9C-B. Aunque el modelo mantuvo adherencia al pool y produjo JSON valido en todos los casos, degrado Top-1 (`0.2500` a `0.2000`) y MRR (`0.3542` a `0.3083`) frente al ranking original enviado. Bajo la regla de decision de 9C-A, el re-ranking no debe ampliarse.

Si se desea usar LLM en una fase posterior, conviene reservarlo para justificacion breve o explicacion controlada de candidatos ya seleccionados, no como re-ranker operativo, salvo que una nueva configuracion demuestre no degradar ranking.

## Outputs regenerables

La corrida genero outputs ignorados por Git en `outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1/`:

- `sample_cases.csv`
- `llm_rerank_raw.jsonl`
- `llm_rerank_normalized.csv`
- `llm_rerank_metrics.json`
- `llm_rerank_summary.md`
- `llm_rerank_case_comparison.csv`

## Politica de ejecucion

No se uso OpenAI ni APIs remotas. Solo se uso Ollama local con el modelo ya instalado `qwen2.5:7b-instruct`; no se descargo ningun modelo.
