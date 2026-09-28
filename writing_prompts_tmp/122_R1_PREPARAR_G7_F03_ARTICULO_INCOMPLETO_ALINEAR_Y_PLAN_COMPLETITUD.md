# PROMPT122-R1 — G7-F03: ARTÍCULO INCOMPLETO — ALINEACIÓN CON TESIS FINAL Y PLAN DE COMPLETITUD

## 0. Estado y supersesión

Este prompt **supersede para ejecución** a:

```text
writing_prompts_tmp/122_PREPARAR_G7_F03_SINCRONIZAR_ARTICULO_CON_TESIS_FINAL.md
commit = 4e4423839d41841b3cdb14657a7306f5d84e1ea1
```

Motivo: se aclaró que `ARTICLE_MASTER_V026.md` **NO es un artículo terminado**. Es el master vigente de un artículo todavía en construcción. Por tanto, G7-F03 no debe tratarlo como manuscrito final pendiente solo de sincronización.

```text
ARTICLE_MASTER_V026_STATUS = WORK_IN_PROGRESS / NOT_FINAL
PROMPT122_ORIGINAL = SUPERSEDED_FOR_EXECUTION
PROMPT122_R1 = AUTHORIZED
```

---

## 1. Actor y gate

Actúa como **IA Gestora de Artículo** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No modifiques la tesis final. No ejecutes Grupo 8.

Lee íntegramente antes de actuar:

```text
writing_prompts_tmp/121N_AUDITORIA_EXTERNA_PASS.md
commit = be902fa0df0cc40ac9a5ad2cb8a040dc3ceeb9e6
```

Gate vinculante:

```text
G7_F02 = CLOSED / APPROVED / INTEGRATED
G7_F03_AUTHORIZED = true
ARTICLE_MASTER_V026_STATUS = WORK_IN_PROGRESS / NOT_FINAL
```

---

## 2. Entradas obligatorias

Debes disponer realmente de:

1. `ARTICLE_MASTER_V026.md`, entendido como **master vigente incompleto** del artículo.
2. `Molleapasa_gv_G7F02_FINAL_CLEAN.docx`

```text
SHA256 = e734e1b93e82e732d7db99eec9fd22334e67f9621dacfedc4a559ab90f785a85
SIZE = 3909601
```

3. `g7_thesis_claim_traceability_v0.3_FINAL.csv`

```text
SHA256 = 5596ea01f1a2b98373de151176f0799f54d5a1e859f60e30c3ecc26eaad32dec
SIZE = 127824
ROWS = 136
```

Si `ARTICLE_MASTER_V026.md` o la tesis final no están disponibles de forma efectiva, devuelve:

```text
PROMPT122_R1_EXECUTION = STOPPED_PRECONDITION
```

y no reconstruyas el artículo desde memoria ni desde resúmenes parciales.

---

## 3. Propósito exclusivo

Realiza un **preflight de G7-F03 sobre un artículo incompleto**. Este preflight tiene dos objetivos simultáneos y separados:

### A. ALINEACIÓN

Auditar únicamente las partes **ya escritas** de `ARTICLE_MASTER_V026.md` contra la tesis final aprobada, para detectar contenido desactualizado, contradictorio, demasiado fuerte o numéricamente inconsistente.

### B. COMPLETITUD

Determinar qué partes del artículo **faltan por escribir, están incompletas o permanecen como placeholders/esqueleto**, y producir un plan mínimo y secuenciado para terminar el artículo.

**No redactes todavía las secciones faltantes y no edites `ARTICLE_MASTER_V026.md` en este bloque.**

Este bloque no evalúa el artículo como si ya fuera final.

---

## 4. Ciencia vinculante

La tesis final aprobada gobierna cualquier contenido científico que ya aparezca o deba aparecer en el artículo.

Verifica, como mínimo:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACIÓN cuando corresponda
BENCHMARK = 1056 series / 67 DAM / 42 NANDINA / Capítulo 87 / offline
HISTORICAL_BANK = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
CURATED_TOTAL = 4106 series
NORMATIVE_HIERARCHICAL_DOCUMENTS = 7648

HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE
HG = NO_FORMAL_DISPOSITION_FOUND

HISTORICAL_TOP1 = 0.5095
HISTORICAL_TOP3 = 0.6714
HISTORICAL_TOP5 = 0.7633
HISTORICAL_TOP10 = 0.8911
HISTORICAL_TOP50 = 0.9915
HISTORICAL_MRR100 = 0.6297

INTEGRATION_RANKING_INVARIANT = 1056/1056
TRACE_HISTORICAL = 3168/3168
TRACE_NORMATIVE = 3168/3168

RERANKER_SAMPLE = 20
RERANKER_REFERENCE_IN_POOL = 19
RERANKER_REFERENCE_OUTSIDE_POOL = 1
RERANKER_TOP1_BEFORE_AFTER = 0.5000 / 0.5000
RERANKER_TOP3_BEFORE_AFTER = 0.6500 / 0.6500
RERANKER_TOP5_BEFORE_AFTER = 0.8000 / 0.8000
RERANKER_MRR_BEFORE_AFTER = 0.6326 / 0.6326
RERANKER_POSITIVE_NOCHANGE_NEGATIVE = 0 / 19 / 0

HE4_TOP3_ORDER_PRESERVED = 50/50
HE4_TRACEABILITY_COMPLETE = 50/50
HE4_GENERIC_NORM_WARNING_CONFORMANT = 41/50
HE4_GENERIC_NORM_WARNING_MISSING = 9/50
HE4_AUDITABLE = 28/50
HE4_NON_AUDITABLE = 22/50
HE4_SEVERE_VIOLATIONS = 0/50
HE4_EVALUATOR = independent AI under expert role
HE4_HUMAN_SCORING = none
```

Guardrails vinculantes:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_OR_LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
EXP11A != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B != SEED_SUPERPOPULATION_INFERENCE
ATTEMPT06 != GLOBAL_ZERO_IMPACT
```

EXP12 permanece cerrado sin recuperación y su efecto de diversidad es no estimable. No reabrirlo.

---

## 5. Auditoría de ALINEACIÓN de lo ya escrito

Para cada parte ya redactada del artículo revisa, cuando exista:

1. título provisional y alcance;
2. resumen/abstract;
3. palabras clave;
4. introducción;
5. objetivo o pregunta del artículo;
6. arquitectura funcional;
7. datos, particiones y unidad de análisis;
8. métodos de recuperación;
9. inferencia HE2;
10. integración histórica–normativa;
11. reranker diagnóstico;
12. explicación y auditabilidad HE4;
13. HE5, errores, sensibilidades y límites;
14. resultados;
15. discusión;
16. conclusiones;
17. figuras y tablas ya incluidas;
18. referencias cruzadas y cifras;
19. afirmaciones que hayan quedado superseded por la tesis final.

Para cada hallazgo usa:

```text
ARTICLE_SYNC_ID
ARTICLE_LOCATION
THESIS_GOVERNING_LOCATION
CURRENT_ARTICLE_TEXT_OR_CLAIM
FINAL_THESIS_STATE
DISPOSITION = KEEP | UPDATE_REQUIRED | DELETE_REQUIRED | VERIFY_ONLY
SEVERITY = CRITICAL | MAJOR | MINOR | NONE
SCIENTIFIC_REASON
PROPOSED_MINIMAL_ACTION
```

No conviertas diferencias puramente editoriales en defectos científicos.

---

## 6. Auditoría de COMPLETITUD del artículo

Reconstruye la estructura real existente de `ARTICLE_MASTER_V026.md` y clasifica cada componente como:

```text
COMPLETE_CURRENT
PARTIAL
PLACEHOLDER
MISSING
NOT_APPLICABLE
```

Para cada componente registra:

```text
ARTICLE_COMPLETENESS_ID
SECTION_OR_COMPONENT
CURRENT_STATUS
WHAT_EXISTS_NOW
WHAT_IS_STILL_MISSING
THESIS_SOURCE_AVAILABLE = true|false
ADDITIONAL_SOURCE_REQUIRED = true|false
CAN_BE_COMPLETED_WITH_FROZEN_SOURCES = true|false
DEPENDENCY
PROPOSED_FUTURE_BLOCK
```

Como mínimo evalúa:

- título;
- resumen/abstract;
- palabras clave;
- introducción;
- antecedentes/estado del arte si el diseño del artículo los requiere;
- método;
- resultados;
- discusión;
- conclusiones;
- limitaciones;
- figuras;
- tablas;
- referencias;
- material suplementario si estuviera previsto;
- requisitos editoriales del journal si ya están congelados en el flujo del artículo.

No inventes una estructura de revista si todavía no existe una especificación aprobada.

---

## 7. Plan futuro de terminación

Con base en Alineación + Completitud, propone la secuencia mínima de bloques futuros de G7-F03.

La secuencia debe separar, cuando corresponda:

1. corrección de contenido ya escrito desactualizado;
2. redacción de secciones faltantes;
3. integración de figuras/tablas;
4. revisión de coherencia interna;
5. ajuste a requisitos editoriales ya aprobados;
6. auditoría final del artículo.

No asignes automáticamente un número fijo de bloques si la evidencia del master no lo permite. Sí debes estimar cuántos bloques serían necesarios y justificar el alcance de cada uno.

---

## 8. Prohibiciones

No:

- edites `ARTICLE_MASTER_V026.md`;
- redactes secciones faltantes todavía;
- modifiques la tesis final;
- uses búsqueda web;
- añadas bibliografía nueva;
- inventes resultados, métricas o inferencias;
- reabras EXP12;
- conviertas HE1 o HG en una disposición terminal;
- presentes HE4 como evaluación humana;
- equipares auditabilidad con corrección jurídica;
- ejecutes Grupo 8;
- declares el artículo completo o aprobado.

---

## 9. Salida obligatoria

Publica exclusivamente:

```text
writing_prompts_tmp/122_R1_RESPUESTA_G7_F03_PREFLIGHT_ARTICULO_INCOMPLETO.md
```

Debe contener, como mínimo:

```text
PROMPT122_R1_EXECUTION = COMPLETE | STOPPED_PRECONDITION | REVISION_REQUIRED
ARTICLE_MASTER_INPUT = ARTICLE_MASTER_V026.md
ARTICLE_MASTER_STATUS = WORK_IN_PROGRESS / NOT_FINAL
THESIS_FINAL_IDENTITY_MATCH = true|false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false

ALIGNMENT_ITEMS_TOTAL = <n>
ALIGNMENT_CRITICAL = <n>
ALIGNMENT_MAJOR = <n>
ALIGNMENT_MINOR = <n>
ALIGNMENT_KEEP = <n>

COMPLETENESS_COMPONENTS_TOTAL = <n>
COMPLETE_CURRENT = <n>
PARTIAL = <n>
PLACEHOLDER = <n>
MISSING = <n>

ESTIMATED_FUTURE_G7_F03_BLOCKS = <n or justified range>
ARTICLE_READY_FOR_FINAL_AUDIT = false
NEW_REFERENCES = 0
WEB_SEARCH_USED = false
GROUP8_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Incluye:

1. matriz completa de alineación;
2. matriz completa de completitud;
3. secuencia propuesta de bloques futuros para terminar el artículo;
4. bloqueadores reales, si existen.

---

## 10. Parada obligatoria

Al finalizar, detente para auditoría externa.

No modifiques el artículo y no ejecutes ningún bloque posterior.
