# Methods B01 V03 — Reauditoría editorial KBS-34 / KBS-34 Editorial Reaudit

## Español

### Dictamen

```text
REVIEW_ID = METHODS_B01_KBS_REAUDIT_V03
BASIS = KBS_EWG_34_V01 + KBS_34_EPM_V01
GUIDE_APPROVAL = D-013
SCIENTIFIC_CONTENT_REVIEW = PREVIOUS_PASS_RETAINED
MATERIAL_SCIENTIFIC_ERRORS = 0
KBS_EDITORIAL_FIT = PASS_WITH_CORRECTIONS
AUTHOR_REVIEW_READY = NO
B01_M09 = OPEN / DOCX_PACKAGE_INTEGRITY
B01_M10 = OPEN / ARCHITECTURE_OVERVIEW_DENSITY
B01_M11 = OPEN / ABSTRACT_NOMINALIZATION_AND_CONTRACT_LANGUAGE
B01_M12 = OPEN / CONFIGURABILITY_PRECONDITIONS
B01_M13 = OPEN / TESTBED_BOUNDARY_CONCRETENESS
B02 = NOT_AUTHORIZED
```

### Alcance de la reauditoría

Esta revisión no reabre el contenido científico ya validado en V03. Examina exclusivamente si la prosa y la organización de `Methods 3.1` alcanzan el estándar editorial empírico aprobado para *Knowledge-Based Systems* mediante D-013.

La V03 mejoró materialmente respecto de V02: abre con el método general, mantiene el Top-3 fijo, separa ranking/evidencia/explicación, delimita la configurabilidad frente a la generalización y coloca NANDINA Chapter 87 como testbed. Esas correcciones permanecen válidas.

Sin embargo, el nuevo estándar KBS-34 muestra que el bloque todavía puede escribirse de forma más natural, concreta y editorialmente eficiente.

### B01-M10 — Densidad excesiva en la vista arquitectónica inicial

**Problema:** el primer párrafo intenta, al mismo tiempo, introducir el flujo completo, describir las funciones de los tres componentes, enumerar todas las prohibiciones del LLM y formular el contrato funcional. Para una subsección de diseño/alcance, la densidad es mayor que la observada en los artículos KBS de referencia, que suelen introducir primero el flujo principal y desplazar restricciones finas al componente correspondiente.

**Corrección obligatoria:** conservar en 3.1 la secuencia operacional y las dos invariantes centrales —Top-3 fijado antes de la recuperación normativa y ausencia de retroalimentación del LLM hacia el ranking—, pero trasladar la enumeración detallada de inserción/eliminación/sustitución/reordenamiento a las subsecciones posteriores previstas para invariancia y explicación (`3.6–3.7`). No añadir contenido de esas subsecciones; solo evitar duplicarlo exhaustivamente en 3.1.

### B01-M11 — Lenguaje aún demasiado contractual/abstracto

**Problema:** expresiones como `fixed sequence of responsibilities`, `functional contract evaluated in the study` y su acumulación en un mismo párrafo hacen que el texto conserve parcialmente el tono de una especificación de gobernanza. `Functional contract` puede mantenerse como término científico central, pero debe definirse a partir de acciones observables y usarse con moderación.

**Corrección obligatoria:** priorizar agente–acción–objeto. La subsección debe decir qué recibe cada etapa, qué hace y qué entrega. Utilizar `functional contract` como síntesis después de haber descrito esas operaciones, no como sustituto de ellas.

### B01-M12 — Configurabilidad sin precondiciones suficientes

**Problema:** la frase `can be instantiated with ...` comunica correctamente la intención general, pero puede leerse como una capacidad plug-and-play irrestricta. La guía KBS-34 exige que la configurabilidad se formule junto con sus interfaces o precondiciones, sin convertirla en generalización empírica.

**Corrección obligatoria:** formular que el workflow está diseñado para recibir recursos definidos por cada dominio/estudio —banco histórico etiquetado, universo de clases objetivo y corpus documental compatible— siempre que se satisfagan las interfaces de representación/identificación necesarias. Los requisitos detallados pueden quedar diferidos a `3.2` y `3.9`. Mantener explícitamente `configurability/replicability ≠ empirical generalization`.

### B01-M13 — Delimitación del testbed todavía abstracta

**Problema:** `administrative, documentary, temporal, and experimental conditions` enumera categorías de alcance sin decir al lector qué debe retener en este punto.

**Corrección obligatoria:** reemplazar esa lista por una delimitación concreta y compacta: los resultados empíricos corresponden al piloto offline de NANDINA Chapter 87 y a las versiones de datos/corpus/configuración utilizadas en dicho piloto. Los detalles de procedencia, versionado, drift y reproducibilidad pertenecen a subsecciones posteriores.

### Elementos que deben preservarse

- método general antes del testbed;
- ranking histórico como generador de candidatos;
- Top-3 fijo antes de recuperación normativa;
- recuperación normativa sin reranking;
- LLM posterior y sin feedback al ranking;
- evaluación funcionalmente separada;
- NANDINA Chapter 87 como testbed, no como alcance conceptual total;
- unidad de observación/análisis = series record;
- DAM como grouping unit cuando corresponda por dependencia;
- consulta = descripción comercial normalizada;
- configurabilidad delimitada, sin claim de generalización empírica.

### Consecuencia de versionado

El prompt V04 de reparación exclusiva de DOCX queda supersedido antes de ejecución por D-013. La siguiente entrega debe combinar la corrección editorial KBS con la reparación técnica del Word. Para evitar reutilizar un identificador ya emitido con otro alcance, la siguiente revisión será **V05**.

---

## English

### Verdict

```text
REVIEW_ID = METHODS_B01_KBS_REAUDIT_V03
BASIS = KBS_EWG_34_V01 + KBS_34_EPM_V01
GUIDE_APPROVAL = D-013
SCIENTIFIC_CONTENT_REVIEW = PREVIOUS_PASS_RETAINED
MATERIAL_SCIENTIFIC_ERRORS = 0
KBS_EDITORIAL_FIT = PASS_WITH_CORRECTIONS
AUTHOR_REVIEW_READY = NO
B01_M09 = OPEN / DOCX_PACKAGE_INTEGRITY
B01_M10 = OPEN / ARCHITECTURE_OVERVIEW_DENSITY
B01_M11 = OPEN / ABSTRACT_NOMINALIZATION_AND_CONTRACT_LANGUAGE
B01_M12 = OPEN / CONFIGURABILITY_PRECONDITIONS
B01_M13 = OPEN / TESTBED_BOUNDARY_CONCRETENESS
B02 = NOT_AUTHORIZED
```

This review does not reopen the scientific content already validated in V03. It assesses whether Methods 3.1 meets the KBS-specific empirical editorial standard approved through D-013.

V03 materially improved over V02 and correctly preserves the general-method-first positioning, the fixed Top-3, the separation of ranking/evidence/explanation, bounded configurability, and Chapter 87 as the testbed. Those corrections remain valid.

Four editorial corrections remain. First, the opening architecture paragraph is too dense because it combines the full flow, all component roles, the full prohibition list, and the functional-contract statement. Second, contractual abstractions such as `fixed sequence of responsibilities` and repeated `functional contract` language should be reduced in favor of explicit agent–action–object prose. Third, configurability must be stated together with the representation/interface preconditions required for a new dataset, class universe, and documentary corpus. Fourth, the testbed boundary should be expressed concretely as the Chapter 87 offline pilot and the versions of data/corpus/configuration used in that pilot rather than as an abstract list of administrative, documentary, temporal, and experimental conditions.

The next revision must preserve all validated scientific boundaries while correcting B01-M09 through B01-M13. Because the previously issued V04 prompt was limited to DOCX repair and is superseded before execution, the next revision identifier is V05. `B02` remains unauthorized.
