# EXP-04 Fase H / EXP-09: inventario HE4 pre-explicador v0.2

## Regla historica y portabilidad

La campaña HE4 previa fue `10B_llm_explanation_top3_audit_sample`: 50 casos, semilla declarada `2026`, cuotas `15/15/10/10` para `rank_1`, `rank_2_3`, `rank_4_10` y `difficult_low_support`. La implementación ordenaba determinísticamente por bucket de soporte, cantidad de soporte, rank exacto y `case_id`; el label se usaba solo para estratificar la muestra de evaluación y nunca se enviaba al LLM.

Clasificación: **B, portable con adaptación técnica**. V0.2 conserva cuotas, semilla, orden y fallback. El soporte se deriva de `support_count_dams`, el campo equivalente del split v0.2. La muestra v0.1 solo se leyó después para cuantificar solapamiento; no suministra case IDs ni contenido a la muestra final.

## Capas congeladas

1. Input experimental: muestra de 50, Top-3 de Fase A y precedente/evidencia exacta ya integrada por Fase F.
2. Especificación de generación: prompt histórico final de ejecución `src/llm/explain_top3_nandina_prompt_v0.2.md`, `qwen2.5:7b-instruct` local, temperatura 0, contexto 8192, JSON y sin retry por desempeño.
3. Especificación de evaluación: schema/validator de `he4_explainer_schema_v0.2.json` y rúbrica congelada en `he4_rubric_v0.2.json`.

El prompt v0.2 es el usado en la ejecución auditable previa. `v0.3` corresponde a una mejora posterior de diseño y no se adopta aquí, para no introducir un cambio semántico en esta reselección.

## Invariantes y límites

Los 150 slots se leen de `integration_candidate_slots.csv` de Fase F y se comparan con `historical_results.csv` de Fase A: código, posición y score son idénticos. Cada slot preserva el precedente ya congelado y evidencia NANDINA-8 exacta del corpus canónico. Los contextos no contienen label, rank de referencia ni material de Fase G.

No se llamó a Ollama, no se generaron respuestas y no se ejecutaron controles post-generación ni rúbrica sobre respuestas. HE4 permanece: `PENDING GENERATION / VALIDATION / QUALITATIVE EVALUATION`.
