# 0B-05C — Normalización de gobernanza previa a la auditoría D1a / Governance normalization before the D1a exposure audit

## Español

### Alcance

Esta revisión audita el feedback experimental recibido sobre el HEAD `3f279fe8cf770c8b6bb1d35a7566c92459801a38`. No ejecuta experimentos, no modifica el Plan Maestro, no altera 0A y no sustituye el snapshot experimental original.

### Dictamen

`PASS WITH CORRECTIONS`.

El feedback experimental es sustantivamente correcto. Se acepta que el estado científico de D1a continúa abierto y que no corresponde ejecutar todavía la sensibilidad numérica. También se acepta que la gobernanza editorial debe normalizarse antes del siguiente paso experimental.

### Correcciones de gobernanza verificadas

1. `article/START_HERE.md` limita los estados operativos formales a `NOT_STARTED`, `IN_ANALYSIS`, `READY_FOR_DRAFTING`, `DRAFTING`, `INTERNAL_REVIEW`, `EXPERIMENTAL_REVIEW`, `REVISION_REQUIRED`, `APPROVED`, `FROZEN` y `BLOCKED`. Por tanto, `CORRECTIVE_PREEXECUTION_SPECIFICATION_PENDING / CORRECTIVE_NUMERICAL_RERUN_REQUIRED` no debe funcionar como estado operativo formal de 0B-05C; debe mantenerse como subestado/flags del gate.

2. `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md` conserva `0B-05C = READY_FOR_DRAFTING`, que describe el estado inicial del sublote pero ya no el estado vigente. Debe preservarse históricamente como estado inicial y remitirse a `ARTICLE_STATUS.md` para el estado operativo actual.

3. `ARTICLE_STATUS.md` debe incorporar `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md` y esta revisión en la lista de revisiones gobernantes del gate actual.

### Estado operativo normalizado

```text
0B-05C_OPERATIONAL_STATUS = EXPERIMENTAL_REVIEW

D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED

D1A_MODEL_POLICY_RULE = PREREGISTERED
D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
CORRECTIVE_NUMERICAL_RERUN = REQUIRED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B06_0C_0D = BLOCKED
MANUSCRIPT_DRAFTING = BLOCKED
```

### Precisión de evidencia para cerrar la especificación D1a

Antes de autorizar cualquier rerun D1a, la IA experimental debe resolver exhaustivamente:

1. `D1A_TRAINING_EXPOSURE`: la evidencia debe provenir del artefacto de entrenamiento **efectivamente consumido por el optimizador** y quedar vinculada por hash y/o run metadata. La mera presencia de los códigos en el corpus, scripts de construcción o pools candidatos no demuestra exposición efectiva. Debe distinguirse target positivo de hard negative explícitamente seleccionado/minado. Una eventual función como negativo implícito *in-batch* bajo MNRL no debe reclasificarse como hard negative explícito.

2. `D1A_RETRIEVAL_OUTPUT_OVERLAP`: la inspección del Top-200 congelado completo debe registrar, para cada aparición de `87044110` o `87045110`, como mínimo código, `case_id`, rank y número total de ocurrencias. El resultado no debe reducirse únicamente a un booleano.

La aparición en Top-200 resuelve overlap de output, no training exposure ni metric impact.

### Política del brazo control

Se acepta como recomendación metodológica prospectiva para que la IA experimental la cierre explícitamente antes de ejecutar:

```text
PRIMARY_CONTROL = FROZEN_ORIGINAL_D1A_OUTPUTS_FROM_DECISION_885_SNAPSHOT

OPTIONAL_CONTROL_REPRODUCTION =
    REPRODUCIBILITY_CHECK_ONLY;
    MUST_REPRODUCE_FROZEN_CONTROL_BEFORE_ANALYTICAL_USE
```

La finalidad es mantener como control primario el resultado experimental realmente congelado y evitar que una nueva ejecución introduzca variación ambiental o de entrenamiento ajena al factor documental 885→906. Esta revisión editorial registra la recomendación; la especificación experimental final sigue siendo competencia de la IA experimental.

### Gate

`EXPERIMENTAL_REVIEW = REQUIRED`. El siguiente paso continúa siendo resolver la exposición efectiva de entrenamiento y output de EXP-04-D1a y cerrar prospectivamente su especificación de ejecución. No se autoriza todavía ninguna sensibilidad numérica.

---

## English

### Scope

This review audits the experimental feedback received for HEAD `3f279fe8cf770c8b6bb1d35a7566c92459801a38`. It does not run experiments, modify the Master Plan, alter 0A, or replace the original experimental snapshot.

### Verdict

`PASS WITH CORRECTIONS`.

The experimental feedback is substantively correct. The scientific state of D1a remains open, and the numerical sensitivity must not yet be executed. Editorial governance must also be normalized before the next experimental step.

### Verified governance corrections

1. `article/START_HERE.md` restricts formal operational states to `NOT_STARTED`, `IN_ANALYSIS`, `READY_FOR_DRAFTING`, `DRAFTING`, `INTERNAL_REVIEW`, `EXPERIMENTAL_REVIEW`, `REVISION_REQUIRED`, `APPROVED`, `FROZEN`, and `BLOCKED`. Therefore, `CORRECTIVE_PREEXECUTION_SPECIFICATION_PENDING / CORRECTIVE_NUMERICAL_RERUN_REQUIRED` must not function as the formal operational state of 0B-05C; it must remain a gate substate/flag set.

2. `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md` still records `0B-05C = READY_FOR_DRAFTING`. That describes the initial sub-batch state but no longer the current state. It must be preserved historically as the initial state and defer to `ARTICLE_STATUS.md` for the current operational state.

3. `ARTICLE_STATUS.md` must include `article/reviews/0B05C_D1A_PREEXECUTION_AUDIT_PENDING_EDITORIAL_REVIEW.md` and this review in the list of governing reviews for the current gate.

### Normalized operational state

```text
0B-05C_OPERATIONAL_STATUS = EXPERIMENTAL_REVIEW

D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED

D1A_MODEL_POLICY_RULE = PREREGISTERED
D1A_EXECUTION_SPECIFICATION = PARTIALLY_PREREGISTERED / NOT_CLOSED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
CORRECTIVE_NUMERICAL_RERUN = REQUIRED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B06_0C_0D = BLOCKED
MANUSCRIPT_DRAFTING = BLOCKED
```

### Evidence precision required to close the D1a specification

Before any D1a rerun can be authorized, the experimental AI must exhaustively resolve:

1. `D1A_TRAINING_EXPOSURE`: evidence must come from the training artifact **actually consumed by the optimizer** and be tied to hash and/or run metadata. Mere occurrence of the codes in the corpus, construction scripts, or candidate pools does not establish effective exposure. Positive targets must be distinguished from explicitly selected/mined hard negatives. A possible implicit *in-batch* negative role under MNRL must not be relabeled as an explicit hard negative.

2. `D1A_RETRIEVAL_OUTPUT_OVERLAP`: inspection of the complete frozen Top-200 must record, for every occurrence of `87044110` or `87045110`, at least the code, `case_id`, rank, and total number of occurrences. The result must not be reduced to a boolean only.

Top-200 occurrence resolves output overlap, not training exposure or metric impact.

### Control-arm policy

The following is accepted as a prospective methodological recommendation for explicit closure by the experimental AI before execution:

```text
PRIMARY_CONTROL = FROZEN_ORIGINAL_D1A_OUTPUTS_FROM_DECISION_885_SNAPSHOT

OPTIONAL_CONTROL_REPRODUCTION =
    REPRODUCIBILITY_CHECK_ONLY;
    MUST_REPRODUCE_FROZEN_CONTROL_BEFORE_ANALYTICAL_USE
```

The purpose is to keep the actually frozen experimental result as the primary control and prevent a new run from introducing environmental or training variation unrelated to the 885→906 documentary factor. This editorial review records the recommendation; final experimental specification remains under the experimental AI's authority.

### Gate

`EXPERIMENTAL_REVIEW = REQUIRED`. The next step remains to resolve effective EXP-04-D1a training/output exposure and prospectively close its execution specification. No numerical sensitivity is authorized yet.