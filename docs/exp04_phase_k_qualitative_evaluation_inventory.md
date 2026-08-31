# EXP-04 Fase K: inventario de evaluacion cualitativa HE4 v0.2

## Modalidad originalmente preparada

La modalidad historica es **A. revision humana/manual**. `docs/revision_cualitativa_fichas_auditables_v0.1.md` contiene revision narrativa por ficha y la rubrica fuente describe calidad para auditoria humana. No se identifico una operacionalizacion deterministica 0-2 por las ocho dimensiones ni un LLM-as-judge preespecificado.

Por ello esta fase prepara el paquete ciego y no asigna puntuaciones. El scoring queda a cargo de un revisor humano no asignado.

## Contrato congelado

- Rubrica: `src/configs/he4_rubric_v0.2.json`.
- Ocho dimensiones, escala 0-2, total maximo 16.
- Una ficha es auditable solo con >=12/16 y sin hard violation.
- Los labels, ranks de referencia y buckets se excluyen del paquete humano.
- `advertencias_globales` se excluye del scoring por `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`.

## Modalidad finalmente ejecutada

La puntuacion final recibida se realizo bajo `AI_EXPERT_ROLE`, identificador anonimizado `independent_ai_reviewer_01`. No constituye revision humana: se registra como `EVALUATOR_MODALITY_DEVIATION` frente a la modalidad `HUMAN/MANUAL REVIEW` originalmente preparada. La desviacion afecta exclusivamente quien asigno las puntuaciones; no altera la muestra, Top-3, inputs, respuestas, rubrica, dimensiones, escala ni umbral congelados.

La evaluacion se baso en el review packet ciego y la rubrica congelada. No se expusieron ground truth, ranks de referencia ni buckets; no se uso evidencia externa, web ni retrieval. `advertencias_globales` permanece excluido por `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`.

## Artefactos y resultados finales

El cierre determinista se ejecuta con `src/experiments/close_he4_qualitative_ai_scoring_v02.py` y conserva la entrada recibida `he4_qualitative_scoring_template_v0.2.csv` sin modificarla. Sus salidas son los case scores derivados, metricas por dimension, distribucion por bucket, comparacion con los nueve casos de advertencia generica de J, findings, assessment conjunto J/K, manifiesto Gate K y summary de fase.

El CSV validado contiene 50 casos, 400 scores y 400 justificaciones. Los totales y la auditabilidad son consistentes en 50/50 casos bajo la regla congelada `total >= 12/16` y sin hard violation. El resultado es 28/50 fichas auditables (56%), 22/50 no auditables y cero hard violations. La trazabilidad obtuvo 50 scores de 2; la verificabilidad concentra 24 scores de 0, por lo que es la principal limitacion cualitativa observada. Los nueve casos con ausencia del control de advertencia normativa generica preservado en J obtuvieron 1/9 auditables, frente a 27/41 en los demas casos.

## Dictamen y limitaciones

`GATE K = APPROVED WITH EVALUATOR-MODALITY LIMITATION` porque el scoring recibido, su procedencia y los agregados son consistentes y reproducibles. Esta aprobacion no equipara la modalidad AI con revision humana. J permanece `APPROVED WITH PROTOCOL/SPECIFICATION LIMITATION`; su mismatch prompt-schema no se usa como penalizacion K. La integracion J/K clasifica HE4 como `PARTIALLY SUPPORTED`, sin iniciar Fase L.

## Estado historico pre-scoring

`GATE K = PENDING HUMAN SCORING` describe correctamente el paquete previo y no se reescribe. El cierre final y sus resultados se registran en `gate_k_qualitative_evaluation_manifest_v0.2.json`, `he4_qualitative_metrics_v0.2.json` y `he4_he4_joint_jk_assessment_v0.2.json`.
