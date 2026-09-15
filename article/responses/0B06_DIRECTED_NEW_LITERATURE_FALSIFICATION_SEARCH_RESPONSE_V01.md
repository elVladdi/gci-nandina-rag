# 0B-06 — Búsqueda dirigida de literatura nueva para falsación de candidatos / Directed new-literature search to falsify candidates

## Español

### Estado de entrada reconstruido

```text
FASE_ACTIVA = 0B
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
0C = BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

La búsqueda se ejecutó como pressure test falsacionista y acotado sobre F1, F2, F5 y, secundariamente, F3. No se trató como expansión abierta del corpus ni como búsqueda confirmatoria de novelty.

### A. Control de búsqueda

| search_family | queries_used | sources/databases_consulted | date_searched | hits_screened | full_texts_read | notes |
|---|---|---|---|---|---:|---|
| S1 / F1 | `"HS code" historical precedents retrieval normative evidence explanation journal`; `"customs tariff classification" RAG legal evidence explanation journal`; `"harmonized system" retrieval legal evidence LLM classification journal`; `"HTS code" rulings machine learning classification retrieval`; `customs classification historical cases retrieval explanation` | búsqueda web; páginas de editoriales/revistas; Springer Nature; Wiley; MDPI; Elsevier/ScienceDirect; DOI landing pages; referencias de candidatos cercanos | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 1 | No se localizó un artículo de revista admisible 2022–2026 que cumpliera conjuntamente ranking histórico fijado, evidencia normativa estrictamente posterior y prohibición de reordenar/sustituir/introducir códigos. Se registraron antecedentes parciales y leads no admisibles. |
| S2 / F2 | `"HS code" explanation retrieval evidence customs journal`; `LLM explanation fixed ranking Top-k customs`; `regulatory classification downstream explanation fixed decision LLM`; `customs LLM explanation immutable candidates` | búsqueda web; Frontiers; Springer Nature; Wiley; Elsevier; DOI/publisher pages; related work/references | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 2 | Se encontró prior art admisible de regulatory AI con evaluación formal de explicación, pero el generador/trace participa en la decisión; no existe aislamiento contractual de un Top-k upstream inmutable. |
| S3 / F3 | `"HS code classification" group split declaration shipment importer leakage`; `"customs commodity classification" grouped split declaration dataset`; `"trade classification" grouped cross validation declaration shipment product family HS code`; `"HS code" duplicate leakage train test declaration`; `"customs declaration" machine learning grouped split classification HS` | búsqueda web; MDPI; Springer Nature; Wiley; Nature; literatura HS reciente localizada mediante review y referencias | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 1 | No se halló antecedente directo admisible con grouped split por DAM/declaración/importer/shipment/entity o control equivalente. La ausencia se reporta solo dentro del alcance buscado y no como novelty. |
| S4 / F5 | `documentary auditability source-to-claim regulatory AI`; `legal classification auditability RAG source support`; `per-output evidence traceability legal AI evaluation`; `source support explanation trace regulatory LLM` | búsqueda web; Frontiers; Springer Nature; publisher PDFs; referencias relacionadas | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 2 | Se encontró un artículo Q1 admisible con evaluación separada de source support y trace-level diagnostics por instancia/salida, suficiente para falsar una formulación amplia de F5 en regulatory AI. |
| S5 | `HS customs historical data knowledge graph LLM explanation auditability`; `customs RAG historical classification regulatory evidence LLM`; `HS code ML KG LLM explainability auditability` | búsqueda web; Elsevier/ScienceDirect; Springer Nature; Frontiers; Wiley; referencias relacionadas | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 2 | El antecedente combinado más cercano en HS/customs localizado fue proceedings y por tanto no admisible. El antecedente admisible más fuerte combina legal-source retrieval, fold-safe examples y auditability, pero no cumple S1/F1 ni el aislamiento estricto S2/F2. |

Los conteos de hits no son reproducibles con precisión en la interfaz de búsqueda empleada y se registran como `NOT_RELIABLY_COUNTABLE`. La deduplicación se realizó por DOI/título. Los trabajos heredados de 0B-01–0B-05C no se contabilizan como referencias nuevas.

### B. Matriz de candidatos nuevos

| ID | authors | year | title | journal | DOI | indexing | quartile/source | full PDF | search family | exact task | method | dataset/context | closest relevant property | critical missing property | recommendation |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N01 | Haoyang Chen; Kumiko Tanaka-Ishii | 2026 | *Executable explanation traces for legal LLM predictions via retrieval-augmented codification* | Frontiers in Artificial Intelligence | `10.3389/frai.2026.1905145` | Scopus; Web of Science ESCI; publisher index list | Frontiers current impact page consulted 2026-09-15: JCR Q1 / CiteScore Q1 | YES — publisher OA PDF, 18 pp., read in full | S2, S4, S5 | legal text-to-label prediction with executable explanation traces | retrieval-augmented codification + iterative refinement + executable traces | five legal benchmarks: CAIL, ECHR, CAP, ILDC, JTD | explicit trace-level audit diagnostics; post-hoc source-support audit between applied predicates and retrieved legal sources, separate from label accuracy | the trace/program itself produces the label and can be revised by feedback; no independent upstream immutable Top-k and no customs/HS task | `CANDIDATE_NEW — ADMIT_RECOMMENDED` |
| N02 | Hana Demma Wube; Sintayehu Zekarias Esubalew; Kena Wendimu Gebisa; Firesew Fayiso Weldesellasie; Taye Girma Debelee | 2026 | *A review of machine learning, deep learning and large language model based harmonized system code classification techniques for import and export commodities* | Discover Computing | `10.1007/s10791-026-10428-y` | Scopus and Web of Science coverage verified through ISSN/index records; Springer Nature journal | SCImago/SJR 2025: Q2 in Library and Information Sciences, Q3 in Information Systems; used only because of very high HS specificity | YES — Springer OA PDF, 39 pp., read in full | S1–S5 as discovery/corroboration | systematic review of HS-code classification | systematic literature review | 29 selected primary studies, search window 2015–2025 | highly specific map of HS methods; explicitly distinguishes explainability concerns and notes limited auditability attention | secondary evidence; cannot independently establish absence, architecture, split details, or novelty without primary-source verification | `CANDIDATE_NEW — REVIEW` |
| N03 | Mengjie Liao; Lei Huang; Jian Zhang; Luona Song; Bo Li | 2024 | *Enhanced HS Code Classification for Import and Export Goods via Multiscale Attention and ERNIE-BiLSTM* | Applied Sciences | `10.3390/app142210267` | peer-reviewed journal; publisher/DOI metadata verified | NOT_USED_FOR_ADMISSION — rejected on functional mismatch | Publisher OA full text/PDF available; admission gate not pursued after functional rejection | S3 close negative | direct HS classification from customs goods text | ERNIE + BiLSTM + channel/spatial attention | HSD: 320,360 entries, 227 HS codes; train/validation/test ratio 0.8/0.1/0.1 | recent direct HS classifier using historical customs-clearance data | no reported grouped split by declaration/entity in the inspected experimental design; no F1/F2/F5 architecture | `REJECT` |
| N04 | Haichao Sun; Chengjie Zhou; Chao Che | 2025 | *Customs Commodity Classification Method Based on the Fusion of Text Sequence and Graph Information* | Expert Systems | `10.1111/exsy.70057` | Scopus and Science Citation Index Expanded listed by Wiley | NOT_USED_FOR_ADMISSION — rejected on functional mismatch | Publisher full text/metadata screened; no admission recommendation made | S1, S2, S5 close negative | direct customs commodity classification | FTSGI: sequence learning + key-element identification + graph learning | real customs declaration data | combines text sequence and graph structure in a customs task | graph/text model directly decides class; no historical fixed Top-k + post-ranking normative evidence; no isolated explanation-only LLM; no separate documentary-auditability evaluation identified | `REJECT` |

`N02` is a secondary review and is not used as independent proof that an architecture/evaluation is absent. Its role is discovery, triangulation, and identification of close primary work already inherited or separately screened.

### C. Ficha completa de cada paper leído íntegramente

#### N01 — Chen & Tanaka-Ishii (2026)

**Identidad bibliográfica.** Haoyang Chen and Kumiko Tanaka-Ishii. *Executable explanation traces for legal LLM predictions via retrieval-augmented codification*. Frontiers in Artificial Intelligence, Volume 9, 2026. DOI `10.3389/frai.2026.1905145`. Original Research; peer-reviewed; open access.

**Tarea y contexto.** Predicción legal text-to-label en cinco benchmarks y jurisdicciones/dominios heterogéneos: Chinese criminal law (CAIL), European human-rights cases (ECHR), U.S. class-action complaints (CAP), Indian judgments (ILDC) y Japanese tort cases (JTD).

**Pipeline reportado.** El sistema recupera dos tipos de conocimiento: `R1`, fuentes legales/autoridad del dominio, y `R2`, ejemplos in-domain resueltos construidos de forma fold-safe. El LLM compila la entrada y materiales recuperados en una representación ejecutable, recibe feedback y puede refinar iterativamente el programa. La representación final produce la etiqueta y conserva un trace con fuentes recuperadas, condiciones, ramas, feedback y predicción.

**Papel de histórico/precedentes.** `R2` aporta ejemplos in-domain resueltos. Los autores establecen un control fold-safe: solo instancias de entrenamiento están disponibles para retrieval en cada fold y se excluye la instancia held-out.

**Papel de normativa/evidencia.** `R1` aporta estatutos, artículos, regulaciones, material judicial u otras fuentes jurídicas curadas. Esas fuentes pueden determinar definiciones, umbrales, excepciones y condiciones usadas por la representación ejecutable.

**Quién fija la decisión.** No existe un ranking/clase externo e inmutable fijado por un componente upstream independiente. El programa generado/refinado es parte del proceso que produce la etiqueta final.

**Reranking.** No existe un ranking HS equivalente. La iteración puede modificar la representación decisoria y solicitar material adicional; por tanto, no satisface una prohibición de feedback hacia el decision path.

**Papel exacto del LLM y capacidad de alterar candidatos/clases.** El LLM no es un explicador downstream impotente: genera/refina la representación ejecutable que calcula la predicción. En consecuencia, N01 no satisface F2 estricto.

**Auditabilidad/trazabilidad evaluada.** Se evalúan propiedades de explicación separadas de label accuracy: executability, refinement depth, final-program exceptions, source support, material-edit sensitivity y failure analysis. En el análisis de source support, se extraen predicates de los traces finales y se contrastan con pasajes recuperados de `R1` mediante un verificador LLM usado como auditoría de soporte de fuente. Una condición solo cuenta como soportada cuando puede emparejarse con una declaración explícita del corpus legal recuperado. Los autores recalcan que esta medida es un diagnóstico de grounding y no prueba legal correctness, doctrinal completeness ni que el predicate deba ser dispositivo.

**Resultados pertinentes.** En 1,000 instancias muestreadas para la auditoría de predicate support, el método completo reporta 99.12% supported / 0.88% unsupported en CAIL y 91.13% / 8.87% en CAP; IRCoT reporta 97.88% / 2.12% y 82.63% / 17.37%, respectivamente. La sensibilidad a ediciones jurídicamente materiales se evalúa además en 50 instancias manualmente editadas por dataset auditado. Los autores presentan estas medidas como diagnostics de explicación, no como certificados de validez jurídica.

**Split/dependencia.** Se reporta retrieval de ejemplos `R2` fold-safe, pero no un control de agrupamiento por DAM/declaración/importer/product family equivalente al que busca F3.

**Limitaciones relevantes.** Executability no implica completitud jurídica; source support no implica legal correctness; algunas etiquetas dependen de procedimiento, evidencia o discreción no recuperables desde el input y las fuentes. El propio paper preserva esta frontera.

**Etiquetado epistemológico.** `REPORTADO_POR_AUTORES`: pipeline R1/R2, fold-safe retrieval, métricas de trace/source support, resultados y límites anteriores. `INFERENCIA_CRITICA`: este diseño constituye prior art directo contra una formulación amplia de F5 en regulatory AI, pero no contra F1 ni F2 estrictos porque la explicación/programa participa en producir la decisión.

**Relación S1–S5.** S1: no satisface. S2: prior art parcial en explicación/auditabilidad, falla el aislamiento upstream/downstream. S3: solo aporta fold-safe example retrieval, no grouped split administrativo. S4: satisface el núcleo conceptual de evaluación explícita y separada de source support/auditability por trace/instancia. S5: combina retrieval de fuentes, ejemplos y evaluación audit-oriented, pero no la arquitectura fija del proyecto.

#### N02 — Wube et al. (2026)

**Identidad bibliográfica.** Hana Demma Wube et al. *A review of machine learning, deep learning and large language model based harmonized system code classification techniques for import and export commodities*. Discover Computing 29, article 505 (2026). DOI `10.1007/s10791-026-10428-y`. Review; open access.

**Tarea y contexto.** Revisión sistemática de técnicas ML/DL/LLM para clasificación HS de mercancías importadas/exportadas. Los autores identificaron inicialmente 322 registros y seleccionaron 29 estudios primarios después de criterios de inclusión/exclusión y consenso de revisores. La búsqueda cubrió Scopus, Web of Science, IEEE Xplore y Google Scholar; el corpus objetivo fue 2015–2025.

**Arquitectura/pipeline.** No propone un sistema clasificatorio nuevo. Su función para 0B-06 es mapear tendencias, evaluation settings, model explanation y close prior art.

**Histórico/precedentes y normativa/evidencia.** La revisión cubre trabajos con datos aduaneros históricos, semantic similarity, deep classification, structured knowledge y LLMs, pero no demuestra por sí misma la existencia de la arquitectura F1. Sus afirmaciones sobre estudios concretos se tratan como secondary claims hasta verificar la fuente primaria.

**Quién fija la decisión / reranking / papel del LLM.** No aplica como mecanismo propio. La revisión describe múltiples paradigmas; no puede utilizarse para imputar a un estudio primario una capacidad de reranking, aislamiento del LLM o post-ranking evidence retrieval no comprobados en la fuente primaria.

**Auditabilidad.** Los autores reportan que, en los 29 estudios revisados, la explainability se orienta principalmente a interpretación user-facing y se presta poca atención a auditability/compliance. También señalan que la evaluación se concentra predominantemente en Accuracy, F1 y Top-k. Estas afirmaciones son `SECONDARY_CLAIM_UNVERIFIED` respecto de cada artículo individual y no se usan como prueba final de ausencia.

**Split/dependencia.** La revisión describe protocolos estándar de partición en parte de la literatura, pero no identifica como patrón central un grouped split por declaración/importador/entidad. Esto orientó S3, pero la conclusión de F3 se basa en la búsqueda dirigida adicional y no exclusivamente en N02.

**Resultados pertinentes.** No se trasladan comparaciones de rendimiento entre papers como ranking debido a heterogeneidad de datasets, nivel HS, idiomas y protocolos; la propia revisión advierte contra comparaciones horizontales estrictas.

**Limitaciones.** Ventana primaria 2015–2025; solo inglés; bases limitadas; posible selection/publication bias; es secondary evidence.

**Etiquetado epistemológico.** `REPORTADO_POR_AUTORES`: metodología de revisión, 322→29, observaciones sobre explainability/auditability y limitaciones. `INFERENCIA_CRITICA`: N02 es útil para discovery y corroboración, pero no puede falsar ni confirmar por sí sola F1–F5.

**Relación S1–S5.** S1–S3: apoyo de discovery y negativos acotados. S4: corrobora que auditability merece una búsqueda específica, pero no reemplaza N01 como evidencia primaria. S5: mapa de combinaciones, no antecedente combinado directo.

### D. Matriz de falsación por candidato

| paper | F1 | F2 | F3 | F5 | evidencia exacta | condición que satisface | condición que no satisface |
|---|---|---|---|---|---|---|---|
| N01 Chen & Tanaka-Ishii 2026 | NO_DIRECT | PARTIAL | NO_DIRECT | DIRECT | executable trace; R1 legal-source retrieval; R2 fold-safe examples; separate source-support audit on predicates; 1,000 sampled instances; explicit warning that source support ≠ legal correctness | formal, explicit, separate trace/source-support evaluation; audit-oriented per-instance diagnostics | trace/program itself computes and can revise prediction; no immutable upstream Top-k; not HS/customs |
| N02 Wube et al. 2026 | SECONDARY_ONLY | SECONDARY_ONLY | SECONDARY_ONLY | PARTIAL_SECONDARY | systematic review of 29 HS studies; reports explainability predominantly user-facing and limited auditability attention | highly specific map of HS literature and discovery of close works | secondary synthesis cannot establish exact architecture, split or absence without primary verification |
| N03 Liao et al. 2024 | NO | NO | CLOSE_NEGATIVE | NO | HSD 320,360 entries / 227 codes; split 0.8:0.1:0.1; direct EBLCS classification | recent direct customs/HS benchmark | no reported grouping by declaration/entity in inspected split; no post-ranking evidence; no isolated LLM; no separate documentary auditability |
| N04 Sun et al. 2025 | NO | NO | NOT_ESTABLISHED | NO | FTSGI directly fuses text-sequence and graph information for classification | recent customs-specific graph/text classifier | graph/text model decides class; no fixed historical ranking + downstream documentary evidence; no explanation-only LLM or separate auditability rubric identified |

`NO`, `NO_DIRECT`, `CLOSE_NEGATIVE`, `SECONDARY_ONLY` y `NOT_ESTABLISHED` son descriptores de la matriz de evidencia, no etiquetas de pressure test. Las etiquetas gobernantes aparecen en la sección E.

### E. Resultado acumulado por candidato

#### F1 — ranking histórico fijado + evidencia normativa posterior no-reranking

**Pressure test:** `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`.

**Papers/leads determinantes:** ninguno admisible satisface todas las condiciones. N02 sirve como mapa secundario; N03/N04 son negativos cercanos; el lead Hendrawan et al. 2026, registrado en G, es funcionalmente cercano pero no admisible y además integra KG/LLM en clasificación.

**Formulación previa:** precedentes históricos recuperados generan y fijan el ranking de candidatos; la evidencia normativa se incorpora exclusivamente después para documentar esos candidatos y no puede modificar el orden.

**Cambio requerido:** no se exige cambio sustantivo por literatura nueva admisible. Debe preservarse el calificativo estrecho y evitar cualquier afirmación de ausencia universal.

**Sigue sin demostrarse:** que esta combinación sea novel o inexistente fuera del alcance buscado; que ningún sistema comercial/no publicado la implemente; que la propiedad por sí sola constituya contribución suficiente.

#### F2 — LLM/generador exclusivamente explicativo sobre Top-k externo e inmutable

**Pressure test:** `PARTIAL_PRIOR_ART_FOUND`.

**Paper determinante:** N01 Chen & Tanaka-Ishii 2026.

**Formulación previa:** componente generativo exclusivamente explicativo que recibe un ranking/Top-k fijado externamente por un componente previo independiente, sin capacidad para introducir, eliminar, sustituir o reordenar códigos y sin feedback hacia la decisión.

**Cambio requerido:** no eliminar F2, pero hacer explícito que “explicación auditable” o “executable explanation” no bastan: el prior art reciente muestra sistemas donde explicación y decisión están acopladas. La formulación superviviente debe conservar como condición constitutiva el aislamiento causal/contractual del generador downstream respecto de un Top-k ya fijado externamente.

**Sigue sin demostrarse:** novelty o ausencia universal de ese contrato estricto; tampoco se demuestra que el aislamiento contractual sea por sí mismo suficiente como contribución científica.

#### F3 — grouped split / dependencia por unidad correlacionada

**Pressure test:** `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`.

**Papers determinantes:** N03 es un negativo cercano: usa una partición 0.8:0.1:0.1 sobre muestras de un dataset aduanero, sin que el diseño inspeccionado reporte agrupamiento por declaración/entity. N02 sugiere que los esquemas estándar de partición siguen siendo comunes, pero es evidencia secundaria.

**Formulación previa:** control explícito de dependencia por unidad administrativa/entidad cuando observaciones correlacionadas pueden cruzar particiones; conserva caveat de aplicabilidad.

**Cambio requerido:** ninguno más allá de mantener F3 como candidato metodológico condicionado al tipo de datos; no convertir la búsqueda negativa en novelty.

**Sigue sin demostrarse:** inexistencia de grouped/entity-aware splitting en toda la literatura de customs/trade/product classification. Tampoco se etiqueta como leakage un paper solo por no reportar agrupamiento.

#### F5 — evaluación formal, explícita y separada de auditabilidad documental por salida/caso

**Pressure test:** `DIRECT_PRIOR_ART_FOUND`.

**Paper determinante:** N01 Chen & Tanaka-Ishii 2026.

**Formulación previa:** candidato estrecho de evaluación formal, explícita y separada, por salida/caso, de auditabilidad documental, diferenciada de accuracy, path validity, faithfulness, metadata, citations visibles/traceability y rationale.

**Cambio requerido:** la formulación amplia “regulatory AI carece de evaluación formal separada de auditabilidad/source support” queda falsada. N01 separa label accuracy de trace-level metrics y realiza una auditoría de source support entre conditions/predicates aplicados y fuentes legales recuperadas, con diagnóstico por instancias/salidas y límites explícitos de legal correctness. Si F5 se conserva para el gate posterior, solo puede reformularse de manera más estrecha y contextual como una posible propiedad **HS/customs-specific** o como integración con la arquitectura fija del proyecto; no como ausencia general en regulatory AI.

**Sigue sin demostrarse:** que la variante HS/customs-specific sea novel; que ningún paper HS fuera del alcance buscado implemente evaluación equivalente; que auditability implique substantive/legal correctness.

### F. Papers cercanos rechazados

1. **Liao et al. (2024), Applied Sciences, DOI `10.3390/app142210267` — `REJECT`.** Directamente relevante a HS classification, pero es un clasificador EBLCS end-to-end. El split reportado es 0.8/0.1/0.1 sobre 320,360 entradas; no se reportó en el diseño inspeccionado agrupamiento por declaración/entity equivalente a F3. No satisface F1, F2 o F5. Esta ausencia no se etiqueta como leakage.
2. **Sun, Zhou & Che (2025), Expert Systems, DOI `10.1111/exsy.70057` — `REJECT`.** Customs-specific y reciente, pero FTSGI usa secuencia + key elements + graph learning para decidir directamente la clase. No existe separación histórica-ranking → evidencia normativa posterior, ni LLM downstream aislado, ni evaluación separada de auditabilidad documental identificada.
3. **Navasardyan (2024), *Interpretable and Generalizable HTS Code Classification Framework* — `REJECT` en este gate.** El trabajo localizado utiliza GPT para clasificar y explicar en el mismo proceso; no satisface el contrato F2. La calidad/indexación/cuártil no se cerraron con una fuente suficientemente fuerte para promoverlo como candidato nuevo bajo `BIBLIOGRAPHIC_FRAMEWORK.md`, por lo que no determina el pressure test.

### G. Referencias no admisibles pero informativas

1. **Syepta Hendrawan, Heru Purnomo Ipung, Eka Budiarto (2026), *Integrating knowledge graphs and LLM for Indonesia HS code classification: A focus on heavy equipment parts*, Procedia Computer Science 284, 76–85, DOI `10.1016/j.procs.2026.06.621` — `NON_ADMISSIBLE_LEAD`.** Es el lead S5 más cercano localizado: ML sobre datos históricos, KG con regulación y LLM para explicación; reporta RAGAS. Sin embargo, es proceedings/Procedia, categoría expresamente no admisible para `CANDIDATE_NEW`. Además, la arquitectura integrada no demuestra un Top-k histórico inmutable antes de evidencia normativa, y RAGAS faithfulness/context metrics no equivale a la evaluación documental per-output exigida por F5.
2. **Trabajos 2025–2026 localizados como preprints/under-review sobre HTS/agentic classification — `NON_ADMISSIBLE_LEAD`.** Se conservaron solo como señales de búsqueda. No determinan F1–F5 porque el prompt prohíbe usar preprints/manuscritos no publicados como nuevas referencias admitidas. Cuando alguno coincide con un trabajo ya heredado por freezes previos, tampoco se contabiliza como referencia nueva.
3. **Tesis/proyectos académicos recientes sobre agentic HS classification — `NON_ADMISSIBLE_LEAD`.** Pueden combinar RAG/LLM y métricas de clasificación, pero el tipo documental los excluye del gate de admisión y no se emplean para declarar prior art determinante.

### H. Dictamen bibliográfico provisional

`PASS — DIRECTED_SEARCH_COMPLETE`

La búsqueda dirigida produjo un resultado falsacionista material: F5 debe estrecharse porque existe prior art admisible reciente en regulatory AI con evaluación explícita, separada y source-supported de traces/salidas. F2 encuentra prior art parcial que obliga a mantener de forma estricta el aislamiento del generador respecto de la decisión. F1 y F3 no presentan un match directo dentro del alcance buscado, lo cual es únicamente un resultado negativo acotado. No se declara novelty ni gap definitivo.

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
0C = BLOCKED
```

### I. Trazabilidad

- Repositorio/rama consumidos: `elVladdi/gci-nandina-rag`, `article/main-manuscript`.
- Commit/HEAD consumido: `9d7a482b05d30def281ea5ef4c2e34c54cb2cf5d`.
- Fecha de búsqueda: `2026-09-15`.
- DOI/URLs primarias verificadas:
  - `https://doi.org/10.3389/frai.2026.1905145` — Frontiers in Artificial Intelligence.
  - `https://doi.org/10.1007/s10791-026-10428-y` — Discover Computing / Springer Nature.
  - `https://doi.org/10.3390/app142210267` — Applied Sciences / MDPI.
  - `https://doi.org/10.1111/exsy.70057` — Expert Systems / Wiley.
  - `https://doi.org/10.1016/j.procs.2026.06.621` — Procedia Computer Science / Elsevier; no admisible por tipo.
- PDFs completos leídos para candidatos recomendados/review:
  - Chen & Tanaka-Ishii 2026: PDF oficial Frontiers, 18 páginas.
  - Wube et al. 2026: PDF oficial Springer Nature, 39 páginas.
- Verificación editorial/indexación:
  - Frontiers journal facts e impact page: Scopus, Web of Science ESCI; cuartiles vigentes consultados el 2026-09-15.
  - Discover Computing: cobertura Scopus/WoS verificada mediante registros ISSN/index; SJR 2025 consultado para la condición Q2. Debido a que la señal de cuartil varía por categoría y el trabajo es una revisión secundaria, se mantiene `CANDIDATE_NEW — REVIEW`, no `ADMIT_RECOMMENDED`.
- Limitaciones de acceso: no se dispuso de una interfaz autenticada de JCR/Scopus para cada journal; se usaron páginas oficiales de editoriales y registros públicos de indexación/cuártil. Los hit counts del buscador no fueron reproducibles y se marcaron `NOT_RELIABLY_COUNTABLE`.
- Ningún resultado negativo de búsqueda se interpreta como inexistencia universal.

---

## English

### Reconstructed entry state

```text
ACTIVE_PHASE = 0B
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
0C = BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

The search was executed as a bounded falsification-oriented pressure test of F1, F2, F5 and, secondarily, F3. It was not treated as open-ended corpus expansion or as a confirmation-oriented novelty search.

### A. Search control

| search_family | queries_used | sources/databases_consulted | date_searched | hits_screened | full_texts_read | notes |
|---|---|---|---|---|---:|---|
| S1 / F1 | `"HS code" historical precedents retrieval normative evidence explanation journal`; `"customs tariff classification" RAG legal evidence explanation journal`; `"harmonized system" retrieval legal evidence LLM classification journal`; `"HTS code" rulings machine learning classification retrieval`; `customs classification historical cases retrieval explanation` | web search; publisher/journal pages; Springer Nature; Wiley; MDPI; Elsevier/ScienceDirect; DOI landing pages; references from close candidates | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 1 | No admissible 2022–2026 journal article was found that jointly satisfies fixed historical ranking, strictly subsequent normative evidence, and prohibition on reordering/substituting/introducing codes. Partial antecedents and non-admissible leads were recorded. |
| S2 / F2 | `"HS code" explanation retrieval evidence customs journal`; `LLM explanation fixed ranking Top-k customs`; `regulatory classification downstream explanation fixed decision LLM`; `customs LLM explanation immutable candidates` | web search; Frontiers; Springer Nature; Wiley; Elsevier; DOI/publisher pages; related work/references | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 2 | Admissible regulatory-AI prior art with formal explanation evaluation was found, but the generator/trace participates in the decision; there is no contractual isolation from an immutable upstream Top-k. |
| S3 / F3 | `"HS code classification" group split declaration shipment importer leakage`; `"customs commodity classification" grouped split declaration dataset`; `"trade classification" grouped cross validation declaration shipment product family HS code`; `"HS code" duplicate leakage train test declaration`; `"customs declaration" machine learning grouped split classification HS` | web search; MDPI; Springer Nature; Wiley; Nature; recent HS literature identified through review and references | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 1 | No direct admissible precedent was found with a DAM/declaration/importer/shipment/entity grouped split or equivalent dependence control. This is reported only within the searched scope and not as novelty. |
| S4 / F5 | `documentary auditability source-to-claim regulatory AI`; `legal classification auditability RAG source support`; `per-output evidence traceability legal AI evaluation`; `source support explanation trace regulatory LLM` | web search; Frontiers; Springer Nature; publisher PDFs; related references | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 2 | One admissible Q1 paper was found with separate source-support and trace-level evaluation by instance/output, sufficient to falsify a broad F5 formulation in regulatory AI. |
| S5 | `HS customs historical data knowledge graph LLM explanation auditability`; `customs RAG historical classification regulatory evidence LLM`; `HS code ML KG LLM explainability auditability` | web search; Elsevier/ScienceDirect; Springer Nature; Frontiers; Wiley; related references | 2026-09-15 | NOT_RELIABLY_COUNTABLE | 2 | The closest combined HS/customs antecedent located was proceedings and therefore non-admissible. The strongest admissible antecedent combines legal-source retrieval, fold-safe examples, and auditability, but does not satisfy S1/F1 or strict S2/F2 isolation. |

Hit counts were not reliably reproducible in the available search interface and are therefore recorded as `NOT_RELIABLY_COUNTABLE`. Deduplication used DOI/title. Works already inherited from 0B-01–0B-05C are not counted as new references.

### B. New-candidate matrix

| ID | authors | year | title | journal | DOI | indexing | quartile/source | full PDF | search family | exact task | method | dataset/context | closest relevant property | critical missing property | recommendation |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N01 | Haoyang Chen; Kumiko Tanaka-Ishii | 2026 | *Executable explanation traces for legal LLM predictions via retrieval-augmented codification* | Frontiers in Artificial Intelligence | `10.3389/frai.2026.1905145` | Scopus; Web of Science ESCI; publisher index list | Frontiers current impact page consulted 2026-09-15: JCR Q1 / CiteScore Q1 | YES — publisher OA PDF, 18 pp., read in full | S2, S4, S5 | legal text-to-label prediction with executable explanation traces | retrieval-augmented codification + iterative refinement + executable traces | five legal benchmarks: CAIL, ECHR, CAP, ILDC, JTD | explicit trace-level audit diagnostics; post-hoc source-support audit between applied predicates and retrieved legal sources, separate from label accuracy | the trace/program itself produces the label and can be revised by feedback; no independent immutable upstream Top-k; not a customs/HS task | `CANDIDATE_NEW — ADMIT_RECOMMENDED` |
| N02 | Hana Demma Wube; Sintayehu Zekarias Esubalew; Kena Wendimu Gebisa; Firesew Fayiso Weldesellasie; Taye Girma Debelee | 2026 | *A review of machine learning, deep learning and large language model based harmonized system code classification techniques for import and export commodities* | Discover Computing | `10.1007/s10791-026-10428-y` | Scopus and Web of Science coverage verified through ISSN/index records; Springer Nature journal | SCImago/SJR 2025: Q2 in Library and Information Sciences, Q3 in Information Systems; used only because of very high HS specificity | YES — Springer OA PDF, 39 pp., read in full | S1–S5 as discovery/corroboration | systematic review of HS-code classification | systematic literature review | 29 selected primary studies, search window 2015–2025 | highly specific map of HS methods; explicitly distinguishes explainability concerns and notes limited attention to auditability | secondary evidence; cannot independently establish absence, architecture, split details, or novelty without primary-source verification | `CANDIDATE_NEW — REVIEW` |
| N03 | Mengjie Liao; Lei Huang; Jian Zhang; Luona Song; Bo Li | 2024 | *Enhanced HS Code Classification for Import and Export Goods via Multiscale Attention and ERNIE-BiLSTM* | Applied Sciences | `10.3390/app142210267` | peer-reviewed journal; publisher/DOI metadata verified | NOT_USED_FOR_ADMISSION — rejected on functional mismatch | Publisher OA full text/PDF available; admission gate not pursued after functional rejection | S3 close negative | direct HS classification from customs goods text | ERNIE + BiLSTM + channel/spatial attention | HSD: 320,360 entries, 227 HS codes; train/validation/test ratio 0.8/0.1/0.1 | recent direct HS classifier using historical customs-clearance data | no reported grouped split by declaration/entity in the inspected experimental design; no F1/F2/F5 architecture | `REJECT` |
| N04 | Haichao Sun; Chengjie Zhou; Chao Che | 2025 | *Customs Commodity Classification Method Based on the Fusion of Text Sequence and Graph Information* | Expert Systems | `10.1111/exsy.70057` | Scopus and Science Citation Index Expanded listed by Wiley | NOT_USED_FOR_ADMISSION — rejected on functional mismatch | Publisher full text/metadata screened; no admission recommendation made | S1, S2, S5 close negative | direct customs commodity classification | FTSGI: sequence learning + key-element identification + graph learning | real customs declaration data | combines text sequence and graph structure in a customs task | graph/text model directly decides class; no historical fixed Top-k + post-ranking normative evidence; no isolated explanation-only LLM; no separate documentary-auditability evaluation identified | `REJECT` |

`N02` is a secondary review and is not used as independent proof that an architecture/evaluation is absent. Its role is discovery, triangulation, and identification of close primary work already inherited or separately screened.

### C. Full record for each paper read in full

#### N01 — Chen & Tanaka-Ishii (2026)

**Bibliographic identity.** Haoyang Chen and Kumiko Tanaka-Ishii. *Executable explanation traces for legal LLM predictions via retrieval-augmented codification*. Frontiers in Artificial Intelligence, Volume 9, 2026. DOI `10.3389/frai.2026.1905145`. Original Research; peer-reviewed; open access.

**Task and context.** Legal text-to-label prediction across five heterogeneous benchmarks/jurisdictions/domains: Chinese criminal law (CAIL), European human-rights cases (ECHR), U.S. class-action complaints (CAP), Indian judgments (ILDC), and Japanese tort cases (JTD).

**Reported pipeline.** The system retrieves two knowledge types: `R1`, legal sources/authority for the domain, and `R2`, solved in-domain examples constructed fold-safely. The LLM compiles the input and retrieved materials into an executable representation, receives feedback, and can iteratively refine the program. The final representation produces the label and retains a trace containing retrieved sources, conditions, branches, feedback, and prediction.

**Role of history/precedents.** `R2` supplies solved in-domain examples. The authors establish a fold-safe control: only training instances are available for retrieval within each fold, and the held-out instance is excluded from the retrieval pool.

**Role of norms/evidence.** `R1` supplies statutes, articles, regulations, judicial materials, or other curated legal sources. Those sources can determine definitions, thresholds, exceptions, and conditions used by the executable representation.

**Who fixes the decision.** There is no immutable external rank/class fixed by an independent upstream component. The generated/refined program is part of the process that produces the final label.

**Reranking.** There is no equivalent HS ranking. Iteration can modify the decision representation and request additional material; therefore it does not satisfy a no-feedback constraint toward the decision path.

**Exact LLM role and ability to alter candidates/classes.** The LLM is not a powerless downstream explainer: it generates/refines the executable representation that computes the prediction. N01 therefore does not satisfy strict F2.

**Evaluated auditability/traceability.** Explanation properties are evaluated separately from label accuracy: executability, refinement depth, final-program exceptions, source support, material-edit sensitivity, and failure analysis. In the source-support analysis, predicates are extracted from final traces and checked against retrieved `R1` passages by an LLM verifier used as a source-support audit. A condition counts as supported only if an explicit supporting statement can be matched in the retrieved legal-source corpus. The authors explicitly state that this is a grounding diagnostic and does not prove legal correctness, doctrinal completeness, or that the predicate should be dispositive.

**Relevant results.** On 1,000 sampled instances for predicate-support auditing, the full method reports 99.12% supported / 0.88% unsupported on CAIL and 91.13% / 8.87% on CAP; IRCoT reports 97.88% / 2.12% and 82.63% / 17.37%, respectively. Sensitivity to legally material edits is additionally evaluated on 50 manually edited instances per audited dataset. The authors frame these measures as explanation diagnostics, not certificates of legal validity.

**Split/dependence.** Fold-safe `R2` example retrieval is reported, but there is no DAM/declaration/importer/product-family grouping control equivalent to F3.

**Relevant limitations.** Executability does not imply legal completeness; source support does not imply legal correctness; some labels depend on procedure, evidence, or discretion not recoverable from the input and retrieved sources. The paper itself preserves this boundary.

**Epistemic labeling.** `REPORTADO_POR_AUTORES`: R1/R2 pipeline, fold-safe retrieval, trace/source-support metrics, results, and stated limitations above. `INFERENCIA_CRITICA`: the design is direct prior art against a broad F5 formulation in regulatory AI, but not against strict F1 or F2 because the explanation/program participates in producing the decision.

**S1–S5 relation.** S1: not satisfied. S2: partial prior art in explanation/auditability, but fails upstream/downstream isolation. S3: only fold-safe example retrieval, not administrative grouped splitting. S4: satisfies the conceptual core of explicit, separate source-support/auditability evaluation by trace/instance. S5: combines source retrieval, examples, and audit-oriented evaluation, but not the project's fixed architecture.

#### N02 — Wube et al. (2026)

**Bibliographic identity.** Hana Demma Wube et al. *A review of machine learning, deep learning and large language model based harmonized system code classification techniques for import and export commodities*. Discover Computing 29, article 505 (2026). DOI `10.1007/s10791-026-10428-y`. Review; open access.

**Task and context.** Systematic review of ML/DL/LLM methods for HS classification of import/export commodities. The authors initially identified 322 records and selected 29 primary studies after inclusion/exclusion screening and reviewer consensus. Searches covered Scopus, Web of Science, IEEE Xplore, and Google Scholar; the target literature window was 2015–2025.

**Architecture/pipeline.** It does not propose a new classification system. Its role in 0B-06 is to map trends, evaluation settings, model explanation, and close prior art.

**History/precedents and norms/evidence.** The review covers work using historical customs data, semantic similarity, deep classification, structured knowledge, and LLMs, but does not by itself demonstrate the F1 architecture. Claims about individual studies are treated as secondary until the primary source is verified.

**Who fixes the decision / reranking / LLM role.** Not applicable as its own mechanism. The review describes multiple paradigms and cannot be used to impute reranking, LLM isolation, or post-ranking evidence retrieval to a primary paper unless verified in that source.

**Auditability.** The authors report that across the 29 reviewed studies, explainability is mainly user-facing and comparatively little attention is paid to auditability/compliance. They also report that evaluation is dominated by Accuracy, F1, and Top-k. These are `SECONDARY_CLAIM_UNVERIFIED` with respect to each underlying paper and are not used as final proof of absence.

**Split/dependence.** The review describes standard partitioning protocols in part of the literature, but does not identify declaration/importer/entity grouped splitting as a central pattern. This guided S3, while the F3 conclusion also rests on the separate directed search rather than N02 alone.

**Relevant results.** Cross-paper performance figures are not carried over as a ranking because datasets, HS levels, languages, and protocols are heterogeneous; the review itself cautions against strict horizontal performance comparisons.

**Limitations.** Primary window 2015–2025; English only; limited databases; possible selection/publication bias; secondary evidence.

**Epistemic labeling.** `REPORTADO_POR_AUTORES`: review method, 322→29, observations on explainability/auditability, and review limitations. `INFERENCIA_CRITICA`: N02 is useful for discovery and corroboration but cannot independently falsify or confirm F1–F5.

**S1–S5 relation.** S1–S3: discovery support and bounded negatives. S4: corroborates the need for an auditability-specific search but does not replace N01 as primary evidence. S5: map of combinations, not a direct combined antecedent.

### D. Falsification matrix by candidate

| paper | F1 | F2 | F3 | F5 | exact evidence | satisfied condition | unsatisfied condition |
|---|---|---|---|---|---|---|---|
| N01 Chen & Tanaka-Ishii 2026 | NO_DIRECT | PARTIAL | NO_DIRECT | DIRECT | executable trace; R1 legal-source retrieval; R2 fold-safe examples; separate source-support audit on predicates; 1,000 sampled instances; explicit warning that source support ≠ legal correctness | formal, explicit, separate trace/source-support evaluation; audit-oriented per-instance diagnostics | trace/program itself computes and can revise prediction; no immutable upstream Top-k; not HS/customs |
| N02 Wube et al. 2026 | SECONDARY_ONLY | SECONDARY_ONLY | SECONDARY_ONLY | PARTIAL_SECONDARY | systematic review of 29 HS studies; reports explainability predominantly user-facing and limited auditability attention | highly specific map of HS literature and discovery of close work | secondary synthesis cannot establish exact architecture, split, or absence without primary verification |
| N03 Liao et al. 2024 | NO | NO | CLOSE_NEGATIVE | NO | HSD 320,360 entries / 227 codes; split 0.8:0.1:0.1; direct EBLCS classification | recent direct customs/HS benchmark | no reported declaration/entity grouping in inspected split; no post-ranking evidence; no isolated LLM; no separate documentary auditability |
| N04 Sun et al. 2025 | NO | NO | NOT_ESTABLISHED | NO | FTSGI directly fuses text-sequence and graph information for classification | recent customs-specific graph/text classifier | graph/text model decides class; no fixed historical ranking + downstream documentary evidence; no explanation-only LLM or separate auditability rubric identified |

`NO`, `NO_DIRECT`, `CLOSE_NEGATIVE`, `SECONDARY_ONLY`, and `NOT_ESTABLISHED` are evidence-matrix descriptors, not governing pressure-test labels. Governing labels appear in Section E.

### E. Cumulative result by candidate

#### F1 — fixed historical ranking + subsequent non-reranking normative evidence

**Pressure test:** `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`.

**Determinant papers/leads:** no admissible paper satisfies all conditions. N02 is secondary mapping; N03/N04 are close negatives; the Hendrawan et al. 2026 lead recorded in G is functionally close but non-admissible and integrates KG/LLM into classification.

**Previous wording:** retrieved historical precedents generate and fix the candidate ranking; normative evidence is added only afterward to document those candidates and cannot alter their order.

**Required change:** no substantive change is required from newly admissible literature. The narrow qualifier must remain and no universal-absence statement may be made.

**Still unproven:** that the combination is novel or absent outside the searched scope; that no commercial/unpublished system implements it; that the property alone is a sufficient scientific contribution.

#### F2 — explanation-only LLM/generator over an external immutable Top-k

**Pressure test:** `PARTIAL_PRIOR_ART_FOUND`.

**Determinant paper:** N01 Chen & Tanaka-Ishii 2026.

**Previous wording:** an exclusively explanatory generative component receives a ranking/Top-k fixed externally by an independent prior component, with no ability to introduce, delete, substitute, or reorder codes and no feedback toward the decision.

**Required change:** do not eliminate F2, but make explicit that “auditable explanation” or “executable explanation” is insufficient: recent prior art shows systems in which explanation and decision are coupled. The surviving formulation must retain causal/contractual isolation of the downstream generator from an externally fixed Top-k as a constitutive condition.

**Still unproven:** novelty or universal absence of this strict contract; nor is it shown that contractual isolation alone is a sufficient scientific contribution.

#### F3 — grouped split / dependence by correlated unit

**Pressure test:** `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`.

**Determinant papers:** N03 is a close negative: it uses a 0.8:0.1:0.1 sample split on a customs dataset, without the inspected design reporting declaration/entity grouping. N02 suggests that standard partitioning remains common, but it is secondary evidence.

**Previous wording:** explicit dependence control by administrative/entity grouping when correlated observations can cross partitions; applicability caveat retained.

**Required change:** none beyond retaining F3 as a methodological candidate conditional on data structure; do not convert the negative search into novelty.

**Still unproven:** absence of grouped/entity-aware splitting across the entire customs/trade/product-classification literature. A paper is also not labeled as leaking merely because grouping is not reported.

#### F5 — formal, explicit, separate per-output/case documentary-auditability evaluation

**Pressure test:** `DIRECT_PRIOR_ART_FOUND`.

**Determinant paper:** N01 Chen & Tanaka-Ishii 2026.

**Previous wording:** narrow candidate of formal, explicit, separate per-output/case evaluation of documentary auditability, distinguished from accuracy, path validity, faithfulness, metadata, visible citations/traceability, and rationale.

**Required change:** the broad statement that “regulatory AI lacks formal, separate auditability/source-support evaluation” is falsified. N01 separates label accuracy from trace-level metrics and performs a source-support audit between applied conditions/predicates and retrieved legal sources, with instance/output-level diagnostics and explicit legal-correctness limits. If F5 is retained for a later gate, it can only be framed more narrowly and contextually as a possible **HS/customs-specific** property or as integration with the project's fixed-candidate architecture; it cannot be framed as a general absence in regulatory AI.

**Still unproven:** that the HS/customs-specific variant is novel; that no HS paper outside the searched scope implements an equivalent evaluation; that auditability implies substantive/legal correctness.

### F. Close rejected papers

1. **Liao et al. (2024), Applied Sciences, DOI `10.3390/app142210267` — `REJECT`.** Directly relevant to HS classification, but it is an end-to-end EBLCS classifier. The reported split is 0.8/0.1/0.1 over 320,360 entries; the inspected design does not report declaration/entity grouping equivalent to F3. It does not satisfy F1, F2, or F5. This absence is not labeled as leakage.
2. **Sun, Zhou & Che (2025), Expert Systems, DOI `10.1111/exsy.70057` — `REJECT`.** Customs-specific and recent, but FTSGI uses sequence + key elements + graph learning to decide the class directly. There is no historical-ranking → subsequent normative-evidence separation, no isolated downstream LLM, and no identified separate documentary-auditability evaluation.
3. **Navasardyan (2024), *Interpretable and Generalizable HTS Code Classification Framework* — `REJECT` in this gate.** The located work uses GPT for classification and explanation within the same process and therefore does not satisfy F2. Journal quality/indexing/quartile could not be closed with sufficiently strong evidence for promotion under `BIBLIOGRAPHIC_FRAMEWORK.md`, so it does not determine the pressure test.

### G. Non-admissible but informative references

1. **Syepta Hendrawan, Heru Purnomo Ipung, Eka Budiarto (2026), *Integrating knowledge graphs and LLM for Indonesia HS code classification: A focus on heavy equipment parts*, Procedia Computer Science 284, 76–85, DOI `10.1016/j.procs.2026.06.621` — `NON_ADMISSIBLE_LEAD`.** This is the closest S5 lead located: ML over historical data, KG encoding regulation, and LLM explanation, with RAGAS reporting. However, it is proceedings/Procedia, a type explicitly non-admissible as `CANDIDATE_NEW`. Its integrated architecture also does not demonstrate an immutable historical Top-k before normative evidence, and RAGAS faithfulness/context metrics are not equivalent to F5's per-output documentary evaluation.
2. **Located 2025–2026 preprints/under-review works on HTS/agentic classification — `NON_ADMISSIBLE_LEAD`.** They were retained only as search signals. They do not determine F1–F5 because the prompt forbids using preprints/unpublished manuscripts as admitted new references. If a work overlaps a paper already inherited in previous freezes, it is also not counted as a new reference.
3. **Recent theses/projects on agentic HS classification — `NON_ADMISSIBLE_LEAD`.** They may combine RAG/LLM and classification metrics, but documentary type excludes them from the admission gate and they are not used as determinant prior art.

### H. Provisional bibliographic verdict

`PASS — DIRECTED_SEARCH_COMPLETE`

The directed search produced a material falsification result: F5 must be narrowed because recent admissible regulatory-AI prior art performs explicit, separate, source-supported trace/output evaluation. F2 encounters partial prior art that reinforces the need for strict generator/decision isolation. F1 and F3 show no direct match within the searched scope, which is only a bounded negative result. No novelty or final gap is declared.

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
0C = BLOCKED
```

### I. Traceability

- Repository/branch consumed: `elVladdi/gci-nandina-rag`, `article/main-manuscript`.
- Commit/HEAD consumed: `9d7a482b05d30def281ea5ef4c2e34c54cb2cf5d`.
- Search date: `2026-09-15`.
- Primary DOI/URLs verified:
  - `https://doi.org/10.3389/frai.2026.1905145` — Frontiers in Artificial Intelligence.
  - `https://doi.org/10.1007/s10791-026-10428-y` — Discover Computing / Springer Nature.
  - `https://doi.org/10.3390/app142210267` — Applied Sciences / MDPI.
  - `https://doi.org/10.1111/exsy.70057` — Expert Systems / Wiley.
  - `https://doi.org/10.1016/j.procs.2026.06.621` — Procedia Computer Science / Elsevier; non-admissible by type.
- Full PDFs read for recommended/review candidates:
  - Chen & Tanaka-Ishii 2026: official Frontiers PDF, 18 pages.
  - Wube et al. 2026: official Springer Nature PDF, 39 pages.
- Editorial/indexing verification:
  - Frontiers journal facts and impact page: Scopus, Web of Science ESCI; current quartiles consulted on 2026-09-15.
  - Discover Computing: Scopus/WoS coverage verified through ISSN/index records; SJR 2025 consulted for the Q2 condition. Because the quartile signal varies by category and the paper is a secondary review, it remains `CANDIDATE_NEW — REVIEW`, not `ADMIT_RECOMMENDED`.
- Access limitations: no authenticated JCR/Scopus interface was available for every journal; official publisher pages and public indexing/quartile records were used. Search-engine hit counts were not reproducible and are marked `NOT_RELIABLY_COUNTABLE`.
- No negative search result is interpreted as universal non-existence.
