# Fase 1 — Methods B01 — Revisión V05 conforme a KBS-34

## Español

### Instrucción operativa

Actúa exclusivamente como **IA de Redacción** del artículo científico en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Ejecuta exclusivamente la revisión **V05 de Methods B01 — 3.1 Design, scope, and units**. **No avances a B02 ni a ninguna otra sección.**

Antes de redactar, lee íntegramente el onboarding y los artefactos vigentes, incluyendo obligatoriamente:

- `article/START_HERE.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/STYLE_GUIDE.md`;
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
- `article/governance/D013_KBS_EMPIRICAL_WRITING_GUIDE_APPROVAL.md`;
- `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md` — leer el contenido completo; su metadata DRAFT fue supersedida por D-013;
- `article/literature/KBS_34_ARTICLE_EDITORIAL_PATTERN_MATRIX.md`;
- `article/reviews/1_METHODS_B01_KBS_EDITORIAL_REAUDIT_V03.md`;
- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V03.md`;
- `article/sections/methods/Methods_B01_V03.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.md`;
- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V03.md`;
- este prompt.

### Estado previo y naturaleza de V05

V03 conserva `SCIENTIFIC_CONTENT_REVIEW = PASS` y no presenta errores científicos materiales. Sin embargo, tras aprobar el autor la guía empírica KBS-34, V03 fue reauditable editorialmente y obtuvo `KBS_EDITORIAL_FIT = PASS_WITH_CORRECTIONS`.

El prompt V04 previo queda `NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION` porque estaba limitado a reparar el DOCX sin modificar el texto. V05 debe resolver simultáneamente:

```text
B01_M09 = DOCX_PACKAGE_INTEGRITY
B01_M10 = ARCHITECTURE_OVERVIEW_DENSITY
B01_M11 = ABSTRACT_NOMINALIZATION_AND_CONTRACT_LANGUAGE
B01_M12 = CONFIGURABILITY_PRECONDITIONS
B01_M13 = TESTBED_BOUNDARY_CONCRETENESS
```

### Objetivo editorial

Reescribe 3.1 para que suene como una sección Methods de un research article reciente de *Knowledge-Based Systems*, no como un documento de gobernanza, contrato administrativo o especificación de requisitos.

La prosa debe seguir preferentemente relaciones concretas de tipo:

`input → actor/componente → operación → condición → output`

Usa voz activa cuando mejore la claridad. No ocultes acciones detrás de nominalizaciones. Evita acumular varias abstracciones en una misma oración.

### Correcciones obligatorias

#### B01-M10 — Reducir densidad de la vista arquitectónica inicial

Mantén una visión general temprana del flujo, pero no enumeres en 3.1 todas las prohibiciones detalladas del LLM. En este bloque bastan las invariantes centrales:

- el ranking histórico fija el Top-3 antes de la recuperación normativa;
- la recuperación normativa aporta evidencia para esos candidatos sin cambiar el ranking;
- el LLM opera después y no retroalimenta la selección/ranking.

Las restricciones finas de insertar, eliminar, sustituir o reordenar pertenecen a las subsecciones posteriores de invariancia/explicación y no deben desarrollarse exhaustivamente aquí.

#### B01-M11 — Sustituir lenguaje contractual por operaciones observables

Puedes conservar **una** referencia al `functional contract` si sirve para nombrar el aporte, pero solo después de describir concretamente el flujo. Evita formulaciones acumuladas como `fixed sequence of responsibilities` o frases que podrían pertenecer a un protocolo de gobernanza.

Debe quedar claro qué entra, qué hace cada etapa y qué sale.

#### B01-M12 — Expresar configurabilidad con precondiciones

Mantén el punto científico aprobado: el método está diseñado para poder instanciarse con recursos definidos para otro estudio/dominio.

Formula de manera concreta que una instancia requiere, como mínimo:

- un banco/dataset histórico etiquetado respecto del universo de clases objetivo;
- un universo de clases objetivo definido;
- un corpus documental/normativo compatible con los candidatos y con el mecanismo de recuperación;
- interfaces de representación/identificación coherentes entre esos recursos y el pipeline.

No conviertas 3.1 en una especificación técnica detallada: indica las precondiciones y difiere los detalles a 3.2/3.9.

Mantén expresamente:

`CONFIGURABILITY / REPLICABILITY ≠ EMPIRICAL GENERALIZATION`.

No afirmar plug-and-play universal, interoperabilidad automática ni transferencia de performance.

#### B01-M13 — Hacer concreta la delimitación del testbed

Presenta NANDINA Chapter 87 después del método general como la instancia experimental evaluada. La frontera debe quedar en términos concretos: los resultados empíricos del artículo corresponden al piloto offline de Chapter 87 y a las versiones de datos, corpus y configuración utilizadas en ese piloto.

No uses como cierre una lista abstracta del tipo `administrative, documentary, temporal, and experimental conditions`.

#### B01-M09 — Reparar el Word

La entrega V05 debe incluir un `.docx` OOXML válido. Antes del commit realiza QA técnico real:

- integridad ZIP/OOXML completa;
- `word/document.xml` presente;
- cero comentarios;
- cero tracked changes;
- render/apertura exitosa con un motor DOCX disponible;
- equivalencia del texto visible entre Markdown y Word.

### Contenido científico que debe preservarse

Preservar sin alterar el alcance:

- método general antes del testbed;
- recuperación histórica = generación/ranking de candidatos;
- Top-k y Top-3 histórico fijo;
- recuperación normativa = evidencia para candidatos ya fijados;
- recuperación normativa no reordena el ranking;
- LLM local posterior = explicación controlada, sin feedback al ranking;
- ranking, evidencia y explicación como funciones diferenciadas;
- NANDINA Chapter 87 = testbed empírico;
- sistema = apoyo a decisión no vinculante;
- revisión experta fuera del flujo automatizado vigente;
- unidad de observación/análisis = `series record` de DAM;
- DAM = grouping unit cuando la dependencia sea metodológicamente relevante;
- query = serie representada por descripción comercial normalizada;
- output relevante = Top-k / fixed historical Top-3 para las etapas posteriores;
- configurabilidad delimitada sin generalización empírica.

### Claims y exclusiones

```text
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
GROUP3 = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
CITATION_COMMENT_COVERAGE = 0/0
```

No introducir:

- resultados o métricas concretas;
- inferencia estadística;
- claims de causalidad;
- novelty final;
- claims de superioridad;
- generalización empírica fuera de Chapter 87;
- corrección jurídica o clasificación legalmente vinculante;
- literatura externa o citas nuevas;
- resultados de Grupo 3;
- EXP-11B;
- detalles técnicos propios de B02–B09;
- detalles del repositorio de reproducibilidad que corresponden a 3.9/end matter.

Los 34 artículos KBS analizados son **evidencia editorial**, no fuentes científicas automáticas para este bloque. No los cites en Methods B01.

### Estilo KBS obligatorio

La subsección debe:

- sonar natural en inglés científico internacional;
- utilizar párrafos con una función argumental reconocible;
- evitar frases que solo nombran categorías sin explicar relaciones;
- evitar sobreexplicar restricciones ya destinadas a subsecciones posteriores;
- mantener economía expresiva sin volverse telegráfica;
- preservar equivalencia semántica inglés–español;
- no inflar la longitud respecto de V03 salvo necesidad científica real.

No existe un número de palabras obligatorio. La claridad y la densidad informativa tienen prioridad.

### Artefactos V05

Genera exclusivamente:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V05.md`;
2. `article/sections/methods/Methods_B01_V05.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V05.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V05.docx`.

No sobrescribas ni elimines V01–V03. No generes V04. No crees todavía `ARTICLE_MASTER_V001.*`.

No modifiques `ARTICLE_STATUS.md`, `DECISIONS.md`, reviews, gobernanza, Claim–Evidence Matrix, literatura, Plan Maestro ni ningún bloque posterior.

### Checklist obligatorio en la respuesta V05

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
GUIDE_APPROVAL = D-013
BLOCK = Methods_B01
BLOCK_REVISION = V05
V04_STATUS = NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION
B01_M09 = ADDRESSED
B01_M10 = ADDRESSED
B01_M11 = ADDRESSED
B01_M12 = ADDRESSED
B01_M13 = ADDRESSED
SCIENTIFIC_CONTENT_SCOPE_FROM_V03 = PRESERVED
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS
GENERAL_METHOD_FIRST = PASS
NANDINA_AS_TESTBED_SECOND = PASS
INPUT_OPERATION_OUTPUT_CLARITY = PASS
ABSTRACTION_DENSITY = LOW_TO_MODERATE
CONTRACT_LANGUAGE_OVERLOAD = ABSENT
CONFIGURABILITY_PRECONDITIONS = EXPLICIT_BOUNDED
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
DOCX_ZIP_INTEGRITY = PASS
DOCX_DOCUMENT_XML = PRESENT
DOCX_COMMENTS = 0
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS
MD_DOCX_VISIBLE_TEXT_EQUIVALENCE = PASS
DOCX_SHA256 = ...
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V05.md + .docx
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW
```

No declares Methods B01 `APPROVED`, `FROZEN` ni `AUTHOR_APPROVED`.

---

## English

Perform only the V05 revision of Methods B01 (Section 3.1). Do not advance to B02 or any later section.

V03 retains its scientific-content pass, but the author has now approved the KBS-34 empirical writing guide through D-013. The KBS-specific reaudit therefore requires B01-M10 through B01-M13 in addition to the unresolved DOCX integrity issue B01-M09. The previously issued V04 delivery-repair-only prompt is `NOT_EXECUTED / SUPERSEDED_BEFORE_EXECUTION`; do not create V04 artifacts.

Rewrite Section 3.1 in the prose style evidenced by recent KBS research articles: concrete input–operation–output relations, active and natural scientific English where appropriate, low abstraction density, and clear rhetorical function for each paragraph. Keep the early architecture overview, but move exhaustive LLM prohibition details out of 3.1 conceptually; retain only the core invariants needed to understand the design. Use `functional contract` sparingly and only after the concrete operations are clear.

State configurability together with bounded preconditions: a labeled historical resource aligned with the target class universe, a defined target class universe, a compatible documentary/normative corpus, and coherent representation/identifier interfaces. Do not imply universal plug-and-play behavior or empirical transfer. Present NANDINA Chapter 87 afterwards as the evaluated offline testbed, and delimit empirical evidence to that pilot and the data/corpus/configuration versions used there.

Preserve the authorized claim set `[C01, C02, C03, C07, C15]`, introduce no citations or results, and maintain all scientific boundaries from V03. Produce only the four V05 artifacts listed above and provide a technically valid, renderable bilingual DOCX that passes the required OOXML and visible-text QA checks.
