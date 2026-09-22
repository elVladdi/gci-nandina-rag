# Architecture B01 — Internal Review V01

## Español

```text
REVIEW = 4_ARCHITECTURE_B01_INTERNAL_REVIEW_V01
DATE = 2026-09-22
ROLE = IA_GESTORA / INDEPENDENT_EDITORIAL_AND_SCIENTIFIC_AUDIT
BLOCK = ARCHITECTURE_B01
AUTHORIZED_SCOPE = SECTIONS_3_1_TO_3_4_ONLY
PROMPT = article/prompts/4_ARCHITECTURE_B01_OVERVIEW_HISTORICAL_FIXED_TOP3.md@7ffd10572fd4563cfe33584ed193c88e9399bc50
DRAFTING_RESPONSE = article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md@688b83bf352ceb89ac41ca4147162e4afb0a640c
CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V01.docx
CANDIDATE_DOCX_SHA256 = 485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx
BASELINE_DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
SCIENTIFIC_CONTENT_REVIEW = PASS_WITH_ONE_MINOR_CORRECTION
DOCX_BINARY_AND_RENDER_QA = PASS
PRIOR_APPROVED_CONTENT_PRESERVATION = PASS
GITHUB_SEMANTIC_DELIVERY = BLOCKED / INCOMPLETE
OVERALL_REVIEW = PASS_WITH_CORRECTIONS / DELIVERY_BLOCKED
AUTHOR_APPROVAL_GATE = NOT_OPEN
ARTICLE_MASTER_V008 = NOT_PROMOTED
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Alcance de la auditoría

La IA Gestora auditó de forma independiente el commit de respuesta, el DOCX entregado al autor, la preservación del baseline aprobado, el contenido científico de 3.1–3.4, las fuentes arquitectónicas y de implementación pertinentes, y el estado experimental concurrente. Los `PASS` autodeclarados por la IA de Redacción no se tomaron como evidencia suficiente por sí mismos.

### 2. Commit y cumplimiento de alcance

El commit `688b83bf352ceb89ac41ca4147162e4afb0a640c` tiene como padre directo el prompt `7ffd10572fd4563cfe33584ed193c88e9399bc50` y añadió únicamente:

`article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md`

No modificó governance, `ARTICLE_STATUS`, `ARTICLE_WRITING_PLAN`, claims, fuentes, el master canónico ni secciones posteriores. Tampoco promovió `ARTICLE_MASTER_V008` ni abrió B02 o Experimental design.

Esto confirma que el bloqueo de transferencia fue registrado sin introducir una entrega científica parcial. Al mismo tiempo, confirma que los dos artefactos Markdown científicos exigidos por el prompt no fueron versionados y, por tanto, la entrega semántica de B01 en GitHub está incompleta.

### 3. Auditoría independiente del DOCX

El binario entregado fue verificado directamente:

- SHA-256 real: `485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53` — coincide exactamente con la respuesta V01;
- el baseline disponible presenta SHA-256 `d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c` — coincide con el baseline gobernante;
- paquete OOXML íntegro, sin miembros ZIP corruptos;
- `word/comments.xml` SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603` tanto en baseline como en candidato;
- 40 comentarios, 40 `commentRangeStart`, 40 `commentRangeEnd` y 40 `commentReference`, sin IDs huérfanos o duplicados;
- `w:ins = 0`, `w:del = 0`, `w:moveFrom = 0`, `w:moveTo = 0`;
- al comparar ambos paquetes, el único miembro OOXML cuyo contenido cambia es `word/document.xml`;
- la comparación de párrafos muestra cambios únicamente en los espacios de redacción correspondientes a 3.1–3.4 en Part I y Part II; Introduction, Related Work, 3.5–3.7 y las secciones posteriores permanecen sin modificación científica;
- render completo: 34 páginas;
- inspección visual independiente: 34/34 páginas, sin clipping, solapamientos, truncamiento, pérdida de contenido ni defectos de maquetación detectados.

Por tanto, `DOCX_BINARY_AND_RENDER_QA = PASS` y `PRIOR_APPROVED_CONTENT_PRESERVATION = PASS`.

### 4. Auditoría científica de 3.1–3.4

El contenido nuevo cumple el objetivo narrativo de B01.

**3.1 Overview and information flow.** La descripción comercial se transforma en consulta normalizada; la recuperación histórica determina el ranking antes de cualquier recuperación normativa o invocación generativa; los tres primeros códigos únicos forman el Top-3 fijo; y recuperación documental, construcción de contexto y LLM quedan downstream sin autoridad para cambiar membresía u orden. La ruta de reranking permanece explícitamente diagnóstica y fuera del flujo principal.

**3.2 Query representation and normalization.** La redacción distingue correctamente el requisito arquitectónico —una interfaz textual normalizada y reproducible— de las operaciones concretas de limpieza/tokenización que deben especificarse en la instanciación experimental. No convierte una receta particular de preprocessing en requisito universal.

**3.3 Historical candidate retrieval and ranking.** La secuencia descrita es observable y consistente con la implementación gobernante: scoring a nivel de registros históricos, ordenamiento, trazabilidad del registro fuente, deduplicación por código conservando la primera aparición mejor posicionada y formación de un ranking Top-k de códigos únicos. BM25 se identifica correctamente como instanciación experimental y no como requisito universal de la arquitectura. Las puntuaciones no se presentan como probabilidades de corrección jurídica.

**3.4 Fixed candidate set.** El Top-3 se define operacionalmente como los tres primeros códigos únicos del ranking histórico y queda inmutable en membresía y orden para el flujo principal. Las etapas posteriores enriquecen el conjunto, pero no lo revisan. La separación entre métricas de recuperación, asociación documental y explicación queda formulada sin convertir ninguna de ellas en corrección jurídica.

No se detectó fuga de resultados, cifras de desempeño, H100, tamaños de datasets ni una apertura prematura desde Clase/Capítulo 87. No se añadieron citas bibliográficas nuevas, lo cual es apropiado porque el bloque describe el diseño propio y sus interfaces.

### 5. Compatibilidad con fuentes y estado experimental concurrente

SRC-02 mantiene el diseño según el cual BM25 histórico produce/fija el Top-3 en la instanciación, la evidencia normativa opera después y el LLM local explica sin modificar el ranking. La implementación `evaluate_historical_retrieval_data_aduanas_v02.py@ca065618d5df0019f76ef5a971e858d91c263e1f` es consistente con la deduplicación y trazabilidad descritas en 3.3.

La IA Gestora verificó además el cambio concurrente del Plan Maestro en `b74b96d0163807007e4579d86450dd235125b30f`: G6-F01 pasó a `CLOSED / APPROVED / INTEGRATED_TO_MAIN`, Grupo 6 quedó `IN_PROGRESS` y G6-F02 sigue no autorizado/no ejecutado. Ese cambio integra únicamente la especificación de figuras y declara expresamente que no generó figuras, nuevos resultados, métricas o inferencia ni modificó artículo o tesis. No introduce conflicto científico con Architecture B01 y no autoriza incorporar una figura final en este bloque.

### 6. Corrección editorial menor obligatoria

Se detectó un residuo estructural en Part II. Inmediatamente después de:

`3. Arquitectura de apoyo a decisiones`

seguido de la nota interna:

`Describir primero la arquitectura general. No abrir esta sección con NANDINA, Capítulo 87, corpus peruano, H100 ni tamaños del experimento.`

permanece la línea:

`[Section text to be drafted in a later approved version.]`

antes de `3.1. Vista general y flujo de información`.

Esa línea ya no describe el estado real de Section 3 después de redactar 3.1–3.4 y no tiene contraparte equivalente en Part I. Debe eliminarse. No deben eliminarse los placeholders de 3.5–3.7 ni modificarse los párrafos científicos aprobables de 3.1–3.4.

La observación es editorial/estructural y no invalida el contenido científico de B01.

### 7. Bloqueo de entrega GitHub

El prompt B01 exigía versionar simultáneamente:

1. `article/sections/architecture/Architecture_B01_V01.md`;
2. un master candidato acumulativo Markdown;
3. la respuesta operacional.

El commit V01 contiene solo la respuesta. En consecuencia:

```text
SCIENTIFIC_DRAFT_EXISTS_IN_DOCX = YES
SCIENTIFIC_CONTENT_AUDIT = PASS_WITH_ONE_MINOR_CORRECTION
GITHUB_SECTION_MD = MISSING
GITHUB_CUMULATIVE_CANDIDATE_MD = MISSING
GITHUB_SEMANTIC_DELIVERY = INCOMPLETE
INTEGRATION_ELIGIBLE = NO
```

El bloqueo es técnico, no una razón para rehacer el contenido científico. La corrección debe preservar la redacción de 3.1–3.4 y completar la transferencia exacta de los artefactos Markdown.

Leer un Markdown local verificado y transferir literalmente su contenido mediante el campo textual de la API de GitHub no constituye una nueva redacción científica ni una reconstrucción manual, siempre que el texto sea verificado antes y después de la transferencia. Si los Markdown locales originales ya no existen, pueden derivarse de forma controlada del DOCX candidato exacto y del master canónico, sin reescribir la prosa y dejando trazabilidad de esa operación.

### 8. Dictamen

```text
SCIENTIFIC_CONTENT = PASS_WITH_ONE_MINOR_CORRECTION
SOURCE_FIDELITY = PASS
ARCHITECTURAL_COHERENCE = PASS
IMPLEMENTATION_CONSISTENCY = PASS
SCOPE_CONTROL = PASS
OVERCLAIMING_CONTROL = PASS
EN_ES_MANUSCRIPT_EQUIVALENCE = PASS_EXCEPT_STALE_SPANISH_SECTION_PLACEHOLDER
DOCX_QA = PASS
GITHUB_REQUIRED_ARTIFACTS = FAIL / INCOMPLETE
OVERALL_REVIEW = PASS_WITH_CORRECTIONS / DELIVERY_BLOCKED
```

No procede todavía solicitar aprobación autoral, integrar B01, promover `ARTICLE_MASTER_V008`, abrir Architecture B02 ni abrir Experimental design. El siguiente paso permitido es exclusivamente una corrección/entrega técnica de B01.

---

## English

```text
REVIEW = 4_ARCHITECTURE_B01_INTERNAL_REVIEW_V01
DATE = 2026-09-22
ROLE = MANAGING_AI / INDEPENDENT_EDITORIAL_AND_SCIENTIFIC_AUDIT
BLOCK = ARCHITECTURE_B01
PROMPT = article/prompts/4_ARCHITECTURE_B01_OVERVIEW_HISTORICAL_FIXED_TOP3.md@7ffd10572fd4563cfe33584ed193c88e9399bc50
DRAFTING_RESPONSE = article/responses/4_ARCHITECTURE_B01_RESPONSE_V01.md@688b83bf352ceb89ac41ca4147162e4afb0a640c
CANDIDATE_DOCX_SHA256 = 485b2ff1c048362fa2200e2f35e81159c5424886e48c38309950e406c2ff9c53
SCIENTIFIC_CONTENT_REVIEW = PASS_WITH_ONE_MINOR_CORRECTION
DOCX_BINARY_AND_RENDER_QA = PASS
PRIOR_APPROVED_CONTENT_PRESERVATION = PASS
GITHUB_SEMANTIC_DELIVERY = BLOCKED / INCOMPLETE
OVERALL_REVIEW = PASS_WITH_CORRECTIONS / DELIVERY_BLOCKED
AUTHOR_APPROVAL_GATE = NOT_OPEN
ARTICLE_MASTER_V008 = NOT_PROMOTED
ARCHITECTURE_B02 = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The Managing AI independently audited the response commit, the delivered DOCX, preservation of the approved baseline, scientific content in Sections 3.1–3.4, the relevant architecture/implementation sources, and the concurrent experimental update.

The candidate DOCX hash exactly matches the response. OOXML integrity passes; there are 40 comments and complete anchors; tracked changes are zero; `comments.xml` is byte-identical to the approved baseline; only `word/document.xml` differs between the baseline and candidate packages; paragraph-level differences are confined to the intended B01 drafting locations; and all 34 rendered pages pass visual inspection.

Scientifically, B01 correctly separates normalized query preparation, historical record retrieval/ranking, code-level deduplication with traceable historical precedent, and the fixed Top-3 boundary. Normative retrieval and the local LLM remain downstream without authority to change candidate membership or order, and diagnostic reranking remains outside the primary path. No results, benchmark figures, premature Chapter-87 scope, novelty claim, or legal-correctness claim was introduced.

One minor structural correction is required in Part II: remove the stale generic line `[Section text to be drafted in a later approved version.]` located between the Section 3 drafting note and `3.1. Vista general y flujo de información`. Keep the placeholders for Sections 3.5–3.7 and do not redraft the scientific B01 prose.

The larger operational issue is that the required section Markdown and cumulative candidate Markdown were not committed. Therefore GitHub semantic delivery remains incomplete even though the scientific draft is substantially sound. B01 cannot yet be approved, frozen, integrated, or used to open B02. The next action is restricted to the controlled correction and completion of B01 delivery.