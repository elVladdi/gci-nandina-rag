# Prompt — Related Work B04 — Section 2.4 Evidence grounding, explainability, and auditability

## Rol

Actúa exclusivamente como **IA de Redacción** del artículo científico de `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

No eres IA Gestora ni IA Experimental. No modifiques gobernanza, decisiones, literatura congelada, Claim–Evidence Matrix, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` ni Plan Maestro experimental.

## Alcance autorizado

```text
BLOCK = RELATED_WORK_B04
BLOCK_REVISION = V01
SECTION = 2.4 Evidence grounding, explainability, and auditability
AUTHORIZED = YES
SECTIONS_2_1_TO_2_3 = APPROVED / FROZEN / PRESERVE_EXACTLY
PRIOR_CITATION_COMMENTS = 19 / PRESERVE_EXACTLY
SECTIONS_2_5_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
METHODS_B01_V06 = NOT_AUTHORIZED
```

Redacta exclusivamente la subsección 2.4 en inglés y su espejo semántico en español dentro del master acumulativo. No alteres 2.1–2.3 ni sus comentarios.

## Onboarding obligatorio

Antes de redactar, lee íntegramente y aplica:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md` — V2.2 vigente;
4. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — `MWDP_V1.0 / FROZEN`;
5. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
6. `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md`, aprobado/activo por D-013;
7. `article/governance/D014_ARTICLE_STRUCTURE_AND_DRAFTING_ORDER_RESET.md`;
8. `article/governance/D015_KBS_ARTICLE_STRUCTURE_APPROVAL_AND_RELATED_WORK_START.md`;
9. `article/governance/D016_RELATED_WORK_B01_APPROVAL_INTEGRATION_AND_B02_START.md`;
10. `article/governance/D017_RELATED_WORK_B02_APPROVAL_INTEGRATION_AND_B03_START.md`;
11. `article/governance/D018_RELATED_WORK_B03_APPROVAL_INTEGRATION_AND_B04_START.md`;
12. `article/manuscript/ARTICLE_MASTER_V003.md`;
13. `article/CLAIM_EVIDENCE_MATRIX.md`;
14. `article/BIBLIOGRAPHIC_FRAMEWORK.md` y el manifiesto de acceso full-text gobernante.

## Baseline acumulativo obligatorio

Debes trabajar sobre:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V003.md
BASELINE_DOCX = article/manuscript/ARTICLE_MASTER_V003.docx
BASELINE_DOCX_SHA256 = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
PRIOR_APPROVED_SECTIONS = 2.1 + 2.2 + 2.3
PRIOR_CITATION_COMMENTS = 19
STATUS = AUTHOR_APPROVED / CANONICAL
```

Localiza el DOCX exacto y verifica SHA-256 antes de editar. Si no puedes acceder al binario exacto o el hash no coincide, declara:

```text
BASELINE_DOCX_ACCESS_REQUIRED = YES
```

y detente. No reconstruyas el Word desde cero ni uses una versión canónica anterior como baseline.

## Fuentes científicas prioritarias para 2.4

Usa las matrices congeladas únicamente como mapa de selección; **no cites por memoria**. Prioriza:

- `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`;
- `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`, especialmente para el contraste entre provenance/faithfulness y auditabilidad formal;
- `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`;
- `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`, solo para provenance, traceability, transparency trail y límites entre lifecycle audit y output-level auditability;
- `article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_FROZEN.md`, solo cuando sea necesario delimitar autoridad, actualidad y trazabilidad de fuentes oficiales frente a corrección jurídica.

Puedes recurrir a otras fuentes ya admitidas en la literatura congelada si son estrictamente necesarias para explicar un concepto de 2.4 y si el uso respeta su función bibliográfica aprobada.

Para **cada cita** incluida debes re-recuperar el full text original, verificar identidad y versión, localizar el pasaje exacto y comprobar el alcance del claim conforme a MWDP-S01–S04. Las matrices congeladas orientan la selección, pero no sustituyen la lectura de la fuente primaria.

Los 34 artículos KBS usados para estilo editorial no son automáticamente evidencia científica.

## Función narrativa de 2.4

La subsección debe explicar que exponer documentos, citas, rationales o trazas no convierte automáticamente una salida en una decisión auditada. El eje de comparación será **qué relación puede reconstruirse y verificarse entre la salida, la evidencia documental y el proceso que la produjo**.

La síntesis debe permitir al lector distinguir, cuando las fuentes disponibles lo soporten:

1. **evidence grounding / source support**: la salida o claim se vincula con material recuperado que puede inspeccionarse; debe diferenciarse presencia de contexto de soporte semántico real;
2. **explainability / rationale**: el sistema presenta razones, features, pasajes o una narrativa explicativa; plausibilidad o legibilidad no equivalen automáticamente a faithfulness;
3. **provenance / traceability**: se registra de dónde provienen datos, documentos, versiones, operaciones o outputs y cómo se relacionan;
4. **audit trail / lifecycle auditability**: se preservan artefactos y decisiones del proceso para revisión posterior;
5. **output-level auditability**: una salida concreta puede revisarse contra criterios y evidencia explícitos; no asumir que todo mecanismo de provenance o lifecycle audit satisface esta propiedad;
6. **source authority and currency**: una fuente puede ser oficial, versionada y temporalmente trazable sin que ello pruebe que el sistema interpretó correctamente la norma;
7. **substantive/legal correctness**: requiere evidencia propia y no debe inferirse de citation presence, faithfulness, provenance, official-source retrieval o auditability por sí solos.

## Distinciones científicas obligatorias

Conserva explícitamente, donde resulte natural:

- `RETRIEVED_CONTEXT ≠ CLAIM_SUPPORT`;
- `VISIBLE_CITATION / EVIDENCE ≠ FORMAL_AUDITABILITY`;
- `RATIONALE / REASONING_TRACE ≠ FAITHFULNESS GUARANTEE`;
- `PROVENANCE / LINEAGE ≠ SUBSTANTIVE_CORRECTNESS`;
- `TRACEABILITY ≠ REPRODUCIBILITY`;
- `LIFECYCLE_AUDIT ≠ OUTPUT_LEVEL_AUDITABILITY`;
- `OFFICIAL_SOURCE / SOURCE_AUTHORITY ≠ CORRECT_LEGAL_INTERPRETATION`;
- `DOCUMENT_CURRENCY ≠ LEGAL_VALIDITY_OF_THE_MODEL_OUTPUT`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.

No presentes estas fronteras como una escalera de madurez ni como una secuencia causal en la que una propiedad garantice la siguiente.

## Literatura/familias especialmente pertinentes

Sin convertir esta lista en obligación de citar todos los trabajos, considera:

- sistemas RAG/QA que reportan faithfulness, answer correctness, relevance, provenance o document/section backtracking;
- trabajos de retrieval/generation que vinculan respuestas con documentos recuperados;
- trabajos de provenance/lineage que permiten reconstruir inputs, outputs, software/configuración o versiones;
- frameworks de internal algorithmic auditing y transparency trails;
- trabajos aduaneros o regulatorios que muestran evidence/rationale/citations junto con la decisión, siempre preservando el límite entre inspectabilidad y corrección jurídica;
- fuentes oficiales únicamente cuando el claim sea sobre autoridad documental, vigencia/currency, trazabilidad o carácter vinculante delimitado de determinados instrumentos, no como sustituto de literatura científica sobre explainability.

No cites una fuente solo porque aparece en una matriz. Cada uso debe tener una función narrativa clara en 2.4 y evidencia primaria exacta.

## Organización retórica esperada

No redactes autor por autor ni paper por paper. Una secuencia adecuada es:

`evidencia visible y grounding → explicación/rationale y problema de faithfulness → provenance/traceability → audit trail y lifecycle auditability → output-level auditability → autoridad/currency de la evidencia documental → frontera con substantive/legal correctness → síntesis y transición a 2.5 reproducibility/evaluation`.

El cierre debe preparar naturalmente **2.5 Reproducibility and evaluation in knowledge-based decision support** sin empezar a desarrollarla.

## Frontera con 2.5

B04 puede utilizar provenance, documentation y audit-trail literature para definir auditabilidad y trazabilidad, pero debe evitar absorber la función de 2.5.

Reserva para 2.5, salvo una mención de transición estrictamente necesaria:

- documentación sistemática de datasets;
- identity/versioning como práctica de reproducibilidad;
- taxonomías de reproducibility/replication/robustness/generalization;
- code/data availability como práctica de reproducibilidad;
- diseño de evaluación experimental y reporting;
- dependencia, splits y leakage;
- reproducibility packages o repositorios del presente estudio.

## Restricciones científicas y editoriales

- No declares `FINAL_GAP`; continúa `NOT_DEFINED`.
- No declares novelty universal.
- No uses `first`, `no prior work`, `unique`, `novel` o equivalentes como claim propio del artículo actual.
- No describas todavía la arquitectura actual, Top-3 fijo, ranking histórico inmutable, NANDINA, Chapter 87, H100, DAM, corpus peruano, HE4 ni resultados propios.
- No conviertas diferencias arquitectónicas o de auditoría en novelty.
- No afirmes que retrieval garantiza grounding.
- No afirmes que una cita visible demuestra soporte semántico del claim.
- No afirmes que rationale, CoT, reasoning trace, path validity o confidence son explicaciones fieles por defecto.
- No afirmes que provenance o lineage demuestran correctness.
- No afirmes que transparency trail o internal audit equivalen a auditoría externa, output-level auditability o legal compliance.
- No afirmes que el uso de fuentes oficiales prueba la corrección jurídica de una clasificación.
- No mezcles métricas de faithfulness, relevance, answer correctness, retrieval quality, auditability o classification accuracy como si midieran la misma propiedad.
- No promuevas claims secundarios heredados por papers sin abrir la fuente primaria correspondiente.
- Si una fuente es preprint, conserva su estado correctamente.
- Evita tono de tesis, especificación contractual o documento de gobernanza.
- Sigue KBS-34 y SPCCR: síntesis funcional, oraciones concretas, agente–acción–objeto visible, relaciones explícitas y transiciones fluidas.

## Extensión y forma

Objetivo orientativo para la parte inglesa de 2.4: **aprox. 650–850 palabras**, salvo que la evidencia rigurosamente necesaria justifique otra extensión.

No uses listas de viñetas dentro de la subsección del manuscrito salvo necesidad científica clara. Debe leerse como prosa continua de research article.

Evita repetir 2.2 y 2.3. B04 debe avanzar desde **qué función cumple el conocimiento y qué autoridad tiene el LLM** hacia **qué puede realmente verificarse sobre el soporte y la inspectabilidad de una salida**.

## Word y comentarios de citas

En la Parte I inglesa, **cada instancia de cita** debe tener un comentario Word anclado exactamente a la cita con:

```text
Fuente / revista:
Autor(es):
Texto original exacto de respaldo:
Traducción al español:
Justificación semántica claim–fuente:
Límite de alcance, si corresponde:
```

No modifiques los 19 comentarios ya existentes. Los nuevos IDs/comentarios deben añadirse preservando íntegramente los anteriores.

La Parte II no requiere duplicar comentarios, pero debe ser semánticamente equivalente a la inglesa.

No elimines notas editoriales de otras secciones. En 2.4 sustituye únicamente la nota/placeholder correspondiente.

## Entregables obligatorios

Genera y versiona exclusivamente:

1. `article/sections/related_work/RelatedWork_B04_V01.md` — texto bilingüe del bloque;
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V01.md` — master acumulativo completo con 2.4 insertada;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V01.docx` — Word acumulativo derivado del baseline V003 exacto, no reconstruido;
4. `article/responses/2_RELATED_WORK_B04_RESPONSE_V01.md` — informe de ejecución.

No modifiques ningún otro archivo.

## QA obligatorio antes de commit

Verifica:

- baseline DOCX SHA-256 correcto antes de editar;
- preservación exacta de 2.1–2.3;
- preservación exacta de los 19 comentarios previos;
- integridad OOXML del Word final;
- render del DOCX completo;
- equivalencia Markdown–DOCX para 2.4;
- equivalencia EN–ES;
- ninguna modificación accidental de otras secciones;
- cobertura de nuevos comentarios de cita `n/n`;
- todos los full texts usados recuperados y verificados;
- cada pasaje del comentario existe realmente en la fuente citada y soporta el claim anclado;
- ninguna referencia inventada;
- ninguna fuente KBS-34 editorial usada como evidencia científica sin admisión bibliográfica;
- ausencia de claims de novelty/gap no autorizados;
- frontera B04/B05 respetada;
- prosa fluida y no abstracta según KBS_EWG_34_V01 y SPCCR;
- cero tracked changes residuales;
- ausencia de comentarios ajenos a los comentarios de auditoría de citas.

## Informe de entrega obligatorio

`article/responses/2_RELATED_WORK_B04_RESPONSE_V01.md` debe declarar como mínimo:

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
PLAN_VERSION = V2.2
BLOCK = RELATED_WORK_B04
BLOCK_REVISION = V01
SECTION = 2.4
BASELINE_MASTER = ARTICLE_MASTER_V003
BASELINE_DOCX_SHA256_EXPECTED = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
BASELINE_DOCX_SHA256_VERIFIED = ...
SOURCE_SNAPSHOT(S) = ...
FULLTEXTS_RETRIEVED = [lista]
AUTHORIZED_CLAIMS_USED = ...
CONDITIONAL_CLAIMS_USED = ...
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [lista]
PRIOR_2_1_TEXT_PRESERVED = PASS / ISSUE
PRIOR_2_2_TEXT_PRESERVED = PASS / ISSUE
PRIOR_2_3_TEXT_PRESERVED = PASS / ISSUE
PRIOR_CITATION_COMMENTS_PRESERVED = 19/19 / ISSUE
NEW_CITATION_COMMENT_COVERAGE = n/n
TOTAL_CITATION_COMMENT_COUNT = ...
EN_ES_SEMANTIC_EQUIVALENCE = PASS / ISSUE
KBS_PROSE_QA = PASS / ISSUE
ABSTRACTION_DENSITY = ACCEPTABLE / ISSUE
AGENT_ACTION_OBJECT_CLARITY = PASS / ISSUE
NOMINALIZATION_OVERLOAD = ABSENT / ISSUE
PROCESS_RELATIONSHIPS_EXPLICIT = PASS / ISSUE
B04_B05_BOUNDARY = PASS / ISSUE
MASTER_CANDIDATE_MD = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V01.md
MASTER_CANDIDATE_DOCX = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B04_V01.docx
DOCX_OOXML_INTEGRITY = PASS / FAIL
DOCX_TRACKED_CHANGES = 0 / ...
DOCX_RENDER = PASS / FAIL
MD_DOCX_EQUIVALENCE = PASS / ISSUE
ENGLISH_SECTION_2_4_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```

## Stop rule

Tras generar los cuatro entregables y hacer un único commit semántico, **detente**.

No avances a 2.5, no redactes Introduction, no redactes la arquitectura, no corrijas Methods B01, no modifiques gobernanza y no integres el candidato como master canónico. La IA Gestora realizará la revisión interna claim por claim contra las fuentes primarias y el autor decidirá la aprobación del bloque.