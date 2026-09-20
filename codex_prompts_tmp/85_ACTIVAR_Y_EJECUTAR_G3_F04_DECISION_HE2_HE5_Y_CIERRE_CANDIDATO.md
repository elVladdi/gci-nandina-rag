# PROMPT 85 — ACTIVAR Y EJECUTAR EXCLUSIVAMENTE G3-F04: DECISIÓN HE2/HE5 Y CIERRE CANDIDATO DE GRUPO 3

## 0. Naturaleza, autorización y límite

La IA Experimental ha verificado externamente el cierre de G3-F03. El usuario ha autorizado continuar con la siguiente ficha elegible.

Esta ejecución constituye autorización expresa **únicamente para G3-F04**.

Estado de entrada:

```text
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F01 = PROSPECTIVE / NOT_AUTHORIZED
```

G3-F04 puede **traducir evidencia ya aprobada en una disposición explícita de HE2 y HE5**, pero no puede crear nueva evidencia, recalcular inferencia, modificar resultados previos ni cerrar canónicamente Grupo 3 antes de la auditoría externa.

El resultado de esta ejecución debe quedar como:

```text
G3_F04 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP3 = CLOSURE_CANDIDATE_PENDING_EXTERNAL_AUDIT / NOT_CLOSED
```

Solo una auditoría externa posterior de la IA Experimental puede autorizar la integración final y el estado `GROUP3=CLOSED / APPROVED`.

---

## 1. Repositorio y refs congelados de entrada

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de cualquier modificación ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 7d09f692da23367d3aba941db1febdca2baa8917
origin/docs/plan-maestro-temporal-2026-08-31 = 96cccb9a61f42ab97b1eba607524e33f992740f6
origin/docs/fichas-grupos-3-8 = 356aebd75c5fb4c9355ae0164bfcd0cadc341814
```

Artículo observado al autorizar Prompt85:

```text
origin/article/main-manuscript = 1e729cd4ade1fbee59f1e31762001886eb68aca7
```

El artículo es **solo observacional** y no es input científico de G3-F04. Si avanza concurrentemente, registra el drift como advertencia siempre que Prompt85 no modifique esa rama.

La rama `codex/prompts-temporary` puede avanzar por la incorporación de este Prompt85; eso no constituye drift científico.

Si `main`, Plan Maestro o fichas presentan drift no explicado antes de la activación:

```text
STOP / SCIENTIFIC_OR_GOVERNANCE_REF_DRIFT
```

---

## 2. Fuentes rectoras obligatorias

Lee íntegramente y usa en este orden.

### 2.1 Ficha G3-F04

Desde `origin/docs/fichas-grupos-3-8 = 356aebd75c5fb4c9355ae0164bfcd0cadc341814`:

```text
docs/fichas/grupos_3_8/grupo_3/G3_F04_DECISION_HE2_HE5_Y_CIERRE.md
```

Blob esperado:

```text
d0ca136829a62fb0985c37975f47f35283f2caab
```

### 2.2 Contrato analítico G3-F01 integrado en main

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

El campo histórico `status=CANDIDATE_PENDING_EXTERNAL_AUDIT` dentro de esos artefactos refleja el estado que tenían al ser generados. **No es el estado operativo vigente**: G3-F01 ya está cerrado/aprobado/integrado por gobernanza posterior.

### 2.3 Registro maestro G3-F02 integrado en main

```text
outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
outputs/analysis/group3/g3_metric_population_registry_v0.1_hash_ledger.csv
```

Blobs congelados:

```text
G3F02_CSV_BLOB = c63619b56a07e6b6d7be78b515d941ec3b205c41
G3F02_JSON_BLOB = 5ea33ca583b18426374fa15baf1b1759e76cd99e
G3F02_LEDGER_BLOB = 521bfcdf34d03c4effa8b8ef19f9777b6827d439
```

### 2.4 Resultados inferenciales G3-F03 integrados en main

```text
src/analysis/run_g3_f03_inference_v01.py
outputs/analysis/group3/g3_inferential_results_v0.1.csv
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
outputs/analysis/group3/g3_inferential_results_v0.1_hash_ledger.csv
```

Blobs congelados:

```text
G3F03_SCRIPT_BLOB = 2378298c9db401c938ebfb3cd505b30cabad2c62
G3F03_CSV_BLOB = cf3d8d85e099a300330da0214836e70af7a02253
G3F03_JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc
G3F03_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
G3F03_LEDGER_BLOB = b128966f1295ac8a853341b7f02ce7f9218157b8
```

El campo histórico `status=CANDIDATE_PENDING_EXTERNAL_AUDIT` dentro del JSON G3-F03 tampoco invalida su estado actual: G3-F03 ya fue auditado externamente e integrado. La fuente operativa del cierre es Plan Maestro + registro de fichas.

### 2.5 Gobernanza vigente

Lee también:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

desde la rama del Plan indicada en sección 1, y:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

desde la rama de fichas indicada en sección 1.

Debe resultar:

```text
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
HE2_DECIDED = false
HE5_DECIDED = false
```

Si no coincide:

```text
STOP / G3_F04_PRECONDITION_MISMATCH
```

---

## 3. Activación prospectiva administrativa de G3-F04

Antes de crear la disposición, materializa la autorización en:

```text
branch = docs/fichas-grupos-3-8
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Actualiza únicamente G3-F04 a:

```text
ACTIVE / AUTHORIZED / DECISION_PENDING
```

Mantén:

```text
G4-F01 = PROSPECTIVE / NOT_AUTHORIZED
```

Añade un bloque con, como mínimo:

```text
FICHA = G3-F04
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT85_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / DECISION_PENDING
ACTIVATION_DATE = 2026-09-19
MAIN_AT_ACTIVATION = 7d09f692da23367d3aba941db1febdca2baa8917
PLAN_AT_ACTIVATION = 96cccb9a61f42ab97b1eba607524e33f992740f6
FICHAS_AT_ACTIVATION = 356aebd75c5fb4c9355ae0164bfcd0cadc341814
ARTICLE_HEAD_OBSERVED = 1e729cd4ade1fbee59f1e31762001886eb68aca7
PROMPT85_COMMIT = <commit exacto de Prompt85>
HE2_DECISION_AUTHORIZED = true
HE5_DECISION_AUTHORIZED = true
NEW_INFERENCE_AUTHORIZED = false
G4_F01_AUTHORIZED = false
```

Haz un solo commit administrativo de activación y push normal.

No modifiques Plan Maestro todavía.

Si la activación no puede publicarse antes de construir la disposición:

```text
STOP / ACTIVATION_NOT_MATERIALIZED
```

---

## 4. Hipótesis literales congeladas

Debes copiar sin reformular en el JSON de disposición.

### HE2

> La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.

### HE5

> Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.

No sustituyas estos textos por versiones simplificadas como hipótesis oficial.

---

## 5. Nomenclatura decisional permitida

Para la **disposición global** de cada hipótesis solo puedes usar:

```text
SUPPORTED
NOT_SUPPORTED
INCONCLUSIVE
```

No uses `PARTIALLY_SUPPORTED` como disposición global, salvo que exista una regla previa explícita versionada que la autorice; en ausencia de esa regla, representa la parcialidad a nivel de componentes y usa `INCONCLUSIVE` cuando corresponda.

No uses `SIGNIFICANT` / `NONSIGNIFICANT`, porque G3-F03 no calculó p-values.

No interpretes la ausencia de evaluación como evidencia de fallo.

---

## 6. Regla decisional HE2_A — ranking temprano

Existen exactamente tres familias primarias:

```text
HE2_A_HISTORICAL_VS_NORMATIVE_FLAT_ATTEMPT06
HE2_A_HISTORICAL_VS_NORMATIVE_HIERARCHICAL_ATTEMPT06
HE2_A_HISTORICAL_VS_D1A_ATTEMPT06
```

Cada familia tiene exactamente cinco contrastes primarios:

```text
Top-1
Top-3
Top-5
Top-10
MRR@100
```

Todos usan diferencia `historical - normative` con dirección congelada `> 0` y CI marginal two-sided de 99% bajo la regla Bonferroni prospectiva.

Para **cada familia** aplica mecánicamente:

```text
si los 5 ci_lower > 0:
    FAMILY_DISPOSITION = SUPPORTED_BY_PRIMARY_EVIDENCE
elif cualquier ci_upper <= 0:
    FAMILY_DISPOSITION = NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
else:
    FAMILY_DISPOSITION = INCONCLUSIVE_PRIMARY_EVIDENCE
```

Luego:

```text
si las 3 familias = SUPPORTED_BY_PRIMARY_EVIDENCE:
    HE2_A_DISPOSITION = SUPPORTED_BY_PRIMARY_EVIDENCE
elif cualquier familia = NOT_SUPPORTED_BY_PRIMARY_EVIDENCE:
    HE2_A_DISPOSITION = NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
else:
    HE2_A_DISPOSITION = INCONCLUSIVE_PRIMARY_EVIDENCE
```

Top-50 no puede cambiar HE2_A. Debe registrarse únicamente como suplementario.

No recalcules los CI: consume los 15 resultados integrados de G3-F03.

---

## 7. Regla decisional HE2_B — cobertura profunda

### 7.1 Componente inferencial jerárquico

Existe un único contraste primario:

```text
Recall@200 - Recall@100
```

con dirección esperada `> 0` y CI two-sided al 95%.

Aplica:

```text
si ci_lower > 0:
    HE2_B_HIERARCHICAL = SUPPORTED_BY_PRIMARY_EVIDENCE
elif ci_upper <= 0:
    HE2_B_HIERARCHICAL = NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
else:
    HE2_B_HIERARCHICAL = INCONCLUSIVE_PRIMARY_EVIDENCE
```

No dupliques `Pool@200` como segundo contraste.

### 7.2 Componente de conjunto candidato Phase E

Consume exclusivamente la evidencia congelada de G3-F02 para:

```text
HE2_B_PHASE_E_FROZEN_ROLE_POOLS
```

Variantes `A_historical_defined`:

```text
hierarchical_only
dual_only
hierarchical_first_100
hierarchical_80_dual_backfill_20
```

Usa sus `Pool@50`, `Pool@100` y `Pool@200` ya materializados. Está permitido comparar descriptivamente esos valores para determinar si el patrón de cobertura a mayor profundidad es direccionalmente consistente con la cláusula de expansión. **No calcules CI, p-values ni un nuevo contraste inferencial.**

Las variantes:

```text
hierarchical_70_dual_backfill_30
diagnostic_union_hierarchical_dual
```

permanecen diagnóstico/descriptivo y no pueden promoverse a evidencia confirmatoria.

Etiqueta el componente Phase E como una de:

```text
DIRECTIONALLY_CONSISTENT_DESCRIPTIVE
NOT_DIRECTIONALLY_CONSISTENT_DESCRIPTIVE
MIXED_DESCRIPTIVE
```

### 7.3 Disposición global HE2

Aplica la siguiente regla conservadora y trazable:

```text
si HE2_A_DISPOSITION = SUPPORTED_BY_PRIMARY_EVIDENCE
   y HE2_B_HIERARCHICAL = SUPPORTED_BY_PRIMARY_EVIDENCE
   y PHASE_E_FROZEN_ROLE_POOLS = DIRECTIONALLY_CONSISTENT_DESCRIPTIVE:
       HE2 = SUPPORTED

elif HE2_A_DISPOSITION = NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
     o HE2_B_HIERARCHICAL = NOT_SUPPORTED_BY_PRIMARY_EVIDENCE:
       HE2 = NOT_SUPPORTED

else:
       HE2 = INCONCLUSIVE
```

La evidencia Phase E es descriptiva: puede completar la trazabilidad de la cláusula de conjunto candidato cuando es consistente, pero **no sustituye** la evidencia primaria de HE2_A ni el contraste primario jerárquico de HE2_B.

---

## 8. Regla decisional HE5

HE5 contiene cuatro proposiciones literales. Evalúalas separadamente sin inventar variables ni umbrales.

### 8.1 Descripciones ambiguas o incompletas

G3-F01 congeló:

```text
description_quality_operationalized = 0
```

Por tanto:

```text
HE5_DESCRIPTION_COMPONENT = NOT_ESTIMABLE
```

No conviertas heurísticas textuales ni ejemplos cualitativos en prevalencia post hoc.

### 8.2 Subpartidas jerárquicamente próximas

Las categorías congeladas `SAME_CHAPTER`, `SAME_HS4`, `SAME_HS6` son descriptivas. Puedes informar sus conteos/patrones materializados, pero no inventes un umbral para afirmar que los errores "se concentran" en proximidad jerárquica si ese criterio no fue congelado.

Estado permitido:

```text
HE5_HIERARCHY_COMPONENT = DESCRIPTIVE_ONLY
```

### 8.3 Precedentes históricos insuficientes

Los buckets congelados son literalmente:

```text
1 DAM
2 DAM
3-4 DAM
5+ DAM
```

No existe umbral prospectivo que defina cuál es "insuficiente".

Por tanto:

```text
HE5_PRECEDENT_COMPONENT = DESCRIPTIVE_ONLY / NO_FROZEN_INSUFFICIENCY_THRESHOLD
```

No renombres retrospectivamente ningún bucket como insuficiente.

### 8.4 Validez restringida al conjunto interno

La frontera empírica congelada es:

```text
CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
```

Registra esta proposición como limitación de validez **documentada** del piloto, no como demostración de generalización externa.

```text
HE5_INTERNAL_VALIDITY_COMPONENT = DOCUMENTED_LIMITATION
```

### 8.5 Disposición global HE5

No se permite convertir componentes `NOT_ESTIMABLE` o `DESCRIPTIVE_ONLY` en evidencia confirmatoria mediante razonamiento post hoc.

Con el contrato actualmente congelado, una disposición `SUPPORTED` para HE5 exige que todas las proposiciones de concentración necesarias sean evaluables con criterios preespecificados. Si al menos una proposición literal de concentración permanece `NOT_ESTIMABLE` y otra carece de umbral prospectivo, `SUPPORTED` no está metodológicamente autorizado.

Tampoco se puede asignar `NOT_SUPPORTED` solo porque una proposición no sea estimable.

Por tanto aplica:

```text
si una o más proposiciones literales necesarias permanecen NOT_ESTIMABLE
   o no existe criterio prospectivo para decidir concentración,
   y no existe evidencia primaria válida en sentido contrario:
       HE5 = INCONCLUSIVE

NOT_SUPPORTED solo puede usarse si existe evidencia válida que contradiga una proposición evaluable de HE5 bajo una regla congelada.
```

Debes explicar con precisión qué partes son descriptivas, cuáles no son estimables y cuál limitación sí está documentada.

---

## 9. Sensibilidades y límites que deben acompañar las decisiones

Preserva explícitamente:

- EXP11A = sensibilidad conjunta tamaño/composición; **no** efecto causal aislado del tamaño del banco.
- EXP11B = sensibilidad descriptiva; las 10 réplicas H150/H200 no definen una superpoblación inferencial y `10 x 1056` no son observaciones independientes.
- 0B-05C = usar únicamente Attempt06 corregido; EV03 cambio agregado cero, EV04 pequeña disminución no nula de MRR, D1a cambios no nulos; no resumir como "sin impacto numérico".
- EXP12 = `NOT_ESTIMABLE`; no D-HIGH/D-MID/D-LOW, no retrieval, no reapertura.
- EVAL = 1,056 series / 67 DAM / 42 NANDINA, benchmark interno de Clase 87.
- recuperación histórica superior en métricas de retrieval **no equivale** a exactitud global del framework RAG completo.
- evidencia normativa recuperada **no equivale** a corrección jurídica vinculante.
- explicación auditable del LLM **no equivale** a clasificación legalmente correcta.
- el LLM local explica candidatos preseleccionados; no clasifica desde cero ni reemplaza el ranking histórico.

---

## 10. Outputs científicos/documentales autorizados

Crea desde exactamente:

```text
7d09f692da23367d3aba941db1febdca2baa8917
```

la rama:

```text
codex/group3-f04-hypothesis-disposition-v01
```

Crea exactamente tres paths nuevos:

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
docs/analysis/group3/g3_claim_registry_v0.1.md
outputs/audits/group3_closure_v0.1.json
```

No modifiques archivos científicos existentes.

Haz un único commit candidato con esos tres paths.

Estado interno obligatorio:

```text
G3_F04_STATUS = CANDIDATE_PENDING_EXTERNAL_AUDIT
GROUP3_CLOSURE = CANDIDATE_PENDING_EXTERNAL_AUDIT / NOT_CLOSED
G4_F01_AUTHORIZED = false
```

---

## 11. Esquema mínimo de `g3_hypothesis_disposition_v0.1.json`

Incluye como mínimo:

```text
artifact_id
status
ficha
input_refs
source_blobs
hypotheses
HE2
  exact_text
  overall_disposition
  HE2_A
    family_dispositions
    primary_result_ids
    rule_applied
  HE2_B
    hierarchical_disposition
    primary_result_id
    phase_e_descriptive_disposition
    phase_e_source_registry_rows
    rule_applied
  supplementary_context
  limitations
HE5
  exact_text
  overall_disposition
  description_component
  hierarchy_component
  precedent_component
  internal_validity_component
  source_registry_rows
  rule_applied
  limitations
sensitivity_context
scope
flags
```

Flags obligatorios:

```text
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
HE2_DECISION_PERFORMED = true
HE5_DECISION_PERFORMED = true
EXP12_REOPENED = false
G4_F01_STARTED = false
```

Todas las cifras citadas deben apuntar a IDs G3-F02 o G3-F03 concretos y a paths existentes.

---

## 12. Claim registry para Grupos 4–8

Crea:

```text
docs/analysis/group3/g3_claim_registry_v0.1.md
```

Debe ser una **fuente de control**, no prosa de artículo.

Para cada claim autorizado incluye al menos:

```text
claim_id
claim_text_controlled
claim_type
hypothesis_link
source_artifact
source_result_or_registry_ids
allowed_strength
scope
causal_status
mandatory_limitation
forbidden_overclaim
eligible_downstream_groups
```

Debe contener como mínimo claims controlados sobre:

1. HE2_A ranking temprano histórico vs flat.
2. HE2_A histórico vs hierarchical.
3. HE2_A histórico vs D1a.
4. HE2_B profundidad jerárquica 100→200.
5. Phase E candidate-pool coverage con estatus descriptivo.
6. Top-50 exclusivamente suplementario.
7. EXP11A sensibilidad no causal.
8. EXP11B sensibilidad descriptiva no inferencial.
9. Attempt06 como estado corregido vigente de 0B-05C.
10. EXP12 diversidad no estimable.
11. HE5 descripción ambigua/incompleta no estimable.
12. HE5 proximidad jerárquica descriptiva.
13. HE5 precedentes: buckets literales sin umbral de insuficiencia.
14. alcance interno Clase 87.
15. separación arquitectónica: ranking histórico, evidencia normativa y explicación controlada.
16. prohibición de equiparar retrieval histórico con exactitud global del RAG.
17. prohibición de equiparar evidencia normativa con corrección jurídica.
18. prohibición de equiparar explicación auditable con corrección clasificatoria/legal.

No redactes Introduction, Methods, Results ni Discussion del artículo.

---

## 13. `group3_closure_v0.1.json`

Este archivo es un **candidato de cierre**, no el cierre canónico todavía.

Debe incluir:

- G3-F01/F02/F03 como `CLOSED / APPROVED / INTEGRATED_TO_MAIN`;
- G3-F04 como `CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED`;
- refs de `main`, Plan, fichas, Prompt85 y commit de activación;
- blobs de G3-F01/F02/F03 consumidos;
- disposiciones HE2/HE5 generadas;
- lista de outputs de G3-F04;
- `PENDING_EXTERNAL_AUDIT = true`;
- `GROUP3_CLOSED = false`;
- `G4_F01_AUTHORIZED = false`;
- `NO_PENDING_INFERENTIAL_CALCULATIONS = true` solo si no queda ningún cálculo autorizado por G3-F01 pendiente;
- advertencias/limitaciones vigentes.

No escribas `GROUP3=CLOSED/APPROVED` dentro del candidato como estado vigente.

---

## 14. Validaciones terminales del candidato

Antes de publicar verifica:

```text
candidate_parent = 7d09f692da23367d3aba941db1febdca2baa8917
commits_ahead = 1
commits_behind = 0
changed_path_count = 3
```

Los únicos paths cambiados deben ser los tres de sección 10.

Valida además:

```text
HE2_OVERALL_DISPOSITION in {SUPPORTED, NOT_SUPPORTED, INCONCLUSIVE}
HE5_OVERALL_DISPOSITION in {SUPPORTED, NOT_SUPPORTED, INCONCLUSIVE}
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
GROUP3_CLOSED = false
PENDING_EXTERNAL_AUDIT = true
G4_F01_STARTED = false
```

Si falla:

```text
STOP / G3_F04_CANDIDATE_VALIDATION_FAILURE
```

Publica la rama con push normal, sin force-push.

---

## 15. Registro post-ejecución en rama de fichas

Solo después de publicar el candidato, vuelve a:

```text
docs/fichas-grupos-3-8
```

partiendo del commit de activación y deja:

```text
G3-F04 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G4-F01 = PROSPECTIVE / NOT_AUTHORIZED
```

Añade un bloque con:

```text
G3_F04_BRANCH = codex/group3-f04-hypothesis-disposition-v01
G3_F04_CANDIDATE_COMMIT = <sha>
G3_F04_CHANGED_PATH_COUNT = 3
HE2_OVERALL_DISPOSITION = <SUPPORTED|NOT_SUPPORTED|INCONCLUSIVE>
HE5_OVERALL_DISPOSITION = <SUPPORTED|NOT_SUPPORTED|INCONCLUSIVE>
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
PENDING_EXTERNAL_AUDIT = true
GROUP3_CLOSED = false
G4_F01_AUTHORIZED = false
RESULT = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

Haz un único commit administrativo post-ejecución y push normal.

**No modifiques Plan Maestro todavía.** Su cierre pertenece al microcierre posterior a auditoría externa.

---

## 16. Prohibiciones absolutas

Durante Prompt85 está prohibido:

- recalcular bootstrap, intervalos o métricas de G3-F03;
- calcular p-values;
- crear nuevos contrastes inferenciales;
- alterar B, seed, unidad, cluster, multiplicidad o estimandos;
- modificar G3-F01/G3-F02/G3-F03;
- modificar outputs experimentales congelados;
- promover Top-50 a primario;
- hacer inferencia sobre Phase E descriptivo;
- inventar un umbral de "precedentes insuficientes";
- inventar una variable de calidad de descripción;
- convertir ausencia de evaluación en fallo de HE5;
- reabrir EXP12;
- reejecutar retrieval/BM25/dense retrieval;
- modificar `article/main-manuscript`;
- modificar Plan Maestro;
- integrar el candidato G3-F04 a `main`;
- declarar Grupo 3 cerrado/aprobado antes de auditoría externa;
- activar o ejecutar G4-F01;
- redactar secciones del artículo o de la tesis;
- force-push, squash, rebase o amend de historia científica publicada.

---

## 17. Respuesta administrativa de Prompt85

Al finalizar crea en `codex/prompts-temporary`:

```text
codex_prompts_tmp/85_RESPUESTA_ACTIVAR_Y_EJECUTAR_G3_F04_DECISION_HE2_HE5_Y_CIERRE_CANDIDATO.md
```

Commitea únicamente ese archivo administrativo en la rama de prompts.

Reporte terminal exacto:

```text
PROMPT85 = COMPLETED | STOP

PREFLIGHT_MAIN =
PREFLIGHT_PLAN =
PREFLIGHT_FICHAS =
ARTICLE_HEAD_OBSERVED =
ARTICLE_HEAD_FINAL_OBSERVED =
ARTICLE_MODIFIED_BY_PROMPT85 = false

G3_F04_ACTIVATION_COMMIT =
G3_F04_BRANCH = codex/group3-f04-hypothesis-disposition-v01
G3_F04_CANDIDATE_COMMIT =
G3_F04_CANDIDATE_PARENT =
G3_F04_COMMITS_AHEAD =
G3_F04_COMMITS_BEHIND =
G3_F04_CHANGED_PATH_COUNT =
G3_F04_CHANGED_PATHS =

HE2_A_DISPOSITION =
HE2_B_HIERARCHICAL_DISPOSITION =
HE2_B_PHASE_E_DESCRIPTIVE_DISPOSITION =
HE2_OVERALL_DISPOSITION =
HE5_DESCRIPTION_COMPONENT =
HE5_HIERARCHY_COMPONENT =
HE5_PRECEDENT_COMPONENT =
HE5_INTERNAL_VALIDITY_COMPONENT =
HE5_OVERALL_DISPOSITION =

NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
GROUP3_CLOSED = false
PENDING_EXTERNAL_AUDIT = true
G4_F01_AUTHORIZED = false
G4_F01_STARTED = false

G3_F04_POSTEXEC_FICHAS_COMMIT =
PROMPT85_RESPONSE_COMMIT = THIS_COMMIT

G3_F04_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP3_FINAL_STATE = CLOSURE_CANDIDATE_PENDING_EXTERNAL_AUDIT / NOT_CLOSED

BLOCKERS =
WARNINGS =
```

Si hay STOP, no simules los campos faltantes; informa el bloqueo real.
