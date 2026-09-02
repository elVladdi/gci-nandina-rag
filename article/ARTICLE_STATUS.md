# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`
- Estado global: `IN_ANALYSIS`
- Fase activa: `0A — Ground truth documental y experimental`
- Bloque activo: `0A-01 — Ground truth documental`
- Prompt activo: `article/prompts/0A01_DOCUMENTARY_GROUND_TRUTH.md`
- Target journal: `PENDING — se decidirá en Fase 0D`
- Idiomas obligatorios: español + inglés con equivalencia semántica
- Manuscrito redactado: no iniciado

### Dependencias actuales

| Elemento | Estado | Efecto sobre el paper |
|---|---|---|
| Proyecto de tesis aprobado | REQUIRED_FOR_0A01 | fuente para problema, objetivos, hipótesis, justificación y alcance |
| Anexo v13 | REQUIRED_FOR_0A01 | fuente para arquitectura y metodología operativa actual |
| Plan Maestro experimental | AVAILABLE_IN_GITHUB | fuente para estado experimental actual; usar `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` en rama `docs/plan-maestro-temporal-2026-08-31`; equivalente operativo de la copia local v20 |
| Tesis preliminar vigente | REQUIRED_FOR_0A01 | fuente secundaria para identificar formulaciones posteriores y discrepancias |
| Literatura científica | DEFERRED_TO_0B | marco inicial definido; los PDF se incorporarán por lotes en Fase 0B |
| GitHub desarrollo | ACTIVE | fuente de artefactos y estado técnico congelado |
| EXP-11B retrieval | PENDING | bloquea resultados de H150/H200 |
| EXP-12 | PENDING | bloquea parte del análisis definitivo |
| Grupo 3 | PENDING | bloquea decisión inferencial final de HE2/HE5 |
| Repositorio de reproducibilidad | STRUCTURAL | se completará tras cierre experimental |

### Trabajo autorizado ahora

Ejecutar exclusivamente `0A-01 — Ground truth documental` mediante el prompt versionado en `article/prompts/0A01_DOCUMENTARY_GROUND_TRUTH.md`.

Este bloque debe:

1. inventariar las cuatro fuentes nucleares, considerando el Plan Maestro como fuente GitHub y no como adjunto;
2. transcribir las formulaciones aprobadas pertinentes;
3. comparar Proyecto, Anexo, Plan Maestro y tesis preliminar;
4. identificar discrepancias sin armonizarlas silenciosamente;
5. separar formulación aprobada, formulación operativa vigente, borrador preliminar y estado experimental;
6. emitir dictamen `PASS`, `PASS WITH CORRECTIONS` o `BLOCKED`.

No está autorizada todavía la redacción de secciones del manuscrito ni el inicio de Fase 0B.

### Próximo gate

Cerrar `0A-01` y, solo después de su revisión científica/editorial y experimental, abrir `0A-02 — consolidación del estado experimental`.

La Fase 0A completa seguirá requiriendo:

1. inventario verificable de fuentes nucleares;
2. formulación exacta de objetivo general, OE1–OE5 y HE1–HE5;
3. tabla FROZEN / EXECUTED / PENDING;
4. snapshot GitHub de referencia;
5. discrepancias documentales identificadas;
6. claims que ya pueden usarse y claims todavía prohibidos.

---

## English

### Overall status

- Working branch: `article/main-manuscript`
- Global status: `IN_ANALYSIS`
- Active phase: `0A — Documentary and experimental ground truth`
- Active block: `0A-01 — Documentary ground truth`
- Active prompt: `article/prompts/0A01_DOCUMENTARY_GROUND_TRUTH.md`
- Target journal: `PENDING — to be decided in Phase 0D`
- Mandatory languages: Spanish + English with semantic equivalence
- Drafted manuscript: not started

### Current dependencies

| Element | Status | Effect on the paper |
|---|---|---|
| Approved thesis project | REQUIRED_FOR_0A01 | source for problem, objectives, hypotheses, justification, and scope |
| Annex v13 | REQUIRED_FOR_0A01 | source for current architecture and operational methodology |
| Experimental Master Plan | AVAILABLE_IN_GITHUB | source for current experimental status; use `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` on branch `docs/plan-maestro-temporal-2026-08-31`; operational equivalent of the local v20 copy |
| Current preliminary thesis | REQUIRED_FOR_0A01 | secondary source for identifying later formulations and discrepancies |
| Scientific literature | DEFERRED_TO_0B | initial framework defined; PDFs will be incorporated in thematic batches during Phase 0B |
| Development GitHub | ACTIVE | source for artifacts and frozen technical status |
| EXP-11B retrieval | PENDING | blocks H150/H200 results |
| EXP-12 | PENDING | blocks part of the final analysis |
| Group 3 | PENDING | blocks final inferential decision for HE2/HE5 |
| Reproducibility repository | STRUCTURAL | to be completed after experimental closure |

### Work authorized now

Execute only `0A-01 — Documentary ground truth` using the versioned prompt at `article/prompts/0A01_DOCUMENTARY_GROUND_TRUTH.md`.

This block must:

1. inventory the four nuclear sources, treating the Master Plan as a GitHub source rather than an attachment;
2. transcribe the relevant approved formulations;
3. compare the Project, Annex, Master Plan, and preliminary thesis;
4. identify discrepancies without silently harmonizing them;
5. separate approved formulation, current operational formulation, preliminary draft wording, and experimental status;
6. issue a `PASS`, `PASS WITH CORRECTIONS`, or `BLOCKED` verdict.

Drafting manuscript sections and starting Phase 0B are not yet authorized.

### Next gate

Close `0A-01` and, only after its scientific/editorial and experimental review, open `0A-02 — experimental-status consolidation`.

The complete Phase 0A will still require:

1. verifiable inventory of nuclear sources;
2. exact wording of the general objective, OE1–OE5, and HE1–HE5;
3. FROZEN / EXECUTED / PENDING table;
4. reference GitHub snapshot;
5. identified documentary discrepancies;
6. claims that may already be used and claims still prohibited.
