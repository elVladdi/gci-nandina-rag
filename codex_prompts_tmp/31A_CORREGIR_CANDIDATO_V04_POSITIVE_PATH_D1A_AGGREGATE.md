# PROMPT 31A — CORREGIR CANDIDATO v0.4: POSITIVE AUTH PATH + D1a v0.4 + BASELINE AGREGADO EV04

## Rol

Actúa como **ejecutor técnico controlado**. Este bloque corrige exclusivamente los hallazgos bloqueantes de la auditoría externa del candidato Prompt31.

No reinicies el diseño metodológico MRR. No repitas la investigación `.77/.78`. No ejecutes retrieval, EV03 real, EV04 real, D1a real, EVAL real ni inferencia del modelo.

Este bloque **NO autoriza Attempt05** y **NO autoriza ejecución numérica**.

---

## 1. Baseline y candidato rechazado

Repositorio: `elVladdi/gci-nandina-rag`

Baseline científico protegido:

`main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

Candidato Prompt31 rechazado por auditoría externa:

`69a05710295556e365086c52f93933c5b3a2ad1c`

Rama rechazada:

`codex/0b05c-v04-complete-preexecution-candidate`

No modifiques ni fuerces esa rama publicada.

Crea una rama nueva desde el baseline exacto:

`codex/0b05c-v04-complete-preexecution-candidate-v02`

La historia final del candidato corregido debe tener como parent científico directo el baseline `ba4bd293...`, sin incorporar el commit rechazado `69a057...` como ancestro. Puedes traer su diff al working tree con `git cherry-pick -n 69a057...` o mecanismo equivalente **sin crear commit intermedio**, aplicar las correcciones de este prompt y producir un único commit científico final.

Antes de editar verifica:

- `origin/main == ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`;
- Plan `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- candidato rechazado sigue exactamente en `69a05710295556e365086c52f93933c5b3a2ad1c`;
- Attempt05 sigue `NOT_AUTHORIZED / NOT_EXECUTED`;
- no existe authorization record v0.4 en el baseline;
- working tree tracked limpio.

Si falla cualquiera: `STOP / FAIL_CLOSED`.

---

# 2. Hallazgos bloqueantes que debes corregir conjuntamente

## F31A-01 — El positive authorization transition es imposible con los estados actuales

En el candidato rechazado, `build_bundle()` materializa:

- `gate_status = "CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED"`
- `authorization_readiness = "NOT_AUTHORIZED"`

pero `validate_authorization_transition()` exige como baseline:

- `gate_status == "CANDIDATE_PENDING_EXTERNAL_AUDIT"`
- `authorization_readiness == "NOT_AUTHORIZATION_READY"`

Por tanto, un futuro commit de autorización válido fallaría determinísticamente al cargar la transición.

### Corrección obligatoria

Haz que el validator use exactamente los estados baseline realmente materializados por v0.4. No debilites el immutable projection ni los requisitos de ancestry, bindings o authorization record.

Añade una prueba **positiva** de transición de autorización construida en memoria:

1. construir baseline bundle v0.4;
2. copiarlo independientemente;
3. aplicar solo los campos autorizables declarados;
4. verificar que `validate_authorization_transition()` retorna PASS;
5. alterar un campo científico/ técnico no autorizable y verificar FAIL_CLOSED.

No basta con probar únicamente que el gate no autorizado rechaza ejecución.

---

## F31A-02 — `run_d1a_corrective_0b05c_v03.py` NO es reutilizable como adapter de v0.4

El runner D1a v0.3 está técnicamente acoplado a v0.3: importa `AUDIT_ROOT`, `AUTHORIZATION_RECORD` y `D1A_ROOTS` desde `prepare_0b05c_corrective_numerical_gate_v03.py`, fija `SPEC_PATH` al spec v0.3 y valida que `authorization_record_binding.path` sea el authorization record v0.3.

El unified runner v0.4, en cambio, produciría un proof cuyo authorization record pertenece a v0.4. Por tanto, el adapter v0.3 fallaría incluso con un proof v0.4 correctamente autorizado, y además leería specs/roots v0.3.

### Corrección obligatoria

Crea un adapter nuevo:

`src/experiments/run_d1a_corrective_0b05c_v04.py`

Debe conservar **sin cambios científicos** la lógica D1a v0.3/v0.1, pero parametrizada por las constantes v0.4:

- importar `AUDIT_ROOT`, `AUTHORIZATION_RECORD`, `D1A_ROOTS`, `ROOT`, `git_binding`, `read_json`, `require` desde `prepare_0b05c_corrective_numerical_gate_v04.py`;
- `SPEC_PATH = AUDIT_ROOT / "d1a_numerical_execution_spec_v0.4.json"`;
- proof esperado con authorization record v0.4;
- preflight sobre roots/spec v0.4;
- ninguna modificación de modelo, corpus original, config, evaluator denso o builder denso;
- ninguna ejecución en este prompt.

Actualiza el unified runner v0.4 para importar y usar el adapter D1a v0.4.

Actualiza el D1a spec v0.4 para que:

- `future_authorized_execution_command` apunte a `run_d1a_corrective_0b05c_v04`;
- `preflight_command` apunte a v0.4;
- `orchestration.runner` quede bound al blob del adapter v0.4;
- todos los roots y outputs sigan siendo v0.4.

Actualiza gate/manifest/ledger/bindings canónicos de forma mecánica.

Añade un tercer test específico, recomendado:

`tests/test_d1a_corrective_0b05c_runner_v04.py`

Debe demostrar de forma read-only que el adapter v0.4:

- referencia exclusivamente spec/auth/root v0.4;
- acepta un proof v0.4 estructuralmente válido;
- rechaza proof cuyo authorization record path sea v0.3;
- no referencia D1A_ROOTS v0.3 como roots de ejecución;
- mantiene los bindings del modelo/config/builder/evaluator originales.

---

## F31A-03 — El aggregate comparison EV04 contamina el efecto D906 con el drift aritmético histórico

En el candidato rechazado, `compare_aggregates()` vuelve a leer para EV04:

`run_metadata.json["metrics"]`

como lado original.

Eso reintroduce los literales históricos Gate C `.77` y la contribución histórica no canónica, mientras el lado corrected usa el contrato prospectivo v0.4 (`.78` y contribución racional). Así, incluso con ranking/casos sin cambio, el delta agregado podría contener una diferencia puramente metodológica de 1 ULP y no un efecto de Decision 906.

Esto contradice la decisión integrada: los literales históricos permanecen como provenance, pero **no son oracle computacional prospectivo**.

### Corrección obligatoria

Para EV04, el baseline agregado original debe ser el **canonical expected v0.4 derivado del frozen original case summary**, es decir, el mismo objeto lógico producido desde el lado expected del control v0.4.

Implementa de forma explícita y auditable:

- EV03: conserva su baseline histórico estable actual;
- EV04: usa `control["EV04"]["expected_metrics"]` o una derivación equivalente directamente desde el frozen case summary;
- corrected EV04: usa `corrected["EV04"]["metrics"]`;
- no uses `run_metadata["metrics"]` histórico como baseline agregado EV04 para MRR@100/contribution prospectivos.

Añade una prueba que demuestre:

1. canonical original EV04 vs el mismo canonical original produce **delta cero para todas las filas**, incluidos MRR@100 y contribution 101–200;
2. la ruta histórica `.77` no es utilizada por el helper/productor de aggregate baseline EV04;
3. MRR@200 permanece bajo el contrato legacy y no cambia por esta corrección.

---

## F31A-04 — Estado compuesto de specs dejaría una contradicción después de autorizar

Los specs v0.4 usan actualmente:

`specification_status = "CLOSED_PROSPECTIVELY / NOT_AUTHORIZED / PENDING_EXTERNAL_AUDIT"`

pero la transición de autorización solo permite mutar el own authorization field y `attempt05`. Si se autorizara después, el mismo spec contendría simultáneamente `specification_status ... NOT_AUTHORIZED` y `authorization.<OWN> = AUTHORIZED`.

### Corrección obligatoria

Haz `specification_status` **authorization-neutral y audit-neutral**, por ejemplo:

`PREEXECUTION_SPEC_DEFINED`

y conserva autorización/auditoría en campos separados.

No agregues `specification_status` como campo mutable de autorización si no es necesario.

Verifica los tres specs.

---

# 3. Shadow positivo adicional — obligatorio

Además de conservar Shadow A-F, añade **Shadow G — POSITIVE_AUTHORIZATION_PATH**.

Debe existir en dos niveles:

### G1 — pure in-memory transition

La prueba positiva de `validate_authorization_transition()` descrita en F31A-01 debe PASS.

### G2 — disposable Git authorization preflight

Después de tener un commit científico local candidato, antes de publicarlo:

1. crea un worktree/rama local temporal **no publicada** hija del candidato;
2. materializa allí una autorización **sintética exclusivamente de prueba** cambiando solo los campos permitidos y creando el authorization record v0.4 conforme al contrato;
3. crea un commit local temporal;
4. ejecuta únicamente `run_0b05c_corrective_numerical_v04.preflight_authorized()`;
5. debe PASS y no crear ningún future root;
6. valida además el adapter D1a v0.4 con ese proof, sin llamar `execute_authorized()`;
7. elimina worktree/rama temporal después de la prueba;
8. confirma que ninguna autorización sintética fue pusheada y que el candidato final sigue `NOT_AUTHORIZED`.

Si el entorno local carece de un frozen binary requerido por preflight, no inventes el PASS. Reporta exactamente el bloqueo de entorno y conserva G1 como prueba lógica. Si el binario está disponible, G2 es obligatorio.

Toda esta ejecución es:

`CODEX_LOCAL_PURE_READ_ONLY_OR_DISPOSABLE_GIT_TEST / NOT_INDEPENDENT_GITHUB_CI`

No constituye autorización real.

---

# 4. Revisión ampliada antes de publicar

Haz una segunda pasada de blast radius específicamente sobre **positive path**, no solo closed path. Revisa al menos:

1. candidate -> future authorization transition;
2. future authorization -> unified `preflight_authorized`;
3. proof -> D1a v0.4 adapter;
4. D1a v0.4 spec -> v0.4 roots/output names;
5. EV04 control expected metrics -> aggregate baseline original;
6. aggregate baseline -> unified summary;
7. runtime ledger expected paths después de introducir adapter v0.4;
8. bindings canónicos de gate/manifest/ledger;
9. absence de v0.3 runtime roots como inputs prospectivos;
10. ningún estado interno contradictorio después de una transición simulada.

Persiste estos resultados actualizados en:

`outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json`

El artefacto debe registrar que el candidato Prompt31 `69a057...` fue rechazado por auditoría externa y enumerar F31A-01..F31A-04 como hallazgos corregidos.

---

# 5. Tests mínimos después de la corrección

Ejecuta solamente suites directamente relevantes; no repitas trabajo histórico que no pueda verse afectado.

Como mínimo:

```text
python -B -m unittest \
  tests.test_0b05c_ev04_mrr_contract_v04 \
  tests.test_0b05c_corrective_numerical_gate_v04 \
  tests.test_d1a_corrective_0b05c_runner_v04
```

Además:

- preflight cerrado v0.4;
- G1 positive transition;
- G2 disposable positive preflight si el entorno lo permite;
- test de zero-delta aggregate baseline EV04;
- `git diff --check`.

No ejecutes retrieval ni pipelines reales.

No es necesario volver a ejecutar las suites históricas v0.1/v0.2/v0.3 completas si ningún archivo histórico fue modificado. Basta verificar sus blobs/path immutability y documentar que ya habían sido ejecutadas en Prompt31.

Toda prueba local debe seguir clasificada como `CODEX_LOCAL... / NOT_INDEPENDENT_GITHUB_CI`.

---

# 6. Alcance final permitido

El candidato corregido debe contener únicamente archivos nuevos v0.4 respecto del baseline. Se permiten los 12 paths originales del Prompt31 más:

- `src/experiments/run_d1a_corrective_0b05c_v04.py`
- `tests/test_d1a_corrective_0b05c_runner_v04.py`

Total esperado: **14 paths nuevos**, salvo que justifiques de forma estricta un path adicional de test/audit. No modifiques archivos v0.3 ni históricos.

No crear:

- authorization record v0.4 real;
- outputs runtime;
- Attempt05;
- cambios en Plan/article/EXP11B/EXP12.

---

# 7. Commit y publicación

Produce preferentemente **un único commit científico** con parent directo:

`ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

Publica solo:

`codex/0b05c-v04-complete-preexecution-candidate-v02`

No integres a `main`.

No publiques la rama/worktree sintética de Shadow G2.

---

# 8. Reporte obligatorio

Persiste el reporte en:

`codex_prompts_tmp/31A_RESPUESTA_CORREGIR_CANDIDATO_V04_POSITIVE_PATH_D1A_AGGREGATE.md`

sobre la rama:

`codex/prompts-temporary`

El reporte debe incluir:

- baseline;
- candidato rechazado 69a057...;
- branch/commit/tree/parent del candidato corregido;
- lista exacta de paths y Git blob SHA-1;
- corrección de F31A-01..04;
- resultado de Shadow A-G;
- resultado G2 o razón exacta de imposibilidad ambiental;
- resultado zero-delta aggregate EV04;
- tests ejecutados;
- confirmación de que `main` no cambió;
- confirmación de ausencia de authorization record real;
- `Attempt05 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

Responde únicamente con el reporte final exigido.