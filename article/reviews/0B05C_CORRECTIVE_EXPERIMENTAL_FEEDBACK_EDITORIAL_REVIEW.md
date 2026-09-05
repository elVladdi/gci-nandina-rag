# 0B-05C — Revisión editorial del corrective experimental gate / Editorial review of the corrective experimental gate

## Español

### Alcance

Revisión editorial independiente del feedback experimental que mantiene `0B-05C_CORRECTIVE_EXPERIMENTAL_GATE = OPEN — BOUNDED NUMERICAL REEXECUTION REQUIRED`. Esta revisión no ejecuta experimentos, no modifica el Plan Maestro y no altera artefactos experimentales congelados.

### Hallazgos aceptados

Se aceptan como sustentados para este gate:

- `SOURCE_VERSION_DRIFT = PRESENT`;
- `CHAPTER_87_SCOPE_OVERLAP = CONFIRMED`;
- los códigos NANDINA-8 materialmente identificados para este drift son `87044110` y `87045110`;
- el drift identificado modifica su representación textual normativa, no sus identificadores NANDINA-8;
- `EVAL_LABEL_IMPACT = NOT_OBSERVED`;
- `HISTORICAL_RANKING_IMPACT = NOT_OBSERVED`;
- `EV03_RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED`, con la intersección conocida `DA-EVAL-V02-00060 / 87044110 / rank 100`;
- `EV03_METRIC_IMPACT = NOT_DETERMINED`;
- `EV04_METRIC_IMPACT = NOT_DETERMINED`;
- no existe justificación actual para `FULL_BENCHMARK_REBUILD`, `SPLIT_REBUILD` ni `LABEL_REMAP`;
- el snapshot experimental original basado en Decisión 885 debe preservarse y cualquier contraste actualizado debe registrarse como sensibilidad correctiva separada;
- la reapertura downstream debe depender de propagación demostrada y no producirse automáticamente.

### Corrección material de alcance

El feedback experimental actual reduce la reejecución numérica pendiente a EV-03 y EV-04. Sin embargo, una revisión experimental previa del mismo gate había identificado explícitamente EV-05/D1a como potencialmente expuesto por su dependencia directa de `corpus_rag_v1_index.jsonl`. El feedback actual no documenta una auditoría de dependencia ni una justificación explícita que permita retirar D1a de ese alcance previamente identificado.

Por tanto, antes de cerrar el corrective experimental gate, la IA experimental debe resolver de forma trazable el estado de EV-05/D1a mediante una de dos vías:

1. incluir EV-05/D1a en la sensibilidad correctiva; o
2. excluirlo explícitamente, sustentando esa exclusión con evidencia de dependencia/independencia suficiente.

Esta observación **no ordena por defecto un rerun de D1a**. Exige que la inclusión o exclusión quede decidida y sustentada antes del cierre del gate.

EXP-04E puede mantenerse como downstream condicional a cambios demostrados en los artefactos que consume. EXP-04F y HE4 pueden mantenerse bajo auditoría de intersección antes de cualquier reejecución. No existe base en este gate para reabrir H100, EXP-11A o EXP-11B por el drift normativo identificado.

### Dictamen editorial

```text
0B05C_CORRECTIVE_EXPERIMENTAL_REVIEW = PASS_WITH_MATERIAL_CORRECTION
CORRECTIVE_GATE_SCOPING = INCOMPLETE

SOURCE_VERSION_DRIFT = PRESENT
CHAPTER_87_SCOPE_OVERLAP = CONFIRMED
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED
EV05_D1A_STATUS = REQUIRES_EXPLICIT_INCLUSION_OR_EXCLUSION_JUSTIFICATION
DOWNSTREAM_REEXECUTION = CONDITIONAL_ON_PROPAGATION

CORRECTIVE_NUMERICAL_RERUN = REQUIRED
0B05C_CLOSURE = NOT_AUTHORIZED
0B06_0C_0D = BLOCKED
MANUSCRIPT_DRAFTING = BLOCKED
```

### Gate

`EXPERIMENTAL_REVIEW = REQUIRED` porque permanecen pendientes la comprobación numérica correctiva y la disposición explícita y trazable de EV-05/D1a. No corresponde todavía aprobación del autor, retorno a la IA de Redacción ni freeze de 0B-05C.

---

## English

### Scope

Independent editorial review of the experimental feedback that keeps `0B-05C_CORRECTIVE_EXPERIMENTAL_GATE = OPEN — BOUNDED NUMERICAL REEXECUTION REQUIRED`. This review does not run experiments, does not modify the Master Plan, and does not alter frozen experimental artifacts.

### Accepted findings

The following are accepted as supported for this gate:

- `SOURCE_VERSION_DRIFT = PRESENT`;
- `CHAPTER_87_SCOPE_OVERLAP = CONFIRMED`;
- the NANDINA-8 codes materially identified for this drift are `87044110` and `87045110`;
- the identified drift changes their normative textual representation, not their NANDINA-8 identifiers;
- `EVAL_LABEL_IMPACT = NOT_OBSERVED`;
- `HISTORICAL_RANKING_IMPACT = NOT_OBSERVED`;
- `EV03_RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED`, with the known intersection `DA-EVAL-V02-00060 / 87044110 / rank 100`;
- `EV03_METRIC_IMPACT = NOT_DETERMINED`;
- `EV04_METRIC_IMPACT = NOT_DETERMINED`;
- there is currently no justification for `FULL_BENCHMARK_REBUILD`, `SPLIT_REBUILD`, or `LABEL_REMAP`;
- the original Decision-885-based experimental snapshot must be preserved, and any updated comparison must be recorded as a separate corrective sensitivity analysis;
- downstream reopening must depend on demonstrated propagation and must not occur automatically.

### Material scope correction

The current experimental feedback narrows the pending numerical re-execution to EV-03 and EV-04. However, an earlier experimental review of the same gate had explicitly identified EV-05/D1a as potentially exposed through its direct dependency on `corpus_rag_v1_index.jsonl`. The current feedback does not document a dependency audit or an explicit rationale supporting removal of D1a from that previously identified scope.

Therefore, before the corrective experimental gate can be closed, the experimental AI must resolve the EV-05/D1a status in a traceable way through one of two paths:

1. include EV-05/D1a in the corrective sensitivity analysis; or
2. explicitly exclude it, supporting that exclusion with sufficient dependency/independence evidence.

This observation **does not mandate a D1a rerun by default**. It requires the inclusion/exclusion decision to be made and supported before gate closure.

EXP-04E may remain conditional downstream pending demonstrated changes in the artifacts it consumes. EXP-04F and HE4 may remain subject to intersection auditing before any re-execution. This gate provides no basis for reopening H100, EXP-11A, or EXP-11B because of the identified normative drift.

### Editorial verdict

```text
0B05C_CORRECTIVE_EXPERIMENTAL_REVIEW = PASS_WITH_MATERIAL_CORRECTION
CORRECTIVE_GATE_SCOPING = INCOMPLETE

SOURCE_VERSION_DRIFT = PRESENT
CHAPTER_87_SCOPE_OVERLAP = CONFIRMED
EV03_METRIC_IMPACT = NOT_DETERMINED
EV04_METRIC_IMPACT = NOT_DETERMINED
EV05_D1A_STATUS = REQUIRES_EXPLICIT_INCLUSION_OR_EXCLUSION_JUSTIFICATION
DOWNSTREAM_REEXECUTION = CONDITIONAL_ON_PROPAGATION

CORRECTIVE_NUMERICAL_RERUN = REQUIRED
0B05C_CLOSURE = NOT_AUTHORIZED
0B06_0C_0D = BLOCKED
MANUSCRIPT_DRAFTING = BLOCKED
```

### Gate

`EXPERIMENTAL_REVIEW = REQUIRED` because the corrective numerical check and the explicit, traceable disposition of EV-05/D1a remain unresolved. Author approval, return to the writing AI, and freezing 0B-05C are not yet appropriate.