# Evaluacion LLM attribute retrieval devset v0.1

## Objetivo

Evaluar una capa exploratoria pre-retrieval donde el LLM solo extrae atributos estructurados explicitos de la descripcion comercial. La fase usa exclusivamente el devset de 13 casos y no clasifica, no sugiere codigos NANDINA y no reemplaza la descripcion original.

## Modelo usado

- Modelo local Ollama: `qwen2.5:7b-instruct`.
- Endpoint local: `http://127.0.0.1:11434/api/chat`.
- Temperature: 0.0.
- APIs remotas: no usadas.
- Text2Trade: no usado.
- Evalset: no ejecutado.

## Prompt usado

```text
Eres un asistente tecnico de comercio exterior. Tu tarea es extraer y normalizar atributos explicitos de una descripcion comercial para apoyar busqueda documental.

Descripcion comercial:
{{descripcion}}

Reglas obligatorias:
- No clasifiques la mercancia.
- No sugieras NANDINA.
- No menciones capitulo, partida, subpartida ni codigo arancelario.
- No inventes atributos.
- Conserva solo informacion explicita o inferencias terminologicas muy seguras.
- Si un atributo no aparece, devuelvelo vacio.
- No reemplaces la descripcion original.
- Responde solo JSON estricto.
- El idioma de salida debe ser espanol tecnico.

Devuelve exactamente un objeto JSON con este esquema:

{
  "producto": "",
  "material": "",
  "composicion": "",
  "uso_funcion": "",
  "presentacion": "",
  "estado": "",
  "tecnologia": "",
  "medidas": "",
  "marca_modelo": "",
  "atributos_discriminantes": [],
  "terminos_busqueda": [],
  "advertencias": []
}

Normalizacion:
- Usa frases breves, tecnicas y fieles al texto.
- En listas, incluye solo terminos o atributos utiles para busqueda documental.
- No incluyas marcas o modelos en `terminos_busqueda` ni en `atributos_discriminantes`.
- No incluyas numeros que parezcan codigos arancelarios.
- Si detectas ambiguedad, conserva el campo vacio y anota una advertencia breve.
```

## Generacion de consultas

- Q0: descripcion original, siempre conservada.
- Q1: producto + material + composicion + estado.
- Q2: producto + uso_funcion + presentacion + tecnologia + medidas.
- Q3: producto + atributos_discriminantes + terminos_busqueda.
- Marca/modelo se conserva como metadata y no entra en Q1-Q3.
- Consultas vacias, genericas o con terminos de codigo arancelario se descartan.

## Formula de fusion

Se usa RRF ponderado por consulta:

`score(d) = sum_q peso(q) / (k_rrf + rank_q(d))`, con `k_rrf = 60`.

Pesos: Q0=3.0, Q1=1.5, Q2=1.0, Q3=0.75.

La variante protegida fija los Top-10 de Q0 como bloque inicial y usa las consultas LLM solo como backfill despues de esos candidatos.

## Metricas comparativas

| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4@10 | HS2@10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25_hierarchical_Q0 | 0.3846 | 0.5385 | 0.6154 | 0.6154 | 0.4701 | 0.6923 | 0.6923 | 0.7692 | 0.7692 |
| BM25_hierarchical_attribute_weighted_rrf | 0.3846 | 0.4615 | 0.6154 | 0.6154 | 0.4607 | 0.6923 | 0.6923 | 0.6154 | 0.6154 |
| BM25_hierarchical_attribute_q0_protected | 0.3846 | 0.5385 | 0.6154 | 0.6154 | 0.4709 | 0.6923 | 0.6923 | 0.7692 | 0.7692 |
| phase7a_pool_hierarchical_80_dual_backfill_20 | 0.3846 | 0.5385 | 0.6154 | 0.6154 | 0.4709 | 0.6923 | 0.7692 | 0.7692 | 0.7692 |

## Comparacion contra Q0

| Metodo | Ganados | Perdidos | Sin cambio | Nuevos Q0 no recuperaba | Degradados |
|---|---:|---:|---:|---:|---:|
| BM25_hierarchical_attribute_weighted_rrf | 1 | 1 | 11 | 0 | 1 |
| BM25_hierarchical_attribute_q0_protected | 1 | 0 | 12 | 0 | 0 |
| phase7a_pool_hierarchical_80_dual_backfill_20 | 1 | 0 | 12 | 1 | 0 |

## Calidad JSON y violaciones

- JSON valido: 13/13.
- JSON invalido: 0.
- Codigos sugeridos o detectados: 0.
- Terminos prohibidos detectados: 1.
- Posibles atributos inventados por heuristica: 2.

## Tabla de los 13 casos

| Caso | Descripcion original | JSON resumido | Q1 | Q2 | Q3 | Rank Q0 | Rank LLM protegido | Resultado |
|---|---|---|---|---|---|---:|---:|---|
| dev-01 | Máquina automática para tratamiento o procesamiento de datos, portátil, constituida al menos por unidad central, tecl... | producto=Máquina automática para tratamiento o procesamiento de datos; uso_funcion=Tratamiento o procesamiento de dat... | Máquina automática para tratamiento o procesamiento de datos | Máquina automática para tratamiento o procesamiento de datos Tratamiento o procesamiento de datos Portátil Peso menor... | Máquina automática para tratamiento o procesamiento de datos unidad central teclado integrado visualizador integrado... | 1 | 1 | sin_cambio |
| dev-02 | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en sacos para venta mayorista. | producto=Arroz; estado=Semiblanqueado, blanqueado, pulido o glaseado; terminos=arroz semiblanqueado, arroz blanqueado... | Arroz Semiblanqueado, blanqueado, pulido o glaseado | Arroz Sacos | Arroz arroz semiblanqueado arroz blanqueado arroz pulido arroz glaseado sacos | 1 | 1 | sin_cambio |
| dev-03 | Leche evaporada, sin adición de azúcar ni otros edulcorantes, en latas. | producto=Leche evaporada; composicion=Sin adición de azúcar ni otros edulcorantes; terminos=leche evaporada, sin azúc... | Leche evaporada Sin adición de azúcar ni otros edulcorantes | Leche evaporada En latas | Leche evaporada sin azúcar latas | 1 | 1 | sin_cambio |
| dev-04 | Cerveza de malta, bebida alcohólica en envases de vidrio para consumo. | producto=Cerveza; material=Vidrio; uso_funcion=Consumo; terminos=Cerveza, Bebida alcohólica, Envases de vidrio | Cerveza Vidrio | Cerveza Consumo | Cerveza Bebida alcohólica Envases de vidrio | 1 | 1 | sin_cambio |
| dev-05 | Polietileno de densidad superior o igual a 0,94, en gránulos (pellets) para transformación industrial. | producto=Polietileno; uso_funcion=Transformación industrial; atributos=densidad superior a 0,94; terminos=polietileno... |  | Polietileno Transformación industrial Gránulos (pellets) | Polietileno densidad superior a 0,94 gránulos pellets transformación industrial densidad > 0,94 | 36 | 26 | ganado |
| dev-06 | Carne de la especie bovina, fresca o refrigerada, deshuesada, cortes empacados al vacío. | producto=Carne bovina; estado=Fresca o refrigerada; terminos=carne bovina, fresca, refrigerada | Carne bovina Fresca o refrigerada | Carne bovina Empacados al vacío | Carne bovina fresca refrigerada empacados al vacío | 1 | 1 | sin_cambio |
| dev-07 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulg... | producto=Computadora portátil; uso_funcion=Personal/Oficina; atributos=Procesador, Memoria RAM, Disco sólido; termino... | Computadora portátil | Computadora portátil Personal/Oficina Procesador Intel Core i5, SSD 512 GB, RAM 8 GB, Pantalla LED 14 pulgadas | Computadora portátil Procesador Memoria RAM Disco sólido Pantalla procesador intel core i5 memoria ram 8 gb disco sol... | 0 | 0 | sin_cambio |
| dev-08 | Disco sólido externo portátil (SSD) de 1 TB, interfaz USB 3.2, usado como unidad de almacenamiento de datos. | producto=Disco sólido externo portátil (SSD); uso_funcion=unidad de almacenamiento de datos; estado=usado; terminos=d... | Disco sólido externo portátil (SSD) usado | Disco sólido externo portátil (SSD) unidad de almacenamiento de datos USB 3.2 1 TB | Disco sólido externo portátil (SSD) disco sólido externo SSD 1 TB interfaz USB 3.2 unidad de almacenamiento | 0 | 0 | sin_cambio |
| dev-09 | Diodos LED SMD para montaje superficial, paquete de 1000 unidades, uso en placas electrónicas e iluminación. | producto=Diodos LED SMD; uso_funcion=Placas electrónicas, Iluminación; terminos=diodos led, smd, montaje superficial |  | Diodos LED SMD Placas electrónicas, Iluminación Paquete de 1000 unidades SMD (Superficial) | Diodos LED SMD diodos led smd montaje superficial placas electrónicas iluminación | 2 | 2 | sin_cambio |
| dev-10 | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba manual incluida. | producto=Colchón inflable para camping; material=PVC; uso_funcion=Camping; terminos=colchón inflable, PVC, válvula | Colchón inflable para camping PVC | Colchón inflable para camping Camping Válvula, bomba manual incluida | Colchón inflable para camping colchón inflable PVC válvula bomba manual | 0 | 0 | sin_cambio |
| dev-11 | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ruedas. | producto=Patinete/scooter; uso_funcion=Infantil; atributos=tres ruedas; terminos=patinete infantil, scooter infantil,... | Patinete/scooter | Patinete/scooter Infantil Con manubrio ajustable, freno | Patinete/scooter tres ruedas patinete infantil scooter infantil manubrio ajustable freno | 3 | 3 | sin_cambio |
| dev-12 | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida para elaboración de detergentes. | producto=Soda cáustica; material=hidróxido de sodio; uso_funcion=elaboración de detergentes; terminos=soda cáustica,... | Soda cáustica hidróxido de sodio | Soda cáustica elaboración de detergentes escamas sólida | Soda cáustica hidróxido de sodio escamas sólida detergentes | 4 | 4 | sin_cambio |
| dev-13 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulg... | producto=Computadora portátil; uso_funcion=Personal/Oficina; atributos=Procesador, Memoria RAM, Disco sólido; termino... | Computadora portátil | Computadora portátil Personal/Oficina Procesador Intel Core i5, SSD 512 GB, RAM 8 GB, Pantalla LED 14 pulgadas | Computadora portátil Procesador Memoria RAM Disco sólido Pantalla procesador intel core i5 memoria ram 8 gb disco sol... | 0 | 0 | sin_cambio |

## Decision metodologica

No escalar al evalset: la capa LLM no mejora claramente Recall@50/Recall@100 frente a Q0 BM25 jerarquico, o no ofrece una ganancia suficiente para justificar el costo. Mantener prioridad en mejorar corpus y recuperacion documental base.

- Mejora Recall@50 protegido: +0.0000.
- Mejora Recall@100 protegido: +0.0000.
- Delta Top-10 protegido: +0.0000.
- Delta MRR protegido: +0.0008.

## Limitaciones

- Devset pequeno de 13 casos; sirve solo como diagnostico temprano.
- La deteccion de atributos inventados es heuristica y debe revisarse manualmente.
- La proteccion Q0 prioriza no degradar Top-10, por lo que la mejora esperada debe aparecer sobre todo como recall/backfill.
- No valida fundamento legal ni clasificacion oficial; mide recuperacion documental.

## Validaciones declaradas

- Devset/evalset/Excel fuente no se modifican por estos scripts.
- No se ejecuto evalset.
- No se uso Text2Trade.
- No se usaron APIs remotas.
- Los artefactos JSONL/CSV son regenerables bajo `outputs/evaluation/llm_attribute_retrieval_devset_v0.1/`.
