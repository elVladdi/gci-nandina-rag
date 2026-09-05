# 0B-05C — Precisión editorial de especificación pre-ejecución D1a / Editorial precision of the D1a pre-execution specification

## Español

### Alcance

Esta revisión registra el segundo feedback experimental sobre la corrección editorial del gate 0B-05C. No ejecuta experimentos, no modifica el Plan Maestro, no altera 0A y no sustituye el snapshot experimental original.

### Dictamen sobre el feedback experimental

Se acepta el dictamen experimental de que la actualización de la rama del artículo es sustantivamente correcta y que la incorporación de D1a fue una corrección material válida. La precisión pendiente no revierte esa corrección; la descompone en estados de exposición distintos que deben resolverse **antes de cualquier reejecución numérica**.

Para trazabilidad se normaliza la nomenclatura:

`EV-05 (identificador editorial del gate) ≡ EXP-04-D1a (identificador experimental canónico)`.

El estado D1a queda desagregado así:

```text
D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_EXECUTION_SPECIFICATION = PENDING
```

`D1A_INDEX_EXPOSURE = CONFIRMED` significa únicamente que el índice denso se construyó desde el corpus normativo afectado por el drift. No autoriza inferir por sí solo exposición efectiva del fine-tuning, aparición de los códigos afectados en los rankings D1a ni impacto sobre Top-k/MRR.

Antes del rerun, la IA experimental debe verificar de forma trazable si `87044110` y/o `87045110` participaron efectivamente en el fine-tuning —como positivos y/o hard negatives— y si aparecen en `d1a_ranked_codes_top200.jsonl`. Esa evidencia debe fijar prospectivamente la especificación de sensibilidad:

- si no existe exposición efectiva del entrenamiento, puede evaluarse una sensibilidad con pesos congelados y reconstrucción del índice normativo corregido;
- si se confirma exposición efectiva del entrenamiento, la IA experimental debe decidir antes de observar métricas si corresponde incluir reentrenamiento controlado.

No es metodológicamente admisible actualizar solo el corpus textual y reutilizar silenciosamente un índice denso construido sobre las representaciones anteriores.

### Estado operativo

La formulación previa `CORRECTIVE_GATE_SCOPING = INCOMPLETE` queda refinada operacionalmente por `D1A_EXECUTION_SPECIFICATION = PENDING`; el registro histórico de la revisión previa se preserva.

```text
0B05C_CORRECTIVE_EXPERIMENTAL_REVIEW = SUBSTANTIVELY_APPROVED_WITH_EXECUTION_SPECIFICATION_PENDING

SOURCE_VERSION_DRIFT = PRESENT
CHAPTER_87_SCOPE_OVERLAP = CONFIRMED
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED

D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_EXECUTION_SPECIFICATION = PENDING

CORRECTIVE_NUMERICAL_RERUN = REQUIRED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B06_0C_0D = BLOCKED
MANUSCRIPT_DRAFTING = BLOCKED
```

La reapertura downstream continúa condicionada a propagación demostrada. No existe base nueva para reconstruir splits, labels, banco histórico o ranking histórico.

### Gate

`EXPERIMENTAL_REVIEW = REQUIRED`. La siguiente acción no es todavía ejecutar la sensibilidad numérica, sino cerrar primero la especificación pre-ejecución de EXP-04-D1a mediante auditoría de exposición de entrenamiento y output.

---

## English

### Scope

This review records the second experimental feedback on the editorial correction of the 0B-05C gate. It does not run experiments, modify the Master Plan, alter 0A, or replace the original experimental snapshot.

### Verdict on the experimental feedback

The experimental verdict that the article-branch update is substantively correct and that adding D1a was a valid material correction is accepted. The remaining precision does not reverse that correction; it decomposes D1a into distinct exposure states that must be resolved **before any numerical re-execution**.

For traceability, nomenclature is normalized as follows:

`EV-05 (editorial gate identifier) ≡ EXP-04-D1a (canonical experimental identifier)`.

D1a is now separated into these states:

```text
D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_EXECUTION_SPECIFICATION = PENDING
```

`D1A_INDEX_EXPOSURE = CONFIRMED` means only that the dense index was built from the normative corpus exposed to the identified drift. It does not by itself establish effective fine-tuning exposure, occurrence of the affected codes in D1a rankings, or Top-k/MRR impact.

Before rerunning, the experimental AI must traceably determine whether `87044110` and/or `87045110` actually participated in fine-tuning—as positives and/or hard negatives—and whether they occur in `d1a_ranked_codes_top200.jsonl`. That evidence must prospectively fix the sensitivity specification:

- if no effective training exposure is found, a sensitivity with frozen model weights and a rebuilt corrected normative index may be evaluated;
- if effective training exposure is confirmed, the experimental AI must decide before observing metrics whether controlled retraining belongs in the sensitivity.

It is not methodologically acceptable to update only the text corpus while silently reusing a dense index built from the previous representations.

### Operational state

The previous broad formulation `CORRECTIVE_GATE_SCOPING = INCOMPLETE` is operationally refined by `D1A_EXECUTION_SPECIFICATION = PENDING`; the historical record of the prior review is preserved.

```text
0B05C_CORRECTIVE_EXPERIMENTAL_REVIEW = SUBSTANTIVELY_APPROVED_WITH_EXECUTION_SPECIFICATION_PENDING

SOURCE_VERSION_DRIFT = PRESENT
CHAPTER_87_SCOPE_OVERLAP = CONFIRMED
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED

D1A_INDEX_EXPOSURE = CONFIRMED
D1A_TRAINING_EXPOSURE = NOT_DETERMINED
D1A_RETRIEVAL_OUTPUT_OVERLAP = NOT_VERIFIED
D1A_METRIC_IMPACT = NOT_DETERMINED
D1A_EXECUTION_SPECIFICATION = PENDING

CORRECTIVE_NUMERICAL_RERUN = REQUIRED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0B05C = NOT_AUTHORIZED
0B06_0C_0D = BLOCKED
MANUSCRIPT_DRAFTING = BLOCKED
```

Downstream reopening remains conditional on demonstrated propagation. There is no new basis to rebuild splits, labels, the historical bank, or the historical ranking.

### Gate

`EXPERIMENTAL_REVIEW = REQUIRED`. The next action is not yet to execute the numerical sensitivity; it is first to close the EXP-04-D1a pre-execution specification through training-exposure and retrieval-output auditing.
