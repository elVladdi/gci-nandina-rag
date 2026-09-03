# Prompt 0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio / Agents, benchmarks, and hierarchical/regulatory reasoning

## Español

### Rol y alcance

Actúa como IA de redacción y análisis bibliográfico del artículo científico principal. Ejecuta **exclusivamente** `0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio`.

No redactes ninguna sección del manuscrito, no declares novelty, no cierres el gap, no busques literatura nueva y no modifiques GitHub. Tu tarea es leer íntegramente los seis PDF asignados, construir un mapa crítico comparable y someter a presión los candidatos provisionales congelados después de 0B-03A.

### Onboarding obligatorio

Accede a la rama `article/main-manuscript` de `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
5. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
6. `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`;
7. `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`;
8. `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`;
9. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
10. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
11. este prompt completo.

No reabras 0A, 0B-01, 0B-02 ni 0B-03A.

### PDFs asignados

Analiza **exclusivamente** estos seis PDF ya disponibles en el corpus de 62:

1. `A Deterministic Agentic Workflow for HS Tariff Classification.pdf`
2. `ATLAS-Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification.pdf`
3. `Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification.pdf`
4. `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification.pdf`
5. `HSCodeComp- A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application.pdf`
6. `HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification.pdf`

Si el nombre exacto del archivo presenta sufijos automáticos o pequeñas variaciones, usa la identidad científica del contenido para reconocer la obra. Si alguno no puede leerse íntegramente, identifica únicamente ese archivo y no sustituyas su contenido con web, snippets, abstracts, tesis, Anexo, conocimiento general ni otros PDF.

Los otros 56 PDF permanecen `OUT_OF_SCOPE_FOR_0B03B`.

### Regla crítica de procedencia

Usa obligatoriamente:

- `REPORTADO_POR_AUTORES`;
- `INFERENCIA_CRITICA`;
- `NO_VERIFICABLE_EN_PDF`;
- `SECONDARY_CLAIM_UNVERIFIED`.

Una afirmación que el paper toma de otra fuente no se convierte en hecho independiente para nuestro artículo. Registra como `SECONDARY_CLAIM_UNVERIFIED` cifras o afirmaciones de terceros sobre comercio, error humano, sanciones, eficiencia, ahorro, volumen de declaraciones, adopción internacional, capacidades generales de LLM u otros efectos que el paper no haya medido directamente.

### Distinciones metodológicas obligatorias

Para el presente artículo:

- clasificación agentic ≠ explicación posterior de candidatos ya fijados;
- deep search ≠ candidate retrieval histórico;
- navegación jerárquica ≠ simple uso de etiquetas HS jerárquicas;
- reglas/GIR/notas legales usadas para **decidir** el código ≠ evidencia normativa posterior usada solo para **documentar** candidatos;
- knowledge graph usado para inferencia ≠ evidencia documental recuperada;
- consensus entre agentes ≠ ground truth independiente;
- self-consistency/majority vote ≠ auditabilidad;
- tool-use o reasoning trace ≠ corrección jurídica;
- citations/rationale visibles ≠ protocolo formal de trazabilidad/auditabilidad;
- benchmark accuracy/Top-k ≠ corrección sustantiva adjudicada;
- benchmark construido para razonamiento jerárquico ≠ validación externa en NANDINA;
- ausencia de group split documentado ≠ leakage demostrado.

### Marco obligatorio por paper

Extrae solo lo que el PDF soporte:

- identificación bibliográfica, versión y tipo de publicación;
- estado documental visible en el PDF: journal/proceedings/preprint/manuscript/benchmark paper;
- tarea exacta y nivel arancelario;
- jurisdicción/nomenclatura;
- dataset/benchmark/corpus, N, clases, origen y unidad de observación;
- split/validación y controles de dependencia/duplicados;
- input y documentos/reglas disponibles;
- LLM/modelos/agentes;
- arquitectura agentic: número de agentes, roles, secuencia, consenso, reflexión, verificación, tools;
- retrieval/deep search: qué se recupera y para qué;
- jerarquía: si gobierna realmente búsqueda/inferencia;
- uso de GIR, legal notes, explanatory notes, rulings, tariff text u otras reglas;
- knowledge graph, constraints o symbolic rules;
- quién produce/decide el código final;
- si existe un conjunto de candidatos previo y si queda fijo o puede reordenarse/ampliarse;
- restricciones `no new codes`, schema, validación contra nomenclatura, abstención o guardrails;
- rationale/citations/evidence y su trazabilidad;
- auditoría/human oversight y cómo se evalúa;
- ground truth y si existe adjudicación experta independiente;
- métricas, denominadores y resultados principales;
- baselines y comparabilidad;
- errores/hallucinations/invalid codes si se reportan;
- limitaciones reconocidas por autores;
- limitaciones adicionales como `INFERENCIA_CRITICA`;
- transferibilidad a NANDINA/Clase 87;
- diferencia real respecto de la arquitectura actual.

### Pressure test obligatorio: F1–F5, G6 y G7

Clasifica el efecto de cada paper como:

- `SUPPORTS_CANDIDATE`;
- `WEAKENS_CANDIDATE`;
- `FALSIFIES_CANDIDATE`;
- `NOT_RELEVANT`;
- `UNRESOLVED`.

Recuerda: `SUPPORTS_CANDIDATE` significa únicamente contraste compatible con supervivencia provisional dentro de este lote; **no** significa evidencia de novelty.

Candidatos vigentes:

- **F1/G1:** precedentes históricos recuperados generan/fijan ranking; normativa se recupera después solo para respaldar candidatos sin reordenarlos.
- **F2/G2:** generador posterior opera sobre Top-k fijo y no puede introducir códigos externos ni alterar orden.
- **F3/G3:** control explícito de dependencia por unidad administrativa/grupo cuando observaciones relacionadas pueden cruzar particiones.
- **F4/G4:** predictive/candidate performance, similitud o coherence scoring deben separarse de corrección sustantiva/jurídica adjudicada.
- **F5/G5:** evaluación formal, por caso, de trazabilidad/auditabilidad documental separada de accuracy, faithfulness, metadata o rationale visible.
- **G6:** ground truth independiente/adjudicado para correctness, separado de labels históricos asumidos correctos.
- **G7:** separación explícita entre papel clasificatorio y papel explicativo del LLM dentro de un sistema aduanero híbrido.

G7 es especialmente importante: **debe ser falsificado, debilitado o estrechado si algún agente/sistema ya desacopla claramente clasificación, recuperación, razonamiento y explicación**.

### Verificaciones críticas específicas

Busca especialmente:

1. Si el agente/LLM **decide el código** o solo explica/valida un conjunto previo.
2. Si existe una etapa que fija candidatos antes del LLM generativo.
3. Si los agentes pueden introducir códigos fuera de una lista inicial.
4. Si el orden de candidatos puede cambiar.
5. Si el sistema utiliza reglas legales/normativas como elementos de decisión o solo como citas posteriores.
6. Si la jerarquía controla la búsqueda o solo organiza labels.
7. Si un benchmark de deep search exige aplicar reglas jerárquicas y cómo construye su ground truth.
8. Si knowledge graph o constraints reducen el espacio de búsqueda de manera determinista.
9. Si hay verificación de códigos válidos/invalid code filtering.
10. Si se reportan hallucinations y bajo qué definición.
11. Si un consensus/multi-agent score mejora resultados y si las comparaciones usan mismo dataset/prompt/denominador.
12. Si “interpretable”, “deterministic”, “compliant”, “auditable” o “expert-level” están operacionalizados con una métrica/protocolo real.
13. Si las referencias/reglas que sustentan una decisión son recuperables y localizables.
14. Si el diseño experimental controla dependencias entre observaciones relacionadas.
15. Si la publicación es una fuente académica heredada o si su admisibilidad final deberá quedar `REVIEW_REQUIRED` según `BIBLIOGRAPHIC_FRAMEWORK.md`.

### Gobernanza bibliográfica adicional

Estos seis trabajos pueden analizarse porque forman parte del corpus de 62 proporcionado por el autor. **Eso no significa que todos estén automáticamente autorizados como citas finales**.

Para cada paper devuelve dos dimensiones distintas:

1. **Función científica en el mapa:** `KEEP_CORE`, `KEEP_SUPPORTING`, `REVIEW_REQUIRED`, `EXCLUDE_FROM_ARTICLE`.
2. **Admisibilidad bibliográfica final:** `INHERITED_ELIGIBLE`, `APPROVED_NEW`, `REVIEW_REQUIRED_FOR_ADMISSION` o `NOT_APPLICABLE_YET`, solo cuando pueda determinarse desde la gobernanza disponible. No inventes cuartil, indexación, DOI ni estado editorial.

No realices web para resolver metadata o admisibilidad.

### Formato obligatorio

#### A. Control de integridad
`ID | archivo | lectura completa sí/no | metadata suficiente sí/no | tipo documental visible | observaciones`

#### B. Matriz crítica
Una fila por paper con tarea, datos, arquitectura agentic, retrieval/deep search, reglas/jerarquía, quién decide el código, restricciones de candidatos/salida, evidencia/rationale, ground truth, validación, métricas, resultados, auditabilidad, dependencia, limitaciones y función bibliográfica.

#### C. Fichas individuales
Una por paper usando las cuatro etiquetas de procedencia.

#### D. Taxonomía funcional
Usa cuando aplique: `AGENTIC_CLASSIFICATION`, `MULTI_AGENT_CONSENSUS`, `DETERMINISTIC_WORKFLOW`, `HIERARCHICAL_SEARCH`, `REGULATION_DRIVEN_SEARCH`, `DEEP_SEARCH_BENCHMARK`, `KNOWLEDGE_GRAPH_GUIDED`, `RULE_CONSTRAINED_REASONING`, `RAG_CLASSIFICATION`, `RERANKING`, `EXPLAINABILITY`, `AUDITABILITY_SUPPORT`, `HUMAN_DECISION_SUPPORT`, `HYBRID`.

#### E. Matriz de presión F1–F5/G6/G7
`paper | F1 | F2 | F3 | F4 | F5 | G6 | G7 | evidencia concreta`.

#### F. Patrones del lote
Solo patrones respaldados por al menos dos papers.

#### G. Candidatos a gap actualizados
Mantén, estrecha, debilita, falsifica o elimina F1–F5/G6/G7. Cualquier candidato nuevo debe ser `CANDIDATE_GAP_ONLY`. No declares novelty.

#### H. Claims secundarios pendientes
`paper | claim secundario | fuente primaria citada | posible utilidad | SECONDARY_CLAIM_UNVERIFIED`.

#### I. Inconsistencias y verificaciones pendientes
Lista cerrada, sin web.

#### J. Recomendación bibliográfica
`paper | función científica | admisibilidad final provisional | justificación`.

#### K. Dictamen
`PASS`, `PASS WITH CORRECTIONS` o `BLOCKED`.

### Prohibiciones

- No web.
- No literatura nueva.
- No usar los otros 56 PDF.
- No redactar secciones del artículo.
- No declarar novelty, gap definitivo ni superioridad.
- No modificar GitHub.
- No alterar claims experimentales congelados.
- No modificar el Plan Maestro.
- No avanzar a 0B-04, 0B-05, 0B-06, 0C ni fases posteriores.

### Idioma y gate

Responde únicamente en español. Detente al finalizar 0B-03B y devuelve la entrega al editor científico para revisión interna.

---

## English

### Role and scope

Act as the drafting/bibliographic-analysis AI for `0B-03B — Agents, benchmarks, and hierarchical/regulatory reasoning`. Analyze only the six assigned PDFs. Do not search the web, add literature, draft manuscript sections, declare novelty/final gap, modify GitHub, alter experimental claims, modify the Master Plan, or advance further.

Read the current status, bibliographic framework, frozen 0B-01/02/03A artifacts, frozen 0A ground truth, and this prompt before analysis.

### Mandatory distinctions

Separate agentic classification from downstream explanation; deep search from historical candidate retrieval; actual hierarchical/rule-driven inference from hierarchical labels; normative rules used to decide a code from post-ranking evidence; knowledge-graph inference from documentary evidence; multi-agent consensus from independent ground truth; reasoning traces from formal auditability; and benchmark predictive metrics from substantive legal correctness.

### Pressure test

Pressure-test F1–F5, G6, and especially G7. `SUPPORTS_CANDIDATE` means only within-batch provisional survival, never novelty evidence. If an agentic system already separates classification/retrieval/reasoning/explanation in a comparable way, G7 must be weakened, narrowed, or falsified.

### Bibliographic governance

The six works may be analyzed because they are part of the author-provided corpus, but availability does not automatically authorize final citation. Report both scientific-map function and provisional admission status without using web or inventing publication metadata.

### Output and gate

Produce sections A–K exactly as defined in the Spanish instructions. Respond only in Spanish, stop after 0B-03B, and return the deliverable for internal scientific/editorial review.
