# PROMPT 32 — INTEGRAR v0.4 Y CONSTRUIR CANDIDATO DE AUTORIZACIÓN ATTEMPT05

## Rol

Actúa como **ejecutor técnico controlado**. Este bloque combina dos transiciones administrativas/científicas de bajo riesgo para reducir ciclos:

1. integrar por fast-forward el candidato v0.4 ya auditado externamente;
2. construir, pero **NO integrar**, el candidato formal de autorización de Attempt05.

Este bloque **NO ejecuta Attempt05**, retrieval, EV03 real, EV04 real, D1a real, EVAL ni inferencia del modelo.

No modifiques el diseño metodológico MRR ni el código v0.4.

---

# 1. Estado obligatorio de entrada

Repositorio:

`elVladdi/gci-nandina-rag`

`main` esperado antes de integrar:

`ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

Candidato v0.4 aprobado por auditoría externa:

- rama: `codex/0b05c-v04-complete-preexecution-candidate-v03`
- commit: `588962100362174df6486a3c6446276d8749743c`
- tree: `cc58251fee6d9d0855037f6bb342c3c1259e09d2`
- parent: `ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

La auditoría externa ha establecido:

`V04_CANDIDATE_AUDIT = PASS / APPROVED_FOR_INTEGRATION`

Plan esperado:

`fe847f708d4d1ded92b5a50a38d4913bb69ed311`

Article esperado:

`254b1e6df736fa9938ac86a515d65b36f4d361c5`

Antes de cualquier escritura verifica:

- `origin/main` exacto en `ba4bd293...`;
- rama candidata exacta en `588962...`;
- compare `ba4bd293... -> 588962...` = 1 ahead / 0 behind / 14 paths nuevos;
- no authorization record v0.4 en candidato;
- `Attempt05 = NOT_AUTHORIZED / NOT_EXECUTED` en candidato;
- Plan y article en los heads indicados;
- working tree tracked limpio.

Si algo falla: `STOP / FAIL_CLOSED`.

---

# 2. FASE A — Integración exacta del bundle v0.4

Integra únicamente mediante **fast-forward**, sin merge commit, rebase, squash ni commit adicional:

`main: ba4bd293... -> 588962100362174df6486a3c6446276d8749743c`

Después del push verifica obligatoriamente:

- `origin/main == 588962100362174df6486a3c6446276d8749743c`;
- tree de `main == cc58251fee6d9d0855037f6bb342c3c1259e09d2`;
- parent único `ba4bd293...`;
- candidate y main apuntan al mismo commit;
- no existe commit científico adicional;
- los 14 paths y blobs siguen exactamente los del candidato auditado;
- no existe authorization record real todavía;
- Attempt05 sigue no ejecutado.

Si la integración no es exactamente esa: `STOP / FAIL_CLOSED` y **no construyas autorización**.

---

# 3. FASE B — Candidato formal de autorización Attempt05

Solo si FASE A pasa, crea desde el nuevo `main = 588962...` una rama nueva:

`codex/0b05c-v04-attempt05-authorization-candidate`

El candidato de autorización debe contener **exactamente 5 paths cambiados** respecto de `588962...`:

1. `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json`
5. `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_numerical_authorization_record_v0.4.json` — NUEVO

No cambies código, tests, manifest, gate hash ledger, shadow audit ni ningún otro artefacto.

## 3.1 Transición permitida del unified gate

Cambia únicamente los campos autorizables ya definidos por el contrato:

- `gate_status` -> `APPROVED / INTEGRATED`
- `authorization_readiness` -> `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`
- `attempt05` -> `AUTHORIZED / NOT_EXECUTED`
- `authorization.EV03_NUMERICAL_EXECUTION` -> `AUTHORIZED`
- `authorization.EV04_NUMERICAL_EXECUTION` -> `AUTHORIZED`
- `authorization.D1A_NUMERICAL_EXECUTION` -> `AUTHORIZED`
- `authorization.UNIFIED_0B05C_NUMERICAL_EXECUTION` -> `AUTHORIZED`
- `authorization.authorization_record_present` -> `true`

Deben permanecer exactamente:

- `authorization.corrective_retrieval_executed = false`
- `authorization.corrective_metrics_computed = false`
- `authorization.runtime_authorization_record_present = false`
- todo campo científico/técnico restante sin cambios.

## 3.2 Transición permitida de specs

En cada spec cambia únicamente:

- su propio `<ARM>_NUMERICAL_EXECUTION` de `NOT_AUTHORIZED` a `AUTHORIZED`;
- `attempt05` de `NOT_AUTHORIZED / NOT_EXECUTED` a `AUTHORIZED / NOT_EXECUTED`.

Debe permanecer:

`specification_status = PREEXECUTION_SPEC_DEFINED`

No conviertas `specification_status` en campo de autorización.

## 3.3 Authorization record v0.4

Crea exactamente el contrato que valida `prepare_0b05c_corrective_numerical_gate_v04.py`:

```json
{
  "artifact_id": "0b05c_numerical_authorization_record_v0.4",
  "schema_version": 3,
  "authorization_baseline_commit": "588962100362174df6486a3c6446276d8749743c",
  "baseline_external_audit": "PASS / APPROVED_FOR_INTEGRATION",
  "baseline_artifacts": {
    "unified_gate": { ...binding exacto en 588962... },
    "ev03_spec": { ...binding exacto en 588962... },
    "ev04_spec": { ...binding exacto en 588962... },
    "d1a_spec": { ...binding exacto en 588962... }
  }
}
```

Cada binding debe derivarse directamente de Git en el baseline `588962...` y contener exactamente:

- `path`
- `git_blob_sha1`
- `canonical_git_blob_sha256`
- `canonical_size_bytes`

No inventes hashes ni uses hashes del commit de autorización.

---

# 4. Validación positiva obligatoria ANTES de publicar el candidato de autorización

Crea un único commit de autorización local con parent directo `588962...` y ejecuta exclusivamente validaciones read-only/preflight; **no llames `execute_authorized()`**.

Debe pasar:

1. `validate_authorization_record_schema()`;
2. ancestry: baseline `588962...` es proper ancestor del commit de autorización;
3. baseline artifact bindings exactos;
4. immutable authorization projection exacta;
5. `run_0b05c_corrective_numerical_v04.preflight_authorized()` -> `PASS / AUTHORIZED_PREFLIGHT_ONLY`;
6. proof contiene las cuatro autorizaciones;
7. `run_d1a_corrective_0b05c_v04.validate_unified_authorization_proof(proof)` -> PASS;
8. `run_d1a_corrective_0b05c_v04.preflight()` -> `PASS / PREEXECUTION_CLOSED_READONLY`;
9. los 16 future roots v0.4 siguen ausentes;
10. `numerical_execution_occurred = false`.

Si el frozen model requerido para el preflight no está materializado localmente, puedes usar exclusivamente el mismo mecanismo read-only/ignorado ya empleado en Shadow G2 para validar su identidad. No lo commits ni lo publiques.

Si cualquier validación falla: no publiques una autorización defectuosa; `STOP / FAIL_CLOSED` y reporta la causa exacta.

---

# 5. Publicación del candidato de autorización

Solo si el preflight positivo pasa:

- publica `codex/0b05c-v04-attempt05-authorization-candidate`;
- **NO** fast-forwardees `main` al commit de autorización;
- **NO** ejecutes Attempt05.

Estado final esperado:

```text
main = 588962100362174df6486a3c6446276d8749743c
V04_BUNDLE = INTEGRATED
AUTHORIZATION_CANDIDATE = VERSIONED / PENDING_EXTERNAL_AUDIT
AUTHORIZATION_IN_MAIN = NOT_YET_INTEGRATED
ATTEMPT05 = NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

No declares `ATTEMPT05 = AUTHORIZED` como estado canónico de `main`; solo existe una **autorización candidata** hasta la auditoría externa e integración posterior.

---

# 6. Alcance prohibido

No ejecutar:

- retrieval;
- EV03 real;
- EV04 real;
- D1a real;
- EVAL real;
- inferencia de modelo;
- `run_0b05c_corrective_numerical_v04 --execute-authorized`;
- ningún paso del pipeline de 19 operaciones.

No modificar:

- Plan Maestro;
- article;
- EXP11B;
- EXP12;
- archivos v0.3/históricos;
- código/tests v0.4 integrado;
- gate manifest/hash ledger/shadow audit.

---

# 7. Reporte obligatorio

Persiste el reporte en:

`codex_prompts_tmp/32_RESPUESTA_INTEGRAR_V04_Y_CONSTRUIR_AUTORIZACION_ATTEMPT05.md`

sobre la rama:

`codex/prompts-temporary`

Incluye obligatoriamente:

### Integración v0.4
- old main;
- new main;
- tree/parent;
- compare old->new;
- confirmación de 14 paths y blobs exactos;
- ausencia de commit adicional.

### Candidato de autorización
- rama;
- commit/tree/parent;
- lista exacta de 5 paths cambiados y sus blobs;
- blob del authorization record;
- bindings baseline del record;
- resultado exacto de immutable projection;
- resultado de `preflight_authorized()`;
- resultado D1a proof/preflight;
- future roots absent;
- confirmación de que no hubo ejecución numérica.

### Estado final
- `main = 588962...`;
- Plan/article sin cambios;
- autorización candidata no integrada;
- `Attempt05 = NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

Toda ejecución local debe clasificarse correctamente como:

`CODEX_LOCAL_READ_ONLY_PREFLIGHT / NOT_INDEPENDENT_GITHUB_CI`

Responde únicamente con el reporte final exigido.
