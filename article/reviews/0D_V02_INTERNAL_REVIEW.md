# Revisión interna 0D V02 / 0D V02 Internal Review

## Español

### 1. Dictamen

```text
0D_V02_INTERNAL_REVIEW = PASS
MATERIAL_ERRORS = 0
MINOR_CORRECTIONS_REQUIRED = 0
0D_M01 = CLOSED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE_0D = NOT_AUTHORIZED_YET
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

La IA Gestora / Editor Científico Principal auditó la entrega correctiva:

`article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`

commit:

`f788f8718ff312b86140c68d875a71f4bd463aaa`.

La integridad del commit fue verificada contra el estado inmediatamente anterior `6e88b5a9ae75af54614a3f91ee6e1b1687971ef2`: existe exactamente un commit adicional y un único archivo añadido, con 808 líneas. No se modificaron archivos de gobernanza, freezes, resultados experimentales ni el Plan Maestro.

### 2. Verificación de 0D-M01

La única corrección exigida por `article/reviews/0D_INTERNAL_REVIEW.md` fue aplicada correctamente en español e inglés.

En la función científica de Fig. 1 quedó:

- ES: `separación arquitectónica/funcional`;
- EN: `architectural/functional separation`.

En la mitigación del riesgo `B vs KBS expectations` quedó:

- ES: `hacer explícitas la separación arquitectónica/funcional y la función diferenciada de cada evaluación`;
- EN: `make the architectural/functional separation and the differentiated role of each evaluation explicit`.

No quedan las formulaciones `separación causal`, `causal/functional` o `causal separation` en los contextos corregidos. La normalización elimina la posible lectura causal y preserva el significado autorizado: aislamiento arquitectónico/funcional e invariantes de flujo.

```text
0D_M01 = CLOSED
```

### 3. Preservación de V01

La V02 preserva materialmente las decisiones y conclusiones de V01:

```text
PRIMARY_TARGET = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

También permanecen sin cambio material:

- la arquitectura IMRaD candidata y el orden de subsecciones;
- el mapa de figuras y tablas y sus dependencias;
- la matriz de redactabilidad;
- las cifras experimentales congeladas consumidas por 0D;
- RQ1–RQ4 y sus estados;
- `RQ4 = RETAINED_CONDITIONAL_ON_GROUP3`;
- `C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE`;
- Grupo 3 como dependencia para RQ4 y el cierre inferencial de HE2/HE5;
- la evaluación comparativa de los seis journals;
- el ranking KBS → ESWA → IPM;
- los riesgos y mitigaciones, salvo la normalización terminológica ordenada;
- la restricción `JOURNAL_FIT ≠ NOVELTY_PROOF`;
- la prohibición de redactar el manuscrito antes del cierre formal de Fase 0.

No se identifica expansión no autorizada del alcance ni nueva interpretación experimental.

### 4. Decisión editorial sobre journal fit

Se ratifica la recomendación de V01/V02 para el gate del autor:

```text
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
```

Esta es todavía una **recomendación editorial**, no una selección definitiva. La selección requiere aprobación expresa del autor dentro del freeze de 0D.

La razón principal se mantiene: KBS ofrece el mejor ajuste al posicionamiento arquitectónico-metodológico congelado en 0C, siempre que el artículo formule su aporte al nivel del contrato funcional completo evaluado y no como novelty de BM25, Top-k, evidencia normativa, RAG, LLM o auditabilidad por separado.

### 5. Gate de Fase 0

Se mantiene:

```text
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
```

La corrección 0D-M01 ya está cerrada. `PASS_WITH_CORRECTIONS` permanece porque existen dependencias posteriores que no impiden cerrar 0D ni comenzar bloques redactables, pero sí restringen el contenido final del artículo:

1. `C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE`;
2. Grupo 3 debe cerrarse antes de responder definitivamente RQ4 y cerrar inferencialmente HE2/HE5;
3. `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` deben preservarse hasta el gate editorial posterior que corresponda;
4. los requisitos exactos del Guide for Authors del target aprobado deben revalidarse antes de submission.

Si el autor aprueba este gate, podrán abrirse los bloques del plan declarados redactables, comenzando por Methods conforme a D-003, sin levantar los bloqueos anteriores.

### 6. Revisión experimental

La V02 no introduce evidencia experimental nueva ni reinterpretación de resultados. Solo corrige terminología epistemológica y conserva los límites ya gobernados.

```text
EXPERIMENTAL_REVIEW = NOT_REQUIRED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### 7. Estado editorial resultante

```text
0D = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
0D_V02_INTERNAL_REVIEW = PASS
0D_M01 = CLOSED
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = PENDING
FREEZE_0D = NOT_AUTHORIZED_YET
PHASE_1 = BLOCKED_UNTIL_0D_AND_PHASE_0_CLOSE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

No se requiere otro retorno a la IA de Redacción.

---

## English

### 1. Verdict

```text
0D_V02_INTERNAL_REVIEW = PASS
MATERIAL_ERRORS = 0
MINOR_CORRECTIONS_REQUIRED = 0
0D_M01 = CLOSED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE_0D = NOT_AUTHORIZED_YET
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

The Managing AI / Lead Scientific Editor audited `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md` at commit `f788f8718ff312b86140c68d875a71f4bd463aaa`. Commit integrity against the immediately preceding state `6e88b5a9ae75af54614a3f91ee6e1b1687971ef2` is correct: exactly one additional commit and one added 808-line file, with no governance, freeze, experimental-result, or Master-Plan modifications.

### 2. 0D-M01 verification

The sole required correction was applied correctly in both languages. Fig. 1 now uses `architectural/functional separation`, and the KBS-risk mitigation states that the architectural/functional separation and differentiated role of each evaluation must be made explicit. The unauthorized causal terminology is no longer present in the corrected contexts.

```text
0D_M01 = CLOSED
```

### 3. Preserved decisions

V02 materially preserves the V01 architecture, journal ranking, RQ states, tables/figures, draftability matrix, frozen numerical evidence, Group-3 dependency, C10/C11 restriction, risk assessment, and closing state. No unauthorized scope expansion or experimental reinterpretation was identified.

The journal recommendation remains:

```text
PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems
ALTERNATIVE_TARGET_1 = Expert Systems with Applications
ALTERNATIVE_TARGET_2 = Information Processing & Management
```

This remains an editorial recommendation pending author approval, not a final journal selection.

### 4. Phase-0 gate

```text
PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS
```

The V02 terminology correction is closed. The remaining conditions are downstream constraints rather than V02 defects: C10/C11 must be reconciled before EXP-11B article use; Group 3 must close before final RQ4 and HE2/HE5 inference; final gap/novelty remain undeclared; and exact target-journal author-guide requirements must be rechecked before submission.

### 5. Experimental review and resulting state

No new experimental interpretation is introduced.

```text
EXPERIMENTAL_REVIEW = NOT_REQUIRED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
0D = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
AUTHOR_APPROVAL = PENDING
FREEZE_0D = NOT_AUTHORIZED_YET
PHASE_1 = BLOCKED_UNTIL_0D_AND_PHASE_0_CLOSE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

No further return to the Writing AI is required.