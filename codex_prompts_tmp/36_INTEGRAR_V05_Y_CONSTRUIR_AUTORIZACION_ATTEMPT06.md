# PROMPT 36 — INTEGRAR v0.5 Y CONSTRUIR AUTORIZACIÓN DE ATTEMPT06

## Rol y objetivo

Actúa como **ejecutor técnico controlado**. Este bloque ya no es una remediación preventiva: debe avanzar el experimento 0B-05C.

La auditoría externa de Prompt35F aprueba para integración el candidato:

- rama `codex/0b05c-v05-remediated-preauthorization-candidate-v4`
- commit `e7cab327f0ef12b1e8ae21cddd01d215cd42db31`
- parent `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`
- tree `6ffb42b20182e9abf1f1adb95083a95bae5dfd67`

Objetivos únicos:

1. integrar ese candidato exactamente en `main`;
2. hacer un reprobe fresco mínimo y suficiente del entorno contractual;
3. si el reprobe pasa, construir una **autorización separada de Attempt06** en un único commit hijo directo del nuevo `main`;
4. ejecutar el `preflight_authorized()` read-only contra ese commit;
5. **NO ejecutar Attempt06** en este bloque.

No abras nuevas rondas de hardening ni añadas controles que no sean necesarios para la validez experimental o para que la ejecución pueda realizarse correctamente.

---

# 1. Estado esperado de entrada

Repositorio: `elVladdi/gci-nandina-rag`

Antes de cualquier write:

- `git fetch`;
- `origin/main == c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`;
- candidato v4 remoto exacto `e7cab327f0ef12b1e8ae21cddd01d215cd42db31`;
- candidato v4 es exactamente 1 commit ahead / 0 behind de `c873ff1...`;
- Plan `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- Article `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- authorization record v0.5 ausente;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- 16 prospective roots v0.5 ausentes;
- working tree limpio.

Si cualquiera falla: `STOP / FAIL_CLOSED`.

---

# 2. Fase A — Integración exacta del candidato v4

Integra `e7cab327...` en `main` exclusivamente mediante fast-forward.

Resultado obligatorio:

`main = e7cab327f0ef12b1e8ae21cddd01d215cd42db31`

No cherry-pick, merge commit, squash, amend, rebase ni cambios adicionales.

Después verifica:

- tree exacto `6ffb42b20182e9abf1f1adb95083a95bae5dfd67`;
- Plan y Article intactos;
- ningún cambio en EXP11B/EXP12;
- authorization record v0.5 todavía ausente;
- Attempt06 todavía no autorizado.

Si la integración no es bit-exact: STOP.

---

# 3. Fase B — Reprobe fresco mínimo antes de autorizar

Usa el mismo entorno exacto que pasó Prompt35F. No instales, actualices ni elimines paquetes. No descargues modelo ni datos.

Ejecuta exclusivamente el preflight ambiental/readiness necesario para confirmar que siguen pasando:

- Python 3.10.11 / CPython / Windows AMD64 64-bit;
- executable SHA-256 exacto gobernado;
- 8 paquetes críticos exactos;
- stack de distribuciones gobernado;
- project-local import closure exacto;
- runtime data dependency bindings exactos;
- model manifest 9/9;
- smoke offline 32x384 float32 finito normalizado;
- replay histórico obligatorio 21/21 PASS;
- capacidad de disco y memoria PASS;
- 16 prospective roots v0.5 ausentes.

Clasifica el resultado como `CODEX_LOCAL_ENVIRONMENT_REPROBE / NOT_INDEPENDENT_GITHUB_CI`.

Si falla un requisito que impide ejecutar correctamente o compromete datos/método/validez: STOP. No abras otro bloque de hardening dentro de este prompt.

---

# 4. Fase C — Rama de autorización

Solo si A y B pasan, crea desde el nuevo `main = e7cab327...`:

`codex/0b05c-v05-attempt06-authorization`

La autorización debe consistir en **exactamente un commit hijo directo** de `e7cab327...`.

Diff baseline→authorization exactamente de cinco paths:

```text
M outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json
M outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev03_numerical_execution_spec_v0.5.json
M outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev04_numerical_execution_spec_v0.5.json
M outputs/audits/0b05c_corrective_numerical_gate_v0.5/d1a_numerical_execution_spec_v0.5.json
A outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_numerical_authorization_record_v0.5.json
```

Ningún otro path puede cambiar.

## 4.1 Cambios permitidos en el gate

Modifica únicamente los campos autorizables ya previstos por el contrato v0.5:

- `gate_status = APPROVED / INTEGRATED`
- `authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`
- `attempt06 = AUTHORIZED / NOT_EXECUTED`
- `authorization.EV03_NUMERICAL_EXECUTION = AUTHORIZED`
- `authorization.EV04_NUMERICAL_EXECUTION = AUTHORIZED`
- `authorization.D1A_NUMERICAL_EXECUTION = AUTHORIZED`
- `authorization.UNIFIED_0B05C_NUMERICAL_EXECUTION = AUTHORIZED`
- `authorization.authorization_record_present = true`

Mantén sin cambio:

- `runtime_authorization_record_present = false`
- `corrective_retrieval_executed = false`
- `corrective_metrics_computed = false`
- `attempt05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED`
- todo contenido científico/técnico restante.

## 4.2 Cambios permitidos en specs

En cada spec EV03/EV04/D1a cambia exclusivamente:

- su flag de autorización correspondiente a `AUTHORIZED`;
- `attempt06 = AUTHORIZED / NOT_EXECUTED`.

Nada más.

## 4.3 Authorization record

Crea el record con el schema exacto ya definido por v0.5:

- `artifact_id = 0b05c_numerical_authorization_record_v0.5`
- `schema_version = 1`
- `authorization_baseline_commit = e7cab327f0ef12b1e8ae21cddd01d215cd42db31`
- `baseline_external_audit = PASS / APPROVED_FOR_INTEGRATION`
- `baseline_artifacts` con bindings exactos de los cuatro artefactos del baseline `e7cab327...`:
  - path
  - git_blob_sha1
  - canonical_git_blob_sha256
  - canonical_size_bytes

No inventes valores; derívalos desde Git.

---

# 5. Fase D — Validación post-commit de autorización

Después de crear y publicar el commit de autorización:

1. verifica que parent sea exactamente `e7cab327...`;
2. verifica diff exact-five-path;
3. verifica bindings baseline↔authorization;
4. verifica filesystem tracked limpio y correspondiente al commit;
5. verifica immutable projection;
6. verifica authorization record schema y bindings;
7. ejecuta `preflight_authorized()` read-only usando el intérprete exacto;
8. exige resultado:
   - `status = PASS`
   - `mode = AUTHORIZED_PREFLIGHT_ONLY`
   - 4 autorizaciones = `AUTHORIZED`
   - replay requerido 21/21 PASS
   - `numerical_execution_occurred = false`
   - 16 prospective roots ausentes.

**NO llames `--execute-authorized`. NO ejecutes ninguna operación científica de los 19 pasos.**

Los probes y tests locales siguen siendo `CODEX_LOCAL_* / NOT_INDEPENDENT_GITHUB_CI`.

---

# 6. Prohibiciones

En este bloque NO:

- ejecutar Attempt06;
- reejecutar Attempt05;
- ejecutar EV03 real/EV04 real/D1a completo/EVAL real;
- producir nuevos resultados métricos;
- instalar/actualizar/eliminar dependencias;
- cambiar modelo;
- tocar Plan o Article;
- tocar EXP11B o EXP12;
- abrir una nueva remediación por mejoras técnicas marginales.

Si aparece una observación no bloqueante, regístrala como deuda técnica y continúa.

Solo detente por algo que:

- impida la ejecución;
- pueda alterar inputs/outputs;
- cambie el método congelado;
- o comprometa la validez de resultados.

---

# 7. Salida obligatoria

Reporta:

- main antes/después de integración;
- branch y commit de autorización;
- parent/tree del commit de autorización;
- diff exacto de cinco paths;
- bindings del authorization record;
- fresh environment reprobe;
- resultado `preflight_authorized()`;
- confirmación de que Attempt06 no fue ejecutado;
- Plan/Article intactos;
- estado exacto final.

Estado final esperado:

```text
V05 = INTEGRATED
V05_BASELINE_COMMIT = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
ATTEMPT06_AUTHORIZATION = VERSIONED / PENDING_EXTERNAL_AUDIT
ATTEMPT06 = AUTHORIZED_IN_CANDIDATE_BRANCH / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

Persiste obligatoriamente el reporte en:

`codex_prompts_tmp/36_RESPUESTA_INTEGRAR_V05_Y_CONSTRUIR_AUTORIZACION_ATTEMPT06.md`

en rama `codex/prompts-temporary`.

Responde únicamente con el reporte final exigido.
