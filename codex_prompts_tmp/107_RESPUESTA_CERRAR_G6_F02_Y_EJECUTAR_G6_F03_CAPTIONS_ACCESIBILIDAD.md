# Prompt107 - Reporte terminal

```text
PROMPT107_EXECUTION = STOPPED_AT_G6_F03_ACCESSIBILITY_AUDIT
STOP_REASON = REVISION_REQUIRED_G6_F02_ARTIFACT
WORKSPACE_CONTRACT = VERIFIED / C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
ORIGIN = https://github.com/elVladdi/gci-nandina-rag.git
G6_F02_EXTERNAL_AUDIT_BINDING = PASS / SOURCE_PROMPT107
MAIN_PRE_G6F02_CLOSE = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F02_CORRECTED_CANDIDATE = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F02_INTEGRATION_METHOD = FAST_FORWARD_ONLY
G6_F02_INTEGRATION_COMMIT = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F02_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN; NEW_G6_F03_ACCESSIBILITY_FINDING_OPEN
G6_F02_CLOSURE_FICHAS_COMMIT = 484c45eaf8233617065af8d43195fa7d24814816
G6_F03_ACTIVATION_COMMIT_OR_STATE_RECORD = aa29e853b60d0d87374504a9d830a66f813f8111
G6_F03_BRANCH = figures/g6-f03-caption-closure-v01 / LOCAL_ONLY_AT_MAIN
G6_F03_CANDIDATE_COMMIT = NOT_CREATED
G6_F03_CANDIDATE_PARENT = NOT_APPLICABLE; INTENDED_BASE=71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F03_CHANGED_PATHS = NONE
G6_F03_CHANGED_PATH_COUNT = 0
CAPTION_REGISTRY_PATH = NOT_CREATED; PLANNED=docs/figures/group6/g6_caption_registry_v0.1.md
GROUP6_CLOSURE_CANDIDATE_PATH = NOT_CREATED; PLANNED=outputs/audits/group6_closure_v0.1.json
CAPTION_COUNT = 0
FIGURE_AUDIT_SUMMARY = FIG01_ACCESSIBILITY_FAIL / FIG02_FIG03_READ_ONLY_INSPECTION / AUDIT_STOPPED
ACCESSIBILITY_AUDIT_SUMMARY = REVISION_REQUIRED_G6_F02_ARTIFACT / FIG01_MIN_EFFECTIVE_FONT_BELOW_REGISTRY
GROUP5_NUMERIC_CROSSCHECK = PARTIAL_READ_ONLY / NOT_COMPLETED_AFTER_STOP
GROUP4_CLAIM_CROSSCHECK = PARTIAL_READ_ONLY / NOT_COMPLETED_AFTER_STOP
GROUP3_UNCERTAINTY_CROSSCHECK = PARTIAL_READ_ONLY / NOT_COMPLETED_AFTER_STOP
NEW_SCIENTIFIC_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
EXP12_REOPENED = false
MAIN_FINAL = 71b13caf6b97e254b4c701b23318bcb0682714bd
PLAN_FINAL = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_FINAL = 87d446197096b3b6ecf8280277637afe67d5dc29
G6_F03_FINAL_STATE = REVISION_REQUIRED_G6_F02_ARTIFACT / AUTHORIZED / NOT_EXECUTED
GROUP6_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
G7_F01_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
EXTERNAL_AUDIT = PENDING
```

## Etapa A: integracion exacta de G6-F02

Se comprobaron las referencias congeladas, el parent directo de
`71b13caf6b97e254b4c701b23318bcb0682714bd`, sus dos commits ahead y cero
behind respecto de `b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`, y los diez
paths aprobados. Se actualizo el `main` local y se integro por `git merge
--ff-only origin/figures/g6-f02-render-v01`. El push de `main` avanzo
exclusivamente de `b6404ca` a `71b13ca`. El cierre se registro y publico
en fichas antes de la activacion separada de G6-F03.

## Etapa B: activacion y hallazgo que detiene G6-F03

La activacion quedo registrada en
`aa29e853b60d0d87374504a9d830a66f813f8111`. Se creo la rama local
`figures/g6-f03-caption-closure-v01` desde `main=71b13caf...`; no contiene
commit nuevo ni fue publicada. La inspeccion read-only de las figuras y del
registry detecto un requisito de accesibilidad incumplido en la figura
aprobada G6-FIG-01:

```text
registry requirement: minimum effective font size 8 pt
FIG01 SVG viewBox width: 1000 drawing units
FIG01 SVG width: 1000 implicit CSS px
FIG01 minimum nonempty text font-size: 8.5 drawing units (comparator labels)
FIG01 PNG width: 2500 px
FIG01 PNG embedded DPI: approximately 300
FIG01 physical width: approximately 8.33335 in
FIG01 minimum effective font at PNG physical size: 8.5 / 1000 * 8.33335 * 72 = 5.10 pt
FIG01 minimum effective font at default SVG CSS size: 8.5 * 72 / 96 = 6.375 pt
result: below the mandatory 8 pt threshold in both representations
```

La medida se obtuvo leyendo `figures/group6/g6_fig_01_he2.svg` y el DPI
embebido en `figures/group6/g6_fig_01_he2.png`; no se regenero la figura.
Los labels de comparadores de Panel B materializan el tamano minimo. El
problema requiere editar el render/script de G6-F02, precisamente el caso
para el cual la seccion 8 de Prompt107 ordena `STOP` y
`REVISION_REQUIRED_G6_F02_ARTIFACT`.

Como control contextual, G6-FIG-03 mide 8.70 pt minimos al tamano fisico
del PNG y satisface su umbral 8.5 pt; G6-FIG-02 conserva el titulo del eje y
externo al campo de datos a 10.20 pt. Otros textos de FIG02 miden 5.40 pt
fisicos frente a 9 pt recomendados por el registry; no fue necesario
resolver si esa recomendacion es bloqueante porque FIG01 ya activa la orden
de detenerse. La inspeccion visual de los tres PNG no modifica el umbral
cuantitativo obligatorio de FIG01.

El ledger de G6-F02 mantuvo 16/16 coincidencias de SHA-256 y tamano contra
bytes Git canonicos. Los archivos de Grupo 5 inspeccionados contienen 15
filas HE2_A, una fila HE2_B, 15 filas Phase E y 37 filas EXP11A (31 corridas
observadas y seis summaries congelados). Se leyeron los contratos de claims
de Grupo 4 y de incertidumbre de Grupo 3. La auditoria completa de captions,
los crosschecks finales y ambos outputs de G6-F03 se detuvieron ante el
hallazgo; no se reportan como aprobados.

## Estado y alcance

El registro de fichas documenta el bloqueo en
`87d446197096b3b6ecf8280277637afe67d5dc29`. No se edito ninguna figura,
script, ledger, tabla, fuente cientifica, Plan Maestro, tesis ni articulo.
No se calculo ninguna metrica, inferencia, CI o p-value; no se reabrio EXP12.
G6-F03 no produjo candidato y Grupo 6 permanece abierto. G7-F01 no fue
autorizado. Los tres untracked preexistentes del workspace se preservaron.

PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
