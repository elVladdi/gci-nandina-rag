# Evaluación multi-query + RRF devset v0.1

## Objetivo de la fase 6A1-1

Implementar y evaluar una estrategia multi-query con fusión Reciprocal Rank Fusion (RRF) para mejorar el ranking inicial sobre el devset preliminar de 13 casos, sin reemplazar la descripción original ni ejecutar nada sobre el evalset final.

La consulta Q0 se copia siempre desde `data/processed/devset_validacion_intermedia.csv` y no se genera con LLM. El LLM solo genera variantes complementarias Q1, Q2 y Q3.

## Cambio de estrategia frente a rewrite v0.1/v0.2

Las iteraciones anteriores reemplazaban la descripción original por una consulta reescrita. Ese enfoque no superó de forma consistente al BM25 original: perdió atributos discriminantes en algunos casos y degradó Top-1/MRR.

Esta fase cambia el enfoque: conserva Q0 y agrega consultas complementarias. El objetivo no es elegir una única reescritura, sino combinar evidencia de varias formulaciones mediante RRF.

## RRF

RRF suma una contribución `1 / (rrf_k + rank)` por cada candidato recuperado en cada fuente. En esta corrida se usó `rrf_k=60` y profundidad 100 por consulta. Un candidato puede recibir aportes de `BM25_Q0`, `BM25_Q1`, `BM25_Q2` y `BM25_Q3`; esas fuentes quedan registradas en los CSV de trazabilidad.

## Modelo, prompt y runtime

- Modelo LLM: `qwen2.5:7b-instruct` vía Ollama local.
- Endpoint: `http://127.0.0.1:11434/api/chat`.
- Prompt: `src/llm/multiquery_prompt_v0.1.md`.
- Formato esperado: JSON estricto con `q1_limpia`, `q2_expandida`, `q3_terminos_clave` y `advertencias`.
- Python usado: runtime bundled de Codex `C:/Users/Vladimir/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe` (Python 3.12.13).
- La `.venv` del proyecto no pudo ejecutarse porque apunta a un Python local inexistente. Se intentó reutilizar sus paquetes con `PYTHONPATH`, pero NumPy falló por incompatibilidad binaria con Python 3.12.

## Outputs generados

- `outputs/evaluation/multiquery_rrf_devset_v0.1/multiqueries.jsonl`
- `outputs/evaluation/multiquery_rrf_devset_v0.1/multiqueries.csv`
- `outputs/evaluation/multiquery_rrf_devset_v0.1/metadata.json`
- `outputs/evaluation/multiquery_rrf_devset_v0.1/summary.md`
- `outputs/evaluation/multiquery_rrf_devset_v0.1/rrf_results.csv`
- `outputs/evaluation/multiquery_rrf_devset_v0.1/rrf_metrics.json`
- `outputs/evaluation/multiquery_rrf_devset_v0.1/rrf_summary.md`
- `outputs/evaluation/multiquery_rrf_devset_v0.1/rrf_case_comparison_13_cases.csv`

## Text2Trade

Text2Trade no pudo ejecutarse con el runtime disponible. Los artefactos locales existen, pero la carga falló inicialmente por `ModuleNotFoundError: No module named 'sentence_transformers'`. El intento de reutilizar paquetes de `.venv` falló por incompatibilidad de extensiones NumPy. Por ello, la evaluación final reportada es BM25 + RRF.

## Trazabilidad de iteraciones previas

| Variante | Top-1 | Top-3 | Top-5 | Top-10 | MRR |
|---|---:|---:|---:|---:|---:|
| BM25 original devset | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4370 |
| Rewrite v0.1 | 0.3077 | 0.4615 | 0.4615 | 0.4615 | 0.3755 |
| Rewrite v0.2 | 0.3077 | 0.4615 | 0.5385 | 0.5385 | 0.3908 |

## Métricas comparativas de esta fase

| Método | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Top-10 HS4 | Top-10 HS2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| BM25_Q0_baseline | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4370 | 0.8462 | 0.8462 |
| BM25_multiquery_RRF | 0.3846 | 0.4615 | 0.4615 | 0.4615 | 0.4296 | 0.8462 | 0.8462 |
| Text2Trade_multiquery_RRF | No disponible | No disponible | No disponible | No disponible | No disponible | No disponible | No disponible |
| Hybrid_RRF | No disponible | No disponible | No disponible | No disponible | No disponible | No disponible | No disponible |

Frente a `BM25_Q0_baseline`, `BM25_multiquery_RRF` tuvo 0 casos ganados, 2 perdidos y 11 sin cambio. El mejor método por MRR siguió siendo `BM25_Q0_baseline`; el método RRF final disponible fue `BM25_multiquery_RRF`.

## Tabla de 13 casos

Los textos de esta tabla se normalizan solo para lectura del reporte. Los CSV conservan los valores originales del devset y de las salidas LLM para trazabilidad.

| Caso | NANDINA esperada | Q0 original | Q1 limpia | Q2 expandida | Q3 términos clave | Rank BM25 Q0 | Rank BM25 RRF | Resultado RRF vs BM25 |
|---|---|---|---|---|---|---:|---:|---|
| dev-01 | 84713000 | Máquina automática para tratamiento o procesamiento de datos, portátil, constituida al menos por unidad central, teclado y visualizador integrados; peso menor a 10 kg. | Máquina automática para tratamiento o procesamiento de datos, portátil, constituida al menos por unidad central, teclado y visualizador integrados; peso menor a 10 kg. | Máquina automática para tratamiento o procesamiento de datos, portátil, compuesta al menos por unidad central, teclado y visualizador integrados; peso inferior a 10 kg. | máquina, automática, tratamiento, procesamiento, datos, portátil, unidad central, teclado, visualizador, integrados, peso, menor, 10kg | 1 | 1 | sin_cambio |
| dev-02 | 10063000 | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en sacos para venta mayorista. | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en sacos para venta mayorista. | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en envases de venta mayorista. | arroz semiblanqueado blanqueado pulido glaseado sacos venta mayorista | 1 | 1 | sin_cambio |
| dev-03 | 04029110 | Leche evaporada, sin adición de azúcar ni otros edulcorantes, en latas. | Leche evaporada, sin adición de azúcar ni otros edulcorantes, en latas. | Leche evaporada, sin adición de azúcar ni otros edulcorantes, empaquetada en latas. | leche evaporada, sin azúcar, sin edulcorantes, latas | 2 | 2 | sin_cambio |
| dev-04 | 22030000 | Cerveza de malta, bebida alcohólica en envases de vidrio para consumo. | Cerveza de malta, bebida alcohólica en envases de vidrio para consumo. | Cerveza de malta, bebida alcohólica en recipientes de vidrio para consumo. | cerveza, malta, bebida alcohólica, envases, vidrio, consumo | 1 | 1 | sin_cambio |
| dev-05 | 39012000 | Polietileno de densidad superior o igual a 0,94, en gránulos (pellets) para transformación industrial. | Polietileno de densidad superior a 0,94, en gránulos (pellets) para transformación industrial. | Polietileno de alta densidad (densidad >= 0,94), en gránulos (pellets) destinado a la transformación industrial. | polietileno, densidad, superior, 0,94, gránulos, pellets, transformación, industrial | 1 | 1 | sin_cambio |
| dev-06 | 02013000 | Carne de la especie bovina, fresca o refrigerada, deshuesada, cortes empacados al vacío. | Carne de la especie bovina, fresca o refrigerada, deshuesada, cortes empacados al vacío. | Carne de la especie bovina, fresca o refrigerada, sin huesos, cortes empaquetados en vacío. | carne, especie bovina, fresca, refrigerada, deshuesada, cortes, empacados, al vacío | 8 | 29 | perdido |
| dev-07 | 84713000 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulgadas. | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulgadas. | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulgadas. | computadora portátil procesador Intel Core i5 memoria RAM 8GB disco sólido SSD 512GB pantalla LED 14 pulgadas | 0 | 0 | sin_cambio |
| dev-08 | 84717000 | Disco sólido externo portátil (SSD) de 1 TB, interfaz USB 3.2, usado como unidad de almacenamiento de datos. | Disco sólido externo portátil (SSD) de 1 TB, interfaz USB 3.2, usado como unidad de almacenamiento de datos. | Disco sólido externo portátil (SSD) de 1024 GB, con conexión USB 3.2, utilizado para almacenar datos. | disco sólido externo portátil SSD 1 TB interfaz USB 3.2 unidad de almacenamiento datos | 0 | 0 | sin_cambio |
| dev-09 | 85414100 | Diodos LED SMD para montaje superficial, paquete de 1000 unidades, uso en placas electrónicas e iluminación. | Diodos LED SMD para montaje superficial, paquete de 1000 unidades, uso en placas electrónicas e iluminación. | Diodos LED Surface Mount Device (SMD) para montaje superficial, paquete de 1000 unidades, aplicación en placas electrónicas y iluminación. | diodos led smd, montaje superficial, paquete, 1000 unidades, uso, placas electrónicas, iluminación | 1 | 1 | sin_cambio |
| dev-10 | 63064000 | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba manual incluida. | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba manual incluida. | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba manual incluida. Colchón neumático, material de policloruro de vinilo, con dispositivo de inflado y desinflado por mano. | colchón inflable camping colchón neumático material PVC válvula bomba manual | 0 | 0 | sin_cambio |
| dev-11 | 95030010 | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ruedas. | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ruedas. | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ruedas. Patineta/transportín para niños con manillar regulable y sistema de frenado, juego con rodillos. | patinete scooter infantil ruedas manubrio ajustable freno juguete | 18 | 20 | perdido |
| dev-12 | 28151100 | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida para elaboración de detergentes. | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida para elaboración de detergentes. | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida para fabricación de detergentes. | soda cáustica escamas hidróxido de sodio grado industrial sólida elaboración detergentes | 0 | 0 | sin_cambio |
| dev-13 | 84713000 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulgadas. | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulgadas. | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulgadas. | computadora portátil procesador Intel Core i5 memoria RAM 8GB disco sólido SSD 512GB pantalla LED 14 pulgadas | 0 | 0 | sin_cambio |

## Análisis de errores

La fusión BM25 multi-query no mejoró el ranking inicial. En carne bovina (`dev-06`), RRF bajó la NANDINA esperada de rank 8 a rank 29 porque variantes similares reforzaron candidatos genéricos de carne bovina y cortes, pero no resolvieron la discriminación exacta. En patinete infantil (`dev-11`), el rank pasó de 18 a 20; las variantes reforzaron términos amplios como ruedas, manubrio y freno.

En los casos sin hallazgo de BM25 Q0 (`dev-07`, `dev-08`, `dev-10`, `dev-12`, `dev-13`), las variantes no recuperaron la NANDINA esperada dentro de la profundidad evaluada de forma suficiente para entrar al Top-10. Q3 además no cumplió siempre la forma estricta de términos separados solo por espacios, porque algunas salidas conservaron comas; se mantuvo la salida original del LLM para trazabilidad.

## Recomendación

No escalar todavía al evalset final. Con los resultados actuales, `BM25_multiquery_RRF` conserva Top-1, Top-3 y Top-5, pero reduce Top-10 de 0.5385 a 0.4615 y baja MRR de 0.4370 a 0.4296 frente a BM25 Q0. La siguiente iteración debería ajustar el prompt y/o el postproceso para que Q2 no altere atributos cuantitativos o discriminantes y para que Q3 sea una lista estricta de términos sin conectores ni puntuación.

## Validaciones

- No se modificó el devset.
- No se modificó el evalset.
- No se ejecutó LLM sobre el evalset.
- No se tocó el Excel fuente.
- `multiqueries.jsonl`: 13 líneas.
- `multiqueries.csv`: 13 filas.
- JSON válido: 13/13.
- Menciones prohibidas en salidas: 0.
- `rrf_case_comparison_13_cases.csv`: 13 filas.
- `rrf_metrics.json`: JSON válido.
- Smoke test BM25 ejecutado dentro de la evaluación RRF: carga de índice BM25 y recuperación para Q0-Q3.
- `git diff --check`: ejecutado sin errores.
