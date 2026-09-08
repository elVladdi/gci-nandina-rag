# CODEX — RECONCILIAR PLAN MAESTRO TRAS INTEGRACIÓN EV03 RECOVERY v0.2

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE GOBERNANZA DOCUMENTAL**.

Debes actualizar el **Plan Maestro canónico** para reconciliar el estado real de 0B-05C después de:

1. autorización histórica v0.1;
2. Intento 01 fail-closed;
3. diagnóstico read-only del WinError 5;
4. Intento 02 fail-closed por reproducción EV03 no exacta;
5. diagnóstico de causa EV03;
6. recuperación de la semántica histórica EV03 v0.2;
7. microclose F001–F004;
8. integración aprobada de esa recuperación a `main`.

**NO construyas todavía el gate numérico v0.2. NO autorices ejecución numérica. NO ejecutes EV03 corrected, EV04 corrected, D1a ni unified. NO modifiques `main` ni `article/main-manuscript`.**

El objetivo es que el Plan Maestro deje de mostrar como estado operativo actual la autorización v0.1 anterior al descubrimiento del defecto EV03, preservándola únicamente como antecedente histórico.

---

## 1. RAMAS Y ESTADOS QUE DEBES VERIFICAR PRIMERO

Repositorio: `elVladdi/gci-nandina-rag`.

Rama científica actual:

`main = origin/main = 43291c312c2934aae03f3c087dd0a1ae594341b7`

Tree integrado esperado:

`9f21cb79c37cbcdf93006503bb4f888f1acfc975`

Cadena recovery integrada:

`06cc75ec173eb6c4b134a45eeb88fe25999f396e`
→ `cef8d7ad58d877e933f8c86b9f721cb214d9058d`
→ `43291c312c2934aae03f3c087dd0a1ae594341b7`

Rama canónica del Plan:

`docs/plan-maestro-temporal-2026-08-31`

HEAD esperado antes de editar:

`f8b37c7f2b5d612ccf2cf9c4779cab7008362fc6`

Archivo único autorizado para modificar:

`docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`

Rama editorial que debe permanecer intacta:

`article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`

Si cualquiera de estas identidades no coincide, **STOP** y reporta. No improvises.

---

## 2. FUENTES DE VERDAD

Antes de editar, lee directamente en GitHub/Git los artefactos gobernantes relevantes en `main`, incluyendo como mínimo:

### v0.1 histórica
- `outputs/audits/0b05c_corrective_numerical_gate_v0.1/0b05c_corrective_numerical_execution_gate_v0.1.json`
- `outputs/audits/0b05c_corrective_numerical_gate_v0.1/0b05c_authorization_record_v0.1.json`
- `src/experiments/run_0b05c_corrective_numerical_v01.py`

### recovery v0.2 integrada
- `docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_historical_builder_provenance_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_logical_index_identity_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_decision885_control_reproduction_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_corrective_execution_spec_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_corrective_numerical_gate_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_manifest_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json`

Usa también los commits integrados `cef8d7ad...` y `43291c31...` para verificar alcance.

Los detalles exclusivamente locales de Intentos 01/02 deben clasificarse de manera honesta como **evidencia operacional reportada por Codex / consistente con GitHub pero no independientemente reconstruible desde artefactos remotos**, salvo que exista artefacto versionado que los pruebe.

---

## 3. HECHOS QUE EL PLAN DEBE RECONCILIAR

### 3.1 Autorización v0.1 — conservar como antecedente histórico

Preserva que el bundle v0.1 fue aprobado/integrado y que existió autorización prospectiva para:

- EV03;
- EV04;
- D1a;
- unified 0B-05C.

Preserva como antecedente:

- authorization baseline commit: `0e074db638f6b7163d98d34f08f76e1efde07b7f`;
- authorization integration commit: `06cc75ec173eb6c4b134a45eeb88fe25999f396e`.

**Pero no presentes esa autorización v0.1 como autorización operativa vigente para un nuevo intento.**

La autorización v0.1 produjo dos intentos fail-closed y quedó metodológicamente superada para futuras ejecuciones por la detección del defecto de reproducción EV03 y la posterior transición a recovery/gate v0.2.

### 3.2 Intento 01

Registrar de forma concisa y explícita:

`0B05C_NUMERICAL_EXECUTION_ATTEMPT_01 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`

Hechos:

- authorized preflight = PASS;
- fallo antes de iniciar EV03/EV04/D1a;
- `FAILED_AT_01_UNIFIED_PREFLIGHT`;
- causa operacional aceptada para trabajo: `SANDBOX_WRITE_BOUNDARY_ON_ONEDRIVE_CHECKOUT`;
- WinError 5 al intentar crear el root de runtime bajo el checkout OneDrive;
- sin métricas correctivas;
- sin decisión downstream;
- sin cierre 0B-05C.

Aclara que la atribución detallada de causa operacional se sustentó en diagnóstico local read-only y no es completamente verificable solo desde GitHub remoto.

### 3.3 Intento 02

Registrar:

`0B05C_NUMERICAL_EXECUTION_ATTEMPT_02 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`

Hechos:

- authorized preflight = PASS;
- una sola invocación del runner reportada;
- step 01 unified preflight alcanzado;
- fallo en `02_EV03_control_reproduction`;
- `ContractViolation: Mandatory control reproduction is not exact`;
- EV04, D1a y corrected arms no iniciados;
- corrective metrics no calculadas;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`.

El mismatch observado que debe registrarse al menos sintéticamente:

- frozen EV03 ranking rows = 50,327;
- reproducción defectuosa con builder actual = 79,912;
- first witness mismatch = `DA-EVAL-V02-00001`;
- frozen top1 = `39173210 / 21.311974833146948`;
- observed top1 = `29314600 / 21.825923130489294`.

No conviertas los outputs locales ignorados del intento en artefactos versionados ni hashes gobernantes.

### 3.4 Diagnóstico EV03

Registrar como conclusión metodológica:

`EV03_REPRODUCTION_ROOT_CAUSE = CURRENT_BUILDER_SEMANTICS_MISMATCH`

La diferencia recuperada:

- builder global/current: conserva tokens alfanuméricos de longitud 1;
- semántica histórica EV03 recuperada: `DROP_SINGLE_CHARACTER_TOKENS`.

Límite epistemológico obligatorio:

`AUTHENTIC_HISTORICAL_SOURCE_PY = NOT_VERSIONED_AT_INDEX_CREATION`

No afirmar que se recuperó el código fuente histórico auténtico; se recuperó y validó su **semántica funcional relevante para EV03**.

### 3.5 Recovery EV03 v0.2

Registrar:

`EV03_HISTORICAL_RECOVERY_V02 = APPROVED / VERSIONED / INTEGRATED`

Commits:

- candidate: `cef8d7ad58d877e933f8c86b9f721cb214d9058d`;
- microclose: `43291c312c2934aae03f3c087dd0a1ae594341b7`;
- `main` actual: `43291c312c2934aae03f3c087dd0a1ae594341b7`.

Resultado científico/técnico:

- `LOGICAL_INDEX_IDENTITY = EXACT`;
- `EV03_DECISION885_CONTROL_REPRODUCTION = PASS_EXACT`;
- ranking rows = 50,327;
- ranking SHA-256 = `d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015`;
- case summary rows = 1,056;
- case summary SHA-256 = `f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0`;
- metric table exact;
- full metrics exact;
- F001–F004 del recovery = cerrados para integración/preexecution;
- reglas LF y bindings canónicos incorporados.

Conclusión permitida:

`HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED`

### 3.6 Estado operativo actual de 0B-05C

Este es el punto crucial de la reconciliación.

El bundle integrado v0.2 es **solo**:

`gate_scope = EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY`

`authorization_readiness = NOT_AUTHORIZATION_READY`

Por tanto, el estado operativo actual debe quedar:

- `EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`;
- `EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`;
- `D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`;
- `UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`;
- `corrective_retrieval_executed = false` para v0.2;
- `corrective_metrics_computed = false`;
- `runtime_authorization_record_v02_present = false`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

Debe quedar explícito que:

**el siguiente paso de 0B-05C es construir prospectivamente un gate/runner numérico v0.2 separado; la recuperación integrada NO constituye autorización numérica.**

No declares que 0B-05C está cerrado.

---

## 4. OTROS ESTADOS QUE NO DEBEN CAMBIAR

Preserva sin reinterpretar:

- Grupo 1 = CLOSED / APPROVED;
- Grupo 2 = EN CURSO;
- EXP11B Bank Materialization = CLOSED / APPROVED / INTEGRATED;
- `EXP11B_PORTABILITY_DEBT = OPEN`;
- la deuda sigue bloqueando EXP11B retrieval authorization, no D1a/0B-05C;
- EXP11B retrieval = NOT_AUTHORIZED / NOT_EXECUTED;
- H150/H200 retrieval results = no observados;
- EXP12 = NOT_AUTHORIZED / NOT_EXECUTED;
- Grupo 3 y posteriores = pendientes.

No autorices EXP11B ni EXP12.

---

## 5. CAMBIOS MÍNIMOS AL PLAN

Actualiza únicamente lo necesario para que el Plan sea canónicamente coherente:

1. `Fecha de actualización` → `2026-09-08`.
2. En la tabla de estado del Grupo 2, sustituye el snapshot obsoleto por un resumen actual que:
   - apunte `main` a `43291c31...`;
   - conserve la autorización v0.1 como histórica;
   - registre Attempt01/Attempt02 fail-closed;
   - registre recovery EV03 v0.2 integrado;
   - establezca v0.2 como `NOT_AUTHORIZATION_READY` y todas las ejecuciones v0.2 como `NOT_AUTHORIZED / NOT_EXECUTED`;
   - mantenga 0B05C impact/downstream/closure sin determinar/no autorizado;
   - preserve EXP11B debt y EXP12.
3. En la cronología/historial de gobernanza de Grupo 2, añade una entrada consolidada y suficientemente detallada que capture la secuencia completa desde autorización v0.1 hasta integración recovery v0.2.
4. En `Orden maestro actual`, si existe un paso 0B-05C, actualízalo para reflejar que el próximo subpaso es **construcción y auditoría del gate numérico v0.2**, no ejecución directa bajo v0.1.
5. No reescribas secciones históricas no relacionadas.
6. No cambies resultados científicos previos.

Evita duplicar grandes bloques si una actualización localizada y una entrada cronológica consolidada bastan.

---

## 6. VALIDACIÓN OBLIGATORIA ANTES DE COMMIT

Verifica:

- diff limitado al único archivo del Plan;
- no existe cambio en `main`;
- no existe cambio en `article/main-manuscript`;
- ningún estado v0.2 aparece como AUTHORIZED;
- ninguna corrected metric aparece como calculada;
- `0B05C_CLOSURE` sigue `NOT_AUTHORIZED`;
- `EXP11B_PORTABILITY_DEBT=OPEN`;
- EXP11B retrieval sigue NOT_AUTHORIZED/NOT_EXECUTED;
- EXP12 sigue NOT_AUTHORIZED/NOT_EXECUTED;
- Grupo 3 no se abre;
- SHA/commits se distinguen correctamente de hashes SHA-256 de archivos.

Haz una revisión textual final buscando contradicciones entre el snapshot del Grupo 2, la cronología y el orden maestro.

---

## 7. COMMIT / PUSH

Si todo pasa:

- realiza un único commit en `docs/plan-maestro-temporal-2026-08-31`;
- mensaje sugerido: `docs: reconcile 0b05c attempts and EV03 recovery v0.2`;
- push solo de esa rama;
- no merge a `main`;
- no modifiques la rama temporal de prompts salvo para leer estas instrucciones.

No uses amend/rebase/force-push.

---

## 8. REPORTE FINAL OBLIGATORIO

Responde únicamente con estas secciones:

### A. Preflight
- heads exactos de main, Plan y article;
- tree de main;
- working tree limpio;
- ausencia de operación Git en progreso.

### B. Cambios del Plan
- lista exacta de secciones modificadas;
- resumen de cada cambio.

### C. Reconciliación 0B-05C
- autorización v0.1 histórica;
- Attempt01;
- Attempt02;
- root cause EV03;
- recovery v0.2;
- estado operativo v0.2 actual.

### D. Estados preservados
- Grupo 1/2;
- EXP11B debt/retrieval;
- EXP12;
- Grupos 3–8.

### E. Validación de contradicciones
- búsquedas/chequeos realizados;
- contradicciones encontradas y corregidas;
- contradicciones residuales, si las hubiera.

### F. Diff/commit
- files changed;
- commit SHA;
- parent;
- tree;
- mensaje;
- push;
- nuevo HEAD remoto del Plan;
- Git blob SHA-1 del Plan;
- SHA-256 canónico del contenido del Plan, distinguiéndolo del Git blob SHA-1.

### G. Estado final
Debe terminar manteniendo explícitamente:

`GROUP_2 = EN_CURSO`

`EV03_HISTORICAL_RECOVERY_V02 = APPROVED / VERSIONED / INTEGRATED`

`0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

`EXP11B_PORTABILITY_DEBT = OPEN`

`EXP11B_RETRIEVAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EXP12 = NOT_AUTHORIZED / NOT_EXECUTED`
