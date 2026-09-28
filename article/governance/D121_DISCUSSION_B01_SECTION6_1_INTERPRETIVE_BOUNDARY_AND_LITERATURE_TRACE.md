# D-121 — Discussion B01 / Section 6.1 interpretive boundary and literature trace

## Español

```text
DECISION = D-121
PHASE = DISCUSSION
BLOCK = DISCUSSION_B01_SECTION_6_1
SECTION = 6.1 SEPARATING CANDIDATE RANKING FROM DOCUMENTARY EVIDENCE
CANONICAL_SOURCE_MASTER = article/manuscript/ARTICLE_MASTER_V023.md
CANONICAL_SOURCE_MASTER_SHA256 = d3a54bd263f8f24690fa259eb732e4805515899f0219b6b822b4978e9b985446
CANONICAL_SOURCE_MASTER_GIT_BLOB = 657c85211323ba60a65d54cccb31edb90c0d18c3
PRIMARY_RESULTS = Sections 5.2 / 5.3 / 5.6 / 5.7
PRIMARY_ARCHITECTURE = Sections 3.3 / 3.4 / 3.5
LITERATURE_ANCHOR_1 = Lee et al. 2021 / Classification of Goods Using Text Descriptions With Sentences Retrieval
LITERATURE_ANCHOR_2 = Lee et al. 2023 / Explainable Product Classification for Customs
NEW_EXPERIMENTAL_RESULTS = PROHIBITED
CROSS_DATASET_NUMERICAL_SUPERIORITY = PROHIBITED
NOVELTY_CLAIM = PROHIBITED
FINAL_GAP = NOT_DEFINED
CONCLUSION = NOT_AUTHORIZED
```

Results §5.1–§5.7 está cerrado e integrado bajo D-120. Discussion B01 puede interpretar únicamente evidencia ya congelada y compararla con literatura previamente incorporada y verificable; no puede recalcular resultados ni convertir diferencias de arquitectura en una declaración de novelty.

## Núcleo interpretativo autorizado

La discusión puede sostener que el resultado empírico y arquitectónico del estudio es coherente con una separación explícita de autoridad entre etapas: el ranking histórico produce y fija candidatos, y la etapa documental enriquece esos candidatos sin modificar membership, orden ni score histórico. En el piloto, la asociación documental exacta alcanzó 3,168/3,168 candidate slots y preservó el Top-3 en 1,056/1,056 casos. Estas cifras pertenecen a Results; en Discussion deben utilizarse como soporte de una interpretación metodológica, no repetirse exhaustivamente.

La comparación con Lee et al. (2021) debe ser funcional: ese trabajo predice primero un heading, recupera oraciones del HS manual y utiliza después la descripción junto con esas oraciones para predecir el subheading. Por tanto, la evidencia recuperada participa en la decisión posterior de clasificación. No afirmar que dicho diseño sea inferior; simplemente señalar que asigna una autoridad distinta a la evidencia documental.

La comparación con Lee et al. (2023) debe reconocerlo como antecedente cercano: el modelo primero predice candidatos de clasificación y después recupera evidencia sobre cada candidato desde el HS manual. La diferencia interpretativa permitida es que el presente estudio formaliza y evalúa como contrato explícito que, una vez fijado el Top-3 histórico, la etapa documental no puede insertar, eliminar, sustituir ni reordenar candidatos, y evalúa ranking y asociación documental como objetos separados. Esto describe una diferencia metodológica/operativa; no constituye por sí sola una claim de novelty.

## Literatura verificada

Los dos anclajes anteriores están ya citados en Related Work y en Introduction. La fuente 2021 establece una secuencia de tres etapas en la cual las oraciones recuperadas del manual se concatenan con la descripción para la predicción de subheading. La fuente 2023 establece una secuencia de dos etapas: predicción de clasificación seguida de recuperación de evidencia sobre cada candidato. No introducir literatura nueva en B01 salvo verificación explícita y cobertura de comentario de cita.

## Límites de interpretación

- Candidate retrieval ≠ overall classification accuracy.
- Documentary association ≠ substantive normative correctness.
- Traceability/invariance ≠ legal correctness.
- Los porcentajes de otros trabajos no son comparables directamente con los resultados NANDINA-8 del piloto por diferencias de dataset, espacio de clases, nivel arancelario, tarea y protocolo.
- No afirmar que el framework completo sea superior a Lee et al. (2021) o Lee et al. (2023).
- No usar lenguaje de causalidad para atribuir resultados a la separación de autoridad.
- No declarar novelty, first-ever, state of the art ni FINAL_GAP.

## Forma editorial

Section 6.1 debe interpretar antes que repetir. Una forma adecuada es: (1) significado de fijar el ranking antes de la evidencia; (2) contraste funcional con Lee et al. 2021 y 2023; (3) qué permite evaluar/atribuir esta separación en el presente piloto; (4) límite: evidencia identificable y ranking invariante no equivalen a corrección jurídica.

El bloque debe ser compacto, sin abrir todavía §6.2–§6.6. Las citas nuevas en el texto inglés deben conservar la política MWDP de comentarios de fuente. Si se reutilizan Lee et al. (2021) y Lee et al. (2023), reutilizar la identidad bibliográfica y el soporte ya verificados; no inventar metadatos.

```text
DISCUSSION_B01_SECTION_6_1 = BOUNDED / READY_FOR_PROMPT
DISCUSSION_B02_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

Discussion B01 may interpret only already integrated results. Section 6.1 should explain the methodological value of fixing candidate ranking before documentary association and compare that authority structure with two verified close precedents. Lee et al. (2021) retrieve HS-manual sentences after heading prediction and then use those sentences together with the product description to predict the subheading; retrieved evidence therefore participates in a later classification decision. Lee et al. (2023) provide a closer two-stage precedent in which classification candidates are predicted first and evidence is then retrieved for each candidate. The present study may be distinguished only by its explicit fixed-Top-3 authority contract and its separate evaluation of ranking versus documentary association. This is a methodological/operational distinction, not a novelty claim. No cross-dataset numerical superiority, causal claim, overall-system accuracy, legal correctness, new result, or downstream Discussion/Conclusion content is authorized.