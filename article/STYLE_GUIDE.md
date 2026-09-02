# Guía de estilo científico / Scientific Style Guide

## Español

### 1. Principio general

La redacción debe ser científica, precisa, sobria y verificable. Se priorizarán claridad lógica, trazabilidad y economía expresiva sobre retórica, grandilocuencia o lenguaje promocional.

### 2. Regla bilingüe

Cada bloque debe existir en español e inglés y ambas versiones deben decir lo mismo. La traducción no debe ser literal cuando ello perjudique la naturalidad, pero debe preservar exactamente:

- alcance;
- grado de certeza;
- relaciones causales o no causales;
- cifras;
- métricas;
- nombres de experimentos;
- restricciones;
- advertencias;
- citas;
- estructura argumental.

Si una formulación inglesa exige reestructuración sintáctica, se permite siempre que no cambie la carga epistémica.

### 3. Registro

Usar un registro académico internacional apropiado para revistas Q1/Q2 en information retrieval, NLP, knowledge-based systems y decision support.

Evitar:

- lenguaje promocional;
- adjetivos no demostrados como "robusto", "superior", "efectivo", "innovador" o "preciso";
- afirmaciones universales;
- frases de tesis excesivamente didácticas;
- explicaciones redundantes;
- listas extensas cuando un párrafo técnico sea más claro.

Preferir:

- afirmaciones delimitadas;
- verbos observacionales cuando corresponda: "se observó", "se obtuvo", "se recuperó", "se evaluó";
- formulaciones causales solo cuando el diseño las sustente;
- distinción explícita entre diseño, implementación, observación e inferencia.

### 4. Terminología obligatoria

Mantener estable, salvo decisión documentada:

- `recuperación histórica` / `historical retrieval`;
- `ranking histórico` / `historical ranking`;
- `Top-3 fijo` / `fixed Top-3`;
- `recuperación normativa` / `normative retrieval`;
- `evidencia normativa` / `normative evidence`;
- `explicación controlada` / `controlled explanation`;
- `LLM local` / `local LLM`;
- `recomendación auditable` / `auditable recommendation`;
- `subpartida NANDINA` / `NANDINA subheading`;
- `serie` / `series record` o término definitivo aprobado;
- `DAM/declaración` / `DAM/customs declaration`, según contexto;
- `unidad de análisis` / `analysis unit`;
- `unidad de agrupamiento` / `grouping unit`.

No utilizar indistintamente `classification accuracy`, `retrieval accuracy`, `Top-k recall` o `system accuracy`. Cada métrica debe nombrarse por su definición real.

### 5. Arquitectura conceptual

La redacción debe preservar siempre:

Descripción comercial → normalización → recuperación histórica → ranking Top-k → Top-3 fijo → recuperación de evidencia normativa para los candidatos → construcción de contexto → LLM local → explicación auditable.

No describir la recuperación normativa como generador principal de candidatos. No describir el LLM como clasificador autónomo. No presentar el reranking LLM diagnóstico como flujo principal.

### 6. Claims y evidencia

Cada afirmación científica debe pertenecer a una de estas clases:

- **hecho documental**: directamente respaldado por Proyecto, Anexo o Plan Maestro;
- **resultado experimental**: respaldado por artefactos congelados;
- **resultado de literatura**: respaldado por la publicación citada;
- **resultado web/editorial**: derivado de fuente web vigente;
- **inferencia**: interpretación explícita de evidencia previa.

Las inferencias no deben presentarse como hechos observados.

### 7. Resultados

En Results:

- presentar observaciones antes que interpretación;
- mantener cifras exactas y denominadores cuando sean relevantes;
- distinguir métricas por función;
- no introducir explicaciones causales no evaluadas;
- no convertir cobertura en correctness;
- no convertir evidencia asociada en evidencia normativamente suficiente;
- no convertir auditabilidad estructural en corrección jurídica.

### 8. Discussion

La Discussion debe:

- interpretar sin repetir tablas;
- contrastar con literatura comparable;
- explicar implicancias de diseño y evaluación;
- distinguir hallazgos principales, secundarios y limitaciones;
- separar explicaciones plausibles de mecanismos demostrados;
- evitar extrapolación más allá de Clase 87 si no existe evidencia externa.

### 9. Introducción

La Introduction debe progresar desde problema → limitación del estado del arte → gap → enfoque → contribución. No debe anticipar todas las decisiones metodológicas ni resumir Results en exceso.

Las contribuciones deben ser pocas, específicas y verificables.

### 10. Related Work

No organizar la literatura como una secuencia de autores. Organizar por tareas y enfoques. Comparar trabajos solo cuando resuelvan tareas suficientemente equivalentes.

No presentar diferencias de métricas entre datasets heterogéneos como comparación directa de rendimiento.

### 11. Limitaciones

Las limitaciones deben ser explícitas, técnicas y vinculadas al alcance real. Reconocer una limitación no implica invalidar el estudio. Evitar lenguaje defensivo.

### 12. Estadística e independencia

Cuando exista dependencia intra-DAM, no describir automáticamente las 1,056 series como 1,056 observaciones independientes para inferencia estadística. Cualquier estimación inferencial debe respetar la unidad de agrupamiento o justificar explícitamente otra decisión.

### 13. Reproducibilidad

Distinguir:

- reproducibilidad del estudio de referencia;
- replicabilidad externa del protocolo;
- generalización empírica.

No usar la configurabilidad del framework como evidencia de generalización empírica.

### 14. Estilo de tablas y figuras

Cada tabla o figura debe responder una pregunta concreta. No duplicar en texto todo su contenido. Los títulos y captions deben ser autosuficientes, sobrios y bilingües durante la redacción.

### 15. Citas

Las citas deben sostener la afirmación inmediatamente asociada. No usar una referencia como soporte genérico de un párrafo completo cuando solo respalda una parte. Verificar que cada comparación con literatura conserve la tarea, dataset y nivel HS de la fuente original.

### 16. Palabras y formulaciones de riesgo

Usar solo con soporte suficiente:

- improve / mejorar;
- outperform / superar;
- robust / robusto;
- generalizable / generalizable;
- causal / causal;
- accurate / preciso;
- correct / correcto;
- reliable / confiable;
- explainable / explicable;
- auditable / auditable.

Cuando el soporte sea parcial, preferir formulaciones delimitadas como "under the evaluated conditions", "within the fixed evaluation set" o equivalentes en español.

### 17. Convención de redacción bilingüe

Durante la fase de trabajo, cada archivo de manuscrito deberá seguir este patrón:

`## Español` → texto completo de la sección.

`## English` → versión semánticamente equivalente.

No alternar idiomas párrafo por párrafo.

---

## English

### 1. General principle

Writing must be scientific, precise, restrained, and verifiable. Logical clarity, traceability, and economy of expression take priority over rhetoric, grandiosity, or promotional language.

### 2. Bilingual rule

Every block must exist in Spanish and English, and both versions must say the same thing. Translation need not be literal when literal wording reduces naturalness, but it must preserve exactly:

- scope;
- degree of certainty;
- causal or non-causal relationships;
- figures;
- metrics;
- experiment names;
- restrictions;
- warnings;
- citations;
- argumentative structure.

If English requires syntactic restructuring, it is allowed provided that the epistemic force does not change.

### 3. Register

Use an international academic register suitable for Q1/Q2 journals in information retrieval, NLP, knowledge-based systems, and decision support.

Avoid:

- promotional language;
- unsupported adjectives such as "robust", "superior", "effective", "innovative", or "accurate";
- universal claims;
- overly didactic thesis-style prose;
- redundant explanations;
- long lists when a technical paragraph is clearer.

Prefer:

- bounded claims;
- observational verbs when appropriate: "was observed", "was obtained", "was retrieved", "was evaluated";
- causal formulations only when supported by the design;
- explicit distinction among design, implementation, observation, and inference.

### 4. Mandatory terminology

Keep stable unless a documented decision changes it:

- `recuperación histórica` / `historical retrieval`;
- `ranking histórico` / `historical ranking`;
- `Top-3 fijo` / `fixed Top-3`;
- `recuperación normativa` / `normative retrieval`;
- `evidencia normativa` / `normative evidence`;
- `explicación controlada` / `controlled explanation`;
- `LLM local` / `local LLM`;
- `recomendación auditable` / `auditable recommendation`;
- `subpartida NANDINA` / `NANDINA subheading`;
- `serie` / `series record` or the final approved term;
- `DAM/declaración` / `DAM/customs declaration`, depending on context;
- `unidad de análisis` / `analysis unit`;
- `unidad de agrupamiento` / `grouping unit`.

Do not use `classification accuracy`, `retrieval accuracy`, `Top-k recall`, or `system accuracy` interchangeably. Each metric must be named according to its actual definition.

### 5. Conceptual architecture

Writing must always preserve:

Commercial description → normalization → historical retrieval → Top-k ranking → fixed Top-3 → normative-evidence retrieval for the candidates → context construction → local LLM → auditable explanation.

Do not describe normative retrieval as the primary candidate generator. Do not describe the LLM as an autonomous classifier. Do not present diagnostic LLM reranking as part of the primary flow.

### 6. Claims and evidence

Every scientific statement must belong to one of these classes:

- **documentary fact**: directly supported by the Project, Annex, or Master Plan;
- **experimental result**: supported by frozen artifacts;
- **literature result**: supported by the cited publication;
- **web/editorial result**: derived from a current web source;
- **inference**: explicit interpretation of prior evidence.

Inferences must not be presented as observed facts.

### 7. Results

In Results:

- present observations before interpretation;
- retain exact figures and denominators when relevant;
- distinguish metrics by function;
- do not introduce untested causal explanations;
- do not convert coverage into correctness;
- do not convert associated evidence into sufficient normative support;
- do not convert structural auditability into legal correctness.

### 8. Discussion

The Discussion must:

- interpret without repeating tables;
- compare against genuinely comparable literature;
- explain design and evaluation implications;
- distinguish primary findings, secondary findings, and limitations;
- separate plausible explanations from demonstrated mechanisms;
- avoid extrapolation beyond Chapter 87 unless external evidence exists.

### 9. Introduction

The Introduction should progress from problem → limitation of prior work → gap → approach → contribution. It should not anticipate every methodological decision or over-summarize Results.

Contributions should be few, specific, and verifiable.

### 10. Related Work

Do not organize the literature as a sequence of authors. Organize it by tasks and approaches. Compare studies only when they address sufficiently equivalent tasks.

Do not present metric differences across heterogeneous datasets as direct performance comparisons.

### 11. Limitations

Limitations must be explicit, technical, and linked to the actual study scope. Acknowledging a limitation does not invalidate the study. Avoid defensive language.

### 12. Statistics and independence

When intra-DAM dependence exists, do not automatically describe the 1,056 series records as 1,056 independent observations for statistical inference. Any inferential estimate must respect the grouping unit or explicitly justify another decision.

### 13. Reproducibility

Distinguish:

- reproducibility of the reference study;
- external replicability of the protocol;
- empirical generalization.

Do not use framework configurability as evidence of empirical generalization.

### 14. Table and figure style

Each table or figure must answer a specific question. Do not repeat all of its content in prose. Titles and captions must be self-contained, restrained, and bilingual during drafting.

### 15. Citations

Citations must support the immediately associated statement. Do not use a reference as generic support for an entire paragraph when it supports only part of it. Verify that every literature comparison preserves the task, dataset, and HS level of the original source.

### 16. High-risk words and formulations

Use only with sufficient support:

- improve / mejorar;
- outperform / superar;
- robust / robusto;
- generalizable / generalizable;
- causal / causal;
- accurate / preciso;
- correct / correcto;
- reliable / confiable;
- explainable / explicable;
- auditable / auditable.

When support is partial, prefer bounded formulations such as "under the evaluated conditions", "within the fixed evaluation set", or their Spanish equivalents.

### 17. Bilingual drafting convention

During the working phase, every manuscript file must follow this pattern:

`## Español` → complete section text.

`## English` → semantically equivalent version.

Do not alternate languages paragraph by paragraph.
