# G3-F02 — Registro maestro de métricas y poblaciones

**Estado:** `PROSPECTIVE / NOT_AUTHORIZED`

## Objetivo

Construir una única matriz de métricas/resultados autorizados para impedir mezclas de particiones, versiones o outputs supersedidos.

## Obligatorio

- usar solo fuentes congeladas por G3-F01;
- mapear cada resultado a experimento, commit, dataset, unidad, N, agrupamiento, métrica y versión;
- distinguir descriptivos, estimandos inferenciales y controles/diagnósticos;
- para 0B-05C usar únicamente Attempt06 corregido;
- registrar H100 como referencia donde corresponda;
- para EXP11A conservar H25/H50/H75/H100 y diseño independiente complete-DAM con H50 D1/D2;
- para EXP11B conservar H150/H200 y sus réplicas aprobadas;
- excluir EXP12 retrieval por no ejecución.

## Outputs

- `outputs/analysis/group3/g3_metric_population_registry_v0.1.csv`
- `outputs/analysis/group3/g3_metric_population_registry_v0.1.json`
- ledger de hashes de esos outputs.

## PASS

Cero filas sin procedencia; cero resultados supersedidos presentados como vigentes; cero mezcla de EVAL incompatible.

**Siguiente:** G3-F03.
