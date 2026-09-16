# Methods B01 — Author Review V02

## Español

### Dictamen del autor

```text
AUTHOR_APPROVAL_METHODS_B01_V02 = REJECTED
REJECTION_REASON = PROSE_ABSTRACTION / CONTRIBUTION_VISIBILITY / CONFIGURABILITY_VISIBILITY
MATERIAL_SCIENTIFIC_ERROR = NO
METHODS_B01 = REVISION_REQUIRED
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

La V02 resolvió correctamente el orden de posicionamiento exigido en B01-M05: primero presenta la arquitectura general y después NANDINA Capítulo 87 como testbed. Sin embargo, el autor no aprueba todavía el bloque porque la prosa permanece excesivamente abstracta y contractual y porque el aporte metodológico completo todavía no queda suficientemente visible para el lector.

### Correcciones obligatorias para V03

#### B01-M06 — Reducir abstracciones y nominalizaciones acumuladas

La V02 concentra formulaciones como `auditable decision-support architecture`, `candidate ranking`, `normative-evidence retrieval`, `downstream explanation`, `dependence structure`, `query representation` y `output object` sin suficiente desarrollo verbal y concreto. Estas expresiones son válidas como terminología técnica, pero su acumulación vuelve la prosa rígida y cercana a una especificación de arquitectura.

V03 debe conservar precisión científica, pero privilegiar oraciones en las que quede claro **qué componente hace qué, sobre qué entrada y con qué restricción**. Debe reducir cadenas de sustantivos abstractos, nominalizaciones innecesarias y enumeraciones conceptuales comprimidas. Esta regla se incorpora también a la guía de estilo para los bloques posteriores.

#### B01-M07 — Hacer visible el aporte arquitectónico-metodológico completo

La V03 no debe limitarse a describir tres componentes separados. El lector debe entender que el artículo formaliza y evalúa un **contrato funcional completo**: el ranking histórico fija los candidatos; la recuperación normativa aporta evidencia sin alterar ese ranking; el LLM local explica un Top-3 inmutable sin insertar, eliminar, sustituir, reordenar ni retroalimentar la clasificación; y la evaluación se organiza por función.

Esto debe presentarse como objeto metodológico del estudio, sin convertirlo en un claim final de novelty, superioridad o ausencia de prior art y sin introducir métricas o resultados de secciones posteriores.

#### B01-M08 — Hacer visible la configurabilidad/replicabilidad sin afirmar generalización empírica

El lector debe comprender que la arquitectura está concebida para poder ser instanciada con recursos propios del estudio o de una replicación: un banco histórico/dataset etiquetado, un universo de clases objetivo y un corpus documental o normativo apropiado al dominio. En el artículo actual, esa instancia se evalúa con NANDINA Capítulo 87 y con los recursos versionados del piloto.

Esta propiedad debe expresarse únicamente como **configurabilidad/replicabilidad de diseño**, nunca como evidencia de que el desempeño observado se generaliza a otros datasets, clases, capítulos, niveles, jurisdicciones o corpus. Debe respetarse expresamente la frontera `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

Para B01 V03 queda autorizado el uso acotado de `C15` exclusivamente con esta finalidad. Los detalles operativos del banco histórico, corpus normativo y repositorio de reproducibilidad corresponden a las subsecciones posteriores de Methods y no deben anticiparse aquí en detalle.

### Contenido que debe preservarse

- B01-M01, B01-M02, B01-M03 y B01-M05 permanecen cerrados y no deben reintroducirse los problemas que corrigieron.
- Mantener la secuencia `arquitectura general → contrato funcional → testbed NANDINA Capítulo 87 → alcance y unidades`.
- Mantener apoyo a decisión no vinculante y revisión experta fuera del flujo automático.
- Mantener SERIE como unidad de observación/análisis y DAM como unidad de agrupamiento cuando la dependencia sea metodológicamente relevante.
- No introducir resultados, cifras, métricas inferenciales, causalidad, novelty final, literatura externa ni contenido de B02–B09.

### Estado posterior al rechazo

```text
B01_M06 = REVISION_REQUIRED
B01_M07 = REVISION_REQUIRED
B01_M08 = REVISION_REQUIRED
AUTHOR_APPROVAL_METHODS_B01_V02 = REJECTED
METHODS_B01 = REVISION_REQUIRED
NEXT_ACTOR = DRAFTING_AI
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

```text
AUTHOR_APPROVAL_METHODS_B01_V02 = REJECTED
REJECTION_REASON = PROSE_ABSTRACTION / CONTRIBUTION_VISIBILITY / CONFIGURABILITY_VISIBILITY
MATERIAL_SCIENTIFIC_ERROR = NO
METHODS_B01 = REVISION_REQUIRED
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
```

V02 correctly fixed the positioning order required by B01-M05, but the author does not approve the block yet. V03 must reduce stacked abstractions and nominalizations, make the complete architectural-methodological contract visible rather than merely listing components, and state the design's configurability/replicability in a bounded way. The reader should understand that the workflow can be instantiated with a study-specific labeled historical dataset, target class universe, and documentary/normative corpus, while the present empirical evaluation remains restricted to NANDINA Chapter 87. This is a design/replication property, not evidence of empirical generalization.

`C15` is authorized for B01 V03 only within that bounded design-property meaning. No novelty, superiority, universal prior-art absence, external generalization, results, metrics, or later-Methods content may be introduced.
