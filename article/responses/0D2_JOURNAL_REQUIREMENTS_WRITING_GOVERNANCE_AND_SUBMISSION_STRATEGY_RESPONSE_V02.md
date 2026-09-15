# 0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío — V02 / Journal Requirements, Writing Governance, and Submission Strategy — V02

## Español

### A. Estado de entrada, alcance de la revisión y criterio de verificación

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D-1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
0D2_ENTRY_GATE = PASS / OPENED
0D2_V01 = PASS_WITH_CORRECTIONS
0D-2 = REVISION_REQUIRED / V02
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
TARGET_JOURNAL = PENDING_0D2_AND_AUTHOR_APPROVAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

**ARCHIVOS LEÍDOS:** `article/START_HERE.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/reviews/0D2_ENTRY_GATE.md`; `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`; `article/reviews/0D_V02_INTERNAL_REVIEW.md`; `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/0B_PHASE_CLOSURE.md`; `article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY.md`; `article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V01.md`; `article/reviews/0D2_INTERNAL_REVIEW.md`; `article/reviews/0D2_AUTHOR_DECISION_DOCX_LANGUAGE_LAYOUT.md`; `article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_REVISION_V02.md`.

**FASE ACTIVA:** `0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío`.

**REDACCIÓN DE MANUSCRITO AUTORIZADA:** no. Esta V02 corrige únicamente 0D2-M01–0D2-M04. No contiene prosa destinada a Methods, Related Work, Results, Introduction ni ninguna otra sección del manuscrito y no abre Fase 1.

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

La verificación web de V02 se volvió a intentar el `2026-09-15` exclusivamente para 0D2-M01. Se priorizaron fuentes oficiales/primarias. La página oficial de KBS en Elsevier continúa confirmando el scope y enlazando el `Guide for Authors`; el acceso al cuerpo del Guide mediante ScienceDirect continuó devolviendo `403 Forbidden` en este entorno. ScienceDirect confirma mediante publicaciones 2026 que KBS publica contenido etiquetado como `Research article`. Las reglas generales de Elsevier sobre highlights y declaración de uso de IA continúan accesibles en fuente primaria. No se promovió ninguna reproducción de terceros a requisito oficial KBS.

Clasificación de evidencia editorial:

```text
JOURNAL_SPECIFIC_REQUIREMENT
PUBLISHER_LEVEL_REQUIREMENT
RECOMMENDATION
OBSERVED_CONVENTION
UNVERIFIED
```

Clasificación adicional exigida por 0D2-M01:

```text
KBS_REQUIREMENTS_VERIFIED_FROM_PRIMARY
KBS_REQUIREMENTS_UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT
KBS_REQUIREMENTS_DEFERABLE_WITHOUT_REWRITE_RISK
```

---

### B. Requisitos actuales de Knowledge-Based Systems y cierre correctivo 0D2-M01

#### B.1 Requisitos verificados desde fuente primaria

```text
KBS_REQUIREMENTS_VERIFIED_FROM_PRIMARY
```

| elemento | estado | evidencia primaria verificada | consecuencia operativa |
|---|---|---|---|
| Scope KBS | `VERIFIED_FROM_PRIMARY` | La página oficial de Elsevier KBS confirma investigación original en knowledge-based y otras técnicas de IA, knowledge engineering, intelligent decision support y aplicaciones | Mantener el framing arquitectónico-metodológico B, sin convertir el caso NANDINA en único aporte |
| Existencia del Guide for Authors | `VERIFIED_FROM_PRIMARY` | La página oficial KBS enlaza el `Guide for Authors` oficial de ScienceDirect | El GFA existe y debe volver a verificarse antes del paquete final; su contenido no se infiere cuando no es accesible |
| Clase científica del paper | `VERIFIED_FROM_PRIMARY + OBSERVED_CONVENTION` | Scope oficial exige investigación original y artículos KBS 2026 en ScienceDirect aparecen como `Research article` | Mantener `Research article` como tipo operativo para construcción; revalidar etiqueta exacta de submission antes de enviar |
| Highlights — formato publisher | `PUBLISHER_LEVEL_VERIFIED_FROM_PRIMARY` | Elsevier: 3–5 bullets, máximo 85 caracteres; no requeridos hasta final-files stage | No condicionan la redacción científica temprana; preparar solo cuando el journal los solicite |
| Política Elsevier de IA | `PUBLISHER_LEVEL_VERIFIED_FROM_PRIMARY` | Elsevier exige disclosure de uso sustantivo de IA en preparación y Methods para IA usada como parte de investigación | Registrar uso de IA desde Fase 1; separar IA experimental de IA de preparación del manuscrito |

Fuentes oficiales comprobadas en V02:

- KBS official Elsevier page: `https://shop.elsevier.com/journals/knowledge-based-systems/0950-7051`;
- KBS Guide for Authors link: `https://www.sciencedirect.com/journal/knowledge-based-systems/publish/guide-for-authors` — fuente oficial identificada; cuerpo no accesible (`403`) en esta ejecución;
- ejemplos primarios KBS 2026 etiquetados `Research article` en ScienceDirect, entre ellos `10.1016/j.knosys.2026.115405`, `10.1016/j.knosys.2026.115989` y `10.1016/j.knosys.2026.116358`;
- Elsevier Highlights: `https://www.elsevier.com/researcher/author/tools-and-resources/highlights`;
- Elsevier generative-AI policy: `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals`.

#### B.2 Requisitos no verificados pero potencialmente relevantes para reescritura

```text
KBS_REQUIREMENTS_UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT
```

| elemento | estado oficial | riesgo potencial | política interna de neutralización antes de Fase 1 | resultado pre-redacción |
|---|---|---|---|---|
| Plantilla Word KBS específica y obligatoriedad | `UNVERIFIED` | una plantilla rígida podría alterar layout, orden formal o archivos de submission | usar master Word neutral, editable, sin estilos journal-specific; estructura científica desacoplada del layout; headings semánticos; tablas editables; figuras separables; ninguna información científica dependiente de columnas, text boxes o maquetación | `CLOSED_WITH_OPERATIONAL_CONDITION` |
| Formato inicial / free format | `UNVERIFIED` | un formato inicial estricto podría exigir migración tardía | no asumir `free format`; usar documento de una columna, estilos simples, párrafos y captions ordinarios; todo contenido científico debe sobrevivir a cambio de estilo sin cambios de claims, evidencia o orden lógico | `CLOSED_WITH_OPERATIONAL_CONDITION` |
| Límite exacto de páginas/palabras | `UNVERIFIED` | compresión tardía podría forzar supresión o fusión apresurada | aplicar disciplina de extensión conservadora y control continuo de longitud descritos en B.4; ninguna cifra secundaria, repetición de tabla o detalle accesorio se incorpora si no cumple una función científica identificable | `CLOSED_WITH_OPERATIONAL_CONDITION` |
| Headings/orden formal obligatorio KBS | `UNVERIFIED` | un orden de headings distinto podría forzar reorganización formal | mantener arquitectura 0D-1 modular y desacoplada de numeración final; cada subsección tiene propósito/evidencia definidos y puede renombrarse o reordenarse formalmente sin alterar contenido científico | `CLOSED_WITH_OPERATIONAL_CONDITION` |

No se atribuyen a KBS un límite numérico de páginas, un régimen `Your Paper Your Way`, una plantilla Word específica ni un modelo de revisión que no estén confirmados por fuente primaria accesible. Los indicios de reproducciones secundarias no se usan como autoridad.

#### B.3 Requisitos diferibles sin riesgo de reescritura científica

```text
KBS_REQUIREMENTS_DEFERABLE_WITHOUT_REWRITE_RISK
```

| elemento | estado | por qué puede diferirse |
|---|---|---|
| Anonimización / modelo exacto de peer review | `UNVERIFIED` | afecta la copia de envío y metadatos; el master interno mantiene autores/afiliaciones y puede derivar una copia anonimizada sin cambiar ciencia |
| Límite exacto del Abstract | `UNVERIFIED` | Abstract se redacta al final; no afecta Methods/Related Work/Results tempranos |
| Número exacto de keywords | `UNVERIFIED` | se seleccionan al final desde terminología ya congelada |
| Obligatoriedad KBS de highlights | `UNVERIFIED` a nivel journal | Elsevier define su formato; se preparan como archivo final si aplica |
| Graphical abstract | `UNVERIFIED` a nivel KBS | no es necesario para construir el núcleo científico; se verifica antes de submission |
| Checklist KBS exacta | `UNVERIFIED` | puede requerir archivos/metadata auxiliares, no reescritura científica si el master y assets permanecen separados |
| Estilo final de referencias | `UNVERIFIED` | Word usa APA 7 provisional y el autor convertirá con Mendeley al final; la relación claim–source permanece estable |
| Etiqueta exacta de Data/Code Availability | `UNVERIFIED` | la información ya se preserva; el nombre/ubicación formal puede adaptarse antes de submission |
| CRediT, funding y competing interests concretos | `DEFERRED` | dependen de datos reales de autores y no alteran el cuerpo científico |

#### B.4 Justificación de migrabilidad del Word neutral

```text
NEUTRAL_WORD_MIGRATION_POLICY = ACTIVE
```

El Word neutral puede migrarse posteriormente al formato KBS **sin reescritura científica** porque se separan contenido y presentación mediante estas reglas obligatorias:

1. las secciones se identifican por función científica y estilos semánticos, no por formatos visuales KBS supuestos;
2. no se usa layout multicolumna, cuadros de texto, encabezados manuales ni numeración incrustada para almacenar contenido científico;
3. tablas permanecen editables y no contienen conclusiones irreemplazables solo en imagen;
4. figuras y captions se conservan como assets/secciones separables;
5. autores, afiliaciones, declaraciones y material de submission se mantienen separables del cuerpo;
6. cambiar fuente, márgenes, interlineado, numeración, orden formal permitido o plantilla no autoriza modificar claims, cifras, RQs, evidencia ni fronteras interpretativas;
7. si el GFA posteriormente exige un cambio que sí afecte contenido científico, deja de ser una migración mecánica y se activa un gate editorial explícito antes de submission.

Por tanto, la ausencia de plantilla KBS verificada no bloquea la construcción científica del manuscrito: queda neutralizada como problema de presentación mediante un master estructuralmente reversible.

#### B.5 Disciplina de extensión conservadora

```text
CONSERVATIVE_LENGTH_DISCIPLINE = ACTIVE
```

No se fija un límite numérico atribuido a KBS porque no se ha verificado en fuente primaria accesible. Desde Fase 1, el control interno será:

- registrar en cada integración candidata el conteo de palabras del **texto principal inglés**, separado de referencias, tablas, captions y declaraciones;
- una función científica principal por párrafo y eliminación sistemática de redundancia entre texto, tablas y figuras;
- Methods conserva lo necesario para comprender/reproducir el diseño; material auxiliar extenso solo se traslada a suplemento si un gate posterior confirma que hacerlo no elimina información esencial del cuerpo;
- Results no repite tablas fila por fila y reporta únicamente observaciones necesarias para responder las RQs autorizadas;
- Related Work se organiza por tareas/contrastes y evita catálogos de autores;
- Introduction, Discussion y Conclusions no se redactan antes de sus gates, evitando duplicación anticipada;
- en cada `MASTER_CANDIDATE_REVISION`, la longitud se audita antes de aceptar nuevo contenido, de modo que la compresión ocurra incrementalmente y no al final;
- cualquier futura restricción oficial KBS se aplica primero como presupuesto editorial; no se elimina evidencia necesaria ni se debilita reproducibilidad para cumplir extensión sin un gate científico-editorial.

Esta disciplina neutraliza el riesgo de una compresión científica tardía al mantener el manuscrito modular, no redundante y continuamente auditado en extensión, sin inventar un supuesto máximo KBS.

#### B.6 Matriz consolidada de requisitos KBS preservada de V01

| elemento | estado oficial | requisito exacto o estado verificable | impacto sobre redacción | acción |
|---|---|---|---|---|
| Scope | `JOURNAL_SPECIFIC_REQUIREMENT` | KBS publica investigación original en sistemas basados en conocimiento y otras técnicas de IA | framing del contrato completo | mantener B de 0C |
| Tipo de artículo | `JOURNAL_SPECIFIC_REQUIREMENT + OBSERVED_CONVENTION` | investigación original; publicaciones 2026 `Research article` | define clase científica | usar `Research article` como tipo operativo |
| Plantilla Word KBS | `UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT` | GFA oficial enlazado pero cuerpo inaccesible | layout inicial | neutral master + gate antes de submission |
| Plantilla LaTeX | `PUBLISHER_LEVEL_RESOURCE` | Elsevier ofrece `elsarticle`; no demuestra obligatoriedad KBS | ninguna para workflow Word | mantener Word operacional |
| Formato inicial / free format | `UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT` | no se confirma KBS `free format` | presentación inicial | formato neutral reversible; no asumir free format |
| Revisión anonimizada | `DEFERABLE_WITHOUT_REWRITE_RISK` | detalle KBS no verificado | copia de envío | derivar copia anonimizada solo si se exige |
| Estructura formal | `UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT` | headings obligatorios no verificados | orden formal | arquitectura modular 0D-1; adaptación formal sin alterar lógica |
| Abstract | `OBSERVED_CONVENTION`; límite `UNVERIFIED` | abstract presente en artículos actuales | etapa tardía | revalidar antes de Abstract |
| Keywords | `OBSERVED_CONVENTION`; cantidad `UNVERIFIED` | keywords presentes | etapa tardía | revalidar cantidad al final |
| Highlights | publisher format `VERIFIED`; KBS-specific `UNVERIFIED` | Elsevier 3–5 bullets, ≤85 caracteres, final-files stage | no afecta cuerpo | preparar si KBS lo solicita |
| Graphical abstract | `DEFERABLE_WITHOUT_REWRITE_RISK` | journal-specific según Elsevier | no afecta núcleo | verificar antes de submission |
| Extensión/páginas | `UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT` | no hay máximo KBS verificado | longitud | disciplina conservadora B.5 |
| Figuras/tablas | `PUBLISHER_LEVEL_REQUIREMENT` | assets legibles, secuenciados y captions | preparar editables | conservar mapa 0D-1 |
| Material suplementario | `PUBLISHER_LEVEL_HANDLING`; KBS-specific `UNVERIFIED` | Elsevier admite supplemental content | puede alojar material auxiliar | no desplazar evidencia esencial sin gate |
| Research Data | `PUBLISHER_LEVEL_REQUIREMENT/WORKFLOW`; KBS `OBSERVED_CONVENTION` | Elsevier data statement; KBS actuales muestran `Data availability` | sección candidata | conservar Data/Code Availability |
| Code Availability | `UNVERIFIED` como sección independiente | no se confirma etiqueta KBS separada | formal | mantener trazabilidad, adaptar etiqueta al final |
| Generative AI declaration | `PUBLISHER_LEVEL_REQUIREMENT` | disclosure para uso sustantivo en preparación | obligatorio por uso del flujo | log + statement final |
| IA como método de investigación | `PUBLISHER_LEVEL_REQUIREMENT` | describir en Methods cuando forma parte de investigación | LLM experimental | documentar reproduciblemente desde fuentes gobernantes |
| CRediT | `PUBLISHER_LEVEL_REQUIREMENT` | statement de contribuciones | late stage | completar con datos reales |
| Funding | `PUBLISHER_LEVEL_REQUIREMENT` | declarar fuentes/rol si aplica | late stage | ledger y statement final |
| Competing interests | `PUBLISHER_LEVEL_REQUIREMENT` | revelar relaciones pertinentes | late stage | confirmación autoral |
| Submission checklist | `DEFERABLE_WITHOUT_REWRITE_RISK` | GFA exacto inaccesible | paquete final | verificar inmediatamente antes de submission |
| Referencias finales KBS | `DEFERABLE_WITHOUT_REWRITE_RISK` | estilo exacto del GFA no verificado | presentación bibliográfica | APA 7 provisional solo en Word + Mendeley final |
| Idioma | `RECOMMENDATION` | inglés académico consistente; variante KBS específica no afirmada | consistencia | inglés estadounidense como convención interna |

#### B.7 Estados KBS

```text
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
```

---

### C. Reconciliación de la arquitectura 0D-1 con KBS

No existe evidencia primaria accesible que obligue a cambiar la lógica IMRaD aceptada en 0D-1. La arquitectura se conserva y queda desacoplada del formato final mediante la política de migrabilidad de B.4.

| bloque 0D-1 | acción 0D-2 | arquitectura candidata para redacción | razón | dependencia |
|---|---|---|---|---|
| Introduction 1.1–1.3 | `KEEP` | Problema/alcance → limitación de prior art → contribución provisional/RQs | Compatible con research article y STYLE_GUIDE; se redacta tarde | Results parciales + Related Work |
| Related Work 2.1–2.4 | `KEEP` | HS/candidate retrieval → RAG/regulatory reasoning → explainability/auditability → validity/provenance | organización por tareas | 0B frozen |
| Related Work 2.5 | `KEEP` | síntesis de posicionamiento | presenta contrato completo sin novelty automática | final gap/novelty no declarados |
| Methods 3.1–3.6 | `KEEP` | diseño/unidades → datos → split → histórico → normativa → integración/invariancia | núcleo arquitectónico-metodológico | evidencia congelada |
| Methods 3.7–3.9 | `KEEP` | LLM controlado → evaluación por función → validez/drift/reproducibilidad | hace visibles interfaces, conocimiento y límites | HE4/Grupo 2/C21–C25 |
| Results 4.1–4.5 | `KEEP` | split → RQ1 → RQ2 → RQ3 → sensibilidades | separa resultados por función | claims autorizados/condicionales |
| Results 4.6 | `DEFER` | cierre inferencial RQ4 | no antes de Grupo 3 | Grupo 3 |
| Results 4.7 | `DEFER` | EXP-11B solo si se autoriza editorialmente | C10/C11 bloquean uso | reconciliación C10/C11 |
| Discussion 5.1–5.4 | `DEFER` | significado del contrato → prior art → decision support → validez/transferibilidad | requiere Results finales | Grupo 3/Results finales |
| Limitations 6.1–6.4 | `KEEP` | benchmark/datos → HE4 → drift → reproducibilidad/external validity | control de overclaiming | ajuste final tras Grupo 3 |
| Conclusions | `DEFER` | respuesta final a RQs | evitar cierre prematuro | Results/Discussion finales |
| Data/Code Availability | `KEEP` | disponibilidad, repositorios, restricciones, provenance | compatible con C17/publisher | snapshot final |
| Declarations | `KEEP / LATE_STAGE` | funding, competing interests, CRediT, AI declaration | publisher-level | target final + datos de autores |

```text
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
```

La condición operacional es que cualquier requisito formal del GFA verificado posteriormente solo puede producir cambios de presentación, nombres de headings o archivos de submission. Si exigiera alterar contenido científico, se abre un gate específico; no se modifica silenciosamente la arquitectura congelada.

---

### D. Política de referencias y citas — corrección 0D2-M03

```text
WORD = PROVISIONAL_APA7_PRESENTATION_LAYER
MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY
```

#### D.1 Word

1. El Word de trabajo usa **APA 7 provisional** en texto plano.
2. No se insertan campos Mendeley, Zotero, EndNote ni otros gestores durante la redacción por bloques.
3. APA 7 provisional es una **capa de presentación exclusiva del Word**; no determina qué fuente respalda qué claim.
4. Cada instancia bibliográfica en Word mantiene comentario de auditoría claim–cita–fuente según la sección H.
5. Al final, el autor gestionará las referencias con Mendeley y convertirá el Word al estilo oficial KBS entonces verificado.

#### D.2 Markdown

1. Markdown conserva identificadores estables de fuente/cita (`source_id`, DOI verificado, clave bibliográfica interna o placeholder humano legible) suficientes para preservar la correspondencia semántica.
2. Markdown **no** es una segunda autoridad de formato APA 7 y no debe mantenerse como una bibliografía paralela cuya puntuación/orden/formato deba sincronizarse con Word.
3. Puede incluir placeholders legibles como `[CITE:SRC-XX]`, `[CITE:DOI-verificado]` o equivalentes definidos por el bloque, siempre que permitan resolver de manera inequívoca la fuente.
4. La equivalencia ES/EN del `.md` se refiere a contenido científico y trazabilidad, no a duplicar la presentación bibliográfica APA 7 del Word.
5. Antes de integración, cada placeholder debe resolver a una fuente verificada y autorizada; ningún placeholder permite incorporar una referencia nueva sin gate bibliográfico.

#### D.3 Conversión final

Antes de Mendeley debe existir una conciliación:

```text
citation_instance → source_id → claim_supported → verified_metadata → Word_location
```

La conversión final es una transformación de formato en Word. No es una fase de descubrimiento de literatura ni puede cambiar la relación entre fuente y claim.

---

### E. Política maestra de escritura científica

```text
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
```

| dimensión | regla de escritura |
|---|---|
| Idioma maestro | Inglés. La parte inglesa es el manuscrito destinado a publicación; la parte española es espejo interno de control semántico conforme a decisión autoral 0D2-M02 |
| Variante interna | Inglés estadounidense como convención de consistencia del proyecto, no como requisito KBS específico |
| Registro | Técnico, sobrio, internacional, verificable y no promocional |
| Voz | Preferir activa cuando el actor sea científicamente relevante; pasiva cuando procedimiento/objeto sea el foco; evitar pasiva mecánica |
| Methods — tiempo | Pasado para acciones ejecutadas; presente para propiedades estables del diseño/artefactos |
| Results — tiempo | Pasado para observaciones; presente solo para referencias explícitas a tablas/figuras o relaciones estables |
| Related Work — tiempo | Presente para lo que un trabajo establece como contenido vigente; pasado para procedimientos/resultados específicos cuando corresponda |
| Discussion — tiempo | Presente para interpretación del artículo; pasado para observaciones experimentales concretas |
| Futuro | Solo para trabajo futuro o bloques no ejecutados; nunca para presentar pendiente como hecho |
| Oraciones | Una relación científica principal por oración; revisar sistemáticamente oraciones >40 palabras |
| Párrafos | Una función argumental por párrafo; evitar párrafos de una sola oración salvo transición excepcional |
| Terminología | mantener `historical retrieval`, `historical ranking`, `fixed Top-3`, `normative retrieval`, `normative evidence`, `controlled explanation`, `local LLM`, `auditable recommendation`, `NANDINA subheading`, `series record`, `DAM/customs declaration` |
| Abreviaturas | definir en primera aparición; evitar abreviar términos poco repetidos |
| Números | usar cifras para métricas, tamaños, porcentajes y unidades; conservar denominadores cuando aporten significado |
| Porcentajes | resultado crítico: numerador/denominador + porcentaje cuando esté autorizado |
| Precisión | no aumentar decimales ni variar redondeo respecto de la fuente canónica |
| Unidades | SI cuando aplique; consistencia científica de símbolos y espaciado |
| Lenguaje absoluto | prohibido salvo soporte universal explícito; preferir `under the evaluated conditions`, `within the fixed evaluation set`, `in the executed protocol` |
| Adjetivos promocionales | evitar `robust`, `superior`, `effective`, `innovative`, `accurate`, `reliable`, `state-of-the-art` salvo autorización claim-level |
| Antropomorfismo | no decir que el modelo “understands/knows/decides” cuando recupera, rankea o genera |
| Diseño vs resultado | propiedad arquitectónica ≠ hallazgo empírico; hallazgo ≠ propiedad universal |
| Causalidad | no usar lenguaje causal sin diseño causal; EXP-11A y sensibilidades conservan límites no causales |
| Ranking vs accuracy | candidate-retrieval Top-k/MRR ≠ overall classification/system/RAG accuracy |
| Evidencia vs correctness | association/coverage/traceability/source support ≠ normative/legal correctness |
| Arquitectura vs novelty | architectural difference ≠ novelty by itself |
| Configurabilidad vs generalización | configurability ≠ empirical generalization |
| Inferencia editorial | marcar como inferencia y no atribuir al experimento/literatura como observación |

---

### F. Protocolo claim–evidence, anti-error, anti-alucinación y anti-overclaiming

```text
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
```

#### F.1 Reglas obligatorias

- Toda cifra debe tener fuente identificable: artefacto, tabla, archivo, claim autorizado o publicación primaria.
- Ninguna referencia, DOI, volumen, article number, fecha, autor o metadato puede inventarse, autocompletarse por patrón o recuperarse solo desde memoria.
- Ningún claim de literatura se redacta sin comprobar texto suficiente de la fuente; título, snippet o metadato no bastan para una afirmación más amplia.
- Una fuente no puede respaldar una afirmación más fuerte que su contenido.
- Toda inferencia editorial se identifica como inferencia y se separa de resultado experimental/literatura.
- `AUTHORIZED`, `CONDITIONAL`, `REVIEW_REQUIRED` y `PROHIBITED` se respetan literalmente según `CLAIM_EVIDENCE_MATRIX.md`.
- C10/C11 no pueden usarse hasta reconciliación editorial explícita.
- RQ4 y cierre HE2/HE5 permanecen dependientes de Grupo 3.
- C14 solo se usa con limitaciones HE4; C12/C13/C18 permanecen prohibidos.
- C21–C25 deben preservar que 0B-05C produjo efecto dependiente del método; no puede resumirse como “sin impacto”.
- `candidate retrieval ≠ overall classification accuracy`.
- `normative association ≠ substantive normative correctness`.
- `auditability ≠ legal correctness`.
- `configurability ≠ empirical generalization`.
- `journal fit ≠ novelty proof`.
- `architectural difference ≠ novelty by itself`.
- `absence within search scope ≠ universal absence`.

#### F.2 Checklist pre-entrega obligatorio

| control | PASS requerido |
|---|---|
| Scope | el bloque coincide exactamente con el prompt; no abre fases/bloques no autorizados |
| Fuente de verdad | se consultó artefacto gobernante vigente; no se sustituyó por memoria |
| Números | toda cifra trazada; denominador, unidad, signo y precisión coinciden |
| Claims | todo claim `AUTHORIZED` o dentro de uso `CONDITIONAL` expresamente permitido |
| Prohibidos | no aparecen C09/C12/C13/C16/C18 ni otros bloqueados |
| C10/C11 | no se usa H150/H200 antes de reconciliación |
| Grupo 3 | no se anticipan RQ4/HE2/HE5 finales |
| Literatura | cita comprobada contra texto suficiente, no snippet/metadata |
| DOI/metadata | coincide con fuente primaria/registro verificado |
| Métrica | Top-k/MRR nombrados por función real |
| Normativa | evidence/coverage/traceability no se convierte en legal correctness |
| Causalidad | no aparece causalidad sin diseño causal |
| Generalización | no se extrapola empíricamente fuera de Clase 87 |
| Novelty | no se usa `first/novel/unprecedented/no prior work` sin gate posterior |
| ES/EN | misma fuerza, cifra, límite y condición |
| Citaciones Word | cada instancia nueva tiene comentario completo |
| Integridad master | candidato parte del último master aprobado; no reconstrucción desde cero |
| Versionado | bloque/revisión/integración usan contadores separados de G.4 |
| Longitud | se actualiza conteo del texto principal inglés y se elimina redundancia antes de integrar |

Un fallo material detiene la entrega hasta corregirlo.

---

### G. Workflow acumulativo `.md` + `.docx` — correcciones 0D2-M02 y 0D2-M04

```text
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
AUTHOR_DECISION = APPROVED
```

#### G.1 Autoridad de generación

La **IA de Redacción** genera y actualiza los artefactos del manuscrito. La IA Gestora audita y administra gates; la IA Experimental revisa consistencia experimental cuando corresponda; el autor aprueba. Ninguno sustituye a la IA de Redacción como responsable de generación/actualización.

#### G.2 Entregables por bloque

Cada entrega futura de redacción producirá simultáneamente:

1. `.md` del bloque trabajado;
2. `.md` maestro acumulativo candidato;
3. `.docx` maestro acumulativo candidato.

Los tres derivan del mismo contenido científico. El `.docx` se actualiza sobre la **última versión acumulativa aprobada**, preservando estilos, tablas, figuras, comentarios y contenido aprobado. No se reconstruye desde cero, salvo creación inicial autorizada del master neutral.

#### G.3 Layout lingüístico del Word — decisión autoral cerrada

La decisión formalizada en `article/reviews/0D2_AUTHOR_DECISION_DOCX_LANGUAGE_LAYOUT.md` gobierna:

- el `.docx` maestro interno es bilingüe;
- **Part I — English manuscript master** contiene el manuscrito científico destinado a publicación;
- **Part II — Spanish semantic-control mirror** contiene el espejo español para revisión del autor;
- ambas partes mantienen equivalencia semántica claim por claim, cifra por cifra, límite por límite y condición por condición;
- comentarios de auditoría de citas se anclan a las citas de la parte inglesa;
- la parte española no forma parte del futuro archivo final de submission;
- su retiro solo se realiza mediante un gate editorial explícito al preparar el paquete final, sin alterar contenido científico aprobado;
- no se reabre esta decisión salvo nueva instrucción expresa del autor.

#### G.4 Convención de versionado no ambigua

```text
BLOCK_REVISION
MASTER_INTEGRATION
MASTER_CANDIDATE_REVISION
```

**Bloque:**

```text
article/sections/P01_METHODS_B01_V01.md
article/sections/P01_METHODS_B01_V02.md
```

`B01_V01 → B01_V02` significa revisión del mismo bloque. No implica nueva integración del master.

**Master candidato — revisiones del mismo intento de integración:**

```text
article/manuscript/ARTICLE_MASTER_V001_CANDIDATE_R01.md
article/manuscript/ARTICLE_MASTER_V001_CANDIDATE_R01.docx
article/manuscript/ARTICLE_MASTER_V001_CANDIDATE_R02.md
article/manuscript/ARTICLE_MASTER_V001_CANDIDATE_R02.docx
```

`R01 → R02` significa corrección del mismo candidato de integración. No avanza el número canónico.

**Master aprobado:**

```text
article/manuscript/ARTICLE_MASTER_APPROVED_V001.md
article/manuscript/ARTICLE_MASTER_APPROVED_V001.docx
```

Solo después de auditorías aplicables y aprobación del autor, la integración se convierte en `APPROVED_V001`. El siguiente bloque parte exclusivamente de ese baseline y prepara:

```text
article/manuscript/ARTICLE_MASTER_V002_CANDIDATE_R01.md
article/manuscript/ARTICLE_MASTER_V002_CANDIDATE_R01.docx
```

Reglas:

- `BLOCK_REVISION` cambia solo cuando cambia el borrador del bloque;
- `MASTER_CANDIDATE_REVISION` cambia cuando se corrige el mismo intento de integración;
- `MASTER_INTEGRATION` avanza únicamente cuando una nueva integración aprobada se convierte en baseline canónico;
- una corrección no puede aparentar una integración nueva;
- no se sobrescribe ningún `APPROVED`;
- hashes del `.docx` aprobado se registran cuando el siguiente prompt lo fije como entrada inmutable;
- V02/V03 correctivas preservan todo material aprobado fuera del alcance y modifican únicamente observaciones autorizadas.

#### G.5 Estado final del proyecto editorial

El cierre final conservará:

```text
1 master canónico .md
1 master canónico .docx bilingüe interno hasta el gate final de submission
historial versionado de bloques
historial versionado de masters candidatos y aprobados
registro de fuentes/claims/citas
assets editables de figuras/tablas
```

El Word final de submission se deriva del master aprobado mediante el gate que retira el espejo español y aplica formato/ref style final; no se reescribe desde archivos parciales.

---

### H. Protocolo de comentarios de auditoría por cita en Word

```text
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
```

Cada **instancia de cita** en la Part I inglesa debe tener comentario Word anclado exactamente a esa cita:

```text
FUENTE / REVISTA:
AUTOR(ES):
AFIRMACIÓN ORIGINAL / EXTRACTO TEXTUAL EXACTO Y SUFICIENTE:
TRADUCCIÓN AL ESPAÑOL:
JUSTIFICACIÓN DE RESPALDO:
LÍMITE DE LA CITA / QUÉ NO DEMUESTRA: [cuando sea pertinente]
```

Reglas:

1. el extracto conserva el idioma original y es el fragmento mínimo suficiente;
2. la traducción española es fiel y no aumenta fuerza, alcance o causalidad;
3. `JUSTIFICACIÓN DE RESPALDO` explica relación exacta fuente–claim y no introduce una proposición nueva;
4. `LÍMITE DE LA CITA` es obligatorio cuando exista riesgo de overclaiming, task/dataset mismatch, falta de generalización, source support sin correctness u otra frontera relevante;
5. una misma referencia usada para claims distintos recibe comentarios distintos por instancia;
6. en clusters se identifica respaldo individual por obra; preferencia: ancla por token de referencia;
7. un comentario no repara una cita insuficiente: se estrecha el claim o se sustituye/elimina la cita mediante gate;
8. snippets, índices y metadatos no sustituyen texto fuente para claims científicos;
9. claims experimentales propios se trazan a artefactos/claims internos, no se simula una cita bibliográfica;
10. comentarios permanecen en masters internos; su retiro para submission solo ocurre tras auditoría final de trazabilidad.

---

### I. Estrategia editorial para maximizar aceptación en KBS sin overclaiming

#### I.1 Centro del paper

El centro editorial continúa siendo el **contrato arquitectónico-metodológico completo evaluado**, no la aduana peruana aislada ni la suma BM25 + LLM. Deben hacerse visibles interfaces, invariantes, prohibición de modificar el ranking, función diferenciada de fuentes de conocimiento, DAM-aware partitioning, evaluación por función, provenance y reproducibilidad.

#### I.2 Lo que el paper no debe parecer

- una aplicación local de RAG a aduanas sin contribución metodológica;
- un clasificador LLM donde el LLM decide el código;
- una comparación genérica BM25 vs dense retrieval;
- una validación jurídica de clasificaciones NANDINA;
- un paper cuya novelty sea una supuesta ausencia general de auditabilidad en regulatory AI;
- una tesis comprimida sin hilo científico central;
- un conjunto de métricas heterogéneas tratado como una sola system accuracy.

#### I.3 Riesgos principales y mitigación

| riesgo | nivel | mitigación |
|---|---|---|
| Integración percibida como incremental | HIGH | formalizar contrato, interfaces, invariantes y prohibiciones; mapear RQs a funciones |
| Aplicación demasiado local | MEDIUM-HIGH | Clase 87 como caso acotado y exigente; lecciones de diseño sin generalización empírica |
| Novelty insuficientemente diferenciada | HIGH | `NOVELTY = NOT_DECLARED`; Related Work con diferencias estrechas, sin `first` |
| HE4 limitado | HIGH | N=50, evaluador IA, mismatch/modalidad visibles; solo estructura/trazabilidad |
| Confusión de métricas | HIGH | tabla `componente → tarea → output → métrica → interpretación permitida/prohibida` |
| Validez interna | MEDIUM | DAM-disjoint split, intra-DAM dependence, near-duplicates y concentración separados |
| Drift normativo | MEDIUM | sensibilidad 0B-05C dependiente del método; no “sin efecto” ni legal correction |
| Reproducibilidad sobreafirmada | MEDIUM | limitaciones no bloqueantes y assets no recuperables/local-only explícitos |
| Resultados negativos ocultos | HIGH | reportar resultados diagnósticos/limitados como delimitación del contrato |

#### I.4 Clase 87

Clase/Capítulo 87 es **alcance experimental delimitado** y caso de evaluación del contrato. No representa todas las clases, países o jurisdicciones. Configurabilidad es propiedad de diseño; transferencia empírica no demostrada.

#### I.5 HE4

HE4 no demuestra corrección jurídica, fidelidad normativa completa ni calidad humana equivalente. Su función editorial es evaluar preservación del Top-3 y estructura/trazabilidad bajo el protocolo ejecutado, con todas sus limitaciones.

#### I.6 Resultados negativos y limitaciones

Reranker de 20 casos, drift normativo, HE4, near-duplicates, concentración y reproducibilidad parcial deben presentarse para delimitar el alcance; no se ocultan ni se convierten en narrativa defensiva.

#### I.7 Futuro Title/Abstract/Introduction

Cuando sus gates se abran: objeto científico central + alcance experimental; separación ranking/evidencia/explicación; solo resultados congelados; sin `first`, `novel`, `unprecedented`, `robust`, `legally correct`, `generalizable`; NANDINA no es el único aporte; Top-3 no es overall accuracy. No se redacta ninguna de esas secciones en 0D-2.

---

### J. Estrategia de cascada A/B/C

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
```

| dimensión | KBS (A) | ESWA (B) | IPM (C) | núcleo común | cambio al migrar | riesgo |
|---|---|---|---|---|---|---|
| Contribución | contrato knowledge-based arquitectónico-metodológico | intelligent/expert system aplicado con restricción verificable | arquitectura IR/evidence/provenance | contrato B, RQs, límites | reponderar framing | MEDIUM |
| Dominio | caso regulatorio de conocimiento acotado | aplicación experta government/law/auditing/IR | critical information-processing application | Clase 87 acotada | motivación/vocabulario | LOW-MEDIUM |
| Methods | interfaces, fuentes, invariancia, evaluación por función | diseño/testing del intelligent system | retrieval/evidence flow/provenance | 3.1–3.9 y datos | énfasis menor | LOW |
| Results | RQ1–RQ4 por función | performance aplicado con métricas separadas | retrieval/evidence centrales, explicación secundaria | mismos resultados gobernados | orden/selección de tablas | LOW |
| Related Work | KBS/RAG/knowledge systems | expert systems/applied AI | IR/information processing/evidence | corpus 0B frozen | reponderar familias | MEDIUM |
| Discussion | significado del contrato | valor/límites de aplicación inteligente | implicaciones IR/evidence | mismos resultados/limitaciones | énfasis interpretativo | MEDIUM |
| HE4 | evidencia complementaria limitada | explainability/auditability component | downstream secundario | mismo protocolo/límites | solo énfasis | LOW |
| Reproducibilidad | provenance/knowledge-system traceability | reproducible applied system | data/evidence/provenance | mismos repos | terminología | LOW |
| Novelty risk | MEDIUM-HIGH | HIGH | MEDIUM-HIGH | novelty no declarada | revisar framing según rechazo | MEDIUM |
| Formato/referencias | GFA KBS a revalidar | GFA ESWA al activar B | GFA IPM al activar C | master neutral + Mendeley final | conversión formal | LOW |
| Submission package | KBS-specific | ESWA-specific | IPM-specific | ledgers data/code/AI/CRediT/funding/COI | checklist/metadata | LOW |

Regla de transferencia:

- rechazo KBS por scope/framing knowledge-based → evaluar ESWA si el carácter expert/intelligent application es más claro;
- rechazo porque el trabajo es principalmente IR/evidence architecture → priorizar IPM;
- rechazo por novelty/incrementalidad → no transferir automáticamente a ESWA; activar revisión editorial del motivo;
- rechazo por validez/evidencia → corregir problema científico antes de cambiar de revista.

```text
JOURNAL_CASCADE_STATUS = CLOSED_FOR_DRAFTING
```

Methods, Results, datos, claims y artefactos permanecen como núcleo común; la migración se concentra en framing, Title/Abstract/Introduction, síntesis de Related Work, Discussion, cover letter y formalidades.

---

### K. Matriz de decisiones pre-redacción corregida

| decisión | estado | fundamento | condición restante |
|---|---|---|---|
| Target A/B/C | `CLOSED_FOR_DRAFTING` | 0D-1 auditado + scope actual | selección final requiere auditoría/autor |
| Tipo científico KBS | `CLOSED_FOR_DRAFTING` | scope oficial + `Research article` 2026 | revalidar etiqueta del submission system |
| Plantilla KBS | `CLOSED_WITH_OPERATIONAL_CONDITION` | requisito oficial `UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT`, neutralizado por master reversible | verificar antes de submission |
| Formato inicial | `CLOSED_WITH_OPERATIONAL_CONDITION` | no se asume free format; master neutral | aplicar formato final tras verificación |
| Arquitectura | `CLOSED_WITH_OPERATIONAL_CONDITION` | 0D-1 modular y compatible | adaptación formal no puede cambiar lógica científica |
| Extensión | `CLOSED_WITH_OPERATIONAL_CONDITION` | límite KBS no verificado; disciplina B.5 activa | aplicar requisito oficial cuando sea accesible sin eliminar evidencia esencial |
| Anonimización | `DEFERRED_WITHOUT_REWRITE_RISK` | solo copia de envío | verificar antes de submission |
| Abstract/keywords | `DEFERRED_WITHOUT_REWRITE_RISK` | late stage | verificar antes de redactarlos |
| Highlights | `DEFERRED_WITHOUT_REWRITE_RISK` | formato publisher verificado; KBS-specific no confirmado | final files si aplica |
| Graphical abstract | `DEFERRED_WITHOUT_REWRITE_RISK` | journal-specific | verificar antes de submission |
| Estilo final referencias KBS | `CLOSED_WITH_OPERATIONAL_CONDITION` | APA7 solo Word + Mendeley final | verificar estilo KBS antes de conversión |
| Política referencias de trabajo | `CLOSED_FOR_DRAFTING` | M03 corregida | ninguna |
| Writing policy | `CLOSED_FOR_DRAFTING` | STYLE_GUIDE + V01 aceptada | ninguna |
| Claim–evidence | `CLOSED_FOR_DRAFTING` | Claim Matrix + freezes | cambios solo por gate |
| Workflow `.md/.docx` | `CLOSED_FOR_DRAFTING` | M02 autoral + M04 corregida | aprobación de cada integración |
| Layout Word | `CLOSED_FOR_DRAFTING` | decisión expresa del autor | `DOCX_BILINGUAL_INTERNAL_MASTER` |
| Comentarios Word | `CLOSED_FOR_DRAFTING` | protocolo aceptado | implementación técnica por cita |
| AI-use governance | `CLOSED_FOR_DRAFTING` | política Elsevier primaria | log desde Fase 1 y disclosure final |
| Data/Code | `CLOSED_WITH_OPERATIONAL_CONDITION` | trazabilidad existente + política publisher | wording/snapshot final |
| CRediT/funding/COI | `DEFERRED_WITHOUT_REWRITE_RISK` | publisher-level | datos reales al cierre |
| C10/C11 | `DEFERRED_WITHOUT_REWRITE_RISK` para bloques independientes; bloqueante para EXP-11B | gobernanza vigente | reconciliación antes de uso |
| Grupo 3 | `DEFERRED_WITHOUT_REWRITE_RISK` para Methods/RW; bloqueante para RQ4/HE2/HE5 final | estado vigente | cierre Grupo 3 |

```text
UNVERIFIED_BLOCKING = NONE_IDENTIFIED_FOR_INITIAL_DRAFTABLE_BLOCKS
```

Los requisitos no verificados capaces de afectar formato inicial, arquitectura o longitud no se ignoran: quedan identificados como potencialmente reescribientes y neutralizados mediante políticas internas reversibles/conservadoras. Si una futura verificación muestra un requisito que no pueda satisfacerse sin cambiar ciencia, el gate debe reabrirse antes del paquete de submission.

---

### L. Recomendación de gate pre-redacción

```text
PRE_DRAFTING_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
```

**Fundamento:** 0D2-M01 queda corregido mediante separación explícita de requisitos primarios verificados, requisitos no verificados potencialmente reescribientes y requisitos diferibles; los riesgos de plantilla/formato/estructura/extensión se neutralizan con master neutral reversible y disciplina conservadora de longitud. 0D2-M02 queda cerrado por decisión expresa del autor. 0D2-M03 separa APA 7 exclusivamente en Word de Markdown como capa de trazabilidad. 0D2-M04 separa revisión de bloque, revisión de candidato e integración del master.

`PASS_WITH_CORRECTIONS` no abre Fase 1. Conserva como condiciones operativas futuras, principalmente antes del **submission**:

1. reintentar el Guide for Authors KBS oficial cuando sea accesible;
2. confirmar plantilla/formato exactos y obligatoriedad;
3. confirmar límite final, abstract/keywords, revisión/anonymization, graphical abstract, highlights y checklist;
4. confirmar estilo final KBS antes de conversión Mendeley;
5. transformar el master interno al paquete KBS mediante gate explícito;
6. mantener cerrados EXP-11B y Grupo-3-dependent blocks hasta sus gates.

```text
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

No se introduce evidencia experimental ni interpretación nueva.

---

### M. Trazabilidad web y documental

**Corte editorial ejecutado:** `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`, commit `348a7ae20a8c337dcf52eca90af60ace0e763e99`.

**Fecha de reverificación web:** `2026-09-15`.

**Fuentes oficiales/primarias reintentadas o preservadas:**

- KBS official Elsevier page: `https://shop.elsevier.com/journals/knowledge-based-systems/0950-7051`;
- KBS official Guide for Authors: `https://www.sciencedirect.com/journal/knowledge-based-systems/publish/guide-for-authors` — enlace oficial confirmado; cuerpo devolvió `403 Forbidden`;
- KBS current ScienceDirect research articles, usados solo para `OBSERVED_CONVENTION` de tipo `Research article`;
- Elsevier Highlights: `https://www.elsevier.com/researcher/author/tools-and-resources/highlights`;
- Elsevier generative-AI policy: `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals`;
- Elsevier LaTeX instructions: `https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions`;
- Elsevier Research Data / Data Statement: `https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement`;
- Elsevier CRediT: `https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement`;
- Elsevier Publishing Ethics: `https://www.elsevier.com/about/policies-and-standards/publishing-ethics`;
- Elsevier Graphical Abstract: `https://www.elsevier.com/researcher/author/tools-and-resources/graphical-abstract`;
- Elsevier Artwork/Media: `https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions`;
- ESWA official page: `https://shop.elsevier.com/journals/expert-systems-with-applications/0957-4174`;
- IPM official page: `https://shop.elsevier.com/journals/information-processing-and-management/0306-4573`.

**Fuentes de terceros:** no se usaron como autoridad para cerrar requisitos KBS no accesibles en fuente primaria.

```text
0D2_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
0D2_M01 = ADDRESSED
0D2_M02 = ADDRESSED_BY_AUTHOR_DECISION
0D2_M03 = ADDRESSED
0D2_M04 = ADDRESSED
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
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

### A. Entry state, revision scope, and verification standard

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D-1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
0D2_ENTRY_GATE = PASS / OPENED
0D2_V01 = PASS_WITH_CORRECTIONS
0D-2 = REVISION_REQUIRED / V02
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
TARGET_JOURNAL = PENDING_0D2_AND_AUTHOR_APPROVAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

**FILES READ:** `article/START_HERE.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/reviews/0D2_ENTRY_GATE.md`; `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`; `article/reviews/0D_V02_INTERNAL_REVIEW.md`; `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/0B_PHASE_CLOSURE.md`; the original 0D-2 prompt; V01; `article/reviews/0D2_INTERNAL_REVIEW.md`; `article/reviews/0D2_AUTHOR_DECISION_DOCX_LANGUAGE_LAYOUT.md`; and the V02 revision prompt.

**ACTIVE PHASE:** `0D-2 — Journal requirements, writing governance, and submission strategy`.

**MANUSCRIPT DRAFTING AUTHORIZED:** no. V02 corrects only 0D2-M01–0D2-M04 and does not draft manuscript sections or open Phase 1.

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

Current official-source verification was reattempted on `2026-09-15` solely for 0D2-M01. The official Elsevier KBS page still confirms scope and links the official ScienceDirect Guide for Authors; the guide body still returned `403 Forbidden` in this environment. Primary ScienceDirect 2026 content confirms current `Research article` labelling. Elsevier publisher-level Highlights and generative-AI policy pages remain directly accessible. No third-party reproduction is treated as governing authority.

Required verification classes:

```text
KBS_REQUIREMENTS_VERIFIED_FROM_PRIMARY
KBS_REQUIREMENTS_UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT
KBS_REQUIREMENTS_DEFERABLE_WITHOUT_REWRITE_RISK
```

---

### B. Current KBS requirements and corrective closure of 0D2-M01

#### B.1 Requirements verified from primary sources

```text
KBS_REQUIREMENTS_VERIFIED_FROM_PRIMARY
```

| element | status | primary evidence | operational consequence |
|---|---|---|---|
| KBS scope | `VERIFIED_FROM_PRIMARY` | Official Elsevier KBS page confirms original research in knowledge-based/AI systems, knowledge engineering, intelligent decision support, and applications | Preserve architectural-methodological B framing rather than a customs-only application narrative |
| Existence of official GFA | `VERIFIED_FROM_PRIMARY` | Official KBS page links ScienceDirect Guide for Authors | GFA must be rechecked before final package; inaccessible text is not inferred |
| Scientific article class | `VERIFIED_FROM_PRIMARY + OBSERVED_CONVENTION` | Official scope requires original research; 2026 KBS ScienceDirect content is labelled `Research article` | Use `Research article` as operational drafting type; recheck exact submission-system label later |
| Highlights publisher format | `PUBLISHER_LEVEL_VERIFIED_FROM_PRIMARY` | Elsevier: 3–5 bullets, ≤85 characters, final-files stage | Does not control early scientific drafting |
| Elsevier AI policy | `PUBLISHER_LEVEL_VERIFIED_FROM_PRIMARY` | Substantive manuscript-preparation AI requires disclosure; research-method AI is described in Methods | Keep AI-use log from Phase 1 and separate research AI from writing assistance |

#### B.2 Unverified requirements that could otherwise cause rewriting

```text
KBS_REQUIREMENTS_UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT
```

| element | official state | potential risk | internal pre-Phase-1 neutralization | pre-drafting result |
|---|---|---|---|---|
| KBS-specific Word template/mandatory use | `UNVERIFIED` | rigid template could change layout/order/files | neutral editable master; semantic headings; editable tables; separable figures; no scientific content stored in layout-dependent constructs | `CLOSED_WITH_OPERATIONAL_CONDITION` |
| Initial format/free format | `UNVERIFIED` | strict format could require late migration | never assume free format; use simple single-column reversible working layout | `CLOSED_WITH_OPERATIONAL_CONDITION` |
| Exact word/page limit | `UNVERIFIED` | late compression could force rushed deletion/merging | conservative continuous length discipline in B.5 | `CLOSED_WITH_OPERATIONAL_CONDITION` |
| Mandatory heading/order details | `UNVERIFIED` | formal order could require rearrangement | modular 0D-1 sections with explicit purpose/evidence; formal rename/reorder cannot alter science | `CLOSED_WITH_OPERATIONAL_CONDITION` |

No page limit, review model, free-format regime, or KBS-specific template is attributed to KBS without accessible primary confirmation.

#### B.3 Deferable requirements without scientific rewrite risk

```text
KBS_REQUIREMENTS_DEFERABLE_WITHOUT_REWRITE_RISK
```

Anonymization/review-copy layout, exact Abstract limit, exact keyword count, KBS-specific highlights requirement, graphical abstract, final submission checklist, final reference style, exact Data/Code heading, and concrete CRediT/funding/COI data can be resolved later because they change the submission layer or late-stage sections rather than the governed scientific core.

#### B.4 Neutral Word migration policy

```text
NEUTRAL_WORD_MIGRATION_POLICY = ACTIVE
```

The neutral Word can later absorb verified KBS formatting without scientific rewriting because content is decoupled from presentation: semantic styles rather than assumed KBS styles; no multicolumn/text-box storage of scientific content; editable tables; separable figures/captions; separable author/declaration metadata; and a strict rule that formatting conversion cannot alter claims, numbers, RQs, evidence, or interpretive boundaries. If a later GFA rule requires a scientific-content change, migration stops and an explicit editorial gate is opened.

#### B.5 Conservative length discipline

```text
CONSERVATIVE_LENGTH_DISCIPLINE = ACTIVE
```

No numeric limit is attributed to KBS. From Phase 1, every candidate integration records English main-text word count separately from references/tables/captions/declarations; redundancy between prose/tables/figures is removed continuously; Methods retains essential reproducibility information; Results reports only RQ-relevant observations and does not duplicate tables; Related Work remains task-organized; late-stage sections remain closed until their gates; and length is reviewed at every candidate-master revision. Any future official KBS constraint is applied as an editorial budget before submission and cannot justify silent loss of necessary evidence.

#### B.6 Consolidated KBS status

```text
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
```

---

### C. 0D-1 architecture reconciliation with KBS

The accepted architecture is preserved. No accessible primary KBS rule requires a scientific-logic change. Introduction remains late; Related Work remains task-based; Methods 3.1–3.9 preserve design/data/split/historical retrieval/normative retrieval/integration/controlled LLM/function-specific evaluation/validity; Results 4.1–4.5 remain function-separated; Results 4.6 remains Group-3-dependent; Results 4.7 remains C10/C11-dependent; Discussion and Conclusions remain deferred; Limitations and Data/Code Availability remain structurally planned.

```text
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
```

Any later journal-specific heading or file adaptation is presentation-only unless a new gate explicitly authorizes a scientific change.

---

### D. Drafting citation/reference policy — 0D2-M03

```text
WORD = PROVISIONAL_APA7_PRESENTATION_LAYER
MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY
```

**Word:** plain-text provisional APA 7; no live citation-manager fields during block drafting; each citation instance carries its audit comment; final author-side Mendeley conversion occurs only after official KBS style is verified.

**Markdown:** stable source/citation identifiers and human-readable placeholders as required for semantic traceability; it is not a second APA-7 formatting authority and does not maintain a parallel APA bibliography surface. Every placeholder must resolve to an authorized verified source before integration.

Final reconciliation remains:

```text
citation_instance → source_id → claim_supported → verified_metadata → Word_location
```

---

### E. Scientific writing policy

```text
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
```

The V01 policy is preserved: English master; American-English internal consistency convention; precise restrained register; active/passive voice chosen by scientific function; section-appropriate tenses; concise one-function sentences/paragraphs; controlled terminology and abbreviations; source-governed numbers/precision/units; bounded language; no unsupported promotional adjectives; no anthropomorphism; no design→result, association→correctness, architectural-difference→novelty, configurability→generalization, or noncausal-design→causal-claim transformations.

---

### F. Claim–evidence and anti-error protocol

```text
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
```

The V01 protocol is preserved in full: every number and bibliographic fact requires traceable evidence; no invented DOI/metadata; literature claims require sufficient source text; source strength bounds claim strength; inference is labelled; Claim-Matrix states are binding; C10/C11 remain blocked; RQ4/HE2/HE5 remain Group-3-dependent; HE4 boundaries remain explicit; C21–C25 retain method-dependent interpretation; and the mandatory distinctions `candidate retrieval ≠ overall classification accuracy`, `normative association ≠ substantive normative correctness`, `auditability ≠ legal correctness`, `configurability ≠ empirical generalization`, `journal fit ≠ novelty proof`, `architectural difference ≠ novelty by itself`, and `absence within search scope ≠ universal absence` remain operative.

The pre-delivery checklist continues to require PASS for scope, source-of-truth currency, numbers, claims, prohibited claims, C10/C11, Group 3, literature support, DOI/metadata, metric semantics, normative boundaries, causality, generalization, novelty, ES/EN equivalence, Word citation comments, master integrity, versioning, and length discipline.

---

### G. Cumulative `.md` + `.docx` workflow — 0D2-M02 and 0D2-M04

```text
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
AUTHOR_DECISION = APPROVED
```

#### G.1 Deliverables and ownership

The Writing AI owns generation/update of the block `.md`, cumulative candidate master `.md`, and cumulative candidate master `.docx`. The Managing AI, Experimental AI, and author audit within their respective scopes. Each Word candidate starts from the last approved cumulative Word and is not rebuilt from scratch except initial authorized master creation.

#### G.2 Author-approved bilingual Word layout

The internal master Word is bilingual. **Part I — English manuscript master** is the publication-facing scientific manuscript. **Part II — Spanish semantic-control mirror** facilitates author review. Both remain semantically equivalent. Citation-audit comments are anchored to English citations. The Spanish internal mirror is removed only through an explicit final-submission gate and removal cannot change approved scientific content.

#### G.3 Separate revision/integration counters

```text
BLOCK_REVISION
MASTER_INTEGRATION
MASTER_CANDIDATE_REVISION
```

Examples:

```text
P01_METHODS_B01_V01.md
P01_METHODS_B01_V02.md
ARTICLE_MASTER_V001_CANDIDATE_R01.md/.docx
ARTICLE_MASTER_V001_CANDIDATE_R02.md/.docx
ARTICLE_MASTER_APPROVED_V001.md/.docx
ARTICLE_MASTER_V002_CANDIDATE_R01.md/.docx
```

`BLOCK_REVISION` tracks changes to the same block; `MASTER_CANDIDATE_REVISION` tracks corrections to the same integration candidate; `MASTER_INTEGRATION` advances only after an integration passes required audits and author approval. No approved artifact is overwritten.

---

### H. Word citation-audit comments

```text
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
```

Each citation instance in English Part I retains the required anchored comment:

```text
FUENTE / REVISTA:
AUTOR(ES):
AFIRMACIÓN ORIGINAL / EXTRACTO TEXTUAL EXACTO Y SUFICIENTE:
TRADUCCIÓN AL ESPAÑOL:
JUSTIFICACIÓN DE RESPALDO:
LÍMITE DE LA CITA / QUÉ NO DEMUESTRA: [cuando sea pertinente]
```

The original-language excerpt must be sufficient; Spanish translation cannot strengthen it; support justification must explain the exact relation; limits are mandatory where overclaiming risk exists; distinct claims require distinct comments even for the same reference; unsupported citations must be corrected rather than “repaired” by comments; and comments remain internal until final traceability audit.

---

### I. KBS acceptance strategy without overclaiming

The accepted V01 strategy is preserved. The scientific center is the complete evaluated architectural-methodological contract. The paper must not look like a local customs-only RAG application, an autonomous LLM classifier, a generic BM25-vs-dense comparison, legal validation, or a compressed thesis. Main risks remain perceived incremental integration, local scope, novelty overclaiming, HE4 limitations, metric conflation, validity threats, normative drift, reproducibility overstatement, and hidden negative evidence. Mitigation remains explicit interfaces/invariants, bounded Chapter-87 framing, transparent HE4 limitations, function-specific metrics, DAM-aware validity controls, method-dependent drift reporting, and transparent reproducibility limitations.

No Title, Abstract, Introduction, Methods, Related Work, Results, Discussion, Conclusions, or other manuscript prose is drafted here.

---

### J. A/B/C journal cascade

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
JOURNAL_CASCADE_STATUS = CLOSED_FOR_DRAFTING
```

The V01 cascade is preserved: Methods, Results, data, claims, and experimental artifacts form the reusable core. KBS emphasizes the knowledge-system contract; ESWA emphasizes a restricted intelligent/expert application; IPM emphasizes information retrieval/evidence/provenance. Migration should mainly affect framing, Title/Abstract/Introduction, Related-Work synthesis, Discussion, cover letter, and formal package. Rejection reason—not journal rank—governs transfer. A novelty/incrementality rejection does not trigger automatic transfer to ESWA; scientific-validity rejection must be corrected before resubmission.

---

### K. Corrected pre-drafting decision matrix

| decision | status | remaining condition |
|---|---|---|
| A/B/C targeting | `CLOSED_FOR_DRAFTING` | final selection after editorial/author gate |
| KBS article class | `CLOSED_FOR_DRAFTING` | recheck submission-system label |
| KBS template | `CLOSED_WITH_OPERATIONAL_CONDITION` | official requirement remains unverified; neutral master active; verify before submission |
| Initial working format | `CLOSED_WITH_OPERATIONAL_CONDITION` | no free-format assumption; final conversion after verification |
| Article architecture | `CLOSED_WITH_OPERATIONAL_CONDITION` | formal GFA adaptation cannot alter science |
| Length | `CLOSED_WITH_OPERATIONAL_CONDITION` | conservative continuous discipline; apply official rule when accessible |
| Anonymization | `DEFERRED_WITHOUT_REWRITE_RISK` | verify for submission copy |
| Abstract/keywords | `DEFERRED_WITHOUT_REWRITE_RISK` | verify before late-stage drafting |
| Highlights/graphical abstract | `DEFERRED_WITHOUT_REWRITE_RISK` | verify KBS-specific status before final package |
| Final KBS reference style | `CLOSED_WITH_OPERATIONAL_CONDITION` | verify before author-side Mendeley conversion |
| Word/Markdown citation policy | `CLOSED_FOR_DRAFTING` | none |
| Writing policy | `CLOSED_FOR_DRAFTING` | none |
| Claim–evidence protocol | `CLOSED_FOR_DRAFTING` | formal gate for any status change |
| `.md/.docx` workflow | `CLOSED_FOR_DRAFTING` | each integration still needs audits/approval |
| Word language layout | `CLOSED_FOR_DRAFTING` | bilingual internal master author-approved |
| Word citation comments | `CLOSED_FOR_DRAFTING` | implement per citation |
| AI governance | `CLOSED_FOR_DRAFTING` | log use; final disclosure |
| Data/Code | `CLOSED_WITH_OPERATIONAL_CONDITION` | final snapshot/wording |
| CRediT/funding/COI | `DEFERRED_WITHOUT_REWRITE_RISK` | real author data |
| C10/C11 | block only EXP-11B use | reconcile before use |
| Group 3 | blocks final RQ4/HE2/HE5 | Group-3 closure |

```text
UNVERIFIED_BLOCKING = NONE_IDENTIFIED_FOR_INITIAL_DRAFTABLE_BLOCKS
```

---

### L. Pre-drafting gate recommendation

```text
PRE_DRAFTING_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
```

M01 is addressed by explicit requirement stratification plus reversible format and conservative length policies. M02 is closed by the author's bilingual-Word decision. M03 makes APA 7 a Word-only provisional presentation layer and Markdown a traceability layer. M04 separates block revision, candidate-master revision, and approved master integration.

This recommendation does **not** open Phase 1. Remaining conditions are chiefly pre-submission verification of the official KBS GFA, exact template/format/length, late-stage metadata/files, final reference style, and continued enforcement of the C10/C11 and Group-3 gates.

```text
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

---

### M. Web/documentary traceability

**Editorial cutoff:** `elVladdi/gci-nandina-rag`, `article/main-manuscript`, commit `348a7ae20a8c337dcf52eca90af60ace0e763e99`.

**Web reverification date:** `2026-09-15`.

Primary/official sources preserved or rechecked: official Elsevier KBS page; official KBS ScienceDirect Guide link (body inaccessible with `403`); current primary KBS research articles; Elsevier Highlights; Elsevier generative-AI policy; Elsevier LaTeX, research-data, CRediT, publishing-ethics, graphical-abstract and artwork/media resources; and the official ESWA/IPM pages for the cascade. Third-party reproductions were not used as governing authority.

```text
0D2_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
0D2_M01 = ADDRESSED
0D2_M02 = ADDRESSED_BY_AUTHOR_DECISION
0D2_M03 = ADDRESSED
0D2_M04 = ADDRESSED
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
KBS_TEMPLATE_STATUS = UNVERIFIED / NEUTRAL_MASTER_POLICY_ACTIVE
KBS_ARTICLE_TYPE_STATUS = CLOSED_FOR_DRAFTING / RESEARCH_ARTICLE
KBS_REFERENCE_STYLE_STATUS = UNVERIFIED_FINAL_STYLE / PROVISIONAL_APA7_POLICY_CLOSED
ARTICLE_ARCHITECTURE_STATUS = CLOSED_WITH_OPERATIONAL_CONDITION
WRITING_POLICY_STATUS = CLOSED_FOR_DRAFTING
CLAIM_EVIDENCE_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
MD_DOCX_WORKFLOW_STATUS = CLOSED_FOR_DRAFTING
WORD_CITATION_COMMENT_PROTOCOL_STATUS = CLOSED_FOR_DRAFTING
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
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
