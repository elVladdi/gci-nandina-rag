# 0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera / Retrieval, validation, knowledge, and customs auditability

## Español

### 1. Estado

- Bloque: `0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera`.
- Estado: **`APPROVED / FROZEN`**.
- Entrega inicial: análisis completo de seis PDF primarios por la IA de redacción.
- Revisión científica/editorial interna: **`PASS WITH MINOR CORRECTIONS`**.
- Aprobación expresa del autor: **RECIBIDA**.
- Revisión experimental: **`NOT_REQUIRED`**.
- Manuscrito: no redactado.
- Gap definitivo: no definido.
- Novelty: no declarada.

Este artefacto congela el mapa analítico canónico de 0B-02. No obliga a citar todos los trabajos en el manuscrito final. `KEEP_CORE` significa relevancia para el mapa bibliográfico, no obligatoriedad de cita.

### 2. Reglas canónicas de procedencia y uso

1. Distinguir siempre `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`.
2. Una afirmación que un paper atribuya a una fuente tercera no se convierte en hecho independiente del artículo sin verificar la fuente primaria correspondiente.
3. `code retrieval`, `sentence retrieval`, `precedent retrieval`, `evidence retrieval`, clasificación directa y correctness assessment son funciones distintas.
4. Conocimiento de nomenclatura/taxonomía usado para seleccionar o validar un código no equivale a evidencia normativa documental recuperada después de un ranking ya fijado.
5. Explicabilidad model-centric, presencia de fuentes visibles y auditabilidad documental son constructos distintos.
6. La ausencia de `group split` documentado no demuestra leakage.
7. Top-k, accuracy, F1, MRR, Hits@k, uncertainty y scores de correctness no se comparan como métricas homogéneas sin respetar su definición, denominador y protocolo.
8. Ningún candidato a gap de este artefacto constituye novelty definitiva.

### 3. Matriz canónica del lote

| ID | Trabajo | Función real | Hallazgo relevante para el mapa | Caveat gobernante | Función bibliográfica |
|---|---|---|---|---|---|
| P01 | Lee et al., *Classification of Goods Using Text Descriptions With Sentences Retrieval* | clasificación HS4→HS6 + sentence retrieval + precedent retrieval | combina predicción, sentencias del manual HS y precedentes; la documentación recuperada participa en la predicción HS6 | test temporal final = 1,652; validación = 1,835; HS6 Top-3 = 0.955 sin retrieved sentences y 0.937 con retrieved sentences; no atribuir 0.955 al pipeline con sentence retrieval | `KEEP_CORE` |
| P02 | Ravi et al., *Text2Trade* | semantic HS-code retrieval + uncertainty | antecedente directo de Top-k retrieval, MNRL y Monte Carlo Dropout | metadata editorial incompatible/placeholders; `REVIEW_REQUIRED`; 171,247+37,794=209,041 frente a “≈208,000”; análisis sectorial del mismo reduced test no es validación externa | `REVIEW_REQUIRED` |
| P03 | Lee et al., *Explainable Product Classification for Customs* | candidate prediction + HS-manual evidence retrieval + human decision support | antecedente funcionalmente cercano a separar candidatos y evidencia visible | total tabulado = 226,703; split explícito = 211,435; disposición de 15,268 registros = `NO_VERIFICABLE_EN_PDF`; helpfulness operativo 65.7% (score 4–5), no 85%; reducción de tiempo/esfuerzo = percepción, no causalidad | `KEEP_CORE` |
| P04 | Spichakova & Haav, *Application of Machine Learning for Assessment of HS Code Correctness* | correctness/coherence assessment con Doc2Vec + estructura HS | muestra que “correctness” puede significar coherencia respecto de labels históricos | scores 3–4 = 98,463/116,891 ≈84.23%, bajo supuesto de códigos históricos correctos; no mide sensibilidad/especificidad frente a errores jurídicamente adjudicados | `KEEP_CORE` |
| P05 | Grainger, *Customs Tariff Classification and the Use of Assistive Technologies* | estudio cualitativo/practicante sobre tecnología asistiva | explicita authoritative sources, GIR/notas/rulings, file note, auditabilidad y responsabilidad humana | nueve informantes senior; pruebas ilustrativas, no benchmark; cifras externas permanecen `SECONDARY_CLAIM_UNVERIFIED` hasta fuente primaria | `KEEP_CORE` |
| P06 | Qi et al., *Attribute Knowledge and KBGAT...* | direct HS-code prediction/link completion con KG | contraste entre structured knowledge y documentary evidence; CV por triples | ecuación impresa Recall=`TP/(TP+TN)` no convencional; no se puede determinar si es typo o implementación; F1 solo como valor reportado; CV por triples no demuestra independencia por mercancía/declaración ni demuestra leakage | `KEEP_CORE` |

### 4. Correcciones C1–C4 integradas

#### C1 — P01: denominador y variantes

Se congela la separación entre universo disponible/filtrado y evaluación efectiva. El test temporal final contiene **1,652** casos y la validación previa **1,835**. La tabla distingue HS6 Top-3 **0.955 sin retrieved sentences** y **0.937 con retrieved sentences**. No se autoriza describir 95.5% como desempeño del pipeline con sentence retrieval.

#### C2 — P03: contabilidad del dataset

La tabla reporta **17,068 casos coreanos + 209,635 internacionales = 226,703**. El split descrito explícitamente suma **201,435 train + 5,000 validation + 5,000 test = 211,435**. Los **15,268** restantes quedan `NO_VERIFICABLE_EN_PDF`: no se infiere si fueron filtrados, excluidos, duplicados o utilizados en otra etapa.

#### C3 — P03: encuesta y eficiencia

El resultado operativo del cuerpo para helpfulness es **65.7% con puntuación 4–5**. El `>85%` corresponde a otra distribución, asociada a accuracy percibida ≥3. La introducción presenta una inconsistencia interna al usar 85% para helpfulness. Claims de menor tiempo/esfuerzo son percepciones de usuarios y no evidencia causal de productividad.

#### C4 — P02/P04/P06: caveats gobernantes

- P02 permanece `REVIEW_REQUIRED`; no se cierra venue/año/DOI desde placeholders o inferencias. Su “Generalizability Analysis” es heterogeneidad interna por sector, no validación externa.
- P04 no puede citarse como “≈84% de misclasificaciones correctamente detectadas”. Ese 84.23% corresponde a scores 3–4 bajo labels históricos asumidos correctos.
- P06 conserva su F1 únicamente como valor reportado con caveat sobre la fórmula de Recall. La CV por triples no autoriza claims de independencia por mercancía/declaración y tampoco autoriza afirmar leakage.

### 5. Pressure test de los candidatos F1–F5

Después de 0B-02:

- **F1:** `CANDIDATE_GAP_ONLY — NARROWED`.
  - Formulación superviviente: **precedentes históricos recuperados generan/fijan el ranking; evidencia normativa se recupera exclusivamente después para documentar candidatos ya fijados y no modifica el orden**.
  - P03 falsifica la versión amplia “nadie separa candidatos y evidencia”, porque ya existe candidate prediction seguida de HS-manual evidence retrieval.
- **F2:** `CANDIDATE_GAP_ONLY — NARROWED`.
  - Formulación superviviente: **componente generativo posterior que recibe un Top-k fijo y tiene prohibido introducir códigos externos o alterar el orden**.
  - Explicar candidatos o mostrar evidencia no basta para sostener este candidato.
- **F3:** `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
  - Ningún trabajo del lote documenta un control de dependencia directamente comparable a una unidad administrativa equivalente a DAM.
  - Esta supervivencia no constituye novelty.
- **F4:** `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION`.
  - Candidate retrieval, coherence scoring y corrección sustantiva/jurídica no son equivalentes.
- **F5:** `CANDIDATE_GAP_ONLY — NARROWED`.
  - Formulación superviviente: **evaluación formal y separada de trazabilidad/auditabilidad documental mediante protocolo explícito**, no mera existencia de explicaciones, fuentes o preocupación por auditoría.
- **G6:** `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM`.
  - Dimensión provisional: ground truth independiente/adjudicado para evaluación de correctness, separado de labels históricos asumidos correctos.

### 6. Claims secundarios no verificados

Los claims cuantitativos o generales que los seis papers atribuyen a WCO, autoridades, auditorías, prensa, empresas u otras fuentes externas permanecen `SECONDARY_CLAIM_UNVERIFIED` hasta abrir y verificar la fuente primaria. Esto incluye, entre otros, cifras de volumen global de declaraciones, tasas de misclasificación, ahorros económicos y efectos operativos no medidos por el propio estudio.

### 7. Fronteras para uso posterior

- No afirmar que candidate prediction + evidence retrieval es nuevo por sí mismo.
- No afirmar que la literatura aduanera carece de preocupación por auditabilidad: P05 la trata explícitamente y P03 incluye evidencia visible + evaluación humana.
- No convertir human-in-the-loop en novelty.
- No presentar evidence visibility como prueba de corrección jurídica.
- No presentar `correctness score` respecto de labels históricos como ground truth jurídico independiente.
- No extrapolar resultados de otras jurisdicciones, capítulos o granularidades a NANDINA Clase 87.

### 8. Gate siguiente

0B-02 queda **`APPROVED / FROZEN`**. Se autoriza abrir 0B-03, pero 0C permanece bloqueado hasta cerrar toda la Fase 0B.

---

## English

### 1. Status

- Block: `0B-02 — Retrieval, validation, knowledge, and customs auditability`.
- Status: **`APPROVED / FROZEN`**.
- Initial delivery: complete analysis of six primary PDFs by the drafting AI.
- Internal scientific/editorial review: **`PASS WITH MINOR CORRECTIONS`**.
- Express author approval: **RECEIVED**.
- Experimental review: **`NOT_REQUIRED`**.
- Manuscript drafting: not started.
- Final gap: not defined.
- Novelty: not declared.

This artifact freezes the canonical analytical map for 0B-02. `KEEP_CORE` means relevance to the literature map, not mandatory final citation.

### 2. Canonical provenance and use rules

Always distinguish `REPORTED_BY_AUTHORS`, `CRITICAL_INFERENCE`, `NOT_VERIFIABLE_IN_PDF`, and `SECONDARY_CLAIM_UNVERIFIED`; do not promote secondary claims to independent manuscript facts without primary-source verification; do not conflate code/sentence/precedent/evidence retrieval, classification, or correctness assessment; nomenclature/taxonomy knowledge used to select or validate a code is not equivalent to post-ranking documentary normative evidence; model-centric explainability and documentary auditability are distinct; missing grouped splits do not prove leakage; and heterogeneous metrics must not be treated as interchangeable.

### 3. Canonical batch findings

P01 combines HS classification, manual-sentence retrieval, and precedent retrieval; retrieved sentences participate in HS6 prediction. The effective final test is 1,652 cases, with 1,835 prior validation cases; HS6 Top-3 is 0.955 without retrieved sentences and 0.937 with them.

P02/Text2Trade is semantic HS-code retrieval with uncertainty and remains `REVIEW_REQUIRED` because the PDF has incompatible/template metadata. Its split counts sum to 209,041 versus the stated approximately 208,000, and its sector analysis is internal heterogeneity rather than external validation.

P03 explicitly separates candidate prediction and HS-manual evidence retrieval. Its tabulated data total 226,703, while the explicit train/validation/test split totals 211,435; the disposition of 15,268 records is `NOT_VERIFIABLE_IN_PDF`. Operational helpfulness is 65.7% for scores 4–5; >85% refers to another perceived-accuracy distribution, and efficiency claims are perceptual rather than causal.

P04 evaluates coherence/correctness of assigned codes under an explicit assumption that historical codes are correct. Scores 3–4 account for approximately 84.23%, but this is not a true-misclassification detection rate against independently adjudicated labels.

P05 is qualitative/practitioner research with nine senior informants and illustrative tests. It explicitly requires authoritative sources, legal notes/rulings, file notes, auditability, and continued human responsibility, but it is not a predictive benchmark.

P06 is direct HS-code prediction/link completion with structured knowledge. The printed Recall formula is `TP/(TP+TN)`, which is non-standard; F1 values are therefore retained only as author-reported values with a metric caveat. Random triple-level cross-validation neither establishes commodity/declaration independence nor proves leakage.

### 4. Frozen candidate-gap status

- F1: `CANDIDATE_GAP_ONLY — NARROWED` to historical-precedent ranking fixed first, followed only by non-reranking normative evidence retrieval.
- F2: `CANDIDATE_GAP_ONLY — NARROWED` to a downstream generator constrained to a fixed Top-k with no external-code insertion or reordering.
- F3: `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
- F4: `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION` between retrieval/coherence and substantive correctness.
- F5: `CANDIDATE_GAP_ONLY — NARROWED` to formal, separately evaluated documentary traceability/auditability.
- G6: `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM` concerning independent/adjudicated correctness ground truth.

All remain provisional and require later literature batches before Phase 0C.

### 5. Secondary claims

Claims inherited by these papers from third-party sources remain `SECONDARY_CLAIM_UNVERIFIED` until the corresponding primary source is checked.

### 6. Next gate

0B-02 is **`APPROVED / FROZEN`**. Phase 0B may proceed to 0B-03. Phase 0C remains blocked until all required 0B batches are closed.
