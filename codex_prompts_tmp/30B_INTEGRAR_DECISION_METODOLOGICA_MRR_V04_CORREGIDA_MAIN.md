# PROMPT 30B — INTEGRAR DECISIÓN METODOLÓGICA MRR v0.4 CORREGIDA A `main`

## Rol

Actúa como **ejecutor técnico controlado de integración**. La IA Experimental auditó externamente el candidato corregido producido por Prompt30A y lo aprobó para integración.

Este bloque autoriza **exclusivamente** integrar por fast-forward el objeto científico ya auditado. No debes modificar su contenido, construir código v0.4 ni autorizar Attempt05.

---

## 1. Repositorio y baseline obligatorio

Repositorio:

`elVladdi/gci-nandina-rag`

Antes de cualquier cambio ejecuta `git fetch --all --prune` y verifica:

- `origin/main = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`;
- rama candidata: `codex/0b05c-ev04-mrr-methodological-decision-v04-corrected`;
- head remoto candidato = `ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`;
- parent del candidato = `ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`;
- tree candidato = `ef6145872ac02da8b750c219b0708e679a9a5b7e`;
- merge-base candidato/main = `ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`;
- candidato = 1 commit ahead / 0 behind respecto al baseline;
- rama rechazada Prompt30 permanece exactamente en `0298a6a51181ba992e981063be87a9742ba266ef`;
- Plan canónico = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- working tree tracked de `main` limpio.

Si cualquiera falla: **STOP / FAIL_CLOSED**. No integres nada.

---

## 2. Identidad exacta del candidato aprobado

El compare baseline→candidato debe contener exactamente:

- 1 commit;
- 1 changed path;
- ningún otro cambio.

Único path autorizado:

`outputs/audits/0b05c_ev04_mrr_methodological_decision_v0.4/mrr_methodological_decision_v0.4.json`

Git blob SHA-1 esperado:

`26b4310979e042bc7bb4fa0594d1ef450bf0032e`

El artefacto debe conservar, sin edición:

- `artifact_id = 0b05c_ev04_mrr_methodological_decision_v0.4`;
- `decision_status = CANDIDATE_PENDING_EXTERNAL_AUDIT` como estado serializado del objeto candidato originalmente auditado;
- `corrects_rejected_candidate_commit = 0298a6a51181ba992e981063be87a9742ba266ef`;
- `external_audit_finding = MRR200_CONTRACT_COLLATERAL_DRIFT`;
- `.77` = literal histórico inmutable, no oracle prospectivo;
- `.78` = referencia prospectiva case-derived para MRR@100;
- `MRR200_ROLE = STABLE_LEGACY_CONTRACT / ENRICHED_ALIAS_OF_LEGACY_MRR`;
- `mrr_at_200_equals_legacy_mrr_required = true`;
- `mrr_at_200_rational_ratio_redefinition_forbidden = true`;
- contribución 101–200 prospectiva derivada por diferencia racional exacta;
- `PASS_EXACT` obligatorio y sin tolerancias;
- `v04_build_authorized = false`;
- `attempt05_authorized = false`;
- `metric_impact = NOT_DETERMINED`;
- `closure = NOT_AUTHORIZED`.

No actualices `decision_status` durante esta integración. La aprobación externa se registra en el reporte de integración y en el estado científico de gobernanza; el objeto científico auditado debe conservar identidad exacta.

---

## 3. Integración autorizada

Si y solo si todo el preflight pasa:

1. sitúate en `main` exactamente en `ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`;
2. integra exclusivamente:
   `origin/codex/0b05c-ev04-mrr-methodological-decision-v04-corrected`;
3. usa **solo** fast-forward (`git merge --ff-only ...`);
4. publica `main` con push normal.

Queda prohibido:

- merge commit;
- squash;
- cherry-pick;
- rebase;
- amend;
- force-push;
- editar archivos durante la integración;
- crear un commit adicional en `main`.

El `main` final debe ser exactamente:

`ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

con tree exacto:

`ef6145872ac02da8b750c219b0708e679a9a5b7e`.

---

## 4. Verificación post-integración obligatoria

Después del push verifica read-only:

- `main = origin/main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`;
- candidato remoto = el mismo SHA;
- tree de `main` = tree candidato exacto;
- diff candidato vs `origin/main` vacío;
- baseline anterior queda 1 commit detrás del nuevo `main`;
- la integración contiene exactamente el único path autorizado;
- blob integrado = `26b4310979e042bc7bb4fa0594d1ef450bf0032e`;
- rama Prompt30 rechazada sigue en `0298a6a51181ba992e981063be87a9742ba266ef`;
- Plan sigue en `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article sigue en `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- working tree tracked limpio.

No ejecutes la comprobación racional nuevamente. No ejecutes tests si hacerlo implica generar o modificar outputs científicos.

---

## 5. Prohibiciones absolutas

No debes:

- modificar el artefacto integrado;
- modificar el candidato Prompt30 rechazado;
- construir código v0.4;
- construir gate/specs v0.4;
- crear una autorización v0.4;
- autorizar o ejecutar Attempt05;
- ejecutar retrieval;
- ejecutar EV03 o EV04 real;
- ejecutar D1a;
- ejecutar EVAL real;
- ejecutar inferencia del modelo;
- modificar productor v0.3;
- modificar tests históricos;
- modificar artefactos históricos;
- tocar Plan Maestro;
- tocar article;
- tocar EXP11B o EXP12;
- determinar impacto métrico;
- autorizar cierre 0B05C.

---

## 6. Estado científico post-integración

Si la integración pasa, reporta separadamente:

```text
INTEGRATION_AUDIT_LOCAL = PASS
CORRECTED_METHODOLOGICAL_DECISION = APPROVED_BY_EXTERNAL_AUDIT / VERSIONED / INTEGRATED
DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE
MRR200_ROLE = STABLE_LEGACY_CONTRACT / ENRICHED_ALIAS_OF_LEGACY_MRR
V04_BUILD = NOT_AUTHORIZED / NOT_BUILT
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```

No declares que v0.4 esté construido o autorizado.

---

## 7. Persistencia administrativa obligatoria

Después de finalizar la integración científica, cambia a:

`codex/prompts-temporary`

Ejecuta `git fetch` antes de persistir la respuesta. No rebase, no amend, no force-push.

Crea exclusivamente:

`codex_prompts_tmp/30B_RESPUESTA_INTEGRAR_DECISION_METODOLOGICA_MRR_V04_CORREGIDA_MAIN.md`

El reporte debe contener:

1. preflight exacto;
2. identidad branch/commit/tree/parent del candidato;
3. compare baseline→candidate;
4. path y blob SHA-1 exactos;
5. método exacto de integración;
6. estado `main` antes y después;
7. verificación post-integración;
8. confirmación de que Prompt30 rechazado, Plan y article permanecen intactos;
9. prohibiciones preservadas;
10. estado científico final.

El commit administrativo debe modificar exclusivamente ese archivo de respuesta.

Responde únicamente con el reporte final exigido.
