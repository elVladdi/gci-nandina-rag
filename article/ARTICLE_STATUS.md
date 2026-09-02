# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`
- Estado global: `IN_ANALYSIS`
- Fase activa: `0A — Ground truth documental y experimental`
- Bloque activo: `0A-01 — Ground truth documental`
- Estado del bloque: `EXPERIMENTAL_REVIEW`
- Prompt activo: `article/prompts/0A01_DOCUMENTARY_GROUND_TRUTH.md`
- Revisión interna: `article/reviews/0A01_INTERNAL_REVIEW.md`
- Revisión experimental: `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`
- Dictamen experimental recibido: `PASS WITH CORRECTIONS`
- Target journal: `PENDING — se decidirá en Fase 0D`
- Idioma del chat: español
- Artefactos GitHub: español + inglés con equivalencia semántica
- Manuscrito redactado: no iniciado

### Dependencias actuales

| Elemento | Estado | Efecto sobre el paper |
|---|---|---|
| Proyecto de tesis aprobado | AVAILABLE_FOR_0A01 | fuente para problema, objetivos, hipótesis, justificación y alcance |
| Anexo v13 | AVAILABLE_FOR_0A01 | fuente para arquitectura y metodología operativa actual |
| Plan Maestro experimental | LIVING_SOURCE_IN_GITHUB / EXPERIMENTAL_WRITE_ONLY | fuente para estado experimental actual; usar `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` en rama `docs/plan-maestro-temporal-2026-08-31`; snapshot registrado de 0A-01 `0a9a82181c6c3840f74f0272e5c225568474058b`; solo la IA experimental puede modificarlo |
| Tesis preliminar vigente | AVAILABLE_FOR_0A01 | fuente secundaria para identificar formulaciones posteriores y snapshots obsoletos; no gobierna estado experimental |
| Literatura científica | DEFERRED_TO_0B | los PDF se incorporarán por lotes en Fase 0B |
| GitHub desarrollo | ACTIVE | fuente de artefactos y estado técnico |
| EXP-11B retrieval | PENDING | bloquea resultados de H150/H200 |
| EXP-12 | PENDING | bloquea parte del análisis definitivo |
| Grupo 3 | PENDING | bloquea decisión inferencial final de HE2/HE5 |
| Repositorio de reproducibilidad | STRUCTURAL | se completará tras cierre experimental |

### Revisión interna de 0A-01

La segunda ejecución corregida de 0A-01 superó la revisión científica/editorial interna con dictamen `PASS WITH MINOR TERMINOLOGY CORRECTION`.

Quedaron validados:

1. `SRC-03` como fuente GitHub viva y su SHA como snapshot del corte;
2. los sufijos automáticos de adjuntos no se consideran versiones científicas por sí solos;
3. el snapshot `3,000/100/1,006` de la tesis preliminar queda aislado como estado experimental obsoleto;
4. la diferencia entre ausencia de `id_unico` repetidos e independencia por DAM;
5. el hallazgo v0.1 de `995/1006` casos de evaluación en DAM presentes en histórico;
6. `SERIE` como unidad de análisis y `DAM` como unidad de agrupamiento para construir particiones sin DAM compartidas;
7. la composición y métricas vigentes del benchmark v0.2;
8. EXP-11B retrieval, EXP-12 y Grupo 3 permanecen pendientes.

Precisión terminológica para etapas posteriores: el agrupamiento por DAM elimina el solapamiento de DAM entre particiones y la dependencia cruzada causada por compartir una misma declaración entre histórico/desarrollo/evaluación. No implica independencia interna de las 1,056 series del evalset cuando varias pertenecen a una misma DAM.

### Revisión experimental de 0A-01

La IA experimental emitió `PASS WITH CORRECTIONS`. Las correcciones aceptadas fueron integradas en la gobernanza del artículo:

1. se normalizó `CLAIM_EVIDENCE_MATRIX.md` para usar exclusivamente los estados permitidos;
2. `995/1006` se conserva como hallazgo histórico autorizado con trazabilidad experimental;
3. `48/59` se separó como observación derivada aún no congelada y quedó bajo `REVIEW_REQUIRED` hasta disponer de artefacto versionado o recomputación auditable;
4. el estado que gobierna la decisión final de HE5 permanece `PENDING_GROUP3`; no se congela ninguna interpretación histórica de EXP-08 sin verificar su artefacto exacto;
5. se formalizó que el Plan Maestro es un único documento lógico con dos copias operativas sincronizadas y que solo la IA experimental posee autoridad de escritura;
6. no se adoptó la sugerencia de ampliar automáticamente literatura nueva a proceedings, porque contradice la política bibliográfica aprobada por el autor.

Estas correcciones están documentadas en `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md` y `DECISIONS.md`.

### Trabajo autorizado ahora

Realizar exclusivamente un **pase experimental de cierre de 0A-01** sobre la actualización actual de `article/main-manuscript`.

El revisor debe comprobar que las correcciones derivadas de su dictamen fueron incorporadas sin introducir regresiones y que 0A-01 puede pasar al gate de aprobación del autor.

No iniciar 0A-02 ni Fase 0B.

### Próximo gate

1. recibir el pase experimental de cierre;
2. resolver únicamente nuevas observaciones bloqueantes, si las hubiera;
3. obtener aprobación expresa del autor para 0A-01;
4. consolidar/cerrar el artefacto definitivo de 0A-01 en GitHub;
5. marcar 0A-01 como `APPROVED/FROZEN` según el protocolo;
6. solo entonces abrir 0A-02.

---

## English

### Overall status

- Working branch: `article/main-manuscript`
- Global status: `IN_ANALYSIS`
- Active phase: `0A — Documentary and experimental ground truth`
- Active block: `0A-01 — Documentary ground truth`
- Block status: `EXPERIMENTAL_REVIEW`
- Active prompt: `article/prompts/0A01_DOCUMENTARY_GROUND_TRUTH.md`
- Internal review: `article/reviews/0A01_INTERNAL_REVIEW.md`
- Experimental review: `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`
- Experimental verdict received: `PASS WITH CORRECTIONS`
- Target journal: `PENDING — to be decided in Phase 0D`
- Chat language: Spanish
- GitHub artifacts: Spanish + English with semantic equivalence
- Drafted manuscript: not started

### Current dependencies

| Element | Status | Effect on the paper |
|---|---|---|
| Approved thesis project | AVAILABLE_FOR_0A01 | source for problem, objectives, hypotheses, justification, and scope |
| Annex v13 | AVAILABLE_FOR_0A01 | source for current architecture and operational methodology |
| Experimental Master Plan | LIVING_SOURCE_IN_GITHUB / EXPERIMENTAL_WRITE_ONLY | source for current experimental status; use `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` on branch `docs/plan-maestro-temporal-2026-08-31`; registered 0A-01 snapshot `0a9a82181c6c3840f74f0272e5c225568474058b`; only the experimental AI may modify it |
| Current preliminary thesis | AVAILABLE_FOR_0A01 | secondary source for later formulations and stale snapshots; does not govern experimental status |
| Scientific literature | DEFERRED_TO_0B | PDFs will be incorporated in thematic batches during Phase 0B |
| Development GitHub | ACTIVE | source of artifacts and technical status |
| EXP-11B retrieval | PENDING | blocks H150/H200 results |
| EXP-12 | PENDING | blocks part of the final analysis |
| Group 3 | PENDING | blocks final inferential decision for HE2/HE5 |
| Reproducibility repository | STRUCTURAL | to be completed after experimental closure |

### Internal review of 0A-01

The second corrected 0A-01 delivery passed the internal scientific/editorial review with verdict `PASS WITH MINOR TERMINOLOGY CORRECTION`.

The following were validated:

1. `SRC-03` as a living GitHub source and its SHA as a cutoff snapshot;
2. automatic attachment suffixes are not treated as scientific versions by themselves;
3. the `3,000/100/1,006` preliminary-thesis snapshot is isolated as stale experimental status;
4. the distinction between absence of repeated `id_unico` values and DAM-level independence;
5. the v0.1 finding that `995/1006` evaluation cases belonged to DAMs present in historical data;
6. `SERIES` as the analysis unit and `DAM` as the grouping unit for constructing partitions without shared DAMs;
7. the current v0.2 benchmark composition and metrics;
8. EXP-11B retrieval, EXP-12, and Group 3 remain pending.

Terminology precision for later stages: DAM grouping removes DAM overlap across partitions and the cross-partition dependence caused by sharing the same declaration across historical/development/evaluation sets. It does not imply internal independence of the 1,056 evaluation series when multiple series belong to the same DAM.

### Experimental review of 0A-01

The experimental AI issued `PASS WITH CORRECTIONS`. The accepted corrections were integrated into article governance:

1. `CLAIM_EVIDENCE_MATRIX.md` was normalized to use only the permitted statuses;
2. `995/1006` is retained as an authorized historical finding with experimental traceability;
3. `48/59` was separated as a derived, not-yet-frozen observation and placed under `REVIEW_REQUIRED` until a versioned artifact or auditable recomputation exists;
4. the state governing the final HE5 decision remains `PENDING_GROUP3`; no historical EXP-08 interpretation is frozen without verification of its exact artifact;
5. the Master Plan was formalized as one logical document with two synchronized operational copies, with write authority restricted to the experimental AI;
6. the suggestion to automatically broaden new literature to proceedings was not adopted because it conflicts with the author-approved bibliographic policy.

These corrections are documented in `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, and `DECISIONS.md`.

### Work authorized now

Perform only a **closing experimental pass for 0A-01** on the current update of `article/main-manuscript`.

The reviewer must verify that the corrections resulting from its verdict were incorporated without introducing regressions and that 0A-01 can proceed to the author's approval gate.

Do not start 0A-02 or Phase 0B.

### Next gate

1. receive the closing experimental pass;
2. resolve only new blocking observations, if any;
3. obtain the author's express approval of 0A-01;
4. consolidate/close the final 0A-01 artifact on GitHub;
5. mark 0A-01 as `APPROVED/FROZEN` according to protocol;
6. only then open 0A-02.
