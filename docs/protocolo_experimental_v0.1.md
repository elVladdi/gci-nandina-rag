# Protocolo experimental v0.1

Este documento congela el protocolo experimental inicial del piloto offline LLM+RAG NANDINA. La version v0.1 define insumos, componentes y metricas previstas, pero no reporta ni interpreta resultados como validacion final.

## Componentes incluidos

- Configuracion metodologica oficial: `src/configs/experiment_v0.1.json`.
- Configuracion operativa vigente: `src/configs/experiment_config.json`.
- Corpus oficial indexable: `data/processed/corpus_rag_v1_index.jsonl`.
- Devset piloto actual: `data/processed/devset_validacion_intermedia.csv`.
- Indice BM25 oficial: `data/processed/indexes/bm25_nandina8.pkl`.
- Metadatos del indice BM25: `data/processed/indexes/bm25_nandina8_run_metadata.json`.
- Corridas preliminares BM25 + LLM rewrite, si se analizan, ubicadas en `data/processed/runs/bm25_2pass_llm_*`.


## Fuente operativa data_aduanas

La Fase 2 incorpora `data_aduanas` como fuente operativa normalizada para trazabilidad metodologica. La fuente local fisica es `data/Series - Descripciones.xlsx`; su nombre metodologico dentro del protocolo es `data_aduanas`.

La capa normalizada/intermedia se genera con `src/ingestion/sunat_series_parser.py` y queda documentada como artefacto regenerable en:

- `data/interim/sunat_series_descripciones_normalized.csv`.
- `data/interim/sunat_series_descripciones_normalized.xlsx`.
- `data/interim/sunat_series_descripciones_normalized_metadata.json`.
- `outputs/audits/sunat_series_labels_v0.1/labels.csv`.
- `outputs/audits/sunat_series_labels_v0.1/id_unico_duplicates.csv`.

La fuente servira para construir posteriormente tres particiones homogeneas: historico, desarrollo y evaluacion. El alcance operativo proyectado sera `Clase = 87`; la ultima normalizacion disponible registra 4,232 instancias de esa clase y 69 NANDINAS distintas.

Las particiones finales deberan conservar las mismas columnas, no mezclar esquemas entre historico/dev/eval y no contener `id_unico` repetidos. La normalizacion actual reporto 107 DAM detectadas, 11,320 series normalizadas, 11,320 filas con `id_unico` y 81 filas con advertencias de parseo.

Esta incorporacion actualiza la trazabilidad de Fase 2. No reemplaza todavia el evalset v0.1 de Fase 3 ni autoriza cambiar `data/processed/evalset_v0.1.csv`, `data/processed/devset_validacion_intermedia.csv` o el historico experimental.

## Baseline

El baseline de v0.1 es BM25 como recuperador documental sobre documentos NANDINA-8. Sus parametros quedan fijos en la configuracion oficial:

- `k1`: 1.5.
- `b`: 0.75.
- uso de stopwords: activo.
- valores Top-K evaluables: 1, 3, 5 y 10.

El baseline debe usarse para medir recuperacion documental antes de interpretar cualquier variante LLM+RAG.

## Variante experimental preliminar

BM25 + LLM rewrite se considera una variante experimental preliminar cuando usa las corridas existentes en `data/processed/runs/bm25_2pass_llm_*`. Su funcion es explorar si la reescritura local de consultas mejora la recuperacion documental.

Esta variante no constituye validacion final. Cualquier comparacion debe declarar la corrida, configuracion, modelo local, temperatura, fecha y artefactos usados.

## Artefacto exploratorio candidato

Text2Trade/dense retrieval queda documentado como artefacto exploratorio o componente candidato, no como componente formal de v0.1. Los artefactos existentes son:

- `data/processed/indexes/text2trade_nandina8_v1/retrieval_config.json`.
- `data/processed/indexes/text2trade_nandina8_v1/text2trade_nandina8_run_metadata.json`.

No debe tratarse como parte del protocolo oficial hasta contar con criterio metodologico y comparacion reproducible suficientes.

## Metricas previstas

Metricas cuantitativas de recuperacion:

- Top-1.
- Top-3.
- Top-5.
- Top-10.
- MRR.
- nDCG.

Criterios cualitativos previstos para salidas LLM+RAG:

- Verificabilidad.
- Trazabilidad.
- Pertinencia documental.
- Concordancia entre evidencia y justificacion.
- Claridad para auditoria.

## Fuera de alcance en v0.1

- Ampliar el dataset.
- Ejecutar experimentos largos.
- Mover o versionar modelos pesados nuevos.
- Declarar clasificacion oficial de mercancias.
- Usar el sistema con fines productivos.
- Ajustar parametros segun resultados.
- Confirmar hipotesis de investigacion.

## Politica de interpretacion

Los resultados generados bajo v0.1 deben interpretarse como evidencia preliminar del piloto offline. No deben presentarse como validacion final, ni como sustituto de revision experta o decision oficial de clasificacion arancelaria.

Si se modifica el corpus, dataset, indice, parametros BM25, configuracion LLM o politica de evaluacion, debe crearse una nueva version del protocolo y de la configuracion experimental.
