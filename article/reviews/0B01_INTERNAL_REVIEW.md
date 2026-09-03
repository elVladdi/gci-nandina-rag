# Revisión interna 0B-01 / 0B-01 Internal Review

## Español

### BLOQUE REVISADO

- Bloque: `0B-01 — Clasificación HS directa y aprendizaje supervisado`.
- Entrega revisada: salida analítica de la IA de redacción sobre los ocho PDF asignados por `article/prompts/0B01_HS_CLASSIFICATION_CORE_LITERATURE.md`.
- Corte de rama previo a la revisión: `article/main-manuscript` en `b6edf4e2eca8f913a0e5d693db9dd83ac7a85852`.
- Alcance de esta revisión: verificación científica/editorial independiente contra los ocho PDF primarios de 0B-01. No se utilizaron los otros 54 documentos del corpus para completar silenciosamente información del lote.

### 1. Fidelidad a fuentes

**PASS WITH MINOR CORRECTIONS**

La reconstrucción de tareas, datasets, métodos, validación, métricas, niveles HS, limitaciones y funciones bibliográficas es sustancialmente fiel a los ocho PDF. Las cifras centrales de P01, P03, P04, P05, P06, P07 y P08 fueron contrastadas con los documentos primarios y no se detectaron errores numéricos que cambien la interpretación del lote.

P02 está correctamente aislado como `REVIEW_REQUIRED`: el PDF disponible conserva placeholders editoriales de plantilla y no permite cerrar de manera segura año final, venue ni DOI. Además, el paper reporta la accuracy comparativa sobre una muestra de 300 observaciones sin documentar suficientemente cómo se seleccionó desde los test sets mayores. Esta incertidumbre no debe resolverse por inferencia ni mediante otra referencia secundaria dentro de 0B-01.

### 2. Consistencia experimental

**PASS**

La entrega no altera el ground truth congelado de 0A y mantiene correctamente que:

- el Top-k histórico del proyecto actual es recuperación de candidatos, no accuracy global del sistema;
- ausencia de group split documentado en un antecedente no equivale a demostrar leakage;
- la comparación con una unidad equivalente a DAM debe formularse como diferencia de control experimental, no como acusación de invalidez de los estudios previos;
- no se extrapolan los resultados de otros capítulos, países o niveles HS a NANDINA Clase 87.

No se requiere intervención de la IA experimental para cerrar esta revisión bibliográfica.

### 3. Consistencia metodológica

**PASS WITH MINOR CORRECTIONS**

Se requieren dos normalizaciones terminológicas para preservar la definición estricta de `evidencia normativa` adoptada por el artículo:

1. **P05 — Pain (2021).** El corpus de la solución STS está formado por descripciones de commodities del `UN Comtrade sheet`, utilizadas como corpus de referencia para producir recomendaciones por similitud. Esto es un **corpus de descripciones de referencia/nomenclatura para ranking**, no evidencia normativa o jurídica recuperada en el sentido funcional del presente proyecto. Las celdas o frases que marcan `Normativa = Sí` para P05 deben reemplazarse por una formulación que explicite esta diferencia.
2. **P02 — Shubham et al.** El paper sí incorpora conocimiento derivado de descripciones/código HS de WCO mediante knowledge graphs y similitud para influir en la selección de candidatos. Debe describirse como **conocimiento WCO/HS o conocimiento de nomenclatura arancelaria usado durante la selección**, no como `evidencia normativa` equivalente al componente posterior y no reordenador del proyecto actual. El contraste funcional de la entrega es correcto; la etiqueta taxonómica debe ser más precisa.

Estas correcciones no cambian la clasificación bibliográfica del lote ni los `CANDIDATE_GAP_ONLY`.

### 4. Claims y overclaiming

**PASS WITH MINOR CORRECTIONS**

La entrega acierta al mantener F1–F5 exclusivamente como `CANDIDATE_GAP_ONLY` y al advertir que Top-k, retrieval histórico, soporte humano, explicación local y conocimiento WCO ya aparecen individualmente en antecedentes.

Debe añadirse una regla de uso para el trabajo posterior: **una afirmación que un paper atribuya a un tercero no se convierte por ello en hecho verificado por 0B-01**. Si el manuscrito necesitara reutilizarla como afirmación factual independiente, deberá verificarse su fuente primaria correspondiente. Esto aplica, entre otros, a cifras de error/misclasificación aduanera o afirmaciones generales de alcance operativo citadas secundariamente por los papers. Se permite describirlas como lo que los autores reportan cuando resulte científicamente pertinente, pero no elevarlas silenciosamente a ground truth.

### 5. Coherencia argumental

**PASS**

La comparación transversal es coherente y útil para la fase posterior 0C. En particular, es correcta la distinción entre:

- clasificación directa y recuperación de candidatos;
- Top-k y corrección sustantiva;
- explicabilidad local y auditabilidad documental;
- uso de conocimiento WCO durante selección y normativa usada únicamente como evidencia posterior;
- control de duplicados/estratificación y control explícito de dependencia por grupos.

Los cinco candidatos a gap deben permanecer provisionales hasta completar, como mínimo, 0B-02 y 0B-03.

### 6. Estilo científico

**PASS**

La entrega utiliza de forma consistente `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA` y `NO_VERIFICABLE_EN_PDF`, evita equiparar métricas heterogéneas y no redacta todavía Related Work ni novelty.

### 7. Equivalencia español–inglés

**NO APLICA A LA ENTREGA DE CHAT**

La salida de la IA de redacción fue correctamente producida solo en español conforme a la política vigente de conversación. Este artefacto GitHub sí se registra de forma bilingüe con equivalencia semántica.

### 8. Terminología y cifras

**PASS WITH MINOR CORRECTIONS**

Verificaciones específicas:

- P08: el mecanismo de `rejection` sí contempla envío a procesamiento manual en §4.2.2; por tanto, `manual fallback` está respaldaldado y no requiere corrección.
- P07: es una **tesis de maestría**, no doctoral. La entrega lo identifica correctamente. Para resultados debe conservarse la distinción `accuracy = 0.62` y `weighted F1 = 0.61`, evitando repetir la expresión ambigua del abstract `weighted accuracy of 61%`.
- P04: el 90 % no debe presentarse como accuracy general de clasificación HS multiclase; la entrega lo limita correctamente a la tarea visual/restringida y al mapping tarifario descrito por los autores.
- P06: la versión disponible es un manuscrito de autor aceptado que identifica la publicación final; esto es suficiente para el análisis del lote.
- P02: la metadata final continúa `REVIEW_REQUIRED` y debe seguir así hasta verificación primaria directa.

### 9. Correcciones obligatorias

1. Normalizar P05 para que `UN Comtrade commodity descriptions` se describa como corpus de referencia/nomenclatura usado para ranking, **no** como evidencia normativa equivalente a la del proyecto actual.
2. Normalizar P02 para distinguir `WCO/HS-derived knowledge used during candidate selection` de la recuperación de evidencia normativa posterior al ranking del proyecto actual.
3. Registrar que las afirmaciones de terceros citadas dentro de los papers no podrán migrar al manuscrito como hechos independientes sin verificar la fuente primaria correspondiente.
4. Mantener P02 en `REVIEW_REQUIRED`; no rellenar año/venue/DOI desde inferencias o fuentes secundarias dentro del cierre de 0B-01.

### 10. Sugerencias opcionales

1. No es necesario devolver el bloque completo a la IA de redacción: las correcciones anteriores son deterministas, acotadas y pueden normalizarse editorialmente al crear el artefacto canónico de 0B-01.
2. La metadata de P02 puede resolverse antes de su eventual incorporación al manuscrito; su estado `REVIEW_REQUIRED` no impide congelar el hallazgo analítico de que el documento fue revisado y presenta las limitaciones indicadas.
3. La selección final de referencias deberá ser más estrecha que `KEEP_CORE`; `KEEP_CORE` significa relevancia para el mapa, no obligación de cita final.

### DICTAMEN FINAL

**PASS WITH MINOR CORRECTIONS**

La entrega 0B-01 es científicamente utilizable después de las cuatro normalizaciones obligatorias anteriores. No se necesita una nueva ejecución analítica completa ni revisión experimental.

### CONDICIÓN PARA INTEGRACIÓN

1. Registrar estas correcciones como gobernantes de la versión canónica de 0B-01.
2. Obtener **aprobación expresa del autor** de 0B-01 con las correcciones integradas.
3. Solo después de esa aprobación, crear/congelar el artefacto canónico de 0B-01, marcar el bloque `APPROVED / FROZEN` y abrir 0B-02.

Hasta entonces, `0B-02` permanece `NOT_STARTED`.

---

## English

### REVIEWED BLOCK

- Block: `0B-01 — Direct HS classification and supervised learning`.
- Reviewed delivery: drafting-AI analytical output covering the eight PDFs assigned by `article/prompts/0B01_HS_CLASSIFICATION_CORE_LITERATURE.md`.
- Pre-review branch cutoff: `article/main-manuscript` at `b6edf4e2eca8f913a0e5d693db9dd83ac7a85852`.
- Review scope: independent scientific/editorial verification against the eight primary PDFs assigned to 0B-01. The other 54 corpus documents were not used to silently complete this batch.

### 1. Source fidelity

**PASS WITH MINOR CORRECTIONS**

The reconstruction of tasks, datasets, methods, validation, metrics, HS levels, limitations, and bibliographic roles is materially faithful to the eight PDFs. Central figures for P01, P03, P04, P05, P06, P07, and P08 were checked against the primary documents, with no numerical error found that changes the interpretation of the batch.

P02 is correctly isolated as `REVIEW_REQUIRED`: the available PDF retains editorial template placeholders and does not safely establish final year, venue, or DOI. It also reports comparative accuracy on a 300-observation sample without sufficiently documenting how that sample was drawn from the larger test sets. This uncertainty must not be resolved by inference or by another secondary reference within 0B-01.

### 2. Experimental consistency

**PASS**

The delivery does not alter frozen 0A ground truth and correctly preserves that historical Top-k in the current project is candidate retrieval rather than global system accuracy; missing documented group splitting in prior work does not prove leakage; comparison with a DAM-equivalent grouping unit must be framed as a difference in experimental control rather than an invalidity claim; and results from other chapters, countries, or HS levels are not extrapolated to NANDINA Chapter 87.

No experimental-AI intervention is required to close this literature review.

### 3. Methodological consistency

**PASS WITH MINOR CORRECTIONS**

Two terminology normalizations are required to preserve the article's strict definition of `normative evidence`:

1. **P05 — Pain (2021).** The STS solution uses commodity descriptions from the `UN Comtrade sheet` as a reference corpus for similarity-based recommendations. This is a **reference/nomenclature description corpus used for ranking**, not retrieved normative or legal evidence in the functional sense adopted by the present project. Cells or statements marking `Normative = Yes` for P05 must be replaced with wording that makes this difference explicit.
2. **P02 — Shubham et al.** The paper does incorporate WCO/HS-derived descriptions and knowledge graphs into similarity and candidate selection. It should be described as **WCO/HS or tariff-nomenclature knowledge used during selection**, not as normative evidence equivalent to the current project's post-ranking, non-reranking evidence component. The functional contrast in the drafting output is correct; the taxonomy label must be more precise.

These corrections do not change bibliographic roles or the `CANDIDATE_GAP_ONLY` items.

### 4. Claims and overclaiming

**PASS WITH MINOR CORRECTIONS**

The delivery correctly keeps F1–F5 strictly as `CANDIDATE_GAP_ONLY` and recognizes that Top-k, historical retrieval, human support, local explanation, and WCO knowledge already occur individually in prior work.

A downstream-use rule must be recorded: **a factual statement that a paper attributes to a third party does not thereby become a fact independently verified by 0B-01**. If the manuscript needs to reuse it as an independent factual claim, the corresponding primary source must be verified. This includes, among others, customs error/misclassification rates or broad operational-scope statements cited secondarily by the papers. Such statements may still be described as author-reported when scientifically relevant, but they may not be silently promoted to ground truth.

### 5. Argumentative coherence

**PASS**

The transversal comparison is coherent and useful for later Phase 0C. In particular, it correctly distinguishes direct classification from candidate retrieval; Top-k from substantive correctness; local explainability from documentary auditability; WCO knowledge used during selection from normative material used solely as post-ranking evidence; and duplicate/stratification controls from explicit group-dependence controls.

All five gap candidates must remain provisional until at least 0B-02 and 0B-03 are complete.

### 6. Scientific style

**PASS**

The delivery consistently uses `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, and `NO_VERIFICABLE_EN_PDF`, avoids equating heterogeneous metrics, and does not yet draft Related Work or declare novelty.

### 7. Spanish–English equivalence

**NOT APPLICABLE TO THE CHAT DELIVERY**

The drafting-AI output was correctly produced only in Spanish under the current conversation-language policy. This GitHub review artifact is bilingual with semantic equivalence.

### 8. Terminology and figures

**PASS WITH MINOR CORRECTIONS**

Specific checks:

- P08: the `rejection` mechanism explicitly sends rejected cases to manual processing in §4.2.2; therefore `manual fallback` is supported.
- P07: this is a **Master's thesis**, not a doctoral thesis. The delivery identifies it correctly. Results should preserve `accuracy = 0.62` versus `weighted F1 = 0.61`, rather than propagate the abstract's ambiguous phrase `weighted accuracy of 61%`.
- P04: the 90% result must not be presented as general multiclass HS-classification accuracy; the delivery correctly limits it to the authors' restricted visual/mapping task.
- P06: the available version is an accepted author manuscript identifying the final publication; this is sufficient for batch analysis.
- P02: final metadata remains `REVIEW_REQUIRED` until direct primary verification.

### 9. Mandatory corrections

1. Normalize P05 so that `UN Comtrade commodity descriptions` are described as a reference/nomenclature corpus used for ranking, **not** as normative evidence equivalent to the current project.
2. Normalize P02 so that `WCO/HS-derived knowledge used during candidate selection` is distinguished from the current project's post-ranking normative-evidence retrieval.
3. Record that third-party statements cited within the papers may not migrate into the manuscript as independent facts without verification of the corresponding primary source.
4. Keep P02 as `REVIEW_REQUIRED`; do not fill year/venue/DOI from inference or secondary sources within the 0B-01 closure.

### 10. Optional suggestions

1. The full block does not need to be returned to the drafting AI: the corrections are deterministic, bounded, and can be editorially normalized when the canonical 0B-01 artifact is created.
2. P02 metadata can be resolved before any eventual manuscript citation; its `REVIEW_REQUIRED` status does not prevent freezing the analytical finding that the document was reviewed and has the stated limitations.
3. Final manuscript selection should be narrower than `KEEP_CORE`; `KEEP_CORE` means relevance to the map, not mandatory final citation.

### FINAL VERDICT

**PASS WITH MINOR CORRECTIONS**

The 0B-01 delivery is scientifically usable after the four mandatory normalizations above. No full analytical rerun or experimental review is required.

### INTEGRATION CONDITION

1. Record these corrections as governing the canonical 0B-01 version.
2. Obtain **explicit author approval** of 0B-01 with the corrections integrated.
3. Only after that approval, create/freeze the canonical 0B-01 artifact, mark the block `APPROVED / FROZEN`, and open 0B-02.

Until then, `0B-02` remains `NOT_STARTED`.
