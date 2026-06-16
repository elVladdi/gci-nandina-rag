# Evaluación weighted BM25 multi-query devset v0.1

## Objetivo de la fase 6A1-2

Evaluar una fusión BM25 multi-query ponderada con Q0 protegido sobre el devset preliminar de 13 casos, reutilizando las variantes generadas en la fase 6A1-1 y sin ejecutar LLM, Text2Trade ni evalset final.

La fase prueba una hipótesis concreta: Q0 debe seguir siendo la señal dominante; Q1 y Q2 deben apoyar el ranking, pero no desplazar fácilmente los candidatos fuertes de la descripción original.

## Por qué se elimina Q3

En 6A1-1 se observó que Q3, formulada como bolsa de términos, puede introducir ruido y reforzar coincidencias genéricas. Para aislar el aporte de las variantes más controladas, esta corrida usa solo:

- Q0: descripción original del devset.
- Q1: descripción limpia ya generada por LLM en 6A1-1.
- Q2: descripción expandida ya generada por LLM en 6A1-1.

Q3 se ignora por completo en esta evaluación.

## Por qué Q0 se pondera más

Q0 preserva la evidencia original del caso y no depende de decisiones generativas. Por eso se le asigna mayor peso: Q0 = 3.0, Q1 = 1.0 y Q2 = 0.5. El objetivo es que Q1/Q2 aporten señales complementarias sin dominar la consulta original.

## Fusión ponderada

La fórmula usada fue:

```text
weighted_score(doc) =
  3.0 * (1 / (60 + rank_Q0)) +
  1.0 * (1 / (60 + rank_Q1)) +
  0.5 * (1 / (60 + rank_Q2))
```

Si un documento no aparece en una consulta, su contribución para esa consulta es 0. Se recuperó Top-100 por consulta BM25.

## Q0 protegido

La variante protegida no usa la NANDINA esperada para construir el ranking. La regla operacional es:

- Tomar el Top-10 de BM25_Q0.
- Mantener esos candidatos dentro del Top-10 final.
- Reordenar el bloque protegido con el score ponderado cuando corresponda.
- Ubicar candidatos nuevos de Q1/Q2 después de conservar el bloque Top-10 de Q0.

La etiqueta esperada solo se usa después, para evaluación diagnóstica.

## Trazabilidad de fases previas

| Variante | Top-1 | Top-3 | Top-5 | Top-10 | MRR |
|---|---:|---:|---:|---:|---:|
| BM25 original devset | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4370 |
| Rewrite v0.1 | 0.3077 | 0.4615 | 0.4615 | 0.4615 | 0.3755 |
| Rewrite v0.2 | 0.3077 | 0.4615 | 0.5385 | 0.5385 | 0.3908 |
| BM25 multiquery RRF plano | 0.3846 | 0.4615 | 0.4615 | 0.4615 | 0.4296 |

## Métricas comparativas

| Método | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Top-10 HS4 | Top-10 HS2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| BM25_Q0_baseline | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4370 | 0.8462 | 0.8462 |
| BM25_Q0_Q1_Q2_weighted_RRF | 0.3846 | 0.4615 | 0.4615 | 0.4615 | 0.4325 | 0.8462 | 0.8462 |
| BM25_Q0_Q1_Q2_weighted_RRF_protected | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4359 | 0.8462 | 0.8462 |

## Recall amplio

| Método o pool | Recall@50 | Recall@100 |
|---|---:|---:|
| BM25_Q0_baseline | 0.6154 | 0.6154 |
| BM25_Q0_Q1_Q2_weighted_RRF | 0.6154 | 0.6154 |
| BM25_Q0_Q1_Q2_weighted_RRF_protected | 0.6154 | 0.6154 |
| Pool Q0_Q1_Q2 | 0.6154 | 0.6154 |

Q1/Q2 no agregaron ningún caso correcto nuevo cuando Q0 no lo traía dentro de la profundidad 100. En esta muestra, las variantes reordenan y refuerzan candidatos ya presentes, pero no amplían el recall de NANDINA correcta.

## Comparación contra BM25_Q0_baseline

| Variante | Ganados | Perdidos | Sin cambio |
|---|---:|---:|---:|
| Weighted RRF | 0 | 1 | 12 |
| Weighted RRF protected | 0 | 1 | 12 |

- Casos donde Q0 tenía la NANDINA en Top-10 y weighted RRF no protegido la expulsó: 1 (`dev-06`).
- Casos donde la protección evitó la expulsión del Top-10: 1 (`dev-06`).
- Casos donde Q1/Q2 trajeron la NANDINA correcta y Q0 no: 0.

## Tabla de 13 casos

Los textos de Q0-Q2 se muestran abreviados solo para lectura. Los CSV guardan las consultas completas y las fuentes por candidato.

| Caso | NANDINA | Q0 | Q1 | Q2 | Rank Q0 | Rank weighted | Rank protected | Weighted vs Q0 | Protected vs Q0 | Protección evitó expulsión | Q1/Q2 trajeron nuevo correcto |
|---|---|---|---|---|---:|---:|---:|---|---|---:|---:|
| dev-01 | 84713000 | Máquina automática para tratamiento o procesamiento de datos, portátil, constituida al ... | Máquina automática para tratamiento o procesamiento de datos, portátil, constituida al ... | Máquina automática para tratamiento o procesamiento de datos, portátil, compuesta al me... | 1 | 1 | 1 | sin_cambio | sin_cambio | 0 | 0 |
| dev-02 | 10063000 | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en sacos para venta mayor... | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en sacos para venta mayor... | Arroz semiblanqueado o blanqueado, incluso pulido o glaseado, en envases de venta mayor... | 1 | 1 | 1 | sin_cambio | sin_cambio | 0 | 0 |
| dev-03 | 04029110 | Leche evaporada, sin adición de azúcar ni otros edulcorantes, en latas. | Leche evaporada, sin adición de azúcar ni otros edulcorantes, en latas. | Leche evaporada, sin adición de azúcar ni otros edulcorantes, empaquetada en latas. | 2 | 2 | 2 | sin_cambio | sin_cambio | 0 | 0 |
| dev-04 | 22030000 | Cerveza de malta, bebida alcohólica en envases de vidrio para consumo. | Cerveza de malta, bebida alcohólica en envases de vidrio para consumo. | Cerveza de malta, bebida alcohólica en recipientes de vidrio para consumo. | 1 | 1 | 1 | sin_cambio | sin_cambio | 0 | 0 |
| dev-05 | 39012000 | Polietileno de densidad superior o igual a 0,94, en gránulos (pellets) para transformac... | Polietileno de densidad superior a 0,94, en gránulos (pellets) para transformación indu... | Polietileno de alta densidad (densidad >= 0,94), en gránulos (pellets) destinado a la tr... | 1 | 1 | 1 | sin_cambio | sin_cambio | 0 | 0 |
| dev-06 | 02013000 | Carne de la especie bovina, fresca o refrigerada, deshuesada, cortes empacados al vacío. | Carne de la especie bovina, fresca o refrigerada, deshuesada, cortes empacados al vacío. | Carne de la especie bovina, fresca o refrigerada, sin huesos, cortes empaquetados en va... | 8 | 15 | 9 | perdido | perdido | 1 | 0 |
| dev-07 | 84713000 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 5... | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 5... | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 5... | 0 | 0 | 0 | sin_cambio | sin_cambio | 0 | 0 |
| dev-08 | 84717000 | Disco sólido externo portátil (SSD) de 1 TB, interfaz USB 3.2, usado como unidad de alm... | Disco sólido externo portátil (SSD) de 1 TB, interfaz USB 3.2, usado como unidad de alm... | Disco sólido externo portátil (SSD) de 1024 GB, con conexión USB 3.2, utilizado para al... | 0 | 0 | 0 | sin_cambio | sin_cambio | 0 | 0 |
| dev-09 | 85414100 | Diodos LED SMD para montaje superficial, paquete de 1000 unidades, uso en placas electr... | Diodos LED SMD para montaje superficial, paquete de 1000 unidades, uso en placas electr... | Diodos LED Surface Mount Device (SMD) para montaje superficial, paquete de 1000 unidade... | 1 | 1 | 1 | sin_cambio | sin_cambio | 0 | 0 |
| dev-10 | 63064000 | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba ma... | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba ma... | Colchón inflable para camping (colchón neumático), material PVC, con válvula y bomba ma... | 0 | 0 | 0 | sin_cambio | sin_cambio | 0 | 0 |
| dev-11 | 95030010 | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ru... | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ru... | Patinete/scooter infantil de tres ruedas con manubrio ajustable y freno, juguete con ru... | 18 | 18 | 18 | sin_cambio | sin_cambio | 0 | 0 |
| dev-12 | 28151100 | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida par... | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida par... | Soda cáustica en escamas (hidróxido de sodio) grado industrial, presentación sólida par... | 0 | 0 | 0 | sin_cambio | sin_cambio | 0 | 0 |
| dev-13 | 84713000 | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 5... | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 5... | Computadora portátil con procesador Intel Core i5, memoria RAM 8 GB, disco sólido SSD 5... | 0 | 0 | 0 | sin_cambio | sin_cambio | 0 | 0 |

## Análisis de errores

El caso crítico sigue siendo `dev-06`. Q0 ubica la NANDINA esperada en rank 8; la fusión ponderada no protegida la baja a rank 15. La protección conserva el bloque Top-10 de Q0 y devuelve el caso a rank 9, evitando la pérdida de Top-10, aunque todavía queda peor que Q0 puro.

`dev-11` deja de ser una pérdida frente a 6A1-1: el weighted RRF con Q0 dominante mantiene rank 18, igual que Q0. Aun así, no hay mejora semántica. Los casos `dev-07`, `dev-08`, `dev-10`, `dev-12` y `dev-13` siguen sin recuperar la NANDINA exacta dentro de Top-100; por eso el pool Q0_Q1_Q2 no mejora Recall@50 ni Recall@100.

## Recomendación

No escalar todavía al evalset final. La variante protegida corrige la degradación más peligrosa de Top-10 y mejora sobre el RRF plano, pero no supera a BM25 Q0 en MRR ni agrega recall amplio. Metodológicamente, esta fase sirve para fijar una regla defensiva útil: cualquier expansión futura debería mantener Q0 protegido. La siguiente iteración debería buscar variantes que realmente aumenten recall, no solo reordenen el pool existente.

## Validaciones

- No se modificó el devset.
- No se modificó el evalset.
- No se ejecutó LLM.
- No se ejecutó sobre el evalset final.
- No se tocó el Excel fuente.
- Se usó `outputs/evaluation/multiquery_rrf_devset_v0.1/multiqueries.jsonl` existente.
- `weighted_case_comparison_13_cases.csv`: 13 filas.
- `weighted_metrics.json`: JSON válido.
- Smoke test BM25: ejecutado.
- `git diff --check`: ejecutado sin errores.
- Revisión de mojibake en este Markdown: sin patrones problemáticos.
