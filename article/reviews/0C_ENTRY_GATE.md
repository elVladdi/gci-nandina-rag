# Gate de entrada 0C / 0C Entry Gate

## Español

### 1. Dictamen

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = READY_FOR_DRAFTING
0D = BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
NEW_LITERATURE_SEARCH = NOT_AUTHORIZED
```

Se cumplen las dependencias documentales para abrir `0C — Gap, contribución y Research Questions`: 0A está cerrado/aprobado y 0B está cerrado/aprobado con todos sus lotes congelados. La apertura de 0C no declara gap final ni novelty y no autoriza la redacción del manuscrito.

### 2. Fuentes gobernantes de entrada

0C deberá consumir, sin reabrirlos ni reinterpretarlos silenciosamente:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- freezes `0B-01` a `0B-06`;
- `article/reviews/0B_PHASE_CLOSURE.md`;
- `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/DECISIONS.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/STYLE_GUIDE.md`.

El Plan Maestro experimental se verificó en modo solo lectura al abrir este gate:

- rama: `docs/plan-maestro-temporal-2026-08-31`;
- HEAD: `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`;
- blob leído: `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`.

Este snapshot coincide con el ya registrado durante la reconciliación final de 0B-05C; no se detectó un cambio de la fuente viva que obligue a reabrir 0A/0B.

### 3. Estado obligatorio transferido desde 0B

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F4 = METHODOLOGICAL_BOUNDARY_NOT_INDEPENDENT_NOVELTY
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
G6 = ELIMINATED_AS_GAP_CANDIDATE
G7 = MERGED_INTO_F2
```

Interpretación obligatoria:

- F1 solo puede tratarse como candidato estrecho; un resultado negativo acotado no demuestra novelty.
- F2 solo sobrevive si se conserva la separación contractual: `EXTERNAL_FIXED_TOP_K + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT/DELETE/SUBSTITUTE/REORDER + NO_CLASSIFICATION_FEEDBACK`.
- F3 es un principio/candidato metodológico condicionado a que existan observaciones correlacionadas por unidad administrativa o entidad; ausencia de grouped split documentado no prueba leakage ni novelty.
- F4 es una frontera metodológica entre desempeño predictivo/retrieval/evidence/path y corrección sustantiva o jurídica; no es novelty independiente.
- F5 no puede formularse como ausencia general de evaluación de auditabilidad en regulatory AI. Cualquier uso posterior debe ser contextual y más estrecho.
- G6 permanece eliminado y G7 permanece absorbido en F2.

### 4. Alcance científico autorizado de 0C

0C debe construir y contrastar, no asumir de antemano:

1. un posible **gap empírico** compatible con el alcance experimental realmente ejecutado;
2. un posible **gap metodológico** centrado en la separación funcional y contractual de etapas, controles de dependencia y límites de inferencia;
3. un posible **gap de apoyo a decisiones/auditabilidad**, únicamente en formulaciones que sobrevivan a F5 y sin equivaler auditabilidad a legal correctness;
4. **tres formulaciones alternativas** de contribución central, con distinta amplitud y riesgo de overclaiming;
5. Research Questions candidatas trazables a evidencia y resultados disponibles;
6. claims principales y secundarios candidatos, distinguiendo `SUPPORTED_NOW`, `CONDITIONAL_ON_PENDING_EXPERIMENT`, `NOT_SUPPORTED` y `PROHIBITED_BY_FROZEN_BOUNDARY` como etiquetas analíticas internas del entregable, sin modificar todavía `CLAIM_EVIDENCE_MATRIX.md`;
7. mapeo de objetivos/hipótesis aprobados hacia `IN_PAPER`, `CONDITIONAL`, o `THESIS_ONLY`, preservando la formulación documental congelada y sin redefinir objetivos o hipótesis.

### 5. Dependencias experimentales

0C puede abrirse aunque la investigación experimental global continúe. Sin embargo, ninguna contribución, RQ o claim puede presentar como hecho un resultado aún no cerrado.

El Plan Maestro vigente mantiene Grupo 3 como siguiente bloque de métricas/inferencia y conserva dependencias experimentales posteriores. Por tanto, 0C debe distinguir entre:

- posicionamiento sustentable con evidencia ya congelada;
- formulaciones condicionadas a resultados experimentales pendientes;
- formulaciones no sustentables que deben descartarse.

0C no ejecuta experimentos, no cambia el Plan Maestro y no decide resultados pendientes.

### 6. Prohibiciones de 0C

Durante este bloque queda prohibido:

- declarar `FINAL_GAP` o `NOVELTY` por cuenta propia;
- usar expresiones como “first”, “novel”, “no prior work”, “unprecedented” o equivalentes sin un gate editorial posterior;
- convertir `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE` en prueba de inexistencia universal;
- reabrir 0B o iniciar una nueva búsqueda bibliográfica;
- promover N02 a admitido sin revisión específica;
- usar F5 en su formulación general falsada;
- presentar auditabilidad, source support o trazabilidad como legal correctness;
- usar resultados experimentales pendientes como hechos;
- modificar objetivos, hipótesis, arquitectura, métricas o unidades de análisis;
- decidir journal fit;
- redactar Introduction, Related Work, Methods, Results, Discussion, Conclusions, Abstract o Title.

### 7. Entregable requerido

La IA de Redacción deberá producir un único artefacto de análisis y posicionamiento en:

`article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`

El artefacto deberá ser bilingüe y quedará pendiente de auditoría de la IA Gestora / Editor Científico Principal. No constituye texto de manuscrito.

### 8. Gate posterior

Tras recibir V01:

```text
IA_GESTORA_AUDIT
-> corrections if needed
-> author approval
-> 0C freeze
-> only then evaluate/open 0D
```

`EXPERIMENTAL_REVIEW = NOT_REQUIRED` en la apertura. Solo se activará si la propuesta de 0C introduce una interpretación nueva de resultados experimentales o entra en conflicto con el Plan Maestro.

---

## English

### 1. Verdict

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = READY_FOR_DRAFTING
0D = BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
NEW_LITERATURE_SEARCH = NOT_AUTHORIZED
```

The documentary dependencies for opening `0C — Gap, contribution, and Research Questions` are satisfied: 0A and 0B are closed/approved and all required literature batches are frozen. Opening 0C does not declare a final gap or novelty and does not authorize manuscript drafting.

### 2. Governing inputs

0C must consume without silently reopening or reinterpreting the frozen 0A artifacts, 0B-01 through 0B-06 freezes, the formal 0B closure, bibliographic admission registry, Claim–Evidence Matrix, Decisions, Source Registry, Master Writing Plan, and Style Guide.

The live experimental Master Plan was checked read-only at branch `docs/plan-maestro-temporal-2026-08-31`, HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`. This is unchanged from the 0B-05C final reconciliation snapshot and creates no reason to reopen 0A/0B.

### 3. Mandatory state transferred from 0B

F1 has a bounded negative search result only; F2 has partial prior art and survives only under strict upstream/downstream isolation; F3 is applicability-conditioned and does not support leakage/novelty claims from missing group splits; F4 is a methodological boundary, not independent novelty; F5 has direct prior art and its broad regulatory-AI absence claim is falsified; G6 is eliminated; G7 is merged into F2.

### 4. Authorized 0C scope

0C must construct and contrast rather than assume: possible empirical, methodological, and decision-support/auditability gaps; three alternative central-contribution formulations with different breadth and overclaiming risk; candidate RQs; candidate primary/secondary claims classified by present support versus pending evidence; and an exact mapping of approved objectives/hypotheses to paper scope versus thesis-only scope.

### 5. Experimental dependencies

0C may open while the broader experimental campaign remains active, but no pending result may be stated as fact. The current Master Plan keeps Group 3 as the next metrics/inference block and retains later experimental dependencies. 0C must therefore separate currently supportable positioning from experiment-conditioned or unsupported formulations.

### 6. Prohibitions

0C may not self-declare final gap/novelty, convert bounded negative searches into universal absence, reopen literature search, restore broad F5, equate auditability with legal correctness, use pending experimental results as facts, change approved architecture/objectives/hypotheses/metrics/units, decide journal fit, or draft manuscript sections.

### 7. Required deliverable

The Writing AI must create exactly one bilingual analysis artifact at:

`article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`

It remains pending Managing-AI / Lead-Editor audit and is not manuscript prose.

### 8. Downstream gate

After V01: Managing-AI audit -> corrections if required -> author approval -> 0C freeze -> only then evaluate/open 0D.

`EXPERIMENTAL_REVIEW = NOT_REQUIRED` at entry. It becomes required only if 0C introduces a new interpretation of experimental results or conflicts with the Master Plan.
