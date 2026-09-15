# 0C — Gap, contribución y Research Questions / Gap, Contribution, and Research Questions

## Español

### A. Estado reconstruido

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = READY_FOR_DRAFTING
0D = BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
NEW_LITERATURE_SEARCH = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

**ARCHIVOS LEÍDOS:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/0B_PHASE_CLOSURE.md`; `article/reviews/0C_ENTRY_GATE.md`; `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`; freezes `0B-01` a `0B-06`; y, en solo lectura, el Plan Maestro experimental `SRC-03`.

**FASE ACTIVA:** `0C — Gap, contribución y Research Questions`.

**ESTADO DEL BLOQUE ASIGNADO:** `READY_FOR_DRAFTING`.

**REDACCIÓN AUTORIZADA:** sí, exclusivamente para este artefacto analítico de posicionamiento; no está autorizada la redacción de ninguna sección del manuscrito.

**DECISIONES CONGELADAS RELEVANTES:** recuperación histórica = generación/ranking de candidatos; recuperación normativa = evidencia documental posterior que no sustituye ni reordena el ranking histórico; Top-3 fijo antes de generación; LLM local = explicación controlada, no clasificación autónoma; SERIE = unidad de análisis y DAM = unidad de agrupamiento cuando existe dependencia; configurabilidad ≠ generalización empírica; auditabilidad/trazabilidad ≠ corrección jurídica.

**CLAIMS AUTORIZADOS RELEVANTES:** C01–C07, C15, C17, C19 y C21–C25 dentro de sus límites; C14 solo de forma condicional y con las limitaciones de HE4.

**CLAIMS PROHIBIDOS O PENDIENTES RELEVANTES:** C09, C12, C13, C16 y C18 permanecen prohibidos; C20 permanece `REVIEW_REQUIRED`. C10–C11 permanecen formalmente `PROHIBITED` en la Claim–Evidence Matrix aunque el Plan Maestro vivo ya registra EXP-11B como cerrado con resultados descriptivos aprobados; por ello dichos resultados no se utilizan aquí para formular claims del artículo hasta que exista reconciliación editorial explícita de la matriz.

**FUENTES EXTERNAS QUE DEBEN VERIFICARSE:** ninguna. `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED` y 0B está cerrado.

**BLOQUEOS O CONTRADICCIONES DETECTADOS:** no existe contradicción material en la arquitectura o en el estado de apertura de 0C. Existe un desfase de gobernanza entre el snapshot histórico 0A-02/Claim–Evidence Matrix y el estado experimental vivo: `SRC-03` registra EXP-11B cerrado/aprobado/integrado, EXP-12 cerrado sin retrieval por fallo de precondición del planning, Grupo 2B cerrado con limitaciones no bloqueantes y Grupo 3 como siguiente bloque no iniciado. Este desfase no se resuelve por inferencia en este artefacto y no se usa para introducir claims nuevos.

**Snapshot experimental consumido:**

```text
SRC-03 branch = docs/plan-maestro-temporal-2026-08-31
SRC-03 HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
SRC-03 blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
GROUP3 = NOT_STARTED / NEXT
```

**Estado bibliográfico transferido sin modificación:**

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F4 = METHODOLOGICAL_BOUNDARY_NOT_INDEPENDENT_NOVELTY
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
G6 = ELIMINATED_AS_GAP_CANDIDATE
G7 = MERGED_INTO_F2
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
```

Reglas de interpretación aplicadas en todo el artefacto:

`LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.

`ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`.

`ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`.

`AUDITABILITY ≠ LEGAL_CORRECTNESS`.

`CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.

### B. Matriz de transferencia 0A + 0B

| elemento | fuente gobernante | evidencia a favor | evidencia en contra/caveat | estado para 0C | riesgo de overclaiming |
|---|---|---|---|---|---|
| Arquitectura `histórico -> ranking Top-k/Top-3 fijo -> evidencia normativa -> LLM explicativo` | 0A-01; D-005; 0A-02; freezes 0B | arquitectura aprobada y operacional; integración preserva el ranking histórico; el LLM principal no decide el código | la existencia de la arquitectura es una propiedad del proyecto, no prueba novelty | `SUPPORTED_NOW` como diseño del proyecto | MEDIUM si se presenta como novedosa por sí sola |
| F1: ranking histórico fijado antes de evidencia normativa posterior no-reranking | 0B-02, 0B-03A/B, 0B-06 | búsqueda dirigida no encontró match directo dentro del alcance; el proyecto implementa separación estricta y preservación de ranking | Lee et al. ya separan candidate prediction y evidence retrieval; otros sistemas combinan retrieval/reglas/normativa; resultado negativo 0B-06 es acotado | candidato estrecho utilizable solo para posicionamiento | MEDIUM |
| F2: generador exclusivamente explicativo sobre Top-k externo e inmutable | 0B-03B; 0B-06; N01 | el contrato del proyecto prohíbe insertar, eliminar, sustituir, reordenar o retroalimentar clasificación | Wang et al. ya separan una ruta fijada de rationale final; N01 ofrece traces/source support pero su representación participa en predicción/refinamiento | candidato estrecho; `PARTIAL_PRIOR_ART_FOUND` | MEDIUM |
| F3: control de dependencia por unidad administrativa/grupo | 0A-01/02; 0B-01/02/03; 0B-06 | split v0.2 elimina overlap de DAM entre H100/DEV/EVAL; SERIE/DAM están explícitamente diferenciadas | ausencia de grouped split en antecedentes no demuestra leakage ni novelty; near-duplicates cross-DAM persisten; inferencia final debe respetar agrupamiento | principio metodológico/validez, no contribución central por sí solo | LOW si se formula como control; HIGH si se vende como novelty |
| F4: performance/retrieval/path/evidence ≠ corrección sustantiva/jurídica | 0B-02–05C | frontera ampliamente respaldada por literatura y gobernanza | precisamente por estar bien establecida no es novelty independiente | frontera metodológica obligatoria | HIGH si se presenta como contribución novedosa |
| F5: evaluación formal per-output de auditabilidad documental | 0B-02/03/05A; 0B-06; N01 | HE4 ejecuta evaluación por caso con criterios explícitos; el proyecto integra evidencia identificable por candidato | N01 constituye prior art directo en regulatory/legal AI para source-support/audit-oriented traces por instancia; la ausencia general está falsada; HE4 tiene muestra 50, evaluador IA y mismatch prompt–schema | solo puede sobrevivir como componente contextual HS/customs y no como ausencia general | HIGH |
| SERIE/DAM y split v0.2 | 0A-01/02; C06/C07 | 0 DAM compartidas entre H100, DEV y EVAL; EVAL = 1,056 series / 67 DAM | cero overlap entre particiones no implica independencia de las 1,056 series; residual exact/near-duplicate cross-DAM existe | `SUPPORTED_NOW` como control de validez | LOW |
| H100 como candidate retrieval | 0A-02; C04/C05 | Top-1 0.50947; Top-3 709/1056 = 0.67140; Top-5 0.76326; Top-10 0.89110; Top-50 0.99148; MRR 0.62971 | no es accuracy global del sistema/RAG/LLM; concentración H100 y composición limitan interpretación | `SUPPORTED_NOW` | LOW si se denomina correctamente; HIGH si se llama system accuracy |
| Recuperación normativa | 0A-02; 0B-04A/B; 0B-05C | BM25 plano/jerárquico caracterizan retrieval documental; variante jerárquica amplía cobertura a posiciones profundas | su tarea es evidencia, no ranking principal; resultados no son directamente intercambiables con accuracy de clasificación | `SUPPORTED_NOW` dentro de función documental | MEDIUM |
| Integración histórico–normativa | 0A-02 EV-06; C02 | 3,168/3,168 slots con evidencia NANDINA-8 identificable; trazabilidad completa; preservación de ranking 1.0 | asociación/coverage ≠ suficiencia semántica, corrección normativa o legal correctness | `SUPPORTED_NOW` | LOW con límites explícitos |
| Reranker LLM diagnóstico | 0A-02 EV-07 | muestra fija de 20; Top-1 10/20 antes/después; Top-3 13/20 antes/después; delta MRR 0; 19/20 ties | muestra diagnóstica, sin prueba inferencial preespecificada; no benchmark ni evidencia general | `AVAILABLE_WITH_LIMITATION`; no central para contribución | HIGH si se generaliza |
| HE4 / explicación y auditabilidad | 0A-02 EV-08; C14 | 50/50 explicaciones; 28/50 auditables (56%); media 11.72; mediana 12; sin hard violations reportadas | evaluador IA; `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`; `EVALUATOR_MODALITY_DEVIATION`; exploratorio; no legal correctness | `AVAILABLE_WITH_LIMITATION` | HIGH si se presenta como validación jurídica o auditabilidad general |
| Reproducibilidad/provenance | 0B-05A; C17; SRC-03 Grupo 2B | trazabilidad, hashes, lineage y cierre de Grupo 2 con `APPROVED_WITH_NONBLOCKING_LIMITATIONS` | no reproducibilidad perfecta; existen `DECLARED_NOT_RECOVERABLE`, `HASH_BOUND_LOCAL_ONLY` y otras limitaciones preservadas | `SUPPORTED_NOW` como protocolo/estado acotado | MEDIUM |
| 0B-05C / drift normativo | 0B-05C; C21–C25 | drift y scope overlap confirmados; sensibilidad correctiva cerrada; EV03 cero cambio agregado, EV04 disminución MRR muy pequeña no nula, D1a cambio no nulo dependiente del método | no legal correctness, no causalidad, no significancia, no generalización; no resumir como “sin impacto” | `SUPPORTED_NOW` como límite metodológico/documental | HIGH si se simplifica a cero impacto o corrección jurídica |
| EXP-11B vivo vs matriz editorial | SRC-03; Claim–Evidence Matrix | Plan Maestro vivo registra EXP-11B cerrado/aprobado/integrado con resultados descriptivos | C10/C11 aún describen EXP-11B como pendiente y prohíben claims direccionales; 0C no puede corregir la matriz | no usar para claim central ni para cerrar HE2 en este artefacto | HIGH |
| EXP-12 | SRC-03 | disposición metodológica final documentada y auditada | no hubo retrieval; no se materializaron condiciones D-HIGH/D-MID/D-LOW; `EXP12_DIVERSITY_EFFECT_ESTIMABLE=false` | limitación metodológica; no resultado sobre efecto de diversidad | HIGH si se infiere efecto de diversidad |
| Grupo 3 | SRC-03; 0A-01/02 | gate prospectivo definido como siguiente bloque | `NOT_STARTED`; HE2/HE5 finales permanecen pendientes | dependencia explícita para inferencia final | HIGH si se anticipa resultado |

### C. Gap empírico candidato

**Formulación candidata, una oración:** Dentro del corpus HS/customs revisado y de la búsqueda dirigida 2022–2026, permanece limitada la evidencia empírica directamente comparable sobre un piloto que evalúe de forma separada un ranking histórico de candidatos, evidencia normativa recuperada después de fijar ese ranking y una explicación restringida de un Top-3 inmutable bajo un split agrupado por unidad administrativa.

**Evidencia bibliográfica que la permite:** F1 y F3 terminaron 0B-06 como `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`; F2 terminó como `PARTIAL_PRIOR_ART_FOUND`. Los trabajos heredados cubren clasificación directa, retrieval, candidate prediction, evidence retrieval, RAG, agentes, búsqueda jerárquica, knowledge graphs, trazabilidad y explicación, pero no debe equipararse esa cobertura con el contrato completo del proyecto.

**Prior art que la debilita:** Lee et al. ya separan candidate prediction de HS-manual evidence retrieval; Wang et al. separan una ruta jerárquica ya fijada de una fase final de evidence aggregation/rationale; N01 evalúa traces/source support por instancia en regulatory/legal AI; múltiples trabajos usan Top-k, retrieval de precedentes, RAG y reglas aduaneras.

**Evidencia del proyecto relevante:** split v0.2 sin DAM compartidas entre particiones; H100 Top-3 0.67140 y MRR 0.62971 como candidate retrieval; integración de 3,168/3,168 slots con evidencia identificable y ranking preservado; HE4 ejecutado sobre 50 casos con limitaciones explícitas.

- `SUPPORTED_NOW`: existe y fue evaluado un pipeline funcionalmente separado dentro de Clase 87; existen métricas de candidate retrieval, evidence retrieval, integración, trazabilidad y explicación acotada.
- `CONDITIONAL_ON_PENDING_EXPERIMENT`: cualquier cierre inferencial de HE2 o HE5 y cualquier claim estadístico dependiente de Grupo 3; cualquier uso editorial de dirección H150/H200 exige reconciliación previa de C10/C11.
- `NOT_SUPPORTED`: ausencia universal de sistemas equivalentes; superioridad general; generalización fuera de Clase 87; corrección legal del output.

**Condiciones que falsarían/invalidarían la formulación:** identificación de prior art admitido que implemente de forma funcionalmente equivalente las tres capas con ranking histórico externo fijado, evidencia posterior no-reranking y explicación downstream aislada; o evidencia de que la implementación del proyecto permite alterar candidatos desde la capa normativa/generativa.

**Riesgo de overclaiming:** `MEDIUM`.

**Función propuesta en 0C:** puede contribuir al posicionamiento, pero no debe formularse como “no existe trabajo previo” ni como novelty final.

### D. Gap metodológico candidato

**Formulación candidata, una oración:** Un candidato de gap metodológico es la evaluación explícita de un contrato que separa generación de candidatos, evidencia documental y explicación —fijando el ranking histórico antes de la recuperación normativa y aislando al generador de cualquier capacidad clasificatoria— junto con controles de dependencia por unidad administrativa y métricas diferenciadas por función.

**Evidencia bibliográfica que la permite:** F1 sobrevivió en forma estrecha y F2 conserva una diferencia contractual precisa; 0B-04A/04B muestran que candidate generation, reranking, explanation, grounding, provenance y auditability no son funciones intercambiables; F3 sustenta la necesidad metodológica de controlar agrupamiento cuando existen observaciones correlacionadas.

**Prior art que la debilita:** candidate prediction + evidence retrieval ya existe; hierarchical/regulation-driven systems ya fijan rutas antes de rationale final; N01 separa evaluación de explicación de label accuracy pero su trace/program participa en prediction/refinement; group-aware validation es un principio general conocido aunque no se haya encontrado un match directo aduanero dentro del alcance 0B-06.

**Evidencia del proyecto relevante:** invariancia de ranking en integración = 1.0; Top-3 fijo; recuperación normativa no-reranking; LLM principal explanation-only; split por DAM; separación explícita de métricas de candidate retrieval, evidence retrieval y auditabilidad.

- `SUPPORTED_NOW`: el contrato metodológico está documentado e implementado; sus invariantes principales están verificadas.
- `CONDITIONAL_ON_PENDING_EXPERIMENT`: inferencia final sobre HE2/HE5 y cualquier análisis estadístico que Grupo 3 deba cerrar.
- `NOT_SUPPORTED`: que cada componente sea nuevo; que la arquitectura sea automáticamente novedosa; que ningún trabajo anterior separe decisión y explicación.

**Condiciones que falsarían/invalidarían la formulación:** prior art funcionalmente equivalente bajo el mismo aislamiento contractual; hallazgo de feedback clasificatorio o reordenamiento en el flujo oficial del proyecto; o uso de métricas que vuelvan a mezclar candidate retrieval con correctness.

**Riesgo de overclaiming:** `MEDIUM`.

**Función propuesta en 0C:** es la familia más fuerte para articular una contribución candidata, siempre como contrato evaluado y no como declaración de novelty por arquitectura.

### E. Gap de apoyo a decisiones/auditabilidad candidato

**Formulación candidata, una oración:** Como gap contextual y no general, puede evaluarse si en clasificación HS/customs existe espacio para integrar, sobre candidatos ya fijados, evidencia documental identificable y una explicación controlada cuya auditabilidad se examine por caso sin convertir source support en corrección jurídica.

**Evidencia bibliográfica que la permite:** la literatura aduanera revisada contiene preocupación por evidencia, trazabilidad, file notes, paths, citations y decision support; el proyecto añade una integración explícita con Top-3 fijo y HE4 a nivel de caso.

**Prior art que la debilita:** F5 = `DIRECT_PRIOR_ART_FOUND`; N01 evalúa source support/audit-oriented traces por instancia en regulatory/legal AI; P03 presenta evidencia visible y evaluación humana; P05 trata explícitamente auditabilidad y fuentes autoritativas; ICCA-RAG y sistemas agentic aportan provenance/traceability aunque no sean equivalentes a HE4.

**Evidencia del proyecto relevante:** 3,168/3,168 slots con evidencia identificable, preservación de ranking, 50 explicaciones HE4, 28/50 auditables en auditoría cualitativa.

- `SUPPORTED_NOW`: el proyecto implementa apoyo documental por candidato y ejecutó una evaluación acotada de auditabilidad/estructura.
- `CONDITIONAL_ON_PENDING_EXPERIMENT`: cualquier síntesis final de HE5 o inferencia estadística relacionada con validez; cualquier ampliación de HE4 más allá del protocolo ejecutado.
- `NOT_SUPPORTED`: que regulatory AI carezca de evaluación de auditabilidad/source support; que HE4 demuestre legal correctness; que 56% sea una tasa generalizable de auditabilidad del sistema.

**Condiciones que falsarían/invalidarían la formulación:** tratar F5 general como ausencia; ignorar N01; presentar source support como suficiencia jurídica; o elevar HE4 más allá de su muestra/protocolo.

**Riesgo de overclaiming:** `HIGH`.

**Función propuesta en 0C:** mejor como componente contextual de la contribución y de la evaluación, no como gap independiente principal.

### F. Alternativas A/B/C de contribución central

#### A — Conservadora / mínima defendible

**Estado:** `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

**Formulación:** El artículo puede contribuir con una evaluación acotada de un piloto offline para recomendación de subpartidas NANDINA que mide separadamente la recuperación histórica de candidatos, la asociación posterior de evidencia normativa y la explicación controlada de un Top-3 fijo, bajo un split por DAM y con trazabilidad documental explícita. La contribución se limita al diseño evaluado en Clase 87 y a las métricas realmente ejecutadas.

**Cadena lógica:** problema de recomendación auditable -> literatura heterogénea con tareas y métricas no equivalentes -> evaluación de componentes diferenciados -> H100 + retrieval normativo + integración + HE4 -> evidencia empírica delimitada sin claims de novelty universal.

**Componentes diferenciadores:** evaluación integrada pero funcionalmente desagregada; Top-3 fijo; split por DAM; evidencia posterior por candidato; límites explícitos entre retrieval, auditabilidad y correctness.

**Componentes que son prior art:** Top-k, historical retrieval, BM25, semantic retrieval, RAG, human decision support, evidencia visible, LLM para clasificación/explicación, provenance y audit trails.

**Evidencia requerida:** C01–C07, C14 con caveats, integración EV-06, HE4 EV-08, freezes 0B y Grupo 2B.

**Resultados pendientes que podrían debilitarla:** Grupo 3 puede modificar la interpretación inferencial de HE2/HE5, pero no invalida la existencia del pipeline ni sus resultados ya congelados.

**Relación con F1–F5:** usa F1/F2 solo para contextualizar; incorpora F3 como validez; usa F4 como frontera; no depende de F5 general.

**Riesgo:** `LOW`.

**Afirmaciones prohibidas:** “primero”, “único”, “sin prior art”, accuracy global del RAG, corrección jurídica, generalización fuera de Clase 87, causalidad de tamaño de banco.

#### B — Arquitectónica-metodológica

**Estado:** `RECOMMENDED_FOR_EDITORIAL_REVIEW`.

**Formulación:** El artículo puede contribuir mediante la formalización y evaluación de un contrato arquitectónico-metodológico en el que la recuperación histórica fija el ranking de candidatos, la recuperación normativa solo documenta esos candidatos y un LLM local downstream explica un Top-3 inmutable sin capacidad de insertar, eliminar, sustituir, reordenar ni retroalimentar la clasificación. La evaluación acompaña ese contrato con particiones agrupadas por DAM y métricas separadas para ranking, evidencia y explicación/auditabilidad.

**Cadena lógica:** sistemas previos frecuentemente mezclan decisión, reglas, retrieval, reranking o generación -> F1 no tuvo match directo dentro de la búsqueda acotada y F2 conserva solo prior art parcial -> el proyecto impone aislamiento contractual de etapas -> invariancia de ranking + evidencia por candidato + explicación restringida + controles de agrupamiento -> contribución metodológica evaluable, sin transformar la diferencia arquitectónica en novelty automática.

**Componentes diferenciadores:** `EXTERNAL_FIXED_TOP_K`; normativa post-ranking no-reranking; `DOWNSTREAM_EXPLANATION_ONLY`; prohibición de modificación de candidatos; ausencia de feedback clasificatorio; DAM-aware split; separación de métricas por función.

**Componentes que son prior art:** candidate prediction; evidence retrieval; fixed-path rationale; RAG; agentic/hierarchical regulatory search; source-support evaluation; Top-k; reranking; provenance.

**Evidencia requerida:** 0A arquitectura; EV-01/02/03/04/06/08; C01–C07/C14; freezes 0B-02/03/04/05/06; N01 como contraevidencia controlada; invariancia 1.0 del ranking.

**Resultados pendientes que podrían debilitarla:** Grupo 3 puede limitar claims inferenciales de HE2/HE5; una futura reconciliación de EXP-11B puede cambiar discusión de sensibilidad, pero no el contrato arquitectónico. Si se pretendiera ampliar la contribución hacia efectos de tamaño/diversidad, la dependencia aumentaría y esa ampliación no está recomendada aquí.

**Relación con F1–F5:** F1 y F2 son los ejes bibliográficos más próximos; F3 es control de validez; F4 es frontera epistemológica; F5 solo aporta una dimensión de evaluación contextual y no un gap general.

**Riesgo:** `MEDIUM`.

**Afirmaciones prohibidas:** que no existe prior art; que cada capa sea nueva; que candidate/evidence separation no exista; que rationale downstream sea inexistente en literatura; que la arquitectura garantice corrección legal; que el LLM sea clasificador principal.

#### C — Integrada de apoyo a decisiones/auditabilidad

**Estado:** `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

**Formulación:** El artículo puede posicionar el piloto como un mecanismo de apoyo a decisiones que conserva un Top-3 recuperado, adjunta evidencia histórica/normativa identificable y produce explicaciones estructuradas sometidas a evaluación por caso de trazabilidad/auditabilidad. El valor científico de esta alternativa reside en la integración contextual HS/NANDINA y no en una supuesta ausencia general de auditability en regulatory AI.

**Cadena lógica:** decisiones arancelarias requieren soporte documental inspeccionable -> existe prior art de trazabilidad, evidence retrieval y source support -> el proyecto integra esas funciones sobre Top-3 fijo -> EV-06 + HE4 permiten evaluar una versión acotada -> contribución de decision support contextual con fuertes límites de validez.

**Componentes diferenciadores:** enlace candidato-evidencia sobre ranking fijo; salida Top-3 explicada; auditoría caso-a-caso bajo HE4; separación explícita entre auditabilidad y legal correctness.

**Componentes que son prior art:** audit trails, source support, citations, evidence snippets, human decision support, legal/regulatory explanation traces, provenance.

**Evidencia requerida:** EV-06, EV-08, C12–C14, 0B-02/03/05A/05B/06, N01.

**Resultados pendientes que podrían debilitarla:** Grupo 3 para límites finales; cualquier reevaluación de HE4; ausencia de evaluación humana independiente a gran escala.

**Relación con F1–F5:** depende de F1/F2 para el contexto fijo; F5 general está falsado y no puede sostener esta alternativa como novelty.

**Riesgo:** `HIGH`.

**Afirmaciones prohibidas:** ausencia general de auditabilidad en regulatory AI; source support = legal correctness; 28/50 como desempeño general del sistema; explicación estructurada = decisión jurídicamente correcta.

### G. Research Questions candidatas

**Alternativa base para estas RQs:** B — `RECOMMENDED_FOR_EDITORIAL_REVIEW`.

| RQ | texto exacto candidato | constructo evaluado | evidencia/experimento | estado | métricas/outputs relevantes | unidad de análisis/agrupamiento | riesgo de respuesta incompleta | relación OE/HE |
|---|---|---|---|---|---|---|---|---|
| RQ1 | ¿Qué desempeño de recuperación de candidatos alcanza la recuperación histórica en el benchmark v0.2 cuando las particiones se mantienen disjuntas por DAM? | candidate retrieval bajo control de agrupamiento | EV-01 + EV-02/H100 | `AVAILABLE_FROZEN` | Top-1/3/5/10/50, MRR; overlap DAM = 0 | SERIE; DAM como agrupamiento/partición | LOW para descriptivos; inferencia agrupada final depende de Grupo 3 | OE2; HE2 parcialmente, sin cierre inferencial |
| RQ2 | ¿En qué medida puede asociarse evidencia normativa identificable a cada candidato de un Top-3 histórico fijo sin alterar su orden? | evidencia documental post-ranking + invariancia | EV-03/04 + EV-06 | `AVAILABLE_FROZEN` | cobertura/evidencia por candidato; 3,168 slots; invariancia de ranking 1.0 | candidato dentro de SERIE; SERIE como caso | LOW para asociación/invariancia; no responde correctness normativa | OE3; HE3 en su componente de integración |
| RQ3 | ¿En qué medida un LLM local restringido a un Top-3 inmutable conserva candidatos y orden y produce explicaciones estructuradas con evidencia identificable bajo el protocolo HE4? | explicación controlada + trazabilidad/auditabilidad acotada | EV-08/HE4 | `AVAILABLE_WITH_LIMITATION` | 50/50 outputs; 28/50 auditables; media 11.72; mediana 12; hard violations; schema checks | salida/caso sobre SERIE; muestra 50 | MEDIUM por evaluador IA, muestra y mismatch prompt–schema | OE4; HE4 |
| RQ4 | ¿Qué límites de validez introducen la dependencia intra-DAM, los near-duplicates residuales, la composición del banco histórico y el drift normativo en la interpretación de los resultados del piloto? | validez interna/externa y sensibilidad | EV-01, EV-09, EV-14, 0B-05C, SRC-03; Grupo 3 para cierre inferencial | `PENDING` para síntesis inferencial final, con evidencia descriptiva ya disponible | concentración/HHI, exact/near duplicate rates, sensibilidad EXP-11A, estados C21–C25; outputs futuros Grupo 3 | SERIE + DAM; método/condición experimental | MEDIUM/HIGH para cierre de HE5 | OE5; HE5 |

Estas RQs no presuponen que la arquitectura sea novedosa, no dependen exclusivamente de un experimento inexistente y mantienen las funciones de ranking, evidencia y explicación separadas. RQ4 debe permanecer condicionada hasta que Grupo 3 cierre la inferencia correspondiente.

### H. Mapeo OE/HE al artículo

| OE/HE | formulación exacta congelada | relación con contribución candidata B | evidencia disponible | estado | recomendación |
|---|---|---|---|---|---|
| OE1 | **Construir y versionar un banco histórico etiquetado y un corpus normativo NANDINA, aplicando criterios de curación, integridad jerárquica, trazabilidad y reproducibilidad.** | sustenta la base documental y reproducible del contrato | datasets/versiones/hashes; 0B-05A; Grupo 2 cerrado con limitaciones no bloqueantes | disponible con limitaciones declaradas | `IN_PAPER` |
| HE1 | **La estructuración y el versionamiento del banco histórico etiquetado y del corpus normativo NANDINA permitirán preservar la integridad jerárquica, la procedencia de la evidencia y la reproducibilidad de las corridas experimentales.** | respalda gobernanza/provenance, no novelty | 0A/Grupo 2; lineage, hashes, manifests; cierre no perfecto | soporte actual acotado; no afirmar reproducibilidad perfecta | `IN_PAPER` |
| OE2 | **Implementar y comparar estrategias de recuperación normativa y recuperación histórica para generar y ordenar candidatos NANDINA, evaluando su desempeño mediante métricas Top-k, MRR y cobertura del conjunto candidato.** | alimenta la separación entre candidate ranking y evidence retrieval | H100; EXP-04; D1a específico; métricas congeladas | disponible; comparación debe respetar función de cada componente | `IN_PAPER` |
| HE2 | **La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.** | puede contextualizar el rol diferenciado, pero no debe cerrarse desde 0C | descriptivos disponibles; decisión inferencial final aún reservada a Grupo 3; C10/C11 además requieren reconciliación editorial respecto de EXP-11B | `CONDITIONAL_ON_PENDING_EXPERIMENT` | `CONDITIONAL` |
| OE3 | **Evaluar la integración del ranking histórico con evidencia normativa y analizar, de forma diagnóstica, el efecto de un LLM local como reordenador (reranker) sobre el orden de los candidatos.** | integración es central; reranker es contraste diagnóstico secundario | EV-06 completo; EV-07 muestra 20 limitada | integración disponible; reranker `AVAILABLE_WITH_LIMITATION` | `IN_PAPER` |
| HE3 | **La integración del ranking histórico con evidencia normativa conservará el desempeño del ranking histórico y aumentará la trazabilidad documental; el uso diagnóstico del LLM local como reordenador no producirá una mejora consistente del orden de los candidatos.** | primer componente sustenta el contrato; segundo no debe generalizarse | ranking preservado + trazabilidad; reranker 20 casos sin cambio agregado | integración `SUPPORTED_NOW`; reranker insuficiente para una conclusión general | `CONDITIONAL` |
| OE4 | **Diseñar e implementar un LLM local restringido a explicar un Top-3 fijo, sin incorporar códigos externos ni alterar el ranking, y evaluar la validez estructural, la trazabilidad y la concordancia de sus explicaciones con la evidencia recuperada.** | núcleo del componente explanation-only de B | arquitectura + HE4 | `AVAILABLE_WITH_LIMITATION` | `IN_PAPER` |
| HE4 | **El LLM local restringido a un Top-3 fijo generará salidas estructuradas que conservarán los tres candidatos y su orden, no incorporarán códigos externos y vincularán las explicaciones con evidencia histórica o normativa identificable. La calidad de esta vinculación se evaluará mediante criterios de verificabilidad, trazabilidad y concordancia entre evidencia y justificación.** | evidencia empírica del contrato downstream | HE4: 50 casos, outputs completos, auditoría cualitativa limitada | soporte empírico acotado; no legal correctness | `IN_PAPER` |
| OE5 | **Analizar cuantitativa y cualitativamente los errores y límites del piloto, considerando la calidad de las descripciones, la proximidad jerárquica, la disponibilidad de precedentes históricos y el alcance interno de la evaluación.** | delimita alcance y evita convertir diferencia arquitectónica en claim excesivo | EXP-08, near duplicates, concentración, EXP-11A, 0B-05C, EXP12 disposition | evidencia descriptiva disponible; síntesis inferencial final pendiente Grupo 3 | `IN_PAPER` |
| HE5 | **Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.** | posible síntesis de limitaciones, no base del gap actual | EXP-08 histórico/intermedio; otras limitaciones congeladas; decisión final Grupo 3 pendiente | `CONDITIONAL_ON_PENDING_EXPERIMENT` | `CONDITIONAL` |

Ningún OE/HE se reescribe para ajustarlo a la contribución candidata. La selección `IN_PAPER` significa pertinencia temática y disponibilidad suficiente para ser considerada posteriormente, no que la hipótesis correspondiente quede inferencialmente confirmada desde 0C.

### I. Claims candidatos

| claim_candidate_id | claim | tipo | soporte | contraevidencia/caveat | estado analítico | uso futuro posible |
|---|---|---|---|---|---|---|
| 0C-C01 | El flujo oficial fija el ranking histórico antes de recuperar evidencia normativa y antes de la explicación del LLM. | diseño/metodología | 0A-01, D-005, arquitectura congelada | propiedad del proyecto, no novelty | `SUPPORTED_NOW` | Methods/arquitectura |
| 0C-C02 | El LLM principal opera como explicador de un Top-3 fijo y no puede introducir, eliminar, sustituir o reordenar códigos ni retroalimentar la clasificación. | diseño/metodología | 0A-01; F2 congelado | no implica que explanation-only sea universalmente ausente en prior art | `SUPPORTED_NOW` | Methods/posicionamiento |
| 0C-C03 | El split v0.2 elimina el solapamiento de DAM entre H100/DEV/EVAL. | resultado metodológico | C06; EV-01 | no implica independencia intra-DAM ni ausencia de near duplicates | `SUPPORTED_NOW` | Methods/validity |
| 0C-C04 | H100 recupera el código de referencia en Top-3 en 709/1056 casos (67.14%). | resultado experimental | C04; EV-02 | candidate retrieval, no system accuracy | `SUPPORTED_NOW` | Results posteriores |
| 0C-C05 | La integración histórico–normativa asoció evidencia identificable a 3,168/3,168 slots y preservó el ranking histórico. | resultado experimental | EV-06 | asociación ≠ suficiencia normativa/corrección | `SUPPORTED_NOW` | Results/Methods posteriores |
| 0C-C06 | HE4 aporta evidencia acotada sobre estructura, trazabilidad y auditabilidad de las explicaciones bajo el protocolo de 50 casos. | resultado experimental limitado | C14; EV-08 | evaluador IA, mismatch prompt–schema, 28/50 auditables, no legal correctness | `SUPPORTED_NOW` | Results/Limitations con caveats |
| 0C-C07 | La separación contractual F1/F2 constituye por sí misma una novelty demostrada. | novelty | resultado negativo acotado F1 + prior art parcial F2 | `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`; arquitectura ≠ novelty | `NOT_SUPPORTED` | no usar como claim final |
| 0C-C08 | No existe prior art que separe candidatos y evidencia o que genere explicación después de una decisión fijada. | literatura | 0B-02/03B falsifican formulaciones amplias | Lee et al.; Wang et al.; N01 | `PROHIBITED_BY_FROZEN_BOUNDARY` | no usar |
| 0C-C09 | Regulatory AI carece de evaluación formal por salida de source support/auditability. | literatura | ninguno | F5 = DIRECT_PRIOR_ART_FOUND; N01 | `PROHIBITED_BY_FROZEN_BOUNDARY` | no usar |
| 0C-C10 | Historical retrieval es inferencialmente superior a todas las estrategias normativas. | resultado/inferencia | descriptivos favorecen H100 dentro de tareas distintas | HE2 final pendiente Grupo 3; funciones no idénticas | `CONDITIONAL_ON_PENDING_EXPERIMENT` | posible claim posterior si el gate lo autoriza y se redacta por función |
| 0C-C11 | El aumento H100->H150/H200 mejora/empeora/estabiliza el desempeño. | resultado experimental | SRC-03 registra EXP11B cerrado con descriptivos | C10/C11 siguen formalmente prohibidos en matriz editorial; no reconciliar aquí | `PROHIBITED_BY_FROZEN_BOUNDARY` | requiere actualización editorial explícita antes de uso |
| 0C-C12 | EXP-12 demuestra el efecto de diversidad del banco histórico. | resultado experimental | ninguno | condiciones oficiales no materializadas; `EXP12_DIVERSITY_EFFECT_ESTIMABLE=false` | `PROHIBITED_BY_FROZEN_BOUNDARY` | no usar |
| 0C-C13 | La evidencia normativa identificable demuestra corrección normativa sustantiva o jurídica. | interpretación | ninguna equivalencia autorizada | C12/C18; 0B-05C | `PROHIBITED_BY_FROZEN_BOUNDARY` | no usar |
| 0C-C14 | La configurabilidad del framework demuestra generalización fuera de Clase 87. | generalización | configurabilidad documentada | C16 prohibido; no evaluación externa | `PROHIBITED_BY_FROZEN_BOUNDARY` | no usar |
| 0C-C15 | El drift normativo 0B-05C tuvo un efecto dependiente del método: EV03 sin cambio agregado, EV04 con disminución MRR muy pequeña no nula y D1a con cambio no nulo de ranking exacto y efecto HS4 menor mixto. | sensibilidad correctiva | C22–C25 | no causalidad, significancia ni generalización | `SUPPORTED_NOW` | Limitations/Discussion posteriores |
| 0C-C16 | Los límites finales asociados a dependencia, calidad descriptiva y disponibilidad de precedentes confirman HE5. | inferencia | evidencia descriptiva parcial | Grupo 3 no iniciado; HE5 final pendiente | `CONDITIONAL_ON_PENDING_EXPERIMENT` | posterior a Grupo 3 |

### J. Comparación A/B/C y recomendación editorial

| criterio | A — conservadora | B — arquitectónica-metodológica | C — decision support/auditabilidad |
|---|---|---|---|
| fuerza evidencial actual | ALTA | ALTA-MEDIA | MEDIA |
| diferenciación frente al prior art | MEDIA | ALTA dentro del contrato estrecho | MEDIA-BAJA por N01/F5 |
| dependencia de resultados pendientes | BAJA | BAJA para arquitectura; MEDIA para inferencia final | MEDIA |
| compatibilidad con OE/HE | ALTA | ALTA | ALTA para OE4/HE4, menor para OE2/HE2 |
| riesgo de overclaiming | LOW | MEDIUM | HIGH |
| claridad para artículo internacional | ALTA | ALTA | MEDIA-ALTA |
| capacidad de sostener RQs medibles | ALTA | ALTA | MEDIA-ALTA |

**A — Conservadora:** `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

**B — Arquitectónica-metodológica:** `RECOMMENDED_FOR_EDITORIAL_REVIEW`.

**C — Integrada de apoyo a decisiones/auditabilidad:** `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

**Razón de la recomendación:** B ofrece el mejor equilibrio entre evidencia ya disponible y diferenciación frente al prior art sin depender de la formulación F5 falsada. Su fuerza no procede de afirmar que sus componentes sean inéditos, sino de tratar como objeto evaluable el contrato de separación funcional e invariancia: ranking histórico fijado, evidencia normativa posterior no-reranking, generador explanation-only sin feedback y control de dependencia por DAM. A sigue siendo la alternativa más segura si la auditoría editorial considera que el riesgo bibliográfico de F1/F2 aún es demasiado alto. C no se recomienda como contribución principal porque N01 y el resto del corpus impiden sostener una ausencia general de evaluación de source support/auditability.

Esta recomendación no constituye aprobación editorial, gap final ni novelty.

### K. Riesgos, dependencias y triggers

1. **Desfase editorial EXP-11B:** `SRC-03` registra EXP-11B cerrado/aprobado/integrado, pero C10/C11 aún lo describen como pendiente/prohibido. No se usan los resultados de EXP-11B para claims de 0C hasta reconciliación formal de la Claim–Evidence Matrix.
2. **Grupo 3 pendiente:** HE2 y HE5 no deben cerrarse inferencialmente. Cualquier contribución o RQ que requiera su confirmación final permanece condicional.
3. **EXP-12 no estimable:** el diseño original quedó cerrado sin retrieval; no existe efecto de diversidad estimable. No puede utilizarse como resultado positivo o negativo sobre diversidad.
4. **F1 y F3 son negativos acotados:** no prueban inexistencia universal ni novelty.
5. **F2 tiene prior art parcial:** la diferenciación solo sobrevive bajo el contrato estricto `EXTERNAL_FIXED_TOP_K + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT/DELETE/SUBSTITUTE/REORDER + NO_CLASSIFICATION_FEEDBACK`.
6. **F5 general está falsado:** cualquier restauración de “regulatory AI lacks auditability/source-support evaluation” contradice el freeze 0B-06.
7. **HE4 es limitada:** 50 casos, evaluador IA y mismatch prompt–schema. No debe convertirse en una tasa general del sistema ni en validación jurídica.
8. **Validez del benchmark:** cero DAM compartidas entre particiones no elimina dependencia intra-DAM ni near-duplicates cross-DAM; Grupo 3 debe manejar la unidad de agrupamiento cuando corresponda.
9. **0B-05C:** el efecto correctivo es method-dependent y no puede resumirse como ausencia de impacto numérico.
10. **Reproducibilidad:** Grupo 2 está cerrado con limitaciones no bloqueantes, no como reproducibilidad perfecta.
11. **Generalización:** toda evidencia empírica permanece limitada a Clase/Capítulo 87 y al marco evaluado.
12. **Legal correctness:** evidencia identificable, source support y auditabilidad no prueban clasificación jurídicamente correcta ni vinculante.
13. **Decisión del autor/editor:** debe decidir si B es suficientemente conservadora para congelarse como contribución provisional de 0C o si se prefiere A como formulación base. Esa decisión no requiere nueva búsqueda bibliográfica.
14. **Motivo por el que 0C todavía no puede congelarse:** falta auditoría de la IA Gestora / Editor Científico Principal y aprobación expresa del autor; además, cualquier intento de incorporar resultados EXP-11B a claims del artículo exige primero reconciliar el desfase C10/C11.

`EXPERIMENTAL_REVIEW_TRIGGER = ABSENT`.

Justificación: este artefacto no introduce una interpretación experimental nueva; consume únicamente estados y resultados ya registrados en freezes o en `SRC-03`, y mantiene como condicionales las decisiones inferenciales aún pendientes. Si la revisión editorial pretendiera convertir los resultados vivos de EXP-11B en claims nuevos o cerrar HE2/HE5 antes de Grupo 3, esa acción posterior sí requeriría el gate correspondiente.

### L. Trazabilidad

- Repositorio: `elVladdi/gci-nandina-rag`.
- Rama consumida: `article/main-manuscript`.
- HEAD/commit de apertura consumido: `75eb14b1fc1d02b8ec9ea81963cfc1d4e8739be8`.
- Prompt ejecutado: `article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md`.
- Plan Maestro `SRC-03`: rama `docs/plan-maestro-temporal-2026-08-31`, HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`.
- Ground truth consumido: `0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md` y `0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.
- Literatura consumida: freezes `0B-01` a `0B-06`, cierre formal 0B y `BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.
- Nueva literatura admitida utilizable: N01 únicamente dentro de sus límites congelados.
- N02 no fue utilizado como evidencia determinante; N03/N04 permanecen rechazados.
- Búsqueda web realizada en 0C: `NO`.
- Experimentos ejecutados/recalculados en 0C: `NO`.
- Archivos de gobernanza modificados: `NO`.

```text
0C_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0C = NOT_PERFORMED
0D = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

---

## English

### A. Reconstructed state

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = READY_FOR_DRAFTING
0D = BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
NEW_LITERATURE_SEARCH = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

**FILES READ:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/0B_PHASE_CLOSURE.md`; `article/reviews/0C_ENTRY_GATE.md`; `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`; freezes `0B-01` through `0B-06`; and the experimental Master Plan `SRC-03` in read-only mode.

**ACTIVE PHASE:** `0C — Gap, contribution, and Research Questions`.

**ASSIGNED-BLOCK STATUS:** `READY_FOR_DRAFTING`.

**DRAFTING AUTHORIZED:** yes, only for this positioning-analysis artifact; no manuscript section may be drafted.

**RELEVANT FROZEN DECISIONS:** historical retrieval = candidate generation/ranking; normative retrieval = post-ranking documentary evidence that does not replace or reorder the historical ranking; fixed Top-3 before generation; local LLM = controlled explanation rather than autonomous classification; SERIES = analysis unit and DAM = grouping unit when dependence exists; configurability ≠ empirical generalization; auditability/traceability ≠ legal correctness.

**RELEVANT AUTHORIZED CLAIMS:** C01–C07, C15, C17, C19, and C21–C25 within their stated limits; C14 only conditionally and under the HE4 limitations.

**RELEVANT PROHIBITED OR PENDING CLAIMS:** C09, C12, C13, C16, and C18 remain prohibited; C20 remains `REVIEW_REQUIRED`. C10–C11 remain formally `PROHIBITED` in the Claim–Evidence Matrix even though the living Master Plan now records EXP-11B as closed with approved descriptive results; those results are therefore not used here to formulate article claims until an explicit editorial reconciliation of the matrix occurs.

**EXTERNAL SOURCES TO VERIFY:** none. `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED` and Phase 0B is closed.

**BLOCKERS OR CONTRADICTIONS DETECTED:** no material contradiction exists in the architecture or 0C opening state. There is a governance lag between the historical 0A-02/Claim–Evidence Matrix and the living experimental state: `SRC-03` records EXP-11B as closed/approved/integrated, EXP-12 as closed without retrieval because the planning precondition failed, Group 2B as closed with nonblocking limitations, and Group 3 as the next unstarted block. This lag is not reconciled by inference in this artifact and is not used to introduce new claims.

**Experimental snapshot consumed:**

```text
SRC-03 branch = docs/plan-maestro-temporal-2026-08-31
SRC-03 HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
SRC-03 blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
GROUP3 = NOT_STARTED / NEXT
```

**Bibliographic state transferred without modification:**

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F4 = METHODOLOGICAL_BOUNDARY_NOT_INDEPENDENT_NOVELTY
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
G6 = ELIMINATED_AS_GAP_CANDIDATE
G7 = MERGED_INTO_F2
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
```

Interpretation rules applied throughout:

`LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.

`ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`.

`ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`.

`AUDITABILITY ≠ LEGAL_CORRECTNESS`.

`CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.

### B. 0A + 0B transfer matrix

| element | governing source | supporting evidence | counterevidence/caveat | 0C status | overclaiming risk |
|---|---|---|---|---|---|
| Architecture `historical -> Top-k/fixed Top-3 -> normative evidence -> explanatory LLM` | 0A-01; D-005; 0A-02; 0B freezes | approved and operational architecture; integration preserves historical ranking; primary LLM does not decide the code | existence of the architecture is a project feature, not proof of novelty | `SUPPORTED_NOW` as project design | MEDIUM if presented as novel by itself |
| F1: historical ranking fixed before later non-reranking normative evidence | 0B-02, 0B-03A/B, 0B-06 | directed search found no direct match within scope; project implements strict separation and rank preservation | Lee et al. already separate candidate prediction and evidence retrieval; other systems combine retrieval/rules/normative information; 0B-06 negative result is bounded | narrow positioning candidate only | MEDIUM |
| F2: explanation-only generator over immutable external Top-k | 0B-03B; 0B-06; N01 | project contract forbids insertion, deletion, substitution, reordering, or classification feedback | Wang et al. already separate a fixed path from final rationale; N01 provides traces/source support but its representation participates in prediction/refinement | narrow candidate; `PARTIAL_PRIOR_ART_FOUND` | MEDIUM |
| F3: dependence control by administrative/group unit | 0A-01/02; 0B-01/02/03; 0B-06 | v0.2 split eliminates DAM overlap across H100/DEV/EVAL; SERIES/DAM are explicitly separated | missing grouped splits in prior work do not prove leakage or novelty; cross-DAM near-duplicates remain; final inference must respect grouping | methodological/validity principle, not stand-alone central contribution | LOW as control; HIGH if sold as novelty |
| F4: performance/retrieval/path/evidence ≠ substantive/legal correctness | 0B-02–05C | boundary is broadly supported by literature and governance | precisely because it is well established, it is not independent novelty | mandatory methodological boundary | HIGH if presented as novel contribution |
| F5: formal per-output documentary-auditability evaluation | 0B-02/03/05A; 0B-06; N01 | HE4 performs case-level evaluation with explicit criteria; project integrates identifiable evidence per candidate | N01 is direct regulatory/legal-AI prior art for instance-level source-support/audit-oriented traces; general absence claim is falsified; HE4 has 50 cases, AI evaluator, prompt–schema mismatch | only a contextual HS/customs component, not general absence | HIGH |
| SERIES/DAM and v0.2 split | 0A-01/02; C06/C07 | zero shared DAMs across H100, DEV, EVAL; EVAL = 1,056 series / 67 DAM | zero cross-partition overlap does not imply independence of all 1,056 series; residual exact/near duplicate cross-DAM cases exist | `SUPPORTED_NOW` as validity control | LOW |
| H100 as candidate retrieval | 0A-02; C04/C05 | Top-1 0.50947; Top-3 709/1056 = 0.67140; Top-5 0.76326; Top-10 0.89110; Top-50 0.99148; MRR 0.62971 | not overall system/RAG/LLM accuracy; H100 concentration/composition limits interpretation | `SUPPORTED_NOW` | LOW when named correctly; HIGH if called system accuracy |
| Normative retrieval | 0A-02; 0B-04A/B; 0B-05C | flat/hierarchical BM25 characterize documentary retrieval; hierarchical variant extends deeper-rank coverage | its task is evidence rather than primary ranking; results are not interchangeable with classification accuracy | `SUPPORTED_NOW` within documentary role | MEDIUM |
| Historical–normative integration | 0A-02 EV-06; C02 | 3,168/3,168 slots with identifiable NANDINA-8 evidence; full traceability; rank preservation 1.0 | association/coverage ≠ semantic sufficiency, normative correctness, or legal correctness | `SUPPORTED_NOW` | LOW with explicit boundaries |
| Diagnostic LLM reranker | 0A-02 EV-07 | fixed 20-case sample; Top-1 10/20 before/after; Top-3 13/20 before/after; delta MRR 0; 19/20 ties | diagnostic sample, no prespecified inferential test; neither benchmark nor general effect | `AVAILABLE_WITH_LIMITATION`; not central | HIGH if generalized |
| HE4 / explanation and auditability | 0A-02 EV-08; C14 | 50/50 explanations; 28/50 auditable (56%); mean 11.72; median 12; no reported hard violations | AI evaluator; `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`; `EVALUATOR_MODALITY_DEVIATION`; exploratory; not legal correctness | `AVAILABLE_WITH_LIMITATION` | HIGH if presented as legal validation or general auditability rate |
| Reproducibility/provenance | 0B-05A; C17; SRC-03 Group 2B | traceability, hashes, lineage, Group-2 closure with `APPROVED_WITH_NONBLOCKING_LIMITATIONS` | not perfect reproducibility; `DECLARED_NOT_RECOVERABLE`, `HASH_BOUND_LOCAL_ONLY`, and other preserved limitations remain | `SUPPORTED_NOW` as bounded protocol/state | MEDIUM |
| 0B-05C / normative drift | 0B-05C; C21–C25 | drift and scope overlap confirmed; corrective sensitivity closed; EV03 zero aggregate change, EV04 tiny nonzero MRR decrease, D1a nonzero method-dependent change | no legal correctness, causality, significance, or generalization; may not be summarized as “no impact” | `SUPPORTED_NOW` as documentary/methodological limitation | HIGH if oversimplified |
| Live EXP-11B vs editorial matrix | SRC-03; Claim–Evidence Matrix | living Master Plan records EXP-11B closed/approved/integrated with descriptive results | C10/C11 still formally prohibit directional H150/H200 claims; 0C cannot amend the matrix | do not use for central claim or HE2 closure here | HIGH |
| EXP-12 | SRC-03 | final methodological disposition is documented/audited | no retrieval; D-HIGH/D-MID/D-LOW conditions were not materialized; `EXP12_DIVERSITY_EFFECT_ESTIMABLE=false` | methodological limitation, not a diversity-effect result | HIGH if a diversity effect is inferred |
| Group 3 | SRC-03; 0A-01/02 | prospective gate is defined as next block | `NOT_STARTED`; final HE2/HE5 decisions remain pending | explicit dependency for final inference | HIGH if anticipated |

### C. Candidate empirical gap

**One-sentence candidate formulation:** Within the reviewed HS/customs corpus and the directed 2022–2026 search, directly comparable empirical evidence remains limited for a pilot that separately evaluates historical candidate ranking, normative evidence retrieved after that ranking is fixed, and restricted explanation of an immutable Top-3 under an administrative-unit-grouped split.

**Bibliographic evidence permitting the formulation:** F1 and F3 closed 0B-06 as `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`; F2 closed as `PARTIAL_PRIOR_ART_FOUND`. Inherited work covers direct classification, retrieval, candidate prediction, evidence retrieval, RAG, agents, hierarchical search, knowledge graphs, traceability, and explanation, but that coverage must not be equated with the project's complete contract.

**Prior art weakening it:** Lee et al. already separate candidate prediction from HS-manual evidence retrieval; Wang et al. separate a fixed hierarchical path from final evidence aggregation/rationale; N01 evaluates instance-level traces/source support in regulatory/legal AI; multiple works already use Top-k, precedent retrieval, RAG, and customs rules.

**Relevant project evidence:** v0.2 split with no shared DAMs across partitions; H100 Top-3 0.67140 and MRR 0.62971 as candidate retrieval; integration with 3,168/3,168 identifiable-evidence slots and preserved ranking; HE4 executed on 50 cases under explicit limitations.

- `SUPPORTED_NOW`: a functionally separated pipeline exists and has been evaluated within Chapter 87; candidate retrieval, evidence retrieval, integration, traceability, and bounded explanation metrics are available.
- `CONDITIONAL_ON_PENDING_EXPERIMENT`: final inferential closure of SH2 or SH5 and any Group-3-dependent statistical claim; editorial use of H150/H200 direction requires prior C10/C11 reconciliation.
- `NOT_SUPPORTED`: universal absence of equivalent systems; general superiority; generalization beyond Chapter 87; legal correctness of outputs.

**Falsification/invalidation conditions:** admissible prior art implementing a functionally equivalent external historical ranking, post-ranking non-reranking normative evidence, and isolated downstream explanation; or evidence that the project's normative/generative layer can alter candidates.

**Overclaiming risk:** `MEDIUM`.

**Proposed 0C function:** useful for positioning, but not as a “no prior work exists” statement or final novelty claim.

### D. Candidate methodological gap

**One-sentence candidate formulation:** A candidate methodological gap is the explicit evaluation of a contract that separates candidate generation, documentary evidence, and explanation—fixing the historical ranking before normative retrieval and isolating the generator from classification capability—together with administrative-unit dependence controls and function-specific metrics.

**Bibliographic evidence permitting the formulation:** F1 survives narrowly and F2 preserves a precise contractual difference; 0B-04A/04B establish that candidate generation, reranking, explanation, grounding, provenance, and auditability are not interchangeable; F3 supports group control when correlated observations exist.

**Prior art weakening it:** candidate prediction + evidence retrieval already exists; hierarchical/regulation-driven systems already fix paths before final rationale; N01 separates explanation-level evaluation from label accuracy but its trace/program participates in prediction/refinement; group-aware validation is a general methodological principle even though no direct customs match was found within the bounded 0B-06 search.

**Relevant project evidence:** integration rank invariance = 1.0; fixed Top-3; non-reranking normative retrieval; explanation-only primary LLM; DAM-based split; separate metrics for candidate retrieval, evidence retrieval, and bounded auditability.

- `SUPPORTED_NOW`: the methodological contract is documented and implemented; its main invariants are verified.
- `CONDITIONAL_ON_PENDING_EXPERIMENT`: final SH2/SH5 inference and any statistical analysis reserved for Group 3.
- `NOT_SUPPORTED`: novelty of each component; automatic novelty of the architecture; absence of all prior decision/explanation separation.

**Falsification/invalidation conditions:** functionally equivalent prior art under the same isolation contract; discovery of classification feedback or reordering in the official project flow; or metric use that collapses candidate retrieval into correctness.

**Overclaiming risk:** `MEDIUM`.

**Proposed 0C function:** strongest family for a candidate contribution, provided it is framed as an evaluated contract rather than architectural novelty by itself.

### E. Candidate decision-support/auditability gap

**One-sentence candidate formulation:** As a contextual rather than general gap, 0C may examine whether HS/customs classification leaves room for integrating identifiable documentary evidence and controlled explanations over already fixed candidates while evaluating auditability by case without converting source support into legal correctness.

**Bibliographic evidence permitting it:** reviewed customs literature includes evidence, traceability, file notes, paths, citations, and decision support; the project adds explicit fixed-Top-3 integration and case-level HE4 evaluation.

**Prior art weakening it:** F5 = `DIRECT_PRIOR_ART_FOUND`; N01 evaluates source support/audit-oriented traces by instance in regulatory/legal AI; P03 presents visible evidence plus human evaluation; P05 explicitly addresses auditability and authoritative sources; ICCA-RAG and agentic systems provide provenance/traceability even when not equivalent to HE4.

**Relevant project evidence:** 3,168/3,168 identifiable-evidence slots, preserved ranking, 50 HE4 explanations, 28/50 auditable in the qualitative audit.

- `SUPPORTED_NOW`: the project implements candidate-level documentary support and a bounded auditability/structure evaluation.
- `CONDITIONAL_ON_PENDING_EXPERIMENT`: any final SH5 synthesis or validity inference; any HE4 generalization beyond the executed protocol.
- `NOT_SUPPORTED`: absence of auditability/source-support evaluation in regulatory AI; HE4 as legal correctness; 56% as a general system auditability rate.

**Falsification/invalidation conditions:** restoring broad F5; ignoring N01; treating source support as legal sufficiency; or extending HE4 beyond its sample/protocol.

**Overclaiming risk:** `HIGH`.

**Proposed 0C function:** better treated as a contextual contribution/evaluation component rather than the primary stand-alone gap.

### F. Central-contribution alternatives A/B/C

#### A — Conservative / minimum defensible

**Status:** `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

**Formulation:** The article may contribute a bounded evaluation of an offline NANDINA-subheading recommendation pilot that separately measures historical candidate retrieval, subsequent normative-evidence association, and controlled explanation of a fixed Top-3 under a DAM-grouped split with explicit documentary traceability. The contribution is limited to the evaluated Chapter-87 design and the metrics actually executed.

**Logical chain:** auditable-recommendation problem -> heterogeneous prior tasks/metrics -> differentiated component evaluation -> H100 + normative retrieval + integration + HE4 -> bounded empirical evidence without universal novelty claims.

**Differentiating components:** integrated yet functionally disaggregated evaluation; fixed Top-3; DAM split; post-ranking evidence per candidate; explicit retrieval/auditability/correctness boundaries.

**Prior-art components:** Top-k, historical retrieval, BM25, semantic retrieval, RAG, human decision support, visible evidence, LLM classification/explanation, provenance, audit trails.

**Required evidence:** C01–C07, C14 with caveats, integration EV-06, HE4 EV-08, 0B freezes, and Group-2 closure.

**Pending results that could weaken it:** Group 3 may change inferential interpretation of SH2/SH5, but it does not invalidate the pipeline or already frozen results.

**F1–F5 relationship:** F1/F2 only contextualize; F3 provides validity control; F4 is a boundary; broad F5 is not required.

**Risk:** `LOW`.

**Prohibited statements:** first/unique/no-prior-art claims; overall RAG accuracy; legal correctness; generalization beyond Chapter 87; causal bank-size effect.

#### B — Architectural-methodological

**Status:** `RECOMMENDED_FOR_EDITORIAL_REVIEW`.

**Formulation:** The article may contribute by formalizing and evaluating an architectural-methodological contract in which historical retrieval fixes the candidate ranking, normative retrieval only documents those candidates, and a downstream local LLM explains an immutable Top-3 without the ability to insert, delete, substitute, reorder, or feed back into classification. Evaluation complements this contract with DAM-grouped partitions and separate ranking, evidence, and explanation/auditability metrics.

**Logical chain:** prior systems often entangle decision, rules, retrieval, reranking, or generation -> F1 had no direct match within the bounded search and F2 retains only partial prior art -> the project imposes contractual stage isolation -> rank invariance + candidate-level evidence + restricted explanation + grouping control -> measurable methodological contribution without turning architectural difference into automatic novelty.

**Differentiating components:** `EXTERNAL_FIXED_TOP_K`; post-ranking non-reranking normative evidence; `DOWNSTREAM_EXPLANATION_ONLY`; no candidate modification; no classification feedback; DAM-aware split; function-specific metrics.

**Prior-art components:** candidate prediction; evidence retrieval; fixed-path rationale; RAG; agentic/hierarchical regulatory search; source-support evaluation; Top-k; reranking; provenance.

**Required evidence:** 0A architecture; EV-01/02/03/04/06/08; C01–C07/C14; 0B-02/03/04/05/06 freezes; N01 as controlled counterevidence; rank-invariance artifact.

**Pending results that could weaken it:** Group 3 may constrain SH2/SH5 inference; later EXP-11B editorial reconciliation may affect sensitivity discussion but not the architectural contract. Extending the contribution to bank-size/diversity effects would increase dependency and is not recommended here.

**F1–F5 relationship:** F1/F2 are the closest bibliographic axes; F3 is validity control; F4 is an epistemic boundary; F5 contributes only a contextual evaluation dimension rather than a general gap.

**Risk:** `MEDIUM`.

**Prohibited statements:** no-prior-art claims; novelty of each layer; absence of candidate/evidence separation; absence of downstream rationale in literature; legal correctness guarantee; LLM as primary classifier.

#### C — Integrated decision support/auditability

**Status:** `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

**Formulation:** The article may position the pilot as decision support that preserves a retrieved Top-3, attaches identifiable historical/normative evidence, and produces structured explanations subjected to case-level traceability/auditability evaluation. The scientific value of this alternative lies in HS/NANDINA contextual integration rather than any general absence of auditability in regulatory AI.

**Logical chain:** tariff decisions require inspectable documentary support -> prior art already provides traceability, evidence retrieval, and source support -> project integrates these over a fixed Top-3 -> EV-06 + HE4 enable bounded evaluation -> contextual decision-support contribution under strong validity limits.

**Differentiating components:** candidate–evidence linkage over fixed ranking; explained Top-3 output; HE4 case-level audit; explicit auditability/legal-correctness separation.

**Prior-art components:** audit trails, source support, citations, evidence snippets, human decision support, legal/regulatory explanation traces, provenance.

**Required evidence:** EV-06, EV-08, C12–C14, 0B-02/03/05A/05B/06, N01.

**Pending results that could weaken it:** Group 3 for final limitations; any HE4 reevaluation; absence of large-scale independent human evaluation.

**F1–F5 relationship:** relies on F1/F2 for fixed context; broad F5 is falsified and cannot support novelty.

**Risk:** `HIGH`.

**Prohibited statements:** general absence of regulatory-AI auditability; source support = legal correctness; 28/50 as general system performance; structured explanation = legally correct decision.

### G. Candidate Research Questions

**Base alternative:** B — `RECOMMENDED_FOR_EDITORIAL_REVIEW`.

| RQ | exact candidate text | evaluated construct | evidence/experiment | status | relevant metrics/outputs | analysis/grouping unit | incomplete-answer risk | approved objective/hypothesis relation |
|---|---|---|---|---|---|---|---|---|
| RQ1 | What candidate-retrieval performance does historical retrieval achieve on the v0.2 benchmark when partitions remain disjoint by DAM? | candidate retrieval under grouping control | EV-01 + EV-02/H100 | `AVAILABLE_FROZEN` | Top-1/3/5/10/50, MRR; DAM overlap = 0 | SERIES; DAM for grouping/partitioning | LOW for descriptives; final grouped inference depends on Group 3 | SO2; SH2 partially, without inferential closure |
| RQ2 | To what extent can identifiable normative evidence be associated with each candidate of a fixed historical Top-3 without changing its order? | post-ranking documentary evidence + invariance | EV-03/04 + EV-06 | `AVAILABLE_FROZEN` | evidence/coverage by candidate; 3,168 slots; rank invariance 1.0 | candidate within SERIES; SERIES as case | LOW for association/invariance; does not answer normative correctness | SO3; integration component of SH3 |
| RQ3 | To what extent does a local LLM restricted to an immutable Top-3 preserve candidates and order and produce structured explanations with identifiable evidence under the HE4 protocol? | controlled explanation + bounded traceability/auditability | EV-08/HE4 | `AVAILABLE_WITH_LIMITATION` | 50/50 outputs; 28/50 auditable; mean 11.72; median 12; hard violations; schema checks | case/output over SERIES; sample 50 | MEDIUM due AI evaluator, sample, prompt–schema mismatch | SO4; SH4 |
| RQ4 | What validity limits do intra-DAM dependence, residual near-duplicates, historical-bank composition, and normative-version drift impose on interpretation of the pilot results? | internal/external validity and sensitivity | EV-01, EV-09, EV-14, 0B-05C, SRC-03; Group 3 for final inference | `PENDING` for final inferential synthesis, with existing descriptive evidence | concentration/HHI, exact/near-duplicate rates, EXP-11A sensitivity, C21–C25 states; future Group-3 outputs | SERIES + DAM; experimental method/condition | MEDIUM/HIGH for SH5 closure | SO5; SH5 |

These RQs do not assume architectural novelty, do not depend exclusively on a nonexistent experiment, and keep ranking, evidence, and explanation functions separate. RQ4 must remain conditional until Group 3 closes the relevant inference.

### H. SO/SH mapping to the article

| SO/SH | exact frozen formulation | relationship to candidate contribution B | available evidence | status | recommendation |
|---|---|---|---|---|---|
| SO1 | **Build and version a labeled historical bank and a NANDINA normative corpus by applying curation, hierarchical-integrity, traceability, and reproducibility criteria.** | supports the documentary/reproducible basis of the contract | datasets/versions/hashes; 0B-05A; Group 2 closed with declared nonblocking limitations | available with declared limitations | `IN_PAPER` |
| SH1 | **Structuring and versioning the labeled historical bank and the NANDINA normative corpus will preserve hierarchical integrity, evidence provenance, and reproducibility of experimental runs.** | supports governance/provenance rather than novelty | 0A/Group 2; lineage, hashes, manifests; closure is not perfect | bounded current support; do not claim perfect reproducibility | `IN_PAPER` |
| SO2 | **Implement and compare normative-retrieval and historical-retrieval strategies to generate and rank NANDINA candidates, evaluating their performance using Top-k, MRR, and candidate-set coverage metrics.** | feeds the separation between candidate ranking and evidence retrieval | H100; EXP-04; specific D1a; frozen metrics | available; comparison must preserve component function | `IN_PAPER` |
| SH2 | **Historical retrieval will achieve better Top-k and MRR performance than normative-retrieval strategies, while hierarchical normative variants and candidate-set variants will expand documentary coverage at deeper ranks.** | may contextualize differentiated roles but must not be closed in 0C | descriptives available; final inferential decision still reserved for Group 3; C10/C11 also require editorial reconciliation for EXP-11B | `CONDITIONAL_ON_PENDING_EXPERIMENT` | `CONDITIONAL` |
| SO3 | **Evaluate integration of the historical ranking with normative evidence and diagnostically analyze the effect of a local LLM as a reranker on candidate ordering.** | integration is central; reranker is a secondary diagnostic contrast | EV-06 complete; EV-07 limited 20-case sample | integration available; reranker `AVAILABLE_WITH_LIMITATION` | `IN_PAPER` |
| SH3 | **Integrating the historical ranking with normative evidence will preserve historical-ranking performance and increase documentary traceability; diagnostic use of the local LLM as a reranker will not produce a consistent improvement in candidate ordering.** | first component supports the contract; second must not be generalized | preserved ranking + traceability; 20-case reranker without aggregate change | integration `SUPPORTED_NOW`; reranker insufficient for general conclusion | `CONDITIONAL` |
| SO4 | **Design and implement a local LLM restricted to explaining a fixed Top-3, without introducing external codes or altering the ranking, and evaluate the structural validity, traceability, and concordance of its explanations with retrieved evidence.** | core of B's downstream explanation-only component | architecture + HE4 | `AVAILABLE_WITH_LIMITATION` | `IN_PAPER` |
| SH4 | **The local LLM restricted to a fixed Top-3 will generate structured outputs that retain the three candidates and their order, introduce no external codes, and link explanations to identifiable historical or normative evidence. The quality of this linkage will be evaluated using verifiability, traceability, and evidence–justification concordance criteria.** | empirical evidence for the downstream contract | HE4: 50 cases, complete outputs, limited qualitative audit | bounded empirical support; not legal correctness | `IN_PAPER` |
| SO5 | **Quantitatively and qualitatively analyze pilot errors and limits, considering description quality, hierarchical proximity, availability of historical precedents, and the internal scope of the evaluation.** | bounds scope and prevents architectural difference from becoming an excessive claim | EXP-08, near duplicates, concentration, EXP-11A, 0B-05C, EXP12 disposition | descriptive evidence available; final inferential synthesis pending Group 3 | `IN_PAPER` |
| SH5 | **Pilot errors and limits will concentrate in ambiguous or incomplete descriptions, hierarchically close subheadings, cases with insufficient historical precedents, and conditions that restrict validity of the results to the internally evaluated set.** | possible limitations synthesis, not basis of current gap | historical/intermediate EXP-08; other frozen limitations; final Group-3 decision pending | `CONDITIONAL_ON_PENDING_EXPERIMENT` | `CONDITIONAL` |

No SO/SH has been rewritten to fit the candidate contribution. `IN_PAPER` denotes thematic relevance and sufficient evidence for later consideration; it does not mean that the corresponding hypothesis has been inferentially confirmed by 0C.

### I. Candidate claims

| claim_candidate_id | claim | type | support | counterevidence/caveat | analytical status | possible future use |
|---|---|---|---|---|---|---|
| 0C-C01 | The official flow fixes the historical ranking before normative-evidence retrieval and before LLM explanation. | design/method | 0A-01, D-005, frozen architecture | project feature, not novelty | `SUPPORTED_NOW` | Methods/architecture |
| 0C-C02 | The primary LLM acts as a fixed-Top-3 explainer and cannot insert, delete, substitute, or reorder codes or feed back into classification. | design/method | 0A-01; frozen F2 | does not establish universal absence of explanation-only prior art | `SUPPORTED_NOW` | Methods/positioning |
| 0C-C03 | The v0.2 split eliminates DAM overlap across H100/DEV/EVAL. | methodological result | C06; EV-01 | does not imply intra-DAM independence or absence of near duplicates | `SUPPORTED_NOW` | Methods/validity |
| 0C-C04 | H100 retrieves the reference code within Top-3 in 709/1056 cases (67.14%). | experimental result | C04; EV-02 | candidate retrieval, not system accuracy | `SUPPORTED_NOW` | later Results |
| 0C-C05 | Historical–normative integration associated identifiable evidence with 3,168/3,168 slots and preserved the historical ranking. | experimental result | EV-06 | association ≠ normative sufficiency/correctness | `SUPPORTED_NOW` | later Results/Methods |
| 0C-C06 | HE4 provides bounded evidence on explanation structure, traceability, and auditability under the executed 50-case protocol. | limited experimental result | C14; EV-08 | AI evaluator, prompt–schema mismatch, 28/50 auditable, not legal correctness | `SUPPORTED_NOW` | later Results/Limitations with caveats |
| 0C-C07 | The F1/F2 separation contract by itself constitutes demonstrated novelty. | novelty | bounded F1 negative + partial F2 prior art | `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`; architecture ≠ novelty | `NOT_SUPPORTED` | do not use as final claim |
| 0C-C08 | No prior art separates candidates/evidence or generates explanation after a fixed decision. | literature | none | broad forms falsified by Lee et al., Wang et al., N01 | `PROHIBITED_BY_FROZEN_BOUNDARY` | do not use |
| 0C-C09 | Regulatory AI lacks formal per-output source-support/auditability evaluation. | literature | none | F5 = DIRECT_PRIOR_ART_FOUND; N01 | `PROHIBITED_BY_FROZEN_BOUNDARY` | do not use |
| 0C-C10 | Historical retrieval is inferentially superior to all normative strategies. | result/inference | descriptive values favor H100 across different component tasks | final SH2 pending Group 3; functions are not identical | `CONDITIONAL_ON_PENDING_EXPERIMENT` | possible later bounded claim if authorized |
| 0C-C11 | Increasing H100 to H150/H200 improves/worsens/stabilizes performance. | experimental result | SRC-03 records closed EXP11B descriptives | C10/C11 remain formally prohibited in editorial matrix; no reconciliation here | `PROHIBITED_BY_FROZEN_BOUNDARY` | requires explicit editorial update before use |
| 0C-C12 | EXP-12 demonstrates the effect of historical-bank diversity. | experimental result | none | official conditions not materialized; `EXP12_DIVERSITY_EFFECT_ESTIMABLE=false` | `PROHIBITED_BY_FROZEN_BOUNDARY` | do not use |
| 0C-C13 | Identifiable normative evidence establishes substantive normative or legal correctness. | interpretation | none | C12/C18; 0B-05C boundaries | `PROHIBITED_BY_FROZEN_BOUNDARY` | do not use |
| 0C-C14 | Framework configurability demonstrates generalization beyond Chapter 87. | generalization | documented configurability only | C16 prohibited; no external empirical evaluation | `PROHIBITED_BY_FROZEN_BOUNDARY` | do not use |
| 0C-C15 | The 0B-05C normative-drift sensitivity had method-dependent effects: EV03 zero aggregate change, EV04 tiny nonzero MRR decrease, and D1a nonzero exact-ranking change with minor mixed HS4 effect. | corrective sensitivity | C22–C25 | no causality, significance, or generalization | `SUPPORTED_NOW` | later Limitations/Discussion |
| 0C-C16 | Final limits associated with dependence, description quality, and precedent availability confirm SH5. | inference | partial descriptive evidence | Group 3 not started; final SH5 pending | `CONDITIONAL_ON_PENDING_EXPERIMENT` | after Group 3 |

### J. A/B/C comparison and editorial recommendation

| criterion | A — conservative | B — architectural-methodological | C — decision support/auditability |
|---|---|---|---|
| current evidential strength | HIGH | HIGH-MEDIUM | MEDIUM |
| differentiation from prior art | MEDIUM | HIGH within narrow contract | MEDIUM-LOW because of N01/F5 |
| dependence on pending results | LOW | LOW for architecture; MEDIUM for final inference | MEDIUM |
| compatibility with SO/SH | HIGH | HIGH | HIGH for SO4/SH4, lower for SO2/SH2 |
| overclaiming risk | LOW | MEDIUM | HIGH |
| clarity for an international article | HIGH | HIGH | MEDIUM-HIGH |
| capacity to support measurable RQs | HIGH | HIGH | MEDIUM-HIGH |

**A — Conservative:** `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

**B — Architectural-methodological:** `RECOMMENDED_FOR_EDITORIAL_REVIEW`.

**C — Integrated decision support/auditability:** `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

**Rationale:** B provides the best balance between currently available evidence and differentiation from prior art without relying on the falsified broad F5 formulation. Its strength does not come from claiming that its components are individually new, but from treating the functional-separation/invariance contract as an evaluable object: fixed historical ranking, post-ranking non-reranking normative evidence, explanation-only generator without feedback, and DAM dependence control. A remains the safest fallback if editorial review considers the remaining F1/F2 bibliographic risk too high. C is not recommended as the primary contribution because N01 and the broader corpus prevent a general absence claim for source-support/auditability evaluation.

This recommendation is not editorial approval, a final gap, or a novelty declaration.

### K. Risks, dependencies, and triggers

1. **EXP-11B editorial lag:** `SRC-03` records EXP-11B as closed/approved/integrated, while C10/C11 still characterize it as pending/prohibited. EXP-11B results are not used for 0C claims until the Claim–Evidence Matrix is formally reconciled.
2. **Group 3 pending:** SH2 and SH5 may not be inferentially closed. Any contribution/RQ requiring their final confirmation remains conditional.
3. **EXP-12 not estimable:** the original design closed without retrieval; no diversity-effect estimate exists. It cannot support a positive or negative diversity-effect claim.
4. **F1 and F3 are bounded negatives:** they do not establish universal absence or novelty.
5. **F2 has partial prior art:** differentiation survives only under `EXTERNAL_FIXED_TOP_K + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT/DELETE/SUBSTITUTE/REORDER + NO_CLASSIFICATION_FEEDBACK`.
6. **Broad F5 is falsified:** restoring “regulatory AI lacks auditability/source-support evaluation” would contradict the 0B-06 freeze.
7. **HE4 is limited:** 50 cases, AI evaluator, prompt–schema mismatch. It must not become a general system rate or legal validation.
8. **Benchmark validity:** zero shared DAMs across partitions does not remove intra-DAM dependence or cross-DAM near duplicates; Group 3 must respect the grouping unit where applicable.
9. **0B-05C:** the corrective effect is method-dependent and cannot be reduced to no numerical impact.
10. **Reproducibility:** Group 2 closed with nonblocking limitations rather than perfect reproducibility.
11. **Generalization:** empirical evidence remains restricted to Chapter 87 and the evaluated frame.
12. **Legal correctness:** identifiable evidence, source support, and auditability do not prove legally correct or binding classification.
13. **Author/editor decision:** editorial review must decide whether B is sufficiently conservative for provisional 0C positioning or whether A should become the base formulation. No new literature search is needed for that decision.
14. **Why 0C cannot yet be frozen:** Managing-AI / Lead-Editor audit and express author approval remain outstanding; additionally, any use of EXP-11B results as article claims first requires reconciliation of the C10/C11 governance lag.

`EXPERIMENTAL_REVIEW_TRIGGER = ABSENT`.

Rationale: this artifact introduces no new experimental interpretation. It consumes only states/results already recorded in freezes or `SRC-03` and retains pending inferential decisions as conditional. If later editorial review attempts to turn living EXP-11B results into new claims or close SH2/SH5 before Group 3, that later action would require the applicable gate.

### L. Traceability

- Repository: `elVladdi/gci-nandina-rag`.
- Consumed branch: `article/main-manuscript`.
- Consumed opening HEAD/commit: `75eb14b1fc1d02b8ec9ea81963cfc1d4e8739be8`.
- Executed prompt: `article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md`.
- Experimental Master Plan `SRC-03`: branch `docs/plan-maestro-temporal-2026-08-31`, HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`.
- Consumed ground truth: `0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md` and `0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.
- Consumed literature: freezes `0B-01` through `0B-06`, formal 0B closure, and `BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.
- Admitted new literature eligible for use: N01 only within its frozen limits.
- N02 was not used as determinant evidence; N03/N04 remain rejected.
- Web search performed in 0C: `NO`.
- Experiments executed/recomputed in 0C: `NO`.
- Governance files modified: `NO`.

```text
0C_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0C = NOT_PERFORMED
0D = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```
