# Evaluacion BM25 fielded devset v0.1

## Objetivo

Evaluar una variante BM25 por campos para NANDINA8 con ponderacion explicita de descripcion 8D, HS6, 4D y expansion lexica controlada del corpus. La evaluacion usa solo el devset de 13 casos.

## Razon metodologica

La Fase 7A-2 con extraccion LLM pre-retrieval no mejoro Recall@50 ni Recall@100 frente a Q0 BM25 jerarquico. Por eso esta fase vuelve al problema base: calidad del corpus y recuperacion documental, sin LLM en tiempo de consulta.

## Construccion del corpus por campos

Se parte de `data/processed/corpus_nandina_hierarchical_v0.1.jsonl` y se generan dos JSONL regenerables: fielded y fielded-expanded. Los codigos NANDINA se conservan como identificadores/metadata, no como terminos en `texto_index_fielded`.

## Ponderacion

| Campo | Peso |
|---|---:|
| descripcion_8d | 4 |
| descripcion_hs6 | 3 |
| descripcion_4d | 1 |
| descripcion_capitulo | 0 |
| texto_expansion_controlada | 2 |

La ponderacion se simula repitiendo campos en el texto indexable porque el BM25 actual no implementa campos reales.

## Expansiones controladas usadas

| ID | Codigos objetivo | Terminos |
|---|---|---|
| sodium_hydroxide_caustic_soda | 28151100, 28151200 | soda caustica, sosa caustica, hidroxido de sodio, caustic soda |
| portable_computer_laptop | 84713000 | computadora portatil, ordenador portatil, laptop, notebook, equipo portatil de procesamiento de datos |
| solid_state_drive_storage | 84717000 | unidad de estado solido, disco solido, ssd, unidad de almacenamiento de datos, memoria externa |
| high_density_polyethylene | 39012000 | polietileno alta densidad, polietileno de alta densidad, hdpe, pead, granulos, pellets |
| light_emitting_diode | 85414100 | led, diodo emisor de luz, diodos emisores de luz, smd, montaje superficial |
| malt_beer | 22030000 | cerveza de malta, bebida de malta, bebida alcoholica de malta |
| inflatable_mattress_camping | 63064000 | colchon inflable, colchon neumatico, articulo de acampar, camping |
| polyvinyl_chloride | 39041010, 39041020, 39042100, 39042200 | pvc, policloruro de vinilo |
| scooter_toy_with_wheels | 95030010 | patinete, scooter, juguete con ruedas, triciclo, coches de pedal |

## Metricas comparativas

| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4@10 | HS2@10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25_hierarchical_Q0 | 0.3846 | 0.5385 | 0.6154 | 0.6154 | 0.4701 | 0.6923 | 0.6923 | 0.7692 | 0.7692 |
| BM25_fielded_weighted_v0.1 | 0.3077 | 0.5385 | 0.6154 | 0.6923 | 0.4385 | 0.6923 | 0.6923 | 0.9231 | 0.9231 |
| BM25_fielded_weighted_expanded_v0.1 | 0.7692 | 0.9231 | 1.0000 | 1.0000 | 0.8654 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| phase7a_pool_hierarchical_80_dual_backfill_20 | 0.3846 | 0.5385 | 0.6154 | 0.6154 | 0.4709 | 0.6923 | 0.7692 | 0.7692 | 0.7692 |

## Comparacion contra BM25_hierarchical_Q0

| Metodo | Ganados | Perdidos | Sin cambio | Nuevos Q0 no recuperaba | Degradados |
|---|---:|---:|---:|---:|---:|
| BM25_fielded_weighted_v0.1 | 2 | 2 | 9 | 0 | 2 |
| BM25_fielded_weighted_expanded_v0.1 | 8 | 0 | 5 | 4 | 0 |
| phase7a_pool_hierarchical_80_dual_backfill_20 | 1 | 0 | 12 | 1 | 0 |

## Tabla de 13 casos

| Caso | Descripcion | NANDINA | Rank Q0 | Rank fielded | Rank expanded | Resultado expanded |
|---|---|---|---:|---:|---:|---|
| dev-01 | Máquina automática para tratamiento o procesamiento de datos, portátil, constituida al menos por unidad central, tecl... | 84713000 | 1 | 2 | 1 | sin_cambio |
| dev-02 | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en sacos para venta mayorista. | 10063000 | 1 | 1 | 1 | sin_cambio |
| dev-03 | Leche evaporada, sin adición de azúcar ni otros edulcorantes, en latas. | 04029110 | 1 | 1 | 1 | sin_cambio |
| dev-04 | Cerveza de malta, bebida alcohólica en envases de vidrio para consumo. | 22030000 | 1 | 1 | 1 | sin_cambio |
| dev-05 | Polietileno de densidad superior o igual a 0,94, en gránulos (pellets) para transformación industrial. | 39012000 | 36 | 5 | 4 | ganado |
| dev-06 | Carne de la especie bovina, fresca o refrigerada, deshuesada, cortes empacados al vacío. | 02013000 | 1 | 1 | 1 | sin_cambio |
| dev-07 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulg... | 84713000 | 0 | 0 | 2 | ganado |
| dev-08 | Disco sólido externo portátil (SSD) de 1 TB, interfaz USB 3.2, usado como unidad de almacenamiento de datos. | 84717000 | 0 | 0 | 1 | ganado |
| dev-09 | Diodos LED SMD para montaje superficial, paquete de 1000 unidades, uso en placas electrónicas e iluminación. | 85414100 | 2 | 2 | 1 | ganado |
| dev-10 | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba manual incluida. | 63064000 | 0 | 0 | 1 | ganado |
| dev-11 | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ruedas. | 95030010 | 3 | 6 | 1 | ganado |
| dev-12 | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida para elaboración de detergentes. | 28151100 | 4 | 3 | 1 | ganado |
| dev-13 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 512 GB, pantalla LED de 14 pulg... | 84713000 | 0 | 0 | 2 | ganado |

## Casos criticos

| Caso | NANDINA | Rank Q0 | Rank fielded | Rank expanded | Top10 expanded |
|---|---|---:|---:|---:|---|
| dev-01 | 84713000 | 1 | 2 | 1 | 84713000 84714100 84717000 90221200 84719000 84718000 84714900 84433219 84433220 84433290 |
| dev-05 | 39012000 | 36 | 5 | 4 | 44119300 44119200 44119400 39012000 11052000 72101100 72072000 76061220 76069230 72193400 |
| dev-07 | 84713000 | 0 | 0 | 2 | 84717000 84713000 85395100 85414100 85395200 84716090 28151100 85411000 84716020 81041100 |
| dev-08 | 84717000 | 0 | 0 | 1 | 84717000 84713000 29034600 85235100 29034700 29034800 29035910 84714100 29035100 29103000 |
| dev-09 | 85414100 | 2 | 2 | 1 | 85414100 85411000 85395100 85395200 94051190 94051120 85412900 85414900 85415900 85419000 |
| dev-10 | 63064000 | 0 | 0 | 1 | 63064000 84798930 84158190 39042100 39042200 84158110 89051000 89059000 39041010 39041020 |
| dev-11 | 95030010 | 3 | 6 | 1 | 95030010 87087010 84834092 87087020 83022000 87142000 84839040 87032410 87033310 87033110 |
| dev-12 | 28151100 | 4 | 3 | 1 | 28151100 28151200 28152000 28153000 25041000 84382020 34029010 28161000 28183000 03019911 |
| dev-13 | 84713000 | 0 | 0 | 2 | 84717000 84713000 85395100 85414100 85395200 84716090 28151100 85411000 84716020 81041100 |

## Decision metodologica

Escalar al evalset en una subfase separada con la variante congelada `BM25_fielded_weighted_expanded_v0.1`, porque mejora recall amplio sin degradar materialmente Top-10/MRR.

- Delta Recall@50 expanded vs Q0: +0.3077.
- Delta Recall@100 expanded vs Q0: +0.3077.
- Delta Top-10 expanded vs Q0: +0.3846.
- Delta MRR expanded vs Q0: +0.3953.

## Limitaciones

- El devset tiene solo 13 casos y sirve como senal exploratoria.
- La expansion es manual y conservadora; puede mejorar casos lexicales concretos sin generalizar.
- El corpus jerarquico fuente tiene ruido en algunos padres 4D/capitulos; el fielded reduce peso 4D, pero no repara la extraccion fuente.
- No se evalua fundamento legal ni clasificacion oficial, solo recuperacion documental.

## Validaciones declaradas

- No se ejecuto evalset.
- No se uso LLM.
- No se uso Text2Trade.
- Devset/evalset/Excel fuente no se modifican por estos scripts.
