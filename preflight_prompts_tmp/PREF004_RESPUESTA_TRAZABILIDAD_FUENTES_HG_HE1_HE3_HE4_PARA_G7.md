# PREF004 — Respuesta de trazabilidad independiente de fuentes para HG, HE1, HE3 y HE4 antes de G7

```text
SOURCE_PROMPT = preflight_prompts_tmp/PREF004_TRAZABILIDAD_FUENTES_HG_HE1_HE3_HE4_PARA_G7.md
SOURCE_PROMPT_COMMIT = 21a2a016279c0e8b97fd319d09f070b46f9a46fa
MAIN_HEAD_OBSERVED = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_HEAD_OBSERVED = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_HEAD_OBSERVED = 804b59b73d7d2803d15e0adcb80546410a6718b8
PREF003_RESPONSE_COMMIT = 7782041ac6749f383779aedb7303e91a87177d8a
THESIS_MANIFEST_BRANCH_HEAD_OBSERVED = 21a2a016279c0e8b97fd319d09f070b46f9a46fa
THESIS_MANIFEST_BLOB_OBSERVED = 42b89b512b8db818238bfd0da22a7c75c207d9f1
THESIS_CURRENT_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
PREF004_IS_NON_GOVERNING = true
FORMAL_G7_AUTHORIZED = false
```

## 0. Alcance y regla aplicada

Esta ejecución reconstruye exclusivamente la trazabilidad primaria de `HG`, `HE1`, `HE3` y `HE4`. No activa Grupo 7, no modifica la tesis, no modifica `main`, Plan Maestro, fichas ni artículo, no recalcula métricas y no redecide hipótesis.

La tesis vigente es el `CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED / CORRECTION_BASELINE`; su contenido no se utiliza como fuente de verdad científica. El manifest vigente confirma que el documento fue redactado antes de los cierres posteriores y debe sincronizarse en un futuro G7-F02 únicamente desde fuentes cerradas/canónicas.

La secuencia formal observada permanece:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
G7-F01 = PROSPECTIVE / NOT_AUTHORIZED
G7-F02 = PROSPECTIVE
```

El Plan Maestro conserva un rezago documental para G6-F02 (`ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`) frente al registro vivo de fichas (`CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED`). Es `DOCUMENTARY_STATE_LAG`, no contradicción científica. Ambas fuentes mantienen Grupo 6 abierto y G7 no activado.

## 1. Fuentes primarias verificadas

### 1.1 Gobernanza

- `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` — rama `docs/plan-maestro-temporal-2026-08-31`, head `b74b96d0163807007e4579d86450dd235125b30f`.
- `docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md` — blob `699a9c6a3f19030b691896161606b2f5d9ff586c`.
- `docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md` — blob `29760a7d8394affbf9e942f00e3c7ce224762a59`.
- `docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md` — rama `docs/fichas-grupos-3-8`, head `804b59b73d7d2803d15e0adcb80546410a6718b8`.
- `preflight_tmp/THESIS_CURRENT_MASTER_MANIFEST_2026-09-22.md` — blob `42b89b512b8db818238bfd0da22a7c75c207d9f1`.

### 1.2 Grupo 1 — cierre experimental y disposiciones preservadas

- `outputs/evaluation/exp04_consolidated_closure_v0.2/gate_exp04_consolidated_closure_manifest_v0.2.json` — blob `643ca2a225572a8406302baa94cf6f8e7df90769`.
- `outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_hypothesis_status_registry_v0.2.csv` — blob `28cd7fbc492ecc4d4744ec5c3433ce5342213e79`.
- `outputs/evaluation/exp04_consolidated_closure_v0.2/summary_exp04_consolidated_closure_v0.2.md` — blob `e1fe802471753e459dceb8f4338b3d0fcc441e9f`.

El manifest de cierre registra `GROUP1 = CLOSED`, `group1_gate = APPROVED`, `HE3 = SUPPORTED`, `HE4 = PARTIALLY_SUPPORTED` y, de forma explícita, `oe1_he1_formal_status = NOT_FABRICATED_NO_CONSOLIDATED_ASSESSMENT_FOUND`. El summary repite que no se inventó una evaluación formal OE1/HE1.

### 1.3 Grupo 2 — reproducibilidad y trazabilidad

- `outputs/audits/g2a_reproducibility_v0.1/gate_g2a_reproducibility_manifest_v0.1.json` — blob `dacbf468fea850ea04632aaf9ade4b43e7748f17`.
- `outputs/audits/g2a_reproducibility_v0.1/summary_g2a_reproducibility_v0.1.md` — blob `37f4f96bb7dec27cdcbe5e3354d4b170a12177b8`.
- `outputs/audits/group2b_reproducibility_readiness_v0.2.json` — blob `802f85bf44922ca2dbeb395042908d5bd2efc133`.
- `outputs/audits/group2b_reproducibility_closure_v0.1.json` — blob `82e49fc9a04cd0bc19b95c863caf209d542144cd`.

El cierre G2B vigente en el Plan es `CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS`, con `BLOCKING_GAP_COUNT=0`, once limitaciones no bloqueantes, `ENVIRONMENT_REPRODUCIBILITY=COMPLETE_WITH_DECLARED_LIMITATION`, `CLEAN_CHECKOUT_REPRODUCIBILITY=COMPLETE_WITH_DECLARED_LIMITATION`, sin reejecución científica ni recomputación de resultados. Este cierre constituye evidencia primaria para reproducibilidad/trazabilidad, pero no contiene una disposición formal literal de HE1.

### 1.4 HE3 — integración y reranker diagnóstico

- `docs/exp04_phase_f_historical_normative_integration_v02_results.md` — blob `01a4573d34c029efb0b055c7b90202842e914549`.
- `outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_ranking_invariance.json` — blob `b295b399d80eee5fb21d1fd582cccae9afef4bdd`.
- `outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_traceability.json` — blob `4fbe3128ce8f453d9ae47eff6f76106b97b1ceea`.
- `outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_metrics_v0.2.json` — blob `15800df93cf77f4f2c6e83ac6cb692be013bbeb3`.
- `outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/summary.md` — blob `2e356497695551c9df61fb36e70d0cd6d2003daa`.

La Fase F confirma invariancia del ranking histórico en 1,056/1,056 casos y trazabilidad completa de 3,168/3,168 slots Top-3. La Fase G vigente es diagnóstica: 20 casos, sin cambio agregado en Top-1/Top-3/Top-5/MRR, `win/tie/loss = 0/19/0` entre los 19 casos con referencia en pool y `HE3 GLOBAL: SUPPORTED`. Estos valores se reportan porque ya están congelados en las fuentes; PREF004 no los calculó.

### 1.5 HE4 — explicación Top-3 y auditabilidad

- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_he4_joint_jk_assessment_v0.2.json` — blob `b617b4f397d0ffb4f8882ddda06790b1c539543e`.
- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_findings_v0.2.md` — blob `4b9dd1b3079235b2c54d5777fc788f0e98b27e32`.

El assessment conjunto J/K congela `he4_global = PARTIALLY SUPPORTED`: J preservó Top-3 y trazabilidad 50/50, mientras K clasificó 28/50 fichas como auditables bajo el umbral cualitativo congelado. Se preservan `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` y `EVALUATOR_MODALITY_DEVIATION`; la revisión cualitativa fue realizada por un `AI_EXPERT_ROLE`, no por la modalidad humana originalmente preparada. La evidencia estructural/auditable no equivale a corrección clasificatoria ni jurídica.

### 1.6 Fuentes posteriores de HE2/HE5 y arquitectura

Para no derivar una hipótesis general desde estados obsoletos se verificó además el cierre posterior:

- `outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json` — blob `d8f20498ebd26e467ba1916e3e0ed93d1dd06c61`: `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE`.
- `outputs/audits/group4_closure_v0.1.json` — blob `64ccc2068c15d0890bb9b978de8ed63d6d891034`: preserva la separación funcional ranking histórico / evidencia normativa / explicación controlada y sus guardrails, pero no congela una disposición formal de HG.

## 2. Matriz de fuentes por hipótesis

| hypothesis | thesis_current_disposition | formal_frozen_disposition_found | formal_disposition_value | formal_source_path | formal_source_commit_or_blob | evidence_sources[] | evidence_scope | superseded_sources_detected[] | traceability_status | recommended_G7_F01_freeze_source | future_G7_F02_action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `HG` | Respaldada dentro del alcance experimental, con cierre definitivo condicionado en la tesis | `false` | `NOT_APPLICABLE / NO_FORMAL_DISPOSITION_FOUND` | — | — | Group1 closure + HE3/HE4 current; Group2B closure; G3 HE2/HE5 disposition; G4 architecture/guardrails | Evidencia de componentes y límites, no dictamen agregado formal de HG | Dictamen agregado de la tesis vigente; no usarlo como autoridad terminal | `PARTIALLY_TRACEABLE / ADDITIONAL_SOURCE_REQUIRED` | Bundle mínimo: Group1 closure manifest/registry + Group2B closure/readiness + G3 hypothesis disposition + G4 architecture/guardrails; G7-F01 debe declarar expresamente que no existe freeze formal de HG o localizar uno adicional | `VERIFY`; conservar por separado la descripción arquitectónica alineada, pero no preservar el dictamen de HG como si estuviera congelado |
| `HE1` | Respaldada dentro de las condiciones documentadas del piloto | `false` | `NOT_APPLICABLE / NO_FORMAL_DISPOSITION_FOUND` | Group1 closure explicitly records absence of consolidated OE1/HE1 assessment | `643ca2a225572a8406302baa94cf6f8e7df90769`; `e1fe802471753e459dceb8f4338b3d0fcc441e9f` | G2A reproducibility artifacts + G2B readiness/closure + Plan terminal state | Reproducibilidad, identidad, procedencia y trazabilidad cerradas con limitaciones no bloqueantes; no equivalen por sí mismas a un dictamen formal HE1 | Dictamen HE1 de la tesis vigente; no existe un registry final que lo congele | `EVIDENCE_FROZEN_BUT_NO_FORMAL_HYPOTHESIS_DISPOSITION_FOUND` | `outputs/audits/group2b_reproducibility_closure_v0.1.json` + readiness v0.2 + Group1 manifest explicit no-assessment marker + Plan | `VERIFY`; no trasladar `RESPALDADA` como disposition congelada hasta que G7-F01 establezca el binding formal o localice una fuente terminal adicional |
| `HE3` | Parcialmente respaldada; componente reranker declarado provisional en la tesis | `true` | `SUPPORTED` | `outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_hypothesis_status_registry_v0.2.csv` + closure manifest | `28cd7fbc492ecc4d4744ec5c3433ce5342213e79`; `643ca2a225572a8406302baa94cf6f8e7df90769` | Fase F integration v0.2 + Fase G reranker v0.2 summary/metrics | Integración histórico-normativa + reranker diagnóstico; benchmark v0.2 | `docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md`; `docs/evaluacion_llm_rerank_pool_v0.1.md`; cifras legacy de la tesis | `FORMALLY_FROZEN_DISPOSITION_FOUND` | Group1 closure registry/manifest, con Fase F y Fase G como evidencia secundaria congelada | `REPLACE`: actualizar la tesis a `SUPPORTED` y sustituir íntegramente las cifras/relato legacy de integración y reranker por las fuentes v0.2, conservando el carácter diagnóstico del reranker |
| `HE4` | Respaldada en la tesis | `true` | `PARTIALLY_SUPPORTED` | `outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_hypothesis_status_registry_v0.2.csv` + HE4 qualitative findings | `28cd7fbc492ecc4d4744ec5c3433ce5342213e79`; `4b9dd1b3079235b2c54d5777fc788f0e98b27e32`; closure manifest `643ca2a225572a8406302baa94cf6f8e7df90769` | HE4 J/K joint assessment, automatic structural controls, frozen qualitative audit | Explicación Top-3 restringida, trazabilidad/verificabilidad/auditabilidad; no legal correctness | `docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md`; score/interpretación legacy de la tesis | `FORMALLY_FROZEN_DISPOSITION_FOUND` | Group1 closure registry/manifest + `he4_he4_joint_jk_assessment_v0.2.json` + `he4_qualitative_findings_v0.2.md` | `REPLACE`: cambiar el dictamen a `PARTIALLY_SUPPORTED`, sustituir métricas/lectura legacy y conservar explícitamente las dos limitaciones J/K y el guardrail no jurídico |

## 3. Auditoría individual

### 3.1 HG

```text
FORMULATION_MATCH = MATCH_WITH_CURRENT_THESIS_FORMULATION_USED_BY_PREF004
GOVERNING_SOURCE = NO_SINGLE_FORMAL_HG_DISPOSITION_SOURCE_FOUND
FORMAL_DISPOSITION_STATUS = NO_FORMAL_HYPOTHESIS_DISPOSITION_FOUND
EVIDENCE_STATUS = COMPONENT_EVIDENCE_FROZEN_BUT_AGGREGATE_HG_RULE_NOT_FROZEN
THESIS_STATE_ALIGNMENT = ARCHITECTURAL_CORE_ALIGNED / DISPOSITION_NOT_TRACEABLE_AS_FORMAL_FREEZE
G7_F01_SOURCE_FREEZE_RECOMMENDATION = FREEZE_COMPONENT_SOURCE_BUNDLE_AND_EXPLICITLY_RECORD_ABSENCE_OR_LOCATE_ADDITIONAL_FORMAL_HG_SOURCE
G7_F02_HANDLING_RECOMMENDATION = VERIFY_DISPOSITION; KEEP_ONLY_ARCHITECTURAL/BOUNDARY_TEXT_SUPPORTED_INDEPENDENTLY
```

No se infiere un nuevo dictamen de HG a partir de HE2, HE3, HE4, HE5 o de los guardrails. La tesis contiene un dictamen agregado, pero PREF004 no encontró un artefacto formal cerrado que lo congele como hipótesis general.

### 3.2 HE1

```text
FORMULATION_MATCH = MATCH_WITH_CURRENT_THESIS_FORMULATION_USED_BY_PREF004
GOVERNING_SOURCE = GROUP1_EXPLICIT_NO_CONSOLIDATED_HE1_ASSESSMENT + GROUP2B_REPRODUCIBILITY_CLOSURE_EVIDENCE
FORMAL_DISPOSITION_STATUS = NO_FORMAL_HYPOTHESIS_DISPOSITION_FOUND
EVIDENCE_STATUS = CLOSED_REPRODUCIBILITY_TRACEABILITY_EVIDENCE_WITH_NONBLOCKING_LIMITATIONS
THESIS_STATE_ALIGNMENT = THESIS_SAYS_SUPPORTED / FORMAL_FREEZE_NOT_FOUND
G7_F01_SOURCE_FREEZE_RECOMMENDATION = GROUP2B_CLOSURE_V0.1 + READINESS_V0.2 + GROUP1_NO_ASSESSMENT_MARKER + PLAN_TERMINAL_STATE
G7_F02_HANDLING_RECOMMENDATION = VERIFY_DISPOSITION; DO_NOT_PROMOTE_REPRODUCIBILITY_CLOSURE_TO_HE1_DECISION
```

El hallazgo negativo es primario y explícito: el manifest de cierre de Grupo 1 ordena no fabricar una evaluación consolidada OE1/HE1. Grupo 2 posteriormente cerró reproducibilidad y trazabilidad con limitaciones no bloqueantes, pero ese cierre tampoco declara literalmente `HE1 = ...`. Por regla de no redecisión, PREF004 no convierte esa evidencia en `SUPPORTED`.

### 3.3 HE3

```text
FORMULATION_MATCH = MATCH_WITH_CURRENT_THESIS_FORMULATION
GOVERNING_SOURCE = GROUP1_EXP04_CONSOLIDATED_HYPOTHESIS_STATUS_REGISTRY
FORMAL_DISPOSITION_STATUS = FORMALLY_FROZEN_DISPOSITION_FOUND
FORMAL_DISPOSITION = SUPPORTED
EVIDENCE_STATUS = FROZEN_F_PLUS_G_EVIDENCE
THESIS_STATE_ALIGNMENT = STALE / THESIS_PARTIALLY_SUPPORTED_IS_SUPERSEDED
G7_F01_SOURCE_FREEZE_RECOMMENDATION = GROUP1_CLOSURE_REGISTRY_AND_MANIFEST + PHASE_F + PHASE_G
G7_F02_HANDLING_RECOMMENDATION = REPLACE_LEGACY_HE3_BLOCKS_WITH_V0.2_CURRENT_STATE
```

La tesis usa un reranker anterior en el que Top-1/MRR disminuían y declara la prueba pendiente. El estado congelado v0.2 ya cerró la Fase G: no hubo mejora agregada ni degradación en la muestra diagnóstica, y el cierre consolidado fija `HE3 = SUPPORTED`. La integración F está separada del reranker G y ambas funciones deben mantenerse separadas en la redacción futura.

### 3.4 HE4

```text
FORMULATION_MATCH = MATCH_WITH_CURRENT_THESIS_FORMULATION
GOVERNING_SOURCE = GROUP1_EXP04_CONSOLIDATED_HYPOTHESIS_STATUS_REGISTRY + HE4_JK_ASSESSMENT
FORMAL_DISPOSITION_STATUS = FORMALLY_FROZEN_DISPOSITION_FOUND
FORMAL_DISPOSITION = PARTIALLY_SUPPORTED
EVIDENCE_STATUS = FROZEN_STRUCTURAL_AND_QUALITATIVE_EVIDENCE
THESIS_STATE_ALIGNMENT = STALE / THESIS_SUPPORTED_IS_SUPERSEDED
G7_F01_SOURCE_FREEZE_RECOMMENDATION = GROUP1_CLOSURE_REGISTRY_AND_MANIFEST + HE4_JK_ASSESSMENT + QUALITATIVE_FINDINGS
G7_F02_HANDLING_RECOMMENDATION = REPLACE_LEGACY_HE4_RESULT_AND_DISPOSITION
```

La tesis vigente describe HE4 como respaldada sobre un score legacy. El estado v0.2 distingue controles estructurales y evaluación cualitativa: la preservación de Top-3/trazabilidad no convierte automáticamente todas las fichas en auditables. El dictamen formal es `PARTIALLY_SUPPORTED`; además deben conservarse las limitaciones de esquema de prompt y modalidad del evaluador. Ningún resultado HE4 demuestra corrección clasificatoria o jurídica.

## 4. Mapa exacto de edición futura en la tesis

PREF004 no edita el Word. Para G7-F02, una vez autorizado y después del source freeze de G7-F01, los anchors actuales deben tratarse así:

| Anchor actual de tesis | Hipótesis | Estado respecto del freeze | Acción futura |
|---|---|---|---|
| Sección 3.1 — formulación HG | HG | formulación vigente; dictamen no congelado aquí | `KEEP` formulación / `VERIFY` cualquier regla decisional agregada |
| Sección 3.1 — formulación HE1 | HE1 | formulación vigente; no existe disposition formal localizada | `KEEP` formulación / `VERIFY` disposición |
| Sección 3.1 — formulación HE3 | HE3 | formulación compatible con el cierre | `KEEP` |
| Sección 3.1 — formulación HE4 | HE4 | formulación compatible con el cierre | `KEEP` |
| 4.1.5 Integración histórico–normativa | HE3-F | snapshot legacy | `REPLACE` desde Fase F v0.2 |
| 4.1.6 Reordenamiento diagnóstico con LLM | HE3-G | snapshot legacy/provisional | `REPLACE` desde reranker v0.2 |
| 4.1.7 Explicación auditable Top-3 | HE4 | métricas/lectura legacy | `REPLACE` desde J/K v0.2 |
| 4.2.1 Contrastación HE1 | HE1 | tesis dice respaldada sin disposition formal congelada localizada | `VERIFY`; no conservar el dictamen por defecto |
| 4.2.3 Contrastación HE3 | HE3 | tesis dice parcialmente respaldada; formal freeze dice SUPPORTED | `REPLACE` |
| 4.2.4 Contrastación HE4 | HE4 | tesis dice respaldada; formal freeze dice PARTIALLY_SUPPORTED | `REPLACE` |
| 4.2.6 Contrastación HG | HG | tesis declara respaldo agregado sin formal freeze localizado | `VERIFY`; separar arquitectura respaldada de disposition HG |
| Tabla 21 — fila HE1 | HE1 | dictamen no trazado a freeze formal | `VERIFY` |
| Tabla 21 — fila HE3 | HE3 | stale | `REPLACE` por `SUPPORTED` con fuente v0.2 |
| Tabla 21 — fila HE4 | HE4 | stale | `REPLACE` por `PARTIALLY_SUPPORTED` con limitaciones |
| Tabla 21 — fila HG | HG | disposition agregada no congelada | `VERIFY` |
| Discusión — integración/reranker | HE3 | cifras/estado legacy | `REPLACE` |
| Discusión — explicación/auditabilidad | HE4 | lectura legacy incompleta | `REPLACE` y mantener guardrail no jurídico |
| Discusión — reproducibilidad | HE1 | parte del texto sigue siendo útil, pero debe sincronizarse con G2B | `REPLACE/UPDATE` desde G2B sin convertir el cierre técnico en dictamen HE1 |
| Conclusiones — HE1 | HE1 | tesis afirma respaldo no formalmente congelado | `VERIFY` |
| Conclusiones — HE3 | HE3 | tesis conserva estado parcial/provisional | `REPLACE` |
| Conclusiones — HE4 | HE4 | tesis conserva respaldo total | `REPLACE` |
| Conclusiones — HG | HG | tesis conserva respaldo agregado | `VERIFY` |

## 5. Fuentes superseded / legacy que no deben gobernar G7-F02

```text
docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md
  blob = 52beb47274c163e7137608fa195398069fd84559
  role = LEGACY_HE3_INTEGRATION

docs/evaluacion_llm_rerank_pool_v0.1.md
  blob = f41b7f7132b2bcf97970b71bdf5e771981743dfb
  role = LEGACY_HE3_RERANKER

docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md
  blob = 3d0afba07643647cfe1bbace6a69ae41a2ab16b4
  role = LEGACY_HE4_EXPLANATION
```

La tesis vigente conserva resultados procedentes de ese estado experimental previo. Su presencia en el Word no los convierte en fuentes terminales.

También debe preservarse la precedencia científica posterior: el registry consolidado de Grupo 1 registra estados históricos de HE2/HE5 (`PARTIALLY_SUPPORTED`), pero esos dos fueron posteriormente redecididos formalmente por G3-F04 a `HE2 = SUPPORTED` y `HE5 = INCONCLUSIVE`. Por tanto, ningún futuro razonamiento sobre HG debe reutilizar los estados pre-G3 de HE2/HE5.

## 6. Riesgos y vacíos restantes

1. `PREF004-GAP-HE1-01`: existe evidencia cerrada y auditada de reproducibilidad/trazabilidad, pero no se localizó una disposición formal literal de HE1. El cierre de Grupo 1 confirma expresamente que no debe inventarse.
2. `PREF004-GAP-HG-01`: no se localizó una disposición formal congelada de HG ni una regla agregada cerrada que autorice derivarla automáticamente desde hipótesis específicas.
3. `PREF004-GOV-01`: el Plan Maestro está rezagado respecto del estado vivo de G6-F02. No afecta la ciencia de HG/HE1/HE3/HE4 y no habilita G7.
4. `PREF004-HE4-LIM-01`: HE4 mantiene `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`.
5. `PREF004-HE4-LIM-02`: HE4 mantiene `EVALUATOR_MODALITY_DEVIATION`; la evaluación cualitativa fue por `AI_EXPERT_ROLE`, no por evaluación humana.
6. `PREF004-G2B-LIM-01`: reproducibilidad permanece `COMPLETE_WITH_DECLARED_LIMITATION`; activos `HASH_BOUND_LOCAL_ONLY` y elementos declarados no recuperables no deben reinterpretarse como reproducibilidad perfecta.
7. `PREF004-G7-BLOCK-01`: G6-F02 no está aprobado y G6-F03 no está ejecutado; por secuencia, G7-F01/G7-F02 continúan no autorizados.

Ninguno de estos vacíos constituye una contradicción científica entre fuentes cerradas. Los dos primeros son vacíos de disposición formal y deben mantenerse explícitos hasta G7-F01.

## 7. Impacto sobre los cuatro VERIFY de PREF003 V02

| Hipótesis | Estado PREF003 | Resultado PREF004 | Justificación |
|---|---|---|---|
| HG | `VERIFY_AGAINST_OTHER_FROZEN_SOURCE` | `VERIFY_PARTIALLY_RESOLVED` | Se trazaron los componentes y sus fuentes actuales, pero no existe disposition formal HG localizada. |
| HE1 | `VERIFY_AGAINST_OTHER_FROZEN_SOURCE` | `VERIFY_PARTIALLY_RESOLVED` | Se trazó G2A/G2B y se verificó la ausencia explícita de assessment HE1 en Grupo 1; falta disposition formal HE1. |
| HE3 | `VERIFY_AGAINST_OTHER_FROZEN_SOURCE` | `VERIFY_RESOLVED` | Group1 closure congela `HE3 = SUPPORTED` y las Fases F/G v0.2 aportan evidencia primaria versionada. |
| HE4 | `VERIFY_AGAINST_OTHER_FROZEN_SOURCE` | `VERIFY_RESOLVED` | Group1 closure congela `HE4 = PARTIALLY_SUPPORTED` y J/K v0.2 conserva evidencia y limitaciones. |

PREF003 V02 no se modifica.

## 8. Respuesta a las preguntas obligatorias

### HG

1. Disposición formal final explícita: **no localizada**.
2. Artefacto exacto de disposición: **no aplica**.
3. Evidencia cerrada suficiente: existen fuentes cerradas para componentes, pero no una disposition agregada HG.
4. Materializado: arquitectura funcional, ranking/evidencia/explicación y límites. No materializado como freeze: regla formal de decisión HG.
5. Diferencia con tesis: la tesis sí declara HG respaldada; ese dictamen no quedó trazado a fuente formal terminal en PREF004.
6. G7-F02: mantener `VERIFY` para el dictamen; puede conservar arquitectura respaldada de forma independiente.
7. G7-F01: congelar el bundle HE1/HE2/HE3/HE4/HE5 + guardrails y registrar explícitamente la ausencia o localizar una fuente formal HG adicional.

### HE1

1. Disposición formal final explícita: **no localizada**.
2. El cierre de Grupo 1 explicita `NOT_FABRICATED_NO_CONSOLIDATED_ASSESSMENT_FOUND`.
3. Evidencia cerrada: sí, G2A/G2B para reproducibilidad, trazabilidad y limitaciones.
4. Materializado: inventarios, identidad, procedencia, reproducibilidad condicionada y limitaciones. No materializado: disposition HE1 formal.
5. Diferencia con tesis: la tesis declara HE1 respaldada; no existe fuente terminal localizada que congele ese label.
6. G7-F02: `VERIFY`, sin redecidir desde la evidencia técnica.
7. G7-F01: freeze de Group2B closure/readiness + Group1 no-assessment marker + Plan.

### HE3

1. Disposición formal final explícita: **sí**.
2. Fuente: Group1 closure registry/manifest, blobs `28cd7f...` y `643ca2...`.
3. Evidencia cerrada: Fase F + Fase G v0.2.
4. Materializado: invariancia y trazabilidad de integración; reranker diagnóstico; ambos cerrados.
5. Diferencia con tesis: tesis mantiene `parcialmente respaldada` y resultados previos; estado congelado es `SUPPORTED`.
6. G7-F02: `REPLACE` con el estado v0.2.
7. G7-F01: freeze del registry/manifest y evidencia F/G.

### HE4

1. Disposición formal final explícita: **sí**.
2. Fuente: Group1 closure registry + HE4 qualitative findings/J-K assessment.
3. Evidencia cerrada: estructural y cualitativa v0.2.
4. Materializado: preservación Top-3/trazabilidad y evaluación cualitativa; limitaciones J/K explícitas.
5. Diferencia con tesis: tesis declara respaldo total y usa métricas legacy; estado congelado es `PARTIALLY_SUPPORTED`.
6. G7-F02: `REPLACE`.
7. G7-F01: freeze del Group1 registry/manifest + J/K assessment/findings.

## 9. Controles

```text
PREF004_NO_G7_ACTIVATION = true
PREF004_NO_PLAN_MODIFICATION = true
PREF004_NO_FICHAS_MODIFICATION = true
PREF004_NO_MAIN_MODIFICATION = true
PREF004_NO_ARTICLE_MODIFICATION = true
PREF004_NO_THESIS_MODIFICATION = true
PREF004_NO_NEW_METRICS = true
PREF004_NO_NEW_INFERENCE = true
PREF004_NO_HYPOTHESIS_REDECISION = true
PREF004_SUPERSEDED_SOURCES_NOT_USED_AS_CURRENT = true
PREF004_PRIMARY_SOURCE_TRACEABILITY = true
PREF004_PENDING_EXTERNAL_AUDIT = true
```

## Resultado terminal

```text
READY_AS_HYPOTHESIS_SOURCE_PREFLIGHT_WITH_NONBLOCKING_GAPS
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
```
