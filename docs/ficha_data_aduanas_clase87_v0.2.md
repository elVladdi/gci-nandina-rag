# Ficha dataset Aduanas Clase 87 v0.2

## Identificacion

- Nombre: data_aduanas_clase87
- Version: v0.2
- Estrategia: T5-safe-159
- Semilla: 2026
- Unidad de analisis: SERIE
- Agrupamiento experimental: DECLARACION / DAM
- Clase elegible: NANDINA que inicia en 87

## Proposito

La version v0.2 corrige la fuga estructural por DAM detectada en v0.1. El objetivo es disponer de particiones independientes a nivel de declaracion, manteniendo compatibilidad de columnas con la pipeline posterior y preservando los artefactos v0.1 como evidencia historica.

## Particiones

| particion | archivo | series | DAM | codigos |
|---|---|---:|---:|---:|
| historico | data/processed/data_aduanas_historico_clase87_v0.2.csv | 2950 | 28 | 66 |
| desarrollo | data/processed/data_aduanas_devset_clase87_v0.2.csv | 100 | 6 | 9 |
| evaluacion | data/processed/data_aduanas_evalset_clase87_v0.2.csv | 1056 | 67 | 42 |

## Campos principales

La estructura conserva las columnas de v0.1. Entre los campos usados por la pipeline y las auditorias estan:

- case_id
- id_unico
- split
- DECLARACION
- SERIE
- NANDINA
- DESCRIPCION DE MERCANCIAS CONCATENADA

Los case_id fueron regenerados con prefijos v0.2 por particion: DA-HIST-V02, DA-DEV-V02 y DA-EVAL-V02.

## Calidad y controles

- Asignacion completa: 4106/4106 series.
- Unicidad: 4106 id_unico distintos.
- Independencia por DAM: 0 solapamientos.
- Independencia por id_unico: 0 solapamientos.
- Soporte historico de evaluacion: 1056/1056 casos.
- Concentracion maxima DAM en evaluacion: 14.109848484848486%.

## Soporte historico de evaluacion

| bucket | codigos | casos |
|---|---:|---:|
| A. 1 DAM historica | 7 | 27 |
| B. 2 DAM historicas | 2 | 21 |
| C. 3-4 DAM historicas | 18 | 425 |
| D. 5+ DAM historicas | 15 | 583 |

## Duplicados y near-duplicates

Los duplicados no se eliminan automaticamente; se documentan para auditoria metodologica.

- Duplicados exactos historico-evaluacion: 35 filas de evaluacion afectadas.
- De esas filas, 34 comparten NANDINA y 1 presenta NANDINA distinta.
- Near-duplicates historico-evaluacion: 55 filas afectadas a 0.90, 44 a 0.95 y 37 a 0.98.

## Reproducibilidad

La version se reproduce con:

- src/configs/data_aduanas_split_clase87_v0.2.json
- src/evaluation/group_split_by_dam.py
- tests/test_data_aduanas_split_v02.py
- docs/manifest_artifacts_v0.2.json

Los hashes SHA-256 de datasets, metadata, auditorias, configuracion, script y documentos estan registrados en el manifest v0.2.

## Usos permitidos

Esta version queda lista como base de evaluacion posterior, una vez autorizadas las fases siguientes. La tarea actual no ejecuta BM25 final, Text2Trade final, RAG, reranking LLM ni explicador LLM.
