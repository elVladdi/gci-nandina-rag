# Prompt — Related Work B03 — Section 2.3 LLMs for classification, reasoning, and explanation

## Rol

Actúa exclusivamente como **IA de Redacción** del artículo científico de `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

No eres IA Gestora ni IA Experimental. No modifiques gobernanza, decisiones, literatura congelada, Claim–Evidence Matrix, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` ni Plan Maestro experimental.

## Alcance autorizado

```text
BLOCK = RELATED_WORK_B03
BLOCK_REVISION = V01
SECTION = 2.3 LLMs for classification, reasoning, and explanation
AUTHORIZED = YES
SECTIONS_2_1_AND_2_2 = APPROVED / FROZEN / PRESERVE_EXACTLY
PRIOR_CITATION_COMMENTS = 14 / PRESERVE_EXACTLY
SECTIONS_2_4_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
METHODS_B01_V06 = NOT_AUTHORIZED
```

Redacta exclusivamente la subsección 2.3 en inglés y su espejo semántico en español dentro del master acumulativo. No alteres 2.1, 2.2 ni sus comentarios.

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
11. `article/manuscript/ARTICLE_MASTER_V002.md`;
12. `article/CLAIM_EVIDENCE_MATRIX.md`;
13. `article/BIBLIOGRAPHIC_FRAMEWORK.md` y el manifiesto de acceso full-text gobernante.

## Baseline acumulativo obligatorio

Debes trabajar sobre:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V002.md
BASELINE_DOCX = article/manuscript/ARTICLE_MASTER_V002.docx
BASELINE_DOCX_SHA256 = ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e
PRIOR_APPROVED_SECTIONS = 2.1 + 2.2
PRIOR_CITATION_COMMENTS = 14
STATUS = AUTHOR_APPROVED / CANONICAL
```

Localiza el DOCX exacto y verifica SHA-256 antes de editar. Si no puedes acceder al binario exacto o el hash no coincide, declara:

```text
BASELINE_DOCX_ACCESS_REQUIRED = YES
```

y detente. No reconstruyas el Word desde cero, no uses `ARTICLE_MASTER_V001` ni el antiguo Word estructural como baseline.

## Fuentes científicas prioritarias para 2.3

Usa las matrices congeladas únicamente como mapa de selección; **no cites por memoria**. Prioriza:

- `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`;
- `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`;
- `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`;
- `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`, solo para contrastes próximos entre decisión, explicación y evidencia;
- `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`, únicamente para continuidad y evitando repetir 2.1.

Para **cada cita** incluida debes re-recuperar el full text original, verificar identidad y versión, localizar el pasaje exacto y comprobar el alcance del claim conforme a MWDP-S01–S04.

Los 34 artículos KBS usados para estilo editorial no son automáticamente evidencia científica.

## Función narrativa de 2.3

La subsección debe explicar que la etiqueta **LLM** agrupa sistemas con responsabilidades operativas distintas. El criterio de comparación principal no será si un trabajo “usa un LLM”, sino **qué autoridad tiene el modelo sobre la decisión, los candidatos, la búsqueda y la salida final**.

La subsección debe permitir que el lector diferencie, cuando las fuentes disponibles lo soporten:

1. **direct generative classification**: el LLM recibe la descripción/contexto y produce o selecciona el código como salida de clasificación;
2. **fine-tuned transformer classification**: encoders/transformers ajustados con classification head y label space cerrado; no deben equipararse automáticamente a generación libre de códigos;
3. **RAG classification / decision-making**: el LLM o generador usa documentos recuperados para decidir el código;
4. **agentic/search-control roles**: el LLM controla next-hop, reranking, selección, consenso, aplicación de reglas o trayectoria de búsqueda y por ello participa en la decisión;
5. **reader/reasoner roles**: el LLM interpreta contexto recuperado para producir una respuesta o decisión downstream;
6. **rationale/explanation generation**: el modelo genera una explicación, rationale o reporte después de una decisión o ruta previa; debe distinguirse si esa decisión fue fijada independientemente o si el mismo modelo participó antes en ella.

La posición causal/funcional del LLM dentro del pipeline debe quedar más visible que su nombre comercial o tamaño.

## Puntos de contraste científicos obligatorios

Cuando la evidencia lo permita, conserva estas distinciones:

- `DIRECT_GENERATIVE_LLM_CLASSIFICATION ≠ FINE_TUNED_TRANSFORMER_CLASSIFIER`;
- `RAG_CLASSIFICATION ≠ RAG_EVIDENCE_SUPPORT ≠ DOCUMENT_QA_RAG`;
- `SEARCH_CONTROL / RERANKING / NEXT_HOP_DECISION ≠ EXPLANATION_ONLY_GENERATION`;
- `CONSENSUS / SELF_CONSISTENCY ≠ INDEPENDENT_GROUND_TRUTH`;
- `RATIONALE / CHAIN_OF_THOUGHT / REASONING_TRACE ≠ FAITHFULNESS GUARANTEE`;
- `VISIBLE_CITATION / PROVENANCE ≠ FORMAL_AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- un componente que genera rationale **después** de una ruta fijada no debe equipararse automáticamente a un explainer que recibe candidatos fijados externamente por un componente independiente;
- que un paper denomine “LLM” a un transformer fine-tuned no autoriza describirlo como modelo generativo si operacionalmente no lo es.

## Literatura/familias que pueden resultar especialmente pertinentes

Sin convertir esta lista en obligación de citar todos los trabajos, considera los precedentes congelados:

- clasificación HS generativa directa con GPT/LLM;
- clasificadores transformer fine-tuned descritos por sus autores como LLM pero operativamente cerrados;
- THE-RAG y otros sistemas RAG donde la evidencia participa en la **decisión del código**;
- workflows agentic/determinísticos donde LLM, reglas, retrieval, consensus o graph constraints controlan la trayectoria de clasificación;
- `Constraint-Aware Hierarchical Search`, donde la ruta se fija mediante búsqueda/decisión regulatoria y luego existe una fase final de evidence aggregation/rationale;
- sistemas en los que rationale/citations acompañan la clasificación sin demostrar por ello auditabilidad formal;
- RAG/reader architectures generales solo cuando sean necesarias para distinguir reader/reasoner de classifier/explainer.

No cites una fuente solo porque aparece en la matriz: cada uso debe justificarse por la función narrativa de 2.3 y por evidencia primaria re-verificada.

## Organización retórica esperada

No redactes autor por autor ni paper por paper. Una secuencia adecuada es:

`“LLM” como etiqueta heterogénea → clasificación generativa directa vs transformer classifier → LLM/RAG que participa en decisión → LLM/agente como controlador de búsqueda/reglas/consenso → reader/reasoner condicionado por retrieval → rationale/explanation después de decisión/ruta → síntesis por grado de autoridad del modelo → transición a 2.4 grounding/explainability/auditability`.

El cierre debe preparar naturalmente **2.4 Evidence grounding, explainability, and auditability** sin empezar a redactarla.

## Restricciones científicas y editoriales

- No declares `FINAL_GAP`; continúa `NOT_DEFINED`.
- No declares novelty universal.
- No uses `first`, `no prior work`, `unique`, `novel` o equivalentes como claim propio del artículo actual.
- `RAG + LLM + HS` no es novedoso por sí mismo.
- No afirmes que el rol explanation-only del proyecto actual es novedoso; su eventual contribución/novelty permanece fuera de este bloque.
- No describas la arquitectura actual, Top-3 fijo, ranking histórico inmutable, NANDINA, Chapter 87, H100, DAM, corpus peruano ni resultados propios.
- No conviertas diferencias arquitectónicas en novelty.
- No presentes CoT/rationale/reasoning trace como explicación fiel por defecto.
- No presentes consensus/self-consistency/majority vote como ground truth independiente.
- No presentes visible evidence, source links, path validity o metadata como prueba de auditabilidad formal o corrección jurídica.
- No homogeneices accuracy, F1, Top-k, MRR, agreement, faithfulness, confidence o human ratings.
- No promuevas claims secundarios de WCO, autoridades, prensa u otras fuentes heredadas por los papers sin abrir la fuente primaria correspondiente.
- Si una fuente es preprint, identifica su estado correctamente y no inventes venue/DOI final.
- Evita tono de tesis, especificación contractual o documento de gobernanza.
- Sigue KBS-34: síntesis funcional, oraciones concretas, agente–acción–objeto visible y transiciones fluidas.

## Extensión y forma

Objetivo orientativo para la parte inglesa de 2.3: **aprox. 650–850 palabras**, salvo que la evidencia rigurosamente necesaria justifique otra extensión.

No uses listas de viñetas dentro de la subsección del manuscrito salvo necesidad científica clara. Debe leerse como prosa continua de research article.

Evita repetir explicaciones ya cerradas en 2.1 y 2.2. La subsección debe avanzar desde **qué función cumple el conocimiento** hacia **qué función cumple el LLM**.

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

No modifiques los 14 comentarios ya existentes. Los nuevos IDs/comentarios deben añadirse preservando íntegramente los anteriores.

La Parte II no requiere duplicar comentarios, pero debe ser semánticamente equivalente a la inglesa.

No elimines notas editoriales de otras secciones. En 2.3 sustituye únicamente la nota/placeholder correspondiente.

## Entregables obligatorios

Genera y versiona exclusivamente:

1. `article/sections/related_work/RelatedWork_B03_V01.md` — texto bilingüe del bloque;
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B03_V01.md` — master acumulativo completo con 2.3 insertada;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B03_V01.docx` — Word acumulativo derivado del baseline V002 exacto, no reconstruido;
4. `article/responses/2_RELATED_WORK_B03_RESPONSE_V01.md` — informe de ejecución.

No modifiques ningún otro archivo.

## QA obligatorio antes de commit

Verifica:

- baseline DOCX SHA-256 correcto antes de editar;
- preservación exacta de 2.1 y 2.2;
- preservación exacta de los 14 comentarios previos;
- integridad OOXML del Word final;
- render del DOCX completo;
- equivalencia Markdown–DOCX para 2.3;
- equivalencia EN–ES;
- ninguna modificación accidental de otras secciones;
- cobertura de nuevos comentarios de cita `n/n`;
- todos los full texts usados recuperados y verificados;
- cada pasaje del comentario existe realmente en la fuente citada y soporta el claim anclado;
- ninguna referencia inventada;
- ninguna fuente KBS-34 editorial usada como evidencia científica sin admisión bibliográfica;
- ausencia de claims de novelty/gap no autorizados;
- prosa fluida y no abstracta según KBS_EWG_34_V01 y SPCCR;
- cero tracked changes residuales;
- ausencia de comentarios ajenos a los comentarios de auditoría de citas.

## Informe de entrega obligatorio

`article/responses/2_RELATED_WORK_B03_RESPONSE_V01.md` debe declarar como mínimo:

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
PLAN_VERSION = V2.2
BLOCK = RELATED_WORK_B03
BLOCK_REVISION = V01
SECTION = 2.3
BASELINE_MASTER = ARTICLE_MASTER_V002
BASELINE_DOCX_SHA256_EXPECTED = ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e
BASELINE_DOCX_SHA256_VERIFIED = ...
SOURCE_SNAPSHOT(S) = ...
FULLTEXTS_RETRIEVED = [lista]
AUTHORIZED_CLAIMS_USED = ...
CONDITIONAL_CLAIMS_USED = ...
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [lista]
PRIOR_2_1_TEXT_PRESERVED = PASS / ISSUE
PRIOR_2_2_TEXT_PRESERVED = PASS / ISSUE
PRIOR_CITATION_COMMENTS_PRESERVED = 14/14 / ISSUE
NEW_CITATION_COMMENT_COVERAGE = n/n
TOTAL_CITATION_COMMENT_COUNT = ...
EN_ES_SEMANTIC_EQUIVALENCE = PASS / ISSUE
KBS_PROSE_QA = PASS / ISSUE
ABSTRACTION_DENSITY = ACCEPTABLE / ISSUE
AGENT_ACTION_OBJECT_CLARITY = PASS / ISSUE
NOMINALIZATION_OVERLOAD = ABSENT / ISSUE
PROCESS_RELATIONSHIPS_EXPLICIT = PASS / ISSUE
MASTER_CANDIDATE_MD = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B03_V01.md
MASTER_CANDIDATE_DOCX = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B03_V01.docx
DOCX_OOXML_INTEGRITY = PASS / FAIL
DOCX_TRACKED_CHANGES = 0 / ...
DOCX_RENDER = PASS / FAIL
MD_DOCX_EQUIVALENCE = PASS / ISSUE
ENGLISH_SECTION_2_3_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```

## Stop rule

Tras generar los cuatro entregables y hacer un único commit semántico, **detente**.

No avances a 2.4, no redactes Introduction, no corrijas Methods B01, no modifiques gobernanza y no integres el candidato como master canónico. La IA Gestora realizará la revisión interna claim por claim contra las fuentes primarias y el autor decidirá la aprobación.