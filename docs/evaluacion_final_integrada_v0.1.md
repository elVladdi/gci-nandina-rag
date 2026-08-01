# Evaluacion final integrada v0.1

Generado por `src/analysis/build_integrated_final_evaluation.py` en `2026-08-01T20:39:55+00:00`.

## Resumen ejecutivo

La evidencia integrada respalda una arquitectura offline donde el recuperador historico real domina el ranking operativo para `data_aduanas` clase 87, mientras el corpus normativo jerarquico queda como respaldo documental, trazabilidad y backfill. El LLM no queda respaldado como re-ranker porque degrada Top-1/MRR en la prueba diagnostica. Si se usa LLM, el rol defendible es explicar de forma auditable un Top-3 fijo ya recuperado, con revision experta.

## Tabla comparativa integrada

| method_name | method_type | n_evaluated | top_1 | top_10 | recall_at_100 | recall_at_200 | mrr | auditability_score | methodological_decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BM25 normativo plano clase 87 | normativo | 1006 | 0.0229 | 0.0467 | 0.0626 | no evaluado | 0.0312 | no evaluado | Baseline auditable de referencia; no se adopta como recuperador principal. |
| Dense Text2Trade clase 87 | denso | 1006 | 0.0 | 0.0 | 0.001 | no evaluado | 0.0 | no evaluado | No se incorpora al pipeline de recuperacion exacta. |
| BM25 jerarquico v0.1 clase 87 | normativo | 1006 | 0.0249 | 0.0497 | 0.3449 | no evaluado | 0.0385 | no evaluado | Se conserva como recuperador normativo auxiliar de trazabilidad. |
| BM25 dual protegido clase 87 | normativo | 1006 | 0.0239 | 0.0487 | 0.1948 | no evaluado | 0.034 | no evaluado | Se conserva solo como fuente auxiliar de cobertura profunda. |
| Candidate pool normativo clase 87 | normativo | 1006 | no evaluado | 0.0497 | 0.3489 | 0.6292 | no comparable | no evaluado | Queda como respaldo documental y trazabilidad, no como fuente principal. |
| Recuperacion historica real clase 87 | historico | 1006 | 0.8628 | 0.9801 | 1.0 | no evaluado | 0.9062 | no evaluado | Debe dominar como recuperador cuando existe soporte historico. |
| Pool hibrido historico + normativo clase 87 | hibrido | 1006 | 0.8628 | 0.9801 | 1.0 | 1.0 | 0.9062 | no evaluado | Estrategia recomendada: historico primero con backfill normativo si falta codigo. |
| LLM re-ranker sobre pool hibrido | LLM re-ranking | 20 | 0.2 | 0.5 | no evaluado | no evaluado | 0.3083 | no evaluado | Resultado negativo; no escalar a Fase 9C-B. |
| LLM explicacion Top-3 auditable | LLM explicacion | 50 | no evaluado | no evaluado | no evaluado | no evaluado | no evaluado | 0.952 | Pasa como explicador auditable del Top-3 fijo, no como recuperador ni re-ranker. |
| Revision cualitativa 10C | LLM explicacion | 10 | no evaluado | no evaluado | no evaluado | no evaluado | no evaluado | 0.9533 | Confirma trazabilidad formal y utilidad humana con cautelas de tono/evidencia. |
| Mejora de ficha 10D | LLM explicacion | no comparable | no evaluado | no evaluado | no evaluado | no evaluado | no evaluado | no evaluado | Mejora el diseno auditable sin regenerar fichas ni cambiar metricas. |

## Validacion de hipotesis

| hypothesis | status | quantitative_evidence | evidence_phase |
| --- | --- | --- | --- |
| Mejora de recuperacion | respaldada | Historico Recall@100=1.0 y Top-1=0.8628; hibrido Recall@100=1.0 frente a pool normativo Recall@100=0.3489. | Fases 7A, 9A y 9B |
| Utilidad del banco historico | respaldada | Historico real: Top-10=0.9801, Recall@100=1.0, MRR=0.9062. | Fase 9A y Fase 10B |
| Utilidad del corpus normativo jerarquico | parcialmente respaldada | Pool normativo: Recall@100=0.3489 y Clase@100=0.7445; bajo Top-10=0.0497. | Fases 6B/6C, 7A, 9B y 10B |
| LLM como re-ranker | no respaldada | LLM re-ranker: Top-1=0.2 y MRR=0.3083; degrada frente al ranking original. | Fase 9C-A |
| LLM como generador de explicacion auditable | respaldada | JSON valido=1.0, ranking preservado=1.0, score auditabilidad=0.952. | Fases 10B, 10C y 10D |
| Trazabilidad/auditabilidad del enfoque RAG | respaldada | Evidencia historica citada=1.0; evidencia normativa citada=1.0. | Fases 9B, 10B, 10C y 10D |

## Decisiones experimentales

| order | phase | tested | result | methodological_decision |
| --- | --- | --- | --- | --- |
| 1 | Fase 4 | BM25 normativo plano clase 87 | Top-10 bajo y Recall@100=0.0626. | Usarlo como baseline auditable, no como recuperador principal. |
| 2 | Fase 5 | Dense Text2Trade clase 87 | Exactitud NANDINA8 practicamente nula; Recall@100=0.0010. | Descartar como componente exacto en esta fase. |
| 3 | Fase 6B/6C | BM25 jerarquico y dual protegido | Mejoran cobertura normativa amplia, pero no ranking temprano suficiente. | Conservar como trazabilidad/backfill normativo. |
| 4 | Fase 7A | Candidate pool normativo | Mejor pool normativo alcanza Recall@100=0.3489 y Recall@200=0.6292. | Mantener como respaldo documental frente al futuro bloque historico. |
| 5 | Fase 9A | Recuperacion historica real | Top-1=0.8628, Top-10=0.9801, Recall@100=1.0000. | Promover historico como fuente dominante. |
| 6 | Fase 9B | Pool hibrido historico + normativo | Conserva metricas historicas y agrega backfill normativo sin degradar. | Recomendar historico primero con backfill normativo si falta codigo. |
| 7 | Fase 9C-A | LLM como re-ranker | Top-1 y MRR degradan; ganados=0, perdidos=4. | No escalar re-ranking; usar LLM despues solo para explicacion. |
| 8 | Fase 10B | LLM como explicador Top-3 auditable | JSON valido, ranking preservado y citas de evidencia en 50/50. | Aceptar rol de explicador auditable controlado. |
| 9 | Fases 10C/10D | Revision cualitativa y mejora de ficha | Utilidad confirmada con cautelas sobre norma generica, predominio historico y tono. | Reforzar prompt, rubrica, formato y necesidad de revision experta. |

## Controles de alcance

- No se reentrenan modelos.
- No se ejecuta LLM, Ollama, OpenAI ni APIs remotas.
- No se modifican datos fuente, splits, Excel original ni outputs historicos.
- Las metricas ausentes o no comparables se marcan como `no evaluado` o `no comparable`.

## Principales hallazgos

- El historico real clase 87 alcanza `Recall@100 = 1.0000`, `Top-1 = 0.8628` y `MRR = 0.9062`.
- El hibrido recomendado conserva las metricas historicas y agrega respaldo normativo sin desplazar el ranking temprano.
- El pool normativo mejora la trazabilidad, pero no compite con el historico como fuente principal.
- Dense Text2Trade no aporta exactitud exacta NANDINA8 en este alcance.
- El LLM como re-ranker queda descartado; como explicador Top-3 auditable queda respaldado.

## Limites del experimento

- La evaluacion principal clase 87 no es comparable de forma pareada con el evalset historico de 600 casos.
- El desempeno historico presupone soporte en el banco de precedentes; faltan particiones temporales y codigos ausentes.
- La evidencia normativa aporta trazabilidad, pero no reemplaza revision juridica ni clasificacion oficial.
- La prueba de LLM re-ranker es diagnostica y pequena, aunque suficiente para no escalar dentro de este piloto.
- La explicacion LLM se evalua como auditabilidad del Top-3 fijo, no como exactitud de clasificacion.

## Pendiente para cierre de reproducibilidad

- Lockfile o contenedor reproducible de dependencias.
- Registro externo versionado por checksum para artefactos pesados.
- Validacion temporal o externa para medir generalizacion del banco historico.
- Eventual corrida 10E con prompt v0.3 si se decide validar la ficha mejorada.
- Politica final de preservacion de outputs regenerables fuera de Git.
