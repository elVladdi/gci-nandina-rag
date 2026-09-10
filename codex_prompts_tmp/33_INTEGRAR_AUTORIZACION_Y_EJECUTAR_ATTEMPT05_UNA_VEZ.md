# PROMPT 33 — INTEGRAR AUTORIZACIÓN v0.4 Y EJECUTAR ATTEMPT05 EXACTAMENTE UNA VEZ

## Rol

Actúa como **ejecutor técnico controlado**. Este bloque combina, para reducir ciclos sin debilitar la gobernanza:

1. un precheck ambiental read-only;
2. la integración exacta del candidato de autorización Attempt05 ya auditado externamente;
3. la ejecución de Attempt05 **exactamente una vez**;
4. la persistencia/versionado del resultado bruto o del fallo, sin interpretación científica ni cierre de 0B-05C.

No rediseñes v0.4. No cambies el contrato MRR. No ejecutes más de una invocación del pipeline bajo ninguna circunstancia.

---

# 1. Estado obligatorio de entrada

Repositorio:

`elVladdi/gci-nandina-rag`

Main científico esperado:

`588962100362174df6486a3c6446276d8749743c`

Candidato de autorización auditado externamente:

- rama: `codex/0b05c-v04-attempt05-authorization-candidate`
- commit: `812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`
- parent: `588962100362174df6486a3c6446276d8749743c`
- tree: `90bea7fa9deb9ca5da56274180efef6c31ac29cf`
- diff: exactamente 5 paths de autorización.

La auditoría externa establece:

`AUTHORIZATION_CANDIDATE_AUDIT = PASS / APPROVED_FOR_INTEGRATION`

Plan esperado:

`fe847f708d4d1ded92b5a50a38d4913bb69ed311`

Article esperado:

`254b1e6df736fa9938ac86a515d65b36f4d361c5`

---

# 2. FASE 0 — PRECHECK AMBIENTAL ANTES DE INTEGRAR LA AUTORIZACIÓN

Esta fase es read-only. **Si falla, NO integres la autorización y NO ejecutes Attempt05.**

Verifica:

1. `origin/main == 588962100362174df6486a3c6446276d8749743c`;
2. rama de autorización exacta en `812cb69a...`;
3. compare `588962... -> 812cb69...` = `1 ahead / 0 behind / exactamente 5 paths`;
4. working tree tracked limpio;
5. Plan/article en los heads indicados;
6. en `main` no existe todavía `0b05c_numerical_authorization_record_v0.4.json`;
7. los 16 future roots v0.4 están ausentes del filesystem local;
8. el frozen model requerido para D1a existe localmente en:
   `models/text2trade_mnrl_v0.2/model.safetensors`
   con tamaño exacto `470637416` bytes y SHA-256 exacto
   `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`;
9. no existe otra ejecución local v0.4 previa ni evidencia de una invocación Attempt05 ya iniciada.

No descargues, regeneres ni sustituyas el modelo en este bloque. Si el modelo exacto no está disponible localmente: `STOP / ENVIRONMENT_BLOCKED_BEFORE_AUTHORIZATION_INTEGRATION`.

---

# 3. FASE A — INTEGRAR EXACTAMENTE LA AUTORIZACIÓN

Solo si FASE 0 pasa:

Fast-forward exacto, sin merge commit, squash, rebase ni commit adicional:

`main: 588962100362174df6486a3c6446276d8749743c -> 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`

Después del push verifica:

- `origin/main == 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`;
- tree `90bea7fa9deb9ca5da56274180efef6c31ac29cf`;
- parent único `588962100362174df6486a3c6446276d8749743c`;
- authorization record presente en main;
- cuatro autorizaciones = `AUTHORIZED`;
- `attempt05 = AUTHORIZED / NOT_EXECUTED`;
- ningún código/test/artefacto científico adicional cambió.

Si no es exactamente así: `STOP / FAIL_CLOSED`; no invoques el pipeline.

---

# 4. FASE B — PREFLIGHT AUTORIZADO FINAL

Desde el `main` autorizado, antes de cualquier side effect del pipeline, ejecuta únicamente el preflight read-only:

`run_0b05c_corrective_numerical_v04.preflight_authorized()`

Debe devolver:

- `status = PASS`;
- `mode = AUTHORIZED_PREFLIGHT_ONLY`;
- cuatro autorizaciones presentes;
- baseline de autorización `588962...`;
- authorization commit `812cb69...`;
- future roots ausentes;
- `numerical_execution_occurred = false`.

Valida además, read-only:

- `run_d1a_corrective_0b05c_v04.validate_unified_authorization_proof(proof)`;
- `run_d1a_corrective_0b05c_v04.preflight()`.

Si cualquiera falla: **NO EJECUTES**. Reporta `AUTHORIZED_PREFLIGHT_FAILED / ATTEMPT05_NOT_INVOKED`.

---

# 5. FASE C — EJECUCIÓN ÚNICA ATTEMPT05

Solo si FASE B pasa.

Crea una rama de resultado desde el main autorizado exacto:

`codex/0b05c-v04-attempt05-execution-result`

Ejecuta **una única vez**:

```text
python -B -m src.experiments.run_0b05c_corrective_numerical_v04 --execute-authorized
```

Reglas absolutas:

- `invocation_count = 1`;
- no retry;
- no resume;
- no segunda invocación aunque falle por una excepción aparentemente trivial;
- no ejecutar manualmente EV03, EV04 o D1a para “completar” resultados;
- no corregir outputs después de producirlos;
- no alterar código, tests, specs, gate, autorización, Plan, article, EXP11B o EXP12;
- no interpretar materialidad científica todavía.

Captura el exit code y stdout/stderr completos de esa única invocación.

---

# 6. FASE D — PERSISTENCIA FAIL-CLOSED DEL RESULTADO

Crea en la rama de resultado:

`outputs/audits/0b05c_attempt05_execution_v0.4/attempt05_execution_record_v0.4.json`

Y, cuando sea razonable como texto, persiste también:

- `attempt05_stdout.txt`
- `attempt05_stderr.txt`

El record debe incluir como mínimo:

- `artifact_id`;
- `schema_version`;
- `authorization_commit = 812cb69...`;
- `execution_branch`;
- comando exacto;
- `invocation_count = 1`;
- UTC start/end;
- exit code;
- SHA-256 y tamaño de stdout/stderr;
- resultado del preflight autorizado;
- estado `SUCCESS_PENDING_EXTERNAL_AUDIT` o `FAIL_CLOSED_PENDING_EXTERNAL_AUDIT`;
- último paso completado y último paso iniciado, si son determinables sin inferencia;
- inventario exacto de los 16 future roots indicando existencia y archivos producidos;
- confirmación `retry_count = 0` y `resume_count = 0`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

## Si exit code = 0

Haz únicamente validación post-run read-only:

- resultado final declara las 19 operaciones completas;
- EV03 control = `PASS_EXACT`;
- EV04 control = `PASS_EXACT`;
- D1a = PASS;
- expected runtime roots/outputs existen;
- runtime exact hash ledger existe y no reporta mismatch;
- aggregate EV04 tiene 28 filas;
- no hay paths runtime inesperados según el contrato.

No recalcules ni vuelvas a ejecutar retrieval/modelo para validar.

## Si exit code != 0

- clasifica `FAIL_CLOSED_PENDING_EXTERNAL_AUDIT`;
- no borres los partial roots;
- no los reutilices;
- no vuelvas a ejecutar;
- inventaría exactamente lo producido;
- conserva el traceback/error exacto en stderr;
- no diagnostiques ni corrijas la causa en este bloque.

---

# 7. VERSIONADO DEL RESULTADO

Después de la única ejecución, crea **un único commit de resultado** en:

`codex/0b05c-v04-attempt05-execution-result`

con parent directo:

`812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`

El commit puede contener exclusivamente:

1. outputs generados por esa única ejecución dentro de los 16 future roots v0.4;
2. `outputs/audits/0b05c_attempt05_execution_v0.4/*`;
3. ningún archivo de código/config/spec/gate/autorización ni histórico.

Si algún artefacto binario generado no puede versionarse por una restricción real de Git/repository policy, **no lo transformes**: registra path, SHA-256, tamaño y razón exacta de no versionado en el execution record.

Publica únicamente la rama de resultado. **No integres el resultado a main en este bloque.**

Importante: después de que la invocación única haya ocurrido, la autorización se considera **operacionalmente consumida por Attempt05**, aunque `main` permanezca temporalmente en el commit de autorización hasta la auditoría externa del resultado. Bajo ninguna circunstancia vuelvas a invocar Attempt05.

---

# 8. ESTADO FINAL ESPERADO

Si la ejecución fue exitosa:

```text
main = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
V04_BUNDLE = INTEGRATED
V04_AUTHORIZATION = INTEGRATED
ATTEMPT05 = EXECUTED_ONCE / SUCCESS_PENDING_EXTERNAL_AUDIT
ATTEMPT05_AUTHORIZATION = OPERATIONALLY_CONSUMED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

Si falla:

```text
main = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
V04_AUTHORIZATION = INTEGRATED
ATTEMPT05 = FAIL_CLOSED / EXECUTED_ONCE / PENDING_EXTERNAL_AUDIT
ATTEMPT05_AUTHORIZATION = OPERATIONALLY_CONSUMED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

Si FASE 0 falla, main debe permanecer `588962...`.
Si FASE B falla después de integrar, main queda `812cb69...` pero `ATTEMPT05 = NOT_INVOKED`.

---

# 9. REPORTE OBLIGATORIO

Persiste en `codex/prompts-temporary`:

`codex_prompts_tmp/33_RESPUESTA_INTEGRAR_AUTORIZACION_Y_EJECUTAR_ATTEMPT05_UNA_VEZ.md`

Incluye:

- FASE 0 completa;
- integración exacta de autorización;
- preflight autorizado;
- branch/commit/tree/parent del resultado si hubo invocación;
- comando exacto e `invocation_count`;
- exit code;
- último paso iniciado/completado;
- inventario de roots/outputs;
- hashes del execution record/stdout/stderr;
- resultado de validaciones post-run si hubo éxito;
- confirmación explícita `retry_count = 0`, `resume_count = 0`;
- `main` final;
- Plan/article sin cambios;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

Clasifica correctamente toda ejecución local como `CODEX_LOCAL_RUNTIME_EXECUTION_REPORT / NOT_INDEPENDENT_GITHUB_CI` hasta la auditoría externa.

Responde únicamente con el reporte final exigido.
