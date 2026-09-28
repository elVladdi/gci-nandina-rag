# D-156 — Conclusion §7 interpretive boundary

## Español

```text
DECISION = D-156
PHASE = CONCLUSION
BLOCK = CONCLUSION_B01_SECTION_7
CANONICAL_MASTER = ARTICLE_MASTER_V030
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V030.md
CANONICAL_MASTER_MD_SHA256 = ba4d3d5021a6be5fc43a435c3618c65e0778b900609b708014cb04d7866b9b7d
CANONICAL_MASTER_MD_GIT_BLOB = 2683f5933205219ed62e16418d3f9a0ace7460bd
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_TRANSVERSAL_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 340e283924a9364447344469cf4eb077bbf93f7d32509f8f173d0a01fb3bbc0f
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0
CANONICAL_DOCX_PAGE_COUNT = 69
PRIMARY_INPUTS = INTRODUCTION; RESULTS_5_1_TO_5_7; DISCUSSION_6_1_TO_6_6; ARCHITECTURE_3_1_TO_3_7; METHODS_SCOPE_4_1_4_7_4_8
NEW_LITERATURE = PROHIBITED
NEW_CITATIONS = PROHIBITED
NEW_RESULTS = PROHIBITED
NEW_CALCULATIONS = PROHIBITED
NEW_INFERENCE = PROHIBITED
FINAL_GAP = NOT_DEFINED
NOVELTY_CLAIM = PROHIBITED
SOTA_OR_SUPERIORITY_CLAIM = PROHIBITED
EXTERNAL_GENERALIZATION = PROHIBITED
LEGAL_CORRECTNESS = PROHIBITED
DEPLOYMENT_READINESS = PROHIBITED
HUMAN_EXPERT_VALIDATION = PROHIBITED
CONCLUSION_FUNCTION = CONTRIBUTION -> MAIN_EVIDENCE -> SCOPE -> BOUNDED_IMPLICATION
```

### Objeto científico

Conclusion debe cerrar el artículo sin reabrir la argumentación ni introducir evidencia nueva. Su función es sintetizar: (1) qué arquitectura/metodología se estudió; (2) qué evidencia principal quedó establecida; (3) bajo qué límites debe interpretarse; y (4) qué implicación acotada se deriva para sistemas de apoyo a decisiones auditables.

### Contenido autorizado

La síntesis puede afirmar, en lenguaje reader-facing, que:

1. el framework separa autoridad entre recuperación histórica, asociación documental y explicación controlada; la recuperación histórica fija candidatos y Top-3 antes de las etapas posteriores;
2. la evaluación trató candidate retrieval, documentary association y controlled explanation como objetos distintos;
3. en el benchmark Chapter-87/NANDINA-8, historical BM25 H100 obtuvo Top-1 50.95%, Top-3 67.14% y MRR@100 0.6297; estas son métricas de candidate retrieval, no overall classification accuracy;
4. la asociación documental exacta estuvo disponible en 3,168/3,168 slots y preservó membresía/orden del Top-3 en 1,056/1,056 casos; esto demuestra cobertura/asociación/trazabilidad/ranking invariance dentro del corpus evaluado, no substantive normative or legal correctness;
5. en 50 casos de explicación, Top-3 y orden se preservaron en 50/50 y 28/50 (56.0%) cumplieron el criterio cualitativo de auditabilidad; la evaluación cualitativa fue LLM-as-judge, no human expert validation;
6. las comparaciones inferenciales de candidate retrieval apoyan HE2 solo dentro del alcance interno congelado y no deben convertirse en superioridad global del framework;
7. configurabilidad e interfaces documentadas permiten re-instanciación condicional, pero no transfieren desempeño ni establecen external validity;
8. las limitaciones principales incluyen colección administrativa purposiva, Chapter 87, dependencia intra-DAM y similitud residual, sensibilidad del banco histórico, objetos no estimables, drift documental Decision 885/906, evaluación cualitativa limitada y LLM-as-judge, ausencia de validación operativa/legal/humana y estado todavía incompleto del paquete público de reproducción de referencia.

### Síntesis preferida

El cierre debe priorizar el argumento central y no convertirse en una segunda sección Results. Se recomienda 3–4 párrafos en inglés, aproximadamente 300–400 palabras, con espejo semántico natural en español:

1. contribución/metodología: separación explícita de autoridad y evaluación por función;
2. evidencia principal: candidate retrieval + association/ranking invariance + explicación estructural/auditabilidad, con solo las cifras indispensables;
3. alcance/limitaciones: benchmark offline Chapter 87, dependencia y generalización, corpus/LLM/reproducibilidad;
4. implicación acotada: la separación de autoridad y provenance puede apoyar revisión auditable, pero cada nueva instancia requiere validación propia y no sustituye adjudicación experta/legal.

### Prohibiciones

No introducir literatura ni citas nuevas; no declarar `first`, `novel`, `state of the art`, `superior`, `best`, `validated for deployment`, `legally correct`, `human validated`, `generalizable`, `robust across jurisdictions` ni equivalentes. No convertir documentary association en correctness, auditability en legal correctness, configurability en empirical generalization, ni Top-k retrieval en overall classification accuracy. No mencionar IDs internos de experimentos, decisiones, gates, hashes, commits, usernames, códigos de QA o nombres internos de campos.

Conclusion no debe definir FINAL_GAP ni novelty. Tampoco debe corregir, resumir de nuevo o modificar otras secciones.

### Gate

```text
CURRENT_GATE = CONCLUSION_B01_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = CREATE_REVIEW_AND_AUTHORIZE_CONCLUSION_B01_PROMPT
EXPECTED_POST_EXECUTION_STATE = CONCLUSION_B01_V01_COMPLETED_PENDING_GESTORA_AUDIT
FRONT_MATTER_FINALIZATION = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

D-156 defines the bounded scientific role of Section 7. Conclusion must synthesize the already approved contribution, main evidence, scope, and implication without introducing literature, citations, results, calculations, inference, novelty, superiority, external generalization, legal correctness, deployment readiness, or human-validation claims. It must keep candidate retrieval, documentary association, and controlled explanation as distinct evaluated objects and preserve all validity limits established in Results and Discussion.