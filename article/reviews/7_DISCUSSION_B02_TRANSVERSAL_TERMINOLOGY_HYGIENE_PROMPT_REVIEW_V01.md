# Internal review — Discussion B02 transversal terminology-hygiene prompt V01

## Español

```text
REVIEW_TARGET = article/prompts/7_DISCUSSION_B02_TRANSVERSAL_TERMINOLOGY_HYGIENE_V01.md
REVIEW_TARGET_GIT_BLOB = 5f400230bec46bb737f92db00a50ba2ec7f3d80c
SCIENTIFIC_BOUNDARY = D-152
CANONICAL_BASELINE = ARTICLE_MASTER_V029
WORD_BASELINE = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V02.docx
VERDICT = PASS
MANDATORY_CORRECTIONS = NONE
```

### Auditoría

El prompt limita correctamente la intervención a §6.2 EN/ES y prohíbe reescritura científica, nuevos resultados, inferencia, literatura, citas, novelty, generalización, legal correctness y Conclusion. Los baselines están identificados de forma exacta y el Word debe editarse directamente, en conformidad con D-027/D-035.

Las seis correcciones terminológicas corresponden exactamente a la deuda registrada: `frozen` usado como etiqueta de gobernanza, el nombre interno `advertencias_globales`, `micro-audit`, el diagnóstico `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`, el identificador `independent_ai_reviewer_01`, el rol `AI_EXPERT_ROLE` y jerga operacional local. El prompt obliga a preservar las cifras de evaluación, la condición LLM-as-judge, la ausencia de validación humana, los límites de traceability/auditability y el contrato de autoridad del LLM.

La intervención no permite alterar las citas existentes a Marra de Artiñano et al. (2023) y Kim et al. (2025), ni mover comentarios. El control de D-136, SPCCR, KBS, equivalencia EN/ES, OOXML y render está explicitado. No se detecta contradicción con D-151/D-152 ni ampliación de scope.

```text
SCOPE_PRECISION = PASS
SCIENTIFIC_FIDELITY_CONTROLS = PASS
EPISTEMIC_BOUNDARY = PASS
INTERNAL_TERMINOLOGY_TARGETING = PASS
CITATION_PRESERVATION = PASS
BILINGUAL_CONTROL = PASS
DOCX_OOXML_CONTROL = PASS
D022_D027_D035 = PASS
CONCLUSION_GUARD = PASS
PROMPT_READY_FOR_EXECUTION = YES
```

---

## English

The prompt passes internal review. It is narrowly restricted to Section 6.2 terminology hygiene, preserves the approved scientific content and citations, targets only the logged D-136 terminology debt, and includes the required bilingual, OOXML, comment-anchor, render, and handoff controls. No mandatory prompt correction is required.