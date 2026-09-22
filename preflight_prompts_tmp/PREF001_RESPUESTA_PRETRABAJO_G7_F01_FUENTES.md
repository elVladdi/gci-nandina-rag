# PREF001 — Respuesta de pretrabajo independiente para G7-F01

```text
SOURCE_PROMPT = preflight_prompts_tmp/PREF001_EJECUTAR_PRETRABAJO_G7_F01_FUENTES.md
SOURCE_PROMPT_COMMIT = 6e8a26a2f2ed587f5cb01b2b4043797a76e2d17b
PREF001_RESULT = READY_AS_PREFLIGHT_WITH_NONBLOCKING_GAPS
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
FORMAL_G7_F01_AUTHORIZED = false
G7_F01_ACTIVATED = false
```

## 0. Naturaleza y límites

Este artefacto es un **pretrabajo metodológico no gobernante**. No activa G7-F01, no aprueba G6-F02, no ejecuta G6-F03, no modifica Plan Maestro, fichas, `main`, artículo o tesis, y no sustituye el futuro output formal de G7-F01.

La secuencia formal preservada es:

```text
G6-F02
→ G6-F03
→ GROUP6 = CLOSED / APPROVED
→ G7-F01
→ G7-F02
→ G7-F03
→ G8
```

El análisis independiente de las Secciones A–G fue cerrado antes de abrir `preflight_tmp/PREG7_001_G7_F01_SOURCE_FREEZE_PREFLIGHT.md`. `PREG7-002` y `PREG8-001` no fueron consultados.

---

# A. Estado de gobernanza observado

## A.1 Refs observadas

```text
SCIENTIFIC_MAIN_HEAD = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_BRANCH = docs/plan-maestro-temporal-2026-08-31
PLAN_HEAD = b74b96d0163807007e4579d86450dd235125b30f
PLAN_PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
PLAN_BLOB = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
FICHAS_BRANCH = docs/fichas-grupos-3-8
FICHAS_HEAD = 804b59b73d7d2803d15e0adcb80546410a6718b8
ARTICLE_BRANCH = article/main-manuscript
ARTICLE_HEAD = 0890a25027047e48584a8ae20aaea359a0bfba87
```

## A.2 Estado operativo de Grupo 6

La fuente de fichas viva registra:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
G7-F01 = PROSPECTIVE / NOT_AUTHORIZED
G7-F02 = PROSPECTIVE
G7-F03 = PROSPECTIVE
```

El candidato remoto de G6-F02 existe y fue verificado en:

```text
branch = figures/g6-f02-render-v01
commit = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
parent = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

No se auditó ni aprobó ese render en PREF001.

## A.3 Divergencia documental interna detectada

El Plan Maestro vigente ya refleja el cierre de G6-F01 y `GROUP6 = IN_PROGRESS`, pero todavía registra G6-F02 como:

```text
ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

mientras que la rama de fichas viva registra el estado posterior:

```text
CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

Clasificación independiente:

```text
GOVERNANCE_DRIFT_ID = PREF001-GOV-001
TYPE = DOCUMENTARY_STATE_LAG
SCIENTIFIC_CONTRADICTION = false
G7_ACTIVATION_IMPACT = NONE_BEYOND_EXISTING_BLOCK
RECONCILIATION_OWNER = EXPERIMENTAL_GOVERNANCE
```

No se resuelve por inferencia. Ambas fuentes coinciden en lo sustantivo para este preflight: Grupo 6 no está cerrado y G7-F01 no puede activarse.

---

# B. Inventario de fuentes para futuro freeze

| Dominio | Estado PREF001 | Fuentes rectoras verificadas | Condición para freeze formal futuro |
|---|---|---|---|
| Grupo 3 | `READY_FOR_FUTURE_FREEZE` | `g3_hypothesis_disposition_v0.1.json` y trazas G3 asociadas | Preservar cierre operacional posterior, aunque algunos artefactos conserven headers históricos de candidato |
| Grupo 4 | `READY_FOR_FUTURE_FREEZE` | `g4_result_claim_evidence_matrix_v0.1.json/.csv`, `g4_interpretation_synthesis_v0.1.md`, `g4_limitations_registry_v0.1.json`, `g4_literature_contrast_v0.1.md` | Mantener 18 claims, 11 limitaciones no bloqueantes, 8 discussion points autorizados y 14 prohibidos |
| Grupo 5 | `READY_FOR_FUTURE_FREEZE` | `g5_table_registry_v0.1.json`, `g5_canonical_tables_v0.1.md`, `g5_appendix_registry_v0.1.md`, nueve CSV canónicos | Mantener roles MAIN/SECONDARY/APPENDIX/TEXT_ONLY; no promover evidencia descriptiva/no estimable |
| Grupo 6 | `PARTIALLY_READY` | `g6_figure_spec_registry_v0.1.json` listo; candidato G6-F02 remoto existente pero no aprobado | Requiere G6-F02 aprobado, G6-F03 ejecutado/auditado y Grupo 6 `CLOSED / APPROVED` antes del freeze G7 |
| Master tesis/Word | `BLOCKED_MISSING_IDENTITY` | No se identificó una copia de tesis Word que pueda probarse como master vigente | Deben verificarse simultáneamente filename, master status y SHA-256 antes de G7-F01 formal |
| Gobernanza artículo | `PARTIALLY_READY` | onboarding completo en `article/main-manuscript`; master y gate editorial identificados | Requiere reconciliar snapshot experimental editorial antes de sincronización formal G7 y resolver gap de trazabilidad de decisiones |
| Controles bibliográficos/literatura | `READY_FOR_FUTURE_FREEZE` | `BIBLIOGRAPHIC_FRAMEWORK.md`, corpus editorial congelado usado por G4-F03 y `g4_literature_contrast_v0.1.md` | No introducir nueva literatura sin flujo `CANDIDATE_NEW → APPROVED_NEW`; verificar PDF completo para toda cita nueva |
| Reglas institucionales UNMSM | `NOT_READY` | No se identificó en este preflight una fuente institucional congelada | G7-F01 formal debe registrar la fuente institucional vigente disponible, sin inventar reglas |

### B.1 Estado científico congelable de G3–G5

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

### B.2 Estado de G6

El registry G6-F01 integrado especifica exactamente tres figuras:

```text
G6-FIG-01 = HE2_A + HE2_B / PRIMARY_INFERENTIAL / MAIN
G6-FIG-02 = PHASE_E / DESCRIPTIVE_SUPPLEMENTARY / SECONDARY
G6-FIG-03 = EXP11A / DESCRIPTIVE_SENSITIVITY_NONCAUSAL / APPENDIX
```

Y preserva como no-figura:

```text
EXP11B = TABLE_ONLY_DESCRIPTIVE_SENSITIVITY
HE5_COMPONENTS = TABLE_ONLY_HE5_DESCRIPTIVE
TOP50 = TABLE_ONLY_SUPPLEMENTARY
0B05C_ATTEMPT06 = TABLE_ONLY_CORRECTIVE_SENSITIVITY
PHASE_E_DIAGNOSTIC_UNION = TABLE_ONLY_DIAGNOSTIC
EXP12 = TEXT_ONLY_NOT_ESTIMABLE_NO_PERFORMANCE_FIGURE
```

Ese registry sí está listo como fuente de diseño, pero los renders de G6-F02 no están aprobados y G6-F03 no ha cerrado captions/accesibilidad/cierre. Por ello **no se congela G6 prematuramente**.

---

# C. Matriz preliminar claim → presentación → destino

Esta matriz usa como fuente primaria la matriz G4-F01 de 18 claims, el sistema G5 y el registry G6. Los destinos son preliminares para el futuro contrato G7 y no activan ninguna sección.

| Claim | Rol científico | Evidencia / tabla canónica | Figura | Destino tesis futuro | Destino artículo futuro | Calificación obligatoria |
|---|---|---|---|---|---|---|
| `G3C-001` | HE2_A primario inferencial | `G5-MAIN-01`; G3F03-0001:0005 | `G6-FIG-01` | `TESIS_RESULTADOS` | `ARTICULO_RESULTS` | Contraste pareado no causal; incertidumbre cluster-aware en benchmark interno; no global RAG accuracy |
| `G3C-002` | HE2_A primario inferencial | `G5-MAIN-01`; G3F03-0006:0010 | `G6-FIG-01` | `TESIS_RESULTADOS` | `ARTICULO_RESULTS` | Contraste pareado no causal; no corrección jurídica ni generalización externa |
| `G3C-003` | HE2_A primario inferencial | `G5-MAIN-01`; G3F03-0011:0015 | `G6-FIG-01` | `TESIS_RESULTADOS` | `ARTICULO_RESULTS` | Usar exclusivamente D1a corregido Attempt06; no fuentes superseded |
| `G3C-004` | HE2_B primario inferencial | `G5-MAIN-02`; G3F03-0016 | `G6-FIG-01` | `TESIS_RESULTADOS` | `ARTICULO_RESULTS` | Un solo contraste Recall@200−Recall@100 con CI 95%; `Pool@200` es contexto, no segundo contraste |
| `G3C-005` | Phase E descriptivo | `G5-SECONDARY-01` | `G6-FIG-02` | `TESIS_RESULTADOS; TESIS_DISCUSION` | `ARTICULO_RESULTS; ARTICULO_DISCUSSION` | Descriptivo; sin CI/p-value/contraste inferencial; no promover a confirmatorio |
| `G3C-006` | Top-50 suplementario | `G5-APPENDIX-01` | `TABLE_ONLY` | `TESIS_RESULTADOS` | `ARTICULO_RESULTS / supplement` | Suplementario; no rol decisional HE2 |
| `G3C-007` | EXP11A sensibilidad | `G5-APPENDIX-02` | `G6-FIG-03` | `TESIS_DISCUSION; TESIS_LIMITACIONES` | `ARTICULO_DISCUSSION` | Tamaño y composición acoplados; no efecto causal aislado ni monotónico del tamaño |
| `G3C-008` | EXP11B sensibilidad | `G5-APPENDIX-03` | `TABLE_ONLY` | `TESIS_DISCUSION; TESIS_LIMITACIONES` | `ARTICULO_DISCUSSION` | Diez pares observados; sin superpoblación de seeds; `10×1056` no son observaciones independientes |
| `G3C-009` | Sensibilidad correctiva 0B-05C | `G5-APPENDIX-04` | `TABLE_ONLY` | `TESIS_DISCUSION; TESIS_LIMITACIONES` | `ARTICULO_DISCUSSION` | Attempt06 únicamente; EV03 cero agregado, EV04 pequeño descenso MRR no nulo, D1a cambio no nulo; no “impacto global cero” |
| `G3C-010` | Limitación / no estimable | `G5-TEXT-01` | `none` | `TESIS_LIMITACIONES` | `ARTICULO_DISCUSSION / LIMITATIONS` | EXP12 cerrado sin retrieval; no inviabilidad global ni evidencia positiva/negativa HE5 |
| `G3C-011` | Limitación / no estimable | `G5-TEXT-02` | `none` | `TESIS_LIMITACIONES` | `ARTICULO_DISCUSSION / LIMITATIONS` | Calidad/prevalencia de descripción no operacionalizada; no convertir heurística en prevalencia |
| `G3C-012` | HE5 descriptivo | `G5-SECONDARY-02` | `TABLE_ONLY` | `TESIS_RESULTADOS; TESIS_LIMITACIONES` | `ARTICULO_RESULTS; ARTICULO_DISCUSSION` | Categorías jerárquicas descriptivas; sin umbral de concentración; no inferir concentración desde conteos |
| `G3C-013` | HE5 descriptivo | `G5-SECONDARY-02` | `TABLE_ONLY` | `TESIS_RESULTADOS; TESIS_LIMITACIONES` | `ARTICULO_RESULTS; ARTICULO_DISCUSSION` | Buckets literales 1/2/3-4/5+ DAM; sin umbral congelado de insuficiencia |
| `G3C-014` | Límite de alcance | `G5-TEXT-03` + contrato G3 | `none` | `TESIS_METODOLOGIA_ALCANCE; TESIS_LIMITACIONES` | `ARTICULO_METHODS_SCOPE` | 1,056 series / 67 DAM / 42 NANDINA, Capítulo 87 offline interno; no external validity |
| `G3C-015` | Guardrail arquitectónico | `G5-TEXT-04` + contrato G3 | `none` | `TESIS_METODOLOGIA_ALCANCE` | `ARTICULO_METHODS_SCOPE` | ranking histórico, evidencia normativa y explicación son funciones separadas; LLM no clasifica desde cero |
| `G3C-016` | Guardrail de overclaim | `NOT_PRESENTED_AS_RESULT_WITH_REASON` | `none` | `TESIS_DISCUSION; TESIS_LIMITACIONES` | `ARTICULO_DISCUSSION` | superioridad de retrieval histórico ≠ accuracy global RAG |
| `G3C-017` | Guardrail de overclaim | `NOT_PRESENTED_AS_RESULT_WITH_REASON` | `none` | `TESIS_DISCUSION; TESIS_LIMITACIONES` | `ARTICULO_DISCUSSION` | evidencia normativa ≠ corrección jurídica vinculante |
| `G3C-018` | Guardrail de overclaim | `NOT_PRESENTED_AS_RESULT_WITH_REASON` | `none` | `TESIS_DISCUSION; TESIS_LIMITACIONES` | `ARTICULO_DISCUSSION` | explicación auditable ≠ corrección clasificatoria o jurídica |

### C.1 Regla de congelamiento de destinos

Los destinos anteriores están respaldados por la matriz G4 y la arquitectura G5 para uso futuro. Su incorporación efectiva en tesis/artículo queda pendiente de G7. La selección final de figuras/captions/cross-references debe esperar el cierre de Grupo 6. Cuando un destino editorial final dependa del estado futuro del master, G7 deberá congelar su ubicación concreta; PREF001 no la decide.

---

# D. Drift del artículo

## D.1 Onboarding editorial completado

Se leyeron en `article/main-manuscript`:

```text
article/START_HERE.md
article/README.md
article/ARTICLE_STATUS.md
article/ARTICLE_WRITING_PLAN.md
article/DECISIONS.md
article/SOURCE_REGISTRY.md
article/CLAIM_EVIDENCE_MATRIX.md
article/STYLE_GUIDE.md
article/BIBLIOGRAPHIC_FRAMEWORK.md
```

Estado editorial identificado:

```text
CANONICAL_MASTER = ARTICLE_MASTER_V007
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
CANONICAL_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
CURRENT_DRAFTING_PHASE = DECISION SUPPORT ARCHITECTURE
CURRENT_AUTHORIZED_BLOCK = ARCHITECTURE_B01 / SECTIONS_3_1_TO_3_4_ONLY
CURRENT_GATE = ARCHITECTURE_B01
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

El artículo consume todavía el snapshot experimental:

```text
EXPERIMENTAL_PLAN_HEAD = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
EXPERIMENTAL_PLAN_BLOB = 9b388fe8cc19fce86ec3c15853e73899cb3e5666
EXPERIMENTAL_MAIN_CHECKPOINT = ca065618d5df0019f76ef5a971e858d91c263e1f
GROUP6 = NOT_STARTED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

El estado experimental observado por PREF001 es posterior: `main@b6404ca...`, Plan `b74b96d...`, G6-F01 cerrado e integrado y G6-F02 ejecutado como candidato pendiente de auditoría en la rama de fichas.

Clasificación requerida:

```text
ARTICLE_DRIFT_CLASSIFICATION = EDITORIAL_SNAPSHOT_STALENESS
SCIENTIFIC_CONTRADICTION = false
BLOCKS_ARCHITECTURE_B01_NOW = false
REQUIRES_FUTURE_G7_RECONCILIATION = true
```

La regla D-034 reproducida en `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` es:

```text
GROUP6_CLOSE_REQUIRED_FOR_FORMAL_G7_ACTIVATION = YES
GROUP6_CLOSE_REQUIRED_FOR_ARCHITECTURE_DRAFTING = NO
GROUP6_CLOSE_REQUIRED_FOR_EXPERIMENTAL_DESIGN_DRAFTING = NO
FORMAL_G7_ACTIVATION_BEFORE_GROUP6_CLOSE = NOT_PERMITTED
G7_F03_ROLE = SYNCHRONIZATION_AND_TRANSVERSAL_CLOSURE
G7_F03_ROLE_IS_ARTICLE_INCEPTION = false
GROUP7_CLOSE_REQUIRED_BEFORE_GROUP8 = YES
SCIENTIFIC_FINAL_FREEZE_REQUIRES_GROUP8 = true
```

Por tanto, la stale snapshot no bloquea Architecture B01 ahora; debe reconciliarse antes de la sincronización formal G7 y del cierre transversal.

## D.2 Gap de trazabilidad editorial adicional

El `DECISIONS.md` leído en `article/main-manuscript@0890a250...` contiene entradas hasta D-011, mientras `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` referencian decisiones posteriores hasta D-034 y reproducen el contenido operativo de D-034.

```text
EDITORIAL_CONTROL_GAP_ID = PREF001-ART-001
TYPE = EDITORIAL_CONTROL_TRACEABILITY_GAP
SCIENTIFIC_CONTRADICTION = false
CURRENT_B01_BLOCKER = false
FUTURE_G7_ACTION = reconcile decision-log traceability before final Group7 synchronization
```

PREF001 no completa ni modifica ese registro.

---

# E. Identidad de freeze de tesis

La búsqueda independiente en los archivos disponibles del proyecto/conversación y Library no produjo una copia de tesis Word identificable de manera confiable como **master vigente**. Se localizaron copias del Anexo metodológico `Anexo_1_NANDINA_LLM_RAG_v13*.docx` y un Word `TFM - rsmc.docx` no relacionado con esta tesis; ninguno se promovió a tesis master.

```text
THESIS_FILE_IDENTIFIED = false
THESIS_FILENAME = NOT_VERIFIED
THESIS_MASTER_STATUS = NOT_VERIFIED
THESIS_SHA256 = NOT_VERIFIED
FORMAL_G7_F01_THESIS_FREEZE_READY = false
THESIS_FREEZE_CLASSIFICATION = BLOCKED_MISSING_IDENTITY
```

Regla: G7-F01 formal no debe inferir filename, estado de master ni hash desde conversaciones previas, nombres parecidos, memoria o PREG no gobernante. El autor/flujo rector deberá proporcionar o identificar inequívocamente la copia Word vigente y permitir la verificación del SHA-256.

La identidad del **master del artículo** (`ARTICLE_MASTER_V007`) no debe confundirse con el master de tesis.

---

# F. Guardrails obligatorios para G7

1. `UNIT_OF_ANALYSIS = SERIE`.
2. `DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda`; no tratar automáticamente 1,056 series como 1,056 observaciones inferenciales independientes.
3. `EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION`.
4. `EVAL_N = 1056`, `EVAL_DAM = 67`, `EVAL_NANDINA = 42`.
5. `HE2 = SUPPORTED` solo dentro del alcance congelado; HE2_A y HE2_B primario no equivalen a accuracy global del sistema.
6. `HE5 = INCONCLUSIVE`; no convertir ausencia de estimabilidad en evidencia positiva o negativa.
7. `EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL`; no efecto causal aislado/monotónico del tamaño.
8. `EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE`; no pseudorreplicación `10×1056`.
9. `0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE`; no usar Attempts superseded y no resumir el estado como impacto global cero.
10. `EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE`; no reabrir, no inventar D-HIGH/D-MID/D-LOW, no afirmar inviabilidad matemática global.
11. `HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false`.
12. `NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false`.
13. `AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false`.
14. Recuperación histórica genera/ordena candidatos; recuperación normativa aporta evidencia posterior; LLM local explica Top-3 ya fijado y no sustituye ranking.
15. `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.
16. HE2_A: CI 99% ligado a la diferencia pareada, no a valores absolutos por brazo.
17. HE2_B: un CI 95% para `Recall@200 − Recall@100`; `Pool@200` no es segundo contraste.
18. Phase E es descriptivo; Top-50 es suplementario; HE5 hierarchy/support es descriptivo; EXP12 es text-only/no estimable.
19. Las 11 limitaciones no bloqueantes de Grupo 2B permanecen vigentes; `HASH_BOUND_LOCAL_ONLY` no significa missing/invalid y `DECLARED_NOT_RECOVERABLE` no significa experimental error.
20. El contraste con literatura se limita al corpus y reglas G4-F03: no SOTA, no novelty absoluta, no superioridad numérica cross-study no comparable.

---

# G. Riesgos heredables a G7-F02 / G7-F03 / G8

| Risk ID | Riesgo | Hereda a | Control requerido |
|---|---|---|---|
| `PREF001-R01` | Grupo 6 todavía abierto; renders/captions no congelables formalmente | G7-F01/F02/F03, G8 | esperar cierre auditado de G6-F02/G6-F03/Grupo6 |
| `PREF001-R02` | Plan Maestro y fichas difieren en el estado puntual de G6-F02 | G7-F01, G8 | reconciliación por gobernanza experimental; no resolver por inferencia |
| `PREF001-R03` | Artículo consume snapshot experimental anterior al cierre de G6-F01 | G7-F03, G8 | nuevo corte experimental editorial y actualización controlada |
| `PREF001-R04` | Identidad de tesis Word master no verificable | G7-F01/F02, G8 | filename + master status + SHA-256 antes de editar/auditar tesis |
| `PREF001-R05` | `DECISIONS.md` no materializa las decisiones posteriores citadas por status/plan | G7-F03, G8 | reconciliar trazabilidad de decisiones sin alterar significado vigente |
| `PREF001-R06` | Reglas institucionales UNMSM no congeladas en este preflight | G7-F01/F02, G8 | identificar fuente institucional vigente y registrar versión/fecha |
| `PREF001-R07` | Riesgo de promover evidencia descriptiva a confirmatoria | G7-F02/F03, G8 | preservar roles G5/G6 y claim matrix G4 |
| `PREF001-R08` | Riesgo de usar CI equivocado o añadir CI no autorizado | G7-F02/F03, G8 | HE2_A 99% paired-difference only; HE2_B 95%; Phase E/EXP11A/EXP11B/HE5 descriptivo sin CI nuevo |
| `PREF001-R09` | Riesgo de usar 0B-05C superseded | G7-F02/F03, G8 | Attempt06 corrected state only |
| `PREF001-R10` | Riesgo de reinterpretar EXP12 como cero, fracaso global o evidencia HE5 | G7-F02/F03, G8 | `NOT_ESTIMABLE`, no performance row/figure |
| `PREF001-R11` | Riesgo de sobregeneralizar Chapter 87 internal benchmark | G7-F02/F03, G8 | frontera 1056/67/42, offline/internal, sin generalización externa |
| `PREF001-R12` | Riesgo bibliográfico de comparar métricas heterogéneas entre estudios | G7-F03, G8 | usar G4-F03 comparability classes y FDP-001..014 |
| `PREF001-R13` | Riesgo de confundir trazabilidad/auditabilidad con correctness legal | G7-F02/F03, G8 | G3C-015..018 y controles del artículo |
| `PREF001-R14` | Riesgo de convertir configurabilidad/reproducibilidad en generalización empírica | G7-F02/F03, G8 | mantener separación diseño ↔ evidencia empírica |

### G.1 Estructura mínima recomendada para auditoría G8

```text
DOCUMENTO / SECCION
→ CLAIM_ID
→ EVIDENCIA PRIMARIA
→ TABLA CANONICA
→ FIGURA/CAPTION SI APLICA
→ CIFRA / CI / N
→ LIMITACION OBLIGATORIA
→ OUTPUT SUPERSEDED PROHIBIDO
→ STATUS
```

Checks prioritarios futuros: 99% vs 95% CI; no arm-level CI; Phase E descriptivo; Top-50 suplementario; HE5 sin thresholds retrospectivos; Attempt06 únicamente; EXP12 sin retrieval; SERIE/DAM consistente; 1,056/67/42 y Capítulo 87 internal/offline; equivalencia texto↔tabla↔figura; no overclaim legal/global.

---

# H. Comparación posterior con PREG7-001 no gobernante

`PREG7-001` se leyó **solo después** de cerrar el análisis independiente precedente. No se utilizó como fuente primaria ni para completar huecos.

## H.1 CONVERGENCES

1. Coincide el estado rector sustantivo: G6-F01 cerrado; G6-F02 candidato ejecutado/no aprobado; G6-F03 prospectivo; Grupo 6 en progreso; G7 no activado.
2. Coincide que G3, G4 y G5 ya aportan material apto para un futuro source freeze.
3. Coinciden las disposiciones `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE`, EXP11A no causal conjunto, EXP11B descriptivo sin superpoblación y EXP12 no estimable.
4. Coincide el mapa general G3C-001..018 → tablas G5 → figuras G6/destinos text-only/table-only.
5. Coincide que G6 solo es parcialmente congelable y que G6-F02/G6-F03/Group6 deben cerrarse antes de G7-F01 formal.
6. Coincide la clasificación del artículo como snapshot experimental desactualizado, no contradicción científica, y que Architecture B01 no queda bloqueado por ello.
7. Coinciden los guardrails de retrieval, evidencia normativa, explicación auditable, SERIE/DAM, Attempt06 y no-estimabilidad EXP12.

## H.2 DIVERGENCES

### H-DIV-001 — identidad de tesis

PREG7-001 afirma haber localizado `Molleapasa_gv(4).docx` y marca `THESIS_FILE_IDENTIFIED = true`, aunque sin SHA ni `APPROVED_MASTER`. El análisis independiente de PREF001, realizado antes de leer PREG7-001, **no encontró esa copia en las superficies de archivos actualmente disponibles** y no pudo verificar que exista ni que sea el master vigente.

Resolución PREF001:

```text
THESIS_FILE_IDENTIFIED = false
THESIS_FILENAME = NOT_VERIFIED
THESIS_MASTER_STATUS = NOT_VERIFIED
THESIS_SHA256 = NOT_VERIFIED
```

No se hereda el filename desde PREG7-001 por ser no gobernante.

### H-DIV-002 — referencia a Prompt106

PREG7-001 menciona un “scope correctivo consolidado pendiente de Prompt106”. Las fuentes rectoras revisadas por PREF001 permiten afirmar únicamente que G6-F02 está pendiente de auditoría/corrección y que G6-F03 no está autorizado. PREF001 no adopta el número o contenido de Prompt106 como hecho gobernante sin una fuente primaria específica dentro del contrato de este preflight.

## H.3 UNSUPPORTED_ITEMS_IN_PREG7_001

1. `Molleapasa_gv(4).docx` como identidad utilizable de tesis vigente: no verificable independientemente en este preflight.
2. Cualquier inferencia de “working draft más reciente” basada solo en flujo conversacional previo: no es suficiente para el freeze G7.
3. La referencia concreta a Prompt106 como gate correctivo gobernante: no fue necesaria ni quedó establecida por las fuentes primarias obligatorias de PREF001.

## H.4 MISSING_ITEMS_IN_PREG7_001

1. La divergencia específica **Plan Maestro vs rama de fichas** sobre el estado de G6-F02 (`ELIGIBLE/NOT_EXECUTED` vs `CANDIDATE_PENDING_EXTERNAL_AUDIT/EXECUTED`).
2. El gap de trazabilidad editorial por el cual `ARTICLE_STATUS.md`/`ARTICLE_WRITING_PLAN.md` referencian D-034 mientras el `DECISIONS.md` observado termina en D-011.
3. La clasificación explícita de reglas institucionales UNMSM como fuente aún no congelada para G7-F01.
4. La distinción explícita entre `ARTICLE_MASTER_V007` —identidad editorial verificable— y la identidad todavía no verificable del Word master de tesis.

PREG7-001 se conserva como comparación histórica no gobernante; no se corrige ni se modifica.

---

# I. Controles PASS/FAIL

| Control | Resultado | Evidencia de ejecución PREF001 |
|---|---|---|
| `PREF001_INDEPENDENT_ANALYSIS_BEFORE_PREG_READ` | `PASS` | Secciones A–G construidas desde Plan, fichas, G3–G6, article y Files antes de abrir PREG7-001 |
| `PREF001_NO_G7_ACTIVATION` | `PASS` | G7-F01 permanece prospectivo/no autorizado |
| `PREF001_NO_PLAN_MODIFICATION` | `PASS` | Plan consultado read-only |
| `PREF001_NO_FICHAS_MODIFICATION` | `PASS` | fichas consultadas read-only |
| `PREF001_NO_MAIN_MODIFICATION` | `PASS` | `main` consultado read-only |
| `PREF001_NO_ARTICLE_MODIFICATION` | `PASS` | rama artículo consultada read-only |
| `PREF001_NO_THESIS_MODIFICATION` | `PASS` | no se editó ni materializó tesis |
| `PREF001_G3_G4_G5_SOURCE_TRACEABILITY` | `PASS` | G3 hypothesis disposition, G4 matrix/synthesis/limitations/literature, G5 registry/canonical tables/appendix registry verificados |
| `PREF001_G6_NOT_PREMATURELY_FROZEN` | `PASS` | G6 clasificado `PARTIALLY_READY`; G6-F02 no aprobado y G6-F03 no ejecutado |
| `PREF001_ARTICLE_ONBOARDING_COMPLETE` | `PASS` | START_HERE, README, STATUS, WRITING_PLAN, DECISIONS, SOURCE_REGISTRY, CLAIM_EVIDENCE_MATRIX, STYLE_GUIDE y BIBLIOGRAPHIC_FRAMEWORK leídos |
| `PREF001_THESIS_IDENTITY_NOT_INVENTED` | `PASS` | identidad de tesis quedó `NOT_VERIFIED` al no existir evidencia suficiente |
| `PREF001_HE2_HE5_GUARDRAILS_PRESERVED` | `PASS` | `HE2=SUPPORTED`; `HE5=INCONCLUSIVE` sin redecisión |
| `PREF001_EXP11A_EXP11B_EXP12_GUARDRAILS_PRESERVED` | `PASS` | joint/noncausal; descriptive/no seed superpopulation; closed/no retrieval/not estimable |
| `PREF001_PREG7_001_TREATED_AS_NON_GOVERNING` | `PASS` | PREG leído solo al final y utilizado únicamente para comparación |

---

# J. Resultado terminal

```text
PREF001_RESULT = READY_AS_PREFLIGHT_WITH_NONBLOCKING_GAPS
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
G6_F02_APPROVAL_AUTHORIZED = false
G6_F03_AUTHORIZED = false
G7_F01_AUTHORIZED = false
G7_F02_AUTHORIZED = false
G7_F03_AUTHORIZED = false
GROUP8_AUTHORIZED = false
```

Los gaps son no bloqueantes **para este preflight** porque fueron identificados sin falsear el estado: Grupo 6 aún abierto, identidad de tesis no verificada, snapshot editorial desactualizado, trazabilidad incompleta del decision log y reglas institucionales UNMSM aún no congeladas. Sí son requisitos que deberán resolverse, según corresponda, antes del cierre formal de G7-F01/G7-F02/G7-F03 o del freeze G8.