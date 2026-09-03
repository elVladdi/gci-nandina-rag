# 0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio / Agents, benchmarks, and hierarchical/regulatory reasoning

## Español

### 1. Estado

- Bloque: `0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio`.
- Estado: **`APPROVED / FROZEN`**.
- Entrega inicial: análisis bibliográfico A–K de seis PDF primarios por la IA de redacción.
- Revisión científica/editorial interna: **`PASS WITH MINOR CORRECTIONS`**.
- Errores materiales detectados: `0`.
- Aprobación expresa del autor: recibida el `2026-09-03`.
- Revisión experimental: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Gap definitivo: `NOT_DEFINED`.
- Manuscrito: `NOT_DRAFTED`.

Registros gobernantes:

- `article/reviews/0B03B_INTERNAL_REVIEW.md`;
- `article/reviews/0B03B_AUTHOR_APPROVAL.md`;
- `article/prompts/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING.md`.

Este artefacto congela el mapa canónico del sub-lote. `KEEP_CORE` expresa función científica dentro del mapa 0B, no obligación de cita final. `INHERITED_ELIGIBLE` expresa elegibilidad bibliográfica heredada, no selección definitiva para el manuscrito.

### 2. Corpus congelado del sub-lote

1. `A Deterministic Agentic Workflow for HS Tariff Classification.pdf`
2. `ATLAS-Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification.pdf`
3. `Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification.pdf`
4. `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification.pdf`
5. `HSCodeComp- A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application.pdf`
6. `HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification.pdf`

Los seis fueron tratados como fuentes primarias del lote. Los otros 56 documentos del corpus permanecieron fuera del alcance de 0B-03B.

### 3. Hallazgos canónicos por trabajo

#### P01 — Deterministic Agentic Workflow

- `KEEP_CORE / INHERITED_ELIGIBLE`.
- El sistema usa un workflow determinista con retrieval, reglas, jerarquía y citas estructuradas.
- La normativa/reglas participan en la **decisión**: pueden demover, redirigir o descartar candidatos.
- El sistema produce Top-3 y evidencia/citas, pero no implementa el contrato del presente piloto donde la normativa llega después de que el ranking histórico queda fijado.
- Las cifras `84.2%` y `77.4%` son **agreement entre backbones/modelos bajo el workflow**, no accuracy contra ground truth.
- La auditoría manual de labels cubre desacuerdos, no una re-adjudicación íntegra del benchmark.
- Interpretability/traceability by construction no equivale a una evaluación formal separada de auditabilidad.

#### P02 — ATLAS

- `KEEP_CORE / INHERITED_ELIGIBLE`.
- Operacionalmente: `DIRECT_GENERATIVE_LLM_CLASSIFICATION / SUPERVISED_FINE_TUNING`; **no** `AGENTIC_CLASSIFICATION`.
- El modelo genera código + rationale; no usa RAG ni candidatos externos fijados en inferencia.
- El paper declara `18,731` rulings, mientras los splits explícitos suman `18,254 + 200 + 200 = 18,654`; los `77` registros restantes permanecen `NO_VERIFICABLE_EN_PDF`.
- El código objetivo procede del ruling, pero los reasoning paths usados para adaptación son generados sintéticamente; no deben tratarse como explicación jurídica experta adjudicada.
- Accuracy respecto de labels/rulings no equivale automáticamente a corrección jurídica independiente.

#### P03 — Consensus-based Agentic LLM

- `KEEP_CORE / INHERITED_ELIGIBLE`.
- Arquitectura multi-agente con retrieval oficial, consenso, confidence y escalamiento.
- La documentación/reglas participan en la clasificación; no son evidencia posterior a un ranking histórico fijo.
- Consensus/self-consistency no constituye ground truth independiente.
- El `human-in-the-loop` forma parte de la arquitectura, pero la evaluación cuantitativa se ejecuta **sin intervención humana correctiva activada**.
- Evidence-grounded reasoning y confidence aportan trazabilidad/uncertainty, no una evaluación formal separada del constructo auditability.

#### P04 — Constraint-Aware Hierarchical Search

- `KEEP_CORE / INHERITED_ELIGIBLE`.
- La jerarquía gobierna realmente el espacio de búsqueda; cada salto se decide con candidatos hijos, evidencia y restricciones regulatorias.
- Una vez fijada la hierarchy path, el generador final no selecciona otro nodo ni cambia esa ruta; agrega evidencia y produce salida/rationale/confidence.
- Este antecedente falsifica cualquier formulación amplia del tipo “no existe explicación posterior a una decisión fijada”.
- No falsifica F2 estrecho porque la ruta fue producida mediante búsqueda jerárquica + reglas/evidencia + modelo de decisión y no corresponde a un **ranking Top-k histórico externo e inmutable**.
- La fase final de rationale no debe equipararse a un explainer contractual que recibe un ranking previo independiente y no retroalimenta la decisión.

#### P05 — HSCodeComp

- `KEEP_CORE / INHERITED_ELIGIBLE`.
- Benchmark de deep-search agents con aplicación de reglas jerárquicas y ground truth experto.
- Proporciona antecedente directo de **anotación multi-experto, resolución/adjudicación de desacuerdos y reanotación de control**.
- En consecuencia, la formulación amplia de G6 queda falsificada como supuesto gap bibliográfico.
- `G6 = ELIMINATED AS GAP CANDIDATE`; la calidad/procedencia/adjudicación del ground truth se conserva solo como principio metodológico.
- El claim de que determinados benchmarks anteriores sufren leakage permanece `SECONDARY_CLAIM_UNVERIFIED` hasta auditar cada fuente primaria implicada.
- Los resultados humanos del benchmark no deben generalizarse a una tasa universal de desempeño de expertos aduaneros.

#### P06 — HSGraphAgent

- `KEEP_CORE / INHERITED_ELIGIBLE`.
- Usa knowledge graph, containment, exclusiones/redirecciones y Select–Redirect para restringir la trayectoria de clasificación.
- Las reglas/constraints forman parte de la inferencia clasificatoria; el LLM sigue participando en la decisión.
- `legally valid path` debe interpretarse como consistencia con las restricciones jerárquicas/regulatorias **codificadas en el graph**, no como adjudicación jurídica independiente de la clasificación final.
- `manually verified` no se amplía a un protocolo multi-experto/adjudicado salvo documentación explícita.
- La mejora observada en el benchmark tiene trade-offs computacionales y no debe generalizarse universalmente.

### 4. Taxonomía funcional congelada

- P01: `AGENTIC_CLASSIFICATION`, `DETERMINISTIC_WORKFLOW`, `HIERARCHICAL_SEARCH`, `REGULATION_DRIVEN_SEARCH`, `RAG_CLASSIFICATION`, `RERANKING`, `RULE_CONSTRAINED_REASONING`, `EXPLAINABILITY`, `AUDITABILITY_SUPPORT`, `HYBRID`.
- P02: `DIRECT_GENERATIVE_LLM_CLASSIFICATION`, `SUPERVISED_FINE_TUNING`; no se clasifica como agentic.
- P03: `AGENTIC_CLASSIFICATION`, `MULTI_AGENT_CONSENSUS`, `REGULATION_DRIVEN_SEARCH`, `RAG_CLASSIFICATION`, `RULE_CONSTRAINED_REASONING`, `HUMAN_DECISION_SUPPORT`, `AUDITABILITY_SUPPORT`, `HYBRID`.
- P04: `HIERARCHICAL_SEARCH`, `REGULATION_DRIVEN_SEARCH`, `RAG_CLASSIFICATION`, `RERANKING`, `RULE_CONSTRAINED_REASONING`, `EXPLAINABILITY`, `AUDITABILITY_SUPPORT`, `HYBRID`.
- P05: `DEEP_SEARCH_BENCHMARK`, `HUMAN_DECISION_SUPPORT` como referencia experta, `HYBRID`.
- P06: `AGENTIC_CLASSIFICATION`, `HIERARCHICAL_SEARCH`, `KNOWLEDGE_GRAPH_GUIDED`, `RULE_CONSTRAINED_REASONING`, `EXPLAINABILITY`, `AUDITABILITY_SUPPORT`, `HYBRID`.

### 5. Reglas canónicas de comparación con el proyecto actual

1. `Agentic classification` no es una categoría metodológica homogénea.
2. Deep search no equivale a recuperación histórica de candidatos.
3. Navegación jerárquica real debe distinguirse del simple uso de labels jerárquicas.
4. Reglas/GIR/notas legales usadas para decidir el código no equivalen a evidencia normativa posterior a un ranking histórico fijado.
5. Knowledge graph usado para inferencia no equivale a evidence retrieval documental.
6. Consensus/self-consistency/majority vote no equivale a ground truth independiente.
7. Reasoning trace, citations, evidence snippets o path provenance no equivalen automáticamente a una **evaluación formal de auditabilidad**.
8. Path validity o cumplimiento de constraints codificados no equivale a corrección jurídica independiente.
9. `SUPPORTS_CANDIDATE` significa solo contraste compatible con supervivencia provisional en el lote; no evidencia de novelty.
10. Ausencia de group split documentado no demuestra leakage; su pertinencia depende de que exista una estructura de observaciones relacionadas susceptible de cruzar particiones.

### 6. Estado congelado de candidatos después de 0B-03B

Ninguno constituye novelty ni gap definitivo.

#### F1/G1 — `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`

> Precedentes históricos recuperados generan y fijan el ranking de candidatos; la evidencia normativa se incorpora exclusivamente después para documentar esos candidatos y no puede modificar su orden.

No es defendible como gap decir simplemente que se combinan retrieval, RAG, histórico, reglas o normativa.

#### F2/G2 — `CANDIDATE_GAP_ONLY — FURTHER NARROWED`

> Componente generativo exclusivamente explicativo que recibe un ranking/Top-k fijado externamente por un componente previo independiente, carece de capacidad para introducir, eliminar, sustituir o reordenar códigos y no retroalimenta la decisión clasificatoria.

Wang et al. obliga a esta formulación estricta porque ya separa una ruta fijada de una fase final de evidence aggregation/rationale.

#### F3/G3 — `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`

> Control explícito de dependencia por unidad administrativa/grupo cuando el diseño contiene múltiples observaciones correlacionadas susceptibles de cruzar particiones.

No debe exigirse mecánicamente a estudios zero-shot o benchmarks sin train/test comparable.

#### F4/G4 — `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`

> Predictive/candidate performance, path validity, rule consistency y evidence grounding no equivalen a corrección sustantiva/jurídica adjudicada.

Es una distinción metodológica, no novelty por sí misma.

#### F5/G5 — `CANDIDATE_GAP_ONLY — FURTHER NARROWED`

> Evaluación formal, explícita y separada de auditabilidad documental por salida, distinta de accuracy, path validity, faithfulness, metadata, citations, traceability visible o rationale.

No se autoriza la formulación amplia “la literatura carece de trazabilidad/auditabilidad”.

#### G6 — `ELIMINATED AS GAP CANDIDATE`

HSCodeComp aporta un antecedente suficiente de ground truth experto/adjudicado. Se conserva solo como regla metodológica sobre calidad, procedencia y adjudicación del ground truth.

#### G7 — `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`

La separación entre papel clasificatorio y explicativo del LLM permanece conceptualmente útil, pero su dimensión defendible ya está contenida en F2. Mantener G7 separado generaría duplicidad conceptual.

### 7. Claims secundarios pendientes

Permanecen `SECONDARY_CLAIM_UNVERIFIED` hasta verificación primaria independiente, entre otros:

- cifras institucionales/globales de volumen de declaraciones o adopción del HS tomadas de WCO u otras fuentes;
- claims de sanciones/impactos operativos tomados de fuentes gubernamentales o prensa;
- claims de leakage de benchmarks previos reportados por HSCodeComp;
- generalizaciones sobre error humano, eficiencia, ahorro o capacidades generales de LLM no medidas directamente por el paper que las menciona.

Ninguno migra automáticamente al manuscrito como hecho independiente.

### 8. Función bibliográfica congelada

Para el mapa 0B:

- P01: `KEEP_CORE / INHERITED_ELIGIBLE`.
- P02: `KEEP_CORE / INHERITED_ELIGIBLE`.
- P03: `KEEP_CORE / INHERITED_ELIGIBLE`.
- P04: `KEEP_CORE / INHERITED_ELIGIBLE`.
- P05: `KEEP_CORE / INHERITED_ELIGIBLE`.
- P06: `KEEP_CORE / INHERITED_ELIGIBLE`.

Esto no obliga a citar los seis en la versión final del artículo.

### 9. Cierre

```text
0B-03B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

0B-03B queda cerrado. Este freeze no modifica 0A ni el Plan Maestro y no autoriza todavía apertura de 0C ni redacción del manuscrito.

---

## English

### 1. Status

- Block: `0B-03B — Agents, benchmarks, and hierarchical/regulatory reasoning`.
- Status: **`APPROVED / FROZEN`**.
- Drafting deliverable: A–K bibliographic analysis over six primary PDFs.
- Internal scientific/editorial review: **`PASS WITH MINOR CORRECTIONS`**.
- Material errors detected: `0`.
- Express author approval: received on `2026-09-03`.
- Experimental review: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Final gap: `NOT_DEFINED`.
- Manuscript: `NOT_DRAFTED`.

Governing records are `article/reviews/0B03B_INTERNAL_REVIEW.md`, `article/reviews/0B03B_AUTHOR_APPROVAL.md`, and the executed 0B-03B prompt.

### 2. Canonical findings

The six-paper batch shows that recent agentic/regulatory HS systems are heterogeneous: deterministic workflows, multi-agent consensus, hierarchical constrained search, deep-search benchmarks, and knowledge-graph-guided traversal already exist. In several systems, regulatory rules and hierarchy directly determine or constrain classification rather than merely documenting a previously fixed ranking.

Wang et al. is especially important: after its hierarchical path is fixed, the final generator cannot choose another node or change the path; it aggregates evidence and produces rationale/confidence. Therefore, a broad claim that “downstream explanation after a fixed decision is absent from prior work” is not defensible. The surviving F2 distinction is narrower: an explanation-only generator operating on an **externally fixed historical ranked Top-k produced by an independent upstream component**, with no code addition/deletion/substitution/reordering and no feedback into classification.

HSCodeComp directly invalidates broad G6 as a gap candidate because it includes multi-expert annotation, disagreement resolution/adjudication, and control re-annotation. Ground-truth quality remains a methodological principle, not a novelty candidate.

Traceability through paths, citations, evidence snippets, and structured traces already exists. F5 therefore survives only as a claim about **formal, explicit, separate per-output documentary-auditability evaluation**, not absence of traceability in the literature.

### 3. Governing corrections

1. ATLAS: preserve the declared 18,731 rulings versus explicit splits totaling 18,654; the remaining 77 are `NOT_VERIFIABLE_IN_PDF`.
2. Deterministic Workflow: 84.2%/77.4% are cross-model agreement, not ground-truth accuracy.
3. Consensus-based framework: human escalation is architectural; quantitative evaluation runs without corrective human intervention.
4. Constraint-Aware Search: the final generator cannot change the already fixed path; the distinction from F2 is the origin/structure of that path, not downstream ability to reorder it.
5. HSCodeComp: G6 is eliminated as a gap candidate; ground-truth quality is retained only as a methodological principle.
6. HSCodeComp leakage claims remain `SECONDARY_CLAIM_UNVERIFIED` until the affected primary benchmarks are directly audited.
7. HSGraphAgent: `legally valid path` means consistency with encoded graph constraints, not independent legal adjudication; `manually verified` must not be upgraded to multi-expert adjudication without documentation.
8. F5 survives only in its narrow formal/separate auditability-evaluation form.
9. G7 is merged into F2 and removed as an independent candidate.
10. ATLAS is not agentic; `KEEP_CORE` and `INHERITED_ELIGIBLE` do not mandate final manuscript citation.

### 4. Frozen candidate status

- F1: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- F2: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- F3: `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- F4: `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- F5: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- G6: `ELIMINATED AS GAP CANDIDATE`; retained only as a ground-truth-quality principle.
- G7: `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

None establishes a final gap or novelty.

### 5. Bibliographic role

All six works remain `KEEP_CORE / INHERITED_ELIGIBLE` for the 0B scientific map. This does not require all six to appear in the final manuscript.

### 6. Closure

```text
0B-03B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

This freeze does not modify 0A or the Master Plan and does not yet authorize Phase 0C or manuscript drafting.
