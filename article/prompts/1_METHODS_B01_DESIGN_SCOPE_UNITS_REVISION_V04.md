# Fase 1 — Methods B01 — Revisión V04 / Closed Delivery-Repair Prompt

## Español

### Instrucción operativa

Actúa exclusivamente como **IA de Redacción** del artículo científico en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Ejecuta exclusivamente la corrección de entrega **B01-M09** sobre `Methods B01`. **No avances a B02 ni a ninguna otra sección.**

Lee íntegramente, además del onboarding y `MWDP_V1.0` obligatorios:

- `article/ARTICLE_STATUS.md`;
- `article/STYLE_GUIDE.md`;
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
- `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V03.md`;
- `article/sections/methods/Methods_B01_V03.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.md`;
- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V03.md`;
- este prompt.

### Naturaleza de V04

V03 superó la revisión interna de **contenido científico**. B01-M06, B01-M07 y B01-M08 están cerradas. La única corrección pendiente es de **integridad del Word candidato**.

El `.docx` V03 versionado en GitHub no es un paquete OOXML válido:

```text
DOCX_BLOB_SHA = 5dec60d1ebeff158c114aaed84c992953d256175
DOCX_SIZE_BYTES = 15007
OOXML_ZIP_INTEGRITY = FAIL
END_OF_CENTRAL_DIRECTORY = MISSING
LIBREOFFICE_RENDER = FAIL
```

Por tanto, **no reescribas el contenido científico de V03** para “mejorarlo”. V04 es una corrección de entrega y versionado.

### B01-M09 — Regenerar un DOCX válido sin cambiar el contenido científico

Genera una nueva revisión V04 preservando sin cambios sustantivos el texto científico V03 en inglés y español.

Requisitos obligatorios:

1. `Methods_B01_V04.md` debe reproducir el contenido científico de V03; solo pueden cambiar los identificadores/versiones necesarios para declarar V04.
2. `ARTICLE_MASTER_CANDIDATE_V04.md` debe reproducir exactamente el mismo contenido científico del bloque V04, con la estructura de master candidato.
3. `ARTICLE_MASTER_CANDIDATE_V04.docx` debe ser un archivo DOCX/OOXML válido y abrirse como ZIP OPC.
4. El Word debe conservar:
   - `Part I — English manuscript master`;
   - `Part II — Spanish semantic-control mirror`;
   - layout neutral/reversible y editable;
   - cero citas y cero comentarios de cita;
   - ausencia de Mendeley y de campos bibliográficos simulados;
   - ausencia de tracked changes.
5. Antes del commit debes ejecutar QA técnico real sobre el archivo final:
   - abrir el `.docx` como ZIP/OOXML y verificar integridad completa;
   - comprobar que existe `word/document.xml`;
   - verificar que no existen comentarios ni tracked changes;
   - abrir/renderizar el archivo con un motor DOCX disponible y comprobar que todas las páginas se generan sin error;
   - comparar el texto visible del Word con `ARTICLE_MASTER_CANDIDATE_V04.md`.
6. No sobrescribas ni elimines V01, V02 o V03.
7. No crees `ARTICLE_MASTER_V001.*`.
8. No modifiques `ARTICLE_STATUS.md`, reviews, `DECISIONS.md`, `CLAIM_EVIDENCE_MATRIX.md`, `STYLE_GUIDE.md`, gobernanza, literatura congelada ni Plan Maestro.

### Contenido y claims que deben permanecer exactamente delimitados

Mantener:

```text
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
CITATION_COMMENT_COVERAGE = 0/0
GROUP3 = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

C15 permanece únicamente como propiedad acotada de configurabilidad/replicabilidad de diseño. No introducir ningún claim adicional.

No introducir resultados, cifras, métricas concretas, inferencia estadística, causalidad, novelty final, superioridad, literatura externa, EXP-11B, resultados de Grupo 3, detalles del repositorio de reproducibilidad ni contenido técnico de B02–B09.

### Artefactos V04

Genera exclusivamente:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V04.md`;
2. `article/sections/methods/Methods_B01_V04.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V04.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V04.docx`.

### Checklist obligatorio

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V04
REVISION_NATURE = DELIVERY_REPAIR_ONLY
B01_M09 = ADDRESSED
B01_M06_M07_M08 = PRESERVED_CLOSED
B01_M01_M02_M03_M05 = PRESERVED_CLOSED
SCIENTIFIC_CONTENT_CHANGE_FROM_V03 = NONE
SOURCE_SNAPSHOT(S) = [SHAs realmente leídos]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS
POSITIONING_ORDER = GENERAL_METHOD_AND_FUNCTIONAL_CONTRACT_FIRST / CONFIGURABILITY_BOUNDARY_SECOND / NANDINA_CH87_TESTBED_THIRD
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
DOCX_ZIP_INTEGRITY = PASS
DOCX_DOCUMENT_XML = PRESENT
DOCX_COMMENTS = 0
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS
MD_DOCX_VISIBLE_TEXT_EQUIVALENCE = PASS
DOCX_SHA256 = ...
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V04.md + .docx
ENGLISH_MAIN_TEXT_WORD_COUNT = 353
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW
```

No declares B01 `APPROVED` ni `FROZEN`.

---

## English

Perform only the `B01-M09` delivery repair. V03 scientific content already passed internal review; do not substantively rewrite it. Create the four V04 artifacts listed above, preserving the V03 English/Spanish scientific text and claim boundaries.

The V03 DOCX blob is invalid OOXML because its ZIP package lacks a valid end-of-central-directory structure and cannot be opened/rendered. V04 must provide a genuinely valid, editable, bilingual DOCX. Before committing, perform actual ZIP/OOXML integrity checks, verify `word/document.xml`, confirm zero comments and zero tracked changes, render the final DOCX successfully, and compare its visible text with the V04 Markdown master.

Do not advance to B02, do not add scientific content, and do not overwrite V01–V03.