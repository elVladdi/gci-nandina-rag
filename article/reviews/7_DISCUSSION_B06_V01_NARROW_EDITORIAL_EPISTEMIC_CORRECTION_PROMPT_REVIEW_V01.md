# Internal review — B06 V02 narrow editorial/epistemic correction prompt V01

## Español

```text
REVIEW = 7_DISCUSSION_B06_V01_NARROW_EDITORIAL_EPISTEMIC_CORRECTION_PROMPT_REVIEW_V01
PROMPT = article/prompts/7_DISCUSSION_B06_V01_NARROW_EDITORIAL_EPISTEMIC_CORRECTION.md@bfa366448a558f63ba2c5e6f0062ed895ebb910a
PROMPT_GIT_BLOB = bc0d79d1827d8950acb2562bc1e12238b031804a
SOURCE_AUDIT = article/reviews/7_DISCUSSION_B06_SECTION6_6_INTERNAL_REVIEW_V01.md@773382c56ebcb96b7f6b29a0ba82fc1529cf5a51
GOVERNANCE_GATE = D-147
VERDICT = PASS
MANDATORY_CORRECTIONS = NONE
READY_FOR_EXECUTION_AUTHORIZATION = YES
```

### Revisión de alcance

El prompt limita correctamente la intervención a §6.6 EN/ES y usa como inputs los candidatos B06 V01 exactos:

```text
INPUT_MD_SHA256 = c73518750ac9faff5e69eca3f5e363ef386efd0ac78969315b9dedf4ce7ec2e1
INPUT_MD_GIT_BLOB = 20028e1c0e9fc8fe9c98b1b1bf3f00b3cf95fef7
INPUT_DOCX_SHA256 = 3859c8686679777d64910839842b4a771befb84dca715e1054a524fa52c75d27
INPUT_DOCX_COMMENTS = 48
INPUT_DOCX_TRACKED_CHANGES = 0
INPUT_DOCX_PAGE_COUNT = 69
```

El prompt prohíbe modificar §§1–6.5, la deuda editorial de §6.2, Conclusion, References y end matter.

### Revisión de correcciones obligatorias

Las cuatro correcciones ordenadas por la auditoría V01 están representadas sin ampliar scope:

1. lenguaje no causal para la sensibilidad correctiva documental;
2. sustitución de `frozen case-level operationalization` por preespecificación reader-facing;
3. sustitución de `canonical runner` y `frozen Chapter-87 reference configuration` por terminología pública de reproducibilidad;
4. naturalización de la frase sobre ausencia de validación para deployment operativo.

La corrección mantiene explícitamente `METHOD_DEPENDENT`, `NOT_ESTIMABLE`, `INCONCLUSIVE`, ausencia de generalización externa, `LLM-as-judge != human validation`, `configurability != empirical generalization` y todas las demás fronteras D-145.

### Revisión de gobernanza y entrega

El prompt incluye START_HERE, MWDP v1.0, SPCCR v1.0, KBS_EWG_34_V01, D-022, D-027, D-035, D-136, D-144, D-145, D-146, la response B06 V01, la auditoría V01 y D-147. Preserva la prohibición de reconstruir Word desde Markdown, exige 48 comentarios, 0 tracked changes, auditoría OOXML y render completo.

No autoriza nueva literatura, citas, resultados, cálculos, inferencias, causalidad, novelty, SOTA, superioridad, legal correctness, human validation, deployment readiness ni Conclusion.

### Veredicto

```text
SCOPE_CONTROL = PASS
BASELINE_IDENTITIES = PASS
SCIENTIFIC_BOUNDARY = PASS
D136_CONTROL = PASS
MWDP_WORD_DELIVERY = PASS
BILINGUAL_CONTROL = PASS
CONCLUSION_GATE = CLOSED
VERDICT = PASS
MANDATORY_CORRECTIONS = NONE
```

---

## English

The narrow B06 V02 correction prompt accurately implements the V01 audit findings without expanding scientific scope. It is protocol-complete, anchored to exact B06 V01 candidate identities, preserves all prior sections and the Conclusion placeholder, and is ready for execution authorization.
