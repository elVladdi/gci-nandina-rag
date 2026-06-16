# Evaluacion BM25 dual backfill evalset v0.1

## Objetivo

Esta fase valida de forma controlada la arquitectura `BM25_dual_protected_top_5_backfill` sobre el evalset final v0.1. La estrategia `protected_top_5_backfill` fue seleccionada previamente usando solo el devset de 13 casos; en esta fase no se ajustaron reglas despues de observar resultados del evalset.

No se ejecuto LLM, no se ejecuto Text2Trade y no se modificaron evalset, devset ni Excel fuente.

## Arquitectura evaluada

- Indice de precision: `C_hs6_leaf`, basado en HS6 + NANDINA8.
- Indice de recall: `D_4d_hs6_leaf`, equivalente jerarquico 4D + HS6 + NANDINA8.
- Fusion: `protected_top_5_backfill`.
- Regla congelada: proteger el Top-5 del indice de precision, completar con candidatos nuevos del indice jerarquico y, finalmente, conservar candidatos restantes del indice de precision si queda espacio.

## Metodos comparados

- `BM25_flat_current`.
- `C_hs6_leaf`.
- `BM25_hierarchical_v0.1`.
- `BM25_dual_protected_top_5_backfill`.

## Metricas globales

| Metodo | Casos | Con resultados | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | HS4@10 | HS2@10 | not_found | sin match Top-10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25_flat_current | 600 | 584 | 0.0050 | 0.0433 | 0.0483 | 0.0517 | 0.0290 | 0.1450 | 0.1633 | 0.1933 | 0.3800 | 502 | 569 |
| C_hs6_leaf | 600 | 600 | 0.0233 | 0.0317 | 0.0367 | 0.0400 | 0.0331 | 0.1267 | 0.1650 | 0.1667 | 0.3183 | 501 | 576 |
| BM25_hierarchical_v0.1 | 600 | 600 | 0.0283 | 0.0583 | 0.0883 | 0.1067 | 0.0524 | 0.2033 | 0.2500 | 0.1533 | 0.2433 | 450 | 536 |
| BM25_dual_protected_top_5_backfill | 600 | 600 | 0.0233 | 0.0317 | 0.0367 | 0.0850 | 0.0406 | 0.2133 | 0.2700 | 0.1850 | 0.3117 | 438 | 549 |

## Comparacion contra baselines

| Baseline | Ganados | Perdidos | Sin cambio | Ganancia media rank | Perdida media rank | Ambos fallan Top-10 | Dual rescata Top-10 | Baseline acierta Top-10 y dual no |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25_flat_current | 130 | 36 | 434 | 42.23 | 33.83 | 542 | 27 | 7 |
| C_hs6_leaf | 126 | 27 | 447 | 43.56 | 27.59 | 549 | 27 | 0 |
| BM25_hierarchical_v0.1 | 69 | 76 | 455 | 26.48 | 12.32 | 530 | 6 | 19 |

## Analisis por familias

Se generaron analisis por `hs2_ref`, `hs4_ref` y `regimen`, filtrando grupos con al menos 5 casos. Los archivos reportan cantidad de casos, Top-10 y MRR para BM25 plano y dual protegido, mas la diferencia dual menos plano.

El evalset esta concentrado casi totalmente en regimen 10, por lo que el analisis por regimen debe interpretarse como una alerta de alcance y no como evidencia transversal para otros regimenes.

## Rescates y deterioros

Frente a BM25 plano, el dual protegido genera 27 rescates Top-10 que BM25 plano no recuperaba en Top-10, pero tambien pierde 7 casos donde BM25 plano acertaba Top-10 y el dual no. En comparacion con `C_hs6_leaf`, el dual rescata 27 casos Top-10 sin perder aciertos Top-10 de ese baseline. Frente al jerarquico v0.1, el dual rescata 6 casos Top-10, pero pierde 19 aciertos Top-10 del jerarquico.

Los archivos regenerables de rescates, deterioros, fallos compartidos y muestra de errores quedan bajo `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/`.

## Codigos criticos del devset

El script revisa si los codigos criticos observados en devset aparecen dentro del evalset. En esta corrida no encontro casos asociados a esos codigos; el archivo `dual_evalset_devset_critical_codes.csv` queda generado con encabezado y sin filas de casos.

## Decision metodologica

`BM25_dual_protected_top_5_backfill` no debe adoptarse como ranking inicial principal. El mejor ranking inicial documental segun evalset es `BM25_hierarchical_v0.1`, porque supera al dual protegido en Top-10 y MRR.

El dual protegido no se descarta: queda como variante auxiliar para ampliar el pool de candidatos porque obtiene el mejor Recall@100. La decision operativa de cierre es:

- Ranking documental principal: `BM25_hierarchical_v0.1`.
- Pool auxiliar para re-ranking posterior: union de candidatos de `BM25_hierarchical_v0.1` + `BM25_dual_protected_top_5_backfill`, idealmente a profundidad 50 o 100.
- Etapa LLM pendiente: no debe buscar NANDINAS desde cero; debe reordenar y justificar sobre el pool recuperado y con evidencia documental.

Esta decision no deriva de una optimizacion posterior sobre evalset. Es una lectura metodologica de validacion controlada de la variante congelada.

## Outputs regenerables

- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_results.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_metrics.json`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_summary.md`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_comparison_vs_flat.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_comparison_vs_c_hs6.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_comparison_vs_hierarchical.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_family_analysis_hs2.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_family_analysis_hs4.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_family_analysis_regimen.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_top_rescues.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_top_deteriorations.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_all_methods_fail.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_failure_sample.csv`
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_devset_critical_codes.csv`

`outputs/` ya esta ignorado por Git, por lo que estos archivos permanecen como salidas regenerables.

## Limitaciones

- Evalset concentrado casi totalmente en regimen 10.
- Evaluacion aun sin LLM de re-ranking ni justificacion.
- BM25 dual solo evalua ranking inicial documental.
- La comparacion es valida para la variante congelada; no debe usarse para ajustar reglas nuevas mirando el evalset.

## Comando reproducible

```powershell
python -m src.experiments.evaluate_bm25_dual_backfill_evalset
```
