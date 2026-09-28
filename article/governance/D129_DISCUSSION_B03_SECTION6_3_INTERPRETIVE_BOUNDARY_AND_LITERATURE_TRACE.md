# D-129 — Discussion B03 / Section 6.3 interpretive boundary and literature trace

## Español

```text
DECISION = D-129
PHASE = DISCUSSION
BLOCK = DISCUSSION_B03_SECTION_6_3
SECTION = 6.3 COMPARISON WITH PRIOR WORK
CANONICAL_SOURCE_MASTER = article/manuscript/ARTICLE_MASTER_V025.md
CANONICAL_SOURCE_MASTER_SHA256 = a805cd220904fb4972d0db59764425aff87a49c8ec1cd34936e85913778feee5
CANONICAL_SOURCE_MASTER_GIT_BLOB = 829a6f5df87cf91dcafe89c48c1afd48ddbd2faf
PRIMARY_POSITIONING = Section 2.6
PRIMARY_DISCUSSION_INPUTS = Sections 6.1 / 6.2
PRIMARY_RESULTS_INPUTS = Sections 5.2 / 5.3 / 5.4 / 5.7
LITERATURE_ANCHOR_1 = Lee et al. 2021
LITERATURE_ANCHOR_2 = Lee et al. 2023
LITERATURE_ANCHOR_3 = Marra de Artinano et al. 2023
LITERATURE_ANCHOR_4 = Kim et al. 2025
NEW_LITERATURE = PROHIBITED_UNLESS_SEPARATELY_VERIFIED
CROSS_STUDY_NUMERICAL_COMPARISON = PROHIBITED
STATE_OF_THE_ART_CLAIM = PROHIBITED
GLOBAL_SUPERIORITY_CLAIM = PROHIBITED
NOVELTY_CLAIM = PROHIBITED
FIRST_EVER_CLAIM = PROHIBITED
LEGAL_CORRECTNESS_CLAIM = PROHIBITED
FINAL_GAP = NOT_DEFINED
DISCUSSION_B04_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

Discussion B03 debe comparar el estudio con antecedentes ya verificados sin reabrir Related Work ni introducir literatura nueva. La comparación se organiza por función y autoridad de los componentes, no por porcentajes de desempeño entre datasets heterogéneos.

Lee et al. (2021) sirve para contrastar un pipeline en el que el material recuperado participa en una decisión posterior de clasificación. Lee et al. (2023) es el antecedente más próximo para candidate prediction seguida de evidencia documental; por tanto, candidate prediction + evidence retrieval no puede presentarse como una novedad del presente estudio.

Marra de Artiñano et al. (2023) sirve como contraste de clasificación generativa directa, donde el modelo generativo produce la etiqueta. Kim et al. (2025) sirve como contraste de clasificación HS condicionada por retrieval/reranking y un LLM con función decisoria dentro del pipeline. Frente a ambos, el LLM del presente estudio está restringido a una etapa downstream de explicación de candidatos fijados upstream.

La comparación autorizada del presente estudio se limita al contrato operativo completo ya integrado: ranking histórico que fija el Top-3 antes de la evidencia documental; asociación documental que no modifica composición ni orden; LLM downstream sin autoridad de clasificación; y evaluación separada de candidate retrieval, documentary association y controlled explanation. Esta combinación se puede describir como el posicionamiento metodológico del estudio, pero no como novelty demostrada, first-ever, state of the art ni superioridad global.

No se permiten comparaciones numéricas directas entre estudios porque difieren datasets, espacios de clases, profundidad arancelaria, tareas, protocolos y métricas. Los resultados internos del presente estudio pueden mencionarse solo para mostrar que el contrato de separación fue efectivamente evaluado, no para inferir superioridad externa.

## Política de citas y Word

El baseline Word integrado B02 contiene 44 comentarios. B03 podrá introducir exactamente cuatro nuevas ocurrencias bibliográficas en la Parte I inglesa, una por cada fuente autorizada: Lee et al. (2021), Lee et al. (2023), Marra de Artiñano et al. (2023) y Kim et al. (2025). Deben añadirse exactamente cuatro nuevos comentarios de fuente y preservarse sin cambios los 44 heredados.

```text
EXPECTED_COMMENTS_AFTER_B03 = 48
TRACKED_CHANGES = 0
```

Las citas equivalentes de la Parte II española no requieren comentarios adicionales. D-035 permanece activo; el Word no debe reconstruirse desde Markdown.

```text
DISCUSSION_B03_SECTION_6_3 = BOUNDED / READY_FOR_PROMPT
DISCUSSION_B04_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
NOVELTY = NOT_DECLARED
```

---

## English

Discussion B03 compares the already integrated framework with four previously verified prior-work anchors. Lee et al. (2021) represents retrieved documentary material entering a later classification decision; Lee et al. (2023) represents candidate prediction followed by evidence retrieval and is therefore close prior art rather than evidence of novelty. Marra de Artiñano et al. (2023) represents direct generative tariff classification, while Kim et al. (2025) represents retrieval-conditioned LLM-based HS classification. The present study may be positioned through its explicit non-overlapping authority contract and separate evaluation of ranking, documentary association, and explanation. This positioning is methodological only. No cross-study numerical superiority, state-of-the-art, first-ever, novelty, legal-correctness, or global-superiority claim is authorized. Exactly four new English citation comments are permitted, taking the cumulative Word count from 44 to 48.