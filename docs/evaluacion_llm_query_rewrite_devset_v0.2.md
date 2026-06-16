# Evaluacion LLM query rewrite devset v0.2

## Objetivo

La mini fase 6A-2 ajusta la capa local de query rewriting para preservar atributos discriminantes antes de BM25, usando exclusivamente el devset preliminar de 13 casos. No se ejecuto LLM ni BM25 sobre el evalset final.

## Modelo y ejecucion

- Modelo: `qwen2.5:7b-instruct` via Ollama local.
- Prompt: `src/llm/query_rewrite_prompt_v0.2.md`.
- Temperature: 0.0.
- Formato: JSON estricto con `format=json`.
- Python usado: runtime bundled de Codex `C:/Users/Vladimir/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`; la `.venv` del proyecto existe, pero no pudo ejecutarse porque apunta a un Python local inexistente.

## Diferencias entre prompt v0.1 y v0.2

- v0.2 mantiene las prohibiciones de clasificar, sugerir NANDINA, mencionar capitulo/partida/subpartida/codigo e inventar atributos.
- v0.2 cambia el criterio operativo de resumir a limpiar y ordenar.
- v0.2 exige conservar estado fisico/conservacion, composicion/material, forma/presentacion, funcion/uso, tecnologia/especificaciones, negaciones y especie/origen.
- v0.2 agrega control explicito: si hay mas de un atributo discriminante, `consulta_reescrita` debe conservarlos en una sola frase nominal aunque sea mas larga.
- v0.2 exige advertir si elimina un atributo potencialmente discriminante por falta de certeza.

## Calidad de salida LLM v0.2

- Casos procesados: 13.
- JSON valido: 13/13 (1.0000).
- Violaciones por codigos arancelarios/NANDINA: 0.
- Violaciones por terminos prohibidos: 0.
- Consultas reescritas vacias: 0.

## Metricas BM25 comparativas

| Metrica | BM25 original | Rewrite v0.1 | Rewrite v0.2 |
|---|---:|---:|---:|
| Top-1 accuracy | 0.3846 | 0.3077 | 0.3077 |
| Top-3 accuracy | 0.4615 | 0.4615 | 0.4615 |
| Top-5 accuracy | 0.4615 | 0.4615 | 0.5385 |
| Top-10 accuracy | 0.5385 | 0.4615 | 0.5385 |
| MRR | 0.4370 | 0.3755 | 0.3908 |

## Casos ganados, perdidos y sin cambio

| Variante | Ganados | Perdidos | Sin cambio | JSON invalidos | Violaciones codigo |
|---|---:|---:|---:|---:|---:|
| Rewrite v0.1 | 1 | 3 | 9 | 0 | 0 |
| Rewrite v0.2 | 2 | 2 | 9 | 0 | 0 |

## Analisis cualitativo

La v0.2 corrigio el problema mas visible de v0.1 en carne bovina: recupero `fresca`, `refrigerada` y `deshuesada`, y el rank mejoro de no encontrado a 5. Tambien conserva mejor atributos de arroz, polietileno y diodos LED SMD. Sin embargo, todavia pierde atributos relevantes en algunos casos: cerveza pierde `malta` y `bebida alcoholica`; leche conserva `sin azucar`, pero no explicita `sin edulcorantes`; soda caustica pierde `hidroxido de sodio` y `grado industrial`; disco externo altera `disco solido` hacia `disco duro` y omite `1 TB`.

Metodologicamente, v0.2 mejora frente a v0.1 en Top-5, Top-10 y MRR, pero no supera al BM25 original en Top-1 ni MRR. La mejora cualitativa de preservacion es real, aunque insuficiente para justificar una corrida sobre el evalset final.

## Recomendacion

No pasar todavia al evalset final. La siguiente iteracion deberia reforzar conservacion literal de negaciones, sustancias/composicion y capacidad tecnica, y penalizar sustituciones no equivalentes como `disco duro` por `disco solido`. Tambien conviene agregar una validacion automatica de cobertura de atributos antes de aceptar una reescritura para retrieval.

## Tabla de 13 casos

CSV regenerable equivalente: `outputs/evaluation/llm_query_rewrite_devset_v0.2/rewrite_comparison_13_cases.csv`.

| case_id | NANDINA esperada | descripcion original | consulta_reescrita v0.1 | consulta_reescrita v0.2 | atributos preservados | atributos perdidos o alterados | rank BM25 original | rank BM25 v0.1 | rank BM25 v0.2 | resultado v0.2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dev-01 | 84713000 | Máquina automática para tratamiento o procesamiento de datos, portátil, constituida al menos por unidad central, teclado y visualizador integrados; peso menor a 10 kg. | maquina automatica para tratamiento de datos portatil con unidad central teclado y visualizador peso menor a 10 kg | maquina automatica para tratamiento de datos portatil con unidad central teclado y visualizador peso menor a 10 kg | maquina automatica; tratamiento/procesamiento de datos; portatil; unidad central; teclado; visualizador; peso menor a 10 kg | ninguno detectado automaticamente | 1 | 3 | 3 | perdido |
| dev-02 | 10063000 | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en sacos para venta mayorista. | arroz semiblanqueado o blanqueado en sacos para venta mayorista | arroz semiblanqueado o blanqueado, pulido o glaseado en sacos para venta mayorista | arroz; semiblanqueado o blanqueado; pulido o glaseado; sacos; venta mayorista | ninguno detectado automaticamente | 1 | 1 | 1 | sin_cambio |
| dev-03 | 04029110 | Leche evaporada, sin adición de azúcar ni otros edulcorantes, en latas. | leche evaporada en latas sin azúcar | leche evaporada sin azucar en lata | leche evaporada; sin azucar; latas | sin edulcorantes | 2 | 1 | 1 | ganado |
| dev-04 | 22030000 | Cerveza de malta, bebida alcohólica en envases de vidrio para consumo. | cerveza en envases de vidrio para consumo | cerveza en envases de vidrio | cerveza; envases de vidrio | malta; bebida alcoholica; consumo | 1 | 2 | 2 | perdido |
| dev-05 | 39012000 | Polietileno de densidad superior o igual a 0,94, en gránulos (pellets) para transformación industrial. | polietileno en gránulos para transformación industrial con densidad superior a 0,94 | polietileno densidad superior a 0,94 gránulos pellets transformación industrial | polietileno; densidad superior o igual a 0,94; granulos/pellets; transformacion industrial | ninguno detectado automaticamente | 1 | 1 | 1 | sin_cambio |
| dev-06 | 02013000 | Carne de la especie bovina, fresca o refrigerada, deshuesada, cortes empacados al vacío. | corte de carne bovina empacado al vacío | carne bovina deshuesada cortes empacados al vacío fresca refrigerada | carne bovina; fresca; refrigerada; deshuesada; cortes; empacados al vacio | ninguno detectado automaticamente | 8 | 0 | 5 | ganado |
| dev-07 | 84713000 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulgadas. | computadora portátil con procesador intel core i5 8 gb ssd 512 gb pantalla led 14 pulgadas | computadora portatil con procesador intel core i5, memoria ram 8 gb, disco solid state ssd 512 gb, pantalla led de 14 pulgadas | computadora portatil; procesador Intel Core i5; memoria RAM 8 GB; SSD 512 GB; pantalla LED 14 pulgadas | ninguno detectado automaticamente | 0 | 0 | 0 | sin_cambio |
| dev-08 | 84717000 | Disco sólido externo portátil (SSD) de 1 TB, interfaz USB 3.2, usado como unidad de almacenamiento de datos. | disco sólido externo portátil interfaz USB 3.2 almacenamiento de datos | disco duro externo SSD portátil interfaz USB 3.2 almacenamiento de datos | disco solido externo portatil; SSD; USB 3.2; almacenamiento de datos | 1 TB | 0 | 0 | 0 | sin_cambio |
| dev-09 | 85414100 | Diodos LED SMD para montaje superficial, paquete de 1000 unidades, uso en placas electrónicas e iluminación. | diodos led smd para placas electronicas y iluminacion en paquetes de 1000 unidades | diodos led smd para montaje superficial en placas electrónicas e iluminación en paquete de 1000 unidades | diodos LED SMD; montaje superficial; paquete de 1000/mil unidades; placas electronicas; iluminacion | ninguno detectado automaticamente | 1 | 1 | 1 | sin_cambio |
| dev-10 | 63064000 | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba manual incluida. | colchón inflable camping PVC válvula bomba manual | colchón inflable camping PVC válvula bomba manual | colchon inflable/neumatico; camping; PVC; valvula; bomba manual | ninguno detectado automaticamente | 0 | 0 | 0 | sin_cambio |
| dev-11 | 95030010 | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ruedas. | patinete scooter infantil tres ruedas manubrio ajustable freno | patinete infantil tres ruedas manubrio ajustable freno | patinete/scooter; infantil; tres ruedas; manubrio ajustable; freno; juguete con ruedas | ninguno detectado automaticamente | 18 | 21 | 21 | sin_cambio |
| dev-12 | 28151100 | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida para elaboración de detergentes. | soda cáustica para detergentes escamas sólidas | soda cáustica escamas sólida para detergentes | soda caustica; escamas; solida; detergentes | hidroxido de sodio; grado industrial | 0 | 0 | 0 | sin_cambio |
| dev-13 | 84713000 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulgadas. | computadora portátil con procesador intel core i5 8 gb ssd 512 gb pantalla led 14 pulgadas | computadora portatil con procesador intel core i5, memoria ram 8 gb, disco solid state ssd 512 gb, pantalla led de 14 pulgadas | computadora portatil; procesador Intel Core i5; memoria RAM 8 GB; SSD 512 GB; pantalla LED 14 pulgadas | ninguno detectado automaticamente | 0 | 0 | 0 | sin_cambio |
