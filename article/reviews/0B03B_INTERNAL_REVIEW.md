# Revisión interna 0B-03B / 0B-03B Internal Review

## Español

### 1. Identificación

- Bloque: `0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio`.
- Tipo de revisión: científica/editorial interna con auditoría de claims contra los seis PDF primarios asignados.
- Entrega revisada: análisis bibliográfico A–K producido por la IA de redacción.
- Estado previo: `READY_FOR_DRAFTING`.
- Dictamen interno: **`PASS WITH MINOR CORRECTIONS`**.
- Errores materiales detectados: **`0`**.
- Revisión experimental: **`NOT_REQUIRED`**.
- Aprobación del autor: **`PENDING`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-04: **`NOT_STARTED`**.

### 2. Resultado general

La entrega cumple el alcance de 0B-03B. Analiza exclusivamente los seis trabajos asignados, mantiene separados los claims reportados por autores de las inferencias críticas, registra claims secundarios no verificados, no declara novelty ni gap definitivo y no altera el ground truth documental/experimental ni el Plan Maestro.

La auditoría primaria confirma como hallazgos gobernantes del lote:

- Los sistemas agentic/regulatorios recientes no forman una categoría homogénea: existen workflows deterministas, consenso multiagente, búsqueda jerárquica restringida, benchmarks de deep search y recorridos guiados por knowledge graph.
- En Zhang et al., Nguyen et al., Wang et al. y Xia et al., la normativa, las reglas o la estructura jerárquica participan de forma directa en la decisión clasificatoria; esto es metodológicamente distinto del contrato del presente piloto, donde la recuperación normativa llega después del ranking histórico y no puede reordenarlo.
- Wang et al. constituye un antecedente particularmente cercano a una separación `decisión -> evidencia/rationale`: su generador final se ejecuta después de que la ruta ha sido determinada y no puede seleccionar otro nodo ni cambiar esa ruta. Por ello, una formulación amplia de “LLM explicativo posterior a una decisión” ya no es sostenible como candidato a gap.
- HSCodeComp proporciona un contraejemplo directo a la formulación amplia de G6: utiliza anotación de varios expertos, resolución/adjudicación de desacuerdos y reanotación de control. En consecuencia, la ausencia de ground truth experto/adjudicado no puede sostenerse como espacio bibliográfico no cubierto.
- La trazabilidad mediante rutas, snippets, citas o structured traces ya está presente en varios antecedentes. Por ello, F5 solo puede conservarse en la forma estrecha de una **evaluación formal, explícita y separada de auditabilidad documental por salida**.
- Ninguno de estos hallazgos autoriza afirmar corrección jurídica, generalización a NANDINA o novelty de la arquitectura actual.

### 3. Correcciones y normalizaciones obligatorias para el freeze

#### C1 — ATLAS: contabilidad del dataset

Conservar explícitamente que el paper declara `18,731` rulings, mientras los splits visibles suman `18,254 + 200 + 200 = 18,654`. Los `77` registros restantes permanecen `NO_VERIFICABLE_EN_PDF`; no se debe inferir su destino.

#### C2 — Deterministic Agentic Workflow: agreement ≠ accuracy

Las cifras `84.2%` a cuatro dígitos y `77.4%` a seis dígitos del backbone abierto representan **acuerdo con el modelo frontier bajo el mismo workflow**, no accuracy contra ground truth. Las métricas de accuracy reportadas para el workflow con Qwen3.6-plus son las Top-1/Top-3 correspondientes al benchmark.

#### C3 — Consensus-based Agentic LLM: human-in-the-loop arquitectónico, no correctivo en el benchmark

El paper incorpora escalamiento y preguntas de aclaración como mecanismo del sistema, pero la evaluación cuantitativa se ejecuta sin activar intervención humana correctiva. No presentar el `human-in-the-loop` como adjudicación humana de las predicciones experimentales.

#### C4 — Constraint-Aware Hierarchical Search: precisar qué está realmente fijado

La entrega debe estrechar su comparación con F2. En Wang et al., una vez fijada la ruta jerárquica, el generador final `Gθ` **no selecciona otro child node ni cambia la hierarchy path**; agrega evidencia y produce clase estructurada, confianza, evidencia y rationale, pudiendo señalar baja confianza.

La diferencia con el piloto no es, por tanto, que ese componente final pueda reordenar la ruta. La diferencia relevante es más específica:

- la ruta previa fue construida mediante búsqueda jerárquica + reglas/evidencia + modelo de decisión;
- no procede de un recuperador histórico independiente;
- representa una ruta/clase seleccionada, no un ranking Top-k externo e inmutable;
- el componente final realiza verificación de soporte/formatting, aunque no altera la ruta.

Esta precisión debe gobernar cualquier comparación posterior.

#### C5 — HSCodeComp: G6 amplio queda falsificado como candidato a gap

HSCodeComp constituye un antecedente directo de ground truth experto con control de adjudicación. Por ello:

`G6 = ELIMINATED AS GAP CANDIDATE`.

La calidad/procedencia/adjudicación del ground truth puede mantenerse como **principio metodológico de evaluación**, pero no como claim de ausencia bibliográfica.

#### C6 — HSCodeComp: claim de leakage previo permanece secundario

La afirmación del paper de que determinados benchmarks construidos desde rulings públicos sufren data leakage no se incorpora como hecho independiente. Hasta auditar las fuentes primarias de esos benchmarks:

`SECONDARY_CLAIM_UNVERIFIED`.

No usar HSCodeComp para atribuir leakage a un trabajo previo sin verificación directa.

#### C7 — HSGraphAgent: path validity ≠ legal correctness

Expresiones del paper como `legally valid path` deben interpretarse para nuestro artículo como consistencia/cumplimiento de las restricciones jerárquicas y regulatorias **codificadas en el knowledge graph**. No equivalen a una adjudicación jurídica independiente de la clasificación final.

Asimismo, `manually verified` no debe ampliarse a un protocolo multi-experto/adjudicado si el PDF no lo documenta.

#### C8 — F5: conservar solo la formulación estrecha

P01, P04 y P06 muestran que evidencia identificable, rutas, citas y traces ya existen. El candidato superviviente queda limitado a:

`formal, explicit, per-output evaluation of documentary auditability as a separate construct from accuracy, path validity, faithfulness, metadata, citations, or visible rationale`.

No usar formulaciones generales como “la literatura carece de trazabilidad/auditabilidad”.

#### C9 — G7: absorber en F2

La versión amplia de G7 queda debilitada por antecedentes que separan fases clasificatorias y explicativas. Para evitar duplicación conceptual:

`G7 = MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

La dimensión todavía útil queda contenida en F2: un componente generativo exclusivamente explicativo que recibe un ranking Top-k fijado por un componente previo independiente, no introduce/elimina/sustituye/reordena códigos y no retroalimenta la decisión clasificatoria.

#### C10 — Taxonomía y función bibliográfica

- ATLAS no debe clasificarse como `AGENTIC_CLASSIFICATION`; operacionalmente es `DIRECT_GENERATIVE_LLM_CLASSIFICATION / SUPERVISED_FINE_TUNING` con generación de código+rationale.
- `KEEP_CORE` significa relevancia para el mapa científico 0B, no obligación de cita en el artículo final.
- `INHERITED_ELIGIBLE` no equivale a selección definitiva para el manuscrito; la inclusión final dependerá de la arquitectura editorial, el journal fit y la necesidad real de cada claim.

### 4. Estado actualizado de candidatos después de 0B-03B

Ninguno constituye novelty ni gap definitivo.

- **F1/G1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
  - Precedentes históricos recuperados generan y fijan el ranking; la normativa llega exclusivamente después para respaldar candidatos y no reordena.
- **F2/G2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
  - Componente generativo exclusivamente explicativo sobre un ranking/Top-k fijado externamente por un componente previo independiente; no introduce, elimina, sustituye ni reordena códigos y no retroalimenta la decisión.
- **F3/G3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
  - Control de dependencia por unidad/grupo solo cuando el diseño contiene observaciones correlacionadas susceptibles de cruzar particiones; no debe exigirse mecánicamente a benchmarks zero-shot sin train/test comparable.
- **F4/G4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
  - Candidate/predictive performance, path validity, rule consistency y evidence grounding no equivalen a corrección sustantiva/jurídica adjudicada.
- **F5/G5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
  - Evaluación formal y separada de auditabilidad documental por salida.
- **G6:** `ELIMINATED AS GAP CANDIDATE`; se conserva solo como principio de calidad del ground truth.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

### 5. Función bibliográfica provisional

La propuesta `KEEP_CORE` para los seis trabajos es aceptable **para el mapa 0B**:

- Zhang et al. — workflow determinista, reglas, retrieval y citas;
- Yuvraj & Devarakonda — generación directa/fine-tuning y contraste con explainer restringido;
- Nguyen et al. — consenso multiagente, retrieval oficial, incertidumbre y escalamiento;
- Wang et al. — búsqueda jerárquica regulatoria y fase final posterior a ruta fijada;
- Yang et al. — benchmark experto, adjudicación y fallos de agentes;
- Xia et al. — knowledge graph, Select–Redirect y restricciones jerárquico-regulatorias.

Esto no obliga a citar los seis en el manuscrito final.

### 6. Dictamen y gate

**`0B-03B INTERNAL REVIEW = PASS WITH MINOR CORRECTIONS`**.

No se requiere una nueva ejecución completa por la IA de redacción. Las correcciones C1–C10 son normalizaciones de alcance, terminología y comparación que pueden integrarse editorialmente en el artefacto canónico después de aprobación expresa del autor.

No se requiere revisión de la IA experimental porque esta revisión no modifica hechos experimentales congelados, claims experimentales ni el Plan Maestro.

Siguiente estado permitido:

`AUTHOR_APPROVAL_PENDING`.

Hasta aprobación expresa del autor:

- no congelar 0B-03B;
- no abrir 0B-04;
- no abrir 0B-05/0B-06;
- no abrir 0C;
- no redactar secciones del manuscrito.

---

## English

### 1. Identification

- Block: `0B-03B — Agents, benchmarks, and hierarchical/regulatory reasoning`.
- Review type: internal scientific/editorial review with claim-level verification against the six assigned primary PDFs.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**.
- Material errors found: **`0`**.
- Experimental review: **`NOT_REQUIRED`**.
- Author approval: **`PENDING`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-04: **`NOT_STARTED`**.

### 2. Overall assessment

The deliverable satisfies the 0B-03B scope. It analyzes only the six assigned works, separates author-reported claims from critical inference, retains secondary third-party claims as unverified, does not declare novelty/final gap, and does not alter frozen documentary/experimental ground truth or the Master Plan.

Primary-source verification confirms the governing batch findings. Recent agentic/regulatory HS systems are heterogeneous; several use regulatory rules or hierarchical structure directly in code decision-making; Wang et al. already separate a fixed hierarchical path from a downstream evidence/rationale generator; HSCodeComp provides a direct multi-expert/adjudication counterexample to broad G6; and traceability through paths, snippets, citations, or structured traces already exists in several systems. None of this establishes legal correctness, NANDINA generalization, or novelty of the present work.

### 3. Required corrections and normalizations for freeze

**C1 — ATLAS dataset accounting.** Preserve the stated `18,731` rulings versus explicit splits totaling `18,654`; the remaining `77` records are `NO_VERIFICABLE_EN_PDF`.

**C2 — Deterministic workflow agreement.** The `84.2%/77.4%` open-backbone figures are cross-backbone agreement, not ground-truth accuracy.

**C3 — Consensus framework human-in-the-loop.** Human escalation is part of the architecture, but quantitative evaluation is run without corrective human intervention.

**C4 — Constraint-Aware Hierarchical Search.** After the path is fixed, the final generator does not select another child or change the hierarchy path. The important difference from F2 is that the path was produced by LLM/rule/evidence-guided hierarchical search, is not an independently retrieved historical ranked Top-k, and represents a selected path/class rather than an immutable external candidate ranking.

**C5 — HSCodeComp and G6.** HSCodeComp provides a direct expert/adjudication precedent. Broad G6 is therefore eliminated as a gap candidate, while ground-truth quality remains a methodological principle.

**C6 — HSCodeComp leakage claim.** Claims that prior ruling-based benchmarks suffer leakage remain `SECONDARY_CLAIM_UNVERIFIED` until the relevant primary studies are audited.

**C7 — HSGraphAgent legal wording.** `Legally valid path` must be narrowed to consistency with the hierarchical/regulatory constraints encoded in the graph; it is not independent legal adjudication. `Manually verified` must not be upgraded to multi-expert adjudication without documentation.

**C8 — F5.** Retain only the narrow candidate concerning formal, explicit, per-output evaluation of documentary auditability as a construct separate from accuracy, path validity, faithfulness, metadata, citations, or visible rationale.

**C9 — G7.** Merge G7 into F2 and eliminate it as an independent gap candidate. The surviving dimension is an explanation-only generator operating on an externally fixed ranking, unable to add/delete/substitute/reorder codes or feed back into classification.

**C10 — Taxonomy and bibliographic role.** ATLAS is not `AGENTIC_CLASSIFICATION`; operationally it is direct generative classification through supervised fine-tuning. `KEEP_CORE` concerns the 0B scientific map only, and `INHERITED_ELIGIBLE` does not mandate final manuscript citation.

### 4. Updated candidate status

No final gap or novelty is authorized.

- F1: survives narrowly.
- F2: survives in a further-narrowed form centered on an independently fixed immutable ranked Top-k and explanation-only downstream generation.
- F3: retained with an applicability caveat.
- F4: retained as a methodological distinction, not novelty.
- F5: further narrowed to formal/separate per-output auditability evaluation.
- G6: eliminated as a gap candidate; retained only as a ground-truth quality principle.
- G7: merged into F2 and eliminated as an independent candidate.

### 5. Bibliographic role

All six works may remain `KEEP_CORE` for the 0B map. This does not require all six to be cited in the final article.

### 6. Verdict and gate

**`0B-03B INTERNAL REVIEW = PASS WITH MINOR CORRECTIONS`**.

No complete drafting-AI rerun is required. C1–C10 can be integrated editorially after express author approval. Experimental review is not required because no frozen experimental fact, experimental claim, or Master-Plan rule is changed.

The only authorized next state is `AUTHOR_APPROVAL_PENDING`. Until express approval, 0B-03B may not be frozen and 0B-04, later 0B blocks, 0C, and manuscript drafting remain closed.
