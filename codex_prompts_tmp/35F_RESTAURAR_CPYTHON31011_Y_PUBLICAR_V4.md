# PROMPT 35F — RESTAURAR CPYTHON 3.10.11 AISLADO + RECONSTRUIR Y PUBLICAR CANDIDATO v4

## Rol y objetivo

Actúa como **ejecutor técnico controlado preautorización**. Prompt35E se detuvo correctamente porque el `python.exe` del venv persistía, pero su instalación base CPython 3.10.11 había desaparecido después del reinicio del host. Este bloque debe restaurar de forma controlada el runtime exacto, reconstruir desde cero el candidato v4 con el contrato F35E de replay histórico obligatorio, ejecutar el reprobe exacto y publicar el candidato **solo si todo pasa**.

**NO autorices ni ejecutes Attempt06. NO reejecutes Attempt05. NO ejecutes retrieval científico, EV03 real, EV04 real, D1a completo ni EVAL real.**

No integres candidatos 35B/35C/35D. Prompt35E no produjo candidato científico.

---

# 1. Estado exacto esperado

Repositorio: `elVladdi/gci-nandina-rag`

Main científico:

`c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`

Refs protegidas:

- Plan `fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- Article `254b1e6df736fa9938ac86a515d65b36f4d361c5`

Candidato Prompt35D de referencia únicamente:

`1f30047b8b3d6d6d484cd6bb96716a0ac1fbd19e`

Stop report Prompt35E:

`codex_prompts_tmp/35E_RESPUESTA_CONTRACTUALIZAR_REPLAY_HISTORICO_V05.md`

Antes de trabajar:

1. `git fetch`;
2. verifica `origin/main == c873ff1...`;
3. verifica Plan/Article exactos;
4. verifica que `1f30047...` NO esté integrado;
5. verifica que no exista rama remota v4 publicada por 35E;
6. verifica que no exista authorization record v0.5 en main;
7. verifica `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
8. verifica que ningún prospective root v0.5 vaya a reutilizarse;
9. no uses partial roots v0.4 como inputs científicos.

Si falla: `STOP / FAIL_CLOSED`.

---

# 2. Restauración del runtime: alcance autorizado

Prompt35E diagnosticó que:

- `.venv/Scripts/python.exe` seguía presente;
- su SHA-256 era `b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961`;
- `.venv/pyvenv.cfg` apuntaba a una instalación base CPython 3.10.11 que ya no existía;
- los paquetes del venv no fueron modificados;
- el bloqueo ocurre al arrancar el intérprete antes del smoke/replay.

Se autoriza **exclusivamente restaurar CPython 3.10.11 de 64 bits**, de forma local/per-user y sin tocar Python global, PATH global ni launcher global.

## 2.1 Fuente autorizada

Única fuente de descarga autorizada para el instalador:

`https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe`

Antes de ejecutar el instalador exige:

- host exacto `www.python.org`;
- nombre exacto `python-3.10.11-amd64.exe`;
- tamaño exacto esperado del artefacto oficial: `29037240` bytes;
- `Get-AuthenticodeSignature` o equivalente Windows => `Status = Valid`;
- firmante atribuible a Python Software Foundation / PSF según la firma válida observada;
- calcula SHA-256 del instalador y regístralo en el reporte administrativo.

No publiques ni commitees el instalador.

Si la descarga, tamaño o firma no cumplen: `STOP / PYTHON_INSTALLER_TRUST_CHECK_FAILED`.

## 2.2 TargetDir derivado, no hard-coded

Lee el `home` de `.venv/pyvenv.cfg` y úsalo como target de restauración. No hardcodees ni publiques la ruta absoluta del usuario.

Requiere antes de instalar:

- `version = 3.10.11` o evidencia equivalente compatible en `pyvenv.cfg`;
- que el home faltante sea el único motivo estructural visible por el que el venv no arranca;
- que el target no sea un directorio global/sistema.

Ejecuta instalación silenciosa **per-user** con `TargetDir=<home derivado>`, al menos:

- `/quiet`
- `InstallAllUsers=0`
- `Include_launcher=0`
- `PrependPath=0`
- `Include_exe=1`
- `Include_lib=1`
- `Include_pip=1`
- `Include_dev=1`
- `Include_test=0`
- `Include_doc=0`
- `Shortcuts=0`

No modifiques PATH del sistema ni instales launcher global.

Después verifica que el base `python.exe` restaurado informa exactamente CPython 3.10.11, 64-bit Windows/AMD64.

## 2.3 Primero reutiliza el `.venv` existente

Una vez restaurado el base, prueba **primero** el `.venv` existente. No reinstales paquetes si ya pasa el contrato.

Exige:

- `.venv/Scripts/python.exe` inicia;
- SHA-256 del launcher = `b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961`;
- Python = 3.10.11;
- las 8 dependencias críticas exactas del contrato Prompt35D;
- las 42 distribuciones exactas del contrato Prompt35D;
- no package install/update si ya coincide.

### Fallback controlado

Solo si restaurar el base no hace utilizable el `.venv` existente por corrupción del propio venv, se permite crear un venv **nuevo y aislado** exclusivamente para Attempt06 usando el CPython 3.10.11 restaurado.

- nombre recomendado `.venv-0b05c-v05`;
- exclúyelo solo localmente, nunca mediante cambio científico necesario;
- instala paquetes solo dentro de ese venv;
- usa exactamente las versiones definidas en `TESTED_ENVIRONMENT` del candidato Prompt35D;
- ninguna sustitución de versión está permitida;
- no instales nada globalmente;
- no descargues modelos ni datos científicos.

Si el launcher SHA del venv nuevo difiere del anterior, eso NO puede ocultarse: solo puede aceptarse si versión/plataforma/stack/model/smoke/replay son exactos; en tal caso actualiza explícitamente el environment contract al nuevo executable SHA al reconstruir v4 y documenta la razón. Si el `.venv` existente revive, preserva el SHA anterior.

Si no se logra un entorno exacto: STOP y no publiques v4.

---

# 3. Reconstrucción limpia del candidato v4

Crea desde `main = c873ff1...`:

`codex/0b05c-v05-remediated-preauthorization-candidate-v4`

Debe ser un único commit con parent directo `c873ff1...` y sin merge.

Recupera el contenido técnicamente válido de Prompt35D `1f30047...` al working tree/index **sin hacerlo ancestro**, y reaplica íntegramente F35E conforme a:

`codex_prompts_tmp/35E_CONTRACTUALIZAR_REPLAY_HISTORICO_V05.md`

No dependas del staged local de la sesión anterior; reconstruye el resultado de manera reproducible.

F35E debe quedar materializado, no solo descrito:

- `historical_vector_replay_required = true` en el contrato;
- replay required, no optional;
- ausencia/mismatch de vectors/docstore/id_map/sample => fail closed;
- sample SHA exacto, 21 filas, 21 índices únicos, rango válido, hashes de texto;
- result required PASS + sample_count 21;
- environment preflight exige replay required PASS;
- readiness registra required=true y PASS;
- runtime authorization record y execution manifest futuro conservan la evidencia del replay requerido;
- `docs/exp04_text2trade_mnrl_d1a_v02_reproducibility_manifest.json` puede incorporarse como dependencia runtime versionada si la derivación implementada por F35E lo requiere; en ese caso bindings 54 = 31 source + 23 data, con justificación explícita.

Regenera los artefactos v0.5 gobernados desde el código final; no copies artefactos 35D sin regenerarlos cuando F35E cambie su contenido contractual.

---

# 4. Reprobe exacto obligatorio ANTES de commit/push

Con el intérprete final seleccionado ejecuta un reprobe fresco:

1. executable SHA exacto al contract final;
2. CPython 3.10.11 / Windows / AMD64 / 64bit;
3. 8 paquetes críticos exactos;
4. 42 distribuciones exactas;
5. project-local import closure exacto;
6. runtime data dependency bindings exactos;
7. model manifest 9/9 PASS_EXACT;
8. offline smoke 32x384, float32, finite, normalized dentro de `8*eps(float32)`;
9. historical vector replay **REQUIRED / 21/21 PASS**;
10. capacity PASS;
11. authorization record v0.5 ausente;
12. 16 future roots v0.5 ausentes;
13. scientific execution = false.

Si cualquiera falla: STOP, no commit, no push.

---

# 5. Tests obligatorios

Ejecuta y reporta como:

`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`

1. suite F35E completa, incluidos negativos 1-13;
2. suite focalizada v0.5 completa;
3. tests de bindings/autorización;
4. tests D1a strong validation;
5. tests manifest/physical ledger/19-step orchestration;
6. regresión v0.4 relevante, reportando honestamente los tres non-successes históricos conocidos si persisten.

Además repite negativos ambientales mínimos:

- required replay result NOT_AVAILABLE => FAIL_CLOSED;
- sample_count != 21 => FAIL_CLOSED;
- package version drift => FAIL_CLOSED;
- executable SHA drift => FAIL_CLOSED;
- project import closure drift => FAIL_CLOSED;
- capacity below margin => FAIL_CLOSED.

No uses full retrieval/D1a/EVAL para estas pruebas.

---

# 6. Preservaciones

No cambies:

- MRR@100 racional prospectivo v0.4;
- MRR@200 legacy;
- contribución 101-200 racional;
- EV04 aggregate 28 filas;
- EV03 recovered historical semantics;
- Decision906 exactamente `87044110` y `87045110`;
- D1a frozen/no retraining;
- EVAL N=1056;
- 19 pasos;
- 16 roots v0.5;
- `V04_PARTIAL_ROOTS = NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05`;
- exact-five-path future authorization commit;
- strong D1a validation;
- physical runtime ledger;
- manifest provenance;
- Attempt05 fail-close.

No modifiques Plan, Article, EXP11B ni EXP12.

---

# 7. Publicación permitida

Solo si runtime restoration + F35E + reprobe + tests pasan:

- crea un único commit científico v4 con parent directo `c873ff1...`;
- publica únicamente la rama candidata v4;
- NO integres main;
- NO crees authorization record v0.5;
- NO autorices Attempt06;
- NO ejecutes Attempt06.

El entorno local y el instalador NO deben entrar al commit.

No publiques rutas absolutas host-locales en artefactos científicos. En el reporte administrativo usa solo rutas relativas o clasificación abstracta; no repitas el directorio de usuario.

---

# 8. Reporte obligatorio

Persistir en:

`codex_prompts_tmp/35F_RESPUESTA_RESTAURAR_CPYTHON31011_Y_PUBLICAR_V4.md`

sobre `codex/prompts-temporary`.

Debe incluir:

- trust check del instalador oficial sin ruta host-local;
- si se revivió `.venv` o se usó fallback;
- installs/updates realmente ocurridos;
- environment fingerprint final;
- branch/commit/parent/tree v4;
- diff exacto contra `c873ff1...`;
- paths conceptualmente distintos de Prompt35D;
- F35E materializado;
- reprobe final;
- tests;
- riesgos residuales;
- estado final exacto.

## Estado final permitido si PASS

```text
PROMPT35F = COMPLETED
ENVIRONMENT_RESTORATION = PASS / ISOLATED / EXACT
F35E_01_HISTORICAL_REPLAY_CONTRACT = CLOSED_BY_CODE_TEST_AND_FRESH_EXACT_REPROBE
V05_CANDIDATE_V4 = BUILT / PUBLISHED / PENDING_EXTERNAL_AUDIT
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

Si falla la restauración o reprobe:

```text
PROMPT35F = STOP / ENVIRONMENT_RESTORATION_OR_REPROBE_FAILED
V05_CANDIDATE_V4 = NOT_PUBLISHED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
```
