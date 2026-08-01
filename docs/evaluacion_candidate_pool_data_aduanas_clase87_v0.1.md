# Evaluacion candidate pool normativo data_aduanas clase 87 v0.1

## Objetivo

Esta actualizacion de Fase 7A construye y evalua un candidate pool normativo para `data_aduanas` clase 87. El objetivo es medir cobertura y trazabilidad normativa con los recuperadores BM25 ya definidos, dejando este bloque como respaldo frente al pool historico de Fase 9.

La corrida no usa historico real como fuente de recuperacion, no usa Dense, no usa LLM, no ejecuta Ollama, no usa Text2Trade y no usa APIs remotas.

## Alcance

- Evalset: `data/processed/data_aduanas_evalset_clase87_v0.1.csv`.
- Casos: 1,006.
- Consulta: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta esperada: `NANDINA`.
- Clase esperada: `87`.
- Output regenerable: `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/`.

El historico real `data/processed/data_aduanas_historico_clase87_v0.1.csv` se conserva solo como referencia de diseno para Fase 9. No se usa para recuperar candidatos en esta Fase 7A normativa.

## Fuentes normativas

- `BM25_hierarchical_v0.1`: ranking normativo jerarquico principal.
- `BM25_dual_protected_top_5_backfill`: fuente dual auxiliar construida con `C_hs6_leaf` y `D_4d_hs6_leaf`.

No se incorpora `BM25_flat_current` al pool final. Sus metricas quedan como referencia en Fase 4/Fase 6B-6C clase 87, pero esta actualizacion se concentra en el bloque normativo jerarquico + dual heredado de Fase 7A.

## Estrategias evaluadas

- `hierarchical_only`: solo Top-K jerarquico.
- `dual_only`: solo Top-K dual protegido.
- `hierarchical_first_100`: primeros 100 lugares jerarquicos; a Top-200 se completa con dual como backfill normativo.
- `hierarchical_80_dual_backfill_20`: primeros 100 lugares con Top-80 jerarquico y hasta 20 dual nuevos; a Top-200 se completa con dual y jerarquico remanentes.
- `hierarchical_70_dual_backfill_30`: primeros 100 lugares con Top-70 jerarquico y hasta 30 dual nuevos; a Top-200 se completa con dual y jerarquico remanentes.

`union_oracle` se reporta como techo diagnostico: mide si la NANDINA correcta aparece en la union de Top-K jerarquico y Top-K dual, sin imponer un orden entregable ni un recorte destructivo posterior. No es una regla operativa.

## Metricas exactas

| Estrategia | Pool@10 | Pool@20 | Pool@50 | Pool@100 | Pool@200 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `hierarchical_only` | 0.0497 | 0.0517 | 0.0626 | 0.3449 | 0.6213 |
| `dual_only` | 0.0487 | 0.0517 | 0.0716 | 0.1948 | 0.5934 |
| `hierarchical_first_100` | 0.0497 | 0.0517 | 0.0626 | 0.3449 | 0.5895 |
| `hierarchical_80_dual_backfill_20` | 0.0497 | 0.0517 | 0.0626 | 0.3459 | 0.6272 |
| `hierarchical_70_dual_backfill_30` | 0.0497 | 0.0517 | 0.0626 | 0.3489 | 0.6272 |
| `union_oracle` diagnostico | 0.0497 | 0.0527 | 0.0805 | 0.3658 | 0.6372 |

La diferencia clave a Top-100 es:

- `hierarchical_only`: 347/1006 = 0.3449.
- `union_oracle@100`: 368/1006 = 0.3658.
- mejor `final_pool@100`: `hierarchical_70_dual_backfill_30`, 351/1006 = 0.3489.

Por tanto, el dual aporta cobertura potencial, pero el ordenamiento y recorte del pool final todavia no capturan todo el techo de la union.

## Metricas jerarquicas

| Estrategia | Partida@100 | Sub Partida@100 | Clase@100 | Partida@200 | Sub Partida@200 | Clase@200 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `hierarchical_only` | 0.5865 | 0.5209 | 0.7386 | 0.7048 | 0.6392 | 0.8628 |
| `dual_only` | 0.5905 | 0.3708 | 0.7753 | 0.7038 | 0.6183 | 0.8777 |
| `hierarchical_first_100` | 0.5865 | 0.5209 | 0.7386 | 0.7008 | 0.6133 | 0.8748 |
| `hierarchical_80_dual_backfill_20` | 0.5865 | 0.5219 | 0.7406 | 0.7107 | 0.6451 | 0.8628 |
| `hierarchical_70_dual_backfill_30` | 0.5885 | 0.5268 | 0.7445 | 0.7107 | 0.6451 | 0.8628 |

La cobertura jerarquica confirma que el bloque normativo conserva utilidad como trazabilidad: incluso cuando no acierta NANDINA8, aporta senal de partida, subpartida o clase.

## Aporte dual

A Top-100:

| Categoria | Casos |
| --- | ---: |
| Solo hierarchical recupera NANDINA8 | 172 |
| Solo dual recupera NANDINA8 | 21 |
| Ambos recuperan NANDINA8 | 175 |
| Ninguno recupera NANDINA8 | 638 |
| Union real | 368/1006 = 0.3658 |

A Top-200:

| Categoria | Casos |
| --- | ---: |
| Solo hierarchical recupera NANDINA8 | 44 |
| Solo dual recupera NANDINA8 | 16 |
| Ambos recuperan NANDINA8 | 581 |
| Ninguno recupera NANDINA8 | 365 |
| Union real | 641/1006 = 0.6372 |

Frente a `hierarchical_only`, los pools mixtos muestran:

| Estrategia | Rescates final@100 | Perdidas final@100 | Rescates final@200 | Perdidas final@200 |
| --- | ---: | ---: | ---: | ---: |
| `hierarchical_first_100` | 0 | 0 | 13 | 45 |
| `hierarchical_80_dual_backfill_20` | 1 | 0 | 6 | 0 |
| `hierarchical_70_dual_backfill_30` | 7 | 3 | 6 | 0 |

`hierarchical_70_dual_backfill_30` es el mejor pool entregable a Top-100. A Top-200, `hierarchical_80_dual_backfill_20` y `hierarchical_70_dual_backfill_30` empatan en exactitud (`0.6272`) y en las metricas jerarquicas principales reportadas.

## Lectura metodologica

La actualizacion confirma que la Fase 7A normativa mejora la cobertura profunda respecto al BM25 plano clase 87 y preserva trazabilidad arancelaria, pero no alcanza cobertura suficiente para ser fuente principal de candidatos. El mejor `final_pool@100` normativo llega a 0.3489 y el techo `union_oracle@100` llega a 0.3658.

Top-200 mejora de forma sustantiva (`final_pool@200 = 0.6272`), pero aun queda lejos de la cobertura esperada para un flujo operativo cerrado. Esto refuerza la decision metodologica ya abierta por Fase 9: el historico real debe dominar cuando haya precedente, mientras el bloque normativo debe funcionar como backfill, respaldo y explicabilidad.

## Decision

Para respaldo/trazabilidad normativa clase 87:

- Si se requiere un pool de 100 candidatos, usar `hierarchical_70_dual_backfill_30`.
- Si se permite un pool de 200 candidatos, `hierarchical_80_dual_backfill_20` y `hierarchical_70_dual_backfill_30` empatan en exactitud; se puede conservar `hierarchical_80_dual_backfill_20` como opcion mas conservadora por continuidad con Fase 7A historica.

Ninguna variante normativa se promueve como fuente principal frente al futuro pool historico de Fase 9. No corresponde mezclar historico real dentro de esta Fase 7A; esa combinacion pertenece a Fase 9B.

## Artefactos

Versionables:

- `src/experiments/build_candidate_pool_data_aduanas.py`.
- `docs/evaluacion_candidate_pool_data_aduanas_clase87_v0.1.md`.

Regenerables e ignorados por Git:

- `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/candidate_pool.csv`.
- `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/candidate_pool_case_summary.csv`.
- `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/candidate_pool_metrics.json`.
- `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/candidate_pool_summary.md`.
- `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/source_contribution.csv`.
- `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/rescue_loss_cases.csv`.

`candidate_pool.csv` es grande porque contiene candidatos por caso y estrategia hasta Top-200 con evidencia normativa disponible. No debe versionarse.

## Controles

- No se ejecuto LLM.
- No se ejecuto Ollama.
- No se ejecuto Text2Trade.
- No se ejecuto Dense.
- No se usaron APIs remotas.
- No se uso historico real como fuente de recuperacion.
- No se modificaron los splits `data_aduanas` clase 87.
- No se modificaron `evalset_v0.1.csv`, `evalset_v0.1_metadata.json` ni `devset_validacion_intermedia.csv`.
