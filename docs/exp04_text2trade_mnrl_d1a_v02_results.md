# EXP-04 Fase D: resultados D1a MNRL v0.2

## Gate D

**GATE D APROBADO para D1a.** La evaluación se ejecutó únicamente después del Gate de integridad vectorial. La muestra determinística de 21 documentos obtuvo coseno reconstruido/almacenado entre 0.9999998878 y 1.0000001403, diferencia absoluta máxima `1.1920928955078125e-07` y diferencia L2 máxima `4.3145173072568673e-07`.

El modelo D1a se entrenó una vez con 2,950 pares históricos, 66 códigos, MNRL y negativos jerárquicos deterministas. No usó devset ni evalset para selección, early stopping o ajuste. Los 2,950 positivos normativos existían en el corpus; los negativos fueron 2,875 de mismo HS-4 y 75 de mismo capítulo.

## Métricas D1a

| Métrica | Resultado |
|---|---:|
| Top-1 | 0 / 1,056 = 0.000000 |
| Top-3 | 4 / 1,056 = 0.003788 |
| Top-5 | 36 / 1,056 = 0.034091 |
| Top-10 | 165 / 1,056 = 0.156250 |
| Top-50 | 323 / 1,056 = 0.305871 |
| Recall@100 | 365 / 1,056 = 0.345644 |
| MRR@100 | 0.032424 |
| Recall@200 | 383 / 1,056 = 0.362689 |
| MRR@200 | 0.032549 |
| HS6@100 / HS4@100 / Chapter@100 | 0.365530 / 0.873106 / 0.980114 |
| HS6@200 / HS4@200 / Chapter@200 | 0.388258 / 0.964015 / 1.000000 |

El salto frente a D0 es sustancial en Recall@100 (`0.003788` a `0.345644`), pero D1a no se presenta como réplica completa del artículo ni como prueba de una configuración óptima: se fijó una única configuración sin búsqueda contra eval.

## Riesgos y MCD

El histórico está concentrado en 28 DAM y conserva 457 grupos de descripciones normalizadas repetidas; los resultados requieren esa cautela. D1a adapta un modelo multilingüe a NANDINA-8 con un solo entrenamiento y no reproduce los datos, idioma, cobertura HS-6 ni la selección de base del paper.

MCD es técnicamente implementable: el modelo Transformer conserva dropout y el paper describe 50 pasadas, `avg_cos`, frecuencia Top-3 y reranking 0.8/0.2. Sin embargo, D1b requeriría una autorización separada y una decisión explícita sobre si se aplican esos parámetros del paper sin nueva selección local. No se ejecutó MCD en D1a.

## Artefactos

- `models/text2trade_mnrl_v0.2/` (modelo grande, no versionado automáticamente)
- `data/processed/indexes/text2trade_mnrl_nandina8_v0.2/` (índice grande, no versionado automáticamente)
- `outputs/training/text2trade_mnrl_v0.2/training_metadata.json`
- `outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json`
- `outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/strategy_comparison_a_b_c_d0_d1a_v0.2.csv`

Las rutas, tamaños y hashes SHA-256 de los artefactos locales se fijan en `docs/exp04_text2trade_mnrl_d1a_v02_reproducibility_manifest.json`. El modelo, vectores e índice permanecen fuera de Git y no usan Git LFS.
