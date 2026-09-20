# D-019 — Reconciliación editorial posterior al cierre de Grupo 4

## Estado

`AUTHORIAL_GOVERNANCE_UPDATE / EXPERIMENTAL_STATE_RECONCILIATION`

Fecha de reconciliación editorial: 2026-09-20.

## Fuente canónica verificada

- Repositorio: `elVladdi/gci-nandina-rag`
- Plan Maestro: rama `docs/plan-maestro-temporal-2026-08-31`
- HEAD leído: `3ba3557eb10e741b8f49c420850940dee1df08ef`
- Ruta: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`
- Blob SHA leído: `5ab0af7af5a2c92a1107e820bee1a6bb65026432`
- Checkpoint experimental `main`: `38e22c19a0eb0d344e7675761a88d7968091eead`

## Estado experimental reconciliado

```text
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03_EXTERNAL_REAUDIT = PASS
GROUP5 = NOT_STARTED
G5_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

El cierre de Grupo 4 no modifica las decisiones `HE2 = SUPPORTED` ni `HE5 = INCONCLUSIVE` y no recalcula métricas, inferencia, intervalos ni p-values.

## Material de Grupo 4 consumible por el artículo

G4-F03 integró el registro controlado de contraste con literatura:

- 11 registros de comparación;
- 8 puntos de discusión autorizados;
- 14 puntos de discusión prohibidos;
- artefacto principal: `docs/analysis/group4/g4_literature_contrast_v0.1.md` en `main@38e22c19a0eb0d344e7675761a88d7968091eead`.

El registro permite, cuando el gate editorial de Discussion esté abierto, contrastes funcionales y metodológicos dentro de las fronteras expresamente fijadas. No autoriza por sí mismo superioridad numérica cross-study, SOTA, novelty absoluta, unicidad, generalización empírica, causalidad no identificada ni corrección jurídica.

Se preservan de forma vinculante, entre otras, estas fronteras:

- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_EVIDENCE ≠ LEGAL_CORRECTNESS`;
- `AUDITABLE_EXPLANATION ≠ CLASSIFICATION_VALIDATION`;
- `PROVENANCE / REPRODUCIBILITY ≠ OUTPUT_LEVEL_AUDITABILITY / CORRECTNESS`;
- `EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL`;
- `EXP11B = DESCRIPTIVE / NO_SEED_SUPERPOPULATION_INFERENCE`;
- `EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE`.

## Efecto editorial

1. `ARTICLE_STATUS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md` y `ARTICLE_WRITING_PLAN.md` deben consumir este nuevo corte canónico.
2. El cierre de Grupo 4 no reabre Related Work 2.1–2.3 ni obliga a modificar su texto aprobado.
3. B04 continúa en revisión correctiva V02; este cierre experimental no sustituye ni cancela el prompt correctivo ya autorizado.
4. B05 / Section 2.5 continúa bloqueada hasta el cierre editorial de B04.
5. `Experimental design`, `Results` y `Discussion` continúan sujetos a sus gates editoriales independientes. Evidencia cerrada no equivale a autorización de redacción.
6. `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen sin cambios.
7. Grupo 5 no se considera iniciado: `G5-F01` es solo elegible y no autorizado.

## English control summary

The article-side experimental snapshot is reconciled with the canonical Master Plan after Group 4 closure. Group 4 is `CLOSED / APPROVED`; G4-F01, G4-F02, and G4-F03 are `CLOSED / APPROVED / INTEGRATED_TO_MAIN`; G4-F03 passed external re-audit. Its controlled literature-contrast registry contains 11 comparison records, 8 authorized discussion points, and 14 forbidden discussion points. These materials become eligible evidence for future Discussion only when the corresponding editorial gate opens. They do not establish cross-study numerical superiority, SOTA, absolute novelty, empirical generalization, unsupported causality, or legal correctness. Group 5 remains `NOT_STARTED` and G5-F01 remains `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`.
