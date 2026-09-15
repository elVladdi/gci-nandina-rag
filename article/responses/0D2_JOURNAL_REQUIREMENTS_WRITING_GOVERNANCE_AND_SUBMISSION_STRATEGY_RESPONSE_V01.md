# 0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío / Journal Requirements, Writing Governance, and Submission Strategy

## Español

### A. Estado de entrada y criterio de verificación

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D-1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
0D2_ENTRY_GATE = PASS / OPENED
0D-2 = READY_FOR_DRAFTING
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
TARGET_JOURNAL = PENDING_0D2_AND_AUTHOR_APPROVAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = DEFERRED_UNTIL_0D2_REVIEW
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_0D2_ENTRY
```

**ARCHIVOS LEÍDOS:** `article/START_HERE.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/reviews/0D2_ENTRY_GATE.md`; `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`; `article/reviews/0D_V02_INTERNAL_REVIEW.md`; `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/0B_PHASE_CLOSURE.md`.

**FASE ACTIVA:** `0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío`.

**REDACCIÓN DE MANUSCRITO AUTORIZADA:** no. Este artefacto define gobernanza pre-redacción; no contiene prosa destinada a ninguna sección del manuscrito.

**ESTADO CIENTÍFICO PRESERVADO:**

```text
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El contrato funcional congelado permanece sin modificación:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

La investigación web de 0D-2 se realizó el `2026-09-15` exclusivamente para requisitos editoriales, formato y estrategia de journals. Se priorizaron páginas oficiales de Elsevier/ScienceDirect y publicaciones actuales del propio journal. La página oficial de KBS confirma y enlaza su `Guide for Authors`, pero el cuerpo de esa guía devolvió `403 Forbidden` en el entorno de consulta. Por ello, ningún dato que solo apareciera en reproducciones de terceros se promovió a requisito oficial. Cuando la fuente oficial accesible no permitió verificar una regla específica, se marca `UNVERIFIED` y se evalúa separadamente si ese vacío es bloqueante o no para comenzar a redactar.

Clasificación usada en este artefacto:

```text
JOURNAL_SPECIFIC_REQUIREMENT
PUBLISHER_LEVEL_REQUIREMENT
RECOMMENDATION
OBSERVED_CONVENTION
UNVERIFIED
```

---

### B. Requisitos actuales de Knowledge-Based Systems

#### B.1 Matriz de requisitos

| elemento | estado oficial | requisito exacto o estado verificable | fuente oficial | impacto sobre redacción | acción antes de Fase 1 |
|---|---|---|---|---|---|
| Scope | `JOURNAL_SPECIFIC_REQUIREMENT` | KBS publica investigación original en sistemas basados en conocimiento y otras técnicas de IA, con cobertura de knowledge engineering, intelligent decision support y aplicaciones, entre otros temas | Elsevier KBS journal page: `https://shop.elsevier.com/journals/knowledge-based-systems/0950-7051` | El paper debe centrarse en el contrato arquitectónico-metodológico evaluado y no en una aplicación aduanera aislada | Mantener el framing B de 0C y su separación funcional |
| Tipo de artículo | `JOURNAL_SPECIFIC_REQUIREMENT` + `OBSERVED_CONVENTION` | El scope oficial declara investigación original; volúmenes 2026 de ScienceDirect clasifican artículos ordinarios como `Research article`/`Research Articles` | KBS official page + ScienceDirect KBS Volume 341 y artículos 2026 | El manuscrito se planifica como artículo de investigación, no review ni short communication | Fijar `Research article` como tipo operativo para redacción; revalidar etiqueta exacta del menú de submission antes de enviar |
| Plantilla Word específica KBS | `UNVERIFIED` | La página oficial enlaza el Guide for Authors, pero el cuerpo no fue accesible; no se verificó una plantilla Word obligatoria específica de KBS | enlace oficial KBS → Guide for Authors; acceso directo bloqueado | No se debe reconstruir ni inventar una plantilla KBS | Usar Word maestro neutral y editable; no denominarlo “plantilla KBS”; revalidar antes de submission |
| Plantilla LaTeX | `PUBLISHER_LEVEL_REQUIREMENT`/recurso editorial | Elsevier mantiene instrucciones y plantilla/clase `elsarticle`; su uso no demuestra por sí solo obligatoriedad específica de KBS | `https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions` | No obliga a cambiar el workflow Word aprobado por el autor | Mantener Word como master operacional; LaTeX queda como alternativa futura solo si se decide |
| Formato inicial Word | `PUBLISHER_LEVEL_REQUIREMENT` + `UNVERIFIED` a nivel KBS | Elsevier exige fuentes editables en sus flujos; el detalle KBS específico no pudo verificarse directamente | Elsevier author resources; KBS Guide link oficial no accesible | El formato de trabajo debe ser simple, editable y convertible; no se impondrá maquetación de producción | Crear el Word maestro en una columna, estilos simples, tablas editables y figuras separables; tratar esto como política interna conservadora, no como requisito KBS confirmado |
| Free-format inicial | `UNVERIFIED` | No se pudo verificar oficialmente que KBS participe en un régimen de `Your Paper Your Way`/free format | Guide KBS inaccesible; la guía `Your Paper Your Way` consultada no es fuente KBS específica | No debe afirmarse que KBS acepta cualquier formato | No usar “free format” como supuesto; mantener formato editorial limpio y reversible |
| Revisión anonimizada | `UNVERIFIED` | El modelo exacto de anonimización no fue verificable en la fuente oficial accesible | Guide KBS inaccesible | Puede afectar únicamente la copia de envío, no el contenido científico | Mantener autores/afiliaciones en el master interno; generar copia anonimizada solo si la guía vigente lo exige |
| Estructura del artículo | `UNVERIFIED` en detalle; `OBSERVED_CONVENTION` para IMRaD | Publicaciones KBS actuales usan secciones científicas convencionales; no se verificó una lista KBS obligatoria de headings | ScienceDirect KBS current research articles | La arquitectura 0D-1 es compatible con research article y no exige reescritura científica | Conservar arquitectura 0D-1; cualquier adaptación futura de headings será formal, no conceptual |
| Abstract | `OBSERVED_CONVENTION` + `UNVERIFIED` para límite | Artículos KBS actuales incluyen abstract no estructurado; límite exacto no pudo verificarse oficialmente | ScienceDirect KBS current research articles | Se redactará al final conforme a D-003; no afecta Methods/Related Work | No fijar todavía número de palabras; revalidar el límite antes de Abstract |
| Keywords | `OBSERVED_CONVENTION` + `UNVERIFIED` para cantidad exacta | Artículos actuales muestran keywords; el número obligatorio no fue verificable en la guía oficial | ScienceDirect KBS current articles | Sin impacto sobre redacción temprana | Seleccionar al final a partir del vocabulario estable; validar cantidad antes de envío |
| Highlights | `PUBLISHER_LEVEL_REQUIREMENT` para formato cuando correspondan; KBS-specific status `UNVERIFIED` | Elsevier define highlights como 3–5 bullets, máximo 85 caracteres, y señala que no se requieren hasta la etapa de final files; no se verificó si KBS los exige específicamente | `https://www.elsevier.com/researcher/author/tools-and-resources/highlights`; KBS current articles muestran highlights | No deben dirigir la redacción de secciones | Prepararlos solo en etapa de submission/final files si KBS los solicita |
| Graphical abstract | `PUBLISHER_LEVEL_REQUIREMENT` para especificaciones si se usa; KBS-specific status `UNVERIFIED` | Elsevier indica que la política es journal-specific y que debe consultarse el Guide for Authors | `https://www.elsevier.com/researcher/author/tools-and-resources/graphical-abstract` | No afecta texto temprano | No producirlo todavía; verificar si KBS lo requiere/permite antes de submission |
| Extensión/páginas | `UNVERIFIED` | No se pudo validar en fuente oficial accesible un máximo actual de páginas o palabras para research article KBS | Guide KBS inaccesible | Riesgo de compresión tardía, pero no impide construir secciones modulares y concisas | Redactar con economía y sin redundancia; revalidar límite antes de cierre de manuscrito |
| Figuras y tablas | `PUBLISHER_LEVEL_REQUIREMENT` | Elsevier exige arte final legible, secuenciado y con captions; especificaciones técnicas generales disponibles | `https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions` | Figuras/tablas deben permanecer editables y cada una responder una pregunta científica | Mantener mapa 0D-1; conservar fuentes editables y captions separados |
| Material suplementario | `PUBLISHER_LEVEL_REQUIREMENT` para manejo; KBS-specific status `UNVERIFIED` | Elsevier admite supplementary content y exige referenciarlo/identificarlo adecuadamente; no se verificó obligación KBS | Elsevier artwork/media and author resources | Puede absorber material de reproducibilidad no esencial al relato principal | Reservar suplemento solo para material científicamente útil que no deba estar en el cuerpo |
| Research Data / Data Availability | `PUBLISHER_LEVEL_REQUIREMENT`/flujo editorial; KBS current `OBSERVED_CONVENTION` | Elsevier ofrece data statement y pide revisar la política del journal; artículos KBS actuales muestran `Data availability` | `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement`; ScienceDirect KBS current articles | La arquitectura ya reserva Data/Code Availability | Mantener una sección candidata y verificar opciones exactas en submission |
| Code Availability | `UNVERIFIED` como sección KBS separada | No se verificó una sección KBS independiente obligatoria; Elsevier trata software/código dentro del ecosistema de research data | Elsevier research data resources | El estudio sí necesita trazabilidad de código, pero no debe inventarse una etiqueta journal-specific | Gestionar conjuntamente con Data/Code Availability y adaptar etiqueta al GFA final |
| Generative AI declaration | `PUBLISHER_LEVEL_REQUIREMENT` | Uso sustantivo de IA en preparación del manuscrito debe declararse; el statement se ubica al final, antes de referencias; herramientas básicas de ortografía/gramática no requieren declaración | `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals` | La IA participa en el flujo de redacción; debe existir log verificable de uso y revisión humana | Abrir registro de uso de IA desde Fase 1; preparar declaración final con nombre de herramienta, finalidad, supervisión y responsabilidad humana |
| IA usada en la investigación | `PUBLISHER_LEVEL_REQUIREMENT` | Cuando IA forma parte de métodos de investigación, su uso debe describirse reproduciblemente en Methods | misma política Elsevier de IA | El LLM local experimental es parte del método; no confundirlo con IA usada para redactar | Methods deberá documentar el LLM experimental según artefactos gobernantes; la declaración editorial cubre la preparación del manuscrito |
| CRediT | `PUBLISHER_LEVEL_REQUIREMENT` | Elsevier solicita statement CRediT durante submission; el corresponding author asegura exactitud y acuerdo | `https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement` | No afecta cuerpo científico | Preparar al final con contribuciones reales y aprobación de autores |
| Funding | `PUBLISHER_LEVEL_REQUIREMENT` | Deben declararse fuentes de financiamiento y, cuando aplique, rol del financiador | Elsevier Publishing Ethics | Sin impacto en estructura científica | Mantener ledger de funding; completar declaración al final |
| Competing interests | `PUBLISHER_LEVEL_REQUIREMENT` | Los autores deben revelar relaciones financieras/personales capaces de influir el trabajo | `https://www.elsevier.com/about/policies-and-standards/publishing-ethics` | Sin impacto en argumentos científicos | Preparar declaración al final; no inferir “none” hasta confirmación de los autores |
| Submission checklist KBS | `UNVERIFIED` | No se pudo inspeccionar la checklist KBS específica en el Guide for Authors oficial | Guide KBS inaccesible | Puede exigir archivos auxiliares, pero no cambia el núcleo científico | Verificación obligatoria inmediatamente antes de submission |
| Referencias: estilo final KBS | `UNVERIFIED` como requisito textual del GFA | El estilo exacto de presentación no pudo verificarse directamente en el GFA oficial accesible; publicaciones actuales muestran referencias producidas por el journal, pero eso se registra solo como convención observada | ScienceDirect current KBS publications; Guide KBS inaccesible | No debe paralizar el borrador porque el autor decidió APA 7 provisional y conversión final con Mendeley | Mantener APA 7 provisional en Word sin campos Mendeley; confirmar estilo KBS y convertir únicamente al final |
| Idioma | `RECOMMENDATION`/política interna | El artículo se redactará en inglés académico consistente. No se atribuye a KBS una variante específica no verificada | gobernanza del proyecto + recursos Elsevier de escritura | Evita reescritura y mezcla de variantes | Adoptar inglés estadounidense como convención interna y aplicarlo consistentemente |

#### B.2 Estado de plantilla

```text
KBS_TEMPLATE_STATUS = UNVERIFIED
```

La fuente oficial confirma la existencia del `Guide for Authors`, pero el contenido específico relativo a plantilla/formatting no fue accesible en esta ejecución. Existe una plantilla LaTeX oficial de Elsevier a nivel publisher, pero no se la presenta como plantilla KBS obligatoria. No se reconstruye una supuesta plantilla KBS a partir de papers publicados ni de sitios de terceros.

Este `UNVERIFIED` se clasifica como `UNVERIFIED_NONBLOCKING` para la **redacción científica inicial** porque el workflow adopta un master Word neutral, editable, de una columna y con estilos simples; cualquier migración posterior a una plantilla de envío sería mecánica y no altera la estructura científica ni los claims. Sí se convierte en condición obligatoria antes de generar el paquete final de submission.

#### B.3 Estado del tipo de artículo

```text
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
```

La decisión se sustenta en el scope oficial de KBS, que solicita investigación original, y en el etiquetado primario actual de ScienceDirect (`Research article`/`Research Articles`). La etiqueta exacta disponible en el sistema de submission deberá revalidarse antes del envío, pero no hay ambigüedad material sobre la clase científica del manuscrito que debe construirse.

#### B.4 Estado de referencias

```text
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
```

No se atribuye un estilo final exacto a KBS sin acceso directo al texto vigente de su Guide for Authors. Para evitar reformatting repetido, el Word utilizará **APA 7 provisional en texto plano** durante la redacción. El autor aplicará Mendeley al final y convertirá las referencias al estilo KBS oficial una vez verificado. Esta incertidumbre es `UNVERIFIED_NONBLOCKING`: afecta formato final, no contenido ni orden científico del artículo.

---

### C. Reconciliación de la arquitectura 0D-1 con KBS

No existe evidencia oficial accesible que obligue a cambiar la lógica IMRaD aprobada en 0D-1. En consecuencia, se conserva la arquitectura y solo se normaliza su función editorial frente al target.

| bloque 0D-1 | acción 0D-2 | arquitectura candidata para redacción | razón | dependencia |
|---|---|---|---|---|
| Introduction 1.1–1.3 | `KEEP` | Problema/alcance → limitación de prior art → contribución provisional/RQs | Compatible con research article y con progresión exigida por STYLE_GUIDE; se redactará tarde | Results parciales + Related Work |
| Related Work 2.1–2.4 | `KEEP` | HS/candidate retrieval → RAG/regulatory reasoning → explainability/auditability → validity/provenance | Organiza por tarea, no por autores, y sustenta framing KBS | 0B frozen |
| Related Work 2.5 | `KEEP` | Síntesis de posicionamiento | Necesaria para presentar el contrato completo sin novelty automática | final gap/novelty no declarados |
| Methods 3.1–3.6 | `KEEP` | Diseño/unidades → datos → split → histórico → normativa → integración/invariancia | Constituye el núcleo del contrato arquitectónico-metodológico | evidencia congelada |
| Methods 3.7–3.9 | `KEEP` | LLM controlado → evaluación function-specific → validez/drift/reproducibilidad | KBS fit exige hacer visibles interfaces, conocimiento, evaluación y límites | HE4/Grupo 2/C21–C25 |
| Results 4.1–4.5 | `KEEP` | split → RQ1 → RQ2 → RQ3 → sensibilidades | Separa resultados por función y evita una única “accuracy del sistema” | claims autorizados/condicionales |
| Results 4.6 | `DEFER` | cierre inferencial RQ4 | No puede redactarse antes de Grupo 3 | Grupo 3 |
| Results 4.7 | `DEFER` | EXP-11B solo si se autoriza editorialmente | No puede usarse mientras C10/C11 sigan bloqueados | reconciliación C10/C11 |
| Discussion 5.1–5.4 | `DEFER` | significado del contrato → prior art → decision support → validez/transferibilidad | Requiere Results finales; no debe anticiparse | Grupo 3/Results finales |
| Limitations 6.1–6.4 | `KEEP` | benchmark/datos → HE4 → drift → reproducibilidad/external validity | Las limitaciones son parte central del control de overclaiming | ajuste final tras Grupo 3 |
| Conclusions | `DEFER` | respuesta final a RQs bajo alcance | Evitar conclusiones prematuras | Results/Discussion finales |
| Data/Code Availability | `KEEP` | disponibilidad, repositorios, restricciones y provenance | Compatible con política Elsevier de research data y con C17 | snapshot final |
| Declarations | `KEEP` / late stage | funding, competing interests, CRediT, AI declaration | Publisher-level requirements/operational submission package | target final + autores |

```text
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
```

La condición operacional es verificar, antes del envío, si el Guide for Authors vigente exige nombres, orden o archivos separados específicos. Ningún cambio de headings permitido en ese gate podrá alterar el contrato científico, las RQs, los límites de claims ni la separación Methods/Results/Discussion.

---

### D. Política de referencias y citas durante la redacción

#### D.1 Regla operacional congelable

1. La versión de trabajo en Word usa **APA 7 provisional**, en texto plano.
2. No se insertan campos Mendeley, Zotero, EndNote ni códigos de campo de otro gestor durante la redacción por bloques.
3. El `.md` mantiene las citas visibles de forma coherente con el Word provisional y una bibliografía verificable; no contiene referencias inventadas ni metadatos inferidos.
4. Cada fuente debe existir en el corpus/registro autorizado o ser incorporada por un gate explícito; 0D-2 no reabre 0B.
5. El autor realizará al final la vinculación/gestión con Mendeley y la conversión al estilo oficial KBS que se verifique entonces.
6. La conversión de estilo bibliográfico no puede cambiar qué fuente soporta qué claim.
7. Si una referencia carece de DOI, páginas, article number u otro metadato, se conserva únicamente lo comprobado; no se rellena por conjetura.
8. Una referencia citada varias veces conserva el mismo registro bibliográfico, pero cada **instancia de uso** en Word recibe su propio comentario de auditoría si respalda un claim distinto.

#### D.2 Control previo a conversión final

Antes de aplicar Mendeley al master final deberá existir una tabla de conciliación `citation_instance → source_id → claim supported → verified metadata`. La conversión bibliográfica será un cambio de formato, no una etapa de descubrimiento bibliográfico.

---

### E. Política de escritura científica para Fase 1 y posteriores

```text
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
```

| dimensión | regla de escritura |
|---|---|
| Idioma maestro | Inglés. La versión inglesa es la versión de manuscrito destinada a submission; la versión española se conserva como control semántico según D-002/D-010 |
| Variante interna | Inglés estadounidense, elegido como convención de consistencia del proyecto; no se presenta como requisito KBS específico |
| Registro | Técnico, sobrio, internacional, verificable y no promocional |
| Voz | Preferir construcción activa cuando el actor sea científicamente relevante; usar pasiva cuando el procedimiento/objeto sea el foco. Evitar una pasiva mecánica sistemática |
| Tiempo verbal — Methods | Pasado para acciones ejecutadas; presente para propiedades permanentes del diseño/artefactos cuando corresponda |
| Tiempo verbal — Results | Pasado para observaciones obtenidas; presente solo para tablas/figuras o relaciones que el texto señala explícitamente |
| Tiempo verbal — Related Work | Presente para lo que un trabajo establece como contenido vigente; pasado para procedimientos/resultados específicos cuando sea más preciso |
| Tiempo verbal — Discussion | Presente para interpretación del artículo; pasado al referirse a observaciones experimentales concretas |
| Futuro | Solo para trabajo futuro real o bloques todavía no ejecutados; nunca para presentar resultados pendientes como hechos |
| Oraciones | Una relación científica principal por oración. Objetivo interno habitual: 20–30 palabras; revisar oraciones >40 palabras salvo necesidad técnica |
| Párrafos | Una función argumental por párrafo; normalmente 3–6 oraciones; no usar párrafos de una sola frase salvo transición excepcional |
| Terminología | Mantener exactamente `historical retrieval`, `historical ranking`, `fixed Top-3`, `normative retrieval`, `normative evidence`, `controlled explanation`, `local LLM`, `auditable recommendation`, `NANDINA subheading`, `series record`, `DAM/customs declaration` |
| Abreviaturas | Definir en primera aparición; no crear abreviaturas para términos usados pocas veces; conservar las ya establecidas y necesarias |
| Números | Usar cifras para métricas, tamaños, porcentajes y unidades; preservar denominador cuando sea científicamente informativo |
| Porcentajes | Primera mención de resultado crítico: numerador/denominador + porcentaje cuando esté autorizado; no convertir aproximaciones en valores exactos |
| Precisión | No aumentar decimales respecto de la fuente ni cambiar redondeo entre texto, tabla y figura. El valor canónico gobierna; una forma redondeada debe ser explícitamente consistente |
| Unidades | SI cuando aplique; espacio entre valor y unidad según convención científica, salvo símbolos como `%` |
| Lenguaje absoluto | Prohibido salvo soporte universal explícito. Preferir `under the evaluated conditions`, `within the fixed evaluation set`, `in the executed protocol` |
| Adjetivos promocionales | Evitar `robust`, `superior`, `effective`, `innovative`, `accurate`, `reliable`, `state-of-the-art` salvo evidencia y comparación que lo autoricen |
| Antropomorfismo | Evitar “the model understands/knows/decides” si solo recupera, rankea o genera; nombrar la operación observable |
| Diseño vs resultado | Una propiedad arquitectónica no puede redactarse como resultado empírico; un resultado no puede presentarse como propiedad universal del diseño |
| Causalidad | No usar `cause`, `effect`, `impact` causal o equivalentes si el diseño no identifica causalidad. EXP-11A y sensibilidades permanecen no causales dentro de sus límites |
| Ranking vs accuracy | Candidate retrieval Top-k/MRR no se denomina `overall classification/system/RAG accuracy` |
| Evidencia vs correctness | `association`, `coverage`, `traceability` y `source support` no equivalen a normative/legal correctness |
| Arquitectura vs novelty | Diferencia arquitectónica no equivale a novelty. La contribución B sigue siendo posicionamiento provisional |
| Configurabilidad vs generalización | Configurar para otros capítulos/jurisdicciones no prueba desempeño fuera de Clase 87 |
| Inferencia editorial | Debe marcarse como interpretación/inferencia y no atribuirse al experimento o a la literatura como hallazgo observado |

---

### F. Protocolo claim–evidence y control anti-error

```text
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
```

#### F.1 Reglas obligatorias

- Toda cifra debe tener fuente identificable: artefacto, tabla, archivo, claim autorizado o publicación primaria.
- Ninguna referencia, DOI, volumen, número de artículo, fecha, autor o metadato puede inventarse, autocompletarse por patrón o recuperarse solo desde memoria.
- Un claim bibliográfico debe estar respaldado por el texto comprobado de la fuente; un título, snippet de buscador o abstract incompleto no basta para un claim más amplio.
- Una fuente no puede citarse para una afirmación más fuerte que la que su contenido demuestra.
- Las inferencias editoriales deben etiquetarse como inferencias y no mezclarse con resultados experimentales o hallazgos de literatura.
- Los estados `CONDITIONAL`, `REVIEW_REQUIRED` y `PROHIBITED` de `CLAIM_EVIDENCE_MATRIX.md` son vinculantes.
- C10/C11 no pueden usarse hasta reconciliación editorial explícita.
- RQ4 y el cierre HE2/HE5 permanecen pendientes de Grupo 3.
- C14 solo puede usarse con limitaciones HE4; C12/C13/C18 permanecen prohibidos.
- C21–C25 deben preservar el resultado dependiente del método de 0B-05C; está prohibido reducirlo a “sin impacto”.
- Los resultados de candidate retrieval, evidence retrieval, integración/invariancia y explicación/auditabilidad deben permanecer separados por función.
- La ausencia de prior art dentro del alcance de búsqueda no puede convertirse en inexistencia universal.

#### F.2 Checklist obligatorio antes de cada entrega de la IA de Redacción

| control | PASS requerido |
|---|---|
| Scope | El bloque corresponde exactamente al prompt cerrado y no abre fases/bloques no autorizados |
| Fuente de verdad | Se consultó el artefacto gobernante más reciente aplicable y no se sustituyó con memoria |
| Números | Cada cifra se trazó a fuente; denominador, unidad, signo y precisión coinciden |
| Claims | Cada claim está `AUTHORIZED` o explícitamente dentro de un uso `CONDITIONAL` permitido |
| Claims prohibidos | No aparecen C09, C12, C13, C16, C18 ni cualquier claim experimental/editorial aún bloqueado |
| C10/C11 | No se usan H150/H200 como claim antes de reconciliación |
| Grupo 3 | No se anticipan RQ4/HE2/HE5 finales |
| Literatura | Cada cita fue comprobada contra fuente suficiente, no solo snippet/metadata |
| DOI/metadata | Coinciden con fuente primaria o registro verificado |
| Métrica | Top-k/MRR se nombran por su función real; no `system accuracy` |
| Normativa | Evidencia/coverage/traceability no se convierte en legal correctness |
| Causalidad | No se introduce lenguaje causal sin diseño causal |
| Generalización | No se extrapola empíricamente fuera de Clase 87 |
| Novelty | No se usan `first`, `novel`, `unprecedented`, `no prior work` sin autorización posterior |
| ES/EN | Las versiones internas obligatorias mantienen misma fuerza, cifra, límite y condición |
| Citaciones Word | Cada instancia de cita nueva tiene comentario de auditoría completo |
| Integridad del master | El candidato parte del último master aprobado; no se reconstruye desde cero |
| Versionado | Solo se modificó el bloque autorizado y se generaron versiones candidatas nuevas sin sobrescribir historia aprobada |

Un solo fallo material de estos controles obliga a detener la entrega del bloque hasta corregirlo.

---

### G. Workflow acumulativo `.md` + `.docx`

```text
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
```

#### G.1 Principio de autoridad

La **IA de Redacción** es responsable de generar y actualizar los artefactos de manuscrito. La IA Gestora audita y administra gates; la IA Experimental revisa consistencia experimental cuando corresponda; el autor aprueba. Ninguno sustituye a la IA de Redacción como propietaria de la generación del manuscrito.

#### G.2 Entregables de cada bloque

Cada entrega de redacción debe producir simultáneamente:

1. un `.md` del bloque trabajado;
2. un `.md` maestro acumulativo candidato;
3. un `.docx` maestro acumulativo candidato.

Los tres deben derivar del mismo contenido científico. El `.docx` se actualiza sobre la **última versión acumulativa aprobada**, preservando estilos, tablas, figuras, comentarios y material ya aprobado. No se reconstruye desde cero, salvo la creación inicial autorizada del master a partir del formato adoptado.

#### G.3 Bilingüismo y función de cada formato

Para cumplir D-002 sin contaminar el futuro paquete de submission:

- el `.md` de bloque y el `.md` master contienen `## Español` como control semántico y `## English` como texto científico equivalente;
- el `.docx` interno acumulativo conserva dos partes claramente separadas: **Part I — English manuscript master** y **Part II — Spanish semantic-control mirror**;
- los comentarios de auditoría de citas se anclan en la Part I inglesa;
- la Part II no forma parte del futuro archivo de submission y solo podrá retirarse mediante un gate explícito cuando se genere el paquete final para el journal;
- retirar la parte española en el paquete de submission es una transformación editorial controlada, no una reescritura científica.

#### G.4 Versionado propuesto

Convención recomendada:

```text
article/sections/P01_METHODS_B01_V01.md
article/manuscript/ARTICLE_MASTER_CANDIDATE_V001.md
article/manuscript/ARTICLE_MASTER_CANDIDATE_V001.docx
```

Tras auditoría y aprobación:

```text
article/manuscript/ARTICLE_MASTER_APPROVED_V001.md
article/manuscript/ARTICLE_MASTER_APPROVED_V001.docx
```

El siguiente bloque parte exclusivamente de `ARTICLE_MASTER_APPROVED_V001` y genera `ARTICLE_MASTER_CANDIDATE_V002`. Una corrección de un mismo candidato usa `V002`, `V003`, etc., según el prompt autorizado; nunca sobrescribe un binario aprobado.

Reglas:

- `CANDIDATE` = entregable no canónico pendiente de auditoría/aprobación;
- `APPROVED` = estado aceptado por los gates correspondientes;
- solo un par `.md/.docx` `APPROVED` puede ser baseline de la siguiente entrega;
- el número del master aumenta por integración aprobada, no por simples intentos descartados;
- el nombre del bloque conserva fase, sección y bloque para trazabilidad;
- los hashes del `.docx` aprobado deben registrarse cuando un prompt posterior lo requiera como entrada inmutable.

#### G.5 Correcciones V02/V03

Una revisión correctiva:

- parte del candidato/approved especificado por el prompt;
- conserva material aprobado fuera del alcance;
- cambia únicamente observaciones autorizadas;
- genera nuevo `.md` de bloque si el bloque cambia y nuevo master candidato `.md/.docx`;
- nunca “limpia” silenciosamente otras secciones;
- documenta en el registro de respuesta qué cambió y por qué.

#### G.6 Estado final del proyecto editorial

El producto final conservará:

```text
1 master canónico .md
1 master canónico .docx
historial versionado de bloques y masters candidatos/aprobados
registro de fuentes/claims/citas
artefactos de figuras/tablas y sus fuentes editables
```

El Word final de submission se deriva del master aprobado; no se vuelve a escribir desde archivos parciales.

---

### H. Protocolo de comentarios de auditoría de citas en Word

```text
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
```

Cada **instancia de cita** de la Part I inglesa debe tener un comentario Word anclado exactamente al texto de la cita. El comentario obligatorio es:

```text
FUENTE / REVISTA:
AUTOR(ES):
AFIRMACIÓN ORIGINAL / EXTRACTO TEXTUAL EXACTO Y SUFICIENTE:
TRADUCCIÓN AL ESPAÑOL:
JUSTIFICACIÓN DE RESPALDO:
LÍMITE DE LA CITA / QUÉ NO DEMUESTRA: [cuando sea pertinente]
```

Reglas operativas:

1. El extracto conserva el idioma original de la fuente y debe ser el fragmento mínimo suficiente para demostrar el claim asociado.
2. La traducción española debe ser fiel y no aumentar fuerza, alcance o causalidad.
3. `JUSTIFICACIÓN DE RESPALDO` explica la relación exacta entre fuente y oración del manuscrito; no introduce un argumento nuevo.
4. `LÍMITE DE LA CITA` es obligatorio cuando exista riesgo de overclaiming, diferencia de tarea/dataset, inferencia no causal, falta de generalización, source support sin correctness o cualquier otra frontera pertinente.
5. Una misma referencia usada para claims distintos recibe comentarios distintos en cada instancia.
6. Una cita agrupada debe permitir identificar el respaldo individual de cada obra. Preferencia: anclar comentario al token de cada referencia dentro del grupo; si técnicamente no es posible, un comentario sobre el grupo repite el bloque anterior por cada fuente.
7. El comentario no puede “reparar” una cita insuficiente. Si la fuente no soporta el claim, se cambia el claim o se elimina/reemplaza la cita mediante el gate bibliográfico correspondiente.
8. Snippets de buscador, páginas de índices y metadatos no sustituyen el texto de la fuente para claims científicos.
9. Para claims experimentales propios no se finge una cita bibliográfica; la trazabilidad se dirige al artefacto/claim interno correspondiente.
10. Los comentarios permanecen en masters internos; su eliminación para submission solo ocurre después de una auditoría final que confirme que la matriz citation–claim–source quedó preservada.

---

### I. Estrategia editorial para maximizar aceptación en KBS sin overclaiming

#### I.1 Centro del paper

El centro editorial debe ser el **contrato arquitectónico-metodológico completo evaluado**, no la aduana peruana por sí sola ni la suma de BM25 + LLM. La narrativa debe hacer explícitos: interfaces entre capas; prohibiciones de modificación del ranking; invariantes; función diferenciada de cada fuente de conocimiento; partición consciente de DAM; métricas separadas por función; provenance y reproducibilidad.

#### I.2 Lo que el paper no debe parecer

- una aplicación local de RAG a aduanas sin contribución metodológica;
- un paper de clasificación LLM donde el LLM decide el código;
- una comparación genérica BM25 versus dense retrieval;
- una validación jurídica de clasificaciones NANDINA;
- un paper cuya contribución sea “auditabilidad” como ausencia general de prior art;
- una tesis comprimida con muchos experimentos sin hilo científico central;
- una colección de métricas heterogéneas tratadas como una única accuracy del sistema.

#### I.3 Principales riesgos de desk rejection y mitigación

| riesgo | nivel | mitigación pre-redacción |
|---|---|---|
| Integración percibida como incremental | HIGH | Formalizar contrato, interfaces, invariantes y prohibiciones; vincular cada RQ con una función evaluada |
| Aplicación demasiado local | MEDIUM-HIGH | Presentar Clase 87 como caso experimental acotado y exigente; extraer lecciones de diseño sin afirmar generalización empírica |
| Novelty insuficientemente defendida | HIGH | Mantener novelty no declarada; Related Work debe mostrar diferencias estrechas y prior art parcial sin “first” |
| HE4 débil como validación de explicación | HIGH | Presentar N=50, evaluador IA, mismatch y modalidad; usar HE4 solo para estructura/trazabilidad bajo protocolo |
| Metric conflation | HIGH | Tabla explícita `componente → tarea → métrica → interpretación permitida/prohibida` |
| Validez interna cuestionada | MEDIUM | Mostrar DAM-disjoint split, dependencia intra-DAM, near-duplicates y concentración como dimensiones separadas |
| Drift normativo | MEDIUM | Exponer 0B-05C como sensibilidad documentada y dependiente del método, no como “sin efecto” ni legal correction |
| Reproducibilidad sobreafirmada | MEDIUM | Declarar limitaciones no bloqueantes y assets no recuperables/local-only; provenance ≠ perfect reproducibility |
| Resultados negativos/limitados ocultos | HIGH | Incorporarlos de forma explícita como evidencia de límites del contrato y del alcance; no maquillarlos |

#### I.4 Framing de Clase 87

Clase/Capítulo 87 debe presentarse como **alcance experimental delimitado** y caso de evaluación del contrato, no como muestra representativa de todas las clases, países o jurisdicciones. La posibilidad de configurar el framework para otros dominios es una propiedad de diseño; cualquier transferencia empírica queda fuera de lo demostrado.

#### I.5 Tratamiento de HE4

HE4 no se usa para afirmar corrección jurídica, fidelidad normativa completa ni calidad humana equivalente. Su función editorial es mostrar qué tan consistentemente el generador restringido conserva el Top-3 y produce estructura/trazabilidad bajo el protocolo ejecutado, junto con sus limitaciones.

#### I.6 Resultados negativos y limitaciones

Los resultados diagnósticos o limitados no deben ocultarse. El reranker de 20 casos, el drift normativo, las limitaciones HE4, near-duplicates, concentración y reproducibilidad parcial sirven para delimitar qué demuestra y qué no demuestra el sistema. Esa transparencia es coherente con KBS si se integra a la evaluación del contrato y no se convierte en una narrativa defensiva.

#### I.7 Título, Abstract e Introduction futuros

Cuando sus gates se abran, deben:

- contener el objeto científico central y el alcance experimental;
- distinguir ranking histórico, evidencia normativa y explicación controlada;
- formular resultados solo cuando estén congelados;
- evitar `first`, `novel`, `unprecedented`, `robust`, `legally correct`, `generalizable` y equivalentes no autorizados;
- evitar vender NANDINA como único aporte;
- evitar llamar al Top-3 “accuracy global”;
- no formular novelty final mientras `NOVELTY = NOT_DECLARED`.

No se redacta ninguna de esas secciones en 0D-2.

---

### J. Estrategia de cascade A/B/C

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
```

| dimensión | KBS (A) | ESWA (B) | IPM (C) | núcleo común | cambio requerido al migrar | riesgo de reescritura |
|---|---|---|---|---|---|---|
| Contribución central | contrato knowledge-based arquitectónico-metodológico | intelligent/expert system aplicado con restricción arquitectónica verificable | architecture de information retrieval/evidence/provenance | contrato B, RQs y límites | reponderar framing, no cambiar evidencia | MEDIUM |
| Dominio | caso regulatorio/aditivo de conocimiento | aplicación experta en government/law/auditing/IR | critical information-processing application | Clase 87 como alcance acotado | cambiar motivación y vocabulario editorial | LOW-MEDIUM |
| Methods | interfaces, fuentes de conocimiento, invariancia, evaluación por función | diseño/testing/implementación del intelligent system | retrieval, evidence flow, provenance y system design | 3.1–3.9 y datos | reordenación menor de énfasis | LOW |
| Results | RQ1–RQ4 por función | desempeño del sistema aplicado con métricas separadas | retrieval/evidence metrics como centro, explicación como apoyo | tablas/resultados gobernados | selección/orden de tablas | LOW |
| Related Work | KBS/RAG/knowledge systems | expert systems/applied AI | IR/information processing/evidence | corpus 0B frozen | reponderar familias ya revisadas; no nueva novelty search automática | MEDIUM |
| Discussion | significado del contrato | valor y límites como intelligent application | implicaciones para IR/evidence architecture | mismos resultados/limitaciones | reescribir énfasis interpretativo | MEDIUM |
| HE4 | evidencia limitada complementaria | componente de explainability/auditability del sistema | componente downstream, secundario frente a IR | mismo protocolo y límites | solo énfasis | LOW |
| Reproducibilidad | provenance + knowledge-system traceability | reproducible applied system | data/evidence/provenance discipline | mismos repos/artefactos | principalmente terminología | LOW |
| Novelty risk | MEDIUM-HIGH | HIGH por énfasis de ESWA en genuine innovation | MEDIUM-HIGH si no hay aporte claro a information science | novelty sigue no declarada | reevaluar framing tras razón de rechazo | MEDIUM |
| Formato/ref style | KBS exacto a revalidar | GFA ESWA a revalidar al activar B | GFA IPM a revalidar al activar C | master editable + Mendeley al final | conversión formal | LOW |
| Submission package | KBS-specific final files | ESWA-specific final files | IPM-specific final files | data/code/AI/CRediT/funding/COI ledgers | checklists y metadatos | LOW |

#### J.1 Regla de transferencia después de rechazo

El cascade no es automático por jerarquía. La **razón de rechazo** gobierna la migración:

- rechazo KBS por scope/énfasis knowledge-based insuficiente: evaluar ESWA si el carácter de intelligent/expert application es más claro;
- rechazo KBS porque el artículo se percibe principalmente como IR/evidence architecture: priorizar IPM;
- rechazo KBS por novelty/incrementalidad: **no** transferir automáticamente a ESWA, cuyo riesgo de innovation/repackaging es al menos tan relevante; activar revisión editorial del framing y del motivo de rechazo antes de decidir B/C;
- rechazo por problemas científicos, validez o evidencia: corregir el problema antes de cualquier resubmission; no maquillarlo mediante cambio de journal.

```text
JOURNAL_CASCADE_STATUS = CLOSED_FOR_DRAFTING
```

La estrategia minimiza reescritura porque Methods, Results, datos, claims y artefactos permanecen invariantes; la mayor parte de la migración debe concentrarse en Title/Abstract/Introduction, síntesis de Related Work, Discussion, cover letter y requisitos formales.

---

### K. Matriz de decisiones pre-redacción

| decisión | estado | fundamento | condición restante |
|---|---|---|---|
| Target A/B/C | `CLOSED_FOR_DRAFTING` | 0D V02 + review PASS + verificación actual de scope | selección final requiere auditoría/autor |
| Tipo científico KBS | `CLOSED_FOR_DRAFTING` | scope oficial + artículos 2026 `Research article` | revalidar etiqueta de submission |
| Plantilla KBS específica | `UNVERIFIED_NONBLOCKING` | Guide oficial enlazado pero cuerpo inaccesible | verificar antes de submission; no reconstruir |
| Formato de trabajo inicial | `CLOSED_WITH_OPERATIONAL_CONDITION` | master Word neutral/editable y markdown acumulativo evitan dependencia de plantilla | aplicar plantilla final solo tras verificación |
| Arquitectura del artículo | `CLOSED_WITH_OPERATIONAL_CONDITION` | 0D-1 aceptada y compatible con research article | nombres/orden formal sujetos a GFA final |
| Abstract/keywords exactos | `DEFERRED_WITHOUT_REWRITE_RISK` | se redactan al final; límites KBS específicos no verificados | verificar antes de redactarlos |
| Highlights | `DEFERRED_WITHOUT_REWRITE_RISK` | publisher define formato; KBS-specific requirement no confirmado | preparar en final-files si aplica |
| Graphical abstract | `UNVERIFIED_NONBLOCKING` | publisher remite al GFA específico | verificar antes de submission |
| Límite exacto de extensión | `UNVERIFIED_NONBLOCKING` | GFA KBS no accesible | mantener redacción compacta y verificar antes del cierre final |
| Peer-review anonymization | `UNVERIFIED_NONBLOCKING` | no verificado en fuente accesible | generar copia de envío según GFA |
| Estilo final de referencias KBS | `UNVERIFIED_NONBLOCKING` | GFA específico no accesible | APA7 provisional; conversión final con Mendeley |
| Política de referencias de trabajo | `CLOSED_FOR_DRAFTING` | decisión expresa del autor | ninguna |
| Writing policy | `CLOSED_FOR_DRAFTING` | STYLE_GUIDE + 0D2 | ninguna |
| Claim–evidence protocol | `CLOSED_FOR_DRAFTING` | Claim Matrix y freezes | actualización solo por gate formal |
| Workflow `.md/.docx` | `CLOSED_FOR_DRAFTING` | regla acumulativa definida | aprobación editorial/autor para canonizar cada master |
| Comentarios de cita Word | `CLOSED_FOR_DRAFTING` | esquema y reglas definidos | implementación técnica en cada DOCX |
| AI-use governance | `CLOSED_FOR_DRAFTING` | política Elsevier vigente | registrar usos desde Fase 1 y declarar al submission |
| Data/Code governance | `CLOSED_WITH_OPERATIONAL_CONDITION` | proyecto ya tiene trazabilidad + política publisher | verificar redacción exacta y snapshot final |
| CRediT/funding/COI | `DEFERRED_WITHOUT_REWRITE_RISK` | publisher requirements | datos reales de autores al cierre |
| C10/C11 | `DEFERRED_WITHOUT_REWRITE_RISK` para bloques no dependientes; bloqueante para EXP-11B | gobernanza editorial vigente | reconciliación antes de cualquier uso EXP-11B |
| Grupo 3 | `DEFERRED_WITHOUT_REWRITE_RISK` para Methods/RW; bloqueante para final RQ4/HE2/HE5 | estado experimental vigente | cierre Grupo 3 |

No existe ningún `UNVERIFIED_BLOCKING` para comenzar **los bloques ya declarados redactables** de Methods/Related Work/Results congelados una vez que la IA Gestora y el autor cierren 0D/Fase 0. Los elementos `UNVERIFIED_NONBLOCKING` se concentran en formalidades específicas de submission cuya aplicación posterior es mecánica y no autoriza alterar contenido científico.

---

### L. Recomendación de gate pre-redacción

```text
PRE_DRAFTING_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
```

**Fundamento:** ya están cerradas las decisiones que podrían producir reescritura científica temprana: tipo de paper, target/cascade, arquitectura científica, política de escritura, protocolo claim–evidence, gobernanza de referencias durante drafting, workflow acumulativo y comentarios de auditoría de citas. No existe un `UNVERIFIED_BLOCKING` para los primeros bloques redactables.

El calificativo `WITH_CORRECTIONS` conserva como condiciones operativas antes del **submission**, no antes del primer borrador de Methods:

1. verificar directamente el Guide for Authors vigente de KBS cuando el acceso sea posible;
2. confirmar si existe plantilla Word/LaTeX journal-specific y su obligatoriedad;
3. confirmar el estilo final de referencias, límite de extensión, abstract/keywords, anonymization, graphical abstract, highlights y checklist exacta;
4. transformar el master interno al paquete KBS solo después del freeze científico aplicable;
5. no abrir los bloques dependientes de C10/C11 o Grupo 3 hasta sus gates respectivos.

Esta recomendación **no abre Fase 1**. La apertura corresponde a la IA Gestora y al autor después de auditar y, cuando proceda, congelar 0D/Fase 0.

```text
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

0D-2 no introduce resultados ni interpretación experimental nueva; organiza requisitos editoriales y gobernanza de escritura sobre evidencia ya gobernada.

---

### M. Trazabilidad web y documental

**Corte editorial:** `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`, commit `346d7b86bae279b38c377845fe332fce802d12f3`.

**Fecha de verificación web:** `2026-09-15`.

**Fuentes oficiales principales:**

- KBS official Elsevier journal page: `https://shop.elsevier.com/journals/knowledge-based-systems/0950-7051`
- KBS ScienceDirect journal/issues/articles: `https://www.sciencedirect.com/journal/knowledge-based-systems`
- KBS Guide for Authors link: `https://www.sciencedirect.com/journal/knowledge-based-systems/publish/guide-for-authors` — identificado como fuente oficial, cuerpo no accesible en esta ejecución (`403`)
- Elsevier LaTeX instructions: `https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions`
- Elsevier AI policy: `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals`
- Elsevier Research Data / Data Statement: `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement`
- Elsevier CRediT: `https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement`
- Elsevier Publishing Ethics / competing interests / funding: `https://www.elsevier.com/about/policies-and-standards/publishing-ethics`
- Elsevier Highlights: `https://www.elsevier.com/researcher/author/tools-and-resources/highlights`
- Elsevier Graphical Abstract: `https://www.elsevier.com/researcher/author/tools-and-resources/graphical-abstract`
- Elsevier Artwork/Media: `https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions`
- ESWA official page: `https://shop.elsevier.com/journals/expert-systems-with-applications/0957-4174`
- IPM official page: `https://shop.elsevier.com/journals/information-processing-and-management/0306-4573`

**Uso de publicaciones KBS actuales:** solo como `OBSERVED_CONVENTION` para confirmar que KBS publica actualmente `Research article`, abstracts/keywords/highlights y secciones de data availability/CRediT en artículos recientes. No se infiere de ellas un requisito del Guide for Authors.

**Fuentes de terceros:** resultados que reproducían o resumían el Guide for Authors se excluyeron como autoridad normativa. No se usaron para cerrar requisitos que la fuente oficial accesible no permitió verificar.

```text
0D2_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
KBS_TEMPLATE_STATUS = UNVERIFIED
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
JOURNAL_CASCADE_STATUS = CLOSED_FOR_DRAFTING
PRE_DRAFTING_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
PHASE_1 = NOT_OPENED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

---

## English

### A. Entry state and verification standard

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D-1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
0D2_ENTRY_GATE = PASS / OPENED
0D-2 = READY_FOR_DRAFTING
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
TARGET_JOURNAL = PENDING_0D2_AND_AUTHOR_APPROVAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = DEFERRED_UNTIL_0D2_REVIEW
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_0D2_ENTRY
```

**FILES READ:** `article/START_HERE.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/reviews/0D2_ENTRY_GATE.md`; `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`; `article/reviews/0D_V02_INTERNAL_REVIEW.md`; `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/0B_PHASE_CLOSURE.md`.

**ACTIVE PHASE:** `0D-2 — Journal requirements, writing governance, and submission strategy`.

**MANUSCRIPT DRAFTING AUTHORIZED:** no. This artifact defines pre-drafting governance and contains no manuscript prose.

**PRESERVED SCIENTIFIC STATE:**

```text
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The frozen functional contract remains unchanged:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

The 0D-2 web verification was performed on `2026-09-15` solely for editorial requirements, formatting, and journal strategy. Official Elsevier/ScienceDirect pages and current papers in the journals were prioritized. The official KBS page confirms and links the `Guide for Authors`, but the guide body returned `403 Forbidden` in the available environment. Therefore, no information available only through third-party reproductions was promoted to an official requirement. Any journal-specific rule that could not be confirmed through an accessible official source is marked `UNVERIFIED`, and its blocking effect is assessed separately.

The classification vocabulary is:

```text
JOURNAL_SPECIFIC_REQUIREMENT
PUBLISHER_LEVEL_REQUIREMENT
RECOMMENDATION
OBSERVED_CONVENTION
UNVERIFIED
```

---

### B. Current Knowledge-Based Systems requirements

#### B.1 Requirements matrix

| element | official status | exact verifiable requirement/status | official source | drafting impact | pre-Phase-1 action |
|---|---|---|---|---|---|
| Scope | `JOURNAL_SPECIFIC_REQUIREMENT` | KBS publishes original research on knowledge-based and other AI-technique systems, including knowledge engineering and intelligent decision support | Elsevier KBS journal page: `https://shop.elsevier.com/journals/knowledge-based-systems/0950-7051` | The paper must center the evaluated architectural-methodological contract rather than a customs-only application | Preserve frozen Alternative-B framing and functional separation |
| Article type | `JOURNAL_SPECIFIC_REQUIREMENT` + `OBSERVED_CONVENTION` | The official scope calls for original research; 2026 ScienceDirect volumes classify ordinary content as `Research article`/`Research Articles` | official KBS page + ScienceDirect KBS 2026 content | Plan as a research article, not a review or short communication | Fix `Research article` as the drafting type; recheck the exact submission-menu label before upload |
| KBS-specific Word template | `UNVERIFIED` | The official page links the Guide for Authors, but its body was not accessible; no KBS-specific mandatory Word template could be verified | official KBS Guide link, access blocked | Do not reconstruct or invent a KBS template | Use a neutral editable Word master and recheck before submission |
| LaTeX template | `PUBLISHER_LEVEL_REQUIREMENT`/resource | Elsevier provides `elsarticle` LaTeX instructions/templates; this alone does not prove a KBS-specific mandate | `https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions` | Does not displace the author-approved Word workflow | Keep Word as operational master; LaTeX remains optional unless later required |
| Initial Word format | `PUBLISHER_LEVEL_REQUIREMENT` + journal-level `UNVERIFIED` | Elsevier workflows require editable sources; exact KBS formatting could not be directly confirmed | Elsevier author resources; inaccessible KBS GFA | Working format must remain simple, editable, and convertible | Use single-column simple styles as an internal conservative convention, not a claimed KBS rule |
| Free-format initial submission | `UNVERIFIED` | KBS participation in a free-format/Your-Paper-Your-Way regime could not be officially confirmed | KBS GFA inaccessible | Do not claim arbitrary formatting is acceptable | Maintain a clean reversible manuscript rather than relying on free format |
| Anonymization | `UNVERIFIED` | Exact KBS peer-review anonymization requirement could not be verified from an accessible official source | KBS GFA inaccessible | Affects submission copy rather than scientific content | Keep authors/affiliations in internal master; derive an anonymized copy only if required |
| Article structure | detail `UNVERIFIED`; `OBSERVED_CONVENTION` for IMRaD | Current KBS papers use conventional scientific sections; no mandatory heading list was directly verified | current ScienceDirect KBS research articles | 0D-1 architecture is compatible and scientifically stable | Keep 0D-1 architecture; future heading adaptation must be formal only |
| Abstract | `OBSERVED_CONVENTION` + limit `UNVERIFIED` | Current KBS research articles contain unstructured abstracts; exact limit is not officially verified | current ScienceDirect KBS articles | Abstract is late-stage under D-003 | Do not set a word count yet; recheck before drafting Abstract |
| Keywords | `OBSERVED_CONVENTION` + exact count `UNVERIFIED` | Current articles show keywords; exact required number is not verified | current ScienceDirect KBS articles | No early-drafting impact | Select late from stable terminology; verify count before submission |
| Highlights | publisher format `PUBLISHER_LEVEL_REQUIREMENT`; KBS-specific status `UNVERIFIED` | Elsevier defines 3–5 bullets, ≤85 characters, and notes that highlights are not required until final-files stage; KBS-specific requirement was not confirmed | `https://www.elsevier.com/researcher/author/tools-and-resources/highlights` | Should not drive manuscript sections | Prepare at final-files stage if KBS requests them |
| Graphical abstract | publisher specifications available; KBS status `UNVERIFIED` | Elsevier states that graphical-abstract policy is journal-specific | `https://www.elsevier.com/researcher/author/tools-and-resources/graphical-abstract` | No early text impact | Do not create yet; verify KBS requirement/option before submission |
| Word/page limit | `UNVERIFIED` | No current KBS maximum could be verified from an accessible official source | KBS GFA inaccessible | Potential late compression risk but not scientific-rewrite risk if sections remain modular | Draft economically; verify before manuscript closure |
| Figures/tables | `PUBLISHER_LEVEL_REQUIREMENT` | Elsevier provides artwork, sizing, sequencing, and caption requirements | `https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions` | Figures/tables must stay editable and scientifically purposeful | Preserve 0D-1 map, editable sources, and standalone captions |
| Supplementary material | publisher handling `PUBLISHER_LEVEL_REQUIREMENT`; KBS status `UNVERIFIED` | Elsevier supports supplementary content with identification/captions; KBS-specific obligation not verified | Elsevier author/media resources | Can host non-core reproducibility material | Use only when scientifically useful and not required in core narrative |
| Research Data / Data Availability | publisher workflow `PUBLISHER_LEVEL_REQUIREMENT`; current KBS `OBSERVED_CONVENTION` | Elsevier provides data statements and directs authors to journal policy; current KBS articles display `Data availability` | `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement`; KBS current papers | Candidate architecture already reserves Data/Code Availability | Keep candidate section; verify exact submission options later |
| Code Availability | KBS separate section `UNVERIFIED` | No separate mandatory KBS code section was verified; Elsevier includes software/code in research-data ecosystem | Elsevier research-data resources | Code traceability remains scientifically necessary regardless of label | Handle within Data/Code Availability, then adapt label to final GFA |
| Generative-AI declaration | `PUBLISHER_LEVEL_REQUIREMENT` | Substantive AI assistance in manuscript preparation requires disclosure before References; basic spelling/grammar checks do not | `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals` | AI is part of the writing workflow, so an auditable use log is required | Start AI-use log with Phase 1; prepare final declaration with tool, purpose, human review, responsibility |
| AI used in research | `PUBLISHER_LEVEL_REQUIREMENT` | AI used in research methods should be described reproducibly in Methods | same Elsevier AI policy | The experimental local LLM must be distinguished from manuscript-preparation AI | Document experimental LLM only from governing artifacts; editorial declaration covers writing assistance |
| CRediT | `PUBLISHER_LEVEL_REQUIREMENT` | Elsevier requests CRediT contribution statements during submission | `https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement` | No scientific-body impact | Prepare late from actual agreed contributions |
| Funding | `PUBLISHER_LEVEL_REQUIREMENT` | Funding sources and sponsor role must be disclosed where applicable | Elsevier Publishing Ethics | No body-text impact | Maintain funding ledger; complete final statement |
| Competing interests | `PUBLISHER_LEVEL_REQUIREMENT` | Authors must disclose relevant financial/personal relationships | `https://www.elsevier.com/about/policies-and-standards/publishing-ethics` | No scientific-body impact | Complete final declaration from author-confirmed facts |
| KBS submission checklist | `UNVERIFIED` | The KBS-specific checklist could not be inspected in the inaccessible GFA | KBS GFA inaccessible | May add auxiliary files but does not alter scientific core | Mandatory recheck immediately before submission |
| Final KBS reference style | `UNVERIFIED` as a textual GFA requirement | Exact final formatting could not be directly verified from the accessible official GFA; published articles are treated only as observed production convention | current KBS papers; inaccessible GFA | Does not block drafting because the author fixed provisional APA 7 and final Mendeley conversion | Keep provisional plain-text APA 7 in Word; verify KBS style and convert only at the end |
| Language | internal `RECOMMENDATION` | Manuscript master will use consistent academic English; no unverified KBS-specific English variant is asserted | project governance + Elsevier writing resources | Prevents variant mixing and later copy-editing | Adopt American English as internal project convention |

#### B.2 Template status

```text
KBS_TEMPLATE_STATUS = UNVERIFIED
```

The official source confirms the KBS Guide for Authors exists, but the template/formatting text itself could not be accessed. Elsevier provides an official publisher-level LaTeX template, but it is not presented here as a mandatory KBS template. No template is reconstructed from published papers or third-party pages.

This `UNVERIFIED` is classified as `UNVERIFIED_NONBLOCKING` for **initial scientific drafting** because the workflow uses a neutral, editable, single-column Word master with simple styles. A later template migration would be mechanical and must not alter claims or scientific architecture. It becomes a mandatory verification gate before generating the submission package.

#### B.3 Article-type status

```text
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
```

This is supported by the official KBS scope and current primary ScienceDirect content labelled `Research article`. The exact submission-system label must still be checked before upload, but there is no material ambiguity about the scientific article class to be drafted.

#### B.4 Reference-style status

```text
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
```

No exact KBS final reference style is asserted without direct access to the current GFA text. During drafting, the Word master uses **plain-text provisional APA 7**. The author will use Mendeley at the end and convert to the then-verified KBS style. This is `UNVERIFIED_NONBLOCKING` because it changes formatting, not claim–source relationships or scientific prose.

---

### C. Reconciliation of the 0D-1 architecture with KBS

No accessible official evidence requires a change to the scientific logic accepted in 0D-1. The architecture is therefore preserved and only its editorial role is normalized for the target.

| 0D-1 block | 0D-2 action | candidate drafting architecture | rationale | dependency |
|---|---|---|---|---|
| Introduction 1.1–1.3 | `KEEP` | problem/scope → prior-art limitation → provisional contribution/RQs | Compatible with research-article logic and project style; drafted late | partial Results + Related Work |
| Related Work 2.1–2.4 | `KEEP` | HS/candidate retrieval → RAG/regulatory reasoning → explainability/auditability → validity/provenance | Task-based organization supports KBS positioning | frozen 0B |
| Related Work 2.5 | `KEEP` | positioning synthesis | Shows the complete contract without automatic novelty | final gap/novelty undeclared |
| Methods 3.1–3.6 | `KEEP` | design/units → data → split → historical → normative → integration/invariance | Core architectural-methodological contract | frozen evidence |
| Methods 3.7–3.9 | `KEEP` | controlled LLM → function-specific evaluation → validity/drift/reproducibility | Makes interfaces, knowledge roles, evaluation, and limits visible | HE4/Group 2/C21–C25 |
| Results 4.1–4.5 | `KEEP` | split → RQ1 → RQ2 → RQ3 → sensitivities | Keeps function-specific results separate | authorized/conditional claims |
| Results 4.6 | `DEFER` | inferential RQ4 closure | Cannot be drafted before Group 3 | Group 3 |
| Results 4.7 | `DEFER` | EXP-11B only if editorially admitted | C10/C11 still block article use | C10/C11 reconciliation |
| Discussion 5.1–5.4 | `DEFER` | contract meaning → prior art → decision support → validity/transferability | Requires final Results | Group 3/final Results |
| Limitations 6.1–6.4 | `KEEP` | benchmark/data → HE4 → drift → reproducibility/external validity | Limitation transparency is central to bounded claims | final adjustment after Group 3 |
| Conclusions | `DEFER` | final scoped RQ response | Prevent premature closure | final Results/Discussion |
| Data/Code Availability | `KEEP` | repositories, availability, restrictions, provenance | Compatible with Elsevier research-data governance and C17 | final snapshot |
| Declarations | `KEEP` / late stage | funding, competing interests, CRediT, AI declaration | Publisher-level submission requirements | final target + author facts |

```text
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
```

The operational condition is to recheck whether the current KBS GFA requires specific heading names/order or separate files before submission. Such formal adaptation may not alter the scientific contract, RQs, claim boundaries, or Methods/Results/Discussion separation.

---

### D. Drafting-stage citation and reference policy

#### D.1 Governable rule

1. The Word working version uses **provisional APA 7** in plain text.
2. No Mendeley, Zotero, EndNote, or other live citation-manager fields are inserted during block drafting.
3. Markdown keeps visible citations consistent with the provisional Word version and a verifiable bibliography; no reference metadata is inferred.
4. Every source must already belong to an authorized corpus/registry or enter through an explicit gate; 0D-2 does not reopen Phase 0B.
5. At the end, the author links/manages citations in Mendeley and converts them to the then-verified official KBS style.
6. Reference-style conversion must not change which source supports which claim.
7. Missing DOI/pages/article number/metadata remain missing until verified; they are never pattern-completed.
8. The same bibliographic record may support multiple passages, but every **citation instance** in Word receives a separate audit comment whenever it supports a distinct claim.

#### D.2 Pre-conversion control

Before final Mendeley conversion, a reconciliation table must exist: `citation_instance → source_id → supported claim → verified metadata`. Bibliographic conversion is formatting work, not a late literature-discovery stage.

---

### E. Scientific writing policy for Phase 1 and later

```text
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
```

| dimension | drafting rule |
|---|---|
| Master language | English. English is the submission-facing manuscript version; Spanish remains the semantic-control mirror under D-002/D-010 |
| Internal English variant | American English, selected as a project consistency convention, not asserted as a KBS requirement |
| Register | Technical, restrained, international, verifiable, non-promotional |
| Voice | Prefer active constructions when the actor matters scientifically; passive is acceptable when procedure/object is the focus; avoid systematic mechanical passives |
| Methods tense | Past for executed actions; present for stable design/artifact properties when appropriate |
| Results tense | Past for observed results; present for explicit references to tables/figures or stable relationships |
| Related Work tense | Present for what a work establishes as current content; past for specific procedures/results when more precise |
| Discussion tense | Present for paper-level interpretation; past for specific experimental observations |
| Future tense | Only for genuine future work or unexecuted/deferred blocks; never to turn pending results into facts |
| Sentences | One main scientific relation per sentence. Internal target: usually 20–30 words; review >40-word sentences unless technically necessary |
| Paragraphs | One argumentative function per paragraph; usually 3–6 sentences; avoid one-sentence paragraphs except rare transitions |
| Terminology | Preserve `historical retrieval`, `historical ranking`, `fixed Top-3`, `normative retrieval`, `normative evidence`, `controlled explanation`, `local LLM`, `auditable recommendation`, `NANDINA subheading`, `series record`, `DAM/customs declaration` |
| Abbreviations | Define on first use; avoid abbreviating rarely repeated terms; preserve established necessary abbreviations |
| Numbers | Use numerals for metrics, sample sizes, percentages, and units; preserve denominators when scientifically informative |
| Percentages | First use of critical results should give numerator/denominator plus percentage when authorized; do not convert approximations into exact values |
| Precision | Never increase precision beyond the source or change rounding across text/table/figure. Canonical source value governs |
| Units | Use SI where applicable and consistent scientific spacing/conventions |
| Absolute language | Prohibited unless universally supported. Prefer bounded wording such as `under the evaluated conditions`, `within the fixed evaluation set`, `in the executed protocol` |
| Promotional adjectives | Avoid `robust`, `superior`, `effective`, `innovative`, `accurate`, `reliable`, `state-of-the-art` unless specifically supported |
| Anthropomorphism | Avoid “the model understands/knows/decides” when it only retrieves, ranks, or generates; state observable operation |
| Design vs result | Architectural property is not an empirical result; an empirical result is not a universal design property |
| Causality | Do not use causal `effect/impact/cause` language without a causal design. EXP-11A and sensitivity analyses retain non-causal boundaries |
| Ranking vs accuracy | Candidate-retrieval Top-k/MRR is not `overall classification/system/RAG accuracy` |
| Evidence vs correctness | Association, coverage, traceability, and source support do not equal normative/legal correctness |
| Architecture vs novelty | Architectural difference does not establish novelty; Alternative B remains provisional positioning |
| Configurability vs generalization | Configuration for other chapters/jurisdictions does not demonstrate empirical performance beyond Chapter 87 |
| Editorial inference | Label interpretation/inference as such; do not attribute it to experiments or literature as an observed result |

---

### F. Claim–evidence and anti-error protocol

```text
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
```

#### F.1 Mandatory rules

- Every number must have an identifiable source: artifact, table, file, authorized claim, or primary publication.
- No reference, DOI, volume, article number, date, author, or metadata may be invented, pattern-completed, or supplied from memory alone.
- Literature claims require checked source text; a title, search snippet, or incomplete abstract cannot support a broader claim.
- A source cannot be cited for a stronger proposition than its content establishes.
- Editorial inferences must be labelled as inference and kept distinct from experimental or literature findings.
- `CONDITIONAL`, `REVIEW_REQUIRED`, and `PROHIBITED` states in the Claim–Evidence Matrix are binding.
- C10/C11 remain unusable until explicit editorial reconciliation.
- Final RQ4/HE2/HE5 remain dependent on Group 3.
- C14 requires HE4 limitations; C12/C13/C18 remain prohibited.
- C21–C25 must preserve the method-dependent 0B-05C result; “no impact” is prohibited.
- Candidate retrieval, evidence retrieval, integration/invariance, and explanation/auditability results remain functionally distinct.
- Bounded prior-art search absence cannot become universal absence.

#### F.2 Mandatory pre-delivery checklist for the Writing AI

| check | required PASS condition |
|---|---|
| Scope | Work matches the closed prompt exactly; no unauthorized phase/block is opened |
| Source of truth | Most current applicable governing artifact was read; memory was not substituted |
| Numbers | Every figure traced; denominator, unit, sign, precision match source |
| Claims | Every claim is `AUTHORIZED` or within an expressly permitted `CONDITIONAL` use |
| Prohibited claims | No C09/C12/C13/C16/C18 or other blocked claim appears |
| C10/C11 | No H150/H200 article claim before reconciliation |
| Group 3 | No final RQ4/HE2/HE5 anticipation |
| Literature | Each citation checked against sufficient source content, not snippets/metadata alone |
| DOI/metadata | Match primary/verified record |
| Metric semantics | Top-k/MRR named for their actual function, not system accuracy |
| Normative boundary | Evidence/coverage/traceability not converted into legal correctness |
| Causality | No causal wording without causal design |
| Generalization | No empirical extrapolation beyond Chapter 87 |
| Novelty | No `first`, `novel`, `unprecedented`, `no prior work` without later authorization |
| ES/EN | Required internal versions preserve claim strength, values, limits, conditions |
| Word citations | Every new citation instance has a complete audit comment |
| Master integrity | Candidate starts from last approved master; no reconstruction from scratch |
| Versioning | Only authorized block changed; new candidate versions preserve approved history |

Any material failure stops delivery until corrected.

---

### G. Cumulative `.md` + `.docx` workflow

```text
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
```

#### G.1 Generation authority

The **Writing AI** generates and updates manuscript artifacts. The Managing AI audits and governs gates; the Experimental AI checks experimental consistency when required; the author approves. None replaces the Writing AI as manuscript-generation owner.

#### G.2 Deliverables per block

Every drafting delivery produces together:

1. the worked block `.md`;
2. a cumulative candidate master `.md`;
3. a cumulative candidate master `.docx`.

All three derive from the same scientific content. The `.docx` is updated on the **last approved cumulative version**, preserving styles, tables, figures, comments, and previously approved text. It is not rebuilt from scratch except for the authorized initial master creation from the adopted working format.

#### G.3 Bilingual governance and format roles

To comply with D-002 without contaminating the eventual submission package:

- block and master `.md` files contain `## Español` as semantic control and `## English` as the equivalent scientific manuscript text;
- the internal cumulative `.docx` contains two clearly separated parts: **Part I — English manuscript master** and **Part II — Spanish semantic-control mirror**;
- citation audit comments are anchored in English Part I;
- Part II is not part of the eventual submission file and may be removed only through an explicit final-package gate;
- removing the Spanish control part for submission is a controlled editorial transformation, not scientific rewriting.

#### G.4 Proposed naming/version convention

```text
article/sections/P01_METHODS_B01_V01.md
article/manuscript/ARTICLE_MASTER_CANDIDATE_V001.md
article/manuscript/ARTICLE_MASTER_CANDIDATE_V001.docx
```

After audit and approval:

```text
article/manuscript/ARTICLE_MASTER_APPROVED_V001.md
article/manuscript/ARTICLE_MASTER_APPROVED_V001.docx
```

The next block starts only from `ARTICLE_MASTER_APPROVED_V001` and produces `ARTICLE_MASTER_CANDIDATE_V002`. Corrective iterations create new versions rather than overwriting an approved binary.

Rules:

- `CANDIDATE` = non-canonical artifact pending audit/approval;
- `APPROVED` = accepted by required gates;
- only one approved `.md/.docx` pair may be baseline for the next delivery;
- master number advances on approved integration, not discarded attempts;
- block filename records phase/section/block for traceability;
- approved `.docx` hashes are recorded whenever a later prompt fixes the binary as immutable input.

#### G.5 Corrective V02/V03 behavior

A corrective revision starts from the prompt-specified candidate/approved state, preserves all approved material out of scope, changes only authorized observations, creates new candidate `.md/.docx` versions, never silently “cleans up” unrelated sections, and records the authorized changes.

#### G.6 Final editorial state

The final project retains:

```text
1 canonical master .md
1 canonical master .docx
version history of block and candidate/approved masters
source/claim/citation audit records
figure/table artifacts and editable sources
```

The submission Word is derived from the approved master and is never rewritten from fragmented block files.

---

### H. Word citation-audit comment protocol

```text
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
```

Every **citation instance** in English Part I must have a Word comment anchored exactly to the citation text. Required comment schema:

```text
FUENTE / REVISTA:
AUTOR(ES):
AFIRMACIÓN ORIGINAL / EXTRACTO TEXTUAL EXACTO Y SUFICIENTE:
TRADUCCIÓN AL ESPAÑOL:
JUSTIFICACIÓN DE RESPALDO:
LÍMITE DE LA CITA / QUÉ NO DEMUESTRA: [cuando sea pertinente]
```

Operational rules:

1. The excerpt preserves the source language and is the shortest sufficient passage supporting the manuscript claim.
2. The Spanish translation is faithful and cannot increase claim strength, scope, or causality.
3. `JUSTIFICACIÓN DE RESPALDO` explains the exact source–claim relation and adds no new proposition.
4. `LÍMITE DE LA CITA` is mandatory where overclaiming risk, task/dataset mismatch, non-causal inference, lack of generalization, source support without correctness, or another boundary applies.
5. The same reference used for different claims receives separate comments at each instance.
6. Citation clusters must preserve source-level accountability. Prefer a separate anchor for each reference token; if technically impossible, one cluster comment repeats the full schema for every source.
7. A comment cannot repair an unsupported citation. The claim must be narrowed or the citation removed/replaced through the proper bibliographic gate.
8. Search snippets, index pages, and metadata do not replace source text for scientific claims.
9. Own experimental claims are traced to internal artifacts/claims rather than pretending they are bibliographic citations.
10. Comments remain in internal masters; removal for submission occurs only after final audit confirms citation–claim–source traceability remains preserved.

---

### I. Acceptance-oriented KBS strategy without overclaiming

#### I.1 Paper center

The editorial center should be the **complete evaluated architectural-methodological contract**, not Peruvian customs by itself or the sum of BM25 + LLM. The manuscript should make interfaces, rank-preservation restrictions, invariants, differentiated knowledge-source roles, DAM-aware partitioning, function-specific metrics, provenance, and reproducibility visible.

#### I.2 What the paper must not resemble

- a local customs RAG application with no methodological contribution;
- an LLM classifier paper in which the LLM decides the code;
- a generic BM25-versus-dense comparison;
- a legal validation of NANDINA classifications;
- a paper claiming auditability is absent from prior regulatory AI;
- a compressed thesis containing many experiments without a central scientific thread;
- a collection of heterogeneous metrics treated as one system accuracy.

#### I.3 Desk-rejection risks and mitigation

| risk | level | pre-drafting mitigation |
|---|---|---|
| Integration perceived as incremental | HIGH | Formalize contract, interfaces, invariants, prohibitions; map every RQ to a differentiated function |
| Overly local application | MEDIUM-HIGH | Present Chapter 87 as a bounded demanding experimental case; derive design lessons without empirical-generalization claims |
| Insufficiently differentiated novelty | HIGH | Keep novelty undeclared; Related Work must show narrow differences and partial prior art without “first” claims |
| Weak HE4 validation | HIGH | Report N=50, AI evaluator, mismatch, modality limits; restrict HE4 to structure/traceability under protocol |
| Metric conflation | HIGH | Include an explicit `component → task → metric → permitted/prohibited interpretation` table |
| Internal-validity concerns | MEDIUM | Show DAM-disjoint split, intra-DAM dependence, near duplicates, concentration as distinct dimensions |
| Normative drift | MEDIUM | Present 0B-05C as documented method-dependent sensitivity, not “no effect” or legal correction |
| Reproducibility overclaiming | MEDIUM | Preserve nonblocking limitations and unrecoverable/local-only assets; provenance ≠ perfect reproducibility |
| Hidden negative/limited evidence | HIGH | Report bounded/diagnostic results transparently as limits of the contract, not as embarrassing exceptions |

#### I.4 Chapter-87 framing

Chapter/Class 87 is an **explicit experimental boundary** and evaluation case for the contract, not a representative sample of every tariff chapter, country, or jurisdiction. Framework configurability is a design property; empirical transfer remains untested.

#### I.5 HE4 treatment

HE4 does not establish legal correctness, complete normative fidelity, or human-equivalent quality. Its editorial role is to measure how the constrained generator preserves the fixed Top-3 and produces structured/traceable outputs under the executed protocol, with all frozen limitations visible.

#### I.6 Negative evidence and limitations

Diagnostic or limited results should not be hidden. The 20-case reranker, normative drift, HE4 limitations, near duplicates, concentration, and partial reproducibility delimit what the contract does and does not establish. This transparency strengthens the evaluation when it is integrated into the scientific logic rather than written defensively.

#### I.7 Future Title, Abstract, and Introduction

When their gates open, they should identify the scientific object and bounded empirical scope, distinguish historical ranking/normative evidence/controlled explanation, state only frozen results, avoid unauthorized `first/novel/unprecedented/robust/legally correct/generalizable` language, avoid presenting NANDINA as the sole contribution, and never call fixed Top-3 candidate retrieval overall accuracy. No such manuscript prose is drafted in 0D-2.

---

### J. A/B/C journal cascade

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
```

| dimension | KBS (A) | ESWA (B) | IPM (C) | common core | migration change | rewrite risk |
|---|---|---|---|---|---|---|
| Central contribution | architectural-methodological knowledge-system contract | applied intelligent/expert system with verifiable architectural restriction | information-retrieval/evidence/provenance architecture | B contract, RQs, boundaries | reweight framing, not evidence | MEDIUM |
| Domain role | bounded regulated knowledge case | expert application in government/law/auditing/IR | critical information-processing application | Chapter 87 as bounded scope | change editorial motivation/vocabulary | LOW-MEDIUM |
| Methods | interfaces, knowledge sources, invariance, function-specific evaluation | intelligent-system design/testing/implementation | retrieval/evidence flow/provenance/system design | Methods 3.1–3.9 and data | minor emphasis reorder | LOW |
| Results | function-specific RQ1–RQ4 | applied-system performance with separated metrics | retrieval/evidence metrics central, explanation supportive | governed tables/results | select/order tables | LOW |
| Related Work | KBS/RAG/knowledge systems | expert systems/applied AI | IR/information processing/evidence | frozen 0B corpus | reweight existing families; no automatic new novelty search | MEDIUM |
| Discussion | meaning of contract | value/limits as intelligent application | IR/evidence-architecture implications | same results/limitations | rewrite interpretation emphasis | MEDIUM |
| HE4 | limited complementary evidence | explainability/auditability component | downstream secondary component | same protocol/limits | emphasis only | LOW |
| Reproducibility | knowledge-system traceability/provenance | reproducible applied system | data/evidence/provenance discipline | same repos/artifacts | terminology mainly | LOW |
| Novelty risk | MEDIUM-HIGH | HIGH due genuine-innovation expectation | MEDIUM-HIGH if information-science contribution is unclear | novelty stays undeclared | reassess after rejection reason | MEDIUM |
| Format/reference style | recheck KBS final GFA | recheck ESWA GFA if B activates | recheck IPM GFA if C activates | editable master + final Mendeley conversion | formal conversion | LOW |
| Submission package | KBS final files | ESWA final files | IPM final files | data/code/AI/CRediT/funding/COI ledgers | checklists/metadata | LOW |

#### J.1 Post-rejection routing rule

The cascade is not automatic by rank. The rejection reason governs routing:

- KBS scope/knowledge-framing mismatch → assess ESWA if the intelligent/expert application is clearer;
- KBS assessment that the paper is primarily IR/evidence architecture → prioritize IPM;
- KBS novelty/incrementality rejection → **do not** automatically transfer to ESWA, whose innovation/repackaging risk is also high; trigger editorial reassessment first;
- rejection for scientific validity/evidence deficiencies → correct the deficiency before any resubmission; journal switching is not a mitigation.

```text
JOURNAL_CASCADE_STATUS = CLOSED_FOR_DRAFTING
```

This strategy minimizes rewriting because Methods, Results, data, claims, and experimental artifacts remain invariant. Most migration should affect Title/Abstract/Introduction, Related-Work synthesis, Discussion, cover letter, and formal submission requirements.

---

### K. Pre-drafting decision matrix

| decision | status | basis | remaining condition |
|---|---|---|---|
| A/B/C targeting | `CLOSED_FOR_DRAFTING` | 0D V02 + PASS review + current official scope verification | final selection still requires editorial/author approval |
| KBS scientific article type | `CLOSED_FOR_DRAFTING` | official scope + 2026 `Research article` labels | recheck submission-menu label |
| KBS-specific template | `UNVERIFIED_NONBLOCKING` | official GFA linked but body inaccessible | verify before submission; do not reconstruct |
| Initial working format | `CLOSED_WITH_OPERATIONAL_CONDITION` | neutral editable Word + cumulative Markdown prevents template lock-in | apply final format only after verification |
| Article architecture | `CLOSED_WITH_OPERATIONAL_CONDITION` | accepted 0D-1 architecture compatible with research article | final heading/order adaptation subject to GFA |
| Exact Abstract/keywords rules | `DEFERRED_WITHOUT_REWRITE_RISK` | late-stage content; exact KBS limits unverified | verify before those sections are drafted |
| Highlights | `DEFERRED_WITHOUT_REWRITE_RISK` | publisher format known; KBS requirement not confirmed | prepare at final-files stage if applicable |
| Graphical abstract | `UNVERIFIED_NONBLOCKING` | publisher says journal-specific | verify before submission |
| Exact length limit | `UNVERIFIED_NONBLOCKING` | GFA inaccessible | draft compactly; verify before final closure |
| Peer-review anonymization | `UNVERIFIED_NONBLOCKING` | inaccessible GFA | generate submission copy accordingly |
| Final KBS reference style | `UNVERIFIED_NONBLOCKING` | exact GFA style inaccessible | provisional APA7; final Mendeley conversion |
| Drafting reference policy | `CLOSED_FOR_DRAFTING` | explicit author decision | none |
| Writing policy | `CLOSED_FOR_DRAFTING` | STYLE_GUIDE + 0D2 | none |
| Claim–evidence protocol | `CLOSED_FOR_DRAFTING` | Claim Matrix/freezes | formal gate required for any status change |
| `.md/.docx` workflow | `CLOSED_FOR_DRAFTING` | cumulative workflow defined | audit/author approval before canonical promotion |
| Word citation comments | `CLOSED_FOR_DRAFTING` | schema and rules defined | technical implementation in each DOCX |
| AI-use governance | `CLOSED_FOR_DRAFTING` | current Elsevier policy | log use from Phase 1; disclose at submission |
| Data/Code governance | `CLOSED_WITH_OPERATIONAL_CONDITION` | existing project traceability + publisher policy | final wording/snapshot at submission |
| CRediT/funding/COI | `DEFERRED_WITHOUT_REWRITE_RISK` | publisher requirements | actual author information at closure |
| C10/C11 | `DEFERRED_WITHOUT_REWRITE_RISK` for independent blocks; blocks EXP-11B use | current editorial governance | explicit reconciliation |
| Group 3 | `DEFERRED_WITHOUT_REWRITE_RISK` for Methods/RW; blocks final RQ4/HE2/HE5 | current experimental state | Group-3 closure |

There is no `UNVERIFIED_BLOCKING` for starting the blocks already classified as draftable **after** the Managing AI and author formally close 0D/Phase 0. `UNVERIFIED_NONBLOCKING` items are submission-format details whose later application is mechanical and may not alter scientific content.

---

### L. Pre-drafting gate recommendation

```text
PRE_DRAFTING_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
```

The decisions that could otherwise cause early scientific rewriting are now closed: paper type, A/B/C strategy, scientific architecture, writing policy, claim–evidence protocol, drafting-stage reference governance, cumulative master workflow, and Word citation-audit comments. No `UNVERIFIED_BLOCKING` remains for the initial draftable blocks.

`WITH_CORRECTIONS` preserves operational conditions before **submission**, not before the first Methods draft:

1. directly recheck the then-current KBS Guide for Authors when accessible;
2. confirm any journal-specific Word/LaTeX template and whether it is mandatory;
3. confirm final reference style, length limits, abstract/keywords, anonymization, graphical abstract, highlights, and exact checklist;
4. transform the internal approved master into the KBS package only after the applicable scientific freeze;
5. keep C10/C11- and Group-3-dependent blocks closed until their own gates are satisfied.

This recommendation does **not** open Phase 1. The Managing AI and author must audit and close 0D/Phase 0 first.

```text
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

0D-2 introduces no new experimental evidence or interpretation. It governs editorial requirements and drafting operations over already governed evidence.

---

### M. Web and documentary traceability

**Editorial cutoff:** `elVladdi/gci-nandina-rag`, branch `article/main-manuscript`, commit `346d7b86bae279b38c377845fe332fce802d12f3`.

**Web verification date:** `2026-09-15`.

**Main official sources:**

- KBS official Elsevier journal page: `https://shop.elsevier.com/journals/knowledge-based-systems/0950-7051`
- KBS ScienceDirect journal/issues/articles: `https://www.sciencedirect.com/journal/knowledge-based-systems`
- KBS Guide for Authors: `https://www.sciencedirect.com/journal/knowledge-based-systems/publish/guide-for-authors` — official source identified; body inaccessible in this execution (`403`)
- Elsevier LaTeX instructions: `https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions`
- Elsevier AI policy: `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals`
- Elsevier Research Data / Data Statement: `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement`
- Elsevier CRediT: `https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement`
- Elsevier Publishing Ethics: `https://www.elsevier.com/about/policies-and-standards/publishing-ethics`
- Elsevier Highlights: `https://www.elsevier.com/researcher/author/tools-and-resources/highlights`
- Elsevier Graphical Abstract: `https://www.elsevier.com/researcher/author/tools-and-resources/graphical-abstract`
- Elsevier Artwork/Media: `https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions`
- ESWA official page: `https://shop.elsevier.com/journals/expert-systems-with-applications/0957-4174`
- IPM official page: `https://shop.elsevier.com/journals/information-processing-and-management/0306-4573`

**Use of current KBS publications:** only as `OBSERVED_CONVENTION` to establish current `Research article` labelling and the presence of abstract/keywords/highlights/data-availability/CRediT elements in recent published papers. Published-layout conventions are not silently promoted to Guide-for-Authors requirements.

**Third-party sources:** search results reproducing or summarizing the KBS Guide for Authors were excluded as governing authority. They were not used to close any requirement that could not be verified through an accessible official source.

```text
0D2_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
KBS_TEMPLATE_STATUS = UNVERIFIED
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
JOURNAL_CASCADE_STATUS = CLOSED_FOR_DRAFTING
PRE_DRAFTING_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
PHASE_1 = NOT_OPENED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```
