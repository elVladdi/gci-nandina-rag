# Evaluacion recuperacion historica data_aduanas clase 87 v0.1

## Objetivo

Esta actualizacion de Fase 9A reemplaza el diagnostico leave-one-out sobre el evalset historico de 600 casos por una prueba con banco historico real separado: `data_aduanas` clase 87. El objetivo es medir si descripciones comerciales previamente clasificadas permiten recuperar la NANDINA correcta para casos nuevos sin usar texto normativo como fuente de candidatos.

## Diferencia frente al leave-one-out anterior

La Fase 9A original usaba `data/processed/evalset_v0.1.csv` como banco inicial y excluia el propio caso consultado. Esa corrida fue util para demostrar el valor de precedentes clasificados, pero estaba condicionada a la cobertura interna del evalset.

Esta actualizacion usa particiones distintas:

- Historico: `data/processed/data_aduanas_historico_clase87_v0.1.csv`, 3,000 filas.
- Evalset: `data/processed/data_aduanas_evalset_clase87_v0.1.csv`, 1,006 filas.
- Consulta: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta: `NANDINA`.

La validacion confirma `id_unico_overlap_count = 0`. No hay self-match entre historico y evaluacion.

## Justificacion metodologica

La literatura revisada sobre clasificacion HS/tariff suele mejorar los resultados cuando incorpora casos historicos, precedentes clasificados, embeddings o modelos supervisados. Esta fase aisla el componente mas auditable de esa idea: recuperar por similitud textual contra ejemplos historicos ya etiquetados.

No se uso LLM, Ollama, Text2Trade, OpenAI ni APIs remotas. Tampoco se uso BM25 normativo como fuente de candidatos.

## Protocolo

El script versionable `src/experiments/evaluate_historical_retrieval_data_aduanas.py` construye un indice BM25 local sobre las 3,000 descripciones historicas. Para cada una de las 1,006 consultas del evalset:

1. Calcula scores BM25 contra el historico.
2. Ordena instancias historicas por score.
3. Deduplica el ranking final por `NANDINA`, preservando la mejor evidencia historica de cada codigo.
4. Conserva hasta 100 candidatos NANDINA8 por caso.
5. Registra el caso historico que sostiene cada candidato.

La profundidad historica operativa fue `history_depth = 500` y la profundidad final `candidate_depth = 100`.

## Metodo evaluado

| Metodo | Fuente de candidatos | Comentario |
| --- | --- | --- |
| `historical_bm25_data_aduanas_clase87` | Historico `data_aduanas` clase 87 | BM25 local sobre descripciones comerciales; sin normas como fuente de candidatos. |

## Metricas globales

| Metrica | Valor |
| --- | ---: |
| Casos evaluados | 1,006 |
| NANDINA esperada presente en historico | 1,006 |
| NANDINA esperada ausente en historico | 0 |
| Top-1 | 0.8638 |
| Top-3 | 0.9384 |
| Top-5 | 0.9612 |
| Top-10 | 0.9791 |
| Top-20 | 0.9960 |
| Top-50 | 0.9980 |
| Recall@100 | 0.9980 |
| MRR | 0.9071 |
| Casos fuera de Top-100 | 2 |

## Metricas jerarquicas

| Nivel | @10 | @50 | @100 |
| --- | ---: | ---: | ---: |
| Partida | 1.0000 | 1.0000 | 1.0000 |
| Sub Partida | 0.9920 | 1.0000 | 1.0000 |
| Clase | 1.0000 | 1.0000 | 1.0000 |

## Soporte historico

| Bucket soporte historico | Casos | Top-1 | Top-10 | Recall@100 | MRR |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 1 | 5 | 0.8000 | 0.8000 | 0.8000 | 0.8000 |
| 2-4 | 7 | 0.2857 | 0.8571 | 1.0000 | 0.4966 |
| 5-9 | 32 | 0.8125 | 0.9688 | 0.9688 | 0.8776 |
| 10+ | 962 | 0.8701 | 0.9813 | 1.0000 | 0.9116 |

La recuperacion es casi completa cuando existe soporte historico amplio. Los dos fallos Top-100 estan en:

- `87089911`: 1 precedente historico, 1 caso eval, 0 recuperados en Top-100.
- `87089950`: 9 precedentes historicos, 2 casos eval, 1 recuperado en Top-100.

## Comparacion metodologica

La referencia normativa actualizada de Fase 7A sobre `data_aduanas` clase 87 reporta:

- Mejor pool operativo normativo @100: `0.3489`.
- Mejor pool operativo normativo @200: `0.6272`.

La recuperacion historica real alcanza `Recall@100 = 0.9980`, con `Top-1 = 0.8638` y `MRR = 0.9071`. La mejora es sustancial y no depende de BM25 normativo como fuente de candidatos.

La comparacion no debe interpretarse como que las normas son innecesarias. El historico domina cuando hay precedentes suficientes; el bloque normativo sigue siendo necesario para trazabilidad, explicacion y codigos con poco o ningun soporte historico.

## Outputs

La corrida genera outputs regenerables e ignorados por Git en:

```text
outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/
```

Archivos principales:

- `historical_results.csv`
- `historical_metrics.json`
- `historical_summary.md`
- `historical_case_summary.csv`
- `historical_failure_cases.csv`
- `historical_rescue_cases.csv`
- `historical_support_by_nandina.csv`

## Decision

La Fase 9A actualizada confirma que el historico real debe ser la fuente dominante de recuperacion para clase 87 cuando existe precedente clasificado. Para Fase 9B se recomienda construir un pool hibrido `historico primero + backfill normativo`, priorizando el ranking historico y reservando senales normativas para trazabilidad y para familias con bajo soporte historico.

Si en una validacion temporal futura aparecen NANDINAs ausentes del historico, la recomendacion debe ajustarse: ampliar el banco historico real y usar recuperacion normativa o clasificadores supervisados como respaldo controlado.
