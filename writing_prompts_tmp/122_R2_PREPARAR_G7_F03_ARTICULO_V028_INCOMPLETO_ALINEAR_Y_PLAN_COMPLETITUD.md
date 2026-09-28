# PROMPT122-R2 — G7-F03: ARTICLE_MASTER_V028 INCOMPLETO — ALINEACIÓN CON TESIS FINAL Y PLAN DE COMPLETITUD

## 0. Estado y supersesión

Este prompt supersede para ejecución a los prompts 122 anteriores:

```text
writing_prompts_tmp/122_PREPARAR_G7_F03_SINCRONIZAR_ARTICULO_CON_TESIS_FINAL.md
commit = 4e4423839d41841b3cdb14657a7306f5d84e1ea1

writing_prompts_tmp/122_R1_PREPARAR_G7_F03_ARTICULO_INCOMPLETO_ALINEAR_Y_PLAN_COMPLETITUD.md
commit = b9044dd44f368c33d6121c452ad9fe9b40a0e08d
```

Motivo de la corrección: la última versión aprobada y gobernante del artículo NO es `ARTICLE_MASTER_V026.md`. Es `ARTICLE_MASTER_V028.md`, ubicada en la rama y ruta del flujo del artículo indicadas abajo. Además, V028 sigue siendo un artículo en construcción, no un manuscrito final.

```text
ARTICLE_MASTER_GOVERNING_VERSION = ARTICLE_MASTER_V028.md
ARTICLE_MASTER_V028_STATUS = WORK_IN_PROGRESS / NOT_FINAL
PROMPT122_ORIGINAL = SUPERSEDED_FOR_EXECUTION
PROMPT122_R1 = SUPERSEDED_FOR_EXECUTION
PROMPT122_R2 = AUTHORIZED
```

No uses V026 ni V027 como base de trabajo salvo para historia de versiones si fuera estrictamente necesario para explicar un cambio. V028 gobierna el preflight.

---

## 1. Actor y gate

Actúa como **IA Gestora de Artículo** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No modifiques la tesis final. No ejecutes Grupo 8. No redactes todavía una nueva versión del artículo.

Lee íntegramente antes de actuar:

```text
writing_prompts_tmp/121N_AUDITORIA_EXTERNA_PASS.md
commit = be902fa0df0cc40ac9a5ad2cb8a040dc3ceeb9e6
```

Gate vinculante:

```text
G7_F02 = CLOSED / APPROVED / INTEGRATED
G7_F03_AUTHORIZED = true
ARTICLE_MASTER_GOVERNING_VERSION = ARTICLE_MASTER_V028.md
ARTICLE_MASTER_V028_STATUS = WORK_IN_PROGRESS / NOT_FINAL
```

---

## 2. Entrada gobernante del artículo — identidad exacta

La fuente gobernante del artículo para este bloque está en:

```text
repository = elVladdi/gci-nandina-rag
branch = article/main-manuscript
source_commit = 235893711cedca743a506f4f5da8f779268b8ed0
path = article/manuscript/ARTICLE_MASTER_V028.md
blob_sha = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
size = 258157 bytes
```

Debes leer `ARTICLE_MASTER_V028.md` completo desde esa identidad exacta. No uses `ARTICLE_MASTER_V026.md` como entrada.

V028 declara explícitamente que es una base editable acumulativa para versiones posteriores y que no constituye un manuscrito terminado. En particular, contiene componentes aún pendientes como título final, abstract y keywords, además de instrucciones editoriales de trabajo que deberán desaparecer de la versión de envío.

Si el archivo en el commit exacto no coincide con el blob indicado, devuelve `STOPPED_PRECONDITION` y no continúes.

---

## 3. Entradas gobernantes de tesis

Debes disponer también de la tesis final limpia aprobada y de su trazabilidad final:

```text
Molleapasa_gv_G7F02_FINAL_CLEAN.docx
SHA256 = e734e1b93e82e732d7db99eec9fd22334e67f9621dacfedc4a559ab90f785a85
SIZE = 3909601

g7_thesis_claim_traceability_v0.3_FINAL.csv
SHA256 = 5596ea01f1a2b98373de151176f0799f54d5a1e859f60e30c3ecc26eaad32dec
SIZE = 127824
ROWS = 136
```

Si no puedes acceder efectivamente a la tesis final limpia, devuelve:

```text
PROMPT122_R2_EXECUTION = STOPPED_PRECONDITION
```

y no reconstruyas la tesis desde memoria ni desde resúmenes parciales.

---

## 4. Propósito exclusivo

Realiza un **preflight de G7-F03 sobre `ARTICLE_MASTER_V028.md` como artículo incompleto**. Este preflight tiene dos objetivos separados y complementarios:

### A. ALINEACIÓN CIENTÍFICA

Audita únicamente las partes ya escritas de V028 contra la tesis final aprobada para detectar:

- contenido desactualizado;
- contradicciones con la tesis final;
- cifras o denominadores obsoletos;
- lenguaje demasiado fuerte;
- alcance no soportado;
- atribución incorrecta de función a un componente;
- referencias internas a resultados, figuras o tablas que hayan quedado superseded;
- cualquier afirmación que exceda los guardrails congelados.

### B. COMPLETITUD DEL MANUSCRITO

Determina qué partes de V028:

```text
COMPLETE_CURRENT
PARTIAL
PLACEHOLDER
MISSING
NOT_APPLICABLE
```

No confundas "estructura definida" con "sección científicamente redactada".

**No edites `ARTICLE_MASTER_V028.md` en este bloque. No redactes todavía las secciones faltantes.**

---

## 5. Ciencia vinculante mínima

La tesis final aprobada gobierna cualquier contenido científico ya escrito o futuro del artículo. Contrasta como mínimo:

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

## 6. Auditoría de ALINEACIÓN de lo ya escrito

Lee V028 completa y revisa, cuando exista contenido redactado:

1. título provisional o instrucciones de título;
2. abstract/resumen;
3. keywords;
4. Introduction;
5. Research Questions / objetivo;
6. Related work;
7. Decision-support architecture;
8. Experimental design;
9. datasets, particiones, unidad de análisis y dependencia;
10. recuperación histórica;
11. recuperación normativa;
12. integración histórica–normativa;
13. reranker diagnóstico;
14. explicación/auditabilidad HE4;
15. HE5, sensibilidades y límites;
16. Results;
17. Discussion;
18. Conclusion;
19. figuras y tablas previstas o incorporadas;
20. referencias cruzadas y cifras;
21. end matter y reproducibilidad cuando ya exista contenido científico;
22. cualquier afirmación superseded por la tesis final.

Para cada hallazgo usa exactamente:

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

No conviertas diferencias editoriales inocuas en defectos científicos.

---

## 7. Auditoría de COMPLETITUD de V028

Reconstruye la estructura real existente de V028 y clasifica cada componente como:

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
ADDITIONAL_FROZEN_SOURCE_REQUIRED = true|false
CAN_BE_COMPLETED_WITH_CURRENT_GOVERNING_SOURCES = true|false
DEPENDENCY
PROPOSED_FUTURE_BLOCK
```

Como mínimo evalúa:

- Title;
- Abstract;
- Keywords;
- 1. Introduction;
- 2. Related work;
- 3. Decision-support architecture;
- 4. Experimental design;
- 5. Results;
- 6. Discussion;
- 7. Conclusion;
- figuras;
- tablas;
- referencias;
- Data availability;
- reproducibility resources;
- CRediT;
- funding;
- competing interests;
- acknowledgements;
- supplementary material si estuviera previsto.

Distingue explícitamente entre:

- texto científico ya redactado;
- notas/instrucciones de drafting;
- placeholders;
- estructura prevista sin prosa;
- elementos finales que solo pueden cerrarse al terminar el manuscrito (por ejemplo, título/abstract/keywords si así lo ordena V028).

---

## 8. Fuentes editoriales del propio flujo del artículo

Respeta la arquitectura editorial ya congelada en V028:

```text
Target journal = Knowledge-Based Systems
Article type = Research article
Editorial basis = KBS empirical writing guide based on 34 recent Open Access articles
Working structure = KBS_ARTICLE_WORKING_STRUCTURE_V02
```

No realices nueva búsqueda web ni reconstruyas requisitos de KBS desde fuentes externas en este bloque. Si existe otra fuente gobernante ya versionada en la rama del artículo, puedes identificarla y citarla como dependencia, pero no debes sustituir V028 por una versión anterior.

---

## 9. Plan futuro de terminación de G7-F03

Con base en Alineación + Completitud, propone la secuencia mínima de bloques futuros para terminar el artículo.

La secuencia debe separar, cuando corresponda:

1. corrección de contenido ya escrito que esté desactualizado;
2. redacción de secciones parciales o faltantes;
3. integración y cierre de figuras/tablas;
4. cierre de Results/Discussion/Conclusion;
5. cierre de Title/Abstract/Keywords cuando corresponda según V028;
6. end matter y referencias;
7. coherencia científica y editorial global;
8. auditoría final del artículo.

No asignes un número fijo de bloques sin evidencia. Sí debes estimar cuántos bloques futuros son necesarios y justificar el alcance de cada uno.

---

## 10. Prohibiciones

No:

- uses `ARTICLE_MASTER_V026.md` como fuente gobernante;
- edites `ARTICLE_MASTER_V028.md`;
- redactes secciones faltantes todavía;
- modifiques la tesis final;
- uses búsqueda web;
- añadas bibliografía nueva;
- inventes resultados, métricas o inferencias;
- reabras EXP12;
- conviertas HE1 o HG en disposición terminal;
- presentes HE4 como evaluación humana;
- equipares auditabilidad con corrección jurídica;
- ejecutes Grupo 8;
- declares el artículo completo o aprobado.

---

## 11. Salida obligatoria

Publica exclusivamente:

```text
writing_prompts_tmp/122_R2_RESPUESTA_G7_F03_PREFLIGHT_ARTICLE_MASTER_V028.md
```

Debe contener, como mínimo:

```text
PROMPT122_R2_EXECUTION = COMPLETE | STOPPED_PRECONDITION | REVISION_REQUIRED
ARTICLE_MASTER_INPUT = article/manuscript/ARTICLE_MASTER_V028.md
ARTICLE_SOURCE_BRANCH = article/main-manuscript
ARTICLE_SOURCE_COMMIT = 235893711cedca743a506f4f5da8f779268b8ed0
ARTICLE_MASTER_BLOB_SHA = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
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
4. bloqueadores reales, si existen;
5. confirmación explícita de que V028 —y no V026— fue la entrada gobernante.

---

## 12. Parada obligatoria

Al finalizar, detente para auditoría externa.

No modifiques el artículo y no ejecutes ningún bloque posterior.
