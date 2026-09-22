# D-030 — Reconciliación editorial posterior al cierre de Grupo 5

## Estado

`AUTHORIAL_GOVERNANCE_UPDATE / EXPERIMENTAL_STATE_RECONCILIATION / ACTIVE / BINDING`

Fecha de reconciliación editorial: 2026-09-21.

## Fuente canónica verificada

- Repositorio: `elVladdi/gci-nandina-rag`
- Plan Maestro experimental: rama `docs/plan-maestro-temporal-2026-08-31`
- HEAD leído: `98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e`
- Ruta: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`
- Blob SHA leído: `9b388fe8cc19fce86ec3c15853e73899cb3e5666`
- Checkpoint experimental `main`: `ca065618d5df0019f76ef5a971e858d91c263e1f`

La rama del Plan Maestro registra además, de forma explícita, los cierres sucesivos de G5-F01, G5-F02 y G5-F03 tras auditoría o reauditoría externa.

## Estado experimental reconciliado

```text
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
GROUP4 = CLOSED / APPROVED
GROUP5 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE

G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F01_INTEGRATION_COMMIT = d5729887f47c36d8cf42d87090c40f9668e5ae84
G5_F01_EXTERNAL_REAUDIT = PASS

G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02_INTEGRATION_COMMIT = e471d4336ab965cd55b7f0e2ca7926445b1f0391
G5_F02_EXTERNAL_REAUDIT = PASS

G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03_INTEGRATION_COMMIT = ca065618d5df0019f76ef5a971e858d91c263e1f
G5_F03_EXTERNAL_AUDIT = PASS

GROUP6 = NOT_STARTED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
```

Elegibilidad de G6-F01 no constituye autorización ni inicio de Grupo 6.

## Material de Grupo 5 consumible por el artículo

Grupo 5 cerró la presentación controlada de resultados sin recalcular métricas, inferencia, intervalos ni p-values. Quedan disponibles para futura redacción de Results, únicamente cuando su gate editorial sea abierto:

- `G5-MAIN-01`: contrastes primarios HE2_A de ranking temprano — `PRIMARY_INFERENTIAL`;
- `G5-MAIN-02`: cobertura profunda HE2_B — `PRIMARY_INFERENTIAL`;
- `G5-SECONDARY-01`: Phase E — `DESCRIPTIVE_SUPPLEMENTARY`;
- `G5-SECONDARY-02`: componentes HE5 — `DESCRIPTIVE_HE5`;
- cinco tablas de apéndice/suplemento, incluidas sensibilidad EXP11A, EXP11B, corrección 0B-05C Attempt06 y unión diagnóstica Phase E.

El sistema canónico comprende nueve tablas. G5-F03 preserva además los destinos `TEXT_ONLY` y `NOT_PRESENTED_AS_RESULT_WITH_REASON` para evidencia no estimable y guardrails.

Grupo 5 no cambia las decisiones científicas previamente congeladas. Permanecen:

- `HE2 = SUPPORTED`;
- `HE5 = INCONCLUSIVE`;
- `EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL`;
- `EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE`;
- `EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE`;
- la sensibilidad correctiva 0B-05C depende del método y no puede resumirse como impacto global cero;
- `HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false`;
- `NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false`;
- `AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false`.

## Efecto editorial

1. `ARTICLE_WRITING_PLAN.md`, `ARTICLE_STATUS.md` y `SOURCE_REGISTRY.md` deben consumir este corte canónico de Grupo 5.
2. `CLAIM_EVIDENCE_MATRIX.md` no requiere nuevos claims por este cierre: Grupo 5 organiza y presenta evidencia ya congelada; no introduce nuevas métricas, inferencia ni decisiones de hipótesis. Sus claims autorizados/prohibidos permanecen gobernados por G3/G4 y por los límites de presentación G5.
3. El cierre de Grupo 5 hace que las tablas canónicas y su clasificación de rol estén disponibles para futura `Results`, pero **no abre** `Results`, `Experimental design`, `Discussion` ni ninguna otra sección.
4. El gate editorial activo continúa siendo `INTRODUCTION_B01 / SECTION_1_PROVISIONAL_ONLY`.
5. `Decision-support architecture` continúa `NOT_AUTHORIZED` hasta el cierre editorial correspondiente de Introduction B01.
6. G6-F01 es solo elegible. Figuras y visualizaciones no están autorizadas ni iniciadas.
7. La fase futura de Results deberá consumir los roles y guardrails de G5 sin convertir tablas descriptivas o diagnósticas en evidencia confirmatoria.
8. `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen sin cambios.

## Relación con el baseline editorial vigente

D-029 continúa gobernando el DOCX acumulativo activo:

```text
GOVERNING_B06_DOCX_FILENAME = ARTICLE_MASTER_B06_REGENERATED_V01.docx
GOVERNING_B06_DOCX_SHA256 = 7050cf9fee27687c7b9ed66d0ee110ef38b7aca1671868aaf3065fe50432377b
GOVERNING_B06_DOCX_COMMENTS = 36
GOVERNING_B06_DOCX_CUSTODY = LOCAL / AUTHOR / VERIFIED_BY_HANDOFF
```

D-030 no modifica el contenido científico aprobado de Related Work ni el baseline Markdown `ARTICLE_MASTER_V006.md`; únicamente reconcilia el estado experimental consumible por la redacción.

## English control summary

The article-side experimental snapshot is reconciled with the canonical Master Plan after full Group 5 closure. G5-F01, G5-F02, and G5-F03 are `CLOSED / APPROVED / INTEGRATED_TO_MAIN`, with the final Group 5 checkpoint at `main@ca065618d5df0019f76ef5a971e858d91c263e1f`. Group 5 provides a frozen nine-table presentation system and appendix/text-only destinations without recomputing metrics or changing `HE2 = SUPPORTED` or `HE5 = INCONCLUSIVE`. Group 6 remains `NOT_STARTED`; G6-F01 is only `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`. This reconciliation does not open Results or any later manuscript section. Introduction B01 remains the sole active drafting authorization.