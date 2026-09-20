# PROMPT 86 — INTEGRAR G3-F04 Y CERRAR CANÓNICAMENTE GRUPO 3 TRAS AUDITORÍA EXTERNA

## 0. Naturaleza y límite

Esta es una ejecución **administrativa de integración y cierre**. La IA Experimental auditó externamente el candidato G3-F04 producido por Prompt85 y el dictamen es:

```text
G3_F04_EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
GROUP3_CLOSURE_AUTHORIZABLE = true
G4_F01_AUTHORIZED = false
```

No debes recalcular inferencia, métricas, intervalos ni decisiones. Debes integrar exactamente el candidato auditado, reconciliar Plan Maestro y registro de fichas, cerrar Grupo 3 y dejar G4-F01 únicamente `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`.

---

## 1. Refs congelados de entrada

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de modificar nada, ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 7d09f692da23367d3aba941db1febdca2baa8917
origin/docs/plan-maestro-temporal-2026-08-31 = 96cccb9a61f42ab97b1eba607524e33f992740f6
origin/docs/fichas-grupos-3-8 = d82e1d6df2d7ed500696ff69e08ed30f29ef9713
origin/codex/group3-f04-hypothesis-disposition-v01 = 09278a10063a1e175ee2991b60f7649dd2ee40f4
```

Gobernanza relacionada:

```text
PROMPT85_COMMIT = f132ea01d45661656fe606bb83ac76efda24a496
PROMPT85_RESPONSE_COMMIT = a57c1d97648f884d866d62acd3329a01b5c0158b
G3_F04_ACTIVATION_COMMIT = cac6a8bdbd5c763611836203e33a4a29648fbf4c
G3_F04_POSTEXEC_FICHAS_COMMIT = d82e1d6df2d7ed500696ff69e08ed30f29ef9713
```

Artículo observado al versionar Prompt86:

```text
origin/article/main-manuscript = 6b32f09b4c4b7cc97eea164b122739f6d8d02184
```

El artículo es solo observacional y no es input científico. Si avanza concurrentemente, regístralo como warning siempre que Prompt86 no lo modifique.

Si `main`, Plan, fichas o la rama candidata presentan drift científico/gobernanza no explicado:

```text
STOP / REF_DRIFT_DETECTED
```

---

## 2. Candidato G3-F04 auditado

Candidato exacto:

```text
branch = codex/group3-f04-hypothesis-disposition-v01
commit = 09278a10063a1e175ee2991b60f7649dd2ee40f4
parent = 7d09f692da23367d3aba941db1febdca2baa8917
commits_ahead = 1
commits_behind = 0
changed_path_count = 3
```

Únicos paths permitidos:

```text
docs/analysis/group3/g3_claim_registry_v0.1.md
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
outputs/audits/group3_closure_v0.1.json
```

Blobs auditados que deben permanecer exactos:

```text
CLAIM_REGISTRY_BLOB = f3f6594277bfeede555f10887bcdb922efd23680
HYPOTHESIS_DISPOSITION_BLOB = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61
GROUP3_CLOSURE_CANDIDATE_BLOB = 17790b1f0d390ebf13672c7f7f63343493aaf7a5
```

Verifica sin recalcular que el contenido preserve exactamente:

```text
HE2_A_DISPOSITION = SUPPORTED_BY_PRIMARY_EVIDENCE
HE2_B_HIERARCHICAL_DISPOSITION = SUPPORTED_BY_PRIMARY_EVIDENCE
HE2_B_PHASE_E_DESCRIPTIVE_DISPOSITION = DIRECTIONALLY_CONSISTENT_DESCRIPTIVE
HE2_OVERALL_DISPOSITION = SUPPORTED

HE5_DESCRIPTION_COMPONENT = NOT_ESTIMABLE
HE5_HIERARCHY_COMPONENT = DESCRIPTIVE_ONLY
HE5_PRECEDENT_COMPONENT = DESCRIPTIVE_ONLY / NO_FROZEN_INSUFFICIENCY_THRESHOLD
HE5_INTERNAL_VALIDITY_COMPONENT = DOCUMENTED_LIMITATION
HE5_OVERALL_DISPOSITION = INCONCLUSIVE

NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
G4_F01_AUTHORIZED = false
```

La auditoría externa verificó además que:

- los 15 contrastes primarios HE2_A tienen `ci_lower > 0` bajo las tres familias Bonferroni congeladas;
- `G3F03-0016` (`Recall@200 - Recall@100`) tiene CI95% completamente mayor que 0;
- las cuatro variantes Phase E `A_historical_defined` presentan descriptivamente `Pool@50 < Pool@100 < Pool@200`;
- HE5 no es forzada a una decisión favorable: descripción no operacionalizada, jerarquía solo descriptiva y ausencia de umbral congelado para “precedentes insuficientes” conducen a `INCONCLUSIVE`;
- EXP12 permanece `NOT_ESTIMABLE / CLOSED_WITHOUT_RETRIEVAL` y no forma un nuevo contraste;
- el claim registry conserva las barreras de sobreinterpretación sobre causalidad, validez externa, exactitud global del RAG y corrección jurídica.

Si cualquier blob, path, parent, conteo o disposición difiere:

```text
STOP / AUDITED_CANDIDATE_MISMATCH
```

---

## 3. Prohibiciones absolutas

Durante Prompt86 está prohibido:

- modificar cualquiera de los 3 artefactos científicos G3-F04;
- modificar artefactos científicos G3-F01/F02/F03;
- recalcular bootstrap, CI, métricas o p-values;
- cambiar HE2=`SUPPORTED` o HE5=`INCONCLUSIVE`;
- crear nuevos claims científicos;
- reabrir EXP12;
- reejecutar retrieval/BM25/dense retrieval;
- modificar `article/main-manuscript`;
- ejecutar o activar G4-F01;
- hacer force-push, squash, rebase o amend del commit científico auditado.

---

## 4. Integración exacta a main

Integra el candidato mediante **fast-forward only**.

Resultado obligatorio:

```text
origin/main = 09278a10063a1e175ee2991b60f7649dd2ee40f4
```

No debe aparecer merge commit nuevo.

Después del fast-forward vuelve a verificar los tres blobs de la sección 2.

Si no es posible el fast-forward exacto:

```text
STOP / MAIN_FAST_FORWARD_NOT_POSSIBLE
```

---

## 5. Reconciliación del Plan Maestro

Trabaja exclusivamente sobre:

```text
branch = docs/plan-maestro-temporal-2026-08-31
file = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Partiendo exactamente de:

```text
96cccb9a61f42ab97b1eba607524e33f992740f6
```

Actualiza el estado canónico para dejar, como mínimo:

```text
GROUP3 = CLOSED / APPROVED
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04_INTEGRATION_COMMIT = 09278a10063a1e175ee2991b60f7649dd2ee40f4

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
STATISTICAL_INFERENCE_EXECUTED = true
P_VALUES_CALCULATED = false
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED

NEXT_ELIGIBLE_FICHA = G4-F01
G4_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque de cierre de Grupo 3 que documente:

```text
G3_F04_EXTERNAL_AUDIT = PASS
G3_F04_CANDIDATE_COMMIT = 09278a10063a1e175ee2991b60f7649dd2ee40f4
G3_F04_CHANGED_PATH_COUNT = 3
HE2_A_DISPOSITION = SUPPORTED_BY_PRIMARY_EVIDENCE
HE2_B_HIERARCHICAL_DISPOSITION = SUPPORTED_BY_PRIMARY_EVIDENCE
HE2_B_PHASE_E_DESCRIPTIVE_DISPOSITION = DIRECTIONALLY_CONSISTENT_DESCRIPTIVE
HE2_OVERALL_DISPOSITION = SUPPORTED
HE5_DESCRIPTION_COMPONENT = NOT_ESTIMABLE
HE5_HIERARCHY_COMPONENT = DESCRIPTIVE_ONLY
HE5_PRECEDENT_COMPONENT = DESCRIPTIVE_ONLY / NO_FROZEN_INSUFFICIENCY_THRESHOLD
HE5_INTERNAL_VALIDITY_COMPONENT = DOCUMENTED_LIMITATION
HE5_OVERALL_DISPOSITION = INCONCLUSIVE
NEW_INFERENCE_PERFORMED_BY_G3_F04 = false
GROUP3_FINAL_STATE = CLOSED / APPROVED
G4_F01_AUTHORIZED = false
```

Preserva todas las limitaciones históricas/canónicas ya existentes de Grupo 2B, EXP12, 0B-05C y EXP11A/B. No simplifiques ni borres historial previo.

Haz un único commit del Plan y push normal.

---

## 6. Cierre en registro de fichas

Trabaja exclusivamente sobre:

```text
branch = docs/fichas-grupos-3-8
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Partiendo exactamente de:

```text
d82e1d6df2d7ed500696ff69e08ed30f29ef9713
```

Actualiza:

```text
G3-F04 = CLOSED / APPROVED
G4-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque de cierre con:

```text
FICHA = G3-F04
ACTIVATION_COMMIT = cac6a8bdbd5c763611836203e33a4a29648fbf4c
PROMPT85_COMMIT = f132ea01d45661656fe606bb83ac76efda24a496
PROMPT85_RESPONSE_COMMIT = a57c1d97648f884d866d62acd3329a01b5c0158b
CANDIDATE_COMMIT = 09278a10063a1e175ee2991b60f7649dd2ee40f4
CANDIDATE_PARENT = 7d09f692da23367d3aba941db1febdca2baa8917
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
INTEGRATION_COMMIT = 09278a10063a1e175ee2991b60f7649dd2ee40f4
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
FINAL_G3_F04_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP3 = CLOSED / APPROVED
G4_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Haz un único commit y push normal.

---

## 7. Validación terminal

Al finalizar verifica:

```text
MAIN_FINAL = 09278a10063a1e175ee2991b60f7649dd2ee40f4
CLAIM_REGISTRY_BLOB_FINAL = f3f6594277bfeede555f10887bcdb922efd23680
HYPOTHESIS_DISPOSITION_BLOB_FINAL = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61
GROUP3_CLOSURE_BLOB_FINAL = 17790b1f0d390ebf13672c7f7f63343493aaf7a5

GROUP3 = CLOSED / APPROVED
G3_F04 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
G4_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F01_STARTED = false

SCIENTIFIC_ARTIFACTS_MODIFIED = false
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
```

Si cualquiera falla:

```text
STOP / GROUP3_CLOSURE_VALIDATION_FAILURE
```

---

## 8. Respuesta administrativa

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/86_RESPUESTA_INTEGRAR_Y_CERRAR_GRUPO3_TRAS_AUDITORIA_EXTERNA_G3_F04.md
```

La respuesta debe reportar al menos:

```text
PROMPT86 = COMPLETED | STOPPED
PREFLIGHT_MAIN = ...
PREFLIGHT_PLAN = ...
PREFLIGHT_FICHAS = ...
ARTICLE_HEAD_OBSERVED = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...
ARTICLE_MODIFIED_BY_PROMPT86 = false

G3_F04_CANDIDATE_COMMIT = 09278a10063a1e175ee2991b60f7649dd2ee40f4
MAIN_FINAL = ...
CLAIM_REGISTRY_BLOB_FINAL = ...
HYPOTHESIS_DISPOSITION_BLOB_FINAL = ...
GROUP3_CLOSURE_BLOB_FINAL = ...
PLAN_CLOSURE_COMMIT = ...
FICHAS_CLOSURE_COMMIT = ...

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP3_FINAL_STATE = CLOSED / APPROVED
G4_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F01_STARTED = false

SCIENTIFIC_ARTIFACTS_MODIFIED = false
NEW_INFERENCE_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
BLOCKERS = ...
WARNINGS = ...
```

Commit y push únicamente ese archivo administrativo en la rama de prompts.
