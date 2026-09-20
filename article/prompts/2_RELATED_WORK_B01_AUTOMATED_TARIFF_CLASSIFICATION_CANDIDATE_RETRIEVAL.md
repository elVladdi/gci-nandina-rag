# Prompt — Related Work B01 — Section 2.1 Automated tariff classification and candidate retrieval

## Rol

Actúa exclusivamente como **IA de Redacción** del artículo científico de `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

No eres IA Gestora ni IA Experimental. No modifiques gobernanza, decisiones, literatura congelada, Claim–Evidence Matrix, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` ni Plan Maestro experimental.

## Alcance autorizado

```text
BLOCK = RELATED_WORK_B01
BLOCK_REVISION = V01
SECTION = 2.1 Automated tariff classification and candidate retrieval
AUTHORIZED = YES
SECTIONS_2_2_TO_2_6 = NOT_AUTHORIZED
INTRODUCTION = NOT_AUTHORIZED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
METHODS_B01_V06 = NOT_AUTHORIZED
```

Debes redactar **exclusivamente la subsección 2.1** en inglés y su espejo semántico en español dentro del manuscrito acumulativo.

## Onboarding obligatorio

Antes de redactar, lee íntegramente y aplica:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md` — V2.1 vigente;
4. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — `MWDP_V1.0 / FROZEN`;
5. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
6. `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md`, cuyo contenido está aprobado y activado por D-013;
7. `article/governance/D014_ARTICLE_STRUCTURE_AND_DRAFTING_ORDER_RESET.md`;
8. `article/governance/D015_KBS_ARTICLE_STRUCTURE_APPROVAL_AND_RELATED_WORK_START.md`;
9. `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`;
10. `article/CLAIM_EVIDENCE_MATRIX.md`;
11. `article/BIBLIOGRAPHIC_FRAMEWORK.md` y el manifiesto de acceso full-text gobernante.

## Baseline Word obligatorio

El baseline binario aprobado es:

```text
FILENAME = KBS_ARTICLE_WORKING_STRUCTURE_V01.docx
SHA256 = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
```

Debes localizar el archivo exacto en los recursos disponibles del proyecto/File Library o en el contexto proporcionado por el autor y verificar su SHA-256 antes de editarlo.

Si no puedes acceder al Word exacto o el hash no coincide:

```text
BASELINE_DOCX_ACCESS_REQUIRED = YES
```

y **detente sin reconstruir el Word desde cero**.

## Fuentes científicas prioritarias para 2.1

Debes trabajar principalmente con:

- `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`;
- `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`;
- `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`, solo cuando una distinción retrieval/validation sea materialmente pertinente.

Estas matrices congeladas sirven para orientar qué literatura es pertinente, **pero no autorizan citar por memoria**. Para cada cita incluida debes re-recuperar el full text de la fuente original, verificar identidad y localizar el pasaje exacto conforme a `MWDP-S01`–`MWDP-S04`.

Los 34 artículos KBS analizados para estilo editorial **no son automáticamente fuentes científicas** de esta subsección. Solo pueden usarse como evidencia de estilo/redacción, salvo que una fuente haya sido admitida científicamente mediante el proceso bibliográfico correspondiente.

## Función narrativa de la subsección 2.1

La subsección debe permitir que un lector de KBS entienda, antes de entrar a RAG, LLM o evidencia normativa, **cómo ha evolucionado el problema técnico de asignar o recuperar códigos arancelarios a partir de descripciones de productos** y qué familias de tareas aparecen en la literatura.

Debe sintetizar, cuando la evidencia disponible lo soporte:

1. clasificación directa de descripciones de productos hacia códigos HS/tarifarios;
2. clasificación jerárquica o explotación explícita de la jerarquía cuando corresponda;
3. recuperación/ranking de códigos o precedentes como tarea distinta de clasificación directa;
4. validación/corrección de códigos ya asignados cuando sea pertinente para distinguir objetivos de tarea;
5. evolución de representaciones/modelos relevantes —por ejemplo métodos supervisados, deep learning, transformers/embeddings, retrieval— solo en la medida necesaria para comparar funciones y no como catálogo histórico exhaustivo;
6. diferencias en nivel objetivo, datasets, esquemas de validación y métricas solo cuando ayuden a explicar por qué los resultados de trabajos distintos no son directamente intercambiables.

## Organización retórica esperada

No redactes autor por autor ni paper por paper. Organiza por **familias de tareas/enfoques** y usa las referencias para respaldar la síntesis.

Una secuencia apropiada es:

`problema de clasificación arancelaria → clasificación directa/jerárquica → modelos de representación → retrieval/ranking como formulación distinta → validation/correction como tarea distinta → síntesis de lo que esta literatura resuelve y de las fronteras que quedan para las siguientes subsecciones`.

La última parte de 2.1 debe preparar naturalmente la transición a **2.2 Knowledge-enhanced retrieval and regulatory reasoning**, sin empezar a redactar 2.2.

## Restricciones científicas y editoriales

- No declares el `FINAL_GAP`; sigue `NOT_DEFINED`.
- No declares novelty universal.
- No uses `no prior work`, `first`, `unique`, `novel` o equivalentes salvo autorización explícita y evidencia exhaustiva que actualmente no existe.
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`.
- No presentes diferencias arquitectónicas como novelty por sí mismas.
- No introduzcas resultados del presente trabajo.
- No introduzcas H100, tamaños de muestra, Chapter 87, corpus peruano, particiones DAM ni detalles del testbed experimental, salvo que una mención mínima sea absolutamente necesaria para una transición; por defecto, no son parte de 2.1.
- No describas todavía la arquitectura propuesta ni el Top-3 fijo; esas funciones pertenecen a secciones posteriores y a 2.6 para posicionamiento comparativo.
- No mezcles `classification`, `candidate retrieval`, `validation/correction` como si fueran la misma tarea.
- No llames `accuracy` a métricas de retrieval si la fuente evalúa ranking/recall/top-k/MRR.
- No atribuyas legal correctness a una predicción de código.
- Evita párrafos de definiciones genéricas y abstracciones acumuladas.
- Evita tono de tesis, estado administrativo, especificación contractual o documento de gobernanza.
- Sigue la prosa KBS-34: oraciones claras, agente/acción/objeto identificables, síntesis comparativa y transiciones fluidas.

## Extensión y forma

Objetivo orientativo para la parte inglesa de 2.1: **aprox. 550–800 palabras**, salvo que la evidencia rigurosamente necesaria justifique una extensión distinta.

No uses listas de viñetas dentro de la subsección del manuscrito salvo necesidad científica clara. Debe leerse como prosa de artículo de investigación.

Las citas deben integrarse en la prosa y no acumularse mecánicamente al final de párrafos con claims heterogéneos.

## Word y comentarios de citas

En la Parte I inglesa, **cada instancia de cita** debe tener comentario de Word anclado exactamente a la cita con:

```text
Fuente / revista:
Autor(es):
Texto original exacto de respaldo:
Traducción al español:
Justificación semántica claim–fuente:
Límite de alcance, si corresponde:
```

La parte española no requiere duplicar comentarios si el protocolo no lo exige, pero debe ser semánticamente equivalente a la inglesa.

No elimines notas editoriales de otras secciones. En 2.1, sustituye la nota/placeholder correspondiente por el texto redactado y conserva el resto del documento intacto.

## Entregables obligatorios

Genera y versiona exclusivamente:

1. `article/sections/related_work/RelatedWork_B01_V01.md` — texto bilingüe del bloque;
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B01_V01.md` — estructura acumulativa completa con 2.1 insertada;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B01_V01.docx` — Word acumulativo derivado **del baseline exacto**, no reconstruido;
4. `article/responses/2_RELATED_WORK_B01_RESPONSE_V01.md` — informe de ejecución.

No modifiques ningún otro archivo.

## QA obligatorio antes de commit

Verifica:

- baseline DOCX SHA-256 correcto antes de editar;
- integridad OOXML del Word final;
- render del DOCX;
- equivalencia Markdown–DOCX para 2.1;
- equivalencia EN–ES;
- ninguna modificación accidental de otras secciones;
- cobertura de comentarios de cita `n/n`;
- todos los full texts usados recuperados y verificados;
- ninguna referencia inventada;
- ninguna fuente KBS-34 editorial usada como evidencia científica sin admisión bibliográfica;
- ausencia de claims de novelty/gap no autorizados;
- prosa fluida y no abstracta según KBS_EWG_34_V01 y SPCCR;
- sin tracked changes residuales ni comentarios ajenos a los comentarios de auditoría de citas.

## Informe de entrega obligatorio

`article/responses/2_RELATED_WORK_B01_RESPONSE_V01.md` debe declarar como mínimo:

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
STRUCTURE_DECISION = D-015
BLOCK = RELATED_WORK_B01
BLOCK_REVISION = V01
SECTION = 2.1
BASELINE_DOCX_SHA256_EXPECTED = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
BASELINE_DOCX_SHA256_VERIFIED = ...
SOURCE_SNAPSHOT(S) = ...
FULLTEXTS_RETRIEVED = [lista]
AUTHORIZED_CLAIMS_USED = ...
CONDITIONAL_CLAIMS_USED = ...
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [lista]
CITATION_COMMENT_COVERAGE = n/n
EN_ES_SEMANTIC_EQUIVALENCE = PASS / ISSUE
KBS_PROSE_QA = PASS / ISSUE
ABSTRACTION_DENSITY = ACCEPTABLE / ISSUE
AGENT_ACTION_OBJECT_CLARITY = PASS / ISSUE
NOMINALIZATION_OVERLOAD = ABSENT / ISSUE
MASTER_CANDIDATE_MD = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B01_V01.md
MASTER_CANDIDATE_DOCX = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B01_V01.docx
DOCX_OOXML_INTEGRITY = PASS / FAIL
DOCX_RENDER = PASS / FAIL
MD_DOCX_EQUIVALENCE = PASS / ISSUE
ENGLISH_SECTION_2_1_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```

## Stop rule

Tras generar los cuatro entregables y hacer un único commit semántico, **detente**.

No avances a 2.2, no redactes Introduction, no corrijas Methods B01, no modifiques gobernanza y no integres el candidato como master canónico. La IA Gestora realizará la revisión interna y el autor decidirá la aprobación.