# D-082 — Rechazo autoral de B07 V01 y corrección de alcance hacia recursos públicos de reproducibilidad / B07 V01 author rejection and public reproducibility scope correction

## Español

```text
DECISION_ID = D-082
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-081
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
AUTHOR_DECISION = NOT_APPROVED / REVISION_REQUIRED
AUTHOR_OBSERVATION = INTERNAL_DEVELOPMENT_REPOSITORY_SHOULD_NOT_BE_PRESENTED_AS_A_REPRODUCIBILITY_RESOURCE
B07_STATE = REVISION_REQUIRED
AUTHOR_APPROVAL_GATE = CLOSED_PENDING_REVISION
CANONICAL_MASTER = ARTICLE_MASTER_V015
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión autoral

El autor no aprueba B07 V01. La observación es válida y modifica el alcance editorial de Section 4.8: el repositorio interno de desarrollo experimental no debe presentarse ni introducirse en la prosa del manuscrito como recurso de reproducibilidad. Su función es interna —historial experimental, trazabilidad de desarrollo y artefactos de trabajo— y no forma parte del paquete público que el lector debe usar como recurso de reproducción/replicación.

El `PASS` técnico previo de D-081 queda superado exclusivamente respecto de esta preferencia/alcance autoral. No se cuestionan la integridad del DOCX, el cumplimiento D-035, la equivalencia EN/ES ni la exactitud del snapshot público.

## 2. Corrección científica/editorial obligatoria

Section 4.8 debe centrarse directamente en `gci-nandina-rag-reproducibility` y en lo que ese repositorio público actualmente contiene, permite documentar y todavía no materializa.

Se elimina de la prosa de Section 4.8:

- la presentación del repositorio de desarrollo experimental;
- la comparación explícita entre repositorio de desarrollo y repositorio público;
- cualquier formulación que invite al lector a considerar el repositorio interno como parte del paquete de reproducibilidad.

Cuando sea necesario referirse a entradas no públicas, debe hacerse por su condición científica —por ejemplo, `restricted/non-redistributed reference inputs`— sin dirigir al lector al repositorio interno de desarrollo.

## 3. Relación con D-079

D-079 sigue vigente para el snapshot público, sus identidades y las fronteras entre recursos materializados, planificados y restringidos. Queda **SUPERSEDED IN PART** el requisito de D-079 que pedía conservar en Section 4.8 una separación narrativa entre repositorio de desarrollo y paquete público.

La nueva regla es:

```text
SECTION_4_8_PUBLIC_RESOURCE_FOCUS = REQUIRED
INTERNAL_DEVELOPMENT_REPOSITORY_MENTION = REMOVE_FROM_MANUSCRIPT_PROSE
PUBLIC_REPRO_REPOSITORY = gci-nandina-rag-reproducibility
REFERENCE_REPRODUCTION_VS_EXTERNAL_REPLICATION = PRESERVE
MATERIALIZED_VS_PLANNED_VS_RESTRICTED = PRESERVE
```

## 4. Alcance de la revisión

La revisión debe ser estrecha. No debe reescribirse el bloque completo. Debe:

1. sustituir el primer párrafo EN/ES por una apertura centrada directamente en el repositorio público de reproducibilidad;
2. eliminar en el resto de Section 4.8 cualquier referencia al repositorio de desarrollo como contraparte pública/privada;
3. conservar sin cambios sustantivos las fronteras ya correctas sobre estado incompleto de la release, reproducción vs replicación, configurabilidad, redistribución y recheck pre-submission;
4. preservar Sections 1–4.7 y Results+ exactamente;
5. mantener el régimen D-035 timeout-safe ya activado para B07.

## 5. Gate

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_NARROW_B07_PUBLIC_REPRO_SCOPE_CORRECTION
B07_INTEGRATION = BLOCKED
AUTHOR_APPROVAL_GATE = CLOSED_PENDING_REVISED_CANDIDATE_AND_GESTORA_AUDIT
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-082
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-081
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
AUTHOR_DECISION = NOT_APPROVED / REVISION_REQUIRED
B07_STATE = REVISION_REQUIRED
AUTHOR_APPROVAL_GATE = CLOSED_PENDING_REVISION
CANONICAL_MASTER = ARTICLE_MASTER_V015
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The author rejected B07 V01 because the internal experimental-development repository should not be presented in manuscript prose as a reproducibility resource. Section 4.8 must focus directly on the public `gci-nandina-rag-reproducibility` package. Internal development history may remain a source used by the editorial/experimental process, but it is not a reader-facing reproducibility resource.

D-079 remains binding for the audited public snapshot and for the materialized/planned/restricted boundaries, but its requirement to narratively contrast the internal development repository with the public package is superseded by this decision.

The revision must be narrow, preserve all other scientifically correct B07 boundaries, preserve Sections 1–4.7 and Results+, and continue to use the D-035 timeout-safe handoff regime.