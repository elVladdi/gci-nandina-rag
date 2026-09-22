# Experimental Design B01 — Evaluation setting and historical data

## 1. Identidad del bloque

```text
BLOCK = EXPERIMENTAL_DESIGN_B01
GOVERNING_DECISION = article/governance/D041_EXPERIMENTAL_DESIGN_B01_OPENING.md
PARENT_DECISION = D-040
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
INHERITED_CITATION_COMMENTS = 40
AUTHORIZED_SCOPE = SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Ejecuta exclusivamente Experimental Design B01. No avances a Section 4.3 ni a ningún bloque posterior.

## 2. Rol

Actúa como IA de Redacción científica subordinada a la gobernanza del artículo. No eres IA Gestora ni IA Experimental. Debes redactar únicamente el bloque autorizado y entregar artefactos verificables para auditoría independiente.

No puedes autoasignar estados `APPROVED`, `FROZEN`, `INTEGRATED`, promover el master ni abrir otro gate.

## 3. Objetivo único

Completar exclusivamente, en Part I English y Part II Spanish semantic-control mirror:

- `4.1 Evaluation setting` / `Escenario de evaluación`;
- `4.2 Historical data` / `Datos históricos`;
- `4.2.1 Data source and selection` / `Fuente de datos y selección`;
- `4.2.2 Target class space` / `Espacio de clases objetivo`;
- `4.2.3 Preparation and curation` / `Preparación y curación`;
- `4.2.4 Versioned datasets used in the experiment` / `Datasets versionados utilizados en el experimento`.

La función narrativa es pasar de la arquitectura general ya cerrada a la instanciación experimental concreta. B01 debe permitir que el lector entienda **qué se evaluó, con qué datos históricos, cuál fue el espacio empírico de códigos, cómo se prepararon/curaron los datos y cuáles son las identidades congeladas de H100, DEV y EVAL**, sin anticipar resultados ni repetir Section 3.

## 4. Onboarding y control de precedencia obligatorio

Antes de redactar:

1. confirma repo `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`;
2. lee `article/START_HERE.md`;
3. lee `article/README.md`;
4. lee `article/ARTICLE_STATUS.md`;
5. lee `article/ARTICLE_WRITING_PLAN.md`;
6. lee `article/governance/D040_ARCHITECTURE_B02_INTEGRATION_AND_V009_PROMOTION.md`;
7. lee `article/governance/D041_EXPERIMENTAL_DESIGN_B01_OPENING.md`;
8. lee `article/SOURCE_REGISTRY.md`;
9. lee `article/CLAIM_EVIDENCE_MATRIX.md`;
10. lee `article/STYLE_GUIDE.md`;
11. verifica `article/manuscript/ARTICLE_MASTER_V009.md` y su Git blob `40f20437458715c615fc1762f025ebcdbb3b6fc2`;
12. verifica el DOCX baseline local exacto `ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx` con SHA-256 `09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657`.

Antes de producir prosa, aplica el control de precedencia: D-021, D-022, D-023, D-035, D-040 y D-041 son vinculantes. Si una instrucción heredada o un artefacto legado contradice estas decisiones, no la sigas silenciosamente: prevalece la gobernanza vigente y debes registrar el conflicto en la respuesta.

Si el DOCX baseline no está disponible o el SHA no coincide, detente con:

`EXPERIMENTAL_DESIGN_B01_BASELINE_DOCX_MISMATCH`

No reconstruyas el DOCX desde Markdown.

## 5. Fuentes experimentales primarias obligatorias

No uses una respuesta previa de otra IA como ground truth. Verifica directamente las fuentes siguientes.

### 5.1 Plan Maestro experimental vivo

```text
REPOSITORY = elVladdi/gci-nandina-rag
BRANCH = docs/plan-maestro-temporal-2026-08-31
HEAD_VERIFIED_AT_OPENING = b74b96d0163807007e4579d86450dd235125b30f
PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
BLOB_VERIFIED_AT_OPENING = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
```

`SRC-03` es fuente viva. Lee la rama/ruta gobernante al iniciar la ejecución. Si el HEAD/blob cambió, no bloquees por el mero cambio: determina si modifica hechos necesarios para B01. Si cambia una identidad, conteo, unidad, provenance claim o decisión usada en B01, detente con `EXPERIMENTAL_DESIGN_B01_SRC03_MATERIAL_CHANGE` y registra la discrepancia en la respuesta GitHub.

### 5.2 Checkpoint de desarrollo

Para los hechos técnicos concretos de B01, usa como mínimo el checkpoint:

`main@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`

Verifica directamente:

1. `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`
   - Git blob esperado: `bcb02c9c3493235a6f80991158c5b24fa7c04510`.
2. `src/configs/data_aduanas_split_clase87_v0.2.json`
   - Git blob esperado: `059eb81677dad92d6f9241f0b8cbbff9bba332cd`.
3. `docs/exp04_bm25_historico_v02_inventory.md`
   - Git blob esperado: `64e7049ae8fb056a5fcc2173b39bdcb244567a89`.
4. `src/ingestion/sunat_series_parser.py`
   - Git blob esperado: `87dafb5f2b5f1febfc588b7b763adc9ab5523339`.
5. `src/ingestion/prepare_new_historical_multisheet_v0.1.py`
   - Git blob esperado: `748c7b7ed7d55a1c2f05a76e1b382ee0077f158f`.
6. Cualquier script/config adicional estrictamente necesario para verificar una frase de preparación/curación. Si no puedes demostrar una operación, no la inventes.

El checkout técnico puede haber avanzado después de la apertura. Un cambio posterior de `main` no invalida automáticamente el checkpoint anterior; usa el checkpoint citado para reproducir la evidencia gobernante de B01 salvo que `SRC-03` registre una sustitución material posterior.

### 5.3 Artefacto legado

Puedes consultar:

`article/sections/methods/Methods_B01_V05.md`

solo como **artefacto legado de redacción previamente auditada**, nunca como fuente primaria ni como estructura canónica. No copies párrafos de configurabilidad que ya quedaron resueltos en Section 3.7. Si el legado contradice `SRC-03` o un artefacto experimental congelado, prevalece la fuente primaria.

## 6. Búsqueda de literatura y web

```text
NEW_LITERATURE_SEARCH = NOT_AUTHORIZED
WEB_SEARCH = NOT_AUTHORIZED
NEW_REFERENCES = NOT_AUTHORIZED
```

Este bloque debe sostenerse con las fuentes internas gobernantes y artefactos experimentales primarios. No añadas citas bibliográficas nuevas.

## 7. Ground truth mínimo que debe quedar correctamente representado

### 7.1 Escenario de evaluación

- evaluación offline;
- piloto de apoyo a decisiones no vinculante;
- dominio empírico delimitado: **NANDINA Chapter 87**;
- SERIE = unidad de análisis;
- DAM/declaración = unidad de agrupamiento cuando existe dependencia entre series de una misma declaración;
- la arquitectura general no queda limitada conceptualmente a Chapter 87, pero B01 describe solo la instanciación realmente evaluada;
- no describas el piloto como validación jurídica, despliegue operativo en aduanas ni clasificación legalmente vinculante.

### 7.2 Datasets v0.2 congelados

Debes conservar exactamente:

```text
H100_FILE = data/processed/data_aduanas_historico_clase87_v0.2.csv
H100_SERIES = 2950
H100_DAM = 28
H100_REPRESENTED_CODES = 66
H100_SHA256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff

DEV_FILE = data/processed/data_aduanas_devset_clase87_v0.2.csv
DEV_SERIES = 100
DEV_DAM = 6
DEV_REPRESENTED_CODES = 9
DEV_SHA256 = 434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00

EVAL_FILE = data/processed/data_aduanas_evalset_clase87_v0.2.csv
EVAL_SERIES = 1056
EVAL_DAM = 67
EVAL_REPRESENTED_REFERENCE_CODES = 42
EVAL_SHA256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

No escribas que los 66 códigos de H100 son el universo exhaustivo de Chapter 87. Son **códigos representados en el banco histórico H100** de esta instanciación. Los 42 de EVAL son **etiquetas/códigos de referencia representados en EVAL**.

### 7.3 Split v0.2

La metadata/configuración congelada documenta:

```text
VERSION = v0.2
STRATEGY = T5-safe-159
GROUPING_FIELD = DECLARACION
ANALYSIS_UNIT = SERIE
ELIGIBLE_CLASS = 87
SELECTION_POLICY = explicit_dam_assignment_no_heuristic_search_no_model_metrics
TOTAL_CURATED_RECORDS = 4106
FULL_ASSIGNMENT = true
ZERO_DAM_OVERLAP_ACROSS_PARTITIONS = true
ZERO_ID_UNICO_OVERLAP_ACROSS_PARTITIONS = true
EVAL_CASES_WITH_NOMINAL_HISTORICAL_SUPPORT = 1056/1056
```

`seed = 2026` aparece en configuración/procedencia, pero **no describas v0.2 como un split aleatorio producido por esa seed**. v0.2 queda materializado mediante listas explícitas de DAM. La seed debe mencionarse solo si una frase de provenance/configuration realmente lo necesita y siempre con esta distinción.

El detalle de cómo se detectaron y cuantificaron duplicados exactos, near-duplicates, concentración y dependencia pertenece principalmente a 4.4. En B01 puedes decir que el split está agrupado por DAM y que las identidades v0.2 están congeladas, pero no conviertas esta subsección en un análisis de validez.

### 7.4 Procedencia histórica y límite forense

Verifica en `SRC-03` la reconstrucción forense antes de redactar. La redacción debe preservar, como mínimo, esta frontera:

- workbook actual: `data/Series - Descripciones.xlsx`;
- SHA-256 actual: `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`;
- la fuente histórica completa no es byte-identificable con el workbook actual;
- la metadata histórica registraba un SHA distinto del workbook actual;
- el procesamiento histórico utilizó `Hoja2`, índice 0, como primera worksheet cuando no se especificaba `--sheet`;
- el intermedio reproducido contiene 107 DAM / 11,320 series;
- el filtrado de Chapter 87 dejó 4,232 filas antes de la curación y 4,106 registros curados;
- H100, DEV y EVAL v0.2 fueron reproducidos byte a byte;
- el pipeline se clasifica conservadoramente como `PIPELINE_PARTIALLY_RECONSTRUCTED`.

En prosa publicable, **no conviertas el label interno `PIPELINE_PARTIALLY_RECONSTRUCTED` en jerga de gobernanza** si puede expresarse naturalmente. Debe quedar claro que la reproducibilidad del conjunto procesado v0.2 está respaldada, pero que no se afirma identidad binaria del workbook histórico original. No digas que el workbook actual *es* el workbook histórico original.

### 7.5 Preparación y curación

Describe únicamente operaciones que puedas verificar en los scripts/configs y artefactos citados. Debes diferenciar:

- extracción/lectura de la fuente;
- selección del ámbito Chapter 87;
- preparación/curación del registro de series;
- construcción/materialización de las particiones v0.2.

No inventes reglas de limpieza, imputación, eliminación, deduplicación o normalización. Si una operación no está inequívocamente documentada, omítela o señálala en la respuesta como no demostrada.

La normalización textual utilizada para retrieval histórico ya fue descrita arquitectónicamente en 3.2; sus parámetros exactos pertenecen principalmente a 4.5. No sobrecargues 4.2.3 con detalles del modelo/retriever.

## 8. Claims autorizados y prohibidos

### Autorizados relevantes

- C06: el split v0.2 evita solapamiento de DAM entre histórico, desarrollo y evaluación;
- C07: la dependencia intra-DAM debe considerarse cuando una inferencia requiera independencia;
- C19: el solapamiento del split v0.1 puede aparecer solo como snapshot histórico si fuera necesario para explicar la motivación metodológica; **preferencia B01: no usarlo salvo que sea imprescindible**;
- C21: drift normativo/documental, dentro de sus límites, pero **preferencia B01: diferirlo a 4.3/4.4/Limitations salvo necesidad directa**.

### Prohibidos / no autorizados para B01

- C20: no usar `48/59 DAM` como cifra congelada;
- C12/C13: no convertir evidencia/explanation en corrección jurídica;
- C16: no declarar generalización empírica fuera de Chapter 87;
- C18: no presentar clasificaciones jurídicamente vinculantes;
- no introducir C04/C05 ni métricas de candidate retrieval en este bloque;
- no introducir resultados HE2/HE5 ni EXP11A/EXP11B/EXP12;
- no declarar novelty, SOTA, first-of-its-kind, superioridad o `FINAL_GAP`.

## 9. Relación con Section 3 y siguientes subsecciones

### Con Section 3

No repitas la arquitectura completa. Section 3 ya fijó:

`historical ranking → fixed Top-3 → documentary evidence → context → local LLM explanation`.

B01 debe limitarse a **cómo se instanció empíricamente** el estudio y a las identidades de los datos históricos.

### Con Section 4.3

No describas aún el corpus documental/normativo concreto, su preparación, vigencia temporal, segmentación o índice. Eso pertenece a 4.3.

### Con Section 4.4

No desarrolles todavía la auditoría de dependencia, leakage, duplicados exactos, near-duplicates o concentración. Puedes establecer que el diseño v0.2 usa DAM como unidad de agrupamiento y no tiene solapamiento DAM entre particiones, pero el diagnóstico detallado pertenece a 4.4.

### Con 4.5–4.11

No adelantes parámetros de BM25, candidate depth, configuración del LLM, prompts, evaluación por RQ, métricas, análisis estadístico ni inventario completo del repositorio de reproducibilidad. Esos elementos tendrán bloques posteriores.

## 10. Estilo científico

- prosa concreta y observable;
- evitar lenguaje de tesis excesivamente didáctico;
- minimizar abstracciones y nominalizaciones;
- no trasladar nombres D-xxx, gates, nombres internos de grupos o estados al manuscrito;
- no narrar la historia de auditoría interna del proyecto;
- no usar “robust”, “accurate”, “validated”, “correct”, “generalizable” o equivalentes sin soporte y scope explícito;
- Part I debe leerse como inglés científico original;
- Part II debe ser espejo semántico natural en español;
- no introducir referencias bibliográficas nuevas.

Extensión orientativa total del bloque: **900–1,300 palabras por idioma**, salvo que la precisión metodológica requiera una variación moderada. Prioriza economía expresiva; no rellenes para alcanzar el rango.

## 11. Preservación obligatoria del master

En el master acumulativo:

- Front matter: sin cambios;
- Introduction: sin cambios;
- Related Work: sin cambios;
- Section 3.1–3.7: sin cambios;
- 4.1 y 4.2.1–4.2.4: únicos placeholders/instrucciones sustituibles;
- 4.3 y posteriores: sin cambios;
- 40 comentarios heredados: preservar exactamente;
- tracked changes: 0.

No elimines Figure 1 placeholder ni ningún placeholder fuera del scope autorizado.

## 12. Prohibiciones operativas

No:

- modifiques gobernanza, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `SOURCE_REGISTRY.md` o `CLAIM_EVIDENCE_MATRIX.md`;
- modifiques `ARTICLE_MASTER_V009.md`;
- redactes 4.3 o subsecciones posteriores;
- redactes Results, Discussion, Conclusion, Abstract, Title o Keywords;
- cambies cifras/hashes;
- reconstruyas el DOCX desde Markdown;
- promuevas `ARTICLE_MASTER_V010`;
- abras un bloque posterior;
- intentes transferir directamente el master acumulativo grande por la vía que ya produjo timeout;
- uses Base64 manual, fragmentación, chunking, reensamblado, archivos auxiliares, ramas temporales o múltiples commits como workaround.

## 13. Artefactos requeridos

### 13.1 Archivo de sección — GitHub

Crear:

`article/sections/experimental_design/Experimental_Design_B01_V01.md`

Debe contener exclusivamente 4.1 y 4.2.1–4.2.4, Part I + Part II. Es relativamente pequeño y debe versionarse directamente en GitHub.

### 13.2 Master Markdown acumulativo candidato — handoff timeout-safe

Generar localmente:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.md`

Debe derivar exactamente de `ARTICLE_MASTER_V009.md`, sustituyendo únicamente los placeholders/instrucciones autorizados de 4.1 y 4.2.1–4.2.4.

**No lo transfieras directamente por la vía grande que ya produjo timeout.** Entrégalo al autor como archivo adjunto descargable exacto y reporta SHA-256 en la respuesta versionada.

### 13.3 DOCX acumulativo candidato — handoff al autor

Generar a partir del baseline DOCX exacto:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.docx`

Debe preservar contenido previo y 40 comentarios existentes e incorporar únicamente B01. Entrégalo al autor como archivo adjunto descargable exacto y reporta SHA-256.

### 13.4 Respuesta operacional — GitHub

Crear:

`article/responses/5_EXPERIMENTAL_DESIGN_B01_RESPONSE_V01.md`

La respuesta debe ser bilingüe y registrar al menos:

```text
BLOCK = EXPERIMENTAL_DESIGN_B01
SOURCE_MASTER_V009_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2 / PASS
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657 / PASS
SRC03_HEAD_READ = <actual>
SRC03_BLOB_READ = <actual>
SRC03_MATERIAL_CHANGE = NO / YES
AUTHORIZED_SCOPE_ONLY = PASS
INTRODUCTION_MODIFIED = NO
RELATED_WORK_MODIFIED = NO
ARCHITECTURE_3_1_TO_3_7_MODIFIED = NO
SECTION_4_3_AND_LATER_MODIFIED = NO
RESULTS_LEAKAGE = NONE
NEW_LITERATURE = NONE
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = <actual>
SECTION_MD_PATH = article/sections/experimental_design/Experimental_Design_B01_V01.md
SECTION_MD_SHA256 = <actual>
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.md
MASTER_CANDIDATE_MD_SHA256 = <actual>
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.docx
CANDIDATE_DOCX_SHA256 = <actual>
DIRECT_LARGE_MASTER_GITHUB_TRANSFER = NOT_ATTEMPTED / D035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3 = NOT_STARTED
RESULTS = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Incluye una tabla breve `claim/fact → primary source → scope` y una lista de cualquier punto omitido por evidencia insuficiente.

## 14. QA obligatorio

### Markdown

Verifica:

- section MD = solo 4.1 y 4.2.1–4.2.4, Part I/Part II;
- cumulative candidate MD = V009 + solo B01;
- Introduction, Related Work y Section 3 exactos al baseline;
- 4.3 y posteriores exactos al baseline;
- equivalencia semántica EN/ES;
- no resultados, nuevas referencias ni claims prohibidos.

### DOCX / OOXML

Verifica:

- integridad ZIP/OOXML;
- 40 comentarios finales;
- 40 `commentRangeStart`, 40 `commentRangeEnd`, 40 `commentReference`;
- `word/comments.xml` inalterado respecto del baseline; SHA esperado `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`;
- 0 tracked changes;
- único contenido textual nuevo dentro de 4.1 y 4.2.1–4.2.4;
- render completo de todas las páginas;
- inspección visual página por página para clipping, overlap, truncamiento, glyph loss, tablas rotas, problemas de encabezado/pie y pérdida de contenido.

No declares `FULL_RENDER_QA = PASS` sin inspeccionar todas las páginas.

## 15. Condiciones de parada

Detente sin redactar o sin continuar si ocurre cualquiera de estas condiciones:

- baseline DOCX hash mismatch;
- V009 blob mismatch;
- `SRC-03` no accesible;
- cambio material en `SRC-03` que altere hechos usados en B01;
- conflicto irresuelto entre fuentes primarias;
- dato metodológico necesario sin soporte primario;
- pérdida/corrupción de comentarios o tracked changes inesperados;
- imposibilidad de producir/entregar exactamente los artefactos grandes mediante handoff seguro.

No resuelvas una parada inventando datos, reconstruyendo el Word, fragmentando artefactos o ampliando scope.

## 16. Estados que esta ejecución no puede conceder

La IA de Redacción no puede declarar:

```text
EXPERIMENTAL_DESIGN_B01 = APPROVED
EXPERIMENTAL_DESIGN_B01 = FROZEN
EXPERIMENTAL_DESIGN_B01 = INTEGRATED
ARTICLE_MASTER_V010 = CANONICAL
SECTION_4_3 = AUTHORIZED
RESULTS = AUTHORIZED
FINAL_GAP = DEFINED
NOVELTY = DECLARED
```

## 17. Mensaje final en chat

Conforme a D-022, al terminar responde en chat únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/5_EXPERIMENTAL_DESIGN_B01_RESPONSE_V01.md@<commit_sha>`

y adjunta como archivos descargables exactos:

- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.md`;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.docx`.

No repitas en chat hashes, QA, hallazgos científicos ni contenido sustantivo de la respuesta.
