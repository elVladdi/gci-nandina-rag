# CODEX — CORREGIR CANDIDATURA EV03 RECOVERY v0.2 DESPUÉS DE AUDITORÍA EXTERNA

## 0. ROL Y ALCANCE

Actúa exclusivamente como **EJECUTOR DE CORRECCIONES DE REPRODUCIBILIDAD** sobre la candidatura ya publicada:

`codex/0b05c-ev03-historical-builder-recovery-v02`

HEAD candidato auditado:

`cef8d7ad58d877e933f8c86b9f721cb214d9058d`

Base científica inmutable:

`06cc75ec173eb6c4b134a45eeb88fe25999f396e`

La auditoría externa considera científicamente plausible y bien sustentada la recuperación:

`EV03_REPRODUCTION_ROOT_CAUSE = CURRENT_BUILDER_SEMANTICS_MISMATCH`

`EV03_RECOVERED_HISTORICAL_TOKEN_POLICY = DROP_SINGLE_CHARACTER_TOKENS`

pero **NO aprueba todavía la candidatura para integración** por defectos de reproducibilidad/procedencia del bundle comprometido.

NO ejecutes EV03 corrected, EV04 corrected, D1a numerical ni el runner unificado. NO autorices ejecución numérica. NO modifiques main, Plan Maestro, article/main-manuscript, EXP11B ni EXP12. NO borres evidencia de Intentos 01/02.

Trabaja sobre la misma rama candidata y agrega, si todo pasa, **un único commit correctivo adicional**. No amend, no rebase, no force-push; el commit `cef8d7ad...` debe conservarse en el historial.

---

## 1. HALLAZGOS EXTERNOS OBLIGATORIOS

### F001 — EL VERIFICADOR VERSIONADO NO ES REEJECUTABLE DESDE EL COMMIT CANDIDATO

En `src/experiments/verify_ev03_historical_builder_recovery_v02.py`, `verify_control()` exige actualmente:

`HEAD == 06cc75ec173eb6c4b134a45eeb88fe25999f396e`

Sin embargo, la candidatura comprometida está en `cef8d7ad...`; por tanto, un checkout limpio del commit candidato no puede ejecutar el propio verificador.

Además, el mismo verificador exige que `AUDIT_ROOT` no exista, pero `AUDIT_ROOT` contiene los artefactos versionados de la candidatura. Incluso eliminando el chequeo de HEAD, un checkout limpio del candidato fallaría por esa condición.

Esto implica que la evidencia fue generada antes del commit y el bundle comprometido no puede regenerar/verificar por sí mismo el control mediante el comando documentado.

**Estado:** `F001 = OPEN / BLOCKING_INTEGRATION`.

### F002 — LAS PRUEBAS NO EJERCITAN EL VERIFICADOR COMPROMETIDO END-TO-END

La suite nueva reconstruye el índice en memoria y compara contra el baseline, lo cual es evidencia valiosa, pero ninguna prueba invoca el flujo completo del verificador comprometido desde un checkout limpio del candidato. Por ello los 12/12 PASS no detectan F001.

**Estado:** `F002 = OPEN / BLOCKING_INTEGRATION`.

### F003 — IDENTIDADES TEXTUALES / LEDGER NO ESTÁN CANONIZADAS DE FORMA PORTABLE

La candidatura registra para `src/configs/experiment_config.json` el SHA-256 del checkout CRLF observado:

`ee23e112fb553a355d9787403eb7fa8688295737f76c7acaff052cc9d0ecb2d3`

pero la identidad canónica del Git blob congelado es:

`107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d`

El artifact de procedencia y el ledger no deben presentar bytes dependientes del checkout como identidad congelada canónica. Además, `.gitattributes` no contiene reglas LF explícitas para los nuevos archivos v0.2.

**Estado:** `F003 = OPEN / BLOCKING_INTEGRATION`.

### F004 — BINDING DE CÓDIGO INSUFICIENTE PARA FUTURA AUTORIZACIÓN

`ev03_corrective_execution_spec_v0.2.json` identifica el builder principalmente por path/token policy, pero no congela explícitamente Git blob SHA-1 + SHA-256 canónico de las dependencias de código que determinan la reproducción: builder recuperado, global `src/bm25_index.py`, evaluator correctivo y retrieval BM25. La candidatura tampoco debe parecer todavía un gate listo para autorización numérica.

**Estado:** `F004 = OPEN / BLOCKING_AUTHORIZATION`.

Este microclose NO debe construir todavía el runner numérico v0.2. Debe cerrar el recovery/preexecution bundle y declarar explícitamente que queda `NOT_AUTHORIZATION_READY` hasta un gate numérico posterior separado.

---

## 2. PRESERVACIÓN OBLIGATORIA

Antes de modificar:

- fetch de `origin`;
- confirma `origin/main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e`;
- confirma la rama candidata remota en `cef8d7ad58d877e933f8c86b9f721cb214d9058d`;
- confirma parent `06cc75ec...` y tree `281806931941e526e590f7d48c8aca01adde600e` del commit auditado;
- confirma que los seis outputs ignorados del Intento 02, si estás en el worktree original, no serán tocados.

Preferir un worktree/checkout limpio separado basado en `cef8d7ad...`.

No usar `git clean`, reset destructivo, checkout sobre el worktree de evidencia ni borrado de roots v0.1.

---

## 3. CORRECCIÓN F001 — VERIFICACIÓN REEJECUTABLE DESDE CANDIDATO COMPROMETIDO

Refactoriza el verificador para que un checkout limpio de la candidatura corregida pueda ejecutar una verificación **read-only respecto de los artefactos versionados** y **build-only en almacenamiento temporal**, sin escribir dentro de los roots contractuales del repositorio.

Requisitos:

1. No exigir `HEAD == BASE_COMMIT`.
2. En su lugar, demostrar que `BASE_COMMIT=06cc75ec...` es ancestro de HEAD y que los frozen dependencies relevantes no han cambiado contra sus identidades canónicas.
3. No exigir ausencia de `AUDIT_ROOT` en modo de replay comprometido.
4. No sobrescribir ni regenerar archivos versionados en `AUDIT_ROOT`.
5. Construir índice/control de replay en `tempfile.TemporaryDirectory()` o raíz temporal externa equivalente; no bajo `data/processed/*` ni `outputs/*` del repo.
6. Comparar el replay temporal contra:
   - índice histórico congelado;
   - ranking EV03 congelado;
   - case summary congelado;
   - métricas congeladas;
   - artefactos de evidencia v0.2 ya versionados.
7. El modo comprometido debe ser read-only sobre el checkout.
8. CLI explícito recomendado:

`python -B -m src.experiments.verify_ev03_historical_builder_recovery_v02 --verify-committed`

No reutilizar `--verify-control` con semántica ambigua si ello dificulta distinguir preparación vs replay.

El resultado debe emitir como mínimo:

- `status=PASS`
- `mode=COMMITTED_REPLAY_READONLY`
- `base_commit_ancestor=true`
- `tracked_worktree_clean=true`
- `LOGICAL_INDEX_IDENTITY=EXACT`
- `EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT`
- ranking/case-summary byte exact
- full metrics exact
- `repo_files_created=0`
- `repo_files_modified=0`
- `repo_files_deleted=0`
- `future_numerical_roots_present=false`

La verificación puede generar temporales fuera del repo y debe eliminarlos al finalizar normalmente.

---

## 4. CORRECCIÓN F002 — TEST END-TO-END DEL REPLAY COMPROMETIDO

Añade tests que invoquen realmente el modo `--verify-committed` mediante subprocess desde un checkout limpio.

Debe existir al menos:

1. test de exit code 0;
2. parse de JSON final y `status=PASS`;
3. `LOGICAL_INDEX_IDENTITY=EXACT`;
4. `EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT`;
5. ausencia de modificaciones tracked después del subprocess;
6. ausencia de los nueve future numerical roots;
7. el replay no crea `AUDIT_ROOT` nuevo ni modifica los artifacts comprometidos;
8. test negativo que demuestre que mutar la semántica recuperada / dependency identity provoca fail-closed antes de declarar PASS, usando fixture/temporary repo cuando sea necesario y sin tocar el checkout real.

La suite anterior de 12 tests debe conservarse salvo correcciones necesarias y ampliarse.

---

## 5. CORRECCIÓN F003 — PORTABILIDAD Y HASHES CANÓNICOS

### 5.1 `.gitattributes`

Agregar exclusivamente las reglas LF necesarias para los nuevos contratos textuales, por ejemplo:

- `src/experiments/build_bm25_ev03_historical_recovered_v02.py text eol=lf`
- `src/experiments/verify_ev03_historical_builder_recovery_v02.py text eol=lf`
- `tests/test_0b05c_ev03_historical_builder_recovery_v02.py text eol=lf`
- `docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md text eol=lf`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/** text eol=lf`

No alterar reglas no relacionadas.

### 5.2 Canonical Git identities

Para todo input/código versionado que el bundle congele, distinguir:

- `git_blob_sha1`
- `canonical_git_blob_sha256` calculado sobre `git cat-file blob <sha1>`
- `worktree_sha256` solo si tiene valor diagnóstico, nunca como identidad autoritativa cuando puede cambiar por EOL.

Para `src/configs/experiment_config.json`, la identidad autoritativa debe ser el blob canónico SHA-256:

`107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d`

No etiquetar `ee23...` como frozen canonical identity.

Actualizar provenance, spec, manifest/ledger y tests según corresponda.

Los outputs temporales/no versionados pueden usar SHA-256 de bytes locales porque son outputs del replay, pero deben clasificarse explícitamente como `GENERATED_LOCAL_OUTPUT`, no como Git identities.

---

## 6. CORRECCIÓN F004 — BINDING PROSPECTIVO DE DEPENDENCIAS

En el spec/gate de recovery v0.2 congela explícitamente las identidades canónicas de, como mínimo:

- `src/experiments/build_bm25_ev03_historical_recovered_v02.py`
- `src/experiments/verify_ev03_historical_builder_recovery_v02.py`
- `src/bm25_index.py`
- `src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py`
- `src/retrieval/bm25.py`
- `src/configs/experiment_config.json`
- corpus Decision885;
- EVAL v0.2;
- índice histórico;
- ranking/case summary/run metadata EV03 congelados.

Para cada archivo de texto Git-tracked, usar Git blob SHA-1 + canonical Git-blob SHA-256. Para binarios como pickle histórico, congelar Git blob SHA-1 + SHA-256 exacto del blob/file.

El verificador `--verify-committed` debe comprobar esos bindings fail-closed.

No vincules el spec a un SHA de commit que requiera autorreferencia imposible. Las identidades de blobs individuales son suficientes para este microclose.

---

## 7. ACLARAR ALCANCE DEL GATE v0.2

Actualizar `0b05c_corrective_numerical_gate_v0.2.json`, spec y documentación para que quede inequívoco:

- `gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT`
- `gate_scope = EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY`
- `authorization_readiness = NOT_AUTHORIZATION_READY`
- cuatro ejecuciones = `NOT_AUTHORIZED`
- corrected flags = false
- `runtime_authorization_record_present=false`
- `0B05C_METRIC_IMPACT=NOT_DETERMINED`
- `DOWNSTREAM_REEXECUTION=NOT_YET_JUSTIFIED`
- `0B05C_CLOSURE=NOT_AUTHORIZED`

No crear todavía `run_0b05c_corrective_numerical_v02.py` ni authorization record. La construcción del gate numérico ejecutable v0.2 será un bloque prospectivo posterior, una vez integrada y auditada esta recuperación.

---

## 8. REGENERACIÓN DE ARTEFACTOS VERSIONADOS

Como los artefactos de audit v0.2 cambiarán, regenera de forma determinista sus contenidos en el worktree de corrección sin usar los roots de Intento 02.

Preserva los hechos científicos ya demostrados:

- `LOGICAL_INDEX_IDENTITY=EXACT`
- ranking frozen SHA `d2edc692...`
- case summary frozen SHA `f75d7d8a...`
- 1056 casos
- 50327 ranking rows
- full metrics exact
- `AUTHENTIC_HISTORICAL_SOURCE_PY=NOT_VERSIONED_AT_INDEX_CREATION`

No conviertas el `.pyc` en fuente auténtica.

El ledger final debe poder distinguir claramente:

- VERSIONED_GIT_BLOB
- FROZEN_BINARY_GIT_BLOB
- GENERATED_LOCAL_OUTPUT

El ledger no debe depender de CRLF del checkout para identidades autoritativas.

---

## 9. TESTS / VALIDACIÓN FINAL

Ejecutar como mínimo:

1. suite completa nueva/actualizada de EV03 recovery;
2. replay `--verify-committed` en checkout limpio;
3. `tests.test_historical_bm25_v02`;
4. `tests.test_normative_bm25_flat_v02`;
5. F003/residual 0B05C v0.1;
6. D1a preexecution + corrective runner tests, siempre que sus dependencias locales estén disponibles.

No ejecutar el runner numérico.

Después de crear el commit correctivo, crear un **segundo checkout limpio detached del nuevo HEAD** y volver a ejecutar obligatoriamente:

- `python -B -m src.experiments.verify_ev03_historical_builder_recovery_v02 --verify-committed`
- suite EV03 recovery

Si cualquiera falla después del commit: STOP; no amend, no force-push y reporta `POSTCOMMIT_CLEAN_REPLAY=FAIL`.

No afirmar tests independientes vía CI si no existe CI.

---

## 10. COMMIT Y PUSH

Si todo lo anterior pasa:

- crear un único commit correctivo adicional encima de `cef8d7ad...`;
- mensaje sugerido: `fix: make EV03 recovery v0.2 self-verifiable and portable`;
- push solo a `codex/0b05c-ev03-historical-builder-recovery-v02`;
- no merge a main.

Reportar parent, tree, changed files y compare vs `06cc75ec...` y vs `cef8d7ad...`.

---

## 11. REPORTE FINAL OBLIGATORIO

Responder únicamente con secciones A–M:

### A. Estado Git
rama, base, HEAD inicial/final, main/origin-main, parent/tree, worktree.

### B. F001
qué cambió en verifier y resultado committed replay.

### C. F002
tests end-to-end nuevos y resultado.

### D. F003
.gitattributes, canonical Git blob identities y tratamiento de CRLF.

### E. F004
lista exacta de bindings de código/input con Git blob SHA-1 y canonical SHA-256.

### F. Reproducción EV03
logical index identity, ranking/case/metrics exactos, witness.

### G. Scope/gate
`EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY`, `NOT_AUTHORIZATION_READY`, cuatro NOT_AUTHORIZED.

### H. Aislamiento
main/Plan/article/EXP11B/EXP12/v0.1 sin cambios; Intento 02 preservado.

### I. Ledger/manifest
paths, categorías, mismatch count.

### J. Tests
RUN/PASS/FAIL/ERROR/SKIP y clean replay postcommit.

### K. Commit candidato corregido
SHA, parent, tree, files, push, ahead/behind.

### L. Limitaciones
sin CI si aplica; source histórico auténtico no versionado; no runner numérico v0.2 todavía.

### M. Estado científico
Terminar exactamente con:

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

No declares integración aprobada; la auditoría externa posterior decidirá.