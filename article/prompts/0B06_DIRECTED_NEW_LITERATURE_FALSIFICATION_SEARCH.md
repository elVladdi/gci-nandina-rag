# Prompt cerrado 0B-06 — Búsqueda dirigida de literatura nueva para falsación de candidatos / Closed prompt 0B-06 — Directed new-literature search to falsify candidates

## Español

### Rol

Actúa exclusivamente como **IA de Redacción y análisis bibliográfico** del artículo científico principal del proyecto Tesis San Marcos.

Ejecuta únicamente `0B-06 — Búsqueda dirigida de literatura nueva para falsación de candidatos`.

No eres la IA Experimental ni la IA Gestora. No defines el gap final, no declaras novelty, no modificas resultados experimentales, no modificas el Plan Maestro, no redactas el manuscrito y no avanzas a 0C.

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
9. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
10. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
11. `article/reviews/0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT.md`;
12. freezes de `0B-01`, `0B-02`, `0B-03A`, `0B-03B`, `0B-04A`, `0B-04B`, `0B-05A`, `0B-05B` y `0B-05C`.

Antes de buscar, reconstruye y declara brevemente dentro del artefacto de respuesta:

```text
FASE_ACTIVA = 0B
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
0C = BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

### Propósito científico

La búsqueda debe ser **falsacionista**, no confirmatoria. Su objetivo es intentar encontrar literatura reciente que falsifique, debilite o vuelva redundantes las formulaciones estrechas supervivientes de F1, F2 y F5 y, secundariamente, comprobar F3.

No busques literatura para “respaldar nuestra novedad”. Busca activamente el prior art más cercano que pueda derrotarla.

### Ventana y criterios de admisión

Para toda **nueva referencia académica**, aplica íntegramente `article/BIBLIOGRAPHIC_FRAMEWORK.md`:

- publicación `2022–2026` inclusive;
- artículo científico revisado por pares;
- preferentemente revista Q1;
- Q2 únicamente si es altamente específica y no existe alternativa Q1 equivalente;
- indexación verificable, preferentemente WoS/JCR y/o Scopus/SJR/CiteScore;
- PDF completo legítimamente accesible;
- DOI u otro identificador estable y metadata verificable;
- relevancia directa para una de las preguntas de búsqueda autorizadas;
- lectura completa antes de recomendar admisión.

No admitas como `CANDIDATE_NEW` nuevas tesis, proceedings, preprints, blogs, white papers o manuscritos no publicados. Si aparece uno especialmente relevante, puede registrarse únicamente como `NON_ADMISSIBLE_LEAD`, sin utilizarlo para concluir el pressure test ni incorporarlo al artículo.

No sustituyas referencias heredadas por recencia.

### Fuentes web permitidas para verificación

Puedes usar búsqueda web actual. Prioriza:

- página oficial de la revista/editorial;
- DOI/Crossref para identidad y metadata;
- Web of Science/JCR, Scopus o SCImago/SJR para indexación/cuartil cuando estén disponibles;
- repositorio institucional o versión de autor legítima para PDF completo.

No uses snippets como evidencia científica. Un paper no puede superar el gate sin lectura de texto completo.

### Familias de búsqueda autorizadas

#### S1 / F1 — ranking histórico fijado + evidencia normativa posterior no-reranking

Busca sistemas de clasificación arancelaria/HS/customs donde:

1. precedentes históricos, casos anteriores o descripciones comerciales recuperadas produzcan un ranking/Top-k de códigos;
2. ese ranking quede fijado antes de recuperar normativa/reglas/evidencia oficial;
3. la evidencia normativa posterior documente/justifique candidatos sin capacidad de reordenar, sustituir o introducir códigos.

Distingue de:

- RAG donde normativa participa en decidir el código;
- reranking;
- hierarchical search guiado por reglas;
- knowledge graphs usados para inferencia;
- evidence retrieval que retroalimenta la clasificación.

#### S2 / F2 — LLM/generador exclusivamente explicativo sobre Top-k externo e inmutable

Busca sistemas aduaneros/HS o, si es necesario como contraste muy cercano, sistemas regulatorios de clasificación donde:

1. un componente independiente upstream fija el ranking/Top-k;
2. el LLM/generador downstream solo explica;
3. no puede introducir, eliminar, sustituir o reordenar códigos/clases;
4. no existe feedback del generador hacia la decisión clasificatoria.

No cuentes como equivalentes:

- rationale generado por el mismo modelo que decide;
- RAG classification;
- agents que pueden redirect/demote/discard;
- explicación posterior a una ruta que fue generada por reglas/modelo dentro del mismo proceso decisorio, salvo que el generador esté contractualmente aislado del decision path.

#### S3 / F3 — grouped split, dependencia o leakage por unidad administrativa/entidad

Búsqueda secundaria y acotada. Busca literatura reciente de clasificación aduanera, trade compliance o clasificación de productos que:

- agrupe por declaración, shipment, importer/exporter, product family, entity u otra unidad correlacionada;
- impida que observaciones relacionadas crucen train/dev/test;
- evalúe duplicate-family leakage, entity leakage, near-duplicate leakage o dependencia equivalente.

No conviertas ausencia de evidencia en afirmación de novelty. Si no hay antecedente directo, reporta solo `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`.

#### S4 / F5 — evaluación formal per-output de auditabilidad documental

Busca trabajos de HS/customs/regulatory AI que evalúen por salida/caso, mediante criterios explícitos o rúbrica separada:

- trazabilidad de evidencia;
- source-to-claim alignment;
- suficiencia/identificabilidad documental;
- auditabilidad documental de la explicación o decisión.

La evaluación debe estar diferenciada de accuracy/F1, path validity, citations visibles, provenance metadata, faithfulness, relevance o mera presencia de rationale.

No concluyas equivalencia entre auditability y legal correctness.

#### S5 — combinaciones

Busca expresamente trabajos que combinen dos o más propiedades de S1–S4. Un único antecedente combinado puede ser más importante que varios antecedentes parciales.

### Estrategia de búsqueda mínima

Para cada S1–S5:

1. usa varias combinaciones de términos en inglés y, cuando aporte recall, español;
2. incluye sinónimos funcionales, no solo nombres exactos del proyecto;
3. revisa referencias y trabajos relacionados de los candidatos más cercanos dentro de la ventana 2022–2026;
4. deduplica por DOI/título;
5. registra también resultados negativos significativos: papers muy cercanos que **no** satisfacen una condición crítica.

No fijes un número mínimo artificial de papers. El objetivo es identificar el prior art más cercano y documentar por qué sí o no satisface cada condición.

### Etiquetas de pressure test permitidas

Para cada candidato F1/F2/F3/F5 utiliza únicamente:

- `DIRECT_PRIOR_ART_FOUND`;
- `PARTIAL_PRIOR_ART_FOUND`;
- `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`;
- `INCONCLUSIVE`.

Estas etiquetas **no equivalen** a novelty ni a gap final.

Para cada nueva referencia usa:

- `CANDIDATE_NEW — ADMIT_RECOMMENDED`;
- `CANDIDATE_NEW — REVIEW`;
- `REJECT`;
- `NON_ADMISSIBLE_LEAD`.

La IA de Redacción no puede promover una referencia a `APPROVED_NEW`; esa decisión corresponde a la IA Gestora / Editor Científico Principal después de auditoría.

### Formato obligatorio del artefacto de respuesta

#### A. Control de búsqueda

`search_family | queries_used | sources/databases_consulted | date_searched | hits_screened | full_texts_read | notes`

No inventes números si la interfaz no permite contarlos con precisión; usa `NOT_RELIABLY_COUNTABLE` cuando corresponda.

#### B. Matriz de candidatos nuevos

`ID | authors | year | title | journal | DOI | indexing | quartile/source | full PDF | search family | exact task | method | dataset/context | closest relevant property | critical missing property | recommendation`

#### C. Ficha completa de cada paper leído

Incluye:

- identidad bibliográfica;
- tipo de publicación;
- tarea;
- contexto/jurisdicción;
- dataset/corpus;
- arquitectura/pipeline;
- papel de histórico/precedentes;
- papel de normativa/evidencia;
- quién fija el ranking/decisión;
- si existe reranking;
- papel exacto del LLM;
- capacidad o incapacidad de alterar candidatos;
- auditabilidad/trazabilidad evaluada y cómo;
- split/controles de dependencia;
- resultados pertinentes;
- limitaciones;
- `REPORTADO_POR_AUTORES` vs `INFERENCIA_CRITICA`;
- relación precisa con S1–S5.

#### D. Matriz de falsación por candidato

`paper | F1 | F2 | F3 | F5 | evidencia exacta | condición que satisface | condición que no satisface`

#### E. Resultado acumulado por candidato

Para F1, F2, F3 y F5:

- etiqueta de pressure test permitida;
- papers determinantes;
- formulación previa;
- qué debe cambiar si aparece prior art;
- qué sigue sin demostrarse.

#### F. Papers cercanos rechazados

Incluye trabajos que parecían relevantes por título/abstract pero fueron descartados después de lectura o verificación, con motivo explícito. Esto es importante para trazabilidad del search gate.

#### G. Referencias no admisibles pero informativas

Lista `NON_ADMISSIBLE_LEAD` separada. No las uses como evidencia final del pressure test.

#### H. Dictamen bibliográfico provisional

Concluye exclusivamente uno de:

- `PASS — DIRECTED_SEARCH_COMPLETE`;
- `PASS WITH CORRECTIONS — ADDITIONAL_TARGETED_CHECK_REQUIRED`;
- `BLOCKED — REQUIRED_FULL_TEXT_OR_METADATA_UNAVAILABLE`.

No declares novelty ni gap definitivo.

#### I. Trazabilidad

Registra:

- commit/HEAD de `article/main-manuscript` consumido;
- fecha de búsqueda;
- URLs/DOI verificadas;
- PDFs completos leídos;
- cualquier limitación de acceso.

### Prohibiciones

- No modificar el Plan Maestro, 0A, resultados experimentales ni `main`.
- No ejecutar experimentos.
- No recalcular métricas experimentales.
- No redactar Introduction, Related Work, Methods, Results, Discussion, Conclusions, Abstract o Title.
- No declarar novelty, superiority o gap definitivo.
- No abrir 0C ni 0D.
- No modificar `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, freezes o reviews.
- No añadir referencias al manuscrito.
- No convertir ausencia de hallazgos en prueba de inexistencia universal.
- No usar literatura fuera de S1–S5 para ampliar el artículo por conveniencia.

### Artefacto de respuesta obligatorio en GitHub

Crea exactamente un archivo:

`article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`

No modifiques ningún otro archivo.

El artefacto debe ser bilingüe: versión completa en español y versión completa en inglés con equivalencia semántica.

Si el archivo `V01` ya existe, detente y reporta conflicto. No crees `V02` sin autorización expresa.

### Commit y respuesta al usuario

Versiona únicamente ese archivo en `article/main-manuscript` con un mensaje equivalente a:

`article: add 0B-06 directed literature search response v01`

En el chat informa únicamente:

- commit SHA;
- ruta del archivo;
- dictamen (`PASS`, `PASS WITH CORRECTIONS` o `BLOCKED`).

No pegues el contenido completo en el chat.

Detente después del commit.

---

## English

### Role and scope

Act exclusively as the **Writing AI and bibliographic-analysis AI** for the main Tesis San Marcos scientific article. Execute only `0B-06 — Directed new-literature search to falsify candidates`.

Do not act as the Experimental AI or Managing AI. Do not define the final gap, declare novelty, modify experiments or the Master Plan, draft manuscript sections, or advance to 0C.

### Mandatory onboarding

Read in full the same governing files listed in the Spanish section, including `BIBLIOGRAPHIC_FRAMEWORK.md`, the complete 0B frozen artifacts, and `article/reviews/0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT.md`.

### Scientific purpose

This is a **falsification-oriented**, not confirmation-oriented, search. Actively seek the closest recent prior art capable of defeating or narrowing F1, F2, F5 and, secondarily, F3.

### Admission window

Apply the full `BIBLIOGRAPHIC_FRAMEWORK.md`: new academic references must be 2022–2026 peer-reviewed journal articles, preferably Q1, with Q2 only when highly specific and lacking an equivalent Q1 alternative, verifiable indexing, stable metadata/DOI, legitimate full PDF access, direct relevance, and full-text verification.

New theses, proceedings, preprints, blogs, white papers, and unpublished manuscripts are not admissible as `CANDIDATE_NEW`. Exceptionally relevant items may only be recorded as `NON_ADMISSIBLE_LEAD` and may not determine the pressure-test conclusion.

### Authorized search families

- **S1/F1:** historical/precedent retrieval fixes the ranked candidates before post-ranking normative evidence retrieval that cannot rerank or introduce codes.
- **S2/F2:** an explanation-only downstream LLM/generator operates on an externally fixed immutable Top-k, with no insertion/deletion/substitution/reordering and no classificatory feedback.
- **S3/F3:** grouped/declaration/entity/product-family split or leakage/dependence controls in customs/trade/product classification; this is secondary and validity-oriented rather than presumed novelty.
- **S4/F5:** explicit, separate per-output/case-level evaluation of documentary auditability, source-to-claim traceability, or evidence identifiability, distinct from predictive accuracy, visible citations, metadata provenance, faithfulness, or path validity.
- **S5:** papers combining two or more of S1–S4.

### Pressure-test labels

Use only `DIRECT_PRIOR_ART_FOUND`, `PARTIAL_PRIOR_ART_FOUND`, `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`, or `INCONCLUSIVE`. None is equivalent to final novelty or a definitive gap.

For new references use only `CANDIDATE_NEW — ADMIT_RECOMMENDED`, `CANDIDATE_NEW — REVIEW`, `REJECT`, or `NON_ADMISSIBLE_LEAD`. Only the Managing AI / Lead Scientific Editor may later promote a reference to `APPROVED_NEW`.

### Required output

Produce sections A–I exactly as specified in the Spanish instructions: search control, new-candidate matrix, complete paper records, candidate-falsification matrix, cumulative result per candidate, rejected near-matches, non-admissible leads, provisional bibliographic verdict, and traceability.

### GitHub response artifact

Create exactly one file:

`article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`

Do not modify any other file. The artifact must contain full Spanish and English versions with semantic equivalence. If V01 already exists, stop and report the conflict; do not create V02 without express authorization.

Commit only that file with a semantic message equivalent to `article: add 0B-06 directed literature search response v01`. In chat report only the commit SHA, file path, and verdict, then stop.