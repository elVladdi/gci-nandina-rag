# EXP-04 Fase F: inventario de integración histórico-normativa v0.2

## Arquitectura previa y decisión aplicable

La implementación previa relevante para asociar evidencia a un Top-3 no es el pool híbrido de Fase 9B, sino `src/experiments/build_llm_explanation_top3_sample.py` y su variante de auditoría. Esos constructores cargan el Top-3 ya emitido por el ranking histórico y hacen un índice por código sobre `corpus_nandina_hierarchical_v0.1.jsonl`; para cada candidato usan `_normative_context(code, normative_index.get(code), rank)`.

La operación histórica es por tanto **CODE-TO-NORMATIVE-EVIDENCE LOOKUP**: `candidate NANDINA-8 -> documento normativo del mismo código`. No es recuperación de descripción comercial a código, no consulta BM25 por la query y no toma una decisión según métricas del evalset.

El corpus jerárquico lleva el sufijo de versión `v0.1`, pero es el corpus canónico cuyo hash `f389ae6c...` ya fue congelado y consumido por EXP-04 Fase C sobre eval v0.2. Se usa como fuente documental normativa, no como split, resultados o evalset v0.1.

## Implementaciones auditadas

| Artefacto | Hallazgo | Aplicación en Fase F |
|---|---|---|
| `build_hybrid_historical_normative_pool.py` | Inserta candidatos normativos y contempla RRF/backfill; cambia el ranking. | Excluido: viola la invariante de ranking. |
| `build_hybrid_pool_data_aduanas.py` | Construye pools híbridos y selecciona estrategia. | Excluido: Fase F no selecciona pools ni candidatos. |
| `build_llm_explanation_top3_sample.py` | Consume Top-3 histórico fijo y adjunta evidencia por lookup exacto de código. | Regla preservada, sin payload ni LLM. |
| `build_llm_explanation_top3_audit_sample.py` | Refuerza que el label no entra al payload y que el orden está bloqueado. | Control de no-leakage e invariancia adoptado. |
| Fase E candidate pools / D1a | Comparadores OE2, no fuente histórica de evidencia por candidato. | Excluidos. |

## Top-3, precedentes y evidencia

La única fuente de candidatos es `historical_results.csv` de Fase A, hash `c350b63e...`. Para cada `case_id` se copian exactamente los ranks 1, 2 y 3, su código, score y orden. La Fase A construyó cada código histórico deduplicado seleccionando el primer precedente en el orden BM25, registrado como `candidate_case_id`, `candidate_id_unico`, `candidate_history_rank`, descripción y score. Fase F conserva ese único precedente por slot y lo completa por lookup en `data_aduanas_historico_clase87_v0.2.csv`; nunca usa dev ni eval como precedente.

La evidencia normativa se obtiene por lookup directo del código del candidato en el corpus jerárquico. El documento exacto aporta `doc_id`, fuente, versión, tipo, línea/página y contexto. HS6, HS4 y capítulo se reportan solo cuando el registro conserva explícitamente esos campos parentales. No hay fallback de recuperación, no se inventa texto, y un padre no se etiqueta como evidencia NANDINA-8 exacta.

## Invariantes y fases posteriores

El artefacto F solo adjunta columnas: no suma ni mezcla scores, no agrega candidatos, no cambia posiciones y no llama LLM. La etiqueta real se usa únicamente después para métricas de presencia Top-3 y nunca en selección de candidato, precedente ni evidencia.

Fase E permanece congelada y sus pools no se emplean. D1a no se emplea. Fase G conserva como pendiente cualquier reranker diagnóstico; no se construyen prompts, RAG ni explicaciones en Fase F.
