# EXP-04 Fase J: inventario de controles automaticos HE4 v0.2

## Alcance

Fase J valida deterministamente los artefactos congelados de H/I. No llama modelos, no hace retrieval, no regenera ni repara respuestas, no aplica la rubrica cualitativa y no inicia Fase K ni EXP-10.

## Validadores historicos auditados

- `src/configs/he4_explainer_schema_v0.2.json`: campos raiz, cardinalidad de tres candidatos, ranks 1/2/3, restricciones duras y umbrales agregados congelados.
- `src/llm/explain_top3_nandina_prompt_v0.2.md`: estructura exacta, Top-3 en orden, codigos cerrados, IDs de evidencia, comparacion y advertencia.
- `src/experiments/evaluate_llm_explanation_top3_audit_sample.py`: validador v0.1 enlazado por el schema; sus controles deterministas se trasladan sin cambiar el criterio.
- `docs/evaluacion_llm_explicacion_top3_sample_v0.1.md` y `docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md`: documentan los controles anti-invencion y los umbrales agregados.

## Clasificacion de controles

| Clase | Controles |
| --- | --- |
| A: preespecificado y automatico | JSON/objeto, campos y tipos estructurales, tres candidatos, ranks y orden Top-3, cierre de codigos, ausencia de codigos externos, `candidate_id_unico`, `evidence_id`, comparacion, advertencia final, regla de advertencia normativa generica, prohibicion literal de clasificacion oficial. |
| B: tecnico de portabilidad | SHA-256 H/I, identidad raw/parsed, conteos 50/150, provenance por `case_id`/`input_hash`, distincion determinista entre referencia inexistente y fuera de contexto, inventario de campos reservados explicitamente filtrados. |
| C: post-hoc o cualitativo diferido | Calidad juridica, persuasividad, pertinencia semantica, fidelidad textual, suficiencia de comparacion, utilidad para experto, evaluacion de afirmaciones no soportadas que exija interpretacion y la rubrica HE4. |

## Denominadores y regla PASS

- Los controles por caso usan 50; los controles por candidato usan 150 slots.
- El schema congelado define umbrales agregados: JSON >= 0.95, ranking y cierre de pool = 1.0, evidencia historica/normativa >= 0.95, comparacion y advertencia final >= 0.95, sin reranking ni clasificacion oficial = 1.0.
- No existe una regla congelada de `automatic_validation_pass` por caso. Fase J reporta controles individuales y el cumplimiento agregado historico, sin inventar una tasa por caso.

## Diferido a Fase K

La rubrica `he4_rubric_v0.2.json` permanece congelada y sin ejecutar. HE4 global sigue en estado `PENDING QUALITATIVE EVALUATION - FASE K`.
