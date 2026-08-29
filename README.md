# Piloto offline LLM+RAG para recomendacion auditable de subpartidas NANDINA

Repositorio de investigacion aplicada para evaluar un piloto offline de recomendacion auditable de subpartidas NANDINA. El sistema no emite clasificacion oficial ni reemplaza el criterio de un especialista; produce candidatos, evidencias y explicaciones trazables para apoyar revision humana.

El alcance experimental actual se mantiene en `data_aduanas`, `Clase = 87`, con ejecucion offline y control de reproducibilidad por artefactos versionados.

![Framework RAG explicativo y auditable](data/Framework%20RAG.png)

## Estado Actual

El piloto v0.1 queda preservado como referencia historica. La linea vigente para nuevas evaluaciones es el split `data_aduanas` Clase 87 `v0.2`, estrategia `T5-safe-159`, construido con independencia por `DECLARACION` / DAM.

| Version | Estado | Uso |
|---|---|---|
| v0.1 | Cerrada y preservada | Referencia historica; no sobrescribir outputs ni splits |
| v0.2 | Gate 5 cerrado | Base oficial para reruns experimentales posteriores |
| EXP-04 Fase A | Gate A aprobado | BM25 historico sobre split v0.2 completado |

## Dataset v0.2

La unidad de analisis es la `SERIE`. La unidad de agrupamiento experimental es `DECLARACION` / DAM: una DAM completa pertenece a una sola particion.

| Particion | Series | DAM | Codigos NANDINA |
|---|---:|---:|---:|
| Historico | 2950 | 28 | 66 |
| Desarrollo | 100 | 6 | 9 |
| Evaluacion | 1056 | 67 | 42 |

Controles aprobados:

- 4106 series asignadas exactamente una vez.
- 0 DAM compartidas entre particiones.
- 0 `id_unico` compartidos entre particiones.
- 1056/1056 casos de evaluacion con soporte historico nominal.
- Los artefactos v0.1 se conservan como evidencia historica y no deben sobrescribirse.

Hashes SHA-256 congelados:

| Split | Ruta | SHA-256 |
|---|---|---|
| Historico | `data/processed/data_aduanas_historico_clase87_v0.2.csv` | `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff` |
| Desarrollo | `data/processed/data_aduanas_devset_clase87_v0.2.csv` | `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00` |
| Evaluacion | `data/processed/data_aduanas_evalset_clase87_v0.2.csv` | `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941` |

Reproducibilidad del split:

- Configuracion: `src/configs/data_aduanas_split_clase87_v0.2.json`.
- Generador: `src/evaluation/group_split_by_dam.py`.
- Tests: `tests/test_data_aduanas_split_v02.py`.
- `.gitattributes` fuerza LF para CSV experimentales v0.2 y resultados EXP-04 v0.2 para preservar hashes reproducibles en Windows/Linux.

## Hallazgo de Independencia Experimental

El split v0.1 fue util para cerrar el piloto inicial, pero tenia dependencia estructural por DAM:

| Control | v0.1 | v0.2 |
|---|---:|---:|
| Casos de evaluacion cuya DAM aparecia en historico | 995/1006 | 0/1056 |
| Casos con descripcion exacta presente en historico | 377/1006 | 35/1056 |

La diferencia documenta una mejora del control de independencia experimental. No implica cambio del algoritmo BM25 ni debe interpretarse como evidencia causal mas alla del cambio de politica de particion.

## Experimental Status

| Phase | Status |
|---|---|
| EXP-01 DAM-grouped split | Complete |
| EXP-02 Cross-split duplicate audit | Complete |
| EXP-03 Balanced split design | Complete |
| Gate 5 | Closed |
| EXP-04 A Historical BM25 v0.2 | Complete |
| EXP-04 B Flat normative BM25 | Pending |
| EXP-04 C Hierarchical normative BM25 | Pending |
| Text2Trade / dense comparator | Pending |
| Candidate pools v0.2 | Pending |
| Diagnostic LLM reranker | Pending |
| Top-3 explainer v0.2 | Pending |
| Integrated error analysis | Pending |

### EXP-04 Fase A - Historical BM25 v0.2

BM25 historico v0.2 esta completado y Gate A esta aprobado. La consulta usa exclusivamente `DESCRIPCION DE MERCANCIAS CONCATENADA`; no usa etiqueta, DAM, SERIE, BM25 normativo, Text2Trade, RAG, reranking LLM ni explicador LLM.

| Metrica | Valor |
|---|---:|
| Casos | 1056 |
| Top-1 | 0.5095 |
| Top-3 | 0.6714 |
| Top-5 | 0.7633 |
| Top-10 | 0.8911 |
| Top-50 | 0.9915 |
| MRR | 0.6297 |

Los valores completos, numeradores, denominadores y hashes de outputs estan en `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json` y `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/run_metadata.json`.

### Comparacion Descriptiva v0.1 vs v0.2

| Metric | v0.1 | v0.2 |
|---|---:|---:|
| Top-1 | 0.8628 | 0.5095 |
| Top-3 | 0.9374 | 0.6714 |
| Top-5 | 0.9592 | 0.7633 |
| Top-10 | 0.9801 | 0.8911 |
| Top-50 | 1.0000 | 0.9915 |
| MRR | 0.9062 | 0.6297 |

La diferencia no representa un cambio del algoritmo BM25. Representa sensibilidad al cambio desde el split v0.1 por serie hacia el split v0.2 independiente por DAM.

## Limitaciones Conocidas v0.2

- Historico concentrado en pocas DAM: DAM mayor = 35.42%; Top-2 DAM aprox. 67.29%; HHI = 0.2361.
- Devset reducido y concentrado: 100 series, 6 DAM, 9 codigos, DAM dominante = 91%.
- Duplicados exactos historico-evaluacion: 35 casos.
- Near-duplicates historico-evaluacion >= 0.95: 44 casos.
- Estos casos se conservan para analisis de sensibilidad bajo HE5; no se eliminan del benchmark v0.2.

## Documentacion Relacionada

- [Protocolo data_aduanas Clase 87 v0.2](docs/protocolo_data_aduanas_clase87_v0.2.md)
- [Ficha dataset data_aduanas Clase 87 v0.2](docs/ficha_data_aduanas_clase87_v0.2.md)
- [Manifiesto de artefactos v0.2](docs/manifiesto_artefactos_v0.2.md)
- [Inventario EXP-04 Fase A BM25 historico v0.2](docs/exp04_bm25_historico_v02_inventory.md)
- [Resumen BM25 historico v0.2](outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_summary.md)

## Comandos Utiles

Tests:

```powershell
python -m unittest discover -s tests -v
```

Generacion split v0.2:

```powershell
python src/evaluation/group_split_by_dam.py --overwrite
```

BM25 historico v0.2:

```powershell
python -m src.experiments.evaluate_historical_retrieval_data_aduanas_v02 --history-depth 2950 --candidate-depth 100
```

## Estructura del Repositorio

```text
.
|-- data/
|   |-- interim/        # tablas intermedias regenerables
|   |-- processed/      # splits, corpus e indices versionados o regenerables
|   |-- raw/            # insumos locales, cuando aplica
|   `-- Framework RAG.png
|-- docs/               # protocolos, fichas, manifiestos y trazabilidad
|-- outputs/            # resultados regenerables; algunos artefactos aprobados se versionan explicitamente
|-- src/
|   |-- analysis/
|   |-- corpus/
|   |-- evaluation/
|   |-- experiments/
|   |-- ingestion/
|   |-- llm/
|   |-- retrieval/
|   `-- bm25_index.py
|-- tests/
|-- requirements.txt
`-- README.md
```

## Politica de Uso

Versionar en Git: codigo, configuraciones, protocolos, manifiestos, tests, metadata y artefactos aprobados necesarios para reproducibilidad.

No versionar por defecto: `.venv/`, `data/interim/`, `data/raw/`, `data/Series - Descripciones.xlsx`, `Referencias/`, credenciales ni salidas regenerables no aprobadas.

La salida del piloto es una recomendacion auditable para revision humana, no una declaracion aduanera ni una decision vinculante.
