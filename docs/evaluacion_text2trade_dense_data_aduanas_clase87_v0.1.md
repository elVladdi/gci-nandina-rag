# Evaluacion Text2Trade dense data_aduanas clase 87 v0.1

## Objetivo

Actualizar Fase 5 repitiendo la comparacion Dense Text2Trade vs BM25 sobre el nuevo evalset `data_aduanas` de Clase = 87. Esta corrida no reemplaza ni reinterpreta la Fase 5 historica sobre `data/processed/evalset_v0.1.csv` de 600 casos; queda como una evaluacion separada por fuente, alcance y tamano.

## Fuente y alcance

- Fuente metodologica: `data_aduanas`.
- Alcance: `Clase = 87`.
- Evalset usado: `data/processed/data_aduanas_evalset_clase87_v0.1.csv`.
- Tamano del evalset: 1,006 casos.
- Columna de consulta: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta esperada: `NANDINA`.

Las etiquetas esperadas fueron validadas como codigos NANDINA8 y no se encontraron consultas vacias.

## Artefacto dense usado

La evaluacion usa artefactos Text2Trade locales existentes:

```text
data/processed/indexes/text2trade_nandina8_v1/
```

Componentes cargados:

- `index/vectors.npy`
- `index/id_map.json`
- `store/nandina8_docstore.jsonl`
- `model/`
- `retrieval_config.json`
- `text2trade_nandina8_run_metadata.json`

El artefacto contiene 7,644 documentos vectorizados y embeddings de dimension 384.

## Fuerza bruta vs HNSW

El archivo `data/processed/indexes/text2trade_nandina8_v1/index/hnsw.index` no existe en el checkout local. Siguiendo la restriccion de no reconstruir HNSW, la evaluacion uso fuerza bruta sobre `vectors.npy`: se codificaron las consultas con el modelo SentenceTransformer local, se calculo producto punto/coseno contra todos los vectores y se ordenaron candidatos a profundidad 100.

No se ejecuto LLM, no se ejecuto Ollama y no se usaron APIs remotas.

## Outputs regenerables

Los outputs se generaron en:

```text
outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/
```

Archivos:

- `results.csv`
- `metrics.json`
- `summary.md`
- `failure_sample.csv`
- `comparison_bm25_dense_data_aduanas.json`
- `comparison_bm25_dense_data_aduanas.md`
- `case_comparison.csv`

Estos outputs son regenerables y permanecen ignorados por Git.

## Metricas Dense

| Metrica | Valor |
| --- | ---: |
| Casos evaluados | 1,006 |
| Top-1 NANDINA8 | 0.0000 |
| Top-3 NANDINA8 | 0.0000 |
| Top-5 NANDINA8 | 0.0000 |
| Top-10 NANDINA8 | 0.0000 |
| MRR | 0.0000 |
| Recall@50 | 0.0010 |
| Recall@100 | 0.0010 |

Metricas jerarquicas:

| Corte | Partida HS4 | Sub Partida HS6 | Clase HS2 |
| --- | ---: | ---: | ---: |
| Top-10 | 0.0109 | 0.0000 | 0.1889 |
| Top-50 | 0.0736 | 0.0119 | 0.7475 |
| Top-100 | 0.2028 | 0.0288 | 0.8618 |

## Comparacion contra BM25 Fase 4 actualizada

| Metrica | BM25 | Dense | Delta dense-BM25 |
| --- | ---: | ---: | ---: |
| Top-1 NANDINA8 | 0.0229 | 0.0000 | -0.0229 |
| Top-10 NANDINA8 | 0.0467 | 0.0000 | -0.0467 |
| MRR | 0.0312 | 0.0000 | -0.0312 |
| Recall@100 | 0.0626 | 0.0010 | -0.0616 |
| Partida@100 | 0.1252 | 0.2028 | +0.0775 |
| Sub Partida@100 | 0.0755 | 0.0288 | -0.0467 |
| Clase@100 | 0.8887 | 0.8618 | -0.0268 |

Casos Top-10:

- Ganados por dense: 0.
- Perdidos por dense: 47.
- Ambos recuperan: 0.
- Ambos fallan: 959.

## Lectura metodologica

Dense Text2Trade no aporta frente a BM25 para recuperacion exacta NANDINA8 en este evalset clase 87. La unica mejora observada es jerarquica a nivel Partida@100, pero ocurre junto con perdida fuerte en exactitud, Sub Partida@100 y Clase@100. Por tanto, no justifica promover dense como recuperador principal ni como sustituto del BM25 normativo para esta actualizacion.

El resultado sugiere desalineacion entre las descripciones comerciales `data_aduanas` clase 87 y el espacio semantico del artefacto dense disponible. Para fases posteriores, dense podria conservarse solo como diagnostico o fuente auxiliar exploratoria si se disena una regla explicita que aproveche familias amplias sin degradar exactitud.

## Decision

Para el nuevo evalset `data_aduanas` clase 87, Dense Text2Trade por fuerza bruta no aporta frente a BM25 como baseline de recuperacion exacta. BM25 normativo queda como comparador auditable de Fase 4 actualizada; dense se mantiene como artefacto previo/exploratorio y no se adopta como componente activo.

## Comparabilidad con Fase 5 historica

La Fase 5 historica evaluo Text2Trade dense sobre `data/processed/evalset_v0.1.csv` con 600 casos. Esta actualizacion evalua `data_aduanas` Clase = 87 con 1,006 casos, otra fuente y otra distribucion. Las metricas no son una comparacion pareada con la corrida historica y no deben leerse como mejora o degradacion del mismo experimento.
