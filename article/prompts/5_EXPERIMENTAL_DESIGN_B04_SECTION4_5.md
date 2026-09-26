# Prompt — Experimental Design B04 / Section 4.5

## Rol

Actúa como **IA de Redacción** del artículo científico principal destinado a *Knowledge-Based Systems*. Ejecuta exclusivamente `EXPERIMENTAL_DESIGN_B04`, limitado a Section 4.5 y su espejo español.

No eres la autoridad de cierre experimental. Debes verificar cada afirmación factual directamente contra las fuentes primarias versionadas y respetar las fronteras editoriales fijadas por la IA Gestora.

## 1. Onboarding obligatorio

Trabaja en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Lee primero `article/START_HERE.md` y completa íntegramente el onboarding que allí se exige. Después lee, como mínimo:

- `article/governance/D058_EXPERIMENTAL_DESIGN_B03_INTEGRATION_AND_V012_PROMOTION.md`;
- `article/governance/D059_EXPERIMENTAL_DESIGN_B04_SECTION4_5_START.md`;
- `article/manuscript/ARTICLE_MASTER_V012.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

No uses el ground truth congelado como sustituto de las fuentes experimentales vivas cuando estas hayan avanzado.

## 2. Baselines exactos obligatorios

### Markdown canónico

`article/manuscript/ARTICLE_MASTER_V012.md`

SHA-256 obligatorio:

`d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`

Git blob obligatorio:

`dfea73f5f462fc65cf98347f796deadc6da58455`

Antes de redactar, verifica que GitHub siga exponiendo ese blob para V012. Si no coincide, detente y reporta drift.

### DOCX acumulativo

El autor debe proporcionarte como adjunto:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`

SHA-256 obligatorio:

`9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`

Calcula el hash antes de editar. Si el binario no está disponible o no coincide exactamente, **detente** con:

`BLOCKED_MISSING_EXACT_B03_DOCX_BASELINE`

Está prohibido reconstruir el DOCX desde Markdown, HTML, PDF, texto plano u otro Word anterior.

## 3. Único alcance científico autorizado

Redacta exclusivamente:

- Part I — `4.5 Historical retrieval configuration and candidate-generation protocol`;
- Part II — `4.5 Configuración de la recuperación histórica y protocolo de generación de candidatos`.

La sección debe explicar, con precisión suficiente para reproducibilidad metodológica:

1. cuál es el banco histórico usado por el benchmark vigente y cuál es el campo textual de consulta;
2. cómo se normaliza/tokeniza la consulta según la implementación realmente ejecutada;
3. que la recuperación principal es lexical BM25 sobre registros históricos y cuáles fueron los parámetros efectivamente ejecutados (`k1`, `b`, profundidades pertinentes), únicamente si quedan verificados en fuente primaria;
4. cómo se ordenan los registros recuperados y cuál es la regla de desempate realmente implementada;
5. cómo se transforma el ranking de registros históricos en ranking de códigos NANDINA únicos;
6. que para cada código se conserva la primera/mejor aparición histórica según el ranking ejecutado, con su precedente asociado;
7. que los tres primeros códigos únicos constituyen el **fixed Top-3** que se entrega a las etapas posteriores;
8. que la recuperación normativa y el LLM operan después de que ese Top-3 haya quedado fijado y no pueden modificar composición u orden;
9. qué información de trazabilidad del candidato/precedente queda disponible según los artefactos realmente ejecutados;
10. qué parámetros/configuraciones son específicos de esta instanciación experimental y cuáles interfaces pertenecen al framework configurable, sin afirmar generalización de desempeño.

No conviertas esta lista en una enumeración mecánica si una prosa científica compacta resulta más natural.

## 4. Fuentes experimentales obligatorias

Consulta directamente el estado vivo de `main` y registra el commit leído. Como mínimo verifica:

- `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py`;
- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json`;
- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`;
- los CSV/artefactos de historical retrieval que sean necesarios para comprobar campos y trazabilidad.

Si consultas `src/bm25_index.py` o `src/retrieval/bm25.py`, distingue cuidadosamente utilidades generales del código específico que produjo el resultado congelado. No atribuyas al experimento una opción de stopwords, tokenización o configuración solo porque exista en una utilidad genérica.

No uses búsqueda web ni literatura externa para completar detalles de implementación. Este bloque es Methods del experimento ejecutado.

## 5. Claims autorizados y prohibidos

### Autorizados

Puedes describir hechos metodológicos directamente verificables, incluidos, si la fuente primaria los confirma:

- H100 como banco histórico vigente de 2,950 series;
- EVAL como conjunto de 1,056 series cuando sea necesario para explicar la ejecución del protocolo, sin narrar resultados;
- `DESCRIPCION DE MERCANCIAS CONCATENADA` como query y `NANDINA` como label/reference field;
- BM25 con `k1=1.5`, `b=0.75`;
- `history_depth=2950` y `candidate_depth=100` del run congelado;
- deduplicación por NANDINA;
- fixed Top-3 aguas abajo;
- ausencia de LLM, Ollama, APIs remotas y recuperación normativa como fuentes de candidatos en esta etapa, si se formula como frontera de implementación y se verifica en el artefacto primario.

### Prohibidos en 4.5

No incluyas:

- Top-1, Top-3, Top-5, Top-10, Top-50, MRR u otros valores observados de desempeño;
- resultados de HE2 o sus intervalos/inferencia;
- resultados EXP11A/EXP11B;
- afirmaciones de superioridad frente a normative retrieval o dense retrieval;
- resultados de exact/near duplicates ya tratados metodológicamente en 4.4;
- resultados de integración candidato–evidencia;
- resultados de explicación/auditabilidad;
- `accuracy` global del RAG/sistema;
- claims de legal correctness;
- `FINAL_GAP` o `NOVELTY`;
- afirmaciones de generalización fuera del Chapter-87 testbed.

## 6. Estilo científico obligatorio

Mantén el estilo ya aprobado del manuscrito:

- prosa científica directa, concreta y verificable;
- evita abstracciones vacías y lenguaje promocional;
- no conviertas detalles simples de implementación en formulaciones grandilocuentes;
- explica suficiente mecanismo para que el lector entienda qué se hizo y pueda re-instanciarlo con su propio banco histórico/clases, sin confundir reproducibilidad/configurabilidad con transferencia de desempeño;
- no repitas innecesariamente 3.1–3.7 ni 4.1–4.4;
- no presentes el framework como específico de NANDINA: NANDINA/Chapter 87 es la instanciación empírica;
- English publication-facing master primero; espejo español semánticamente equivalente después.

## 7. Entregables Markdown obligatorios

Crea y versiona en GitHub:

1. `article/sections/experimental_design/Experimental_Design_B04_V01.md`
   - encabezado de trazabilidad;
   - Part I English manuscript text;
   - Part II Spanish semantic-control mirror.

2. `article/responses/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_RESPONSE_V01.md`
   - fuentes y commits realmente leídos;
   - matriz breve claim → fuente primaria;
   - controles de scope;
   - QA de Markdown y DOCX;
   - hashes finales.

Además genera localmente, a partir de V012 exacto:

3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md`

Solo pueden cambiar los placeholders de Section 4.5 en Part I y Part II. Sections 1–4.4 y 4.6+ deben permanecer byte-equivalentes en contenido respecto de V012 fuera de las sustituciones estrictamente necesarias de esos placeholders.

Reporta SHA-256 del candidato y, si lo materializas en Git, el blob correspondiente. No es obligatorio subir el master candidato a GitHub si la gobernanza vigente mantiene el handoff por hash/archivo exacto.

## 8. DOCX acumulativo obligatorio

Partiendo exclusivamente del DOCX B03 exacto:

- sustituye únicamente los placeholders de Section 4.5 en las partes inglesa y española por el contenido B04 aprobado en esta ejecución;
- conserva Sections 1–4.4 y 4.6+;
- preserva estilos, estructura, numeración, saltos, tablas, captions y comentarios/anclajes heredados;
- no elimines comentarios de citas existentes;
- no agregues comentarios de citas salvo que 4.5 incorpore una fuente bibliográfica nueva, lo cual en principio no es necesario para este bloque metodológico;
- `tracked changes = 0`;
- no reconstruyas el Word completo.

Nombre obligatorio:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx`

Este DOCX debe entregarse al autor como archivo descargable y permanecer bajo custodia local del autor; no lo subas al repositorio salvo instrucción posterior expresa.

## 9. QA obligatorio del DOCX

Verifica y reporta antes de entregar:

- hash del baseline B03 = PASS;
- SHA-256 del candidato B04;
- ZIP/OOXML integrity = PASS;
- XML/RELS parse = PASS;
- `word/document.xml` legible = PASS;
- comentarios heredados: conteo, starts, ends y references preservados = PASS;
- tracked changes = 0;
- Section 4.5 EN presente = PASS;
- Section 4.5 ES presente = PASS;
- Section 4.6 boundary EN/ES presente = PASS;
- equivalencia semántica EN/ES = PASS;
- Sections 1–4.4 sin cambios de contenido = PASS;
- Sections 4.6+ sin cambios de contenido = PASS;
- render completo del DOCX = PASS, sin corrupción, truncamiento ni pérdida material de formato.

## 10. Autocontrol científico antes de cerrar

Comprueba explícitamente:

```text
HISTORICAL_RETRIEVAL = CANDIDATE_GENERATOR / RANKER
FIXED_TOP3 = FIRST_THREE_UNIQUE_NANDINA_CODES
NORMATIVE_RETRIEVAL_CAN_RERANK = FALSE
LLM_CAN_RERANK = FALSE
CANDIDATE_RETRIEVAL != GLOBAL_CLASSIFICATION_ACCURACY
FRAMEWORK_CONFIGURABILITY != EMPIRICAL_GENERALIZATION
RESULTS_VALUES_IN_4_5 = NONE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Si alguna afirmación de la sección no puede trazarse a evidencia primaria, elimínala o reporta bloqueo; no la completes por plausibilidad.

## 11. Gate de salida

Detente después de producir B04 V01, el master Markdown candidato, el DOCX acumulativo candidato y la respuesta versionada.

No redactes 4.6, 4.7, 4.8 ni Results.

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```

Responde únicamente en español en el chat y entrega al autor el DOCX candidato generado.