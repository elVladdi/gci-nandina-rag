# Experimental Design B01 V02 — rewrite under Structure V02

## 1. Identidad del bloque

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
GOVERNING_DECISION = article/governance/D046_EXPERIMENTAL_DESIGN_B01_REOPENING_UNDER_STRUCTURE_V02.md
PARENT_DECISION = D-045
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_GIT_BLOB = f5270e02e3af1407a2dec2988d6382e433972d3e
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
INHERITED_CITATION_COMMENTS = 40
AUTHORIZED_SCOPE = SECTION_3_TWO_FORWARD_REFERENCE_EDITORIAL_AMENDMENTS_PLUS_SECTION_4_1_AND_4_2_1_TO_4_2_3
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Ejecuta exclusivamente este bloque. La versión B01 V02 previamente observada **no es baseline** y no debe editarse incrementalmente. Debes partir del master canónico V009 y del DOCX baseline exacto indicado.

## 2. Rol

Actúa exclusivamente como IA de Redacción científica subordinada a la gobernanza del artículo. No eres IA Gestora ni IA Experimental. No puedes modificar el Plan Maestro experimental, promover un master, autoasignar estados `APPROVED`, `FROZEN` o `INTEGRATED`, ni abrir 4.3 o bloques posteriores.

## 3. Objetivo único

Reescribir el primer bloque de Experimental Design conforme a Structure V02 para que Methods explique **cómo se evaluó experimentalmente una instanciación concreta de la arquitectura**, y no una herramienta operativa ni un inventario de artefactos del repositorio.

Debes completar, en Part I English y Part II Spanish semantic-control mirror:

- dos enmiendas editoriales precisas de forward-reference en 3.5 y 3.7;
- `4.1 Experimental setting and scope` / `Entorno y alcance experimental`;
- `4.2 Historical data and experimental dataset construction` / `Datos históricos y construcción de los datasets experimentales`;
- `4.2.1 Source and data collection` / `Fuente y recolección`;
- `4.2.2 Processing and curation` / `Procesamiento y curación`;
- `4.2.3 Partition construction and dataset composition` / `Construcción de particiones y composición`.

No redactes 4.3 ni posteriores.

## 4. Onboarding y control de precedencia

Antes de redactar, confirma repo `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`, y lee íntegramente:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`;
6. `article/governance/D044_SECTION4_CONCEPTUAL_REOPENING_AND_PRIOR_PROMPT_SUPERSESSION.md`;
7. `article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md`;
8. `article/governance/D046_EXPERIMENTAL_DESIGN_B01_REOPENING_UNDER_STRUCTURE_V02.md`;
9. `article/reviews/5_EXPERIMENTAL_DESIGN_SECTION4_CONCEPTUAL_REAUDIT_V01.md`;
10. `article/reviews/5_EXPERIMENTAL_DESIGN_SECTION4_RESTRUCTURE_PROPOSAL_V01.md`;
11. `article/SOURCE_REGISTRY.md`;
12. `article/CLAIM_EVIDENCE_MATRIX.md`;
13. `article/STYLE_GUIDE.md`;
14. `article/manuscript/ARTICLE_MASTER_V009.md` y verifica Git blob `40f20437458715c615fc1762f025ebcdbb3b6fc2`;
15. DOCX local exacto `ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx` y verifica SHA-256 `09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657`.

Decisiones activas a respetar explícitamente: D-021, D-022, D-023, D-034, D-035, D-040, D-044, D-045 y D-046. D-043 permanece como antecedente del defecto editorial. El prompt `5_EXPERIMENTAL_DESIGN_B01_KBS34_PROSE_CORRECTION.md` está superado y **no debe ejecutarse**.

Si el DOCX baseline no está disponible o el SHA no coincide, detente con:

`EXPERIMENTAL_DESIGN_B01_V02_BASELINE_DOCX_MISMATCH`

No reconstruyas el DOCX desde Markdown.

## 5. Fuentes gobernantes y precedencia por dimensión

No uses una respuesta previa de otra IA ni la B01 observada como ground truth.

### 5.1 SRC-03 — Plan Maestro experimental vivo

```text
REPOSITORY = elVladdi/gci-nandina-rag
BRANCH = docs/plan-maestro-temporal-2026-08-31
PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
LAST_EDITORIAL_HEAD = b74b96d0163807007e4579d86450dd235125b30f
LAST_EDITORIAL_BLOB = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
```

Lee el estado vivo al iniciar. Si HEAD/blob cambió, determina si modifica hechos necesarios para este bloque. Si cambia materialmente una unidad, conteo, regla de split, provenance claim o decisión usada, detente con `EXPERIMENTAL_DESIGN_B01_V02_SRC03_MATERIAL_CHANGE`.

### 5.2 SRC-02 — metodología operativa vigente

Usa el archivo de Project/Library identificado científicamente como:

`Anexo_1_NANDINA_LLM_RAG_v13.docx`

Es fuente requerida para el procedimiento de origen/recolección y la metodología operativa, **siempre subordinada a SRC-03 y a los artefactos experimentales congelados cuando una formulación prospectiva de v13 haya sido sustituida por lo realmente ejecutado**.

Si el archivo exacto v13 no está disponible, detente con:

`EXPERIMENTAL_DESIGN_B01_V02_SRC02_UNAVAILABLE`

### 5.3 Fuentes técnicas congeladas

Como mínimo, verifica directamente en el checkpoint de desarrollo gobernante registrado en `SOURCE_REGISTRY.md`:

- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`;
- `src/configs/data_aduanas_split_clase87_v0.2.json`;
- `docs/exp04_bm25_historico_v02_inventory.md`;
- `src/ingestion/sunat_series_parser.py`;
- `src/ingestion/prepare_new_historical_multisheet_v0.1.py`;
- `build_data_aduanas_splits.py` o el script congelado que gobierne las reglas de curación/partición;
- cualquier artefacto adicional estrictamente necesario para verificar una frase.

No inventes una operación que no puedas demostrar.

### 5.4 Precedencia

1. Estado experimental, composición final y reglas ejecutadas: `SRC-03` + artefactos congelados.
2. Procedimiento de consulta administrativa/acopio y metodología operativa: `SRC-02`, salvo contradicción con lo ejecutado.
3. Problema/objetivos/alcance aprobado: `SRC-01` cuando sea necesario.
4. Tesis preliminar: solo comparación, nunca sustitución de 1–3.
5. KBS-34: controla forma y nivel de detalle publicable, no hechos experimentales.

Toda contradicción material debe registrarse y detener la ejecución; no reconciliar silenciosamente.

## 6. Búsqueda externa

```text
NEW_LITERATURE_SEARCH = NOT_AUTHORIZED
WEB_SEARCH = NOT_AUTHORIZED
NEW_REFERENCES = NOT_AUTHORIZED
```

No se necesitan nuevas citas bibliográficas para este bloque.

## 7. Ground truth y función narrativa por subsección

### 7.1 Enmiendas editoriales de Section 3

Solo se permiten dos cambios mínimos:

- **3.5**: corregir la frase que promete que Section 4 especificará `hashes` como parte de la narrativa metodológica. Section 4 puede documentar los recursos/condiciones concretos; las identidades exhaustivas quedan en reproducibility resources/manifests.
- **3.7**: corregir la frase que presenta la futura subsección de reproducibilidad como un inventario narrativo de identidades técnicas. Debe explicar que el repositorio conserva los recursos e identificadores necesarios para reconstrucción, sin anticipar una lista de hashes/rutas en Methods.

No cambies ninguna otra afirmación, función, interfaz, autoridad de componente ni frontera de Section 3.

### 7.2 Section 4.1 — Experimental setting and scope

Debe quedar claro:

- se realiza una **evaluación experimental offline** de una instanciación concreta de la arquitectura;
- dominio empírico: NANDINA de ocho dígitos, Chapter 87;
- SERIE = unidad de análisis;
- DAM/declaración = unidad de agrupamiento cuando la dependencia entre series de una misma declaración es metodológicamente relevante;
- condiciones controladas y alcance empírico delimitado;
- el escenario evaluado no redefine el alcance conceptual de la arquitectura;
- configurabilidad/reinstanciación con otros bancos, clases, profundidades o corpus no implica transferencia del desempeño observado.

No uses como formulación rectora `non-binding decision-support pilot` / `piloto no vinculante de apoyo a decisiones`. Si la ausencia de efecto jurídico necesita mencionarse, debe aparecer como límite secundario y no como definición del experimento.

Preferir `evaluate/evaluar`. No usar `validate/validar` como claim general.

### 7.3 Section 4.2.1 — Source and data collection

La narrativa debe comenzar por la **fuente administrativa real**, no por el workbook intermedio.

Verifica en SRC-02 y conserva, si no existe contradicción posterior:

- portal Aduanet de SUNAT;
- régimen: importación para el consumo;
- Aduana Marítima del Callao, código 118;
- declaraciones numeradas entre el **2 de enero y el 30 de marzo de 2026**;
- acopio realizado entre el **11 y el 20 de abril de 2026**;
- declaraciones de canal naranja o rojo;
- fecha de cancelación registrada y levante autorizado;
- DAM con al menos una partida de Chapter/Class 87;
- después de identificar las DAM elegibles se ingresó a cada declaración y se copiaron manualmente sus series al registro inicial;
- las capturas de consulta se conservaron como evidencia del procedimiento y no como fuente adicional de etiquetas.

Explica qué información era necesaria para representar cada SERIE y vincularla con su DAM y código de referencia administrativo, solo hasta el nivel respaldado por las fuentes.

El workbook/Excel inicial puede mencionarse genéricamente como **registro intermedio de recolección** si ayuda a conectar la recolección manual con el procesamiento automatizado. No escribas su nombre físico, ruta, SHA, nombre de hoja ni índice de worksheet.

La limitación forense sobre la fuente histórica original puede expresarse de forma natural y breve si es necesaria para la procedencia: el contenido procesado relevante pudo reconstruirse funcionalmente, pero no se afirma identidad binaria con el workbook histórico completo. No uses hashes para explicarla.

### 7.4 Section 4.2.2 — Processing and curation

Describe únicamente operaciones verificadas:

- transformación automatizada desarrollada en Python desde la disposición recolectada hacia una estructura con una fila por SERIE;
- identificación/extracción de campos por SERIE;
- conservación/concatenación de las líneas descriptivas disponibles;
- generación de identificadores reproducibles cuando sea metodológicamente relevante, usando lenguaje científico y no nombres internos de columnas salvo necesidad real;
- limpieza textual que esté demostrada por el parser;
- validación de campos obligatorios, descripción no vacía, NANDINA de ocho dígitos, coherencia jerárquica, pertenencia a Chapter 87 y advertencias críticas de parseo;
- tratamiento de duplicados admisibles y exclusión trazable de grupos conflictivos, conforme al código congelado;
- 11,320 series / 107 DAM en el intermedio reconstruido;
- 4,232 registros Chapter 87 antes de curación;
- 4,106 registros curados para la construcción del benchmark v0.2.

No nombres scripts, rutas, `Hoja2`, fingerprints, SHA o labels internos del pipeline en la prosa publicable.

No traslades automáticamente una formulación prospectiva de SRC-02 si el código/artefactos congelados muestran que la ejecución final fue diferente.

### 7.5 Section 4.2.3 — Partition construction and dataset composition

Explica:

- construcción de tres particiones: historical bank, development set y evaluation set;
- v0.2 se materializó mediante **asignaciones explícitas de DAM**; no describirla como split aleatorio generado por `seed=2026`;
- DAM es la unidad de agrupamiento para construir las particiones;
- cero solapamiento de DAM entre las tres particiones;
- cero solapamiento del identificador de SERIE entre particiones, expresado con un término descriptivo si el nombre interno del campo no es necesario;
- composición final:
  - historical bank: **2,950 series / 28 DAM / 66 represented codes**;
  - development: **100 series / 6 DAM / 9 represented codes**;
  - evaluation: **1,056 series / 67 DAM / 42 represented reference codes**.

No describas 66 como universo completo de Chapter 87. Los 66 son los códigos representados en el banco histórico utilizado.

Presenta estos conteos preferentemente en una **tabla compacta** si mejora la lectura. La tabla debe contener información científica, no filenames/hashes/rutas.

El detalle de leakage, duplicados y near-duplicates se reserva principalmente para 4.4. B01 puede registrar los controles estructurales de separación, pero no anticipar los resultados diagnósticos de 4.4.

## 8. Reglas de prosa KBS para todo el bloque

1. No escribir SHA-256 en la prosa ni en tablas publicables de B01.
2. No escribir rutas internas de repositorio.
3. No escribir nombres físicos de CSV/workbook/scripts/worksheet salvo que exista una necesidad metodológica excepcional demostrada; en este bloque no se presume ninguna.
4. No usar labels de gobernanza o códigos internos (`PIPELINE_PARTIALLY_RECONSTRUCTED`, `T5-safe-159`, etc.) si el mismo hecho puede expresarse científicamente.
5. No convertir trazabilidad técnica en argumento central.
6. No repetir la arquitectura de Section 3.
7. No anticipar resultados de retrieval, explicación, hipótesis, sensibilidad, robustez o inferencia.
8. No afirmar generalización empírica fuera del escenario evaluado.
9. No afirmar legal correctness ni carácter jurídicamente vinculante.
10. Conservar tono de Research Article KBS, no tesis, memoria técnica o documentación de software.

## 9. Claims autorizados/prohibidos

Relevantes y autorizados dentro de sus límites:

- C06: v0.2 evita solapamiento de DAM entre historical/development/evaluation;
- C07: la dependencia intra-DAM debe considerarse cuando la inferencia requiera independencia;
- C15: configurabilidad para otros capítulos/niveles/jurisdicciones, **solo propiedad de diseño**;
- C17: separación conceptual entre reproducción del estudio y replicación externa, preferentemente diferida a 4.8 salvo una frase estrictamente necesaria.

No usar en B01:

- C04/C05 o métricas de retrieval;
- C20;
- C22–C29 y resultados de hipótesis/sensibilidad/inferencia;
- C12/C13 como correctness;
- C16 generalización empírica;
- C18 clasificaciones jurídicamente vinculantes;
- novelty, SOTA, first-of-its-kind, superioridad no gobernada o `FINAL_GAP`.

C19 y C21 se difieren preferentemente a 4.4/Limitations salvo necesidad metodológica directa demostrada.

## 10. Preservación acumulativa

Fuera del alcance autorizado:

- no cambies Introduction;
- no cambies Related Work;
- no cambies 3.1–3.4 ni 3.6;
- en 3.5 y 3.7 cambia solo las dos forward references autorizadas;
- no redactes 4.3 ni posteriores;
- no cambies Section 5+;
- preserva los 40 comentarios heredados;
- no introduzcas tracked changes.

Part I y Part II deben mantener equivalencia semántica; Part II no es una reescritura libre.

## 11. Entregables obligatorios

### 11.1 Section MD pequeño — GitHub

Crear:

`article/sections/experimental_design/Experimental_Design_B01_V02.md`

Debe contener únicamente:

- registro de las dos enmiendas de 3.5/3.7;
- texto final de 4.1, 4.2, 4.2.1, 4.2.2 y 4.2.3 en English y Spanish mirror;
- cualquier tabla compacta aprobada para composición de datasets.

### 11.2 Respuesta de ejecución — GitHub

Crear:

`article/responses/5_EXPERIMENTAL_DESIGN_B01_V02_STRUCTURE_V02_REWRITE_RESPONSE_V01.md`

Debe registrar como mínimo:

```text
BLOCK
STRUCTURE_V02_GIT_BLOB_CHECK
SOURCE_MASTER_V009_GIT_BLOB_CHECK
BASELINE_DOCX_SHA256_CHECK
SRC02_EXACT_FILE_CHECK
SRC03_HEAD_READ
SRC03_BLOB_READ
SRC03_MATERIAL_CHANGE
AUTHORIZED_SCOPE_ONLY
SECTION_3_FORWARD_REFERENCE_AMENDMENT_COUNT
SECTION_4_3_AND_LATER_MODIFIED
SHA_PATH_FILENAME_DISCLOSURE_IN_B01_PROSE
RESULTS_LEAKAGE
NEW_LITERATURE
INHERITED_COMMENT_COUNT
FINAL_COMMENT_COUNT
TRACKED_CHANGES
OOXML_QA
FULL_RENDER_QA
RENDERED_PAGE_COUNT
SECTION_MD_PATH
SECTION_MD_SHA256
SECTION_MD_GIT_BLOB
MASTER_CANDIDATE_MD_FILENAME
MASTER_CANDIDATE_MD_SHA256
CANDIDATE_DOCX_FILENAME
CANDIDATE_DOCX_SHA256
DIRECT_LARGE_MASTER_GITHUB_TRANSFER
MANUAL_BASE64
FRAGMENTATION_OR_CHUNKING
ARTICLE_MASTER_V010
SECTION_4_3
RESULTS
FINAL_GAP
NOVELTY
```

Incluye además una tabla `claim/fact → primary source → scope/strength` para todas las cifras y hechos empíricos usados.

### 11.3 Master acumulativo Markdown — handoff exacto

Genera:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md`

No intentes transferir este master grande directamente a GitHub. Entrégalo como archivo exacto descargable al autor y registra SHA-256 en la respuesta.

### 11.4 DOCX acumulativo — handoff exacto

Edita exclusivamente el DOCX baseline exacto y entrega:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx`

Preserva los 40 comentarios heredados. No reconstruyas el DOCX desde Markdown. No tracked changes. Registra SHA-256 y entrégalo al autor como archivo descargable exacto.

## 12. QA obligatorio

Antes de cerrar:

1. compara el Markdown candidato contra V009 y demuestra que solo cambiaron las dos referencias autorizadas de Section 3 y el bloque 4.1–4.2.3;
2. confirma que no apareció texto nuevo en 4.3+;
3. busca expresamente `SHA-256`, `data/`, `.csv`, `.xlsx`, `.py`, `Hoja`, `T5-safe-159`, `PIPELINE_PARTIALLY_RECONSTRUCTED` dentro de la nueva prosa B01; cualquier aparición debe justificarse como indispensable o eliminarse;
4. valida equivalencia English/Spanish;
5. valida OOXML;
6. confirma comments starts/ends/refs y total 40;
7. confirma tracked changes = 0;
8. renderiza el DOCX completo e inspecciona visualmente todas las páginas para clipping, overlap, truncation, glyph loss, table overflow y pérdida de contenido.

## 13. Handoff timeout-safe

Aplica D-035 estrictamente:

- section MD pequeño y response pequeña → GitHub;
- masters grandes MD/DOCX → archivos exactos adjuntos al autor + SHA-256;
- no Base64 manual;
- no fragmentación/chunking/recomposición;
- no archivos auxiliares ni múltiples commits como workaround;
- no reintentar una vía grande ya conocida como problemática.

## 14. Estados que no puedes conceder

No declarar:

- `APPROVED`;
- `FROZEN`;
- `INTEGRATED`;
- `ARTICLE_MASTER_V010 = PROMOTED`;
- `SECTION_4_3 = AUTHORIZED`;
- `RESULTS = AUTHORIZED`;
- `FINAL_GAP` definido;
- novelty declarada.

Tu estado terminal máximo es:

`EXPERIMENTAL_DESIGN_B01_V02_REWRITE = DELIVERED_FOR_GESTORA_AUDIT`

## 15. Respuesta terminal en chat

Conforme a D-022, no repitas el informe sustantivo en chat. Devuelve únicamente el puntero:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/5_EXPERIMENTAL_DESIGN_B01_V02_STRUCTURE_V02_REWRITE_RESPONSE_V01.md@<commit>`

y adjunta los dos archivos acumulativos exactos MD/DOCX. No avances a 4.3.