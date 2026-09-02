# 0A-02 — Ground truth experimental congelado / Frozen experimental ground truth

## Español

### 1. Estado del bloque

- Bloque: `0A-02 — Ground truth experimental`.
- Estado: **`APPROVED / FROZEN`**.
- Fecha de aprobación del autor: `2026-09-02`.
- Revisión científica/editorial interna: `PASS WITH MINOR NORMALIZATION`.
- Auditoría experimental independiente: `PASS WITH MINOR NORMALIZATION — READY FOR AUTHOR APPROVAL`.
- Aprobación expresa del autor: recibida el `2026-09-02`.
- Errores experimentales materiales pendientes al cierre: `0`.
- Normalización aplicada: cada fila de la matriz canónica usa exactamente un estado 0A-02 permitido.

Este artefacto congela el **ground truth experimental verificable del corte 0A-02** para gobernar fases editoriales posteriores. No congela el estado experimental completo de la investigación: experimentos y análisis identificados como `PENDING` continúan abiertos exclusivamente dentro del flujo experimental.

### 2. Corte experimental congelado

El corte verificado por la IA de redacción, la revisión científica/editorial interna y la auditoría experimental independiente fue:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` — Plan Maestro vivo, blob SHA leído: `0a9a82181c6c3840f74f0272e5c225568474058b`;
- sin drift experimental material durante la ejecución y las revisiones de 0A-02.

El SHA de `SRC-03` identifica el snapshot consultado en este corte; no convierte al Plan Maestro en una fuente inmutable. La autoridad de escritura sobre el Plan Maestro permanece exclusivamente en el flujo experimental.

### 3. Vocabulario canónico de estado 0A-02

Cada registro de la matriz experimental utiliza exactamente uno de los siguientes estados:

- `FROZEN_CURRENT`: resultado/artefacto vigente, versionado y utilizable dentro de su alcance documentado;
- `EXECUTED_LIMITED`: ejecutado y verificable, pero de interpretación o alcance limitado;
- `HISTORICAL_SNAPSHOT`: evidencia histórica que no gobierna el benchmark actual;
- `PENDING`: experimento, análisis o decisión todavía no ejecutado/cerrado;
- `NOT_AUTHORIZED`: interpretación o claim no autorizado por la evidencia actual;
- `REVIEW_REQUIRED`: evidencia/cifra cuya trazabilidad o autorización todavía es insuficiente.

No se admiten estados combinados.

### 4. Matriz experimental canónica normalizada

| ID | Evidencia / componente | Fuente principal | Estado 0A-02 | Alcance permitido | Limitaciones obligatorias |
|---|---|---|---|---|---|
| EV-01 | Split v0.2 H100/DEV/EVAL | `outputs/audits/data_aduanas_splits_clase87_v0.2/` | `FROZEN_CURRENT` | diseño del benchmark, independencia entre particiones, validez interna | no implica independencia entre series de una misma DAM dentro de EVAL |
| EV-02 | Recuperación histórica H100 | `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json` | `FROZEN_CURRENT` | ranking principal de candidatos; Top-k y MRR | no denominar accuracy global del sistema/RAG |
| EV-03 | BM25 normativo plano | `exp04_final_results_registry_v0.2.csv` + artefacto normativo plano | `FROZEN_CURRENT` | recuperación documental normativa | no sustituye ni reordena el ranking histórico |
| EV-04 | BM25 normativo jerárquico | `exp04_final_results_registry_v0.2.csv` + artefacto normativo jerárquico | `FROZEN_CURRENT` | recuperación documental normativa a mayor profundidad | no sustituye ni reordena el ranking histórico |
| EV-05 | D1a Text2Trade-inspired MNRL dense retriever | `outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json` | `EXECUTED_LIMITED` | baseline denso específico y exploratorio | no generalizar a dense retrieval en general; D0 legado invalidado |
| EV-06 | Integración histórico–normativa | `outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/` | `FROZEN_CURRENT` | asociación candidato–evidencia, cobertura y trazabilidad; preservación del ranking | asociación documental no equivale a corrección normativa sustantiva |
| EV-07 | Reranker LLM diagnóstico | `outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/` | `EXECUTED_LIMITED` | diagnóstico de muestra de 20 casos | no benchmark, no generalización, sin prueba inferencial preespecificada |
| EV-08 | HE4 — explicación Top-3 y auditoría cualitativa | `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/` | `EXECUTED_LIMITED` | estructura, trazabilidad y auditabilidad bajo el protocolo ejecutado | muestra de 50; evaluador IA; mismatch prompt–schema; no corrección jurídica completa |
| EV-09 | EXP-08 — análisis v0.1 vs v0.2 | `outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/` | `FROZEN_CURRENT` | análisis histórico de sensibilidad y rediseño del split | comparación no causal; evalsets no equivalentes |
| EV-10 | EXP-08 — interpretación `HE5 = PARTIALLY_SUPPORTED` | artefactos EXP-08 | `HISTORICAL_SNAPSHOT` | interpretación intermedia específica de EXP-08 | no sustituye decisión inferencial final de HE5 |
| EV-11 | Decisión inferencial final HE5 | `SRC-03` / Grupo 3 | `PENDING` | ninguna decisión final todavía | debe resolverse en Grupo 3 |
| EV-12 | Grupo 1 — diseño y ejecución experimental | cierre Grupo 1 / EXP-04 | `FROZEN_CURRENT` | estado de cierre de EXP-01…EXP-10 | el cierre no elimina limitaciones preservadas |
| EV-13 | Grupo 2A — reproducibilidad/trazabilidad inicial | `outputs/audits/g2a_reproducibility_v0.1/` | `FROZEN_CURRENT` | cierre de reproducibilidad del corte con limitaciones declaradas | `APPROVED_WITH_NONBLOCKING_LIMITATIONS`, no reproducibilidad perfecta |
| EV-14 | EXP-11A — sensibilidad a tamaño/composición del banco | `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/` | `FROZEN_CURRENT` | análisis descriptivo H25/H50/H75/H100 | no identifica efecto causal aislado del tamaño; tamaño y composición están acoplados |
| EV-15 | Forensic Audit 01 — procedencia histórica | Plan Maestro + artefactos de reconstrucción | `EXECUTED_LIMITED` | reconstrucción forense y procedencia del pipeline | workbook histórico completo no recuperado byte a byte; `PIPELINE_PARTIALLY_RECONSTRUCTED` |
| EV-16 | NEW_HISTORICAL_GATE Gate 02 | `outputs/audits/new_historical_gate_v0.1/` + contrato multi-hoja | `FROZEN_CURRENT` | contrato prospectivo de ingesta y freeze de fuente | equivalencia funcional del contenido procesado no implica identidad binaria del workbook histórico |
| EV-17 | Real Ingest 01 / Gate 03 | `real_ingest_01_freeze_manifest_v0.1.json` y artefactos asociados | `FROZEN_CURRENT` | pool nuevo elegible y diseño prospectivo para EXP-11B | ingesta/materialización no es retrieval |
| EV-18 | EXP-11B Bank Materialization | `outputs/audits/exp11b_bank_materialization_v0.1/` | `FROZEN_CURRENT` | identidad/composición y reproducibilidad de 10 bancos H150 + 10 H200 | materialización no es evaluación de retrieval |
| EV-19 | EXP-11B retrieval H150/H200 | estado `main` + `SRC-03` | `PENDING` | ninguno todavía | `retrieval_executed=false`; no existen métricas autorizadas H150/H200 |
| EV-20 | EXP-12 | `SRC-03` | `PENDING` | ninguno todavía | ejecución/análisis pendiente |
| EV-21 | Grupo 2B | `SRC-03` | `PENDING` | ninguno todavía | depende de EXP-11B/EXP-12 |
| EV-22 | Grupo 3 — métricas/inferencia final | `SRC-03` | `PENDING` | ninguna decisión inferencial final todavía | HE2/HE5 finales permanecen pendientes |
| EV-23 | Split v0.1 `3000/100/1006` | artefactos históricos / EXP-08 | `HISTORICAL_SNAPSHOT` | explicar evolución metodológica | no gobierna benchmark vigente |
| EV-24 | v0.1: `995/1006` casos EVAL con DAM también presentes en histórico | EXP-08 | `HISTORICAL_SNAPSHOT` | hallazgo histórico autorizado para explicar el rediseño del split | no usar como resultado del benchmark v0.2 ni como efecto causal |
| EV-25 | v0.1: `48/59` DAM de evaluación compartidas | claim C20 | `REVIEW_REQUIRED` | no utilizar como hecho congelado | falta trazabilidad versionada suficiente al nivel exigido |

### 5. Benchmark v0.2 vigente

#### 5.1 Composición y hashes

| Partición | Series | DAM | Códigos NANDINA | SHA-256 |
|---|---:|---:|---:|---|
| H100 histórico | 2,950 | 28 | 66 | `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff` |
| DEV | 100 | 6 | 9 | `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00` |
| EVAL | 1,056 | 67 | 42 | `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941` |

Auditoría de independencia entre particiones:

- DAM overlap H100–DEV = `0`;
- DAM overlap H100–EVAL = `0`;
- DAM overlap DEV–EVAL = `0`;
- `id_unico` overlap en los tres pares = `0`.

Interpretación obligatoria:

- `SERIE` = unidad de análisis;
- `DAM` = unidad de agrupamiento cuando existe dependencia.

Cero DAM compartidas entre particiones elimina el solapamiento de una misma declaración entre particiones, pero no convierte automáticamente las 1,056 series de EVAL en observaciones inferencialmente independientes: EVAL contiene 67 DAM.

#### 5.2 Recuperación histórica H100

| Métrica | Resultado |
|---|---:|
| Top-1 | `538/1056 = 0.509469696969697` |
| Top-3 | `709/1056 = 0.6714015151515151` |
| Top-5 | `806/1056 = 0.7632575757575758` |
| Top-10 | `941/1056 = 0.8910984848484849` |
| Top-50 | `1047/1056 = 0.9914772727272727` |
| MRR | `0.6297077493524843` |

El Top-k histórico mide **recuperación de candidatos**: por ejemplo, Top-3 significa que el código de referencia aparece entre los tres candidatos históricos en 709/1,056 casos. No es accuracy global del sistema, del RAG ni del LLM.

#### 5.3 Duplicados y near-duplicates residuales H100–EVAL

- descripción exacta normalizada: `35/1056 = 3.3144 %`;
- near duplicate `>= 0.90`: `55/1056`;
- near duplicate `>= 0.95`: `44/1056`;
- near duplicate `>= 0.98`: `37/1056`.

Estas similitudes textuales se producen entre DAM diferentes y son una dimensión de validez distinta del DAM leakage.

#### 5.4 Concentración por DAM

- H100: DAM mayor `35.42 %`; HHI `≈0.2361`; DAM efectivas `≈4.23`;
- DEV: DAM mayor `91 %`; HHI `0.8302`; DAM efectivas `≈1.20`;
- EVAL: DAM mayor `14.11 %`; HHI `≈0.0624`; DAM efectivas `≈16.02`.

La fuerte concentración de DEV y la concentración de H100 deben conservarse como limitaciones de representatividad/composición.

### 6. Resultados finales consolidados de EXP-04

Los valores gobernantes son los de `outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_results_registry_v0.2.csv`. No deben mezclarse con cifras de snapshots pre-cierre.

#### 6.1 Recuperación normativa

BM25 plano:

- Top-1: `0.027462`;
- Recall@100: `0.071023`;
- MRR@100: `0.042297`.

BM25 jerárquico:

- Top-1: `0.026515`;
- Recall@100: `0.101326`;
- Recall@200: `0.303977`;
- MRR@100: `0.041981`;
- MRR@200: `0.043342`.

Interpretación obligatoria: estos resultados caracterizan **recuperación de evidencia documental normativa**. No convierten a la recuperación normativa en el ranking principal de códigos y no autorizan comparaciones de “accuracy del clasificador” contra el ranking histórico.

#### 6.2 D1a — retriever denso específico

Resultados finales congelados:

- Top-1: `0/1056 = 0`;
- Top-3: `4/1056 = 0.003787878787879`;
- Top-5: `36/1056 = 0.034090909090909`;
- Top-10: `165/1056 = 0.15625`;
- Top-50: `323/1056 = 0.305871212121212`;
- Recall@100: `365/1056 = 0.345643939393939`;
- MRR@100: `0.032424326390346`;
- Recall@200: `383/1056 = 0.362689393939394`;
- MRR@200: `0.032548534776308`.

Uso permitido: baseline denso D1a específico, temprano y exploratorio. No autoriza una conclusión general de superioridad/inferioridad entre BM25 y dense retrieval como familias de métodos.

### 7. Integración candidato–evidencia

Para 1,056 casos × Top-3 fijo = `3,168` slots de candidato:

- evidencia exacta NANDINA-8: `3168/3168`;
- trazabilidad completa: `3168/3168`;
- evidencia exacta para ranks 1, 2 y 3: `1056/1056` en cada rank;
- preservación del ranking/Top-3 histórico: `1.0` en el artefacto de invariancia.

Claim permitido: el pipeline asoció evidencia documental identificable a los tres candidatos históricos y preservó su orden.

Claim prohibido: que `3168/3168` demuestre suficiencia semántica, corrección normativa sustantiva o corrección jurídica de las recomendaciones.

### 8. Reranker LLM diagnóstico

Muestra fija de 20 casos:

- 20 llamadas / 20 casos;
- Top-1 antes: `10/20 = 0.50`;
- Top-1 después: `10/20 = 0.50`;
- Top-3 antes/después: `13/20 = 0.65`;
- `delta_mrr = 0`;
- `19/20` casos registrados como tie en el cierre consolidado;
- sin prueba inferencial preespecificada;
- alcance: `DIAGNOSTIC SAMPLE ONLY`.

No debe presentarse como benchmark ni como evidencia general de que el LLM mejora o no mejora el ranking.

### 9. HE4 — explicación controlada del Top-3

Hechos congelados y verificables:

- muestra: `50` casos;
- explicaciones generadas: `50/50`;
- casos auditables según auditoría cualitativa: `28/50 = 56 %`;
- puntuación media: `11.72`;
- mediana: `12`;
- evaluación cualitativa sin hard violations;
- evaluador: IA en rol experto, no revisor humano independiente;
- estado histórico del experimento: `HE4 = PARTIALLY_SUPPORTED`.

Limitaciones obligatorias:

- `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`;
- `EVALUATOR_MODALITY_DEVIATION`;
- el schema congelado exigía `advertencias_globales` aunque el prompt v0.2 no lo exigía, por lo que el `0/50` de compliance literal quedó confundido por la especificación;
- 50/50 habrían quedado completos si ese campo no evaluable se excluyera; otros errores de schema = `0`;
- las puntuaciones cualitativas son exploratorias.

Uso permitido: evidencia limitada sobre estructura, trazabilidad y auditabilidad bajo el protocolo ejecutado.

No autorizado: afirmar que HE4 demuestra corrección jurídica completa, validez legal del código o corrección normativa sustantiva de la justificación.

### 10. EXP-08 y v0.1

v0.1 se conserva únicamente como `HISTORICAL_SNAPSHOT`:

- split: `3,000` histórico / `100` DEV / `1,006` EVAL;
- `995/1006` casos de EVAL pertenecían a DAM también presentes en histórico: hallazgo histórico autorizado para explicar el rediseño;
- `48/59`: permanece `REVIEW_REQUIRED` y no puede utilizarse como cifra congelada.

EXP-08 está `FROZEN_CURRENT` como análisis histórico de sensibilidad. Sin embargo:

- `HE5 = PARTIALLY_SUPPORTED` de EXP-08 es una interpretación `HISTORICAL_SNAPSHOT` específica de ese experimento;
- la decisión inferencial final de HE5 permanece `PENDING` hasta Grupo 3;
- los deltas v0.1→v0.2 no pueden atribuirse causalmente solo al rediseño del split porque los evalsets no son equivalentes, sus N difieren y la procedencia/metadata de v0.1 es incompleta.

### 11. EXP-11A — sensibilidad descriptiva

EXP-11A está cerrado, aprobado, versionado e integrado. Sus agregados congelados son:

| Condición | Top-3 media ± sd | MRR media ± sd |
|---|---:|---:|
| H25 | `0.645170 ± 0.051964` | `0.603787 ± 0.047775` |
| H50 | `0.597917 ± 0.066393` | `0.542492 ± 0.060405` |
| H75 | `0.463352 ± 0.132774` | `0.414030 ± 0.126668` |
| H100 | `0.671402` | `0.629708` |

Interpretación congelada: **sensibilidad del desempeño de recuperación histórica al tamaño nominal del banco bajo muestreo de DAM completas y restricciones naturales de composición**.

No autorizado: inferir un efecto causal aislado del tamaño del banco. Tamaño, composición por DAM, concentración y cobertura cambian conjuntamente.

### 12. Expansión histórica y EXP-11B

#### 12.1 Procedencia histórica

Forensic Audit 01 se conserva como `EXECUTED_LIMITED`:

- pipeline histórico clasificado `PIPELINE_PARTIALLY_RECONSTRUCTED`;
- H100/DEV/EVAL v0.2 pudieron reproducirse byte a byte desde el contenido procesado disponible;
- el workbook histórico completo no es byte-identificable con el workbook actual.

#### 12.2 Real Ingest 01 / Gate 03

Pool nuevo congelado:

- `6,029` filas elegibles finales;
- `43` DAM;
- `56` NANDINA;
- cero modificación de H100/DEV/EVAL congelados;
- `retrieval_executed = false` en este gate.

#### 12.3 Bank Materialization Gate

- H150 materializados: `10` bancos;
- H200 materializados: `10` bancos;
- total: `20` bancos;
- núcleo H100 preservado en los bancos auditados;
- identidad/composición y hashes registrados.

Conclusión congelada: **los bancos existen y están materializados/auditados; no han sido evaluados mediante retrieval en el corte 0A-02**.

Por tanto:

- `EXP-11B retrieval = PENDING`;
- cualquier métrica H150/H200 = no disponible/no autorizada;
- cualquier dirección del efecto H150/H200 — mejorar, empeorar, estabilizar o no afectar — = `NOT_AUTHORIZED` hasta ejecución, auditoría y freeze del retrieval.

### 13. Pendientes experimentales que el artículo debe respetar

- EXP-11B retrieval: `PENDING`;
- EXP-12: `PENDING`;
- Grupo 2B: `PENDING`;
- Grupo 3: `PENDING`;
- decisión inferencial final HE2: `PENDING`;
- decisión inferencial final HE5: `PENDING`.

Estos estados no bloquean el congelamiento de 0A-02 porque 0A-02 congela **el estado experimental verificable del corte**, no resultados aún inexistentes.

### 14. Claims expresamente no autorizados en este corte

No podrán presentarse como resultados/conclusiones del artículo mientras el estado experimental no cambie mediante el gate correspondiente:

- efecto causal aislado del tamaño del banco a partir de EXP-11A;
- cualquier desempeño, mejora, deterioro, estabilidad o ausencia de efecto de H150/H200;
- decisión final HE2/HE5 antes de Grupo 3;
- corrección normativa sustantiva inferida de la mera asociación candidato–evidencia;
- corrección jurídica completa inferida de HE4;
- reranker de 20 casos presentado como benchmark o generalización;
- deltas v0.1→v0.2 interpretados como efecto causal puro del split;
- generalización empírica fuera de Clase/Capítulo 87;
- clasificación aduanera jurídicamente vinculante.

### 15. Limitaciones congeladas que deben acompañar la redacción posterior

1. Dependencia intra-DAM: EVAL tiene 1,056 series agrupadas en 67 DAM; Grupo 3 deberá respetar la agrupación cuando la inferencia lo requiera.
2. Duplicados/near-duplicates residuales entre H100 y EVAL pese a cero DAM compartidas.
3. Concentración fuerte de H100 y especialmente DEV.
4. v0.1 con dependencia entre particiones y procedencia/metadata incompleta.
5. HE4 limitado por muestra, modalidad de evaluador y mismatch prompt–schema.
6. EXP-11A no causal por acoplamiento tamaño–composición.
7. Procedencia histórica parcialmente reconstruida, no workbook histórico byte-identificable.
8. Grupo 2A cerrado con limitaciones no bloqueantes, no reproducibilidad perfecta.
9. Restricción empírica del piloto a Clase/Capítulo 87.
10. Falta de validación operativa/producción y de clasificación jurídicamente vinculante.

### 16. Efecto del congelamiento

A partir de este cierre:

- `0A-01` gobierna las formulaciones documentales, arquitectura, alcance y precedencia de fuentes;
- `0A-02` gobierna el ground truth experimental del corte y la frontera entre resultados utilizables, limitados, históricos, pendientes y no autorizados;
- cualquier actualización experimental posterior debe ingresar mediante un gate explícito y no reescribir silenciosamente este artefacto histórico;
- el cierre de 0A-02 no autoriza por sí mismo 0B ni la redacción del manuscrito; esa apertura debe registrarse separadamente en `ARTICLE_STATUS.md`.

---

## English

### 1. Block status

- Block: `0A-02 — Experimental ground truth`.
- Status: **`APPROVED / FROZEN`**.
- Author approval date: `2026-09-02`.
- Internal scientific/editorial review: `PASS WITH MINOR NORMALIZATION`.
- Independent experimental audit: `PASS WITH MINOR NORMALIZATION — READY FOR AUTHOR APPROVAL`.
- Express author approval: received on `2026-09-02`.
- Pending material experimental errors at closure: `0`.
- Normalization applied: every canonical-matrix row uses exactly one permitted 0A-02 status.

This artifact freezes the **verifiable experimental ground truth at the 0A-02 cutoff** for subsequent editorial phases. It does not freeze the full experimental state of the research: experiments and analyses identified as `PENDING` remain open exclusively within the experimental workflow.

### 2. Frozen experimental cutoff

The cutoff verified by the drafting AI, internal scientific/editorial review, and independent experimental audit was:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` — living Master Plan, blob SHA read: `0a9a82181c6c3840f74f0272e5c225568474058b`;
- no material experimental drift during 0A-02 execution and review.

The `SRC-03` SHA identifies the snapshot consulted at this cutoff; it does not make the Master Plan immutable. Write authority over the Master Plan remains exclusively within the experimental workflow.

### 3. Canonical 0A-02 status vocabulary

Each experimental-matrix record uses exactly one of:

- `FROZEN_CURRENT`: current, versioned result/artifact usable within its documented scope;
- `EXECUTED_LIMITED`: executed and verifiable but limited in interpretation or scope;
- `HISTORICAL_SNAPSHOT`: historical evidence that does not govern the current benchmark;
- `PENDING`: experiment, analysis, or decision not yet executed/closed;
- `NOT_AUTHORIZED`: interpretation or claim not authorized by current evidence;
- `REVIEW_REQUIRED`: evidence/value whose traceability or authorization remains insufficient.

Combined statuses are not permitted.

### 4. Normalized canonical experimental matrix

| ID | Evidence / component | Primary source | 0A-02 status | Permitted scope | Mandatory limitations |
|---|---|---|---|---|---|
| EV-01 | v0.2 H100/DEV/EVAL split | `outputs/audits/data_aduanas_splits_clase87_v0.2/` | `FROZEN_CURRENT` | benchmark design, cross-partition independence, internal validity | does not imply independence among series from the same DAM within EVAL |
| EV-02 | H100 historical retrieval | `historical_metrics.json` | `FROZEN_CURRENT` | main candidate ranking; Top-k and MRR | do not call overall system/RAG accuracy |
| EV-03 | Flat normative BM25 | final EXP-04 registry + flat normative artifact | `FROZEN_CURRENT` | normative documentary retrieval | does not replace or reorder historical ranking |
| EV-04 | Hierarchical normative BM25 | final EXP-04 registry + hierarchical artifact | `FROZEN_CURRENT` | normative documentary retrieval at greater depth | does not replace or reorder historical ranking |
| EV-05 | D1a Text2Trade-inspired MNRL dense retriever | `d1a_metrics.json` | `EXECUTED_LIMITED` | specific exploratory dense baseline | do not generalize to dense retrieval as a family; legacy D0 invalidated |
| EV-06 | Historical–normative integration | integration artifacts | `FROZEN_CURRENT` | candidate–evidence association, coverage, traceability, rank preservation | documentary association is not substantive normative correctness |
| EV-07 | Diagnostic LLM reranker | reranker artifacts | `EXECUTED_LIMITED` | 20-case diagnostic | not a benchmark or generalizable result; no prespecified inferential test |
| EV-08 | HE4 Top-3 explanation and qualitative audit | HE4 artifacts | `EXECUTED_LIMITED` | structure, traceability, auditability under executed protocol | 50 cases; AI evaluator; prompt–schema mismatch; not complete legal correctness |
| EV-09 | EXP-08 v0.1 vs v0.2 analysis | EXP-08 artifacts | `FROZEN_CURRENT` | historical sensitivity and split-redesign analysis | non-causal comparison; evalsets not equivalent |
| EV-10 | EXP-08 `HE5 = PARTIALLY_SUPPORTED` interpretation | EXP-08 artifacts | `HISTORICAL_SNAPSHOT` | experiment-specific intermediate interpretation | does not replace final inferential HE5 decision |
| EV-11 | Final inferential HE5 decision | `SRC-03` / Group 3 | `PENDING` | no final decision yet | must be resolved in Group 3 |
| EV-12 | Group 1 design/execution closure | Group 1 / EXP-04 closure | `FROZEN_CURRENT` | closure status of EXP-01…EXP-10 | closure does not remove preserved limitations |
| EV-13 | Group 2A initial reproducibility/traceability | G2A artifacts | `FROZEN_CURRENT` | reproducibility closure at cutoff | `APPROVED_WITH_NONBLOCKING_LIMITATIONS`, not perfect reproducibility |
| EV-14 | EXP-11A bank-size/composition sensitivity | EXP-11A artifacts | `FROZEN_CURRENT` | descriptive H25/H50/H75/H100 analysis | does not identify isolated causal bank-size effect |
| EV-15 | Forensic Audit 01 historical provenance | Master Plan + reconstruction artifacts | `EXECUTED_LIMITED` | forensic reconstruction/provenance | historical workbook not recovered byte-for-byte; `PIPELINE_PARTIALLY_RECONSTRUCTED` |
| EV-16 | NEW_HISTORICAL_GATE Gate 02 | new historical gate artifacts | `FROZEN_CURRENT` | prospective ingestion contract/source freeze | functional processed-content equivalence is not binary historical-workbook identity |
| EV-17 | Real Ingest 01 / Gate 03 | freeze manifest and associated artifacts | `FROZEN_CURRENT` | eligible new pool and prospective EXP-11B design | ingestion/materialization is not retrieval |
| EV-18 | EXP-11B Bank Materialization | bank-materialization artifacts | `FROZEN_CURRENT` | identity/composition/reproducibility of 10 H150 + 10 H200 banks | materialization is not retrieval evaluation |
| EV-19 | EXP-11B H150/H200 retrieval | `main` + `SRC-03` status | `PENDING` | none yet | `retrieval_executed=false`; no authorized H150/H200 metrics |
| EV-20 | EXP-12 | `SRC-03` | `PENDING` | none yet | execution/analysis pending |
| EV-21 | Group 2B | `SRC-03` | `PENDING` | none yet | depends on EXP-11B/EXP-12 |
| EV-22 | Group 3 final metrics/inference | `SRC-03` | `PENDING` | no final inferential decisions yet | final HE2/HE5 remain pending |
| EV-23 | v0.1 `3000/100/1006` split | historical artifacts / EXP-08 | `HISTORICAL_SNAPSHOT` | explain methodological evolution | does not govern current benchmark |
| EV-24 | v0.1 `995/1006` EVAL cases from DAMs also in historical | EXP-08 | `HISTORICAL_SNAPSHOT` | authorized historical finding for split redesign | not a v0.2 benchmark result or causal effect |
| EV-25 | v0.1 `48/59` shared EVAL DAM count | claim C20 | `REVIEW_REQUIRED` | do not use as frozen fact | insufficient versioned traceability at required level |

### 5. Current v0.2 benchmark

#### 5.1 Composition and hashes

| Partition | Series | DAM | NANDINA codes | SHA-256 |
|---|---:|---:|---:|---|
| H100 historical | 2,950 | 28 | 66 | `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff` |
| DEV | 100 | 6 | 9 | `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00` |
| EVAL | 1,056 | 67 | 42 | `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941` |

Cross-partition audit: zero DAM overlap and zero `id_unico` overlap in all three partition pairs.

Mandatory interpretation: `SERIES` is the analysis unit and `DAM` is the grouping unit when dependence exists. Zero shared DAMs across partitions removes same-declaration overlap across partitions, but does not make the 1,056 EVAL series automatically inferentially independent because they belong to 67 DAMs.

#### 5.2 H100 historical retrieval

| Metric | Result |
|---|---:|
| Top-1 | `538/1056 = 0.509469696969697` |
| Top-3 | `709/1056 = 0.6714015151515151` |
| Top-5 | `806/1056 = 0.7632575757575758` |
| Top-10 | `941/1056 = 0.8910984848484849` |
| Top-50 | `1047/1056 = 0.9914772727272727` |
| MRR | `0.6297077493524843` |

Historical Top-k measures **candidate retrieval**. It is not overall system, RAG, or LLM accuracy.

#### 5.3 Residual H100–EVAL textual similarity

- exact normalized descriptions: `35/1056 = 3.3144%`;
- near duplicate `>=0.90`: `55/1056`;
- near duplicate `>=0.95`: `44/1056`;
- near duplicate `>=0.98`: `37/1056`.

These occur across different DAMs and are a validity dimension distinct from DAM leakage.

#### 5.4 DAM concentration

- H100: largest DAM `35.42%`; HHI `≈0.2361`; effective DAM `≈4.23`;
- DEV: largest DAM `91%`; HHI `0.8302`; effective DAM `≈1.20`;
- EVAL: largest DAM `14.11%`; HHI `≈0.0624`; effective DAM `≈16.02`.

### 6. Final consolidated EXP-04 results

The governing values are those in `outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_results_registry_v0.2.csv`; earlier pre-closure snapshot values must not be reintroduced.

Flat normative BM25: Top-1 `0.027462`; Recall@100 `0.071023`; MRR@100 `0.042297`.

Hierarchical normative BM25: Top-1 `0.026515`; Recall@100 `0.101326`; Recall@200 `0.303977`; MRR@100 `0.041981`; MRR@200 `0.043342`.

These characterize normative documentary retrieval, not a replacement candidate-ranking classifier.

D1a final frozen metrics: Top-1 `0`; Top-3 `4/1056 = 0.003787878787879`; Top-5 `36/1056 = 0.034090909090909`; Top-10 `165/1056 = 0.15625`; Top-50 `323/1056 = 0.305871212121212`; Recall@100 `365/1056 = 0.345643939393939`; MRR@100 `0.032424326390346`; Recall@200 `383/1056 = 0.362689393939394`; MRR@200 `0.032548534776308`.

D1a is a specific exploratory baseline and cannot support a general family-level conclusion about dense retrieval.

### 7. Candidate–evidence integration

For 1,056 cases × fixed Top-3 = `3,168` candidate slots:

- exact NANDINA-8 evidence: `3168/3168`;
- complete traceability: `3168/3168`;
- exact evidence at ranks 1, 2, and 3: `1056/1056` at each rank;
- historical ranking/Top-3 preservation: `1.0` in invariance artifacts.

Permitted claim: identifiable documentary evidence was linked to all three historical candidates while preserving their order.

Prohibited claim: `3168/3168` establishes semantic sufficiency, substantive normative correctness, or legal correctness.

### 8. Diagnostic LLM reranker

Fixed 20-case sample: 20 calls/20 cases; Top-1 before and after `10/20 = 0.50`; Top-3 before and after `13/20 = 0.65`; `delta_mrr = 0`; `19/20` ties in consolidated closure; no prespecified inferential test; scope `DIAGNOSTIC SAMPLE ONLY`.

It is not a benchmark and does not establish a general effect of LLM reranking.

### 9. HE4 controlled Top-3 explanation

Frozen facts: 50 cases; 50/50 explanations generated; `28/50 = 56%` auditable in qualitative audit; mean score `11.72`; median `12`; no hard violations in qualitative evaluation; AI expert-role evaluator; historical experimental status `HE4 = PARTIALLY_SUPPORTED`.

Mandatory limitations: `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`; `EVALUATOR_MODALITY_DEVIATION`; frozen schema required `advertencias_globales` while prompt v0.2 did not, confounding literal `0/50` schema compliance; 50/50 would otherwise be complete if the non-evaluable field were excluded; other schema errors = `0`; qualitative scores are exploratory.

Permitted use: limited evidence on structure, traceability, and auditability under the executed protocol. It does not establish complete legal or substantive normative correctness.

### 10. EXP-08 and v0.1

v0.1 is historical only: `3000/100/1006`; `995/1006` EVAL cases were from DAMs also present in historical and may be used only as an authorized historical finding explaining split redesign; `48/59` remains `REVIEW_REQUIRED`.

EXP-08 itself is `FROZEN_CURRENT` as a historical sensitivity analysis, while its `HE5 = PARTIALLY_SUPPORTED` interpretation is an experiment-specific `HISTORICAL_SNAPSHOT`. Final inferential HE5 remains `PENDING` until Group 3. v0.1→v0.2 deltas cannot be causally attributed solely to split redesign because the evalsets are not equivalent and v0.1 provenance/metadata are incomplete.

### 11. EXP-11A descriptive sensitivity

| Condition | Top-3 mean ± sd | MRR mean ± sd |
|---|---:|---:|
| H25 | `0.645170 ± 0.051964` | `0.603787 ± 0.047775` |
| H50 | `0.597917 ± 0.066393` | `0.542492 ± 0.060405` |
| H75 | `0.463352 ± 0.132774` | `0.414030 ± 0.126668` |
| H100 | `0.671402` | `0.629708` |

Frozen interpretation: sensitivity of historical retrieval performance to nominal bank size under complete-DAM sampling and natural composition constraints. No isolated causal bank-size effect is authorized because size, DAM composition, concentration, and code coverage change jointly.

### 12. Historical expansion and EXP-11B

Forensic Audit 01 is `EXECUTED_LIMITED`: historical pipeline `PIPELINE_PARTIALLY_RECONSTRUCTED`; v0.2 H100/DEV/EVAL were reproduced byte-for-byte from available processed content, but the full historical workbook was not recovered as a binary-identical source.

Real Ingest 01/Gate 03 froze `6,029` final eligible rows / `43` DAM / `56` NANDINA with no change to frozen H100/DEV/EVAL and `retrieval_executed=false`.

Bank Materialization Gate froze 10 H150 + 10 H200 banks, with preserved H100 core and recorded identity/composition/hashes.

Therefore, at the 0A-02 cutoff: `EXP-11B retrieval = PENDING`; no H150/H200 retrieval metrics exist; no direction of H150/H200 effect is authorized.

### 13. Experimental items still pending

- EXP-11B retrieval: `PENDING`;
- EXP-12: `PENDING`;
- Group 2B: `PENDING`;
- Group 3: `PENDING`;
- final HE2 decision: `PENDING`;
- final HE5 decision: `PENDING`.

These pending items do not block the 0A-02 freeze because 0A-02 freezes the verifiable experimental state at the cutoff, not nonexistent future results.

### 14. Explicitly unauthorized claims at this cutoff

Unauthorized until a later explicit experimental gate changes the evidence state:

- isolated causal bank-size effect from EXP-11A;
- any H150/H200 performance or direction of effect;
- final HE2/HE5 decisions before Group 3;
- substantive normative correctness inferred from candidate–evidence association alone;
- complete legal correctness inferred from HE4;
- 20-case reranker presented as benchmark/generalization;
- v0.1→v0.2 deltas interpreted as a pure causal split effect;
- empirical generalization outside Class/Chapter 87;
- legally binding customs classification.

### 15. Frozen limitations for later writing

1. Intra-DAM dependence within EVAL.
2. Residual duplicates/near-duplicates despite zero shared DAMs.
3. Strong H100 and especially DEV concentration.
4. v0.1 cross-partition dependence and incomplete provenance/metadata.
5. HE4 sample/evaluator/prompt-schema limitations.
6. EXP-11A non-causal size–composition coupling.
7. Partially reconstructed historical provenance, without binary-identical historical workbook.
8. Group 2A closure with nonblocking limitations rather than perfect reproducibility.
9. Empirical restriction to Class/Chapter 87.
10. No operational/production validation and no legally binding classification.

### 16. Effect of freeze

From this closure onward:

- `0A-01` governs documentary formulations, architecture, scope, and source precedence;
- `0A-02` governs the experimental ground truth at this cutoff and the boundary between usable, limited, historical, pending, and unauthorized evidence;
- later experimental updates must enter through an explicit gate and must not silently rewrite this historical artifact;
- closing 0A-02 does not itself authorize 0B or manuscript drafting; that opening must be separately recorded in `ARTICLE_STATUS.md`.