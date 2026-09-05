# 0B-05C — Revisión editorial del feedback pre-ejecución D1a pendiente / Editorial review of pending D1a pre-execution feedback

## Español

### Alcance

Esta revisión registra el feedback experimental recibido tras `0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`. No ejecuta experimentos, no modifica el Plan Maestro, no altera 0A y no sustituye el snapshot experimental original.

### Dictamen

El feedback experimental se acepta como **avance parcial metodológicamente correcto, pero no como cierre de la especificación pre-ejecución**. La IA experimental se abstuvo correctamente de inferir exposición de entrenamiento o solapamiento de output sin inspección exhaustiva de los artefactos que determinan esos estados.

Se mantienen confirmados:

```text
D1A_INDEX_EXPOSURE = CONFIRMED
D1A_METRIC_IMPACT = NOT_DETERMINED
```

Permanecen abiertos:

```text
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
```

La decisión entre las políticas siguientes continúa bloqueada hasta resolver `D1A_TRAINING_EXPOSURE`:

```text
A. FREEZE_ORIGINAL_D1A_WEIGHTS + FULL_INDEX_REBUILD
B. CONTROLLED_RETRAINING + FULL_INDEX_REBUILD
```

### Regla pre-registrada aceptada

Se acepta prospectivamente, antes de observar métricas de sensibilidad, la siguiente regla de decisión:

```text
IF
    affected_code is actually consumed as a positive training target
    OR
    affected_code is actually consumed as an explicit hard-negative
    in the optimizer's training examples
THEN
    D1A_TRAINING_EXPOSURE = CONFIRMED
    MODEL_POLICY = CONTROLLED_RETRAINING
ELSE
    D1A_TRAINING_EXPOSURE = NO_EFFECTIVE_EXPOSURE_IDENTIFIED
    MODEL_POLICY = FREEZE_ORIGINAL_D1A_WEIGHTS
```

La condición `HARD_NEGATIVE_EXPOSURE = CONFIRMED` requiere trazabilidad de incorporación mediante el mecanismo explícito de selección/minería de negativos que alimentó realmente el entrenamiento. Una eventual función como negativo implícito *in-batch* bajo `MultipleNegativesRankingLoss` no debe reclasificarse retrospectivamente como hard negative explícito.

### Comprobaciones todavía obligatorias

Antes de autorizar el rerun D1a, la IA experimental debe resolver exhaustivamente y con evidencia trazable:

1. si `87044110` y/o `87045110` fueron realmente consumidos por el optimizador como targets positivos y/o hard negatives explícitos;
2. si cualquiera de esos códigos aparece en el Top-200 congelado completo de `d1a_ranked_codes_top200.jsonl`.

La segunda comprobación solo determina `D1A_RETRIEVAL_OUTPUT_OVERLAP`; una aparición en Top-200 no autoriza por sí sola reentrenamiento.

### Especificación mínima aceptada provisionalmente

Se acepta como parte ya pre-registrada de la futura sensibilidad:

- identificador: `EXP-04-D1a corrective normative-source-currency sensitivity`;
- control documental: snapshot congelado basado en Decisión 885;
- brazo corregido: estado documental corregido por Decisión 906 para el alcance material identificado;
- EVAL v0.2, `N = 1056`, sin cambio;
- profundidad Top-200, construcción de consulta, normalización/tokenización, arquitectura D1a y configuración de similitud/FAISS sin cambio;
- hiperparámetros y seeds sin cambio donde aplique;
- reconstrucción atómica del índice normativo completo y su mapping en el brazo corregido; no parcheo aislado de dos vectores;
- artefactos originales inmutables y salida en directorio específico de sensibilidad;
- interpretación exclusivamente como sensibilidad a vigencia de fuente normativa, no como reemplazo retrospectivo de EXP-04-D1a;
- reapertura downstream no automática;
- `D1A_METRIC_IMPACT = NOT_DETERMINED` hasta la ejecución.

Esta especificación permanece **parcialmente pre-registrada y no cerrada** mientras la política de pesos no pueda fijarse con la auditoría de exposición pendiente.

Antes de ejecutar, la IA experimental también debe dejar inequívoco si el brazo de control numérico reutilizará los outputs congelados o será reejecutado bajo el mismo entorno correctivo. La elección debe fijarse prospectivamente y preservar la atribución del contraste al estado documental normativo; este punto no autoriza todavía ninguna ejecución.

### Estado operativo

```text
0B05C_D1A_PREEXECUTION_FEEDBACK = ACCEPTED_AS_PARTIAL_PROGRESS

D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_MODEL_POLICY_RULE = PREREGISTERED
D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B06_0C_0D = BLOCKED
MANUSCRIPT_DRAFTING = BLOCKED
```

### Gate

`EXPERIMENTAL_REVIEW = REQUIRED`. La IA experimental debe completar las dos comprobaciones pendientes y cerrar prospectivamente la política de ejecución de EXP-04-D1a antes de cualquier sensibilidad numérica.

---

## English

### Scope

This review records the experimental feedback received after `0B05C_D1A_PREEXECUTION_SPECIFICATION_EDITORIAL_REVIEW.md`. It does not run experiments, modify the Master Plan, alter 0A, or replace the original experimental snapshot.

### Verdict

The experimental feedback is accepted as **methodologically correct partial progress, but not as closure of the pre-execution specification**. The experimental AI correctly refrained from inferring training exposure or retrieval-output overlap without exhaustive inspection of the artifacts that determine those states.

The following remain confirmed:

```text
D1A_INDEX_EXPOSURE = CONFIRMED
D1A_METRIC_IMPACT = NOT_DETERMINED
```

The following remain unresolved:

```text
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
```

The choice between these policies remains blocked until `D1A_TRAINING_EXPOSURE` is resolved:

```text
A. FREEZE_ORIGINAL_D1A_WEIGHTS + FULL_INDEX_REBUILD
B. CONTROLLED_RETRAINING + FULL_INDEX_REBUILD
```

### Accepted pre-registered rule

Before observing any sensitivity metrics, the following decision rule is accepted prospectively:

```text
IF
    affected_code is actually consumed as a positive training target
    OR
    affected_code is actually consumed as an explicit hard-negative
    in the optimizer's training examples
THEN
    D1A_TRAINING_EXPOSURE = CONFIRMED
    MODEL_POLICY = CONTROLLED_RETRAINING
ELSE
    D1A_TRAINING_EXPOSURE = NO_EFFECTIVE_EXPOSURE_IDENTIFIED
    MODEL_POLICY = FREEZE_ORIGINAL_D1A_WEIGHTS
```

`HARD_NEGATIVE_EXPOSURE = CONFIRMED` requires traceable evidence that the code was incorporated through the explicit negative-selection/mining mechanism that actually fed training. A possible implicit *in-batch* negative role under `MultipleNegativesRankingLoss` must not be retrospectively relabeled as an explicit hard negative.

### Checks still required

Before authorizing the D1a rerun, the experimental AI must exhaustively and traceably establish:

1. whether `87044110` and/or `87045110` were actually consumed by the optimizer as positive targets and/or explicit hard negatives;
2. whether either code occurs anywhere in the complete frozen Top-200 artifact `d1a_ranked_codes_top200.jsonl`.

The second check resolves only `D1A_RETRIEVAL_OUTPUT_OVERLAP`; Top-200 occurrence does not by itself authorize retraining.

### Provisionally accepted minimum specification

The following is accepted as already pre-registered for the future sensitivity:

- identifier: `EXP-04-D1a corrective normative-source-currency sensitivity`;
- documentary control: frozen Decision-885-based snapshot;
- corrected arm: Decision-906-corrected documentary state for the materially identified scope;
- unchanged EVAL v0.2, `N = 1056`;
- unchanged Top-200 depth, query construction, normalization/tokenization, D1a architecture, and similarity/FAISS configuration;
- unchanged hyperparameters and seeds where applicable;
- atomic rebuild of the complete corrected normative index and mapping, not isolated patching of two vectors;
- immutable original artifacts and a sensitivity-specific output directory;
- interpretation only as normative-source-currency sensitivity, not retrospective replacement of EXP-04-D1a;
- no automatic downstream reopening;
- `D1A_METRIC_IMPACT = NOT_DETERMINED` until execution.

The specification remains **partially pre-registered and not closed** until the weight policy can be fixed from the pending exposure audit.

Before execution, the experimental AI must also make explicit whether the numerical control arm will reuse frozen outputs or be re-executed under the same corrective environment. That choice must be fixed prospectively and preserve attribution of the contrast to normative documentary state; this point does not yet authorize execution.

### Operational state

```text
0B05C_D1A_PREEXECUTION_FEEDBACK = ACCEPTED_AS_PARTIAL_PROGRESS

D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_MODEL_POLICY_RULE = PREREGISTERED
D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B06_0C_0D = BLOCKED
MANUSCRIPT_DRAFTING = BLOCKED
```

### Gate

`EXPERIMENTAL_REVIEW = REQUIRED`. The experimental AI must complete the two pending checks and prospectively close the EXP-04-D1a execution policy before any numerical sensitivity run.