# EXP-04 Fase L / EXP-10: matriz integrada de errores v0.2

## Fuente histórica y clasificación

No se localizó una ficha EXP-10 ni una formulación literal de OE5/HE5 versionada en el repositorio o su historial. Sí se preespecificaron la sensibilidad por duplicados y near-duplicates, y la interpretación del soporte histórico por DAM en `docs/protocolo_data_aduanas_clase87_v0.2.md` y `README.md`.

- **A. Preespecificado:** rendimiento histórico, distancia jerárquica, soporte por DAM, duplicados exactos y near-duplicates.
- **B. Adaptación técnica necesaria:** la matriz por `case_id`, cobertura por componente y eventos trazables derivados de outputs congelados A-K.
- **C. Exploratorio:** combinaciones de múltiples señales y cualquier priorización de casos críticos. No confirma HE5.

## Alcance y límites

La matriz tiene una fila por los 1056 casos del evalset v0.2. G cubre 20 casos y HE4 cubre 50: el resto se registra como no evaluado, nunca como fallo. `reference_nandina` se usa en evaluación, sin exposición a generación.

HE2, HE3 y HE4 no se reabren. Se preservan respectivamente como `PARTIALLY SUPPORTED`, `SUPPORTED` y `PARTIALLY SUPPORTED`. Se registran por separado `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` y `EVALUATOR_MODALITY_DEVIATION`.

## Dictamen

Gate L evalúa integridad y reproducibilidad, y queda `APPROVED`. OE5 y HE5 quedan `NOT EVALUABLE` porque no existe una formulación literal fuente para contrastarlas; esto no invalida los resultados descriptivos de la matriz. EXP-08 no se ejecutó.
