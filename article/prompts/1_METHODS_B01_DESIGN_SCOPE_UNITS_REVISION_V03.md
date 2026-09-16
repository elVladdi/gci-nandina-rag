# Fase 1 — Methods B01 — Revisión V03 / Closed Revision Prompt

## Español

### Instrucción operativa

Actúa exclusivamente como **IA de Redacción** del artículo científico en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Corrige exclusivamente `Methods B01 — Design, scope, and units` V02. **No avances a B02 ni a ninguna otra sección.**

Lee íntegramente, además del onboarding y `MWDP_V1.0` obligatorios:

- `article/ARTICLE_STATUS.md`;
- `article/STYLE_GUIDE.md`;
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
- `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`;
- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`;
- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V02.md`;
- `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V02.md`;
- `article/sections/methods/Methods_B01_V02.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md`;
- el `SRC-03` vivo indicado en `SOURCE_REGISTRY.md`;
- este prompt.

El estado experimental correcto para este corte sigue siendo `GROUP3 = NOT_STARTED`. No uses resultados ni inferencias de Grupo 3.

### Objetivo de V03

La V03 debe conservar las correcciones científicas ya logradas en V02, pero mejorar de forma sustantiva la **claridad de prosa, visibilidad del aporte metodológico y comprensión de la configurabilidad del enfoque**.

El lector debe poder entender, sin tener que reconstruir una secuencia de abstracciones, cuatro ideas en este orden:

1. **qué método general se propone/evalúa**;
2. **cómo funciona el contrato entre sus componentes**;
3. **qué elementos pueden configurarse para una replicación o nueva instancia**;
4. **cómo se evaluó concretamente esa instancia en NANDINA Capítulo 87**.

No conviertas esta secuencia en una declaración final de novelty.

### Correcciones obligatorias

#### B01-M06 — Reducir abstracciones y nominalizaciones acumuladas

Aplicar obligatoriamente `SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`.

La V02 es científicamente correcta, pero concentra demasiadas formulaciones abstractas y nominalizaciones. V03 debe preferir oraciones concretas en las que sea evidente:

- qué componente recibe la entrada;
- qué operación realiza;
- qué produce;
- qué no puede modificar;
- cómo pasa la información al siguiente componente.

No elimines terminología técnica necesaria, pero evita cadenas como una sucesión de etiquetas conceptuales sin verbos o relaciones explícitas. No redactes como especificación de software ni como texto de gobernanza.

#### B01-M07 — Hacer visible el aporte arquitectónico-metodológico completo

El bloque no debe presentar solamente tres módulos separados. Debe quedar claro que el objeto metodológico del artículo es el **contrato funcional completo**:

```text
historical retrieval fixes/ranks candidates
→ fixed Top-3
→ normative retrieval provides evidence for those fixed candidates without reranking
→ local LLM receives the fixed candidates plus retrieved evidence and generates the explanation
→ no insertion / deletion / substitution / reordering / classification feedback
→ evaluation is organized by function
```

Puedes reformularlo en prosa natural. No es obligatorio reproducir esta cadena literalmente.

En B01 solo debes presentar la lógica general de evaluación por función. **No introduzcas métricas, cifras ni resultados**; estos corresponden a bloques posteriores.

La formulación debe ser compatible con el posicionamiento 0C: el objeto diferenciador es el contrato funcional completo evaluado, no la mera coexistencia de sus componentes. No declarar novelty final, superioridad ni ausencia universal de prior art.

#### B01-M08 — Hacer visible la configurabilidad/replicabilidad sin afirmar generalización empírica

Por instrucción expresa del autor, el lector debe comprender desde Methods que la arquitectura puede **instanciarse/configurarse** con recursos definidos por cada estudio o replicación, manteniendo el mismo contrato funcional.

Expresa de manera sobria y acotada que una instancia puede utilizar:

- un **dataset o banco histórico etiquetado** propio;
- un **universo de clases objetivo** definido para la tarea;
- un **corpus documental o normativo** apropiado al dominio.

En el presente artículo, la instancia evaluada utiliza NANDINA Capítulo 87 y los recursos versionados del piloto.

Esta afirmación debe quedar estrictamente delimitada como **propiedad de diseño/configurabilidad/replicabilidad**. No afirmar que el desempeño observado se generaliza a otros datasets, clases, capítulos, niveles, jurisdicciones o corpus.

Preservar expresamente la frontera:

```text
CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION
```

Para esta V03 se autoriza el uso acotado de `C15` con ese único sentido. No extrapoles C15 más allá de lo respaldado por la arquitectura y los artefactos de reproducibilidad. Si una formulación específica no está respaldada por las fuentes gobernantes, no la inventes: delimítala o repórtala como observación de entrega.

Los detalles sobre construcción/versionamiento del banco histórico y corpus, y sobre el repositorio de reproducibilidad, **no deben desarrollarse en B01**. Su tratamiento corresponde a las subsecciones posteriores de Methods. B01 solo debe dejar clara la propiedad general del diseño y el alcance de la instancia evaluada.

### Correcciones previas que deben permanecer cerradas

No reintroduzcas los problemas ya resueltos:

- **B01-M01:** no usar lenguaje interno de gobernanza en el manuscrito;
- **B01-M02:** primera aparición inglesa de DAM = `Declaración Aduanera de Mercancías (DAM; customs declaration)` o equivalente natural;
- **B01-M03:** no confundir configurabilidad con generalización empírica. V03 puede usar `C15` únicamente por la autorización específica B01-M08;
- **B01-M05:** arquitectura general primero; NANDINA Capítulo 87 después como testbed experimental regulatorio.

### Contenido científico que debe conservarse

Conservar:

- piloto experimental aplicado y offline;
- arquitectura de apoyo a decisión no vinculante;
- revisión experta fuera del flujo automático;
- historical retrieval = generación y ranking de candidatos;
- normative retrieval = evidencia documental para candidatos fijados, sin sustituir ni reordenar el ranking;
- local LLM = explicación downstream del Top-3 fijo, sin clasificación desde cero ni inserción/eliminación/sustitución/reordenamiento/feedback;
- SERIE como unidad de observación y análisis;
- DAM como unidad de agrupamiento cuando la dependencia sea metodológicamente relevante;
- SERIE/descripción comercial normalizada como unidad de consulta;
- historical Top-k y fixed historical Top-3 como objetos de salida pertinentes;
- alcance empírico restringido al testbed de NANDINA Capítulo 87 y al marco administrativo, documental, temporal y experimental evaluado.

### Qué no debe aparecer

No introduzcas:

- resultados ni cifras;
- métricas concretas;
- inferencias estadísticas;
- causalidad;
- `FINAL_GAP`;
- novelty final;
- superioridad;
- ausencia universal de prior art;
- literatura externa;
- EXP-11B;
- resultados de Grupo 3;
- detalles propios de B02–B09;
- desarrollo detallado del repositorio de reproducibilidad.

### Claims autorizados

Para B01 V03:

```text
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
```

`C15` solo puede utilizarse bajo la frontera definida en B01-M08.

### Citación

Mantener:

```text
CITATION_COMMENT_COVERAGE = 0/0
```

No añadas literatura externa para resolver V03.

### Artefactos V03

No sobrescribas ni elimines V01 o V02. Genera exclusivamente:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V03.md`;
2. `article/sections/methods/Methods_B01_V03.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.docx`.

`ARTICLE_MASTER_CANDIDATE_V03.*` sigue siendo candidato y contiene únicamente B01 revisado. No crees `ARTICLE_MASTER_V001.*`.

No modifiques `ARTICLE_STATUS.md`, reviews, prompts, `DECISIONS.md`, `CLAIM_EVIDENCE_MATRIX.md`, `STYLE_GUIDE.md`, archivos de gobernanza, literatura congelada ni Plan Maestro.

### Word V03

El `.docx` debe reproducir exactamente el contenido científico de `ARTICLE_MASTER_CANDIDATE_V03.md` y conservar:

- Part I — English manuscript master;
- Part II — Spanish semantic-control mirror;
- layout neutral/reversible y editable;
- cero citas y cero comentarios de cita;
- ausencia de Mendeley o campos bibliográficos simulados.

### QA obligatorio de prosa

Antes de entregar, verificar además:

```text
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
```

### Checklist de salida

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V03
B01_M06 = ADDRESSED
B01_M07 = ADDRESSED
B01_M08 = ADDRESSED
B01_M01_M02_M03_M05 = PRESERVED_CLOSED
SOURCE_SNAPSHOT(S) = [SHAs realmente leídos]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [lista]
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS / ISSUE
POSITIONING_ORDER = GENERAL_METHOD_AND_FUNCTIONAL_CONTRACT_FIRST / CONFIGURABILITY_BOUNDARY_SECOND / NANDINA_CH87_TESTBED_THIRD
ABSTRACTION_DENSITY = ACCEPTABLE / ISSUE
AGENT_ACTION_OBJECT_CLARITY = PASS / ISSUE
NOMINALIZATION_OVERLOAD = ABSENT / ISSUE
PROCESS_RELATIONSHIPS_EXPLICIT = PASS / ISSUE
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS / ISSUE
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.md + .docx
ENGLISH_MAIN_TEXT_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW
```

No declares B01 `APPROVED` ni `FROZEN`.

---

## English

Revise only `Methods B01 — Design, scope, and units` V02. Do not advance to B02.

V03 must preserve the scientific corrections already achieved while addressing three author-mandated issues: **(1)** reduce stacked abstractions and nominalizations by using concrete agent-action-object prose; **(2)** make the complete architectural-methodological functional contract visible rather than merely listing components; and **(3)** make bounded design configurability/replicability visible, so readers understand that a study-specific labeled historical dataset, target class universe, and documentary/normative corpus can instantiate the workflow while the functional contract remains fixed.

The current empirical instance remains NANDINA Chapter 87. Configurability is a design/replication property and must never be presented as evidence of empirical generalization. `C15` is authorized only in this bounded sense. Keep `AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]`.

Do not add results, metrics, causal claims, final novelty, external literature, Group-3 results, EXP-11B claims, or later-Methods detail. Preserve B01-M01, M02, M03, and M05 as closed. Create only the four V03 artifacts listed above and end with the full checklist, including the mandatory prose-QA fields.
