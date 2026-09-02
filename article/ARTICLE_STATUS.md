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
- Último dictamen experimental recibido: `PASS WITH 2 REQUIRED CORRECTIONS`
- Estado de remediación: `SECOND_REMEDIATION_INTEGRATED — PENDING_FINAL_EXPERIMENTAL_PASS`
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

Quedaron validados, entre otros puntos, `SRC-03` como fuente GitHub viva, el carácter obsoleto del snapshot `3,000/100/1,006`, la diferencia entre unicidad de `id_unico` e independencia por DAM, la composición/métricas vigentes de v0.2 y el carácter pendiente de EXP-11B retrieval, EXP-12 y Grupo 3.

La revisión interna conserva históricamente la mención `48/59`, pero un addendum posterior aclara que su estado vigente es `C20 = REVIEW_REQUIRED`; no está autorizado como hallazgo congelado.

### Revisión experimental de 0A-01

La primera auditoría experimental emitió `PASS WITH CORRECTIONS` y condujo a normalizar los estados de claims, separar `995/1006` de `48/59`, preservar `HE5 = PENDING_GROUP3` como estado inferencial final y formalizar la gobernanza del Plan Maestro.

El pase experimental de cierre posterior emitió `PASS WITH 2 REQUIRED CORRECTIONS`. Las dos correcciones requeridas fueron:

1. reconocer expresamente el artefacto versionado `outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/exp08_integrated_findings_v0.2.md`, que registra `HE5 = PARTIALLY_SUPPORTED` como interpretación histórica/intermedia específica de EXP-08, sin confundirla con la decisión inferencial final vigente `HE5 = PENDING_GROUP3`;
2. reforzar D-011 y `SOURCE_REGISTRY.md` para exigir sincronización por **igualdad del contenido textual canónico** entre la copia local y GitHub del Plan Maestro, no mera equivalencia semántica, admitiendo únicamente diferencias técnicas de fin de línea, y declarar que D-011 supersede a D-009 en materias de sincronización, coexistencia y divergencia.

Ambas correcciones ya están integradas. También se añadió al registro histórico de revisión interna la nota de supersesión correspondiente a `48/59`.

### Estado científico que no cambia

- `995/1006`: autorizado como hallazgo histórico v0.1 con trazabilidad experimental.
- `48/59`: `REVIEW_REQUIRED`.
- EXP-08: contiene una interpretación histórica/intermedia `HE5 = PARTIALLY_SUPPORTED`.
- Decisión inferencial final de HE5: `PENDING_GROUP3`.
- EXP-11B retrieval: `PENDING`.
- H150/H200: sin resultados de retrieval autorizados todavía.
- EXP-12: `PENDING`.
- Grupo 3: `PENDING`.
- 0A-02: `NOT_AUTHORIZED`.

### Trabajo autorizado ahora

Realizar exclusivamente un **pase experimental final y limitado de 0A-01** sobre la actualización actual de `article/main-manuscript`.

El revisor debe verificar únicamente:

1. tratamiento correcto de EXP-08/HE5;
2. redacción exacta de sincronización del Plan Maestro y precedencia D-011 sobre D-009;
3. ausencia de regresiones respecto de los puntos ya resueltos.

No reabrir el análisis documental desde cero. No iniciar 0A-02 ni Fase 0B.

### Próximo gate

1. recibir `PASS — READY FOR AUTHOR APPROVAL` de la IA experimental;
2. obtener aprobación expresa del autor para 0A-01;
3. consolidar/cerrar el artefacto definitivo de 0A-01 en GitHub;
4. marcar 0A-01 como `APPROVED/FROZEN` según el protocolo;
5. solo entonces abrir 0A-02.

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
- Latest experimental verdict received: `PASS WITH 2 REQUIRED CORRECTIONS`
- Remediation status: `SECOND_REMEDIATION_INTEGRATED — PENDING_FINAL_EXPERIMENTAL_PASS`
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

Among other points, it validated `SRC-03` as a living GitHub source, the stale character of the `3,000/100/1,006` snapshot, the distinction between `id_unico` uniqueness and DAM-level independence, the current v0.2 composition/metrics, and the pending character of EXP-11B retrieval, EXP-12, and Group 3.

The internal review historically retains the `48/59` mention, but a later addendum clarifies that its current status is `C20 = REVIEW_REQUIRED`; it is not authorized as a frozen finding.

### Experimental review of 0A-01

The first experimental audit issued `PASS WITH CORRECTIONS` and led to normalization of claim statuses, separation of `995/1006` from `48/59`, preservation of `HE5 = PENDING_GROUP3` as the final inferential status, and formalization of Master Plan governance.

The subsequent closing experimental pass issued `PASS WITH 2 REQUIRED CORRECTIONS`. The two required corrections were:

1. explicitly acknowledge the versioned artifact `outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/exp08_integrated_findings_v0.2.md`, which records `HE5 = PARTIALLY_SUPPORTED` as a historical/intermediate interpretation specific to EXP-08, without confusing it with the current final inferential decision `HE5 = PENDING_GROUP3`;
2. strengthen D-011 and `SOURCE_REGISTRY.md` to require synchronization by **equality of canonical textual content** between the local and GitHub Master Plan copies, rather than mere semantic equivalence, allowing only technical line-ending differences, and state that D-011 supersedes D-009 on synchronization, coexistence, and divergence matters.

Both corrections have now been integrated. The corresponding `48/59` supersession note was also added to the historical internal-review record.

### Scientific status that remains unchanged

- `995/1006`: authorized as a historical v0.1 finding with experimental traceability.
- `48/59`: `REVIEW_REQUIRED`.
- EXP-08: contains a historical/intermediate interpretation `HE5 = PARTIALLY_SUPPORTED`.
- Final inferential HE5 decision: `PENDING_GROUP3`.
- EXP-11B retrieval: `PENDING`.
- H150/H200: no authorized retrieval results yet.
- EXP-12: `PENDING`.
- Group 3: `PENDING`.
- 0A-02: `NOT_AUTHORIZED`.

### Work authorized now

Perform only a **final, limited experimental pass for 0A-01** on the current update of `article/main-manuscript`.

The reviewer must verify only:

1. correct EXP-08/HE5 handling;
2. exact Master Plan synchronization wording and D-011 precedence over D-009;
3. absence of regressions in previously resolved points.

Do not reopen the documentary analysis from scratch. Do not start 0A-02 or Phase 0B.

### Next gate

1. receive `PASS — READY FOR AUTHOR APPROVAL` from the experimental AI;
2. obtain the author's express approval of 0A-01;
3. consolidate/close the final 0A-01 artifact on GitHub;
4. mark 0A-01 as `APPROVED/FROZEN` according to protocol;
5. only then open 0A-02.
