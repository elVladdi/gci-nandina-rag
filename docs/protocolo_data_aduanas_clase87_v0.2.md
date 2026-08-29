# Protocolo data Aduanas Clase 87 v0.2

## Alcance

Este protocolo documenta la reconstruccion de las particiones del dataset Aduanas Clase 87 para la version v0.2, implementando las fichas EXP-01, EXP-02 y EXP-03. La version aprobada es T5-safe-159 y queda congelada como decision metodologica.

La unidad de analisis sigue siendo la SERIE. La independencia experimental se garantiza agrupando por DECLARACION / DAM: una DAM completa pertenece a una sola particion.

## Entradas preservadas

Los artefactos v0.1 son evidencia historica y no se sobrescriben. Antes de generar v0.2, el script verifica estos SHA-256:

- data/processed/data_aduanas_historico_clase87_v0.1.csv: ea3286063fc890d2569a8cd3704ab18d82970e3b41973153957e27486c28f2f0
- data/processed/data_aduanas_devset_clase87_v0.1.csv: 19eeb607cb1586f3eb459a95d267844bcb068daf93f05e4055ce1183dd698a50
- data/processed/data_aduanas_evalset_clase87_v0.1.csv: ae642d01c0e941ab94a187fb2a820fbc8dcd6259c90d9decb70408b9dea344bb
- data/processed/data_aduanas_splits_clase87_v0.1_metadata.json: 71a42f793ae7e7cb02ec5b97723c74ac7b60d67f9f7b542ebfa43bb77834189a

## Configuracion congelada

La configuracion reproducible esta en:

- src/configs/data_aduanas_split_clase87_v0.2.json

Contiene version, estrategia, semilla 2026, campo de agrupamiento, unidad de analisis, clase elegible, rangos/targets y listas explicitas de DAM por particion. El generador no vuelve a ejecutar una busqueda Pareto ni optimiza candidatos.

## Generacion

Comando canonico:

```powershell
& "C:\Users\Vladimir\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" src\evaluation\group_split_by_dam.py --overwrite
```

El script produce:

- data/processed/data_aduanas_historico_clase87_v0.2.csv
- data/processed/data_aduanas_devset_clase87_v0.2.csv
- data/processed/data_aduanas_evalset_clase87_v0.2.csv
- data/processed/data_aduanas_splits_clase87_v0.2_metadata.json

## Composicion aprobada

| particion | series | DAM | codigos NANDINA |
|---|---:|---:|---:|
| historico | 2950 | 28 | 66 |
| desarrollo | 100 | 6 | 9 |
| evaluacion | 1056 | 67 | 42 |

## Reglas de auditoria

El generador valida y deja artefactos en outputs/audits/data_aduanas_splits_clase87_v0.2/:

- independencia por DAM e id_unico;
- concentracion por DAM e HHI;
- soporte historico nominal para codigos de evaluacion;
- duplicados exactos por descripcion normalizada entre particiones;
- near-duplicates historico-evaluacion con token_jaccard_rare_block en umbrales 0.90, 0.95 y 0.98.

La normalizacion de descripciones aplica nulos, trim, espacios normalizados, Unicode NFC y casefold. El algoritmo de near-duplicates usa tokens de longitud minima 3 y bloqueo por tokens raros con df <= max(20, int(n_historico * 0.25)).

## Resultado Gate 5

Gate 5 queda aprobado para el split v0.2:

- 4106 series elegibles asignadas exactamente una vez;
- 0 DAM compartidas entre particiones;
- 0 id_unico compartidos entre particiones;
- 1056/1056 casos de evaluacion con soporte historico nominal;
- concentracion maxima DAM en evaluacion = 14.109848484848486%, menor o igual a 15%;
- duplicados exactos historico-evaluacion documentados: 35 filas afectadas, 34 misma NANDINA, 1 NANDINA distinta;
- near-duplicates historico-evaluacion documentados: 55 filas a 0.90, 44 a 0.95, 37 a 0.98.

## Restricciones

Esta etapa no ejecuta BM25 final, Text2Trade final, candidate pools finales, RAG, reranking LLM ni explicador LLM. Las metricas de modelo no intervienen en la seleccion del split.
