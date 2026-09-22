# PREG7-002 — Preauditoría no gobernante de la tesis para G7-F02

## 0. Naturaleza y límites

Este documento es **pretrabajo no gobernante** para reducir el costo de la futura G7-F02. No activa Grupo 7, no modifica la tesis, no modifica `main`, Plan Maestro, fichas ni artículo, no recalcula métricas y no sustituye la auditoría formal de G7/G8.

Documento examinado mediante la copia legible disponible en Project/Library:

```text
Molleapasa_gv(4).docx
```

La identidad binaria exacta aún no puede congelarse:

```text
THESIS_SHA256_VERIFIED = false
THESIS_APPROVED_MASTER_STATUS = NOT_ESTABLISHED
```

Por ello, los hallazgos siguientes son válidos como **preauditoría de contenido**, pero deberán revalidarse contra el Word maestro formalmente identificado cuando G7-F01 sea activable.

---

## 1. Ground truth usado para la preauditoría

### 1.1 Estado científico

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
```

### 1.2 Guardrails

```text
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

### 1.3 Presentación canónica

Nueve tablas G5 y tres figuras G6 especificadas. Las figuras de G6-F02 permanecen candidatas pendientes de corrección/aprobación; por ello no se usan todavía como evidencia editorial final.

---

## 2. Resultado general

```text
PREG7_002_RESULT = MAJOR_UPDATE_REQUIRED
THESIS_SCIENTIFIC_BASE = PARTIALLY_CURRENT_BUT_NUMERICALLY_STALE
FORMAL_G7_F02_AUTHORIZED = false
THESIS_EDITED = false
NEW_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
```

La tesis conserva formulaciones conceptuales e hipótesis que siguen siendo válidas, pero su Capítulo 4, parte de la metodología, la contrastación de hipótesis y las conclusiones contienen un estado experimental previo a los cierres G3–G5 y deben ser reemplazados o reconciliados.

---

## 3. Elementos que pueden conservarse conceptualmente

### KEEP-001 — Texto exacto de HE2

La tesis contiene la formulación que coincide con el contrato G3:

> La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.

Clasificación:

```text
ACTION = KEEP_EXACT_TEXT
RISK = NONE
```

### KEEP-002 — Texto exacto de HE5

La tesis contiene la formulación que coincide con el contrato G3:

> Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.

Clasificación:

```text
ACTION = KEEP_EXACT_TEXT
RISK = NONE
```

### KEEP-003 — Separación funcional de la arquitectura

La tesis describe correctamente, en términos generales:

```text
Descripción comercial
→ normalización
→ recuperación histórica BM25
→ ranking de códigos no repetidos
→ Top-3 fijo
→ evidencia histórica + normativa
→ payload estructurado
→ LLM local explicador
```

También afirma que la evidencia normativa no cambia la puntuación ni el orden del ranking histórico y que el modelo no debe agregar/reordenar candidatos ni emitir clasificación oficial.

Clasificación:

```text
ACTION = KEEP_WITH_LOCAL_REVIEW
RISK = LOW
```

Debe conservarse la lógica, pero cualquier cifra, nombre de output, configuración o afirmación de resultado asociada debe revalidarse por separado.

### KEEP-004 — Delimitación no jurídica

La tesis ya contiene formulaciones compatibles con el guardrail de que la explicación estructurada/auditable no constituye corrección jurídica ni sustituye juicio experto.

```text
ACTION = KEEP_WITH_TERMINOLOGY_HARMONIZATION
RISK = LOW
```

---

## 4. Hallazgos que requieren actualización obligatoria

### PREG7-TESIS-001 — Split/evaluación obsoletos

**Severidad:** `BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE`

La tesis describe una partición previa:

```text
historical = 3000
DEV = 100
EVAL = 1006
seed = 2026
control = no shared identifiers
```

El estado científico congelado posterior usa:

```text
EVAL = 1056 series
EVAL_DAM = 67
EVAL_NANDINA = 42
v0.2 = DAM-disjoint governance where dependency applies
```

**Riesgo:** Methods, Results y conclusiones pueden referirse a una población distinta de la inferencia final.

**Acción futura:** `REPLACE/RECONCILE` en metodología, descripción de datos, tablas de partición, resultados y cualquier conclusión que use 1006.

---

### PREG7-TESIS-002 — Métricas históricas antiguas presentadas como finales

**Severidad:** `BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE`

La tesis reporta repetidamente:

```text
Top-1 = 0.8628
Top-3 = 0.9374
Top-10 = 0.9801
MRR = 0.9062
coverage complete before position 50 / 1006 cases
```

Estas cifras pertenecen al estado anterior y no deben gobernar G7-F02. El futuro texto debe consumir exclusivamente G5-MAIN-01/G5-MAIN-02 y las fuentes G3 cerradas.

**Acción futura:** `REMOVE_OR_SUPERSEDE_NUMERIC_CONTENT`.

No se deben “editar a mano” solo los números dentro de la narrativa antigua; debe reescribirse el pasaje desde la tabla canónica y el claim correspondiente.

---

### PREG7-TESIS-003 — HE2 permanece provisional en la tesis

**Severidad:** `BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE`

La tesis declara:

```text
HE2 = respaldada de forma provisional
```

y condiciona el dictamen a futuras reejecuciones normativas.

El estado final G3-F04 es:

```text
HE2 = SUPPORTED
HE2_A = SUPPORTED_BY_PRIMARY_EVIDENCE
HE2_B hierarchical = SUPPORTED_BY_PRIMARY_EVIDENCE
Phase E = DIRECTIONALLY_CONSISTENT_DESCRIPTIVE
```

**Acción futura:** reemplazar la contrastación HE2 completa usando:

- G5-MAIN-01 para HE2_A;
- G5-MAIN-02 para HE2_B;
- G5-SECONDARY-01 solo como contexto descriptivo;
- 99% CI de las diferencias pareadas HE2_A;
- 95% CI del único contraste HE2_B;
- sin CI por brazo y sin promover Pool@200 a segundo contraste confirmatorio.

---

### PREG7-TESIS-004 — HE5 está indebidamente “parcialmente respaldada”

**Severidad:** `BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE`

La tesis registra:

```text
HE5 = parcialmente respaldada
```

El cierre G3-F04 es:

```text
HE5 = INCONCLUSIVE
Description component = NOT_ESTIMABLE
Hierarchy component = DESCRIPTIVE_ONLY
Precedent component = DESCRIPTIVE_ONLY / NO_FROZEN_INSUFFICIENCY_THRESHOLD
Internal validity component = DOCUMENTED_LIMITATION
```

La tesis además usa categorías históricas antiguas de soporte (`2–4`, `10+`) para inferir mayor dificultad con “bajo soporte”. Eso no corresponde al contrato final. Las categorías congeladas actuales son literalmente:

```text
1 DAM
2 DAM
3-4 DAM
5+ DAM
```

Ninguna puede renombrarse retrospectivamente como “insuficiente”.

**Acción futura:** reescribir 4.1.8, 4.2.5, tabla de contrastación, discusión y conclusiones relacionadas con HE5.

---

### PREG7-TESIS-005 — Afirmaciones sobre descripciones ambiguas/incompletas no son estimables

**Severidad:** `MAJOR`

La tesis atribuye parte de HE5 a “descripciones ambiguas o incompletas” y a una futura revisión integrada de 1006 descripciones.

El contrato final establece:

```text
description_quality_operationalized = 0
DESCRIPTION_COMPONENT = NOT_ESTIMABLE
```

**Acción futura:** eliminar cualquier prevalencia, concentración o inferencia empírica sobre ambigüedad/incompletitud que no tenga un estimando congelado. Puede conservarse únicamente como limitación/no-estimabilidad.

---

### PREG7-TESIS-006 — Integración histórico–normativa basada en resultados antiguos

**Severidad:** `MAJOR`

La sección 4.1.5 reporta un estado antiguo con:

```text
Top-1 0.8628
Top-3 0.9374
Top-10 0.9801
Top-100 1.0000
MRR 0.9062
373 historical-only
633 both
0 normative-only
```

También concluye que no hubo rescates adicionales porque el histórico ya cubría los 1006 casos a Top-100.

Este bloque no aparece como una de las nueve presentaciones canónicas G5 y no debe mantenerse automáticamente como resultado final solo porque figure en la tesis previa.

**Acción futura:** `VERIFY_AGAINST_CURRENT_HE3/INTEGRATION_ARTIFACTS_OR_REMOVE_FROM_FINAL_RESULTS`. No trasladar las cifras legacy al candidato G7-F02 sin trazabilidad vigente.

---

### PREG7-TESIS-007 — Figura legacy de integración no pertenece al catálogo G6 aprobado

**Severidad:** `MAJOR_EDITORIAL`

La tesis contiene una “Figura 7 — Contribución diferenciada de la recuperación histórica y la evidencia normativa en el pool híbrido”, marcada como pendiente.

El catálogo G6-F01 aprobado contiene solo:

```text
G6-FIG-01 = HE2_A + HE2_B / MAIN
G6-FIG-02 = Phase E / SECONDARY
G6-FIG-03 = EXP11A / APPENDIX
```

**Acción futura:** no generar la Figura 7 legacy como gráfico de resultados salvo una futura decisión explícita que modifique G6. En el estado actual debe clasificarse `REMOVE_OR_REPLACE_BY_APPROVED_PRESENTATION`.

---

### PREG7-TESIS-008 — Conclusiones cuantitativas obsoletas

**Severidad:** `BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE`

Las conclusiones reproducen cifras legacy y dictámenes provisionales, incluyendo:

```text
HE2 = provisional
HE3 = partially supported
HE5 = partially supported
absence of integrated analysis of 1006 descriptions
```

El futuro cierre debe construirse desde los estados aprobados actuales y no desde la conclusión previa.

**Acción futura:** `REWRITE_FROM_APPROVED_CLAIMS`.

---

### PREG7-TESIS-009 — “Exactitud Top-k” requiere armonización semántica

**Severidad:** `MINOR_BUT_SYSTEMATIC`

La matriz/operacionalización usa en lugares el término “exactitud Top-k”. El contrato actual diferencia estrictamente:

```text
candidate retrieval / ranking metrics
≠ overall classification accuracy
```

**Acción futura:** revisar terminología para que Top-k/MRR describan recuperación/ranking de candidatos y no exactitud global del framework.

---

### PREG7-TESIS-010 — Discusión del banco histórico contiene inferencias antiguas de soporte

**Severidad:** `MAJOR`

La discusión afirma, a partir de categorías antiguas, que los grupos con pocos precedentes mostraron mayor variación y usa comparaciones como `2–4 casos` frente a `10+`.

El estado final solo autoriza buckets literales `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`, sin umbral de insuficiencia ni CI.

**Acción futura:** reescribir desde G5-SECONDARY-02 y mantener la interpretación descriptiva.

---

### PREG7-TESIS-011 — Discusión de métodos normativos todavía habla de “corridas por repetir”

**Severidad:** `MAJOR`

La tesis advierte que BM25 plano, Text2Trade y BM25 jerárquico “deben volver a ejecutarse con el evalset congelado”. Ese estado ya fue superado por el cierre experimental y el Attempt06 corregido.

**Acción futura:** reemplazar por el estado actual, usando únicamente las fuentes corregidas vigentes y la interpretación G4.

---

### PREG7-TESIS-012 — Resultados de HE3/HE4 necesitan reconciliación separada

**Severidad:** `VERIFY_REQUIRED`

La tesis presenta HE3 y HE4 con cifras y dictámenes de un estado previo (p. ej., reranker legacy de 20 casos, HE4 50 casos/score 0.9520). El ground truth de G3–G5 utilizado en este preflight está centrado en HE2/HE5 y en las sensibilidades aprobadas posteriores.

**Acción futura:** antes de G7-F02, verificar cada claim HE1/HE3/HE4 contra los artefactos cerrados de Grupo1/Grupo2 y la gobernanza del Plan Maestro; no inferir que una cifra de la tesis sigue vigente por ausencia de contradicción explícita en G3–G5.

---

## 5. Tabla de acciones por bloque de tesis

| Bloque | Estado preauditado | Acción futura |
|---|---|---|
| Problema/objetivos/hipótesis | mayormente vigente | preservar formulaciones aprobadas; verificar master formal |
| Variables/operacionalización | parcialmente vigente | armonizar SERIE/DAM, retrieval vs accuracy, estimabilidad |
| Arquitectura R-A-G / Top-3 fijo | sustancialmente vigente | conservar lógica; verificar detalles técnicos |
| Curación/partición | obsoleta en puntos críticos | actualizar a v0.2 y N=1056/67 DAM/42 NANDINA |
| Resultados normativos | obsoletos | sustituir por G3/G5 actuales |
| Resultados históricos | obsoletos | sustituir por G5-MAIN-01 |
| Integración histórica–normativa | legacy / verificar | no usar cifras antiguas sin trazabilidad actual |
| Reranker diagnóstico | legacy / verificar | revisar artefactos actuales y alcance diagnóstico |
| Explicación HE4 | verificar | conservar guardrail no jurídico; auditar cifras aparte |
| HE2 | obsoleto/provisional | reescribir como SUPPORTED con evidencia G3/G5 |
| HE5 | científicamente incompatible | reescribir como INCONCLUSIVE |
| Discusión | mezcla vigente + legacy | reconstruir sobre G4 synthesis/literature contrast |
| Limitaciones | incompletas/legacy | incorporar G2B-L01..L11 + G3/G4 límites actuales |
| Conclusiones | obsoletas | reescribir desde claims aprobados |
| Figuras de resultados legacy | no gobernadas por G6 actual | retirar/reemplazar según G6-F01/G6-F03 |

---

## 6. Mapeo mínimo futuro para G7-F02

### Resultados

```text
HE2_A → G5-MAIN-01 → G6-FIG-01 (cuando G6 cierre)
HE2_B → G5-MAIN-02 → G6-FIG-01
Phase E → G5-SECONDARY-01 → G6-FIG-02
HE5 hierarchy/support → G5-SECONDARY-02 → TABLE_ONLY
Top50 → G5-APPENDIX-01 → TABLE_ONLY
```

### Discusión / limitaciones

```text
EXP11A → G5-APPENDIX-02 + G6-FIG-03 / NONCAUSAL
EXP11B → G5-APPENDIX-03 / DESCRIPTIVE_ONLY
Attempt06 → G5-APPENDIX-04 / CURRENT_CORRECTED_STATE_ONLY
Phase-E diagnostic union → G5-APPENDIX-05 / DIAGNOSTIC_ONLY
EXP12 → TEXT_ONLY / NOT_ESTIMABLE
HE5 ambiguous descriptions → TEXT_ONLY / NOT_ESTIMABLE
```

### Hipótesis

```text
HE2 → SUPPORTED
HE5 → INCONCLUSIVE
```

No se emite aquí redecisión sobre HE1, HE3, HE4 o hipótesis general; esas deben mapearse a sus fuentes propias en el freeze formal.

---

## 7. Riesgos de G8 detectables desde ahora

```text
G8-RISK-001 = legacy EVAL_N 1006 appearing after final EVAL_N 1056
G8-RISK-002 = legacy metrics 0.8628/0.9374/0.9801/0.9062 surviving into final thesis
G8-RISK-003 = HE2 provisional wording surviving after HE2 SUPPORTED
G8-RISK-004 = HE5 partially-supported wording surviving after HE5 INCONCLUSIVE
G8-RISK-005 = support buckets retrospectively relabeled as insufficient/low support
G8-RISK-006 = ambiguous-description prevalence inferred despite NOT_ESTIMABLE
G8-RISK-007 = superseded normative/0B-05C outputs used instead of Attempt06
G8-RISK-008 = legacy figures retained outside G6 approved catalog
G8-RISK-009 = Top-k described as global accuracy
G8-RISK-010 = article and thesis using different experimental snapshots
```

Estos riesgos deben convertirse posteriormente en checks explícitos de G8-F01/G8-F02.

---

## 8. Conclusión del pretrabajo

La tesis no necesita ser reconstruida desde cero: conserva un armazón conceptual útil, hipótesis exactas vigentes y una descripción arquitectónica sustancialmente alineada. Sin embargo, **sus resultados, contrastación HE2/HE5, parte de Métodos y conclusiones pertenecen a un estado experimental anterior** y requerirán una actualización controlada amplia en G7-F02.

El cambio debe hacerse por sustitución trazable desde claims/tablas/artefactos actuales, no mediante edición puntual de cifras antiguas.

```text
FORMAL_G7_F02_READY_NOW = false
PREPARATORY_MAPPING_READY = true
THESIS_REWRITE_SCOPE_ESTIMATE = SUBSTANTIAL_BUT_LOCALIZED_TO_EMPIRICAL_SECTIONS
CRITICAL_REWRITE_AREAS = METHODS_SPLIT + RESULTS + HE2 + HE5 + DISCUSSION + CONCLUSIONS
PRESERVABLE_CORE = APPROVED_PROBLEM/HYPOTHESES + FUNCTIONAL_ARCHITECTURE + NONBINDING_SCOPE
```
