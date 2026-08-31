# Piloto offline LLM+RAG para recomendacion auditable de subpartidas NANDINA

Repositorio de investigacion aplicada para evaluar un piloto offline de recomendacion auditable de subpartidas NANDINA. El sistema no emite clasificacion oficial ni reemplaza el criterio de un especialista; produce candidatos, evidencias y explicaciones trazables para apoyar revision humana.

El alcance experimental actual se mantiene en `data_aduanas`, `Clase = 87`, con ejecucion offline y control de reproducibilidad por artefactos versionados.

![Framework RAG explicativo y auditable](data/Framework%20RAG.png)

## Estado Actual

**Grupo 1 — Diseño y ejecución experimental: CLOSED / APPROVED.** El benchmark final es `v0.2`, `DAM_GROUPED_FINAL_SPLIT`; `v0.1` queda solo como referencia histórica de sensibilidad, no como benchmark final.

| Tarjeta | Estado |
|---|---|
| EXP-01 | CLOSED |
| EXP-02 | CLOSED |
| EXP-03 | CLOSED |
| EXP-04 | CLOSED |
| EXP-05 | CLOSED |
| EXP-06 | CLOSED |
| EXP-07 | CLOSED |
| EXP-08 | CLOSED |
| EXP-09 | CLOSED |
| EXP-10 | CLOSED |

## Arquitectura Metodológica

- **Historical retrieval:** ranking principal de candidatos.
- **Normative retrieval:** evidencia documental; no reemplaza el ranking histórico.
- **Fixed Top-3:** entrada cerrada del explicador.
- **Local LLM:** explicación controlada sobre ese contexto; no clasifica NANDINA desde cero.
- **Diagnostic reranker:** diagnóstico solamente, sin reclamo de benchmark.

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

## Resumen de Resultados Congelados

| Componente | Métricas compactas |
|---|---|
| Historical BM25 v0.2 (`n=1056`) | Top1 `0.509470`; Top3 `0.671402`; Top5 `0.763258`; Top10 `0.891098`; Top50 `0.991477`; MRR `0.629708` |
| Normative flat | Top1 `0.027462`; Recall@100 `0.071023`; MRR@100 `0.042297` |
| Normative hierarchical | Top1 `0.026515`; Recall@100 `0.101326`; Recall@200 `0.303977` |
| D1a Text2Trade-inspired MNRL | Top1 `0/1056`; Top3 `4/1056`; Top5 `36/1056`; Top10 `165/1056`; Top50 `323/1056`; Recall@100 `365/1056`; MRR@100 `0.032424326`; Recall@200 `383/1056`; MRR@200 `0.032548535` |

La fuente D1a final es [`d1a_metrics.json`](outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json), SHA-256 `620412bc15dbba2edd4e2d195457f0b8b4ce670cd75ff7c6d87835a435b8fb3c`. No se usan métricas del baseline D0 legacy como D1a.

## Integración y Auditorías LLM

- **F:** 1056 casos, 3168 slots Top-3; se preservó el ranking histórico y hubo evidencia normativa exacta en `3168/3168` slots.
- **G:** 20 casos diagnósticos: `0` win, `19` tie, `0` loss y `1` reference absent.
- **HE4:** 50 casos, `28/50` auditables, `PARTIALLY_SUPPORTED`.
- `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` y `EVALUATOR_MODALITY_DEVIATION` permanecen como limitaciones.

## Hipótesis

| Hipótesis | Estado final |
|---|---|
| HE2 | PARTIALLY_SUPPORTED |
| HE3 | SUPPORTED |
| HE4 | PARTIALLY_SUPPORTED |
| HE5 | PARTIALLY_SUPPORTED |

## Sensibilidad EXP-08

v0.1 Top1 `0.862823` frente a v0.2 Top1 `0.509470` (delta `-35.335 pp`); v0.1 MRR `0.906239` frente a v0.2 MRR `0.629708`. Es sensibilidad al diseño/configuración experimental, no una degradación causal de BM25.

## Limitaciones Conocidas v0.2

- Concentración DAM y duplicados residuales.
- Debilidad de los early rankings normativo y denso.
- Tamaños diagnósticos de G y HE4.
- `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` y `EVALUATOR_MODALITY_DEVIATION`.
- Calidad de descripción no operacionalizada, limitación de provenance v0.1 y alcance interno de Clase 87.

Las 13 limitaciones preservadas y su tratamiento están en [exp04_consolidated_limitations_v0.2.csv](outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_consolidated_limitations_v0.2.csv).

## Documentacion Relacionada

- [Protocolo data_aduanas Clase 87 v0.2](docs/protocolo_data_aduanas_clase87_v0.2.md)
- [Ficha dataset data_aduanas Clase 87 v0.2](docs/ficha_data_aduanas_clase87_v0.2.md)
- [Manifiesto de artefactos v0.2](docs/manifiesto_artefactos_v0.2.md)
- [Cierre consolidado EXP-04 / Grupo 1](docs/exp04_group1_consolidated_closure_inventory.md)
- [Gate consolidado](outputs/evaluation/exp04_consolidated_closure_v0.2/gate_exp04_consolidated_closure_manifest_v0.2.json)
- [Gate correctivo de procedencia](outputs/evaluation/exp04_consolidated_closure_v0.2/gate_exp04_consolidated_corrective_microclose_manifest_v0.2.json)
- [Registro final de resultados](outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_results_registry_v0.2.csv)
- [Registro final de procedencia](outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_provenance_registry_v0.2.csv)

## Comandos Utiles

Tests:

```powershell
python -m unittest discover -s tests -v
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
