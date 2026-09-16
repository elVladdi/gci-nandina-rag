# Protocolo maestro de escritura y entrega / Master Writing and Delivery Protocol

```text
PROTOCOL_ID = MWDP
PROTOCOL_VERSION = 1.0
STATUS = FROZEN
AUTHORITY = PHASE_0D_AUTHOR_APPROVAL
```

## Español

### 1. Autoridad, alcance y precedencia

Este protocolo es la fuente de verdad acumulativa para toda redacción, revisión, integración y entrega posterior del manuscrito. Debe leerse íntegramente antes de ejecutar cualquier bloque de Fase 1 en adelante.

Reglas de precedencia:

1. las fuentes científicas/experimentales gobernantes conservan su autoridad sobre hechos y resultados;
2. `ARTICLE_STATUS.md`, `CLAIM_EVIDENCE_MATRIX.md`, `DECISIONS.md` y este protocolo gobiernan el estado editorial y las condiciones de uso;
3. un prompt específico de bloque puede restringir más el trabajo, pero **no puede omitir, debilitar ni sustituir silenciosamente** este protocolo;
4. una regla posterior solo modifica este protocolo mediante una enmienda explícita, versionada, bilingüe, auditada y aprobada por el autor;
5. ausencia de una regla en un prompt concreto no significa derogación.

### 2. Roles

**MWDP-R01 — IA Gestora.** Controla estado, secuencia, prompts, auditoría científica/editorial, gates y freeze. No ejecuta experimentos y no modifica el Plan Maestro experimental. Normalmente no genera ni actualiza el Word maestro.

**MWDP-R02 — IA de Redacción.** Genera y actualiza los bloques del manuscrito, el master acumulativo `.md` candidato y el master acumulativo `.docx` candidato. No modifica por su cuenta claims, decisiones, reviews, literatura congelada, `ARTICLE_STATUS.md` ni Plan Maestro.

**MWDP-R03 — IA Experimental.** Tiene autoridad exclusiva sobre ejecución/auditoría/cierre experimental y escritura del Plan Maestro. No administra el Word del manuscrito.

**MWDP-R04 — Autor.** Aprueba o rechaza bloques, autoriza freezes y gestiona Mendeley únicamente en la etapa final.

### 3. Artefactos acumulativos obligatorios

**MWDP-A01.** Cada bloque se trabaja como artefacto versionado independiente, por ejemplo `Methods_B01_V01.md`.

**MWDP-A02.** Toda integración aprobada actualiza dos masters acumulativos inseparables:

```text
ARTICLE_MASTER_V00N.md
ARTICLE_MASTER_V00N.docx
```

**MWDP-A03.** El `.md` es la capa estable de contenido y trazabilidad de fuentes; no es autoridad de formato APA 7.

**MWDP-A04.** El `.docx` es la capa editable de revisión interna y presentación provisional.

**MWDP-A05.** El siguiente bloque parte del último master aprobado. Está prohibido reconstruir silenciosamente el Word desde cero o perder contenido, comentarios, estilos semánticos, tablas, captions o trazabilidad ya aprobados.

### 4. Layout e idioma del Word

**MWDP-W01.** `DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER`.

El Word interno contiene:

- Part I — English manuscript master;
- Part II — Spanish semantic-control mirror.

**MWDP-W02.** Ambas partes deben conservar equivalencia semántica de claims, cifras, métricas, límites, incertidumbre y condiciones experimentales.

**MWDP-W03.** La parte española se elimina únicamente mediante gate explícito al preparar la copia final de submission; esa operación no puede alterar el contenido científico aprobado.

**MWDP-W04.** `WORD = PROVISIONAL_APA7_PRESENTATION_LAYER`. APA 7 es provisional durante la construcción del Word. No se atribuye a KBS como estilo final.

**MWDP-W05.** `MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY`.

**MWDP-W06.** La conversión final y gestión de referencias con Mendeley corresponde exclusivamente al autor.

### 5. Comentarios obligatorios de auditoría de citas en Word

**MWDP-C01.** Toda instancia de cita en la parte inglesa del Word debe llevar un comentario de Word anclado exactamente a esa cita.

**MWDP-C02.** Cada comentario debe contener como mínimo:

```text
Fuente / revista:
Autor(es):
Texto original exacto de respaldo:
Traducción al español:
Justificación semántica claim–fuente:
Límite de alcance, si corresponde:
```

**MWDP-C03.** El extracto debe ser suficiente para verificar el claim y conservar el idioma original de la fuente. No se sustituye por una paráfrasis inventada.

**MWDP-C04.** Una misma referencia usada para claims distintos requiere comentarios independientes cuando la justificación sea distinta.

**MWDP-C05.** Un comentario anclado al párrafo o a una cita diferente no satisface el requisito.

**MWDP-C06.** Antes de la gestión final con Mendeley debe ejecutarse QA para evitar que la conversión de citas destruya o desplace los comentarios anclados.

### 6. Recuperación y verificación de fuentes

**MWDP-S01.** El manifiesto `REF-001`–`REF-062` de `article/reviews/0D2_BIBLIOGRAPHIC_FULLTEXT_ACCESS_AUDIT.md` facilita recuperación, pero no autoriza citar por memoria.

**MWDP-S02.** Antes de cada cita la IA de Redacción debe volver a recuperar el full text, verificar identidad, localizar el pasaje exacto y comprobar que el claim no excede fuerza, población, tarea, dataset, causalidad ni transferibilidad de la fuente.

**MWDP-S03.** Si el full text no puede recuperarse en la sesión activa, usar `ACCESS_RECHECK_REQUIRED`; no inventar extractos ni confiar en snippets, resúmenes o memoria.

**MWDP-S04.** Una referencia nueva solo puede entrar al manuscrito si cumple el marco bibliográfico y alcanza `APPROVED_NEW`.

### 7. Contrato claim–evidence y controles anti-overclaiming

**MWDP-E01.** Toda afirmación factual, numérica, metodológica o comparativa debe estar autorizada y trazable.

**MWDP-E02.** Está prohibido inventar números, citas, DOI, metadatos, resultados, interpretaciones experimentales o evidencia.

**MWDP-E03.** Los estados `AUTHORIZED`, `CONDITIONAL`, `REVIEW_REQUIRED` y `PROHIBITED` de `CLAIM_EVIDENCE_MATRIX.md` son vinculantes.

**MWDP-E04.** Permanecen obligatorias las fronteras:

```text
LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM
ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE
ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF
JOURNAL_FIT ≠ NOVELTY_PROOF
CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY
NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY ≠ LEGAL_CORRECTNESS
CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION
```

**MWDP-E05.** No usar lenguaje causal sin diseño causal que lo autorice.

**MWDP-E06.** C10/C11 permanecen bloqueados hasta reconciliación editorial explícita. Grupo 3 sigue requerido para el cierre final de RQ4 y de las inferencias HE2/HE5 aplicables.

### 8. Arquitectura científica que no puede alterarse silenciosamente

**MWDP-F01.** El contrato funcional gobernante es:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

**MWDP-F02.** Flujo:

`Descripción comercial → normalización → recuperación histórica → ranking histórico Top-k → Top-3 fijo → evidencia normativa por candidato → construcción de contexto → LLM local → explicación auditable`.

**MWDP-F03.** Cualquier cambio a arquitectura, unidades, particiones, métricas, hipótesis, claim central, interpretación experimental o alcance exige gate explícito.

### 9. Ciclo obligatorio por bloque

**MWDP-B01.** Antes de redactar: onboarding completo, estado live de GitHub, fuentes, claims y dependencias.

**MWDP-B02.** La IA Gestora emite un prompt cerrado que referencia expresamente este protocolo y el bloque autorizado.

**MWDP-B03.** La IA de Redacción produce V01 sin avanzar a otros bloques.

**MWDP-B04.** La IA Gestora audita claim por claim, estructura, terminología, citas, equivalencia bilingüe, Word, comentarios de citas y versionado.

**MWDP-B05.** Si cambia un hecho/result/inferencia experimental o se alcanza un trigger experimental, se requiere revisión de IA Experimental. Si no, se registra `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

**MWDP-B06.** Correcciones generan V02/V03 del bloque o del master candidato, sin simular una nueva integración.

**MWDP-B07.** Solo tras aprobación expresa del autor se integra el bloque al master canónico.

### 10. Versionado

**MWDP-V01.** `BLOCK_REVISION`: V01, V02… del bloque individual.

**MWDP-V02.** `MASTER_CANDIDATE_REVISION`: correcciones del candidato acumulativo antes de integración aprobada.

**MWDP-V03.** `MASTER_INTEGRATION`: únicamente una integración aprobada incrementa `ARTICLE_MASTER_V00N`.

**MWDP-V04.** Nunca sobrescribir silenciosamente un master aprobado ni reutilizar su número para contenido diferente.

### 11. Política editorial y revistas

**MWDP-J01.** Target A: `Knowledge-Based Systems`.

**MWDP-J02.** Plan B: `Expert Systems with Applications`.

**MWDP-J03.** Plan C: `Information Processing & Management`.

**MWDP-J04.** La redacción debe preservar un núcleo científico común para minimizar reescritura ante transferencia de revista.

**MWDP-J05.** `Research article` es el tipo operativo actual.

**MWDP-J06.** Requisitos KBS no verificados desde fuente primaria accesible —plantilla específica, límite exacto, free-format, headings obligatorios, estilo final de referencias y otros detalles de submission— no se inventan. Rige master neutral/reversible y revalidación antes del paquete final.

### 12. Disciplina de extensión

**MWDP-L01.** Registrar en cada integración candidata el conteo de palabras del texto principal inglés separado de referencias, tablas, captions y declaraciones.

**MWDP-L02.** Evitar redundancia entre prosa, tablas y figuras; una función científica principal por párrafo.

**MWDP-L03.** No sacrificar evidencia necesaria o reproducibilidad para cumplir un límite no verificado.

### 13. Checklist obligatorio de cada entrega de IA de Redacción

Toda entrega debe declarar explícitamente:

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = ...
BLOCK_REVISION = ...
SOURCE_SNAPSHOT(S) = ...
AUTHORIZED_CLAIMS_USED = ...
CONDITIONAL_CLAIMS_USED = ...
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [lista]
CITATION_COMMENT_COVERAGE = n/n
EN_ES_SEMANTIC_EQUIVALENCE = PASS / NOT_APPLICABLE / ISSUE
MASTER_CANDIDATE = ...
ENGLISH_MAIN_TEXT_WORD_COUNT = ...
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
```

La ausencia de cualquiera de estos campos es una observación de entrega y debe corregirse antes de integración.

### 14. Enmiendas

**MWDP-G01.** Este protocolo es acumulativo. Las nuevas reglas se agregan; no se eliminan reglas anteriores por omisión.

**MWDP-G02.** Toda enmienda debe indicar versión anterior, reglas afectadas, motivo, impacto, revisión y aprobación del autor.

**MWDP-G03.** Una regla congelada solo cambia mediante una nueva versión explícita de este protocolo; nunca mediante conversación aislada o instrucción de bloque no registrada.

---

## English

### 1. Authority, scope, and precedence

This protocol is the cumulative source of truth for all subsequent manuscript drafting, review, integration, and delivery. It must be read in full before any Phase-1-or-later block is executed.

Scientific/experimental governing sources retain authority over facts and results. `ARTICLE_STATUS.md`, `CLAIM_EVIDENCE_MATRIX.md`, `DECISIONS.md`, and this protocol govern editorial state and use conditions. A block prompt may be stricter but may not silently omit, weaken, or replace this protocol. Any later change requires an explicit, versioned, bilingual, audited, author-approved amendment. Omission from a block prompt is not repeal.

### 2. Roles

**MWDP-R01. Managing AI:** controls editorial state, sequence, prompts, audits, gates, and freezes; does not execute experiments or modify the experimental Master Plan and normally does not generate/update the Word master.

**MWDP-R02. Writing AI:** generates/updates manuscript blocks and cumulative candidate `.md`/`.docx` masters; it does not independently change claims, decisions, reviews, frozen literature, editorial status, or the experimental Master Plan.

**MWDP-R03. Experimental AI:** owns experimental execution/audit/closure and Master-Plan writing; it does not manage manuscript Word.

**MWDP-R04. Author:** approves/rejects blocks, authorizes freezes, and performs final Mendeley management.

### 3. Mandatory cumulative artifacts

Each block is independently versioned. Every approved integration updates the paired cumulative masters `ARTICLE_MASTER_V00N.md` and `ARTICLE_MASTER_V00N.docx`. Markdown is the stable content/source-traceability layer, not APA-7 formatting authority. Word is the editable internal-review/provisional-presentation layer. Each new block starts from the latest approved master; silent reconstruction from scratch or loss of approved content/comments/styles/tables/captions/traceability is prohibited.

### 4. Word language and layout

`DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER`: Part I is the English publication manuscript and Part II is the Spanish semantic-control mirror. They must remain semantically equivalent. Removing the Spanish mirror requires an explicit submission-preparation gate and may not change approved science. Word uses provisional APA 7; Markdown does not. Final Mendeley management belongs to the author.

### 5. Mandatory Word citation-audit comments

Every citation instance in the English Word part must have a comment anchored exactly to that citation, containing source/journal, author(s), exact original supporting passage, Spanish translation, claim–source semantic justification, and scope limit when relevant. Distinct claims supported by the same reference require distinct comments when their justification differs. Paragraph-level or mismatched anchoring does not satisfy the rule. Before final Mendeley conversion, QA must verify preservation of comment anchors.

### 6. Source re-retrieval and verification

The `REF-001`–`REF-062` manifest supports retrieval but never authorizes citation from memory. Before every citation, the Writing AI must re-retrieve the full text, verify identity, locate the exact supporting passage, and ensure the claim does not exceed the source's strength, population, task, dataset, causality, or transferability. Retrieval failure produces `ACCESS_RECHECK_REQUIRED`; snippets, abstracts, or memory may not substitute. New references require the governed admission process and `APPROVED_NEW` status.

### 7. Claim–evidence and anti-overclaiming contract

All factual, numerical, methodological, and comparative claims must be authorized and traceable. Invented numbers, citations, metadata, results, interpretations, or evidence are prohibited. `CLAIM_EVIDENCE_MATRIX.md` statuses are binding. The following boundaries remain mandatory:

```text
LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM
ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE
ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF
JOURNAL_FIT ≠ NOVELTY_PROOF
CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY
NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY ≠ LEGAL_CORRECTNESS
CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION
```

Causal language requires a causal design. C10/C11 remain blocked until explicit reconciliation. Group 3 remains required for final RQ4 and applicable HE2/HE5 inference.

### 8. Frozen scientific architecture

The governing functional contract is `EXTERNAL_FIXED_HISTORICAL_RANKING + POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT_DELETE_SUBSTITUTE_REORDER + NO_CLASSIFICATION_FEEDBACK + DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS + FUNCTION_SPECIFIC_EVALUATION`.

The flow is commercial description → normalization → historical retrieval → historical Top-k → fixed Top-3 → candidate-specific normative evidence → context construction → local LLM → auditable explanation. Architecture, units, partitions, metrics, hypotheses, central claims, experimental interpretation, or generalization scope cannot be changed without an explicit gate.

### 9. Mandatory block cycle

Each block requires current onboarding; a constrained prompt explicitly referencing this protocol; Writing-AI V01 limited to the authorized block; Managing-AI claim-level/content/version/Word/citation-comment audit; Experimental-AI review only when experimentally triggered; explicit revisions; author approval; and only then integration into the canonical master.

### 10. Versioning

`BLOCK_REVISION` tracks individual block V01/V02/etc. `MASTER_CANDIDATE_REVISION` tracks cumulative candidate corrections. `MASTER_INTEGRATION` alone increments `ARTICLE_MASTER_V00N` after approval. Approved masters may never be silently overwritten or reused for different content.

### 11. Journal policy

Target A is Knowledge-Based Systems; Plan B is Expert Systems with Applications; Plan C is Information Processing & Management. Drafting must preserve a common scientific core to minimize substantive rewriting on journal transfer. Research article is the current operational article type. Unverified KBS-specific template, exact length, free-format, mandatory-heading, final-reference-style, or submission-detail requirements must not be invented; the neutral reversible master and pre-submission revalidation govern.

### 12. Length discipline

Every candidate integration records English-main-text word count separately from references/tables/captions/declarations. Redundancy across prose/tables/figures is minimized. Necessary evidence or reproducibility content may not be sacrificed for an unverified limit.

### 13. Mandatory Writing-AI delivery checklist

Every delivery must declare `PROTOCOL_READ = MWDP_V1.0`, block/revision, source snapshots, authorized/conditional claims, zero prohibited claims, access-recheck state, citation-comment coverage, ES/EN equivalence, candidate master, English main-text word count, and experimental-review trigger. Missing fields are a delivery defect requiring correction before integration.

### 14. Amendments

The protocol is cumulative. New rules are added rather than silently replacing omitted earlier rules. Every amendment must identify the prior version, affected rules, rationale, impact, review, and author approval. Frozen rules change only through an explicit new protocol version, never through an isolated conversation or unrecorded block instruction.
