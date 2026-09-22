# PREF003 V02 — Respuesta de preauditoría independiente de tesis para futuro G7-F02

```text
SOURCE_PROMPT = preflight_prompts_tmp/PREF003_V02_PREAUDITORIA_INDEPENDIENTE_TESIS_G7_F02.md
SOURCE_PROMPT_COMMIT = 15c5055e78ee1062d062dfdc5fe75e48c622b9a4
THESIS_MANIFEST = preflight_tmp/THESIS_CURRENT_MASTER_MANIFEST_2026-09-22.md
THESIS_MANIFEST_COMMIT = 4bea8c0034aa862b6b18de8d2307fdc8fffe80ea
MAIN_HEAD_OBSERVED = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_HEAD_OBSERVED = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_HEAD_OBSERVED = 804b59b73d7d2803d15e0adcb80546410a6718b8
PREF003_V02_RESULT = REVISION_REQUIRED
FORMAL_G7_F02_AUTHORIZED = false
PREF003_IS_NON_GOVERNING = true
```

## 0. Naturaleza, independencia y límite de esta ejecución

Esta ejecución es **pretrabajo metodológico independiente y no gobernante**. No activa G7-F01 ni G7-F02, no modifica la tesis, no modifica `main`, Plan Maestro, fichas, artículo ni artefactos científicos, no recalcula métricas y no redecide hipótesis.

La secuencia formal observada permanece:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
G7-F01 = PROSPECTIVE / NOT_AUTHORIZED
G7-F02 = PROSPECTIVE
```

La rama del Plan Maestro conserva un rezago documental respecto de G6-F02 y todavía lo muestra como `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`; la rama viva de fichas registra el estado posterior `CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED`. Esta divergencia es de gobernanza documental, no una contradicción científica, y no altera el bloqueo de G7: Grupo 6 aún no está cerrado.

La preauditoría independiente de las secciones A–G fue cerrada **antes** de abrir `preflight_tmp/PREG7_002_TESIS_PREAUDIT_G7_F02.md`. `PREG8-001` no fue consultado.

---

# A. Identidad y alcance

```text
THESIS_FILE_IDENTIFIED = true
THESIS_FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
THESIS_ORIGINAL_UPLOADED_FILENAME = Molleapasa_gv(5).docx
THESIS_MASTER_STATUS = CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED
THESIS_LIBRARY_PATH = /Tesis San Marcos/tesis_vigente/Molleapasa_gv_vigente_2026-09-22.docx
THESIS_LIBRARY_FILE_ID_OBSERVED = libfile_a4565dde90148191898d246f47c287e7
THESIS_LIBRARY_BACKING_FILE_ID_OBSERVED = file_0000000051cc820eba659f9c9c28771a
THESIS_EXPECTED_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
THESIS_EXPECTED_SIZE_BYTES = 4360620
THESIS_PARSED_PAGE_COUNT = 129
THESIS_HASH_RECHECK_STATUS = BYTE_HASH_RECHECK_NOT_AVAILABLE_IN_EXECUTOR
FORMAL_G7_F02_AUTHORIZED = false
PREF003_IS_NON_GOVERNING = true
```

La copia histórica `Molleapasa_gv(4).docx` no se utilizó como tesis vigente. La lectura se realizó exclusivamente sobre el archivo canónico indicado por el manifest. La superficie de archivos permitió lectura indexada completa y revisión visual de páginas con figuras, pero denegó la materialización de bytes originales; por ello no se recalculó localmente SHA-256 y se conserva literalmente el hash esperado del manifest, sin inferir identidad binaria adicional.

## A.1 Ground truth científico aplicado

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
H100 = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Guardrails preservados:

```text
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
historical retrieval superiority != global RAG accuracy
normative evidence != binding legal correctness
auditable explanation != classification/legal correctness
configurability != empirical generalization
```

Presentación de incertidumbre:

```text
HE2_A = 15 primary paired contrasts / 99% CI on paired differences / no arm-level CI
HE2_B = 1 primary Recall@200 - Recall@100 contrast / 95% CI
Phase E = descriptive only
Top50 = supplementary only
HE5 hierarchy/support = descriptive only
EXP12 = text-only / not estimable
P_VALUES = not calculated
```

---

# B. Mapa por macrosección

| section_or_topic | current_state | alignment_status | action | severity | primary_source | reason |
|---|---|---|---|---|---|---|
| 1.1 Situación problemática | Conceptualmente compatible con clasificación asistiva, fuentes documentales y revisión experta | ALIGNED_WITH_GUARDRAILS | KEEP_WITH_TERMINOLOGY_REVIEW | MINOR | G4 `G3C-015..018`; tesis vigente | Conserva la separación entre recomendación, evidencia y corrección jurídica; no depende de cifras legacy para su argumento central. |
| 1.2 Problema general y específicos | La arquitectura funcional coincide sustancialmente con el contrato actual | SUBSTANTIALLY_ALIGNED | KEEP_WITH_TERMINOLOGY_REVIEW | MINOR | G3/G4 architecture guardrails | Ranking histórico, evidencia normativa, Top-3 fijo y explicación local siguen vigentes; la formulación no debe interpretarse como generalización empírica fuera del benchmark. |
| 1.4 Objetivos | OE1–OE5 conservan la estructura funcional aprobada | SUBSTANTIALLY_ALIGNED | KEEP_WITH_TERMINOLOGY_REVIEW | MINOR | Tesis vigente + G4 claim map | Deben mantenerse sin convertir objetivos de auditabilidad en legal correctness. |
| Cap. 2 Marco teórico | Base conceptual generalmente compatible | PARTIALLY_ALIGNED / NOT_FULLY_REAUDITED_HERE | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | INFORMATIONAL | G4 literature contrast + corpus bibliográfico vigente | PREF003 no reaudita citas una por una; deben preservarse los límites de comparabilidad y no transferir cifras externas. |
| 3.1 Hipótesis | HE2 y HE5 coinciden literalmente con G3; HG/HE1/HE3/HE4 requieren su propia fuente cerrada | MIXED | KEEP_EXACT para HE2/HE5; VERIFY_AGAINST_OTHER_FROZEN_SOURCE para HG/HE1/HE3/HE4 | MAJOR | G3 hypothesis disposition | No redecidir hipótesis no cubiertas por el cierre G3/G4 usado aquí. |
| 3.1 Variables y operacionalización | Contiene métricas válidas, pero también categorías legacy de soporte y semántica previa | PARTIALLY_OBSOLETE | UPDATE_REQUIRED | MAJOR | G3 methods; G5 SECONDARY-02 | Debe reflejar SERIE, dependencia DAM, roles inferenciales/descriptivos y buckets congelados `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`. |
| 3.2 Tipo/diseño | La descripción offline y funcional es útil, pero no incorpora el tratamiento inferencial final por DAM | MATERIAL_METHODS_DRIFT | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | G3 inferential methods | La tesis actual presenta un marco descriptivo sin el bootstrap pareado por cluster DAM que sí fue ejecutado para HE2. |
| 3.3 Unidad de análisis | Declara correctamente la SERIE como unidad experimental/analítica | ALIGNED_BUT_INCOMPLETE_DEPENDENCY | KEEP_WITH_TERMINOLOGY_REVIEW | MAJOR | Plan + G3 methods | Debe añadirse explícitamente DAM/DECLARACIÓN como grupo de dependencia cuando corresponda y mantener esa dependencia en partición e inferencia. |
| 3.4 Población | Conserva el marco fuente histórico, pero las cantidades finales deben distinguirse del benchmark v0.2 | PARTIALLY_CURRENT | UPDATE_REQUIRED | MAJOR | Plan benchmark v0.2 | El marco fuente 11,320/4,232 puede conservarse si sigue trazado; los conjuntos finales deben ser v0.2. |
| 3.5 Tamaño de muestra | Describe 3,000/100/1,006 y niega finalidad inferencial | OBSOLETE | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Plan + G3 methods | El benchmark final es H100 2,950/28 DAM, DEV 100/6 DAM, EVAL 1,056/67 DAM/42 NANDINA; además existe inferencia cluster-aware dentro del benchmark fijo. |
| 3.6 Selección/partición | Describe estratificación por fila/NANDINA con seed 2026 y control solo por identificador | OBSOLETE_DEPENDENCY_CONTROL | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Plan v0.2 | v0.2 se materializa desde asignaciones explícitas de DAM; seed 2026 es procedencia/configuración, no regla aleatoria de asignación v0.2. |
| 3.7 Recolección, normalización y corpus | Mezcla componentes aún útiles con rutas y outputs de la partición v0.1 | MIXED | UPDATE_REQUIRED | MAJOR | Plan + artefactos científicos vigentes | Preservar el procedimiento documental que siga trazado, pero reemplazar referencias a datasets v0.1 como estado final. |
| 3.8 Análisis e interpretación | Afirma que no hubo inferencia ni CI | SCIENTIFICALLY_INCOMPATIBLE | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | G3 inferential results/methods | G3 ejecutó 15 contrastes HE2_A con CI 99% y un contraste HE2_B con CI 95%, usando bootstrap pareado por DAM; solo es correcto mantener que no se calcularon p-values. |
| 4.1.1 Curación/partición | Presenta 3,000/100/1,006; 69/44/62 códigos | LEGACY_V0_1 | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Plan benchmark v0.2 | Las cantidades finales de H100/EVAL y su gobernanza por DAM cambiaron. |
| 4.1.2 Corpus normativo | Contiene conteos documentales que no son el foco de G3–G5 | NEEDS_SOURCE_REVALIDATION | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | MAJOR | Fuente propia de corpus/Grupo1–2 | No se debe asumir vigencia solo porque G3–G5 no contradigan esos conteos. |
| 4.1.3 Recuperación normativa | Métricas legacy y lenguaje de “provisional / por reejecutar” | OBSOLETE | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | G5 MAIN-01, MAIN-02, SECONDARY-01 | Debe usar exclusivamente comparadores corregidos Attempt06 y roles inferencial/descriptivo congelados. |
| 4.1.4 Recuperación histórica | Top-1 0.8628, Top-3 0.9374, Top-10 0.9801, MRR 0.9062 sobre 1,006 | OBSOLETE | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | G5 MAIN-01 | H100 vigente: Top-1 0.509470, Top-3 0.671402, Top-5 0.763258, Top-10 0.891098, MRR@100 0.629708 sobre EVAL=1,056. |
| 4.1.5 Integración histórico–normativa | Reporta 373/633/0 y métricas del snapshot antiguo | LEGACY / NOT_CANONICAL_G5_PRESENTATION | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | MAJOR | Fuente específica HE3/integración aún por congelar en G7 | No reutilizar automáticamente cifras legacy; G3–G5 no autorizan redecidir HE3 desde este bloque. |
| 4.1.6 Reranker diagnóstico | Corrida de 20 casos declarada provisional y pendiente | LEGACY / VERIFY | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | MAJOR | Fuente cerrada propia de HE3 + estado correctivo vigente cuando aplique | No trasladar la corrida legacy a la tesis final sin binding explícito a la fuente congelada correspondiente. |
| 4.1.7 Explicación auditable | 50 casos y score 0.9520 pueden pertenecer a una fuente distinta de G3–G5 | VERIFY_REQUIRED | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | MAJOR | Fuente cerrada propia de HE4 | Conservar el guardrail no jurídico; revalidar números y dictamen HE4 contra su artefacto congelado. |
| 4.1.8 Errores/límites | Declara análisis pendiente de 1,006 descripciones y usa categorías legacy | INCOMPATIBLE_WITH_G3_G4_CLOSURE | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | G3 HE5 disposition; G5 SECONDARY-02 | Calidad descriptiva es NOT_ESTIMABLE; jerarquía/soporte son descriptivos y HE5 es INCONCLUSIVE. |
| 4.2 Contrastación | Usa reglas pre-G3 y niega inferencia estadística | OBSOLETE_DECISION_FRAME | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | G3/G4 | HE2 y HE5 deben reflejar cierres actuales; HG/HE1/HE3/HE4 deben verificarse sin redecisión. |
| 4.3 Discusión | Mezcla guardrails correctos con métricas y estados provisionales legacy | MIXED | REWRITE_REQUIRED | MAJOR | G4 interpretation + literature contrast | Reconstruir desde claims autorizados y calificadores actuales, preservando límites no causales/no jurídicos. |
| 4.3.7 Validez/reproducibilidad | Contiene límites útiles pero todavía afirma reejecuciones/análisis pendientes legacy | PARTIALLY_OBSOLETE | UPDATE_REQUIRED | MAJOR | G4 limitations + Group2B sources | Debe distinguir limitaciones vigentes de tareas ya cerradas y conservar el alcance 1,056/67/42. |
| Conclusiones | Repite métricas legacy, HE2 provisional, HE5 parcial y pendientes ya cerrados | OBSOLETE | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | G3–G5 + fuentes propias HE1/3/4/HG | No basta sustituir números: debe reconstruirse la cadena claim–evidencia–conclusión. |
| Recomendaciones | Son prospectivas y en general compatibles con el alcance limitado | GENERALLY_ALIGNED | KEEP_WITH_TERMINOLOGY_REVIEW | MINOR | G4 limitations | Deben formularse como futuras validaciones, no como generalización ya demostrada. |

---

# C. Matriz de discrepancias científicas

| finding_id | location_in_thesis | observed_thesis_claim_or_value | current_frozen_state | source_artifact | classification | severity | future_G7_F02_action |
|---|---|---|---|---|---|---|---|
| PREF003V02-F001 | 3.5, 3.6, 3.7.4; Tablas 4/10; 4.1.1; 4.2.1; conclusiones | `HIST=3000`, `DEV=100`, `EVAL=1006`; partición por estratificación NANDINA/seed y no solapamiento de `id_unico` | `H100=2950/28 DAM/66 NANDINA`; `DEV=100/6 DAM`; `EVAL=1056/67 DAM/42 NANDINA`; v0.2 con asignaciones explícitas por DAM | Plan Maestro v0.2 | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Reescribir todas las descripciones de partición, conteos y controles de dependencia; eliminar el split v0.1 como estado final. |
| PREF003V02-F002 | 3.6; 4.1.1; 4.3.2; conclusión 3 | Histórico `69` códigos; EVAL `62` códigos | H100 `66` NANDINA; EVAL `42` NANDINA | Plan Maestro | UPDATE_REQUIRED | MAJOR | Sustituir los conteos finales y revalidar toda interpretación dependiente de cobertura de códigos. |
| PREF003V02-F003 | 3.8, p. 78; 4.2, p. 105 | “No se aplicaron pruebas inferenciales, valores p ni intervalos de confianza” | Inferencia G3 ejecutada mediante `PAIRED_DAM_CLUSTER_PERCENTILE`; HE2_A 15 CI 99%; HE2_B 1 CI 95%; p-values no calculados | `g3_inferential_results_v0.1.json`; `g3_inferential_methods_and_checks_v0.1.md` | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Reescribir Métodos/Contrastación. Mantener únicamente `P_VALUES_CALCULATED=false`; incorporar el esquema de incertidumbre congelado. |
| PREF003V02-F004 | 3.3, 3.6, 3.8 | SERIE se identifica correctamente, pero DAM no gobierna de forma explícita partición/inferencia; se controla solo solapamiento de identificadores | `UNIT_OF_ANALYSIS=SERIE`; `DEPENDENCY_GROUP=DAM/DECLARACION`; bootstrap por cluster DAM | Plan + G3 methods | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Hacer explícita la dependencia intradeclaración en diseño, partición, estimando, remuestreo y limitaciones. |
| PREF003V02-F005 | 3.5 y 3.8 | “No se buscó estimar parámetros…”, usado como razón para excluir toda inferencia | G3 usa incertidumbre de remuestreo cluster-aware dentro del benchmark fijo, sin reclamar inferencia a población externa | G3 methods | REWRITE_REQUIRED | MAJOR | Separar `no external-population inference` de la inferencia/uncertainty efectivamente ejecutada dentro del benchmark. |
| PREF003V02-F006 | 4.1.4; Tabla 14; 4.2.2; 4.3.2; conclusión 3 | Histórico Top-1 `0.8628`, Top-3 `0.9374`, Top-5 `0.9592`, Top-10 `0.9801`, Top-50 `1.0000`, MRR `0.9062` | H100: Top-1 `0.5094697`, Top-3 `0.6714015`, Top-5 `0.7632576`, Top-10 `0.8910985`, Top-50 `0.9914773`, MRR@100 `0.6297077` | G5 MAIN-01; G5 APPENDIX-01 | REMOVE_OR_SUPERSEDE | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Reescribir desde G5; no hacer sustitución manual aislada de números en prosa legacy. |
| PREF003V02-F007 | 4.1.3; Tabla 12 | Flat/Hierarchical/Dual/Text2Trade con valores legacy sobre 1,006 | Comparadores corregidos Attempt06 sobre 1,056; Flat/Hierarchical/D1a gobernados para HE2_A | G5 MAIN-01; G5 APPENDIX-04 | REMOVE_OR_SUPERSEDE | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Sustituir por el estado corregido y separar evidencia primaria de contexto/sensibilidad. |
| PREF003V02-F008 | 4.1.3; Tabla 13; Figura 5 | `70/30` presentado como “mejor pool entregable” y unión diagnóstica junto a rendimiento ordinario con cifras legacy | Cuatro variantes `A_historical_defined` sostienen G3C-005; `70/30` es contexto descriptivo adicional; diagnostic union es techo diagnóstico, no ranking ordinario | G5 SECONDARY-01; G5 APPENDIX-05; G6-FIG-02 spec | REWRITE_REQUIRED | MAJOR | Presentar Phase E como descriptivo; no elegir variante por favorabilidad ni promover la unión diagnóstica. |
| PREF003V02-F009 | 4.2.2; Tabla 21; conclusión 8 | `HE2 = respaldada de forma provisional`; requiere futuras reejecuciones | `HE2 = SUPPORTED`; HE2_A y HE2_B hierarchical respaldadas por evidencia primaria; Phase E solo descriptivo | G3 hypothesis disposition; G4 matrix | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Reescribir la contrastación completa con los 15 CI 99% y el único contraste HE2_B con CI 95%. |
| PREF003V02-F010 | 4.2.2 y narrativa normativa | HE2 se sustenta mediante diferencias agregadas legacy sin incertidumbre y mezcla cobertura Phase E con decisión | Confirmatorio: HE2_A + HE2_B; descriptivo: Phase E; Top50 suplementario | G3/G4/G5 | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Separar explícitamente `PRIMARY_INFERENTIAL`, `DESCRIPTIVE` y `SUPPLEMENTARY`. |
| PREF003V02-F011 | 3.8.1; Tabla 8; Tabla 15; 4.2.5; 4.3.2 | Buckets `0`, `1`, `2-4`, `5-9`, `10+`; se interpreta “bajo soporte” y mayor dificultad | Buckets congelados: `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`; sin umbral prospectivo de insuficiencia | G5 SECONDARY-02; G3 HE5 | REMOVE_OR_SUPERSEDE | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Sustituir categorías y mantener solo lectura descriptiva; no renombrar buckets como insuficientes. |
| PREF003V02-F012 | 4.2.5; Tabla 21; conclusión 8 | `HE5 = parcialmente respaldada` | `HE5 = INCONCLUSIVE` | G3 hypothesis disposition; G4 synthesis | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Reescribir HE5, tabla resumen, discusión y conclusiones. |
| PREF003V02-F013 | 3.8.6; 4.1.8; 4.2.5; 4.3.7 | Se prevé medir/cerrar patrones de “descripciones ambiguas o incompletas” mediante análisis pendiente | `description_quality_operationalized=0`; componente `NOT_ESTIMABLE` | G3/G4 | REMOVE_OR_SUPERSEDE | MAJOR | No producir prevalencia/concentración post hoc; conservarlo como no-estimabilidad/limitación. |
| PREF003V02-F014 | 4.1.8; 4.3.7; conclusión 8 | `outputs/analysis/error_analysis_data_aduanas_clase87_v0.1/` “todavía debe generarse”; HE5 pendiente por 1,006 descripciones | Grupo 3/4 ya cerró HE5 como INCONCLUSIVE con componentes descriptivos/no estimables | G3/G4 | REMOVE_OR_SUPERSEDE | MAJOR | Eliminar lenguaje de tarea experimental pendiente y sustituir por el cierre vigente. |
| PREF003V02-F015 | 4.1.3; 4.2.2; 4.3.3; Tabla 24; conclusión 4 | BM25/Text2Trade/jerárquico “deben volver a ejecutarse” | Reejecuciones correctivas ya cerradas; Attempt06 es el estado actual | G4 G3C-009; G5 APPENDIX-04 | REMOVE_OR_SUPERSEDE | MAJOR | Eliminar pendientes ya resueltos y usar solo outputs corregidos vigentes. |
| PREF003V02-F016 | 4.1.5; Tabla 16; Figura 7 | 373 histórico-only, 633 ambas, 0 normativo-only y métricas históricas legacy | No es una de las nueve presentaciones canónicas G5 y no decide HE2/HE5 | G5 registry + scope boundary | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | MAJOR | Verificar contra artefactos cerrados de HE3/integración o retirar cifras del resultado final. |
| PREF003V02-F017 | 4.1.6; Tabla 17; Figura 8; 4.2.3; conclusión 6 | Reranker legacy: 20 casos, `0` ganados, `4` perdidos, `13` rankings incompletos; declarado provisional | No redecidido por G3–G5; cualquier estado correctivo aplicable debe estar ligado a su fuente propia congelada | Fuentes de HE3 + registros correctivos pertinentes | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | MAJOR | No conservar cifras ni dictamen hasta demostrar trazabilidad contra el freeze específico de HE3. |
| PREF003V02-F018 | 4.1.7; Tablas 18/19; Figura 9; 4.2.4; conclusión 7 | HE4: 50 casos, score medio `0.9520`, 49/50 conclusión auditable | G3–G5 no bastan para validar HE4 | Fuente cerrada propia de HE4 | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | MAJOR | Revalidar valores, muestra y dictamen; preservar que auditabilidad estructural ≠ corrección jurídica. |
| PREF003V02-F019 | 4.1.4 y decisión HE2 | Top-50 aparece integrado al relato principal histórico | Top-50 tiene rol `SUPPLEMENTARY_ONLY`, fuera de las cinco métricas primarias HE2_A | G5 APPENDIX-01; G3 | UPDATE_REQUIRED | MAJOR | Si se conserva, etiquetarlo como suplementario y sin rol decisional. |
| PREF003V02-F020 | Cap. 4 completo | No aparece `EXP11A` ni `EXP11B` por identificador; no hay incorporación explícita de sus sensibilidades cerradas | EXP11A = sensibilidad conjunta tamaño/composición no causal; EXP11B = descriptiva sobre diez pares observados | G5 APPENDIX-02/03; G4 | UPDATE_REQUIRED | MAJOR | Incorporar en discusión/limitaciones con sus calificadores; no inferir causalidad ni superpoblación de seeds. |
| PREF003V02-F021 | Cap. 4 completo | No aparece `EXP12` por identificador y no se registra su cierre actual | `EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE`; text-only | G3C-010; G4; G5 TEXT-ONLY disposition | UPDATE_REQUIRED | MAJOR | Incorporar como limitación/no-estimabilidad; no crear figura ni convertirlo en evidencia para HE5. |
| PREF003V02-F022 | Resultados/Discusión | Estado Attempt06 completo no está expuesto con su semántica actual | EV03 cambio agregado cero; EV04 descenso MRR diminuto no nulo; D1a cambios no nulos; efecto `METHOD_DEPENDENT` | G5 APPENDIX-04; G4 G3C-009 | UPDATE_REQUIRED | MAJOR | Usar Attempt06 únicamente donde corresponda; prohibido resumir 0B-05C como impacto global cero. |
| PREF003V02-F023 | 4.3 y conclusiones | Parte del texto usa el buen desempeño histórico como argumento general del componente | Superioridad de retrieval histórico se limita al benchmark interno y no equivale a accuracy global del RAG | G4 G3C-016 | KEEP_WITH_TERMINOLOGY_REVIEW | MAJOR | Mantener calificadores de alcance en cada pasaje comparativo y actualizar las cifras. |
| PREF003V02-F024 | Arquitectura, explicación, discusión | La tesis ya declara que evidencia/explicación no son corrección jurídica | Guardrails vigentes coinciden | G4 G3C-017/018 | KEEP_EXACT | INFORMATIONAL | Preservar estas delimitaciones al reescribir resultados; no debilitarlas. |
| PREF003V02-F025 | 4.3.7 y recomendaciones | La transferencia se presenta como futura, pero algunas formulaciones pueden sugerir portabilidad de protocolo | Configurabilidad/reaplicación del protocolo no demuestra generalización empírica | Scope/guardrails | KEEP_WITH_TERMINOLOGY_REVIEW | MINOR | Diferenciar reutilización del procedimiento de validez empírica en otras clases/aduanas/periodos. |
| PREF003V02-F026 | Figuras 4–10 | Siete figuras de resultados pertenecen al snapshot legacy; varias muestran 1,006, buckets previos o resultados fuera del catálogo | G6-F01 aprueba exactamente G6-FIG-01, G6-FIG-02 y G6-FIG-03; HE5/Top50/EXP11B/0B05C/diagnostic union son table-only; EXP12 text-only | G6 figure spec registry | REMOVE_OR_SUPERSEDE | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Retirar/reemplazar según la clasificación de la sección E; no usar renders G6-F02 aún no aprobados. |
| PREF003V02-F027 | Tabla 21 y conclusión general | HG, HE1, HE3 y HE4 aparecen con dictámenes del snapshot previo | PREF003 no está autorizado para redecidirlos desde G3–G5 | Fuentes propias cerradas de cada hipótesis | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | MAJOR | Congelar fuentes específicas en G7-F01/G7-F02 antes de conservar o cambiar dictamen. |
| PREF003V02-F028 | Todo el Cap. 4 | Numerosos resultados se expresan como proporciones descriptivas sin distinguir qué tiene CI inferencial y qué no | HE2_A/HE2_B tienen incertidumbre materializada; Phase E/HE5/EXP11A/EXP11B/Attempt06 roles descritos según contratos | G3–G5 | REWRITE_REQUIRED | BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE | Etiquetar cada familia por rol y evitar mezcla confirmatoria–descriptiva. |

## C.1 Valores actuales mínimos que no deben confundirse

HE2_A — valores observados del brazo histórico:

```text
Top-1 = 0.509469696969697
Top-3 = 0.6714015151515151
Top-5 = 0.7632575757575758
Top-10 = 0.8910984848484849
MRR@100 = 0.6297077493524843
```

HE2_B:

```text
Recall@100 = 0.10132575757575757
Recall@200 = 0.3039772727272727
paired_difference = 0.20265151515151514
95% CI = [0.06676310583580614, 0.34160130792395144]
```

HE5 support — categorías literales actuales:

```text
1 DAM   n=27  Top1=0.370370  Top3=0.703704  MRR=0.564447
2 DAM   n=21  Top1=0.047619  Top3=0.190476  MRR=0.239384
3-4 DAM n=425 Top1=0.691765  Top3=0.767059  MRR=0.760152
5+ DAM  n=583 Top1=0.399657  Top3=0.617496  MRR=0.551697
```

Estos valores HE5 son descriptivos y no autorizan etiquetar retrospectivamente ningún bucket como “insuficiente”.

---

# D. Auditoría de hipótesis

| hipótesis | texto/estado observado en tesis | estado/fuente permitida en PREF003 | clasificación | acción futura |
|---|---|---|---|---|
| HG | Tesis: respaldada dentro del alcance, pero cierre condicionado a reejecuciones y HE5/HE3 pendientes | G3–G5 no contienen una redecisión autorizada suficiente de HG | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | Congelar y leer fuente específica de HG antes de preservar/cambiar el dictamen; eliminar dependencias de “pendientes” ya cerrados solo cuando su fuente lo autorice. |
| HE1 | Tesis: respaldada | No redecidir desde G3–G5 | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | Verificar contra artefactos cerrados de integridad/reproducibilidad, incluidos límites Group2B. |
| HE2 | Tesis: “respaldada de forma provisional” | `HE2 = SUPPORTED`; HE2_A y HE2_B primary supported; Phase E descriptivo | REWRITE_REQUIRED | Sustituir la contrastación completa con evidencia G3/G5 y CI congelados; eliminar provisionalidad y pendientes legacy. |
| HE3 | Tesis: parcialmente respaldada; reranker legacy pendiente | No redecidir desde G3–G5 | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | Verificar integración y reranker contra su fuente congelada específica antes del candidato G7-F02. |
| HE4 | Tesis: respaldada, 50 casos/score 0.9520 | No redecidir desde G3–G5 | VERIFY_AGAINST_OTHER_FROZEN_SOURCE | Verificar valores y dictamen en su fuente congelada; preservar el límite auditabilidad ≠ corrección jurídica. |
| HE5 | Tesis: parcialmente respaldada | `HE5 = INCONCLUSIVE`; descripción NOT_ESTIMABLE; jerarquía/soporte DESCRIPTIVE_ONLY; scope limitation | REWRITE_REQUIRED | Reescribir resultados, contrastación, tabla resumen, discusión, limitaciones y conclusiones sin umbrales post hoc. |

No se ejecutó ninguna nueva decisión de hipótesis en PREF003 V02.

---

# E. Tablas y figuras

## E.1 Tablas relevantes de resultados

| elemento de tesis | contenido actual | clasificación | fundamento/acción |
|---|---|---|---|
| Tabla 10 — curación/deduplicación/partición | 3,000/100/1,006; 69/44/62 códigos | VERIFY | Debe reconciliarse con benchmark v0.2 y fuentes de partición; G5 no gobierna la curación. |
| Tabla 11 — auditoría corpus normativo | 9,785 registros; 7,648 NANDINA8; coberturas parentales | VERIFY | Revalidar contra su fuente congelada propia; no inferir vigencia desde G3–G5. |
| Tabla 12 — desempeño normativo | métricas legacy | UPDATE_FROM_G5 | Sustituir por comparadores corregidos actuales y roles congelados. |
| Tabla 13 — pool normativo | cifras legacy, 70/30 + unión diagnóstica | UPDATE_FROM_G5 | Usar G5-SECONDARY-01 y separar G5-APPENDIX-05 diagnóstico. |
| Tabla 14 — recuperación histórica | métricas legacy H=3,000/EVAL=1,006 | UPDATE_FROM_G5 | Reconstruir desde G5-MAIN-01; Top50 solo suplementario. |
| Tabla 15 — soporte de precedentes | buckets 1/2-4/5-9/10+ | UPDATE_FROM_G5 | Sustituir por G5-SECONDARY-02 literal 1 DAM/2 DAM/3-4 DAM/5+ DAM. |
| Tabla 16 — integración histórica–normativa | 373/633/0 + métricas legacy | VERIFY | Requiere fuente cerrada HE3/integración; no está en el sistema canónico G5. |
| Tabla 17 — reranker | 20 casos legacy/provisional | VERIFY | Requiere fuente cerrada HE3; no reutilizar por defecto. |
| Tablas 18–19 — explicación | 50 casos, controles y soporte | VERIFY | Requieren fuente cerrada HE4; guardrail no jurídico se mantiene. |
| Tabla 20 — patrones de error | mezcla resultados legacy/pendientes | REMOVE_AS_LEGACY | Debe desmontarse; HE5 actual se presenta por G5-SECONDARY-02 + texto de no-estimabilidad y límites. |
| Tabla 21 — contrastación de hipótesis | HE2 provisional; HE5 parcial; HE3/HG legacy | VERIFY | Rehacer HE2/HE5 desde G3–G5 y verificar HG/HE1/HE3/HE4 contra sus fuentes específicas. |
| Tabla 22 — contribución gestión información/conocimiento | síntesis conceptual | VERIFY | Puede preservarse tras retirar cualquier supuesto numérico/empírico obsoleto. |
| Tabla 23 — contraste con antecedentes | comparación cualitativa | VERIFY | Reconciliar con G4 literature contrast y sus clases de comparabilidad/forbidden claims. |
| Tabla 24 — amenazas a validez | incluye reejecuciones y análisis pendientes legacy | VERIFY | Actualizar con cierres reales y limitaciones G4/Group2B; conservar alcance interno. |

## E.2 Figuras

| figura de tesis | clasificación | razón |
|---|---|---|
| Figura 1 — jerarquía HS/NANDINA/nacional | KEEP | Conceptual; no es figura de resultados G6. Mantener sujeto a revisión terminológica/documental ordinaria. |
| Figura 2 — arquitectura funcional R-A-G | KEEP | La separación ranking histórico → evidencia → explicación Top-3 está alineada con G3/G4. |
| Figura 3 — flujo de transformación de datos/corpus | VERIFY | Conceptual/metodológica; revisar que no preserve el split v0.1 como estado final. |
| Figura 4 — comparación de desempeño temprano/cobertura | REPLACE_BY_G6_APPROVED_PRESENTATION | Usa métricas legacy y mezcla brazos; el diseño autorizado correspondiente es G6-FIG-01 para HE2 primaria. |
| Figura 5 — cobertura del pool normativo | REPLACE_BY_G6_APPROVED_PRESENTATION | Debe sustituirse por la especificación G6-FIG-02 de Phase E, sin líneas inferenciales y con 70/30 solo contextual. |
| Figura 6 — desempeño según precedentes | REMOVE_AS_LEGACY | HE5 soporte es `TABLE_ONLY_HE5_DESCRIPTIVE`; además usa buckets legacy. |
| Figura 7 — integración histórica–normativa | REMOVE_AS_LEGACY | No pertenece al catálogo de tres figuras G6 aprobado; cualquier resultado HE3 debe verificarse por separado. |
| Figura 8 — reranker diagnóstico | REMOVE_AS_LEGACY | No pertenece al catálogo G6 aprobado; el resultado HE3 debe verificarse y no autoriza una nueva figura. |
| Figura 9 — controles de explicación | REMOVE_AS_LEGACY | No pertenece al catálogo G6 aprobado; HE4 puede conservarse en texto/tabla solo tras verificación de su fuente propia. |
| Figura 10 — categorías de error | REMOVE_AS_LEGACY | HE5 está reservado a tabla descriptiva/texto; la figura mezcla categorías y denominadores legacy. |
| Figura 11 — banco histórico/corpus como gestión de información | VERIFY | Conceptual; puede conservarse si se armoniza con benchmark/roles actuales. |
| Figura 12 — datos/información/conocimiento/revisión experta | KEEP | Conceptual y consistente con que la revisión experta quede fuera del sistema; no es evidencia de rendimiento. |

La futura G7-F02 **no debe usar renders candidatos de G6-F02 como si fueran finales**. Solo se utiliza aquí la especificación aprobada G6-F01. G6-FIG-03 (EXP11A) ya está autorizada a nivel de especificación como figura de apéndice; su eventual inserción deberá esperar el cierre formal de Grupo 6 y el handoff G7 correspondiente, sin crear una cuarta figura de resultados.

---

# F. Scope estimado de futura G7-F02

```text
PRESERVABLE_CORE =
  - problema y objetivos en su arquitectura funcional, con revisión terminológica;
  - texto exacto de HE2 y HE5;
  - separación ranking histórico / evidencia normativa / explicación;
  - Top-3 fijo y LLM sin clasificación desde cero;
  - delimitación no vinculante/no jurídica y necesidad de revisión experta;
  - figuras conceptuales que no dependan de cifras legacy, tras verificación local.

CRITICAL_UPDATE_AREAS =
  - identidad del benchmark v0.2 y conteos H100/DEV/EVAL;
  - dependencia por DAM en diseño y partición;
  - operacionalización de métricas y roles de evidencia;
  - referencias a outputs v0.1, reejecuciones o análisis ya cerrados;
  - tablas/figuras de resultados;
  - alcance y limitaciones actuales, incluidas EXP11A/EXP11B/EXP12 y Attempt06.

CRITICAL_REWRITE_AREAS =
  - 3.5–3.8 en todo lo relativo a partición final, dependencia e inferencia;
  - 4.1.3–4.1.4 resultados HE2;
  - 4.1.8 HE5;
  - 4.2.2 HE2 y 4.2.5 HE5;
  - partes de 4.3 que usan cifras/estados legacy;
  - conclusiones cuantitativas y dictámenes HE2/HE5.

VERIFY_ONLY_AREAS =
  - HE1, HE3, HE4 e hipótesis general;
  - corpus normativo/cifras de curación no gobernadas por G3–G5;
  - integración histórica–normativa;
  - reranker diagnóstico;
  - explicación LLM de 50 casos;
  - literatura/citas y algunas figuras conceptuales.

LEGACY_CONTENT_TO_REMOVE =
  - 3,000/100/1,006 como partición final;
  - 69/62 códigos como estado final H100/EVAL;
  - métricas históricas 0.8628/0.9374/0.9801/0.9062 como resultados vigentes;
  - métricas normativas/pools anteriores al estado corregido;
  - buckets 0/1/2-4/5-9/10+ como soporte final;
  - HE2 provisional y HE5 parcialmente respaldada;
  - afirmación de que no hubo inferencia/CI;
  - pendientes de reejecución/análisis ya cerrados;
  - figuras de resultados legacy 4–10 fuera del catálogo G6 vigente.
```

La tesis no requiere reconstrucción total: el armazón conceptual es preservable, pero la capa empírica central exige una actualización amplia y trazable.

---

# G. Riesgos heredables a G8

```text
G8-RISK-001 = legacy partition 3000/100/1006 survives after v0.2 2950/100/1056
G8-RISK-002 = DAM dependency is omitted or reduced to case-id nonoverlap
G8-RISK-003 = legacy code counts 69/62 survive instead of H100=66 and EVAL=42
G8-RISK-004 = legacy historical metrics 0.8628/0.9374/0.9801/0.9062 survive
G8-RISK-005 = corrected normative Attempt06 sources are mixed with superseded outputs
G8-RISK-006 = thesis still states no inferential tests/CI despite G3 cluster-bootstrap CIs
G8-RISK-007 = 99% HE2_A CI is attached to arm values instead of paired differences
G8-RISK-008 = HE2_B Pool@200 is duplicated as a second confirmatory contrast
G8-RISK-009 = Phase E descriptive evidence is promoted to confirmatory inference
G8-RISK-010 = Top50 is used to decide HE2
G8-RISK-011 = HE2 remains provisional after SUPPORTED closure
G8-RISK-012 = HE5 remains partially supported after INCONCLUSIVE closure
G8-RISK-013 = support buckets are relabeled retrospectively as insufficient/low support
G8-RISK-014 = ambiguous/incomplete-description prevalence is inferred despite NOT_ESTIMABLE
G8-RISK-015 = EXP11A is interpreted as an isolated/monotonic causal size effect
G8-RISK-016 = EXP11B is generalized to a seed superpopulation or 10x1056 pseudo-independent cases
G8-RISK-017 = EXP12 is omitted, reopened, graphed as performance, or used for/against HE5
G8-RISK-018 = 0B05C is summarized as globally zero impact instead of method-dependent Attempt06 state
G8-RISK-019 = legacy figures 4-10 coexist with or contradict G6 approved presentation
G8-RISK-020 = historical retrieval superiority is rewritten as global RAG/classification accuracy
G8-RISK-021 = normative evidence or auditable explanation is rewritten as legal correctness
G8-RISK-022 = configurability/reusability of protocol is presented as empirical generalization
G8-RISK-023 = HG/HE1/HE3/HE4 are silently redecided without their frozen sources
G8-RISK-024 = article and thesis retain different experimental snapshots
G8-RISK-025 = future edited Word is not rebound to an exact SHA-256 after the current manifest snapshot
G8-RISK-026 = Plan/fichas G6-F02 documentary lag is mistaken for authorization/closure state
```

---

# H. Comparación posterior con PREG7-002

`preflight_tmp/PREG7_002_TESIS_PREAUDIT_G7_F02.md` se abrió únicamente después de cerrar los hallazgos independientes anteriores. Su estado permanece `SELF_GENERATED_UNAUDITED / NON_GOVERNING`.

## CONVERGENCES

1. Ambos análisis identifican como bloqueante el split legacy `3000/100/1006` frente al benchmark v0.2 y la necesidad de gobernar dependencia por DAM.
2. Ambos identifican como obsoletas las métricas históricas `0.8628/0.9374/0.9801/0.9062`.
3. Ambos concluyen que HE2 ya no es provisional y debe quedar `SUPPORTED`, usando G5-MAIN-01/G5-MAIN-02 y los CI congelados.
4. Ambos concluyen que HE5 no puede quedar “parcialmente respaldada” y debe reflejar `INCONCLUSIVE`, con descripción `NOT_ESTIMABLE` y jerarquía/soporte descriptivos.
5. Ambos rechazan los buckets legacy de soporte y preservan las categorías literales `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM` sin umbral de insuficiencia.
6. Ambos detectan que el lenguaje de reejecuciones normativas pendientes está superseded.
7. Ambos tratan integración, HE3 y HE4 como áreas que requieren verificación contra fuentes propias, sin redecisión desde G3–G5.
8. Ambos preservan como núcleo útil la arquitectura funcional, Top-3 fijo y guardrails no jurídicos.
9. Ambos concluyen que resultados, contrastación, discusión empírica y conclusiones requieren una actualización amplia, no un simple reemplazo manual de cifras.
10. Ambos reconocen que el catálogo G6 gobierna las figuras de resultados y que no deben generarse figuras legacy fuera de ese catálogo.

## DIVERGENCES

1. PREG7-002 se construyó sobre `Molleapasa_gv(4).docx`; PREF003 V02 está vinculado exclusivamente al current working master `Molleapasa_gv_vigente_2026-09-22.docx` derivado de `Molleapasa_gv(5).docx` y fijado por manifest.
2. PREG7-002 declara `THESIS_SHA256_VERIFIED=false` y master no establecido. En el estado actual existe manifest autor-confirmado con SHA-256 esperado `08b48e...3aed`; PREF003 pudo verificar identidad documental pero no recalcular bytes por limitación de materialización.
3. PREG7-002 singulariza la Figura 7 como pendiente; en el current working master la Figura 7 está efectivamente insertada/renderizada. La conclusión de fondo —no pertenece al catálogo G6— converge, pero el estado material de la figura difiere.
4. PREF003 V02 clasifica explícitamente todas las Figuras 4–10 de resultados, no solo la Figura 7, y determina que las Figuras 4–5 deben ser reemplazadas por presentaciones G6 aprobadas y 6–10 retiradas como legacy salvo que una gobernanza posterior las autorice.
5. PREF003 V02 eleva a hallazgo bloqueante la contradicción metodológica “no se aplicaron pruebas inferenciales ni intervalos de confianza”, aspecto no materializado como hallazgo independiente en PREG7-002.

## UNSUPPORTED_ITEMS_IN_PREG7_002

1. La identidad de trabajo `Molleapasa_gv(4).docx` ya no es válida para preflight nuevo: el manifest vigente la clasifica como copia histórica anterior.
2. `THESIS_APPROVED_MASTER_STATUS = NOT_ESTABLISHED` está superseded para el propósito de identidad de trabajo: existe `CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED`. Esto no equivale a aprobación final de tesis ni a cierre G7.
3. La afirmación de que la Figura 7 está “marcada como pendiente” no describe el current working master; la figura está insertada en la página correspondiente. Su contenido sigue siendo legacy y no gobernado por G6.
4. No se identificó otro hallazgo científico material de PREG7-002 que contradiga las fuentes G3–G6 revisadas; su principal limitación es haber auditado una copia ya superseded.

## MISSING_ITEMS_IN_PREG7_002

1. No aísla como discrepancia científica propia la negación explícita de inferencia/CI en 3.8 y 4.2 frente al bootstrap pareado por DAM de G3.
2. No desarrolla la obligación de reflejar en Métodos el estimando series-weighted y el agrupamiento DAM a lo largo de partición, emparejamiento e incertidumbre.
3. No congela explícitamente en su matriz los tres conteos completos del benchmark v0.2: H100 `2950/28 DAM/66 NANDINA`, DEV `100/6 DAM`, EVAL `1056/67 DAM/42 NANDINA`.
4. No audita de forma exhaustiva las Figuras 4–10 del current working master contra el catálogo G6.
5. No registra como omisión que el texto actual no contiene `EXP11A`, `EXP11B` ni `EXP12` por identificador, pese a que G4/G5 les asignan roles obligatorios de sensibilidad/limitación para escritura downstream.
6. No destaca por separado el rol suplementario de Top-50 y el riesgo de usarlo como evidencia decisional.
7. No desarrolla la divergencia exacta de Phase E: cuatro variantes formales para G3C-005, `70/30` solo contextual y diagnostic union como techo diagnóstico, no rendimiento ordinario.
8. No identifica como riesgo específico que el estado Attempt06 debe conservar simultáneamente EV03 cero, EV04 descenso MRR diminuto no nulo y D1a cambio no nulo, sin narrativa global de impacto cero.
9. No registra la imposibilidad técnica de recalcular el SHA-256 en este ejecutor y la necesidad de rebind binario antes de una futura edición formal.
10. No registra el rezago documental actual Plan/fichas de G6-F02, que debe reconciliarse por gobernanza y no por inferencia del redactor.

---

# I. Fuentes primarias consultadas

## Gobernanza / preflight

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
  branch = docs/plan-maestro-temporal-2026-08-31
  head = b74b96d0163807007e4579d86450dd235125b30f
  blob = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57

docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
  branch = docs/fichas-grupos-3-8
  blob = 29760a7d8394affbf9e942f00e3c7ce224762a59

docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
  branch = docs/fichas-grupos-3-8
  blob = 179e1f1f178ef545af6504a744fcdb1c621c98e9

preflight_tmp/THESIS_CURRENT_MASTER_MANIFEST_2026-09-22.md
  commit = 4bea8c0034aa862b6b18de8d2307fdc8fffe80ea
  blob = 3240f4ca15712e6921a06f4caf1863a8478c962b

preflight_prompts_tmp/PREF001_RESPUESTA_PRETRABAJO_G7_F01_FUENTES.md
  commit = 90f5baef9a800ca0b44334af23a7a8caeff8fd09

preflight_prompts_tmp/PREF002_RESPUESTA_CORRECCION_PREF001_IDENTIDAD_TESIS_Y_PROMPT106.md
  commit = c159b17bb2747bd2231db374422be2b11fa69616
```

## Grupo 3

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
  blob = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61

outputs/analysis/group3/g3_inferential_results_v0.1.json
  blob = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc

docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
  blob = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
```

## Grupo 4

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
  blob = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab

outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
  blob = da0351cb523fc7f3b45a83e072765a07f809b7fe

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
  blob = 129a67b15db429b86af059d61753b1942c8f243f

outputs/analysis/group4/g4_limitations_registry_v0.1.json
  blob = ae00b93431e912cb78a58344057d9bf7a51fcd47

docs/analysis/group4/g4_literature_contrast_v0.1.md
  blob = 2baff53184b17c23380693235a2f3257de5e2bba
```

## Grupo 5

```text
outputs/results/group5/g5_table_registry_v0.1.json
  blob = 4fe9318d52fad093066ff9f42d524fc95e436245

docs/results/group5/g5_canonical_tables_v0.1.md
  blob = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d

docs/results/group5/g5_appendix_registry_v0.1.md
  blob = 9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a

outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
  blob = cb68583ee2260e4455796bac99ad90995ca7ef92
outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
  blob = 359e4e19b5ef1d44983c03039162209293b2a44c
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
  blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61
outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
  blob = 727076a0d09735a87f45f6522d2a0ecead2cee17
outputs/results/group5/tables/g5_appendix_01_top50_supplementary.csv
  blob = c2ded734af9ea340d715483b6e8cc00a7536dfea
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
  blob = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403
outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv
  blob = 76c8c6c588c7e809c6be64f7192f497c491fb692
outputs/results/group5/tables/g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv
  blob = 490ef570fa1674e2eecad7f0a3cdf34ba96204db
outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv
  blob = f43cce08d1d7bc3cef64698dbebf14eae4b26ed5
```

## Grupo 6

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
  main head observed = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
  figure_spec_count = 3
```

No se utilizaron renders candidatos G6-F02 como evidencia editorial final.

## Tesis

```text
Molleapasa_gv_vigente_2026-09-22.docx
Library file id = libfile_a4565dde90148191898d246f47c287e7
Backing file id = file_0000000051cc820eba659f9c9c28771a
Parsed pages reviewed = 129 / 129
Expected SHA-256 from manifest = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
Raw-byte materialization = unavailable in executor
```

## Comparación posterior únicamente

```text
preflight_tmp/PREG7_002_TESIS_PREAUDIT_G7_F02.md
role = SELF_GENERATED_UNAUDITED / NON_GOVERNING
read_after_independent_findings_closed = true
```

---

# J. Controles obligatorios

```text
PREF003_EXACT_CURRENT_THESIS_BOUND = true
PREF003_CURRENT_THESIS_MANIFEST_READ_FIRST = true
PREF003_HISTORICAL_GV4_NOT_USED_AS_CURRENT_THESIS = true
PREF003_INDEPENDENT_ANALYSIS_BEFORE_PREG7_002_READ = true
PREF003_NO_G7_ACTIVATION = true
PREF003_NO_PLAN_MODIFICATION = true
PREF003_NO_FICHAS_MODIFICATION = true
PREF003_NO_MAIN_MODIFICATION = true
PREF003_NO_ARTICLE_MODIFICATION = true
PREF003_NO_THESIS_MODIFICATION = true
PREF003_NO_NEW_METRICS = true
PREF003_NO_NEW_INFERENCE = true
PREF003_NO_HYPOTHESIS_REDECISION = true
PREF003_G3_G4_G5_SOURCE_TRACEABILITY = true
PREF003_G6_RENDER_NOT_TREATED_AS_FINAL = true
PREF003_LEGACY_OUTPUTS_IDENTIFIED = true
PREF003_PREG7_002_TREATED_AS_NON_GOVERNING = true
PREF003_PREG8_001_NOT_READ = true
PREF003_PENDING_EXTERNAL_AUDIT = true
```

## Resultado terminal

```text
REVISION_REQUIRED
```

La tesis vigente es accesible y está inequívocamente identificada, por lo que no corresponde un resultado `BLOCKED_CURRENT_THESIS_UNAVAILABLE`. El resultado `REVISION_REQUIRED` se debe a discrepancias científicas bloqueantes en partición/dependencia, inferencia, resultados HE2, disposición HE5 y presentación legacy. Este resultado no aprueba G7-F02 ni la tesis.

PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true