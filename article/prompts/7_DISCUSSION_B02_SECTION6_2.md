# Prompt — Discussion B02 / Section 6.2 — Controlled use of the LLM for explanation

## Español

### Rol

Actúa exclusivamente como IA de Redacción del manuscrito. No cambies gobernanza, no recalcules resultados, no declares novelty y no avances fuera del bloque autorizado.

### Autorización

Ejecuta únicamente Discussion B02 V01 / Section 6.2 bajo:

`article/governance/D125_DISCUSSION_B02_SECTION6_2_INTERPRETIVE_BOUNDARY_AND_LITERATURE_TRACE.md`

Usa exclusivamente como baseline Markdown:

`article/manuscript/ARTICLE_MASTER_V024.md`

Identidad congelada:

```text
SHA256 = 0b6ea338cf325c1c59e23f91633791f97868c91eeaea44cca89f8d65c6ee7864
GIT_BLOB = d0ecf9f4a44b8900dd1b65f289fb0b2abf6d29c0
```

Usa como baseline Word exclusivamente el archivo acumulativo aprobado:

`ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.docx`

```text
SHA256 = cc0bb87adacbfbca7403335f6a1070acf27f04b05c2d6a8772b0608c3923f0e0
COMMENTS = 42
TRACKED_CHANGES = 0
PAGE_COUNT = 60
```

No reconstruyas Word desde Markdown. D-035 sigue vigente: no Base64 manual, chunking, fragmentación ni reensamblado.

### Fuentes científicas obligatorias

Interpreta exclusivamente evidencia ya integrada de:

- Section 3.6 — Evidence-context construction and controlled explanation.
- Section 4.5 — configuración real del LLM y contrato del prompt.
- Section 4.6.3 — protocolo de evaluación de explicación.
- Section 5.4 — resultados estructurales y cualitativos de RQ3.
- Section 5.7 — síntesis RQ3.

Revalida antes de citar las dos fuentes de literatura ya incorporadas en Related Work:

1. Marra de Artiñano et al. (2023): uso de GPT-3.5 como clasificador/categorizador directo de productos.
2. Kim et al. (2025): THE-RAG, donde recuperación/reranking alimentan un LLM que participa como lector/decisor condicionado por contexto para clasificación HS.

No introduzcas nueva literatura salvo que sea indispensable, esté completamente verificada y se documente su soporte. La opción preferida es no introducir ninguna fuente adicional.

### Función editorial de §6.2

La sección debe interpretar el valor y los límites de restringir al LLM a explicación downstream. Debe explicar que la arquitectura separa autoridad: ranking y Top-3 se fijan antes; el LLM recibe candidatos y evidencia ya construidos y no puede modificar membership, orden ni clasificación.

No repitas Results de forma exhaustiva. Utiliza solo las cifras necesarias para sostener la interpretación.

### Contenido obligatorio

Redacta una Section 6.2 compacta, aproximadamente 350–450 palabras en inglés, seguida de una versión española semánticamente equivalente. Usa preferentemente cinco párrafos por idioma con esta función:

1. **Restricción de autoridad.** Explica que el LLM es un generador de explicación sobre un objeto ya fijado, no un clasificador ni reranker. Relaciona esta decisión con atribución por componente, sin afirmar causalidad o superioridad.
2. **Contraste funcional con literatura.** Cita exactamente una vez en el texto inglés a Marra de Artiñano et al. (2023) y exactamente una vez a Kim et al. (2025). Contrasta únicamente la autoridad asignada al LLM y el punto del pipeline donde interviene. No hagas comparaciones numéricas entre estudios.
3. **Qué sí muestran los controles estructurales.** Interpreta que 50/50 casos preservaron Top-3/orden/controles estructurales y que 150/150 candidate slots conservaron las referencias/rank consistency pertinentes. Esto demuestra cumplimiento del contrato en la muestra evaluada, no calidad explicativa completa.
4. **Qué no garantiza la restricción.** Integra que solo 28/50 casos (56.0%) alcanzaron el criterio cualitativo de auditabilidad; trazabilidad fue fuerte, mientras verificabilidad (0.54/2) y separación histórico–normativa (1.04/2) fueron más débiles. Explica que trazabilidad ≠ verificabilidad y que una explicación downstream puede seguir siendo insuficiente para revisión experta.
5. **Contrato de salida y límite de evaluación.** Interpreta `schema compliance = 0/50` exclusivamente como `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` por `advertencias_globales`, no como 50 explicaciones inválidas. Expón la necesidad de alinear prompt/schema/validators y recuerda que el scoring cualitativo fue LLM-as-judge, no humano.

### Claims permitidas

Puedes sostener:

- el LLM no tuvo autoridad para cambiar el Top-3 ni retroalimentar clasificación;
- los 50/50 casos evaluados respetaron el conjunto/orden y los controles estructurales reportados;
- 28/50 casos cumplieron el criterio cualitativo congelado de auditabilidad;
- la restricción de autoridad facilita atribución de outputs a componentes separados;
- trazabilidad y preservación estructural no equivalen a verificabilidad, corrección, validación humana o fidelidad causal;
- el mismatch prompt-schema es un problema de especificación/interfaz que debe distinguirse de calidad sustantiva de explicación.

### Claims prohibidas

No afirmar ni implicar:

- que la restricción del LLM reduce alucinaciones;
- que hace al sistema más seguro, más exacto o más confiable en sentido global;
- que 50/50 demuestra calidad o validez jurídica;
- que 28/50 constituye validación humana;
- que la explicación es fiel al mecanismo causal que produjo el ranking;
- que el framework completo supera a Marra de Artiñano et al. o Kim et al.;
- novelty, first-ever, state of the art o `FINAL_GAP`;
- overall classification accuracy;
- substantive normative correctness o legal correctness;
- nuevos resultados, intervalos, p-values o tests.

### Política de citas y comentarios Word

En la Parte I inglesa introduce exactamente dos nuevas ocurrencias bibliográficas:

- una de Marra de Artiñano et al. (2023);
- una de Kim et al. (2025).

Cada una debe tener exactamente un comentario de cita nuevo con soporte claim–fuente y límites de interpretación. Preserva sin modificación los 42 comentarios heredados.

Resultado esperado:

```text
COMMENTS = 44
TRACKED_CHANGES = 0
```

La Parte II española puede contener las mismas dos referencias bibliográficas, pero no debe añadir comentarios de cita adicionales.

### Diferencial autorizado

Modifica exclusivamente los placeholders inglés y español de Section 6.2.

Debe permanecer byte/content-preserved, salvo reflow Word inevitable:

- Front matter.
- Sections 1–5.7.
- Discussion §6.1.
- Discussion §6.3–§6.6.
- Conclusion.
- End matter.

### Entregables

1. `article/sections/discussion/Discussion_B02_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx`
4. `article/responses/7_DISCUSSION_B02_SECTION6_2_RESPONSE_V01.md`

La response debe declarar identidades SHA-256, Git blob esperado del Markdown acumulativo, auditoría diferencial, equivalencia EN/ES, estado de comentarios/citas, OOXML, render completo y D-035.

Detente al completar §6.2. No avances a §6.3 ni a Conclusion.

```text
EXPECTED_EXIT = DISCUSSION_B02_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Draft only Discussion Section 6.2 against canonical V024 and the approved B01 Word baseline. Interpret the local LLM as an explanation-only downstream component with no authority to change the fixed Top-3. Contrast its authority functionally, not numerically, with Marra de Artiñano et al. (2023) direct generative classification and Kim et al. (2025) retrieval-conditioned HS classification. Use the integrated RQ3 evidence to distinguish structural preservation from qualitative auditability: 50/50 structural preservation does not guarantee explanation quality, and 28/50 qualitative auditability plus low verifiability/evidence-separation scores must remain visible. Treat the 0/50 schema result only as the frozen prompt-schema mismatch. The qualitative evaluator was LLM-as-judge, not human. Exactly two new English citation comments are authorized, taking the Word comment count from 42 to 44. No §6.3+, Conclusion, novelty, safety, hallucination-reduction, superiority, legal-correctness, or causal-faithfulness claim is authorized.