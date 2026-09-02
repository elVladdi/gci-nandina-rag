# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`
- Estado global: `IN_ANALYSIS`
- Fase activa: `0A — Ground truth documental y experimental`
- Bloque activo: `0A-01 — Ground truth documental`
- Estado del bloque: `REVISION_REQUIRED`
- Prompt activo: `article/prompts/0A01_DOCUMENTARY_GROUND_TRUTH.md`
- Target journal: `PENDING — se decidirá en Fase 0D`
- Idioma del chat: español
- Artefactos GitHub: español + inglés con equivalencia semántica
- Manuscrito redactado: no iniciado

### Dependencias actuales

| Elemento | Estado | Efecto sobre el paper |
|---|---|---|
| Proyecto de tesis aprobado | AVAILABLE_FOR_0A01 | fuente para problema, objetivos, hipótesis, justificación y alcance |
| Anexo v13 | AVAILABLE_FOR_0A01 | fuente para arquitectura y metodología operativa actual |
| Plan Maestro experimental | LIVING_SOURCE_IN_GITHUB | fuente para estado experimental actual; usar `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` en rama `docs/plan-maestro-temporal-2026-08-31`; snapshot actual de revisión `0a9a82181c6c3840f74f0272e5c225568474058b` |
| Tesis preliminar vigente | AVAILABLE_FOR_0A01 | fuente secundaria para identificar formulaciones posteriores y snapshots obsoletos; no gobierna estado experimental |
| Literatura científica | DEFERRED_TO_0B | los PDF se incorporarán por lotes en Fase 0B |
| GitHub desarrollo | ACTIVE | fuente de artefactos y estado técnico |
| EXP-11B retrieval | PENDING | bloquea resultados de H150/H200 |
| EXP-12 | PENDING | bloquea parte del análisis definitivo |
| Grupo 3 | PENDING | bloquea decisión inferencial final de HE2/HE5 |
| Repositorio de reproducibilidad | STRUCTURAL | se completará tras cierre experimental |

### Revisión interna de 0A-01

La primera ejecución de 0A-01 reconstruyó correctamente las formulaciones aprobadas y detectó la obsolescencia del snapshot experimental presente en la tesis preliminar. Sin embargo, requiere correcciones antes de la auditoría experimental:

1. el cambio de blob SHA del Plan Maestro en la misma rama/ruta no debe tratarse como bloqueo automático; `SRC-03` es una fuente viva y el SHA se registra como snapshot del corte;
2. los sufijos automáticos de adjuntos como `(3)`/`(4)` no constituyen por sí solos una versión científica distinta;
3. la discrepancia 3,000/1,006 frente a 2,950/1,056 debe mantenerse como snapshot experimental obsoleto, pero no como bloqueo documental porque la precedencia ya la resuelve;
4. debe hacerse explícito que el cambio a v0.2 no fue solo de tamaño: la independencia experimental se garantiza agrupando por DAM, y la tesis preliminar no debe inducir a interpretar la ausencia de IDs repetidos como ausencia de dependencia entre DAM compartidas;
5. el dictamen debe reevaluarse después de esas correcciones.

### Trabajo autorizado ahora

Corregir exclusivamente la entrega de `0A-01` conforme al prompt actualizado y a los cinco puntos anteriores. No iniciar 0A-02 ni Fase 0B.

### Próximo gate

Después de recibir la corrección de 0A-01:

1. revisión científica/editorial interna;
2. si queda en `PASS` o `PASS WITH CORRECTIONS` sin observaciones críticas pendientes, auditoría experimental independiente;
3. resolución de observaciones;
4. aprobación del autor;
5. generación del artefacto bilingüe de GitHub y cierre de 0A-01.

---

## English

### Overall status

- Working branch: `article/main-manuscript`
- Global status: `IN_ANALYSIS`
- Active phase: `0A — Documentary and experimental ground truth`
- Active block: `0A-01 — Documentary ground truth`
- Block status: `REVISION_REQUIRED`
- Active prompt: `article/prompts/0A01_DOCUMENTARY_GROUND_TRUTH.md`
- Target journal: `PENDING — to be decided in Phase 0D`
- Chat language: Spanish
- GitHub artifacts: Spanish + English with semantic equivalence
- Drafted manuscript: not started

### Current dependencies

| Element | Status | Effect on the paper |
|---|---|---|
| Approved thesis project | AVAILABLE_FOR_0A01 | source for problem, objectives, hypotheses, justification, and scope |
| Annex v13 | AVAILABLE_FOR_0A01 | source for current architecture and operational methodology |
| Experimental Master Plan | LIVING_SOURCE_IN_GITHUB | source for current experimental status; use `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` on branch `docs/plan-maestro-temporal-2026-08-31`; current review snapshot `0a9a82181c6c3840f74f0272e5c225568474058b` |
| Current preliminary thesis | AVAILABLE_FOR_0A01 | secondary source for later formulations and stale snapshots; does not govern experimental status |
| Scientific literature | DEFERRED_TO_0B | PDFs will be incorporated in thematic batches during Phase 0B |
| Development GitHub | ACTIVE | source of artifacts and technical status |
| EXP-11B retrieval | PENDING | blocks H150/H200 results |
| EXP-12 | PENDING | blocks part of the final analysis |
| Group 3 | PENDING | blocks final inferential decision for HE2/HE5 |
| Reproducibility repository | STRUCTURAL | to be completed after experimental closure |

### Internal review of 0A-01

The first 0A-01 execution correctly reconstructed the approved formulations and detected the obsolete experimental snapshot in the preliminary thesis. Corrections are required before experimental audit:

1. a changed Master Plan blob SHA at the same branch/path must not be treated as an automatic blocker; `SRC-03` is a living source and its SHA is recorded as the cutoff snapshot;
2. automatic attachment suffixes such as `(3)`/`(4)` do not by themselves define distinct scientific versions;
3. the 3,000/1,006 versus 2,950/1,056 discrepancy must remain identified as a stale experimental snapshot, but it is not a documentary blocker because precedence already resolves it;
4. the move to v0.2 must explicitly reflect DAM-grouped experimental independence; absence of repeated IDs in the preliminary thesis must not be interpreted as absence of dependence from shared DAMs;
5. the verdict must be reassessed after these corrections.

### Work authorized now

Correct only the `0A-01` delivery according to the updated prompt and the five points above. Do not start 0A-02 or Phase 0B.

### Next gate

After the corrected 0A-01 is received:

1. internal scientific/editorial review;
2. if it reaches `PASS` or `PASS WITH CORRECTIONS` with no unresolved critical observations, independent experimental audit;
3. resolve observations;
4. author approval;
5. generate the bilingual GitHub artifact and close 0A-01.
