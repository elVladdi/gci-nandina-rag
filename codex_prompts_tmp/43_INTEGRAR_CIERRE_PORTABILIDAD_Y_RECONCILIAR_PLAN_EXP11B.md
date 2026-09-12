# PROMPT 43 — INTEGRAR CIERRE DE PORTABILIDAD EXP11B Y RECONCILIAR PLAN MAESTRO

## Rol y objetivo

Actúa como **ejecutor técnico controlado**. La IA Experimental auditó externamente el resultado de Prompt42 contra GitHub y aprobó el candidato formal de cierre de la deuda de portabilidad de EXP11B.

Este bloque tiene exactamente dos objetivos:

1. integrar por fast-forward en `main` el registro formal de cierre de `EXP11B_PORTABILITY_DEBT` ya auditado externamente;
2. reconciliar de forma mínima el Plan Maestro canónico para que refleje el cierre aprobado e integrado de la deuda, **sin autorizar ni ejecutar EXP11B Retrieval H150/H200**.

Este bloque NO ejecuta retrieval, NO calcula métricas H150/H200, NO modifica EXP12, NO modifica Article y NO abre Grupo 2B ni bloques posteriores.

---

# 1. Dictamen externo que gobierna este bloque

La IA Experimental establece:

```text
PROMPT42_EXTERNAL_GIT_AUDIT = PASS / APPROVED_FOR_INTEGRATION
PORTABILITY_CLOSURE_RECORD = APPROVED_FOR_INTEGRATION
EXP11B_PORTABILITY_DEBT = CLOSED_BY_EXTERNAL_DECISION / PENDING_CLOSURE_RECORD_INTEGRATION
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

La aprobación externa se limita a integrar el closure record y reconciliar el Plan. No constituye autorización de retrieval.

---

# 2. Refs obligatorias de entrada

Repositorio:

`elVladdi/gci-nandina-rag`

Haz `git fetch --all --prune` y verifica exactamente:

## 2.1 Main científico

`origin/main = 7d7267f8224e56ea5e945625a7e3955ddc15eadb`

Este commit ya contiene integrado el proof Prompt41:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_replay_proof_v0.1.json`

Blob Git esperado:

`ab3ed6aadaaebbfc3d23c725d3ad53e9518b1ead`

## 2.2 Candidato de cierre Prompt42 aprobado

Rama:

`codex/exp11b-portability-debt-external-closure-v01`

Commit:

`09ff184854659110f7711b3eee65fc18927649da`

Parent directo obligatorio:

`7d7267f8224e56ea5e945625a7e3955ddc15eadb`

Único path añadido:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_debt_external_closure_v0.1.json`

Blob Git esperado:

`bfbeedff9025ae928a85ab8b65a261ff475422cb`

El compare `7d7267f... -> 09ff184...` debe ser exactamente:

- 1 commit ahead;
- 0 behind;
- 1 changed path;
- solo el JSON anterior.

## 2.3 Plan Maestro canónico

Rama:

`docs/plan-maestro-temporal-2026-08-31`

Commit inicial obligatorio:

`b814a8c2f976185209153e97e0d6ece0510526fb`

Archivo canónico:

`docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`

## 2.4 Article protegido

`article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`

Si cualquiera de estas refs científicas/protegidas difiere antes de iniciar: `STOP / PRECONDITION_DRIFT`.

---

# 3. Auditoría read-only previa del closure record

Antes de integrar, verifica que el closure record conserve exactamente, como mínimo:

```text
artifact_id = exp11b_portability_debt_external_closure_v0.1
schema_version = 1
baseline_commit = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
status = CANDIDATE_CLOSURE_RECORD / EXTERNAL_DECISION_ALREADY_PASS / PENDING_GIT_AUDIT_AND_INTEGRATION
external_audit_verdict = PASS / APPROVED_FOR_PORTABILITY_DEBT_CLOSURE
prompt40_candidate_status = REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED
prompt41_replay_proof_status = APPROVED_BY_EXTERNAL_AUDIT / INTEGRATED
EXP11B_PORTABILITY_DEBT = CLOSED_BY_EXTERNAL_AUDIT / NOT_YET_INTEGRATED_AS_CLOSURE_RECORD
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Verifica además:

- `triple_comparison_status = PASS_EXACT_20_OF_20`;
- `bank_identity_mismatch_count = 0`;
- runtime evidence clasificada como `CODEX_LOCAL_RUNTIME_EVIDENCE / NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR`;
- `process_return_code = 2` preservado y clasificado no bloqueante solo para identidad gobernada;
- `failure_field = total_bank_descriptor`;
- `failure_field_is_part_of_required_14_identity_contract = false`;
- `within_historical_descriptor_tolerance = true`;
- `bank_csv_content_affected = false`;
- resolución LF/CRLF preservada;
- `retrieval_authorization_requires_separate_future_block = true`;
- `retrieval_executed = false`;
- `evaluation_metrics_computed = false`;
- `h150_h200_results_created = false`;
- `exp11b_retrieval_authorized = false`;
- `exp12_authorized = false`;
- `canonical_plan_modified = false` dentro del candidato histórico;
- `article_modified = false`.

No edites ni regeneres el closure record.

---

# 4. FASE A — Integrar closure record en main

Si el preflight pasa, integra únicamente mediante fast-forward exacto:

`7d7267f8224e56ea5e945625a7e3955ddc15eadb`

→

`09ff184854659110f7711b3eee65fc18927649da`

Reglas absolutas:

- no merge commit;
- no squash;
- no cherry-pick;
- no rebase;
- no amend;
- no force-push;
- no edición durante la integración;
- no commit adicional en `main`;
- no modificación de artefactos históricos.

Después del push verifica:

```text
origin/main = 09ff184854659110f7711b3eee65fc18927649da
```

Y que:

- el closure record exista en `main` con blob `bfbeedff9025ae928a85ab8b65a261ff475422cb`;
- el proof Prompt41 siga con blob `ab3ed6aadaaebbfc3d23c725d3ad53e9518b1ead`;
- no exista diff entre la rama candidata aprobada y `origin/main`;
- el candidato rechazado Prompt40 `799156b3c98858fbe081de73f381030426174ce1` siga sin integrar;
- no se haya ejecutado retrieval ni creado outputs H150/H200.

Si la integración no es exactamente fast-forward bit a bit: STOP y no modifiques el Plan.

Estado científico después de FASE A:

```text
EXP11B_PORTABILITY_DEBT = CLOSED / APPROVED / INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No interpretes `CLOSED` como autorización de retrieval.

---

# 5. FASE B — Reconciliación mínima del Plan Maestro

Solo si FASE A pasa, cambia a:

`docs/plan-maestro-temporal-2026-08-31`

Partiendo exactamente de:

`b814a8c2f976185209153e97e0d6ece0510526fb`

Modifica únicamente:

`docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`

No modifiques ningún otro archivo en la rama del Plan.

## 5.1 Objetivo documental exacto

El Plan debe conservar íntegramente todo el historial previo, incluido Prompt40 rechazado, Prompt41 replay proof, el return code 2 y la clasificación epistemológica runtime. No borres historia ni reescribas eventos previos como si no hubieran ocurrido.

Actualiza exclusivamente el estado vigente y el historial reciente necesario para registrar:

```text
PROMPT41_EXTERNAL_AUDIT = PASS / APPROVED_FOR_INTEGRATION
PROMPT41_REPLAY_PROOF = APPROVED / INTEGRATED_IN_MAIN
PROMPT42_EXTERNAL_GIT_AUDIT = PASS / APPROVED_FOR_INTEGRATION
EXP11B_PORTABILITY_DEBT = CLOSED / APPROVED / INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Debe constar explícitamente:

- proof Prompt41 integrado en `main` como `7d7267f8224e56ea5e945625a7e3955ddc15eadb`;
- closure record integrado en `main` como `09ff184854659110f7711b3eee65fc18927649da`;
- closure record path:
  `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_debt_external_closure_v0.1.json`;
- Prompt40 candidate `799156b...` permanece rechazado y no integrado;
- evidencia runtime Prompt41 permanece `CODEX_LOCAL_RUNTIME_EVIDENCE / NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR`;
- `process_return_code = 2` fue aceptado como no bloqueante exclusivamente para la identidad bancaria gobernada;
- el notice histórico del retrieval gate permanece inmutable y su condición de bloqueo por deuda de portabilidad quedó superada prospectivamente por el cierre aprobado;
- **retrieval requiere un bloque prospectivo separado de autorización**;
- cierre de deuda ≠ autorización de retrieval.

## 5.2 Orden maestro vigente

En el orden maestro, la secuencia vigente debe quedar conceptualmente:

```text
EXP11B Bank Materialization ✅ CLOSED / APPROVED / INTEGRATED
  ↓
EXP11B Retrieval Execution Gate ✅ APPROVED / INTEGRATED
  ↓
0B-05C ✅ CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
  ↓
EXP11B Portability Replay / Debt Closure ✅ CLOSED / APPROVED / INTEGRATED
  ↓
EXP11B Retrieval H150/H200 ⛔ NOT_AUTHORIZED / NOT_EXECUTED
  ↓
EXP12 ⛔ NOT_AUTHORIZED / NOT_EXECUTED
  ↓
Grupo 2B
```

No marques EXP11B Retrieval como ejecutado, aprobado o cerrado.

## 5.3 Próximo paso permitido

El Plan puede indicar únicamente que el próximo bloque elegible es una **autorización prospectiva separada de EXP11B Retrieval H150/H200**, sujeta a auditoría del estado integrado.

No autorices retrieval dentro del Plan en este bloque.

---

# 6. Validación de la rama del Plan antes de publicar

Antes de push verifica:

- rama parte exactamente de `b814a8c2...`;
- solo cambió `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`;
- no hay archivos adicionales;
- no se borró historial metodológico relevante;
- el estado actual dice deuda CLOSED/APPROVED/INTEGRATED;
- retrieval y EXP12 siguen NOT_AUTHORIZED / NOT_EXECUTED;
- Article continúa intacto en `254b1e6...`;
- main continúa exactamente en `09ff184...`;
- working tree tracked limpio.

Haz un único commit documental sobre la rama canónica del Plan y publícalo.

No modifiques `main` después de FASE A.

---

# 7. Prohibiciones absolutas

NO:

- integrar el candidato Prompt40 `799156b...`;
- reejecutar Prompt41;
- rematerializar bancos oficiales;
- ejecutar EXP11B Retrieval H150/H200;
- calcular métricas Top-k/MRR H150/H200;
- crear resultados H150/H200;
- autorizar retrieval;
- modificar retrieval gate config/manifest/inventory históricos;
- modificar H100/DEV/EVAL;
- modificar BM25;
- modificar Attempt06;
- modificar Article;
- modificar EXP12;
- abrir Grupo 2B;
- avanzar a Grupo 3;
- reinterpretar resultados científicos.

---

# 8. Persistencia administrativa

Después del trabajo científico/documental:

1. vuelve a `codex/prompts-temporary`;
2. haz `git fetch`;
3. no rebase/amend/force;
4. crea y publica únicamente:

`codex_prompts_tmp/43_RESPUESTA_INTEGRAR_CIERRE_PORTABILIDAD_Y_RECONCILIAR_PLAN_EXP11B.md`

La respuesta debe reportar como mínimo:

- refs iniciales y finales;
- auditoría pre-integración del closure record;
- método exacto de integración;
- main antes/después;
- compare candidata vs main post-integración;
- verificación de que Prompt40 sigue sin integrar;
- blob del proof Prompt41 y closure record en main;
- commit nuevo del Plan, parent y changed paths;
- extracto exacto del nuevo estado vigente del Plan;
- confirmación de que retrieval/metrics/EXP12/Article no fueron modificados ni ejecutados;
- working trees limpios;
- estado terminal exacto.

---

# 9. Estado terminal permitido

Si todo pasa:

```text
PROMPT43 = COMPLETED
EXP11B_PORTABILITY_DEBT = CLOSED / APPROVED / INTEGRATED
CANONICAL_PLAN = RECONCILED_WITH_PORTABILITY_CLOSURE
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
NEXT_ELIGIBLE_BLOCK = SEPARATE_PROSPECTIVE_EXP11B_RETRIEVAL_AUTHORIZATION
```

Si cualquier condición falla:

```text
PROMPT43 = STOP / INTEGRATION_OR_PLAN_RECONCILIATION_INCOMPLETE
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No avances a ningún bloque posterior.
