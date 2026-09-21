# Related Work B06 — Positioning of this study

## 1. Alcance autorizado

Ejecuta exclusivamente `RELATED_WORK_B06 / Section 2.6 Positioning of this study`.

Este bloque cierra Related Work. No redactes Introduction, Decision-support architecture, Experimental design, Results, Discussion, Conclusion ni ninguna sección posterior.

Aplica obligatoriamente:

- `article/START_HERE.md`;
- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
- `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`;
- `article/governance/D024_RELATED_WORK_B05_APPROVAL_INTEGRATION_AND_B06_START.md`;
- `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
- `article/literature/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_FROZEN.md`;
- `article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
- `article/STYLE_GUIDE.md`.

D-022 gobierna la respuesta: toda respuesta sustantiva debe quedar versionada en GitHub. En chat solo se permite el puntero mínimo autorizado.

## 2. Baseline acumulativo obligatorio

### Markdown canónico

Usa como baseline exacto:

`article/manuscript/ARTICLE_MASTER_V005.md`

Git blob esperado:

`25782b8b2305b546f2f5ff69514893d045e50762`

### DOCX local

Conforme a D-021, el baseline Word no se obtiene de GitHub. Debes continuar sobre el binario local aprobado de B05:

`ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx`

o sobre una copia local renombrada que sea byte-for-byte idéntica.

SHA-256 obligatorio del baseline DOCX:

`042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`

Antes de editar el Word, verifica ese SHA-256. Si el binario exacto no está disponible, detente con `BASELINE_DOCX_ACCESS_REQUIRED`; no reconstruyas el DOCX desde Markdown.

Preserva exactamente:

- Sections 2.1–2.5 en inglés y español;
- los 32 comentarios Word heredados;
- estilos, estructura y controles existentes;
- cero tracked changes.

## 3. Función científica de 2.6

Section 2.6 debe responder una sola pregunta narrativa:

**¿Cómo se posiciona este estudio frente a los enfoques revisados cuando se distingue qué componente genera candidatos, cuándo entra la evidencia documental, qué autoridad tiene el LLM y cómo se evalúa cada función?**

No redactes una lista de contribuciones ni una declaración de novelty. No repitas 2.1–2.5 como resumen mecánico. La subsección debe sintetizar las diferencias funcionales necesarias para preparar la futura Introduction.

El objeto de posicionamiento autorizado es el contrato completo:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

La diferencia defendible está en la combinación y separación de funciones y límites de autoridad. **No se autoriza afirmar que esa diferencia sea novelty por sí misma.**

## 4. Prior art que debe reconocerse

La subsección debe reconocer de forma explícita y equilibrada que existen antecedentes parciales y cercanos.

Como mínimo, preserva estas conclusiones ya congeladas:

1. La literatura incluye direct classification, hierarchical/staged prediction, candidate retrieval/ranking y post-assignment validation; no son la misma tarea.
2. Lee et al. (2021) recuperan sentencias del HS manual que participan en una predicción posterior; por tanto, la evidencia recuperada puede intervenir en la decisión.
3. Lee et al. (2023) combinan candidate prediction con retrieval de evidencia del HS manual para inspección; por tanto, **candidate prediction + evidence retrieval no es por sí solo el elemento diferenciador del presente estudio**.
4. Trabajos regulatorios/agentic como Wang et al. (2026) permiten que evidencia y/o LLM participen en search control, next-hop selection o en la construcción del decision path; eso difiere de explanation-only generation sobre candidatos ya fijados.
5. Chen and Tanaka-Ishii (2026) constituyen prior art directo contra una formulación amplia de ausencia de auditability en regulatory AI: evalúan traces/source support, pero su representación generada/refinada participa en producir la etiqueta; no existe un Top-k upstream externo e inmutable equivalente al contrato aquí estudiado.
6. Los principios de reproducibilidad y evaluación revisados en 2.5 justifican interpretar cada métrica para la función que realmente mide; no convierten tareas diferentes en comparables.

No es obligatorio citar todas esas fuentes si una formulación más compacta cumple la función narrativa, pero cualquier afirmación bibliográfica que permanezca en el texto debe estar soportada por fuente primaria exacta.

## 5. Fuentes y citas

### No realizar búsqueda bibliográfica abierta

El corpus frozen ya es suficiente para B06. No busques nuevos papers, no propongas nuevas referencias y no abras un ciclo de admisión bibliográfica.

Usa únicamente referencias ya admitidas/frozen para el artículo.

Para cada cita que aparezca en la versión inglesa:

1. recupera o abre el full text primario correspondiente;
2. verifica el pasaje exacto que soporta la oración;
3. limita la afirmación al alcance real del pasaje;
4. inserta un comentario Word anclado a la cita inglesa con el pasaje verificable y la identificación de la fuente, siguiendo el patrón acumulativo vigente.

No uses los freezes, reviews o matrices internas como sustituto de la fuente primaria en una cita del manuscrito. Esos artefactos gobiernan la interpretación, pero el claim bibliográfico debe quedar respaldado por el paper original.

Si una fuente primaria necesaria no puede recuperarse, elimina/reformula el claim o detente con `ACCESS_RECHECK_REQUIRED`; no cites de memoria.

## 6. Forma narrativa esperada

Objetivo orientativo para Part I English: **550–750 palabras**, aproximadamente 4–5 párrafos cohesionados, sin sub-subsecciones ni listas dentro del manuscrito.

Flujo recomendado:

1. síntesis de cómo la literatura distribuye autoridad entre classification, retrieval, regulatory evidence y generation;
2. reconocimiento del antecedente más cercano en customs/HS y de por qué candidate prediction + evidence retrieval no basta para diferenciar el estudio;
3. contraste con sistemas donde evidence/LLM participa en search o decision making;
4. posicionamiento del presente trabajo como separación explícita de ranking, evidencia y explicación, junto con evaluación por función y control de dependencia cuando corresponde;
5. frase final que cierre Related Work y prepare la Introduction sin declarar novelty ni resultados.

Redacta como artículo científico KBS, no como documento de gobernanza. Evita enumerar nombres internos como F1/F2/F3/F5, C01, D024, HE2, Grupo 4, etc. Esos códigos son control interno y no deben aparecer en la prosa publicable.

Aplica SPCCR: entidad/componente → acción → entrada → salida → restricción. Evita cadenas de abstracciones, nominalizaciones excesivas y lenguaje de especificación contractual visible al lector.

## 7. Fronteras obligatorias

Debe permanecer cierto:

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Queda prohibido escribir, incluso con sinónimos:

- `first`, `novel`, `unique`, `unprecedented`, `to our knowledge, the first`;
- ausencia universal de antecedentes;
- SOTA o superioridad cross-study;
- resultados, cifras o performance del presente estudio;
- causalidad no identificada;
- que normative evidence pruebe substantive/legal correctness;
- que explanation/auditability pruebe legal correctness;
- que provenance o reproducibility prueben correctness;
- que configurability implique empirical generalization;
- que ausencia de grouped split reportado en otros trabajos implique leakage;
- que el testbed NANDINA/Chapter 87 defina el alcance conceptual de la arquitectura.

También evita presentar el contrato completo como un hecho empírico ya validado; B06 posiciona el diseño del estudio frente a literatura. La evidencia empírica se reportará en secciones posteriores cuando sus gates estén abiertos.

## 8. Artefactos de salida

Genera exactamente:

1. `article/sections/related_work/RelatedWork_B06_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B06_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx` — **solo local, bajo D-021; no subir a GitHub**
4. `article/responses/2_RELATED_WORK_B06_RESPONSE_V01.md`

Los dos Markdown científicos deben contener Part I English y Part II Spanish semantic-control mirror.

El master candidato Markdown debe partir de `ARTICLE_MASTER_V005.md` y modificar exclusivamente el placeholder de Section 2.6 en ambas partes.

El DOCX local debe partir del binario exacto B05 y modificar exclusivamente Section 2.6, preservando todos los comentarios heredados y agregando únicamente los comentarios de las nuevas citas inglesas de B06.

No promuevas todavía `ARTICLE_MASTER_V006`. Esa promoción corresponde a la IA Gestora después de auditoría y aprobación del autor.

## 9. QA obligatorio antes del commit

Verifica y registra en la respuesta GitHub:

- baseline MD blob correcto;
- baseline DOCX SHA-256 correcto;
- Sections 2.1–2.5 preservadas;
- 32/32 comentarios heredados preservados;
- número de citas inglesas nuevas y cobertura de comentarios B06;
- equivalencia semántica EN–ES;
- ausencia de tracked changes;
- integridad OOXML;
- render completo del DOCX candidato;
- SHA-256 final del DOCX candidato local;
- que 2.6 sea el único contenido científico nuevo;
- `FINAL_GAP = NOT_DEFINED`;
- `NOVELTY = NOT_DECLARED`;
- que Introduction y secciones posteriores no hayan sido redactadas.

## 10. Commit y respuesta GitHub

Después del QA, crea **un único commit semántico** que añada exclusivamente estos tres archivos Markdown:

- `article/sections/related_work/RelatedWork_B06_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B06_V01.md`
- `article/responses/2_RELATED_WORK_B06_RESPONSE_V01.md`

No subas el DOCX.

No modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, governance, canonical masters, B01–B05, fuentes experimentales ni secciones posteriores.

Evita commits auxiliares, placeholders, `__noop__`, ramas temporales, force push y transferencias Base64 innecesarias. Para los Markdown usa texto UTF-8 directo.

La respuesta GitHub debe contener el informe completo de ejecución y los hashes pertinentes. Conforme a D-022, no reproduzcas ese informe en chat.

Si la interfaz exige un mensaje final, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/2_RELATED_WORK_B06_RESPONSE_V01.md@<commit_sha>`

Después, detente. La IA Gestora realizará la auditoría independiente y solicitará aprobación del autor antes de cualquier integración o apertura de Introduction.
