# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase vigente: `0A — Ground truth documental y experimental`.
- `0A-01 — Ground truth documental`: **`APPROVED / FROZEN`**.
- Bloque activo: **ninguno**.
- `0A-02`: **`NOT_STARTED / NOT_YET_OPENED`**.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Idioma del chat: español.
- Artefactos GitHub del entorno del artículo: español + inglés con equivalencia semántica.
- Manuscrito redactado: no iniciado.

### Cierre formal de 0A-01

El bloque 0A-01 completó el ciclo de gobernanza exigido:

1. ejecución documental por la IA de redacción;
2. revisión científica/editorial interna;
3. remediación de observaciones internas;
4. auditoría experimental independiente;
5. remediación de observaciones experimentales;
6. pase experimental final `PASS — READY FOR AUTHOR APPROVAL`;
7. aprobación expresa del autor el 2026-09-02;
8. generación del artefacto documental definitivo y congelado.

Estado final:

```text
0A-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS
EXPERIMENTAL_REVIEW = PASS
AUTHOR_APPROVAL = RECEIVED
```

Artefacto congelado:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

Registros del cierre:

- `article/reviews/0A01_INTERNAL_REVIEW.md`;
- `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`;
- `article/reviews/0A01_AUTHOR_APPROVAL.md`.

### Ground truth congelado por 0A-01

Quedan fijadas para el flujo editorial posterior las siguientes reglas documentales:

- `SRC-01` gobierna las formulaciones aprobadas del problema, objetivos, hipótesis, justificación y alcance;
- `SRC-02` gobierna la arquitectura y metodología operativa vigente;
- `SRC-03` gobierna el estado experimental actual y permanece como fuente viva;
- `SRC-04` es fuente secundaria de comparación y no puede sustituir silenciosamente formulaciones aprobadas ni estado experimental;
- `SERIE` es la unidad de análisis;
- `DAM` es la unidad administrativa original y la unidad de agrupamiento cuando existe dependencia;
- la recuperación histórica genera y ordena candidatos;
- la recuperación normativa aporta evidencia documental y no sustituye el ranking histórico;
- el LLM local explica un Top-3 fijo y no clasifica desde cero ni altera su orden;
- el reranking con LLM es diagnóstico;
- la restricción empírica actual es Clase/Capítulo 87;
- los resultados `3,000/100/1,006` de la tesis preliminar son un snapshot experimental obsoleto;
- `995/1006` permanece autorizado solo como hallazgo histórico v0.1 sobre el rediseño del split;
- `48/59` permanece `REVIEW_REQUIRED`;
- `HE5 = PARTIALLY_SUPPORTED` de EXP-08 es una interpretación histórica/intermedia específica de EXP-08 y no sustituye `HE5 = PENDING_GROUP3`;
- D-011 exige igualdad de contenido textual canónico entre las dos copias del Plan Maestro y limita su escritura exclusivamente a la IA experimental.

### Dependencias experimentales abiertas

| Elemento | Estado | Efecto sobre el artículo |
|---|---|---|
| Plan Maestro experimental | `LIVING_SOURCE_IN_GITHUB / EXPERIMENTAL_WRITE_ONLY` | fuente de estado experimental; la edición y redacción tienen solo lectura |
| Snapshot de `SRC-03` utilizado en 0A-01 | `0a9a82181c6c3840f74f0272e5c225568474058b` | snapshot del corte, no identidad inmutable |
| EXP-11B retrieval | `PENDING` | no existen resultados autorizados de retrieval H150/H200 |
| H150/H200 retrieval results | `NOT_AVAILABLE` | prohibido anticipar mejora, empeoramiento o estabilidad |
| EXP-12 | `PENDING` | bloquea parte del análisis definitivo |
| Grupo 3 | `PENDING` | bloquea decisión inferencial final de HE2/HE5 |
| Repositorio de reproducibilidad | `STRUCTURAL` | se completará según el cierre experimental/publicación |

### Estado de claims relevante

La taxonomía válida continúa siendo:

`AUTHORIZED / CONDITIONAL / PENDING / PROHIBITED / REVIEW_REQUIRED`.

En particular:

- `C19 — 995/1006 = AUTHORIZED` como hallazgo histórico v0.1;
- `C20 — 48/59 = REVIEW_REQUIRED`.

No se autoriza ningún claim nuevo por el mero cierre de 0A-01.

### Trabajo autorizado ahora

El cierre de 0A-01 **no abre automáticamente 0A-02**.

En este corte no está autorizada todavía la ejecución de 0A-02 ni de 0B, ni la redacción de secciones del manuscrito. El siguiente acto editorial será preparar y registrar la apertura formal de `0A-02 — consolidación del ground truth experimental`, con su prompt, fuentes y gate propios.

### Próximo gate

1. preparar el alcance preciso de 0A-02;
2. versionar su prompt en `article/prompts/`;
3. actualizar este archivo para declarar 0A-02 como bloque activo;
4. entregar al autor el prompt operativo y los adjuntos necesarios, si los hubiera;
5. ejecutar 0A-02 sin avanzar a 0B hasta completar su propio ciclo de revisión y aprobación.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global status: `IN_ANALYSIS`.
- Current phase: `0A — Documentary and experimental ground truth`.
- `0A-01 — Documentary ground truth`: **`APPROVED / FROZEN`**.
- Active block: **none**.
- `0A-02`: **`NOT_STARTED / NOT_YET_OPENED`**.
- Target journal: `PENDING — to be decided in Phase 0D`.
- Chat language: Spanish.
- GitHub artifacts in the article workspace: Spanish + English with semantic equivalence.
- Manuscript drafting: not started.

### Formal closure of 0A-01

Block 0A-01 completed the required governance cycle:

1. documentary execution by the drafting AI;
2. internal scientific/editorial review;
3. remediation of internal observations;
4. independent experimental audit;
5. remediation of experimental observations;
6. final experimental pass `PASS — READY FOR AUTHOR APPROVAL`;
7. explicit author approval on 2026-09-02;
8. creation of the definitive frozen documentary artifact.

Final status:

```text
0A-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS
EXPERIMENTAL_REVIEW = PASS
AUTHOR_APPROVAL = RECEIVED
```

Frozen artifact:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

Closure records:

- `article/reviews/0A01_INTERNAL_REVIEW.md`;
- `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`;
- `article/reviews/0A01_AUTHOR_APPROVAL.md`.

### Ground truth frozen by 0A-01

The following documentary rules are fixed for the later editorial workflow:

- `SRC-01` governs approved problem, objective, hypothesis, justification, and scope formulations;
- `SRC-02` governs current operational architecture and methodology;
- `SRC-03` governs current experimental status and remains a living source;
- `SRC-04` is a secondary comparison source and may not silently replace approved formulations or experimental status;
- `SERIES` is the analysis unit;
- `DAM` is the original administrative unit and the grouping unit when dependence matters;
- historical retrieval generates and ranks candidates;
- normative retrieval provides documentary evidence and does not replace the historical ranking;
- the local LLM explains a fixed Top-3 and does not classify from scratch or alter its order;
- LLM reranking is diagnostic;
- current empirical scope is Class/Chapter 87;
- the preliminary-thesis `3,000/100/1,006` results are a stale experimental snapshot;
- `995/1006` remains authorized only as a historical v0.1 finding concerning split redesign;
- `48/59` remains `REVIEW_REQUIRED`;
- EXP-08's `HE5 = PARTIALLY_SUPPORTED` is a historical/intermediate interpretation specific to EXP-08 and does not replace `HE5 = PENDING_GROUP3`;
- D-011 requires equality of canonical textual content between the two Master Plan copies and restricts write authority to the experimental AI.

### Open experimental dependencies

| Element | Status | Effect on the article |
|---|---|---|
| Experimental Master Plan | `LIVING_SOURCE_IN_GITHUB / EXPERIMENTAL_WRITE_ONLY` | experimental-status source; editing and drafting are read-only |
| `SRC-03` snapshot used in 0A-01 | `0a9a82181c6c3840f74f0272e5c225568474058b` | cutoff snapshot, not immutable identity |
| EXP-11B retrieval | `PENDING` | no authorized H150/H200 retrieval results exist |
| H150/H200 retrieval results | `NOT_AVAILABLE` | improvement, deterioration, or stability claims are prohibited |
| EXP-12 | `PENDING` | blocks part of the final analysis |
| Group 3 | `PENDING` | blocks the final inferential HE2/HE5 decision |
| Reproducibility repository | `STRUCTURAL` | to be completed according to experimental/publication closure |

### Relevant claim status

The valid taxonomy remains:

`AUTHORIZED / CONDITIONAL / PENDING / PROHIBITED / REVIEW_REQUIRED`.

In particular:

- `C19 — 995/1006 = AUTHORIZED` as a historical v0.1 finding;
- `C20 — 48/59 = REVIEW_REQUIRED`.

Closing 0A-01 does not itself authorize any new claim.

### Work currently authorized

Closing 0A-01 **does not automatically open 0A-02**.

At this cutoff, execution of 0A-02 or 0B and drafting of manuscript sections are not yet authorized. The next editorial action is to prepare and formally register the opening of `0A-02 — experimental ground-truth consolidation`, with its own prompt, sources, and gate.

### Next gate

1. prepare the precise scope of 0A-02;
2. version its prompt under `article/prompts/`;
3. update this file to declare 0A-02 as the active block;
4. provide the author with the operational prompt and any required attachments;
5. execute 0A-02 without advancing to 0B until its own review and approval cycle is complete.
