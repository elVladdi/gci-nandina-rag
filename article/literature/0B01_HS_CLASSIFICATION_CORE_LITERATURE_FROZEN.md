# 0B-01 — Literatura núcleo de clasificación HS / Core HS-classification literature

## Español

### 1. Estado

- Bloque: `0B-01 — Clasificación HS directa y aprendizaje supervisado`.
- Estado: **`APPROVED / FROZEN`**.
- Entrega inicial: análisis de ocho PDF primarios por la IA de redacción.
- Revisión científica/editorial interna: **`PASS WITH MINOR CORRECTIONS`**.
- Aprobación expresa del autor: recibida el `2026-09-02`.
- Revisión experimental: no requerida; el lote no modificó hechos/claims experimentales bajo autoridad del flujo experimental.
- Manuscrito: no redactado.
- Novelty/gap final: no definido.

Este artefacto congela el mapa analítico canónico del lote 0B-01. No obliga a citar los ocho trabajos en el manuscrito final; `KEEP_CORE` indica relevancia para el mapa bibliográfico, no obligatoriedad de cita.

### 2. Reglas canónicas de interpretación

1. Toda afirmación atribuida a un paper debe permanecer dentro del alcance que su PDF soporta.
2. `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA` y `NO_VERIFICABLE_EN_PDF` son categorías distintas.
3. Una afirmación que un paper atribuya a un tercero **no se convierte en hecho independiente verificado** para el artículo. Si se necesita como claim factual propio, deberá verificarse la fuente primaria correspondiente.
4. La ausencia de un `group split` equivalente a DAM en un antecedente no demuestra leakage; solo permite afirmar que ese control de independencia no está documentado.
5. Top-k, classification accuracy, weighted F1, recommendation precision ad hoc y accuracy condicionada por rejection no deben homogeneizarse como si fueran la misma métrica.
6. Ningún `CANDIDATE_GAP_ONLY` de este lote constituye novelty ni gap definitivo.

### 3. Matriz canónica de los ocho trabajos

| ID | Trabajo | Tarea / salida | Datos y nivel | Rasgo relevante | Limitación gobernante | Función 0B-01 |
|---|---|---|---|---|---|---|
| P01 | Stassin et al., *Similarity versus Supervision: Best Approaches for HS Code Prediction* | similitud semántica + comparación con clasificación supervisada; Top-k | 95,903 declaraciones; HS6/HS8/HS10 | precedente directo de retrieval histórico y utilidad de Top-k | protocolo de independencia del retrieval no documentado al nivel de un split agrupado; no inferir leakage | `KEEP_CORE` |
| P02 | Shubham, Arya, Roy y Jonnala, *An Ensemble-based Approach for Assigning Text to Correct Harmonized System Code* | clasificación jerárquica + similitud + NER + KG | 232,467 train / 77,490 test; niveles HS2/HS4 y similitud posterior | conocimiento WCO/HS/KG puede influir en selección de candidatos | metadata editorial final no verificable en PDF; muestra de 300 y +16% insuficientemente trazables | `REVIEW_REQUIRED` |
| P03 | Luppes, *Classifying Short Text for the Harmonized System with Convolutional Neural Networks* | clasificación directa | grandes datasets Bills of Lading/Atos; HS2/HS4 | evidencia sobre texto corto, ruido, cardinalidad y CNN | HS6 no evaluado; control por grupos no documentado; labels históricos potencialmente imperfectos | `KEEP_CORE` |
| P04 | Cuaya-Simbro et al., *Automatic Tariff Classification System using Deep Learning* | atributos visuales de café -> mapping tarifario | 200 + 180 imágenes; fracción TIGIE restringida | contraste multimodal/visual | 90% no es accuracy general HS multiclase; muestra y dominio muy restringidos | `KEEP_SUPPORTING` |
| P05 | Pain, *Harmonized System Code Classification Using Transfer Learning with Pre-Trained Weights* | recomendación semántica Top-10 con soporte humano | >30,000 EDI; cuatro shippers; principalmente HS6 | antecedente directo de STS/Top-k/human-assisted recommendation | `UN Comtrade commodity descriptions` = corpus de referencia/nomenclatura para ranking, **no evidencia normativa** equivalente al proyecto actual | `KEEP_CORE` |
| P06 | Anggoro et al., *Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Ranking Loss* | clasificación supervisada con SBERT+MNR y SVM/RF | India 66,522/172 clases; EE.UU. 58,003/112; capítulos 84/85 | baseline moderno de representation learning; LIME local | LIME no equivale a evidencia normativa ni auditabilidad documental; sin group split reportado | `KEEP_CORE` |
| P07 | Ruder, *Application of Machine Learning for Automated HS-6 Code Assignment* | clasificación directa HS6 | 1,124,874 casos; 3,243 clases | baseline ML/DL a gran escala sobre texto ruidoso | conservar `accuracy=0.62` y `weighted F1=0.61` como métricas distintas; labels históricos potencialmente incorrectos | `KEEP_CORE` |
| P08 | Ding, Fan y Chen, *Auto-Categorization of HS Code Using Background Net Approach* | ranking Top-1/2/3 + rejection/manual processing | capítulos 22 y 90; 40,861 y 83,830 tras limpieza | Top-k, rejection y fallback manual; sensibilidad a calidad descriptiva | rejection cambia el subconjunto de decisiones automáticas; jerarquía no operacional en el modelo ejecutado | `KEEP_CORE` |

### 4. Correcciones editoriales congeladas

#### P05 — corpus UN Comtrade

La solución STS usa descripciones de commodities del `UN Comtrade sheet` como **corpus de referencia/nomenclatura para producir ranking por similitud**. No debe etiquetarse como `evidencia normativa` en el sentido funcional del presente proyecto.

#### P02 — conocimiento WCO/HS/KG

P02 incorpora conocimiento derivado de WCO/HS y knowledge graphs durante la selección/recomendación. Debe describirse como **conocimiento de nomenclatura arancelaria usado durante selección de candidatos**. No es equivalente a la arquitectura actual, donde la recuperación normativa ocurre después del ranking histórico y no lo modifica.

P02 conserva estado `REVIEW_REQUIRED`. Año final, venue y DOI no se completan en este freeze porque el PDF disponible mantiene placeholders editoriales y no ofrece evidencia primaria suficiente para cerrarlos.

### 5. Patrones congelados del lote

Solo aplican a estos ocho trabajos:

- el texto comercial corto, ruidoso, abreviado o poco informativo aparece como dificultad en varios antecedentes;
- cardinalidad, long tail, imbalance y calidad de etiquetas condicionan los clasificadores supervisados;
- Top-k y recomendación de candidatos anteceden a los LLM generativos;
- la palabra `accuracy` y métricas afines no se usa de forma homogénea entre papers;
- reconocer la jerarquía HS no equivale a realizar razonamiento/navegación jerárquica durante la inferencia;
- los controles reportados se concentran en duplicados, limpieza, estratificación o leakage de features; este lote no documenta un group split equivalente a DAM;
- disponibilidad de precedentes históricos y confiabilidad/corrección de esos precedentes son dimensiones diferentes;
- explicabilidad local, visualización de embeddings, rationale/KG, Top-k visible o estructura inspeccionable no equivalen automáticamente a auditabilidad documental.

### 6. Candidatos provisionales a gap — NO novelty

Los siguientes permanecen estrictamente `CANDIDATE_GAP_ONLY` hasta completar los lotes posteriores:

- F1: separación funcional entre precedentes históricos para ranking y normativa usada solo como evidencia posterior;
- F2: explicación restringida a un Top-k previamente fijado, sin introducir ni reordenar códigos;
- F3: evaluación explícita de dependencia mediante unidad administrativa/grupo en particiones aduaneras;
- F4: separación evaluativa entre recuperar el código de referencia en Top-k y demostrar corrección sustantiva;
- F5: evaluación de trazabilidad/auditabilidad de evidencia como dimensión distinta del predictive performance.

0B-02 y 0B-03 pueden falsar, debilitar o reformular cualquiera de estos candidatos.

### 7. Fronteras de uso posterior

- No afirmar que Top-k, retrieval histórico, human-in-the-loop, LIME, rejection o conocimiento WCO son individualmente novedosos.
- No comparar porcentajes entre papers sin respetar tarea, nivel HS, denominador, métrica, rejection y esquema de validación.
- No presentar resultados fuera de país/capítulo/nivel como evidencia empírica de generalización a NANDINA Clase 87.
- No usar afirmaciones secundarias como hechos independientes sin verificación primaria.
- No usar P02 como referencia bibliográficamente cerrada mientras permanezca `REVIEW_REQUIRED`.

---

## English

### 1. Status

- Block: `0B-01 — Direct HS classification and supervised learning`.
- Status: **`APPROVED / FROZEN`**.
- Initial delivery: analysis of eight primary PDFs by the drafting AI.
- Internal scientific/editorial review: **`PASS WITH MINOR CORRECTIONS`**.
- Express author approval: received on `2026-09-02`.
- Experimental review: not required because this literature batch did not alter experimental facts or claims under experimental-workflow authority.
- Manuscript drafting: not started.
- Final novelty/gap: not defined.

This artifact freezes the canonical analytical map for 0B-01. It does not require all eight works to be cited in the final manuscript; `KEEP_CORE` denotes relevance to the literature map rather than mandatory citation.

### 2. Canonical interpretation rules

1. Any statement attributed to a paper must remain within what its PDF supports.
2. `REPORTED_BY_AUTHORS`, `CRITICAL_INFERENCE`, and `NOT_VERIFIABLE_IN_PDF` are distinct categories.
3. A statement that a paper attributes to a third party does **not** become an independently verified fact for the manuscript. If needed as an independent factual claim, the corresponding primary source must be verified.
4. Absence of a DAM-equivalent group split in prior work does not prove leakage; it only shows that such an independence control is not documented.
5. Top-k, classification accuracy, weighted F1, ad-hoc recommendation precision, and rejection-conditioned accuracy must not be treated as interchangeable metrics.
6. No `CANDIDATE_GAP_ONLY` item from this batch is a final novelty or gap claim.

### 3. Canonical eight-paper map

| ID | Work | Task/output | Data/level | Relevant feature | Governing limitation | 0B-01 role |
|---|---|---|---|---|---|---|
| P01 | Stassin et al. | semantic similarity + supervised comparison; Top-k | 95,903 declarations; HS6/8/10 | direct precedent for historical retrieval and Top-k | retrieval independence not documented at grouped-split level; do not infer leakage | `KEEP_CORE` |
| P02 | Shubham et al. | hierarchical classification + similarity + NER + KG | 232,467 train / 77,490 test | WCO/HS/KG knowledge may influence candidate selection | final metadata unresolved; 300-case sample and +16% insufficiently traceable | `REVIEW_REQUIRED` |
| P03 | Luppes | direct classification | large Bills of Lading/Atos datasets; HS2/HS4 | short/noisy text, cardinality, CNN | HS6 not evaluated; grouped control not documented; historical labels may be imperfect | `KEEP_CORE` |
| P04 | Cuaya-Simbro et al. | visual attributes -> tariff mapping | 200 + 180 images; restricted TIGIE fraction | multimodal/visual contrast | 90% is not general multiclass HS accuracy; narrow domain/sample | `KEEP_SUPPORTING` |
| P05 | Pain | Top-10 semantic recommendation with human support | >30,000 EDI; four shippers; mainly HS6 | STS/Top-k/human assistance | UN Comtrade descriptions are a ranking reference/nomenclature corpus, not normative evidence equivalent to this project | `KEEP_CORE` |
| P06 | Anggoro et al. | SBERT+MNR supervised classification with SVM/RF | India and US; chapters 84/85 | modern representation-learning baseline; local LIME | LIME is not normative evidence or documentary auditability; no reported group split | `KEEP_CORE` |
| P07 | Ruder | direct HS6 classification | 1,124,874 cases; 3,243 classes | large-scale ML/DL baseline | preserve `accuracy=0.62` vs `weighted F1=0.61`; historical labels may be wrong | `KEEP_CORE` |
| P08 | Ding et al. | Top-1/2/3 ranking + rejection/manual processing | chapters 22/90 | Top-k, rejection, manual fallback | rejection changes automatic-decision subset; hierarchy not operational in executed model | `KEEP_CORE` |

### 4. Frozen editorial corrections

**P05:** UN Comtrade commodity descriptions are a **reference/nomenclature corpus used for similarity ranking**, not normative evidence in the functional sense adopted by this project.

**P02:** WCO/HS/KG-derived information is **tariff-nomenclature knowledge used during candidate selection**, not equivalent to the current architecture's post-ranking normative evidence. P02 remains `REVIEW_REQUIRED`; final year, venue, and DOI are not filled in this freeze.

### 5. Frozen batch patterns

Within these eight works only: short/noisy commercial text is recurrent; cardinality/imbalance/label quality affect supervised models; Top-k recommendation predates generative LLMs; metrics labeled as accuracy are heterogeneous; acknowledging HS hierarchy differs from operational hierarchical reasoning; controls focus on cleaning/duplicates/stratification rather than DAM-equivalent grouping; precedent availability differs from precedent reliability; and local explainability/visible Top-k/rationale do not automatically equal documentary auditability.

### 6. Provisional gap candidates — NOT novelty

F1–F5 remain strictly `CANDIDATE_GAP_ONLY`: functional historical-ranking/normative-evidence separation; fixed Top-k constrained explanation; group-aware dependency control; candidate retrieval vs substantive correctness; and evidence traceability/auditability distinct from predictive performance. Later batches may falsify or reformulate them.

### 7. Downstream-use boundaries

Do not claim Top-k, historical retrieval, human-in-the-loop, LIME, rejection, or WCO knowledge as individually novel; do not compare percentages without respecting task/level/metric/validation/rejection; do not generalize empirically to NANDINA Class 87 from other contexts; do not use secondary claims as independent facts without primary verification; and do not treat P02 as bibliographically closed while `REVIEW_REQUIRED` remains.