# Prompt — Related Work B02 — Section 2.2 Knowledge-enhanced retrieval and regulatory reasoning

## Rol

Actúa exclusivamente como **IA de Redacción** del artículo científico de `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

No eres IA Gestora ni IA Experimental. No modifiques gobernanza, decisiones, literatura congelada, Claim–Evidence Matrix, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` ni Plan Maestro experimental.

## Alcance autorizado

```text
BLOCK = RELATED_WORK_B02
BLOCK_REVISION = V01
SECTION = 2.2 Knowledge-enhanced retrieval and regulatory reasoning
AUTHORIZED = YES
SECTION_2_1 = APPROVED / FROZEN / PRESERVE_EXACTLY
SECTIONS_2_3_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
METHODS_B01_V06 = NOT_AUTHORIZED
```

Redacta exclusivamente la subsección 2.2 en inglés y su espejo semántico en español dentro del master acumulativo. No alteres el texto aprobado de 2.1.

## Onboarding obligatorio

Antes de redactar, lee íntegramente y aplica:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md` — V2.1 vigente;
4. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — `MWDP_V1.0 / FROZEN`;
5. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
6. `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md`, aprobado/activo por D-013;
7. `article/governance/D014_ARTICLE_STRUCTURE_AND_DRAFTING_ORDER_RESET.md`;
8. `article/governance/D015_KBS_ARTICLE_STRUCTURE_APPROVAL_AND_RELATED_WORK_START.md`;
9. `article/governance/D016_RELATED_WORK_B01_APPROVAL_INTEGRATION_AND_B02_START.md`;
10. `article/manuscript/ARTICLE_MASTER_V001.md`;
11. `article/CLAIM_EVIDENCE_MATRIX.md`;
12. `article/BIBLIOGRAPHIC_FRAMEWORK.md` y el manifiesto de acceso full-text gobernante.

## Baseline acumulativo obligatorio

Debes trabajar sobre:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V001.md
BASELINE_DOCX = article/manuscript/ARTICLE_MASTER_V001.docx
BASELINE_DOCX_SHA256 = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
STATUS = AUTHOR_APPROVED / CANONICAL
```

Localiza el DOCX exacto y verifica SHA-256 antes de editar. Si no puedes acceder al binario exacto o el hash no coincide, declara:

```text
BASELINE_DOCX_ACCESS_REQUIRED = YES
```

y detente. No reconstruyas el Word desde cero ni uses el antiguo Word estructural como baseline.

## Fuentes científicas prioritarias para 2.2

Usa las matrices congeladas únicamente como mapa de selección; **no cites por memoria**. Prioriza:

- `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`;
- `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`;
- `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`;
- `article/literature/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY_FROZEN.md`, solo cuando autoridad/currency/traceability sea necesaria para una distinción concreta;
- `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`, únicamente para continuidad con 2.1 y evitar duplicación.

Para **cada cita** incluida debes re-recuperar el full text original, verificar identidad, localizar el pasaje exacto y comprobar el alcance del claim conforme a MWDP-S01–S04.

Los 34 artículos KBS usados para estilo editorial no son automáticamente evidencia científica.

## Función narrativa de 2.2

La subsección debe explicar cómo la literatura incorpora **conocimiento externo, documentos, reglas o estructuras regulatorias** en tareas de clasificación, retrieval y razonamiento, y debe distinguir con precisión **qué función cumple ese conocimiento dentro del pipeline**.

El lector debe poder diferenciar, cuando la evidencia lo soporte:

1. conocimiento de nomenclatura/taxonomía o knowledge graphs que participa directamente en la selección o validación de códigos;
2. retrieval de documentos/pasajes/sentencias que luego participa en una predicción o generación;
3. reglas, restricciones jerárquicas o fuentes regulatorias usadas durante búsqueda, clasificación o reranking;
4. retrieval usado para exponer evidencia o material de respaldo alrededor de candidatos;
5. agentic/deep-search workflows en los que retrieval, reglas y razonamiento están acoplados a la decisión;
6. RAG/retrieve-then-generate como patrón general, diferenciándolo de query rewriting, query expansion, passage fusion o evidentiality cuando corresponda.

No construyas una taxonomía enciclopédica. Incluye solo distinciones que preparen el argumento de las subsecciones 2.3–2.6.

## Organización retórica esperada

Evita paper-by-paper. Una secuencia adecuada es:

`external knowledge in tariff/regulatory systems → knowledge participating in classification/selection → retrieved documents/passages as decision context → rule-/hierarchy-/agent-driven regulatory search → general RAG/retrieve-then-generate distinctions → synthesis and transition to LLM roles`.

La última parte debe preparar naturalmente **2.3 LLMs for classification, reasoning, and explanation**, sin redactarla.

## Distinciones científicas obligatorias

Preserva expresamente estas fronteras cuando sean pertinentes:

```text
CODE_RETRIEVAL ≠ SENTENCE_RETRIEVAL ≠ PRECEDENT_RETRIEVAL ≠ EVIDENCE_RETRIEVAL
CLASSIFICATION ≠ VALIDATION/CORRECTION
NOMENCLATURE_OR_TAXONOMY_KNOWLEDGE_USED_TO_DECIDE ≠ POST_RANKING_DOCUMENTARY_EVIDENCE
RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE
QUERY_EXPANSION/REWRITING ≠ EVIDENCE
RETRIEVED_PASSAGE ≠ EVIDENCE_ATTRIBUTION ≠ GROUNDING_GUARANTEE
CITATIONS_OR_REASONING_TRACE ≠ FORMAL_AUDITABILITY
PATH/RULE_CONSISTENCY ≠ INDEPENDENT_LEGAL_CORRECTNESS
CONSENSUS/SELF_CONSISTENCY ≠ INDEPENDENT_GROUND_TRUTH
```

## Restricciones del presente artículo

- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- No uses `first`, `unique`, `novel`, `no prior work` ni equivalentes para el presente estudio.
- No afirmes que candidate prediction + evidence retrieval sea nuevo por sí mismo.
- No afirmes que la literatura carezca de auditabilidad o trazabilidad de manera general.
- No describas todavía la arquitectura propuesta del presente artículo, el Top-3 fijo, la prohibición de reranking, el LLM local explanation-only ni su contrato funcional; esas comparaciones pertenecen principalmente a 2.6 y Section 3.
- No introduzcas NANDINA, Chapter/Class 87, H100, corpus peruano, DAM, tamaños de muestra ni resultados del estudio actual.
- No conviertas claims secundarios de WCO, autoridades, prensa o terceros citados por los papers en hechos propios sin verificar la fuente primaria.
- No generalices resultados de otros benchmarks/jurisdicciones a nuestro testbed.
- No equipares evidencia visible o citas con corrección jurídica.
- No conviertas ausencia de group split documentado en prueba de leakage.

## Prosa y extensión

Sigue KBS_EWG_34_V01 y SPCCR:

- síntesis funcional, no catálogo;
- oraciones con agente/acción/objeto claros;
- abstracción solo cuando vaya acompañada de operación concreta;
- transiciones explícitas entre familias funcionales;
- evita tono de tesis, gobernanza o especificación contractual.

Objetivo orientativo para la parte inglesa de 2.2: **650–900 palabras**, salvo que la evidencia rigurosamente necesaria justifique otra extensión.

No uses listas de viñetas dentro del manuscrito salvo necesidad científica clara.

## Word y comentarios de citas

En Part I, cada instancia de cita debe tener comentario Word anclado exactamente a la cita, con:

```text
Fuente / revista:
Autor(es):
Texto original exacto de respaldo:
Traducción al español:
Justificación semántica claim–fuente:
Límite de alcance, si corresponde:
```

Preserva los 8 comentarios aprobados de 2.1 sin modificación ni desplazamiento. La parte española debe ser semánticamente equivalente, pero no necesita comentarios duplicados salvo regla posterior.

Elimina únicamente la nota/placeholder de 2.2 que reemplaces por texto. No modifiques notas de otras secciones.

## Entregables obligatorios

Genera y versiona exclusivamente:

1. `article/sections/related_work/RelatedWork_B02_V01.md`;
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B02_V01.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B02_V01.docx`;
4. `article/responses/2_RELATED_WORK_B02_RESPONSE_V01.md`.

No modifiques ningún otro archivo.

## QA obligatorio

Antes del commit verifica:

- baseline DOCX SHA-256 exacto;
- preservación exacta de 2.1 EN/ES;
- preservación de los 8 comentarios de cita de 2.1;
- integridad OOXML del Word final;
- render completo del DOCX;
- equivalencia MD–DOCX para 2.2;
- equivalencia EN–ES;
- ninguna modificación accidental fuera de 2.2;
- comentarios de cita nuevos `n/n` para todas las instancias inglesas de 2.2;
- full text re-recuperado para cada cita;
- ninguna referencia inventada;
- ninguna fuente KBS-34 editorial usada como evidencia científica sin admisión;
- ausencia de novelty/gap final no autorizado;
- prosa KBS-34 fluida, concreta y comparativa;
- cero tracked changes residuales.

## Informe de entrega obligatorio

`article/responses/2_RELATED_WORK_B02_RESPONSE_V01.md` debe declarar como mínimo:

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
BLOCK = RELATED_WORK_B02
BLOCK_REVISION = V01
SECTION = 2.2
BASELINE_MASTER = ARTICLE_MASTER_V001
BASELINE_DOCX_SHA256_EXPECTED = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
BASELINE_DOCX_SHA256_VERIFIED = ...
SOURCE_SNAPSHOT(S) = ...
FULLTEXTS_RETRIEVED = [lista]
AUTHORIZED_CLAIMS_USED = ...
CONDITIONAL_CLAIMS_USED = ...
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [lista]
PRIOR_2_1_TEXT_PRESERVED = PASS / ISSUE
PRIOR_2_1_CITATION_COMMENTS_PRESERVED = 8/8 / ISSUE
NEW_CITATION_COMMENT_COVERAGE = n/n
TOTAL_CITATION_COMMENT_COUNT = ...
EN_ES_SEMANTIC_EQUIVALENCE = PASS / ISSUE
KBS_PROSE_QA = PASS / ISSUE
ABSTRACTION_DENSITY = ACCEPTABLE / ISSUE
AGENT_ACTION_OBJECT_CLARITY = PASS / ISSUE
NOMINALIZATION_OVERLOAD = ABSENT / ISSUE
MASTER_CANDIDATE_MD = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B02_V01.md
MASTER_CANDIDATE_DOCX = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B02_V01.docx
DOCX_OOXML_INTEGRITY = PASS / FAIL
DOCX_RENDER = PASS / FAIL
MD_DOCX_EQUIVALENCE = PASS / ISSUE
ENGLISH_SECTION_2_2_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```

## Stop rule

Tras generar los cuatro entregables y hacer un único commit semántico, **detente**.

No avances a 2.3, no redactes Introduction, no describas la arquitectura del presente estudio, no corrijas Methods B01, no modifiques gobernanza y no integres el candidato como master canónico. La IA Gestora realizará la revisión interna.