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
- Target journal: `PENDING — se decidirá en Fase 0D`
- Idioma del chat: español
- Artefactos GitHub: español + inglés con equivalencia semántica
- Manuscrito redactado: no iniciado

### Dependencias actuales

| Elemento | Estado | Efecto sobre el paper |
|---|---|---|
| Proyecto de tesis aprobado | AVAILABLE_FOR_0A01 | fuente para problema, objetivos, hipótesis, justificación y alcance |
| Anexo v13 | AVAILABLE_FOR_0A01 | fuente para arquitectura y metodología operativa actual |
| Plan Maestro experimental | LIVING_SOURCE_IN_GITHUB | fuente para estado experimental actual; usar `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` en rama `docs/plan-maestro-temporal-2026-08-31`; snapshot de la revisión interna `0a9a82181c6c3840f74f0272e5c225568474058b` |
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
5. el hallazgo v0.1 de `995/1006` casos de evaluación en DAM presentes en histórico y `48/59` DAM de evaluación compartidas con histórico;
6. `SERIE` como unidad de análisis y `DAM` como unidad de agrupamiento para construir particiones sin DAM compartidas;
7. la composición y métricas vigentes del benchmark v0.2;
8. EXP-11B retrieval, EXP-12 y Grupo 3 permanecen pendientes.

Precisión terminológica para etapas posteriores: el agrupamiento por DAM elimina el solapamiento de DAM entre particiones y la dependencia cruzada causada por compartir una misma declaración entre histórico/desarrollo/evaluación. No implica independencia interna de las 1,056 series del evalset cuando varias pertenecen a una misma DAM.

### Trabajo autorizado ahora

Realizar exclusivamente la **auditoría experimental independiente de 0A-01**. La IA experimental debe verificar directamente contra repositorio y artefactos congelados los puntos consignados en `article/reviews/0A01_INTERNAL_REVIEW.md`.

No iniciar 0A-02 ni Fase 0B.

### Próximo gate

1. recibir feedback de la IA experimental;
2. resolver cualquier observación experimental;
3. obtener aprobación expresa del autor;
4. generar/consolidar el artefacto bilingüe definitivo de 0A-01 en GitHub;
5. cerrar 0A-01;
6. solo entonces evaluar apertura de 0A-02.

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
- Target journal: `PENDING — to be decided in Phase 0D`
- Chat language: Spanish
- GitHub artifacts: Spanish + English with semantic equivalence
- Drafted manuscript: not started

### Current dependencies

| Element | Status | Effect on the paper |
|---|---|---|
| Approved thesis project | AVAILABLE_FOR_0A01 | source for problem, objectives, hypotheses, justification, and scope |
| Annex v13 | AVAILABLE_FOR_0A01 | source for current architecture and operational methodology |
| Experimental Master Plan | LIVING_SOURCE_IN_GITHUB | source for current experimental status; use `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` on branch `docs/plan-maestro-temporal-2026-08-31`; internal-review snapshot `0a9a82181c6c3840f74f0272e5c225568474058b` |
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
5. the v0.1 finding that `995/1006` evaluation cases belonged to DAMs present in historical data and `48/59` evaluation DAMs were shared with historical data;
6. `SERIES` as the analysis unit and `DAM` as the grouping unit for constructing partitions without shared DAMs;
7. the current v0.2 benchmark composition and metrics;
8. EXP-11B retrieval, EXP-12, and Group 3 remain pending.

Terminology precision for later stages: DAM grouping removes DAM overlap across partitions and the cross-partition dependence caused by sharing the same declaration across historical/development/evaluation sets. It does not imply internal independence of the 1,056 evaluation series when multiple series belong to the same DAM.

### Work authorized now

Perform only the **independent experimental audit of 0A-01**. The experimental AI must verify directly against the repository and frozen artifacts the items recorded in `article/reviews/0A01_INTERNAL_REVIEW.md`.

Do not start 0A-02 or Phase 0B.

### Next gate

1. receive experimental-AI feedback;
2. resolve any experimental observation;
3. obtain express author approval;
4. generate/consolidate the final bilingual 0A-01 GitHub artifact;
5. close 0A-01;
6. only then evaluate opening 0A-02.
