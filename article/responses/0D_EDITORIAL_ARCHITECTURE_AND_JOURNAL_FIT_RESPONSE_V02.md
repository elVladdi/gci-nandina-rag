# 0D — Arquitectura editorial y journal fit / Editorial Architecture and Journal Fit

## Español

### A. Estado reconstruido

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
TARGET_JOURNAL = PENDING_0D
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

**ARCHIVOS LEÍDOS:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/0B_PHASE_CLOSURE.md`; `article/reviews/0C_ENTRY_GATE.md`; `article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`; `article/reviews/0C_INTERNAL_REVIEW.md`; `article/reviews/0C_AUTHOR_APPROVAL.md`; `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`; `article/reviews/0C_PHASE_CLOSURE.md`; `article/reviews/0D_ENTRY_GATE.md`; y, en modo solo lectura, `SRC-03` en `docs/plan-maestro-temporal-2026-08-31@f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`.

**FASE ACTIVA:** `0D — Arquitectura editorial y journal fit`.

**ESTADO DEL BLOQUE ASIGNADO:** `READY_FOR_DRAFTING`.

**REDACCIÓN AUTORIZADA:** sí, exclusivamente para este artefacto analítico de arquitectura editorial y journal fit. No está autorizada todavía ninguna sección del manuscrito.

**DECISIONES CONGELADAS RELEVANTES:** la recuperación histórica genera y ordena candidatos; la recuperación normativa aporta evidencia posterior sin sustituir ni reordenar el ranking; el Top-3 se fija antes de la generación; el LLM local explica ese Top-3 y no clasifica desde cero; SERIE es unidad de análisis y DAM es unidad de agrupamiento cuando existe dependencia; configurabilidad no equivale a generalización empírica; auditabilidad/trazabilidad no equivalen a corrección jurídica; la contribución provisional 0C es la alternativa B arquitectónica-metodológica.

**CLAIMS AUTORIZADOS RELEVANTES:** C01–C07, C15, C17, C19 y C21–C25 dentro de sus límites documentados. C14 permanece condicional y solo puede utilizarse con las limitaciones HE4.

**CLAIMS PROHIBIDOS O PENDIENTES RELEVANTES:** C09, C12, C13, C16 y C18 permanecen prohibidos; C20 permanece `REVIEW_REQUIRED`; C10/C11 continúan `PROHIBITED` en la matriz editorial aunque `SRC-03` ya registra EXP-11B como cerrado/aprobado/integrado. No se reconcilia ese desfase por inferencia y no se usan H150/H200 como claims del artículo.

**FUENTES EXTERNAS VERIFICADAS:** búsqueda web realizada el `2026-09-15`, exclusivamente para journal fit y requisitos editoriales actuales, usando fuentes primarias/oficiales de Elsevier/ScienceDirect y Springer Nature, además de artículos recientes publicados en las revistas evaluadas. La búsqueda no se utiliza para reabrir 0B ni para modificar el mapa de novelty/gap.

**BLOQUEOS O CONTRADICCIONES DETECTADOS:** no existe bloqueo para estructurar el artículo ni para evaluar journal fit. Persisten dos dependencias editoriales posteriores: (1) `C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE`; (2) Grupo 3 no ha iniciado y, por tanto, RQ4 y el cierre inferencial de HE2/HE5 permanecen condicionados. Las guías específicas de autor de los journals Elsevier fueron identificadas, pero el acceso web actual a ciertas páginas `Guide for Authors` de ScienceDirect devolvió restricción de acceso; por ello no se inventan límites exactos de palabras/páginas y estos deberán revalidarse antes de la eventual sumisión.

**Snapshot experimental consumido:**

```text
SRC-03 branch = docs/plan-maestro-temporal-2026-08-31
SRC-03 HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
SRC-03 blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
GROUP3 = NEXT / NOT_STARTED
```

El posicionamiento 0C congelado se preserva sin modificación:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Este contrato es el objeto diferenciador provisional. No prueba novelty por sí mismo y no autoriza afirmar que sus componentes individuales sean nuevos.

Resultados ya disponibles para futura redacción, dentro de sus límites:

- benchmark v0.2 H100/DEV/EVAL con particiones disjuntas por DAM;
- recuperación histórica H100 como **candidate retrieval**: Top-1 `0.50947`, Top-3 `709/1056 = 0.67140`, Top-5 `0.76326`, Top-10 `0.89110`, Top-50 `0.99148`, MRR `0.62971`;
- recuperación normativa BM25 plana y jerárquica como **documentary evidence retrieval**, no como classifier accuracy;
- integración histórico–normativa: `3168/3168` slots Top-3 con evidencia NANDINA-8 identificable, trazabilidad completa y preservación de orden `1.0`;
- HE4: 50 explicaciones, `28/50 = 56%` auditables bajo el protocolo cualitativo, media `11.72`, mediana `12`, con evaluador IA y las limitaciones congeladas de prompt–schema y modalidad;
- sensibilidad correctiva 0B-05C: efecto dependiente del método, no reducible a “cero impacto”;
- reproducibilidad/provenance con cierre `APPROVED_WITH_NONBLOCKING_LIMITATIONS`, no reproducibilidad perfecta.

Resultados/decisiones que no pueden tratarse todavía como cierre editorial del manuscrito:

- dirección de EXP-11B H150/H200 mientras C10/C11 no estén reconciliados;
- decisión inferencial final HE2/HE5;
- cierre de RQ4, dependiente de Grupo 3;
- cualquier efecto de diversidad de EXP-12, porque no fue estimable bajo el diseño congelado.

---

### B. Arquitectura IMRaD candidata

La arquitectura propuesta mantiene el contrato funcional de 0C como eje metodológico, separa estrictamente Methods/Results/Discussion y permite redactar primero las partes sustentadas por evidencia congelada.

| sección | subsección | propósito científico | evidencia/claims que consume | estado de redactabilidad | dependencia pendiente | riesgo editorial |
|---|---|---|---|---|---|---|
| 1. Introduction | 1.1 Problema y alcance del piloto | Delimitar recomendación NANDINA como apoyo documental offline, no decisión jurídicamente vinculante | 0A-01; C18 prohibido; alcance Clase 87 | `DEFER_TO_LATE_STAGE` | arquitectura y Results parciales estables | MEDIUM: sobredimensionar relevancia jurídica/institucional |
| 1. Introduction | 1.2 Limitación del estado del arte y posicionamiento | Presentar la separación funcional estrecha sin convertir ausencia acotada en ausencia universal | 0B freezes; F1–F5; 0C freeze | `DEFER_TO_LATE_STAGE` | Related Work redactado | HIGH: novelty/absence overclaiming |
| 1. Introduction | 1.3 Contribución provisional y RQs | Formular B y RQ1–RQ4 con sus condiciones | 0C freeze | `DEFER_TO_LATE_STAGE` | RQ4 sigue condicional a Grupo 3 | MEDIUM |
| 2. Related Work | 2.1 Clasificación HS y recuperación de candidatos | Distinguir clasificación directa, retrieval y Top-k | 0B-01/02/03 | `DRAFTABLE_NOW` | ninguna | LOW |
| 2. Related Work | 2.2 RAG, agentes y razonamiento regulatorio | Comparar sistemas donde normativa/reglas participan en decisión frente al contrato del piloto | 0B-03A/B; 0B-04B | `DRAFTABLE_NOW` | ninguna | MEDIUM: equiparar arquitecturas no equivalentes |
| 2. Related Work | 2.3 Explicabilidad, source support y auditabilidad | Situar F5 falsado y conservar auditabilidad como componente contextual | 0B-02/03/05A/06; N01 | `DRAFTABLE_NOW` | ninguna | HIGH: restaurar F5 general o legal correctness |
| 2. Related Work | 2.4 Validez, provenance y reproducibilidad | Fundamentar grouped dependence, provenance y límites de inferencia | 0B-04A/05A/05B/05C | `DRAFTABLE_NOW` | ninguna | LOW |
| 2. Related Work | 2.5 Síntesis de posicionamiento | Mostrar el contrato completo evaluado como objeto de comparación, no novelty automática | 0C freeze | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | novelty final no declarada | MEDIUM |
| 3. Methods | 3.1 Diseño, alcance y unidades | Describir piloto offline, Clase 87, SERIE/DAM y no vinculación jurídica | 0A-01/02; C06/C07/C18 | `DRAFTABLE_NOW` | ninguna | LOW |
| 3. Methods | 3.2 Datos, corpora, versionado y curación | Identidad del benchmark, hashes, corpus histórico/normativo, provenance | 0A-02; Grupo 2; C17 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | preservar limitaciones no recuperables | MEDIUM |
| 3. Methods | 3.3 Particionado v0.2 y controles de dependencia | Explicar DAM-disjoint split y near-duplicates como dimensiones distintas | C06/C07/C19; 0A-02 | `DRAFTABLE_NOW` | inferencia final Grupo 3 solo para análisis posterior | LOW |
| 3. Methods | 3.4 Recuperación histórica y Top-k/Top-3 fijo | Definir candidate generation/ranking principal | C01; D-004/D-005 | `DRAFTABLE_NOW` | ninguna | LOW |
| 3. Methods | 3.5 Recuperación normativa post-ranking | Definir retrieval documental posterior, sin reranking | C02; EV-03/EV-04 | `DRAFTABLE_NOW` | ninguna | LOW |
| 3. Methods | 3.6 Integración candidato–evidencia e invariancia | Especificar contrato de preservación del ranking y trazabilidad | EV-06; 0C B | `DRAFTABLE_NOW` | ninguna | LOW |
| 3. Methods | 3.7 LLM local y explicación controlada | Documentar Top-3 inmutable, contexto y prohibiciones de modificación | C03; OE4/HE4 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | HE4 limitations deben quedar explícitas | MEDIUM |
| 3. Methods | 3.8 Diseño de evaluación por función | Separar candidate retrieval, evidence retrieval, invariancia y HE4 | C04/C05/C14; 0A-02 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | Grupo 3 para inferencia final | MEDIUM |
| 3. Methods | 3.9 Validez, drift y reproducibilidad | Explicar near-duplicates, concentración, drift 0B-05C y provenance | C21–C25; Grupo 2 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | ninguna para descripción; inferencia final RQ4 sí depende de Grupo 3 | MEDIUM |
| 4. Results | 4.1 Benchmark y controles del split | Reportar composición y cero overlap DAM inter-partición | C06/C07 | `DRAFTABLE_NOW` | ninguna | LOW |
| 4. Results | 4.2 Recuperación histórica de candidatos — RQ1 | Reportar Top-k/MRR H100 como candidate retrieval | C04/C05 | `DRAFTABLE_NOW` | ninguna | LOW si no se denomina accuracy global |
| 4. Results | 4.3 Recuperación normativa e integración — RQ2 | Reportar BM25 normativo, cobertura de evidencia, trazabilidad e invariancia | EV-03/04/06; C02 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | ninguna | MEDIUM: no convertir coverage en correctness |
| 4. Results | 4.4 Explicación controlada — RQ3 | Reportar estructura/traceability HE4 y límites | C14; EV-08 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | ninguna, pero interpretación estrictamente acotada | HIGH: muestra/evaluador/schema |
| 4. Results | 4.5 Sensibilidades y validez documental | Reportar 0B-05C y otros resultados congelados pertinentes sin inferencia nueva | C21–C25; EXP-11A solo descriptivo | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | EXP-11B no utilizable hasta C10/C11 | MEDIUM |
| 4. Results | 4.6 Cierre inferencial de validez — RQ4 | Resolver dependencia, límites y HE2/HE5 bajo el gate inferencial | Grupo 3 | `BLOCKED_BY_GROUP3` | Grupo 3 | HIGH si se anticipa |
| 4. Results | 4.7 EXP-11B, si editorialmente se incorpora | Usar resultados H150/H200 solo tras autorización claim-level | SRC-03 + futura reconciliación | `BLOCKED_BY_C10_C11_RECONCILIATION` | C10/C11 | HIGH |
| 5. Discussion | 5.1 Significado del contrato funcional | Interpretar separación de ranking/evidencia/explicación sin vender componentes como nuevos | Results finales + 0C | `BLOCKED_BY_FINAL_RESULTS` | Grupo 3 y claims finales | MEDIUM |
| 5. Discussion | 5.2 Comparación con prior art | Contrastar con candidate prediction, RAG/agents y source-support prior art | 0B + N01 | `BLOCKED_BY_FINAL_RESULTS` | Results finales | HIGH: novelty overclaiming |
| 5. Discussion | 5.3 Implicaciones para apoyo a decisiones | Discutir auditabilidad documental como soporte, no corrección jurídica | C12/C13/C18 prohibidos; C14 condicional | `BLOCKED_BY_FINAL_RESULTS` | Results finales | HIGH |
| 5. Discussion | 5.4 Validez y transferibilidad | Separar validez interna, reproducibilidad, configurabilidad y generalización | C15–C17; RQ4 | `BLOCKED_BY_GROUP3` | Grupo 3 | HIGH |
| 6. Limitations | 6.1 Límites del benchmark y datos | Clase 87, DAM, near-duplicates, concentración | 0A-02 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | consolidación final después de Grupo 3 | MEDIUM |
| 6. Limitations | 6.2 HE4 y auditabilidad | Muestra 50, evaluador IA, prompt–schema mismatch | EV-08/C14 | `DRAFTABLE_NOW` | ninguna | LOW si se conserva textual |
| 6. Limitations | 6.3 Normativa y drift | Snapshot vs estado normativo actual; impacto dependiente del método | C21–C25 | `DRAFTABLE_NOW` | ninguna | MEDIUM |
| 6. Limitations | 6.4 Reproducibilidad y external validity | Limitaciones no bloqueantes; no generalización fuera de Clase 87 | Grupo 2; C16 prohibido | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | cierre final de resultados | MEDIUM |
| 7. Conclusions | — | Responder RQs y sintetizar alcance, sin extenderlo | Results/Discussion finales | `DEFER_TO_LATE_STAGE` | Grupo 3 + Results/Discussion | HIGH si se anticipa |
| Data/Code Availability | — | Declarar fuentes, repositorios, artefactos reproducibles y restricciones | D-006; C17; Grupo 2 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | verificar snapshot final antes de envío | LOW |
| Declarations | AI use, funding, competing interests, author contributions | Cumplir requisitos del journal/editorial | políticas publisher vigentes | `DEFER_TO_LATE_STAGE` | target final | LOW |

**Principio de no duplicación:** Methods describe el contrato y cómo se mide; Results presenta únicamente observaciones; Discussion interpreta su significado y contraste con prior art. Los riesgos de validez detallados se centralizan en Limitations, mientras Methods solo registra los controles necesarios para reproducir el diseño.

---

### C. Mapa de tablas y figuras

| ID | tipo | contenido | sección | función científica | fuente de datos | estado | dependencia |
|---|---|---|---|---|---|---|---|
| Fig. 1 | figura de arquitectura | Contrato funcional completo: histórico fija ranking → normativa documenta sin reranking → LLM explica Top-3 inmutable, con prohibición de feedback | Methods | Hacer visible la separación arquitectónica/funcional que sostiene la contribución B | 0A-01; D-005; 0C freeze | `ESSENTIAL_NOW` | ninguna |
| Tabla 1 | tabla de benchmark | H100/DEV/EVAL: series, DAM, códigos, hashes, cero overlap DAM | Methods/Results 4.1 | Delimitar unidades y control de particiones | EV-01/0A-02 | `ESSENTIAL_NOW` | ninguna |
| Tabla 2 | tabla metodológica | Componente → tarea → output → métrica → interpretación permitida/prohibida | Methods | Evitar confundir candidate retrieval, evidence retrieval y auditability | 0A-02; C01–C14 | `ESSENTIAL_NOW` | ninguna |
| Tabla 3 | resultados | H100 Top-1/3/5/10/50 y MRR | Results 4.2 | Responder RQ1 como candidate retrieval | EV-02; C04/C05 | `ESSENTIAL_NOW` | ninguna |
| Tabla 4 | resultados integrados | BM25 normativo plano/jerárquico + asociación `3168/3168` + trazabilidad + preservación de orden | Results 4.3 | Responder RQ2 separando retrieval documental de invariancia | EV-03/04/06 | `ESSENTIAL_NOW` | límites de correctness explícitos |
| Tabla 5 | resultados/limitaciones | HE4: 50 casos, 28/50 auditables, media/mediana y limitaciones de protocolo | Results 4.4 | Responder RQ3 sin ocultar limitaciones | EV-08; C14 | `ESSENTIAL_NOW` | ninguna, pero interpretación acotada |
| Tabla 6 | sensibilidad | Resumen 0B-05C por método: drift, overlap y efectos EV03/EV04/D1a | Results 4.5 / Limitations | Mostrar que drift documental y efecto métrico son dimensiones distintas | C21–C25 | `ESSENTIAL_NOW` | ninguna |
| Tabla 7 | literatura comparativa | Prior art más cercano vs propiedades del contrato B, sin lenguaje de novelty | Related Work 2.5 | Sintetizar posicionamiento de forma trazable | freezes 0B + N01 | `OPTIONAL` | seleccionar solo antecedentes determinantes |
| Fig. 2 | figura de validez | Mapa de amenazas/controles: DAM split, near-duplicates, concentración, drift, reproducibilidad | Methods/Limitations | Integrar validez sin repetir múltiples tablas | 0A-02; Grupo 2; 0B-05C | `OPTIONAL` | podría omitirse si aumenta densidad gráfica |
| Tabla 8 | resultados inferenciales | Cierre de Grupo 3 y respuesta final a RQ4/HE2/HE5 | Results 4.6 | Incorporar inferencia final | Grupo 3 | `ESSENTIAL_AFTER_PENDING_EXPERIMENT` | Grupo 3 |
| Tabla 9 | EXP-11B | H150/H200 y contraste autorizado si la gobernanza editorial lo permite | Results 4.7 | Solo si aporta al paper después de reconciliación | SRC-03 + futura Claim Matrix | `ESSENTIAL_AFTER_PENDING_EXPERIMENT` si se integra; de otro modo omitir | C10/C11 reconciliation |
| Fig. 3 | curva de sensibilidad por tamaño/composición | EXP-11A/11B | Results/Discussion | Visualizar sensibilidad descriptiva | EXP-11A/11B | `NOT_RECOMMENDED` por ahora | riesgo de sugerir causalidad y C10/C11 no reconciliado |

La arquitectura visual recomendada es deliberadamente compacta: una figura principal de arquitectura, 5–6 tablas esenciales con evidencia ya gobernada y, posteriormente, una tabla inferencial de Grupo 3. No se recomienda multiplicar diagramas que repitan el mismo pipeline.

---

### D. Matriz de redactabilidad inmediata

| bloque | estado | justificación |
|---|---|---|
| Methods 3.1, 3.3–3.6 | `DRAFTABLE_NOW` | arquitectura, unidades, split y contrato funcional están congelados y no dependen de Grupo 3 |
| Methods 3.2, 3.7–3.9 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | pueden redactarse, pero deben conservar provenance no perfecto, límites HE4 y drift normativo |
| Related Work 2.1–2.4 | `DRAFTABLE_NOW` | 0B está cerrado/frozen y no requiere nueva búsqueda de gap |
| Related Work 2.5 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | posicionamiento B es provisional; final gap/novelty siguen no definidos |
| Results 4.1–4.2 | `DRAFTABLE_NOW` | benchmark/split y H100 están congelados |
| Results 4.3–4.5 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | evidencia disponible, pero coverage/auditability/drift tienen límites interpretativos estrictos |
| Results 4.6 | `BLOCKED_BY_GROUP3` | RQ4 y cierre HE2/HE5 no pueden anticiparse |
| Results 4.7 | `BLOCKED_BY_C10_C11_RECONCILIATION` | EXP-11B vive en SRC-03 pero no está autorizado editorialmente como claim |
| Introduction | `DEFER_TO_LATE_STAGE` | D-003 ordena redactarla después de Methods, Related Work y Results congelados iniciales |
| Discussion 5.1–5.3 | `BLOCKED_BY_FINAL_RESULTS` | una discusión válida debe interpretar el conjunto final de resultados y no solo snapshots parciales |
| Discussion 5.4 | `BLOCKED_BY_GROUP3` | transferibilidad/validez final depende de RQ4 y cierre inferencial |
| Limitations 6.1–6.4 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | existe suficiente evidencia para un borrador técnico, pero debe ajustarse tras Grupo 3 |
| Conclusions | `DEFER_TO_LATE_STAGE` | depende de respuesta final de RQs y Discussion |
| Abstract y Title definitivo | `DEFER_TO_LATE_STAGE` | expresamente bloqueados hasta manuscrito completo |
| Data/Code Availability | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | repositorios/provenance existen, pero debe verificarse snapshot final y assets no recuperables |
| Declaraciones editoriales | `DEFER_TO_LATE_STAGE` | dependen del journal finalmente aprobado y del uso real de IA durante preparación |

Si la Fase 0 fuera posteriormente aprobada, el orden operativo coherente con D-003 sería: **Methods → Related Work → Results congelados disponibles → figuras/tablas preliminares → Introduction provisional**, manteniendo bloqueados Grupo 3, EXP-11B no reconciliado, Results definitivos, Discussion, Conclusions, Abstract y Title.

---

### E. Journal-fit screening

#### E.1 Regla de evaluación

La escala `HIGH/MEDIUM/LOW` expresa ajuste científico o, en la columna de riesgo, magnitud del riesgo. No se usan factor de impacto, CiteScore o cuartil como sustituto de fit. La verificación web del `2026-09-15` se limitó a fuentes oficiales/primarias y artículos publicados en las propias revistas.

Para las cinco revistas Elsevier se verificó la política general vigente de IA para autores: el uso de herramientas generativas en preparación debe mantenerse bajo supervisión humana y, cuando corresponde, declararse mediante una declaración específica; el uso de IA como parte del método de investigación debe describirse reproduciblemente en Methods. También se verificó la política general de research data/data statements; el requisito exacto depende de la guía específica de cada journal. Las páginas específicas `Guide for Authors` de ScienceDirect se identificaron, pero el acceso directo no permitió verificar de forma confiable límites exactos de extensión; se registra esto como limitación y no se inventan cifras.

| journal | scope fit | contribution fit | methods/results fit | novelty expectation risk | empirical-scope fit | explainability/auditability fit | reproducibility/open-science fit | recent related articles | structural/length constraints | operational notes | overall fit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Knowledge-Based Systems (KBS)** | HIGH — IA, knowledge-based systems, knowledge engineering, intelligent decision support | HIGH — el contrato B puede formularse como diseño/evaluación de un sistema basado en conocimiento con roles diferenciados | HIGH — retrieval, knowledge representation, decision support y explicación encajan | MEDIUM — la revista exige resultados originales/innovadores; no basta ensamblar técnicas conocidas | HIGH — un caso Clase 87 puede funcionar como caso aplicado si la contribución metodológica es transferible como diseño, no como generalización empírica | HIGH | HIGH — compatible con data/code statements y trazabilidad; requisitos exactos se revalidan en guía | KBS 295 (2024) 111761, DOI `10.1016/j.knosys.2024.111761`; KBS 303 (2024) 112410, DOI `10.1016/j.knosys.2024.112410`; KBS 311 (2025) 113047, DOI `10.1016/j.knosys.2025.113047` | límite exacto no verificable en acceso web actual; estructura IMRaD propuesta es compatible con research article estándar | Elsevier; AI declaration y research-data policy aplicables según guía | **HIGH** |
| **Expert Systems with Applications (ESWA)** | HIGH — expert/intelligent systems en industria, gobierno, law, auditing, information retrieval, knowledge management | HIGH — sistema híbrido aplicado con evaluación funcional | HIGH | HIGH — scope enfatiza contribución genuina y desalienta mero reempaquetado de conceptos existentes | HIGH — aplicación aduanera/gobierno encaja, pero debe trascender un caso local | HIGH | HIGH | ESWA 255 (2024) 124710, DOI `10.1016/j.eswa.2024.124710`; ESWA 297 (2026) 129508, DOI `10.1016/j.eswa.2025.129508` | límite exacto no verificable en acceso web actual | Muy adecuado si se demuestra con claridad qué aporta el contrato funcional y no solo la integración de BM25/LLM | **HIGH** |
| **Information Processing & Management (IPM)** | HIGH — intersección computing/information science, métodos, critical applications y system design | HIGH — recuperación, evidencia, provenance y separación de funciones son centrales | HIGH | MEDIUM — requiere avance claro en métodos o system-design research, pero admite critical applications | HIGH — el dominio aduanero puede funcionar como aplicación crítica si la lección de IR/gestión de información es explícita | HIGH | HIGH | IPM 63(2) (2026) 104369, DOI `10.1016/j.ipm.2025.104369`; IPM 61(4) (2024) 103732, DOI `10.1016/j.ipm.2024.103732` | límite exacto no verificable en acceso web actual | El framing debe centrarse en information retrieval/evidence architecture más que en “expert system” | **HIGH** |
| **Decision Support Systems (DSS)** | MEDIUM — encaja si el paper demuestra contribución a soporte de decisión, no solo a IR | MEDIUM — el contrato auditable es pertinente, pero el estudio no mide directamente desempeño del decisor humano | MEDIUM | HIGH — DSS exige relevancia teórica/técnica para decisión mejorada y general implications | MEDIUM — Clase 87 es aceptable como caso si produce implicaciones generales de DSS, hoy no demostradas empíricamente | HIGH | HIGH | DSS 184 (2024) 114276, DOI `10.1016/j.dss.2024.114276` | límite exacto no verificable en acceso web actual | Riesgo de desk rejection si el artículo parece principalmente retrieval/NLP sin evaluación del decisor | **MEDIUM** |
| **Government Information Quarterly (GIQ)** | MEDIUM — aduanas pertenece al gobierno y la revista cubre IT, accountability y decisión pública | LOW — la contribución B es técnica y no estudia política pública, adopción, ciudadanos, organización o valor público | MEDIUM | HIGH — requiere contribución sustantiva al cruce gobierno–información–tecnología | MEDIUM — el caso SUNAT/aduanero es relevante, pero el paper no evalúa implementación organizacional ni consecuencias públicas | HIGH conceptualmente, pero no suficiente | MEDIUM-HIGH | GIQ 41(4) (2024) 101976, DOI `10.1016/j.giq.2024.101976`; GIQ 41(1) (2024) 101906, DOI `10.1016/j.giq.2023.101906`; GIQ 41(1) (2024) 101914 | límite exacto no verificable en acceso web actual | Mejor fit si hubiera estudio de gobernanza/adopción/usuarios; no debe forzarse ese framing | **LOW** |
| **Artificial Intelligence and Law** | MEDIUM — publica modelos computacionales de derecho, legal reasoning y AI aplicada al dominio jurídico | LOW-MEDIUM — el piloto usa normativa como evidencia, pero evita deliberadamente afirmar razonamiento jurídico/corrección legal | MEDIUM | HIGH — la revista esperaría una contribución genuina a AI & Law, no solo contexto regulatorio | MEDIUM — aduanas es un dominio regulatorio, pero el experimento no adjudica legal correctness | HIGH en trazabilidad legal, pero la evidencia recuperada no decide jurídicamente | HIGH — guía Springer incluye data availability, SI y reglas detalladas | Mentzingen et al. (2025), DOI `10.1007/s10506-025-09440-2`; Italiani et al. (2025), DOI `10.1007/s10506-025-09463-9` | double-blind; abstract 150–250 palabras; 4–6 keywords; hasta tres niveles de headings; Word/LaTeX; data availability y SI; requisitos exactos verificados en guía oficial | LLM no puede ser autor; uso sustantivo de LLM debe documentarse; AI-assisted copy editing no requiere declaración según guía actual | **LOW** |

#### E.2 Evidencia web principal por revista

**Knowledge-Based Systems.** La descripción oficial de Elsevier define KBS como journal internacional/interdisciplinario de IA orientado a sistemas basados en conocimiento y otras técnicas de IA, con objetivos explícitos de apoyar predicción/decisión humana y combinar teoría con estudio práctico. Artículos recientes incluyen decision support explicable, RAG con conocimiento de diseño y semantic/LLM knowledge retrieval. Esto ofrece un encaje directo con el framing arquitectónico-metodológico B, siempre que el aporte se presente en el nivel del contrato funcional evaluado.

**Expert Systems with Applications.** La descripción oficial incluye sistemas inteligentes aplicados en gobierno, law, auditing, information retrieval, information management y knowledge management. Sin embargo, la propia página enfatiza “genuine innovation” y advierte contra renombrar/reempaquetar conceptos conocidos, por lo que el artículo tendría que demostrar que la restricción contractual y su evaluación producen una contribución técnica defendible, no simplemente una integración aplicada.

**Information Processing & Management.** La descripción oficial acepta research, methods, review y critical-application manuscripts en la intersección computing–information science. Artículos recientes en evidence-aware RAG y XAI/decision performance muestran compatibilidad temática con retrieval, evidencia y explicación. Su fit aumenta si el paper enfatiza arquitectura de información, retrieval y evidencia, no “legal reasoning”.

**Decision Support Systems.** El scope exige relevancia a problemas teóricos/técnicos de soporte de decisión, incluyendo funcionalidad, implementación, evaluación e impacto. El piloto es un sistema de apoyo potencial, pero la revisión experta está fuera del sistema y no se midió impacto del decisor, por lo que el fit es más débil que en KBS/ESWA/IPM.

**Government Information Quarterly.** El scope cubre gobierno, IT, accountability y herramientas para decisión pública; no obstante, sus artículos recientes se orientan a implementación, gobernanza, percepciones, public values y policy/organizational fit. El manuscrito actual no evalúa esas dimensiones, por lo que convertir el contexto aduanero en un paper de GIQ exigiría un framing que la evidencia no sostiene.

**Artificial Intelligence and Law.** La revista cubre modelos computacionales del derecho/legal reasoning y aplicaciones de IA al dominio legal. Existen trabajos recientes sobre retrieval de precedentes y legal QA, pero el presente proyecto separa explícitamente evidence retrieval de legal correctness y no evalúa razonamiento jurídico adjudicado. Esto reduce su fit como target principal.

---

### F. Deep dive Top-3 journals

#### F.1 Knowledge-Based Systems — candidato 1

1. **Razón de fit científico.** KBS alinea simultáneamente knowledge-based systems, knowledge representation/engineering, intelligent decision support y aplicaciones prácticas. El contrato B puede describirse como una arquitectura de conocimiento con responsabilidades restringidas: precedentes históricos para ranking, normativa para evidencia y LLM para explicación downstream.
2. **Posibles motivos de desk rejection.** Contribución percibida como mera integración de BM25 + normas + LLM; foco excesivamente local en NANDINA Clase 87; novelty insuficientemente diferenciada del prior art RAG/agentic; ausencia de generalización externa; HE4 limitado.
3. **Énfasis editorial requerido.** El paper debe centrarse en el **contrato funcional evaluado**, las invariancias verificables y la separación de métricas por función. El dominio aduanero debe operar como caso regulatorio exigente, no como sustituto de una contribución metodológica.
4. **Qué fortalecer/atenuar.** Fortalecer definición formal de interfaces y prohibiciones de cada módulo, trazabilidad, grouped split, invariancia y evaluación function-specific. Atenuar cualquier lenguaje de “first”, superioridad general, legal correctness o generalización.
5. **Compatibilidad con B.** `HIGH`: B está naturalmente expresada como arquitectura de sistema basada en conocimiento.
6. **Compatibilidad con Clase 87.** `HIGH` si se declara como evaluación acotada y se evita extrapolación empírica.
7. **Compatibilidad con RQ1–RQ4.** RQ1/RQ2 encajan directamente; RQ3 aporta explicación; RQ4 aporta validez y debe permanecer condicionada a Grupo 3.
8. **Compatibilidad con resultados pendientes.** Se puede construir Methods/Related Work y Results parciales; la versión final deberá esperar Grupo 3 y cualquier reconciliación EXP-11B que se decida incorporar.
9. **Artículos recientes relevantes.** Abbaspour Onari et al., KBS 295 (2024), `10.1016/j.knosys.2024.111761`; Siddharth & Luo, KBS 303 (2024), `10.1016/j.knosys.2024.112410`; Ghali et al., KBS 311 (2025), `10.1016/j.knosys.2025.113047`.
10. **Requisitos editoriales condicionantes.** Aplican políticas Elsevier vigentes de AI disclosure y research data; el límite exacto de extensión debe revalidarse en la guía KBS antes de envío. La arquitectura propuesta ya reserva Data/Code Availability y Declarations.

**Dictamen 0D:** mejor equilibrio entre arquitectura B, knowledge retrieval, evidence support y explicación controlada.

#### F.2 Expert Systems with Applications — candidato 2

1. **Razón de fit científico.** ESWA publica diseño, desarrollo, testing e implementación de sistemas inteligentes en dominios que incluyen gobierno, law, auditing e information retrieval. El piloto es claramente un sistema experto/inteligente aplicado con evaluación multi-función.
2. **Posibles motivos de desk rejection.** La propia revista exige contribución genuina; un pipeline compuesto por técnicas conocidas puede percibirse como incremental. El H100/Clase 87 y HE4 limitado podrían verse como evidencia empírica demasiado acotada si la contribución no está formalizada.
3. **Énfasis editorial requerido.** Formular la contribución como **restricción arquitectónica verificable + protocolo de evaluación**, no como “aplicación de RAG a aduanas”.
4. **Qué fortalecer/atenuar.** Fortalecer contraste con sistemas que dejan a la normativa/LLM modificar la decisión; hacer visibles las pruebas de preservación de ranking y separación de outputs. Atenuar la narrativa de auditabilidad como novelty independiente porque F5 fue falsado.
5. **Compatibilidad con B.** `HIGH`.
6. **Compatibilidad con Clase 87.** `HIGH` para una aplicación experta, siempre que el alcance quede explícito.
7. **Compatibilidad con RQ1–RQ4.** `HIGH`, aunque RQ4 requiere cierre de Grupo 3.
8. **Compatibilidad con resultados pendientes.** Similar a KBS; publicación final exige resultados suficientemente cerrados, pero Methods/Related Work son redactables antes.
9. **Artículos recientes relevantes.** Abusitta et al., ESWA 255 (2024), `10.1016/j.eswa.2024.124710`; Luo et al., ESWA 297 (2026), `10.1016/j.eswa.2025.129508`.
10. **Requisitos editoriales condicionantes.** Políticas Elsevier de AI disclosure y research data; límites exactos de extensión no verificados en el acceso web actual y deberán revalidarse en la guía oficial.

**Dictamen 0D:** alternativa fuerte, pero con riesgo de novelty más alto que KBS porque el journal explicita una expectativa de innovación genuina frente a repackaging.

#### F.3 Information Processing & Management — candidato 3

1. **Razón de fit científico.** IPM cubre teoría, métodos y critical applications en la intersección computing–information science. El proyecto se puede posicionar como gestión/recuperación de información con separación de evidence retrieval, provenance y generación controlada.
2. **Posibles motivos de desk rejection.** El artículo podría parecer más un expert system/domain application que una contribución a information processing; el componente normativo/LLM podría dominar sin suficiente análisis del retrieval.
3. **Énfasis editorial requerido.** Resaltar arquitectura de recuperación, evidencia, source traceability, función de cada métrica y control de dependencia; tratar el LLM como consumidor downstream, no como núcleo de novelty.
4. **Qué fortalecer/atenuar.** Fortalecer RQ1/RQ2, evidencia/invariancia y provenance. Atenuar framing legal y claims de decision support humano no evaluado.
5. **Compatibilidad con B.** `HIGH`, especialmente la separación functional `candidate retrieval ≠ evidence retrieval ≠ explanation`.
6. **Compatibilidad con Clase 87.** `HIGH` como critical application si las lecciones metodológicas son explícitas y no se confunde con generalización.
7. **Compatibilidad con RQ1–RQ4.** RQ1/RQ2 son muy fuertes; RQ3 es complementaria; RQ4 añade validez metodológica.
8. **Compatibilidad con resultados pendientes.** El paper puede estructurarse con resultados congelados, pero la Discussion final requiere Grupo 3.
9. **Artículos recientes relevantes.** Li et al., IPM 63(2) (2026), `10.1016/j.ipm.2025.104369`; Wang & Ding, IPM 61(4) (2024), `10.1016/j.ipm.2024.103732`.
10. **Requisitos editoriales condicionantes.** Políticas Elsevier de AI disclosure y research data; límites específicos de extensión deben revalidarse antes de envío.

**Dictamen 0D:** excelente alternativa si el artículo se orienta más a retrieval/evidence architecture que a sistema experto aplicado.

---

### G. Target principal y alternativas

```text
PRIMARY_TARGET = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
```

#### PRIMARY_TARGET — Knowledge-Based Systems

**Justificación científica.** Es el mejor ajuste al objeto que 0C congeló: un contrato arquitectónico-metodológico evaluado donde distintas fuentes de conocimiento cumplen funciones no intercambiables y un generador downstream está restringido por diseño. KBS combina explícitamente knowledge-based systems, knowledge engineering, intelligent decision support y aplicaciones prácticas, y publica trabajos recientes sobre retrieval, RAG, conocimiento explícito y explicabilidad.

**Riesgos.** El principal es que la contribución se interprete como una integración incremental de componentes conocidos. El alcance Clase 87 y las limitaciones HE4 reducen la amplitud empírica. El final gap y novelty siguen no definidos.

**Ajustes de framing necesarios.** Presentar el “qué” novedoso, si posteriormente fuese autorizado, solo al nivel del **contrato funcional completo y su evaluación**, nunca al nivel de BM25, Top-k, RAG, normative evidence, LLM o auditability por separado. El artículo debe mostrar interfaces, invariantes y métricas específicas por función. La aplicación aduanera debe enmarcarse como escenario de alta exigencia documental y no como evidencia de corrección jurídica.

**Estructura recomendada.** La arquitectura IMRaD de la sección B es compatible: Related Work orientado por funciones; Methods centrado en contrato, datos, partición y evaluación; Results separados por RQ1–RQ3 y posteriormente RQ4; Discussion sobre separación funcional y límites; Limitations técnica y explícita.

**Por qué supera a las alternativas.** Frente a ESWA, KBS requiere menos dependencia del argumento de “aplicación experta” y permite enfatizar la arquitectura de conocimiento. Frente a IPM, KBS acomoda mejor el sistema completo, incluida la capa de explicación controlada y decision support, sin exigir que el aporte sea principalmente una innovación de IR.

#### ALTERNATIVE_TARGET_1 — Expert Systems with Applications

Se recomienda como primera alternativa por su fit directo con sistemas expertos/inteligentes, información retrieval, government/law/auditing y evaluación de aplicaciones. Queda detrás de KBS porque su expectativa explícita de “genuine innovation” incrementa el riesgo si la contribución B no se articula con precisión suficiente frente al prior art.

#### ALTERNATIVE_TARGET_2 — Information Processing & Management

Se recomienda como segunda alternativa por el fuerte ajuste a retrieval, evidence, provenance e information-processing architecture. Queda detrás de KBS porque exige desplazar el centro narrativo desde el sistema completo hacia la contribución de IR/information science, lo que podría subrepresentar la función del contrato de explicación controlada.

**Journals no seleccionados.** DSS conserva fit medio, pero el proyecto no evalúa impacto del decisor humano; GIQ exigiría una contribución pública/organizacional que no fue estudiada; AI & Law exigiría un énfasis en legal reasoning/correctness que el diseño explícitamente no afirma.

Esta selección es una recomendación 0D para auditoría editorial y aprobación del autor. No constituye elección definitiva del journal.

---

### H. Riesgos y mitigaciones

| riesgo | nivel | fundamento | mitigación obligatoria |
|---|---|---|---|
| Novelty risk | HIGH | F1/F3 son negativos acotados; F2 tiene prior art parcial; F5 general fue falsado | Mantener `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED`; argumentar solo diferenciación del contrato completo; no usar “first/no prior work” |
| Overclaiming | HIGH | Es fácil convertir 67.14% Top-3 en system accuracy, 3168/3168 en correctness o HE4 en legal validation | Tabla metodológica de interpretación permitida/prohibida; revisión claim-by-claim |
| Internal validity | MEDIUM | Split DAM-disjoint mejora validez, pero existe dependencia intra-DAM y concentración | Mantener DAM como agrupamiento y esperar Grupo 3 para inferencia final |
| Grouped dependence | MEDIUM | 1,056 series pertenecen a 67 DAM; no son 1,056 observaciones independientes para toda inferencia | Usar análisis/inferencia compatible con DAM cuando corresponda; no anticipar Grupo 3 |
| Leakage / near-duplicates | MEDIUM | Cero DAM overlap no elimina exact/near-duplicate cross-DAM | Reportar exact/near duplicate como amenaza distinta; sensibilidad/limitación explícita |
| External validity/generalization | HIGH | Evaluación empírica restringida a Clase 87 y marco SUNAT/NANDINA del piloto | Formular configurabilidad como propiedad de diseño; prohibir generalización empírica fuera de Clase 87 |
| HE4 limitations | HIGH | N=50, evaluador IA, mismatch prompt–schema, modalidad desviada | Presentar HE4 como evidencia limitada de estructura/trazabilidad; no correctness/legal validation |
| Normative-source drift | MEDIUM | Decision 885 snapshot vs Decision 906 vigente produjo drift y efecto dependiente del método | Preservar C21–C25; distinguir snapshot, overlap y metric impact; no resumir como “cero impacto” |
| Reproducibility limitations | MEDIUM | Grupo 2 cerró con limitaciones no bloqueantes y assets no completamente recuperables | Data/Code Availability transparente; separar provenance de reproducibilidad perfecta |
| Group-3 dependency | HIGH | RQ4 y HE2/HE5 no están cerradas inferencialmente | Bloquear Results 4.6, Discussion final y Conclusions hasta Grupo 3 |
| C10/C11 governance lag | HIGH | EXP-11B cerrado en SRC-03, pero Claim Matrix lo mantiene prohibido por wording histórico | No usar H150/H200; reconciliación explícita antes de cualquier claim/tabla EXP-11B |
| B vs KBS expectations | MEDIUM | KBS espera investigación original/innovadora y puede considerar la arquitectura una integración | Formalizar interfaces/invariantes, hacer explícitas la separación arquitectónica/funcional y la función diferenciada de cada evaluación; evitar novelty de componentes |
| B vs ESWA expectations | HIGH | ESWA enfatiza genuine innovation frente a repackaging | Solo usar ESWA si la contribución arquitectónica queda formalizada y comparada rigurosamente |
| B vs IPM expectations | MEDIUM | IPM puede exigir un aporte más nítido a information science/IR | En ese target, enfatizar retrieval/evidence/provenance y evaluación function-specific |
| Journal-specific author-guide access | LOW | Las páginas exactas de Guide for Authors Elsevier no pudieron verificarse íntegramente en el acceso web actual | Revalidar extensión, estructura, data policy y submission checklist inmediatamente antes de envío |
| AI-use disclosure | LOW | Elsevier y Springer tienen políticas explícitas actuales | Mantener registro de uso de IA; añadir declaración conforme al target final; responsabilidad humana y verificación integral |

No se detecta un riesgo que invalide por sí solo la arquitectura B. Los riesgos altos están concentrados en novelty/overclaiming, HE4, external validity y dependencias aún abiertas, todos controlables mediante gates y alcance explícito.

---

### I. Gate de Fase 0

```text
PHASE_0_GATE = PASS_WITH_CORRECTIONS
```

**Fundamento.** La arquitectura editorial ya puede definirse de forma coherente; 0A, 0B y 0C están cerrados; existe un target principal defendible; Methods, Related Work y varios Results congelados son redactables sin reinterpretación experimental. Sin embargo, la Fase 0 no debería cerrar como `PASS` limpio porque persisten condiciones editoriales explícitas que afectan el contenido final:

1. C10/C11 deben reconciliarse antes de cualquier uso de EXP-11B en el artículo.
2. Grupo 3 debe cerrarse antes de responder definitivamente RQ4, cerrar HE2/HE5 y redactar Results/Discussion/Conclusions finales.
3. El final gap y novelty continúan `NOT_DEFINED / NOT_DECLARED`; no deben inferirse de journal fit.
4. Los requisitos exactos del `Guide for Authors` del target finalmente aprobado deben revalidarse antes de sumisión, dado que el acceso web actual no permitió verificar todos los límites específicos de las revistas Elsevier.

**Qué podría autorizarse si este gate fuese posteriormente aprobado por la IA Gestora y el autor:** apertura de la secuencia de redacción prevista en D-003/ARTICLE_WRITING_PLAN — Methods, Related Work, Results congelados disponibles y después figuras/tablas preliminares e Introduction provisional — manteniendo bloqueados EXP-11B no reconciliado, Grupo 3/RQ4, Results definitivos, Discussion final, Conclusions, Abstract y Title definitivo.

Este artefacto no autoriza por sí mismo esa apertura.

```text
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

No se introduce ninguna interpretación experimental nueva. El artefacto solo organiza editorialmente evidencia congelada y usa investigación web para journal fit/requisitos actuales. Las dependencias experimentales se preservan como bloqueos, no se resuelven.

---

### J. Trazabilidad

**Repositorio y corte editorial consumido**

- repositorio: `elVladdi/gci-nandina-rag`;
- rama: `article/main-manuscript`;
- commit/HEAD de apertura 0D: `113500a0745cb10a8e29761c67879fa3d19aa3ad`;
- mensaje: `article: activate 0D editorial architecture and journal fit`.

**SRC-03 consumido en solo lectura**

- rama: `docs/plan-maestro-temporal-2026-08-31`;
- HEAD: `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`;
- blob registrado: `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`.

**Fecha de búsqueda web de journal fit:** `2026-09-15`.

**Fuentes oficiales de scope/políticas**

- Knowledge-Based Systems — Elsevier: `https://shop.elsevier.com/journals/knowledge-based-systems/0950-7051`
- Expert Systems with Applications — Elsevier: `https://shop.elsevier.com/journals/expert-systems-with-applications/0957-4174`
- Information Processing & Management — Elsevier: `https://shop.elsevier.com/journals/information-processing-and-management/0306-4573`
- Decision Support Systems — Elsevier: `https://shop.elsevier.com/journals/decision-support-systems/0167-9236`
- Government Information Quarterly — Elsevier: `https://shop.elsevier.com/journals/government-information-quarterly/0740-624X`
- Artificial Intelligence and Law — Springer Nature: `https://link.springer.com/journal/10506`
- AI & Law submission guidelines: `https://link.springer.com/journal/10506/submission-guidelines`
- Elsevier generative-AI policy for journals: `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals`
- Elsevier research-data statement: `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement`
- Elsevier research-data guidelines: `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines`

**Artículos recientes usados solo para demostrar fit temático, no novelty**

- Abbaspour Onari et al. (2024), *An explainable data-driven decision support framework for strategic customer development*, Knowledge-Based Systems 295, 111761, DOI `10.1016/j.knosys.2024.111761`.
- Siddharth & Luo (2024), *Retrieval augmented generation using engineering design knowledge*, Knowledge-Based Systems 303, 112410, DOI `10.1016/j.knosys.2024.112410`.
- Ghali et al. (2025), *Enhancing knowledge retrieval with in-context learning and semantic search through generative AI*, Knowledge-Based Systems 311, 113047, DOI `10.1016/j.knosys.2025.113047`.
- Abusitta et al. (2024), *Survey on Explainable AI: Techniques, challenges and open issues*, Expert Systems with Applications 255, 124710, DOI `10.1016/j.eswa.2024.124710`.
- Luo et al. (2026), *RALLRec+: Retrieval augmented large language model recommendation with reasoning*, Expert Systems with Applications 297, 129508, DOI `10.1016/j.eswa.2025.129508`.
- Li et al. (2026), *Towards evidence-aware retrieval-augmented generation via self-corrective chain-of-thought*, Information Processing & Management 63(2), 104369, DOI `10.1016/j.ipm.2025.104369`.
- Wang & Ding (2024), *The rationality of explanation or human capacity? Understanding the impact of explainable artificial intelligence on human-AI trust and decision performance*, Information Processing & Management 61(4), 103732, DOI `10.1016/j.ipm.2024.103732`.
- *Explainable AI for enhanced decision-making* (2024), Decision Support Systems 184, 114276, DOI `10.1016/j.dss.2024.114276`.
- Fischer-Abaigar et al. (2024), *Bridging the gap: Towards an expanded toolkit for AI-driven decision-making in the public sector*, Government Information Quarterly 41(4), 101976, DOI `10.1016/j.giq.2024.101976`.
- Haesevoets et al. (2024), *How do citizens perceive the use of Artificial Intelligence in public sector decisions?*, Government Information Quarterly 41(1), 101906, DOI `10.1016/j.giq.2023.101906`.
- Mentzingen et al. (2025), *Effectiveness in retrieving legal precedents: exploring text summarization and cutting-edge language models toward a cost-efficient approach*, Artificial Intelligence and Law, DOI `10.1007/s10506-025-09440-2`.
- Italiani et al. (2025), *Enhancing legal question answering with data generation and knowledge distillation from large language models*, Artificial Intelligence and Law, DOI `10.1007/s10506-025-09463-9`.

**Limitación de acceso web:** las páginas específicas `Guide for Authors` de los journals Elsevier fueron identificadas, pero no pudieron inspeccionarse íntegramente en el acceso web actual. Se verificaron scope y políticas publisher-level, pero los límites exactos de extensión/formato deben revalidarse en la guía del target final antes de submission. No se inferieron ni inventaron límites.

```text
0D_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
PRIMARY_TARGET = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

---

## English

### A. Reconstructed state

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
TARGET_JOURNAL = PENDING_0D
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

**FILES READ:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/0B_PHASE_CLOSURE.md`; `article/reviews/0C_ENTRY_GATE.md`; `article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`; `article/reviews/0C_INTERNAL_REVIEW.md`; `article/reviews/0C_AUTHOR_APPROVAL.md`; `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`; `article/reviews/0C_PHASE_CLOSURE.md`; `article/reviews/0D_ENTRY_GATE.md`; and `SRC-03` in read-only mode at `docs/plan-maestro-temporal-2026-08-31@f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`.

**ACTIVE PHASE:** `0D — Editorial architecture and journal fit`.

**ASSIGNED BLOCK STATUS:** `READY_FOR_DRAFTING`.

**DRAFTING AUTHORIZED:** yes, exclusively for this editorial-architecture/journal-fit analytical artifact. No manuscript section is yet authorized for drafting.

**RELEVANT FROZEN DECISIONS:** historical retrieval generates and ranks candidates; normative retrieval provides post-ranking evidence without replacing or reordering the ranking; the Top-3 is fixed before generation; the local LLM explains that Top-3 and does not classify from scratch; SERIES is the analysis unit and DAM is the grouping unit where dependence exists; configurability is not empirical generalization; auditability/traceability are not legal correctness; the frozen provisional 0C contribution is Alternative B, architectural-methodological.

**RELEVANT AUTHORIZED CLAIMS:** C01–C07, C15, C17, C19, and C21–C25 within their documented boundaries. C14 remains conditional and may only be used with the HE4 limitations.

**RELEVANT PROHIBITED OR PENDING CLAIMS:** C09, C12, C13, C16, and C18 remain prohibited; C20 remains `REVIEW_REQUIRED`; C10/C11 remain `PROHIBITED` in the editorial Claim–Evidence Matrix although `SRC-03` now records EXP-11B as closed/approved/integrated. This lag is not reconciled by inference, and H150/H200 are not used as article claims.

**EXTERNAL SOURCES VERIFIED:** web research was performed on `2026-09-15` exclusively for journal fit and current editorial requirements, using primary/official Elsevier/ScienceDirect and Springer Nature sources plus recent articles published in the screened journals. This research is not used to reopen Phase 0B or alter novelty/gap findings.

**BLOCKERS OR CONTRADICTIONS:** there is no blocker to defining article architecture or assessing journal fit. Two downstream editorial dependencies remain: (1) `C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE`; (2) Group 3 has not started, so RQ4 and final inferential closure of HE2/HE5 remain conditional. Journal-specific Elsevier `Guide for Authors` pages were identified, but current web access did not allow reliable inspection of all exact word/page limits; these must therefore be revalidated before eventual submission rather than inferred.

**Experimental snapshot consumed:**

```text
SRC-03 branch = docs/plan-maestro-temporal-2026-08-31
SRC-03 HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
SRC-03 blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
GROUP3 = NEXT / NOT_STARTED
```

The frozen 0C positioning is preserved unchanged:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

This complete contract is the provisional differentiating object. It does not prove novelty by itself and does not authorize claims that its individual components are new.

Results already available for later drafting, within their boundaries, are the v0.2 benchmark and DAM-disjoint split; H100 historical candidate-retrieval metrics; flat/hierarchical normative BM25 as documentary-evidence retrieval; historical–normative integration with `3168/3168` identifiable NANDINA-8 evidence slots, complete traceability, and rank preservation `1.0`; bounded HE4 explanation/auditability evidence; the method-dependent 0B-05C corrective sensitivity; and reproducibility/provenance closure with nonblocking limitations rather than perfect reproducibility.

Results/decisions that cannot yet be treated as final article evidence include the direction of H150/H200 until C10/C11 are reconciled; final inferential HE2/HE5 decisions; final RQ4 closure before Group 3; and any EXP-12 diversity effect, which was not estimable under the frozen design.

---

### B. Candidate IMRaD architecture

The proposed architecture makes the frozen functional contract the methodological spine of the paper, keeps Methods/Results/Discussion strictly separate, and allows drafting to begin with evidence already governed by frozen artifacts.

| section | subsection | scientific purpose | evidence/claims consumed | draftability | pending dependency | editorial risk |
|---|---|---|---|---|---|---|
| 1. Introduction | 1.1 Problem and pilot scope | Bound NANDINA recommendation as offline documentary decision support, not legally binding classification | 0A-01; prohibited C18; Chapter 87 scope | `DEFER_TO_LATE_STAGE` | stable architecture and partial Results | MEDIUM: legal/institutional overstatement |
| 1. Introduction | 1.2 Prior-work limitation and positioning | Present narrow functional separation without turning bounded absence into universal absence | frozen 0B; F1–F5; frozen 0C | `DEFER_TO_LATE_STAGE` | drafted Related Work | HIGH: novelty/absence overclaiming |
| 1. Introduction | 1.3 Provisional contribution and RQs | State B and RQ1–RQ4 with conditions | frozen 0C | `DEFER_TO_LATE_STAGE` | RQ4 remains conditional on Group 3 | MEDIUM |
| 2. Related Work | 2.1 HS classification and candidate retrieval | Distinguish direct classification, retrieval, and Top-k | 0B-01/02/03 | `DRAFTABLE_NOW` | none | LOW |
| 2. Related Work | 2.2 RAG, agents, and regulatory reasoning | Compare decision-coupled regulatory systems against the pilot contract | 0B-03A/B; 0B-04B | `DRAFTABLE_NOW` | none | MEDIUM |
| 2. Related Work | 2.3 Explainability, source support, and auditability | Preserve falsified broad F5 and contextualize auditability | 0B-02/03/05A/06; N01 | `DRAFTABLE_NOW` | none | HIGH |
| 2. Related Work | 2.4 Validity, provenance, and reproducibility | Ground group dependence, provenance, and inferential boundaries | 0B-04A/05A/05B/05C | `DRAFTABLE_NOW` | none | LOW |
| 2. Related Work | 2.5 Positioning synthesis | Show the complete evaluated contract as comparison object, not automatic novelty | frozen 0C | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | final novelty undeclared | MEDIUM |
| 3. Methods | 3.1 Study design, scope, and units | Describe offline pilot, Chapter 87, SERIES/DAM, and nonbinding status | 0A-01/02; C06/C07/C18 | `DRAFTABLE_NOW` | none | LOW |
| 3. Methods | 3.2 Data, corpora, versioning, and curation | Establish benchmark identity, hashes, historical/normative corpora, and provenance | 0A-02; Group 2; C17 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | retain unrecoverable limitations | MEDIUM |
| 3. Methods | 3.3 v0.2 split and dependence controls | Describe DAM-disjoint splitting and separate near-duplicate risk | C06/C07/C19; 0A-02 | `DRAFTABLE_NOW` | Group 3 only for later inference | LOW |
| 3. Methods | 3.4 Historical retrieval and fixed Top-k/Top-3 | Define primary candidate generation/ranking | C01; D-004/D-005 | `DRAFTABLE_NOW` | none | LOW |
| 3. Methods | 3.5 Post-ranking normative retrieval | Define documentary retrieval that cannot rerank | C02; EV-03/04 | `DRAFTABLE_NOW` | none | LOW |
| 3. Methods | 3.6 Candidate–evidence integration and invariance | Specify rank-preservation and traceability contract | EV-06; B | `DRAFTABLE_NOW` | none | LOW |
| 3. Methods | 3.7 Local LLM and controlled explanation | Document immutable Top-3, context, and no-modification rules | C03; OE4/HE4 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | HE4 limitations | MEDIUM |
| 3. Methods | 3.8 Function-specific evaluation design | Separate candidate retrieval, evidence retrieval, invariance, and HE4 | C04/C05/C14; 0A-02 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | Group 3 for final inference | MEDIUM |
| 3. Methods | 3.9 Validity, drift, and reproducibility | Explain near duplicates, concentration, 0B-05C drift, and provenance | C21–C25; Group 2 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | final RQ4 inference requires Group 3 | MEDIUM |
| 4. Results | 4.1 Benchmark and split controls | Report composition and zero inter-partition DAM overlap | C06/C07 | `DRAFTABLE_NOW` | none | LOW |
| 4. Results | 4.2 Historical candidate retrieval — RQ1 | Report H100 Top-k/MRR as candidate retrieval | C04/C05 | `DRAFTABLE_NOW` | none | LOW if not called system accuracy |
| 4. Results | 4.3 Normative retrieval and integration — RQ2 | Report normative BM25, evidence coverage, traceability, and invariance | EV-03/04/06; C02 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | none | MEDIUM |
| 4. Results | 4.4 Controlled explanation — RQ3 | Report HE4 structure/traceability with explicit limits | C14; EV-08 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | none | HIGH |
| 4. Results | 4.5 Sensitivity and documentary validity | Report bounded 0B-05C and other frozen sensitivity evidence | C21–C25; descriptive EXP-11A only | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | EXP-11B excluded until C10/C11 | MEDIUM |
| 4. Results | 4.6 Inferential validity closure — RQ4 | Resolve dependence/validity and HE2/HE5 under inferential gate | Group 3 | `BLOCKED_BY_GROUP3` | Group 3 | HIGH |
| 4. Results | 4.7 EXP-11B, if later included | Use H150/H200 only after claim-level editorial authorization | SRC-03 + future reconciliation | `BLOCKED_BY_C10_C11_RECONCILIATION` | C10/C11 | HIGH |
| 5. Discussion | 5.1 Meaning of functional separation | Interpret ranking/evidence/explanation separation without component novelty claims | final Results + 0C | `BLOCKED_BY_FINAL_RESULTS` | Group 3 and final claims | MEDIUM |
| 5. Discussion | 5.2 Comparison with closest prior art | Contrast candidate prediction, RAG/agents, source-support prior art | 0B + N01 | `BLOCKED_BY_FINAL_RESULTS` | final Results | HIGH |
| 5. Discussion | 5.3 Decision-support implications | Discuss documentary auditability as support, not legal correctness | prohibited C12/C13/C18; conditional C14 | `BLOCKED_BY_FINAL_RESULTS` | final Results | HIGH |
| 5. Discussion | 5.4 Validity and transferability | Distinguish internal validity, reproducibility, configurability, and generalization | C15–C17; RQ4 | `BLOCKED_BY_GROUP3` | Group 3 | HIGH |
| 6. Limitations | 6.1 Benchmark/data limits | Chapter 87, DAM, near duplicates, concentration | 0A-02 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | final consolidation after Group 3 | MEDIUM |
| 6. Limitations | 6.2 HE4/auditability | N=50, AI evaluator, prompt–schema mismatch | EV-08/C14 | `DRAFTABLE_NOW` | none | LOW if preserved exactly |
| 6. Limitations | 6.3 Normative drift | Snapshot versus current normative state; method-dependent sensitivity | C21–C25 | `DRAFTABLE_NOW` | none | MEDIUM |
| 6. Limitations | 6.4 Reproducibility/external validity | Nonblocking reproducibility limitations; no Chapter-87 extrapolation | Group 2; prohibited C16 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | final Results | MEDIUM |
| 7. Conclusions | — | Answer RQs within scope | final Results/Discussion | `DEFER_TO_LATE_STAGE` | Group 3 + final Results/Discussion | HIGH |
| Data/Code Availability | — | Declare repositories, reproducible artifacts, and restrictions | D-006; C17; Group 2 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | verify final snapshot | LOW |
| Declarations | AI use, funding, competing interests, author contributions | Satisfy target-journal requirements | current publisher policies | `DEFER_TO_LATE_STAGE` | final target | LOW |

**Non-duplication principle:** Methods define the contract and measurements; Results report observations only; Discussion interprets implications and prior-art relationships. Detailed validity threats are centralized in Limitations, while Methods records only controls needed to reproduce the design.

---

### C. Essential table/figure map

| ID | type | content | section | scientific function | data source | status | dependency |
|---|---|---|---|---|---|---|---|
| Fig. 1 | architecture figure | Complete contract: historical ranking → non-reranking normative evidence → immutable-Top-3 explanation, with no feedback | Methods | Make architectural/functional separation visible | 0A-01; D-005; frozen 0C | `ESSENTIAL_NOW` | none |
| Table 1 | benchmark table | H100/DEV/EVAL series, DAMs, codes, hashes, zero DAM overlap | Methods/Results 4.1 | Bound units and partition controls | EV-01/0A-02 | `ESSENTIAL_NOW` | none |
| Table 2 | methodological table | Component → task → output → metric → permitted/prohibited interpretation | Methods | Prevent metric/function conflation | 0A-02; C01–C14 | `ESSENTIAL_NOW` | none |
| Table 3 | results | H100 Top-1/3/5/10/50 and MRR | Results 4.2 | Answer RQ1 as candidate retrieval | EV-02; C04/C05 | `ESSENTIAL_NOW` | none |
| Table 4 | integrated results | Flat/hierarchical normative BM25 + `3168/3168` evidence + traceability + rank preservation | Results 4.3 | Answer RQ2 while separating evidence retrieval and invariance | EV-03/04/06 | `ESSENTIAL_NOW` | explicit correctness boundaries |
| Table 5 | results/limitations | HE4 N=50, 28/50 auditable, mean/median, protocol limitations | Results 4.4 | Answer RQ3 without hiding limitations | EV-08; C14 | `ESSENTIAL_NOW` | bounded interpretation |
| Table 6 | sensitivity | 0B-05C drift/overlap and EV03/EV04/D1a effects by method | Results 4.5 / Limitations | Separate documentary drift from metric impact | C21–C25 | `ESSENTIAL_NOW` | none |
| Table 7 | literature comparison | Closest prior art vs B-contract properties without novelty wording | Related Work 2.5 | Condense positioning traceably | frozen 0B + N01 | `OPTIONAL` | determinant precedents only |
| Fig. 2 | validity map | DAM split, near duplicates, concentration, drift, reproducibility | Methods/Limitations | Integrate validity threats/controls | 0A-02; Group 2; 0B-05C | `OPTIONAL` | omit if redundant |
| Table 8 | inferential results | Group-3 closure and final RQ4/HE2/HE5 response | Results 4.6 | Add final inference | Group 3 | `ESSENTIAL_AFTER_PENDING_EXPERIMENT` | Group 3 |
| Table 9 | EXP-11B | H150/H200 if editorially admitted | Results 4.7 | Use only after claim reconciliation | SRC-03 + future Claim Matrix | `ESSENTIAL_AFTER_PENDING_EXPERIMENT` if included | C10/C11 reconciliation |
| Fig. 3 | size/composition sensitivity curve | EXP-11A/11B | Results/Discussion | Descriptive sensitivity | EXP-11A/11B | `NOT_RECOMMENDED` for now | causal-interpretation risk and C10/C11 lag |

The visual plan is intentionally compact: one primary architecture figure, five to six essential evidence tables, and later one Group-3 inferential table. Repeated pipeline diagrams are not recommended.

---

### D. Immediate draftability matrix

| block | status | rationale |
|---|---|---|
| Methods 3.1, 3.3–3.6 | `DRAFTABLE_NOW` | architecture, units, split, and functional contract are frozen and Group-3 independent |
| Methods 3.2, 3.7–3.9 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | draftable while preserving provenance, HE4, and drift limitations |
| Related Work 2.1–2.4 | `DRAFTABLE_NOW` | Phase 0B is closed/frozen and no new gap search is required |
| Related Work 2.5 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | B is provisional positioning; final gap/novelty remain undeclared |
| Results 4.1–4.2 | `DRAFTABLE_NOW` | benchmark/split and H100 are frozen |
| Results 4.3–4.5 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | evidence is available but coverage/auditability/drift require strict boundaries |
| Results 4.6 | `BLOCKED_BY_GROUP3` | RQ4 and HE2/HE5 cannot be anticipated |
| Results 4.7 | `BLOCKED_BY_C10_C11_RECONCILIATION` | EXP-11B is live experimentally but not editorially authorized as a claim |
| Introduction | `DEFER_TO_LATE_STAGE` | D-003 places it after Methods, Related Work, and initial frozen Results |
| Discussion 5.1–5.3 | `BLOCKED_BY_FINAL_RESULTS` | valid interpretation requires the final result set |
| Discussion 5.4 | `BLOCKED_BY_GROUP3` | final validity/transferability depends on RQ4 |
| Limitations 6.1–6.4 | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | technical draft is possible, final form after Group 3 |
| Conclusions | `DEFER_TO_LATE_STAGE` | depends on final RQ answers and Discussion |
| Abstract/final Title | `DEFER_TO_LATE_STAGE` | explicitly late-stage |
| Data/Code Availability | `DRAFTABLE_WITH_FROZEN_LIMITATIONS` | provenance exists; final snapshot/assets must be checked |
| Editorial declarations | `DEFER_TO_LATE_STAGE` | depend on final journal and actual AI use |

If Phase 0 is later approved, the D-003/ARTICLE_WRITING_PLAN order remains: **Methods → Related Work → available frozen Results → preliminary figures/tables → provisional Introduction**, while unreconciled EXP-11B, Group-3/RQ4, final Results, final Discussion, Conclusions, Abstract, and final Title remain blocked.

---

### E. Journal-fit screening

#### E.1 Evaluation rule

`HIGH/MEDIUM/LOW` expresses scientific fit, or risk magnitude in the risk column. Impact factor, CiteScore, and quartile are not substitutes for scientific fit. Web verification dated `2026-09-15` was limited to official/primary publisher sources and articles published in the screened journals.

For the five Elsevier journals, the current publisher AI policy was verified: generative-AI use in manuscript preparation requires human oversight and, where applicable, a separate disclosure statement; AI use as part of research methods should be reproducibly described in Methods. Elsevier’s research-data/data-statement policy was also verified, while exact journal-level requirements depend on the specific Guide for Authors. Several exact ScienceDirect Guide-for-Authors pages were not fully accessible in the current web environment; no word/page limits are therefore inferred.

| journal | scope fit | contribution fit | methods/results fit | novelty expectation risk | empirical-scope fit | explainability/auditability fit | reproducibility/open-science fit | recent related articles | structural/length constraints | operational notes | overall fit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Knowledge-Based Systems (KBS)** | HIGH — AI, knowledge-based systems, knowledge engineering, intelligent decision support | HIGH — B can be framed as an evaluated knowledge-system contract with differentiated roles | HIGH | MEDIUM — original/innovative research expected; known-technique assembly is insufficient | HIGH — Chapter 87 can serve as an applied case if methodological lessons are bounded | HIGH | HIGH | KBS 295 (2024) 111761, `10.1016/j.knosys.2024.111761`; KBS 303 (2024) 112410, `10.1016/j.knosys.2024.112410`; KBS 311 (2025) 113047, `10.1016/j.knosys.2025.113047` | exact limit not reliably verifiable in current access | Elsevier AI declaration and research-data policy apply subject to guide | **HIGH** |
| **Expert Systems with Applications (ESWA)** | HIGH — intelligent systems in government/law/auditing/IR/KM | HIGH | HIGH | HIGH — scope explicitly emphasizes genuine innovation over repackaging | HIGH if the contribution extends beyond a local application narrative | HIGH | HIGH | ESWA 255 (2024) 124710, `10.1016/j.eswa.2024.124710`; ESWA 297 (2026) 129508, `10.1016/j.eswa.2025.129508` | exact limit not reliably verifiable in current access | strong fit if functional-contract contribution is made explicit | **HIGH** |
| **Information Processing & Management (IPM)** | HIGH — computing × information science, methods, critical applications, system design | HIGH | HIGH | MEDIUM | HIGH as a critical information-retrieval/evidence application | HIGH | HIGH | IPM 63(2) (2026) 104369, `10.1016/j.ipm.2025.104369`; IPM 61(4) (2024) 103732, `10.1016/j.ipm.2024.103732` | exact limit not reliably verifiable in current access | framing should foreground IR/evidence/provenance | **HIGH** |
| **Decision Support Systems (DSS)** | MEDIUM — decision-support theory/technology | MEDIUM | MEDIUM | HIGH — expects implications for enhanced decision making | MEDIUM because no human-decision outcome is measured | HIGH | HIGH | DSS 184 (2024) 114276, `10.1016/j.dss.2024.114276` | exact limit not reliably verifiable in current access | desk-rejection risk if seen as retrieval/NLP rather than DSS contribution | **MEDIUM** |
| **Government Information Quarterly (GIQ)** | MEDIUM — government, IT, accountability, decision tools | LOW | MEDIUM | HIGH | MEDIUM — customs is governmental but organizational/public effects are not evaluated | HIGH conceptually | MEDIUM-HIGH | GIQ 41(4) (2024) 101976, `10.1016/j.giq.2024.101976`; GIQ 41(1) (2024) 101906, `10.1016/j.giq.2023.101906`; GIQ 41(1) (2024) 101914 | exact limit not reliably verifiable in current access | current study lacks policy/adoption/citizen/public-value empirical dimension | **LOW** |
| **Artificial Intelligence and Law** | MEDIUM — computational law/legal reasoning and AI in legal domain | LOW-MEDIUM — normative evidence is used, but legal reasoning/correctness is not claimed | MEDIUM | HIGH | MEDIUM — customs is regulatory but no independently adjudicated legal correctness | HIGH for traceability, not legal validity | HIGH | Mentzingen et al. (2025), `10.1007/s10506-025-09440-2`; Italiani et al. (2025), `10.1007/s10506-025-09463-9` | double blind; 150–250-word abstract; 4–6 keywords; max three heading levels; Word/LaTeX; data availability/SI rules verified | LLMs are not authors; substantive LLM use should be documented; AI copy editing need not be declared under current guide | **LOW** |

#### E.2 Primary fit evidence

**Knowledge-Based Systems.** Elsevier describes KBS as an international/interdisciplinary AI journal focused on knowledge-based and other AI-technique systems, supporting human prediction/decision making and balancing theory with practical study. Recent KBS papers cover explainable decision support, RAG with explicit engineering knowledge, and LLM-based knowledge retrieval. This directly accommodates B if the contribution is framed as an evaluated functional contract rather than novelty of individual components.

**Expert Systems with Applications.** Its official scope includes intelligent systems in government, law, auditing, information retrieval, information management, and knowledge management. The same scope explicitly stresses genuine innovation and discourages superficial repackaging, raising the novelty bar for an architecture assembled from established components.

**Information Processing & Management.** Its official scope welcomes research, methods, reviews, and critical-application manuscripts at the computing–information-science intersection. Recent evidence-aware RAG and XAI/decision-performance work supports topical fit around retrieval, evidence, and explanation. Fit is strongest under an IR/evidence/provenance framing.

**Decision Support Systems.** The journal requires relevance to theoretical/technical support for enhanced decision making, including functionality, implementation, evaluation, and impacts. This project is potentially decision-support oriented, but does not measure downstream human decision performance, making fit weaker than the top three.

**Government Information Quarterly.** GIQ explicitly covers government, IT, transparent/accountable government, and technology for decision/policy making, but recent papers emphasize adoption, governance, public values, perceptions, and organizational/public-sector effects. Those dimensions are not empirically evaluated here.

**Artificial Intelligence and Law.** AI & Law focuses on computational models of law/legal reasoning and AI in the legal domain. Recent work on legal precedent retrieval and legal QA is relevant, but this project explicitly separates documentary evidence retrieval from legal correctness and does not evaluate adjudicated legal reasoning.

---

### F. Top-3 journal deep dive

#### F.1 Knowledge-Based Systems — candidate 1

1. **Scientific fit.** KBS simultaneously fits knowledge-based systems, knowledge engineering, intelligent decision support, and practical AI systems. B can be stated as a knowledge architecture with restricted responsibilities across historical, normative, and generative components.
2. **Desk-rejection risks.** Perceived assembly of BM25 + normative sources + LLM; overly local NANDINA/Chapter-87 application; insufficient differentiation from RAG/agentic prior art; limited external validation; bounded HE4.
3. **Required editorial emphasis.** Center the **evaluated functional contract**, verifiable invariants, and function-specific metrics. Treat customs as a demanding regulated case study, not as a substitute for methodological contribution.
4. **Strengthen/attenuate.** Strengthen formal interfaces, module prohibitions, traceability, grouped splitting, invariance, and function-specific evaluation. Attenuate “first”, broad superiority, legal correctness, and generalization claims.
5. **Compatibility with B:** `HIGH`.
6. **Compatibility with Chapter 87:** `HIGH` if clearly bounded.
7. **Compatibility with RQ1–RQ4:** RQ1/RQ2 direct; RQ3 complementary; RQ4 conditional on Group 3.
8. **Pending-results compatibility.** Methods/Related Work and partial Results can be built before Group 3; final version must wait for the applicable inferential gate and any EXP-11B reconciliation if used.
9. **Recent relevant articles.** KBS 295 (2024) 111761; KBS 303 (2024) 112410; KBS 311 (2025) 113047.
10. **Architecture-conditioning requirements.** Current Elsevier AI disclosure and research-data requirements apply; exact KBS length limits should be rechecked before submission. The candidate architecture already reserves Data/Code Availability and Declarations.

**0D verdict:** strongest balance among B, knowledge retrieval, evidence support, and controlled explanation.

#### F.2 Expert Systems with Applications — candidate 2

1. **Scientific fit.** ESWA covers design/development/testing/implementation of intelligent systems in domains including government, law, auditing, and information retrieval.
2. **Desk-rejection risks.** Its explicit genuine-innovation expectation makes an established-component pipeline vulnerable to being judged incremental. Chapter-87 scope and HE4 limitations amplify this risk if the contract is not formalized.
3. **Required editorial emphasis.** Present the paper as **verifiable architectural restriction + evaluation protocol**, not “RAG applied to customs”.
4. **Strengthen/attenuate.** Strengthen comparison to systems where regulations/LLMs alter decisions and foreground rank-preservation tests; attenuate auditability-as-novelty because broad F5 is falsified.
5. **Compatibility with B:** `HIGH`.
6. **Compatibility with Chapter 87:** `HIGH` for an expert-system application under explicit scope.
7. **Compatibility with RQ1–RQ4:** `HIGH`, with RQ4 pending Group 3.
8. **Pending-results compatibility.** Same as KBS; final paper requires sufficiently closed results.
9. **Recent relevant articles.** ESWA 255 (2024) 124710; ESWA 297 (2026) 129508.
10. **Architecture-conditioning requirements.** Elsevier AI disclosure/data policy; exact guide-specific length/format must be revalidated.

**0D verdict:** strong alternative, but novelty-risk is higher than KBS because the scope expressly rejects superficial repackaging.

#### F.3 Information Processing & Management — candidate 3

1. **Scientific fit.** IPM directly covers methods and critical applications in computing/information science; this project can be framed as information retrieval/evidence/provenance architecture with controlled downstream generation.
2. **Desk-rejection risks.** The article could be judged primarily an expert-system/domain application rather than an information-processing contribution; customs/LLM content could dominate the retrieval contribution.
3. **Required editorial emphasis.** Foreground retrieval architecture, evidence provenance, traceability, metric semantics, and dependence control; keep the LLM as a constrained downstream consumer rather than a novelty core.
4. **Strengthen/attenuate.** Strengthen RQ1/RQ2 and invariance/provenance; attenuate legal and human-decision-support claims.
5. **Compatibility with B:** `HIGH`, especially the separation `candidate retrieval ≠ evidence retrieval ≠ explanation`.
6. **Compatibility with Chapter 87:** `HIGH` as critical application if methodological lessons are explicitly bounded.
7. **Compatibility with RQ1–RQ4:** RQ1/RQ2 strongest; RQ3 supportive; RQ4 adds validity.
8. **Pending-results compatibility.** Frozen Results support initial construction, but final Discussion requires Group 3.
9. **Recent relevant articles.** IPM 63(2) (2026) 104369; IPM 61(4) (2024) 103732.
10. **Architecture-conditioning requirements.** Elsevier AI disclosure/data policy; journal-specific length constraints require pre-submission revalidation.

**0D verdict:** excellent alternative if the manuscript foregrounds IR/evidence architecture rather than expert-system application.

---

### G. Primary target and alternatives

```text
PRIMARY_TARGET = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
```

#### PRIMARY_TARGET — Knowledge-Based Systems

**Scientific justification.** KBS best matches the 0C-frozen object: an evaluated architectural-methodological contract in which distinct knowledge sources have non-interchangeable roles and a downstream generator is restricted by design. KBS explicitly combines knowledge-based systems, knowledge engineering, intelligent decision support, and practical applications, and recent publications cover retrieval, RAG, explicit knowledge, and explainable decision support.

**Risks.** The contribution may be perceived as incremental integration of known components. Chapter-87 scope and HE4 limitations constrain empirical breadth. Final gap and novelty remain undefined.

**Required framing adjustments.** If later authorized, novelty should only be discussed at the level of the **complete functional contract and its evaluation**, never BM25, Top-k, RAG, normative evidence, LLM, or auditability separately. Interfaces, invariants, and function-specific metrics should be explicit. Customs should be framed as a demanding documentary/regulatory case, not evidence of legal correctness.

**Recommended structure.** The Section-B IMRaD architecture: function-organized Related Work; Methods centered on contract/data/partition/evaluation; Results separated by RQ1–RQ3 and later RQ4; Discussion on functional separation and bounded prior-art comparison; explicit technical Limitations.

**Why it outranks alternatives.** Compared with ESWA, KBS accommodates a knowledge-architecture contribution without relying as heavily on an “expert application” novelty argument. Compared with IPM, KBS better accommodates the full system including controlled explanation and decision-support framing rather than requiring retrieval to dominate the contribution.

#### ALTERNATIVE_TARGET_1 — Expert Systems with Applications

Recommended because of direct fit with expert/intelligent systems, information retrieval, government/law/auditing, and applied evaluation. It ranks below KBS because its explicit genuine-innovation expectation raises desk-rejection risk if B is not sufficiently formalized against prior art.

#### ALTERNATIVE_TARGET_2 — Information Processing & Management

Recommended because of strong fit with retrieval, evidence, provenance, and information-processing architecture. It ranks below KBS because it would require shifting the narrative center toward IR/information science, potentially underrepresenting the constrained-explanation contract.

**Not selected:** DSS remains a medium fit because downstream human decision impact is not evaluated; GIQ would require government/public-administration dimensions not studied; AI & Law would require stronger legal-reasoning/legal-correctness emphasis than the design permits.

This is a 0D recommendation for editorial audit and author approval, not an irrevocable journal choice.

---

### H. Risks and mitigations

| risk | level | basis | mandatory mitigation |
|---|---|---|---|
| Novelty risk | HIGH | F1/F3 are bounded negatives; F2 has partial prior art; broad F5 is falsified | Keep `FINAL_GAP = NOT_DEFINED`, `NOVELTY = NOT_DECLARED`; differentiate only the complete contract; no “first/no prior work” |
| Overclaiming | HIGH | Top-3 can be miscalled system accuracy; 3168/3168 can be miscalled correctness; HE4 can be miscalled legal validation | Add interpretation-boundary table; claim-by-claim review |
| Internal validity | MEDIUM | DAM-disjoint split is strong, but intra-DAM dependence and concentration remain | Retain DAM grouping and wait for Group-3 inference |
| Grouped dependence | MEDIUM | 1,056 series belong to 67 DAMs | Use DAM-compatible inference where required; do not anticipate Group 3 |
| Leakage/near duplicates | MEDIUM | Zero DAM overlap does not eliminate cross-DAM exact/near duplicates | Report as distinct validity threat; explicit sensitivity/limitation |
| External validity/generalization | HIGH | Empirical evaluation is Chapter-87 bounded | Configurability only as design property; prohibit empirical extrapolation |
| HE4 limitations | HIGH | N=50, AI evaluator, prompt–schema mismatch, modality deviation | Treat as limited structure/traceability evidence; no correctness/legal validation |
| Normative-source drift | MEDIUM | Decision-885 snapshot vs Decision-906 current state produced drift and method-dependent sensitivity | Preserve C21–C25; separate snapshot, overlap, and metric impact |
| Reproducibility limitations | MEDIUM | Group-2 closure has nonblocking unrecoverable/local-only assets | Transparent Data/Code Availability; provenance ≠ perfect reproducibility |
| Group-3 dependency | HIGH | RQ4 and HE2/HE5 remain open | Block final RQ4 Results, final Discussion, and Conclusions |
| C10/C11 governance lag | HIGH | EXP-11B is experimentally closed but editorially prohibited | No H150/H200 use until explicit reconciliation |
| B vs KBS expectations | MEDIUM | KBS expects original/innovative research | Formalize interfaces/invariants; make the architectural/functional separation and the differentiated role of each evaluation explicit; avoid component-level novelty claims |
| B vs ESWA expectations | HIGH | ESWA explicitly rejects superficial repackaging | Use only with strong formal architectural differentiation |
| B vs IPM expectations | MEDIUM | IPM may require clearer information-science/IR contribution | Foreground retrieval/evidence/provenance for this target |
| Journal-specific guide access | LOW | Exact Elsevier author-guide limits were not fully accessible in current web environment | Recheck length/format/data policy immediately before submission |
| AI-use disclosure | LOW | Elsevier/Springer now have explicit AI rules | Keep AI-use records; include target-compliant declaration; retain full human verification/accountability |

No identified risk invalidates B by itself. The main HIGH risks are novelty/overclaiming, HE4, external validity, and still-open dependencies; all require explicit gating and bounded claims.

---

### I. Phase-0 gate

```text
PHASE_0_GATE = PASS_WITH_CORRECTIONS
```

**Rationale.** Editorial architecture can now be coherently fixed; Phases 0A/0B/0C are closed; a defensible primary target exists; Methods, Related Work, and several frozen Results can be drafted without new experimental interpretation. A clean `PASS` is not recommended because explicit downstream conditions remain:

1. C10/C11 must be reconciled before any EXP-11B article use.
2. Group 3 must close before RQ4, HE2/HE5, final Results, final Discussion, and Conclusions are completed.
3. Final gap and novelty remain `NOT_DEFINED / NOT_DECLARED`; journal fit cannot establish either.
4. Exact target-journal Guide-for-Authors requirements must be revalidated before submission because current access did not support complete verification of every Elsevier journal-specific limit.

**What could be authorized if the Managing AI and author later approve this gate:** opening the D-003/ARTICLE_WRITING_PLAN drafting sequence — Methods, Related Work, available frozen Results, then preliminary figures/tables and provisional Introduction — while keeping unreconciled EXP-11B, Group-3/RQ4, final Results, final Discussion, Conclusions, Abstract, and final Title blocked.

This artifact does not itself grant that authorization.

```text
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

No new experimental interpretation is introduced. The artifact only organizes governed evidence and uses web research for journal fit/current editorial requirements; experimental dependencies are preserved as blockers rather than resolved.

---

### J. Traceability

**Repository and editorial cutoff consumed**

- repository: `elVladdi/gci-nandina-rag`;
- branch: `article/main-manuscript`;
- 0D opening commit/HEAD: `113500a0745cb10a8e29761c67879fa3d19aa3ad`;
- message: `article: activate 0D editorial architecture and journal fit`.

**Read-only SRC-03**

- branch: `docs/plan-maestro-temporal-2026-08-31`;
- HEAD: `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`;
- recorded blob: `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`.

**Journal-fit web-search date:** `2026-09-15`.

**Official scope/policy sources**

- Knowledge-Based Systems — Elsevier: `https://shop.elsevier.com/journals/knowledge-based-systems/0950-7051`
- Expert Systems with Applications — Elsevier: `https://shop.elsevier.com/journals/expert-systems-with-applications/0957-4174`
- Information Processing & Management — Elsevier: `https://shop.elsevier.com/journals/information-processing-and-management/0306-4573`
- Decision Support Systems — Elsevier: `https://shop.elsevier.com/journals/decision-support-systems/0167-9236`
- Government Information Quarterly — Elsevier: `https://shop.elsevier.com/journals/government-information-quarterly/0740-624X`
- Artificial Intelligence and Law — Springer Nature: `https://link.springer.com/journal/10506`
- AI & Law submission guidelines: `https://link.springer.com/journal/10506/submission-guidelines`
- Elsevier generative-AI policy: `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals`
- Elsevier research-data statement: `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement`
- Elsevier research-data guidelines: `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines`

**Recent articles used only for topical-fit evidence, not novelty**

- Abbaspour Onari et al. (2024), Knowledge-Based Systems 295, 111761, DOI `10.1016/j.knosys.2024.111761`.
- Siddharth & Luo (2024), Knowledge-Based Systems 303, 112410, DOI `10.1016/j.knosys.2024.112410`.
- Ghali et al. (2025), Knowledge-Based Systems 311, 113047, DOI `10.1016/j.knosys.2025.113047`.
- Abusitta et al. (2024), Expert Systems with Applications 255, 124710, DOI `10.1016/j.eswa.2024.124710`.
- Luo et al. (2026), Expert Systems with Applications 297, 129508, DOI `10.1016/j.eswa.2025.129508`.
- Li et al. (2026), Information Processing & Management 63(2), 104369, DOI `10.1016/j.ipm.2025.104369`.
- Wang & Ding (2024), Information Processing & Management 61(4), 103732, DOI `10.1016/j.ipm.2024.103732`.
- *Explainable AI for enhanced decision-making* (2024), Decision Support Systems 184, 114276, DOI `10.1016/j.dss.2024.114276`.
- Fischer-Abaigar et al. (2024), Government Information Quarterly 41(4), 101976, DOI `10.1016/j.giq.2024.101976`.
- Haesevoets et al. (2024), Government Information Quarterly 41(1), 101906, DOI `10.1016/j.giq.2023.101906`.
- Mentzingen et al. (2025), Artificial Intelligence and Law, DOI `10.1007/s10506-025-09440-2`.
- Italiani et al. (2025), Artificial Intelligence and Law, DOI `10.1007/s10506-025-09463-9`.

**Web-access limitation:** exact journal-specific Elsevier `Guide for Authors` pages were identified but could not be fully inspected in the current web environment. Scope and publisher-level policies were verified; exact length/format limits must be revalidated for the final target before submission. No limits were inferred or invented.

```text
0D_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
PRIMARY_TARGET = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```
