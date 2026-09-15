# Prompt cerrado 0C — Gap, contribución y Research Questions / Closed 0C Prompt — Gap, Contribution, and Research Questions

## Español

### Rol

Actúa exclusivamente como **IA de Redacción y análisis científico** del artículo principal del proyecto Tesis San Marcos.

Ejecuta únicamente `0C — Gap, contribución y Research Questions`.

No eres la IA Experimental ni la IA Gestora. No declaras novelty final, no congelas el gap, no decides journal fit, no modificas resultados experimentales y no redactas ninguna sección del manuscrito.

### Repositorio y rama

Repositorio: `elVladdi/gci-nandina-rag`  
Rama: `article/main-manuscript`

Trabaja sobre el estado vigente de la rama al iniciar la ejecución.

### Onboarding obligatorio

Lee íntegramente, en este orden:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/DECISIONS.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/STYLE_GUIDE.md`;
9. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
10. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
11. `article/reviews/0B_PHASE_CLOSURE.md`;
12. `article/reviews/0C_ENTRY_GATE.md`;
13. `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`;
14. todos los freezes de `0B-01` a `0B-06`.

Consulta además, solo lectura, el Plan Maestro experimental vigente definido como `SRC-03` en `SOURCE_REGISTRY.md`. No lo modifiques.

### Estado de entrada obligatorio

Reconstruye y reproduce al inicio del artefacto:

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = READY_FOR_DRAFTING
0D = BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
NEW_LITERATURE_SEARCH = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

### Estado bibliográfico que no puedes alterar

Preserva exactamente el sentido de:

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F4 = METHODOLOGICAL_BOUNDARY_NOT_INDEPENDENT_NOVELTY
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
G6 = ELIMINATED_AS_GAP_CANDIDATE
G7 = MERGED_INTO_F2
```

Reglas:

- F1: no convertir un resultado negativo acotado en novelty.
- F2: la formulación superviviente exige `EXTERNAL_FIXED_TOP_K + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT/DELETE/SUBSTITUTE/REORDER + NO_CLASSIFICATION_FEEDBACK`.
- F3: no inferir leakage por ausencia de grouped split documentado; su aplicabilidad depende de observaciones correlacionadas.
- F4: frontera metodológica, no contribución novedosa por sí sola.
- F5: queda prohibida la afirmación amplia de ausencia de auditability/source-support evaluation en regulatory AI.
- G6/G7 no se reabren.

### Admisión bibliográfica nueva

- `N01 = APPROVED_NEW` y puede utilizarse dentro de sus límites congelados.
- `N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET`; no lo uses como evidencia determinante ni lo cites como fuente admitida.
- `N03 = REJECT`.
- `N04 = REJECT`.

No realices nueva búsqueda web. 0B está cerrado.

### Propósito científico de 0C

Construye un **mapa de posicionamiento candidato** que permita a la IA Gestora decidir posteriormente el gap, la contribución central y las RQs. Tu tarea es contrastar alternativas con evidencia y contraevidencia, no elegir por autoridad propia la novelty final.

Debes distinguir siempre:

`LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.

También:

`ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`.

`ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`.

`AUDITABILITY ≠ LEGAL_CORRECTNESS`.

`CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.

### Tarea 1 — Matriz de transferencia 0A + 0B

Construye una matriz:

`elemento | fuente gobernante | evidencia a favor | evidencia en contra/caveat | estado para 0C | riesgo de overclaiming`

Debe cubrir como mínimo:

- arquitectura histórica → Top-k/Top-3 fijo → evidencia normativa → LLM explicativo;
- F1–F5;
- dependencia SERIE/DAM y split v0.2;
- H100 y su interpretación como candidate retrieval;
- HE4/auditabilidad con sus límites;
- reproducibilidad/provenance;
- 0B-05C y límites de drift normativo;
- dependencias experimentales pendientes relevantes para claims futuros.

### Tarea 2 — Tres familias de gap candidatas

Evalúa separadamente:

1. **Gap empírico candidato**.
2. **Gap metodológico candidato**.
3. **Gap de apoyo a decisiones/auditabilidad candidato**.

Para cada uno entrega:

- formulación candidata de una sola oración;
- evidencia bibliográfica que la permite;
- prior art que la debilita;
- evidencia experimental/documental del proyecto relevante;
- qué parte es `SUPPORTED_NOW`;
- qué parte es `CONDITIONAL_ON_PENDING_EXPERIMENT`;
- qué parte es `NOT_SUPPORTED`;
- condiciones que falsarían o invalidarían la formulación;
- riesgo `LOW / MEDIUM / HIGH` de overclaiming.

No estás obligado a conservar las tres familias como gaps separados. Puedes concluir que una funciona mejor como limitación, principio metodológico o componente de contribución y no como gap.

### Tarea 3 — Tres formulaciones alternativas de contribución central

Produce exactamente **tres alternativas**:

- **A — Conservadora / mínima defendible**.
- **B — Arquitectónica-metodológica**.
- **C — Integrada de apoyo a decisiones/auditabilidad**.

Para cada alternativa incluye:

1. formulación de contribución central en 1–2 oraciones;
2. cadena lógica `problema -> vacío/limitación previa -> diseño del proyecto -> evidencia disponible -> alcance permitido`;
3. componentes realmente diferenciadores;
4. componentes que son prior art y no deben venderse como novelty;
5. evidencia requerida para sostenerla;
6. resultados pendientes que podrían debilitarla;
7. relación con F1–F5;
8. riesgo de overclaiming;
9. qué afirmaciones están expresamente prohibidas.

No uses “first”, “novel”, “unprecedented”, “no previous work” o equivalentes.

### Tarea 4 — Research Questions candidatas

Propón un conjunto principal de **2 a 4 RQs** coherentes con la alternativa de contribución que consideres científicamente más robusta, pero etiquétala solo como `RECOMMENDED_FOR_EDITORIAL_REVIEW`, no como seleccionada/final.

Cada RQ debe incluir:

- texto exacto candidato;
- constructo evaluado;
- evidencia/experimento que puede responderla;
- estado de esa evidencia: `AVAILABLE_FROZEN`, `AVAILABLE_WITH_LIMITATION`, `PENDING`, o `NOT_AVAILABLE`;
- métricas/outputs relevantes;
- unidad de análisis/agrupamiento pertinente;
- riesgo de no poder responderla completamente;
- relación con objetivo/hipótesis aprobados.

No diseñes una RQ cuya respuesta dependa exclusivamente de un experimento inexistente o no autorizado.

### Tarea 5 — Mapeo OE/HE al artículo

Usando únicamente las formulaciones exactas congeladas en 0A, construye:

`OE/HE | formulación exacta | relación con contribución candidata | evidencia disponible | estado | recomendación`

La recomendación solo puede ser:

- `IN_PAPER`;
- `CONDITIONAL`;
- `THESIS_ONLY`.

No reescribas objetivos o hipótesis para hacerlos encajar. Si una HE depende de Grupo 3 u otro bloque experimental pendiente, debe quedar `CONDITIONAL` salvo evidencia congelada suficiente en sentido contrario.

### Tarea 6 — Claims candidatos para posterior actualización de la Claim–Evidence Matrix

No modifiques `CLAIM_EVIDENCE_MATRIX.md`.

Genera una tabla candidata:

`claim_candidate_id | claim | tipo | soporte | contraevidencia/caveat | estado analítico | uso futuro posible`

Usa únicamente estos estados analíticos internos:

- `SUPPORTED_NOW`;
- `CONDITIONAL_ON_PENDING_EXPERIMENT`;
- `NOT_SUPPORTED`;
- `PROHIBITED_BY_FROZEN_BOUNDARY`.

Incluye tanto claims positivos como claims que deberían permanecer prohibidos.

### Tarea 7 — Comparación y recomendación editorial

Compara A/B/C mediante:

- fuerza evidencial;
- diferenciación frente al prior art;
- dependencia de resultados pendientes;
- compatibilidad con objetivos/hipótesis;
- riesgo de overclaiming;
- claridad para un artículo internacional;
- capacidad de sostener RQs medibles.

Selecciona solo una como:

`RECOMMENDED_FOR_EDITORIAL_REVIEW`

Las otras deben quedar `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE`.

Esta recomendación no equivale a aprobación editorial, final gap o novelty.

### Tarea 8 — Riesgos y bloqueos antes de congelar 0C

Lista explícitamente:

- contradicciones internas detectadas;
- claims que dependen de experimentos pendientes;
- formulaciones que exigirían revisión experimental;
- cualquier punto que requiera una decisión del autor;
- cualquier motivo por el que 0C no pueda congelarse todavía.

Si introduces una interpretación experimental no presente ya en los freezes/Plan Maestro, marca:

`EXPERIMENTAL_REVIEW_TRIGGER = PRESENT`

En caso contrario:

`EXPERIMENTAL_REVIEW_TRIGGER = ABSENT`

No solicites directamente la revisión experimental; solo identifica el trigger.

### Formato obligatorio del artefacto

Usa estas secciones:

A. Estado reconstruido  
B. Matriz de transferencia 0A + 0B  
C. Gap empírico candidato  
D. Gap metodológico candidato  
E. Gap de apoyo a decisiones/auditabilidad candidato  
F. Alternativas A/B/C de contribución central  
G. Research Questions candidatas  
H. Mapeo OE/HE al artículo  
I. Claims candidatos  
J. Comparación A/B/C y recomendación editorial  
K. Riesgos, dependencias y triggers  
L. Trazabilidad

### Cierre obligatorio

Termina exactamente con un bloque equivalente a:

```text
0C_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0C = NOT_PERFORMED
0D = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT | PRESENT
```

### Prohibiciones

- No hacer búsqueda web ni añadir literatura nueva.
- No modificar Plan Maestro, 0A, freezes de 0B o resultados experimentales.
- No modificar `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md` ni reviews.
- No declarar final gap o novelty.
- No seleccionar revista.
- No redactar ninguna sección de manuscrito.
- No inventar resultados pendientes.
- No reinterpretar resultados descriptivos como causales.
- No equiparar evidence retrieval/auditability con legal correctness.
- No presentar configurabilidad como generalización empírica.
- No crear nuevas RQs incompatibles con los objetivos/hipótesis aprobados.

### Artefacto de respuesta obligatorio en GitHub

Crea exactamente un archivo:

`article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`

No modifiques ningún otro archivo.

El artefacto debe ser bilingüe: versión completa en español y versión completa en inglés con equivalencia semántica.

Si `V01` ya existe, detente y reporta conflicto. No crees `V02` sin autorización expresa.

### Commit y respuesta al usuario

Versiona únicamente ese archivo en `article/main-manuscript` con un mensaje equivalente a:

`article: add 0C positioning analysis response v01`

En el chat informa únicamente:

- commit SHA;
- ruta del archivo;
- estado `COMPLETED_PENDING_EDITORIAL_REVIEW`.

Detente después del commit.

---

## English

### Role and scope

Act exclusively as the Writing and scientific-analysis AI for the main Tesis San Marcos article. Execute only `0C — Gap, contribution, and Research Questions`. Do not act as the Experimental AI or Managing AI; do not self-declare final novelty/gap, change experiments, decide journal fit, or draft manuscript sections.

### Mandatory inputs

Read the same governing files listed in the Spanish section, including all frozen 0A/0B artifacts, formal Phase-0B closure, the 0C entry gate, the bibliographic admission registry, the Claim–Evidence Matrix, Decisions, Source Registry, Master Writing Plan, Style Guide, and the current experimental Master Plan in read-only mode.

### Mandatory transferred state

F1 has only a bounded negative search result. F2 has partial prior art and survives only under `EXTERNAL_FIXED_TOP_K + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT/DELETE/SUBSTITUTE/REORDER + NO_CLASSIFICATION_FEEDBACK`. F3 is applicability-conditioned and does not justify leakage or novelty claims from missing grouped splits. F4 is a methodological boundary rather than independent novelty. F5 has direct prior art and its broad regulatory-AI absence claim is falsified. G6 remains eliminated and G7 merged into F2.

N01 is `APPROVED_NEW`; N02 is not admitted; N03/N04 are rejected. No new web/literature search is authorized.

### Scientific task

Construct a candidate positioning map rather than a final novelty statement. Keep `LITERATURE_GAP`, `PROJECT_FEATURE`, `SCIENTIFIC_CONTRIBUTION`, `EXPERIMENTAL_RESULT`, and `NOVELTY_CLAIM` distinct.

Perform the same eight tasks specified in Spanish: transfer matrix; empirical/methodological/decision-support gap candidates; exactly three contribution alternatives A/B/C; 2–4 candidate RQs for the strongest alternative; exact OE/HE mapping; candidate claims with analytical support states; comparative editorial recommendation; and risks/dependencies/triggers.

### Required status labels

For candidate claims use only `SUPPORTED_NOW`, `CONDITIONAL_ON_PENDING_EXPERIMENT`, `NOT_SUPPORTED`, or `PROHIBITED_BY_FROZEN_BOUNDARY`.

For contribution alternatives use one `RECOMMENDED_FOR_EDITORIAL_REVIEW` and two `ALTERNATIVE_NOT_SELECTED_AT_DRAFTING_STAGE` labels. Neither constitutes editorial approval or final novelty.

### Required artifact

Create exactly:

`article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`

The artifact must be fully bilingual with semantic equivalence. Modify no other file. Do not overwrite V01 or create V02 without explicit authorization.

### Required closure

End with:

```text
0C_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0C = NOT_PERFORMED
0D = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT | PRESENT
```

Commit only the response artifact and report to the author only the commit SHA, path, and `COMPLETED_PENDING_EDITORIAL_REVIEW` state.
