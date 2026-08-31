# EXP-04 Fase L / EXP-10: matriz integrada de errores v0.2

## Corrección de procedencia

La fuente aprobada externa `Anexo_1_NANDINA_LLM_RAG_v13.docx` contiene OE5, HE5 y la ficha EXP-10. No estaba versionada en el repositorio de ejecución: `SOURCE_NOT_VERSIONED_IN_EXECUTION_REPO = true`; no implica ausencia de la fuente.

OE5: “Analizar cuantitativa y cualitativamente los errores y límites del piloto, considerando la calidad de las descripciones, la proximidad jerárquica, la disponibilidad de precedentes históricos y el alcance interno de la evaluación.”

HE5: “Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.”

## Fuente histórica y clasificación

No se localizó una ficha EXP-10 ni una formulación literal de OE5/HE5 versionada en el repositorio o su historial. Sí se preespecificaron la sensibilidad por duplicados y near-duplicates, y la interpretación del soporte histórico por DAM en `docs/protocolo_data_aduanas_clase87_v0.2.md` y `README.md`.

- **A. Preespecificado:** rendimiento histórico, distancia jerárquica, soporte por DAM, duplicados exactos y near-duplicates.
- **B. Adaptación técnica necesaria:** la matriz por `case_id`, cobertura por componente y eventos trazables derivados de outputs congelados A-K.
- **C. Exploratorio:** combinaciones de múltiples señales y cualquier priorización de casos críticos. No confirma HE5.

## Alcance y límites

La matriz tiene una fila por los 1056 casos del evalset v0.2. G cubre 20 casos y HE4 cubre 50: el resto se registra como no evaluado, nunca como fallo. `reference_nandina` se usa en evaluación, sin exposición a generación.

HE2, HE3 y HE4 no se reabren. Se preservan respectivamente como `PARTIALLY SUPPORTED`, `SUPPORTED` y `PARTIALLY SUPPORTED`. Se registran por separado `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` y `EVALUATOR_MODALITY_DEVIATION`.

## Dictamen

Gate L correctivo queda `APPROVED`. OE5 queda `IN_PROGRESS` y HE5 `PENDING_FINAL_ASSESSMENT_AFTER_EXP08`. La matriz conserva la descripción comercial literal y los flags near-duplicate congelados 0.90/0.95/0.98. No hubo regla case-level congelada para calidad descriptiva, por lo que ese componente no se evaluó. EXP-08 no se ejecutó.
