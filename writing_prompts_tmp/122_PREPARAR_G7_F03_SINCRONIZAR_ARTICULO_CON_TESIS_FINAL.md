# PROMPT122 — G7-F03: preflight de sincronización del artículo con la tesis final aprobada

## 0. Actor y gate

Actúa como **IA Gestora de Artículo / IA de Redacción Científica del artículo** del proyecto `elVladdi/gci-nandina-rag`.

Este prompt abre G7-F03 únicamente después del cierre externo de G7-F02.

Lee íntegramente antes de actuar:

```text
writing_prompts_tmp/121N_AUDITORIA_EXTERNA_PASS.md
commit = be902fa0df0cc40ac9a5ad2cb8a040dc3ceeb9e6
```

Gate vinculante:

```text
G7_F02 = CLOSED / APPROVED / INTEGRATED
G7_F03_AUTHORIZED = true
```

No eres CODEX. No modifiques la tesis final. No ejecutes Grupo 8.

---

## 1. Entradas obligatorias

Debes disponer de:

1. `ARTICLE_MASTER_V026.md`, aprobado en el flujo de gestión del artículo.
2. La tesis final limpia aprobada:

```text
Molleapasa_gv_G7F02_FINAL_CLEAN.docx
SHA256 = e734e1b93e82e732d7db99eec9fd22334e67f9621dacfedc4a559ab90f785a85
SIZE = 3909601
```

3. La trazabilidad final de tesis:

```text
g7_thesis_claim_traceability_v0.3_FINAL.csv
SHA256 = 5596ea01f1a2b98373de151176f0799f54d5a1e859f60e30c3ecc26eaad32dec
SIZE = 127824
ROWS = 136
```

Si `ARTICLE_MASTER_V026.md` o la tesis final limpia no están disponibles, devuelve `STOPPED_PRECONDITION` y no inventes contenido ni reconstruyas el artículo desde memoria.

---

## 2. Propósito EXCLUSIVO

Realiza un **preflight de sincronización**, no una reescritura del artículo.

Compara `ARTICLE_MASTER_V026.md` contra la tesis final aprobada y determina qué elementos del artículo requieren actualización para quedar científicamente alineados con el estado final de G7-F02.

No edites todavía `ARTICLE_MASTER_V026.md`.

---

## 3. Ciencia vinculante a contrastar

La tesis final aprobada gobierna el estado científico. Verifica como mínimo:

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

Guardrails:

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

## 4. Ámbitos de comparación obligatorios

Audita `ARTICLE_MASTER_V026.md` contra la tesis final en, al menos:

1. título y alcance;
2. problema/pregunta u objetivo del artículo;
3. arquitectura funcional y rol de cada componente;
4. datos, particiones, unidad de análisis y dependencia;
5. metodología e inferencia de HE2;
6. recuperación normativa;
7. recuperación histórica;
8. integración histórica–normativa;
9. reranker diagnóstico;
10. explicación/auditabilidad HE4;
11. HE5 y sensibilidades;
12. discusión y límites;
13. conclusiones;
14. figuras y tablas del artículo;
15. referencias cruzadas a cifras o resultados;
16. cualquier afirmación que pueda haber quedado superseded por la tesis final.

No conviertas diferencias editoriales inocuas en cambios científicos obligatorios.

---

## 5. Clasificación de hallazgos

Para cada diferencia registra:

```text
ARTICLE_SYNC_ID
ARTICLE_LOCATION
THESIS_GOVERNING_LOCATION
CURRENT_ARTICLE_CLAIM
FINAL_THESIS_STATE
DISPOSITION = KEEP | UPDATE_REQUIRED | DELETE_REQUIRED | VERIFY_ONLY
SEVERITY = CRITICAL | MAJOR | MINOR | NONE
SCIENTIFIC_REASON
PROPOSED_MINIMAL_ACTION
```

Distingue explícitamente:

- contradicción científica;
- cifra desactualizada;
- lenguaje demasiado fuerte;
- desalineación de alcance;
- referencia/figura/tabla obsoleta;
- diferencia puramente editorial sin efecto científico.

---

## 6. Prohibiciones

No:

- modifiques todavía el artículo;
- modifiques la tesis final;
- busques nueva bibliografía en web;
- añadas referencias nuevas;
- inventes resultados o inferencias;
- reabras EXP12;
- transformes resultados descriptivos en confirmatorios;
- conviertas HE1 o HG en una disposición terminal;
- presentes evaluación HE4 como puntuación humana;
- equipares auditabilidad con corrección jurídica;
- ejecutes Grupo 8.

---

## 7. Salida obligatoria

Publica exclusivamente un plan de sincronización en:

```text
writing_prompts_tmp/122_RESPUESTA_PREPARAR_G7_F03_SINCRONIZAR_ARTICULO_CON_TESIS_FINAL.md
```

Debe incluir:

```text
PROMPT122_EXECUTION = COMPLETE | STOPPED_PRECONDITION | REVISION_REQUIRED
ARTICLE_MASTER_INPUT = ARTICLE_MASTER_V026.md
THESIS_FINAL_IDENTITY_MATCH = true|false
ARTICLE_SYNC_ITEMS_TOTAL = <n>
CRITICAL_ITEMS = <n>
MAJOR_ITEMS = <n>
MINOR_ITEMS = <n>
KEEP_ITEMS = <n>
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
NEW_REFERENCES = 0
WEB_SEARCH_USED = false
GROUP8_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Incluye la matriz completa de hallazgos y propone la secuencia mínima de edición futura, pero no la ejecutes.

---

## 8. Parada obligatoria

Al finalizar, detente para auditoría externa.

No ejecutes la modificación del artículo ni ningún bloque posterior.
