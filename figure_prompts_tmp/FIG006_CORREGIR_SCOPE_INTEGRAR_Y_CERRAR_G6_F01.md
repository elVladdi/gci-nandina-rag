# FIG006 — CORREGIR DERIVA DE ALCANCE, INTEGRAR Y CERRAR G6-F01

## 0. Rol y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto de tesis.

Ejecuta exclusivamente FIG006.

FIG005 produjo correctamente el candidato científico de G6-F01, pero la auditoría externa detectó una única desviación administrativa de alcance en la rama de fichas: el commit de activación `e7079755ad57033ef9cfa1a52664b47ca20125a5` añadió además una línea histórica no solicitada:

```text
FICHA = G4-F02
```

dentro del bloque histórico `## Candidato G4-F02 pendiente de auditoria externa` de `docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md`.

Esa adición no cambia ciencia, resultados ni estado vigente, pero no pertenecía al alcance autorizado de FIG005. FIG006 debe **revertir exclusivamente esa adición accidental**, preservar intacta toda la activación/postejecución de G6-F01 y, dado que el candidato científico pasó la auditoría externa, integrar y cerrar G6-F01.

FIG006 no genera figuras ni scripts y no ejecuta G6-F02.

---

## 1. Dictamen externo que gobierna FIG006

La auditoría externa de FIG005 establece:

```text
G6_F01_CANDIDATE_SCIENTIFIC_AUDIT = PASS
G6_F01_REGISTRY_CONTENT_AUDIT = PASS
G6_F01_GOVERNANCE_AUDIT = PASS_WITH_ADMINISTRATIVE_CORRECTION_REQUIRED
SCIENTIFIC_CORRECTION_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
FIGURE_REDESIGN_REQUIRED = false
ADMINISTRATIVE_CORRECTION_REQUIRED = true
```

La corrección administrativa requerida es solo:

```text
REMOVE_ACCIDENTAL_UNRELATED_LINE = "FICHA = G4-F02"
LOCATION = historical G4-F02 candidate block
INTRODUCED_BY = e7079755ad57033ef9cfa1a52664b47ca20125a5
```

No alteres ningún otro contenido histórico de G3–G5.

---

## 2. Refs rectoras

Verifica antes de modificar:

```text
PROMPTS_BRANCH = codex/prompts-temporary
FIG005_RESPONSE_COMMIT = 6b6c38e4e6ee77e630dc9febd2721d1c7816db6b

MAIN_BEFORE = ca065618d5df0019f76ef5a971e858d91c263e1f
PLAN_BEFORE = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
FICHAS_BEFORE = f5686cc7aa7ffd11ab45dc52cf258b256523abc9

G6_F01_CANDIDATE_BRANCH = figures/g6-f01-spec-registry-v01
G6_F01_CANDIDATE_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F01_CANDIDATE_PARENT = ca065618d5df0019f76ef5a971e858d91c263e1f
G6_F01_REGISTRY_BLOB = 44cc30fc3c38639c6aa4370cb6f317458041f1b1

G6_F01_ACTIVATION_COMMIT = e7079755ad57033ef9cfa1a52664b47ca20125a5
G6_F01_POSTEXEC_COMMIT = f5686cc7aa7ffd11ab45dc52cf258b256523abc9
```

STOP si `main`, Plan o fichas no coinciden exactamente con estas refs, salvo que el único cambio concurrente esté en `article/main-manuscript`, lo cual no es material para FIG006.

---

## 3. Candidato científico aprobado

El candidato:

```text
b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

debe estar exactamente:

```text
1 commit ahead
0 commits behind
```

respecto de `MAIN_BEFORE` y añadir solo:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

Debe conservar:

```text
figure_spec_count = 3
non_figure_disposition_count = 6
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
```

La auditoría externa ya verificó que consolida fielmente:

```text
G6-FIG-01 = HE2_A + HE2_B / PRIMARY_INFERENTIAL
G6-FIG-02 = Phase E / DESCRIPTIVE_SUPPLEMENTARY
G6-FIG-03 = EXP11A / DESCRIPTIVE_SENSITIVITY / NONCAUSAL
```

No modifiques el JSON candidato en FIG006.

---

## 4. Corrección administrativa en fichas

Trabaja sobre:

```text
branch = docs/fichas-grupos-3-8
base = f5686cc7aa7ffd11ab45dc52cf258b256523abc9
path = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Primero crea un commit correctivo que elimine **solo** la línea accidental:

```text
FICHA = G4-F02
```

que aparece inmediatamente bajo:

```text
## Candidato G4-F02 pendiente de auditoria externa
```

La corrección NO debe:

- borrar ni alterar el encabezado `## Candidato G4-F02 pendiente de auditoria externa`;
- cambiar ningún SHA, estado, resultado o texto de G4-F02;
- alterar otros bloques históricos;
- alterar los bloques `Activacion G6-F01` o `Postejecucion G6-F01 pendiente de auditoria externa`;
- modificar ningún otro archivo.

Registra el SHA como:

```text
G6_F01_SCOPE_CORRECTION_COMMIT
```

---

## 5. Integración a main

Después de verificar nuevamente que:

```text
origin/main = ca065618d5df0019f76ef5a971e858d91c263e1f
candidate = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
candidate ahead/behind = 1/0
```

integra el candidato mediante **fast-forward** de `main` hasta:

```text
b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

No hagas merge commit, squash, cherry-pick ni reconstrucción del JSON.

Tras la integración:

```text
MAIN_AFTER = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

Verifica que el blob integrado del registro siga siendo:

```text
44cc30fc3c38639c6aa4370cb6f317458041f1b1
```

---

## 6. Cierre operacional de G6-F01 en fichas

Sobre `docs/fichas-grupos-3-8`, después del commit correctivo, modifica únicamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Actualiza la tabla superior a:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque de cierre G6-F01 que registre al menos:

```text
FICHA = G6-F01
FIG005_PROMPT_COMMIT = 79aab9a6f63408f0fed554beb98355db5cbf404f
FIG005_RESPONSE_COMMIT = 6b6c38e4e6ee77e630dc9febd2721d1c7816db6b
ACTIVATION_COMMIT = e7079755ad57033ef9cfa1a52664b47ca20125a5
POSTEXEC_COMMIT = f5686cc7aa7ffd11ab45dc52cf258b256523abc9
SCOPE_CORRECTION_COMMIT = <G6_F01_SCOPE_CORRECTION_COMMIT>
CANDIDATE_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
CANDIDATE_PARENT = ca065618d5df0019f76ef5a971e858d91c263e1f
EXTERNAL_AUDIT = PASS_WITH_ADMINISTRATIVE_CORRECTION_COMPLETED
SCIENTIFIC_CORRECTION_REQUIRED = false
FIGURE_SPEC_COUNT = 3
NON_FIGURE_DISPOSITION_COUNT = 6
INTEGRATION_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
FINAL_G6_F01_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6 = IN_PROGRESS
G6_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
```

No actives G6-F02.

---

## 7. Reconciliación del Plan Maestro

El Plan sigue mostrando Grupo 6 como `NOT_STARTED`, por lo que después del cierre de G6-F01 debe reconciliarse.

Trabaja sobre:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Modifica únicamente lo necesario para reflejar el nuevo estado operacional:

```text
Grupo 6 = IN_PROGRESS
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F01_INTEGRATION_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6-F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
Grupo 7 = Pendiente / no autorizado
```

Preserva todo el resto del Plan Maestro. No alteres HE2, HE5, EXP11A, EXP11B, Attempt06, EXP12 ni ningún cierre previo.

Registra el commit como:

```text
PLAN_G6_F01_CLOSURE_COMMIT
```

---

## 8. Prohibiciones

FIG006 NO autoriza:

- generar figuras;
- escribir scripts Python;
- ejecutar G6-F02;
- activar G6-F02;
- ejecutar G6-F03;
- activar Grupo 7;
- modificar artículo o tesis;
- recalcular métricas, CI, p-values o inferencia;
- modificar el candidato G6-F01;
- cambiar el catálogo de tres figuras;
- reabrir EXP12;
- cambiar HE2 o HE5;
- corregir otras imperfecciones históricas no relacionadas.

---

## 9. Validaciones terminales

Antes de finalizar, verifica:

```text
MAIN_AFTER = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F01_REGISTRY_BLOB_AFTER = 44cc30fc3c38639c6aa4370cb6f317458041f1b1

G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6 = IN_PROGRESS
G6_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false

ACCIDENTAL_G4F02_LINE_PRESENT = false
SCIENTIFIC_ARTIFACT_CHANGED_DURING_CORRECTION = false
NEW_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
FIGURE_BINARY_COUNT = 0
FIGURE_SCRIPT_COUNT = 0
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
EXP12_REOPENED = false
```

---

## 10. Respuesta oficial

Persiste la respuesta en:

```text
figure_prompts_tmp/FIG006_RESPUESTA_CORREGIR_SCOPE_INTEGRAR_Y_CERRAR_G6_F01.md
```

sobre `codex/prompts-temporary`.

La respuesta debe incluir:

```text
FIG006_EXECUTION = COMPLETE / BLOCKED
G6_F01_SCOPE_CORRECTION_COMMIT = <sha>
G6_F01_CLOSURE_FICHAS_COMMIT = <sha>
PLAN_G6_F01_CLOSURE_COMMIT = <sha>
MAIN_AFTER = <sha>
FICHAS_AFTER = <sha>
PLAN_AFTER = <sha>
G6_F01_FINAL_STATE = ...
GROUP6_FINAL_STATE = ...
G6_F02_FINAL_STATE = ...
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
```

No declares G6-F02 iniciado.