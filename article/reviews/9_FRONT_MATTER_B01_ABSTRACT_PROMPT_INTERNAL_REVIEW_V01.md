# Internal review — Front matter B01 / Abstract prompt V01

## Español

```text
REVIEW_TYPE = PROMPT_INTERNAL_REVIEW
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B01_ABSTRACT
PROMPT = article/prompts/9_FRONT_MATTER_B01_ABSTRACT_V01.md
PROMPT_COMMIT = e26a35a7caf26c6118c3efc6c0239c2a8a1f9905
PROMPT_GIT_BLOB = 508c2d06dd94f18470b1835771d3201b3e9c4e83
BOUNDARY = D-160
CANONICAL_MASTER = ARTICLE_MASTER_V031
VERDICT = PASS
MANDATORY_CORRECTIONS = NONE
READY_FOR_EXECUTION_AUTHORIZATION = YES
```

### Revisión de alcance

El prompt limita la ejecución al Abstract final EN/ES. Title/Título, Keywords/Palabras clave, Sections 1–7 y todo el end matter quedan expresamente preservados. Los baselines están fijados por identidad exacta a V031 y al Word acumulativo de Conclusion aprobado. Se prohíbe reconstruir el DOCX desde Markdown y se conservan 48 comentarios y 0 tracked changes como invariantes técnicas.

### Revisión científica

El prompt reproduce correctamente D-160 y la secuencia KBS observada:

```text
PROBLEM_AND_LIMITATION
-> PROPOSAL_AND_AUTHORITY_BOUNDARIES
-> EVALUATION_AND_MAIN_EVIDENCE
-> BOUNDED_INTERPRETATION
```

El Abstract debe ser autosuficiente sin conocimiento previo de NANDINA y distingue correctamente:

- historical retrieval como única autoridad primaria de ranking;
- fixed Top-3 antes de documentary association y generation;
- documentary association como evidencia sin reranking;
- local LLM restringido a controlled explanation;
- evaluación separada de candidate retrieval, documentary association y explanation.

Las cifras permitidas proceden únicamente de Results/Conclusion ya integrados. La priorización evita saturar el Abstract: Top-3 histórico como métrica primaria, Top-1/MRR opcionales, asociación/invariancia documental y el criterio cualitativo 28/50 como evidencia central. Se excluyen intervalos, p-values, comparadores, sensibilidades detalladas, métricas secundarias e IDs internos.

El prompt conserva las fronteras:

```text
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
LLM_AS_JUDGE != HUMAN_EXPERT_VALIDATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
REINSTANTIATION != DEPLOYMENT_READINESS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No permite literatura, búsqueda externa, citas, resultados, cálculos o inferencia nuevos.

### Revisión editorial / D-136 / KBS

El objetivo aproximado de 200–250 palabras inglesas es consistente con la estructura canónica y con la guía empírica KBS. El prompt exige un Abstract reader-facing, preferentemente de un solo párrafo, con problema inmediato, limitación concreta, mecanismo de la propuesta, evaluación/evidencia e interpretación delimitada. Se evita `H100` y otros códigos internos cuando exista una formulación científica pública equivalente.

No se permite lenguaje promocional, novelty, first, SOTA, superiority, legal correctness, human validation, deployment readiness ni external generalization.

### Revisión bilingüe y técnica

Se exige espejo semántico natural EN/ES, edición directa del Word acumulativo, auditoría diferencial OOXML, render completo, preservación de comentarios y detención antes de Title, Keywords o end matter. D-022, D-027, D-035, MWDP, SPCCR, KBS EWG y D-136 permanecen vinculantes.

```text
SCIENTIFIC_SCOPE = PASS
ANTI_OVERCLAIMING = PASS
NO_NEW_EVIDENCE = PASS
ABSTRACT_SELF_CONTAINED_REQUIREMENT = PASS
METRIC_ECONOMY = PASS
INTERNAL_TERMINOLOGY_CONTROL = PASS
KBS_EDITORIAL_FIT = PASS
BILINGUAL_CONTROL = PASS
DOCX_CONTROL = PASS
EXIT_GATE = PASS
VERDICT = PASS
MANDATORY_CORRECTIONS = NONE
```

---

## English

The Front Matter B01 Abstract V01 prompt passes internal review. It is strictly limited to the English Abstract and semantically equivalent Spanish mirror, preserves Title, Keywords, Sections 1–7 and end matter, uses exact V031/Word baselines, and follows the KBS-style sequence of problem/limitation, proposal with authority separation, evaluation/main evidence, and bounded interpretation. It permits only essential already integrated figures, introduces no citations or new claims, and preserves all established epistemic boundaries. No mandatory prompt corrections are required.
