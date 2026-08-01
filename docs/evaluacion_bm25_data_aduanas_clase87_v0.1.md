# Evaluacion BM25 data_aduanas clase 87 v0.1

## Objetivo

Evaluar el baseline BM25 normativo plano sobre el nuevo evalset `data_aduanas` de Clase = 87, sin reemplazar ni reinterpretar la evaluacion BM25 v0.1 historica de 600 casos.

## Insumos

- Fuente metodologica: `data_aduanas`.
- Alcance: Clase = `87`.
- Evalset: `data/processed/data_aduanas_evalset_clase87_v0.1.csv`.
- Filas evaluadas: 1006.
- Columna de consulta: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta esperada: `NANDINA`.
- Indice BM25 normativo: `data/processed/indexes/bm25_nandina8.pkl`.
- Profundidad de recuperacion: 100.

## Metricas exactas

| Metrica | Valor |
| --- | ---: |
| Casos evaluados | 1006 |
| Casos con recuperacion | 997 |
| Top-1 NANDINA8 | 0.0229 |
| Top-3 NANDINA8 | 0.0338 |
| Top-5 NANDINA8 | 0.0398 |
| Top-10 NANDINA8 | 0.0467 |
| MRR | 0.0312 |
| Recall@50 | 0.0616 |
| Recall@100 | 0.0626 |

## Metricas jerarquicas

| Corte | Partida HS4 | Sub Partida HS6 | Clase HS2 |
| --- | ---: | ---: | ---: |
| Top-10 | 0.0755 | 0.0537 | 0.6829 |
| Top-50 | 0.1183 | 0.0716 | 0.8797 |
| Top-100 | 0.1252 | 0.0755 | 0.8887 |

## Lectura metodologica

BM25 normativo se conserva como baseline lexical de referencia. En este evalset de descripciones comerciales clase 87, el desempeno exacto NANDINA8 es bajo frente a la profundidad amplia de recuperacion. La brecha entre aciertos exactos y aciertos jerarquicos muestra que el indice normativo puede acercarse a familias arancelarias, pero no debe tratarse como recuperacion historica principal.

## Comparabilidad con Fase 4 anterior

La Fase 4 historica v0.1 evaluo BM25 sobre `data/processed/evalset_v0.1.csv` con 600 casos de otra fuente y alcance. Esta actualizacion evalua `data_aduanas` Clase = 87 con otro tamano, fuente y distribucion. Las metricas no son una comparacion pareada ni deben leerse como mejora o degradacion sobre el mismo conjunto; sirven para contrastar dos baselines de alcance distinto.

## Decision

BM25 normativo sirve como baseline auditable de referencia para fases futuras sobre `data_aduanas`, pero no como recuperacion historica principal. Para pipelines posteriores, lo normativo debe operar como respaldo/trazabilidad y comparador minimo, mientras la recuperacion historica clase 87 debe evaluarse por separado contra su propio banco historico.

## Controles

- No se ejecuto LLM.
- No se ejecuto Text2Trade.
- No se modifico el evalset historico v0.1 ni los splits de Fase 3.
- Los outputs bajo `outputs/` son regenerables e ignorados por Git.

## Advertencias

- Casos sin resultados recuperados: 9.
