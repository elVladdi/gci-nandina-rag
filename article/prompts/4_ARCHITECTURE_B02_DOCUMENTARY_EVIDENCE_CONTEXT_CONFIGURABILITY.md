# Architecture B02 — Documentary evidence, controlled explanation, and configurability

## 1. Identidad del bloque

```text
BLOCK = ARCHITECTURE_B02
GOVERNING_DECISION = article/governance/D038_ARCHITECTURE_B02_OPENING.md@9e21642e3840844df7968a30e1213808a624c4fa
PARENT_BLOCK = ARCHITECTURE_B01
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
CANONICAL_MASTER_MD_SHA256 = 895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d
CANONICAL_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx
BASELINE_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
INHERITED_CITATION_COMMENTS = 40
AUTHORIZED_SCOPE = SECTIONS_3_5_TO_3_7_ONLY
ARTICLE_MASTER_V009 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Ejecuta exclusivamente Architecture B02. No avances a Section 4 ni a ningún bloque posterior.

## 2. Rol

Actúa como IA de Redacción científica subordinada a la gobernanza del artículo. No eres IA Gestora ni IA Experimental. Debes redactar únicamente el bloque autorizado y entregar artefactos verificables para auditoría independiente.

No puedes autoasignar estados `APPROVED`, `FROZEN`, `INTEGRATED`, promover el master ni abrir otro gate.

## 3. Objetivo único

Completar exclusivamente, en Part I English y Part II Spanish semantic-control mirror:

- `3.5 Candidate-specific documentary retrieval` / `Recuperación documental específica por candidato`;
- `3.6 Evidence-context construction and controlled explanation` / `Construcción de contexto de evidencia y explicación controlada`;
- `3.7 Configurability and interface requirements` / `Configurabilidad y requisitos de interfaz`.

La secuencia narrativa obligatoria es:

`fixed Top-3 inherited from 3.4 → candidate-specific documentary evidence → evidence-context construction → local LLM controlled explanation → configurability/interface requirements`

## 4. Onboarding y verificación inicial

Antes de redactar:

1. confirma repositorio `elVladdi/gci-nandina-rag` y rama `article/main-manuscript`;
2. lee `article/START_HERE.md`;
3. lee `article/governance/D038_ARCHITECTURE_B02_OPENING.md@9e21642e3840844df7968a30e1213808a624c4fa`;
4. lee `article/manuscript/ARTICLE_MASTER_V008.md` y verifica que su Git blob sea `0145d13e1bc4e4fdeab79f7bad83d00f67221a76`;
5. lee `article/CLAIM_EVIDENCE_MATRIX.md`, `article/SOURCE_REGISTRY.md` y `article/STYLE_GUIDE.md`;
6. consulta `SRC-02`, el Anexo metodológico vigente `Anexo_1_NANDINA_LLM_RAG_v13.docx` o la copia de plataforma documentalmente equivalente proporcionada en el proyecto;
7. verifica el DOCX baseline local exacto `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx` y su SHA-256 `f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4`.

Si el DOCX baseline no está disponible o el hash no coincide, detente con:

`ARCHITECTURE_B02_BASELINE_DOCX_MISMATCH`.

No reconstruyas el DOCX desde Markdown.

Si `SRC-02` no está accesible y una afirmación arquitectónica depende de él, detente con:

`ARCHITECTURE_B02_REQUIRED_SOURCE_UNAVAILABLE`.

## 5. Ground truth y claims permitidos

Debes respetar como mínimo:

- C02 `AUTHORIZED`: la recuperación normativa/documental aporta evidencia para candidatos y no reemplaza el ranking histórico;
- C03 `AUTHORIZED`: el LLM local explica un Top-3 previamente recuperado y no clasifica desde cero;
- C15 `AUTHORIZED`: el framework puede configurarse para otros capítulos, niveles o jurisdicciones como propiedad de diseño, no como generalización empírica;
- C17 `AUTHORIZED`: el protocolo separa reproducción del estudio de referencia y replicación externa con datos independientes;
- C12 `PROHIBITED`: evidencia normativa asociada no demuestra corrección normativa sustantiva;
- C13 `PROHIBITED`: explicaciones no demuestran corrección jurídica completa;
- C16 `PROHIBITED`: no se ha demostrado generalización empírica fuera del setting evaluado;
- C18 `PROHIBITED`: el sistema no produce clasificaciones jurídicamente vinculantes.

No introduzcas claims experimentales o de resultados que no sean necesarios para describir interfaces arquitectónicas.

## 6. Contenido obligatorio — 3.5

### 3.5 Candidate-specific documentary retrieval

Redacta de manera concreta y operacional:

1. La entrada de esta etapa es el Top-3 ya fijado en 3.4. No existe reapertura del espacio de clases.
2. La recuperación documental se ejecuta para cada candidato o conserva de forma explícita la identidad del candidato con el que se relaciona cada evidencia.
3. La salida es un conjunto de asociaciones candidato–evidencia identificables y trazables.
4. La evidencia puede incluir material documental/normativo compatible con la instanciación, pero la arquitectura no debe quedar atada en esta sección al corpus experimental concreto.
5. Esta etapa no inserta, elimina, sustituye ni reordena candidatos y no recalcula el ranking histórico.
6. La presencia, autoridad formal o recuperabilidad de un fragmento no demuestra por sí sola pertinencia, suficiencia ni corrección jurídica de la alternativa.

Diferir a Section 4: documentos concretos, corpus exacto, fechas/versiones regulatorias, segmentación, indexación, parámetros, estrategia de consulta, top-N documental y hashes.

## 7. Contenido obligatorio — 3.6

### 3.6 Evidence-context construction and controlled explanation

Explica claramente qué recibe y qué produce cada paso.

El contexto debe conservar, en el nivel arquitectónico pertinente:

- descripción/consulta;
- identidad de cada candidato del Top-3 y su posición fija;
- precedente o respaldo histórico disponible;
- evidencia documental recuperada vinculada al candidato;
- identificadores/procedencia necesarios para reconstruir qué evidencia se utilizó en la explicación.

Después explica el contrato del LLM local:

- recibe el Top-3 fijo y el contexto ya ensamblado;
- opera downstream del ranking;
- produce explicación controlada sobre las alternativas recibidas;
- preserva candidatos y orden;
- no incorpora códigos externos;
- no sustituye candidatos;
- no retroalimenta ni modifica candidate generation/ranking;
- el reranking diagnóstico queda fuera del flujo primario.

Mantén explícita la diferencia entre:

`structured/traceable explanation ≠ substantive or legal correctness`.

No afirmes que una explicación trazable demuestra fidelidad causal del razonamiento. No conviertas auditabilidad operacional en auditoría legal.

Diferir a Section 4: modelo exacto, versión, prompt textual, parámetros de generación, formato de salida, validadores concretos, hardware/software y configuración experimental.

## 8. Contenido obligatorio — 3.7

### 3.7 Configurability and interface requirements

Esta subsección debe hacer comprensible para un lector cómo puede reinstanciarse el procedimiento con recursos distintos sin presentar esa posibilidad como generalización empírica.

Explica concretamente que pueden sustituirse, si se satisfacen los contratos necesarios:

- el banco histórico etiquetado;
- el espacio de clases/códigos objetivo;
- el corpus documental compatible.

Los contratos de interfaz deben expresarse en términos observables, por ejemplo:

- entrada comercial representable/normalizable;
- registros históricos enlazables con códigos y procedencia;
- retrieval que produzca un ranking ordenado y trazable;
- construcción de candidatos únicos y frontera Top-3 fija antes de downstream;
- evidencia documental vinculable a candidatos mediante identificadores recuperables;
- contexto que conserve candidato, posición, soporte histórico, evidencia y procedencia;
- generador restringido a explicar los candidatos recibidos sin modificar la decisión upstream.

Explica también que los objetos que afectan una instanciación deben identificarse/versionarse cuando corresponda —datos, corpus, código, configuraciones, prompts/modelos y otros artefactos necesarios— de forma que la ejecución pueda reconstruirse o compararse.

### Repositorio de reproducibilidad

Debe quedar explícito, sin entrar aún al inventario experimental definitivo, que el repositorio de reproducibilidad tiene la función de permitir reconstruir la instanciación evaluada mediante artefactos versionados y trazables, como configuraciones, scripts, manifiestos, hashes, instrucciones y datos/recursos redistribuibles cuando corresponda. Section 4.11 documentará los recursos concretos, sus identidades y cualquier restricción de acceso o redistribución.

### Corpus que alimenta la explicación

Debe quedar explícito que la evidencia documental usada para construir el contexto de explicación procede de un corpus documental/normativo compatible y versionado para la instanciación. Section 4.3 documentará el corpus empírico concreto, su preparación, vigencia temporal e índice de recuperación.

Cierra la subsección con la frontera:

`configurability/re-instantiation ≠ empirical performance transfer`.

No prometas desempeño fuera del setting evaluado.

## 9. Estilo científico

Aplica el estilo gobernado del artículo:

- prosa concreta y observable;
- minimizar abstracciones, nominalizaciones y jerga de gobernanza;
- definir componentes por entradas, acciones, salidas y restricciones;
- no trasladar al manuscrito nombres de decisiones D-xxx, gates, estados internos ni lógica de workflow;
- Part I debe leerse como texto originalmente escrito en inglés científico;
- Part II debe ser espejo semántico natural en español, no traducción literal rígida;
- evitar sobreexplicar conceptos ya fijados en 3.1–3.4; B02 debe continuar, no repetir B01.

## 10. Preservación obligatoria

En el master acumulativo:

- Introduction: sin cambios;
- Related Work: sin cambios;
- 3.1–3.4: sin cambios;
- 3.5–3.7: únicos placeholders sustituibles por prosa B02;
- Section 4 y posteriores: sin cambios;
- 40 comentarios heredados: preservar exactamente;
- tracked changes: 0.

No elimines Figure 1 placeholder ni otros placeholders fuera de 3.5–3.7.

## 11. Prohibiciones expresas

No:

- redactes Experimental design;
- redactes Results, Discussion, Conclusion o front matter;
- introduzcas métricas observadas, tamaños de datasets o resultados;
- nombres H100, H150/H200, EXP-xx o grupos experimentales en la prosa publicable de B02;
- declares novelty, SOTA, first-of-its-kind, superioridad global, `FINAL_GAP` o generalización empírica;
- conviertas evidencia documental en corrección legal;
- conviertas el LLM en clasificador;
- presentes el reranker diagnóstico como arquitectura principal;
- conviertas BM25, un modelo, un prompt, un índice o un corpus concreto en requisito universal de la arquitectura;
- modifiques governance, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md` o `ARTICLE_MASTER_V008.md`;
- promuevas `ARTICLE_MASTER_V009`;
- abras un bloque posterior.

## 12. Artefactos requeridos

### 12.1 Archivo de sección — GitHub

Crear:

`article/sections/architecture/Architecture_B02_V01.md`

Debe contener exclusivamente 3.5–3.7, Part I + Part II.

Es un artefacto relativamente pequeño y debe versionarse directamente en GitHub.

### 12.2 Master Markdown acumulativo candidato — handoff timeout-safe

Generar localmente:

`ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.md`

Debe derivar exactamente de `ARTICLE_MASTER_V008.md`, sustituyendo únicamente los placeholders/instrucciones autorizados de 3.5–3.7 por la prosa B02 aprobable.

**No intentes transferir este master Markdown grande directamente por la vía que ya produjo timeout.** Entrégalo al autor como archivo adjunto descargable, preservando bytes y reportando SHA-256.

### 12.3 DOCX acumulativo candidato — handoff al autor

Generar a partir del baseline DOCX exacto:

`ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx`

Debe preservar exactamente el contenido ya aprobado y los 40 comentarios existentes, incorporando únicamente 3.5–3.7.

Entrégalo al autor como archivo adjunto descargable y reporta SHA-256.

### 12.4 Respuesta versionada — GitHub

Crear:

`article/responses/4_ARCHITECTURE_B02_RESPONSE_V01.md`

## 13. QA obligatorio

### Markdown

Verifica:

- Section MD = solo 3.5–3.7 Part I/Part II;
- cumulative candidate MD = baseline V008 + solo B02;
- Introduction, Related Work y 3.1–3.4 idénticos al baseline;
- Section 4 y posteriores idénticos al baseline;
- Part I/Part II semánticamente equivalentes;
- no resultados ni claims prohibidos.

Calcula SHA-256 de ambos Markdown.

### DOCX

Verifica:

- integridad OOXML;
- 40 comentarios heredados y anclajes válidos;
- `word/comments.xml` sin cambios respecto del baseline;
- 0 tracked changes;
- diff textual baseline→candidate limitado a 3.5–3.7;
- render completo;
- inspección visual de todas las páginas, sin clipping, solapamiento, truncamiento, glyphs faltantes ni pérdida de contenido.

Calcula SHA-256 final.

## 14. Regla timeout-safe vinculante

Conforme a D-035:

- NO Base64 manual;
- NO fragmentación/chunking;
- NO recomposición manual;
- NO reintentos seriales de un master grande por una vía que ya causó timeout;
- NO archivos auxiliares o blobs de prueba para evadir el handoff;
- section MD pequeña y response sí se versionan normalmente;
- cumulative candidate MD y DOCX se entregan exactamente al autor como adjuntos descargables;
- la IA Gestora verificará y materializará después el master acumulativo cuando corresponda.

La codificación interna utilizada automáticamente por una API/conector no está prohibida; la prohibición se refiere a convertir manualmente los artefactos en Base64 o fragmentarlos como workaround.

## 15. Contenido mínimo de la respuesta versionada

Registrar al menos:

```text
BLOCK = ARCHITECTURE_B02
GOVERNING_DECISION = D038
CANONICAL_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76 / PASS
BASELINE_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4 / PASS
SECTIONS_DRAFTED = 3.5 / 3.6 / 3.7 ONLY
INTRODUCTION_MODIFIED = NO
RELATED_WORK_MODIFIED = NO
SECTIONS_3_1_TO_3_4_MODIFIED = NO
SECTION_4_OR_LATER_MODIFIED = NO
RESULTS_LEAKAGE = NO
PROHIBITED_CLAIMS = NO
TOP3_MEMBERSHIP_AND_ORDER_IMMUTABLE = YES
DOCUMENTARY_STAGE_RERANKS_PRIMARY_TOP3 = NO
LLM_CLASSIFIES_OR_CHANGES_TOP3 = NO
CONFIGURABILITY_PRESENTED_AS_EMPIRICAL_GENERALIZATION = NO
REPRODUCIBILITY_REPOSITORY_ROLE_EXPLICIT = YES
DOCUMENTARY_CORPUS_ROLE_FOR_EXPLANATION_EXPLICIT = YES
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = <actual>
SECTION_MD_PATH = article/sections/architecture/Architecture_B02_V01.md
SECTION_MD_SHA256 = <actual>
SECTION_MD_GIT_BLOB = <actual>
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.md
MASTER_CANDIDATE_MD_SHA256 = <actual>
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
CANDIDATE_DOCX_SHA256 = <actual>
EXACT_LARGE_ARTIFACT_HANDOFF_TO_AUTHOR = COMPLETED
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V009 = NOT_PROMOTED
EXPERIMENTAL_DESIGN = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 16. Respuesta final en chat

Responde únicamente con:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/4_ARCHITECTURE_B02_RESPONSE_V01.md@<commit_sha>`

más los dos archivos descargables:

- `ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.md`;
- `ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx`.

No incluyas explicación adicional en chat. Detente después de B02.
