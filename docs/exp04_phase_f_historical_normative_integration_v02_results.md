# EXP-04 Fase F: integración histórico-normativa v0.2

## Resultado y definición

EXP-04 Fase F ejecuta una integración determinística de evidencia, no un clasificador. La definición congelada es **CODE-TO-NORMATIVE-EVIDENCE LOOKUP**: para cada código del Top-3 histórico de Fase A se consulta directamente el documento de ese mismo NANDINA-8 en el corpus jerárquico. Esto es distinto de la recuperación query-to-code de las fases B--E.

La fuente normativa es `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`, SHA-256 `f389ae6c303279cfea23697cbedb3315a5254254c2efc2450cf28f81243df175`, corpus documental canónico ya congelado en Fase C. La fuente no se eligió por las métricas de Fase E. Fase E y D1a no intervienen en la construcción.

El ranking de entrada es exclusivamente `historical_results.csv` de Fase A, SHA-256 `c350b63e0180a4c28573d2626c76d030308913b690c524d2d62ea439cf34a6c8`. Para cada caso se copian los ranks 1, 2 y 3, con sus códigos y scores literales. La evidencia normativa se agrega como columnas; no hay score normativo, fusión, inserción ni reordenamiento.

## Precedentes y trazabilidad

Cada slot conserva un precedente de la fuente histórica v0.2: la fila que Fase A seleccionó antes de deduplicar el código NANDINA-8. Se documentan `candidate_case_id`, `id_unico`, DAM, serie, código, descripción, score y `candidate_history_rank`. El lookup contra `data_aduanas_historico_clase87_v0.2.csv` confirmó que los 3,168 precedentes pertenecen exclusivamente al split `historico`; no se usó dev ni eval.

Cada documento normativo registra `doc_id`, fuente, versión, tipo, código, página, línea, referencia textual y hash de corpus. El lookup no tiene fallback: si faltara el documento exacto, se reportaría como ausente; una evidencia de padre jamás se promueve a evidencia exacta.

## Invariantes

| Control | Resultado |
|---|---:|
| Casos | 1,056 |
| Slots Top-3 | 3,168 |
| Ranking histórico invariante | 1,056/1,056 (1.000000) |
| Top-3 código/posición/score invariante | 3,168/3,168 (1.000000) |
| Hash histórico antes/después | `c350b63e...` / `c350b63e...` |
| Candidatos normativos insertados | 0 |
| Candidatos históricos removidos | 0 |
| Score normativo afecta orden | no |

`integration_compatibility.json` confirma mismo eval hash, mismos casos/etiquetas, tres candidatos históricos por caso y `compatible = true`.

## Cobertura documental

| Métrica | Resultado |
|---|---:|
| Evidencia NANDINA-8 exacta | 3,168/3,168 (1.000000) |
| Evidencia HS6 explícita | 2,168/3,168 (0.684343) |
| Evidencia HS4 explícita | 3,168/3,168 (1.000000) |
| Evidencia Chapter explícita | 3,168/3,168 (1.000000) |
| Top-1 con evidencia exacta | 1,056/1,056 |
| Top-2 con evidencia exacta | 1,056/1,056 |
| Top-3 con evidencia exacta | 1,056/1,056 |
| Casos con evidencia exacta 3/3, 2/3, 1/3, 0/3 | 1,056; 0; 0; 0 |
| Cobertura de precedente | 3,168/3,168 (1.000000) |
| Trazabilidad completa | 3,168/3,168 (1.000000) |

El Top-3 histórico contiene la referencia en 709 casos y no la contiene en 347. Ambos grupos tienen 100% de evidencia exacta por slot, lo cual mide disponibilidad documental de los candidatos emitidos, no precisión de clasificación. La tabla de candidatos sin evidencia exacta está vacía salvo por su encabezado.

## Auditorías de alcance

El label-leakage audit confirma que la etiqueta real no intervino en la selección de candidato, precedente, evidencia, orden ni fallback; solo se leyó después para la métrica de presencia de referencia en Top-3. No se ejecutaron LLM, RAG, reranker, candidate pools, D1a ni Fase G.

El corpus documental conserva un nombre legado `v0.1`, pero no se usó ningún evalset, ranking, split ni output experimental v0.1 como entrada. La excepción está explícita porque es el mismo corpus/hash ya congelado en Fase C y la arquitectura histórica de evidencia lo identifica como fuente canónica.

## Dictamen HE3-F y Gate F

**HE3-F — INTEGRACIÓN HISTÓRICO-NORMATIVA: SUPPORTED.** El ranking histórico se preservó completamente y se adjuntó evidencia normativa exacta, precedente histórico y provenance reconstruible a todos los slots. Esto no evalúa ni autoriza un reranker, una explicación ni una clasificación final.

**HE3 GLOBAL PENDING EXP-04 FASE G / EXP-06 DIAGNOSTIC LLM RERANKER.**

**GATE F APROBADO** técnicamente: los invariantes, compatibilidad, trazabilidad, no-leakage y pruebas se cumplen; el cierre permanece sujeto a revisión antes de cualquier reranker diagnóstico.

Limitación: la cobertura documental exacta no demuestra por sí misma adecuación jurídica ni calidad de una explicación futura. La cobertura HS6 de 68.43% refleja la presencia explícita de ese padre en el corpus jerárquico, no ausencia del código NANDINA-8 exacto.
