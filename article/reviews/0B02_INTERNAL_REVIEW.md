# Revisión interna 0B-02 / 0B-02 Internal Review

## Español

### BLOQUE REVISADO

- Bloque: `0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera`.
- Entrega revisada: salida analítica de la IA de redacción sobre los seis PDF asignados por `article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`.
- Corte de rama previo a la revisión: `article/main-manuscript` en `8d88164b6d615de7b957fd2b02a376d050464f97`.
- Alcance: verificación científica/editorial independiente contra los seis PDF primarios del lote. No se utilizaron los otros 56 PDF para completar silenciosamente información bibliográfica.

### 1. Fidelidad a fuentes

**PASS WITH MINOR CORRECTIONS**

La entrega reconstruye correctamente las tareas reales, funciones documentales, métodos, métricas y límites principales de los seis trabajos. La taxonomía funcional es científicamente útil porque evita tratar `HS code prediction` como una tarea única y separa clasificación, code retrieval, sentence retrieval, precedent retrieval, correctness assessment, structured knowledge, uncertainty, explainability y human decision support.

Las verificaciones primarias confirman, entre otros puntos:

- P01 utiliza las sentencias recuperadas del manual HS como entrada de la predicción HS6; por tanto, la normativa/documentación recuperada influye en la clasificación final y no funciona únicamente como evidencia posterior.
- P02 es semantic code retrieval; su PDF conserva metadata editorial de plantilla/incompatible y debe permanecer `REVIEW_REQUIRED`.
- P03 separa predicción de candidatos y recuperación posterior de sentencias del manual HS, constituyendo el antecedente funcionalmente más cercano del lote a la separación candidato/evidencia.
- P04 evalúa coherencia/correctness de códigos ya asignados bajo el supuesto explícito de que los códigos históricos son correctos; no dispone de adjudicación independiente de misclasificación real.
- P05 es un estudio cualitativo/practicante con nueve informantes senior y pruebas ilustrativas, no un benchmark predictivo.
- P06 formula una tarea de predicción de código/link completion con knowledge graph; no implementa una capa de evidencia normativa documental posterior al ranking.

### 2. Consistencia experimental

**PASS**

La entrega no modifica el ground truth congelado de 0A ni convierte resultados de literatura en hechos experimentales del proyecto. Mantiene correctamente que:

- ausencia de group split documentado no demuestra leakage;
- un split por triples o registros no equivale a independencia por unidad administrativa;
- Top-k, accuracy, F1, MRR, Hits@k y uncertainty no son métricas intercambiables;
- resultados de Corea, China, Estados Unidos/Europa u otros niveles HS no se transfieren automáticamente a NANDINA Clase 87.

No se requiere revisión de la IA experimental para este cierre bibliográfico, porque ninguna corrección altera hechos, claims o restricciones experimentales congelados.

### 3. Consistencia metodológica

**PASS WITH MINOR CORRECTIONS**

La comparación funcional es correcta y obliga a estrechar varios candidatos heredados de 0B-01:

- **F1** no puede formularse como ausencia de separación entre candidatos y evidencia. P03 ya implementa candidate prediction seguido de HS-manual evidence retrieval, y P01 separa módulos aunque la evidencia recuperada participe en la predicción HS6. El candidato superviviente debe restringirse a la arquitectura específica donde **los precedentes históricos fijan el ranking y la evidencia normativa se recupera únicamente después para documentar candidatos ya fijados, sin modificar el ranking**.
- **F2** debe restringirse a un **generador posterior, controlado sobre un Top-k ya fijado, sin introducir códigos externos ni alterar su orden**. Mostrar varios candidatos, recuperar evidencia o usar un sistema human-in-the-loop no es suficiente para sostener F2.
- **F4** se mantiene metodológicamente fuerte como distinción: candidate retrieval, coherence scoring y correctness sustantivo no son equivalentes.
- **F5** debe estrecharse: P03 y P05 ya incorporan evidencia visible, razonamiento asistivo, authoritative materials y preocupación explícita por auditabilidad. El candidato defendible es una **evaluación formal y separada de trazabilidad/auditabilidad documental mediante protocolo explícito**, no la afirmación amplia de que la literatura carece de auditabilidad.

F3 permanece provisional: el lote no proporciona un antecedente directamente comparable a un control explícito de dependencia por unidad administrativa equivalente a DAM, pero esta supervivencia no constituye novelty.

### 4. Claims y overclaiming

**PASS WITH MINOR CORRECTIONS**

La entrega aplica adecuadamente `SECONDARY_CLAIM_UNVERIFIED` y evita elevar cifras de terceros a ground truth. Deben mantenerse las siguientes restricciones en la versión canónica:

- P02: las posibles reducciones de tiempo de búsqueda o pérdidas financieras se presentan como potenciales/futuras; el propio paper remite su cuantificación a trabajo futuro.
- P03: comentarios sobre reducción de tiempo/esfuerzo son percepciones de usuarios, no un experimento causal de `time-on-task`.
- P04: ≈84.23 % de scores 3–4 no significa que se haya detectado correctamente ese porcentaje de misclasificaciones reales.
- P05: cifras externas de misclasificación u otras magnitudes atribuidas a auditorías/autoridades permanecen secundarias hasta verificar la fuente primaria.
- P06: la afirmación de aproximadamente 30 % de códigos incorrectos es secundaria y no queda validada por este PDF.

### 5. Coherencia argumental

**PASS**

La entrega fortalece el mapa crítico al demostrar que los trabajos del lote ocupan posiciones funcionales diferentes. En especial:

1. candidate ranking y evidence retrieval pueden coexistir, pero la evidencia puede influir o no en la clasificación según el diseño;
2. un sistema explicable no es automáticamente auditable;
3. mostrar una fuente no equivale a demostrar corrección jurídica de la justificación;
4. correctness assessment contra labels históricas no equivale a validación frente a ground truth independiente;
5. human-in-the-loop y múltiples candidatos no equivalen a un contrato de salida rígido como el Top-3 fijo del proyecto actual.

El candidato adicional propuesto por la entrega sobre **ground truth independiente para correctness** puede conservarse como `CANDIDATE_GAP_ONLY`, pero por ahora debe tratarse como una dimensión de validación/metodología y no como contribución o novelty del artículo.

### 6. Estilo científico y procedencia

**PASS**

Se usaron las etiquetas de procedencia exigidas y no se redactaron secciones del manuscrito, ni se declaró novelty, superioridad o gap definitivo. La recomendación `KEEP_CORE` significa relevancia para el mapa y no obligación de cita final.

### 7. Equivalencia español–inglés

**NO APLICA A LA ENTREGA DE CHAT**

La IA de redacción respondió correctamente solo en español. Este registro GitHub se mantiene bilingüe con equivalencia semántica.

### 8. Verificaciones específicas y correcciones obligatorias

#### C1 — P01: denominador experimental y variantes

El abstract indica de forma amplia evaluación sobre 129,084 casos y Top-3 de 95.5 %. El protocolo experimental conserva aproximadamente 126,000 casos tras filtrado y usa como test temporal final **1,652 casos** (1,466 internacionales + 186 coreanos), con **1,835** de validación previa. Además, la tabla distingue:

- sin retrieved sentences: HS6 Top-3 = **0.955**;
- con retrieved sentences: HS6 Top-3 = **0.937**.

La versión canónica debe conservar esta distinción y no describir 95.5 % como resultado del pipeline con sentence retrieval ni 129,084 como denominador efectivo del test final.

#### C2 — P03: contabilidad del dataset no explicada

La tabla de datos informa **17,068 casos coreanos + 209,635 internacionales = 226,703 casos**. El split descrito explícitamente usa **201,435 entrenamiento + 5,000 validación + 5,000 test = 211,435**. Quedan **15,268 registros cuya disposición no se explica explícitamente en el PDF**.

La versión canónica debe registrar esta diferencia como `NO_VERIFICABLE_EN_PDF`; no debe inferir exclusión, duplicación, filtrado ni uso alternativo de esos registros.

#### C3 — P03: encuesta y claims de eficiencia

El cuerpo del paper informa **65.7 %** de respuestas de helpfulness con score 4–5; el `>85 %` corresponde a accuracy percibida con score ≥3. La frase introductoria que atribuye 85 % a “helpful” es internamente inconsistente. Para uso factual debe prevalecer el resultado operativo del cuerpo: 65.7 % para helpfulness 4–5, registrando la discrepancia. No se puede convertir percepción de reducción de esfuerzo/tiempo en medición causal de productividad.

#### C4 — P02, P04 y P06: caveats que deben quedar gobernantes

- **P02 Text2Trade:** conservar `REVIEW_REQUIRED`; no cerrar venue/año/DOI desde placeholders. Registrar que 171,247 + 37,794 = 209,041 frente a “approximately 208,000”, y que el llamado `Generalizability Analysis` usa sectores del mismo reduced test set, por lo que no es validación externa independiente.
- **P04 Spichakova & Haav:** scores 3–4 = 98,463/116,891 ≈ **84.23 %**, pero bajo el supuesto de que los códigos históricos son correctos; no es una estimación de sensibilidad/especificidad frente a misclasificaciones adjudicadas.
- **P06 Qi et al.:** la ecuación impresa de Recall es `TP/(TP+TN)`, definición no convencional. El PDF no permite saber si es error tipográfico o implementación; por ello sus F1 se conservan solo como valores reportados por autores con caveat métrico. La 10-fold CV divide triples aleatoriamente; no demuestra independencia por mercancía/declaración y tampoco autoriza afirmar leakage.

### 9. Estado de F1–F5 después de 0B-02

- **F1:** `CANDIDATE_GAP_ONLY — NARROWED`.
- **F2:** `CANDIDATE_GAP_ONLY — NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
- **F4:** `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — NARROWED`.
- **G6 / independent correctness ground truth:** `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM`.

Todos requieren todavía 0B-03 y, según el tema, 0B-04/0B-05 antes de cualquier cierre en 0C.

### 10. Sugerencias opcionales

1. No es necesaria una nueva ejecución completa de 0B-02 por la IA de redacción. Las correcciones son acotadas y deterministas y pueden integrarse editorialmente al freeze.
2. Text2Trade puede seguir en el mapa pese a `REVIEW_REQUIRED`; ese estado impide cerrar metadata bibliográfica, no analizar el contenido científico del PDF disponible.
3. Antes de una cita final de P03 puede verificarse la versión editorial publicada, pero 0B-02 debe conservar trazabilidad de que analizó específicamente el PDF `arXiv:2311.10922v1`.

### DICTAMEN FINAL

**PASS WITH MINOR CORRECTIONS**

La entrega 0B-02 es científicamente utilizable. Las cuatro correcciones/normalizaciones C1–C4 deben gobernar el artefacto canónico. No se requiere nueva ejecución completa ni revisión experimental.

### CONDICIÓN PARA INTEGRACIÓN

1. Registrar esta revisión y las correcciones C1–C4 como gobernantes del freeze.
2. Obtener **aprobación expresa del autor** de 0B-02 con estas correcciones integradas.
3. Solo después de la aprobación crear/congelar `0B02_..._FROZEN.md`, marcar `0B-02 = APPROVED / FROZEN` y abrir 0B-03.

Hasta entonces:

`0B-02 = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`

---

## English

### REVIEWED BLOCK

- Block: `0B-02 — Retrieval, validation, knowledge, and customs auditability`.
- Reviewed delivery: drafting-AI analytical output covering the six PDFs assigned by `article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`.
- Pre-review branch cutoff: `article/main-manuscript` at `8d88164b6d615de7b957fd2b02a376d050464f97`.
- Scope: independent scientific/editorial verification against the six primary PDFs in the batch; the other 56 PDFs were not used to silently complete bibliographic information.

### 1. Source fidelity

**PASS WITH MINOR CORRECTIONS**

The delivery accurately reconstructs the six papers' real tasks, documentary functions, methods, metrics, and main limitations. Its functional taxonomy is scientifically useful because it separates direct classification, code retrieval, sentence retrieval, precedent retrieval, correctness assessment, structured knowledge, uncertainty, explainability, and human decision support rather than treating `HS code prediction` as one homogeneous task.

Primary-source checks confirm that P01 feeds retrieved HS-manual sentences into HS6 prediction; P02 is semantic code retrieval and retains incompatible/template metadata; P03 explicitly predicts candidates and then retrieves HS-manual evidence; P04 evaluates already-assigned codes while assuming historical codes are correct; P05 is qualitative/practitioner research with nine senior informants and illustrative tests; and P06 is HS-code prediction/link completion over a knowledge graph rather than post-ranking documentary-evidence retrieval.

### 2. Experimental consistency

**PASS**

The delivery does not modify frozen 0A ground truth or turn literature results into experimental facts of the current project. Missing documented group splitting does not prove leakage; record/triple splitting is not equivalent to administrative-unit independence; heterogeneous metrics are not treated as interchangeable; and findings from other jurisdictions or HS scopes are not transferred to NANDINA Chapter 87.

No experimental-AI review is required because these literature corrections do not change frozen experimental facts, claims, or restrictions.

### 3. Methodological consistency

**PASS WITH MINOR CORRECTIONS**

The batch requires narrowing the inherited candidates. F1 must be limited to the specific design in which historical precedents fix candidate ranking and normative evidence is retrieved only afterward without changing that ranking. F2 must be limited to a controlled downstream generator operating on an already fixed Top-k without introducing external codes or changing their order. F4 remains a strong methodological distinction between candidate retrieval, coherence scoring, and substantive correctness. F5 must be limited to a formal, separately evaluated documentary traceability/auditability protocol because P03 and P05 already contain visible evidence, authoritative-source reasoning, and explicit auditability concerns. F3 survives this batch provisionally but is not thereby novel.

### 4. Claims and overclaiming

**PASS WITH MINOR CORRECTIONS**

`SECONDARY_CLAIM_UNVERIFIED` is applied appropriately. The canonical version must preserve that Text2Trade's time/financial benefits are potential/future rather than measured; P03's time/effort reduction evidence is perceptual rather than causal; P04's ≈84.23% of scores 3–4 is not a real-misclassification detection rate; P05's externally sourced quantitative claims remain secondary until their primary sources are checked; and P06's roughly 30% inaccuracy claim is likewise secondary.

### 5. Argumentative coherence

**PASS**

The delivery correctly shows that candidate ranking and evidence retrieval may coexist while evidence can have different causal roles; explainability is not automatically auditability; visible evidence does not prove legal correctness; correctness assessment against historical labels is not independent adjudication; and human-in-the-loop/multiple candidates do not equal a rigid fixed-Top-3 output contract.

The newly proposed independent-ground-truth dimension may remain `CANDIDATE_GAP_ONLY`, but only as a validation/methodological dimension, not as an article contribution or novelty claim.

### 6. Scientific style and provenance

**PASS**

The required provenance labels were used, no manuscript section was drafted, and no definitive novelty, superiority, or gap claim was made. `KEEP_CORE` denotes relevance to the literature map rather than mandatory final citation.

### 7. Spanish–English equivalence

**NOT APPLICABLE TO CHAT DELIVERY**

The drafting AI correctly responded only in Spanish. This GitHub review record is bilingual with semantic equivalence.

### 8. Mandatory checks and corrections

#### C1 — P01: experimental denominator and variants

The abstract broadly refers to 129,084 cases and 95.5% Top-3. The experimental protocol retains about 126,000 cases after filtering and uses a final temporal test of **1,652 cases** (1,466 international + 186 Korean), with **1,835** prior validation cases. The table distinguishes HS6 Top-3 **0.955 without retrieved sentences** from **0.937 with retrieved sentences**. The canonical version must preserve these distinctions and must not describe 95.5% as the sentence-retrieval pipeline result or 129,084 as the final test denominator.

#### C2 — P03: unexplained dataset accounting

The data table reports **17,068 Korean + 209,635 international = 226,703 cases**, while the explicit split uses **201,435 train + 5,000 validation + 5,000 test = 211,435**. The disposition of the remaining **15,268 records is not explicitly explained in the PDF**. The canonical version must mark this as `NOT_VERIFIABLE_IN_PDF` and must not infer filtering, duplication, exclusion, or alternative use.

#### C3 — P03: survey and efficiency claims

The body reports **65.7%** helpfulness ratings of 4–5; `>85%` refers to perceived accuracy rated at least 3. An introductory statement assigning 85% to “helpful” is internally inconsistent. Factual reuse should use the operational body result, 65.7% for helpfulness 4–5, while recording the discrepancy. Perceived reductions in time/effort must not be converted into causal productivity evidence.

#### C4 — governing caveats for P02, P04, and P06

- **P02 Text2Trade:** remain `REVIEW_REQUIRED`; do not resolve venue/year/DOI from placeholders. Record 171,247 + 37,794 = 209,041 against “approximately 208,000,” and treat its sector analysis on the same reduced test set as internal heterogeneity analysis rather than independent external validation.
- **P04 Spichakova & Haav:** scores 3–4 equal 98,463/116,891 ≈ **84.23%**, under the assumption that historical codes are correct; this is not sensitivity/specificity against independently adjudicated misclassification.
- **P06 Qi et al.:** the printed Recall equation is `TP/(TP+TN)`, which is nonstandard. The PDF does not establish whether this is a typographical or implementation error, so F1 values may only be preserved as author-reported values with a metric caveat. Random tenfold CV splits triples; it does not establish commodity/declaration-level independence and does not justify a leakage claim.

### 9. F1–F5 status after 0B-02

- **F1:** `CANDIDATE_GAP_ONLY — NARROWED`.
- **F2:** `CANDIDATE_GAP_ONLY — NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
- **F4:** `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — NARROWED`.
- **G6 / independent correctness ground truth:** `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM`.

All still require later literature batches before any Phase 0C closure.

### 10. Optional suggestions

A full 0B-02 rerun is unnecessary: C1–C4 are bounded, deterministic editorial corrections that can be integrated at freeze. Text2Trade may remain in the literature map while metadata stays `REVIEW_REQUIRED`. If P03 is ultimately cited, its published editorial version may be checked later, while 0B-02 must preserve that its analyzed document was specifically `arXiv:2311.10922v1`.

### FINAL VERDICT

**PASS WITH MINOR CORRECTIONS**

The 0B-02 delivery is scientifically usable after applying C1–C4. No full rerun or experimental review is required.

### INTEGRATION CONDITION

1. Record this review and C1–C4 as governing the canonical freeze.
2. Obtain **explicit author approval** of 0B-02 with these corrections integrated.
3. Only then create/freeze the canonical 0B-02 artifact, mark `0B-02 = APPROVED / FROZEN`, and open 0B-03.

Until then:

`0B-02 = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`
