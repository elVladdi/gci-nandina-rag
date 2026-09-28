# Discussion B01 V01 — Section 6.1 / Sección 6.1

## English

### 6.1. Separating candidate ranking from documentary evidence

Fixing the historical Top-3 before documentary association establishes an explicit boundary of authority between stages. Historical retrieval determines candidate membership and order; the documentary stage can only attach evidence to those fixed candidates. In the pilot, exact NANDINA-8 association was available for all 3,168 candidate slots, and the documentary stage preserved Top-3 membership and order in all 1,056 evaluation cases. These observations confirm that the implemented documentary stage respected the fixed-ranking contract.

That authority structure differs functionally from the staged design of Lee et al. (2021), in which the model first predicts a four-digit heading, retrieves key sentences from the HS manual, and then predicts the six-digit subheading from the product description together with the retrieved sentences. In that pipeline, documentary retrieval contributes input to a later classification decision. The difference relevant here is therefore the role assigned to retrieved evidence, not a claim that one design is generally better than the other.

A closer precedent is Lee et al. (2023), whose model first predicts item classification candidates and then retrieves evidence about each candidate from the HS manual. The present study adopts a similar high-level ordering but makes the downstream authority restriction explicit: once historical retrieval fixes the Top-3, later stages cannot insert, delete, substitute, or reorder candidates. It also evaluates candidate ranking and documentary association separately. This distinction is methodological and operational.

The separation also defines what can be attributed to each evaluation object. Top-k and MRR values characterize the historical candidate-retrieval stage that produced the ranking, whereas documentary coverage, association, provenance, and traceability characterize a downstream stage that cannot alter that ranking. Reporting these outputs separately therefore supports component-level attribution without implying that the separation itself caused the observed retrieval performance.

The same boundary makes the normative and legal limit explicit. Complete documentary association and ranking invariance show that identifiable material can be attached to fixed candidates without changing them; they do not show that the retrieved material is the controlling or legally sufficient authority, that a candidate is substantively correct under the nomenclature, or that the final recommendation is legally valid. Those questions require a different form of adjudication and remain outside the evidential scope of this offline pilot.

## Español

### 6.1. Separación entre ranking de candidatos y evidencia documental

Fijar el Top-3 histórico antes de la asociación documental establece una frontera explícita de autoridad entre etapas. La recuperación histórica determina la composición y el orden de los candidatos; la etapa documental solo puede asociar evidencia con esos candidatos ya fijados. En el piloto, la asociación exacta NANDINA-8 estuvo disponible para las 3.168 posiciones de candidato, y la etapa documental preservó la composición y el orden del Top-3 en los 1.056 casos de evaluación. Estas observaciones confirman que la etapa documental implementada respetó el contrato de ranking fijo.

Esa estructura de autoridad difiere funcionalmente del diseño por etapas de Lee et al. (2021), en el que el modelo primero predice una partida de cuatro dígitos, recupera oraciones clave del manual HS y después predice la subpartida de seis dígitos a partir de la descripción del producto junto con las oraciones recuperadas. En ese flujo, la recuperación documental aporta entradas a una decisión posterior de clasificación. La diferencia relevante aquí es, por tanto, la función asignada a la evidencia recuperada, no una afirmación de que un diseño sea en general mejor que el otro.

Un antecedente más cercano es Lee et al. (2023), cuyo modelo primero predice candidatos de clasificación y luego recupera del manual HS evidencia sobre cada candidato. El presente estudio adopta un orden general similar, pero hace explícita la restricción de autoridad de las etapas posteriores: una vez que la recuperación histórica fija el Top-3, esas etapas no pueden insertar, eliminar, sustituir ni reordenar candidatos. Además, evalúa por separado el ranking de candidatos y la asociación documental. Esta distinción es metodológica y operativa.

La separación también delimita qué puede atribuirse a cada objeto de evaluación. Los valores Top-k y MRR caracterizan la etapa de recuperación histórica de candidatos que produjo el ranking, mientras que la cobertura documental, la asociación, la procedencia y la trazabilidad caracterizan una etapa posterior que no puede modificar ese ranking. Reportar estas salidas por separado permite, por tanto, una atribución a nivel de componente sin implicar que la separación haya causado el desempeño de recuperación observado.

La misma frontera hace explícito el límite normativo y jurídico. La asociación documental completa y la invariancia del ranking muestran que puede vincularse material identificable con candidatos fijos sin modificarlos; no demuestran que el material recuperado sea la fuente normativa determinante o jurídicamente suficiente, que un candidato sea sustantivamente correcto bajo la nomenclatura ni que la recomendación final sea jurídicamente válida. Esas cuestiones requieren otra forma de adjudicación y permanecen fuera del alcance evidencial de este piloto offline.
