# PROMPT 87 — ACTIVAR Y EJECUTAR EXCLUSIVAMENTE G4-F01: MATRIZ RESULTADO → CLAIM → EVIDENCIA

## 0. Naturaleza, autorización y límite

La IA Experimental ha auditado externamente Prompt86 y ha verificado el cierre canónico de Grupo 3.

Esta ejecución constituye autorización expresa **únicamente para G4-F01**.

Estado de entrada esperado:

```text
GROUP3 = CLOSED / APPROVED
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
G4_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F02 = PROSPECTIVE / NOT_AUTHORIZED
```

G4-F01 es una ficha de **traducción controlada de resultados ya aprobados a claims interpretables**. No autoriza nueva inferencia, recalcular métricas, reabrir experimentos, reinterpretar hipótesis, redactar el artículo ni producir una síntesis narrativa libre.

El producto debe quedar como candidato pendiente de auditoría externa:

```text
G4_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G4_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

No cierres G4-F01 ni avances a G4-F02.

---

## 1. Repositorio y refs congelados de entrada

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de modificar nada ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 09278a10063a1e175ee2991b60f7649dd2ee40f4
origin/docs/plan-maestro-temporal-2026-08-31 = 06b24245f4c974b7550863d21ed05f4d63c2792b
origin/docs/fichas-grupos-3-8 = 5084f6916b57ee34049f2315b4a5068df178938a
```

Artículo observado al autorizar Prompt87:

```text
origin/article/main-manuscript = 020c65c9ffc0f6516b69a66628adc813a9c37664
```

El artículo es **solo observacional**. No es fuente científica de G4-F01 y no debe modificarse. Si avanza concurrentemente, registra el drift como advertencia siempre que Prompt87 no lo haya modificado.

La rama `codex/prompts-temporary` puede avanzar por la incorporación de Prompt87 y de su respuesta; eso no constituye drift científico.

Si `main`, Plan Maestro o fichas presentan drift no explicado antes de la activación:

```text
STOP / G4_F01_SCIENTIFIC_OR_GOVERNANCE_REF_DRIFT
```

---

## 2. Fuentes rectoras obligatorias

Lee íntegramente y usa estas fuentes en el orden indicado.

### 2.1 Ficha G4-F01

Desde `origin/docs/fichas-grupos-3-8 = 5084f6916b57ee34049f2315b4a5068df178938a`:

```text
docs/fichas/grupos_3_8/grupo_4/G4_F01_MATRIZ_RESULTADO_CLAIM_EVIDENCIA.md
```

Blob esperado:

```text
40dd0aabef2c96744c8c0d0e966ddec86403feb3
```

Su criterio PASS es vinculante:

```text
cero claims sin evidencia
cero claims más fuertes que el resultado que los soporta
```

### 2.2 Claim registry de cierre de Grupo 3 — FUENTE CONTROLADORA DE CLAIMS

Desde `origin/main = 09278a10063a1e175ee2991b60f7649dd2ee40f4`:

```text
docs/analysis/group3/g3_claim_registry_v0.1.md
```

Blob esperado:

```text
f3f6594277bfeede555f10887bcdb922efd23680
```

Contiene exactamente los claims controlados:

```text
G3C-001 ... G3C-018
```

**No inventes claims adicionales. No elimines ninguno. No fortalezcas el texto controlado.**

### 2.3 Disposición HE2/HE5

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
```

Blob esperado:

```text
d8f20498ebd26e467ba1916e3e0ed93d1dd06c61
```

Los campos históricos `status=CANDIDATE_PENDING_EXTERNAL_AUDIT` reflejan el momento de generación del artefacto; el estado operativo vigente es el de Plan Maestro + registro de fichas.

Debes preservar exactamente:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

### 2.4 Cierre de Grupo 3

```text
outputs/audits/group3_closure_v0.1.json
```

Blob esperado:

```text
17790b1f0d390ebf13672c7f7f63343493aaf7a5
```

Su estado interno de candidato también es histórico. No lo reescribas.

### 2.5 Registro maestro G3-F02

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

### 2.6 Resultados inferenciales G3-F03

```text
outputs/analysis/group3/g3_inferential_results_v0.1.csv
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
outputs/analysis/group3/g3_inferential_results_v0.1_hash_ledger.csv
```

Blobs congelados:

```text
G3F03_CSV_BLOB = cf3d8d85e099a300330da0214836e70af7a02253
G3F03_JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc
G3F03_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
G3F03_LEDGER_BLOB = b128966f1295ac8a853341b7f02ce7f9218157b8
```

### 2.7 Gobernanza vigente

Lee:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

desde `origin/docs/plan-maestro-temporal-2026-08-31`, y:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

desde `origin/docs/fichas-grupos-3-8`.

Debe resultar exactamente:

```text
GROUP3 = CLOSED / APPROVED
G4_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F02 = PROSPECTIVE
```

Si no coincide:

```text
STOP / G4_F01_PRECONDITION_MISMATCH
```

---

## 3. RPRE obligatorio antes de ejecutar

Antes de activar la ficha, realiza una revisión preventiva interna y confirma:

```text
RPRE_G4_F01_SOURCE_CONTRACT = PASS
RPRE_G4_F01_NO_NEW_SCIENCE = PASS
RPRE_G4_F01_CLAIM_STRENGTH_GUARDRAILS = PASS
RPRE_G4_F01_G3C010_EXP12_ROLE = PASS
RPRE_G4_F01_ARTICLE_ISOLATION = PASS
```

Comprueba específicamente que:

1. la matriz será una **capa de trazabilidad**, no una reinterpretación de resultados;
2. ninguna fila causalizará EXP11A, EXP11B, Attempt06, HE2 o HE5;
3. `G3C-010` (EXP12) se tratará como **limitación experimental no estimable** y nunca como evidencia positiva de HE5;
4. los claims arquitectónicos/guardrails sin cifra numérica no recibirán valores inventados;
5. las secciones candidatas de tesis/artículo serán solo metadatos de destino, no redacción editorial.

Si cualquiera falla:

```text
STOP / RPRE_G4_F01_FAILED
```

---

## 4. Activación prospectiva administrativa de G4-F01

Antes de producir la matriz, materializa la autorización en:

```text
branch = docs/fichas-grupos-3-8
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Actualiza únicamente G4-F01 a:

```text
ACTIVE / AUTHORIZED / EXECUTION_PENDING
```

Mantén:

```text
G4-F02 = PROSPECTIVE / NOT_AUTHORIZED
```

Añade un bloque con, como mínimo:

```text
FICHA = G4-F01
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT87_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
ACTIVATION_DATE = 2026-09-19
MAIN_AT_ACTIVATION = 09278a10063a1e175ee2991b60f7649dd2ee40f4
PLAN_AT_ACTIVATION = 06b24245f4c974b7550863d21ed05f4d63c2792b
FICHAS_AT_ACTIVATION = 5084f6916b57ee34049f2315b4a5068df178938a
ARTICLE_HEAD_OBSERVED = 020c65c9ffc0f6516b69a66628adc813a9c37664
PROMPT87_COMMIT = <commit exacto de Prompt87>
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
G4_F02_AUTHORIZED = false
```

Haz un solo commit administrativo de activación y push normal.

No modifiques Plan Maestro todavía.

Si la activación no puede publicarse antes de crear la matriz:

```text
STOP / G4_F01_ACTIVATION_NOT_MATERIALIZED
```

---

## 5. Rama científica y alcance exacto

Crea desde `origin/main` exacto:

```text
branch = codex/group4-f01-result-claim-evidence-v01
parent = 09278a10063a1e175ee2991b60f7649dd2ee40f4
```

La rama científica debe terminar **exactamente un commit adelante y cero detrás** de ese parent.

Únicos paths científicos permitidos:

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
```

No generes scripts, figuras, prosa de artículo, análisis inferencial nuevo ni archivos auxiliares adicionales.

No modifiques `main`, Plan Maestro ni `article/main-manuscript`.

---

## 6. Unidad de la matriz: 18 claims controlados, sin expansión semántica

La matriz CSV debe contener **exactamente 18 filas primarias**, una por cada claim controlado `G3C-001` a `G3C-018`, en ese orden.

Esto no significa ocultar la granularidad científica. Para claims respaldados por múltiples resultados, el JSON debe incluir un arreglo estructurado `evidence_atoms` con cada resultado/registro materializado pertinente.

Reglas:

```text
CONTROLLED_CLAIM_COUNT = 18
CSV_PRIMARY_ROW_COUNT = 18
NEW_CLAIM_COUNT = 0
DROPPED_CLAIM_COUNT = 0
```

El campo `claim_text_controlled` debe copiarse literalmente desde `g3_claim_registry_v0.1.md`. No parafrasearlo.

---

## 7. Esquema mínimo obligatorio del CSV

El CSV debe contener, como mínimo, estas columnas en este orden lógico (puedes añadir columnas solo si son estrictamente de trazabilidad y no cambian el significado):

```text
matrix_row_id
claim_id
claim_text_controlled
claim_type
hypothesis_link
evidence_class
source_artifact
source_result_or_registry_ids
numeric_evidence_status
numeric_evidence_summary
uncertainty_status
uncertainty_summary
allowed_strength
causal_status
scope
mandatory_limitation
forbidden_overclaim
thesis_candidate_section
article_candidate_section
evidence_trace_status
```

### 7.1 IDs de matriz

Usa:

```text
G4F01-0001 ... G4F01-0018
```

con correspondencia 1:1 y ordenada a:

```text
G3C-001 ... G3C-018
```

### 7.2 `numeric_evidence_status`

Valores permitidos:

```text
MATERIALIZED_NUMERIC
MATERIALIZED_CATEGORICAL
NOT_APPLICABLE_GUARDRAIL
NOT_ESTIMABLE
```

No inventes cifras para guardrails arquitectónicos o prohibiciones.

### 7.3 `uncertainty_status`

Valores permitidos:

```text
MATERIALIZED_G3F03_CI
DESCRIPTIVE_NO_CI_AUTHORIZED
NOT_APPLICABLE
NOT_ESTIMABLE
```

No calcules nuevos intervalos.

### 7.4 secciones candidatas

Son únicamente metadatos de destino. Usa solo valores controlados de esta lista:

```text
TESIS_RESULTADOS
TESIS_DISCUSION
TESIS_LIMITACIONES
TESIS_METODOLOGIA_ALCANCE
ARTICULO_RESULTS
ARTICULO_DISCUSSION
ARTICULO_METHODS_SCOPE
NOT_APPLICABLE
```

Cuando una afirmación pueda ser útil en dos destinos, usa `;` como separador. No redactes ningún párrafo de tesis o artículo.

---

## 8. Esquema obligatorio del JSON

El JSON debe ser la versión estructurada autoritativa y contener al menos:

```text
artifact_id
status
ficha
input_refs
source_blobs
hypothesis_dispositions
matrix_rows
validation
flags
```

`matrix_rows` debe contener exactamente 18 objetos y cada objeto debe incluir todos los campos semánticos del CSV más:

```text
evidence_atoms
```

Cada `evidence_atom` debe incluir únicamente datos ya materializados, según corresponda:

```text
source_id
source_path
metric_or_record
point_estimate_or_value
value_unit
ci_level
ci_lower
ci_upper
evidence_role
```

Si un campo no aplica, usa `null`; no inventes valores.

---

## 9. Reglas de trazabilidad por claim

### 9.1 G3C-001, G3C-002, G3C-003 — HE2_A primario

Cada uno debe incorporar como `evidence_atoms` los cinco resultados G3-F03 correspondientes:

```text
Top-1
Top-3
Top-5
Top-10
MRR@100
```

Incluye point estimate, `ci_level=0.99`, `ci_lower`, `ci_upper` tal como existen en G3-F03.

No uses Top-50 para fortalecer estos claims.

### 9.2 G3C-004 — HE2_B jerárquico

Usa exclusivamente:

```text
G3F03-0016
```

más los IDs G3-F02 ya controlados por el claim. Registra el contraste `Recall@200 - Recall@100` y su CI95% ya materializado.

No dupliques `Pool@200` como un segundo contraste inferencial.

### 9.3 G3C-005 — Phase E descriptivo

Usa exclusivamente las cuatro variantes `A_historical_defined` y sus filas exact-NANDINA `Pool@50`, `Pool@100`, `Pool@200` ya señaladas en el claim registry.

Debe quedar:

```text
evidence_class = DESCRIPTIVE
uncertainty_status = DESCRIPTIVE_NO_CI_AUTHORIZED
allowed_strength = DIRECTIONALLY_CONSISTENT_DESCRIPTIVE
```

No calcules intervalos, tests ni diferencias nuevas.

### 9.4 G3C-006 — Top-50 suplementario

Usa G3F03-0017:G3F03-0019 y conserva:

```text
allowed_strength = SUPPLEMENTARY_ONLY
hypothesis_decision_role = NONE
```

No uses Top-50 para redecidir HE2.

### 9.5 G3C-007 — EXP11A

Debe explicitar:

```text
causal_status = NONCAUSAL
mandatory_limitation = size and composition are coupled
```

No afirmar efecto causal aislado del tamaño del banco.

### 9.6 G3C-008 — EXP11B

Debe preservar:

```text
DESCRIPTIVE_ONLY
no frozen seed superpopulation
10 x 1056 are not independent observations
```

No fabricar inferencia sobre semillas ni tratar las observaciones repetidas como independientes.

### 9.7 G3C-009 — Attempt06

Debe preservar literalmente el estado científico:

```text
EV03 aggregate change zero
EV04 small non-zero MRR decrease
D1a non-zero changes
```

Solo Attempt06 corregido es vigente. No resumir como “sin impacto numérico”.

### 9.8 G3C-010 — EXP12

Este punto es crítico.

Aunque el claim registry heredado contiene `hypothesis_link=HE5`, G4-F01 debe dejar explícito en campos separados:

```text
evidence_class = EXPERIMENTAL_LIMITATION
numeric_evidence_status = NOT_ESTIMABLE
HE5_POSITIVE_EVIDENCE_ROLE = NONE
HE5_NEGATIVE_EVIDENCE_ROLE = NONE
```

EXP12 no es evidencia a favor ni en contra de HE5. Es una limitación experimental por no haberse producido condiciones D-HIGH/D-MID/D-LOW ni retrieval.

No reabrir EXP12 ni alterar el claim controlado.

### 9.9 G3C-011 a G3C-014 — HE5

Preserva exactamente:

```text
G3C-011 = NOT_ESTIMABLE
G3C-012 = DESCRIPTIVE_ONLY
G3C-013 = DESCRIPTIVE_ONLY / NO FROZEN INSUFFICIENCY THRESHOLD
G3C-014 = DOCUMENTED_LIMITATION
HE5 = INCONCLUSIVE
```

No crear umbrales de concentración, insuficiencia o prevalencia.

### 9.10 G3C-015 a G3C-018 — arquitectura y guardrails

Son afirmaciones de control y prohibición, no resultados cuantitativos.

Usa:

```text
numeric_evidence_status = NOT_APPLICABLE_GUARDRAIL
uncertainty_status = NOT_APPLICABLE
```

No inventes cifras.

Preserva:

- ranking histórico, evidencia normativa y explicación controlada son funciones distintas;
- superioridad del retrieval histórico ≠ exactitud global del RAG;
- evidencia normativa recuperada ≠ corrección jurídica vinculante;
- explicación auditable ≠ clasificación ni corrección jurídica;
- el LLM local explica candidatos preseleccionados y no reemplaza el ranking histórico.

---

## 10. Cifras e incertidumbre: extracción, no recálculo

Está permitido **copiar** cifras ya materializadas desde G3-F02/G3-F03.

Está prohibido:

- recalcular point estimates;
- recalcular CI;
- calcular p-values;
- calcular nuevos effect sizes;
- calcular nuevas diferencias, ratios o porcentajes;
- derivar nuevos rankings;
- reinterpretar ausencia de evaluación como resultado negativo.

Si una cifra no está materializada en una fuente aprobada, usa:

```text
numeric_evidence_status = NOT_ESTIMABLE
```

o `NOT_APPLICABLE_GUARDRAIL`, según corresponda.

---

## 11. Fuerza del claim y causalidad

Los campos `allowed_strength`, `causal_status`, `mandatory_limitation` y `forbidden_overclaim` deben provenir del claim registry y/o de las fuentes G3 congeladas.

No uses vocabulario como:

```text
caused
causal effect
proves
validates legally
generalizes
full-system accuracy
```

salvo dentro de una prohibición explícita del tipo “do not claim ...”.

HE2 respaldada por bootstrap pareado de clusters sigue siendo un contraste no causal dentro del benchmark fijo interno.

---

## 12. Validaciones obligatorias del candidato

El JSON debe incluir un bloque `validation` con al menos:

```text
CONTROLLED_CLAIM_COUNT = 18
CSV_PRIMARY_ROW_COUNT = 18
JSON_MATRIX_ROW_COUNT = 18
NEW_CLAIM_COUNT = 0
DROPPED_CLAIM_COUNT = 0
DUPLICATE_CLAIM_ID_COUNT = 0
MISSING_SOURCE_ID_COUNT = 0
MISSING_SOURCE_PATH_COUNT = 0
MISSING_ALLOWED_STRENGTH_COUNT = 0
MISSING_MANDATORY_LIMITATION_COUNT = 0
MISSING_FORBIDDEN_OVERCLAIM_COUNT = 0
OVERSTRENGTH_CLAIM_COUNT = 0
G3C010_HE5_POSITIVE_EVIDENCE_COUNT = 0
G3C010_HE5_NEGATIVE_EVIDENCE_COUNT = 0
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
G4_F02_STARTED = false
```

### PASS operativo

Solo considera candidato válido si:

```text
CONTROLLED_CLAIM_COUNT = 18
CSV_PRIMARY_ROW_COUNT = 18
JSON_MATRIX_ROW_COUNT = 18
NEW_CLAIM_COUNT = 0
DROPPED_CLAIM_COUNT = 0
DUPLICATE_CLAIM_ID_COUNT = 0
MISSING_SOURCE_ID_COUNT = 0
MISSING_SOURCE_PATH_COUNT = 0
OVERSTRENGTH_CLAIM_COUNT = 0
G3C010_HE5_POSITIVE_EVIDENCE_COUNT = 0
G3C010_HE5_NEGATIVE_EVIDENCE_COUNT = 0
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
G4_F02_STARTED = false
```

Si no se cumple, no declares PASS ni cierres la ficha.

---

## 13. Commit científico candidato

En `codex/group4-f01-result-claim-evidence-v01` crea un único commit con exactamente los dos outputs autorizados.

Mensaje sugerido:

```text
analysis: add G4-F01 result-claim-evidence matrix
```

Haz push normal.

Verifica después:

```text
G4_F01_COMMITS_AHEAD = 1
G4_F01_COMMITS_BEHIND = 0
G4_F01_CHANGED_PATH_COUNT = 2
```

Los únicos paths deben ser:

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
```

No integres a `main`.

---

## 14. Registro postejecución en fichas

Después de publicar el candidato, actualiza nuevamente **solo**:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

en `docs/fichas-grupos-3-8`.

Cambia G4-F01 a:

```text
CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

Mantén G4-F02:

```text
PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque que registre:

```text
G4_F01_BRANCH
G4_F01_CANDIDATE_COMMIT
G4_F01_CANDIDATE_PARENT
G4_F01_CHANGED_PATH_COUNT = 2
CONTROLLED_CLAIM_COUNT = 18
CSV_PRIMARY_ROW_COUNT = 18
JSON_MATRIX_ROW_COUNT = 18
OVERSTRENGTH_CLAIM_COUNT = 0
G3C010_HE5_POSITIVE_EVIDENCE_COUNT = 0
G3C010_HE5_NEGATIVE_EVIDENCE_COUNT = 0
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
PENDING_EXTERNAL_AUDIT = true
G4_F02_AUTHORIZED = false
```

Haz un segundo commit administrativo postejecución y push normal.

No modifiques Plan Maestro.

---

## 15. Prohibiciones expresas

No:

- modificar `main`;
- modificar Plan Maestro;
- modificar `article/main-manuscript`;
- redactar Resultados, Discusión o cualquier sección del artículo;
- modificar los 18 claims controlados;
- crear claims adicionales;
- recalcular cifras o incertidumbre;
- hacer inferencia nueva;
- decidir nuevamente HE2 o HE5;
- convertir HE5 de `INCONCLUSIVE` a otro estado;
- convertir EXP12 en evidencia positiva/negativa de HE5;
- causalizar EXP11A/EXP11B/Attempt06;
- reabrir EXP12;
- autorizar o ejecutar G4-F02;
- cerrar Grupo 4.

---

## 16. Persistencia obligatoria de la respuesta

Publica en:

```text
branch = codex/prompts-temporary
path = codex_prompts_tmp/87_RESPUESTA_ACTIVAR_Y_EJECUTAR_G4_F01_MATRIZ_RESULTADO_CLAIM_EVIDENCIA.md
```

La respuesta debe contener **solo el reporte terminal**, sin narrativa adicional.

Formato mínimo:

```text
PROMPT87 = COMPLETED | STOPPED

PREFLIGHT_MAIN = <sha>
PREFLIGHT_PLAN = <sha>
PREFLIGHT_FICHAS = <sha>
ARTICLE_HEAD_OBSERVED = <sha>
ARTICLE_HEAD_FINAL_OBSERVED = <sha>
ARTICLE_MODIFIED_BY_PROMPT87 = true|false

RPRE_G4_F01_SOURCE_CONTRACT = PASS|FAIL
RPRE_G4_F01_NO_NEW_SCIENCE = PASS|FAIL
RPRE_G4_F01_CLAIM_STRENGTH_GUARDRAILS = PASS|FAIL
RPRE_G4_F01_G3C010_EXP12_ROLE = PASS|FAIL
RPRE_G4_F01_ARTICLE_ISOLATION = PASS|FAIL

G4_F01_ACTIVATION_COMMIT = <sha>
G4_F01_BRANCH = codex/group4-f01-result-claim-evidence-v01
G4_F01_CANDIDATE_COMMIT = <sha>
G4_F01_CANDIDATE_PARENT = 09278a10063a1e175ee2991b60f7649dd2ee40f4
G4_F01_COMMITS_AHEAD = <n>
G4_F01_COMMITS_BEHIND = <n>
G4_F01_CHANGED_PATH_COUNT = <n>
G4_F01_CHANGED_PATHS = <paths>

G4_F01_CSV_BLOB = <blob>
G4_F01_JSON_BLOB = <blob>

CONTROLLED_CLAIM_COUNT = <n>
CSV_PRIMARY_ROW_COUNT = <n>
JSON_MATRIX_ROW_COUNT = <n>
NEW_CLAIM_COUNT = <n>
DROPPED_CLAIM_COUNT = <n>
DUPLICATE_CLAIM_ID_COUNT = <n>
MISSING_SOURCE_ID_COUNT = <n>
MISSING_SOURCE_PATH_COUNT = <n>
MISSING_ALLOWED_STRENGTH_COUNT = <n>
MISSING_MANDATORY_LIMITATION_COUNT = <n>
MISSING_FORBIDDEN_OVERCLAIM_COUNT = <n>
OVERSTRENGTH_CLAIM_COUNT = <n>
G3C010_HE5_POSITIVE_EVIDENCE_COUNT = <n>
G3C010_HE5_NEGATIVE_EVIDENCE_COUNT = <n>

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
G4_F02_STARTED = false

G4_F01_POSTEXEC_FICHAS_COMMIT = <sha>
PROMPT87_RESPONSE_COMMIT = THIS_COMMIT

G4_F01_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G4_F02_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED

BLOCKERS = NONE | <detalle>
WARNINGS = NONE | <detalle>
```

Si se activa cualquier STOP, persiste la respuesta indicando el STOP exacto y no continúes.

---

## 17. Estado terminal obligatorio

Si todo finaliza correctamente:

```text
G4_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G4_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP4 = IN_PROGRESS / NOT_CLOSED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Solo la auditoría externa posterior de la IA Experimental podrá autorizar integración/cierre de G4-F01 y habilitar G4-F02.
