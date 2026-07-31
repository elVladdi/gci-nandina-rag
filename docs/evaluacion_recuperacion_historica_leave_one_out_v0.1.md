# Evaluacion recuperacion historica leave-one-out v0.1

## Proposito de Fase 9A

Fase 9A diagnostica si el lenguaje comercial del propio `evalset_v0.1.csv` permite recuperar la NANDINA correcta usando casos previamente clasificados como precedentes historicos. El objetivo no es declarar un modelo final, sino medir el techo inicial de un banco de pares `descripcion -> nandina_ref` bajo un protocolo leave-one-out.

## Justificacion metodologica

La literatura revisada sobre clasificacion HS/tariff classification reporta mejores resultados cuando se incorporan precedentes clasificados, embeddings o modelos supervisados, no solo texto normativo. Esta fase prueba la hipotesis minima y auditable: si existen descripciones comerciales similares ya clasificadas, un recuperador local sobre ejemplos historicos puede proponer codigos NANDINA8 con mayor cobertura que un pool lexical/normativo puro.

## Protocolo leave-one-out

- Dataset: `data/processed/evalset_v0.1.csv`.
- Casos evaluados: 600.
- Para cada fila, la consulta es `descripcion`.
- El indice historico contiene las otras 599 filas.
- Se excluye explicitamente el caso consultado para evitar self-match.
- El ranking final por caso se deduplica por `nandina_ref`.
- Profundidad maxima evaluada: Top-100 candidatos NANDINA8 unicos.
- No se modifica `devset`, `evalset` ni el Excel fuente.

## Metodos evaluados

| Metodo | Estado | Descripcion |
| --- | --- | --- |
| `historical_bm25_description` | Ejecutado | BM25 local sobre `descripcion`, con normalizacion deterministica y ranking leave-one-out. |
| `historical_tfidf_char_word` | Omitido | `scikit-learn` no esta disponible en el runtime local usable; no se instalo nada. |

## Metricas principales

| Metodo | @1 | @3 | @5 | @10 | @20 | @50 | @100 | MRR | Fuera Top-100 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `historical_bm25_description` NANDINA8 exacta | 0.7967 | 0.8617 | 0.8683 | 0.8750 | 0.8750 | 0.9017 | 0.9100 | 0.8305 | 54 |

Metricas jerarquicas:

| Familia | @1 | @3 | @5 | @10 | @20 | @50 | @100 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| HS6 | 0.8117 | 0.8650 | 0.8717 | 0.8800 | 0.8817 | 0.9050 | 0.9133 |
| HS4 | 0.8567 | 0.8783 | 0.8850 | 0.9017 | 0.9100 | 0.9350 | 0.9450 |
| HS2 | 0.8833 | 0.9033 | 0.9233 | 0.9517 | 0.9683 | 0.9833 | 0.9833 |

## Lectura por soporte historico interno

El resultado `Recall@100 = 0.9100` debe interpretarse condicionado por la existencia de precedentes de la misma NANDINA dentro del banco evaluado. En leave-one-out, los codigos con una sola instancia no tienen otro caso historico de su misma NANDINA contra el cual recuperarse.

| Soporte total de NANDINA8 en evalset | Casos | Recuperados@100 | Fallos@100 | Recall@100 |
| --- | ---: | ---: | ---: | ---: |
| 1 | 54 | 0 | 54 | 0.0000 |
| 2-4 | 116 | 116 | 0 | 1.0000 |
| 5-9 | 82 | 82 | 0 | 1.0000 |
| 10+ | 348 | 348 | 0 | 1.0000 |

En consecuencia, Fase 9A no debe leerse como desempeno final general sobre casos futuros, sino como evidencia de que la recuperacion historica es muy fuerte cuando existe precedente comparable. La validacion externa requiere historicos reales adicionales o particiones temporales donde el banco de busqueda y el lote evaluado esten separados.
## Comparacion contra Fase 7A/8B

Los outputs existentes fueron encontrados y leidos:

- Fase 7A: `outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool_case_summary.csv`.
- Fase 8B: `outputs/evaluation/nonrestrictive_expanded_pool_evalset_v0.1/expanded_pool_case_summary.csv`.

| Enfoque | Recall@100 NANDINA8 | Recall@200 NANDINA8 |
| --- | ---: | ---: |
| Fase 7A pool lexical/normativo | 0.2667 | NA |
| Fase 8B pool expandido no restrictivo | 0.2633 | 0.3233 |
| Fase 9A historico BM25 leave-one-out | 0.9100 | NA |

El recuperador historico rescata 400 casos frente a Fase 7A/8B cuando se evalua Top-100: 394 frente a Fase 7A, 398 frente a Fase 8B y 392 frente a ambas. Persisten 54 casos fuera de Top-100 historico.

## Analisis de error

Por HS2, las familias con mayor cantidad de fallos Top-100 son:

| HS2 | Casos | Fallos Top-100 | Recall@100 |
| --- | ---: | ---: | ---: |
| 85 | 35 | 10 | 0.7143 |
| 82 | 8 | 6 | 0.2500 |
| 39 | 55 | 5 | 0.9091 |
| 84 | 24 | 5 | 0.7917 |
| 94 | 16 | 3 | 0.8125 |

Por HS4, las familias con mas fallos son `8509`, `8516`, `9405`, `4202`, `2917`, `8302` y `8518`. Parte de los fallos se explica por clases con pocos precedentes utiles o descripciones con mucho ruido administrativo repetido; el evalset funciona como banco historico inicial, pero no sustituye un historico real amplio y curado.

## Outputs regenerables

La corrida genero outputs ignorados por Git en `outputs/evaluation/historical_examples_leave_one_out_v0.1/`:

- `historical_results.csv`
- `historical_metrics.json`
- `historical_summary.md`
- `historical_case_summary.csv`
- `historical_failure_cases.csv`
- `historical_rescue_cases.csv`

## Decision

Fase 9A mejora sustancialmente Recall@100 frente a Fase 7A y Fase 8B: pasa de `0.2667`/`0.2633` a `0.9100`. La recomendacion es ejecutar Fase 9B como pool hibrido: conservar fuentes normativas/lexicales para trazabilidad y respaldo, pero incorporar recuperacion historica como fuente prioritaria o de alto peso.

Esta conclusion debe leerse con cautela: el leave-one-out usa el evalset como banco inicial de casos historicos, por lo que mide potencial de similitud entre precedentes dentro del mismo universo, no desempeno final sobre casos futuros. Los 54 casos fuera de Top-100 corresponden a NANDINA8 con una sola instancia en el evalset, sin precedente interno de la misma etiqueta. Para fortalecer la validez externa, Fase 9B deberia incorporar historicos reales adicionales, particiones temporales o validacion sobre un lote posterior no usado como banco.

## Politica de ejecucion

No se uso LLM, Ollama, OpenAI ni APIs remotas. La fase se ejecuto con codigo local deterministico sobre archivos locales del repositorio.
