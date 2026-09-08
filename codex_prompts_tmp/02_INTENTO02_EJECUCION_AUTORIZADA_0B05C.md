# CODEX — 0B-05C INTENTO 02: EJECUCIÓN NUMÉRICA AUTORIZADA CON ESCRITURA FUERA DE SANDBOX

## 0. ROL Y ALCANCE

Actúa exclusivamente como **EJECUTOR** de la sensibilidad numérica correctiva 0B-05C ya congelada y autorizada.

Este prompt constituye una **autorización prospectiva independiente para el INTENTO 02** después del fallo cerrado del Intento 01.

El Intento 01 terminó antes del primer side effect científico por `WinError 5`. El diagnóstico read-only posterior determinó que la causa de mayor confianza fue la frontera de escritura de `CodexSandboxOffline` sobre un repositorio ubicado en OneDrive. El runtime root continúa ausente y no existen outputs científicos del Intento 01.

No reabras el diseño científico. No modifiques contratos, código, configs, specs, gates, tests, corpus, queries, pesos, parámetros BM25, métricas, ranking semantics, output paths ni orden de ejecución.

No modifiques `main`, el Plan Maestro, `article/main-manuscript`, EXP11B, EXP12, ACL de Windows, Defender/CFA ni configuración de OneDrive.

No muevas el repositorio y no crees un checkout alternativo en este intento.

---

## 1. IDENTIDADES OBLIGATORIAS

Repositorio local esperado:

`C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA`

Rama local de ejecución existente:

`codex/0b05c-corrective-numerical-execution-v01`

Debe apuntar exactamente a:

`06cc75ec173eb6c4b134a45eeb88fe25999f396e`

También deben cumplirse:

- `HEAD = 06cc75ec173eb6c4b134a45eeb88fe25999f396e`
- `local main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e`
- `origin/main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e`
- tree esperado: `c84da63249619e94ae69fb2a6f080dd3f84cbcf4`
- tracked working tree limpio
- ningún merge/rebase/cherry-pick/revert en curso
- los untracked preexistentes bajo `Referencias/` y `data/Series - Descripciones.xlsx` deben preservarse sin modificación

La reutilización de esta rama local está **expresamente autorizada para el Intento 02** porque el Intento 01 no produjo ningún commit, ningún archivo contractual y ningún runtime root. Esto no es resume ni overwrite.

Si cualquiera de las identidades anteriores falla: **STOP**.

---

## 2. AUSENCIA DE SIDE EFFECTS PREVIOS

Antes de ejecutar, verifica read-only que continúa ausente:

`outputs/evaluation/0b05c_corrective_numerical_v0.1`

Y verifica la ausencia de **todos los prospective/discovery roots** definidos por los contratos EV03, EV04, D1a y unified 0B-05C.

No borres, renombres ni limpies nada para conseguir el PASS.

Si aparece cualquiera de esos roots: **STOP** y reporta el path exacto.

---

## 3. PREFLIGHT AUTORIZADO READ-ONLY

Ejecuta una sola vez el preflight autorizado read-only:

```powershell
python -B -c "import json; from src.experiments.run_0b05c_corrective_numerical_v01 import preflight_authorized; print(json.dumps(preflight_authorized(), ensure_ascii=False, sort_keys=True))"
```

Debe devolver exactamente un estado compatible con:

- `status = PASS`
- `mode = AUTHORIZED_PREFLIGHT_ONLY`
- `numerical_execution_occurred = false`
- cuatro autorizaciones simultáneamente `AUTHORIZED`

Confirma después, read-only, que el preflight no creó ningún prospective root.

Si no pasa: **STOP**. No invoques el runner numérico.

---

## 4. AUTORIZACIÓN OPERACIONAL ESPECÍFICA DEL INTENTO 02

El diagnóstico del Intento 01 determinó que la ejecución ordinaria sandboxed no puede crear el primer directorio contractual dentro de este repositorio OneDrive.

Por tanto, para el **único comando numérico del Intento 02** queda autorizada la ejecución mediante el mecanismo disponible de Codex para correr **fuera de la frontera de escritura de la sandbox / con permiso de escritura elevado sobre el checkout actual**.

Esta autorización operacional:

- NO autoriza cambiar ACL;
- NO autoriza ejecutar `icacls` modificador;
- NO autoriza cambiar Defender/CFA;
- NO autoriza cambiar atributos de OneDrive;
- NO autoriza mover el repositorio;
- NO autoriza ejecutar comandos científicos distintos;
- NO autoriza probar escritura creando archivos o carpetas de prueba;
- NO autoriza un segundo intento si este vuelve a fallar.

Si Codex no puede obtener el permiso operacional requerido para ejecutar el comando exacto fuera de la restricción sandbox, **STOP antes de invocar el runner** y repórtalo como bloqueo operativo.

---

## 5. ÚNICA INVOCACIÓN NUMÉRICA AUTORIZADA

Si y solo si las secciones 1–4 PASS, ejecuta **UNA SOLA VEZ** exactamente:

```powershell
python -m src.experiments.run_0b05c_corrective_numerical_v01 --execute-authorized
```

Ejecuta esa única invocación con el permiso operacional fuera de sandbox autorizado en la sección 4.

No ejecutes manualmente EV03, EV04 o D1a por separado.

No rerun.
No retry automático.
No resume.
No overwrite.
No cleanup posterior para ocultar un fallo.
No sustituyas scripts.
No cambies el comando.

Si la invocación falla en cualquier etapa: **STOP inmediatamente**. Preserva todos los artefactos que ya existan y no repitas el comando.

---

## 6. ORDEN CONTRACTUAL INMUTABLE

Debe observarse exactamente:

1. `01_unified_preflight`
2. `02_EV03_control_reproduction`
3. `03_EV03_control_reproduction_verification`
4. `04_EV03_corrected_corpus_materialization`
5. `05_EV03_corrected_index_build`
6. `06_EV03_corrected_evaluation`
7. `07_EV04_Decision885_control_reproduction`
8. `08_EV04_control_reproduction_verification`
9. `09_EV04_corrected_corpus_materialization`
10. `10_EV04_corrected_index_build`
11. `11_EV04_corrected_evaluation`
12. `12_D1a_corrected_execution_under_its_own_authorization`
13. `13_integrity_validation`
14. `14_case_level_comparisons`
15. `15_aggregate_comparisons`
16. `16_unified_sensitivity_summary`
17. `17_execution_manifest`
18. `18_exact_hash_ledger`
19. `19_final_completion_state`

EV03 y EV04 deben reproducir su control Decision885 y verificarlo antes del brazo correctivo. Un mismatch del control bloquea todo lo posterior.

D1a se ejecuta únicamente en el paso 12, con pesos congelados, sin retraining y con rebuild atómico del índice/mapping correctivo.

---

## 7. ESTADO CIENTÍFICO DURANTE LA EJECUCIÓN

Hasta que el pipeline termine íntegramente:

- `0B05C_METRIC_IMPACT = NOT_DETERMINED`
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`
- `0B05C_CLOSURE = NOT_AUTHORIZED`

No decidas por tu cuenta si el impacto es material, significativo o irrelevante.

No autorices EXP11B ni EXP12.

---

## 8. SI EL PIPELINE TERMINA EN PASS

Verifica read-only todos los artefactos contractuales generados, incluyendo como mínimo:

- runtime authorization record;
- EV03 Decision885 control reproduction;
- EV03 corrected outputs;
- EV04 Decision885 control reproduction;
- EV04 corrected outputs;
- D1a corrected outputs;
- EV03/EV04 case-level comparisons;
- EV03/EV04 aggregate comparisons;
- D1a comparison artifacts;
- `unified_sensitivity_summary.json`;
- `execution_manifest.json`;
- `unified_output_hash_ledger.json`;
- final completion state.

Verifica que el exact hash ledger corresponda a los archivos realmente producidos.

No recalcules métricas fuera de los productores congelados.

---

## 9. VERSIONADO CANDIDATO PARA AUDITORÍA EXTERNA

Solo si la ejecución completa termina en `PASS`:

1. Mantén `main` sin cambios.
2. Prepara **UN SOLO commit candidato** en la rama local:
   `codex/0b05c-corrective-numerical-execution-v01`.
3. El parent del primer commit candidato debe ser exactamente:
   `06cc75ec173eb6c4b134a45eeb88fe25999f396e`.
4. No hagas merge.
5. No modifiques `.gitignore`.
6. No fuerces al repositorio artefactos binarios pesados o índices regenerables únicamente para poder auditarlos.
7. Versiona con `git add -f` **solo cuando sea necesario** los artefactos textuales/estructurados de evidencia que permitan auditoría independiente: runtime authorization record, summaries, manifests, hash ledger, comparaciones case-level/agregadas y demás evidencia textual contractual razonable.
8. Para artefactos deliberadamente no versionados, reporta obligatoriamente:
   - path;
   - tipo;
   - `size_bytes`;
   - SHA-256;
   - razón de no versionado;
   - entrada correspondiente del exact hash ledger.
9. Publica únicamente esta rama candidata para auditoría externa.

Si la ejecución NO termina en PASS, no crees commit ni push de una ejecución presentada como completa.

---

## 10. REPORTE FINAL OBLIGATORIO

Entrega un único reporte exhaustivo con:

### A. ATTEMPT IDENTITY
- `attempt = 02`
- branch
- HEAD inicial
- tree inicial
- origin/main
- tracked clean
- operaciones Git en curso
- prospective roots before run

### B. PREFLIGHT
- comando exacto
- exit code
- JSON completo relevante
- estado de las cuatro autorizaciones
- confirmación de cero side effects

### C. PERMISSION MODE
- usuario efectivo del preflight
- usuario/permission context efectivo de la invocación numérica
- mecanismo utilizado para salir de la restricción de escritura sandbox
- confirma que NO cambiaste ACL/Defender/OneDrive

### D. NUMERICAL INVOCATION
- comando exacto
- número total de invocaciones del runner en Intento 02
- exit code
- pipeline status
- estado de cada uno de los 19 pasos
- si falló: excepción exacta, paso exacto y artefactos creados antes del fallo

### E. CONTROL REPRODUCTIONS
Para EV03 y EV04:
- status
- exact-match observado
- hashes/identidades relevantes

### F. EV03
- métricas originales
- métricas correctivas
- deltas mecánicos
- casos cuyo ranking cambió
- `case_id` afectados
- ocurrencias/cambios de `87044110` y `87045110`

### G. EV04
Mismos campos que EV03.

### H. D1a
- `weights_unchanged`
- `retraining = false`
- `full_atomic_index_and_mapping_rebuild`
- métricas originales congeladas
- métricas correctivas
- deltas mecánicos
- casos/rankings modificados si existen

### I. UNIFIED
- contenido/resumen de `unified_sensitivity_summary`
- integrity status
- execution manifest status
- exact hash ledger status y conteos
- final completion state

### J. FILE PROVENANCE
Lista exhaustiva de archivos creados/modificados durante Intento 02:
- path
- Git status
- size
- SHA-256
- Git blob SHA-1 cuando corresponda

Distingue siempre Git blob SHA-1 de SHA-256 del contenido.

### K. CANDIDATE COMMIT
Solo si PASS:
- branch
- candidate commit
- parent
- tree
- commit message
- files changed
- ahead/behind vs origin/main
- working tree posterior
- push status

### L. ESTADO FINAL
No declares todavía:
- `0B05C_CLOSURE=CLOSED`
- `DOWNSTREAM_REEXECUTION=JUSTIFIED`
- `DOWNSTREAM_REEXECUTION=NOT_JUSTIFIED`
- `EXP11B_AUTHORIZED`
- `EXP12_AUTHORIZED`

La IA Experimental realizará la auditoría independiente y tomará esas decisiones.

Finaliza y detente. No avances a ningún bloque posterior.
