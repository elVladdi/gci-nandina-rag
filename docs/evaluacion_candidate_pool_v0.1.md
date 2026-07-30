# Evaluacion candidate pool v0.1

## Objetivo de Fase 7A

La Fase 7A construye y evalua un pool combinado de candidatos NANDINA para medir si la NANDINA correcta queda contenida antes de pasar a re-ranking con LLM.

Esta fase no usa LLM, no usa Text2Trade, no cambia reglas mirando resultados del evalset y no modifica devset, evalset ni Excel fuente.

## Correccion metodologica

La primera version de Fase 7A reporto `Pool@100 = 0.2500` en evalset, pero ese valor no era la union real de los recuperadores. Medias el pool final `hierarchical_first`: primero agregaba 100 candidatos jerarquicos, luego agregaba dual y finalmente recortaba a 100. Ese cap descartaba candidatos utiles solo presentes en dual.

La correccion separa cuatro metricas:

- `hierarchical_at_K`: la NANDINA correcta aparece en Top-K de `BM25_hierarchical_v0.1`.
- `dual_at_K`: la NANDINA correcta aparece en Top-K de `BM25_dual_protected_top_5_backfill`.
- `union_oracle_at_K`: la NANDINA correcta aparece en la union de Top-K jerarquico y Top-K dual. No es ranking entregable.
- `final_pool_at_K`: la NANDINA correcta aparece en el pool final ordenado y recortado que recibiria el LLM.

Tambien se reportan equivalentes HS4 y HS2 para cada una de esas familias.

## Arquitectura evaluada

- Ranking documental principal: `BM25_hierarchical_v0.1`.
- Fuente auxiliar de expansion: `BM25_dual_protected_top_5_backfill`.
- Regla dual congelada: proteger Top-5 de `C_hs6_leaf`, completar con candidatos nuevos de `D_4d_hs6_leaf` y luego agregar el resto de `C_hs6_leaf`.
- `union_oracle`: diagnostico de cobertura maxima disponible por ambos recuperadores.
- `final_pool`: ranking efectivamente entregable al LLM.

## Estrategias final_pool

- `hierarchical_first`: comportamiento inicial; jerarquico primero y dual solo entra si queda espacio.
- `hierarchical_80_dual_backfill_20`: Top-80 jerarquico y hasta 20 candidatos nuevos del dual, completando con jerarquico si falta espacio.
- `hierarchical_70_dual_backfill_30`: Top-70 jerarquico y hasta 30 candidatos nuevos del dual, completando con jerarquico si falta espacio.

Estas reglas son predefinidas y simples. No se optimizaron mirando el evalset.

## Parametros usados

- `--hier-depth 100`.
- `--dual-depth 100`.
- `--pool-depths 10,20,50,100`.
- Devset: `data/processed/devset_validacion_intermedia.csv`.
- Evalset: `data/processed/evalset_v0.1.csv`.
- Outputs devset: `outputs/evaluation/candidate_pool_devset_v0.1/`.
- Outputs evalset: `outputs/evaluation/candidate_pool_evalset_v0.1/`.

## Metricas devset

| Estrategia | K | Hierarchical | Dual | Union oracle | Final pool |
| --- | ---: | ---: | ---: | ---: | ---: |
| hierarchical_first | 10 | 0.6154 | 0.6923 | 0.6923 | 0.6154 |
| hierarchical_first | 20 | 0.6154 | 0.6923 | 0.6923 | 0.6154 |
| hierarchical_first | 50 | 0.6923 | 0.6923 | 0.6923 | 0.6923 |
| hierarchical_first | 100 | 0.6923 | 0.7692 | 0.7692 | 0.6923 |
| hierarchical_80_dual_backfill_20 | 100 | 0.6923 | 0.7692 | 0.7692 | 0.7692 |
| hierarchical_70_dual_backfill_30 | 100 | 0.6923 | 0.7692 | 0.7692 | 0.7692 |

HS4/HS2 en devset a K=100:

| Estrategia | Union HS4 | Final HS4 | Union HS2 | Final HS2 |
| --- | ---: | ---: | ---: | ---: |
| hierarchical_first | 0.9231 | 0.9231 | 0.9231 | 0.9231 |
| hierarchical_80_dual_backfill_20 | 0.9231 | 0.9231 | 0.9231 | 0.9231 |
| hierarchical_70_dual_backfill_30 | 0.9231 | 0.9231 | 0.9231 | 0.9231 |

Aporte del dual en devset a profundidad 100:

| Categoria | Casos |
| --- | ---: |
| Solo hierarchical recupera la NANDINA correcta | 0 |
| Solo dual recupera la NANDINA correcta | 1 |
| Ambos recuperan la NANDINA correcta | 9 |
| Ninguno recupera la NANDINA correcta | 3 |
| Union real | 10/13 = 0.7692 |

## Metricas evalset

| Estrategia | K | Hierarchical | Dual | Union oracle | Final pool |
| --- | ---: | ---: | ---: | ---: | ---: |
| hierarchical_first | 10 | 0.1067 | 0.0850 | 0.1167 | 0.1067 |
| hierarchical_first | 20 | 0.1283 | 0.1100 | 0.1417 | 0.1283 |
| hierarchical_first | 50 | 0.2033 | 0.2133 | 0.2350 | 0.2033 |
| hierarchical_first | 100 | 0.2500 | 0.2700 | 0.2767 | 0.2500 |
| hierarchical_80_dual_backfill_20 | 100 | 0.2500 | 0.2700 | 0.2767 | 0.2667 |
| hierarchical_70_dual_backfill_30 | 100 | 0.2500 | 0.2700 | 0.2767 | 0.2650 |

HS4/HS2 en evalset a K=100:

| Estrategia | Union HS4 | Final HS4 | Union HS2 | Final HS2 |
| --- | ---: | ---: | ---: | ---: |
| hierarchical_first | 0.3100 | 0.2850 | 0.5417 | 0.4983 |
| hierarchical_80_dual_backfill_20 | 0.3100 | 0.2983 | 0.5417 | 0.5283 |
| hierarchical_70_dual_backfill_30 | 0.3100 | 0.2983 | 0.5417 | 0.5300 |

Aporte del dual en evalset a profundidad 100:

| Categoria | Casos |
| --- | ---: |
| Solo hierarchical recupera la NANDINA correcta | 4 |
| Solo dual recupera la NANDINA correcta | 16 |
| Ambos recuperan la NANDINA correcta | 146 |
| Ninguno recupera la NANDINA correcta | 434 |
| Union real | 166/600 = 0.2767 |

La union real se calcula como `146 + 16 + 4 = 166` casos. El `final_pool@100` inicial de `hierarchical_first` queda en `150/600 = 0.2500`, porque descarta los 16 casos solo-dual al llenar primero los 100 espacios con candidatos jerarquicos.

## Mejor estrategia entregable

La mejor estrategia exacta a K=100 es `hierarchical_80_dual_backfill_20`:

- Devset: `final_pool@100 = 0.7692`, igual a `union_oracle@100`.
- Evalset: `final_pool@100 = 0.2667`, frente a `0.2500` de `hierarchical_first`.
- Evalset HS4@100: `0.2983`, frente a `0.2850`.
- Evalset HS2@100: `0.5283`, frente a `0.4983`.

`hierarchical_70_dual_backfill_30` mejora HS2 levemente (`0.5300`), pero baja exactitud a `0.2650`. Por criterio principal exacto, queda preferida `hierarchical_80_dual_backfill_20`.

## Evidencia documental

`candidate_pool.csv` incluye `evidence_text` cuando el indice BM25 expone texto documental en el hit. La evidencia se copia desde el indice; no se inventa ni se completa manualmente. Si una futura variante de indice no expone texto, el campo debe permanecer vacio y esa limitacion debe documentarse.

## Decision metodologica

La correccion confirma que el dual protegido aporta cobertura real y que reservar espacio en el pool final mejora lo entregable al LLM. Aun asi, incluso el techo `union_oracle@100 = 0.2767` en evalset sigue siendo bajo para una Fase 7B sustantiva orientada a mejorar exactitud NANDINA8.

Se puede pasar a una Fase 7B diagnostica/acotada usando `hierarchical_80_dual_backfill_20`, dejando explicito que el LLM no podra corregir los casos donde la NANDINA correcta no esta en el pool. La prioridad metodologica sigue siendo mejorar recuperacion documental antes de depender del re-ranking.

## Limitaciones

- El evalset esta concentrado en regimen 10; no generalizar a otros regimenes.
- La cobertura exacta Top-100 sigue siendo baja para re-ranking cerrado.
- Hay 434 casos de evalset donde la NANDINA correcta no aparece ni en Top-100 de hierarchical ni en Top-100 dual.
- `union_oracle` no es un ranking entregable al LLM.
- `evidence_text` depende del texto expuesto por el indice BM25, no de una docstore enriquecida externa.
- No se evaluo calidad de justificacion, solo presencia del candidato correcto en el pool.

## Artefactos generados

- `src/experiments/build_candidate_pool.py`.
- `outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool.csv`.
- `outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool_metrics.json`.
- `outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool_summary.md`.
- `outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool_case_summary.csv`.
- `outputs/evaluation/candidate_pool_devset_v0.1/candidate_pool_source_overlap.csv`.
- `outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool.csv`.
- `outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool_metrics.json`.
- `outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool_summary.md`.
- `outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool_case_summary.csv`.
- `outputs/evaluation/candidate_pool_evalset_v0.1/candidate_pool_source_overlap.csv`.
