# PROMPT 47 — INTEGRAR PAQUETE V03 Y PREPARAR AUTORIZACIÓN ONE-SHOT EXP11B

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque tiene dos fases y **NO ejecuta retrieval H150/H200**:

1. integrar exactamente en `main` el paquete de ejecución EXP11B v0.3 ya aprobado por auditoría externa;
2. desde el nuevo `main`, construir y publicar **únicamente un candidato de autorización one-shot**, sin integrarlo y sin consumirlo.

No ejecutes EXP11B Retrieval, no calcules métricas/rankings H150/H200 y no avances a EXP12.

---

# 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt46 concluyó:

```text
PROMPT46_EXTERNAL_AUDIT = PASS / APPROVED_FOR_INTEGRATION
EXP11B_RETRIEVAL_EXECUTION_PACKAGE_V03 = APPROVED_FOR_INTEGRATION
F005 = CLOSED
F006 = CLOSED
F003_NO_REGRESSION = PASS
F004_NO_REGRESSION = PASS
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato aprobado:

```text
branch = codex/exp11b-retrieval-execution-package-v03
commit = 50d90a356a0fac0267c270568f3926430a246026
parent = 09ff184854659110f7711b3eee65fc18927649da
```

Los candidatos v01 y v02 continúan rechazados e inmutables:

```text
26b9e2bcf6dad74231f208f9137ffb0e39caf2e1 = DO_NOT_INTEGRATE
f5dddac0d296e74e5f92af3f863cbb3c74e757b9 = DO_NOT_INTEGRATE
```

---

# 2. Precondiciones Git exactas

Ejecuta `git fetch` y verifica:

```text
origin/main = 09ff184854659110f7711b3eee65fc18927649da
origin/codex/exp11b-retrieval-execution-package-v03 = 50d90a356a0fac0267c270568f3926430a246026
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Verifica también:

```text
50d90a356a0fac0267c270568f3926430a246026 parent = 09ff184854659110f7711b3eee65fc18927649da
50d90a... is exactly 1 commit ahead / 0 behind main
50d90a... changes exactly 3 paths
```

Paths del candidato aprobado:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.3.json
src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.3.json
src/experiments/run_exp11b_historical_retrieval_h150_h200_v03.py
```

Si cualquier ref o diff difiere: `STOP / PRECONDITION_REF_DRIFT`.

---

# 3. Fase A — integración exacta del paquete v0.3

Integra mediante **fast-forward exacto**:

```text
09ff184854659110f7711b3eee65fc18927649da
→
50d90a356a0fac0267c270568f3926430a246026
```

No hagas merge commit, squash, cherry-pick, rebase, amend ni reconstrucción.

Después del push exige:

```text
origin/main = 50d90a356a0fac0267c270568f3926430a246026
```

Verifica que no exista en `main` ningún commit adicional.

No modifiques Plan Maestro ni Article.

---

# 4. Fase B — candidato prospectivo de autorización one-shot

Solo después de que Fase A sea correcta, crea desde el nuevo:

```text
origin/main = 50d90a356a0fac0267c270568f3926430a246026
```

la rama:

```text
codex/exp11b-retrieval-authorization-v03
```

El único commit de esa rama debe añadir **exclusivamente**:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.3.json
```

No modifiques runner, config, readiness, bancos, gate histórico, Plan, Article ni ningún otro archivo.

El candidato de autorización **NO está integrado ni puede ejecutarse en este Prompt47**.

---

# 5. Contenido exacto de la autorización candidata

El JSON debe contener como mínimo, con estos valores exactos:

```text
authorization_id = EXP11B_H150_H200_AUTH_001
attempt_id = EXP11B_H150_H200_ATTEMPT_001
authorization_status = AUTHORIZED_ONE_SHOT

approved_package_commit = 50d90a356a0fac0267c270568f3926430a246026

runner_path = src/experiments/run_exp11b_historical_retrieval_h150_h200_v03.py
runner_git_blob = 90bbeba27e4890613cb463fffc1cfc07252292c5
runner_sha256 = 32f495996b8f1486cc6ef5f3906e84eb417e480208a721fb8b1c3f6820e65e06

config_path = src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.3.json
config_git_blob = 08cc58f95b2d6989bf75e64b16c0d9aa8158f642
config_sha256 = 2b91c06762409d10478cbf112bb25486ef3ffa410e5819fb0704f61fe64aa6af

eval_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
bank_manifest_sha256 = 67512d88a46dcd85427d9eca4be07eeea3f6ec2821bf77e7acfec5a09a706cf4
bank_ledger_sha256 = 9686c2f642ec47c36079a3085c4d68a3f1b555588a8623ecca59333e12e0f56c
portability_closure_blob = bfbeedff9025ae928a85ab8b65a261ff475422cb
expected_banks = 20
official_output_root = outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1
```

Puedes añadir exclusivamente metadatos auditables no ambiguos, por ejemplo:

```text
experiment_id = EXP-11B
scope = H150_H200_HISTORICAL_RETRIEVAL_ONLY
authorization_kind = PROSPECTIVE_ONE_SHOT
authorization_candidate_status = PENDING_EXTERNAL_AUDIT_NOT_EFFECTIVE_ON_MAIN
issued_after_external_audit = PROMPT46_EXTERNAL_AUDIT_PASS
```

No añadas parámetros científicos nuevos ni campos que modifiquen la semántica del runner.

---

# 6. Validaciones no consumidoras del candidato

Sobre la rama candidata de autorización, sin ejecutar scoring ni crear marcadores reales:

1. verifica que el authorization JSON sea JSON válido;
2. verifica que `HEAD:<canonical_authorization_path>` exista;
3. verifica que el working-tree blob del authorization sea idéntico a HEAD;
4. verifica que los bytes/SHA-256 working-tree del authorization sean idénticos a HEAD;
5. importa el runner v03 y ejecuta únicamente su validación de autorización (`_validate_authorization` o equivalente) contra la ruta canónica;
6. verifica que devuelve:
   - `approved_package_commit = 50d90a...`;
   - `execution_head = <commit candidato de autorización>`;
   - authorization path canónico;
   - authorization Git blob observado;
   - authorization SHA-256 observado;
7. verifica que `approved_package_commit` es ancestro de `execution_head`;
8. verifica que runner/config en package commit, HEAD y working tree conservan exactamente los blobs/hashes aprobados;
9. verifica que no existe marcador oficial real para `EXP11B_H150_H200_AUTH_001--EXP11B_H150_H200_ATTEMPT_001`;
10. verifica que no existe el output root oficial.

Estas validaciones son **pre-ejecución y no consumen autorización**.

NO invoques `--execute-official` en Prompt47.

---

# 7. Estado epistemológico y de autorización

Aunque el JSON candidato contenga:

```text
authorization_status = AUTHORIZED_ONE_SHOT
```

el estado canónico tras Prompt47 debe seguir siendo:

```text
EXP11B_RETRIEVAL_AUTHORIZATION = CANDIDATE / PENDING_EXTERNAL_AUDIT / NOT_INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED_ON_MAIN / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No presentes el candidato como autorización efectiva mientras no esté auditado externamente e integrado en `main`.

---

# 8. Prohibiciones absolutas

NO:

- ejecutar `--execute-official`;
- ejecutar scoring H150/H200;
- calcular/observar métricas o rankings H150/H200;
- crear marcador real de consumo;
- crear output root oficial;
- integrar el candidato de autorización a `main`;
- crear una segunda autorización;
- modificar la autorización después de su commit;
- integrar v01/v02 rechazados;
- modificar Plan Maestro;
- modificar Article;
- modificar EXP12;
- avanzar Grupo 2B/Grupo 3;
- hacer retry/resume/overwrite.

Si cualquier validación falla: `STOP`, conserva evidencia y no fabriques una nueva autorización automáticamente.

---

# 9. Persistencia administrativa

Después del trabajo:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch`;
3. no hagas rebase/amend/force;
4. crea únicamente:

```text
codex_prompts_tmp/47_RESPUESTA_INTEGRAR_PAQUETE_V03_Y_PREPARAR_AUTORIZACION_ONE_SHOT_EXP11B.md
```

El commit administrativo debe contener solo esa respuesta.

---

# 10. Reporte obligatorio

Reporta al menos:

```text
PROMPT47 = COMPLETED | STOP

main_initial
main_final
package_integration_mode
package_integrated_commit
package_changed_paths

plan_head_initial/final
article_head_initial/final

AUTHORIZATION_CANDIDATE_BRANCH
AUTHORIZATION_CANDIDATE_COMMIT
AUTHORIZATION_CANDIDATE_PARENT
AUTHORIZATION_CANDIDATE_TREE
AUTHORIZATION_CHANGED_PATH_COUNT
AUTHORIZATION_PATH
AUTHORIZATION_GIT_BLOB
AUTHORIZATION_SHA256

AUTHORIZATION_JSON_VALID
AUTHORIZATION_HEAD_TRACKED
AUTHORIZATION_HEAD_WORKTREE_BLOB_IDENTITY
AUTHORIZATION_HEAD_WORKTREE_SHA256_IDENTITY
APPROVED_PACKAGE_IS_ANCESTOR_OF_AUTHORIZATION_HEAD
RUNNER_PACKAGE_HEAD_WORKTREE_IDENTITY
CONFIG_PACKAGE_HEAD_WORKTREE_IDENTITY
NONCONSUMING_AUTHORIZATION_VALIDATION

OFFICIAL_OUTPUT_ROOT_EXISTS
REAL_CONSUMPTION_MARKER_EXISTS
H150_H200_SCORING_COUNT
H150_H200_RESULTS_OBSERVED

EXP11B_RETRIEVAL_AUTHORIZATION = CANDIDATE / PENDING_EXTERNAL_AUDIT / NOT_INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED_ON_MAIN / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No declares PASS externo. Solo IA Experimental puede aprobar el candidato de autorización.
