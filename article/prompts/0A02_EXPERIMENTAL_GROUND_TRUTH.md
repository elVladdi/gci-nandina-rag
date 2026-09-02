# Prompt 0A-02 — Ground truth experimental / Experimental ground truth

## Español

### Rol

Actúa como IA de redacción y análisis experimental del artículo científico principal. En este bloque **no redactarás ninguna sección del manuscrito** y **no ejecutarás ni modificarás experimentos**. Tu tarea es reconstruir y consolidar el estado experimental verificable que podrá gobernar la redacción posterior.

### Incorporación obligatoria

Accede a la rama `article/main-manuscript` del repositorio `elVladdi/gci-nandina-rag` y comienza por `article/START_HERE.md`.

Después consulta, como mínimo:

1. `article/ARTICLE_STATUS.md`;
2. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
3. `article/SOURCE_REGISTRY.md`;
4. `article/DECISIONS.md`;
5. `article/CLAIM_EVIDENCE_MATRIX.md`;
6. este prompt completo.

Completa el onboarding obligatorio antes de iniciar el análisis.

### Fuentes experimentales obligatorias

#### Fuente viva de estado experimental

Consulta `SRC-03` directamente en GitHub:

- repositorio: `elVladdi/gci-nandina-rag`;
- rama: `docs/plan-maestro-temporal-2026-08-31`;
- ruta: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

Registra el blob SHA efectivamente leído. `SRC-03` es una fuente viva y su contenido puede haber avanzado después de la apertura de este bloque.

#### Repositorio de desarrollo

Consulta directamente `elVladdi/gci-nandina-rag`, principalmente la rama `main`, los commits y los artefactos experimentales versionados necesarios para comprobar el estado real.

Corte de referencia al abrir 0A-02 el 2026-09-02:

- `main`: `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA: `0a9a82181c6c3840f74f0272e5c225568474058b`.

Estos SHA son **snapshots de apertura**, no identidades inmutables. Si al ejecutar 0A-02 alguno cambió, identifica el nuevo SHA, compara el cambio material y determina si afecta el ground truth que estás consolidando. No uses silenciosamente un snapshot antiguo.

### Adjuntos

**No solicites al autor ningún adjunto para 0A-02.** Las fuentes de este bloque están versionadas en GitHub. No solicites nuevamente Proyecto, Anexo, tesis preliminar ni Plan Maestro local.

### Exclusiones

- No realices búsqueda web.
- No analices literatura científica ni abras 0B.
- No redactes Introduction, Related Work, Methods, Results, Discussion, Conclusions, Abstract ni Title.
- No propongas nuevos experimentos, reruns, cambios de diseño o cambios de métricas.
- No modifiques `SRC-03`, el repositorio de desarrollo ni ningún archivo GitHub.
- No conviertas resultados pendientes en hallazgos.
- No declares novelty ni contribución publicable definitiva.

### Objetivo de 0A-02

Construir una **matriz experimental canónica y auditable** que distinga inequívocamente:

1. resultados vigentes y congelados;
2. resultados o snapshots históricos útiles únicamente para explicar la evolución metodológica;
3. experimentos ejecutados pero con alcance limitado;
4. experimentos, análisis o decisiones inferenciales todavía pendientes;
5. claims prohibidos o no autorizados;
6. limitaciones de trazabilidad que deben acompañar cualquier uso posterior de la evidencia.

0A-02 no reemplaza 0A-01. El artefacto congelado de 0A-01 gobierna las formulaciones documentales y la arquitectura; 0A-02 debe concentrarse en el **estado experimental**.

### Vocabulario de estado para esta entrega

Usa únicamente, cuando corresponda:

- `FROZEN_CURRENT`: resultado/artefacto vigente, versionado y apto para ser utilizado dentro de su alcance documentado;
- `EXECUTED_LIMITED`: ejecutado y verificable, pero su interpretación o alcance exige una limitación explícita;
- `HISTORICAL_SNAPSHOT`: estado anterior que no gobierna el benchmark actual;
- `PENDING`: todavía no ejecutado/cerrado o pendiente de análisis/decisión posterior;
- `NOT_AUTHORIZED`: no puede presentarse como resultado o conclusión en el artículo bajo el estado actual;
- `REVIEW_REQUIRED`: existe una observación o cifra cuya trazabilidad/autorización aún no es suficiente.

No inventes estados nuevos. Cuando un artefacto del repositorio use otra etiqueta propia (`CLOSED`, `APPROVED`, `PARTIALLY_SUPPORTED`, etc.), conserva esa etiqueta en una columna separada de **estado original del artefacto** y tradúcela al vocabulario anterior solo para la matriz de 0A-02.

### Verificaciones mínimas obligatorias

Debes verificar directamente, no solo repetir desde `ARTICLE_STATUS.md`, al menos los siguientes componentes:

1. **Benchmark v0.2 vigente**
   - composición de H100, DEV y EVAL;
   - hashes congelados cuando estén disponibles;
   - ausencia de DAM compartidas entre particiones;
   - métricas H100 autorizadas;
   - Top-3 descrito como recuperación de candidatos, no accuracy global.

2. **Snapshot v0.1 y rediseño del split**
   - `3,000/100/1,006` como snapshot histórico;
   - hallazgo `995/1006` con su fuente verificable;
   - `48/59` debe respetar el estado vigente de `C20 = REVIEW_REQUIRED` mientras no exista trazabilidad suficiente;
   - distinguir duplicación/unicidad de `id_unico` de dependencia por DAM.

3. **Resultados base de recuperación**
   - recuperación histórica H100;
   - baseline normativo y su rol como evidencia, no como clasificador sustituto;
   - experimento denso D1a y su alcance exploratorio/limitado;
   - cualquier otro baseline congelado material para las claims existentes.

4. **Integración candidato–evidencia y HE4**
   - verificar el estado de la integración Top-3 + evidencia normativa;
   - distinguir asociación/cobertura de evidencia de corrección normativa sustantiva;
   - consolidar el estado de HE4 con sus límites reales de auditoría y sin convertirlo en corrección jurídica completa.

5. **EXP-08**
   - verificar `outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/exp08_integrated_findings_v0.2.md`;
   - registrar `HE5 = PARTIALLY_SUPPORTED` únicamente como interpretación histórica/intermedia específica de EXP-08;
   - mantener la decisión inferencial final de HE5 como `PENDING` hasta Grupo 3.

6. **Grupo 1 y Grupo 2A**
   - estado de cierre;
   - hallazgos/limitaciones que materialmente condicionan lo que puede afirmarse en el paper;
   - no reinterpretar un cierre operativo como eliminación de todas las limitaciones.

7. **EXP-11A**
   - estado de cierre y versionado;
   - condiciones H25/H50/H75/H100;
   - resultados descriptivos verificables;
   - restricción obligatoria: no inferir efecto causal aislado del tamaño del banco;
   - HE2/HE5 continúan sujetos a la decisión final de Grupo 3.

8. **NEW_HISTORICAL_GATE**
   - Forensic Audit 01;
   - Gate 02 / contrato multi-hoja;
   - limitaciones de procedencia relevantes;
   - distinguir materialización/ingesta de ejecución de retrieval.

9. **EXP-11B**
   - verificar el estado real de `main` y del Bank Materialization Gate;
   - distinguir inequívocamente materialización de bancos de ejecución de retrieval;
   - no reportar H150/H200 como resultados de retrieval mientras estos no existan;
   - si `main` avanzó desde el snapshot de apertura, reconstruir el estado actual sin anticipar conclusiones.

10. **EXP-12, Grupo 2B y Grupo 3**
    - estado actual;
    - dependencias pendientes;
    - qué resultados/decisiones bloquean;
    - HE2/HE5 finales permanecen pendientes salvo evidencia posterior expresamente verificada.

11. **Repositorio de reproducibilidad**
    - solo si es necesario para determinar el estado del protocolo de reproducción/replicación;
    - no confundir estructura reproducible con evidencia de generalización empírica.

### Regla de inferencia y dependencia

`SERIE` es la unidad de análisis. `DAM` es la unidad de agrupamiento cuando existe dependencia. El split v0.2 elimina DAM compartidas entre particiones, pero no convierte automáticamente en independientes a las series de una misma DAM dentro del evalset. Si una conclusión inferencial futura exige independencia, debe respetarse la agrupación por DAM.

No ejecutes inferencia estadística en este bloque.

### Regla sobre resultados y claims

Cruza el resultado de tu reconstrucción contra `article/CLAIM_EVIDENCE_MATRIX.md`.

Para cada discrepancia entre la matriz y la evidencia experimental actual:

- identifica el claim;
- identifica la evidencia exacta;
- explica la discrepancia;
- recomienda `mantener`, `revisar`, `autorizar`, `prohibir` o `dejar pendiente`;
- **no modifiques tú la matriz**.

No autorices por inferencia propia:

- efectos H150/H200 no ejecutados;
- causalidad de EXP-11A;
- corrección normativa sustantiva por mera asociación de evidencia;
- corrección jurídica completa de HE4;
- generalización empírica fuera de Clase 87;
- decisiones finales HE2/HE5 antes de Grupo 3;
- clasificación jurídicamente vinculante.

### Idioma de la respuesta en chat

**Responde únicamente en español.** El bilingüismo obligatorio aplica a los artefactos que posteriormente se integren en GitHub, no a la respuesta del chat.

### Formato de salida obligatorio

#### A. Onboarding y corte verificado

Incluye:

- estado de `0A-01`;
- estado de `0A-02`;
- HEAD de `article/main-manuscript` leído;
- HEAD de `main` leído;
- SHA de `SRC-03` leído;
- cualquier drift detectado respecto del corte de apertura.

#### B. Inventario de evidencia experimental

Tabla:

`ID | experimento/gate/artefacto | ruta/commit | evidencia verificada | estado original | estado 0A-02 | alcance permitido | limitaciones`.

#### C. Benchmark vigente

Tabla separada para H100/DEV/EVAL, hashes, unidades, agrupamiento y métricas autorizadas.

#### D. Matriz cronológica de estado experimental

Desde v0.1 hasta el estado experimental actual. Debe diferenciar explícitamente snapshots históricos, resultados vigentes, gates de materialización y experimentos pendientes.

#### E. Resultados utilizables en el artículo hoy

Lista cerrada de resultados que pueden utilizarse, con alcance exacto y lenguaje permitido.

#### F. Resultados no utilizables todavía

Lista cerrada de resultados/interpretaciones pendientes o prohibidos y la condición necesaria para desbloquearlos.

#### G. Limitaciones experimentales y de trazabilidad

Incluye leakage histórico, dependencia intra-DAM, duplicados/near-duplicates, limitaciones de v0.1, HE4, EXP-11A, procedencia del histórico y cualquier otra limitación material verificada.

#### H. Cruce con `CLAIM_EVIDENCE_MATRIX.md`

Tabla:

`Claim | estado actual de la matriz | evidencia verificada | consistente sí/no | acción recomendada`.

#### I. Bloqueos reales para cerrar 0A-02

Incluye solo problemas que impidan consolidar el ground truth experimental actual. No conviertas experimentos legítimamente pendientes en bloqueo de 0A-02 si su estado `PENDING` puede documentarse correctamente.

#### J. Dictamen

Uno de:

- `PASS`;
- `PASS WITH CORRECTIONS`;
- `BLOCKED`.

Justifica el dictamen brevemente.

### Gate

No avances a 0B ni a ninguna sección del manuscrito. No abras 0A-03 salvo que `ARTICLE_STATUS.md` lo defina posteriormente. La entrega de 0A-02 debe regresar al editor científico para revisión interna y después, cuando el editor lo indique, a la IA experimental para auditoría independiente.

---

## English

### Role

Act as the drafting and experimental-analysis AI for the main scientific article. In this block, **do not draft any manuscript section** and **do not execute or modify experiments**. Your task is to reconstruct and consolidate the verifiable experimental state that may govern later writing.

### Mandatory onboarding

Access the `article/main-manuscript` branch of `elVladdi/gci-nandina-rag` and begin with `article/START_HERE.md`.

Then consult, at minimum:

1. `article/ARTICLE_STATUS.md`;
2. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
3. `article/SOURCE_REGISTRY.md`;
4. `article/DECISIONS.md`;
5. `article/CLAIM_EVIDENCE_MATRIX.md`;
6. this complete prompt.

Complete the mandatory onboarding before starting the analysis.

### Mandatory experimental sources

#### Living experimental-status source

Consult `SRC-03` directly on GitHub:

- repository: `elVladdi/gci-nandina-rag`;
- branch: `docs/plan-maestro-temporal-2026-08-31`;
- path: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

Record the blob SHA actually read. `SRC-03` is a living source and may have advanced after this block was opened.

#### Development repository

Consult `elVladdi/gci-nandina-rag` directly, primarily the `main` branch, commits, and versioned experimental artifacts required to verify the actual state.

Opening reference cutoff on 2026-09-02:

- `main`: `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA: `0a9a82181c6c3840f74f0272e5c225568474058b`.

These SHAs are **opening snapshots**, not immutable identities. If either changed by the time 0A-02 is executed, identify the new SHA, inspect the material change, and determine whether it affects the ground truth being consolidated. Do not silently use an outdated snapshot.

### Attachments

**Do not request any attachment from the author for 0A-02.** The sources for this block are versioned on GitHub. Do not request the Project, Annex, preliminary thesis, or local Master Plan again.

### Exclusions

- Do not perform web searches.
- Do not analyze scientific literature or open 0B.
- Do not draft manuscript sections.
- Do not propose new experiments, reruns, design changes, or metric changes.
- Do not modify `SRC-03`, the development repository, or any GitHub file.
- Do not present pending results as findings.
- Do not declare novelty or a final publishable contribution.

### Objective of 0A-02

Build a **canonical and auditable experimental matrix** that clearly distinguishes:

1. current frozen results;
2. historical snapshots used only to explain methodological evolution;
3. executed experiments with limited interpretation or scope;
4. pending experiments, analyses, or inferential decisions;
5. prohibited or unauthorized claims;
6. traceability limitations that must accompany later use of the evidence.

0A-02 does not replace 0A-01. The frozen 0A-01 artifact governs documentary formulations and architecture; 0A-02 focuses on **experimental status**.

### Status vocabulary for this delivery

Use only, when applicable:

- `FROZEN_CURRENT`: current, versioned result/artifact usable within its documented scope;
- `EXECUTED_LIMITED`: executed and verifiable, but interpretation/scope requires an explicit limitation;
- `HISTORICAL_SNAPSHOT`: prior state that does not govern the current benchmark;
- `PENDING`: not yet executed/closed or awaiting later analysis/decision;
- `NOT_AUTHORIZED`: may not be presented as a result or conclusion under the current state;
- `REVIEW_REQUIRED`: an observation/figure still lacks sufficient traceability or authorization.

Do not invent new states. If a repository artifact uses another native label (`CLOSED`, `APPROVED`, `PARTIALLY_SUPPORTED`, etc.), preserve it in a separate **original artifact status** field and map it to the vocabulary above only for the 0A-02 matrix.

### Minimum mandatory checks

Directly verify, rather than merely repeat from `ARTICLE_STATUS.md`, at least:

1. current v0.2 benchmark composition, hashes, DAM separation, H100 metrics, and candidate-retrieval interpretation;
2. v0.1 snapshot, `995/1006`, `48/59 = C20 REVIEW_REQUIRED`, and the distinction between ID uniqueness and DAM dependence;
3. historical H100 retrieval, normative baseline as evidence rather than substitute classifier, dense D1a as exploratory/limited, and other material frozen baselines;
4. candidate-evidence integration and HE4, distinguishing evidence association/coverage from substantive normative correctness and legal correctness;
5. EXP-08 and historical/intermediate `HE5 = PARTIALLY_SUPPORTED`, while final HE5 remains pending Group 3;
6. Group 1 and Group 2A closure plus material limitations;
7. EXP-11A status, descriptive results, and prohibition on isolated causal bank-size inference;
8. NEW_HISTORICAL_GATE Forensic Audit 01 and Gate 02, including provenance limitations and the distinction between ingestion/materialization and retrieval;
9. EXP-11B materialization versus retrieval, current `main`, and absence of H150/H200 retrieval results unless later evidence proves otherwise;
10. EXP-12, Group 2B, Group 3, and final HE2/HE5 decision status;
11. the reproducibility repository only when needed to establish reproduction/replication protocol status, without converting configurability into empirical generalization.

### Inference and dependence rule

`SERIES` is the analysis unit. `DAM` is the grouping unit when dependence exists. The v0.2 split removes shared DAMs across partitions, but does not automatically make series from the same DAM within the evaluation set independent. Future inference requiring independence must respect DAM grouping.

Do not run statistical inference in this block.

### Results and claims rule

Cross-check your reconstruction against `article/CLAIM_EVIDENCE_MATRIX.md`. For every discrepancy, identify the claim, exact evidence, discrepancy, and recommended action (`maintain`, `review`, `authorize`, `prohibit`, or `leave pending`). **Do not modify the matrix yourself.**

Do not independently authorize:

- unexecuted H150/H200 effects;
- causal interpretation of EXP-11A;
- substantive normative correctness from evidence association alone;
- complete legal correctness of HE4;
- empirical generalization beyond Chapter 87;
- final HE2/HE5 decisions before Group 3;
- legally binding customs classification.

### Chat response language

**Respond only in Spanish.** Mandatory bilingualism applies to artifacts later integrated into GitHub, not to the chat response.

### Mandatory output format

A. Onboarding and verified cutoff.  
B. Experimental-evidence inventory.  
C. Current benchmark.  
D. Chronological experimental-status matrix.  
E. Results usable in the article today.  
F. Results not yet usable.  
G. Experimental and traceability limitations.  
H. Cross-check against `CLAIM_EVIDENCE_MATRIX.md`.  
I. Genuine blockers to closing 0A-02.  
J. Verdict: `PASS`, `PASS WITH CORRECTIONS`, or `BLOCKED`.

### Gate

Do not advance to 0B or any manuscript section. Do not open 0A-03 unless later defined by `ARTICLE_STATUS.md`. Return the 0A-02 delivery to the scientific editor for internal review and, only when the editor requests it, to the experimental AI for independent audit.
