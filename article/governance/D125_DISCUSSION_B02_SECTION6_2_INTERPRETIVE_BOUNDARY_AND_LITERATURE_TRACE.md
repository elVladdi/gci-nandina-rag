# D-125 — Discussion B02 / Section 6.2 interpretive boundary and literature trace

## Español

```text
DECISION = D-125
PHASE = DISCUSSION
BLOCK = DISCUSSION_B02_SECTION_6_2
SECTION = 6.2 CONTROLLED USE OF THE LLM FOR EXPLANATION
CANONICAL_SOURCE_MASTER = article/manuscript/ARTICLE_MASTER_V024.md
CANONICAL_SOURCE_MASTER_SHA256 = 0b6ea338cf325c1c59e23f91633791f97868c91eeaea44cca89f8d65c6ee7864
CANONICAL_SOURCE_MASTER_GIT_BLOB = d0ecf9f4a44b8900dd1b65f289fb0b2abf6d29c0
PRIMARY_ARCHITECTURE = Section 3.6
PRIMARY_METHODS = Sections 4.5 / 4.6.3
PRIMARY_RESULTS = Sections 5.4 / 5.7-RQ3
LITERATURE_ANCHOR_1 = Marra de Artiñano et al. 2023 / direct GPT-3.5 tariff classification
LITERATURE_ANCHOR_2 = Kim et al. 2025 / THE-RAG retrieval-conditioned HS classification
NEW_EXPERIMENTAL_RESULTS = PROHIBITED
NEW_INFERENCE = PROHIBITED
CAUSAL_SAFETY_OR_HALLUCINATION_REDUCTION_CLAIM = PROHIBITED
HUMAN_VALIDATION_CLAIM = PROHIBITED
LEGAL_CORRECTNESS_CLAIM = PROHIBITED
FAITHFUL_CAUSAL_EXPLANATION_CLAIM = PROHIBITED
NOVELTY_CLAIM = PROHIBITED
FINAL_GAP = NOT_DEFINED
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

Discussion B01 / §6.1 está cerrado e integrado bajo D-124. Discussion B02 puede interpretar únicamente la función del LLM dentro de la arquitectura ya congelada y los resultados ya integrados de RQ3. No puede recalcular resultados, introducir un nuevo experimento ni convertir la restricción de autoridad del LLM en una afirmación de seguridad, reducción de alucinaciones, mayor exactitud o superioridad global.

## Núcleo interpretativo autorizado

La discusión puede sostener que, en esta arquitectura, el LLM recibe un Top-3 y un contexto de evidencia ya fijados y tiene autoridad únicamente para generar una explicación. No puede insertar, eliminar, sustituir ni reordenar candidatos y no puede retroalimentar la clasificación. Esta restricción facilita atribuir por separado el ranking al componente histórico y la explicación al componente generativo; es una propiedad del contrato arquitectónico, no una demostración de que la explicación sea necesariamente correcta o fiel.

Los resultados de RQ3 permiten interpretar dos hechos simultáneos. Primero, los controles estructurales se preservaron en los 50/50 casos evaluados y en 150/150 candidate slots, mostrando que el LLM respetó el conjunto y orden de candidatos y las referencias exigidas en esa muestra. Segundo, solo 28/50 casos (56.0%) alcanzaron el criterio cualitativo de auditabilidad. La restricción de autoridad, por tanto, separa funciones y preserva invariantes, pero no garantiza por sí sola calidad explicativa, verificabilidad o utilidad para auditoría.

La discusión puede señalar que el perfil cualitativo refuerza esta separación: trazabilidad fue alta/completa en los controles estructurales, mientras las medias de verificabilidad (0.54/2) y separación entre evidencia histórica y normativa (1.04/2) fueron considerablemente menores. Esto permite argumentar que disponer de referencias y una traza recuperable no equivale a una explicación plenamente verificable o conceptualmente bien separada.

El resultado `schema compliance = 0/50` debe interpretarse exclusivamente como `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`: el schema exigía `advertencias_globales` y el prompt congelado no. Todos los fallos de schema se debieron a ese campo. B02 puede usarlo como lección de ingeniería sobre la necesidad de alinear prompt, schema y validadores cuando la salida generativa está contractualmente restringida; no puede presentarlo como 50 explicaciones sustantivamente inválidas.

La modalidad de evaluación limita la conclusión: el scoring cualitativo fue realizado por `independent_ai_reviewer_01` en `AI_EXPERT_ROLE` como LLM-as-judge, no por evaluadores humanos. Por tanto, la evidencia sobre auditabilidad cualitativa caracteriza conformidad con una rúbrica bajo esa modalidad de evaluación, no validación humana experta.

## Contraste funcional con literatura

Marra de Artiñano et al. (2023) se utiliza como contraste de autoridad: GPT-3.5 es consultado directamente para categorizar productos, por lo que el modelo generativo participa en la selección de la etiqueta. El presente estudio restringe el LLM a explicar candidatos fijados upstream. Esta diferencia es funcional; no autoriza afirmar que un enfoque sea globalmente mejor, más seguro o más preciso.

Kim et al. (2025) se utiliza como segundo contraste: THE-RAG combina recuperación y reranking y emplea el modelo de lenguaje como lector condicionado por contexto para la clasificación HS. En el presente estudio, el contexto recuperado alimenta una etapa explicativa posterior que no conserva autoridad de clasificación. La comparación debe limitarse a la función asignada al modelo y al lugar donde interviene en la decisión.

No introducir literatura nueva en B02 salvo verificación explícita y cobertura de comentario de cita. Las dos fuentes anteriores ya están incorporadas en Related Work y deben revalidarse antes de redactar nuevas ocurrencias en Discussion.

## Límites de interpretación

- Preservar el Top-3 ≠ producir una explicación correcta o fiel.
- Trazabilidad ≠ verificabilidad.
- Auditabilidad cualitativa bajo LLM-as-judge ≠ validación humana.
- Evidencia vinculada ≠ corrección normativa o jurídica.
- Explicación downstream ≠ reconstrucción causal del ranking upstream.
- La restricción de autoridad no demuestra reducción de alucinaciones, seguridad, mayor accuracy ni superioridad global.
- No declarar novelty, first-ever, state of the art ni `FINAL_GAP`.

## Política de citas y Word

El baseline Word integrado B01 contiene 42 comentarios. B02 podrá introducir exactamente dos nuevas ocurrencias bibliográficas en la Parte I inglesa —una para Marra de Artiñano et al. (2023) y una para Kim et al. (2025)— con exactamente dos nuevos comentarios de fuente. Los 42 comentarios heredados deben preservarse sin modificación. El candidato B02 correcto deberá terminar con:

```text
COMMENTS = 44
TRACKED_CHANGES = 0
```

Las citas equivalentes en la Parte II española no requieren comentarios adicionales. D-035 continúa activo y el Word no debe reconstruirse desde Markdown.

```text
DISCUSSION_B02_SECTION_6_2 = BOUNDED / READY_FOR_PROMPT
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

Discussion B02 may interpret only the already integrated RQ3 evidence and the frozen explanation-only role of the local LLM. The LLM receives the fixed Top-3 and candidate-linked context after ranking and documentary association have been completed; it cannot alter candidate membership/order or feed information back into classification. Structural preservation in all 50 evaluated cases can be interpreted as evidence that this authority contract was respected in the evaluated sample, but the 28/50 qualitative auditability result shows that authority restriction does not by itself guarantee explanation quality. Lower verifiability and historical-versus-normative separation scores further support the distinction between traceability and stronger forms of explanation quality. The prompt-schema mismatch must be described as a specification-interface defect, not as 50 substantively invalid explanations, and the LLM-as-judge modality must remain an explicit limitation. Functional comparison is restricted to Marra de Artiñano et al. (2023), where GPT-3.5 directly assigns tariff categories, and Kim et al. (2025), where the LLM acts as a retrieval-conditioned classifier. These contrasts concern model authority and sequencing only; no safety, hallucination-reduction, superiority, human-validation, legal-correctness, novelty, or causal-faithfulness claim is authorized.